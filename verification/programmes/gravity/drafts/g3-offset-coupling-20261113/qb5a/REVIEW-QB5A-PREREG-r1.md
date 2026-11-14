# REVIEW-QB5A-PREREG-r1: independent preregistration review of G3 QB5(a), r1

**Verdict: REVISE.** Seven findings are blocking, fourteen are should-fix and five are nits. The design is sound:
two stages, inert constructed rows, a fixed candidate list, symmetric relativity of the universal negatives,
and controls on constructed examples. But the rule as written leaves several decisive choices to the
executor. It also sets defaults that settle QB5(a)'s central question without saying so. And its
witness-tuning countercontrol cannot fail. Because the blocking fixes change rule text, the next revision
(r2) needs a fresh review round, not only a check of its edits.

**Target.** Branch `research/g3-offset-873-20261113` at `2e18a2dfe8db99d1806a7c2081a63a2f0ecee5e0`, parent
`8d661a649`. The commit adds exactly two files: `qb5a/G3-QB5A-PREREG-r1.md` (949 lines, "P:n") and
`qb5a/NOTES-QB5A-r1.md` (149 lines, "N:n"). Other references: "r5:n" is `G3-UNIT2B-BG-r5.md`, "U2Ar3:n" is
`G3-UNIT2A-r3.md` and "U1r5:n" is `G3-UNIT1-r5.md`. Corpus lines refer to `main` at `c3b5f37a`, which is
also the current `origin/main`.

**Method.** I worked by reading and hand logic only, and ran no computation on OI rules. I ran the §9–§10
rule-level controls by hand (§2 below). Each inventory `file:line` was checked against
`git show c3b5f37a:<path>` for location only. I classify no inventory passage under F4 or F5 and state no
expected outcome. Wherever I propose rule text, it is justified from AGENTS.md, from r5's definitions or
from external examples.

**Reviewer provenance.** As the brief required, I read r5 in full, including its §2.4 per-passage readings.
I also displayed inventory lines to check their location. A clause I propose here can affect inventory rows,
as any status or role test must. QR-2 and QR-12 are the two most likely to. Neither is motivated by any
passage's expected classification. The second reader of QR-6 is the check on this review as well.

