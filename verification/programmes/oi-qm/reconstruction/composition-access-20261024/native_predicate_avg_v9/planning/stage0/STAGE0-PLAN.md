# NP-AVG-1 Stage 0: masking geometry of the passive-readout class

26 October 2026. A draft preregistration for Issue #929. The owner approved a
Stage-0 plan on 2026-10-26. Stage 0 is a geometry-only investigation, not a
prediction experiment: it computes no probability law of the question's
objects, with the one exception of S6 below, which needs owner approval.

The re-check of draft r2 motivates it (`RECHECK-r2.md`, SHA-256
`676ecc085d3c2f329df6a05426550f8d6a914092bc553d678f844066f935d7a7`). Its §1
argues that under full averaging the L3 elimination removes every record
except the carrier boundary and "tie" configurations, and that collapsed
records reduce to v8 under the licensed convention.

Stage 0 does two things:
- it writes that argument out as a proposition with proof obligations;
- it checks the argument exactly, by an integer-geometry enumeration of the
  closure of every record.

Stage 1, the law machinery of `PLAN-r2.md` (SHA-256
`c9d8dbf86ab4b9add0fa030a157aeaab67df9d728e8baa22b99bfd85a05842c2`), runs, if
the owner approves it, only on what Stage 0 leaves.

Launching the Stage 0 enumeration needs owner approval, and it runs in CI
(§A.40, §A.43). The plan is committed alone, on a base containing
`fc452ea825b986a3babab5d110626e0019c39847`. Open items S1–S10 are in the last
section; each is written in at its proposed value.

**What Stage 0 does not claim.** Survivor counts are counts of configurations.
They imply nothing about unpredictability, computational hardness or quantum
behaviour. Any such reading needs a separate argument and is out of scope.
Empty, small or unfavourable survivor sets are all valid outcomes.

## 1. Configuration space (frozen)

The geometry is v8's: q9 at the origin, n = 6, the complete six-neighbour
two-slice rule x_t = x_{t−2} ⊕ H(Σ_e x_{t−1}(· + e)), and H a permutation of
the eight triples.

- **Region:** Reg = ball(4), the ℓ¹ ball of 129 sites.
- **Items:** (x, t) with x ∈ Reg and t ∈ {−1, …, 23}, read as whole triples at
  every slice −1..t. There are 3,225 items (O2).
- **Records:** sets of at most k = 2 items at distinct sites (O1). There are
  3,225 singles and C(129, 2) · 25² = 5,160,000 pairs. The empty record is the
  base context, reported separately (S10).
- **Fixed quantities** (never eliminated):
  - the carrier boundary Φ: the six neighbours of q9 at slice 7, and V = q9 at
    slice 8;
  - p = q9 at slice 6.
- **Port samples:** the port stream N[0..n], the whole triples at (0, 0, −3) at
  slices 0..6. They are public context quantities and are eliminable like
  record samples. Under G they are in-frame, so they are never eliminated
  there.
- **Context Ctx(R):** the fixed quantities, the port samples, and every sample
  of R's items.

**Equivalences** (frozen; each is counted, none excludes a record):
- **E1, identity merge.** A record sample at a Φ site-time, at p, or at a port
  sample is that quantity. Such a sample is "Φ in clear", "p in clear" or
  "port in clear".
- **E2, parity (L1).** Odd-class samples (|c| + t odd) are dropped from the
  context, as inert. Records whose even-class contexts coincide are
  *masking-equivalent*, and the number of distinct contexts is reported.
- **E3, unordered pairs.** Items at the same site are excluded, since they
  reduce to the longer one.
