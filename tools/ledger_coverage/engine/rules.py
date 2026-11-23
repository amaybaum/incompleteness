"""Rule schema oi-term-rules/2: allow-rule application, deny-rule examples and countercontrols, lint and widening."""
import re

from . import util

rules_schema = 'oi-term-rules/2'
allow_fields = ['id', 'kind', 'profiles', 'scope', 'matcher', 'context_required', 'max_instances', 'fingerprints',
                'recorded_at', 'positive_examples', 'negative_examples', 'reason', 'author']
deny_fields = ['id', 'kind', 'patterns', 'combine', 'levels', 'scope', 'positive_examples', 'negative_examples',
               'countercontrol', 'reason', 'author']
pattern_fields = ['id', 'kind', 'patterns', 'combine', 'levels', 'scope', 'positive_examples', 'negative_examples',
                  'reason', 'author']


def sentence_context_sha(sents, k):
    prev = sents[k - 1][0] if k > 0 else 'BOF'
    nxt = sents[k + 1][0] if k + 1 < len(sents) else 'EOF'
    return util.sha256(prev.encode('utf-8') + b'\x00' + nxt.encode('utf-8'))


def _neg_match(neg, sentence):
    for n in neg:
        if isinstance(n, dict):
            if re.search(n['regex'], sentence):
                return True
        elif n in sentence:
            return True
    return False


def literal_covers(literal, sentence, span):
    """The literal occurs in the sentence at a position covering the match span."""
    i = sentence.find(literal)
    while i >= 0:
        if i <= span[0] and span[1] <= i + len(literal):
            return True
        i = sentence.find(literal, i + 1)
    return False


def matcher_holds(rule, sentence, neighbours, spans):
    m = rule['matcher']
    if not all(literal_covers(m['literal'], sentence, sp) for sp in spans):
        return False
    pool = sentence + '\n' + '\n'.join(neighbours)
    return all(c in pool for c in m.get('context', []))


def apply_allow(rules, path, sentence, neighbours, ctx_sha, spans, deny_hit, counts, inst_key):
    """Sec. 6.2 steps 1-6 for one hit sentence. Returns (state, class or None, rule id or None)."""
    cand = [r for r in rules if r['kind'] == 'allow' and path in r['scope']['files']
            and matcher_holds(r, sentence, neighbours, spans)]
    if not cand:
        return 'review', 'unclassified', None
    r = cand[0]
    if deny_hit:
        return 'fail', 'deny-match', r['id']
    if _neg_match(r['matcher'].get('negative', []), sentence):
        return 'fail', 'rule-negative-match', r['id']
    ssha = util.sha256(sentence)
    fps = [f for f in r['fingerprints'] if f['file'] == path and f['sentence_sha256'] == ssha
           and (not r['context_required'] or f['context_sha256'] == ctx_sha)]
    if not fps:
        return 'review', 'rule-fingerprint-mismatch', r['id']
    seen = counts.setdefault(r['id'], set())
    if inst_key not in seen and len(seen) >= r['max_instances']:
        return 'fail', 'rule-overreach', r['id']
    seen.add(inst_key)
    return 'pass', None, r['id']


# ---- lint ------------------------------------------------------------------------------------------------

