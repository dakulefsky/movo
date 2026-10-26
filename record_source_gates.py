#!/usr/bin/env python3
"""Append this follow-up's evidence to the master ledger; retain prior checkpoints."""
from collections import Counter, defaultdict
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from source_gate_repairs import manifest

ROOT = Path(__file__).resolve().parent
KEY = 'source_gate_followup_20261026'
RECEIPTS = ROOT / 'audit/reviews/source-gates-2026-10-26'

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

def create_checkpoint(data, ledger):
    plan = manifest()
    previous = {r['claim_id']: r for r in ledger['continuation_20261026']['claim_records']}
    edits = {e['claim_id']: e for e in plan['edits']}
    catalog = defaultdict(list)
    for path in sorted(RECEIPTS.glob('catalog-*.json')):
        receipt = json.loads(path.read_text())
        for url in receipt.get('catalog_urls', receipt['requested_urls']):
            catalog[url].append(str(path.relative_to(ROOT)))
    sources = {}
    for sid, source in data['sources'].items():
        old = ledger['external_witness_catalog'].get(sid, {})
        sources[sid] = {
            'citation': source['citation'], 'display_reference': source['ref'],
            'historical_edition': source['edition'],
            'historical_catalog_url': old.get('url'),
            'fresh_catalog_receipts': catalog.get(old.get('url'), []),
            'gate_2': 'pending_external_edition_identity_and_full_relevant_text_comparison',
            'warning': 'Retrieval is partial context, not full source comparison or verification.'}
    # These named passages have actually been read, separately from the URL sweep.
    for sid, paths, note in [
        ('m1-1', ['witness-01.json', 'witness-02.json'], 'Read Mishnah and Rambam: ordinary menachot do not discharge obligation; sinner/jealousy offerings invalid. The disclosed Omer/code disagreement remains.'),
        ('c-Nedarim-2.2', ['supplement-10-nedarim.json'], 'Read Rambam and adjacent Bartenura. Sukkah forbidden by vow compared with matzah of tevel/hekdesh; distinguish conditional offering obligation. Public Rambam text compresses the final sentence relative to bundled text; no silent emendation.'),
        ('v-Niddah-4.7', ['supplement-06-alternate-spellings.json'], 'Alternate spelling נידה yields the complete Rambam paragraph: three consecutive days, one/two-day watch, seven clean days, midras, no korban for minor zavah. Practical calendar not inferred.'),
        ('c-Yadayim-3.2', ['supplement-06-alternate-spellings.json'], 'Alternate spelling ידיים yields the complete Rambam paragraph: second degree, rabbinic hands/books, dispute and ruling against Rabbi Yehoshua; no extrapolation between decrees.'),
        ('i-meiri', ['supplement-06-alternate-spellings.json', 'supplement-07-context.json'], 'Read complete Ketubot introduction including twelve divisions: rights before/after death, ketubah/tosefet, automatic conditions. Printed edition lineage not established.'),
        ('meiri-ketubot-intro-ending', ['supplement-07-context.json'], 'Read the twelve divisions and their concluding chapter map. No new legal rules inferred from the thematic map.'),
        ('p-meiri-geneivah', ['supplement-09-meiri-bk.json'], 'Read full Meiri section on BK79b: hiding the animal remains theft despite observers; ambushers hiding to prevent flight are robbers; theological explanation is explicitly Meiri. Daf Yomi printed-edition lineage remains unidentified.'),
        ('meiri', ['witness-02.json'], 'Read full Pesachim introduction on Daf Yomi, including chametz, matzah, maror and seder; physical edition lineage remains unidentified.'),
        ('t-intro', ['supplement-01.json', 'supplement-02-tahorot.json', 'supplement-03-tahorot.json', 'supplement-04-tahorot.json'], 'Read relevant Derenbourg introduction contexts across Torah/rabbinic tumah, ranks, liquids, tevul yom and kelim. Difficult avot/rank wording remains; glass/code conflict retained. Ibn Tibbon page is a different translation, not an exact witness for the bundled Derenbourg translation.')]:
        sources[sid]['read_context_receipts'] = [str((RECEIPTS / p).relative_to(ROOT)) for p in paths]
        sources[sid]['same_editor_context_note'] = note
        sources[sid]['independent_review'] = 'pending'
    records = []
    for handbook in data['handbooks']:
        for entry in handbook['entries']:
            for block in entry['blocks']:
                units = [(f'paragraph-{n}', text) for n, text in enumerate(block['paragraphs'], 1)]
                units += [(f'item-{n}', v['label'] + ': ' + v['text']) for n, v in enumerate(block['items'], 1)]
                for unit, text in units:
                    cid = entry['id'] + '/' + block['id'] + '/' + unit
                    old = previous[cid]
                    edit = edits.get(cid)
                    assert text == (edit['after'] if edit else old['current_hebrew']), cid
                    context = deepcopy(old['current_source_context'])
                    records.append({
                        'claim_id': cid, 'handbook': handbook['id'],
                        'current_hebrew': text, 'current_sha256': digest(text),
                        'current_source_context': context,
                        'prior_record': 'continuation_20261026.claim_records:' + cid,
                        'text_unchanged_since_prior_checkpoint': not bool(edit),
                        'current_disposition': old['current_disposition'] if not edit or old['current_disposition'] == 'conflict_unresolved' else 'corrected_pending_recheck',
                        'applied_edit': edit,
                        'source_evidence_keys': sorted({r['source'] for r in block['refs']}),
                        'source_review_scope': 'Named source-context notes above only; URL sweep is not a fresh full-claim review.',
                        'independent_applied_text_second_review': 'pending',
                        'six_gate_status': 'incomplete_not_verified'})
    receipts = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(RECEIPTS.glob('*.json'))}
    return {
        'date': '2026-10-26', 'basis_commit': plan['basis_commit'],
        'status': 'SOURCE_GATE_FOLLOWUP_INCOMPLETE',
        'editorial_sha256': hashlib.sha256((ROOT / 'editorial.json').read_bytes()).hexdigest(),
        'scope': 'Continue the recorded 317-block reading; fresh catalog sweep plus named full-context comparisons. No new full-corpus or independent second-review claim.',
        'entries': 98, 'blocks': 317, 'claim_units': 360,
        'prior_blocks_read_editorially': 317, 'fresh_full_corpus_read_claimed': False,
        'changed_blocks': len(edits), 'changed_paragraphs': len(edits),
        'expanded_blocks': sum(e['expanded'] for e in plan['edits']),
        'source_reference_metadata_repairs': plan['source_metadata'],
        'fresh_catalog_urls_attempted': len(catalog),
        'catalog_access_followup': 'All 146 attempted. Three initially failed; Maaser Sheni canonical underscores, Niddah נידה and Yadayim ידיים succeed in supplement-01 and supplement-06. Page access does not establish edition lineage.',
        'source_evidence': sources, 'receipt_sha256': receipts,
        'claim_records': records,
        'current_disposition_claim_counts': dict(Counter(r['current_disposition'] for r in records)),
        'independently_second_reviewed_changed_blocks': 0,
        'independently_six_gate_verified_blocks': 0,
        'unresolved_conflict_groups': 6,
        'validation': {
            'receipt_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted((RECEIPTS / 'validation').glob('*')) if p.is_file()},
            'scope': 'Preservation, two clean packages, browser, pinned SDK and native packaging. See logs for outcomes; no scholarly clearance or installed-reader indexed-source success inferred.',
            'sdk_initial_failure': 'Initial concurrent run failed its pre-boot hidden-body assertion; subsequent retry passed. Both logs retained.'},
        'release_blockers': [
            'All 317 blocks still require completion of the six protocol gates; named context checks and retrieval do not complete them.',
            'Applied-text adversarial review by another reviewer is pending, including the two changes here and eight prior continuation paragraphs.',
            'Printed-edition lineage/original Judeo-Arabic and per-proposition full-context comparisons remain incomplete; Meiri public access improved without resolving edition identity.',
            'Omer, guardian oath, glass, impurity rank, court and Meilah conflicts remain disclosed; no historical resolution inferred.',
            'Native installed-reader indexed-source opening still requires a real source catalogue; packaging/SDK tests do not replace that check.'],
        'publication': 'not_merged_not_published'}

if __name__ == '__main__':
    path = ROOT / 'audit/master-ledger.json'
    ledger = json.loads(path.read_text())
    ledger[KEY] = create_checkpoint(json.loads((ROOT / 'editorial.json').read_text()), ledger)
    ledger['active_review_checkpoint'] = KEY
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n')
    print('Recorded 360 units; retained historical checkpoints; no verification promotion.')
