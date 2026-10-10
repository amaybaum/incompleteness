#!/usr/bin/env python3
"""
b1_implicit.py -- thread B (PAIR-ACT), research only: no implicit consumption of hgate / hinv.

Run:  python3 -I -B b1_implicit.py <pt-root> <B1_UNBUILT.lean>

Purpose.  b1_consumed S1 counts the occurrences of the NAMES hgate and hinv per declaration on the proof path of
kt4_forward_ie1 and matches them with the consuming calls.  A tactic that reads the local context without naming a
hypothesis (assumption, simp [*], simp_all, aesop, tauto, ...) could consume hgate or hinv invisibly to that count, and
the _cons declarations of B1_UNBUILT.lean (copies of the design declarations with the consuming lines changed) would
then lack a hypothesis the copied lines need.  This script checks that no such tactic occurs where hgate or hinv is in
scope, in the design declarations and in the UNBUILT file.

Decision rules (fixed before the first run; rules, not expected numbers):
  I1  The scanned design declarations are exactly the twelve on-path declarations of b1_consumed's frozen list
      (where hgate or hinv is a binder), extracted from inputs/fourcopy/*.lean by the same extraction as b1_consumed
      (comments stripped; a declaration runs from its keyword line to the next declaration keyword).  PASS iff all
      twelve are found and each has an hgate or hinv binder.
  I2  Context-reading tactics, frozen list CTX: assumption, ‹, [*, simp_all, aesop, tauto, itauto, solve_by_elim,
      apply_assumption, exact?, apply?, trivial, grind, cc, contradiction, exact_mod_cast, assumption_mod_cast, fun_prop,
      gcongr, bound, continuity, measurability, simpa (without 'using'), linarith, nlinarith, polyrith, omega,
      positivity.  The subclass ARITH = {linarith, nlinarith, polyrith, omega, positivity} reads only hypotheses that
      are comparisons (Mathlib Tactic/Linarith/Preprocessing.lean filterComparisons; Tactic/Positivity/Core.lean
      compareHyp: hypotheses of the form a </<=/= e).  PASS iff every CTX occurrence in the scanned design
      declarations and in the UNBUILT file (comments stripped) belongs to ARITH.
  I3  The binder types of hgate and hinv in the scanned design declarations contain no comparison symbol
      (<=, <, >=, >, !=, = and their Unicode forms), so ARITH tactics drop them.  PASS iff every binder is found and
      none contains one.
  I4  Positive control (the scanner is not blind): at least one ARITH occurrence is found in the UNBUILT file, and the
      scanner reports it with its declaration.
  I5  Countercontrols, each must be DETECTED: (i) 'assumption' inserted into a copy of the design body of bell_mem
      makes I2 fail; (ii) a binder '(hgate : ∀ ω ∈ K, 0 ≤ ipW ω ω)' inserted into a copy of link_mem makes I3 fail;
      (iii) 'simpa' (without 'using') inserted into a copy of the UNBUILT text makes I2 fail.
  VERDICT B1-IMPLICIT prints only if I1-I5 all pass.  No timing in stdout.
"""
import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAILS = []


def check(cid, kind, ok, text, detail=""):
    global PASS_COUNT
    tag = "PASS" if ok else "FAIL"
    line = f"{tag} {cid}  [{kind}] {text}"
    if detail:
        line += " -- " + detail
    print(line)
    if ok:
        PASS_COUNT += 1
    else:
        FAILS.append(cid)


DECL_RE = re.compile(r"^(?:theorem|lemma|def|abbrev|structure|noncomputable def)\s+([A-Za-z0-9_.']+)", re.M)

ON_PATH = [
    "FourCopyHeadline.ie1_all", "FourCopyHeadline.parity_all", "FourCopyHeadline.kt4_general_ie1",
    "FourCopyHeadline.kt4_forward_ie1", "FourCopyHeadline.kt4_forward_ie1_kt4", "FourCopyHeadline.kt4_forward_ie1_lt",
    "FourCopyIE1.link_mem", "FourCopyIE1.parity_witnesses", "FourCopyLocal.bell_mem", "FourCopyLocal.bell_mem_dual",
    "FourCopyBipolar.inv_mem_of_orth", "FourCopyParity.dualW_of_inv",
]

