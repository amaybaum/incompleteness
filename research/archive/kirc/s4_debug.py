import sympy as sp, itertools
d, p = 3, 1
exec(open('s12_exact.py').read().split('# ---- S4')[1].split("print('\\nSUMMARY")[0].replace("for (d, p) in ((5, 2), (7, 3)):", "for (d, p) in ((3, 1),):").replace("    rep('S4", "    print(sp.expand(val - form)); rep('S4"), {'sp': sp, 'itertools': itertools, 'rep': lambda *a: print(a[1])})
