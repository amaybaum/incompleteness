# Coordinator audit — `research/origin`, round 2

Thread head `42bc3da6` (2026-10-10; round-2 commits `8f0c832a` … `42bc3da6`). Base L = `9f9f8257`. Audited: the
round-2 sections of `RESULTS.md` (O5, O6, O7, O5-SRC, O7 extension, verdicts by node), `NOTES-O5.md`, `NOTES-O6.md`,
`NOTES-O7.md`, `experiments/o5_kbd`, `o5_src`, `o6_tower`, `o7_density`, `o7_level3` (run 2; run 1 kept),
`lean/OriginPassive.lean`, the receipts in `inbox/`, the handoff proposal `O5-O7-round2-findings.md`, `LOG.md`.

## Method

1. **Receipts.** HO-2, HO-3, HO-8 copied verbatim (byte-identical to the overview files at `62cbb3cf`) and committed at
   `8f0c832a` with the reliance recorded in `LOG.md` (HO-2c as a constraint only; HO-3 item 3 for scope; HO-8 as a list
   of targets at their labels). Protocol satisfied.
2. **Replay.** Five scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 5/5 (`origin/REPLAY-LOG.txt`);
   stderr differs only by the thread's `exit 0` marker line.
3. **Independent check.** `origin/indep_checkO2.py` (own code, reads nothing; decision rule fixed before the first
   run): run 2 **6/6 CONFIRMED**, `INDEP-O2-FIXED`, replay identical. Run 1 (kept) was 4/6; both mismatches were
   defects of the coordinator's harness (sympy's primitive-integer form of a minimal polynomial compared with the
   monic form; a Python float zero in a symbolic comparison), none in a thread claim.
   - X1 (O7-D1) the SO(3) density certificate: `2 cos θ = √2 − 1/2` with minimal polynomial `x² + x − 7/4`
     (infinite order), `R01` of order 8, no common invariant line, `R01` moves the axis of `U` — with the classification
     of closed subgroups of SO(3) [L] the closure is SO(3).
   - X2 (O7-D2) the Hadamard pair of the coordinator's round-1 check X5 is infinite dihedral: both reflections fix the
     axis of their product exactly; closure a proper O(2). The round-1 reading "infinite order" stands; "density" was
     never claimed there, and the thread's correction of reading is accepted as an assumption-watch marker.
   - X3 (O5-T1a) exclusivity: with the 24 exchanges and one passive readout of any of the 14 nontrivial partitions of
     `{0,1}²`, every point mass is reachable from the uniform seed (exact BFS), so the body is the simplex.
   - X4 (O5-KB1) the KB-D instrument on the frame partition equals `forget_x ∘ Lüders_z` branch by branch.
   - X5 (O6-I) the Kochen–Specker circle tower: cosine law exact and repeatable; stage tables of rank 3 (single and
     two-step readouts, Pythagorean stages 1–4); `e^{ia}` (`cos a = 3/5`) of infinite order; the balanced value `1/2`
     reached only by the closure member `R(π/2)`, by no stage datum (`T_k(3/5) ≠ 0`, `k ≤ 60`).
   - X6 (O7-L3) level three, recomputed from scratch in the coordinator's own ordering of `Fin 2 × Fin 3` with exact
     Q(√2) arithmetic: `U = M1·M2` orthogonal; `Π = (2/3)(U + Uᵀ)` a rank-4 projector commuting with `U`, with
     `U + Uᵀ = 0` off its range and `= (3/2)Π` on it; the Lie algebra generated from `Y = Π(U − Uᵀ)Π/2` under the five
     adjacent transpositions and brackets has dimension 10 and annihilates the all-ones vector; under `Ad(M1)`,
     `Ad(M1ᵀ)` as well it has dimension 15 = dim so(6); the countercontrol `Y0` stays at 10. The argument that `Y` lies
     in the closure's Lie algebra (the circle `exp(φJ)` on the range of `Π`, from the density of `{U^{4k}}`) was
     re-derived and holds. With Cartan's theorem [L], the closure of `⟨mixImage 3 (π/4), permutations⟩` contains SO(6).
