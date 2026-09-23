# Substratum — A6 status adjudication: which label does the merged record support for the row `P1 — A6`? RESULT

## Outcome, in one line

**`AJ6-conditional`**, with `AJ5` finding a clause of the row's reasons not carried: the row
`P1 — A6` keeps `CONDITIONAL`, its reasons are written to the freeze's `ROW-conditional` text
character-for-character at `verification/ROADMAP.md:65`, and the row stays in the queue. The
`DERIVED` gate was run and did not open, on **both** of its halves. No departure fired.

**This round is type P throughout.** No Lean module, no definition, no theorem, no probe function
and no new guard tag were written. There is **no axiom table and no `#print axioms` line**, because
no Lean was written — stated in terms rather than left to be inferred. **No `sorry`, no `axiom`, no
`native_decide`** appears anywhere in the round's diff.

**This round is NON-SEALING, under `AGENTS.md` `§A.37`.** It owns the guard contracts asserting the
live row and the live label cell, and it owns no seal state. `_A6P_SEALED_HEAD`,
`_A6D_SEALED_HEAD`, `_A6I_SEALED_HEAD`, `_A6P_MERGE`, `_A6D_MERGE`, `_A6I_MERGE`, `_A6P_BASE`,
`_A6D_BASE` and `_A6I_BASE` were read and **never written**. The landing is `E` → `L`, **with no
archive-pin commit**: the round reserves no guard tag, adds no guard file and creates no pin state,
so there is nothing for a `P` commit to pin.

## The chronology control, checked at the mandated base

The execution branches from `c4ae9bfa907572c35ce18d93baeb250bbf100d67`, the merge commit of this
round's control plane (PR #637), and from nothing else.

**First act, performed before any target.** `git rev-parse
c4ae9bfa907572c35ce18d93baeb250bbf100d67:verification/programmes/substratum/a6-status-adjudication/preregistration.md`
returns `0f98c6a102fb69f98552a94e7af7214065e67947`, the blob the freeze names. **Confirmed.**

The freeze's clause 3 preconditions, each checked at the base:

| check | result |
| --- | --- |
| `git merge-base --is-ancestor 58100aea15eea8f5808b351d64163f55c9fed1bf HEAD` | exit `0` |
| `git merge-base --is-ancestor d0b8c6e83c32a01a586f947c0dfd9618a8b42a91 HEAD` | exit `0` |
| `git merge-base --is-ancestor 93405f3ff7eb4818a2895b5f5e2861094d9fe757 HEAD` | exit `0` |
| `_A6P_SEALED_HEAD = '58100aea15eea8f5808b351d64163f55c9fed1bf'` present character-for-character | `edge_rigidity_probe.py:15339` |
| `_A6D_SEALED_HEAD = 'd0b8c6e83c32a01a586f947c0dfd9618a8b42a91'` present character-for-character | `edge_rigidity_probe.py:17341` |
| `_A6I_SEALED_HEAD = '93405f3ff7eb4818a2895b5f5e2861094d9fe757'` present character-for-character | `edge_rigidity_probe.py:18031` |
| `AGENTS.md` carries `## §A.37 Round lifecycle: control plane, then execution and landing` | `AGENTS.md:647` |

All seven hold. No main merge, no rebase and no branch update was performed, and no result that
landed after `c4ae9bfa` was consumed — see the anti-contamination note in the discrepancy section.

## `AJ0` — locating controls

**Outcome: positive. Evidence type 1 (verbatim quotation from a pinned blob). Strength `full`**, as
predicted. Every passage the target enumerates was located at the base.

