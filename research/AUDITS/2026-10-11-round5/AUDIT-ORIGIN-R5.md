# Audit — `research/origin`, round 5 (head `44c06d46`)

Coordinator's audit of the origin thread's round-5 report (node O14; O15 and O16 carried to round 6 by the owner's
direction of 10:38Z), from the round-4 head `7192e3b5`, against the certified base L = `9f9f8257`. Method as in rounds
1–4, plus the owner's round-5 checks for O14: the generated group established from the permitted operations, exact and
dense generation kept apart, every alternative generating set classified with its disguise test, nothing inferred from
an unbuilt module. Evidence levels: [K] kernel at L; [D] design module built in CI on a disposable branch (not
certified); [X] exact computation; [W] written; [L] literature; [A] audited record.

## 1. Receipts

HO-29, HO-31, HO-32, HO-33, copied into `inbox/` at `acc5fce0`: 4/4 byte-identical to the overview's files at
`4c4a02b1`, and unchanged at `44c06d46`.

## 2. Provenance

- Fifteen commits `7192e3b5..44c06d46`, all by `Claude (research origin)`; every changed path is under
  `research/origin/`. The first, `6a71b2be` (05:21Z), is the post-close record of round 4's two `dev-origin/angle` runs,
  logged as such when round 5 opened (LOG 07:19Z).
- `LOG.md` is append-only across the eleven commits that touch it; `RESULTS.md` is append-only (one commit).
  `NOTES-O14.md` changed in place three times, none of them in the pre-registered text: the S0 block (written
  08:04:30Z, before any run or dispatch) is unchanged; addendum 1 (inserted 11:04:35Z, before dispatch 1 at 11:05:00Z) and
  addendum 2 (11:07:45Z, before the Mathlib bridge job of dispatch 1 started at 11:13:23Z; it raises a Python search
  depth from 10 to 12 and touches nothing in the module) are insertions ahead of the verdict placeholder; the verdict
  (11:29Z) replaces that two-line placeholder. The script `o14_opdrive.py` was written at 11:11:20Z, after both addenda,
  and run at 11:13:18Z.
- The interruption of 08:33Z: `NOTES-O14.md` is identical to the recorded digest (`c5ef134f`) in its first commit
  `9893930e`, and the recorded `LOG.md` is a prefix of the committed one (`interrupt_descent.out`). The six
  `dev-origin-drive` rows of `INTERRUPTION-MANIFEST.sha256` (`dev_descent_origin.out`): `OIBridge.lean`, `BridgeAvail`,
  `BridgeAvailFull`, `OriginAngle` and `OriginTokenOrder` are identical to their recorded digests at every commit of the
  dev branch. `OriginDrive.lean`, the file the thread was appending to when it stopped (recorded `adaf19a2` at
  08:33:36Z), matches no commit and is a prefix of none: the thread revised it in place after resuming. It was rebuilt
  from the thread's own transcript (`dev_replay.py`; the `Write` at 08:21:40Z, two appends, thirteen in-place edits by
  Python heredoc and three `Edit` calls, a fourth `Edit` refused by the tool and not applied): the rebuild matches all
  seven recorded digests — the interruption state `adaf19a2`, the draft `0f0bdbb4` (`f9eabcaf`), the coordinator's safety
  copy in `research/wip-checkpoints` @ `1b2ec2bb` (`03fafb41`, equal to `80909988`), `538dc51d` (`58d639b4`), `78baca7c`
  (`2639b3ce`, dispatched in run 38134267257) and `86358785` (`a1d595ea`, dispatched in run 38135099684)
  (`origin/dev_replay.out`; the events in `origin/TRANSCRIPT-O14-EVENTS.txt`).
