"""Synthetic second configuration (sec. 16.5), held as in-memory fixture data, never committed as a record.

It is structurally different from A1: a line-patch ledger, sites declared in the configuration, no replay, one
review and one deny profile, one HP obligation with one merge, one delegation class (artifact-hash/1), context
field `kind`, and one indicator (LIST). It runs the Y controls, the configuration-defect controls Z1-Z8 and Z10,
the purity controls Z9a-Z9f and the command-line controls X2-X10 and M10 through the same executable.
The identities in its review chain (writer-a, reviewer-b, widener-d, owner-c) are synthetic fixtures.
"""
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if tools not in sys.path:
    sys.path.insert(0, tools)

from ledger_coverage.engine import checker, cli, gitobj, outcome as oc, pipeline as pl, purity, util  # noqa: E402

DOC = 'doc/s.md'
TEXT = ('# synthetic\n\nAxiom Z is the named premise of the synthetic world.\n\nDefinition one states the base object.\n\n'
        'Remark two notes a side fact.\n\nIntro to the list:\n\n- item first here\n- item second here\n\n'
        'Closing words of the file.\n')
WITNESS = 'syn/witness.md'
OWNER, WRITER, REVIEWER, WIDENER = 'owner-c', 'writer-a', 'reviewer-b', 'widener-d'
AD = 'tools/ledger_coverage/adapters/'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def jb(obj):
    return (json.dumps(obj, indent=1, sort_keys=True) + '\n').encode()


def module_bytes(name):
    with open(os.path.join(here, name), 'rb') as f:
        return f.read()