4. **Kernel citations.** All 23 `file:line` citations new in round 2 verified at L (`cite_check_r2.out`), including
   CompositionOrder.lean:378 `not_stagePreserving_of_infiniteOrderOn` (O6-K, CERTIFIED), :348, :149, :171;
   TransitiveBody.lean:109, :80; CompletionAction.lean:352; OperationalAssembly.lean:658, :675, :492, :515, :649;
   InternalObserver.lean:249, :290; StateMixingCoupling.lean:56–59; LieRankSource.lean:209; DiscreteCompletion.lean:1926,
   :1522, :1948.
5. **Design module.** `lean/OriginPassive.lean` (sha256 `5da5a6d4…`), `dev-origin/passive` @ `aef5d446` then
   `c2484cca`; runs 38090594001 and 38091462366 (`workflow_dispatch`): Mathlib bridge *Build* success (3645 jobs) in
   both; `lean-axioms` OK (5882, then 5884 named results, no sorry); release gate red only on `claims`, `duplicate`,
   `lean-manuscript` — `CI-RUNS-R2.md`. Design evidence only; nothing certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| O5-T1, O5-T1a | CONDITIONAL ([W] + [X] + [D]; kernel facts CERTIFIED) | accepted; X3 confirms the exclusivity on all 14 partitions; the sharpened Lemma P is a design-run theorem, not certified |
| O5-KB1 | CONDITIONAL | accepted; X4 |
| O5-a, O5-b | FAILED (as sources of KB-D) | accepted (replayed) |
| O5-a′, O5-d | CONDITIONAL (one-bit scope; SYMP + UPC, UPC circular) | accepted as labelled |
| O5-V | CONDITIONAL; source of KB-D OPEN | accepted |
| O5-SRC1, O5-SRC2 | CONDITIONAL (on KB-D2; HO-3 at its labels) | accepted; SRC via KB-D is token-only |
| O6-K | CERTIFIED (CompositionOrder.lean:378, :348) | verified at L |
| O6-T1 | CONDITIONAL ([W] tower step; [D] finite-order step composed with landed lemmas) | accepted; the finite-order step (an affine bijection of a polytope permutes its finitely many extreme points, hence has finite order) is elementary and the design module carries it |
| O6-T2, O6-L | CONDITIONAL | accepted (replayed) |
| O6-I | CONDITIONAL on the re-preparing law (outside the stated access) | accepted; X5 confirms the exact instance; scope note (circle and sphere substrata, not OI's lattice) recorded by the thread |
| O6-V | CONDITIONAL; the re-preparing law's source OPEN | accepted: the field-neutral Continuous Origin and the source of KB-D are one premise |
| O7-D1 … O7-D4, O7-C | CONDITIONAL ([X] + [W] + [L]) | accepted; X1, X2 confirm the certificates; O7-C's correction of reading accepted (an assumption-watch marker: infinite order is not density for reflections) |
| O7-L3 | CONDITIONAL ([X] exact Lie-algebra dimensions; [W]; [L] Cartan) | accepted; X6 reproduces 10 → 15 independently; O7-O superseded |
| O7-L3r1 | FAILED (as a verdict; kept) | the method correction between run 1 and run 2 is recorded in the script header and LOG; accepted |

**Label changes: none.**

## Recorded for the overview

- New assumption (watch marker): an **exclusive measure-and-re-prepare readout** — KB-D in discrete form, the cosine
  re-preparation law in continuous form — is the single open premise behind both the Discrete witness from monomial
  input and the field-neutral Continuous Origin. Its exclusivity contradicts the native passive Lüders readout.
- Eliminated alternatives: a memory bound and the kernel recorder as sources of KB-D; passive repeatable finite-rank
  towers as carriers of any infinite-order datum (hence of a drive); "two overlapping balanced mixers ⇒ dense control"
  for reflections (dihedral); SRC via KB-D as a route to a candidate pair cone (token-only).
- Positive results (conditional): the balanced rotation datum is dense in SO(3) on three states, and at the kernel's
  level three the generated group's closure contains SO(6) (SU(6) with the quarter phase): density without exactness.
- Thread deviations disclosed (a receipts commit that annotated a round-1 LOG entry, restored verbatim at `6f1c2895`;
  two LOG stamps ahead of the clock, corrected by a later entry; pre-run edits logged; the dev branch cut from
  `dev-origin/envelope`) — noted, no action.
- Round-ready: nothing. Routed: HO-9 (origin → bridge, equivalence).