- Dev branch `dev-origin/drive`: five commits on L — the draft `0f0bdbb4`, two commits labelled "WIP — unbuilt,
  unverified" (`80909988`, `538dc51d`) made under the owner's checkpoint direction, and the two dispatched heads
  `78baca7c` and `86358785`; changes only under `verification/lean-mathlib/` (five import lines in `OIBridge.lean` and
  five modules). The carried modules are byte-identical to their sources: `BridgeAvail` and `BridgeAvailFull` to
  `research/bridge` @ `a34d20b5` (an authorized cross-branch read, LOG 07:34Z); `OriginTokenOrder` and `OriginAngle` to
  this thread's round-4 modules at `7192e3b5`. The committed `lean/OriginDrive.lean` and
  `lean/OriginDrive.run38134267257.lean` are byte-identical to the modules dispatched at `86358785` and `78baca7c`.
  HP-origin-14's evidence-hash table matches the committed files, 6/6 (`EVIDENCE-HASHES.txt`).
- Logged deviations, checked against the transcript: one launcher failure before run 1 (11:13:08Z: `/usr/bin/time` is
  absent from the container, so the shell exited 127 before Python started; stdout empty, stderr the one-line shell
  error); the two artifacts were removed and run 1 started at 11:13:18Z. One LOG stamp was written ahead of the clock
  (11:31Z at 11:29Z) and is disclosed in the close entry, not edited.
- The coordinator's own write, recorded under §A.26. The first transcript replay (`dev_replay.run1.py`, output kept as
  `origin/dev_replay.run1.out`) re-executed two of the thread's commands that write into the thread's session scratch
  area — `scratchpad/origin-r5/check/names.py` and `names2.py`, name-resolution tooling of a pre-dispatch review, not
  committed anywhere — at 11:48:46Z and 11:48:49Z. Their content is unchanged: the same two transcript commands
  re-executed in a sandbox give identical digests (`d5da912e…`, `79296cd1…`; `origin/names_sandbox_check.py` and
  `.out`); only their modification times changed. The same run applied an `Edit` the tool had refused (11:01:52Z), so its
  last two checkpoints differed. Run 2 skips refused calls and every command that names a path outside the dev tree,
  writes only into its sandbox, and matches all seven digests.

## 3. Replays

`o14_opdrive.py`: IDENTICAL (stdout 3124 bytes, 8 s; stderr empty, as committed). 1/1.

## 4. Independent checks

`indep_checkO5.py` (exact arithmetic in ℚ(ζ₈), its own number class; reads nothing the thread wrote; decision rule in
the header before run 1; one pre-run simplification of a helper, the rule unchanged). Run 1: **VERDICT
INDEP-O5-FIXED** — Z1–Z6 PASS, CC1–CC6 False; replay byte-identical.

- Z1: on `N` configurations the transpositions generate `N!` elements modulo scalars, and with one quarter phase
  `N! · 4^{N−1}` (8 and 1536 at `N = 2, 4`), every element a unit multiple of a `μ₄`-monomial.
