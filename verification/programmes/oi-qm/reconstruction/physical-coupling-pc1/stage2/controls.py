"""PC-1 stage 2, controls only.

Implements exactly what amendments/PC-S2.md (4d2c4d56) and amendments/PC-S2-C13.md (895e5c5b)
freeze, under the preregistration (948b30c1). No candidate exists (PC★), so nothing is computed on
any candidate: no probe is run, and no R, P, P1, Gauge, section-7 or held-out quantity is computed
on a new or previously rejected candidate. The section-7 values are computed only for the
controls C7 and C10.

Standard library only; exact arithmetic (fractions, Gaussian rationals, Q(sqrt 3), Q(sqrt -3));
checks use require(), never assert, so normal and -O runs are identical.

    python3 -I -B controls.py            # regenerate and compare with results.json
    python3 -I -B controls.py --write    # first execution only
    python3 -I -B controls.py --kernel kernel-steps.json [--review review.json]
"""

from fractions import Fraction as Fr
from hashlib import sha1, sha256
from math import isqrt
from pathlib import Path
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
UNIT = HERE.parent
ROOT = UNIT.parents[4]
RESULTS = HERE / "results.json"
OIB = ROOT / "verification/lean-mathlib/OIBridge"
PC1_LEAN = OIB / "PC1Controls.lean"
F21_LEAN = OIB / "F2CoherenceControls.lean"
VENDOR = HERE / "vendor/recursive-substates"

GAP_TOKEN = "INCONCLUSIVE (" + "gap)"          # the gap token's name, used only to check absence
VOID_TOKEN = "INCONCLUSIVE (void)"


def require(ok, label):
    if not ok:
        raise RuntimeError("check failed: " + label)


def git_blob(data):
    return sha1(b"blob %d\0" % len(data) + data).hexdigest()


# ---------------------------------------------------------------- frozen inputs (PC-S2 table; PC-S2-C13)

FROZEN = {
    "preregistration.md": ("414f31686e7890117abaa599b7e7ef18b7049ae8",
                           "9754d93187b8ffc68645f4873247aaac73dc26b78880a05dec0b3ef5b8ee87fc"),
    "amendments/PC-star.md": ("79aad250aa63558c18739d94ba114baced78ca1d",
                              "97e3567e1303ccda1698f9f19dad069f3bbbf93013021dd281a4751f643532b6"),
    "amendments/stage1-log.json": ("744c28c88d31176847c55d89946670706bb39a02",
                                   "6f2b74b70dd2d589c3a24975c3ee1d924c296ccf00d72b0d63b8c65d434aa3ab"),
    "amendments/PC-star-disposition.md": ("a94c531b2e8cedf5fc8b05848bcd41e1cc6b3cf0",
                                          "4dac1d3599740af6621138b64e071dba48963ab9974e661bc544fef533c77207"),
    "amendments/PC-S2.md": ("f81dca8cd4bc231a3e97377b73430cc9749590e3",
                            "ad6ed9b53400451a5b2f0d73d839142263d59ca9b9e871e75c7daf51efcbb5d6"),
    "amendments/PC-S2-C13.md": ("2b68474be1c035f02ecf1fd2dc57a898e2680921",
                                "bf4aa26fa712fa5d5950038ffb9b3b4ecd6680ab69cec84778aa9f13f5403cca"),
}
COMMITS = {"preregistration.md": "948b30c10e575aec2f449f97428192c4bba2628f",
           "amendments/PC-star.md": "72b4af275193ba65bbe8eea690d83b9c3ec28fb6",
           "amendments/stage1-log.json": "9245d542",
           "amendments/PC-star-disposition.md": "89a8feba039303d26e4d1c280f2ee082e290ace9",
           "amendments/PC-S2.md": "4d2c4d56a855decd6ab80a3b512f9f5f7e7cc8fe",
           "amendments/PC-S2-C13.md": "895e5c5b1ca99a5efcbab643417cdf1a7c421a8a"}
DISPOSITION_SHA256 = FROZEN["amendments/PC-star-disposition.md"][1]

VENDORED = {   # S2-2: destination -> (blob at 4e7ddb70, sha256)
    "verification/lean-mathlib/OIBridge/F2CoherenceControls.lean":
        ("fbf475043ce589ccf1bfac511898eda821636137",
         "66ab7a9c96e7eda9385a08208483164f65621a064cb9b2167e40d2783c092897"),
    "stage2/vendor/recursive-substates/f2-1-coherence-sourcing/stage2/run-2/controls.py":
        ("18c519f3a423db7506d1438b8ef22a9ca847e481",
         "7994448e707373cb0f64c5cc262508d1d61c7703b2783f3b64b1fbf1625dc09f"),
    "stage2/vendor/recursive-substates/fixed-scale-skew/fixed_scale_probe.py":
        ("313c2f80476d3d464b75f3b98ed48379959b5ac6",
         "524c599e89282f7d1d9e95f60f1a36d4cff630afdac464cbea3057276bf39f8c"),
    "stage2/vendor/recursive-substates/native-padic-bridge/native_padic_probe.py":
        ("0bdb22325d44394bbaa590581a71bc13e6d62608",
         "72ff1a1bc5cc8cab9fb72bc46d5e2301216972fef682847380fb4063a29c092c"),
}

# Every OIBridge module other than the two stage-2 modules, as at 5914c17c: sha256 over the sorted
# lines "<file> <git blob>\n".
OIBRIDGE_OTHERS_SHA256 = "2d91bf59c2d8f4b367af458dfa5f44d71ce265a5397c1d4f095d67e24f61ce8a"
NEW_MODULES = {"F2CoherenceControls.lean", "PC1Controls.lean"}

# The 19 F2-1 statements (A★-1.3 table), kept by the vendored module's blob identity.
F21_STATEMENTS = {
    "OnesBounded": "ca5a780aef401ef352a4d94c5045aedc75d16a37f6e5c24ea0e761b762affc79",
    "rot_not_preservesNonneg": "9f8f95080d250efa528ae9db248f849a886a348eb5942a4efad638a502744550",
    "rot_moves_ones": "5632c158fa1c1887c45a1b05540bf162a27d84a82b05390ddd689128206d6e2e",
    "falsifierUnavailable_of_nonnegBounded": "aab60341150c338d416a4531023fd90b00589d8940bfff9ae7e8460611041528",
    "falsifierUnavailable_of_onesBounded": "daa04869a79f782c79502253d37608e6a4feb493af0c4e350e050ab302cab695",
    "onesBounded_of_onesFixing": "0fd3fa9b489e3b0f09cb829a54fa1946b65a7918dd3d458e4fa0175abffe9dec",
    "permTheory_onesBounded": "4445000e19eeecbb6570455bef79ecc1de8193c7669a782a4c941dbb2e32a66a",
    "onesTheory_falsifierUnavailable": "1d12f11ba87c988907463e0f7d7a2c70365ebc4fcd1cf79cf2a4e692d7550703",
    "nonnegClass": "0442e82e1febdfe0062677902c5857f06b5877508d22fc6a2dca2a252809e1e2",
    "nonnegClass_arch": "8b0f3899e3ae902edf8a5b7c009ae291093a7f979159dc60ce43065fdf4b1a5a",
    "nonnegClass_nonnegBounded": "2ba9a7adcb1e84896853044a24479a6dd4e230efe2768ef95ec160e97f015162",
    "nonnegClass_onesFixing": "38778839677136914faa94da81166a5e219303ada81497ef1a57fa0c8049fe68",
    "realClass": "24a871a5b99105b22db0606298a80123dc61322974b40bbc43a90c63f233716a",
    "realClass_arch": "e9b667c38e423195347c0f02ddbaad7d4d718acef0de3e859de0718365f3fdd7",
    "realTheory_rot": "ff2463bead80562b2ebf649680556b9f8fb10fc639deda7054548f5044103fed",
    "realTheory_not_phases": "72fbf03898979884713e3a1f2b1480748fbcb8c684f9b497a6f2b909a8565f59",
    "fullTheory_rot": "aa7d163085000219847fe36a95141d6e587de040dc3db71fe87557bb61fe5a64",
    "fullTheory_rotDagger": "1a14a6a3d6562d38515f64c5184c030689769733c4bf79ebbe02940ad7a8c64f",
    "fullTheory_phases": "44896c9e71b69b2d6688a00bf63c23d7665a190a846c1c86db1db2963246963d",
}
F21_COMBINED = "ee8a6ce6bbc2badf86d86dc808b17d2d7db987698b01df647a119febfbb0f5a3"

