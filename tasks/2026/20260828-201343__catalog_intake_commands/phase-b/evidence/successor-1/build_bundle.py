#!/usr/bin/env python3
"""Reconcile all sealed Phase B candidates into one closed preview bundle."""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


BASELINE_CATALOG_SHA256 = "a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ADD = {
    "ai_qadam_kazakhstan": {
        "category": "ai",
        "description": "Kazakhstan chapter of AI Qadam for learning and applying artificial intelligence.",
        "description_ru": "Казахстанское отделение AI Qadam для изучения и практического применения искусственного интеллекта.",
        "description_kk": "Жасанды интеллектті үйренуге және іс жүзінде қолдануға арналған AI Qadam-ның Қазақстандағы қауымдастығы.",
        "topic": "The public description explicitly identifies a Kazakhstan AI chapter for newcomers and practitioners.",
        "commercial": "No sales offer or advertising purpose appears in the retained public description; risk is low.",
    },
    "allkzit": {
        "category": "general",
        "description": "Kazakhstan IT professionals' community for discussion and peer support.",
        "description_ru": "Сообщество IT-специалистов Казахстана для общения и взаимопомощи.",
        "description_kk": "Қазақстандағы IT мамандарының пікір алмасу және өзара көмек қауымдастығы.",
        "topic": "The target-bound public name explicitly identifies Kazakhstan IT professionals and the description links community rules.",
        "commercial": "The retained public preview exposes rules, not a sales or advertising offer; group content remains non-public and risk is medium-low.",
    },
    "anykeykz": {
        "category": "devops-sysadmin",
        "description": "Community for Kazakhstan helpdesk and junior system-administration specialists.",
        "description_ru": "Сообщество казахстанских эникейщиков и начинающих системных администраторов.",
        "description_kk": "Қазақстандағы техникалық қолдау және жүйелік әкімшілендіруді бастап жүрген мамандар қауымдастығы.",
        "topic": "The public name and description identify a Kazakhstan peer group for helpdesk staff progressing toward system administration.",
        "commercial": "No promotional or sales purpose is visible in the retained description; risk is low.",
    },
    "astana_hub": {
        "category": "startups",
        "description": "Official Astana Hub channel with Kazakhstan startup ecosystem news, programs, and events.",
        "description_ru": "Официальный канал Astana Hub с новостями, программами и событиями стартап-экосистемы Казахстана.",
        "description_kk": "Қазақстанның стартап экожүйесіндегі жаңалықтар, бағдарламалар мен іс-шаралар туралы Astana Hub-тың ресми арнасы.",
        "topic": "The official Astana Hub target publishes current Kazakhstan technology programs and events.",
        "commercial": "The retained evidence shows ecosystem information and support, not a product-sales-only feed; risk is low.",
    },
    "astanajkugoutputstream": {
        "category": "programming-languages",
        "description": "Announcements and learning resources from the Astana Java user group.",
        "description_ru": "Анонсы и учебные материалы сообщества Java-разработчиков Астаны.",
        "description_kk": "Астана Java пайдаланушылары тобының хабарландырулары мен оқу материалдары.",
        "topic": "The public description binds the channel to the Astana JKUG Java community and its current posts contain learning and event material.",
        "commercial": "Vacancy submissions are mentioned, but the retained feed is community/event oriented rather than purely commercial; risk is medium-low.",
    },
    "aws_kz": {
        "category": "devops-sysadmin",
        "description": "Announcements for the AWS User Group Kazakhstan community.",
        "description_ru": "Канал анонсов сообщества AWS User Group Kazakhstan.",
        "description_kk": "AWS User Group Kazakhstan қауымдастығының хабарландыру арнасы.",
        "topic": "The public description explicitly identifies the AWS User Group Kazakhstan announcement channel.",
        "commercial": "The retained description and current event posts are community announcements, not a sales-only feed; risk is low.",
    },
    "blockchainkz": {
        "category": "blockchain",
        "description": "Kazakhstan community for AI, blockchain, and digital-asset technology.",
        "description_ru": "Казахстанское сообщество по искусственному интеллекту, блокчейну и технологиям цифровых активов.",
        "description_kk": "Қазақстандағы жасанды интеллект, блокчейн және цифрлық активтер технологиялары қауымдастығы.",
        "topic": "The public description explicitly identifies a Kazakhstan AI and blockchain community; retained posts cover Kazakhstan digital-asset policy.",
        "commercial": "No sales-only purpose is visible in the retained evidence; risk is low.",
    },
    "devopskaz": {
        "category": "devops-sysadmin",
        "description": "Kazakhstan DevOps channel covering cloud infrastructure, Linux, CI/CD, and high-load systems.",
        "description_ru": "Казахстанский DevOps-канал об облачной инфраструктуре, Linux, CI/CD и высоконагруженных системах.",
        "description_kk": "Бұлттық инфрақұрылым, Linux, CI/CD және жоғары жүктемелі жүйелер туралы қазақстандық DevOps арнасы.",
        "topic": "The target-bound KazDevOps identity and public description explicitly cover DevOps, cloud, Linux, CI/CD, and high-load systems.",
        "commercial": "The description includes support and advertising contacts, but the current feed is not sales-only; promotional risk is medium.",
    },
    "devs_kz": {
        "category": "jobs",
        "description": "Kazakhstan IT careers, workshops, meetups, and professional-development channel.",
        "description_ru": "Канал об IT-карьере, воркшопах, митапах и профессиональном развитии в Казахстане.",
        "description_kk": "Қазақстандағы IT мансабы, воркшоптар, митаптар және кәсіби даму туралы арна.",
        "topic": "The public description explicitly covers Kazakhstan IT careers, workshops, and meetups.",
        "commercial": "Advertising and a course are disclosed, but the retained description and feed also contain broader career and professional content; risk is medium.",
    },
    "digitalbussinesskz": {
        "category": "news",
        "description": "Kazakhstan technology and business publication covering IT, startups, and digital products.",
        "description_ru": "Казахстанское издание о технологиях и бизнесе, освещающее IT, стартапы и цифровые продукты.",
        "description_kk": "IT, стартаптар және цифрлық өнімдер туралы жазатын қазақстандық технология және бизнес басылымы.",
        "topic": "The public description explicitly covers Kazakhstan business, technology, startups, and IT, with current visible posts.",
        "commercial": "This is a professional publication rather than a community chat, but the retained feed is editorial content, not a sales-only channel; risk is medium-low.",
    },
    "ethkz": {
        "category": "devops-sysadmin",
        "description": "Kazakhstan networking community for routing, wireless, VPN, and network equipment.",
        "description_ru": "Казахстанское сетевое сообщество о маршрутизации, беспроводных сетях, VPN и сетевом оборудовании.",
        "description_kk": "Маршруттау, сымсыз желілер, VPN және желілік жабдықтар жөніндегі Қазақстан қауымдастығы.",
        "topic": "The target identity uses the .kz/KZ marker and the public description is specifically about networking protocols and equipment.",
        "commercial": "No sales or advertising purpose is visible in the retained description; risk is low.",
    },
    "go_kz_vacancy": {
        "category": "jobs",
        "description": "Go developer vacancies in Kazakhstan and international roles relevant to the local community.",
        "description_ru": "Вакансии Go-разработчиков в Казахстане и зарубежные позиции для местного сообщества.",
        "description_kk": "Қазақстандағы Go әзірлеушілеріне және жергілікті қауымдастыққа қатысты халықаралық бос орындар.",
        "topic": "The public description explicitly identifies Go developer vacancies in Kazakhstan and links the local Go community.",
        "commercial": "Vacancies are the declared catalog-relevant purpose; no unrelated sales or spam signal appears in retained evidence; risk is low.",
    },
    "hackathon_kz": {
        "category": "events",
        "description": "Hackathon news and event announcements in Kazakhstan.",
        "description_ru": "Новости и анонсы хакатонов в Казахстане.",
        "description_kk": "Қазақстандағы хакатон жаңалықтары мен іс-шаралар хабарландырулары.",
        "topic": "The public description explicitly identifies Kazakhstan hackathon news and current event announcements.",
        "commercial": "Registration links serve the declared event purpose and no unrelated sales-only pattern appears; risk is low.",
    },
    "it_jobs_kz": {
        "category": "jobs",
        "description": "IT vacancies in Kazakhstan and worldwide, with salary ranges when available.",
        "description_ru": "IT-вакансии в Казахстане и мире с указанием вилки зарплаты, когда она доступна.",
        "description_kk": "Қазақстандағы және әлемдегі IT бос орындары; бар болса жалақы ауқымы көрсетіледі.",
        "topic": "The multilingual public description explicitly identifies IT vacancies in Kazakhstan and worldwide.",
        "commercial": "Vacancies are the declared catalog-relevant purpose; no unrelated sales-only signal appears in retained evidence; risk is low.",
    },
    "it_kazahstan": {
        "category": "news",
        "description": "News for Kazakhstan IT specialists, low-voltage systems professionals, and technology entrepreneurs.",
        "description_ru": "Новости для IT-специалистов, слаботочников и технологических предпринимателей Казахстана.",
        "description_kk": "Қазақстандағы IT мамандарына, әлсіз ток жүйелері мамандарына және технология кәсіпкерлеріне арналған жаңалықтар арнасы.",
        "topic": "The public description explicitly identifies Kazakhstan IT and low-voltage-system professionals, and current posts are technology news.",
        "commercial": "No sales-only purpose is stated and the retained current posts are informational; risk is medium-low.",
    },
    "kolesa_group": {
        "category": "general",
        "description": "Kolesa Group channel sharing Kazakhstan product-development experience, internships, and technology events.",
        "description_ru": "Канал Kolesa Group об опыте разработки продуктов в Казахстане, стажировках и технологических событиях.",
        "description_kk": "Kolesa Group-тың Қазақстандағы өнім әзірлеу тәжірибесі, тағылымдамалары және технологиялық іс-шаралары туралы арнасы.",
        "topic": "The public description identifies a Kazakhstan IT company sharing technical experience, internships, and events.",
        "commercial": "The source is corporate, but the declared and retained content includes technical knowledge and community opportunities rather than product sales only; risk is medium.",
    },
    "kz_bi_jobs": {
        "category": "jobs",
        "description": "Data analytics and business intelligence vacancies for Kazakhstan professionals.",
        "description_ru": "Вакансии в аналитике данных и Business Intelligence для специалистов Казахстана.",
        "description_kk": "Қазақстандағы деректер талдауы және Business Intelligence мамандарына арналған бос орындар.",
        "topic": "The target-bound KZ BI identity, linked local BI community, and current vacancy posts establish Kazakhstan data-career relevance.",
        "commercial": "Vacancies are the declared catalog-relevant purpose and posting rules are public; risk is low.",
    },
    "kz_bi_news": {
        "category": "data-analytics",
        "description": "Kazakhstan data analytics and business intelligence news, events, and community updates.",
        "description_ru": "Новости, события и обновления казахстанского сообщества аналитики данных и Business Intelligence.",
        "description_kk": "Қазақстандағы деректер талдауы мен Business Intelligence жаңалықтары, іс-шаралары және қауымдастық хабарлары.",
        "topic": "The public description explicitly identifies Kazakhstan data analytics and Business Intelligence news and events.",
        "commercial": "A workshop registration appears in retained posts, but the channel is broader community news and events rather than sales-only; risk is medium-low.",
    },
    "sandyq_orda": {
        "category": "news",
        "description": "News and analysis on B2B and B2G digitalization in Kazakhstan.",
        "description_ru": "Новости и аналитика о цифровизации B2B и B2G в Казахстане.",
        "description_kk": "Қазақстандағы B2B және B2G цифрландыру туралы жаңалықтар мен талдау.",
        "topic": "The public description and current posts explicitly cover B2B/B2G digitalization in Kazakhstan.",
        "commercial": "The retained feed is topical reporting, not a product-sales-only channel; risk is low.",
    },
    "tvkrg": {
        "category": "startups",
        "description": "Karaganda technology and startup hub channel for events, news, and networking.",
        "description_ru": "Канал технологического и стартап-хаба Караганды с событиями, новостями и нетворкингом.",
        "description_kk": "Қарағандыдағы технология және стартап хабының іс-шаралар, жаңалықтар және нетворкинг арнасы.",
        "topic": "The public name identifies IT and business in Karaganda; the description and current posts show hub events and networking.",
        "commercial": "The retained evidence is ecosystem programming and community events, not a sales-only feed; risk is low.",
    },
}