- Z2: 400 random lattice protocols (uniform ancilla of size 2 or 4, `μ₄`-monomial isometries, computational-basis
  readout with outcome-dependent continuations, coarse-graining, discard) are trace preserving and keep the coefficient
  `c(Φ) = ⟨0|Φ(|0⟩⟨1|)|1⟩` in the square `|Re| + |Im| ≤ 1`; the drive's coefficient is `w̄`, with `7/5`. The sample is a
  spot check of the written argument, which I confirm: every Kraus operator of a channel composed from the constructors of
  a fourth-root lattice class is a positive multiple of a partial monomial matrix with `μ₄` entries (a member is a
  scalar times such a matrix, and the scalar's phase cancels in `K₀₀ K̄₁₁`), so `c(Φ) = Σ p_K K₀₀ K̄₁₁` is a combination
  of `μ₄` units of total weight at most `Σ p_K |K₀₀|² ≤ 1`.
- Z3: a repeat-until-success protocol built from a **different circuit** than the thread's — `(H ⊗ H)` on the ancillas
  around `Tof · S · Tof · S†`, which is the doubly controlled `iZ` — with the pure ancilla prepared from the uniform
  attachment by readout and conditional flips. Its readout blocks are `(3I + iZ)/4` (weight 5/8, a multiple of
  `V = diag(1, (4 − 3i)/5)`) and three multiples of `S` (weight 1/8 each); with the correction `S†` after a failure the
  `k`-round channel equals `(1 − (3/8)^k) Ad(V) + (3/8)^k id` exactly on the matrix units (`k = 1, 2, 3`), and `S V = D`.
- Z4: `⟨rot(π/4), S, X⟩` has 24 elements modulo phase and contains neither `V` nor `D`.
- Z5: `w = (2 + i)/(2 − i)`; its `(2 − i)`-adic valuation is −1, while every entry of the 24 elements has a power-of-two
  denominator.
- Z6: `⟨T, S, X⟩` has 16 elements modulo scalars, all monomial; `H T` is not monomial and no power up to 200 is scalar.
- Countercontrols, all False: the circuit with `CC(Z)` in place of `CC(iZ)` has a non-unitary success branch
  (`K†K = diag(1, 1/4)`); the drive's coefficient in the square; `V` or `D` in the 24-element group; a nonnegative
  valuation; a sampled protocol outside the square; `H T` in `⟨T, S, X⟩`.

`indep_checkO5b.py` (supplementary, its own decision rule fixed before its run 1): the thread's own circuit and the
identity it cites for `J`. Run 1: **VERDICT INDEP-O5B-FIXED** — Y1–Y4 PASS, DD1–DD3 False; replay byte-identical. Y1:
`uJ` as defined in `BridgeAvail.lean` (lines 80–81) equals `e^{−iπ/4} H S³` exactly, is not monomial, lies in
`⟨rot(π/4), S, X⟩` modulo phase, and `H` lies in `⟨uJ, S, X⟩` modulo phase (both 24 elements): with the quarter phase
of the stated access, the J datum and the balanced mixer generate the same level-one group. Y2: the circuit
`(1 ⊗ H ⊗ H) Tof (S ⊗ 1 ⊗ 1) Tof (1 ⊗ H ⊗ H)` has blocks `((3 + i)/4) zPh` and three multiples of `Z`, with
`K†K = 5/8, 1/8, 1/8, 1/8`. Y3: with the correction `Z`, the `k`-round channel is `(1 − (3/8)^k) Ad(zPh) + (3/8)^k id`
(`k = 1 … 4`). Y4: the same with a spectator qubit, on all sixteen matrix units (`k = 1, 2`). Countercontrols: without
the correction the identity fails; `uJ` is not a multiple of a monomial; with `S` applied unconditionally the success
block is not a multiple of `zPh`.

## 5. Citations

`cite_check_r5.py` over the thread's added text (inbox excluded): 33 distinct citations; 31 resolve at L (15 named in
the window, 8 cite no identifier on the line, 8 window misses — all in row O14-K, whose backticked names belong to other
citations of the same row, read by declaration); 2 cite the bridge's design modules. The thread writes most kernel
citations as lists (`File.lean:268, :305, …`), which that regex does not expand; `cite_expand_r5.py` expands them: 55
citations, 53 resolving at L to the declaration the prose names — O14-K's 43 kernel facts item by item, from
`InstAvail` (ImplementationLocality.lean:268) and `instAvail_mono` (:305) to `genTheory_avail_conj`
(SubstratumSource.lean:103) — and 2 to the bridge's committed modules at `a34d20b5` (`BridgeAvail.lean:74`, the block
defining `w345`, `zPh`, `uJ`, `tokOp`, `TokenAvailAt`; `BridgeAvailFull.lean:64`, `latticeClass`). 55/55. O14-K's
CERTIFIED label applies to these kernel facts at L only, as the row states; every other row is CONDITIONAL.

## 6. CI

