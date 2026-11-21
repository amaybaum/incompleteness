"""Model-side predictions for the BTFR-z test (no observational data is read here).

Everything in this module is fixed at the preregistration commit.

Cosmology (H(z) model).  GR §7.3 extends the radial law to "the supplied flat
cosmological background", H(z) = H0 sqrt(Om (1+z)^3 + OL).  Primary parameters:
Planck 2018 VI (TT,TE,EE+lowE+lensing, Table 2): H0 = 67.36 km/s/Mpc,
Om = 0.3153, OL = 1 - Om (flat; radiation neglected, < 1e-3 effect on E(z) at z < 3).
GR quotes H0 = 67.4; the ratio E(z) = H(z)/H0 does not depend on H0.

OI law (GR §7.3): a0(z) = c H(z) / 6.  Deep-MOND limit: v_flat^4 = G M_b a0(z), so
at fixed v_flat the baryonic mass shifts by  dlogM = -log10 E(z)  (the "asymptotic"
prediction, P_asym).

Forward model (P_vmax).  The high-z velocities are peak circular velocities of an
exponential-disk model (v_circ,max), not v_flat.  For a baryonic exponential disk of
mass M and scale length R_d, the OI radial law g = g_N nu(g_N / a0) gives a
rotation curve whose maximum over 0 < r <= r_obs is V_max(M, R_d, a0).  Inverting
at fixed V gives log M(V; R_d, a0).  Variants (each a stated model choice, none
fitted):
  geometry : 'sph'  -- enclosed mass in the spherical approximation (GR's convention)
             'disk' -- Freeman thin exponential disk
  nu       : 'simple' -- nu(y) = (1 + sqrt(1 + 4/y)) / 2   (GR §7.3 Step 4)
             'rar'    -- nu(y) = 1 / (1 - exp(-sqrt(y)))    (McGaugh+2016 RAR form)
  H0       : 67.36 or 73.0 km/s/Mpc (sets the absolute a0(0) = c H0 / 6)
  Om       : 0.3153, with 0.30 and 0.33 as the cosmology band
"""
import math
import numpy as np

G = 4.30091727e-6          # kpc (km/s)^2 / Msun
C_KMS = 299792.458         # km/s
KPC_KM = 3.0856775814913673e16
MPC_KPC = 1.0e3

OM_PRIMARY = 0.3153
H0_PRIMARY = 67.36
OM_BAND = (0.30, 0.33)
H0_BAND = (67.36, 73.0)


def E(z, om=OM_PRIMARY):
    z = np.asarray(z, dtype=float)
    return np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def a0_kpc(h0=H0_PRIMARY):
    """a0(0) = c H0 / 6 in (km/s)^2 / kpc."""
    h0_per_s = h0 / (MPC_KPC * KPC_KM)          # 1/s
    a0_kms2 = C_KMS * h0_per_s / 6.0             # km/s^2
    return a0_kms2 * KPC_KM                      # (km/s)^2 / kpc


def a0_si(h0=H0_PRIMARY):
    return C_KMS * 1e3 * (h0 * 1e3 / 3.0856775814913673e22) / 6.0


def P_asym(z, om=OM_PRIMARY):
    """Deep-MOND OI shift of log M_b at fixed v_flat."""
    return -np.log10(E(z, om))


# ---- Modified Bessel functions (Abramowitz & Stegun 9.8.1-9.8.8) -------------
def _i0(x):
    t = x / 3.75
    if x <= 3.75:
        t2 = t * t
        return 1 + t2 * (3.5156229 + t2 * (3.0899424 + t2 * (1.2067492 + t2 * (
            0.2659732 + t2 * (0.0360768 + t2 * 0.0045813)))))
    u = 1.0 / t
    return (math.exp(x) / math.sqrt(x)) * (0.39894228 + u * (0.01328592 + u * (
        0.00225319 + u * (-0.00157565 + u * (0.00916281 + u * (-0.02057706 + u * (
            0.02635537 + u * (-0.01647633 + u * 0.00392377))))))))


