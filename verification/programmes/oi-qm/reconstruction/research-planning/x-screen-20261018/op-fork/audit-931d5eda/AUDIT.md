# Independent audit: op-fork @ 931d5eda (OP-weak vs OP-strong purification fork)

Research only. No round, no F, no merge, no promotion of X. Read-only on the repository: nothing was committed, pushed,
commented on or dispatched. Auditor's scratch: `xop-audit/` (tools/, runs/; under 0.1 MB beside the worktree).

Tags: [EC] exact computation by this audit, with its own code; [WA] written argument; [L] literature; [UP] unsourced or
unverifiable.

## Verdict: CONFIRMED WITH CORRECTIONS

The decisive mathematics holds:
- OP-weak does not imply OP-strong on SEP ⊆ K ⊆ maxCone.
- K(Z_F), L = Q3 ∩ Z_F\* and K_Γ = Q3 + ℝ₊Γ(B) each satisfy E and U-weak at every marginal, and each fails U-strong.
- K(Z_F) and L are invariant under all 24 native permutations.

So RETIRE, worded as "OP-weak insufficient alone as a standalone cone-selection condition under the tested premises",
follows from the frozen rule and is not overstated.

The corrections below concern three things: an overstated assumption-watch marker and remark, how the verdict
generator labels written arguments, and gaps in the rule design and in chronology. None of them changes the verdict.

## Findings (decisive first)

**F1. The decisive facts reproduce under independent exact code.** [EC] `tools/audit_exact.py` imports nothing from the
probes, takes the defects from the historical record (R6 NOTES A2 @ `e7d380fc`), and passes 47/47 checks over two
byte-identical runs.

- **(a) Domain inclusions.** {I/2 − z_k} are orthogonal rank-one projectors that sum to I, and each m_k is maximally
  entangled. The symbolic identity ⟨ab|z_k|ab⟩ = ½|a|²|b|² − |⟨m_k|ab⟩|² gives SEP ⊆ Z_F\* and shows each z_k is
  block-positive. Each Γ(z_k) is a rank-one projector, so z_k ∈ Γ(Q3) ⊆ maxCone. Γ(B) = SWAP/2 is block-positive.
  All three cones differ from Q3 and from Γ(Q3), with exact witnesses.
- **(b) Existence and U-weak at I/2 and at two non-diagonal marginals.**
  - Existence, by a certificate of my own that differs from the RESULT's identity. For symbolic Hermitian S,
    Tr(z_k·vec(S)vec(S)†) = c_k·det S + SOS_k, with c_k ∈ {0, 1}:
    - for (±1, 1): (p−s)²/4 + q²;
    - for (1, −1): det S + ((p−s+2q)² + 8r²)/4;
    - for (−1, −1): det S + ((p−s−2q)² + 8r²)/4.

    With S = √ρ ⪰ 0, the canonical purification lies in L for every ρ in the ball. This is an exact identity plus a
    one-line argument. A countercontrol shows the certificate needs S PSD.
  - U-weak:
    - Further pure states (I⊗u)ψ ∈ L are related to ψ by unitaries solved exactly from the data (SO(3) action).
    - In K(Z_F) at I/2:
      - Φ⁺ → z_k by an improper Γ∘Ad_v, with v exact and det −1;
      - z_j → z_k by a proper Ad, for all 16 ordered pairs.
    - In K_Γ: Φ⁺ → Γ(B) by Γ.
- **(c) U-strong failure.** My own witnesses differ from the RESULT's diag(1, i).
  - L and K(Z_F) fail at I/2 with u = Cayley([[0, 1+i], [1−i, 0]]), and at the non-diagonal marginal ρ_A with a second
    rational u:
    - the only relating map is Ad_u;
    - improper images are non-PSD, by symbolic covariance and det Γ(ψψ†) < 0;
    - x = (I⊗u†)m_k lies in L, but Ad_u x = P_{m_k};
    - P_{m_k} ∉ K(Z_F), certified by the exact separating functional z_k ∈ K(Z_F)\*. This uses Tr(z_k z_j) = δ_jk and
      L ⊆ Z_F\*, and it does not depend on the RESULT's extremality argument.
  - K_Γ fails with my separator W′ = P_singlet + P₁₁: W′ ⪰ 0, Tr(W′Γ(B)) = 0, and Tr(W′Γ(χχᵀ)) = b(b−a) < 0 for
    a > b.
- **(d) Native permutations.** All 24 permute Z_F exactly, including CNOT (control token 1) and SWAP. The non-native
  I⊗diag(1, i) does not.
