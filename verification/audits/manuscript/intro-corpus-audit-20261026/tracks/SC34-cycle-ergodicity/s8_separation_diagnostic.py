#!/usr/bin/env python3
"""Two-trajectory separation of the rounded bijection, as in papers/main_repro/lyapunov_v3.py, resolved in time.

Dynamics and measurement transcribed from lyapunov_v3.py (L = 20, q = 2^16, T = 400, seeds 1-3, uniform random
(prv, cur), unit perturbation of the central site of cur, cone = Chebyshev distance <= min(t, L//2) from the
centre, circular per-site difference, cone RMS, auto window rms in (max(3*rms[0], 1), sat/4), sat = q/sqrt(12)).

For each seed, per step t:
  rms(t)     cone RMS circular separation (the reproducer's observable)
  maxsep(t)  largest per-site circular separation
  nbig(t)    number of sites with circular separation > q/100
  nsep(t)    number of sites with nonzero separation
  rad(t)     largest Chebyshev distance from the centre of a separated site
  radii      L1 and Chebyshev radius, about the first straddling site, of the region with sep > q/100
  strad(t)   number of sites whose two trajectories' values straddle the alphabet boundary at time t
             (integer representatives differ by more than q/2 while the circular difference is below q/2)
Reports: the onset step t* (first step with maxsep > q/100), the jump factor rms(t*)/rms(t*-1), whether t*-1 is
the first step with a boundary straddle, rad and nsep for 12 steps after t*, the step at which rad reaches L//2
and the step at which rms first exceeds sat/2, the reproducer's window and fitted rate, whether the window
contains t*, and the residual sums of squares of exponential (log rms vs t) and power-law (log rms vs log t) fits
on that window.

Controls:
  K0  the transcribed step and fit reproduce lyapunov_v3.py's printed rates 0.2481, 0.5029, 0.6440 (4 d.p.).
  K1  exactness: rerunning seed 1 with no perturbation gives rms = 0 at every step.
  K2  the straddle detector fires on a planted pair (q-1, 0) and not on (0, 1).
"""
import numpy as np

