# Audit — `research/equivalence`, round 5 (head `3a46b811`)

Coordinator's audit of the equivalence thread's round-5 report (node E19; E20–E22 deferred to round 6 by the owner's
direction of 10:38Z, their partial work committed and labelled work in progress), from the round-4 head `ab6788b9`,
against the certified base L = `9f9f8257`. Method as in rounds 1–4, plus the owner's round-5 checks (the generated group
and the reachability statement derived or contained; the two directions of every equivalence apart). Evidence levels:
[K] kernel at L; [D] design module built in CI on a disposable branch (not certified); [X] exact computation;
[W] written; [L] literature; [A] audited record.

## 1. Receipts

HO-27, HO-30, HO-31, HO-32, HO-33, HO-34, HO-35, HO-36, copied into `inbox/` at `6362fea4`: 8/8 byte-identical to the
overview's files at `4c4a02b1`.

## 2. Provenance

- Sixteen commits `ab6788b9..3a46b811`, all by `Claude (research equivalence)`; every changed path is under
  `research/equivalence/`. `RESULTS.md` is append-only across them.
- Dev branch `dev-equivalence/r5-design`: `7dd71a7e` (one commit on L), `f67da967` (one on `7dd71a7e`), `f0c36cf9` (one
  on `f67da967`); changes only under `verification/lean-mathlib/`. The committed module texts are byte-identical to the
  dispatched ones (`EqvK2Generation`, `EqvK2Block`, `EqvOneDictionary` at `f0c36cf9`; the dispatch-1 texts kept as
  `.run38124464622.lean` at `7dd71a7e`). The carried modules are byte-identical to their sources: `EqvK2Schema`,
  `EqvK2Converse` to this thread's round-4 modules; `BridgeDictionary`, `BridgeConverge` to `research/bridge` @
  `a34d20b5`.
- The interruption of 08:34Z: the recorded `NOTES-E20.md` (`96e95bc5`, written 08:26:43Z) is the version first
  committed (`4cee1af6`); S0-b was appended later and a one-line work-in-progress status inserted at close. The recorded
  `experiments/e20_odd_bodies.py` (`5743149f`, 08:30:53Z) was never committed: it was edited before E20's run 1. Its
  text is reconstructed from the thread's transcript (the `Write` at 08:30:53Z; digest `5743149f`, equal to the record)
  and preserved as `equivalence/thread-scratch/e20_odd_bodies.draft-0830.py`; applying the four logged `Edit`s
  (10:16:57–10:17:09Z) and the one `sed` (10:17:17Z) to it reproduces the committed run-1 script exactly (`4f1a4739`).
  E20 is deferred and relied on for nothing.
- `LOG.md` is not append-only in two commits: `a047ee43` and `1329adc9` rewrite three timestamps that had been written
  ahead of the clock (10:37Z → 10:34Z; 11:03Z → 10:58Z, twice — the 11:03Z entries were committed at 10:58:33Z). A
  word-level diff shows only the timestamps changed. The thread reports these as "corrected at or before commit"; two of
  the three were corrected one commit later (finding F-E5-1, §9).
- Logged deviations, checked: an extraction loop wrote four overview files not authorized for this round to the
  session scratchpad (not to any worktree) and deleted them; E20 run 1's `.err` had the shell wrapper's `exit 1` line
  removed (a deferred node's kept run record); a debugging pass on a scratch copy of the E20 probe; `EqvOneDictionary`
  built in dispatch 2 because it was queued before the narrowing.

## 3. Replays

`e19_s6_controls`, `e19b_block_controls`, `e8_cite_check` replay byte-identically (stdout); the first and third read the
kernel and the thread's documents by relative path and were re-run from a full export of `3a46b811`
(`equivalence/REPLAY-LOG.txt`). `e20_odd_bodies` has no final output (deferred; its two runs are kept as `.run1`,
`.run2`).

## 4. Independent check

`equivalence/indep_checkE5.py`, decision rule fixed in its header before run 1; reads nothing the thread wrote; matrix
level with the kernel's conventions (the gate `blockdiag(1, X)` — the module's `cnotMat_eq` states this form, read as a
statement — token operations `1 ⊗ U`, the flow `1 ⊗ diag(1, w)` at every unit `w`, the cyclic operation `1 ⊗ U_c` with
`U_c : X → Y → Z → X`); exact (Fractions, sympy). Run 1: **INDEP-E5-FIXED**, Z1–Z7 PASS, CC1–CC6 all False; replay
identical. What it establishes:

- **Z1, the generation words, for all angles (symbolic).** `U_c` acts as `(x, y, z) ↦ (z, x, y)`, `U_c³ = −1`,
  `U_c† = −U_c²`; Euler `[[p, −q̄], [q, p̄]] = diag(a, ā)R(c, s)diag(b, b̄)`; `diag(z, z̄) = z·diag(1, z̄²)` (a flow phase up
  to a scalar); `R(c, s) = U_c† diag(c − is, c + is) U_c`; the controlled-diagonal word
  `CNOT·L(diag(r, r̄))·CNOT·L(diag(r̄, r)) = blockdiag(1, diag(r̄², r²))`; the controlled real rotation by conjugation with
  idle cyclic lifts; `blockdiag(U₀, U₁) = blockdiag(1, U₁U₀†)·blockdiag(U₀, U₀)`. Countercontrols: without the gate the
  controlled-diagonal word is the identity (CC1); without the cyclic lift the diagonal pair is not a real rotation (CC2).
- **Z2, end to end, exactly.** For three pairs `(U₀, U₁) ∈ SU(2) × SU(2)` built from rational points, the explicit
  19-factor product of generator matrices (the gate, flow phases, the cyclic lift and its inverse `−L(U_c)²`) equals
  `blockdiag(U₀, U₁)` exactly — exact finite words, no closure, as G states.
- **Z3, necessity.** Conjugation by the gate, the flow and the cyclic lift preserves the characteristic polynomial of
  six exact Hermitian matrices: `Q3` is invariant (the direction `Q3_cnot` + `Q3_aMiss`).
- **Z4, sufficiency chain.** Six exact pure states (entangled, product, one zero block) are each reached from a product
  by an element of `H = blockdiag(SU(2), SU(2))`: with H1 and `H`-invariance every pure state, hence `Q3`, lies in `K`,
  and H3 gives `K ⊆ Q3` [W].
- **Z5, the group.** The determinant ratio is `−1` on the gate and `1` on the flow, the cyclic lift and `H`: the
  clause's operations lie in `U(1)H` (G′), the gate does not (CC4).
- **Z6, the hypotheses' witnesses.** `−Q3` misses a product (H1 fails; invariant and self-dual); the half-space
  `{tr ≥ 0}` holds products and is invariant but two of its elements pair `−1/2` (H3 fails) (CC5, CC6).
- **Z7, the finite-order part and the dense form.** `⟨CNOT, 1 ⊗ diag(1, i), 1 ⊗ U_c⟩` is finite of order **384**
  modulo phase — the order of the thread's `G₃₈₄`, confirmed independently — and does not contain
  `1 ⊗ diag(1, (3 + 4i)/5)` (CC3); `(3 + 4i)/5` has no power 1 up to 1000; `cos θ₀ = 3/5` lies outside Niven's list, so
  `θ₀/π` is irrational (the density half of DENSE(θ₀) stays [L], as the thread records).

## 5. Citations

`cite_check_r5.py` over the thread's added text (inbox excluded): 88 distinct citations. 78 resolve at L (one window
miss read by hand: the citing line names `SingletonFaces` at KInfFoundations.lean:139 and `RelStrictConvex` at :144,
both correct); nine are module-internal references to design modules (`EqvK2Schema` ×3, `EqvK2Converse`, `EqvOmega4`
×2, `EqvPowerCone`, `EqvTransport`, `CmSprime.lean:1067` = `theorem_Sprime_ineq`), each resolved against the thread's
or countermodels' committed module; one is the thread's checker's own countercontrol string (`NoSuchModule.lean:1`),
excluded. 87/87.

## 6. CI

