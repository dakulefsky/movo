#!/usr/bin/env python3
"""Generate an auditable 317-block baseline. Run AFTER python3 build.py.

This creates a claim-by-claim review queue; it makes NO truth/accuracy claims.
No original source passages or app explanations are changed.
"""
from pathlib import Path
import csv, json, re
ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "editorial.json").read_text(encoding="utf-8"))
rows = []
for handbook in data["handbooks"]:
    for entry in handbook["entries"]:
        for block in entry["blocks"]:
            key = f"{entry['id']}/{block['id']}"
            refs = block["refs"]
            passages = []
            for ref in refs:
                src = data["sources"][ref["source"]]
                for number in ref["segments"]:
                    seg = src["segments"][number - 1]
                    passages.append({"source_id": ref["source"], "segment": number,
                                     "citation": src["citation"],
                                     "edition": src.get("edition", []),
                                     "source_text": seg["text"]})
            assert passages, key
            for kind, n, claim in (
                [("paragraph", i, p) for i,p in enumerate(block.get("paragraphs", []), 1)]
                + [("item", i, f"{v['label']}: {v['text']}") for i,v in enumerate(block.get("items", []), 1)]
            ):
                if not claim.strip(): continue
                rows.append({
                    "claim_id": f"{key}/{kind}-{n}",
                    "handbook": handbook["id"], "entry_id": entry["id"],
                    "block_id": block["id"], "heading": block["title"],
                    "claim_text": claim, "source_refs": passages,
                    "reference_integrity": "pending", "external_source_check": "pending",
                    "claim_fidelity": "pending", "omissions_check": "pending",
                    "literary_review": "pending", "adversarial_review": "pending",
                    "decision": "not_reviewed", "evidence_urls": [],
                    "findings": [], "proposed_revision": "", "reviewer": "",
                    "reviewed_at": ""
                })
keys = {f"{e['id']}/{b['id']}" for h in data["handbooks"] for e in h["entries"] for b in e["blocks"]}
assert len(keys) == 317, f"Expected 317 unique blocks, saw {len(keys)}"
assert len(rows) >= 317
out = ROOT / "audit"
out.mkdir(exist_ok=True)
(out / "master-ledger.json").write_text(json.dumps({
    "release_basis":data["version"], "status":"UNVERIFIED_BASELINE",
    "warning":"Pending means NOT checked. Exact quotation checks do not certify halachic fidelity.",
    "block_count":len(keys),"claim_units":len(rows),"rows":rows
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
with (out / "review-queue.csv").open("w", encoding="utf-8", newline="") as f:
    columns=["claim_id","handbook","entry_id","block_id","heading","claim_text",
             "source_locator","reference_integrity","external_source_check","claim_fidelity",
             "omissions_check","literary_review","adversarial_review","decision",
             "evidence_urls","findings","proposed_revision","reviewer","reviewed_at"]
    writer=csv.DictWriter(f,fieldnames=columns)
    writer.writeheader()
    for item in rows:
        row={k:item.get(k,"") for k in columns}
        row["source_locator"]="; ".join(f"{s['source_id']}#{s['segment']}" for s in item["source_refs"])
        row["evidence_urls"]=""
        row["findings"]=""
        writer.writerow(row)
print(f"BASELINE ONLY: {len(keys)} blocks, {len(rows)} paragraph/item claim units; zero independently certified.")
