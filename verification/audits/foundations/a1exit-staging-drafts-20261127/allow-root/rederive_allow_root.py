"""WIP / UNVERIFIED staging draft, not frozen, not reviewed, not adopted.

Second derivation of the five allowances of the designated first allow record `a1-staging-allow-root.json`
(A1 staging amendment r2, sec. 2, "Allow-rule record"; design r6 R6.RULE.2, R6.RULE.4 to .7, R6.RULE.10 to .12,
R6.REC.13, R6.REC.14), written independently of `../derive_rule_drafts.py`: it neither imports nor reads that
script, its report or the superseded rule file `w1-w2-allow-v3.json`.

What is taken as given, for each rule, is its meaning: `profiles`, `matcher` (literal, context literals, negative
literals), `context_required` and `reason`, read from the draft root. Everything R6.REC.14 asks to be re-derived is
derived here from bytes at H alone and then compared with the draft:

- the fingerprint set: every corpus sentence at H (corpus `papers/*.md`, `book/*.md`, R6.A1CFG.2) that contains the
  literal, on which a hit of one of the rule's profiles lies inside an occurrence of the literal (the trigger,
  R6.RULE.2);
- `scope.files` (the files of those sentences), `max_instances` (their number), each `sentence_sha256` and
  `context_sha256` (R6.RULE.5, computed here, not by the tool's helper), and each `negative_allowance` (R6.RULE.7:
  case-insensitive non-overlapping matches, R6.REC.14);
- the self-pass of each fingerprinted sentence through steps 1-6 of R6.RULE.4 (deny profiles from the draft
  `dr-deny.json`, whose four pattern pins are checked here);
- uniqueness and context at `X_rep` (H with the pinned ledger's splices, every `expected_sha256` checked);
- the behaviour of every positive and negative example, with the literal checked as well as the context;
- the W1-a adverse case (#1577 comment 7187883838): the papers/SM.md sentence at H carrying "the six structural
  properties", decided against every rule, in scope and as if every rule's scope held papers/SM.md, and every
  occurrence of "six structural propert" in the corpus at H and `X_rep` accounted for.

The tool is used only for what the design makes it the authority on: splitter version 2 (`util.sentences_of`,
R6.SPLIT) and profile loading from pinned sources (`profiles.load_profile`, R6.PROF). Context hashes, literal
coverage, negative counts, allowance and example behaviour are computed here.

Usage: python3 -I rederive_allow_root.py --repo <git dir> --tool <root holding tools/ledger_coverage>
           --root <path of the draft allow root> --deny <path of the draft dr-deny.json>
Prints one JSON report on stdout; exit status 0 when every check holds, 1 otherwise.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys

H = '53c6601a10419b6b333cc992474272501ab542af'
LEDGER_BLOB = 'ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e'
LEDGER_SHA = '2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5'
# The sentence abbreviations and profile specs of the A1 configuration as last staged. The configuration (checklist
# item 4.8) is not fixed; a change to either invalidates every context hash below.
ABBREV = ['sec.', 'Sec.', 'e.g.', 'i.e.', 'cf.', 'Fig.', 'Eq.', 'Eqs.', 'No.', 'vs.', 'et al.', 'Ch.', 'App.',
          'Thm.', 'Prop.', 'Lem.']
P_CHECKER = ('4c79be642ca631573f06b444903be75ec4f5e2b6',
             'verification/audits/foundations/a1exit-deletion-20261121/edits_check.py',
             '2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c')
PROFILES = {
    'count-grep': ({'kind': 'literal-list', 'selector': ['Fourteen', 'six structural', 'sixth of']}, None,
                   'd8a72dbd7ffecc708ee24d2dcb0e3ceb457b4031ff7ec00b45516063f4f84a8a'),
    'ptr': ({'kind': 'python-ast-assign', 'selector': 'PTR'}, P_CHECKER,
            '00a25f44c1adad9c9cc8de5097871336b15f56534e3d30394beedd2ad6a1ec5d'),
    'repo': ({'kind': 'python-ast-assign', 'selector': 'REPO_PAT'}, P_CHECKER,
             '1664bdf1e5e12cb8d7b95e78e99a7d89f1cbab0d05d603ed4604a43bb5a6a80b'),
    'p0-core': ({'kind': 'json-pointer', 'selector': '/core_patterns'},
                (H, 'verification/audits/foundations/a1-scope-phase0-20261120/sites.json',
                 '00165404a6411a219a875ea1d9d6187e1d0d8f9951637fbb31ca0280212b4a5f'),
                '939cafdad4dbcb47762af98a82a357bf2f1ff0da17408177d806eaff18204d93'),
    'p0-para': ({'kind': 'json-pointer', 'selector': '/paraphrase_patterns'},
                (H, 'verification/audits/foundations/a1-scope-phase0-20261120/sites.json',
                 '00165404a6411a219a875ea1d9d6187e1d0d8f9951637fbb31ca0280212b4a5f'),
                '28b482757bee068e79eaac85619b4fd0a0e6f23e4d72cdd2b8252fb22167bd42'),
    'ledger-ext': ({'kind': 'python-ast-assign', 'selector': 'EXTENDED_PATTERNS'},
                   (H, 'verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py',
                    '34314041cff64f01287bd195d33c61cd17882166e11bd1296b005e72d4ad78e8'),
                   '63f19fbfea68e9468aadcb5fa52685f1c4f15f38f4b376dc9d48de5c0ef25a2e'),
}
DENY_PINS = {'DR-1': ('/rules/0/patterns', ['line', 'sentence'], 'any',
                      '6e8e5cda3b386761043c23830ed629ebb9366b8548d5a997c4ac7fa6d0133368'),
             'DR-3': ('/rules/1/patterns', ['sentence'], 'all',
                      'ca9942f4dbf13728d3c9055b32e296378a18ee81982f56f1284ceef546cc6eed'),
             'DR-4': ('/rules/2/patterns', ['line', 'sentence'], 'any',
                      'f8db18e04bb603aed81386af55c37699c22bdaa036a3e68e223e92e315f4e72a'),
             'DR-5': ('/rules/3/patterns', ['line', 'sentence'], 'any',
                      '0d1e2360877eb31e392594f9fd38e70d9c075137d498e35a3a0ab2482f70482a')}
W1A_FILE = 'papers/SM.md'
GENERIC = 'six structural propert'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    if r.returncode != 0:
        raise SystemExit('git %s failed' % ' '.join(a))
    return r.stdout


def ctx_sha(ss, k):
    """R6.RULE.5: sha256(prev || 0x00 || next), BOF / EOF at the ends, sentences as the splitter yields them."""
    prev = ss[k - 1][0] if k > 0 else 'BOF'
    nxt = ss[k + 1][0] if k + 1 < len(ss) else 'EOF'
    return sha(prev.encode('utf-8') + b'\x00' + nxt.encode('utf-8'))


def neg_counts(negs, s):
    """R6.RULE.4 step 3 and R6.RULE.7: non-overlapping, case-insensitive matches of each negative literal."""
    out = {}
    for n in negs:
        if isinstance(n, dict):
            out[n['regex']] = len(re.findall(n['regex'], s))
        else:
            out[n] = len(re.findall(re.escape(n.lower()), s.lower()))
    return out


def covers(literal, s, span):
    i = s.find(literal)
    while i >= 0:
        if i <= span[0] and span[1] <= i + len(literal):
            return True
        i = s.find(literal, i + 1)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--tool', required=True)
    ap.add_argument('--root', required=True)
    ap.add_argument('--deny', required=True)
    a = ap.parse_args()
    sys.path.insert(0, a.tool + '/tools')
    from ledger_coverage.engine import util, profiles as pr

    def show(commit, path):
        return git(a.repo, 'show', '%s:%s' % (commit, path))

    rep = {'H': H, 'rules': {}, 'checks': {}}
    chk = rep['checks']
    root = json.load(open(a.root, encoding='utf-8'))
    deny_bytes = open(a.deny, 'rb').read()

    led_b = git(a.repo, 'cat-file', 'blob', LEDGER_BLOB)
    chk['ledger_pin'] = sha(led_b) == LEDGER_SHA
    led = json.loads(led_b)
    chk['ledger_base_is_H'] = led['base'] == H

    def xrep(path):
        b = show(H, path)
        for s in sorted([s for s in led['splices'] if s['file'] == path], key=lambda s: s['start'], reverse=True):
            assert sha(b[s['start']:s['end']]) == s['old_sha256'] and sha(s['new'].encode()) == s['new_sha256']
            b = b[:s['start']] + s['new'].encode() + b[s['end']:]
        if path in led['files']:
            assert sha(b) == led['files'][path]['expected_sha256'], path
        return b

    def sents(b):
        return util.sentences_of(util.lines_of(b.decode('utf-8')), ABBREV, 2)

    # profiles from their pinned sources
    def read_source(src):
        b = show(src['commit'], src['path'])
        if sha(b) != src['blob_sha256']:
            raise SystemExit('profile source %s differs from its pin' % src['path'])
        return b
    profs = {}
    for name, (ext, src, pin) in PROFILES.items():
        spec = {'name': name, 'kind': 'review', 'applies_to': 'tree', 'scope': 'corpus',
                'source': {'commit': src[0] if src else None, 'path': src[1] if src else None, 'extractor': ext},
                'pattern_sha256': pin}
        if src:
            spec['source']['blob_sha256'] = src[2]
        p, h = pr.load_profile(spec, read_source)
        chk['profile_pin:' + name] = h == pin
        profs[name] = p
    deny = []
    for rid, (ptr, levels, comb, pin) in DENY_PINS.items():
        val = pr.extract('json-pointer', ptr, deny_bytes)
        chk['deny_pattern_pin:' + rid] = pr.pattern_hash(val) == pin
        deny.append(pr.Profile({'name': rid, 'kind': 'deny', 'applies_to': 'tree', 'scope': 'corpus',
                                'levels': levels, 'combine': comb,
                                'source': {'commit': None, 'path': None,
                                           'extractor': {'kind': 'json-pointer', 'selector': ptr}}}, val))

    def deny_hit(s):
        return any(d.matches(s) for d in deny)

    corpus = sorted(p for p in git(a.repo, 'ls-tree', '-r', '--name-only', H, 'papers', 'book').decode().split('\n')
                    if p.endswith('.md') and p.count('/') == 1)
    chk['corpus_files_at_H'] = len(corpus)
    S_H = {f: sents(show(H, f)) for f in corpus}

    allok = True
    for r in root['rules']:
        rid, m = r['id'], r['matcher']
        lit, ctxl, negs = m['literal'], m.get('context', []), m.get('negative', [])
        out = {'literal_length': len(lit), 'literal_at_least_8': len(lit) >= 8}
        # derive the fingerprint set from H
        derived = []
        uncovered = []
        for f in corpus:
            ss = S_H[f]
            for k, (s, ln, _) in enumerate(ss):
                if lit not in s:
                    continue
                spans = [(p, x, y) for p in r['profiles'] for _, x, y in profs[p].matches(s)]
                cov = [(p, s[x:y]) for p, x, y in spans if covers(lit, s, (x, y))]
                if not cov:
                    uncovered.append({'file': f, 'line': ln})
                    continue
                nb = [ss[j][0] for j in (k - 1, k + 1) if 0 <= j < len(ss)]
                pool = s + '\n' + '\n'.join(nb)
                cnt = neg_counts(negs, s)
                derived.append({'file': f, 'line_at_H': ln, 'sentence': s, 'sentence_sha256': sha(s.encode()),
                                'context_sha256': ctx_sha(ss, k), 'triggers': sorted(set(cov)),
                                'all_rule_profile_spans_covered': len(cov) == len(spans),
                                'context_literals_hold': all(c in pool for c in ctxl),
                                'negative_counts': {kk: v for kk, v in cnt.items() if v},
                                'deny_match': deny_hit(s),
                                'same_sentence_in_file_at_H': sum(1 for t in ss if t[0] == s)})
        out['derived_fingerprints'] = derived
        out['literal_without_covered_trigger'] = uncovered
        der_scope = sorted({d['file'] for d in derived})
        out['derived_scope'] = der_scope
        out['scope_equal'] = sorted(r['scope']['files']) == der_scope
        out['max_instances_equal'] = r['max_instances'] == len(derived) == len(r['fingerprints'])
        draft_fp = sorted((fp['file'], fp['sentence_sha256'], fp['context_sha256'],
                           json.dumps(fp.get('negative_allowance'), sort_keys=True)) for fp in r['fingerprints'])
        der_fp = sorted((d['file'], d['sentence_sha256'], d['context_sha256'],
                         json.dumps(d['negative_counts'] or None, sort_keys=True)) for d in derived)
        out['fingerprints_equal'] = draft_fp == der_fp
        out['allowances_name_only_negative_literals'] = all(
            set((fp.get('negative_allowance') or {})) <= set(n if isinstance(n, str) else n['regex'] for n in negs)
            for fp in r['fingerprints'])
        # self-pass through R6.RULE.4 steps 1-6 at H, with each fingerprint's own allowance
        selfpass = []
        for d in derived:
            al = d['negative_counts']  # equals the fingerprint's allowance when fingerprints_equal holds
            ok = d['all_rule_profile_spans_covered'] and d['context_literals_hold'] and not d['deny_match'] and \
                all(v <= al.get(kk, 0) for kk, v in neg_counts(negs, d['sentence']).items()) and \
                d['same_sentence_in_file_at_H'] == 1
            selfpass.append(ok)
        out['self_pass_at_H'] = selfpass
        out['fingerprinted_sentences_are_positive_examples'] = all(d['sentence'] in r['positive_examples']
                                                                   for d in derived)
        # X_rep: uniqueness and context
        xr = []
        for d in derived:
            ss = sents(xrep(d['file']))
            ks = [k for k, t in enumerate(ss) if sha(t[0].encode()) == d['sentence_sha256']]
            xr.append({'file': d['file'], 'unique': len(ks) == 1,
                       'line_at_X_rep': ss[ks[0]][1] if len(ks) == 1 else None,
                       'context_equal_to_H': len(ks) == 1 and ctx_sha(ss, ks[0]) == d['context_sha256']})
        out['x_rep'] = xr
        # examples: a positive example holds the literal and the context literals within itself and has no
        # negative match beyond the allowance of the fingerprint whose sentence it is (zero otherwise); a negative
        # example fails one of these, or matches a deny profile
        fp_allow = {d['sentence']: d['negative_counts'] for d in derived}

        def accepted(ex):
            al = fp_allow.get(ex, {})
            reasons = []
            if lit not in ex:
                reasons.append('literal absent')
            if not all(c in ex for c in ctxl):
                reasons.append('context literal absent')
            over = {kk: v for kk, v in neg_counts(negs, ex).items() if v > al.get(kk, 0)}
            if over:
                reasons.append('negative beyond allowance %s' % json.dumps(over, sort_keys=True))
            if deny_hit(ex):
                reasons.append('deny match')
            return not reasons, reasons
        out['positive_examples'] = [{'accepted': accepted(ex)[0], 'why_not': accepted(ex)[1]}
                                    for ex in r['positive_examples']]
        out['negative_examples'] = [{'rejected': not accepted(ex)[0], 'by': accepted(ex)[1]}
                                    for ex in r['negative_examples']]
        ok = (out['literal_at_least_8'] and out['scope_equal'] and out['max_instances_equal'] and
              out['fingerprints_equal'] and out['allowances_name_only_negative_literals'] and all(selfpass) and
              out['fingerprinted_sentences_are_positive_examples'] and all(x['unique'] for x in xr) and
              all(e['accepted'] for e in out['positive_examples']) and
              all(e['rejected'] for e in out['negative_examples']) and len(derived) > 0 and not uncovered)
        out['holds'] = ok
        allok = allok and ok
        rep['rules'][rid] = out

    # W1-a adverse case
    sm = S_H[W1A_FILE]
    w1a = [(k, s, ln) for k, (s, ln, _) in enumerate(sm) if 'satisfying the six structural properties.' in s]
    chk['w1a_sentence_unique_at_H'] = len(w1a) == 1
    k, s, ln = w1a[0]
    hits = [(p, x, y) for p in profs for _, x, y in profs[p].matches(s)]
    nb = [sm[j][0] for j in (k - 1, k + 1) if 0 <= j < len(sm)]
    per_rule = {}
    for r in root['rules']:
        m = r['matcher']
        per_rule[r['id']] = {
            'in_scope': W1A_FILE in r['scope']['files'],
            'literal_in_sentence': m['literal'] in s,
            'literal_covers_some_hit': any(covers(m['literal'], s, (x, y)) for _, x, y in hits),
            'is_a_negative_example': s in r['negative_examples']}
    rep['w1a'] = {'file': W1A_FILE, 'line_at_H': ln, 'sentence': s, 'sentence_sha256': sha(s.encode()),
                  'hits': sorted({(p, s[x:y]) for p, x, y in hits}), 'per_rule': per_rule,
                  'deny_match': deny_hit(s)}
    chk['w1a_classified_by_no_rule_even_out_of_scope'] = not any(
        v['literal_covers_some_hit'] for v in per_rule.values())
    chk['w1a_negative_example_of_every_rule'] = all(v['is_a_negative_example'] for v in per_rule.values())
    # every occurrence of the generic phrase in the corpus at H and X_rep, and which rule (if any) could hold it
    occ = {}
    for tag in ('H', 'X_rep'):
        rows = []
        for f in corpus:
            ss = S_H[f] if tag == 'H' else sents(xrep(f))
            for kk, (t, l2, _) in enumerate(ss):
                if GENERIC in t:
                    holders = [r['id'] for r in root['rules'] if r['matcher']['literal'] in t
                               and f in r['scope']['files']]
                    rows.append({'file': f, 'line': l2, 'sentence_sha256': sha(t.encode()), 'held_by': holders})
        occ[tag] = rows
    rep['generic_phrase_occurrences'] = occ
    chk['generic_phrase_only_held_by_fingerprinted_sentences'] = all(
        (not row['held_by']) or any(row['sentence_sha256'] == d['sentence_sha256'] and row['file'] == d['file']
                                    for rr in rep['rules'].values() for d in rr['derived_fingerprints'])
        for row in occ['H'])
    chk['rule_ids'] = [r['id'] for r in root['rules']]
    chk['rule_ids_exactly_the_five'] = chk['rule_ids'] == ['W1-b', 'W1-c', 'W1-d', 'W2-a', 'W2-b']
    chk['no_rule_id_W1-a'] = 'W1-a' not in chk['rule_ids']
    bools = [v for v in chk.values() if isinstance(v, bool)]
    rep['holds'] = allok and all(bools)
    sys.stdout.write(json.dumps(rep, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
    sys.exit(0 if rep['holds'] else 1)


if __name__ == '__main__':
    main()
