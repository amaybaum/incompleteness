# A5-Q3 — amendment A1: the preregistration review applied (#1049)

**Standing: WIP / UNVERIFIED. Paper-only. Pre-assessment amendment to `../DESIGN.md`.** No assessment
of E1–E3 exists at this commit or before it. A1 applies every finding of the independent review of
the preregistration at `f71bdc8706300a743c03346a7b2d1d0bee4f9a49`: verdict REVISE, with blocking
findings F1–F3, should-fix findings F4–F10 and nits N1–N7. The review was relayed to this session by
the coordinating session, and its text is not on `main`.

**Precedence.** A1 governs wherever it differs from `DESIGN.md`. In detail:
- `DESIGN.md` §1 and §2 remain operative as amended by A1 §1 and §2.
- `DESIGN.md` §3–§7 are replaced in full by A1 §3–§7. A1 §3–§5 are the operative rule.
- `DESIGN.md` §8 remains operative and is extended by A1 §8.
- `DESIGN.md` itself is unchanged; its text at `f71bdc87` is the frozen original.

**Handling of revisions made before the assessment (N2).** A revision made before any assessment text
exists lands as an amendment file under `amendments/`, in a single-parent commit that adds only that
file. `DESIGN.md` and earlier amendments are left byte-identical. I1 is re-measured on each such
commit (§6). An amendment made after any assessment text exists must say so in its first paragraph.

**Source snapshot.** Unchanged: `main` at `9c201475ba6fd8f341591d14dd8e88db2e2aaa90`, with `File:N` as
in `DESIGN.md`. No assessment or computation was performed for this amendment.

***

## §0 Owner records (additions and corrected attributions)

**Owner guidance on Q3 [O] (F8).** #1049 comment 6719886996, posted from the owner's account
(amaybaum) on 2026-11-08T09:36:19Z. It records the owner's earlier chat message of 2026-11-08 and was
posted after `f71bdc87` was committed:

> I recommend Q3 before O5. Q3 asks what background independence (A6) means when the microscopic
> dynamics include affine offsets. The existing E1–E3 alternatives lead to materially different
> conclusions. O5—the promotion to local gauge invariance—depends on how that question is resolved.
> … The Q3 assessment should compare E1–E3 against the existing A6 sources, identify which
> assumptions each imports, and recommend whether any extension is independently justified. It must
> not simply choose the extension that produces the desired gauge group. The outcome may be that
> none of the extensions is selected. O5 and the proposed downstream A5 record changes remain
> unapproved.

The same comment records the boundary of the unit: "O5 stays unauthorized. Q3 may read the local
transformation class directly from each extension's definition. It may not derive any promotion to
local gauge invariance." This sentence is the source of criterion A3 (§3).

