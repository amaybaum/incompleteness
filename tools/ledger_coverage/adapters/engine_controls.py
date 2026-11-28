"""Records of the engine controls (the self-test's controls of engine/controls_engine.py) for the gate (design r6,
R6.GATE.5 and R6.GATE.7).

It runs every engine control exactly as `ledger_coverage.py self-test` does, with the engine's capture hook set:
each in-process stage result the controls compute (coverage, execution and terms items, with sites and side
changes) is retained as a result document whose outcome and exit status the tool's own outcome function gives,
and bound to the control assigned next. It writes `control-records.json` (oi-control-records/1) and
`evidence/engine-self-test/<id>/` into DIR. A group that raises is one FAIL record, `<group>-group-error`.

Usage: python3 -I -S -B tools/ledger_coverage/adapters/engine_controls.py DIR
"""
import json
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    # the package is loaded by its location, as the entry point loads it; no directory is put on sys.path
    import importlib.util
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.engine import controls_engine as ce  # noqa: E402
from ledger_coverage.adapters import control_records  # noqa: E402

JOB = 'engine-self-test'


class Capture(object):
    def __init__(self, rec):
        self.rec = rec
        self.runs_of = {}
        self.procedures = {}
        self.files = {}

    def result_map(self):
        return control_records.RunMap(self.rec, self.runs_of)

    def name_last(self, case, bindings, baseline=None):
        """Names the last stage result; `baseline` names an earlier case of the same control whose result a
        restored case is compared with."""
        base = None
        if baseline is not None:
            base = next((r for r in self.rec.pending if r['case'] == baseline), None)
        self.rec.name_last(case, bindings=dict(bindings), baseline=base)

    def attest(self, case, values):
        """Values the runner states for a named case (checked by the gate for integrity only)."""
        run = next((r for r in self.rec.pending if r['case'] == case), None)
        if run is not None and values:
            run['attested'] = dict(run.get('attested') or {}, **values)

    def count(self):
        return len(self.rec.pending)

    def bind_first(self, bindings):
        run = next((r for r in self.rec.pending if r['case'] is None), None)
        if run is not None:
            run['case'], run['bindings'] = '', dict(bindings)

    def stage(self, label, items, **facts):
        self.rec.capture_doc('engine control stage: %s (controls_engine.py)' % label,
                             control_records.stage_doc(items, operation=label, **facts))


