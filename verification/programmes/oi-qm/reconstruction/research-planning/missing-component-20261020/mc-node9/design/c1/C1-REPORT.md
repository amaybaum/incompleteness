# Node 9, task C-i: the pointer coupling built from the lattice dynamics (design-stage evidence)

**Pre-freeze design evidence for settling QA′.** This is not the preregistered execution, and it renders no M0–M5
verdict. It establishes only whether the measurement mechanism is available in the specified model. It says nothing
about closure (C-ii). Base: a detached checkout of `6cf71e0e`. Everything is
exact: F₂ bitmask linear algebra, numpy integer bit operations, and Fractions. There is no floating point anywhere.

Read first: `AGENTS.md` (§A.16, §A.21, §A.29, §A.31); `mc-node9/PREREG.md` §1.2, §2.2, §4, §4.1; `mc-node9/NOTES.md`
(QA′); `papers/Main.md` l. 56–62 and l. 288–320. Also read: Main.md l. 74–76 for (C1)/(C2), l. 88 ("By Lemma 2, the
partition is fixed") and l. 109 (§2.2, slow bath).

## 0. Verdict lines (owner's scope update of 2026-10-21 applied)

- **(C-i-a) Pointer coupling realized from lattice dynamics: realized up to stated corrections, for one read
  functional and one update step.** Construction C1 (§3) uses the corpus region partition. It equals the target on
  declared clean visible inputs, with bookkeeping relabelling, and reproduces R_u exactly against every visible record.
  It reads only the toy's current u coordinate. It is not realized at unchanged positions, not for the other two
  reads, and not in the draft's own pointer form (§1, §2).
- **(C-i-b) Recording with back-action: not realized as a consequence of the lattice dynamics; a disturbance-free
  record is available instead.**
  - Storing a reading in visible cells is an observer operation. It is exactly the identity on every hidden
    coordinate, so it has zero back-action (§9.1 (c)). κ4 readout and feedback on all records already give free
    retention.
  - The owner's copy rule X′ = X + Q, P′ = P + Y is realized by short lattice words only as a decoupled product: an
    observer CNOT on visible cells, and an unconditional hidden update between two hidden sites. The kick occurs
    whether or not anything is recorded. In the owner's literal coordinate-level form, nothing record-safe is found
    (§9.2 (i)).
  - In the abstract model the owner's repair checks out: W4 plus recording gives support 2 in all 8 branches. No
    sequence of length ≤ 7 without free readout reaches a point mass. Free readout reaches one at length 5 (§9.2).
  - On the fixed graph, the lattice's own substitute for the refresh, a hidden reservoir behind the bath, only delays
    the W4 collapse: the toy becomes a point mass at step 2(L+1) (§9.1 (d)).
- **(C-i-c) Resources and extra postulates.**
  - For C-i-a: clean visible pointer site (Q and Q̄); a uniform hidden bath; AP-1 (fresh kick source at every read);
    AP-2 (one step of contact); AP-3 (choice of read). See §4 and §5.
  - For C-i-b, beyond the abstract checks: **AP-4**, every retained reading passes through a back-acting record. This
    excludes free retention, which κ4 readout plus feedback on all records grants, and excludes disturbance-free
    visible copies. **AP-5**, memory conjugates are fresh and independent, and are never accessed later. On a finite
    fixed graph the lattice analogue, a hidden reservoir behind the bath, stays fresh for only 2(L+1) − 1 steps.
  - None of these follows from symplecticity. Under the region partition the visible sector is a symplectic subspace,
    so symplecticity never forces a hidden kick on a visible copy.

## 1. Result

**C-i verdict line: realized up to stated corrections, for one read functional and one update step. Not realized as
specified.**

1. **Corpus partition, positions unchanged: not realized.** Under Main.md l. 292, the visible sector is "the sites of
   a region R", so both coordinates of a site share its visibility. No word in the searched space (§2) makes the four
   designated rows equal to the target with the toy bit and pointer at their input positions. This holds even with
   clean visible ancillas, and even if leaking records were allowed (`run_search1_*`). For exact equality there is a
   general reason, independent of graph, size and step count. **No symplectic map** has designated rows equal to the
   target when Q and P lie on different sites (V3, a two-line pairing identity). Under the region partition, a visible
   coordinate's lattice conjugate is visible: "Q visible with hidden conjugate P" cannot be formed from the lattice's
   own canonical pairs.
2. **Corpus partition, with output relabelling (bookkeeping only): realized, construction C1 (§3).** The toy's u and v
   exchange at every step, and P moves from u_c to v_c. With that relabelling, one update step on the path
   *pointer site – toy site – bath site* (R = {pointer site}) gives Q′ = Q + q, q′ = q, p′ = p + P + Q̄, P′ = P. Here
   Q̄ is the pointer site's other visible coordinate. **On the declared clean input Q̄ = 0 this is the target** for the
   read of the toy's u coordinate. It reproduces R_u exactly against **every** visible record. It needs no observer
   operation and no hidden coordinate in a known state.
3. **Only one of the three reads.** The construction reads ω(u, ·) for a single u: the toy's *current u coordinate*.
   This follows from Main.md's Lemma 1 column statement: a step's visible outputs see hidden inputs only through the u
   of hidden sites adjacent to R. In the searched space no record-safe word reads the toy's v coordinate or u + v
   without a hidden coordinate in a known state (§2, table). The observer's free choice of u in model A is not
   supplied.
4. **The draft's own pointer form is outside the corpus and fails anyway.** A pointer with visible Q and hidden
   lattice-conjugate P on one site needs a coordinate-level partition, which Main.md does not define. Under such a
   partition the update exposes the hidden coordinate of a split site after one step. If the site's v is visible, it
   is exposed exactly: v′_x = u_x. If its u is visible, the exposure is masked only by the neighbours' u (V4). The
   searched space has no record-safe AV/E realization there; every hit leaks or needs a known hidden coordinate.
5. **Not on demand.** On a fixed graph the coupling acts at every step, as Main.md l. 109 states: "By (C1), coupling
   is continuously active". Continued waiting re-reads the toy against the same bath site. Each step reveals one more
   hidden bit, and after 4 steps toy and bath are fully determined by the records, with or without feedback resets of
   the pointer (C1.6). With the bath supplied in a known state, C1 *is* K-SYMP2's failure mode (C1.7).

## 2. Search: space, bounds, method, outcome

**Word.** T = G_k M G_{k−1} M ⋯ G_1 M G_0, with 1 ≤ k ≤ 4. M is Main.md l. 290 on the whole graph: u′_x = Σ_{z∼x} u_z +
v_x, v′_x = u_x. Each G_i is an observer operation on the visible coordinates only. There are three operation classes,
nested: **none** (pure waiting), **cell** (all permutations of the visible coordinates), and **GL** (all invertible
linear maps of the visible coordinates). Affine shifts and record feedback only add known constants and are covered by
the AV rule. Nonlinear visible permutations are **not** searched.

**Graphs and assignments.** All simple graphs on n labelled sites. Site 0 is the toy, with both coordinates hidden.
- **strict** (corpus): site 1 is visible and carries Q (u1 or v1); site 2 is hidden and carries P (u2 or v2); other
  sites are V or H.
- **relaxed** (coordinate-level, outside the corpus): site 1 is split, with Q its visible coordinate and P its hidden
  one (both orientations); other sites are V, H or split either way.

Search5 also removes isomorphic duplicates among the non-designated sites.

**Acceptance.** For both toy orientations and all three nonzero u:
- **E**: the designated rows equal the target exactly.
- **AV**: they equal it whenever every visible input is 0, i.e. on declared clean visible inputs.
- **AH**: the realization needs a hidden idle input in a known state, which is the K-CLN failure mode.

**Record-safety** is required throughout. L_k is the span of every visible configuration at times 0..k. Each one is
an accessible record, since readout does not change the ontic state. After eliminating uniform hidden idle inputs and
dropping known visible ones, L_k must give exactly span{ω(u, ·)} on (q, p, P). Because L only grows, classes that
already violate this are pruned. **Relabelled outputs**: the toy may end on any fully hidden site in either order. In
the relaxed mode the pointer may end on any split site; in the strict mode Q may end on any visible coordinate and P on
any coordinate of another hidden site.

**Exactness of the quotient.** X and G·X have identical futures. A class is therefore (hidden rows exactly, visible
rows modulo the class, L), and every level is complete for its class.

| partition | outputs | n | ops (completed coverage) | outcome (record-safe; best category per configuration, by step count and read functional) |
|---|---|---|---|---|
| strict | unchanged | 3 | none, cell, GL | none at any k ≤ 4 |
| strict | unchanged | 4 | none, cell (all 512 configurations); GL (visible dimension 2: 256 configurations) | none at any k ≤ 4 |
| strict | unchanged | 5 | none (16384 configurations) | none at any k ≤ 4 |
| relaxed | unchanged | 2–4 | none, cell (all); GL (visible dimension ≤ 3: 1408 of 2048 configurations at n = 4) | none at any k ≤ 4 |
| strict | relabelled | 3 | none, cell, GL | k = 1: AV read u_toy (2 configurations); k = 2–4: none |
| strict | relabelled | 4 | none, cell | k = 1: AV read u_toy 16, AH read u_toy 4; k = 2, 3: AH read u_toy 2 each; k = 4: none |
| strict | relabelled | 4 | GL (visible dimension 2: 256 configurations) | k = 1: AV read u_toy 4, AH read u_toy 4; k = 2: AH read u_toy 2; k = 3: AH read u_toy 2, AH read v_toy 2; k = 4: AH read u_toy+v_toy 4 |
| strict | relabelled | 5 | none (8704 configurations up to isomorphism) | k = 1: AV read u_toy 168, AH read u_toy 148; k = 2: AH read u_toy 46; k = 3: AH read u_toy 16; k = 4: AH read u_toy 6, AH read u_toy+v_toy 2 |
| strict | relabelled | 5 | GL (visible dimension 2: 2304 configurations) | k = 1: AV read u_toy 12, AH read u_toy 28; k = 2: AH read u_toy 18; k = 3: AH read u_toy 10, AH read v_toy 4; k = 4: AH read u_toy 6, AH read u_toy+v_toy 18 |
| relaxed | relabelled | 2–4 | none, cell | none: n = 4, k = 2, AH read u_toy (1 configuration); cell: n = 4, k = 2, AH read u_toy 2 and AH read v_toy 2; k = 3, AH read v_toy 2 |
| relaxed | relabelled | 2–4 | GL (visible dimension ≤ 3: 752 configurations at n = 4) | n = 4: k = 2, AH read u_toy 2 and AH read v_toy 2; k = 3, AH read v_toy 2 |
| relaxed | relabelled | 5 | none (23936 configurations up to isomorphism) | k = 2: AH read u_toy 29; otherwise none |

**Not completed** (stopped after about 1 h under AGENTS.md §A.40's resource discipline; partial outputs are in
`superseded/`):
- GL at visible dimension 4 (strict n = 4 with two visible sites: 256 configurations; relaxed n = 4 with dimension 4);
- cell at n = 5 (a bounded rerun at visible dimension ≤ 4 also hit its 1700 s cap before the strict block printed);
- GL at n = 5 beyond the strict, visible-dimension-2 block (the relaxed n = 5 GL block hit the cap).

These are the bounds of every negative statement below.

Across the whole completed space, **every AV/E realization reads u_toy at k = 1**, and every read of v_toy or of
u_toy + v_toy is AH. AH hits are of two kinds, separated exactly by `rebase_check.py`:
- **Composite kick.** With several hidden bath neighbours the kick is K = u_c1 + u_c2 + …. This is still uniform. In
  the basis (q, p, K, idle) the learnable space is exactly span{ω(u, ·)}, so it is a re-basing of P and needs no known
  hidden state. Such re-basings occur **only for u_toy reads at k = 1**: 4 configurations at n = 4 (none/cell/GL), 84
  at n = 5 (none) and 28 at n = 5 (GL, visible dimension 2).
- **Genuine.** A hidden idle coordinate kicks the coordinate that was read, or noises the pointer. The read survives
  only if that coordinate is supplied known: the K-CLN failure mode. **Every v_toy and u_toy + v_toy hit, and every
  relaxed-partition hit, is genuine.**

**Closest structure without record-safety** (designated-only search, `search.py`). In the relaxed partition at n = 3,
the GL class at k = 4 has exact (E) designated matches: pointer site isolated, toy adjacent to a fully visible site, u =
(1, 1). Every one routes P through a visible cell. An isolated split site swaps its two coordinates, so P sits exactly
in the visible slot after one step: this is the K-SYMP2 leak, not a mechanism.

## 3. The explicit construction C1

Graph: path 1 – 0 – 2, n = 3. Region R = {1}: site 1 is visible; sites 0 and 2 are hidden. Coordinates are
(u0, u1, u2, v0, v1, v2). **One** update step; no observer operation.

```
M (rows = outputs u0 u1 u2 v0 v1 v2; columns = inputs, same order)
  u0  [0 1 1 1 0 0]      u0' = u1 + u2 + v0
  u1  [1 0 0 0 1 0]      u1' = u0 + v1
  u2  [1 0 0 0 0 1]      u2' = u0 + v2
  v0  [1 0 0 0 0 0]      v0' = u0
  v1  [0 1 0 0 0 0]      v1' = u1
  v2  [0 0 1 0 0 0]      v2' = u2
```

| role | input cell | output cell | |
|---|---|---|---|
| toy q | u0 (hidden) | v0 | q′ = q |
| toy p | v0 (hidden) | u0 | p′ = p + P + Q̄ |
| pointer Q | v1 (visible) | u1 | Q′ = Q + q |
| pointer's lattice conjugate Q̄ | u1 (visible) | v1 | Q̄′ = Q̄ |
| P (kick source) | u2 (hidden, bath site) | v2 | P′ = P |
| P̄ | v2 (hidden, bath site) | u2 | P̄′ = q + P̄ |

In role coordinates, with columns (q, p, Q, Q̄, P, P̄), the step reads:

```
q'  [1 0 0 0 0 0]
p'  [0 1 0 1 1 0]
Q'  [1 0 1 0 0 0]
Q̄'  [0 0 0 1 0 0]
P'  [0 0 0 0 1 0]
P̄'  [1 0 0 0 0 1]
```

The target on (q, p, Q, P) for ω(u, h) = q (u = (0, 1)) is Q′ = Q + q, q′ = q, p′ = p + P, P′ = P. The only extra entry
in the four designated rows is p′ ← Q̄, a visible input declared clean at 0. A nonzero but known Q̄ is a known shift of
p. Idle outputs: Q̄′ = Q̄ is visible and known. P̄′ = q + P̄ is hidden: a masked record of q left on the bath site.

**General form found by the search** (all 16 AV configurations at n = 4, `list_av.out`):
- the toy has at least one visible neighbour; each such neighbour reads u_toy, and its other neighbours are
  visible/known;
- the toy has exactly one hidden neighbour c, the bath, with P = u_c; several hidden neighbours give a composite kick;
- c has no visible neighbour.

## 4. Resource table (C1)

| coordinate | role | required initial state | source in the interface |
|---|---|---|---|
| u0, v0 | the system (toy q, p) | arbitrary | — |
| v1 | pointer Q (visible) | clean, 0, or known | declared clean visible ancilla; can be reset by feedback (g3) with a visible permutation |
| u1 | the pointer's lattice conjugate Q̄ (visible) | **clean, 0, or known** | must be declared as well: the draft declares "Q = 0" only |
| u2 | P, the kick (hidden, bath site) | **uniform, independent of the system and of every accessible record, at the read** | counting measure at the initial time (Main.md l. 56, l. 60; Q3); the independence at the read is postulate AP-1 |
| v2 | P̄ (hidden, bath site) | uniform; not in any designated row | counting measure |
| partition | R = {1} | fixed | Main.md l. 88: "By Lemma 2, the partition is fixed"; no observer control needed |
| timing | exactly one step of contact | — | not available on a fixed graph: AP-2 |

**Known hidden state needed? No.** Every hidden coordinate (u0, v0, u2, v2) is under the counting measure, and the
only clean resources are visible. This is not the K-CLN/K-SYMP2 failure mode. The realizations that would need a known
hidden coordinate are exactly the "genuine AH" hits of §2: every read other than u_toy, and the relaxed-partition hits.
They are not realizations under the clean-ancilla declaration.

## 5. Additional postulates the mechanism needs (each independent; none is a consequence of symplecticity)

- **AP-1, fresh kick source.** At every read, the hidden coordinate(s) that kick the toy are uniform and independent
  of the system and of every accessible record. This is the draft's independence clause, relocated. In C1 the
  disturbance comes from a hidden **bath site**, not from the pointer's conjugate: the pointer's lattice conjugate Q̄ is
  visible and **must be clean**. The postulate as worded in PREREG §4 ("pointer conjugates are never supplied clean")
  therefore does not describe the lattice mechanism. The lattice needs the opposite for the pointer's own conjugate,
  plus a fresh-bath condition.

  The counting measure gives uniformity at the initial time only. On a fixed graph the bath is a permanent neighbour,
  so after the first step it carries P̄′ = q + P̄ and is no longer independent (C1.6). AP-1 is a condition of
  Markovian-bath type. It sits in tension, though it does not contradict, with the corpus's regime conditions: (C2)
  requires "a hidden record of visible history, once written, persists to the readback that uses it" (Main.md l. 76),
  and §2.2 sets τ_S ≪ τ_B (l. 109). Both can hold only if the hidden sector splits into a fresh reservoir that supplies
  kicks and a slow memory part. The corpus supplies no such split.
- **AP-2, contact timing.** The coupling acts for exactly one step. The corpus gives the observer no operation that
  starts or stops a coupling on a fixed graph, and Main.md l. 109 states that coupling is continuously active.
  Without AP-2 the construction is a read at every step, not R_u on demand.
- **AP-3, choice of read.** The lattice reads the toy's current u coordinate; which functional is read is fixed by the
  dynamics and the step parity. Model A's free choice of u among the three nonzero vectors needs a further mechanism
  or postulate. None was found in the searched space without a known hidden coordinate.
- **Declaration extension, not a new postulate:** the clean-ancilla declaration must cover the whole visible pointer
  site (Q and Q̄), not only Q. It is within the interface through condition O and feedback resets.
- **Bookkeeping, no resource:** the observer tracks the output relabelling (toy u↔v, P from u_c to v_c).

## 6. Verification (all exact; all green)

`verify.out`, `verify2.out`, `engine_controls.out`, `brute_none_n4.out`:
- **V1, elementary construction** (abstract (q, p, Q, P)), for each of the three u:
  - bijective and symplectic;
  - with Q = 0, P uniform and discarded, the joint law of (Q′, h′) equals R_u for all four h;
  - countercontrol: with P = 0 known, Q′ = ω(u, h) and h′ = h, a read without disturbance; with P = 1 known, h′ = h + u,
    a known shift.
- **C1.1 to C1.5, lattice construction**:
  - M is bijective and symplectic;
  - the designated-row residual is only p′ ← Q̄ (visible, clean);
  - with Q = Q̄ = 0 and P, P̄ uniform, the joint law of (u1′, v1′, q′, p′), **including every visible record**, equals
    R_u (read q, kick p) for all h;
  - countercontrol: with the bath known (P = 0), the pointer reads q and h′ = h exactly;
  - the records carry u0 = q only.
- **C1.6, continued waiting.** Toy plus bath has 4 hidden bits, and their support given all records is 8, 4, 2, 1, 1, 1
  after steps 1 to 6, with or without feedback reset of the pointer. This describes the construction under further
  steps. It is **not** an M0 computation: there are no generators and no closure, and the proposed restriction's N is
  not modelled.
- **C1.7 and V2, K-SYMP2.** V2 reproduces the two-site example in the f2 conventions: region R = {0}, clean visible
  site, uniform hidden site. After two steps the visible site equals (v1, u1) of the input, and each of the 4 branches
  has probability 1/4 and hidden support 1. C1.7: C1 with the bath supplied known reveals q at step 1 and p at step 2.
  So K-SYMP2 is C1 without a fresh bath.
- **V3, pairing obstruction.**
  - For all 192 placements (n = 3, 4) with Q and P on different sites, the target rows violate a symplectic pairing:
    ω(row_Q′, row_q′) = u_q (J(Q, P) + 1).
  - With Q, P on the same site (the split pointer), the target extended by the identity is symplectic in all 36 cases.
- **V4, split-site exposure.** v′_x = u_x and u′_x = Σ_{z∼x} u_z + v_x for all 284 (graph, site) cases at n ≤ 4.
- **Engine controls (GREEN).**
  - PC-1: target-as-update gives E at k = 1.
  - PC-2: target composed with a visible swap: none fails, cell and GL succeed.
  - PC-3: each of the three read functionals is detected.
  - LC-1: target followed by the pointer exchange: no record-safe class survives.
- **Cross-checks.**
  - search3 (reference, pure Python) against search4 (vectorized): 0 mismatches in class counts and hits on every
    configuration, n ≤ 4, none and cell. At n = 4 that includes cell classes up to 820 per level.
  - `brute_none.py` (independent: explicit Mᵏ, exact record *distributions*, no quotient, no pruning, no subspace
    algebra) reproduces search5's ops = none tallies exactly, both partitions, n ≤ 4.
  - After the memory patch (incremental de-duplication), search5's n ≤ 4 none/cell output is byte-identical to the
    pre-patch output.
  - `rebase_check.py` separates composite-kick re-basings from genuine AH hits by an explicit change of basis
    P → K = P + z and a recomputed learnable space (§2).

## 7. Gem-finding (§A.31): hidden assumptions, stated plainly

**Productivity test.** A result counts as a gem iff it is strictly stronger than "the coupling is symplectic" and it
either constrains or exposes a hidden assumption. The DFS nodes:

1. *Does the corpus partition admit a pointer with a hidden conjugate?* **No** (V3 + Main.md l. 292): the lattice
   conjugate of a visible coordinate is visible. **NEW.** The draft's "pointer's conjugate variable is hidden" has no
   referent under the corpus partition.
2. *Is the disturbance then possible at all?* **Yes**, from a hidden neighbour (C1). The favourable branch was
   pressure-tested (§A.31): every visible record was included and the result was cross-checked by brute force. It
   survives, but only for one step and one functional. **NEW:** the disturbance source is a bath site, not the
   pointer.
3. *Which functional?* Only the toy's current u (Lemma 1's column statement in action). **NEW:** the setting choice
   of u is not supplied.
