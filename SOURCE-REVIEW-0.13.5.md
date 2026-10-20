# מבואות הש״ס — Sixth independent source audit, version 0.13.5

**Scope:** A fresh Gemini audit highlighted 16 passages in the released 0.13.4 plugin. These were checked against the **actual bundled Mishnah and Rambam texts**, not adopted mechanically. We revised **16 explanatory blocks** and recorded **20 exact source/updated-prose anchors** in [SOURCE-REVIEW-0.13.5.json](SOURCE-REVIEW-0.13.5.json). The existing six study areas, **98 introductions**, **317 explanatory sections**, **215 bundled sources**, cross-handbook navigation and previous audit tests remain.

## Decisions by block

| Block | Primary source | Source-led editorial resolution |
| --- | --- | --- |
| `i-yuchasin/limits` | Mishnah and Rambam, Kiddushin 3:12 | **Confirmed structural misclassification.** A section entitled “cases without kiddushin taking effect” was mixing those cases with permitted unions whose kiddushin **do** take effect. Renamed the section and explicitly cited Rambam. **Critically, Gemini's proposed Egyptian example was wrong:** Rambam writes that when a second-generation Egyptian man marries a first-generation Egyptian woman, the third-generation child **follows the father** (`והולד הולך אחר הזכר`), not the mother. The ger/mamzeret exception is explained separately. |
| `i-kiddushin/meaning` | Rambam, Kiddushin 1:1 | Restored the contrast between a woman's consent for ordinary kiddushin and Rambam's description of the legal effect of yibbum even without the usual intent/consent. The wording is explanatory, not a statement about present-day conduct. |
| `t-yadayim/distinction` | Rambam, Yadayim 3:2 | Restored the actual argument against extrapolating one rabbinic decree from another: `אין למדין דברי סופרים מדברי סופרים`, and `מאי דתקון תקון`. |
| `i-nissuin/time` | Rambam, Ketubot 5:2 | Restored the separately stated post-marriage terumah/chullin food allowance and distinction from an Israelite betrothed to a kohen who cannot yet eat terumah. |
| `i-gerushin/delivery` | Rambam, Gittin 8:1 | Explained **why** a get in a woman's lap or basket can function even in her husband's domain: he does not object to her occupying that particular space and grants her its place. |
| `z-maaser-sheni/fifth` | Rambam, Maaser Sheni 4:3 | Preserved the prior correction on sela/dinar versus sela/issar, and restored the separate rule that consecrated maaser sheni cannot be transferred by gift after its separation because it is `ממון גבוה`. |
| `z-peah/meaning` | Mishnah and Rambam, Peah 1:2 | Restored the third factor in the amount of peah: `רוב הענווה` or `ענבה`, understood in connection with agricultural yield or grain quality. |
| `z-maaser-ani/biur` | Rambam, Maaser Sheni 5:6 | Clarified the fourth-/seventh-year Passover setting for biur and restored Beit Hillel's exceptional treatment of cooked maaser-sheni food as already `כמבוער`. |
| `t-safek/distinction` | Rambam, Tahorot 4:11 | Restored the explicit **no burning of terumah** ruling when the underlying rabbinic impurity is itself doubtful (e.g., Beit Haperas) and contact is also in doubt, yielding a `ספק ספיקא`. This does not indiscriminately declare all doubtful cases pure. |
| `z-prozbul/meaning` | Mishnah and Rambam, Sheviit 10:4 | Restored judges'/witnesses' signatures and the rabbinic `עד נעשה דיין` basis in the explained prozbul setting. |
| `z-terumah/who` | Rambam, Terumot 1:1 | Explained that the Mishnah's number “five” excludes Rabbi Yehuda's opinion concerning a minor, and retained the `גם אתם` derivation for agency. |
| `d-shevuot/hesset` | Rambam, Shevuot 6:1 | Added the **thirty-day** condition before discretionary lashes after a rabbinic-oath refusal, retaining the earlier distinction between Mishnaic rabbinic oaths and `שבועת היסת` and the subsequent lifting of the ban. |
| `d-edut/meaning` | Mishnah, Sanhedrin 3:6 | Clarified that hearing the debtor say “I owe him” is not by itself testimony of a formally binding acknowledgment; the Mishnah requires `בפנינו הודה לו`. Preserved the separate discussion of adding dayanim when voting remains unresolved. |
| `d-edut/distinction` | Rambam, Sanhedrin 3:6 | Anchored the distinction between conversation and formal acknowledgment in the wording of the Mishnah's rejected testimony, with `הוו עלי עדים` as a recognized form. |
| `d-dayanim/three` | Rambam, Sanhedrin 3:1 | Restored Rambam's distinction concerning nonexperts in the disputes around `זה בורר`; **did not** adopt an unqualified claim that any nonexpert can always be rejected. |
| `d-dayanim/acceptance` | Rambam, Sanhedrin 3:1 and Mishneh Torah Sanhedrin 4:14–15 | Clarified that parties' acceptance of lay judges does not immunize every mistaken judgment. Rambam himself warns that the law of mistaken judgments has **different subcases and disputes**, so the correction does not claim that all mistakes automatically void a judgment. Preserved territorial limits of authority and the earlier phrase-checked requirements. |

## Source evidence and regression coverage

The companion JSON lists **20 direct quotation checks**. Each includes the exact block ID, bundled source ID, source filename, segment number, short Hebrew quotation and the key phrase required in the revised explanation. The packaged browser suite checks source availability, exact segment reference, filename identity and the new prose, plus **all 74 previously recorded audit quotation checks**, home/index navigation, document display, responsive/RTL behavior and IPC integration.

The project remains an **introductory learning tool**. Matches to written source quotations verify provenance but cannot certify a complete interpretation, adjudicate Rishonim, or authorize a practical ruling. Important issues in Gittin, Kiddushin/Yibbum, Maaser Sheni and monetary judgments still deserve review by a qualified תלמיד חכם; some existing source snapshots use older Hebrew translations of the Rambam.

## Product improvement

This sixth audit again shows that many earlier short paragraphs were **accurate in what they did say but incomplete in the reason, exception or outcome central to the source**. Simply generating more section headings is not an adequate remedy. Future editorial work should systematically include source mechanism, scope, and a worked example wherever the source supplies one, with a human scholarly review of difficult cases.
