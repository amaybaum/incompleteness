# REC-1 r1: independent non-author review

**Object.** Draft PR #1268, branch `research/rec-1-1169-20261113`, exact head
`d7f7aac1342932bdd125c7aa7c91647001fb1d68`; files
`verification/programmes/oi-qm/reconstruction/drafts/rec-1-20261113/REC-1.md` (333 lines) and
`REC-1-NOTES.md` (55 lines). The head adds only these two files on top of `main` `c3b5f37a`.

**Reviewer.** Fresh, non-author. Read-only, paper-only: no computation on OI rules, no Lean. Hand
checks only. Nothing committed, pushed, posted or dispatched.

**Governing records, fetched from the API and read in full:** #1169 c.6850732002 (owner
authorization, `amaybaum`, 2026-11-13T10:51:17Z), c.6848080209 (scope, 08:34:02Z), c.6848268369
(ChatGPT safeguards, 08:44:28Z); #1236 c.6847314661; #1143 body (2026-11-09 reformulation). REC-1's
quotations of all four comments are verbatim.

**Sources checked at their pins.** Every input blob in REC-1 §1 matches (`git rev-parse <commit>:<path>`):
Main `0db17597`, OA1 `5a16b213`, OA2 `8f8ddf73`, OA3 `0a36fd05`, W11 `8bf64629`, S3 `a9cbc675`,
S4 `17ca08f8`, M1D `7f8a142b`, M2D `9352d9da`, B4P `aff62906`, Q2A `7fd5aeda`, MR1 `321bc874`;
off `main`: 3A `7bbec04d` at `8228b3c2`, review `49a5d52a` at `8228b3c2`, OC1 `83188952` at
`77226128`. The three full ids in REC-1 name existing commits; the branch tips of
`research/tune1-step3a-1236-20261113` and `research/oicore1-record-20261109` are `8228b3c2…` and
`77226128…`. Pin facts verified: `2d064a71`, `62bdc2cf`, `080cd2be`, `c03a5764`, `1287748d`,
`9facdf03`, `c987b890`, `f810f5ee` are ancestors of `c3b5f37a`; `papers/Main.md` and
`drafts/tune-1-20261111/` are unchanged `080cd2be..c3b5f37a`; the OA reports differ
`2d064a71..c3b5f37a` only at OA2:65 and :958. All ten Lean line citations (`Equivalence.lean:245,
:294, :422, :462`; `GeneralCarrier.lean:93, :100, :160`; `PhysicalCharacterization.lean:301`;
`RankGapTheory.lean:702`; `StructuralClosure.lean:348`) land on the named theorem.

**Rows spot-checked against source (31 of 47):** 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
19, 20, 21, 22, 27, 28, 29, 33, 34, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, including every
[R-off] row (36, 37, 46, 47) and the non-obvious calls (5, 6, 12, 17/20/42 Q2-F, 30, 33). Q3 rows
C1–C18 all checked against their citations. Most citations are exact; the defects are listed below.

***

## Verdict: **REVISE**

The table is careful and most rows keep their proved scope. Four problems stop acceptance:

