# The OBL-29 remedy r9, sec. 2.2: reliance on a retained witness's disputed basis, non-reliance evidence NR-1 to
# NR-5, the token rule and the decision `blocked(D, W)`.
#
# These are the mechanical predicates of sec. 2.2 over explicit records. A run calls `decide` for the witnesses custody
# supplies (R6.CUST.6, category3.custody_decisions). Route 2 (adjudication) is `Adjudicated(W, D)` of #1605 R6.ADJ.9,
# which the caller establishes from admitted records (engine/adjudication.py) and passes as `adjudicated`; it is false
# unless verified records establish it.
#
# A witness W is a dict:
# kind: 'lineage' or 'review';
# disputed: {path, blob_sha256} of the disputed record, disputed_doc its parsed content, disputed_git its git blob id;
# edge: (successor blob sha256, predecessor blob sha256) of the exact disputed edge, or None;
# forming: [{doc, git, path}] of the records forming the witness (the competing successor, or the adverse review V);
# contested: [blob sha256] of the predecessors a retained competing-successor witness rests on, or whose own retained
# adverse review forms a witness;
# original: (finding reference, item) the original operative discharge named;
# inapplicable: True only when verified records establish that its original qualification does not reproduce.
# A candidate discharge D is a dict:
# reassessment: its doc and ref; finding: (reference, item); repair: None or {entry ref, entry doc (the cited record),
# entry_path, commits}; lineage_blobs: [blob sha256] of its repair record's and reassessment's resolved lineages,
# lineage_edges: [(successor, predecessor)] of those lineages, unresolved: True when a required reference does not
# resolve.
# A replacement R is {ref, doc, lineage_blobs, lineage_edges}. A review passed to NR-3 or NR-5 is its parsed content
# with `_dir`, the directory of its path, added by the caller.
import re

from . import findings as fd
from . import records as rec

_split = re.compile(r'[ \t\n\r]+')
_hex40 = re.compile(r'^[0-9a-f]{40}$')
_split_char = re.compile(r'[ \t\n\r]')


def tokens(value):
    """The elements of a field under the token rule: its string value split at every run of space, tab, line feed and
    carriage return. A value that is not a string holds no token."""
    if not isinstance(value, str):
        return set()
    return {t for t in _split.split(value) if t}


def holds(value, token):
    """A field holds a token when one element equals the token byte for byte (no case change, abbreviation,
    punctuation or other spelling)."""
    return token in tokens(value)


def item_token(blob_git, item):
    """`<b>#<item>`: a git blob id (40 lowercase hex), `#` and the exact item id; None when either part cannot form a
    token (an item id with a splitting character cannot be matched)."""
    if not isinstance(blob_git, str) or not _hex40.match(blob_git) or not isinstance(item, str) or not item or \
            _split_char.search(item):
        return None
    return '%s#%s' % (blob_git, item)


def adverse_items(review, reviewed_doc):
    """The items that make a review adverse or defective: a verdict other than accept, an omitted item, or a
    duplicated item; and 'dissent' when its dissent field is non-empty."""
    ids = rec.item_ids(reviewed_doc) if isinstance(reviewed_doc, dict) else []
    verdicts = {}
    for v in review.get('verdicts') or []:
        if isinstance(v, dict):
            verdicts.setdefault(v.get('item'), []).append(v.get('verdict'))
    out = []
    for i in ids:
        if i not in verdicts or len(verdicts[i]) != 1 or verdicts[i][0] != 'accept':
            out.append(i)
    if isinstance(review.get('dissent'), str) and review['dissent'].strip():
        out.append('dissent')
    return out


def dissents(review):
    """A review with a non-empty dissent field counts as dissenting, an accepting review included."""
    return isinstance(review, dict) and isinstance(review.get('dissent'), str) and bool(review['dissent'].strip())


# ---- reliance ----------------------------------------------------------------------------------------------------

