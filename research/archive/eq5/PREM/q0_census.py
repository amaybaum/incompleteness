"""EQ5-PREM q0 — exact text census of the base for the candidate sources of TokProdState / tok (Part A) and of
gate preservation hgate (Part B).  Read-only over the base snapshot.  Research only; nothing here is adopted.

Usage:  python3 -I -B q0_census.py <base>/verification/lean-mathlib/OIBridge <base> <eq5>/inputs

What it establishes (each a finite text fact about the base at bcbc516f):
  * every kernel object and record line the result cites exists at the cited file:line with the cited text;
  * which candidate objects are complex-typed (their declaration block contains the character ℂ) and which are
    field-neutral;
  * the import separation between the field-neutral composite core and the complex-side candidate modules;
  * the absence, in every field-neutral module, of any regrouping / four-token / token-coherence vocabulary;
  * the status records (ROADMAP K1/K2/K∞/Kₙ, the K∞ seams audit, COMP-1's open list, Main.md's OI⁺ scope sentence and
    posit ledger, the typed-completion audit's coherence outcome).

DECISION RULE (fixed before the first run; rules, not expected numbers):
 A  anchors: each cited triple (file, line, text) holds iff the line, stripped of leading whitespace, starts with the
    text.  Families: A1 complex-side candidates, A2 field-neutral candidates (Part A and Part B), A3 records.
 T  typing: the declaration block of an object is its declaration line up to (excluding) the first following line that
    is blank or starts a new top-level declaration or doc comment.  An object is COMPLEX-TYPED iff its block contains
    'ℂ' or names 'FiniteOperationalTheory' or 'TheoryFamily' (the control establishes that the structure block of
    FiniteOperationalTheory contains 'ℂ').  T1: every complex-side candidate is complex-typed; T2: every field-neutral
    candidate is not.  Controls: FiniteOperationalTheory (structure block) contains 'ℂ' and PreComposite's does not.
 I  imports: the transitive OIBridge import closure of every module.  I1 holds iff no field-neutral core module reaches
    a complex-side candidate module and no complex-side candidate module reaches a field-neutral core module.  Control:
    the closure contains the known direct edges EmbeddedObservation -> CarrierGeneralOIPlus and
    CompositeInterface -> CompletionAction -> StageCompletion.
 F  vocabulary: no field-neutral core module contains any of the strings in FORBIDDEN.  Controls: the same scan finds
    'TokenCoherent' and 'W4' in the inputs package and 'Regroup' in EmbeddedObservation.
 R  records: the ledger paragraph of Main.md (the line starting '**The posit ledger.**') contains 'Seven items' and
    'Axiom 2' and none of 'compos', 'tensor', 'token identity', 'regroup' (case-insensitive).
 VERDICT Q0-CENSUS-COMPLETE iff every check passes; otherwise VERDICT NOT RENDERED.  No timing in stdout.
"""
import os
import re
import sys

LEAN = sys.argv[1]
BASE = sys.argv[2]
INPUTS = sys.argv[3]
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def lean(mod):
    return read(os.path.join(LEAN, mod + ".lean"))


def anchor_ok(text, line, prefix):
    lines = text.split("\n")
    if line < 1 or line > len(lines):
        return False
    return lines[line - 1].lstrip().startswith(prefix)


def run_anchors(name, triples):
    bad = []
    for src, line, prefix in triples:
        text = lean(src) if not src.startswith("/") else read(src)
        if not anchor_ok(text, line, prefix):
            bad.append("%s:%d" % (os.path.basename(src), line))
    return check(name, not bad, "%d anchors; missing: %s" % (len(triples), bad if bad else "none"))