class Syn:
    """Builds the synthetic world. variant: dict of configuration changes for the Z controls."""

    def __init__(self, two_merges=False):
        self.repo = gitobj.Overlay(None)
        base = {DOC: TEXT.encode(), WITNESS: b'Axiom Z holds in the witness text.\n',
                AD + 'line_patch.py': module_bytes('line_patch.py'),
                AD + 'artifact_hash.py': module_bytes('artifact_hash.py')}
        self.pin = self.repo.add_commit(base, [], 'synthetic pin')
        self.m1 = self.repo.derive(self.pin, {'syn/note.txt': b'merge one\n'}, parents=[self.pin],
                                   subject='Merge #7: synthetic merge')
        self.H = self.m1
        if two_merges:
            self.H = self.repo.derive(self.m1, {DOC: TEXT.replace('Remark two notes', 'Remark two records').encode()},
                                      parents=[self.m1], subject='Merge #8: second synthetic merge')

    def lines(self, commit):
        return util.lines_of(self.repo.read(commit, DOC).decode())

    def rule_files(self, allow_scope=None, allow_sup=None):
        pats = {'schema': 'oi-term-rules/2', 'record_id': 'syn-pat', 'supersedes': None, 'author': WRITER,
                'recorded_at': self.pin, 'rules': [
                    {'id': 'syn-review', 'kind': 'review-pattern', 'patterns': {'a': r'\bAxiom Z\b'}, 'combine': 'any',
                     'levels': ['line'], 'scope': 'all-corpus', 'positive_examples': ['Axiom Z appears.'],
                     'negative_examples': ['Axiom Y appears.'], 'reason': 'synthetic', 'author': WRITER},
                    {'id': 'syn-deny', 'kind': 'deny', 'patterns': {'a': r'\bAxiom Z\b[^.]{0,40}\b(holds|assumed)\b'},
                     'combine': 'any', 'levels': ['line', 'sentence'], 'scope': 'all-corpus',
                     'positive_examples': ['Axiom Z is assumed.'], 'negative_examples': ['Axiom Z is named.'],
                     'countercontrol': [{'control_input': 'witness', 'line': 1}], 'reason': 'synthetic',
                     'author': WRITER},
                    {'id': 'syn-beta', 'kind': 'review-pattern', 'patterns': {'a': r'\bbeta\b'}, 'combine': 'any',
                     'levels': ['line'], 'scope': 'all-corpus', 'positive_examples': ['a beta word'],
                     'negative_examples': ['an alpha word'], 'reason': 'synthetic', 'author': WRITER}]}
        sent = 'Axiom Z is the named premise of the synthetic world.'
        sents = util.sentences_of(self.lines(self.pin), ['e.g.'], 2)
        k = [i for i, s in enumerate(sents) if s[0] == sent][0]
        from ledger_coverage.engine import rules as rulemod
        allow = {'schema': 'oi-term-rules/2', 'record_id': 'syn-allow', 'supersedes': allow_sup, 'author': WRITER,
                 'recorded_at': self.pin, 'rules': [
                     {'id': 'syn-allow-1', 'kind': 'allow', 'profiles': ['axiom-Z'],
                      'scope': {'files': allow_scope or [DOC]},
                      'matcher': {'literal': 'Axiom Z is the named premise', 'context': ['synthetic world'],
                                  'negative': ['holds', 'assumed']},
                      'context_required': False, 'max_instances': 1,
                      'fingerprints': [{'file': DOC, 'sentence_sha256': sha(sent.encode()),
                                        'context_sha256': rulemod.sentence_context_sha(sents, k)}],
                      'recorded_at': self.pin, 'positive_examples': ['Axiom Z is the named premise of the synthetic world.'],
                      'negative_examples': ['Axiom Z is the named premise and holds in the synthetic world.'],
                      'reason': 'synthetic legitimate use', 'author': WRITER}]}
        return pats, allow

    def build(self, variant=None, at=None):
        """Writes the configuration and its records into a commit derived from `at`; returns (commit, path, sha)."""
        v = variant or {}
        at = at or self.H
        files = {}
        pats, allow = self.rule_files(v.get('allow_scope'))
        files['syn/rules-pat.json'] = jb(pats)
        files['syn/rules-allow.json'] = jb(allow)
        recs = []
        for p in ('syn/rules-pat.json', 'syn/rules-allow.json'):
            recs += self.chain(files, p, v.get('reviewer', REVIEWER) if p.endswith('allow.json') else REVIEWER)
        wr0 = {'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': WIDENER,
               'reviewed': {'path': 'syn/rules-allow.json', 'blob_sha256': sha(files['syn/rules-allow.json'])},
               'method': 'read the new allow rule', 'verdicts': [{'item': 'syn-allow-1', 'verdict': 'accept'}]}
        files['syn/rules-allow.widen.json'] = jb(wr0)
        recs.append({'kind': 'review', 'path': 'syn/rules-allow.widen.json',
                     'blob_sha256': sha(files['syn/rules-allow.widen.json'])})
        for rp_, rd_ in sorted(v.get('records_extra', {}).items()):
            files[rp_] = jb(rd_)
            recs.append({'kind': 'record', 'path': rp_, 'blob_sha256': sha(files[rp_])})
            recs += self.chain(files, rp_, REVIEWER)
        if v.get('allow_widened'):
            old_ref = {'path': 'syn/rules-allow.json', 'blob_sha256': sha(files['syn/rules-allow.json'])}
            _, wide = self.rule_files([DOC, 'syn/other.md'], old_ref)
            files['syn/rules-allow-v2.json'] = jb(wide)
            recs += self.chain(files, 'syn/rules-allow-v2.json', REVIEWER)
            if v.get('widening_review'):
                wr = {'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': v.get('widener', WIDENER),
                      'reviewed': {'path': 'syn/rules-allow-v2.json', 'blob_sha256': sha(files['syn/rules-allow-v2.json'])},
                      'method': 'read', 'verdicts': [{'item': 'syn-allow-1', 'verdict': 'accept'}]}
                files['syn/rules-allow-v2.widen.json'] = jb(wr)
                recs.append({'kind': 'review', 'path': 'syn/rules-allow-v2.widen.json',
                             'blob_sha256': sha(files['syn/rules-allow-v2.widen.json'])})
        controls = {'control_inputs': [{'id': 'witness', 'commit': self.pin, 'path': WITNESS,
                                        'sha256': sha(self.repo.read(self.pin, WITNESS))}],
                    'controls': [{'id': 'Y-%s-%s' % (op, d), 'operations': [op], 'direction': d}
                                 for op in ('coverage', 'execution', 'terms') for d in ('positive', 'adversarial')]}
        if v.get('no_controls'):
            controls['controls'] = [c for c in controls['controls'] if c['direction'] == 'positive']
        files['syn/controls.json'] = jb(controls)
        deleg = {'schema': 'oi-delegation/1', 'record_id': 'syn-deleg', 'author': WRITER, 'classes': [
            {'id': 'artifact', 'adapter': 'artifact-hash', 'paths': ['out/digest.txt'], 'params': {'sources': [DOC]},
             'evidence': []}]}
        files['syn/delegation.json'] = jb(deleg)
        rules = [{'path': 'syn/rules-pat.json', 'blob_sha256': sha(files['syn/rules-pat.json'])},
                 {'path': 'syn/rules-allow-v2.json' if v.get('allow_widened') else 'syn/rules-allow.json',
                  'blob_sha256': sha(files['syn/rules-allow-v2.json' if v.get('allow_widened') else
                                         'syn/rules-allow.json'])}]
        if v.get('allow_widened'):
            recs.append({'kind': 'superseded-rules', 'path': 'syn/rules-allow.json',
                         'blob_sha256': sha(files['syn/rules-allow.json'])})
        merges = [{'pr': '#7', 'commit': self.m1, 'first_parent': self.pin}]
        if v.get('second_merge'):
            merges.append({'pr': '#8', 'commit': self.H, 'first_parent': self.m1})

        def prof(name, kind, ptr, applies='tree', levels=None):
            src = {'path': 'syn/rules-pat.json', 'blob_sha256': sha(files['syn/rules-pat.json']),
                   'extractor': {'kind': 'json-pointer', 'selector': ptr}}
            value = json.loads(files['syn/rules-pat.json'])
            cur = value
            for part in ptr.split('/')[1:]:
                cur = cur[int(part)] if isinstance(cur, list) else cur[part]
            d = {'name': name, 'kind': kind, 'applies_to': applies, 'scope': 'corpus', 'source': src,
                 'pattern_sha256': sha(util.canonical(cur)), 'combine': 'any', 'levels': levels or ['line']}
            return d
        profiles = [prof('axiom-Z', 'review', '/rules/0/patterns'),
                    prof('Z-premise', 'deny', '/rules/1/patterns', levels=['line', 'sentence']),
                    prof('beta-word', 'review', '/rules/2/patterns')]
        if v.get('duplicate_profile'):
            profiles.append(dict(profiles[0]))
        if v.get('bad_pattern_hash'):
            profiles[0] = dict(profiles[0], pattern_sha256='0' * 64)
        lp = AD + 'line_patch.py'
        cfg = {'schema': 'oi-retirement-config/1', 'config_id': 'synthetic-retirement-config',
               'version': v.get('version', 1), 'supersedes': v.get('supersedes'),
               'retirement': {'name': 'synthetic', 'issue': 'none', 'owner': OWNER},
               'roles': {'scientific_base': self.H, 'pin': self.pin, 'side_change_classes': None},
               'corpus': {'patterns': [r'^doc/[^/]+\.md$']},
               'adapters': {'ledger': {'adapter': 'line-patch', 'adapter_version': 1,
                                       'module': {'path': lp, 'blob_sha256': sha(self.repo.read(self.pin, lp))},
                                       'path': 'syn/patch.json', 'blob_sha256': v.get('patch_sha', '0' * 64),
                                       'companion': []},
                            'sitemap': None, 'replay': None},
               'sites': [{'site_id': 's-def', 'file': DOC, 'line_sha256': sha(b'Definition one states the base object.'),
                          'carried': {'row': 'r', 'code': 'c', 'owner': 'o'}, 'kind': 'definition'},
                         {'site_id': 's-rem', 'file': DOC, 'line_sha256': sha(b'Remark two notes a side fact.'),
                          'carried': {'row': 'r', 'code': 'c', 'owner': 'o'}, 'kind': 'remark'},
                         {'site_id': 's-item', 'file': DOC, 'line_sha256': sha(b'- item first here'),
                          'carried': {'row': 'r', 'code': 'c', 'owner': 'o'}, 'kind': 'remark'}],
               'profiles': profiles,
               'checks': [{'id': 'zc', 'profiles': ['axiom-Z', 'beta-word', 'Z-premise'],
                           'final_profiles': v.get('final', ['axiom-Z']), 'default_for': ['coverage', 'terms']}],
               'rules': rules,
               'context_mapping': {'source_field': 'kind', 'values': {'definition': True, 'remark': False},
                                   'default': 'invalid'},
               'indicators': {'strip': [r'^\s*'], 'definitions': [{'name': 'list', 'on': 'line',
                                                                   'effect': 'structure-list',
                                                                   'patterns': [r'^\s*[-*+]\s+']}],
                              'list_item_patterns': [r'^\s*[-*+]\s+'], 'table_row_pattern': r'^\s*\|',
                              'caption_prefixes': []},
               'sentence': {'splitter_version': 2, 'abbreviations': ['e.g.']},
               'hp_obligations': [{'segment': [self.pin, self.H], 'merges': merges}],
               'delegation': {'path': 'syn/delegation.json', 'blob_sha256': sha(files['syn/delegation.json']),
                              'class_adapters': [{'adapter': 'artifact-hash', 'adapter_version': 1,
                                                  'module': {'path': AD + 'artifact_hash.py',
                                                             'blob_sha256': sha(self.repo.read(self.pin,
                                                                                               AD + 'artifact_hash.py'))}}]},
               'records': recs, 'operations': v.get('operations', ['coverage', 'execution', 'terms']),
               'controls': {'path': 'syn/controls.json', 'blob_sha256': sha(files['syn/controls.json'])},
               'author': WRITER}
        if v.get('widening_review_cfg'):
            cfg['widening_review'] = v['widening_review_cfg']
        for k in v.get('drop', []):
            cfg.pop(k, None)
        cfg.update(v.get('extra', {}))
        if v.get('schema'):
            cfg['schema'] = v['schema']
        if v.get('adapter_version'):
            cfg['adapters']['ledger']['adapter_version'] = v['adapter_version']
        path = v.get('config_path', 'syn/cfg/config.json')
        cb = jb(cfg)
        files[path] = cb
        cref = {'path': path, 'blob_sha256': sha(cb)}
        rv = {'schema': 'oi-review-record/1', 'reviewer': v.get('cfg_reviewer', REVIEWER), 'reviewed': cref,
              'method': 'read every referenced object', 'verdicts': [{'item': 'synthetic-retirement-config',
                                                                     'verdict': 'accept'}]}
        files[path.rsplit('/', 1)[0] + '/review.json'] = jb(rv)
        au = {'schema': 'oi-owner-authorization/1', 'owner': OWNER, 'time': 't0', 'comment_id': 'c-1',
              'authorizes': [{'record': cref, 'review': {'path': path.rsplit('/', 1)[0] + '/review.json',
                                                         'blob_sha256': sha(jb(rv))}}]}
        files[path.rsplit('/', 1)[0] + '/auth.json'] = jb(au)
        files.update(v.get('files', {}))
        if v.get('post'):
            files.update(v['post'](path, sha(cb)))
        commit = self.repo.derive(at, files, parents=self.repo.parents(at), subject=self.repo.subject(at))
        return commit, path, sha(cb), files

    def chain(self, files, path, reviewer):
        ref = {'path': path, 'blob_sha256': sha(files[path])}
        from ledger_coverage.engine import records as rec
        ids = rec.item_ids(json.loads(files[path]))
        rv = {'schema': 'oi-review-record/1', 'reviewer': reviewer, 'reviewed': ref, 'method': 'read',
              'verdicts': [{'item': i, 'verdict': 'accept'} for i in ids]}
        rp = path[:-5] + '.review.json'
        files[rp] = jb(rv)
        au = {'schema': 'oi-owner-authorization/1', 'owner': OWNER, 'time': 't0', 'comment_id': 'c-2',
              'authorizes': [{'record': ref, 'review': {'path': rp, 'blob_sha256': sha(files[rp])}}]}
        ap = path[:-5] + '.auth.json'
        files[ap] = jb(au)
        return [{'kind': 'review', 'path': rp, 'blob_sha256': sha(files[rp])},
                {'kind': 'authorization', 'path': ap, 'blob_sha256': sha(files[ap])}]