def reliance(D, W):
    """The clauses of (r1)-(r3) through which D relies on W's disputed basis; ['undecidable'] when a required record
    or lineage reference does not resolve (which counts as reliance)."""
    if D.get('unresolved'):
        return ['undecidable']
    out = []
    dis = W['disputed']['blob_sha256']
    rep = D.get('repair')
    if rep and (rep.get('entry') or {}).get('blob_sha256') == dis:
        out.append('r1')
    if dis in (D.get('lineage_blobs') or []) or (W.get('edge') and tuple(W['edge']) in
                                                  {tuple(e) for e in D.get('lineage_edges') or []}):
        out.append('r2')
    if rep:
        mine = set(rep.get('commits') or [])
        doc = rep.get('entry_doc') or {}
        for e in doc.get('paths') or []:
            if isinstance(e, dict) and e.get('path') == rep.get('entry_path'):
                mine |= set(e.get('side_change_commits') or [])
        theirs = set()
        for e in (W.get('disputed_doc') or {}).get('paths') or []:
            if isinstance(e, dict):
                theirs |= set(e.get('side_change_commits') or [])
        if tuple(D.get('finding') or ()) == tuple(W.get('original') or ()) or (mine & theirs):
            out.append('r3')
    return out


# ---- non-reliance evidence ----------------------------------------------------------------------------------------

def nr1(R, W):
    """R and every record of its resolved lineage differ in blob from the disputed record, the lineage holds no
    disputed edge, and no record of it names in supersedes a contested predecessor."""
    blobs = set(R.get('lineage_blobs') or []) | {R['ref']['blob_sha256']}
    if W['disputed']['blob_sha256'] in blobs:
        return False
    if W.get('edge') and tuple(W['edge']) in {tuple(e) for e in R.get('lineage_edges') or []}:
        return False
    named = {e[1] for e in R.get('lineage_edges') or []}
    return not (named & set(W.get('contested') or []))


def nr3(R, review, excluded, reviews_of_R):
    # An accepting same-directory review of R's exact reference meeting R6.REC.6, by a reviewer outside `excluded`
    # (the authors of R, the reassessment, the disputed record, the contested predecessor and each record forming the
    # witness, and the reviewers of the witness's reviews and of each accepting review of the disputed record); no
    # eligible review of R in R* dissents.
    if not isinstance(review, dict) or review.get('reviewed') != R['ref'] or \
            review.get('_dir') != R['ref']['path'].rsplit('/', 1)[0]:
        return False
    # staging S-2 sec. 5: the NR-3 reviewer is independent (S2.4) of every excluded party
    if fd.independence_problems(review, excluded):
        return False
    if adverse_items(review, R['doc']):
        return False
    return not any(dissents(v) or adverse_items(v, R['doc']) for v in reviews_of_R)


def nr4(review, W):
    """The method of the required review holds the git blob id of the disputed record and of each record forming the
    witness."""
    m = (review or {}).get('method')
    return holds(m, W['disputed_git']) and all(holds(m, x['git']) for x in W.get('forming') or [])