**Owner records read first-hand** (#873):

- c.6872004336 (`amaybaum`, 2026-11-14T04:53:01Z): QB5(a), QB6 and QB7(a)/(b), and the gate "The QB5(a)
  investigation may proceed once its decision rule passes independent preregistration review".
- c.6872277416 (`amaybaum`, 2026-11-14T05:17:28Z): the owner guidance, now on record (QR-20).

***

## 1. What holds

- **Architecture.** The rule renders Stage 2 (formalization verdicts) before Stage 3 (the mapping to B_G),
  and the order is checkable in the commit history (X-7). This is the right way to meet the owner's
  instruction not to select F4 "merely because it excludes an unwanted coupling" (c.6872004336).
- **Symmetry for the witness (I-SYM, I-BLIND item 3).** The witness rows receive the same per-term tests,
  and the derived cells U[v, b] are reported for them (P:607). They cannot move a Stage-2 verdict, because
  status Cx is never a commitment (P:499). That asymmetry is principled. A constructed row is not something
  the corpus commits to, so its unrealizability under F4 can count neither against F4 nor for it. This is
  "apply equally" in the sense the guidance needs.
  - One consequence follows. Because status always differs, no witness row has the same attribute vector
    as a corpus row, so I-SYM's "identical vectors" consequence (P:115–116) never bites across the two
    groups. The protection that matters lies in the attribute tests and the carve predicates (QR-3, QR-6).
- **The corpus's own offset coupling.** GR:352 and GR:577 are classified as ordinary corpus rows (Group V).
  They can therefore reject F4, or fail a carve under GRT-4, exactly as any other corpus row can.
- **Relativity of both universal negatives.** D-5 (P:542–544, OQ-2) makes both universal negatives relative
  to the same frozen list. That repairs the tilt CONFIRM-BG-r4 DF-2 identified, and it is symmetric.
- **OQ-3's counting.** It is r5 §1.2's content definition, as relativized by R-6, applied to carves. It is
  not a new choice (§5, OQ-3).
- **The four-class partition.** The partition of §8.2 is correct [A]. Each Stage-3 implication in the §8.3
  table agrees with items 1–5, apart from the gaps noted in QR-25.
- **The late-passage rule.** §4.5 is sound. An X-row reaches the decisive table only through an amendment,
  and the verdict as rendered stays beside any amended one.
- **Inventory locations.** Every `file:line` in §4.2 exists at `c3b5f37a` and opens with the content the row
  describes. GR:400 is correctly split into Readings 1 and 2.

***

## 2. Rule-level controls, run by hand

| Control | Result | Note |
|---|---|---|
| RC-P (TC-R) | green | p1 is rejecting for F4, F4-law and F4-null. Every carve fails GRT-1. F5 is Admissible. Class R; Stage 3 gives (B). |
| RC-N (TC-N) | green | No row is rejecting or potentially rejecting for F4. Class C, F5 Admissible, (C). |
| RC-X X1–X4 | green | Each flip moves the class as required. |
| RC-W W-a | green | It catches only a row-naming clause, which I-SYM already forbids syntactically. |
| RC-W W-b | green, **vacuously** | It holds by P:499 whatever the rest of the rule says (QR-6). |
| RC-W W-c | green | Δ† fails GRT-1 in both forms, and GRT-5 in the row-identity form. This is a real test. |
| RC-W W-d | green, **vacuously** | It holds by P:499 (QR-6). |
| RC-U TC-U | **red as written** | Stage 2 gives U, with u1's A2 named. Stage 3 cannot be computed: TC-U has no `w*` row, so no formalization can be sorted (QR-7). |
| RC-U TC-K | green | F4[Δk] is Undetermined, so the class is U. Resolving it Admissible gives (C); resolving it failed gives R and so (B). The resolutions disagree, so the outcome is (C) with K3 named. |

Under P:720–724, a rule-level control with a result other than its required one has failed. RC-U fails as
written, so the rule cannot be frozen until QR-7 is applied.

***

## 3. Answers to the brief's checks, in short

1. **Reachability.**
   - Every class and every outcome is reached by some toy once QR-7 is applied. None is trivially forced.
   - Three properties tilt the rule as written:
     - Unhedged assertions are non-commitments by default, which widens C (QR-2).
     - U is the attractor whenever a committed row has an Und decisive cell. That is acceptable, but it
       should be stated (QR-19).
     - (A) requires F5 to be Rejected. That needs an explicit grounding commitment or a failed control, so
       on a corpus without one, (A) is unreachable by construction. This is a property of the question, not
       a tilt, but it must be stated (QR-19).
   - R and (A) both rest on universal negatives over a finite list, and both can be met. One exception:
     Δ9 is an open slot that makes R's negative unbounded and also opens a fitting channel (QR-3).
   - (C) absorbs every disagreement between branch, route and witness convention only if QR-5 says so. As
     written, the rule says nothing about how those results combine.
2. **Symmetry and anti-fitting.**
   - X-5 applies the rule equally.
   - X-7 is real and checkable for the order of the record. It does not create blindness, because the
     executor already knows the witness's attributes from r5 (QR-6).
   - RC-W would not catch a rule tuned to the witness (QR-6).
   - After the corpus has been seen, the main channels for adjusting the rule are:
     - Δ9 (QR-3);
     - GRT-4's undefined "agrees" (QR-8);
     - the absence of a default for a test that "cannot be applied as written" (QR-17);
     - the A2 density ambiguity (QR-11);
     - the side-keyed role test (QR-1).
3. **Controls.**
   - All rule-level controls are constructed.
   - None exercises the §5 tests themselves, because the toys stipulate attribute values (QR-9).
   - Several sensitivities have no flip: role, A3x, Conflict, GRT-2, GRT-3 and GRT-4 (QR-9).
   - RC-W's W-b and W-d reproduce P:499 (QR-6).
4. **Inventory.**
   - It is exact.
   - It is closed relative to a search that is not recorded.
   - It has three gaps worth closing: GR:418, GR:571 and GR:701 (QR-15).
   - The K3 uses that are not rows cannot be fed to GRT-4 (QR-8).
   - The late-passage rule is sound.
5. **Definitions.**
   - The role test is presentation-dependent (QR-1).
   - The words "metric volume" make every density M (QR-11).
   - A1q is too broad (QR-13).
   - Statements of non-sourcing have no value (QR-12).
   - The ⊳_G vocabulary of A5g is narrow but workable (QR-26).
6. **Invariants and checkpoints.**
   - X-5(iii) conflicts with naming rejecting rows.
   - X-11 checks one direction only.
   - Several asserted properties have no checkpoint (QR-16).
7. **Productivity, freeze and deviations.**
   - The productivity baseline omits r5's determinate carve verdicts (QR-18).
   - The deviation rule needs an Und default (QR-17).
   - The freeze rule is adequate once OQ-5 is answered.
8. **Owner questions.** See §5.
9. **Provenance.** The risk is real. Four features lean the same way, toward coexistence (C):
   - the default for unhedged assertions;
   - a hedging vocabulary that tracks phrases quoted in r5;
   - D-9, motivated by a passage;
   - Δ8, a writer addition.

   None of this shows bad faith. All of it is repairable by QR-2, QR-21 and the blind second reader of
   QR-6.

***

## 4. Findings

### Blocking

#### QR-1. The role test is keyed to presentation, which contradicts F4's invariant statement

**Where.** P:341–343 (T test); P:197 (`Dom(F4)`); P:305–306 (route-dependent role for W0 only); N:107.

**Evidence.**

- The T test fires when a passage "places it on the source side of a displayed or verbally stated field
  equation". A term on the geometric side receives T only if it is also called a source.
  - Example: a constant `Λ g_μν` written beside the Einstein tensor.
- Such a term is then outside `Dom(F4)` = role T or IC, unless it is called an integration constant.
- r5 rejects exactly this. A side-keyed F4 "would classify a presentation, not a law" (r5:416–419, node F4-1).
  F4 is therefore stated on "every term of the realized equation other than the Einstein tensor", and r5
  F4-6 applies it to "the Λ term of SM:162".
- The witness's own law carries `Λ^Z g` on the left and `−ρ_Z g` on the right (U2Ar3:342). The class
  𝒞_div puts Λ on the left by definition (U1r5:198–199).
- As written, then, membership in `Dom(F4)` would turn on how an equation happens to be typeset. That is a
  hidden attribute that can separate rows I-SYM means to treat alike.
- The route-dependent role (P:305–306) is stated for W0 rows only. The same principle should be stated for
  every row.

**Replacement.** Replace the T and IC bullets of §5.1's test (P:341–344) with:

> - T if the quantity is a term of a displayed or verbally stated field equation of the realized metric,
>   other than the Einstein tensor, on either side as presented (r5 §3.4, node F4-1); or if a passage says
>   it "sources", "is a (gravitational) source" or "source term", "gravitates", "is gravitationally
>   active", "feeds back as a source", or is converted "into curvature". The side as presented is recorded
>   in A1s (left, right, verbal) for information only. A1s enters no predicate.
> - IC if it is called an integration constant, or the datum that fixes one. For a quantity and route on
>   which both T and IC hold, the role is IC.
> - Where the passages on a quantity state its role per route (a divergence-free sourcing law, or the
>   Jacobson route), the role is recorded per route. This applies to every row, corpus or constructed.

At P:305–306, replace the bullet with "Their role is computed per route under §5.1's per-route clause,
because the route is not a premise (§2.2)."

Add a text control (QR-9, TX-6) with `G_μν + Λ g_μν = 8πG T_μν`, Λ a fixed constant; required values: Λ
has A1 = T, A1c = uniform and A2 = X.

#### QR-2. Unhedged assertions default to non-commitment, and the status word map is asymmetric

**Where.** P:397–423 (A3 values, word map, aggregation); P:483–496 (rejecting predicates); P:427–428 (an
example of D); N:107 (D-9).

**Evidence.**

- A sourcing statement made in the corpus's own voice with no status word, and no inherited status note,
  gets Ns. Ns is in neither the rejecting set nor the potentially rejecting set (P:483–489). It therefore
  behaves exactly like Ps.
- That settles, by a default the text never states, what QB5(a) asks: "taken on the corpus's own sourcing
  commitments". Only explicitly status-marked text can then reject F4.
- r5's premise base is "the text … as cited, with its stated status" (r5:156). An unqualified assertion is
  stated text.
- The word map's hedging side includes "structural reading", "not presently derived" and "does not
  adjudicate". Those are phrasings the writer read in r5's quotations. Its commitment side is generic and
  omits common status vocabulary: "established", "shown", "lemma", "corollary", "forced", "necessary".
  AGENTS.md uses "established" as the status word (§A.27: "State what is established"), and §A.25 lists
  "theorem / derived / forced / open / hypothesis / conditional / retrodiction".
- Aggregation is defined only for Conflict (P:420–423). D with Ns, D with D|cond, and the hedges among
  themselves are not specified.
- F5's rejecting predicate reads "its grounding status ∈ {D, D|cond, Rq}" (P:493). The same default
  therefore governs grounding commitments, and the fix must apply to both sides.
- The example at P:427–428 is itself scope-ambiguous. "derived from the Stefan–Boltzmann law" naturally
  attaches to the value.

**Replacement.**

1. Add an A3 value after Ns (P:404):

   > - As: asserted in the corpus's own voice, with no status word in scope and no inherited status note
   >   whose scope includes the source role.

   Ns then means: the passage states nothing about the quantity's source role.

2. Replace the word map (P:411–418) with this one, drawn from AGENTS.md §A.25 and §A.33 and not from
   inventory phrasing:

   > - D: "derived", "proved", "theorem", "lemma", "corollary", "established", "shown", "follows from",
   >   "is a consequence of" a stated derivation.
   > - D|cond: a D word with "conditional on …" or "under …" naming conditions, or an inherited status
   >   note naming conditions.
   > - Rq: "requires", "is required", "must", "forced", "forces", "necessary".
   > - Ps: "proposal", "posit", "posited", "hypothesis", "reading", "taken as", "assumed",
   >   "on the … proposal".
   > - In: "input", "imported", "taken from experiment", "fitted", "retrodiction".
   > - ND: "not derived", "not presently derived", "not established".
   > - Op: "open", "not settled", "undecided", "not adjudicated", "does not adjudicate", "conjecture".

3. Replace the aggregation bullet (P:420–423) with:

   > - **Aggregation per quantity.** Commitment values are D, D|cond, Rq and As. Hedge values are Ps, In,
   >   ND and Op.
   >   - If any row gives a commitment value and any row gives a hedge value, the value is Conflict, and
   >     the conflict is recorded as a finding.
   >   - Otherwise, if any row gives a commitment value, the value is D|cond if any row gives D|cond, with
   >     the union of the named conditions; else D or Rq if any row gives one; else As.
   >   - Otherwise, the value is the hedge value or values given, or Ns if every row gives Ns.

4. In §6.3, replace "A3 ∈ {D, D|cond, Rq}" (P:484, P:488) and "its grounding status ∈ {D, D|cond, Rq}"
   (P:493) with "∈ {D, D|cond, Rq, As}". Add:

   > - A verdict whose only rejecting rows have As is labelled "rests on unqualified assertion".

5. Put the treatment of As to the owner as **OQ-7** (§5). If the owner rejects As as a commitment, the
   fallback is that As makes a row potentially rejecting, never non-rejecting. As must not be equivalent
   to Ns unless a reason is stated.
6. Replace the D example (P:427–428) with two examples:

   > - "That radiation enters the Friedmann equation as a source is derived from the Einstein equation with
   >   the perfect-fluid stress tensor": D, and the scope includes the source role.
   > - "The radiation density is derived from the Stefan–Boltzmann law": D in A3v; no A3 status.

7. Remove D-9's reference to an inventory passage (QR-21).

Add the flip X11 (QR-9): TC-N, n2's status Ps → As. Required: C → R if OQ-7 adopts As as a commitment, or
C → U under the fallback.

#### QR-3. Carves are not all predicates on attribute values, and Δ9 is an open slot

**Where.** P:113–114 (I-SYM); P:525–544 (§7.2); P:198–200; P:798 (Q-6); X-6(iii) at P:852.

**Evidence.**

- I-SYM requires every carve to be "a predicate on attribute values". Several are not:
  - Δ1, "partition-defined", has no §5 attribute.
  - Δ7, "emergent against classical", is not mapped to one either. M-em is the nearest.
  - Δ9 is "any further reason-bearing difference stated in an inventory row". That is a schema, enumerated
    at execution, after the corpus has been read.
- Class membership of the witness under Δ1, Δ7 and Δ9 would therefore be a judgment made at execution, with
  the witness's attributes known from r5.
- Δ9 also makes R's negative ("no carve passes") a negative over an unenumerated set. And Δ9 instances are
  not deviations, so they can change a verdict without an amendment. The rule otherwise closes that route
  (§7.2, last bullet).

**Replacement.**

1. Add an attribute to §5.2:

   > - **A2p, partition-definedness.** Yes if an argument of the definiens is the partition Π(g) of GR:40,
   >   its boundary, or a set or count it selects. No if the definiens is C or X, or if it is M with no such
   >   argument. Und otherwise.
   >   - Examples outside the inventory: the count of modes inside an observer's causal horizon is yes; the
   >     Ricci scalar at a point is no; an electron's rest energy is no.

2. Add a predicate column to the §7.2 table:

   | Δ | `class(Δ)` (predicate on §5 attributes) |
   |---|---|
   | Δ1 | A2p = yes |
   | Δ2 | A1q = yes |
   | Δ3 | A1 = IC |
   | Δ4 | A1c = uniform |
   | Δ5 | A2 ∈ {M-geo, M-set, M-em, M-pure} |
   | Δ6 | A2§ filled |
   | Δ7 | A2 = M-em |
   | Δ8 | A2 = M-pure |
   | Δ9.k | as enumerated at Q-6a: a Boolean combination of the attributes above |

   Membership is Und where a predicate's attribute is Und.

3. Replace Δ9's row with "Δ9.k: each reason enumerated at node Q-6a". Add a node before Q-6:

   > **Q-6a (enumeration, committed before any GRT verdict).**
   > - List every sentence of a §4.2 row that contains a reason connective ("because", "since",
   >   "therefore", "hence", "so", "in virtue of", "as a consequence", "is a property of … and therefore")
   >   and whose conclusion is that a quantity does or does not source, gravitate, ground, or enter the
   >   field equation.
   > - For each sentence, write the predicate it induces as a Boolean combination of §5's attributes.
   > - A predicate equal to one of Δ1–Δ8's is merged with it.
   > - A reason that cannot be written on §5's attributes is a deviation (§14.2), with a sensitivity line.
   > - The list lands in a commit before Q-6.

4. At X-6(iii), replace "Every carve is one of Δ1–Δ9" with "Every carve is one of Δ1–Δ8 or Δ9.k as
   committed at Q-6a".

#### QR-4. A slice-local definiens is spared under every variant, which builds F4-3's diachronic variant into synchronic F4

**Where.** P:373–377 (A2t); P:474–476 (§6.2); P:152–153; N:108 (D-8).

**Evidence.**

- The premise base carries r5's diachronic reading with two conditions: "with a slice-local partition *and
  diachronic relata*, the cycle does not close" (P:152–153; r5 node F4-3, r5:541–547).
- Diachronic relata are a property of the formalization: F4 "taken diachronically", with energy content at
  `s` grounding curvature at `s′ > s`.
- r5 §3.4 states F4 synchronically, and every formalization in §3 is r5's F4 or a restriction of it.
- Yet §6.2 sets U[v, b] = N whenever A2t is slice-local, for every v. For synchronic F4,
  `g(s) ⊳_G t(s) ⊳_G g(s)` closes whether or not the definiens is slice-local.
- D-8's "a per-row fact" holds for slice-locality, not for the relata. As written, every variant silently
  gets the diachronic exemption. That moves decisive U cells toward N, the coexistence direction.

**Replacement.** Replace the first two rows of the §6.2 table with:

| Condition | U[v, b] |
|---|---|
| The quantity is in `Dom(v)`, its definiens in branch b is M, and either A2t is closing, or A2t is slice-local and v's relata are synchronic | Y |
| The quantity is not in `Dom(v)`; or its definiens in branch b is C or X; or A2t is slice-local and v's relata are diachronic | N |

Add to §3:

> Every formalization above is synchronic (r5 §3.4).

If the diachronic variant is wanted, add a row as well:

> | F4-dia | r5 node F4-3: F4 with diachronic relata | as F4 |

It is sorted at Stage 3 like any formalization, and its verdict is reported beside F5's. Amend D-8
accordingly. Add the flip X6 (QR-9).

#### QR-5. No rule combines the per-branch, per-route and per-convention results into the headline

**Where.** P:567 (summary class per branch); P:589–607 (Stage 3 per branch, per route and per W0 row);
P:298–302 (three W0 rows).

**Evidence.**

- Stage 2 yields a class for β0 and for β1.
- Stage 3 yields an outcome for each combination of branch (2), route (2) and W0 row (3): twelve in all.
- No clause says what the unit's verdict is when these differ. That leaves the executor a free choice after
  the results are known, which is the selection the owner's guidance forbids.
- β1 rests on a posit (U1r5:504–505). The route is not a premise. The three conventions are alternative
  constructions of one witness.

**Replacement.** Add §8.4:

> **8.4 Headline.**
> - The Stage-2 class is reported per branch. If the two branches agree, that class is the headline class.
>   Otherwise the headline states "branch-dependent", with both classes.
> - The B_G outcome is reported per cell of the grid: branch {β0, β1} × route {𝒞_div, Jacobson} × W0 row
>   {Z0, ZI, ZII}.
> - The headline outcome is X if every cell returns X. Otherwise it is (C), with the grid shown and the
>   deciding coordinates named.
> - No coordinate may be selected to break a disagreement. β1 rests on the geometry-first posit, the route
>   is not a premise, and no convention is preferred.

Add the matching checkpoint X-21 (QR-16).

#### QR-6. RC-W cannot fail, and nothing tests where tuning to the witness can enter

**Where.** P:745–767 (RC-W); P:117–130 (I-BLIND); X-6 at P:852; N:118–120.

**Evidence.**

- W-b and W-d pass because §6.3 says "a row with A3 = Cx never satisfies a rejecting … predicate" (P:499),
  whatever else the rule does. They reproduce a clause of the rule. AGENTS.md: "A computational verdict is
  invalid if a required control … merely reproduces the claimed formula."
- W-a catches only a clause that names a row. X-5(iii) already forbids that syntactically.
- W-c is a real test, but only of GRT-1 against an attribute with no grounding reason.
- A rule tuned to the witness would not reach the witness through Stage 2's rejecting predicates. It would
  work through three things written by someone who knows the witness's attributes:
  - the attribute tests;
  - the candidate carves;
  - how GRT is judged.

  None of the controls touches these.
- X-7 fixes the order of the record. It cannot make the executor blind, because r5 states the witness's
  attributes.

**Replacement.**

1. Rename W-b and W-d "Cx-clause consistency checks". Keep them, but do not count them as countercontrols.
2. Add W-e (status-blindness of the predicates):

   > - **W-e (status-blindness of the predicates).**
   >   - Toy TC-M has rows m1 and m2 with identical attribute vectors except A3: m1 is D and m2 is Cx.
   >   - Required:
   >     - for every carve predicate Δ1–Δ8 (and each Δ9.k once enumerated), m1 ∈ `class(Δ)` if and only
   >       if m2 ∈ `class(Δ)`;
   >     - for every v, U[v](m1) = U[v](m2);
   >     - m1 is rejecting for v exactly when U[v](m2) = Y.
   >   - The control fails if any carve predicate or U reads A3, a row's identity or the witness tag.

3. Add a checkpoint for a blind second reading:

   > | X-18 | The attribute cells do not depend on the executor's prior readings | After Q-4 and before the Stage-2 commit, a second reader classifies every A1, A1c, A1q, A2, A2t, A2p, A2§, A3 and A5g cell of every §4.2 row, from the frozen tests and the cited corpus lines only. The second reader has not read r5 §0, §2.4 or §6–§9, CONFIRM-BG-r2 to r4, NOTES-BG-r1 to r5, or the executor's table, and classifies the text controls (QR-9) first. Disagreements are reconciled once, by citation. A cell still in disagreement is Und. The second reading lands in the Stage-2 commit, and the reviewer checks that it is complete. |

#### QR-7. TC-U has no witness row, so RC-U's Stage-3 requirement cannot be computed

**Where.** P:683–691 (TC-U); P:771 (RC-U).

**Evidence.** Stage 3 sorts each formalization by whether "the W0 row's quantity is in `Dom(v)`" (P:592–594).
TC-U contains only u1, so the "(C)" claimed at P:690–691 has no derivation. Under P:720–722 RC-U is red as
written.

**Replacement.**

1. Add a row to the TC-U table:

   | Row | Role | Comp | Def | St | Gc | U[F4] |
   |---|---|---|---|---|---|---|
   | w* | T | full | M (closing) | Cx | No | Y |

2. Replace the Stage-3 bullet with:

   > - **Stage 3.** Resolving u1 to M gives R. F5 is Admissible, so the outcome is (B). Resolving u1 to C
   >   gives C. F4 is then grounding-content (w* is in its domain), F5 is Admissible, and the outcome is (C).
   >   The resolutions disagree, so the outcome is **(C)**, with u1's A2 named.

### Should-fix

#### QR-8. GRT-4's "agrees" is undefined, the K3 uses cannot be fed to it, and "every row" includes W0

**Where.** P:516–518; P:289–293; P:798.

**Evidence.**

- Two readers can apply "the class agrees with each corpus use" differently.
- The K3 uses that are not rows (GR:340, GR:342, GR:346, Substratum.md:385–393) are "read for K3 only", but
  a predicate on attribute values needs attributes to read.
- "every row" includes the W0 rows, which are not classified until Q-8, after GRT.

**Replacement.** Replace GRT-4 with:

> - **GRT-4 (K3, uniformity).** State the carve's reason as a claim R_Δ about every item in `class(Δ)`.
>   - GRT-4 fails if some corpus row or K3 use x, not on the excluded list, satisfies (a) or (b), and no
>     further difference passing GRT-1 to GRT-3 is stated for x:
>     - (a) x is in `class(Δ)`, and a passage on x states, in its own vocabulary, the negation of what R_Δ
>       states of x;
>     - (b) x is outside `class(Δ)`, and a passage on x states of x what R_Δ states of the class.
>   - GRT-4 is Und if (a) or (b) turns on an Und attribute.
>   - It is applied to the §4.2 rows and to Group K. It is never applied to W0 rows.

Add **Group K**: the K3 uses of §4.3 that are not already rows, classified at Q-4 like every row. Add to
§5.3:

> - A row whose own passage is on §2.2's excluded list has A3x = yes.

#### QR-9. No rule-level control exercises the §5 tests, and several sensitivities have no flip

**Where.** §9–§10 (P:627–783).

**Evidence.**

- Every toy stipulates its attribute values. The controls therefore test §6–§8 and never the per-term
  tests, which is where judgment enters.
- Some broken rules pass every control as written:
  - a rule that ignores role (n3 and n4 are non-rejecting on status anyway);
  - a rule that ignores A3x;
  - a rule that treats Conflict as admissible;
  - a GRT that never applies GRT-2, GRT-3 or GRT-4.

**Replacement.** Add §10.7, with required values preregistered now. The executor (at Q-0) and the second
reader (X-18) must both return them; any miss halts the unit as a rule defect.

> **10.7 RC-T (text controls; constructed sentences outside the inventory).**
>
> | ID | Sentence | Required |
> |---|---|---|
> | TX-1 | "That radiation enters the Friedmann equation as a source is derived from the Einstein equation with the perfect-fluid stress tensor." | A1 T; A3 D |
> | TX-2 | "The radiation density is derived from the Stefan–Boltzmann law." | D in A3v only; A3 Ns |
> | TX-3 | "The scalar's gradient energy gravitates." | A1 T; A3 As |
> | TX-4 | "We take the dark fluid to gravitate, with w = −1." | A1 T; A3 Ps |
> | TX-5 | "Whether the axion background sources curvature is not settled here." | A3 Op |
> | TX-6 | "G_μν + Λ g_μν = 8πG T_μν, with Λ a fixed constant." | Λ: A1 T, A1c uniform, A2 X |
> | TX-7 | "In unimodular gravity Λ is an integration constant." | A1 IC |
> | TX-8 | "The number of modes inside the observer's horizon." | A2 M-set; A2p yes |
> | TX-9 | "Dust with rest-energy density ρ = n m c²." | A2 C (QR-11) |
> | TX-10 | "The total energy inside the Hubble volume, divided by that volume." | A2 M-geo |
> | TX-11 | "The field's energy is that in virtue of which spacetime curves." / "Matter tells spacetime how to curve." | A5g Yes / No |
> | TX-12 | "The bare zero-point energy does not source curvature." | A1 NS (QR-12) |
> | TX-13 | "The Komar mass of the solution." | A1q yes; no role T |

Add these flips to §10.3:

| Flip | From | To (required) |
|---|---|---|
| X5: TC-R, p1's role T → Dep | R | C |
| X6: TC-R, p1's A2t closing → slice-local | R | R (every variant is synchronic; QR-4). C for F4-dia, if it is adopted |
| X7: TC-R, p1's A3x no → yes | R | C |
| X8: TC-R, p1's A3 D → Conflict | R | U |
| X9: TC-C, Ax-κ replaced by a toy axiom on the toy's excluded list | Cc | R (GRT-2) |
| X10: TC-C, Ax-κ replaced by "c1's value covaries with the toy curvature" | Cc | R (GRT-3) |
| X11: TC-N, n2's A3 Ps → As | C | R, or U under OQ-7's fallback |
| X12: TC-C, a toy row c3 that Ax-κ's reason covers, added outside `class(Δκ)` | Cc | R (GRT-4(b) or GRT-5) |

The writer should check that no TX sentence paraphrases an inventory sentence, and replace any that does.

#### QR-10. `Dom(F4-null)` is not mapped from A1c

**Where.** P:199; P:335–339.

**Evidence.** "Full (general symmetric tensor or energy density)" lumps two cases together. The null–null
component of a scalar energy density with no stated pressure is undetermined: `(ρ + p)(u·k)²` vanishes at
`w = −1`.

**Replacement.**

1. Split A1c's full value into "full-tensor" and "density-only".
2. Replace F4-null's domain with:

   > role T or IC, and A1c ∈ {full-tensor, null-flux}. A1c = uniform is outside. A1c ∈ {density-only,
   > unstated} gives Und.

#### QR-11. "A metric volume" makes every energy density M

**Where.** P:360; P:368–372.

**Evidence.** Any density is energy per volume, and any volume is metric. Read literally, dust is M, which
contradicts the toys (dust is C) and r5's treatment of `T^cl` (r5:422–423). Two readers will draw the line
in different places.

**Replacement.** Add to §5.2's test:

> - The metric entering only as the measure or normalization that expresses a microstate-defined energy as
>   a local density or tensor does not make the quantity M. That covers:
>   - the proper volume element at a point;
>   - the normalization of a 4-velocity;
>   - raising and lowering indices.
> - The following do make it M:
>   - a metric volume of a region selected by the metric (a horizon volume, a Hubble volume);
>   - curvature, H, or any derivative of the metric;
>   - a horizon;
>   - the partition.

Add TX-9 and TX-10 (QR-9).

#### QR-12. Statements of non-sourcing have no value, and role aggregation discards them

**Where.** P:327–347; P:241 (the inventory itself locates a "non-sourcing clause").

**Evidence.**

- A1 has no value for "the quantity does not source", and A3 reads status only for the source role.
- "Role is aggregated per quantity: T if any row gives T" (P:346) therefore discards an explicit statement
  of non-sourcing.
- The rule also does not say how a statement made explicitly on the geometry-first proposal enters β0.

**Replacement.**

1. Add an A1 value:

   > - NS: a passage states that the quantity does not source, gravitate or enter the field equation. Its
   >   status is read by §5.3, with "non-sourcing" in place of "source role".

2. Add an aggregation rule:

   > - T and NS on one quantity give role Conflict-R, and `Dom(v)` membership is Und, unless the two are
   >   scoped to different branches.

3. Add a branch rule to §6.1:

   > - A statement explicitly conditional on the geometry-first proposal (U1r5:504–505) enters β1 only.
   >   In β0 it is recorded and has no role.

#### QR-13. A1q is broad enough to fit almost any derived quantity

**Where.** P:333–334.

**Evidence.** "A consequence of a law or relation applied to a given solution" covers nearly any quantity
computed from anything. Δ2's class (A1q = yes) then has no definite extension.

**Replacement.**

> **A1q.** Yes if a passage states the quantity's value or identity as obtained by evaluating a law of the
> gravitational dynamics, as the passage identifies it, on a given solution. Examples: the Komar mass and
> the ADM energy are yes; a radiation density from the Stefan–Boltzmann law is no.

#### QR-14. Nodes Q-2 and Q-3 need attributes that Q-4 produces

**Where.** P:794–796.

**Evidence.** Q-2 uses "the A1c of the rows with role T and A3 ∈ {D, Rq}". Q-3 uses A2§. Both run before
Q-4, which classifies the rows.

**Replacement.**

- Move Q-4 before Q-2.
- In Q-2, read "A3 ∈ {D, D|cond, Rq, As}" (QR-2).

#### QR-15. Inventory: three gaps, and no record of the search that closes it

**Where.** P:224–287; N:84–90.

**Evidence** (location only).

- **GR:418.** It is the statement of the Corollary whose proof steps are T-GR422 to T-GR426 and C-GR444
  (GR:420 heads that proof). Status is read by inheritance from enclosing statements (P:419), so the
  statement of the result itself should be a row.
- **GR:571.** It is the one non-blank paragraph of §8.3 (GR:567–581) without a row, while GR:569 and
  GR:573–581 have rows for Q4.
- **GR:701.** It names "the covariant Level-G3 target equation (§7)", which bears on Q5. GR:689–697 (§8.7)
  is represented by :691 and :697 only.
- NOTES records the lines read, but not the search that makes the inventory closed. Status notes reached by
  inheritance are not listed.

**Replacement.**

- Add C-GR418 to Group C, E-GR571 to Group Q (Q4), and G-GR701 to Group Q (Q5).
- Either add GR:693 and GR:695 or state why they are omitted.
- Record in NOTES the search patterns used to build the inventory and the hits that were excluded, each
  with a reason.
- At Q-4, list every line read through §5.3's inheritance clause, as cited lines rather than rows.

#### QR-16. Checkpoint table: one conflict, one asymmetry, and asserted properties with no checkpoint

**Where.** P:845–863.

- **X-5(iii).** Stage-2 verdicts must name their rejecting rows, so a grep for row IDs in the Stage-2 text
  will hit. Replace it with:

  > (iii) A grep of the Stage-2 text for `W0`, `w*`, `ρ_Z`, `K_cpl` and "witness" finds nothing. Corpus row
  > IDs may appear.

- **X-11.** It spot-checks D and Rq cells only. Cells that keep F4 admissible are exempt, so the check runs
  in one direction. Replace it with:

  > The reviewer checks every A3 cell that decides a verdict, whatever its value, and all D, D|cond, Rq and
  > As cells.

- **Add:**
  - **X-18,** the blind second reading (QR-6).
  - **X-19.** The same-quantity table (P:219–220) and the Q-6a enumeration land in commits before any
    derived cell and before any GRT verdict, respectively. Checked from the history.
  - **X-20.** Skeptical-node completeness. The record lists every cell whose flip changes a Stage-2
    verdict, and gives a node for each favourable one. The reviewer recomputes the list by flipping cells.
  - **X-21.** Stage 3 and the §8.4 headline (QR-5) are recomputed by the reviewer from the Stage-2 commit
    and the W0 rows.
  - **X-22.** RC-T (QR-9) is green at Q-0, for the executor and for the second reader.
- **X-16.** "No premise adopted" is not measured by `git diff`. Add:

  > and every decisive step's premise list (X-9) contains only §2.1 items.

#### QR-17. Deviations: a test that cannot be applied needs an Und default

**Where.** P:885–886; P:891–899.

**Evidence.** "A test that cannot be applied as written" is a deviation, but the rule does not say what the
cell then becomes. That leaves room for a substitute test chosen during execution.

**Replacement.**

- Add to §14.2:

  > - A test that cannot be applied as written gives Und for the cell. No substitute test enters the
  >   decisive table. A substitute may be shown in the sensitivity line.

- Replace P:898–899 with:

  > - Every amendment after F needs independent review before it takes effect. One written after any
  >   Stage-2 cell has been rendered also needs a recorded owner decision.

#### QR-18. Productivity baseline: list r5's determinate items, so that restating them does not count

**Where.** P:822–838.

**Evidence.**

- r5 already gives determinate verdicts on several carve candidates:
  - partition-definedness does not yield an F4-c, and removing `ρ_Z` from it fails K3;
  - "emergent against classical" fails K4;
  - "a consequence of the law" covers `ρ_s` only.
- r5 also has uniform F4 and F5 admissible (r5:217–222, r5:593–609).
- Clause (a) counts "a carve passing or failing GRT" and "a Stage-2 verdict on uniform F4". Restating
  these verdicts would satisfy it.

**Replacement.** Add to the baseline:

> r5's determinate verdicts: uniform F4 admissible; F5 admissible; partition-definedness and
> emergent-against-classical failing as F4-c candidates; consequence-of-the-law covering `ρ_s` only. An
> item counts under (a) only if it is absent from this list or differs from it.

#### QR-19. State the rule's structural properties in the preregistration

**Where.** P:542–544; P:659–661; §8.

**Evidence.** Three properties follow from the rule [A] and bear on how its outcome reads. None is stated.

- (A) requires F5 to be Rejected. That needs a row with A5g = Yes and a grounding status in the commitment
  set, or a failed F5 control.
- A scope variant with no stated reason (F4-law, F4-null) fails GRT-1 and is Rejected. This changes r5,
  where F4-null was a formalization whose "controls are not assessed" (r5:709–711).
- Any Und in a decisive cell of a committed row gives U.

**Replacement.** Add §8.5:

> **8.5 Properties of the rule [A].**
> - (i) (A) requires F5 to be Rejected, by a row with A5g = Yes and a grounding status in
>   {D, D|cond, Rq, As}, or by a failed F5 control.
> - (ii) A scope or carve variant with no stated reason is Rejected by GRT-1. This applies to F4-law and
>   F4-null alike, and it changes r5's treatment of F4-null.
> - (iii) F4 is Admissible only if no committed row in its domain has an Und decisive cell; otherwise the
>   class is at best U.
> - (iv) (C) is the outcome in each case listed in §8.3's table and wherever §8.4's grid disagrees.

#### QR-20. The owner guidance is now on record: cite it

**Where.** P:17–20; N:26–40; N:149; OQ-6 at P:935–937.

**Evidence.** #873 c.6872277416 (`amaybaum`, 2026-11-14T05:17:28Z) records the guidance verbatim: "G3
QB5(a): The preregistration-first approach is essential. The decision rule must apply equally to the
corpus's own metric-dependent source terms and the disputed vacuum-offset coupling, without selecting F4 or
F5 to obtain a preferred result." It also records: "Physical source remains NOT PASSED; G3 remains (C)."

**Replacement.**

- At P:17–19, write: "**Owner guidance,** #873 comment 6872277416 (`amaybaum`, 2026-11-14T05:17:28Z)", and
  quote both sentences.
- In NOTES §2 and §6, reclassify the guidance as on record.
- Withdraw OQ-6.

#### QR-21. Provenance: remove clauses motivated by a passage, and justify Δ8 on its own

**Where.** N:107 (D-9); N:102 (D-4); N:118–120.

**Evidence.**

- D-9 justifies the general scope test by r5's reading of one inventory passage, GR:374's "requires".
  That is a cell reading of an inventory row, used as the rationale of a rule, and X-13 bars that kind of
  anchoring. The test itself is reasonable on external grounds, and P:429 gives one external example.
- Δ8 is the writer's addition (D-4). Its source, F4's exemption of the Einstein tensor, is legitimate. But
  the writer knew from r5 which side of Δ8 the witness falls on.
- NOTES' own limit (N:118–120) is accurate.

**Replacement.**

- Replace D-9's reason with:

  > A status word attaches to what it modifies. The external examples at P:427–431 fix the test.

- Add to D-4:

  > Δ8 is a writer addition. Its candidacy rests on F4's statement alone, and GRT decides it.

- Rely on X-18 (QR-6) as the check on all cells.

### Nits

- **QR-22. Toy carve naming** (P:672–674). TC-C's Δκ is Δ8 in the toy. Say so, and state that TC-C has no
  K3 uses, so GRT-4 is satisfied vacuously.
- **QR-23. RC-P wording** (P:728). Replace "must return class R for F4, F4-law and F4-null" with "must
  return class R, with F4, F4-law and F4-null each Rejected".
- **QR-24. Same quantity** (P:217–219). Add "or names it by the same defined phrase". Rename T-GR482 to
  C-GR482 (P:284), since it sits in Group C.
- **QR-25. The §8.3 table** (P:618–619) omits two cases in which the W0 quantity is outside `Dom(F4)`:
  - in the "C | Admissible" row, say what follows: (B) if no grounding-content variant is Admissible or
    Undetermined;
  - the "C | Rejected" row needs the same case.

  In §2.1, add "general form only" after the set-level reading (P:149–151), as is done for Lemma U.
- **QR-26. A5g's paraphrases.**
  - List the treatment of "because", "due to", "arises from", "emerges from", "results from", "determined
    by" and "a property of". The recommendation is sourcing or justificatory vocabulary (No), unless both
    relata are quantities and the phrase is one of P:441–442's forms.
  - NOTES §1 says neither file is committed. Both are committed at `2e18a2df`. This is CONFIRM-BG-r3
    CF-7's pattern recurring, so the next NOTES should record the commit state as of the time it is read.

***

## 5. Owner questions

**OQ-1 (QB7(a)'s scope). Recommend the writer's reading, with a sensitivity line.**

- The owner's words are "Do not adopt running-vacuum sourcing as a premise."
- "Adopt" names an act of taking the sourcing on by decision, or importing it. The writer's reading bars
  exactly that (X-10), and it reads the channel's status from the text by the test every row receives.
- That reading is consistent with the owner's words, and with c.6872004336's instruction to "test the
  framework's own gravitational source terms against F4". The running-vacuum passages are among QB5(a)'s
  listed source terms.
- The alternative reading bars those rows from rejecting F4 whatever the text says. That is a row-identity
  exemption, the form W-c's decoy is built to reject, and it would decide the coexistence direction by
  decree.
- One qualifier is needed. The owner answered QB7(a) on r5's reading that the text does not commit to the
  sourcing (r5:94–97, r5:636–650). A finding that the text does commit departs from the reading on which
  the decision was made. Add to §8.2:

  > If a Stage-2 verdict would differ were the A3 cells of the rows that the same-quantity table identifies
  > with GR:376's `Λ_eff(H)` or with GR:400 Reading 1's quantity non-committal, the verdict is reported with
  > that sensitivity line, labelled "rests on the corpus text's commitment to running-vacuum sourcing
  > (QB7(a))".

  The owner then sees whether QB7(a) is being reached through the text.

**OQ-2 (GRT, Δ1–Δ9, relativity). Accept, after QR-3, QR-8 and QR-19.**

- Relativity to a frozen, finite list on both sides is better than r5's open schema, which made (B) depend
  on an open universal negative (CONFIRM-BG-r4 DF-2).
- Each verdict must carry the relativity, as P:583 requires.
- The owner should accept explicitly that a scope variant with no stated reason is Rejected (QR-19 ii).
  That treats F4-law and F4-null alike, and it differs from r5.

**OQ-3 (carves containing the witness's term count as CoC-content). Accept.**

- This is r5 §1.2's content definition, relativized to the witness's term by R-6, applied to every carve.
  It is not an extension that needs a separate justification.
- Its consequence for (A) is real, and the mirror consequence should be stated beside it. If a carve whose
  class excludes a metric-defined W0 quantity passes GRT and is Admissible, it is grounding-content and
  blocks (B) in the same way.

**OQ-4 (inventory additions). Accept Groups V, Q and C, with QR-15's additions.**

- QR-15 adds C-GR418, E-GR571 and G-GR701, and asks for GR:693 and GR:695 to be added or their omission
  explained.
- QR-8 adds Group K.
- The search patterns should be recorded.
- Group V is required by the owner guidance. Groups Q and C are justified by Q3–Q6 and by r5's K3 and
  AW-entropic site lists.

**OQ-5 (freeze designation). Recommend owner designation on #873, after the reviewer's acceptance is
recorded.**

- The owner set the gate as passing independent preregistration review (c.6872004336, QB6).
- The plan recorded at c.6872277416 has the owner designating the freeze.
- Acceptance is the precondition, and designation is the owner's act. This is a paper-only unit, so no
  workflow dispatch is involved.

**OQ-6 (record of the guidance). Withdrawn as answered.** The guidance is at #873 c.6872277416 (QR-20).

**OQ-7 (new; QR-2). Does an unqualified assertion in the corpus's own voice count as a commitment?**

- **Recommendation: yes.** Treat As as a commitment, on both the sourcing side (F4) and the grounding side
  (F5). Label any verdict that rests only on As rows.
- **Reason.** r5's premise base is the corpus text "with its stated status". Hedges mark non-commitment,
  and the Conflict rule handles text that both asserts and hedges.
- **Fallback if the owner declines.** As makes a row potentially rejecting, never non-rejecting. Either way,
  the choice must be stated before F rather than left to a default.

***

## 6. Disposition

**REVISE.**

- **Before r2 can be accepted for freeze:**
  - Apply QR-1 to QR-7.
  - Have the owner answer OQ-1 to OQ-5 and OQ-7.
  - Re-run every rule-level control at r2, including RC-T and the new flips.
- **With them:** apply QR-8 to QR-21.
- **Nits:** QR-22 to QR-26 can go in with the rest.
- **Next review.** r2 needs a full review round, not a delta check, because QR-1 to QR-6 change the tests
  and the decision rule.

No inventory passage is classified in this review, and no expected outcome is stated. No manuscript change
is proposed, and no premise is adopted.
