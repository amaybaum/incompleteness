# Focused review of GAMMA-1 unit G1, r2

**Objects.**
- At PR #1294 commit `fcf24c9a355a4712b58d1ce297380b9c6a8cff95`, in
  `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`:
  - `GAMMA-G1-r2.md`, blob `44ff0b53` (cited r2:N);
  - `RESPONSE-GAMMA-G1-r1.md` (RESP).
- r1 is unchanged at blob `46697d9c`.

**Inputs re-read.** U4-CALC-r2, blob `bef634e2`, sections cited by r2. The owner record #1169
c.6892224647 (`amaybaum`, 2026-11-15T09:17:55Z), read through the API: "2b r2 (`U4-CALC-r2.md`, blob
`bef634e2` …) is accepted". U4 r3 and its review are on the branch, and the U4 r3 review was not used.
No external source was read.

**Reviewer.** Independent, non-author. Read-only; hand checks only.

## Verdict: ACCEPT WITH CHANGES

All 20 r1 findings are resolved. Finding 8 is resolved in form, but the new statistics it introduced
fail on spatial patterns (N2). The `K_P` repair, the bookkeeping for each encoding, the NC-rep
correction and the O11 extension all check by hand.

Two new required findings concern definitions added in r2 itself:
- the credit-set quantifier leaves no observable creditable on the declared list (N1);
- the qualitative-feature statistics of `κ_cmp` call false misses on patterns with an envelope,
  including the exact standard law (N2).

Both have specified remedies. A focused confirmation of N1 and N2 suffices; the rest of r2 needs no
further review.

## Item 1. r1 findings, one by one

| # | Status | Where in r2 | Note |
|---|---|---|---|
| R1 credit set per phenomenon | **RESOLVED** | 618–626, 713–730, 753–764 | Clause removed; Q6 is now a condition on the whole result; NC-γ6 added. See N1 for the new quantifier |
| R2 `K_P` | **RESOLVED** | 216–257 | Re-derived in item 3 |
| R3 masses per encoding | **RESOLVED** | 283–319, 470–478, 751 | Checked in item 4 |
| R4 NC-rep versus AV-t | **RESOLVED** | 676–691 | The background inequality is correct (item 4) |
| R5 visible-herald route | **RESOLVED** | 371, 386–390, 822 | The MR★:639 versus OA1:328 reconciliation is sound |
| R6 `μ` scope and conditions | **RESOLVED** | 392–405 | Factor-set condition and PROVISIONAL tags carried |
| R7 O11 scope | **RESOLVED** | 375, 377, 786–797, 869–875 | Blocking by a prepared content is not classified; the stated ground is adequate |
| R8 qualitative misses | **PARTLY** | 557–583, 612 | Counted and separated, as required. The statistics are defective (N2) |
| R9 κ-orb weight; H-ens | **RESOLVED** | 526–555 | all/some/none, with the `μ`-mass beside it and no weight; H-ens named |
| M10 `κ_det` | **RESOLVED** | 431–460 | See item 7 |
| M11 E-decl | **RESOLVED** | 158–164 | |
| M12 PROVISIONAL tags | **RESOLVED** | 369, 706 | |
| M13 screen-part equalities | **RESOLVED** | 645–656, 668–670 | |
| M14 ledger observer | **RESOLVED** | 132–134 | |
| M15 the wording on `D` | **RESOLVED** | 201–204, 520, 837 | |
| M16 OCP:45 | **RESOLVED** | 183–185 | |
| A1 | **RESOLVED** | 260–263, 840–842, 871–873 | |
| A2 | **RESOLVED** | 843–846 | Recorded as unchecked |
| A3 | **RESOLVED** | 748, 752 | |
| A4 | **RESOLVED** | 577, 612 | |

## Item 2. Diff from r1 to r2 against RESP

Every RESP row corresponds to a change at the cited place, and I found no change without a row.
Changes beyond the findings (RESP, last section) are also accounted for:
- inputs moved to U4 r2 and CALC r2;
- CALC-based rows at r2:377, 380–381;
- the NC-copy slot for G2 at 697–700;
- G1-F8, AW-det and AW-ens;
- owner question 5.

The CALC claims cited (Theorem 1(c), Theorem 1′, Prop. 1.4, Instances 1.1–1.2, Prop. 2.8) match CALC
r2's statements.

Two stale items:
- r2:57–58 and :856 say CALC r2's "owner acceptance not on record". It is now on record
  (c.6892224647), so update both (minor, M-a).
- PROVISIONAL tags point to U4 r2 sections. U4 r3 now exists, so re-point them when U4 is accepted
  (advisory).

## Item 3. `K_P` by hand

Notation: `c_π(m)` is the detected mass in 𝔇 with marker report `m ≠ ∅`, per incident particle, in
the run with only `π` open.
- **Formula.** Let `w_π = Σ_m c_π(m)/Σ c`, and let the joint over detected runs be
  `P(π, m) = c_π(m)/Σ c`. Wootters–Zurek betting gives `L = Σ_m max_π P(π, m)`. Since
  `2 max(u, v) − u − v = |u − v|`, `2L − 1 = Σ_m |c_L(m) − c_R(m)| / Σ c = K_P` (r2:224–229).
  Correct.
