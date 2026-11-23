"""The per-edit unit of items 5 and 6 (sec. 6.1, D6, V1): `register`, `register-caps` and `infinity` evaluated
per edit and per pair of the frozen edit list, as the plan checker's own per-edit scan does, with the parameters
of the reviewed rule file of kind `params` and the profiles extracted from the plan checker's blob.
"""
import re
from collections import Counter

from . import outcome as oc
from . import profiles as pr
from . import util

params_kind = 'params'
params_fields = ['id', 'kind', 'profiles', 'caps_kinds', 'old_rewrite', 'key_normalize', 'key_rules', 'splitter', 'pairs_key',
                 'positive_examples', 'negative_examples', 'reason', 'author']


def find_params(rule_files):
    """The one admitted rule of kind `params` (or None)."""
    found = [r for _, d in rule_files for r in (d or {}).get('rules', []) if r.get('kind') == params_kind]
    return found[0] if len(found) == 1 else None


def _one(profile):
    if profile is None or len(profile.patterns) != 1:
        return None
    return profile.patterns[0][1]


class Unit:
    def __init__(self, params, profiles):
        self.p = params
        self.names = params['profiles']
        self.reg = _one(profiles.get(self.names['register']))
        self.caps = _one(profiles.get(self.names['caps']))
        caps_prof = profiles.get(self.names['caps'])
        self.caps_ok = caps_prof.minus[1] if caps_prof is not None and caps_prof.minus else set()
        inf = profiles.get(self.names['infinity'])
        self.inf = _one(inf)
        self.neutral = inf.minus[1] if inf is not None and inf.minus else []
        self.split = re.compile(params['splitter'])
        self.rewrite = re.compile(params['old_rewrite']['pattern'])
        self.norm = re.compile(params['key_normalize'])
        self.keys = [(re.compile(k['pattern']), k['key']) for k in params['key_rules']]

    def ready(self):
        return None not in (self.reg, self.caps, self.inf)

    def key(self, g):
        k = self.norm.sub(' ', g.lower()).strip()
        for rx, name in self.keys:
            if rx.search(k):
                return name
        return k

    def assertions(self, text):
        out = []
        for sent in self.split.split(text):
            spans = [m.span() for rx in self.neutral for m in rx.finditer(sent)]
            out += [(m.group(0), sent) for m in self.inf.finditer(sent)
                    if not any(a <= m.start() and m.end() <= b for a, b in spans)]
        return out

    def pair(self, eid, kind, old, new):
        reg, caps, inf = [], [], []
        a_new = self.assertions(new)
        a_old = self.assertions(self.rewrite.sub(self.p['old_rewrite']['replacement'], old))
        extra = Counter(self.key(g) for g, _ in a_new) - Counter(self.key(g) for g, _ in a_old)
        for g, sent in a_new:
            k = self.key(g)
            if extra.get(k, 0) > 0:
                extra[k] -= 1
                inf.append((eid, g, sent[:120]))
        for tok in sorted(set(x.lower() for x in self.reg.findall(new)) - set(x.lower() for x in self.reg.findall(old))):
            reg.append((eid, tok))
        if kind in self.p['caps_kinds']:
            for tok in sorted(set(self.caps.findall(new)) - set(self.caps.findall(old)) - set(self.caps_ok)):
                caps.append((eid, tok))
        return reg, caps, inf

    def run(self, units):
        """units: [{id, kind, pairs, raw}] in edit-list order; each pair is evaluated separately."""
        reg, caps, inf = [], [], []
        for u in units:
            for old, new in u['pairs_p']:
                r, c, i = self.pair(u['id'], u.get('kind'), old, new)
                reg += r
                caps += c
                inf += i
        return {self.names['register']: reg, self.names['caps']: caps, self.names['infinity']: inf}


def unit_pairs(units, pairs_key):
    """The pairs the plan checker's per-edit scan evaluates: (old, new), and the second pair when the edit carries
    the key `pairs_key` (the checker's own test)."""
    out = []
    for u in units:
        ps = [tuple(u['pairs'][0])]
        if u.get('raw_keys') is not None and pairs_key in u['raw_keys'] and len(u['pairs']) > 1:
            ps.append(tuple(u['pairs'][1]))
        elif u.get('raw_keys') is None and len(u['pairs']) > 1:
            ps.append(tuple(u['pairs'][1]))
        out.append(dict(u, pairs_p=ps))
    return out