- **Q4 (main finding).** OBL-SP's "why open" paragraph cites only half of the reviewer remark it
  relies on (3A:613–617), omits the corpus statement on `main` that bears most directly on it
  (S3:196–207, TUNE-1 Node L5.4: under R-lin with a coset-uniform law and heralds on the prefix,
  "The restricted record theory is a classical simplex theory whose extreme points the labels
  translate"), and derives "(SP) fails whenever that subgroup is nontrivial" from a lemma stated
  only for unheralded record laws. On the reviewer's hand reading (below, unreviewed) the
  coset-space model may settle OBL-SP's main case at once, as O-C. "Open" holds as stated on
  `main`, but "smallest" and the claim that its answer separates classical, quantum and
  supra-quantum structure have not been examined against this (§A.19, §A.16, §A.31).
- **Row 5** classifies the finite-substratum obstruction as dynamics-intrinsic (Q1-D), but Main:558
  names its own interface assumption, and that factorization needs an independence condition on
  the initial law that inclusion does not supply.
- **C5** upgrades a source's *convention* to "follows from stated premises", and this conflicts
  with C6.
- **§3.2 step 4** presents two routes, MP-0a and MP-0b, as exhaustive. MP-0a itself leaves μ-G,
  and any non-uniform law would also give a φ-dependent statistic.

***

## Required changes

### RC-1 (Q4, central). Re-justify OBL-SP against S3:196–207 and the full 3A remark

*Finding.*
(a) Lemma A-T (c) (S3:56–98) is stated for the record law of a label sequence *without heralds*
(S3:107, Node L5.1: "without heralds"). OBL-SP's fragment includes heralded preparations (OA2:96–97;
OA3:396–397). The heralded case is S3 Node L5.4 (S3:196–207): conditional on a complete prefix
record the continuation law is uniform on `t_r + S₀` with one fixed subgroup `S₀`, and "The
restricted record theory is a classical simplex theory whose extreme points the labels
translate" (S3:206–207). REC-1 cites neither.
(b) 3A:613–617, which REC-1 cites for the (SP)-failure point, continues: "while a model on the
coset space might restore measurement noncontextuality. '(SP) open' may therefore resolve cheaply,
in either direction." REC-1 omits this half.
(c) Reviewer's hand sketch [W, reviewer; unreviewed; not used as a result]. Suppose every reachable
law of `Z₀` is a mixture of uniform laws on cosets of one finest subgroup `S_f`, each such coset
reachable as an extreme preparation, and each coset of `S_f` a function of the held record. Take
`Λ` = the reachable cosets, `μ_s` = the coset weights, and `ξ_(c,f)(t+S_f)` = the average of
`f(· + h(c))` over `t+S_f`. This model reproduces every statistic. It is preparation-noncontextual,
because coset indicators are effects, and measurement-noncontextual, because every reachable coset
is a vertex, so equivalent effects agree on `Λ`. It is then a simplex embedding without raw (SP).
Two cases fit these conditions:
- Unheralded preparations under `D_0`: each label sequence gives one coset of `S_m` (Lemma A-T (c)).
- Heralds on prefixes of one length (S3:198–201).

For prefixes of several lengths, the cosets refine as the prefix grows, which suggests the same
argument at the finest level. Any open content would then sit in:
- preparations whose heralds cannot be composed (held-at-use typing without retention, C6/C7);
- effects outside the record class.

This is a reviewer sketch, not a result. Its consequence for REC-1 is that "smallest open
obligation" and "separates classical, quantum and supra-quantum" are unexamined.

*Change.* Replace REC-1.md lines 243–246, from "Under laws of `D_0` the record laws are" through
"and this obligation does not rest on it.", with:

> For unheralded preparations under a law of `D_0`, each label sequence's record law is uniform on
> one coset of a label-independent subgroup `S_m` (Lemma A-T (c), S3:56–98, with `r_O` the
> designated values; S3:107). For heralds on a complete prefix, the continuation law is a mixture
> of uniform laws on cosets of one fixed subgroup `S₀` (S3:198–201), and S3:206–207 states that "The
> restricted record theory is a classical simplex theory whose extreme points the labels translate"
> [R]. Raw (SP) therefore fails whenever the relevant subgroup is nontrivial. A model on the coset
> space may still restore measurement noncontextuality, so that "(SP) open" may resolve cheaply in
> either direction (3A:613–617 [R-off], an unverified reviewer remark). OBL-SP's first step is that
> check (P0 below). If the coset model is a simplex embedding for the whole class, OBL-SP closes
> as O-C, and Q4 is re-run on the remaining items.

Add before P1:

> - P0. Cheapest decisive step: decide whether, for every instance in the class, the reachable laws
>   of `Z₀` are mixtures of uniform laws on the cosets of one subgroup, each coset reachable and
>   determined by the held record, so that the coset-space model is a simplex embedding. Record
>   which preparations, if any, fall outside that form, such as heralds that cannot be composed
>   under the fixed typing. Only those preparations carry OBL-SP's open content.

