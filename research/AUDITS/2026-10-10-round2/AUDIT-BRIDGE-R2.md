# Coordinator audit — `research/bridge`, round 2

Thread head `3686049e` (2026-10-10; round-2 commits `e29b6a42` … `3686049e`). Base L = `9f9f8257`. Audited: the
round-2 rows of `RESULTS.md` (B6-1, B7-1 … B7-5, B8-1 … B8-4, B9-1 … B9-5, V-2), `NOTES-B6.md`, `NOTES-B7.md`,
`NOTES-B8.md`, `NOTES-B9.md`, `experiments/b7_b3c`, `b7b_generic`, `b8_composition`, `b9_spec`, the design modules
`lean/BridgeLemma.lean` and `lean/BridgeDictionary.lean`, the receipts in `inbox/`, the handoff proposals HP-4 … HP-6,
`LOG.md`.

## Method

1. **Receipts.** HO-4, HO-5, HO-6 copied verbatim (sha256 `0c67c449…`, `25a4ff61…`, `901e8d10…`, each equal to the
   overview file at `62cbb3cf`) and committed at `e29b6a42` with the reliance recorded in `LOG.md`. Protocol satisfied.
2. **Replay.** Four scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 4/4
   (`bridge/REPLAY-LOG.txt`); stderr differs only by the thread's `exit 0` marker line.
3. **Independent check.** `bridge/indep_checkB2.py` (own code, reads nothing; decision rule fixed before the first
   run): run 2 **5/5 CONFIRMED**, `INDEP-B2-FIXED`, replay identical. Run 1 (kept) was 4/5: X2's pool of certified
   members of K(Z_F) was too small to witness every exclusion — a defect of the coordinator's harness, enlarged in
   run 2 from the pure states of `Q3 ∩ Z_F*` with Gaussian-integer coordinates; no thread claim was involved.
   - X1 (B7, Lemma 2): on the thread's instance I1 (one product vertex) the moment-orbit certificate holds —
     `ε < |det C_k|²` at the three non-product vertices and `d_{k,τ} > √ε` in all six orders at the product vertex
     (`d_min = −1/10 + √395/60 > 1/1000`); Lemma 2(b) exact on explicit products; Lemma 3 (no orthonormal basis with
     exactly three product vectors) on 180 exact orthonormal product triples.
   - X2 (B8-4): among the octahedral rotations exactly `V4` on each token permutes `Z_F`; every other rotation moves a
     defect out of K(Z_F), witnessed by a negative pairing with a certified member.
   - X3 (B9-4): `⟨cnot, actC cyc3, actT cyc3⟩` and `⟨cnot, local octahedral⟩` both have order 11520 and coincide
     (own signed-permutation closures).
   - X4 (B9-3): the `Ad`-closure of `{Z⊗I, I⊗Z}` under `CNOT`, the NOTs and SWAP is `span{Z⊗I, I⊗Z, Z⊗Z}`, abelian;
     `V Z V* = X` and `[Z, X] = 2iY`.
   - X5 (B9-1, (D1)–(D2)): `pauliW ∘ cnot = Ad(CNOT) ∘ pauliW`; `pauliW ∘ actT R_z = Ad(I⊗U) ∘ pauliW`,
     `pauliW ∘ actC R_z = Ad(U⊗I) ∘ pauliW`; `pauliW(prodState) = ρ⊗ρ`.
4. **Written proofs read.** NOTES-B7's reduction and Lemma 2 (the moment-orbit certificate near the vertices of the
   simplex, both the non-product and the product vertex), Lemma 3 (via the absence of unextendible product bases in
   `2⊗n` [L]) and the `(2,1,1)` case of §4: sound as written; the step from "some pure state is unreachable" to
   "an exotic invariant cone exists" is claim (D) of the audited stage-4 record [A], which the thread names at every
   use. NOTES-B9's disguise test of the transfer clause (T): the clause is (b) for the monomial images, as stated.
5. **Kernel statements.** B8-2's certified non-implication read at L: OIRealization.lean:360
   `finiteOI_not_implies_inert`, SpectatorBridge.lean:223 and :233 (`InertSpectatorCompositionality` and its
   equivalence with `HasParallelReferenceExtension`). The design module `BridgeLemma.lean` (sha256 `0fdf72f6…`):
   `bH_respect`, `bH_perm`, `bH_convex`, `ctl_bH`, `ctl_counter` read against NOTES-B1 §2 — the hypotheses are RESPECT,
   (A), (P) and H1, local tomography is proved from one-token spanning, and the countercontrol shows (A) load-bearing;
   consistent with the written Theorem B1.1. `BridgeDictionary.lean` (sha256 `e4b60411…`) is a draft whose product law
   did not build; its content rests on b9 Y1–Y3 [X], re-checked in X5.
