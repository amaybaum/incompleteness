"""Controls of design r6 amendment 3 (general multi-path reconciliation) on the engine's neutral in-memory trees:
RECON-MULTI, RECON-ENUM, RECON-CORPUS, RECON-CONFLICT, RECON-CATEGORY, RECON-SCI, RECON-BLOCK, RECON-TRIAL and
RECON-OVERLAP and RECON-RETAINED.

Each case is one in-process op C main-role stage (engine/execution.py) over commits built in memory: the pin H, a
candidate X carrying the ledger's splices, a main commit M, and reconciliation records drafted by the engine from those
objects (oi-reconciliation/2) with the writer's scientific effect. The stage's items, side changes and dispositions are
retained as the case's result. Cases the tool revision cannot evaluate yet are not built and are named in the record;
their rows record FAIL.
"""
import copy
from types import SimpleNamespace

from ledger_coverage.engine import controls_engine as ce, execution as exmod, reconcile as rcmod, schema, util
from ledger_coverage.engine.gitobj import Overlay
from ledger_coverage.adapters import control_records

EFFECT = {'conclusions': 'none', 'assessment': 'control fixture: the change on main touches no planned edit',
          'method': 'control: every condition recomputed from git objects', 'verdict': 'no-effect'}
A = ce.doc_path            # notes/a.md, ledgered
B = ce.other_path          # notes/b.md, ledgered
C_PATH = 'notes/c.md'      # a corpus path the ledger does not list
B_TEXT = ('# heading two\n\nzero row one stands here.\n\nomega row two stands here.\n\nfinal row three.\n')
C_TEXT = '# heading three\n\nplain corpus text.\n'


class World:
    def __init__(self, a_text=ce.base_text, b_text=B_TEXT, two=True, three=False, earlier=None):
        self.w = ce.World(earlier if earlier is not None else a_text,
                          extra={B: b_text.encode(), C_PATH: C_TEXT.encode()})
        self.repo = self.w.repo
        self.H = self.w.pin if earlier is None else self.w.child(self.w.pin, a_text, subject='scientific base')
        self.a_text, self.b_text = a_text, b_text
        sa = a_text.index('beta line two')
        sps = [(A, sa, sa + len('beta line two'), 'beta line second')]
        if two:
            sb = b_text.index('omega row two')
            sps.append((B, sb, sb + len('omega row two'), 'omega row second'))
        if three:
            sc = C_TEXT.index('plain corpus')
            sps.append((C_PATH, sc, sc + len('plain corpus'), 'plain ledgered'))
        self.led = ce.ledger(self.H, sps, self.repo)
        # the ledger's edit list: one entry per splice, so a scientific effect can name an edit id
        self.led['raw']['edits'] = [{'id': s['id'], 'file': s['file'], 'new': s['new']} for s in self.led['splices']]
        ch = {}
        for sp in self.led['splices']:
            data = self.repo.read(self.H, sp['file'])
            ch[sp['file']] = data[:sp['start']] + sp['new_bytes'] + data[sp['end']:]
        self.X = self.repo.derive(self.H, ch, parents=[self.H], subject='candidate')
        self.ctx = self.w.ctx()

    def main(self, changes):
        ch = {}
        for path, (old, new) in changes.items():
            data = self.repo.read(self.H, path).decode()
            assert old in data, (path, old)
            ch[path] = data.replace(old, new, 1).encode()
        return self.repo.derive(self.H, ch, parents=[self.H], subject='main')

    def record(self, M, path, effect=None):
        return rcmod.draft(self.repo, self.ctx, self.H, M, self.X, self.led, path,
                           scientific_effect=copy.deepcopy(effect or EFFECT))

    def retain(self, text, line):
        site = '%s:%d@%s' % (A, line, self.w.pin[:8])
        self.ctx.sitemap['sites'].append({'site_id': site, 'file': A, 'pin_line': line})
        self.led['retained'] = [{'id': 'retained-fixture', 'site_ref': site, 'file': A, 'text': text, 'identity': True}]

    def stage(self, M, records, cap, label):
        refs = []
        for i, r in enumerate(records):
            r = dict(r, _ref={'path': 'records/r%d.json' % i, 'blob_sha256': util.sha256(util.canonical(r))})
            refs.append(r)
        e = exmod.Execution(self.ctx, self.H, self.X, self.led, None, M, None, None, [], refs)
        e.candidate()
        e.main_role(set(self.led['files']) | set(self.ctx.corpus(M)))
        doc = control_records.stage_doc(e.items, operation='execution', side_changes=e.side_changes,
                                        dispositions=e.dispositions)
        cap.rec.capture_doc('op C main role (recon_controls.py): %s' % label, doc)
        return doc


