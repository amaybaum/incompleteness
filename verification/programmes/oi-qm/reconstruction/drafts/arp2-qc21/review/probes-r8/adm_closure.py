# Reviewer probe r8 (exact; control, not evidence). Closure of Adm_B under SA-1(c)'s wording
# ("exactly one known linear functional"): single fresh arm cells whose known functional is u, v, OR u+v.
# The u+v-known cells (w, w+c) are not in r8's hand-listed Adm_B. Same model as r6/r7/r8 (independent code).
import itertools
from fractions import Fraction as F
def run(src, phi, cellfn):
    # cellfn(w, w2) -> (u_a, v_a) supply at t=2; w, w2 uniform unknowns (w2 may be unused)
    out = {}
    cz, cx = {'X+': (None, 0), 'Z+': (0, None), 'Z-': (1, None)}[src]
    for z, x, vp, ws, w, w2 in itertools.product((0, 1), repeat=6):
        if cz is not None and z != cz: continue
        if cx is not None and x != cx: continue
        # encoded carrier (z, x); phase cell (phi, vp) at t0: x += phi; p := (z+vp, phi)
        x = (x + phi) % 2
        ua, va = cellfn(w, w2)
        # t2 (even): u_c' = u_a + v_c(=x) -> kick u_a on x; a' = (z + v_a, u_a)
        x2 = (x + ua) % 2; held = ((z + va) % 2, ua)
        port = x2                                    # t3 X read (screen (w_s,0)): port = x
        key = (port, held)
        out[key] = out.get(key, 0) + 1
    tot = sum(out.values()); return {k: F(v, tot) for k, v in out.items()}
def P0(src, phi, fn): return sum(p for (pt, h), p in run(src, phi, fn).items() if pt == 0)
def V(fn): return abs(P0('X+', 0, fn) - P0('X+', 1, fn))
def D(fn):
    a = {}; b = {}
    for (pt, h), p in run('Z+', 0, fn).items(): a[h] = a.get(h, 0) + p
    for (pt, h), p in run('Z-', 0, fn).items(): b[h] = b.get(h, 0) + p
    return sum(abs(a.get(k, 0) - b.get(k, 0)) for k in set(a) | set(b)) / 2
cells = {
 "(w,0) u-unknown, v=0 [in Adm_B]": lambda w, w2: (w, 0),
 "(0,w') [in Adm_B]":               lambda w, w2: (0, w2),
 "(w,w') hidden [in Adm_B]":        lambda w, w2: (w, w2),
 "(w,w) : u+v = 0 known [NOT listed]":   lambda w, w2: (w, w),
 "(w,w+1): u+v = 1 known [NOT listed]":  lambda w, w2: (w, (w + 1) % 2),
}
for n, fn in cells.items(): print(f"{n:40s} V={V(fn)} D={D(fn)}")
