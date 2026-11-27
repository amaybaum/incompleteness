# Formal adjudication of retained witnesses (design r4 of PR #1605 at its adopted head, adopted with OD-1 to OD-7 at
# their defaults): the mechanical predicates of R6.ADJ.1 to R6.ADJ.14 over explicit
# records.
#
# The #1605 sec. 6 amendment rows are adopted with the lineage witness edge read as U -> P (owner decision of
# 2026-11-27). A run calls `evaluate` for each discharge D and custody witness W
# (category3.custody_decisions): the configuration kind row `adjudication` (config.py), the review item ids
# (records.item_ids), the R6.REC.3 owner check (authorization_problems), R6.REC.4/.5 reading of unreferenced
# adjudications in R* (Cumulative.adjudications, for R6.ADJ.9's contradiction and upheld rules), route 2 in the decision
# (obl29.decide `adjudicated`) and the result field `adjudications` (R6.ADJ.13).
#
# In a control-harness run, which has no freeze, the candidate freeze F' of ADJ-LANDED is the configuration's commit.
# Clearing uses the run's whole R*. Adverse use evaluates qualifying reviews and parties at the adjudication's landing.
# R6.ADJ.12's eligible dissent items are collected per witness here. Category 3 combines them per discharge
# and verifies R6.REC.6 and all relying witnesses before the disregard can affect the result.
import posixpath
import re
from datetime import datetime, timezone

from . import findings as fd
from . import obl29
from . import category3 as c3
from . import util

schema = 'oi-adjudication/1'
_time = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?Z$')
_hex40 = re.compile(r'^[0-9a-f]{40}$')
_ground_id = re.compile(r'^\S+$')

item_ref_keys = {'ref': (('keyed', fd.ref_keys), True), 'item': ('nestr', True)}
authorization_keys = {'quote': ('nestr', True), 'author': ('identity', True), 'time': ('nestr', True),
                 'source': ('nestr', True), 'adjudicator': ('identity', True),
                 'finding': (('keyed', c3.reassess_finding_keys), True),
                 'witness_sources': (('nearray', ('keyed', fd.ref_keys)), True),
                 'replacement': (('keyed', c3.reassess_entry_keys), True)}
edge_keys = {'successor': (('keyed', fd.ref_keys), True), 'predecessor': (('keyed', fd.ref_keys), True)}
witness_keys = {'class': (('lit', ('review', 'lineage')), True), 'disputed': (('keyed', fd.ref_keys), True),
           'edge': (('or', ('null',), ('keyed', edge_keys)), True), 'sources': (('nearray', ('keyed', fd.ref_keys)), True),
           'adverse': (('arr', ('keyed', item_ref_keys)), True), 'original_configuration': (('keyed', fd.ref_keys), True)}
ground_keys = {'id': ('nestr', True), 'target': (('keyed', item_ref_keys), True), 'reasoning': ('nestr', True),
          'evidence': (('nearray', 'blob'), True)}
RECORD = {'schema': (('lit', (schema,)), True), 'record_id': ('nestr', True), 'supersedes': (('null',), True),
          'author': ('identity', True), 'authorization': (('keyed', authorization_keys), True),
          'finding': (('keyed', c3.reassess_finding_keys), True), 'witness': (('keyed', witness_keys), True),
          'replacement': (('keyed', c3.reassess_entry_keys), True), 'reassessment': (('keyed', fd.ref_keys), True),
          'dissents_addressed': (('arr', ('keyed', item_ref_keys)), True),
          'disposition': (('lit', ('cleared', 'upheld')), True), 'grounds': (('nearray', ('keyed', ground_keys)), True),
          'method': ('nestr', True), 'conflicts': ('nestr', True)}
fixed_items = ('authorization', 'binding', 'dissents', 'disposition', 'conflicts')
never_exempt = ('authorization', 'binding', 'conflicts')


def _key(x):
    import json
    return json.dumps(x, sort_keys=True)


def _dups(arr):
    keys = [_key(x) for x in arr or []]
    return len(keys) != len(set(keys))


def parse_time(s):
    if not isinstance(s, str) or not _time.match(s):
        return None
    fmt = '%Y-%m-%dT%H:%M:%SZ' if s.count(':') == 2 else '%Y-%m-%dT%H:%MZ'
    try:
        return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


# ---- R6.ADJ.2 and R6.ADJ.14: form ------------------------------------------------------------------------------

def form_problems(J):
    # [(condition, message)] of R6.ADJ.2's closed key tables: ADJ-AUTH-FORM for the authorization object, ADJ-FORM for
    # the rest (with the no-duplicate arrays, `edge` non-null exactly for a lineage witness, unique ground ids without
    # whitespace, and a time of R6.RECON.29's encoding).
    out = []
    if not isinstance(J, dict):
        return [('ADJ-FORM', 'not an object')]
    tmp = []
    fd.validate({k: v for k, v in RECORD.items() if k != 'authorization'}, {k: v for k, v in J.items()
                                                                          if k != 'authorization'}, '$', tmp)
    out += [('ADJ-FORM', x) for x in tmp]
    if 'authorization' not in J:
        out.append(('ADJ-AUTH-FORM', '$.authorization: missing'))
    else:
        tmp = []
        fd.validate(authorization_keys, J['authorization'], '$.authorization', tmp)
        if isinstance(J['authorization'], dict) and parse_time(J['authorization'].get('time')) is None:
            tmp.append('$.authorization.time: not a time (yyyy-mm-ddThh:mm[:ss]Z)')
        out += [('ADJ-AUTH-FORM', x) for x in tmp]
    w = J.get('witness') if isinstance(J.get('witness'), dict) else {}
    if isinstance(w.get('class'), str) and (w.get('edge') is None) == (w.get('class') == 'lineage'):
        out.append(('ADJ-FORM', '$.witness.edge: non-null exactly when the class is lineage'))
    for k, arr in (('witness.sources', w.get('sources')), ('witness.adverse', w.get('adverse')),
                   ('dissents_addressed', J.get('dissents_addressed'))):
        if isinstance(arr, list) and _dups(arr):
            out.append(('ADJ-FORM', '$.%s: a duplicate element' % k))
    ids = [g.get('id') for g in J.get('grounds') or [] if isinstance(g, dict)]
    if len(ids) != len(set(map(str, ids))):
        out.append(('ADJ-FORM', '$.grounds: a ground id occurs more than once'))
    if any(isinstance(i, str) and not _ground_id.match(i) for i in ids):
        out.append(('ADJ-FORM', '$.grounds: a ground id holds whitespace'))
    return out


