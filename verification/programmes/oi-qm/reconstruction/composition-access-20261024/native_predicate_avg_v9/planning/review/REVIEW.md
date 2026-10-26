# Pre-freeze review: NP-AVG-1 draft plan (Issue #929)

Reviewed: `npavg/draft/PLAN.md` (368 lines) and `npavg/draft/NOTES.md` (102 lines), against
`npavg/ISSUE-929.md`, the #912 worktree at `2af1d5d5` (programme dir
`composition-access-20261024/`, below `CA/`), `main` at `52e2db40` and `AGENTS.md`.
This review is read-only. The only executions were the drafter's v8 replay output compared with
`result.json` (`cmp`: identical) and the reviewer's lemma toy checks in `review/toy/`:
`lemmas.py` (random instances of v8's 3D rule) and `l2_1d.py` (an exhaustive 1D analogue).
Neither computes anything for the plan's question.

## Verdict: ACCEPT WITH CHANGES (not freezable as drafted)

The question, the prior and the three reductions are sound. The decision-rule skeleton is also
sound: partial sweeps cannot reach the negative classes, and the cap can only produce
`NOT_DECIDED`. But the plan has these defects:
- two of the three freshness checks run only under full averaging, which is the averaging the
  contract does not license;
- one control (K6) is VOID by construction;
- four controls or protocol steps cannot run as specified (K4, Z0, L2c, protocol 3);
- one control (L1c) restates the lemma it gates;
- the stream-closure treatment misclassifies records.

Every fix is a bounded edit to the plan. None needs a new design. After the changes, a short
re-review of the edited sections is enough.

## Findings

### A. The exact reductions L1–L3 (priority 1)

**A1. L1, L2 and L3 hold for v8's construction, with the conditions the plan states. Decidability
is unaffected.** (PLAN:111-131)
- **L1.** Under v8's rule (`CA/native_predicate_v8/checks.py:191-204`; the six-neighbour XOR, then
  `x_{t-2} ⊕ H(·)`), x+y+z+t mod 2 is preserved along every dependence edge. Φ, p, V and G are all
  even: the sources have coordinate sums −8, −6, −8 at t = 0, the pool is at |c| = 1 at t = 7, and
  V is at t = 8. Toy check: in 80 single-variable perturbations of random backgrounds, no change
  appeared outside the perturbed variable's parity class, and 1,127 same-parity changes did appear,
  so the test is not vacuous.
- **L2.** The induction is correct on the infinite lattice: (x_{t−1}|_W, x_t|_{W+1}) i.i.d. fair
  ⇒ (x_t, x_{t+1})|_W i.i.d. fair, and the same holds backward. Exhaustive 1D analogue (2^24
  worlds): the pair (1,2) at one site is exactly uniform under the fair prior, and takes 48
  distinct weights under bias 1/4, so L2c's bias branch can fail. L2 requires G to be uniform as
  well, which Native A's source law gives.
- **L3.** The unique-path argument is correct forward from slice 0 or n+2, and backward from slice
  n+1, because the backward rule has the same form. Toy check:
  - 60 forward and 30 backward random instances, all bijective in the axis extreme;
  - for an off-axis extreme at the same distance, 48 of 60 were not bijective, so the axis
    restriction is load-bearing.

  Iterated elimination is sound and order-independent. Removing a quantity can only free further
  extremes, and the eliminated set is jointly independent of the retained set (the induction is
  short; the report should write it out). L3 needs u uniform, so it applies only to fair variables:
  A in reference coordinates, and G on non-frame variables. The plan restricts it correctly
  (PLAN:120-121, 137-138).

**A2. L3 is the load-bearing step of any negative under A, and its controls do not exercise the
engine that applies it.** Under A in reference coordinates, Φ is seven i.i.d. fair triples,
independent of every other pair variable (L2). Iterated L3 therefore makes most native site-times
independent of Φ. One example, derived from the lemmas only: x_{n+3}(q8) = q8 ⊕ H(V ⊕ four non-Φ
slice-(n+2) triples). A negative under A will thus mostly arise by *masking*, where the cells carry
no carrier information, and not by the *leakage* v8 found under P. An L3 implementation bug that
over-eliminates would produce exactly this negative, spuriously.

