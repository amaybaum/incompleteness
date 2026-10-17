"""Write the prototype layout of the proposed PR, and the full preservation manifest.

  layout/verification/audits/evidence-retention/objects/
      manifest.json                    what the PR would commit (no local paths, no host-state claims beyond dates)
      blob/<aa>/<oid>                  a blob's bytes, unmodified
      tree/<aa>/<oid>                  a tree object's content (the bytes after git's "tree <len>\\0" header)
      commit/<aa>/<oid>                a commit object's content (likewise)
  manifest.json                        the deliverable: every object, its citations, holders, mechanism and size

Never committed anywhere. Reads work/union-stage1.json, work/plan.json and the source repository.
"""
import collections, datetime, hashlib, json, os, shutil, sys, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import Store

O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(O)
W = os.path.join(O, 'work')
REL = 'verification/audits/evidence-retention/objects'
OUT = os.path.join(O, 'layout', REL)
MAIN = '66a981d5a9cab35b9ebd253aa0e610c0afbfefb6'
src = Store(os.path.join(W, 'src.git'))
U = json.load(open(os.path.join(W, 'union-stage1.json')))['objects']
PL = json.load(open(os.path.join(W, 'plan.json')))
P = PL['objects']
EXCERPTS = sorted(l.strip() for l in open(os.path.join(S, 'r1', 'excerpt-blobs.txt')) if l.strip())
HOST_TIME = open(os.path.join(W, 'hostcheck.time')).read().strip()
REFS_TIME = open(os.path.join(W, 'host-refs.time')).read().strip()
TRANCHE = {'host-unreferenced': 1, 'local-only': 1, 'pull-ref': 2, 'branch': 3}
STORED = ('byte-copy', 'raw', 'raw:proof-path')

def is_stored(r):
    return r['type'] == 'commit' or r['mechanism'] in STORED

FORM = os.environ.get('LAYOUT_FORM', 'hybrid')     # raw | hybrid | zlib

def form(r):
    """raw: the object content, unmodified (a blob's bytes; a commit's text; a tree's binary entries).
    zlib: a git loose object, zlib(\"<type> <size>\\0\" + content), droppable into .git/objects."""
    if FORM == 'raw':
        return 'raw'
    if FORM == 'zlib':
        return 'zlib'
    return 'raw' if r['type'] == 'commit' or (r['type'] == 'blob' and r.get('cited')) else 'zlib'

def relpath(r):
    if form(r) == 'zlib':
        return f"loose/{r['oid'][:2]}/{r['oid'][2:]}"
    return f"{r['type']}/{r['oid'][:2]}/{r['oid']}"

# tranche: a cited object by its own holder; a dependency by the most at-risk cited object that needs it
need_of = collections.defaultdict(set)
for oid, r in P.items():
    for by, _ in r['needed_by']:
        need_of[oid].add(by)
def tranche(oid, seen=()):
    r = P[oid]
    ts = [TRANCHE[r['holder']]] if r.get('cited') else []
    ts += [tranche(b, seen + (oid,)) for b in need_of[oid] if b not in seen]
    return min(ts) if ts else TRANCHE[r['holder']]

# identities in stored commit headers (digests only in the PR manifest)
def identities(data):
    out = set()
    text = data.decode('utf-8', 'surrogateescape')
    head, _, msg = text.partition('\n\n')
    for l in head.split('\n'):
        if l.startswith(('author ', 'committer ', 'tagger ')):
            out.add(l[l.index('<') + 1:l.index('>')])
    for l in msg.split('\n'):
        if l.lower().startswith('co-authored-by:') and '<' in l:
            out.add(l[l.index('<') + 1:l.index('>')])
    return out

if os.path.isdir(OUT):
    shutil.rmtree(OUT)          # this script's own output directory only (the checker beside it is kept)