Two `workflow_dispatch` runs on `dev-origin/drive`, rows added to `CI-RUNS-R5.md`: 38134267257 (`78baca7c`) failed at
Build in `OriginDrive` at exactly the two sites the thread records (`337:16`, three unsolved goals in `zPh_entries`, one
of them `w345 ^ 4 = 1` from a `first` fallback; `810:4`, a type mismatch `μ * star μ = 1` against `star μ * μ = 1`), eight
prints on `sorryAx` (the two theorems and six that use them); 38135099684 (`86358785`) built (3650 jobs), all 110 prints
of `OriginDrive` on the standard axioms (two, `phi5_three_four` and `phi5_five`, on the subset `[propext, Quot.sound]`),
`lean-axioms` 6178 = 5860 + 318 (the 318 prints of the five design modules, each a distinct new short name), gate red only
on `lean-manuscript` (5 problems, the five design modules), 20 PASS of 21.

## 7. Lean statement review (`OriginDrive.lean` @ `86358785`)

The statements say what the rows say. `OpDrive 𝓘 arch := ∀ n, 0 < n → TokenAvailAt 𝓘 arch zPh n`. O14-T1:
`not_opDrive_perm`, `not_opDrive_mixEmpty`, `not_opDrive_lattice` (through `not_opDrive_of_quartLattice`), with the
positive controls `opDrive_substratum`, `opDrive_fullClass`. T2: `opDrive_of_substratumAvail` (hypothesis
`SubstratumAvail` of the generated theory on the token) and `lattice_not_substratumAvail`. T3: `opDrive_of_control`,
`opDrive_of_qm`. T4: `driveClass := IsSubmonomial ∧ WLat`, with `WLat` the lattice of `⟨i, w⟩` (fourth powers equal up to
powers of `w⁴`), `opDrive_drive`, `driveTheory_not_qm`, and `not_tokenAvail_rot_of_submonomial` (for every architecture
whose members are all submonomial, `rot θ`, `0 < θ < π/2`, is unavailable at every positive level). T5:
`avail_unitary_iff` (for a unitary-ray-saturated architecture, a unitary conjugation is available iff a nonzero multiple
of the unitary is a member) and `lattice_avail_finite_upToScalar`, `mixEmpty_avail_finite_upToScalar` (every available
unitary is `b • M` with `M` in the finite set of matrices with entries in `{0} ∪ μ₄`). T6:
`not_levelOneClause_of_submonomial` (the level-one clause of `DenseUnitaryControl` fails for every submonomial
architecture). T7: `irrational_theta0_div_pi`, `fixedGateTheory_theta0_denseUnitaryControl`,
`fixedGateTheory_theta0_not_qm`, composed from the kernel's DiscreteCompletion.lean:1942 and :1948. T10:
`not_opDrive_pi_div_four` and `not_opDrive_of_rotClifford` take `LevelOneCliffordInput` (O9-L1) as an explicit
hypothesis, a definition whose docstring states it is written and not kernel-checked. T12: `discard_tokOp_eq`,
`tokenAvail_descend` (needs `LabelInvariant`). The cores `o14_core` (19 conjuncts) and `latticeGroup_core` (5) restate
these. The valuation argument (T8) and the repeat-until-success protocol (T9) have no Lean form; their rows are labelled
[W] + [X], "no kernel check", correctly.

## 8. Mathematical assessment — the owner's O14 questions