NON_ADD = {
    "helpfixit": {
        "action": "unresolved",
        "it": True,
        "kz": False,
        "commercial": False,
        "category": "devops-sysadmin",
        "reason": "Public evidence verifies a live computer-help group but contains no Kazakhstan audience or relevance signal; admission remains unresolved.",
    },
    "itbazarkzchannel": {
        "action": "duplicate",
        "it": True,
        "kz": True,
        "commercial": True,
        "category": "marketplace",
        "reason": "The public description points to live catalog group @itbazarkz and retained channel messages redirect to that group, so this advertising mirror is a canonical duplicate.",
    },
    "itqazaqstan": {
        "action": "reject",
        "it": True,
        "kz": True,
        "commercial": True,
        "category": "marketplace",
        "reason": "The public description centers paid service access, promotions, and integrator work; commercial/spam risk fails the non-commercial admission gate.",
    },
    "kazakhtelecom_official": {
        "action": "reject",
        "it": False,
        "kz": True,
        "commercial": True,
        "category": "news",
        "reason": "The target is an official telecom operator corporate feed, not an IT community or specialist resource; it fails community-scope and commerciality gates.",
    },
    "nfactorial_school": {
        "action": "reject",
        "it": True,
        "kz": True,
        "commercial": True,
        "category": "education",
        "reason": "The retained public description and recent posts are a school lead funnel with consultation and WhatsApp sales calls; it fails the purely-commercial gate.",
    },
    "qaz_qa_vacancies": {
        "action": "unresolved",
        "it": True,
        "kz": True,
        "commercial": False,
        "category": "jobs",
        "reason": "The target name and online count suggest Kazakhstan QA vacancies, but no public description or messages expose scope, rules, or spam risk; admission remains unresolved.",
    },
    "rootway": {
        "action": "unresolved",
        "it": True,
        "kz": False,
        "commercial": False,
        "category": "devops-sysadmin",
        "reason": "The public target is a live system-administration learning channel, but retained evidence contains no Kazakhstan audience or relevance signal; admission remains unresolved.",
    },
    "sysadm_in_job": {
        "action": "unresolved",
        "it": True,
        "kz": False,
        "commercial": False,
        "category": "jobs",
        "reason": "The public target is a live IT jobs group with rules, but no retained target evidence establishes Kazakhstan audience or relevance; admission remains unresolved.",
    },
}


