# SMD-SRC-1: physical sourcing of SMD for SM Theorem 5 (#1049, #1217). Plan

**WIP / UNVERIFIED. Model-written research plan, paper-only. Nothing here is adopted, proposed for
the manuscripts or authorized beyond the investigation's scope. This file fixes the question, the
definitions, the decision rule, the controls and countercontrols, the stopping conditions and what
counts as each outcome. It is committed alone, before the report, and contains no result. It is a
research plan, recorded without freezing; it is not a frozen preregistration under §A.39 or
§A.50 item 5.**

**Chronology disclosure.** Before writing this file the writer read: unit A's record
(`../theorem5-premise-ledger-20261126/`, PLAN.md, REPORT-r3.md in full, PRESERVATION.md); SM:130–138,
SM:286–300, SM:305–345 and SM:370–376 at [P]; lane 2's REPORT-r2.md §4.1–§4.4
(`../complex-carrier-20261126/`); the successor assessment (#1169 comment 7191949320); and the two
authority records quoted below. While reading, the writer formed, without writing or checking them, a
candidate positive route (spreading of test functions under the dispersive linear map, combined
with a clustering bound) and two candidate countercontrols (the uncoupled point μ = 0, and finite
mixtures of Gaussian states). The decision rule below is fixed as a rule over outcomes, not as an
expected result, and every outcome class it lists is admissible.

- **Accountable Issues:** #1049 and #1217; programme #1169.
- **Authorization:** owner decision (account `amaybaum`, #1169 comment 7200549806, created
  2026-11-26T18:30:55Z; decision stated as received 2026-11-26T18:30Z), item 4: "Authorize all three
  ranked scientific investigations — SMD sourcing, uniform norm control and F-slice — at paper-only
  level, with independent review and bounded stopping conditions." Operations under standing work
  package WP-2, scientific research, whose record is #1169 comment 7199704501 (account `amaybaum`,
  created 2026-11-26T17:49:03Z). The package starts no investigation and never executes a frozen
  procedure, trial or dispatch.
- **Goal link (§A.47).** It serves #1049 and #1217 (both tier Foundational). The investigation
  decides, for each clustering notion of §2, whether SMD, an unstated condition on the state that
  SM Theorem 5's physical reading needs (unit A, ledger item SMD and step P2d), follows from
  stationarity under the stated linear dynamics together with that clustering notion, or fails
  under them. Rank 1 of the successor assessment. It does not decide H-PF, TPC, L-SDS themselves,
  H-ZM, the owner readings O5 of unit A, or any manuscript wording.
- **Pinned main commit [P]:** `a8d4ab969e274dc6ba25cbc6021da909d5aec814`. `papers/SM.md` is
  unchanged between unit A's pin `353a066f` and [P] (`git diff --stat` empty), so unit A's SM line
  citations carry over.
- **Writer:** the designated writer of this investigation; branch
  `research/smd-sourcing-20261126`. No push and no GitHub write by the writer.

## 0. Labels

- [A]: exact hand algebra or proof written here, unreviewed. [W]: reasoning here, unreviewed.
- [I]: an imported external theorem, cited with its hypotheses as the writer recalls them; not
  re-checked against the source text in this investigation (no external access is used). A result
  resting on [I] is conditional on it.
- [U-A]: a result of unit A's REPORT-r3 (reviewed paper derivation, partially verified).
  [L2]: a result of lane 2's REPORT-r2 (reviewed paper derivation, partially verified).
- [C]: a local computation recorded in this directory: exact (rational arithmetic) where it
  certifies an identity, floating point only where it illustrates.
- Premise statuses in the report: proved / conditional / posited / open.

## 1. Question

**Q.** On the carrier Z = Z^d (d ≥ 1; d = 3 physical), at M = μI_6 with abs(μ) < 1, under the
observer-level linear update of SM:314 written as the real lift F = F_s ⊗ I_6,
F_s(u, v) = (v, A_s v − u), A_s = (μ/d) Σ_j (T_j + T_j⁻¹) (unit A §1): does stationarity of the
state under F (L-SDS), together with spatial clustering, force SMD? Otherwise, is there a
counterexample satisfying the same assumptions?

