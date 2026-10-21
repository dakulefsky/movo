# Full source-fidelity audit and applied repairs — 2026-10-20

**Selected repairs are applied; native packaging and selected installation/WebView checks pass. Scholarly and full release clearance remains incomplete.** The single evidence ledger is `master-ledger.json`. `review-queue.csv` remains the historical derived index, not another adjudication ledger.

All **317 blocks / 360 claim units** have the recorded first and independent adversarial reports from `aa8d284`. The application now applies **32 selected paragraph repairs** through `adjudicated_repairs.json` and `adjudicated_repairs.py`, after the earlier overlays. Each operation asserts the exact prior paragraph. Fourteen separately identified prooftexts supplement the original 227 source records, giving 241 application sources without adding entries or blocks. Historical source files, original ledger `claim_text`/`source_refs`, both reports, rejected candidates and adjudications are preserved.

Each affected ledger row has an `application_repair` record; `repair_checkpoint` describes the current implementation. Earlier `audit_checkpoint` validation and implementation descriptions are retained as history of the pre-repair corpus. No claim was promoted to `verified`: the decisions remain 320 `not_reviewed`, 32 `corrected_pending_recheck`, 8 `conflict_unresolved`. Here `not_reviewed` includes incomplete gates, not an unread claim. Implementation checks and historical independent review of proposed wording do not constitute a new independent scholarly review of the applied corpus.

## Applied scope

- Orlah distinguishes not seeing the harvest from the adjacent kilayim prohibition on personally harvesting; the Mishnah and MT10:11 are separate prooftexts.
- Food preparation removes the unsupported exclusive restriction to primary impurity liquids. Wet-at-consent support is separately attributed to Rashi, not silently to Rambam.
- The oral-loan note distinguishes a lien from collection from purchasers. Ketubah wording follows the cited land context; consent wording identifies the separate father-authority case.
- Get witnesses explicitly distinguish valid delivery without signatures, absent delivery witnesses, and invalid signed witnesses.
- Milk/meat stirring distinguishes initial and late stirring, retains covering through the end, and states that a piece already prohibited remains prohibited. Udder counts toward sixty and remains forbidden itself.
- Court wording separates original three from expanded five, retaining the Commentary/MT disagreement about four agreeing and one unsure.
- Challah1:1/1:2, Gittin9:3/9:2 and Shevuot8:1/local segment4/canonical8:4 have visible source notes and separate witnesses. Local filenames and historical labels were not relabeled as different editions.
- The Omer context paragraph remains intact; its separate note attributes explicit **חזר בו** to **Ikkar Tosafot Yom Tov**, with full Tosafot Yom Tov identified separately.
- The fuller Meiri Ketubot ending is now separately attached: absence from the shortened snapshot does not disprove the attribution. Existing prose remains valid and unchanged.
- Other selected corrections clarify sacrificial service, impurity outcomes, poor gifts and bounded oath consequences. No unidentified alternative asham-age edition is implied. Optional wolf-rule additions were not mistaken for proven errors.

Omer, guardian-oath, glass, impurity-rank and court textual differences remain explicit. Independent Meiri Pesachim/Bava Kamma witnesses and appropriate human scholarly approval remain outstanding.

## Reproduce validation

Run `python3 build.py`, `python3 package.py`, then `python3 check_adjudicated_repairs.py`. The last command generates a comparison inventory **only in a temporary directory under `work/`**. It checks all 360 claim IDs/texts against the explicit repair selection, retains all original source references, compares every historical source file byte-for-byte, and preserves all historical reviewed row fields. Do not run `generate_audit_ledger.py` over this reviewed ledger.

Two final clean builds passed with identical package-file payloads and ZIP SHA-256 `a0e578f1f9fd9a5092656a0ebeabe1844024ace0dc94d42e853ea71bf0c871cb`. ZIP CRC and JavaScript syntax passed. The official validator passed with zero errors/warnings, bundled SDK fallback, and `published=false`.

Both packaged browser suites pass using the authorized loopback HTTP preview transport:

