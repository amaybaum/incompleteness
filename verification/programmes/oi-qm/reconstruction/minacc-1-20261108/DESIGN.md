# M-INACC-1: protection of `Q* = 1` functionals under a symmetric state-dependent coupling graph at `q = 2` (preregistration)

**Standing.** WIP / UNVERIFIED. Paper-only research unit under #1169.
Writer: Claude Code session, 2026-11-08. Independent review pending.

**Owner authorization** (amaybaum, owner chat decision, 2026-11-08; relayed
to this writer by the coordinating session):

> I approve M-INACC as the next bounded paper-only investigation, with Claude
> Code responsible. The central question is whether a symmetric,
> state-dependent coupling graph can naturally preserve the hidden-information
> protection identified in Q-A, even under nonlinear transport. The
> investigation should: Select one independently motivated symmetric
> construction. Determine whether Lemma Q(iii)'s protection survives under the
> specified P1/P2 preparation and recording assumptions. Test whether an
> allowed protocol can expose the supposedly inaccessible information. Account
> for observer access, complete records, composition and the source of any
> preparation resources. Report either a rigorous conditional result or the
> first missing premise. Crucially, M-INACC is not approved as a new OI
> postulate. We are investigating whether OI produces that property naturally.
> Use one guiding draft PR and an independent reviewer. No scientific
> computation, V3 execution, new physical premise, or theorem promotion is
> authorized.

The [earlier owner addendum](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714136234)
for mechanism units also applies: composition and changed measurement choices
are tested, reproducing an operation only after averaging over hidden states
does not count, and three shortcuts are checked (imported quantum behaviour,
hidden external control, representation versus physical implementation).

**What this file is.** Checkpoint 1: the preregistration only. It fixes the
question, the construction, the operational setting, the decision rule, the
controls and the invariant→checkpoint table. It contains no derivation and no
verdict. The derivation and the verdicts go into `RESULT.md` in this directory
at checkpoint 2. After checkpoint 1 this file is not edited: a change is made
by a separate file under `amendments/` in this directory, which states whether
it was written before or after any result and whether it affects the decision.

M-INACC is a hypothesis under test, not a postulate. Nothing in this unit
adopts a premise, proposes a physical mechanism for adoption, promotes a
theorem, edits a manuscript, builds Lean, runs a V3 round, freezes, dispatches
or merges.

**Source snapshot.** Every repository link is pinned to `main` at
`f88c184220453badfc9279ab9a86b6785e4db5ff` (cited as `main@f88c1842`).
Abbreviations:

- **M2D**: [MECH-2 DESIGN](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md);
- **QA**: [Q-A DESIGN](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md);
- **PR-QA**: [Q-A PROOF-RECOVERY](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/PROOF-RECOVERY.md);
- **FB**: [feedback RESULT](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md);
- **M1D**: [MECH-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md);
- **AP1**: [apparatus-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md).

Labels carried from those records keep their meaning there: N (QA's native
class), P1 (terminal registration), P2 (half-known ready cells), P3 (per-tick,
per-edge arming), E-iso, H-PREP, N2, H-INF-μ, H-FIN, NNB, Lemma Q, Lemma 3
(AP1), Lemma R, Lemma Qσ, Lemma F, H-LIFT, Theorem NC, P★, M-INACC, CC-RECON,
R1, C-LEAK, C-NS.

## 0. What this file fixes

1. **Question (§1).** Whether the conclusion of QA's Lemma Q(iii) — every
   linear functional on active cells that the observer can determine has
   `Q* = 0` — holds when QA's linear symmetric step is replaced by one
   symmetric, center-free, state-dependent coupling rule at `q = 2`, under
   P1 and P2 exactly as QA defines them; and whether any allowed protocol
   determines or biases a `Q* = 1` functional. This is M2D's "first decisive
   check of a symmetrized `G(x)`"
   ([M2D:120](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L120)).
2. **Construction (§2).** `G_σ`: the native second-order update summed over
   the neighbours of SM's explicit ring graph, read as an undirected graph.
3. **Setting (§3).** Two nested protocol classes: `Π_A` (the fixed rule always
   on, with P1 registration and P2 supply only) and `Π_B` (QA's class N with
   its step replaced by `G_σ`: P3 arming, E-iso, vacancies and constant
   translations added).
4. **Decision rule (§4).** Outcomes (A) protection proved, (B) exposing
   protocol exhibited, (C) undecided with the first missing premise named, per
   class.
5. **Controls (§5).** Mechanism off (two linear limits), the classical
   countercontrol of Theorem NC, a target-import check, P1- and P2-removal
   controls that must break, exactness and shortcut checks.

## 1. Question

### 1.1 Owner question and scope

The owner's central question: can a symmetric, state-dependent coupling graph
naturally preserve the hidden-information protection of QA, even under
nonlinear transport?

The protection in question is QA's
[Lemma Q](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L458),
conclusion
[(iii)](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L472):
under P1 and P2, every functional on active cells that the observer can
determine has `Q* = 0`, for every process in N, adaptive or not, and for NNB
couplings. Its hypotheses are a symmetric step with `k_ij = k_ji`, `k_ii = 0`,
and a linear step `u′ = Ku − v`, `v′ = u` over `F_2`.

