# Host integration review — 0.6.0

Reviewed primary implementation: https://github.com/Otzaria/otzaria at commit `9f11690b80bf37703a3d1477a32c677c889dab7b` (dev snapshot retrieved 18 October 2026).

Relevant implementation paths: `lib/plugins/view/plugin_sdk_scripts.dart`, `lib/plugins/bridge/plugin_bridge_adapter.dart`, `lib/plugins/bridge/plugin_search_api.dart`, `lib/plugins/models/plugin_valid_permissions.dart`; corresponding API/design documents under `docs/plugin-sdk`.

The actual injected JavaScript SDK returns ordinary RPC response envelopes and builds an AsyncIterable for search. The previous bare-boolean reader test missed the envelope. The plugin now accepts success only when the envelope has success=true and data=true (and supports the old direct-boolean test path). It propagates bookUid where returned, otherwise numeric identity with type/source, otherwise the returned bookId. It strips highlight markup for phrase comparison and display, does not open stale results, and does not deduplicate different databases by numeric ID alone. Closing the source dialog cancels a pending stream through the SDK iterator return method.

`test_host_sdk.cjs` reads the actual stub and boot script from that pinned checkout at test time. It does not replace `window.Otzaria` with a rewritten mock; only the Flutter RPC transport boundary is doubled. It tests multiple chunks, highlighted text, response envelopes, distinct-database IDs, false opening response, no match, permission denial, stream cancellation and host theme events. Host source is not bundled into the deliverable.

Official validator checkout: https://github.com/Otzaria/otzaria-plugin-validator . The 0.6.0 package was validated with `--app-version 0.9.98 --publish false --fail-on-warnings`; no publication credentials or publishing request were supplied. This verifies declared/API compatibility against the retrieved official spec, not every released host behavior at the minimum version.

Installed-app attempt: downloaded the official Linux `.deb` release `0.9.98+801`, extracted it locally and attempted its `pack-plugin` command. The loader exited 127 because `libwayland-server.so.0` was missing; dependency inspection also found other missing libraries. No host window, installed source catalogue or live reader opening was reached. Do not mark installation or main-app opening as verified from these SDK tests.

The offline reader never needs the app catalogue or internet for the bundled explanations/sources. Native source lookup does require an available locally indexed source; its failure message states that the book may be absent, unindexed or differently worded.

## Audit repair validation — 0.13.5

The audit-0135-repairs suite now extracts the 0.13.5 artifact, checks its manifest version, and uses a clean temporary extraction directory. `OTZARIA_HOST_SOURCE` can select the pinned external source checkout; this task uses `/workspace/otzaria-audit-host`. The SDK revision remains unchanged.

Managed Chromium rejects `file://` navigation in this environment. The optional `MOVO_TEST_TRANSPORT=http` transport serves the exact extracted package on loopback, which this runtime permits. Both package and actual-SDK suites pass through that transport, with assertions against external requests. The default remains file navigation; no policy flags or settings are changed. An HTTP pass establishes package/SDK behavior over HTTP, not native WebView file behavior or an installed app. Native installation and live reader opening remain release-gate work.

Native retry on the repaired corpus: downloaded the official `0.9.98+801` release asset `otzaria-0.9.98+99800-linux.deb` (SHA-256 `cb2cef903b165f1e38a557a23bcc2819ae1af3a05b1e206d416dc62e61880d7f`), verified its published asset digest/size, and extracted it under `work/` without system installation. Running `otzaria pack-plugin` on the repaired plugin exited127 at the loader: missing `libharfbuzz-icu.so.0`. Dependency inspection with its launcher library path also found that bundled `libmount.so.1` lacks `MOUNT_2_40` required by system `libgio-2.0.so.0`. No host window, catalogue or live source opening was reached. Flutter is not installed as an alternative build route. This is a failed native attempt, not a validator pass or native release clearance.

## Resolved native runtime retry

The loader/display failures above are historical. `python3 validate_native.py` now reproduces successful native `pack-plugin` validation on this Debian13 amd64 runtime. It verifies SHA-256-pinned downloads, extracts them only under `work/`, adds the missing harfbuzz-ICU and GLES runtime libraries, selects the system `libmount` ahead of the older bundled copy, and uses a TCP-disabled Xvfb display. It does not change system libraries or managed Chromium policy. Native packaging exits0, ZIP CRC passes, and all ten payload files match the Python-built0.13.5 package byte-for-byte. The receipt is written under `work/native-validation/`.

With the same runtime, the package was installed in an isolated native profile and opened from Tools & Plugins. The native WebView rendered the home page, Hebrew search results, the repaired Orlah harvesting explanation, and the separately attached MT10:11 source dialog. Actual SDK permission denial and, after granting the declared local permissions, the empty-catalogue no-match response were both handled correctly. `--open` starts an isolated GUI profile for repeating these manual checks. Screenshots and their hashes are recorded in the master ledger; no screenshots are bundled with the plugin.

This resolves native packaging/installation and selected native-WebView smoke checks. It does not establish successful opening of an indexed source, since the test profile has no source library. Full Chromium browser suites still use authorized loopback HTTP; the managed `file://` restriction remains unchanged. Scholarly and release approval are still outstanding.
