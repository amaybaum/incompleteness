import sys, time; sys.path.insert(0, 'a38')
from lib38b import *
t0 = time.time()
T = defect_rows(SIG)           # first-moment (tangent) equations, integer rows
rT = rank_int(T)
print('tangent equations', len(T), 'rank', rT, '=> dim T =', 256 - rT, ' defect(SIG) =', 256 - rT - 31)
for s in CENSUS9:
    for tr in (False, True):
        A = struct_eqs(s[0], s[1], s[2], False, tr)
        r = rank_int(T + A)
        rA = rank_int(A)
        Arel = struct_eqs(s[0], s[1], s[2], True, tr)
        rrel = rank_int(T + Arel)
        print('%s %-6s dim L_S = %3d  dim(L_S ∩ T) = %3d  relaxed dim(L_S^rel ∩ T) = %3d' % (NAMES9[s], 'row' if tr else 'column', 256 - rA, 256 - r, 256 - rrel))
# the span of all L_S ∩ T together: is it all of T?
allrows = None
print('%.0fs' % (time.time() - t0))