- **Perfect marker.** `c_L = (L: d_L)` and `c_R = (R: d_R)`, so `K_P = (d_L + d_R)/(d_L + d_R) = 1`
  for all `d_L, d_R > 0`.
- **Position of the block.** Blocked runs reach no screen cell, so they are outside 𝔇 whether they
  carry a mark or `∅`. `K_P = 1` either way. The r1 dependence (1/2 or 0) is gone.
- **Uninformative marker.** `|d_L − d_R|/(d_L + d_R)`, which is the predictability `P`. Correct.
- **Efficiency.** A common factor on all `η_m` cancels, so only efficiency ratios enter. Correct.
- **NC-copy.** `K_P = 1` with `V = 1` gives `K² + V² = 2`. Since `K ≤ D`, this lies outside
  `D² + V² ≤ 1`. NC-copy is now reachable (r2:692–695).
- **Advisory (A-b).** 𝔇 excludes `m = ∅`, so a null report that depends on the path is discarded
  information. Reporting `f_∅` (r2:233) shows the excluded mass but not whether it depends on the
  path. Report beside `K_P` the same formula with `∅` kept as an outcome; it needs no new datum.

## Item 4. Masses, sum rule and equal marginals, by hand

- **E-set.** The incident events are disjoint and the total mass is `μ(z = a)`.
- **E-prep.** Total mass `μ(𝔄_a)`, with `(a, ¬E)` inside it.
- **E-read.** One event `𝔈_*`, with each projection of total mass `μ(𝔈_*)`. The joint law is
  `L^full`, the sum over distinct events, so shared runs enter once. `L^full ≠ Σ_a L_a^full` holds
  exactly when E-read encodes more than one protocol, as stated.
- **Normalization.** `κ_norm` (r2:470–473) is consistent with this.
- **Sum rule.** `ρ_{a5}` maps `𝓒_A` by a total function `π_P`, with `∅` among its values. So
  `Σ_m (ρ_{a5})_* L^full_{a5} = (ρ_{a4})_* L^full_{a5}`, with both sides of mass `μ(𝔈_{a5})`. The
  same holds for `π_C`. This is valid in every encoding, as r2:328–332 states.
- **Equal marginals under E-read.** The three protocols share one event and one record map, so
  `L^full_{a4} = L^full_{a5} = L^full_{a6}` and the screen marginals are equal. Correct.
- **Under E-set and E-prep.** No equality across protocols is claimed, which is correct.
- **NC-rep background (r2:678–680).** Let `V_sub = (M − m)/(M + m − 2b)` and
  `V_raw = (M − m)/(M + m)`. Then `V_raw ≤ V_sub` when `M + m > 2b`. Correct.

## Item 5. NC-γ6 and its conditional labelling

The hand evaluation (r2:755–764) and G1-F8 state that whether QM meets §7.2 "turns on X-2 and X-3",
pending G3. That is labelled conditional, as it should be. The checkpoint row (r2:753) reads as
met: "no clause … fails for it by construction". State its status in the row: **met for (γ←)'s
clauses; open for §7.2's condition, pending G3 and N1** (M-b).

Two further points:
- **The benchmark lacks X-2 and X-3.** NC-γ6 substitutes the OCP benchmark family, a two-port toy
  on `𝒜_6`, which has no X-2 or X-3 laws. The evaluation needs a declared standard-QM reference for
  X-2 and X-3, used only for the structure of the definition (NC-γ2), with its source (M-c).
- **N1 decides the outcome.** Under r2's quantifier the open question is close to decided in the
  negative; see N1.

## Item 6. G1-F1 and the wording on `D`

G1-F1 survives the `K_P` fix (r2:819, :830–838).
- The statistic needs one-path runs with the marker engaged. a2 and a3 specify no marker
  (OCP:20–21), and a4–a6 block no path, so `K` is not a functional of any law on `𝒜_6`. The
  refinement "two programs, not four, under E-read" is correct.
- The `D` wording now matches LIT 1.11, 1.12 and §3: `D = max{K}` is defined, the FULL-read sources
  report `K`, and Dürr's "measured D and V independently" is marked ABSTRACT, method NOT READ. NEW
  stands.

## Item 7. `κ_det` alternative and `κ_cmp`

- **`κ_det`.** `κ_det^part` meets R1 wherever the held value depends on the carrier. Its dark law
  under μ-G, `|C_j|/|states|`, follows from MR★:642. Both variants are declared under NC-γ1, counted
  under NC-γ5's trial count and reported separately. Neither presupposes agreement. Owner question 2
  carries the choice.
- **`k = 3` and the trial count.** Fixed without source values. They do not beg agreement.
- **The qualitative rules.** Not chosen toward agreement, but mis-specified in a way that produces
  false misses (N2).

## New findings

