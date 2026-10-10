# NOTES-E6 — H-Bell, H-∞ and Level III, bounded exactly

Base L = `9f9f8257`. For each: what is proved at L, the scope gap, and the statement at L that is scope-correct. No new
probe was run for this node; every kernel citation is re-read at L.

## 1. H-Bell (ROADMAP :67, :953–969)

**What the row is.** Not a statement about operational Bell correlations of quantum composites. Quoted (ROADMAP
:957–959): "H-Bell requires the preparation-indexed state-dependent graph family to preserve operational no-signaling
**and** to satisfy a curvature/metric convergence condition strong enough for the Ollivier–Ricci continuum step the
Einstein reconstruction uses." The manuscripts' own enumeration (`papers/Substratum.md:132`, quoted in HB-1's control
plane) adds the ontic parameter dependence the graphs must supply. Upstream of it (:961–966): "for the degree-6 cubic
reference graph the intrinsic hop metric is exactly `ℓ¹` … so the hop-metric curvature route fails for the reference
family **before any Bell edge is added**."

**What is proved at L.** No kernel object. The H-Bell round HB-1 froze a type-P control plane on the obligation's shape
(`verification/programmes/oi-qm/h-bell/round-hb-1-obligation-shape/preregistration.md`, merged under §A.37) and was never
executed; under §A.37 a question left frozen and unexecuted is taken up by a new native round citing it.

**Scope gap.** H-Bell is a substratum/gravity obligation: a Bell-inclusive completion of the *substratum* with curvature
stability. The operational side of Bell correlations is K2's: in the finite characterization composites are tensor
products by construction (complex matrix carriers in the types), so Bell-violating states and effects exist there by
the type; field-neutrally, whether they exist is decided by the pair cone (K2(b)): the product cone admits none, `Q3`
does (the Bell table `phiW` with sharp effects — standard [L], and the dictionary is exact, k2c P1 [A]). ROADMAP :1006
records that K2 does not discharge H-Bell.

**Scope-correct statement at L.** "The finite OI→QM characterization (`oiPlus_iff_qm`, CarrierGeneralOIPlus.lean:207)
is stated over complex matrix carriers whose composites are tensor products by type; it contains Bell-violating
composite statistics as a property of those carriers. Whether the substratum realizes them by preparation-indexed graphs
that preserve operational no-signalling and satisfy the curvature stability the Einstein reconstruction uses (H-Bell) is
OPEN; Bell-inclusive full-substratum uniqueness is not established." An OI–QM equivalence statement carries H-Bell
only if it claims a Bell-inclusive substratum completion; the operational Bell content sits with K2.

## 2. H-∞ (ROADMAP :70, :936–951)

**What is proved at L [K].** The quasilocal completion: the local algebra of finite-region observables, its C*-norm
completion equal to the closure of the union of the stages; every consistent family of finite-region density matrices
extends uniquely to a state (`quasiState_unique`, QuasilocalAlgebra.lean:879); the reversible finite-range update extends
to an isometric *-automorphism; finite-support instruments of the completion are exactly the per-region Kraus
instruments (`finiteSupport_iff_kraus`, InstrumentCompletion.lean:195, both directions proved separately in the kernel);
finite-region availability does not give infinite-support availability (`q3_countermodel`, InstrumentAvailability.lean:335);
discrete dynamics does not determine a continuous interpolation (`continuous_extension_not_unique`, RegionLimit.lean:296);
region inclusion is `X ↦ X ⊗ 1` (`inclObs`, RegionLimit.lean:102).

**Scope gap.** No theorem promotes the *whole* finite characterization — composites, dynamics, selection — to
infinite-dimensional or QFT systems. The quasilocal construction's stages are complex matrix algebras by construction, so
every infinite-system statement sits downstream of the K row (HINF-REVIEW point 3 [A]); infinite-support instruments
are a separate, deliberately unprioritized question (:945–947, :1426–1427), and Hilbert-space representation selection
and the continuous-time generator are set aside with reasons (:1428–1434).

**Scope-correct statement at L.** "Finite-carrier results only: OI⁺ ⟺ exact finite operational QM on every nonempty
finite carrier (`carrier_general_oiPlus`, CarrierGeneralOIPlus.lean:213); on the quasilocal lattice system built from the substratum's finite-region
matrix-algebra stages, states extend uniquely, the dynamics extends, finite-support instruments are exactly the
per-region Kraus instruments, and the completion is unique up to canonical isomorphism among systems with those stages
(§3). No statement is made about infinite-dimensional or QFT systems beyond this lattice completion, about
infinite-support instruments, or about a continuous-time generator."

## 3. Level III — a uniqueness, not an iff

**What is proved [K].** `QuasilocalSystem ι Q` (QuasilocalCharacterization.lean, header (2)) is defined independently of
the construction but **with the complex matrix algebras of the region configurations in its definition** (a unital
star homomorphism from `Matrix (Conf Λ Q) (Conf Λ Q) ℂ` for every finite region). Quoted:

```lean
theorem canon_unique (g : Quasilocal ι Q → S.A) (hg : Continuous g)
    (hst : ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), g (stage Λ X) = S.st Λ X) :
    g = canon S                                                   -- :359
theorem systemEquiv_dyn (T T' : OISystem ι Q) (hΦ : T.Φ = T'.Φ) (y : T.A) :
    systemEquiv T.toQuasilocalSystem T'.toQuasilocalSystem (T.α y)
      = T'.α (systemEquiv T.toQuasilocalSystem T'.toQuasilocalSystem y)   -- :497
```

The OI region completion is a member of the class, any two members are canonically isomorphic compatibly with the
stages, and two OI systems with the same substratum dynamics are isomorphic compatibly with their automorphisms. This is
uniqueness relative to fixed data — the kind of theorem §A.34 says is not a converse.

**The missing direction, exactly.** From a quasilocal system to the OI_Q conditions. Per region it is cheap *relative to
the matrix-algebra stages*: a member's finite-support instruments on region Λ are the Kraus instruments on `Conf Λ Q`
(`finiteSupport_iff_kraus`), and exact finite QM on a carrier gives OI⁺ there (`oiPlus_of_qm`, CarrierGeneralOIPlus.lean:198,
one direction of `oiPlus_iff_qm`); the glue is an interface definition building a `FiniteOperationalTheory (Conf Λ Q)`
from a member's finite-support instruments (not in the kernel, cost unchecked, HINF-REVIEW's candidate). It presupposes
the complex matrix stages — the K row — so even assembled it would be an iff *between two descriptions that both carry
the quantum kinematics*, not a derivation of them.

**Scope-correct statement at L.** "Level III: among quasilocal C*-systems with the substratum's finite-region
matrix-algebra stages (and, for Target A, its dynamics), the OI region completion is the unique member up to canonical
isomorphism (`canon_unique`, `systemEquiv`, `systemEquiv_dyn`). No theorem derives the OI_Q conditions from membership
in that class; the stages are complex matrix algebras by definition."

## 4. Classification (§A.31)

CONFIRMING (HINF-REVIEW's corrections and §A.34's Level III lesson, re-read against the kernel at L) and ELABORATING
(the separation of H-Bell's substratum content from the operational Bell content that belongs to K2; the exact form of
the Level III converse relative to the matrix stages). No NEW finding.