def detection_shape_problems(J):
    # R6.ADJ.14: no key `reviewed` or `verdicts` and no `schema` value beginning `oi-review-record/` or
    # `oi-reconciliation/` at any depth. A record that violates it is classed by R6.RECON.35 as it stands (this
    # function only reports the shape).
    out = []

    def walk(x, where):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ('reviewed', 'verdicts'):
                    out.append('%s.%s: a key the category-3 scan reads' % (where, k))
                if k == 'schema' and isinstance(v, str) and v.startswith(('oi-review-record/', 'oi-reconciliation/')):
                    out.append('%s.schema: a schema value the category-3 scan selects' % where)
                walk(v, '%s.%s' % (where, k))
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, '%s[%d]' % (where, i))
    walk(J, '$')
    return out


def record_id_problems(J, jref, adjudications, visible=lambda ref: True):
    # R6.ADJ.2 uniqueness among the adjudications in the applicable R*. Reported as ADJ-FORM.
    rid = J.get('record_id') if isinstance(J, dict) else None
    others = [r for r, d in adjudications if r != jref and isinstance(d, dict) and d.get('record_id') == rid
              and visible(r)]
    return [('ADJ-FORM', 'record_id %r is also the record_id of %s' % (rid, others[0].get('path')))] if others else []


def dissents_addressed_problems(J, reviews_of_R, R):
    # R6.ADJ.2 acceptance of `dissents_addressed`: each element names a review of R in R*(L(J)) (`reviews_of_R`,
    # [(reference, doc)] of the reviews in R*(L(J)) naming R's exact reference, until the R* wiring exists) and an item
    # adverse in it (a verdict other than accept, an omitted or duplicated item id, or `dissent` for a non-empty dissent
    # field). Reported as ADJ-FORM.
    out = []
    by_ref = {_key(r): d for r, d in reviews_of_R}
    for x in J.get('dissents_addressed') or [] if isinstance(J, dict) else []:
        rv = by_ref.get(_key((x or {}).get('ref')))
        if not isinstance(rv, dict):
            out.append(('ADJ-FORM', 'dissents_addressed names %r, which is not a review of R in R*(L(J))'
                        % ((x or {}).get('ref'),)))
        elif not isinstance(R, dict) or (x or {}).get('item') not in c3.repair_dissent_items(rv, R):
            out.append(('ADJ-FORM', 'dissents_addressed names item %r, which is not adverse in that review'
                        % (x or {}).get('item')))
    return out


# ---- R6.ADJ.3: authorization -----------------------------------------------------------------------------------

def authorization_problems(J, landing_time, owner_identities):
    # [(condition, message)]: the author a member of OWNER_IDENTITIES (ADJ-AUTH-OWNER); adjudicator, finding,
    # witness_sources (set equality) and replacement equal to the record's own (ADJ-AUTH-SCOPE); time earlier than the
    # committer time of L(J), a form check of chronology only (ADJ-AUTH-TIME; `landing_time` a datetime or None when
    # L(J) does not exist, which fails).
    a = J.get('authorization') if isinstance(J, dict) else None
    if not isinstance(a, dict):
        return [('ADJ-AUTH-FORM', 'no authorization object')]
    out = []
    if not member(a.get('author'), owner_identities):
        out.append(('ADJ-AUTH-OWNER', 'the authorization\'s author is not a member of OWNER_IDENTITIES'))
    if not same(a.get('adjudicator'), J.get('author')):
        out.append(('ADJ-AUTH-SCOPE', 'the authorized adjudicator is not the record\'s author'))
    if a.get('finding') != J.get('finding'):
        out.append(('ADJ-AUTH-SCOPE', 'the authorized finding is not the record\'s finding'))
    ws = (J.get('witness') or {}).get('sources') if isinstance(J.get('witness'), dict) else None
    if not isinstance(a.get('witness_sources'), list) or not isinstance(ws, list) or \
            {_key(x) for x in a['witness_sources']} != {_key(x) for x in ws}:
        out.append(('ADJ-AUTH-SCOPE', 'the authorized witness sources are not the record\'s'))
    if a.get('replacement') != J.get('replacement'):
        out.append(('ADJ-AUTH-SCOPE', 'the authorized replacement is not the record\'s'))
    t = parse_time(a.get('time'))
    if landing_time is None or t is None or not t < landing_time:
        out.append(('ADJ-AUTH-TIME', 'the authorization\'s time is not earlier than the committer time of L(J)'))
    return out


# ---- R6.ADJ.4: independence ------------------------------------------------------------------------------------

def usable(v):
    return fd._enc('identity', v)


def same(a, b):
    # Identity strings compare under R6.RECON.29 (findings.same_identity).
    return fd.same_identity(a, b)


def member(v, identities):
    return any(same(v, x) for x in identities)


