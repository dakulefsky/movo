# Source-led fourth independent audit — version 0.13.3

The fourth independent Gemini report was compared to the actual Mavos HaShas 0.13.2 corpus and the bundled Hebrew sources rather than accepted on authority. **Eleven explanatory blocks were revised:** nine pre-existing entries and two source-anchored 0.13.0 depth sections. The original source texts, all six broad study areas, 98 introductions and 317 explanatory blocks were retained.

| Block | Actual source | Important distinction restored |
|---|---|---|
| `i-maamar/consequence` (report inaccurately labeled `i-yibum/maamar`) | Rambam on Yevamot 2:1 | Rachel is forbidden to Levi as `אשת אחיו שלא היה בעולמו`; Leah's special `חולצת ולא מתייבמת` treatment results from the partial force of Reuven's *maamar* together with `צרת ערוה`. The three possible cases—no maamar, complete marriage and maamar alone—are now explicitly distinguished. |
| `z-challah/baker` | Rambam on Challah 2:7 | The Rambam's two explanations of 1/24 for a homeowner vs 1/48 for a baker, including the traditional phrase `האשה עינה רעה`, are identified as reasons quoted by the Rambam, not asserted as present-day observations. Crucially a homeowner's large dough for his son's wedding keeps the homeowner's fraction. |
| `d-chazakah/distinction` | Rambam on Bava Batra 3:1 | The property's **owner** can say `לא הגיע לי דבר` when wartime interruption stopped news that someone occupied his property, explaining why lack of protest fails to support the occupier's claim. |
| `a-neder/meaning` | Rambam on Nedarim 2:2 | Distinguishes forbidding the mitzvah object (a specific sukkah) from making a sacrificial undertaking on the condition of performing a mitzvah: `קרבן עלי כל זמן שמניח תפילין`. |
| `d-shevuot/hesset` | Rambam on Shevuot 6:1 | Rabbinically imposed oaths **mentioned in the Mishnah**, like Torah oaths, require holding a sacred object; the refusal sanctions differ. *Shevuat hesset* is distinguishable also in the way the sacred object is held. The audit's proposed `מלקין עד שיישבע` was not copied since the Rambam prescribes a bounded course and the ban is eventually lifted. |
| `i-shlichut/get` | Rambam on Gittin 1:1 | Where witness signatures are not recognized, `בפני נכתב ובפני נחתם` is accompanied by delivery before two, **who read the document before delivery**. |
| `z-kilayim/grafting` | Rambam on Orlah 3:9, segment 3 | Tree grafting and animal cross-breeding are forbidden from the Torah outside Israel; sowing ordinary *kilayim zera'im* is permitted there, and the specific *kilayim hakerem* sowing is rabbinically forbidden. |
| `d-edut/meaning` | Mishnah and Rambam on Sanhedrin 3:6 | Adds the **separate judicial mechanism** of adding two judges when there is no deciding majority, without conflating witness examination with a balanced panel. |
| `z-orlah/chutz` | Rambam on Orlah 3:9, segment 2 | Restores `ובלבד שלא ילקט ביד`: for the particular permitted case of uncertain origin, someone other than the consumer must pick the grapes. |
| `d-yerushah/meaning` | Rambam on Bava Batra 8:2 | Restores Rambam's multigeneration inheritance illustration from Amram's descendants through Kehat, Levi and the ancestors, instead of replacing it with an unrelated simplified example. |
| `d-gezel/distinction` | Rambam on Bava Kamma 9:1 | Describes the consequence of acquiring through a physical change: a stolen young animal that matures is subsequently slaughtered or sold as the thief's property, so he is exempt from the fourfold/fivefold penalty in that example. |

## Checkable evidence and constraints

[SOURCE-REVIEW-0.13.3.json](SOURCE-REVIEW-0.13.3.json) supplies eleven **literal short quotations**, their original source-ID, filename and segment number, plus the corresponding phrase that must remain visible in the explanatory block. The browser regression test validates all eleven links, primary source strings and the new prose, as well as all older audit checks and the complete interface.

This is a **source-traceability audit, not a certification of halachic conclusions or contemporary practice**. The work did not separately check the Rambam's original Judeo-Arabic or differences from later poskim. Material intended for practical application, particularly Gittin, Yibum, Shavuot, Challa and Orlah, still warrants review by a qualified תלמיד חכם.

## Release behavior

Version 0.13.3 changes the explanatory corpus only, with no new area, entry, source record or navigation model. The earlier 0.13.2 cross-handbook link fix remains intact.