4. *Does the observer need to control the partition?* **No** for C1, where R is fixed. Yes for the draft's own pointer
   form, which needs a sub-site partition the corpus does not define and which fails anyway (V4, searches).
   **POSITIVE** for C1, **NEW** for the draft form.
5. *Does it need control of step timing?* **Yes**: the mechanism is a single step of contact, while the corpus says
   coupling is continuously active. **NEW:** AP-2.
6. *Is P's independence supplied by the counting measure?* **Only at the initial time.** On a fixed graph the bath
   records the toy at the first step (C1.6), and (C2)/(C4) make persistent hidden records the observer-admitting
   regime. **NEW:** AP-1 is a fresh-bath condition in tension with the slow-bath regime.
7. *Is a known hidden state needed?* **No** for C1. Yes for every other read found. **CONFIRMING** the K-CLN boundary.
8. *Does storing a reading cost back-action?* **No.** A visible copy is exactly the identity on hidden coordinates,
   and κ4 plus feedback give free retention (§9.1). **NEW:** the owner's back-acting record needs AP-4, which
   restricts what the drafted interface grants. The lattice's copy realizations are decoupled products (§9.2).
9. *Is the bath's freshness renewable on a fixed graph?* **Only finitely.** The toy becomes a point mass at step
   2(L+1), the hidden bit count (§9.1 (d)). **NEW**, quantitative: one bit of freshness is consumed per step.

