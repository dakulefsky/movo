# Mavo — source-fidelity review protocol (0.13.5)

## Governing rule

One unified review of **all 317 existing explanatory blocks** in the six approved areas. Preserve the source snapshots verbatim; do not add new topics merely to grow coverage. **No line is marked verified merely because a quote matches, CI succeeds, or an AI reviewer agrees.**

## Reproducible inventory

Run `python3 build.py` then `python3 generate_audit_ledger.py`. The generator reads the *fully overlaid* `editorial.json` produced by the builder, not an obsolete baseline. It emits `audit/master-ledger.json` (original paragraph/item plus exact bundled source segments and editions) and `audit/review-queue.csv`.

The inventory is deliberately **UNVERIFIED_BASELINE**. All gates start as pending. Do not check the generated ledger into a public release unless its count and content agree with the exact release commit under examination.

## Six gates for every paragraph and list item

1. **Reference integrity:** source ID, number, citation, author and edition identity are correct.
2. **Independent textual witness:** compare with external, verifiable edition (record link, date, variants); the bundled snapshot does not count as independent.
3. **Claim fidelity:** read full relevant context; record which exact words support *each* proposition, its boundaries, and any dispute.
4. **Completeness in context:** ask whether a condition, exception or central detail in the same source has been omitted such that this introduction misleads; do not introduce new sugyot.
5. **Literary revision:** preserve mature flowing Hebrew while not adding an unsourced reason or changing the force of a statement.
6. **Adversarial second pass:** another reviewer attempts to disprove all assertions and all newly introduced language, citing the original witness; disagreements remain visible.

## Allowed final statuses

- `verified`: all six gates completed with recorded citations and independent second pass.
- `corrected_pending_recheck`: fix proposed but not independently checked.
- `conflict_unresolved`: source variants/interpretations cannot responsibly be reconciled.
- `not_reviewed`: includes partially checked items. **Never count these as verified.**

Each finding records: claim ID, exact original Hebrew, source citation/segment and short quotation, defect type, severity, precise revision, independent witness URL/edition, reviewer and date. A conflict requires both witnesses and an explicit editorial note.

## Immediate high-risk queue

Start with issue #12's 31 flagged blocks; verify existing PR #13 correction operations one by one, including its three disclosed Rambam witness differences. Then process **all remaining blocks**, including the 286 not originally flagged. The previously created `INDEPENDENT-SOURCE-VERIFICATION-2026-10-20.md` documents three *targeted* witness checks, **not** the full ledger.

## Release gate

Do not close issue #12, merge audit PR #13 as 'source-certified', or claim completion until every claim unit has an evidence-backed disposition; all critical defects are fixed and second-reviewed; remaining historical disagreements are conspicuously disclosed; two consecutive clean builds and complete package/browser/Otzaria tests pass. Scholarly approval by an appropriate תלמיד חכם is a separate human decision, not an automated test.
