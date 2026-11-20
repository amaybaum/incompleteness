# R1-L8 Stage 0 — preregistration: scope, schema, classes and decision rule

**Status.** Writer's paper-only preregistration, committed and pushed before any row is classified.
The classification is `AUDIT.md` in this directory, in a later commit. Existing evidence only: no
new measure construction, no replacement probability law, no new physical assumption, no manuscript
edit (Main included), no Lean, no computation beyond reading. A1 (Main posit ledger item (ii))
remains open and unadopted. Independent non-author review is required before any use of the audit.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7039208422](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7039208422),
2026-11-20T12:11:13Z, "Owner decision record: R1-L8 Stage 0 authorized". Quoted: "**Authorized:** a
paper-only requirements audit." The same record names a single writer and requires "independent
non-author review, existing evidence only." "**Not authorized:** Stage 1; new measure constructions or replacement probability laws; new
physical assumptions; manuscript edits, including any change to Main; broader A1-removal work."
"Cover M1, M2 (including μ-G, μ-O and μ-R), M3 (the doubly stochastic corner), C1 (the coupled
case), C4 and M19 (R5 / L8). Trace each to its actual observational conclusions. C4 must be traced,
not classified without a trace. Reuse REMAINDER, R1-INF, NR-1 and FCLASS without repeating their
investigations." Owner technical note: "Infinite lattices admit well-defined translation-invariant
probability laws and entropy densities. The question is not whether probability or maximal entropy is
defined. It is whether the particular law OI requires is justified rather than selected by
assumption."

**Goal link (§A.47), from the authorization.** "Decides how much of OI genuinely needs a selected
probability law and how much needs only a declared law with provable properties. This is the R1
obstacle to removing A1 (priority record c.7037422124)." It does not decide whether such a law is
physically justified.

**Source pin.** `main` at `23a28dab9976e67482d45247bc2fdcce10e224a8`. `M:n`, `GR:n`, `SM:n`,
`Sub:n`, `Str:n` are line `n` of `papers/Main.md`, `papers/GR.md`, `papers/SM.md`,
`papers/Substratum.md`, `papers/Structure.md` at the pin. Line numbers quoted from a reused record
refer to that record's own pin; where `papers/Main.md` has moved since (A1-SCOPE Phase 2), the audit
cites the current line.

## 1. Scope: the six items

Item definitions are those of A1-REMAINDER (`verification/audits/foundations/a1-remainder-20261119/REMAINDER.md`)
§1 rows M1, M2, M3, M19, C1, C4 and §2 residues R1 and R5:

| Item | Definition (REMAINDER) | Scoped part |
|---|---|---|
| M1 | Lemma 3 selection clause: the counting measure as the maximal-entropy invariant measure (row M1) | whole |
| M2 | μ-G, μ-O, μ-R and posit (iv) (row M2) | whole |
| M3 | baseline matrices under the uniform hidden prior; the doubly stochastic corner (row M3) | the doubly stochastic corner, with the uniform-prior consumers it feeds |
| C1 | H-count, the classical horizon temperature as a counting derivative (row C1) | the coupled case (P7B node 6.3); the decoupled case is recorded as the comparison |
| C4 | H-BD and the boundary-only lemma (b) (row C4) | whole, traced to its consumers |
| M19 | §4.6 equilibrium phase: global equilibrium macrostate ⇒ local equilibrium by canonical typicality (row M19; residue R5; lemma L8) | whole |

## 2. Reused records (not re-derived)

