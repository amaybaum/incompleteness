#!/usr/bin/env python3
"""SUBSTATE-2 unit F2-1, stage 2: the preregistered controls only.

Owner-authorized stage 2 (PR #1011 comment 6545904226). Runs the reference
controls C1-C10, the mutations M1-M10 and the decision-function self-test of
the frozen preregistration (66eb48ca) and amendment A-star (b86f0547), with
exact arithmetic only (fractions, exact Gaussian rationals, exact Q(sqrt -3)).
No R, R-dagger, P, Gate 4 or Gate 5 quantity is computed on any candidate:
stage 1 fixed none. The kernel facts the controls rest on enter the results
only as CI step conclusions; locally they are recorded as "pending" and the
unit token is withheld until they are supplied with --kernel.

Usage (from the repository root):
  python3 -I -B <this file>            check against the committed results.json
  python3 -I -B <this file> --write    write results.json (first execution only)
  python3 -I -B <this file> --kernel FILE
      FILE: {"head_sha", "run_url", "build_step", "axiom_check_step"} read from
      the host's job and step records; prints the unit decision as JSON.
"""
from fractions import Fraction as Fr
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
UNIT = HERE.parent.parent
ROOT = UNIT.parents[4]
SUBSTATE2 = UNIT.parent
RESULTS = HERE / "results.json"
LEAN = ROOT / "verification/lean-mathlib/OIBridge/F2CoherenceControls.lean"

PREREG_SHA256 = "389e7556bb2e23d165a9bcaf91b22a552bbad8dc3d1954f374add7b25bdfe17a"
ASTAR_SHA256 = "3d84c2054872046bdff88b52ba5ba7dfaa86bf5519fbf2e36d94efb25fdd5b05"
STAGE1_LOG_SHA256 = "5ce6cdc88eeb8ee9785f78410be4960dca8ac3ece87c7e561bc624de9c7bfd00"
ASTAR1_SHA256 = "184e331549a10b3e9eab6014223305f9f39de7f06fc77d7ffb1c75b6d414b2bb"


def require(ok, label):
    if not ok:
        raise RuntimeError("control failed: " + label)


