"""Test the probe's section-6 logic on the measurement's pickled objects (stepG's machinery)."""
import pickle, random, time
from lib36 import *
src = open('stepG.py').read()
exec(src[src.index("A = pickle.load"):src.index("for si, V in enumerate(spaces):")])
Tco = Tcoords; zf = zero
def check(name, got, want):
    ok = got == want
    print('  %s  %s %s' % ('PASS' if ok else 'FAIL', name[:70], got if ok else '%s (expected %s)' % (got, want)))
body = open('probe36_body.py', encoding='utf-8').read()
seg = body[body.index('zf = [Fr(0)] * 64\ndef certificate'):body.index("print('  (%.0fs)' % (time.time() - t0))\n\nprint()")]
t0 = time.time(); exec(seg); print('%.0fs' % (time.time() - t0))
