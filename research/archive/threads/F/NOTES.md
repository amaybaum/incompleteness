# Thread F running notes (RESULT log)

## 1. KInf1 definition (KInfFoundations.lean:1013-1015 at 6d0abf6b)
KInf1 Ω avail := IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail.
- Conclusion is SEC ONLY. SingletonFaces, RelStrictConvex, CopyNatural are NOT in KInf1.
- relStrictConvex_of_kInf1 (l.1019) takes SF as a separate hypothesis.
- Drivability is an ANTECEDENT: KInf1 is vacuous on non-drivable bodies (bit, square, disk?).

## Early findings (to verify)
- F1: with avail = fullEffects and FiniteDimensional V, SEC holds for every compact convex Ω (supporting
  hyperplane at relative boundary, Rockafellar 11.6) -> drive hypothesis idle. DERIVABLE.
- F2: drivability ⇏ SEC for arbitrary avail: kernel not_kInf1_ball3_unit (l.1089).
- F3 (candidate): D×D (bidisk) with flow (R_t,R_2t), N=flow π, J=swap seems drivable, SEC holds with full effects,
  but SF/RSC fail -> KInf1 ⇏ RelStrictConvex. Needs exact script.
- F4 (candidate): disk (rebit) not drivable: Aut0 = SO(2), every affine automorphism normalizes it (J_off_axis fails).
- F5 (candidate): infinite-dim V, continuous effects: Hilbert-cube × ball3 drivable, SEC fails for continuous
  effects; but fullEffects in Lean are algebraic (no continuity) so not a countermodel to Lean fullEffects.

## Sources read (6d0abf6b)
- KInfFoundations.lean full (1212 lines); KINF-2 result + prereg l.1-320; KINF-1 result; ROADMAP l.971-1034;
  SubstratumSource.lean l.1-200; census l.1295-1313; Main.md:352,538-540; design notes K-INF-DESIGN.md all.
- KInfFoundations is a leaf module: nothing imports it except OIBridge.lean:246.
- ROADMAP l.997-999 still says the corrected SF statement "is planned ... and is not frozen" -> stale after KINF-2
  (KINF-2 froze IsProperOn-based SF). Flag only (read-only thread).

## Findings (verified by argument; scripts pending)
- G1 (NEW): KInf1 truth is drive-independent at both ends: (a) avail=fullEffects + FiniteDimensional => SEC for every
  compact convex Ω (Rockafellar 6.4 + 11.6), drive idle; (b) every compact convex drivable Ω has a boundary state
  (extreme point), so ¬KInf1 Ω {unit} for all such Ω (generalizes not_kInf1_ball3_unit). The drive only restricts scope
  (vacuity on non-drivable bodies). The intended "Naimark step" is not expressible: avail has no structural link to
  the flow; no composite/ancilla/readout vocabulary.
- G2: flow_zero is derivable from flow_add (flow 0 = flow 0 ∘ flow 0, cancel). Redundant field.
- G3: continuity-free exclusions: finite Aut(Ω) => not drivable (flow(t0/m)^m = N, g^m = id, m=|Aut|): covers every
  polytope (all FiniteStage bodies!) and the square gbit. Disk: flow t = flow(t/2)^2 is a rotation; O(2)-conjugate of a
  rotation is R^{±1} = flow(±t) => J_off_axis fails. Both DERIVABLE without continuity.
- G4: KInf1 is vacuous on every finite stage (polytope => non-drivable). Finite-stage evidence cannot bear on KInf1.
- G5: KInf1 ⇏ RSC: bidisk D×D = torus orbitope conv(S^1×S^1) (probe §4 drivable) with full effects.
- G6: orbit route (avail closed under drive group + seed) needs boundary covering; extreme-point transitivity is not
  enough: D×D with seed (2+x1+y1)/4 fails SEC at (e1,0). With RSC as input -> circular with Lemma C.
- G7: compactness load-bearing for (a): ball3×[0,∞) drivable closed convex, SEC fails with full effects.
- G8: infinite-dim + continuous effects: Hilbert cube × ball3 drivable, SEC fails for every continuous family.
  Lean fullEffects are algebraic (no continuity) — not a countermodel to Lean's statement; needs FiniteDimensional.
- G9: typing: Ω∞ (design note §2) lives in [0,1]^{E∞} with product topology, not a normed space; placing it in
  KInf1's normed V with matching compactness needs finite affine dimension = finite predictive rank, which
  Main.md:352 records as NOT proved for the completion.

## Script f_countermodels.py (exact; sympy 1.14.0 + fractions)
- run: `PYTHONDONTWRITEBYTECODE=1 python3 f_countermodels.py` -> "OK -- 39 checks, 8 written notes"; output in f_countermodels.out
- sections CM-RSC, CM-ORB, CM-CPT, BR-FIN, BR-DISK, CM-INF, CM-SIC.
- vacuous `True` checks were converted to labelled notes (not counted).

## More findings
- G10 (NEW): no compact convex body of affine dimension <= 2 is drivable (finite Aut -> exponent argument; infinite
  Aut in dim 2 -> conjugate into O(2), flow members are squares hence rotations, conjugates are R^{±1}). With ball3
  drivable, dim 3 is the sharp threshold. Combined with NB-1's d ∈ {1,3}: drivability removes d = 1 (kernel
  not_drivable_Icc), so drivability + NB-1 give d = 3 (assumption-watch, outside KInf1).
- G11: SIC ball in Δ3 with response effects: drivable body, KInf1 FALSE (kernel response_eq_one_forces l.899 +
  probe §7). So avail∞ cannot be the response family of any fixed finite ontic realization (Main.md:538-540).
- G12: decomposition: in finite dim, SEC(avail) = [B1 supplies O2–O5 for some affine e] + O1 availability. The only
  genuinely open conclusion atom is O1 (membership), coupled to the missing definition of avail∞.

## Status
- LEDGER.md written (N=18, X=0, Y=7, Z=11 for R-phys; all 18 PROVED in the ball3/full control regime).
- Section check tallies verified against f_countermodels.out (39 checks, 8 notes).