Assumption-watch markers for other claims:
- (a) "visible Q with hidden conjugate" presupposes a sub-site partition;
- (b) "φ = identity" between reads (PREREG §4) is not the lattice's behaviour: on a fixed graph contact is permanent;
- (c) freshness of hidden randomness is a resource that a finite substratum supplies only finitely (Lemma 1 /
  finiteness).

## 8. Scope (what this does not establish)

- **Bounds.** n ≤ 4 for all three operation classes (GL only at visible dimension ≤ 4); n = 5 for none and cell.
  Depth k ≤ 4. Linear observer operations only; no nonlinear visible permutations and no adaptive changes of the
  linear word. A single toy site; the pointer and P on single coordinates (composite kicks noted, not searched as
  designated). The update is Main.md l. 290 over F₂ only.
- **Lifecycle and copy-rule bounds.**
  - Lifecycle: path graphs only, reservoir L ≤ 5.
  - Copy search: n ≤ 3 for all classes; n = 4 for ops = none only (cell/GL killed at the memory limit); GL at visible
    dimension ≤ 3.
  - Owner model: the stated alphabet up to length 7 (length 5 with FREE).
- **Negative results** hold for this construction class and these bounds only. They are not impossibility for every
  observer-level extension.
- **C1 is a mechanism witness, not closure.** C1.6 describes continued waiting and is not an M0 computation. Nothing
  here bears on C-ii, M0 or R-MENU (iii); in particular, whether Π_ω is a principle stays open.
