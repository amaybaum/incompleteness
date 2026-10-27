import sys
sys.path.insert(0, sys.argv[1])
from regime_exact import rooted, revival
sw = {}
for x in (0, 1):
    for h in range(6): sw[(x, h)] = (x, h)
for h in (0, 1): sw[(0, h)], sw[(1, h)] = (1, h), (0, h)
for x in (0, 1):
    sw[(x, 2)], sw[(x, 3)] = (x, 3), (x, 2); sw[(x, 4)], sw[(x, 5)] = (x, 5), (x, 4)
G = rooted(sw, 2, 6, 20)
for K in (2, 4, 10, 20):
    R, B = revival(G, K); print(f"K={K}: peak R={R}, cumulative BLP-type B={B}")
