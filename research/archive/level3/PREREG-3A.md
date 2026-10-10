# Level 3A — interface-capacity test for the linear leap rule (preregistration; written before any computation)

Base `0f2687b7`. Read-only, off-repo (scratchpad/level3); no act, freeze or repository implication. Inherits RECORD's
frozen definitions (record/FREEZE.md `b66b1a69`, record/RESULT.md §2 `dc759199`) literally where it says
"as RECORD". Designed from the premise ledger (ledger/SUMMARY-2.md `407fae0b`). Nothing in this document is a
criterion unless the section says so; §8 is a prediction and is marked as such.

## 0. Amendments before execution (owner, 2026-10-03; candidate `ffb58069` was never executed)

1. One primitive letter c is kept; a scope sentence on the word metric of {f, s, c} is added to §3.
2. Stage C is (4, 5), not (3, 5): only the effect depth increases over Stage B and the preparation set is nested,
   so rank comparisons across stages compare the same preparations (RECORD showed finite preparation sets
   understate dimension).
3. §5: R4-CLOSED requires a structural proof about the true orbit C(r; G₃); the sandwich argument is stated.

No criterion other than the Stage-C horizon changed.

## 1. The single question

For the existing linear leap rule, under the uniform product initial measure, observer OBS-R, measured effect
r = (o, outcome 1) and RECORD's record-writing class IC: does enlarging the local reversible action set from
{f, s} to {f, s, c} expose an observer-relevant system-effect sector of certified dimension exactly 4 — moving the
linear rule from UNDER-RANK (certified dimension 3 through horizon 4 at Level 2) to AT-RANK — and does any
interface in the class push it OVER-RANK?

This is an interface-capacity test. It is not a QM discrimination test and not a rule comparison.

## 2. Held fixed (every item as RECORD unless stated)

| Variable | Value | Ledger axis |
|---|---|---|
| Rule | linear, F = v_{i−1} + v_{i+1}; leap v^{t+1} = F(v^t) + v^{t−1} mod 2 — the only rule run | A5 kept, A4-S kept |
| Hidden-law class | uniform product measure on (u_i, v_i), i ∈ ℤ (invariant under the leap) | H₀ |
| Observer | OBS-R: site-0 pair (u_0, v_0) visible, all else hidden, record external and never read by the dynamics | OBS-1 |
| Record-writing class | IC: read b = v_0, append b, disturb (u_0, b) ↦ κ_b(u_0) with κ_b injective, one leap; 143 κ (passive excluded) | interface, κ part |
| Measured effect | r = (o, outcome 1), fixed here; not searched | r |
| Setting | field-neutral: exact integer count tables, probabilities in ℚ | setting |
| Preparation family rule | all protocols over the preparation alphabet of length ≤ L_p, conditioned on their record, positive weight | — |
| Effect family rule | protocols over the effect alphabet of length ≤ L_e with a singleton record event; record bits are never system effects | G-SPLIT |
| Non-selective generators | all non-selective letters of the interface; selective branches preserve nothing | G-FS |
| R4 definitions | R4(r; G), R4-global, orbit-span lemma, monotonicities (i)–(iii), as RESULT.md §2 | R4-MEASURED-EFFECT |
| Certification | rank-basis method (quotient/rankbasis.py: greedy mod p, exact ℚ independence and spanning); WELLDEF guard on every generator | — |
| Evidence classes | UNDER-RANK (< 4, nonterminal) · AT-RANK (= 4, nonterminal) · OVER-RANK (certified > 4, terminal for that κ) · R4-CLOSED only by a structural invariance/upper-bound theorem | — |

The alphabets are part of the interface and change in §3; the rules that generate the families from the alphabets
do not.

## 3. The one interface change: the local reversible action set

