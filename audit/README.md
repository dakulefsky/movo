# Full source audit checkpoint — 2026-10-20

The single evidence ledger is `master-ledger.json`; `review-queue.csv` is a derived baseline index, not another adjudication ledger. Basis: b320d46, version 0.13.5. Inventory: 317 blocks, 360 claim units, 227 sources. All claim units remain not_reviewed; zero are verified. No scholarly corrections are claimed in this checkpoint.

Environment: Python 3.12.14, Node 24.19.0, Playwright 1.62.1 installed. Run `python3 build.py`, then `python3 package.py`. The ledger was initialized with `python3 generate_audit_ledger.py`. CAUTION: that generator overwrites the master ledger; preserve review findings before rerunning it.

Two consecutive builds produced identical package hashes. Source-copy/inventory integrity, ZIP CRC, JavaScript syntax, and official validator passed. Validator used its bundled SDK spec after live-fetch failure; published=false. Both `npm test` and pinned-source `npm run test:host` were attempted and failed at file navigation due to managed Chromium policy. These are blocked tests, not passes. Native Otzaria was not provisioned or tested.

External requests to mechon-mamre.org, he.wikisource.org, and wiki.jewishbooks.org.il all returned proxy tunnel 403 Forbidden. Enable these domains in environment network settings or supply independent editions to continue the required external witness gates. File-based tests require an authorized browser environment permitting local file navigation. The pinned Otzaria source checkout is /workspace/otzaria-audit-host.

Existing Omer, guardian-oath, and asham-talui textual disagreements are recorded explicitly in the master ledger checkpoint. Earlier targeted verification notes have not been treated as newly verified evidence. No merge, push, store publication, or release was performed.
