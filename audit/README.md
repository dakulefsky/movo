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

The 0.13.10 review update is published in the Otzaria store, confirmed by [workflow39600903892](https://github.com/dakulefsky/movo/actions/runs/39600903892) at 2026-10-21 12:37:08 UTC. The server returned success and no pending approval, replacing 0.13.9. All workflow checks passed. No main merge or scholarly certification.

## Labeled Hebrew glosses — 0.13.11

Sixteen short lexical annotations cover seven terms in twelve explanation paragraphs: לכתחילה, בדיעבד, דאורייתא, הוו עלי עדים, רישא, סיפא and כחל. Parentheses visibly say `תרגום העורך` for translations or `ביאור העורך` for explanatory definitions. They are appended outside quotation marks. Repeated procedural terms are glossed on first mention in each entry; כחל is also explained in its separately accessible block. Already-explained חפצא/אגב and tractate names are left alone. The definition of לכתחילה describes the rule before the act; it does not turn a requirement into a preference.

`editorial_glosses_01311.json` contains guarded paragraph hashes and explicit anchors. `editorial_glosses.py` compiles separate offsets; it never changes the underlying paragraph. The reader and Markdown export display the marked additions, and introduction search includes their Hebrew explanations. The source viewer uses only the original saved text. `check_editorial_glosses.py` builds committed 0.13.10 in a temporary directory and requires the entire underlying corpus and full prior ledger to be unchanged. Earlier preservation checkers permit only the separately checked top-level annotation metadata.

The ledger stores the full annotation inventory in `editorial_gloss_checkpoint`, leaving every historical row/report/adjudication intact. These lexical annotations are same-editor additions, with independent scholarly recheck pending. They resolve no recorded source conflict and do not supply missing source editions. Native installation/rendering limitations from earlier checks remain explicit.

For 0.13.11, all five preservation checkers pass. The packaged browser suite verifies every original rendered paragraph after removing labeled gloss spans, translation placement after closing quotes, exact unannotated source text, Hebrew-gloss search, and mobile/desktop layout. The host SDK suite, native packager payload comparison and official validation pass (zero errors/warnings, bundled SDK fallback, local `published=false`). Two clean builds have identical ten-file payloads and valid CRC; ZIP timestamps differ. Desktop and mobile gloss rendering was visually checked. The existing accuracy notice remains.

The 0.13.11 review update is published in the Otzaria store, confirmed by [workflow39602678465](https://github.com/dakulefsky/movo/actions/runs/39602678465) at 2026-10-21 12:50:14 UTC. The server returned success and no pending approval, replacing 0.13.10. All workflow checks passed. No main merge or scholarly certification.

## Restrict glosses to unfamiliar vocabulary — 0.13.12

The user clarified that elementary Aramaic should not be translated. Fourteen routine glosses are removed from display, including דאורייתא, לכתחילה, בדיעבד, רישא, סיפא and הוו עלי עדים. Only the less familiar anatomical term כחל retains its two marked explanations. No new lexical definition is introduced. `editorial_gloss_scope_01312.json` explicitly selects those two records; the 0.13.11 inventory and ledger records remain untouched as history.

The existing full preservation checker compares with committed 0.13.11, requires all original corpus content and complete historical ledger to be unchanged, and allows only the selected annotation metadata to differ. Browser tests require zero glosses in the former elementary-phrase example and exactly two occurrences of כחל in the glossary data, while retaining the source-separation and Hebrew-search tests. The standing scholarly/native-installation limitations and accuracy notice remain unchanged.

For 0.13.12, all five preservation checks, full packaged browser suite, pinned SDK host suite, native packager payload comparison and official validation pass. Two clean builds have identical ten-file payloads and valid CRCs; timestamps differ. Local official validation uses its bundled SDK fallback and reports zero errors/warnings with `published=false`. The accuracy-under-review notice remains.

The 0.13.12 review update is published in the Otzaria store, confirmed by [workflow39603524176](https://github.com/dakulefsky/movo/actions/runs/39603524176) at 2026-10-21 12:56:29 UTC. The server returned success and no pending approval, replacing 0.13.11. All workflow checks passed; a transient CLI authentication error while fetching results was resolved before recording this receipt. No main merge or scholarly certification.

## Referent and phrasing refinements — 0.13.13

Five guarded changes in `refinement_01313.json` clarify which quantity is doubtful, name the actor in the maamar example, replace compressed inheritance wording, spell out the claim of a prior purchase and clarify the reference to Egyptian/Edomite distinctions. No example, legal qualification, quotation, number or gloss is added. The sparse כחל-only gloss selection is retained.

`check_refinement.py` compares committed 0.13.12 with exactly those five changes and preserves all other corpus data and prior ledger rows. Earlier checkers account for the explicit later overlay; no reviewed ledger data is regenerated. Same-editor wording review does not complete independent scholarly review. Existing native-installation limitations remain.

All six evidence checks, full packaged browser and SDK host suites, native packaging and official validation passed locally. Two clean builds have identical ten-file payloads; ZIP timestamps differ. The 0.13.13 review update is published in the store, confirmed by [workflow39636336622](https://github.com/dakulefsky/movo/actions/runs/39636336622) at 2026-10-21T16:38:14.1200054Z. All workflow checks passed. No scholarly certification or main merge.

## Final focused reading pass — 0.13.14

Two exact edits in `refinement_01314.json` improve the distinction between the two kinds of חזקה: remove a repeated purchase claim while retaining both the claim and the evidence of use, and identify the owner explicitly in the reference to silence. The evidence period, conditions for protest, source references and all other content remain unchanged. No new glosses or legal explanations are introduced.

The explicit overlay chain and all preservation checkers account for this pass. `check_refinement.py` compares committed 0.13.13 with exactly those two edits; previous manifests and reviewed ledger data remain intact. Scholarly approval and the previously recorded native-installation limitations are unaffected.

All six preservation checks, full packaged browser and SDK host suites, native packaging and official validation passed locally for 0.13.14. Two clean builds have identical ten-file payloads; ZIP timestamps differ. The review update is published in the store, confirmed by [workflow39637382648](https://github.com/dakulefsky/movo/actions/runs/39637382648) at 2026-10-21T16:44:55.3942906Z. All workflow checks passed. No scholarly certification or main merge.

## Separate AI source review — 0.13.14

At the user's request, a separate reviewer followed [this source-first brief](AI-SOURCE-REVIEWER.md) and read the current corpus at `d6ee916`: **all 317 blocks / 360 paragraph-and-item units**, all 32 selected repairs and the later wording overlays. The [report](reviews/ai-01314/report.md), [exact coverage](reviews/ai-01314/coverage.json), findings, reading notes and selected fresh public-text receipts are archived together. Both active כחל glosses and all 98 reading plans were checked separately.

The reviewer found no demonstrable source contradiction in this pass and recorded two **pre-existing, low-severity wording ambiguities**: some/all fruit versus degree of deterioration, and the compressed order of preparing the head/body of a bird offering. Neither is established as a halakhic error, and no application correction was applied. Five designated source-conflict topics remain visible. Full-corpus reading does not complete the six scholarly gates: most independent-witness checks, unresolved edition questions and appropriate human scholarly approval remain outstanding.

`separate_ai_review_01314` in the consolidated ledger contains the full findings, block coverage, presentation review, provenance and artifact hashes. All 26 existing top-level ledger fields and every historical row remain unchanged; decision counts remain 320 `not_reviewed`, 32 `corrected_pending_recheck`, 8 `conflict_unresolved`, zero `verified`. The coordinator checked all 360 current texts, 732 cited segment hashes, exact finding quotations/editions, receipt paths and presentation assignments. This is an evidence-only commit: application/source snapshots and the published 0.13.14 package are unchanged. No new store release or main merge.

## Introduction completeness and teaching review — 0.13.14

The user requested a different assessment: whether the selected introductions prepare a learner for their central discussions, and where another major approach is needed alongside Rambam. Following [the review brief](INTRODUCTION-REVIEW-BRIEF.md), the separate AI reviewer reread **all 98 entries / 317 blocks / 360 units**, plus six separately counted handbook framing statements, at `e701a40`. The [report](reviews/completeness-01314/report.md), exact coverage, authored entry notes, prioritized findings and public-text receipts are archived together. The intended audience remains a mature Hebrew/beis-midrash reader entering an unfamiliar subject, without elementary Aramaic glosses.

Judgments are **92 adequate for the stated selected scope, five concrete teaching gaps, and one source-check-needed candidate**. The five supported proposals define חופה within Rambam's framework, complete the נדר/שבועה comparison, identify the material of a מנחה, identify the כתובה debt and its collection events, and distinguish designation from delivery in דמאי. Naming the two שחיטה organs is supported but optional. Twelve overlap pairs and targeted cross-links are recorded separately as teaching-quality proposals, preserving details that differ. ביכורים identity remains an unimplemented candidate needing source work.

Rambam remains a useful backbone; the actual corpus already includes Mishnah, Scripture, Meiri, Rashi, Ramban and other commentators. The essential Ramban/Rambam ביעור comparison is already present. No additional mandatory alternative-view omission was established in this bounded pass. The freshly checked Rav/Shmuel מבעה discussion is optional breadth, and a proposed חופה definition must remain explicitly attributed. This is not proof of exhaustive completeness or agreement of all authorities.

`introduction_completeness_review_01314` supplements the single consolidated ledger with full findings, entry coverage, six framing assessments, provenance and hashes. All 27 previous top-level fields and every historical row remain unchanged. The coordinator independently checked the six proposed source contexts and validated all entry hashes, IDs, current excerpts, short witness quotations, framing texts and link targets. New public citations are proposals to attach, not application sources already added. This evidence-only review changes no application/source snapshot, historical decision, or store package; 0.13.14 remains the published review distribution. No new release or main merge.

## Apply five supported teaching bridges — 0.13.15

The user approved the five core additions from the completeness review. `teaching_additions_01315.json` guards exact before/after paragraphs and source/attribution metadata; `teaching_additions.py` applies them after the existing wording layers. The additions define חופה in Rambam's framework with its fitness qualification, complete the נדר/שבועה contrast, identify מנחה material with barley exceptions, identify the כתובה debt/collection events, and distinguish designation from delivery in דמאי. Two source labels now include Rambam alongside retained Meiri/Mishnah attribution. Five separately captured prooftexts bring the source count from241 to246. Existing98 entries /317 blocks /360 units, all historical snapshots, rare-word gloss selection and disclosed source conflicts remain. No optional expansion or bulk consolidation is applied.

The separate reviewer found the exact five drafted additions source-supported and requested the attribution-label fixes. Its usage limit prevented a subsequent generated-version recheck; the [application report](reviews/teaching-01315/report.md) and recorded messages distinguish the draft check from the coordinator's final content/software checks. No historical claim status or human scholarly gate is promoted. The new checkpoint supplements all previous ledger data unchanged; the ledger is not regenerated.

`check_teaching_additions.py` compares the entire application against committed0.13.14 plus exactly this overlay. Existing checkers strictly reverse the later overlay before checking their own historical layers. The packaged browser suite checks all five rendered additions and opens each corresponding new prooftext. The accuracy-under-review notice and prior native-installation/edition limitations remain explicit.

For0.13.15, all seven preservation checks, the full packaged browser suite including the five new source dialogs, pinned SDK host suite, native packager payload comparison and official validator pass. Two clean builds produce identical ten-file payloads with valid CRCs; ZIP timestamps differ. Local official validation uses its bundled SDK fallback and reports zero errors/warnings with `published=false`. Receipts are archived with the application report and recorded in the consolidated ledger.
