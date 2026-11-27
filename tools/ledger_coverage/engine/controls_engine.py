"""Engine controls on neutral in-memory trees (sec. 10.1; engine parts of sec. 10.2 and 13).

Each control runs in both directions where the design asks for it: the mutant gives the stated outcome and the
restored tree gives the control outcome. The texts are neutral; no retirement constant appears here (Z9).
"""
import traceback

from . import context as ctxmod
from . import execution as exmod
from . import outcome as oc
from . import pipeline as pl
from . import profiles as pr
from . import records as rec
from . import rules as rulemod
from . import reconcile as rcmod
from . import util
from .gitobj import Overlay

# A control runner may set capture_hook to an object with `result_map()` (a dict that binds each control id to the stage
# results captured before its assignment) and `stage(label, items, **facts)`. Unset (the self-test and the
# preflight), the controls run unchanged.
capture_hook = None


def _out():
    return capture_hook.result_map() if capture_hook is not None else {}


def _stage(label, items, **facts):
    if capture_hook is not None:
        capture_hook.stage(label, items, **facts)
    return items


def _stage_stop(label, stop):
    """Captures a stage that ended in oc.Stop (its outcome and stop class)."""
    if capture_hook is not None:
        capture_hook.stage(label, [], stop=stop)


def _restore_with(fn, label):
    """The restored case: the same stage on the unmutated input (`fn` runs it and returns its items or raises),
    against a clean run of the same stage."""
    if capture_hook is None:
        return
    for name in ('baseline', 'restored'):
        before = capture_hook.count()
        try:
            got = fn()
            if capture_hook.count() == before:
                _stage(label, got or [])
        except oc.Stop as s:
            _stage_stop(label, s)
        _case(name, baseline='baseline' if name == 'restored' else None)


def _bind_first(**bindings):
    """Binds the first unnamed stage result of the control being computed as its case '' (its row's case)."""
    if capture_hook is not None:
        capture_hook.bind_first(bindings)


def _case(name, baseline=None, **bindings):
    """Names the last captured stage result as the expectation case `name`, with its bindings; `baseline` names the
    earlier case a restored case is compared with."""
    if capture_hook is not None:
        capture_hook.name_last(name, bindings, baseline)

doc_path = 'notes/a.md'
other_path = 'notes/b.md'
base_text = ('# heading one\n\nalpha line one stands here.\n\nbeta line two stands here.\n\n'
             'gamma line three stands here.\n\ndelta line four stands here.\n\nepsilon closing line.\n')
neutral_ind = {
    'strip': [r'^\s*(?:>\s*)*(?:#{1,6}\s+)?(?:(?:[-+*]|\d+[.)])\s+)?[_*]*'],
    'definitions': [{'name': 'ana', 'on': 'stripped', 'effect': 'meaning', 'patterns': [r'^(This)\b']},
                    {'name': 'lst', 'on': 'line', 'effect': 'structure-list', 'patterns': [r'^\s*([-*+]|\d+[.)])\s+']},
                    {'name': 'tbl', 'on': 'line', 'effect': 'structure-table', 'patterns': [r'^ *\|']},
                    {'name': 'prt', 'on': 'quote', 'effect': 'info'}],
    'list_item_patterns': [r'^\s*([-*+]|\d+[.)])\s+'], 'table_row_pattern': r'^ *\|', 'caption_prefixes': [';; '],
}


def neutral_profiles():
    rv = pr.Profile({'name': 'np-review', 'kind': 'review', 'applies_to': 'tree',
                     'source': {'extractor': {'kind': 'json-pointer'}}}, [r'\bzeta\b'])
    dn = pr.Profile({'name': 'np-deny', 'kind': 'deny', 'applies_to': 'tree', 'levels': ['line', 'sentence'],
                     'source': {'extractor': {'kind': 'json-pointer'}}}, [r'\bzeta\s+holds\b'])
    return {'np-review': rv, 'np-deny': dn}


class World:
    """A neutral in-memory repository with a pin, sites and a configuration."""

    def __init__(self, text=base_text, sites=None, extra=None, mapping=None):
        self.repo = Overlay(None)
        self.text = text
        files = {doc_path: text.encode()}
        files.update(extra or {})
        self.pin = self.repo.add_commit(files, [], 'pin')
        self.cfg = {'roles': {'pin': self.pin, 'scientific_base': self.pin}, 'corpus': {'patterns': [r'^notes/[^/]+\.md$']},
                    'sentence': {'abbreviations': ['zz.'], 'splitter_version': 2},
                    'context_mapping': mapping or {'values': {'sd': True, 'sr': False}, 'default': 'invalid'},
                    'checks': [{'id': 'nc', 'profiles': ['np-review'], 'final_profiles': ['np-review']}]}
        lines = util.lines_of(text)
        if sites is None:
            sites = [(i + 1, 'sr') for i, l in enumerate(lines) if 'line' in l]
        self.sitemap = {'sites': [{'file': doc_path, 'line': ln, 'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'},
                                   'context_field_value': v, 'quote': None} for ln, v in sites]}

    def ctx(self, allow=()):
        c = pl.RunContext(self.repo, self.cfg, neutral_profiles(), list(allow), {},
                          ctxmod.Indicators(neutral_ind), sitemap=self.sitemap)
        return c

    def child(self, parent, text=None, files=None, subject='child'):
        ch = dict(files or {})
        if text is not None:
            ch[doc_path] = text.encode()
        return self.repo.derive(parent, ch, parents=[parent], subject=subject)

    def coverage(self, commit, segs, adj=None, hits=True, allow=()):
        ctx = self.ctx(allow)
        cv = pl.Coverage(ctx, commit, segs, ctx.cfg if False else None, adj or {}, []).run()
        items = list(cv.items)
        if hits:
            tm = pl.Terms(ctx, commit, [ctx.profiles['np-review']], [ctx.profiles['np-deny']])
            tm.deny()
            tm.review(held=pl.held_lines(cv.states))
            items += tm.items
        if capture_hook is not None:
            from .cli import site_state
            sites = [dict(v, state=site_state(v)) for k, v in sorted(cv.site_out.items())]
            counts = {}
            for x in sites:
                counts[x['state']] = counts.get(x['state'], 0) + 1
            _stage('coverage', items, sites=sites, site_counts=counts)
        return cv, items


# the second direction of design r6 OBL-20
def _restore(w, hits=True):
    """The restored case of an unledgered mutation, captured only by a control runner: the same coverage run over an
    identity segment from the pin to the unmutated tree, compared with the clean run on the pin."""
    if capture_hook is None:
        return
    w.coverage(w.pin, [], hits=hits)
    _case('baseline')
    r = w.child(w.pin, w.text, subject='restored')
    w.coverage(r, [seg(w.pin, r)], hits=hits)
    _case('restored', baseline='baseline')


def _restore_ledgered(w, clean, led):
    """The restored case of a mutation of a ledgered tree: the same coverage run on the tree that carries exactly
    the ledger's splices, compared with the clean run on that tree."""
    if capture_hook is None:
        return
    w.coverage(clean, [seg(w.pin, clean, 'ledgered', ledger=led)])
    _case('baseline')
    w.coverage(clean, [seg(w.pin, clean, 'ledgered', ledger=led)])
    _case('restored', baseline='baseline')