RELATIONS = {
    "astanajkugoutputstream": "Distinct announcement/learning channel linked to live catalog group astanajug; different handle, type, and public function, so not an alias duplicate.",
    "devs_kz": "Distinct target from live catalog devkz: different handle, visible name, body hash, and career/workshop scope.",
    "go_kz_vacancy": "Distinct jobs channel linked to live catalog group go_kz; separate handle, type, and vacancy function.",
    "itbazarkzchannel": "Canonical mirror of live catalog group itbazarkz: description names the group and retained messages redirect to group posts.",
    "it_kazahstan": "Distinct from itqazaqstan: different canonical handles, response hashes, descriptions, and broad-news versus paid-integrator-service scope.",
    "itqazaqstan": "Distinct from IT_Kazahstan: different canonical handles, response hashes, descriptions, and paid-integrator-service versus broad-news scope.",
    "kz_bi_jobs": "Distinct vacancy channel linked to live catalog group kz_bi; separate handle, type, and jobs function.",
    "kz_bi_news": "Distinct news/events channel linked to live catalog group kz_bi; separate handle, type, and editorial function.",
    "sysadm_in_job": "Distinct jobs group within the SysAdm.in ecosystem; no same-target alias evidence, but Kazakhstan relevance remains unresolved.",
}


def public_text(public_row: dict[str, object]) -> tuple[str, str, list[str], str]:
    root = public_row["root"] if public_row["root"].get("ok") else public_row["public_stream"]
    extracted = root.get("extracted", {})
    meta = extracted.get("meta", {})
    text = extracted.get("text", {})
    description = text.get("tgme_page_description") or meta.get("og:description") or ""
    extra = text.get("tgme_page_extra") or ""
    stream = public_row["public_stream"].get("extracted", {})
    timestamps = stream.get("message_timestamps", [])
    activity = (
        f"latest public stream post {timestamps[-1]}" if timestamps
        else f"current public preview {extra}" if "online" in extra
        else "no public activity signal beyond liveness"
    )
    return description, extra, timestamps, activity