M2D shows that QA's argument does not apply to SM's directed ring `G_SM`
([Lemma Qσ](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L593)),
that every symmetric, loop-free switched graph conserves `Q` (Lemma Qσ(a)),
and that whether the protection survives nonlinear transport under P1 and P2
is open. It names M-INACC
([M2D:832](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L832))
with three clauses: (a) the fixed rule uses the functional, so later
statistics depend on it; (b) no permitted preparation, read, reuse or
recombination determines it or changes its conditional law; (c) its
inaccessibility follows from a structure stated without reference to the
quantum target. It records what would derive M-INACC (no protocol under P1 and
P2 determines a `Q* = 1` functional) and what would rule it out (such a
protocol, or every functional the dynamics uses becoming determinable through
reuse or recombination)
([M2D:862](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L862)).

Out of scope: an encoded quarter phase, C-CP of encoded operations, FB's
reflections, Bell composites, H-Bell, odd `q`, and any physical source for
P1, P2, P3 or H-PREP. A result bearing on these is reported only if it falls
out of the derivation, and no verdict on them is preregistered.

### 1.2 Definitions

Cells carry `(u_i, v_i) ∈ F_2²`, with `u_i = x_i(t)` and `v_i = x_i(t − 1)`.

- **Linear functional.** `f = Σ_i (a_i u_i + b_i v_i)` on the current slots of
  a finite set of cells, with `a_i, b_i ∈ F_2`.
- **`Q*` and `ω`.** `Q*(f) = Σ_i a_i b_i`, and
  `ω(f, f′) = Σ_i (a_i b′_i + b_i a′_i)`, as in QA. `Q(u, v) = Σ_i u_i v_i`.
- **Active cell.** A cell that is on the ring and not archived (§3.3). Hidden
  cells are active.
- **Knowledge `K`.** Everything the observer holds at a time (§3.6): supplied
  known slot values with their placement, the settings, multipliers,
  translations and schedule executed, and the entire joint record.
- **Determined.** `f` is determined in a record branch of positive
  probability if it is constant on the support of the conditional law of the
  configuration given `K`.
- **Biased.** `f` is biased in such a branch if its conditional law given `K`
  is not uniform on `F_2`.

Determination and bias are judged on the entire joint record of a single
protocol run, branch by branch, before any record is discarded or averaged
(PR-QA §1). A conclusion reached only after averaging over hidden states or
over record branches does not count, in either direction.

### 1.3 Sub-questions

- **Q1 (determination).** Is any `Q* = 1` linear functional on active cells
  determined in some positive-probability branch of some protocol of the class?
- **Q2 (bias).** Is any `Q* = 1` linear functional on active cells biased in
  some such branch? In QA's linear class, non-determination implies
  uniformity, because conditional laws are uniform on affine subspaces. Under
  a nonlinear step that implication is not available, so Q2 is asked
  separately. QA's C-LEAK requires both
  ([QA C-LEAK](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L207)).
- **Q3 (reuse, recombination, composition, changed measurements).** Do
  retained cells, later recoupling, a second system, or a changed choice of
  what to register on the same preparation expose a functional that a single
  read does not?
- **Q4 (the M-INACC clauses).** Asked only if Q1 and Q2 are answered "no" for
  a class: does the protected functional meet clauses (a) and (c) of M-INACC?

## 2. The candidate construction `G_σ`

### 2.1 Definition

Ring `Z_L` with `L ≥ 5`, alphabet `F_2`. At configuration `u = x(t)`, the
coupling graph is the undirected graph

```text
E(u) = { {i, i+1} : i ∈ Z_L }  ∪  { {i, i+2} : u_{i+1} = 0 }.
```

The step sums the current values of all graph neighbours:

```text
f_i(u) = Σ_{j : {i,j} ∈ E(u)} u_j
       = u_{i−1} + u_{i+1} + (1 + u_{i+1}) u_{i+2} + (1 + u_{i−1}) u_{i−2},

F_σ(u, v) = (f(u) + v, u),        F_σ^{−1}(a, b) = (b, a + f(b)).          (1)
```

Site `i + 1` is the **gate** of the edge `{i, i + 2}`. At `q = 2` the memory
terms `+v` and `−v` coincide, so nothing in (1) depends on #1193.

`G_σ` is fixed by this section at checkpoint 1. Its gate position, gate
polarity, range, edge families and coefficients are not changed afterwards.

### 2.2 Properties by inspection

These are properties of the definition. They are re-checked as control C-EX
at checkpoint 2.

