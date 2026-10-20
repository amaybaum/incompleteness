#!/usr/bin/env python3
"""closure.py -- tranche-2 pilot: select the head by rule S and compute its object/byte closure.

Usage: python3 -I -B closure.py <archive-dir> <out.json>

<archive-dir> is a copy of verification/audits/evidence-retention/ (manifest blob 2ee4fbb9...).
Reads only the archive's own files: stored objects are decoded from objects/ and every id is re-hashed.
Ids a retained tree names that the archive does not retain are reported as 'outside' (expected on main;
checked separately by regen.sh).
"""
import hashlib
import json
import os
import sys
import zlib

ARCH = sys.argv[1]
OUT = sys.argv[2]
man = json.load(open(os.path.join(ARCH, 'objects', 'manifest.json')))
objs = man['objects']
by = {x['oid']: x for x in objs}


def content(e):
    """Return (type, content) of a stored entry, verifying its id."""
    data = open(os.path.join(ARCH, 'objects', e['file']), 'rb').read()
    if e['form'] == 'raw':
        typ, body = e['type'], data
    else:
        raw = zlib.decompress(data)
        hdr, body = raw.split(b'\0', 1)
        typ = hdr.split(b' ')[0].decode()
    oid = hashlib.sha1(b'%s %d\0' % (typ.encode(), len(body)) + body).hexdigest()
    assert oid == e['oid'] and typ == e['type'], (e['oid'], oid)
    return typ, body


def tree_entries(body):
    i, out = 0, []
    while i < len(body):
        sp = body.index(b' ', i)
        nul = body.index(b'\0', sp)
        mode = body[i:sp].decode()
        name = body[sp + 1:nul].decode('utf-8', 'surrogateescape')
        oid = body[nul + 1:nul + 21].hex()
        out.append((mode, name, oid))
        i = nul + 21
    return out


def commit_fields(body):
    tree, parents = None, []
    for line in body.split(b'\n'):
        if not line:
            break
        if line.startswith(b'tree '):
            tree = line[5:].decode()
        elif line.startswith(b'parent '):
            parents.append(line[7:].decode())
    return tree, parents


def walk(commit_oid):
    """Every object the commit's root tree names, with path and status."""
    _, cb = content(by[commit_oid])
    root, parents = commit_fields(cb)
    rows = []
    stack = [(root, '', '40000')]
    while stack:
        oid, path, mode = stack.pop()
        e = by.get(oid)
        kind = 'tree' if mode == '40000' else ('gitlink' if mode == '160000' else 'blob')
        if e is None:
            status = 'outside'
        elif e.get('file'):
            status = 'stored'
        else:
            status = 'withheld'
        rows.append({'oid': oid, 'path': path or '/', 'mode': mode, 'kind': kind, 'status': status})
        if kind == 'tree' and status == 'stored':
            _, tb = content(e)
            for m, n, o in tree_entries(tb):
                stack.append((o, (path + n + '/') if m == '40000' else path + n, m))
    return root, parents, rows


def select():
    frozen = ('native-record', 'legacy-record')
    for x in objs:
        if x['tranche'] == 2 and x['type'] == 'commit' and x.get('cited') and any(
                c['class'] in frozen and ':' in c['location'] for c in x['cited']):
            return x['oid']


h = select()
root, parents, rows = walk(h)
# history sub-closure: retained raw:connected ancestors down to the base
chain, cur = [], parents
while cur:
    nxt = []
    for p in cur:
        e = by.get(p)
        if e and e['type'] == 'commit':
            chain.append(p)
            nxt += commit_fields(content(e)[1])[1]
    cur = nxt
# which retained commits name each retained object (by walking every retained commit's retained trees)
named_by = {}
for x in objs:
    if x['type'] == 'commit' and x.get('file'):
        try:
            _, _, rs = walk(x['oid'])
        except Exception as exc:  # inclusion-proof path trees are partial; skip names they omit
            rs = []
        for r in rs:
            if r['status'] != 'outside':
                named_by.setdefault(r['oid'], set()).add(x['oid'])
anc_rows = {}
for a in chain:
    anc_rows[a] = [r for r in walk(a)[2] if r['status'] != 'outside']

own = {r['oid'] for r in rows if r['status'] != 'outside'} | {h}
res = {
    'head': h, 'root_tree': root, 'parents': parents,
    'retained_ancestors': chain,
    'tree_rows': rows,
    'ancestor_retained_rows': anc_rows,
    'entries': {o: {k: by[o][k] for k in ('type', 'mechanism', 'bytes', 'content_bytes', 'file', 'needed_by', 'cited', 'tranche') if k in by[o]}
                | {'named_by_commits': sorted(named_by.get(o, set()))} for o in sorted(own)},
}
json.dump(res, open(OUT, 'w'), indent=1, sort_keys=True)
st = {}
for r in rows:
    st.setdefault((r['kind'], r['status']), [0, set()])
    st[(r['kind'], r['status'])][1].add(r['oid'])
print('head', h, 'root', root, 'parents', parents)
print('retained ancestors (raw:connected chain):', chain)
for k in sorted(st):
    print(k, 'distinct ids', len(st[k][1]))
stored = [o for o in own if by[o].get('file')]
print('own retained entries', len(own), 'stored', len(stored), 'stored bytes', sum(by[o]['bytes'] for o in stored),
      'content bytes', sum(by[o]['content_bytes'] for o in stored))
print('shared with other retained commits:', sum(1 for o in own if named_by.get(o, set()) - {h}))
