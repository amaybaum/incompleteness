#!/usr/bin/env python3
"""B1 — two-trajectory separation to saturation on a rounded candidate map.
The map, unit perturbation at q=2^16, cone-restricted circular RMS and three
seeds follow the archived construction. A fitted log-linear slope is reported
as a window-dependent diagnostic; it does not establish a positive Lyapunov
exponent or chaotic mixing of the realized hidden sector. PASS means finite
separation grows from below half the reference saturation scale to above it
on every seed. The separate mixing-battery diagnostics are described in SM 4.2.
"""
import argparse
import numpy as np
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--no-perturbation-control', action='store_true',
                    help='bounded identical-twin countercontrol (L=4, q=256, T=80)')
args = parser.parse_args()
L,q,T = (4, 256, 80) if args.no_perturbation_control else (20, 1 << 16, 400)
perturbation = 0 if args.no_perturbation_control else 1
def nn(x): return sum(np.roll(x,s,a) for a in range(3) for s in (1,-1))
def step(cur,prv): return (((nn(cur)+1)//3)-prv)%q
def circ(a,b):
    d=(a-b)%q; return np.minimum(d,q-d).astype(float)
idx=np.indices((L,L,L)); dist=np.max(np.minimum(np.abs(idx-L//2),L-np.abs(idx-L//2)),axis=0)
sat=q/np.sqrt(12)
def reaches_saturation(rms, saturation):
    """Finite separation-to-saturation criterion; independent of fitted slope."""
    return bool(np.isfinite(rms).all() and rms[0] < saturation/2
                and rms.max() > saturation/2)

slopes=[]; ok=True; control_ok=True
for seed in (1,2,3):
    r=np.random.default_rng(seed)
    c=r.integers(0,q,(L,L,L)); p=r.integers(0,q,(L,L,L))
    c2=c.copy(); c2[L//2,L//2,L//2]=(c2[L//2,L//2,L//2]+perturbation)%q; p2=p.copy()
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
    passes = reaches_saturation(rms, sat)
    slopes.append(lam); ok &= passes
    control_ok &= bool(np.all(rms == 0)) and not passes
    print(f"seed {seed}: fitted log-separation slope={lam:.4f}/step "
          f"(window {w.sum()} pts; diagnostic only); saturation reached: {reached}")
print(f"\nmean fitted log-separation slope = {np.mean(slopes):.4f} "
      f"+/- {np.std(slopes):.4f} per step (diagnostic only)")
if args.no_perturbation_control:
    print('PASS: no-perturbation control has zero separation and fails saturation on every seed'
          if control_ok else 'FAIL: no-perturbation control')
    raise SystemExit(0 if control_ok else 1)
print('PASS: separation to saturation on every seed' if ok
      else 'FAIL: separation to saturation not reached on every seed')
raise SystemExit(0 if ok else 1)