# ------------------------------------------------------------------ A1 complex-side candidates
A1 = [
    ("EmbeddedObservation", 98, "def RegroupingInvariant (𝒯 : TheoryFamily) : Prop :="),
    ("EmbeddedObservation", 106, "def RelabellingInvariant (𝒯 : TheoryFamily) : Prop :="),
    ("EmbeddedObservation", 123, "def EmbeddedObservation (T : FiniteOperationalTheory A) : Prop :="),
    ("CarrierGeneralOIPlus", 73, "def ObservationalIndependence : Prop := HasParallelReferenceExtension T"),
    ("CarrierGeneralOIPlus", 75, "theorem observationalIndependence_iff_inert :"),
    ("CarrierGeneralOIPlus", 207, "theorem oiPlus_iff_qm : OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T :="),
    ("ReferenceExtension", 422, "def withSpectator (R : Type*) [Fintype R] [DecidableEq R] {n m : ℕ}"),
    ("ReferenceExtension", 447, "def HasParallelReferenceExtension (T : FiniteOperationalTheory A) : Prop :="),
    ("SpectatorBridge", 223, "def InertSpectatorCompositionality (T : FiniteOperationalTheory A) : Prop :="),
    ("MonoidalCompletion", 204, "def SpectatorIndependent (CB : Equiv.Perm B → Matrix B B ℂ)"),
    ("MonoidalCompletion", 311, "def HComp (act : ι → Equiv.Perm (A × B)) (corr : ι → Matrix (A × B) (A × B) ℂ)"),
    ("OperationalAssembly", 594, "structure FiniteOperationalTheory (A : Type*) [Fintype A] [DecidableEq A] where"),
]
run_anchors("A1 complex-side candidates present at the cited lines", A1)

# ------------------------------------------------------------------ A2 field-neutral candidates
A2 = [
    ("CompositeInterface", 210, "structure ProductData (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] where"),
    ("CompositeInterface", 223, "structure PreComposite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)"),
    ("CompositeInterface", 243, "structure Composite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)"),
    ("CompositeInterface", 306, "theorem margA_prodState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : D.margA (D.prodState x y) = x := by"),
    ("CompositeInterface", 332, "theorem condA_prodState (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) {y : Fin dB → ℝ} (hy : f y ≠ 0)"),
    ("CompositeInterface", 382, "theorem margA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) :"),
    ("CompositeInterface", 445, "abbrev JointReversible (G : Set (V ≃ᵃ[ℝ] V)) : Prop := PreservesBody P.Ω G"),
    ("CompositeInterface", 148, "theorem exists_effect_rescale {Ω : Set (Fin d → ℝ)} (hb : BoundedAffine Ω)"),
    ("CompositeInterface", 290, "theorem prodEff_expand (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : V) :"),
    ("CompositeInterface", 750, "def minComposite {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} (hA : IsCompact ΩA)"),
    ("CompositeInterface", 807, "def ball3MinComposite : Composite ball3 ball3 (Carrier 3 3) :="),
    ("CompositeInterface", 811, "def ball3MaxComposite : Composite ball3 ball3 (Carrier 3 3) :="),
    ("CompositeInterface", 848, "def paddedPre : PreComposite ΩA ΩB (V × ℝ) where"),
    ("OrbitGeneration", 69, "def PreservesBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :="),
    ("OrbitGeneration", 74, "def SeedOrbitAvailable (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) (avail : Set (V →ᵃ[ℝ] ℝ)) :"),
    ("CompletionAction", 46, "structure OpDatum (D : DirectedStages) where"),
    ("CompletionAction", 58, "def AffineRespect (T : OpDatum D) : Prop :="),
    ("CompletionAction", 202, "theorem body_isClosed : IsClosed (body D) := isClosed_closure"),
    ("CompletionAction", 300, "theorem induced_mem {T : OpDatum D} (hT : AffineRespect T) :"),
    ("CompletionAction", 352, "theorem preservesBody_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S)"),
    ("StageCompletion", 141, "def body : Set (CSpace D) :="),
    ("StageCompletion", 142, "closure (convexHull ℝ (Set.range (prepVec D)))"),
    ("CompositeDimension", 97, "abbrev W (d : ℕ) := Fin (d + 1) → Fin (d + 1) → ℝ"),
    ("CompositeDimension", 186, "def maxCone (Ω : Set (Fin d → ℝ)) : Set (W d) :="),
    ("CompositeDimension", 218, "structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))"),
    ("CompositeDimension", 222, "posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω"),
    ("CompositeDimension", 223, "posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω"),
    ("CompositeDimension", 869, "def Lor (v : HVec d) : Prop := 0 ≤ v 0 ∧ ∑ j : Fin d, v j.succ ^ 2 ≤ v 0 ^ 2"),
    ("CompositeDimension", 930, "theorem lor_ehom {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) : Lor (ehom e) := by"),
    ("CompositeDimension", 1160, "theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot where"),
    ("CompositeDimension", 1380, "theorem entangling_cnot : Entangling (eball 3) cnot :="),
    ("K1Bridge", 49, "structure NativeGateOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ)"),
    ("EffectSpace", 572, "theorem maxConeOf_avail_eq (hd : 0 < d) (hG : PreservesBody (eball d) G)"),
    ("K2Guard", 95, "def CandidateCone (K : Set (W 3)) : Prop :="),
    ("KInfFoundations", 116, "def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :="),
    ("KInfFoundations", 264, "structure ElementaryDrivability (Ω : Set V) where"),
    ("KInfFoundations", 284, "def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) : Prop :="),
]
run_anchors("A2 field-neutral candidates (Part A and Part B) present at the cited lines", A2)

