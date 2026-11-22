# RECON-INF P2-C Node 2: execution packet (proposal)

**Status.** A proposal for an owner decision. It runs nothing, freezes nothing and authorizes
nothing. Node 2 is not authorized. The reference rule set, its per-rule lists and the `Φ_{q,α}`
readout-map lists named below are proposals of what Node 2's freezing amendment would contain and
how it would be made; none of them is frozen by this file. `DESIGN.md` and `NODE-1.md` are not
edited.

**Goal link (§A.47).** RECON-INF (#1531) → P2-C (#1535). Node 2 decides whether lattice realization
without the Stage 2 constraints (J1⁰, J1) is vacuous, and freezes the comparison set that every later
specificity question uses. It decides no part of Q (J2) or Q⁺ (J3); what it would decide for them is
which positive outcomes of Nodes 4–5 can be credited as specific to the Stage 2 dynamics.

**Authorization of this packet.** Owner decision on #1169,
[comment 7075274142](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7075274142)
(`amaybaum`, 2026-11-22T06:20:58Z), workstream "P2-C Node 2 packet": "Prepare the execution packet
only, as for Node 1: scope, pins, the decision rule from the accepted design, the freezing of the
reference rule set and its per-rule lists, the cost class, and the writer and reviewer." Excluded:
"Running Node 2; changing `DESIGN.md`". Conditions recorded there: its own branch, writer, draft PR
and an independent reviewer in a separate session; no change to accepted designs; no automatic
successor tasks, and no merges.

## 1. Pins

| Object | Pin | Standing |
|---|---|---|
| Design | `verification/audits/foundations/recon-inf-p2c-20261121/DESIGN.md` at `d1f39ce886c69c0d5bf3dd566f30c55285d0a4c6` (branch `research/recon-inf-p2c-20261121`, PR #1535) | Accepted as a reviewed plan, #1169 c.7069340219, with the condition "Keep the nonempty J1 reference requirement and the full-domain exclusion certificates" |
| Node 1 | `verification/audits/foundations/recon-inf-p2c-20261121/NODE-1.md` at `08626aa270da27df0f369dece9bb09560aa1c17f` (branch `research/recon-inf-p2c-n1-20261122`, PR #1538) | Accepted, #1169 c.7074721954: definitions, counting analysis, Lemmas R and P under their stated assumptions; M1–M8 and D1–D5 stay open |
| Corpus | `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed` (the design's pin B1) | `Sub:n`, `Main:n`, `SM:n` are lines of `papers/Substratum.md`, `papers/Main.md`, `papers/SM.md` there |
| Model of form | The Node 1 packet, #1535 c.7074070661 | — |

**Corpus check against current `main` (`53c6601a10419b6b333cc992474272501ab542af`).** `df6da1c6` is an
ancestor of `53c6601a`. `git diff df6da1c6 53c6601a -- papers` is empty, so every paper line the
design, Node 1 and this packet cite is unchanged. `book/` is not unchanged: commit `98e55009`
("THM24 prior hypothesis P2") edits `book/ch02-substratum.md`:140 and its mirror
`book/The-Incompleteness-of-Observation-FULL.md`:770 (Theorem (Generators) (i), hidden-state
relabelling, now stated for a finite hidden set with the uniform hidden prior) and regenerates the
book `.tex`. The design, Node 1 and Node 2's reading list cite no book line, so the pin `df6da1c6`
stands for Node 2. The Node 2 writer repeats this check at the head current when Node 2 starts and
records the result.

## 2. Node 2 as the design states it (quoted unchanged, design §4)

> ### Node 2 — Is lattice realization without the Stage 2 constraints vacuous? (J1⁰, J1)
>
> - **Hypothesis under test.** Every finite-horizon law is J1⁰-realizable by a construction that carries
>   no Stage 2 content, so J1⁰ cannot by itself identify the systems.
> - **Check.** Paper construction, one per class: (a) J1⁰: a range-0 rule acting as `φ` on a site
>   alphabet `C_V × C_H`, identity elsewhere; (b) J1: the same question inside A2–A4, including A4's
>   no-self-input clause (Sub:98), for example a second-order rule `x(t+1) = F(x(t)) − x(t−1)` with a
>   non-linear `F` (reversible for every `F`, SM:106) whose hidden coordinates feed a window like a
>   tape. Each construction is checked against the classes of §2.3 and against L1, L6, L7.
> - **Decision rule.** If a construction realizes every target of a class exactly inside a given set
>   of premises, the relation at that premise set is recorded as uninformative for Q, and Q is carried
>   by the next stronger relation. If no construction is found inside A2–A4, J1 is carried as Missing
>   and the obstruction found, if any, is recorded at its scope. The rules used here form the
>   **reference rule set**: a finite list frozen by additive amendment before Node 4 opens and before
>   any outcome is evaluated, and used unchanged for every later specificity question. Membership
>   criterion: each listed rule is a J1 rule (reversible, finite-range, translation-invariant,
>   centre-free under A4's no-self-input clause) outside the `Φ_{q,α}` family and carrying no Stage 2
>   content, with a stated reason for its inclusion. Node 2's universal construction is included
>   wherever Node 2 finds one. The comparison set must contain at least one genuine J1 member,
>   including Node 2's case (b) tape construction, which is always listed; a reference rule set
>   containing only the range-0 rule cannot establish J1 specificity. **Domain correspondence.** The
>   freezing amendment fixes, for each reference rule, the readout-map and preparation lists that
>   correspond to those of each positive that may be tested against it: the same readout and
>   preparation classes, the same window size and the same number of readout values, with the explicit
>   correspondence of maps where the site alphabet differs from `ℤ_q × ℤ_q`. The readout-map lists for
>   `Φ_{q,α}` (Nodes 4–5) are frozen in the same amendment, together with the reference set and these
>   lists, before any outcome is evaluated; a readout map added later has no frozen counterpart, so a
>   positive that uses it cannot be credited as specific. These lists are frozen before any outcome is
>   evaluated; a different site alphabet does not allow the comparison to be changed after the fact.
>   If the range-0 rule is kept in the set, it is listed as a J1⁰ member outside the membership
>   criterion, because it violates A4's no-self-input clause. A positive realized only by the range-0
>   rule is recorded as generic over J1⁰ and is decided by the J1 members: it is credited as specific
>   only if every J1 member of the reference rule set is excluded, each by its own exact dual or
>   Farkas certificate matching the positive result's full domain: the same target, the same exactness
>   or ε-tolerance, the same measurement settings (Stage 1's experimental context, that is the fixed
>   basis and the unitary between readings, which the same-target clause already fixes; and the time
>   map `m` range and setting (F) or (Z)), the same torus conditions (side and wrapping conditions on
>   `P`), the same readout classes and the same preparations, as given by the readout and preparation
>   lists frozen for that rule in Node 2, and the same window and the same horizon (a thinner domain
>   does not count), as in §4's common rule.
> - **Countercontrol.** The range-0 construction is the vacuity witness: any identification criterion
>   that it satisfies is too weak to answer Q and is not used. Applied at freeze to J5(T), which it
>   satisfies (§2.4).

The common rules of design §4 bind Node 2 unchanged, in particular the specificity question
(the reference-set requirements: at least one genuine J1 member including Node 2's tape
construction; per-rule readout and preparation lists frozen before any outcome is evaluated;
exclusion certificates matching the positive result's full domain; the `Φ_{q,α}` readout-map lists
frozen with the reference set), design §5's stop conditions and design §7's invariants I5, I12 and
I13. Node 2 does not count toward S1 (design §5).

## 3. Proposed procedure

Node 2 would run in this order, depth-first, each step closed before the next opens.

1. **Literature (design §3, rows L1, L6, L7).** Run the three queries the design assigns to Node 2
   and record each per design §3: source, exact statement, hypotheses, and whether it decides the
   node, bears on it, or shows it known hard; null results included. A query that decides a case is
   applied at the cited theorem's scope, with its hypotheses checked against the classes of design
   §2.3 and Node 1 §1, before any construction for that case is written.
2. **Case (a), J1⁰.** Write the range-0 construction (§4.2 below) and decide, per readout class,
   preparation class, target class and exactness of design §2.3, whether it realizes every target of
   the class exactly. Paper proof only; it may cite J0-ind and J0-joint (Main:526–528; `S_imp_D`) as
   Node 1 §5.1–5.2 states them.
3. **Case (b), J1.** Write the tape construction (§4.3) and, where one is found, the universal
   construction (§4.4). For each, check membership (§4.1, with the membership controls of §7), then
   decide, per class as in step 2, whether it realizes every target exactly. If no construction is
   found inside A2–A4, J1 is carried as Missing and any obstruction found is recorded at its scope
   (design Node 2 decision rule).
4. **Verdicts.** Apply the design's decision rule per premise set: a relation realized for every
   target of a class is recorded as uninformative for Q at that class, and Q is carried by the next
   stronger relation. Apply the countercontrol (design I12) to every identification criterion the
   record uses.
5. **Freezing amendment.** Write the amendment of §4 and §5 below as one additive commit, before
   Node 4 opens and before any per-target outcome is evaluated (owner decision OD6 on what "outcome"
   covers). It is reviewed at its exact head and accepted by the owner; its accepted SHA is the one
   every later node cites (design I5).

Node 2 evaluates no realizability question for any individual target of the families Nodes 4–5 will
list (design Node 4a "Target families"), for `Φ_{q,α}` or for any reference rule. Its verdicts are
class-level paper results.

## 4. Proposed content of the freezing amendment: the reference rule set

### 4.1 Membership criterion

The design's criterion: "each listed rule is a J1 rule (reversible, finite-range,
translation-invariant, centre-free under A4's no-self-input clause) outside the `Φ_{q,α}` family and
carrying no Stage 2 content, with a stated reason for its inclusion." Proposed operational reading,
each clause with the witness the amendment records for each listed rule:

| Clause | Proposed reading | Witness recorded per rule |
|---|---|---|
| Reversible (A2) | The one-step rule `F` is a bijection of `Ω` | Explicit inverse; for the second-order form `x(t+1) = f(x(t)) − x(t−1)` it is `x(t−1) = f(x(t)) − x(t+1)` (SM:106) |
| Finite range (A3) | Each output coordinate depends on inputs within a fixed graph distance `r_F`; bounded degree | `r_F` and the read set stated |
| Inverse finite range | Per D5, §6 | `r_{F^{-1}}` stated; for the second-order form it equals `r_F` |
| Translation invariance (A4, first sense) | Commutes with the translations of `ℤ³`, or of `ℤ³/P_lat`, exactly | By the form; a rule commuting only up to site-wise gauge is listed only with OD2 decided |
| No self-input (A4, second sense) | The second-order form with `f_i` not depending on `x_i(t)` (Node 1 §5.4; SM:228) | By the form. A rule not of second-order form needs D3 decided first (OD8) |
| Lattice and torus conditions | `d = 3`; on (F), `P_lat` with every nonzero vector of ℓ¹-norm at least 3 (Node 1 §1) | Stated; the design's specificity rule compares on the same torus conditions |
| Outside the `Φ_{q,α}` family | Not equal to `Φ_{q,α}` for any `q, α`; proposed also: not conjugate to one by a site-wise gauge (OD2) | A gauge-invariant distinguishing property. Sub:98 records that a site-wise gauge "preserves which sites each update reads", so a read set different from the six nearest neighbours (and nonempty, which excludes `Φ_{q,0}`) is a paper witness |
| No Stage 2 content | Proposed (OD1): the rule fails at least one premise that, beyond A2–A4, singles out `Φ_{q,α}` within the second-order form: linearity (A5, Sub:100), spatial isotropy (E4, used in SM:228's uniqueness proof) or the nearest-neighbour premise. The alternative reading fails all of them | The premise failed, stated with its counterexample configuration or coefficient |
| Reason for inclusion | Stated per rule | — |

**Site alphabet (proposal, OD10).** Every J1 member of the tape kind is a second-order rule over
`ℤ_q` per site, so its window phase group is `G_W = (ℤ_q²)^W`, the same group as for `Φ_{q,α}`
(Node 1 §1). The domain correspondence for such a rule is then the identity on readout maps and on
preparations, and no correspondence is chosen after an outcome. A rule on a different site alphabet
(the universal construction may need one) takes the correspondence of §5.3.

### 4.2 The range-0 rule, labelled J1⁰

Listed as the design requires, **outside the membership criterion**, because it violates A4's
no-self-input clause (and, in its single-active-site form, translation invariance). Content:

- **R0 (single active site).** Site alphabet `C_V × C_H`; `F` acts as a bijection `φ` at one site
  and as the identity elsewhere (design Node 2 (a)); `φ` the bijection of a J0 realization of the
  target. It is a schema indexed by the target, not one rule; this is admissible for R0 alone,
  since the design requires no certificate for the range-0 rule and decides a positive realized
  only by it through the J1 members.
- **R0-ti (translation-invariant variant).** The same bijection at every site (Node 1 §5.3, reading
  note (a)); also J1⁰, also outside the criterion.
- **Role.** The vacuity witness of the countercontrol (design Node 2; I12), and the comparison rule
  of Node 4b's test (ii′) and Node 5c's test (ii) "with the window's own coordinates".

### 4.3 The tape construction (case (b), always listed)

The design: "a second-order rule `x(t+1) = F(x(t)) − x(t−1)` with a non-linear `F` (reversible for
every `F`, SM:106) whose hidden coordinates feed a window like a tape." Node 2 constructs it; this
packet fixes the acceptance conditions and records two candidate families.

**Packet-level observation (unreviewed; to be checked by Node 2).** For the one-dimensional
second-order form `x_i(t+1) = f(x_{i−1}(t), x_{i+1}(t)) − x_i(t−1)` over `ℤ_q`, every right-moving
profile `x_i(t) = a(i − t)` is a solution if and only if `f(u, w) = u + w` for every pair `(u, w)`:
with `s = i − t` the equation reads `a(s − 1) = f(a(s − 1), a(s + 1)) − a(s + 1)`, and an arbitrary
sequence `a` takes every pair `(a(s − 1), a(s + 1))`. The same holds for left movers. A tape that
carries arbitrary hidden data through the read pair is therefore linear on that pair; a non-linear
tape must restrict its data or place its non-linearity on coordinates the tape does not carry.

**Candidate families** (Node 2 selects and proves; the list is not frozen here):

- **T-lin (anisotropic d'Alembert tape).** `x_i(t+1) = x_{i−e₁}(t) + x_{i+e₁}(t) − x_i(t−1)` over `ℤ_q`
  on `ℤ³`: one-dimensional discrete wave equations along `e₁`, uncoupled across `e₂, e₃`. It
  satisfies A2–A4 by its form, is linear (A5) and nearest-neighbour, and fails spatial isotropy; its
  read set `{i ± e₁}` differs from that of every `Φ_{q,α}` with `α ≠ 0` and is nonempty. It is
  admissible under OD1's weaker reading only.
- **T-nl (non-linear tape).** A second-order rule over `ℤ_q` whose `f` is non-linear, built per the
  observation above (for example a linear transport pair along `e₁` with a non-linear term read from
  a transverse neighbour that the transport does not carry). It is admissible under both readings
  of OD1 if it fails linearity and is not gauge-conjugate to a `Φ_{q,α}`.

Whether the always-listed tape must be non-linear, as the design's example is, or may be T-lin, is
owner decision OD3. Proposal: list T-nl if Node 2 constructs one that meets §4.1, and list T-lin as
well if OD1 admits it; a rule is listed whether or not it realizes every target of a class, since
listing records a comparison rule, not a vacuity verdict.

### 4.4 The universal construction, where found

Listed if Node 2 finds a J1 construction that realizes every target of some class exactly (design:
"included wherever Node 2 finds one"). Starting points are L1 (intrinsic universality of reversible
CA; block and partitioned representations) and L7 (embeddings of finite reversible systems). Such
constructions are commonly stated in block or partitioned form rather than the second-order form;
A4's no-self-input clause is then undefined until D3 is decided (OD8), and the rule cannot be listed
as a J1 member before that. A universal construction whose site alphabet differs from `ℤ_q²` per
phase site takes the correspondence of §5.3.

### 4.5 Finiteness and form of the list

The frozen set is a finite list `𝓡 = {R0, R0-ti} ∪ 𝓡_J1`, `𝓡_J1` the genuine J1 members, each named
by `(q, d = 3, read set, f, r_F, r_{F^{-1}})` with its §4.1 table. Where a rule is a family indexed
by `q`, it is listed once per `q` of the grid of §5.1. **Requirement checked at freeze:** `𝓡_J1` is
nonempty and contains the tape construction (design Node 2; the owner's acceptance condition at
c.7069340219). If it cannot be met, Node 2 stops (S-N2a, §8) and the freeze is not made.

## 5. Proposed content of the freezing amendment: readout, preparation and `Φ_{q,α}` lists

### 5.1 The grid

A readout-map list is defined per `(q, W)`. The amendment fixes a finite grid `𝒢` of pairs
`(q, W)`; for `Φ_{q,α}` and for every rule of `𝓡_J1` the lists below are frozen on `𝒢`. A Node 4 or 5
run at a `(q, W)` outside `𝒢` has no frozen counterpart, and its positives cannot be credited as
specific (design common rules). Proposal (OD4): `q ∈ {2, 3}`; `W` one site, or two sites adjacent
along `e₁`. The grid fixes the readout lists only; `α`, `m_max`, the torus side and the targets remain
choices of the Node 4–5 amendments, and a specificity comparison uses the positive's own values of
them.

### 5.2 Readout-map lists (one list per `(q, W)`, shared by `Φ_{q,α}` and every `ℤ_q` reference rule)

| Class | Proposed list `𝓜(q, W)` | Size at `w = |W|` |
|---|---|---|
| (R-coord) | Every nonempty coordinate set `X_V` of the `2w` phase coordinates of `W` | `2^{2w} − 1` |
| (R-lin) | Every pair `(ker h, K')` with `ker h` a proper subgroup of `G_W` having a complement and `K'` a recorded complement (`h` determined by `ker h` up to an automorphism of its image, which the free injective labelling `ι` absorbs); a change of `K'` is a separate entry (design §2.3) | Finite; enumerated in the amendment by rule, with its count |
| (R-nl) | For `q^{2w} ≤ 9`: every partition of `G_W` into at least two blocks (a map `g` up to relabelling of values, which `ι` absorbs). For larger `G_W`: a named finite subfamily stated in the amendment (OD4) | `w = 1`: the partitions of 4 (`q = 2`) or 9 (`q = 3`) points |

The `Φ_{q,α}` readout-map lists the design requires (design Node 2, "Domain correspondence"; I5)
are these same lists, frozen in the same commit. Because the `ℤ_q` reference rules share `G_W`, the
correspondence of maps between `Φ_{q,α}` and each of them is the identity.

### 5.3 Correspondence for a rule on a different site alphabet

For a listed rule whose window phase group `G'_W` differs from `G_W`: its list is, for each map of
`𝓜(q, W)` in a class with `k` values, every map of the same class on `G'_W` over the same window
sites with `k` values, enumerated in the amendment. This gives the reference rule at least the
freedom the design's "free within the lists" requires, makes a "generic" record no harder to reach
and a "specific" credit no easier, and is fixed before any outcome. Alternative forms (a single
named map per `Φ` map) are OD10.

### 5.4 Preparation lists (per rule, per readout map)

For each rule and each map of its list, the admitted preparation classes are those of design §2.3,
in Node 1 §1's form: (Π-H) and (Π-prod) under (R-coord) and (R-lin) with the split of the map;
(Π-β), (Π-W), (Π-W,β) and (Π-joint) under every class. `β` is the uniform (counting) law on (F) and
the uniform Bernoulli law on (Z) for every rule over the same site alphabet, so the classes are the
same sets of laws for `Φ_{q,α}` and for the `ℤ_q` reference rules. **(Π-β) event list.** A cylinder
event is specified by its site–time–value set and is evaluated with the dynamics of the rule under
test. Proposal (OD5): the amendment fixes a finite list of event specifications, with time set
`T_E ⊂ {0}` (an apparatus record at preparation time, so the event is a cylinder of the initial
configuration and identical for every rule). A wider time set needs D1 decided first (Node 1 §6;
D1 is first needed by Node 3).

## 6. D5 inside Node 2 (proposal; the owner or reviewer decides)

D5 (Node 1 §6): the design does not fix whether `F^{-1}` must have finite range in J1⁰.

- **Where it does not bite.** Every rule this packet proposes to list has a finite-range inverse by
  explicit formula: R0 and R0-ti have range-0 inverses; every second-order rule has
  `r_{F^{-1}} = r_F` (§4.1). A vacuity verdict is an existence statement; proved with witnesses whose
  inverses have finite range, it holds under both readings. The freeze is the same under both.
- **Where it bites.** A negative ("no construction found") or an obstruction is stated under the
  reading it was proved for, and the weaker reading (no inverse requirement) is the larger class. On
  (Z), for translation-invariant rules on a full shift, the inverse of a bijective cellular automaton
  is again a cellular automaton (L1, Hedlund 1969: to be checked by Node 2 against the exact
  statement and hypotheses), so D5 is empty there; it is substantive only for J1⁰ rules that are not
  translation-invariant on (Z). On (F) every bijection has range bounded by the torus diameter, and
  the reading needed is a range bound uniform in the torus size.
- **Proposal.** Node 2 adopts "`F^{-1}` of finite range" (on (F): uniform in the torus size) as the
  working reading, states for each verdict whether it holds under both readings, and routes D5 to
  the owner under S2 only if a verdict differs between them.

D3 bears on Node 2 only through OD8. D1 bears only through the (Π-β) event list (OD5). D2 and D4 are
not needed by Node 2.

## 7. Controls and countercontrols

| Control | Content | Pass condition |
|---|---|---|
| Vacuity countercontrol (design Node 2; I12) | Apply each identification criterion the record uses to R0 | A criterion R0 satisfies is not used to answer Q; recorded for J5(T) at freeze, and stated for J1⁰ and J1 |
| Membership detector, positive side | Apply §4.1 to `Φ_{q,α}` itself | It is rejected ("outside the `Φ_{q,α}` family" fails); otherwise the criterion is void (S3) |
| Membership detector, self-input | Apply §4.1 to Sub:98's rule `x_i(t+1) = x_i(t) + Σ_{j∼i} x_j(t) − x_i(t−1)` | Rejected for reading `x_i(t)` |
| Membership detector, gauge (if OD2 adopts it) | Apply §4.1 to a site-wise gauge conjugate of `Φ_{q,α}` | Rejected; the read-set witness or another gauge invariant shows it |
| Membership of R0 | Apply §4.1 to R0 and R0-ti | Rejected from J1 and listed as J1⁰ only |
| Non-emptiness | Count `𝓡_J1` and check the tape construction is in it | At least one member, the tape construction among them |
| Freeze-before-outcome | The amendment commit precedes every record of a per-target outcome in P2-C | Checked by the reviewer on the branch history and the record text (§10, row N2-5) |
| List identity | The `Φ_{q,α}` lists and the `ℤ_q` reference lists are one list per `(q, W)` | Checked in the amendment |

Each control's result is printed before the verdict it guards (design I6); a verdict above a failed
control is void.

## 8. Stop conditions

Design S2, S3, S4 and S6 apply; S1 does not (design §5). In addition:

- **S-N2a.** The freeze cannot meet §4.5's requirement (no genuine J1 member, or no tape
  construction meeting §4.1): Node 2 records the verdicts it has, makes no freeze, and stops. Node 4
  cannot open without a freeze, so this is routed to the owner.
- **S-N2b.** A step needs a definitional choice listed in §11 that is not yet decided: the step stops
  and the choice is routed under S2, with the alternatives and their consequences.
- **S-N2c.** A step needs computation: it is recorded as "Missing (needs computation)" and stops there,
  as in Node 1. It does not escalate.
- **S-N2d.** Any per-target outcome is evaluated before the freeze: the freeze is void for the lists
  that outcome bears on, and Node 2 stops for an owner decision.
- **S-N2e.** A listed rule fails a membership clause after it was proposed: it is removed before the
  freeze; once the freeze is accepted no rule or list is added, removed or changed (design I5).

## 9. Computation and cost class (§A.40)

**No computation.** Node 2 as proposed is reading, the literature queries L1, L6 and L7, and paper
derivation. Bijectivity, the inverse, the range and the gauge non-membership of every proposed rule
follow from its form (§4.1, §7). Cost class: no compute; nothing runs locally or in CI.

If Node 2 records "Missing (needs computation)" for a step, a later packet would estimate it and
classify it under §A.40 before any run, and the run would need its own authorization. Such a check
must evaluate no target law (S-N2d). An exhaustive check over `Ω` on a side-3 torus in `d = 3` is not
a bounded local task (`|Ω| = q^{54}`), so any such check would be symbolic or restricted to a stated
sub-problem; a larger one is planned for CI (§A.40).

## 10. Invariant → checkpoint table for Node 2's execution (§A.41)

| # | Invariant | Checkpoint |
|---|---|---|
| N2-1 | `DESIGN.md`, `NODE-1.md` and this packet are unchanged | `git diff <base> HEAD` on the three paths is empty, checked before each push |
| N2-2 | Node 2 adds only its record and its freezing amendment | `git diff --stat <base>...HEAD` lists only the two files of §12 |
| N2-3 | No code or data file is added; no computation is run | The diff above; the record states that no command beyond `git` and reading was run |
| N2-4 | Every corpus citation reads as cited at the pin | Each `file:line` re-read at `df6da1c6`; the reviewer re-reads a sample |
| N2-5 | The freeze precedes every per-target outcome | The amendment is one commit; no earlier commit of the branch, and no part of `NODE-2.md`, contains a realizability statement for an individual target |
| N2-6 | Every listed J1 member meets §4.1 with recorded witnesses; `𝓡_J1` is nonempty and contains the tape construction | The §4.1 table filled per rule; the count printed |
| N2-7 | R0 and R0-ti are labelled J1⁰ and outside the criterion | Checked in the amendment |
| N2-8 | The membership controls of §7 pass before the freeze | The control table precedes the list in the amendment |
| N2-9 | Repository-text constraints | A grep of the added lines for the excluded vocabulary and for local paths returns nothing |
| N2-10 | No equivalence is displayed without a witness per direction (§A.34) | The packet-level observation of §4.3 is the only biconditional here; Node 2 proves each direction separately or states the direction it proves |

## 11. Points needing an owner decision

None is settled by this packet. Each is stated with the proposal; the owner, or the reviewer where
the owner delegates it, decides.

- **OD1. "No Stage 2 content."** Proposal: the rule fails at least one of linearity (A5), spatial
  isotropy (E4) or the nearest-neighbour premise. Alternative: it fails all three. The weaker
  reading admits T-lin; the stronger admits only non-linear rules.
- **OD2. "Outside the `Φ_{q,α}` family" modulo site-wise gauge.** Proposal: yes, with a gauge-invariant
  witness (the read set, Sub:98). Without it, a gauge conjugate of `Φ_{q,α}` could enter the reference
  set and make positives "generic" spuriously.
- **OD3. Must the always-listed tape be non-linear?** The design's example is non-linear; the
  observation of §4.3 shows that a free tape on its read pair is linear there. Proposal: T-nl
  required if constructed; T-lin listed in addition under OD1's weaker reading.
- **OD4. The grid `𝒢` and the (R-nl) list form.** Proposal: `q ∈ {2, 3}`, `W` one site or two sites along
  `e₁`; (R-nl) all partitions for `q^{2w} ≤ 9`, a named subfamily above. Consequence: a Node 4–5 run
  outside `𝒢` has no frozen counterpart and cannot be credited as specific.
- **OD5. (Π-β) events.** Proposal: a finite list with `T_E ⊂ {0}`. A wider time set waits for D1.
- **OD6. What "before any outcome is evaluated" covers.** Proposal: every per-target realizability
  outcome, for `Φ_{q,α}` or a reference rule, in any node. Node 2's class-level paper verdicts precede
  the freeze, which the design's "Node 2's universal construction is included wherever Node 2 finds
  one" requires. Alternative: freeze the rule list before Node 2's verdicts, admitting the universal
  construction only if found before the freeze.
- **OD7. D5.** Proposal of §6: adopt "`F^{-1}` of finite range" as the working reading and route only
  if a verdict differs.
- **OD8. D3 for a universal construction outside the second-order form.** Proposal: such a rule is
  not listed as J1 until the owner fixes the no-self-input reading for its form.
- **OD9. Computation.** Proposal: none authorized for Node 2; any need is recorded as Missing.
- **OD10. Site alphabet and correspondence.** Proposal: tape-kind members over `ℤ_q` with the identity
  correspondence; a rule on a different alphabet takes §5.3's all-maps-with-the-same-count list.
- **OD11. Branch base.** Proposal: Node 2's branch is cut from the accepted head of this packet's
  branch, which descends from `08626aa2` and so contains `DESIGN.md`, `NODE-1.md` and this packet.

## 12. Writer, reviewer and record location

- **Writer.** One fresh agent, not the writer of this packet.
- **Reviewer.** An independent exact-head review by a separate session, never the writer, of both the
  record and the freezing amendment, before the owner accepts either. The freeze counts only at the
  SHA the owner accepts after that review (design I5).
- **Record.** New branch `research/recon-inf-p2c-n2-20261122` (base per OD11), carrying two new files
  in the round directory `verification/audits/foundations/recon-inf-p2c-20261121/`:
  `NODE-2.md` (the literature record, the constructions, the controls and the verdicts) and
  `amendments/NODE-2-REFERENCE-SET.md` (the freezing amendment of §4 and §5, in its own commit). A
  draft PR linked to #1531, #1535 and #1538. `DESIGN.md` and `NODE-1.md` are not edited.

## 13. Requested authorization

Execute P2-C Node 2 as the design states it, by the procedure of §3, with the freezing amendment of
§4 and §5 as decided under §11, paper-only, by the writer and reviewer of §12, into the record
location of §12.

This request grants nothing by itself. It would not authorize Nodes 3–9, any computation, any
change to `DESIGN.md` or `NODE-1.md`, any manuscript or Lean change, or any merge. The decisions of
§11 are needed before the freeze is made.
