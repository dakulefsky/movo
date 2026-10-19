# 0.12.3 — בדיקת מקורות וליטוש לשון

This pass gives **source comparison priority over the number of rewritten paragraphs**. It examines **16 existing explanatory sections**, of which **13 were revised** and **three were checked and left unchanged**. Every audited passage is connected to one or more existing references in `SOURCE-REVIEW-0.12.3.json` (19 source anchors total). The scope remains six areas, 89 introductions and 251 blocks.

## Corrections and clarifications grounded in the actual passages

| Section | Source(s) checked | Editorial decision |
| --- | --- | --- |
| `i-kiddushin/ways` | Rambam, Kiddushin 1:1 | Retain both circumstances named for מכת מרדות: kiddushin by intercourse and kiddushin without preceding shidduchin; distinguish the penalty from the validity of kiddushin |
| `d-onaah/meaning` | Rambam, Bava Metzia 4:3 | Restore the explicit third numerical illustration, a commodity worth seven sold for six, alongside six for five and six for seven |
| `z-biur/distinction` | Rambam, Sheviit 9:2; Ramban, Leviticus 25:7 | Preserve the disagreement between destruction/consumption and hefker; add the Ramban's warning concerning fruit deliberately kept past biur for eating |
| `k-meilah/meaning` | Rambam, Meilah 1:1 | Distinguish מועלין, אין מועלין, and לא נהנין ולא מועלין; no korban does not automatically mean permitted enjoyment |
| `i-maamar/consequence` | Rambam, Yevamot 2:1 | Replace an obscure generic description with the actual illustrative brothers, women and partial kinyan of maamar; leave the original parenthesized textual variant uncorrected |
| `t-ohel/distinction` | Mishnah and Rambam, Oholot 3:7 | Tie the result for a bib beneath the house to the openings to the house and to the outside, not simply to a covered hollow |
| `t-hechsher/conditions` | Rambam, Makhshirin 1:1 | Clarify moisture and intention after produce is detached, preserving the special case where preparation and impurity coincide |
| `d-chazakah/distinction` | Rambam, Bava Batra 3:1 | Name the owner's protest before two and preserve the case in which broken communication due to war affects the owner's knowledge |
| `i-edei-get/meaning` | Mishnah and Rambam, Gittin 9:4 | Distinguish witnesses of signing and delivery. The Mishnah says רבי אלעזר and the preserved commentary says רבי אליעזר: neither original text has been silently amended |
| `a-taam/distinction` | Mishnah, Chullin 8:3; Rambam, Chullin 8:3 | Contrast the isolated meat piece with the pot **after stirring**; avoid treating the piece/pot denominator as identical |
| `a-basar-chalav/meaning` | Mishnah and Rambam, Chullin 8:4 | Make Rambam's specific distinction between permission to cook and rabbinic prohibition to eat meat of chayah and fowl in milk explicit |
| `a-neder/distinction` | Rambam, Nedarim 1:1 | State that “מודר אני ממך” alone is not equivalent to “שאיני אוכל לך”; the latter specifies the food prohibition |
| `d-dayanim/acceptance` | Rambam, Sanhedrin 3:1 | Separate expertise sufficient to judge individually from the authority needed to compel litigants |
| `z-hafrashah/order` | Mishnah, Terumot 3:6 | Checked the order of separation and the distinction between the prohibition of reversal and its effectiveness; wording retained |
| `pesach/eating` | Rambam, Zevachim 5:8 | Checked the preserved assertion about the Torah status of the listed Pesach laws; disputed end-time details remain outside this brief introduction; wording retained |
| `z-sheviit/fruit` | Rambam, Sheviit 7:1 | Checked that the source explicitly assigns Sheviit law to the proceeds of sold produce; wording retained |

## How this remains testable

The browser/package test now reads `SOURCE-REVIEW-0.12.3.json` and verifies all of the following for each anchored claim:

1. The relevant Torah paragraph and block still exist.
2. The block still cites the specified source ID and numbered passage.
3. The included source has the expected filename, and that passage still contains the short quoted Hebrew anchor, after normalization of vowels and punctuation.
4. The revised paragraph still contains the matching explanatory phrase.

These are deliberately *traceability assertions*, not mechanical judgments of Torah accuracy. A passage can contain the quoted source words yet still be explained incorrectly. For that reason, the review is also a manual, close reading of the passages identified above.

## Limits and editorial discipline

The cited texts are the **bundled Hebrew editions/translations** of the sources; the Rambam's Arabic original has not been compared. Original Mishnah, Rambam, Ramban, source notes, edition metadata, uncertain brackets and textual variants were left unchanged. This pass did not modify topics, references, links or the 251-block index, and did not add Shabbat or Moed. Where there is a disagreement among Rishonim or a doubtful wording, the introduction explicitly names the dispute or limits its claim rather than deciding a variant by conjecture.

The improvement should be assessed by fidelity and readability, not by how many paragraphs can be rewritten. The corpus still benefits from a later independent review by a qualified תלמיד חכם.
