# Confirmation review of GATE-A-AMEND-r2.md (with GATE-A-AMEND-r2-TRACE.md and RESPONSE-r1.md)

Non-author confirmation review of r2 against `REVIEW-r1.md`. The review was paper-only: reading,
grep and hand reasoning. Nothing was computed on OI models, no Lean was built, and nothing in the
repository or on GitHub was edited or posted.

`r2:n` refers to line n of `GATE-A-AMEND-r2.md`, `TR` to `GATE-A-AMEND-r2-TRACE.md`, and `EP:n` to
line n of `endpoints.md`, blob `d9d92e03`, on `main` at `c3b5f37a`.

**Verdict: ACCEPT WITH CHANGES.** Every disposition of REVIEW-r1 is applied as RESPONSE-r1
describes. The trace is complete and correct. The changes still needed are these:

- **K1 (blocking).** An access-closure gap in the sector equivalence. It was missed in REVIEW-r1,
  and the overstated sentence at r2:248–250 is the text that REVIEW-r1 itself proposed.
- **K2–K5 (should-fix).** Typing and quantifier repairs to B; the C-regime row; the commitments
  of each option for the owner questions; and the wording of EP:51.
- **N1–N4 (nits).**

Exact replacement text is given for each change. Once the changes are applied as written, no
further review is needed. If K1's text is changed in substance, that paragraph needs a focused
check.

RESPONSE-r1 is right that REVIEW-r1's header miscounted: it reads "fourteen", but there are
sixteen should-fix findings.

## 1. B1, the residual clause and the trace

- **Residual clause (r2:75–78).** It is correct and adequate. Every line not named in §4.1 stays in
  force, and the table does not narrow EP.
- **Coverage of the trace.** EP has 113 nonblank lines, and I checked them mechanically against TR
  §1. Every nonblank line appears in exactly one row. No line is duplicated, missing, or listed
  while blank.
- **Content of the trace.** Each row's content summary was compared with EP. EP:21–29 are traced
  (TR rows 21–29) and kept; their content is summarized correctly. EP:110 is kept with the
  comparator law, availability and transport clause stated correctly (TR row 110, r2:112).
- **Other dispositions checked.** The "record" dispositions for EP:1, 3, 31, 65, 71, 108, 125, 127,
  166, 168 and 170–173 are right: these are headings, standing, a code fence and completed
  deliverables. For EP:172 the scope clause is kept, which is also right. "Kept for every direction
  required" is the right reading of EP:67, 69, 104, 112 and 120–121.
- **EP:51, partly superseded (TR row 51, r2:143–144).** This disposition is right. EP:51 names the
  display EP:53–64 as "the primary proposed model-level target". After the amendment, the primary
  model-level target is §5, and the display survives only through EP:54 and EP:61–64. Keeping
  EP:51 as "record" would leave it naming the old display as the primary target. The only
  supersessions outright remain EP:56–59, plus the forward half of EP:157.

  r2's wording ("superseded only in that its target is §5") is slightly loose. EP:69, EP:112 and
  EP:120 refer back to "the model-level target above" and are kept through their own dispositions,
  so the r2 sentence should say so. This is K5.

## 2. Dispositions F1–F16

At source, each disposition does what RESPONSE-r1 says, and I re-checked the new quotations (§5).

**F2/F3, modified (B added; r2:80–82, r2:149–151, TR row 170).** The modification is correct. Once
Bell is its own obligation, the lists must name it.

**F8, modified (r2:203–212, r2:228–230).** The C-law and C-model rows are correct, and their
commitments are stated correctly. Under C-law, S⇐ implies S⇐ᴺ; this was checked by hand. The
C-regime row is not a third type, since it is admissible only when restated as C-law or C-model.
Its last clause, a "named restricted target", leaves open whether a restricted-target sector result
discharges part 2. It does not: C-4 forbids removing procedures from `J_exact(A)`, and EP:43 makes a
restricted target a different target. This is K3.

**F12, modified (r2:261–275).** The writer correctly notices that `M_C(E, A)` is defined over
`J_exact(A)`, so "members of `M_C(E, A)`" cannot be typed on `J_Bell`. The fix still leaves three
problems:

