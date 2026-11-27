"""Formal adjudication of retained witnesses (design r4 of PR #1605 at its adopted head, adopted with OD-1 to OD-7 at
their defaults): the mechanical predicates of R6.ADJ.1 to R6.ADJ.14 over explicit
records.

These predicates are not called by a run. Applying them needs the amendments the design's sec. 6 lists, which its
adoption did not make ("Not authorized by this adoption: the schema and admission-rule changes the design lists"):
- r13 R6.CFG.4 and R6.RECON.33: the kind row `adjudication` -> `oi-adjudication/1`, without which no configuration can
  cite an adjudication (ADJ-ADMIT);
- r13 R6.RECON.31: the item-id row of `oi-adjudication/1`, without which its review has no item ids to lint;
- r13 R6.REC.3: the deliberate change that checks the authorization's author against OWNER_IDENTITIES;
- r13 R6.REC.4 and R6.REC.5: reading adjudications in R* that no configuration references (R6.ADJ.9's contradiction
  and upheld rules);
- r13 R6.REC.6 and r9 NR-3 and NR-5: R6.ADJ.12's disregard of addressed and exempt dissent items;
- r9 sec. 2.2 decision and route 2: `Adjudicated(W)` read as `Adjudicated(W, D)`; r9 R6.OBL29.8 and the result schema:
  the `adjudications` field (R6.ADJ.13);
- r13 R6.REC.1 and R6.RECON.1: the reconciliation directory also holding adjudications and their reviews.
Until those amendments are adopted, r9's `Adjudicated(W)` stays false in every run (engine/obl29.py `decide`), and
these predicates serve only the local controls.

Unsettled in the adopted text (each keeps `Adjudicated` false): the lineage witness's `edge`. The `adj.witness` table
calls it "the exact disputed edge" (r9 sec. 2.2: U -> P, the operative edge), while CONTROLS.json ADJ-P-LINEAGE writes
`edge {S, P}` (the competing successor's edge). self_consistency raises findings.Unsettled for a lineage witness.
"""
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

ITEMREF = {'ref': (('table', fd.REF), True), 'item': ('nestr', True)}
AUTHORIZATION = {'quote': ('nestr', True), 'author': ('identity', True), 'time': ('nestr', True),
                 'source': ('nestr', True), 'adjudicator': ('identity', True),
                 'finding': (('table', c3.REASSESS_FINDING), True),
                 'witness_sources': (('nearray', ('table', fd.REF)), True),
                 'replacement': (('table', c3.REASSESS_ENTRY), True)}
EDGE = {'successor': (('table', fd.REF), True), 'predecessor': (('table', fd.REF), True)}
WITNESS = {'class': (('lit', ('review', 'lineage')), True), 'disputed': (('table', fd.REF), True),
           'edge': (('or', ('null',), ('table', EDGE)), True), 'sources': (('nearray', ('table', fd.REF)), True),
           'adverse': (('arr', ('table', ITEMREF)), True), 'original_configuration': (('table', fd.REF), True)}
GROUND = {'id': ('nestr', True), 'target': (('table', ITEMREF), True), 'reasoning': ('nestr', True),
          'evidence': (('nearray', 'blob'), True)}
RECORD = {'schema': (('lit', (schema,)), True), 'record_id': ('nestr', True), 'supersedes': (('null',), True),
          'author': ('identity', True), 'authorization': (('table', AUTHORIZATION), True),
          'finding': (('table', c3.REASSESS_FINDING), True), 'witness': (('table', WITNESS), True),
          'replacement': (('table', c3.REASSESS_ENTRY), True), 'reassessment': (('table', fd.REF), True),
          'dissents_addressed': (('arr', ('table', ITEMREF)), True),
          'disposition': (('lit', ('cleared', 'upheld')), True), 'grounds': (('nearray', ('table', GROUND)), True),
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
    """[(condition, message)] of R6.ADJ.2's closed key tables: ADJ-AUTH-FORM for the authorization object, ADJ-FORM for
    the rest (with the no-duplicate arrays, `edge` non-null exactly for a lineage witness, unique ground ids without
    whitespace, and a time of R6.RECON.29's encoding)."""
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
        fd.validate(AUTHORIZATION, J['authorization'], '$.authorization', tmp)
        if isinstance(J['authorization'], dict) and parse_time(J['authorization'].get('time')) is None:
            tmp.append('$.authorization.time: not a time (YYYY-MM-DDTHH:MM[:SS]Z)')
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
    """R6.ADJ.14: no key `reviewed` or `verdicts` and no `schema` value beginning `oi-review-record/` or
    `oi-reconciliation/` at any depth. A record that violates it is classed by R6.RECON.35 as it stands (this
    function only reports the shape)."""
    out = []

    def walk(x, where):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ('reviewed', 'verdicts'):
                    out.append('%s.%s: a key R6.RECON.35 reads' % (where, k))
                if k == 'schema' and isinstance(v, str) and v.startswith(('oi-review-record/', 'oi-reconciliation/')):
                    out.append('%s.schema: a schema value R6.RECON.35 selects' % where)
                walk(v, '%s.%s' % (where, k))
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, '%s[%d]' % (where, i))
    walk(J, '$')
    return out