os.makedirs(OUT)
ids = set()
entries, withheld = [], []
raw_total = zlib_total = 0
for oid in sorted(P):
    r = P[oid]
    t, data = src.read(oid)
    ent = {'oid': oid, 'type': t, 'mechanism': r['mechanism'], 'tranche': tranche(oid)}
    if r.get('cited'):
        ent['cited'] = [{k: c[k] for k in ('location', 'class', 'role', 'via', 'run', 'range_member', 'tokens') if c.get(k)}
                        for c in U[oid]['citations']]
    if r['needed_by']:
        byc = collections.defaultdict(set)
        for by, p in r['needed_by']:
            byc[by].add(p)
        ent['needed_by'] = sorted(({'object': b, 'path': sorted(ps)[0]} for b, ps in byc.items()),
                                  key=lambda x: x['object'])
    if t == 'commit':
        ent['parents'] = r['parents']
        if r.get('parents_not_retained'):
            ent['parents_not_retained'] = r['parents_not_retained']
        if r.get('withheld_blobs'):
            ent['withheld_blobs'] = r['withheld_blobs']
        if r.get('inclusion_paths'):
            ent['inclusion_paths'] = r['inclusion_paths']
        if r.get('anchor_reason'):
            ent['anchor_reason'] = r['anchor_reason']
        ids |= identities(data)
    if is_stored(r):
        p = os.path.join(OUT, relpath(r))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        body = data if form(r) == 'raw' else zlib.compress(t.encode() + b' %d\0' % len(data) + data, 9)
        open(p, 'wb').write(body)
        ent['file'] = relpath(r)
        ent['form'] = form(r)
        ent['bytes'] = len(body)
        ent['sha256'] = hashlib.sha256(body).hexdigest()
        ent['content_bytes'] = len(data)
        ent['content_sha256'] = hashlib.sha256(data).hexdigest()
        raw_total += len(data)
        zlib_total += len(body)
    else:
        ent['bytes'] = len(data)
        ent['paths'] = r['paths']
        withheld.append(oid)
    entries.append(ent)

pr_manifest = {
    'schema': 'oi-evidence-objects', 'version': 1, 'tranche_of_archive': 2,
    'base': MAIN,
    'object_format': 'sha1; a stored file holds the object content without git\'s "<type> <size>\\0" header; '
                     'its id is sha1("<type> <size>\\0" + content)',
    'mechanisms': {
        'raw:connected': 'commit with every tree and blob main lacks; every parent on main or a retained connected commit',
        'raw:tree': 'commit with every tree and blob main lacks; parents_not_retained are named, not retained',
        'raw:partial-tree': 'commit with every tree; withheld_blobs are named by id, not retained',
        'inclusion-proof': 'commit, root tree, the trees on each inclusion path and what lies under it',
        'identity-anchor': 'the commit object only',
        'raw': 'a tree object, retained with everything under it that main lacks',
        'raw:proof-path': 'a tree on an inclusion path: its entries off the path are named, not retained',
        'byte-copy': 'a blob, byte for byte',
        'withheld:raw-log': 'a raw log or transcript (AGENTS §A.42 item 1): named by id and size, not retained',
        'withheld:build-pdf': 'a build output whose bytes no record freezes: named by id and size, not retained'},
    'host_state': {'refs_listed_at': REFS_TIME, 'by_sha_served_at': HOST_TIME},
    'identities_sha256': sorted(hashlib.sha256(i.encode()).hexdigest() for i in ids),
    'excerpt_denylist_sha256_of_id': sorted(hashlib.sha256(e.encode()).hexdigest() for e in EXCERPTS),
    'scan_exemptions': ['the author, committer and tagger header lines of a commit, and its Co-Authored-By trailers, '
                        'when the address digest is in identities_sha256',
                        'the gpgsig header block of a commit (a signature, not a key)',
                        'e-mail addresses in the reserved domains example.invalid, example.com, example.org, '
                        'example.net and *.test, *.invalid (RFC 2606, RFC 6761)'],
    'id_discrepancies': [
        {'location': loc, 'cited_id': cited, 'retained_id': true, 'run': run,
         'basis': 'the cited id names no object on the host or in any local store; the run\'s head commit, read from '
                  'the host\'s runs API, shares its first eight hex digits and has the subject the citing line '
                  'describes; the host resolves the eight-digit prefix to it'}
        for loc, cited, true, run in (
            ('verification/programmes/oi-qm/track-b/act-35-dita-hull/result.md:218',
             '2ae4dbeef5d9a1c9f0fcf3fbbf1ceaf4de4d3a0d', '2ae4dbeeceae2b2e66bd43658045b67da0f0e650', '36310787113'),
            ('verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/preregistration.md:710',
             '4c4155da7ccc2cf47d63bfe2ce7d8c4cba7f0ff2', '4c4155da059388a4724039fd5e60aaa96965f7c3', '36257341185'),
            ('verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/preregistration.md:711',
             'cff3c1560f4c0fc09aba2c8af06e9f00e0fc0cd7', 'cff3c1566228158acbf6cb710dbdf4ba4c5db91f', '36257659584'),
            ('verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/preregistration.md:400',
             'ad64b60319e1ff2d40a5a5eed8e3aa4bfcf30b0e', 'ad64b603b7a1dac18b7246d339abaf43a3642dd3', '36612901341'))],
    'objects': entries,
}
json.dump(pr_manifest, open(os.path.join(OUT, 'manifest.json'), 'w'), indent=1, sort_keys=True)
open(os.path.join(OUT, 'manifest.json'), 'a').write('\n')

