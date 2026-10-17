"""Controlled injection of REAL R1 excerpt blobs into copies of the prototype layout; each must fail the recovery
check. Usage: inject_real_excerpt.py CHECKER PROTO_WT SRC_GIT WORKDIR. Nothing here is committed anywhere."""
import hashlib, importlib.util, json, os, shutil, subprocess, sys, zlib
checker, proto, srcgit, work = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('check_objects', checker)
co = importlib.util.module_from_spec(spec); spec.loader.exec_module(co)
EX = [l.strip() for l in open(os.path.join(os.path.dirname(os.path.dirname(srcgit)), '..', 'r1', 'excerpt-blobs.txt')) if l.strip()]
def blob(oid):
    return subprocess.run(['git', '--git-dir', srcgit, 'cat-file', 'blob', oid], capture_output=True).stdout
objdir0 = os.path.join(proto, 'verification/audits/evidence-retention/objects')
res = []
def case(name, mutate, history=False):
    d = os.path.join(work, 'case')
    shutil.rmtree(d, ignore_errors=True); shutil.copytree(objdir0, d)
    man = json.load(open(os.path.join(d, 'manifest.json')))
    mutate(d, man)
    json.dump(man, open(os.path.join(d, 'manifest.json'), 'w'), indent=1, sort_keys=True)
    fails, _ = co.check_with(d, proto, history, co.Fails())
    res.append((name, [f for f in fails if f[:2] in ('O5', 'H6')][:2] or fails[:2]))
x1, x2 = EX[0], EX[1]
def raw(d, man):
    data = blob(x1); rel = 'blob/%s/%s' % (x1[:2], x1)
    os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True); open(os.path.join(d, rel), 'wb').write(data)
    man['objects'].append({'oid': x1, 'type': 'blob', 'mechanism': 'byte-copy', 'form': 'raw', 'file': rel,
                           'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'tranche': 1})
def loose(d, man):
    data = blob(x2); body = zlib.compress(b'blob %d\0' % len(data) + data, 9); rel = 'loose/%s/%s' % (x2[:2], x2[2:])
    os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True); open(os.path.join(d, rel), 'wb').write(body)
    man['objects'].append({'oid': x2, 'type': 'blob', 'mechanism': 'byte-copy', 'form': 'zlib', 'file': rel,
                           'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest(), 'tranche': 1})
def unlisted_bytes(d, man):
    open(os.path.join(d, 'blob', 'note'), 'wb').write(blob(x1))     # the excerpt's bytes under another name
def tree(d, man):
    t = b'100644 excerpt.log\0' + bytes.fromhex(x1)
    oid = hashlib.sha1(b'tree %d\0' % len(t) + t).hexdigest(); body = zlib.compress(b'tree %d\0' % len(t) + t, 9)
    rel = 'loose/%s/%s' % (oid[:2], oid[2:])
    os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True); open(os.path.join(d, rel), 'wb').write(body)
    man['objects'].append({'oid': oid, 'type': 'tree', 'mechanism': 'raw', 'form': 'zlib', 'file': rel, 'cited': [],
                           'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest(), 'tranche': 1})
case('a real excerpt stored as a raw byte copy', raw)
case('a real excerpt stored as a zlib loose object', loose)
case('a real excerpt\'s bytes as an unlisted file', unlisted_bytes)
case('a retained tree naming a real excerpt', tree)
for n, f in res:
    print('%-50s %s' % (n, f))