def evaluate(led, params, profiles):
    """Returns (record, items). Fail-closed: a missing parameter record or profile is a FAIL of the unit."""
    units = led.get('edit_units')
    if units is None:
        return None, []
    if params is None:
        return {'evaluated': False, 'why': 'no admitted params rule'}, [
            oc.make_item('TERMS', 'deny-match', 'per-edit unit', None, {'why': 'no params'},
                         detail='the per-edit unit has no admitted register-infinity-params rule: fail closed')]
    u = Unit(params, profiles)
    if not u.ready():
        return {'evaluated': False, 'why': 'profiles missing'}, [
            oc.make_item('TERMS', 'deny-match', 'per-edit unit', None, {'why': 'profiles'},
                         detail='register, register-caps or infinity is missing: fail closed')]
    res = u.run(unit_pairs(units, params['pairs_key']))
    items = []
    for prof, finds in sorted(res.items()):
        for f in finds:
            items.append(oc.make_item('TERMS', 'deny-match', '%s: %s' % (f[0], prof), None,
                                      {'edit': f[0], 'profile': prof, 'token': f[1]},
                                      profiles=[prof], rule_id=[prof], unit='per-edit', edit=f[0], match=f[1]))
    rec = {'evaluated': True, 'edits': len(units), 'counts': {k: len(v) for k, v in sorted(res.items())},
           'findings': {k: [list(x) for x in v] for k, v in sorted(res.items())}}
    return rec, items


def lint_params(rule, checker_src, extracted_splitter):
    """Each parameter equals the literal in the plan checker's per-edit scan and key function (sec. 6.1)."""
    out = []
    for f in params_fields:
        if f not in rule:
            out.append('%s: missing field %s' % (rule.get('id'), f))
    if out or checker_src is None:
        return out or ['%s: no checker source to lint against' % rule.get('id')]
    sn = pr.function_literals(checker_src, rule['lint']['scan_function']) if 'lint' in rule else None
    ik = pr.function_literals(checker_src, rule['lint']['key_function']) if 'lint' in rule else None
    if sn is None or ik is None:
        return ['%s: the checker functions named for the lint are absent' % rule['id']]
    for k in rule['caps_kinds']:
        if k not in sn:
            out.append('%s: caps kind %r is not in the checker\'s per-edit scan' % (rule['id'], k))
    if rule['old_rewrite']['pattern'] not in sn or rule['old_rewrite']['replacement'] not in sn:
        out.append('%s: the old-text rewrite differs from the checker\'s' % rule['id'])
    if rule['pairs_key'] not in sn:
        out.append('%s: the second-pair key differs from the checker\'s' % rule['id'])
    if rule['key_normalize'] not in ik:
        out.append('%s: the key normalization differs from the checker\'s' % rule['id'])
    for k in rule['key_rules']:
        if k['pattern'] not in ik or k['key'] not in ik:
            out.append('%s: key rule %r differs from the checker\'s' % (rule['id'], k['key']))
    if rule['splitter'] != extracted_splitter:
        out.append('%s: the splitter differs from the checker\'s sentence function' % rule['id'])
    return out


def check_examples(rule, profiles):
    """Positive examples must give the stated findings, negative examples none."""
    out = []
    try:
        u = Unit(rule, profiles)
    except (re.error, KeyError, TypeError) as exc:
        return ['%s: params do not compile: %s' % (rule.get('id'), exc)]
    if not u.ready():
        return ['%s: profiles missing for the examples' % rule.get('id')]
    for ex in rule.get('positive_examples', []):
        r, c, i = u.pair('ex', ex.get('kind'), ex['old'], ex['new'])
        got = {u.names['register']: len(r), u.names['caps']: len(c), u.names['infinity']: len(i)}
        if any(got[k] != v for k, v in ex['expect'].items()):
            out.append('%s: positive example %r gives %s' % (rule['id'], ex['new'][:40], got))
    for ex in rule.get('negative_examples', []):
        r, c, i = u.pair('ex', ex.get('kind'), ex['old'], ex['new'])
        if r or c or i:
            out.append('%s: negative example %r gives findings' % (rule['id'], ex['new'][:40]))
    return out


def fingerprint(rec):
    return util.fingerprint(rec)
