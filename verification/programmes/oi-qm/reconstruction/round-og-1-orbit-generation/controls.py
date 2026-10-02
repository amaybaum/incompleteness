#!/usr/bin/env python3
"""controls.py -- round OG-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the candidate blobs; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  L   continuity  OrbitGeneration.lean is the frozen blob; its byte suffix from the first `import` has the frozen
                  SHA-256, which is the suffix of the design-validated draft (Thread L, blob e9722042)
  N1  decls       OrbitNormalization.lean declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every def/abbrev is the frozen
                  text whole; the preamble (imports, namespaces, `open`, `variable`) is the frozen text -- a proof
                  may change, a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide in either module; every frozen
                  `#print axioms` line present
  S1  4-ball      the countercontrol is a kernel theorem: `boundaryTransitive_ball4` and `finrank_E4` are theorems
                  with axiom prints, not probe output
  S2  dimension   only `finrank_E4` and the verdict mention `finrank`; no theorem has BoundaryTransitive among its
                  hypotheses and `finrank` in its conclusion
  S3  G-AUT       `preservesBody_words` has exactly one hypothesis, `PreservesBody` on the generators, and `words` is
                  the subgroup closure
  S4  transport   `hypotheses_tr` and `hypotheses_restrict` conclude all four named hypotheses of the transported
                  data (body, seed, automorphisms, available effects) together
  S5  no sourcing no theorem concludes SharpSeed, SeedOrbitAvailable or ElementaryDrivability without the same predicate
                  among its hypotheses; only the two named controls conclude BoundaryTransitive without it; no
                  declaration name or header claims a source for the ellipsoid, the drive, dimension three, SC∞, ELEM
                  or V4′
  I   imports     OIBridge.lean is D's with exactly the two frozen import lines after `import OIBridge.KInfFoundations`
  C   census      the census is D's with exactly the frozen family inserted after the KINF-2 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, json, re, subprocess, sys

D = '6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-og-1-orbit-generation/'
PREREG = RDIR + 'preregistration.md'
OG = 'verification/lean-mathlib/OIBridge/OrbitGeneration.lean'
ON = 'verification/lean-mathlib/OIBridge/OrbitNormalization.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {OG: 'A', ON: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
L_DRAFT_BLOB = 'e9722042c2fc076ef292cbdb6d800a591ff71eb4'
OG_BLOB = '0673321f2920b38674685a1494c1cdbf42e0d2d1'
ON_REFERENCE_BLOB = 'bf627dfe3563fb9361e41fe7e633ea49168be95e'
OG_SUFFIX_SHA256 = '843c68c1a4d2dffff9b595475c710b960201c3ba8e218b71af1bfc50291415d9'
IMPORT_LINES = 'import OIBridge.KInfFoundations\nimport OIBridge.OrbitGeneration\nimport OIBridge.OrbitNormalization\n'
CENSUS_FAMILY = json.loads(r'''{
 "name": "conditional orbit-generation infrastructure — the reduced orbit-generation theorem for one sharp readout on the 3-ball, its transport along affine coordinate changes and affine charts, generated words of a drive, boundary transitivity of the control drive, and the four-dimensional countercontrol (round OG-1, reconstruction)",
 "modules": [
  "OrbitGeneration",
  "OrbitNormalization"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round OG-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-og-1-orbit-generation/preregistration.md. The kernel layer is conditional: given a sharp seed (P1), seed-orbit availability (V4′), boundary transitivity (K∞-R) and that the automorphisms preserve the body, the transports of the seed on the 3-ball are exactly the directional effects (1 + b·x)/2 and reach NativeGateBall.lorentz_of_effects at p = 3 (seedOrbit_ball3_eq, lorentz_of_available); the hypotheses move unchanged along affine coordinate changes and affine charts of the body's affine span (hypotheses_tr, hypotheses_restrict); body preservation extends from generators to words (preservesBody_words); the words of the control drive ball3Drive are boundary-transitive (boundaryTransitive_ball3Drive); the unit ball of a four-dimensional Euclidean space is boundary-transitive under its isometries (boundaryTransitive_ball4). Carried by no manuscript. None of the hypotheses is sourced: no OI construction supplies the seed, the drive, dimension three, or seed-orbit availability, and nothing here is a reconstruction theorem."
}''')
KINF2_FAMILY_PREFIX = 'the corrected field-neutral vocabulary of the pre-quantum completion'
ON_DECLS = json.loads(r'''[
 [
  "def",
  "words"
 ],
 [
  "theorem",
  "subset_words"
 ],
 [
  "theorem",
  "mul_mem_words"
 ],
 [
  "theorem",
  "inv_mem_words"
 ],
 [
  "theorem",
  "one_apply'"
 ],
 [
  "theorem",
  "mul_apply'"
 ],
 [
  "theorem",
  "symm_eq_inv"
 ],
 [
  "theorem",
  "inv_apply'"
 ],
 [
  "theorem",
  "preservesBody_words"
 ],
 [
  "theorem",
  "preservesBody_driveWords"
 ],
 [
  "theorem",
  "flow_zero_of_add"
 ],
 [
  "theorem",
  "isEmpty_drivability_of_finite_orbits"
 ],
 [
  "noncomputable def",
  "effTr"
 ],
 [
  "theorem",
  "effTr_apply"
 ],
 [
  "theorem",
  "effTr_apply_apply"
 ],
 [
  "theorem",
  "effTr_comp"
 ],
 [
  "theorem",
  "effTr_injective"
 ],
 [
  "def",
  "conjTr"
 ],
 [
  "theorem",
  "conjTr_apply"
 ],
 [
  "theorem",
  "conjTr_apply_apply"
 ],
 [
  "theorem",
  "conjTr_symm_apply"
 ],
 [
  "theorem",
  "mem_image_tr"
 ],
 [
  "theorem",
  "apply_mem_image_tr"
 ],
 [
  "theorem",
  "tr_extension"
 ],
 [
  "theorem",
  "isEffectOn_tr"
 ],
 [
  "theorem",
  "isProperOn_tr"
 ],
 [
  "theorem",
  "isBoundaryState_tr"
 ],
 [
  "theorem",
  "sharpSeed_tr"
 ],
 [
  "theorem",
  "preservesBody_tr"
 ],
 [
  "theorem",
  "boundaryTransitive_tr"
 ],
 [
  "theorem",
  "seedTransport_tr"
 ],
 [
  "theorem",
  "seedOrbit_tr"
 ],
 [
  "theorem",
  "seedOrbitAvailable_tr"
 ],
 [
  "theorem",
  "hypotheses_tr"
 ],
 [
  "theorem",
  "seedOrbit_eq_of_normalization"
 ],
 [
  "theorem",
  "lorentz_of_normalization"
 ],
 [
  "noncomputable def",
  "chart"
 ],
 [
  "theorem",
  "chart_apply"
 ],
 [
  "theorem",
  "chart_injective"
 ],
 [
  "theorem",
  "chart_extension"
 ],
 [
  "theorem",
  "exists_chart_leftInverse"
 ],
 [
  "noncomputable def",
  "chartRetract"
 ],
 [
  "theorem",
  "chartRetract_apply"
 ],
 [
  "theorem",
  "chartRetract_chart"
 ],
 [
  "theorem",
  "chart_chartRetract"
 ],
 [
  "def",
  "bodyR"
 ],
 [
  "noncomputable def",
  "effR"
 ],
 [
  "theorem",
  "effR_apply"
 ],
 [
  "theorem",
  "isBoundaryState_restrict"
 ],
 [
  "theorem",
  "isEffectOn_restrict"
 ],
 [
  "theorem",
  "sharpSeed_restrict"
 ],
 [
  "theorem",
  "affineSpan_preserved"
 ],
 [
  "theorem",
  "range_preserved"
 ],
 [
  "noncomputable def",
  "restrictMap"
 ],
 [
  "theorem",
  "restrictMap_apply"
 ],
 [
  "theorem",
  "chart_restrictMap"
 ],
 [
  "theorem",
  "restrictMap_bijective"
 ],
 [
  "noncomputable def",
  "restrictEquiv"
 ],
 [
  "theorem",
  "chart_restrictEquiv"
 ],
 [
  "theorem",
  "chart_restrictEquiv_symm"
 ],
 [
  "def",
  "autR"
 ],
 [
  "theorem",
  "seedTransport_restrict"
 ],
 [
  "theorem",
  "hypotheses_restrict"
 ],
 [
  "def",
  "driveWords3"
 ],
 [
  "theorem",
  "rot3_mem_driveWords3"
 ],
 [
  "theorem",
  "cyc3_mem_driveWords3"
 ],
 [
  "noncomputable def",
  "rotX"
 ],
 [
  "theorem",
  "rotX_mem_driveWords3"
 ],
 [
  "theorem",
  "euler_apply_pole"
 ],
 [
  "theorem",
  "exists_euler_angles"
 ],
 [
  "theorem",
  "exists_word_pole"
 ],
 [
  "theorem",
  "boundaryTransitive_ball3Drive"
 ],
 [
  "theorem",
  "preservesBody_driveWords3"
 ],
 [
  "theorem",
  "seedOrbit_ball3Drive"
 ],
 [
  "theorem",
  "isBoundaryState_closedBall_iff"
 ],
 [
  "abbrev",
  "E4"
 ],
 [
  "def",
  "ball4"
 ],
 [
  "def",
  "isom4"
 ],
 [
  "theorem",
  "preservesBody_isom4"
 ],
 [
  "theorem",
  "boundaryTransitive_ball4"
 ],
 [
  "theorem",
  "finrank_E4"
 ],
 [
  "theorem",
  "zero_mem_interior_ball4"
 ],
 [
  "theorem",
  "og1_infrastructure_core"
 ]
]''')
ON_TEXTS = json.loads(r'''{
 "words": "def words (S : Set (V ≃ᵃ[ℝ] V)) : Set (V ≃ᵃ[ℝ] V) := (Subgroup.closure S : Set (V ≃ᵃ[ℝ] V))",
 "subset_words": "theorem subset_words (S : Set (V ≃ᵃ[ℝ] V)) : S ⊆ words S",
 "mul_mem_words": "theorem mul_mem_words {S : Set (V ≃ᵃ[ℝ] V)} {g k : V ≃ᵃ[ℝ] V} (hg : g ∈ words S)\n    (hk : k ∈ words S) : g * k ∈ words S",
 "inv_mem_words": "theorem inv_mem_words {S : Set (V ≃ᵃ[ℝ] V)} {g : V ≃ᵃ[ℝ] V} (hg : g ∈ words S) :\n    g⁻¹ ∈ words S",
 "one_apply'": "theorem one_apply' (x : V) : (1 : V ≃ᵃ[ℝ] V) x = x",
 "mul_apply'": "theorem mul_apply' (g k : V ≃ᵃ[ℝ] V) (x : V) : (g * k) x = g (k x)",
 "symm_eq_inv": "theorem symm_eq_inv (g : V ≃ᵃ[ℝ] V) : g.symm = g⁻¹",
 "inv_apply'": "theorem inv_apply' (g : V ≃ᵃ[ℝ] V) (x : V) : g⁻¹ x = g.symm x",
 "preservesBody_words": "theorem preservesBody_words {Ω : Set V} {S : Set (V ≃ᵃ[ℝ] V)} (h : PreservesBody Ω S) :\n    PreservesBody Ω (words S)",
 "preservesBody_driveWords": "theorem preservesBody_driveWords {Ω : Set V} (D : ElementaryDrivability Ω) :\n    PreservesBody Ω (words (Set.range D.flow ∪ {D.J}))",
 "flow_zero_of_add": "theorem flow_zero_of_add (flow : ℝ → V ≃ᵃ[ℝ] V)\n    (h : ∀ s t, flow (s + t) = (flow t).trans (flow s)) : flow 0 = AffineEquiv.refl ℝ V",
 "isEmpty_drivability_of_finite_orbits": "theorem isEmpty_drivability_of_finite_orbits {Ω : Set V}\n    (hfin : ∀ x ∈ Ω,\n      {y | ∃ g : V ≃ᵃ[ℝ] V, (∀ z ∈ Ω, g z ∈ Ω ∧ g.symm z ∈ Ω) ∧ g x = y}.Finite) :\n    IsEmpty (ElementaryDrivability Ω)",
 "effTr": "noncomputable def effTr (T : V ≃ᵃ[ℝ] W) (e : V →ᵃ[ℝ] ℝ) : W →ᵃ[ℝ] ℝ :=\n  e.comp T.symm.toAffineMap",
 "effTr_apply": "theorem effTr_apply (T : V ≃ᵃ[ℝ] W) (e : V →ᵃ[ℝ] ℝ) (w : W) : effTr T e w = e (T.symm w)",
 "effTr_apply_apply": "theorem effTr_apply_apply (T : V ≃ᵃ[ℝ] W) (e : V →ᵃ[ℝ] ℝ) (x : V) : effTr T e (T x) = e x",
 "effTr_comp": "theorem effTr_comp (T : V ≃ᵃ[ℝ] W) (e : V →ᵃ[ℝ] ℝ) : (effTr T e).comp T.toAffineMap = e",
 "effTr_injective": "theorem effTr_injective (T : V ≃ᵃ[ℝ] W) : Function.Injective (effTr T)",
 "conjTr": "def conjTr (T : V ≃ᵃ[ℝ] W) (g : V ≃ᵃ[ℝ] V) : W ≃ᵃ[ℝ] W := (T.symm.trans g).trans T",
 "conjTr_apply": "theorem conjTr_apply (T : V ≃ᵃ[ℝ] W) (g : V ≃ᵃ[ℝ] V) (w : W) :\n    conjTr T g w = T (g (T.symm w))",
 "conjTr_apply_apply": "theorem conjTr_apply_apply (T : V ≃ᵃ[ℝ] W) (g : V ≃ᵃ[ℝ] V) (x : V) :\n    conjTr T g (T x) = T (g x)",
 "conjTr_symm_apply": "theorem conjTr_symm_apply (T : V ≃ᵃ[ℝ] W) (g : V ≃ᵃ[ℝ] V) (w : W) :\n    (conjTr T g).symm w = T (g.symm (T.symm w))",
 "mem_image_tr": "theorem mem_image_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {w : W} : w ∈ T '' Ω ↔ T.symm w ∈ Ω",
 "apply_mem_image_tr": "theorem apply_mem_image_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {x : V} : T x ∈ T '' Ω ↔ x ∈ Ω",
 "tr_extension": "theorem tr_extension (T : V ≃ᵃ[ℝ] W) (x y : V) (ε : ℝ) :\n    T (x + ε • (x - y)) = T x + ε • (T x - T y)",
 "isEffectOn_tr": "theorem isEffectOn_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} (he : IsEffectOn Ω e) :\n    IsEffectOn (T '' Ω) (effTr T e)",
 "isProperOn_tr": "theorem isProperOn_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} (he : IsProperOn Ω e) :\n    IsProperOn (T '' Ω) (effTr T e)",
 "isBoundaryState_tr": "theorem isBoundaryState_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {x : V} :\n    IsBoundaryState Ω x ↔ IsBoundaryState (T '' Ω) (T x)",
 "sharpSeed_tr": "theorem sharpSeed_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {r : V →ᵃ[ℝ] ℝ} (hr : SharpSeed Ω r) :\n    SharpSeed (T '' Ω) (effTr T r)",
 "preservesBody_tr": "theorem preservesBody_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)}\n    (hG : PreservesBody Ω G) : PreservesBody (T '' Ω) (conjTr T '' G)",
 "boundaryTransitive_tr": "theorem boundaryTransitive_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)}\n    (hK : BoundaryTransitive Ω G) : BoundaryTransitive (T '' Ω) (conjTr T '' G)",
 "seedTransport_tr": "theorem seedTransport_tr (T : V ≃ᵃ[ℝ] W) (r : V →ᵃ[ℝ] ℝ) (g : V ≃ᵃ[ℝ] V) :\n    seedTransport (effTr T r) (conjTr T g) = effTr T (seedTransport r g)",
 "seedOrbit_tr": "theorem seedOrbit_tr (T : V ≃ᵃ[ℝ] W) (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) :\n    seedOrbit (conjTr T '' G) (effTr T r) = effTr T '' seedOrbit G r",
 "seedOrbitAvailable_tr": "theorem seedOrbitAvailable_tr (T : V ≃ᵃ[ℝ] W) {G : Set (V ≃ᵃ[ℝ] V)} {r : V →ᵃ[ℝ] ℝ}\n    {avail : Set (V →ᵃ[ℝ] ℝ)} (hV4 : SeedOrbitAvailable G r avail) :\n    SeedOrbitAvailable (conjTr T '' G) (effTr T r) (effTr T '' avail)",
 "hypotheses_tr": "theorem hypotheses_tr (T : V ≃ᵃ[ℝ] W) {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} {r : V →ᵃ[ℝ] ℝ}\n    {avail : Set (V →ᵃ[ℝ] ℝ)} (hG : PreservesBody Ω G) (hP1 : SharpSeed Ω r)\n    (hK : BoundaryTransitive Ω G) (hV4 : SeedOrbitAvailable G r avail) :\n    PreservesBody (T '' Ω) (conjTr T '' G) ∧ SharpSeed (T '' Ω) (effTr T r) ∧\n      BoundaryTransitive (T '' Ω) (conjTr T '' G) ∧\n      SeedOrbitAvailable (conjTr T '' G) (effTr T r) (effTr T '' avail)",
 "seedOrbit_eq_of_normalization": "theorem seedOrbit_eq_of_normalization {Ω : Set V} (T : V ≃ᵃ[ℝ] (Fin 3 → ℝ)) (hT : T '' Ω = ball3)\n    {G : Set (V ≃ᵃ[ℝ] V)} {r : V →ᵃ[ℝ] ℝ} (hG : PreservesBody Ω G) (hP1 : SharpSeed Ω r)\n    (hK : BoundaryTransitive Ω G) :\n    seedOrbit G r =\n      {f | ∃ b : Fin 3 → ℝ, b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1 ∧\n        f = (ballEffect b).comp T.toAffineMap}",
 "lorentz_of_normalization": "theorem lorentz_of_normalization {Ω : Set V} (T : V ≃ᵃ[ℝ] (Fin 3 → ℝ)) (hT : T '' Ω = ball3)\n    {G : Set (V ≃ᵃ[ℝ] V)} {r : V →ᵃ[ℝ] ℝ} (hG : PreservesBody Ω G) (hP1 : SharpSeed Ω r)\n    (hK : BoundaryTransitive Ω G) (x0 : ℝ) (v : Fin 3 → ℝ)\n    (h : ∀ e ∈ seedOrbit G r, 0 ≤ conePair (effTr T e) x0 v) :\n    0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2",
 "chart": "noncomputable def chart (L : W →ₗ[ℝ] V) (p0 : V) : W →ᵃ[ℝ] V :=\n  L.toAffineMap + AffineMap.const ℝ W p0",
 "chart_apply": "theorem chart_apply (L : W →ₗ[ℝ] V) (p0 : V) (w : W) : chart L p0 w = L w + p0",
 "chart_injective": "theorem chart_injective {L : W →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) (p0 : V) :\n    Function.Injective (chart L p0)",
 "chart_extension": "theorem chart_extension (L : W →ₗ[ℝ] V) (p0 : V) (w u : W) (ε : ℝ) :\n    chart L p0 (w + ε • (w - u)) =\n      chart L p0 w + ε • (chart L p0 w - chart L p0 u)",
 "exists_chart_leftInverse": "theorem exists_chart_leftInverse {L : W →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) :\n    ∃ Lg : V →ₗ[ℝ] W, ∀ w, Lg (L w) = w",
 "chartRetract": "noncomputable def chartRetract (Lg : V →ₗ[ℝ] W) (p0 : V) : V →ᵃ[ℝ] W :=\n  Lg.toAffineMap + AffineMap.const ℝ V (-(Lg p0))",
 "chartRetract_apply": "theorem chartRetract_apply (Lg : V →ₗ[ℝ] W) (p0 x : V) :\n    chartRetract Lg p0 x = Lg x + -(Lg p0)",
 "chartRetract_chart": "theorem chartRetract_chart {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w) (p0 : V)\n    (w : W) : chartRetract Lg p0 (chart L p0 w) = w",
 "chart_chartRetract": "theorem chart_chartRetract {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w) {p0 x : V}\n    (hx : x ∈ Set.range (chart L p0)) : chart L p0 (chartRetract Lg p0 x) = x",
 "bodyR": "def bodyR (L : W →ₗ[ℝ] V) (p0 : V) (Ω : Set V) : Set W := chart L p0 ⁻¹' Ω",
 "effR": "noncomputable def effR (L : W →ₗ[ℝ] V) (p0 : V) (e : V →ᵃ[ℝ] ℝ) : W →ᵃ[ℝ] ℝ :=\n  e.comp (chart L p0)",
 "effR_apply": "theorem effR_apply (L : W →ₗ[ℝ] V) (p0 : V) (e : V →ᵃ[ℝ] ℝ) (w : W) :\n    effR L p0 e w = e (chart L p0 w)",
 "isBoundaryState_restrict": "theorem isBoundaryState_restrict {L : W →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) {p0 : V}\n    {Ω : Set V} (hΩ : Ω ⊆ Set.range (chart L p0)) {w : W} :\n    IsBoundaryState (bodyR L p0 Ω) w ↔ IsBoundaryState Ω (chart L p0 w)",
 "isEffectOn_restrict": "theorem isEffectOn_restrict (L : W →ₗ[ℝ] V) (p0 : V) {Ω : Set V} {e : V →ᵃ[ℝ] ℝ}\n    (he : IsEffectOn Ω e) : IsEffectOn (bodyR L p0 Ω) (effR L p0 e)",
 "sharpSeed_restrict": "theorem sharpSeed_restrict (L : W →ₗ[ℝ] V) {p0 : V} {Ω : Set V}\n    (hΩ : Ω ⊆ Set.range (chart L p0)) {r : V →ᵃ[ℝ] ℝ} (hr : SharpSeed Ω r) :\n    SharpSeed (bodyR L p0 Ω) (effR L p0 r)",
 "affineSpan_preserved": "theorem affineSpan_preserved {Ω : Set V} {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ Ω, g x ∈ Ω) {x : V}\n    (hx : x ∈ affineSpan ℝ Ω) : g x ∈ affineSpan ℝ Ω",
 "range_preserved": "theorem range_preserved {L : W →ₗ[ℝ] V} {p0 : V} {Ω : Set V}\n    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) {G : Set (V ≃ᵃ[ℝ] V)}\n    (hG : PreservesBody Ω G) {g : V ≃ᵃ[ℝ] V} (hg : g ∈ G) {x : V}\n    (hx : x ∈ Set.range (chart L p0)) :\n    g x ∈ Set.range (chart L p0) ∧ g.symm x ∈ Set.range (chart L p0)",
 "restrictMap": "noncomputable def restrictMap (L : W →ₗ[ℝ] V) (Lg : V →ₗ[ℝ] W) (p0 : V) (g : V ≃ᵃ[ℝ] V) :\n    W →ᵃ[ℝ] W :=\n  (chartRetract Lg p0).comp (g.toAffineMap.comp (chart L p0))",
 "restrictMap_apply": "theorem restrictMap_apply (L : W →ₗ[ℝ] V) (Lg : V →ₗ[ℝ] W) (p0 : V) (g : V ≃ᵃ[ℝ] V) (w : W) :\n    restrictMap L Lg p0 g w = chartRetract Lg p0 (g (chart L p0 w))",
 "chart_restrictMap": "theorem chart_restrictMap {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w) {p0 : V}\n    {g : V ≃ᵃ[ℝ] V} (hg : ∀ w, g (chart L p0 w) ∈ Set.range (chart L p0)) (w : W) :\n    chart L p0 (restrictMap L Lg p0 g w) = g (chart L p0 w)",
 "restrictMap_bijective": "theorem restrictMap_bijective {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w)\n    {p0 : V} {g : V ≃ᵃ[ℝ] V}\n    (hg : ∀ x ∈ Set.range (chart L p0),\n      g x ∈ Set.range (chart L p0) ∧ g.symm x ∈ Set.range (chart L p0)) :\n    Function.Bijective (restrictMap L Lg p0 g)",
 "restrictEquiv": "noncomputable def restrictEquiv {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w)\n    {p0 : V} {g : V ≃ᵃ[ℝ] V}\n    (hg : ∀ x ∈ Set.range (chart L p0),\n      g x ∈ Set.range (chart L p0) ∧ g.symm x ∈ Set.range (chart L p0)) : W ≃ᵃ[ℝ] W :=\n  AffineEquiv.ofBijective (restrictMap_bijective hLg hg)",
 "chart_restrictEquiv": "theorem chart_restrictEquiv {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w)\n    {p0 : V} {g : V ≃ᵃ[ℝ] V}\n    (hg : ∀ x ∈ Set.range (chart L p0),\n      g x ∈ Set.range (chart L p0) ∧ g.symm x ∈ Set.range (chart L p0)) (w : W) :\n    chart L p0 (restrictEquiv hLg hg w) = g (chart L p0 w)",
 "chart_restrictEquiv_symm": "theorem chart_restrictEquiv_symm {L : W →ₗ[ℝ] V} {Lg : V →ₗ[ℝ] W} (hLg : ∀ w, Lg (L w) = w)\n    {p0 : V} {g : V ≃ᵃ[ℝ] V}\n    (hg : ∀ x ∈ Set.range (chart L p0),\n      g x ∈ Set.range (chart L p0) ∧ g.symm x ∈ Set.range (chart L p0)) (w : W) :\n    chart L p0 ((restrictEquiv hLg hg).symm w) = g.symm (chart L p0 w)",
 "autR": "def autR (L : W →ₗ[ℝ] V) (p0 : V) (G : Set (V ≃ᵃ[ℝ] V)) : Set (W ≃ᵃ[ℝ] W) :=\n  {g' | ∃ g ∈ G, ∀ w, chart L p0 (g' w) = g (chart L p0 w)}",
 "seedTransport_restrict": "theorem seedTransport_restrict {L : W →ₗ[ℝ] V} (p0 : V) (r : V →ᵃ[ℝ] ℝ) {g : V ≃ᵃ[ℝ] V}\n    {g' : W ≃ᵃ[ℝ] W} (hgg : ∀ w, chart L p0 (g' w) = g (chart L p0 w)) :\n    seedTransport (effR L p0 r) g' = effR L p0 (seedTransport r g)",
 "hypotheses_restrict": "theorem hypotheses_restrict {L : W →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V}\n    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) {G : Set (V ≃ᵃ[ℝ] V)}\n    {r : V →ᵃ[ℝ] ℝ} {avail : Set (V →ᵃ[ℝ] ℝ)} (hG : PreservesBody Ω G) (hP1 : SharpSeed Ω r)\n    (hK : BoundaryTransitive Ω G) (hV4 : SeedOrbitAvailable G r avail) :\n    (∀ g ∈ G, ∃ g' ∈ autR L p0 G, ∀ w, chart L p0 (g' w) = g (chart L p0 w)) ∧\n      PreservesBody (bodyR L p0 Ω) (autR L p0 G) ∧ SharpSeed (bodyR L p0 Ω) (effR L p0 r) ∧\n      BoundaryTransitive (bodyR L p0 Ω) (autR L p0 G) ∧\n      SeedOrbitAvailable (autR L p0 G) (effR L p0 r) (effR L p0 '' avail)",
 "driveWords3": "def driveWords3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) :=\n  words (Set.range ball3Drive.flow ∪ {ball3Drive.J})",
 "rot3_mem_driveWords3": "theorem rot3_mem_driveWords3 (t : ℝ) : rot3 t ∈ driveWords3",
 "cyc3_mem_driveWords3": "theorem cyc3_mem_driveWords3 : cyc3 ∈ driveWords3",
 "rotX": "noncomputable def rotX (θ : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cyc3 * rot3 θ * cyc3⁻¹",
 "rotX_mem_driveWords3": "theorem rotX_mem_driveWords3 (θ : ℝ) : rotX θ ∈ driveWords3",
 "euler_apply_pole": "theorem euler_apply_pole (ψ θ : ℝ) :\n    (rot3 ψ * rotX θ) ![0, 0, 1] =\n      ![Real.sin ψ * Real.sin θ, -(Real.cos ψ * Real.sin θ), Real.cos θ]",
 "exists_euler_angles": "theorem exists_euler_angles {b : Fin 3 → ℝ} (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) :\n    ∃ ψ θ : ℝ, Real.sin ψ * Real.sin θ = b 0 ∧ -(Real.cos ψ * Real.sin θ) = b 1 ∧\n      Real.cos θ = b 2",
 "exists_word_pole": "theorem exists_word_pole {b : Fin 3 → ℝ} (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) :\n    ∃ g ∈ driveWords3, g ![0, 0, 1] = b",
 "boundaryTransitive_ball3Drive": "theorem boundaryTransitive_ball3Drive : BoundaryTransitive ball3 driveWords3",
 "preservesBody_driveWords3": "theorem preservesBody_driveWords3 : PreservesBody ball3 driveWords3",
 "seedOrbit_ball3Drive": "theorem seedOrbit_ball3Drive {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (hP1 : SharpSeed ball3 r) :\n    seedOrbit driveWords3 r = directionalFamily",
 "isBoundaryState_closedBall_iff": "theorem isBoundaryState_closedBall_iff {x : V} :\n    IsBoundaryState (Metric.closedBall (0 : V) 1) x ↔ ‖x‖ = 1",
 "E4": "abbrev E4 := EuclideanSpace ℝ (Fin 4)",
 "ball4": "def ball4 : Set E4 := Metric.closedBall 0 1",
 "isom4": "def isom4 : Set (E4 ≃ᵃ[ℝ] E4) :=\n  {g | ∃ R : E4 ≃ₗᵢ[ℝ] E4, ∀ x, g x = R x}",
 "preservesBody_isom4": "theorem preservesBody_isom4 : PreservesBody ball4 isom4",
 "boundaryTransitive_ball4": "theorem boundaryTransitive_ball4 : BoundaryTransitive ball4 isom4",
 "finrank_E4": "theorem finrank_E4 : Module.finrank ℝ E4 = 4",
 "zero_mem_interior_ball4": "theorem zero_mem_interior_ball4 : (0 : E4) ∈ interior ball4",
 "og1_infrastructure_core": "theorem og1_infrastructure_core :\n    (∀ (Ω : Set V) (S : Set (V ≃ᵃ[ℝ] V)), PreservesBody Ω S → PreservesBody Ω (words S)) ∧\n    (∀ flow : ℝ → V ≃ᵃ[ℝ] V, (∀ s t, flow (s + t) = (flow t).trans (flow s)) →\n      flow 0 = AffineEquiv.refl ℝ V) ∧\n    (∀ (Ω : Set V) (T : V ≃ᵃ[ℝ] (Fin 3 → ℝ)) (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ),\n      T '' Ω = ball3 → PreservesBody Ω G → SharpSeed Ω r → BoundaryTransitive Ω G →\n      seedOrbit G r = {f | ∃ b : Fin 3 → ℝ, b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1 ∧\n        f = (ballEffect b).comp T.toAffineMap}) ∧\n    BoundaryTransitive ball3 driveWords3 ∧\n    PreservesBody ball3 driveWords3 ∧\n    BoundaryTransitive ball4 isom4 ∧\n    PreservesBody ball4 isom4 ∧\n    Module.finrank ℝ E4 = 4"
}''')
ON_PRINTS = json.loads(r'''[
 "OIBridge.OrbitNormalization.preservesBody_words",
 "OIBridge.OrbitNormalization.preservesBody_driveWords",
 "OIBridge.OrbitNormalization.flow_zero_of_add",
 "OIBridge.OrbitNormalization.isEmpty_drivability_of_finite_orbits",
 "OIBridge.OrbitNormalization.isBoundaryState_tr",
 "OIBridge.OrbitNormalization.hypotheses_tr",
 "OIBridge.OrbitNormalization.seedOrbit_eq_of_normalization",
 "OIBridge.OrbitNormalization.lorentz_of_normalization",
 "OIBridge.OrbitNormalization.isBoundaryState_restrict",
 "OIBridge.OrbitNormalization.affineSpan_preserved",
 "OIBridge.OrbitNormalization.chart_restrictEquiv",
 "OIBridge.OrbitNormalization.hypotheses_restrict",
 "OIBridge.OrbitNormalization.euler_apply_pole",
 "OIBridge.OrbitNormalization.exists_euler_angles",
 "OIBridge.OrbitNormalization.boundaryTransitive_ball3Drive",
 "OIBridge.OrbitNormalization.seedOrbit_ball3Drive",
 "OIBridge.OrbitNormalization.isBoundaryState_closedBall_iff",
 "OIBridge.OrbitNormalization.boundaryTransitive_ball4",
 "OIBridge.OrbitNormalization.finrank_E4",
 "OIBridge.OrbitNormalization.og1_infrastructure_core"
]''')
ON_PREAMBLE = json.loads(r'''"import OIBridge.OrbitGeneration\nimport Mathlib.Analysis.InnerProductSpace.Projection.Reflection\nimport Mathlib.Analysis.InnerProductSpace.PiL2\nimport Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse\nimport Mathlib.LinearAlgebra.Basis.VectorSpace\n\nnamespace OIBridge\nnamespace OrbitNormalization\n\nopen Set KInfFoundations OrbitGeneration\n\nvariable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]\nvariable {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W]\n"''')
NAMED = ('PreservesBody', 'SharpSeed', 'BoundaryTransitive', 'SeedOrbitAvailable')
CONTROL_TRANSITIVE = {'boundaryTransitive_ball3Drive', 'boundaryTransitive_ball4'}
CONTROL_PRESERVES = {'preservesBody_driveWords', 'preservesBody_driveWords3', 'preservesBody_isom4'}
VERDICT = 'og1_infrastructure_core'
SOURCING_NAME = re.compile(r'(substratum|ellipsoid|scInf|SCInf|stageConsist|ELEM|elementaryDrivability_of|'
                           r'dim(ension)?Three|sourced|seedOrbitAvailable_of|sharpSeed_of_stage)')
SOURCING_PROSE = re.compile(r'(OI (supplies|derives|sources)|is sourced|are sourced by|derives? the drive|'
                            r'sources? (the|a) (seed|drive|dimension))', re.I)
DISCLAIMER_ON = 'Nothing here is a hypothesis about OI.'
DISCLAIMER_OG = 'proved\n  nowhere in the corpus'

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
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


def blob(text):
    data = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def suffix_sha(text):
    i = text.index('\nimport ') + 1
    return hashlib.sha256(text[i:].encode('utf-8')).hexdigest()


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def decl_texts(text):
    """theorem/lemma: signature up to the first ' :=' ; def/abbrev/structure/instance: the declaration whole, up to
    the next blank line followed by a doc comment, a section marker, a declaration, '#print' or 'end'."""
    out = {}
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend '):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            chunk = chunk[:j] if j != -1 else chunk
        out[m.group(2)] = chunk
    return out


def split_statement(stmt):
    """(binders, conclusion) at the first colon at bracket depth 0 after the name."""
    i = len(stmt.split(None, 2)[0]) + 1 + len(stmt.split(None, 2)[1])
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


def module_checks(og, on, tag=''):
    check('L', 'OrbitGeneration is the frozen blob' + tag, og is not None and blob(og) == OG_BLOB)
    check('L', 'OrbitGeneration suffix from the first import is the design-validated suffix' + tag,
          og is not None and suffix_sha(og) == OG_SUFFIX_SHA256)
    if on is None:
        check('N1', 'OrbitNormalization present' + tag, False)
        return
    check('N1', 'OrbitNormalization declares exactly the frozen declarations' + tag,
          [list(x) for x in decls(on)] == ON_DECLS)
    check('N2', 'the preamble (imports, namespaces, open, variable) unchanged' + tag,
          '\n/-! ### §A' in on and '\nimport ' in on and preamble(on) == ON_PREAMBLE)
    texts = decl_texts(on)
    bad = sorted(n for n in ON_TEXTS if texts.get(n) != ON_TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s' % (tag, (' (changed: %s)' % ', '.join(bad[:4]))
                                                                        if bad else ''), not bad)
    for name, text in (('OrbitGeneration', og or ''), ('OrbitNormalization', on)):
        c = code_only(text)
        check('N3', '%s has no sorry, admit, axiom or native_decide%s' % (name, tag),
              not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', on, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in ON_PRINTS))
    kinds = dict((n, k) for k, n in decls(on))
    check('S1', 'the 4-ball countercontrol is a kernel theorem with axiom prints' + tag,
          kinds.get('boundaryTransitive_ball4') == 'theorem' and kinds.get('finrank_E4') == 'theorem'
          and 'OIBridge.OrbitNormalization.boundaryTransitive_ball4' in prints
          and 'OIBridge.OrbitNormalization.finrank_E4' in prints)
    fin = sorted(n for n, t in texts.items() if 'finrank' in t)
    dimbad = [n for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')
              and 'BoundaryTransitive' in split_statement(t)[0] and 'finrank' in split_statement(t)[1]]
    check('S2', 'only finrank_E4 and the verdict mention finrank; no transitivity-to-dimension statement' + tag,
          fin == sorted(['finrank_E4', VERDICT]) and not dimbad)
    pbw = texts.get('preservesBody_words', '')
    b, c = split_statement(pbw) if pbw else ('', '')
    check('S3', 'preservesBody_words: one PreservesBody hypothesis on the generators, words = subgroup closure' + tag,
          b.count('PreservesBody') == 1 and not any(p in b for p in NAMED if p != 'PreservesBody')
          and c.strip() == 'PreservesBody Ω (words S)'
          and 'Subgroup.closure S' in texts.get('words', ''))
    ok4 = True
    for n, objs in (('hypotheses_tr', ('conjTr T', 'effTr T r', 'T \'\' Ω', 'effTr T \'\' avail')),
                    ('hypotheses_restrict', ('autR L p0 G', 'effR L p0 r', 'bodyR L p0 Ω', 'effR L p0 \'\' avail'))):
        bb, cc = split_statement(texts.get(n, n + ' : '))
        ok4 = ok4 and all(p in cc for p in NAMED) and all(o in cc for o in objs) and all(p in bb for p in NAMED)
    check('S4', 'the transport theorems carry body, seed, automorphisms and available effects together' + tag, ok4)
    viol = []
    for n, t in texts.items():
        if kinds.get(n) not in ('theorem', 'lemma') or n == VERDICT:
            continue
        bb, cc = split_statement(t)
        for p in ('SharpSeed', 'SeedOrbitAvailable', 'ElementaryDrivability'):
            if p in cc and p not in bb and not (p == 'ElementaryDrivability' and 'IsEmpty' in cc):
                viol.append((n, p))
        if 'BoundaryTransitive' in cc and 'BoundaryTransitive' not in bb and n not in CONTROL_TRANSITIVE:
            viol.append((n, 'BoundaryTransitive'))
        if 'PreservesBody' in cc and 'PreservesBody' not in bb and n not in CONTROL_PRESERVES:
            viol.append((n, 'PreservesBody'))
    names = [n for _, n in decls(on)] + [n for _, n in decls(og or '')]
    hdr_on = on[:on.index('-/')]
    hdr_og = (og or '')[:(og or '-/').index('-/')]
    check('S5', 'no sourcing conclusion, name or header claim%s%s' % (tag, (' %s' % viol[:3]) if viol else ''),
          not viol and not any(SOURCING_NAME.search(n) for n in names)
          and not SOURCING_PROSE.search(hdr_on) and not SOURCING_PROSE.search(hdr_og)
          and DISCLAIMER_ON in hdr_on and DISCLAIMER_OG in hdr_og)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and \
        e_text == d_text.replace('import OIBridge.KInfFoundations\n', IMPORT_LINES, 1) and \
        d_text.count('import OIBridge.KInfFoundations\n') == 1


def census_ok(d_text, e_text):
    try:
        d, e = json.loads(d_text), json.loads(e_text)
    except Exception:
        return False
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['name'].startswith(KINF2_FAMILY_PREFIX)]
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
    module_checks(show(commit, OG), show(commit, ON))
    check('I', 'OIBridge.lean is D\'s with exactly the two frozen import lines', imports_ok(show(D, IMPORTS),
                                                                                         show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family', census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def self_test():
    og = git('cat-file', '-p', OG_BLOB).stdout
    on = git('cat-file', '-p', ON_REFERENCE_BLOB).stdout
    draft = git('cat-file', '-p', L_DRAFT_BLOB).stdout
    check('T', 'the candidate blobs and the draft blob are readable', bool(og) and bool(on) and bool(draft))
    check('T', 'the frozen suffix digest is the design-validated draft\'s suffix', suffix_sha(draft) == OG_SUFFIX_SHA256)
    check('T', 'the draft blob is not the landed blob (only the header differs)', blob(draft) != OG_BLOB)
    module_checks(og, on, ' [candidate]')
    base = len(FAILS)

    def must_fail(code, label, og2, on2):
        before, count = list(FAILS), COUNT[0]
        sys.stdout_backup = sys.stdout
        import io
        sys.stdout = io.StringIO()
        try:
            module_checks(og2, on2)
        finally:
            sys.stdout = sys.stdout_backup
        new = FAILS[len(before):]
        del FAILS[len(before):]
        COUNT[0] = count
        check('M', 'mutation %s fails with %s' % (label, code), code in new)

    must_fail('L', 'OrbitGeneration body byte', og.replace('theorem seedOrbit_ball3_eq',
                                                           'theorem seedOrbit_ball3_eq ', 1), on)
    must_fail('L', 'OrbitGeneration header', og.replace('round OG-1', 'round OG-2', 1), on)
    must_fail('N1', 'a removed declaration', og, re.sub(r'\ntheorem finrank_E4[^\n]*\n', '\n', on, 1))
    must_fail('N2', 'a strengthened statement', og,
              on.replace('(hK : BoundaryTransitive Ω G) :\n    seedOrbit G r =',
                         '(hK : BoundaryTransitive Ω G) (h3 : True) :\n    seedOrbit G r =', 1))
    must_fail('N2', 'a changed binder context', og,
              on.replace('variable {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W]',
                         'variable {W : Type} [NormedAddCommGroup W] [InnerProductSpace ℝ W]', 1))
    must_fail('N2', 'a changed definition', og, on.replace('(Subgroup.closure S : Set', '(Subgroup.closure (S ∪ S) : Set', 1))
    must_fail('N3', 'a sorry', og, on.replace('  refine ⟨fun D => ?_⟩', '  sorry\n  refine ⟨fun D => ?_⟩', 1))
    must_fail('S2', 'a transitivity-to-dimension theorem', og,
              on.replace('\nend OrbitNormalization',
                         '\ntheorem dim_of_bt {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (h : BoundaryTransitive Ω G) :'
                         '\n    Module.finrank ℝ V = 3 := sorry\n\nend OrbitNormalization', 1))
    must_fail('S5', 'a sourcing conclusion', og,
              on.replace('\nend OrbitNormalization',
                         '\ntheorem seed_free {Ω : Set V} (r : V →ᵃ[ℝ] ℝ) : SharpSeed Ω r := sorry'
                         '\n\nend OrbitNormalization', 1))
    must_fail('S5', 'a sourcing name', og,
              on.replace('\nend OrbitNormalization', '\ntheorem ellipsoid_of_drive : True := trivial'
                         '\n\nend OrbitNormalization', 1))
    must_fail('S3', 'a stronger G-AUT premise', og,
              on.replace('theorem preservesBody_words {Ω : Set V} {S : Set (V ≃ᵃ[ℝ] V)} (h : PreservesBody Ω S) :',
                         'theorem preservesBody_words {Ω : Set V} {S : Set (V ≃ᵃ[ℝ] V)} (h : PreservesBody Ω S)'
                         ' (h2 : BoundaryTransitive Ω S) :', 1))
    must_fail('S1', 'the 4-ball control demoted', og, on.replace('theorem boundaryTransitive_ball4',
                                                                 'def boundaryTransitive_ball4', 1))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace('import OIBridge.KInfFoundations\n', IMPORT_LINES, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, good_imp.replace('import OIBridge.OrbitNormalization\n',
                                                                                 '', 1)))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(KINF2_FAMILY_PREFIX)][0]
    good = dict(dd)
    good['families'] = dd['families'][:k + 1] + [CENSUS_FAMILY] + dd['families'][k + 1:]
    bad = json.loads(json.dumps(good))
    bad['families'][k + 1]['status'] = 'carried'
    check('M', 'census: the frozen family passes and a changed status fails',
          census_ok(d_cen, json.dumps(good)) and not census_ok(d_cen, json.dumps(bad)))
    return base


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