# ---- the deliverable manifest, with holders and local copies
deliv = []
for ent in entries:
    r = P[ent['oid']]; u = U.get(ent['oid'], {})
    d = dict(ent)
    d['size'] = r['size']
    d['zlib_bytes'] = r['zlib_bytes']
    d['holder'] = {'state': r['holder']}
    if r['holder'] == 'branch' or r['holder'] == 'pull-ref':
        pass  # filled below
    if r['holder'] == 'host-unreferenced':
        d['holder']['host_by_sha'] = 'served ' + HOST_TIME
    d['local_copies'] = r['local_copies']
    d['why'] = ('cited' if r.get('cited') else 'dependency of ' + ', '.join(sorted({x['object'][:12] for x in ent.get('needed_by', [])})[:5]) +
                (' …' if len(ent.get('needed_by', [])) > 5 else ''))
    if u:
        d['inputs'] = u['inputs']
        if u.get('survey'):
            d['survey'] = {k: u['survey'][k] for k in ('universe', 'role', 'proposed_mechanism')}
    d['mechanism_reason'] = {
        'raw:connected': 'parents on main or retained and connected: reconstitutes the exact commit, fully connected',
        'raw:tree': 'a parent is off main and not retained: commit id and complete tree verified, parent named',
        'raw:partial-tree': 'its tree holds raw logs or build PDFs, which are not committed: ids verified, entries named',
        'inclusion-proof': 'research-archive commit (236+ MB tree, 330+ logs): only the cited paths are retained',
        'identity-anchor': 'research-archive commit cited for identity, parents and dates only',
        'raw': 'tree object needed to verify a retained commit or cited tree',
        'raw:proof-path': 'tree on the path from a research-archive commit to a cited file: siblings named only',
        'byte-copy': 'restores the blob id on main and lets frozen controls read it with git cat-file',
        'withheld:raw-log': 'AGENTS §A.42 item 1: a raw log or transcript is not committed; no frozen record pins it',
        'withheld:build-pdf': 'build output, bytes not frozen by any record: provenance only, owner decision',
    }[r['mechanism']]
    deliv.append(d)
json.dump({'deliv': deliv, 'ids': sorted(ids)}, open(os.path.join(W, 'layout-stage.json'), 'w'), indent=1)
print('entries', len(entries), 'stored', len(entries) - len(withheld), 'withheld', len(withheld))
print('form', FORM, 'content bytes', raw_total, 'stored bytes', zlib_total, 'identities', len(ids))
