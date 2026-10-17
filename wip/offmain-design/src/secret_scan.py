"""Secrets and operational-data scan (AGENTS §A.42 item 5) of every object the plan would store.

Patterns: R1's check_retention.py SECRET regex (tokens, keys, key headers, signed-URL parameters, passwords, API keys,
IPv4 addresses, e-mail addresses) plus a few more token shapes. Commit objects are scanned in full; the author and
committer header lines are reported separately, since their identities are already public in main's history.
Writes work/secret-scan.json.
"""
import collections, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import Store, parse_tree
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'work')
src = Store(os.path.join(W, 'src.git'))
SECRET = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
                    r'|x-access-toke[n]|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key'
                    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)
EXTRA = re.compile(r'xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{35}|X-Amz-Signature'
                   r'|-----BEGIN [A-Z ]*PRIVATE KEY|ssh-(rsa|ed25519) AAAA')
P = json.load(open(os.path.join(W, 'plan.json')))['objects']
hits = []
ident = collections.Counter()
for oid, r in P.items():
    stored = r['mechanism'] in ('byte-copy', 'raw', 'raw:proof-path') or r['type'] == 'commit'
    if not stored:
        continue
    t, data = src.read(oid)
    if t == 'tree':
        text = '\n'.join(n for _, n, _ in parse_tree(data))
    else:
        text = data.decode('utf-8', 'replace')
    lines = text.split('\n')
    head = True
    for i, l in enumerate(lines, 1):
        if t == 'commit' and head:
            if l == '':
                head = False
            elif l.startswith(('author ', 'committer ', 'tagger ')):
                m = re.search(r'<([^>]*)>', l)
                ident[m.group(1) if m else '?'] += 1
                continue
        m = SECRET.search(l) or EXTRA.search(l)
        if m:
            hits.append({'oid': oid, 'type': t, 'path': (r['paths'] or ['?'])[0], 'line': i, 'match': m.group(0)[:60],
                         'context': l.strip()[:160]})
json.dump({'hits': hits, 'identities': len(ident), 'identity_lines': sum(ident.values())},
          open(os.path.join(W, 'secret-scan.json'), 'w'), indent=1)
print('hits', len(hits), 'identity header lines', sum(ident.values()), 'distinct identities', len(ident))
c = collections.Counter(h['match'] if not re.search(r'@', h['match']) else '<e-mail>' for h in hits)
print(c.most_common(30))
for h in hits[:80]:
    print(h['oid'][:10], h['type'], h['path'], h['line'], '|', h['context'][:150])