- **(e) Extreme rays.**
  - My own zero-set nullspace implementation gives dimension 1 in maxCone for:
    - a non-maximally entangled rank-one table;
    - P_m;
    - z_(1,1) and z_(−1,−1);
    - Γ(B).

    Both countercontrols give dimension ≥ 2: 11 with a single zero, and 4 for P₀⊗I.
  - Exact face-dimension spot checks in L, each with an explicit X ± εY ∈ L at rational ε:

    | element | active cuts | face dimension |
    |---|---|---|
    | rank 2 on span{m₁, m₂} | 2 | 3 |
    | rank 2, P_{m₁} + φφ† | 1 | 3 |
    | rank 2, z₁ + z₂ = P_{m₃} + P_{m₄} | 2 | 3 |
    | rank 2, generic | 0 | 4 |
    | rank 3 | 0 | 9 |
    | rank 4 | 0 | 16 |
    | rank one | – | 1 |

  - **No rank-2 extreme ray is confirmed on these spot checks.** The universal statement is a proof [WA]: at most two
    cuts are active (exact trace identity), so the face has dimension ≥ r² − 2 ≥ 2. The defects z_k have rank 4.

**F2. Replay is byte-identical.** [EC]
- `python3 -I -B op-fork/probes/replay.py` in a fresh detached worktree at 931d5eda: rc 0, `REPLAY GREEN`.
- `sha256sum -c runs/SHA256SUMS`: all 9 OK.
- `git status` is clean after the replay, so the regenerated outputs equal the committed blobs. Log:
  `runs/replay-of-931d5eda.log`.
- The audit's own harness-error run is kept in `runs/run1-harness-error/`. It had two FAILs, both in my code: unnormalized
  m_k in one identity, and a unitary list with no I/2 witness. Neither was a disk failure. Both were fixed and re-run.

**F3. Status of the written arguments.**

| argument | status |
|---|---|
| N1 transport | Proof [WA + L]. Ad_{A⊗I} with A invertible, and Γ, are linear automorphisms of maxCone; every Schmidt-rank-2 vector is (A⊗I)Φ⁺. Størmer–Woronowicz is needed only for the upper bound Ext(maxCone) ⊆ rank-one ∪ Γ(rank-one), which only N6 uses. The decisive chain for the three cones does not depend on S–W: it needs extremality of the listed elements plus Ext(C₁ + C₂) ⊆ Ext C₁ ∪ Ext C₂. |
| N2 lemma | Proof, short [WA + L, Uhlmann]. |
| N3 "exact symbolic identity over the whole ball" | The identity is exact. The step to ≥ 0 is a correct one-line inequality [WA], which I confirmed with an independent SOS certificate [EC]. The label is accurate as "EC identity + WA". |
| L classification (active cuts ≤ 2 ⇒ face dimension ≥ 2) | Proof [WA], standard face argument. |
| U-strong uniqueness of the relating map | Proof [WA]. |
| MI | Proof, and trivial: see F7. |
| TS-a and TS-b (q3 A3) | Proof [WA]. |

