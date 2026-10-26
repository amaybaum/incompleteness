"""Koide angle theta_0 and Koide Q from charged-lepton pole masses, high precision.

Parametrization (SM §7.2, SM.md:895): sqrt(m_k) = mu * (1 + A cos(theta_0 + 2 k pi / 3)),
k = 0 (tau), 1 (e), 2 (mu).  The three masses fix (mu, A, theta_0) exactly:
  sum_k s_k                = 3 mu
  sum_k s_k cos(2 pi k/3)  = (3/2) mu A cos(theta_0)
  sum_k s_k sin(2 pi k/3)  = -(3/2) mu A sin(theta_0)
with s_k = sqrt(m_k).  Q = sum m / (sum sqrt m)^2 = 1/3 + A^2/6.

Uncertainties: linear propagation with numerical derivatives (mpmath, 50 digits),
independent mass errors.  The m_tau error dominates.

Controls:
  C1 round trip: masses rebuilt from the extracted (mu, A, theta_0) equal the inputs.
  C2 identity:   Q computed directly equals 1/3 + A^2/6.
  C3 known point: A = sqrt(2), theta_0 = 2/9 input gives Q = 2/3 exactly and theta_0 back.
  C4 convention: relabelling k (cyclic shift) changes theta_0 by 2 pi/3 only; reflection gives -theta_0.
Verdict text is generated from the numbers.
"""
import mpmath as mp

mp.mp.dps = 50
TWO_PI_3 = 2 * mp.pi / 3
TARGET = mp.mpf(2) / 9

# PDG 2024 (Navas et al., Phys. Rev. D 110, 030001), MeV
PDG2024 = {
    "e": (mp.mpf("0.51099895000"), mp.mpf("0.00000000015")),
    "mu": (mp.mpf("105.6583755"), mp.mpf("0.0000023")),
    "tau": (mp.mpf("1776.93"), mp.mpf("0.09")),
}
# Earlier PDG tau averages, for provenance of older figures
OLD_TAU = {
    "PDG 2016-2022 (1776.86 +- 0.12)": (mp.mpf("1776.86"), mp.mpf("0.12")),
    "PDG 2012-2014 (1776.82 +- 0.16)": (mp.mpf("1776.82"), mp.mpf("0.16")),
}


def extract(me, mmu, mtau, order=("tau", "e", "mu")):
    m = {"e": me, "mu": mmu, "tau": mtau}
    s = [mp.sqrt(m[name]) for name in order]
    S0 = sum(s)
    C = sum(s[k] * mp.cos(TWO_PI_3 * k) for k in range(3))
    Sn = sum(s[k] * mp.sin(TWO_PI_3 * k) for k in range(3))
    mu = S0 / 3
    A = 2 * mp.sqrt(C**2 + Sn**2) / (3 * mu)
    th = mp.atan2(-Sn, C)
    Q = (me + mmu + mtau) / S0**2
    return mu, A, th, Q


def rebuild(mu, A, th):
    return [(mu * (1 + A * mp.cos(th + TWO_PI_3 * k)))**2 for k in range(3)]  # tau, e, mu


def propagate(f, vals, errs):
    """Linear error propagation of scalar f(*vals)."""
    tot = mp.mpf(0)
    for i in range(len(vals)):
        h = errs[i] * mp.mpf("1e-6") if errs[i] != 0 else mp.mpf("1e-30")
        up = list(vals); dn = list(vals)
        up[i] += h; dn[i] -= h
        d = (f(*up) - f(*dn)) / (2 * h)
        tot += (d * errs[i])**2
    return mp.sqrt(tot)


def report(label, me, mmu, mtau, dme, dmmu, dmtau):
    mu, A, th, Q = extract(me, mmu, mtau)
    vals, errs = [me, mmu, mtau], [dme, dmmu, dmtau]
    dth = propagate(lambda a, b, c: extract(a, b, c)[2], vals, errs)
    dQ = propagate(lambda a, b, c: extract(a, b, c)[3], vals, errs)
    rel_th = (th - TARGET) / TARGET
    rel_Q = (Q - mp.mpf(2) / 3) / (mp.mpf(2) / 3)
    print(f"== {label}")
    print(f"   theta_0 = {mp.nstr(th, 10)} +- {mp.nstr(dth, 3)}   A^2 = {mp.nstr(A**2, 10)}   mu = {mp.nstr(mu, 10)} MeV^(1/2)")
    print(f"   (theta_0 - 2/9)/(2/9) = {mp.nstr(100*rel_th, 4)} %   pull = {mp.nstr((th-TARGET)/dth, 3)} sigma")
    print(f"   Q = {mp.nstr(Q, 12)} +- {mp.nstr(dQ, 3)}   (Q - 2/3)/(2/3) = {mp.nstr(100*rel_Q, 4)} %   pull = {mp.nstr((Q-mp.mpf(2)/3)/dQ, 3)} sigma")
    return mu, A, th, Q, dth


