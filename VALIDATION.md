# Current phrasing refinement — 0.13.13

Five guarded paragraph edits clarify references and compressed phrasing. All other explanations, source quotations, reading stages and the sparse gloss selection remain unchanged from 0.13.12. Results and store receipt are recorded in `audit/master-ledger.json`; earlier reports below are historical.

# Current sparse gloss selection — 0.13.12

Fourteen elementary translations are removed; only the two existing כחל glosses remain. Original explanations, quotations, all sources, reading stages and the complete reviewed ledger history are unchanged from 0.13.11. Current checks and store receipts are recorded in `audit/master-ledger.json`; older reports below remain historical.

# Current labeled glosses — 0.13.11

Sixteen separate editorial annotations clarify seven terms in twelve explanation paragraphs. Raw explanations, quotations, all 241 sources, source notes and reading stages remain byte-identical to committed 0.13.10. Original source text is displayed without annotations. The current check suite validates the separation, rendered attribution labels and Hebrew-gloss search; runtime results and store receipts are recorded in `audit/master-ledger.json`. Earlier reports below are historical.

# Current sentence-flow pass — 0.13.10

Eight paragraphs receive clearer sentence breaks. The checked word sequences are identical before and after; source texts, reading stages and all other corpus fields are unchanged from committed 0.13.9. Current runtime validation and store receipts are recorded in `audit/master-ledger.json`; earlier reports below are historical.

# Current sentence polish — 0.13.9

Exactly 14 explanatory paragraphs receive small wording changes. Full comparison against committed 0.13.8 preserves every other corpus field and all previously reviewed ledger-row fields. Quotations, numbers and all 0.13.8 reading stages remain intact. Runtime validation and store receipts are recorded in `audit/master-ledger.json`; the earlier reports below are historical.

# Current reading structure — 0.13.8

All 98 introductions have explicit nonempty reading stages and linked outlines. All 317 complete blocks, 360 claims and 241 sources are preserved exactly against the committed 0.13.7 build. No new legal explanations or quotations are introduced. Current build, browser, SDK, native and store results are recorded in `audit/master-ledger.json`; earlier results below remain historical.

# Current review build — 0.13.7

The readability pass changes 203 explanatory paragraphs in 185 of the existing 317 blocks. Exact source-preservation and guarded-overlay checks pass for all 241 source records and 360 claim units. Two clean builds produce identical ten-file package payloads; ZIP timestamps may differ. Host SDK tests, native Otzaria packaging and official validation pass (zero errors/warnings, local validation `published=false`, bundled SDK fallback). The full packaged browser suite passes using the authorized loopback HTTP preview transport, checking all 98 entries and 317 block controls with no external requests or JavaScript errors. Store receipts are recorded separately in `audit/master-ledger.json`.

Native 0.13.6 installation and selected WebView/permission checks passed in an isolated profile. Successful indexed-source opening still needs a populated catalogue. The current native packager validates the 0.13.7 payload. Independent scholarly review remains pending; the plugin visibly says accuracy is under review. See [audit/README.md](audit/README.md) for the current audit and reproducible commands.

The following 0.9.3 report is historical and does not describe the current corpus.

# Validation — 0.9.3, 18 October 2026

## Content and package

- Seven active areas: Kodashim 26 entries/99 blocks; Taharot 14/38; Ishut 10/26; Zeraim 15/40; Shabbat/Moed 17/34; monetary law 17/34; Issur/heter 7/14. Total **106 entries, 285 sourced blocks, 259 saved source documents**.
- Build assertions check unique identifiers, nonempty source references, source segment bounds, related links and exact extraction where raw provenance is recorded. These check structure/copying, never interpretation.
- JavaScript syntax and package ZIP integrity passed. The source archive rebuilt the plugin offline and reproduced every packaged file's bytes.
- Official Otzaria validator 1.19.1, checkout `64ee7c7806a03fcba16c111a7b6c3185e4d92804`, validated the actual `.otzplugin` against the live official SDK spec with app version 0.9.98 and fail-on-warnings: **0 errors, 0 warnings, 0 design notices; published=false**.

- Added checks open both new entries’ source dropdowns, verify the visible חובל textual note, and locate Rambam’s precise admission qualification.


## Browser and host contract

- Chromium opened the actual unpacked package. All 106 entries rendered with expected heading and all block/source controls.
- Seven-area navigation, introductions/source search scopes, vocalized Hebrew search, no-result messages, source dialogues and full catalogue, deep links, back/reload, previous/next, related-entry links, font persistence and 390px/1280px overflow checks passed.
- Retained 0.7.0 checks open Meiri Pesachim 6b from the bitul entry and Meiri Bava Kamma 79b from the theft distinction, verify visible textual notes, open Rambam Rosh Hashanah 3:1, follow theft → robbery and search directly into the order-of-inheritance subsection.
- Specific source assertions also include the new Issur/heter material and the existing/new-area Beitzah, Bava Metzia, Zevachim, Menachot, Kelim, Yevamot and Maaser Sheni passages.
- A separate test reads the actual injected JavaScript SDK from Otzaria commit `9f11690b80bf37703a3d1477a32c677c889dab7b`. Only the Flutter RPC transport boundary is doubled. Actual stream construction, multi-chunk delivery, cancellation, highlighted results, reader response envelopes, cross-database identities, permission/no-match/false-open paths and boot/change theme events passed.
- No JavaScript errors or runtime HTTP requests were observed. No previews or screenshots were made. Nothing was published or pushed.

## Unverified

The downloaded official Linux app could not start: loader exit 127, missing `libwayland-server.so.0` and other dependencies. Therefore installation and cited-source opening **in a running installed Otzaria application remain unverified**. SDK/validator/browser tests are not a substitute for that check.

Editorial review is by the same editor. No independent rabbinic audit, exhaustive Shas coverage or proof of interpretation from tests/citation matches is claimed. Each area lists its remaining coverage boundaries. See `EDITORIAL-REVIEW.md` and `HOST-INTEGRATION.md` for the detailed review.

0.9.3 removes the rejected blessings/prayer area from live data, navigation, search and source catalogue. The other coverage checks remain. Historical 0.9.0 wording above does not authorize restoration.

0.9.3: no new subjects or entries. אישות fidelity corrections retain ten entries/26 blocks and shorten its explanation text. Scope of this additional editorial pass is אישות only; see EDITORIAL-REVIEW.md.

0.9.3 completes the additional source-comparison pass on every existing area (prior Ishut pass retained). FIDELITY-REVIEW.json and EDITORIAL-REVIEW.md supersede earlier partial-pass descriptions. Source authors and textual notes were checked separately from software validation. No new entries, blocks or sources.