- **Run log.**
  - The first unpruned record-complete run (`search2.py`) was stopped by its 900 s time limit during relaxed n = 3 GL.
    Its none/cell part was rerun to `run_search2_unpruned_n3_none_cell.out`.
  - One n = 5 process was killed by the memory limit (12.8 GB) and rerun after the incremental de-duplication patch.
  - One unrelabelled n = 5 process ended early. Only its strict/none block is reported; relabelled n = 5 covers the
    identity assignment.

## 9. Record lifecycle and the owner's recording mechanism (scope update)

### 9.1 The lifecycle of C1 on the lattice (`lifecycle.py` → `lifecycle.out`; `verify2.py`)

| stage | what the lattice does | resource or postulate |
|---|---|---|
| (a) preparation | pointer site (Q, Q̄) and any memory site clean at 0; toy, bath and reservoir under the counting measure, independent of each other and of every record at t = 0 | clean visible cells are declared (condition O; feedback resets); independence holds only at t = 0 |
| (b) coupling | one update step: Q′ = Q + q, p′ = p + P + Q̄, P′ = P (§3) | AP-2 (one step of contact), AP-3 (fixed read) |
| (c) storing | (c1) **free retention**: the visible configuration is an accessible record (κ4: readout does not change the ontic state), and feedback may use every record so far. (c2) **physical copy** into a visible memory site, X += Q, completed symplectically by Q̄ += X̄: exactly the identity on every hidden coordinate, rows and columns. After the read, it leaves every hidden coordinate unchanged and puts the reading in X | **no back-action**. The interface and the lattice give a disturbance-free, persistent record |
| (d) reuse or discard | the pointer site can be reset by feedback, but the bath and any reservoir stay adjacent forever; every later step is another read with the same hidden neighbours. Support of the toy's current state given every visible record, path pointer–toy–bath–reservoir (L hidden sites behind and including the bath): **2 until step 2(L+1) − 1, then 1 in every branch from step 2(L+1)**, which equals the number of hidden bits including the toy (L = 1..5; with or without pointer reset for L = 1) | a discarded pointer does **not** stay unavailable: AP-1 fails after the reservoir's freshness is consumed, one bit per step |
| (e) later access | later steps re-read the bath's hidden record of the first read (P at v2, q + P̄ at u2), which is the mechanism of (d); with the bath supplied known, C1 becomes K-SYMP2 (C1.7) | single-use condition (owner): Pr(P = r \| h, H) = ½ and no later recovery. On a fixed finite graph this holds only for 2(L+1) − 1 steps |

