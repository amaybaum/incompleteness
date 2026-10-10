import sys, re
sys.path.insert(0, sys.argv[1])
import preserve as pv, controls as c
# widen the [:3] truncation
src = open(pv.__file__).read().replace('[:3]', '[:99]')
ns = {}; exec(compile(src, pv.__file__, 'exec'), ns)
pv.check = ns['check']
ok, lines = c.v313('.', '0811754da89dd5e3674ec913c0c89a24462a88fd', '378073fa')
print('\n'.join(lines))
