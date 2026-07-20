#!/usr/bin/env python3
"""WP-B battery v2 — corrected diagnostics (v1 flaws documented in RESULTS)."""
import numpy as np
L,q = 20,64
def nn(x): return sum(np.roll(x,s,a) for a in range(3) for s in (1,-1))
def step_round(cur,prv): return (((nn(cur)+1)//3)-prv)%q
def step_lin(cur,prv): return nn(cur)/3.0-prv
def circ(a,b):
    d=(a-b)%q; return np.minimum(d,q-d).astype(float)

# ---------- B1 v2: longer run, inner-cone (matured) RMS, growth fit ----------
def lyap(seed,T=2600):
    r=np.random.default_rng(seed)
    c=r.integers(0,q,(L,L,L)); p=r.integers(0,q,(L,L,L))
    c2=c.copy(); c2[L//2,L//2,L//2]=(c2[L//2,L//2,L//2]+1)%q; p2=p.copy()
    out=[]
    for t in range(1,T+1):
        c,p = step_round(c,p),c
        c2,p2 = step_round(c2,p2),c2
        # after the cone fills the periodic box (t>~L), per-site RMS over ALL sites = matured measure
        out.append(np.sqrt(np.mean(circ(c,c2)**2)))
    return np.array(out)
print("B1 v2 Lyapunov (global per-site RMS after cone fills box; fit on clean exp window):")
lams=[]
for seed in (1,2,3,4):
    rms=lyap(seed); t=np.arange(1,len(rms)+1)
    w=(t>L)&(rms>1e-3)&(rms<q/8)
    if w.sum()>100:
        lam=np.linalg.lstsq(np.vstack([np.ones(w.sum()),t[w]]).T,np.log(rms[w]),rcond=None)[0][1]
        lams.append(lam)
        print(f"  seed {seed}: lambda={lam:.4f}/step over {w.sum()} steps (rms {rms[w][0]:.3f}->{rms[w][-1]:.2f})")
    else:
        print(f"  seed {seed}: window empty (rms range {rms.min():.4f}..{rms.max():.2f}) — growth slower than window floor")
if lams: print(f"  => lambda = {np.mean(lams):.4f} +/- {np.std(lams):.4f}  (SM 241 target 0.0092 +/- 0.0001)")

# ---------- B3 v2: single-mode initial data; linear = discrete peaks, rounded = ? ----------
def spec_entropy(series):
    w=np.hanning(len(series)); F=np.abs(np.fft.rfft((series-np.mean(series))*w))**2
    P=F[1:]/max(F[1:].sum(),1e-30); P=P[P>0]
    return float(-(P*np.log(P)).sum()/np.log(len(P)))
x=np.arange(L)
mode=(q//2+ (q//4)*np.cos(2*np.pi*x/L))[:,None,None]*np.ones((1,L,L))
ci=np.rint(mode).astype(np.int64)%q
c,p=ci.copy(),ci.copy(); cl,pl=ci.astype(float),ci.astype(float)
sr=[];sl=[]
for t in range(2048):
    c,p=step_round(c,p),c; cl,pl=step_lin(cl,pl),cl
    sr.append(c[3,4,5]); sl.append(cl[3,4,5])
Hr,Hl=spec_entropy(np.array(sr,float)),spec_entropy(np.array(sl))
print(f"\nB3 v2 spectral continuity (SINGLE-MODE start): rounded H={Hr:.3f} vs linear H={Hl:.3f}")
print(f"  => {'SEPARATED: rounded broadband (chaotic-class), linear discrete (integrable-class)' if Hr>Hl+0.15 else 'weak/no separation at this scale — honest result, record as-is'}")

# ---------- B4 v2: thermalization (autocorrelation decay) under matched single-mode start ----------
def autocorr_decay(series,lagmax=400):
    s=np.array(series,float); s=s-s.mean()
    ac=[np.dot(s[:-l],s[l:])/(np.dot(s,s)) if l>0 else 1.0 for l in range(lagmax)]
    return np.array(ac)
ar,al=autocorr_decay(sr),autocorr_decay(sl)
print(f"\nB4 v2 thermalization (|autocorr| at lag 200-400, single-mode start):")
print(f"  rounded {np.mean(np.abs(ar[200:])):.3f} vs linear {np.mean(np.abs(al[200:])):.3f}")
print(f"  => {'rounded THERMALIZES (memory decays), linear retains coherent oscillation' if np.mean(np.abs(ar[200:]))<np.mean(np.abs(al[200:]))-0.05 else 'no separation — record honestly'}")

# ---------- B2c v2: LINEAR-control cycle census for the 1D analog (same size) ----------
Lr,qr=5,4
def census(rounded):
    def step1d(st):
        cur=np.array(st[:Lr]); prv=np.array(st[Lr:])
        s=np.roll(cur,1)+np.roll(cur,-1)
        f=(s+1)//2 if rounded else s   # linear control: exact integer map x'=sum-prv (no division)
        return tuple(((f-prv)%qr).tolist()+cur.tolist())
    N=qr**(2*Lr); visited=np.zeros(N,bool)
    def enc(st):
        v=0
        for xx in st: v=v*qr+xx
        return v
    def dec(v):
        st=[]
        for _ in range(2*Lr): st.append(v%qr); v//=qr
        return tuple(reversed(st))
    cyc=[]
    for v0 in range(N):
        if visited[v0]: continue
        v=v0; n=0
        while not visited[v]:
            visited[v]=True; n+=1; v=enc(step1d(dec(v)))
        cyc.append(n)
    cyc=np.array(sorted(cyc,reverse=True))
    return len(cyc), cyc[0], cyc[0]/N
nr,topr,fr = census(True); nl,topl,fl = census(False)
print(f"\nB2c v2 1D-analog cycle census WITH linear control (L={Lr},q={qr},N={qr**(2*Lr)}):")
print(f"  rounded: {nr} cycles, largest {topr} = {100*fr:.1f}% of phase space")
print(f"  linear : {nl} cycles, largest {topl} = {100*fl:.1f}% of phase space")
print(f"  => {'rounding CONSOLIDATES cycles vs linear (mixing-favourable)' if fr>2*fl else ('rounding does NOT consolidate at this scale — fragmentation is real in the 1D analog; record honestly' if fr<=fl*1.5 else 'marginal')}")
