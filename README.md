# מבואות הש״ס

An offline Hebrew introductory index for Otzaria, by **DanTheMan**.

The plugin introduces the main subjects and essential processes in קדשים, טהרות, אישות, זרעים, דיני ממונות, and איסור והיתר. Entries are short, with expandable headings, search, related entries, and bundled source passages. The current package is **0.9.5**.

## Install

Download [Mevoot-Shas-0.9.5.otzplugin](dist/Mevoot-Shas-0.9.5.otzplugin) and import it into Otzaria's plugin manager. No internet connection or AI service is required by the installed plugin.

The manifest declares Otzaria 0.9.97 or later. Package validation was run against 0.9.98. Installation and source opening in a running installed Otzaria application remain unverified; see [VALIDATION.md](VALIDATION.md).

## Build offline

Python 3 and its standard library are sufficient. All required source snapshots are included.

```sh
python3 build.py
python3 package.py
```

This generates the content export, editorial data and `plugin/data/library.js`, then creates `dist/Mevoot-Shas-0.9.5.otzplugin`. Build output is reproducible without fetching source texts.

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

Uploading this repository does not publish the plugin to the Otzaria store. No publication workflow is included.

## Store submission

Version 0.9.4 uses the Hebrew name מבואות הש״ס. The user-supplied store image is `store/logo.png`, and the proposed Hebrew listing text is `store/description.txt`. The package passed the actual-package interface tests and official validator with zero errors or warnings. Submission is blocked on store sign-in; no store publication is claimed.

The entire Shabbat/Moed section is excluded at the user’s instruction. The current index contains six broad areas, 89 entries and 251 sourced blocks. Version 0.9.4 also adopts the official Otzaria design guide’s top bar, surface roles, selection controls and UI/reader font separation. Native-app appearance remains unverified.

Version 0.9.5 packages the corrected six-subject build as a distinct store update. The user reports publishing an earlier build; 0.9.5 has not been submitted from this session.
