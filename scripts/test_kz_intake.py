import json
import copy
import shutil
import tempfile
import unittest
from argparse import Namespace
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from scripts import kz_intake as intake
from scripts import validate_links
from scripts import validate_schema


class SourceTests(unittest.TestCase):
    def test_lossless_closed_grammar_and_grouping(self):
        values = [
            "https://t.me/Valid_Name", "https://telegram.me/valid_name/",
            "https://telegram.dog/VALID_NAME).", "http://t.me/valid_name",
            "https://t.me./valid_name",
            "https://www.t.me/valid_name", "https://t.me.evil/valid_name",
            "https://user@t.me/valid_name", "https://t.me:443/valid_name",
            "https://t.me/valid%5Fname", "https://t.me/+secret",
            "https://t.me/joinchat/secret", "https://t.me/valid_name/10",
            "https://t.me/valid_name?start=1", "https://t.me/valid_name#story",
            "https://t.me/share/url?url=x", "tg://resolve?domain=valid_name",
            "https://evil.example/t.me/valid_name", "https://t.me/abc",
        ]
        source = intake.parse_source("Ω " + "\n".join(values), "fixture")
        self.assertEqual(source["totals"], {"occurrences": 19, "candidates": 1,
                                             "non_candidates": 16})
        self.assertEqual(len(source["candidates"][0]["occurrence_ids"]), 3)
        self.assertEqual(source["occurrences"][0]["byte_start"], 3)
        wrapped = source["occurrences"][2]
        self.assertEqual(wrapped["trimmed_suffix"], ").")
        self.assertEqual(bytes.fromhex(wrapped["raw_utf8_hex"]).decode(), wrapped["raw_text"])
        kinds = {row["link_kind"] for row in source["occurrences"]}
        self.assertTrue({"candidate", "unsupported_scheme", "spoofed_authority", "userinfo",
                         "port", "percent_encoded", "private_invite", "message_path",
                         "query_or_fragment", "reserved_action", "invalid_handle"} <= kinds)
        self.assertEqual(intake.classify_token("https://t.me./valid_name"),
                         ("spoofed_authority", None))
        for index, row in enumerate(source["occurrences"], 1):
            self.assertEqual(row["ordinal"], index)
            raw = ("Ω " + "\n".join(values)).encode()[row["byte_start"]:row["byte_end"]]
            self.assertEqual(raw, bytes.fromhex(row["raw_utf8_hex"]))

    def test_no_parent_or_prefix_salvage(self):
        source = intake.parse_source(
            "https://t.me/good_handle/5 https://t.me/good_handle?x=1 "
            "https://t.me/good_handle%2F5"
        )
        self.assertEqual(source["totals"]["candidates"], 0)
        self.assertEqual(source["totals"]["occurrences"], 3)

    def test_live_archive_and_cross_input_collisions_are_explicit(self):
        source = intake.parse_source("https://t.me/repeat_one https://telegram.me/REPEAT_ONE")
        catalog = {"groups": [], "channels": [], "bots": [],
                   "archive": [{"handle": "repeat_one"}]}
        result = intake.catalog_collisions(source, catalog)
        self.assertEqual(result[0]["status"], "archive")
        self.assertTrue(result[0]["cross_input_duplicate"])

    def test_file_utf8_and_exactly_one_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.txt"
            path.write_bytes(b"\xff")
            with self.assertRaises(intake.IntakeError):
                intake._source(Namespace(text=None, file=path))
        parser = intake.parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["parse"])
        with self.assertRaises(SystemExit):
            parser.parse_args(["parse", "--text", "x", "--file", "x"])


