# מבואות הש״ס — הרחבת כיסוי 0.13.0

## What changed and why

The installed 0.12.3 corpus contained 89 entries and 251 blocks. Many major sugyas had just two paragraphs of roughly 30–50 words each. Such a corpus is useful as a glossary, but insufficient as an introduction comparable in purpose to a thoughtful opening to an Artscroll masechta or sugya.

This edition addresses **real substance**, not a count of labels. It adds nine introductions covering important missing conceptual distinctions, each with three explanatory units, plus 39 deeper units distributed among existing entries. The total expected output is 98 entries / 317 blocks. Existing 251 editorial blocks and their source attributions remain intact.

The six top-level study areas remain **קדשים, טהרות, אישות, זרעים, דיני ממונות, איסור והיתר**. There is deliberately no new Shabbat or Moed category.

## Nine sourced subject introductions

| Broad area | Introduction | Primary passages used for the new units |
| --- | --- | --- |
| קדשים | חטאות הפנימיות | משנה זבחים ה:א–ב; פירוש הרמב״ם זבחים ד:ב |
| קדשים | מתנות הדם: מצוה ועיכוב | משנה ופירוש הרמב״ם זבחים ד:א–ב |
| טהרות | טומאת משקין | הקדמת הרמב״ם לטהרות, segments 24–25 |
| אישות | תפיסת קידושין וייחוס הוולד | משנה ופירוש הרמב״ם קידושין ג:יב |
| זרעים | לקט ושכחה בשעת הקציר | פירוש הרמב״ם פאה ד:י, ו:ו |
| זרעים | חמשת מיני דגן וחיוב עיסה | משנה חלה א:א; פירוש הרמב״ם שם |
| דיני ממונות | חזקת קניין וחזקת שלוש שנים | פירוש הרמב״ם קידושין א:ה; בבא בתרא ג:א |
| דיני ממונות | אונס ושמירת הבהמה | משנה בבא מציעא ז:ח–ט; פירוש הרמב״ם שם |
| איסור והיתר | ידות וכינויים בנדרים | פירוש הרמב״ם נדרים א:א |

## Thirty-nine expansions of existing introductions

- **קדשים:** הפשט וניתוח; אשם תלוי; סמיכה ותנופה; לחמי תודה; שלא לשמה במנחות; מחשבה בעבודה המעכבת; מעילה; בעלות בתמורה
- **טהרות:** דרגות חולין, תרומה וקודש; כלי זכוכית; כלי חרס; היסט; טבול יום; שומרת יום; דוגמת הביב באהלות
- **אישות:** קידושי שטר; עיקר ותוספת כתובה; גוף הגט; בית אחד בייבום; כוח המאמר; דייני החליצה
- **זרעים:** שיעור פאה; גמר מלאכה; חומש הפדיון; חלת בעל הבית ונחתום; דמי פירות שביעית; אזורי ביעור
- **דיני ממונות:** חילוקי האבות; בעליו עמו; עיקרי נחלות; זמן תביעת אונאה; היסת לעומת שבועת תורה; קבלת דיינים
- **איסור והיתר:** חמישה מפסידי השחיטה; נקב בקרומים בטרפה; גזירת שולחן בבשר בחלב; כחל; נדר במקום מצווה; אכילה ושתייה בשבועה

## Evidence and limits

1. Every new block cites at least one bundled primary-source segment (the previously preserved Hebrew editions and translations).
2. Every new block records a short source-text quotation, and `coverage_013.py` makes the package build fail if the quotation is no longer found in the **specific passage it cites**.
3. Block IDs are unique within each entry; entry IDs are unique across the library; related links must resolve within the broad study area.
4. All 251 previously edited explanations remain subject to the existing prose revision and 0.12.3 source-led regression tests. No source text or textual variant was replaced.
5. Structural tests should assert 98 entries, 317 explanatory sections and six broad areas; browser tests still exercise the installed plugin’s navigation, Hebrew search, source dialogs, and mobile reading.

**Crucial limitation:** Finding an exact quotation in the Rambam does not by itself prove that a new explanation correctly states every condition of the halacha. This is a **traceability safeguard**, not automatic rabbinic certification. Material has been drafted and checked against the cited Hebrew texts; an independent תלמיד חכם should inspect difficult cases, disagreement among Rishonim, and any passage intended as authoritative.

## Further coverage priorities, not yet claimed

The index is still not a full Artscroll-style multi-page introduction to every masechta. Some central gaps remain: individual classes of menachos and their exceptions; non-mental pesulei avodah and exact avodas Yom Kippur; tumas negaim and full Taharot/Oholot case maps; deeper Get/Chalitzah and Ketubot sugyot; further laws of trumah/demai/bikkurim; full Choshen Mishpat treatment of the avot, kinyanim and loans; and broader Issur/Heter beyond the current Chullin/Nedarim/Shevuot selections.

Future expansions should be selected by the importance of a sugya, not by the ability to produce more index terms, and should continue to be anchored to actual source passages.