**Decisive question.** Does OI physically implement persistent records in a way that supplies recording back-action,
or does it in effect provide an external, disturbance-free record? **In this lattice realization it provides a
disturbance-free record.**
- Persistence is free: the readout is passive, accessible records accumulate, and observer operations on visible
  cells never touch hidden cells.
- The only back-action in the lifecycle is the read's own kick from the bath, at (b). Storing, at (c), adds none.
- (C2) persistence of *hidden* records holds here too: the bath keeps q + P̄. But it is exactly what (d)/(e) exploit;
  it does not supply recording back-action.

### 9.2 Owner's copy rule, checks (i)–(iv)

**(i) Lattice realization** (`copy_search.py` → `copy_search_n3.out`, `copy_search_n4.out`; `copy_decoupling*.py/.out`).
The search is record-safe (nothing about P or Y is ever learnable) and relabels outputs. The reading Q must actually
be copied.
- **Strict partition:** E realizations exist.
  - n = 3: GL at k = 1, 2, 4.
  - n = 4: ops = none at k = 1, 2, 4. For example, edges (0,3),(1,2) with sites VHHV: the visible pair 0–3 performs
    X′ = X + Q by the update itself, and the hidden pair 1–2 performs P′ = P + Y.
  - n = 4, cell and GL: **not completed** (killed at the memory limit).