def _i1(x):
    t = x / 3.75
    if x <= 3.75:
        t2 = t * t
        return x * (0.5 + t2 * (0.87890594 + t2 * (0.51498869 + t2 * (0.15084934 + t2 * (
            0.02658733 + t2 * (0.00301532 + t2 * 0.00032411))))))
    u = 1.0 / t
    return (math.exp(x) / math.sqrt(x)) * (0.39894228 + u * (-0.03988024 + u * (
        -0.00362018 + u * (0.00163801 + u * (-0.01031555 + u * (0.02282967 + u * (
            -0.02895312 + u * (0.01787654 - u * 0.00420059))))))))


def _k0(x):
    if x <= 2.0:
        t = x * x / 4.0
        return (-math.log(x / 2.0) * _i0(x)) + (-0.57721566 + t * (0.42278420 + t * (
            0.23069756 + t * (0.03488590 + t * (0.00262698 + t * (0.00010750 + t * 0.0000074))))))
    u = 2.0 / x
    return (math.exp(-x) / math.sqrt(x)) * (1.25331414 + u * (-0.07832358 + u * (
        0.02189568 + u * (-0.01062446 + u * (0.00587872 + u * (-0.00251540 + u * 0.00053208))))))


def _k1(x):
    if x <= 2.0:
        t = x * x / 4.0
        return (math.log(x / 2.0) * _i1(x)) + (1.0 / x) * (1 + t * (0.15443144 + t * (
            -0.67278579 + t * (-0.18156897 + t * (-0.01919402 + t * (-0.00110404 - t * 0.00004686))))))
    u = 2.0 / x
    return (math.exp(-x) / math.sqrt(x)) * (1.25331414 + u * (0.23498619 + u * (
        -0.03655620 + u * (0.01504268 + u * (-0.00780353 + u * (0.00325614 - u * 0.00068245))))))


def bessel_selftest():
    ref = {"i0": 1.2660658777520082, "i1": 0.5651591039924851,
           "k0": 0.42102443824070834, "k1": 0.6019072301972346}
    got = {"i0": _i0(1.0), "i1": _i1(1.0), "k0": _k0(1.0), "k1": _k1(1.0)}
    ref5 = {"i0": 27.239871823604442, "k0": 0.0036910983340425942}
    got5 = {"i0": _i0(5.0), "k0": _k0(5.0)}
    err = max(abs(got[k] / ref[k] - 1) for k in ref)
    err5 = max(abs(got5[k] / ref5[k] - 1) for k in ref5)
    return max(err, err5)


# ---- Newtonian baryonic field of an exponential disk -------------------------
def gN(r, M, Rd, geometry):
    """Newtonian radial acceleration ((km/s)^2/kpc) at radius r (kpc)."""
    x = r / Rd
    if geometry == "sph":
        menc = M * (1.0 - (1.0 + x) * math.exp(-x))
        return G * menc / (r * r)
    if geometry == "disk":
        y = 0.5 * x
        sig0 = M / (2.0 * math.pi * Rd * Rd)
        v2 = 4.0 * math.pi * G * sig0 * Rd * y * y * (_i0(y) * _k0(y) - _i1(y) * _k1(y))
        return v2 / r
    raise ValueError(geometry)


def nu(y, form):
    if form == "simple":
        return 0.5 * (1.0 + math.sqrt(1.0 + 4.0 / y))
    if form == "rar":
        return 1.0 / (1.0 - math.exp(-math.sqrt(y)))
    raise ValueError(form)


def vmax(M, Rd, a0, geometry, form, r_obs):
    """Peak circular velocity over 0 < r <= r_obs under g = gN nu(gN/a0)."""
    rs = np.linspace(r_obs / 400.0, r_obs, 400)
    best = 0.0
    for r in rs:
        g = gN(r, M, Rd, geometry)
        v = math.sqrt(r * g * nu(g / a0, form))
        if v > best:
            best = v
    return best