- "satisfies C" is undefined for a model typed on `J_Bell`. Under C-law in particular, C is a
  predicate on laws over `J_exact(A)`.
- B⇒ quantifies over "No model", without naming the class.
- B⇐ quantifies over unnamed "quantum Bell correlations", and it does not tie its models to the
  coverage witnesses of S⇐. The owner record requires "a compatible model and interface for all
  parts" (#914 c.6875548603).

This is K2. The coordinator's description, that the two Bell directions are "quantified over models
of the architecture satisfying C", fits B⇐. B⇒ should instead range over every admitted model
satisfying C, as S⇒ does.

**The other findings.** F1, F4–F7, F9–F11 and F13–F16 are applied as RESPONSE-r1 states:

- **F1.** The quotations at r2:22–29 match the API text exactly.
- **F4.** TR §2 has 14 rows, and the quotations I hold match.
- **F15 and F16.** The statuses match their sources (r2:307–311, r2:316).

## 3. Sector statements (check 3)

- **S⇒ (r2:237–242).** The quantifiers are complete and well typed: every A, every M in
  `M(E, J_exact(A))` with C(M), one T. M's own fixed label interpretation is used, and composition
  is preserved.
- **S⇐ (r2:244–248).** The quantifiers are complete and well typed. S⇐ implies I.
- **S⇐ᴺ (r2:252–259).** Correct. It is separate and unadopted, and its contrapositive is correctly
  stated: no admitted model outside the sector reproduces a member of `Q_exact(A)`.
- **S-J (r2:261–263).** It is its own obligation and is not implied by the others.

**K1 (blocking), r2:248–250 and r2:352–353.**

*What r2 claims.* r2 states that "S⇒ and S⇐ together give the set equality of #914 c.6875548603",
and that the exclusion of nonquantum behaviour "is required in the sector (S⇒, B⇒)".

*Why S⇒ and S⇐ do not deliver this.* Both compare only the protocols of `J_exact(A)`, which are
quantum-labelled requests (EP:43) interpreted by allowed physical procedures (EP:47). No line of EP
constrains what a member's other admissible procedures (EP:75) produce. A sector member could
therefore satisfy S⇒ on every labelled protocol while its other admissible procedures produce
nonquantum histories, PR-type ones for instance. Main:427 records that the unrestricted OI class
includes this behaviour: "Removing the screened local-intervention restrictions admits the
unrestricted OI behavior class, including the PR negative control."

*What the owner records require.* The owner's set equality is on "the experiment families satisfying
C" (#914 c.6875548603). Its Bell clause requires "excluding stronger-than-quantum correlations in
the physical sector". The dependent statements r2 itself lists require the same thing:

- "account for every operation the proposed physical OI interface admits" (#1169 body);
- "a quantum counterpart for every behavior admitted by the physical OI interface" (#1169
  c.6703342848);
- "no extra nonquantum complete histories" (#1169 c.6763928950);
- "no non-quantum OI behaviours … at the complete operational-theory level" (#1143);
- "no extra accessible behavior" (`composition-source-map.md`:90).

*Consequence.* Reading these "in sector form" as S⇒ drops their content about every admissible
procedure. That silently narrows the forward direction within C, which the authorization forbids.

*Fixes.* Insert after r2:242:

> **S-A (access closure; part of C ⟹ quantum).** For every nonempty finite A and every M in
> `M(E, J_exact(A))` with C(M), every finite adaptive protocol that M's admissible physical
> preparation, intervention and record procedures (EP:47, EP:75) can carry out on the objects of
> `J_exact(A)` has, with its complete accessible record history, the history law of some protocol
> of `J_exact(A)` under M's fixed label interpretation, up to relabelling of outcomes. Witness: a
> proof over every such M and every such protocol. S⇒ alone compares only label-interpreted
> protocols; S⇒ with S-A gives that the complete experiment family of each sector member is that
> of one member of `Q_exact(A)`. Source: #914 c.6875548603 ("the experiment families satisfying C
> are exactly those of QM_fin"; "excluding stronger-than-quantum correlations in the physical
> sector") and the statements of §4.2 that require accounting for every admitted operation.

Replace r2:248–250 from "S⇒ and S⇐ together" through "(§7, R1)." with:

> S⇒ and S⇐ together give that the `J_exact(A)` history laws of members of `M_C(E, A)` are
> exactly those of `Q_exact(A)`; with S-A this is the set equality of #914 c.6875548603 on
> complete experiment families. The coverage form is the reading the owner record supports
> (§7, R1).

Replace r2:352–353 (R5) with:

> - **R5, nonquantum exclusion.** The statements in §4.2 require excluding nonquantum behaviour for
>   every operation the interface admits; under part 2 that exclusion is required in the sector: on
>   labelled protocols by S⇒, on every admissible procedure of a sector member by S-A, and on
>   two-wing protocols by B⇒. EP itself constrains only label-interpreted protocols (EP:47, EP:102),
>   so S-A has no counterpart in the accepted contract.

Then add S-A wherever the obligations are listed:

- In r2:80, r2:150 and r2:369, change "I, S⇒, S⇐" to "I, S⇒, S-A, S⇐".
- In TR row 170, change "S⇒, S⇐" to "S⇒, S-A, S⇐".
- In r2:262, change "S⇒, S⇐ and S⇐ᴺ" to "S⇒, S-A, S⇐ and S⇐ᴺ".
- In r2:284, change "S⇒, S⇐, S-J" to "S⇒, S-A, S⇐, S-J".
- In §8, add item 4:

> 4. Whether the sector's experiment family is every admissible procedure of a sector member (S-A,
>    the reading of "experiment families" taken here) or only the label-interpreted protocols of
>    `J_exact(A)`; the second commits to a restricted reading under which nonquantum behaviour of
>    unlabelled procedures in the sector is permitted, and would be named as such.

**K2 (should-fix), r2:265–275.** Replace r2:265–275 from "On a two-wing interface" onward with:

> `J_Bell(A₁, A₂)` is a two-wing interface still to be typed. It extends `J_exact(A₁ × A₂)`, states
> its locality and setting-independence hypotheses (EP:81–92), and contains every two-wing protocol
> that a model's admissible physical procedures (EP:47, EP:75) can carry out, not only
> quantum-labelled requests. `M(E, J_Bell(A₁, A₂))` is defined as at EP:102 with J = `J_Bell`, and
> a member satisfies C when its restriction to `J_exact(A₁ × A₂)` does.
>
> - **B⇐ (coverage).** For all nonempty finite A₁, A₂ there exists an M meeting S⇐ for A₁ × A₂
>   whose extension to `J_Bell(A₁, A₂)`, with the same fixed label interpretation and meeting I-1
>   to I-4, reproduces exactly the law of every quantum two-wing protocol on the quantum-labelled
>   part of `J_Bell(A₁, A₂)`.
> - **B⇒ (soundness).** For all nonempty finite A₁, A₂ and every M in `M(E, J_Bell(A₁, A₂))`
>   satisfying C, no protocol of `J_Bell(A₁, A₂)` yields correlations outside the quantum set.
>
> Both are required in the physical sector, not in all of OI + E (#914 c.6875548603). `J_Bell` is
> not part of `J_exact(A)` as defined at EP:33–41, and this amendment does not type it.

## 4. Owner questions (check 4)

**Question 1, the type of C.** This is a real question, and the two records conflict on it:
"experiment families" (#914 c.6875548603) against "OI models outside C" (#1169 c.6875724719). The
real options are C-law and C-model. C-regime is not a third option.

**Question 2, whether necessity is part of the target.** This is real only under C-model, as r2:363
says. It is therefore conditional on question 1, not independent of it, and that is stated
correctly.

**Question 3, one architecture or one single model.** This is real and independent of the other
two. The two records again conflict: "one common OI model" (#914 c.6875548603) against "one common,
physically sourced substratum–observer architecture" (#1169 c.6875724719).

**Missing question.** The domain of the sector's experiment family, which is K1's item 4.

**K3 (should-fix), r2:211 and r2:362.** Replace the C-regime row's third cell with:

> not a separate type: admissible only when stated as a predicate of type C-law or C-model, and
> then subject to C-4; a restriction of the procedures compared is not an admissible C, and a
> sector result over such a restriction is a named restricted target (EP:43) that does not
> discharge S⇒, S-A or S⇐ over `J_exact(A)`

In the C-law row, replace "and its equivalence to the quantum class is a theorem" with "and its
agreement with the quantum class on OI + E is a theorem to be proved, not a definition".

**K4 (should-fix), r2:360–365.** The commitments of questions 2 and 3 are not stated. Replace
items 1–3 with:

> 1. The type of C. C-law commits to a condition on history laws over `J_exact(A)` stated without
>    reference to `Q_exact(A)`, under which S⇐ᴺ follows from S⇐; C-model commits to a condition on
>    native data, under which S⇐ᴺ is a separate claim. A regime-formulated condition is admitted
>    only as one of these (§5.2).
> 2. Whether S⇐ᴺ is part of the target; a distinct question only under C-model. Including it
>    commits to a theorem that no admitted model outside the sector reproduces any member of
>    `Q_exact(A)`; excluding it permits such models.
> 3. "One common": the architecture reading commits to I as stated (one 𝔄 with a fixed parameter
>    map, one instance per (A, T)); the single-model reading commits to one model whose subsystems
>    realize every carrier A, one E for every A, typed subsystem embeddings, and each per-A
>    comparison as a restriction of that model.

## 5. New text checked at source (check 5)

These additions were checked and are correct:

- the r2:20–29 quotations from #914 c.6875548603 and c.6875046763 (API text, exact);
- the pins at r2:11–16;
- the §3.1 rows against EP;
- the R2 quotations and `TARGET-THEOREM-r3.md`:34 ("Q_op with every density preparation …");
- the R4 line numbers: `whole-model-bridge.md`:238–240 and :247–248, with :242 "refuted under
  E-AR";
- StructuralClosure.lean :348, :414, :419–420 and :423;
- TypedCompletion.lean :850 (location);
- Main:558, :588 and :600, item (4).

The TR §2 quotations I hold also match: the #1169 body, c.6703342848, c.6763928950, #1143 and the
five records.

**K5 (should-fix), r2:143–144.** Replace "EP:51 introduces this target and is superseded only in
that its target is §5." with:

> EP:51 is superseded only in naming the display EP:53–64 as the primary proposed model-level
> target: the primary model-level target is §5, of which EP:54 and EP:61–64 remain components;
> EP:69, EP:112 and EP:120, which refer back to that display, apply to each direction §5 requires.

Make the matching change in TR row 51.

**N1, r2:129 and r2:51.** The quoted sentence of #1169 c.6703342848 is part of "the explanation"
after which "The owner approved proceeding". "Deterministic hidden dynamics … are admissible" is the
comment author's own statement. In r2:51, replace "for one owner clarification" with "for an
explanation the owner approved". Replace the r2:129 cell with: "Hidden machinery need not be quantum
(the explanation the owner approved: "We do not need the hidden machinery itself to be quantum");
deterministic hidden dynamics admissible (the comment's statement)". REVIEW-r1 F1 introduced the
looser attribution.

**N2, r2:307.** Main:580's check 13 reports "all steps injective, laws exact". That makes it a
computational check, not a numerical probe; REVIEW-r1 F15 introduced the word "numerical". Replace
"is checked by a numerical probe (:580, check 13)" with "is checked computationally (:580, check
13, `opglue_probes.py`)".

**N3, r2:159.** TR §2 has fourteen rows holding sixteen quotations. Replace "Fourteen statements"
with "Fourteen entries".

**N4.** RESPONSE-r1:49 notes that r2 runs over the line guide. Adding K1 and K2 lengthens it
further. If length matters, move §6.2 or the type table to TR rather than shortening the
obligations.

## 6. Register

The register of r2 is neutral and technical. I found no self-narration, no reader instruction and
no caps emphasis outside quotations. The replacement texts above keep the same register.
