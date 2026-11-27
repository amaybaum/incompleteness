"""Local controls for the formal adjudication design r4 (PR #1605 at 6d79e98363f7542414a00598ddd0197737f09c84,
adopted with OD-1 to OD-7 at their defaults), at the level of its mechanical predicates (engine/adjudication.py) over
explicit records. The predicates are not called by a run: applying them needs the r9 and r13 amendments the design's
sec. 6 lists, which are not adopted, so `Adjudicated(W)` stays false in every run. The control ids carry the prefix
PRED: and name the CONTROLS.json control whose predicate dimension each exercises; none stands for the run-level
control itself, and no expectation row is registered by this suite.

Usage: python3 -I -B tools/ledger_coverage/adapters/adjudication_controls.py OUT
Writes OUT/adjudication-controls.json and exits 0 when every control holds, 1 otherwise.
"""
import copy
import importlib.util
import json
import os
import shutil
import sys
from datetime import datetime, timezone

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage import record_authority as ra  # noqa: E402
from ledger_coverage.engine import adjudication as adj  # noqa: E402
from ledger_coverage.engine import findings as fd  # noqa: E402
from ledger_coverage.engine import gitobj  # noqa: E402

RESULTS = []
OWNERS = ra.OWNER_IDENTITIES
P = 'doc/s.md'