```sh
MOVO_TEST_TRANSPORT=http PLAYWRIGHT_CHROMIUM_EXECUTABLE=/usr/bin/chromium npm test
MOVO_TEST_TRANSPORT=http PLAYWRIGHT_CHROMIUM_EXECUTABLE=/usr/bin/chromium npm run test:host
```

The host suite now extracts **0.13.5**, asserts its manifest version, and uses a fresh temporary directory and pinned SDK commit `9f11690b80bf37703a3d1477a32c677c889dab7b`. Its Flutter RPC boundary remains a test double. Both default `file://` attempts still fail at navigation with `ERR_BLOCKED_BY_ADMINISTRATOR`. The optional HTTP test server does not change browser policy or certify native file loading; external requests remain forbidden by test assertions. The initial native loader failures are now resolved locally: `validate_native.py` pins and extracts the official executable plus Debian harfbuzz-ICU/GLES/Xvfb packages under `work/`, and selects the system `libmount` ahead of the older bundled copy. No system installation or managed policy changes are needed. Native `pack-plugin` passes and its ten extracted payload files exactly match the tested Python package. Installation, native-WebView home/article rendering, the repaired Orlah paragraph, separate MT10:11 prooftext, denied-permission handling and granted-search empty-catalogue no-match handling were checked in an isolated native profile. These are selected native smoke checks; successful indexed-source reader opening still needs a real source catalogue and is not certified. Independent applied-text scholarly recheck and source-conflict resolutions remain release blockers.