# ---- R6.ADJ.3: authorization -----------------------------------------------------------------------------------

def authorization_problems(J, landing_time, owner_identities):
    """[(condition, message)]: the author a member of OWNER_IDENTITIES (ADJ-AUTH-OWNER); adjudicator, finding,
    witness_sources (set equality) and replacement equal to the record's own (ADJ-AUTH-SCOPE); time earlier than the
    committer time of L(J), a form check of chronology only (ADJ-AUTH-TIME; `landing_time` a datetime or None when
    L(J) does not exist, which fails)."""
    a = J.get('authorization') if isinstance(J, dict) else None
    if not isinstance(a, dict):
        return [('ADJ-AUTH-FORM', 'no authorization object')]
    out = []
    if a.get('author') not in owner_identities:
        out.append(('ADJ-AUTH-OWNER', 'the authorization\'s author is not a member of OWNER_IDENTITIES'))
    if a.get('adjudicator') != J.get('author'):
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
    """ADJ-INDEP: the adjudicator and the technical reviewer usable identities, outside Parties and OWNER_IDENTITIES
    (OD-4), the reviewer not the adjudicator. Identity strings compare as strings (R6.RECON.29)."""
    out = []
    j = J.get('author') if isinstance(J, dict) else None
    if not usable(j):
        out.append(('ADJ-INDEP', 'the adjudicator is not a usable identity'))
    elif j in party_set:
        out.append(('ADJ-INDEP', 'the adjudicator is a party'))
    if j in owner_identities:
        out.append(('ADJ-INDEP', 'the adjudicator is a member of OWNER_IDENTITIES'))
    if tech_reviewer is not None:
        if not usable(tech_reviewer):
            out.append(('ADJ-INDEP', 'the technical reviewer is not a usable identity'))
        elif tech_reviewer in party_set:
            out.append(('ADJ-INDEP', 'the technical reviewer is a party'))
        if tech_reviewer == j:
            out.append(('ADJ-INDEP', 'the technical reviewer is the adjudicator'))
        if tech_reviewer in owner_identities:
            out.append(('ADJ-INDEP', 'the technical reviewer is a member of OWNER_IDENTITIES'))
    return out


# ---- R6.ADJ.5: binding -----------------------------------------------------------------------------------------

def witness_description(kind, disputed, sources, adverse, original_configuration, edge=None):
    """A reproduced witness as R6.ADJ.5 compares it: references and item references only."""
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


def self_consistency(J, reproduced, resolves):
    """ADJ-BIND, self-consistency: every reference of J resolves (`resolves(ref)`), and `witness` reproduces as the
    retained witness `reproduced` (witness_description, or None when it cannot be reproduced from custody)."""
    out = []
    refs = [J.get('reassessment'), J.get('replacement'), (J.get('witness') or {}).get('disputed'),
            (J.get('witness') or {}).get('original_configuration')] + list((J.get('witness') or {}).get('sources') or [])
    f = J.get('finding')
    if isinstance(f, dict):
        refs.append({'path': f.get('path'), 'blob_sha256': f.get('blob_sha256')})
    for r in refs:
        if not isinstance(r, dict) or not resolves({'path': r.get('path'), 'blob_sha256': r.get('blob_sha256')}):
            out.append(('ADJ-BIND', 'a reference does not resolve: %r' % (r,)))
    w = J.get('witness') if isinstance(J.get('witness'), dict) else {}
    if reproduced is None:
        return out + [('ADJ-BIND', 'the retained witness cannot be reproduced from custody (R6.OBL29.3)')]
    if w.get('class') == 'lineage' or reproduced.get('class') == 'lineage':
        raise fd.Unsettled('R6.ADJ.5 for a lineage witness: adj.witness `edge` is "the exact disputed edge" (r9 '
                           'sec. 2.2: the operative edge U -> P) while CONTROLS.json ADJ-P-LINEAGE writes edge {S, P}; '
                           'the design does not settle which edge reproduces (recommended default: the operative '
                           'edge U -> P, as r9 retains it)')
    for k in ('class', 'disputed', 'edge', 'original_configuration'):
        if w.get(k) != reproduced.get(k):
            out.append(('ADJ-BIND', 'witness.%s does not reproduce' % k))
    for k in ('sources', 'adverse'):
        if {_key(x) for x in w.get(k) or []} != {_key(x) for x in reproduced.get(k) or []}:
            out.append(('ADJ-BIND', 'witness.%s is not set-equal to the retained witness\'s' % k))
    return out


