# מבואות הש״ס — Source-first fifth audit, version 0.13.4

The fifth independent audit supplied **nine findings** regarding missing concepts in the source-based explanations. All findings were compared against the actual released 0.13.3 prose, bundled Mishnah/Rambam texts and the Meiri passage before changes were made. We revised **ten existing explanatory blocks** (the Baalav Imo finding belongs to two existing blocks, not to the block ID supplied by the reviewer). **No new index entries, explanations, study areas or source records** were added; the expected corpus remains **98 introductions / 317 blocks / 215 bundled source records**.

## Findings and editorial dispositions

| Finding | Original source | Resolution in 0.13.4 |
|---|---|---|
| `av-kabbalah/person`: חציצה | Rambam on Zevachim 2:1, `z2-1#1` | **Accepted.** The text now preserves the precise comparison: no barrier between the kohen's hands and the service vessel; equally none between his feet and the Azarah floor. It retains reception in the right hand and the disagreement of R. Shimon with the Sages. |
| `i-yibum/falling`: כל העולה ליבום | Rambam on Yevamot 1:1, `a-yevamot-1-1#1` | **Accepted with an essential qualification.** Added the Rambam's fourth principle: a yevamah excluded from Torah yibum as an *ervah* also requires no chalitzah from that brother, with the co-wife governed by the third principle. **Do not** infer that every forbidden union (including a rabbinic yibum restriction or an ordinary prohibition) is also exempt from chalitzah. |
| Report's `d-shomer-ones/roles`: בעליו עמו | Rambam on Bava Metzia 8:1, `n-Bava_Metzia-8.1#1` | **Accepted; reviewer block ID was incorrect.** `d-shomer-ones/roles` actually defines the **four types of guardian**. The source's time-of-loan discussion belongs to `d-shomrim/ones` and to `d-shomrim/baalav`. Both now explain that when the owner was with the borrower at the moment of borrowing, the borrower is exempt **even if negligent** (`אפילו פשע בה פטור`); the conditions are not satisfied merely by the owner being there at the time of later loss. |
| `av-melikah/blood`: מן הכתוב | Rambam on Zevachim 6:4–5, `z6-4#1` and `z6-5#1` | **Accepted.** Bird sin-offering blood is applied below because the remnant must reach the `יסוד`; the burnt-offering of a bird's blood is applied above because `יסוד` is absent from its verse. The explanation separately contrasts the locations of animal olah and chatat blood, avoiding an overgeneralization based on the offering's name. |
| `k-temurah/meaning`: מלקות ולאו הניתק לעשה | Rambam on Temurah 1:1, `c-Temurah-1.1#1` | **Accepted.** The prohibited substitution is wider than the sanctity effect: public and jointly owned offerings do not make temurah even though the prohibition extends to those who try. This explains why lashes may attach to a prohibition with a related positive command, and restores `כל המימר לוקה, ואין כל מימר עושה תמורה`. |
| `t-ranks/rabbinic`: בשר תאווה | Rambam's introduction to Taharot, `t-intro#23` | **Accepted with correction of the auditor's inference.** The historical decree could classify `בשר תאווה` as a third-level impurity **even without contact with impurity**. But the Rambam also describes successive decrees and concludes that it was later **טהור לתרומה ומטמא את הקודש**. The prose now explicitly preserves the latter limitation rather than wrongly saying it automatically invalidates terumah. |
| `z-shemittat-kesafim/debt`: שטר ושלא בשטר | Rambam on Sheviit 10:1, `a-sheviit-10-1#1–2` | **Accepted.** The introductory account now covers both a loan secured by a document with property-liability terms and one without such terms, and the Rambam's ruling that a land lien by itself does not remove shemittah cancellation. It retains the distinction of `הקפת חנות` and wages that have not been converted into a loan. |
| `d-geneivah/meaning`: חומרת הגנב | Meiri on Bava Kamma 79b, `p-meiri-geneivah#1,3` | **Accepted.** The Meiri's explanation of why secret theft is especially grave—treating human witnesses as more threatening than divine observation—has been restored, including his `דוחק רגלי שכינה` language. The distinction between concealment *of the theft* and the ambush of a roadside robber is preserved. The conceptual explanation is attributed to the Meiri, not presented as a separate legal rule. |
| `a-taam/distinction`: בדיקת הטעם | Rambam on Chullin 8:3, `c-Chullin-8.3#1` | **Accepted with scope limitation.** Rambam refers to checking a mixture's actual taste by a non-Jew, and where such a taster is unavailable and the flavor cannot be checked he discusses the fixed ratio of sixty, including the udder mixed with meat. This records the cited **Rambam passage**, not a general ruling on whether all present-day kosher mixtures can be evaluated by a non-Jew. |

## Evidence-based safeguards

[SOURCE-REVIEW-0.13.4.json](SOURCE-REVIEW-0.13.4.json) preserves **15 paired quotation checks** across **10 distinct blocks**, each with the exact original source ID, filename, one-indexed segment, quoted Hebrew anchor and phrase required to remain in the explanation.

The installable Otzaria package CI is required to:
- ensure each corrected block still cites the specified source and segment;
- confirm the source filename and exact text anchor still match the bundled corpus;
- confirm each explanatory distinction remains visible;
- retain all earlier regression checks, structure and browser interactions;
- ensure the Baalav Imo correction is not mistakenly attached to `d-shomer-ones/roles`, and that the Taharot and taste-checking qualifications are not flattened.

Source-quotation checks are **provenance and regression tests**, not a substitute for rabbinic review. Some cited texts are an older Hebrew rendering of the Rambam's original Judeo-Arabic; nuanced legal applications should be reviewed by a qualified תלמיד חכם, and comparisons with later poskim belong in a separate, explicitly cited commentary layer.

## Remaining product-level concern

Repeated independent audits identify an underlying weakness: short explanatory paragraphs regularly omit the **very source-specific mechanism or exception** that makes a sugya intelligible. The sustainable next step is to expand source-first explanations systematically and independently review interpretation—not merely increase the count of index labels. Historical audit findings must always be checked against the installed version before being labeled “current Hebrew.”
