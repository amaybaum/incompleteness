"""A small json-schema subset validator (type, const, enum, required, properties, items, pattern)."""
import json
import os
import re

here = os.path.dirname(os.path.abspath(__file__))
_types = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'null': type(None)}


def load():
    with open(os.path.join(here, 'schemas', 'oi-ledger-coverage-5.schema.json'), encoding='utf-8') as f:
        return json.load(f)


def _type_ok(v, t):
    if t == 'integer':
        return isinstance(v, int) and not isinstance(v, bool)
    if t == 'number':
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, _types[t])


def disposition_problems(doc):
    """Design r6 amendment 3, the complete ledger-path check: one disposition for each drifted ledgered or corpus
    path (the side changes of class base-drift), none for any other path, none twice."""
    if not isinstance(doc, dict) or 'dispositions' not in doc:
        return []
    drifted = [x.get('path') for x in doc.get('side_changes') or [] if isinstance(x, dict)
               and x.get('class') == 'base-drift']
    named = [d.get('path') for d in doc.get('dispositions') or [] if isinstance(d, dict)]
    out = []
    if any(p not in named for p in drifted):
        out.append('missing disposition')
    if any(p not in drifted for p in named):
        out.append('disposition for an unchanged path')
    if len(named) != len(set(named)):
        out.append('two dispositions for one path')
    return out


def validate(doc, sch=None, path='$'):
    top = sch is None
    sch = load() if sch is None else sch
    errs = disposition_problems(doc) if top else []
    if 'const' in sch and doc != sch['const']:
        errs.append('%s: not the constant' % path)
    if 'enum' in sch and doc not in sch['enum']:
        errs.append('%s: not in enum' % path)
    if 'type' in sch:
        ts = sch['type'] if isinstance(sch['type'], list) else [sch['type']]
        if not any(_type_ok(doc, t) for t in ts):
            errs.append('%s: wrong type' % path)
            return errs
    if 'pattern' in sch and isinstance(doc, str) and not re.search(sch['pattern'], doc):
        errs.append('%s: pattern' % path)
    if isinstance(doc, dict):
        for k in sch.get('required', []):
            if k not in doc:
                errs.append('%s: missing %s' % (path, k))
        for k, s in sch.get('properties', {}).items():
            if k in doc:
                errs += validate(doc[k], s, '%s.%s' % (path, k))
    if isinstance(doc, list) and 'items' in sch:
        for i, v in enumerate(doc):
            errs += validate(v, sch['items'], '%s[%d]' % (path, i))
    return errs
