"""Delete exactly the enumerated Tier 1 paths, one at a time, with a fresh process check before each. Writes ledger.jsonl."""
import json, os, shutil, subprocess, sys, datetime
S = sys.argv[1]; L = os.path.join(S, 'cleanup-20261017')
REL = ['agent-r2b/u1.git', 'agent-r2b/u2.git', 'agent-r2b/u3.git', 'agent-r2b/probe-k2g', 'agent-r2b/mech', 'agent-r2b/probe-og1',
       'agent-errata-fix/clone-branch2', 'agent-errata-fix/clone-branch3', 'agent-errata-fix/clone-main2',
       'agent-errata-fix/clone-sd', 'agent-errata-fix/clone-bd', 'agent-accept/restore.git', 'bundle/src.git',
       'bundle/verify.git', 'review-855b/noobj', 'review-855b/shared', 'review-855/clone']
REASON = {
 'agent-r2b/u1.git': 'R2-B survey scratch bare repo; all ref objects present in the main clone; no repo borrows its objects',
 'agent-r2b/u2.git': 'R2-B survey scratch bare repo; all ref objects present in the main clone; no repo borrows its objects',
 'agent-r2b/u3.git': 'R2-B survey scratch bare repo; all ref objects present in the main clone; no repo borrows its objects',
 'agent-r2b/probe-k2g': 'R2-B probe clone of main at 66a981d5; clean; nothing unique',
 'agent-r2b/mech': 'R2-B storage-mechanism test packs and bundles; results recorded in agent-r2b/memo.md',
 'agent-r2b/probe-og1': 'R2-B OG-1 probe clones. Only unique object: commit f7c1a1afc6fa77dad170df596af22fcd390dcf00 "scratch probe: blob bytes only (never pushed)", adding two files whose bytes are blobs bf627dfe3563fb9361e41fe7e633ea49168be95e and e9722042c2fc076ef292cbdb6d800a591ff71eb4, both present in the main clone and in the off-main layout; referenced nowhere else',
 'agent-errata-fix/clone-branch2': '#855 fixer test clone at b2f06c78 (pushed); clean',
 'agent-errata-fix/clone-branch3': '#855 fixer test clone at 8021c1fc (pushed); clean',
 'agent-errata-fix/clone-main2': '#855 fixer clone of main at 66a981d5; clean',
 'agent-errata-fix/clone-sd': '#855 fixer site-deletion clone at b2f06c78; edits: check_errata.py and errata.json identical to 8021c1fc, README an earlier draft superseded by 8021c1fc (diff kept in this ledger)',
 'agent-errata-fix/clone-bd': '#855 fixer branch-deletion clone; clean; HEAD present in the main clone',
 'agent-accept/restore.git': 'inventory validator restore-test repo; all ref objects present in the main clone',
 'bundle/src.git': 'scratch repo used to build the R1 drafting bundle; bundle file kept',
 'bundle/verify.git': 'scratch repo used to verify the R1 drafting bundle; bundle file kept',
 'review-855b/noobj': '#855 reviewer test clone; its edited files are identical to 8021c1fc',
 'review-855b/shared': '#855 reviewer test clone; its edited files are identical to 8021c1fc',
 'review-855/clone': '#855 first-review clone at 0326e56b (pushed); clean',
}
def inside(p, t):
    p, t = os.path.realpath(p), os.path.realpath(t)
    return p == t or p.startswith(t + os.sep)
def users(t):
    hits = []
    for pid in filter(str.isdigit, os.listdir('/proc')):
        paths = []
        for l in ('cwd', 'root', 'exe'):
            try: paths.append(os.readlink('/proc/%s/%s' % (pid, l)))
            except OSError: pass
        try:
            for fd in os.listdir('/proc/%s/fd' % pid):
                try: paths.append(os.readlink('/proc/%s/fd/%s' % (pid, fd)))
                except OSError: pass
        except OSError: pass
        if any(p.startswith('/') and inside(p, t) for p in paths):
            hits.append(pid)
    return hits
out = open(os.path.join(L, 'ledger.jsonl'), 'a')
for rel in REL:
    t = os.path.join(S, rel)
    assert os.path.isabs(t) and t.startswith(S + '/') and '*' not in t and rel.count('/') >= 1, t
    rec = {'path': t, 'reason': REASON[rel], 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
    if not os.path.isdir(t) or os.path.islink(t):
        rec['outcome'] = 'skipped: not a directory'
    else:
        rec['bytes'] = int(subprocess.run(['du', '-sb', t], capture_output=True, text=True).stdout.split('\t')[0])
        u = users(t)
        if u:
            rec['outcome'] = 'skipped: in use by pid(s) %s' % u
        else:
            shutil.rmtree(t)
            rec['outcome'] = 'deleted' if not os.path.exists(t) else 'FAILED: still present'
    out.write(json.dumps(rec) + '\n'); out.flush()
    print('%-34s %12s  %s' % (rel, rec.get('bytes', '-'), rec['outcome']))