def logM_at_V(V, Rd, a0, geometry, form, r_obs, lo=6.0, hi=14.0):
    """Invert vmax(M) = V for log10 M by bisection (vmax is monotone in M)."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if vmax(10.0 ** mid, Rd, a0, geometry, form, r_obs) < V:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


RE_TO_RD = 1.6783469900166608     # R_e / R_d for an exponential disk


def P_vmax_variants(V, z1, Re1, z2, Re2, a0_scaling, extent_re=2.5):
    """Predicted log M(V) at epoch 2 minus epoch 1, for all model variants.

    a0_scaling(z, om) returns a0(z)/a0(0) for the model under test
    (OI: E(z); constant-a0 MOND: 1).  Radii in kpc; the peak is taken within
    r <= extent_re * R_e (the typical extent of the high-z data, Übler+2017 §2.3).
    Returns dict variant -> shift (dex).
    """
    out = {}
    for geometry in ("sph", "disk"):
        for form in ("simple", "rar"):
            for h0 in H0_BAND:
                for om in (OM_PRIMARY,) + OM_BAND:
                    a00 = a0_kpc(h0)
                    Rd1, Rd2 = Re1 / RE_TO_RD, Re2 / RE_TO_RD
                    m1 = logM_at_V(V, Rd1, a00 * a0_scaling(z1, om), geometry, form, extent_re * Re1)
                    m2 = logM_at_V(V, Rd2, a00 * a0_scaling(z2, om), geometry, form, extent_re * Re2)
                    out[(geometry, form, h0, om)] = m2 - m1
    return out


def summarize(variants):
    primary = variants[("sph", "simple", H0_PRIMARY, OM_PRIMARY)]
    vals = list(variants.values())
    return {"central": primary, "band_halfwidth": 0.5 * (max(vals) - min(vals)),
            "min": min(vals), "max": max(vals)}


def oi_scaling(z, om):
    return float(E(z, om))


def mond_scaling(z, om):
    return 1.0


def limit_controls():
    """C6: the forward model must reduce to its analytic limits.

    deep-MOND limit (tiny, extended disk, peak taken far out): shift -> -log10 E(z)
    Newtonian limit (massive, compact disk, peak inside the Newtonian core): shift -> 0
    """
    a00 = a0_kpc()
    z = 2.0
    res = {}
    # deep-MOND: V = 30 km/s, R_d = 20 kpc, peak searched to 200 R_d
    for geometry in ("sph",):
        m0 = logM_at_V(30.0, 20.0, a00, geometry, "simple", 4000.0)
        mz = logM_at_V(30.0, 20.0, a00 * float(E(z)), geometry, "simple", 4000.0)
        res["deep_mond_shift"] = mz - m0
    res["deep_mond_expected"] = float(P_asym(z))
    # Newtonian: V = 600 km/s, R_d = 0.3 kpc, peak within 2.5 R_e
    re = 0.3 * RE_TO_RD
    m0 = logM_at_V(600.0, 0.3, a00, "sph", "simple", 2.5 * re)
    mz = logM_at_V(600.0, 0.3, a00 * float(E(z)), "sph", "simple", 2.5 * re)
    res["newton_shift"] = mz - m0
    res["newton_expected"] = 0.0
    return res


if __name__ == "__main__":
    import json
    print("bessel max rel err:", bessel_selftest())
    print("a0(0) [m/s^2] at H0=67.36:", a0_si(), " at 73:", a0_si(73.0))
    for zz in (1, 2, 3):
        print(f"E({zz}) = {float(E(zz)):.3f}   P_asym = {float(P_asym(zz)):+.3f}")
    print("limit controls:", json.dumps(limit_controls()))
    # Nominal preview at the KMOS3D bin centres and published median sizes
    # (Übler+2017 Table 1: R_e = 4.8 kpc at z~0.9, 4.0 kpc at z~2.3); V_ref = 242 km/s.
    V = 242.0
    for name, sc in (("OI", oi_scaling), ("MOND-const", mond_scaling)):
        s = summarize(P_vmax_variants(V, 0.9, 4.8, 2.3, 4.0, sc))
        print(name, "T2 nominal P_vmax:", json.dumps({k: round(v, 3) for k, v in s.items()}))
    print("OI T2 nominal P_asym:", round(float(P_asym(2.3) - P_asym(0.9)), 3))
