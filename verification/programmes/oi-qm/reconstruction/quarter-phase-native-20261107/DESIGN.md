# Q-A: a native source for the 8-point quarter-phase mechanism

**Standing.** Paper-only research unit for step 3 of #1169, question Q-A. Author:
Claude Code session, 2026-11-07. Scope: [owner approval and Q-A scope](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6712359044),
[owner direction on the three levels and the native/supplied distinction](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6711920779),
and the [Q-B target decision](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6712409082),
whose finiteness remark binds this unit: no step assumes that a traced-out or
inaccessible sector is finite unless the ledger names that as a hypothesis.
Q-B is out of scope.

This file proposes no premise for adoption. No simulation, enumeration campaign,
Lean build, manuscript change, freeze, dispatch or merge is part of it. Every
pass and fail verdict below rests on a paper argument. Small exact checks of this
file's own algebra were run as author self-checks (§7). They serve as controls on
that algebra; they are not evidence and carry no verdict.

**Source snapshot.** All repository links are pinned to `main` at
`b1d782f954f02cec578a10e071b73e48f86eb3dd` (cited as `main@b1d782f9`), which
contains the #1173 papers and the apparatus-1 record of #1183.

## 0. Result

1. **Native class, non-adaptive processes: the quarter phase is excluded (§2,
   nodes 1–4).** Center independence (A4) makes every native and P3-armed
   coupling free of self-terms. On a bipartite coupling graph such as the
   nearest-neighbour cubic lattice, every armed coupling then preserves a split
   of the slot variables into two sublattice-time sectors (Lemma G1). Each
   sector is Lagrangian. Two consequences follow:
   - at most two of the observer's native reads can disturb each other through
     reciprocal backaction;
   - for non-adaptive processes (no record feedback into armings or
     translations), no encoding of a qubit admits an encoded quarter phase `S`
     together with native X reads and the comparator's statistics (Lemma G2).
     This holds on any number of cells and with a hidden sector of any size,
     finite or not.

   The traced-out sector runs the same rule, so non-adaptive processes cannot
   draw `S` from it either. Adaptive native processes are not covered:
   apparatus-1's Lemma 5 counted them as SA-1 processes, and whether they can
   produce `S` is open (§4.3).
2. **A native protection of an absolute parity (§2, node 6).** At `q = 2` the
   native step conserves `Q = Σ_i x_i(t) x_i(t−1) mod 2` on any coupling graph
   with symmetric couplings and no self-terms. Under apparatus-1's supplied
   access posits P1 (terminal registration) and P2 (half-known ready cells),
   every functional the observer can determine has `Q* = 0`, with or without
   record feedback (Lemma Q). A functional with `Q* = 1` is therefore never
   determined, whatever the reuse, recombination, ancillas or records. The
   relative parity of two such functionals has `Q* = 0` and is not protected.
3. **Minimal departure (§2, nodes 5–8).** One change suffices for a
   quarter-phase mechanism: premise NNB, an armable symmetric coupling between
   two cells of the same sublattice (non-bipartite, still center-free and
   linear). The translations it needs are supplied by ready cells with a known
   value 1, which are instances of apparatus-1's P2 obtained through H-PREP.
   Under NNB, a two-cell carrier gives the following:
   - **(A1) pass.** It carries `z`, `x` and `y = z + x + p`, pairwise disturbing.
     The Z and X reads are native minimal reads. The Y read is a native minimal
     read conjugated by available couplings. The parity `p = z_2 + x_2` is never
     determined (Lemma Q). A shared parity cell signals, and a parity flip is
     detectable relative to a correlated reference parity cell.
   - **(A2) pass.** The encoded `S` is a center-free linear coupling word
     followed by a constant translation. Its read and continuation laws equal
     the comparator on the single-qubit stabilizer domain (proof by induction,
     node 8).
   - **(A3) pass relative to the encoded subtheory.** LWE's `T_1` and `T_2` are
     operationally equivalent on the encoded preparations and reads, and their
     realizations preserve and flip `p`, respectively. In the full NNB theory
     they are distinguishable through the parity cell's readable slots, and `S`
     is distinguishable from `I` on `Z±`. The contextuality is relative to the
     encoded subtheory, not to the observer's full accessible theory.
