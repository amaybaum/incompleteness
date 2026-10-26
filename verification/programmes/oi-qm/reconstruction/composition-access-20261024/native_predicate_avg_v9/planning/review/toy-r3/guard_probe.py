"""Reviewer probe: which entry points refuse v8's setup. Builds NO closure on v8's class:
every call that is not refused is stopped before closure (Context constructed only; no run())."""
import sys
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0ref as REF
res = {}
def tryit(name, f):
    try:
        f(); res[name] = 'NOT refused'
    except PermissionError:
        res[name] = 'refused'
tryit('Context(V8,A)', lambda: G.Context(G.V8, (), 'A'))
tryit('Context(V8,G)', lambda: G.Context(G.V8, (), 'G'))
tryit('num_records(V8)', lambda: G.num_records(G.V8))
tryit('record_at(V8,0)', lambda: G.record_at(G.V8, 0))
tryit('record_samples(V8,())', lambda: G.record_samples(G.V8, ()))
clone = G.Setup(3, 6, 4, 23, (0, 0, -3), G.V8.sources)   # identical parameters, flag not set
tryit('num_records(clone of V8)', lambda: G.num_records(clone))
tryit('record_at(clone of V8, 0)', lambda: G.record_at(clone, 0))
tryit('Context(clone of V8, (), A) [constructed, not run]', lambda: G.Context(clone, (), 'A'))
tryit('s0ref.ref_context(v8 params) [context only]', lambda: REF.ref_context(3, 6, (0, 0, -3), (), 'A'))
G.V8.v8 = False   # attribute is mutable
tryit('Context(V8 after V8.v8=False) [constructed, not run]', lambda: G.Context(G.V8, (), 'A'))
for k, v in res.items():
    print('%-55s %s' % (k, v))