CITED = ["SubstratumInterfaceAudit.permClass_permMatrix", "SubstratumInterfaceAudit.permTheory_falsifierUnavailable",
         "FrozenSourcing.permTheory_nonnegBounded", "FrozenSourcing.permTheory_phase_ceiling",
         "FrozenSourcing.nonnegBounded_not_phasesAvailable", "RouteB.substratumTheory_derivedOI",
         "RouteB.substratumTheory_falsifierUnavailable", "FlowEndpoint.onesTheory_not_phasesAvailable",
         "InterventionLocality.instAvail_mono", "MicroReversibility.exists_scaled_mem_of_instAvail_unitary",
         "InterventionLocality.genTheory_mono"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


F21 = load(VENDOR / "f2-1-coherence-sourcing/stage2/run-2/controls.py", "f21_controls_vendored")
G, Q3, mm, dag, fr = F21.G, F21.Q3, F21.mm, F21.dag, F21.fr
ROT, PHASE, SWAP, IDENT = F21.ROT, F21.PHASE, F21.SWAP, F21.IDENT


# ---------------------------------------------------------------- freeze, vendor, statements

def pcs2_statements():
    """S2-3 extraction rule on the first lean block of PC-S2.md: (header, statements)."""
    text = (UNIT / "amendments/PC-S2.md").read_text(encoding="utf-8")
    block = text.split("```lean\n", 1)[1].split("\n```", 1)[0]
    header, chunks, cur = [], [], None
    for ln in block.split("\n"):
        if ln.startswith(("def ", "noncomputable def ", "theorem ")):
            if cur:
                chunks.append(cur)
            cur = [ln]
        elif cur is None:
            header.append(ln)
        elif ln.strip():
            cur.append(ln)
    if cur:
        chunks.append(cur)
    return "\n".join(header).rstrip(), ["\n".join(c).rstrip() for c in chunks]


def decl_name(st):
    words = st.split()
    return words[2] if words[0] == "noncomputable" else words[1]


def freeze_checks():
    out = {"inputs": {}, "vendor": {}}
    ok = True
    for rel, (blob, digest) in FROZEN.items():
        data = (UNIT / rel).read_bytes()
        b, d = git_blob(data), sha256(data).hexdigest()
        good = (b == blob and d == digest)
        out["inputs"][rel] = {"commit": COMMITS[rel], "blob": b, "sha256": d, "pass": good}
        ok = ok and good
    for rel, (blob, digest) in VENDORED.items():
        p = (ROOT / rel) if rel.startswith("verification/lean-mathlib") else (UNIT / rel)
        data = p.read_bytes()
        b = git_blob(data)
        good = (b == blob and sha256(data).hexdigest() == digest)
        out["vendor"][rel] = {"expected_blob": blob, "actual_blob": b, "pass": good}
        ok = ok and good
    lines = []
    for p in sorted(OIB.iterdir(), key=lambda q: q.name):
        if p.name in NEW_MODULES:
            continue
        lines.append(f"{p.name} {git_blob(p.read_bytes())}\n")
    others = sha256("".join(lines).encode("utf-8")).hexdigest()
    out["untouched_oibridge"] = {"modules": len(lines), "sha256": others,
                                 "pass": others == OIBRIDGE_OTHERS_SHA256}
    ok = ok and out["untouched_oibridge"]["pass"]
    out["ok"] = ok
    return out


def statement_checks():
    header, sts = pcs2_statements()
    lean = PC1_LEAN.read_text(encoding="utf-8")
    kern = {}
    require(len(sts) == 14, "PC-S2 fixes fourteen PC1Controls statements")
    hdr_ok = header in lean
    for st in sts:
        kern["PC1Controls." + decl_name(st)] = {
            "module": "PC1Controls", "statement_sha256": sha256(st.encode("utf-8")).hexdigest(),
            "verbatim_in_module": st in lean, "build_step": "pending", "axiom_check_step": "pending"}
    for name, digest in F21_STATEMENTS.items():
        kern["F2CoherenceControls." + name] = {
            "module": "F2CoherenceControls", "statement_sha256": digest,
            "verbatim_in_module": "by vendored blob fbf47504 (S2-2)",
            "build_step": "pending", "axiom_check_step": "pending"}
    for name in CITED:
        kern[name] = {"module": "cited at 5914c17c", "statement_sha256": None,
                      "verbatim_in_module": True, "build_step": "pending", "axiom_check_step": "pending"}
    ok = hdr_ok and all(v["verbatim_in_module"] is True for k, v in kern.items()
                        if k.startswith("PC1Controls."))
    return {"header_verbatim": hdr_ok, "pc1_count": len(sts), "f21_count": len(F21_STATEMENTS),
            "f21_combined_statement_digest (A★-1.3)": F21_COMBINED,
            "ok": ok}, kern


# ---------------------------------------------------------------- exact helpers for the new controls

class R3:
    """Exact element a + b*sqrt(3) of Q(sqrt 3)."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o): return R3(self.a + o.a, self.b + o.b)
    def __mul__(self, o): return R3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)
    def __eq__(self, o): return self.a == o.a and self.b == o.b
    def text(self): return f"{fr(self.a)}+{fr(self.b)}*sqrt(3)"


def mmg(X, Y, zero):
    n, m, k = len(X), len(Y[0]), len(Y)
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            acc = zero
            for t in range(k):
                acc = acc + X[i][t] * Y[t][j]
            row.append(acc)
        out.append(row)
    return out


def perm_matrix(perm):
    n = len(perm)
    return [[Fr(1) if perm[j] == i else Fr(0) for j in range(n)] for i in range(n)]


def compress_counts(perm, cells):
    """|C_i ∩ σ^{-1}(C_j)|: the baseline compression's numerators in the indicator basis."""
    return [[sum(1 for x in ci if perm[x] in cj) for cj in cells] for ci in cells]


def frac_sqrt(q):
    q = Fr(q)
    require(q >= 0, "sqrt of a nonnegative rational")

    def isq(n):
        r = isqrt(n)
        return r if r * r == n else None
    a, b = isq(q.numerator), isq(q.denominator)
    return None if a is None or b is None else Fr(a, b)


def gauge_conj(D, K):
    """D^dagger K D for a diagonal D given by its entries (Gaussian rationals)."""
    n = len(K)
    return [[D[i].conj() * K[i][j] * D[j] for j in range(n)] for i in range(n)]


def is_scaled_nonneg(K):
    """K = a * M with M entrywise nonnegative, for some complex a (2x2 exact test)."""
    nz = [e for row in K for e in row if e.norm2() != 0]
    if not nz:
        return True
    ref = nz[0]
    for row in K:
        for e in row:
            if e.norm2() == 0:
                continue
            q = e * ref.conj()                         # same direction as ref: real and positive
            if q.im != 0 or q.re <= 0:
                return False
    return True


def fixes_ones(K):
    s = [K[i][0] + K[i][1] for i in range(2)]
    return s[0] == s[1]


UNIMODULAR_GAUGES = [[G(1), G(1)], [G(1), G(0, 1)], [G(1), G(-1)], [G(1), G(0, -1)]]


def gauge_detector(gens, enabled=True):
    """Exact record of Gauge_N and Gauge_O for a 2x2 generating set (PC-1 §2).
    Gauge_N holds when some generator has a cycle ratio K01 K10 / (K00 K11) that is not a
    nonnegative real (a diagonal-gauge invariant); it fails when a listed gauge makes every
    generator a scalar times a nonnegative matrix. Gauge_O fails when a listed gauge makes every
    unitary generator fix the all-ones vector up to a scalar."""
    if not enabled:
        return {"Gauge_N": True, "Gauge_O": True, "method": "disabled (mutation M11)"}
    cyc_block = False
    for K in gens:
        d = K[0][0] * K[1][1]
        o = K[0][1] * K[1][0]
        if d.norm2() != 0:
            q = o * d.conj()
            if q.im != 0 or q.re < 0:
                cyc_block = True
    gn = None
    if cyc_block:
        gn = True
    else:
        for D in UNIMODULAR_GAUGES:
            if all(is_scaled_nonneg(gauge_conj(D, K)) for K in gens):
                gn = False
                break
    go = True
    for D in UNIMODULAR_GAUGES:
        if all(fixes_ones(gauge_conj(D, K)) for K in gens):
            go = False
            break
    return {"Gauge_N": gn, "Gauge_O": go, "method": "cycle invariant; gauges diag(1, i^k)"}


# ---------------------------------------------------------------- the new controls C11-C15

def c11a():
    rows = []
    models = [("S3 on Fin 3", 3, [(1, 0, 2), (1, 2, 0)], [[0], [1, 2]]),
              ("Spekkens S4 on Fin 4", 4, [(1, 0, 2, 3), (1, 2, 3, 0)], [[0, 1], [2, 3]])]
    for name, n, gens, cells in models:
        for g in gens:
            require(sorted(g) == list(range(n)), f"C11a {name} bijection")
            P = perm_matrix(g)
            require(all(sum(P[i][j] for i in range(n)) == 1 for j in range(n))
                    and all(e in (0, 1) for row in P for e in row), f"C11a {name} permutation matrix")
            cnt = compress_counts(g, cells)
            require(all(c >= 0 for row in cnt for c in row), f"C11a {name} compression nonnegative")
        a, b = perm_matrix(gens[0]), perm_matrix(gens[1])
        noncomm = mmg(a, b, Fr(0)) != mmg(b, a, Fr(0))
        require(noncomm, f"C11a {name} generators do not commute")
        rows.append({"model": name, "generators": [list(g) for g in gens], "cells": cells,
                     "permutation_matrices": True, "compressions_nonnegative": True,
                     "noncommuting": True})
    gd = gauge_detector([[[G(0), G(1)], [G(1), G(0)]], [[G(1), G(0)], [G(0), G(1)]]])
    require(gd["Gauge_N"] is False and gd["Gauge_O"] is False, "C11a identity gauge suffices")
    return {"models": rows, "gauge": gd, "class": "inside permClass; register compressions inside nonnegClass"}


def c11b():
    # the 3-cycle (0 1 2) on the sum-zero plane, basis e0-e1, e1-e2 (integer matrix A)
    A = [[Fr(0), Fr(-1)], [Fr(1), Fr(-1)]]
    A3 = mmg(A, mmg(A, A, Fr(0)), Fr(0))
    require(A3 == [[1, 0], [0, 1]] and A != [[1, 0], [0, 1]] and A[0][0] + A[1][1] == -1,
            "C11b 3-cycle on the sum-zero plane")
    # the same rotation in an orthonormal basis, over Q(sqrt 3)
    h = Fr(1, 2)
    Rm = [[R3(-h), R3(0, -h)], [R3(0, h), R3(-h)]]
    I3 = [[R3(1), R3(0)], [R3(0), R3(1)]]
    R3m = mmg(Rm, mmg(Rm, Rm, R3(0)), R3(0))
    RtR = mmg([[Rm[0][0], Rm[1][0]], [Rm[0][1], Rm[1][1]]], Rm, R3(0))
    tr = Rm[0][0] + Rm[1][1]
    nonmono = all(not (e == R3(0)) for row in Rm for e in row)
    require(R3m == I3 and not (Rm == I3) and tr == R3(-1) and RtR == I3 and nonmono,
            "C11b standard-representation rotation")
    # Fourier basis: characters of Z/3 are eigenvectors of the cyclic shift, eigenvalues omega^k
    w = Q3(Fr(-1, 2), Fr(1, 2))                      # omega = exp(2 pi i/3)
    one = Q3(1)
    pw = [one, w, w * w]
    require(w * w * w == one and not (w == one), "C11b omega")
    for k in (1, 2):
        v = [pw[(k * x) % 3] for x in range(3)]
        shifted = [v[(x + 1) % 3] for x in range(3)]
        require(all(shifted[x] == pw[k] * v[x] for x in range(3)), f"C11b character {k}")
    ratio = w * (w * w).inv()
    fourier_verified = ratio.b != 0
    require(fourier_verified, "C11b Fourier relative phase non-real")
    return {"exhibits": [
        {"exhibit": "3-cycle, standard representation, orthonormal basis (Q(sqrt 3))",
         "matrix": [[e.text() for e in row] for row in Rm], "checks": "R^3 = 1, R != 1, trace -1, orthogonal, non-monomial",
         "verified": False,
         "reason": "neither rot up to a scalar nor a relative phase in its named basis (inherited definition)"},
        {"exhibit": "diag(omega, omega^2), Fourier basis of Z/3 (Q(sqrt -3))",
         "diagonal": [w.text(), (w * w).text()], "ratio": ratio.text(), "verified": True}],
        "exhibits_verified": True}


def c12(enabled=True):
    D = [G(1), G(0, 1)]
    Dg = [[D[0], G(0)], [G(0), D[1]]]
    Dd = dag(Dg)
    gens = [mm(Dg, mm(P, Dd)) for P in (IDENT, SWAP)]
    gs = gens[1]
    require(gs == [[G(0), G(0, -1)], [G(0, 1), G(0)]], "C12 D swap D^dagger = [[0, -i], [i, 0]]")
    require(not is_scaled_nonneg(gs) and not fixes_ones(gs), "C12 neither nonnegative nor ones-fixing")
    back = [mm(Dd, mm(K, Dg)) for K in gens]
    require(back == [IDENT, SWAP], "C12 D^dagger maps the generators back to permutations")
    gd = gauge_detector(gens, enabled)
    return {"gauge": "D = diag(1, i)", "swap_image": [[e.text() for e in row] for row in gs],
            "detector": gd, "transport": "paper (PC-S2 S2-4)"}


def c13():
    n0, n1 = 4, 9
    perm = list(range(13))
    for a, b in ((0, 4), (1, 5), (2, 6), (3, 7)):
        perm[a], perm[b] = b, a
    cells = [list(range(4)), list(range(4, 13))]
    cnt = compress_counts(perm, cells)
    size = [n0, n1]
    K = []
    for i in range(2):
        row = []
        for j in range(2):
            s = frac_sqrt(Fr(size[i] * size[j]))
            require(s is not None, "C13 rational normalization")
            row.append(Fr(cnt[i][j]) / s)
        K.append(row)
    require(K == [[0, Fr(2, 3)], [Fr(2, 3), Fr(5, 9)]], "C13 K as fixed")
    a, b, c, d = K[0][0], K[0][1], K[1][0], K[1][1]
    require(a * d - b * c < 0, "C13 det K < 0")
    s = frac_sqrt((a - d) ** 2 + (b + c) ** 2)
    require(s is not None, "C13 polar normalization rational")
    U = [[(a - d) / s, (b + c) / s], [(b + c) / s, (d - a) / s]]
    require(U == [[Fr(-5, 13), Fr(12, 13)], [Fr(12, 13), Fr(5, 13)]], "C13 U as fixed")
    UtU = mmg([[U[0][0], U[1][0]], [U[0][1], U[1][1]]], U, Fr(0))
    require(UtU == [[1, 0], [0, 1]], "C13 U orthogonal")
    P = mmg([[U[0][0], U[1][0]], [U[0][1], U[1][1]]], K, Fr(0))
    psd = (P[0][1] == P[1][0] and P[0][0] >= 0 and P[1][1] >= 0
           and P[0][0] * P[1][1] - P[0][1] * P[1][0] >= 0)
    require(psd, "C13 U^T K symmetric positive semidefinite")
    return {"model": {"X": "Fin 13, uniform", "C0": cells[0], "C1": cells[1],
                      "sigma": "(0 4)(1 5)(2 6)(3 7)"},
            "K": [[fr(x) for x in row] for row in K], "U": [[fr(x) for x in row] for row in U],
            "UtU_identity": True, "UtK_symmetric_psd": True,
            "exhibit_listed": "U", "exhibit_verified": False,
            "reason": "neither rot up to a scalar nor a relative phase in its named basis"}


def c14(count_unsourced_orders=False):
    X, S = [0, 1, 2], [0, 2]
    T = {0: (1, 0, 2), 2: (1, 2, 0)}
    states = [(x, s) for x in X for s in S]
    F = {(x, s): (T[s][x], s) for (x, s) in states}
    require(sorted(F.values()) == sorted(states), "C14 F bijective")
    s_conserved = all(F[st][1] == st[1] for st in states)
    require(s_conserved, "C14 F conserves s")
    a, b = perm_matrix(T[0]), perm_matrix(T[2])
    require(mmg(a, b, Fr(0)) != mmg(b, a, Fr(0)), "C14 T0 T2 != T2 T0")
    claims_change = count_unsourced_orders
    flags = ["external_switch"] if s_conserved else []
    return {"bijective": True, "s_conserved": True, "noncommuting": True,
            "both_orders_counted_executed": claims_change, "screen_item_8": "fails (s conserved)",
            "screen_flags": flags}


def c15():
    gd = gauge_detector([ROT])
    cyc = (ROT[0][1] * ROT[1][0]).re / (ROT[0][0] * ROT[1][1]).re
    D = [G(1), G(0, 1)]
    Gr = gauge_conj(D, ROT)
    s = [Gr[i][0] + Gr[i][1] for i in range(2)]
    require(cyc == Fr(-16, 9), "C15 cycle ratio -16/9")
    require(s[0] == s[1] == G(Fr(3, 5), Fr(4, 5)), "C15 D^dagger rot D fixes ones (PC-F1)")
    require(gd["Gauge_N"] is True and gd["Gauge_O"] is False, "C15 gauge record")
    return {"cycle_ratio": fr(cyc), "gauged_ones_eigenvalue": s[0].text(), "detector": gd}


# ---------------------------------------------------------------- decision rule (frozen §6)

TOKENS = {"0": VOID_TOKEN, "1": GAP_TOKEN, "2": "COUNTEREXAMPLE (falsified)",
          "3a": "REPRESENTATION-ONLY", "3b": "REPRESENTATION-ONLY", "4": "L3-SUCCESS",
          "5": "L2-SUCCESS", "6a": "PARTIAL", "6b": "PARTIAL", "6c": "PARTIAL", "6d": "PARTIAL",
          "7": "L1-SUCCESS", "8": "L1-SUCCESS", "9": "COUNTEREXAMPLE (countertheory)",
          "10": "INCONCLUSIVE (undecided)"}


def l2_met(c):
    coh = c.get("coherence") or {}
    ip = c.get("ip") or {}
    fork = c.get("fork") or {}
    probes = c.get("probes") or {}
    ip_ok = ((ip.get("IP1_qualifies") is True and ip.get("IP1") == "decided")
             or ip.get("IP2") == "decided")
    return (c.get("L1") == "met" and c.get("gstar") is True and c.get("R") is True
            and c.get("Rdag") is True and c.get("Rdag_source") == "kernel" and c.get("P") is True
            and c.get("S") is True and c.get("N") is False and c.get("O") is False
            and c.get("Gauge_N") is True and c.get("Gauge_O") is True
            and coh.get("G4a") is True and coh.get("G4b") is True
            and coh.get("G4b_label") == "sourced" and coh.get("G4c") is True
            and not fork.get("L2_varies") and c.get("transplantable") is True
            and c.get("probes_run") is True and bool(probes)
            and all(not (v.get("R") or v.get("P") or v.get("gauge_robust_escape")) for v in probes.values())
            and ip_ok)


def decide_row(c):
    """Rows 2-10 of the frozen §6 for one record (a control or a synthetic candidate)."""
    grade = c.get("grade") or "AVAILABLE"
    probes = c.get("probes") or {}
    R, P1, P = c.get("R"), c.get("P1"), c.get("P")
    if any(v.get("R") or v.get("P") or v.get("gauge_robust_escape") for v in probes.values()):
        return TOKENS["2"], "2"
    if c.get("candidate"):
        coh = c.get("coherence") or {}
        if R is True and c.get("Rdag") is True and coh and (
                coh.get("G4a") is False or coh.get("G4c") is False
                or (coh.get("G4b_label") == "sourced" and coh.get("G4b") is False)):
            return TOKENS["2"], "2"
        if R is True and c.get("heldout") == "refuted":
            return TOKENS["2"], "2"
        if R is True and P1 is True and c.get("phase_heldout") == "refuted":
            return TOKENS["2"], "2"
        if (c.get("ip") or {}).get("refuted"):
            return TOKENS["2"], "2"
    if (R is True or P1 is True or P is True) and c.get("screen_flags"):
        return TOKENS["3a"], "3a"
    if c.get("L1") != "met" and R is False and P1 is False and c.get("exhibits_verified"):
        return TOKENS["3b"], "3b"
    if l2_met(c) and c.get("L3") is True:
        return TOKENS["4"] + "/" + grade, "4"
    if l2_met(c):
        return TOKENS["5"] + "/" + grade, "5"
    if c.get("L1") == "met":
        fork = c.get("fork") or {}
        ip = c.get("ip") or {}
        if fork.get("measure_dependent") and fork.get("L2_varies") and fork.get("R_or_P1_some_member"):
            return TOKENS["6a"], "6a"
        if c.get("phi_min") is True and P is not True:
            return TOKENS["6b"], "6b"
        if (R is True and P1 is False) or (P1 is True and R is False):
            return TOKENS["6c"], "6c"
        ip_ok = ((ip.get("IP1_qualifies") is True and ip.get("IP1") == "decided")
                 or ip.get("IP2") == "decided")
        coh = c.get("coherence") or {}
        if R is True and P is True and (
                not (c.get("Rdag") is True and c.get("Rdag_source") == "kernel") or c.get("S") is not True
                or coh.get("G4b_label") != "sourced" or not ip_ok
                or c.get("transplantable") is False or not c.get("probes_run")):
            return TOKENS["6d"], "6d"
        if R is False and P1 is False:
            return TOKENS["7"] + "/" + grade, "7"
        return TOKENS["8"] + "/" + grade, "8"
    if R is False and P1 is False and not c.get("exhibits_verified"):
        return TOKENS["9"], "9"
    return TOKENS["10"], "10"


def kernel_of(res):
    return res["statements"] if "statements" in res else res.get("kernel", {})


def has_float(x):
    if isinstance(x, float):
        return True
    if isinstance(x, dict):
        return any(has_float(v) for v in x.values())
    if isinstance(x, list):
        return any(has_float(v) for v in x)
    return False


def decide_file(res):
    """The frozen §6 on a results file: (token or None while kernel steps pend, row, void reasons)."""
    void = []
    if not all(v.get("pass") for v in res.get("controls", {}).values()):
        void.append("0(i)")
    elif not all(v.get("caught") for v in res.get("mutations", {}).values()):
        void.append("0(i)")
    elif not all(res.get("selftest_ok", {}).values()):
        void.append("0(i)")
    if not res.get("freeze", {}).get("ok", False):
        void.append("0(ii)")
    if res.get("fork_violation"):
        void.append("0(iii)")
    if has_float(res):
        void.append("0(iv)")
    concl = [(v["build_step"], v["axiom_check_step"]) for v in kernel_of(res).values()]
    if any("failure" in c for c in concl):
        void.append("0(v)")
    if res.get("stage1", {}).get("forbidden_precomputation"):
        void.append("0(vi)")
    if any(not p.get("coupling_is_transplanted_C") for p in res.get("probe_runs", {}).values()):
        void.append("0(vii)")
    if void:
        return TOKENS["0"], "0", void
    if any(c != ("success", "success") for c in concl):
        return None, None, []
    cand = res.get("stage1", {}).get("candidate")
    if cand is None:
        return TOKENS["1"], "1", []
    tok, row = decide_row(cand)
    return tok, row, []


# ---------------------------------------------------------------- the unit token (S2-1)

FINDING_STATEMENT = ("No admissible candidate among the 25 screened (F2-1's 13 rules and Q1–Q12); the "
                     "obstruction is G★ item 3 for native couplings: A★2 premise (ii) is broken by no "
                     "native source.")
FINDING_SCOPE = ("PC★ §PC★4: couplings whose joint process is a classical measurable bijection with "
                 "function-valued records; the sources at 5914c17c and the named branches; not a no-go.")
EXCEPTION = "PR #1022 comment 6547077354"


def unit_token(res):
    st = res.get("stage1", {})
    disp_ok = (st.get("source", {}).get("sha256") == DISPOSITION_SHA256)
    flag = st.get("forbidden_precomputation")
    void = []
    if flag is True and disp_ok:
        void.append("0(vi)")
    other = []
    if (not all(v.get("pass") for v in res.get("controls", {}).values())
            or not all(v.get("caught") for v in res.get("mutations", {}).values())
            or not all(res.get("selftest_ok", {}).values())):
        other.append("0(i)")
    if not res.get("freeze", {}).get("ok", False) or not disp_ok or flag is not True:
        other.append("0(ii)")
    if has_float(res):
        other.append("0(iv)")
    concl = [(v["build_step"], v["axiom_check_step"]) for v in kernel_of(res).values()]
    if any("failure" in c for c in concl):
        other.append("0(v)")
    void += other
    pending = any(c != ("success", "success") for c in concl) or not res.get("review")
    if other:
        status = "withheld: " + ", ".join(other)
    elif pending:
        status = "pending exact-head review"
    else:
        status = "carried under exception"
    finding = {"statement": FINDING_STATEMENT, "scope": FINDING_SCOPE, "exception": EXCEPTION,
               "status": status, "review": res.get("review")}
    return {"token": VOID_TOKEN, "void_reasons": void, "scientific_finding": finding}


def verdict_text(token):
    return f"PC-1 stage 2: strict token {token}."


def text_matches_token(text, token):
    levels = ["L3-SUCCESS", "L2-SUCCESS", "L1-SUCCESS"]
    named = [lv for lv in levels if lv in text]
    return all(lv in (token or "") for lv in named)


# ---------------------------------------------------------------- control records (S2-4; C13 per W1)

EXPECTED_ROWS = {"C1": "9", "C2": "9", "C3": "3a", "C4": "9", "C6": "3b", "C7": "3a", "C8": "3a",
                 "C10": "9", "C11a": "9", "C11b": "3b", "C12": "9", "C13": "9", "C14": "9", "C15": "3a"}


def control_records(nx):
    k = "kernel"
    recs = {
        "C1": {"R": False, "P1": False, "P": False, "N": True, "O": True, "L1": "not met", "screen_flags": [],
               "exhibits_verified": False,
               "sources": {"R": k + ":falsifierUnavailable_of_nonnegBounded+nonnegClass_nonnegBounded",
                           "P1": k + ":not_p1_of_nonnegBounded", "containment": "exact"}},
        "C2": {"R": False, "P1": False, "P": False, "N": True, "O": True, "L1": "not met", "screen_flags": [],
               "exhibits_verified": False,
               "sources": {"R": k + ":permTheory_falsifierUnavailable", "P1": k + ":permTheory_not_p1",
                           "containment": "exact"}},
        "C3": {"R": False, "P1": True, "P": True, "L1": "not met",
               "screen_flags": F21.screen(["permutation"] + (["nonreal_diagonal_unitary"]
                                                            if nx["C3"]["phaseOperator_nonreal_ratio"] else [])),
               "exhibits_verified": False,
               "sources": {"R": k + ":substratumTheory_falsifierUnavailable", "P": k + ":substratumTheory_derivedOI"}},
        "C4": {"R": False, "P1": False, "P": False, "O": True, "L1": "not met", "screen_flags": [],
               "exhibits_verified": False,
               "sources": {"R": k + ":onesTheory_falsifierUnavailable", "P1": k + ":not_p1_of_onesBounded"}},
        "C6": {"R": False, "P1": False, "P": False, "N": True, "O": True, "L1": "not met", "screen_flags": [],
               "exhibits_verified": (nx["C6"]["odometer"]["relative_phase_verified"]
                                     and nx["C6"]["wave"]["relative_phase_verified"]),
               "sources": {"R": k + ":as C1", "P1": k + ":as C1"}},
        "C7": {"R": True, "Rdag": True, "Rdag_source": k, "P1": True, "P": True, "N": False, "O": False,
               "L1": "not met", "screen_flags": F21.screen(["fullClass"]), "exhibits_verified": False,
               "sources": {"R": k + ":fullTheory_rot", "P": k + ":fullTheory_phases"}},
        "C8": {"R": True, "P1": False, "P": False, "N": False, "O": False, "L1": "not met",
               "screen_flags": F21.screen(["rot"]), "exhibits_verified": False,
               "sources": {"R": k + ":realTheory_rot", "P1": k + ":realSubclass_not_p1",
                           "P": k + ":realTheory_not_phases"}},
        "C10": {"R": False, "P1": False, "P": False, "N": True, "O": True, "L1": "not met", "screen_flags": [],
                "exhibits_verified": False,
                "sources": {"R": k + ":as C1", "containment": "paper (hemisphere indicators)"}},
        "C11a": {"R": False, "P1": False, "P": False, "N": True, "O": True,
                 "Gauge_N": nx["C11a"]["gauge"]["Gauge_N"], "Gauge_O": nx["C11a"]["gauge"]["Gauge_O"],
                 "L1": "not met", "screen_flags": [], "exhibits_verified": False,
                 "sources": {"R": k + ":falsifierUnavailable_of_nonnegBounded", "P1": k + ":not_p1_of_nonnegBounded",
                             "O": k + ":permTheory_onesBounded_all", "containment": "exact"}},
        "C11b": {"R": False, "P1": False, "P": False, "N": True, "O": True, "L1": "not met", "screen_flags": [],
                 "exhibits_verified": nx["C11b"]["exhibits_verified"], "sources": {"R": k + ":as C11a"}},
        "C12": {"R": False, "P1": False, "P": False, "Gauge_N": nx["C12"]["detector"]["Gauge_N"],
                "Gauge_O": nx["C12"]["detector"]["Gauge_O"], "L1": "not met", "screen_flags": [],
                "exhibits_verified": False, "obstruction": "Gauge_N",
                "sources": {"R": k + ":permTheory_not_gauged_rot+paper transport",
                            "P1": k + ":permTheory_not_p1+paper transport"}},
        "C13": {"R": False, "R_source": "paper:PC-S2-C13 §3", "P1": False,
                "P1_source": "kernel:realSubclass_not_p1", "P": False, "exhibits_verified": False,
                "screen_flags": ["no_executing_process"], "L1": "not met"},
        "C14": {"R": False, "P1": False, "P": False, "N": True, "O": True, "L1": "not met",
                "screen_flags": nx["C14"]["screen_flags"], "exhibits_verified": False,
                "sources": {"R": k + ":as C11a", "containment": "exact"}},
        "C15": {"R": True, "P1": False, "P": False, "Gauge_N": nx["C15"]["detector"]["Gauge_N"],
                "Gauge_O": nx["C15"]["detector"]["Gauge_O"], "L1": "not met", "screen_flags": F21.screen(["rot"]),
                "exhibits_verified": False,
                "sources": {"R": k + ":falsifier_available_of_mem", "P": k + ":realSubclass_not_phases+rot_mem_realClass",
                            "Gauge_N": k + ":scaled_rot_not_gauge_nonneg",
                            "Gauge_O": k + ":gauged_rot_mem_onesClass"}},
    }
    return recs


# ---------------------------------------------------------------- mutations (M1-M17)

def cand_base():
    return {"candidate": True, "L1": "met", "gstar": True, "R": True, "Rdag": True, "Rdag_source": "kernel",
            "P1": True, "P": True, "S": True, "N": False, "O": False, "Gauge_N": True, "Gauge_O": True,
            "screen_flags": [], "exhibits_verified": False, "phi_min": True,
            "coherence": {"G4a": True, "G4b": True, "G4b_label": "sourced", "G4c": True},
            "heldout": "consistent", "phase_heldout": "consistent",
            "ip": {"IP1_qualifies": True, "IP1": "decided", "IP2": "decided", "refuted": False},
            "fork": {"measure_dependent": False, "L2_varies": False, "R_or_P1_some_member": True},
            "transplantable": True, "probes_run": True,
            "probes": {p: {"R": False, "P": False, "gauge_robust_escape": False}
                       for p in ("C1", "C2", "C10", "C11", "C14")}, "grade": "AVAILABLE", "L3": False}


def records_complete(branches):
    """Rec: every branch kept, failures included, masses unrenormalized and summing to 1."""
    kinds = {b["kind"] for b in branches}
    return ("failure" in kinds and "success" in kinds
            and sum(Fr(b["mass"]) for b in branches) == 1 and all(Fr(b["mass"]) > 0 for b in branches))


def fork_ok(fork):
    if fork.get("mu_choice_reason") == "gives L2":
        return False
    if fork.get("branch") == "invariance" and fork.get("class_infinite") and fork.get("proof") == "sample":
        return False
    return True


def mutations(nx, decider):
    m = {}
    coh, dep = F21.g4(SWAP, dag(SWAP))
    m["M1"] = {"what": "rot replaced by the swap", "returns": [fr(coh), fr(dep)], "caught": coh == dep == 1}
    flags = F21.screen(["permutation", "nonreal_diagonal_unitary", "phaseGate"])
    m["M2"] = {"what": "phaseGate added to the C3 generator set", "flags": flags, "caught": "phaseGate" in flags}
    q = 8
    w = [Fr(x + 1, 36) for x in range(q)]
    m["M3"] = {"what": "non-invariant measure on the depth-3 odometer stage",
               "caught": not F21.haar_invariant(w, lambda x: x + 1, q)}
    bad = green_file()
    bad["extra"] = 0.25
    m["M4"] = {"what": "a float in a decision path", "caught": decider(bad)[1] == "0"}
    c = {"candidate": True, "L1": "met", "R": False, "P1": False, "P": False, "N": True, "O": True,
         "screen_flags": [], "exhibits_verified": False, "probes": {}}
    row = decide_row(c)[1]
    m["M5"] = {"what": "a C2 model in place of the candidate", "row": row, "caught": row not in ("4", "5")}
    m["M6"] = {"what": "an inserted dephasing relabelled sourced",
               "caught": not F21.g4b_label_ok("inserted", "sourced")}
    p1 = {"rot": F21.freq_p1_rational(ROT), "rot2": F21.freq_p1_rational(mm(ROT, ROT))}
    c = cand_base()
    c["heldout"] = "refuted" if any(p1[x] != F21.EXPECTED_FREQ[x] for x in p1) else "consistent"
    row = decide_row(c)[1]
    m["M7"] = {"what": "amplitudes encoded as measures (p = 1)",
               "frequencies": {x: fr(v) for x, v in p1.items()}, "row": row, "caught": row == "2"}
    c = cand_base()
    c["Rdag_source"] = "assumed"
    row = decide_row(c)[1]
    m["M8"] = {"what": "R-dagger assumed instead of proved", "row": row, "caught": row not in ("4", "5")}

    def hardcoded(res):
        return "L2-SUCCESS/AVAILABLE", "5", []

    m["M9"] = {"what": "a verdict template hardcoding success",
               "caught": not all(run_selftest(hardcoded).values())}
    c = cand_base()
    c["screen_flags"] = F21.screen(["rot"])
    probe = cand_base()
    probe["probes"]["C2"] = {"R": True, "P": False, "gauge_robust_escape": False}
    rows = [decide_row(c)[1], decide_row(probe)[1]]
    m["M10"] = {"what": "constant rule := rot applied to a C2 model", "rows": rows,
                "caught": rows[0] in ("2", "3a") and rows[1] == "2"}
    off = c12(enabled=False)["detector"]
    m["M11"] = {"what": "gauge check disabled on C12", "Gauge_N": off["Gauge_N"],
                "caught": off["Gauge_N"] != nx["C12"]["detector"]["Gauge_N"]}
    rec = {"R": False, "P1": False, "P": False, "L1": "not met", "exhibits_verified": True,
           "screen_flags": ["declared_basis"]}
    row = decide_row(rec)[1]
    m["M12"] = {"what": "C11b standard-representation basis declared as the readout",
                "flags": rec["screen_flags"], "row": row, "caught": "declared_basis" in rec["screen_flags"]
                and row in ("3a", "3b")}
    mut = c14(count_unsourced_orders=True)
    m["M13"] = {"what": "C14 with both orders counted as executed without a sourced s change",
                "flags": mut["screen_flags"], "caught": "external_switch" in mut["screen_flags"]}
    good = [{"kind": "success", "mass": "1/2"}, {"kind": "failure", "mass": "1/4"}, {"kind": "rejected", "mass": "1/4"}]
    dropped = [{"kind": "success", "mass": "2/3"}, {"kind": "rejected", "mass": "1/3"}]
    m["M14"] = {"what": "failure branches dropped and success renormalized",
                "caught": records_complete(good) and not records_complete(dropped)}
    r = green_file(cand_base())
    r["fork_violation"] = not fork_ok({"branch": "selection", "mu_choice_reason": "gives L2"})
    m["M15"] = {"what": "mu chosen as the member giving L2", "row": decider(r)[1],
                "caught": decider(r)[1] == "0" and "0(iii)" in decider(r)[2]}
    c = cand_base()
    c["R"], c["P1"], c["P"], c["phi_min"] = False, False, False, False
    tok, row = decide_row(c)
    m["M16"] = {"what": "a row-7 file whose verdict text says L2", "row": row,
                "caught": row == "7" and not text_matches_token("L2-SUCCESS reached", tok)
                and text_matches_token(verdict_text(tok), tok)}
    r = green_file(cand_base())
    r["fork_violation"] = not fork_ok({"branch": "invariance", "class_infinite": True, "proof": "sample"})
    m["M17"] = {"what": "invariance claimed from a two-member sample of an infinite class",
                "caught": decider(r)[1] == "0" and "0(iii)" in decider(r)[2]}
    return m


# ---------------------------------------------------------------- self-test (§6 rows; U1-U5)

def green_file(candidate=None):
    return {"controls": {"C1": {"pass": True}}, "mutations": {"M1": {"caught": True}},
            "selftest_ok": {"x": True}, "freeze": {"ok": True}, "fork_violation": False,
            "kernel": {"k": {"build_step": "success", "axiom_check_step": "success"}},
            "stage1": {"candidate": candidate, "forbidden_precomputation": False}, "probe_runs": {}}


def selftest_cases():
    cases = []

    def add(name, res, row, tok=None):
        cases.append((name, res, row, tok))

    r = green_file(); r["controls"]["C1"]["pass"] = False; add("0(i)", r, "0")
    r = green_file(); r["freeze"]["ok"] = False; add("0(ii)", r, "0")
    r = green_file(); r["fork_violation"] = True; add("0(iii)", r, "0")
    r = green_file(); r["extra"] = 0.5; add("0(iv)", r, "0")
    r = green_file(); r["kernel"]["k"]["build_step"] = "failure"; add("0(v)", r, "0")
    r = green_file(); r["stage1"]["forbidden_precomputation"] = True; add("0(vi)", r, "0")
    r = green_file(); r["probe_runs"] = {"C1": {"coupling_is_transplanted_C": False}}; add("0(vii)", r, "0")
    add("1", green_file(), "1", GAP_TOKEN)
    r = green_file(); r["kernel"]["k"]["axiom_check_step"] = "pending"; add("pending", r, None)
    c = cand_base(); c["probes"]["C11"] = {"R": True}; add("2 probe R", green_file(c), "2")
    c = cand_base(); c["probes"]["C14"] = {"gauge_robust_escape": True}; add("2 probe gauge", green_file(c), "2")
    c = cand_base(); c["coherence"]["G4a"] = False; add("2 coherence", green_file(c), "2")
    c = cand_base(); c["heldout"] = "refuted"; add("2 held-out", green_file(c), "2")
    c = cand_base(); c["phase_heldout"] = "refuted"; add("2 phase hold-out", green_file(c), "2")
    c = cand_base(); c["ip"]["refuted"] = True; add("2 prediction", green_file(c), "2")
    c = cand_base(); c["screen_flags"] = ["no_executing_process"]; add("3(a)", green_file(c), "3a")
    c = {"L1": "not met", "R": False, "P1": False, "exhibits_verified": True}; add("3(b)", green_file(c), "3b")
    c = cand_base(); c["L3"] = True; add("4 AVAILABLE", green_file(c), "4", "L3-SUCCESS/AVAILABLE")
    c = cand_base(); c["L3"] = True; c["grade"] = "DERIVED"; add("4 DERIVED", green_file(c), "4", "L3-SUCCESS/DERIVED")
    add("5 AVAILABLE", green_file(cand_base()), "5", "L2-SUCCESS/AVAILABLE")
    c = cand_base(); c["grade"] = "DERIVED"; add("5 DERIVED", green_file(c), "5", "L2-SUCCESS/DERIVED")
    c = cand_base(); c["fork"] = {"measure_dependent": True, "L2_varies": True, "R_or_P1_some_member": True}
    add("6(a)", green_file(c), "6a")
    c = cand_base(); c["P"] = None; add("6(b) Phi_min without P", green_file(c), "6b")
    c = cand_base(); c["P1"], c["P"], c["phi_min"] = False, False, False; add("6(c) R, not P1", green_file(c), "6c")
    c = cand_base(); c["R"], c["P"], c["phi_min"] = False, False, False; add("6(c) P1, not R", green_file(c), "6c")
    c = cand_base(); c["Rdag"] = None; add("6(d) R-dagger missing", green_file(c), "6d")
    c = cand_base(); c["transplantable"] = False; c["probes_run"] = False; c["probes"] = {}
    add("6(d) not transplantable", green_file(c), "6d")
    c = cand_base(); c["ip"] = {"IP1_qualifies": False, "IP1": "decided", "IP2": "undecided", "refuted": False}
    add("6(d) Pi_C = Z/4, IP-2 undecided", green_file(c), "6d")
    c = cand_base(); c["R"], c["P1"], c["P"], c["phi_min"] = False, False, False, False
    add("7", green_file(c), "7", "L1-SUCCESS/AVAILABLE")
    c = cand_base(); c["R"], c["P1"], c["P"], c["phi_min"] = False, False, False, False
    c["exhibits_verified"] = True; add("7 with exhibit, never 3(b)", green_file(c), "7")
    c = cand_base(); c["R"], c["P1"], c["P"], c["phi_min"] = False, False, False, False
    c["fork"] = {"measure_dependent": True, "L2_varies": True, "R_or_P1_some_member": False}
    add("7 S varying, never 6(a)", green_file(c), "7")
    c = cand_base(); c["R"], c["P1"], c["P"], c["phi_min"] = False, None, None, False
    add("8 R refuted, P1 undecided", green_file(c), "8", "L1-SUCCESS/AVAILABLE")
    c = cand_base(); c["R"], c["P1"], c["P"], c["phi_min"] = None, None, None, False
    add("8 both undecided", green_file(c), "8")
    c = {"L1": "not met", "R": False, "P1": False, "exhibits_verified": False}; add("9", green_file(c), "9")
    c = {"L1": "not met", "R": None, "P1": None}; add("10", green_file(c), "10")
    c = cand_base(); c["P"] = None; add("Phi_min without P, never 5", green_file(c), "6b")
    c = cand_base(); c["P1"], c["P"], c["phi_min"], c["Gauge_O"] = False, False, False, False
    add("C15 shape, never 7", green_file(c), "6c")
    return cases


def run_selftest(decider):
    out = {}
    for name, res, row, tok in selftest_cases():
        got_tok, got, _ = decider(res)
        ok = got == row
        if tok is not None:
            ok = ok and got_tok == tok
        out[name] = ok
    return out


def unit_cases():
    def base():
        return {"controls": {"C1": {"pass": True}}, "mutations": {"M1": {"caught": True}},
                "selftest_ok": {"x": True}, "freeze": {"ok": True},
                "kernel": {"k": {"build_step": "success", "axiom_check_step": "success"}},
                "stage1": {"forbidden_precomputation": True, "source": {"sha256": DISPOSITION_SHA256}},
                "review": {"reviewer": "r", "time": "t", "head": "h", "quote": "q"}}
    cases = []
    cases.append(("U1", base(), ["0(vi)"], "carried under exception"))
    r = base(); r["controls"]["C1"]["pass"] = False; cases.append(("U2", r, ["0(vi)", "0(i)"], "withheld: 0(i)"))
    r = base(); r["kernel"]["k"]["build_step"] = "failure"; cases.append(("U3", r, ["0(vi)", "0(v)"], "withheld: 0(v)"))
    r = base(); r["review"] = None; cases.append(("U4", r, ["0(vi)"], "pending exact-head review"))
    r = base(); r["stage1"]["forbidden_precomputation"] = False; cases.append(("U5", r, ["0(ii)"], "withheld: 0(ii)"))
    return cases


def run_unit_selftest(fn):
    out = {}
    for name, res, reasons, status in unit_cases():
        u = fn(res)
        blob = json.dumps(u, ensure_ascii=False)
        out[name] = (u["token"] == VOID_TOKEN and u["void_reasons"] == reasons
                     and u["scientific_finding"]["status"] == status and GAP_TOKEN not in blob)
    return out


# ---------------------------------------------------------------- assembly

def guarded(fn, *a):
    try:
        return fn(*a), None
    except RuntimeError as e:
        return None, str(e)


def build():
    fz = freeze_checks()
    stc, kern = statement_checks()
    nx, errors = {}, {}
    for cid, fn in (("C1", F21.c1), ("C2", F21.c2), ("C6o", F21.c6_odometer), ("C6w", F21.c6_wave),
                    ("C7", F21.c7), ("C9", F21.c9), ("C10", F21.c10), ("C11a", c11a), ("C11b", c11b),
                    ("C12", c12), ("C13", c13), ("C14", c14), ("C15", c15)):
        val, err = guarded(fn)
        nx[cid] = val
        if err:
            errors[cid] = err
    nx["C3"] = {"phaseOperator": "diag(i, 1)",
                "phaseOperator_nonreal_ratio": F21.nonreal_ratio(PHASE[0][0], PHASE[1][1])}
    nx["C6"] = {"odometer": nx.pop("C6o") or {"relative_phase_verified": False},
                "wave": nx.pop("C6w") or {"relative_phase_verified": False}}
    for cid in ("C11a", "C11b", "C12", "C14", "C15"):
        if nx[cid] is None:
            nx[cid] = {"gauge": {"Gauge_N": None, "Gauge_O": None}, "detector": {"Gauge_N": None, "Gauge_O": None},
                       "exhibits_verified": False, "screen_flags": []}
    recs = control_records(nx)
    controls = {}
    for cid, rec in recs.items():
        tok, row = decide_row(rec)
        ok = row == EXPECTED_ROWS[cid] and cid not in errors
        if cid == "C6":
            ok = ok and "C6o" not in errors and "C6w" not in errors
        entry = {"record": rec, "expected_row": EXPECTED_ROWS[cid], "row": row, "token": tok, "pass": ok}
        if cid in errors:
            entry["error"] = errors[cid]
        if cid == "C13":
            entry["reference_source"] = "amendments/PC-S2-C13.md"
            entry["exhibit_listed"] = "U"
            entry["exhibit_verified"] = False
            entry["reason"] = "neither rot up to a scalar nor a relative phase in its named basis"
        if cid == "C12":
            ok2 = rec["Gauge_N"] is False
            entry["gauge_reference"] = {"Gauge_N": "fails (detector finds D^dagger)", "pass": ok2}
            entry["pass"] = entry["pass"] and ok2
        if cid == "C15":
            ok2 = rec["Gauge_N"] is True and rec["Gauge_O"] is False
            entry["gauge_reference"] = {"Gauge_N": "holds", "Gauge_O": "fails", "pass": ok2}
            entry["pass"] = entry["pass"] and ok2
        controls[cid] = entry
    c5 = not any(r.get("R") is True and (r.get("N") is True or r.get("O") is True) for r in recs.values())
    controls["C5"] = {"expected_row": None, "row": None, "pass": c5,
                      "reference": "no record with R and N, or R and O; obstruction lemmas built in CI"}
    c9ok = "C9" not in errors
    controls["C9"] = {"expected_row": None, "row": None, "pass": c9ok, "values": nx["C9"],
                      **({"error": errors["C9"]} if not c9ok else {})}
    g4d = (nx["C2"] is not None and all(x["return"] == ["1", "1"] for x in nx["C2"]["models"])
           and nx["C10"] is not None and nx["C10"]["G4a"] == "1" and nx["C10"]["G4b"] == "337/625")
    controls["C2"]["G4d"] = g4d
    controls["C2"]["pass"] = controls["C2"]["pass"] and g4d
    c7ok = nx["C7"] is not None and nx["C7"]["G4a"] == "1" and nx["C7"]["G4b"] == "337/625"
    controls["C7"]["pass"] = controls["C7"]["pass"] and c7ok

    muts = mutations(nx, decide_file)
    st = run_selftest(decide_file)
    ut = run_unit_selftest(unit_token)
    exact = {k: v for k, v in nx.items()}

    res = {
        "schema": "pc1-stage2-results/1",
        "inputs": fz["inputs"],
        "vendor": fz["vendor"],
        "untouched_oibridge": fz["untouched_oibridge"],
        "stage1": {"candidate": None, "forbidden_precomputation": True,
                   "source": {"path": "amendments/PC-star-disposition.md",
                              "sha256": fz["inputs"]["amendments/PC-star-disposition.md"]["sha256"]},
                   "owner_decision": EXCEPTION},
        "statements_check": stc,
        "statements": kern,
        "exact": exact,
        "controls": controls,
        "probes": None, "probes_reason": "no candidate frozen (PC★)",
        "mutations": muts,
        "selftest": {"decide_row": st, "unit_token": ut},
        "selftest_ok": {**{"decide_row:" + k: v for k, v in st.items()},
                        **{"unit_token:" + k: v for k, v in ut.items()}},
        "freeze": {"ok": fz["ok"] and stc["ok"]},
        "review": None,
        "run": {"script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
                "head": None, "note": "exact-head record in kernel-steps.json and RESULT.md"},
    }
    u = unit_token(res)
    res["token"] = u["token"]
    res["void_reasons"] = u["void_reasons"]
    res["scientific_finding"] = u["scientific_finding"]
    res["verdict_status"] = "awaiting CI step conclusions"
    res["verdict_text"] = verdict_text(res["token"])
    require(GAP_TOKEN not in json.dumps({k: res[k] for k in ("token", "scientific_finding", "verdict_text")},
                                        ensure_ascii=False), "the gap token never appears in the unit result")
    return res


def dump(obj):
    return (json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def main(argv):
    res = build()
    data = dump(res)
    if "--kernel" in argv:
        k = json.loads(Path(argv[argv.index("--kernel") + 1]).read_text(encoding="utf-8"))
        for v in res["statements"].values():
            v["build_step"], v["axiom_check_step"] = k["build_step"], k["axiom_check_step"]
        if "--review" in argv:
            res["review"] = json.loads(Path(argv[argv.index("--review") + 1]).read_text(encoding="utf-8"))
        u = unit_token(res)
        out = {"head_sha": k.get("head_sha"), "run_url": k.get("run_url"),
               "build_step": k["build_step"], "axiom_check_step": k["axiom_check_step"],
               "token": u["token"], "void_reasons": u["void_reasons"],
               "scientific_finding": u["scientific_finding"], "verdict_text": verdict_text(u["token"])}
        sys.stdout.buffer.write(dump(out))
        return 0
    if "--write" in argv:
        require(not RESULTS.exists(), "results.json exists; --write is for the first execution only")
        RESULTS.write_bytes(data)
        sys.stdout.write("wrote results.json\n")
        return 0
    require(RESULTS.exists(), "results.json missing")
    require(RESULTS.read_bytes() == data, "results differ from the committed results.json")
    fails = [c for c, v in res["controls"].items() if not v["pass"]]
    fails += [m for m, v in res["mutations"].items() if not v["caught"]]
    fails += [s for s, ok in res["selftest_ok"].items() if not ok]
    sys.stdout.write(f"PC-1 stage 2: token {res['token']}, void_reasons {res['void_reasons']}; "
                     f"scientific_finding {res['scientific_finding']['status']}; "
                     f"failures: {fails if fails else 'none'}; freeze ok: {res['freeze']['ok']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
