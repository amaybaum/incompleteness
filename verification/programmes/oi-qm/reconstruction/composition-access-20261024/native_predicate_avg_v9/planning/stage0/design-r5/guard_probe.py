"""Reviewer probe (r4): attempts to reach v8's configuration without authorization.
Contexts/records are CONSTRUCTED only; no closure is run on anything v8-derived."""
import sys
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0ref as REF
res = []
def tryit(name, f):
    try:
        f(); res.append((name, 'NOT refused'))
    except PermissionError:
        res.append((name, 'refused'))
    except Exception as e:
        res.append((name, 'error ' + type(e).__name__))
src = ((-7, 0, -1), (-7, 0, 1), (-8, 0, 0))
fresh = G.Setup(3, 6, 4, 23, (0, 0, -3), src)
tryit('V8 Context A', lambda: G.Context(G.V8, (), 'A'))
tryit('fresh copy Context A', lambda: G.Context(fresh, (), 'A'))
tryit('fresh copy, sources reordered', lambda: G.Context(G.Setup(3, 6, 4, 23, (0, 0, -3), src[::-1]), (), 'A'))
G.V8.v8 = False
tryit('V8 with flag flipped', lambda: G.Context(G.V8, (), 'A'))
G.V8.v8 = True
tryit('ref_context v8 (A)', lambda: REF.ref_context(3, 6, (0, 0, -3), (), 'A'))
tryit('ref_context v8 (G)', lambda: REF.ref_context(3, 6, (0, 0, -3), (), 'G'))
# new bypass attempts
tryit('port as list [0,0,-3]', lambda: G.Context(G.Setup(3, 6, 4, 23, [0, 0, -3], src), (), 'A'))
tryit('ref_context port as list', lambda: REF.ref_context(3, 6, [0, 0, -3], (), 'A'))
tryit('sources empty (closure identical under A)', lambda: G.Context(G.Setup(3, 6, 4, 23, (0, 0, -3), ()), (), 'A'))
tryit('sources one changed', lambda: G.Context(G.Setup(3, 6, 4, 23, (0, 0, -3), ((-7, 0, -1), (-7, 0, 1), (-9, 0, 0))), (), 'A'))
tryit('rho = 5 (superset of v8 region)', lambda: G.num_records(G.Setup(3, 6, 5, 23, (0, 0, -3), src)))
tryit('tlast = 24 (superset of v8 slices)', lambda: G.num_records(G.Setup(3, 6, 4, 24, (0, 0, -3), src)))
tryit('rho=5 record_at -> a v8 record [index only]', lambda: G.record_at(G.Setup(3, 6, 5, 23, (0, 0, -3), src), 0))
tryit('V8_PARAMS rebound', lambda: (setattr(G, 'V8_PARAMS', None), G.Context(fresh, (), 'A')))
G.V8_PARAMS = (3, 6, 4, 23, (0, 0, -3), tuple(sorted(src)))
tryit('ref V8_REF rebound', lambda: (setattr(REF, 'V8_REF', None), REF.ref_context(3, 6, (0, 0, -3), (), 'A')))
for k, v in res:
    print('%-50s %s' % (k, v))