def nr5(Z, V, W, R, D, finding_git, reviews_of_R):
    """Z explicitly resolves the adverse review V forming a review witness; every condition is mechanical. Returns
    [] when Z resolves V, else the failed conditions."""
    bad = []
    who = V['doc'].get('reviewer')
    if not rec._person(who):
        return ['V has no usable reviewer identity']
    adverse = adverse_items(V['doc'], W.get('disputed_doc'))
    toks = []
    for i in adverse:
        t = item_token(V['git'], i)
        if t is None:
            return ['an adverse item id of V cannot form a token']
        toks.append(t)
    if not isinstance(Z, dict) or not fd.same_identity(Z.get('reviewer'), who):
        bad.append("Z's reviewer is not V's reviewer")
    authors = {R['doc'].get('author'), (W.get('disputed_doc') or {}).get('author'),
               (D.get('reassessment') or {}).get('doc', {}).get('author')}
    if isinstance(Z, dict) and any(fd.same_identity(Z.get('reviewer'), author) for author in authors):
        bad.append("Z's reviewer is an author of R, the disputed record or the reassessment")
    if isinstance(Z, dict) and (fd.declared_dependency(Z, authors) or not fd.declaration_ok(Z.get('independence'))):
        # staging S-2 sec. 5: Z is independent (S2.4) of those authors
        bad.append("Z's independence declaration is missing or malformed, or names an author of R, the disputed "
                   "record or the reassessment")
    if not isinstance(Z, dict) or Z.get('_dir') != R['ref']['path'].rsplit('/', 1)[0] or Z.get('kind', 'review') != \
            'review' or adverse_items(Z, R['doc']):
        bad.append('Z does not meet the record lint in R\'s reconciliation directory')
    # NR-3's test: a review dissents when its dissent field is non-empty or it does not accept every item of R
    if any(dissents(v) or adverse_items(v, R['doc']) for v in list(reviews_of_R) + [Z or {}]):
        bad.append('an eligible review of R dissents')
    entry = ((D.get('repair') or {}).get('entry')) or {}
    if not isinstance(Z, dict) or Z.get('reviewed') != R['ref'] or entry != R['ref']:
        bad.append("Z's reviewed or the reassessment's repair entry is not R's exact reference")
    method = (Z or {}).get('method')
    if not all(holds(method, t) for t in toks):
        bad.append("Z's method lacks a <b>#<item> token of V")
    ep = (D.get('repair') or {}).get('entry_path')
    for item in (ep, '%s:scientific_effect' % ep):
        vs = [v for v in (Z or {}).get('verdicts') or [] if isinstance(v, dict) and v.get('item') == item]
        if len(vs) != 1 or vs[0].get('verdict') != 'accept' or not (isinstance(vs[0].get('reason'), str) and
                                                                     vs[0]['reason'].strip()) or \
                not all(holds(vs[0]['reason'], t) for t in toks):
            bad.append('the verdict on %s does not accept with a reason holding every token' % item)
    fref, fitem = D.get('finding') or (None, None)
    if fitem is None:
        ftok = finding_git if isinstance(finding_git, str) and _hex40.match(finding_git) else None
    else:
        ftok = item_token(finding_git, fitem)
    if ftok is None or not holds(method, ftok):
        bad.append("Z's method lacks the token of the finding the reassessment discharges")
    return bad


def decide(D, W, R=None, Z=None, required_review=None, excluded=(), reviews_of_R=(), nr2=False, finding_git=None,
           adjudicated=False):
    # blocked(D, W) = Relies(D, W) and not Cleared(D, W). Returns (blocked, clauses, route). `nr2` states whether
    # the candidate freeze admits R through an existing route making R's own R6.REC.6 and R6.REC.7 checks operative
    # (an admission fact the caller establishes). `Z` is a review of R or a list of them (one may resolve each V).
    clauses = reliance(D, W)
    if not clauses:
        return False, [], None
    if W.get('inapplicable') is True:
        return False, clauses, 'inapplicable'
    if adjudicated:
        # route 2 (#1605 R6.ADJ.9): Adjudicated(W, D), established by the caller from admitted records
        return False, clauses, 'adjudication'
    only_r3 = clauses == ['r3']
    if only_r3 and R is not None and nr1(R, W) and nr2:
        if W['kind'] == 'lineage':
            if nr3(R, required_review, excluded, reviews_of_R) and nr4(required_review, W):
                return False, clauses, 'non-reliance (NR-1 to NR-4)'
        elif W['kind'] == 'review':
            # NR-5 for each adverse or failed review V forming the witness: some review Z of R resolves that V, and
            # NR-4 holds for it
            zs = Z if isinstance(Z, (list, tuple)) else [Z]
            forming = W.get('forming') or []
            if forming and all(any(z is not None and nr4(z, W) and not nr5(z, v, W, R, D, finding_git, reviews_of_R)
                                   for z in zs) for v in forming):
                return False, clauses, 'explicit resolution (NR-1, NR-2, NR-4, NR-5)'
    return True, clauses, None
