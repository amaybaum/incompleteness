# Q-β b-consumption trace (#1049, lane 1) — PLAN

**Standing: WIP / UNVERIFIED. Paper-only research record.** This file fixes the question, the
consumer list, the classification conventions, the decision rule, the countercontrol, the
productivity test and the stopping rule. It is committed alone, before `REPORT.md`, and contains no
classification.

**Chronology disclosure.** Before this file was committed the writer had read the sources named in
§3 and had done hand algebra on several consumers. The decision rule and the conventions below are
fixed as rules, not as expected results, and this file carries no chronological weight beyond its
commit order (compare A5-Q4-STAGE2D §8.2). It is not a §A.39 preregistration and freezes nothing.

**Authorization.** Owner decision (amaybaum, 2026-11-26T06:25:53Z, #1169 comment 7184425769),
lane 1, #1049, approved as written: "Determine which results genuinely depend on microscopic
linearity and the zero-offset condition." Restrictions carried from the same decision: paper-only
research, no computational experiments, no manuscript changes, no adoption of new premises, no
automatic merges. The owner also wrote: "A rigorous negative result or counterexample is as valuable
as a positive derivation. Do not favor conclusions merely because they support OI."

**Goal link (§A.47).** #1049. The work decides, for each consumer of A5, whether its use of the zero
offset b = 0 is confined to the linear part, removable by a static uniform shift, or located on the
resonant uniform sector; and with that, which branch of the decision rule of §5 obtains for
criterion 2 of #1049 in sense (1). It does not decide A5's status, any selection principle (Q-γ), or
Q4b and Q4c.

**Pin.** `main` = `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`. `SM:n`, `Sub:n`, `Main:n` denote
line n of `papers/SM.md`, `papers/Substratum.md`, `papers/Main.md` at the pin. The three manuscript
files are identical at the pin and at `e2e2a623` (the pin of REPORT-r5), so REPORT-r5's line numbers
carry over unchanged. Kernel statements are read at the pin; nothing is built.

***

## 1. Question

**Q-β** (REPORT-r5 §1.4 and §5, on `main` under
`verification/programmes/substratum/a5-linear-affine-20261104/reassess-1049-20261125/`): does any
result whose other support stands consume b = 0 of the substratum rule, rather than only its linear
part? REPORT-r5 records that whether every consumer's use of b = 0 reduces to the resonant uniform
A₁ locus is "not traced"; this record is that trace.

For each consumer, two columns are recorded:
- **class** (a), (b) or (c), §4;
- **linearity level**: whether the consumer needs linearity of the substratum rule, or only
  linearity of the lift (POSIT-MIN D1(b); SM:224, SM:232).

Only affine offsets are in scope: rules F(x) = Ax + b with A additive. Genuinely non-affine rules
are outside Q-β and are not classified here.

## 2. Consumers (re-pinned at the pin in `REPORT.md`)

1. A5-LA D1–D16 (`A5-LINEAR-AFFINE.md` §2), each re-pinned.
2. Stage 2(d) on the Σ-route: Sub:163; SM Theorem 5 (SM:340).
3. Theorem 23 (Sub:193, with Lemma 23.0 at Sub:189).
4. SM's shell-sampling site (REPORT-r5's SM:1416).
5. The four kernel consumer modules of H-D `A5S-1b`: `SubstratumInterfaceAudit.lean`,
   `HydroSourceAudit.lean`, `StochasticInterface.lean`, `HexLatticeGas.lean` (re-enumerated at the
   pin).

A further site met while tracing a listed consumer is recorded beside it, labelled as outside the
list, and does not change the list.

## 3. Inputs and labels

- [K] kernel theorem on `main`, statement read at the pin.
- [P] manuscript statement at the pin.
- [D] partially verified derivation in a model-reviewed record: A5-LA, Q4 (`A5-Q4-STAGE2D.md`),
  Q3 (`q3-a6-offsets-20261108/ASSESSMENT.md`).
- [R] partially verified reviewed research record: POSIT-MIN
  (`verification/audits/foundations/posit-min-20261120/AUDIT.md`), OA-1, H-D
  (`round-h-d-a5-status-adjudication/result.md`).
- [A] / [W]: exact hand algebra / reasoning, unreviewed. REPORT-r5's own [A]/[W] steps keep their
  label and are partially verified.

