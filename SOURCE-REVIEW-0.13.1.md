# Source-by-source resolution of Gemini audit #2 — Mavos HaShas 0.13.1

**Scope:** The audit inspected 156 blocks across Ishut, Zeraim, Mammon and Issur, with 139 source records, and identified eight omissions or imprecisions. These results concern the **already released 0.13.0 corpus**, not a hypothetical replacement of the 66 new sections. Each revised block below remains linked to its previously bundled and cited primary source.

**Decision:** All eight explanations were revised. **Seven findings were substantially accepted, and one (Challah) was accepted as an omission but NOT with the proposed interpretation**. The reviewed `prose_012.json` overlay is still the generated corpus's editorial source; the unchanged filename does not mean the edition remains 0.12.0.

## Dispositions

| Block | Source actually read | Finding and disposition |
| --- | --- | --- |
| `i-edei-get/distinction` | Rambam on Mishnah Gittin 9:4, `c-Gittin-9.4#1` | **Accepted.** The three *bediavad* cases do **not** make a scribe-written get with only one witness acceptable. Rambam specifically distinguishes the husband's own handwriting from a scribe's. The latter leads to `תצא והולד ממזר`. |
| `i-shlichut/kiddushin` | Rambam on Mishnah Kiddushin 2:1, `a-kiddushin-2-1#1` | **Accepted.** Restored the linked instruction that a father should not marry off his daughter while she is a minor, until she grows and states whom she wants to marry. The legal ability to effect kiddushin does not eliminate the objection recorded by Rambam. |
| `z-challah/dough` | Mishnah and Rambam on Challah 2:5, `am-challah-2-5#1`, `a-challah-2-5#1–3`; compare Mishneh Torah, Bikkurim 8:1 | **Partially accepted; Gemini's proposed formulation was overconfident.** The original flour designation is ineffective, and the flour must still be treated as requiring challah if it is later kneaded in the requisite quantity. Mishnah's `ואסורה לזרים` is important and was omitted. But Rambam's own commentary uses `ואותה חלה אסורה לזרים` while Mishneh Torah explicitly speaks of kneading the previously designated flour and separating challah `כשאר כל קמח חולין`. Other commentators debate what exactly `ואסורה לזרים` governs. We state Rambam's explanation without silently claiming that the raw designated flour becomes consecrated challah merely by intent. Independent `תלמיד חכם` review is warranted before extending the claim. |
| `z-biur/distinction` | Rambam on Mishnah Sheviit 9:2, `v-Sheviit-9.2#1` and previously cited Ramban, Leviticus 25:7 | **Accepted with qualification.** Rambam expressly applies the biur treatment to **proceeds for which biur is applicable**, not absolutely to all money acquired in any sale. The disagreement between Rambam and Ramban remains identified. |
| `d-shomrim/four` | Rambam on Mishnah Shevuot 8:1, `review-shomrim#1`; other exemptions elsewhere in original entry | **Accepted; corrected an overstatement in the proposed patch.** Rambam says that even when the borrower pays for the item, he first swears a Torah oath that the item really was lost, lest he wish to retain it. The report's suggestion that `מתה מחמת מלאכה` is the **only** exemption ignores `בעליו עמו`; the updated prose preserves the existence of multiple exemptions. |
| `d-chovel/meaning` | Mishnah Bava Kamma 8:1, `q-m-Bava_Kamma-8.1#1` | **Accepted.** Embarrassment liability requires intention in the act: someone falling from the roof who injures and embarrasses is liable for injury but not embarrassment. The wording avoids turning `מתכוון` into a blanket requirement to have intended specifically to embarrass. |
| `a-terefah/meaning` | Rambam on Mishnah Chullin 3:1, `c-Chullin-3.1#1` | **Accepted.** `זה הכלל` incorporates cases beyond the explicit list, such as displaced hip, decayed kidney, cut-off legs and an animal stripped of its skin, each with its own rules. |
| `a-shechitah/meaning` | Rambam on Mishnah Chullin 2:1, `av-chullin#1`; Mishnah Chullin 2:1 | **Accepted with specificity.** `אין הלכה כרבי יהודה` concerns Rabbi Yehuda's additional requirement about the veins. This is **separate** from how many simanim must be cut initially or to validate the act after the fact. |

## Regression evidence

The review ledger [SOURCE-REVIEW-0.13.1.json](SOURCE-REVIEW-0.13.1.json) records **13 explicit primary-source quotations** across **8 blocks**. The package test checks:
1. Each block continues to cite its source and numbered segment.
2. The bundled source retains its original file identity and the reviewed quotation (normalized to ignore niqqud and punctuation).
3. Each new explanation still contains the specific correction.

These assertions establish document traceability rather than independently testing whether every nuanced interpretation is halachically correct. No original source file, textual variant or category was replaced; this pass makes no new coverage claims. The original 98 introductions and 317 explanatory blocks remain intact.

## Open scholarly check

**[לבדיקה ע״י תלמיד חכם]** The interpretation of `ואסורה לזרים` in Challah 2:5 deserves comparison of Rambam's Commentary on the Mishnah with his *Mishneh Torah*, Bikkurim 8:1, and with the Rosh, Rash and other commentators; one cannot safely read a rabbinic injunction regarding that flour as equivalent to the flour acquiring Torah-level challah status. See [Mishnah Challah 2:5](https://he.wikisource.org/wiki/משנה_חלה_ב_ה) and [Rambam, Hilchot Bikkurim chapter 8](https://he.wikisource.org/wiki/רמב%22ם_הלכות_ביכורים_ושאר_מתנות_כהונה_שבגבולין_ח).

## Files and compatibility

No layout, search, host SDK, UI code, source corpus count, or subject hierarchy changed. The installable package and manifest version are bumped to **0.13.1** so Otzaria can identify the update. CI builds the plugin and runs the browser/source checks before publication.