The repair branch is pushed to GitHub. The user-requested **0.13.6 review distribution is published in the Otzaria store**, confirmed by [workflow39529142768](https://github.com/dakulefsky/movo/actions/runs/39529142768). The plugin and store short description state that accuracy is under review. No scholarly status was promoted and nothing was merged into main.

Repeat native packaging with `python3 validate_native.py` (first run downloads pinned packages into `work/`). Use `python3 validate_native.py --open` for an isolated manual GUI session on a virtual display; the display number and receipt location are recorded locally. This does not install system packages, merge or publish.

## Readability review — 0.13.7

All 317 blocks / 360 claim units were read for flow. The guarded overlay in `readability_0137.json` revises 203 explanatory paragraphs in 185 blocks, using shorter sentences and clearer order. It leaves all 241 source records, headings, lists, references and links intact. `check_readability.py` builds the committed 0.13.6 baseline in a temporary directory and checks the exact changes, direct quotations and 47 explicit explanatory-anchor crosswalks. Historical evidence is preserved; row-level `readability_edit` records supplement the ledger rather than replacing adjudications. This is a same-editor wording pass, with independent scholarly review still pending.

Run `python3 check_readability.py` after building, alongside the adjudicated-repair checker. The persistent accuracy-under-review notice remains in the plugin and store description.

For 0.13.7, two clean builds have identical ten-file payloads and valid ZIP CRCs. Both packaged browser suites pass using the authorized HTTP preview. The pinned native Otzaria packager produces the same payload, and the official validator reports zero errors/warnings with its bundled SDK fallback (`published=false` for local validation). Full source/quotation/overlay checks pass. No scholarly claim status changes.

The user-requested 0.13.7 readability review update is published in the Otzaria store, confirmed by [workflow39533946991](https://github.com/dakulefsky/movo/actions/runs/39533946991) on 2026-10-21 UTC (2026-10-20 New York). The server returned success with no pending approval, replacing 0.13.6. The workflow's packaged browser suite and official validation also passed. Accuracy remains under review; nothing was merged into main.

## Consistent reading structure — 0.13.8

`reading_structure_0138.json` explicitly assigns every block of all 98 entries to definition, operation or distinctions. The displayed order follows those stages while the underlying block/ledger order stays unchanged. Empty stages are omitted. Each entry has an outline linking directly to its passages; source buttons and textual disagreements stay attached to the complete original block. The Markdown export follows the same teaching order.

`reading_structure.py` guards the original block IDs/order and exact single coverage; `check_reading_structure.py` builds the committed 0.13.7 baseline only in a temporary directory, then requires the entire original entry content and all 241 sources to be identical. Only the new reading plan may differ. Row-level `reading_structure` fields record presentation placement without changing a scholarly decision. Run this checker after the existing repair and readability checks. This organization does not complete independent scholarly review or resolve source conflicts.

For 0.13.8, two clean builds reproduce the identical ten-file payload and ZIP hash `e40f7aac33dc54b1e37e18283d5fc07b5d387ec6621fa9df2248616415bfddae`. Full packaged browser checks cover stage/block order in every entry and mouse/keyboard outline links. The actual SDK host suite, native packager with matching payload, and official validator (zero errors/warnings, bundled SDK fallback, local `published=false`) pass. Mobile and desktop previews were visually checked. A manual native update attempt still showed the older installed 0.13.5 content, so it does not certify 0.13.8 native installation/rendering; this limitation is explicit in the ledger.

The 0.13.8 review update is published in the Otzaria store, confirmed by [workflow39598424377](https://github.com/dakulefsky/movo/actions/runs/39598424377) at 2026-10-21 12:18:48 UTC. The server returned success, no pending approval, and updated 0.13.7 to 0.13.8. Workflow build, all evidence checks, browser tests and official validation passed. No main merge or scholarly certification.

## Final sentence polish — 0.13.9

A focused pass smooths 14 explanatory paragraphs: it replaces stiff constructions, separates a compound sentence and uses ordinary Hebrew phrasing. `polish_0139.json` records exact before/after text; `polish_revision.py` asserts each prior paragraph before changing it. Source quotations, source notes, technical terms, legal conditions, examples, references and reading-stage assignments are retained. Row-level `sentence_polish` fields supplement all earlier reviewed evidence.

`check_polish.py` builds committed 0.13.8 in a temporary directory and compares the entire corpus after only those 14 changes. It also checks quoted phrases, digits and every previously reviewed ledger-row field. The earlier checkers account for this explicit later overlay. Run it after `check_adjudicated_repairs.py`, `check_readability.py` and `check_reading_structure.py`; no generator writes over the reviewed ledger. No scholarly status is promoted. Native installation/rendering limitations recorded for 0.13.8 remain unresolved by a sentence-only release.

For 0.13.9, two clean builds have identical ten-file payloads and valid ZIP CRCs (ZIP timestamps differ). Both full packaged browser suites, pinned SDK host checks, native packager payload comparison and official validation pass. The official validator uses its bundled SDK fallback and reports zero errors/warnings with local `published=false`. All four evidence/scope checkers pass. The accuracy-under-review notice remains visible.

The 0.13.9 review update is published in the Otzaria store, confirmed by [workflow39600059331](https://github.com/dakulefsky/movo/actions/runs/39600059331) at 2026-10-21 12:30:57 UTC. The server returned success and no pending approval, updating 0.13.8 to 0.13.9. All workflow checks passed. No main merge or scholarly certification.

## Sentence-flow pass — 0.13.10

The additional pass splits long sentences in eight paragraphs concerning מאמר, חלה, תמורה, internal חטאת offerings, ספקות, מנחת כהן and court authority. Only sentence boundaries change; every word remains in its original order, including attributions and legal qualifications. The selected operations are recorded in `sentence_flow_01310.json`. `polish_revision.py` now applies both explicitly guarded sentence passes; the earlier manifests and row-level records remain unchanged.

`check_polish.py` compares the entire current corpus with committed 0.13.9 after exactly those eight operations. It requires identical word sequences in each changed paragraph and preserves all other corpus fields and every historical ledger-row field. The earlier repair, readability and reading-structure comparisons account for the full overlay chain. No source snapshots, source notes, claim statuses, examples, source references or reading stages change. Native installation/rendering and independent scholarly review remain unverified beyond the already recorded checks.

For 0.13.10, all four preservation checkers, the full packaged browser suite, pinned SDK host suite, native packaging payload comparison and official validation pass. Two clean builds have identical ten-file payloads and valid CRCs; ZIP timestamps differ. Local official validation reports zero errors/warnings with bundled SDK fallback and `published=false`. The accuracy-under-review notice remains visible.
