#!/usr/bin/env python3
"""Rebuild a dev-branch file from a subagent transcript's own write events and compare it with recorded digests.
Usage: python3 -I -B dev_replay.py <transcript.jsonl> <dev-root> <relpath> <scratch-root> <checkpoint-iso>=<sha256> ...
Replays, in timestamp order, the transcript's Write and Edit calls on <dev-root>/<relpath> and its Bash calls that name
the file and contain an append (cat >>) or a python heredoc, with <dev-root> rewritten to <scratch-root>.  A call whose
result the transcript marks as an error is not applied.  Bash calls that run a writing git subcommand (add, commit, push,
checkout, reset, stash, merge, rebase) or name any absolute path outside <dev-root> are skipped and listed, so the replay
writes nowhere but <scratch-root>; the checkpoint digests show whether a skipped call touched the file.  At each
checkpoint time the rebuilt file's sha256 is compared with the given digest.  Prints MATCH or DIFF per checkpoint.
"""
import hashlib, json, os, re, subprocess, sys
tr, dev, rel, scr = sys.argv[1:5]
cps = [a.split('=', 1) for a in sys.argv[5:]]
target = os.path.join(dev, rel)
events, errs = [], set()
for ln in open(tr, encoding='utf-8'):
    try:
        m = json.loads(ln)
    except Exception:
        continue
    content = (m.get('message') or {}).get('content')
    if not isinstance(content, list):
        continue
    for c in content:
        if c.get('type') == 'tool_use':
            events.append((m.get('timestamp', ''), c.get('name'), c.get('input', {}), c.get('id')))
        elif c.get('type') == 'tool_result' and c.get('is_error'):
            errs.add(c.get('tool_use_id'))
events.sort(key=lambda e: e[0])
os.makedirs(os.path.dirname(os.path.join(scr, rel)), exist_ok=True)
out = os.path.join(scr, rel)
base = os.path.basename(rel)
ci = 0
def digest():
    return hashlib.sha256(open(out, 'rb').read()).hexdigest() if os.path.exists(out) else 'ABSENT'
def checkpoint_upto(ts):
    global ci
    while ci < len(cps) and cps[ci][0] <= ts:
        d = digest()
        print(f'{"MATCH" if d == cps[ci][1] else "DIFF "} at {cps[ci][0]}: rebuilt {d[:12]} recorded {cps[ci][1][:12]}')
        ci += 1
for ts, name, inp, cid in events:
    checkpoint_upto(ts)
    if cid in errs:
        if inp.get('file_path') == target or base in inp.get('command', ''):
            print(f'{ts} {name:6s} result marked as an error in the transcript; not applied')
        continue
    if name == 'Write' and inp.get('file_path') == target:
        open(out, 'w', encoding='utf-8').write(inp['content'])
        print(f'{ts} Write  -> {digest()[:12]}')
    elif name == 'Edit' and inp.get('file_path') == target:
        s = open(out, encoding='utf-8').read()
        old, new = inp['old_string'], inp['new_string']
        n = s.count(old)
        if inp.get('replace_all'):
            s = s.replace(old, new)
        elif n == 1:
            s = s.replace(old, new, 1)
        else:
            print(f'{ts} Edit   old_string occurs {n} times: Edit tool would have refused; not applied')
            continue
        open(out, 'w', encoding='utf-8').write(s)
        print(f'{ts} Edit   -> {digest()[:12]}')
    elif name == 'Bash':
        cmd = inp.get('command', '')
        if base not in cmd:
            continue
        outside = [a for a in re.findall(r'(/(?:home|tmp|root)/[^\s\'";|&)]*)', cmd) if not a.startswith(dev)]
        if re.search(r'\bgit\b(?:\s+-C\s+\S+)?\s+(?:add|commit|push|checkout|reset|stash|merge|rebase)\b', cmd) or outside:
            print(f'{ts} SKIP   {cmd[:110]!r}')
            continue
        if not ('cat >>' in cmd or 'python3' in cmd):
            continue
        cmd2 = cmd.replace(dev, scr)
        r = subprocess.run(['bash', '-c', cmd2], capture_output=True, text=True)
        print(f'{ts} Bash   exit {r.returncode} -> {digest()[:12]}  {cmd[:80]!r}')
checkpoint_upto('9999')