def failed(doc, path):
    return sorted({c for x in doc.get('side_changes') or [] if x.get('path') == path
                   for ev in x.get('record_conditions') or [] for c in ev.get('failed') or []})


def disp(doc, path):
    return next((d for d in doc.get('dispositions') or [] if d.get('path') == path), None)


def classes(doc):
    return sorted({i['class'] for i in doc.get('items') or []})


def name_last(cap, case, **bindings):
    cap.rec.name_last(case, bindings=bindings)


def landing_controls(cap):
    """Run the six exact R6.TREE.12–13 fixtures through the builder and landing checker."""
    out = cap.result_map()
    path = 'p.md'
    base = b'alpha\nbeta\ngamma\n'
    old, replacement = b'beta\n', b'BETA\n'
    start = base.index(old)
    edited = base[:start] + replacement + base[start + len(old):]
    added = base + b'delta\n'
    moved = old + base[:start] + base[start + len(old):]
    extra = 'landing-extra-change'
    conflict = 'landing-conflict-unresolved'
    fixtures = (
        ('neither side changed', base, base, base, extra),
        ('only X/C changed', edited, base, edited, extra),
        ('only M changed', base, added, added, 'landing-drops-main-change'),
        ('both changed to equal blobs', edited, edited, edited, extra),
        ('both changed to different blobs, ledgered path (a line prepended on M)',
         edited, b'zero\n' + base, b'zero\n' + edited, conflict),
        ('both changed to different blobs, ledgered path (the spliced line moved on M)',
         edited, moved, replacement + moved[len(old):], conflict),
    )
    clean_case = 'landing check of L carrying exactly that blob'
    duplicate_case = 'M carrying the splice\'s old bytes twice (M[p.md] = "beta\\nalpha\\nbeta\\ngamma\\n"): no composition exists, any L'
    for index, (label, candidate, main, expected, adverse_class) in enumerate(fixtures, 1):
        repo = Overlay()
        H = repo.add_commit({path: base}, [], 'landing base')
        C = repo.add_commit({path: candidate}, [H], 'landing candidate')
        M = repo.add_commit({path: main}, [H], 'landing main')
        led = ce.ledger(H, [(path, start, start + len(old), replacement.decode())], repo)
        sp = led['splices'][0]
        splice = {k: sp[k] for k in ('id', 'start', 'end', 'old_sha256', 'new_sha256')}

        def retain(case, main_id, landing, builder=False, refusal=None):
            items, compositions = [], []
            if not builder:
                execution = exmod.Execution(SimpleNamespace(repo=repo), H, C, led, M=main_id, L=landing, C=C)
                execution.landing()
                items, compositions = execution.items, execution.compositions
            fixture = {'path': path, 'H': repo.read(H, path).decode(), 'C': repo.read(C, path).decode(),
                       'M': repo.read(main_id, path).decode(), 'splices': [splice]}
            cap.rec.capture_doc(
                'landing builder' if builder else 'execution landing checker',
                control_records.stage_doc(
                    items, operation='compose_landing' if builder else 'execution.landing', fixture=fixture,
                    splice_bytes=sp['new_bytes'].decode(), roles={'H': H, 'C': C, 'M': main_id, 'L': landing},
                    landing={'bytes': repo.read(landing, path).decode(), 'parents': repo.parents(landing),
                             'git_blob': repo.blob_id(landing, path), 'mode': repo.mode(landing, path)},
                    landing_compositions=compositions, builder_refusal=refusal),
                case=case)
            return items

        built = exmod.compose_landing(repo, H, M, C, led, repo)
        retain('builder: the landing blob of p.md composed from the fixture (%s)' % label, M, built, builder=True)
        clean = retain(clean_case, M, built)
        wrong = expected[:-1] + b'!' if index <= 4 else expected.replace(replacement, b'BETB\n')
        mutant = repo.derive(M, {path: wrong}, parents=[M, C], subject='adverse landing')
        text = wrong.decode().replace('\n', '\\n')
        adverse = retain('landing check of L carrying that blob with one byte changed (%s)' % text, M, mutant)
        passed = (repo.read(built, path) == expected and not clean and
                  [(i['subject'], i['class']) for i in adverse] == [(path, adverse_class)])
        if index == 5:
            twice = repo.add_commit({path: old + base}, [H], 'landing main')
            refusal = None
            try:
                exmod.compose_landing(repo, H, twice, C, led, repo)
            except ValueError as exc:
                refusal = str(exc)
            L = repo.derive(twice, {path: candidate}, parents=[twice, C], subject='adverse landing')
            bad = retain(duplicate_case, twice, L, refusal=refusal)
            passed = passed and refusal is not None and [(i['subject'], i['class']) for i in bad] == [(path, conflict)]
        out['LC-%d' % index] = passed
    return out