# ------------------------------------------------------------------ A3 records
V = os.path.join(BASE, "verification")
A3 = [
    (os.path.join(V, "ROADMAP.md"), 984, "- **K1 — the dimension. CONDITIONAL.**"),
    (os.path.join(V, "ROADMAP.md"), 1001, "- **K2 — the composite. OPEN.**"),
    (os.path.join(V, "ROADMAP.md"), 1007, "- **K∞ — the field-neutral premises. OPEN.**"),
    (os.path.join(V, "ROADMAP.md"), 1014, "- **K∞-Act** — reversible operation data on the completed body"),
    (os.path.join(V, "ROADMAP.md"), 1027, "- **K∞-Copy** — identical-copy covariance, or copy naturality"),
    (os.path.join(V, "ROADMAP.md"), 1058, "- **Kₙ — elementary-to-arbitrary-carrier lift. OPEN.**"),
    (os.path.join(V, "audits/foundations/kinf-seams-audit.md"), 44,
     "Body preservation, `PreservesBody Ω G`, is not a separate entry: `preservesBody_inducedEquiv` gives it from K∞-Act,"),
    (os.path.join(V, "programmes/oi-qm/reconstruction/round-comp-1-composite-interface/result.md"), 106,
     "reversible action and a common NOT on a composite; the dimension selector."),
    (os.path.join(V, "audits/operational/typed-completion-audit.md"), 60,
     "question: the product-type cross-carrier coherence that embedded observation asks for is automatic"),
    (os.path.join(BASE, "papers/Main.md"), 568,
     "Each added principle is independently necessary relative to the OI core, well-formedness, and the other two. "
     "This is a characterization of a quantum-complete extension of OI, not a claim that bare OI entails the added "
     "principles"),
    (os.path.join(BASE, "papers/Main.md"), 706, "**The posit ledger.**"),
]
run_anchors("A3 record lines present (ROADMAP K-rows, seams audit :44, COMP-1 open list, typed audit :60, Main.md "
            ":568, :706)", A3)

# ------------------------------------------------------------------ T typing
DECL = re.compile(r"^(def|abbrev|structure|theorem|lemma|class|inductive|instance|noncomputable def|/--|/-!|@\[)")


def decl_block(mod, line):
    lines = lean(mod).split("\n")
    out = [lines[line - 1]]
    for k in range(line, len(lines)):
        s = lines[k]
        if s.strip() == "" or DECL.match(s):
            break
        out.append(s)
    return "\n".join(out)


COMPLEX_C = [("EmbeddedObservation", 98), ("EmbeddedObservation", 106), ("EmbeddedObservation", 123),
             ("ReferenceExtension", 447), ("SpectatorBridge", 223), ("MonoidalCompletion", 311),
             ("MonoidalCompletion", 204)]
NEUTRAL_C = [("CompositeInterface", 223), ("CompositeInterface", 445), ("OrbitGeneration", 69),
             ("CompletionAction", 46), ("CompletionAction", 58), ("StageCompletion", 141), ("CompositeDimension", 218),
             ("K1Bridge", 49), ("K2Guard", 95), ("KInfFoundations", 264), ("KInfFoundations", 284)]
blocks_c = {"%s:%d" % m: decl_block(*m) for m in COMPLEX_C}
blocks_n = {"%s:%d" % m: decl_block(*m) for m in NEUTRAL_C}
CPLX_MARK = ("ℂ", "FiniteOperationalTheory", "TheoryFamily")


def complex_typed(block):
    return any(t in block for t in CPLX_MARK)


