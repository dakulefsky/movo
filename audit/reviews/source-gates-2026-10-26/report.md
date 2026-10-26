# Source-gate follow-up — October 26, 2026

The comprehensive source certification remains incomplete. This follows the existing full-corpus reading; it does not restart the audit or claim that opening an external page verifies its explanations. Work remains on `audit-0135-repairs`, with no merge or publication.

## Accounting

| Measure | Scope and result |
|---|---|
| Existing editorial reading retained | 317 blocks / 98 introductions / 360 units |
| Current units reconciled with exact prior Hebrew and source contexts | 360 |
| Historical catalog URLs freshly attempted | 146, spanning all six subjects |
| New corrections in displayed plugin content | 2 paragraphs in 2 blocks |
| Blocks expanded with concrete source explanations | 2 |
| Source-reference display labels repaired | 5 |
| New applied-text independent second reviews | 0 |
| Blocks fully independently verified under all six gates | 0 |
| Explicit unresolved conflict groups | 6, affecting 9 units in 6 blocks |
| Blocks still awaiting completed six-gate review | 317 |

Current unit dispositions are 311 `not_reviewed` (including partially checked units), 40 `corrected_pending_recheck`, and 9 `conflict_unresolved`. The corrected-pending category spans 37 blocks. This is a cumulative disposition count, not the number of blocks changed in this follow-up. The edited מנחות paragraph retains its unresolved עומר disposition.

The authoritative current checkpoint is `source_gate_followup_20261026` in [the single master ledger](../../master-ledger.json). It retains every earlier checkpoint, records all 360 current Hebrew units and hashes, links source-context notes and archived receipts, and identifies pending gates. The guarded manifest is [source_gate_repairs_20261026.json](../../../source_gate_repairs_20261026.json). Original `sources/` snapshots remain byte-identical to the basis commit, `d6a8804`.

## Actual content changes

* `minchah/exceptions`: say explicitly that מנחת חוטא and מנחת קנאות offered שלא לשמן are invalid; state the ordinary מנחה rule as failure to discharge the obligation, and explain the Commentary's חטאת connection. Mishnah Menachot 1:1 and the full relevant Rambam context support the change. Both sides of the עומר Commentary/code disagreement remain visible.
* `a-neder/sukkah`: replace an editorial instruction and repeated abstraction with the Rambam's own analogy to matzah of tevel or hekdesh. Explain the distinction between an object prohibited by a vow and an offering obligation contingent on performing a mitzvah. No new topic or silent source emendation was added.
* Five supplementary Rambam source dialogs previously displayed internal capture IDs as their `ref`. They now name הלכות מעילה א–ג, הלכות שחיטה א, ט, and הלכות ביכורים ב. The historical raw records and segment text are unchanged; this is a display-metadata repair, not evidence of native indexed-book opening.

## Witness evidence and limitations

All 146 historical catalog URLs actually referenced in the runtime were attempted, in subject order. Three initial access failures were recovered: canonical underscores for מעשר שני, and the alternate spellings נידה and ידיים. The archived `catalog-*.json` receipts often contain partial viewports. These are retrieval evidence, not 146 completed full-context comparisons. Search results likewise do not count as read editions.

Named context comparisons are distinguished in the ledger from this sweep. They include Menachot 1:1, Nedarim 2:2, Niddah 4:7, Yadayim 3:2, the full Meiri Ketubot introduction, the Meiri Pesachim introduction, Meiri BK79b, and the relevant Derenbourg Tahorot introduction contexts. Checks of one cited source do not clear a block's other sources or propositions.

The [Daf Yomi text of BK79b](https://daf-yomi.com/Dafyomi_Page.aspx?id=2946&vt=2) supplies the actual Meiri passage about concealment, ambushers and the theological explanation of theft's severity. Its printed-edition lineage remains unidentified. The [Derenbourg Tahorot text](https://he.wikisource.org/wiki/הקדמת_הרמב%22ם_לסדר_טהרות_(דירינבורג)) is kept distinct from the Ibn Tibbon translation. The difficult avot/rank wording is present in the accessed transcription; it was not silently repaired. The public Rambam Nedarim 2:2 transcription compresses its final conditional-offering sentence relative to the bundled Vilna text; this difference is recorded, without inferring a textual history. Adjacent Bartenura also states the conditional offering liability.

The six existing conflict groups remain: עומר, guardian oath, glass utensils, impurity rank, court composition, and מעילה. Public transcription access improves the evidence but does not establish manuscript or printed-edition independence, resolve the original Judeo-Arabic, or provide adversarial applied-text review.

## Validation

* Two consecutive clean builds produced identical ten-file package payloads with valid ZIP CRCs.
* All nine preservation/evidence scripts passed, including exact whole-corpus reversal of the two new edits and five metadata changes, historical ledger retention, and original source-file hashes.
* The complete packaged browser suite passed, traversing all 98 introductions and 317 controls and rendering both new paragraphs.
* The pinned actual JavaScript SDK suite passed on retry. Its first concurrent run failed the pre-boot visibility timing assertion; both logs are retained. Flutter RPC is a test double.
* The pinned native Otzaria packager produced the same payload. This is not a new installed-reader or indexed-source-opening test.
* Official validator: zero errors, zero warnings, `published=false`. It used its bundled SDK specification after its live specification fetch failed, as recorded in the log.
* JavaScript syntax and whitespace checks passed.

See [validation receipts](validation/). Built audit version remains 0.13.15. No release workflow was dispatched.

## Remaining work

The [protocol](../../../FULL-SOURCE-AUDIT-PROTOCOL.md) requires, for every unit, an independently identified textual witness, a full-context proposition-by-proposition comparison, completeness and literary review, and “another reviewer attempts to disprove all assertions.” Historical source-paired reading and this editor's new comparisons do not satisfy that separate applied-text pass. An independent reviewer is still needed, including for the eight prior continuation paragraphs and these two paragraphs. Full-edition and per-proposition source gates also remain incomplete across the corpus; the ledger records them as pending rather than promoting retrieval to verification. Appropriate human scholarly approval remains separate from the technical tests.
