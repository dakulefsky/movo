# Language and interface revision — 0.10.0

The scope remains six broad subjects, 89 entries, 251 sourced blocks, and 214 source documents. No material on Shabbat/Moed or blessings was reintroduced.

## Language changes

`prose_refresh.py` is applied after the existing fidelity corrections. Its replacements and exact deletions are reviewable in one place. It simplifies section headings, consolidates awkward contents-group names, and removes repetitive instructions such as “one must first determine…” or “this is not a full account…”. It does not replace source texts, add speculative explanations, or remove identified disputes. Necessary distinctions between different offerings, tumah rules, and legal cases remain in the explanations. General scope limits remain accessible under “על המבואות”.

The עולה and אשם paragraph rewrites were compared with the actual bundled passages: Rambam’s introduction to Kodashim §§14, 16, 18, 20–22, 25, 33, 35–37, 39, 41; Mishnah Zevachim 5:4–5 and 6:5; Rambam on Zevachim 1:1, 5:1, 5:4, and 6:5. The revisions preserve the animal/bird distinction, portions, service, compulsory/voluntary offerings, liability for neder/nedavah, the limited cases of asham talui, and the hand/vessel distinction in asham metzora. This list identifies the passages read for the wording changes; it is not a new exhaustive review of every source in the library.

Other changes are language-only headings or deletions of repetitive editorial commentary. Existing source references, bylines, disputes, and visible source-text notes remain. Prior source reviews and their limitations continue to apply. Source matching and tests do not prove interpretation correct.

## Interface

A fresh opening shows the home page. A subject opens a directory, never its first entry. The reading view has breadcrumbs, a return-to-contents button, adjustable type, and expandable sections with the first section initially open. There is no sidebar. The source dialog puts the text first and edition metadata in a disclosure.

Rubik UI and Noto Serif Hebrew reading fallback fonts are bundled under OFL licenses. The host’s supplied fonts, theme and reading line height are respected. Font size now persists only after an explicit user adjustment; the old automatically-written font preference is not treated as a user choice.

## Verification boundary

Actual-package browser tests exercise all entries and blocks, home/directory routing, reload/back, source dialogs, search, related links, keyboard-accessible controls, narrow layout and font loading. The actual pinned host SDK is tested at the JavaScript/Flutter-transport boundary. Installed-app rendering and source opening remain unverified. No claim of pixel identity or independent rabbinic review is made.

## Startup and publishing follow-up

The theme cache is restored by a synchronous head script. Host content stays hidden until the first theme/font setup is ready, with a bounded fallback for failed host initialization. Actual host startup tests cover first opening, theme changes, and reopening with cached colors. The current SDK provides `events.subscribe:theme.changed` as a baseline permission, which the host checks when delivering palette changes and resuming suspended plugins. This does not constitute installed-WebView first-paint verification.

The release workflow follows the existing Yevamos workflow: GitHub Actions secrets OTZARIA_USER / OTZARIA_PASSWORD authenticate the owner’s Otzaria store account. The workflow updates by the unchanged manifest ID and preserves the store image. It fails explicitly if the repository is not connected, rather than claiming publication.