**N1 (required). The credit-set quantifier leaves no observable creditable (r2:715–724, :753–764).**
§7.2 admits an observable `o` only if **every** ceiling member is established to disagree on `o`.
The two members always in `𝒦(o)` fail on different observables:
- C0 (fixed-path particles) fails the additivity defect `Δ` but reproduces single-quantum
  anticorrelation at a beam splitter, since a fixed-path particle exits one port;
- PC-wave fails anticorrelation but reproduces `Δ ≠ 0` and X-1.

Both satisfy `I_3 = 0`: C0 because its probabilities are additive, PC-wave by square-law detection,
as PLAN-G §5.3 records. Reviewer's inference, by hand; G3 confirms first-hand. With C0 extended to
X-2 as `𝒦(o)` requires ("C0 and PC-wave" always), X-1 to X-3 and the two-port fringes each have some
ceiling member agreeing, so the credit set is empty for every model, the quantum benchmark included.
Quantum behaviour is distinguished by a conjunction across observables that no single member
reproduces, not by any single observable. NC-γ6's "turns on X-2 and X-3" is then answered by the
definition, not by G3. This repeats r1's defect at one remove.
- *Required change.* Credit per ceiling member: a native result has nonempty credit when, for
  **every** member `K ∈ 𝒦`, some typed observable `o` exists on which `κ(L)` agrees with the data and
  `K` is established to disagree. This reverses the quantifier order, from "some observable on which
  every member disagrees" to "for every member, some observable on which it disagrees".
- Report, per member, the observables that separate it.
- Re-run NC-γ6's hand evaluation under that form.
- State whether C0 has an X-2 law (a stated construction) or is outside `𝒦(X-2)`.

**N2 (required). The fringe and π-shift statistics misclassify patterns with an envelope
(r2:568–576, :519).**
- *(a) Visibility.* "Present iff `V ≥ 0.5`", with `V = (max − min)/(max + min)` over the cells of one
  channel. Any channel whose envelope approaches zero inside the scan has `V ≈ 1`, fringes or not.
  An envelope with no fringes, such as Kim's `R03`, "an absence of interference" (LIT 1.6), is then
  classified "present". The exact standard law therefore incurs a qualitative miss there.
- *(b) π-shift.* "Shifted iff the cell-wise covariance of the mean-subtracted images is negative."
  Exact hand counterexample, 16 cells:
  - envelope `f = (0×12, 4, 4, 4, 4)`, `g = (·, 1, ½, 0, ½)` on the lit cells, channels `c₁ = fg`
    and `c₂ = f(1 − g)`, which are exactly complementary;
  - both means are ½;
  - the covariance is `12·¼ + (−1.75 + 2.25 − 1.75 + 2.25) = 4 > 0`, which reads "in phase".
  More generally, for fringes fast against the envelope,
  `Cov(fg, f(1 − g)) ≈ ⅛E[f²] − ¼E[f]²`, which is positive when the envelope's coefficient of
  variation exceeds 1. That is typical of a scan across a single-slit envelope, as in Kim's 0–3 mm
  and Walborn's −4 to +4 mm.
- *Consequence.* Both rules create false misses against correct laws. This is the reverse of begging
  agreement, and still disqualifying for a preregistered decision rule.
- *Required change.* Declare local statistics with `I`, for example:
  - fringe contrast from adjacent extrema within a declared fringe period, or the envelope-normalized
    ratio `c₁/(c₁ + c₂)` for paired channels;
  - the π-shift as the sign of the covariance of `c₁/(c₁ + c₂) − ½` with a declared fringe reference,
    or the phase of the Fourier component at a declared fringe frequency.

  Add a control that the OCP and standard two-slit laws classify correctly under each rule, used for
  the structure of the rule only. For quantitative `V`, use the source's own formula and scan (phase
  scan in Schwindt and Ma).

### Minor

- **M-a.** CALC r2's owner acceptance is now on record (c.6892224647); update r2:57–58 and :856.
- **M-b.** State NC-γ6's status in its checkpoint row (item 5).
- **M-c.** NC-γ6 needs a declared QM reference for X-2 and X-3 beyond OCP's two-port table (item 5).

### Advisory

- **A-b.** Report `K_P` with `∅` kept as an outcome, beside the 𝔇 version (item 3).
- **A-c.** Re-point PROVISIONAL citations from U4 r2 to the accepted U4 revision when there is one.

## Checked and not checked

**Checked by hand.**
- All RESP rows against r2.
- The `K_P` identity and its five checks.
- The incident events, masses and pushforward identities for each encoding.
- The background inequality.
- The C0 full laws and `Δ` (OCP's `(+1/2, −1/2)`).
- The CALC citations.
- G1-F1 against LIT and OCP.
- Both κ-statistics, by an exact counterexample and the covariance identity.
- The owner record c.6892224647.

**Not checked.**
- The external sources, including Grangier and Sinha, used here only through standard physics, as
  labelled in N1.
- U4 r2 and r3.
- VER2's CC4 and CC5 scopes.
- CALC r2's proofs beyond the statements cited.