def main() -> int:
    root = Path.cwd()
    universe = Path(__file__).resolve().parent
    source = json.loads((universe / "ledger.json").read_text(encoding="utf-8"))
    probe = json.loads((universe / "observations.json").read_text(encoding="utf-8"))
    public = json.loads((universe / "editorial-public-evidence.json").read_text(encoding="utf-8"))
    catalog_path = root / "data" / "communities.json"
    if digest(catalog_path) != BASELINE_CATALOG_SHA256:
        raise SystemExit("production catalog baseline drift")
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    categories = set(catalog["categories"])
    kz_intake.validate_source(source)
    if probe["source"] != source:
        raise SystemExit("probe source differs from retained ledger")
    observations = probe["observations"]
    for observation in observations:
        kz_intake.validate_observation(observation)
        if observation["status"] != "verified" or not observation["target_bound"]:
            raise SystemExit(f"candidate not mechanically verified: {observation['candidate_id']}")
    if len(observations) != 28 or source["totals"] != {
        "occurrences": 29, "candidates": 28, "non_candidates": 0
    }:
        raise SystemExit("universe totals differ")

    collisions = kz_intake.catalog_collisions(source, catalog)
    collision_by_id = {row["candidate_id"]: row for row in collisions}
    observation_by_id = {row["candidate_id"]: row for row in observations}
    public_by_id = {row["candidate_id"]: row for row in public["candidates"]}
    candidate_by_id = {row["candidate_id"]: row for row in source["candidates"]}
    editorial: list[dict[str, object]] = []
    actions: list[dict[str, object]] = []
    judgements: list[dict[str, object]] = []

    expected_handles = set(ADD) | set(NON_ADD)
    actual_handles = {row["handle"].casefold() for row in source["candidates"]}
    if expected_handles != actual_handles:
        raise SystemExit(f"decision coverage differs: {sorted(expected_handles ^ actual_handles)}")

    for candidate in source["candidates"]:
        candidate_id = candidate["candidate_id"]
        handle = candidate["handle"].casefold()
        observation = observation_by_id[candidate_id]
        public_row = public_by_id[candidate_id]
        collision = collision_by_id[candidate_id]
        if collision["status"] != "clear" or collision["matched_handles"]:
            raise SystemExit(f"unexpected exact catalog collision for {candidate_id}")
        description_evidence, extra, timestamps, activity = public_text(public_row)
        evidence_refs = [
            f"phase-b/evidence/successor-1/observations.json candidate_id={candidate_id}",
            f"phase-b/evidence/successor-1/editorial-public-evidence.json candidate_id={candidate_id}",
            f"phase-b/evidence/successor-1/collisions.json candidate_id={candidate_id}",
        ]
        if handle in ADD:
            decision = ADD[handle]
            category = decision["category"]
            if category not in categories:
                raise SystemExit(f"unknown category for {candidate_id}: {category}")
            entry = {
                "type": observation["observed_type"],
                "name": observation["visible_name"],
                "handle": observation["canonical_handle"],
                "description": decision["description"],
                "description_ru": decision["description_ru"],
                "description_kk": decision["description_kk"],
                "category": category,
                "last_verified": observation["observed_at"],
                "member_count": observation["member_count"],
            }
            if any(not str(entry[key]).strip() for key in (
                "name", "handle", "description", "description_ru", "description_kk", "category", "last_verified"
            )):
                raise SystemExit(f"incomplete proposed entry for {candidate_id}")
            action_name = "add"
            reason = (
                f"Target-bound {observation['observed_type'][:-1]} is live; public evidence supports Kazakhstan and IT relevance, "
                f"current activity, non-pure-commercial admission, and category {category}."
            )
            proposed_entry = entry
            editorial_row = {
                "candidate_id": candidate_id,
                "it_relevant": True,
                "kazakhstan_relevant": True,
                "purely_commercial": False,
                "category_valid": True,
                "locales_complete": True,
                "evidence_refs": evidence_refs,
            }
            topic_reason = decision["topic"]
            commercial_reason = decision["commercial"]
        else:
            decision = NON_ADD[handle]
            category = decision["category"]
            action_name = decision["action"]
            reason = decision["reason"]
            proposed_entry = None
            editorial_row = {
                "candidate_id": candidate_id,
                "it_relevant": decision["it"],
                "kazakhstan_relevant": decision["kz"],
                "purely_commercial": decision["commercial"],
                "category_valid": category in categories,
                "locales_complete": False,
                "evidence_refs": evidence_refs,
            }
            topic_reason = reason
            commercial_reason = reason
        editorial.append(editorial_row)
        actions.append({
            "candidate_id": candidate_id,
            "action": action_name,
            "reason": reason,
            "proposed_entry": proposed_entry,
        })
        occurrence_rows = [
            row for row in source["occurrences"] if row["occurrence_id"] in candidate["occurrence_ids"]
        ]
        relation = RELATIONS.get(
            handle,
            "No exact live/archive match, canonical redirect, public same-target alias, or material near-handle collision was found.",
        )
        judgements.append({
            "candidate_id": candidate_id,
            "source_occurrence_ids": candidate["occurrence_ids"],
            "source_occurrence_count": len(occurrence_rows),
            "identity": {
                "requested_handle": observation["requested_handle"],
                "canonical_handle": observation["canonical_handle"],
                "target_bound": observation["target_bound"],
                "visible_name": observation["visible_name"],
                "engine_body_sha256": observation["body_sha256"],
                "identity_result": "verified_exact_public_target",
            },
            "type": {
                "observed": observation["observed_type"],
                "declared_type_trials": observation["type_results"],
                "result": "one_verified_two_target_bound_declared_type_mismatches",
            },
            "liveness": {
                "status": observation["status"],
                "transport": observation["transport"],
                "observed_at": observation["observed_at"],
                "result": "live_public_preview",
            },
            "collisions": {
                "exact_live_or_archive": collision,
                "canonical_alias_near_handle": relation,
                "cross_input_duplicate": collision["cross_input_duplicate"],
            },
            "relevance": {
                "it_or_startup": editorial_row["it_relevant"],
                "kazakhstan": editorial_row["kazakhstan_relevant"],
                "reason": topic_reason,
                "public_description_excerpt": description_evidence,
            },
            "commerciality_spam": {
                "purely_commercial": editorial_row["purely_commercial"],
                "reason": commercial_reason,
                "limitation": "Only the bounded public description and up to three visible public-stream excerpts were inspected; private history was not accessed.",
            },
            "activity": {
                "evidence": activity,
                "public_preview_extra": extra,
                "retained_public_timestamps": timestamps,
                "limitation": "A public timestamp or online count establishes a current public signal, not long-term posting quality.",
            },
            "category": {
                "proposed": category,
                "valid_in_baseline": category in categories,
            },
            "observed_facts": {
                "member_count": observation["member_count"],
                "verification_date": observation["observed_at"],
                "count_semantics": "Observed once by the approved engine; never estimated.",
            },
            "copy": proposed_entry and {
                "description": proposed_entry["description"],
                "description_ru": proposed_entry["description_ru"],
                "description_kk": proposed_entry["description_kk"],
                "assessment": "Concise neutral parallel meaning; facts bounded to retained evidence.",
            },
            "disposition": {"action": action_name, "reason": reason},
            "evidence_refs": evidence_refs,
        })

    counts = Counter(row["action"] for row in actions)
    if counts != Counter({"add": 20, "unresolved": 4, "reject": 3, "duplicate": 1}):
        raise SystemExit(f"unexpected action totals: {dict(counts)}")
    if sum(len(row["occurrence_ids"]) for row in source["candidates"]) != 29:
        raise SystemExit("occurrence-to-candidate accounting differs")
    if [row["candidate_id"] for row in editorial] != [row["candidate_id"] for row in source["candidates"]]:
        raise SystemExit("editorial ordering differs")

    action_by_id = {row["candidate_id"]: row for row in actions}
    occurrence_accounting = {
        "schema_version": "kz-intake-occurrence-accounting/v1",
        "totals": {
            "source_occurrences": 29,
            "candidate_cases": 28,
            "add_cases": 20,
            "reject_cases": 3,
            "duplicate_cases": 1,
            "unresolved_cases": 4,
            "accounted_occurrences": 29,
        },
        "occurrences": [
            {
                "occurrence_id": row["occurrence_id"],
                "candidate_id": row["candidate_id"],
                "source_ordinal": row["ordinal"],
                "raw_text": row["raw_text"],
                "action": action_by_id[row["candidate_id"]]["action"],
                "reason": action_by_id[row["candidate_id"]]["reason"],
            }
            for row in source["occurrences"]
        ],
    }
    bundle = {
        "source": source,
        "collisions": collisions,
        "observations": observations,
        "editorial": editorial,
        "actions": actions,
    }
    outputs = {
        "collisions.json": collisions,
        "editorial.json": editorial,
        "actions.json": actions,
        "judgements.json": {
            "schema_version": "kz-intake-candidate-judgements/v1",
            "catalog_before_sha256": BASELINE_CATALOG_SHA256,
            "totals": dict(sorted(counts.items())),
            "candidates": judgements,
            "global_limitations": [
                "No authenticated or private Telegram access was used.",
                "Public group history is not exposed; current online counts are only point-in-time activity signals.",
                "No Phase A engine, rule, prompt, or fixture was changed after holdout evaluation.",
                "Unresolved candidates remain unresolved; preliminary discovery claims were not promoted to current facts.",
            ],
        },
        "occurrence-accounting.json": occurrence_accounting,
        "bundle.json": bundle,
    }
    for name, value in outputs.items():
        (universe / name).write_text(
            json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print(json.dumps({
        "actions": dict(sorted(counts.items())),
        "actions_sha256": kz_intake.actions_sha256(actions),
        "add_ids": [row["candidate_id"] for row in actions if row["action"] == "add"],
        "bundle_sha256": digest(universe / "bundle.json"),
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
