# Compare 1/(pi*sqrt2) to PDG 2025 CKM review (Ceccucci-Ligeti-Sakai, rev. Apr 2024) values, read first-hand.
from mpmath import mp, mpf, pi, sqrt
mp.dps=30
lam = 1/(pi*sqrt(2)); print("1/(pi sqrt2) =", mp.nstr(lam,12))
rows = [("global fit lambda, CKMfitter method (12.26)", "0.22501","0.00068"),
        ("global fit lambda, UTfit prescription", "0.22497","0.00070"),
        ("|Vus| K_l3 (f+(0) Nf=2+1+1)", "0.2233","0.0005"),
        ("|Vus| K_mu2/pi_mu2 (fK/fpi)", "0.2250","0.0004"),
        ("|Vus| PDG average (12.8), err scaled", "0.22431","0.00085"),
        ("|Vus| hyperon", "0.2250","0.0027"),
        ("|Vus| tau (incl+excl)", "0.2207","0.0014"),
        ("SM.md cited (PDG-2022)", "0.22500","0.00067")]
for n,v,e in rows:
    v=mpf(v); e=mpf(e)
    print(f"{n:45s} {mp.nstr(v,6):>8s} ± {mp.nstr(e,2):<7s} pull {mp.nstr((lam-v)/e,3):>6s} sigma  rel {mp.nstr(100*(lam-v)/v,3):>6s} %")
