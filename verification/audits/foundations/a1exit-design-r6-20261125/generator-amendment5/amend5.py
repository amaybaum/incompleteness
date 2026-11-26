"""Generator of amendment 5 to design r6: the consolidated expectation correction (owner decision of
2026-11-26T08:28:18Z, #1169 comment 7186638587, items 8 and 9).

Usage: python3 -I -B amend5.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md as amendment 4 leaves them
(each checked against its sha256 below). The script reads owner-decisions-amendment5.json beside itself and writes
into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-5.md and the
updated LANDING-MANIFEST.md.

Every correction names its governing requirement (CORRECTIONS below). Self-checks: no requirement loses a control or
changes a field other than its controls and pending entries; every corrected row keeps every class its old
expectation required (in classes_include, classes_exact or a site), every old site, every old count and invariant or
its declared scoped form, its restored expectation and its outcome where the outcome was FAIL; every new row records
both directions; correspondence; the closed invariant vocabulary. Standard library only; deterministic.
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': '96cec7155e87bd8da46d24441285f4ce062b3f3bfe0dde91894965444ad96861',
    'EXPECTATIONS.json': 'bcf6857656443b4d99248ad97f50a1ac6ab06f9d7081486b6390b52c40a21ea3',
    'REQUIREMENTS.json': '6ceeb80394b0b8c1f128332cb962bce98fe0dfcc1927fa06de47a691312eba09',
    'LANDING-MANIFEST.md': 'ad48bc39edb29a615df822164016a3be07c228cbb0229574289583112316a7b9',
}
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'r6 amendment 5 (owner decision of 2026-11-26T08:28:18Z, #1169 comment 7186638587, item 9)'
FLAG = 'added by amendment 5; the tool records this id; the expectation follows from the design text'
MARK = '(amendment 5, sec. 0.6: pending independent review and the owner\'s acceptance)'
PENDING = ('amendment 5 (expectation correction): drafted under the owner\'s authorization of 2026-11-26T08:28:18Z '
           '(#1169 comment 7186638587, items 8 and 9); needs independent review and the owner\'s acceptance')
ADMITTED = {'outcome': 'ANY', 'invariants': [{'record_admitted': '$record'}, {'not_class': ['record-invalid']}]}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    c = text.count(old)
    if c != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, c))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def rb(rid, case, restored_case):
    r = {'id': rid, 'requirements': ['R6.RECON.2'], 'runner': None, 'operations': ['execution'],
         'expect': {'outcome': 'FAIL', 'classes_include': ['record-invalid']},
         'restored': dict(ADMITTED, invariants=ADMITTED['invariants'] + [{'baseline': restored_case}]),
         'source': SRC, 'flags': [FLAG]}
    return r, case


ON_M = 'the same record commit built with the run\'s M as its single parent'
NEW_ROWS = [
    ({'id': 'RB-P1', 'requirements': ['R6.RECON.2'], 'runner': None, 'operations': ['execution'], 'direction': 'both',
      'expect': {'cases': [
          {'case': 'a record commit whose single parent is the run\'s M and which adds one regular file in a '
                   'reconciliation directory (positive)', 'outcome': 'ANY',
           'invariants': [{'record_admitted': '$record'}, {'not_class': ['record-invalid']}]},
          {'case': 'countercase: the same record commit also changing a path its parent holds', 'outcome': 'FAIL',
           'classes_include': ['record-invalid']}]},
      'source': SRC, 'flags': [FLAG]},
     'the record commit of R6.RECON.2 (c): single parent the record base `M`, only reconciliation-directory files '
     'added; admitted'),
    rb('RB-C4', 'a record commit whose parent lies below the run\'s M across a change to a ledgered path', ON_M),
    rb('RB-C4b', 'a record commit whose parent lies below the run\'s M across a change to a corpus path', ON_M),
    rb('RB-C4c', 'a record commit whose parent lies below the run\'s M across a change to another path', ON_M),
    rb('RB-C4d', 'a record commit whose parent lies below the run\'s M across an added reconciliation record', ON_M),
    rb('RB-C4e', 'a record commit whose parent lies below the run\'s M across a merge', ON_M),
    rb('RB-C5', 'a record commit whose parent lies below the run\'s M across a change to a tool-landing pin', ON_M),
    rb('RB-C5b', 'a record commit whose parent lies below the run\'s M across the deletion of a tool-landing pin', ON_M),
    rb('RB-C7', 'a class record that the configuration does not pin, with prefixes over ledgered and corpus paths, '
                'named by --classify; the record commit\'s parent lies below M across a ledgered change', ON_M),
    rb('RB-C7b', 'the same unpinned class record; the record commit\'s parent lies below M across a corpus change',
       ON_M),
    rb('RB-C8', 'a plan record directory that is not an authorized record directory; the record commit\'s parent lies '
                'below M across a corpus change', ON_M),
    rb('RB-C10', 'a chain-admitted run whose record commit\'s parent is a commit below the run\'s M', ON_M),
    rb('RB-C11', 'a record commit that also changes a path its parent holds',
       'the same record commit adding only the reconciliation-directory file'),
    ({'id': 'LINE-PATCH-RC8', 'requirements': ['R6.RECON.13'], 'runner': None, 'operations': ['execution'],
      'direction': 'both', 'predicate_kind': 'procedural',
      'expect': {'cases': [
          {'case': 'the synthetic line-patch ledger stating expected_sha256 equal to the sha256 of the candidate\'s '
                   'patched bytes (positive)', 'outcome': 'RC_HOLDS'},
          {'case': 'countercase: the same ledger with a wrong expected_sha256', 'outcome': 'RC_FAILS',
           'invariants': [{'failed_conditions_include': 'RC8'}]}]},
      'procedure': {'name': 'line-patch-rc8', 'lib': 'oracle',
                    'tool_output': 'RC8 evaluation with the stated and with the wrong expected_sha256',
                    'oracle_output': 'sha256 of the candidate\'s patched bytes'},
      'source': SRC, 'flags': [FLAG]},
     'RC8 reads the ledger\'s `expected_sha256` (R6.RECON.13): with the value equal to the sha256 of the candidate\'s '
     'bytes RC8 holds; with another value it fails'),
]
NEW_IDS = [r['id'] for r, _ in NEW_ROWS]
NEW_REQ_CONTROLS = {}
for _r, _ in NEW_ROWS:
    for _q in _r['requirements']:
        NEW_REQ_CONTROLS.setdefault(_q, []).append(_r['id'])

# Corrections: row id -> (citation, new expect, declared scoped forms {old json: new json}, explanation)
P = '$planted'


def site(cls=None, **kw):
    d = {'subject': P}
    if cls is not None:
        d['classes_exact'] = cls
    d.update(kw)
    return d


CORRECTIONS = {}


def corr(rid, cite, expect, why, scoped=None, case_index=None):
    CORRECTIONS[rid] = {'cite': cite, 'expect': expect, 'why': why, 'scoped': scoped or {}, 'case': case_index}


corr('M1', 'R6.ANCH.9 (the file is FAIL `unauthorized-edit`, and its sites are then processed by the unledgered rules '
     'of R6.ANCH.17, which can add `unauthorized-change`)',
     {'outcome': 'FAIL', 'classes_include': ['unauthorized-edit']},
     'whole-file conformance FAILs the file; the file\'s sites may add further site classes')
corr('M2', 'R6.ANCH.9 (as for M1)', {'outcome': 'FAIL', 'classes_include': ['unauthorized-edit']},
     'as M1')
corr('B5', 'R6.ANCH.17 (the count changes: `duplicated`) and R6.CLASS.2 (`ambiguous` includes a disagreement between '
     'translation and search, which a replacement region made non-unique in `X` produces)',
     {'outcome': 'FAIL', 'classes_exact': ['ambiguous', 'duplicated']},
     'both labels follow from the design for this case')
corr('H5', 'R6.HP.9 and R6.HP.11 (the `RET` entry is FAIL `untracked-hp-overlap`; the `HP` entry keeps its own '
     'provenance status); R6.CLASS.4 (`untracked-hp-overlap` is reported in RET); R6.CLASS.10 lists only tree-role '
     'classes and does not name this class, so there is no conflict with it',
     {'outcome': 'FAIL', 'classes_include': ['untracked-hp-overlap'],
      'invariants': [{'items_include': [{'obligation': 'RET', 'class': 'untracked-hp-overlap'}]},
                     {'none': 'items[obligation=HP,class=untracked-hp-overlap]'}]},
     'the class is required under RET and forbidden under HP, as R6.HP.9 and R6.CLASS.4 state',
     scoped={json.dumps({'items_include': [{'obligation': 'HP', 'class': 'untracked-hp-overlap'},
                                           {'obligation': 'RET', 'class': 'untracked-hp-overlap'}]}, sort_keys=True):
             'the RET entry kept; the HP entry with this class contradicted R6.HP.9 and R6.CLASS.4 and is replaced by '
             'its absence'})
corr('U14', 'R6.REC.10 (an entry that names an existing subject but disagrees with it is decided by the subject\'s own '
     'rule, `provenance-mismatch`, not by the orphan rule); R6.HP.7 is corrected accordingly (sec. 0.6)',
     None, 'the second case requires `provenance-mismatch` alone at the site', case_index=1)
corr('Y4', 'R6.REC.13 (widening without review: FAIL `record-invalid`) and R6.PROF.3 with R6.CLASS.5 (the hit the '
     'rejected allow rule no longer holds is REVIEW_REQUIRED `unclassified`)',
     None, 'the second case requires both items the design specifies', case_index=1)
corr('S11-1', 'R6.PLAN.1 (a FAIL naming its class) and R6.ANCH.9 (`unauthorized-edit` for the reverted splice)',
     {'outcome': 'FAIL', 'classes_include': ['unauthorized-edit']},
     'the specified item is required; items of harness admission (delegated evidence) are governed elsewhere')
corr('S11-2a', 'R6.PLAN.4 (the unclassified new site at `E`); R6.PROF.4 (deny profiles do not run on `E`, so a '
     'deny-match on the mutant of `E` is a tool defect and the outcome stays REVIEW_REQUIRED)',
     {'outcome': 'REVIEW_REQUIRED', 'classes_include': ['unclassified'],
      'sites': [{'subject': '$new_line', 'classes_exact': ['unclassified']}]},
     'the specified site item is required; the outcome is unchanged')
corr('S11-5', 'R6.DENY.3 (a deny FAIL item carries the rule id) and R6.GATE.8 (the gate reads `items[]` with '
     '`rule_id`)',
     {'outcome': 'FAIL', 'classes_include': ['deny-match'],
      'invariants': [{'items_include': [{'class': 'deny-match', 'rule_id': 'register'}]}]},
     'the item field is `rule_id`',
     scoped={json.dumps({'items_include': [{'class': 'deny-match', 'profile': 'register'}]}, sort_keys=True):
             'the same item, named by its field `rule_id`'})
corr('S11-6', 'R6.DENY.3 and R6.GATE.8 (as for S11-5)',
     {'outcome': 'FAIL', 'classes_include': ['deny-match'],
      'invariants': [{'items_include': [{'class': 'deny-match', 'rule_id': 'infinity'}]}]},
     'the item field is `rule_id`',
     scoped={json.dumps({'items_include': [{'class': 'deny-match', 'profile': 'infinity'}]}, sort_keys=True):
             'the same item, named by its field `rule_id`'})
corr('R18', 'R6.TREE.5 (a pin that differs leaves the path `side-change-unclassified`), R6.TREE.7 and R6.RECON.16 '
     'as amended by amendment 3 (an unclassified side change fails RC11 for every entry, so every drifted ledgered '
     'path of the run stays `base-drift`)',
     {'outcome': 'FAIL', 'classes_include': ['side-change-unclassified', 'base-drift'],
      'sites': [{'subject': '$workflow_path', 'classes_include': ['side-change-unclassified']}]},
     're-derived for a run whose `M` carries drifted ledgered paths (as `main` does from eb3a69f4): the class pin '
     'mismatch also leaves the drifted paths `base-drift`, so the run FAILs')


def scoped_terms(kind):
    """The T1' whole-result rows: (expect builder, explanation)."""
    pass


