# Hebrew prose review — 0.11.0

The language revision covers all 89 existing entries and 251 explanatory blocks in the same six subjects. It replaces choppy sentences and repetitive editorial instructions with connected, concise rabbinic Hebrew. It adds no subjects or entries. Editorial word count decreased from 8,767 to 8,481 (whitespace-separated words in explanation paragraphs and lists).

## Source fidelity

The actual bundled passages supporting the explanations were consulted during the rewrite. Rambam, Meiri and editorial explanation remain distinguished. Qualifications, stated disputes and source-text uncertainties remain visible. All 214 bundled source documents, their textual notes, and attribution fields are unchanged. This is an editorial review against the bundled editions, not an independent scholarly certification or a comparison with Arabic originals.

One reference was added: `z-kilayim/grafting` now also cites the already bundled Rambam on Orlah 3:9, segment 3, for the existing geographical qualification. The previously attached Kilayim passages alone did not establish that qualification. No source quotation was rewritten.

The explicit `prose_011.json` mapping covers every existing block. `prose_revision.py` applies it after earlier editorial passes and rejects missing or stale keys. Structural comparison confirmed unchanged entry IDs, navigation links, subject scope and source documents. These checks demonstrate preservation and coverage of the edit, not correctness of interpretation.

## Package checks

The actual 0.11.0 archive passed the browser package test: all 89 entries and 251 section controls, source dialogs, Hebrew search and deep links, navigation, font persistence, narrow and wide layouts, and host success/failure paths. No network requests or JavaScript errors occurred. No screenshots were created.

The official Otzaria validator passed with zero errors, warnings or design notices. Its informational unused-file notice concerns dynamically loaded offline fonts and their licenses.

Native installation and appearance inside the installed Otzaria app remain unverified; browser and injected-SDK tests are not native app end-to-end tests.