def predict_masses(mtau, theta=TARGET, A=mp.sqrt(2)):
    mu = mp.sqrt(mtau) / (1 + A * mp.cos(theta))
    _, me, mmu = rebuild(mu, A, theta)
    return me, mmu


def main():
    me, dme = PDG2024["e"]; mm, dmm = PDG2024["mu"]; mt, dmt = PDG2024["tau"]
    mu, A, th, Q, dth = report("PDG 2024 (SM.md:903 inputs)", me, mm, mt, dme, dmm, dmt)

    # Controls
    rb = rebuild(mu, A, th)
    c1 = max(abs(rb[0] - mt) / mt, abs(rb[1] - me) / me, abs(rb[2] - mm) / mm)
    c2 = abs(Q - (mp.mpf(1) / 3 + A**2 / 6))
    m3 = rebuild(mp.mpf(1), mp.sqrt(2), TARGET)
    mu3, A3, th3, Q3 = extract(m3[1], m3[2], m3[0])
    c3 = max(abs(Q3 - mp.mpf(2) / 3), abs(th3 - TARGET), abs(A3 - mp.sqrt(2)))
    th_shift = extract(me, mm, mt, order=("e", "mu", "tau"))[2]
    c4a = abs(mp.fmod(th - th_shift + 4 * mp.pi, TWO_PI_3))
    c4a = min(c4a, abs(c4a - TWO_PI_3))
    th_refl = extract(me, mm, mt, order=("tau", "mu", "e"))[2]
    c4b = abs(th + th_refl)
    controls = {"C1 round trip": c1 < mp.mpf("1e-40"), "C2 Q identity": c2 < mp.mpf("1e-40"),
                "C3 known point": c3 < mp.mpf("1e-40"), "C4a cyclic relabel": c4a < mp.mpf("1e-40"),
                "C4b reflection": c4b < mp.mpf("1e-40")}
    print("   controls:", {k: ("PASS" if v else "FAIL") for k, v in controls.items()})
    green = all(controls.values())

    for lab, (t, dt) in OLD_TAU.items():
        report(lab, me, mm, t, dme, dmm, dt)

    print("== Predicted masses, Q = 2/3 (A^2 = 2), theta_0 = 2/9, m_tau input")
    for lab, t in [("m_tau = 1776.93", mt), ("m_tau = 1776.86", mp.mpf("1776.86"))]:
        pe, pm = predict_masses(t)
        print(f"   {lab}: m_e = {mp.nstr(pe, 8)} MeV ({mp.nstr(100*(pe-me)/me, 3)} %),"
              f" m_mu = {mp.nstr(pm, 9)} MeV ({mp.nstr(100*(pm-mm)/mm, 3)} %)")

    print("== Other quantities that could be quoted as a 'theta_0 match'")
    for lab, obs in [("rounded observed 0.2227 (SM.md:928, :934)", mp.mpf("0.2227")),
                     ("observed 0.22227", mp.mpf("0.22227"))]:
        print(f"   {lab}: deviation of 2/9 = {mp.nstr(100*(obs-TARGET)/TARGET, 4)} %")
    # theta_0 with A fixed at sqrt(2), from each mass ratio
    for lab, ratio, k in [("from m_e/m_tau, A^2 = 2", me / mt, 1), ("from m_mu/m_tau, A^2 = 2", mm / mt, 2)]:
        f = lambda t: ((1 + mp.sqrt(2) * mp.cos(t + TWO_PI_3 * k)) / (1 + mp.sqrt(2) * mp.cos(t)))**2 - ratio
        t = mp.findroot(f, TARGET)
        print(f"   theta_0 {lab}: {mp.nstr(t, 10)}  deviation of 2/9 = {mp.nstr(100*(t-TARGET)/TARGET, 4)} %")

    print("== VERDICT")
    if not green:
        print("   VOID: a control failed; no verdict.")
        return
    rel = abs(100 * (th - TARGET) / TARGET)
    pull = abs((th - TARGET) / dth)
    print(f"   theta_0(PDG 2024) deviates from 2/9 by {mp.nstr(rel, 3)} % ({mp.nstr(pull, 2)} sigma);"
          f" quoted as '{'0.001%' if rel < mp.mpf('0.0015') else 'NOT 0.001%'}' to one significant figure,"
          f" and '0.02%' is {'consistent' if abs(rel - mp.mpf('0.02')) < mp.mpf('0.005') else 'inconsistent'} with it.")


if __name__ == "__main__":
    main()
