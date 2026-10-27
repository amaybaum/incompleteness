# Independent θ0/Q extraction via discrete Fourier transform of sqrt-masses (Fraction-free, mpmath 60 digits).
from mpmath import mp, mpf, sqrt, cos, sin, pi, atan2, findroot, exp, mpc
mp.dps=60
me=mpf('0.51099895000'); mmu=mpf('105.6583755')
def extract(mt):
    s=[sqrt(mt),sqrt(me),sqrt(mmu)]      # k=0 tau, 1 e, 2 mu
    mu=sum(s)/3
    F=sum(s[k]*exp(mpc(0,-2*pi*k/3)) for k in range(3))   # = (3/2) mu A e^{i th}
    th=atan2(F.imag,F.real); A=2*abs(F)/(3*mu)
    Q=(mt+me+mmu)/sum(s)**2
    # control: rebuild masses
    rb=[ (mu*(1+A*cos(th+2*pi*k/3)))**2 for k in range(3)]
    err=max(abs(rb[0]-mt),abs(rb[1]-me),abs(rb[2]-mmu))
    return th,A,Q,err
two9=mpf(2)/9
for lab,mt,dmt in [('PDG2024',mpf('1776.93'),mpf('0.09')),('PDG2016-22',mpf('1776.86'),mpf('0.12'))]:
    th,A,Q,err=extract(mt); thp,_,Qp,_=extract(mt+dmt); thm,_,Qm,_=extract(mt-dmt)
    sth=abs(thp-thm)/2; sQ=abs(Qp-Qm)/2
    print(f"{lab}: theta0={mp.nstr(th,9)} ± {mp.nstr(sth,2)}  rel={mp.nstr(100*(th-two9)/two9,4)}%  pull={mp.nstr((th-two9)/sth,3)}  | Q={mp.nstr(Q,9)} ± {mp.nstr(sQ,2)} rel={mp.nstr(100*(Q-mpf(2)/3)/(mpf(2)/3),3)}% pull={mp.nstr((Q-mpf(2)/3)/sQ,3)} | A^2={mp.nstr(A**2,8)} 1/3+A^2/6-Q={mp.nstr(mpf(1)/3+A**2/6-Q,3)} rebuild_err={mp.nstr(err,3)}")
# control: exact Koide point
mu0=mpf(1); s=[mu0*(1+sqrt(2)*cos(two9+2*pi*k/3)) for k in range(3)]
F=sum(s[k]*exp(mpc(0,-2*pi*k/3)) for k in range(3)); print("control exact point theta0-2/9 =",mp.nstr(atan2(F.imag,F.real)-two9,3))
# countercontrol: perturb m_mu by 1e-4 relative -> theta shifts visibly
# predicted masses from m_tau with Q=2/3, theta0=2/9
for mt in (mpf('1776.93'),mpf('1776.86')):
    mu=sqrt(mt)/(1+sqrt(2)*cos(two9)); pe=(mu*(1+sqrt(2)*cos(two9+2*pi/3)))**2; pm=(mu*(1+sqrt(2)*cos(two9+4*pi/3)))**2
    print(f"m_tau={mt}: m_e={mp.nstr(pe,7)} ({mp.nstr(100*(pe-me)/me,3)}%), m_mu={mp.nstr(pm,8)} ({mp.nstr(100*(pm-mmu)/mmu,3)}%)")
# closure: m_mu from m_e, m_tau at Q=2/3
for mt in (mpf('1776.93'),mpf('1776.86')):
    f=lambda x: (mt+me+x)/(sqrt(mt)+sqrt(me)+sqrt(x))**2-mpf(2)/3
    r=findroot(f,mpf(105))
    print(f"closure m_tau={mt}: m_mu={mp.nstr(r,8)} ({mp.nstr(100*(r-mmu)/mmu,3)}%)")
# sensitivity d theta/theta per relative mass shift (for O4): shift each mass by +delta
for k,name in enumerate(['tau','e','mu']):
    d=mpf('1e-6')
    ms=[mpf('1776.93'),me,mmu]; ms2=list(ms); ms2[k]*=1+d
    def ex(ms):
        s=[sqrt(x) for x in ms]; F=sum(s[j]*exp(mpc(0,-2*pi*j/3)) for j in range(3)); return atan2(F.imag,F.real)
    print(f"d ln(theta)/d ln(m_{name}) = {mp.nstr((ex(ms2)-ex(ms))/ex(ms)/d,4)}")
