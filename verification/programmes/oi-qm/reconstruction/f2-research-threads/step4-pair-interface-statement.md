# Step 4 — the combined #829/#823 interface: statement and compiled pair assembly

Base: main `M = 5bfdaba6`. Design commits `5a18db06`…`c9f16498` on the session branch (disposable, not for merge),
children of the disposable design-run commit `22e0d002`. Module:
`verification/programmes/oi-qm/reconstruction/pair-interface-design/PairInterfaceDesign.lean`, namespace
`OIBridge.PairInterfaceDesign`, compiled by `.github/workflows/pair-interface-design.yml` against the landed library
(no adopted file changed). Run 38606560943, job 115998853118, at exact commit `c9f16498`: every step succeeded;
all 27 `#print axioms` reports are `[propext, Classical.choice, Quot.sound]`; the same comparison rejects the compiled
output with `sorryAx` injected into one report and with one report removed; legacy records, receipts and placement
pass. Earlier runs on this branch record the build history: 38601947315 (`5a18db06`) and 38605005576 (`8b2131fb`)
failed at compilation, the first for the unopened `ᴴ` notation and the `BridgeDictionary.pauli` unfolding, the second
for the missing `DenseOrbit` import; the runs between them passed with fewer reports.

Evidence labels as in threads A–E: [K] kernel at M, [D] compiled design (this module, run above, or the
design runs cited), [W] written, [X] exact computation, [U] unsourced.

***

## 1. What step 4 combines

| side | object | source |
|---|---|---|
| cone side | pair cone `K ⊆ W 3`, clauses H1, hadd, hsmul, hmax, gate clauses hH2 (cnot), hA (rotLin, cycEquiv) | `EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone` :153 [K]; k-token form proposed by #829 (no object exists at any head [X: git grep]) |
| matrix side | `ImplementationClass`, `Architecture`, `ContextStable`, `LabelInvariant`, `DaggerStable`, `DrivesElementary`, `QuantumArchitecture` | ImplementationLocality / SubstratumSource [K]; drivability at qubit-power carriers `quantumArchitecture_iff_pow` [D, KnDescentDesign @ d3a95be6, run 38457070337 job 115502431432] |
| interface | carrier identification, common class, admitted repertoire, state–operation compatibility | `argument.md` §6 (research branch) — none supplied at M |
| correlations | availability of preparations, settings, joint protocols | thread E §3, §6 (H-Corr 1–7) |

## 2. The compiled pair assembly [D]

Every statement below has every clause as a premise. Nothing sources drivability, compatibility, availability or
validity.

**(A) Gate admission.** On one token: `phaseMat (cos s) (sin s) = flow (transition 1 1) (−s/2)`
(`phaseMat_eq_flow`); `cycMat = flow(transition 0 0)(π/8) · flow(transition 1 1)(−π/8) · flow(transition 0 1)(π/4)`
(`cycMat_eq_flows`, i.e. `R_z(π/2) R_x(π/2)`). On the pair: `cnotMat = permMatrix (swap (1,0) (1,1))`
(`cnotMat_eq_swap`). With unitarity of each.

**(B) The combined pair theorem.**

```
pairCone_eq_Q3_of_admitted
  (arch : Architecture 𝓘)          -- only `mul` is used
  (hC : ContextStable 𝓘)           -- puts the one-token gates on the target token
  (hflow : ∀ a b : Fin 2, ∀ t, 𝓘 (Fin 2) (flow (transition a b) t))
  (hswap : 𝓘 (Fin 2 × Fin 2) (permMatrix (swap (1,0) (1,1))))
  (hcompat : PairCompat 𝓘 K)       -- H-COMPAT: admitted pair unitaries preserve K through dict
  (hH1 hadd hsmul hmax)            -- the adopted pair theorem's cone clauses
  : K = Q3
```

with corollaries `pairCone_eq_Q3_of_drives` (hflow, hswap from `DrivesElementary`) and
`pairCone_eq_Q3_of_quantumArchitecture`. LabelInvariant, DaggerStable and the quarter phases are not used.
Direction: forward only.

**(C) Controls.**

- Positive: `fullClass_pairControl` — the full class satisfies Architecture, ContextStable, DrivesElementary and
  `PairCompat fullClass Q3` [D]. (Q3's own cone clauses are the adopted round's MAXCONE-EXACT controls, not re-proved.)