def patch_doc(base, edits):
    return jb({'schema': 'line patch v1', 'base': base, 'edits': [
        {'id': 'E%d' % (i + 1), 'file': DOC, 'old_line_sha256': sha(old.encode()), 'new_lines': new}
        for i, (old, new) in enumerate(edits)]})


def apply_text(text, edits):
    for old, new in edits:
        assert text.count(old + '\n') == 1
        text = text.replace(old + '\n', '\n'.join(new) + '\n')
    return text


class Runner:
    def __init__(self, out_root):
        self.out_root = out_root
        self.n = 0

    def out(self):
        self.n += 1
        return os.path.join(self.out_root, 'run%03d' % self.n)

    def cli(self, repo, args, commit, path, csha, harness=False, stderr=None):
        argv = args[:1] + ['--config', '%s:%s' % (commit, path), '--config-sha256', csha, '--out', self.out()] + \
            args[1:]
        return cli.run(argv, repo=repo, harness=harness, stderr=stderr or io.StringIO())


def y_world(syn, edits, extra_files=None, edits_doc=None, x_text=None):
    """Candidate X = H plus the edits; the patch record lives in X and in the configuration commit."""
    pd = edits_doc or patch_doc(syn.H, edits)
    txt = x_text if x_text is not None else apply_text(TEXT, edits)
    xf = {DOC: txt.encode()}
    xf.update(extra_files or {})
    X = syn.repo.derive(syn.H, xf, parents=[syn.H], subject='candidate')
    c, p, s, files = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}, at=syn.H)
    return X, c, p, s


