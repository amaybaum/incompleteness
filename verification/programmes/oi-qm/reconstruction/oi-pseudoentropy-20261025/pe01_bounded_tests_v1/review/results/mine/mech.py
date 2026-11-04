import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from collections import Counter
from indep import gen
n=5; phi, sig, f = gen('clk', n, True)
rho = ([1,0,2,3],[0,2,3,1]); a=[1,0,0,1]
# Does c_t depend only on past record? record controls; and Pr[c_t == Y_t] per t
agree = Counter(); vk_det = {}
pat = Counter()
for x0 in (0,1):
  for h0 in range(32):
    x,h,v = x0,h0,0; cs=[]; xs=[x0]
    for t in range(8):
      v = rho[x][v]; c = x ^ a[v]; cs.append(c)
      x2,h2 = phi(c,h); Y = x2 ^ c
      agree[t] += (Y == c)
      vk_det.setdefault((t+1, v), set()).add(xs[-1])
      x,h = x2,h2; xs.append(x)
    pat[tuple(cs[:7])] += 1
print('Pr[Y_t == c_t] - 1/2 for t=0..7:', [str(Fr(agree[t],64)-Fr(1,2)) for t in range(8)])
print('control patterns c_0..c_6 (count):', sorted(pat.items(), key=lambda z:-z[1])[:12])
print('does v_t determine x_{t-1}?', all(len(s)==1 for s in vk_det.values()))
