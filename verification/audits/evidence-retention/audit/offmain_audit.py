"""Read-only audit: references in main's tracked text that depend on content not retained on main.

Classes:
  P  local/temporary paths (/tmp/, scratchpad, /root/, /home/)
  B  names of branches other than main (pattern <prefix>/<name>), and whether they still exist
  C  commit ids (abbreviated or full) that resolve to a commit not reachable from main
  O  blob/tree ids that resolve to an object not reachable from main
  D  64-hex digests cited under verification/ that equal the sha256 of no file tracked at MAIN
Hex tokens of 7-40 characters that resolve to no object are not reported (they are digests or other numbers).
Paths are taken exactly as git lists them (repository-relative); no directory prefix is added to them.
Usage: offmain_audit.py MAIN   (run from a clone with every remote branch fetched)
"""
import re, subprocess, sys, collections, json
MAIN = sys.argv[1]
def run(*a, inp=None):
    return subprocess.run(a, input=inp, capture_output=True, text=True, check=False).stdout
files = [f for f in run('git','ls-tree','-r','--name-only',MAIN).split('\n') if f]
skip_ext = ('.pdf','.tex','.olean','.png','.jpg','.gz','.zip','.ilean')
files = [f for f in files if not f.endswith(skip_ext)]
reach = set(l.split()[0] for l in run('git','rev-list','--objects',MAIN).split('\n') if l)
branches = set(l.strip().replace('origin/','',1) for l in run('git','branch','-r').split('\n') if l.strip() and '->' not in l)
hexre = re.compile(r'(?<![0-9A-Za-z])[0-9a-f]{7,40}(?![0-9A-Za-z])')
pathre = re.compile(r'(/tmp/|scratchpad|/root/|/home/user)')
brre = re.compile(r'(?<![\w/.-])((?:tmp|build|research|plan|draft|codex|docs|fix|feat|pr|exp|archive)/[A-Za-z0-9._-]+)')
tokens = collections.defaultdict(list)
P=[]; B=[]
for f in files:
    try: txt = subprocess.run(['git','show',f'{MAIN}:{f}'],capture_output=True,check=True).stdout.decode('utf-8')
    except Exception: continue
    for i,line in enumerate(txt.split('\n'),1):
        if pathre.search(line): P.append((f,i,line.strip()[:160]))
        for m in brre.finditer(line):
            name=m.group(1).rstrip('.,;:)`\'"')
            if '/' in name and not name.endswith(('.md','.py','.lean','.json')) and re.search(r'\d{6,8}|[a-z]-[a-z]', name):
                B.append((f,i,name, name in branches))
        for m in hexre.finditer(line):
            tokens[m.group(0)].append((f,i))
# resolve tokens in batch
names = list(tokens)
out = run('git','cat-file','--batch-check=%(objectname) %(objecttype)', inp='\n'.join(names)+'\n').split('\n')
C=[]; O=[]
for tok, res in zip(names, out):
    parts = res.split()
    if len(parts)!=2 or parts[1] not in ('commit','tree','blob','tag'): continue
    oid, typ = parts
    if typ=='commit':
        anc = subprocess.run(['git','merge-base','--is-ancestor',oid,MAIN]).returncode==0
        if not anc: C.append((tok,oid,tokens[tok]))
    else:
        if oid not in reach: O.append((tok,oid,typ,tokens[tok]))
def cont(oid):
    r = run('git','branch','-r','--contains',oid).split()
    return [x.replace('origin/','',1) for x in r if x!='->']
print('== P: local/temporary paths: %d lines' % len(P))
for f,i,l in P: print('  %s:%d  %s' % (f,i,l))
print('== B: non-main branch names: %d mentions' % len(B))
seen=collections.Counter((n,e) for _,_,n,e in B)
for (n,e),c in sorted(seen.items()): print('  %-55s %s  x%d' % (n, 'exists' if e else 'GONE', c))
print('== C: commits not reachable from main: %d' % len(C))
for tok,oid,locs in sorted(C, key=lambda x: x[2][0]):
    br = cont(oid)
    print('  %s (%s)  on: %s' % (tok, oid[:12], ', '.join(br) if br else 'NO BRANCH (unreachable)'))
    for f,i in locs[:6]: print('      %s:%d' % (f,i))
    if len(locs)>6: print('      ... %d more' % (len(locs)-6))
print('== O: blobs/trees not reachable from main: %d' % len(O))
for tok,oid,typ,locs in sorted(O, key=lambda x: x[3][0]):
    print('  %s %s (%s)' % (typ,tok,oid[:12]))
    for f,i in locs[:4]: print('      %s:%d' % (f,i))
    if len(locs)>4: print('      ... %d more' % (len(locs)-4))
# D: cited sha256 digests with no tracked file at MAIN carrying that digest
digests = set()
for f in files:
    if not f.startswith('verification/'):
        continue
    try: txt = subprocess.run(['git','show',f'{MAIN}:{f}'],capture_output=True,check=True).stdout.decode('utf-8')
    except Exception: continue
    digests.update(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])', txt))
tracked = {}
for f in run('git','ls-tree','-r','--name-only',MAIN).split('\n'):
    if not f: continue
    data = subprocess.run(['git','show',f'{MAIN}:{f}'],capture_output=True).stdout
    tracked.setdefault(__import__('hashlib').sha256(data).hexdigest(), f)
hit = sorted(d for d in digests if d in tracked)
print('== D: 64-hex digests cited under verification/: %d; equal to a tracked file at MAIN: %d; equal to none: %d'
      % (len(digests), len(hit), len(digests) - len(hit)))
for d in hit:
    print('  tracked  %s  %s' % (d[:16], tracked[d]))