| object | coordinate at the base |
| --- | --- |
| `ROW` | `verification/ROADMAP.md:65` |
| `VOCAB`, seven entries | `verification/ROADMAP.md:24–30`, table at `:22–30` |
| the `ROADMAP` section `P1 — A6, and what is and is not already represented` | `verification/ROADMAP.md:474–587` |
| the propagation's `The ROADMAP label — the recommendation, with reasons` | `verification/audits/foundations/a6-covariance-propagation-audit.md:115–151` |
| round 2's `AS2 — the status determination` | `verification/programmes/substratum/a6-instantiation/result.md:304–336` |
| round 2's `What these outcomes do NOT license` | `verification/programmes/substratum/a6-instantiation/result.md:338–385` |
| round 2's `The ROADMAP propagation, and the re-pin that was NOT performed` | `verification/programmes/substratum/a6-instantiation/result.md:441–456` |
| round 2's freeze `What each outcome licenses for the row's label, and what it does not` | `verification/programmes/substratum/a6-instantiation/preregistration.md:576–…` |

**`_A6P_ROW`'s literal and its value.** The constant is a parenthesised string literal spanning
`verification/lean/edge_rigidity_probe.py:15468–15478` at the base, and its value was checked
programmatically to be **character-identical** both to the freeze's pinned row text and to the live
`verification/ROADMAP.md:65`. The three strings had not come apart. The clause consuming it is
`_a6p_roadmap`'s first conjunct, `_A6P_ROW in _r`, at `:15610`.

**`VOCAB`'s seven entries, quoted** (`verification/ROADMAP.md:24–30`):

- **`ACTIVE`** — "A round is running, or is **frozen and merged** and awaiting execution. A drafted
  or closed control plane is not a frozen one."
- **`OPEN`** — "A named obligation not closed at the required scope: no closing construction or
  theorem, and no impossibility theorem."
- **`GAP`** — "The manuscript states the condition, and the formal interface has **no predicate for
  it at all** — not a weak one, not an image. Closing it starts with defining the object."
- **`EXTERNAL`** — "A published result consumed as a cited premise."
- **`CONDITIONAL`** — "Formally present, carrying a named hypothesis this programme has not
  discharged. The manuscript states the hypothesis; the row tracks it."
- **`DERIVED`** — "Kernel-proved and propagated to the manuscript. Rows reach this state and then
  leave the queue."
- **`INDEPENDENT`** — "The kernel has **settled it negatively**: the resource is not sourced by the
  stated architecture."

## `AJ1` — what the label is conditional ON, quoted

**Outcome: positive. Evidence type 2 (verbatim quotation from a merged audit and from the pinned
`ROADMAP`). Strength `high`**, as predicted. The prediction that the two statements agree is
**confirmed at the headline and in the halves**; a further point on which they come apart is
reported below as a finding, not repaired.

The two statements are reported **separately and are not merged**.

### The propagation's statement of `COND`

`verification/audits/foundations/a6-covariance-propagation-audit.md:133–141`:

> **`CONDITIONAL`** — "Formally present, carrying a named hypothesis this programme has not
> discharged. The manuscript states the hypothesis; the row tracks it." — is exactly true. The
> predicate is formally present and proved. The named, undischarged hypothesis is **that the
> manuscripts' substratum instantiates the link-coupled interface on which `a6cov_all` is stated**:
> in its finite-alphabet half, that the `K = 6` link-coupled rule on `(ℤ/qℤ)^6`, packaged as a
> `Substratum`, is an instance — a packaging job the programme has not done; in its complex-lift
> half, that the covariance of `SM.md:112–114` holds on an interface the programme has not built.
> The manuscripts state the assumption itself, as the covariant interface, and the row tracks what
> separates that statement from a kernel statement about their object.

**Half 1, the packaging half, in the propagation's own words:** "that the `K = 6` link-coupled rule
on `(ℤ/qℤ)^6`, packaged as a `Substratum`, is an instance — a packaging job the programme has not
done".

**Half 2, the lift half, in the propagation's own words:** "that the covariance of `SM.md:112–114`
holds on an interface the programme has not built".

### The `ROADMAP` section's statement of `COND`

`verification/ROADMAP.md:494–498` at the base, the sentence pinned by `_A6P_ROAD_HYP`:

> The named hypothesis the row carries is that the manuscripts' substratum — the `K = 6`
> link-coupled rule on `(ℤ/qℤ)^6` and its complex lift — instantiates the link-coupled interface on
> which `a6cov_all` is stated. Discharging the first half is a packaging job on the finite alphabet;
> the second needs an interface the programme has not built.

**They agree.** Both name the same hypothesis — the substratum instantiates the link-coupled
interface — and both split it into the same two halves with the same content. The `ROADMAP`
section's parenthetical gloss "the `K = 6` link-coupled rule on `(ℤ/qℤ)^6` and its complex lift"
makes explicit that "the manuscripts' substratum" there denotes **the formal rule**, not the
physical object.

### The propagation's per-label reasoning, quoted

`verification/audits/foundations/a6-covariance-propagation-audit.md:119–132`:

- **`GAP`** — "'the formal interface has **no predicate for it at all**' — is false after adoption:
  `A6Cov` is the adopted predicate, defined and proved on the least interface."
- **`DERIVED`** — "'Kernel-proved and propagated to the manuscript' — would overclaim. What is
  kernel-proved is that `A6Cov` holds for every link-coupled rule of the interface. Nothing is
  proved of the manuscripts' substratum … 'The substratum satisfies A6' is therefore not a kernel
  statement, and a `DERIVED` row would say it is."
- **`OPEN`** — "'no closing construction or theorem' — misdescribes a row that has a closing theorem
  on the interface it is stated on."
- **`EXTERNAL`**, **`INDEPENDENT`**, **`ACTIVE`** — "do not apply."

### The propagation's recorded point of imperfect fit, quoted

`verification/audits/foundations/a6-covariance-propagation-audit.md:143–147`:

> One point of imperfect fit is recorded so that the owner sees it: the queue's other `CONDITIONAL`
> rows carry **physical** hypotheses (H-link, H-state), whereas this row's named hypothesis is one of
> **formalization scope**. The label is recommended anyway because it is the only one whose stated
> meaning is true of the row; the row text below names the hypothesis explicitly so that nobody reads
> the label as a physical premise the manuscripts have added.

### The separation this target keeps

**What the label tracks** and **what stands outside `A6Cov`** are two lists and are not merged. The
propagation's `COND`, in both halves, is a hypothesis of **formalization scope**. The §3.1 material
and the complex carrier's failure of `A1` appear nowhere in the propagation's statement of the
hypothesis; they are located under `AJ4-out` below.

## `AJ2` — the packaging half: what the record says about its discharge

**Outcome: positive — discharged, at evidence level 2. Evidence type 2. Strength `high`**, as
predicted.

**The organizing caveat, carried verbatim as status rule clause 12 requires:**

> Round 1 proved `a6cov_all : ∀ N M, A6Cov N M` — the adopted reading holds **identically** on every
> link-coupled rule of the interface, so its content is the covariant interface itself and not a
> constraint. A full positive therefore says exactly that the manuscripts' rule **is of that form**.
> It does **not** say that a nontrivial condition was tested and survived.

`verification/programmes/substratum/a6-instantiation/result.md:309–318`:

> **The packaging half.** It is discharged at evidence level 2: the manuscripts' six-fold
> link-coupled rule **is** packaged as a `Substratum` of the kernel's own structure with no field
> added — the cubic torus, the six-component alphabet over $\mathbb{Z}/q\mathbb{Z}$, the axis
> neighbourhood, the link-valued coupling as a parameter and the second-order term carried by the
> leap — the interface's link-coupled map **is** its update map (`PK2-a`), `A1`–`A5` hold of it
> (`PK3`, `A4Exact` under the translation-invariance hypothesis on the link coupling), its
> transformation class is larger than the singleton-index one (`PK4`), and the adopted reading holds
> of its own link data (`PK2-b`) — **and because the adopted reading holds identically on every
> link-coupled rule, what that last clause discharges is that the rule is of the covariant form, and
> not that a condition was tested and survived.**

The same finding is carried by the `ROADMAP` section at `:544–555`.

**The `A4Exact` hypothesis, reported with the conjunct it qualifies and never as a footnote to it.**
The conjunct is "`A1`–`A5` hold of it (`pk3a_A1`–`pk3e_A5`)", and the hypothesis qualifying its
`A4Exact` part is `∀ v i j, M (i + v) (j + v) = M i j`, the translation-invariance hypothesis on the
link coupling. The `ROADMAP` section states it in the same breath at `:549–551`: "`A1`–`A5` hold of
it (`pk3a_A1`–`pk3e_A5`, with `A4Exact` **under the translation-invariance hypothesis on the link
coupling**, `∀ v i j, M (i + v) (j + v) = M i j`, which is part of that statement and is reported
with it every time)".

**Named results carrying it:** `pk1_packaging`, `pk2a_bridge`, `pk3a_A1`–`pk3e_A5`,
`pk4_shift_not_scalar`, `pk2b_covariance`.

## `AJ3` — the lift half: what the record says about its discharge, and at what scope

**Outcome: positive, with the covariance statement discharged and the carrier proved outside.
Evidence type 2. Strength `high` on the split.** The **scope question** — whether the propagation's
own words for this half are answered by the covariance statement alone — is a separate determination
and is reported below; it lands **negative**, against the freeze's prediction of positive at medium,
and is reported against prediction with the freeze left unedited.

**The organizing caveat, carried verbatim** (re-wrapped in the source, word-for-word identical):

> Round 1 proved `a6cov_all : ∀ N M, A6Cov N M` — the adopted reading holds **identically** on
> every link-coupled rule of the interface, so its content is the covariant interface itself and
> not a constraint. A full positive therefore says exactly that the manuscripts' rule **is of that
> form**. It does **not** say that a nontrivial condition was tested and survived.

The two scopes are reported **separately and never as one**.

### Scope 1 — the covariance statement

`verification/programmes/substratum/a6-instantiation/result.md:320–324`:

> **The lift half.** It is discharged **for the covariance statement only**: the covariance statement
> is statable and proved at a complex six-component carrier with no new definition (`CX1`), the
> manuscripts' site-dependent transformation — `ℂ`-linear, and unitary in the matrix packaging — is
> an instance of the interface's transformation class (`CX2`), and the covariant form reaches the
> second-order dynamics there (`AS1`, `as1_complex`)

Carried by `cx1_complex_covariance`, `cx2_clinear_forgets`, `cx2_manuscript_law`,
`cx2_unitary_gaugeLink`, `as1_complex`.

### Scope 2 — the carrier

`verification/programmes/substratum/a6-instantiation/result.md:324–328`:

> while the complex carrier is **proved not to
> be** a `Substratum` satisfying `A1` (`CX3-b`), so the **carrier** does not come inside the
> interface, and the residual `CX0` classifies as (iii) — the inner product, unitarity as a
> constraint, the condensate, the stabilizer in $\mathrm{U}(6)$ and the cubic decomposition — stays
> outside and is named here as the residual.

**`cx3b_complex_not_A1` with its bounded reading**, `result.md:270–274` and `:276–285`:

> **`CX3-b` — level 2, the preregistered NEGATIVE, proved as predicted; strength high.**
> `cx3b_complex_not_A1`: `A1` **fails** at the complex carrier. `Substratum.A1` is
> `Finite (ι → V × V)` and the constant families exhibit an injection from `ℂ`, so the
> configuration space is infinite. **This is a computed certificate in the kernel, not a failed
> proof search.**

> **The covariance statement comes inside** (`CX1`, `CX2`). **The complex carrier does not come
> inside as a substratum in the kernel's sense** (`CX3-b`), because the interface's first axiom is
> finiteness and the complex carrier is infinite. That is **not a defect of the interface, not a
> defect of the manuscripts, and not a defect of the complex lift** … The two facts are reported
> **together** here, and reporting the first without the second would overstate the round.

The positive accompanying it is scope 1 above, and the two are reported together here as round 2
requires.

### The scope question — NEGATIVE, against prediction

**The question:** does what the propagation's own words for the lift half name — "that the covariance
of `SM.md:112–114` holds on an interface the programme has not built" — coincide with what round 2
proved?

**The record does not leave this silent; it answers it, and answers it in the negative.**
`verification/programmes/substratum/a6-instantiation/result.md:444–449`:

> **The row's label cell reads `**CONDITIONAL**` before and after, and the row's reasons are left
> byte-identical**, because they are the reasons the label is `CONDITIONAL` and every one of them
> still holds: `A6Cov` is a predicate of a neighbourhood function and a link coupling rather than of
> a `Substratum`; the covariance of `SM.md:112–114` on the complex lift is not kernel-checked as the
> manuscripts conduct it, on the carrier they conduct it on; and nothing is proved of the
> manuscripts' **physical** object.

That sentence names the propagation's own coordinates, `SM.md:112–114`, and says of them that the
covariance there **is not kernel-checked as the manuscripts conduct it, on the carrier they conduct
it on**. Round 2's own bounded reading gives the mechanism: the interface's statement "**contains**
the manuscripts' transformation law as a specialization and is **not identical to it**"
(`result.md:250–251`), and "**Nothing here is a complex-lift interface**" (`result.md:359`), the
interface the propagation's words name having still not been built.

**Determination.** What the propagation's words for the lift half name is **not established to be**
what round 2 proved. Evidence type 2, strength `high` — the determination rests on a located,
affirmative statement of the merged record, not on an absence.

**This is the finding, and it is not repaired.** It is a scope determination about two quoted
passages and it does not revise, promote or demote any target of round 2: `CX1`, `CX2`, `CX3` and
`AS1` stand exactly as merged, at exactly the strengths their result note records.

## `AJ4` — the residual, in two lists that are never merged

**Outcome: positive. Evidence type 2. Strength `high` on the sorting; `medium` on whether the record
presents the substratum identification as this row's own hypothesis** — exactly as predicted, and
for the reason predicted. **This is a census, not an adjudication**: no item below is judged fatal
or harmless here.

### `AJ4-in` — what the record presents as a hypothesis the row tracks

**One item: the substratum identification** — that the manuscripts' physical substratum is the
packaged carrier.

The determination the gate turns on is **whether the record presents it as this row's named
hypothesis or as a premise ambient to the programme's rows generally**. The record does **both**, at
two coordinates, and the difference is reported as a finding rather than resolved.

**(a) Presented as ambient — a premise no round can discharge.**
`verification/programmes/substratum/a6-instantiation/result.md:344–347`:

> **They do not assert anything about the physical substratum.** The packaged carrier is a formal
> object built from stated data; that the physical substratum is that object is a premise no round
> can discharge, and it is the residual that survives every outcome here. **Nothing here says the
> sixth assumption holds of the physical substratum, or fails of it.**

The same, in the `ROADMAP` section at `:563–564`: "*What is left.* That the manuscripts' **physical**
substratum is the packaged carrier is a premise no round discharges". Neither passage says "this
row's hypothesis"; both say "a premise", and round 2's freeze uses the identical wording at
`preregistration.md:602–604`.

**(b) Presented as a reason this row's label stands.**
`verification/programmes/substratum/a6-instantiation/result.md:444–449`, quoted in full under `AJ3`,
lists three items as "the reasons the label is `CONDITIONAL` and every one of them still holds", and
the third is: "**nothing is proved of the manuscripts' physical object**".

**Determination: the substratum identification is NOT established not to be a hypothesis this row
tracks.** Coordinate (b) presents it, in terms, as one of the reasons this row's label stands. The
gate's requirement is an establishment in the negative, and the record does not supply one; it
supplies a passage in each direction. Strength `medium`, per the freeze's own rule that a
determination carried by a passage naming a thing without displaying it is at most `medium`.

**A recorded tension of the record, not repaired.** The propagation's point of imperfect fit says
"this row's named hypothesis is one of **formalization scope**" and that "the row text below names
the hypothesis explicitly so that nobody reads the label as a physical premise the manuscripts have
added" (`a6-covariance-propagation-audit.md:143–147`), while round 2's result lists a physical-object
residual among the reasons the label stands. The record therefore presents the row's hypothesis in
one place as strictly a formalization-scope matter and in another as including a physical-object
matter. **The record does not draw the distinction that would settle which is authoritative, and
this round does not draw it on the record's behalf.**

**Whether the manuscripts state the hypothesis.** `CONDITIONAL`'s second sentence says "The
manuscript states the hypothesis". Recorded by quotation: the propagation says "The manuscripts state
the assumption itself, as the covariant interface, and the row tracks what separates that statement
from a kernel statement about their object"
(`a6-covariance-propagation-audit.md:140–141`). On the substratum identification specifically, the
record presents it as a premise the programme carries rather than as a sentence quoted from a
manuscript, and **no passage was found, on a search of the four A6 artifacts and the `ROADMAP`
section bounded to them, in which a manuscript coordinate states the identification**. That absence
is recorded as an absence on a named and bounded search.

### `AJ4-out` — what the record places outside `A6Cov`

**These stand outside the interface and are no part of the condition the label carries. No outcome
of this round moved any item from this list into `AJ4-in`, and none entered the gate.**

1. **The part of `[SM §3.1]`'s derivation that consumes the inner product, unitarity as a
   constraint, the condensate `Σ`, the stabilizer in `U(6)` or the cubic decomposition.**
   `result.md:326–328`: "the residual `CX0` classifies as (iii) — the inner product, unitarity as a
   constraint, the condensate, the stabilizer in $\mathrm{U}(6)$ and the cubic decomposition — stays
   outside and is named here as the residual." The `ROADMAP` section carries it at `:564–568`.
2. **The complex carrier's failure of `A1`.** `cx3b_complex_not_A1`, `result.md:270–274`, quoted
   under `AJ3` scope 2.

### Reported alongside both, and in neither

- **The `A4Exact` translation-invariance hypothesis**, `∀ v i j, M (i + v) (j + v) = M i j`, reported
  with the conjunct it qualifies — "`A1`–`A5` hold of it" — as under `AJ2`. It qualifies a named
  result, not the label.
- **Round 2's six unsettled points**, `result.md:387–415`.
- **Round 1's three unsettled points**, pinned by `_a6d_unsettled`: the definition/use-site split,
  the `μ I_6`-versus-block-scalar denotation of "the cubic-symmetric coupling matrix", and the shared
  name between `A6-sd` and the gauge readings.
- **The manuscript-axiom audit's bare-carrier finding**, which is about a different carrier:
  `ROADMAP.md:536–540`, "That finding is about the operational interface; the paragraphs above are
  about the substratum structure. Both hold, of different objects." It stands untouched.

## `AJ5` — the current row text, clause by clause, against the merged record

**Outcome: one semicolon-delimited clause not carried, comprising two conjuncts each not carried.
Evidence type 2. Strength `high`.** The freeze predicted "at least two clauses not carried" at
medium; under semicolon delimitation the count is **one clause**, whose two internal conjuncts are
each not carried. **Reported against prediction, and the prediction is not amended.**

The label-and-reasons cell of `ROW` at the base splits at its semicolons into five clauses.

| # | clause | verdict | quotation carrying the verdict |
| --- | --- | --- | --- |
| 1 | "the adopted meaning is covariance, `A6Cov`, which holds identically on every link-coupled rule of the least interface (`a6cov_all`), so its content is the covariant interface and not a constraint" | **carried** | `ROADMAP.md:480–483`: "proves it for every neighbourhood function and link coupling (`a6cov_all`): once the link-coupled transformation law is built into the interface no further equation is imposed on the rule, so its content is the covariant interface itself, not a constraint" |
| 2 | "the named hypothesis is that the manuscripts' substratum instantiates that interface: the `K = 6` link-coupled rule is not packaged as a `Substratum` (the interface's `waveSubstratum` has a singleton internal index) and the complex lift on which `[SM §3.1]` conducts the gauge derivation is outside the interface" | **NOT carried** | see the two conjuncts below |
| 3 | "`A6-inv` is a separate, stronger fixed-background condition, refuted on the frozen two-site carrier and at the symmetric point `M = μ I_6` (`d3b_not_a6inv`, `d4b_mu_id`)" | **carried** | `ROADMAP.md:502–509`: "a separate and strictly stronger fixed-background condition … it fails on the frozen two-site link-coupled carrier (`d3b_not_a6inv`) … and at the manuscripts' symmetric point `M = μ I_6` it fails (`d4b_symmetric_point`, `d4b_mu_id`)" |
| 4 | "`A6-glob` its global specialization (`a6glob_of_a6inv`)" | **carried** | `ROADMAP.md:512–513`: "`A6-glob` (`A6Glob F M`), the constant-`g` specialization (`a6glob_of_a6inv`)" |
| 5 | "`A6-sd` a different principle under a shared name" | **carried** | `ROADMAP.md:518–522`: "`A6-sd`, the state-dependent coupling graph of `SM.md:100` … `SM.md` §3.1 says in place that it is a different principle under a shared name" |

**Clause 2, conjunct by conjunct:**

- **"the `K = 6` link-coupled rule is not packaged as a `Substratum`" — NOT carried.**
  `result.md:309–313`: "the manuscripts' six-fold link-coupled rule **is** packaged as a
  `Substratum` of the kernel's own structure with no field added". The merged record carries the
  contradictory of this conjunct.
- **"(the interface's `waveSubstratum` has a singleton internal index)" — carried as a fact, not
  carried as a reason.** `ROADMAP.md:514` still records `waveSubstratum`'s degenerate singleton
  index; but the clause offers it as the reason no packaging exists, and `pk4_shift_not_scalar`
  removes the degeneracy verdict for the packaged carrier — `result.md:315`: "its transformation
  class is larger than the singleton-index one (`PK4`)".
- **"the complex lift on which `[SM §3.1]` conducts the gauge derivation is outside the interface" —
  NOT carried as stated.** The merged record splits "inside the interface" in two and the row's
  clause does not: `result.md:278–279`, "**The covariance statement comes inside** (`CX1`, `CX2`).
  **The complex carrier does not come inside as a substratum in the kernel's sense** (`CX3-b`)."
- **"the named hypothesis is that the manuscripts' substratum instantiates that interface" — carried
  as the propagation's wording** (`AJ1`), but its two stated grounds are the two conjuncts above.

**The finding is the collation, and it fires `AJ7`'s second branch.** Because at least one clause is
not carried, the row text changes under every label outcome, which is what makes the guard-contract
edit unavoidable — the point the `§A.37` declaration turns on.

## `AJ6` — the adjudication

**Outcome: `AJ6-conditional`. As predicted, at the predicted strength `medium`.**

This determination is the freeze's one bounded exception: **a judgement against a quoted rule**, its
inputs all type P. It is stated as the application it is, and is not reported as a located passage.

### All seven entries of `VOCAB`, run

| entry | candidate? | the application |
| --- | --- | --- |
| **`ACTIVE`** | no | "A round is running, or is **frozen and merged** and awaiting execution." No A6 round is running or awaiting execution at this base. The propagation set it aside: "do not apply." |
| **`OPEN`** | no | "no closing construction or theorem, and no impossibility theorem." The row has a closing theorem on the interface it is stated on, `a6cov_all`. The propagation: "misdescribes a row that has a closing theorem on the interface it is stated on." |
| **`GAP`** | no | "the formal interface has **no predicate for it at all**." `A6Cov` is the adopted predicate, defined and proved. The propagation: "is false after adoption." |
| **`EXTERNAL`** | no | "A published result consumed as a cited premise." Nothing in the row is a cited external publication. The propagation: "do not apply." |
| **`INDEPENDENT`** | no | "The kernel has **settled it negatively**: the resource is not sourced by the stated architecture." No negative settlement of the sixth assumption exists; `cx3b_complex_not_A1` is a statement about a carrier, not about the assumption. The propagation: "do not apply." |
| **`CONDITIONAL`** | **YES** | see below |
| **`DERIVED`** | **gated, and the gate does not open** | see below |

### `DERIVED` — both halves of the gate, run

The gate, as frozen, requires **both**.

**Gate half 1 — the substratum identification established not to be a hypothesis this row tracks.**
**NOT met.** `AJ4-in` finds the record presenting it in one place as "a premise no round can
discharge" and in another, in terms, as one of "the reasons the label is `CONDITIONAL`". The gate
asks for an establishment in the negative; the record supplies a passage in each direction, so the
negative is not established. Per the gate's own closing sentence: "If the substratum identification
is this row's tracked hypothesis … the outcome is `AJ6-conditional` or `AJ6-UNDECIDED`, never
`AJ6-derived`."

**Gate half 2 — `AJ3` establishing, from the propagation's own words for the lift half, that what
those words name is what round 2 proved.** **NOT met, and not by silence.** The record states the
contrary in terms: "the covariance of `SM.md:112–114` on the complex lift is not kernel-checked as
the manuscripts conduct it, on the carrier they conduct it on" (`result.md:447–449`). The
propagation's words name that covariance; the record says it is not kernel-checked as conducted.

**What the gate did not test, and did not need to.** No item of `AJ4-out` entered the gate. The
inner product, unitarity as a constraint, the condensate `Σ`, the stabilizer in `U(6)`, the cubic
decomposition and the complex carrier's failure of `A1` were **not** used as gate inputs, in either
direction. The gate closed on the substratum identification and on the propagation's lift-half
wording, which are the only two things it tests. **`AJ6-derived` was not blocked on anything the row
does not track.**

**Nothing in `AJ4-out` bore on this outcome**, exactly as the freeze's prediction said it would not.

### `CONDITIONAL` — the application

`CONDITIONAL`'s stated meaning: "Formally present, carrying a named hypothesis this programme has
not discharged. The manuscript states the hypothesis; the row tracks it."

- **"Formally present"** — `A6Cov` is defined in `BackgroundIndependence.lean` and proved by
  `a6cov_all`. True of the row.
- **"carrying a named hypothesis this programme has not discharged"** — the named, undischarged
  hypothesis identified from **`AJ4-in`** and quoted: *that the manuscripts' physical substratum is
  the packaged carrier* — `result.md:345–346`, "that the physical substratum is that object is a
  premise no round can discharge, and it is the residual that survives every outcome here". **No
  item of `AJ4-out` carries this outcome**; what stands outside `A6Cov` is not a hypothesis the
  label tracks, and none was used to reach it.
- **"The manuscript states the hypothesis"** — **recorded, as the vocabulary's second sentence
  requires**: the record presents the assumption itself as stated by the manuscripts ("The
  manuscripts state the assumption itself, as the covariant interface"), and presents the substratum
  identification as a premise the programme carries rather than as a manuscript sentence. **No
  manuscript coordinate stating the identification was found on the bounded search named in
  `AJ4-in`.** This is recorded as a point at which the vocabulary's second sentence fits the row
  imperfectly — the propagation recorded the same imperfect fit from the other side — and it is
  **not repaired**.

**`AJ6-conditional` is not a finding that the landed rounds achieved less.** It is a finding about
which vocabulary entry describes a row that carries a named residual. The kernel content of the row
is exactly what round 1 and round 2 proved, at exactly the strengths their result notes record.

### A bounded search, reported as it was found

`DERIVED` occurs in `verification/ROADMAP.md` at exactly two coordinates: the vocabulary entry
(`:29`) and the section heading at `:487`. **No row of the queue carries `DERIVED`, and the file
carries no settled-`DERIVED` record.** Per hazard 7, that is a fact about the queue: it is neither
evidence that the label is unavailable nor evidence that it applies, and **no target above rests on
it**.

### Analysis paragraph, which is NOT evidence

A reader who knows the programme can argue that a hypothesis of pure formalization scope, both of
whose halves the propagation named and round 2 addressed, ought to fall away and let the row move.
**That is reconstructive inference, it is forbidden as a finding by the evidence rule, and no target
above rests on it.** The determinations above rest on located passages, each quoted with its
coordinate.

## `AJ7` — the replacement row text

**Outcome: positive. Strength `high`.** The decision rule's second branch fires:
**`AJ6-conditional`, and `AJ5` found at least one clause not carried → `ROW-conditional`, written at
`verification/ROADMAP.md:65`, the row staying in the queue.**

`ROW-conditional` was **copied character-for-character** from the freeze — extracted programmatically
from the preregistration blob rather than retyped — and written to `verification/ROADMAP.md:65`. The
execution composed no row text of its own.

**The departure did NOT fire**, and could not: it belongs to `AJ6-derived` alone. The queue table is
**byte-identical apart from line 65**; no row left, no row was reordered, no row changed a cell, no
settled-`DERIVED` record was created, and the `INDEPENDENT` record at `:773` was not touched. The
row's section keeps its position between `### P1 — Substratum Lemma 24.1, the semigroup-transfer
step` and `### P1 — physical C4 discharge`.