A **local reversible action** is a permutation of the four visible-pair configurations {0,1}², applied between
leaps, with no leap and no record. The set of all such actions is Sym({0,1}²), of order 24. Level 2 used
f: (u, v) ↦ (u, v ⊕ 1) and s: (u, v) ↦ (v, u), which generate the order-8 subgroup of actions that preserve the
register structure (verified by closure, design arithmetic).

Level 3A adds exactly one letter:

**c: (u, v) ↦ (u ⊕ v, v)** — flip register u exactly when register v = 1 (a conditional flip). In the pair code
p = u + 2v it is the transposition of codes 2 and 3, fixing 0 and 1.

- {f, s, c} generates all of Sym({0,1}²) (24 elements; design arithmetic, re-checked by the letter unit test §6).
  The other three conditional flips are words: s c s (flip v when u = 1), f c f (flip u when v = 0),
  s f c f s (flip v when u = 0).
- **Why field-neutral.** c is a bijection of a four-element configuration set, realized as a relabelling of the
  site-0 configuration exactly as f and s are; "conditional" is set-theoretic. No vector space over any field, no
  amplitude, phase or linear structure enters its definition. The name of any matrix that represents this
  permutation is not part of the definition.
- **Why one letter.** It is the minimal extension of {f, s} that generates the full action group. Admitting all
  four conditional flips as letters changes only word-length bookkeeping at ~2.5× the protocol count.
- Everything else in the interface is unchanged: κ class, record rule, leap after observation, m = o with the
  record forgotten.

**Scope of the finite-horizon experiment.** Horizons are measured in the word metric of the primitive letters
{f, s, c} (together with o, i, m). An interface giving each of the four conditional flips its own primitive letter
would generate the same permutation group but would be a different finite-horizon interface, with different
reachable sets at each L_p, L_e; no result here is a statement about that interface.

Alphabets: preparations {o, i, f, s, c}; effects {o, i, m, f, s, c}; generators **G₃ = {i, m, f, s, c}**.
G₂ ⊆ G₃ with the same κ and the same code for o, i, m, so by monotonicity (iii) OVER-RANK at Level 2 would
propagate to Level 3A; no linear κ was OVER-RANK at Level 2, so every linear κ is live here.

## 4. Horizons and stages

| Stage | κ set | L_p, L_e | Orbit words | Protocols per κ (concatenations) | Purpose |
|---|---|---|---|---|---|
| A | all 143 | 3, 3 | ≤ 2 | 156 × 259 = 40,404 (length ≤ 6) | filter: NOT-INVASIVE and OVER-RANK |
| B | every κ advancing from A | 4, 4 | ≤ 3 | 781 × 1,555 = 1,214,455 (length ≤ 8) | verdict stage |
| C | first three AT-RANK κ and the first UNDER-RANK κ (if any) in frozen interface order after B | 4, 5 | ≤ 4 | 781 × 9,331 = 7,287,511 (length ≤ 9) | depth probe of the orbit span over the Stage-B preparation set (nested: X_B ⊆ X_C) |

**Advance rule A → B (criterion):** a κ advances iff it is operationally invasive at Stage A and its certified
dim C_2 ≤ 4. Stage A does not need finite stabilization: the parity direction (effect "c s o") requires an orbit
word of length 2, so Stage A can show dim C_2 = 4 but cannot show C_2 = C_1 for such κ; Stage A filters, it does
not decide.

**Guard handling (criterion):** rank, WELLDEF, invasiveness and the dims C_k are computed for every κ at every
stage; a WELLDEF failure is recorded and gates only positive claims (AT-RANK, R4-CLOSED); it never removes an
OVER-RANK lower bound (orbit-span lemma, guard-independent), and it does not stop the job early.

Cost estimate, from Level-2 timings (not a criterion): Stage A ≈ 25 min on 4 cores; Stage B ≈ 18 min per κ per
core, so ≤ 6 h if all 76 Level-2-invasive κ advance; Stage C ≈ 2 h per κ per core, four κ in parallel.

## 5. Verdicts (criteria)

**Per κ, at Stage B** (Stage C can only add an OVER-RANK, by monotonicity (ii)):