def case(cid, expected, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL'})


def h64(c):
    return c * 64


def h40(c):
    return c * 40


class Fx:
    """The base fixture: finding f (record carrying it by fw, reviewed by fr), disputed record Q (author w, accepting
    review by qa), adverse review V of Q by v (reject on <p>:scientific_effect), replacement R (author ra, reviewer n),
    reassessment A (author aa), configuration K' (author ka), adjudication J by j, technical review T by t."""

    def __init__(self):
        self.fref = {'path': 'verification/audits/rf/f.json', 'blob_sha256': h64('1')}
        self.qref = {'path': 'verification/audits/rq/q.json', 'blob_sha256': h64('2')}
        self.vref = {'path': 'verification/audits/rq/v.review.json', 'blob_sha256': h64('3')}
        self.rref = {'path': 'verification/audits/rr/r.json', 'blob_sha256': h64('4')}
        self.aref = {'path': 'verification/audits/plan/a.json', 'blob_sha256': h64('5')}
        self.kref = {'path': 'verification/audits/plan/config.json', 'blob_sha256': h64('6')}
        self.jref = {'path': 'verification/audits/rr/j.json', 'blob_sha256': h64('7')}
        self.tref = {'path': 'verification/audits/rr/j.review.json', 'blob_sha256': h64('8')}
        self.git = {self.fref['blob_sha256']: h40('a'), self.qref['blob_sha256']: h40('b'),
                    self.vref['blob_sha256']: h40('c'), self.rref['blob_sha256']: h40('d'),
                    self.aref['blob_sha256']: h40('e'), self.jref['blob_sha256']: h40('f')}
        self.frec = {'author': 'fw'}
        self.frev = {'reviewer': 'fr'}
        self.Q = {'schema': 'oi-reconciliation/2', 'author': 'w', 'record_id': 'q', 'paths': [{'path': P}]}
        self.V = {'reviewer': 'v', 'verdicts': [{'item': P, 'verdict': 'accept'},
                                                {'item': P + ':scientific_effect', 'verdict': 'reject'}]}
        self.R = {'author': 'ra'}
        self.entry = dict(self.rref, entry_path=P)
        self.finding = dict(self.fref, item=P)
        self.A = {'author': 'aa', 'finding': dict(self.finding),
                  'repair': {'commits': [h40('9')], 'entry': dict(self.entry)}}
        self.K = {'author': 'ka'}
        self.reviews = [{'reviewer': 'qa'}, {'reviewer': 'n'}]  # accepting review of Q by qa; review of R by n
        adverse = adj.review_witness_adverse([(self.vref, self.V, self.Q)])
        self.W = adj.witness_description('review', self.qref, [self.vref], adverse, self.kref)
        self.J = {'schema': adj.schema, 'record_id': 'j1', 'supersedes': None, 'author': 'j',
                  'authorization': {'quote': 'I authorize j to adjudicate W for R.', 'author': OWNERS[0],
                                    'time': '2026-11-27T10:00Z', 'source': '#1169 comment 1',
                                    'adjudicator': 'j', 'finding': dict(self.finding),
                                    'witness_sources': [dict(self.vref)], 'replacement': dict(self.entry)},
                  'finding': dict(self.finding),
                  'witness': {'class': 'review', 'disputed': dict(self.qref), 'edge': None,
                              'sources': [dict(self.vref)], 'adverse': copy.deepcopy(adverse),
                              'original_configuration': dict(self.kref)},
                  'replacement': dict(self.entry), 'reassessment': dict(self.aref), 'dissents_addressed': [],
                  'disposition': 'cleared',
                  'grounds': [{'id': 'g1', 'target': copy.deepcopy(adverse[0]),
                               'reasoning': 'the objection concerns Q\'s entry, which R replaces',
                               'evidence': [h40('c'), h40('b'), h40('d')]}],
                  'method': 'read ' + ' '.join([h40('a'), h40('c'), h40('b'), h40('d'), h40('e')]),
                  'conflicts': 'none'}
        self.landing_time = datetime(2026, 11, 27, 12, 0, tzinfo=timezone.utc)

    def T(self, reviewer='t', **upd):
        rv = {'schema': fd.review_schema, 'reviewer': reviewer, 'reviewed': dict(self.jref),
              'method': 'read %s %s' % (h40('f'), h40('c')),
              'verdicts': [{'item': i, 'verdict': 'accept', 'reason': 'checked'} for i in adj.item_ids(self.J)]}
        rv.update(upd)
        return rv

    def git_of(self, ref):
        return self.git.get((ref or {}).get('blob_sha256')) if isinstance(ref, dict) else None

    def parties(self, J=None):
        return adj.parties(finding_record=self.frec, finding_review=self.frev, Q=self.Q, R=self.R, A=self.A,
                           config=self.K, sources=[self.V], reviews=self.reviews)

    def all_problems(self, J=None, T=None, reproduced='base', resolves=lambda r: True):
        J = J if J is not None else self.J
        T = T if T is not None else self.T()
        W = self.W if reproduced == 'base' else reproduced
        ps = self.parties()
        out = adj.form_problems(J)
        if out:
            return out
        out += adj.authorization_problems(J, self.landing_time, OWNERS)
        out += adj.independence_problems(J, T.get('reviewer'), ps, OWNERS)
        out += adj.self_consistency(J, W, resolves)
        out += adj.binds(J, self.aref, self.A, W)
        out += adj.substance_problems(J, self.git_of)
        out += adj.review_problems(T, J, self.jref, self.git_of(self.jref),
                                   [self.git_of(s) for s in J['witness']['sources']], ps, OWNERS)
        return out


def conds(problems):
    return sorted({c for c, _m in problems})


def variants(name, expected, base_mut, want):
    got = {}
    for v, mut in base_mut.items():
        fx = Fx()
        J = copy.deepcopy(fx.J)
        got_kw = mut(fx, J)
        # a mutator returns keyword arguments for all_problems only as a dict of T, reproduced or resolves
        kw = got_kw if isinstance(got_kw, dict) and set(got_kw) <= {'T', 'reproduced', 'resolves'} else {}
        got[v] = conds(fx.all_problems(J=J, **kw))
    case(name, expected, got, all(want in got[v] for v in got))


def form_and_authorization():
    fx = Fx()
    base = fx.all_problems()
    case('PRED:ADJ-BASE', 'the base adjudication J and its technical review T meet R6.ADJ.2 to R6.ADJ.7 (no failure)',
         base, base == [])
    variants('PRED:ADJ-N-UNAUTHORIZED', 'J without an authorization key (variant b: authorization claimed only in '
                                        'method and reasoning): ADJ-AUTH-FORM',
             {'a': lambda fx, J: J.pop('authorization'),
              'b': lambda fx, J: (J.pop('authorization'), J.update(method=J['method'] + ' authorized by o'))},
             'ADJ-AUTH-FORM')
    variants('PRED:ADJ-N-AUTH-NOT-OWNER', 'authorization.author outside OWNER_IDENTITIES: ADJ-AUTH-OWNER',
             {'a': lambda fx, J: J['authorization'].update(author='lead')}, 'ADJ-AUTH-OWNER')
    variants('PRED:ADJ-N-AUTH-SCOPE', 'authorized adjudicator, finding item, witness sources or replacement differ from '
                                      'the record\'s: ADJ-AUTH-SCOPE',
             {'a': lambda fx, J: J['authorization'].update(adjudicator='j2'),
              'b': lambda fx, J: J['authorization']['finding'].update(item=P + ':other'),
              'c': lambda fx, J: J['authorization'].update(witness_sources=[{'path': 'x/v2.json',
                                                                             'blob_sha256': h64('c')}]),
              'd': lambda fx, J: J['authorization'].update(replacement=dict(fx.entry, blob_sha256=h64('d')))},
             'ADJ-AUTH-SCOPE')
    variants('PRED:ADJ-N-AUTH-TIME', 'authorization.time later than the committer time of L(J): ADJ-AUTH-TIME',
             {'a': lambda fx, J: J['authorization'].update(time='2026-11-27T13:00Z')}, 'ADJ-AUTH-TIME')
    variants('PRED:ADJ-N-ERASE-BY-DISPOSITION', 'disposition withdrawn, or supersedes non-null: ADJ-FORM',
             {'a': lambda fx, J: J.update(disposition='withdrawn'),
              'b': lambda fx, J: J.update(supersedes=dict(fx.fref)),
              'c': lambda fx, J: J.update(supersedes={'path': 'x/j0.json', 'blob_sha256': h64('0')})},
             'ADJ-FORM')
    J = copy.deepcopy(fx.J)
    J['grounds'][0]['nested'] = {'reviewed': {}, 'verdicts': [{'verdict': 'invalidates'}]}
    shape = adj.detection_shape_problems(J)
    case('PRED:ADJ-B-DETECTION-SHAPE', 'a nested object with keys reviewed and verdicts: R6.ADJ.14 reports the shape '
                                       '(and the closed table fails the extra key)',
         {'shape': shape, 'form': conds(adj.form_problems(J))},
         len(shape) == 2 and 'ADJ-FORM' in conds(adj.form_problems(J)) and adj.detection_shape_problems(fx.J) == [])


def independence():
    def author(a):
        return lambda fx, J: (J.update(author=a), J['authorization'].update(adjudicator=a))
    variants('PRED:ADJ-N-CONFLICTED', 'the adjudicator is the author of R, of A or of K\', a reviewer of Q or R, the '
                                      'reviewer of the record carrying the finding, or the owner: ADJ-INDEP',
             {'a': author('ra'), 'b': author('aa'), 'c': author('qa'), 'd': author('n'), 'e': author('ka'),
              'f': author('fr'), 'g': author(OWNERS[0])}, 'ADJ-INDEP')
    variants('PRED:ADJ-N-DISPUTED-AUTHOR', 'the adjudicator is the author of Q or the adverse reviewer v: ADJ-INDEP',
             {'a': author('w'), 'b': author('v')}, 'ADJ-INDEP')
    variants('PRED:ADJ-N-REVIEWER-CONFLICTED', 'the technical reviewer is the author of R, the adjudicator, v or a CI '
                                               'run URL: ADJ-INDEP',
             {'a': lambda fx, J: {'T': fx.T('ra')}, 'b': lambda fx, J: {'T': fx.T('j')},
              'c': lambda fx, J: {'T': fx.T('v')},
              'd': lambda fx, J: {'T': fx.T('https://github.com/o/r/actions/runs/1')}}, 'ADJ-INDEP')
    variants('PRED:ADJ-N-CONFLICTED-CASE', 'identity strings compare under R6.RECON.29 (case and surrounding space '
                                           'ignored): the adjudicator RA (R\'s author ra), the adjudicator AMAYBAUM '
                                           '(the owner), the technical reviewer \' V\' (v): ADJ-INDEP',
             {'a': author('RA'), 'b': author(OWNERS[0].upper()), 'c': lambda fx, J: {'T': fx.T(' V')}},
             'ADJ-INDEP')
    fx = Fx()
    J = copy.deepcopy(fx.J)
    J['authorization']['author'] = OWNERS[0].capitalize()
    J['authorization']['adjudicator'] = 'J'
    got = conds(adj.authorization_problems(J, fx.landing_time, OWNERS))
    case('PRED:ADJ-AUTH-CASE', 'the owner check and the adjudicator equality compare under R6.RECON.29: a case variant '
                               'of the owner\'s login, and J for j, pass', got, got == [])
    variants('PRED:ADJ-N-OWNER-TECH-REVIEWER', 'the owner as technical reviewer (OD-4): ADJ-INDEP',
             {'a': lambda fx, J: {'T': fx.T(OWNERS[0])}}, 'ADJ-INDEP')


def substance_and_binding():
    def no_ground_for(fx, J):
        J['grounds'][0]['target'] = {'ref': dict(fx.vref), 'item': P}

    variants('PRED:ADJ-N-NO-SUBSTANCE', 'no ground for an adverse item, empty reasoning, evidence or method lacking a '
                                        'required git blob id, an extra ground: ADJ-SUBST (empty grounds: ADJ-FORM)',
             {'b': no_ground_for,
              'c': lambda fx, J: J['grounds'][0].update(reasoning=' '),
              'd': lambda fx, J: J['grounds'][0].update(evidence=[h40('b'), h40('d')]),
              'e': lambda fx, J: J.update(method='read ' + ' '.join([h40('a'), h40('c'), h40('b'), h40('d')])),
              'f': lambda fx, J: J['grounds'].append({'id': 'g9', 'target': {'ref': dict(fx.vref), 'item': P},
                                                      'reasoning': 'x', 'evidence': [h40('c'), h40('b'), h40('d')]})},
             'ADJ-SUBST')
    fx = Fx()
    J = copy.deepcopy(fx.J)
    J['grounds'] = []
    case('PRED:ADJ-N-NO-SUBSTANCE-A', 'grounds empty: ADJ-FORM', conds(adj.form_problems(J)),
         'ADJ-FORM' in conds(adj.form_problems(J)))

    def other_w(fx, J):
        W = copy.deepcopy(fx.W)
        W['sources'].append({'path': 'x/v2.json', 'blob_sha256': h64('e')})
        return {'reproduced': W}
    variants('PRED:ADJ-N-MISBIND', 'finding item, replacement or reassessment differ from A\'s; the witness does not '
                                   'reproduce (sources, adverse, disputed, original configuration); a reference does '
                                   'not resolve: ADJ-BIND',
             {'a': lambda fx, J: (J['finding'].update(item=P + ':x'), J['authorization']['finding'].update(item=P + ':x')),
              'b': lambda fx, J: (J.update(replacement=dict(fx.entry, path='verification/audits/rr/r2.json')),
                                  J['authorization'].update(replacement=dict(J['replacement']))),
              'c': lambda fx, J: J.update(reassessment={'path': 'verification/audits/plan/a0.json',
                                                        'blob_sha256': h64('5')}),
              'd': other_w,
              'e': lambda fx, J: J['witness'].update(adverse=[]),
              'f': lambda fx, J: J['witness'].update(disputed={'path': 'x/p.json', 'blob_sha256': h64('2')}),
              'g': lambda fx, J: J['witness'].update(original_configuration={'path': 'x/k2.json',
                                                                             'blob_sha256': h64('6')}),
              'h': lambda fx, J: {'resolves': lambda r: r.get('blob_sha256') != h64('4')}}, 'ADJ-BIND')
    fx = Fx()
    J = copy.deepcopy(fx.J)
    p_ref = {'path': 'x/p.json', 'blob_sha256': h64('0')}
    J['witness'].update({'class': 'lineage', 'edge': {'successor': dict(fx.qref), 'predecessor': dict(p_ref)}})
    W = dict(fx.W, **{'class': 'lineage', 'edge': {'successor': dict(fx.qref), 'predecessor': dict(p_ref)}})
    ok = conds(adj.self_consistency(J, W, lambda r: True))
    J2 = copy.deepcopy(J)
    J2['witness']['edge'] = {'successor': dict(fx.vref), 'predecessor': dict(p_ref)}
    bad = conds(adj.self_consistency(J2, W, lambda r: True))
    case('PRED:ADJ-P-LINEAGE', 'a lineage witness reproduces with the operative edge U -> P (#1605 sec. 6 rows adopted '
                               'with the U -> P edge); the edge {S, P} does not (ADJ-BIND)', {'U-P': ok, 'S-P': bad},
         ok == [] and bad == ['ADJ-BIND'])


def decision():
    fx = Fx()
    J1 = copy.deepcopy(fx.J)
    J2 = copy.deepcopy(fx.J)
    J2.update(author='j2', disposition='upheld', record_id='j2')
    for status, name, want in (('valid', 'PRED:ADJ-N-CONTRADICTED', True),
                               ('unknown', 'PRED:ADJ-N-CONTRADICTION-UNRESOLVABLE', True),
                               ('invalid', 'PRED:ADJ-N-CONTRADICTION-INVALID-IGNORED', False)):
        got = adj.contradiction_problems(J1, [(J2, status)])
        res = adj.adjudicated([J1], lambda J: adj.contradiction_problems(J, [(J2, status)]))
        case(name, 'a matching upheld adjudication %s: %s' % (status, 'ADJ-CONTRA, Adjudicated false' if want else
                                                               'no contradiction, Adjudicated true'),
             {'contra': conds(got), 'adjudicated': res}, bool(got) == want and res == (not want))
    J3 = copy.deepcopy(fx.J)
    J3['replacement'] = dict(J3['replacement'], path='verification/audits/rr2/r.json')
    case('PRED:ADJ-N-RENAMED-REPLACEMENT', 'a byte-identical replacement at another path matches the upheld '
                                           'adjudication (matching is by blob)', adj.matches(J3, J2), adj.matches(J3, J2))
    J4 = copy.deepcopy(fx.J)
    J4['replacement'] = dict(J4['replacement'], blob_sha256=h64('d'))
    case('PRED:ADJ-P-REVERSAL-NEW-REPLACEMENT', 'a replacement with another blob does not match the upheld '
                                                'adjudication', adj.matches(J4, J2), not adj.matches(J4, J2))
    J5 = copy.deepcopy(J2)
    J5['witness']['sources'] = [{'path': fx.vref['path'], 'blob_sha256': h64('0')}]
    case('PRED:ADJ-N-MATCH-DISJOINT-SOURCES', 'the same finding, replacement and disputed record with witness sources '
                                              'sharing no blob: no match, so no contradiction',
         {'match': adj.matches(J1, J5), 'contra': conds(adj.contradiction_problems(J1, [(J5, 'valid')]))},
         not adj.matches(J1, J5) and not adj.contradiction_problems(J1, [(J5, 'valid')]))
    rid = adj.record_id_problems(J1, fx.jref, [(fx.jref, J1), ({'path': 'x/j2.json', 'blob_sha256': h64('9')}, J2)])
    J2b = dict(J2, record_id='j1')
    dup = adj.record_id_problems(J1, fx.jref, [(fx.jref, J1), ({'path': 'x/j2.json', 'blob_sha256': h64('9')}, J2b)])
    case('PRED:ADJ-N-RECORD-ID', 'record_id unique among the adjudications in R*: another adjudication with the same '
                                 'record_id fails (ADJ-FORM)', {'unique': rid, 'duplicate': conds(dup)},
         rid == [] and conds(dup) == ['ADJ-FORM'])
    blocks = adj.upheld_blocks_nr5(dict(fx.entry), J1['witness'], dict(fx.finding), [J2])
    case('PRED:ADJ-N-UPHELD-THEN-NR5', 'a valid upheld adjudication makes NR-5 false for the replacement and witness it '
                                       'matches (OD-6)', blocks, blocks is True)


def dissents():
    fx = Fx()
    J = copy.deepcopy(fx.J)
    dv = {'path': 'verification/audits/rr/dv.review.json', 'blob_sha256': h64('a')}
    J['dissents_addressed'] = [{'ref': dict(dv), 'item': P + ':scientific_effect'}]
    docs = {fx.vref['blob_sha256']: {'reviewer': 'v'}, dv['blob_sha256']: {'reviewer': 'v'}}
    ans = adj.answered(J, lambda r: docs.get((r or {}).get('blob_sha256')))
    pre = [{'J': J, 'ref': dict(fx.jref), 'binds': True, 'landing_index': 5, 'answered': ans}]

    def run(reviews_of_j, dissents_on_r):
        return adj.strata(pre, lambda ref: reviews_of_j, dissents_on_r)

    def rv(reviewer, bad_item, idx):
        verd = [{'item': i, 'verdict': 'reject' if i == bad_item else 'accept'} for i in adj.item_ids(J)]
        return {'reviewer': reviewer, 'verdicts': verd, 'first_index': idx,
                'ref': {'path': 'x/%s.json' % reviewer, 'blob_sha256': h64('b')}}
    redissent = {'reviewer': 'v', 'item': P + ':scientific_effect', 'first_index': 7,
                 'review': {'path': 'x/dv2.json', 'blob_sha256': h64('c')}}
    first = {'reviewer': 'v', 'item': P + ':scientific_effect', 'first_index': 3, 'review': dict(dv)}
    o = run([rv('v', 'ground:g1', 8)], [first, redissent])
    case('PRED:ADJ-P-ADDRESSED-REDISSENT', 'v (answered) repeats the dissent on R and rejects ground:g1 after L(J): the '
                                           'review of J is exempt, J admitted, both dissent items disregarded',
         o, o['admitted'] and not o['blocking'] and len(o['disregarded']) == 2 and
         o['exempt_reviews'][adj._key(fx.jref)])
    o = run([], [first, dict(redissent, reviewer='x')])
    case('PRED:ADJ-N-NEW-DISSENTER', 'x (not answered) dissents on R after L(J): the dissent item blocks (ADJ-DISSENT)',
         o, o['admitted'] and len(o['blocking']) == 1 and o['blocking'][0]['reviewer'] == 'x')
    o = run([rv('x', 'ground:g1', 8)], [first])
    case('PRED:ADJ-N-DISSENT-ON-J', 'x (not answered) rejects ground:g1 of J after L(J): J is not admitted', o,
         not o['admitted'])
    vetoes = {i: run([rv('v', i, 8)], [first]) for i in ('authorization', 'binding', 'conflicts')}
    case('PRED:ADJ-N-ANSWERED-AUTH-VETO', 'v (answered, later than L(J)) rejects the item authorization, binding or '
                                          'conflicts: never exempt, J not admitted', vetoes,
         all(not o['admitted'] for o in vetoes.values()))
    o = run([rv('v', 'ground:g1', 5)], [first])
    case('PRED:ADJ-N-EXEMPT-NOT-LATER', 'v (answered) rejects ground:g1 in a review that is not later than L(J): not '
                                        'exempt, J not admitted', o, not o['admitted'])
    early = {'reviewer': 'v', 'item': P, 'first_index': 4, 'review': {'path': 'x/dv0.json', 'blob_sha256': h64('d')}}
    o = run([], [first, early])
    case('PRED:ADJ-N-DISSENT-NOT-LATER', 'a dissent item on R by v (answered) that is not later than L(J) and not '
                                         'addressed: not exempt, it blocks', o,
         o['admitted'] and o['blocking'] == [early])
    R = {'schema': 'oi-reconciliation/2', 'paths': [{'path': P}]}
    dvdoc = {'reviewer': 'v', 'reviewed': {}, 'verdicts': [{'item': P, 'verdict': 'accept'},
                                                           {'item': P + ':scientific_effect', 'verdict': 'dissent'}]}
    ok = adj.dissents_addressed_problems(J, [(dv, dvdoc)], R)
    J_bad = copy.deepcopy(J)
    J_bad['dissents_addressed'] = [{'ref': dict(dv), 'item': P}, {'ref': {'path': 'x/none.json',
                                                                         'blob_sha256': h64('e')}, 'item': P}]
    bad = adj.dissents_addressed_problems(J_bad, [(dv, dvdoc)], R)
    case('PRED:ADJ-N-DISSENTS-ADDRESSED', 'dissents_addressed names a review of R in R*(L(J)) and an item adverse in '
                                          'it; an accepted item, or a review not of R in R*(L(J)), fails (ADJ-FORM)',
         {'ok': ok, 'bad': bad}, ok == [] and len(bad) == 2 and conds(bad) == ['ADJ-FORM'])


def admission():
    fx = Fx()
    T = fx.T()
    cited = [dict(fx.jref, kind='adjudication'), dict(fx.tref, kind='review')]
    case('PRED:ADJ-ADMIT-OK', 'J cited with kind adjudication and exactly one qualifying review, both in R\'s '
                              'reconciliation directory', adj.citation_problems(cited, fx.jref, [fx.tref]) +
         adj.location_problems(fx.jref, [fx.tref], fx.J),
         not adj.citation_problems(cited, fx.jref, [fx.tref]) and not adj.location_problems(fx.jref, [fx.tref], fx.J))
    t2 = {'path': 'verification/audits/rr/j.review2.json', 'blob_sha256': h64('9')}
    two = adj.citation_problems(cited + [dict(t2, kind='review')], fx.jref, [fx.tref, t2])
    case('PRED:ADJ-N-TWO-REVIEWS-CITED', 'two qualifying reviews of J cited: ADJ-ADMIT', two, conds(two) == ['ADJ-ADMIT'])
    none = adj.citation_problems([dict(fx.tref, kind='review')], fx.jref, [fx.tref])
    case('PRED:ADJ-N-NOT-CITED', 'J not referenced with kind adjudication: ADJ-ADMIT', none,
         conds(none) == ['ADJ-ADMIT'])
    elsewhere = dict(fx.jref, path='verification/audits/plan/j.json')
    loc = adj.location_problems(elsewhere, [fx.tref], fx.J)
    case('PRED:ADJ-N-WRONG-LOCATION', 'J outside R\'s reconciliation directory: ADJ-ADMIT', loc,
         conds(loc) == ['ADJ-ADMIT'])
    # the dedicated landing (M5', OD-3) over an in-memory history
    repo = gitobj.Overlay()
    jb, tb = b'{"j": 1}\n', b'{"t": 1}\n'
    from ledger_coverage.engine import util
    jref = {'path': 'verification/audits/rr/j.json', 'blob_sha256': util.sha256(jb)}
    tref = {'path': 'verification/audits/rr/j.review.json', 'blob_sha256': util.sha256(tb)}
    c0 = repo.add_commit({'a.txt': b'a\n'}, [])
    c1 = repo.derive(c0, {jref['path']: jb, tref['path']: tb}, parents=[c0])
    c2 = repo.derive(c0, {jref['path']: jb, tref['path']: tb, 'b.txt': b'b\n'}, parents=[c0])
    ok, bad = adj.dedicated_landing_problems(repo, c1, jref, tref), adj.dedicated_landing_problems(repo, c2, jref, tref)
    # L(J): the earliest first-parent commit holding J with a qualifying review (a review lands one commit later)
    c3 = repo.derive(c0, {jref['path']: jb}, parents=[c0])
    c4 = repo.derive(c3, {tref['path']: tb}, parents=[c3])
    c5 = repo.derive(c4, {'c.txt': b'c\n'}, parents=[c4])
    lj = adj.landing(repo, c5, jref, lambda c: repo.read(c, tref['path']) is not None)
    none = adj.landing(repo, c5, jref, lambda c: False)
    case('PRED:ADJ-LANDING', 'L(J) is the earliest commit on M\'s first-parent chain holding J and a qualifying review; '
                             'none without a qualifying review', {'L': lj, 'want': c4, 'none': none},
         lj == c4 and none is None)
    case('PRED:ADJ-N-NOT-DEDICATED-LANDING', 'the commit introducing J also changes another file: ADJ-DEDICATED (a '
                                             'commit adding only J and its review passes)', {'ok': ok, 'bad': bad},
         ok == [] and conds(bad) == ['ADJ-DEDICATED'])
    del T


SUITES = [('form-authorization', form_and_authorization), ('independence', independence),
          ('substance-binding', substance_and_binding), ('decision', decision), ('dissents', dissents),
          ('admission', admission)]


def main(out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for name, fn in SUITES:
        try:
            fn()
        except Exception as exc:  # a suite that cannot run is a failed control of its own
            import traceback
            case(name + '/group-error', 'the suite runs', '%s: %s %s' % (type(exc).__name__, exc,
                                                                          traceback.format_exc()[-1500:]), False)
    with open(os.path.join(out, 'adjudication-controls.json'), 'w') as f:
        json.dump({'schema': 'oi-local-controls/1', 'suite': 'adjudication', 'cases': RESULTS}, f, indent=1,
                  sort_keys=True, default=str)
        f.write('\n')
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'adjudication-controls-out'))
