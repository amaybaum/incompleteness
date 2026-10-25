"""Points where PLAN.md, as written, does not determine the computation or a reading of it.

None of them is decided in code. Each item lists the readings the code implements; where it is
cheap, every reading is computed and recorded, so the decision needs no recomputation. An item is
resolved only by the machine-readable `pe01-resolutions` block of amendment A2 in ../amendments/,
which TH pins as it pins A1 (params.py). A run in result mode refuses to start while any item is
unresolved or names a reading not listed here.
"""

PENDING = {
    "B3W-K0": (
        "B3 window class, K0. §3 asks for exact max over (window, test) of min_phi over all tests on "
        "windows of w <= 16; a window carries 2^(2^w) tests. Computed: the average case exactly by "
        "stationarity (mu is phi-invariant, so windows of equal length have equal marginals, checked) "
        "and sign-pattern decomposition over the union of supports; the deterministic worst case exactly "
        "for w <= 4 and as the U-form interval for 5 <= w <= 16."
    ),
    "LF-A": (
        "Linear-filter observers: §3 defines them by rho_x(v) = A v XOR x b and does not state a. "
        "Computed for passive linear filters (a = 0), named so in every output."
    ),
    "WIT-A": (
        "Condition (a): which generators. Computed for the fixed G_lin(p_n), G_filt(p_n), G_clk(p_n); "
        "other family members enter through the K0 status only (conservative toward the claim under audit)."
    ),
    "TAG-L": (
        "§6 item 5, COVERED-literature: the mechanical form of the four closed forms. Computed as L1-L4 "
        "(B1 fires on G_lin at n+1; B2 at lambda = n+1 equals 1 - Pr_Q[LC <= n+1] with its K_delta; the "
        "B4 counting horizon, subsumed by COVERED-corpus; a curve equal to max(0, 1 - 2^(n-K))), "
        "COVERED-corpus first. L2 as computed compares the B2 K1 horizons (maximum over lambda) with the "
        "closed form at lambda = n+1; that is conservative (it never gives a false COVERED tag) and tags "
        "only where lambda = n+1 is the earliest to fire. The exact comparison would use the closed-form "
        "K1 maximum over lambda; reading 'L1-L4' is the conservative form."
    ),
    "D-SIGN": (
        "Condition (d): |adv| (the literal §2 definition) lets a fixed chi alternate orientation across "
        "the window. Both readings are computed: 'signed' (Pr[chi = X_K'] - 1/2 >= 1/8 at every K') and "
        "'abs' (|.| >= 1/8). A2 selects which is the COUNTEREXAMPLE rule; the other is a measurement."
    ),
}

READINGS = {
    "B3W-K0": ("exact-average+interval-worst",),
    "LF-A": ("passive",),
    "WIT-A": ("fixed-primary",),
    "TAG-L": ("L1-L4",),
    "D-SIGN": ("signed", "abs"),
}


def open_items(resolutions=None):
    """PENDING ids not resolved by A2's block with a listed reading."""
    res = resolutions or {}
    return sorted(k for k in PENDING if res.get(k) not in READINGS[k])