def extra_controls(cap):
    """Rows whose runner is this adapter rather than the self-test: RECLINT-ORPHAN (R6.REC.10) and
    PIPE-UNRESOLVED (R6.PIPE.7), on the engine's neutral in-memory trees."""
    out = cap.result_map()
    ce.capture_hook = cap
    try:
        # RECLINT-ORPHAN: an HP adjudication entry naming a site_id that no tracked site carries
        w, h, sg = ce.hp_world()
        sid = '%s:%d@%s' % (ce.doc_path, 5, w.pin[:8])
        steps = ce.walk_steps(w, h, sg, 5)
        good = {'site_id': sid, 'steps': steps, 'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'},
                'semantic_classification': 'stated', 'author': 'session.fixture-eng-writer'}
        orphan_id = '%s:%d@%s' % (ce.doc_path, 99, w.pin[:8])
        orphan = dict(good, site_id=orphan_id)
        cv, it = w.coverage(h, [sg], adj={'hp': [good, orphan]}, hits=False)
        ce._case('an HP adjudication record entry that, on a tree and in a segment to which the record applies, '
                 'matches no subject (orphan)', entry=orphan_id)
        c1 = any(i['class'] == 'stale-adjudication' and i['obligation'] == 'HP' and i['subject'] == orphan_id
                 for i in it)
        # a context adjudication entry and a hit classification entry, each for a segment of the chain, whose
        # subject is no tracked site / no line of the tree: FAIL record-invalid for each (one run)
        sname = '%s..%s' % (sg['from'][:8], sg['to'][:8])
        ctx_orphan = {'site_id': orphan_id, 'segment': sname, 'from_context_sha256': 'f' * 64,
                      'to_context_sha256': 'e' * 64}
        hit_orphan = {'id': 'hit-orphan', 'file': ce.doc_path, 'line_sha256': 'a' * 64, 'segment': sname,
                      'profiles': ['np-review']}
        cv, it_c = w.coverage(h, [sg], adj={'hp': [good], 'context': [ctx_orphan]}, hits=True,
                              hit_records=[hit_orphan])
        ce._case('a context adjudication or hit classification entry matching no subject on a tree and segment its '
                 'record applies to (orphan)', entry=orphan_id)
        c2 = any(i['class'] == 'record-invalid' and i['subject'] == orphan_id for i in it_c) and \
            any(i['class'] == 'record-invalid' and i['subject'] == 'hit-orphan' for i in it_c)
        # two HP entries naming the same site (duplicate): FAIL record-invalid naming the record, neither applied.
        # The entries carry the in-memory reference the entry point gives an admitted record's entries (`_ref`).
        rec_path = 'verification/fixture/hp-adjudication.json'
        d1 = dict(good, _ref={'path': rec_path})
        d2 = dict(good, semantic_classification='stated twice', _ref={'path': rec_path})
        cv_d, it_d = w.coverage(h, [sg], adj={'hp': [d1, d2]}, hits=False)
        ce._case('two entries naming the same subject (duplicate)', record=rec_path)
        c3 = any(i['class'] == 'record-invalid' and i['subject'] == rec_path for i in it_d) and \
            not cv_d.site_out[sid].get('provenance_adjudicated')
        # the same orphans naming a segment outside the chain and another tree: out of scope, no finding
        far = '0' * 8 + '..' + '1' * 8
        cv, it_o = w.coverage(h, [sg], adj={'hp': [good], 'context': [dict(ctx_orphan, segment=far)]}, hits=True,
                              hit_records=[dict(hit_orphan, segment=None, tree='2' * 40)])
        ce._case('the orphan entry naming a segment outside the chain, or a tree the record does not apply to')
        c4 = not [i for i in it_o if i['class'] in ('stale-adjudication', 'record-invalid')] and \
            sorted(x['schema'] for x in w.last_out_of_scope) == ['oi-context-adjudication/1', 'oi-hit-classification/1']
        # operation D (terms, no chain; cli op_terms passes an empty chain): an entry naming no tree and no segment
        # applies to the terms tree, and one matching no line is FAIL record-invalid; an entry naming a segment is
        # out of scope there (no finding)
        from ledger_coverage.engine import pipeline as pl
        ctx_d = w.ctx()
        tm = pl.Terms(ctx_d, h, [ctx_d.profiles['np-review']], [ctx_d.profiles['np-deny']],
                      hit_records=[dict(hit_orphan, id='hit-orphan-d', segment=None),
                                   dict(hit_orphan, id='hit-segment-d')], chain_segments=[])
        tm.deny()
        tm.review()
        ce._stage('terms', tm.items, out_of_scope=tm.out_of_scope)
        ce._case('operation D: a hit classification entry naming no tree and no segment, matching no line of the '
                 'terms tree (orphan)', entry='hit-orphan-d')
        c6 = any(i['class'] == 'record-invalid' and i['subject'] == 'hit-orphan-d' for i in tm.items) and \
            not [i for i in tm.items if i['subject'] == 'hit-segment-d'] and \
            [x['id'] for x in tm.out_of_scope] == ['hit-segment-d']
        cv, it2 = w.coverage(h, [sg], adj={'hp': [good]}, hits=False)
        ce._case('the record without the orphan and duplicate entries (positive)')
        c5 = not [i for i in it2 if i['class'] in ('stale-adjudication', 'record-invalid')]
        out['RECLINT-ORPHAN'] = c1 and c2 and c3 and c4 and c5 and c6
        out['_RECLINT-ORPHAN'] = {'hp_orphan': c1, 'context_and_hit_orphan': c2, 'duplicate': c3,
                                  'out_of_scope': c4, 'positive': c5, 'operation_d_hit_orphan': c6}

        # PIPE-UNRESOLVED: a site lost in the first of two segments is reported there only, its state unresolved
        w = ce.World()
        line = 'beta line two stands here.\n'
        x1 = w.child(w.pin, ce.base_text.replace(line, ''), subject='site removed')
        x2 = w.child(x1, files={ce.other_path: b'unrelated\n'}, subject='unrelated change')
        s1, s2 = ce.seg(w.pin, x1), ce.seg(x1, x2)
        cv, it = w.coverage(x2, [s1, s2], hits=False)
        site = '%s:5@%s' % (ce.doc_path, w.pin[:8])
        n1, n2 = '%s..%s' % (w.pin[:8], x1[:8]), '%s..%s' % (x1[:8], x2[:8])
        ce._case('', site=site, first_segment=n1, second_segment=n2)
        mine = [(i['class'], i['segment']) for i in it if i['subject'] == site]
        x2r = w.child(w.pin, files={ce.other_path: b'unrelated\n'}, subject='restored')
        w.coverage(x2r, [ce.seg(w.pin, x2r)], hits=False)
        ce._case('baseline')
        w.coverage(x2r, [ce.seg(w.pin, x2r)], hits=False)
        ce._case('restored', baseline='baseline')
        from ledger_coverage.engine.cli import site_state
        state = site_state(cv.site_out[site])
        out['PIPE-UNRESOLVED'] = mine == [('missing', n1)] and state == 'unresolved'
        out['_PIPE-UNRESOLVED'] = {'items': mine, 'state': state}
    finally:
        ce.capture_hook = None
    return out


