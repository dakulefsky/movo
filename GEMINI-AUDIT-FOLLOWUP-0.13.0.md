# Independent Gemini audit — review against the 0.13.0 expansion

The external audit supplied by the project owner was based on the **0.12.3 release** (commit `9e96e3ff9f6a46b340804a0395ccdd0d3b7cfb16`), not the 0.13.0 expansion. This record distinguishes corrections supported by the cited Rambam source from an audit tool's unsupported generalizations.

## Source-checked corrections integrated into 0.13.0

| Existing block | Source checked | Resolution |
| --- | --- | --- |
| `av-shechitah/person` | Rambam on Mishnah Zevachim 3:1 (`z3-1#1`) | Restore the case of a טמא standing **outside the עזרה** while slaughtering with a long knife; retain the Rambam's explicit `טמא שלכתחלה לא ישחוט`, rather than turning the example into a blanket permission לכתחילה. Keep the distinction between validity of shechitah and prohibited entry. |
| `t-met/scope` | Rambam, Introduction to Seder Taharot (`t-intro#6`) | State his derivation from `אדם כי ימות באהל` / `אתם קרויין אדם` and retain the passage's own distinction between counts of avot for תרומה וקדשים and other tum'ah applications. Delete uncited comparative claim about other Rishonim. |
| `olah/bird` | Rambam on Mishnah Zevachim 6:5 (`z6-5#1`) | Restore the operative meaning of `ספגו במלח`: applying the salt by hand with a sponge-like motion, rather than generic `מולחים` alone. |
| `chattat/shem` | Rambam on Mishnah Zevachim 1:1 (`z1-1#1`) | Express the דין of שחיטה סתם directly (כשרה ועולה לבעלים לשם חובה) rather than the confusing double negative. |

The previous 0.12.3 editorial overlay already has source-anchored tests; the 0.13.0 Playwright test includes new regressions for all four corrections and their citations. These fixes **do not rewrite the stored primary-source snapshots** or change the entry IDs.

## What the external audit did *not* establish

1. Its assertion that most explanations cite "missing" primary sources is **not proven by the appendix it inspected**. The complete Gemini text audit package supplied to the owner contains **214 source headings and 421 numbered segments** in Part II. Gemini's self-reported count of 28 examined passages is a limit on what it *actually read*, not proof that other cited sources do not exist. A full independent audit must explicitly enumerate all source IDs in the package and mark each as reviewed, skipped or inaccessible.
2. Its code audit is `N/A` because the auditor was unable to inspect the binary ZIP. That is a tool/input limitation, not evidence of a code defect. The main repo includes `plugin/app.js`, `plugin/index.html`, `plugin/style.css`, a build, and regression tests as plain-text files.
3. Automatically replacing phrases like `הרמב״ם מבאר` with more ornate or highly idiomatic phrases would not establish better fidelity. Do not change a demonstrably clear explanation merely to sound older. Style revision should be subordinate to checked content.
4. A quoted substring anchor is a **traceability control**, not proof that every condition in the rewritten halachic statement is correct. Independent human source comparison remains desirable, including possible review of the Rambam's original Judeo-Arabic where translation differences matter.

## Next review procedure

Review one of the six approved broad areas at a time. For each explanatory block, compare **all** its asserted halachic distinctions against the **actual source passages cited**, record the claim and its supporting quote or a concrete contradiction, and avoid a blanket "verified" claim for unread passages. Mark uncertain variants `[לבדיקה ע״י תלמיד חכם]`. Compare the 0.13.0 new entries and depth sections separately from the 0.12.3 wording edits, and never infer that the previous audit exhaustively covered the expansion.

Source texts are reproduced under their respective licensing and edition metadata in the repository's offline source corpus.