[D], [R] and REPORT-r5's [A]/[W] inputs are used only as labelled conditional inputs. Q4's G1 claim
("u_R has no home for any lift") is known to be invalid and is not used. Content not on `main`
(for example #1226) is provenance only; anything used from it is re-derived here.

## 4. Classification conventions (fixed before classification)

**Notation** as in A5-LA: second-order rule x(t+1) = F(x(t)) − x(t−1); affine F = A + b; phase map
Φ = τ_β ∘ L with L(u, v) = (v, Av − u), β = (0, b); for translation-commuting rules b = b𝟙 is
uniform (A5-LA B0.3(a)) and A𝟙 = κ𝟙. The **resonant uniform sector** is the uniform two-slice
subgroup C at κ ≡ 2 (mod q) on the substratum, or at κ = 2 on the lift; on the six-link carrier
with H-b (Q4 N0) it is the uniform A₁ sector at μ_{A₁} = 1. For a single-component rule the site
value is invariant under the cubic group, so its uniform sector is the A₁ analogue; this identification
is a convention of this record.

**Classes**, assigned to a consumer's conclusion as the manuscript or record uses it, per locus:
- **(a)** the conclusion holds for every offset b in the class considered, by an argument that uses
  only the linear part L of the rule or of the lift;
- **(b)** the conclusion uses b = 0, and holds for b ≠ 0 wherever a static uniform shift removes b
  (b ∈ (κ − 2)ℤ/q, A5-LA R3; owner Q2 reads the shift as a relabelling), and the consumer's stated
  scope contains no resonant-locus case on which it fails or is unestablished;
- **(c)** the conclusion fails, or is not established, for some b ≠ 0 on the resonant uniform
  sector, where no static uniform shift exists.

A consumer's class is the worst class over the loci its stated scope covers; the per-locus classes
are recorded. Items that do not consume A5 (definitions, witnesses of A5 or of its failure, results
holding for every `Rule`) are recorded as **n/a**, with the reason.

**Reading.** "The reading the manuscript states" is the reading stated in the manuscript text at the
pin, at the consumer's own site and at the sites its statement or proof cites. Where the text states
more than one reading for one consumer, the consumer is classified under each. A placement in (c)
that holds conditionally on Q4c, on SM:232's bridge or on H-b counts as a placement in (c), with its
conditions recorded. Where a class depends on Q4b (rule or coupling stabilizer; linear or affine
elements), both branches are recorded and that node stops.

**Offsets.** Uniform offsets only, as exact translation commutation gives. Offsets under A4 "up to
gauge" (non-uniform) are recorded as open where they matter.

## 5. Decision rule (verbatim)

"If no consumer falls in class (c) under the reading the manuscript states, the outcome is
'unnecessary in sense (1) at stated scope' (criterion 2 of #1049). Otherwise #1049 reduces to Q4c,
conditional on SM:232."

Applied with §4's reading convention: the first branch obtains only if no reading the manuscript
states places any consumer in (c). The verdict text in `REPORT.md` is generated from the
classification table.

## 6. Controls

- **Countercontrol (required).** S1 (SM:240: N = 4, q = 5, F_i(x) = x_{i−1} + x_{i+1} + 1, κ = 2)
  at Main's absolute interface must come out with a labelled difference from its linear part. If it
  does not, the classification is void.
- **Preserved results.** A5-LA C1–C8 must not be contradicted.
- **Internal controls for new [A] steps.** Each new step states its b = 0 limit, which must
  reproduce the linear statement, and, where a fixed point exists (A5-LA B0.3(e), (f)), the case in
  which the step's obstruction must vanish.

## 7. Productivity test (fixed now)

The result is a gem iff at least one consumer moves from REPORT-r5's "not traced" to a pinned class,
and the lane either places a consumer in (c) or proves none is there under the stated reading, or
exposes an unrecorded use of b = 0 or of substratum linearity. Anything less is record-only.

## 8. Stopping rule

- Every consumer is classified with source pins.
- Where a class depends on Q4b, both branches are recorded and that node stops.
- Otherwise the trace stops after 3–4 passes with no NEW finding (§A.31).

## 9. A1 independence

For each consumer the record states its row membership in
`verification/audits/foundations/a1exit-ledger-20261120/rows.json` (and its site map), so that the
trace can be re-pinned after A1 retirement, and any use of finite q. The trace itself uses no
finiteness premise: a statement about finite q is made only where the consumer is itself a statement
about finite q, and is labelled so.

## 10. Excluded

No search for or adoption of a selection principle (Q-γ; PM-D5 is paused). No change to A5's status.
No use of Q4 G1. Nothing is frozen. No computation is run.
