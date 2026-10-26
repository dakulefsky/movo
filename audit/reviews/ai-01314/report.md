# Independent source-fidelity review — 0.13.14

**All 317 blocks / 360 paragraph-and-item units received fresh reading against their cited bundled source contexts. No demonstrable source contradiction or established unsupported inference/decisive omission was found in this pass. Two pre-existing, low-severity wording ambiguities remain open.** This completes the requested corpus-reading scope, not the protocol's six scholarly gates.

This is an AI review using a rigorous talmid-chacham-style method: distinguish דין from טעם, identify whose opinion is stated, test conditions and exceptions, and preserve genuine source disagreements. It is not human rabbinic approval. No claim is marked verified.

## Reviewed version and scope

The corpus is commit `d6ee91672c76355f8b189a702b8504741e8fb69f`, version **0.13.14**. The reviewed `editorial.json` SHA-256 is `9049de9b3be00871daba93a0b4f1e477b1e04aeeac13a52e72d3c390698ee973`. The historical ledger read during this review hashes to `dfeff78bc336da883b4fe0291d8a6cf53b9fdfb1d47c33849f7f640b49c6f0ae`. [review-manifest.json](review-manifest.json) records the source-record hash and hashes of all six requested repair/wording manifests.

| Area | Blocks read | Paragraph/item units read |
|---|---:|---:|
| קדשים | 113 / 113 | 136 / 136 |
| טהרות | 48 / 48 | 51 / 51 |
| אישות | 35 / 35 | 40 / 40 |
| זרעים | 52 / 52 | 53 / 53 |
| דיני ממונות | 46 / 46 | 54 / 54 |
| איסור והיתר | 23 / 23 | 26 / 26 |
| Total | **317 / 317** | **360 / 360** |

All **32 selected repairs**, **203 readability edits**, **14 polish edits**, **8 sentence-flow edits**, and **5 + 2 subsequent refinements** were examined in the actual current text. Reading included each complete block, every paragraph and labeled item, and its cited context, not merely changed words. Shared source passages were read once and reused where actually cited. Truncated tool output was re-read rather than counted as coverage.

[coverage.json](coverage.json) enumerates every block and exact inspected paragraph/item ID, current Hebrew and hash, source ID/segment/citation/edition metadata, segment hashes, and authored block-specific note. There are **no unread units in this pass**. Its assessments are 350 units with no specific defect identified, 8 units preserving disclosed source conflicts, and 2 units with evidence insufficient to resolve a wording concern. All retain incomplete six-gate status. [block-notes.json](block-notes.json) contains the 317 block notes.

The two active **כחל → עטין הבהמה** annotations were separately inspected: both are anchored to כחל and visibly labeled **ביאור העורך**, a reasonable anatomical explanation rather than a source quotation. All 98 reading-stage assignments were read as presentation context; no specific source-distorting assignment was identified. These metadata checks add no units to the fixed denominator of 360; their record is [presentation-review.json](presentation-review.json).

## Qualified wording concerns

Both concerns already occur verbatim in the historical baseline and were **not introduced by the recent overlays**. Neither is classified as a confirmed halakhic contradiction.

1. **TR-001 — `d-gezel/meaning/paragraph-1`:** current **״הרקיבו במקצת ... הרקיבו לגמרי״** naturally suggests degree of deterioration. Rambam's attached wording is **״כשהרקיבו מקצת הפירות ... ואם הרקיבו כולם״**, which can suggest some versus all fruits. The newly accessed [public commentary](https://he.wikisource.org/wiki/משנה_בבא_קמא_ט_ב) preserves that wording in context but does not settle its interpretation merely by matching it. Optional minimal clarification: quote the source's two exact phrases without choosing between interpretations.
2. **TR-007 — `av-melikah/portions/paragraph-1`:** **״מקטירים את הראש ואת הגוף, לאחר הסרת המוראה והנוצה והמליחה״** can attach body preparation to both burnings. [Mishnah Zevachim6:5](https://he.wikisource.org/wiki/משנה_זבחים_ו_ה) explicitly salts/burns the head before turning to the body. The current sentence may be compressed distributive wording; the separate `olah/bird` paragraph already gives the right order. Optional clarification: state head salting/burning first, then the body's removal, splitting, salting and burning. This does not establish a ruling that the current paragraph declares another order valid or invalid.

Exact complete current Hebrew, verbatim source segments, citations/edition metadata, fresh witness receipts, reasoning and minimal proposed wording are in [findings.json](findings.json). No correction was applied.

## Preserved source conflicts and high-risk boundaries

Five designated textual difficulties remain expressly visible:

- **Omer:** the Commentary invalidates shelo-lishmah kemitzah while the code permits it. Explicit **חזר בו** is correctly assigned to **עיקר תוספות יום טוב**; the full commentary is separately described as comparing the code. No unidentified alternative edition is invented.
- **Guardian oath:** the saved Commentary says **שבועת התורה**, while the separate code witness identifies the relevant oath as an enactment of the sages.
- **Glass:** the introduction's general immersion wording is qualified against the code's explicit glass-vessel exception.
- **Impurity rank:** the saved difficult sentence is retained, while the explanation follows the explicit av/derivative maxim and attached warning.
- **Court:** the initial three-judge panel differs from an expanded five; the four-agree/one-unsure Commentary/code difference is retained.

These are **faithfully disclosed source conflicts**, not defects to erase or textual histories resolved by this review. TR-002–TR-006 record the exact passages.

The selected repairs retain the decisive boundaries: Orlah seeing the harvest versus kilayim personal harvesting; food detachment/consent, wet-at-consent with separate Rashi attribution, and impure-liquid simultaneous transmission; lien versus purchaser recovery; unsigned valid get delivery versus invalid signed witness; ketubah land; separate paternal kiddushin authority; initial/late stirring and covering through the end; udder's contribution toward sixty while remaining forbidden; and original versus enlarged court. The later two-chazakot wording retains the purchase claim, fruit-use evidence and owner's opportunity to know/protest.

## Witness and approval limits

New shell requests to seven public pages returned HTTP403, recorded in [external/manifest.json](external/manifest.json). Normal connected-web access subsequently rendered selected public texts. Fresh [Mechon Mamre Sanhedrin8](https://mechon-mamre.org/i/e108.htm) and [Wikisource Sanhedrin3:6](https://he.wikisource.org/wiki/משנה_סנהדרין_ג_ו) contexts support the disclosed panel-dependent court discrepancy; fresh fruit and bird witnesses support the quotations underlying the qualified wording concerns. Receipts are preserved under [external](external/), separately from failed requests and pre-existing saved evidence.

Public transcriptions do not establish independent physical-edition lineage, manuscript collation, original-Arabic interpretation or agreement of all Rishonim. Historical ledger witnesses remain historical, not relabeled as newly fetched. Independent Meiri edition checks remain outstanding. Most units still lack the protocol's completed independent-witness gate, and this one AI pass supplies neither all six gates nor appropriate human scholarly approval.

The original 221-block checkpoint is retained separately; the final artifacts now cover the remaining 96 blocks as well. No application, source snapshot, historical evidence or master-ledger row was changed. No generator was run over the reviewed ledger, and no push, merge or publication was performed.