6. **Kernel citations.** 14/14 new citations resolve at L (`cite_check_r2b.out`).
7. **Design runs** (`CI-RUNS-R2.md`): 38090784384 (`dev-bridge/b11-lemma` @ `00d43da4`): Build failure on the
   reserved token `𝒫`, corrected; 38092042844 (@ `f1c5f0fb`): Mathlib bridge Build success (3644 jobs),
   `BridgeLemma` 14/14 prints on `[propext, Classical.choice, Quot.sound]`, `lean-axioms` PASS (5874 named results, no
   sorry), gate red only on `claims`, `duplicate`, `lean-manuscript`; 38093576860 (@ `bbbefb72`): Build failure in
   `BridgeDictionary.dict_tens` (`dict_tens`, `dict_prodState` print `sorryAx`; `monomial_extension_admissible`
   standard; `BridgeLemma` rebuilt 14/14 standard). Three dispatches, the cap. Design evidence only; nothing certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| B6-1 | CONJECTURE ([D], run 38092042844) | accepted; the run verified at the step level; the module's statements match NOTES-B1 §2 (method 5). Supersedes B5-2's OPEN for the formalization |
| B7-1 | CONJECTURE (complete written proof) | accepted; Lemma 2 confirmed on I1 (X1), Lemma 3 on 180 triples; the (2,1,1) argument read |
| B7-2 | CONDITIONAL (on claim (D) [A]) | accepted; B3.C now holds in every case at this label, the reachability step being B7-1. The overview carries "B3.C: CONDITIONAL on (D); reachability CONJECTURE" and HO-2's open item is updated by HO-10 (a new handoff, HO-2 not edited) |
| B7-3 | CONDITIONAL ([L] no UPB in `2⊗n`; [W]) | accepted; X1 |
| B7-4 | CONDITIONAL (Jordan [L]; (D) [A]) | accepted |
| B7-5 | CONJECTURE (evidence); run verdict B7B-FAILED Z1 kept | accepted as recorded: the generator produced 2 product lines where 1 was designed; Z2/Z3 PASS; no re-run, no edit |
| B8-1 | CONDITIONAL (reading of Main.md:552 through the dictionary) | accepted; X5 |
| B8-2 | CERTIFIED (matrix-level non-implication); reading [W] | verified at L (method 5) |
| B8-3 | FAILED as a bridge; exclusion facts CONDITIONAL on KZ7 [A] | accepted; X2 confirms the Clifford part exactly |
| B8-4 | CONDITIONAL (KZ7) for SO(3); exact among the 24 Cliffords | accepted; X2 |
| B9-1 | FAILED as a bridge; (D1)–(D2) exact | accepted; X5; the vacuity of HO-6's "image cone" form is correct (`M⁻¹(PSD) = Q3`) |
| B9-2 | CONDITIONAL (on (T) = SPEC_P(φ)) | accepted — a relocation, as stated |
| B9-3 | CONDITIONAL (claim (D) [A]; stage 4 [A]) | accepted; X4 |
| B9-4 | CONJECTURE (exhaustive exact computation) | accepted; X3 reproduces both orders and the equality |
| B9-5 | OPEN (draft; build failed) | accepted; the untested fix is recorded in NOTES-B9 §4 |
| V-2 | CONDITIONAL (on H-OI_g; (ii)–(iii) on (D) [A] and Jordan [L]) | accepted |

**Label changes: none.**

## Recorded for the overview

- New assumption (watch marker): the **transfer clause (T)** — the pulled-back idle extension of every admissible
  one-token implementation maps the pair's cone into itself; for the monomial class it is SPEC_P(φ) ∧ SPEC_P(NOT),
  i.e. (b) for the phase flow and the NOT on each token. The certified `substratumClass_contextStable` supplies none of
  it (the matrix carrier's cone is PSD by construction).
- A_miss splits into a continuous abelian half (SPEC_P(φ): matrix-certified, needs (T) at P) and a finite half
  (SPEC_P(J): given H2, equivalent to (b) for the native Clifford local family of order 11520, H-sourceable as hidden
  permutations, needs (A) at H). Each alone leaves exotic cones (CONDITIONAL on (D)); together they force `Q3`.
- B3.C holds CONDITIONAL on claim (D); the finite and locally finite route is closed without conjecture; the
  single-token stabilizer of K(Z_F) is `V4`; the realization theorem's excluding clause is family membership, whose
  matrix form is certified independent of the sealed OI core.
- Theorem B1.1 is a design module ([D], green).
- Thread deviations disclosed (one root import line per module on the dev branch; the leftover numerical-probe shards
  of all three runs cancelled by the thread; estimate-based timestamps corrected; b7b's Z1 generator defect; b9 Y2's
  message wording) — noted; round 3 instructs the threads not to cancel CI jobs.
- Routed: HO-10 (bridge → countermodels, equivalence), HO-11 (bridge → countermodels), HO-12 (bridge → origin,
  equivalence).
