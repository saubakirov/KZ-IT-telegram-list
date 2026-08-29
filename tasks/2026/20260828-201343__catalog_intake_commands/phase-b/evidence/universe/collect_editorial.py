#!/usr/bin/env python3
"""Collect bounded, public, read-only editorial evidence for Phase B candidates."""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo


CAPTURE_CLASSES = {
    "tgme_page_title",
    "tgme_page_extra",
    "tgme_page_description",
    "tgme_channel_info_header_title",
    "tgme_channel_info_description",
    "tgme_channel_info_counter",
    "tgme_widget_message_text",
}


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def normalize(value: str, limit: int = 1200) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value[:limit]


class EvidenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[list[str]] = []
        self.active: list[str] = []
        self.values: dict[str, list[str]] = {name: [] for name in CAPTURE_CLASSES}
        self.meta: dict[str, str] = {}
        self.times: list[str] = []
        self.canonical_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        started: list[str] = []
        classes = set(attributes.get("class", "").split())
        for name in sorted(CAPTURE_CLASSES & classes):
            self.active.append(name)
            started.append(name)
        self.stack.append(started)
        if tag == "meta":
            key = attributes.get("property") or attributes.get("name")
            if key and attributes.get("content"):
                self.meta[key] = normalize(attributes["content"])
        if tag == "time" and attributes.get("datetime"):
            self.times.append(attributes["datetime"])
        if tag == "link" and "canonical" in attributes.get("rel", "").split():
            if attributes.get("href"):
                self.canonical_links.append(attributes["href"])

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if not self.stack:
            return
        for name in reversed(self.stack.pop()):
            if self.active and self.active[-1] == name:
                self.active.pop()
            elif name in self.active:
                self.active.remove(name)

    def handle_data(self, data: str) -> None:
        for name in self.active:
            self.values[name].append(data)

    def result(self) -> dict[str, object]:
        extracted = {
            name: normalize(" ".join(parts))
            for name, parts in self.values.items()
            if normalize(" ".join(parts))
        }
        message_texts = [
            normalize(part)
            for part in self.values["tgme_widget_message_text"]
            if normalize(part)
        ]
        return {
            "meta": self.meta,
            "text": extracted,
            "message_text_excerpt": message_texts[-3:],
            "message_timestamps": sorted(set(self.times))[-5:],
            "canonical_links": sorted(set(self.canonical_links)),
        }


def fetch(url: str) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; KZ-IT-telegram-list-public-evidence/1.0)",
            "Accept-Language": "en,ru;q=0.8,kk;q=0.7",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read()
            status = response.status
            final_url = response.geturl()
    except urllib.error.HTTPError as exc:
        body = exc.read()
        status = exc.code
        final_url = exc.geturl()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "requested_url": url,
            "ok": False,
            "reason": type(exc).__name__,
            "detail": normalize(str(exc), limit=300),
        }
    parser = EvidenceParser()
    parser.feed(body.decode("utf-8", errors="replace"))
    return {
        "requested_url": url,
        "final_url": final_url,
        "status_code": status,
        "ok": status == 200,
        "bytes": len(body),
        "body_sha256": sha256(body),
        "extracted": parser.result(),
    }


def main() -> int:
    universe_dir = Path(__file__).resolve().parent
    observations = json.loads((universe_dir / "observations.json").read_text(encoding="utf-8"))
    rows = []
    for observation in observations["observations"]:
        handle = observation["requested_handle"]
        canonical = observation["canonical_handle"]
        rows.append({
            "candidate_id": observation["candidate_id"],
            "requested_handle": handle,
            "canonical_handle": canonical,
            "engine_body_sha256": observation["body_sha256"],
            "root": fetch(f"https://t.me/{handle}"),
            "public_stream": fetch(f"https://t.me/s/{canonical}"),
        })
    result = {
        "schema_version": "kz-intake-editorial-public-evidence/v1",
        "observed_at": datetime.now(ZoneInfo("Asia/Qyzylorda")).isoformat(timespec="seconds"),
        "semantics": {
            "transport": "Unauthenticated public HTTPS GET only; no Telegram session or private fallback.",
            "retention": "Response SHA-256 plus bounded machine-extracted public text/timestamps; raw HTML not retained.",
            "activity": "A public-stream timestamp is evidence of a visible post, not proof of overall community quality.",
            "admission": "Extracted text is evidence for human judgement and does not itself authorize catalog admission.",
        },
        "candidates": rows,
    }
    output = universe_dir / "editorial-public-evidence.json"
    output.write_text(
        json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "candidates": len(rows),
        "root_ok": sum(bool(row["root"].get("ok")) for row in rows),
        "public_stream_ok": sum(bool(row["public_stream"].get("ok")) for row in rows),
        "output_sha256": sha256(output.read_bytes()),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
