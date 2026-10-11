# Coordinator audit — `research/equivalence`, round 3

Thread head `c10dbaee` (2026-10-11; round-3 commits `44c2708c` … `c10dbaee`). Base L = `9f9f8257`. Audited: the
round-3 rows of `RESULTS.md` (R-E12.1; R-E11.1 … R-E11.4; R-E13.1 … R-E13.4; R-E14.1 … R-E14.3; R-CITE.3),
`NOTES-E11.md`, `NOTES-E12.md`, `NOTES-E13.md`, `NOTES-E14.md`, `experiments/e11_k2_dict` (run 2; run 1 kept),
`e13_selfdual_body`, `e13b_central_selfdual`, `e14_hdyn_rings`, `e8_cite_check` (run 4; runs 1–3 kept), the design
modules `lean/EqvK2Schema.lean` (with the failed dispatch's copy `EqvK2Schema.run38099025197.lean`) and
`lean/EqvOmega4.lean`, the receipts in `inbox/`, the handoff proposals HP-8, HP-9, HP-10, the LEDGER's round-3 notes,
draft S4's update, `LOG.md`.

## Method

1. **Receipts.** HO-9 v1, HO-10 v1, HO-12 v1 and HO-15 v1 copied verbatim (sha256 `4b2c4a0f…`, `ef909f69…`,
   `b9584f3b…`, `f941456f…`, each equal to the overview file at `2a055180`, re-checked by the coordinator) and committed
   at `44c2708c`, with the reliance recorded in `LOG.md` before any research step: HO-9 item 3 only, as a CONDITIONAL
   constraint in the LEDGER notes; HO-10 items 1–2 as comparators for E11; HO-12 item 1 and the bridge's draft
   dictionary as E11's convergence target, items 2–4 recorded at their labels; HO-15 items 1–5 and its marker as E13's
   starting point, item 5 re-checked by E13's own computation. No earlier LOG entry was changed (three time
   corrections were appended forward). One recorded deviation: a cross-branch read of the bridge's draft
   `BridgeDictionary.lean` and NOTES-B9 §4, made on the coordinator's instruction. Protocol satisfied.
2. **Replay.** Five scripts re-run (`python3 -I -B`, cwd `experiments/`): `e11_k2_dict`, `e13_selfdual_body`,
   `e13b_central_selfdual`, `e14_hdyn_rings` stdout IDENTICAL at the head; `e8_cite_check` DIFFERENT at the head by
   one citation occurrence and one named pair (111/50 against the recorded 110/49) and IDENTICAL when replayed at its
   run commit `e2f522d3` in a detached worktree. The script scans the thread's documents, and the closing commit
   `c10dbaee` added a LEDGER note citing CompositionOrder.lean:378 after the run; the recorded output is a snapshot of
   the document tree at the run commit, and the thread's "replay identical" holds there
   (`equivalence/replay3/REPLAY-LOG.txt`).