**SMD** (unit A, ledger item SMD): Stab_{U(6)}(ρ) = Stab_{U(6)}(C), where ρ is the state (a Borel
probability law on the configuration space X = ((R^6)²)^{Z^d} of pairs (u, v) = (φ(t−1), φ(t))),
C is its second moment, and U(6) acts through R(w) = I ⊗ X + J_s ⊗ Y for w = X + iY, J_s the
positive-frequency complex structure of F_s ([L2] Theorem 1Z; unit A §1).

**Premises held fixed throughout** (the "fixed set"; their statuses are unit A's and are not
changed here): H-link with m = 1; H-cust's kinetic clause (supplied at M = μI_6); O-equivariance of
Σ; distinct block values; linear offset-free branch (SM:312–316); H-PF; TPC under reading r2; L-SDS.
A positive result must not use a premise outside the fixed set and the clustering notion under
test; a countercontrol must meet every premise of the fixed set and state which clustering notions
it meets.

**Range.** abs(μ) < 1, with μ = 0 (the uncoupled point, A_s = 0) treated separately as a boundary
case of the stated branch. μ = 1 (massless; the zero mode, unit C's H-ZM) is excluded and recorded
as an open node. The finite torus T is out of scope except as a remark: unit A's Propositions A
and B stand there, and clustering is a thermodynamic-limit notion.

## 2. Clustering notions under test

Ordered from weakest to strongest; each later one implies the earlier ones for translation-invariant
states with the stated moments (to be checked in the report where used):
- **K0:** translation ergodicity.
- **K1:** translation mixing (correlations of local observables factorize at large separation),
  without rate.
- **Kα:** uniform strong (α-) mixing with a summable rate, and uniformly bounded moments of some
  order 2 + δ.
- **K2 (cumulant clustering):** finite moments of all orders, and for every r ≥ 3 the joint
  cumulants (truncated r-point functions) of the site variables are summable in all but one site,
  uniformly in that site.
- **K3:** finite-range dependence: the σ-algebras of two regions at distance > R are independent,
  for some R; with uniformly bounded fourth (or all) moments.

The report may add a notion only if it is stated before the result that uses it, and it may not
re-define one of these.

## 3. Decision rule (fixed before any result)

For each clustering notion K of §2, separately:
- **POSITIVE(K)** iff the report gives a proof, labelled [A] (or [A] together with named [I]
  imports, giving a conditional positive), that every state on the range of §1 meeting L-SDS, K and
  the stated moment condition satisfies SMD, and CC-N and CC-E are green.
- **OBSTRUCTION(K)** iff the report gives a witness ρ meeting L-SDS, K and every premise of the
  fixed set, with Stab_{U(6)}(ρ) strictly smaller than Stab_{U(6)}(C), with an itemized witness
  check (CC-W).
- **OPEN(K)** otherwise, with the strongest partial result and the precise remaining gap.

A POSITIVE(K) implies POSITIVE for every stronger notion; an OBSTRUCTION(K) implies OBSTRUCTION for
every weaker notion. If the two would ever meet in contradiction, the investigation halts.

**Verdict sentences, generated from the per-notion table and printed only over green controls:**
- "Stationarity and clustering force SMD" is printed only with the weakest notion K for which
  POSITIVE(K) holds, its conditional imports, and its range.
- "Stationarity and clustering do not force SMD" is printed only with the strongest notion K for
  which OBSTRUCTION(K) holds.
- Every notion in neither class is printed as open, with its gap.
- No sentence is printed about a notion not in §2.

**Consequence for #1217 and #1049, stated with conditions.** A positive result replaces SMD in unit
A's ledger by its hypotheses (L-SDS, the clustering notion, the moment condition, the range); it
does not derive SMD from SM's stated premises unless those hypotheses are themselves stated there,
which the report checks by grep and reading. Whether that replacement is adopted is the owner's
(§A.29, §A.50 item 6); the report proposes nothing.

## 4. Controls and countercontrols

A verdict printed over a failed or vacuous control is void.
- **CC-N (non-vacuity).** For each POSITIVE(K), exhibit a state meeting K, L-SDS and the whole fixed
  set, with distinct block values. Without one, POSITIVE(K) is vacuous and is reported as such.
- **CC-K (clustering is load-bearing).** Exhibit a state meeting L-SDS and the whole fixed set,
  failing every clustering notion of §2, and violating SMD. If none is found, the report states
  that the use of clustering in the positive result is not shown to be necessary.
- **CC-D (dispersion is load-bearing).** At the boundary point μ = 0, exhibit a state meeting K3
  (hence K2, Kα, K1, K0 where applicable), L-SDS and the fixed set, violating SMD; and identify the
  line of any positive proof that fails there. A positive proof that does not fail at μ = 0 proves
  too much and is void.
- **CC-G (reproduction).** Re-derive that a centred Gaussian state satisfies SMD (unit A, CC3),
  including the step that R(w) is defined almost surely on the state's support.
- **CC-E (exact identities).** Every identity a witness rests on (F-invariance FCFᵀ = C, positivity,
  translation and cubic invariance, J-Hermiticity) is checked by exact rational arithmetic on a
  small torus or by exact symbolic algebra, with code and output recorded here. Floating point does
  not certify these.
- **CC-X (illustration only).** Any spreading or decay statement used in a proof may be illustrated
  numerically, at μ ≠ 0 and at μ = 0; the illustration certifies nothing and carries no verdict.
- **CC-W (witness check).** Every witness carries an itemized table: each premise of the fixed set,
  L-SDS, each clustering notion of §2, and SMD. A missing line voids the witness.
- **CC-P (pin).** Quoted lines are re-read at [P].

**Skepticism on the favourable branch (§A.31).** A positive result is pressure-tested against CC-D,
CC-K and the mean (offset) case before it is accepted; the report states explicitly what the
positive result does not show (in particular, whether L-SDS, the clustering notion or the moment
condition is a stated premise of SM).

## 5. Productivity test (fixed before work, §A.31)

The investigation is a gem iff it yields at least one of:
- (S1) POSITIVE(K) for some K of §2, with CC-N, CC-D and CC-E green;
- (S2) OBSTRUCTION(K) for some K that includes translation mixing (K1 or stronger);
- (S3) an identification of a load-bearing hypothesis of the infinite-lattice route not recorded by
  unit A (the "premise audit" the successor assessment asks for), with a countercontrol.

Non-gems: restating unit A's O3; a reproduction of Proposition A on T; relabelling. Findings are
classified NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE.

## 6. Stopping conditions

Stop when the first of these holds:
- the decision rule has assigned each notion of §2 to POSITIVE, OBSTRUCTION or OPEN with its gap
  stated, and the controls have run;
- a bounded effort, of the order of unit A (a few depth-first passes), is exhausted; the remaining
  gap is then stated precisely;
- a result would need a premise outside the fixed set and the clustering notion under test: it is
  recorded as such and the investigation ends on that branch; adoption is the owner's (§A.29,
  §A.50 item 6).

**Halt** (the report records the halt and prints no verdict): a control fails; a provenance
anomaly (§A.26); a positive and an obstruction for the same notion.

## 7. Exclusions

- No manuscript, ledger, census or registry edit; no edit of unit A's or lane 2's records.
- No adoption, weakening or change of any premise.
- No execution of frozen procedures, trials or dispatches; no Lean build. Only small local control
  computations, recorded here.
- No GitHub writes and no push by the writer.
- No claim for the Z/q level, for the nonlinear case, or at μ = 1.

## 8. Review requirement and deliverables

The report is reviewed, before any acceptance, by an independent non-author reviewer at an exact
commit, who checks each control, the claim/evidence boundary, every displayed equivalence one
direction at a time (§A.34), the generation of the verdict from the table, and the §A.42 item 8
tracing. A model review is evidence of review, not independent mathematical verification (§A.46).

Deliverables: this PLAN.md, as its own commit; then REPORT.md, with the per-notion table and
generated verdict, every premise labelled, each result's scope, the controls and countercontrols
with their code and output, the productivity verdict, open nodes, off-`main` tracing and a
verification-status table.