def class_controls(cap):
    """Retain the actual execution and coverage stages for the named class controls."""
    from ledger_coverage.adapters import a1exit_exact_edit as exact_edit
    from ledger_coverage.engine import execution as exmod

    out = cap.result_map()
    ce.capture_hook = cap
    try:
        guard = 'checks/fixture_pin.py'
        targets = ('notes/first.md', 'notes/second.md')
        old = 'the former fixture term remains in use'
        new = 'the revised fixture term remains in use'
        old_guard = 'EXPECTED = %r\n' % old
        new_guard = 'EXPECTED = %r\n' % new
        w = ce.World(extra={guard: old_guard.encode(), **{p: old.encode() for p in targets}})
        led = ce.ledger(w.pin, [(guard, 0, len(old_guard), new_guard)], w.repo)
        led['guard_pins'] = exact_edit.guard_pins([{'id': 'guard-edit', 'file': guard, 'old': old_guard,
                                                   'new': new_guard, 'kind': 'guard-pin', 'targets': targets}])
        good = {guard: new_guard.encode(), **{p: new.encode() for p in targets}}

        def pins(changes):
            x = w.child(w.pin, files=changes, subject='guard pin target fixture')
            ex = exmod.Execution(w.ctx(), w.pin, x, led)
            ex.pins({'min_len': 20, 'skip_prefixes': [], 'ok': []})
            return ce._stage('execution', ex.items, roles={'H': w.pin, 'X': x}, guard_pins=led['guard_pins'],
                             entries={p: w.repo.read(x, p).decode() for p in (guard, *targets)})

        outside_guard = pins({**good, guard: old_guard.encode()})
        ce._case('an updated guard pin whose new literal is absent from its file')
        outside_target = pins({**good, targets[1]: old.encode()})
        ce._case('an updated guard pin whose new literal does not occur in one of its targets')
        ce._restore_with(lambda: pins(good), 'execution')
        out['CLASS-PIN-TARGET'] = [(i['class'], i['subject']) for i in outside_guard] == [
            ('pin-target-missing', 'guard-edit')] and [(i['class'], i['subject']) for i in outside_target] == [
            ('pin-target-missing', 'guard-edit->' + targets[1])]

        w = ce.World(sites=[(5, 'sr')])
        site_line = ce.base_text.splitlines()[4]

        def hp(steps):
            parent = w.pin
            parents = {}
            for text in steps:
                child = w.child(parent, text, subject='historical provenance fixture')
                parents[child] = parent
                parent = child
            seg = ce.seg(w.pin, parent, 'hp', chain=list(parents), parent_of=parents, merges=set(parents),
                         obligation='HP')
            return w.coverage(parent, [seg], hits=False, facts={
                'files_at_chain': {c: w.repo.read(c, ce.doc_path).decode() for c in [w.pin, *parents]},
                'chain': seg['chain'], 'parent_of': parents, 'pin_line': site_line})[1]

        duplicated = ce.base_text + site_line + '\n'
        dup_items = hp([duplicated, duplicated + 'A new end of file.\n'])
        ce._case('an HP region not unique as a whole-line block at a parent')
        # The distinct closest anchors exchange positions and the original site changes.
        lines = ce.base_text.splitlines(keepends=True)
        lines[2], lines[6] = lines[6], lines[2]
        lines[4] = 'A revised site between the anchors.\n'
        rev_items = hp([''.join(lines)])
        ce._case('HP anchors that do not keep their order')
        ce._restore_with(lambda: hp([ce.base_text]), 'coverage')
        out['CLASS-PROV-AMBIGUOUS'] = all(ce.classes(items) == ['provenance-ambiguous']
                                         for items in (dup_items, rev_items))

        w = ce.World(extra={ce.other_path: b'An unchanged unledgered file.\n'})
        at = ce.off(ce.base_text, 'beta line two')
        led = ce.ledger(w.pin, [(ce.doc_path, at, at + len('beta line two'), 'beta line revised')], w.repo)
        text = ce.base_text.replace('beta line two', 'beta line revised', 1)

        def segment(files):
            x = w.child(w.pin, text, files=files, subject='ledgered segment file-scope fixture')
            return w.coverage(x, [ce.seg(w.pin, x, 'ledgered', ledger=led)], hits=False, facts={
                'roles': {'FROM': w.pin, 'TO': x}, 'ledger_paths': sorted(led['files']),
                'file_entries': [w.repo.read(c, ce.other_path).decode() for c in (w.pin, x)]})[1]

        items = segment({ce.other_path: b'A changed unledgered file.\n'})
        ce._case('in a ledgered segment, a file not in the ledger whose bytes differ between FROM and TO')
        ce._restore_with(lambda: segment({}), 'coverage')
        out['CLASS-UNLEDGERED'] = [(i['class'], i['subject']) for i in items] == [
            ('unledgered-file-change', ce.other_path)]
    finally:
        ce.capture_hook = None
    return out