**The row text is in manuscript voice.** It states what is; it narrates no change, cites no round
number, and refers to no state of the row other than the one it writes. Verified by scan.

## `AJ8` — the guard-contract surface

**Outcome: positive on the census as a census; the eight-row candidate list is NOT complete.
Strength `high`.** Predicted "positive, and the eight-row candidate list is expected to be complete"
at medium. **The completeness half lands negative and is reported against prediction**, under
`AJ8`'s own bounding clause. See the discrepancy section.

Coordinates below are the **live** ones at the base; the freeze's coordinates for everything after
`edge_rigidity_probe.py:16824` are `491` lines lower, a mechanical shift recorded as a discrepancy.

| live coordinate | constant / clause | assertion about the live file | changed? |
| --- | --- | --- | --- |
| `:15468–15478` | `_A6P_ROW` | the row string, character-for-character | **YES** — set to `ROW-conditional` |
| `:15479–15481` | `_A6P_ROAD_HYP` | the section's named-hypothesis sentence, consumed by `_a6p_roadmap` | **YES** — re-pointed at the section's adjudicated sentence |
| `:15604–15619` | `_a6p_roadmap` | `_A6P_ROW in _r`; the "Why the row is `CONDITIONAL`, and neither `DERIVED` nor `GAP`." heading; `_A6P_ROAD_HYP`; four further section sentences; the propagation link | **no** — the clause bodies stand; two of the constants they consume changed |
| `:15750–15755` | `_a6p_m5` | mutation control: the complex-lift covariance declared kernel-checked in the live section | **YES** — re-pointed; **not named by `AJ8`** |
| `:15758–15759` | `_a6p_m6` | mutation control: live label cell rewritten `CONDITIONAL` → `DERIVED`, `_a6p_roadmap` required to reject | **no** — the label cell is unchanged, the rewrite still fires and is still rejected |
| `:17573–17594` | `_a6d_roadmap_row` | the same row string written out inline, plus two link clauses and a clause about round 1's result note | **YES** — inline row string set to `ROW-conditional`; the three other clauses untouched |
| `:17786–17789` | `_a6d_m25` | the same mutation control against `_a6d_roadmap_row` | **no** — unchanged, still fires, still rejected |
| `:18349–18366` | `_a6i_label_unmoved` | the live row's label-cell prefix, and that `\| Substratum \| **DERIVED** —` is absent from the live `ROADMAP` | **no** — `ROW-conditional` keeps the same label-cell prefix and the absence still holds |
| `:18165+491 = :18656–18657` | `_a6i_m10` | the same mutation control against `_a6i_label_unmoved` | **no** — unchanged, still fires, still rejected |
| `:18369–18387` | `_a6i_roadmap_section` | ten sentences of the live `P1 — A6` section | **no** — every sentence it pins is in the "What the instantiation round settled" paragraph, which this round does not edit |