class ObservationTests(unittest.TestCase):
    def preview(self, canonical="SamplePeer", extra="123 members", action="Join Group"):
        return (f'<link rel="canonical" href="https://t.me/{canonical}">'
                f'<div class="tgme_page_title">Sample Community</div>'
                f'<div class="tgme_page_extra">{extra}</div>'
                f'<a class="tgme_action_button_new" href="https://t.me/{canonical}">{action}</a>')

    def test_fetch_once_and_exact_three_type_reconciliation(self):
        calls = []
        body = self.preview().encode()

        def fetch(handle):
            calls.append(handle)
            return validate_links.FetchResult(True, "fetched", body, 200, 1)

        result = intake.observe_candidate("SamplePeer", fetch, "2026-08-28")
        self.assertEqual(calls, ["SamplePeer"])
        self.assertEqual(result["status"], "verified")
        self.assertEqual(result["observed_type"], "groups")
        self.assertEqual(result["member_count"], 123)
        self.assertEqual([row["classification"] for row in result["type_results"]],
                         ["verified", "ambiguous", "ambiguous"])
        self.assertEqual(result["body_sha256"], intake.sha256_bytes(body))

    def test_conflict_dead_and_transport_fail_closed(self):
        cases = (
            validate_links.FetchResult(True, "fetched", self.preview("OtherPeer").encode(), 200, 1),
            validate_links.FetchResult(True, "fetched", b"This group or channel no longer exists", 200, 1),
            validate_links.FetchResult(False, "http_404", None, 404, 1),
        )
        for fetched in cases:
            with self.subTest(reason=fetched.reason):
                result = intake.observe_candidate("SamplePeer", lambda _handle: fetched, "2026-08-28")
                self.assertEqual(result["status"], "unresolved")
                self.assertIsNone(result["canonical_handle"])
                self.assertIsNone(result["member_count"])
                self.assertFalse(result["target_bound"])
                intake.validate_observation(result)

    def test_transport_retry_contract_and_existing_wrapper(self):
        body = self.preview().encode()

        class Response:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *_args): return False
            def read(self): return body

        limited = HTTPError("https://t.me/SamplePeer", 429, "rate", None, None)
        with patch.object(validate_links, "urlopen", side_effect=[limited, Response()]), \
                patch.object(validate_links.time, "sleep") as sleep:
            fetched = validate_links.fetch_preview_with_retry("SamplePeer")
        self.assertEqual((fetched.ok, fetched.body, fetched.attempts), (True, body, 2))
        sleep.assert_called_once_with(2.0)
        with patch.object(validate_links, "urlopen", side_effect=URLError("offline")), \
                patch.object(validate_links.time, "sleep") as sleep:
            failed = validate_links.fetch_preview_with_retry("SamplePeer")
        self.assertEqual((failed.ok, failed.reason, failed.attempts),
                         (False, "url_error:offline", 3))
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1.0, 2.0])
        with patch.object(validate_links, "fetch_preview_with_retry",
                          return_value=validate_links.FetchResult(True, "fetched", body, 200, 1)):
            result = validate_links.check_link_with_retry("SamplePeer", "groups")
        self.assertEqual(result["classification"], "verified")


class CanonicalTests(unittest.TestCase):
    def test_closed_lexical_profile(self):
        invalid = (
            '{"a":1,"a":2}', '{"a":-0}', '{"a":1.0}', '{"a":1e2}',
            '{"a":9007199254740992}', '{"é":1}', '{"a":"\\ud800"}', '{"a":NaN}',
        )
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(intake.IntakeError):
                intake.parse_closed_json(text)
        value = intake.parse_closed_json('{"z":"Ж","a":1}')
        self.assertEqual(intake.canonical_bytes(value), '{"a":1,"z":"Ж"}\n'.encode())

    def test_exact_integer_type_excludes_boolean_recursively(self):
        intake._exact(1, int)
        intake._exact(None, (int, type(None)))
        for value, schema in ((True, int), (False, (int, type(None)))):
            with self.subTest(value=value, schema=schema), self.assertRaises(intake.IntakeError):
                intake._exact(value, schema)


class PreviewApplyTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.root, self.stage = base / "root", base / "stage"
        self.root.mkdir(); self.stage.mkdir()
        self._write_tree(self.root, False)
        self._write_tree(self.stage, True)
        self.preview = self._preview()
        self.approval = self._approval(self.preview)
        self.pending = base / "pending.json"

    def tearDown(self):
        self.temporary.cleanup()

    def _catalog(self, added):
        entry = {"name": "Sample Community", "handle": "sample_peer",
                 "description": "English", "description_ru": "Русский",
                 "description_kk": "Қазақша", "category": "general",
                 "last_verified": date.today().isoformat(), "member_count": 42}
        return {"categories": {"general": {"name": "General"}},
                "archive": [], "groups": [entry] if added else [], "channels": [], "bots": []}

    def _write_tree(self, root, added):
        for path in intake.CONTROLLED_PATHS:
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            body = json.dumps(self._catalog(added), ensure_ascii=False).encode() if path.startswith("data/") \
                else f"{'after' if added else 'before'}:{path}\n".encode()
            target.write_bytes(body)

    def _observation(self, stale=False):
        typed = [
            validate_links.result("verified", "target_preview_verified", "groups", 42,
                                  "Sample Community", "groups", True),
            validate_links.result("ambiguous", "declared_type_mismatch", "channels", None,
                                  "Sample Community", "groups", True),
            validate_links.result("ambiguous", "declared_type_mismatch", "bots", None,
                                  "Sample Community", "groups", True),
        ]
        return {"candidate_id": "candidate:sample_peer", "requested_handle": "sample_peer",
                "status": "verified", "reason": "one_verified_two_bound_mismatches",
                "canonical_handle": "sample_peer", "observed_type": "groups",
                "visible_name": "Sample Community", "member_count": 42, "target_bound": True,
                "observed_at": (date.today() - timedelta(days=1) if stale else date.today()).isoformat(),
                "source_classification": "public_telegram_preview", "body_sha256": "a" * 64,
                "transport": {"ok": True, "reason": "fetched", "status_code": 200, "attempts": 1},
                "type_results": typed}

    def _preview(self, stale=False):
        source = intake.parse_source("https://t.me/sample_peer")
        candidate_id = source["candidates"][0]["candidate_id"]
        collisions = [{"candidate_id": candidate_id, "status": "clear", "matched_handles": [],
                       "cross_input_duplicate": False}]
        editorial = [{"candidate_id": candidate_id, "it_relevant": True,
                      "kazakhstan_relevant": True, "purely_commercial": False,
                      "category_valid": True, "locales_complete": True,
                      "evidence_refs": ["evidence/editorial.md"]}]
        proposed = {"type": "groups", "name": "Sample Community", "handle": "sample_peer",
                    "description": "English", "description_ru": "Русский",
                    "description_kk": "Қазақша", "category": "general",
                    "last_verified": self._observation(stale)["observed_at"], "member_count": 42}
        actions = [{"candidate_id": candidate_id, "action": "add", "reason": "all gates pass",
                    "proposed_entry": proposed}]
        with patch.object(intake, "validate_action_stage", return_value=intake.path_hashes(self.stage)):
            return intake.build_preview(source, collisions, [self._observation(stale)], editorial,
                                        actions, self.root, self.stage)

    def _approval(self, preview):
        return {"schema_version": intake.APPROVAL_VERSION,
                "canonical_profile": intake.CANONICAL_PROFILE,
                "payload_sha256": intake.preview_sha256(preview),
                "actions_sha256": intake.actions_sha256(preview["actions"]),
                "approved_candidate_ids": ["candidate:sample_peer"], "owner_handle": "owner",
                "owner_evidence_ref": "owner-event-1", "approved_at": date.today().isoformat()}

    def _apply(self, preview=None, approval=None, fail_after=None):
        with patch.object(intake, "validate_action_stage", return_value=intake.path_hashes(self.stage)):
            return intake.apply_preview(
                self.root, self.stage, preview or self.preview, approval or self.approval,
                {"owner-event-1"}, self.pending, lambda _stage: ["schema", "currency"], fail_after,
            )

    def test_preview_render_schema_and_tamper(self):
        rendered = intake.render_preview(self.preview)
        self.assertIn("Exact significant payload", rendered)
        self.assertIn(intake.canonical_bytes(self.preview).decode().strip(), rendered)
        tampered = json.loads(json.dumps(self.preview))
        tampered["hidden"] = True
        with self.assertRaises(intake.IntakeError):
            intake.validate_preview(tampered)
        tampered = json.loads(json.dumps(self.preview))
        tampered["totals"]["add"] = 0
        with self.assertRaises(intake.IntakeError):
            intake.validate_preview(tampered)
        tampered = json.loads(json.dumps(self.preview))
        tampered["source"]["candidates"][0]["occurrence_ids"] = ["occurrence:9999"]
        with self.assertRaises(intake.IntakeError):
            intake.validate_preview(tampered)

    def test_recursive_integer_editorial_and_transport_constraints(self):
        intake.validate_preview(self.preview)
        for field_path in (("totals", "add"), ("source", "totals", "occurrences")):
            tampered = json.loads(json.dumps(self.preview))
            target = tampered
            for key in field_path[:-1]:
                target = target[key]
            target[field_path[-1]] = True
            with self.subTest(field_path=field_path), self.assertRaises(intake.IntakeError):
                intake.validate_preview(tampered)
        for reference in ("", " \t "):
            tampered = json.loads(json.dumps(self.preview))
            tampered["editorial"][0]["evidence_refs"] = [reference]
            with self.subTest(reference=reference), self.assertRaisesRegex(
                    intake.IntakeError, "non-blank"):
                intake.validate_preview(tampered)
        tampered = json.loads(json.dumps(self.preview))
        tampered["observations"][0]["transport"]["ok"] = False
        with self.assertRaisesRegex(intake.IntakeError, "failed transport"):
            intake.validate_preview(tampered)

    def test_impossible_classifier_and_transport_tuples_are_rejected(self):
        paths = (
            ("type_results", 0, "target_bound", False),
            ("type_results", 0, "reason", "arbitrary"),
            ("type_results", 0, "observed_type", "channels"),
            ("type_results", 1, "visible_name", "Other"),
            ("transport", "status_code", None),
            ("body_sha256", None),
            ("canonical_handle", "other_peer"),
            ("reason", "arbitrary"),
        )
        for path in paths:
            tampered = json.loads(json.dumps(self.preview))
            target = tampered["observations"][0]
            for key in path[:-2]:
                target = target[key]
            target[path[-2]] = path[-1]
            with self.subTest(path=path), self.assertRaises(intake.IntakeError):
                intake.validate_preview(tampered)
        tampered = json.loads(json.dumps(self.preview))
        tampered["observations"][0]["type_results"][0]["reason"] = "arbitrary"
        approval = dict(self.approval)
        approval["payload_sha256"] = intake.sha256_bytes(intake.canonical_bytes(tampered))
        with self.assertRaises(intake.IntakeError):
            self._apply(tampered, approval)
        failed = json.loads(json.dumps(self.preview))
        observation = failed["observations"][0]
        observation["status"] = "unresolved"; observation["reason"] = "http_500"
        observation["canonical_handle"] = observation["observed_type"] = None
        observation["visible_name"] = observation["member_count"] = None
        observation["target_bound"] = False
        observation["transport"] = {"ok": False, "reason": "http_500", "status_code": 500, "attempts": 1}
        with self.assertRaisesRegex(intake.IntakeError, "failed transport"):
            intake.validate_preview(failed)
        failed["observations"][0]["body_sha256"] = None
        failed["observations"][0]["type_results"] = []
        failed["observations"][0]["transport"]["reason"] = "arbitrary"
        with self.assertRaisesRegex(intake.IntakeError, "failed transport"):
            intake.validate_preview(failed)
        for field, value in (("type", "channels"), ("handle", "other_peer"), ("name", "Other")):
            tampered = json.loads(json.dumps(self.preview))
            tampered["actions"][0]["proposed_entry"][field] = value
            with self.subTest(proposed=field), self.assertRaisesRegex(intake.IntakeError, "observation"):
                intake.validate_preview(tampered)

    def test_approval_binds_payload_actions_exact_set_and_owner_record(self):
        for field, value in (("payload_sha256", "0" * 64), ("actions_sha256", "0" * 64),
                             ("approved_candidate_ids", [])):
            approval = dict(self.approval); approval[field] = value
            with self.assertRaises(intake.IntakeError):
                intake.validate_approval(self.preview, approval, {"owner-event-1"})
        with self.assertRaises(intake.IntakeError):
            intake.validate_approval(self.preview, self.approval, set())


    def test_apply_exact_noop_and_unknown_stop(self):
        receipt = self._apply()
        self.assertEqual(receipt["outcome"], "applied_exact")
        self.assertFalse(self.pending.exists())
        self.assertEqual(self._apply()["outcome"], "already_applied_exact")
        (self.root / "README.md").write_text("unknown", encoding="utf-8")
        with self.assertRaises(intake.IntakeError):
            self._apply()

    def test_equal_paths_are_neutral_for_first_apply_and_exact_rerun(self):
        neutral_path = "README.md"
        (self.stage / neutral_path).write_bytes((self.root / neutral_path).read_bytes())
        preview = self._preview()
        approval = self._approval(preview)
        first = self._apply(preview, approval)
        self.assertEqual(first["outcome"], "applied_exact")
        self.assertEqual(first["before_state"][intake.CONTROLLED_PATHS.index(neutral_path)], "N")
        self.assertEqual(self._apply(preview, approval)["outcome"], "already_applied_exact")

    def test_equal_path_remains_neutral_during_marked_recovery(self):
        neutral_path = "README.md"
        (self.stage / neutral_path).write_bytes((self.root / neutral_path).read_bytes())
        preview = self._preview()
        approval = self._approval(preview)
        with self.assertRaisesRegex(RuntimeError, "injected"):
            self._apply(preview, approval, fail_after=1)
        self.assertTrue(self.pending.exists())
        receipt = self._apply(preview, approval)
        self.assertEqual(receipt["outcome"], "recovered_exact")
        self.assertEqual(receipt["before_state"][intake.CONTROLLED_PATHS.index(neutral_path)], "N")

    def test_wholly_unchanged_stage_is_exact_noop_and_unknown_still_stops(self):
        self._write_tree(self.stage, False)
        preview = self._preview()
        approval = self._approval(preview)
        with self.assertRaisesRegex(intake.IntakeError, "catalog"):
            intake.apply_preview(self.root, self.stage, preview, approval,
                                 {"owner-event-1"}, self.pending, lambda _stage: [])
        (self.root / "README.md").write_text("unknown", encoding="utf-8")
        with self.assertRaises(intake.IntakeError):
            self._apply(preview, approval)

    def test_marked_recovery_and_unmarked_or_corrupt_mixture_stop(self):
        with self.assertRaisesRegex(RuntimeError, "injected"):
            self._apply(fail_after=2)
        self.assertTrue(self.pending.exists())
        self.assertEqual(self._apply()["outcome"], "recovered_exact")
        self._write_tree(self.root, False)
        (self.root / intake.CONTROLLED_PATHS[0]).write_bytes(
            (self.stage / intake.CONTROLLED_PATHS[0]).read_bytes())
        with self.assertRaises(intake.IntakeError):
            self._apply()
        self.pending.write_text('{"wrong":true}', encoding="utf-8")
        with self.assertRaises(intake.IntakeError):
            self._apply()

    def test_stale_collision_and_staged_tamper_stop_before_write(self):
        stale = self._preview(stale=True)
        with self.assertRaisesRegex(intake.IntakeError, "not fresh"):
            self._apply(stale, self._approval(stale))
        (self.stage / "README.md").write_text("tampered", encoding="utf-8")
        with self.assertRaisesRegex(intake.IntakeError, "staged bytes"):
            self._apply()
        self._write_tree(self.stage, True)
        self._write_tree(self.root, True)
        collision_preview = self._preview()
        with self.assertRaisesRegex(intake.IntakeError, "catalog|collides"):
            self._apply(collision_preview, self._approval(collision_preview))

    def test_preflight_failure_precedes_marker_and_replacement(self):
        before = intake.path_hashes(self.root)
        def fail(_stage):
            raise intake.IntakeError("schema failed")
        with patch.object(intake, "validate_action_stage", return_value=intake.path_hashes(self.stage)), \
                self.assertRaisesRegex(intake.IntakeError, "schema failed"):
            intake.apply_preview(self.root, self.stage, self.preview, self.approval,
                                 {"owner-event-1"}, self.pending, fail)
        self.assertEqual(intake.path_hashes(self.root), before)
        self.assertFalse(self.pending.exists())


class ActionStageBindingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.root, self.stage = base / "root", base / "stage"
        project = Path(__file__).parent.parent
        for destination in (self.root, self.stage):
            for path in intake.CONTROLLED_PATHS:
                target = destination / path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(project / path, target)
        (self.stage / "scripts").mkdir()
        for name in ("validate_schema.py", "generate_readme.py"):
            shutil.copyfile(project / "scripts" / name, self.stage / "scripts" / name)
        self.baseline = json.loads((self.root / "data/communities.json").read_text(encoding="utf-8"))
        self.bundle = self._bundle()

    def tearDown(self):
        self.temporary.cleanup()

    def _bundle(self, action="add"):
        source = intake.parse_source("https://t.me/synthetic_peer", "synthetic")
        candidate_id = source["candidates"][0]["candidate_id"]
        typed = [
            validate_links.result("verified" if kind == "groups" else "ambiguous",
                                  "target_preview_verified" if kind == "groups" else "declared_type_mismatch",
                                  kind, 7 if kind == "groups" else None, "Synthetic Peer", "groups", True)
            for kind in validate_links.ENTRY_TYPES
        ]
        observation = {"candidate_id": candidate_id, "requested_handle": "synthetic_peer",
                       "status": "verified", "reason": "one_verified_two_bound_mismatches",
                       "canonical_handle": "synthetic_peer", "observed_type": "groups",
                       "visible_name": "Synthetic Peer", "member_count": 7, "target_bound": True,
                       "observed_at": date.today().isoformat(),
                       "source_classification": "public_telegram_preview", "body_sha256": "b" * 64,
                       "transport": {"ok": True, "reason": "fetched", "status_code": 200, "attempts": 1},
                       "type_results": typed}
        proposed = {"type": "groups", "name": "Synthetic Peer", "handle": "synthetic_peer",
                    "description": "Synthetic fixture", "description_ru": "Synthetic RU",
                    "description_kk": "Synthetic KK", "category": next(iter(self.baseline["categories"])),
                    "last_verified": date.today().isoformat(), "member_count": 7}
        return {"source": source,
                "collisions": [{"candidate_id": candidate_id, "status": "clear", "matched_handles": [],
                                "cross_input_duplicate": False}],
                "observations": [observation],
                "editorial": [{"candidate_id": candidate_id, "it_relevant": True,
                               "kazakhstan_relevant": True, "purely_commercial": False,
                               "category_valid": True, "locales_complete": True,
                               "evidence_refs": ["synthetic:editorial"]}],
                "actions": [{"candidate_id": candidate_id, "action": action, "reason": "synthetic",
                             "proposed_entry": proposed if action == "add" else None}]}

    def _write_stage(self, data, stale_projection=False):
        (self.stage / "data/communities.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        outputs = intake.generate_readme.generated_outputs(data)
        for path in intake.CONTROLLED_PATHS[1:]:
            (self.stage / path).write_text(outputs[intake.generate_readme.PROJECT_ROOT / path],
                                           encoding="utf-8", newline="\n")
        if stale_projection:
            shutil.copyfile(self.root / "README.md", self.stage / "README.md")

    def _exact_add_data(self):
        data = copy.deepcopy(self.baseline)
        proposed = dict(self.bundle["actions"][0]["proposed_entry"])
        data[proposed.pop("type")].append(proposed)
        return data

    def test_reject_only_cannot_bind_unrelated_real_valid_delta(self):
        data = copy.deepcopy(self.baseline)
        data["groups"][0]["description"] += " (synthetic edit)"
        data["localization_review"]["payload_sha256"] = validate_schema.review_payload_sha256(data)
        self._write_stage(data)
        self.assertEqual(intake.validate_staged_project(self.stage),
                         ["scripts/validate_schema.py", "scripts/generate_readme.py --check"])
        with self.assertRaisesRegex(intake.IntakeError, "exactly baseline"):
            intake.build_preview(**self._bundle("reject"), root=self.root, stage_root=self.stage)

    def test_reject_only_exact_unchanged_stage_is_a_noop(self):
        preview = intake.build_preview(**self._bundle("reject"), root=self.root, stage_root=self.stage)
        approval = {"schema_version": intake.APPROVAL_VERSION,
                    "canonical_profile": intake.CANONICAL_PROFILE,
                    "payload_sha256": intake.preview_sha256(preview),
                    "actions_sha256": intake.actions_sha256(preview["actions"]),
                    "approved_candidate_ids": [], "owner_handle": "owner",
                    "owner_evidence_ref": "owner:synthetic", "approved_at": date.today().isoformat()}
        receipt = intake.apply_preview(self.root, self.stage, preview, approval, {"owner:synthetic"},
                                       self.stage.parent / "pending.json")
        self.assertEqual(receipt["outcome"], "already_applied_exact")

    def test_exact_add_is_bound_and_apply_accepts_only_its_generated_stage(self):
        self._write_stage(self._exact_add_data())
        preview = intake.build_preview(**self.bundle, root=self.root, stage_root=self.stage)
        approval = {"schema_version": intake.APPROVAL_VERSION,
                    "canonical_profile": intake.CANONICAL_PROFILE,
                    "payload_sha256": intake.preview_sha256(preview),
                    "actions_sha256": intake.actions_sha256(preview["actions"]),
                    "approved_candidate_ids": ["candidate:synthetic_peer"], "owner_handle": "owner",
                    "owner_evidence_ref": "owner:synthetic", "approved_at": date.today().isoformat()}
        receipt = intake.apply_preview(self.root, self.stage, preview, approval, {"owner:synthetic"},
                                       self.stage.parent / "pending.json", lambda _stage: ["synthetic"])
        self.assertEqual((receipt["outcome"], receipt["applied_candidate_ids"]),
                         ("applied_exact", ["candidate:synthetic_peer"]))

    def test_extra_edit_delete_reorder_wrong_type_field_and_stale_projection_stop(self):
        for case in ("extra", "edit", "delete", "reorder", "wrong_type", "proposed", "stale"):
            with self.subTest(case=case):
                data, bundle = self._exact_add_data(), copy.deepcopy(self.bundle)
                if case == "extra": data["groups"].append(dict(data["groups"][-1], handle="synthetic_extra"))
                elif case == "edit": data["groups"][0]["description"] += " edited"
                elif case == "delete": del data["groups"][0]
                elif case == "reorder": data["groups"][0], data["groups"][1] = data["groups"][1], data["groups"][0]
                elif case == "wrong_type": data["channels"].append(data["groups"].pop())
                elif case == "proposed": bundle["actions"][0]["proposed_entry"]["description"] = "Changed"
                self._write_stage(data, case == "stale")
                with self.assertRaises(intake.IntakeError):
                    intake.build_preview(**bundle, root=self.root, stage_root=self.stage)

    def test_owner_subset_requires_a_successor_preview(self):
        self._write_stage(self._exact_add_data())
        preview = intake.build_preview(**self.bundle, root=self.root, stage_root=self.stage)
        approval = {"schema_version": intake.APPROVAL_VERSION,
                    "canonical_profile": intake.CANONICAL_PROFILE,
                    "payload_sha256": intake.preview_sha256(preview),
                    "actions_sha256": intake.actions_sha256(preview["actions"]),
                    "approved_candidate_ids": [], "owner_handle": "owner",
                    "owner_evidence_ref": "owner:synthetic", "approved_at": date.today().isoformat()}
        with self.assertRaisesRegex(intake.IntakeError, "exact add set"):
            intake.validate_approval(preview, approval, {"owner:synthetic"})


if __name__ == "__main__":
    unittest.main()
