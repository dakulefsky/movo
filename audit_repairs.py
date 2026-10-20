"""Incremental 0.13.5 source-audit corrections, applied after all prose overlays.

Original source segments are never modified. All edits assert the expected
previous wording to fail loudly on future upstream prose changes.
"""
def apply_audit_repairs(handbooks):
    blocks = {e['id'] + '/' + b['id']: b
              for h in handbooks for e in h['entries'] for b in e['blocks']}
    def replacement(key, before, after):
        b = blocks[key]
        matches = sum(p.count(before) for p in b['paragraphs'])
        assert matches == 1, ('audit-repair original drift', key, matches, before)
        b['paragraphs'] = [p.replace(before, after) for p in b['paragraphs']]
    def note(key, text):
        b = blocks[key]
        assert text not in b['paragraphs'], ('duplicate audit note', key)
        b['paragraphs'].append(text)
    replacement('t-kelim/purification',
        'בשאר מיני הכלים המתוארים נוהגת טהרה במקווה.',
        'שאר הכלים אינם שווים בדרכי טהרתם: כלי זכוכית, אף שגזרו עליהם טומאה, אינם נטהרים מטומאתם בטבילה במקווה; ואילו מיני כלים אחרים נטהרים לפי דיניהם. אין ללמוד מן הכלל שבהקדמה שכל כלי שנזכר נטהר בטבילה.')
    note('t-kelim/purification',
        'הערת מקור: הלשון הכללית שבהקדמה לסדר טהרות טעונה סייג לאור דברי הרמב״ם בהלכות מקוואות א, ג, המוציאים כלי זכוכית מכלל הכלים הנטהרים בטבילה מטומאתם. אין עניין זה נוגע לטבילת כלים הנקנים מן הגוי.')
    replacement('d-shomrim/four',
        'הרמב״ם מוסיף שאף כשהשואל משלם על הדבר שאבד, עליו להישבע תחילה שבועת התורה שאכן אבד, שמא נתן בו עיניו וביקש לעכבו בידו בתשלום.',
        'גם כשהשואל משלם על החפץ שאבד, עשויה להידרש שבועה שאינו ברשותו, מחשש שנתן בו עיניו. במשנה תורה, הלכות שאלה ופיקדון ו, א, מגדיר הרמב״ם שבועה זו כתקנת חכמים, ומבחין בין חפץ מסוים לבין דבר המצוי לקנות כמותו.')
    note('d-shomrim/four',
        'הערת מקור: בנוסח פירוש המשנה המצוטט כאן מופיע הביטוי ״שבועת התורה״, ואילו במשנה תורה נאמר שזו שבועה מתקנת חכמים. אין לטשטש חילוף לשונות זה; טעמו ויחס שני המקורות עדיין טעונים בירור.')
    replacement('minchah/exceptions',
        'ולעומר התנופה דין מיוחד: אם קמצו שלא לשמו פסול, משום שהקרבן בא להתיר את החדש ועדיין לא נעשה ההיתר.',
        'ולעומר התנופה נזכר בפירוש המשנה דין מיוחד, שלפיו אם קמצו שלא לשמו הוא פסול, מפני שבא להתיר את החדש. אולם במשנה תורה, הלכות פסולי המוקדשין יד, ג, כתב הרמב״ם שמנחת העומר שקמצה שלא לשמה הרי היא כאילו נקמצה לשמה, ושייריה נאכלין.')
    note('minchah/exceptions',
        'הערת מקור: שני הנוסחים הנזכרים שונים זה מזה, ואין להציג את פסול העומר כפסיקה מוסכמת ברמב״ם. מקורו של השינוי, יחס המהדורות והאפשרות ליישוב לא הוכרעו בבדיקה זו.')
    replacement('a-neder/meaning',
        'בנדרי איסור חלים על גוף הדבר שנאסר',
        'בנדרי איסור חל האיסור על גוף הדבר שנאסר')
    replacement('a-yadot-kinuyim/meaning',
        'אין הלשון לבדה אוסרת את אכילת חברו',
        'אין הלשון לבדה אוסרת עליו לאכול ממאכלי חברו')
    replacement('i-yibum/house-rule',
        'בלשון הכתוב', 'בדרשת הכתוב')
    return 7