T1P = {
    'WB1': ({'outcome': 'ANY', 'sites': [{'subject': 'ch19:198', 'state': 'PASS'},
                                         {'subject': 'book/The-Incompleteness-of-Observation-FULL.md:5270',
                                          'state': 'PASS'}]},
            'R6.RULE.4: the fingerprinted sentences PASS under their rule; both sites stay required'),
    'WB2': ({'outcome': 'FAIL', 'classes_include': ['rule-negative-match'], 'sites': [site(['rule-negative-match'])]},
            'R6.RULE.9: the edited sentence is `rule-negative-match`; exact at the planted sentence'),
    'WB6': ({'outcome': 'FAIL', 'classes_include': ['rule-negative-match'], 'sites': [site(['rule-negative-match'])]},
            'R6.RULE.4: the near-copy is `rule-negative-match`; exact at the planted sentence'),
    'WB7': ({'outcome': 'ANY', 'classes_include': ['rule-fingerprint-mismatch'],
             'sites': [site(['rule-fingerprint-mismatch'], decision='REVIEW_REQUIRED')]},
            'R6.RULE.4: the sentence without its `finit` word is REVIEW_REQUIRED `rule-fingerprint-mismatch`; exact at '
            'the planted sentence'),
    'WB8': ({'outcome': 'ANY', 'sites': [site(state='PASS')]},
            'R6.RULE.5: the shifted fingerprinted sentence PASSes; required at that sentence'),
    'WB11': ({'outcome': 'FAIL', 'classes_include': ['record-invalid'],
              'invariants': [{'items_include': [{'class': 'record-invalid', 'subject': '$rule_file'}]}]},
             'R6.REC.14: the rule file fails its own lint; `record-invalid` required for that rule file'),
    'WB12': ({'outcome': 'FAIL', 'classes_include': ['rule-negative-match'], 'sites': [site(['rule-negative-match'])],
              'invariants': [{'none': 'items[class=deny-match,subject=$planted]'}]},
             'R6.RULE.9: `rule-negative-match`, and no deny match, at the planted sentence'),
    'WB13': ({'outcome': 'ANY', 'sites': [site(state='PASS')],
              'invariants': [{'none': 'items[class=rule-stale,rule_id=$rule]'}]},
             'R6.RULE.5: the moved sentence PASSes and its rule is not stale'),
    'WB15': ({'outcome': 'FAIL', 'classes_include': ['rule-negative-match'], 'sites': [site(['rule-negative-match'])]},
             'R6.RULE.7: "Finiteness" makes the sentence `rule-negative-match`; exact at the planted sentence'),
    'V7a': ({'outcome': 'FAIL', 'classes_include': ['rule-negative-match'], 'sites': [site(['rule-negative-match'])],
             'invariants': [{'items_include': [{'class': 'rule-negative-match', 'rule_id': 'W1-d'}]}]},
            'R6.RULE.4, R6.RULE.7, R6.RULE.9: `rule-negative-match` by W1-d at the edited sentence'),
    'V7c': ({'outcome': 'ANY', 'classes_include': ['rule-fingerprint-mismatch'],
             'sites': [site(['rule-fingerprint-mismatch'], decision='REVIEW_REQUIRED')]},
            'R6.RULE.4: the edited W1 sentence is REVIEW_REQUIRED `rule-fingerprint-mismatch`'),
    'V15': ({'outcome': 'ANY', 'classes_include': ['unclassified'],
             'sites': [site(['unclassified'], decision='REVIEW_REQUIRED')],
             'invariants': [{'all': 'hits[subject=$planted]', 'have': {'profiles': ['resid']}}, {'resid_key': 'resid-a'}]},
            'R6.PROF.3, R6.DENY.4: the planted sentence is REVIEW_REQUIRED `unclassified`, hit by `resid` only, key '
            'resid-a'),
    'V21': ({'outcome': 'ANY', 'classes_include': ['unclassified'],
             'sites': [site(['unclassified'], decision='REVIEW_REQUIRED')],
             'invariants': [{'all': 'hits[subject=$planted]', 'have': {'profiles': ['resid']}}]},
            'R6.PROF.3, R6.DENY.4: as V15, without the key'),
    'V23': ({'outcome': 'FAIL', 'classes_include': ['final-unclassified'], 'sites': [site(['final-unclassified'])],
             'invariants': [{'none': 'items[class=deny-match,subject=$planted]'},
                            {'items_include': [{'class': 'final-unclassified', 'profile': 'ptr'}]}]},
            'R6.OUT.17: the reinstated line is `final-unclassified` by `ptr` and not a deny match'),
    'V24': ({'outcome': 'FAIL', 'classes_include': ['final-unclassified'], 'sites': [site(['final-unclassified'])],
             'invariants': [{'none': 'items[class=deny-match,subject=$planted]'},
                            {'items_include': [{'class': 'final-unclassified', 'profile': 'count-grep'}]}]},
            'R6.OUT.17: the added line is `final-unclassified` by `count-grep` and not a deny match'),
    'V27': ({'outcome': 'ANY', 'counts': {'hits[subject=$planted]': 0}, 'sites': [site(state='PASS')]},
            'R6.PUR.9, R6.DENY.6: the planted sentence has no hit and PASSes'),
    'V27-glossary': ({'outcome': 'ANY', 'counts': {'hits[subject=$planted]': 0}, 'sites': [site(state='PASS')]},
                     'R6.PUR.9, R6.DENY.6: the edited glossary line has no hit and PASSes'),
    'L2': ({'outcome': 'ANY', 'invariants': [{'all': 'lines[rule=W2]', 'have': {'state': 'PASS'}}]},
           'R6.RULE.4, R6.RULE.7, R6.HIT.1: every W2 line PASSes after the move'),
    'RT-D': (None, 'R6.DENY.1, R6.PROF.3, R6.HIT.2, R6.HIT.3: the corpus-wide counts (no deny match, 11 W1/W2 PASS lines, '
             '45 resid REVIEW lines, 17 resid-only lines) and the GR.md:58 site are kept; the whole-result class set '
             'and outcome are dropped'),
    'item11-T1p': (None, 'R6.PLAN.12: 176 `final-unclassified` lines required; the class set becomes inclusive'),
}
# Scoped forms of whole-result invariants and counts, declared (old -> new) for the self-check
T1P_SCOPED = {
    ('WB12', json.dumps({'none': 'items[class=deny-match]'}, sort_keys=True)): 'items[class=deny-match,subject=$planted]',
    ('WB13', json.dumps({'none': 'items[class=rule-stale]'}, sort_keys=True)): 'items[class=rule-stale,rule_id=$rule]',
    ('V15', json.dumps({'all': 'hits', 'have': {'profiles': ['resid']}}, sort_keys=True)): 'hits[subject=$planted]',
    ('V21', json.dumps({'all': 'hits', 'have': {'profiles': ['resid']}}, sort_keys=True)): 'hits[subject=$planted]',
    ('V23', json.dumps({'none': 'items[class=deny-match]'}, sort_keys=True)): 'items[class=deny-match,subject=$planted]',
    ('V24', json.dumps({'none': 'items[class=deny-match]'}, sort_keys=True)): 'items[class=deny-match,subject=$planted]',
    ('V27', 'count:hits'): 'hits[subject=$planted]', ('V27-glossary', 'count:hits'): 'hits[subject=$planted]',
}
# The one class an old expectation required that the design, once its contradiction is resolved, forbids: R6.HP.7
# against R6.REC.10 (sec. 0.6). The self-check allows exactly this removal and no other.
DESIGN_RESOLVED = {('U14', 'stale-adjudication')}
UNCHANGED_T1P = {'RT-D-gr58': 'already scoped: its expectation names only the GR.md:58 site with outcome ANY'}

