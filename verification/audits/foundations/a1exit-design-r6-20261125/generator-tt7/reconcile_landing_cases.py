"""Prepare the TT7 expectation correction for review and the owner decision under R6.GATE.17.

R6.CTRL.20 and R6.CTRL.29 require the computed landing to be asserted. R6.TREE.7 requires
base-drift for the unreconciled main-side edit. R6.TREE.12 requires the unresolved-conflict
class when the landing bytes differ from the computed composition. Both landings are asserted.
The pinned blob IDs are derived from the neutral fixture's exact text and are also retained by
the independent computed-versus-dropped edit diagnostic at the prior tool head.
"""
import hashlib
import json
from pathlib import Path
import sys


BASE_SHA256 = '91524b2410524afc5df05fca86547e3194c46cd04af65f90018b4d7cabb42b5e'
COMPOSED_BLOB = 'e5cfde9c8f69036d38ec8f8d89b87993b9268d7e'
CANDIDATE_BLOB = '80a00051601605443377fcb9b9f3f03ad52f30ac'


def landing_case(name, blob, expected_classes):
    return {
        'case': name,
        'outcome': 'FAIL',
        'classes_exact': expected_classes,
        'invariants': [
            {'items_include': [{'class': k, 'obligation': 'MAIN', 'file': '$ledgered'}
                               for k in expected_classes]},
            {'composed_blob': COMPOSED_BLOB},
            {'L_blob': blob},
        ],
    }


def generate(base, output):
    raw = base.read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise SystemExit('expected the pinned pre-correction expectations')
    doc = json.loads(raw)
    row, = (r for r in doc['rows'] if r['id'] == 'TT7')
    old = row['expect']['cases']
    if old[-1] != {'case': 'landing under the computed composition', 'outcome': 'FAIL',
                   'classes_include': ['landing-conflict-unresolved']}:
        raise SystemExit('expected the recorded conflicting TT7 case')
    row['expect']['cases'] = old[:-1] + [
        landing_case(old[-1]['case'], COMPOSED_BLOB, ['base-drift']),
        landing_case('landing that drops the main-side edit', CANDIDATE_BLOB,
                     ['base-drift', 'landing-conflict-unresolved']),
    ]
    output.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    generate(*(Path(p) for p in sys.argv[1:]))