WORD = r"(?<![A-Za-z0-9_'?])"
END = r"(?![A-Za-z0-9_'?])"
CTX = {
    "assumption": WORD + r"assumption" + END,
    "‹": r"‹",
    "[*": r"\[\s*\*",
    "simp_all": WORD + r"simp_all" + END,
    "aesop": WORD + r"aesop" + END,
    "tauto": WORD + r"tauto" + END,
    "itauto": WORD + r"itauto" + END,
    "solve_by_elim": WORD + r"solve_by_elim" + END,
    "apply_assumption": WORD + r"apply_assumption" + END,
    "exact?": WORD + r"exact\?",
    "apply?": WORD + r"apply\?",
    "trivial": WORD + r"trivial" + END,
    "grind": WORD + r"grind" + END,
    "cc": WORD + r"cc" + END,
    "contradiction": WORD + r"contradiction" + END,
    "exact_mod_cast": WORD + r"exact_mod_cast" + END,
    "assumption_mod_cast": WORD + r"assumption_mod_cast" + END,
    "fun_prop": WORD + r"fun_prop" + END,
    "gcongr": WORD + r"gcongr" + END,
    "bound": WORD + r"bound" + END,
    "continuity": WORD + r"continuity" + END,
    "measurability": WORD + r"measurability" + END,
    "simpa (no using)": WORD + r"simpa" + END + r"(?![^\n]*\busing\b)",
    "linarith": WORD + r"linarith" + END,
    "nlinarith": WORD + r"nlinarith" + END,
    "polyrith": WORD + r"polyrith" + END,
    "omega": WORD + r"omega" + END,
    "positivity": WORD + r"positivity" + END,
}
ARITH = {"linarith", "nlinarith", "polyrith", "omega", "positivity"}
COMPARISON = re.compile(r"≤|<|≥|>|≠|(?<![:≃])=(?!>)")


def strip_comments(src):
    src = re.sub(r"/-.*?-/", lambda m: "\n" * m.group(0).count("\n"), src, flags=re.S)
    return re.sub(r"--[^\n]*", "", src)


def decls(src):
    starts = [(m.start(), m.group(1)) for m in DECL_RE.finditer(src)]
    starts.append((len(src), None))
    return {nm: src[s:e] for (s, nm), (e, _) in zip(starts, starts[1:])}


def ctx_hits(body):
    hits = []
    for name, pat in CTX.items():
        for _ in re.finditer(pat, body):
            hits.append(name)
    return hits


def binder_types(body):
    # (hgate : TYPE) / (hinv : TYPE) with one level of nested parentheses in TYPE
    return re.findall(r"\((hgate|hinv)\s*:\s*((?:[^()]|\([^()]*\))*)\)", body)


def i2_ok(bodies):
    bad = []
    for key, body in bodies.items():
        for h in ctx_hits(body):
            if h not in ARITH:
                bad.append((key, h))
    return bad


def i3_ok(bodies):
    bad, n = [], 0
    for key, body in bodies.items():
        for (nm, tp) in binder_types(body):
            n += 1
            if COMPARISON.search(tp):
                bad.append((key, nm, tp.strip()))
    return bad, n


