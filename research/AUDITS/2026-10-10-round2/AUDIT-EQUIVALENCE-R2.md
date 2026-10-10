# Coordinator audit — `research/equivalence`, round 2

Thread head `5d266133` (2026-10-10; round-2 commits `d14140db` … `5d266133`). Base L = `9f9f8257`. Audited: the
round-2 rows of `RESULTS.md` (R-AUDIT.1, R-E8.1 … R-E8.7, R-E9.1 … R-E9.4, R-E10.1 … R-E10.4), `NOTES-E8.md`,
`NOTES-E9.md`, `NOTES-E10.md`, the round-2 notes of `LEDGER.md`, `experiments/e8_ktrans_probe`, `e8_cite_check`
(run 3; runs 1–2 kept), `e9_level3`, `e9_dyn_finite`, `e10_k2_schema` (run 2; run 1 kept), the design modules under
`lean/` (`StageSeed`, `CopyCovariance`, `EqvKnDesc`, `EqvLevel3`, `EqvOmega4`, `EqvOmega4.run38090924005`), the
preregistration drafts S1–S4, the receipt in `inbox/`, the handoff proposals HP-5 … HP-7, `LOG.md`.

## Method

1. **Receipt.** HO-2 v1 copied verbatim (sha256 `13abf306…`, equal to the overview file at `62cbb3cf`) and committed
   at `d14140db` with the reliance recorded in `LOG.md`. Protocol satisfied.
2. **Replay.** Five scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 5/5
   (`equivalence/REPLAY-LOG.txt`); stderr differs only by the thread's `exit 0` marker line.