RTL2_POS = {'case': "a reviewed reconciliation record bound to the run: ledger_base the run's H, naming the run's M and "
                    "X, its m and x the path's blobs at the run's M and C (positive: drift reconciled; REVIEW_REQUIRED "
                    "only from delegated classes)",
            'outcome': 'ANY',
            'invariants': [{'drift_state_in': ['reconciled']}, {'none': 'items[decision=FAIL]'},
                           {'all': 'items[decision=REVIEW_REQUIRED]', 'have': {'class': 'delegated-evidence-missing'}}]}
RTL2_EXTRA = {'case': 'countercase: the same reconciled drift with an unclassified side change beside it (REVIEW_REQUIRED '
                      'side-change-unclassified, not a delegated class)',
              'outcome': 'REVIEW_REQUIRED', 'invariants': [{'rt_l2_status': 'FAIL'}]}


def amend_expectations(E):
    E = copy.deepcopy(E)
    by = {r['id']: r for r in E['rows']}
    changes = []
    for rid, cdef in CORRECTIONS.items():
        r = by[rid]
        if cdef['case'] is None:
            r['expect'] = copy.deepcopy(cdef['expect'])
        elif rid == 'U14':
            c = r['expect']['cases'][1]
            c['sites'] = [{'subject': '$site', 'classes_exact': ['provenance-mismatch']}]
        elif rid == 'Y4':
            c = r['expect']['cases'][1]
            c['classes_exact'] = ['record-invalid', 'unclassified']
        changes.append((rid, cdef['cite'], cdef['why']))
    for rid, (exp, why) in T1P.items():
        r = by[rid]
        if exp is not None:
            r['expect'] = copy.deepcopy(exp)
        elif rid == 'RT-D':
            r['expect'].pop('classes_exact')
            r['expect']['classes_include'] = ['unclassified']
            r['expect']['outcome'] = 'ANY'
        elif rid == 'item11-T1p':
            r['expect'].pop('classes_exact')
            r['expect']['classes_include'] = ['final-unclassified']
        changes.append((rid, why.split(':')[0], why))
    rt = by['RTL2-BIND']
    if rt['expect']['cases'][0]['outcome'] != 'PASS':
        raise SystemExit('RTL2-BIND positive case differs from the base')
    rt['expect']['cases'][0] = copy.deepcopy(RTL2_POS)
    rt['expect']['cases'].append(copy.deepcopy(RTL2_EXTRA))
    changes.append(('RTL2-BIND', 'R6.RECON.21 (drift state reconciled; every side change classified), R6.TREE.12 '
                    '(a generated artifact is REVIEW_REQUIRED `delegated-evidence-missing` until regenerated)',
                    'positive case: drift reconciled, no FAIL item, REVIEW_REQUIRED only from the delegated class; '
                    'countercases kept, one added for a non-delegated REVIEW item'))
    for r, _ in NEW_ROWS:
        if r['id'] in by:
            raise SystemExit('id %s already a row' % r['id'])
        E['rows'].append(copy.deepcopy(r))
    return E, changes