3. **Independent check.** `equivalence/indep_checkE3.py` (own code; sympy and Fraction arithmetic; reads nothing from
   the thread; decision rule fixed before the first run): run 2 **8/8 CONFIRMED**, `INDEP-E3-FIXED`, replay identical.
   Run 1 (kept) scored 4/8 through four defects of the coordinator's harness, named in the script header (positive
   semidefiniteness decided by sympy eigenvalue signs, indeterminate on radicals; a countercontrol grid without
   antiparallel directions; a slope list yielding three arc points where six were demanded; an assertion that swap `J₀`
   lies on the ellipse, which the thread never claimed and which is false). No thread claim was involved.
   - X1 (E11): on exact random tables, `tr(dict ω · dict η) = ipW(ω, η)/4`, `tr(T_μν · dict η) = η_μν`,
     `Σ tr(T_μν H) T_μν = 4H`, `dict(tens X Y) = tokMat X ⊗ tokMat Y`, injectivity; PSD tables pair nonnegatively and
     the Bell defect pairs `−4` with the Bell projector's table.
   - X2 (E11): the kernel's `rotLin` on the target is `Ad(1 ⊗ diag(1, e^{it}))` and `cycEquiv` is `Ad(1 ⊗ U_J)`,
     `U_J = (I − i(X+Y+Z))/2`, through the dictionary (σ₁ → σ₂ → σ₃ → σ₁, the kernel's orientation); the drive
     generators and `Ad(CNOT)` preserve positive semidefiniteness on instances (principal minors, exact).
   - X3 (E13, Ω⋆): the weighted AM–GM identity `p³ + 2q³ − 3pq² = (p − q)²(p + 2q)`; nonnegative `M`-pairings on
     cube-parametrised points of the power cone; an exact outside point with a cone witness pairing `−7/24`; the
     meridian `x³ = (1 + y)(1 − y)²` is an irreducible cubic, so no conic contains it and Ω⋆ is no ellipsoid (the ball's
     meridian is a conic, control); `f''/f = −(2/9)(p + q)²`; the form without the cross term and the form with the
     opposite cross term each pair two cone points negatively (`−27/128`, `−99/64`).
   - X4 (E13, Ω_cs): `J₀` on `4u² + v² = 5`; the circle `u² + v² − (1254/325)(u + v) + 5114/845 = 0` through `J₀` and
     swap `J₀`, tangent to `π(J₀)` and, at swap `J₀`, to `π(g·swap J₀)`; the junction slopes `−19/44`, `−44/19`,
     `−76/11` with `C¹` matching from both sides; `M⁻¹ZMZ = g = (u/4, 4v)`; fourteen exact points of the arc `B₀` whose
     `M`-poles lie on the dual conic `E₀` and pair exactly 1 with their partners; over three periods (93 points,
     8649 ordered pairs) the minimum of `⟨Mx, y⟩` is exactly 1 and the 97 equalities are exactly the polar-partner
     pairs computed from the tangent lines; six points of Γ lie on no conic; countercontrols XB1 (no swap-invariant
     inner product makes the circle self-polar: the minor system has no solution) and XB2 (the `(2, 2)`-centred
     circle's polar conic misses `J₀`).
   - X5 (E14): exhaustive over all 40320 configuration permutations of the ring of 3 — exactly 48 satisfy (R-lit), and
     they are exactly the 48 site permutations with on-site relabelings; the top-stage condition holds for all 40320.
   - X6 (E14): the 384 site-permutation-relabelings of the ring of 4 satisfy (R-lit) on all 624 units; CNOT(0,1)
     violates it at `E^{0}_{0,1}` on both rings (4 and 8 image pairs, each also flipping site 1) while satisfying the
     top-stage condition; `T²` satisfies (R-lit) and carries site-0 units to site-2 units.
   - X7 (E14): the rule `x_i + x_{i+1} + x_{i+2}` has 16 images on the ring of 4 and 2 on the ring of 3; `(110)^∞` maps
     to `0^∞`.
   - X8 (E13): the chain is swap-symmetric; `J₀` is self-polar and swap `J₀`'s partner is `g·swap J₀`; `F` vanishes on
     the axes.
4. **Modules read.** `lean/EqvK2Schema.lean` (blob `659ae36c`): the 22 printed declarations are those of R-E11.1 …
   R-E11.3. `pairCone_eq_Q3_of_drive` has exactly five hypotheses — products of `eball 3` states in `K`,
   `cnot`-invariance, `K = dualW K`, invariance under `actT (rotLin t)` for every `t` and under `actT cycEquiv`, and
   `ReachPure` — and its proof derives closure under nonnegative scaling and addition from `K = dualW K`, applies
   `driveWords_preserve` and the two cone lemmas; no hidden hypothesis. Precision: the A_miss hypothesis is the
   full-flow form (HO-5), as the module's header states; HO-13 item 2's two-rotation clause is not formalized (the
   passage from two rotations to the flow uses closedness, which H3 supplies, and is not in the module). `Q3` is the set
   of tables with positive semidefinite dictionary image, `dualW` the dual under `ipW`; `ReachPure` quantifies over
   every `x`, the zero vector trivially. `lean/EqvOmega4.lean`'s fifteen declarations are those of R-E12.1.
   **Precision on R-E11.4.** The recorded fix "full expansion, then `ring`" fails in this module's rendering — a single
   `simp only` list carrying `Fin.sum_univ_four` together with `Matrix.sum_apply` — exactly as the job log shows
   (errors at 105:87, 122:67, 167:64, 235:2). The bridge's own round-3 module `BridgeDictionary.lean` renders the same
   fix in two stages (`simp only [dict, tokMat, tens_apply, Matrix.sum_apply, …]`, then `simp only [Fin.sum_univ_four]`,
   then `ring`) and builds (run 38099134414, 20/20). So the finding holds for the one-list rendering; the thread's
   repair (`Matrix.add_apply`, `Matrix.trace_add`) is one of two working renderings. No label changes.
5. **Written proofs read.** Ω⋆'s self-duality (both inclusions: weighted AM–GM for `C ⊆ C^{*M}`, the explicit witness
   `(k/u′, k/v′, −cX′)` for the converse, boundary cases included): sound. The lemma L-a (a `Z`-invariant
   self-dualizing form gives `Ω = aD⁻¹Ω°`, so `(D/a)^{1/2}Ω` is self-polar, hence the unit ball), L-b (`gᵀMg`
   self-dualizes for every cone automorphism; `h = M⁻¹ZᵀMZ` is a positive automorphism with `ZhZ = h⁻¹`, scalar iff `M`
   is `Z`-invariant; compactness modulo scalars forces the scalar case and contradicts the Lorentz cone), L-c: sound.
   Ω_cs: the junction identities verified exactly (X4); the global self-polarity of Γ rests on the envelope argument
   [W] and is supported by the exact sample (minimum pairing 1, equalities exactly the polar partners); strict
   convexity of Ω⋆ verified (`f''`), that of Ω_cs [W] from the strictly convex chain. E14: the (R-lit) collapse (the
   tracial state, pairwise orthogonal single-site projections at one site, the off-diagonal units): sound; the (R-01)
   passage, steps (1)–(5), read: a `{0,1}` self-adjoint idempotent is diagonal, so `α(D) ⊆ D`, and onto because `α(D)`
   is maximal abelian; Gelfand duality; a `{0,1}` partial isometry implements a partial bijection; the transport along
   `G`; finite range from locality preservation — CONJECTURE [W] as labelled, with the three standard facts the thread
   names as unchecked (the diagonal is maximal abelian; Gelfand duality for `C(Q^ι)`; the identification with the
   kernel's `transported`).
6. **Kernel citations.** The coordinator's sweep (`cite_check_r3.py`, lines added since `5d266133`) finds 61 distinct
   `File.lean:NNN` strings; four are the thread's own module lines or its countercontrol (`EqvK2Schema.lean:453`,
   `EqvOmega4.lean:530`, `EqvOmega4.lean:157`, `NoSuchModule.lean:1`); the remaining **57/57 resolve at L**
   (`cite_check_r3_equivalence.out`). The thread's own run 4 (54 distinct within its document scope) agrees.
7. **Design runs** (`CI-RUNS-R3.md`): 38096511360 (`dev-equivalence/omega4` @ `95beab2b`): Build success, `EqvOmega4`
   **15/15** prints standard, `lean-axioms` OK 5875, gate red only at `lean-manuscript`; 38099025197
   (`dev-equivalence/k2-schema` @ `472835c5`): Build **failure** at four proofs, 10 standard and 12 `sorryAx` prints,
   as the thread recorded; 38101580750 (@ `aabc649e`): Build success, `EqvK2Schema` **22/22**, `lean-axioms` OK 5882,
   gate red only at `lean-manuscript`. Each run 32 jobs success, 1 failure (the bridge job), nothing cancelled; the
   dev branches are cut from L. Design evidence only; nothing certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| R-E12.1 | CONJECTURE ([D], run 38096511360) | accepted; `C0` met by the rule fixed before the dispatch (15/15 verified in the job log) |
| R-E11.1 | CONJECTURE ([D], run 38101580750) | accepted; X1, X2; the module's statements read |
| R-E11.2 | CONJECTURE ([D]) | accepted; the cone lemmas read (LOWER through `psdFactorization_discharged`, BoundaryAudit.lean:100 at L; UPPER through the pairing identity) |
| R-E11.3 | CONDITIONAL on H2, H3, A_miss and `ReachPure`; implication [D] | accepted; the five hypotheses are exactly those stated; A_miss in the full-flow form (method 4) |
| R-E11.4 | CONJECTURE (two design runs) | accepted with the precision of method 4: true of the one-list rendering; the bridge's two-stage rendering builds |
| R-E13.1 | CONJECTURE (written proof, exact checks) | accepted; X3; the self-duality proof read |
| R-E13.2 | CONJECTURE (written proof) | accepted; L-a/L-b/L-c read (method 5) |
| R-E13.3 | CONJECTURE (written proof, exact checks) | accepted; X4, X8; the global self-polarity rests on the envelope argument [W], supported by the exact sample |
| R-E13.4 | CONJECTURE (as R-E2.6) | accepted |
| R-E14.1 | CONJECTURE (exact finite instances; written argument) | accepted; X5 (exhaustive), X6; the collapse proof read |
| R-E14.2 | CONJECTURE (written proof) | accepted at its label; the three unchecked standard facts as the thread states |
| R-E14.3 | CONJECTURE (written proof with literature; exact instances) | accepted; X7 |
| R-CITE.3 | measurement | accepted; the coordinator's sweep 57/57; the recorded output is a snapshot at `e2f522d3` (method 2) |

No label changes. The thread's recorded deviations (dev commits written by git plumbing, one import line per module in
the root `OIBridge.lean`, no local Lean toolchain, a floating-point scratch exploration used only to choose Ω_cs's
parameters before the exact probe, three LOG time corrections, the cross-branch read on instruction) are each in the
LOG and change nothing audited here.

## Handoff items

- HP-8 (the dictionary kernel-checked in a design run; the `dict_tens` finding) → **HO-18** to the bridge and the
  countermodels thread, with the rendering precision above and the convergence point: `dict_injective` is [D] in this
  module and OPEN in the bridge's.
- HP-9 (self-duality is not a source of K∞-Trans; Ω⋆, Ω_cs, the lemma, the sharpened marker) → **HO-19** to the
  countermodels and bridge threads; the marker recorded in the overview.
- HP-10 (S4 ready for owner review; S6's skeleton built in design; the infinite-volume form of H-DYN) is addressed to
  the coordinator and is recorded in `research/OVERVIEW.md` (round-ready findings; assumption-watch markers), not as a
  handoff.
