# Targeted Hebrew prose pass — 0.12.1

This update is a selective literary refinement of existing prose, **not** a content or coverage expansion. The revisions are applied through the existing `prose_012.json` map; the source bundle, original citations, editorial attribution fields and underlying block identifiers have not been changed.

## Blocks revised

| Subject | Sections |
| --- | --- |
| קדשים | `olah/bird`, `av-melikah/portions`, `av-holachah/possible` |
| זרעים | `z-maaser-sheni/use`, `z-biur/meaning` |
| טהרות | `t-sheretz/example` |
| אישות | `i-nissuin/stages` |
| דיני ממונות | `d-chovel/meaning`, `d-shomrim/four` |
| איסור והיתר | `a-terefah/meaning` |

The revisions remove repeated constructions, improve sentence continuity and sharpen distinctions already stated in the preceding text. All ten replacements preserve the paragraph count and the referenced facts. The source-citation and embedded textual apparatus are unchanged. This is a language edit based on the prior sourced revision; it does not establish independent verification of the original Rambam or Arabic text.

## Interface changes

- A subject-based landing page remains the default, with no automatic opening to עולה or another entry.
- Direct search from home, subject counts, and an opt-in recent-entry link based on local storage.
- Source-backed subject directory with RTL group grid; no separate sidebar.
- Continuous reading expands existing sections without disabling normal collapse/expand.
- Responsive typography and an opaque first-paint fallback while waiting for host theme.

## Verification

The Playwright package test now covers the new home search, voluntary resume, continuous reading and the unchanged six-area scope. CI additionally builds a fresh package and runs the official plugin validator. Neither browser tests nor source-level checks prove visual behavior in the installed Otzaria WebView or rabbinic accuracy of every entry. Those remain separate review steps.
