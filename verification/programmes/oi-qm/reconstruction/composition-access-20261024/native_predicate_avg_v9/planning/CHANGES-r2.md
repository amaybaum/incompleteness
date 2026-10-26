# Changes from draft r1 (`PLAN.md`) to r2 (`PLAN-r2.md`)

`PLAN.md` is unchanged and remains the reviewed object (SHA-256 `b0be3278…`).
The review is `../review/REVIEW.md` (SHA-256 `4d77c7c2…`). Section names below
are those of `PLAN-r2.md`.

## Required changes

| item | addressed in | how |
| --- | --- | --- |
| R1 | Freshness certificate; Decision rule | F1a, F1b and F2 are each required in A (exact screen) and in G on every frame. A G failure on any frame is a decided failure, with codes `F1a-G[frame]` and `F2-G[frame, member]`. |
| R2 | Decision rule | POS_A_SAMPLED_FRAMES is a distinct class with the review's text. PADS_NOT_FRESH's text names the seed declaration and does not assert the pointwise convention beyond it. The seed declaration has its own paragraph (Prior, conventions and seed declaration). |
| R3 | Decision rule (reason-code table; NEG_BOTH text) | Each failing R carries a check, convention, frame and member code; counts are printed. NEG_BOTH reports how many records were reduced by L1 or L3 and how many were enumerated and failed. |
| R4 | Fixed question; Objects (𝓛_R items i–ii); Computation 2; O1, O2 | Elements are v8's backward-closed stream items: 3,225 singles and 5,160,000 two-site pairs. A′ may use the whole closed record. F2 covers only samples after each item's last slice, plus the port and the O4 segments. |
| R5 | Required controls K6, K3, K3c | K6's second record is w2 = (A, R ⊕ u1.B, 0). K3 and K3c append in the clear. K3c's herald is in Π_R. K3d is added, as the review suggested. |
| R6 | Engines (GB, Z0, L2c); K4; protocol 3 | GB, a general-prior brute-force engine on reduced 1D and 2D instances and K6's block, carries L2c and Z0. Z0 is a three-way comparison (fair, zero, biased) on those instances, plus K2 with c fixed at 0 in 3D. K4 biases c alone, exactly, as a product factor. Protocol 3 is IM2 exhaustive over u on R's eliminations, plus brute force without L3 when it fits, plus separate-agent reproduction. |
| R7 | IM1, IM2 | IM1: the images from v8's native pair reproduce v8's values at every point of the domain through T_h, in all families and worlds. IM2: sampled and targeted soundness checks on the sweep's own eliminations (bijection in u, and cone containment by perturbation). |
| R8 | L1c | Measured by perturbation in the native scalar evaluator, with a non-vacuity condition, plus one GB law computed without L1 that includes an odd-class read. |
| R9 | Computation 5; Decision rule; Resources | Structured `shard-<s>.json` schema and a merge that reads only those files and exit status. Coverage, disjointness and determinism are checked before any negative class prints. A missing shard gives NOT_DECIDED. §A.44 is cited. |
| R10 | Internal consistency checks IC1–IC6; protocol 1–3; Decision rule | IC1–IC6 are enumerated, and each gives VOID on failure. Protocol 1 adds the residual excluding Φ, and is "not applicable" when that set is empty. The deferred state prints `_PENDING_REVIEW`. Protocol 2 is report-only (see the comments on the review). |
| R11 | Mutants | The injection mutants I1–I4 run on a fixed restricted set M, with outcomes stated per record. I3 is the off-axis L3 mutant. |
| R12 | Invariant → checkpoint; Scope; Inputs, pinned; Dependencies | The table now covers every asserted invariant the review listed. The scope adds T_h and 𝓛_R, the seventeen frames and the seed declaration. Every input is pinned by full SHA-256. The base must contain `fc452ea8`. |
| R13 | Computation 2; K1b | The verdict sweep is native-only, and the controls are separate runs. K1b's expected values are constants transcribed from v8's pinned `result.json`. |

## Nits

| nit | status |
| --- | --- |
| Φ contains the public p and V | adopted: "carrier boundary (p and V public; the rest private)" |
| N_old naming | adopted: port stream N[0..n] and N[n+1..T_h]; "eight actual-L ports" kept separate |
| "exact over-approximations" | adopted: "light cones over-approximate dependence" |
| G averages non-frame background as fair on the infinite lattice | adopted (conventions, G bullet) |
| AGENTS sections cited in a heading | adopted for the heading. §A.40, §A.43 and §A.44 stay cited in the Resources text, because R9 and the last nit ask for §A.44 there. |
| protocol 1 name | adopted: "pads are load-bearing"; "maximum-skepticism protocol" kept as #929's term |
| cite §A.44 for the sweep | adopted (Computation 5; Resources) |

## Also changed

- The statement on unrestricted later access is corrected per B4: it would
  also determine Φ, so it contradicts the access contract. It does not force
  PADS_NOT_FRESH by definition.
- The roles of the conventions are stated consistently per B6. A is the
  necessary screen; G is the licensed check under the seed declaration.
- F2's later-read family is computed by elimination on the union of the
  family's members, followed by an exact restriction to the residual Ω_R. This
  is my method for the O4 recommendation. It is sound because the family is
  downward closed and elimination is monotone.
- FR (frame soundness) and W1 (witness replay) are new controls. They fill the
  table rows the review flagged: the seed declaration, and witness replay.

## Comments on the review

1. **O3 certificate (partial disagreement).** The review suggests a mechanical
   L3-type proof that every averaged pad is a free axis extreme outside the
   frame. That covers only the averaged variables. A candidate's retained
   (non-eliminated) part is a function of the frame and G, so its law on every
   frame still needs an all-frame argument. r2 makes the certificate (a) that
   mechanical proof plus (b) a written argument of the Native A kind for the
   retained classes. Without (b) the result prints POS_A_SAMPLED_FRAMES.
2. **C5 / protocol 2.** I took the report-only option. Under the seed
   declaration, the G9 condition P(U | H, frame, Φ) = ν holds by construction
   for initial-variable seeds, so it would be vacuous as a criterion. The
   meaningful joint checks are F1a-G and F2-G (R1). The construction itself is
   measured by FR.
3. **A2's example (minor factual point).** The review's example
   x_{n+3}(q8) = q8 ⊕ H(V ⊕ four non-Φ slice-(n+2) triples) has the wrong
   count. q8 has six neighbours at slice n+2: q9, which carries V, and five
   cells outside Φ. The conclusion, that the cell is masked, is unchanged.
4. Every other finding I accept as stated, including B2: G is stricter than the
   contract's G9, so a G failure is relative to the seed declaration.
