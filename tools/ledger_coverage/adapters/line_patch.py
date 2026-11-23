"""Ledger adapter line-patch/1 (synthetic configuration): edits replace one whole line located by its hash."""
import hashlib
import json

INTERFACE = 'ledger'
NAME = 'line-patch'
VERSION = 1
SCHEMA = 'line patch v1'


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def load(main, companions, read=None):
    doc = json.loads(main.decode('utf-8'))
    if doc.get('schema') != SCHEMA:
        return {'errors': [('schema', 'unknown line-patch schema')]}
    base = doc['base']
    splices, files, errors = [], {}, []
    for e in doc['edits']:
        data = read(base, e['file'])
        if data is None:
            errors.append(('span', '%s: file absent at base' % e['id']))
            continue
        pos, hits = 0, []
        for line in data.split(b'\n'):
            if _sha(line) == e['old_line_sha256']:
                hits.append((pos, pos + len(line)))
            pos += len(line) + 1
        if len(hits) != 1:
            errors.append(('span', '%s: old line not unique at base' % e['id']))
            continue
        a, b = hits[0]
        new = '\n'.join(e['new_lines'])
        nb = new.encode('utf-8')
        splices.append({'id': e['id'], 'file': e['file'], 'start': a, 'end': b, 'old_sha256': _sha(data[a:b]),
                        'new_sha256': _sha(nb), 'new': new, 'new_bytes': nb, 'kind': None})
        files[e['file']] = {'base_sha256': _sha(data)}
    return {'base': base, 'splices': splices, 'files': files, 'retained': [], 'mirrors': [], 'ignored_fields': [],
            'errors': errors, 'edits': [], 'pin_rules': {'min_len': 20, 'skip_prefixes': [], 'ok': []}}
