# מבואות הש״ס — Third independent audit resolution (0.13.2)

This pass compared the third Gemini report to **the actual released 0.13.1 files**. The audit's "exact current Hebrew" is not current for several entries: `d-shomrim/four`, `i-edei-get/distinction`, `z-biur/distinction`, `d-chovel/meaning`, `i-shlichut/kiddushin`, `z-challah/dough`, and `a-terefah/meaning` had already been source-checked and rewritten in 0.13.1. No blanket reversion to the audit's proposed wording has been made.

## Newly confirmed explanatory gaps

| Block(s) | Cited evidence | Corrective action |
| --- | --- | --- |
| `z-maaser-sheni/fifth` | Rambam on Maaser Sheni 4:3, `a-maaser_sheni-4-3#1`; Mishnah Maaser Sheni 4:3 | The auditor was right to request the `איסר` case but wrong to call it a **mandatory extra coin for every pidyon**. The Mishnah compares competing redemption offers: owner bids a sela and must add a chomesh, another bids sela plus issar as principal. The other bidder takes priority because the principal is increased even though the owner could potentially avoid the chomesh. The revised prose now explains that precise distinction, without fabricating a new universal redemption requirement. |
| `d-shevuot/distinction` and `d-shevuot/hesset` | Rambam on Shevuot 6:1, `c-Shevuot-6.1#1` | Restored the explicit difference upon refusal to swear: a Torah oath exposes the litigant to court collecting from his property; in the rabbinic oath category the court does not collect by seizure but imposes a procedure of ban, and after thirty days discretionary lashes before lifting the ban. The `היסת` distinction is preserved, including the text's separate description of holding the sacred object. Gemini's generic `מלקין עד שיישבע` would misstate the end of that procedure. |
| `d-dayanim/acceptance` and `d-dayanim/permission` | Rambam Commentary on Sanhedrin 3:1, `n-Sanhedrin-3.1#1`, supplemented with Mishneh Torah, Sanhedrin 4:14–15 (new bundled `mt-sanhedrin-authority#1–2`) | Restored the important territorial scope of permissions to compel parties: an eligible dayan authorized by the exilarch can compel even outside Eretz Yisrael, while authority from an Eretz Yisrael court is territorially limited. The brief Mishnah commentary mentions the Rosh Galuta and Rosh Yeshiva but contains a less complete geographic description; the additional Mishneh Torah passage explicitly supports the world/Eretz Yisrael distinction. |
| `i-kiddushin/way-of-act` | Rambam Commentary on Kiddushin 1:1, `a-kiddushin-1-1#1` | Replaced a shallow contrast about the value of paper with the actual source of kiddushin by shtar, `ויצאה והיתה` — a comparison of entering marriage and leaving it by a document. The explanation retains the concrete examples of pottery and leaves and witnesses. |

All written additions are tied to original Hebrew source passages and nine checkable source/explanation anchors in [SOURCE-REVIEW-0.13.2.json](SOURCE-REVIEW-0.13.2.json).

## Confirmed technical weakness: cross-area related links

Gemini identified real fragile code: the pre-0.13.2 renderer used `H.entries.find(...)` and unconditionally read `next.title`, causing a TypeError if a related link pointed outside the selected handbook. The old build prevented such data by asserting links were restricted to the same handbook. Thus this is a **latent crash** that could surface as soon as an editor introduces a cross-area related link, rather than proof that an existing 0.13.1 installed entry already crashed.

This release:
- Resolves related links through a single global entry-ID map across six handbooks and guards against a missing target.
- Validates links against **all** globally unique entry IDs rather than just the active handbook.
- Adds one useful cross-area related link from `i-kiddushin/way-of-act` (קידושי שטר) to `d-karka` (קנין קרקע), where learners can compare forms of acquisition.
- Adds a Playwright browser test that actually **clicks** the cross-handbook related link, checks the title, active handbook and URL, and injects an invalid link to prove no JavaScript crash occurs.
- Maintains current page routing, RTL layout, offline restrictions and no-network plugin permissions.

## Editorial limits

This is an audit correction and small crosslink demonstration, not a coverage expansion: **98 introductions / 317 explanatory blocks / six study areas** remain. The original 214 source records are unchanged; **one additional Rambam source record** was bundled to support the stronger judicial-jurisdiction claim. An automated quotation match demonstrates citation traceability but cannot determine the final halachic validity of an interpretation. Scholarly inspection of the Rambam's original Arabic, and direct review by a תלמיד חכם, are still valuable.

The audits have correctly found omissions, but the claim that an old quotation is the *current* installed wording must always be checked against the actual release. Never overwrite an already corrected 0.13.1 block with an earlier suggested patch.