Against that, the controls are:
- L3c tests only "small cones" (PLAN:215-218);
- x1 checks v8's initial-coordinate evaluator (PLAN:219-221), not the new reference-coordinate
  forward and backward image engine.

Nothing ties the reference-coordinate images to the native fields (see Required change R7).

**A3. L1c restates its claim** (PLAN:210-211).
- "The exact cone dependence set has the stated parity" is a geometric computation of the cone
  with the parity filter. It cannot fail unless the filter's own code is wrong.
- "A planted odd-class read leaves every law unchanged" is tautological if the engine drops
  odd-class quantities by L1.

The control must measure *actual* dependence: perturb initial variables in the native evaluator,
as `review/toy/lemmas.py` does, and compute one law by brute force without L1 (R8).

**A4. L2c, K4, Z0 and protocol step 3 cannot run as specified** (PLAN:137-138, 194-196, 207-214,
242-245). In initial coordinates, Φ's backward cone is 833 slice-0 sites plus 575 slice-(−1)
sites: 1,408 triples, about 4.2 × 10³ bits.
- **L2c** asks for "exhaustive enumeration in initial coordinates" of Φ, p, V and three nearby
  site-times "on small windows". In 3D even the pair (1,2) at a single site is 96 bits. L2c
  therefore needs a stated reduced instance: fewer ticks, a lower-dimensional analogue, or both.
- **K4** "in initial coordinates without L2 or L3", with bias on every non-source bit, has no
  feasible exact method as written. With bias on c alone it is feasible, since c is independent of
  everything else. Open item 9 is therefore partly a feasibility question.
- **Z0**: A's engine is L2-based and valid only under the fair prior, so it cannot run under the
  zero point mass. As written, "A equals P on the zero background" can only compare the P engine
  with itself. That is vacuous, and it is the only checkpoint for the invariant "averaging is the
  only difference from P" (PLAN:279).
- **Protocol 3** (a second engine in initial coordinates) exceeds any cap for a native R near Φ,
  so every candidate POS_A falls to the "separate-agent review" branch. The decision rule does not
  say what verdict is printed then (see C4).

### B. Conventions and the freshness certificate (priority 3)

**B1. F1a and F2 run only under convention A, which averages over the frame, the background in
Φ's own cones.** That is the averaging the contract does not license. The drafter states this for
the law (NOTES:55-60; `CA/REPORT.md:59-64`: "X_relevant includes all non-seed variables used by
the stage"), but F1a and F2 remain A-only (PLAN:93-97, 100-102). F1b checks only the J-law under
G. So the certificate never checks two things given the frame:
- (i) conditional independence of w_R and Φ;
- (ii) the later-port law.

Constructive gap for (ii): take w_R = Y ⊕ c, with c a non-frame fresh bit, and a later port
carrying c ⊕ b, where b is a frame bit independent of Φ under A. L3 makes this generic. F2 under A
passes, because b masks Y. Given the frame, Y is revealed. The analogue for (i) is a leak of
K ⊕ b: F1a passes and F1b passes, because J's law is unaffected. This is exactly the
"fair-after-heralding" class of hazard the contract names (`CA/REPORT.md:151-157`). See R1.

**B2. F1b is a sampled pass, but an exact failure only for one conservative seed declaration.**
G conditions on the geometric union of the backward cones of Φ and N_old (PLAN:77-79). G9
requires conditioning on the public history's *values* H = h and on the variables the stage
*uses* (`CA/REPORT.md:59-67`, "in a way that changes the relevant joint law"). Two consequences
follow:
- Background in N_old's cone that N_old does not reveal, and background in Φ's geometric cone
  that Φ does not depend on, are admissible seeds that G freezes. G is therefore *stricter* than
  G9. An F1b failure is an exact witness against the declaration "seeds = background outside the
  cones of Φ and N_old", not against every licensed averaging.
- A pass on 17 frames certifies nothing about the other frames.

The decision rule ignores both directions. POS_A lists "F1b" without qualification (PLAN:158-159),
and PADS_NOT_FRESH counts an F1b failure as a "decided failure" (PLAN:160-163). The 17-frame
limitation appears only in protocol 6 (PLAN:249-252), which is a caveat and not the verdict text.
See R2 and owner decision O3.

**B3. A failure of F1a is a carrier leak, not a pad failure.** PADS_NOT_FRESH pools failures of
F1a, F1b and F2 (PLAN:160-163). In #929 this class means "the pointwise convention is then forced,
and this result shows why" (ISSUE:49). An R that passes the J-law but leaks K beyond A′ fails
F1a without any pad being involved. The verdict must carry the failing check and its convention
for each R (R3).

**B4. "Every later public port": the declared-ports reading is right, but the stated consequence of
the alternative is not, and a middle reading is omitted** (PLAN:104-107; NOTES:64-66).
- The declared-ports reading is the one consistent with #929's "Access stays supplied"
  (ISSUE:24).
- Unrestricted later access would not give PADS_NOT_FRESH "by definition". A large later window
  also determines Φ, so the private carrier, and with it the v6 and v7 reference, fails as well.
  That reading contradicts the supplied access contract; it is not a freshness verdict.
- A middle reading is omitted: later reads of the class's own kind, meaning at most k site-times
  (or streams) in the radius-ρ region through T_h.

Under A with an infinite fair background, L3 masks almost every sample of a single fixed port. F2
against one port is therefore close to vacuous for native R; only K3 and K3c exercise it. This
should be stated, and the owner should choose whether F2 includes later in-region reads (O4).

**B5. Stream closure in F2 is incoherent as specified** (PLAN:54-55, 100-102, 145-146; NOTES:87-88;
open item 6).
- v8's class element is a *stream item* (site x, read at every slice −1..t;
  `CA/native_predicate_v8/checks.py:503-508`). It is not a bare site-time. "Stream closure leaves
  only the two initial slices" holds only if k counts site-times. With k counting v8's stream
  items, the counts are unchanged: 3,225 single items, and C(129,2)·25² = 5,160,000 two-site pairs.
