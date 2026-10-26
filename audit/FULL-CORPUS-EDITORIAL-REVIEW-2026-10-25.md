# מבואות הש״ס — Full-corpus editorial review: intake and evidence register

Date: 2026-10-25. Branch: audit-0135-repairs.

**Status: IN PROGRESS — NOT CERTIFIED.** This document initiates a review of all 317 explanatory blocks in 98 introductions across six areas; it does not claim they have been read, corrected, independently witnessed, or second-reviewed. The authoritative inventory must be regenerated from the fully overlaid build, as required by FULL-SOURCE-AUDIT-PROTOCOL.md.

## Review order and scope

1. Resolve all 31 high-risk findings from issue #12 and inspect every corresponding proposed repair in PR #13, not merely whether an anchor quote exists.
2. Review the other 286 blocks for claim fidelity, misleading omission, precise citation and textual witnesses.
3. For every block, record original paragraph, claim-by-claim source support, omitted conditions, proposed Hebrew, independent edition URL, adversarial review and status.
4. Edit the **runtime content** only after recording the exact current block and its overlay precedence. Existing documents and proposed patches are not necessarily the current displayed text.
5. Run build, ledger generation, package/runtime tests and second review. No merge or release before these gates.

## Concrete cross-audit findings requiring action

| ID | Concern | Evidence already in repository | Next disposition |
|---|---|---|---|
| `minchah/exceptions` | Rambam Commentary on Mishnah Menachot 1:1 describes the Omer offering differently from Mishneh Torah, Pesulei Hamukdashin 14:3; do not silently choose one as final ruling | INDEPENDENT-SOURCE-VERIFICATION-2026-10-20.md | conflict_unresolved pending scholarly adjudication; retain both citations |
| `t-kelim/purification` | Exclude glass utensils from purification of ritual impurity, without confusing this with immersion of newly purchased utensils | Same verification, Hilchot Mikvaot 1:3 | corrected_pending_recheck |
| `d-shomrim/four` | Rabbinic oath that deposit is not in possession; distinguish from Torah oath and from case where guardian actually owes money | Same verification, Hilchot She'elah uFikadon 6:1–2 | corrected_pending_recheck |
| `i-yuchasin/limits` | Do not place ger marrying mamzeret and Egyptian/Edomite descent under a heading implying kiddushin does not take effect | SOURCE-REVIEW-0.13.5.json; a-kiddushin-3-12 | corrected_pending_recheck |
| `i-yibum/falling` | Distinguish Torah ervah exempt from yibum/chalitzah from other prohibitions that can prohibit yibum without removing chalitzah | SOURCE-REVIEW-0.13.4.md | corrected_pending_recheck |
| `d-shomrim/baalav` | Baalav imo depends on presence at the time of borrowing, not merely at the time of loss | SOURCE-REVIEW-0.13.4.md | corrected_pending_recheck |
| `t-ranks/rabbinic` | Preserve final limitation regarding basar ta'avah: tahor for terumah, metamei kodesh | SOURCE-REVIEW-0.13.4.md | corrected_pending_recheck |
| `a-taam/distinction` | Rambam's non-Jewish taste-testing discussion is not automatically a blanket contemporary practical ruling | SOURCE-REVIEW-0.13.4.md | corrected_pending_recheck |
| `k-meilah/invalid-service` | A rejected service does not automatically remove meilah; distinguish stages of service and debate over sha'at heter | Mishnah Meilah 1:1 and Bavli Meilah 2a, 4b–5a | corrected_pending_recheck |

## Independent witness: Meilah

- Mishnah Meilah 1:1: https://www.mechon-mamre.org/b/h/h58.htm
- Bavli Meilah 2a and 4b–5a: https://mechon-mamre.org/b/l/l5801.htm
- Mishneh Torah, Hilchot Meilah 1:2 and 1:6: https://mechon-mamre.org/i/8901.htm

Specific distinction: the Mishnah states that invalid slaughter in the south does not by itself eliminate meilah. Bavli Meilah 2a explains why this differs from sanctified animals that died. Bavli 4b–5a records disagreement on what constitutes sha'at heter la-kohanim. Mishneh Torah 1:6 distinguishes rabbinically prohibited benefit from Torah-level meilah liability. Any expanded prose must keep these distinct and avoid claiming that every listed invalid service entails Torah-level meilah under every interpretation.

## Editorial style to apply consistently

- Begin with the **definition** of the subject and the essential act or legal status.
- Explain **what makes the distinction necessary**, but only if the cited source supports that explanation.
- Preserve **conditions, exceptions, and disputes** before writing a general rule.
- Use complete, connected rabbinic Hebrew paragraphs, not disconnected slogans or mechanically repeated 'נמצא ש...' endings.
- Expand genuinely terse material within existing entries; do not fabricate additional topics, artificial cases, or reasons.
- Do not attribute the Gemara's explanation to Rambam or attribute a later halachic conclusion to the Commentary.
- Avoid a normative psak where sources disagree; state whose position is being summarized.
- Record exact source edition, location, and witness URL before marking verified.

## Remaining work

All unlisted blocks remain `not_reviewed` in this register, including blocks for which earlier audit files proposed revisions. No automatic promotion to `verified` is allowed. A successful build is technical evidence only. This document is not the generated master ledger.
