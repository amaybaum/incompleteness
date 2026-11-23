"""A small json-schema subset validator (type, const, enum, required, properties, items, pattern)."""
import json
import os
import re

here = os.path.dirname(os.path.abspath(__file__))
_types = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'null': type(None)}


def load():
    with open(os.path.join(here, 'schemas', 'oi-ledger-coverage-4.schema.json'), encoding='utf-8') as f:
        return json.load(f)


def _type_ok(v, t):
    if t == 'integer':
        return isinstance(v, int) and not isinstance(v, bool)
    if t == 'number':
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, _types[t])


def validate(doc, sch=None, path='$'):
    sch = load() if sch is None else sch
    errs = []
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