Rewrite "why smallest" accordingly. If P0's expected outcome is O-C, say so, state what the
obligation still separates, and compare it explicitly with AW-OA2-1 (non-additive observers). That
item needs no new physical premise either: H-AR is a restriction the Definition does not impose
(OA2:182–196), so dropping it removes a restriction and does not add one. Without this comparison,
"smallest" is not defended.

### RC-2 (Q4). Rival outcomes: vacuity, scope carried, finite horizons, non-exclusivity

(a) NOTES item 5 records that whether faithful records can be formed inside `S` under R-lin for
`D_0` laws "is part of the obligation". If no instance with records formed inside `S` exists, O-C
holds vacuously. Add before O-U:

> - O-V (vacuous): no instance of the class has a nontrivial prepare–measure fragment with records
>   formed inside `S` (P4(v)). Reported as such and not as O-C.

(b) Old: "O-C (classical): simplex-embeddable for every rule of the class, every law in `D_0`,
every H-AR observer and every horizon. Bearing: no boundary condition of the `D_0` form gives a
cell-aligned observer non-classical prepare–measure structure under the native rule;"
New: "O-C (classical): simplex-embeddable for every rule of the class, every law in `D_0`, every
H-AR observer and every finite horizon. Bearing: under (H3), the record class ((H4) or (V-ii-H)),
held-at-use herald typing with records formed inside `S`, and C-PM, no boundary condition of the
`D_0` form gives a cell-aligned observer non-classical prepare–measure structure under the native
rule;". In the list of remaining routes, add "other herald typings and record classes (C6, C7)".

(c) After O-SQ add: "O-Q and O-SQ are not exclusive; both are reported if both occur."

(d) Old: "(for example the dual-gbit shape of OA-2 N2.1, OA2:313–315)"
New: "(a candidate shape is the dual gbit of OA-2 N2.1, OA2:313–315, whose lack of a quantum model
in the sense of P2 is not established here)".
The source does not establish it. A qubit model fails by hand, but no record shows that every
finite dimension fails.

### RC-3 (Q4). Make P2 precise and give it controls; add a non-vacuity control

(a) P2's "preserving its operational equivalences" leaves open whether equivalent effects must map
to *equal operators*. If only statistics and preparation equivalences are preserved, a commuting
(diagonal) model realizes many classical-ontic fragments, and O-Q/O-SQ lose their meaning. Old:
"a finite-dimensional set of density operators and effects reproducing all statistics of the
fragment and preserving its operational equivalences."
New: "a finite-dimensional set of density operators and effects reproducing all statistics of the
fragment, with every operational equivalence of preparations mapped to equality of density
operators and every operational equivalence of effects mapped to equality of effect operators."
Alternatively, state another fixed reading and use it throughout.

(b) Add to P4:

> (v) non-vacuity: at least one instance of the class with records formed inside `S` and a
> nontrivial fragment is exhibited, or O-V is reported; (vi) P2's label is checked on a known
> quantum-realizable contextual fragment (labelled O-Q) and on a fragment with no quantum model
> under P2 (labelled O-SQ), both fixed before the attempt.

### RC-4 (§A.46 item 7). P3 inputs are [R] and need validation before use

Old: "P3. Inputs, each with its hypotheses carried:"
New: "P3. Inputs, each with its hypotheses carried, each re-derived or independently validated in
the unit before it is used as a premise (§A.46 item 7):".

### RC-5 (Q1, row 5). The finite-substratum obstruction is not interface-free

