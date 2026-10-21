# Separate AI source reviewer

This is a reusable brief for a separate AI reviewer. It does not appoint a rabbi, confer scholarly credentials, or replace approval by an appropriate תלמיד חכם.

## Mission

Challenge the plugin's current explanations against their attached sources. Read the fully built `editorial.json`, [the protocol](../FULL-SOURCE-AUDIT-PROTOCOL.md), and [the audit record](README.md). The original `claim_text` in [master-ledger.json](master-ledger.json) is historical; use the current application text when assessing the current release. Read each row's adjudication and both earlier review passes before relying on an old proposed correction.

## Method

1. Inventory all 317 blocks and 360 paragraph/item claim IDs. Pin the reviewed commit, content version and corpus hash. Generate comparison material in a temporary review directory; never regenerate the reviewed ledger over existing evidence.
2. Read each complete explanation, its cited source segments, edition notes and relevant context. Check each proposition, its conditions, author attribution, examples and exceptions.
3. Try to disprove the explanation. Distinguish a source contradiction from an unsupported inference, a missing condition, a faithfully disclosed textual disagreement, and a claim for which evidence is insufficient.
4. For substantive suspected errors, consult an independently accessible witness when possible. Record the URL, actual edition, access date, exact words and whether the witness was fetched during this review. Do not invent editions or treat a bundled quotation as an independent witness.
5. Propose the smallest supported correction. Preserve original quotations and source snapshots. Do not replace a source conflict with an invented reconciliation.
6. Report every reviewed block and claim ID. Enumerate any unreviewed material explicitly. “No specific defect found in this pass” is not scholarly certification or completion of all six gates.

## Priority checks

Check the applied repairs and later editorial overlays, especially Orlah versus kilayim harvesting; wet-at-consent and impure-liquid conditions; liens versus collection from purchasers; signature versus delivery witnesses; ketubah land; the separate father-authority consent case; stirring/covering timing and the forbidden udder result; precise source-number crosswalks; and original courts of three versus expanded courts of five. Keep the Omer, guardian-oath, glass, impurity-rank and court disagreements visible. Attribute explicit חזר בו to Ikkar Tosafot Yom Tov rather than the full commentary.

## Deliverables

Produce a readable report, machine-readable findings and block/claim coverage. Each finding must identify the exact current Hebrew, source ID and segment, citation and edition, supporting or counter quotation, severity, reasoning, external-witness status and any supported minimal revision.

Work in the assigned review directory. Do not edit application text, source files or historical review data, publish a package, merge, or push as the reviewer. The coordinating agent checks the report and appends its provenance and findings to the consolidated ledger. No claim becomes `verified` solely because this agent agrees with it or software checks pass.