4. **Cost (§2, node 9).** In every linear encoding, the linear part of `S` and its
   translation each act on the encoded qubit as a reflection (Lemma R), and both
   are separately available. The translation reflection needs only constant
   translations, which are already in N. The reflection by the linear part needs
   NNB. Control C-CP therefore fails for every linear encoding whose parity is
   translatable, with or without NNB. It holds under the one-cell identification
   R1. The construction also does not compose (node 10, outside Q-A's scope).
5. **Outcome type (ii): stop (§4).**
   - Minimal additional physical structure, beyond apparatus-1's supplied P1,
     P2, P3, E-iso and H-PREP, for an encoded quarter phase at single-qubit
     stabilizer scope: NNB alone.
   - For a CP encoded single-qubit stabilizer operation set, a further premise I
     is needed: the linear part of an odd Clifford, and any translation that
     flips `p`, are available only together. I is a conditional premise, not
     adopted. As stated it is target-defined, easy to vary, and contradicts P3's
     arming of the individual couplings that compose that linear part.
   - The physical theory remains read-write-sourced, so the kernel no-go
     theorems apply to it unchanged (§6.1).
   - No V3 round is proposed. Two items are open: adaptive native `S` and a
     native derivation of I (§4.3).

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
- **Supply.** Attaching ready cells with one known slot (P2). P2 fixes which
  functional is known, not its value. A known value 1 is obtained through
  H-PREP, as a record-conditioned preparation.
- **Registration.** Registering a meter cell's record slot (P1, terminal).
- **Discarding.** Marginalizing cells.
- **Corrections.** Translations of slots by supplied constants, and adaptive
  record-conditioned armings and translations.

The hidden sector runs the same update
([Substratum L48](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Substratum.md#L48)).
Its size is not restricted.

A **native minimal read** is one armed coupling to one ready meter whose record
slot is then registered. Its only effects are the record and the reciprocal kick
into the conjugate slot
([apparatus-1 §4.1](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L464)).

**Adaptive and non-adaptive.** A process is *non-adaptive* when its armings and
translations depend only on settings, heralds and supplied constants, never on
records. Write `N_na` for the non-adaptive subclass of N.

Apparatus-1's Lemma 5 counts adaptive record-conditioned corrections among SA-1
processes
([L731](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L731)),
and its stochastic-matrix argument covers them on the one-cell carrier. N
therefore includes them. Which results cover which subclass:

- Lemmas G1 and Q are stated for all of N.
- Lemma G2, and the statement of node 1 about the generated group, are proved
  for `N_na` only.

P1, P2, P3, E-iso and H-PREP keep apparatus-1's classification as supplied
([ledger](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L411)).
A verdict "native" below means: within N, using no posit beyond these.

### 1.3 Sub-questions and their pass conditions

- **(A1) Carrier.** Pass iff both of the following hold.
  - (a) A subsystem built from cells carries three binary linear functionals
    `f_z`, `f_x`, `f_y`. Each is registrable by a native minimal read, or by a
    native minimal read conjugated by available couplings. Each read randomizes
    the other two through the reciprocal kick it transports.
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
- **(A3) Cost.** Pass iff LWE's `T_1` and `T_2`, operationally equivalent on the
  encoded subtheory's preparations and reads (LWE's notion), are realized by
  ontic maps that differ on a sector those preparations and reads do not
  access. A separate statement is required: whether the observer's full
  accessible theory distinguishes the two realizations.

### 1.4 Controls

| ID | Preserved result or requirement | Required outcome |
| --- | --- | --- |
| C-ROT | `rot` unreachable (apparatus-1 §5.3) | The encoded `rot` is unavailable, with every finiteness or measure hypothesis stated |
| C-NS | No-signalling of complete local histories | For a two-wing arrangement, each wing's complete local history law is independent of the remote settings |
| C-LEAK | The two-system hidden-parity leak ([two-system §4](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241)) and native recombination ([recombination §3](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L116)) | `p` is never determined, nor biased given the records, under reuse or recombination. A construction in which some permitted protocol exposes `p` fails (A1) |
| C-B2 | B2 fixed-instrument failure | Copy-only reads (reciprocal kick removed) must fail the comparator |
| C-EAR | E-AR obstruction scope | At most 2 pairwise perfectly distinguishable encoded preparations |
| C-L5 | Lemma 5 of apparatus-1 as countercontrol | Removing the extra cell must return to "no `S`" |
| C-CP | Introduced here: every available process induces a completely positive map on the encoded carrier | No available encoded map has an orientation-reversing (determinant −1) action on the Bloch octahedron |
| C-EX | §A.21 exactness | The structural invariants (grading, `Q`) are checked together with controls that must break them |

C-CP is added because escaping C-PH while adding a non-quantum encoded operation
is not progress toward the comparator. A failure of C-CP does not void the
computation; it is reported per encoding, with the resource that causes it.

### 1.5 Decision rule

- **D0.** A failed C-EX, C-B2 or C-L5 voids the verdict of the branch it controls.
- **D1.** Each of (A1)–(A3) is decided within N first. Any sub-question that
  passes in N gets the verdict "native". A verdict proved only for `N_na` is
  stated with that scope.
- **D2.** If one fails in N, the smallest single departure from N that makes
  it pass is identified. Each departure is stated as a conditional premise,
  together with what it preserves (controls), what it buys and its independent
  consequences (§A.29).
- **D3.** Outcome types:
  - (i) if (A1)–(A3), C-ROT, C-NS, C-LEAK and C-CP all pass in N;
  - (ii) if passing needs a new premise, or C-CP fails;
  - (iii) if the decisive remaining question is a finite search over native
    update rules.

## 2. Depth-first walk

Each node is closed by a paper argument.

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
- `v_i(t)` is a linear combination of variables of type `t + χ_i + 1` only;
- within each record branch, an adaptive choice of coefficients changes nothing,
  since each branch is a fixed armed sequence.

*Proof.* By induction. The update `u_i(t+1) = Σ_j k_ij u_j(t) − v_i(t)` adds
neighbours `j` with `χ_j = χ_i + 1`, of type `t + χ_i + 1`, and `v_i(t)`, of type
`t + χ_i + 1`. That is the required type `(t + 1) + χ_i`. Also `v_i(t+1) = u_i(t)`.
A self-term would add `u_i(t)`, of type `t + χ_i`; that is the only place the
induction uses `k_ii = 0`. ∎

**What the lemma covers.** It concerns couplings: no armed coupling mixes the
sectors. A classical feedforward that translates a slot of one sector by a
record value from the other sector is not a coupling, and the lemma does not
cover it. Such feedforward correlates the sectors in the joint law.

**Consequences.**

- **Every record is single-sector.** A record is a slot value, so it is a
  linear functional of the variables of one type (one sector).
- **Each sector is Lagrangian.** The cell form `ω = Σ_i u_i ∧ v_i` pairs a type-`τ`
  variable with a type-`τ+1` variable. Each sector is therefore isotropic, of
  half dimension. Two single-sector functionals of the same sector commute.
- **The generated maps are the graded subgroup (for `N_na`).** In the per-cell
  encoded frames `J^{−t}` of apparatus-1, every non-adaptive process acts by
  `A ⊕ A^{−T}` on (sector E, sector O), plus constant translations.
  - One coupled tick at a given parity is one graded transvection between the
    two cells.
  - On a connected bipartite graph these transvections generate the elementary
    subgroup of `GL(n, Z_q)`. At `q = 2` that is all of `GL(n, F_2)`.
  - A graded transvection between two same-colour cells `c_1, c_2` is obtained
    through an opposite-colour mediator `m`: from four coupled ticks at
    alternating parities, the commutator `[E_{c_2 m}, E_{m c_1}] = E_{c_2 c_1}`,
    with `m` returned.
- **Phase shears and Fourier maps are not generated (for `N_na`).** For
  encodings whose Z and X functionals are single-sector, no same-cell phase shear
  (`x ↦ x + a z`) and no Fourier map (`z ↔ x`) is generated, at any `q`. For odd
  `q` this bears on apparatus-1's open expectation that SA-1 gives the qudit
  stabilizer theory
  ([§5.6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L1065)):
  on a bipartite graph, non-adaptive per-edge couplings do not generate the full
  symplectic group, and the qudit phase and Fourier gates lie outside it. The
  adaptive case is open (§4.3).
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

**Control (C-EX).** Self-check c1 found no violation on bipartite graphs at
`q = 2, 3, 5`. Three controls break the grading as they must: a self-term, an
odd cycle, and a meter–meter edge.

**Verdict.** Native couplings preserve a two-sector Lagrangian grading.

### Node 2. Native complementarity: at most two mutually disturbing reads

A native minimal read of a single-sector functional `f` kicks only the conjugate
slot. That slot lies in the other sector, so the read changes the value of no
same-sector functional. Three reads that pairwise disturb by backaction would
need three functionals pairwise in different sectors. There are two sectors.

**Verdict.** Within N, (A1)(a) fails for every encoding: at most two of the
three encoded reads can be native minimal reads that disturb each other. This
holds for adaptive processes as well, since it concerns the kick of a single
read. A third mutual disturbance needs an operation besides the read. That
operation can be omitted, and omitting it lets the observer know two
complementary encoded values at once. That is the sharpening behind C-EAR.

### Node 3. Can non-adaptive processes in N induce `S`? Lemma G2

**Lemma G2 (graded quarter-phase obstruction, non-adaptive).** Fix any encoding
of a qubit. The hypotheses are:

- any number of cells and ancillas, and a hidden sector of any size, with or
  without E-iso;
- the encoded X read is a native minimal read of an O-sector functional `f_X`,
  with heralded failure acting as the encoded identity (as in SA-1);
- free evolution acts as the encoded identity in the fixed frame (C8);
- `S` is any process of `N_na` (fresh ancillas, internal registrations without
  feedback, supplied constant translations allowed).

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
any hidden-sector size. It needs non-adaptivity, at step 3. Suppose a record of
an E-sector functional `g`, with `ω(f_X^{mid}, g) ≠ 0`, is fed into a
translation of an O slot. The record then carries the middle read's E-sector
kick into the O sector, and the identity of step 3 fails. Adaptive processes
are therefore outside the lemma. That is a class apparatus-1's Lemma 5 includes,
and the question is open (§4.3).

**Control.** Self-check c2 examined every graded affine `S` and every
O-functional encoding on `n ≤ 3` cells. No case reproduces both R1 and R0.

**Verdict.** For non-adaptive processes in N, (A2) fails for every encoding.
This includes encodings that place any cell in the traced-out sector.

### Node 4. The traced-out sector as the home of the parity

The owner's suggestion was to put the parity bit in the traced-out sector. Three
closures apply.

1. **Same rule.** Hidden cells run the native rule (Substratum L48), so Lemma G2
   covers every non-adaptive process that involves them, always-on hidden
   coupling included.
2. **Reciprocal access.** Suppose the observer can arm an edge `c–h` and supply
   `c` ready as `(w, 0)`. The coupled tick gives `u_c' = k u_h` (apparatus-1
   §4.1), so every slot of `h` is registrable at the matching parity. A cell that
   an available `S` must couple to therefore has no inaccessible slot.

   If the observer cannot arm any edge into `h`, then `S` can only be native free
   evolution. A fixed free evolution is absorbed into the fixed frame (PC-F1),
   so it is not a selectable operation.

   If `h` is instead coupled to a maximal-entropy hidden background, a read of
   `h` through `c` is masked
   ([receiver assessment, eq. (3) and §6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L144)).
   But the same coupling feeds background unknowns into the carrier while it is
   coupled. This file does not establish a general masking-without-randomization
   statement and claims none.
3. **Shared sector.** A parity cell shared by two wings signals. Take Route U of
   node 5 with the parity cell shared. Bob's encoded `y_B` contains the shared
   `p`, and Alice's `S` flips `p`. So Bob's `Y` read on `Y_+` changes from 0 to 1
   with certainty. This is the two-system leak of
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
- **`S` exists.** For example `x_1 ↦ z_1 + x_1 + z_2 + 1`, `z_2 ↦ z_2 + 1`,
  `x_2 ↦ x_2 + z_1`. Its linear part contains the same-cell shear `x_1 += z_1`,
  which needs the center term.
- **The parity is accessible.** `p = z_2` is a single slot, registrable by
  reciprocal access (node 4.2). (A1)(b) fails.

The center term also breaks the conserved form of node 6.

**Route NNB: a same-sublattice coupling (keeps A4 and A5).** P3 may arm a
symmetric, center-free coupling between two cells of the same colour, for
example next-nearest neighbours. In the common encoded frame this coupled tick
acts as `x_1 += z_2, x_2 += z_1` at one tick parity (call it `Na`), and as
`z_1 += x_2, z_2 += x_1` at the other. It breaks bipartiteness, so Lemma G1 does
not apply. Encoding U′:
- the same two cells, of the same colour;
- `f_z = z_1`, `f_x = x_1`, `f_y = z_1 + x_1 + z_2 + x_2`, so `p = z_2 + x_2`.

Bounded coupling degree (A3) admits such couplings. SM adopts the
nearest-neighbour branch as a premise beyond A3 (L226), so NNB is a departure
from that branch, not from A1–A6.

**Selection.** Route U fails (A1)(b) outright. NNB is the decisive branch.

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
  determine has `Q* = 0`. This holds for every process in N, adaptive or not, and
  for NNB couplings.

*Proof.*

- (i) `Q(u', v') = Σ_i (Σ_j k_ij u_j − v_i) u_i = Σ_{i,j} k_ij u_i u_j − Q(u, v)`.
  The double sum is `2 Σ_{i<j} k_ij u_i u_j ≡ 0`, and `−1 = 1`. A center term
  would add `Σ_i k_ii u_i`.
- (ii) The step `M` is symplectic and preserves `Q`. Transporting functionals
  acts by `M^{−T} = J M J^{−1}`, and `Q` is invariant under the coordinate swap
  `J`.
- (iii) Condition on all of the observer's records. Each branch is then a fixed
  sequence of symplectic center-free steps and constant translations, because a
  record-controlled translation is a constant given the record. Translations
  change values, not which functionals are determined. By apparatus-1's Lemma 3
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
  condition on the size of the hidden sector.
- **A conserved quantity at `q = 2` only.** SM records conserved quadratic forms
  of the exact rule for general `q`
  ([L296](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/SM.md#L296)).
  The form `u·v` is a `q = 2` invariant not listed there. Modulo 2 its energy
  `E` reduces to `Σu + Σv + u·Av`, a different quantity.
- **Role of A4.** Lemma Q is where center independence does work at `q = 2`.
  NNB keeps it.
- **Absolute and relative parity.** The rule protects every single `Q* = 1`
  functional. It does not protect the sum of two of them. That sum has
  `Q* = 1 + 1 + ω = 0` when they commute, and it can be determined.
- **The P1-removed case is an existing construction.** The recombination paper's
  passive two-slice receiver registers both slots of a cell
  ([recombination §1](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L26)).
  It therefore determines that cell's `Q* = 1` functional `u + v`. It is the
  P1-removed control in existing form.

**Controls (C-EX).** Self-check c5 ran random center-free protocols with ready
cells and minimal reads. The protected functional was never determined. Two
controls must break the protection, and do: center terms allowed, and P1
removed (the kick variable also registered).

**Verdict.** Natively (A4, at `q = 2`), and given the supplied P1 and P2, a
functional with `Q* = 1` is permanently undetermined for the observer, whatever
the protocol.

### Node 7. (A1) under NNB

The three encoded functionals are:

- `f_z = z_1`, `f_x = x_1` and `f_y = z_1 + x_1 + z_2 + x_2`. Each has `Q* = 0`, so
  Lemma Q allows each to be determined.
- `ω(f_z, f_x) = ω(f_z, f_y) = ω(f_x, f_y) = 1`.
- The parity `p = f_x + f_y + f_z = z_2 + x_2` has `Q* = 1`.

**Reads.**
- `f_z` and `f_x` are slots of the carrier, registered by native minimal reads.
- `f_y` is not a slot. It is registered by a native minimal read conjugated by
  available couplings: apply `L^{−1}`, the linear word of node 8, then a native
  X read, then `L`. The conjugation needs no translation, because `L` maps
  `f_x` to `f_y` exactly.
- By symplectic covariance, the kick of this composite is the transported kick
  of the X read, which is along `J f_y`.
- A read of any `f_a` along `J f_a` changes each other encoded functional `f_b`
  by `w · ω(f_b, f_a) = w`. So each read randomizes the other two.

A single-cell `Y` functional `z_1 + x_1` has `Q* = 1`, so it is never
determined. This matches node 2 and Lemma 5: a Y read always involves a second
cell.

| Check | Result |
| --- | --- |
| (A1)(a) | Pass under NNB, with the Y read as a conjugated native minimal read |
| (A1)(b) | Pass, by Lemma Q. Given the records, `p` is never determined, and it is uniform under N2. This covers reuse of the parity cell and native recombination, since both are center-free couplings |
| C-LEAK within one wing | Green for the absolute parity. Reciprocal access reads `z_2` or `x_2`. They do not commute, so either read kicks the other and `p` stays undetermined |
| C-LEAK across wings, shared parity cell | Red. A shared parity cell signals (node 4.3; the same argument applies to U′) |
| C-LEAK with a correlated reference parity cell | The relative parity `p + p_R` has `Q* = 0` and can be determined. A flip of `p` (by `S` or `H`) is then detectable relative to the reference. `p` itself stays undetermined |
| C-EAR | Green. At most one of `f_x, f_y, f_z` is determined in any isotropic knowledge state, because they pairwise do not commute. Encoded laws lie in the octahedron, and at most two encoded preparations are perfectly distinguishable |

### Node 8. (A2) and (A3) under NNB

**The operation.** Write `C12` for the graded transvection
`z_2 += z_1, x_1 += x_2`, realized through a mediator (node 1). Write `Na` for
the NNB coupled tick `x_1 += z_2, x_2 += z_1`. Let `L = Na ∘ C12`, with `C12`
applied first. Then:

- `L`: `z_1 ↦ z_1`, `x_1 ↦ z_1 + x_1 + z_2 + x_2`, `z_2 ↦ z_1 + z_2`,
  `x_2 ↦ x_2 + z_1`.
- On the encoded functionals: `f_x∘L = f_y`, `f_y∘L = f_x`, `f_z∘L = f_z`,
  `p∘L = p`.
- Let `τ` translate `x_1` by 1 and `z_2` by 1. Each is one coupled tick with a
  ready cell whose known slot is 1 (P2 through H-PREP).
- `S := τ ∘ L` gives `f_x∘S = f_y + 1`, `f_y∘S = f_x`, `f_z∘S = f_z`, `p∘S = p + 1`.
  These are the value-level identities of the encoded `S`.
- `L` and `S` are symplectic: they are compositions of symplectic steps and a
  translation.

**(A2), by induction.** Let `Λ_{a,b}` be the uniform law on the level set
`{f_a = b}`, with all else uniform, and let `Λ_0` be the uniform law.

1. *Reads.* A read of `f_a` along `J f_a` acts as follows.
   - On `Λ_{a,b}` it records `b` with certainty. The kick leaves `{f_a = b}`
     invariant, since `f_a(J f_a) = 0`, so the law stays `Λ_{a,b}`.
   - On `Λ_{c,b}` with `c ≠ a`, it records a uniform `r`. Conditioning gives
     `{f_c = b, f_a = r}`. The kick changes `f_c` by `w` (since `ω = 1`) and keeps
     `f_a`. With `w` uniform, the result is `Λ_{a,r}`.
   - On `Λ_0` it records a uniform `r` and leaves `Λ_{a,r}`.

   These are the comparator's Pauli-read transitions on the six eigenstates and
   the maximally mixed state.
2. *The operation.* The bijection `S` maps a uniform law on a set to the uniform
   law on its image. The identities above give `S(Λ_{x,b}) = Λ_{y,b}`,
   `S(Λ_{y,b}) = Λ_{x,b+1}`, `S(Λ_{z,b}) = Λ_{z,b}` and `S(Λ_0) = Λ_0`. These are the
   comparator's transitions for `S`, with the Bloch convention "bit 0 = +".
3. *Induction.* The model's family `{Λ_{a,b}, Λ_0}` and the comparator's family
   (six eigenstates and the maximally mixed state) are each closed under reads
   and `S`, with equal record laws and corresponding post-states at every step.
   Induction on the sequence length gives equal joint record laws for every
   finite sequence, and linearity extends this to mixtures.

**Pass**, under NNB. The constant translation is P2 through H-PREP, so no other
departure is needed. Self-check c5 matches the comparator on all sequences up to
length 4 (control).

**(A3).** Take `T_1` as the uniform mixture of the encoded Paulis, which are the
cell-1 translations `z_1 += 1` and `x_1 += 1`. Take `T_2` as `T_1` followed by
the encoded `H`.

- **The encoded `H`.** It needs `f_z ↔ f_x` and `f_y ↦ f_y + 1`. One realization
  composes a center-free linear part with a `p`-flipping translation (Lemma R
  below).
- **The encoded subtheory.** Both maps send every encoded state to `Λ_0`, so
  they are operationally equivalent on the encoded preparations and reads.
- **The ontic level.** The Pauli translations preserve `p`. `H` flips it. So
  `T_1` preserves `p` and `T_2` flips it, as in LWE's eqs. (6) and (7) with
  `xyz ↔ p`.
- **Verdict relative to the encoded subtheory: pass.** The two realizations
  differ on `p`, which the encoded preparations and reads never access.
- **The full NNB theory.** Three kinds of trace make the realizations
  distinguishable there:
  1. `T_2`'s realization also changes the parity cell's slots: its translation
     flips `z_2` or `x_2`, and its linear part mixes them. Those slots are
     readable (node 7). For instance, from encoded `Z_+` with `z_2 = 0` known,
     `T_1` leaves `z_2 = 0` and `T_2` does not.
  2. `S` itself is distinguishable from `I` on `Z_±`. With `z_2` known, `S` flips
     it deterministically.
  3. A twirl `(z_2, x_2) += (b, b)` with uniform `b` preserves `p` and
     randomizes `z_2` and `x_2`. Composed with the twirl, the two maps differ
     within one system only on `p`. With a correlated reference parity cell,
     the flip of `p` is detectable again (node 7).

  The observer's full accessible theory therefore contains no equivalence of the
  LWE type between these realizations. The transformation contextuality is
  relative to the encoded subtheory.

  By LWE Theorem 1, any preparation-noncontextual model of the full subtheory
  has this subtheory-relative feature. What this unit derives beyond the theorem
  is the sector: `p`, made inaccessible by A4 together with P1 and P2.

**C-ROT.** Green without H-FIN, under N2, which needs H-INF-μ for an infinite
hidden sector. Every record probability is then a count of uniform bits within
a finite cone, so it is dyadic, conditional on herald success. The `rot` Z-read
probability `9/25` is not dyadic. With non-uniform hidden priors the dyadic
argument is unavailable, and apparatus-1 §5.3 then applies only under H-FIN,
with Markovian reuse of a finite carrier.

**C-NS.** Green with wing-local parity cells, under the hypotheses (i)–(iv) of
Main's
[cone and screening theorem](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L366).
Each wing's maps and kicks act only on its own cells. Red with a shared parity
cell (node 7).

**C-B2.** Green. Without the kick, a Z read on `Λ_{x,b}` leaves `f_x = b`, so a
subsequent X read is deterministic. The comparator requires it to be uniform.

**C-L5.** Green. Removing the parity cell puts the encoding under R1, and
apparatus-1's Lemma 5 excludes `S` there by any stochastic map.

### Node 9. Lemma R and C-CP

**Lemma R (two reflections in every linear encoding).** Take an encoding in which
each encoded Pauli eigenstate is a level set `{f_a = b}` of a linear functional,
with "bit 0 = +". Let the encoded `S` be an affine bijection with linear part
`L` and translation `τ`. Then:

- `L` maps the encoded state family to itself, and its encoded action is a pure
  axis permutation of determinant −1;
- the translation `τ` also acts as determinant −1;
- `τ` flips `p`, that is, `p(τ) = 1`.

*Proof.*

1. **`L` has determinant −1.** A linear bijection maps the subspace `{f_a = 0}`
   to a subspace. Being an encoded level set, that subspace contains 0, so it is
   `{f_{π(a)} = 0}`. Hence `f_a ∘ L^{−1} = f_{π(a)}` exactly, and `L` acts as the
   permutation matrix of `π` on Bloch vectors. For `S` the permutation `π` is the
   transposition `(x y)`, so the determinant is −1.
2. **`τ` has determinant −1.** A translation flips the sign of each axis `a`
   with `f_a(τ) = 1`. Since `S = τ ∘ L` has determinant +1, `τ` flips an odd
   number of axes.
3. **`τ` flips `p`.** Because `p = f_x + f_y + f_z`, an odd number of flips
   means `p(τ) = 1`. ∎

The same holds for `H`, and for every Clifford whose axis permutation is odd.
These are exactly the parity-flipping elements in LWE's remark that "the
Hadamard swaps it (as does the phase gate P)".

**Separate availability, in every linear encoding.**

- **The linear part.** A process built from P3 couplings and P2 ready cells is
  affine in the known constants it uses. The same process with every known-1
  cell replaced by a known-0 cell, which P2 supplies, is the linear part `L`.
- **The translation.** `τ = S ∘ L^{−1}` is a constant translation. It is
  available on its own, as one coupled tick with a known-1 ready cell per
  translated slot.

**C-CP, per encoding.**

- **Under R1 (one cell, `N_na`).** By Lemma G1, each branch of a non-adaptive
  process maps the carrier pair to `(α z + e, β x + o)`. Here `α, β ∈ F_2` and
  `(e, o)` are ancilla values independent of the carrier. If both slots are
  retained (`α = β = 1`), the branch is a mixture of translations, that is, of
  encoded Paulis. Otherwise it reads at most one carrier slot and prepares a law
  on the four points. By apparatus-1's Lemma 3 that law lies in the octahedron,
  hence in the Bloch ball. The branch is then a measure-and-prepare map.
  Mixtures of Pauli channels and of measure-and-prepare maps onto valid states
  are CP, so C-CP holds.
- **For any linear encoding with a translatable parity, within N already.** A
  single translation with `p(τ) = 1` and an odd number of flipped axes is
  available from P2 through H-PREP. In U′ that is `z_2 += 1`, which flips `f_y`
  only and acts as `Y ↦ −Y`. So C-CP fails without NNB. This reflection is
  attributed to the constant-translation resource.
- **Under NNB.** The linear part `L` is also available. It acts as `X ↔ Y` with
  `Z` fixed: a second reflection, attributed to NNB.

**Fixed offsets do not weld the factors.** Suppose each same-sublattice coupling
carried a fixed affine offset, so that `L` and `τ` might cease to be separately
available. Self-check c8 is a control on this: with the graded couplings and the
encoded Pauli translations, all 256 offset pairs generate groups that contain
both `S` and an encoded reflection.

**Verdict.** In linear encodings, NNB buys the quarter phase only together with
both encoded reflections. Excluding them needs premise I (§4.1).

### Node 10. Composites (outside Q-A's scope; recorded for #868)

- **Wing-local parities.** Start from encoded `Z_+ Z_+`, apply encoded `H` on
  wing A, then an encoded CNOT. The CNOT is a graded coupling between the
  carrier cells. It acts on the encoded functionals as a CNOT:
  `f_y^A ↦ f_y^A + f_x^B` and `f_y^B ↦ f_y^B + f_z^A`.
  - The determined functionals are `f_x^A + f_x^B` and `f_z^A + f_z^B`. Their sum
    is `f_y^A + f_y^B + p_A + p_B`.
  - With independent uniform parities, `f_y^A + f_y^B` is undetermined. So
    `⟨XX⟩ = ⟨ZZ⟩ = 1` and `⟨YY⟩ = 0`.
  - The comparator's `Φ⁺` has `⟨YY⟩ = −1`.
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
| P1 | Terminal registration | Supplied (apparatus-1) | Load-bearing for Lemma Q: the two-slice receiver and the c5 control determine `Q* = 1` functionals without it |
| P2 | Half-known ready cells. The known functional is a slot; its value is 0, or 1 through H-PREP | Supplied (apparatus-1) | Load-bearing for Lemma Q. A supplied cell with known `u + v` would carry `Q* = 1`. The value-1 instances supply every constant translation |
| P3, E-iso | Per-tick, per-edge armed couplings; isolation | Supplied (apparatus-1) | Lemma G2 needs non-adaptive arming |
| H-PREP | Record-conditioned classes read as laboratory preparations | Supplied (open hypothesis) | As in apparatus-1; also supplies P2's value-1 cells |
| NNB | Armable symmetric center-free coupling between same-sublattice cells | Supplied (new conditional premise) | Not adopted (§4) |
| WL | Parity cell local to its wing | Design condition | Derived necessity: shared parity signals |
| I | Linear parts of odd Cliffords and `p`-flipping translations available only together | Supplied (conditional premise) | Not adopted. As stated it is target-defined and easy to vary, and it contradicts P3's arming of the individual couplings (§4.1) |
| E-U′ | Encoded identification of §2 node 5, fixed for all settings | Mathematical representation | — |
| H-FIN | Finiteness of the total carrier | Hypothesis, used only where named | Odd-torus winding (node 1); the finite-carrier form of C-ROT |
| H-INF-μ | Normalized product law on the hidden variables in a protocol's cone | Hypothesis | N2 statistics and the dyadic C-ROT with an infinite hidden sector |
| I1 | Single-qubit stabilizer comparator, Lüders reads, CPTP | Imported (comparator only) | — |
| I2 | LWE Theorem 1, eqs. (5)–(7), the parity remark and the Discussion | Imported, read first-hand | Its appendix covers measurable ontic spaces, so no finiteness is assumed |

## 4. Outcome

### 4.1 Type (ii): stop, with the minimal additional structure named

| Capability | Within N | Smallest departure that supplies it | Status |
| --- | --- | --- | --- |
| Third read complementary to Z and X | Fails (node 2; adaptive included) | NNB | Conditional |
| Inaccessible absolute parity, robust to reuse and recombination | Holds as a selection rule (Lemma Q), given P1 and P2, adaptive included | — | Derived from A4 at `q = 2`. The relative parity is not protected |
| Encoded `S` | Fails for `N_na` (Lemma G2). Open for adaptive processes | NNB | Conditional |
| LWE transformation contextuality on the inaccessible sector | Not reached | NNB | Conditional, relative to the encoded subtheory only (node 8) |
| CP encoded single-qubit stabilizer operation set (C-CP) | Holds under R1 for `N_na`. Fails for linear encodings with a translatable parity | Fails under NNB (Lemma R) | Requires the conditional premise I |
| Composites | — | Fails (node 10) | Outside Q-A |

**Conditional OI extension premise NNB.** P3 may arm a symmetric, center-free,
linear coupling between two cells of the same sublattice.

- **What it preserves (controls).** SA-1's Z/X law (graded protocols are
  unchanged), apparatus-1's Lemma 3, Lemma Q, C-ROT, C-NS with WL, C-B2 and C-L5.
- **What it buys.** The encoded quarter phase and the Hadamard at single-qubit
  stabilizer scope, with the absolute parity protected by Lemma Q. Constant
  translations come from P2 through H-PREP.
- **Independent consequences (§A.29).**
  1. A second encoded reflection, the linear part `L`, becomes available
     (Lemma R). This consequence conflicts with the quantum target.
  2. A Y-type read always involves a second cell: a one-cell `z + x` read has
     `Q* = 1`.
  3. The construction fails two-qubit stabilizer correlations (node 10).

  NNB is therefore ruled out as a source of a CP stabilizer operation set unless
  I holds.
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

**Conditional premise I.** Not adopted. As stated it restricts the available
operations to encoded rotations: the linear part of an odd Clifford and any
`p`-flipping translation are available only together. It is defined by the
target and is easy to vary, since any subgroup could be posited.

- **Conflict with P3.** I contradicts P3's arming of the individual couplings
  that compose `L`.
- **Not rescued by a constant.** Under I, the constant translations of P2
  through H-PREP must also be restricted.
- **What would derive it.** A native mechanism that makes the two factors
  unavailable separately. Fixed affine offsets on the NNB coupling do not
  (node 9). An affine native rule would violate A5 (Substratum L100).

**Position relative to the kernel no-go theorems.** Every process in N, with or
without NNB, is a configuration bijection with fresh ready cells and
registrations. So the physical theory's operations lie in `permClass`
(apparatus-1 Lemma 2): it is a subtheory of `permTheory`, and the kernel
theorems `permTheory_not_control`, `permTheory_not_qm` and
`monomialSource_not_qm` apply to it unchanged (§6.1). `S` and `H` are encoded
maps only. The construction claims neither composite unitary control nor exact
finite QM.

### 4.2 Answers to the three sub-questions

- **(A1).**
  - Native: fail at (a), including adaptive processes; pass at (b) (Lemma Q).
  - Under NNB: pass. The absolute parity is protected and the relative parity is
    not.
- **(A2).**
  - Native: fail for non-adaptive processes (Lemma G2); open for adaptive
    processes.
  - Under NNB: pass.
- **(A3).**
  - Native: not reached.
  - Under NNB: pass relative to the encoded subtheory. In the full NNB theory the
    realizations are distinguishable through the parity cell, and the
    traced-out hidden sector cannot host the parity (node 4).

### 4.3 Open items, and no V3 round

**Open items.**

1. **Adaptive native `S`.** Can a process of N with record feedback, with
   record-controlled armings or translations, induce the encoded `S` under some
   encoding? This is the class apparatus-1's Lemma 5 includes.
   - Lemma G2 does not decide it.
   - Nodes 2 and 6 hold with feedback. Each read's kick stays single-sector, and
     Lemma Q holds.
   - A decision needs either a paper proof that covers feedforward from records
     into slots of the other sector, or a counterexample.
   - A closure over a bounded protocol class (fixed cells, fixed ancilla budget)
     decides that class only. Such a closure is not decisive for the open item,
     so it is not proposed as a V3 round.
2. **A native derivation of I** (§4.1).
3. **Masking without randomization** for a parity cell coupled to a
   maximal-entropy background (node 4.2).

**No V3 round.** The native update-rule class is decided by proofs (G1, Q, and
G2 for non-adaptive processes), and the extension by an explicit construction
with paper proofs. No finite search over native update rules is decisive. The
open items concern available protocols and operations, not update rules.

### 4.4 What remains for Q-B

This unit does not start Q-B. Two results bear on it.

1. The finite mechanism found here is dyadic and excludes `rot` (C-ROT).
2. C-CP, wing-locality and the composite checks of node 10 apply to any
   finite-resolution construction built on linear encodings. Lemma R's
   reflections and the Mermin–Peres parity constraint should be among Q-B's
   controls.

Neither result uses H-FIN. Both hold under N2, with H-INF-μ for an infinite
hidden sector.

### 4.5 Classification (§A.31)

| Finding | Class |
| --- | --- |
| Lemma G1 (sublattice grading of armed couplings) and the graded subgroup generated by non-adaptive processes; it answers apparatus-1 §5.6's generation question for that class | New for this programme |
| Lemma G2 (no encoded `S` with native reads, non-adaptive processes, any encoding or hidden sector); the adaptive case is open | New |
| Lemma Q (`u·v` conserved at `q = 2`; selection rule `Q* = 0` on determined functionals, with feedback included) | New |
| U′ realizes the 8-point mechanism under NNB alone, with LWE's contextuality relative to the encoded subtheory | New for this programme; the model is Wallman–Bartlett's as described by LWE |
| Lemma R (an odd Clifford factors into two encoded reflections) | New for this programme; consistent with LWE's parity remark |
| A shared parity signals; the relative parity is readable; local parities fail composites | Elaborating (two-system leak); confirming (LWE Discussion) |
| The traced-out sector cannot host the parity natively | Positive (closes the owner's suggested branch) |

## 5. Assumption-watch markers

- **Center independence does work at `q = 2`.** Lemma Q makes A4 a superselection
  rule on `Q*`. Any proposal that adds self-terms, at any level, loses it.
- **Bipartiteness carries the non-adaptive no-`S` result.** Any proposal that
  relies on a non-bipartite native graph (state-dependent graphs, odd tori, link
  carriers) must re-examine Lemma G1 and C-CP.
- **Arming individual couplings (P3) carries the reflection result.** A theory
  in which couplings are available only in fixed combinations changes Lemma R's
  consequence, not Lemma R itself.
- **Record feedback is outside Lemma G2.** Any proposal that uses classical
  feedforward of records into slot values needs its own argument.

## 6. Sources

### 6.1 Prior repository results

| Source | Use here | Review status |
| --- | --- | --- |
| [Apparatus-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md) §1.3, §3.4, §4.1–4.2, Lemma 3, Lemma 5, §5.2–5.7 | Ceiling, ledger, native read, isotropy, C-L5, P-8, Q-A | Merged (#1183) after three independent review rounds; ACCEPT at `af8df1b4` |
| [Two-system interface §2, §4](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L109) | C-LEAK; observer-relative hiddenness | Accepted at scoped review (#1173); on `main` |
| [Correlation recombination §1, §3, §6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md#L246) | C-LEAK: a native recombination is a center-free coupling, and the two-slice receiver is the P1-removed case | Accepted at scoped review (#1173); on `main` |
| [Receiver assessment](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md#L269) | Masking; reciprocal identity | Accepted at scoped review (#1173); on `main` |
| [Observer-interface source](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L197) | Infinite-carrier and measure caveat (H-INF-μ) | Accepted at scoped review (#1173); on `main` |
| MR★ [S-L6](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L595), [S-L7](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md#L603); MR-1 [AW-MR5](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L406), [Catani et al. row](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md#L752) | Symplectic step; epistemic restriction; recurrence | Frozen preregistration with append-only amendments; stage-1 token provisional |
| #914 [selection record](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707416018) and [named controls](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6707509318) | Escape-test discipline: escape is not sufficiency | Issue records |
| Kernel declarations: [`PhasesAvailable`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/RouteB.lean#L132), [`FalsifierUnavailable`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/RouteB.lean#L179), [`rot`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/DiagonalTheory.lean#L368), [`permClass`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L236), [`onesFixing_not_phasesAvailable`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/PhaseSource.lean#L55), [`permClass_onesFixing`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/PhaseSource.lean#L82), [`scalar_center_chiral_iff`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/ChiralCenterRecovery.lean#L214) | Physical-carrier ceiling (unchanged, apparatus-1 Lemma 2); the observer-level chiral analogue | On `main`; kernel-checked statements, read and not rebuilt |
| [`permTheory_not_control`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L708), [`permTheory_not_qm`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L717) and [`monomialSource_not_qm`](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/verification/lean-mathlib/OIBridge/SubstratumInterface.lean#L192) | The physical theory of N, with or without NNB, has its operations in `permClass` (every process is a configuration bijection with fresh cells and registrations), so these theorems apply to it: it has no composite unitary control and is not exact finite operational QM. The construction here claims neither; `S` and `H` are encoded maps only | On `main`; kernel-checked statements, read and not rebuilt |
| Main [Definition](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L44), [Lemma 3](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L56), [§3.3 theorem](https://github.com/amaybaum/incompleteness/blob/b1d782f954f02cec578a10e071b73e48f86eb3dd/papers/Main.md#L366); Substratum L48, A1, A3–A6; SM L104, L224, L226, L296, L302, L541 | Native class N, measure, C-NS, bipartite and chiral structure | Manuscript text at `main@b1d782f9` |

### 6.2 Imported literature

| Work | Used for | Read in this unit |
| --- | --- | --- |
| P. Lillystone, J. J. Wallman, J. Emerson, "Contextuality and the single-qubit stabilizer subtheory", arXiv:1802.06121v2 | Comparator definition (I1); operational equivalence relative to the subtheory; Theorem 1 and its measure-theoretic appendix; eqs. (5)–(7); the parity remark; the Discussion on the toy theory, rebits and two-qubit preparation contextuality | Full text |
| J. J. Wallman, S. D. Bartlett, *Phys. Rev. A* 85, 062121 (2012) | Origin of the 8-state model | Not read; the model is used as LWE describe it |
| L. Catani, M. Leifer, D. Schmid, R. W. Spekkens, arXiv:2111.13727 | Epistricted mod-2 field theories are generalized-noncontextual | Not read in this unit; MR-1's reading (L752) |
| N. D. Mermin, *Phys. Rev. Lett.* 65, 3373 (1990); A. Peres (1991) | The name of the square in node 10. The operator identities used there were verified directly | Not read; cited for the construction's name only |

No literature result is a premise of nodes 1–3, 6 or 8. Those are self-contained
algebra over `F_2` and `Z_q`.

## 7. Verification scope

Every verdict rests on the paper arguments of §2. Exact author self-checks
(c1–c10) were run locally as controls on that algebra. They are not committed,
are not evidence, and carry no verdict. All are exact over `F_2`/`Z_q` with
`Fraction` arithmetic.

| Check | What it controls |
| --- | --- |
| c1 | Lemma G1, with three breaking controls |
| c2 | Lemma G2 on `n ≤ 3`, every graded affine `S` |
| c3 | Route U and the comparator; Route B (graded, `f_y = π_1 + π_2`) passes only with a same-sector dephasing bundled into each read, and fails Lemma G2's sequence with native reads |
| c4 | Route U's `H`, `T_1`/`T_2`, shared-parity signalling, generator closures |
| c5 | U′: `S`, group membership, comparator sequences up to length 4, Lemma Q under random protocols with two breaking controls, shared parity |
| c6 | U′: `H`, `T_1`/`T_2` |
| c7 | Composite `⟨YY⟩` |
| c8 | Affine offsets, all 256 pairs |
| c9 | Copy-only reads; the one-cell countercontrol |
| c10 | The word `L = Na ∘ C12` and the translation `τ` |

No Lean build, simulation campaign, manuscript edit, freeze, dispatch or merge
was performed. Independent review of this file is a separate step.
