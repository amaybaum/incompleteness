# AUDIT-T — coordinator's audit of T6 (stage 6, step 4: the test of (b) against the complete applicable premises)

Base L = `9f9f8257…`, read-only. Written 2026-10-10, 19:29Z, after T6 reported (`.end_marker` 19:23:21Z, RESULT.md
19:24Z) and against the decision rules fixed beforehand: `pt/audit/stage6-inputs/PRE-AUDIT-R6T6.md` §3 (18:05Z) and
§5 (18:56Z, the expected witnesses recomputed), and amendment 2 A2.4. Inputs read: `pt/T6/RESULT.md` (sha256
`8de7fabe…`), `pt/T6/TEST.md` (`e007939c…`), the five script outputs and the hash list of RESULT §4. Nothing under
`pt/T6/` was modified.

## 1. Mechanical verification (`verify_thread.sh`, 19:25:08Z–19:25:22Z)

- **Hashes.** The 35 files T6 lists in RESULT §4 verify (`sha256sum -c`, 35/35 OK, `listed_hashes.check`);
  RESULT.md hashes to `8de7fabe…`, the value T6 reported.
- **Replays.** `t1_bridges`, `t2_pairthms`, `t3_countermodel`, `t4_rows`, `t5_axes` re-run from `pt/T6/` with
  `python3 -I -B`, stdout and stderr byte-identical to T6's own outputs, 5/5 (`replay/REPLAY-LOG.txt`). No script
  writes a file.
- **Integrity.** Start marker 18:50:48Z (manifests, base HEAD = L, clean porcelain, the twelve protocol prefixes
  with sidecars, the three audits at 845bd662 / 3fd6763d / 04308355); end marker 19:23:21Z, same checks, sweep clean,
  nothing quarantined; writes only under `pt/T6/`; kept runs `t1` and `t2` run 1. Every `.err` is `exit 0`.

## 2. The pre-registered acceptance rule for INDEPENDENCE, clause by clause

