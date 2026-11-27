"""WIP / UNVERIFIED staging draft, not frozen, not reviewed, not adopted.

Writer's derivation of the draft A1 rule records (checklist items 4.3 and 4.4 of #1169 comment 7207860923):

- the designated first allow root `a1-staging-allow-root.json` (A1 staging amendment r2, sec. 2 "Allow-rule
  record" and "Initial widening review"), carrying W1-b, W1-c, W1-d, W2-a and W2-b re-derived at H under
  R6.REC.14, and never W1-a;
- the deny rules DR-1 (alternatives a, b, c), DR-3, DR-4 and DR-5 and the review-profile rule `resid` (resid-a,
  resid-b, resid-c), as OBL-3 and R6.DENY.5 of design r6 (r13) list them.

Eligible bytes. Every byte the drafts are derived from is read through `git cat-file` by full object id from
objects that R6.EVID.8 pins or that are reachable from `main`: H (53c6601a, on main), the retirement ledger
(git blob ba37c1cd, sha256 2055e68f) and edit list (git blob ec384fdf, sha256 528f146d), P's checker
(sha256 2856e58c, also on main as the design's inputs/edits_check.py), the Phase-0 and ledger profile sources at H,
and the superseded drafts on the tool branch (custody inputs only; their content is re-checked, not inherited).
`T1'` (14ac71b4) is never read. `X_rep`'s ledgered files are built here from H and the pinned ledger alone and
checked against each file's `expected_sha256`.

The script writes the drafts and prints a JSON report of every check. It imports the tool's own `util`,
`profiles` and `rules` modules (it does not change them); the independent reviewers re-derive without it
(R6.REC.2).

Usage: python3 -I derive_rule_drafts.py --repo <git dir> --tool <tool tree root> --out <plan record dir>
       [--check]   (with --check nothing is written; the drafts on disk are compared with the derivation)
"""
import argparse
import hashlib
import json
import subprocess
import sys

H = '53c6601a10419b6b333cc992474272501ab542af'
LEDGER_BLOB, LEDGER_SHA = 'ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e', \
    '2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5'
EDITS_BLOB, EDITS_SHA = 'ec384fdfbc12937b860e2f226355e8c5d94820a5', \
    '528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1'
TOOL_RULES = 'verification/audits/foundations/ledger-coverage-tool-20261123/rules/'
# custody inputs (staging r2 sec. 2): the exact superseded drafts the re-derivation starts from
ALLOW_V3 = (TOOL_RULES + 'w1-w2-allow-v3.json', '5485154a9c703192d4de65619ad5948d14fec7dbbffa2440b6482019efea15db')
DENY_V1 = (TOOL_RULES + 'dr-deny-v1.json', 'daf3a8e231ace391f0037447d1266d1255df8dc015baaaa601fcc79b63cec6ae')
RESID_V1 = (TOOL_RULES + 'resid-v1.json', '7aa1412206f7bf5fec1d3573d76e1b91c0f6bc8f67704a1dcb75344d09aac221')
TOOL_COMMIT = '7db52f380f1e51d4af52b84f0a7e728827ac5a60'  # the tool branch head the drafts were cut from (custody inputs are read there)
D_REC = 'verification/audits/foundations/a1exit-deletion-20261121/'
# The writer identity is an open point (README, stop S-1): staging r2 sec. 2 requires the independently verified
# GitHub identity of the actual author; this placeholder is not one.
AUTHOR = 'a1-staging-writer-20261127'
STATUS = ('WIP / UNVERIFIED staging draft, not frozen, not reviewed, not adopted (checklist #1169 comment '
          '7207860923). No review record, owner adoption or freeze exists for it, and the tool admits no record '
          'without them.')
# the sentence abbreviations of the A1 configuration as last staged (configuration item 4.8 is not yet fixed)
ABBREV = ['sec.', 'Sec.', 'e.g.', 'i.e.', 'cf.', 'Fig.', 'Eq.', 'Eqs.', 'No.', 'vs.', 'et al.', 'Ch.', 'App.',
          'Thm.', 'Prop.', 'Lem.']
