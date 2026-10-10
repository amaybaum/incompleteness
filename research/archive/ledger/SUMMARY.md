# Premise ledger — consolidated architecture and obligations (checkpoint 1)

Read-only audit of the corpus at base `0f2687b7` (extracted with `git archive`, every paper diffed equal to
`git show 0f2687b7:<path>`). No repository change; no act, freeze or manuscript implication. This summary states what
the frozen entries establish; it adds no new claim. Source of every statement: the frozen entry named in brackets.

Frozen entries: L-A5 `909ba422` · L-A2 `76802938` · L-A1 `6a2048c8` · L-A4 `4f933b26` · L-A6 `dfe77731` ·
L-A3 `6fd22ff1` · L-HT1 `c32fef3c` · L-HT2 `4a7c2bd2` (= current LEDGER.md). Exact checks:
`checks/edge_area.py` `59612ab9`, `checks/carre_du_champ.py` `049fab1b`.

***

## 1. The architecture the audit found

```
 [R] observable-law representation ──► [B1] observer bridge H-T1 ──► [B2] geometry bridge H-T2 ──► [Z] realization / selection ──► SM, GR, Q-specific claims
```

Beside each arrow, only what is unresolved:

| Arrow | Unresolved obligations |
|---|---|
| R → B1 | **OBS-1**: which observer. R is proved for OBS-M (spatial partition V ⊊ S). B1 is stated on OBS-C (whole current field visible, one retarded copy hidden). No stated map OBS-M → OBS-C. [L-HT1 T-HT1-1; OBS-1] |
| B1 (H-T1) | **O-a/b** projection covariance [P, R_g] = 0 for the observer's actual visible algebra (translations, O_h). **O-d** range descent: a class 𝓗 of hidden conditional laws keeping the projected one-step law range 1 — plus the substrate nearest-neighbour choice, which A3 does not supply. **O-f** self-weight descent p₀ = 0 on 𝓗 (swap counterexample shows it fails for correlated laws). **O-g** derive the companion form for the physical observer, or restate the wave branch on the full resummed kernel 𝒟(λ). [L-HT1] |
| B1 → B2 | none beyond B1 for OBS-C; for OBS-M, isotropy may be reached **without** O-d, O-f, O-g (candidate, unproved) [L-HT2] |
| B2 (H-T2) | **T2-1** projection covariance (= O-a/b). **T2-2** nondegeneracy b ≠ 0 and a gapless real branch of the resummed dispersion on OBS-M. **T2-3** curved case: locally O_h-equivariant, slowly varying kernels → metric field g(x). **T2-4** measure–metric compatibility (invariant density = √det g) so the limit is Δ_g without drift. **T2-5** boundary functional = g-area. **T2-6** curvature from Γ₂ of the same limiting generator, with convergence for prepared families. [L-HT2] |
| B2 → Z | the identification of the extracted g with spacetime geometry is a realization claim [L-HT2] |
| Z → SM/GR/Q | the realization premises of §3, each with its replacement obligation |

***

## 2. The representation core [R] — established, and how little it uses

| Result | Anchor | Substrate premises actually used |
|---|---|---|
| S ⇔ D ⇔ Q_fb (finite stochastic laws = marginals of finite reversible systems = fixed-basis unitary Born laws) | Main.md:526; Lean `finite_horizon_equivalence`, `S_imp_D` | finite visible alphabet (F1, a theorem: Main Lemma 1) and a *constructed* finite representative (F4). No A1-total, A2, A3, A4, A5, A6: bijectivity and finiteness appear in the **conclusion** [L-A2, L-A1] |
| Finite reversible realization of any finite law | Main.md:498 (product-prior response table) | none (exact for real laws; uniform-prior form exact iff rational) [L-A1] |
| Unavoidable hidden predictive memory (pushforward, distinguishability and capacity floors) | Main.md:580; Lean `HiddenMemory.lean` | **determinism only** (proof uses X_{t+1} = function of (X_t, H_t)); injectivity unused [L-A2] |
| Canonical predictive quotient (universality clause) | Main.md:598 | determinism [L-A2] |
| Characterization theorem (non-Markovian ⇔ reversible C1–C4 realization) | Main.md:516 | reversibility as the *definition* of the realization class; physical reading conditional (T-A2-2) [L-A2] |
| Accessible backflow from readback | Main.md:167–170 | C1–C4 + a C4 gap; no substrate premise [L-A1] |

