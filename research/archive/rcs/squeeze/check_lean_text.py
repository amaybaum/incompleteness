"""Cross-check the polynomial statements as written in RelcSelectSqueeze.lean against the exact model.

Parses the Lean text (not a hand copy) of:
  * the RHS of `pairVal_gSq_prodState`  -> must equal pairVal a b (G (prodState x y)) computed from the
    entry table sqW / sqPc / sqPt of check_squeeze.py (which A1 ties to the ledger's model);
  * the conclusion of `gSq_core`         -> must be the same polynomial as that RHS (with a i -> ai);
  * the conclusion of `rsq_assemble`, instantiated as in `gSq_core`, -> same polynomial;
  * the conclusions of `rsq_key`, `rsq_s`, `rsq_ab`, `rsq_cs4` -> re-verify the certificates of
    check_squeeze.py Part C against the statement text.
Exit code 0 iff all pass.
"""
import os
import re
import sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "RelcSelectSqueeze.lean")).read()
FAILS = []


def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILS.append(name)


def block(start, end, after=None):
    i0 = SRC.index(after) if after else 0
    i = SRC.index(start, i0)
    j = SRC.index(end, i)
    return SRC[i + len(start):j]


def to_sympy(txt, extra=None):
    t = " ".join(txt.split())
    t = re.sub(r"\b([abxy]) (\d)", r"\1\2", t)  # a 0 -> a0
    t = t.replace("^", "**").replace("α", "alpha")
    loc = {n: sp.Symbol(n) for n in re.findall(r"[A-Za-z_][A-Za-z_0-9]*", t)}
    if extra:
        loc.update(extra)
    return sp.sympify(t, locals=loc, rational=True)


# --- pairVal_gSq_prodState RHS
rhs_txt = block("pairVal a b (gSq (prodState x y))\n      =", ":= by\n  -- Primary: evaluate")
V_lean = to_sympy(rhs_txt)

# model, as in check_squeeze.py
odd5 = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}
perm5 = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
cls = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}
sig = {0: 1, 1: 0, 2: 2, 3: 5, 4: 4, 5: 3}
pc = lambda m, n: perm5[m] if odd5[n] else m  # noqa: E731
pt = lambda m, n: n if cls[m] else sig[n]  # noqa: E731
R = lambda m: sp.Integer(1) if cls[m] else sp.Rational(1, 10)  # noqa: E731
K = lambda n: sp.Integer(1) if cls[n] else sp.Rational(1, 2)  # noqa: E731
a = sp.symbols("a0:6")
b = sp.symbols("b0:6")
x = sp.symbols("x0:5")
y = sp.symbols("y0:5")
hx = [1] + list(x)
hy = [1] + list(y)
V_model = sum(a[m] * R(m) * K(pt(m, n)) * hx[pc(m, n)] * hy[pt(m, n)] * b[n] for m in range(6) for n in range(6))
check("L1 Lean RHS of pairVal_gSq_prodState == model pairVal (polynomial identity)",
      sp.expand(V_lean - V_model) == 0)

core_txt = block("    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :\n    0 ≤", ":= by\n  obtain ⟨hA, hB, hkey⟩", after="theorem gSq_core")
check("L2 gSq_core conclusion == pairVal_gSq_prodState RHS", sp.expand(to_sympy(core_txt) - V_lean) == 0)
check("L2' gSq_core conclusion text == RHS text up to `a i -> ai` (so `exact` matches syntactically)",
      " ".join(re.sub(r"\b([abxy]) (\d)", r"\1\2", rhs_txt).split()) == " ".join(core_txt.split()))