- Converse refuted: `diagClass_pairControl`, `not_drives_of_pairCompat` — the diagonal class satisfies all four closure
  clauses and `PairCompat diagClass Q3`, and `¬ DrivesElementary diagClass` [D]. So "K = Q3 ∧ closure ∧ compatibility ⇒
  drivability" is false; no iff is displayed (§A.34).
- Drivability is load-bearing (not compiled): `(substratumClass, K_mono)` satisfies every premise except the off-diagonal
  admissions and K_mono ≠ Q3, via the support-3 element `(1⊗cycMat)·phaseGate(1,1)|++⟩` [X + W, thread B X6].

**(D) Correlations at the pair, availability explicit.** `prep` and `avail` are free parameters, read as the available
joint preparations and the available one-token tests. Nothing at M ties `avail` to stage data: the only kernel notion
of an available physical test is stage membership (`(D.stage i).E`, `stageEffects`), and no theorem connects it to
`avail` (thread G). The content of (D) is therefore conditional on that identification.

```
pair_available_eq_Q3
  (arch) (hC) (hd : DrivesElementary 𝓘)
  (hcompat : PairCompat 𝓘 prep)    -- admitted unitaries carry available preparations to available preparations
  (hprod : products of eball 3 states ∈ prep)          -- product preparations available
  (hadd hsmul)                                        -- mixing available
  (hvalid : prep ⊆ maxConeOf avail)                    -- product tests valid on available preparations
  (hdense : denseTests ⊆ avail)                        -- a countable dense family of sharp tests is available
  : prep = Q3
pair_available_eq_Q3_and_chsh  -- the same, with the eight CHSH tests available (hz hx hp hm)
  : prep = Q3 ∧ ∃ ω ∈ prep, ∃ a a' b b', (each ±-measurement available) ∧ chsh a a' b b' ω = 2√2
```

`denseTests` is DenseOrbit's rational-reflection orbit of the axis test, countable with
`maxConeOf denseTests = maxCone (eball 3)` (`countable_seedOrbit_cone` [K]). The eight CHSH tests are sharp tests
(`chshTests_subset_sharpFamily`); their settings `(x ± z)/√2` lie outside the rational orbit, so they are a separate
premise.