Three dispatches, verified at job and step level from the saved job logs (`CI-RUNS-R5.md`): `38124464622` @ `7dd71a7e`
Build failure in `EqvK2Block` (6 `sorryAx` prints); `38132266383` @ `f67da967` Build success, six design modules 93/93
standard, `lean-axioms` 5949 with no sorry, gate red only at `lean-manuscript` (6 problems); `38134245361` @ `f0c36cf9`
Build success, `EqvK2Generation` 12/12 standard, `lean-axioms` 5961, gate red only at `lean-manuscript` (7 problems). 33
jobs each, 32 success. None cancelled. The gate counts distinct short names: the six modules' 93 prints have 89
(5860 + 89 = 5949; + 12 = 5961).

## 7. Lean statement review (E19)

- `blockInvariant_of_drive`: hypotheses — invariance under the kernel's `cnot` (CompositeDimension.lean:775) and, for
  every real `t`, under `actT (rotLin t)` and `actT cycEquiv` (KInfFoundations.lean:386, :416); conclusion
  `BlockInvariant K`. No H1, no H3, no closure; the proof composes conjugation invariances along explicit words.
- `reachPure`: no hypothesis; a theorem about the drive words applied to products (`driveOrbit`), from `reach_block` and
  `blockInvariant_of_drive` applied to the orbit set. S6's `ReachPure` is a theorem, not a premise.
- `pairCone_eq_Q3_of_drive_exact`: H1 ∧ H2 ∧ H3 ∧ A_miss ⇒ `K = Q3`, through `pairCone_eq_Q3_of_block`.
- `pairCone_eq_Q3_iff_drive_exact`: given H1 and H3, `K = Q3 ↔ H2 ∧ A_miss`; `→` by `Q3_cnot` with `Q3_aMiss` (no use of
  H1 or H3), `←` by the sufficiency theorem. Each direction has its own witness (§A.34). The objects are the kernel's
  own (`cnot`, `actT`, `rotLin`, `cycEquiv`, `dualW`, `Q3` via the dictionary), not surrogates.

## 8. Hypothesis classification and reading

H1 is the products clause of I3.43 (assumed); H2 (I3.148), H3 (I3.149) and A_miss (the (b)-instance for the clause's two
operations, I3.165 with I3.150 and I3.153) are introduced, not OI premises; `ReachPure` is derived; DENSE(θ₀) is a
mathematical fact [L] in the one-angle form only. Reading: invariance throughout; no availability statement is made or
implied. The strongest justified equivalence, at the audited scope (pair cones over two copies of `eball 3`, the kernel's
gate and the clause's operations, at L): given H1 and H3, `K = Q3` ⟺ H2 ∧ A_miss [D]. The forcing conditions do not
contain the conclusion: H2 and A_miss mention no positivity, no `Q3`, no pure state and no reachability; the transitivity
of `H` on pure states from products is a theorem [D], confirmed independently (Z4).

On the owner's distinctions: exact generation (every angle, exact finite words, no closure) and dense control (one
irrational angle: invariance under its powers, closedness from H3, continuity, and DENSE(θ₀) [L]) are kept apart in the
statements, and the finite-order parts alone do not force `Q3` (`K384`, `K768`, `KC`), definitive for those groups and
cones only. E19 does not derive the drive: whether A_miss (and H2, H3) follow from the complete OI framework is the open
question it isolates.

## 9. Findings

- **F-E5-1 — LOG timestamps edited in place (process).** Three entries were written with times ahead of the clock and
  later rewritten in place; only the timestamps changed. No result depends on them; the LOG's append-only discipline is
  to be kept by appending corrections, as the other threads do.
- No finding on the mathematics. Observation: the order 384 of `⟨CNOT, 1 ⊗ S, 1 ⊗ U_c⟩` modulo phase is confirmed
  independently (Z7).
- No label changes: R-E19.1 … R-E19.6 and R-CITE.5 CONJECTURE as recorded.

## 10. Carried to round 6 (equivalence)

- E20 (odd-`d` residual), E21 (transport passage), E22 (one dictionary): deferred, work in progress, unverified.
- The sources of H2, H3 and A_miss — the open pair-level content E19 isolates; cross-thread: the bridge's transfer clause
  gives A_miss for a class containing the drive (`aMiss_of_transferClause` [D]), and origin's O14-N1 proposes a limit
  route for the drive (audited separately).
- Handoff proposals HP-equivalence-14 … 17 await issue at the round's close.