def parties(finding_record=None, finding_review=None, Q=None, R=None, A=None, config=None, sources=(),
            predecessor=None, reviews=()):
    """Parties: the usable identities among the author or reviewer of the record carrying the finding; the author of
    Q, R, A, the citing configuration (None for Parties_J), each source with an author and, for a lineage witness, the
    predecessor; and the reviewer of each source review and of each review in `reviews` (those in R*(C) of Q, R and
    A naming their exact references, and of the predecessor). An unusable identity is left out."""
    out = set()

    def add(v):
        if usable(v):
            out.add(v)
    for d in (finding_record, Q, R, A, config, predecessor) + tuple(sources):
        if isinstance(d, dict):
            add(d.get('author'))
    for d in (finding_review,) + tuple(sources) + tuple(reviews):
        if isinstance(d, dict):
            add(d.get('reviewer'))
    return out


def independence_problems(J, tech_reviewer, party_set, owner_identities):
    # ADJ-INDEP: the adjudicator and the technical reviewer usable identities, outside Parties and OWNER_IDENTITIES
    # (OD-4), the reviewer not the adjudicator. Identity strings compare as strings (R6.RECON.29).
    out = []
    j = J.get('author') if isinstance(J, dict) else None
    if not usable(j):
        out.append(('ADJ-INDEP', 'the adjudicator is not a usable identity'))
    elif member(j, party_set):
        out.append(('ADJ-INDEP', 'the adjudicator is a party'))
    if member(j, owner_identities):
        out.append(('ADJ-INDEP', 'the adjudicator is a member of OWNER_IDENTITIES'))
    if tech_reviewer is not None:
        if not usable(tech_reviewer):
            out.append(('ADJ-INDEP', 'the technical reviewer is not a usable identity'))
        elif member(tech_reviewer, party_set):
            out.append(('ADJ-INDEP', 'the technical reviewer is a party'))
        if same(tech_reviewer, j):
            out.append(('ADJ-INDEP', 'the technical reviewer is the adjudicator'))
        if member(tech_reviewer, owner_identities):
            out.append(('ADJ-INDEP', 'the technical reviewer is a member of OWNER_IDENTITIES'))
    return out


# ---- R6.ADJ.5: binding -----------------------------------------------------------------------------------------

def witness_description(kind, disputed, sources, adverse, original_configuration, edge=None):
    # A reproduced witness as R6.ADJ.5 compares it: references and item references only.
    return {'class': kind, 'disputed': disputed, 'edge': edge, 'sources': list(sources), 'adverse': list(adverse),
            'original_configuration': original_configuration}


def review_witness_adverse(sources):
    """The adverse item references of a review witness: for each (reference of V, V, the record V reviews), each item
    that makes V adverse or defective (a verdict other than accept, an omitted or duplicated item, `dissent` for a
    non-empty dissent field)."""
    out = []
    for vref, V, reviewed in sources:
        out += [{'ref': vref, 'item': i} for i in obl29.adverse_items(V, reviewed)]
    return out


def unresolved_references(J, resolves):
    """References required by binding and substance whose exact path and digest cannot be resolved."""
    w = J.get('witness') or {}
    refs = [J.get('finding'), J.get('reassessment'), J.get('replacement'), w.get('disputed'),
            w.get('original_configuration'), *w.get('sources', ())]
    if isinstance(w.get('edge'), dict):
        refs.extend(w['edge'].values())
    targets = [*w.get('adverse', ()), *J.get('dissents_addressed', ())]
    targets.extend(g.get('target') for g in J.get('grounds') or [] if isinstance(g, dict))
    refs.extend(x.get('ref') for x in targets if isinstance(x, dict))
    return [r for r in refs if not isinstance(r, dict) or not resolves(_ref(r))]


def self_consistency(J, reproduced, resolves):
    # ADJ-BIND, self-consistency: every reference of J resolves and witness reproduces from custody.
    out = [('ADJ-BIND', 'a reference does not resolve: %r' % (r,)) for r in unresolved_references(J, resolves)]
    w = J.get('witness') if isinstance(J.get('witness'), dict) else {}
    if reproduced is None:
        return out + [('ADJ-BIND', 'the retained witness cannot be reproduced from custody (R6.OBL29.3)')]
    # a lineage witness's edge is the operative edge U -> P {successor, predecessor} as r9 retains it (#1605 sec. 6
    # rows adopted with the U -> P edge)
    for k in ('class', 'disputed', 'edge', 'original_configuration'):
        if w.get(k) != reproduced.get(k):
            out.append(('ADJ-BIND', 'witness.%s does not reproduce' % k))
    for k in ('sources', 'adverse'):
        if {_key(x) for x in w.get(k) or []} != {_key(x) for x in reproduced.get(k) or []}:
            out.append(('ADJ-BIND', 'witness.%s is not set-equal to the retained witness\'s' % k))
    return out


def binds(J, aref, A, reproduced):
    # ADJ-BIND, binding to a discharge D (reassessment A at `aref`) and witness W (`reproduced`): finding equal to A's
    # (path, blob sha256 and item), reassessment equal to A's reference, replacement equal to A's repair.entry, and
    # witness describing W.
    out = []
    if not isinstance(A, dict) or J.get('finding') != A.get('finding'):
        out.append(('ADJ-BIND', 'the finding is not the reassessment\'s finding'))
    if J.get('reassessment') != aref:
        out.append(('ADJ-BIND', 'the reassessment is not the discharge\'s'))
    entry = ((A or {}).get('repair') or {}).get('entry') if isinstance((A or {}).get('repair'), dict) else None
    if J.get('replacement') != entry:
        out.append(('ADJ-BIND', 'the replacement is not the reassessment\'s repair entry'))
    w = J.get('witness') if isinstance(J.get('witness'), dict) else {}
    if reproduced is None or any(w.get(k) != reproduced.get(k) for k in ('class', 'disputed', 'edge')) or \
            {_key(x) for x in w.get('sources') or []} != {_key(x) for x in reproduced.get('sources') or []}:
        out.append(('ADJ-BIND', 'the witness is not W'))
    return out


