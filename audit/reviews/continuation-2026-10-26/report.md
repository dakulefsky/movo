# Source-fidelity continuation — 2026-10-26

**The requested six-gate overhaul remains incomplete.** This continuation reread the displayed text of all 317 blocks in all 98 introductions, reconciled the existing source-paired reviews, and applied eight paragraph changes in seven blocks. It does not claim a fresh independent source review of every statement or final scholarly clearance.

Content/evidence commit: [6951b4d](https://github.com/dakulefsky/movo/commit/6951b4d). Branch: `audit-0135-repairs`. Built version remains 0.13.15 for local audit testing; no release, merge or publication was performed.

## Accounting

| Measure | This continuation |
|---|---:|
| Introductions whose current explanations were reread | 98 / 98 |
| Current blocks reread editorially | 317 / 317 |
| Current paragraph/item units recorded | 360 / 360 |
| Prior cited source segments reconciled by exact text hashes | 732 occurrences |
| Blocks changed in actual plugin content | 7 |
| Paragraphs changed | 8 |
| Blocks expanded substantively | 5 |
| Changed blocks checked against freshly accessed public textual witnesses | 7 |
| Blocks newly independently second-reviewed after application | 0 |
| Blocks fully verified under all six protocol gates | 0 |
| Blocks containing explicit unresolved source conflicts | 6, comprising 9 units |
| Blocks still awaiting completed six-gate clearance | 317 |

The current-reading scope is 113 blocks in קדשים, 48 in טהרות, 35 in אישות, 52 in זרעים, 46 in ממונות and 23 in איסור והיתר. The prior separate 0.13.14 source-paired reading covers every block. Of its 360 exact claim texts, 347 remain identical to this continuation's final corpus; the differences are the five previously applied teaching bridges and eight paragraphs changed here. Hash continuity preserves the relevance of old source evidence; it does **not** turn it into a newly fetched witness or completed verification.

The authoritative ledger is [master-ledger.json](../../master-ledger.json), specifically `continuation_20261026.claim_records`. It contains the exact current Hebrew, hashes, current references/edition metadata, carried-forward review locations, new witness receipts, applied changes, and pending gates for every unit. Original rows, adjudications, witnesses and all earlier checkpoints remain unchanged. Current dispositions are 312 `not_reviewed` (including incompletely checked units), 39 `corrected_pending_recheck`, and 9 `conflict_unresolved`; zero are `verified`. These are unit counts, not mutually exclusive block counts. The current corrected-pending category spans 36 distinct blocks, including the 29 from earlier adjudicated repairs and seven changed here.

## Applied changes

| Block | Source-grounded change |
|---|---|
| `av-melikah/portions` | Separate salting/burning the head from the subsequent preparation of the body; resolve the prior TR-007 wording concern without treating every procedural deviation as invalidating. |
| `d-gezel/meaning` | Preserve the Commentary's exact “מקצת הפירות” versus “כולם” language; do not silently decide the prior TR-001 quantity/degree ambiguity. |
| `k-meilah/meaning` | Distinguish Torah liability, principal/fifth/asham, from rabbinic prohibited benefit carrying principal alone. |
| `k-meilah/distinction` | Restrict the prior-permission exemption to edible flesh; it does not extinguish meilah in the emurim. |
| `k-meilah/invalid-service` | Disclose the Commentary/code disagreement about Torah versus rabbinic meilah after south slaughter. Explain that the valid priest receives remaining nefesh-blood, and preserve the code's impure-worker exception. |
| `a-shechitah/meaning` | Identify the two simanim as קנה and ושט before explaining their fractions. |
| `z-bikkurim/meaning` | Resolve the previously unsourced identity candidate: identify the seven species and Temple/territorial framework, including the code's rabbinic extension to ערי סיחון ועוג וסוריה. |

Five separately identified prooftexts supplement the 246 earlier runtime sources. All historical source files remain byte-identical; the corpus still has 98 introductions, 317 blocks and 360 units. The actual displayed explanations and Markdown export are changed through a guarded final overlay, with an exact inverse for earlier-layer preservation checks. No old proposal was blindly substituted for the current text.

## Meilah conflict and the October 25 proposal

The [October 25 draft](../../EDITORIAL-PASS-2026-10-25.md) could not responsibly be applied unchanged. The Commentary on Meilah 1:1 explicitly describes Torah meilah after south slaughter. [Mechon Mamre, Meilah 3](https://mechon-mamre.org/i/8903.htm) and the separate [Wikisource printed transcription](https://he.wikisource.org/wiki/רמב%22ם_הלכות_מעילה_ג) describe the listed disqualified offerings as rabbinic meilah. Meilah 1:6 supplies the different payment/korban consequences, and Meilah 2:2,6 distinguishes edible flesh from emurim.

The full accessed [Kesef Mishneh discussion](https://wiki.jewishbooks.org.il/mediawiki/wiki/כסף_משנה/מעילה/ג) discusses the code's rabbinic classification through the ascent dispute and Rabbi Yehudah/Rabbi Shimon. This is an identified explanatory discussion, not proof of a particular textual history or a resolution of the two Rambam passages. No corruption, retraction or original-Arabic reading is asserted. The new application paragraph retains both readings. Search-only Lechem Mishneh results are leads, not counted as a directly read full witness.

## Validation and remaining blockers

Two consecutive final clean builds have identical ten-file payloads and valid ZIP CRCs. All eight preservation/evidence scripts pass. The full packaged browser suite passes, including rendered new paragraphs and all five new source dialogs; the pinned actual JavaScript SDK suite also passes. Both use the existing loopback HTTP test transport. The pinned native Otzaria packager produces the same ten payload files. Official validation reports zero errors/warnings and `published=false`; JavaScript syntax and whitespace checks pass. [Validation receipts](validation/) record these scoped results.

The source snapshot and ledger-preservation checks are technical evidence, not independent judgments of the Hebrew's halachic accuracy. The new paragraphs have **not** received a separate applied-text adversarial review. Most units still lack completed independent-edition gates; public transcription access does not establish physical edition lineage or original Judeo-Arabic collation. Independent Meiri Pesachim/Bava Kamma edition checks remain outstanding. The five historical conflict groups—Omer, guardian oath, glass, impurity rank and court—remain, with Meilah now a sixth. Native successful indexed-source opening still needs a real source catalogue; this continuation tested native packaging, not a new installed native reader session.

Accordingly, all scholarly completion gates remain open. The full-corpus reading and recorded corrections are completed work; the comprehensive source certification and independent final review requested by the user are **not completed**. No permission to publish is requested or implied.
