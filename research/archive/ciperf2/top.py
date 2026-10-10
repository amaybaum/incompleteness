import pstats, sys, os
p = pstats.Stats(sys.argv[1]); key = sys.argv[2]; n = int(sys.argv[3])
rows = []
for (f, l, fn), (cc, nc, tt, ct, callers) in p.stats.items():
    rows.append((tt if key == 'tottime' else ct, nc, tt, ct, '%s:%d(%s)' % (os.path.basename(f), l, fn)))
rows.sort(reverse=True)
print('total %.1f s' % p.total_tt)
print('%12s %9s %9s  %s' % ('ncalls', 'tottime', 'cumtime', 'function'))
for r in rows[:n]: print('%12d %9.1f %9.1f  %s' % (r[1], r[2], r[3], r[4]))
