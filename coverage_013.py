"""Version 0.13.0: source-anchored expansion within the six approved handbook areas.

The existing 0.12.3 prose overlay runs first; these newly sourced blocks and
entries are intentionally applied afterward. Every new block must cite a
bundled source and quote a checkable phrase from one of its exact segments.
A successful source-anchor check is NOT an independent psak or interpretation
review. No source text is rewritten here.
"""
from pathlib import Path
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parent
FILES = ("coverage_013_entries.json", "coverage_013_details_a.json", "coverage_013_details_b.json")


def letters_only(value):
    clean = unicodedata.normalize("NFKD", str(value))
    return "".join(char for char in clean if char.isalnum())


def checked_block(raw, sources, context):
    b = dict(raw)
    anchor = b.pop("anchor", None)
    assert anchor and anchor.get("contains"), ("Missing source anchor", context)
    assert b["paragraphs"] and all(p.strip() for p in b["paragraphs"]), context
    assert b["refs"] and all(r["source"] in sources for r in b["refs"]), context
    source_id, segment = anchor["source"], anchor["segment"]
    assert {"source": source_id, "segments": [segment]} in b["refs"] or any(
        r["source"] == source_id and segment in r["segments"] for r in b["refs"]
    ), ("Anchor must be a directly cited source", context)
    passage = sources[source_id]["segments"][segment - 1]["text"]
    assert letters_only(anchor["contains"]) in letters_only(passage), (
        "Claim is not anchored to the quoted source segment", context, anchor
    )
    assert b.get("by") == "ביאור ערוך על פי המקורות המצוטטים", context
    return b


def apply_expansion(handbooks, sources):
    payloads = [json.loads((ROOT / filename).read_text(encoding="utf-8")) for filename in FILES]
    assert all(p["edition"] == "0.13.0" for p in payloads)
    assert len(payloads[0]["entries"]) == 9
    assert len(payloads[1]["additions"]) == 18
    assert len(payloads[2]["additions"]) == 21
    by_area = {h["id"]: h for h in handbooks}
    assert len(by_area) == 6
    old_entry_ids = {entry["id"] for h in handbooks for entry in h["entries"]}
    old_block_count = sum(len(e["blocks"]) for h in handbooks for e in h["entries"])
    assert len(old_entry_ids) == 89 and old_block_count == 251, (
        "Base corpus changed: perform a fresh source/coverage review before applying 0.13.0"
    )

    for item in payloads[0]["entries"]:
        h = by_area[item["handbook"]]
        assert item["id"] not in old_entry_ids, item["id"]
        idx = next(i for i, e in enumerate(h["entries"]) if e["id"] == item["after"])
        entry = {k: item[k] for k in ("id", "title", "group")}
        entry["blocks"] = [checked_block(b, sources, item["id"] + "/" + b["id"]) for b in item["blocks"]]
        assert len(entry["blocks"]) == 3 and len({b["id"] for b in entry["blocks"]}) == 3
        h["entries"].insert(idx + 1, entry)
        old_entry_ids.add(item["id"])

    entries = {entry["id"]: entry for h in handbooks for entry in h["entries"]}
    seen_extras = set()
    for payload in payloads[1:]:
        for item in payload["additions"]:
            entry = entries[item["entry"]]
            b = checked_block(item["block"], sources, item["entry"] + "/" + item["block"]["id"])
            key = item["entry"] + "/" + b["id"]
            assert key not in seen_extras and b["id"] not in {old["id"] for old in entry["blocks"]}, key
            entry["blocks"].append(b)
            seen_extras.add(key)

    assert len(seen_extras) == 39
    assert len(entries) == 98
    assert sum(len(e["blocks"]) for e in entries.values()) == 317
    return {"new_entries": 9, "new_blocks": 66, "source_anchor_checks": 66}
