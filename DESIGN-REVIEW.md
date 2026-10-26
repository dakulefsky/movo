# Design and usability review — 0.13.6

Reading toolbar shows the current font size and disables controls at the limits. Slash opens search; Escape closes search and returns focus while retaining the query. Search controls and toolbar wrap in narrow panes. Packaging now derives the version from the manifest. Package browser tests use a local HTTP server for Chromium installations that block file URLs.

## Verification

Full unpacked-package suite passed: 98 entries, 317 sections, source references/dialogs, navigation, search, font persistence and offline checks. No editorial prose or source passages were edited.

All four interfaces checked in Chromium at 320, 390, 600 and 1280 pixels, without page overflow, JavaScript errors or CSP violations. Audio UI checks use a mock Otzaria bridge and a sample library. Installed Otzaria/WebView rendering and physical audio output have not been tested. These are review builds, not store publications.