def classes(res):
    return sorted({i['class'] for i in (res or {}).get('items', [])})


def y_controls(r):
    out = {}
    syn = Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.', '', 'Preface line two.'])]
    X, c, p, s = y_world(syn, edits)
    seg = ['--segment', '%s..%s' % (syn.pin, syn.H), '--segment', '%s..%s=%s:syn/patch.json' % (syn.H, X, c)]
    code, res = r.cli(syn.repo, ['coverage', '--commit', X] + seg, c, p, s)
    moved = all(st['statuses'][-1]['status'] == 'moved' for st in res.get('sites', [])) if res else False
    out['Y1'] = code == 0 and moved
    y1_engine = res and res['engine']['blob_sha256']
    Xb = syn.repo.derive(syn.H, {DOC: apply_text(TEXT, [('# synthetic', ['# synthetic', '', 'Preface line uno.',
                                                                          '', 'Preface line two.'])]).encode()},
                         parents=[syn.H])
    code, res = r.cli(syn.repo, ['coverage', '--commit', Xb, '--segment', '%s..%s' % (syn.pin, syn.H),
                                 '--segment', '%s..%s=%s:syn/patch.json' % (syn.H, Xb, c)], c, p, s)
    out['Y2'] = code == 20 and 'unauthorized-edit' in classes(res)
    e3 = [('Closing words of the file.', ['Closing words of the file.', '', 'Axiom Z is assumed.'])]
    X3, c3, p3, s3 = y_world(syn, e3)
    code, res = r.cli(syn.repo, ['coverage', '--commit', X3, '--segment', '%s..%s' % (syn.pin, syn.H),
                                 '--segment', '%s..%s=%s:syn/patch.json' % (syn.H, X3, c3)], c3, p3, s3)
    out['Y3'] = code == 20 and 'deny-match' in classes(res)
    code4, res4 = r.cli(syn.repo, ['terms', '--commit', syn.H], c, p, s)
    pd = patch_doc(syn.H, edits)
    cw, pw, sw, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'allow_widened': True})
    codew, resw = r.cli(syn.repo, ['terms', '--commit', syn.H], cw, pw, sw)
    cv, pv, sv, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'allow_widened': True,
                               'widening_review': True})
    codev, resv = r.cli(syn.repo, ['terms', '--commit', syn.H], cv, pv, sv)
    out['Y4'] = code4 == 0 and codew == 20 and 'record-invalid' in classes(resw) and codev == 0
    e5 = [('Axiom Z is the named premise of the synthetic world.',
           ['Axiom Z is the named premise of the synthetic world, restated.'])]
    X5, c5, p5, s5 = y_world(syn, e5)
    code, res = r.cli(syn.repo, ['coverage', '--commit', X5, '--segment', '%s..%s' % (syn.pin, syn.H),
                                 '--segment', '%s..%s=%s:syn/patch.json' % (syn.H, X5, c5)], c5, p5, s5)
    out['Y5'] = code == 20 and [i['class'] for i in res['items'] if i['subject'].endswith(':5@%s' % syn.pin[:8])] \
        == ['context-meaning-unverified']
    good_digest = (hashlib.sha256(apply_text(TEXT, edits).encode()).hexdigest() + '\n').encode()
    Xg, cg, pg, sg_ = y_world(syn, edits, {'out/digest.txt': good_digest})
    ex = ['execution', '--scientific-base', syn.H, '--candidate', Xg, '--ledger', '%s:syn/patch.json' % cg,
          '--edits', '%s:syn/patch.json' % cg, '--delegation', '%s:syn/delegation.json' % cg]
    out['_exec_note'] = 'execution needs an edits companion; the synthetic ledger has none'
    code_g, res_g = run_exec(r, syn, Xg, cg, pg, sg_)
    Xw, cw2, pw2, sw2 = y_world(syn, edits, {'out/digest.txt': b'0\n'})
    code_w, res_w = run_exec(r, syn, Xw, cw2, pw2, sw2)
    Xa, ca, pa, sa = y_world(syn, edits)
    code_a, res_a = run_exec(r, syn, Xa, ca, pa, sa)
    out['Y6'] = code_g == 0 and code_w == 20 and 'delegated-evidence-invalid' in classes(res_w) and code_a == 10 \
        and 'delegated-evidence-missing' in classes(res_a)
    code, res = r.cli(syn.repo, ['record', '--pin', syn.pin, '--record', syn.H], c, p, s)
    out['Y7'] = code == 65 and res['stop']['class'] == 'CONFIG_UNSUPPORTED'
    out['_Y8_engine'] = y1_engine
    e9 = [('Intro to the list:', ['Intro to the changed list:'])]
    X9, c9, p9, s9 = y_world(syn, e9)
    code, res = r.cli(syn.repo, ['coverage', '--commit', X9, '--segment', '%s..%s' % (syn.pin, syn.H),
                                 '--segment', '%s..%s=%s:syn/patch.json' % (syn.H, X9, c9)], c9, p9, s9)
    out['Y9'] = code == 10 and 'context-structure-changed' in classes(res)
    lp = AD + 'line_patch.py'
    c10 = syn.repo.derive(c, {lp: syn.repo.read(c, lp) + b' '}, parents=syn.repo.parents(c))
    code, res = r.cli(syn.repo, ['coverage', '--commit', X] + seg, c10, p, s)
    out['Y10'] = code == 65 and res['stop']['class'] == 'SOURCE_CHANGED'
    return out