fot = decl_block("OperationalAssembly", 594)
ctrl_t = ("ℂ" in fot) and ("ℂ" not in blocks_n["CompositeInterface:223"])
check("T1 complex-side candidates are complex-typed (block contains ℂ, or names FiniteOperationalTheory / "
      "TheoryFamily)", all(complex_typed(b) for b in blocks_c.values()),
      "; ".join("%s:%s" % (k, "ℂ" if "ℂ" in b else "via theory type") for k, b in blocks_c.items()))
check("T2 field-neutral candidates are not complex-typed", not any(complex_typed(b) for b in blocks_n.values()),
      ", ".join(k for k in blocks_n))
check("T-control FiniteOperationalTheory's structure block contains ℂ; PreComposite's does not", ctrl_t)

# ------------------------------------------------------------------ I imports
mods = sorted(f[:-5] for f in os.listdir(LEAN) if f.endswith(".lean"))
direct = {}
for m in mods:
    direct[m] = set(re.findall(r"^import OIBridge\.(\w+)", lean(m), re.M))


def closure(m):
    seen, stack = set(), [m]
    while stack:
        x = stack.pop()
        for y in direct.get(x, ()):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen


CORE = ["CompositeInterface", "CompositeDimension", "K2Guard", "K1Bridge", "EffectSpace", "CompletionAction",
        "StageCompletion", "OrbitGeneration", "KInfFoundations", "TransitiveBody", "InvariantInnerProduct",
        "CompositionOrder", "NativeGateBall", "OrbitNormalization"]
CPLX = ["EmbeddedObservation", "CarrierGeneralOIPlus", "CompletedOI", "ReferenceExtension", "SpectatorBridge",
        "MonoidalCompletion", "OperationalAssembly", "TypedCompletion", "RegionTower", "RegionLimit",
        "QuasilocalAlgebra"]
cl = {m: closure(m) for m in mods}
cross = [(a, b) for a in CORE for b in CPLX if b in cl[a]] + [(b, a) for a in CORE for b in CPLX if a in cl[b]]
ctrl_i = ("CarrierGeneralOIPlus" in direct["EmbeddedObservation"] and "CompletionAction" in direct["CompositeInterface"]
          and "StageCompletion" in direct["CompletionAction"] and "StageCompletion" in cl["CompositeInterface"])
check("I1 no import path in either direction between the field-neutral core (%d modules) and the complex-side "
      "candidate modules (%d)" % (len(CORE), len(CPLX)), not cross, "crossing paths: %s" % (cross if cross else "none"))
check("I-control known edges EmbeddedObservation->CarrierGeneralOIPlus, CompositeInterface->CompletionAction->"
      "StageCompletion found", ctrl_i)

# ------------------------------------------------------------------ F vocabulary
FORBIDDEN = ["Regroup", "regroup", "TokProd", "TokenCoherent", "FourCopy", "W4", "prodState4", "Associat", "associat",
             "JointTower", "stageProd", "LocalExt", "fourToken", "FourToken"]
hits = [(m, w) for m in CORE for w in FORBIDDEN if w in lean(m)]
pkg = read(os.path.join(INPUTS, "FourCopyPackage.lean")) + read(os.path.join(INPUTS, "FourCopyDefs.lean"))
ctrl_f = "TokenCoherent" in pkg and "W4" in pkg and "Regroup" in lean("EmbeddedObservation")
check("F no field-neutral core module contains regrouping / four-token / token-coherence vocabulary",
      not hits, "hits: %s" % (hits if hits else "none"))
check("F-control the scan finds TokenCoherent and W4 in the inputs package and Regroup in EmbeddedObservation",
      ctrl_f)

# ------------------------------------------------------------------ R records
main_lines = read(os.path.join(BASE, "papers/Main.md")).split("\n")
ledger = next(l for l in main_lines if l.startswith("**The posit ledger.**"))
low = ledger.lower()
check("R Main.md posit ledger: 'Seven items' and 'Axiom 2' present; no 'compos', 'tensor', 'token identity', "
      "'regroup'", "Seven items" in ledger and "Axiom 2" in ledger
      and not any(w in low for w in ("compos", "tensor", "token identity", "regroup")))

nfail = sum(1 for _, ok in CHECKS if not ok)
print("--- q0_census: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT Q0-CENSUS-COMPLETE" if nfail == 0 else "VERDICT NOT RENDERED")