Main:558: "The factorization interface assumed is the ordinary preparation → finite ontic system →
measurement one". For an embedded observer the measurement choice is cell content. `B = ΞM` needs
the ontic law under preparation `p` to be independent of the measurement choice, which is a
(xiv)/H-μ-type condition on the initial law (C12). Inclusion does not give it: without it,
`M_{p,e}` may depend on `e`, and two ontic states reproduce any two-outcome table. 3A:263–266
defines inclusion only and does not state the factorization.
Old Class cell: "Q1-D".
New Class cell: "Q1-D + Q1-I + Q1-μ".
Old justification: "Premise: total finiteness (ledger (ii), Main:724) and the factorization of
every preparation and effect through the finite ontic state, which holds for any embedded interface
by inclusion (statement (i), 3A:263–266)."
New justification: "Dynamics: total finiteness (ledger (ii), Main:724). Interface: the ordinary
preparation → finite ontic system → measurement factorization, which Main:558 names as assumed.
μ: the ontic law of a preparation is independent of the measurement choice, a (xiv)-type condition
(C12) that inclusion does not supply. Main:558 extends the obstruction to finite shared
coordination ([55]); whether that covers every embedded correlation is not checked here." Update
NOTES item 4 to match.

### RC-6 (Q3, C5). Source says *convention*

OA1:112–113: "**Held** means a function of the present configuration `V_t`. That convention carries
D2's no-go (R1); MP-0b replaces it." "Follows from stated premises" is stronger than the source. It
also conflicts with C6 "undetermined": if C5 followed, MP-0b would be a departure from a stated
premise.
Old C5 status/reason: "follows from stated premises | The Definition (Main:42); OA1:112–114. Under
μ-G its consequence is §3.2."
New: "convention (OA1:112–113); the Definition (Main:42) is consistent with it [W, REC-1] but does
not fix it, and MP-0b is the alternative (C6) | Under μ-G its consequence is §3.2."
In the Answer to Q3, old: "interface from C4 and C5. It names no quantum object."
New: "interface from C4 and the convention C5. It names no quantum object."

### RC-7 (§3.2 step 4 and the Answer to Q3). The routes are not exhaustive as stated

Steps 1–2 are correct: the uniform marginal and the stationarity of the uniform law under any
bijection. They give a stronger statement: under μ-G with held-at-use typing, *no* held one-time
statistic of fixed functions depends on φ. A φ-dependent held statistic then needs to leave μ-G or
to leave held-at-use typing. MP-0a is one law outside μ-G, not a way of staying in it. Any
structured initial law (Main:58, Main:97) also leaves μ-G.
Replace step 4, from "So, under μ-G with held-at-use typing, a dynamics-dependent held statistic
needs" through "carries one of these two.", with:

> 4. So, under μ-G with held-at-use typing, no held one-time statistic of fixed functions depends on
>    φ. A φ-dependent held statistic needs either an initial or boundary law other than μ-G (MP-0a,
>    OA1:556–558, is the form the corpus names; any structured realization law, Main:58, :97, also
>    qualifies) or a typing other than held-at-use (the retention convention MP-0b, or heralds read
>    as ensemble conditionings, C7). Read as what an embedded observer holds at time `K` under μ-G
>    with held-at-use typing, the finite-horizon law `P(x_0, …, x_K)` of Main:546 presupposes one of
>    these.

Also:
- In step 1, after "any subsystem `W`", add "(a set of sites, ledger (viii))".
- In step 3, define `R` (OA-1 D8's record cells, OA1:211).
- In the Answer to Q3, old: "a dynamics-dependent operational theory needs C11 (μ) or C6 (interface)"
  New: "a dynamics-dependent operational theory needs a law other than C8 (C11 is the form named in
  the corpus; C9, C10 or another structured μ_H also qualifies) or a typing other than C5 (C6, or C7's
  ensemble reading) [W, REC-1; unreviewed]".

### RC-8 (row 12; OA-3 safeguard; §A.19). Scope the reconstruction point; do not oppose Main:26

Main:26 asserts that degrees of freedom "beyond causal reach are permanently hidden". That is a
cone statement, which C14 treats. Row 27's reconstruction covers sites *inside* causal reach on a
finite ring, so it is not a counterexample to Main:26. As written, row 12 also carries OA-3's result
without its observer class.
Old: "Per-moment inaccessibility follows from the Definition. Persistence over a horizon is not
derived: row 27 shows reconstruction within `2(L−3)` ticks for one rule family."
New: "Per-moment inaccessibility follows from the Definition. Persistence over a horizon of
influential hidden content is not derived from the Definition alone (Main:26's permanence concerns
degrees of freedom beyond causal reach, C14). For one rule family, on a finite ring, a held
three-site block with retained history reconstructs the ring within `2(L−3)` ticks (row 27, with
its hypotheses; OA-3 is not extended beyond those observers)."

