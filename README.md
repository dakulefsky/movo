# מבואות הש״ס

An offline Hebrew introductory index for Otzaria, by **DanTheMan**.

The plugin introduces the main subjects and essential processes in קדשים, טהרות, אישות, זרעים, דיני ממונות, and איסור והיתר. Entries are short, with expandable headings, search, related entries, and bundled source passages. The current package is **0.10.0**.

## Install

Download [Mevoot-Shas-0.10.0.otzplugin](dist/Mevoot-Shas-0.10.0.otzplugin) and import it into Otzaria's plugin manager. No internet connection or AI service is required by the installed plugin.

The manifest declares Otzaria 0.9.97 or later. Package validation was run against 0.9.98. Installation and source opening in a running installed Otzaria application remain unverified; see [VALIDATION.md](VALIDATION.md).

## Build offline

Python 3 and its standard library are sufficient. All required source snapshots are included.

```sh
python3 build.py
python3 package.py
```

This generates the content export, editorial data and `plugin/data/library.js`, then creates `dist/Mevoot-Shas-0.10.0.otzplugin`. Build output is reproducible without fetching source texts.

## Sources and editorial scope

Rambam's Commentary on Mishnah and introductions are the main foundation. Selected passages from Meiri, the Mishnah, Scripture, and Ramban are explicitly identified. Explanations are editorial paraphrases, distinct from the bundled source text.

The aim is to give a learner his bearings in the main areas. Do not expand this into an encyclopedia of every term. Do not add inferred reasons or conceptual frameworks. Preserve qualifications, disputes and textual uncertainty. See [COVERAGE.md](COVERAGE.md), [EDITORIAL-REVIEW.md](EDITORIAL-REVIEW.md), and [FIDELITY-REVIEW.json](FIDELITY-REVIEW.json).

All existing entries received the additional same-editor source-comparison pass: אישות in 0.9.2 and the remaining areas in 0.9.3. This is not independent rabbinic certification or verification against Arabic originals. Passing software tests does not establish interpretive accuracy.

Source snapshots and their supplied edition/license metadata are in `sources/`. See [SOURCE-NOTICES.md](SOURCE-NOTICES.md). Earlier project archives are preserved separately and are not the editorial foundation of this repository.

## Interface tests

Install development dependencies and Playwright's browser:

```sh
npm install
npx playwright install chromium
npm test
```

For an existing Chromium binary, set `PLAYWRIGHT_CHROMIUM_EXECUTABLE` to its absolute path. Tests open the actual unpacked plugin, check reading/search/source controls and responsive layout, and assert no runtime HTTP requests. They do not create screenshots.

The optional host SDK contract test requires an Otzaria source checkout at commit `9f11690b80bf37703a3d1477a32c677c889dab7b`:

```sh
OTZARIA_HOST_SOURCE=/path/to/otzaria npm run test:host
```

That test reads the host's actual injected SDK and doubles the Flutter transport boundary. It does not replace installed-app testing. See [HOST-INTEGRATION.md](HOST-INTEGRATION.md).

The publishing workflow in `.github/workflows/release.yml` builds and tests the package, then updates the existing Otzaria listing on pushes to `main`. It uses repository secrets `OTZARIA_USER` and `OTZARIA_PASSWORD`, as in the author’s other plugins. Missing account settings fail visibly; a GitHub push is not itself proof of store publication.

## Store submission

Version 0.9.4 uses the Hebrew name מבואות הש״ס. The user-supplied store image is `store/logo.png`, and the proposed Hebrew listing text is `store/description.txt`. The package passed the actual-package interface tests and official validator with zero errors or warnings. Submission is blocked on store sign-in; no store publication is claimed.

The entire Shabbat/Moed section is excluded at the user’s instruction. The current index contains six broad areas, 89 entries and 251 sourced blocks. Version 0.9.4 also adopts the official Otzaria design guide’s top bar, surface roles, selection controls and UI/reader font separation. Native-app appearance remains unverified.

Version 0.9.5 packages the corrected six-subject build as a distinct store update. The user reports publishing an earlier build; 0.9.5 has not been submitted from this session.

## Reading interface — 0.10.0

The plugin opens to six broad subjects. Choosing one opens its contents; choosing an entry opens the reading view. There is no permanent sidebar and no automatic entry selection. Existing entry and subsection links still work.

The app’s selected reading and UI fonts take precedence. Unmodified Rubik and Noto Serif Hebrew fallback fonts are bundled for offline use, under their included SIL Open Font Licenses; they also prevent browser-dependent fallback typography when opened outside Otzaria. Font assets were copied from the reviewed Otzaria source checkout. The interface follows the app’s theme colors, with a compact top bar and a narrower reading column. Native installation and pixel-for-pixel appearance inside Otzaria remain unverified.

The language pass simplifies headings, removes repetitive editorial instructions throughout the six subjects, and rewrites the opening עולה and אשם explanations without expanding their scope. The actual cited passages were compared for those paragraph rewrites. Qualifications, disputes and source-text uncertainty are retained. See [PROSE-REVIEW-0.10.0.md](PROSE-REVIEW-0.10.0.md). This is not an independent scholarly certification of all entries.

Startup theme colors are cached and applied synchronously before the stylesheet paints. Inside Otzaria, the reading content waits for the initial theme/font setup (with a three-second fallback if host boot fails). The current SDK grants `events.subscribe:theme.changed` as a baseline permission; the manifest does not redundantly request it. The cached/reopen path is tested with the real injected SDK; a native WebView’s own pre-document background remains outside the plugin’s control.