# ---- R6.ADJ.6: substance ---------------------------------------------------------------------------------------

def substance_problems(J, git_of):
    # ADJ-SUBST: the grounds' targets equal witness.adverse union dissents_addressed, one each; each ground's
    # evidence holds the git blob ids of its target's record, of Q and of R; `method` holds (token rule) the git blob
    # ids of the record carrying the finding, of each source, of Q, of R and of A. `git_of(ref)` is the git blob id of a
    # reference, or None when it does not resolve (which fails).
    out = []
    w = J.get('witness') if isinstance(J.get('witness'), dict) else {}
    want = {_key(x) for x in (w.get('adverse') or []) + (J.get('dissents_addressed') or [])}
    targets = [_key(g.get('target')) for g in J.get('grounds') or [] if isinstance(g, dict)]
    if sorted(targets) != sorted(want):
        out.append(('ADJ-SUBST', 'the grounds\' targets are not witness.adverse and dissents_addressed, one each'))
    q, r = git_of(w.get('disputed')), git_of(_ref(J.get('replacement')))
    for g in J.get('grounds') or []:
        if not isinstance(g, dict):
            continue
        ev = set(g.get('evidence') or [])
        tg = git_of((g.get('target') or {}).get('ref'))
        if not (tg and q and r and {tg, q, r} <= ev):
            out.append(('ADJ-SUBST', 'ground %s: evidence lacks the git blob id of its target, Q or R' % g.get('id')))
        if not (isinstance(g.get('reasoning'), str) and g['reasoning'].strip()):
            out.append(('ADJ-SUBST', 'ground %s: empty reasoning' % g.get('id')))
    f = J.get('finding') if isinstance(J.get('finding'), dict) else {}
    need = [git_of(_ref(f)), q, r, git_of(J.get('reassessment'))] + [git_of(s) for s in w.get('sources') or []]
    if not all(need) or not all(obl29.holds(J.get('method'), x) for x in need):
        out.append(('ADJ-SUBST', 'method lacks a git blob id R6.ADJ.6 requires'))
    return out


def _ref(x):
    return {'path': x.get('path'), 'blob_sha256': x.get('blob_sha256')} if isinstance(x, dict) else None


# ---- R6.ADJ.7: technical review ---------------------------------------------------------------------------------

def item_ids(J):
    # The review item ids of an adjudication (R6.ADJ.2): authorization, binding, dissents, disposition, conflicts,
    # and ground:<id> for each ground.
    return list(fixed_items) + ['ground:%s' % g.get('id') for g in J.get('grounds') or [] if isinstance(g, dict)]


def adverse_to(review, J):
    """A review of J is adverse when it does not accept every item, or has a non-empty dissent."""
    return bool(_adverse_items(review, J))


def _adverse_items(review, J):
    ids = item_ids(J)
    verdicts = {}
    for v in review.get('verdicts') or [] if isinstance(review, dict) else []:
        if isinstance(v, dict):
            verdicts.setdefault(v.get('item'), []).append(v.get('verdict'))
    out = [i for i in ids if i not in verdicts or len(verdicts[i]) != 1 or verdicts[i][0] != 'accept']
    if isinstance(review, dict) and isinstance(review.get('dissent'), str) and review['dissent'].strip():
        out.append('dissent')
    return out


def review_problems(review, J, jref, j_git, source_gits, party_set, owner_identities):
    # ADJ-REVIEW / ADJ-INDEP: [] when the review qualifies (R6.REC.6 and R6.RECON.31 form, kind review, reviewed J's
    # exact reference, every item accepted once, empty or absent dissent, reviewer allowed by R6.ADJ.4, and a method
    # holding the git blob ids of J and of each source).
    out = []
    if not isinstance(review, dict):
        return [('ADJ-REVIEW', 'not a review')]
    out += [('ADJ-REVIEW', x) for x in fd.review_schema_problems(review)]
    if review.get('kind', 'review') != 'review' or review.get('reviewed') != jref:
        out.append(('ADJ-REVIEW', 'not an ordinary review of J\'s exact reference'))
    if _adverse_items(review, J):
        out.append(('ADJ-REVIEW', 'it does not accept every item of J, or dissents'))
    # the reviewer's own independence conditions (the adjudicator's are checked by independence_problems on J)
    out += [p for p in independence_problems(J, review.get('reviewer'), party_set, owner_identities)
            if 'technical reviewer' in p[1]]
    if not j_git or not all(source_gits) or not obl29.holds(review.get('method'), j_git) or \
            not all(obl29.holds(review.get('method'), x) for x in source_gits):
        out.append(('ADJ-REVIEW', 'its method lacks the git blob id of J or of a source'))
    return out


# ---- R6.ADJ.8: admission conditions ----------------------------------------------------------------------------

def landing(repo, M, jref, qualifying_review_at):
    # L(J): the earliest commit C on M's first-parent chain whose tree holds J (at its path, with its blob) and a review
    # of J that qualifies under R6.ADJ.7 evaluated over R*(C) with Parties_J(C). `qualifying_review_at(C)` decides the
    # second condition (the caller evaluates R6.ADJ.7 over R*(C)). None when there is none.
    chain, c = [], M
    while c:
        chain.append(c)
        ps = repo.parents(c)
        c = ps[0] if ps else None
    for c in reversed(chain):
        e = repo.entries(c).get(jref['path'])
        if e is None or e[0] not in ('100644', '100755'):
            continue
        data = repo.read(c, jref['path'])
        if data is not None and util.sha256(data) == jref['blob_sha256'] and qualifying_review_at(c):
            return c
    return None


def location_problems(jref, review_refs, J):
    # ADJ-ADMIT: J and its cited review lie in the reconciliation directory of J's replacement (R6.ADJ.1).
    d = posixpath.dirname(((J.get('replacement') or {}).get('path')) or '')
    out = []
    for r in [jref] + list(review_refs):
        if posixpath.dirname(r.get('path') or '') != d:
            out.append(('ADJ-ADMIT', '%s is not in the reconciliation directory of the replacement' % r.get('path')))
    return out