| Property | `G_σ` | Reason |
| --- | --- | --- |
| Symmetric adjacency at every `u` | Kept | Membership in `E(u)` is a property of the unordered pair. The gate of `{i, i+2}` is site `i + 1` from both endpoints |
| Center-free (A4, first sense; SM constraint (ii)) | Kept | `f_i` does not read `u_i`, and no edge is gated by one of its own endpoints |
| Translation invariance (A4, second sense) | Kept | Same rule at every site |
| Reflection invariance `i ↦ −i` | Kept | The edge families and the gate position are mirror symmetric. `G_SM` lacks this |
| Bijection (A2) | Kept | Explicit inverse in (1), SM's second-order inverse ([SM:106](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/SM.md#L106)) |
| Bounded degree (A3) | Kept | Undirected degree `2 + [u_{i+1} = 0] + [u_{i−1} = 0] ∈ {2, 3, 4}`; graph dependence of range 1, update reach 2 |
| Linearity (A5) | Broken | Quadratic terms `u_{i+1}u_{i+2}` and `u_{i−1}u_{i−2}`. Each fixed graph is linear; the map is not. `G_SM` breaks A5 in the same way |
| Conservation of `Q` | Expected by M2D Lemma Qσ(a) | `E(u)` is symmetric and loop-free at every `u`. Re-checked in C-EX-Q |

### 2.3 Motivation, stated without reference to the target

