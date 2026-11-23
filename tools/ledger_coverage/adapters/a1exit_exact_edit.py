"""Ledger adapter for the A1-EXIT exact-edit ledger and its edit list."""
import ast
import hashlib
import json

INTERFACE = 'ledger'
NAME = 'a1exit-exact-edit'
VERSION = 2
LEDGER_SCHEMA = 'a1exit deletion exact-edit ledger v2'
EDITS_SCHEMA = 'a1exit deletion edit list v1'
READ_FIELDS = {'schema', 'base', 'edits_sha256', 'retained_unchanged', 'splices', 'files'}


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def load(main, companions, read=None):
    """main: ledger.json bytes; companions: {'edits': edits.json bytes}."""
    errors = []
    led = json.loads(main.decode('utf-8'))
    if led.get('schema') != LEDGER_SCHEMA:
        return {'errors': [('schema', 'unknown ledger schema %r' % led.get('schema'))]}
    edits_b = companions.get('edits')
    edits = json.loads(edits_b.decode('utf-8')) if edits_b is not None else None
    if edits is not None and edits.get('schema') != EDITS_SCHEMA:
        errors.append(('schema', 'unknown edit-list schema %r' % edits.get('schema')))
    if led.get('edits_sha256') is not None and edits_b is not None and _sha(edits_b) != led['edits_sha256']:
        errors.append(('edits_sha256', 'edits.json does not hash to edits_sha256'))
    splices = []
    for s in led['splices']:
        nb = s['new'].encode('utf-8')
        if _sha(nb) != s['new_sha256']:
            errors.append(('hash', '%s: new_sha256 mismatch' % s['id']))
        splices.append({'id': s['id'], 'file': s['file'], 'start': s['start'], 'end': s['end'],
                        'old_sha256': s['old_sha256'], 'new_sha256': s['new_sha256'], 'new': s['new'],
                        'new_bytes': nb})
    by = {}
    for s in splices:
        by.setdefault(s['file'], []).append(s)
    for f, ss in by.items():
        ss.sort(key=lambda x: (x['start'], x['end']))
        for a, b in zip(ss, ss[1:]):
            if b['start'] < a['end'] or (b['start'] == a['end'] == b['end'] == a['start']):
                errors.append(('overlap', '%s and %s overlap in %s' % (a['id'], b['id'], f)))
        for s in ss:
            if s['end'] < s['start']:
                errors.append(('span', '%s: negative span' % s['id']))
    kinds = {e['id']: e.get('kind') for e in (edits['edits'] if edits else [])}
    for s in splices:
        s['kind'] = kinds.get(s['id'])
    retained, mirrors, edit_new = [], [], {}
    if edits is not None:
        prim = {}
        for e in edits['edits']:
            edit_new[e['id']] = e
            if e.get('mirror_of') is None:
                prim[(e['site'], e['part'])] = e['id']
        for e in edits['edits']:
            if e.get('mirror_of') is not None:
                mirrors.append({'id': e['id'], 'mirror_of': prim.get((e['mirror_of'], e['part']))})
        for rid in led.get('retained_unchanged', []):
            e = edit_new.get(rid)
            retained.append({'id': rid, 'site_ref': e['site'] if e else None, 'file': e['file'] if e else None,
                             'text': e['old'] if e else None})
    ignored = sorted(set(led) - READ_FIELDS)
    edit_list = [{'id': e['id'], 'file': e['file'], 'old': e['old'], 'new': e['new'], 'kind': e.get('kind'),
                  'targets': e.get('targets'), 'retained': bool(e.get('retained')),
                  'pin_note': e.get('pin_note')} for e in (edits['edits'] if edits else [])]
    pin_rules = None
    if companions.get('checker') is not None:
        pin_rules = _pin_rules(companions['checker'])
    return {'pin_rules': pin_rules, 'base': led['base'], 'splices': splices, 'files': led['files'], 'retained': retained,
            'mirrors': mirrors, 'ignored_fields': ignored, 'errors': errors, 'edits': edit_list}


def _pin_rules(src):
    """MIN_PIN, PIN_SKIP and PIN_OK of the plan's checker, by ast (never retyped)."""
    vals = {}
    for node in ast.parse(src.decode('utf-8')).body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if getattr(t, 'id', None) in ('MIN_PIN', 'PIN_SKIP', 'PIN_OK'):
                    vals[t.id] = ast.literal_eval(node.value)
    return {'min_len': vals.get('MIN_PIN', 20), 'skip_prefixes': list(vals.get('PIN_SKIP', ())),
            'ok': [{'file': a, 'prefix': b, 'reason': c} for a, b, c in vals.get('PIN_OK', [])]}