def citation_problems(cfg_records, jref, qualifying_review_refs):
    # ADJ-ADMIT: the configuration references J with kind adjudication and exactly one qualifying review of J with
    # kind review (R6.REC.4; R6.ADJ.11: two cited reviews of J fail).
    recs = [r for r in cfg_records or [] if isinstance(r, dict)]
    out = []
    if not any(r.get('kind') == 'adjudication' and _ref(r) == jref for r in recs):
        out.append(('ADJ-ADMIT', 'the configuration does not reference J with kind adjudication'))
    q = {_key(x) for x in qualifying_review_refs}
    cited = [r for r in recs if r.get('kind') == 'review' and _key(_ref(r)) in q]
    if len(cited) != 1:
        out.append(('ADJ-ADMIT', '%d qualifying reviews of J are cited, not one' % len(cited)))
    return out


def dedicated_landing_problems(repo, M, jref, review_ref):
    # ADJ-DEDICATED (M5', OD-3): the commit L1 on M's first-parent chain that first holds J's blob at its path differs
    # from its first parent only by adding J and that review. No such commit fails.
    chain, c = [], M
    while c:
        chain.append(c)
        ps = repo.parents(c)
        c = ps[0] if ps else None
    chain.reverse()
    for c in chain:
        e = repo.entries(c).get(jref['path'])
        data = repo.read(c, jref['path']) if e is not None and e[0] in ('100644', '100755') else None
        if data is None or util.sha256(data) != jref['blob_sha256']:
            continue
        ps = repo.parents(c)
        a, b = repo.entries(ps[0]) if ps else {}, repo.entries(c)
        changed = sorted(p for p in set(a) | set(b) if a.get(p) != b.get(p))
        if sorted(changed) != sorted({jref['path'], review_ref['path']}) or any(p in a for p in changed):
            return [('ADJ-DEDICATED', 'the commit that introduces J changes more than adding J and its review')]
        return []
    return [('ADJ-DEDICATED', 'no commit on M\'s first-parent chain holds J')]


# ---- R6.ADJ.9: matching, contradiction and the decision --------------------------------------------------------

def matches(J1, J2):
    """Two adjudications match: the same finding (reference and item), replacements with the same blob_sha256 and
    entry_path, witness.disputed with the same blob_sha256, and witness.sources sharing at least one blob_sha256."""
    try:
        w1, w2 = J1['witness'], J2['witness']
        return J1['finding'] == J2['finding'] and \
            J1['replacement']['blob_sha256'] == J2['replacement']['blob_sha256'] and \
            J1['replacement']['entry_path'] == J2['replacement']['entry_path'] and \
            w1['disputed']['blob_sha256'] == w2['disputed']['blob_sha256'] and \
            bool({s['blob_sha256'] for s in w1['sources']} & {s['blob_sha256'] for s in w2['sources']})
    except (KeyError, TypeError):
        return False


def contradiction_problems(J, others):
    # ADJ-CONTRA: `others` is [(J2, validity)] of every other oi-adjudication/1 record in R*, validity 'valid',
    # 'invalid' (established invalid for adverse use by a definite failure) or 'unknown' (its validity cannot be
    # established). A matching upheld record that is not established invalid contradicts J.
    return [('ADJ-CONTRA', 'a matching upheld adjudication %s' % ('is valid' if v == 'valid' else
                                                                   'cannot be established invalid'))
            for J2, v in others if J2 is not J and isinstance(J2, dict) and J2.get('disposition') == 'upheld'
            and matches(J, J2) and v != 'invalid']


def upheld_blocks_nr5(replacement, witness, finding, upheld_valid):
    # ADJ-UPHELD (OD-6): an upheld adjudication valid for adverse use makes NR-5 false for a replacement and witness
    # it matches (with R in place of J.replacement).
    probe = {'finding': finding, 'replacement': replacement, 'witness': witness}
    return any(matches(probe, J2) for J2 in upheld_valid)


def adjudicated(admitted_cleared_binding, contradicted):
    # R6.ADJ.9: Adjudicated(W, D) holds exactly when some admitted adjudication that binds D and W, with disposition
    # cleared, has no contradiction. `admitted_cleared_binding` lists those adjudications; `contradicted(J)` returns
    # ADJ-CONTRA problems. False unless verified records establish it (R6.ADJ.11).
    return any(not contradicted(J) for J in admitted_cleared_binding)


# ---- R6.ADJ.12: dissents in four strata ------------------------------------------------------------------------

def strata(pre_admitted, reviews_of, dissents_on_R):
    # R6.ADJ.12 for one discharge D. `pre_admitted` is [{J, ref, binds, landing_index, answered}] of stratum 1 (each
    # pre-admitted adjudication with whether it binds D and W and is cleared, `landing_index` the position of L(J) on
    # M's first-parent chain, `answered` = Answered(J)); `reviews_of(ref)` lists [{reviewer, verdicts, dissent,
    # first_index, ref}] of the reviews of J in R*; `dissents_on_R` is [{reviewer, item, first_index, review}] of the
    # dissent items on R. Returns {admitted: [refs], exempt_reviews: {J ref: [review refs]}, disregarded: [dissent
    # items], blocking: [dissent items neither addressed nor exempt]}.
    exempt, admitted = {}, []
    for p in pre_admitted:
        J = p['adjudication']
        ex, ok = [], True
        for rv in reviews_of(p['ref']):
            bad = _adverse_items(rv, J)
            if not bad:
                continue
            later = rv['first_index'] > p['landing_index']
            # the non-accept items lie on ground:<id>, disposition or dissents (or the dissent field): an item of J is
            # one of those or of never_exempt (authorization, binding, conflicts), which keeps its veto
            if p['binds'] and later and member(rv.get('reviewer'), p['answered']) and \
                    not any(i in never_exempt for i in bad):
                ex.append(rv['ref'])
            else:
                ok = False
        exempt[_key(p['ref'])] = ex
        if ok:
            admitted.append(p)
    disregarded, blocking = [], []
    for d in dissents_on_R:
        addressed = any(p['binds'] and {'ref': d['review'], 'item': d['item']} in
                        (p['adjudication'].get('dissents_addressed') or []) for p in admitted)
        late = [p for p in admitted if p['binds'] and d['first_index'] > p['landing_index']
                and member(d['reviewer'], p['answered'])]
        for p in late:
            refs = exempt[_key(p['ref'])]
            if d['review'] not in refs:
                refs.append(d['review'])
        (disregarded if addressed or late else blocking).append(d)
    return {'admitted': [p['ref'] for p in admitted], 'exempt_reviews': exempt, 'disregarded': disregarded,
            'blocking': blocking}


