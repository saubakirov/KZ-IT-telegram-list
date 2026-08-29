import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import sync_kz_commands as sync


class CommandContractTests(unittest.TestCase):
    def test_repository_inventory_metadata_completeness_and_parity(self):
        self.assertEqual(sync.run(False), [])
        self.assertEqual(sync.inventory(), (set(sync.NAMES), set(sync.NAMES)))
        for name in sync.NAMES:
            source, target = sync.paths(name)
            body = source.read_bytes()
            self.assertEqual(body, target.read_bytes())
            self.assertEqual(sync.metadata(body.decode())["name"], name)
            self.assertEqual(sync.validate(name, body), [])
            text = body.decode()
            self.assertIn("$ARGUMENTS", text)
            for section in sync.SECTIONS:
                self.assertEqual(text.count(section), 1)

    def test_check_is_non_mutating_and_reports_drift_extra_and_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            claude, codex = root / "claude", root / "codex"
            claude.mkdir(); codex.mkdir()
            for name in sync.NAMES:
                source, _ = sync.paths(name)
                (claude / f"{name}.md").write_bytes(source.read_bytes())
            with patch.object(sync, "CLAUDE", claude), patch.object(sync, "CODEX", codex):
                self.assertEqual(sync.run(True), [])
                before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
                self.assertEqual(sync.run(False), [])
                self.assertEqual(before, {path: path.read_bytes() for path in root.rglob("*") if path.is_file()})
                (codex / "kz-add" / "SKILL.md").write_text("drift", encoding="utf-8")
                self.assertTrue(any("parity" in error for error in sync.run(False)))
                (codex / "kz-extra").mkdir()
                (codex / "kz-extra" / "SKILL.md").write_text("extra", encoding="utf-8")
                self.assertTrue(any("inventory" in error for error in sync.run(False)))
                (claude / "kz-release.md").unlink()
                self.assertTrue(any("missing" in error for error in sync.run(False)))

    def test_thin_or_location_dependent_body_fails(self):
        body = ("---\nname: kz-add\ndescription: x\n---\n"
                "See ../../workflow.\n").encode()
        errors = sync.validate("kz-add", body)
        self.assertTrue(any("section" in error for error in errors))
        self.assertTrue(any("forbidden" in error for error in errors))

    def test_sync_direction_is_claude_to_codex(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            claude, codex = root / "claude", root / "codex"
            claude.mkdir(); codex.mkdir()
            for name in sync.NAMES:
                source, _ = sync.paths(name)
                (claude / f"{name}.md").write_bytes(source.read_bytes())
            with patch.object(sync, "CLAUDE", claude), patch.object(sync, "CODEX", codex):
                self.assertEqual(sync.run(True), [])
                for name in sync.NAMES:
                    self.assertEqual((claude / f"{name}.md").read_bytes(),
                                     (codex / name / "SKILL.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
