# Independent witness pass — 2026-10-27

**Branch:** `audit-0135-repairs`  
**Scope:** one targeted issue-#12 block checked against the exact runtime export and public textual witnesses. This is not certification of the 317-block corpus and does not complete the required adversarial second pass.

## `d-karka/ways` — collateral / collection from purchasers

**Issue #12 concern:** qualify the statement about a prior debt and land sold to a purchaser; an ordinary oral loan does not automatically permit collection from purchasers.

**Exact current runtime wording** (from `Mevoot-Shas-Content.md`, section “קנין קרקע”):

> קרקע נקנית בכסף, בשטר או בחזקה. המשנה מכנה אותה ״נכסים שיש להם אחריות״, והרמב״ם מסביר את הכינוי באמצעות גביית חובות. אם מכר אדם קרקע שהיתה משועבדת כדין לחוב שקדם למכירה, כגון במלווה בשטר המועילה לטריפת לקוחות, עשוי בעל החוב להוציאה מיד הלוקח כשאין לו לגבות מן המוכר. בשונה ממטלטלין, הקרקע משועבדת לגביית החוב.

The following paragraph explicitly adds that collection from purchasers is not permitted for every prior debt: an oral loan is not collected from purchasers because it lacks publicity, while a written loan may be collectible under the applicable rules; it distinguishes the debtor's asset lien from the separate right to collect from purchasers.

**Independent textual witnesses**

1. Mishnah Kiddushin 1:5 and Rambam's Commentary on the Mishnah, same mishnah: https://he.wikisource.org/wiki/משנה_קידושין_א_ה  
   The Mishnah calls real estate “נכסים שיש להם אחריות”; Rambam's commentary explains that label through a prior creditor recovering the sold field from the purchaser if the debtor has no assets to pay.
2. Mishneh Torah, Hilchot Malveh veLoveh 11:4: https://www.mechon-mamre.org/i/d311.htm  
   The text distinguishes a loan documented in a note, which can be collected from purchasers, from an oral loan, which cannot be collected from purchasers because it has no public notice: “ומלווה על פה ... אינו גובה אותה מן הלקוחות: לפי שאין לה קול”.

**Assessment:** the current runtime paragraph is materially qualified in the way required by issue #12 and is consistent with these witnesses. The source check supports the distinction; it does not independently settle every legal nuance of the full paragraph.

**Status:** `corrected_pending_recheck`, not `verified`. Reference and claim checks were performed for this targeted point. The full six-gate process, particularly an independent adversarial second pass and scholarly review, remains outstanding. Do not count this item as source-certified or use it to infer completion of other blocks.


## `t-hechsher/conditions` — consent, drying, and impure liquids

**Issue #12 concern:** retain the timing condition for later consent while moisture remains, and distinguish ordinary pure liquid from impure liquids that both convey impurity and effect the preparation.

**Exact current runtime wording** (from `Mevoot-Shas-Content.md`, section “טומאת כלים” / subsection “עקירה ורצון”):

> כדי שאוכל יוכשר לקבל טומאה, עליו להירטב באחד משבעת המשקים לאחר שנעקר מן הקרקע, וברצון. גם אם נרטב בתחילה שלא לרצון, הסכמה מאוחרת עשויה להכשירו, ובלבד שנתרצה בעוד המשקה על האוכל. אם כבר נתייבש, אין ההסכמה המאוחרת מכשירה אותו מכוח אותה הרטבה. משקין טמאין המטמאים את האוכל ומכשירים אותו בשעת טומאתם נידונים אחרת: אין צורך ברצון להכשר זה, מפני שהטומאה וההכשר באין כאחד. אין ללמוד מכך שהרטבה רגילה במשקה טהור מועילה בלא רצון.

**Independent textual witnesses**

1. Mishneh Torah, Hilchot Tum'at Ochlin 12:1–2: https://mechon-mamre.org/i/a612.htm  
   Halakhah 1 requires the owner's consent and that the produce/liquid have been detached from the ground. Halakhah 2 says liquid that fell on food is effective if it was wanted at the beginning even if not at the end, or wanted at the end even if not at the beginning.