**The three clauses named as expected NOT to change, confirmed not changed.** `_a6p_readme`
(`:15622–…`) and `_a6i_readme` (`:18390–…`) assert sentences inside the **round records** of the
propagation and of round 2 in `verification/README.md`; those sentences are statements about what
those rounds did, they stay true, and **no existing `README` paragraph was edited**. The third,
`_a6d_roadmap_row`'s clause asserting that round 1's result note still records that round 1 left the
`GAP` label in place — `'**The `ROADMAP` row `P1 — A6` keeps its `GAP` label**' in t` — stands
unmodified.

**Two further live-`ROADMAP` mutation controls were checked and stand unmodified**, their targets
being sentences this round does not edit: `_a6i_m18` (`:18704–…`, the covariance instance reported as
a tested condition) and `_a6i_m21` (`:18735–…`, the complex lift declared kernel-checked and the
assumption declared to hold of the physical substratum, written in place of the owner's call).

**No mutation control was deleted, and none was weakened.** `_a6p_m5`'s re-pointing keeps it a
control that its guarded clause rejects: the rewrite strips the scope qualification from the
section's covariance sentence, and `_a6p_roadmap`'s clause `'on the complex lift is not
kernel-checked' in _sec` then fails, so the guard rejects the mutated file. It is not a rewrite the
clause rejects trivially — it is a single-word flip on exactly the claim the clause guards.

**No seal constant, merge constant or base constant appears in the diff.** Verified mechanically;
see the pre-commit checks below.

## `AJ9` — the section and the landing page

**Outcome: positive. Strength `high`.** Predicted positive at medium; the target landed above its
predicted strength because the sentences requiring change were identified by direct contradiction
with quoted passages rather than by judgement. **The promotion and its reason are recorded here, as
the freeze requires.**

**The section.** `### P1 — A6, and what is and is not already represented` keeps its position and
its heading. **One paragraph changed**, the one under the bolded heading **"Why the row is
`CONDITIONAL`, and neither `DERIVED` nor `GAP`."**, whose sentences the adjudication reaches:

- its statement that "no `Substratum` packaging of the manuscripts' `K = 6` link-coupled rule
  exists" is contradicted by `pk1_packaging` (`AJ5`);
- its statement that the complex lift "is outside the interface by decision" does not carry round
  2's split of "inside the interface" in two (`AJ3`);
- its named-hypothesis sentence states `COND` as the propagation stated it, which `ROW-conditional`
  replaces with the substratum identification.

The replacement is written in manuscript voice, in the present tense, and **separates, as the row
does, the named hypothesis from what stands outside `A6Cov`** — the second introduced by
"**Separately, and outside `A6Cov` rather than as a condition on it**" and closed by "Neither of
these is a component of the condition the label carries". It carries round 2's own scope
qualification verbatim: "the covariance of `SM.md:112–114` on the complex lift is not kernel-checked
as the manuscripts conduct it, on the carrier they conduct it on."

**Every other paragraph of the section stands byte-identical**, including "What the instantiation
round settled, and what it did not", the three-readings paragraph, the two attached qualifications,
the bare-carrier paragraph and the link block. In particular the sentence naming the stronger-label
decision as an owner decision taken in a separate round is **left standing**, as the freeze's open
question records: it is accurate in manuscript voice, and no owner instruction to recast it was
given before the freeze merged.

**The landing page.** `verification/README.md` gains **one appended paragraph** for this round,
placed after round 2's record and before the `verify.yml` sentence. **No existing paragraph was
edited.**

**Bounded in terms, and verified.** The `ROADMAP` edit is confined to the row `P1 — A6` and its
section. No other row, section or research status was touched; no other row moved, changed a cell or
changed order. **No manuscript was edited**: `papers/` and `book/` are untouched, and the census
gains no anchor, no manuscript propagation occurring in this round.

## Discrepancies

**1. Four start-state blobs differ at the mandated base.** Recorded, **not repaired**, and none of
the differing material was consumed.

| path | blob the freeze names | blob at the base | what differs |
| --- | --- | --- | --- |
| `verification/lean-manuscript-census.json` | `06ad11f4b954f290a5ae523d83a6fb0b142d13e1` | `59f94ac1d18d1f965541a523629e5df9dafd9359` | the Physical C4 round 2 landing |
| `verification/lean/edge_rigidity_probe.py` | `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e` | `55e7c3e3139741521bc5aeac6add56f557be5943` | one purely additive hunk of 491 lines at `:16824`, the `R7-PC4S` guard block |
| `verification/ROADMAP.md` | `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218` | `c356e9b5f857ef18a992d67df613b9db96a949d7` | 31 added lines in the `### P1 — physical C4 discharge` section and its link block |
| `verification/README.md` | `585dd145186dae654f58e2dc16712550b68ec9e0` | `d25eb2d44d0aa324c095930f40174296fd0f2279` | one appended round record for Physical C4 round 2 |

Every difference is an addition by the Physical C4 round 2 landing, which merged between this
freeze's drafting and its control plane's merge. **Each diff was inspected**: all three text diffs
are purely additive, the probe diff is a single hunk with one changed line elsewhere and none inside
the A6 blocks, and **no A6 surface is touched by any of them**. The row at
`verification/ROADMAP.md:65` and the value of `_A6P_ROW` were both verified **character-identical to
the freeze's pinned text** despite the enclosing files having moved, and the start state's identity
clause — that `_A6P_ROW`'s value equals the row line — held.

**The anti-contamination invariant was observed.** Physical C4 round 2 is not named as an input by
this freeze, and nothing of it was consumed: no target above cites it, quotes it or depends on it.
No base merge, rebase or branch update was performed. The branch will show as behind `main`; that is
the protocol working.

**2. `AJ8` under-counted the guard surface by one clause.** `edge_rigidity_probe.py:15750–15755`
carries the mutation control `_a6p_m5`, whose `.replace` source is a **live `P1 — A6` section
sentence** — ", and the covariance of `SM.md:112–114` on the complex lift is not kernel-checked." —
and whose assertion is therefore about the live section. `AJ8`'s candidate table does not name it.
`AJ9` requires that sentence to carry round 2's scope qualification, which moves the sentence's
terminal period, so the control's rewrite would become a no-op and the control would fail by
construction. **The clause is named here, the freeze is reported as having under-counted the
surface, and the surface was not enlarged silently.** The control was re-pointed, not deleted and not
weakened, per hazard 8's principle and `AJ8`'s departure note read for its general rule; its
re-pointing is recorded in `AJ8`'s table and in a comment at the clause. This is the exact failure
mode hazard 10 names — a clause that escapes a search built on the label token and the row string,
because it pins a **section sentence** rather than either.

**3. The freeze's line coordinates for `edge_rigidity_probe.py` are `491` lines low after `:16824`.**
`_a6d_roadmap_row` is at `:17558` and not `:17067`; `_a6d_m25` at `:17786–17789` and not
`:17295–17298`; `_a6i_label_unmoved` at `:18349` and not `:17858`; `_a6i_roadmap_section` at `:18369`
and not `:17878`; `_a6i_m10` at `:18656–18657` and not `:18165–18166`. `_A6P_ROW`, `_a6p_roadmap` and
`_a6p_m6` are at their frozen coordinates, being above the insertion. **The identity of every clause
is preserved**; only the coordinates moved, by the addition recorded as discrepancy 1. Recorded, not
repaired.

**4. `VOCAB`'s table occupies `ROADMAP.md:22–30`, not `:22–31`** as the freeze and the propagation
both write it. The seven entries are at `:24–30` and all seven were located. A one-line coordinate
difference; recorded, not repaired.

**5. A tension within the merged record about what the row's hypothesis is.** Reported in full under
`AJ4-in`: the propagation records the row's named hypothesis as one of **formalization scope** and
warns against reading the label as a physical premise, while round 2's result lists "nothing is
proved of the manuscripts' **physical** object" among the reasons the label stands. **The record does
not draw the distinction that would settle which is authoritative**, and this round does not draw it
on the record's behalf. It is the reason gate half 1 is not met, and it is the round's principal
item for the owner.

**6. Two determinations landed against prediction.** `AJ3`'s scope question was predicted positive at
medium and lands **negative at `high`**. `AJ8`'s completeness half was predicted positive at medium
and lands **negative**. `AJ5` was predicted to find at least two clauses not carried and finds **one**
semicolon-delimited clause with two failing conjuncts. `AJ9` landed at `high` against a predicted
medium; the promotion and its reason are recorded at `AJ9`. **In every case the outcome is reported
against prediction and the freeze is left unedited.**

**7. The shape reference named for this result note is not present at the mandated base.**
`verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` does not exist at
`c4ae9bfa`; only that act's control plane does. Round 2's own result note — a pinned start-state
input of this freeze — was used for shape instead. Recorded so that the absence is a located absence
on a named search and not a silent substitution.

## The post-round sentence, written verbatim from the freeze

The outcome is `AJ6-conditional` with `AJ5` finding at least one clause not carried, so the frozen
sentence is **`AJ-stand-restate`**:

> The row `P1 — A6` carries `CONDITIONAL`, and the label is the one the queue's vocabulary supports:
> the predicate is formally present and proved, the hypothesis the covariance propagation named is
> discharged in its packaging half at evidence level 2 and discharged for the covariance statement in
> its lift half, and the hypothesis the row tracks is the one named in the frozen row text — that the
> manuscripts' physical substratum is the packaged carrier, and that identification is the whole of
> it. Separately, and outside `A6Cov` rather than as a condition on it, the part of the gauge
> derivation that consumes the inner product, unitarity as a constraint, the condensate, the
> stabilizer in `U(6)` or the cubic decomposition stands outside the interface, as does the complex
> carrier. The row stays in the queue and its reasons are written to
> the frozen text. Nothing here strengthens or weakens what the three landed A6 rounds established,
> nothing here says the sixth assumption holds of the physical substratum or fails of it, and nothing
> here is a derivation of the gauge group.

## The landing shape, stated

**Type P throughout. No axiom table, no `#print axioms` line, no Lean, no definition, no new guard
tag** — the definition budget was **ZERO** and nothing drew on it. **No `sorry`, no `axiom`, no
`native_decide`**, checked rather than assumed.

**NON-SEALING.** No seal constant, merge constant or base constant was touched. The landing is
`E` → `L`, **with no archive-pin commit**: this round owns guard contracts about the live row, owns
no seal state, and — in `§A.37`'s own words — does not "acquire a pin commit merely by touching the
guard file that carries it". A pin added here would pin nothing.