### RC-9 (C14). Wrong ledger items and an ambiguous section reference

Main:724 says (x) is the nearest-neighbour range "which the cone of §3.3 does not require". The
cone uses (viii) and (ix). "§3.3" also reads as REC-1's own §3.3.
Old: "follows from stated premises (cone of §3.3 under (viii)–(x))"
New: "follows from stated premises (the causal cone of Main §3.3, under (viii) and (ix), Main:724)".
Old: "Lemma M (one-time pad, S4:94–101) gives masking only per tick and under the uniform law."
New: "Lemma M (one-time pad, S4:94–101) gives masking for one tick, given previous components
uniform and independent of the rest."

### RC-10 (§3.1 φ and C1). Translation is on the configuration, not on every observer's held record

D5 (i) concerns the map. For non-additive observers, settings translate the configuration but not
the held record (OA2:601–602, AW-OA2-1).
Old (§3.1): "The settings of such a rule act by translation,\n  for every measure and observer (row 13)."
New: "The settings of such a rule act on the configuration by translation, for every measure (row
13); held records are translated only for additive (H-AR) observers (OA2:601–602)."
C1, old: "Consequence: translation-only settings (row 13)."
New: "Consequence: settings act on the configuration by translation only (row 13)."

### RC-11 (row 33, C18). Carry NL-C's used premises

S4:451–456 lists what NL-C uses. Row 33 omits two of them:
- the declared target's separation length `L` with `K ≥ L + 1`, and Q6′(i) with its credit on `𝒯_L`;
- that an identified test's labels do not depend on the preparation's records (final B1.1, S4:456).

Append both to row 33's "Premises:". C18, old: "fails the one-qubit target at small ε (row 33)".
New: "fails Q6′(i) for TUNE-1's declared one-qubit target at every `ε < ε_C(c)`, for a menu bound `c`
uniform over the class (row 33)".

### RC-12 (Q2-F rows 6, 17, 20, 42). Annotate the dynamics' status; record the contrary reading

As defined, Q2-F holds for any fixed map. For designed maps, everything definable is reachable
(Main:582: "the same reversible machinery can realize non-quantum finite instrument families"), so
F collapses onto A unless the row states the map's standing. 3A:295–297 [R-off] reads row 6's
construction as "definable for every target, and nothing makes it the world's dynamics".
- Extend the Q2-F definition (line 87) with: "The row states the dynamics' standing: ledger class,
  proposal rule, or a map designed from the target."
- Prefix the justifications of rows 6, 17 and 20 with "Designed map." and of row 42 with "Proposal
  rule (`G_SM`)."
- Row 6: add "3A:295–297 [R-off] reads it as definable only (Q2-A)."
- In §6, list that use.

### RC-13 (§A.42 item 8). Classify each reference individually; state the landing condition

The §6 3A row's "Used where" column lists §3.1, C6 and C12, but its classification covers only rows
5, 7, 30, 33, C4, 36, 37 and the terms. The OC1 row does not classify the §4 last-paragraph use.
Item 8: "'Provenance only' is a finding about each reference, never a label applied to a group of
them."
- Classify 3A in §3.1 and in C6 as "support off `main`" for C6's "undetermined" status (it rests on
  OA-1 against 3A:501). C12's H-μ can cite TUNE-1's proposal on `main` (P:145, as 3A:496 does);
  re-cite it there and classify it as support on `main`.
- Classify OC1:359–363 in §4 as a premise named and not used (provenance), and say so.
- Add S3:196–207 (RC-1) as support on `main`.
- Add one sentence to §6: "This record does not land on `main` while any support off `main` remains;
  before landing, each such row is closed by landing its source or narrowed (§A.42 items 2, 8)."

### RC-14 (C3). Wrong line; FIX for interventions is an interpretation