def main():
    if len(sys.argv) != 3:
        print("usage: python3 -I -B b1_implicit.py <pt-root> <B1_UNBUILT.lean>")
        sys.exit(2)
    root = Path(sys.argv[1])
    design = root / "inputs" / "fourcopy"
    unbuilt = strip_comments(Path(sys.argv[2]).read_text(encoding="utf-8"))

    print("== I1  the on-path design declarations")
    bodies = {}
    for key in ON_PATH:
        mod, nm = key.split(".", 1)
        d = decls(strip_comments((design / f"{mod}.lean").read_text(encoding="utf-8")))
        if nm in d:
            bodies[key] = d[nm]
    have_binder = {k: bool(binder_types(b)) for k, b in bodies.items()}
    check("I1", "source", len(bodies) == len(ON_PATH) and all(have_binder.values()),
          "the twelve on-path declarations are found and each has an hgate or hinv binder",
          f"{len(bodies)}/{len(ON_PATH)} found; with binder {sum(have_binder.values())}")

    print("\n== I2  context-reading tactics where hgate / hinv are in scope")
    ub = decls(unbuilt)
    for key in ON_PATH:
        print(f"  design {key}: {sorted(ctx_hits(bodies.get(key, ''))) or 'none'}")
    for nm, body in ub.items():
        h = ctx_hits(body)
        if h:
            print(f"  UNBUILT {nm}: {sorted(h)}")
    bad_d = i2_ok(bodies)
    bad_u = i2_ok({f"UNBUILT.{k}": v for k, v in ub.items()})
    check("I2", "source", not bad_d and not bad_u,
          "every context-reading tactic in scope of hgate/hinv (design) and in the UNBUILT file reads only comparisons",
          f"non-arithmetic hits: design {bad_d}, UNBUILT {bad_u}")

    print("\n== I3  the binder types of hgate and hinv")
    bad3, n3 = i3_ok(bodies)
    types = sorted({tp.strip() for b in bodies.values() for (_, tp) in binder_types(b)})
    for t in types:
        print(f"  binder type: {t}")
    check("I3", "source", not bad3 and n3 >= len(bodies),
          "no hgate/hinv binder type is a comparison, so the arithmetic tactics drop them",
          f"{n3} binders; comparison-typed {bad3}")

    print("\n== I4  positive control")
    arith_u = [(nm, h) for nm, b in ub.items() for h in ctx_hits(b) if h in ARITH]
    check("I4", "control", len(arith_u) >= 1,
          "the scanner finds the arithmetic tactics of the UNBUILT file (not blind)",
          f"{len(arith_u)} hits: {sorted(set(arith_u))}")

    print("\n== I5  countercontrols")
    b1 = dict(bodies)
    b1["FourCopyLocal.bell_mem"] = b1["FourCopyLocal.bell_mem"] + "\n  assumption\n"
    check("I5.i", "countercontrol", bool(i2_ok(b1)),
          "countercontrol: 'assumption' planted in bell_mem is detected by I2")
    b2 = dict(bodies)
    b2["FourCopyIE1.link_mem"] = b2["FourCopyIE1.link_mem"] + "\n  (hgate : ∀ ω ∈ K, 0 ≤ ipW ω ω)\n"
    bad_b2, _ = i3_ok(b2)
    check("I5.ii", "countercontrol", bool(bad_b2),
          "countercontrol: a comparison-typed hgate binder planted in link_mem is detected by I3")
    u3 = decls(unbuilt + "\ntheorem planted_x : True := by\n  simpa\n")
    check("I5.iii", "countercontrol", bool(i2_ok({f"UNBUILT.{k}": v for k, v in u3.items()})),
          "countercontrol: 'simpa' without 'using' planted in the UNBUILT text is detected by I2")

    print()
    total = PASS_COUNT + len(FAILS)
    if FAILS:
        print(f"b1_implicit: NO VERDICT -- {len(FAILS)} of {total} checks failed: {', '.join(FAILS)}")
        sys.exit(1)
    print("VERDICT B1-IMPLICIT: where hgate or hinv is in scope on the design proof path, and anywhere in "
          "B1_UNBUILT.lean, the only context-reading tactics are arithmetic ones, which drop non-comparison "
          "hypotheses; hgate and hinv are not comparisons, so they are consumed only where named (b1_consumed S1)")
    print(f"b1_implicit: OK -- {total} checks")


if __name__ == "__main__":
    main()
