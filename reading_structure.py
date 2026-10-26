"""Add a reviewed reading plan without altering the audited explanatory blocks."""
import json
from pathlib import Path


def apply_reading_structure(handbooks):
    plan = json.loads(Path(__file__).with_name('reading_structure_0138.json').read_text())
    seen = set()
    for handbook in handbooks:
        for entry in handbook['entries']:
            key = entry['id']
            structure = plan['entries'][key]
            original = [block['id'] for block in entry['blocks']]
            assert original == structure['block_order'], ('reading-plan baseline drift', key)
            ordered = [id for section in structure['sections'] for id in section['blocks']]
            assert len(ordered) == len(set(ordered)) and set(ordered) == set(original), key
            assert structure['sections'][0]['id'] == 'meaning', key
            assert structure['sections'][0]['blocks'][0] == original[0], key
            entry['readingSections'] = structure['sections']
            seen.add(key)
    assert seen == set(plan['entries']) and len(seen) == 98
    return len(seen)
