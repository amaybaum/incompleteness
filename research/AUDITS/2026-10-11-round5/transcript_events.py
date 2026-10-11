#!/usr/bin/env python3
"""List a subagent transcript's tool calls (timestamp, tool, target) and, for each, the timestamp of its result.
Usage: python3 -I -B transcript_events.py <transcript.jsonl> <regex> [<from-iso> <to-iso>]"""
import json, re, sys
path, pat = sys.argv[1], re.compile(sys.argv[2])
lo = sys.argv[3] if len(sys.argv) > 3 else ''
hi = sys.argv[4] if len(sys.argv) > 4 else '9999'
calls, results = {}, {}
for ln in open(path, encoding='utf-8'):
    try:
        m = json.loads(ln)
    except Exception:
        continue
    ts = m.get('timestamp', '')
    msg = m.get('message') or {}
    content = msg.get('content')
    if not isinstance(content, list):
        continue
    for c in content:
        if c.get('type') == 'tool_use':
            inp = c.get('input', {})
            tgt = inp.get('file_path') or inp.get('command') or inp.get('pattern') or ''
            extra = ''
            if c.get('name') == 'Edit':
                extra = ' | old: ' + (inp.get('old_string', '')[:90]).replace('\n', ' ') + ' | new: ' + (inp.get('new_string', '')[:90]).replace('\n', ' ')
            calls[c['id']] = (ts, c.get('name'), str(tgt).replace('\n', ' ')[:220] + extra)
        elif c.get('type') == 'tool_result':
            results[c.get('tool_use_id')] = ts
for k, (ts, name, tgt) in sorted(calls.items(), key=lambda kv: kv[1][0]):
    if lo <= ts <= hi and pat.search(tgt):
        print(f'{ts}  ->{results.get(k, "?")}  {name:5s} {tgt}')