**Counting.** The sharp-family premise `sharpFamily 3 ⊆ avail` is false for every countable `avail`
(`not_sharpFamily_subset_of_countable` [D]: the unit sphere is uncountable and `b ↦ sharpEff b` is injective). Every
stage tower on record is countably indexed (`badD`, `bitTower`, `midD`, PT-STAGE-1's `protocolTower`), so if
"available" means "carried by a stage" that premise fails for all of them (thread G). The counted premises above are met
by the countable family `denseTests ∪ chshTests`, which does not contain the sharp family (`countable_avail_control`).
Exact attainment of `2√2` needs the eight irrational-angle tests; with rational settings only, `2√2` is a supremum.

`marginal_independent`: no-signalling of the marginal, every joint vector, by bilinearity.

What (D) gives that the cone theorem alone does not: with K read as the available preparations, cone equality becomes
**availability of every PSD table** (state-level Q-down), and the CHSH attainment is by an available preparation with
available settings, not by mere membership (AW-E1).

**(E) The quantum reading of the pair's sharp behaviours.** `prodEffVal_sharp_eq_trace`: a sharp-test value is
`tr((Π_a ⊗ Π_b) · dict ω)` with `Π_a = (1 + a·σ)/2`, which is Hermitian, complete (`Π_a + Π_{−a} = 1`) and, for unit
`a`, a projector. `pair_sharp_behaviours`, under the premises of `pair_available_eq_Q3`, with one witness per
direction:

- (Q-up) every available preparation has a positive semidefinite dictionary image, and its sharp-test values are those
  traces — every available two-outcome sharp behaviour of the pair is a quantum behaviour of a two-qubit state
  with projective qubit measurements;
- (Q-down) every positive semidefinite two-qubit operator is the dictionary image of an available preparation — with
  the two settings available, the quantum behaviour at those settings is attained by an available protocol.

What (D)–(E) do not give: the identification of the projectors `Π_a` (unit `a`) with all rank-one qubit projectors is
the Bloch parametrization, used and not proved here; the CHSH upper bound is then the standard quantum bound for
these behaviours, not a kernel theorem; general POVMs, local instruments and post-measurement update (E's G5) and
anything multi-party (G3) are outside the pair clause.

## 3. The finite statement step 4 is building toward (stated, not compilable at M)

Register form, k tokens, matching A's F1-reg and B's L2, with C's KN-DESC hypotheses:

```
kToken_cone_and_descent
  (arch : Architecture 𝓘) (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
  (hpow : ∀ k, DrivesElementaryAt 𝓘 (Fin (2^k)))       -- KN-DESC (#823): with hC, hL, arch this gives DrivesElementary
  (hCAR : carrier identification  dictK ↔ Fin (2^k))   -- H-CAR, introduced, unsourced
  (prep : ∀ k, Set (WK k)) (hcompat : ∀ k, ConeCompat 𝓘 k (prep k))   -- H-COMPAT_k, introduced, unsourced
  (hprod_k hadd_k hsmul_k) (hvalid_k : prep k ⊆ maxConeOfK avail) (hdense : denseTests ⊆ avail)   -- countable
  : DrivesElementary 𝓘 ∧ ∀ k, prep k = QK k
```

- Forward only; the converse is refuted by the same diagonal control at every k [K + W].
- Needs, in build order (B §5): L8 + L3b on a generic carrier; L1-M carrier triangle and `pairCarrierEquiv`; L5 k-token
  intertwinings; #829's `kCone_eq_QK_of_drive_maxCone`; L4′; L7 for carriers that are not powers of two.
- Correlations at k (E §6): with `prep k = QK k` and the k-token dictionary, Q-up for multi-party behaviours follows
  from PSD-ness, not from hmax (AW-E2: maxCone alone is insufficient for n ≥ 3); Q-down needs the availability
  premises H-Corr 2–6, which the k-token form carries as `prep` and `avail`.

## 4. Hypothesis ledger after step 4 (relative to thread A's table and thread C's KN-DESC table)

| hypothesis | role | status at M |
|---|---|---|
| Architecture (mul) | gate words | introduced (closure clause) |
| ContextStable | spectator for one-token gates | introduced; at k only needed off qubit-power carriers (B L7) |
| LabelInvariant | k-token relabelling, descent | introduced; unused at the pair |
| DaggerStable | — | unused by step 4 |
| one-token transition flows, one pair exchange (⊂ DrivesElementary) | off-diagonal control | **unsourced; false for the substratum class** (`substratum_residual`); the continuous family is the resource Arc D and K∞-Drive's `J` name, which the presently stated architecture does not source (frozen-sourcing audit). A Bell violation needs less: particular non-monomial gates and measurement settings suffice, and monomial-only protocols stay within CHSH ≤ 2 (thread E, W6) |
| H-COMPAT (PairCompat / ConeCompat_k) | state–operation compatibility | introduced, unsourced; availability does not imply it (#820 K_B) |
| H-CAR | carrier identification | introduced, unsourced (k ≥ 3) |
| hprod, hadd, hsmul (as availability) | preparations | unsourced |
| hvalid | product-test validity on available preparations | unsourced (#836) |
| hdense, the eight CHSH tests (in place of `sharpFamily 3 ⊆ avail`) | available tests | unsourced; `avail` is not tied to stage data at M. With `avail` tied to stage tests (A's M1), they need A's H11 in two parts (thread G): **H11a** stage tests are available, **H11b** an available operation followed by an available test is an available test. Neither has a predicate at M; the zero value of the seed is load-bearing (`not_seedOrbit_unsharp_eq`) and mixing cannot produce sharp tests (`sharp_eq_of_certain`) |
| A's H23 (cnotI), H24 (aMiss) | gate invariance | derived in (B) from the admissions and H-COMPAT |

Thread G's corrections to thread A's table: reading H13 as "avail = stage effects ∪ seed orbit" makes H11 true by
definition, contrary to its status "introduced"; H10 cites #821's theorem 1 (the single-effect form), not the
existential form; and H10 does not depend on H3. #821 as frozen touches only H10, which is free on the ball
(`sharpEff_sharpSeed`); its composite with `hypotheses_tr` and `sharpFamily_subset_avail` is not frozen.

Classification: consistency work (structural assembly); correctness bands unchanged. NEW at the pair: the gate clauses
of the adopted pair theorem are consequences of drivability + compatibility, and the cyclic clause is exactly what the
monomial class cannot supply (B, k = 2).