def amend_requirements(R):
    R = copy.deepcopy(R)
    by = {q['id']: q for q in R}
    for rid, ctl in sorted(NEW_REQ_CONTROLS.items()):
        q = by[rid]
        if set(ctl) & set(q['controls']):
            raise SystemExit('%s: controls' % rid)
        q['controls'] = q['controls'] + ctl
        q['pending_owner_confirmation'] = q['pending_owner_confirmation'] + [PENDING]
    by['R6.HP.7']['pending_owner_confirmation'] = by['R6.HP.7']['pending_owner_confirmation'] + [PENDING]
    return R


def table_row(r, case):
    d = r.get('direction', 'adversarial')
    dirs = {'adversarial': 'adv +restored', 'both': 'both'}[d]
    kind = 'proc' if r.get('predicate_kind') == 'procedural' else 'decl'
    return '| %s | %s | to be implemented (tool revision) | %s | %s | %s (amendment 5) |' % (
        r['id'], ', '.join(r['requirements']), kind, dirs, case)


COUNTS = ''


def counts_text(E):
    rows = [r for r in E['rows'] if not r['id'].startswith(('MUT:', 'GATE-'))]

    def dof(r):
        d = r.get('direction', 'adversarial')
        return d.get('of') if isinstance(d, dict) else d
    n_out = sum(1 for r in rows if isinstance(r.get('direction'), dict) and 'scope' in r['direction'])
    n_ex = sum(1 for r in rows if isinstance(r.get('direction'), dict) and r['direction'].get('exempt') == 'observation')
    return ('%d rows, %d of them recording `scope: "outside"`; %d carry a `restored` expectation, %d declare '
            'direction `both`, %d name `paired_with`, %d are exempt as observations'
            % (len(rows), n_out, sum(1 for r in rows if r.get('restored') is not None),
               sum(1 for r in rows if dof(r) == 'both'), sum(1 for r in rows if r.get('paired_with')), n_ex))


