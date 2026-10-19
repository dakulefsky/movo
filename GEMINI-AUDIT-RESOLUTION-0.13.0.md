# Independent Gemini audit — checked resolutions for the 0.13.0 expansion branch

**Audit baseline:** `9e96e3ff9f6a46b340804a0395ccdd0d3b7cfb16` (released 0.12.3, before the 0.13.0 coverage expansion). The reviewer stated that it inspected 82 explanatory blocks and **28 source segments included in the single-text appendix**, and could not decode the attached binary ZIP. It was **not** an exhaustive audit of the 251-block/214-source installed corpus, nor of version 0.13.0.

## Four source-compared corrections incorporated

| Block | Disposition | Primary source and precise point |
| --- | --- | --- |
| `av-shechitah/person` | **Partially accepted; corrected a misleading proposed patch** | Rambam on Zevachim 3:1, bundled `z3-1#1`. The omitted long-knife example is real: the tamei can stand outside the Azarah and slaughter with a long knife. But the SAME text explicitly says `מפני הטמא שלכתחלה לא ישחוט גזירה שמא יגע בבשר`. The Gemara in Zevachim 32a also calls his slaughter valid *bediavad* while retaining the *lechatchila* prohibition. Therefore we **did not** adopt Gemini's blanket phrasing `אך רשאי לשחוט מבחוץ בסכין ארוך` if meant as advance permission. The new description gives the spatial case and preserves the prohibition. |
| `t-met/scope` | **Accepted (lack of cited external evidence)** | Rambam introduction to Taharot, `t-intro#6`. He explicitly states that gentile corpses do not transmit tumah by *ohel* and explains the differences in tumah rankings for terumah/kodashim vs nazir/tumat mikdash. The broader phrase about what `כל הראשונים` agree upon was not supported by the block's own source, so it was removed rather than implicitly attributed to Rambam. |
| `olah/bird` | **Accepted and expanded by checking the Mishnah as well** | Rambam on Zevachim 6:5, `z6-5#1`, and Mishnah Zevachim 6:5. The source describes `ספגו במלח` as manual spreading and gives a sponge analogy; the Mishnah says `ספגו במלח וזרקו על גבי האישים` for the head and body. The new prose explains the action concretely instead of only saying `מולחים ומקטירים`. |
| `chattat/shem` | **Accepted (style clarification)** | Rambam on Zevachim 1:1, `z1-1#1`, explicitly `אם שחט סתם שהוא כשר ועלה לבעלים`. Replaced the awkward double negative with a clear affirmative. |

These four adjustments alter the **editorial explanation overlay** (`prose_012.json`) only. The original source snapshots, identifiers, source notes, segments and links remain unchanged.

## Verification and automation

- Seven short **exact-source quotation anchors**, together with corresponding excerpts of the edited text, are stored in [GEMINI-AUDIT-FOLLOWUP-0.13.0.json](GEMINI-AUDIT-FOLLOWUP-0.13.0.json).
- The package's Playwright regression test checks that each of those four blocks still refers to the intended source segment and that both source text and explanation include the reviewed passages.
- A matching quote is a **traceability check**, not automatic proof of halachic correctness.

## Apparent 'orphan sources' are mostly an audit-handoff limitation

The reviewer was right that the single **Part II** text appendix contained only 28 primary-source segments: this limited its ability to verify the remaining claims. This does **not** mean those sources are absent from the Otzaria plugin.

Version 0.12.3 actually ships **214 bundled source records**. The installed `data/library.js` contains the corresponding full source texts, with reference IDs and numbered segments. The package tests require every block citation and segment index to resolve to one of these records. The fuller audit ZIP also includes `02_FULL_CORPUS.json`, `03_BLOCK_BY_BLOCK_EVIDENCE.json` and individually accessible `07_READING_PLUGIN_CODE/` files. A text-only model presented with ZIP bytes beginning `PK\\x03\\x04` cannot reliably read those files; it should instead receive the **extracted text files**.

The audit's 'orphan' label was therefore an overstatement about the **plugin**; it accurately reflects **insufficient evidence supplied to that particular review pass**. The 214 bundled texts still require source-by-source critical study, and the earlier audit's 82/251 review scope should not be represented as exhaustive.

## Additional review still needed

- Independently examine the Rambam's Judeo-Arabic original and/or a suitable scholarly translation wherever the Vilna Hebrew is unclear; do not silently alter textual variants.
- Have a qualified `תלמיד חכם` evaluate the legal reasoning and exceptions; textual anchors alone cannot certify that they have been explained correctly.
- Evaluate the full 0.13.0 expansion **after** it builds, especially the 66 additional sections. The Gemini report predates these additions and cannot be presented as reviewing them.
- Review the actual plugin UX by unpacking `.otzplugin` and inspecting/running `app.js`, `index.html`, styles, themes and source controls; the ZIP bytes are not evidence of a UX defect.

## Editorial objective

Source-supported, naturally flowing rabbinic Hebrew. Avoid mechanical replacement of every `הרמב״ם מבאר` with an archaic expression. Any stylistic revision must retain the author attribution, source qualifications and distinction between lemma, example and legal conclusion.
