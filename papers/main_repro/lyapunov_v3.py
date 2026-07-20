#!/usr/bin/env python3
"""B1 — two-trajectory Lyapunov measurement on the realized rounded bijection.
Construction per journal §B.2.575 b1_v3 (large alphabet q=2^16 so delta=1 is
infinitesimal-like; cone-restricted per-site circular RMS; 3 seeds), with an
AUTO-SELECTED exponential window replacing the hand-tuned one (the hand window
assumed slow growth and finds zero points when divergence is fast).
CLAIM VERIFIED (Main, Bell section): lambda_max > 0 — chaotic mixing of the
discretization nonlinearity. The QUANTITATIVE rate is ensemble/spec-dependent
(RESULTS.md §B1: the specific SM-241 value 0.0092 was not replicated; Main's
text states the rate as ensemble-dependent accordingly). PASS = lambda_max > 0
with growth to saturation on every seed.
"""
import numpy as np
L,q,T = 20, 1<<16, 400
def nn(x): return sum(np.roll(x,s,a) for a in range(3) for s in (1,-1))
def step(cur,prv): return (((nn(cur)+1)//3)-prv)%q
def circ(a,b):
    d=(a-b)%q; return np.minimum(d,q-d).astype(float)
idx=np.indices((L,L,L)); dist=np.max(np.minimum(np.abs(idx-L//2),L-np.abs(idx-L//2)),axis=0)
sat=q/np.sqrt(12)
lams=[]; ok=True
for seed in (1,2,3):
    r=np.random.default_rng(seed)
    c=r.integers(0,q,(L,L,L)); p=r.integers(0,q,(L,L,L))
    c2=c.copy(); c2[L//2,L//2,L//2]=(c2[L//2,L//2,L//2]+1)%q; p2=p.copy()
    rms=[]
    for t in range(1,T+1):
        c,p=step(c,p),c; c2,p2=step(c2,p2),c2
        cone=dist<=min(t,L//2)
        rms.append(np.sqrt(np.mean(circ(c,c2)[cone]**2)))
    rms=np.array(rms); t=np.arange(1,T+1)
    w=(rms>max(3*rms[0],1.0))&(rms<sat/4)            # auto window: clear of seed noise & saturation
    if w.sum()>=5:
        lam=np.linalg.lstsq(np.vstack([np.ones(w.sum()),t[w]]).T,np.log(rms[w]),rcond=None)[0][1]
    else:                                            # very fast divergence: per-step slope
        g=np.log(np.maximum(rms,1e-12)); pre=t[rms<sat/4]
        lam=(g[len(pre)-1]-g[0])/max(len(pre)-1,1)
    reached=rms.max()>sat/2
    lams.append(lam); ok &= (lam>0) and reached
    print(f"seed {seed}: lambda={lam:.4f}/step (window {w.sum()} pts); saturation reached: {reached}")
print(f"\nlambda_max = {np.mean(lams):.4f} +/- {np.std(lams):.4f} per step "
      f"-> {'PASS: lambda_max > 0 (chaotic); rate ensemble-dependent per RESULTS.md' if ok else 'FAIL'}")