HP7_OLD = ("differs from the walk (U14's second case) gives FAIL `provenance-mismatch`, because the record does\n"
           "not match the walk, and FAIL `stale-adjudication`, because the entry then resolves no subject\n"
           "(R6.REC.10); any other class emitted for that case is a defect (Q12, RE-7).")
HP7_NEW = ("differs from the walk (U14's second case) gives FAIL `provenance-mismatch`, because the record does\n"
           "not match the walk, and no `stale-adjudication`: the entry names an existing site, and R6.REC.10 decides\n"
           "such an entry by the site's own rule, not as an entry that resolves no subject; any other class emitted\n"
           "for that case is a defect (Q12, RE-7) %s." % MARK)


def note(owner):
    d = owner['decisions'][0]
    out = ['', '### 0.6 Amendment 5 of 2026-11-26', '',
           'The owner decided at %s (%s, %s, relayed by the %s). Excerpt of items 8 and 9, in the order of the source '
           '(table cells joined by " | ", table padding removed; headings left out; each line prefixed by "> "; '
           '"[...]" marks text left out):' % (d['record'], d['author'], d['time'], d['relayed_by']), '',
           '\n>\n'.join('> ' + (x if x is not None else '[...]') for x in d['quotes']), '',
           'Amendment 5 corrects expectations only where the design requires it, each correction citing its governing '
           'requirement (AMENDMENT-5.md sec. 2), adds the 14 rows the tool records (RB-P1, RB-C4 to RB-C11, '
           'LINE-PATCH-RC8), and resolves one contradiction in the design: R6.HP.7 required `stale-adjudication` for an '
           'adjudication entry that names an existing HP site but disagrees with its walk, while R6.REC.10 decides such '
           'an entry by the site\'s own rule. R6.HP.7 is corrected to agree with R6.REC.10, and U14\'s second case '
           'follows. The whole-result rows on `T1\'` are scoped to the lines or subjects they plant or name; their '
           'obligation at those subjects is kept exactly (AMENDMENT-5.md sec. 3). No requirement is weakened and no '
           'row loses an obligation; amendment 5 is pending independent review and the owner\'s acceptance.', '']
    return '\n'.join(out)


