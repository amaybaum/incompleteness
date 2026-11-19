# PREP-REGRESS-1: the preparation regress, stationarity, and the held-predictability budget

**Standing.** Revision r2 applies the required and recommended findings of the independent review
at `eef4d3ab` ([#1417 c.7019920749](https://github.com/amaybaum/incompleteness/pull/1417#issuecomment-7019920749),
REVISE; §4 proofs accepted) and the owner's OI Review requirements relayed with it (scope of the
conclusion; no irreversible-consumption reading; the reading of item 2). No §4 theorem changes.
WIP / UNVERIFIED author record of a paper-only gem-finding unit (AGENTS.md §A.31,
depth-first form). One independent non-author review is a separate gate. This record adopts no
premise, edits no manuscript, Lean module or registry, and runs no simulation. Small exact checks
are included as controls (§9).

- **Authorization.** Owner `amaybaum`, recorded at
  [#866 c.7019171625](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-7019171625),
  2026-11-19T19:03:20Z: "Proceed as suggested", approving the unit as stated there. Its limits:
  "Paper-only: no simulation, Lean, manuscript edit, premise adoption or merge. A short exact check
  of small cases may be included as a control."
- **Goal link (§A.47), from the authorization.** Decide whether the physical-measurement
  bottleneck for #1169 is a missing mechanism or a missing boundary input. Physical measurement
  sourcing NOT PASSED; A1 OPEN/UNADOPTED.
- **Accountable Issues.** #866 (native preparation source), #1169 (OI projection objective).
- **Snapshot.** `main` at `0d02d8d3b6a53a43168eabead12e1ff675a4d048`. The files cited below are
  unchanged from `b6f11fb9b`, the snapshot named in the assignment (the only intervening change
  adds `A1-P12-GLUE-1.md`, not cited). `Main:n` is `papers/Main.md` line n; other record paths are
  relative to `verification/programmes/oi-qm/reconstruction/` unless they start with
  `verification/` or `book/`.

**Support labels.**

| Label | Meaning |
|---|---|
| [K] | Lean statement on `main`, cited by its record; nothing built here |
| [P] | manuscript statement |
| [R] | research record on `main`, not independently established |
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/prep_regress_checks.py` (exact rational and `log2 3` arithmetic) |
| [LIT2] | literature cited from memory, not re-read for this record; no result depends on it |

Units: all information quantities are in bits; `h₂(ε) = −ε log₂ ε − (1−ε) log₂(1−ε)`.

***

## 0. Summary

1. **Extracted contract (§2).** The screens require the producer regress to end at "an already
   declared and independently justified initial distribution or physical boundary rule or …
   native autonomous history". Native laws are those typed in OA-1: μ-O (derived given the actual
   orbit), μ-G and μ-R (posited, ledger item (iv)); any other law needs independent justification.
2. **Node 1 (exclusion) [W, EC].** Under any invariant law every single-time statistic of every
   fixed block is constant in time; the one-step flux into any event equals the flux out of it.
   No native history raises readiness, held predictability or held-carrier correlation of a fixed
   block in law. The "native autonomous history" disjunct is therefore never a source distinct
   from the law it starts from. Escapes at law level remain: conditioning (cost exactly
   `log₂ 1/μ(E)`), a boundary law, the per-orbit law μ-O (static budget `log₂(|S|/ℓ)` fixed by the
   orbit length ℓ), the record-compatible law μ-R (static budget `log₂(|S|/|U|)` on the orbit
   union `U`), and, without total finiteness, a stationary incoming low-entropy stream.
3. **Node 2 (budget) [W, EC].** Relative entropy to the counting measure is conserved exactly.
   Its coarse-grained part is not monotone (ARROW-1 C.4 is a counterexample). The correct
   statements are an exact transfer identity, a fresh-cell monotonicity under stated hypotheses,
   and a single-time budget: `N` binary target functionals held ε-predictably at one time require
   `D(p₀‖u) ≥ Σ_k (1 − h₂(ε_k))`, with equality attained, provided the targets are jointly balanced
   under `u` (uniform on `{0,1}^N`; the AND of two bits gives `ε = 1/4` at `D = 0`) and the
   predictor block is disjoint from the target block (a copy pair `x = y` predicting each other
   gives two bits at `D = 1`), both blocks fixed. The owner's per-cycle form
   `N(1−h₂(ε))` holds exactly when the `N` results are still held, and still predictable, at the
   time of evaluation; without retention, reversible copy/uncopy cycles run without limit at a
   fixed budget of 1 bit, and exchange records cost 0 bits. The budget is not consumed irreversibly: retained, inert results keep it committed (2.3), and it
   is released when the results are uncomputed (C5).
4. **Conclusion (§6).** Reversible autonomous dynamics cannot create a net statistical supply of
   preparation resources in a fixed block under an invariant law; it can redistribute resources supplied by the
   law or by the boundary conditions. A physical measurement source therefore needs both an
   admissible resource supply and a native mechanism that makes the resource operationally
   available. The result does not exclude measurement interactions, individual trajectories that
   create records, conditioning on observations, or the redistribution of an available resource,
   and it does not remove the need to investigate apparatus mechanisms.
5. **Node 3 (productivity test).** Item 1 is proved; item 2 is resolved partly by proof (§4 forms)
   and partly by counterexample (the owner's monotonicity clause); the controls hold. On the author's
   reading of the fixed test this is a gem, classification ELABORATING, with no NEW item. On the
   owner's reading (relayed for this revision), a rigorous counterexample to the proposed
   monotonicity clause completes that obligation provided the corrected replacement statements are
   proved and all controls pass; it does not count as a proof of the original clause.
6. **Node 4 (proposal only).** Two boundary-posit forms, NEQ-T (time-slice law) and NEQ-O
   (orbit-level), with candidate independent consequences and falsifiers. Neither is hard to vary
   as stated. Nothing is adopted.

***

## 1. Corpus read (§A.19) and what each piece already contains

| Source | Content used | Standing |
|---|---|---|
| `oa-1-20261112/OA-1-REPORT-r5.md:141–143` (D1) | "The unconditional law is the same at every time. Every time-specific preparation, and every new same-time correlation between record and carrier, is conditional on a record event." | [W] in an [R] record |
| same, :156–159 (D3) | `P(Σ_t = σ | E) ≤ μ(Σ_t = σ)/P(E)`; ready cells under μ-G cost `q^{−M}` | [W] in [R] |
| same, :162–174 (D4) | complete in-`V` records under a stationary law make the visible process deterministic on the support; under μ-G, no hidden influence | [W] in [R] |
| same, :100–109 (§1) | measure typing: μ-O derived "the unique invariant measure there"; μ-G and μ-R posited via ledger (iv); "native" relative to (iv) under μ-G, μ-R | [R] |
| same, :316–360 (N1-K, N1-S) | knowing can be native under μ-O (swap 2-cycle); under μ-G selectable preparation fails by retention, "the blank-memory cost" | [W] in [R] |
| same, :556–560 (MP-0a) | "fixed known values on designated cells … declared as the joint initial law"; "a past-hypothesis-type supply of ready cells"; "Main §4.6 supplies only selection" | [R] |
| same, :625 (AW-OA1-2) | "Main §4.6 replaces the past hypothesis's selection role, not its supply role." | [R] |
| `verification/audits/manuscript/arrow-1-20261105/RECOVERY.md:43` (A5) | memory arrow: direction "conditional on a non-stationary preparation and the orientation convention" | [R] |
| same, :396–411 (C.1), :413–438 (C.2), :440–484 (C.3) | no globally monotone state function under finite recurrence; rooted results closed under `φ ↦ φ^{−1}`; under the invariant measure block entropies are reversal-invariant | [EA]/[HA] in [R] |
| same, :486–509 (C.4) | the CNOT example in which the sum of sector entropies rises then falls | [EA] in [R]; reproduced as C1 |
| same, :350–372 (B.9) | the §4.6 selection rule "selects *where* … does not select *which way* … does not supply a low-entropy boundary" | [R] |
| `observer-interface-obsmu-20261104/ANALYSIS.md:529–543` (Lemma P-1) | under Haar measure on a finite abelian group every region is uniform at every `t`, disjoint regions independent | PD in [R] |
| same, :893–900 (H-PREP) | identifying a laboratory preparation with an in-realization conditional is an open, unadopted hypothesis | [R] |
| same, :233–244 | Main limits its past-hypothesis replacement to the selection role; book ch18 states a low-entropy initial condition | [R] |
| `o-ret-routes-20261103/DEFINITIONS.md:177–183` (Lemma C) | `I(c; r′) ≤ D(μ_R ‖ u_R) + H(c′|c)`: "an entropy trade-off", readiness (`D > 0`) or carrier disturbance | statement [R]; its proof is in `ROUTES.md`, not on `main`; used here only as a related statement, provenance |
| `o-ret-routes-20261103/SOURCES.md:96–106` | Landauer (1961), Bennett (1982), Wolpert (1992) as background, "not re-read" | [LIT2] in [R] |
| Main:54 (Lemma 3) | invariant measure unique and uniform on each cycle; counting measure "a selection principle, not uniqueness from invariance alone" | [P] |
| Main:58 | structured priors permitted as "part of the realization datum" | [P] |
| Main:60 | "on the orbit of the actual microstate, the uniform measure is the unique φ-invariant measure; the selection among orbits is fixed by maximal entropy compatible with the observer's records — and an orbit of period p makes at most p states dynamically accessible"; a realization "requiring more than log₂ p bits of predictive memory exceeds its capacity" | [P] |
| `observer-interface-obsmu-20261104/ANALYSIS.md:183–185`, :863–867 (H-OC_orb) | the measure is "the maximal-entropy *invariant* measure compatible with the observer's records"; the rule "does not produce a law at a time slice" | [R] |
| `physical-source-hypotheses-20261118/LEDGER.md:244`, :381 (B20) | H-OC_orb "selects the uniform law on the union of orbits meeting the record event"; "Orbit selection does not identify a prepared laboratory ensemble." | [R] |
| Main:486, :534 (§3.4) | the action-ledger dilation writes "into the action ledger's next blank slot — injective on blank-bearing states"; the structured prior with "the ancilla prepared uniform on the initial register slice" | [P] |
| Main:516 | sustained memory over `K` events needs `m ≳ 2^{K I₀}` only "under the additional hypothesis that the per-event contributions accumulate without hidden-state reuse" | [P] |
| Main:730 (ledger (ii), (iv), (xiv)) | total finiteness open; measure selection "the maximal-entropy invariant measure compatible with the observer's records … not derived"; measurement independence "a posit about the initial condition" | [P] |
| Main:746–766 (§4.6) | observer selection conditional on (EM), rate condition, bounded diameter, canonical typicality, in the iterated-channel description; corollary retitled "observer-selection rule, with its rate condition" | [P] |
| `book/ch18-beyond.md:212`, :218 | "the universe begins in a low-entropy configuration"; "why does the universe start in a low-entropy partition? … a question about *initial conditions* … rather than a question about *dynamics*" | [P] (book) |
| `native-producer-2-20261117/SOURCE-SCREEN.md:29–34, :81–93, :123–135` and #1358 body, "Regress boundary" | admission and regress rules (§2) | [R]; Issue text is planning provenance |
| `native-preparation-source-1-20261110/PREPARATION-SCREEN.md:12–16, :88, :100, :106` | bank is "a proposed incoming resource"; "permitted realization data" does not source it; "'Zero,' 'vacuum,' 'low entropy' and 'available blank' cannot be substituted for one another"; "Mathematical bijectivity supplies neither an observer-operated inverse nor fresh banks." | [R] |
| `controller-preparation-1-20261108/SELECTION.md:105–132` | first missing link: no native interaction, no common input/resource law, "no free reset or blank supply" | [R] |
| `native-apparatus-source-20261113/ASSESSMENT.md:12, :90–94, :153–159` | first missing ingredient: "producer/request interface for the common incoming ready resource, with its lawful boundary/initial supply"; the elementary counting fact under μ-G; ch18's boundary "not a demonstrated map into local addressable blanks" | [R] |
| `physical-source-hypotheses-20261118/LEDGER.md:198, :245, :405, :479` | PSH-NEQ; A05 "non-stationary preparation"; A01 cosmic boundary "an initial condition; why it is selected and how a detector accesses it are separate questions"; an invariant state is "a possible supplied state in the P8 source" | [R] |
| `verification/audits/foundations/a1-p8-history-bridge-20261119/RESULT.md` | full-history next-read bound for a stationary reversible register with a fresh input law | [R], reviewed ACCEPT WITH NITS |

**What already exists, and what does not.** D1 states stationarity and that time-specific
preparation is conditional. D3 bounds heralded preparation by event mass. Lemma C gives a one-write
entropy trade-off. ARROW-1 shows that a direction needs a non-stationary preparation and that the
sector-entropy sum is not monotone. AW-OA1-2 separates selection from supply. Not on `main`: a
statement that the contract's "native autonomous history" disjunct is empty as a distinct source;
an exact conservation/transfer identity in the contract's terms; a multi-record budget with its
hypotheses and necessity counterexamples; a quantitative account of the budget carried by the
per-orbit law μ-O.

***

## 2. The extracted native-source contract

The screens applied the following contract. Each clause is quoted or cited.

- **NSC-1 (admission).** "an actual native update on main; a structural difference from the old
  fixed-ring cut; and independent physical motivation and an eligible initial/boundary-law or
  autonomous history source" (`native-producer-2-20261117/SOURCE-SCREEN.md:29–32`).
- **NSC-2 (regress endpoint).** "Trace the proposed preparation/request dependency backward to an
  **already declared and independently justified initial distribution or physical boundary rule**
  or to native autonomous history. … If the allowed law is an existing posit, report the
  conclusion **conditional on that posit**" (#1358, "Regress boundary", rule 1; Issue text,
  provenance). Support on `main`: `native-producer-2-20261117/SOURCE-SCREEN.md:29–34` ("independent
  physical motivation and an eligible initial/boundary-law or autonomous history source. An already
  posited, independently justified boundary law may support a conditional result."). The on-`main`
  text says "initial/boundary-law or autonomous history source" where #1358 says "initial
  distribution or physical boundary rule or … native autonomous history", and it does not repeat the
  proved/standard/posited/open labelling.
- **NSC-3 (exclusions).** "Do **not** add a newly tuned prepared producer state, a herald outside
  the stated physical model, postselection, a special hidden distribution, a fresh memory cell or
  a secondary controller" (#1358 rule 2; also `SOURCE-SCREEN.md:132–135`).
- **NSC-4 (stop).** "stop at that first unsupported step. A regress cannot be declared solved by
  renaming the producer's initialization" (#1358 rule 3; provenance). Support on `main`:
  `SOURCE-SCREEN.md:84–86` applies the rule ("No source in this bounded packet identifies their
  physical production or licenses them as the regress endpoint required by #1358") and the record
  stops there (:5, "No derivation follows the source stop"). The on-`main` text states the stop as
  applied; it does not state the renaming clause.
- **NSC-5 (what "independently justified" requires).** "An initial law is not rejected merely
  because it is an assumption: the missing qualification is independent physical justification
  for this particular resource/preparation law" (`SOURCE-SCREEN.md:89–92`); "An arbitrary
  candidate input law does not become such a boundary law by having appeared in an earlier
  research file" (:33–34); "CONDITIONAL is not awarded merely for a supplied candidate prior"
  (:126–127); a permitted realization datum is not a source
  (`native-preparation-source-1-20261110/PREPARATION-SCREEN.md:88`); a stated cosmological
  boundary is not "a demonstrated map into local addressable blanks, requests and renewed
  apparatus" (`native-apparatus-source-20261113/ASSESSMENT.md:94`).
- **NSC-6 (what counts as native).** Supplied by `(φ, partition, μ, A)` with a stated μ; μ-O is
  derived, μ-G and μ-R rest on ledger item (iv) (OA-1 r5 :100–109; Main:54, :60, :730 (iv)).
- **NSC-7 (ready, request, record).**
  - *Ready:* "fixed known values on designated cells, independent of settings and carrier" (MP-0a,
    OA-1 r5 :556–560); "'Zero,' 'vacuum,' 'low entropy' and 'available blank' cannot be substituted
    for one another" (`PREPARATION-SCREEN.md:100`).
  - *Request:* a setting chosen and recorded, independent of the carrier (ledger (xiv)), with the
    carrier's held conditional law depending on it (N1-S, OA-1 r5 §1 table).
  - *Record:* held (a function of present `V`, or the MP-0b history convention), correlated with a
    functional of `Σ`, residual handed on (N3); outcomes, heralds, failures and residual known at
    the end (N4); #1358 adds "a **one-tick persistent record** readable on the same physical
    carrier, and a second measurement retaining the first result".

**Reading used below.** The endpoint of NSC-2 is a law on the joint state (the screens speak of
"initial law", "common incoming law", "ready distribution"). "Native autonomous history" is read
as: a law admissible under NSC-6 without a further posit, together with the evolution under the
fixed φ. Every result below is stated for laws; a per-trajectory remark is in §4, node 1.6.

***

## 3. Setting and notation

- `S` finite, a product of finite cells (ledger (viii)); `φ: S → S` a bijection; `p_t = φ^t_* p₀`
  for `t ∈ ℤ`. `u` is the counting probability on `S`. `u` is φ-invariant for every bijection, and
  on a product of cells it is the product of the uniform cell laws.
- Measurable case: `(S, 𝓑)` a standard Borel space, `T: S → S` bimeasurable bijection, `μ` a
  `T`-invariant probability.
- For disjoint factor blocks `A`, `B`, `Rest`: `H(·)`, `H(·|·)`, `I(·;·)` are Shannon quantities of
  `p_t`; `D(p‖q)` relative entropy.
- **Held predictable content of a block `H`:** `K_t(H) := log₂|H| − H_{p_t}(H | Rest)`, where
  `Rest` is the complement of `H`. `0 ≤ K_t(H) ≤ log₂|H|`. `K = 0` exactly when `H` is uniform and
  independent of `Rest`; `K = log₂|H|` exactly when `H` is a function of `Rest`.

***

## 4. Depth-first walk

### Node 1 — exclusion lemma

**1.1 Stationarity [W].** *If μ is φ-invariant (finite case) or `T`-invariant (measurable case),
then `p_t = μ` for all `t ∈ ℤ` when `p₀ = μ`; for every event `E`, `P_t(E) = μ(E)`; and for every
finite collection of fixed blocks the joint law of their contents at time `t` does not depend on
`t`.* Proof: `φ^t_* μ = μ` by invariance, applied to `t` and, through `φ^{−1}`, to `−t`; the block
contents at `t` are fixed coordinate functions of the state at `t`. ∎
Check: OA-1 D1 states the same. Verdict: proved; CONFIRMING.

**1.2 Flux balance [W, EC C8].** *For a bijection φ of finite `S` and any `E ⊆ S`,
`|{s ∉ E : φs ∈ E}| = |{s ∈ E : φs ∉ E}|`. For an invariant μ in the measurable case,
`μ(T^{−1}E ∖ E) = μ(E ∖ T^{−1}E)`.* Proof: `{s ∉ E: φs ∈ E} = φ^{−1}E ∖ E` and
`{s ∈ E: φs ∉ E} = E ∖ φ^{−1}E`; both equal `|E| − |E ∩ φ^{−1}E|` because `|φ^{−1}E| = |E|`; the
measure case is the same computation with `μ(T^{−1}E) = μ(E)`. ∎ Check: exhaustive over all 24
bijections of a 4-set and all 16 events (C8); a non-bijection violates it (C11b). Verdict: proved.
Reading: every state that becomes ready in one step is matched by one that ceases to be ready.

**1.3 No production of block statistics [W].** *Under any invariant law, `P_t(ready)`, `K_t(H)`,
`I_t(H; C)` and `H_t(H | C)` are constant in `t` for all fixed blocks `H`, `C`.* Proof: each is a
functional of the joint block law at `t`, constant by 1.1. ∎ Corollary: a protocol whose success
requires `K_{t₁}(H) > K_{t₀}(H)` for a fixed block `H` (a log that is uninformative at `t₀` holds
predictable records at `t₁`; a register unready in law becomes ready in law) cannot run under any
invariant law. Under an invariant law, held predictable content present at the end of a protocol
was present in law, in the same block, at its start.
*Scope: fixed blocks.* 1.3 covers blocks fixed in time (or selected by a fixed functional of the
state). A block indexed by time is not covered: with `φ(0,b) = (0,1−b)`, `φ(1,b) = (1,b)` and μ-O on
`{00, 01}`, the block `H₀ = cell 1`, `H₁ = cell 0` has `K` rising from 0 to 1 in law (C13). Such a
block is still bounded at every `t` by 2.3: `K_t(H_t) ≤ D(μ‖u)`, which is 0 under μ-G for every
block (obsmu Lemma P-1) and is the static budget of 1.5(b), 1.5(b′) under μ-O and μ-R.

**1.4 Formulation and verdict for the contract.** Define *native autonomous history producing
readiness* (NAH) as: a law admissible under NSC-6 without a further posit, a fixed block `H`, and
times `t₀ < t₁` with `K_{t₁}(H) > K_{t₀}(H)` or `P_{t₁}(E) > P_{t₀}(E)` for a readiness event `E`.
The NSC-6 laws are μ-G, μ-O and μ-R. Each is invariant: μ-G and μ-O by Main:54, μ-R by ledger
(iv)'s wording, "the maximal-entropy invariant measure compatible with the observer's records"
(Main:730). By 1.3, **NAH is empty** [W]. The contract's third disjunct never supplies readiness
distinct from the law it starts from; along an invariant law a history transports readiness and
does not create it in law.

**1.5 Escape checks (maximum skepticism, since 1.4 favours the hypothesis under test).**

- **(a) Conditioning on observer records (CR_rec, H-PREP, a time-slice μ-R).** A conditional
  law `μ(·|E)` is in general not invariant, so 1.3 does not apply to it. **Lemma E3 [W, EC C7].**
  `D(μ(·|E) ‖ μ) = log₂(1/μ(E))` exactly; for `μ = u`, `D(u_E‖u) = log₂(|S|/|E|)`. Proof:
  `μ(s|E)/μ(s) = 1/μ(E)` on `E`. ∎ D3's herald bound is the readiness consequence of this budget
  (via 2.4). Conditioning on a present record content alone supplies readiness of the record
  cells, not faithful records: under `u`, disjoint blocks are independent at each time, so a log
  `L_T` and a residual carrier `Σ_T` satisfy `P_u(g(Σ_T) = r | L_T = r) = P_u(g(Σ_T) = r)`, which is
  `2^{−N}` for a balanced `N`-bit functional. Verdict: not an escape from the budget; the conditioning
  event carries the budget, and H-PREP stays open.
- **(b) Per-orbit law μ-O.** μ-O is invariant, so 1.3 holds: nothing is produced in law. Its static
  content is not zero: `D(μ-O ‖ u) = log₂(|S|/ℓ)` for an orbit of length `ℓ` (C2: the swap 2-cycle,
  `ℓ = 2`, `|S| = 4`, carries 1 bit, all of it held predictability `K(V) = 1`, which is the native
  N1-K of OA-1 r5 :316–328). In general, by 2.3, `K_t(H) ≤ D(μ-O‖u)` for every block. Main:60 already
  types the orbit selection as fixed by posit (iv) and bounds the predictive memory of a period-`p`
  orbit by `log₂ p`; OA-1 types μ-O as derived given "the orbit of the actual microstate"
  (r5 :101). Under that typing (NSC-6) this budget enters the contract as native. Its size is set by the actual state's orbit. For a uniformly random bijection the
  cycle through a fixed state has length uniform on `1..|S|` (C12, exhaustive for `|S| = 5`), so an
  orbit carrying `b` bits has weight `≤ 2^{−b}`: the orbit selection is a boundary datum of the same
  weight as the budget it carries. For a structured φ with many short cycles (Main:730 (v) records
  that the exact linear rule splits its largest energy shell into exponentially many cycles) the
  budget can be typical, supplied by conserved quantities. Whether that budget can be converted into
  held predictability for an embedded observer, rather than predictability from the whole of `Rest`,
  is open. Verdict: μ-O is a possible carrier of a static budget, quantified here; it is not a
  physically sourced preparation. It is the open μ-O route of OA-1 (N1-S open under μ-O), not a
  forward producer. Recorded as AW-PR1-1 (§5).
- **(b′) Record-compatible law μ-R.** μ-R is invariant, so 1.3 holds for it. On the H-OC_orb
  reading (obsmu :183–185; PSH B20, `LEDGER.md:244`) it is the uniform law on the union `U` of orbits
  compatible with the records, so `D(μ-R‖u) = log₂(|S|/|U|)`, a static budget with
  `K_t(H) ≤ log₂(|S|/|U|)` for every block (2.3). OA-1 r5 N1-K states that knowing can be native
  "under μ-R … once the records exclude the fixed points". Verdict: μ-R is a second possible
  carrier of a static budget, posited under ledger (iv), not a physically sourced preparation; its
  size is the information the records carry about the orbit.
- **(c) A non-stationary preparation under NSC-2's first clause.** This is the boundary-law route
  itself (ARROW-1 A5; MP-0a; book ch18:212, :218). The screens did not deny it; they found no map
  from it to local ready cells (NSC-5). Not an escape from the conclusion; it is the alternative.
- **(d) Infinite volume (A1 not assumed).** An invariant probability can supply readiness at a
  constant rate forever: the shift on `{0,1}^ℤ` preserves the product law `Bern(1−δ)^{⊗ℤ}`, so the
  cell entering position 0 is ready with probability `1 − δ` at every step. 1.3 holds (the rate is
  constant). This law is singular to the product-uniform law, so the global budget of node 2 is
  infinite and uninformative; 2.6 localizes it. Verdict: escape from the finite total budget only;
  the supply is the law of the incoming stream, a boundary condition at spatial infinity.
- **(e) Single trajectories.** Along one trajectory a fixed block can pass from unready to ready
  (1.2 says the flux is two-way). The contract's objects are laws (NSC-2, NSC-5); a trajectory
  selected as the law is `δ_s`, with `D(δ_s‖u) = log₂|S|`, the maximal boundary datum.

**1.6 Node 1 verdict.** Proved [W]: 1.1, 1.2, 1.3, E3. The NAH disjunct is empty, for fixed blocks,
for every law the contract treats as native. The contract is not thereby unsatisfiable: every
surviving endpoint is a law whose budget node 2 measures, namely a declared boundary law, a
conditioning event of mass `2^{−b}`, an orbit selection under μ-O, an orbit-union selection under
μ-R, or (without A1) an incoming stream at infinity.

### Node 2 — budget theorem

**2.1 Conservation [W].** *For a bijection φ of finite `S`, any `p₀`, and any φ-invariant μ with
`p₀ ≪ μ`: `D(p_t‖μ) = D(p₀‖μ)` for all `t ∈ ℤ`. For `μ = u`: `D(p_t‖u) = log₂|S| − H(p_t)`. The
same holds for a bimeasurable bijection `T` with invariant μ.* Proof: relative entropy does not
increase under a measurable map applied to both arguments; apply it to `T` and to `T^{−1}`, and use
`T_*μ = μ`. ∎ Check: C1a, C4a, C4d, C5a.

**2.2 The coarse-grained part is not monotone [EC C1].** The owner's clause "its coarse-grained
part does not increase" is false for a deterministic bijection. Counterexample (ARROW-1 C.4):
`(v, b) ↦ (v ⊕ b, b)`, `p₀ = δ_{v=0} ⊗ unif_b`. Then `D(p_t‖u) = 1` for all `t`, while the sum of
cell-marginal relative entropies is `1, 0, 1` at `t = 0, 1, 2`, and the total correlation is
`0, 1, 0` (C1b, C1c). What does hold is a bound: for any map `f` (a coarse-graining),
`D(f_* p_t ‖ f_* u) ≤ D(p₀‖u)` at every `t` (data processing), and for a cell partition
`Σ_X D(p_{t,X}‖u_X) = D(p₀‖u) − TC_t` with `TC_t ≥ 0` the total correlation. Verdict: refuted as
monotonicity; correct as a bound.

**2.3 Exact transfer identity [W, EC C2, C4b, C4d].** *For `S = H × Rest` and any law `p`,
`D(p‖u) = K(H) + D(p_Rest ‖ u_Rest)`. Hence, for every `t`,
`K_t(H) + D(p_{Rest,t} ‖ u_Rest) = D(p₀‖u)`.* Proof:
`D(p ‖ u_H ⊗ u_Rest) = Σ p(h,r) log₂[p(r)/u_Rest(r)] + Σ p(h,r) log₂[p(h|r)/u_H(h)]
= D(p_Rest‖u_Rest) + log₂|H| − H(H|Rest)`; then 2.1. ∎
Consequences:
- A rise of held predictable content in `H` equals, exactly, a fall of the non-equilibrium of the
  rest: `K_{t₁}(H) − K_{t₀}(H) = D(p_{Rest,t₀}‖u) − D(p_{Rest,t₁}‖u)`.
- **Inert retention keeps the budget committed.** If over `[t₁, t₂]` the dynamics acts as
  `(h, r) ↦ (h, ψ(r))` with ψ a bijection not depending on `h`, then `H(H|Rest)` and `K(H)` are
  unchanged.

**2.4 Readiness ceiling for any law [W, EC C9].** *Let `E` be an event with `u(E) = π` (for `M`
designated `q`-ary cells in a fixed pattern, `π = q^{−M}`). For every law `p₀` and every `t`,
`d(P_t(E) ‖ π) ≤ D(p₀‖u)`, hence `P_t(E) ≤ (D(p₀‖u) + 1)/log₂(1/π)`.* Proof: data processing to the
indicator of `E` at time `t` (with `u` invariant), and `d(P‖π) ≥ P log₂(1/π) − h₂(P) ≥
P log₂(1/π) − 1`. ∎ For `D(p₀‖u) = 0` this gives `P_t(E) = π`, the μ-G case of OA-1 D3.

**2.5 Held-predictability budget (main statement) [W, EC C4].** *Let `S = A × B` with `A`, `B`
disjoint factor blocks, `g: B → {0,1}^N` balanced under `u_B` (`g_* u_B` uniform), `f: A → {0,1}^N`,
and at time `T` let `ε_k := P_{p_T}(f_k(A) ≠ g_k(B)) ≤ 1/2`. Then*
```text
D(p₀ ‖ u) = D(p_T ‖ u) ≥ N − Σ_k h₂(ε_k) ≥ N (1 − h₂(max_k ε_k)).
```
*Proof.* Put `F = f(A_T)`, `G = g(B_T)`. Under `u`, `A` and `B` are independent and `G` is uniform,
so `(F, G)` has law `f_* u_A ⊗ unif_N`. Data processing and the chain rule give
`D(p_T‖u) ≥ D(q_F ‖ f_*u_A) + Σ_x q_F(x) D(q_{G|F=x} ‖ unif_N) ≥ N − H(G|F)`. Subadditivity and
Fano's inequality for binary variables give `H(G|F) ≤ Σ_k H(G_k|F_k) ≤ Σ_k h₂(ε_k)`. ∎

Both hypotheses are needed. Without joint balancedness: `g = x₁ AND x₂` with `f ≡ 0` gives
`ε = 1/4` at `D = 0 < 1 − h₂(1/4)` (C15a). Without disjointness: a copy pair `x = y`, each cell
predicting the other, gives `N = 2`, `ε = 0` at `D = 1` (C15b).

The statement covers each item of NSC-7 that is evaluated at one time:

| Requirement at time `T` | `A` | `B`, `g` | Cost per bit |
|---|---|---|---|
| ready binary cell, `P(ready) ≥ 1 − ε` | trivial, `f` constant | the cell | `1 − h₂(ε)` |
| knowing a carrier (N1-K) | held records | carrier functional | `1 − h₂(ε)` |
| selectable preparation with the choice held (N1-S) | held setting | prepared carrier | `1 − h₂(ε)` |
| repeatable record (record still agrees with the residual carrier) | log | residual carrier | `1 − h₂(ε)` |

**Tightness [EC C4].** Two carriers, one register and two log cells; steps CNOT(c₁→r), SWAP(r,l₁),
CNOT(c₂→r), SWAP(r,l₂). With exact blanks: `D₀ = 3`, final `l₁ = c₁`, `l₂ = c₂`, `r = 0`, and
`K(r, l₁, l₂) = 3 = (N+1)(1 − h₂(0))` for `N = 2` (C4a–C4c). With blanks of `P(0) = 3/4`:
`D₀ = 3(1 − h₂(1/4))`, each final error is `1/4`, and `K = D₀` exactly (C4d, C4e). The bound is
attained at `ε = 0` and at `ε = 1/4`.

**Per-cycle form (the owner's formula) [W].** For `N` prepare/write/re-arm cycles whose `N` results
are still held at time `T`, each ε-predictable from a disjoint block, with the register re-armed at
`T` to reliability `1 − ε`, 2.5 gives `D(p₀‖u) ≥ (N+1)(1 − h₂(ε)) ≥ N(1 − h₂(ε))`. If in addition the
observer's block starts with `K₀(H) = 0` (no supplied blanks or correlations in it), 2.3 gives a
transfer: the rest's non-equilibrium `D(p_Rest‖u)` is lower at `T` than at `0` by at least
`(N+1)(1 − h₂(ε))`, while `D(p₀‖u)` is conserved. The transfer is not irreversible: it stays
committed while the results are retained inert (2.3), and reversible dynamics that uncomputes the
results returns it to the rest (C5).

**2.6 Local form; infinite volume [W].** *Let ν be a `T`-invariant reference probability and `A` a
finite region with `ν_A = u_H ⊗ ν_{A∖H}`. Suppose the state on `A` at time `t` is a measurable
function `F_t` of the state on a region `B` at time 0 (finite causal cone, ledger (ix) in family
form). Then `D(p_{0,B} ‖ ν_B) ≥ D(p_{t,A} ‖ ν_A) ≥ log₂|H| − H_{p_t}(H | A∖H)`, and the predictability
bound of 2.5 holds with `D(p_{0,B}‖ν_B)` on the left.* Proof: `ν_A = (F_t)_* ν_B` by invariance;
data processing; then the computation of 2.3 with `A∖H` in place of `Rest`. ∎ Hypothesis H-ν (the
reference is invariant and uniform on `H`) is automatic for finite `S` with `ν = u`; in infinite
volume it is a hypothesis to check for each model. For 1.5(d) the cone base contains the incoming
cells, each contributing `1 − h₂(δ)`: the budget is located in the incoming boundary data.

**2.7 Fresh-cell monotonicity [W, EC C10].** *Let `S = A × C₁ × … × C_n`,
`p₀ = p_A ⊗ p_{C₁} ⊗ … ⊗ p_{C_n}`, and let step `j` apply a bijection of `A × C_j` only (each cell
used once). With `a_j` the law of `A` after step `j`,
`F_j := D(a_j ‖ u_A) + Σ_{i > j} D(p_{C_i} ‖ u)` is non-increasing, and
`F_{j−1} − F_j = I(A; C_j) + D(p'_{C_j} ‖ u)` evaluated just after step `j`.* Proof: before step `j`
the joint law of `(A, C_j)` is `a_{j−1} ⊗ p_{C_j}`, since `A` depends only on `A₀, C₁, …, C_{j−1}`.
Its relative entropy to `u` is `D(a_{j−1}‖u) + D(p_{C_j}‖u)`, conserved by step `j`, and after the step
it equals `I(A;C_j) + D(a_j‖u) + D(p'_{C_j}‖u)`. ∎ Check: CNOT steps on fresh cells, with `I(A; C_j) > 0`, satisfy the decrement identity and
`F` is non-increasing (C10a); reusing a cell makes `F` rise (C10b, computed on its own trajectory). Finite
recurrence forces eventual reuse, so this monotonicity holds only on windows without reuse; this is
the hypothesis Main:516 states for accumulated memory ("without hidden-state reuse").

**2.8 Necessity of the hypotheses [EC].**
- **No retention, no bound on the number of cycles (C5).** One register, `N = 5` uniform carriers,
  cycle `k` = CNOT(c_k→r) then CNOT(c_k→r). Mid-cycle `I(r; c_k) = 1` bit (the register knows the
  carrier), after the cycle `r = 0` exactly; `D₀ = 1` bit for every `N`. The per-cycle bound
  fails without retention.
- **Exchange records cost nothing and give no predictability (C6).** Under `u`, SWAP(c, l) makes the
  log equal the carrier's past value with probability 1, with `D₀ = 0` and `K(l) = 0`. This is the
  write the o-ret owner decision lets count as transfer, subject to a distinct readable register and
  retention after the carrier has left (`o-ret-routes-20261103/DEFINITIONS.md:160–164`); it
  satisfies none of the rows of the table in 2.5.
- **Multi-time memory is budget-free (C3).** The swap under `u` has `K(V) = 0` at every `t` and
  `M₁ = I(X₀; X₂ | X₁) = 1` bit. (C4) readback, Main's hidden predictive memory and the A1-P8 history
  bounds concern conditionals across times, which 2.5 does not constrain.

**2.9 Node 2 verdict.** Proved [W]: 2.1, 2.3, 2.4, 2.5 (tight), 2.6, 2.7. Refuted by
counterexample: monotonicity of the coarse-grained part (2.2). The owner's `N(1 − h₂(ε))` bound
holds under explicit hypotheses — the `N` results are held at the evaluation time and are
ε-predictable from a disjoint block (or the cells are ready), with a reference measure that is
invariant and uniform on the held block — and fails without retention (C5) or without
predictability (C6). Its transfer form needs `K₀(H) = 0` in addition and describes a reversible
transfer, not an irreversible consumption.

### Node 3 — productivity test (fixed in advance by the authorization)

**Test.** A finding only if items 1–2 come with complete proofs and the controls hold: the
finite-horizon equivalence S⇔D⇔Q_fb, the P8 selection result, and every earlier screen's conclusion
at its own scope.

| Control | Check | Verdict |
|---|---|---|
| S⇔D⇔Q_fb, `finite_horizon_equivalence` [K] (`OB/Equivalence.lean:462–469`, as cited by OA-1 r5 :285–289) | It holds for every supplied finite-horizon law and quantifies over no prior. Nothing here restricts which laws are realizable. Its realizations use supplied structured priors (Main:486 blank slots; Main:534 initial register slice), which carry `D > 0` where blanks are used, as 2.5 requires of any held predictable content. | untouched |
| P8 selection (Main §4.6, Main:746–766; `a1-p8-history-bridge-20261119`) | P8 constrains memory times in the iterated-channel description under (EM) and the rate condition, and is time-symmetric (ARROW-1 B.9). The results here use no mixing hypothesis and bound single-time held predictability by `D₀`; they say nothing about `τ_B`. The A1-P8 history bound is a multi-time statement under a stationary law, which 1.3 and 2.8 (C3) leave free. | untouched; complementary |
| NATIVE-PRODUCER-2, NATIVE-PREP-SRC-1, CP-PREP-1, NATIVE-APPARATUS-SRC-1, NATIVE-INT-SRC-2, the detector, mechanical-latch and Geiger–Müller screens | Each is a bounded documentary finding that its packet identifies no independently justified producer or law. 1.4 shows that the autonomous-history disjunct cannot supply one; 2.5 gives a necessary budget for the law. Neither statement shows that no independently justified law exists (book ch18:212 remains a stated candidate), so no screen is promoted to an impossibility result and none is weakened. | each conclusion true at its scope |
| OA-1 D1–D4, N1-K, N1-S, MP-0a | D1 is 1.1. D2 is the case `D₀ = 0` of 2.3 (`K ≡ 0` for every block). D3 is 2.4 with E3. N1-K native under μ-O (swap) is C2 and saturates the budget. N1-S under μ-G fails by 2.5 with `D₀ = 0`; N1-S under μ-O, μ-R stays open, since 2.5 is only necessary. | consistent; none changed |
| ARROW-1 C.1–C.4 | 2.1–2.5 hold for `t < 0` as for `t > 0` (closure under inversion, C.2). A direction enters only through 2.7's no-reuse hypothesis or through the location of a boundary (node 4). C.4 is reused as the 2.2 counterexample. | consistent |
| Lemma C (o-ret, statement only) | One-write form of the same trade-off (readiness `D > 0` or disturbance). 2.5 is a multi-record form with predictability in place of disturbance. | consistent |

**Pressure test of the favourable reading.**
1. The mathematics is elementary: invariance of relative entropy, the chain rule and Fano's
   inequality. Its content lies in the contract-level consequences (1.4, the table in 2.5, 2.8), not
   in new mathematics.
2. Item 2 as written was partly false (2.2) and needs hypotheses (2.9). It is resolved by proof of
   the corrected forms and by counterexample to the monotonicity clause; the counterexample is not a
   proof of that clause.
3. The results do not make the source a boundary input instead of a mechanism. 1.5(b), (b′) show
   that μ-O and μ-R can carry static budgets, and a supplied budget still needs a native mechanism
   that makes it operationally available. §6 states the conclusion at that scope.
4. The results concern laws. Per-trajectory production exists (1.5(e)); the contract's objects are
   laws, so this does not reach it.

**Verdict.** Item 1 has a complete proof. Item 2 is resolved partly by proof of the corrected forms
(2.1, 2.3–2.7) and partly by counterexample (2.2); every control holds. On the author's reading,
which takes item 2's own wording ("Prove this, or find the exact obstruction or counterexample") to
admit a counterexample, the unit passes the fixed test: **gem, ELABORATING**, with no NEW item.
The owner's reading, relayed for this revision: a rigorous counterexample to the proposed
monotonicity clause completes that obligation provided the corrected replacement statements are
proved and all controls pass; it does not count as a proof of the original clause. Against §A.31's productivity test: the facts are stronger than D1's restatement (1.3, E3,
2.3–2.5 are quantitative and tight) and they constrain the contract (the NAH disjunct is empty for
fixed blocks; every endpoint carries a computable budget). The orbit-selection datum they quantify
is already stated (Main:60; H-OC_orb), so no hidden assumption is newly exposed.

### Node 4 — the boundary-posit option (proposal only; nothing adopted)

**What node 1–2 force.** Under NSC-2 as screened, the regress endpoint for any protocol that holds
`N` ε-predictable binary results at one time (plus a re-armed register) is a law with
`D(p₀‖u) ≥ (N+1)(1 − h₂(ε))` (under 2.5's hypotheses: fixed blocks, predictors disjoint from
targets, targets jointly balanced), located in the causal-cone base of the protocol (2.6).
Reversible dynamics does not change that quantity (2.1); it redistributes it between `K(H)` and
`D(p_Rest‖u)` (2.3). A physical source needs both such a supply and a native mechanism that makes it
operationally available; Node 4 addresses only the supply, and the mechanism question stays open.
Two named forms of the supply are possible.

- **NEQ-T (time-slice boundary law; proposal).** The realized law is the counting measure
  conditioned on a boundary event `B₀` at one time, `p₀ = u(·|B₀)`, with budget
  `D₀ = log₂(|S|/|B₀|)` (E3). This is the past-hypothesis form of MP-0a and of book ch18:212.
- **NEQ-O (orbit-level; proposal).** The operative law is μ-O on an orbit of length `ℓ` with
  `log₂(|S|/ℓ) ≥ (N+1)(1 − h₂(ε))`. It carries no time-slice and is stationary in law (1.3).

**Candidate independent consequences** (beyond "the observer has finite data"):
1. *Finite total holding capacity (under A1).* At every time, for any family of predictor/target
   pairs whose predictor blocks together are disjoint from their target blocks together, and whose
   targets are jointly balanced under `u`, `Σ_k (1 − h₂(ε_k)) ≤ D₀ ≤ log₂|S|` (2.5 applied to the two
   unions). Without disjointness it fails: mutual records `x = y` give 2 at `D₀ = 1` (C15b). Under
   NEQ-T the bound is `log₂(|S|/|B₀|)`, the entropy gap of the boundary macrostate.
2. *No accumulation in law under NEQ-O.* By 1.3, under any invariant law the held predictable content
   of every fixed block is constant in law. NEQ-O therefore predicts no ensemble-level growth of
   records, and no record arrow, which ARROW-1 C.3 also states for the invariant measure. NEQ-T
   with fresh-cell use (2.7) predicts a monotone conversion of `D(p_Rest‖u)` into held content on
   windows without reuse, pointing away from `B₀`. Observing a consistent record arrow is
   therefore a postdiction favouring NEQ-T over NEQ-O; it is not a novel prediction.
3. *Alignment.* Under NEQ-T and 2.7's hypotheses the record arrow and the decrease of the available
   fresh-cell resource `F_j` point the same way. This is ARROW-1 C.6 (β) ("posited coincidence of the
   two boundary data") with the coincidence derived for records, conditional on the no-reuse
   window; alignment with the horizon clock stays open.
4. *Relation to P8 and (C2).* P8 selects where observers can exist and is time-symmetric; NEQ-T or
   NEQ-O supplies the non-equilibrium content P8's selected regions require. Neither implies the
   other (Node 3), matching AW-OA1-2 (selection versus supply).

**What would falsify or discriminate.**
- A protocol meeting NSC-7 with `D(p₀‖u)` below the bound of 2.5 would refute 2.5, which is a
  theorem; the reachable falsifiers concern the posits.
- NEQ-T with a single past boundary is falsified by records anti-aligned with the rest of the
  domain in an isolated subsystem, or by a local supply shown to require a boundary elsewhere (an
  incoming stream as in 1.5(d), which needs A1 to fail).
- NEQ-O is favoured over NEQ-T if a native φ is shown to have, for typical states, orbits short
  enough to carry the budget, together with a conversion of that budget into observer-held
  predictability.

**§A.29 status.** Neither form is hard to vary as stated: the size and location of `B₀` (or `ℓ`) can
be tuned to any required budget. NEQ-T becomes hard to vary only if `B₀` is specified independently,
for example from the cosmological boundary and horizon count (Main:76's `A/ε²` count is a stated
model input, not a derivation), with its consequence 1 then fixed. That specification is not
attempted here.

***

## 5. Classification and markers (§A.31)

| Item | Class |
|---|---|
| 1.1 stationarity | CONFIRMING (OA-1 D1) |
| 1.2 flux balance; 1.3 no production of block statistics; NAH empty (1.4) | ELABORATING |
| E3 conditioning cost; 2.4 readiness ceiling | ELABORATING (OA-1 D3) |
| 2.2 non-monotonicity | CONFIRMING (ARROW-1 C.4) |
| 2.3 transfer identity; 2.5 budget with tightness; 2.6; 2.7; 2.8 necessity examples | ELABORATING (o-ret Lemma C; Landauer–Bennett accounting) |
| AW-PR1-1 (below) | ELABORATING (Main:60; OA-1 r5 §1; H-OC_orb; PSH B20) |

- **AW-PR1-1 (assumption-watch marker; ELABORATING).** The orbit selection behind μ-O is stated as
  a datum (Main:60, posit (iv); OA-1 r5 :101, "the orbit of the actual microstate"; H-OC_orb, obsmu
  :183–185; PSH B20). This record quantifies it: `D(μ-O‖u) = log₂(|S|/ℓ)` and, for μ-R,
  `D(μ-R‖u) = log₂(|S|/|U|)`; every block satisfies `K_t(H) ≤ D(μ‖u)` (2.3), with equality in the
  swap 2-cycle (C2). For a uniformly random bijection the orbit carrying `b` bits has weight
  `≤ 2^{−b}`; for a structured φ it is supplied by conserved quantities. Any claim of native knowing
  or preparation under μ-O or μ-R should state ℓ (or `U`) or the conserved quantities that fix it.
- **AW-PR1-2.** Single-time held predictability (readiness, knowing, selectable preparation with the
  choice held, repeatable records) is budget-bearing; multi-time memory, exchange records and
  unretained reversible cycles are budget-free. A screen or protocol requirement should be sorted
  into one class before its source is sought.
- **Fixed point.** One pass; no NEW item. The §A.31 fixed point (3–4 passes without NEW) is not
  reached.

***

## 6. What this decides for #1169 (the authorization's question)

*Is the native-source contract unsatisfiable in the form it was screened, so that the missing input
is a non-equilibrium boundary condition rather than a mechanism?*

**Answer at the proved scope.** Neither alternative alone. Reversible autonomous dynamics cannot
create a net statistical supply of preparation resources in a fixed block under an invariant law; it can redistribute resources supplied by the
law or by the boundary conditions. A physical measurement source therefore needs both an
admissible resource supply and a native mechanism that makes the resource operationally
available. The result does not exclude measurement interactions, individual trajectories that
create records, conditioning on observations, or the redistribution of an available resource,
and it does not remove the need to investigate apparatus mechanisms.

- **Not unsatisfiable.** The contract can be met through its first clause, an independently
  justified law (NSC-2).
- **Its third disjunct is empty.** Under every law the contract treats as native, no history raises
  readiness or held predictability of any fixed block in law (1.3, 1.4); a moving block stays below
  the law's static budget (1.3, scope).
- **The endpoint carries a computable budget.** Every protocol that, at one time and on fixed blocks,
  holds `N` ε-predictable results and a re-armed register, with predictors disjoint from targets and
  targets jointly balanced under `u`, needs `D(p₀‖u) ≥ (N+1)(1 − h₂(ε))` in its causal-cone base
  (2.5, 2.6). Reversible dynamics does not change `D(p₀‖u)` (2.1); it redistributes non-equilibrium
  between the rest and held content (2.3), and the redistribution is reversible (C5).
- **Supply.** The supply side is a property of the law: a time-slice boundary law (NEQ-T), or a
  static budget carried by μ-O (the orbit structure of φ, 1.5(b)) or by μ-R (the orbit union
  compatible with the records, posited under ledger (iv), 1.5(b′)). μ-O and μ-R are possible carriers
  of static budgets, not physically sourced preparation.
- **Mechanism.** A native mechanism that makes a supplied budget operationally available (NSC-5's
  "map into local addressable blanks"; the screens' coupling, record and read gates) is required in
  addition and remains open. Apparatus mechanisms still need investigation.
- **Not excluded.** Measurement interactions; individual trajectories that create records (1.5(e));
  conditioning on observations (1.5(a), E3); redistribution of an available resource (2.3).

***

## 7. Limits and what an independent reviewer must check

- Every [W] proof in §4, in particular 2.5 (the data-processing step with `(F, G)` and the
  balancedness of `g`), 2.6 (that `ν_A = (F_t)_*ν_B` follows from invariance and the cone hypothesis),
  and 2.7 (the product structure before each step).
- The reading of NSC-6: that μ-R in ledger (iv) is an invariant measure, so 1.3 applies, while a
  time-slice conditioning (CR_rec) is not and falls under E3.
- The escape analysis 1.5, in particular whether any law admissible under the screens is neither
  invariant nor a conditioning nor a declared boundary law.
- The control table of Node 3, in particular the P8 and A1-P8 rows.
- That the exact checks test what §4 claims of them (§9 maps each check to its statement).
- Whether item 2's resolution partly by counterexample meets the fixed test (owner decision).
- Not done: no literature re-read; no statement about R-lin's orbit lengths; no conversion
  mechanism; no infinite-volume model beyond the Bernoulli shift remark; no Lean.

***

## 8. Literature (cited from memory, not re-read; [LIT2])

- R. Landauer, IBM J. Res. Dev. 5 (1961) 183–191; C. H. Bennett, Int. J. Theor. Phys. 21 (1982)
  905–940 — erasure cost and reversible copy/uncopy (the C5 pattern). Already listed in
  `o-ret-routes-20261103/SOURCES.md:98–101`.
- D. Reeb and M. M. Wolf, "An improved Landauer principle with finite-size corrections", New J.
  Phys. 16 (2014) 103011 — Landauer bounds from relative-entropy identities in a system–reservoir
  setting, the analogue of 2.7.
- D. Z. Albert, *Time and Chance* (2000) — the past hypothesis as the source of the record
  asymmetry (secondary summary already in `observer-interface-obsmu-20261104/ANALYSIS.md:599–601`).

No result in §4 depends on these; they place the mathematics as standard.

***

## 9. Exact checks

`checks/prep_regress_checks.py` uses exact rational arithmetic; entropies are exact elements
`a + b·log₂3`, and signs are decided by comparing integer powers `3^q` and `2^p`. Command, from this
directory: `python3 -I checks/prep_regress_checks.py` (about one minute, dominated by C14). Exit status 0 iff every check holds.

| Check | Statement tested |
|---|---|
| C1a–c | 2.1 conservation; 2.2 counterexample (marginal sum `1,0,1`; total correlation `0,1,0`) |
| C2a–b | 1.5(b) `D(μ-O‖u) = log₂(|S|/ℓ)`; 2.3 identity on the swap 2-cycle |
| C3a–b | 2.8: `K ≡ 0` under `u`, `M₁ = 1` bit |
| C4a–e | 2.1, 2.3 along a protocol; 2.5 tightness at `ε = 0` and `ε = 1/4` |
| C5a–b | 2.8: copy/uncopy cycles at a fixed budget |
| C6 | 2.8: exchange record |
| C7 | E3 for a cylinder event and a non-cylinder event |
| C8 | 1.2 for all bijections of a 4-set and all events |
| C9 | 2.4 along the C4d trajectory |
| C10a–b | 2.7 with fresh CNOT steps (nonzero `I(A;C_j)`, decrement identity); rise under reuse on its own trajectory |
| C13 | 1.3 scope: a moving block gains `K` under μ-O, bounded by `D(μ-O‖u)` |
| C14 | 2.5 inequality away from equality: every law on 3 bits with point masses in `{0,1,2,3,4,6}/16` whose quantities stay in the `{2,3}` field (others skipped, not counted), four predictor maps; 20,500 cases, 20,432 strict |
| C15a–b | 2.5 countercontrols: the bound fails without joint balancedness (AND) and without disjointness (copy pair) |
| C12 | 1.5(b) cycle-length distribution for all 120 permutations of 5 points |
| C11a–b | countercontrols: the sign test separates `1.58 < log₂3 < 1.59`; C8's flux routine reports failure on a non-bijection |

Output at this record's commit:

```text
CHECK C1a total D(p_t||u) constant = 1: PASS
CHECK C1b sum of marginal D = 1, 0, 1 (rises at t=2): PASS
CHECK C1c total correlation = 0, 1, 0: PASS
CHECK C2a D(muO||u) = log2(|S|/l) = 1: PASS
CHECK C2b K(V) = 1 and D(p_H||u_H) = 0 (transfer identity 1 = 1 + 0): PASS
CHECK C3a K(V)=0 for t=0..3 under u: PASS
CHECK C3b M_1 = I(X0;X2|X1) = 1 bit under u (memory is budget-free): PASS
CHECK C4a perfect blanks: D0 = 3 bits, conserved at every step: PASS
CHECK C4b transfer identity K_t(H) + D(p_Rest||u) = D0 at every step: PASS
CHECK C4c final: l1=c1, l2=c2, r=0 exactly; K(H)=3 = (N+1)(1-h(0)): PASS
CHECK C4d noisy blanks P(0)=3/4: D0 = 3(1-h(1/4)), conserved; transfer identity holds: PASS
CHECK C4e final errors 1/4, 1/4, 1/4 and K(H) = D0 = 3(1-h(1/4)): bound attained: PASS
CHECK C5a budget D0 = 1 bit for any N; conserved: PASS
CHECK C5b each of N=5 cycles: I(r;c_k)=1 bit mid-cycle, r re-armed exactly: PASS
CHECK C6 exchange: D0 = 0, P(l_1 = c_0) = 1, K(l) = 0: PASS
CHECK C7 |E|=2: D(u_E||u) = log2(8/|E|): PASS
CHECK C7 |E|=3: D(u_E||u) = log2(8/|E|): PASS
CHECK C8 flux balance |{s notin E: phi s in E}| = |{s in E: phi s notin E}| (24 x 16 cases): PASS
CHECK C9 readiness ceiling P_t(E) <= (D0+1)/(M log2 q) at every step: PASS
CHECK C10a fresh CNOT steps: I(A;C_j) > 0, decrement = I + D(outgoing), F non-increasing: PASS
CHECK C10b reuse of a used cell: D(a) rises from 0 to 1-h(1/4): PASS
CHECK C12 cycle length through a fixed point is uniform on 1..5 (24 each of 120): PASS
CHECK C13 mu-O invariant; moving block K: cell1 at t0 = 0 -> cell0 at t1 = 1 <= D(mu-O||u) = 1: PASS
CHECK C14 2.5 holds on 20500 exact (law, predictor) cases, 20432 strictly: PASS
CHECK C15a no joint balancedness (g = AND, f = 0): eps = 1/4 and D = 0 < 1 - h(1/4): PASS
CHECK C15b no disjointness (x predicts y, y predicts x): N - sum h = 2 > D = 1: PASS
CHECK C11a sign test: 1.58 < log2(3) < 1.59 decided by integer powers: PASS
CHECK C11b C8's flux routine reports failure on a non-bijection (constant map): PASS
28/28 checks hold
```
