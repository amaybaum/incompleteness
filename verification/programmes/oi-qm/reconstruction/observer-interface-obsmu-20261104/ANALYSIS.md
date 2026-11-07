# O-OBSMU — what `(Obs, μ)` needs, what the corpus supplies, and what is missing

**Status: WIP / UNVERIFIED research record.** Original paper author `writer-866`, under
#866 c.6642599988 and the bounded extension c.6643823627. The independent model-review chain
ends at `f67b9f0c81e0e404d78c042adfa47d71abf3ad45` (#1110 c.6649378167, ACCEPT), carrying the
earlier reviews and the owner's D-OB7/D-OB8 decisions (#866 c.6649267203).
The current-source reconciliation is by `root`, under the owner's 2026-11-07 instruction
recorded in [#866 c.6707972400](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6707972400).
Its exact-head review is recorded separately on #1110; earlier verdicts do not automatically
cover this correction. Review comments are provenance, not sole evidence of a result
(§A.46 item 7). No computation was run. No statement here is a premise of an established claim.

## 0. Conventions

**Anchors.** Unqualified anchors remain at the historical drafting snapshot
`D` = `f5c281ae10a913ec68fa41b3b839ad0b164979cd`.
The named ARROW-1 passages were re-read at current-main snapshot
`M` = `5ea5a40218e4e660b39a9b149050ced4f95d9b48` on 2026-11-07.
`M/Main`, `M/Substratum` and `M/ch18` mean the corresponding files at `M`;
`RECOVERY` means [ARROW-1's substantive recovery note at `M`](https://github.com/amaybaum/incompleteness/blob/5ea5a40218e4e660b39a9b149050ced4f95d9b48/verification/audits/manuscript/arrow-1-20261105/RECOVERY.md).
This bounded reconciliation does not re-run the original whole-corpus search.

| Anchor | Refers to |
| --- | --- |
| `Main:N`, `SM:N`, `Substratum:N` | lines of `papers/` |
| `FULL:N`, `ch04:N`, `ch18:N`, `appC:N` | lines of `book/The-Incompleteness-of-Observation-FULL.md`, `book/ch04-methodology.md`, `book/ch18-beyond.md`, `book/appendix-c-objections.md` |
| `MR-pre:N` | `../measurement-record-formation/preregistration.md` |
| `MR★:N` | `../measurement-record-formation/amendments/MR-star.md` |
| `PC★:N` | `../physical-coupling-pc1/amendments/PC-star.md` |
| `SOI-audit` | `verification/audits/operational/stochastic-observer-interface-audit.md` |
| `ROF` | `verification/audits/operational/rooted-observer-family-sourcing/result.md` |

**Support layers.**

- **KC:** kernel-checked on `main`.
- **PD:** a paper derivation in a record on `main`, with its review status stated where it
  matters.
- **PD-here:** a paper derivation written in this note; reviews have the exact scopes recorded on #1110.
- **CJ:** a conjecture or sketch.
- **OP:** open.

A chain takes the layer of its weakest link.

**Sorting rule** (owner guidance, relayed 2026-11-04). Each requirement goes in exactly one
group:

- **(a)** implied by OI's axioms or theorems. The locator and support layer are given.
- **(b-stated)** not implied by the axioms, but stated in a manuscript as a posit, principle,
  idealization, convention, realization datum or solution-specific datum, and labelled there as
  such. One sub-case is marked separately: **(b-stated, construction step)**. This covers a step
  stated inside a manuscript derivation that is not labelled as a posit there (Q5).
- **(b-new)** not stated anywhere in the corpus as a premise of the result that uses it.

Mathematical validity and physical justification are recorded separately.

**Literature** (§3.8). The owner's arXiv authorization is recorded at #866 c.6643204362. Each
source is marked as read directly or taken from a named secondary source. External results never
establish that something follows from OI's assumptions. An ingredient that only an external
construction supplies is an additional assumption.

**Off-`main` references** are classified one by one in §7 (§A.42 item 8).

## 1. The obligation, by consumer

The obligation, quoted in #866 c.6600176951 from the ROADMAP P1 section frozen at `9613b21c`:
"supply independently motivated structure selecting the physical observation map and ensemble,
or prove that the claims consuming an induced stochastic law are invariant under that residual
choice." Its negative bound is `ensemble_underdetermined` and
`waveSubstratum_stochastic_interface_gap` (KC, `OIBridge/StochasticInterface.lean`).

The consumers were found by searching `papers/Main.md`, `papers/Substratum.md`, `papers/SM.md`
§3.1, the SOI-audit, ROF and the #914 matrix. This is a census of those sources, not of every
downstream paper.

| # | Consumer | Locator | What it needs from `Obs` | What it needs from `μ` | Status under the residual choice |
| --- | --- | --- | --- | --- | --- |
| U1 | Representation equivalence `S ⇔ D ⇔ Q_fb` | Main §1.5, §3.4; KC `finite_horizon_equivalence` (`Equivalence.lean:462`), a biconditional for every `P : Traj V K → ℝ` with no hypothesis on `μ` | a finite outcome alphabet | nothing | **not a residual-choice consumer**: it holds for every finite-horizon law |
| U2 | Unavoidable hidden predictive memory; pushforward identity | Main §1.5, §3.4; KC `pushforward_identity` | finite alphabet | nothing | **not a residual-choice consumer** |
| U3 | Reverse finite realization | Main §1.5 (3) | finite alphabet | nothing | **not a residual-choice consumer** |
| R1 | Recurrence-cycle P-indivisibility of the rooted family | Main:137–145; KC `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`), its rooted form (`:148`), `isPermMatrix_of_stochastic_inverse` | product cut, `π_V` | the hidden laws given each root | **support-invariant**: depends on the hidden laws only through their supports (Theorem SI, §3.2; ELABORATING Main:141). **Not invariant across supports** (CC-1) |
| R2 | A C4 gap at order `k` | Main §1.3 (C4), Main:141 | product cut, `π_V` | the preparation law | **not invariant, even at fixed full support** (CC-2, §3.3). A generic dichotomy holds (Proposition G), and the canonical law can lie in its exceptional set |
| R3 | P-divisibility on an accessible window; the stochastic route's diagnostic | Main:141 scope; SOI-audit stage 3 | product cut, `π_V` | the hidden law | **not invariant in general, even at fixed full support** (CC-2, §3.4). **Open for native K1** |
| R4 | Applying the stochastic–quantum correspondence | Main:526–530 (translation hypothesis (T)); arXiv:2309.03085v2 §3.1 | finite configuration space | a transition map that does not change when the initial distribution is varied (Q9′) | **nothing new relative to Main.** Q9′ is (b-stated) at Main:137 and Main:284 (§3.8) |
| L1 | Partition-relativity lemma | Main:86 | the partition | the canonical measure, by name | **stated relative to a named measure** (Q8) |
| L2 | Baseline matrices; Lemma 3 prong 1; the uniform-prior one-step lemma | Main:60, :62, :276 | product cut | the uniform hidden prior | **stated relative to a named measure** (Q8) |
| L3 | A specific visible law (a Born weight, a correlation, a parameter) | Main:60 | the cut | the prior | **refuted as invariant** by Main:60's own swap example |
| L4 | Setting screening in the Bell analysis | Main:366 ff. | the wings' cuts | setting–hidden independence | **non-invariance argued, not shown here**; it also needs capacity (2) |
| L5 | Readiness and records (O-RDY, O-REC) | #914 rows O-RDY, O-REC; MR★:642 | the cut, its access | a ready resource | **non-invariance argued** (Lemma P-1: H-μ has no ready region), **not shown for every μ** |

**How each consumer fares.**

- **U1–U3:** use nothing from the residual choice. They are non-consumers, and they carry no
  prediction.
- **R1:** reduces the μ leg to a choice of supports.
- **R2 and R3:** depend on the measure itself, not only its support.
- **R4:** needs nothing beyond what Main states.
- **L1 and L2:** carry the named measure Q8 as a hypothesis.
- **L3:** is refuted as invariant.
- **L4 and L5:** non-invariance is argued here, not shown.

## 2. The four capacities: what the corpus establishes

**K1** is MR-1's frozen `K★ = {K1}`: the additive second-order step
`φ(u_prev, u) = (u, A u − u_prev)` on the native cubic graph, with finite or compact value group
`𝐑` (MR★:462–466).

| Capacity | Established (locator, layer) | Conditional (hypotheses) | Open | Physical justification of the hypotheses |
| --- | --- | --- | --- | --- |
| **(1) Preparation** | Main:60: a realization "carries its own fixed hidden prior `μ_H` as part of the realization datum" (stated datum). For finite `𝐑` under H-μ, every region is uniform and disjoint regions are independent at equal times (Lemma P-1, PD-here). | For rooted laws with a full-support visible prior, conditioning on the observed initial value replaces preparation (§3.5, PD-here). | O-RDY (#914 row O-RDY). No process on K1 writes a chosen value into a region (MR★:637). | The structured `μ_H` is supplied, not sourced (ROF Q3(ii)). |
| **(2) Selectable interactions** | The controlled lift `F(x, s) = (T_s x, s)` conserves `s` (MR-pre:115, N7; a frozen record). | On K1, a setting region changes every other region only by an additive offset that does not depend on the carrier's state. This is the identity part of Lemma D (MR★ S-L1, S-C1, :479–509; PD in a frozen record; re-derived here, PD-here). Counting offsets as non-selectable needs premise D-SEL, and O-SET's definition is open. | O-SET, DEFINITION-OPEN (#1009). Non-additive native-type rules are unscreened (MR★:667, σ12). | Additivity is Substratum A5, "partly derived" from amplitude-scale gauge, an "explicit operational principle" (Substratum:100, :272) (b-stated). |
| **(3) Accessible outcomes** | A finite outcome alphabet: Main Definition and Lemma 1 (Main:44, :48; PD with an external holographic input). The readout is configuration-sector (Main:222). Region readout: KC definition `cutRealization` (`PhysicalC4Discharge.lean:582`). | For finite `𝐑`, under H-μ and K1 with a homomorphic readout, conditional next-step laws are flat on cosets of a history-independent subgroup (Proposition C, PD-here). | O-ACC: whether one retained tick is native or a convention (#914 row O-ACC). | The cut exists (a): Main:38–40, :50. The product form is (b-stated): "idealized" (Main:54). A finite readout does not imply a product (§4.1, Q4, PD-here). |
| **(4) Readable, persistent records** | MR-1 stage 1 gives a scoped `GAP` (a frozen record). After its correction round, the named element is "the absence of a physically sourced quiet, ready region" (MR★ C-3, :1342–1371; C-14, :1491–1505). MR★ C-2 (:1322–1340) withdraws the claim that localized records are impossible. | On K1, no confined pattern lasts beyond about twice its width (MR★ S-L4, S-C4a, :528–571). PD in a frozen record. MR★:1297–1300 reports that a review verified it "by case analysis"; it is not re-verified here. C-11 corrects S-L4's torus lift. C-10 corrects S-C4a's slice count and the log, not S-L4. Hypotheses: `ℤ^d`, or a torus with `N ≥ 5w + 2`, and `a` injective. This excludes confined patterns only. It does not show that localized records are impossible (C-2), and the trace route is `UNDECIDED` (C-4, :1373–1380). | O-RET (#1032), O-REC (#866). | Finite recurrence bounds every budget (MR★ S-L6). |

## 3. The routes, depth-first

Each node is closed by the check it names. Productivity test (§A.31), fixed before the walk: a
node is a gem if it is strictly stronger than a restatement and either constrains something or
exposes a hidden assumption.

### 3.0 Node S — the sourcing route

**S.1, the Obs leg.** Checks: Main §1.2, ROF Q1 and Q6, SOI-audit T2.

- **Existence of the cut (a).** It is constitutive of Axiom 1 on Main's adopted perspectival
  reading (Main:38–40), and Lemma 2 states it (Main:50).
- **Which cut.** Not implied. Main §1.4 makes the description partition-relative, so the cut is
  a parameter of every per-cut claim.
- **Product form (b-stated).** Main calls it "idealized" (Main:54).
- **Readout slice.** Main treats the readout as configuration-sector (Main:222), so the slice is
  (b-stated). Whether it is native is O-ACC.
- **The two layers.** The reduced `Substratum` record has no observation map (KC
  `readWriteFamily_exists`). The realization layer declares one (ROF Q6).

**Verdict S.1.** The Obs leg is sourced as a family indexed by the declared cut. The product form
and the readout slice are (b-stated).

**S.2, the μ leg.**

- **S.2.1, invariance alone.** It does not select a measure: KC `ensemble_underdetermined`.
  Closed, negative.
- **S.2.2, Lemma 3's selection (b-stated).** Main:56 reads: "the counting measure is selected
  among invariant measures as the maximal-entropy one — a selection principle, not uniqueness
  from invariance alone".
  - It needs finite total `S`. Main:62 and :268 carry that as a posit. The owner's
    observer-relative finiteness decision (§7) keeps it as a branch premise.
  - On an infinite space the counting measure is not a probability, and Haar measure on a
    compact completion would need its own selection argument (PC★:219–220).
- **S.2.3, what Main states about conditioning, and at what level.** Main §4.6 is quoted in full
  in Appendix A.
  - **What §4.6 states.** Its theorem (Main:748–752) is conditional on (EM) and concerns "the
    coarse-grained description generated by iterating `𝒦_{Σ_loc(V)}`". It assumes bounded
    coupling-graph diameter, canonical typicality for the equilibrium clause, and finite `S`
    (Main:760, Scope). Its observer-selection corollary (M/Main:758; titled
    "past-hypothesis replacement" at `D`) adds the rate condition
    `τ_mix ≪ τ_S` and concludes that, "in that description, with (C2) read in its timescale form
    (C2-slow), the framework's observers therefore exist only in the non-equilibrium phase of
    `(S, φ)`". §4.6 says where observers can exist. It states no measure.
  - **The "structural, not measure-theoretic" sentence** (Main:756) belongs to the
    anti-Boltzmann-brain corollary. The first revision of this note used it to infer that Main
    states no conditioning, and that inference is withdrawn. The sentence says only how the
    Boltzmann-brain exclusion is argued.
  - **What Main does state about the measure** is orbit-level conditioning:
    - Main:62: "the selection among orbits is fixed by maximal entropy compatible with the
      observer's records", with "the atypical short orbits … precisely observer-lacking
      substrata … outside the scope of every theorem below";
    - the posit ledger, Main:726 (iv): "the measure selection is a maximal-entropy principle ('the
      maximal-entropy invariant measure compatible with the observer's records') — a standard but
      substantive epistemic postulate, not derived";
    - book ch01:85, which says the same.
  - **Classification.** The note's earlier single label H-OC is split into two:
    - **H-OC_orb (b-stated):** the measure is the maximal-entropy *invariant* measure compatible
      with the observer's records, which excludes observer-lacking orbits (Main:62,
      :726 (iv); ch01:85).
    - **CR_rec (b-stated, construction step; accepted in D-OB7):** the conditional of the
      stated measure on the observer's present visible value (Main:88, :105), and the hidden
      posterior after a visible history within a given realization (Main:99). These lines define
      predictive quantities given a law. They are not a measure-selection rule. See §4.6.2 Q-b.
    - **CR_slice (b-new):** conditioning on a stipulated event at a time slice that goes beyond the
      observer's records. No source states one.
- **S.2.4, why orbit-level conditioning cannot give a preparation.**
  - A measure invariant under `φ` gives equal weight to every point of each orbit in its support.
    It therefore assigns a time-slice event `R` the weight of `R` within each orbit, at every time
    alike. That is not a preparation made at a time.
  - Lemma 3's selection is among invariant laws (Main:56, :726 (iv)). The uniform law on a
    time-slice event `R` is invariant only if `φ(R) = R`. So "given `R`, the measure follows from
    Lemma 3" stays withdrawn.
  - A preparation law at a time is obtained in one of two ways:
    - **(i)** supplied directly as a realization datum. Main:60 allows "its own fixed hidden prior
      `μ_H`", and Main:524 gives a structured state-level prior, "uniform on the initialized
      ledger/clock sector times the tape".
    - **(ii)** derived from the canonical measure by conditioning at a time slice. On the
      observer's own visible record this is CR_rec (a construction step, D-OB7). Conditioning on an
      event stipulated beyond the records is CR_slice (b-new). Either way, reading the result as a
      preparation law is the further identification H-PREP (§4.6.2).
  - Route (i) needs no new rule. Its content, which particular state-level law, is supplied, not
    sourced.
- **S.2.5, related statements in the corpus** (a §A.19 search).
  - **Main:62:** "the selection among orbits is fixed by maximal entropy compatible with the
    observer's records". This is a stated, records-conditioned, orbit-level selection
    (b-stated). It does not name a state-level preparation event.
  - **ch18:210 (= FULL:5023)** reads: "The universe starts in a configuration that is far from
    equilibrium relative to the substratum's full state space". **ch18:214 (= FULL:5027)** reads:
    "the universe begins in a low-entropy configuration with most degrees of freedom on the hidden
    side of the cosmological horizon". Together these state a low-entropy initial condition in the
    book (b-stated). These are historical quotations at `D`. [M/ch18:214](https://github.com/amaybaum/incompleteness/blob/5ea5a40218e4e660b39a9b149050ced4f95d9b48/book/ch18-beyond.md#L214)
    retains the low-entropy initial condition, explicitly marks thermodynamic/cosmological
    alignment open, and qualifies apparent-horizon monotonicity by an expanding FRW background
    satisfying the null energy condition. The physical-input classification survives; no
    preparation or alignment mechanism follows.
  - **Main:524's realization prior** has the uniform-on-an-event form: "uniform on the
    initialized ledger/clock sector times the tape". It is supplied as data.
  - **Further sources on initial data** are sorted in §4.6.1: ch19 §19.3.4–§19.3.5,
    Substratum:538 and :552, ch00:101, GR:358–366, SM:48 and :124. Two passages come close to
    generating initial data without doing so: ch19:198 (statistical isotropy, "speculative") and
    ch19:200 ("initial conditions as gauge … has not been investigated").
  - **ch04:170:** "Cosmic initial conditions are solution-specific … The state at any particular
    cosmic time, including the time-zero conditions, is not a framework output."
  - **appC:329:** "Why this initial state rather than another is not addressed by the framework's
    structural content."
  - **Main versus ch18 (historical comparison, rechecked at `M`).**
    - Main limits its replacement of the past hypothesis to one role, at both places it states
      it:
      - Main:744: "in its role of selecting observer-compatible configurations";
      - Main:758: "The low-entropy initial condition commonly imported as a "past hypothesis" to
        select observer-compatible configurations is replaced here, within that description, by
        a structural selection rule".
    - At `M`, the corollary is titled "observer-selection rule, with its rate condition".
      Its statement and hypotheses are unchanged (RECOVERY §F.4). The cited selection result
      determines where the stated observers can exist in the iterated-channel description;
      it supplies neither a preparation nor a time direction nor a measure.
    - No contradiction is recorded between that result and ch18's stated initial condition.
      This conclusion is limited to those passages.
  - **Historical cross-document finding, tracked as #1112 (ARROW-1).** Each passage below
    quotes `D`, where the corpus disagreed on whether the arrow of time was derived.
    - **Saying it is derived:**
      - Substratum:401: "every arrow the observer sees descends from this confinement together
        with the horizon growth that the accelerating phase produces";
      - ch02:194–196 (= FULL:837 and the paragraph after it): "it derives a monotonic parameter
        along observer worldlines and four aligned arrows of time";
      - ch03:58;
      - Explainer:930: "You don't need to posit low initial entropy to explain why we see it".
    - **Saying it is inherited:** ch18:210 and :218–222 (= FULL:5023, :5031–5035): "the arrow is
      at the level of partition initial conditions, not at the level of substratum dynamics".
    - At `M`, the quoted Substratum sentence is absent. [M/Substratum:401](https://github.com/amaybaum/incompleteness/blob/5ea5a40218e4e660b39a9b149050ced4f95d9b48/papers/Substratum.md#L401)
      instead states: "The confinement is time-symmetric and fixes where observers can exist,
      not a direction of time; that the arrows the observer sees descend from it together with
      horizon growth is not established." M/ch18:214–216 likewise leaves alignment open.
      The disagreement at these rechecked sites is historical, not a current contradiction.
      This note neither certifies the entire historical search nor edits a manuscript.
  - **What is missing.**
    - **Its category is stated.** State-level realization or solution-specific data: Main:60,
      :524; ch01:85; ch04:170.
    - **Its content is not.** No source specifies which state-level preparation event or law is
      realized.
    - **Any principle fixing that content** would be b-new.
- **S.2.6, ordering against O-RDY.**
  - #914 makes O-RDY depend on the μ leg, "or a named prior [C]", and records two further
    routes: "under H-μ, equal-time readiness is absent, so positives go through conditioned
    patches (I2, open) or cross-time routes". It also forbids assuming "a record that supplies
    readiness (Z1)" (#914 c.6563412926, row 1′).
  - Read through CR_slice on a stipulated readiness event, the μ leg needs the readiness event
    that O-RDY supplies, so that route is circular.
  - Read through CR_rec, it needs retained records (O-REC). On K1, MR★ C-3 (:1342–1371) places
    the record-formation gap at the unsourced ready region. C-4 (:1373–1380) records the trace
    route as blocked by C-3, and #914 row 1′ forbids assuming a record that supplies readiness
    (Z1).
  - So the CR_rec route has not been shown to be non-circular against O-RDY: μ-leg preparations
    need CR_rec, CR_rec needs O-REC, O-REC needs O-RDY, and O-RDY needs the μ leg.
  - The named-prior option, conditioned patches and cross-time routes are not circular. So no
    circularity forces O-OBSMU to come before O-RDY, provided one of those routes is used.
  - Status: ELABORATING.

**Verdict S.2.** The μ leg is not sourced from the axioms. Main supplies a measure only through
Q8 and H-OC_orb (b-stated: Main:56, :62, :726 (iv)), which need finite total `S`. Orbit-level
conditioning cannot produce a time-slice preparation. A preparation law at a time is either a
realization datum with supplied content (b-stated category), or the canonical measure conditioned
by CR_slice (b-new).

### 3.1 Node I.1 — non-consumers U1–U3

KC `finite_horizon_equivalence` is a biconditional for every `P : Traj V K → ℝ`, with no
hypothesis on `μ` (`Equivalence.lean:462`). Every induced law with a finite alphabet is in its
scope. So U1–U3 use nothing from the residual choice. They carry no prediction and do not
discharge O-OBSMU for any consumer that does.

### 3.2 Node I.2 — Theorem SI (support invariance), consumer R1

**Setting.**

- `C_V` and `C_H` are finite, and `φ` is a bijection of `C_V × C_H` of order `L`. Finite order
  needs finite total `S` (Main:62, :268).
- `μ_a` is the hidden law given root `a`. It may depend on `a`.
- `Γ_t(a, j) = μ_a{h : π_V φ^t(a, h) = j}`.

**Theorem SI (PD-here).** Whether the family is P-divisible on `{0, …, L}` depends on the `μ_a`
only through their supports `Σ_a`.

*Proof.*

1. **Permutation status depends only on the supports.** `Γ_s(a, ·)` is a point mass iff
   `h ↦ π_V φ^s(a, h)` is constant on `Σ_a`. A square stochastic matrix is a permutation iff its
   rows are point masses at pairwise distinct columns. Both conditions depend only on these maps
   restricted to the `Σ_a`.
2. **All permutations give divisibility.** `Γ_0 = I`, and `Γ_L = I` whatever the `μ_a`, because
   `φ^L = id`. If every `Γ_s` with `1 ≤ s ≤ L − 1` is a permutation, then `Γ_s⁻¹ Γ_t` is a
   stochastic divisor for all `s < t ≤ L`.
3. **One non-permutation gives indivisibility.** Suppose some `Γ_s` is not a permutation.
   - Two distinct rows of `Γ_s` then share positive mass (Main:139).
   - KC `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`) assumes only
     that `Γ_s` is row-stochastic. With `Γ_L = I`, it gives P-indivisibility on `{0, …, L}`.
   - The P-divisibility predicate is `PDivisible` (`CausalReadback.lean:54`). `□`

**Corollary SI-1** (every `Σ_a = C_H`). A point-mass row forces
`φ^s({a} × C_H) = {σ(a)} × C_H`, by counting and injectivity. So the verdict depends on
`(φ, π_V)` alone. It is indivisibility exactly when the hidden state changes the visible value
from some root at some time `1 ≤ s ≤ L − 1`.

**Countercontrol CC-1.** Take `C_V = C_H = {0, 1}` and `φ(v, h) = (v ⊕ h, h)`, so `L = 2`.

- Uniform `μ_H`: `Γ_1 = [[½, ½], [½, ½]]` and `Γ_2 = I`. Not P-divisible.
- `μ_H = δ_1`: `Γ_1` is the swap and `Γ_2 = I`. P-divisible.

**Status: ELABORATING.** Main:141 already carries the shared-prior, full-support form: "With a
full-support visible prior the hypothesis and the conclusion coincide" … "For every visible
prior, a non-deterministic visible step … makes some `Γ_s` a non-permutation". What this note
adds is the root-dependent generalization and the statement that only the supports matter.

**Limits.**

- The consumer is a property of the whole recurrence cycle, which no accessible window reaches
  (Main:141).
- The theorem needs the product form (b-stated) and finite total `S`.

### 3.3 Node I.3 — consumer R2: generic dichotomy, not invariance

**Proposition G (PD-here).** Fix `(φ, π_V)`, an order `k` and a support `Σ ⊆ C_V × C_H`. Among
preparation laws with exactly this support, exactly one of the following holds:

- no law has a C4 gap at order `k`;
- every law has one, except for a closed set of Lebesgue measure zero in the relative open
  simplex `Δ_Σ` of such laws.

*Proof.*

1. **Positivity depends only on the support.** A visible history `p = (x_0, …, x_k)` has positive
   probability iff some `(a, h) ∈ Σ` produces it, that is, iff
   `π_V φ^t(a, h) = x_t` for all `t ≤ k`.
2. **The criterion is polynomial.** Fix two positive-probability histories `p ≠ p′` with
   `x_k = x′_k`, and an outcome `y`.
   - Write `D_p = Σ_{(a,h) ∈ Σ} λ(a, h) 1[(a, h) produces p]`, and `N_p(y)` for the same sum
     with the further condition `π_V φ^{k+1}(a, h) = y`.
   - Both are linear in the law `λ`. Their next-step probabilities are `N_p(y)/D_p` and
     `N_{p′}(y)/D_{p′}`.
   - Since `D_p, D_{p′} > 0` on `Δ_Σ`, the two differ at `y` iff
     `Q_{p,p′,y}(λ) = N_p(y) D_{p′} − N_{p′}(y) D_p ≠ 0`, a polynomial in `λ`.
3. **The dichotomy.** A C4 gap at order `k` exists at `λ` iff `Q_{p,p′,y}(λ) ≠ 0` for some
   triple. The set of triples is finite and, by step 1, the same for every `λ ∈ Δ_Σ`.
   - If every `Q` vanishes identically on `Δ_Σ`, no law has a gap.
   - Otherwise some `Q` is a polynomial that is not identically zero on the open set `Δ_Σ`
     (open in its affine hull). The laws with no gap lie in its zero set. That set is closed, and
     it has measure zero, because a polynomial that does not vanish identically on a connected
     open set has a null zero set. `□`

**Product preparations `λ = ν ⊗ μ_H`** (Main's rooted setting). These form a lower-dimensional
subset of `Δ_Σ`. Here `Σ = Σ_V × Σ_H`, and `D_p` and `N_p(y)` are bilinear in `(ν, μ_H)`. The same
argument therefore gives the same dichotomy on the product of the two relative open simplices.

**The dichotomy is not invariance.** The canonical law can lie in the exceptional set.

**Countercontrol CC-2 (PD-here, checked by hand; construction from the first review).**

- **The construction.** `C_V = {0, 1}`, `C_H = {0, 1}^m` with `m ≥ 2`, and
  `φ(x, h) = (x ⊕ h_0, rot h)`, where `(rot h)_i = h_{i+1 mod m}`.
  - It is a bijection. Its inverse is `(x′, h′) ↦ (x′ ⊕ (rot⁻¹ h′)_0, rot⁻¹ h′)`.
  - `φ^{2m} = id`.
  - Along a trajectory `x_{t+1} = x_t ⊕ h_t`, so `x_t = x_0 ⊕ h_0 ⊕ … ⊕ h_{t−1}`.
- **The preparations.** Take `x_0` uniform and independent of `h`. Let `h_0` and `h_1` have
  uniform marginals and `P(h_0 ≠ h_1) = q ∈ (0, 1)`. Any further coordinates are independent and
  uniform. Every such law has full support.
- **R2 at order 1.**
  - A history `(x_0, x_1)` reveals `h_0 = x_0 ⊕ x_1`, and `x_2 = x_1 ⊕ h_1`.
  - The histories `(0, 0)` and `(1, 0)` both end at `x_1 = 0`. Their next-step probabilities of
    `x_2 = 1` are `P(h_1 = 1 | h_0 = 0) = q` and `P(h_1 = 1 | h_0 = 1) = 1 − q`.
  - So there is a gap iff `q ≠ ½`. The uniform tape (`q = ½`) has no gap at order 1. Every other
    `q` in `(0, 1)` has one.
- **R3 on the window `{0, 1, 2}`.**
  - `Γ_1(a, ·)` is the law of `a ⊕ h_0`, uniform for both roots, so its rows are equal.
    `Γ_2(a, ·)` is the law of `a ⊕ h_0 ⊕ h_1`, with flip probability `q`.
  - `Γ_1 Λ` has equal rows for every `Λ`. So `Γ_2 = Γ_1 Λ` needs `q = ½`.
  - So the family is P-divisible on `{0, 1, 2}` at `q = ½` (take `Λ = Γ_2`), and not P-divisible
    for `q ≠ ½`.

**A related zero-memory uniform-tape instance.** Main:178's §3.4 fair-coin dilation has zero
conditional memory "exactly at every horizon time" under its uniform tape. It is not the same
construction as CC-2. This note does not check whether a correlated tape law in that
construction gives memory.

**Verdict R2.** Not invariant, even at fixed full support. Proposition G still says that the
verdict at the canonical law is non-generic whenever it differs from the generic one.

### 3.4 Node I.4 — consumer R3

**Closedness (PD-here).** Fix a window `{0, …, n}` and the supports `Σ_a` of the hidden laws
given each root. Let `Δ` be the product over roots of the relative open simplices of laws with
those supports. The set `Div ⊆ Δ` of hidden-law families at which the rooted family is
P-divisible on `{0, …, n}` (`PDivisible`, `CausalReadback.lean:54`) is relatively closed in `Δ`.

*Proof.*

1. Each `Γ_t` is linear in the hidden-law family, so `μ ↦ (Γ_t(μ))_{t ≤ n}` is continuous.
2. The set `Stoch` of row-stochastic `|C_V| × |C_V|` matrices is compact.
3. For a pair `s < t`, let `F_{s,t} = {(A, AΛ) : A, Λ ∈ Stoch}`. It is the image of the
   compact set `Stoch × Stoch` under the continuous map `(A, Λ) ↦ (A, AΛ)`.
   - The domain `Stoch × Stoch` is compact, and so
     is its image.
   - So `F_{s,t}` is closed.
4. `Div` is the intersection, over the finitely many pairs `s < t ≤ n`, of the preimages of the
   `F_{s,t}` under the continuous maps `μ ↦ (Γ_s(μ), Γ_t(μ))`. So `Div` is closed in `Δ`. `□`

**Consequences.**

- `Δ` is connected. So the verdict is the same at every point of `Δ` iff `Div` is empty or all of
  `Δ`, that is, iff `Div` is also relatively open.
- CC-2 (§3.3) shows that `Div` can be neither, at full support. So window P-divisibility is
  **not invariant in general**.

**Open for native K1.** Whether some native `(φ, π_V)` has a window verdict that does not depend on
the prior is open. Settling it needs a paper argument or a native two-prior counterexample. The
first version said that finding such a pair "is a computation"; that is withdrawn, since CC-2 was
found by hand.

### 3.5 Node I.5 — consumers L1–L5, and the root convention

- **L3** is refuted as invariant by Main:60's swap example.
- **L1 and L2** are stated relative to a named measure (Main:86, :276). They need Q8 and nothing
  less.
- **L4 and L5:** non-invariance is argued, not shown.
  - L4 needs setting–hidden independence (Main:366 ff.) and capacity (2).
  - L5 needs a ready region, which H-μ lacks (Lemma P-1).

**Root convention (PD-here, restricted).** Let the visible prior `ν` have full support. Then for
every root `a`, conditioning on the observed `X_0 = a` gives `μ_a`. Every row of the rooted family
is then a conditional law given an initial record, and capacity (1) is not needed for R1.

The rooted family keeps rows of roots with visible probability zero (Main:139). If `ν` lacks
full support, those rows cannot be obtained by conditioning. They are then either a preparation
(capacity (1)) or a convention extending `μ_a` to those roots.

### 3.6 Node D — K1's dynamical obstructions, conditionally independent of `(Obs, μ)`

**Lemma D, identity part (PD-here; MR★:479–485 and :491–509).** On K1, `φ^t` is additive. So
`pr_Y φ^t(s) = Σ_X Φ^t_{YX}(s_X)`, with each `Φ^t_{YX}` a fixed homomorphism. This is an
identity in the state `s`, and so it holds under every `μ`.

**Lemma D, conclusion (conditional).** Two premises, both named:

- **D-SEL (definitional).** A selectable interaction is a setting-dependent change of the
  carrier's transformation that is not only an additive offset `T_s = τ_{Bs} ∘ T_0`. It must also
  survive the foils of #866 c.6567167742: precomputed selector, post-processing, XOR relabelling
  and masked kicks, effects of `Z_rest` alone, and decoy cancellation.
  - Under additivity, settings give exactly such offsets.
  - Offsets compose to non-commuting affine maps (`T_s T_{s′} ≠ T_{s′} T_s` in general).
  - So whether they count is a question for O-SET's open definition (#1009), not a fact about
    `μ`.
- **S-L4 (MR★:531–562), with its torus lift repaired by C-11 (:1450–1462).** PD in a frozen record.
  C-10 (:1441–1448) corrects the slice count of S-C4a, the corollary, and the log; it does not
  correct S-L4.
  - **Review status.** MR★:1297–1300 records that the review of `fc68d333` "verified S-L1, S-L3,
    S-L4 (case analysis)". This note has not re-verified S-L4.
  - **On "unreviewed".** The earlier reviews of #1110 called S-L4 "unreviewed". That is not
    accurate: the frozen record reports a review. Under §A.46 item 7, though, that report does
    not count as verification here, so S-L4 is used only as a named premise.
  - **Hypotheses.** `Λ = ℤ^d` with nearest neighbours, or a torus with `N ≥ 5w + 2` (via C-11's
    cylinder lift), and `a` injective on `𝐑`.

**Scope of the K1 obstruction.** It concerns two things under the native linear rule:

- **Selectable interactions.** Under D-SEL, no `(Obs, μ)` on K1 supplies capacity (2).
- **Interference destruction.** On K1, marking leaves the carrier's transfers unchanged, so a
  record formed by the interaction does not cause interference loss (MR★ S-L5, :584–593, as
  reworded by C-9, :1433–1439).
  - S-L5 is PD in a frozen record. It is not among the lemmas MR★:1297–1300 reports as verified.
  - #1023 c.6555028014 (off `main`) also reports S-L5 as holding "as scoped". This note keeps the
    narrower statement, since that record is off `main`.
  - It is re-read here, not independently reviewed.
  - It follows from S-L1, the additivity identity re-derived in Lemma D, so it is conditional on
    neither D-SEL nor S-L4.

Under S-L4 (review reported in the frozen record, not re-verified here; `ℤ^d`, or a torus with
`N ≥ 5w + 2`, and `a` injective), no confined pattern on K1 persists over `2w + 2` consecutive
slices (S-C4a as corrected by C-10), for any `(Obs, μ)`.

The obstruction does **not** claim that every localized record is impossible on K1.

- MR★ C-2 (:1322–1340) withdraws that claim: a free field leaves a wake.
- MR★ C-4 (:1373–1380) records the trace route as `UNDECIDED`.

Every statement here is scoped to K1. Each rests on a stated premise:

- the selectable-interaction statement on D-SEL;
- the confined-pattern statement on S-L4;
- the interference statement on S-L1 alone, through S-L5.

**Status: ELABORATING** (a reduction of the MR★ §S lemmas).

### 3.7 Node C — the law H-μ induces on K1 with finite `𝐑` (ELABORATING)

**Scope.** `𝐑 = ℤ/q` on a finite lattice (a torus), so `S` is a finite abelian group. This
excludes the infinite lattice `ℤ^d` and the `ℤ_p` and `ℝ/ℤ` cases
of K1.

**Lemma P-1 (PD-here).** Let `S` be a finite abelian group, `φ` an automorphism of `S`, and `μ`
the Haar (uniform) probability on `S`. For a region `X`, let `S_X` be its factor and
`pr_X : S → S_X` the projection. Then:

- the law of `pr_X(φ^t s)` is uniform on `S_X` for every `t`;
- for disjoint `X` and `Y`, `pr_X(φ^t s)` and `pr_Y(φ^t s)` are independent;
- a fixed pattern on `X` has probability `|S_X|⁻¹`.

*Proof.*

1. `φ^t` is a bijection, so it preserves the uniform law.
2. `pr_X` is a surjective homomorphism. Each fibre `pr_X⁻¹(x)` is a coset of `ker pr_X`, so all
   fibres have size `|S|/|S_X|`, and the pushforward is uniform.
3. `pr_{X∪Y} = (pr_X, pr_Y)` is a surjective homomorphism onto `S_X × S_Y`, since the regions are
   disjoint factors. Its pushforward is uniform on the product, which is the product of the
   uniform laws. `□`

**Proposition C (PD-here).** Take `S`, `φ` and `μ` as in Lemma P-1, and a homomorphic readout
`π : S → G` onto a finite abelian group `G`.

*Definitions.*

- `Ψ_k(s) = (π φ^0 s, π φ^1 s, …, π φ^k s) ∈ G^{k+1}`. This is a homomorphism. Its image is
  `I_k ≤ G^{k+1}`.
- `K_{k+1} = {y ∈ G : (0, …, 0, y) ∈ I_{k+1}}`, with `k + 1` zeros. It is a subgroup of `G`.
- `π̂ : G^{k+2} → G^2` keeps the last two coordinates, `(g_0, …, g_k, g_{k+1}) ↦ (g_k, g_{k+1})`.
- `K′_{k+1} = {y ∈ G : (0, y) ∈ π̂(I_{k+1})}`. It is a subgroup of `G` with
  `K_{k+1} ≤ K′_{k+1}`.

*Claims.*

1. The history `X_{≤k} = Ψ_k(s)` is uniform on `I_k`.
2. For every `h ∈ I_k`, the conditional law of `X_{k+1}` given `X_{≤k} = h` is uniform on a coset
   `y_0(h) + K_{k+1}`.
3. `H(X_{k+1} | X_{≤k} = h) = log₂|K_{k+1}|` for every such `h`. The conditional law given `X_k`
   alone is uniform on a coset of `K′_{k+1}`, and
   `M_k = I(X_{<k}; X_{k+1} | X_k) = log₂ [K′_{k+1} : K_{k+1}]`.

*Proof.*

1. By Lemma P-1's step 2 applied to the surjective homomorphism `S → I_k`.
2. `I_{k+1}` is uniform by step 1. Let `ρ : I_{k+1} → I_k` drop the last coordinate. It is a
   surjective homomorphism with kernel `{0}^{k+1} × K_{k+1}`. So the fibre over `h` is
   `{(h, y_0(h) + κ) : κ ∈ K_{k+1}}` for any `y_0(h)` in it, and the uniform law on `I_{k+1}`
   conditions to the uniform law on that coset.
3. The same argument applies to `π̂(I_{k+1})`, which is the image of a homomorphism and so carries
   the uniform pushforward. Its projection to the first coordinate has kernel `{0} × K′_{k+1}`.
   So `H(X_{k+1} | X_k) = log₂|K′_{k+1}|` at every positive-probability value. Then
   `M_k = H(X_{k+1} | X_k) − H(X_{k+1} | X_{≤k}) = log₂|K′_{k+1}| − log₂|K_{k+1}|`. Finally,
   `K_{k+1} ≤ K′_{k+1}`, because `(0, …, 0, y) ∈ I_{k+1}` gives `(0, y) ∈ π̂(I_{k+1})`. `□`

**Status.** ELABORATING. The equal-time part overlaps #914 C-10, which cites an off-`main` record.
That record is classified in §7. The proofs above are complete in this note and do not use it.

### 3.8 Literature

1. **Barandes, arXiv:2309.03085v2, §3.1, pp. 8–10, equations (24)–(35). Read directly.**
   - The tuple is `(C, T, T_0, Γ, p, A)`, with `Γ_ij(t ← t_0) = p(i, t | j, t_0)`.
   - Quoted: "Only the standalone probabilities `p_1(0), …, p_N(0)` at the initial time 0 will be
     taken to be freely adjustable".
   - Quoted: the definition of `Γ` "is independent of the choice of standalone probabilities …
     at the initial time 0".
   - Use here: to identify that R4 needs Q9′.
   - Main already states Q9′: Main:137 draws the hidden state from one prior "whatever the root",
     and Main:284's channel `Φ(ρ_V) = Tr_H[U_φ(ρ_V ⊗ ρ_H)U_φ†]` uses one fixed `ρ_H` for every
     input. So R4 needs nothing new relative to Main.
   - The source's divisibility (35) is imposed only at conditioning times. It is not Main's
     P-divisibility, and ROF records that the two are not identified.
2. **Barandes, arXiv:2302.10778v3. Read directly: abstract page only.** Not used.
3. **'t Hooft, arXiv:1405.1548v3. Read directly: abstract page only.** Not used.
4. **The Past Hypothesis and the record asymmetry. Secondary only:** web-search result summaries,
   2026-11-04. The summaries attribute the record asymmetry to a low-entropy initial macrocondition
   (Albert, Loewer), and report that arXiv:2309.03484 calls the basic Past Hypothesis too vague.
   No passage was read, and nothing here uses them as support.
5. **Additive cellular automata (superposition).** Background only. No source was read. Lemma D's
   identity is derived here directly.

## 4. What is missing

### 4.1 Requirements for `(Obs, μ)`, sorted

| # | Requirement | Group | Locator and layer |
| --- | --- | --- | --- |
| Q1 | A finite outcome alphabet | (a) | Main Definition (Main:44: "finitely many distinguishable internal states") and Lemma 1 (Main:48). PD with an external holographic input. |
| Q2 | An observer cut exists | (a) | Main:44, :50; constitutive of Axiom 1 on the adopted reading (Main:38–40). |
| Q3 | Which cut | (b-stated), as a parameter | Main §1.4, Main:86. |
| Q4 | Product form `S = C_V × C_H` | (b-stated) | "idealized" (Main:54). A finite readout does not imply it. Take `S = {1, 2, 3}` and `π(1) = π(2) = 0`, `π(3) = 1`: the fibres have sizes 2 and 1, so `S` is not `C_V × C_H` with `π` the projection (PD-here). |
| Q5 | Readout slice content | (b-stated, construction step) | Main:222 projects the flow onto the configuration sector. This is a step inside the marginalization, not labelled as a posit (§0, sorting rule). Whether the slice is native is O-ACC (open). |
| Q6 | `μ` is invariant | (b-stated) | Part of the canonical-measure posit (Main:56; ledger Main:726 (iv)). Realization priors need not be invariant (Main:60, :524). |
| Q7 | `μ` is unique | not available | KC `ensemble_underdetermined`. |
| Q8 | Maximal-entropy selection of the counting measure | (b-stated) | Main:56; ledger Main:726 (iv), "a standard but substantive epistemic postulate, not derived"; KC `counting_maximal_entropy`. Needs finite total `S` (Main:62, :268), a branch premise under the owner's finiteness decision (quoted in §7). |
| Q9 | Root independence `μ = ν ⊗ μ_H` | (b-stated) | Main:60, :137; ROF Q4. |
| Q9′ | The hidden laws given each root do not change when the visible initial distribution is varied | (b-stated) | Main:137, :284. Implied by Q9. "Measurement independence" is an analogy only. |
| Q10 | The supports `Σ_a` of the hidden laws | (b-stated) | Part of the realization datum `μ_H` (Main:60). Full support under Q8. |
| Q12 | The measure beyond its support | (b-stated) | Q8, or a realization datum (Main:60). |

The axioms imply none of Q3–Q12. The conditioning and preparation requirements are sorted
separately below, in the four groups the owner asked to be kept apart.

The first version's Q11 ("a low-entropy or ready initial condition") is not lost. Its category is
now group (3), and its low-entropy content is part of (4a) (§4.6.1).

| Group | Requirement | Classification | Locator |
| --- | --- | --- | --- |
| **(1)** | **H-OC_orb:** the measure is the maximal-entropy *invariant* measure compatible with the observer's records; observer-lacking orbits are outside scope | **b-stated** (orbit level) | Main:62; Main:726 (iv); ch01:85 |
| **(2a)** | **CR_rec:** the present-value conditional and the in-realization history posterior | **(b-stated, construction step); accepted in D-OB7** | Main:88, :99, :105 (§4.6.2 Q-b) |
| **(2b)** | **CR_slice:** conditioning on a stipulated event at a time slice that goes beyond the observer's records | **b-new** | Stated nowhere (S.2.3–S.2.4). It drops Q6 unless `φ(R) = R` |
| **(3)** | **Q11′ category:** a state-level preparation event or law, admitted as starting data | **b-stated** (as a category) | Main:60 ("its own fixed hidden prior `μ_H`"); Main:524 (a structured state-level prior); ch01:85; ch04:170 (initial data "solution-specific"); appC:329. The book states a low-entropy initial condition (ch18:210, FULL:5023–5033) |
| **(4)** | **G-PREP:** a physical principle that generates the *content* of those events, saying which state-level preparation is realized | **none identified.** Any such principle would be b-new | No source supplies one (S.2.5, "What is missing"). The split into (4a) cosmic data and (4b) laboratory preparations is in §4.6 |

### 4.2 By consumer

| Consumer | What it needs |
| --- | --- |
| U1–U3 | Q1 only. They are not residual-choice consumers. |
| R1 | Q1, Q2, Q4, Q10 and finite total `S`. Supports suffice (Theorem SI). Relative to Main nothing new; relative to the axioms Q4 and Q10 are b-stated. |
| R2, R3 | The measure itself (CC-2), so Q12. R3 on native K1 is open. |
| R4 | Q9′, which Main states. Nothing new. |
| L1, L2 | Q8 only. |
| L4 | Setting–hidden independence (Main:366 ff.) and capacity (2). |
| L3, L5 | A measure for a preparation that is actually made. |

**For L3 and L5. A scoped answer, not a minimality result.**

- **Group (1) is not enough.** An invariant measure gives equal weight along each orbit, so it
  cannot produce a preparation made at a time (S.2.4).
- **Two routes reach a time-slice preparation law.** Neither uses more than groups (2) and (3):
  - **Route (i), datum:** take the preparation law directly as group-(3) starting data. No new
    rule is needed. The content is supplied, not sourced, so L3 and L5 outputs are conditional
    on supplied data. Under ch04:170 they are solution-specific.
  - **Route (ii), conditioning:** derive the preparation law from Q8 by conditioning on an event
    at the slice. If the event is the observer's own record, this is CR_rec (2a, a construction
    step, D-OB7). If it is stipulated beyond the records, it is CR_slice (2b,
    b-new). Reading the result as a preparation law is H-PREP (open). §4.6.2 tests route (ii)
    with record events.
- **The second review's formulation** was "a sourced state-level preparation event, whose
  category is already admitted as data, plus one new slice-conditioning rule". I checked it
  against route (i), and it holds for route (ii) only. Route (i) needs no new rule. So the
  slice-conditioning rule is needed only to obtain the preparation law *from the canonical
  measure* on stipulated events. §4.6.2 refines this, and D-OB7 accepts the refinement: for the observer's
  own visible data, Main already defines the conditional (CR_rec, a construction step). Using it
  as a preparation law is H-PREP.
- **Either way, group (4) is missing.** No physical principle generating the content of the
  preparation event is identified in the corpus. This note does not supply one.
- **Not shown minimal.** This note does not show that no smaller ingredient serves.

**Which assumptions prevent OI from deriving its own observer and measurement structures.** After
the (4a)/(4b) split, the list is in §4.6.4.

### 4.3 Proposal P-R (not adopted; awaiting the owner)

**Statement.** For a declared cut `V`, the laws are drawn from the counting measure, or Haar
measure on a compact completion, conditioned by CR_slice on a declared state-level preparation
event `R`. Group (2) is added; group (3) content is supplied. P-R does not supply group (4).

**Failable controls (§A.29).**

- **(i) Lemma 3, prong 1 (Main:62).** Main:62 excludes visible merges "wherever the observed
  statistics are of that doubly stochastic class under the uniform prior". Main:276 and :524
  confine double stochasticity to uniform-prior marginals.
  - **Evaluation (PD-here).** CR_slice on an `R` that constrains hidden sites makes the hidden
    prior non-uniform. The visible marginals are then generically not doubly stochastic, even for
    a bijection. So under P-R, observed departures from double stochasticity no longer witness a
    merge, and prong 1 loses its empirical input.
  - Lemma 3's conclusion (bijectivity) survives through prong 2, which is structural:
    finiteness and recurrence on the eventual image (Main:62).
  - **Verdict:** control (i) **fails as worded**. P-R removes prong 1's empirical input. It does
    not contradict Lemma 3's conclusion.
  - The same loss applies to any preparation datum that constrains hidden sites, whether it is
    supplied directly (route (i)) or obtained by conditioning (route (ii)). It is not specific to
    P-R.
  - P-R could be scoped away from the control only by restricting its conditioning to visible or
    apparatus sites that leave the hidden prior uniform. That restriction is a further free
    choice.
- **(ii) Main §4.6.** Main:744 (the same selection role at M/Main:744) replaces the past hypothesis "in its role of selecting
  observer-compatible configurations". P-R must not take over that selection role. It fails if
  `R` is required to select observer-compatible configurations rather than a laboratory
  preparation.
- Theorem SI and Lemma D hold for every measure, so they are not controls.

**Independent consequence: none identified.** Proposition C's coset structure already holds under
unconditioned H-μ.

**Refuting outcome.** None realizable on K1. MR-1 stage 1 sources no native record law there
(scoped `GAP`).

**§A.29.** `R` and CR_slice are free, so P-R fails the hard-to-vary test. Not recommended.

### 4.4 Beyond O-OBSMU: capacities (2) and (4)

On K1, selectable interactions (capacity (2)) need a dynamical ingredient. Whether records
(capacity (4)) do is not settled: K1 excludes confined patterns, conditional on S-L4, but it does
not exclude every localized record (§3.6). SM §3.1 states a state-dependent coupling
principle. Its explicit construction (SM:112) makes the transfer to site `i` depend on the value
at `i + 1`, so in it the transfer does depend on another region's state. MR★:667 lists it as
outside `K★` and unscreened.

**Proposal P-SDC (not adopted; awaiting the owner).** The native step has SM §3.1-type
state-dependent coupling.

**Failable controls (§A.29).**

- SM's constraints (i)–(iii) (SM:108).
- Substratum's A5-based reconstruction must survive as the reference-class limit (SM:108,
  "the reference derivation chain survives").
- A sourced setting region must pass every foil of #866 c.6567167742.

**Refuting outcome.** The first version's first refuting bullet is withdrawn: SM:112 already
exhibits state-dependent transfer. What remains: if no rule satisfying (i)–(iii) gives a sourced
setting that passes the foils, with a readable record, P-SDC is refuted for that class.

**Independent consequence: none identified.** The gravitational role in SM §3.1 is the
principle's motivation, not a consequence derived from it.

**§A.29.** The switching rule is unconstrained, so P-SDC is easy to vary. Testing it is not
authorized here.

### 4.5 What this note does not establish

- That the architecture is refuted, or that no extension supplies `(Obs, μ)`.
- That O-OBSMU is closed for any consumer.
- That either route of §4.2 is minimal, or that any group-(4) principle exists or cannot exist.
- Anything about window divisibility for native K1.
- That P-R or P-SDC is true, adopted or recommended.
- Any change to a manuscript, ROADMAP, frozen record or Lean module.

### 4.6 The (4a)/(4b) split

**Origin.** The final review of `cd15123b` (#1110 c.6643749363) raised a hidden-assumption marker:
group (4) may split into cosmic initial data (4a) and laboratory preparations (4b). The owner
authorized a bounded, paper-only examination (#866 c.6643823627, which quotes amaybaum, Claude
Code session chat, 2026-11-04; the record was posted 2026-11-04T22:31:55Z): "Determine which parts
are gauge choices, which are genuine physical inputs, and which remain unexplained"; "A positive
answer to the first question does not establish the other two"; "My preferred direction is to
reduce the number of independent assumptions wherever a genuine derivation is possible, rather than
introducing a new observer-specific posit."

The original sorting reads the passages at `D`; the low-entropy row and the ARROW-1 account
below also state their recheck at `M`. The sorting is a reading of those sources, not a proof.

#### 4.6.1 (4a) Cosmic initial data

| Item | Source and quotation | Class |
| --- | --- | --- |
| Cardinality of the deep hidden sector | GR:142: "The cardinality of the deep hidden sector is gauge in the scope of this corollary". Scope: the leading-order transition law on accessible timescales. | **gauge** (scoped) |
| The representative within the reconstructed local equivalence class | ch19:210: "Gauge — no answer is physically required for representative choices that Theorem 24 identifies as observably equivalent". Substratum:538 lists among what does not falsify: "the choice among representatives related by the fixed-interface invariances of Theorem 24". This concerns the rule `φ`, not the configuration. | **gauge** (for `φ`'s representative) |
| Visible initial data as gauge | ch19:200: "If the initial state of the visible sector is also gauge-equivalent across a wide class of initial conditions … This is an intriguing possibility but has not been investigated within the framework's existing structure." | **near-miss.** Not established, and it generates nothing |
| Statistical isotropy of the initial state | ch19:198: "if the initial state of `φ` is statistically isotropic (one of the framework's six structural properties of the bijection), isotropy is built in … This is speculative". | **physical input** (stated property). Its use is speculative, and it constrains rather than generates the content |
| The uniform initial class | SM:48: the area-law lemma "uses range-1 dynamics together with **uniform initial conditions** … a theorem for that state class, not a universal entropy theorem for every admissible prepared state". SM:124 has the same. | **physical input**: a hypothesis of one lemma, about a reference class |
| A product initial state | GR:799, Theorem A.6: "Let the state … at `t = 0` be a product". GR:805: "The generalized second law is open." | **physical input**: a hypothesis of one theorem |
| Expansion and horizon growth | ch04:30: "the cosmological initial conditions are taken as given rather than derived". ch04:32: "The framework does not commit to a specific cosmological history beyond the structural arrow of horizon growth in the `Λ`-dominated phase." | **physical input** (a stated commitment) |
| A low-entropy start | ch18:214 at `D`, retained at M/ch18:214: "The cosmological partition has a specific initial condition: the universe begins in a low-entropy configuration". ch00:101 at `D`: "the arrow of time as emergent from partition initial conditions". M/ch18:214–216 explicitly leaves alignment open and states the expanding-FRW/NEC qualification. | **physical input** (stated in the book). The initial condition is supplied; an alignment mechanism remains open in #1112 |
| Which microstate | Substratum:552: "the *initial conditions* — the specific configuration of the bijection at any given time — are likewise not determined by the framework". Substratum:538: "the framework derives the structure from which evolution proceeds, not the state at `t_0`". | **unexplained** (solution-specific) |
| The very early universe | ch19:194: "**Framework status.** Not addressed." ch19:346 (table): "Initial state \| Framework-specific \| Partially gauge, partially irreducible". | **unexplained** |
| The vacuum-energy scale | GR:360: "The framework does not explain *why* `ρ ∼ H²/G`; this is set by initial conditions via the Friedmann equation." | **unexplained**: it is set by the initial data |

**Verdict (4a).**

- **Gauge, for structural data only.** The corpus identifies gauge freedom in two places: the
  deep-sector cardinality, for leading-order laws, and the choice of `φ`'s representative within
  a Theorem-24 class. No gauge freedom of the initial *configuration* is identified. ch19:200
  calls that question uninvestigated.
- **Physical inputs.** These are of two kinds:
  - **hypotheses of particular theorems, not asserted data:** the uniform reference class (SM:48,
    :124) and a product initial state (GR:799);
  - **stated commitments:** expansion with horizon growth (ch04:30, :32) and a low-entropy start
    (ch18:214).

  Statistical isotropy (ch19:198) is a stated property whose use there is speculative. None of
  these is one stated initial datum.
- **Unexplained.** Which microstate is realized, and the very early universe.
- **No principle** in the sources read generates the content of (4a).
- **#1112 is the accountable home for this question** (§A.45 rule 6). For the arrow claims
  audited by ARROW-1, RECOVERY §§B.2–B.9, C.1–C.6 and D, together with M/Substratum:401–409,
  support the following bounded account: observer selection is conditional and time-symmetric;
  the cosmological clock uses the expanding background and its stated matter conditions;
  thermodynamic and memory accounts retain preparation/boundary inputs and an orientation
  convention; a common alignment mechanism remains open. An orientation convention does not
  itself select asymmetric boundary data. The earlier comments c.6643691865 and c.6643840329
  are historical provenance for this narrowed account, whose substantive support is on `main`
  (§7). This note does not certify their whole-corpus search or assert a universal no-go.

#### 4.6.2 (4b) Laboratory preparations

**The question.** Is a laboratory preparation law the existing measure, conditioned on the
observer's accessible records at a time slice?

**The setting.**

- `S = C_V × C_H` is finite (Q4, finite total `S`), and `φ` is a bijection.
- The reference measure `μ` is one of two:
  - the counting measure (Q8);
  - `μ_orb`, the uniform law on the union `U_A` of the `φ`-orbits that meet a record event `A`.
    This is one reading of Main:62's orbit-level "compatible with the observer's records"
    (H-OC_orb).
- A record event `A ⊆ S` is a set of states at time `t_0`:
  - the present record: `A = {s : π_V(s) = r}`;
  - a record history: `A_p = {s : π_V(φ^{−j} s) = x_{t_0 − j}, 0 ≤ j ≤ k}`.

**Q-a, mathematics: can the conditional law be defined?**

- **Lemma Q-a1 (PD-here).** Take `A ≠ ∅`. Then `μ(· | A)` is defined iff `μ(A) > 0`.
  - Under the counting measure, this always holds for a nonempty `A`.
  - Under `μ_orb`, it holds by construction, since `A ⊆ U_A`.
- **Lemma Q-a2 (slice versus orbit; PD-here).** `μ_orb(· | A) = μ_count(· | A)`, the uniform law on
  `A`.
  - *Proof.* Both measures are uniform on sets that contain `A`. Conditioning a uniform law on a
    subset gives the uniform law on that subset. `□`
  - So once one conditions on the record event itself at the slice, the orbit-level selection
    makes no difference.
- **Invariance.** `φ_#(unif_A) = unif_{φ(A)}`. So the conditioned law is `φ`-invariant iff
  `φ(A) = A`. A preparation law at a time is generally not stationary, and that is expected.
- **Infinite `S`.** There is no counting measure there. Under Haar measure on a compact
  completion, an event constraining finitely many sites has positive measure in two cases:
  - when `𝐑` is finite;
  - when the event constrains those sites to sets of positive Haar measure (finite-readout
    events).

  For `𝐑 = ℤ_p` or `ℝ/ℤ`, an event fixing exact values has measure zero, and conditioning on it
  would need regular conditional probabilities, which are not examined here.
- **Verdict Q-a: yes.** The conditional law is defined in two settings:
  - on finite `S`, for every nonempty record event;
  - on compact completions, for events of positive Haar measure.

  It is not invariant unless `φ(A) = A`.

**Q-b, supply: does OI supply the records and the conditioning rule?**

*(i) The rule.*

- **As stated, Main's rule works at orbit level.** Main:62 reads "the selection among orbits is
  fixed by maximal entropy compatible with the observer's records". Main:726 (iv) reads "the
  maximal-entropy invariant measure compatible with the observer's records". The word
  "invariant" makes this a rule for choosing the reference measure. It does not produce a law at
  a time slice.
- **But Main also uses slice conditionals of that measure on the observer's own visible
  values:**
  - Main:88 defines the transition probabilities as
    `T_ij(t_2, t_1) = ∫_{Γ_H} δ_{x_j}[π_V(φ_{t_2−t_1}(x_i, h))] dμ(h)`, the conditional of the
    measure given `x_i` at `t_1`.
  - Main:105 reads: "The observer knows `x` but not `h` … Transition probabilities are obtained by
    marginalizing over the Liouville measure".
  - Main:99 (§1.5): the next-step law after a positive-probability history is the pushforward of
    the hidden posterior given that history.
- **Refinement of group (2), accepted in narrowed form (D-OB7).** This was checked against Main:88, :99 and
  :105, and narrowed after #1110 c.6644159894.
  - **CR_rec.** It has two parts:
    - the conditional of the stated measure on the observer's present visible value (Main:88,
      :105; ROF Q2 and Q4);
    - the hidden posterior after a visible history within a given realization and its initial
      law (Main:99).
  - **Classification of CR_rec: (b-stated, construction step).** These lines define predictive
    quantities *given* a law. They are not a measure-selection rule.
  - **CR_slice, b-new (group (2b)).** Conditioning on stipulated events beyond the observer's
    records, such as the content of hidden or apparatus sites outside `V`.
  - **Owner decision (D-OB7).** amaybaum, Claude Code session chat, 2026-11-05 (#866
    c.6649267203): "Accept the narrowed classification. Conditioning on the observer's present
    visible value, and computing an in-realization history posterior given an initial law, are
    existing construction steps in Main. This does not establish a physical mechanism that
    selects the probability law or generates a laboratory preparation."
- **H-PREP, a named hypothesis of the reduction.** A laboratory preparation law is the
  in-realization conditional of the stated measure on the observer's visible past.
  - **Main does not state this.** Main uses the history posterior for memory witnesses (§1.5),
    not as a preparation law.
  - **Main and ROF treat preparations otherwise.** They treat structured hidden preparations as
    realization data: Main:60, "its own fixed hidden prior `μ_H` as part of the realization
    datum"; ROF Q3(ii) (ROF:73), "structured `μ_H` is allowed as realization/preparation data".
  - **Status.** H-PREP is the reduction's own reading. The owner recorded it as an explicit open
    hypothesis (D-OB8, #866 c.6649267203). It is not adopted.

*(ii) The records.*

- **The present record** is the declared cut's readout (Q3; Q5, a construction step). It is
  supplied as b-stated data.
- **Lemma Q-b1 (equal-time blindness; PD-here).** Under the counting measure on `C_V × C_H`,
  conditioning on `π_V(s) = r` at a time slice gives `δ_r ⊗ unif(C_H)`. This is ROF Q4's
  conditioning identity.
  - *Proof.* There are `|C_H|` states with `π_V = r`, and each has weight `1/(|C_V||C_H|)`. `□`
  - So conditioning on the present record alone prepares nothing outside the cut. A preparation
    of a system outside `V` can come only from records that the dynamics has correlated with it,
    which means the record history.
- **The record history.** Conditioning on `A_p` is defined (Q-a), and it gives the hidden
  posterior (Main:99).
  - For this to be the observer's *accessible* record at `t_0`, `V` must hold at `t_0` a record
    of its past values. That is retention: O-RET, O-REC and O-ACC, all open.
  - Retention is not excluded on K1. S-L4 excludes only confined patterns, MR★ C-2 withdraws the
    impossibility claim, and the trace route is `UNDECIDED` (C-4).
  - On K1, however, retention is not independent of O-RDY.
    - MR★ C-3 (:1342–1371) places the record-formation gap at "the absence of a physically
      sourced quiet, ready region".
    - C-4 (:1373–1380) records the trace route as "blocked at stage 1 by C-3".
    - #914 row 1′ forbids assuming a record that supplies readiness (Z1).
    - So this route has not been shown to be non-circular against O-RDY (S.2.6).
- **Lemma Q-b2 (mirror; PD-here).** Setting: `σ` is an involution of `S` that preserves the
  counting measure and satisfies `σφσ = φ⁻¹`, `A` is an event with `μ(A) > 0`, and
  `σ(A) = φ^m(A)` for some integer `m`. Then for every `t ≥ 0` and every `B ⊆ S`,

      μ(φ^{−t}s ∈ B | s ∈ A) = μ(φ^{t+m}s ∈ σB | s ∈ A).

  - *Proof.*
    1. Let `s` be uniform on `A`. Then `σs` is uniform on `σ(A) = φ^m(A)`, so `σs = φ^m s″`
       with `s″` uniform on `A`.
    2. Since `σφ^tσ = φ^{−t}`, we have `φ^{−t}s = σφ^t(σs) = σφ^{t+m}s″`.
    3. As `σ` is an involution, `φ^{−t}s ∈ B` iff `φ^{t+m}s″ ∈ σB`. `□`
  - *Instance on K1.* Take `σ(x, y) = (y, x)`. Then
    `σφσ(x, y) = σφ(y, x) = σ(x, Ax − y) = (Ax − y, x) = φ⁻¹(x, y)`, re-derived here and agreeing
    with MR★ S-L3.
    - A configuration-sector record event `A = {u|_X = r}` has
      `σ(A) = {u_prev|_X = r} = φ(A)`, so `m = 1`.
    - So the law this conditioning retrodicts at `−t` is the mirror image, under `σ`, of the law
      it predicts at `t + 1`.
  - *Consequence, scoped to the lemma's hypotheses.* The lemma needs two things:
    - time-reversal invariance (`σφσ = φ⁻¹` with `σ` measure-preserving), a property of K1 and a
      posit in general;
    - a mirror-compatible event (`σ(A) = φ^m(A)`). On K1, configuration-only events are one
      such class. It is sufficient, not a characterization.
      Events that constrain both slices differently, and history events, are excluded.

    For such events, conditioning on a present record retrodicts at `−t` the mirror of what it
    predicts at `t + m`. So it cannot by itself make the record more reliable as a record of the
    past than as a predictor of the future, and reliability then needs past boundary data: (4a),
    or conditioning on an actual past history the observer still holds.
  - *Not covered.* Records that are reliable by a dynamical identity rather than by conditioning,
    and events outside the lemma's hypotheses.
  - *Not proved here.* The general statement, that reversible dynamics with a time-symmetric
    measure cannot give record reliability without asymmetric boundary data, is the Loschmidt
    point. It is not proved here. #1112's verification (c.6643840329) gives the related
    stationarity argument: under Lemma 3's uniform invariant measure the visible process is
    stationary, so its block entropies and `M_k` are invariant under time reversal.
  - This is the standard reversibility point (Loschmidt, Boltzmann), here written in OI's terms
    and scoped to the hypotheses above. The Albert–Loewer account of the records asymmetry is
    known here only from secondary sources (§3.8 item 4) and is not used.
- **Verdict Q-b: partly.**
  - **Conditioning on the observer's own visible data** is Main's predictive construction: CR_rec,
    a construction step (D-OB7). It establishes no physical mechanism that selects the law or
    generates a preparation.
  - **Reading it as a preparation law** is H-PREP, which is open.
  - **A rule for stipulated non-record events** is not supplied (CR_slice, b-new).
  - **The present record** is supplied.
  - **Retained records** are open, and on K1 they are tied to the unsourced ready region (MR★ C-3,
    C-4).
  - **Record reliability.** For time-reversal-invariant dynamics and mirror-compatible events,
    slice conditioning does not supply it (Lemma Q-b2). It then needs (4a).

**Q-c, physics: does OI explain how an observer creates or selects the preparation?**

- To create a preparation, a choice made by the observer must change the system's state. That is
  a selectable interaction (O-SET, DEFINITION-OPEN).
- On K1, settings enter only as additive offsets (Lemma D, identity part). Whether offsets count
  is the open premise D-SEL.
- Conditioning on records selects among histories after the fact. It does not create anything.
- This says nothing about whether localized records are possible on K1 (§3.6).
- **Verdict Q-c: no.** OI does not explain it. It is open in general and, on K1, obstructed
  conditionally on D-SEL.

#### 4.6.3 Conclusion on (4b)

**What reduces, conditionally.** For forward predictions, a laboratory preparation law reduces to
conditioning Main's stated measure (Q8, with H-OC_orb) on the observer's own accessible records,
by CR_rec: the present-value conditional and the in-realization history posterior that Main
defines (Main:88, :99, :105). The reduction needs every one of these:

- **(α) Correlation.** The prepared system is one the dynamics has correlated with the records. By
  Lemma Q-b1, present-record conditioning alone prepares nothing outside the cut.
- **(β) Retained records.** The observer holds retained records at `t_0`.
  - O-RET, O-REC and O-ACC are open.
  - On K1, retention is not excluded (MR★ C-2, C-4). It is, however, tied to the unsourced quiet,
    ready region (MR★ C-3, :1342–1371; C-4, :1373–1380), and #914 row 1′ forbids assuming a
    record that supplies readiness (Z1).
  - So this route has not been shown to be non-circular against O-RDY.
- **(γ) Reliability.** The records are reliable as records of the past.
  - Take time-reversal-invariant dynamics and mirror-compatible record events (`σ(A) = φ^m(A)`;
    on K1, e.g. configuration-only events). Slice conditioning does not supply reliability there
    (Lemma Q-b2), so it rests on past boundary data, which is (4a).
  - Records reliable by a dynamical identity, events that constrain both slices, and history
    events are not covered.
  - The general Loschmidt statement is not proved here.
- **(δ) H-PREP.** A laboratory preparation law is identified with that in-realization
  conditional. This hypothesis is open (§4.6.2 Q-b). Main:60 and ROF Q3(ii) treat structured
  preparations as realization data instead.
- **(ε) D-OB7.** The owner accepted the classification of CR_rec as (b-stated, construction
  step) (#866 c.6649267203). This settles a classification, not a mechanism.

**What remains.** Creating preparations (Q-c) is not explained. It needs selectable interactions
(O-SET).

**Answer to the owner's question, conditional.** *If* (α), (β) and (δ) hold, with (ε) settled by
D-OB7 and (γ) within its scope, then laboratory preparations need no observer-specific assumption of their own beyond
CR_rec. Their independent input is the time-asymmetric past boundary data of (4a), the input #1112
examines, together with O-REC (tied on K1 to O-RDY) for the records and O-SET for creating the
preparation.

None of (α)–(δ) is established here. (ε) is an owner classification decision:

- (α) restricts which systems can be prepared at all: by Lemma Q-b1, only systems the dynamics
  has correlated with retained records. It is not established for any laboratory system.
- (β) is open and not shown non-circular against O-RDY.
- (δ) H-PREP is an open hypothesis (D-OB8).
- (γ) holds only within Lemma Q-b2's scope.
- (ε) settles a classification only (D-OB7).

The owner's decision records that retained records, reliability, readiness and selectable
interactions remain independent, unresolved requirements. It also says the conditional reduction
is not to be treated as a derivation or as a proof of minimality (#866 c.6649267203).

CR_slice (b-new) is needed only if a preparation is stipulated beyond the observer's records.

**Skepticism (§A.31), applied to this favourable reduction.**

- The reduction is about predictions given records the observer holds. It does not derive the
  records, their reliability, or the act of preparing.
- It moves the burden onto (4a), O-REC and O-RDY, and O-SET. It does not remove it.
- It is a reduction, not a derivation of laboratory preparations from OI's premises.
- Gem test: ELABORATING.
  - Lemmas Q-a2, Q-b1 and Q-b2 restate standard statistical-mechanics points in OI's terms, under
    stated hypotheses.
  - They expose (β) and (γ) as the places where assumptions enter, and (δ) as an identification
    that had been implicit.

#### 4.6.4 The four groups, updated

| Group | Content | Classification |
| --- | --- | --- |
| (1) | Orbit-level conditioning of the reference measure on records (H-OC_orb) | b-stated: Main:62, :726 (iv); ch01:85 |
| (2a) | CR_rec: the present-value conditional (Main:88, :105) and the in-realization history posterior (Main:99) | (b-stated, construction step); **accepted in D-OB7**. It establishes no mechanism |
| (2b) | CR_slice: conditioning on stipulated events beyond the observer's records | b-new |
| (3) | Preparation events or laws admitted as starting data | b-stated category: Main:60, :524; ch01:85; ch04:170 |
| (4a) | The content of cosmic initial data | Gauge freedom is identified for structural data only: deep-sector cardinality (GR:142) and `φ`'s representative (ch19:210). None is identified for the initial configuration (ch19:200, uninvestigated). Theorem hypotheses (SM:48, :124; GR:799) and stated commitments (ch04:30, :32; ch18:214) enter. Isotropy (ch19:198) is speculative. The microstate is unexplained. **No generating principle is identified.** #1112 is the accountable home |
| (4b) | The content of laboratory preparations | Conditionally reduces to (2a), via the open identification H-PREP, plus retained records (open, tied on K1 to O-RDY) and (4a) for record reliability (Lemma Q-b2's scope). Creating a preparation (Q-c) is unexplained (O-SET) |

**Which assumptions prevent OI from deriving its own observer and measurement structures, after
the split.** Scoped to the sources read:

1. **The audited arrow accounts retain supplied inputs.** RECOVERY §§B.2–B.7 and
   M/Substratum:405–409 distinguish the expanding-background/matter assumptions, the low-entropy
   or product boundary condition, and the preparation root/orientation convention. Their
   common alignment is open; the conditional, time-symmetric selection result does not source
   these inputs (RECOVERY §§B.9, C.3 and D). Within Lemma Q-b2's stated scope
   (time-reversal-invariant dynamics, mirror-compatible record events), conditioning alone
   does not select the direction of a reliable record. This does not prove that every possible
   preparation requires each cosmological input above. #1112 is the accountable home.
2. **Retained, readable records are not sourced.** O-RET, O-REC and O-ACC are open. On K1 they are
   not excluded (MR★ C-2, C-4), but they are tied to the unsourced quiet, ready region (MR★ C-3;
   O-RDY). The CR_rec route has not been shown to be non-circular against O-RDY.
3. **Creating preparations needs selectable interactions** (O-SET, open). On K1, the native
   linear rule obstructs two things for every `(Obs, μ)`:
   - selectable interactions, conditional on D-SEL;
   - interference destruction by marking (S-L5, as reworded by C-9). S-L5 is PD in a frozen
     record, not among the lemmas MR★:1297–1300 reports as verified, and not independently
     reviewed here.

   Under S-L4, no confined pattern persists over `2w + 2` consecutive slices. Its review is
   reported in the frozen record (MR★:1297–1300) but not re-verified here. Its hypotheses are
   `ℤ^d`, or a torus with `N ≥ 5w + 2`, and `a` injective.

   None of this shows that localized records are impossible on K1 (§3.6; MR★ C-2). This is a
   dynamical assumption (Substratum A5, b-stated), not an interface one.
4. **The measure itself is posited, not derived** (Q8 with H-OC_orb, finite total `S`).
5. **No result selects the observer's cut.** C1–C4 and Main §4.6 only restrict it. The product form
   is an idealization, and the readout slice is a construction step.

## 5. Owner decisions needed

1. **D-OB1, how O-OBSMU is stated.**
   - (a) Split it by consumer:
     - U1–U3 are non-consumers;
     - R1 is support-invariant, pending review;
     - R4 needs nothing beyond Main;
     - L1 and L2 carry Q8;
     - R2, R3, L3, L4 and L5 stay open.
   - (b) Keep it as one open item.
   - (c) Carry it as a named condition `[C: Q8, Q9]` everywhere.
2. **D-OB2, the entry point for O-RDY.**
   - (a) The named-prior option, as #914 already allows.
   - (b) Conditioned patches or cross-time routes, per #914 row 1′.
   - (c) First commission a search for a group-(4) principle, one that generates preparation
     content.
3. **D-OB3, the measure.**
   - (a) Keep Q8 and H-OC_orb as stated, with finite total `S` as a branch premise.
   - (b) Commission a selection argument for Haar measure on compact completions.
   - (c) Ask whether CR_slice (group (2b), b-new) should be proposed, with its own §A.29 case. It
     fails control (i) as worded (§4.3).
4. **D-OB4, the arrow of time.** This is tracked as #1112 (ARROW-1). This note records the
   cross-document finding only (S.2.5) and edits no manuscript.
5. **D-OB5, P-R and P-SDC.** Record them unadopted, decline them, or ask for hard-to-vary
   versions. A screen of P-SDC, whether on paper or by computation, is outside the present
   authorization.
6. **D-OB6, review** of Theorem SI, CC-1, CC-2, Proposition G, the §3.4 closedness argument,
   Lemma P-1, Proposition C and Lemma D at the revised head, and of §4.6's Lemmas Q-a1, Q-a2,
   Q-b1 and Q-b2.
7. **D-OB7: decided.** amaybaum, Claude Code session chat, 2026-11-05 (#866 c.6649267203):
   "**D-OB7:** Accept the narrowed classification. Conditioning on the observer's present visible
   value, and computing an in-realization history posterior given an initial law, are existing
   construction steps in Main. This does not establish a physical mechanism that selects the
   probability law or generates a laboratory preparation."
   - CR_rec is recorded as (b-stated, construction step).
   - CR_slice on stipulated events remains b-new.
8. **D-OB8: decided.** amaybaum, Claude Code session chat, 2026-11-05 (#866 c.6649267203):
   "**D-OB8:** Record H-PREP as an explicit open hypothesis: identifying a laboratory preparation
   with conditioning on the observer's own records within an existing realization. Retained
   records, reliability, readiness and selectable interactions remain independent unresolved
   requirements. Do not treat the conditional reduction as a derivation or a proof of
   minimality."
   - H-PREP is recorded as an explicit open hypothesis (§4.6.2).
   - The four requirements stay open. §4.6.3's reduction is conditional, and it is neither a
     derivation nor a minimality result.

## 6. Review packet (revised head)

1. **§1 table:** the U1 description; the R2 and R3 verdicts; the L1 and L2 wording.
2. **CC-2:**
   - the bijection and its inverse;
   - an order-1 gap iff `q ≠ ½`;
   - divisibility on `{0, 1, 2}` iff `q = ½`;
   - full support for every `q ∈ (0, 1)`.
3. **The proofs, which are now complete in this note:**
   - Proposition G, including its product-form paragraph;
   - the §3.4 closedness argument;
   - Lemma P-1;
   - Proposition C, with the definitions of `Ψ_k`, `I_k`, `K_{k+1}`, `π̂` and `K′_{k+1}`.
4. **Theorem SI:** the root-dependent form; the kernel citations (`RecurrenceHorizon.lean:119`,
   `CausalReadback.lean:54`); ELABORATING against Main:141.
5. **§3.5:** the full-support restriction and the null-root convention.
6. **S.2.3–S.2.5:**
   - Appendix A matches Main:746–760 at `D`.
   - Main:756's sentence is attributed to the anti-Boltzmann-brain corollary.
   - H-OC_orb is b-stated (Main:62, :726 (iv), ch01:85).
   - CR_slice is b-new.
   - The Main↔ch18 verdict is limited to that pair.
   - The arrow-of-time finding points to #1112 and quotes its passages accurately.
7. **Lemma D:** D-SEL and S-L4 carried as premises; the scope is K1; Lemma D and S-L4 appear in
   the "Conditional" column of §2.
8. **§4.1:** the Q-table labels, and the four groups kept separate:
   - (1) b-stated;
   - (2) b-new;
   - (3) a b-stated category;
   - (4) none identified.
9. **§4.2:**
   - the two routes, (i) datum and (ii) conditioning;
   - the partial disagreement with the second review's formulation;
   - the list of blocking assumptions.
10. **§4.3–§4.4:**
    - the evaluation of P-R's control (i);
    - "no independent consequence identified";
    - SM:112.
11. **§7:** each reference, individually.
12. **§4.6.1:** each quotation and its class (gauge, physical input, unexplained), and the
    near-misses at ch19:198 and :200.
13. **§4.6.2:**
    - Lemma Q-a2 (slice and orbit conditionals agree on the record event);
    - Lemma Q-b1 (equal-time blindness);
    - Lemma Q-b2 (mirror), including the K1 instance `σ(A) = φ(A)` and `σφσ = φ⁻¹`;
    - the CR_rec refinement against Main:88, :99, :105;
    - that Q-a, Q-b and Q-c each have their own verdict.
14. **K1 scope:** every K1 sentence about records says only that confined patterns are excluded
    (S-L4, review reported in MR★:1297–1300 and not re-verified here), not that localized records
    are impossible (§2, §3.6, §4.6.4, README; MR★ C-2).
15. **This revision:**
    - D-OB7 marked pending at every site, then updated to the owner's decision;
    - CR_rec narrowed;
    - H-PREP named;
    - Lemma Q-b2's scope carried into (γ), §4.6.3 and §4.6.4;
    - the O-RDY dependence (MR★ C-3, C-4; Z1);
    - the conditional answer;
    - (4a) gauge freedom limited to structural data;
    - the Haar positivity scope;
    - `A ≠ ∅` in Q-a1;
    - S-L5's status;
    - the MR★ C-2, C-4, C-9, C-10 and C-11 locators, with C-10 attributed to S-C4a and C-11 to
      S-L4.
16. **Wording corrections after c.6644302632:**
    - item 1's attribution and its §7 row;
    - the C-10 and C-11 attribution;
    - (α) in the conditional answer;
    - "e.g. configuration-only events";
    - MR★:1297–1300;
    - c.6555028014 for S-L5;
    - the D-OB7 and D-OB8 records in §5.

## 7. Off-`main` and non-record references (§A.42 item 8)

Each reference was classified by reading the claim it is attached to.

| Reference | Used where | Classification |
| --- | --- | --- |
| #866 c.6642599988, c.6643204362, c.6643530298 | authorization; owner acceptance of the second review | governance records. They establish no claim |
| #1110 c.6643202940, c.6643501421, c.6643749363 (model-authored reviews) | the status line; §4.6's origin | provenance. They do not verify any result here (§A.46 item 7) |
| #866 c.6643823627 (owner decision: bounded extension) | §4.6 | governance record, quoted in §4.6 |
| Branch commits `1a796918`, `9a34c823`, `cd15123b` (earlier heads of this record, off `main`) | the status line | provenance. This head is self-contained |
| #1112 c.6643691865 (ARROW-1 analysis) and c.6643840329 (its model-authored verification) | §4.6.4 item 1; the #1112 bullet of §4.6.1 | **Support on `main` for the narrowed claim:** RECOVERY §§B.2–B.9, C.1–C.6 and D at `M`, and M/Substratum:401–409, supply the conditional/time-symmetric selection, named background/preparation inputs and open-alignment account stated at those sites. This replaces reliance on the comments; their whole-corpus search and complete verdict are not adopted. A README link alone is not support. The precise earlier gap is closed by this narrowing and substantive main support; #1112 remains accountable for the open arrow question |
| #866 c.6707972400 | current-source reconciliation and bounded writer handover | governance/provenance. Owner, this Codex conversation, 2026-11-07: "Proceed as suggested", accepting #1110's source repair and independent review; no physical premise or merge adopted |
| #1112 c.6643840329, the stationarity argument | §4.6.2 Q-b2, "Not proved here" | provenance. It is cited for context only, and no claim here relies on it |
| #1110 c.6644159894 (model-authored review of `478451b5`) | the status line | provenance |
| Branch commit `478451b5` | the status line | provenance |
| #866 c.6600176951 (quoting ROADMAP at `9613b21c`) | §1, the wording of the obligation | provenance. The quoted text is on `main` in `verification/ROADMAP.md` |
| #866 c.6567167742 (the foils) | D-SEL, P-SDC | provenance. The foil list is carried as a named premise (D-SEL); no claim here is supported by it |
| #866 c.6526292899 (controlled lift) | — | replaced by MR-pre:115 (N7), which is on `main` |
| #914 c.6563412926 (rows O-ACC, O-RDY, O-SET, 1′, 3′; C-10) | status labels; S.2.6; §4.2 item 3 | planning record, used for status labels and recorded routes. No mathematical claim here rests on it |
| #914 C-10 (MAP §4, off `main`) | §3.7 | provenance. Proposition C is proved here without it |
| #1007 c.6526897139 | S.2.2, Q8 | governance record. Quoted: "The *principle* is adopted; its infinite-carrier physical adequacy is **not proved**. Finite total-S remains a conditional branch premise where already consumed by recurrence/gauge/reconstruction theorems." (amaybaum, 2026-10-30T15:44:46Z). That Q8 needs finite `S` follows mathematically, independently of the record |
| #1007 c.6527637527, #1017 | — | provenance only. Replaced by the three-state example in Q4 (PD-here) |
| #1009, #1032, #1025, #1112 | status labels (O-SET, O-RET, O-RDY); the arrow-of-time pointer | planning records. They support no claim |
| arXiv sources | §3.8 | external, classified there |

The README lists further #866 comments as reading context: c.6541293037, c.6541615446,
c.6548283392, c.6627392555, c.6631480154 and c.6641545083. They are provenance only, and no claim
here uses them.

No claim here rests on content that exists only off `main`. The proofs this note relies on are
stated in it.

## Appendix A — Main:746–760 at `D`, verbatim

The text below preserves `papers/Main.md` lines 746–760 at the historical snapshot `D`.
At `M`, the second corollary's title is "observer-selection rule, with its rate condition";
the statement, hypotheses and scope below are unchanged (RECOVERY §F.4). This appendix is a
historical quotation, not the current title or a derivation of preparation, measure or time direction.

```text
**Setup.** Let $V$ be a partition with hidden sector $B = S \setminus V$. Define the coupling-graph neighborhood $\Sigma_{\text{loc}}(V)$ as the subset of $S$ reached from $V$ by at most $\tau_S / \Delta t$ steps of $\varphi$, where $\Delta t$ is the update step. The exact Koopman operator of $\varphi$ — and of its restriction to any invariant subsystem — is a permutation operator: unitary, with modulus-one spectrum and exact recurrence. It has no dissipative gap; exponential mixing cannot hold for it. Mixing, where it holds, is a property of a *compression*: let $\mathcal{K}_\Sigma := P_\Sigma\, \mathcal{U}_\varphi\, P_\Sigma$ denote the coarse-grained effective channel on the observable algebra of a local region $\Sigma$. **Effective-mixing hypothesis (EM).** *The local effective channel $\mathcal{K}_{\Sigma_{\text{loc}}(V)}$ mixes, with mixing time $\tau_{\text{mix}}(\Sigma_{\text{loc}}(V))$ set by its (dissipative) spectral gap.* (EM) is an explicit physical hypothesis — motivated by local thermalization phenomenology, not derived from $\varphi$ — with the same status as the conditional-mixing curve of (C2).

**Theorem (structural observer selection — conditional on (EM)).** Under the effective-mixing hypothesis, for any partition $V$ of bounded coupling-graph diameter, the hidden-sector memory time of the coarse-grained description generated by iterating $\mathcal{K}_{\Sigma_{\text{loc}}(V)}$ obeys
$$
\tau_B(V) \leq \tau_{\text{mix}}(\Sigma_{\text{loc}}(V)) + O(\varepsilon),
$$
where $\varepsilon$ absorbs typical-set and finite-size corrections. In particular, if $\Sigma_{\text{loc}}(V)$ is in its local equilibrium macrostate in the sense of canonical typicality [31], $\tau_B(V)$ is bounded by the local thermal decorrelation time.

*Proof.* Correlations between a $V$-localized observable $f$ and a $B$-localized observable $g$ at time $t$ require information to propagate from $V$ to $B$ at time $0$ and back to influence the $V$-correlated component of $g$ at time $t$. By the bounded per-step range of $\varphi$ (its causal cone), this round trip stays within $\Sigma_{\text{loc}}(V)$ for $t \leq \tau_S$. In the description generated by iterating $\mathcal{K}_{\Sigma_{\text{loc}}}$ the $n$-step channel is $\mathcal{K}_{\Sigma_{\text{loc}}}^n$, and under (EM) its dissipative gap — which on an equilibrium macrostate sets the local thermal decorrelation rate — bounds the decay of such coarse-grained correlations exponentially at rate $1/\tau_{\text{mix}}$; canonical typicality [31] supplies the local-equilibrium *state*, not the temporal mixing, which is exactly what (EM) posits. Hence $\tau_B(V) \leq \tau_{\text{mix}}(\Sigma_{\text{loc}}) + O(\varepsilon)$. $\square$

**Corollary (anti-Boltzmann-brain).** A Boltzmann brain is by construction a local fluctuation within a neighborhood $\Sigma_{\text{loc}}$ that is itself in local thermal equilibrium — that is what "fluctuation from equilibrium" means. The exclusion is the conditional chain, in the coarse-grained description generated by iterating $\mathcal{K}_{\Sigma_{\text{BB}}}$ (Scope (ii)): (EM) together with $\tau_{\text{mix}}(\Sigma_{\text{BB}}) \ll \tau_S$ implies the candidate partition fails (C2-slow), and hence — by the fast-bath erasure lemma of §2.3, under its uniform-erosion hypothesis — has its order-$k$ readback gap suppressed as $e^{-(k-1)\tau_S/\tau_B}$ for every $k \geq 2$; that gap is what (C4), the condition the characterization actually requires, asserts. For a numeric illustration under a further generic-thermal estimate — (GT): the region's effective-channel correlation time is set by the thermal scale, $\sim \hbar/(k_B T_{\text{local}}) \cdot O(1)$, an estimate that fails for protected slow modes (conserved-quantity bottlenecks, activation barriers, glassy or critical slowing) — the bound is at most $\sim 10^{-12}$ s for temperatures warm enough to support structured matter. The illustration rides (GT); the exclusion itself rides only the chain. Any finite-information observer has $\tau_S$ bounded below by its own internal processing time — for biological or synthetic BBs of any currently-envisioned type, $\tau_S \gtrsim 10^{-6}$ s. The slow form (C2-slow), $\tau_S \ll \tau_B$, therefore fails by at least six orders of magnitude for any BB whose local environment satisfies (GT) — and because (EM) posits genuine mixing rather than mere speed, the record the persistence form (C2-structural) requires is degraded with it: records are scrambled before readback up to a residue suppressed exponentially in $\tau_S/\tau_{\text{mix}}$. The chain bounds the readback gap: by the fast-bath erasure lemma, the failure of (C2-slow) with uniform erosion bounds the order-$k$ gap by $\delta_0\, e^{-(k-1)\tau_S/\tau_B}$ for every $k \geq 2$ — Boltzmann-brain observers so described carry at most exponentially suppressed readback at those orders, and since they fail (C2-slow), within that description they are not observers in the sense of (C1)–(C4) with (C2) read in its timescale form; the fixed-basis quantum representation they trivially possess ($S \iff D \iff Q_{\mathrm{fb}}$) carries no discriminating content. The exclusion is structural, not measure-theoretic — it follows from the incompatibility of (C2-slow) with fast-mixing local equilibrium, not from arguments about the ratio of BBs to "ordinary" observers in an anthropic sample.

**Corollary (past-hypothesis replacement, with its rate condition).** The theorem above bounds $\tau_B(V)\le\tau_{\rm mix}(\Sigma_{\rm loc}(V))+O(\varepsilon)$, while (C2)-slow requires $\tau_S\ll\tau_B$; those do not compose. Contradicting (C2-slow) additionally requires $\tau_{\rm mix}\ll\tau_S$ — the condition the Boltzmann-brain corollary states explicitly. A slowly mixing equilibrium with $\tau_S\ll\tau_{\rm mix}$ is entirely compatible with $\tau_S\ll\tau_B\le\tau_{\rm mix}$, so the valid form is that a sufficiently fast-mixing equilibrium supports no observer satisfying (C2) in its timescale form (C2-slow); for (C2-structural) and (C4) it gives suppression, not exclusion (§2.3). This matters for the de Sitter route, where $\tau_{\rm thermal}\sim\hbar/(k_BT_{\rm GH})=2\pi/H$ is Hubble-order and hence enormously longer than laboratory $\tau_S$: a de Sitter thermal state does not erase observer memory on accessible timescales. Under $\tau_{\rm mix}\ll\tau_S$: For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies every local subsystem is also in its local equilibrium. By the theorem — under (EM) for each region's effective channel, in the coarse-grained description it generates — $\tau_B(V)$ is bounded by the local $\tau_{\text{mix}}$ for every bounded-diameter partition $V$. No bounded-diameter partition supports (C2-slow) in that description. That every relevant equilibrium region satisfies (EM) at the required rate is itself a physical hypothesis, to be established model by model; the theorem converts it into the selection rule and does not supply it. In that description, with (C2) read in its timescale form, the framework's observers therefore exist only in the non-equilibrium phase of $(S, \varphi)$. The low-entropy initial condition commonly imported as a "past hypothesis" to select observer-compatible configurations is replaced here, within that description, by a structural selection rule: observers exist where (C1)–(C4), with (C2) read as (C2-slow), are satisfiable, and (C1)–(C4), so read, are not satisfiable in the coarse-grained description of the equilibrium phase.

**Scope.** The theorem uses bounded coupling, finiteness of $S$, the canonical-typicality result [31], and the effective-mixing hypothesis (EM) — the last an additional conditional physical premise, established model by model; it does not follow from isotropy or bounded-coupling regularity. Three scope notes. (i) *Locality of $V$.* The theorem assumes $V$ has bounded coupling-graph diameter. Adversarially non-local partitions — cherry-picking distant subsystems that happen to be correlated — are excluded by that assumption; bounded coupling degree does not by itself bound the diameter of $V$, and the finite response time of a physical observer motivates the assumption. (ii) *Ergodicity.* The gap the argument needs belongs to the coarse-grained effective channel $\mathcal{K}_\Sigma$, not to $\varphi$ itself: the exact Koopman operator of a finite permutation has modulus-one spectrum and cannot mix, so no spectral gap on typical orbits of $\varphi$ is available or assumed. A gap for $\mathcal{K}_\Sigma$ is exactly the content of (EM) and does not follow from statistical isotropy or bounded-coupling regularity. The cycle structure of $\varphi$ does not settle (EM), which concerns the one-step compression: a single cycle does not make the exact compressions relax (below), and orbits of length at most $2$ do not prevent a gap (on four states with cells $\{0,1\}$, $\{2,3\}$, the transposition $(0\,2)$ gives $\mathcal{K}_\Sigma$ with eigenvalues $1$ and $0$). The exact linear rule of [SM §4.2], whose largest energy shell for $d\ge2$ splits into exponentially many cycles, is therefore not excluded by its cycle structure; whether it or the rounded bijection satisfies (EM) is open. The exact $n$-step compressions $P_\Sigma\, \mathcal{U}_\varphi^n\, P_\Sigma$ are compressions of a permutation, recur, and need not equal $\mathcal{K}_\Sigma^n$: for the cyclic shift on five states with a coarse variable marking one of them, they equal $\mathcal{K}_\Sigma$ for $1 \leq n \leq 4$ and the identity at $n = 5$, while $\mathcal{K}_\Sigma^n$ relaxes. The theorem and its two corollaries are therefore statements about the coarse-grained description generated by iterating $\mathcal{K}_\Sigma$; that these iterates govern the exact compressions over the accessible window is not established, and the corollaries do not assert that the exact visible law carries no accessible memory. (iii) *The cosmological realization.* The de Sitter horizon is thermal in the static-patch sense at Hawking temperature, but the globally expanding system is not in equilibrium with respect to any static-observer partition. The horizon's expansion sets $\tau_B \sim H^{-1}$ structurally, not thermally, which is the OI-native mechanism making human-timescale laboratory observation compatible with (C2).
```