def amend_design(t, owner):
    t = once(t, HP7_OLD, HP7_NEW, 'R6.HP.7')
    t = once(t, "Sources: E-1341, RV-027. Controls: O8, N2, POSTF-1, POSTF-2, POSTF-3, POSTF-4, POSTF-5, RECORD-BASE.",
             "Sources: E-1341, RV-027. Controls: O8, N2, POSTF-1, POSTF-2, POSTF-3, POSTF-4, POSTF-5, RECORD-BASE, %s."
             % ', '.join(i for i in NEW_IDS if i.startswith('RB-')), 'R6.RECON.2 controls')
    t = once(t, "Sources: E-1349. Controls: N15.", "Sources: E-1349. Controls: N15, LINE-PATCH-RC8.", 'R6.RECON.13')
    t = once(t, "adds 9 rows (sec. 0.4), and amendment 4 adds 3 rows (sec. 0.5), each with one. Counted",
             "adds 9 rows (sec. 0.4), amendment 4 adds 3 rows (sec. 0.5), and amendment 5 adds %d rows (sec. 0.6),\n"
             "each with one. Counted" % len(NEW_ROWS), 'R6.CTRL.3 rows')
    m = re.search(r"\(\d+ rows, \d+ of them recording `scope: \"outside\"`; \d+ carry a `restored` expectation, \d+ "
                  r"declare direction `both`, \d+ name `paired_with`, \d+ are exempt as observations\)", t)
    if not m or t.count(m.group(0)) != 1:
        raise SystemExit('R6.CTRL.3 counts')
    t = t.replace(m.group(0), '(%s)' % COUNTS)
    anchor = [x for x in re.finditer(r'^\| RECORD-BASE \| [^\n]*$', t, re.M)]
    if len(anchor) != 1:
        raise SystemExit('RECORD-BASE table row')
    t = t[:anchor[0].end()] + '\n' + '\n'.join(table_row(r, c) for r, c in NEW_ROWS) + t[anchor[0].end():]
    a = t.index('### 0.5 Amendment 4 of 2026-11-26')
    b = t.index('\n***\n\n## 1. Notation and symbols', a)
    t = t[:b] + '\n' + note(owner) + t[b:]
    return t


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def classes_required(e):
    out = set(e.get('classes_exact', [])) | set(e.get('classes_include', []))
    for s in e.get('sites', []):
        out |= set(s.get('classes_exact', [])) | set(s.get('classes_include', []))
    return out


def keeps_obligation(rid, old, new):
    """Every class, site, count and invariant of the old expectation is kept, or kept in its declared scoped form."""
    probs = []
    lost = classes_required(old) - classes_required(new) - {c for r, c in DESIGN_RESOLVED if rid.split('/')[0] == r}
    if lost:
        probs.append('%s: classes %s not all kept' % (rid, sorted(lost)))
    if old.get('outcome') == 'FAIL' and new.get('outcome') != 'FAIL':
        probs.append('%s: FAIL outcome dropped' % rid)
    for s in old.get('sites', []):
        if not any(all(n.get(k) == v or (k == 'subject' and v.startswith('$')) for k, v in s.items()
                       if k not in ('classes_exact',)) for n in new.get('sites', [])):
            probs.append('%s: site %s dropped' % (rid, s))
    newinv = [json.dumps(i, sort_keys=True) for i in new.get('invariants', [])]
    for inv in old.get('invariants', []):
        j = json.dumps(inv, sort_keys=True)
        if j in newinv:
            continue
        sc = T1P_SCOPED.get((rid, j)) or CORRECTIONS.get(rid, {}).get('scoped', {}).get(j)
        if sc is None or not any(sc in x for x in newinv) and not isinstance(sc, str):
            probs.append('%s: invariant %s dropped' % (rid, j))
        elif isinstance(sc, str) and sc.startswith(('items[', 'hits[')) and not any(sc in x for x in newinv):
            probs.append('%s: invariant %s not in its scoped form %s' % (rid, j, sc))
    for k, v in (old.get('counts') or {}).items():
        if (new.get('counts') or {}).get(k) == v:
            continue
        sc = T1P_SCOPED.get((rid, 'count:' + k))
        if sc is None or (new.get('counts') or {}).get(sc) != v:
            probs.append('%s: count %s dropped' % (rid, k))
    return probs


