# מבואות הש״ס

An offline Hebrew introductory index for Otzaria, by **DanTheMan**.

The plugin introduces the main subjects and essential processes in קדשים, טהרות, אישות, זרעים, דיני ממונות, and איסור והיתר. Entries are short, with expandable headings, search, related entries, and bundled source passages. The current source version is **0.13.5**, incorporating a sixth source-first audit of the Rambam and Meiri while retaining 98 introductions, 317 sections and globally safe cross-handbook links.

The 0.13.7 readability pass clarifies 203 explanatory paragraphs across all six areas. Original source quotations, references and legal qualifications are preserved. Accuracy remains under review.

Each introduction now follows a reading plan: **what the subject means**, **its main rules and process**, then **distinctions and exceptions**. A linked outline lets readers jump to each passage. Shorter entries omit stages they do not need. Sources remain attached to the passages they support. This presentation change preserves all 98 entries, 317 audited blocks and their full wording.

The 0.13.9 final wording polish smooths 14 remaining sentences without changing sources, legal conditions or the reading plan. Accuracy remains under review.

## Install

Install the **0.13.9** review package from the `Mevoot-Hashas-plugin` artifact of the latest successful [GitHub Actions run](https://github.com/dakulefsky/movo/actions/workflows/release.yml), or update it from the Otzaria plugin store. The older [0.12.0 package](dist/Mevoot-Shas-0.12.0.otzplugin) remains in the repository for comparison. No internet connection or AI service is required by the installed plugin.

The manifest declares Otzaria 0.9.97 or later. Package validation was run against 0.9.98. Selected installation and reading checks passed in native Otzaria; successful indexed-source opening still needs a real library catalogue. See [audit/README.md](audit/README.md) for current validation and scholarly limitations.

## Build offline

Python 3 and its standard library are sufficient. All required source snapshots are included.

```sh
python3 build.py
python3 package.py
```

This generates the content export, editorial data and `plugin/data/library.js`, then creates `dist/Mevoot-Shas-0.13.9.otzplugin`. Build output is reproducible without fetching source texts.

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

## Hebrew prose — 0.11.0

Every existing explanatory section and list has been rewritten for connected rabbinic Hebrew: 89 entries, 251 blocks, the same six subjects. The index is slightly shorter (8,481 editorial words versus 8,767). Source texts and textual notes remain unchanged; one existing claim now also cites the relevant bundled Orlah passage. See [PROSE-REVIEW-0.11.0.md](PROSE-REVIEW-0.11.0.md).

## Hebrew prose — 0.12.0

A second reading of the whole index refined 50 passages across all six subjects, with more direct explanations, smoother transitions and fewer vague summaries of the sources. The cited passages for those edits were read again. The 89 entries, 251 blocks, original source texts, citations and qualifications remain in place. See [PROSE-REVIEW-0.12.0.md](PROSE-REVIEW-0.12.0.md).

## Reading and editorial refinements — 0.12.1

The home screen remains the six approved study areas, with a clearer introduction, direct search, subject-entry counts, and an optional **continue where you left off** control. The last-read link is stored only in local storage; it never opens an entry automatically. The subject directories now lay out groups in RTL reading order. A **קריאה ברצף** button expands all sections for uninterrupted reading; the original expandable sections and reading controls remain available.

The reading view has clearer hierarchy, narrower text measure, source controls, and mobile breakpoints. Theme-wait mode retains an opaque host-matched background rather than displaying transparency while the Otzaria theme initializes. The plugin still follows host theme colors and font roles.

Ten existing editorial paragraphs have received a targeted wording revision across קדשים, טהרות, אישות, זרעים, דיני ממונות and איסור והיתר. No new Torah propositions, source passages, citations, subject areas, cross-references, or entry counts were introduced. See [PROSE-REVIEW-0.12.1.md](PROSE-REVIEW-0.12.1.md). The prose review is not an independent scholarly endorsement. Native Otzaria rendering remains to be verified.

## Hebrew prose — 0.12.2

A close editorial pass revised **126 of 251 explanatory sections** across all six areas (39 קדשים, 22 זרעים, 20 טהרות, 17 אישות, 16 דיני ממונות, 12 איסור והיתר). The goal is lucid, connected rabbinic Hebrew without modern-schoolbook formulations, inflated rhetoric, or artificial transitions. Revisions keep the point of each legal distinction in view and retain explicit qualifications and dissenting opinions.

The revision changes explanation paragraphs only: their number, block identifiers, all source text, attribution, references, links and the six-area scope remain unchanged. The cumulative replacement map is still stored in `prose_012.json` because the existing build/review pipeline uses that filename. This was a literary and internal-consistency review of the previously sourced text, not a fresh independent verification of every Rambam passage against its original. See [PROSE-REVIEW-0.12.2.md](PROSE-REVIEW-0.12.2.md) for the audit scope and editorial examples.

## Source verification and Hebrew prose — 0.12.3

The editorial priority for this pass is to **check the cited primary-source texts before changing the wording**, instead of accumulating stylistic edits that might quietly distort a Rishon's meaning. We inspected 16 existing explanatory sections and their cited Rambam, Mishnah and Ramban passages. Thirteen explanations were revised, while three were left unchanged after checking. The exact reference IDs, bundled source filenames, numbered passages and 19 short source-text anchors are recorded in [SOURCE-REVIEW-0.12.3.json](SOURCE-REVIEW-0.12.3.json) and explained individually in [SOURCE-REVIEW-0.12.3.md](SOURCE-REVIEW-0.12.3.md).

The packaged browser test now checks that each reviewed paragraph continues to cite the expected source and that the source passage and explanation still contain the reviewed quotations/claims. This catches accidental source detachment; it does **not** prove that each interpretation is correct. All original source texts, textual variants, citations, 89 introductions and 251 sourced sections remain intact. A separate comparison with the Rambam's original Arabic and independent rabbinic review have not been performed.

## Substantive introductory coverage — 0.13.0

The previous 89 entries (251 explanatory sections) were judged **too thin to prepare someone for a major sugya**. This version adds **nine distinct, central-sugya introductions**, each with three substantive sections, and adds **39 explanatory sections** to existing introductions. The intended resulting corpus is **98 introductions and 317 sections**, while preserving exactly the six approved study areas—no new Moed or Shabbat area.

New introductions: `k-inner-chattat` (חטאות הפנימיות), `k-matanot` (מתנות הדם ומצוה לעומת עיכוב), `t-mashkin` (טומאת משקין), `i-yuchasin` (תפיסת קידושין וייחוס הוולד), `z-leket-shikcha` (לקט ושכחה), `z-five-grains` (חמשת מיני דגן וחיוב עיסה), `d-two-chazakot` (חזקת קניין וחזקת שלוש שנים), `d-shomer-ones` (אונס ושמירה) and `a-yadot-kinuyim` (ידות וכינויים בנדרים).

All 66 new sections cite numbered passages from the **already bundled primary-source snapshots**; none was drafted as a generic AI-generated survey. The build validates a Hebrew quotation anchor for each block directly against a passage it cites, after Unicode/niqqud normalization, and aborts if an anchor or reference is lost. The new material is kept in `coverage_013_entries.json`, `coverage_013_details_a.json` and `coverage_013_details_b.json` rather than rewriting the preserved source files or the 0.12.3 editorial overlay. See [COVERAGE-REVIEW-0.13.0.md](COVERAGE-REVIEW-0.13.0.md) for the scope and known gaps.

**Limitations:** matching a quotation to the source is a provenance check, not a determination that the explanatory interpretation is correct. The original Rambam Arabic was not checked; these are explanations on the basis of preserved Hebrew translations and Mishnah. Significant halachic claims and nuanced Rishonim still benefit from a human talmid-chacham review.

## Eight source-check corrections — 0.13.1

A second Gemini review identified eight missing legal qualifications in **אישות, זרעים, דיני ממונות** and **איסור והיתר**. We re-read each quoted Mishnah and Rambam passage in the repository before revising the prose. See [SOURCE-REVIEW-0.13.1.md](SOURCE-REVIEW-0.13.1.md) for the full disposition table and [SOURCE-REVIEW-0.13.1.json](SOURCE-REVIEW-0.13.1.json) for 13 machine-checkable source anchors across the eight corrected blocks.

Corrections address the crucial difference between husband-handwritten and scribe-written gittin with one witness; the Rambam's admonition about marrying off a minor daughter; the correct meaning of Challah 2:5 without declaring flour to be consecrated challah; biur of proceeds where applicable; a borrower's oath even when paying; the intent prerequisite for boshet; the inclusiveness of the list of treifot; and Rabbi Yehuda's additional vein requirement in shechita.

**Two proposals were narrowed rather than copied as written:** the Challah passage requires the distinction between an invalid flour designation and challah separated after kneading, and the Shomrim passage must not state that `מתה מחמת מלאכה` is the borrower's only exemption. The new prose and CI source-quotation checks preserve these points. The number of subjects, introductions, blocks and original source records are unchanged from 0.13.0.

## Third audit: source and crosslink corrections — 0.13.2

A third independent report repeated seven findings **already corrected and published in 0.13.1**, and identified new limitations in the maaser sheni illustration, the consequences of refusing an oath, a dayan's territorial authority and the scriptural source of kiddushin by shtar. The new prose was checked against Rambam's cited commentary before editing. For the dayanim jurisdiction comparison a new primary text, **Mishneh Torah, Hilchot Sanhedrin 4:14–15**, was bundled and is now cited directly. This raises the offline source-record count from 214 to 215; the number of explanatory blocks and categories remains unchanged.

The report also identified a real latent JavaScript crash in related links to another handbook. The renderer now uses global entry lookup and skips invalid targets rather than dereferencing `undefined`, and the offline build allows source-valid cross-handbook links. A concrete link from קידושי שטר to קנין קרקע and a Playwright click-through/invalid-link test prove this behavior. See [SOURCE-REVIEW-0.13.2.md](SOURCE-REVIEW-0.13.2.md) for the source-disposition report and [SOURCE-REVIEW-0.13.2.json](SOURCE-REVIEW-0.13.2.json) for nine automated source quotation checks.

The auditor's recommendation to add an איסר **to every** מעשר שני redemption was not adopted: the original משנה and Rambam discuss which of two competing offers takes priority, and the new wording reflects that case exactly. This remains an introductory learning tool, not independent psak or final certification of every Hebrew/Rambam interpretation.

## Fourth source-fidelity review — 0.13.3

Corrects eleven explanatory sections in Yibum/Maamar, Challah, Chazakah, Nedarim, rabbinic oaths, delivery of Gittin by a shaliach, Kilayim outside Israel, witness examination and judicial panel expansion, Orlah, inheritance and monetary acquisition through change. Changes were checked against the actual bundled Mishnah/Rambam passages; original texts and 98/317 explanations count remain intact. Eleven exact source/explanation checks protect the amendments in CI. See [SOURCE-REVIEW-0.13.3.md](SOURCE-REVIEW-0.13.3.md) and [SOURCE-REVIEW-0.13.3.json](SOURCE-REVIEW-0.13.3.json). This verifies source linkage, not halachic correctness certification.

## Fifth independent Torah source audit — 0.13.4

Resolved nine identified omissions in **ten** existing explanatory blocks, covering the two kinds of `חציצה` in receiving korban blood, `כל העולה ליבום עולה לחליצה` and the *ervah* qualification, the `בעליו עמו` exemption even when the borrower was negligent, the verses establishing the upper/lower bird-offering blood applications, why temurah incurs lashes despite the associated positive command, historical `בשר תאווה` impurity decrees and their limits, shemittah of documented loans secured by property, the Meiri's moral explanation of secret theft, and the Rambam's reference to non-Jewish taste testing in Chullin.

The user's audit attached the Baalav Imo ruling to `d-shomer-ones/roles`, but the actual relevant blocks are `d-shomrim/ones` and `d-shomrim/baalav`; neither the four-guardians introduction nor the legal distinction was discarded. The Taharot revision expressly preserves the Rambam's conclusion that the historically decreed `בשר תאווה` is *טהור לתרומה* while *מטמא את הקודש*. The Chullin account describes the Rambam's example, not universal contemporary kashrut practice.

See [SOURCE-REVIEW-0.13.4.md](SOURCE-REVIEW-0.13.4.md) for the exact decisions and [SOURCE-REVIEW-0.13.4.json](SOURCE-REVIEW-0.13.4.json) for 15 machine-checked source-text quotations and matching explanatory phrases. The release does not change the six broad study areas, 98 entries, 317 blocks or 215 source records; it preserves every previous source-audit regression.

## Sixth source-first audit — 0.13.5

A consolidated review of the exact 0.13.4 prose identified one serious ambiguity about inner sin-offering blood applications, several omitted source-specific legal mechanisms, and several false positives. Fifteen existing explanatory blocks were revised after checking the bundled sources; the separate asham species and bird-chattat melikah explanations already covered two alleged omissions, so those blocks were left unchanged. The reviewed changes are in [SOURCE-REVIEW-0.13.5.json](SOURCE-REVIEW-0.13.5.json), with source-text quotation and explanation guards applied at build time. The six approved areas, 98 introductions, 317 blocks and original source records remain intact. Tests check source attachment and wording regressions; they do not constitute independent rabbinic certification.

### Source-first depth additions

Five short introductions were deliberately expanded instead of increasing the index count: inner blood applications (`k-matanot/inner`), the Mishnah's specific standards for unavoidable losses by animal attacks (`d-shomer-ones/wolves`), the five grain species and their related obligations (`z-five-grains/species`), the Meiri's map of Ketubot (`i-ketubah/source-map`), and the distinction between invalid slaughter, retained meilah and the three formulae of the Mishnah (`k-meilah/invalid-service`). See `DEPTH-REVIEW-0.13.5.json` for complete prose and passage anchors. The build and packaged regression tests require both directly cited source evidence and minimum meaningful depth in each revised explanation.

## 0.13.6 review distribution

The plugin and store short description explicitly state that content accuracy is under review. This version carries the adjudicated repairs without declaring scholarly clearance. It can be published from `audit-0135-repairs` by manually running the existing release workflow; no merge into main is required. The workflow checks reviewed evidence preservation instead of overwriting the master ledger. Historical review files retain their 0.13.5 audit basis.