| clause (PRE-AUDIT §3; A2.4) | coordinator's check | result |
|---|---|---|
| the countermodel satisfies every item reaching the pair cone at L: SATISFIES or NOT REACHED on every non-hypothesis row of R6's audited table | `check_t6_rows.py` (4/4 `CHECK-T6-ROWS-FIXED`, replay identical) against my own recount `r6_rows.tsv` (Table A2): 199 rows with exactly the A2 ids; the R6 verdict T6 quotes agrees with my recount on every row; every non-hypothesis row is SATISFIES or NOT REACHED; FAILS = exactly the 13 hypothesis ids; T6's NOT REACHED set = mine (68); tallies 118 (3 vacuous) / 68 / 13 | met |
| it violates (b) in its weakest sufficient form by an exact witness | `indep_checkT.py` (5/5 `INDEP-T-FIXED`, replay identical; my own table-level code, rational rotations): X1 the flow law holds symbolically for a general unit axis, both tokens, all four defects — `ipW(act R_n(t) z_s, act R_n(π/2) P_s) = −sin(t)/2` in my normalization (T6's `p_s = P_s/4` gives its `−sin(t)/8`), equivalently `ipW(z_s, act R_n(u) P_s) = −cos(u)/2`; X2 the witness lies in Z_F* for every unit axis (pairings 0, (n₂²+n₃²)/2, (1−n₂²)/2, (1−n₃²)/2, nonnegative on the sphere); X3 `cyc3` and `cyc3⁻¹` on either token, witness −1/2; X4 mixed placement (flow on one token, J on the other) — each operation moves K(Z_F) out; X5 controls: at u = 0 the construction yields −1/2 but `P_s ∉ Z_F*` (so not a witness), at u = π the pairing is +1/2, `nflip` and `rot3 π` permute Z_F on either token. PRE-AUDIT §5's expected witness (K(Z_F) under the quarter-turn of the flow on one token) is T6's witness | met |
| the missing assumption is stated as exact content, with its own disguise test | TEST §5: A_miss = for one token τ, `K` invariant under `actτ R_x(t)` and `actτ R_z(t)` for all t (ball3Drive's flow and its J-conjugate; equally the drive through the NOT with the phase flow about z). Disguise test: fails — it restates I3.153 (b_DJ), I3.150 (b_S4) for two generators, K2's clause "local actions compatible with the composite cone" (I3.165), and is the drive instance of OI⁺-1 (I4.3 / I4.82 / I4.96, level M). Candidates that pass the test and would close the gap — λ (I3.133 with `tok` I3.134, [D]), pair homogeneity H (I3.160), extreme-ray transitivity T (I3.161) — are not items at L. This is the expectation PRE-AUDIT §3 recorded (the spectator clause for the drive and one off-frame partner, the instance of OI⁺-1) | met |
| the derivation attempt came first and was exhausted (depth-first) | TEST §2: D1 no H→P, M→P, G→P bridge at declaration level (t1); D2 no theorem at L concludes a pair-cone invariance under `actC g`/`actT g` (t2); D3 the ten object-specific discharges are closed statements off the pair carrier (t2 (d)); D4 the direct chain fails at step 6; §2.5 every CONDITIONAL-shaped route listed with the status of the item it uses. My own scan of the kernel at L (`OIBridge/**/*.lean`, read-only): 39 theorems mention `actC`/`actT` in their statement, the same count; among theorems, only `no_candidateCone_cnot_reflY` and `k2guard_orientation` bind an arbitrary pair cone; the two further theorems naming `CandidateCone` (`candidateCone_productSet` K2Guard.lean:185, `candidateCone_cnotOrbit` :194) are instance statements about the fixed sets `productSet` and `cnotOrbit` and conclude no invariance of an arbitrary `K`; the root aggregator's H/M/G tokens occur in its `import` lines only | met |

**The written proof of self-duality (TEST §3.3), reviewed step by step.** `K = A + C` with `A = Q3 ∩ Z_F*`,
`C = cone Z_F`, trace pairing `⟨M(z_s), M(z_t)⟩ = [s = t]` (`M(z_s) = I/2 − P_s`, the `P_s` orthogonal rank-one
projectors summing to I). (1) `K ⊆ K*` from `⟨A, A⟩ ≥ 0`, `⟨A, Z_F⟩ ≥ 0`, `⟨z_s, z_t⟩ ≥ 0`. (2) `K* = A* ∩ Z_F*` and
`A* = cl(Q3 + C) = Q3 + C` (closedness by the bounded-trace argument: `tr q_k` and `Σ_s λ_{k,s}` are both bounded
along a convergent sequence since `tr M(z_s) = 1`). (3) For `w = q + Σ λ_s z_s ∈ K*`: `⟨q, z_t⟩ = tr q/2 − ⟨ψ_t|q|ψ_t⟩`
and `Σ_t ⟨ψ_t|q|ψ_t⟩ = tr q`, so at most one `t` has `⟨q, z_t⟩ < 0`; if none, `q ∈ A`. (4) Otherwise `μ = −⟨q, z_t⟩ =
(a − tr Q)/2 > 0` with `a = ⟨ψ_t|q|ψ_t⟩`, `λ_t ≥ μ`, and `q' = q + μ M(z_t)` is PSD by the Schur complement bound
`S ⪰ (μ/2)(1 − tr Q/(a − μ/2)) I ⪰ 0`, which uses `Q ⪰ b b†/a`, `‖b‖² ≤ a tr Q` and `a − μ/2 = (3a + tr Q)/4 ≥ tr Q ⟺
a ≥ tr Q`; then `⟨q', z_t⟩ = 0`, `⟨q', z_u⟩ = ⟨q, z_u⟩` for `u ≠ t`, so `q' ∈ A` and `w ∈ K`. The argument is correct
and self-contained; it does not cite the stage-3 surgery theorems SD1/SD2 and agrees with that audited result. The
correction lemma is controlled on 600 exact instances with a countercontrol (a non-orthogonal family defeats step 3).

## 3. Observations and wording

1. **Normalization.** T6's `p_s` is the table of the projector `P_s` divided by 4 (so `ipW(z_s, p_s) = −1/8`);
   my `P_s` and R6's witnesses carry the factor 4 (`−1/2`). The two conventions agree on every sign and on every
   value up to that factor.
2. **Vacuous rows.** T6's "SATISFIES (vacuous)" rows I3.139, I3.140, I3.187 are R6's `d4v` class: implications
   whose hypothesis (IE1) fails for K(Z_F). Consistent.
3. **The two-way form.** Relative to the items at L, INDEPENDENCE. Relative to an enlarged premise set that adjoins
   the non-do-not-assume hypotheses K(Z_F) fails — the design-run four-token coherence λ (I3.133 with `tok`) or the
   PT-record pair homogeneity H (I3.160) — the verdict would read CONDITIONAL on that item (as stage 5 found for λ);
   neither is an item at L, and neither yields a derivation at L. The integration note carries both statements.
4. **Minor finding (BORDERLINE), carried as a clarification.** With the certified `ball3Drive` (flow about z,
   `J = cyc3`, `J R_z J⁻¹ = R_x`), the two weakest sufficient forms of INTEGRATION-NOTE-STAGE5 §2 — the drive with
   its J-conjugate, and the drive through the NOT with the phase flow about z — are the same pair `{R_z, R_x}`;
   they differ only under the PT convention that calls `R_x` the drive. No change of content.
5. **Deviations T6 disclosed** (RESULT §5): a version check and one stdin helper run without `-I -B` (nothing
   written under `pt/`; bytecode checked absent under `pt/base` and `pt/T6`); two NOTES interval stamps and one
   script-header stamp first estimated, then corrected or declared; NOTES appended in batches; directory listings of
   `pt/D5/`, `pt/C5/` by name only. None bears on any evidence line; recorded.
6. **Counts by method.** My declaration scan of the root counts 52 line-start declarations against T6's 65 (T6's
   scan includes attribute-prefixed and other forms); immaterial to the claim, which is that no root declaration
   carries either vocabulary.
7. **Gem classification** (§A.31): ELABORATING — the derivation's wall located at the declaration level, and the
   closed-form witness law for every axis (K(Z_F) admits no one-parameter local rotation symmetry of either token);
   CONFIRMING — NO-MEET at declaration level, R6's table for K(Z_F); POSITIVE — R6's classification survives a
   second independent re-check (T6's and mine). No NEW structural finding; the fixed point of the stage is reached.

## 4. Verdict

T6 is **accepted as INDEPENDENCE** under the pre-registered rule: every clause is met by independent checks that
replay byte-identically and agree with the witnesses the coordinator recomputed before T6 reported. The verdict is
the one the pre-audit expected; it was pressure-tested in both directions (TEST §7; my X5 controls and the Lean
scan), and the favourable-to-the-framework branch (a derivation) was exhausted first with the wall named exactly.

## 5. Files (sha256)

```
6bbd466344d70d8fadd88301649d90e106d7211c9ef199ed607ed9e88d1b9192  verify_thread.sh
c06e3f9432a7a433256924af7951385640ad90c7e3dc96e7c11ff1df2c3362e4  verify_thread.log        (hashes 35/35; replays 5/5)
f2c6b4b8cbd5e2827a22e8d22f92cae27c68e3fac8edd663b891c89b7b1557da  listed_hashes.txt
ae2ff2d320cfb91e6dd7bf96f5e23cb27f1fa23c376b03ed3bb608d36965aa91  listed_hashes.check
ea8f38fbc705379f61fc95c6876b57f87e482cc883209bafba84dff59864ee85  replay/REPLAY-LOG.txt
932e8c59a71f4af6d7b82fd4dedb2bae7552d9865842585f924456bda48d6e58  r6_rows.py               (5/5; written before T6 reported)
5a4258a265d00ce9e9d78f498b161cf66c38d2e2b7eee7f86a8785aa8d256fa0  r6_rows.tsv
b0c918556f1c3a1b3151211edb1bf1e75a7afebe0921841c93a6338ddbb8954a  preaudit_t6.py           (6/6; written before T6 reported; replay identical)
85e16e3aacb96113aee4b687fc691d316c13537a00ca92804163a540aaf3d1b0  preaudit_t6.out
52e0bf7c7f6a3959976c15bbe17bf4989393b8bd1b4a3f0050fa8e5392101140  check_t6_rows.py         (4/4; replay identical)
b17e63c0d017450d119d476c58d7441f1b746da4da380c9a73865f3fdcc5c0a5  check_t6_rows.out
0dee5f0af2903c13864be258ce4b215715a89914df07919068f81b6a2d32fc49  indep_checkT.py          (5/5; replay identical)
ca638118a2b51fcad613da89b28fdfc1d1bf4193761f18af2853a6d2417d835f  indep_checkT.out
```