- F2 requires "A′ unchanged as a function of Π_R" over the closure in *both* directions. The
  earlier samples (−1..t) are public history *before* use. The flag may legitimately depend on
  them, and G9 conditions on them. So an R whose earlier stream refines the posterior is recorded
  as a freshness failure, when it is in fact a different admissible record.

The coherent version is v8's: R is at most k stream items, with backward closure imposed and A′
any function of the closed record; F2 covers only samples after each item's last slice, through
T_h, plus the port (R4, O2).

**B6. The plan calls A "the cone form the question asks for" (PLAN:75-76), while NOTES:55-60 calls
G the licensed form.** State it consistently: Law_A is a necessary screen, because G on every
frame implies A (PLAN:84-87, correct); the licensed form is G with seeds declared as in B2.

### C. Decision rule and outcome classes (priority 2)

**C1. The precedence is sound.**
- PADS_NOT_FRESH and NEG_BOTH both require every R to be decided (PLAN:160-165), so a partial
  sweep or the cap yields NOT_DECIDED.
- POS_A is existential, so reaching it on a partial sweep is correct.
- "and K1 holds" in NEG_BOTH is redundant with VOID, which is harmless.

The precedence also needs a **completeness gate** for the sharded CI sweep. §A.44 (worktree
`AGENTS.md:1016-1040`) requires the verdict to read structured shard outputs, not logs. The merge
step must prove coverage of exactly 3,225 + 5,198,700 sets (or the R4 counts) before NEG_BOTH or
PADS_NOT_FRESH can print. A missing or failed shard gives NOT_DECIDED (R9).

**C2. VOID's "any internal consistency check" is not enumerated** (PLAN:156-157). §A.41 needs each
one named, with a checkpoint. Candidates:
- Law_P on a frame ⇒ Law_G on that frame for the same R and A′;
- Law_G on all 17 frames ⇒ the per-frame accept maps agree as functions of Π_R;
- F2 ⇒ Law_A(Π_R);
- probability mass conserved per class;
- the shard union is the class (R9).

**C3. Protocol 1 can VOID a genuine positive** (PLAN:237-238). If R's record is a function of Φ
alone, there are no pads; adding "the residual variables" cannot make F2 fail, and the verdict
becomes VOID. If the residual includes Φ, the step is trivially satisfied. Restrict the added
variables to the residual minus Φ's seven triples. If that set is empty, mark the step not
applicable instead of VOID.

**C4. The verdict when protocol 3 defers is undefined** (PLAN:242-245). A candidate that passes
Law_A, F1a, F1b and F2 but awaits separate review is neither POS_A nor any other class. The rule
must print a named state: either NOT_DECIDED with the candidate listed, or a distinct
`POS_A_PENDING_REVIEW`.