- **NOT-INVASIVE:** no domain effect e has m·e ≠ i·e on any preparation. Reported with its rank; excluded from
  the capacity question.
- **OVER-RANK:** certified table rank > 4, or certified dim C_k > 4 for some k. Terminal for R4(r; G₃) at that κ;
  a table rank > 4 also excludes R4-global.
- **AT-RANK:** not OVER-RANK, certified table rank = 4, dim C_3 = dim C_2 = 4, WELLDEF holds. Nonterminal.
  (Then C_2 is the whole effect space on X, so its invariance is the invariance of everything.)
- **AT-RANK (unequal):** dim C_3 = 4 but C_3 ≠ C_2, i.e. the dimension 4 was first reached at word length 3.
  Nonterminal; reported separately from AT-RANK.
- **UNDER-RANK:** not OVER-RANK, dim C_3 < 4. Nonterminal.
- **INCONCLUSIVE:** rank certification fails, or WELLDEF fails where an AT-RANK claim depends on it (reported as
  "dimension 4 observed, guard failed").

**Level 3A label** (over the 143 κ, linear rule):

- **EXPOSED:** ≥ 1 κ AT-RANK and 0 κ OVER-RANK.
- **NOT-EXPOSED:** 0 κ AT-RANK (either kind) and 0 κ OVER-RANK.
- **OVER:** ≥ 1 κ OVER-RANK, whatever the others — this refutes §8 and excludes R4(r; G₃) at those κ.
- **INCONCLUSIVE:** none of the above decided, and some κ INCONCLUSIVE where the label depends on it.

No label is R4-CLOSED. R4-CLOSED for a κ requires a written structural theorem about the true orbit C(r; G₃) —
an upper bound dim C(r; G₃) ≤ 4 proved for the infinite-horizon object, not the success of §8 as a prediction —
with the computation as its control. Given such a proof, a certified finite-table lower bound of 4 sandwiches the
true dimension at exactly 4, and since the full orbit span is G₃-invariant by construction, R4-CLOSED follows.

## 6. Validation and replay plan

Code is written after this freeze and before any run; its sha256s are recorded in SEAL-3A.md before Stage A
starts. The reference simulator (record_sim.py) and fast evaluator (record_fast.py) are extended by the letter c
only, in new files; the sealed record/ directory is not modified.

1. **Letter unit test (exact):** on the radius-0 state, every word over {f, s, c} of length ≤ 4 acts on the pair
   as its abstract permutation; the generated group has 24 elements; {f, s} alone 8.
2. **V1′ brute force:** the extended reference simulator equals full-cone enumeration (validate_brute.py extended
   with c) on 40 random (κ, protocol) pairs per rule, all three rules exercised because the code is rule-generic;
   these outputs are validation samples, not results.