def self_checks(E0, E, R0, R, t):
    problems = []
    r0 = {r['id']: r for r in E0['rows']}
    r1 = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    corrected = set(CORRECTIONS) | set(T1P) | {'RTL2-BIND'}
    for rid, r in r0.items():
        if rid in corrected:
            continue
        if r1.get(rid) != r:
            problems.append('row %s changed without a correction' % rid)
    for rid in corrected:
        a, b = r0[rid], r1[rid]
        for f in a:
            if f not in ('expect',) and a[f] != b.get(f):
                problems.append('%s: field %s changed' % (rid, f))
        if 'cases' in a['expect']:
            ca, cb = a['expect']['cases'], b['expect']['cases']
            if len(cb) < len(ca):
                problems.append('%s: a case dropped' % rid)
            for x, y in zip(ca, cb):
                problems += keeps_obligation('%s/%s' % (rid, x.get('case', '')[:30]), x, y)
        else:
            problems += keeps_obligation(rid, a['expect'], b['expect'])
    for rid, q in {q['id']: q for q in R0}.items():
        q1 = reqs[rid]
        if q1['controls'][:len(q['controls'])] != q['controls']:
            problems.append('requirement %s lost or reordered a control' % rid)
        for f in q:
            if f not in ('controls', 'pending_owner_confirmation') and q[f] != q1[f]:
                problems.append('requirement %s field %s changed' % (rid, f))
    vocab = vocabulary(t)

    def walk(rid, e):
        if not e:
            return
        for inv in e.get('invariants', []):
            for k in inv:
                if k not in vocab:
                    problems.append('%s: invariant key %s outside the vocabulary' % (rid, k))
        for c in e.get('cases', []):
            walk(rid, c)
    for rid in corrected | set(NEW_IDS):
        walk(rid, r1[rid]['expect'])
        walk(rid, r1[rid].get('restored'))
    for r, _ in NEW_ROWS:
        if r.get('direction') != 'both' and r.get('restored') is None:
            problems.append('%s: no second direction' % r['id'])
        for q in r['requirements']:
            if r['id'] not in reqs[q]['controls']:
                problems.append('%s lists %s, which does not name it' % (r['id'], q))
    for q, ctl in NEW_REQ_CONTROLS.items():
        start = t.index('**%s**' % q)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        cl = t[start:nxt.start()].split('Controls:')[-1]
        for c in ctl:
            if not re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % re.escape(c), cl):
                problems.append('%s: DESIGN Controls line does not name %s' % (q, c))
    return problems


def change_record(owner, outs, gen_sha, owner_sha, changes):
    d = owner['decisions'][0]
    lines = ['# r6 amendment 5: change record', '',
             'Owner decision: %s, %s (%s), items 8 and 9, quoted as an excerpt in DESIGN-r6.md sec. 0.6. Generated by '
             'generator-amendment5/amend5.py (sha256 %s) from the amendment-4 outputs and '
             'generator-amendment5/owner-decisions-amendment5.json (sha256 %s). The conflicts are those the tool '
             'writer listed (IMPLEMENTATION-PLAN-r6.md, sec. 15, on branch tools/a1-ledger-coverage-r6 at 1caba1c8, '
             'provenance); each correction below follows from the cited requirement, not from the tool\'s output. '
             'Amendment 5 is a draft; it needs independent review and the owner\'s acceptance.'
             % (d['author'], d['time'], d['record'], gen_sha, owner_sha), '',
             '## 1. Rows added', '', '| Row | Requirement | Case |', '|---|---|---|'] + \
        ['| %s | %s | %s |' % (r['id'], ', '.join(r['requirements']), c) for r, c in NEW_ROWS] + ['',
             'The RB rows test the record commit of R6.RECON.2 (c) without `--record-base`, where the record base is the '
             'run\'s `M`; amendment 4\'s RECORD-BASE row tests the `--record-base M0` route. The ids are the tool\'s, so '
             'they are kept as rows of their own rather than folded into RECORD-BASE, whose cases name a different '
             'route; no case is duplicated.', '',
             '## 2. Rows corrected, with the governing requirement', '', '| Row | Citation | Change |', '|---|---|---|'] + \
        ['| %s | %s | %s |' % c for c in changes] + ['',
             '## 3. The scoped rows on T1\', and why each obligation is preserved', '',
             'Each row\'s obligation is the decision its requirement assigns to the line, sentence or subject the row '
             'plants or names. The scoped expectation keeps that decision exactly at that subject (`sites` with '
             '`classes_exact`, `state` or `decision`; per-subject invariants and counts), keeps every class the old '
             'expectation required, keeps a FAIL outcome where the planted class is a FAIL class, keeps every old '
             'invariant or count in a form restricted to the planted subject, and keeps the restored case (the same run '
             'on the unmutated tree equal to the clean result), which together establish that the mutation, and only it, '
             'produces the decision. What is dropped is only the claim that no other line of the real tree carries an '
             'item, which those lines\' own controls (RT-D, RT-T0, the item checks) govern. The generator checks each '
             'row mechanically.', ''] + \
        ['- %s: %s.' % (rid, why) for rid, (_, why) in T1P.items()] + \
        ['- %s: %s.' % (rid, why) for rid, why in UNCHANGED_T1P.items()] + ['',
             '## 4. Design contradiction resolved', '',
             'R6.HP.7 stated:', '', '> ' + HP7_OLD.replace('\n', ' '), '',
             'R6.REC.10 states that an entry naming an existing subject but disagreeing with it "is decided by the '
             'subject\'s own rule (for example `provenance-mismatch` ...), not by this rule". R6.HP.7 now reads:', '',
             '> ' + HP7_NEW.replace('\n', ' '), '',
             'and U14\'s second case requires `provenance-mismatch` alone at the site.', '',
             '## 5. Open points', '',
             '- S11-2a: the tool reports a deny match on the mutant of `E`; R6.PROF.4 does not run deny profiles on `E`, '
             'so this stays a tool defect and the row\'s outcome REVIEW_REQUIRED is unchanged.',
             '- R18 is re-derived for a run whose `M` carries drifted ledgered paths; on an `M` without drift its '
             'outcome would be REVIEW_REQUIRED, which this row does not test.',
             '- The scoped rows bind `$planted` (and `$rule`, `$rule_file`, `$new_line`, `$workflow_path`); the runners '
             'must record these bindings.', '',
             '## 6. Outputs', '', '| File | sha256 |', '|---|---|']
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json'):
        lines.append('| %s | %s |' % (n, sha(outs[n])))
    lines.append('')
    return '\n'.join(lines)