**C5. Protocol 2 has no pass criterion** (PLAN:239-241). It is "computed and reported", with
"per-cell freshness is not accepted". Either make it the G9 condition itself, evaluated jointly on
the frames (P(U_R | H = h, X_relevant = x) = ν), as a required criterion, or label it report-only.
For |R| ≤ 2 the joint law is already what Law_A computes, so the label is the honest option unless
R1 is adopted.

**C6. POS_A skepticism (§A.31): the main hidden assumption is missing.** Under A, the i.i.d. fair
background acts as an unlimited one-time-pad bank, by L2 and L3. Protocol 4 reports the bias-1/4
law but cannot compute it for a native R (A4). The POS_A verdict text should therefore state:
- that prior dependence was not computed, if it was not;
- that the pads are initial background bits, whose fairness at actual L is the named F2-ledger
  item (ISSUE:22).

**C7. The planted controls must not enter the verdict sweep.** v8 ran x3 through the search
separately. The plan should state that the verdict sweep is over native R only, and that every K
control is a separate run of the same classifier.

### D. Controls (priority 4)

**D1. K6 is VOID by construction** (PLAN:200-206). w2 = (0, R ⊕ u1.B, 0) carries no flag. Alone it
leaves Pr(J | Q) = Pr(J | p, V, N_old), and under A that is uniform: p ⊥ pool given V, because
the three other neighbours are fresh under L2. That is neither target, so "each … alone passes
Law_A" is false for w2. The fix is w2 = (A, R ⊕ u1.B, 0). Then u0 = u1 (transport audit,
`main:…/transport_audit_v1/REPORT.md:188-203`) makes the pair reveal Y ⊕ R, which fails, while
each cell alone passes. K6 is also the natural L3 sharing control: u0 and u1 share every extreme.

**D2. K3 is ambiguous where it matters** (PLAN:187-188). "c added to the port at slice n+5" could
mean XOR into the native port triple. Under A that triple is L3-masked: the port at
(0, 0, −3, n+5) has five free slice-(n+2) axis extremes. F2 would then correctly *pass*, K3 would
fail, and the run would be VOID. Specify that c is appended to the port record in the clear. The
same applies to c2 in K3c.

**D3. K3c**: state that the herald at slice 0 belongs to Π_R as pre-use history, not to E_R.
Consider a K3d, where the herald is [c = o.B] with o the hidden +x neighbour. That is the exact
`CA/REPORT.md:151-157` hazard, against F1a and F1b rather than F2.

**D4. K1a and K1b are split correctly** (PLAN:177-183). K1a tests the inputs. K1b is a real control
of the new P engine and can fail (it requires matching `native_table_sha256` field for field).
- K1b's `admissible_R_exists` and `law_good_partitions_per_v` are v8's all-R search, not the
  |R| ≤ 2 search. State that the P engine implements v8's full search.
- State that K1b's expected values are transcribed constants with provenance, because the checker
  reads no repository file (PLAN:304-305).

**D5. K2, K3b and K5 can fail as specified.**
- K2: Law_P fails because c is fixed by C0. F1b passes because c is outside the frame.
- K3b: o at (1, 0, 0, n+1) is not reached by G (distance ≥ 9 > 7), so it is fixed by the frame
  and F1b fails. Under A, F1a fails while Law_A passes.
- K5 is a weak control but a valid one.

**D6. The injection mutants' expected verdicts depend on the measurement** (PLAN:226-231).
"K2's plant in a native site-time gives POS_A" requires protocol 3, which defers (A4, C4).
"Adding K3's reuse gives PADS_NOT_FRESH" holds only if the base sweep is fully decided and has no
other Law_A R. Run the injection mutants on a fixed restricted candidate set, or state their
expected per-R classification instead of the global verdict. Add an L3 mutant that accepts
off-axis extremes; the toy check shows L3c can catch it.

### E. Open items and proposed values (priority 5)

**E1.** No value looks chosen to favour an outcome.
- k = 2 and S_max = 27 are feasibility bounds. Exceeding either gives only NOT_DECIDED, never a
  false verdict.
- T_h = 46 is the stricter of the two horizon options: v7's alternative, the last first G arrival
  at the port, is slice 11.
