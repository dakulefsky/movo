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
