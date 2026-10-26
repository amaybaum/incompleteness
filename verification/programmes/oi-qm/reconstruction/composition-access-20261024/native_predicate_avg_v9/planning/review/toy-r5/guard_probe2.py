"""Reviewer probe (r5): further attempts to reach v8's configuration. Construct only; no closure."""
import sys
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0ref as REF
src = ((-7, 0, -1), (-7, 0, 1), (-8, 0, 0))
res = []
def tryit(name, f):
    try:
        f(); res.append((name, 'NOT refused'))
    except PermissionError:
        res.append((name, 'refused'))
    except Exception as e:
        res.append((name, 'error ' + type(e).__name__))
tryit('float port (0.0,0.0,-3.0)', lambda: G.Context(G.Setup(3, 6, 4, 23, (0.0, 0.0, -3.0), src), (), 'A'))
tryit('n = 6.0', lambda: G.Context(G.Setup(3, 6.0, 4, 23, (0, 0, -3), src), (), 'A'))
tryit('port as generator', lambda: G.Context(G.Setup(3, 6, 4, 23, (x for x in (0, 0, -3)), src), (), 'A'))
tryit('rho=10, tlast=40, sources empty', lambda: G.record_at(G.Setup(3, 6, 10, 40, (0, 0, -3), ()), 5))
tryit('record_samples on rho=5 copy', lambda: G.record_samples(G.Setup(3, 6, 5, 23, (0, 0, -3), src), ()))
tryit('ref_context float port', lambda: REF.ref_context(3, 6, (0.0, 0.0, -3.0), (), 'G'))
tryit('ref_retained v8 (A) [guarded via ref_context; refused before any closure]', lambda: REF.ref_retained(3, 6, (0, 0, -3), (), 'A'))
class Sub(G.Setup):
    def key(self):
        return ('x',)
tryit('Setup subclass overriding key() [deliberate tampering]', lambda: G.Context(Sub(3, 6, 4, 23, (0, 0, -3), src), (), 'A'))
tryit('port None, v8 n and region [different configuration: no port]', lambda: G.Context(G.Setup(3, 6, 4, 23, None, src), (), 'A'))
tryit('port moved to (0,0,-2) [different configuration]', lambda: G.Context(G.Setup(3, 6, 4, 23, (0, 0, -2), src), (), 'A'))
for k, v in res:
    print('%-75s %s' % (k, v))