**F4. AW-OP1 is real but overstated; reclassify it as ELABORATING.** [WA, using the RESULT's own C3 and my `ctl` check]
- The lead sentence ("on SEP ⊆ K ⊆ maxCone the relational content … is inherited for free") is false as a universal.
  So are the conclusion ("OP's cone-selecting power lies entirely in its automorphism clause") and the PR-comment
  paraphrase ("on this domain the relational half is automatic"):
  - E excludes SEP and K_B;
  - U-weak excludes K_mut = Q3 + ℝ₊(Γ(B) + ½P₀₀), the fork's own control C3.
- Correct scope: U-weak holds automatically for every cone with Ext K ⊆ Ext(maxCone) (N2). On such cones OP-weak selects
  by E alone.
- The SO(3) half, "the automorphism clause at pure marginals forces token-2 SO(3)", is correct [WA + L]. That is, TS-a
  holds on the whole domain, so products are the pure states at pure marginals; U-strong then makes the closed group
  {g : (id⊗g)K = K} transitive on S², so it contains SO(3). But it is already REPORT S3 steps 2–3, and REPORT P3 already
  says OP's exclusion power on K(Z_F) lies in its compatibility clause.
- So the new part is the generalization to the class Ext K ⊆ Ext(maxCone): ELABORATING, not NEW.

**F5. AW-OP2 is real, and stronger than stated.** [WA]
- TS-a and TS-b hold on every domain cone (q3 A3; I checked the argument), so neither reading can exclude anything.
- maxCone satisfies E, U-weak and U-strong:
  - its relating maps Ad_u and Γ∘Ad_u preserve maxCone, because Γ(SEP) = SEP;
  - it fails PC.
- REPORT:70, "maxCone fails only the trivial-system clause [L]", has no two-token support. My grep of this tree finds no
  definition of the clause [UP].

**F6. The PREREG→RESULT chain is sound in substance, with three gaps.**
- *Rule fixed before measurement: partly verifiable.*
  - The KEEP/RETIRE core is REPORT:132–134, committed at fb55f654 (05:23Z), before the fork.
  - PREREG, probes, runs and RESULT all landed in one commit (07:47Z), twelve minutes after the owner comment
    (07:35Z). So "PREREG was written before any probe was run" cannot be verified from the record [UP]. No evidence of
    post-result test changes was found either.
- *Rule design.* The branches are not mutually exclusive. Under PREREG's clause set (TS separated out), maxCone already
  satisfies the RETIRE condition, E ∧ U-weak with K ∉ {Q3, Γ(Q3)}, by N1 + S–W [L] + N2. So RETIRE was reachable before
  any probe ran. The informative content is the U-strong failures, which the rule does not require. The outcome is
  unambiguous, because the three cones also refute KEEP's disjunct 1 (OP-weak ⇒ OP-strong).
- *Mechanical generation.* Mostly mechanical, with two defects:
  - `replay.py:68` prints "OP-weak ⇒ OP-strong is therefore false" as a fixed string, not conditioned on the measured
    `ustrong` values.
  - The RESULT keys `existence_all_marginals`, `uweak_all_marginals` and `pure_classification` are GREEN labels on
    written-argument conclusions. In q3, a single bucket `cert('N5')` feeds five keys and C6. This conflates
    verification layers (Code Review Rules: keep layers distinct). It is correct here, but it should be relabeled.
- *Owner wording clause.* Applied to wording only. The verdict structure, the tests and the rule are unchanged. ✓

**F7. MI adds nothing on the domain: PC ⇒ MI for every domain cone.** [WA, EC instance] Since ρ⊗P₀ ∈ SEP ⊆ K, any cone
that CNOT preserves satisfies MI. The pairing CNOT(ρ⊗P₀)CNOT·z_k = (1 ± x)/4 ≥ 0 [EC]. So "OP-weak ⊕ PC ⊕ MI" equals
"OP-weak ⊕ PC". The RESULT's statement is true; listing MI separately adds no constraint.

**F8. A RESULT remark is overstated.** [WA] "This fork shows a relation-level statement selects nothing on this domain"
is wrong: OP-weak excludes SEP, K_B and K_mut. It should read "does not select Q3 and does not exclude K(Z_F)".
Separately, the remark identifies Main.md:600's quotient-level uniqueness with OP-weak's O(3)-relation without a
formal map. The RESULT says no map exists, but it still concludes "could at best supply a relation-level statement"
[UP]. Code Review Rules: no identification without a formal map.

## Gates G1–G8 and M1 (memo @ acfef447 §2.3, §3.2, §3.3, applied to OP-weak as written)

The owner's direction (PR #864, comment 6247055849) asked for both readings to be screened against G1–G8 and M1.
RESULT.md has no gate table, so the audit supplies one for OP-weak. OP-strong stays as REPORT S1 has it.

| gate | OP-weak | evidence |
|---|---|---|
| G1 | BORDERLINE | The uniqueness clause relates states by ball symmetries that PREREG §2 explicitly says are not operational resources [WA] |
| G2 | FAIL | No consequence beyond compatibility, (iii). Sourcing, (ii), is only the quotient-level ingredient of Main.md:600, with no formal map [WA, UP] |
| G3 | FAIL | Γ(Q3) satisfies OP-weak, and in fact OP-strong (C1; Γ-covariance) [WA + EC] |
| G4 | at best OPEN | OP-weak adds no operation. REPORT S1's conditional G4 pass rests on the automorphism clause (\|+⟩ ↦ \|+i⟩ as a K-automorphism), which OP-weak lacks, so it does not transfer [WA] |
| G5 | FAIL on the §3.3 exclusion controls | X must exclude K_B, K(Z_F) and Γ(Q3). OP-weak excludes K_B (E fails), but not K(Z_F) [EC + WA, this fork and F1] and not Γ(Q3). **This is the gate-level content of "insufficient alone".** |
| G6 | OPEN | No prediction |
| G7 | PASS for the fork | R = O(3) was fixed before testing; the SO(3) variant is record-only, and L satisfies U-weak-SO, so the verdict does not depend on the choice [EC + WA] |
| G8 | PASS | A1/B1 fixed (memo, 2026-10-17) |
| M1 | not at risk; not tested | No operation or protocol is added and the retained readout is untouched [WA]. The fork runs no M1 computation; REPORT P5 is the instance |

**Does RETIRE / "insufficient alone" follow?** Yes, and the scope is right.
- It is not a rejection of OP-strong.
- It is not a rejection of purification as a component of a sourced X.
- Instance coverage (96 pairs) and the five N1 points are labeled as instances.
- The universal statements are labeled [WA] and are proofs. None is presented as an exact computation, except the RESULT
  keys noted in F6.

**Skepticism toward framework-favorable readings (§A.31).**
- The only favorable reading in play is that S3 (OP ⊕ PC ⇒ Q3) is "unaffected". The fork does not test S3. "Unaffected"
  means only "not refuted here", and OP-strong survivors are unclassified.
- F4 sharpens S3's G2 FAIL rather than relieving it. The OP content S3 uses is OP-strong at pure marginals, which is
  token-2 SO(3) invariance. That is hA itself: `actT` acts on the target index (CompositeDimension.lean:198), which is
  OP's partner token.
- OP-strong's exclusion of K(Z_F) uses Ad_{diag(1,i)}-type automorphisms, i.e. continuous local phases. Under strict A1
  their availability is posited (AW-X4), which bears on §3.3's "uniformly available operations only" [WA].

## Propagation to REPORT.md (record-only; for the research branch's owner)

- **S3** must read OP as OP-strong. L and K(Z_F) satisfy OP-weak ⊕ PC (⊕ MI) and are not Q3 [EC]. The S3 logic itself
  stands.
- **S1 countercontrols:**
  - :69, "K(Z_F) fails uniqueness", means OP-strong uniqueness only; K(Z_F) satisfies U-weak.
  - :70, maxCone's exclusion, is unsupported on the stated clauses (F5).
- **S1 G4:** the conditional pass needs the automorphism clause and does not extend to OP-weak (gate table).
- **S2 / C13:** on the domain, PC ⇒ MI (F7), so MI is strictly weaker than PC there.

## Corrections required (none changes the verdict)

1. **AW-OP1:** restrict it to cones with Ext K ⊆ Ext(maxCone). Drop "OP's cone-selecting power lies entirely in its
   automorphism clause", and the paraphrase in PR comment 6247305053. Reclassify NEW → ELABORATING (F4).
2. **RESULT's lift remark:** replace "selects nothing" with "does not select Q3 or exclude K(Z_F)", and tag the lift
   inference [UP] (F8).
3. **replay.py and RESULT keys:**
   - condition the OP-weak ⇏ OP-strong sentence on the measured `ustrong` values;
   - relabel the keys that are WA conclusions;
   - unbundle q3's `cert('N5')` (F6).
4. **State in RESULT:**
   - RETIRE's condition was already met by maxCone under PREREG's clauses, and the branches are not exclusive;
   - the informative result is the U-strong failure together with PC and 24-permutation invariance (F6).
5. **State that PREREG and the probes share one commit,** so "written before any probe" is unverifiable from the
   record (F6).
6. **Record these on the domain:**
   - PC ⇒ MI (F7);
   - TS-a and TS-b hold for every domain cone, so they cannot discriminate (F5).
7. **Add a G1–G8 / M1 table for OP-weak,** as the owner directed; the audit's table is above. G5's §3.3 exclusion-control
   failure on K(Z_F) is the gate-level reason for "insufficient alone".

## Files and digests

| file | sha256 |
|---|---|
| `tools/audit_exact.py` | `e728f6c2246e60b8ae91f47156807d9f44013ba789fd2e6fc1c6c18ac57c987b` |
| `runs/final/audit_exact.out` | `61ffe323b9e4f3f32de9b2cde342eaea91869f8cea9e373fc1e39b3716509219` (run twice, byte-identical, rc 0, ~49 s) |
| `runs/replay-of-931d5eda.log` | `c4a1bf5775b223851aebd30cff831a3e49446751455fcdee2a59cc76aed013ed` |

`runs/run1-harness-error/` holds the audit's own harness-error run; its digests are in `runs/SHA256SUMS`. No disk
failures occurred (about 150 MB was free at the end).