# the W1-a adverse case (staging r2 sec. 2; #1577 comment 7187883838): papers/SM.md, the sentence carrying
# "the six structural properties", read at H
W1A_FILE = 'papers/SM.md'
W1A_TRIGGER = 'satisfying the six structural properties.'
PROFILE_SPECS = {
    'count-grep': {'name': 'count-grep', 'kind': 'review', 'applies_to': 'tree', 'scope': 'corpus',
                   'source': {'commit': None, 'path': None,
                              'extractor': {'kind': 'literal-list',
                                            'selector': ['Fourteen', 'six structural', 'sixth of']}},
                   'pattern_sha256': 'd8a72dbd7ffecc708ee24d2dcb0e3ceb457b4031ff7ec00b45516063f4f84a8a'},
    'ptr': {'name': 'ptr', 'kind': 'review', 'applies_to': 'tree', 'scope': 'corpus',
            'source': {'commit': '4c79be642ca631573f06b444903be75ec4f5e2b6',
                       'path': 'verification/audits/foundations/a1exit-deletion-20261121/edits_check.py',
                       'extractor': {'kind': 'python-ast-assign', 'selector': 'PTR'},
                       'blob_sha256': '2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c'},
            'pattern_sha256': '00a25f44c1adad9c9cc8de5097871336b15f56534e3d30394beedd2ad6a1ec5d'},
    'repo': {'name': 'repo', 'kind': 'review', 'applies_to': 'tree', 'scope': 'repo',
             'source': {'commit': '4c79be642ca631573f06b444903be75ec4f5e2b6',
                        'path': 'verification/audits/foundations/a1exit-deletion-20261121/edits_check.py',
                        'extractor': {'kind': 'python-ast-assign', 'selector': 'REPO_PAT'},
                        'blob_sha256': '2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c'},
             'pattern_sha256': '1664bdf1e5e12cb8d7b95e78e99a7d89f1cbab0d05d603ed4604a43bb5a6a80b'},
    'p0-core': {'name': 'p0-core', 'kind': 'review', 'applies_to': 'tree', 'scope': 'corpus',
                'source': {'commit': H, 'path': 'verification/audits/foundations/a1-scope-phase0-20261120/sites.json',
                           'extractor': {'kind': 'json-pointer', 'selector': '/core_patterns'},
                           'blob_sha256': '00165404a6411a219a875ea1d9d6187e1d0d8f9951637fbb31ca0280212b4a5f'},
                'pattern_sha256': '939cafdad4dbcb47762af98a82a357bf2f1ff0da17408177d806eaff18204d93'},
    'p0-para': {'name': 'p0-para', 'kind': 'review', 'applies_to': 'tree', 'scope': 'corpus',
                'source': {'commit': H, 'path': 'verification/audits/foundations/a1-scope-phase0-20261120/sites.json',
                           'extractor': {'kind': 'json-pointer', 'selector': '/paraphrase_patterns'},
                           'blob_sha256': '00165404a6411a219a875ea1d9d6187e1d0d8f9951637fbb31ca0280212b4a5f'},
                'pattern_sha256': '28b482757bee068e79eaac85619b4fd0a0e6f23e4d72cdd2b8252fb22167bd42'},
    'ledger-ext': {'name': 'ledger-ext', 'kind': 'review', 'applies_to': 'tree', 'scope': 'corpus',
                   'source': {'commit': H,
                              'path': 'verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py',
                              'extractor': {'kind': 'python-ast-assign', 'selector': 'EXTENDED_PATTERNS'},
                              'blob_sha256': '34314041cff64f01287bd195d33c61cd17882166e11bd1296b005e72d4ad78e8'},
                   'pattern_sha256': '63f19fbfea68e9468aadcb5fa52685f1c4f15f38f4b376dc9d48de5c0ef25a2e'},
}
DENY_PINS = {'DR-1': ('/rules/0/patterns', ['line', 'sentence'], 'any',
                      '6e8e5cda3b386761043c23830ed629ebb9366b8548d5a997c4ac7fa6d0133368'),
             'DR-3': ('/rules/1/patterns', ['sentence'], 'all',
                      'ca9942f4dbf13728d3c9055b32e296378a18ee81982f56f1284ceef546cc6eed'),
             'DR-4': ('/rules/2/patterns', ['line', 'sentence'], 'any',
                      'f8db18e04bb603aed81386af55c37699c22bdaa036a3e68e223e92e315f4e72a'),
             'DR-5': ('/rules/3/patterns', ['line', 'sentence'], 'any',
                      '0d1e2360877eb31e392594f9fd38e70d9c075137d498e35a3a0ab2482f70482a')}