def run_exec(r, syn, X, c, p, s):
    args = ['execution', '--scientific-base', syn.H, '--candidate', X, '--ledger', '%s:syn/patch.json' % c,
            '--delegation', '%s:syn/delegation.json' % c]
    return r.cli(syn.repo, args, c, p, s)


def z_controls(r):
    out = {}
    syn = Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
    pd = patch_doc(syn.H, edits)
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}

    def stop_of(variant, op=('terms', '--commit')):
        v = dict(base)
        v.update(variant)
        c, p, s, _ = syn.build(v)
        code, res = r.cli(syn.repo, [op[0], op[1], syn.H], c, p, s)
        return code, (res or {}).get('stop', {}).get('class')
    out['Z1'] = stop_of({'schema': 'oi-retirement-config/0'}) == (65, 'CONFIG_INVALID')
    out['Z2'] = stop_of({'drop': ['indicators']}) == (65, 'CONFIG_INVALID')
    out['Z3'] = stop_of({'extra': {'surprise': 1}}) == (65, 'CONFIG_INVALID')
    out['Z4'] = stop_of({'operations': ['coverage', 'execution']}) == (65, 'CONFIG_UNSUPPORTED')
    out['Z5'] = stop_of({'cfg_reviewer': WRITER}) == (65, 'CONFIG_UNREVIEWED')
    out['Z6'] = stop_of({'adapter_version': 2}) == (65, 'CONFIG_INVALID')
    c, p, s, files = syn.build(base)
    code, res = r.cli(syn.repo, ['terms', '--commit', syn.H], c, p, '1' * 64)
    out['Z6b'] = (code, res['stop']['class']) == (65, 'SOURCE_CHANGED')
    out['Z7'] = stop_of({'duplicate_profile': True}) == (65, 'CONFIG_INCONSISTENT') and \
        stop_of({'final': ['Z-premise']}) == (65, 'CONFIG_INCONSISTENT') and \
        stop_of({'bad_pattern_hash': True}) == (65, 'CONFIG_INCONSISTENT')
    out['Z8'] = stop_of({'no_controls': True}) == (70, 'CONFIG_NO_CONTROLS')
    # Z10: a merge added to the HP obligation is widening
    s2 = Syn(two_merges=True)
    pd2 = patch_doc(s2.H, [])
    b2 = {'patch_sha': sha(pd2), 'files': {'syn/patch.json': pd2}}
    c1, p1, h1, f1 = s2.build(b2)
    code, res = r.cli(s2.repo, ['coverage', '--commit', s2.H], c1, p1, h1)
    foreign = 'provenance-foreign' in classes(res)
    sup = {'path': p1, 'blob_sha256': h1}
    v2 = dict(b2, second_merge=True, version=2, supersedes=sup, config_path='syn/cfg2/config.json',
              files=dict(b2['files'], **{p1: f1[p1]}))
    c2, p2, h2, f2 = s2.build(v2)
    code_u, res_u = r.cli(s2.repo, ['coverage', '--commit', s2.H], c2, p2, h2)
    unrev = (code_u, (res_u or {}).get('stop', {}).get('class')) == (65, 'CONFIG_UNREVIEWED')
    # with a widening review by a third person and a matching HP adjudication
    from ledger_coverage.engine import segments as sgm
    fts = {}

    def dec(cm, pth):
        if (cm, pth) not in fts:
            fts[(cm, pth)] = sgm.FileText(s2.repo.read(cm, pth), pth)
        return fts[(cm, pth)]
    st, steps, region, det = sgm.walk_region(s2.repo, [s2.m1, s2.H], {s2.m1: s2.pin, s2.H: s2.m1}, DOC,
                                             ['Remark two notes a side fact.'], dec)
    adj = {'schema': 'oi-hp-adjudication/1', 'record_id': 'syn-hp', 'author': WRITER,
           'sites': [{'site_id': '%s:7@%s' % (DOC, s2.pin[:8]),
                      'steps': [{k: v for k, v in x.items() if k != 'post'} for x in steps],
                      'carried': {'row': 'r', 'code': 'c', 'owner': 'o'}, 'semantic_classification': 'restated',
                      'author': WRITER}]}

    def widening(path, cfg_sha):
        wr = {'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': WIDENER,
              'reviewed': {'path': path, 'blob_sha256': cfg_sha}, 'method': 'read the added merge and its chain',
              'verdicts': [{'item': 'synthetic-retirement-config', 'verdict': 'accept'}]}
        return {path.rsplit('/', 1)[0] + '/widening.json': jb(wr)}
    v3 = dict(v2, post=widening, records_extra={'syn/hp.json': adj})
    c3, p3, h3, f3 = s2.build(v3)
    code_a, res_a = r.cli(s2.repo, ['coverage', '--commit', s2.H, '--hp', '%s:syn/hp.json' % c3], c3, p3, h3)
    site = [x for x in (res_a or {}).get('sites', []) if x['site_id'].endswith(':7@%s' % s2.pin[:8])]
    adjudicated = bool(site) and site[0]['provenance'] is not None and \
        not [i for i in res_a['items'] if i['subject'] == site[0]['site_id']]
    v2b = dict(v2, records_extra={'syn/hp.json': adj})
    c4, p4, h4, f4 = s2.build(v2b)
    code_b, res_b = r.cli(s2.repo, ['coverage', '--commit', s2.H, '--hp', '%s:syn/hp.json' % c4], c4, p4, h4)
    out['_Z10_detail'] = {'v1': classes(res), 'v2_no_widening_review': (code_u, (res_u or {}).get('stop', {}).get('class')),
                          'v2_with_widening_review': (code_a, classes(res_a)), 'v2_hp_only': (code_b, (res_b or {}).get('stop', {}).get('class'))}
    out['Z10'] = foreign and unrev and adjudicated and (code_b, (res_b or {}).get('stop', {}).get('class')) == (65, 'CONFIG_UNREVIEWED')
    return out


