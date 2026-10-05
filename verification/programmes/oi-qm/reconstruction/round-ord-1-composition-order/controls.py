#!/usr/bin/env python3
"""controls.py -- round ORD-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context line is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  separation  no transitivity, ball-geometry, drive, flow, continuity, compactness or inner-product token in the
                  module; no import of TransitiveBody or InvariantInnerProduct; the header disclaimer present
  S2  dimension   outside the controls section no statement names `3`, `Fin 3`, `ball3`, `rot3`, `hh3`, `fullAut3` or
                  `finrank`
  S3  F-D3        `finiteOrderOn_of_stagePreserving` has exactly the frozen binders (chart, two data, two
                  AffineRespect, two Undoes, StagePreserving) and the frozen conclusion
  S4  definitions `InfiniteOrderOn`, `FiniteOrderOn`, `OrdInf` (existential over `G`), `MulClosed`, `StagePreserving`
                  (same stage on both sides), `idDatum`, `iterAfter` are the frozen texts
  S5  closure     the closure control carries both `G.Finite` and `MulClosed G`, and the singleton countercontrol is a
                  kernel theorem with its print
  S6  controls    the §E controls are kernel theorems with prints
  S7  directions  finite/infinite order are two theorems, one per direction; the `iff` cites both names in its proof
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.TransitiveBody`
  C   census      the census is D's with exactly the frozen family inserted after the TRB-1 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = 'afa66d16d7adaffe94fb9bac391e6039c51dad8a'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-ord-1-composition-order/'
PREREG = RDIR + 'preregistration.md'
MOD = 'verification/lean-mathlib/OIBridge/CompositionOrder.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = 'd8e04d32423c1f5ec33c1c9100822f6dadc727eb'
ANCHOR_IMPORT = 'import OIBridge.TransitiveBody\n'
NEW_IMPORT = 'import OIBridge.CompositionOrder\n'
PREV_FAMILY_PREFIX = 'the completed-chart adapter, the boundary-state bridge, boun'
CENSUS_FAMILY = json.loads(r'''{
 "name": "iterated operation data and finite/infinite order on the completed body (round ORD-1, reconstruction)",
 "modules": [
  "CompositionOrder"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round ORD-1, a native round under AGENTS.md §A.39. The kernel layer composes a completion-valued operation datum that respects affine relations with itself through the composition law of CompletionAction and names finite and infinite order of an affine automorphism on a set of states, with ORD∞ as the predicate that a set of automorphisms has a member of infinite order and MulClosed as composition closure. It proves that the map induced by the m-fold composite is the m-fold composite of the induced map (induced_iterAfter), that a reversible datum whose induced automorphism has infinite order on the chart body has every positive power nontrivial on the preparations (exists_moved_of_infiniteOrderOn), that a reversible datum carrying each stage's preparations to preparation vectors of the same stage induces an automorphism of finite order on the chart body (finiteOrderOn_of_stagePreserving), through a finite affinely spanning subset of the chart generators (exists_finset_affineSpan_eq_top), and that a finite composition-closed set of automorphisms has no member of infinite order (not_ordInf_of_finite_of_mulClosed); controls show the rotation by one radian of infinite order on the ball (infiniteOrderOn_rot3_one), the Householder reflections without a member of infinite order (not_ordInf_householder3), and the singleton of the rotation, finite and not composition-closed, with one (ordInf_singleton_rot3). Carried by no manuscript. Nothing here claims transitivity, a ball theorem, a dimension, a drive or a flow, and TRANS ⇒ ORD∞ is not stated; nothing supplies an operation datum, finite rank, a completion chart or stage preservation from an OI construction."
}''')
DECLS = json.loads(r'''[
 [
  "def",
  "InfiniteOrderOn"
 ],
 [
  "def",
  "FiniteOrderOn"
 ],
 [
  "def",
  "OrdInf"
 ],
 [
  "def",
  "MulClosed"
 ],
 [
  "def",
  "affPow"
 ],
 [
  "theorem",
  "coe_affPow"
 ],
 [
  "theorem",
  "finiteOrderOn_of_not_infiniteOrderOn"
 ],
 [
  "theorem",
  "not_infiniteOrderOn_of_finiteOrderOn"
 ],
 [
  "theorem",
  "not_infiniteOrderOn_iff"
 ],
 [
  "theorem",
  "finiteOrderOn_refl"
 ],
 [
  "theorem",
  "finiteOrderOn_of_iterate_eq"
 ],
 [
  "theorem",
  "not_ordInf_of_finite_of_mulClosed"
 ],
 [
  "theorem",
  "exists_return"
 ],
 [
  "theorem",
  "exists_common_period"
 ],
 [
  "theorem",
  "exists_finset_affineSpan_eq_top"
 ],
 [
  "noncomputable def",
  "idDatum"
 ],
 [
  "def",
  "StagePreserving"
 ],
 [
  "theorem",
  "affineRespect_idDatum"
 ],
 [
  "noncomputable def",
  "iterAfter"
 ],
 [
  "noncomputable def",
  "stageGen"
 ],
 [
  "theorem",
  "induced_idDatum"
 ],
 [
  "theorem",
  "affineRespect_iterAfter"
 ],
 [
  "theorem",
  "induced_iterAfter"
 ],
 [
  "theorem",
  "coe_induced_iterAfter"
 ],
 [
  "theorem",
  "coe_inducedEquiv"
 ],
 [
  "theorem",
  "iterate_eq_id_of_fix"
 ],
 [
  "theorem",
  "exists_moved_of_infiniteOrderOn"
 ],
 [
  "theorem",
  "nonempty_prep"
 ],
 [
  "theorem",
  "exists_gen_finset"
 ],
 [
  "theorem",
  "mem_stageGen"
 ],
 [
  "theorem",
  "mapsTo_stageGen"
 ],
 [
  "theorem",
  "finiteOrderOn_of_stagePreserving"
 ],
 [
  "theorem",
  "not_infiniteOrderOn_of_stagePreserving"
 ],
 [
  "theorem",
  "not_stagePreserving_of_infiniteOrderOn"
 ],
 [
  "def",
  "householder3"
 ],
 [
  "theorem",
  "hh3_hh3"
 ],
 [
  "theorem",
  "finiteOrderOn_hh3"
 ],
 [
  "theorem",
  "not_ordInf_householder3"
 ],
 [
  "theorem",
  "rot3_mem_fullAut3"
 ],
 [
  "theorem",
  "rot3_one_iterate"
 ],
 [
  "theorem",
  "infiniteOrderOn_rot3_one"
 ],
 [
  "theorem",
  "ordInf_fullAut3"
 ],
 [
  "theorem",
  "ordInf_range_rot3"
 ],
 [
  "theorem",
  "ordInf_singleton_rot3"
 ],
 [
  "theorem",
  "ord1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "InfiniteOrderOn": "def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop :=\n  ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x",
 "FiniteOrderOn": "def FiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop :=\n  ∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x",
 "OrdInf": "def OrdInf (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∃ g ∈ G, InfiniteOrderOn Ω g",
 "MulClosed": "def MulClosed (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G",
 "affPow": "def affPow (Φ : V →ᵃ[ℝ] V) : ℕ → V →ᵃ[ℝ] V\n  | 0 => AffineMap.id ℝ V\n  | m + 1 => Φ.comp (affPow Φ m)",
 "coe_affPow": "theorem coe_affPow (Φ : V →ᵃ[ℝ] V) (m : ℕ) : ⇑(affPow Φ m) = (⇑Φ)^[m]",
 "finiteOrderOn_of_not_infiniteOrderOn": "theorem finiteOrderOn_of_not_infiniteOrderOn {Ω : Set V} {g : V ≃ᵃ[ℝ] V}\n    (h : ¬ InfiniteOrderOn Ω g) : FiniteOrderOn Ω g",
 "not_infiniteOrderOn_of_finiteOrderOn": "theorem not_infiniteOrderOn_of_finiteOrderOn {Ω : Set V} {g : V ≃ᵃ[ℝ] V}\n    (h : FiniteOrderOn Ω g) : ¬ InfiniteOrderOn Ω g",
 "not_infiniteOrderOn_iff": "theorem not_infiniteOrderOn_iff {Ω : Set V} {g : V ≃ᵃ[ℝ] V} :\n    ¬ InfiniteOrderOn Ω g ↔ FiniteOrderOn Ω g",
 "finiteOrderOn_refl": "theorem finiteOrderOn_refl (Ω : Set V) : FiniteOrderOn Ω (AffineEquiv.refl ℝ V)",
 "finiteOrderOn_of_iterate_eq": "theorem finiteOrderOn_of_iterate_eq {Ω : Set V} {g : V ≃ᵃ[ℝ] V} {a b : ℕ} (hab : a < b)\n    (h : (⇑g)^[a] = (⇑g)^[b]) : FiniteOrderOn Ω g",
 "not_ordInf_of_finite_of_mulClosed": "theorem not_ordInf_of_finite_of_mulClosed {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hG : G.Finite)\n    (hcl : MulClosed G) : ¬ OrdInf Ω G",
 "exists_return": "theorem exists_return {S : Finset α} {f : α → α} (hf : Function.Injective f)\n    (hm : ∀ w ∈ S, f w ∈ S) {w : α} (hw : w ∈ S) : ∃ p : ℕ, 0 < p ∧ f^[p] w = w",
 "exists_common_period": "theorem exists_common_period {f : α → α} (A : Finset α)\n    (h : ∀ w ∈ A, ∃ p : ℕ, 0 < p ∧ f^[p] w = w) :\n    ∃ N : ℕ, 1 ≤ N ∧ ∀ w ∈ A, f^[N] w = w",
 "exists_finset_affineSpan_eq_top": "theorem exists_finset_affineSpan_eq_top {V P : Type*} [AddCommGroup V] [Module ℝ V]\n    [AddTorsor V P] [FiniteDimensional ℝ V] {s : Set P} (h : affineSpan ℝ s = ⊤) :\n    ∃ t : Finset P, (↑t : Set P) ⊆ s ∧ affineSpan ℝ (↑t : Set P) = ⊤",
 "idDatum": "noncomputable def idDatum (D : DirectedStages) : OpDatum D where\n  τ := prepVec D\n  mem_body := prepVec_mem_body D",
 "StagePreserving": "def StagePreserving (T : OpDatum D) : Prop :=\n  ∀ (i : D.ι) (x : (D.stage i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩",
 "affineRespect_idDatum": "theorem affineRespect_idDatum : AffineRespect (idDatum D)",
 "iterAfter": "noncomputable def iterAfter (T : OpDatum D) (hT : AffineRespect T) : ℕ → OpDatum D\n  | 0 => idDatum D\n  | m + 1 => after C T (iterAfter T hT m) hT",
 "stageGen": "noncomputable def stageGen (i : D.ι) : Finset (Fin C.d → ℝ) := by\n  classical exact Finset.univ.image fun y : (D.stage i).P => gen C ⟨i, y⟩",
 "induced_idDatum": "theorem induced_idDatum : induced C (idDatum D) affineRespect_idDatum = AffineMap.id ℝ _",
 "affineRespect_iterAfter": "theorem affineRespect_iterAfter {T : OpDatum D} (hT : AffineRespect T) (m : ℕ) :\n    AffineRespect (iterAfter C T hT m)",
 "induced_iterAfter": "theorem induced_iterAfter {T : OpDatum D} (hT : AffineRespect T) (m : ℕ) :\n    induced C (iterAfter C T hT m) (affineRespect_iterAfter C hT m) =\n      affPow (induced C T hT) m",
 "coe_induced_iterAfter": "theorem coe_induced_iterAfter {T : OpDatum D} (hT : AffineRespect T) (m : ℕ) :\n    ⇑(induced C (iterAfter C T hT m) (affineRespect_iterAfter C hT m)) =\n      (⇑(induced C T hT))^[m]",
 "coe_inducedEquiv": "theorem coe_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)\n    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :\n    ⇑(inducedEquiv C hS hT hST hTS) = ⇑(induced C T hT)",
 "iterate_eq_id_of_fix": "theorem iterate_eq_id_of_fix {T : OpDatum D} (hT : AffineRespect T) (m : ℕ)\n    (h : ∀ x, (iterAfter C T hT m).τ x = prepVec D x) : (⇑(induced C T hT))^[m] = id",
 "exists_moved_of_infiniteOrderOn": "theorem exists_moved_of_infiniteOrderOn {S T : OpDatum D} (hS : AffineRespect S)\n    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)\n    (h : InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) :\n    ∀ m : ℕ, 1 ≤ m → AffineRespect (iterAfter C T hT m) ∧\n      ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x",
 "nonempty_prep": "theorem nonempty_prep (C : CompletionChart D) : Nonempty (Prep D)",
 "exists_gen_finset": "theorem exists_gen_finset :\n    ∃ A : Finset (Prep D),\n      affineSpan ℝ ((A.image (gen C) : Finset (Fin C.d → ℝ)) : Set (Fin C.d → ℝ)) = ⊤",
 "mem_stageGen": "theorem mem_stageGen (i : D.ι) (y : (D.stage i).P) : gen C ⟨i, y⟩ ∈ stageGen C i",
 "mapsTo_stageGen": "theorem mapsTo_stageGen {T : OpDatum D} (hT : AffineRespect T) (hsp : StagePreserving T)\n    (i : D.ι) : ∀ w ∈ stageGen C i, induced C T hT w ∈ stageGen C i",
 "finiteOrderOn_of_stagePreserving": "theorem finiteOrderOn_of_stagePreserving {S T : OpDatum D} (hS : AffineRespect S)\n    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)\n    (hsp : StagePreserving T) :\n    FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)",
 "not_infiniteOrderOn_of_stagePreserving": "theorem not_infiniteOrderOn_of_stagePreserving {S T : OpDatum D} (hS : AffineRespect S)\n    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)\n    (hsp : StagePreserving T) :\n    ¬ InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)",
 "not_stagePreserving_of_infiniteOrderOn": "theorem not_stagePreserving_of_infiniteOrderOn {S T : OpDatum D} (hS : AffineRespect S)\n    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)\n    (h : InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) :\n    ¬ StagePreserving T",
 "householder3": "def householder3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) := {g | ∃ d k hk, g = hh3 d k hk}",
 "hh3_hh3": "theorem hh3_hh3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)\n    (v : Fin 3 → ℝ) : hh3 d k hk (hh3 d k hk v) = v",
 "finiteOrderOn_hh3": "theorem finiteOrderOn_hh3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1) :\n    FiniteOrderOn ball3 (hh3 d k hk)",
 "not_ordInf_householder3": "theorem not_ordInf_householder3 : ¬ OrdInf ball3 householder3",
 "rot3_mem_fullAut3": "theorem rot3_mem_fullAut3 (t : ℝ) : rot3 t ∈ fullAut3",
 "rot3_one_iterate": "theorem rot3_one_iterate (m : ℕ) (v : Fin 3 → ℝ) : (⇑(rot3 1))^[m] v = rotFun (m : ℝ) v",
 "infiniteOrderOn_rot3_one": "theorem infiniteOrderOn_rot3_one : InfiniteOrderOn ball3 (rot3 1)",
 "ordInf_fullAut3": "theorem ordInf_fullAut3 : OrdInf ball3 fullAut3",
 "ordInf_range_rot3": "theorem ordInf_range_rot3 : OrdInf ball3 (Set.range rot3)",
 "ordInf_singleton_rot3": "theorem ordInf_singleton_rot3 : OrdInf ball3 {rot3 1}",
 "ord1_core": "theorem ord1_core :\n    (∀ (D : DirectedStages) (C : CompletionChart D) (S T : OpDatum D) (hS : AffineRespect S)\n      (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT),\n        StagePreserving T → FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) ∧\n    (∀ (D : DirectedStages) (C : CompletionChart D) (S T : OpDatum D) (hS : AffineRespect S)\n      (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT),\n        InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS) →\n          ∀ m : ℕ, 1 ≤ m → ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x) ∧\n    InfiniteOrderOn ball3 (rot3 1) ∧ ¬ OrdInf ball3 householder3 ∧ OrdInf ball3 {rot3 1} ∧\n    (∀ (V : Type) [AddCommGroup V] [Module ℝ V] (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)),\n      G.Finite → MulClosed G → ¬ OrdInf Ω G)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.CompositionOrder.coe_affPow",
 "OIBridge.CompositionOrder.finiteOrderOn_of_not_infiniteOrderOn",
 "OIBridge.CompositionOrder.not_infiniteOrderOn_of_finiteOrderOn",
 "OIBridge.CompositionOrder.not_infiniteOrderOn_iff",
 "OIBridge.CompositionOrder.finiteOrderOn_refl",
 "OIBridge.CompositionOrder.finiteOrderOn_of_iterate_eq",
 "OIBridge.CompositionOrder.not_ordInf_of_finite_of_mulClosed",
 "OIBridge.CompositionOrder.exists_return",
 "OIBridge.CompositionOrder.exists_common_period",
 "OIBridge.CompositionOrder.exists_finset_affineSpan_eq_top",
 "OIBridge.CompositionOrder.affineRespect_idDatum",
 "OIBridge.CompositionOrder.induced_idDatum",
 "OIBridge.CompositionOrder.affineRespect_iterAfter",
 "OIBridge.CompositionOrder.induced_iterAfter",
 "OIBridge.CompositionOrder.coe_induced_iterAfter",
 "OIBridge.CompositionOrder.coe_inducedEquiv",
 "OIBridge.CompositionOrder.iterate_eq_id_of_fix",
 "OIBridge.CompositionOrder.exists_moved_of_infiniteOrderOn",
 "OIBridge.CompositionOrder.nonempty_prep",
 "OIBridge.CompositionOrder.exists_gen_finset",
 "OIBridge.CompositionOrder.mem_stageGen",
 "OIBridge.CompositionOrder.mapsTo_stageGen",
 "OIBridge.CompositionOrder.finiteOrderOn_of_stagePreserving",
 "OIBridge.CompositionOrder.not_infiniteOrderOn_of_stagePreserving",
 "OIBridge.CompositionOrder.not_stagePreserving_of_infiniteOrderOn",
 "OIBridge.CompositionOrder.hh3_hh3",
 "OIBridge.CompositionOrder.finiteOrderOn_hh3",
 "OIBridge.CompositionOrder.not_ordInf_householder3",
 "OIBridge.CompositionOrder.rot3_mem_fullAut3",
 "OIBridge.CompositionOrder.rot3_one_iterate",
 "OIBridge.CompositionOrder.infiniteOrderOn_rot3_one",
 "OIBridge.CompositionOrder.ordInf_fullAut3",
 "OIBridge.CompositionOrder.ordInf_range_rot3",
 "OIBridge.CompositionOrder.ordInf_singleton_rot3",
 "OIBridge.CompositionOrder.ord1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.CompletionAction\nimport Mathlib.Analysis.Real.Pi.Irrational\n\nnamespace OIBridge\nnamespace CompositionOrder\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace CompositionOrder",
 "open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction",
 "section Order",
 "variable {V : Type*} [AddCommGroup V] [Module ℝ V]",
 "end Order",
 "section Generic",
 "variable {α : Type*}",
 "end Generic",
 "variable {D : DirectedStages}",
 "variable (C : CompletionChart D)",
 "end CompositionOrder",
 "end OIBridge"
]''')

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
                  re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]


def check(code, name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name, flush=True)
    if not cond:
        FAILS.append(code)


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = git('show', '%s:%s' % (commit, path))
    return r.stdout if r.returncode == 0 else None


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    return [m.group(0) for m in CTX.finditer(text)]


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def decl_chunks(text):
    """name -> (kind, chunk up to the next declaration or stop marker, proof text after ' :=' for theorems)."""
    out = {}
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        proof = ''
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            if j != -1:
                proof = text[start + j:nxt]
                chunk = chunk[:j]
        out[m.group(2)] = (m.group(1), chunk, proof)
    return out


def decl_texts(text):
    return {n: c for n, (_, c, _) in decl_chunks(text).items()}


def split_statement(stmt):
    """(binders, conclusion) at the first colon at bracket depth 0 after the name."""
    parts = stmt.split(None, 2)
    i = len(parts[0]) + 1 + len(parts[1])
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return stmt[i:j], stmt[j + 1:]
    return stmt[i:], ''


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def norm(s):
    return ' '.join(s.split())


PREFIX = 'OIBridge.CompositionOrder.'
FD3 = 'finiteOrderOn_of_stagePreserving'
IFF, DIR1, DIR2 = 'not_infiniteOrderOn_iff', 'finiteOrderOn_of_not_infiniteOrderOn', 'not_infiniteOrderOn_of_finiteOrderOn'
CLOSURE, SINGLETON = 'not_ordInf_of_finite_of_mulClosed', 'ordInf_singleton_rot3'
CONTROL_THMS = ('finiteOrderOn_refl', 'hh3_hh3', 'finiteOrderOn_hh3', 'not_ordInf_householder3', 'rot3_one_iterate',
                'infiniteOrderOn_rot3_one', 'ordInf_fullAut3', 'ordInf_range_rot3', 'ordInf_singleton_rot3',
                'not_ordInf_of_finite_of_mulClosed')
FORBIDDEN_TOKENS = ('BoundaryTransitive', 'CoversBoundaryFrom', 'IsBodyGroup', 'TransBody', 'Transitive',
                    'ElementaryDrivability', 'Continuous', 'IsCompact', 'invMatrix', 'SCInf', 'BinaryVisible',
                    'SharpSeed', 'centroid', 'qBall', 'eball', 'import OIBridge.TransitiveBody',
                    'import OIBridge.InvariantInnerProduct')
DISCLAIMER = 'No transitivity, ball, dimension, drive or flow is claimed; TRANS ⇒ ORD∞ is not stated.'
DIM3 = re.compile(r'ball3|Fin 3|rot3|hh3|fullAut3|finrank|(?<![\w.])3(?![\w.])')
FD3_BINDERS = ('{S T : OpDatum D}', '(hS : AffineRespect S)', '(hT : AffineRespect T)',
               '(hST : Undoes C S T hS)', '(hTS : Undoes C T S hT)', '(hsp : StagePreserving T)')
FD3_CONCL = 'FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)'
DEF_TEXTS = {
    'InfiniteOrderOn': '∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x',
    'FiniteOrderOn': '∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x',
    'OrdInf': ':= ∃ g ∈ G, InfiniteOrderOn Ω g',
    'MulClosed': '∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G',
    'StagePreserving': '∀ (i : D.ι) (x : (D.stage i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩',
    'idDatum': 'τ := prepVec D',
    'iterAfter': '| m + 1 => after C T (iterAfter T hT m) hT',
}


def control_names(mod):
    i = mod.find('\n/-! ### §E')
    j = mod.find('\n/-! ### §F')
    if i == -1 or j == -1:
        return set()
    return {n for _, n in decls(mod[i:j])}


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    hits = [t for t in FORBIDDEN_TOKENS if t in mod]
    check('S1', 'no transitivity, ball, drive, flow or inner-product token; disclaimer present%s%s'
          % (tag, (' %s' % hits[:3]) if hits else ''), not hits and DISCLAIMER in norm(mod))
    ctrl = control_names(mod)
    bad = [n for n, t in texts.items() if n not in ctrl and n != 'ord1_core' and DIM3.search(t)]
    vt = texts.get('ord1_core', '')
    check('S2', 'no dimension outside the controls%s%s' % (tag, (' %s' % bad[:3]) if bad else ''),
          not bad and 'StagePreserving T → FiniteOrderOn (chartBody C)' in norm(vt))
    t = texts.get(FD3, '')
    b, c = split_statement(t) if t else ('', '')
    check('S3', 'the stage-preservation theorem carries exactly the frozen hypotheses' + tag,
          kinds.get(FD3) == 'theorem' and all(h in norm(t) for h in FD3_BINDERS) and norm(c) == FD3_CONCL
          and 'variable (C : CompletionChart D)' in context_lines(mod)
          and norm(b).count('(') == 5
          and not any(f in b for f in ('SCInf', 'BinaryVisible', 'Continuous', 'IsCompact', 'Transitive')))
    check('S4', 'the order predicates and the iterated datum are the frozen definitions' + tag,
          all(kinds.get(n) in ('def', 'noncomputable def') and DEF_TEXTS[n] in norm(texts.get(n, ''))
              for n in DEF_TEXTS) and '∀ g ∈ G' not in texts.get('OrdInf', ''))
    tc = texts.get(CLOSURE, '')
    check('S5', 'the closure control needs finiteness and closure; the singleton countercontrol is present' + tag,
          kinds.get(CLOSURE) == 'theorem' and '(hG : G.Finite)' in norm(tc) and '(hcl : MulClosed G)' in norm(tc)
          and norm(split_statement(tc)[1]) == '¬ OrdInf Ω G' and kinds.get(SINGLETON) == 'theorem'
          and PREFIX + SINGLETON in prints and norm(split_statement(texts[SINGLETON])[1]) == 'OrdInf ball3 {rot3 1}')
    check('S6', 'the controls are kernel theorems with prints' + tag,
          all(kinds.get(n) == 'theorem' and PREFIX + n in prints for n in CONTROL_THMS))
    check('S7', 'one direction per theorem; the iff cites both' + tag,
          kinds.get(DIR1) == 'theorem' and kinds.get(DIR2) == 'theorem'
          and '↔' not in texts.get(DIR1, '') and '↔' not in texts.get(DIR2, '')
          and (IFF not in texts or (DIR1 in proofs.get(IFF, '') and DIR2 in proofs.get(IFF, ''))))


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context line unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s' % (tag, (' (changed: %s)' % ', '.join(bad[:4]))
                                                                        if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, chunks, prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_ok(d_text, e_text):
    try:
        d, e = json.loads(d_text), json.loads(e_text)
    except Exception:
        return False
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['name'].startswith(PREV_FAMILY_PREFIX)]
    if len(k) != 1:
        return False
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return e == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    module_checks(show(commit, MOD))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family', census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def must_fail(code, label, mod2):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mod2)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) >= 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    i = text.rindex('\nend ')
    i = text.rindex('\nend ', 0, i)
    return text[:i] + '\n' + decl + '\n' + text[i:]


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    must_fail('N1', 'a removed declaration', replace_once(mod, '\n' + DECLS[-1][0] + ' ' + DECLS[-1][1],
                                                          '\n' + DECLS[-1][0] + ' ' + DECLS[-1][1] + 'X'))
    must_fail('N2', 'a changed binder context', replace_once(mod, CONTEXT[-3], CONTEXT[-3] + ' -- x\nopen Real'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, '∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x', '∃ N : ℕ, ∀ x ∈ Ω, (⇑g)^[N] x = x'))
    must_fail('N3', 'a sorry', append_decl(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('S1', 'a transitivity hypothesis with an order conclusion',
              append_decl(mod, 'theorem ordInf_of_bt (Ω : Set (Fin 3 → ℝ)) (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)))\n'
                               '    (h : BoundaryTransitive Ω G) : OrdInf Ω G := by\n  exact absurd h h'))
    must_fail('S1', 'the TransitiveBody import', replace_once(mod, 'import OIBridge.CompletionAction\n',
                                                              'import OIBridge.CompletionAction\nimport OIBridge.TransitiveBody\n'))
    must_fail('S2', 'a 3 in the stage-preservation theorem',
              replace_once(mod, 'FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS) := by\n  classical',
                           'FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS) ∧ C.d = 3 := by\n  classical'))
    must_fail('S3', 'reversibility dropped from the stage-preservation theorem',
              replace_once(mod, '(hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)\n    (hsp : StagePreserving T) :\n    FiniteOrderOn',
                           '(hT : AffineRespect T) (hST : Undoes C S T hS)\n    (hsp : StagePreserving T) :\n    FiniteOrderOn'))
    must_fail('S4', 'ORD∞ made universal', replace_once(mod, ':= ∃ g ∈ G, InfiniteOrderOn Ω g', ':= ∀ g ∈ G, InfiniteOrderOn Ω g'))
    must_fail('S4', 'stage preservation across stages',
              replace_once(mod, 'T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩', 'T.τ ⟨i, x⟩ = prepVec D ⟨j, y⟩'))
    must_fail('S5', 'closure dropped from the closure control',
              replace_once(mod, '(hG : G.Finite)\n    (hcl : MulClosed G) : ¬ OrdInf Ω G', '(hG : G.Finite) : ¬ OrdInf Ω G'))
    must_fail('S6', 'a control print removed',
              replace_once(mod, '#print axioms OIBridge.CompositionOrder.infiniteOrderOn_rot3_one\n', ''))
    must_fail('S7', 'one direction removed',
              replace_once(mod, 'theorem not_infiniteOrderOn_of_finiteOrderOn', 'theorem not_infiniteOrderOn_of_finiteOrderOn2'))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(PREV_FAMILY_PREFIX)][0]
    good = dict(dd)
    good['families'] = dd['families'][:k + 1] + [CENSUS_FAMILY] + dd['families'][k + 1:]
    bad = json.loads(json.dumps(good))
    bad['families'][k + 1]['status'] = 'carried'
    check('M', 'census: the frozen family passes and a changed status fails',
          census_ok(d_cen, json.dumps(good)) and not census_ok(d_cen, json.dumps(bad)))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