3. **V0′ fast = reference:** byte-equal on the full Stage-A protocol set for κ = ((0,1),(0,1)) and
   κ = ((1,3),(0,2)) (RECORD's gate and countercontrol κ), and on 300 random protocols of length ≤ 7 for three κ.
4. **Stage-A replay (fixed now, outcome-blind):** the nine κ at positions 0, 18, 36, 54, 72, 90, 108, 126, 142 of
   the frozen INTERFACES order, reproduced field by field on the reference simulator; plus, after the output
   exists, the first κ in frozen order of each verdict class not already covered.
5. **Stage-B replay:** the complete job for κ = ((0,1),(0,1)) if it advances, else the first advancing κ in
   frozen order, reproduced field by field on the reference simulator (MATCH required, as RECORD gate 4).
6. **G identities as faithfulness checks:** G2 forgetful sum, G3 normalization, G3 trailing-idle on all 143 κ at
   the Stage-A horizon (layers.py extended), plus the exchanged-branch countercontrol census over all 143 κ. Per
   L-G these are identities of the model, not evidence about nature; the census shows the check discriminates.
7. **Byte-identical rerun:** Stage A rerun once on the fast evaluator after Stages B and C; the JSON must match.

## 7. Interpretation limits (stated in advance)

- **Not evidence on A5 versus A4-S.** Only the linear rule runs; A5 and A4-S are both held. No 3A outcome bears on
  the attribution of RECORD's nonlinear/majority OVER-RANK to either premise; that is 3B's question.
- **Not a QM test.** AT-RANK, and R4-CLOSED if a theorem follows, assert a 4-dimensional effect sector. They say
  nothing about strict convexity, continuous reversible transitivity or any Q-layer premise. If the sector is the
  pair-marginal space its reachable states form a finite polytope (§8), which is not a qubit; that classification
  is a later Q round.
- **OBS-R only.** Nothing transfers to OBS-M or OBS-C without a stated map (OBS-1).
- **H₀ only.** §8's mechanism uses the product measure; nothing transfers to correlated hidden laws (3B's H block).
- **G-INV is relative to (linear, κ, I₃).** It is reported per κ and is not a property of the rule.
- **Not a search for r.** r is fixed; if the result is UNDER-RANK, no other seed is tried in this round.

## 8. Prediction (written now; not a criterion; falsified by any certified rank > 4 for the linear rule)

**Masking lemma (candidate, to be proved in writing after the run; the run is its control).** Under the linear
rule and the product measure, every leap writes v_0 ← v_{−1} + v_{1} + u_0, and v^t_{±1} contain the cone-edge
initial variables v^0_{±(t+1)} with coefficient 1. Those variables are independent of the record, of the pair
before the leap and of every disturbance so far (all functions of initial data within radius t). Hence after every
leap the pair is (v′, N) with v′ the post-action v-register and N a fair bit independent of everything observable,
and every protocol probability is a function of the prepared pair's marginal distribution alone. Consequence: the
system-effect space restricted to any preparation set has dimension ≤ 4 at every horizon, for every κ ∈ IC and
every action set. (The argument uses edge-permutivity — coefficient 1 on an edge variable — not linearity as such;
this bears on 3B's design, see PREREG-3B-DRAFT.md.)

**Predicted tallies, if the lemma holds** (numbers are predictions, not criteria):

- 0 κ OVER-RANK at any stage;
- the 64 κ whose two branch images differ in v on both branches: rank 1, nothing learnable, NOT-INVASIVE (as at
  Level 2);
- the 3 passive-type κ (v-image = b on both branches): NOT-INVASIVE, rank 4 (u becomes known after o; c moves the
  knowledge to the parity);
- the 76 κ invasive at Level 2: certified table rank 4 and dims C = [2, 3, 4, 4] at Stage B — the directions
  unit, P(v = 1) = r, P(u = 1) = s·r, P(u ⊕ v = 1) = (c s)·r, the last entering at word length 2 — so
  **AT-RANK for all 76 and label EXPOSED**;
- the reachable pure states are the six "one register function known, the rest fair" states (uniform on a
  2-element subset of the pair configurations), permuted transitively by Sym({0,1}²).

Design-time check (exact, no simulator; 2026-10-03 before the freeze): the partition of the 143 κ by the
v-images of their branch maps is 64 / 3 / 76, and the 76 coincide exactly with the linear rule's Level-2
operationally invasive set in the sealed artifact fast_stageA_L2.json `580d4721`. The mechanism therefore
retrodicts which κ were invasive at Level 2; this is consistency with existing data, not a 3A result.

If the prediction holds, the written lemma plus certified rank 4 and the structural invariance (every generator's
dual maps pair functionals to pair functionals) would give **R4-CLOSED** for the linear rule under I₃ — a
4-dimensional observer-relevant sector whose state set is a polytope; the Q question (why a ball rather than this
polytope) would then be posed with a fixed interface. If any certified rank exceeds 4, the lemma is false as
stated and a hidden correlation it claims masked is operationally visible; that would itself be the finding.