def answered(J, review_docs):
    """Answered(J): the reviewer of each review in J.witness.sources and of each review referenced in
    dissents_addressed (`review_docs(ref)` returns the review or None), usable identities only."""
    refs = list((J.get('witness') or {}).get('sources') or []) + \
        [d.get('ref') for d in J.get('dissents_addressed') or [] if isinstance(d, dict)]
    out = set()
    for r in refs:
        d = review_docs(r)
        if isinstance(d, dict) and usable(d.get('reviewer')):
            out.add(d['reviewer'])
    return out


# ---- R6.ADJ.13: result entry -----------------------------------------------------------------------------------

def result_entry(jref, J, landing, valid_adverse, pre_admitted, admitted, applies, failures, exempt_reviews):
    return {'path': jref['path'], 'blob_sha256': jref['blob_sha256'],
            'witness_sources': list(((J or {}).get('witness') or {}).get('sources') or []),
            'disposition': (J or {}).get('disposition'), 'landing': landing, 'valid_adverse': bool(valid_adverse),
            'pre_admitted': bool(pre_admitted), 'admitted': bool(admitted), 'applies': bool(applies),
            'failures': sorted(set(failures)), 'exempt_reviews': list(exempt_reviews)}


# ---- the run: Adjudicated(W, D) from admitted records -------------------------------------------------------------

def describe(W):
    # The retained witness W of custody (category3.replay_run) as R6.ADJ.5 compares it.
    sources = [x['ref'] for x in W.get('forming') or []]
    if W.get('kind') == 'lineage':
        er = W.get('edge_refs') or (None, None)
        return witness_description('lineage', W['disputed'], sources, [{'ref': s_, 'item': 'edge'} for s_ in sources],
                                   W.get('config'), edge={'successor': er[0], 'predecessor': er[1]})
    adverse = review_witness_adverse([(x['ref'], x['doc'], W.get('disputed_doc')) for x in W.get('forming') or []])
    return witness_description('review', W['disputed'], sources, adverse, W.get('config'))


def fp_chain(repo, M):
    out, c = [], M
    while c:
        out.append(c)
        ps = repo.parents(c)
        c = ps[0] if ps else None
    out.reverse()
    return out


class Run:
    # What `evaluate` reads: the reader, M, the candidate freeze F' (the run's F, or the configuration's commit in a
    # control-harness run), the configuration's records and store, R* (cum), a document lookup doc_of(ref), the custody
    # historical witness replay and OWNER_IDENTITIES.

    def __init__(self, repo, M, Fprime, cfg_records, store, cum, doc_of, witnesses_at, owners):
        self.repo, self.M, self.Fprime = repo, M, Fprime
        self.cfg_records, self.store, self.cum, self.doc_of = cfg_records, store, cum, doc_of
        self.witnesses_at, self.owners = witnesses_at, owners
        self.chain = fp_chain(repo, M)
        self.index = {c: i for i, c in enumerate(self.chain)}
        self._first = {}
        self._landing_evidence = None

    def evidence_at(self, commit):
        if self._landing_evidence is None or self._landing_evidence.commit != commit:
            self._landing_evidence = LandingEvidence(self.repo, commit)
        return self._landing_evidence

    def first_index(self, ref):
        """The index on M's first-parent chain of the first commit holding ref's blob at its path, or -1."""
        key = (ref.get('path'), ref.get('blob_sha256'))
        if key not in self._first:
            self._first[key] = -1
            for i, c in enumerate(self.chain):
                e = self.repo.entries(c).get(ref.get('path'))
                if e is not None and e[0] in ('100644', '100755') and \
                        util.sha256(self.repo.read(c, ref['path'])) == ref.get('blob_sha256'):
                    self._first[key] = i
                    break
        return self._first[key]

    def git_of(self, ref):
        if not isinstance(ref, dict):
            return None
        g = self.cum.git_id({'path': ref.get('path'), 'blob_sha256': ref.get('blob_sha256')})
        if g:
            return g
        for c in (self.M, self.Fprime):
            e = self.repo.entries(c).get(ref.get('path')) if c else None
            if e is not None and e[0] in ('100644', '100755') and \
                    util.sha256(self.repo.read(c, ref['path'])) == ref.get('blob_sha256'):
                return e[1]
        return None

    def reviews_of(self, ref, directory=None, *, at=None):
        """Reviews in the run's R*, or in R*(at) through verified ancestry for adverse use."""
        rows = self.cum.reviews_naming_ids(ref, directory)
        if at is None:
            return rows
        ancestors = self.evidence_at(at).ancestors
        return [(p, o, d) for p, o, d in rows
                if not ancestors.isdisjoint(self.cum.holders.get((p, o), ()))]