**Attribution of the #1169 sentences (N1).** `DESIGN.md` quotes two sentences from #1169 comment
6719386464 (amaybaum, 2026-11-08T08:41:15Z). They have different standing:
- "A restriction designed to exclude a particular construction is treated as tuned to the target."
  This is refinement 1 as worded by the coordinating session. The owner approved it ("The owner
  approved the proposed sequencing and all three refinements"). It is not quoted owner speech.
- "Every candidate physical restriction must have an independent physical motivation …" This is
  quoted owner speech, stated for FHE-SEL-1 Stage 1.

Applying the Stage 1 standard to Q3 is this file's choice [D]. No owner record extends it to Q3. The
owner's own boundary for Q3 is in c.6719806528: "Do not introduce assumptions chosen merely to
eliminate affine offsets."

**The #1049 safeguard (F9).** This is the Issue body of #1049, section "Scope and safeguards", as read
on 2026-11-08 (Issue `updated_at` 2026-11-08T09:36:19Z). The Issue body is mutable and is not on
`main`. The full sentence pair:

> Site-dependent transformations on other carriers and time-dependent coordinate changes may
> eliminate affine offsets in particular settings. Their physical admissibility as OI gauge
> transformations must be established separately.

**Conditionality on amplitude-scale gauge (N6).** The affine rule class F = linkF + b, which is the
setting of all three extensions, rests on amplitude-scale gauge. Substratum:272 records that principle
as "*Status (open, referee-grade).* Amplitude-scale gauge is adjoined as an explicit operational
principle". Every verdict, entry and outcome produced under this rule is therefore conditional on
amplitude-scale gauge, and the result states this in its outcome line.

***

## §1 Scope (amends `DESIGN.md` §1.1)

- **The affine-local-group question (F7).** No outcome of this rule bears on the first clause of the
  core file's Q3, whether A6's local group is AddAut(V) or the affine group. Under Q2, an extension
  that treats translations as local gauge transformations would need a justification of their
  physical gauge status. That question is outside the candidate set authorized by c.6719806528 and
  framed by c.6719886996.
- **Criterion A3** is bounded by c.6719886996's sentence quoted in §0.

***

## §2 Candidate statements and variants (amends `DESIGN.md` §2.3–§2.4)

**E2's offset map (N5).** In E2, b_i = Σ_{j ∈ N i} a_ij reaches every b_i whenever N i is nonempty. On
the torus every N i has 2d ≥ 2 elements, so every b is reached.

**Variants recorded in advance.** These replace `DESIGN.md` §2.4. Each relation below is read from
the definitions in `DESIGN.md` §2.3.
- **E1 / E1′.** As in `DESIGN.md` §2.4. The two have the same data and transport. They differ only in
  the domain of the quantifier over g: all of AddAut V for E1, the site-wise stabilizer of b for E1′.
- **E1 ↔ E3 (F4).** E1 is E3 with the offset transforming by the trivial law, b_i ↦ b_i. Each is
  therefore a variant of the other that differs in the offset's transformation law.
- **E2's split.** The split of b into link offsets a_ij is not unique. At b = 0 the data space contains
  nonzero link offsets that sum to zero at every site.
- **E2 ↔ E3.** The law that E2 induces on b, b_i ↦ g_i b_i, is the law E3 states. This is recorded
  under A4 and is not a verdict.
- **E3's offset laws.** b transforms by a representation other than g itself. The trivial
  representation gives E1. The Q4 note's H-b is the global, O-action form of E3's choice.
- **Transformation class, all three.** All of AddAut V, or a subgroup such as the unitaries on the
  lift.
- **Aff(V) readings (F7).** A reading of any extension with an affine local group fails C-LIN's
  same-class clause by construction, and lies outside the candidate set. Suppose an extension's own
  stated motivation supports such a reading as well as its AddAut reading. Then that is recorded
  next to its J5 entry as a scope finding ("J5 within the AddAut class; an Aff(V) reading equally
  supported"). It does not count against J5.

The assessment reports every variant it finds beyond this list (I14, §6).

***

## §3 Evaluation criteria (operative; replaces `DESIGN.md` §3)

Block A is recorded, and the decision rule never scores it. §4 reads blocks B–D and the controls. It
reads block A only through J5, which compares variants, and J6, which excludes A entries from
counting.

### Block A — mathematical consequences (recorded, not scored)

- **A1. What the extension forces on b.** For E1, the set of b for which Cov_E1 holds. For E2 and E3,
  the transformation law of the rule offset b and whether any b is excluded. Cases: K = 1 and K ≥ 2;
  q odd, q even > 2, q = 2; finite carrier and lift; uniform and non-uniform b; S1. What an imported
  assumption yields **together with 𝔅** is recorded here, and only here (F1).
- **A2. The Q4 stabilizer.** As in `DESIGN.md` §3: Glob_Ek(𝒢), compared with the Q4 note's G_0 and
  G_v under (L), (A-lin) and (A-aff), stating whether H-b and μ_{A₁} = 1 are used, and whether the
  Stage 2(d) object is taken at rule level or coupling level (Q4b).
- **A3. The O5 boundary.** The local transformation class under which Cov_Ek holds with the
  extension's data transported, read directly from the extension's definition (c.6719886996). No
  promotion to local gauge invariance, link action, plaquette statement or local SU(3)×SU(2)×U(1) is
  derived.
- **A4. Relations among E1–E3.** Whether two extensions induce the same transformation on b, or
  coincide on a subclass.

**A3 and A4 entries never count toward J6 (F2(iii)).** An A3 entry restates part of a definition, and
an A4 entry is a relation internal to the candidate set. Neither is checkable against an independent
result.

### Block B — imported assumptions

**The baseline 𝔅.** As in `DESIGN.md` §3, with two changes:
- E4, H-link and Theorem 7 are in 𝔅 only for their use on the field and the coupling. E4 or H-link
  used on the offset is an import (B1), because the Q4 note's Q4a records that E4's application to
  the offset is open (F10).
- **Role (F3).** An element's *role* is the role that a source cited at the pin states for it. A role
  stated only in this file or in a parent note is not a role.

**B1. Imported assumptions.** Each entry gives the statement, where it appears at the pin (or "not in
the corpus"), and its status there. Each extension has at least the following mandatory B1 row,
because no A6 source at the pin mentions offsets:
- E1: "the offset is not transformed";
- E2: "link couplings are affine maps; the offset is link data transported by g_i ∘ A_ij ∘ g_j⁻¹";
- E3: "the offset is site data transformed as the field is".

None of the three laws is the default, and each is assessed under C.

**B2. Baseline elements used outside their stated role.** An element of 𝔅 counts as imported in a
given use when the extension applies it to an object its stated role does not cover. Neutral
patterns, one shaped like each extension:
- a quantifier stated over transported data, applied to a datum that is not transported;
- a transport law stated for additive maps, applied to affine maps;
- an action stated on configurations, applied to a datum that is not a configuration.

Each pattern is an example of the definition. None is a finding about any extension.

**The B2 table (F3).** The assessment fills each cell with the stated role and its source (C1), and
with whether the use lies inside that role. The "used in the statement" entries are read from
`DESIGN.md` §2.3 before any assessment. They are fixed here and are not verdicts.

| 𝔅 element (stated role, source at pin) | E1 | E2 | E3 |
|---|---|---|---|
| Transformation class ι → AddAut V (BackgroundIndependence.lean module statement; A6Instantiation.lean `pk4_shift_not_scalar`, `cx2_unitary_gaugeLink`) | used: every g is required to commute with an untransported b | used: acts on link offsets a_ij | used: acts on b |
| `gaugeLink` (:124 docstring: "the transformation law of `SM.md:112`", which is SM:116 at the pin) | used on M only | extended to affine link maps | used on M only |
| `siteAct` (:92 docstring: "the pointwise action … on configurations") | appears on the right-hand side, acting on F's value including b | not used on the offset directly; the induced law on b is g_i b_i | used to transport b |
| `V →+ V` typing of link couplings (`linkF` :118; `linkSubstratum_A5` :147) | kept; the offset is a site datum | relaxed to affine maps | kept; the offset is a site datum |
| E4 (Substratum E-inputs; Q4 note Q4a) | not used in the statement | not used in the statement | not used in the statement |
| H-link (SM:340, SM:374) | not used in the statement | not used in the statement | not used in the statement |

E4 and H-link enter only A2 entries that invoke H-b. In those entries their use on the offset is a B1
import.

### Block C — independent physical justification

For each B1 and B2 import, and for each hypothesis that would place an extension in J_c (F10):
- **C1. Source.** As in `DESIGN.md` §3. Presence on `main` is not a justification (§A.46 item 7).
- **C2. Classification.** **Equivalence and presupposition are judged for the assumption on its own,
  without 𝔅 (F1(a)).** What the assumption yields together with 𝔅 goes in A1 and never in C. No
  clause counts deriving T1, T2 or ¬T as a merit or as a demerit. The classes:
  - **independent** — the stated motivation and its support do not presuppose T1, T2 or ¬T, and are
    not designed to exclude a particular construction. Such constructions include S1 or the class of
    offset-carrying rules, and, in the mirror direction, the linear class or the Stage 2(d)
    construction (N7);
  - **target-adjacent** — taken on its own, the assumption or its motivation presupposes T1, T2 or
    ¬T; is logically equivalent to one of them on the rule class at issue; or is supported only by a
    consequence of one of them;
  - **target-defined** — any of the following:
    - the stated reason is to obtain T1, T2 or ¬T, or to exclude a particular construction in either
      direction;
    - **the functional test (F5):** the assumption's statement is itself a restriction on, an
      identification of, or an exclusion of values or components of the offset, rather than a law for
      how the offset transforms, and it has no stated effect outside the offset sector. This applies
      whatever reason is given, and equally to assumptions that eliminate offsets and to assumptions
      that retain them. A transformation law for b is never caught by this test; its consequences for
      b are recorded in A1;
  - **mixed** — an independent component together with a target-adjacent one, each identified;
  - **none found** — no motivation located after the C3 search.
- **C3. Search record.** As in `DESIGN.md` §3. Every "none found" carries its search record (I15).

### Block D — consistency

The grades are those of `DESIGN.md` §3 (consistent / tension / inconsistent), with one addition:
- **out of scope** — the source's statement is made for a class of rules that does not contain the
  extension's offset sector.

D1–D4 are as in `DESIGN.md` §3, amended as follows.

- **D1, the "imposes no condition" sources (F1(b)), graded in advance.** The sources are:
  - Substratum:102: "once it is in place the local transformation law imposes no further condition
    on the rule";
  - SM:118: "once the link variable is data transported in this way the local transformation law
    imposes no further condition on the rule";
  - Main:726 item (xii): "in the form formalized imposes no restriction on the rule"; and its ledger
    sentence "(xii) restricts no rule";
  - BackgroundIndependence.lean:52–55 (`D3-a`): "it restricts no link-coupled rule".

  **Grade, for every extension:** these sentences are graded **out of scope** on the offset sector
  (b ≠ 0) and **consistent** on the linear class. The reason is that each is stated where the rule
  class is additive link-coupled:
  - Substratum:102 lists A6 beside A5 (Substratum:100), and states the rule as link-coupled data;
  - SM:118 is a statement about "the wave equation" of SM:116 under the linear transport;
  - Main:726 item (xii) says "in the form formalized", and the formalized form is `A6Cov`, typed
    `V →+ V`. Item (vii), A5, is in the same ledger;
  - the kernel docstring states its scope as link-coupled rules over `V →+ V`.

  No extension is graded tension or inconsistent on these sentences for restricting b, or for
  restricting nothing. On the linear class all three coincide by C-LIN.
- **D3, scoped (F6).** D3 applies only to:
  - an identification by a map outside the extension's transformation class, such as a translation
    or a time-dependent map; or
  - a declared physical identification of rules beyond the covariance relation.

  The covariance relation between (M, b) and (gaugeLink g M, g·b) under E2 or E3 is not an
  identification under D3, just as `A6Cov` relates M and gaugeLink g M. The #1049 safeguard (§0)
  applies to the first case.
- **D4.** P1–P6 as in `DESIGN.md` §3.

***

## §4 Decision rule (operative; replaces `DESIGN.md` §4)

Clauses J1–J4 are as in `DESIGN.md` §4, with J3 read through the amended C2. J5 and J6 are amended:

- **J5, operationalized (F4).** A variant counts as equally supported unless a source cited at the
  pin, or the extension's own stated motivation, states the feature that distinguishes it.
  - **Decided in advance:** conformity with `A6Cov`'s quantifier, ∀ g over the whole transformation
    class, counts as that selection among variants that differ only in the domain of the quantifier
    over g. It does not select among variants that differ in the offset's transformation law, because
    no A6 source at the pin states a law for offsets.
  - J5 holds iff no equally supported variant within the AddAut class gives a different A1 or A2
    entry.
  - Aff(V) readings are reported as in §2 and do not count against J5.
- **J6, scoped (F2).** As in `DESIGN.md` §4, with A3 and A4 entries excluded (§3). Suppose the
  consequence that would satisfy J6 can be stated only by a derivation outside the O5 boundary. Then
  J6 is recorded as **not evaluable within the authorized scope**. That is distinct from "not held".

**Two sets, reported separately (F2(ii)).**
- **J₁₋₄ — "independently justified":** the extensions meeting J1–J4. This answers the owner's
  question in c.6719886996.
- **J₁₋₆ — "adoptable as a premise":** the extensions meeting J1–J6. This is the §A.29 standard for a
  Layer-0 revision, which §A.45 rule 5 applies to any proposal adding a premise.

**Outcome.** The outcome is defined on |J₁₋₄|:
- **(S)** exactly one extension is independently justified;
- **(M)** more than one is, and the choice stays open with no tie-break; A1 and A2 entries are never
  used to rank;
- **(N)** none is. **(N) is a valid outcome.** It states only that none of E1–E3 is independently
  justified on the record at the pin. It does not state that each is false, that no extension of A6
  to offsets exists, or anything about A5.

The J5 and J6 status of each extension, and the set J₁₋₆, are reported alongside the outcome. They do
not change it.

**J_c (F10).** J_c is the list of extensions that would meet J1–J4 given a named open hypothesis. The
hypothesis is itself classified under C2. Only a hypothesis classified independent, or mixed with an
independent component that suffices on its own, can place an extension in J_c. J_c is reported with
the outcome and never counted into J₁₋₄.

**Clauses that cannot be evaluated.** A clause among J1–J4 that cannot be evaluated is labelled "not
evaluable", with its reason. The extension is then not in J₁₋₄, and the label is reported distinctly
from "not held". For J6, see above.

**Non-differential failures.** An extension that fails a clause for the same reason the baseline
fails it (C-POS, §5.1) is reported as failing that clause in common with the baseline.

**Every verdict and outcome is conditional on amplitude-scale gauge (§0, N6).** What no outcome does
is unchanged from `DESIGN.md` §4. Each per-extension verdict lists J1–J6 as held, not held or not
evaluable, and names the B, C or D finding behind each one that is not held.

***

## §5 Controls (operative; replaces `DESIGN.md` §5)

### 5.1 C-POS — positive control on the baseline, and C-CAL — calibration of C2 (F2(i))

**C-POS.** The rule is applied, in the assessment, to the baseline `A6Cov` on the linear class. Its
imports are its own content: covariance with transported link data, the class ι → AddAut V, and the
coupling as link-valued data. The predicted J-profile, fixed now [D] and labelled a prediction:
- **J1:** held. It is a predicate on stated data (:131).
- **J2:** held, trivially.
- **J3:** predicted held, through a **mixed** classification.
  - The independent component is the standard gauge principle, that internal symmetries act locally
    with a transported connection [L]. It does not presuppose T1, T2 or ¬T.
  - The target-adjacent component is the role SM:114 states, "the premise carrying the surviving
    global stabilizer to the local gauge reading" (T2).
  - Whether the independent component suffices on its own is for the assessment, after the C3
    search. If it does not, the baseline fails J3, and that is reported.
- **J4:** held. It is the source.
- **J5:** predicted held. The alternative readings `A6-inv`, `A6-glob` and `A6-sd` are distinguished
  by cited sources: Substratum:102 says A6 "is not the stronger fixed-background condition", and SM:104
  separates the state-dependent principle.
- **J6:** predicted **not held**. The consequences of the interface in the corpus (SM:118: the link
  transforms as a connection, and the plaquette transforms in the adjoint) are identities of the
  interface. Its further consequences are T2 or lie beyond the O5 boundary. No consequence checked
  against an independent result at the pin is known to this drafting session.

So the baseline is predicted to be in J₁₋₄ and not in J₁₋₆. J6 is therefore expected to bind the
baseline as well as the extensions, and a J6 failure of an extension is reported as non-differential
where it shares the baseline's reason. This is why the outcome is defined on J₁₋₄.

C-POS is a calibration that is reported, not a pass/fail gate. The assessment reports the observed
profile against the predicted one, clause by clause, with each deviation explained.

**C-CAL (pass/fail).** C2 must classify the following item as **independent**: A4's translation
clause applied to the affine rule including its offset, "F commutes with lattice translations".
- Its source is Substratum:98's anchor, "the homogeneity of physical law — no experiment has found a
  preferred location in the laws". The sentence's grammatical referent within Substratum:98 is A4's
  second sense. Its content bears on translation commutation, and the assessment records that
  reading.
- The clause's statement concerns the whole rule, M included. So the functional test does not catch
  it, even though it implies that b is uniform (core file B0.3(a)).

If C2 returns any other class for C-CAL, C2 is miscalibrated. No outcome is then rendered until a
disclosed amendment repairs it.

### 5.2 C-LIN — linear-limit control, with a negative case (F7)

C-LIN is as in `DESIGN.md` §5.1, for E1, E2, E3, E★ and E☆.

**Negative control.** **E-inv**, an extension built on `A6Inv` (:104): the coupling is held fixed and
preserved pointwise, and the offset is untransported. At b = 0 it reduces to `A6Inv`, not to `A6Cov`.
It must fail C-LIN. If C-LIN as applied does not fail E-inv, C-LIN is void, and J2 is not evaluable for
any candidate until a disclosed amendment repairs it.

An Aff(V)-class reading fails C-LIN's same-class clause by construction (§2).

### 5.3 C-TI — target-import check (replaces `DESIGN.md` §5.2)

No criterion or clause takes as a merit or a demerit whether an extension yields T1, T2 or ¬T. No
clause refers to the desired gauge group or to b = 0 in that role. The permitted references:

| Clause | Reference | Role |
|---|---|---|
| `DESIGN.md` §1.2 | defines T1, T2, ¬T | naming, for exclusion |
| A1 | what the extension forces on b, including what it yields with 𝔅 | recorded, not scored |
| A2 | G_0, G_v, U(K) | recorded, not scored |
| A3 | local gauge invariance, SU(3)×SU(2)×U(1) | scope exclusion |
| A3, A4 | not counted toward J6 | exclusion |
| 𝔅 | Theorem 7, E4 and H-link on the field and coupling, for block A | baseline, recorded |
| C2, "judged on the assumption alone" | T1, T2, ¬T | prevents a derivation of T1 (or T2 or ¬T) with 𝔅 from counting against the assumption (F1(a)) |
| C2, target-adjacent and target-defined | T1, T2, ¬T, and excluded constructions in both directions | penalizes dependence on the target in either direction; never rewards attaining it |
| C2, functional test | elimination or retention of offset values | applies symmetrically to elimination and retention; transformation laws exempt |
| D1, "imposes no condition" sources (Substratum:102; SM:118; Main:726 (xii) and its ledger sentence; BackgroundIndependence.lean:52–55) | restricting b or not | graded out of scope on the offset sector for every extension; never correlated with T1 (F1(b)) |
| D4-P4 (N4) | (C-b) Theorem 7, (C-c) Theorem 15, T2 outputs | controls on the linear class, identical for every candidate |
| J5 | variants that change A1 or A2 | penalizes adjustability to the outcome, in either direction |
| J6 | consequences that are T1, T2 or ¬T do not count | exclusion |
| Outcome (M) | A1 and A2 never used to rank | exclusion |
| C-POS | `A6Cov`'s T2-directed role (SM:114) | calibration, reported |
| C-LIN | b = 0 as `A6Cov`'s own data | control, identical for every candidate |
| E★, E☆ | the target, by design | countercontrols |

**Result at this commit [D]:** no clause uses T1, T2 or ¬T as a merit or a demerit. The reviewer
re-checks this table against §3–§4. At checkpoint 2 the reviewer also checks that no per-extension
verdict cites an A1 or A2 entry as its reason, except through J5 or J6 as worded.

### 5.4 Countercontrols (F5; replaces `DESIGN.md` §5.3)

Both are built on E3's data, so that neither inherits a failure specific to E1. Each must be rejected
through **J3**, alone or together with J4 through D2 or D3, **and the J3 failure must come from the
added stipulation**, not from anything E3 shares. If either is rejected only by other clauses, or
is not rejected, the rule is void and no outcome is rendered.

- **E★ (explicitly target-tuned).**
  - Data and covariance: E3's.
  - Added stipulation: two rules F_{M,b} and F_{M,b′} are the same physical rule, for all b and b′.
  - Offered justification: "the offset would remove the singlet-block U(1) that Substratum:163
    identifies as hypercharge, so it is unphysical."

  Expected rejection:
  - J3, because the justification is target-defined (T2) and the functional test catches the
    identification;
  - J4 through D3, because the identification is a declared physical identification beyond the
    covariance relation;
  - J4 through D2, because S1 and its linear part are distinguishable at Main's absolute interface
    (core file, Proposition 2.6(a)).
- **E☆ (neutral-sounding).**
  - Data and covariance: E3's.
  - Added stipulation: offsets are identified modulo the phase of their A₁-block component.
  - Offered justification: "offsets are background data, and the phase of background data is not
    observable."

  Expected rejection:
  - J3, by the functional test. The stipulation is an identification of offset components and has
    no stated effect outside the offset sector, whatever reason is given. In addition, C1 finds no
    source at the pin for "the phase of background data is not observable" (search record required);
  - J4 through D3, as a declared identification beyond the covariance relation.

C-LIN passes for both by design.

### 5.5 When the verdict is void

- **C-TI fails at assessment:** the affected clause is void until a disclosed amendment repairs it.
- **C-CAL fails:** C2 is void. No outcome is rendered until a disclosed amendment repairs it.
- **C-LIN does not fail E-inv:** C-LIN is void, and J2 is not evaluable.
- **E★ or E☆ is not rejected through J3, as specified in §5.4:** the rule is void, and no outcome is
  rendered.

***

## §6 Invariants and their checkpoints (operative; replaces `DESIGN.md` §6)

| # | Invariant | Checkpoint that measures it |
|---|---|---|
| I1 | The rule, as amended, is fixed before any assessment exists | `git show --stat` of `f71bdc87` lists exactly `DESIGN.md` (parent `9c201475`). `git show --stat` of the A1 commit lists exactly this file (parent `f71bdc87`). No assessment file exists in either tree. The same check is re-measured on any later pre-assessment amendment |
| I2 | `DESIGN.md` and A1 are unchanged after the A1 commit, except by disclosed amendment | At checkpoint 2, `git diff <A1> <head> -- ../DESIGN.md A1-prereg-review.md` is empty. Any later amendment is a new file here, saying whether it was written after any assessment text, and is cited by the result |
| I3 | Every `File:N` and Lean line resolves at the pin | Reviewer reads each cited line with `git show 9c201475:<path>` |
| I4 | Paper only | `git diff --name-only 9c201475 <head>` lists only `.md` files under `q3-a6-offsets-20261108/`. "Every step was done by hand" is the writer's self-report, and is recorded as such |
| I5 | No manuscript, ROADMAP or kernel change; A5 unchanged | `git diff --name-only 9c201475 <head> -- papers book verification/ROADMAP.md verification/lean verification/lean-mathlib` is empty |
| I6 | No target import | The C-TI table (§5.3), at this commit and at checkpoint 2 |
| I7 | C-LIN evaluated for E1, E2, E3, E★, E☆, and fails for E-inv | One C-LIN entry per candidate, and the E-inv entry, in the result |
| I8 | Countercontrols rejected through J3 by the added stipulation | For E★ and E☆, the result names the J3 finding and attributes it to the stipulation. Otherwise no outcome is rendered |
| I9 | (N) admissible; no tie-break; outcome on \|J₁₋₄\| | Outcome computed from \|J₁₋₄\| alone, with J₁₋₆ reported separately and no ranking |
| I10 | O5 boundary | Reviewer checks that the A3 entries are read from the definitions only, as c.6719886996 bounds them |
| I11 | Owner records quoted with author and time | `DESIGN.md` header and A1 §0; repeated in the result |
| I12 | Off-main references traced | §7; the result carries its own trace |
| I13 | Neutral register | Reviewer scans the added lines for the §A.32 and §A.33 phrase families |
| I14 | Every variant found beyond A1 §2 is reported | The result's variant list, compared with A1 §2 |
| I15 | Every "none found" carries its C3 search record | Each C2 "none found" entry has a search record, checked by the reviewer |
| I16 | C-POS and C-CAL evaluated | The result reports the baseline's observed J-profile against the prediction in §5.1, and C-CAL's classification |
| I17 | Every verdict carries amplitude-scale-gauge conditionality | The outcome line states it |

***

## §7 References not on `main` (§A.42 item 8; replaces `DESIGN.md` §7)

| Reference | Used for | Classification |
|---|---|---|
| #1049 c.6719806528 | authorization and boundaries | support, by quotation with author and time |
| #1049 c.6719886996 (F8) | Q3 scope guidance; A3's boundary | support, by quotation with author and time (§0) |
| #1049 c.6624263637 | Q1, Q2 (D2, D3) | support, by quotation; also quoted on `main` in the core file §6 |
| #1049 Issue body, "Scope and safeguards" (F9) | D3's safeguard | support, by quotation of the full sentence pair (§0). The Issue body is mutable, and is quoted as read on 2026-11-08 |
| #1169 c.6719386464 | the standard applied in C2 and J3 | support, by quotation, with the attribution corrected in §0 |
| #1169 c.6719708521 (the Stage 0 map; `STAGE0-MAP.md` is not on `main`) | context; vocabulary | provenance. C2 defines every term it uses |
| The independent review of `f71bdc87` | the findings applied here | provenance. Each change is stated here in full, so no content of the review is relied on |
| #1083 | context | provenance |
| Branch `research/a5-q3-a6-offsets-20261108` | this work | provenance |

***

## §8 Drafting disclosure (extends `DESIGN.md` §8)

Before writing A1, this session read the review of `f71bdc87`. The review re-derives that Cov_E1
reduces to "siteAct g b = b for all g", and that E2 induces E3's law on b. These are A1 and A4
entries, and the rule uses neither as a merit or a demerit. The C-POS prediction (§5.1) and the B2
"used in the statement" entries (§3) were written with knowledge of `A6Cov`'s definition, of the
§2.3 statements and of the core file's N9. They read definitions and assess nothing.

***

## Finding-to-change map

| Finding | Change |
|---|---|
| F1 | C2 judged on the assumption alone, with yields-with-𝔅 recorded in A1 only. The "imposes no condition" sources graded out of scope on the offset sector for every extension, with the reason given. Both added to C-TI |
| F2 | C-POS on `A6Cov` with a predicted J-profile (J6 predicted not held). Two sets: J₁₋₄ "independently justified", which carries the outcome, and J₁₋₆ "adoptable as a premise". A3 and A4 do not count for J6. "Not evaluable within the authorized scope" introduced |
| F3 | Role defined as the role a cited source states. Mandatory symmetric B1 offset-law rows. Symmetric B2 table. Neutral patterns replace the N9-derived example |
| F4 | J5 operationalized. The ∀-quantifier selects only on quantifier domain. E1↔E3 relation recorded |
| F5 | E★ rebuilt on E3. E☆ added. Rejection required through J3 from the stipulation. Symmetric functional test in C2 |
| F6 | D3 scoped to maps outside the class and to declared identifications beyond covariance |
| F7 | E-inv negative control for C-LIN. Affine-local-group exclusion stated; Aff(V) readings reported, not counted |
| F8 | c.6719886996 quoted, reclassified as support, and cited as A3's source |
| F9 | #1049 safeguard traced and quoted in full |
| F10 | J_c hypotheses classified under C2. E4 and H-link on the offset are imports |
| N1 | #1169 attribution corrected. The application to Q3 marked [D] |
| N2 | Pre-assessment revisions land as amendments. I1 re-measured |
| N3 | I14 (variant reporting), I15 (search records). I4's self-report noted |
| N4 | D4-P4 and the F1(b) sources added to C-TI |
| N5 | E2's offset map reaches every b on the torus |
| N6 | Every verdict conditional on amplitude-scale gauge (Substratum:272). I17 |
| N7 | C2's excluded-construction examples mirrored |