- **They are decoupled products.**
  - Of 60 (configuration, k) realization cases, 54 have the P/Y hidden sites in a connected component with **no
    visible site**. There the kick is unconditional hidden evolution: it happens whether or not anything is recorded.
  - The other 6 (triangle graph, GL, k = 4) connect the two. Even there, the observer can make the same visible copy
    with one visible operation that is the identity on every hidden coordinate (9.1 (c2)).
  - So the lattice never forces the kick on the recording.
- **Owner's literal form** (pointer site = (Q visible, P hidden), memory site = (X visible, Y hidden), a
  coordinate-level partition): no record-safe realization at n ≤ 3 (all classes) or at n = 4, ops = none. n = 4
  cell/GL is not completed. This is consistent with V4: split sites expose their hidden coordinate.

**(ii) What it needs** (abstract model, `owner_model.py` → `owner_model.out`, linear algebra plus brute-force branch
enumeration, all agreeing):
- W4 with free retention: point mass in all 8 branches, readings (p, p + q + P, q). Reproduced.
- W4 + REC after every read, observer sees only the X's: support 2 in all 8 branches. Reproduced.
- Memory conjugate supplied known (Y = 0): support 1, the repair fails.
- Later access to every Y_i: support 1, the repair fails.
- One Y reused for all three records: still 2 for this sequence. Not tested adversarially; independence is therefore
  shown necessary only through the known-Y case.
