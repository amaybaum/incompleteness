#!/usr/bin/env python3
"""Scratch: render the V3-9 preregistration. Never landed. Usage: render39.py <out>"""
import hashlib, os, sys
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: open(os.path.join(H, n), encoding='utf-8').read()
out = rd('sim.out') if False else None
st = [l[6:] for l in open(os.path.join(H, 'selftest.out'), encoding='utf-8').read().split('\n') if l.startswith('      ')]
sub = {'{{BUILDER}}': rd('v3_receipt.py'), '{{A39}}': rd('a39.md'), '{{PRE_OLD}}': rd('pre_old.txt'),
       '{{PRE_NEW}}': rd('pre_new.txt'), '{{SELFTEST}}': '\n'.join(st) + '\n',
       '{{BLOB:builder}}': 'e08d15f6e301bec4d32f9dab34b5c7b40fb48d1f',
       '{{BLOB:agents}}': '864494c1a9696a3b08330da64cf9d265d6d8b92f',
       '{{BLOB:arch}}': 'f699471b34d4f332c557f6b5452c952db49a0306',
       '{{SHA:builder}}': hashlib.sha256(open(os.path.join(H, 'v3_receipt.py'), 'rb').read()).hexdigest()}
t = rd('prereg-template.md')
for k, v in sub.items():
    t = t.replace(k, v)
assert '{{' not in t
open(sys.argv[1], 'w', encoding='utf-8').write(t)
