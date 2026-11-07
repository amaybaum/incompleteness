# Q-A: a native source for the 8-point quarter-phase mechanism

**Standing.** Paper-only research unit for step 3 of #1169, question Q-A. Author:
Claude Code session, 2026-11-07. Scope: [owner approval and Q-A scope](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6712359044),
[owner direction on the three levels and the native/supplied distinction](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6711920779),
and the [Q-B target decision](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6712409082),
whose finiteness remark binds this unit: no step assumes that a traced-out or
inaccessible sector is finite unless the ledger names that as a hypothesis.
Q-B is out of scope.

This file proposes no premise for adoption. No simulation, enumeration campaign,
Lean build, manuscript change, freeze, dispatch or merge is part of it. Small exact
checks of this file's own algebra were run as author self-checks (§8). They are
not evidence and are not cited as support.

**Source snapshot.** All repository links are pinned to `main` at
`b1d782f954f02cec578a10e071b73e48f86eb3dd` (cited as `main@b1d782f9`), which
contains the #1173 papers and the apparatus-1 record of #1183.

## 0. Result

1. **Native class: the quarter phase is excluded (§2, nodes 1–4).** Center
   independence (A4) makes every native and P3-armed coupling free of
   self-terms. On a bipartite coupling graph such as the nearest-neighbour cubic
   lattice, the slot variables then split into two sublattice-time sectors that
   no armed protocol mixes (Lemma G1). Each sector is Lagrangian. Two
   consequences are proved:
   - at most two of the observer's native reads can disturb each other through
     reciprocal backaction;
   - no encoding of a qubit, on any number of cells and with any hidden sector,
     finite or not, admits an encoded quarter phase `S` together with native X
     reads and the comparator's statistics (Lemma G2).

   The traced-out sector runs the same rule, so it cannot supply `S` either.
2. **A native protection of a parity (§2, node 6).** At `q = 2` the native step
   conserves `Q = Σ_i x_i(t) x_i(t−1) mod 2` on any coupling graph with
   symmetric couplings and no self-terms. Under apparatus-1's supplied access posits P1 (terminal
   registration) and P2 (half-known ready cells), every functional the observer
   can determine has `Q* = 0` (Lemma Q). A functional with `Q* = 1` is
   therefore never determined, whatever the reuse, recombination, ancillas or
   records. The selection rule is derived from A4, P1 and P2; nothing is
   stipulated beyond those.
3. **Minimal departure (§2, nodes 5–8).** One change suffices for a
   quarter-phase mechanism: premise NNB, an armable symmetric coupling between
   two cells of the same sublattice (non-bipartite, still center-free and
   linear). It is used together with R-ONE, a supplied ready cell whose known
   slot has value 1. Under NNB and R-ONE, a two-cell carrier gives the following:
   - **(A1) pass.** It carries `z`, `x` and `y = z + x + p`. The three are
     pairwise disturbing by native reciprocal backaction, and the parity
     `p = z_2 + x_2` is never determined (Lemma Q). This survives reuse and
     recombination by any center-free protocol. A parity shared between wings
     signals.
   - **(A2) pass.** The encoded `S` is an affine bijection: a center-free linear
     map followed by an R-ONE translation. On the single-qubit stabilizer domain
     its read and continuation laws equal the comparator.
   - **(A3) pass, in a qualified sense.** LWE's operationally equivalent `T_1`
     and `T_2` are realized by ontic maps that respectively preserve and flip the
     inaccessible `p`. The inaccessibility comes from the conserved form, not
     from tracing out a hidden sector.