- Needs:
  - fresh, independent memory conjugates;
  - no later access to Y;
  - **AP-4: no reading is retained except through the back-acting copy.** This rules out free retention and
    back-action-free visible copies, both of which the drafted interface (§1.1: κ4 readout, feedback on records so far,
    permutations of visible cells) and the lattice (9.1 (c)) provide.

**(iii) Exchange followed by unrestricted free readout breaks it.**
- W3′ reproduced: SWP, FREE, read p, read q gives support 1.
- With records only via REC: SWP, FREE, p, REC, q, REC keeps support 2, because REC re-randomizes P before the
  second read.
- With free readout of the readings: SWP, FREE, p, FREE, q, FREE gives support 1.
- The exhaustive search with FREE allowed reaches support 1 at length 5 (e.g. p q FREE p REC).

**(iv) Adversarial sequences with reuse and recording.**
- Exhaustive over all sequences of {read p, read q, read q+p, REC, SWP} up to length 7: 97,655 sequences in total
  (5 + 25 + … + 78,125). Observer sees only the X's.
- **Minimum toy support 2 at every length; no point mass.**
- This is a checked counterexample repair within that alphabet and length bound. It is **not** a closure theorem, and
  it does not cover memory exchanges, reuse of memories as pointers, or composites.


## 10. Files (all in this directory; sha256 at report time)

Scripts: `f2.py` (F₂ engine), `search.py` (designated-only first pass), `search2.py` (unpruned, record-complete), `search3.py` (pruned reference), `search4.py` (vectorized), `search5.py` (relabelled outputs), `brute_none.py` (independent brute force), `engine_controls.py`, `verify.py`, `verify2.py` (C1), `list_av.py`, `analyze_ah.py`, `rebase_check.py`, `lifecycle.py`, `owner_model.py`, `copy_search.py`, `copy_decoupling.py`, `copy_decoupling_detail.py`. Outputs: the matching `*.out` files. `superseded/` holds the stopped runs' partial outputs.