def fr(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# ---------------------------------------------------------------- exact numbers

class G:
    """Exact Gaussian rational re + im*i."""
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(self, o): return G(self.re + o.re, self.im + o.im)
    def __sub__(self, o): return G(self.re - o.re, self.im - o.im)
    def __neg__(self): return G(-self.re, -self.im)
    def __mul__(self, o):
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    def __eq__(self, o): return self.re == o.re and self.im == o.im
    def conj(self): return G(self.re, -self.im)
    def norm2(self): return self.re * self.re + self.im * self.im
    def text(self): return f"{fr(self.re)}+{fr(self.im)}i"


class Q3:
    """Exact element a + b*sqrt(-3) of Q(sqrt -3)."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o): return Q3(self.a + o.a, self.b + o.b)
    def __sub__(self, o): return Q3(self.a - o.a, self.b - o.b)
    def __mul__(self, o): return Q3(self.a * o.a - 3 * self.b * o.b, self.a * o.b + self.b * o.a)
    def __eq__(self, o): return self.a == o.a and self.b == o.b
    def inv(self):
        n = self.a * self.a + 3 * self.b * self.b
        return Q3(self.a / n, -self.b / n)
    def text(self): return f"{fr(self.a)}+{fr(self.b)}*sqrt(-3)"


def mm(X, Y):
    n = len(X)
    return [[sum((X[i][k] * Y[k][j] for k in range(n)), G(0)) for j in range(n)] for i in range(n)]


def dag(X):
    n = len(X)
    return [[X[j][i].conj() for j in range(n)] for i in range(n)]


ROT = [[G(Fr(3, 5)), G(Fr(4, 5))], [G(Fr(-4, 5)), G(Fr(3, 5))]]   # DiagonalTheory.rot
PHASE = [[G(0, 1), G(0)], [G(0), G(1)]]                           # phaseGate (0,0) at level one
SWAP = [[G(0), G(1)], [G(1), G(0)]]
IDENT = [[G(1), G(0)], [G(0), G(1)]]


# ---------------------------------------------------------------- shared checks

FLAGGED = {"rot", "rotH", "phaseGate", "nonreal_diagonal_unitary", "fullClass"}


def screen(tags):
    """Screen item 1 on a declared generator or rule description: the flagged tags."""
    return sorted(t for t in tags if t in FLAGGED)


def nonreal_ratio(d0, d1):
    """Relative phase (A-star 3): two nonzero diagonal entries with a non-real ratio."""
    require(d0.norm2() != 0 and d1.norm2() != 0, "nonzero diagonal entries")
    q = d0 * d1.conj()
    return q.im != 0


def g4(U, Uinv):
    """Coherent return, and return under a dephasing between the steps, from visible 0."""
    coherent = mm(Uinv, U)[0][0].norm2()
    dephased = sum(U[k][0].norm2() * Uinv[0][k].norm2() for k in range(2))
    return coherent, dephased


def freq(U, p=2):
    """f(U): visible 1 after U from visible 0, under exponent p (p=2 is the trace rule)."""
    w = [U[k][0].norm2() for k in range(2)]
    if p == 2:
        return w[1] / (w[0] + w[1])
    if p == 1:
        raise RuntimeError("p=1 needs moduli; handled by freq_p1")
    w = [x ** (p // 2) for x in w]
    return w[1] / (w[0] + w[1])


def freq_p1_rational(U):
    """p=1 on entries whose moduli are rational (true for rot and rot^2)."""
    mods = []
    for k in range(2):
        e = U[k][0]
        require(e.im == 0, "p=1 control uses real entries")
        mods.append(abs(e.re))
    return mods[1] / (mods[0] + mods[1])


def g4b_label_ok(provenance, label):
    """An inserted dephasing must carry the label 'diagnostic'."""
    return not (provenance == "inserted" and label == "sourced")


def haar_invariant(weights, step, q):
    """Gate 3 form: the weights on Z/q are invariant under the step."""
    return all(weights[step(x) % q] == weights[x] for x in range(q))


# ---------------------------------------------------------------- C1, C6: odometer

def compression(m, r=2):
    """Theta-K compression of the odometer onto depth-m cylinders, computed at depth m+r."""
    q, Q = 2 ** m, 2 ** (m + r)
    K = [[Fr(0)] * q for _ in range(q)]
    for x in range(Q):
        K[x % q][(x + 1) % q] += Fr(1, Q)
    return [[e * q for e in row] for row in K]


def c1():
    out = []
    for m in range(1, 7):
        K = compression(m)
        q = 2 ** m
        require(all(e >= 0 for row in K for e in row), f"C1 nonnegative m{m}")
        require(all(e in (0, 1) for row in K for e in row), f"C1 0/1 entries m{m}")
        require(all(sum(row) == 1 for row in K), f"C1 ones-fixing rows m{m}")
        require(all(sum(K[i][j] for i in range(q)) == 1 for j in range(q)), f"C1 columns m{m}")
        require(haar_invariant([Fr(1, q)] * q, lambda x: x + 1, q), f"C1 Haar invariant m{m}")
        out.append({"depth": m, "permutation": True, "nonnegative": True, "ones_fixing": True,
                    "haar_invariant": True})
    return {"compressions": out, "class": "permClass (Theta-A) and nonnegClass (Theta-K)",
            "measure": "Haar, selected by unique ergodicity (paper; invariance checked m<=6)"}


def c6_odometer():
    q = 4
    chars = [[G(*((1, 0), (0, 1), (-1, 0), (0, -1))[(j * x) % 4]) for x in range(q)] for j in range(q)]
    eig = []
    for j in range(q):
        shifted = [chars[j][(x + 1) % q] for x in range(q)]
        lam = chars[j][1]
        require(all(shifted[x] == lam * chars[j][x] for x in range(q)), f"C6 character {j}")
        eig.append(lam)
    require(nonreal_ratio(eig[1], eig[0]), "C6 odometer relative phase")
    return {"basis": "characters of Z/4 (not the computed readout basis)",
            "diagonal": [e.text() for e in eig], "relative_phase_verified": True}


def c6_wave():
    L = 6
    zeta = Q3(Fr(1, 2), Fr(1, 2))                       # exp(i pi/3)
    powers = [Q3(1)]
    for _ in range(5):
        powers.append(powers[-1] * zeta)
    k = (1, 1, 4)
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    e = {s: powers[(k[0] * s[0] + k[1] * s[1] + k[2] * s[2]) % 6] for s in sites}

    def A(v):
        out = {}
        for (x, y, z) in sites:
            acc = Q3(0)
            for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                acc = acc + v[((x + d[0]) % L, (y + d[1]) % L, (z + d[2]) % L)]
                acc = acc + v[((x - d[0]) % L, (y - d[1]) % L, (z - d[2]) % L)]
            out[(x, y, z)] = acc
        return out

    Ae = A(e)
    a = Q3(1)
    require(all(Ae[s] == a * e[s] for s in sites), "C6 wave mode eigenvector, a_k = 1")
    lam_p, lam_m = Q3(Fr(1, 2), Fr(1, 2)), Q3(Fr(1, 2), Fr(-1, 2))
    for lam in (lam_p, lam_m):
        require(lam * lam - a * lam + Q3(1) == Q3(0), "C6 mode characteristic polynomial")
        u = {s: lam * e[s] for s in sites}
        Au = A(u)
        new_now = {s: Au[s] - e[s] for s in sites}          # W(u, e) = (A u - e, u)
        require(all(new_now[s] == lam * u[s] for s in sites) and
                all(u[s] == lam * e[s] for s in sites), "C6 two-slice eigenvector")
    ratio = lam_p * lam_m.inv()
    require(ratio.b != 0, "C6 wave relative phase non-real")
    return {"lattice": "periodic cubic L=6, alpha=1 two-slice rule over C", "mode": list(k),
            "a_k": a.text(), "diagonal": [lam_p.text(), lam_m.text()],
            "ratio": ratio.text(), "relative_phase_verified": True}


# ---------------------------------------------------------------- C2: classical hidden memory

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def g4d_classical(states, step, unstep, vis):
    """Return to the initial visible value after step then unstep, without and with an
    intermediate non-invasive readout (a copy into a fresh register)."""
    n = len(states)
    without = Fr(sum(1 for s in states if vis(unstep(step(s))) == vis(s)), n)
    hits = 0
    for s in states:
        t = step(s)
        register = vis(t)            # the copy changes no sub-state
        hits += vis(unstep(t)) == vis(s)
        require(register in (0, 1, 2, 3), "readout value")
    return without, Fr(hits, n)


def c2():
    rows = []
    for m in (1, 2, 3, 5, 7):
        st = list(range(256))
        f = (lambda m: lambda x: x ^ ((x >> m) & 1))(m)
        require(sorted(map(f, st)) == st, f"C2 B1 bijective m{m}")
        w, r = g4d_classical(st, f, f, lambda x: x & 1)
        require(w == 1 and r == 1, f"C2 B1 G4d m{m}")
        rows.append({"model": f"B1 depth {m}", "bijective": True, "return": [fr(w), fr(r)]})
    for n in range(3, 10):
        st = list(range(1 << n))
        sh = (lambda n: lambda x: (x >> 1) | ((x & 1) << (n - 1)))(n)
        un = (lambda n: lambda x: ((x << 1) & ((1 << n) - 1)) | (x >> (n - 1)))(n)
        require(sorted(map(sh, st)) == st and all(un(sh(x)) == x for x in st), f"C2 B2 n{n}")
        w, r = g4d_classical(st, sh, un, lambda x: x & 1)
        require(w == 1 and r == 1, f"C2 B2 G4d n{n}")
        rows.append({"model": f"B2 cycle {n}", "bijective": True, "return": [fr(w), fr(r)]})
    fs = load(SUBSTATE2 / "fixed-scale-skew/fixed_scale_probe.py", "fixed_scale_probe_ro")
    for n in range(3, 10):
        st = fs.states(n)
        stp = (lambda n: lambda x: fs.step(x, n))(n)
        und = (lambda n: lambda x: fs.undo(x, n))(n)
        require(sorted(map(stp, st)) == sorted(st) and all(und(stp(x)) == x for x in st),
                f"C2 FIXED-SCALE n{n}")
        w, r = g4d_classical(st, stp, und, fs.obs)
        require(w == 1 and r == 1, f"C2 FIXED-SCALE G4d n{n}")
        rows.append({"model": f"FIXED-SCALE tape {n}", "bijective": True, "return": [fr(w), fr(r)]})
    for L in (3, 4):
        st = [(p, tape) for p in range(3) for tape in range(4 ** L)]

        def blocks(t, L=L):
            return [((t >> (2 * k)) & 1, (t >> (2 * k + 1)) & 1) for k in range(L)]

        def pack(bl):
            return sum((a | (b << 1)) << (2 * k) for k, (a, b) in enumerate(bl))

        def step(s, L=L):
            p, t = s
            if p < 2:
                return (p + 1, t)
            bl = blocks(t)
            return (0, pack(bl[1:] + bl[:1]))

        def unstep(s, L=L):
            p, t = s
            if p > 0:
                return (p - 1, t)
            bl = blocks(t)
            return (2, pack(bl[-1:] + bl[:-1]))

        def vis(s):
            p, t = s
            a, b = blocks(t)[0]
            return (a, b, a ^ b)[p]

        require(sorted(map(step, st)) == sorted(st) and all(unstep(step(s)) == s for s in st),
                f"C2 XOR L{L}")
        w, r = g4d_classical(st, step, unstep, vis)
        require(w == 1 and r == 1, f"C2 XOR G4d L{L}")
        rows.append({"model": f"infinite-XOR cyclic truncation, {L} blocks", "bijective": True,
                     "return": [fr(w), fr(r)]})
    return {"models": rows, "class": "permClass (Theta-A: bijections of finite stages)"}


# ---------------------------------------------------------------- C7, C10: numerics

def held_out():
    S2 = mm(PHASE, PHASE)
    return {"rot": ROT, "rot2": mm(ROT, ROT), "rot_S_S_rot": mm(ROT, mm(S2, ROT))}


EXPECTED_FREQ = {"rot": Fr(16, 25), "rot2": Fr(576, 625), "rot_S_S_rot": Fr(0)}


def c7():
    require(mm(dag(ROT), ROT) == IDENT, "C7 rot isometry")
    coh, dep = g4(ROT, dag(ROT))
    require(coh == 1 and dep == Fr(337, 625), "C7 G4 values")
    fq = {k: freq(U) for k, U in held_out().items()}
    require(fq == EXPECTED_FREQ, "C7 trace-rule frequencies")
    return {"G4a": fr(coh), "G4b": fr(dep), "frequencies": {k: fr(v) for k, v in fq.items()}}


PAULI = [[[G(0), G(1)], [G(1), G(0)]], [[G(0), G(0, -1)], [G(0, 1), G(0)]],
         [[G(1), G(0)], [G(0), G(-1)]]]


def so3(U):
    """Bloch rotation R_ij = tr(sigma_i U sigma_j U^dagger)/2, exact."""
    R = []
    for i in range(3):
        row = []
        for j in range(3):
            M = mm(PAULI[i], mm(U, mm(PAULI[j], dag(U))))
            tr = M[0][0] + M[1][1]
            require(tr.im == 0, "Bloch entry real")
            row.append(tr.re / 2)
        R.append(row)
    return R


def apply(R, n):
    return [sum(R[i][j] * n[j] for j in range(3)) for i in range(3)]


def c10():
    """Kochen-Specker 1967 single-qubit model: hidden Bloch vector, outcome rule
    (1 + n.a)/2 as published, disturbing readout resets n to the outcome axis."""
    z = [Fr(0), Fr(0), Fr(1)]
    R, Rinv = so3(ROT), so3(dag(ROT))
    n1 = apply(R, z)
    coh = (1 + apply(Rinv, n1)[2]) / 2
    dep = Fr(0)
    for sgn in (1, -1):
        p = (1 + sgn * n1[2]) / 2
        back = apply(Rinv, [Fr(0), Fr(0), Fr(sgn)])
        dep += p * (1 + back[2]) / 2
    fq = {k: (1 - apply(so3(U), z)[2]) / 2 for k, U in held_out().items()}
    require(coh == 1 and dep == Fr(337, 625), "C10 G4 reproduction")
    require(fq == EXPECTED_FREQ, "C10 frequency reproduction")
    return {"G4a": fr(coh), "G4b": fr(dep), "frequencies": {k: fr(v) for k, v in fq.items()},
            "measure": "as published (state-dependent hidden density); a control, not a Gate 3 selection",
            "containment_theta_K": "paper: compressions onto hemisphere indicators are nonnegative"}


# ---------------------------------------------------------------- C9: depth-coupling mutant

def c9():
    npb = load(SUBSTATE2 / "native-padic-bridge/native_padic_probe.py", "native_padic_probe_ro")
    out = []
    for q in (4, 8):
        zero = (tuple([0] * npb.N), tuple([0] * npb.N))
        now = [0] * npb.N
        now[npb.ORIGIN] = 2
        higher = (tuple(now), tuple([0] * npb.N))
        require(npb.project(zero, 2) == npb.project(higher, 2), "C9 equal low bits")
        plain = npb.project(npb.native_step(zero, q), 2) == npb.project(npb.native_step(higher, q), 2)
        a, b = npb.native_step(zero, q, True), npb.native_step(higher, q, True)
        backflow = a[0][npb.ORIGIN] % 2 != b[0][npb.ORIGIN] % 2
        require(npb.native_unstep(a, q, True) == zero and npb.native_unstep(b, q, True) == higher,
                "C9 mutant reversible")
        require(plain and backflow, f"C9 q{q}")
        out.append({"q": q, "alpha1_backflow": False, "mutant_backflow": True})
    return {"cases": out}


# ---------------------------------------------------------------- decision rule (prereg 4)

TOKENS = {"0": "INCONCLUSIVE (void)", "1": "INCONCLUSIVE (gap)", "2a": "COUNTEREXAMPLE",
          "2b": "COUNTEREXAMPLE", "3a": "REPRESENTATION-ONLY", "3b": "REPRESENTATION-ONLY",
          "5": "PARTIAL", "6": "PARTIAL", "7": "PARTIAL", "8": "COUNTEREXAMPLE",
          "9": "INCONCLUSIVE (undecided)"}


def classify(c, grade=None):
    """Rows 2-9 for a candidate-like record; returns (token, row)."""
    R, P, S = c.get("R"), c.get("P"), c.get("S")
    Rd = c.get("Rdag") is True and c.get("Rdag_source") == "kernel"
    probes = c.get("probes") or {}
    G4 = c.get("G4")
    g4ok = None
    if G4 is not None:
        label = G4["b_label"] if g4b_label_ok(G4.get("b_provenance"), G4["b_label"]) else "diagnostic"
        g4ok = (G4["a"], label, G4["b"], G4["c"])
    if any(v.get("R") or v.get("P") for v in probes.values()):
        return TOKENS["2a"], "2a"
    if R is True and (c.get("G5a") == "refuted" or c.get("dagger_claim_refuted")):
        return TOKENS["2b"], "2b"
    if R is True and Rd and g4ok is not None and (
            not g4ok[0] or (g4ok[1] == "sourced" and not g4ok[2]) or not g4ok[3]):
        return TOKENS["2b"], "2b"
    if (R is True or P is True) and c.get("screen_flags"):
        return TOKENS["3a"], "3a"
    if R is False and P is False and c.get("exhibits_verified"):
        return TOKENS["3b"], "3b"
    probes_clean = c.get("transplantable") is True and probes and all(
        v.get("R") is False and v.get("P") is False for v in probes.values())
    if (R is True and Rd and P is True and S is True and c.get("N") is False and c.get("O") is False
            and c.get("G3") in ("selected", "no_dependence") and g4ok is not None
            and g4ok[0] and g4ok[1] == "sourced" and g4ok[2] and g4ok[3]
            and c.get("G5a") == "derived" and probes_clean):
        return "SOURCED-SUCCESS/" + (grade or "AVAILABLE"), "4"
    if R is True and P is True and S is False:
        return TOKENS["5"], "5"
    if R is True and P is True and S is True and not Rd:
        return TOKENS["6"], "6"
    if (R is True) != (P is True):
        return TOKENS["7"], "7"
    if R is True and Rd and P is True and S is True and (
            c.get("G3") == "dependent" or c.get("G5a") == "undetermined"
            or (g4ok is not None and g4ok[1] == "diagnostic") or c.get("transplantable") is False):
        return TOKENS["7"], "7"
    if R is False and P is False and not c.get("exhibits_verified"):
        return TOKENS["8"], "8"
    return TOKENS["9"], "9"


def has_float(x):
    if isinstance(x, float):
        return True
    if isinstance(x, dict):
        return any(has_float(v) for v in x.values())
    if isinstance(x, list):
        return any(has_float(v) for v in x)
    return False


def decide(res):
    """The unit decision: (token or None while kernel steps are pending, row, void reasons)."""
    void = []
    if has_float(res):
        void.append("0(iv) floating point")
    if not all(v["reference_pass"] for v in res["controls"].values()):
        void.append("0(i) control")
    if not res["G4d_pass"]:
        void.append("0(i) G4d")
    if not all(v["caught"] for v in res["mutations"].values()):
        void.append("0(i) mutation")
    if not all(res["selftest"].values()):
        void.append("0(i) self-test")
    if any(r.get("R") is True and (r.get("N") is True or r.get("O") is True)
           for r in res["control_records"].values()):
        void.append("0(i) C5 consistency")
    if not res["freeze"]["ok"]:
        void.append("0(ii) freeze")
    if res["measure_post_hoc"]:
        void.append("0(iii) measure")
    concl = [(v["build_step"], v["axiom_check_step"]) for v in res["kernel"].values()]
    if any("failure" in c for c in concl):
        void.append("0(v) kernel")
    if res["stage1"]["forbidden_computations"]:
        void.append("0(vi) pre-A-star computation")
    if any(not p["coupling_is_transplanted_C"] for p in res["probe_runs"].values()):
        void.append("0(vii) probe coupling")
    if void:
        return TOKENS["0"], "0", void
    if any(c != ("success", "success") for c in concl):
        return None, None, []
    cand = res["stage1"]["candidate"]
    if cand is None:
        return TOKENS["1"], "1", []
    tok, row = classify(cand, res["review"]["grade"])
    return tok, row, []


# ---------------------------------------------------------------- records and kernel map

def astar_statements():
    text = (UNIT / "amendments/A-star.md").read_text(encoding="utf-8")
    block = text.split("```lean\n", 1)[1].split("\n```", 1)[0]
    lines = block.split("\n")
    chunks, cur = [], None
    for ln in lines:
        if ln.startswith("def ") or ln.startswith("theorem "):
            if cur:
                chunks.append(cur)
            cur = [ln]
        elif cur is not None and ln.strip():
            cur.append(ln)
    if cur:
        chunks.append(cur)
    return ["\n".join(c).rstrip() for c in chunks]


CITED = ["SubstratumInterfaceAudit.permTheory_falsifierUnavailable",
         "FrozenSourcing.permTheory_phase_ceiling", "FrozenSourcing.permTheory_nonnegBounded",
         "FrozenSourcing.nonnegBounded_not_phasesAvailable", "FrozenSourcing.nonnegBounded_verdict",
         "RouteB.substratumTheory_falsifierUnavailable", "RouteB.substratumTheory_derivedOI",
         "FlowEndpoint.onesTheory_not_phasesAvailable", "FlowEndpoint.onesTheory_layerFlowExecutable",
         "PhaseSource.onesFixing_not_phasesAvailable", "InterventionLocality.genTheory_mono"]


def kernel_map(statements):
    lean = LEAN.read_text(encoding="utf-8")
    out = {}
    for st in statements:
        name = st.split()[1]
        out["F2CoherenceControls." + name] = {
            "statement_sha256": sha256(st.encode("utf-8")).hexdigest(),
            "statement_verbatim_in_module": st in lean,
            "build_step": "pending", "axiom_check_step": "pending"}
    for name in CITED:
        out[name] = {"statement_sha256": None, "statement_verbatim_in_module": True,
                     "build_step": "pending", "axiom_check_step": "pending"}
    return out


def control_records(numerics):
    """Candidate-like records of the controls, from the kernel declarations they cite and the
    exact checks above (C3's flagged generator, C6's verified exhibits)."""
    c3_flag = ["nonreal_diagonal_unitary"] if numerics["C3"]["phaseOperator_nonreal_ratio"] else []
    c6_ex = (numerics["C6"]["odometer"]["relative_phase_verified"]
             and numerics["C6"]["wave"]["relative_phase_verified"])
    return {
        "C1": {"R": False, "P": False, "N": True, "O": True, "screen_flags": [],
               "exhibits_verified": False},
        "C2": {"R": False, "P": False, "N": True, "O": True, "screen_flags": [],
               "exhibits_verified": False},
        "C3": {"R": False, "P": True, "screen_flags": screen(["permutation"] + c3_flag),
               "exhibits_verified": False},
        "C4": {"R": False, "P": False, "N": None, "O": True, "screen_flags": [],
               "exhibits_verified": False},
        "C6": {"R": False, "P": False, "N": True, "O": True, "screen_flags": [],
               "exhibits_verified": c6_ex},
        "C7": {"R": True, "Rdag": True, "Rdag_source": "kernel", "P": True, "N": False, "O": False,
               "screen_flags": screen(["fullClass"]), "exhibits_verified": False,
               "G4": {"a": True, "b": True, "b_label": "sourced", "b_provenance": "semantics",
                      "c": True}, "G5a": "derived"},
        "C8": {"R": True, "P": False, "N": False, "O": False, "screen_flags": screen(["rot"]),
               "exhibits_verified": False},
        "C10": {"R": False, "P": False, "N": True, "O": True, "screen_flags": [],
                "exhibits_verified": False},
    }


EXPECTED_ROWS = {"C1": "8", "C2": "8", "C3": "3a", "C4": "8", "C6": "3b", "C7": "3a",
                 "C8": "3a", "C10": "8"}


# ---------------------------------------------------------------- mutations

def candidate_base():
    return {"R": True, "Rdag": True, "Rdag_source": "kernel", "P": True, "S": True,
            "N": False, "O": False, "screen_flags": [], "exhibits_verified": False,
            "transplantable": True,
            "probes": {k: {"R": False, "P": False} for k in ("C1", "C2", "C10")},
            "G3": "selected",
            "G4": {"a": True, "b": True, "b_label": "sourced", "b_provenance": "semantics", "c": True},
            "G5a": "derived"}


def mutations():
    m = {}
    coh, dep = g4(SWAP, dag(SWAP))
    m["M1"] = {"what": "rot replaced by the swap", "returns": [fr(coh), fr(dep)],
               "caught": coh == dep == 1}
    flags = screen(["permutation", "nonreal_diagonal_unitary", "phaseGate"])
    m["M2"] = {"what": "phaseGate added to the C3 generator set", "flags": flags,
               "caught": "phaseGate" in flags}
    q = 8
    w = [Fr(x + 1, 36) for x in range(q)]
    m["M3"] = {"what": "non-invariant measure on the depth-3 odometer stage",
               "caught": not haar_invariant(w, lambda x: x + 1, q)}
    m["M4"] = {"what": "a float in a decision path", "caught": None}
    c = {"R": False, "P": False, "N": True, "O": True, "screen_flags": [], "exhibits_verified": False,
         "transplantable": True, "probes": {}}
    m["M5"] = {"what": "a C2 model in place of the candidate", "row": classify(c)[1]}
    m["M5"]["caught"] = m["M5"]["row"] != "4"
    m["M6"] = {"what": "an inserted dephasing relabelled sourced",
               "caught": not g4b_label_ok("inserted", "sourced")}
    p1 = {"rot": freq_p1_rational(ROT), "rot2": freq_p1_rational(mm(ROT, ROT))}
    c = candidate_base()
    c["G5a"] = "refuted" if any(p1[k] != EXPECTED_FREQ[k] for k in p1) else "derived"
    m["M7"] = {"what": "amplitudes encoded as measures (p = 1)",
               "frequencies": {k: fr(v) for k, v in p1.items()}, "row": classify(c)[1]}
    m["M7"]["caught"] = m["M7"]["row"] == "2b"
    c = candidate_base()
    c["Rdag_source"] = "assumed"
    m["M8"] = {"what": "R-dagger assumed instead of proved", "row": classify(c)[1]}
    m["M8"]["caught"] = m["M8"]["row"] != "4"
    flags = screen(["rot"])
    c = candidate_base()
    c["screen_flags"] = flags
    probe = candidate_base()
    probe["probes"] = {"C2": {"R": True, "P": False}}
    m["M10"] = {"what": "constant rule := rot applied to a C2 model", "flags": flags,
                "rows": [classify(c)[1], classify(probe)[1]]}
    m["M10"]["caught"] = m["M10"]["rows"][0] in ("3a", "2a") and m["M10"]["rows"][1] == "2a"
    return m


# ---------------------------------------------------------------- self-test

def green(candidate=None, grade=None):
    return {"controls": {"C1": {"reference_pass": True}}, "G4d_pass": True,
            "mutations": {"M1": {"caught": True}}, "selftest": {"x": True},
            "control_records": {}, "freeze": {"ok": True}, "measure_post_hoc": False,
            "kernel": {"k": {"build_step": "success", "axiom_check_step": "success"}},
            "stage1": {"candidate": candidate, "forbidden_computations": []},
            "probe_runs": {}, "review": {"grade": grade}}


def selftest_cases():
    cases = []

    def add(name, res, row):
        cases.append((name, res, row))

    r = green(); r["controls"]["C1"]["reference_pass"] = False; add("0(i)", r, "0")
    r = green(); r["freeze"]["ok"] = False; add("0(ii)", r, "0")
    r = green(); r["measure_post_hoc"] = True; add("0(iii)", r, "0")
    r = green(); r["extra"] = 0.5; add("0(iv)", r, "0")
    r = green(); r["kernel"]["k"]["build_step"] = "failure"; add("0(v)", r, "0")
    r = green(); r["stage1"]["forbidden_computations"] = ["R on a candidate"]; add("0(vi)", r, "0")
    r = green(); r["probe_runs"] = {"C1": {"coupling_is_transplanted_C": False}}; add("0(vii)", r, "0")
    add("1", green(), "1")
    r = green(); r["kernel"]["k"]["axiom_check_step"] = "pending"; add("pending", r, None)
    c = candidate_base(); c["probes"]["C10"] = {"R": True, "P": False}; add("2(a)", green(c), "2a")
    c = candidate_base(); c["G5a"] = "refuted"; add("2(b) Gate 5a", green(c), "2b")
    c = candidate_base(); c["G4"]["a"] = False; add("2(b) G4a", green(c), "2b")
    c = candidate_base(); c["screen_flags"] = ["rot"]; add("3(a)", green(c), "3a")
    c = {"R": False, "P": False, "exhibits_verified": True}; add("3(b)", green(c), "3b")
    add("4 available", green(candidate_base()), "4")
    add("4 derived", green(candidate_base(), "DERIVED"), "4")
    c = candidate_base(); c["S"] = False; add("5", green(c), "5")
    c = candidate_base(); c["Rdag"] = None; add("6", green(c), "6")
    c = candidate_base(); c["P"] = False; add("7 one of R, P", green(c), "7")
    c = candidate_base(); c["transplantable"] = False; c["probes"] = {}
    add("7 not transplantable", green(c), "7")
    c = {"R": False, "P": False, "exhibits_verified": False}; add("8", green(c), "8")
    c = {"R": False, "P": False, "exhibits_verified": False, "transplantable": False, "probes": {}}
    add("8 not transplantable", green(c), "8")
    c = candidate_base(); c["R"] = None; c["P"] = None; add("9", green(c), "9")
    return cases


def run_selftest(decider):
    out = {}
    for name, res, row in selftest_cases():
        tok, got, _ = decider(res)
        ok = got == row
        if name == "4 derived":
            ok = ok and tok == "SOURCED-SUCCESS/DERIVED"
        if name == "4 available":
            ok = ok and tok == "SOURCED-SUCCESS/AVAILABLE"
        out[name] = ok
    return out


# ---------------------------------------------------------------- assembly

def build():
    statements = astar_statements()
    require(len(statements) == 19, "A-star fixes nineteen statements")
    prereg = sha256((UNIT / "preregistration.md").read_bytes()).hexdigest()
    astar = sha256((UNIT / "amendments/A-star.md").read_bytes()).hexdigest()
    log = sha256((UNIT / "amendments/stage1-log.json").read_bytes()).hexdigest()
    astar1 = sha256((UNIT / "amendments/A-star-1.md").read_bytes()).hexdigest()
    stage1 = json.loads((UNIT / "amendments/stage1-log.json").read_text(encoding="utf-8"))
    kern = kernel_map(statements)
    freeze_ok = (prereg == PREREG_SHA256 and astar == ASTAR_SHA256 and log == STAGE1_LOG_SHA256
                 and astar1 == ASTAR1_SHA256
                 and all(v["statement_verbatim_in_module"] for v in kern.values()))

    numerics = {"C1": c1(), "C2": c2(),
                "C3": {"phaseOperator": "diag(i, 1)",
                       "phaseOperator_nonreal_ratio": nonreal_ratio(PHASE[0][0], PHASE[1][1])},
                "C6": {"odometer": c6_odometer(), "wave": c6_wave()},
                "C7": c7(), "C9": c9(), "C10": c10()}
    recs = control_records(numerics)
    controls = {}
    for cid, rec in recs.items():
        tok, row = classify(rec)
        controls[cid] = {"token": tok, "row": row, "expected_row": EXPECTED_ROWS[cid],
                         "reference_pass": row == EXPECTED_ROWS[cid]}
    c5 = not any(r.get("R") is True and (r.get("N") is True or r.get("O") is True)
                 for r in recs.values())
    controls["C5"] = {"token": None, "row": None, "expected_row": None, "reference_pass": c5}
    controls["C9"] = {"token": None, "row": None, "expected_row": None, "reference_pass": True}
    g4d = (all(m["return"] == ["1", "1"] for m in numerics["C2"]["models"])
           and numerics["C10"]["G4a"] == "1" and numerics["C10"]["G4b"] == "337/625")

    muts = mutations()
    bad = green()
    bad["extra"] = 0.25
    muts["M4"]["caught"] = decide(bad)[1] == "0"
    st = run_selftest(decide)

    def hardcoded(res):
        return "SOURCED-SUCCESS/AVAILABLE", "4", []

    muts["M9"] = {"what": "a verdict template hardcoding success",
                  "caught": not all(run_selftest(hardcoded).values())}

    res = {
        "schema": "f2-1-results/1",
        "prereg": {"commit": "66eb48ca64a79ffef98c8b086293f454a3dbeab6", "sha256": prereg},
        "amendment": {"commit": "b86f0547011ab7ce0465d7a15cdcacc726b13b57", "sha256": astar,
                      "stage1_log_sha256": log},
        "amendment_1": {"commit": "fdeeb2d5ba17a8f3e93aa2f08f3ca21e9ae60081", "sha256": astar1},
        "run": {"id": "run-2", "preserved_earlier_attempt": "05ecc8732160736b538b422114a5a1738d682c16",
                "preserved_earlier_ci_run": "41220197866", "preserved_earlier_outcome": "INCONCLUSIVE (void)"},
        "stage1": {"candidate": None, "gap": "G-star (A-star 4)", "clause4_reachable": False,
                   "forbidden_computations": stage1["forbidden_computations_run"]},
        "freeze": {"ok": freeze_ok},
        "measure_post_hoc": False,
        "kernel": kern,
        "exact": numerics,
        "controls": controls,
        "control_records": recs,
        "G4d_pass": g4d,
        "probes": {"C1": None, "C2": None, "C10": None},
        "probe_runs": {},
        "mutations": muts,
        "selftest": st,
        "labels": {"G4b_dephasing": "n/a"},
        "review": {"grade": None, "reviewer": None, "time": None, "quote": None},
    }
    tok, row, void = decide(res)
    res["token"] = tok
    res["void_reasons"] = void
    res["verdict_status"] = ("awaiting CI step conclusions for the kernel declarations"
                             if tok is None and not void else "decided")
    green_kernel = json.loads(json.dumps(res))
    for v in green_kernel["kernel"].values():
        v["build_step"] = v["axiom_check_step"] = "success"
    res["token_if_kernel_steps_succeed"] = decide(green_kernel)[0]
    return res


def dump(res):
    return (json.dumps(res, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def main(argv):
    res = build()
    data = dump(res)
    if "--kernel" in argv:
        k = json.loads(Path(argv[argv.index("--kernel") + 1]).read_text(encoding="utf-8"))
        for v in res["kernel"].values():
            v["build_step"], v["axiom_check_step"] = k["build_step"], k["axiom_check_step"]
        tok, row, void = decide(res)
        sys.stdout.write(json.dumps({"head_sha": k.get("head_sha"), "run_url": k.get("run_url"),
                                     "token": tok, "row": row, "void_reasons": void},
                                    sort_keys=True) + "\n")
        return 0 if tok is not None else 1
    if "--write" in argv:
        require(not RESULTS.exists(), "results.json exists; --write is for the first execution only")
        RESULTS.write_bytes(data)
        sys.stdout.write("wrote results.json\n")
        return 0
    require(RESULTS.exists(), "results.json missing")
    require(RESULTS.read_bytes() == data, "results differ from the committed results.json")
    require(res["void_reasons"] == [], "void: " + ", ".join(res["void_reasons"]))
    sys.stdout.write("F2-1 stage 2: all controls, mutations and self-test as preregistered; "
                     f"token {res['token']} ({res['verdict_status']}); "
                     f"if kernel steps succeed: {res['token_if_kernel_steps_succeed']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
