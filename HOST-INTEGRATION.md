# Host integration review — 0.6.0

Reviewed primary implementation: https://github.com/Otzaria/otzaria at commit `9f11690b80bf37703a3d1477a32c677c889dab7b` (dev snapshot retrieved 18 October 2026).

Relevant implementation paths: `lib/plugins/view/plugin_sdk_scripts.dart`, `lib/plugins/bridge/plugin_bridge_adapter.dart`, `lib/plugins/bridge/plugin_search_api.dart`, `lib/plugins/models/plugin_valid_permissions.dart`; corresponding API/design documents under `docs/plugin-sdk`.

The actual injected JavaScript SDK returns ordinary RPC response envelopes and builds an AsyncIterable for search. The previous bare-boolean reader test missed the envelope. The plugin now accepts success only when the envelope has success=true and data=true (and supports the old direct-boolean test path). It propagates bookUid where returned, otherwise numeric identity with type/source, otherwise the returned bookId. It strips highlight markup for phrase comparison and display, does not open stale results, and does not deduplicate different databases by numeric ID alone. Closing the source dialog cancels a pending stream through the SDK iterator return method.

`test_host_sdk.cjs` reads the actual stub and boot script from that pinned checkout at test time. It does not replace `window.Otzaria` with a rewritten mock; only the Flutter RPC transport boundary is doubled. It tests multiple chunks, highlighted text, response envelopes, distinct-database IDs, false opening response, no match, permission denial, stream cancellation and host theme events. Host source is not bundled into the deliverable.

Official validator checkout: https://github.com/Otzaria/otzaria-plugin-validator . The 0.6.0 package was validated with `--app-version 0.9.98 --publish false --fail-on-warnings`; no publication credentials or publishing request were supplied. This verifies declared/API compatibility against the retrieved official spec, not every released host behavior at the minimum version.

Installed-app attempt: downloaded the official Linux `.deb` release `0.9.98+801`, extracted it locally and attempted its `pack-plugin` command. The loader exited 127 because `libwayland-server.so.0` was missing; dependency inspection also found other missing libraries. No host window, installed source catalogue or live reader opening was reached. Do not mark installation or main-app opening as verified from these SDK tests.

The offline reader never needs the app catalogue or internet for the bundled explanations/sources. Native source lookup does require an available locally indexed source; its failure message states that the book may be absent, unindexed or differently worded.