L, q, T = 20, 1 << 16, 400
def nn(x): return sum(np.roll(x, s, a) for a in range(3) for s in (1, -1))
def step(cur, prv): return (((nn(cur) + 1) // 3) - prv) % q
def circ(a, b):
    d = (a - b) % q; return np.minimum(d, q - d)
def straddle(a, b):
    return (np.abs(a.astype(np.int64) - b.astype(np.int64)) > q // 2) & (circ(a, b) < q // 2)

idx = np.indices((L, L, L))
dist = np.max(np.minimum(np.abs(idx - L // 2), L - np.abs(idx - L // 2)), axis=0)
sat = q / np.sqrt(12)

def run(seed, perturb=True):
    r = np.random.default_rng(seed)
    c = r.integers(0, q, (L, L, L)); p = r.integers(0, q, (L, L, L))
    c2 = c.copy(); p2 = p.copy()
    if perturb: c2[L // 2, L // 2, L // 2] = (c2[L // 2, L // 2, L // 2] + 1) % q
    rec = {k: [] for k in ("rms", "maxsep", "nsep", "nbig", "rad", "strad")}
    rec["bigmask"] = []; rec["stradpos"] = None
    strad0 = int(straddle(c, c2).sum())
    for t in range(1, T + 1):
        c, p = step(c, p), c; c2, p2 = step(c2, p2), c2
        cone = dist <= min(t, L // 2)
        d = circ(c, c2)
        rec["rms"].append(np.sqrt(np.mean(d[cone].astype(float) ** 2)))
        rec["maxsep"].append(int(d.max())); rec["nsep"].append(int((d > 0).sum())); rec["nbig"].append(int((d > q / 100).sum()))
        rec["rad"].append(int(dist[d > 0].max()) if (d > 0).any() else -1)
        st = straddle(c, c2); rec["strad"].append(int(st.sum()))
        if rec["stradpos"] is None and st.any(): rec["stradpos"] = [tuple(int(v) for v in x) for x in np.argwhere(st)]
        rec["bigmask"].append(d > q / 100); rec.setdefault("sepmask", []).append(d > 0)
    out = {k: np.array(v) for k, v in rec.items() if k not in ("bigmask", "stradpos", "sepmask")}
    out["bigmask"] = rec["bigmask"]; out["stradpos"] = rec["stradpos"]; out["sepmask"] = rec["sepmask"]
    return out, strad0

def pdist(pos, kind):
    """periodic distance of every site from pos: Chebyshev or L1"""
    g = [np.minimum(np.abs(idx[a] - pos[a]), L - np.abs(idx[a] - pos[a])) for a in range(3)]
    return np.maximum(np.maximum(g[0], g[1]), g[2]) if kind == "cheb" else g[0] + g[1] + g[2]

def fits(rms):
    t = np.arange(1, T + 1)
    w = (rms > max(3 * rms[0], 1.0)) & (rms < sat / 4)
    if w.sum() >= 5:
        X = np.vstack([np.ones(w.sum()), t[w]]).T
        lam = np.linalg.lstsq(X, np.log(rms[w]), rcond=None)[0][1]
    else:
        g = np.log(np.maximum(rms, 1e-12)); pre = t[rms < sat / 4]
        lam = (g[len(pre) - 1] - g[0]) / max(len(pre) - 1, 1)
    y = np.log(rms[w]); res = {}
    for name, xv in (("exp", t[w].astype(float)), ("pow", np.log(t[w].astype(float)))):
        X = np.vstack([np.ones(w.sum()), xv]).T
        coef = np.linalg.lstsq(X, y, rcond=None)[0]; res[name] = float(((X @ coef - y) ** 2).sum())
    return lam, t[w], res

ok = {}
expected = {1: 0.2481, 2: 0.5029, 3: 0.6440}
for seed in (1, 2, 3):
    rec, strad0 = run(seed)
    rms, maxsep, nsep, nbig, rad, strad = (rec[k] for k in ("rms", "maxsep", "nsep", "nbig", "rad", "strad"))
    tt = np.arange(1, T + 1)
    on = int(tt[maxsep > q / 100][0])
    first_strad = int(tt[strad > 0][0]) if (strad > 0).any() else None
    lam, wt, res = fits(rms)
    ok[f"K0 seed {seed} rate reproduces lyapunov_v3 ({expected[seed]:.4f})"] = round(float(lam), 4) == expected[seed]
    print(f"=== seed {seed}")
    print(f"  boundary straddles at t=0 (initial perturbation): {strad0}")
    print(f"  before onset: rms range {rms[:on-1].min():.3f}..{rms[:on-1].max():.3f}, maxsep range "
          f"{maxsep[:on-1].min()}..{maxsep[:on-1].max()}, nsep at t*-1 = {nsep[on-2]}, rad at t*-1 = {rad[on-2]}")
    print(f"  first step with a boundary straddle: t = {first_strad}")
    print(f"  onset t* = {on}: maxsep {maxsep[on-2]} -> {maxsep[on-1]} (q/3 = {q/3:.0f}); "
          f"rms {rms[on-2]:.3f} -> {rms[on-1]:.1f}, factor {rms[on-1]/rms[on-2]:.0f} "
          f"(= 10^{np.log10(rms[on-1]/rms[on-2]):.2f}); sites with sep > q/100 at t*: {nbig[on-1]}")
    print(f"  after onset, t = t*..t*+11: rad {rad[on-1:on+11].tolist()}")
    print(f"                              nsep {nsep[on-1:on+11].tolist()}")
    print(f"                              sites with sep > q/100 {nbig[on-1:on+11].tolist()}")
    sp = rec["stradpos"]; print(f"  straddling sites at t = {first_strad}: {len(sp)} at {sp}")
    dl1 = pdist(sp[0], "l1"); dch = pdist(sp[0], "cheb")
    rl1 = [int(dl1[m].max()) for m in rec["bigmask"][on-1:on+11]]
    rch = [int(dch[m].max()) for m in rec["bigmask"][on-1:on+11]]
    print(f"  radius of the sep > q/100 region about the straddling site, t = t*..t*+11: L1 {rl1}; Chebyshev {rch}")
    par = (idx[0] + idx[1] + idx[2]) % 2
    cls = set()
    for t_, m in enumerate(rec["sepmask"], start=1):
        if m.any(): cls |= set(((par[m] + t_) % 2).tolist())
    half = L**3 // 2
    t90 = int(tt[nbig >= 0.9 * half][0])
    print(f"  separated sites (all sizes and steps) lie in one parity class of x+y+z+t: {len(cls) == 1}; "
          f"that class holds {half} sites per step")
    print(f"  sep > q/100 at >= 90% of those {half} sites from t = {t90} (t* + {t90-on}); max count {nbig.max()}")
    radfull = int(tt[rad >= L // 2][0]); satt = int(tt[rms > sat / 2][0])
    print(f"  rad reaches L//2 = {L//2} at t = {radfull} (t* + {radfull-on}); rms first > sat/2 at t = {satt}")
    print(f"  reproducer window t = {wt.min()}..{wt.max()} ({wt.size} pts); contains t*: {wt.min() <= on <= wt.max()}; "
          f"contains t*-1 and t*: {(on-1 in wt) and (on in wt)}")
    print(f"  reproducer rate {lam:.4f}/step; window RSS: exponential {res['exp']:.3f}, power law {res['pow']:.3f}, "
          f"ratio exp/pow {res['exp']/res['pow']:.2f}")

rec0, _ = run(1, perturb=False)
ok["K1 unperturbed twin has zero separation at every step"] = bool((rec0["rms"] == 0).all())
a = np.array([q - 1, 0, 5]); b = np.array([0, 1, 5])
ok["K2 straddle detector: fires on (q-1,0), not on (0,1) or (5,5)"] = straddle(a, b).tolist() == [True, False, False]
print()
for k, v in ok.items(): print(f"[{'PASS' if v else 'FAIL'}] {k}")
print("ALL CONTROLS GREEN" if all(ok.values()) else "SOME CONTROL FAILED")