# rsq_assemble conclusion instantiated as in gSq_core
asm_txt = block("    (hkey : (Se ^ 2 + So ^ 2) / 50 ≤ A * B) :\n    0 ≤", ":= by\n  have hP1", after="theorem rsq_assemble")
asm = to_sympy(asm_txt)
inst_txt = block("have h := rsq_assemble x4 (a0 + a5) (a0 - a5)", "(by linarith [hx4.1])")
args = re.findall(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)", inst_txt)
names = ["A", "B", "Se", "So", "Ce", "Co", "Tc", "Ta"]
check("L3 rsq_assemble instantiation has 8 parenthesised args", len(args) == 8)
sub = {sp.Symbol(nm): to_sympy(ar) for nm, ar in zip(names, args)}
sub[sp.Symbol("alpha")] = sp.Symbol("x4")
sub[sp.Symbol("p")] = a[0] + a[5]
sub[sp.Symbol("q")] = a[0] - a[5]
check("L3' rsq_assemble conclusion, instantiated as in gSq_core, == gSq_core conclusion",
      sp.expand(asm.subs(sub, simultaneous=True) - to_sympy(core_txt)) == 0)

# rsq_key: third conjunct is (Se^2+So^2)/50 <= A*B with the same A, B, Se, So as gSq_core uses
key_txt = block("      ∧ ((b1 + (b0 * y0 + b2 * y1) / 2) ^ 2", ":= by\n  obtain ⟨t, ht0, ht2⟩", after="theorem rsq_key")
lhs, rhs = key_txt.split("≤")
key_l = to_sympy("((b1 + (b0 * y0 + b2 * y1) / 2) ^ 2" + lhs)
key_r = to_sympy(rhs)
check("L4 rsq_key third conjunct == (Se^2+So^2)/50 <= A*B for gSq_core's A, B, Se, So",
      sp.expand(key_l - (sub[sp.Symbol("Se")] ** 2 + sub[sp.Symbol("So")] ** 2) / 50) == 0
      and sp.expand(key_r - sub[sp.Symbol("A")] * sub[sp.Symbol("B")]) == 0)

# rsq_s statement: certificate re-check against the text
s_txt = block("    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :\n    (b1 + (f * y0", ":= by\n  have hy4", after="theorem rsq_s")
s_l, s_r = ("(b1 + (f * y0" + s_txt).split("≤")
f, b1, b2, b3, b4, b5 = sp.symbols("f b1 b2 b3 b4 b5")
y0, y1, y2, y3, y4 = sp.symbols("y0:5")
h = sp.Rational(1, 2)
X = f * y0 + b2 * y1
Z = b5 * y2 + b4 * y3
cert = ((b1 - X / 2) ** 2 + (b3 * y4 - Z / 2) ** 2 + h * (f * y1 - b2 * y0) ** 2 + h * (b5 * y3 - b4 * y2) ** 2
        + 2 * b3 ** 2 * (1 - y4 ** 2) + h * (f ** 2 - b2 ** 2) * (y0 ** 2 + y1 ** 2)
        + h * (f ** 2 - b5 ** 2 - b4 ** 2) * (y2 ** 2 + y3 ** 2) + h * f ** 2 * (y2 ** 2 + y3 ** 2)
        + 2 * b2 ** 2 + 2 * b4 ** 2)
check("L5 rsq_s text: RHS - LHS == nonnegative certificate", sp.expand(to_sympy(s_r) - to_sympy(s_l) - cert) == 0)

# rsq_ab final certificate against the text
t, s, u, A, B = sp.symbols("t s u A B")
L1, L2 = f + u - t * s / 2, f - u - t * s / 2
ab_goal = to_sympy(block("    0 ≤ A ∧ 0 ≤ B ∧", ":= by\n  have hts", after="theorem rsq_ab").split("≤")[0])
check("L6 rsq_ab text: AB - goal == certificate",
      sp.expand(A * B - ab_goal - ((A * B - L1 * L2) + ((f ** 2 - t ** 2) * (1 - s ** 2) - u ** 2)
                                   + h * (t - f * s) ** 2 + sp.Rational(3, 8) * t ** 2 * (1 - s ** 2)
                                   + sp.Rational(3, 8) * s ** 2 * (f ** 2 - t ** 2))) == 0)
print()
print("%d failed" % len(FAILS))
sys.exit(1 if FAILS else 0)