- **E4, symmetry.** The group of the masking geometry is the stabilizer, in
  the octahedral group O_h, of {Reg, q9, Φ's site set, port}. It is C4v
  (order 8): rotations about the z-axis and reflections in planes containing
  it. It fixes q8 and q10 and permutes m with the other three neighbours,
  which is also a symmetry of the A-law structure (J reads only q8 and q10).
  Without the port the group would be O_h (order 48). The sources G break
  C4v, but in both conventions G lies in the fixed part (A: absorbed in the
  reference pair; G: frame variables), so it does not enter the geometry.
  Laws on v8's frames are not symmetric; Stage 0 computes none.
- **Orbits** (computed as a design control, §9): 875 single-item orbits and
  815,175 pair orbits, equal by direct canonicalization and by Burnside's
  lemma.

## 2. Masking rules (frozen)

Two coordinate systems, with the cone radii stated as asymmetric.

**Convention A (reference pair (n+1, n+2) = (7, 8)), under the fair prior.**
- **F type** (slice t ≥ 8, depth d = t − 8):
  - cone: slice 8 within d, and slice 7 within d − 1;
  - near tips: c ± d·e on slice 8 (one tip, c itself, when d = 0);
  - far tips: c ± (d − 1)·e on slice 7, for d ≥ 1.
- **B type** (slice s ≤ 7, depth d = 7 − s):
  - cone: slice 7 within d, and slice 8 within d − 1;
  - near tips: c ± d·e on slice 7;
  - far tips: c ± (d − 1)·e on slice 8, for d ≥ 1.

Within the even class, the parity of every cone member matches automatically
(proof obligation PO1).

**Convention G (initial pair (−1, 0)).** Every quantity is F type from slice
0, with depth t:
- cone: slice 0 within t, and slice −1 within t − 1;
- near tips on slice 0 at distance t, far tips on slice −1 at distance t − 1.

A tip is eligible only if it is a *seed*, that is, outside the frame. The
frame is the union of the light cones of Φ, of p and of N[0..n].

**Rule L3′ (frozen, S2).** A non-fixed quantity q is eliminated if some
eligible tip u of q lies in the cone of no other currently retained quantity.
- Under A every tip is eligible; under G only seeds are.
- The rule is iterated to its fixed point. Fixed quantities are never
  eliminated.
- **ret(R)** is the retained set. Elimination is monotone and does not depend
  on the order (PO4).
- The near-only rule L3, the rule of `PLAN-r2.md` and of the re-check, is run
  as well and reported beside it. The labels use L3′.

**Why both tip classes.** A far-slice extreme x_E(u) enters the dynamics only
through x_{L+1}(u) = x_E(u) ⊕ H(Σ x_L(u ± e)). That is a bijection in x_E(u),
which then travels on the unique straight path, so it masks exactly as a near
tip does.

The toy design controls (§9) show three things:
- far-slice axis extremes are bijective, and off-axis far cells are not;
- L3′ never retains more than L3;
- one planted block separates the two rules. The constraint block minus its
  centre is fully masked: L3 keeps 7 of its 8 quantities, and L3′ keeps none.

Both rules are sufficient conditions only. "Retained" means "not eliminated by
the declared rule", not "informative".

## 3. Survivors (frozen definitions)

- **A-survivor:** S_A(R) = ret_A(R) ∖ (Φ ∪ {p}) is nonempty. Φ in clear and p
  in clear are Φ and p, by E1.
- **G-survivor:** S_G(R), the retained quantities that have at least one seed
  tip, is nonempty. The retained in-frame record samples are the *truncated
  record*.
- **Collapsed:** neither of the above holds.
- **Tie residue:** the set of A-survivors and G-survivors. Each survivor is
  stored with its canonical orbit representative.

**Classification of each survivor:**
- **Linkage (A).** *Φ-linked* if the union of the cones of S_A contains a Φ
  cell (a slice-7 neighbour of q9, or V); *J-linked* if it contains q8 or q10
  at slice 7; otherwise *unlinked*. Under the product prior, an unlinked S_A
  is independent of Φ (PO6).
- **Linkage (G).** *G-linked* if the union of the cones of S_G contains a
  source site at slice 0.
- **Observer interface.** Which retained quantities are public (record samples
  or port samples), and whether the survivor's retained set differs from the
  base context's.
- **Tie structure.** The cover graph (who covers which tip), its connected
  components, and the shared aligned tips: axis line, tip and reach.
- **Residual support:** the number of bits a Stage 1 law computation would
  enumerate, compared with S_max = 27.
- **Rule dependence:** whether the record is a survivor under L3, under L3′,
  or under both.

**Degeneracies.** Each is counted, none is excluded, and survivors are
cross-tabulated against each:
- items at q9;
- items at a Φ site;
- items at the port site;
- items on the z-axis (the port's axis line);
- pairs on a common axis line (the configurations that can tie);
- records with a nontrivial stabilizer (orbit size below 8);
- items with t ≤ 0, and items with t = −1;
- masking-equivalent records (E2);
- records whose last sample is odd-class.

Counterexamples are reported, not excluded. These include:
- records on which L3 and L3′ disagree;
- self-supporting dynamical-constraint blocks;
- any survivor contradicting a statement in `RECHECK-r2.md` §1.

## 4. The collapse proposition (stated; proof in the Stage 0 report)

The tip reach in direction e is c·e + d for a near tip. The aligned reach of q
is ρ(q) = ‖c‖_∞ + d, attained in the direction of c's largest coordinate (any
direction when c = 0).

**Proposition P_A.** If S_A(R) is nonempty, every ρ-maximal element of S_A(R)
shares its aligned near tip with another element of S_A(R) of the same type,
on the same axis line and at equal reach.

**Proposition P_G.** If S_G(R) is nonempty, every ρ-maximal element of S_G(R)
has |c| + t > 8, and shares its aligned near tip, which is then a seed, with
another element of S_G(R).

**Corollary C_A.** If R is collapsed under A, Law_A(Π_R) fails. The retained
public part is (p, V, and at most two of Φ's six slice-7 triples in clear).
- If q8 is read, Y is fixed, and both t1 and t0 put mass on both values of y.
- If q10 is read, R and Z are fixed, with the same consequence.
- If at most two of {m, o1, o2, o3} are read, the remaining fresh triples
  leave (q8, q10) uniform given the record, so J is uniform. That is neither
  t1/20 nor t0/44.

An unlinked survivor reduces to this case by PO6.

**Corollary C_G.** If R is collapsed under G, then on each frame Law_G(Π_R) is
Law_P of the truncated record. The truncated record is a set of site-times of
v8's domain, and v8 found it admissible in no family and not on the zero
background (`native_predicate_v8/REPORT.md:19-21, 37`). So Law_G fails on all
seventeen frames.

**Proof obligations.** Each is written out in the Stage 0 report.

| item | statement |
| --- | --- |
| PO1 | Cone radii as stated, forward and backward, with parity automatic in the even class |
| PO2 | L1, L2 (from `PLAN-r2.md`); L3′ near and far tips are bijective via the unique straight path |
| PO3 | Covering inequalities. A near tip of q at reach r lies in an opposite-type cone only if that quantity's reach in e is at least r + 1, and in a same-type cone only if the tip is shared at equal reach |
| PO4 | Iterated elimination is monotone and order-independent. The eliminated set is jointly independent of the retained set |
| PO5 | Φ-cover. Under A, fixed quantities cover only the Φ site-times: F near tips at q9 on slice 8, and B near tips at Φ's slice-7 sites. The aligned near tip of a non-fixed quantity is never a Φ site-time |
| PO6 | An S_A whose cones contain no Φ cell is independent of Φ under π. An S_G whose cones contain no source cell is independent of G given the frame |
| PO7 | The even part of the frame equals V's cone B8 (slice 0: even, \|c\| ≤ 8; slice −1: odd, \|c\| ≤ 7). A quantity with \|c\| + t ≤ 8 has its whole cone inside the frame |
| PO8 | C_A's three cases (the Φ-in-clear lemma) |
| PO9 | C_G's reduction to v8's per-family statement, covering records that are not stream-closed |

**Proof versus computation.**
- **Proof:** PO1–PO9, P_A, P_G, C_A and C_G. C_G also inherits v8's computed
  negative.
- **Computation:** ret_A and ret_G of every record, exactly; the survivor
  sets, classifications and counts; and, on every survivor, a mechanical check
  of the necessary conditions in P_A and P_G.
- **What neither does:** the enumeration computes no law, so the corollaries
  rest on proof alone. The exception is S6, an optional exact check of PO8.
  The propositions are necessary conditions, so a tied record that collapses
  is consistent with them.

## 5. Decision rule (preregistered)

Precedence, first match. Labels are generated from the measured values.

- **VOID:** a required control (§6) fails.
- **MISMATCH:** the computation contradicts a proof statement. That is, one of
  the following happens:
  - a survivor violates P_A or P_G;
  - a fixed quantity is eliminated;
  - a retained in-frame quantity's cone leaves the frame (PO7);
  - L3′ retains something L3 does not;
  - a record's retained set is not contained in the global closure bound;
  - a hand derivation in C6 disagrees with the code.

  The minimal witness is recorded. Neither the proposition nor the counts is
  then reported as established. Resolution needs a written amendment that names
  the error (proof or code), followed by a full re-run of every control.
  Neither side is preferred silently.
- **INCOMPLETE:** a shard is missing, failed, non-deterministic, or the
  merge's coverage check fails. No global label prints.
- **COLLAPSE_ALL:** every record is collapsed under A and under G. The report
  states that, by P_A, P_G, C_A and C_G, with the enumeration as their exact
  check:
  - Law_A fails for every record of C_avg(4, 16, 2);
  - Law_G fails on v8's seventeen frames.

  Stage 1 is not needed for k ≤ 2. This is a consistency-axis result.
- **RESIDUE_UNLINKED:** survivors exist, and all of them are unlinked under A
  and under G. Law_A and Law_G fail for them by PO6 with C_A and C_G. The
  residue is reported, and Stage 1 is not needed for k ≤ 2.
- **RESIDUE:** linked survivors exist. The classified residue is the output,
  and Stage 1, if approved, is restricted to it.

## 6. Required controls (each can fail)

- **C0, configuration space.** The following are checked:
  - the counts: 3,225 items, 3,225 singles and 5,160,000 pairs;
  - the orbit counts, 875 and 815,175, by direct canonicalization and by
    Burnside's lemma;
  - group orders 48 and 8;
  - ℓ¹-ball sizes equal the crystal-ball formula (OEIS A001845);
  - the context sizes per record.
- **C1, cone radii against the native rule.** On random backgrounds, single
  perturbations in a native evaluator, forward and backward from each pair,
  cover every depth used: A, F 0..15 and B 0..8; G, 0..23.
  - The measured dependence must lie inside the computed cone.
  - Both radii, d and d − 1, must be attained in the sample, which shows the
    sample is not vacuous and the asymmetry is real.
- **C2, tip bijection.** For every depth and direction class, near and far
  axis tips are bijective, by exhaustive test over the tip's eight values at
  sampled other values. The test runs forward and backward. Off-axis cells at
  the same distance must show non-bijective cases.
- **C3, planted ties.** Three planted cases, each run under A and under G
  geometry:
  - the dynamical-constraint block (a depth-1 quantity, its six near tips and
    its far centre) must be retained;
  - the block minus its centre must be eliminated under L3′;
  - the depth-2 planted set (the quantity, its six near tips and its six far
    tips) must be retained in full.
- **C4, off-axis mutant.** A closure that treats off-axis cells at distance d
  as tips must eliminate C3's depth-2 set. It is required to fail on that set.
- **C5, symmetric-radius countercontrol.** With far radius d in place of
  d − 1, the closure must retain a superset on every sampled record, and
  strictly more on a planted case.
- **C6, hand-checked instances.**
  - Toy: two F quantities on the +x line sharing their aligned tip collapse.
    The constraint block is retained; without its centre it is retained under
    L3 and eliminated under L3′. These are worked in `STAGE0-NOTES.md`.
  - At execution: the base context and the single item (q9, 9) are derived by
    hand in the report, before their computed values are read, and compared.
- **C7, a second closure implementation.** A separately written algorithm
  computes the greatest self-supporting subset from an explicit cover graph.
  It must agree on every survivor, on every record that contains any shared
  tip, and on a deterministic 1-in-1,000 sample of the rest.
- **C8, symmetry invariance.** Survivor status, survivor size and
  classification are constant on every C4v orbit. This is checked in full on
  every survivor's orbit, and on a deterministic 1-in-100 sample of orbits.
- **C9, monotonicity.**
  - For every record, ret_{L3′}(R) ⊆ ret_{L3}(R).
  - Every record's retained set lies inside the global closure bound (S1a),
    the closure of the union of all items' samples.
- **C10, fixed quantities and merges.** Φ and p are never eliminated. Under G,
  N[0..n] is retained as in-frame. E1 merges are counted.
- **C11, proposition check.** P_A and P_G are checked on every survivor. A
  failure is a MISMATCH, not a VOID.
- **C12, frame.** The frame's even part equals B8, and every retained in-frame
  quantity's cone lies in the frame.
- **C13, evidence form** (§A.44). Each shard writes structured output (stated
  schema, parameter digest, covered index ranges, per-record codes, counts,
  witnesses, its own SHA-256). The merge reads only these files and the exit
  status, and checks exact coverage and disjointness. Normal and `-O` runs are
  byte-identical, per shard and merged.
- **C14, static checks.** No floating point, no file read, no import outside
  the standard library, no author engine.
- **Mutants.** Each control above, broken in turn, must give VOID and name its
  target. The rule mutants are:
  - off-axis tips (C4);
  - symmetric radii (C5);
  - near-only tips, which C3's centre-removed block exposes;
  - swapped near and far slices;
  - a parity filter dropped.

  A mutant counts only when it fails on its named case.

## 7. Invariant → checkpoint

| invariant asserted | checkpoint |
| --- | --- |
| the configuration space and its counts are the frozen ones | C0 |
| the group is C4v and orbits are counted correctly | C0, C8 |
| cones match the native rule, with the asymmetric radii | C1, C5 |
| near and far axis tips are bijective; off-axis cells are not | C2, C4 |
| the detector retains genuine self-supporting structure | C3 |
| far tips are load-bearing beyond L3 | C3 (centre removed), near-only mutant |
| the closure is computed correctly | C6, C7 |
| closure results respect the symmetry | C8 |
| the rules and records are monotone | C9 |
| fixed quantities and merges are handled | C10 |
| the propositions agree with the computation | C11, the MISMATCH rule |
| the frame is B8, and in-frame cones stay inside it | C12 |
| the evidence is structured and complete, and the result deterministic | C13 |
| integer-only, no repository read | C14 |
| every control can fail | the mutant campaign |

## 8. Comparison with known results (before any novelty statement)

The Stage 0 report reads the following and states which parts of L2, L3′, P_A
and P_G are known. Candidates to check:
- **One-time pad, perfect secrecy.** Shannon (1949), "Communication theory of
  secrecy systems". L3′ is the masking-by-bijection argument.
- **Secret sharing and access structures.** Shamir (1979); Blakley (1979); Ito,
  Saito and Nishizeki (1987) for general access structures. The tie residue is
  the masking's qualified sets.
- **Secret sharing with reversible memory (second-order) cellular automata.**
  Martín del Rey, Pereira Mateus and Rodríguez Sánchez, *Appl. Math. Comput.*
  170 (2005). Shares there are consecutive configurations of
  x^{t+1} = f(x^t) ⊕ x^{t−1}.
- **Permutive cellular automata.** Hedlund (1969); later work on mixing and
  Bernoulli properties, including Shereshevsky. L3′ is extremal permutivity
  of v8's space-time map.
- **Expansive subdynamics.** Boyle and Lind (1997), for directional
  cone geometry.
- **Measure preservation by surjective cellular automata.** Hedlund (1969);
  Coven and Paul (1974). This is the context of L2.
- **Second-order reversible cellular automata.** Margolus (1984); Toffoli and
  Margolus (1987).
- **Light-cone and causal-cone counting.** The ℓ¹-ball counts (A001845), and
  causal cones of local circuits.

A statement that coincides with one of these is cited, not claimed. The
result specific to v8's geometry, the exact residue, is stated as a geometric
fact on the consistency axis.

## 9. Design controls run before freeze (owner-approved; no enumeration of v8's class)

Scripts and outputs are in `npavg/stage0-design/`, with SHA-256 values in
`STAGE0-NOTES.md`. All were run with `python3 -I -B`, standard library only.

- **`sym_check.py`.** Group orders: 48, then 8 with the port, then 8 with the
  labelled roles. The ball counts match A001845. The record space has 3,225
  items and 5,160,000 pairs, with orbits 875 and 815,175 (direct canonicalization
  equals Burnside). This is configuration combinatorics only; no masking was
  computed.
- **`toy_closure.py`, `toy_block.py`, `toy_fartip.py`.** These run on toy
  geometries: pair (2, 3), regions ball(1)–ball(2), no streams, no port. None
  of them is v8's class. Results:
  - the hand instance collapses;
  - no self-supporting sets of size 1–3 exist in a 75-quantity toy pool;
  - a 14-quantity block keeps the 8-quantity constraint block;
  - symmetric radii retain strictly more in 160 of 400 random toy sets and
    never less;
  - native cone radii are (d − 1, d) at depths 1–4;
  - near and far axis tips are bijective (0 failures in 300, and 0 in 200);
    far off-axis cells are not (87 non-bijective in 100);
  - L3′'s retained set lay inside L3's in all 300 random toy sets, and L3′
    separates the rules on the centre-removed block (0 retained against 7);
  - the off-axis mutant eliminates the depth-2 planted set (13 retained → 0),
    although it differs on no random toy set (0 of 400), so random tests are
    not enough to catch it.
  - **Timing:** the unoptimized prototype takes 2.65 ms per closure with 30
    quantities plus 8 fixed, near tips only.

## 10. Resources and launch

v8 contexts have at most 37 quantities: Φ, p, three even port samples, and up
to 26 even samples from two items. L3′ roughly doubles the tip count. The
unoptimized estimate is 4–8 ms per closure, so about 6–12 CPU-hours per
(convention, rule) pair over all 5,163,225 records. Running orbit
representatives (S4) cuts this by a factor of about 6.3.

The global closure bound (S1a) is a handful of closures with about 1,600
quantities each.

The run is sharded in CI (S7). A dry run prints the shard plan and context
sizes without computing any closure. Launching the enumeration, adding its
workflow and every dispatch need owner approval (§A.43 item 4). Local
pre-push checks (§A.40) are C0, C2–C6 on toys, C14, and compilation. Code,
controls, structured outputs, counts and the coverage limits are retained in
the package (§A.42).

## 11. Coverage limits (stated in every output)

- k ≤ 2 stream items, v8's region and slices, the scaled control only.
- One port. No later reads, unless S3 is extended.
- Conventions A and G with the declared frame.
- The masking rules L3′ and L3 only. Survivors are not shown to be informative.
- No law is computed, apart from S6 if approved.
- Nothing at actual L.
- No A1/A2 statement.
- No claim about OI beyond the class.

## 12. Open items for the owner (proposed values)

- **S1. Class and size extension.** k ≤ 2 stream items (O1/O2 at the review's
  recommendation). To address the smallest record that masking does not wipe
  out:
  - (a) **Global closure bound:** the closures, under A and G, of the union of
    all items' samples, and of each axis line's items. By monotonicity they
    bound the retained set of every record of any size. *Recommended for
    inclusion.*
  - (b) **Minimal self-supporting record search:** the smallest number m of
    items whose closure retains a Φ-linked quantity, for m ≤ 4. It is
    restricted to items whose samples meet (a)'s retained set, run on orbit
    representatives, and stopped at a budget, beyond which it is reported as
    not decided. *Proposed as a separately approved extension.*
  - (c) **k = 3**, pruned by P_A to records that can tie, with a 1-in-1,000
    audit of the pruned records. *Proposed only after (a) is seen.*
- **S2. Masking rules.** L3′ (near and far tips) for the labels, with near-only
  L3 reported beside it.
- **S3. Contexts.** Π_R contexts only. If the owner chooses to extend them:
  F2 contexts (the port continuation and the items' own continuations) for
  Π_R-survivors only, and `PLAN-r2.md`'s item (iii) per member, only for
  survivors.
- **S4. Enumeration form.** C4v orbit representatives, with C8's full-orbit
  checks. *Alternative:* the full enumeration, at about 6.3 times the cost.
- **S5. Second implementation sampling.** 1 in 1,000, plus every survivor and
  every record containing a tie.
- **S6. Exact check of PO8.** The law of J given (p, V, any at most two of
  Φ's six slice-7 triples), over 2^21 reference worlds and 22 subsets. It is a
  small law computation on the carrier, so it needs approval in a stage that is
  geometry-only. *Recommended.*
- **S7. CI budget.** 24 runner-hours over at most 32 shards, with a stop rule
  on the projected cost.
- **S8. Location.** `native_predicate_avg_v9/stage0/`, under O6's base rule.
- **S9. Literature list (§8).** Confirm, or add to it.
- **S10. Base context** (the empty record): reported separately, and
  hand-derived in C6.

The decisions O3–O9 of `PLAN-r2.md` concern Stage 1 and are unchanged.