def x_controls(r, repo_path):
    out = {}
    syn = Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
    X, c, p, s = y_world(syn, edits)
    # X2: an exception injected in classification becomes INTERNAL through the wrapper
    import ledger_coverage as pkg  # noqa: F401
    entry = os.path.join(tools, 'ledger_coverage.py')
    spec = __import__('importlib.util').util.spec_from_file_location('lc_entry', entry)
    mod = __import__('importlib.util').util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    orig = cli.op_terms

    def boom(*a, **k):
        raise RuntimeError('injected fault in the classification stage')
    cli.op_terms = boom
    o = r.out()
    real_run = cli.run
    cli.run = lambda argv: real_run(argv, repo=syn.repo, stderr=io.StringIO())
    try:
        code = mod.main(['terms', '--config', '%s:%s' % (c, p), '--config-sha256', s, '--out', o,
                         '--commit', syn.H])
    finally:
        cli.op_terms = orig
        cli.run = real_run
    doc = json.load(open(os.path.join(o, 'result.json')))
    out['X2'] = code == 71 and doc['outcome'] == 'INTERNAL'
    err = io.StringIO()
    o = r.out()
    code, res = cli.run(['terms', '--bogus', '--out', o], repo=syn.repo, stderr=err)
    out['X3'] = code == 64 and res is None and not os.path.exists(o) and json.loads(err.getvalue())['outcome'] == 'USAGE'
    code, res = cli.run(['terms', '--help'], repo=syn.repo, stderr=io.StringIO())
    code2, _ = cli.run(['--help'], repo=syn.repo, stderr=io.StringIO())
    out['X4'] = code == 64 and code2 == 64
    code, res = cli.run(['terms', '--out', r.out()], repo=syn.repo, stderr=io.StringIO())
    out['X5'] = code == 64
    X6 = syn.repo.derive(syn.H, {DOC: (TEXT + '\nA beta word appears.\n').encode()}, parents=[syn.H])
    code, res = r.cli(syn.repo, ['terms', '--commit', X6], c, p, s)
    out['X6'] = code == 10 and res['outcome'] == 'REVIEW_REQUIRED'
    # X7: a module of the package raises ImportError at import time
    tmp = tempfile.mkdtemp(prefix='x7-')
    try:
        shutil.copytree(os.path.join(tools, 'ledger_coverage'), os.path.join(tmp, 'ledger_coverage'),
                        ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy(entry, os.path.join(tmp, 'ledger_coverage.py'))
        with open(os.path.join(tmp, 'ledger_coverage', 'engine', 'outcome.py'), 'a') as f:
            f.write('\nraise ImportError("deliberately broken module")\n')
        o = os.path.join(tmp, 'out')
        pr = subprocess.run([sys.executable, '-I', '-B', os.path.join(tmp, 'ledger_coverage.py'), 'terms',
                             '--config', 'x:y', '--config-sha256', '0', '--out', o, '--commit', 'x'],
                            capture_output=True)
        doc = json.load(open(os.path.join(o, 'result.json'))) if os.path.exists(os.path.join(o, 'result.json')) \
            else None
        out['X7'] = pr.returncode not in (0, 20) and (doc is None or doc['outcome'] != 'PASS') and \
            not checker.accept(doc or {}, pr.returncode, {})
        out['_X7_exit'] = pr.returncode
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    pr = subprocess.run([sys.executable, '-I', '-B', os.path.join(tools, 'no_such_script.py')], capture_output=True)
    out['X8'] = pr.returncode == 2 and not checker.accept({}, pr.returncode, {})
    # X9: --final converts only the selected check's final profiles
    X9 = syn.repo.derive(syn.H, {DOC: (TEXT + '\nAxiom Z appears again.\n').encode()}, parents=[syn.H])
    a, ra = r.cli(syn.repo, ['terms', '--commit', X9, '--check', 'zc'], c, p, s)
    b, rb = r.cli(syn.repo, ['terms', '--commit', X9, '--check', 'zc', '--final'], c, p, s)
    d, rd = r.cli(syn.repo, ['terms', '--commit', X6, '--check', 'zc', '--final'], c, p, s)
    e, re_ = r.cli(syn.repo, ['terms', '--commit', X9, '--final'], c, p, s)
    out['X9'] = a == 10 and b == 20 and 'final-unclassified' in classes(rb) and d == 10 and e == 64
    # X10: the acceptance predicate
    good, rg = r.cli(syn.repo, ['terms', '--commit', syn.H], c, p, s)
    pins = {'engine': rg['engine']['blob_sha256'], 'config': rg['config']['blob_sha256']}
    edited = dict(rg, outcome='FAIL')
    other = dict(rg, engine=dict(rg['engine'], blob_sha256='f' * 64))
    out['X10'] = checker.accept(rg, good, pins) and not checker.accept(edited, 0, pins) and \
        not checker.accept(other, 0, pins) and checker.recompute(rg) == 'PASS'
    # M10: --out inside the repository checkout is refused
    code, res = cli.run(['terms', '--config', 'x:y', '--config-sha256', '0', '--out',
                         os.path.join(repo_path, 'no-such-out-dir'), '--commit', 'x', '--repo', repo_path],
                        stderr=io.StringIO())
    out['M10'] = code == 64 and not os.path.exists(os.path.join(repo_path, 'no-such-out-dir'))
    # schema: every result written above validates
    from ledger_coverage.engine import schema
    bad = []
    for root, dirs, fs in os.walk(r.out_root):
        for f in fs:
            if f == 'result.json':
                d_ = json.load(open(os.path.join(root, f)))
                if schema.validate(d_):
                    bad.append((root, schema.validate(d_)[:2]))
                if d_.get('outcome') not in ('USAGE', 'INTERNAL', 'ERROR', 'VOID') and checker.recompute(d_) != d_['outcome']:
                    bad.append((root, 'checker disagrees'))
    out['S7-schema-and-checker'] = not bad
    out['_S7_bad'] = bad[:3]
    return out


def z9_controls():
    """Z9a-Z9f on in-memory engine trees; values and patterns are planted here, outside the purity scope."""
    from ledger_coverage.engine import profiles as prf
    hexid = hashlib.sha1(b'planted').hexdigest()
    a1 = prf.Profile({'name': 'p', 'kind': 'review', 'applies_to': 'tree', 'source': {'extractor': {'kind': 'x'}}},
                     [r'\bA1\b'])
    vals = {'per unit Q2', 'a1exit deletion exact-edit ledger v2', r'\bA1\b'}

    def lint(src):
        return purity.lint_sources({'engine/m.py': src}, vals, [a1])
    out = {'Z9a': bool(lint('x = %r\n' % hexid)), 'Z9b': bool(lint('x = %r\n' % hexid[:7])),
           'Z9c': bool(lint('x = %r\n' % r'\bA1\b')), 'Z9d': bool(lint("x = 'per unit Q2'\n")),
           'Z9e': not lint("x = {'splices': []}\n")}
    adapter_ok = not purity.lint_sources({}, vals, [a1])
    out['Z9f'] = adapter_ok and bool(lint("x = 'a1exit deletion exact-edit ledger v2'\n"))
    return out


def run_all(out_root, repo_path):
    r = Runner(out_root)
    res = {}
    for name, fn in (('Y', lambda: y_controls(r)), ('Z', lambda: z_controls(r)), ('X', lambda: x_controls(r, repo_path)),
                     ('Z9', z9_controls)):
        try:
            res.update(fn())
        except Exception as exc:
            import traceback
            res['%s-group-error' % name] = '%s: %s %s' % (type(exc).__name__, exc, traceback.format_exc()[-1500:])
    return res


if __name__ == '__main__':
    root = tempfile.mkdtemp(prefix='syn-controls-', dir=sys.argv[1] if len(sys.argv) > 1 else None)
    res = run_all(root, sys.argv[2] if len(sys.argv) > 2 else os.getcwd())
    print(json.dumps(res, indent=1, sort_keys=True, default=str))