def recon_controls(cap):
    out = cap.result_map()
    w = World()
    M = w.main({A: ('epsilon closing line.', 'epsilon closing line, edited on main.'),
                B: ('final row three.', 'final row three, edited on main.')})
    ra, rb = w.record(M, A), w.record(M, B)

    # RECON-MULTI
    d1 = w.stage(M, [ra, rb], cap, 'two records')
    name_last(cap, MULTI[0])
    one = dict(ra, paths=ra['paths'] + rb['paths'])
    d2 = w.stage(M, [one], cap, 'one record with two entries')
    name_last(cap, MULTI[1])
    d3 = w.stage(M, [ra], cap, 'second record removed')
    name_last(cap, MULTI[2])
    rb_bad = copy.deepcopy(rb)
    rb_bad['paths'][0]['m'] = '0' * 40
    d4 = w.stage(M, [ra, rb_bad], cap, 'second record failing RC2')
    name_last(cap, MULTI[3])
    M5 = w.repo.derive(M, {'misc/unclassified.txt': b'side\n'}, parents=[M], subject='unclassified side change')
    ra5, rb5 = w.record(M5, A), w.record(M5, B)
    d5 = w.stage(M5, [ra5, rb5], cap, 'unclassified non-corpus path')
    name_last(cap, MULTI[4])
    ok = not ({'base-drift', 'record-invalid'} & set(classes(d1) + classes(d2))) and \
        'RC10' in failed(d3, A) and 'base-drift' in classes(d3) and \
        'RC2' in failed(d4, B) and 'RC10' in failed(d4, A) and 'RC11' in failed(d5, A)
    out['RECON-MULTI'] = ok
    out['_RECON-MULTI'] = [classes(d) for d in (d1, d2, d3, d4, d5)]

    # RECON-ENUM
    w3 = World(three=True)
    M3 = w3.main({A: ('epsilon closing line.', 'epsilon edited.'), B: ('final row three.', 'final edited.'),
                  C_PATH: ('# heading three', '# heading three, edited')})
    e1 = w3.stage(M3, [w3.record(M3, A), w3.record(M3, B)], cap, 'three drifted paths, two covered')
    name_last(cap, ENUM[0], uncovered_path=C_PATH)
    paths = sorted(d['path'] for d in e1['dispositions'])
    missing = dict(e1, dispositions=[d for d in e1['dispositions'] if d['path'] != C_PATH])
    extra = dict(e1, dispositions=e1['dispositions'] + [{'path': 'notes/unchanged.md', 'disposition': 'reconciled'}])
    p1, p2 = schema.disposition_problems(missing), schema.disposition_problems(extra)
    for case, probs in ((ENUM[1], p1), (ENUM[2], p2)):
        cap.rec.capture_doc('schema check of a mutated result (recon_controls.py)',
                            {'operation': 'schema check', 'schema_errors': probs, 'exit_status': None},
                            case=case, attested={'outcome': 'PREDICATE', 'schema_errors': probs})
    kinds = sorted((d['path'], d['disposition'], bool(d.get('record')), d.get('why')) for d in e1['dispositions'])
    listed_ok = kinds == [(A, 'reconciled', True, None), (B, 'reconciled', True, None),
                          (C_PATH, 'base-drift', False, 'no admitted record covers the path')]
    ok = listed_ok and 'missing disposition' in p1 and 'disposition for an unchanged path' in p2
    cap.attest(ENUM[0], {'equals': ENUM_EQUALS} if listed_ok else {})
    out['RECON-ENUM'] = ok
    out['_RECON-ENUM'] = {'dispositions': kinds, 'missing': p1, 'extra': p2}

    # RECON-CORPUS
    w4 = World()
    M4 = w4.main({C_PATH: ('plain corpus text.', 'plain corpus text, edited on main.')})
    rc_ = w4.record(M4, C_PATH)
    c1 = w4.stage(M4, [rc_], cap, 'corpus entry')
    name_last(cap, CORPUS[0])
    res = [c1]
    for case, mut in ((CORPUS[1], lambda e: e.update(l='0' * 40)), (CORPUS[2], lambda e: e.update(x='0' * 40)),
                      (CORPUS[3], lambda e: e['ledger_binding'].update(files_entry_sha256='0' * 64))):
        r2 = copy.deepcopy(rc_)
        mut(r2['paths'][0])
        res.append(w4.stage(M4, [r2], cap, case))
        name_last(cap, case)
    res.append(w4.stage(M4, [], cap, 'no record'))
    name_last(cap, CORPUS[4])
    ok = not ({'base-drift', 'record-invalid'} & set(classes(c1))) and 'RC7' in failed(res[1], C_PATH) and \
        'RC8' in failed(res[2], C_PATH) and 'RC13' in failed(res[3], C_PATH) and 'base-drift' in classes(res[4])
    out['RECON-CORPUS'] = ok
    out['_RECON-CORPUS'] = [failed(d, C_PATH) for d in res]

    # RECON-CONFLICT
    w5 = World(two=False)
    w5.retain('alpha line one', 3)
    restored_M = w5.main({A: ('epsilon closing line.', 'epsilon closing line, edited on main.')})
    base_rec = w5.record(restored_M, A)
    cases = []

    def conflict(case, M_):
        r_ = w5.record(M_, A) or base_rec
        d_ = w5.stage(M_, [r_], cap, case)
        name_last(cap, case)
        cases.append((case, d_))
    conflict(CONFLICT[0], w5.main({A: ('beta line two stands here.', 'beta line two stands there.')}))
    ws = World(a_text=SENT_TEXT, two=False)
    Ms = ws.main({A: ('here, continued.', 'here, continued anew.')})
    d_s = ws.stage(Ms, [ws.record(Ms, A) or ws.record(ws.main({}), A)], cap, CONFLICT[1])
    name_last(cap, CONFLICT[1])
    cases.append((CONFLICT[1], d_s))
    conflict(CONFLICT[2], w5.main({A: ('alpha line one stands here.', 'alpha line one stands there.')}))
    conflict(CONFLICT[3], w5.main({A: ('epsilon closing line.', 'epsilon closing line.\n\nbeta line two stands here.')}))
    conflict(CONFLICT[4], w5.main({A: ('beta line two stands here.',
                                       'beta LINE 2 stands here.\n\nbeta line two elsewhere.')}))
    w5.stage(restored_M, [base_rec], cap, 'restored')
    name_last(cap, 'restored')
    out['RECON-CONFLICT'] = all('RC14' in failed(d_, A) and 'base-drift' in classes(d_) for _c, d_ in cases)
    out['_RECON-CONFLICT'] = {'failed': {c: failed(d_, A) for c, d_ in cases}}

    # RECON-RETAINED: a whole line at H, a multiline window, and a site whose earlier pin_line moved.
    second_line = World(two=False)
    second_line.retain('gamma line three stands here.\n\ndelta line four', 7)
    moved = World(a_text='Moved preface.\n\n' + ce.base_text, two=False, earlier=ce.base_text)
    moved.retain('alpha line one', 3)
    retained_cases = [
        (w5, w5.main({A: ('alpha line one stands here.', 'alpha line one stands there.')})),
        (w5, w5.main({A: ('epsilon closing line.', 'epsilon closing line.\n\nalpha line one stands here.')})),
        (second_line, second_line.main({A: ('delta line four stands here.', 'delta line four stands there.')})),
        (moved, moved.main({A: ('epsilon closing line.', 'epsilon edited.')})),
        (w5, restored_M),
    ]
    retained_results = []
    for caption, (world, main) in zip(RETAINED, retained_cases):
        rec = world.record(main, A)
        retained_results.append(world.stage(main, [rec], cap, caption))
        name_last(cap, caption)
    adverse = retained_results[:3]
    clean = retained_results[3:]
    out['RECON-RETAINED'] = all('RC14' in failed(doc, A) and 'base-drift' in classes(doc) and
                                (disp(doc, A) or {}).get('category') == 2 for doc in adverse) and \
        all(not {'base-drift', 'record-invalid'} & set(classes(doc)) for doc in clean)
    out['_RECON-RETAINED'] = [failed(doc, A) for doc in retained_results]

    # RECON-CATEGORY (both directions)
    k1 = w5.stage(restored_M, [base_rec], cap, 'category 1')
    name_last(cap, CATEGORY[0])
    Mk2 = w5.main({A: ('beta line two stands here.', 'beta line two stands there.')})
    k2 = w5.stage(Mk2, [w5.record(Mk2, A) or base_rec], cap, 'category 2 window')
    name_last(cap, CATEGORY[1])
    Mk3 = w5.main({A: ('beta line two', 'beta line deux')})
    k3 = w5.stage(Mk3, [base_rec], cap, 'category 2 span')
    name_last(cap, CATEGORY[2])
    d_k1 = disp(k1, A) or {}
    ok = d_k1.get('disposition') == 'reconciled' and d_k1.get('category') == 1 and \
        'RC14' in failed(k2, A) and (disp(k2, A) or {}).get('category') == 2 and \
        'RC4' in failed(k3, A) and 'RC14' in failed(k3, A) and (disp(k3, A) or {}).get('category') == 2
    cap.attest(CATEGORY[0], {'equals': "the path's disposition is reconciled, category 1"}
               if d_k1.get('category') == 1 and d_k1.get('disposition') == 'reconciled' else {})
    out['RECON-CATEGORY'] = ok

    # RECON-SCI runs as op C runs through the post-freeze route in postfreeze_controls.py

    # RECON-TRIAL and RECON-OVERLAP need the reconciled-state trial and resolutions, which this tool revision does
    # not implement yet: recorded FAIL with no evidence. RECON-BLOCK runs as op C runs in postfreeze_controls.py.
    out['RECON-TRIAL'] = False
    out['RECON-OVERLAP'] = False
    return out