**The actual generated group under the permitted operations.** For a unitary-ray-saturated architecture the `InstAvail`
closure (ancillas, readouts, feed-forward, coarse-graining, discard, relabelling) adds no unitary conjugation beyond unit
multiples of members (`avail_unitary_iff` [D], through the kernel's ray step MicroscopicReversibility.lean:251 [K]).
At the audited scope this gives: `permClass`, unit multiples of permutation matrices; `MixR ∅` and FM's `latticeClass`,
unit multiples of `μ₄`-monomials; in both, finite up to scalar at every carrier [D], each element with a scalar power [D].
The exact orders modulo scalars, `(2n)!` and `(2n)! · 4^{2n−1}`, are computed at `n = 1, 2` [X] (the thread's X6;
independently Z1) and are the monomial count at general `n` [W], which rests on every permutation and every
quarter-phase pattern being a member at that carrier (finding F-O5-2).

**Exact against dense.** Availability reaches only the exact group (finite compositions by `op` and `bind`); its closure
is reached only under a closure premise, which the archive names LIMCLOSE-C — introduced, not an OI premise, not an
inventory item at L. At the audited scope the group is finite, so it is its own closure, and the drive is not even a
limit of available channels (the coefficient square [W], spot-checked [X]). In every submonomial class the level-one
clause of `DenseUnitaryControl` fails [D].

**Alternative generating sets and their disguise tests** (the thread's §2 table, confirmed). A finite-order non-Clifford
phase `T` with the stated access generates a finite group (16 elements modulo scalars; X7, Z6): no density, no drive. `T`
with the balanced mixer is dense [L] but never makes the drive available (T8's valuation argument over `ℤ[ζ₈][1/2]`
[W]; Z5 checks its inputs). `{rot(π/8), S, X}` is dense at level one and never gives the drive (T8). The balanced mixer:
level-one group the 24 Clifford channels, the drive only as a limit of available channels (T9, verified with two
different circuits, Z3 and Y2–Y4). `rot θ₀`: dense at every level [K composed in D], the exact drive OPEN (excluded at
level one without dilations given [L]). The fractional layer flow with the quarter phase gives the drive exactly but is
the phase intervention in the exchange's eigenbasis (disguise test FAILED). The phase intervention at θ₀ (the drive
class), at every angle (I4.60) and the re-preparing tower fail their disguise tests as independent principles.

**O14-N1 and its scope — the cross-thread point.** Verified: in `MixR {π/4}` the drive is a limit of available channels
[X] + [W] (protocol assembly from `op`, `readout`, `bind`, `coarse`, `discard`, with the pure ancilla prepared from the
uniform attachment by readout and flips), while it is never available there (T8 [W]; T10 under O9-L1). Three
consequences for the bridge, which the thread's placement "(B), provisional twice" anticipates and which I make
explicit:

1. O14-N1 cannot supply B20-2's premise OpDrive(θ₀): that premise is an availability statement, and the drive is not
   available in `MixR {π/4}` at any level.
2. What it supplies is invariance of every closed set — every closed pair cone — that is invariant under every
   available channel of the class. The bridge's transfer clause (T)_𝓘, as built (`TransferClause`, BridgeDictionary
   [D]), transfers admissible **one-token unitaries** only. The repeat-until-success channels act through two ancillas,
   readout, feed-forward and discard, so the route needs the transfer in **channel form** — every available one-token
   channel of `𝓘` maps `K` into itself through its transferred table, `coordOf ∘ (1 ⊗ Φ) ∘ dict` — written below
   (T^ch)_𝓘, together with closedness of `K` (the equivalence ledger's `hcl`). (T^ch) implies (T) for the class's
   unitaries. QM's cone `Q3` satisfies (T) for every class (`transferClause_Q3` [D], round 4) and (T^ch) (a local
   channel preserves the composite positive cone [W]).
3. The ancilla gates need the J datum on every qubit factor, which follows from its availability on the token by I4.30
   (`LabelInvariant`) and kernel transport (ImplementationLocality.lean:644); I4.30 is among B20's hypotheses. Y1 shows
   that the J datum and the balanced mixer generate the same level-one group with the quarter phase.

