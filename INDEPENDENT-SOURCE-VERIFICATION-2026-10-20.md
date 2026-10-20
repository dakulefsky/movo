# Independent source verification — 2026-10-20 (initial external witness pass)

Scope: compare three high-risk explanations on `audit-0135-repairs` with independent, publicly readable Hebrew texts. These checks do **not** certify the full 317-block corpus or original Arabic readings.

## 1. `minchah/exceptions` — source conflict confirmed, scholarly commentary located

- **Rambam, Commentary on Mishnah Menachot 1:1**: `אבל עומר התנופה אם קמצו שלא לשמו פסול, הואיל ובאת להתיר ולא הותרה` (Wikisource: https://he.wikisource.org/wiki/רמב"ם_על_מנחות_א ; parallel witness: https://wiki.jewishbooks.org.il/mediawiki/wiki/פירוש_המשנה_לרמב%22ם/מנחות/א ).
- **Rambam, Mishneh Torah, Hilchot Pesulei Hamukdashin 14:3 (paragraph d in continuous numbering)**: `מנחת העומר שקמצה שלא לשמה--הרי זו כמי שנעשת לשמה, ושייריה נאכלין` (Mechon Mamre: https://mechon-mamre.org/i/8714.htm ).
- **Tosafot Yom Tov, Menachot 1:1**, in the commentary reproduced with the Mishnah at https://he.wikisource.org/wiki/משנה_מנחות_א_א, observes that the Omer exception follows Rav's statement, which the Gemara challenges, and notes the Rambam does not invalidate it in his Mishneh Torah.

Disposition: maintain both readings and do not assert that the earlier Commentary represents final normative conclusion. Existing on-screen disclosure is directionally correct; the historical/text-critical matter is not settled merely by quoting two witnesses. Editorial follow-up: cite Tosafot Yom Tov explicitly when discussing the discrepancy, rather than asserting no explanation exists.

## 2. `t-kelim/purification` — correction supported

- Rambam, Mishneh Torah, Hilchot Mikvaot 1:3, Mechon Mamre https://mechon-mamre.org/i/a801.htm : `כל הכלים שנטמאו--יש להן טהרה במקוה, חוץ מכלי חרס וכלי זכוכית; וכן המפץ`.
- The Mavo correction excluding glass from purification **of ritual impurity** is supported. Do not use this passage to make a claim about the separate law of immersing newly purchased utensils.

Disposition: the substantive corrected explanation matches this witness.

## 3. `d-shomrim/four` — rabbinic oath confirmed; applicability must remain qualified

- Rambam, Mishneh Torah, Hilchot She'elah uFikadon 6:1–2, Mechon Mamre https://mechon-mamre.org/i/d206.htm : `משביעין אותו בתקנת חכמים שבועה בנקיטת חפץ שאינו ברשותו; ואחר כך משלם`, followed by `והוא הדין לשאר השומרין, כגון השואל`.
- Halakhah 1 distinguishes common interchangeable objects from objects where the guardian might have set his eyes on the particular deposit.

Disposition: the rabbinic character and borrower applicability of this oath are confirmed by this *Mishneh Torah* witness. Its contrast with wording of the bundled *Commentary* must remain marked, not silently harmonized.

## Evidence standard and next review

These are independent public Hebrew witnesses, not an inspection of the original Arabic manuscripts. A verified source quote is not equivalent to a certified interpretation across a full explanatory paragraph. Further audit must enumerate each remaining block, retrieve the exact cited passage/segment, assess positive claims and omitted conditions, and log whether a correction is required. Existing PR #13 technical tests already passed, but technical CI is not a substitute for this editorial review.
