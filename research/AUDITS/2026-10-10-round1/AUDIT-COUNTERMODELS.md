# Coordinator audit — `research/countermodels`, round 1

Thread head `54f79532d7b5dd7dd703ca0b3cf1e92066df9f0d` (2026-10-10). Base L = `9f9f8257`. Audited: `RESULTS.md`
(sha256 `ab6372c5a4d76258…`), `NOTES-C1.md` … `NOTES-C6.md`, `experiments/c1_cones`, `c1_rows`, `c2_structure`,
`c3_transitivity`, `c4_bell_family`, `c5_kappa_torus`, `c6_handoff_checks`, the handoff proposal HP1.

## Method

1. **Replay.** All seven scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 7/7
   (`countermodels/REPLAY-LOG.txt`). The committed `.err` files differ from the replay's stderr only by the thread's
   `exit 0` marker line appended by its harness; the replay's stderr is empty for every script.
2. **Independent check.** `countermodels/indep_checkC.py` (own code, reads nothing; decision rule fixed before the first
   run): run 2 **7/7 CONFIRMED**, `INDEP-C-FIXED`, replay identical. Run 1 (kept, `indep_checkC.run1.*`) was 4/7; all
   three mismatches were defects of the coordinator's harness and none touched a thread claim: X0 expected
   `ipW(z_s, P_s) = 0` where the cap exclusion gives `−1/2`; the `Herm(v^⊥)` basis scaled its projection coefficient by
   `|v|²` once too often (its members did not annihilate `v`); face members were taken in iteration order and shared a
   zero coordinate. The header of run 2 records the corrections.
   - X1 (C2.1) among the 2304 maps `actC R · actT R'` exactly 96 of type (+,+) and 96 of type (−,−) permute `Z_F`, none
     mixed; closures 96 / 192 / with SWAP 384 / with SWAP and `cnot` 1536.
   - X2 (C2.3) facial invariant `c`: 15 on a defect (face members on the null quadric span the hyperplane), 9 on `|00⟩`,
     10 on a one-tight-cap pure state, 10 on a two-tight-cap pure state (`z_s + z_t` annihilates `ψ_s + ψ_t`): the
     thread's refuted prediction 11 is confirmed refuted, its correction confirmed. Lower bounds by exact ranks of
     explicit members, upper bounds by `dim(Herm(v^⊥) + tight defects)`, both exact.
   - X3 (C4.1, "only if") at squared overlaps `16/25` and `144/169`: an explicit `y ∈ K* \ K` (ipW with `z_1` zero, with
     `z_2` positive, a negative quadratic-form witness on the projection of `g_2`), so the two-defect cone is not
     self-dual — the direction stage 4 had not reached beyond overlap `1/2`.
   - X4 (C4.3) `Z_Y = Ad(S⊗I) Z_F` is a set of four pairwise orthogonal Bell-type defects, `≠ Z_F`; `|G16| = 16`
     permuting both; `Ad(S⊗I)` normalizes G16; SWAP permutes `Z_F` and moves `Z_Y`.
   - X5 (C1.4) `K_F2`: `c = 15` on the defect, `9` on `P00` — T fails for `K_F2`.
   - X6 (C6.2) the flow law `ipW(R_n(t) z_s, R_n(π/2) P_s/4) = −sin t/8`, symbolic in `t`, three axes, both tokens,
     all defects.
3. **Kernel citations.** K2Guard.lean:106, :110, :134, :143 verified at L (`cite_check.out`).

## Findings by row

| row | thread label | audit |
|---|---|---|
| C1.1–C1.3 | CONDITIONAL [X]+[W]+[A] | accepted; the 199-row table is the thread's own replayed computation over R6's reference rows; the T row decided by computation (C1.4) |
| C1.4 | CONDITIONAL (W3–W5, [A] Y6) | accepted; X5 confirms the `K_F2` values; `K(e_c)` not re-derived here (the thread's exact interval cover stands at its label) |
| C1.5–C1.7 | CONDITIONAL | accepted (replayed) |
| C2.1 | CONDITIONAL (W1) | accepted; X1 confirms 96/96/0, 384, 1536 |
| C2.2 | CONDITIONAL ([A] Z z1, W3) | accepted; the extreme-ray characterization is a written proof with exact checks |
| C2.3, C2.3f | CONDITIONAL; FAILED prediction kept | accepted; X2 confirms 15/9/10/10 |
| C2.4 | CONDITIONAL | accepted (replayed) |
| C2.5 | CONDITIONAL on a rank-one-preserver theorem [U] | accepted as labelled; the [U] input is the only literature-dependent step and is named |
| C2.6, C2.7 | CONDITIONAL on EBF [A] — EXOTIC-E | accepted; `K_circ` exists by EBF, not exhibited (as stated) |
| C2.8 | OPEN | — |
| C3.1 | OPEN (wall: continuum of non-PSD extreme rays) | accepted; no principle proposed, correctly |
| C3.2–C3.4, C3.6 | CONDITIONAL (Lemmas 1–4 [W]) | accepted as written arguments with exact checks; not re-derived beyond the X2/X5 instances |
| C3.5 | disguise test; no round proposed | accepted |
| C4.1 | CONDITIONAL (W1) | accepted; X3 confirms the "only if" direction at two new overlaps; the "if" direction rests on T6 §3.3 [A] |
| C4.2, C4.3 | CONDITIONAL | accepted; X4 confirms the level-(ii) facts |
| C4.4, C5.4 | OPEN | — |
| C5.1–C5.3 | CONDITIONAL (W2) | accepted (replayed); the no-go for finitely many non-PSD extreme rays is Lemma 3's consequence |
| C6.1, C6.2 | CONDITIONAL | accepted; X6 confirms the law; HO-4 issued |

**Label changes: none.** The thread labelled nothing CERTIFIED, correctly: none of its results is kernel-checked.

## Recorded for the overview

- New assumptions/inputs: the rank-one linear-preserver theorem [U] (behind `Aut(K(Z_F))`); EBF [A] (behind
  `K_circ`); Y6's invariance of the facial invariant under automorphisms of a self-dual cone [A].
- Eliminated alternatives: extreme-ray transitivity T as a principle excluding *every* exotic cone — not established
  (wall recorded); finite-defect surgery cones for the κ-with-G16 and torus nodes — excluded (no finite-defect cone
  serves them); uniqueness of K(Z_F) given its symmetry group — refuted (`K_circ`).
- Round-ready: nothing; C3.1 would become a candidate principle only if EXCLUDES-ALL were proved, and it is OPEN.
- Thread deviations disclosed by the thread (one `python3 -I -B -c` version check; R6 scripts read as templates; the
  `K(e_c)` all-`c` FCC check added after run 1 and disclosed in the script header) — noted, no action.