**Headline.** A1 (beyond F1/F4), A2, A3, A4, A5 and A6 are not prerequisites of the generic observable QM
representation. Their content enters when a chosen representative is identified with the physical substratum and
further recurrence, counting, coherence, SM or GR conclusions are drawn from that identification.

***

## 3. Realization / selection [Z] — where each premise does its work

| Premise | Split found | Where its content enters | Replacement obligations recorded |
|---|---|---|---|
| **A1** finiteness | F1 visible (theorem) · F2 boundary layer (the one interpretive premise: E3 as dimension cutoff) · F3 total (gauge for accessible-time content only) · F4 representation (theorem) · F5 recurrence · F6 counting | recurrence-scale P-indivisibility, readback ⇒ global indivisibility, counting-measure selection, GSL | infinite deep sector: replace recurrence-scale results by accessible-window statements (strictly weaker), normalizable measure; O-A1-1: finite + counting measure ⇒ all exact probabilities rational [L-A1] |
| **A2** bijectivity | A2a determinism · A2b injectivity · A2c recurrence (= A2b + A1) | permutation unitary as the substrate's own dynamics; recurrence; uniform-on-cycle measure; double stochasticity (+ uniform prior); CP-indivisibility; classical side of the ħ calibration (microreversibility); Page-curve cycles; GSL unitality | **A2-GR**: stochastic microreversibility P(x,y) = P(Θy,Θx) + T-even coarse states; **A2-EV**: deterministic non-invertible = A2 on the eventual image + registered history lies there [L-A2] |
| **A3** locality | A3-D bounded degree (= A3) · A3-R range on G_φ (definitional) · A3-CONE (theorem) · A3-NN (not A3) · PG polynomial growth (not A3) · A3-OBS (open) | cones, Bell–lattice obstruction, observer selection (A3-CONE); boundary-only lemma (A3-R); dimension (A3-D + PG); Lemma 1 support, H-T1 (A3-NN / A3-OBS) | PG as explicit premise; area law: specify state class and prove proportionality; re-found area on the generator geometry [L-A3] |
| **A4** center independence | A4-T translation · A4-S no self-coupling · A4-P partition-center (book only) | A4-T → observer covariance via Theorem 1a (given projection covariance); A4-S → wave form, C = 0, chirality (Theorem 3), masslessness | self-weight descent theorem on a hidden-law class (O-f) or an explicit observer premise [L-A4] |
| **A5** linearity | substrate route (A5 → form lemma) vs observer route (Koopman projection; A5-free, conditional on H-T1) · structural part exact, realized bijection has bounded chaotic nonlinearity used for ergodicity | SM selection (wave form on the substrate route, §4.4 matrix branch, U(1) stripping, Gaussian measure); Main's coherence cluster (realization-specific, not load-bearing); G2 weak field; ν-magnitude ω⁴ measure | discharge on the observer route iff H-T1 holds for nonlinear φ; amplitude gauge as observer redundancy without the circular route [L-A5] |
| **A6** background independence | A6-COV covariant link data (near-definitional) · A6-GRAPH state-dependent graph (separate principle) · H-Bell · A6-EMERG (interpretive) | local gauge reading (H-link/H-cust branch); Einstein reconstruction; Bell completion | Wilson dynamics, not only gauge invariance; A6-GRAPH reuses A4-S (descent gap); H-Bell blocked upstream by T-A6-2 [L-A6] |

Gravity ladder by A5/A2 dependence: **G1** (ħ, ε = 2l_p, area law, 1/4) A5-free as declared, but A2-dependent at one
step (classical rate-ratio slope = β_E, T-A2-1); **G2** weak field A5-transitive (harmonic boundary modes); **G3**
open; **G4** partly A5-transitive (ω⁴ measure), Page curve replaceable by any energy-conserving bijection
[L-A5, L-A2].

***

## 4. Cross-ledger issues

**OBS-1 — three observer notions.** OBS-M (Main: spatial partition, hidden memory, C1–C4) · OBS-C (field/companion:
whole current field + one hidden lag; degenerate point of OBS-M) · OBS-∞ (continuum: long-wavelength sector of the
resummed kernel). Rule: no result transfers between notions without a stated map. R is proved for OBS-M; H-T1 for
OBS-C; H-T2 may reach OBS-∞ from OBS-M directly (candidate).

**One-geometry finding (exact checks).** On the cubic substrate the combinatorial objects are crystalline — hop metric
ℓ₁ (corpus, T-A6-2), edge-boundary "area" ∫‖n‖₁dA with ratio 1 : √2 : √3 for normals (1,0,0), (1,1,0), (1,1,1)
(`edge_area.py`, exact) — while the generator objects are isotropic — dispersion symbol ℓ₂ (corpus), carré du champ
Γ(k·x, k·x) = ‖k‖₂²/(2d) (`carre_du_champ.py`, exact for five k). The audit therefore *indicates* a generator-first
repair: metric, Laplacian, area and curvature read from one observer generator. Recorded as a conclusion of the audit,
not adopted as an axiom.