RESID_PIN = '39a91e1a3d6a628adc889f83a034aa6399942d984c8dc8b3e963fdb0ff9a18d4'
AGENTS_AT_H = {'id': 'agents-md-at-H', 'commit': H, 'path': 'AGENTS.md',
               'sha256': 'd87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


class Git:
    def __init__(self, repo):
        self.repo = repo

    def _run(self, *a):
        r = subprocess.run(['git', '-C', self.repo] + list(a), capture_output=True)
        return r.stdout if r.returncode == 0 else None

    def blob(self, oid, want_sha=None):
        b = self._run('cat-file', 'blob', oid)
        if b is None or (want_sha and sha(b) != want_sha):
            raise SystemExit('blob %s missing or wrong sha256' % oid)
        return b

    def show(self, commit, path):
        return self._run('show', '%s:%s' % (commit, path))

    def full(self, rev):
        out = self._run('rev-parse', '--verify', rev + '^{commit}')
        return out.decode().strip() if out else None


def dumps(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--tool', required=True, help='root holding tools/ledger_coverage (imported, never changed)')
    ap.add_argument('--out', required=True, help='the plan record directory D_rec in a working tree')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    sys.path.insert(0, a.tool + '/tools')
    from ledger_coverage.engine import util, profiles as pr, rules as rm

    g = Git(a.repo)
    report = {'H': H, 'checks': {}}
    chk = report['checks']
    # ---- inputs ---------------------------------------------------------------------------------------------
    led = json.loads(g.blob(LEDGER_BLOB, LEDGER_SHA))
    g.blob(EDITS_BLOB, EDITS_SHA)
    chk['ledger_base_is_H'] = led['base'] == H

    def custody(ref):
        b = g.show(TOOL_COMMIT, ref[0])
        if b is None or sha(b) != ref[1]:
            raise SystemExit('custody input %s differs from its pin' % ref[0])
        return json.loads(b)
    v3, dv1, rv1 = custody(ALLOW_V3), custody(DENY_V1), custody(RESID_V1)

    def xrep(path):
        """X_rep's bytes of a ledgered path (R6.EVID.8): H's bytes with the ledger's splices applied."""
        b = g.show(H, path)
        for s in sorted([s for s in led['splices'] if s['file'] == path], key=lambda s: s['start'], reverse=True):
            if sha(b[s['start']:s['end']]) != s['old_sha256'] or sha(s['new'].encode()) != s['new_sha256']:
                raise SystemExit('splice %s does not apply at H' % s['id'])
            b = b[:s['start']] + s['new'].encode() + b[s['end']:]
        if path in led['files'] and sha(b) != led['files'][path]['expected_sha256']:
            raise SystemExit('X_rep %s does not hash to expected_sha256' % path)
        return b

    def sents(data):
        return util.sentences_of(util.lines_of(data.decode('utf-8')), ABBREV, 2)

    # ---- profiles (read from pinned sources; pattern hashes compared with the staged pins) --------------------
    def read_source(src):
        b = g.show(src['commit'], src['path'])
        if b is None or sha(b) != src['blob_sha256']:
            raise SystemExit('profile source %s differs from its pin' % src['path'])
        return b
    profs = {}
    for name, spec in PROFILE_SPECS.items():
        p, h = pr.load_profile(spec, read_source)
        chk['profile_pin:' + name] = h == spec['pattern_sha256']
        profs[name] = p

    # ---- deny and resid drafts (patterns byte-equal to the v1 drafts; reasons cite r6) -------------------------
    deny_rules = []
    reasons = {
        'DR-1': 'A count or ordinal of the structural posits, or the A1-A6 label range (R6.DENY.5, OBL-3). The '
                'ordinal alternatives a and b encode the corpus terminology decision the plan amendment states '
                '(OBL-4); alternative c is the label range.',
        'DR-3': 'A sentence with a posit noun and a tail naming finiteness among them (R6.DENY.5, OBL-3). Its real '
                'witness lies outside the corpus and is read by a control-only scan (R6.A1CFG.2, controls).',
        'DR-4': 'The retired posit entry, a label A1 followed within the sentence or the next by finiteness, the '
                'configuration space or the substratum (R6.DENY.5, OBL-3).',
        'DR-5': 'The posit-ledger count fourteen (R6.DENY.5, OBL-3).',
    }
    for r in dv1['rules']:
        deny_rules.append(dict(r, reason=reasons[r['id']], author=AUTHOR))
    deny_doc = {'schema': 'oi-term-rules/2', 'record_id': 'a1-plan-deny-dr', 'status': STATUS, 'supersedes': None,
                'recorded_at': H, 'author': AUTHOR, 'rules': deny_rules}
    resid_rule = dict(rv1['rules'][0], author=AUTHOR,
                      reason='Residual review profile on added text (R6.DENY.4, R6.DENY.5, OBL-3): REVIEW_REQUIRED '
                             'for lexically unanchored paraphrases of the retired posit, never a PASS. Its negative '
                             'examples are the accepted residuals V4 and V27 and the six-posit form (R6.DENY.6, owner '
                             'decision 3 of 2026-11-25), which it does not catch.')
    resid_doc = {'schema': 'oi-term-rules/2', 'record_id': 'a1-plan-resid', 'status': STATUS, 'supersedes': None,
                 'recorded_at': H, 'author': AUTHOR, 'rules': [resid_rule]}
    deny_bytes, resid_bytes = dumps(deny_doc), dumps(resid_doc)
    chk['deny_patterns_equal_v1'] = [r['patterns'] for r in deny_rules] == [r['patterns'] for r in dv1['rules']]
    chk['resid_patterns_equal_v1'] = resid_rule['patterns'] == rv1['rules'][0]['patterns']
    deny_profiles = []
    for rid, (ptr, levels, comb, pin) in DENY_PINS.items():
        val = pr.extract('json-pointer', ptr, deny_bytes)
        chk['deny_pattern_pin:' + rid] = pr.pattern_hash(val) == pin
        spec = {'name': rid, 'kind': 'deny', 'applies_to': 'tree', 'scope': 'corpus', 'levels': levels,
                'combine': comb, 'source': {'commit': None, 'path': D_REC + 'dr-deny.json',
                                            'extractor': {'kind': 'json-pointer', 'selector': ptr}}}
        deny_profiles.append(pr.Profile(spec, val))
    chk['resid_pattern_pin'] = pr.pattern_hash(pr.extract('json-pointer', '/rules/0/patterns', resid_bytes)) == RESID_PIN

    agents_h = g.show(H, 'AGENTS.md')
    chk['agents_md_at_H_pin'] = agents_h is not None and sha(agents_h) == AGENTS_AT_H['sha256']

    def control_input(cc):
        if 'control_input' in cc:
            if cc['control_input'] != AGENTS_AT_H['id']:
                return None
            lines = util.lines_of(agents_h.decode())
        else:
            data = g.show(cc['commit'], cc['path'])
            if data is None:
                return None
            lines = util.lines_of(data.decode())
        if 'sentence_line' in cc:
            for s, x, _ in util.sentences_of(lines, ABBREV, 2):
                if x == cc['sentence_line']:
                    return s
            return None
        return lines[cc['line'] - 1] if 0 < cc['line'] <= len(lines) else None

    full_h = g.full(H)

    def sentence_lookup(commit, path, ssha):
        if commit != full_h:
            return None  # only H is an eligible recorded_at here
        data = g.show(commit, path)
        if data is None:
            return None
        ss = sents(data)
        for k, (s, _, _) in enumerate(ss):
            if util.sha256(s) == ssha:
                return s, [ss[j][0] for j in (k - 1, k + 1) if 0 <= j < len(ss)], rm.sentence_context_sha(ss, k)
        return None

    for r in deny_rules + [resid_rule]:
        chk['lint:' + r['id']] = rm.lint_rule(r, profs.get, sentence_lookup, deny_profiles, control_input)

    # ---- the W1-a adverse case at H ---------------------------------------------------------------------------
    sm = sents(g.show(H, W1A_FILE))
    w1a = [s for s, _, _ in sm if W1A_TRIGGER in s]
    chk['w1a_sentence_unique_at_H'] = len(w1a) == 1
    w1a_sentence = w1a[0]

    # ---- the allow root ---------------------------------------------------------------------------------------
    keep = ['W1-b', 'W1-c', 'W1-d', 'W2-a', 'W2-b']
    v3_ids = [r['id'] for r in v3['rules']]
    chk['custody_v3_ids'] = v3_ids
    rules_out = []
    fp_report = {}
    for r in v3['rules']:
        if r['id'] not in keep:
            raise SystemExit('unexpected rule %s in v3' % r['id'])
        fps = []
        for fp in r['fingerprints']:
            ss_h = sents(g.show(H, fp['file']))
            ss_x = sents(xrep(fp['file']))
            hk = [k for k, (s, _, _) in enumerate(ss_h) if util.sha256(s) == fp['sentence_sha256']]
            xk = [k for k, (s, _, _) in enumerate(ss_x) if util.sha256(s) == fp['sentence_sha256']]
            if len(hk) != 1 or len(xk) != 1:
                raise SystemExit('%s: the fingerprinted sentence is not unique at H and X_rep' % r['id'])
            ctx_h = rm.sentence_context_sha(ss_h, hk[0])
            ctx_x = rm.sentence_context_sha(ss_x, xk[0])
            new = {'file': fp['file'], 'sentence_sha256': fp['sentence_sha256'], 'context_sha256': ctx_h}
            if fp.get('negative_allowance'):
                negs = rm.neg_counts(r['matcher']['negative'], ss_h[hk[0]][0])
                new['negative_allowance'] = {k: negs[k] for k in fp['negative_allowance']}
            fps.append(new)
            fp_report['%s %s' % (r['id'], fp['file'])] = {
                'line_at_H': ss_h[hk[0]][1], 'line_at_X_rep': ss_x[xk[0]][1],
                'context_at_H_equals_X_rep': ctx_h == ctx_x,
                'context_equals_superseded_draft': ctx_h == fp['context_sha256']}
        negex = list(r['negative_examples'])
        if w1a_sentence not in negex:
            negex.append(w1a_sentence)
        rules_out.append({'id': r['id'], 'kind': 'allow', 'profiles': r['profiles'], 'scope': r['scope'],
                          'matcher': r['matcher'], 'context_required': r['context_required'],
                          'max_instances': len(fps), 'fingerprints': fps, 'recorded_at': full_h,
                          'positive_examples': r['positive_examples'], 'negative_examples': negex,
                          'reason': r['reason'], 'author': AUTHOR})
    root = {'schema': 'oi-term-rules/2', 'record_id': 'a1-staging-w1-w2',
            'status': STATUS + ' Designated first record of the allow lineage (A1 staging amendment r2, sec. 2): '
                      'W1-b, W1-c, W1-d, W2-a and W2-b only. W1-a is excluded and is never admitted under any id; '
                      'its sentence (papers/SM.md at H) is a negative example of every rule here.',
            'supersedes': None, 'recorded_at': full_h, 'author': AUTHOR, 'rules': rules_out}
    root_bytes = dumps(root)
    report['fingerprints'] = fp_report
    for r in rules_out:
        chk['lint:' + r['id']] = rm.lint_rule(r, profs.get, sentence_lookup, deny_profiles, control_input)
    # meaning preserved: every field other than recorded_at, fingerprints' contexts, author and the added W1-a
    # negative example equals the superseded draft
    v3_by = {r['id']: r for r in v3['rules']}
    same = {}
    for r in rules_out:
        o = v3_by[r['id']]
        same[r['id']] = all(r[k] == o[k] for k in ('profiles', 'scope', 'matcher', 'context_required',
                                                     'max_instances', 'positive_examples', 'reason')) and \
            r['negative_examples'][:len(o['negative_examples'])] == o['negative_examples'] and \
            [(f['file'], f['sentence_sha256'], f.get('negative_allowance')) for f in r['fingerprints']] == \
            [(f['file'], f['sentence_sha256'], f.get('negative_allowance')) for f in o['fingerprints']]
    chk['meaning_equal_to_superseded_draft'] = same

    # Each hit (one profile match span) is decided on its own (R6.RULE.4, R6.RULE.9).
    def hits(s):
        return [(p.name, x, y) for p in profs.values() for _, x, y in p.matches(s)]

    # W1-a: none of the five rules classifies any hit of the SM sentence at H
    sk = [k for k, (s, _, _) in enumerate(sm) if s == w1a_sentence][0]
    neigh = [sm[j][0] for j in (sk - 1, sk + 1) if 0 <= j < len(sm)]
    w1a_hits = hits(w1a_sentence)
    chk['w1a_hits_at_H'] = sorted({h[0] for h in w1a_hits})
    chk['w1a_at_H_stays_unclassified'] = bool(w1a_hits) and all(
        rm.apply_allow(rules_out, W1A_FILE, w1a_sentence, neigh, rm.sentence_context_sha(sm, sk), [(x, y)], False,
                       {}, None) == ('review', 'unclassified', None) for _, x, y in w1a_hits)
    # and no rule's matcher holds for any of its hits even if SM were in every rule's scope
    chk['w1a_no_matcher_holds_out_of_scope'] = not any(rm.matcher_holds(r, w1a_sentence, neigh, [(x, y)])
                                                       for r in rules_out for _, x, y in w1a_hits)

    # ---- exhaustive classification sweep at H and at X_rep over the rules' scope files -------------------------
    # every hit in a scope file that some rule's matcher covers, with that rule's decision; and, for each sentence
    # so classified, the hits of the same sentence that no rule covers (they stay REVIEW on their own)
    sweep = {}
    for tag, reader in (('H', lambda p: g.show(H, p)), ('X_rep', xrep)):
        got = []
        files = sorted({f for r in rules_out for f in r['scope']['files']})
        for f in files:
            ss = sents(reader(f))
            for k, (s, ln, _) in enumerate(ss):
                hs = hits(s)
                if not hs:
                    continue
                nb = [ss[j][0] for j in (k - 1, k + 1) if 0 <= j < len(ss)]
                deny = any(dp.matches(s) for dp in deny_profiles)
                covered = False
                for pname, x, y in hs:
                    res = rm.apply_allow(rules_out, f, s, nb, rm.sentence_context_sha(ss, k), [(x, y)], deny, {},
                                         None)
                    if res[2] is not None:
                        covered = True
                        got.append([res[2], f, ln, pname, s[x:y], res[0], res[1]])
                if covered:
                    for pname, x, y in hs:
                        res = rm.apply_allow(rules_out, f, s, nb, rm.sentence_context_sha(ss, k), [(x, y)], deny,
                                             {}, None)
                        if res[2] is None:
                            got.append([None, f, ln, pname, s[x:y], res[0], res[1]])
        sweep[tag] = sorted(got, key=lambda z: (z[1], z[2], z[3], z[4], str(z[0])))
    report['sweep'] = sweep

    # ---- write or compare -------------------------------------------------------------------------------------
    outs = {'a1-staging-allow-root.json': root_bytes, 'dr-deny.json': deny_bytes, 'resid.json': resid_bytes}
    report['outputs'] = {k: sha(v) for k, v in sorted(outs.items())}
    for name, b in outs.items():
        path = a.out.rstrip('/') + '/' + name
        if a.check:
            with open(path, 'rb') as fh:
                chk['on_disk_equal:' + name] = fh.read() == b
        else:
            with open(path, 'wb') as fh:
                fh.write(b)
    sys.stdout.write(json.dumps(report, indent=1, sort_keys=True, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
