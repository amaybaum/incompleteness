"""Reviewer's own git helpers (read-only). Not derived from work-v4."""
import subprocess, functools, json, os
REPO = '<repo>'
E = 'e837e3dbaa605efc867a213f3345cee14c36d8f5'
H = '53c6601a10419b6b333cc992474272501ab542af'
P = '4c79be642ca631573f06b444903be75ec4f5e2b6'
T = '14ac71b4b0a0c0aa2d7068d6799a73f474097060'
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def git(*a, text=True):
    return subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, check=True, text=text).stdout

@functools.lru_cache(maxsize=None)
def ls(commit):
    return [l for l in git('ls-tree', '-r', '--name-only', commit).split('\n') if l]

@functools.lru_cache(maxsize=None)
def blob(commit, path):
    r = subprocess.run(['git', '-C', REPO, 'show', '%s:%s' % (commit, path)], capture_output=True)
    if r.returncode:
        return None
    return r.stdout

def text(commit, path):
    b = blob(commit, path)
    return None if b is None else b.decode('utf-8')

def lines(commit, path):
    t = text(commit, path)
    return None if t is None else t.split('\n')

def corpus(commit):
    out = []
    for p in ls(commit):
        d, _, n = p.partition('/')
        if d in ('papers', 'book') and '/' not in n and n.endswith('.md'):
            out.append(p)
    return sorted(out)

def load(name):
    return json.load(open(os.path.join(DATA, name)))