def lint_rule(rule, profile_lookup, sentence_lookup, deny_profiles, control_inputs):
    """Structural, example, fingerprint and countercontrol checks of one rule. Returns a list of problems."""
    out = []
    kind = rule.get('kind')
    need = allow_fields if kind == 'allow' else deny_fields if kind == 'deny' else pattern_fields
    for f in need:
        if f not in rule:
            out.append('%s: missing field %s' % (rule.get('id'), f))
    if out:
        return out
    if kind == 'allow':
        files = rule['scope'].get('files')
        if not isinstance(files, list) or not files or any((not isinstance(f, str)) or f.endswith('/') or '*' in f
                                                           for f in files):
            out.append('%s: scope.files must be exact paths' % rule['id'])
        if rule['max_instances'] != len(rule['fingerprints']):
            out.append('%s: max_instances differs from the fingerprint count' % rule['id'])
        if not rule['positive_examples'] or not rule['negative_examples']:
            out.append('%s: needs at least one positive and one negative example' % rule['id'])
        for fp in rule['fingerprints']:
            got = sentence_lookup(rule['recorded_at'], fp['file'], fp['sentence_sha256'])
            if got is None:
                out.append('%s: fingerprint %s not reproduced at recorded_at' % (rule['id'], fp['sentence_sha256'][:12]))
                continue
            sentence, neighbours, ctx = got
            if rule['context_required'] and ctx != fp['context_sha256']:
                out.append('%s: context fingerprint not reproduced' % rule['id'])
            spans = []
            for pn in rule['profiles']:
                p = profile_lookup(pn)
                if p is None:
                    out.append('%s: unknown profile %s' % (rule['id'], pn))
                    continue
                spans += [(a, b) for _, a, b in p.matches(sentence)]
            if not spans:
                out.append('%s: no trigger in fingerprinted sentence' % rule['id'])
            if not all(literal_covers(rule['matcher']['literal'], sentence, sp) for sp in spans):
                out.append('%s: literal does not cover the trigger' % rule['id'])
        for ex in rule['positive_examples']:
            if not (matcher_holds(rule, ex, [], []) and not _neg_match(rule['matcher'].get('negative', []), ex)):
                out.append('%s: positive example not accepted by the matcher' % rule['id'])
        for ex in rule['negative_examples']:
            if matcher_holds(rule, ex, [], []) and not _neg_match(rule['matcher'].get('negative', []), ex) \
                    and not any(dp.matches(ex) for dp in deny_profiles):
                out.append('%s: negative example accepted by the matcher' % rule['id'])
        return out
    # deny rules and pattern rules
    comp = {}
    try:
        for k, v in rule['patterns'].items():
            comp[k] = re.compile(v)
    except re.error as exc:
        out.append('%s: pattern error %s' % (rule['id'], exc))
        return out

    def hit(text):
        found = {k for k, rx in comp.items() if rx.search(text)}
        return found == set(comp) if rule['combine'] == 'all' else bool(found)

    if not rule['positive_examples'] or not rule['negative_examples']:
        out.append('%s: needs at least one positive and one negative example' % rule['id'])
    for ex in rule['positive_examples']:
        if not hit(ex):
            out.append('%s: positive example not matched' % rule['id'])
    for ex in rule['negative_examples']:
        if hit(ex):
            out.append('%s: negative example matched' % rule['id'])
    if kind == 'deny':
        ccs = rule['countercontrol']
        if not ccs:
            out.append('%s: no countercontrol' % rule['id'])
        for cc in ccs:
            text = control_inputs(cc)
            if text is None:
                out.append('%s: countercontrol input not found' % rule['id'])
                continue
            pats = {cc['alternative']: comp[cc['alternative']]} if cc.get('alternative') else comp
            if rule['combine'] == 'all':
                ok = all(rx.search(text) for rx in comp.values())
            else:
                ok = any(rx.search(text) for rx in pats.values())
            if not ok:
                out.append('%s: countercontrol does not match' % rule['id'])
    return out


def allow_widening(old, new):
    """Sec. 6.3: is the new allow rule wider than the one it supersedes?"""
    why = []
    if set(new['scope']['files']) - set(old['scope']['files']):
        why.append('added files')
    if new['matcher']['literal'] != old['matcher']['literal']:
        why.append('changed literal')
    if len(new['matcher'].get('context', [])) < len(old['matcher'].get('context', [])) or \
            not set(map(str, old['matcher'].get('context', []))) <= set(map(str, new['matcher'].get('context', []))):
        why.append('fewer context literals')
    if not set(map(str, old['matcher'].get('negative', []))) <= set(map(str, new['matcher'].get('negative', []))):
        why.append('fewer negative literals')
    if sorted(util.fingerprint(f) for f in old['fingerprints']) != \
            sorted(util.fingerprint(f) for f in new['fingerprints']):
        why.append('fingerprint set changed')
    if new['max_instances'] > old['max_instances']:
        why.append('larger max_instances')
    if old['context_required'] and not new['context_required']:
        why.append('context_required turned off')
    return why


def deny_widening(old, new):
    why = []
    if util.canonical(old['patterns']) != util.canonical(new['patterns']) or old.get('combine') != new.get('combine'):
        why.append('changed pattern')
    if old['scope'] != new['scope'] and old['scope'] == 'all-corpus' or \
            (isinstance(old['scope'], list) and isinstance(new['scope'], list) and not set(old['scope']) <= set(new['scope'])):
        why.append('narrower scope')
    for k in ('positive_examples', 'negative_examples'):
        if not set(old[k]) <= set(new[k]):
            why.append('removed examples')
    if util.canonical(old['countercontrol']) != util.canonical(new['countercontrol']):
        why.append('countercontrol changed')
    return why