- The frames are the existing ones.

**E2. k = 2 with stream closure checked in F2 is not coherent; see B5.**

**E3. K4 scope (item 9)**: "every non-source bit" is infeasible as specified (A4). Bias on c alone
is feasible and is enough for an engine control.

### F. §A.41 table (priority 6)

The following asserted invariants have no checkpoint:
- the reference-coordinate image engine equals the native rule (only x1 exists, and it covers
  initial coordinates);
- the port geometry (slice 9 = n+3 first arrival; offsets 3, 5, 5; PLAN:50-53);
- the frame definition and the frame list, which should be hashed in K0;
- "the checker reads no repository file and imports no author engine" (PLAN:304-305), which needs
  a static check;
- shard coverage and structured merge (C1);
- the internal consistency checks (C2);
- exact witnesses for PADS_NOT_FRESH (PLAN:161-163), whose replay through an independent
  evaluator is unchecked;
- "averaging is the only difference from P", whose only checkpoint is Z0, which is vacuous (A4).

### G. Scope and dependencies (priority 7)

**G1. Scope** (PLAN:286-300) omits three limits:
- freshness is not tested beyond T_h, or against any later read other than one port and R's
  stream (#929 names "leaks beyond the declared horizon", ISSUE:39);
- F1b covers 17 frames;
- the seed declaration of B2.

**G2. Location** (PLAN:366-367; ISSUE:73) is "#912's guiding draft or a linked successor from a
current D". K1a needs v8's files in the tree, and `fc452ea8` is not on `main`: the object is absent
from the local `main` clone, and the drafter checked it against `52e2db40`. A successor whose `D`
is current `main` cannot run K1a until #912 lands. The plan should require a base that contains
`fc452ea8`.

**G3. Pins**: PLAN:177-178 and NOTES:9-22 use 8-hex git blob ids. They match the worktree
(`0a53c776…`, `9ef92ae4…`, `9f5e5bd1…`, `2f77fe2f…`). v8's own plan pinned full SHA-256
(`CA/native_predicate_v8/PLAN.md:62-78`). A frozen preregistration should do the same for every
input: v8 `checks.py`, `result.json`, `PLAN.md`; v6 and v7 `REPORT.md`; the transport audit;
`history_v11`.

**G4. #923**: PLAN:321-327 is a read-only compatibility analysis. #929 asks for "prior
coordination" (ISSUE:80), which is the owner's call.

**G5. §A.42** (PLAN:316-319) is handled correctly for results. The plan itself cites `fc452ea8`;
if it lands on `main` before v8 does, it cites off-main content, so the same rule should cover the
plan.

### H. Register and fitness (priority 8)

The plan follows v8's house style, makes no claim about OI beyond the construction class, and its
scope paragraph is properly negative-scoped (PLAN:296-297). Minor points are listed under Nits.

## Required changes before freeze

- **R1.** Add F1a-G and F2-G: evaluate w_R ⊥ Φ | (p, V, N_old, A′, frame), and
  Law_G(Π_R ∪ E_R) with A′ fixed, on every frame. Keep the A versions as exact screens. POS_A
  requires F1a, F1b and F2 in both conventions; a G failure on any frame is a decided failure.
- **R2.** Fix the verdict text in the decision rule.
  - POS_A's text names "freshness against stage inputs checked on 17 frames; not certified on
    other frames", unless O3 adopts an exact all-frame certificate.
  - PADS_NOT_FRESH's text names the seed declaration (background outside the cones of Φ and
    N_old). It does not assert "pointwise convention forced" beyond that declaration.
- **R3.** Give each failing R a reason code (F1a carrier leak / F1b input-correlated pad / F2 later
  reuse; convention; frame), and print the counts in the verdict. Also report the NEG mechanism:
  L1 or L3 reduced to independence of Φ, versus enumerated and failed.
- **R4.** Redefine the class elements as v8 stream items (site x, last slice t, read at −1..t),
  with |R| ≤ k items. Remove "A′ unchanged" from the earlier half of the closure. F2's E_R becomes
  the port plus each item's samples after t through T_h. Restate the counts. Owner confirmation:
  O2.
- **R5.** Fix K6 to w2 = (A, R ⊕ u1.B, 0). Specify K3 and K3c as in-the-clear appends. Put K3c's
  herald in Π_R.