"Smallest faithful strengthening" is at OC1:310 and :319, not :187. OC1:187 types FIX as "C (*interp.*
for interventions, N3)".
Old: "Main:44; OC1:187 [R-off] calls it the smallest faithful strengthening."
New: "Main:44 (composition of the evolution); for interventions an interpretation (OC1:187 [R-off]),
which OC1:310, :319 calls the smallest faithful strengthening."

### RC-15 (accuracy; process leakage)

- NOTES line 55, old: "#1236. Nothing has been committed, pushed or posted."
  New: "#1236. The draft is on PR #1268; this review is r1."
- REC-1.md line 35: delete " (worktree `wt-rec1`)". A local worktree name is not resolvable from
  `main` (§A.42 item 2).

### RC-16 (§5 item 1). Carry OBL-SP's scope into the tier rationale

Old: "(its outcome decides whether the native rule class can host non-classical prepare–measure
structure for cell-aligned observers, which conditions the foundational OI→QM question)"
New: "(its outcome decides, for H-AR observers, `D_0` laws, the record class and herald typing
stated in §4, whether the native rule class can host non-classical prepare–measure structure; P0
may settle it cheaply (§4))". If P0 is expected to give O-C, reconsider "high".

***

## Items checked and found correct (no change)

- **Safeguard 1, NL-C.** Row 33 and C18 classify NL-C by its per-round bounded-cell label-menu form,
  covering designated and emergent controls alike (S4:423–475, :697–698). The listed outside cases
  are those 3A:433–439 records. Correct (apart from RC-11).
- **Safeguard 1, OA-3.** Rows 27 and 28 are scoped to finite-ring held-block observers, with
  OA3:383–391 cited. Only row 12 leaks (RC-8).
- **Safeguard 2.** The Q2-A/F/P split is applied consistently, and no row is Q2-P. C-rows each name
  φ, μ, embedding or interface and a premise status.
- **[R] use.** OA-1/2/3 and W1-1 are tagged [R] throughout and not used as established premises,
  except that P3 needs the RC-4 clause.
- **§A.34.** Rows 1–3 keep the three implications separate with their own kernel witnesses. Row 7
  cites necessity and sufficiency separately. Row 41 is stated one-way. B4′/Q2A/M-1 keep G⇒O and
  O⇒G apart.
- **Q4 gate.** OBL-SP adopts no physical premise: φ comes from the ledger, and `D_0` is quantified
  over, not selected (Main:58, :97). H-AR, the record class and herald typing are scope hypotheses.
  The criterion (simplex-embeddability) is target-neutral, and quantum realizability enters only as
  a label. "Open" is correct on `main` (OA2:779; OA3:494, :633), subject to RC-1. Controls P4(i),
  (ii) and (iv) are non-vacuous (preservation, countercontrol, out-of-class positive). P4(iii) is a
  scope check, not a control.
- **Register (§A.32/§A.33).** No meta-commentary, caps emphasis or revision-history voice found.
  Caps tokens are identifiers or OA classification vocabulary.
- **§5.** Every item is labelled a proposal. "Authorization: not authorized" is stated, and nothing
  is applied.

## Optional suggestions

1. Row 27: add "with `v_a(0)`; `2(L−2)` without it (OA3:228–232)".
2. Row 3: "The three directions" → "The three implications of the cycle S⇒D⇒Q_fb⇒S".
3. C16: add OC1:258's draft-conditional note that one ACC-U instance (ARP-3 F0) is classically
   imitable.
4. Row 22: OA-2 labels Corollary E1 "[W]" only; drop "+ [RW]" unless a source supports it.
5. NOTES "Not read": add S3:196–229 once read for RC-1.
6. R-lin on a finite ring is permutive in its extreme argument, so Lemma OBS's (★) mechanism may
   make `S₀` trivial there at horizons of order `2L` (AW-OA3-1), in which case (SP) holds and E(b)
   applies directly. This is worth one line in P0's scope note, scoped to finite rings and not
   carried to cubic-lattice observers.
