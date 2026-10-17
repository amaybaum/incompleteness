"""Independent reconstitution control: zlib files are copied into .git/objects unread (git itself parses them), raw
files are written with git hash-object; then git fsck --full, with and without the shallow boundaries, and with the
partial-tree commits, as a countercontrol. Usage: independent_control.py OBJDIR SEED_OBJECTS WORKDIR"""
import json, os, shutil, subprocess, sys
objdir, seed, work = sys.argv[1:4]
man = json.load(open(os.path.join(objdir, 'manifest.json')))
E = {e['oid']: e for e in man['objects']}
def git(*a, inp=None):
    return subprocess.run(['git', '--git-dir', g] + list(a), input=inp, capture_output=True)
res = {}
def fresh(name):
    global g
    g = os.path.join(work, name)
    shutil.rmtree(g, ignore_errors=True)
    subprocess.run(['git', 'init', '-q', '--bare', g], check=True)
    open(os.path.join(g, 'objects', 'info', 'alternates'), 'w').write(seed + '\n')
    for e in man['objects']:
        if not e.get('file'):
            continue
        src = os.path.join(objdir, e['file'])
        if e['form'] == 'zlib':
            d = os.path.join(g, 'objects', e['oid'][:2]); os.makedirs(d, exist_ok=True)
            shutil.copyfile(src, os.path.join(d, e['oid'][2:]))
        else:
            out = git('hash-object', '-w', '-t', e['type'], src).stdout.decode().strip()
            assert out == e['oid'], (e['oid'], out)
    chk = git('cat-file', '--batch-check', inp=''.join(o + '\n' for o, e in E.items() if e.get('file')).encode()).stdout.decode()
    ok = sum(1 for l in chk.split('\n') if l and 'missing' not in l and l.split()[0] in E)
    return ok
def refs(sel):
    git('update-ref', '--stdin', inp=''.join('create refs/r/%s %s\n' % (o, o) for o in sel).encode())
def fsck():
    p = git('fsck', '--full', '--no-dangling', '--no-progress')
    return p.returncode, [l for l in p.stderr.decode().split('\n') if l][:3], len([l for l in (p.stdout + p.stderr).decode().split('\n') if 'missing' in l])
M = lambda m: [o for o, e in E.items() if e['mechanism'] == m]
n = fresh('ctl-connected'); refs(M('raw:connected'))
res['A raw:connected commits only, no shallow file'] = (n,) + fsck()
fresh('ctl-tree-noshallow'); refs(M('raw:tree'))
res['B raw:tree commits, no shallow file (countercontrol: must fail)'] = (None,) + fsck()
fresh('ctl-tree-shallow'); refs(M('raw:tree') + M('raw:connected'))
open(os.path.join(g, 'shallow'), 'w').write(''.join(o + '\n' for o in M('raw:tree')))
res['C raw:connected + raw:tree, raw:tree commits shallow'] = (None,) + fsck()
fresh('ctl-partial'); refs(M('raw:partial-tree'))
open(os.path.join(g, 'shallow'), 'w').write(''.join(o + '\n' for o in M('raw:partial-tree')))
rc, first, nmiss = fsck()
want = sum(len(E[o]['withheld_blobs']) for o in M('raw:partial-tree'))
res['D raw:partial-tree commits, shallow (countercontrol: must fail on exactly the withheld blobs)'] = (None, rc, first, nmiss, 'withheld blobs listed: %d' % len(set(b for o in M('raw:partial-tree') for b in E[o]['withheld_blobs'])))
fresh('ctl-bg3')
for c in ('6c160ad26a9831448e6e4cfca5761efb876a1baf', 'e3ef9358d6690220c21a9b32924af9b3f70cb890', '3218e8d052e01650baae645e7eb92355e56e7b34'):
    t = git('rev-parse', c + '^{tree}').stdout.decode().strip()
    ls = git('ls-tree', '-r', c).returncode
    res['E BG-3 ' + c[:8]] = (E[c]['mechanism'], 'commit^{commit} ok' if git('cat-file', '-e', c + '^{commit}').returncode == 0 else 'MISSING',
                              'tree ' + t[:8], 'ls-tree -r rc=%d' % ls,
                              'parent on main' if git('merge-base', '--is-ancestor', c + '^', man['base']).returncode == 0 else 'parent off main')
for k, v in res.items():
    print(k, '->', v)
