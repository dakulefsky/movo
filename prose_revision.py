"""Complete 0.11.0 language revision of the existing introductory index.

Only editorial prose/headings/list wording are replaced. Original source text,
attribution, textual notes, entry IDs, links and subject scope are preserved.
This mapping is explicit so a future content change cannot silently miss review.
"""
import json
from pathlib import Path


def apply_prose_revision(handbooks):
    revisions = json.loads(Path(__file__).with_name('prose_011.json').read_text())
    seen = set()
    for handbook in handbooks:
        for entry in handbook['entries']:
            for block in entry['blocks']:
                key = entry['id'] + '/' + block['id']
                assert key in revisions, f'Unreviewed block: {key}'
                edit = revisions[key]
                assert set(edit) <= {'paragraphs', 'items', 'title'}, key
                if 'items' in edit:
                    assert len(edit['items']) == len(block['items']), key
                block.update(edit)
                seen.add(key)
                # Existing geographical qualification is supported in Orlah 3:9,
                # already bundled, rather than the attached Kilayim passage alone.
                if key == 'z-kilayim/grafting':
                    reference = {'source': 'a-orlah-3-9', 'segments': [3]}
                    if reference not in block['refs']:
                        block['refs'].append(reference)
    assert seen == set(revisions), 'Stale language revisions'
