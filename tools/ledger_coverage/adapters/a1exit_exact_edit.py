"""Ledger adapter for the A1-EXIT exact-edit ledger and its edit list.

Besides reading the ledger, it binds the splices to the frozen plan's edit list exactly as the plan's checker
applies it (design sec. 6.1): P's `variant` selection (the first pair whose `old` occurs exactly once, by the
non-overlapping count of `str.count`), application in edit-list order to a running copy kept as segments, each
replaced occurrence mapped back to a byte span at the base, and the three stricter refusals (a splice for the
unselected variant, one splice over two edits, chained edits). It also returns the per-edit pairs that items 5
and 6 evaluate, and the guard-pin semantics of the edit list (B5), through the ledger interface.
"""
import ast
import hashlib
import json
import re

INTERFACE = 'ledger'
NAME = 'a1exit-exact-edit'
VERSION = 2
LEDGER_SCHEMA = 'a1exit deletion exact-edit ledger v2'
EDITS_SCHEMA = 'a1exit deletion edit list v1'
READ_FIELDS = {'schema', 'base', 'edits_sha256', 'retained_unchanged', 'splices', 'files'}
GUARD_KIND = 'guard-pin'
NOT_PINS = ('message', 'comment')
PIECE_MIN = 12
PIECE_SKIP = ('ok', 'in ', '#')


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def pairs_of(e):
    out = [(e['old'], e['new'])]
    if 'old_step2' in e:
        out.append((e['old_step2'], e['new_step2']))
    return out


def select(e, text):
    """P's variant(): the first pair whose old occurs exactly once (non-overlapping count)."""
    for o, n in pairs_of(e):
        if text.count(o) == 1:
            return o, n
    return None


class Running:
    """A running copy: segments ('H', h_start, text) of original base text and ('I', None, text) of images."""

    def __init__(self, t):
        self.seg = [('H', 0, t)]

    def text(self):
        return ''.join(s[2] for s in self.seg)

    def replace_first(self, o, n):
        """Replace the first occurrence; its base span, or None if it is not inside one base-text segment."""
        t = self.text()
        p = t.index(o)
        q = p + len(o)
        pos = 0
        out = []
        hspan = None
        ok = True
        done = False
        for kind, h0, s in self.seg:
            a, b = pos, pos + len(s)
            pos = b
            if done or b <= p or a >= q:
                out.append((kind, h0, s))
                continue
            if kind == 'H' and a <= p and q <= b:
                hspan = (h0 + (p - a), h0 + (q - a))
                if p > a:
                    out.append(('H', h0, s[:p - a]))
                out.append(('I', None, n))
                if q < b:
                    out.append(('H', h0 + (q - a), s[q - a:]))
                done = True
            else:
                ok = False
                out.append((kind, h0, s))
        if not ok or hspan is None:
            return None
        self.seg = out
        return hspan