So the candidate route replaces the bridge's introduced set {OpDrive(θ₀), J-datum, (T)_𝓘} by {J-datum taken as the
balanced mixer, (T^ch)_𝓘, `K` closed}: the phase intervention at θ₀ is traded for the channel form of the transfer
clause. The J datum stays introduced (I4.239; O2-G3), and the transfer is not removed but strengthened. Whether OI's
operational semantics — available operations are admissible maps on the state space of every system they act on —
supplies (T^ch) on the P-level pair cone without identifying the cone with `Q3` is the bridge audit's open round-6
question (§9 there) in its channel form. Nothing in round 5 assembles this route against the bridge's derived half; it
is [W] + [X], not [D].

**The owner's four claims, after O14.**

| claim | status after this audit |
|---|---|
| a bridge from the existing OI assumptions alone | not established. At the audited scope (the stated access, `MixR ∅`, FM) the drive is excluded exactly and as a limit of channels, so no route through the drive starts from those premises (class (D) at Table A2's scope) |
| a bridge using additional assumptions | B20-2 with {OpDrive(θ₀), J-datum, (T)_𝓘}: CONDITIONAL [D] (bridge audit). Candidate alternative {J-datum as the balanced mixer, (T^ch)_𝓘, `K` closed}: [W] + [X], not assembled in a module, not checked against the derived half |
| (T) necessary for this construction | yes, as the bridge audit established; O14 adds that the alternative route also needs a transfer, in channel form |
| (T) necessary for any derivation of quantum equivalence | not shown. Exact QM entails the drive (O14-T3) and satisfies (T) and (T^ch) for its own class, so every premise set that derives QM implies them; that is a consequence of the target, not a proof that the transfer is an independent necessary premise |

B20's outcome stays **(C), provisional**. O14 identifies a different route to the drive in the invariance reading, and
that route still carries a transfer requirement; the cross-thread check is whether the bridge's cones are required to be
invariant under every available channel, which round 6 carries.

## 9. Findings

- **F-O5-1 — table rendering.** Rows O14-T8 and O14-T9 of `RESULTS.md` contain unescaped `|` inside code spans
  (`|a| ≤ 1`, `|Re| + |Im| ≤ 1`, `|0⟩⟨1|`), which split the cells in GitHub-flavored Markdown: those two rows render with
  their kind, label and evidence cells displaced. The source text is intact and no label is affected; the fix is `\|`
  in those spans, forward, in the thread's next round.
- **F-O5-2 — orders at general `n`.** O14-V and HP-origin-14 item 1 state the orders `(2n)!` and `(2n)! · 4^{2n−1}` at
  every level without the qualifier O14-T5 carries ("levels one and two computed"). The module proves finiteness up to
  scalar at every carrier; the general-`n` value is the monomial count [W]. No label change (the rows are CONDITIONAL).
- **F-O5-3 — what (T)_𝓘 must become for item 7 of HP-origin-14.** "The bridge's premise set would reduce to that one
  finite-order Clifford datum with H1, H3 and whatever (T)_𝓘 requires": what it requires is the channel form (T^ch)_𝓘
  and closedness of the cone (§8), not (T)_𝓘 as built. The thread's §0 and HP §3 already condition the placement on
  invariance under every available channel; recorded so that the bridge's cross-thread check uses the channel form.
- The coordinator's write into the thread's scratch area during the first transcript replay (§2): content unchanged,
  modification times changed; recorded, no effect on any committed file.
- No label changes. O14-K CERTIFIED (kernel facts at L); O14-T1 … O14-T12, O14-A, O14-P, O14-V CONDITIONAL at their
  stated evidence; O14-D FAILED (for the candidates as independent principles); (B) for the balanced mixer provisional.

## 10. Carried to round 6 (origin)

- O15 and O16 (the owner's narrowing).
- The exact drive in `fixedGateTheory θ₀` through dilations (OPEN).
- Kernel forms of T8 (the valuation argument over `InstAvail`), of T9 (the protocol and its limit) and of O9-L1.
- The transfer clause in channel form, (T^ch)_𝓘, against the existing premises; whether the bridge's cones must be
  invariant under every available channel (the scope of the (B) placement).
- F-O5-1 and F-O5-2, corrected forward.