def _capture_site_case(name, coverage, items, site, **bindings):
    if capture_hook is None:
        return
    from .cli import site_state
    selected = coverage.site_out[site]
    _stage('coverage of the named site', [i for i in items if i['subject'] == site],
           sites=[dict(selected, state=site_state(selected))])
    _case(name, **bindings)


def seg(f, t, kind='unledgered', **kw):
    d = {'from': f, 'to': t, 'kind': kind}
    d.update(kw)
    return d


def ledger(base, splices, repo):
    out = {'base': base, 'splices': [], 'files': {}, 'retained': [], 'mirrors': [], 'edits': []}
    for i, (path, a, b, new) in enumerate(splices):
        data = repo.read(base, path)
        out['splices'].append({'id': 'S%d' % (i + 1), 'file': path, 'start': a, 'end': b,
                               'old_sha256': util.sha256(data[a:b]), 'new': new, 'new_bytes': new.encode(),
                               'new_sha256': util.sha256(new.encode())})
        out['files'][path] = {'base_sha256': util.sha256(data)}
    from . import segments as sgm
    for path in out['files']:
        out['files'][path]['expected_sha256'] = util.sha256(sgm.apply_splices(
            repo.read(base, path), [s for s in out['splices'] if s['file'] == path]))
    out['raw'] = {'files': out['files'], 'splices': [{k: v for k, v in s.items() if k != 'new_bytes'}
                                                     for s in out['splices']], 'edits': []}
    return out


def classes(items):
    return sorted({i['class'] for i in items})


def decision(items):
    return oc.compute([], None, items)


def off(text, needle):
    return text.encode().index(needle.encode())


# ---- controls ----------------------------------------------------------------------------------------------

