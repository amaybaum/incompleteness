"""Register the R6.EVID.8 runner after the Amendment 8, 9, and 7 generators.

Usage: python3 -I -B register_rep_build.py EXPECTATIONS A1_CONTROLS OUT
The input digest pins the adopted case definitions. Only the REP-BUILD runner field changes.
"""

import ast
import hashlib
import json
from pathlib import Path
import sys


BASE_SHA256 = '5ba4cba7c4ca7c1ee89b8d7b404cb2f60c93fcec0f095973796b584f073b4551'


def register(base, source, output):
    raw = base.read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise SystemExit('expected the pinned Amendment 7 expectation file')
    doc = json.loads(raw)
    matches = [row for row in doc['rows'] if row['id'] == 'REP-BUILD']
    if len(matches) != 1 or matches[0]['runner'] is not None:
        raise SystemExit('expected one REP-BUILD row with an unset runner')
    tree = ast.parse(source.read_bytes(), filename=str(source))
    definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                   and node.name == 'rep_build_control']
    if len(definitions) != 1 or source.name != 'a1_controls.py':
        raise SystemExit('expected one rep_build_control definition in a1_controls.py')
    matches[0]['runner'] = f'{source.name}:{definitions[0].lineno}'
    output.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    register(*(Path(arg) for arg in sys.argv[1:]))