def binds(J, aref, A, reproduced):
    """ADJ-BIND, binding to a discharge D (reassessment A at `aref`) and witness W (`reproduced`): finding equal to A's
    (path, blob sha256 and item), reassessment equal to A's reference, replacement equal to A's repair.entry, and
    witness describing W."""
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
    """ADJ-SUBST: the grounds' targets equal witness.adverse union dissents_addressed, one each; each ground's
    evidence holds the git blob ids of its target's record, of Q and of R; `method` holds (token rule) the git blob
    ids of the record carrying the finding, of each source, of Q, of R and of A. `git_of(ref)` is the git blob id of a
    reference, or None when it does not resolve (which fails)."""
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
    """The review item ids of an adjudication (R6.ADJ.2): authorization, binding, dissents, disposition, conflicts,
    and ground:<id> for each ground."""
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
    """ADJ-REVIEW / ADJ-INDEP: [] when the review qualifies (R6.REC.6 and R6.RECON.31 form, kind review, reviewed J's
    exact reference, every item accepted once, empty or absent dissent, reviewer allowed by R6.ADJ.4, and a method
    holding the git blob ids of J and of each source)."""
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
    """L(J): the earliest commit C on M's first-parent chain whose tree holds J (at its path, with its blob) and a review
    of J that qualifies under R6.ADJ.7 evaluated over R*(C) with Parties_J(C). `qualifying_review_at(C)` decides the
    second condition (the caller evaluates R6.ADJ.7 over R*(C)). None when there is none."""
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
    """ADJ-ADMIT: J and its cited review lie in the reconciliation directory of J's replacement (R6.ADJ.1)."""
    d = posixpath.dirname(((J.get('replacement') or {}).get('path')) or '')
    out = []
    for r in [jref] + list(review_refs):
        if posixpath.dirname(r.get('path') or '') != d:
            out.append(('ADJ-ADMIT', '%s is not in the reconciliation directory of the replacement' % r.get('path')))
    return out


def citation_problems(cfg_records, jref, qualifying_review_refs):
    """ADJ-ADMIT: the configuration references J with kind adjudication and exactly one qualifying review of J with
    kind review (R6.REC.4; R6.ADJ.11: two cited reviews of J fail)."""
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
    """ADJ-DEDICATED (M5', OD-3): the commit L1 on M's first-parent chain that first holds J's blob at its path differs
    from its first parent only by adding J and that review. No such commit fails."""
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
    """ADJ-CONTRA: `others` is [(J2, validity)] of every other oi-adjudication/1 record in R*, validity 'valid',
    'invalid' (established invalid for adverse use by a definite failure) or 'unknown' (its validity cannot be
    established). A matching upheld record that is not established invalid contradicts J."""
    return [('ADJ-CONTRA', 'a matching upheld adjudication %s' % ('is valid' if v == 'valid' else
                                                                   'cannot be established invalid'))
            for J2, v in others if J2 is not J and isinstance(J2, dict) and J2.get('disposition') == 'upheld'
            and matches(J, J2) and v != 'invalid']


def upheld_blocks_nr5(replacement, witness, finding, upheld_valid):
    """ADJ-UPHELD (OD-6): an upheld adjudication valid for adverse use makes NR-5 false for a replacement and witness
    it matches (with R in place of J.replacement)."""
    probe = {'finding': finding, 'replacement': replacement, 'witness': witness}
    return any(matches(probe, J2) for J2 in upheld_valid)


def adjudicated(admitted_cleared_binding, contradicted):
    """R6.ADJ.9: Adjudicated(W, D) holds exactly when some admitted adjudication that binds D and W, with disposition
    cleared, has no contradiction. `admitted_cleared_binding` lists those adjudications; `contradicted(J)` returns
    ADJ-CONTRA problems. False unless verified records establish it (R6.ADJ.11)."""
    return any(not contradicted(J) for J in admitted_cleared_binding)


# ---- R6.ADJ.12: dissents in four strata ------------------------------------------------------------------------

def strata(pre_admitted, reviews_of, dissents_on_R):
    """R6.ADJ.12 for one discharge D. `pre_admitted` is [{J, ref, binds, landing_index, answered}] of stratum 1 (each
    pre-admitted adjudication with whether it binds D and W and is cleared, `landing_index` the position of L(J) on
    M's first-parent chain, `answered` = Answered(J)); `reviews_of(ref)` lists [{reviewer, verdicts, dissent,
    first_index, ref}] of the reviews of J in R*; `dissents_on_R` is [{reviewer, item, first_index, review}] of the
    dissent items on R. Returns {admitted: [refs], exempt_reviews: {J ref: [review refs]}, disregarded: [dissent
    items], blocking: [dissent items neither addressed nor exempt]}."""
    exempt, admitted = {}, []
    for p in pre_admitted:
        J = p['J']
        ex, ok = [], True
        for rv in reviews_of(p['ref']):
            bad = _adverse_items(rv, J)
            if not bad:
                continue
            later = rv['first_index'] > p['landing_index']
            items_ok = all(i.startswith('ground:') or i in ('disposition', 'dissents') or i == 'dissent' for i in bad)
            if p['binds'] and later and rv.get('reviewer') in p['answered'] and items_ok and \
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
                        (p['J'].get('dissents_addressed') or []) for p in admitted)
        ex = any(p['binds'] and d['first_index'] > p['landing_index'] and d['reviewer'] in p['answered']
                 for p in admitted)
        (disregarded if addressed or ex else blocking).append(d)
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