def u_controls():
    out = _out()
    w = World()
    cv, it = w.coverage(w.pin, [])
    _restore(w)
    out['U1'] = decision(it) == oc.pass_ and all(not s['statuses'] for s in cv.site_out.values())
    x = w.child(w.pin, 'new one\nnew two\nnew three\n' + base_text)
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _bind_first(subject='%s:3@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['U2'] = decision(it) == oc.pass_ and all(s['statuses'][-1]['status'] == 'moved' for s in cv.site_out.values())
    led = ledger(w.pin, [(doc_path, 0, 0, 'new one\nnew two\nnew three\n')], w.repo)
    x = w.child(w.pin, 'new one\nnew two\nnew three\n' + base_text)
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _bind_first(subject='%s:3@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['U3'] = decision(it) == oc.pass_ and all(s['statuses'][-1]['status'] == 'moved' for s in cv.site_out.values())
    x = w.child(w.pin, base_text.replace('beta line two', 'beta line deux'))
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _restore(w)
    out['U4'] = classes(it) == ['unauthorized-change']
    x = w.child(w.pin, base_text + '\nbeta line two stands here.\n')
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _restore(w)
    out['U5'] = classes(it) == ['duplicated']
    dup = '# h\n\nfirst ctx\nsame line here\nend one\n\nsecond ctx\nsame line here\nend two\n'
    w6 = World(dup, sites=[(4, 'sr'), (8, 'sr')])
    x = w6.child(w6.pin, 'top\n' + dup)
    cv, it = w6.coverage(x, [seg(w6.pin, x)], hits=False)
    _restore(w6, hits=False)
    out['U6'] = decision(it) == oc.pass_
    swapped = '# h\n\nsecond ctx\nsame line here\nend two\n\nfirst ctx\nsame line here\nend one\n'
    x = w6.child(w6.pin, swapped)
    cv, it = w6.coverage(x, [seg(w6.pin, x)], hits=False)
    _restore(w6, hits=False)
    out['U7'] = 'ambiguous' in classes(it)
    x = w.child(w.pin, base_text.replace('beta line two stands here.\n', ''))
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _restore(w)
    out['U8'] = classes(it) == ['missing']
    x = w.child(w.pin, base_text.replace('beta line two', 'beta  line two'))
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _bind_first(subject='%s:5@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['U9'] = classes(it) == ['unauthorized-change'] and it[0]['detail'].get('whitespace_only') is True
    a = off(base_text, 'beta line two')
    led = ledger(w.pin, [(doc_path, a, a + len('beta line two'), 'beta line second')], w.repo)
    x = w.child(w.pin, base_text.replace('beta line two', 'beta line second'))
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    st = [s['statuses'][-1] for s in cv.site_out.values() if s['statuses'][-1]['status'] == 'authorized-replacement']
    _bind_first(subject='%s:5@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['U10'] = decision(it) == oc.pass_ and len(st) == 1 and st[0]['splice_ids'] == ['S1']
    b = a + len('beta line two stands here.\n')
    led = ledger(w.pin, [(doc_path, a, b, '')], w.repo)
    x = w.child(w.pin, base_text.replace('beta line two stands here.\n', ''))
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _bind_first(subject='%s:5@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['U11'] = decision(it) == oc.pass_ and any(s['statuses'][-1]['status'] == 'authorized-removal'
                                                  for s in cv.site_out.values())
    x = w.child(w.pin, base_text + '\nzeta appears on a new line.\n')
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _restore(w)
    out['U12'] = decision(it) == oc.review and classes(it) == ['unclassified']
    # U13 is retired with the `read` route (DESIGN-r6.md sec. 33); U15 is U14's wrong-region-hash case
    u14, u15 = hp_adjudication_pair()
    out['U14'] = u14 and u15
    return out


def hp_world(two_steps=False, foreign=False, shared=False):
    """pin -> m1 (changes a site) [-> m2] = H, with merges named in the obligation."""
    text = base_text
    if shared:
        text = '# h\n\nanchor above.\n\nfirst shared line.\n\nsecond shared line.\n\nanchor below.\n'
    w = World(text, sites=[(5, 'sr'), (7, 'sr')] if shared else None)
    t1 = text.replace('beta line two', 'beta line revised') if not shared else \
        text.replace('first shared line.\n\nsecond shared line.', 'first merged line.\n\nsecond merged line.')
    m1 = w.child(w.pin, t1, subject='merge one')
    h = m1
    if two_steps:
        h = w.child(m1, t1.replace('beta line revised', 'beta line twice revised'), subject='merge two')
    merges = {m1, h}
    if foreign:
        merges = {w.pin}
    chain = [m1] + ([h] if h != m1 else [])
    par = {m1: w.pin}
    if h != m1:
        par[h] = m1
    s = seg(w.pin, h, 'hp', chain=chain, parent_of=par, merges=merges, obligation='HP')
    return w, h, s


def walk_steps(w, h, s, site_line):
    sts = []
    ctx = w.ctx()
    st_lines = ctx.ft(w.pin, doc_path).lines
    from . import segments as sg
    status, steps, region, det = sg.walk_region(w.repo, s['chain'], s['parent_of'], doc_path,
                                                [st_lines[site_line - 1]], lambda c, p: ctx.ft(c, p))
    return [{k: v for k, v in x.items() if k != 'post'} for x in steps]


def hp_adjudication_pair():
    w, h, s = hp_world()
    sid = '%s:%d@%s' % (doc_path, 5, w.pin[:8])
    steps = walk_steps(w, h, s, 5)
    good = {'site_id': sid, 'steps': steps, 'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'},
            'semantic_classification': 'stated', 'author': 'eng-writer'}
    cv, it = w.coverage(h, [s], adj={'hp': [good]}, hits=False)
    pos = 'a provenance adjudication matching the walk for a changed HP site (positive)'
    _case(pos, site=sid)
    u14 = not [i for i in it if i['subject'] == sid]
    # the restored case: the control's own positive case run again (DESIGN-r6.md, U14 `restored`)
    cv_r, it_r = w.coverage(h, [s], adj={'hp': [good]}, hits=False)
    _case('restored', baseline=pos, site=sid)
    bad = dict(good, steps=[dict(steps[0], post_sha256=util.sha256('other'))])
    cv, it = w.coverage(h, [s], adj={'hp': [bad]}, hits=False)
    _case('the same adjudication with a wrong region hash (the v1 U15 case)', site=sid)
    u15 = [i['class'] for i in it if i['subject'] == sid] == ['provenance-mismatch']
    return u14, u15


def m_controls():
    out = _out()
    w = World()
    a = off(base_text, 'beta line two')
    led = ledger(w.pin, [(doc_path, a, a + 4, 'betax')], w.repo)
    good = base_text.replace('beta line two', 'betax line two', 1)
    x = w.child(w.pin, good.replace('epsilon closing', 'epsilon finishing'))
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    x0 = w.child(w.pin, good)
    cv0, it0 = w.coverage(x0, [seg(w.pin, x0, 'ledgered', ledger=led)])
    _case('restored')
    out['M1'] = 'unauthorized-edit' in classes(it) and decision(it0) == oc.pass_
    x = w.child(w.pin, base_text.replace('beta line two', 'betay line two', 1))
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _restore_ledgered(w, x0, led)
    out['M2'] = 'unauthorized-edit' in classes(it)

    def integ(mut):
        l2 = {k: (list(v) if isinstance(v, list) else v) for k, v in led.items()}
        l2['splices'] = [dict(sp) for sp in led['splices']]
        mut(l2)
        try:
            pl.check_ledger(w.repo, w.pin, l2)
            _stage('ledger integrity', [])
            return None
        except oc.Stop as s:
            _stage_stop('ledger integrity', s)
            return s.cls

    def clean_integ():
        integ(lambda l: None)
        return None
    m3 = integ(lambda l: l['splices'][0].update(old_sha256=util.sha256('z')))
    m3c = integ(lambda l: None)
    _restore_with(clean_integ, 'ledger integrity')
    out['M3'] = m3 == 'LEDGER_INTEGRITY' and m3c is None
    m4 = integ(lambda l: l['splices'][0].update(start=a + 1, end=a + 5))
    _restore_with(clean_integ, 'ledger integrity')
    out['M4'] = m4 == 'LEDGER_INTEGRITY'
    m5 = integ(lambda l: l.update(base=x0))
    _restore_with(clean_integ, 'ledger integrity')
    out['M5'] = m5 == 'SCIENTIFIC_BASE_MISMATCH'
    x = w.child(w.pin, base_text.replace('beta line two stands here.\n', ''),
                files={other_path: b'beta line two stands here.\n'})
    cv, it = w.coverage(x, [seg(w.pin, x)])
    _restore(w)
    out['M6'] = classes(it) == ['missing']
    x = w.child(w.pin, base_text.replace('beta line two', 'beta line\rtwo'))
    try:
        w.coverage(x, [seg(w.pin, x)])
        m11 = False
    except util.EncodingFault as exc:
        # the entry point turns the fault into ERROR ENCODING (cli.run)
        _stage_stop('coverage', oc.Stop(oc.error, 'ENCODING', str(exc)))
        m11 = True
    _restore(w)
    out['M11'] = m11
    return out


def k_controls():
    out = _out()
    w = World(sites=[(3, 'sd'), (7, 'sr')])
    x = w.child(w.pin, base_text.replace('beta line two stands here.', 'beta line two does not stand.'),
                files={})
    cv, it = w.coverage(x, [seg(w.pin, x)], hits=False)
    sd = '%s:3@%s' % (doc_path, w.pin[:8])
    sr = '%s:7@%s' % (doc_path, w.pin[:8])
    _restore(w, hits=False)
    out['K1'] = [i['class'] for i in it if i['subject'] == sd] == ['context-meaning-unverified']
    # K10: the positive direction of K1, with a matching context adjudication (sec. 4.1 row 2)
    sg0 = cv.segments[0]
    from_ctx = sg0['ctx_from'][sd][0]
    xl = w.ctx().ft(x, doc_path).lines
    to_ctx = util.context_hash_block(xl, 2, 3)
    adj = {'context': [{'site_id': sd, 'segment': sg0['name'], 'from_context_sha256': from_ctx,
                        'to_context_sha256': to_ctx}]}
    cv10, it10 = w.coverage(x, [seg(w.pin, x)], adj=adj, hits=False)
    _restore(w, hits=False)
    out['K10'] = not [i for i in it10 if i['subject'] == sd] and decision(it10) == oc.pass_
    _capture_site_case('', cv, it, sr, subject=sr)
    _restore(w, hits=False)
    out['K2'] = not [i for i in it if i['subject'] == sr] and cv.site_out[sr]['context_changed'] is True
    sw = base_text.replace('alpha line one stands here.\n\nbeta line two stands here.\n\ngamma line three stands here.',
                           'gamma line three stands here.\n\nbeta line two stands here.\n\nalpha line one stands here.')
    x = w.child(w.pin, sw)
    cv, it = w.coverage(x, [seg(w.pin, x)], hits=False)
    _capture_site_case('required site', cv, it, sd, subject_required=sd)
    _capture_site_case('non-required site', cv, it, sr, subject_nonrequired=sr)
    _restore(w, hits=False)
    out['K3'] = [i['class'] for i in it if i['subject'] == sd] == ['context-meaning-unverified'] and \
        not [i for i in it if i['subject'] == sr]
    mv = base_text.replace('alpha line one stands here.\n\n', '') + '\nfar away.\n\nalpha line one stands here.\n'
    x = w.child(w.pin, mv)
    cv, it = w.coverage(x, [seg(w.pin, x)], hits=False)
    _capture_site_case('required site', cv, it, sd, subject_required=sd)
    _capture_site_case('non-required site', cv, it, sr, subject_nonrequired=sr)
    _restore(w, hits=False)
    out['K4'] = [i['class'] for i in it if i['subject'] == sd] == ['context-meaning-unverified']
    at = '# h\n\nlead sentence here.\nThis bound holds below.\n\nother text.\n'
    w5 = World(at, sites=[(4, 'sr')])
    x = w5.child(w5.pin, at.replace('lead sentence here.', 'lead sentence changed.'))
    cv, it = w5.coverage(x, [seg(w5.pin, x)], hits=False)
    _restore(w5, hits=False)
    out['K5'] = classes(it) == ['context-meaning-unverified']
    lt = '# h\n\nlead-in sentence:\n\n- item one here\n- item two here\n\ntrailer paragraph.\n'
    w6 = World(lt, sites=[(5, 'sr')])
    x = w6.child(w6.pin, lt.replace('lead-in sentence:', 'lead-in changed:'))
    cv, it = w6.coverage(x, [seg(w6.pin, x)], hits=False)
    _restore(w6, hits=False)
    out['K6'] = classes(it) == ['context-structure-changed'] and decision(it) == oc.review
    tt = '# h\n\n| head a | head b |\n|---|---|\n| row one | v |\n| row two | v |\n\nafter.\n'
    w7 = World(tt, sites=[(6, 'sr')])
    x = w7.child(w7.pin, tt.replace('| head a | head b |', '| head x | head b |'))
    cv, it = w7.coverage(x, [seg(w7.pin, x)], hits=False)
    _case('header row changed')
    k7a = classes(it) == ['context-structure-changed']
    x = w7.child(w7.pin, tt.replace('| row one | v |', '| row uno | v |'))
    cv, it = w7.coverage(x, [seg(w7.pin, x)], hits=False)
    _case('neighbour row changed')
    _restore(w7, hits=False)
    out['K7'] = k7a and classes(it) == ['context-structure-changed']
    x = w6.child(w6.pin, lt.replace('trailer paragraph.', 'trailer changed.'))
    cv, it = w6.coverage(x, [seg(w6.pin, x)], hits=False)
    _restore(w6, hits=False)
    out['K8'] = classes(it) == ['context-structure-changed']
    w9 = World()
    w9.sitemap['sites'][0]['quote'] = 'alpha line one'
    cv, it = w9.coverage(w9.pin, [], hits=False)
    s0 = cv.site_out['%s:3@%s' % (doc_path, w9.pin[:8])]
    w9.sitemap['sites'][0]['quote'] = None
    cv2, it2 = w9.coverage(w9.pin, [], hits=False)
    _bind_first(subject='%s:3@%s' % (doc_path, w9.pin[:8]))
    _restore(w9, hits=False)
    out['K9'] = s0['indicators']['prt'] is True and decision(it) == decision(it2) == oc.pass_
    return out


def b_controls():
    out = _out()
    w = World()
    a = off(base_text, 'beta line two stands here.\n')
    b = a + len('beta line two stands here.\n')
    led = ledger(w.pin, [(doc_path, a, b, '')], w.repo)
    x = w.child(w.pin, base_text.replace('beta line two stands here.\n', ''))
    ctx = w.ctx()
    imgs = pl.image_lines(ctx, x, led, [doc_path])
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _bind_first(subject='%s:5@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['B1'] = any(s['statuses'][-1]['status'] == 'authorized-removal' for s in cv.site_out.values()) and \
        bool(imgs.get(doc_path))
    a2 = off(base_text, 'beta line two')
    b2 = off(base_text, 'gamma line three') + len('gamma line three')
    led = ledger(w.pin, [(doc_path, a2, b2, 'beta and gamma joined')], w.repo)
    t2 = base_text[:a2] + 'beta and gamma joined' + base_text[b2:]
    x = w.child(w.pin, t2)
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    reps = [s for s in cv.site_out.values() if s['statuses'][-1]['status'] == 'authorized-replacement']
    _bind_first(subject='%s:5@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['B2'] = decision(it) == oc.pass_ and len(reps) == 2
    c = off(base_text, 'gamma line three')
    led = ledger(w.pin, [(doc_path, c, c, 'inserted\n\n')], w.repo)
    x = w.child(w.pin, base_text[:c] + 'inserted\n\n' + base_text[c:])
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _case('insertion at a line boundary', subject='%s:7@%s' % (doc_path, w.pin[:8]))
    g = cv.site_out['%s:7@%s' % (doc_path, w.pin[:8])]['statuses'][-1]['status']
    led2 = ledger(w.pin, [(doc_path, c + 3, c + 3, 'X'.lower())], w.repo)
    x2 = w.child(w.pin, base_text[:c + 3] + 'x' + base_text[c + 3:])
    cv2, it2 = w.coverage(x2, [seg(w.pin, x2, 'ledgered', ledger=led2)])
    _case('insertion inside the line', subject='%s:7@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    g2 = cv2.site_out['%s:7@%s' % (doc_path, w.pin[:8])]['statuses'][-1]['status']
    out['B3'] = g == 'moved' and g2 == 'authorized-replacement'
    wl = World(base_text.rstrip('\n'))
    last = len(util.lines_of(base_text.rstrip('\n')))
    cv, it = wl.coverage(wl.pin, [])
    _bind_first(subject='%s:%d@%s' % (doc_path, last, wl.pin[:8]))
    _restore(wl)
    out['B4'] = '%s:%d@%s' % (doc_path, last, wl.pin[:8]) in cv.site_out and decision(it) == oc.pass_
    led = ledger(w.pin, [(doc_path, a2, a2 + len('beta line two'), 'gamma line three')], w.repo)
    x = w.child(w.pin, base_text.replace('beta line two', 'gamma line three', 1))
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _restore(w)
    out['B5'] = 'duplicated' in classes(it)
    e = off(base_text, 'beta line two stands here.\n') + len('beta line two stands here.\n')
    led = ledger(w.pin, [(doc_path, e, e, 'touch\n')], w.repo)
    x = w.child(w.pin, base_text[:e] + 'touch\n' + base_text[e:])
    cv, it = w.coverage(x, [seg(w.pin, x, 'ledgered', ledger=led)])
    _bind_first(subject='%s:5@%s' % (doc_path, w.pin[:8]))
    _restore(w)
    out['B6'] = cv.site_out['%s:5@%s' % (doc_path, w.pin[:8])]['statuses'][-1]['status'] == 'unchanged'
    return out


def h_controls():
    out = _out()
    w, h, s = hp_world()
    sid = '%s:5@%s' % (doc_path, w.pin[:8])
    steps = walk_steps(w, h, s, 5)
    good = {'site_id': sid, 'steps': steps, 'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'},
            'semantic_classification': 'stated', 'author': 'eng-writer'}
    wrong = dict(good, steps=[dict(steps[0], commit=w.pin)])

    def clean_hp():
        return w.coverage(h, [s], adj={'hp': [good]}, hits=False)[1]

    cv, it = w.coverage(h, [s], adj={'hp': [wrong]}, hits=False)
    _restore_with(clean_hp, 'coverage')
    out['H1'] = [i['class'] for i in it if i['subject'] == sid] == ['provenance-mismatch']
    w2, h2, s2 = hp_world(two_steps=True)
    st2 = walk_steps(w2, h2, s2, 5)
    one = {'site_id': '%s:5@%s' % (doc_path, w2.pin[:8]), 'steps': st2[:1],
           'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'}, 'semantic_classification': 'stated', 'author': 'eng-writer'}
    cv, it = w2.coverage(h2, [s2], adj={'hp': [one]}, hits=False)
    full = dict(one, steps=st2)
    _restore_with(lambda: w2.coverage(h2, [s2], adj={'hp': [full]}, hits=False)[1], 'coverage')
    out['H2'] = 'provenance-gap' in classes(it) and len(st2) == 2
    w3, h3, s3 = hp_world(foreign=True)
    cv, it = w3.coverage(h3, [s3], hits=False)
    _restore_with(clean_hp, 'coverage')
    out['H3'] = 'provenance-foreign' in classes(it)
    x = w.child(h, w.ctx().ft(h, doc_path).text.replace('beta line revised', 'beta line rewritten'))
    cv, it = w.coverage(x, [s, seg(h, x)], adj={'hp': [good]}, hits=False)
    _case('', subject=sid)
    x0 = w.child(h, 'top\n' + w.ctx().ft(h, doc_path).text)
    cv0, it0 = w.coverage(x0, [s, seg(h, x0)], adj={'hp': [good]}, hits=False)
    _restore_with(clean_hp, 'coverage')
    out['H4'] = [(i['obligation'], i['class']) for i in it if i['subject'] == sid] == \
        [('RET', 'unauthorized-change')] and not [i for i in it0 if i['subject'] == sid]
    ht = w.ctx().ft(h, doc_path)
    a = ht.data.index(b'revised')
    led = ledger(h, [(doc_path, a, a + 7, 'amended')], w.repo)
    x = w.child(h, ht.text.replace('revised', 'amended'))
    cv, it = w.coverage(x, [s, seg(h, x, 'ledgered', ledger=led)], hits=False)
    _restore_with(lambda: w.coverage(h, [s], hits=False)[1], 'coverage')
    out['H5'] = 'untracked-hp-overlap' in classes(it) and 'hp-unadjudicated' in classes(it) and \
        cv.site_out[sid]['hp_overlap'] is True
    cv, it = w.coverage(h, [s], adj={'hp': [dict(good, carried={'row': 'other', 'code': 'code-x', 'owner': 'owner-x'})]},
                        hits=False)
    _restore_with(clean_hp, 'coverage')
    out['H6'] = [i['class'] for i in it if i['subject'] == sid] == ['adjudication-row-changed']
    wm, hm, sm = hp_world(shared=True)
    cv, it = wm.coverage(hm, [sm], hits=False)
    shared = [so for so in cv.site_out.values() if so['region_shared_with']]
    ht = wm.ctx().ft(hm, doc_path)
    a = ht.data.index(b'second merged')
    led = ledger(hm, [(doc_path, a, a + 6, 'other ')], wm.repo)
    x = wm.child(hm, ht.text.replace('second merged', 'other  merged'))
    cv2, it2 = wm.coverage(x, [sm, seg(hm, x, 'ledgered', ledger=led)], hits=False)
    s1, s2 = ['%s:%d@%s' % (doc_path, n, wm.pin[:8]) for n in (5, 7)]
    so1, so2 = cv2.site_out[s1], cv2.site_out[s2]
    basic = len(shared) == 2 and so1['region_shared_with']['with'] == [s2] and so1['region_splices'] == ['S1'] and \
        so2['region_splices'] == ['S1'] and so1['line_splices'] == [] and so2['line_splices'] == ['S1']
    st5, st7 = walk_steps(wm, hm, sm, 5), walk_steps(wm, hm, sm, 7)
    region = [l for l in ht.lines if 'merged' in l or not l.strip()]
    reg = ['first merged line.', '', 'second merged line.']

    def adj(sid, steps, own, attr):
        return {'site_id': sid, 'steps': steps, 'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'},
                'semantic_classification': 'stated', 'author': 'eng-writer', 'own_lines': own,
                'splice_attribution': attr}
    good = [adj(s1, st5, [util.sha256(reg[0])], {'S1': [s2]}), adj(s2, st7, [util.sha256(reg[2])], {'S1': [s2]})]
    cv3, it3 = wm.coverage(x, [sm, seg(hm, x, 'ledgered', ledger=led)], adj={'hp': good}, hits=False)
    hp_ok = not [i for i in it3 if i['class'] == 'record-invalid']
    unassigned = [adj(s1, st5, [util.sha256(reg[0])], {'S1': [s2]}), adj(s2, st7, [], {'S1': [s2]})]
    cv4, it4 = wm.coverage(x, [sm, seg(hm, x, 'ledgered', ledger=led)], adj={'hp': unassigned}, hits=False)
    unattr = [adj(s1, st5, [util.sha256(reg[0])], {}), adj(s2, st7, [util.sha256(reg[2])], {})]
    cv5, it5 = wm.coverage(x, [sm, seg(hm, x, 'ledgered', ledger=led)], adj={'hp': unattr}, hits=False)
    out['H7'] = basic and hp_ok and 'record-invalid' in classes(it4) and 'record-invalid' in classes(it5)
    return out


def chain_world():
    """A record and its review, with fixture identities."""
    rule = {'schema': 'oi-term-rules/2', 'record_id': 'r1', 'author': 'eng-writer', 'supersedes': None,
            'rules': [{'id': 'q1'}]}
    rb = util.canonical(rule)
    ref = {'path': 'rec/r.json', 'blob_sha256': util.sha256(rb)}
    review = {'schema': rec.review_schema, 'reviewer': 'eng-reviewer', 'reviewed': ref, 'method': 'read the objects',
              'verdicts': [{'item': 'q1', 'verdict': 'accept'}]}
    vb = util.canonical(review)
    vref = {'path': 'rec/r.review.json', 'blob_sha256': util.sha256(vb)}
    return rule, review, ref, vref


def chain_probs(rule, review, admitted_extra=(), mutate_ref=None):
    rb, vb = util.canonical(rule), util.canonical(review)
    entries = [('rec/r.json', rb), ('rec/r.review.json', vb)]
    st = rec.Store(entries)
    ref = {'path': 'rec/r.json', 'blob_sha256': util.sha256(rb)}
    admitted = {util.sha256(b) for _, b in entries} | set(admitted_extra)
    checked = mutate_ref or ref
    problems = rec.lint_chain(checked, st, admitted)
    _capture_record_lint(checked, entries, admitted, problems)
    return problems


def _capture_record_lint(ref, entries, admitted, problems):
    if capture_hook is None:
        return
    items = []
    if problems:
        items.append(oc.make_item('RECORD', 'record-invalid', ref['path'], None,
                                  {'sha': ref['blob_sha256'], 'why': problems[0]}, detail=problems))
    _stage('record lint', items, record_blobs={path: data.decode('utf-8') for path, data in entries},
           admitted_blob_hashes=sorted(admitted), inputs={'classify_records': [] if problems else [ref]})


def o_controls():
    out = _out()
    rule, review, ref, vref = chain_world()

    def clean_lint():
        return chain_probs(rule, review)

    def checked_lint(check_rule, check_review, **options):
        problems = chain_probs(check_rule, check_review, **options)
        _case('', record=ref['path'])
        _restore_with(clean_lint, 'record lint')
        return problems

    out['O9'] = checked_lint(rule, review) == []
    out['O1'] = bool(checked_lint(rule, dict(review, reviewer='eng-writer')))
    other = dict(rule, record_id='r2')
    r2 = dict(review, reviewed={'path': 'rec/r.json', 'blob_sha256': util.sha256(util.canonical(other))})
    out['O2'] = bool(checked_lint(rule, r2))
    r3 = dict(rule, rules=[{'id': 'q1'}, {'id': 'q2'}])
    nref = {'path': 'rec/r.json', 'blob_sha256': util.sha256(util.canonical(r3))}
    rv3 = dict(review, reviewed=nref)
    out['O3'] = bool(checked_lint(r3, rv3))
    out['O5'] = bool(checked_lint(rule, dict(review, reviewer='https://ci.example/runs/7')))
    rb = util.canonical(rule)
    st = rec.Store([('rec/r.json', rb + b' ')])
    out['O6'] = st.get({'path': 'rec/r.json', 'blob_sha256': util.sha256(rb)}) is None
    sup = dict(rule, record_id='r1b', supersedes=ref)
    out['O7'] = bool(checked_lint(sup, review, mutate_ref={'path': ref['path'],
                                                        'blob_sha256': util.sha256(util.canonical(sup))}))
    rb2 = util.canonical(rule)
    st = rec.Store([('rec/r.json', rb2)])
    problems = rec.lint_chain(ref, st, set())
    _capture_record_lint(ref, [('rec/r.json', rb2)], set(), problems)
    _case('', record=ref['path'])
    _restore_with(clean_lint, 'record lint')
    out['O8'] = any('not referenced' in p for p in problems)
    return out


def r_controls():
    """Tree roles (sec. 13) on neutral trees."""
    out = _out()
    w = World()
    H = w.pin
    a = off(base_text, 'beta line two')
    led = ledger(H, [(doc_path, a, a + 4, 'bet' + 'X'.lower())], w.repo)
    led['edits'] = []
    wf = 'ops/flow.yml'
    M = w.child(H, files={wf: b'flow two\n'}, subject='main moves')
    X = w.child(H, base_text.replace('beta line two', 'betx line two', 1), subject='candidate')
    ctx = w.ctx()

    def run(m=None, l=None, x=X, side=(), recon=(), cand=True):
        e = exmod.Execution(ctx, H, x, led, None, m, l, None, list(side), list(recon))
        if cand:
            e.candidate()
        if m:
            e.main_role(set(led['files']) | {doc_path})
        if l:
            e.landing()
        _stage('execution', e.items, side_changes=e.side_changes)
        return e

    def pin(cid, commit, *paths):
        return {'id': cid, 'pins': [{'path': p, 'git_blob': w.repo.blob_id(commit, p),
                                     'blob_sha256': util.sha256(w.repo.read(commit, p))} for p in paths]}
    wfc = pin('wf', M, wf)

    def clean_c():
        return run(M, side=[wfc]).items

    def clean_l():
        return run(M, exmod.compose_landing(w.repo, H, M, X, led, w.repo), side=[wfc]).items
    e = run(M, side=[wfc])
    _restore_with(clean_c, 'execution')
    out['TT1'] = not e.items and e.side_changes[0]['class'] == 'wf'
    # R18 (S3): a listed path whose blob at M differs from its pin; R19 (V3): a prefix alone classifies nothing
    _restore_with(clean_c, 'execution')
    out['R18-engine'] = 'side-change-unclassified' in classes(run(M, side=[dict(wfc, pins=[dict(
        wfc['pins'][0], blob_sha256='0' * 64)])]).items)
    xm = w.repo.derive(M, {doc_path: w.repo.read(X, doc_path)}, parents=[H])
    e2 = run(x=xm)
    _restore_with(clean_c, 'execution')
    out['TT2'] = any(i['subject'] == wf for i in e2.items)
    X3 = w.repo.derive(M, {doc_path: w.repo.read(X, doc_path)}, parents=[M])
    _restore_with(clean_c, 'execution')
    out['TT3'] = 'candidate-parent' in classes(run(x=X3).items)
    X4 = w.repo.derive(H, {doc_path: w.repo.read(X, doc_path)}, parents=[H, M])
    _restore_with(clean_c, 'execution')
    out['TT4'] = 'candidate-parent' in classes(run(x=X4).items)
    l5 = dict(led, base=M)
    e5 = exmod.Execution(ctx, H, X, l5, None)
    try:
        e5.integrity()
        tt5 = False
    except oc.Stop as s:
        _stage_stop('execution integrity', s)
        tt5 = s.cls == 'SCIENTIFIC_BASE_MISMATCH'

    def clean_integrity():
        exmod.Execution(ctx, H, X, led, None).integrity()
        return []
    _restore_with(clean_integrity, 'execution integrity')
    out['TT5'] = tt5
    other = w.repo.add_commit({doc_path: b'unrelated\n'}, [], 'unrelated root')
    try:
        run(other, cand=False)
        tt6 = False
    except oc.Stop as s:
        _stage_stop('execution', s)
        tt6 = s.cls == 'MAIN_NOT_DESCENDANT'
    _restore_with(lambda: run(M, side=[wfc], cand=False).items, 'execution')
    out['TT6'] = tt6
    M7 = w.child(H, base_text.replace('epsilon closing', 'epsilon finale'), subject='main edits ledgered file')
    if capture_hook is not None:
        run()
        _case('candidate X')
    e7 = run(M7)
    _case('M side')
    L7 = exmod.compose_landing(w.repo, H, M7, X, led, w.repo)
    e7l = run(M7, L7)
    _case('landing under the computed composition')
    _restore_with(clean_l, 'execution')
    out['TT7'] = not [i for i in e7.items if i['obligation'] == 'RET'] and 'base-drift' in classes(e7.items)
    rec8 = rcmod.draft(w.repo, ctx, H, M7, X, led, doc_path, scientific_effect=control_effect)
    e8 = run(M7, L7, recon=[rec8])
    _case('the control input (positive)')
    if capture_hook is not None:
        run(M7, L7)
        _case('countercase: the same landing with a ledgered path changed on main after H')
    out['TT8'] = not [i for i in e8.items if i['class'] in ('base-drift', 'landing-conflict-unresolved',
                                                         'record-invalid')]
    bad8 = dict(rec8, paths=[dict(rec8['paths'][0], l=w.repo.blob_id(X, doc_path))])
    e8b = run(M7, L7, recon=[bad8])
    out['R8-S6'] = 'record-invalid' in classes(e8b.items) and 'base-drift' in classes(e8b.items)
    L = exmod.compose_landing(w.repo, H, M, X, led, w.repo)
    out['RL'] = not run(M, L, side=[wfc]).items
    L9 = w.repo.derive(L, {}, parents=[X, M])
    _restore_with(clean_l, 'execution')
    out['TT9'] = 'landing-parents' in classes(run(M, L9, side=[wfc]).items)
    L10 = w.repo.derive(L, {wf: None}, parents=[M, X])
    _restore_with(clean_l, 'execution')
    out['TT10'] = 'landing-drops-main-change' in classes(run(M, L10, side=[wfc]).items)
    L11 = w.repo.derive(L, {other_path: b'extra word\n'}, parents=[M, X])
    _restore_with(clean_l, 'execution')
    out['TT11'] = 'landing-extra-change' in classes(run(M, L11, side=[wfc]).items)
    L12 = w.repo.derive(L, {doc_path: w.repo.read(H, doc_path)}, parents=[M, X])
    _restore_with(clean_l, 'execution')
    out['TT12'] = bool(classes(run(M, L12, side=[wfc]).items))
    M13 = w.child(H, files={'tools/t.py': b'x = 1\n'}, subject='tool landing')
    tool = dict(pin('tool', M13, 'tools/t.py'), prefixes=['tools/'])
    L13 = exmod.compose_landing(w.repo, H, M13, X, led, w.repo)
    e13 = run(M13, L13, side=[tool])
    positive13 = 'the control input (positive)'
    _case(positive13)
    classified = bool(e13.side_changes) and all(side.get('class') == tool['id'] for side in e13.side_changes)
    if capture_hook is not None:
        capture_hook.attest(positive13, {'side_changes_classified_by': 'tool-landing class pin' if classified else None,
                                         'candidate_and_landing_pass': not e13.items})
    changed13 = w.child(H, files={'tools/t.py': b'x = 2\n'}, subject='changed tool blob')
    invalid13 = run(changed13, side=[tool])
    _case('countercase: a tool-landing path whose blob differs from its class pin')
    out['TT13'] = not e13.items and classified and 'side-change-unclassified' in classes(invalid13.items)
    M19 = w.child(M13, files={'tools/u.py': b'y = 2\n'}, subject='unlisted tool file')
    _restore_with(lambda: run(M13, side=[tool]).items, 'execution')
    out['R19-engine'] = 'side-change-unclassified' in classes(run(M19, side=[tool]).items)
    M14 = w.child(H, base_text.replace('epsilon closing', 'epsilon tool edit'), subject='tool touches ledgered')
    _restore_with(lambda: run(M13, side=[tool]).items, 'execution')
    out['TT14'] = 'base-drift' in classes(run(M14, side=[tool]).items)
    Mo = w.child(M, files={'ops/other.yml': b'z\n'}, subject='another main')
    L15 = exmod.compose_landing(w.repo, H, Mo, X, led, w.repo)
    _restore_with(clean_l, 'execution')
    out['R15'] = 'landing-first-parent-not-M' in classes(run(M, L15, side=[wfc, pin('ops-other', Mo, 'ops/other.yml')],
                                                             cand=False).items)
    e16 = exmod.Execution(ctx, H, X, led, None, pin_ok=[{'file': 'tools/t.py', 'prefix': 'x', 'recorded_at': M}])
    e16.freeze = H
    e16.pins({'min_len': 20, 'skip_prefixes': [], 'ok': []})
    _stage('execution pins', e16.items)
    e17 = exmod.Execution(ctx, H, X, led, None, pin_ok=[{'file': 'tools/t.py', 'prefix': 'x', 'recorded_at': H}])
    e17.freeze = M
    e17.pins({'min_len': 20, 'skip_prefixes': [], 'ok': []})
    _stage('execution pins', e17.items)
    _case('restored')
    out['N1'] = 'pin-broken' in classes(e16.items) and not e17.items
    # N2 (S2): op C's items on X with and without the records must be identical; a candidate stage that let a
    # record change a decision on X is caught by that comparison (the defect is injected here)
    out['N2'] = n2_control(w, ctx, H, X, led, rec8)
    return out


def n2_control(w, ctx, H, X, led, rec):
    from . import cli as climod
    real = exmod.Execution.candidate

    def leaky(self, commit=None, parent=None):
        real(self, commit, parent)
        if self.reconciliations:
            self.items = [i for i in self.items if i['class'] != 'unauthorized-edit']
    Xu = w.child(H, base_text.replace('beta line two', 'bxta line two', 1), subject='bad')
    exmod.Execution.candidate = leaky
    try:
        items = climod.candidate_with_and_without(ctx, H, Xu, led, None, None, None, Xu, [], [rec]).items
    finally:
        exmod.Execution.candidate = real
    _stage('compare candidate evaluations', items)

    def clean_candidate():
        return climod.candidate_with_and_without(ctx, H, Xu, led, None, None, None, Xu, [], [rec]).items

    clean = clean_candidate()
    _restore_with(clean_candidate, 'compare candidate evaluations')
    return 'record-invalid' in classes(items) and 'record-invalid' not in classes(clean) and \
        'unauthorized-edit' in classes(clean)


def rule_controls():
    """Generic rule application and lint (sec. 6.2, 6.3) on a neutral allow rule."""
    out = _out()
    sent = 'The zeta value counts seven items, listed below.'
    w = World(base_text.replace('delta line four stands here.', sent))
    ctx = w.ctx()
    sents = ctx.sentences(w.pin, doc_path)
    k = [i for i, s in enumerate(sents) if s[0] == sent][0]
    rule = {'id': 'q1', 'kind': 'allow', 'profiles': ['np-review'], 'scope': {'files': [doc_path]},
            'matcher': {'literal': 'The zeta value', 'context': ['items'], 'negative': ['omega']},
            'context_required': False, 'max_instances': 1,
            'fingerprints': [{'file': doc_path, 'sentence_sha256': util.sha256(sent),
                              'context_sha256': rulemod.sentence_context_sha(sents, k)}],
            'recorded_at': w.pin, 'positive_examples': [sent, 'The zeta value counts items.'],
            'negative_examples': ['The zeta value counts omega items.'], 'reason': 'neutral', 'author': 'eng-writer'}

    def terms(commit, rules):
        c = w.ctx(rules)
        tm = pl.Terms(c, commit, [c.profiles['np-review']], [c.profiles['np-deny']])
        tm.deny()
        tm.review()
        tm.stale_rules()
        return _stage('terms', tm.items)
    out['E-L1'] = not terms(w.pin, [rule])
    x = w.child(w.pin, w.ctx().ft(w.pin, doc_path).text + '\n' + sent + '\n')
    out['E-L3'] = classes(terms(x, [rule])) == ['rule-overreach']
    x = w.child(w.pin, w.ctx().ft(w.pin, doc_path).text.replace(sent, 'The zeta value counts seven new items.'))
    it = terms(x, [rule])
    out['E-S1r'] = 'rule-fingerprint-mismatch' in classes(it)
    x = w.child(w.pin, w.ctx().ft(w.pin, doc_path).text.replace(sent, ''))
    out['E-S2r'] = 'rule-stale' in classes(terms(x, [rule]))
    x = w.child(w.pin, w.ctx().ft(w.pin, doc_path).text.replace(sent, 'The zeta value counts omega items.'))
    out['rule-negative'] = 'rule-negative-match' in classes(terms(x, [rule]))
    x = w.child(w.pin, w.ctx().ft(w.pin, doc_path).text.replace(sent, 'The zeta value counts items; zeta holds.'))
    out['A5r-generic'] = 'deny-match' in classes(terms(x, [rule]))
    lk = (lambda n: w.ctx().profiles.get(n),
          lambda c, f, sh: next(((s, [], rulemod.sentence_context_sha(sents, i)) for i, (s, _, _) in enumerate(sents)
                                 if util.sha256(s) == sh), None))
    rule_file = 'rec/rules.json'

    def rule_lint(problems):
        # the rule record's lint as a stage result: one record-invalid item on the rule file when lint fails
        items = [oc.make_item('RECORD', 'record-invalid', rule_file, None, {'why': problems[0]}, file=rule_file,
                              detail=problems)] if problems else []
        _stage('rule lint', items, lint_problems=list(problems))
        _case('', rule_file=rule_file)
        return problems

    lint_problems = rulemod.lint_rule(rule, lk[0], lk[1], [], lambda cc: None)
    rule_lint(lint_problems)
    if capture_hook is not None:
        capture_hook.attest('', {'outcome': 'LINT_PASS' if lint_problems == [] else 'LINT_FAIL',
                                 'lint_problems': lint_problems})
    out['lint-ok'] = lint_problems == []
    out['E-A6r'] = bool(rule_lint(rulemod.lint_rule(dict(rule, matcher=dict(rule['matcher'], literal='counts seven')),
                                                    lk[0], lk[1], [], lambda cc: None)))
    out['E-A8r'] = bool(rule_lint(rulemod.lint_rule(dict(rule, negative_examples=[]), lk[0], lk[1], [],
                                                    lambda cc: None)))
    out['E-A1r'] = bool(rule_lint(rulemod.allow_widening(rule, dict(rule, scope={'files': [doc_path, other_path]}))))
    out['E-A2r'] = bool(rule_lint(rulemod.allow_widening(rule, dict(rule, matcher=dict(rule['matcher'],
                                                                                        literal='zeta')))))
    fp2 = dict(rule['fingerprints'][0], sentence_sha256=util.sha256('another'))
    out['E-A3r'] = bool(rule_lint(rulemod.allow_widening(rule, dict(rule, fingerprints=[fp2]))))
    return out


# the writer's scientific effect of a control fixture's reconciliation record (amendment 3, R6.RECON.25)
control_effect = {'conclusions': 'none', 'assessment': 'control fixture: the change on main touches no planned edit',
                  'method': 'control: every condition recomputed from git objects', 'verdict': 'no-effect'}


def route_controls():
    """The record commit of the post-freeze route (recon_route.rev_problems, placement and the scanned set) on a
    neutral in-memory repository, each countercase beside the admitted control input: only a record commit whose
    single parent is the run's M, adding regular files in a reconciliation directory, is admitted."""
    from . import recon_route as rr
    from .. import record_authority as ra
    out = _out()
    repo = Overlay(None)
    root = ra.reconciliation_root
    plan = ra.authorized_record_directories[0] + '/'
    tool_dir = root + 'neutral-tool/'
    pin_path = 'tools/neutral/entry.py'
    files = {'notes/a.md': b'ledgered text\n', 'corpus/b.md': b'corpus text\n', 'misc/readme.txt': b'readme\n',
             pin_path: b'x = 1\n', plan + 'cfg.json': b'{}\n'}
    m0 = repo.add_commit(files, [], 'm0')
    landing = {pin_path: b'x = 2\n', tool_dir + 'note.md': b'tool note\n'}
    mp = repo.derive(m0, landing, parents=[m0], subject='predicted main: m0 plus the tool landing')
    cls_doc = {'classes': [{'id': ra.tool_landing_class_id, 'prefixes': [tool_dir],
                            'pins': [{'path': pin_path, 'git_blob': repo.blob_id(mp, pin_path)}]}]}

    def scope(M, harness=True, pinned=cls_doc, plan_dir=plan.rstrip('/')):
        return rr.Scope(repo, m0, M, M, None, harness, pinned, plan_dir, ['notes/a.md'],
                        lambda p: p.startswith('corpus/'), [])

    rec_dir = root + 'neutral-recon/'

    def rev(parent, extra=None, parents=None):
        ch = {rec_dir + 'r.json': b'{"schema": "oi-reconciliation/1"}\n'}
        ch.update(extra or {})
        return repo.derive(parent, ch, parents=parents or [parent], subject='record commit')

    def probs(r, sc):
        return rr.rev_problems(repo, r, r, sc)
    good = probs(rev(mp), scope(mp))
    ok = good == []

    def child(base, ch, subject):
        return repo.derive(base, ch, parents=[base], subject=subject)
    # C4 to C4e: a base below M across a ledgered, corpus or other change, a record added, or a merge
    for cid, ch in (('RB-C4', {'notes/a.md': b'changed on main\n'}), ('RB-C4b', {'corpus/b.md': b'changed\n'}),
                    ('RB-C4c', {'misc/readme.txt': b'changed\n'}),
                    ('RB-C4d', {rec_dir + 'other.json': b'{"schema": "oi-reconciliation/1"}\n'})):
        top = child(mp, ch, cid)
        out[cid] = ok and probs(rev(mp), scope(top)) != [] and probs(rev(top), scope(top)) == []
    side = repo.derive(m0, {'misc/side.txt': b'side\n'}, parents=[m0])
    merged = repo.derive(mp, {'misc/side.txt': b'side\n'}, parents=[mp, side], subject='merge')
    out['RB-C4e'] = ok and probs(rev(mp), scope(merged)) != [] and probs(rev(merged), scope(merged)) == []
    # C5, C5b: a tool-landing pin changed or deleted between the base and M
    top = child(mp, {pin_path: b'arbitrary\n'}, 'pin changed')
    out['RB-C5'] = ok and probs(rev(mp), scope(top)) != [] and probs(rev(top), scope(top)) == []
    top = repo.derive(mp, {pin_path: None}, parents=[mp], subject='pin deleted')
    out['RB-C5b'] = ok and probs(rev(mp), scope(top)) != [] and probs(rev(top), scope(top)) == []
    # C7, C7b: a class record that the configuration does not pin, with prefixes over ledgered and corpus paths,
    # neither widens the domain nor admits a base across those changes
    extra = {'classes': [{'id': 'neutral-extra', 'prefixes': ['notes/', 'corpus/']}]}
    top = child(mp, {'notes/a.md': b'changed on main\n'}, 'ledgered change')
    sc7 = scope(top, pinned=cls_doc)
    out['RB-C7'] = ok and probs(rev(mp), sc7) != [] and \
        rr.Scope(repo, m0, top, top, None, True, extra, plan, ['notes/a.md'], lambda p: p.startswith('corpus/'),
                 []).prefixes == []
    top = child(mp, {'corpus/b.md': b'changed\n'}, 'corpus change')
    out['RB-C7b'] = ok and probs(rev(mp), scope(top)) != [] and probs(rev(top), scope(top)) == []
    # C8: a plan directory that is not an authorized record directory counts for nothing
    top = child(mp, {'corpus/b.md': b'changed again\n'}, 'corpus change')
    sc8 = scope(top, plan_dir='corpus')
    out['RB-C8'] = ok and sc8.plan_dir is None and probs(rev(mp), sc8) != []
    # C10: chain mode, base m0 under the predicted main
    out['RB-C10'] = ok and probs(rev(m0), scope(mp, harness=False)) != [] and \
        probs(rev(mp), scope(mp, harness=False)) == []
    # C11: the record commit also changes a path its parent holds
    out['RB-C11'] = ok and probs(rev(mp, {'notes/a.md': b'edited by the record commit\n'}), scope(mp)) != []
    out['RB-P1'] = ok
    return out


groups = [('U', u_controls), ('M', m_controls), ('K', k_controls), ('B', b_controls), ('H', h_controls),
          ('O', o_controls), ('R', r_controls), ('rules', rule_controls), ('RB', route_controls)]
preflight_ids = ['U1', 'U4', 'U10', 'M1', 'K1', 'O9', 'O1']


def run(ids):
    res = []
    for name, fn in groups:
        if ids is not None and not any(i.startswith(name) or i in ('O9', 'O1') for i in ids):
            continue
        try:
            got = fn()
        except Exception as exc:
            res.append({'id': name, 'passed': False, 'error': '%s: %s' % (type(exc).__name__, exc),
                        'trace': traceback.format_exc()[-800:]})
            continue
        for k, v in sorted(got.items()):
            if ids is None or k in ids:
                res.append({'id': k, 'passed': bool(v)})
    return res