**Control axes known so far** (for any later level; nothing run): A5 (linearity) · A4-S (self-coupling) · hidden-law
class (product vs correlated preparations; drives O-d, O-f) · observer notion (OBS-M / OBS-C). RECORD's nonlinear and
majority controls differ from the linear control in A5 **and** A4-S; RECORD's leap rules all satisfy A2 (the
second-order form is bijective for every F), A3-NN (d = 1) and A6 trivially. Candidate orthogonal rules recorded in
the ledger (held).

***

## 5. Claim/evidence and drift items (record only; none harmonized)

| ID | Site(s) | Item | Kind |
|---|---|---|---|
| T-A1-1 | Substratum.md:262; Main.md:706 | transfer corollary extends gauge-class transfer to recurrence-scale P-indivisibility and equates it with accessible backflow, contrary to Main.md:604, :174 | claim/evidence |
| T-A2-1 | GR.md:669 vs :68–74 | stochastic-substratum universality of ħ omits the classical-side microreversibility condition | claim/evidence |
| T-A2-2 | Main.md:62 vs :526 | characterization "conditional on finite reversible dynamics" — physical reading conditional, law-level equivalence not | precision |
| T-A2-3 | Main.md:62; Main.md:502; GR.md:76 | empirical prong of the injectivity dilemma needs the uniform prior and bistochastic observed statistics | scope |
| T-A3-1 | SM.md:118 | mod-q area law "scales as η\|∂V\|" vs a proof giving an upper bound, identically zero in the uniform class | claim/evidence |
| T-A3-2 | SM.md:146 (i),(iii) | \|∂V\| used as area; it is ∫‖n‖₁dA (exact check); not discussed in the corpus | new finding |
| T-A4-1 | Substratum.md:98, :158; book ch02:82, :98 | posit stated as translation invariance (A4-T); wave-equation uniqueness needs no self-coupling (A4-S) | claim/evidence |
| T-A6-1 | SM.md:114; book ch05:147 | "Wilson plaquette action, now derived"; gauge invariance of plaquettes derived, the dynamics not | claim/evidence |
| T-A6-2 | SM.md:140 vs :146 (iv) | Theorem label over a proof stating the result "is not established by the cited chain" | status (§A.30) |
| T-HT1-1 | SM.md:248–250, :274 | the field-theory observer is OBS-C, a degenerate point of OBS-M | scope |
| R1 | Substratum.md:158; book ch02:98; FULL.md:739 | "v = α; α = 1 by relativistic causality" vs SM.md:226–228 | drift |
| R2 | Structure.md:301 vs :219, Substratum.md:268 | necessity via q-gauge vs via amplitude-scale gauge | drift |
| R3 | book ch09:205 | A5 restated at visible-sector level | level crossing |
| R4 | book ch02:84 | A5 without its sharpened-stipulation status | lag |
| R5 | SM.md:306–310 | multi-component linear update: substrate vs observer level ambiguous | level ambiguity |
| R6 | book ch02:78 | A2 without its two-part status | lag |
| R7 | book ch02:76 | A1 derived from Lemma 1 (finite visible → finite ontology) | conflation |
| R8 | book ch09:197 | total finiteness treated as physical | drift |
| R9 | book ch09:203 | A4 restated as partition-center independence | third meaning |
| R10 | book ch05:97 | substrate A4-S equated with emergent chiral symmetry | level crossing |
| R11 | SM §3 title; Explainer.md:882 | "background independence" without a sense | loose usage |
| R12 | Main.md:734 | cone property attributed to "bounded coupling degree" | attribution |
| R13 | SM.md:1358 | Theorem 22's C1 proof invokes nearest-neighbour coupling; connectivity suffices | over-assumption |

These are inputs for a future §A.25 propagation round under owner direction.

***

## 6. Not yet audited

- **G clauses** (selective branches, record sector, forgetful sum, unit, composition, invasiveness), **R4-MEASURED-
  EFFECT**, **E1–E7** (empirical inputs) — next ledger families.
- G1's A5-freedom is declared, not line-checked (GR.md:675 has no theorem-style proof).
- The book mirror was checked only for the premises audited.
- Level 3 design is held until the G/R4/E families are ledgered.