def class_entrypoint_controls(cap):
    """Check the retained, class-record and replay predicates through their adapter and CLI routes."""
    from ledger_coverage.adapters import a1exit_exact_edit as exact_edit, a1exit_sitemap as sitemap
    from ledger_coverage.adapters import synthetic_fixture as sf
    from ledger_coverage.engine import cli

    out = cap.result_map()
    runner = sf.Runner(os.path.join(cap.rec.out_dir, 'class-cases'))
    unwrap = cap.rec.wrap_cli(cli)

    def run(syn, variant, args, case, baseline=None):
        commit, path, digest, _ = syn.build(variant)
        code, result = runner.cli(syn.repo, args(commit), commit, path, digest)
        cap.rec.name_last(case, baseline=baseline)
        return code, result or {}

    try:
        syn = sf.Syn()
        adapter_path = sf.AD + 'a1exit_exact_edit.py'
        adapter = sf.module_bytes('a1exit_exact_edit.py')
        syn.H = syn.repo.derive(syn.H, {adapter_path: adapter}, subject='exact ledger adapter fixture')
        h_bytes = syn.repo.read(syn.H, sf.DOC)
        retained_text = 'Remark two notes a side fact.'
        edit = {'id': 'retained-fixture', 'file': sf.DOC, 'site': 's-rem', 'part': 'text',
                'old': retained_text, 'new': retained_text}
        at = h_bytes.index(retained_text.encode())
        ld, ep = 'syn/exact-ledger.json', 'syn/edits.json'

        def retained(case, edits, splice=False, changed=False, baseline=None):
            eb = sf.jb({'schema': exact_edit.EDITS_SCHEMA, 'edits': edits})
            splices = []
            if splice:
                splices.append({'id': edit['id'], 'file': sf.DOC, 'start': at, 'end': at + len(retained_text),
                                'new': retained_text, 'old_sha256': sf.sha(retained_text.encode()),
                                'new_sha256': sf.sha(retained_text.encode())})
            digest = sf.sha(h_bytes)
            lb = sf.jb({'schema': exact_edit.LEDGER_SCHEMA, 'base': syn.H, 'edits_sha256': sf.sha(eb),
                        'splices': splices, 'files': {sf.DOC: {'base_sha256': digest, 'expected_sha256': digest}},
                        'retained_unchanged': [edit['id']]})
            spec = {'adapter': exact_edit.NAME, 'adapter_version': exact_edit.VERSION,
                    'module': {'path': adapter_path, 'blob_sha256': sf.sha(adapter)},
                    'path': ld, 'blob_sha256': sf.sha(lb),
                    'companion': [{'role': 'edits', 'path': ep, 'blob_sha256': sf.sha(eb)}]}
            x_bytes = h_bytes.replace(retained_text.encode(), b'Remark two records a changed fact.') \
                if changed else h_bytes
            x = syn.repo.derive(syn.H, {sf.DOC: x_bytes}, subject='retained edit fixture')
            variant = {'files': {ld: lb, ep: eb},
                       'extra': {'adapters': {'ledger': spec, 'sitemap': None, 'replay': None}}}
            return run(syn, variant, lambda c: ['execution', '--scientific-base', syn.H, '--candidate', x,
                                                '--ledger', c + ':' + ld, '--edits', c + ':' + ep], case, baseline)

        ret = [retained('a ledger entry listed as retained that is absent from edits.json', []),
               retained('a ledger entry listed as retained that has a splice', [edit], splice=True),
               retained('a ledger entry listed as retained whose site text differs between H and X', [edit],
                        changed=True)]
        retained('baseline', [edit])
        retained('restored', [edit], baseline=cap.rec.pending[-1])
        out['CLASS-RETAINED'] = all(code == 20 and 'retained-changed' in sf.classes(result) for code, result in ret)

        syn = sf.Syn()
        first, second = 'notes/first.txt', 'notes/second.txt'
        sides = {first: b'first side record\n', second: b'second side record\n'}
        m = syn.repo.derive(syn.H, sides, subject='class schema fixture main')
        x = syn.repo.derive(syn.H, {}, subject='class schema fixture candidate')
        patch = sf.patch_doc(syn.H, [])
        base_path, tip_path = 'syn/side-classes-root.json', 'syn/side-classes-tip.json'
        pin = {'path': first, 'blob_sha256': sf.sha(sides[first])}
        root = {'schema': 'oi-side-change-classes/1', 'record_id': 'fixture-classes', 'author': sf.WRITER,
                'supersedes': None, 'classes': [{'id': 'notes', 'prefixes': ['notes'], 'pins': [pin]}]}
        good = 'a class record whose classes carry id, prefixes and pins [{path, blob_sha256}] (positive)'

        def classes(case, entry=None, successor=False, baseline=None):
            files = {'syn/patch.json': patch}
            primary = tip_path if successor else base_path
            records = []
            if successor:
                files[base_path] = sf.jb(root)
                syn.chain(files, base_path, sf.REVIEWER)
                predecessor = {'path': base_path, 'blob_sha256': sf.sha(files[base_path])}
                entry = dict(root['classes'][0], pins=[pin, {'path': second, 'blob_sha256': sf.sha(sides[second])}])
            else:
                predecessor = None
            files[primary] = sf.jb(dict(root, classes=[entry or root['classes'][0]], supersedes=predecessor))
            ref = {'path': primary, 'blob_sha256': sf.sha(files[primary])}
            records.append({'kind': 'side-change-classes', **ref})
            records.extend(syn.chain(files, primary, sf.REVIEWER))
            variant = {'patch_sha': sf.sha(patch), 'files': files, 'add_records': records,
                       'extra': {'roles': {'scientific_base': syn.H, 'pin': syn.pin, 'side_change_classes': ref}}}
            return run(syn, variant, lambda c: ['execution', '--scientific-base', syn.H, '--candidate', x,
                                                '--main', m, '--ledger', c + ':syn/patch.json'], case, baseline)

        _, clean = classes(good)
        clean_run = cap.rec.pending[-1]
        cls = root['classes'][0]
        adversaries = [
            classes('countercase: a pin carrying git_blob (a key outside the table)',
                    dict(cls, pins=[dict(pin, git_blob=syn.repo.blob_id(m, first))])),
            classes('countercase: a class carrying the class-level paths form',
                    {'id': 'notes', 'prefixes': ['notes'], 'paths': [first], 'blob_sha256': pin['blob_sha256']}),
            classes('countercase: a superseding class record that adds a pin without a widening review',
                    successor=True),
        ]
        classes('restored', baseline=clean_run)
        first_class = next((entry.get('class') for entry in clean.get('side_changes', []) if entry['path'] == first),
                           None)
        out['CLASS-SCHEMA'] = first_class == 'notes' and not (
            {'base-drift', 'record-invalid'} & set(sf.classes(clean))) and all(
                code == 20 and 'record-invalid' in sf.classes(result) for code, result in adversaries)

        syn = sf.Syn()
        modules = {sf.AD + p: sf.module_bytes(p) for p in ('a1exit_sitemap.py', 'python_frozen_replay.py')}
        syn.H = syn.repo.derive(syn.H, modules, subject='record adapters fixture')
        record = 'syn/frozen/'
        checker = b'''import hashlib, json, os
HERE = os.path.dirname(__file__)
SITEMAP = os.path.join(HERE, "sitemap.json")
ROWS = os.path.join(HERE, "rows.json")
def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
def manuscript_digest():
    with open("doc/s.md", "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
def build():
    rows = load(ROWS)
    return dict(rows["site_map"], manuscript_digest=manuscript_digest())
def render(sm, rows):
    return {"body": rows["summary"]}
def splice_block(text, name, replacement):
    return replacement
def check(sm, rows, quiet=True):
    return [] if sm["pin"] == rows["site_map"]["pin"] else ["record pin differs from its source"]
def extended_unmapped(sm):
    return [site["file"] for site in sm["sites"] if not os.path.isfile(site["file"])]
def self_test():
    return manuscript_digest() == load(ROWS)["digest"]
def main():
    raise AssertionError("the replay called frozen main")
'''
        pin_text = syn.repo.read(syn.pin, sf.DOC)
        wanted = sf.sha(pin_text)
        smap = {'schema': sitemap.SITEMAP_SCHEMA, 'pin': syn.pin,
                'sites': [{'file': sf.DOC, 'line': 5, 's3': 'definition'}]}
        summary = 'Fixture record summary.\n'
        inserted_line = 'An inserted line in the record tree.'

        def record_checks(case, mutant=False, baseline=None, override=None, shifted=False, frozen_failure=False,
                          retain=None):
            rows = {'site_map': smap, 'digest': wanted, 'summary': summary}
            if mutant:
                override = 'fixture anchor absent from the pinned line'
            if override is not None:
                rows['site_overrides'] = {sf.DOC + ':5': {'anchor': override}}
            frozen_code = (checker.replace(b'def build():\n', b'def build():\n    raise LookupError("fixture failure")\n')
                           if frozen_failure else checker)
            blobs = {record + 'ledger_check.py': frozen_code, record + 'rows.json': sf.jb(rows),
                     record + 'sitemap.json': sf.jb(dict(smap, manuscript_digest=('0' * 64 if mutant else wanted))),
                     record + 'LEDGER.md': summary.encode()}
            if shifted:
                blobs[sf.DOC] = (inserted_line + '\n').encode() + pin_text
            rc = syn.repo.derive(syn.H, blobs, subject='record checks fixture')

            def module(name):
                p = sf.AD + name
                return {'path': p, 'blob_sha256': sf.sha(modules[p])}
            sm_path, rows_path = record + 'sitemap.json', record + 'rows.json'
            ads = {'sitemap': {'adapter': sitemap.NAME, 'adapter_version': sitemap.VERSION,
                               'module': module('a1exit_sitemap.py'), 'commit': rc, 'path': sm_path,
                               'blob_sha256': sf.sha(blobs[sm_path]),
                               'companion': [{'role': 'rows', 'path': rows_path, 'blob_sha256': sf.sha(blobs[rows_path])}]},
                   'replay': {'adapter': 'python-frozen-replay', 'adapter_version': 1,
                              'module': module('python_frozen_replay.py'), 'module_path': record + 'ledger_check.py',
                              'record_tree': syn.repo.tree_id(rc, record[:-1])}}
            variant = {'operations': ['record'], 'control_ops': ['record'], 'drop': ['sites'],
                       'extra': {'adapters': ads, 'roles': {'scientific_base': syn.H, 'pin': syn.pin,
                                                           'record_commit': rc, 'side_change_classes': None}}}
            observed = run(syn, variant, lambda _: ['record', '--pin', syn.pin, '--record', rc], case, baseline)
            if retain:
                cid, label = retain
                files = cap.files.setdefault(cid, {})
                if cid == 'ANCH-OVERRIDE':
                    files['pin.txt'] = pin_text
                    files[label + '.record.txt'] = syn.repo.read(rc, sf.DOC)
                    files[label + '.rows.json'] = blobs[rows_path]
                else:
                    argv = cap.rec.pending[-1]['argv']
                    replay = os.path.join(argv[argv.index('--out') + 1], 'replay')
                    for output in ('replay-result.json', record + 'ledger_check.py'):
                        with open(os.path.join(replay, output), 'rb') as f:
                            files[label + '.' + os.path.basename(output)] = f.read()
            return observed

        code, result = record_checks('', mutant=True)
        clean_code, clean = record_checks('baseline')
        restore_code, restored = record_checks('restored', baseline=cap.rec.pending[-1])
        out['CLASS-RECORD-CHECKS'] = code == 20 and clean_code == restore_code == 0 and {
            'digest_equal', 'rebuild_equal', 'pin_findings'
        } <= {i['subject'] for i in result.get('items', []) if i['obligation'] == 'RECORD' and
              i['class'] == 'record-invalid'} and clean.get('record_checks') == restored.get('record_checks')

        fixture_anchor = pin_text.splitlines()[4].decode('utf-8')
        bad_code, bad = record_checks('an override whose anchor is not a substring of the pin line',
                                      override=inserted_line, shifted=True, retain=('ANCH-OVERRIDE', 'adverse'))
        good_code, good = record_checks('a valid override whose pin-line text moves after the pin '
                                        '(positive: the anchor is never searched later)',
                                        override=fixture_anchor, shifted=True, retain=('ANCH-OVERRIDE', 'clean'))
        baseline = cap.rec.pending[-1]
        restored_code, clean = record_checks('restored', baseline=baseline, override=fixture_anchor, shifted=True,
                                             retain=('ANCH-OVERRIDE', 'restored'))
        out['ANCH-OVERRIDE'] = (bad_code == 20 and sf.classes(bad) == ['record-invalid'] and
                                bool(bad['record_checks']['pin_findings']) and good_code == restored_code == 0 and
                                not good['record_checks']['pin_findings'] and
                                good['record_checks'] == clean['record_checks'])

        frozen_code, frozen_result = record_checks('', frozen_failure=True, retain=('OUT-FROZEN', 'adverse'))
        clean_code, clean = record_checks('baseline', retain=('OUT-FROZEN', 'clean'))
        restored_code, restored = record_checks('restored', baseline=cap.rec.pending[-1], retain=('OUT-FROZEN', 'restored'))
        failure = frozen_result.get('stop') or {}
        out['OUT-FROZEN'] = (frozen_code == 71 and failure.get('message') == 'build raised LookupError: fixture failure'
                             and failure.get('detail', {}).get('calls') ==
                             ['load_sitemap', 'load_rows', 'manuscript_digest']
                             and clean_code == restored_code == 0 and clean == restored)
    finally:
        unwrap()
    return out


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    rec = control_records.Recorder(JOB, out_dir)
    cap = Capture(rec)
    ce.capture_hook = cap
    try:
        results = ce.run(None)
    finally:
        ce.capture_hook = None
    try:
        extra = extra_controls(cap)
    except Exception as exc:
        extra = {'extra-group-error': '%s: %s' % (type(exc).__name__, exc)}
    try:
        extra.update(class_controls(cap))
    except Exception as exc:
        cap.rec.discard()
        extra['class-group-error'] = '%s: %s' % (type(exc).__name__, exc)
    try:
        extra.update(class_entrypoint_controls(cap))
    except Exception as exc:
        cap.rec.discard()
        extra['class-entrypoint-error'] = '%s: %s' % (type(exc).__name__, exc)
    from ledger_coverage.adapters import recon_controls
    try:
        extra.update(recon_controls.recon_controls(cap))
    except Exception as exc:
        import traceback
        extra['recon-group-error'] = '%s: %s %s' % (type(exc).__name__, exc, traceback.format_exc()[-1200:])
    try:
        extra.update(recon_controls.landing_controls(cap))
    except Exception as exc:
        extra['landing-group-error'] = '%s: %s' % (type(exc).__name__, exc)
    for cid, v in sorted(extra.items()):
        if cid.startswith('_'):
            continue
        rec.pending = cap.runs_of.get(cid, [])
        rec.record(cid, 'PASS' if v is True else 'FAIL', {'value': v, 'detail': extra.get('_' + cid)},
                   'the boolean computed for this id in adapters/engine_controls.py', files=cap.files.get(cid))
    for r in results:
        if r['id'] == 'RB-P1':
            # The conformance runner retains both RB-P1 executions. Keep this route unit check in the self-test.
            continue
        cid = r['id'] if 'error' not in r else '%s-group-error' % r['id']
        rec.pending = cap.runs_of.get(r['id'], []) if 'error' not in r else []
        rec.record(cid, 'PASS' if r['passed'] else 'FAIL', r.get('error', r['passed']),
                   'the boolean computed for this id in engine/controls_engine.py',
                   procedure=cap.procedures.get(r['id']))
    rec.write()
    n = sum(1 for r in results if r['passed'])
    print(json.dumps({'controls': len(results), 'passed': n}))
    return 0 if n == len(results) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