class LandingEvidence:
    """Resolve an exact reference using regular files in the verified ancestry of one commit."""

    def __init__(self, repo, commit):
        self.repo, self.commit = repo, commit
        self.ancestors = set()
        self._history = []
        todo = [commit]
        while todo:
            cid = todo.pop()
            if cid in self.ancestors:
                continue
            self.ancestors.add(cid)
            self._history.append(cid)
            todo.extend(reversed(repo.parents(cid)))
        self._refs = {}
        self._digests = {}

    def git_of(self, ref):
        path, digest = ref['path'], ref['blob_sha256']
        key = (path, digest)
        if key not in self._refs:
            self._refs[key] = None
            for commit in self._history:
                oid = self.repo.regular_blob_at(commit, path)
                if oid is None:
                    continue
                if oid not in self._digests:
                    self._digests[oid] = util.sha256(self.repo.read_blob(oid))
                if self._digests[oid] == digest:
                    self._refs[key] = oid
                    break
        return self._refs[key]

    def doc_of(self, ref):
        oid = self.git_of(ref)
        return fd.strict_parse(self.repo.read_blob(oid)) if oid else None


def _parties_for(run, finding_ref, Q, R, A, config, sources, predecessor, refs_reviewed, *, at=None):
    frec = run.doc_of(finding_ref) if at is None else run.evidence_at(at).doc_of(finding_ref)
    reviews = []
    for r_ in refs_reviewed:
        if isinstance(r_, dict):
            reviews += [d for _p, _o, d in run.reviews_of(r_, at=at)]
    return parties(finding_record=frec if isinstance(frec, dict) and 'author' in frec else None,
                   finding_review=frec if isinstance(frec, dict) and 'reviewer' in frec else None,
                   Q=Q, R=R, A=A, config=config, sources=sources, predecessor=predecessor, reviews=reviews)


def parties_j(run, J, at):
    # Parties_J(at): J's own bindings and reviews in R*(at) (R6.ADJ.4).
    w = J.get('witness') if isinstance(J.get('witness'), dict) else {}
    f = J.get('finding') if isinstance(J.get('finding'), dict) else {}
    fref = {'path': f.get('path'), 'blob_sha256': f.get('blob_sha256')}
    pred = ((w.get('edge') or {}).get('predecessor')) if isinstance(w.get('edge'), dict) else None
    lookup = run.evidence_at(at).doc_of
    srcs = [lookup(s_) for s_ in w.get('sources') or []]
    return _parties_for(run, fref, lookup(w['disputed']), lookup(_ref(J['replacement'])),
                        lookup(J['reassessment']), None, [x for x in srcs if isinstance(x, dict)],
                        lookup(pred) if pred else None,
                        [w.get('disputed'), _ref(J.get('replacement')), J.get('reassessment')] + ([pred] if pred else []),
                        at=at)


def qualifying_landing(run, jref, J, joid, reviews):
    """Find L(J) using the qualifying technical reviews held in each candidate first-parent tree."""
    sources = J['witness']['sources']

    def qualifying_review_at(commit):
        entries = run.repo.entries(commit)
        present = [d for p, o, d in reviews if entries.get(p) in (('100644', o), ('100755', o))]
        if not present:
            return False
        srcs = [run.evidence_at(commit).git_of(s) for s in sources]
        pj = parties_j(run, J, commit)
        return any(not review_problems(d, J, jref, joid, srcs, pj, run.owners) for d in present)

    return landing(run.repo, run.M, jref, qualifying_review_at)


def addressed_problems_at(run, J, L):
    if not J['dissents_addressed']:
        return []
    if L is None:
        return [('ADJ-FORM', 'the addressed dissents cannot be verified without L(J)')]
    rref = _ref(J['replacement'])
    reviews = [({'path': p, 'blob_sha256': run.cum.info[o][2]}, d) for p, o, d in run.reviews_of(rref, at=L)]
    return dissents_addressed_problems(J, reviews, run.evidence_at(L).doc_of(rref))


def validity(run, jref, J, joid):
    # Return the adverse verdict and L(J). Unresolved evidence stays unknown under R6.ADJ.9 (4).
    if form_problems(J):
        return 'invalid', None
    reviews = run.reviews_of(jref)
    if not reviews:
        return 'invalid', None
    L = qualifying_landing(run, jref, J, joid, reviews)
    if L is None:
        # Without L(J), only defects independent of the unresolved party snapshot can disqualify the review.
        srcs = [run.evidence_at(run.M).git_of(s) for s in J['witness']['sources']]
        if all(srcs) and all(review_problems(d, J, jref, joid, srcs, set(), run.owners) for _p, _o, d in reviews):
            return 'invalid', None
        return 'unknown', None
    evidence = run.evidence_at(L)
    others = [(r, d) for r, _oid, d in run.cum.adjudications()]
    if record_id_problems(J, jref, others, evidence.git_of):
        return 'invalid', L
    pj = parties_j(run, J, L)
    t = run.repo.committer_time(L)
    lt = datetime.fromtimestamp(t, timezone.utc) if t is not None else None
    if authorization_problems(J, lt, run.owners) or independence_problems(J, None, pj, run.owners):
        return 'invalid', L
    if unresolved_references(J, evidence.git_of):
        return 'unknown', L
    if substance_problems(J, evidence.git_of):
        return 'invalid', L
    if addressed_problems_at(run, J, L):
        return 'invalid', L
    verdict = 'unknown'
    for W in run.witnesses_at(L):
        reproduced = describe(W)
        if reproduced['class'] != J['witness']['class'] or reproduced['disputed'] != J['witness']['disputed'] or \
                {_key(x) for x in reproduced['sources']} != {_key(x) for x in J['witness']['sources']}:
            continue
        try:
            if not self_consistency(J, reproduced, evidence.git_of):
                return 'valid', L
        except fd.Unsettled:
            return 'unknown', L
        verdict = 'invalid'
    return verdict, L