SENT_TEXT = ('# heading one\n\nalpha line one stands here.\n\nbeta line two stands\nhere, continued.\n\n'
             'gamma line three stands here.\n')
MULTI = ['two ledgered paths in two files changed on M, each covered by its own reviewed reconciliation record bound to '
         'the run, every condition RC1-RC14 holding for each (positive)',
         'the same two paths covered by one reviewed record with two path entries, each with its own ledger_binding '
         '(positive)',
         'countercase: the same run with the second record removed',
         "countercase: the second record failing RC2 (its m differs from the path's blob at M)",
         'countercase: an unledgered non-corpus path changed on M left unclassified']
ENUM = ['three ledgered paths changed on M, two covered by applying records and one by none',
        'countercase: the same result with one disposition removed',
        'countercase: the same result with a disposition for a path that does not differ between H and M']
ENUM_EQUALS = ('the result lists exactly one disposition for each path that differs between H and M and is ledgered '
               'or corpus: two reconciled, each naming its record, and one base-drift naming that no admitted record '
               'covers it; no other path has one')
CORPUS = ["a corpus path the ledger does not list, changed on M, covered by a reviewed record entry with no splices, l "
          "equal to m, x equal to the path's blob at H, and null ledger_binding values (positive)",
          'countercase: the same entry with l differing from m',
          "countercase: the same entry with x differing from the path's blob at H",
          'countercase: the same entry with a non-null ledger_binding value',
          'countercase: the same path with no record']