4. **Cost, found by pressure-testing the favourable branch (§2, node 9).** In
   every linear encoding, the linear part of `S` acts on the encoded qubit as a
   reflection (determinant −1), and so does the translation that `S` needs
   (Lemma R). Both factors are separately available under NNB, R-ONE and P3. The
   encoded operation set then contains a map that is not completely positive
   (control C-CP fails). An exhaustive check found that a fixed affine offset on
   the same-sublattice coupling does not remove this. The construction also does
   not compose (node 10, outside Q-A's scope):
   - with wing-local parities, encoded two-qubit correlations miss the comparator;
   - a shared parity signals;
   - no fixed parity correlation satisfies both the row and the column constraint
     of the Mermin–Peres square.
5. **Outcome type (ii): stop (§4).**
   - Minimal additional physical structure for an encoded quarter phase at
     single-qubit stabilizer scope: NNB plus R-ONE, beyond apparatus-1's
     supplied P1, P2, P3, E-iso and H-PREP.
   - For a quantum operation set (C-CP), a further posit I is needed: the linear
     part of an odd Clifford, and any translation that flips `p`, are available
     only together. I is defined by the target and is easy to vary, so it is
     not adoptable under §A.29.

   No V3 round is proposed: the native class is settled by proof, and the open
   item, I, is an operation-set posit, not a rule-search question (§4.3).

## 1. Question and decision rule

The question, sub-questions, controls and decision rule below are stated in the
same commit as the derivation of §2. Their priority over the result is not
separately recorded.

### 1.1 Target and comparator

The comparator is imported (I1): the single-qubit stabilizer subtheory as
defined in Lillystone–Wallman–Emerson (LWE), arXiv:1802.06121v2:

- Pauli eigenstates and their convex mixtures;
- Pauli reads with Lüders continuation;
- the Clifford group.

The encoded quarter phase is `S = diag(1, i)`, with Bloch action
`(r_x, r_y, r_z) ↦ (−r_y, r_x, r_z)`. A read along axis `a` gives outcome bit `b`
with probability `(1 + (−1)^b r_a)/2` and leaves the eigenstate. The comparator is
a definition, not a native postulate
([endpoints L45](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md#L45)).
The C-PH test of apparatus-1 §1.3 is transported unchanged: an available process
induces `S` on the encoded carrier under one identification, fixed for all
settings.

### 1.2 The native class and the carried-over posits

The class **N** of native processes consists of the following steps.

- **Update.** Second-order, linear, center-free updates
  `u_i' = Σ_j k_ij u_j − v_i`, `v_i' = u_i` over `Z_q`, with symmetric coefficients
  `k_ij = k_ji` and `k_ii = 0`, on the nearest-neighbour cubic graph. The
  coefficients are either the native fixed ones or loaded per tick and per edge
  under P3, and E-iso may be applied.
  - Sources: Substratum A4 and A5
    ([L98](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Substratum.md#L98),
    [L100](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Substratum.md#L100));
    the SM form lemma and its nearest-neighbour scope remark
    ([L224](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L224),
    [L226](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L226)).
  - The same holds for `K`-component site fields with matrix-valued link
    coefficients (A6,
    [L102](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Substratum.md#L102)).
- **Supply.** Attaching ready cells with one known slot (P2).
- **Registration.** Registering a meter cell's record slot (P1, terminal).
- **Discarding.** Marginalizing cells.

The hidden sector runs the same update
([Substratum L48](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Substratum.md#L48)).
Its size is not restricted.

A **native minimal read** is one armed coupling to one ready meter whose record
slot is then registered. Its only effects are the record and the reciprocal kick
into the conjugate slot
([apparatus-1 §4.1](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L464)).

A process is **non-adaptive** when its armings depend only on settings and
heralds, never on records. That is SA-1's P3 as stated.

P1, P2, P3, E-iso and H-PREP keep apparatus-1's classification as supplied
([ledger](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L411)).
A verdict "native" below means: within N, using no posit beyond these.

### 1.3 Sub-questions and their pass conditions

- **(A1) Carrier.** Pass iff both of the following hold.
  - (a) A subsystem built from cells carries three binary linear functionals
    `f_z`, `f_x`, `f_y`. Each is registrable by a native minimal read, and each
    read randomizes the other two by its reciprocal kick (native complementarity
    for all three pairs).
  - (b) The parity `p := f_x + f_y + f_z` is not determined in any knowledge
    state reachable by any protocol of the stated class, including reuse of
    retained cells and native recombination.

  Clause (b) must be derived. A protocol of the class that determines `p` fails
  (A1), whether it does so directly, through two commuting records, through
  recombination into one slot, or through reuse.
- **(A2) Operation.** Pass iff a bijective process of the stated class induces
  `S` on the encoded statistics under the same identification. On the
  single-qubit stabilizer domain the read and continuation laws must equal the
  comparator.
- **(A3) Cost.** Pass iff LWE's operationally equivalent `T_1` and `T_2` are
  realized by ontic maps that differ exactly on the sector that (A1)(b) makes
  inaccessible.

### 1.4 Controls

| ID | Preserved result or requirement | Required outcome |
| --- | --- | --- |
| C-ROT | `rot` unreachable (apparatus-1 §5.3) | The encoded `rot` is unavailable. The finite-carrier argument is used only with its finiteness hypothesis stated |
| C-NS | No-signalling of complete local histories | For a two-wing arrangement, each wing's complete local history law is independent of the remote settings |
| C-LEAK | The two-system hidden-parity leak ([two-system §4](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241)) and native recombination ([recombination §3](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L116)) | `p` is never determined, nor biased given the records, under reuse or recombination. A construction in which some permitted protocol exposes `p` fails (A1) |
| C-B2 | B2 fixed-instrument failure | Copy-only reads (reciprocal kick removed) must fail the comparator |
| C-EAR | E-AR obstruction scope | At most 2 pairwise perfectly distinguishable encoded preparations |
| C-L5 | Lemma 5 of apparatus-1 as countercontrol | Removing the extra cell must return to "no `S`" |
| C-CP | Introduced here: every available process induces a completely positive map on the encoded carrier | No available encoded map has an orientation-reversing (determinant −1) action on the Bloch octahedron |
| C-EX | §A.21 exactness | The structural invariants (grading, `Q`) are checked together with controls that must break them |

C-CP is added because escaping C-PH while adding a non-quantum encoded operation
is not progress toward the comparator. A failure of C-CP does not void the
computation; it is reported as a cost of the premise that causes it.

### 1.5 Decision rule

- **D0.** A failed C-EX, C-B2 or C-L5 voids the verdict of the branch it controls.
- **D1.** Each of (A1)–(A3) is decided within N first. Any sub-question that
  passes in N gets the verdict "native".
- **D2.** If one fails in N, the smallest single departure from N that makes
  it pass is identified. Each departure is stated as a conditional premise,
  together with what it preserves (controls), what it buys and its independent
  consequences (§A.29).
- **D3.** Outcome types:
  - (i) if (A1)–(A3), C-ROT, C-NS, C-LEAK and C-CP all pass in N, or under
    posits already supplied in apparatus-1;
  - (ii) if passing needs a new premise, or C-CP fails;
  - (iii) if the decisive remaining question is a finite search over native
    update rules.

## 2. Depth-first walk

Each node is closed by an exact paper argument. Self-checks are listed in §8.

### Node 1. Where can a third complementary functional come from in N? Lemma G1

**Lemma G1 (sublattice grading).** Let the armed coupling graph at every tick be a
subgraph of a bipartite graph with colouring `χ`. Let every coupling be
center-free (`k_ii = 0`), with arbitrary per-tick, per-edge coefficients over
`Z_q`. Give each initial variable a type:
- type `χ_i` for `u_i(0)`;
- type `χ_i + 1` for `v_i(0)`;
- the type of the slot it enters, for a fresh ready-cell variable.

Then at tick `t`:
- the slot `u_i(t)` is a linear combination of variables of type `t + χ_i` only;
- `v_i(t)` is a linear combination of variables of type `t + χ_i + 1` only.

*Proof.* By induction. The update `u_i(t+1) = Σ_j k_ij u_j(t) − v_i(t)` adds
neighbours `j` with `χ_j = χ_i + 1`, of type `t + χ_i + 1`, and `v_i(t)`, of type
`t + χ_i + 1`. That is the required type `(t + 1) + χ_i`. Also `v_i(t+1) = u_i(t)`.
A self-term would add `u_i(t)`, of type `t + χ_i`; that is the only place the
induction uses `k_ii = 0`. ∎

**Consequences.**

- **Every record is single-sector.** A record is a slot value, so it is a
  linear functional of the variables of one type (one sector).
- **Each sector is Lagrangian.** The cell form `ω = Σ_i u_i ∧ v_i` pairs a type-`τ`
  variable with a type-`τ+1` variable. Each sector is therefore isotropic, of
  half dimension. Two single-sector functionals of the same sector commute.
- **The generated maps are the graded subgroup.** In the per-cell encoded frames
  `J^{−t}` of apparatus-1, every native process acts by `A ⊕ A^{−T}` on (sector
  E, sector O), plus translations. On a connected bipartite graph, edge
  transvections generate the elementary subgroup of `GL(n, Z_q)`, which is all of
  `GL(n, F_2)` at `q = 2`. A graded transvection between two
  same-colour cells `c_1, c_2` is obtained through an opposite-colour mediator
  `m` from the commutator `[E_{c_2 m}, E_{m c_1}] = E_{c_2 c_1}`, with `m`
  returned.
- **Phase shears and Fourier maps are never generated.** No same-cell phase
  shear (`x ↦ x + a z`) and no Fourier map (`z ↔ x`) is generated, at any `q`. For
  odd `q` this bears on apparatus-1's open expectation that SA-1 gives the qudit
  stabilizer theory
  ([§5.6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L1065)):
  on a bipartite graph the per-edge couplings do not generate the full
  symplectic group, and the qudit phase and Fourier gates lie outside the
  generated group.
- **Relation to apparatus-1.** Apparatus-1's type invariant for its §3.3 class
  ([L521](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L521))
  is the special case of a carrier with its meters. On the cubic lattice, two
  meters adjacent to the same carrier have the same colour and are never
  adjacent to each other. So the lattice geometry itself excludes the
  meter–meter edges that would break the grading.
- **Relation to SM.** SM's exact chiral (sublattice) symmetry of the
  observer-level staggered operator (Theorem 3,
  [L302](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L302);
  §4.8,
  [L541](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L541))
  is the same bipartite structure at another level. That correspondence is an
  analogy across levels, which SM itself says needs a bridge. Lemma G1 uses
  only the finite update.

**Scope of "bipartite".** The infinite cubic lattice and every periodic cubic
lattice of even side are bipartite. A finite periodic lattice of odd side `L` is
not; its shortest odd cycles wind the torus and have length `L`. The grading
then holds for every protocol whose dependency cone, of radius equal to its
duration, contains no odd cycle. Mixing through winding needs a finite carrier
(Substratum A1,
[L92](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Substratum.md#L92)),
and it needs coherent use of the whole torus over at least `L` ticks. It is
recorded as a hypothesis-dependent exception (ledger H-FIN) and is not used.

**Check.** Self-check c1:
- 0 violations over bipartite paths, even cycles, a 3×3 grid and a star, at
  `q = 2, 3, 5` with random coefficients;
- the three controls break the grading as they must: a self-term, an odd cycle,
  and a meter–meter edge.

**Verdict.** The native couplings preserve a two-sector Lagrangian grading.

### Node 2. Native complementarity: at most two mutually disturbing reads

A native minimal read of a single-sector functional `f` kicks only the conjugate
slot. That slot lies in the other sector, so the read changes the value of no
same-sector functional. Three reads that pairwise disturb by backaction would
need three functionals pairwise in different sectors. There are two sectors.

**Verdict.** Within N, (A1)(a) fails for every encoding: at most two of the
three encoded reads can be native minimal reads that disturb each other. A third
mutual disturbance needs an operation besides the read. That operation can be
omitted, and omitting it lets the observer know two complementary encoded
values at once. That is the sharpening behind C-EAR.

### Node 3. Can N induce `S` at all? Lemma G2

**Lemma G2 (graded quarter-phase obstruction).** Within N, fix any encoding of a
qubit. The hypotheses are:

- any number of cells and ancillas, and a hidden sector of any size, with or
  without E-iso;
- the encoded X read is a native minimal read of an O-sector functional `f_X`,
  with heralded failure acting as the encoded identity (as in SA-1);
- free evolution acts as the encoded identity in the fixed frame (C8);
- `S` is any non-adaptive process of N (fresh ancillas, internal registrations
  without feedback, supplied constant translations allowed).

Then the comparator is not reproduced on the protocol
`X_+ → S³ → X → S → X`.

*Proof.* Let R1 be this protocol and R0 the same protocol on the herald-failure
branch of the middle read.

1. **The comparator's demands.** It gives the final X outcome in R0 as
   deterministic (`S⁴ = I`). In R1 it gives the final outcome as uniform and
   independent of the middle record `c`.
2. **What separates the two runs.** By Lemma G1, the O sector evolves under a
   linear map that never takes input from the E sector. The two runs differ only
   by the armed meter edge. In O, that edge copies the carrier's O-value `c` into
   the meter's record slot. In E, it adds the meter's unknown to the carrier.
3. **The final outcome.** Since the subsequent armings are the same in both runs,
   linearity gives, pointwise in every initial configuration,
   `f_X^{final}(R1) = f_X^{final}(R0) + λ c` with a fixed `λ ∈ Z_q`.
4. **Conclusion.** The final outcome is therefore a deterministic function of
   `c`, which contradicts step 1. If `S` mixes several fixed graded maps, each
   branch gives `0 + λ_b c`, and `P(final = f_X^{R0} | c = 0) = 1` still
   contradicts the comparator. ∎

**Scope.** The argument uses no measure, so it holds for any hidden prior and
any hidden-sector size. It needs the non-adaptive hypothesis. Record-controlled
armings or record-controlled translations across sectors make the joint map
nonlinear or ungraded, and they are outside the lemma. They are a further
supplied capability (classical feedback from records into slot values), not
part of SA-1's P3.

**Check.** Self-check c2 examined `n ≤ 3` cells: every graded affine `S`, every
O-functional encoding, 75,556 cases in all. In none of them do R1 and R0 both
match the comparator. Wherever R0 is deterministic, the final outcome in R1 is
determined by `c`.

**Verdict.** Within N, (A2) fails for every encoding. This includes encodings
that place any cell in the traced-out sector.

### Node 4. The traced-out sector as the home of the parity (tested hardest)

The owner's suggestion was to put the parity bit in the traced-out sector. Three
independent closures apply.

1. **Same rule.** Hidden cells run the native rule (Substratum L48), so Lemma G2
   covers every process that involves them, always-on hidden coupling included.
2. **Reciprocal access.** Suppose the observer can arm an edge `c–h` and supply
   `c` ready as `(w, 0)`. The coupled tick gives `u_c' = k u_h` (apparatus-1
   §4.1), so every slot of `h` is registrable at the matching parity. A cell that
   an available `S` must couple to therefore has no inaccessible slot.

   If the observer cannot arm any edge into `h`, then `S` can only be native free
   evolution. A fixed free evolution is absorbed into the fixed frame
   (PC-F1), so it is not a selectable operation.

   If `h` is instead coupled to a maximal-entropy hidden background, a read of
   `h` through `c` is masked
   ([receiver assessment, eq. (3) and §6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L144)).
   But the same coupling feeds background unknowns into the carrier while it is
   coupled. This file does not establish a general masking-without-randomization
   statement and claims none.
3. **Shared sector.** A parity cell shared by two wings signals. Self-check c4
   used Route U, node 5, with the parity cell shared. Bob prepares `Y_+`. If
   Alice applies her `S`, Bob's `Y` read changes from 0 to 1 with certainty. This
   is the two-system leak of
   [two-system §4](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241)
   in the present setting. A common traced-out sector cannot host `p`.

**Verdict.** The traced-out sector does not supply the parity natively. The
decisive branch is the structure of the native step (nodes 1–3), not the
location of the parity.

### Node 5. The smallest departures, compared

Two single changes reintroduce a third complementary read. The cubic lattice is
kept in both.

**Route U: a controlled center term (violates A4).** Encoding:
- carrier cell `(z_1, x_1)` and parity cell `(z_2, x_2)`;
- `f_z = z_1`, `f_x = x_1`, `f_y = z_1 + x_1 + z_2`, so `p = z_2`.

Results:
- **`S` exists.** Self-check c3 found four symplectic affine maps with the
  encoded action of `S`. The read and continuation laws equal the comparator on
  all 2,380 cases (sequences up to length 4 over `{S, X, Y, Z}`, from seven
  preparations).
- **The parity is accessible.** `p = z_2` is a single slot, registrable by
  reciprocal access (node 4.2). (A1)(b) fails.

The center term also breaks the conserved form of node 6.

**Route NNB: a same-sublattice coupling (keeps A4 and A5).** P3 may arm a
symmetric, center-free coupling between two cells of the same colour, for
example next-nearest neighbours. In the encoded frames this coupled tick acts
CZ-like: `x_1 += z_2, x_2 += z_1` at one tick parity, and `z_1 += x_2, z_2 += x_1`
at the other. It breaks bipartiteness, so Lemma G1 does not apply. Encoding U′:
- the same two cells;
- `f_z = z_1`, `f_x = x_1`, `f_y = z_1 + x_1 + z_2 + x_2`, so `p = z_2 + x_2`.

Bounded coupling degree (A3) admits such couplings. SM adopts the
nearest-neighbour branch as a premise beyond A3 (L226), so NNB is a departure
from that branch, not from A1–A6.

**Selection.** Route U fails (A1)(b) outright. NNB is the decisive branch. Nodes
6–8 test it.

### Node 6. Lemma Q: a conserved form that protects the parity

**Lemma Q (quadratic selection rule, `q = 2`).** Hypotheses:

- every coupling is symmetric (`k_ij = k_ji`) with `k_ii = 0`, on any graph,
  bipartite or not;
- the step is `u' = K u − v`, `v' = u` over `F_2`.

Conclusions:

- (i) The step conserves `Q(u, v) = Σ_i u_i v_i mod 2`.
- (ii) Write `Q*(f) = Σ_i f_{u_i} f_{v_i}` for a linear functional `f`. The value
  of `Q*` is preserved when a functional is transported through the step. Its
  polar form is `ω`.
- (iii) Under P1 and P2, every functional on active cells that the observer can
  determine has `Q* = 0`.

*Proof.*

- (i) `Q(u', v') = Σ_i (Σ_j k_ij u_j − v_i) u_i = Σ_{i,j} k_ij u_i u_j − Q(u, v)`.
  The double sum is `2 Σ_{i<j} k_ij u_i u_j ≡ 0`, and `−1 = 1`. A center term
  would add `Σ_i k_ii u_i`.
- (ii) The step `M` is symplectic and preserves `Q`. Transporting functionals
  acts by `M^{−T} = J M J^{−1}`, and `Q` is invariant under the coordinate swap
  `J`.
- (iii) By apparatus-1's Lemma 3
  ([L533](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L533)),
  the determined functionals on active cells form an isotropic subspace `D`
  spanned by two kinds of functional:
  - transported known slots of ready cells (P2);
  - registered record slots on terminal cells (P1).

  A slot has `Q* = 0`, and (ii) preserves this. On an isotropic subspace the
  polar term `ω` vanishes, so `Q*` is additive there. Hence `Q* ≡ 0` on `D`. ∎

**Properties.**

- **Measure, size and translations.** Statement (iii) concerns support, not
  measure: any full-support prior on the unknown slots will do. It places no
  condition on the size of the hidden sector, and translations by known
  constants do not change `D`.
- **A conserved quantity at `q = 2` only.** SM records conserved quadratic forms
  of the exact rule for general `q`
  ([L296](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L296)).
  The form `u·v` is a `q = 2` invariant not listed there. Modulo 2 its energy
  `E` reduces to `Σu + Σv + u·Av`, a different quantity.
- **Role of A4.** Lemma Q is where center independence does work at `q = 2`.
  NNB keeps it.

**Check.** Self-check c5 ran 4,000 random center-free protocols on four cells,
with ready cells and minimal reads. The functional `z_2 + x_2` was determined in
0 of them. Two controls must break the protection, and do:

- with center terms allowed, it was determined in 175 of 4,000;
- with P1 removed (the kick variable also registered, apparatus-1's C9
  mechanism), it was determined in 222 of 4,000.

**Verdict.** Natively (A4, at `q = 2`), and given the supplied P1 and P2, a
functional with `Q* = 1` is permanently undetermined for the observer, whatever
the protocol.

### Node 7. (A1) under NNB

The three encoded functionals are:

- `f_z = z_1`, `f_x = x_1` and `f_y = z_1 + x_1 + z_2 + x_2`. Each has `Q* = 0`, so
  Lemma Q allows each to be a record.
- `ω(f_z, f_x) = ω(f_z, f_y) = ω(f_x, f_y) = 1`. Each native minimal read therefore
  kicks the other two: native complementarity holds for all three pairs.
- The parity `p = f_x + f_y + f_z = z_2 + x_2` has `Q* = 1`.

A single-cell `Y` functional `z_1 + x_1` has `Q* = 1`, so it is never a record.
This matches node 2 and Lemma 5. A Y read always involves a second cell.

The `Y` read is realized as `S†`, then an X read, then `S`. Symplectic
covariance makes its kick the transported kick of the X read, so it is the
native minimal read of `f_y`.

| Check | Result |
| --- | --- |
| (A1)(a) | Pass under NNB (and R-ONE for `S`, node 8) |
| (A1)(b) | Pass, by Lemma Q. Given the records, `p` is uniform under N2 and never determined. This covers reuse of the parity cell and native recombination, since both are center-free couplings |
| C-LEAK within one wing | Green. Reciprocal access reads `z_2` or `x_2`. They do not commute, so either read kicks the other and `p` stays undetermined |
| C-LEAK across wings | Requires wing-local parity cells (WL). A shared parity cell signals (self-check c5: Bob's `Y` outcome moves from 0 to 1 with Alice's `S`) |
| C-EAR | Green. At most one of `f_x, f_y, f_z` is determined in any isotropic knowledge state, so encoded laws lie in the octahedron and at most two encoded preparations are perfectly distinguishable |

Self-check c3 found the parity unbiased given the records on every encoded
sequence of length at most 4 for Routes U and B. For U′ the same follows from
Lemma Q under N2, and c5 checked its non-determination directly.

### Node 8. (A2) and (A3) under NNB

- **(A2).** Self-check c5 found four symplectic affine `S` with the encoded
  action of `S`.
  - All four linear parts preserve `Q`.
  - Two lie in the group generated by graded couplings and the NNB coupling. That
    group has 36 elements on two cells; the graded couplings alone generate 6,
    and adding center terms gives all 720 elements of `Sp(4, F_2)`.
  - The translation flips `p`. It needs a known value 1 from R-ONE.
  - With native minimal reads of `f_z, f_x, f_y`, the law equals the comparator
    on all 2,380 cases.

  **Pass** under NNB, R-ONE and P3.
- **(A3).** Take `T_1` as the uniform mixture of the encoded Paulis (cell-1
  translations) and `T_2` as `T_1` followed by the encoded `H`.
  - Self-check c6 found encoded `H` solutions with center-free linear part.
  - Both maps send every encoded state to the maximally mixed state, so they are
    operationally equivalent.
  - On the ontic level, `T_1` preserves `p` and `T_2` flips it. This is LWE's
    eqs. (6) and (7) with `xyz ↔ p`.

  **Pass**, with a qualification. The two realizations differ on a sector that
  Lemma Q makes inaccessible. The source is a conserved quadratic form together
  with isotropy, not a traced-out hidden sector. By LWE Theorem 1, any
  preparation-noncontextual model of the full subtheory has this feature, so
  (A3) restates a forced property of every model that passes (A1) and (A2). The
  derived content here is that the inaccessible sector is fixed by A4 together
  with P1 and P2.
- **C-ROT.** Green without a finiteness hypothesis. Under N2 every record
  probability is a count of uniform bits within a finite cone, so it is dyadic,
  conditional on herald success. The `rot` Z-read probability `9/25` is not
  dyadic. With non-uniform hidden priors the dyadic argument is unavailable, and
  apparatus-1 §5.3 then applies only under H-FIN, with Markovian reuse of a
  finite carrier.
- **C-NS.** Green with wing-local parity cells, under the hypotheses (i)–(iv) of
  Main's
  [cone and screening theorem](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L366).
  Each wing's maps and kicks act only on its own cells. Red with a shared
  parity cell (node 7).
- **C-B2.** Green. Copy-only reads fail the comparator (self-check c9: 138
  failing cases of 588).
- **C-L5.** Green. With the parity cell removed, no bijection of `F_2²` realizes
  `S` under either `Y` convention (self-check c9: 0 found, Lemma 5).

### Node 9. Maximum skepticism on the favourable branch: Lemma R and C-CP

**Lemma R (two reflections in every linear encoding).** Take an encoding in which
each encoded Pauli eigenstate is a level set `{f_a = b}` of a linear functional,
and let the encoded `S` be an affine bijection with linear part `L` and
translation `τ`. Then:

- `L` maps the encoded state family to itself, and its encoded action is a
  signed permutation of determinant −1;
- the translation `τ` also acts as determinant −1;
- `τ` flips `p`, that is, `p(τ) = 1`.

*Proof.*

1. **`L` has determinant −1.** A homogeneous map sends the zero level set
   `{f = 0}` to a zero level set, so `L` permutes the three states
   `{f_a = 0}`. Its encoded action is `D P D` with `D` diagonal of signs and
   `P` the axis permutation. The determinant of this action is the sign of
   that permutation. For `S` the axis permutation is the transposition
   `(x y)`, so the sign is −1.
2. **`τ` has determinant −1.** A translation flips the sign of each axis `a`
   with `f_a(τ) = 1`. Since `S = τ ∘ L` has determinant +1, `τ` flips an odd
   number of axes.
3. **`τ` flips `p`.** Because `p = f_x + f_y + f_z`, an odd number of flips
   means `p(τ) = 1`. ∎

The same holds for `H`, and for every Clifford whose axis permutation is odd.
These are exactly the parity-flipping elements in LWE's remark that "the
Hadamard swaps it (as does the phase gate P)".

**Consequence.**

- **The linear part.** Under NNB and P3, the linear part `L` is a composition of
  separately armable couplings. It is available on its own and acts as
  `X ↔ Y` with `Z` fixed (self-check c5).
- **The translation.** Under R-ONE, the translation `z_2 += 1` is available on
  its own. It flips `f_y` and `p` only, so it acts as `Y ↦ −Y` (self-check c6).
- **C-CP fails.** Both encoded maps are orientation-reversing, so neither is
  completely positive.

**Can an offset weld the factors?** Self-check c8 tested whether a fixed affine
offset on each same-sublattice coupling could make `L` and `τ` unavailable
separately. It went through all 256 pairs of offsets on the two coupling
parities, together with the graded couplings and the encoded Pauli
translations. Every generated group contains `S` and an encoded reflection.

**Verdict.** NNB together with R-ONE buys the quarter phase only together with
the encoded reflections. Removing them needs a posit I, which restricts the
operation set to the rotation subgroup. I is defined by the target and is not a
native mechanism.

### Node 10. Composites (outside Q-A's scope; recorded for #868)

- **Wing-local parities.** Self-check c7 started from encoded `Z_+ Z_+`, then
  applied encoded `H` on wing A and an encoded CNOT. The CNOT is a graded
  coupling between the carrier cells, and on the encoded functionals it acts as
  CNOT. The result has `⟨XX⟩ = ⟨ZZ⟩ = 1` and `⟨YY⟩ = 0`; the comparator's `Φ⁺`
  has `⟨YY⟩ = −1`. The determined functional is `f_y^A + f_y^B + p_A + p_B`, not
  `f_y^A + f_y^B`.
- **Shared parity.** It signals (node 4.3).
- **Correlated but local parities.** Here `p_A + p_B` is determined, which
  Lemma Q permits, since it has `Q* = 0`. The values of the joint reads are sums
  of local functionals. Two constraints then apply:
  - Mermin–Peres row: `(X⊗Z)(Z⊗X)(Y⊗Y) = +I` requires `p_A + p_B = 0`;
  - Mermin–Peres column: `(X⊗X)(Z⊗Z)(Y⊗Y) = −I` requires `p_A + p_B = 1`.

  The operator identities were verified directly. No fixed value satisfies both.

So the mechanism is a single-system mechanism. This agrees with LWE's Discussion,
read first-hand, on the impossibility of a preparation-noncontextual model of
the two-qubit stabilizer subtheory.

## 3. Ledger

| Item | Content | Native or supplied | Status |
| --- | --- | --- | --- |
| N1 | Second-order linear symmetric update; symplecticity | Native | Substratum A4, A5; apparatus-1 N1 |
| N1-CI | Center independence, `k_ii = 0` (A4) | Native | Used in Lemma G1 and Lemma Q |
| N1-BIP | Nearest-neighbour cubic, hence bipartite, coupling graph | Native, selected branch | SM L224–L226 adopts it as a premise beyond A3. On odd periodic sides the graph is bipartite only within cones without winding (H-FIN) |
| N2 | Uniform law on unknown slots | Native measure, applied through H-PREP | Used only for read statistics and dyadicity. Lemmas G1, G2 and Q do not use it. On an infinite hidden sector counting is not normalized ([interface source L266](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L266)), so a product law on the finitely many variables in a cone is a hypothesis (H-INF-μ) |
| N3 | Bijective steps | Native | — |
| P1 | Terminal registration | Supplied (apparatus-1) | Load-bearing for Lemma Q (self-check c5, P1 removed: 222 of 4,000) |
| P2 | Half-known ready cells whose known functional is a slot | Supplied (apparatus-1) | Load-bearing for Lemma Q. A supplied cell with known `u + v` would carry `Q* = 1` |
| P3, E-iso | Per-tick, per-edge armed couplings; isolation | Supplied (apparatus-1) | Non-adaptive in G2 |
| H-PREP | Record-conditioned classes read as laboratory preparations | Supplied (open hypothesis) | As in apparatus-1 |
| NNB | Armable symmetric center-free coupling between same-sublattice cells | Supplied (new conditional premise) | Not adopted (§4) |
| R-ONE | Ready cell whose known slot has value 1, or an equivalent H-PREP-selected preparation | Supplied resource | Needed for every translation, including encoded Paulis |
| WL | Parity cell local to its wing | Design condition | Derived necessity: shared parity signals |
| I | Linear parts of odd Cliffords and `p`-flipping translations available only together | Supplied posit (target-defined) | Not adoptable (§4) |
| E-U′ | Encoded identification of §2 node 5, fixed for all settings | Mathematical representation | — |
| H-FIN | Finiteness of the total carrier | Hypothesis, used only where named | Odd-torus winding (node 1); the finite-carrier form of C-ROT |
| H-INF-μ | Normalized product law on the hidden variables in a protocol's cone | Hypothesis | N2 statistics with an infinite hidden sector |
| I1 | Single-qubit stabilizer comparator, Lüders reads, CPTP | Imported (comparator only) | — |
| I2 | LWE Theorem 1, eqs. (5)–(7), the parity remark and the Discussion | Imported, read first-hand | Its appendix covers measurable ontic spaces, so no finiteness is assumed |

## 4. Outcome

### 4.1 Type (ii): stop, with the minimal additional structure named

| Capability | Within N | Smallest departure that supplies it | Status |
| --- | --- | --- | --- |
| Third read complementary to Z and X | Fails (node 2) | NNB | Conditional |
| Inaccessible parity, robust to reuse and recombination | Holds as a selection rule (Lemma Q), given P1 and P2 | — | Derived from A4 at `q = 2` |
| Encoded `S` | Fails (Lemma G2) | NNB plus R-ONE | Conditional |
| LWE transformation contextuality on the inaccessible sector | Not reached | NNB plus R-ONE | Conditional; forced by LWE Theorem 1 once (A1) and (A2) hold |
| Quantum operation set (C-CP) | Holds vacuously | Fails under NNB plus R-ONE (Lemma R; self-check c8) | Requires the posit I |
| Composites | — | Fails (node 10) | Outside Q-A |

**Conditional OI extension premise NNB.** P3 may arm a symmetric, center-free,
linear coupling between two cells of the same sublattice.

- **What it preserves (controls).** SA-1's Z/X law (graded protocols are
  unchanged), apparatus-1's Lemma 3, Lemma Q, C-ROT, C-NS with WL, C-B2 and C-L5.
- **What it buys.** Together with R-ONE: the encoded quarter phase and the
  Hadamard at single-qubit stabilizer scope, with the parity protected by
  Lemma Q.
- **Independent consequences (§A.29).**
  1. Encoded orientation-reversing maps become available (Lemma R). This
     consequence conflicts with the quantum target.
  2. A Y-type read always involves a second cell: a one-cell `z + x` read has
     `Q* = 1`.
  3. The construction fails two-qubit stabilizer correlations (node 10).

  NNB is therefore ruled out as a quantum source unless I holds.
- **What would derive it.** A native coupling graph with odd cycles at apparatus
  scale. The first decisive check is whether the state-dependent coupling graph
  of SM §3.1
  ([L104](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L104))
  or the preparation-induced edges of H-Bell (Substratum L48) can produce
  same-sublattice edges. Winding on an odd torus needs H-FIN and the whole torus.
- **What would rule it out.** Retaining the nearest-neighbour bipartite branch as
  physical (SM L226).
- **What would weaken it.** Nothing smaller was found. A center term (Route U)
  is a stronger change and loses the parity protection.

**Posit I.** The status of I:

- **Not adoptable.** It restricts the available operations to encoded rotations.
  It is fixed by the target, and any subgroup could be posited, so it is easy
  to vary.
- **What would derive it.** A native mechanism that makes the linear part of an
  odd Clifford and a `p`-flipping translation unavailable separately. Fixed
  affine offsets on the NNB coupling do not do this (self-check c8). An affine
  native rule would violate A5 (Substratum L100).
- **What would rule it out.** The availability of P3 armings of the individual
  couplings that compose `L`.

### 4.2 Answers to the three sub-questions

- **(A1).** Native: fail at (a), pass at (b) (Lemma Q). Under NNB: pass.
- **(A2).** Native: fail (Lemma G2). Under NNB plus R-ONE: pass.
- **(A3).** Native: not reached. Under NNB plus R-ONE: pass. The inaccessible
  sector comes from a conserved form, not from a traced-out hidden sector,
  which cannot host the parity (node 4).

### 4.3 No V3 round proposed

The native class is decided by proofs (G1, G2) and the extension by explicit
construction, so no finite search over native update rules is decisive. The
remaining open item is whether some mechanism derives I. That question concerns
which operations are available. It is not a rule-search question.

A search could be specified over fixed, always-on non-bipartite rules without
per-coupling arming. Its result would turn on the open question of what makes a
fixed evolution a selectable operation (node 4.2), not on the search itself.
Specifying it before that question is settled would not be decisive.

### 4.4 What remains for Q-B

This unit does not start Q-B. Two results bear on it.

1. The finite mechanism found here is dyadic and excludes `rot` (C-ROT).
2. C-CP, wing-locality and the composite checks of node 10 apply to any
   finite-resolution construction built on linear encodings. Lemma R's
   reflections and the Mermin–Peres parity constraint should be among Q-B's
   controls.

Neither result depends on the finiteness of the underlying sector.

### 4.5 Classification (§A.31)

| Finding | Class |
| --- | --- |
| Lemma G1 (sublattice grading of armed protocols) and the graded subgroup; it answers apparatus-1 §5.6's open generation question | New for this programme |
| Lemma G2 (no encoded `S` with native reads, any encoding or hidden sector) | New |
| Lemma Q (`u·v` conserved at `q = 2`; selection rule `Q* = 0` on determined functionals) | New |
| U′ realizes the 8-point mechanism under NNB plus R-ONE | New for this programme; the model is Wallman–Bartlett's as described by LWE |
| Lemma R (an odd Clifford factors into two encoded reflections) | New for this programme; consistent with LWE's parity remark |
| A shared parity signals; local parities fail composites | Elaborating (two-system leak); confirming (LWE Discussion) |
| The traced-out sector cannot host the parity natively | Positive (closes the owner's suggested branch) |

## 5. Assumption-watch markers

- **Center independence does work at `q = 2`.** Lemma Q makes A4 a superselection
  rule on `Q*`. Any proposal that adds self-terms, at any level, loses it.
- **Bipartiteness carries the native no-`S` result.** Any proposal that relies
  on a non-bipartite native graph (state-dependent graphs, odd tori, link
  carriers) must re-examine Lemma G1 and C-CP.
- **Arming individual couplings (P3) carries the reflection result.** A theory
  in which couplings are available only in fixed combinations changes Lemma R's
  consequence, not Lemma R itself.

## 6. Sources

### 6.1 Prior repository results

| Source | Use here | Review status |
| --- | --- | --- |
| [Apparatus-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md) §1.3, §3.4, §4.1–4.2, Lemma 3, Lemma 5, §5.2–5.7 | Ceiling, ledger, native read, isotropy, C-L5, P-8, Q-A | Merged (#1183) after three independent review rounds; ACCEPT at `af8df1b4` |
| [Two-system interface §2, §4](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L109) | C-LEAK; observer-relative hiddenness | Accepted at scoped review (#1173); on `main` |
| [Correlation recombination §3, §6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L246) | C-LEAK: a native recombination is a center-free coupling | Accepted at scoped review (#1173); on `main` |
| [Receiver assessment](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L269) | Masking; reciprocal identity | Accepted at scoped review (#1173); on `main` |
| [Observer-interface source](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L197) | Infinite-carrier and measure caveat (H-INF-μ) | Accepted at scoped review (#1173); on `main` |
| MR★ [S-L6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L595), [S-L7](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L603); MR-1 [AW-MR5](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L406), [Catani et al. row](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L752) | Symplectic step; epistemic restriction; recurrence | Frozen preregistration with append-only amendments; stage-1 token provisional |
| #914 [selection record](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707416018) and [named controls](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707509318) | Escape-test discipline: escape is not sufficiency | Issue records |
| Kernel declarations: [`PhasesAvailable`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/RouteB.lean#L132), [`FalsifierUnavailable`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/RouteB.lean#L179), [`rot`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/DiagonalTheory.lean#L368), [`permClass`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L236), [`onesFixing_not_phasesAvailable`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/PhaseSource.lean#L55), [`permClass_onesFixing`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/PhaseSource.lean#L82), [`scalar_center_chiral_iff`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/ChiralCenterRecovery.lean#L214) | Physical-carrier ceiling (unchanged, apparatus-1 Lemma 2); the observer-level chiral analogue | On `main`; kernel-checked statements, read and not rebuilt |
| Main [Definition](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L44), [Lemma 3](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L56), [§3.3 theorem](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L366); Substratum L48, A1, A3–A6; SM L104, L224, L226, L296, L302, L541 | Native class N, measure, C-NS, bipartite and chiral structure | Manuscript text at `main@b1d782f9` |

### 6.2 Imported literature

| Work | Used for | Read in this unit |
| --- | --- | --- |
| P. Lillystone, J. J. Wallman, J. Emerson, "Contextuality and the single-qubit stabilizer subtheory", arXiv:1802.06121v2 | Comparator definition (I1); Theorem 1 and its measure-theoretic appendix; eqs. (5)–(7); the parity remark; the Discussion on the toy theory, rebits and two-qubit preparation contextuality | Full text |
| J. J. Wallman, S. D. Bartlett, *Phys. Rev. A* 85, 062121 (2012) | Origin of the 8-state model | Not read; the model is used as LWE describe it |
| L. Catani, M. Leifer, D. Schmid, R. W. Spekkens, arXiv:2111.13727 | Epistricted mod-2 field theories are generalized-noncontextual | Not read in this unit; MR-1's reading (L752) |
| N. D. Mermin, *Phys. Rev. Lett.* 65, 3373 (1990); A. Peres (1991) | The name of the square in node 10. The operator identities used there were verified directly | Not read; cited for the construction's name only |

No literature result is a premise of nodes 1–3 or 6. Those are self-contained
algebra over `F_2` and `Z_q`.

## 7. Verification scope

The derivations are on paper. Exact author self-checks (c1–c9) were run
locally. They are not committed and are not evidence. All are
exact over `F_2`/`Z_q` with `Fraction` arithmetic.

| Check | What it covers |
| --- | --- |
| c1 | Lemma G1 with three breaking controls |
| c2 | Lemma G2, exhaustive for `n ≤ 3` |
| c3 | Route U, Route B (bundled versus native reads), parity bias |
| c4 | Route U's `H`, `T_1`/`T_2`, shared-parity signalling, generator closures |
| c5 | U′: `S`, group membership, the comparator, Lemma Q under random protocols with two controls, shared parity |
| c6 | U′: `H`, `T_1`/`T_2` |
| c7 | Composite `⟨YY⟩` |
| c8 | Affine offsets, all 256 |
| c9 | Copy-only reads and the one-cell countercontrol |

Route B in c3 is a graded encoding (`f_y = π_1 + π_2`). It passes the comparator
only with a supplied same-sector dephasing bundled into each read (2,380 cases,
0 failing). With native minimal reads it fails 294 cases, which is Lemma G2's
sequence. It is recorded as the bundled-read posit of P-8 and is not selected,
because the bundling is optional under P3.

No Lean build, simulation campaign, manuscript edit, freeze, dispatch or merge
was performed. Independent review of this file is a separate step.