def manifest(m, outs, gen_sha, owner_sha):
    for n, label in (('DESIGN-r6.md', 'final r6 document (the design)'),
                     ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
                     ('REQUIREMENTS.json', 'final r6 document (requirement index)')):
        mm = [x for x in re.finditer(r'^\| %s \| [^\n]*$' % re.escape(n), m, re.M)]
        if len(mm) != 1:
            raise SystemExit('manifest row %s' % n)
        m = m[:mm[0].start()] + '| %s | %s | amendment-5 output | %s |' % (n, label, sha(outs[n])) + m[mm[0].end():]
    rows = ('| AMENDMENT-5.md | change record of amendment 5 | amendment-5 output | %s |\n'
            '| generator-amendment5/amend5.py | amendment-5 generator | amendment-5 generator | %s |\n'
            '| generator-amendment5/owner-decisions-amendment5.json | amendment-5 generator input (the owner decision '
            'quoted) | amendment-5 generator | %s |\n' % (sha(outs['AMENDMENT-5.md']), gen_sha, owner_sha))
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | amendment-4 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-5 output | (this file) |', 'manifest self')
    para = ('\nAmendment 5 (owner decision of 2026-11-26T08:28:18Z, amaybaum, #1169 comment 7186638587, items 8 and 9, '
            'quoted in DESIGN-r6.md sec. 0.6): DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json are amended, and '
            'AMENDMENT-5.md records the changes. Recipe: run the amendment-4 recipe into `out4/` and run `python3 -I -B '
            'generator-amendment5/amend5.py out4 out5`. It checks the four files against their sha256, exits 0 and '
            'writes into `out5/` the files of sec. 1 marked "amendment-5 output" with the sha256 stated and this '
            'manifest.\n')
    m = once(m, '\n## 2. Files left to Git history', para + '\n## 2. Files left to Git history', 'manifest recipe')
    return m


def main():
    global COUNTS
    if len(sys.argv) != 3:
        sys.stderr.write('usage: amend5.py BASE OUT\n')
        return 64
    base, out = sys.argv[1], sys.argv[2]
    data = {}
    for n, h in BASE_SHA256.items():
        with open(os.path.join(base, n), 'rb') as f:
            data[n] = f.read()
        if sha(data[n]) != h:
            sys.stderr.write('%s: sha256 %s, expected %s\n' % (n, sha(data[n]), h))
            return 65
    with open(os.path.join(HERE, 'owner-decisions-amendment5.json'), 'rb') as f:
        owner_b = f.read()
    owner = json.loads(owner_b)
    E0 = json.loads(data['EXPECTATIONS.json'])
    R0 = json.loads(data['REQUIREMENTS.json'])
    E, changes = amend_expectations(E0)
    R = amend_requirements(R0)
    COUNTS = counts_text(E)
    t = amend_design(data['DESIGN-r6.md'].decode('utf-8'), owner)
    problems = self_checks(E0, E, R0, R, t)
    if problems:
        sys.stderr.write('self-check failures:\n' + '\n'.join(problems) + '\n')
        return 1
    outs = {'DESIGN-r6.md': t.encode('utf-8'), 'EXPECTATIONS.json': dumpj(E), 'REQUIREMENTS.json': dumpj(R)}
    with open(os.path.join(HERE, 'amend5.py'), 'rb') as f:
        gen_sha = sha(f.read())
    outs['AMENDMENT-5.md'] = change_record(owner, outs, gen_sha, sha(owner_b), changes).encode('utf-8')
    outs['LANDING-MANIFEST.md'] = manifest(data['LANDING-MANIFEST.md'].decode('utf-8'), outs, gen_sha,
                                           sha(owner_b)).encode('utf-8')
    os.makedirs(out, exist_ok=True)
    for n, b in sorted(outs.items()):
        with open(os.path.join(out, n), 'wb') as f:
            f.write(b)
        print('%s %s' % (sha(b), n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