- **R6.** Give a feasible exact method, or a reduced instance, for L2c, K4 (bias on c alone, or a
  stated structural method), Z0 and protocol 3. Z0 must exercise an engine that accepts an
  arbitrary prior on the instance where it runs; otherwise drop the invariant row it supports.
- **R7.** Add an image-engine control. On all 16 families, the reference-coordinate forward and
  backward images, evaluated from v8's native pair (n+1, n+2), must reproduce v8's native value
  at every site-time in the domain and the initial pair. Also add an L3-soundness check on the
  sweep's own eliminations: for a deterministic sample of performed eliminations, verify
  bijectivity in u at random fixed other values, and cone containment by perturbation.
- **R8.** Rewrite L1c to measure actual dependence: perturbation in the native evaluator, plus one
  brute-force law with an odd-class read, computed without L1.
- **R9.** Write shard outputs as structured files in a stated schema (§A.44). The merge verifies
  complete coverage before NEG_BOTH or PADS_NOT_FRESH; a missing shard gives NOT_DECIDED.
  Determinism is checked per shard and on the merged file.
- **R10.** Enumerate the internal consistency checks (C2). Define protocol 1 per C3, the deferred
  state per C4, and protocol 2's status per C5.
- **R11.** Define the injection mutants on a restricted candidate set with stated per-R outcomes
  (D6). Add the off-axis L3 mutant.
- **R12.** Complete the §A.41 table (F) and the scope list (G1). Pin every input by full SHA-256
  (G3). Require a base containing `fc452ea8` (G2).
- **R13.** State that the verdict sweep is native-only and that the controls are separate runs
  (C7). State that K1b's expected values are transcribed constants (D4).

## Owner decisions

- **O1. k = 2** (item 1). Recommend accepting it, with the class counted in stream items (R4).
- **O2. Stream closure** (item 6). Recommend v8's backward-closed stream items, with F2 forward
  only (B5). The alternative, bare site-times, must at least drop "A′ unchanged" on earlier
  samples.
- **O3. All-frame freshness** (item 5). Recommend that POS_A require an exact all-frame
  certificate, for example a mechanical L3-type proof that every averaged pad is a free axis
  extreme outside the frame, which holds "for every fixed value of all other variables". Failing
  that, the sampled result prints as a distinct `POS_A_SAMPLED_FRAMES` class. Do not report POS_A
  on 17 frames under the unqualified name.
- **O4. Later ports** (item 4 / B4). Recommend adding later in-region reads of the class's own kind
  (≤ k items after R, through T_h) to F2, or recording explicitly that F2 is against one port
  only, which is near-vacuous under A.
- **O5. K4 scope** (item 9). Recommend c alone (feasible). Record prior dependence of a native
  result as "not computed" where it is not computable.
- **O6. Location and base** (item 11). Recommend #912's guiding draft, or a successor based on a
  commit containing `fc452ea8` (G2).
- **O7. #923 coordination** (G4). The owner confirms, or cross-links, before freeze.
- **O8. Frames** (item 10) and **CI budget** (item 12). Accept. Optionally add independently
  seeded fair frames: it is cheap, and it narrows B2's sampling gap without changing the rule.
- **O9. T_h = 46 and S_max = 27** (items 2–3). Accept. T_h = 46 is the stricter horizon.

## Nits

- PLAN:44: Φ contains the public p and V. Say "carrier boundary (p and V public; the rest
  private)".
- PLAN:47-55: "N_old" names one port whose later stream is in E_R. Call it the port stream
  N[0..n] and N[n+1..T_h]. "Old ports" in v8 means the eight actual-L ports.
- PLAN:131: "Cones are exact over-approximations" should read "light cones over-approximate
  dependence".
- PLAN:66-69 and 77-82: state that G averages the non-frame background as fair on the infinite
  lattice, even where v8's families are zero outside radius 27.
- PLAN:302: "(§A.40, §A.43)" in a heading; v8's plan cites no AGENTS sections in its body.
  Optional.
- PLAN:159 and 233: "maximum-skepticism protocol" is #929's term. Keep it, but call protocol 1
  "pads are load-bearing", the v7 c1 idiom.
- NOTES:36 cites §A.40–§A.44 from `main`. The plan should also cite §A.44 where it governs the
  sweep (R9).
