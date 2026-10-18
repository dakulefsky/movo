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