def correspondence(edits, splices, read, base):
    """Errors (kind, message) when the splices are not exactly P's application of the edit list at base."""
    errors = []
    files = sorted({e['file'] for e in edits})
    texts = {}
    for f in files:
        data = read(base, f)
        if data is None:
            errors.append(('correspondence', '%s: edited file absent at the base' % f))
            continue
        texts[f] = data.decode('utf-8')
    for e in edits:
        if e['file'] not in texts:
            continue
        if select(e, texts[e['file']]) is None:
            counts = ', '.join('%r occurs %d times' % (o[:40], texts[e['file']].count(o)) for o, _ in pairs_of(e))
            errors.append(('correspondence', '%s: no pair occurs exactly once at the base (%s)' % (e['id'], counts)))
    if errors:
        return errors
    run = {f: Running(t) for f, t in texts.items()}
    by_id = {s['id']: s for s in splices}
    used = set()
    for e in edits:
        f = e['file']
        s = select(e, run[f].text())
        if s is None:
            errors.append(('correspondence', '%s: the edit is lost (no pair occurs exactly once after the '
                                             'edits before it)' % e['id']))
            continue
        o, n = s
        hs = run[f].replace_first(o, n)
        if hs is None:
            errors.append(('correspondence', '%s: chained edit (its occurrence lies in or across an earlier '
                                             'edit\'s image)' % e['id']))
            continue
        hb = (len(texts[f][:hs[0]].encode('utf-8')), len(texts[f][:hs[1]].encode('utf-8')))
        sp = by_id.get(e['id'])
        if o == n:
            if sp is not None:
                errors.append(('correspondence', '%s: a retained edit has a splice' % e['id']))
            continue
        if sp is None:
            errors.append(('correspondence', '%s: edit without a splice' % e['id']))
            continue
        if (sp['file'], sp['start'], sp['end'], sp['new']) != (f, hb[0], hb[1], n):
            errors.append(('correspondence', '%s: splice differs from the plan checker\'s application '
                                             '(splice %s %d-%d, application %d-%d)'
                           % (e['id'], sp['file'], sp['start'], sp['end'], hb[0], hb[1])))
            continue
        old_b = read(base, f)[sp['start']:sp['end']]
        if old_b != o.encode('utf-8'):
            errors.append(('correspondence', '%s: replaced bytes differ from the selected old text' % e['id']))
            continue
        used.add(e['id'])
    for sid in sorted(set(by_id) - used):
        if not any(m[1].startswith(sid + ':') for m in errors):
            errors.append(('correspondence', '%s: splice without an applied edit' % sid))
    return errors


def guard_pins(edits):
    """The updated pin literals the edit list requires, with the plan's own selection rules (B5)."""
    out = []
    for e in edits:
        if e.get('kind') != GUARD_KIND or e.get('pin_note') in NOT_PINS:
            continue
        pieces = [' '.join(x.split()) for x in re.split(r'[\'"]', e['new'])]
        pieces = [x for x in pieces if len(x) >= PIECE_MIN and not x.startswith(PIECE_SKIP)]
        out.append({'id': e['id'], 'file': e['file'], 'pieces': pieces, 'targets': list(e.get('targets') or [])})
    return out


def load(main, companions, read=None):
    """main: ledger.json bytes; companions: {'edits': edits.json, 'checker': the plan checker source}."""
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
    elist = edits['edits'] if edits else []
    kinds = {e['id']: e.get('kind') for e in elist}
    for s in splices:
        s['kind'] = kinds.get(s['id'])
    if edits is not None and read is not None and not errors:
        errors += correspondence(elist, splices, read, led['base'])
    retained, mirrors = [], []
    prim = {}
    for e in elist:
        if e.get('mirror_of') is None:
            prim[(e['site'], e['part'])] = e['id']
    for e in elist:
        if e.get('mirror_of') is not None:
            mirrors.append({'id': e['id'], 'mirror_of': prim.get((e['mirror_of'], e['part']))})
    byid = {e['id']: e for e in elist}
    for rid in led.get('retained_unchanged', []):
        e = byid.get(rid)
        pair = (e['old'], e['new']) if e else None
        if e is not None and read is not None and not errors:
            data = read(led['base'], e['file'])
            pair = select(e, data.decode('utf-8')) if data is not None else None
        identity = pair is not None and pair[0] == pair[1]
        retained.append({'id': rid, 'site_ref': e['site'] if e else None, 'file': e['file'] if e else None,
                         'text': pair[0] if identity else None, 'identity': identity})
    units = [{'id': e['id'], 'file': e['file'], 'kind': e.get('kind'), 'pairs': [list(p) for p in pairs_of(e)],
              'raw_keys': sorted(e)} for e in elist]
    pin_rules = _pin_rules(companions['checker']) if companions.get('checker') is not None else None
    return {'base': led['base'], 'splices': splices, 'files': led['files'], 'retained': retained,
            'mirrors': mirrors, 'guard_pins': guard_pins(elist), 'edit_units': units, 'pin_rules': pin_rules,
            'ignored_fields': sorted(set(led) - READ_FIELDS), 'errors': errors,
            'edit_count': len(elist), 'raw': {'files': led['files'], 'splices': led['splices'], 'edits': elist}}


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
