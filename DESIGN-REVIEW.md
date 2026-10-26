# Design and usability review — 0.13.16

Reading toolbar shows the current font size and disables controls at the limits. Slash opens search; Escape closes search and returns focus while retaining the query. Search controls and toolbar wrap in narrow panes. Packaging now derives the version from the manifest. Package browser tests use a local HTTP server for Chromium installations that block file URLs.

## Verification

Full unpacked-package suite passed: 98 entries, 317 sections, source references/dialogs, navigation, search, font persistence and offline checks. No editorial prose or source passages were edited.

All four interfaces checked in Chromium at 320, 390, 600 and 1280 pixels, without page overflow, JavaScript errors or CSP violations. Audio UI checks use a mock Otzaria bridge and a sample library. Installed Otzaria/WebView rendering and physical audio output have not been tested. These are review builds, not store publications.

## Publication reconciliation

The store already contained 0.13.15. Merge its exact published source commit a47025750aafa6c152a7dd4ea7fbaf5c6ca75bf5 and preserve its content corrections, reading structure, glossary and accuracy disclosure. Generated library data was compared to the downloaded live 0.13.15 archive and is identical, including source text and metadata. The editorial corpus version remains 0.13.15; the plugin/UI release is 0.13.16. Keep the published source branch’s optional HTTP test helper. Later unpublished editorial work on that branch is excluded.