2. *Mincha Tehorah*, “Hechsher Ochlin,” pp. 151–152 in the PDF: https://www.etzion.org.il/sites/default/files/MinchaTehora12-HechsherOchlin.pdf  
   This study explicitly explains Rambam's interpretation: “תחלה” is when the liquid falls on the food, and “סוף” is after the food has become wet; on Rambam's reading, consent is required while the liquid is on the food. It also records a different interpretation by the Rash and Ra'avad, so the wording should be understood as following Rambam, not as an uncontested reading of every Rishon.
3. Rambam, Hilchot Tum'at Ochlin, chapter 2, halakhah 13 (online edition): https://web.yad14.co.il/yad-hachazakah/%D7%A4%D7%A8%D7%A7-%D7%91-%D7%94%D7%9C%D7%9B%D7%95%D7%AA-%D7%98%D7%95%D7%9E%D7%90%D7%AA-%D7%90%D7%95%D7%9B%D7%9C%D7%99%D7%9F-%D7%A1%D7%A4%D7%A8-%D7%98%D7%94%D7%A8%D7%94/  
   The text distinguishes impure liquids: they can make food impure even without the owner's consent because impurity and preparation occur together.

**Assessment:** the core timing distinction and the exception for impure liquids are supported by these witnesses. The current wording correctly preserves the difference between Rambam's interpretation and the alternative interpretation noted by later authorities. This targeted check does not replace verification of the full source citation, bundled segment, or all surrounding claims.

**Status:** `corrected_pending_recheck`, not `verified`. Independent adversarial second pass and scholarly review remain outstanding.


## `i-edei-get/distinction` — one signature, valid delivery witnesses, and `מזויף מתוכו`

**Issue #12 concern:** condition the severe outcome on absence of valid עדי מסירה; assess a defective signature (`מזויף מתוכו`) separately.

**Exact current runtime wording** (from `Mevoot-Shas-Content.md`, section “עדי חתימה ועדי מסירה”):

> המשנה מונה שלושה גיטין פסולים שאם נישאת בהם האשה, הוולד כשר. אחד מהם הוא גט שאין עליו אלא עד אחד; הרמב״ם מעמיד מקרה זה בגט שכתב הבעל בכתב ידו. אם כתבו סופר ואין עליו אלא עד אחד, ולא נמסר בפני שני עדים כשרים, אין זה גט. חסרון החתימות כשלעצמו אינו קובע תוצאה זו: גט שאין עליו חתימות כשר כשנמסר כדין בפני שני עדים כשרים, כמבואר בהלכות גירושין א.

The next paragraph separately states that a validly witnessed delivery can validate a get with no signatures, but does not cure the distinct problem of a valid and an invalid signature within the get.

**Independent textual witness**

Rambam, Mishneh Torah, Hilchot Gerushin 1:13–18: https://he.wikisource.org/wiki/רמב%22ם_הלכות_גירושין_א  
- 1:13: delivery must occur before witnesses; delivery privately, even before one witness, is not a get.
- 1:14: a get in the husband's handwriting with one signature is treated as invalid (פסול) and disqualifying for priesthood, not simply equated with a get delivered privately.
- 1:15–16: signatures were instituted as a safeguard, while the essential act is delivery before witnesses; a get with proper signatures can remain valid despite a defective delivery-witness situation under the stated conditions.
- 1:17: one valid and one invalid signature is treated as `מזוייף מתוכו` and is invalid even if delivered before two valid witnesses.
- 1:18: a get with signatures too far from the text can be valid when properly delivered before witnesses, including when no signatures are present.

Rambam, Hilchot Gerushin 3:8, also discusses a get with an invalid signature or only one witness and distinguishes the status of `מזוייף מתוכו`; its exact relationship to the chapter-1 cases must not be flattened into one blanket rule: https://he.wikisource.org/wiki/רמב%22ם_הלכות_גירושין_ג

**Assessment:** the current text now distinguishes (a) a lack of valid delivery witnesses, (b) no signatures but valid delivery witnesses, and (c) a defective signature within the get. These are materially different cases in Rambam's text. The source supports the distinctions; full source-segment and edition checks and an independent adversarial review remain.

**Status:** `corrected_pending_recheck`, not `verified`. This check is limited to the flagged block and does not certify the whole gittin entry.