| Short name | Path on `main` | Used for |
|---|---|---|
| REMAINDER | `verification/audits/foundations/a1-remainder-20261119/REMAINDER.md` | item definitions, repairs P-μ, L1–L10 |
| R1-INF | `verification/audits/foundations/r1-inf-20261119/RESULT.md` | E/N/U, P-ED, Lemma 8 (L3), Props. 7 and 9, countermodels C1–C7 |
| NR-1 | `verification/audits/foundations/nr1-near-return-20261116/NR-1.md` | selected update on `ℤ^d` under Haar; torus comparison |
| FCLASS | `verification/audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md` | finiteness classes, rows 06, 16–19, 23–24 |
| RIGID | `verification/audits/foundations/a1-rigid-visible-recurrence-20261119/A1-RIGID-1.md`; `verification/lean-mathlib/OIBridge/ObservableRigidity.lean` | measured rooted family, compact-orbit route |
| PREP | `verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md` | stationarity, budgets, escapes 1.5(a)–(e) |
| P7B | `verification/audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | H1–H14, node 5, node 6.3 |
| P6 | `verification/audits/foundations/p6-reciprocity-20261116/P6-RECIPROCITY.md`; `verification/lean-mathlib/OIBridge/MeasuredReciprocity.lean` | reciprocity under a specified invariant law |
| A1-05 | `verification/audits/foundations/a1-05-p8-observer-selection/SOURCE-MATRIX.md` | P8-M, P8-S |
| OA-1 | `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md` | typing of μ-O, μ-G, μ-R |
| CM | `verification/lean-mathlib/OIBridge/CanonicalMeasure.lean` | finite Lemma 3 in the kernel |
| GLUE | `verification/audits/foundations/a1-p12-common-carrier-20261119/A1-P12-GLUE-1.md` | cited only where REMAINDER cites it |
| POSIT-MIN | `verification/audits/foundations/posit-min-20261120/AUDIT.md` | item (iv) row |

Every reused record is a paper-layer research record or a manuscript statement unless it names a
kernel declaration; none is promoted beyond the layer it states for itself (§A.46 item 7). A short
argument written in this audit is marked [W] and is a reading of existing statements (which property
of the law a proof step uses; a one-line invariance check of an example already on `main`). No [W]
argument constructs a new law, proposes a replacement or closes a named lemma.

## 3. Unit of classification and trace procedure

The unit is a **conclusion row**: one conclusion that consumes the item, traced to its observational
consequence. For each item:

1. Start at the item's site(s) in REMAINDER and at the current Main/companion lines.
2. Follow consumers by search over `papers/*.md`, `book/*.md`, `verification/lean*/` and
   `verification/` records for the item's phrases and symbols: `maximal-entropy`, `maximal
   entropy`, `counting measure`, `uniform prior`, `uniform hidden prior`, `doubly stochastic`,
   `μ-O`, `μ-G`, `μ-R`, `H-count`, `H-BD`, `canonical typicality`, `local equilibrium`, `(IP)`,
   `(NR)`, `(IL)`. Book chapters and `FULL.md` are checked as mirrors; a mirror that states the
   same conclusion adds no row.
3. Read the proof of each consumed conclusion and record the measure properties it uses (not the
   label it carries).
4. A conclusion whose only consumer is another row is merged into that row; a conclusion with no
   observational consequence is still classified, and typed `NONE` (§4).
5. Rows found by step 2 beyond those REMAINDER names are added; the search patterns and hit counts
   are recorded in AUDIT's coverage section.

## 4. Schema (one row per conclusion)

| Field | Content |
|---|---|
| Id | `<item>.<k>` |
| Conclusion and site | exact theorem or claim, file:line |
| Observational consequence | what an observer could measure, typed: `ACC` (finite-window, testable in principle), `REC` (recurrence-scale or all-time; no finite-window test), `RETRO` (reproduces a known value; consistency, not correctness, §A.23), `GAUGE` (unobservable by construction), `NONE` (representational or structural) |
| Measure assumptions used | properties of the law the proof actually uses: normalization, invariance (under which maps), product form, uniform factor (on which finite set), root-independence, a return/compactness condition, a fibrewise bound, a selection principle |
| Weakest sufficient condition on `main` | the weakest condition an existing record proves sufficient, with its layer (kernel / exact / paper / numerical) and source |
| Mathematical sufficiency | whether the condition in the previous field suffices for the conclusion as claimed, or for a named narrower form |
| Physical justification | whether the framework gives a reason that nature realizes such a law: `given` (cite), `partial` (cite what is given), `none on main` (cite the record that says so) |
| Class | (a), (b) or (c), by §5, with a one-line justification |
| Predictions vary between admissible laws? | `yes` (cite a witness on `main`, or a [W] reading of an example already on `main`), `no` ([W] reason), `not determined on main` |
| Outstanding physical-sourcing obligations | named, with the repair id from REMAINDER where one exists |
| Stage 1 recommendation | recommendation only, or `none` |

## 5. Classes (fixed before classification)

Notation. For a declared carrier `S` and update `φ`, `𝒜(φ)` is the set of normalized laws on `S`
invariant under `φ` (the admissible invariant laws). Where a result uses a prior that need not be
invariant (a root-shared hidden prior, a preparation), the admissible class is the set of normalized
priors of that form, and the row says so. `P` is the set of measure properties the weakest
sufficient proof on `main` uses.

The tests are applied in the order (c), (b), (a).

- **(c)** A particular law or a selection principle is required to obtain the claimed observational
  result. The row is (c) if either holds:
  - **(c1)** the conclusion reports a quantitative value or a state that is computed from the law's
    weights (not merely a property the law has), the value varies across admissible laws satisfying
    the result's other premises, and the claimed value is obtained only for the law a stated
    selection fixes (equal weighting, maximal entropy, counting, entropy-density maximization under
    stated symmetry, the uniform law on the orbit of the actual microstate, a typicality measure);
  - **(c2)** the conclusion is a typicality statement ("every", "almost every" or "most" states in
    a macrostate) whose quantifier is taken with respect to one selected law, and an admissible law
    is on `main` (or follows by a [W] reading of an example on `main`) under which the conclusion
    fails.

  A uniqueness proof for the selected law is not required (owner clarification 2).
- **(b)** Not (c), and the conclusion requires measure properties beyond membership in `𝒜(φ)` (or
  beyond normalization and root-sharing, for a non-invariant prior): product form, a uniform
  marginal on a finite factor, invariance under an additional map, a return or compactness
  condition, a fibrewise bound. The conclusion is structural (a property such as double
  stochasticity, reciprocity, P-indivisibility, an error bound) and holds for every law with
  those properties. Each property stays an explicit conditional premise.
- **(a)** The conclusion holds for every law in `𝒜(φ)` (respectively every normalized root-shared
  prior), with no further property.

**Boundary case, fixed in advance.** A premise that fixes one *finite factor* of the law to be
uniform (the visible marginal in (IP); the boundary-shell count in P7B H4) is read as a property
under (b) when the conclusion is structural, and as a selection under (c1) when the conclusion's
reported value is computed from those weights. The audit also reports the counts under the
alternative reading **R′**, in which every premise that fixes some factor of the law uniquely puts
the row in (c), whatever the conclusion's type.

## 6. Decision rule (fixed before classification)

Let `N_c` be the number of rows classed (c) under §5, and `N_c′` the number under R′. The audit
reports `N_c`, `N_c′`, the number of (c) rows whose observational consequence is `ACC` or `RETRO`,
and the (a)/(b)/(c) counts.

- If `N_c = 0`, the verdict states only: "No traced conclusion requires a uniquely selected law."
  It does not state that OI has derived a physical probability measure or solved R1.
- If `N_c > 0`, the verdict lists each (c) row with its selection premise and its unresolved
  obligation, and states that R1 remains open for those rows.
- In either case: every existence, invariance, preparation and measure-property assumption stays
  visible in its row; mathematical sufficiency is never reported as physical justification; A1
  remains open and unadopted; nothing in the verdict authorizes Stage 1.

Verdict text is generated from the table counts; it is not written before the rows.

## 7. Controls (fixed in advance)

| Id | Control | Expected property of a valid audit |
|---|---|---|
| K1 | Main's partition-relativity lemma (`M:84`): "In general T = T(φ, 𝒫, μ_H)" | Classified as a statement that holds for every μ_H (it names the law as an input); if a row built on it came out (c), the tests are misapplied |
| K2 | R1-INF Prop. 3 (P-ED) | A conclusion whose only support is P-ED is a selection under (G3)+(G4) and cannot be (a) |
| K3 | Owner technical note | No row's finding is worded as "probability is undefined" or "maximal entropy is undefined" on an infinite lattice; findings concern whether the required law is justified |
| K4 | Main's (NR) corollary (`M:131`) | Uses no invariance; its row's admissible class is root-shared normalized priors |
| K5 | C4 | Has its own consumer trace (GR, Substratum, book) before its class is assigned |
| K6 | Every (c) row | Names either a variation witness or the typicality quantifier, with citation or [W] |
| K7 | Every (a) row | States why every law in `𝒜(φ)` (or every root-shared normalized prior) suffices |
| K8 | No row is resolved by a new derivation | Each [W] is a reading of the use of the law in an existing proof, or a one-line check of an example already on `main` |

## 8. Limits

Paper-only. No Stage 1 work, no lemma L1–L10 attempted, no new law proposed, no manuscript or Lean
edit, no premise adopted or dropped. The trace is bounded by §3's searches and is not a certified
exhaustive census; the coverage section of AUDIT states what was and was not traced.

## 9. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7039208422 | Authorization, scope, classes, decision rule | Provenance; quoted above with author and time |
| #1169 comment 7037422124 | Goal link's priority record | Provenance |
| #1169, #1334, #1055 | Accountability | Provenance |
