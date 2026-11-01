"""Flatten two JSON files and list differing leaves. Usage: cmpjson.py a b"""
import json, sys
def flat(o, p=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from flat(v, f'{p}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from flat(v, f'{p}[{i}]')
    else:
        yield p, o
a = dict(flat(json.load(open(sys.argv[1]))))
b = dict(flat(json.load(open(sys.argv[2]))))
for k in sorted(a.keys() | b.keys()):
    if a.get(k, '<absent>') != b.get(k, '<absent>'):
        print(k, ':', a.get(k, '<absent>'), '->', b.get(k, '<absent>'))
print('common equal leaves:', sum(1 for k in a.keys() & b.keys() if a[k] == b[k]))