3. **Independent check.** `equivalence/indep_checkE2.py` (own code, reads nothing; decision rule fixed before the
   first run): run 2 **7/7 CONFIRMED**, `INDEP-E2-FIXED`, replay identical. Run 1 (kept) crashed inside the
   coordinator's own harness in X4 before any X4 verdict was printed (the unitary `W` was built with the transposed
   convention `W σ_x W* = n·σ`, so the pair `[W|0⟩, XW|1⟩]` was singular on the first instance); X1–X3 were already
   CONFIRMED in run 1. No thread claim was involved.
   - X1 (E10 L2): `U_J = (1/√2)[[−i, −1], [−i, 1]]` is unitary, `Ad(U_J)` sends `σ_x → σ_y → σ_z → σ_x`, and
     `Ad(1⊗U_J)` equals `actT cyc3` on all sixteen basis tables; `Ad(1⊗exp(−itσ_z/2))` equals `actT R_z(t)` at
     `cos t = 3/5` (exactly, with `e^{it/2} = (2+i)/√5`).
   - X2 (E10 F1): the group generated on `W 3` by `cnot`, `actT R_z(π/2)` and `actT cyc3` has order **384**;
     `φ₀ = (1, 2, 3i, −1+i)/4` is carried to a rank-one (product) table by **no** element, the Bell state by 192;
     every product state has a rank-one table (symbolic in the two Bloch vectors) and `φ₀`'s table is not rank one.
   - X3 (E10 §3): `θ₀/π` is irrational for `cos θ₀ = 3/5` by an exact argument stronger than the thread's
     2000-power check — `(3+4i)/5 = (2+i)/(2−i)` with `2±i` non-associate Gaussian primes of norm 5, so no power of
     `(3+4i)/5` is 1; no `R_z(θ₀)^n`, `n ≤ 3000`, is the identity (exact rationals).
   - X4 (E10 L4): `CNOT (1⊗W) CNOT = P₀⊗W + P₁⊗XWX` symbolically; on three Gaussian-rational states chosen by the
     coordinator (not the thread's instances; `κ = (1+i)/2`, `0`, `2i/√5`) the word `(1⊗W′) CNOT (1⊗W) CNOT` carries
     `(a|0⟩ + b|1⟩)⊗|0⟩` to the target state exactly, with `W` and `W′` unitary.
   - X5 (E10 L5): a PSD Gaussian-rational matrix is an exact sum of four rank-one terms (LDL), and
     `v*ρ(ω)v = ipW(ω, table(vv*))/4` on an instance — the cone step's two ingredients.
   - X6 (E9 M1–M3): over the 6144 monomial unitaries of `M₄` with fourth-root phases, H-DYN holds for exactly the
     96 with a scalar diagonal, which give exactly **24 distinct maps** (the permutation conjugations); the Householder
     reflection `1 − 2vvᵀ/25`, `v = (1,2,2,4)`, is orthogonal and conjugates all 16 matrix units to non-units.
   - X7 (E9 P1, P2, K1): the phase map gives `i·E_01` and conjugation by `Z` gives `−E_01`, while permutation
     transports of `E_01⊗1` have entries in `{0, 1}`; `[E_01, E_10] = diag(1, −1)`; the Jordan–Wigner copies
     anticommute while their even parts commute.
   - Additionally (not in the script, exact sympy session recorded in the audit log): R-E8.6's sum-of-squares identity
     for the gradient gap of `F = ‖x‖⁴ + s⁴` and the Euler identity `∇F(p)·p = 4F(p)` hold identically in the eight
     variables.
4. **Kernel citations.** The coordinator's own sweep (`cite_check_r2b.py`, lines added since `8c67c7fb`) finds 47
   distinct `File.lean:NNN` strings; two are not kernel citations (the design-module error location
   `EqvOmega4.lean:157` and the countercontrol input `NoSuchModule.lean:1`, both quoted from the thread's own
   citation-check output); the remaining **45/45 resolve at L**, 25 with a named identifier found at the line, 17 with
   no identifier named on the citing line, and three whose citing line names a different identifier, inspected and
   correct (QuasilocalCharacterization.lean:769 `phase_localityPreserving`, DenseOrbit.lean:53 `DenseBoundaryOrbit`,
   OrbitGeneration.lean:69 `PreservesBody`). The thread's own `e8_cite_check` (43 distinct, run 3) is consistent.
5. **Design runs** (`CI-RUNS-R2.md`): 38090116254 (`dev-equivalence/kn-desc` @ `05b5756c`): Mathlib bridge Build
   success, 12 prints standard, gate red at `lean-manuscript` only; 38090924005 (`dev-equivalence/omega4` @
   `195dfbee`): Build **failure** at `EqvOmega4.lean:157`, `:215`, gate skipped (the eight built declarations' prints
   standard as the thread records; the repair `95beab2b` is unmeasured); 38091534622 (`dev-equivalence/split-l3` @
   `8c92343e`): Build success (3646 jobs), `StageSeed` 3 + `CopyCovariance` 12 + `EqvLevel3` 4 prints standard,
   `lean-axioms` 5879 no sorry, gate red at `lean-manuscript` only (the dev branches are cut from L, so `claims` and
   `duplicate` pass there). Three dispatches, the cap. Design evidence only; nothing certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| R-AUDIT.1 | [X] (label correction of R-E3.4, R-E5.1) | accepted; the round-1 precision note is acknowledged without editing the old rows |
| R-E8.1 | OPEN (drafts for owner review) | accepted; S1–S4 each carry one `v3-round` and one `v3-governed-paths` block; S4 marked not ready (checkpoint `C0`) |
| R-E8.2 | CONJECTURE [D] | accepted; run 38090116254 verified |
| R-E8.3 | CONJECTURE ([D] partial) | accepted as labelled: the separation stays at [W]+[X] (the coordinator's round-1 curvature check X1 is the independent confirmation of the decisive step); `not_affine_eball_omega4` as a built declaration is thread-reported from the failed run's log |
| R-E8.4 | CONJECTURE [D] | accepted; run 38091534622 verified |
| R-E8.5, R-E8.7 | [X] | accepted; the coordinator's own sweep agrees (above) |
| R-E8.6 | CONJECTURE; CONFIRMING | accepted; the identity recomputed (method 3); the advice to omit "supporting-effect completeness" from HP-1's phrase is recorded in the overview |
| R-E9.1 | CONJECTURE ([D] transfer; [W] OI⁺ link) | accepted; the pressure test (a transfer lemma, not evidence for OI) is the right reading |
| R-E9.2 | CONJECTURE [D]; automorphism level CERTIFIED | accepted; QuasilocalCharacterization.lean:769, :792 verified at L; X7 |
| R-E9.3 | CONJECTURE ([X] + [D]) | accepted; X7 (the commutator and the JW instance) |
| R-E9.4 | CONJECTURE ([W] + [L]) | accepted; X6. Precision: "exactly the 24 permutation conjugations among 6144 cases" counts maps; at the level of unitaries 96 satisfy H-DYN (four scalar phases each). No label change |
| R-E10.1, R-E10.2 | CONDITIONAL (H2, H3, A_miss); CONJECTURE | accepted; X1, X4, X5; the six-lemma proof read lemma by lemma (A_miss enters only in L4; L5 uses the definition of PSD and a Gram decomposition) |
| R-E10.3 | CONJECTURE (unreachability); CONDITIONAL on claim D | accepted; X2 reproduces 384 and the unreachable `φ₀` independently |
| R-E10.4 | CONDITIONAL | accepted; X3 strengthens the irrationality evidence to an exact proof |

**Label changes: none.**

## Recorded for the overview

- Assumption-watch marker (HP-5 item 1): a Level III "iff" must name its right-hand side — with an abstract net it is
  false (K1, K3), with a locality-preserving dynamics it is false (Target B, P2), with the target class it is (C-REG)
  and carries the matrix stages in its premise. Repairing hypotheses: H-FAC, H-UNIF, H-GEN, H-DYN.
- S6's kernel cost revised (HP-5 item 2): no spectral theorem; dictionary + explicit reachability construction.
- A strictly weaker sufficient clause for the K2 schema: `R_z(θ₀)` (`cos θ₀ = 3/5`) and `cyc3` on one token, given H3
  (routed as HO-13); the finite clause fails with an exact unreachable state (routed as HO-14).
- Drafts S1–S3 are at owner-review stage; S4 is not ready to freeze (one dispatch needed for its `C0`).
- Thread deviations disclosed (one root import line per module on each dev branch; `e10` run 1 terminated with no
  output and kept; `e8_cite_check` runs 1–2 kept; dev branches cut from L rather than from the thread branch) — noted,
  no action.
- Routed: HO-13 (equivalence → bridge, origin), HO-14 (equivalence → countermodels); HP-5 recorded here and in the
  overview (not a handoff).