- **(m1) SM's graph.** SM's state-dependent-geometry principle
  ([SM:104](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/SM.md#L104))
  has the explicit ring
  ([SM:112](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/SM.md#L112))
  as its example: left neighbour `L(i) = i − 1`, right neighbour
  `R(i, x) = i + 2` if `x_{i+1} = 0` and `i + 1` otherwise. SM states a bound
  on the ring graph's undirected degree. The undirected graph of that ring is
  exactly `E(u)`: the edges `{i, L(i)}` give every `{i, i + 1}`, and the edges
  `{i, R(i, x)}` add `{i, i + 2}` exactly when `x_{i+1} = 0`.
- **(m2) The native form at each step.** The native update sums over graph
  neighbours with one symmetric coefficient: SM's form lemma
  `x_i(t+1) = α Σ_{j∼i} x_j(t) − x_i(t−1)`
  ([SM:224](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/SM.md#L224)),
  with A4 and A5
  ([Substratum A4](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/Substratum.md#L98),
  [A5](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/Substratum.md#L100)).
  SM states that under constraints (i)–(iii) "the form lemma of §4.1 applies
  at each step"
  ([SM:110](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/SM.md#L110)).
  Applying that form on `E(x(t))`, with `α = 1` (the only nonzero coefficient
  at `q = 2`), gives (1). SM's explicit dynamics sums over the two
  out-neighbours `L(i)` and `R(i, x)` of a directed graph instead; M2D
  assesses that directed rule as `G_SM`.
- **(m3) Reciprocity is native.** For a fixed graph, the second-order step is
  symplectic iff the adjacency is symmetric
  ([AP1 §4.1](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L464)),
  and AP1 derives backaction from that reciprocity. Symmetric adjacency is a
  property of the native linear rule, independent of any comparator.
- **(m4) SM's constraints.** (i) graph dependence of range 1; (ii) center-free;
  (iii) statistical isotropy, here met by exact translation and reflection
  invariance ([SM:108](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/SM.md#L108)).

**Status.** An independently motivated proposal, of the same standing as
`G_SM` in M2D: SM's principle is a stated hypothesis, the ring is SM's
example of it, and neither is physically sourced. `G_σ` is not adopted and is
not selected by OI.

### 2.4 What would make the choice ad hoc; alternatives set aside before any derivation

The choice is ad hoc if any of the following holds:

- (a1) it was selected among variants by its verdict on Q1–Q4 or on any
  quantum target;
- (a2) its gate position, polarity, range, edge families or coefficients are
  changed after checkpoint 1;
- (a3) the protocol classes of §3 are narrowed after checkpoint 1 to remove an
  exposing protocol;
- (a4) its only motivation is programme-internal: conservation of `Q`, or the
  wish to keep Lemma Q.

**Disclosure on (a4).** The requirement "symmetric" enters through the owner's
question, which follows M2D's observation that symmetric switched graphs
conserve `Q`. Reciprocity is therefore in part selected for the property under
test. Its independent support is (m2) and (m3). Conservation of `Q` does not
select `G_σ` among symmetric graphs: by M2D Lemma Qσ(a) every symmetric
loop-free switched graph conserves it.

**Alternatives set aside, with reasons fixed before any derivation.**

| Alternative | Reason it is not the candidate |
| --- | --- |
| `G_SM` (directed) | Not symmetric for `L ≥ 5`; assessed in M2D |
| Intersection reading: keep an edge only if both directed edges of SM's ring exist | `{i, i+1}` is then present iff `x_{i+1} ≠ 0`, gated by its own endpoint, so `f_{i+1}` reads `u_{i+1}`: violates SM constraint (ii). No `{i, i+2}` edge survives for `L ≥ 5` |
| Opposite polarity (`{i, i+2}` present iff `u_{i+1} = 1`) | Not the graph of SM's ring |
| Gated edges without the nearest-neighbour family | Not the graph of SM's ring. M2D's self-check c6 checked `Q` for "a symmetric switched graph (edge `{i, i+2}` present iff `u_{i+1} = 0`, read by both ends)" as a control variant; its record does not state whether nearest-neighbour edges were included. Only Lemma Qσ(a) is used from M2D, and it covers `G_σ` |
| Ungated next-nearest edges (linear) | QA's NNB-type linear class; it is the mechanism-off limit `N_0` below |

**Observation on the source text (no manuscript change by this unit).** SM:112
gives the ring graph's undirected degree as "bounded in [3, 2]", which is not
an interval in increasing order. For the undirected graph `E(u)` the degree
takes the values 2, 3 and 4 (table in §2.2). This is recorded for propagation
review by the coordinator.

### 2.5 Mechanism off

| Limit | Rule | Class | Lemma Q(iii) |
| --- | --- | --- | --- |
| `N_1`: every gate held at 1 (no `{i, i+2}` edges) | `f_i = u_{i−1} + u_{i+1}` | QA's class N on a ring; bipartite iff `L` is even | Holds (QA) |
| `N_0`: every gate held at 0 (all `{i, i+2}` edges) | `f_i = u_{i−1} + u_{i+1} + u_{i−2} + u_{i+2}` | Linear, symmetric, center-free, with same-sublattice (NNB-type) edges | Holds (QA states Lemma Q on any graph, NNB included) |

Both are linear and conserve `Q`. They are the mechanism-off controls of §5.

## 3. Operational setting

### 3.1 Cells, sources and supplies

At `t = 0` every ring site holds one cell, except sites that start vacant
(`Π_B` only). The observer chooses a finite region `R`. Each site of `R` holds
one of:

- **a ready cell (P2).** Exactly one slot, `u` or `v`, is known. Its value is
  0, or 1 through H-PREP. The other slot is unknown, uniform and independent of
  everything else
  ([AP1 SA-1(c)](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L297);
  [QA ledger P2](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L780));
- **a source cell.** Both slots unknown, uniform and independent (N2 through
  H-PREP). Carrier inputs are source cells or ready cells; any other carrier
  law arises only through a protocol and its records.

Every site outside `R` holds a source cell (the hidden sector). For an
infinite ring, the finite dependency cone of a protocol carries the normalized
product law H-INF-μ. No cell with both slots known is supplied. No correlated
background is supplied (**H-PS**, product sources): correlations arise only
through the dynamics and the records. Correlated or preparation-dependent
background sources are outside both classes, as in PR-QA §1.

### 3.2 The step and the two protocol classes

`Π_A ⊂ Π_B`. Both are closed under sequential composition: the outgoing
configuration and the retained records of one protocol are the input of the
next.

**`Π_A`, the fixed rule always on.**

- At every tick `F_σ` acts on all active cells of the ring.
- Supplies: the choice of `R` and of the cells in it at `t = 0`, and the refill
  of each archived site (§3.3).
- Registration under P1 with refill (§3.3).
- Record feedback (§3.4) into the choice of what to register and when, and of
  the known slot and value of each refill.
- No arming, no isolation, no vacancies, no translations.

**`Π_B`, QA's class N with its step replaced by `G_σ`** (QA
[§1.2](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L124)).
Everything in `Π_A`, and:

- **P3 multipliers.** Per tick and per edge, a multiplier `c_e(t) ∈ F_2` for
  every nearest-neighbour edge and every gated edge `{i, i+2}`. The effective
  coefficient is `c_e` for a nearest-neighbour edge and `c_e (1 + u_{i+1})` for
  a gated edge. A multiplier cannot remove the gate factor, and no edge outside
  the two families can be armed.
- **E-iso.** Multipliers may be set to 0 on every edge joining `R` to its
  complement. A cell whose effective edges are all 0 takes the free tick
  `(u, v) ↦ (v, u)`.
- **Vacancies.** A site may start vacant, and an archived site may be left
  vacant. A vacant site has no slots and no edges. As a gate it acts as the
  value 0, the reading of SM's ring in which the coupling skips a zero site.
  This convention is input-independent and carries no information. A vacant
  site may be refilled with a fresh P2 ready cell at any time.
- **Constant translations.** Any slot may be translated by a supplied constant,
  including a record-conditioned one (QA §1.2, "Corrections").
- **Discarding.** Marginalizing cells. On the ring a discarded cell keeps
  evolving and coupling; discarding changes only what the observer tracks.

### 3.3 Registration and the archive (P1)

As in [AP1 SA-1(b)](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L292):

- Between ticks the observer may register one slot of any active cell. That
  slot's value enters the record.
- The registered cell is then **archived**: it leaves the ring, takes free
  ticks thereafter, couples to no cell and gates no edge. It may be registered
  again only on the same transported functional. One functional is registered
  per cell.
- In `Π_A` the archived site is refilled at the same moment by a fresh P2
  ready cell. In `Π_B` it is refilled or left vacant.
- The observer acquires record values only by registration. Reading a cell
  without archiving it is not available (P1); the P1-removed case is control
  C-P1.

### 3.4 Records, feedback, settings and changed measurements

- **Complete records.** The joint record of every registration is kept. Every
  verdict on Q1 and Q2 is conditional on the entire joint record, branch by
  branch (§1.2).
- **Feedback.** Any later choice the class allows may depend on earlier
  records. The agent that executes feedback is supplied (as in M1D's SC-2
  finding).
- **Changed measurements.** The setting choices (which cell, which slot, at
  which tick; and in `Π_B` which multipliers and translations) may differ on
  the same preparation. Q1 and Q2 quantify over every setting choice.
- **No heralds** are used. Branch probabilities are counts of uniform bits in
  a finite cone, so they are dyadic.

### 3.5 Reuse, recombination and composition

- **Reuse and recombination.** Retained cells (unregistered meters, carriers,
  cells holding kick variables) may couple again at later ticks. In `Π_A` they
  do so whenever they remain within range; in `Π_B` the observer arms such
  couplings. AP1's eraser-type recombination
  ([AP1 §4.5](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L628))
  and its gated analogues are in the class.
- **Composition.** A system is a set of sites with its own supplies and
  records. Two systems `W_1`, `W_2` are **separated** if, over the protocol's
  duration, no cell of one system's dependency cone is within range 2 of the
  other's; otherwise they are **adjacent**, and cross-system coupling and
  cross-system gating are in the class. Q1 and Q2 quantify over all active
  functionals, so composition is included in them. Route R-C (§4.3) examines
  it explicitly. A determined relative functional with `Q* = 0` (such as the
  sum of two commuting `Q* = 1` functionals, QA node 7) is not an exposure.

### 3.6 Observer access

The observer holds exactly `K` (§1.2). It has no access to source cells, to
unknown slots of ready cells, to the hidden sector, or to unregistered slots
of archived cells. Settings, multipliers, translations and refills are
executed by supplied means (§3.7). No reading of a cell other than by P1
registration exists in either class.

### 3.7 Resource ledger

| Resource | Class | Native or supplied | Status |
| --- | --- | --- | --- |
| The step `F_σ` | Both | Proposal (§2) | Independently motivated proposal; not adopted |
| Ready cells, known value 0 | Both | Supplied (P2) | AP1 posit; resource accounted under #1147 |
| Ready cells, known value 1 | Both | Supplied (P2 through H-PREP) | Open hypothesis H-PREP |
| Uniform unknown slots and source cells | Both | Native measure N2, applied through H-PREP | H-INF-μ for an infinite hidden sector |
| Region choice and placement at `t = 0` | Both | Supplied | Laboratory design |
| Registration and archive | Both | Supplied (P1) | AP1 posit |
| Refill of archived sites | Both | Supplied (P2) | As ready cells |
| Feedback executor | Both | Supplied | As in M1D SC-2 |
| P3 multipliers | `Π_B` | Supplied (P3) | AP1 posit |
| Isolation | `Π_B` | Supplied (E-iso) | AP1 idealization |
| Vacancies (gate value 0) | `Π_B` | Supplied | Convention fixed in §3.2 |
| Constant translations | `Π_B` | Supplied (P2 through H-PREP, as in QA) | As in QA N |

## 4. Decision rule

### 4.1 Properties decided

For a protocol class `Π`:

- **PROT-D(Π).** For every protocol of `Π`, every tick and every record branch
  of positive probability, no linear functional on active cells with
  `Q* = 1` is determined. This is Lemma Q(iii)'s conclusion with N replaced by
  `Π`.
- **PROT-B(Π).** For the same quantifiers, no such functional is biased.

For the mechanism-off classes (`G_σ` replaced by `N_1` or `N_0`), QA's Lemma
Q(iii) gives PROT-D, and uniformity on affine subspaces gives PROT-B.

### 4.2 Outcomes

Each class is decided separately.

- **(A) Protection proved.** PROT-D(Π) and PROT-B(Π) are proved by a paper
  argument covering adaptive protocols, reuse, recombination, composition and
  changed measurements. The record lists every hypothesis used and carries it
  into the conclusion. It then evaluates M-INACC's clauses:
  - **(a) use.** USE-dyn: at the tick where `f` is evaluated, there is a
    configuration `λ`, a shift `w` with `f(w) = 1`, and a continuation protocol
    of `Π` whose record, as a function of the configuration, differs at `λ` and
    `λ + w`. USE-dyn excludes only a dynamically inert `f`; it is weak and is
    reported with that qualification.
    USE-ctx is also reported: whether two available operations that no
    protocol of `Π` distinguishes (on the full accessible theory, not an
    encoded subtheory) have realizations that differ in their action on `f`.
    By Bayes, a record that depends on `f` given `K` biases `f`, so under
    PROT-B "use" cannot mean statistical dependence of a record on `f` given
    `K`; this is why USE-ctx is the informative form.
  - **(b) inaccessibility.** PROT-D(Π) and PROT-B(Π) over every preparation
    reachable in `Π`.
  - **(c) reason.** The load-bearing structure of the proof is named, and
    C-IMPORT checks that it is stated without the comparator.

  If (a), (b) and (c) all hold, the result is reported as a conditional result
  under the listed hypotheses. If (a) or (c) fails, the outcome is **(A′)**:
  protection holds and M-INACC is not met, with the failing clause named.
- **(B) Exposure.** A protocol of `Π` is exhibited that determines (**B-D**) or
  biases (**B-B**) a `Q* = 1` linear functional `f` on active cells in a
  positive-probability branch. The record states:
  - the protocol: sites, initial cells, ticks, multipliers and translations if
    any, registrations, the record branch and its probability, and `f`;
  - every resource used, with its §3.7 status, and whether the protocol lies
    in `Π_A`;
  - CC-OFF on the same protocol (§5);
  - whether AP1 Lemma 3's isotropy also fails;
  - the first premise whose addition would block this protocol, with CC-RECON
    applied when its only motivation is the protection or the target. It is
    named, not adopted.

  A (B) verdict is a negative result for `G_σ` and the stated class only. It
  says nothing about other symmetric graphs or other access posits.
- **(C) Undecided within paper scope.** Neither a proof nor an exposure is
  obtained. The record names the first step of Lemma Q(iii)'s proof (node 1,
  §4.3) that does not transfer, the precise statement that would close it, and
  whether a bounded finite check would decide it for a stated protocol bound.
  No such check is run, and no V3 round is proposed.

**Combinations.** `Π_A ⊂ Π_B`, so (B) for `Π_A` implies (B) for `Π_B`, and
(A) for `Π_B` implies (A) for `Π_A`. The admissible pairs `(Π_B, Π_A)` are
(A, A), (B, A), (B, B), (B, C), (C, A) and (C, C). The answer to the owner's
question is stated for both classes. An exposure found in `Π_B` and not in
`Π_A` is attributed to the resources `Π_B` adds (P3, E-iso, vacancies,
translations), not to `G_σ` alone.

**D0.** A failed or vacuous control voids the verdict of the branch it
controls (§5).

**D-ATTR.** Every (B) verdict states which element is load-bearing: the gate
of `G_σ` (shown by CC-OFF), P3, E-iso, vacancies, translations, known-1 cells
(H-PREP) or feedback.

**D-Q.** No quantum quantity enters the decision of PROT-D or PROT-B. R1 and
the comparator enter only CC-NC and USE-ctx.

### 4.3 Order of the walk and preregistered routes

Depth-first (§A.12, §A.31), each node closed by a written check.

1. **Node 1, transfer audit.** QA's proof of Lemma Q(iii) has four steps:
   - (s1) conditioned on all records, each branch is a fixed sequence of
     symplectic center-free steps and constant translations;
   - (s2) by AP1 Lemma 3, the determined functionals on active cells form the
     isotropic span of transported known slots and registered records;
   - (s3) `Q*` is preserved under transport through a step (Lemma Q(ii));
   - (s4) `Q*` is additive on an isotropic subspace.

   For `G_σ` each step is classified as transfers, fails, or transfers under a
   named added condition. The first failing step is the candidate first
   missing premise for outcome (C). The audit applied to `N_1` and `N_0` must
   reproduce QA's proof (C-LIN).
2. **Node 2, exposure routes in `Π_B`,** in this order:
   - **R-G (gate read).** A cell's slot serves as the gate of an edge between
     two other cells. The gate is not an endpoint of the edge it gates, so the
     gated edge enters no term of the gate cell's own update;
   - **R-N (nonlinear record).** Records that are nonlinear functions of the
     configuration, whose conditioning gives non-affine supports (the
     mechanism of M2D's P★), under P1 terminality;
   - **R-R (reuse and recombination).** Recoupling of retained kick variables
     through gated edges (AP1 §4.5 analogues);
   - **R-T (translated gates).** Constant and record-conditioned translations
     of gate slots that change later edge sets;
   - **R-C (composition).** Cross-system coupling and gating between adjacent
     systems; relative functionals; C-NS for separated systems.

   **Disclosure.** Before writing this file, the writer's informal scoping
   identified R-G as the route to examine first. No derivation of it is
   recorded here, and its verdict is not anticipated by this file.
3. **Node 3.** If node 2 exhibits an exposure in `Π_B`: whether that protocol,
   or a modification of it, lies in `Π_A`; then the routes of node 2 in `Π_A`.
4. **Node 4.** A protection proof for each class without an exposure.
5. **Node 5.** Composition and C-NS, if not closed in node 2.
6. **Node 6.** Controls, the countercontrol and the shortcut checks.

The walk stops when each class has an outcome. Findings are classified as in
§A.31 (NEW, POSITIVE, ELABORATING, CONFIRMING, BORDERLINE), with
assumption-watch markers. When a branch favours the framework (an (A)
verdict), that branch is pressure-tested first.

### 4.4 Standards of proof

- **Exposure (B).** An explicit protocol with its record branch and the
  conditional support written out over `F_2` in the record, small enough to
  check by hand.
- **Protection (A).** A complete paper proof, covering adaptive protocols.
- **Exactness.** Every verdict is exact over `F_2`. Floating-point results are
  not accepted for any identity, determination or bias.
- **Self-checks.** Small exact checks of the record's own algebra (integer or
  `Fraction` arithmetic over explicitly stated finite instances) are allowed
  as controls. They are listed in the result, are not committed, are not
  evidence, and no verdict rests on them. No simulation, search or enumeration
  campaign is run.

## 5. Controls and countercontrols

| ID | Requirement | Required outcome | Voids if failed |
| --- | --- | --- | --- |
| CC-OFF-1 | Mechanism off, `N_1` (class N) | Any exposing protocol of (B), run with every gate held at 1, determines and biases no `Q* = 1` functional. Any proof of (A) specializes to Lemma Q(iii) for `N_1` | The (B) or (A) verdict it controls |
| CC-OFF-0 | Mechanism off, `N_0` (linear NNB-type ring) | The same, with every gate held at 0 | As CC-OFF-1 |
| C-EX-Q | §A.21 exactness: `G_σ` conserves `Q` (Lemma Qσ(a)), and the §2.2 properties hold | Holds for `G_σ`. Two breaking controls must break: `G_SM` (Lemma Qσ(b)) and `G_σ` with a center term `u_i` added to `f_i` | Every verdict |
| C-LIN | Node 1 audit applied to `N_1` and `N_0` | Reproduces QA's proof of Lemma Q(iii) step by step | Node 1 and outcome (C) |
| C-P1 | P1 removed: a registered cell stays on the ring, or both slots of a cell are registered | Must expose a `Q* = 1` functional (QA's two-slice receiver, [QA:512](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L512); AP1 [C9](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L682)). If the analysis does not register this, it is insensitive | An (A) verdict |
| C-P2 | P2 removed: a supplied cell with `u + v` known | Must expose (QA ledger P2) | An (A) verdict |
| C-L3 | AP1 [Lemma 3](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L533) isotropy under `G_σ` | Reported. A sharp active cell determines that cell's `u + v` (`Q* = 1`); the converse does not hold | — (diagnostic) |
| CC-NC | Classical / noncontextual countercontrol: does M2D's [Theorem NC](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L483) already give a classical imitation? | Under (A): check Theorem NC's premises for an encoded system carrying the protected functional (injective identification, H-LIFT, spanning-read certification). If the available laws cannot change the protected functional's conditional law, spanning certification fails and Theorem NC does not decide; the result is then stated as "not decided by Theorem NC". If an exact noncontextual model of the observer-level statistics is found anyway, protection is reported as not separated from classical behaviour (M2D D2). No contextuality claim is made without a witness certified over tomographically complete equivalences. Under (B): the exposure is a configuration-level fact and Theorem NC is unaffected; the record states this | An (A) verdict stated as a nonclassicality resource |
| C-IMPORT | Target-import check | (i) §2's definition contains no quantum quantity (unitary, CP map, Pauli, Clifford, encoding); (ii) PROT-D and PROT-B are decided at configuration level (D-Q); (iii) no restriction on `Π_A` or `Π_B` is added after checkpoint 1; (iv) any premise named under (B) as blocking an exposure is reported, not adopted, with CC-RECON applied when its only motivation is the protection or the target; (v) the protected class is QA's `Q* = 1` class, fixed in §1 | Every verdict |
| C-AVG | Owner guidance: no conclusion only after averaging | Every Q1–Q2 verdict is per record branch, on the entire joint record | The verdict concerned |
| C-MEAS | Changed measurement choices on one preparation | Q1–Q2 quantify over every setting choice; an (A) proof says where it uses this | An (A) verdict |
| C-NS | No-signalling of complete local histories for separated systems | Reported, under Main's cone theorem ([Main:366](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/Main.md#L366)) with range 2 | — (reported) |
| SC-1 | Imported quantum behaviour | Reported: no unitary, interference, CP restriction or comparator enters as a premise | — (reported) |
| SC-2 | Hidden external control | Reported with D-ATTR: which supplied element (§3.7) each verdict uses | — (reported) |
| SC-3 | Representation versus physical implementation | Reported: whether the protected or exposed functional is a configuration-level object or exists only in an encoded representation | — (reported) |

**Physical-carrier ceiling (context, not a control of this unit).** `G_σ` is a
configuration bijection, so its operations on the physical carrier are
monomial. For condition (iv) of #1169's conditions profile the kernel statement
is [`substratumGen_not_control`](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/lean-mathlib/OIBridge/StructuralClosure.lean#L348).
This unit does not revisit it. The vacuous `ReadWriteSourced` family (#1188) is
not cited.

## 6. Hypothesis ledger

Every conclusion carries the hypotheses it uses from this list.

| Item | Content | Native or supplied | Status |
| --- | --- | --- | --- |
| G-σ | The step (1) | Proposal (§2) | Independently motivated; A5 broken; not adopted |
| Nq | `q = 2` | Native parameter value, chosen per the owner's instruction | Odd `q` is out of scope; any odd-`q` remark is conditional on #1193 |
| P1 | Terminal registration with archive (§3.3) | Supplied (AP1) | Posit |
| P2 | Half-known ready cells (§3.1) | Supplied (AP1) | Posit |
| P3 | Per-tick, per-edge multipliers (§3.2) | Supplied (AP1) | `Π_B` only |
| E-iso | Isolation of the region | Supplied (AP1) | `Π_B` only |
| V-0 | Vacant sites gate as 0 | Supplied convention | `Π_B` only |
| T-C | Constant translations | Supplied (QA N) | `Π_B` only |
| H-PREP | Record-conditioned classes read as preparations; known-1 cells | Supplied | Open hypothesis |
| N2 | Uniform law on unknown slots | Native measure through H-PREP | As in QA |
| H-INF-μ | Normalized product law on a cone of an infinite hidden sector | Hypothesis | As in QA |
| H-PS | Product sources; no supplied correlated background | Hypothesis | Correlated backgrounds are outside both classes |
| H-NW | Protocol cones do not wind the ring | Hypothesis | Winding needs the whole ring (H-FIN), not used |
| FB-EX | Feedback executed by a supplied agent | Supplied | As in M1D SC-2 |
| I1 | Qubit stabilizer comparator, R1 | Imported | CC-NC and USE-ctx only |

## 7. Invariant → checkpoint table (§A.41)

| Invariant asserted of this unit's execution | Checkpoint that measures it |
| --- | --- |
| The preregistration precedes the derivation | Checkpoint 1's commit changes exactly this file: `git show --stat` on it lists `minacc-1-20261108/DESIGN.md` only. Checkpoint 2 is a descendant of checkpoint 1 |
| The construction, setting, decision rule and controls are unchanged after checkpoint 1 | At checkpoint 2, `git diff <checkpoint 1> <checkpoint 2> -- …/minacc-1-20261108/DESIGN.md` is empty. Any change is a file under `amendments/`, which states whether it precedes any result and whether it affects the decision |
| Paper only; no computation committed | At checkpoint 2, the unit's diff from `main@f88c1842` touches only `minacc-1-20261108/` (`DESIGN.md`, `RESULT.md`, `amendments/`). `RESULT.md` lists every self-check with what it controls |
| Every verdict is over green controls | `RESULT.md`'s control table gives each §5 control an outcome. A red or vacuous control is applied by D0 to the verdict it controls, and the verdict text states this |
| Exactness | `RESULT.md` states the arithmetic of every self-check. No floating-point result supports a verdict |
| No vacuous Lean citation | At each checkpoint, a search of the unit's directory for the `ReadWriteSourced` lemma family (identifiers beginning with `readWriteSourced` and an underscore) returns no match |
| Links pinned | At each checkpoint, every blob link to this repository in the unit's files names commit `f88c184220453badfc9279ab9a86b6785e4db5ff` |
| Odd-`q` statements are conditional | At checkpoint 2, every odd-`q` sentence in `RESULT.md` names #1193; checked by the reviewer |
| No adoption or promotion | At checkpoint 2, `RESULT.md`'s ledger marks M-INACC and every named premise "not adopted"; checked by the reviewer |
| Register | At each checkpoint, the added lines are scanned for the revision-history phrase family of §A.33, for mid-sentence capitals of four or more letters outside acronyms and named labels, and for the reader-instruction family of §A.32; hits are removed before the checkpoint is reported |
| Independent review | The reviewer's verdict on the exact pushed SHA of each checkpoint is recorded on the guiding draft PR by the coordinator |

## 8. Checkpoint plan; what is not authorized

- **Checkpoint 1 (this file).** Committed alone, not pushed by the writer. The
  coordinator pushes it, opens the guiding draft PR and obtains an independent
  review of the preregistration before checkpoint 2 starts.
- **Checkpoint 2.** `RESULT.md`: nodes 1–6 of §4.3, the outcome per class,
  the control table, the ledger with the hypotheses carried, sources, and the
  self-check list. Amendments, if any, under `amendments/`.
- **Not authorized.** Scientific computation (simulation, search, enumeration
  campaign), Lean builds, V3 execution, new physical premises, theorem
  promotion, manuscript edits, freezes, dispatches, merges.

## 9. Sources

All repository sources are on `main@f88c1842` and are cited at their stated
scope. Issue and chat items are provenance.

| Source | Use | Classification (§A.42 item 8) |
| --- | --- | --- |
| SM:104, :106, :108, :110, :112, :224, :226 | Principle; bijectivity; constraints (i)–(iii); form lemma at each step; ring graph; form lemma; nearest-neighbour scope | Manuscript text (support on `main`) |
| Substratum A4 (L98), A5 (L100) | Center independence; linearity | Manuscript text |
| Main:366 | Cone theorem for C-NS | Manuscript text |
| QA §1.2 (L124), C-LEAK (L207), Lemma Q (L458, L472), P1-removed case (L512), ledger P1/P2 (L779–L780) | Class N; Lemma Q(iii); controls | Support on `main` (#1184, #1189), at its stated scope |
| PR-QA §1 (L10) | Entire-joint-record discipline; product sources | Support on `main`; its header records independent review pending |
| FB | Context for out-of-scope items | Support on `main`; its header records independent review pending |
| M2D first decisive check (L120), Lemma F (L307), H-LIFT (L319), Theorem NC (L483), Lemma Qσ (L593), P★ (L630), M-INACC (L832, L862) | Question; Lemma Qσ(a); countercontrol; M-INACC clauses | Support on `main`, at its stated scope |
| M1D SC-2 finding; M1 and CTRL-MON (L940, L964) | Supplied feedback executor; controller context | Support on `main` (#1191), at its reviewed scope |
| AP1 SA-1(b) (L292), SA-1(c) (L297), §4.1 (L464), Lemma 3 (L533), §4.5 (L628), C9 (L682) | P1, P2; reciprocity and symplecticity; isotropy; recombination; P1-removed control | Support on `main` (#1183) |
| Kernel `substratumGen_not_control` (StructuralClosure:348) | Context for condition (iv) | Kernel statement on `main`, read and not rebuilt |
| Owner chat decision 2026-11-08 (quoted above); #1169 comment 6714136234 (addendum); #1188; #1193 | Authorization and scope; excluded citation; odd-`q` condition | Provenance |