```
0e389a789d971510848c01a3e7b994cee59bca87b49dc97bc6ead50d5bf1b236  analyze_ah.py
6d4a93312f29dfb8a56e5142c03218d545d9aef808c8665ac9362e72bf430c2d  brute_none.py
26fb8162c0397e57c2a9126c7aac04e985578b635e4f90a0fb57fce5b0508d06  copy_decoupling.py
08ff81f2c98322e6a8f61aeba324ff9a16f21bc4d1a259ee697a29dcd7dff235  copy_decoupling_detail.py
ab82d3e000729b24937e954049fcbab80dc91bff2afc117837e4e54fc1f6e1f9  copy_search.py
fa06c5348c18f3af61894040bee40819134208534b677f8812d472dad545f93d  engine_controls.py
855df88d65f9c45b2140438f3d717912b16c41970494652b40e3795b08d43d59  f2.py
af97455f0b9a729702e378120124ce23513ece48b6deb5992778a79c683f7952  lifecycle.py
2560f0ea2350b956f6d05bd001b638c6d4b741898576b6fb9c38e802e18a7192  list_av.py
af2fc5e181916b51fc6e1aab38e7a026aca73f158b31213d274df36a9ec30669  owner_model.py
c8b4ba0545facbc552568edd7eaad8f1b779d5ca7054892405d44d1f06adb84f  rebase_check.py
7a61d68107dddd7675f1dfe26ea14ab9140139ced9ec1d9443c57fe8552a1092  search.py
cd1550d44c8898a5ba0b9609abb651f79b2c1f7911ce20c427623a34c3634119  search2.py
966a39a99817b9a38b994b335f6962395293cfdf65297f02bd6990cde70f0bb6  search3.py
2caa77955b3bec01761ab39426d967b695008a6287d2cf3c4b27d4538a1591f8  search4.py
970b425c09aa493e3441cfd211a3442dd92e20d5d82dad9d29332343afc261b2  search5.py
28918b298ec961864add23fcf197944c8062830e33ba6ef4947b1a8e7158a159  verify.py
5501ab90f33f09dfd664cc732b3ed4def269e09d286275f3abb48ebf63f79032  verify2.py
74909ce324c4bc70ed4c5387a96293e98fba42a9cabaae5a49f512a1b7d82aff  analyze_ah.out
4528547007cb935b93d12c20fa98f6cea9c9286f3fc3b0b2a62df13c5b3c3d7e  brute_none_n4.out
742f2480256eef1db405421635bf08d89534596ac23a7902fe018a13fbf220bf  copy_decoupling.out
1d6de76845150e2289c2f36f3aabd1f1271c250e67766f79b60fead37d7ed4f9  copy_decoupling_detail.out
5440e0306f205e41b725a9d9562dc308c6aa45cf8a612e907f093265207d5428  copy_search_n3.out
10e6dab6df2bf2cf73eda941ff666c7b7b8e769244b1a3823ff66c4addd657e7  copy_search_n4.out
61f6d3a09d727a9838f726db11106eacacbb99a98c9f8c50d63aa5bc5eda33a1  engine_controls.out
797f8985ca009843bc8b96f60fa7ddc1ada7dd7bd8981a2159fb9fdb6fe7a0e3  lifecycle.out
2563bf4210b58e6dde9df0e07f50a656017efad754bb66bc183b4e5fe9c3d772  list_av.out
08c5468ea877b0106fc5956b05e656195a7188e5c349477df97a00d4c3fd5ee2  owner_model.out
febb2897e4cb9fb39a2eac6e80e3ed706aff9c6be5ec6998a656f20a34f269c9  rebase_check.out
48203a7ddda3176963d091dedfcfe3c1ea4c43f726f92752a4cd010c69109cb0  run_n4_GL_dv3.out
ad7132050afe10f0c7b29b5784580ef572f25d5e86b5a1203fd376b5d4cb30cb  run_n4_none_cell.out
2bc72d34be5b59ec25fa7bec3f8879dd152e35afca6fc51a8cb908d40b2dac51  run_n5_none_cell.out
fc0f9755ca8be6edb4cd589ffc8b703e49ed263e672aef40af68cc9f380dacba  run_relabel_n4_GL_dv3.out
647ec50a89f99809ffd48c53de6631809b89d8052a726c7ac3eff65dda51bcad  run_relabel_n4_none_cell.out
79edfa111751b82d8b387bae7def8d8d9b6d16ad059184f3f2ee9fbbfe68379c  run_relabel_n5_GL_dv3.out
46b867048ab4d46e64d5b9a345bbc12d28a23c1d492a4beeb1dbcf60c1a48939  run_relabel_n5_cell_dv4.out
32afbbf5dc5b4c2bf7c9eb4950775b0c72b6604815a1014888101eda83b261d4  run_relabel_n5_none_cell.out
62f7b29b93895b58d68ee18745478dd1a72ccaa79b96e62ee0fc9993f1e491d2  run_relabel_n5_relaxed_none.out
c4fe1a40f90d15d55d49c9e57a7c271a71ae26fdd29fd3b1f9089f045eeaf78c  run_search1_designated_only_n3.out
4ce3da4c5079fbb9688b9c42239c5cc8922c25ba6f5594a262974a4ffbc00598  run_search2_unpruned_n3_none_cell.out
89d5dd22af6bb5f21d68f5985342df4f6eb99bd473dc4cad431d47368d60500b  verify.out
b471ebb69388f66f922ca6d4ee8acd5c896682b289e34518d48d09f68caf6416  verify2.out
14b666fd6274a46f64d5e6ac2632e64caf23bd300696a7293854cf0e2f53a915  superseded/run_n4_GL.out
56f4985ed188aec4f88e4a135ec98aa9587b8eca5e5c18c961de4491450fb70d  superseded/run_relabel_n4_GL.out
47896919d764998f89ef80f07a68cb07ac6fe7ee3d2e85720481134dadbc4cd7  superseded/run_relabel_n5_relaxed_cell.out
14b666fd6274a46f64d5e6ac2632e64caf23bd300696a7293854cf0e2f53a915  superseded/run_relabel_n5_strict_cell.out
```