def evaluate(run, D, W, dissents_on_R):
    """Return qualified route-2 candidates, their reports, upheld records and exact covered dissent items.

    The caller checks stratum 4 across all relying witnesses of D before applying any clearance.
    """
    Wd = describe(W)
    cited = [r for r in run.cfg_records if isinstance(r, dict) and r.get('kind') == 'adjudication']
    all_adj = run.cum.adjudications()
    rows, qualified = [], []
    records = [(r, d) for r, _oid, d in all_adj]
    disregarded = []
    upheld_valid = []
    for jr, jo, J2 in all_adj:
        if isinstance(J2, dict) and J2.get('disposition') == 'upheld' and validity(run, jr, J2, jo)[0] == 'valid':
            upheld_valid.append(J2)
    pd = _parties_for(run, D['finding_ref'], W.get('disputed_doc'), D.get('R'), D.get('A'), D.get('config'),
                      [x['doc'] for x in W.get('forming') or [] if isinstance(x.get('doc'), dict)],
                      run.doc_of((W.get('edge_refs') or (None, None))[1]) if W.get('edge_refs') else None,
                      [W['disputed'], D.get('rref'), D['aref']] +
                      ([W['edge_refs'][1]] if W.get('edge_refs') else []))
    for r in cited:
        jref = {'path': r.get('path'), 'blob_sha256': r.get('blob_sha256')}
        J = run.store.get(jref)
        failures = []
        if not isinstance(J, dict):
            rows.append(result_entry(jref, None, None, False, False, False, False, ['ADJ-ADMIT'], []))
            continue
        joid = run.git_of(jref)
        rv_refs = [{'path': x.get('path'), 'blob_sha256': x.get('blob_sha256')} for x in run.cfg_records
                   if isinstance(x, dict) and x.get('kind') == 'review' and
                   isinstance(run.store.get(x), dict) and run.store.get(x).get('reviewed') == jref]
        srcs = [run.git_of(s_) for s_ in ((J.get('witness') or {}).get('sources') or [])]
        qual = [x for x in rv_refs if not review_problems(run.store.get(x), J, jref, joid, srcs, pd, run.owners)]
        failures += [c for c, _m in citation_problems(run.cfg_records, jref, qual)]
        failures += [c for c, _m in location_problems(jref, rv_refs, J)]
        form = form_problems(J)
        form += record_id_problems(J, jref, records)
        failures += [c for c, _m in form]
        L = qualifying_landing(run, jref, J, joid, run.reviews_of(jref)) if not form else None
        t = run.repo.committer_time(L) if L else None
        lt = datetime.fromtimestamp(t, timezone.utc) if t is not None else None
        if not form:
            failures += [c for c, _m in authorization_problems(J, lt, run.owners)]
            failures += [c for c, _m in independence_problems(J, (run.store.get(qual[0]) or {}).get('reviewer')
                                                               if qual else None, pd, run.owners)]
            try:
                failures += [c for c, _m in self_consistency(J, Wd, lambda r_: run.git_of(r_) is not None)]
            except fd.Unsettled:
                failures.append('ADJ-BIND')
            failures += [c for c, _m in binds(J, D['aref'], D.get('A'), Wd)]
            failures += [c for c, _m in substance_problems(J, run.git_of)]
            failures += [c for c, _m in addressed_problems_at(run, J, L)]
            for x in rv_refs:
                failures += [c for c, _m in review_problems(run.store.get(x), J, jref, joid, srcs, pd, run.owners)]
        # ADJ-LANDED: J and its review on M's first-parent chain, at a commit that is an ancestor of F'
        for x in [jref] + qual:
            i = run.first_index(x)
            if i < 0 or not run.Fprime or not (run.chain[i] == run.Fprime or
                                               run.repo.is_ancestor(run.chain[i], run.Fprime)):
                failures.append('ADJ-LANDED')
        if qual:
            failures += [c for c, _m in dedicated_landing_problems(run.repo, run.M, jref, qual[0])]
        else:
            failures.append('ADJ-REVIEW')
        pre = not failures
        admitted = applies = False
        exempt = []
        if pre and J.get('disposition') == 'cleared':
            ans = answered(J, lambda r_: run.doc_of(r_))
            li = run.index.get(L, -1)
            rj = [{'reviewer': d.get('reviewer'), 'verdicts': d.get('verdicts'), 'dissent': d.get('dissent'),
                   'first_index': run.first_index({'path': p, 'blob_sha256': run.cum.info[o][2]}),
                   'ref': {'path': p, 'blob_sha256': run.cum.info[o][2]}} for p, o, d in run.reviews_of(jref)]
            st = strata([{'adjudication': J, 'ref': jref, 'binds': True, 'landing_index': li, 'answered': ans}],
                        lambda ref_: rj, dissents_on_R)
            exempt = st['exempt_reviews'].get(_key(jref), [])
            admitted = bool(st['admitted'])
            if not admitted:
                failures.append('ADJ-REVIEW')
            contra = contradiction_problems(J, [(J2, validity(run, jr, J2, jo)[0]) for jr, jo, J2 in all_adj
                                                if jr != jref])
            failures += [c for c, _m in contra]
            applies = admitted and not contra
            if applies:
                qualified.append({'adjudication': jref, 'review': qual[0]})
                for item in st['disregarded']:
                    target = {'ref': item['review'], 'item': item['item']}
                    basis = 'addressed' if target in J['dissents_addressed'] else 'exempt'
                    disregarded.append({'review': item['review'], 'item': item['item'], 'basis': basis,
                                        'adjudication': jref})
        elif pre:
            failures.append('ADJ-UPHELD' if J.get('disposition') == 'upheld' else 'ADJ-FORM')
        rows.append(result_entry(jref, J, L, False, pre, admitted, applies, failures, exempt))
    return qualified, rows, upheld_valid, disregarded