RETAINED = ["M changes a byte of the line holding a retained edit's text at H",
            "M adds a second copy of a retained site's line elsewhere in the file",
            "a retained edit whose text spans two lines; M changes a byte of the second line",
            "a retained site that moved between E and H (its site-map pin_line differs from its line at H), M not "
            "touching its line: the line at H is found from the retained text, with no E..H walk (positive)",
            "countercase: M changes bytes outside every context window and every retained site's line (positive)"]
CONFLICT = ["M changes a byte of the line holding a splice, outside the splice's span",
            "M changes a byte of a sentence (splitter version 2) that overlaps a splice's span, on another line",
            'M changes the line of a retained site of the path',
            "M adds a second copy of a splice's context window elsewhere in the file",
            "M changes the bytes of a splice's span and the old bytes occur once elsewhere at M"]
CATEGORY = ['a drifted ledgered path whose changes on M lie outside every context window and retained-site line, covered '
            'by an applying entry (positive: category 1, mechanical)',
            "countercase: the same path with a change on M inside a splice's context window and no resolution (category "
            "2, unresolved)",
            "countercase: the same path with a change on M to a splice's span, so that its old bytes do not occur at M "
            "(category 2, unresolved)"]
SCI = ['a path entry without scientific_effect',
       'a scientific_effect whose conclusions name an id that is no edit id of the ledger',
       'a scientific_effect with an empty assessment or method',
       "a review record whose verdicts do not cover the entry's scientific_effect item, or do not accept it",
       "a review record whose reviewer equals the record's author",
       "a scientific_effect without verdict, or with verdict invalidates and no invalidated edit id, or an invalidated "
       "sha256 that differs from the edit-list entry's",
       "an executed path's entry whose method names no check re-run at the composed blob"]
