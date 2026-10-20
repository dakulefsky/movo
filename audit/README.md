# Full source-fidelity audit — 2026-10-20

**Two review passes recorded; scholarly/release clearance remains incomplete.** The consolidated evidence and adjudications are in `master-ledger.json`. `review-queue.csv` is a derived index, not a competing ledger.

All **317 blocks / 360 paragraph-and-list claim units** were read in a first pass and an independent adversarial second pass. This includes all 31 blocks flagged in issue #12 and the remaining 286. Original Hebrew and source snapshots remain unchanged. The exact original claim IDs/text/source references were checked against a fresh generator run in a temporary directory.

| Area | Blocks | Claim units | First pass | Second pass |
|---|---:|---:|---:|---:|
| Kodashim | 113 | 136 | 136 | 136 |
| Tahorot | 48 | 51 | 51 | 51 |
| Ishut | 35 | 40 | 40 | 40 |
| Zeraim | 52 | 53 | 53 | 53 |
| Monetary law | 46 | 54 | 54 | 54 |
| Issur | 23 | 26 | 26 | 26 |
| Total | 317 | 360 | 360 | 360 |

The master records findings on45 claim units and candidate/selected revisions on36. Status totals:320 `not_reviewed`,32 `corrected_pending_recheck`,8 `conflict_unresolved`,0 `verified`. Under the protocol, `not_reviewed` includes partially completed gates: it does not mean those320 claims were left unread. Two readings do not automatically clear all six gates. Proposed corrections have **not been applied to application text**.

## Principal results

- Orlah paragraph transfers the adjacent kilayim harvesting qualification and omits the no-seeing-harvest condition.
- Food preparation impurity paragraph presents one disputed restriction to primary-source liquids as the Rambam's general rule.
- Oral-loan note confuses existence of a lien with ability to collect from purchasers.
- Judicial-panel correction needs the initial-three/expanded-five distinction; Commentary and Mishneh Torah disagree on four agreeing plus one unsure. The unsafe general replacement is superseded explicitly.
- Get witnesses, ketubah land, and consent-scope paragraphs need precise qualifications.
- Milk/meat stirring requires an initial-versus-late distinction; udder paragraph omits that the udder counts toward sixty but remains forbidden.
- Challah1:1/1:2, Gittin9:2/9:3 and Shevuot8:1/8:4 require explicit citation/segmentation crosswalks.
- The phrase that Rambam “retracted” belongs to **Ikkar Tosafot Yom Tov**, not the full commentary. The earlier review proposal is superseded, with heading-specific evidence.
- Omer, guardian-oath, glass/Introduction wording, impurity-rank wording and other textual differences remain explicit. Unidentified alternative asham-age witnesses are not invented. Exact independent Meiri witnesses remain missing for the recorded Pesachim/BavaKamma passages.

Every row retains its original, full cited source passages, both review reports, supporting quotations/URLs/edition labels/dates/hashes, findings, candidate wording and limits. All1797 quoted evidence occurrences were traced against captured page text and hashes. That check establishes traceability, not interpretive correctness. Raw witness captures are retained under `/workspace/audit-witnesses`.

## Validation

- Python3.12.14, Node24.19.0, Playwright1.62.1 work.
- Two final builds/packages passed; committed generated exports have no drift.
- Inventory/source-copy preservation, JavaScript syntax and ZIP integrity passed.
- Official validator passed with0errors/0warnings and `published=false`; live SDK fetch failed so its bundled spec was used.
- Both browser suites were attempted and failed before assertions at `file://` navigation with `ERR_BLOCKED_BY_ADMINISTRATOR`.
- Existing host suite extracts0.12.0, so even a later pass would not establish latest0.13.5 host behavior. Native Otzaria installation/source opening remains unverified.

## Resume without losing evidence

Do not run `generate_audit_ledger.py` over this reviewed ledger: it overwrites findings with an unverified baseline. Generate any comparison inventory in a temporary directory, then compare immutable original fields.

Next: apply/recheck selected repairs in an application-editing task, add separate prooftexts without changing historical snapshots, resolve named source/edition gaps and conflicts, and complete browser/native-host checks in an authorized runtime. Appropriate human scholarly approval remains separate from automated validation. Nothing has been merged, pushed, or published.
