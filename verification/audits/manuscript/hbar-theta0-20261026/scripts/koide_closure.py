"""Koide closure: m_mu from observed m_e, m_tau with Q = 2/3 exactly (both roots), and
m_e/m_tau vs 1/(36 pi^4). Control: closure applied to the exact Koide point returns its m_mu."""
import mpmath as mp
mp.mp.dps = 40
me, mt = mp.mpf("0.51099895000"), mp.mpf("1776.93")
mm_obs = mp.mpf("105.6583755")
def roots(me, mt):
    # Q = (me+mm+mt)/(se+x+st)^2 = 2/3, x = sqrt(mm): 3(me+x^2+mt) = 2(se+st+x)^2
    se, st = mp.sqrt(me), mp.sqrt(mt); b = se + st
    # x^2 - 4 b x + 3(me+mt) - 2 b^2 = 0
    disc = 16*b**2 - 4*(3*(me+mt) - 2*b**2)
    return [((4*b + s*mp.sqrt(disc))/2)**2 for s in (1, -1)]
# control on an exact Koide triple
tw = mp.mpf(2)/9
tri = [(1+mp.sqrt(2)*mp.cos(tw+2*mp.pi*k/3))**2 for k in range(3)]  # tau, e, mu
ctrl = min(abs(r - tri[2]) for r in roots(tri[1], tri[0]))
print("control (exact Koide point recovers m_mu):", "PASS" if ctrl < mp.mpf("1e-30") else "FAIL")
for mt_ in (mp.mpf("1776.93"), mp.mpf("1776.86")):
    r = [x for x in roots(me, mt_) if x < mt_]
    for x in r:
        print(f"m_tau={mt_}: closure m_mu = {mp.nstr(x, 9)} MeV, dev {mp.nstr(100*(x-mm_obs)/mm_obs, 3)} %")
ratio = me/mt; pred = 1/(36*mp.pi**4)
print("m_e/m_tau =", mp.nstr(ratio, 6), " 1/(36 pi^4) =", mp.nstr(pred, 6), " dev", mp.nstr(100*(pred-ratio)/ratio, 3), "%")
