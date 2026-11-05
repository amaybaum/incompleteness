# K1-RDY: single-use readiness on one fixed K1 instance (decision-complete preregistration)

**Status.** Text for independent exact-text review (#1031 gate 2). Not frozen, not an `F` candidate. It authorizes no
execution, enumeration, Lean run, probe, commit, post or premise adoption. Freeze needs a separate owner authorization
(K-11), and execution a further one (#1031 gate 3).
- **Authority, in order:** owner decisions K-1 to K-18 and D-07(a) (#914 c.6566997020, binding verbatim); planning issue
  #1031; proposal K1-RDY r3 and its independent review (verdict ACCEPT, with both Confirmation nits applied here, §2 and
  §4). Provenance only: the O-ACC audit and P2-G record (both accepted), and RR-1 (#1025, STAGE-VOID, not reopened; no
  RR-1 token is used).
- **Anchors.** `Main:N`, `SM:N` = `papers/{Main,SM}.md` at `07d94f2c` (every cited line is unchanged at the drafting
  snapshot `02009693`). `MR★:N`, `MR-pre:N` = the MR-1 amendment and preregistration at `af1e9be2`. `RR:N` = RR-1's
  preregistration at `e02544d5`. TA, TD, MAP and P2 are working records cited by key as provenance (§A.42 item 2).

***

## 1. Question

**K1-Q.** At the fixed instance of §2, for each candidate prior in §3 and each branch, is the dependency region `E` of a
declared observer `V` sharply ready, that is, in `R_E = {0}` at `t_0` with conditional probability 1 given a
positive-mass event of a rule-fixed readout region `W`; and if so, is `V` non-blind to its carrier `Σ` under the
conditioned law, and under which named hypotheses?

Conditions, not further questions. **Single use** (K-15): readiness once, at `t_0`; renewal (Lemma R, MR-pre:177),
RR's "(c) reliably preparable" (RR:52–53) and a ready supply in `Res` (C-3) are not decided. **Sharp decides** (K-7):
weak readiness is reported in exact values and decides nothing; no TV threshold exists. **Ceiling** (K-5, K-16(b)): a
positive is at most `AVAILABLE[H-sel]`, the grade RR-AVAILABLE[H-sel] of #914 c.6558349705, with its named hypotheses;
SOURCED is not reachable (§5.4).

## 2. Instance and definitions (fixed before any declaration is evaluated)

- **Instance** (K-3, K-18(b)). `(d, N, q, a) = (1, 5, 2, 1)`: `Λ = ℤ/5`, `𝐑 = ℤ/2`, `S = 𝐑^Λ × 𝐑^Λ`, `|S| = 1024`,
  `φ(x, y) = (y, Ay − x)` with `(Ay)_i = y_{i−1} + y_{i+1}` (MR★:462–483). `x_i` is site `i`'s previous slice and `y_i`
  its current slice; `φ^{−1}(x, y) = (Ax − y, x)`. `Σ = {x_0, y_0}` (site 0, both slices). `V` = site 1, current slice:
  `V_t = y_1(t)`. `T = 1`. `t_0` is the first tick of the readout window `[t_0, t_0 + T]`. `V ∩ Σ = ∅` (K-14, D-19).
  `μ` is the joint law of the whole state at `t_0`, `Σ` included (MR-pre:137).
- **Region `E`** (K-9). Every cell outside `Σ` that enters `V_t` with a nonzero coefficient, as a linear function of the
  state at `t_0`, for some `0 ≤ t ≤ T`. It is not the backward cone. `E` is computed from `(V, Σ, T)`, `V`'s readout
  class and `φ` alone, and is first evaluated in §6, after the declarations of §3.
- **Ready set** (K-13). `R_E = {0}`. The ready event is `{E_{t_0} = 0}`.
- **Branches and readout regions.** Each candidate is evaluated in the branches below; `W` is fixed by rule, never by
  coordinates (review nit 1):
  - **B-pl** (prior level): `W` trivial, `t_u = t_0`.
  - **B-eq** (equal time): `t_u = t_0`, `W = W_eq :=` the site set of `V`, both slices (K-12(b)'s rule).
  - **B-ct** (cross time; owner decision O-1(b)): `t_u = t_0 − 1`, `W = W_eq`, i.e. `V`'s own site set by rule, read at
    `t_u`. `W`'s value is carried from `t_u` to `t_0` by retention outside the state. Reading `V`'s site at the earlier
    tick is conditional on H-ret and H-2s (declared) and never counts as native access. If the row is not positive, that
    result stands as issued; no other readout region is substituted. An in-state record is evaluated as equal-time readiness relative to its region (TA §3.1).
  - **Overlap rule.** At equal time a cell in both `E` and `W` is counted in `W`, reported, and its certification
    flagged tautological (TA §3.1(i)). At cross time `W`'s cells at `t_u` and `E`'s at `t_0` are distinct by tick.
- **Readiness.** *Sharp:* some `w` has `μ(W_{t_u} = w) > 0` and `μ(E_{t_0} = 0 | W_{t_u} = w) = 1` (in B-pl:
  `μ(E_{t_0} = 0) = 1`). *Weak:* for each positive-mass `w`, the exact value `r(w) = μ(E_{t_0} = 0 | W_{t_u} = w)` is
  reported beside `π_0(E_{t_0} = 0 | W_{t_u} = w)` and `q^{−|E|}`.
- **Non-blindness** `NB(ν)`. There exist `σ ≠ σ′` with `ν(s_Σ(t_0) = σ), ν(s_Σ(t_0) = σ′) > 0` such that the law under
  `ν` of `(V_{t_0}, …, V_{t_0+T})` given `s_Σ(t_0) = σ` differs from that given `σ′` (R1, MR-pre:162). Exact on finite `S`.
- **W-certified.** There is a fixed `f` with `1[E_{t_0} = 0] = f(W_{t_u})` at every configuration (`π_0` has full
  support; RR:47–51's test). If not, H-law is added to the row.
- **Access labels** (K-8, D-07(a)). Every read is declared, never native. A read of current-slice cells only is
  **H-cur (declared)**. A read that includes a previous-slice cell is **H-2s (declared)**, a named conditional
  hypothesis. Cross-time carriage is **H-ret** (outside the state), a named conditional hypothesis.
- **Ledger** (MR-pre:184–187; TA §2). `D(μ) = log|S| − H(μ) = D_KL(μ ‖ π_0)`. Equal-time bounds: B-pl sharp readiness
  needs `|E| log q ≤ D(μ)` (c1); B-eq sharp readiness on `w` of mass `p` needs `p·|E∖W| log q ≤ D(μ)` (c2, the chain rule
  with overlap cells counted in `W`). Cross-time readiness is not bounded by `D(μ)`; its ledger line names H-ret.

## 3. Candidate declarations (written before `E` is evaluated; no `E`, `R_E` or readiness symbol)

Every row carries H-cur (declared) for `V`. A declaration has a **rule part** (what fixes `W`, the event, its window,
`t_u` and any support restriction, with its listed inputs) and an **image statement** (its prediction for G2(b)).

**P0 — counting measure.** `μ = π_0` (Main:56; fork leg H-μ). Hypotheses: H-μ, the finite-`S` posit (Main:62).
Rule part: none. Image statement: no restriction (`supp π_0 = S`).

**P1 — invariance class** (K-4, K-17(a)). `𝓘` = all φ-invariant probability measures on `S`, i.e. the mixtures of the
uniform measures `u_c` on the cycles `c` of φ, `π_0` included (MR-pre:137–140, invariance leg; Main:56). No member is
selected or excluded, by NB or otherwise. P2's energy-shell measures (SM:294–296) are members and are not run
separately. Hypotheses: H-inv[K-17(a)]. Rule part: inputs `φ` only. Image statement: each member's support is
φ-invariant, so its image at `t_0` is itself.

**P3 — persistence selection** (K-6, K-12(b)). `μ_O = π_0(· | O)`. Rule part: `W = W_eq` (inputs: `V`);
`O` = "`W`'s configuration is identical at each tick of `[t_u − 2, t_u]`" (value-free; window `k = 2`), `t_u = t_0`
(constants fixed by K-12(b)). `O` conditions on configurations, never on records, and `W`'s persistence is never cited
as memory (Z2). Anchor: Main §4.6 under (EM), open for linear K1 (Main:760), and TA §5; Main:62 is motivation only and
is classified as H-sel (K-5). Hypotheses: H-sel, K-12(b)'s rule, (EM) with `τ_mix ≪ τ_S`, H-2s (declared) for B-eq's
read of `W`'s previous slice. Branches: B-eq, and B-pl as a starting-measure diagnostic
(owner decision O-2). Readiness obtained there by conditioning the measure is not evidence that OI physically generates
`μ_O`. The row keeps its ledger line. B-ct does not apply (`t_u = t_0`).
*Image statement at `t_0`* (derived from `O` and `φ` only). As functions of the state at `t_0`, `x(t−1) = Ax(t) − y(t)`
gives `y_1(t_0 − k)` for `k = 0, 1, 2, 3` as `y_1`, `x_1`, `x_0 + x_2 − y_1` and `x_1 + x_3 + x_4 − y_0 − y_2`. Since
`W(t) = (y_1(t − 1), y_1(t))`, `O` holds iff these four values are equal. Mod 2 that is
`Im_O = {x_1 + y_1 = 0, x_0 + x_2 = 0, x_3 + x_4 + y_0 + y_2 = 0}`, a subgroup of index 8, so `π_0(O) = 1/8` and
`D(μ_O) = 3 log 2` (TA (c5)).

**Not run.** P4 is ineligible: no source for its bias is named (K-4), and a bias toward `R_E` fails G2. Routes (ii)–(iv)
(MR★:1367–1368; #1007) are outside this unit.

## 4. Lemmas used (paper arguments; the blindness lemma and L-O(ii) were checked in the proposal's review, and L-O(i) restates r3's L-O(a) argument without the strict-form definition)

**Blindness lemma.** Let `μ` be φ-invariant as the joint law of the whole state, `V ∩ Σ = ∅`, `E` given by §2, and
`μ(E_{t_0} = 0) = 1`. Then `V_t = 0` μ-a.s. for every `t`, and `NB(μ)` fails. Not covered: non-invariant laws,
W-relative branches, weak readiness, `V ∩ Σ ≠ ∅`, and ready sets with more than one element. It is not extended beyond
these premises (K-14).

**Lemma L-O** (quantifiers fixed; review nit 2). Let `O` be an event on `W`'s cells over a window, transported to `t_0`,
`μ_O = π_0(· | O)`, and `w` of positive `μ_O`-mass.
- *(i) Sharp readiness, any event.* `μ_O` is sharply ready on `w` iff `O ∩ {W_{t_u} = w} ⊆ {E_{t_0} = 0}`. If, in
  addition, `π_0` is not sharply ready on `w`, then `O ∩ {W_{t_u} = w}` determines the nonconstant function
  `1[E_{t_0} = 0]`, which `{W_{t_u} = w}` alone does not.
- *(ii) Affine events, sharp or weak.* If `O` is a coset of a subgroup (equations on `W`'s window cells), then under
  `μ_O(· | W_{t_u} = w)` the variable `E_{t_0}` is uniform on a coset `C_O(w)` contained in the coset `C(w)` it fills under
  `π_0(· | W_{t_u} = w)`. Its law differs from `π_0`'s on the same `w` iff `C_O(w) ⊊ C(w)`, and then the class of
  `E_{t_0}` modulo the smaller subgroup is a nonconstant function that `O ∩ {W_{t_u} = w}` fixes.
- *Scope.* "Readiness beyond P0's is a dynamical determination of `E`" holds for sharp readiness (any event) and for
  affine events (any departure). It is not asserted for weak readiness from a non-affine event. Under K-16(b) the
  determination is recorded as H-sel content and is not voided by definition. P3's `O` is a subgroup (§3), so (ii)
  applies to it.

## 5. Decision procedure

**5.1 Order.** S0 (all controls of §6) first; then P0, P1, P3, each branch through G1–G7 in that order.

**5.2 Gates per row** (row = candidate, member where P1 applies, branch). Each gate passes, fails with the token named
in §5.4, or ends in UNDECIDED(Gk).
- **G1 Declaration.** The §3 block is complete and every symbol is mapped in §10; otherwise UNDECIDED(G1). In B-pl,
  `NB(μ)` is recorded and decides nothing; G4 issues the B-pl token, so BLIND requires sharp readiness (owner
  decision O-3). No prior or member is removed at G1, and `π_0` stays in K-17(a)'s class.
- **G2 Z1 audit** (K-16(b), tailoring form), on the rule part of each declaration and each support restriction.
  - *(a) Syntactic.* The rule part names neither `E`, `R_E` nor readiness, and names no cell of `E∖W` by coordinates.
    It conditions on no event that it describes as a record, a preparation or a copy of a prepared cell (MAP §3).
    The image statement is exempt: it is the prediction (b) tests.
  - *(b) Semantic, decidable.* **T1** (constructed using `E` or `(Σ, T)`) fires iff the rule part lists an input other
    than `V`, `φ`, `(d, N, q, a)` and constants fixed by an owner decision (for a §6 fixture, the scalar constants fixed in §6; a literal set of cells is never such a constant). Any set given by literal coordinates
    instead of as a function of those inputs counts as such an input. **T2** (unpredicted image constraint) fires iff the
    declaration states no image at `t_0`, or the image G2 computes from the rule and `φ` differs, as a subset of `S`,
    from the stated one. If neither fires, G2 computes, for each positive-mass `w`, the function of `E_{t_0}`'s cells
    that `Im ∩ {W_{t_u} = w}` fixes and `{W_{t_u} = w}` does not under `π_0`. If it is nonconstant, it is recorded as the
    row's H-sel content and H-sel joins the row's list.
  - A flag in (a) or (b) gives Z1-VOID, which supersedes every branch token of the candidate, including any already
    issued. In P1, a flag on a member's support restriction gives that member's rows Z1-VOID; the member stays in the
    class, and §5.3 applies. A flag on the class declaration voids the class.
- **G3 Ledger.** `D(μ)` is stated with its source, and the equal-time bound of §2 is written for the row.
- **G4 Readiness, exact first.** Sharp readiness is decided and every sharp `w` is listed. For each sharp `w`, `NB` is
  decided under `μ(· | W_{t_u} = w)` (in B-pl, under `μ`). Weak values are reported. An equal-time sharp positive that
  breaks its G3 bound voids the row. The ledger comparison precedes the `NB` decision, so VOID[row] takes precedence
  over BLIND. ABSENT (no sharp `w`) excludes both.
- **Operational-usefulness report** (owner decision O-3; reporting only, not a filter). Every positive row also reports
  whether its prepared or conditioned ensemble permits distinguishable carrier-dependent records. Concretely, it lists
  which pairs of positive carrier values `σ, σ′` give `V`-readout laws with disjoint supports, and which differ in law
  only. The report never changes membership in K-17(a)'s class or any token.
- **G5 Hypotheses.** The row's list `Λ` is written: the declaration's hypotheses, the access labels of §2 for `V` and
  `W`, H-ret in B-ct, H-law if not W-certified, and H-sel if G2(b) recorded content.
- **G6 Skepticism** (§A.31), on every row that reaches a positive. A second derivation made independently and an
  adversarial note must give the same token, with G2(b) recomputed from the rule part alone. For enumerated rows (including P1 member rows), "independently" means
  a second, separately written enumeration that imports nothing from the first and matches it row by row. Disagreement
  gives UNDECIDED(G6).
- **G7 Token** from §5.4.

**5.3 P1 class rule** (K-17(a); no post-selection). Member rows are evaluated for `π_0` and for every cycle-uniform
`u_c`, in increasing order of each cycle's lexicographically least state, and every member row is reported. Per
branch, if any member row is not a positive, the class token is the first of VOID[row], Z1-VOID, UNDECIDED(Gk), ABSENT,
BLIND attained by a member row, scoped as "not every member of `𝓘`". If every member row is positive, the class
token is positive iff every nonempty union `C` of cycles admits a `w` with `∅ ≠ C ∩ {W_{t_u} = w} ⊆ {E_{t_0} = 0}`
at which `NB` holds under every weighting supported on `C`. It is ABSENT if some `C` admits no such `w`, BLIND if each `C`
admits one but `NB` fails there for some weighting, and UNDECIDED(G4) if this is not decided. In B-pl a member row is ABSENT
if the member is not sharply ready, and BLIND by the blindness lemma if it is.

**5.4 Token map (frozen; verdict text quotes tokens only).**

| Gate outcome | Token |
|---|---|
| Any S0 control fails or is undecided | VOID[stage]; no row token is issued |
| G1 incomplete or a symbol unmapped | UNDECIDED(G1) |
| G2(a) flag / G2(b) flag | Z1-VOID[IMPORTED] / Z1-VOID[DYN], for the candidate |
| G4: equal-time sharp positive breaks its G3 bound | VOID[row] |
| G4: no sharp `w` | ABSENT[μ; branch; access] |
| G4: sharp `w` exist, `NB` fails at each | BLIND[μ; branch; access] |
| Gk not decided on paper or by authorized enumeration | UNDECIDED(Gk) |
| G6 disagreement | UNDECIDED(G6) |
| G1–G6 pass, H-sel ∈ Λ | AVAILABLE[H-sel](Λ) |
| G1–G6 pass, H-sel ∉ Λ | CONDITIONAL[Λ] |

SOURCED would need a prior fixed by the fork rule with a reviewed necessity assessment, a native readout of `W` (R3,
MR-pre:165) and no H-sel. No declared read meets R3 (owner decision 4, W3, RR:57–59), so G7 never issues it here.
**Precedence.** VOID[stage] supersedes every token. Z1-VOID supersedes every branch token of its candidate, or of its
P1 member. Otherwise a row takes the token of the first gate that issues one; within G4, VOID[row] precedes BLIND.
`Λ` is compared as a set. A candidate's report is the tuple of its branch tokens; no aggregate verdict is formed.

**5.5 What execution consists of.** After separate owner authorization (#1031 gate 3), and only then:
(1) S0: the eleven controls of §6, each at its stated instance and in isolation on the gate it tests;
(2) rows: P0 (B-pl, B-eq, B-ct), P1 (the same three; member rows and the class rule), P3 (B-pl, B-eq);
(3) for each gate, a written derivation. Where that does not decide the gate, and only if the authorization covers it,
a labelled exact enumeration over the fixed instance's 1024 states (4096 for CC-IMP″), in integer and rational
arithmetic. That includes the cycle decomposition of φ for P1. Otherwise the gate ends UNDECIDED(Gk) (K-10).
Output: a gate-outcome table in a stated schema (candidate, member, branch, G1–G7 outcomes, sharp `w` list, weak values
as exact rationals, `NB` record, `Λ`, ledger line, token). Each token is computed from that table by §5.4, and any
enumeration reports through its exit status and a schema file (§A.44).

## 6. Controls (S0; any failure gives VOID[stage])

At the fixed instance, §2's rule gives `E = {x_1, y_1, y_2}`, `W_eq = {x_1, y_1}`. POS-X uses its own
fixture region `W_ct :=` `E`'s one-tick dependency set, `{y_0, y_1, y_2, y_3, x_1, x_2}` at `t_u = t_0 − 1`. No candidate
row uses it. Each control is decidable on paper at its instance. The hand check in §11
confirms the controls marked HC-1. CC-PASS's image is derived as P3's is (§3), with `k = 1`. CC-IMP″ keeps r3's
reviewed `N = 6` instance by choice, not by necessity: at `N = 5` a `k = 2` event on `W = {x_2, x_3, y_4}` fixes `y_1`.

| Id | Instance, fixture | Gate under test | Passes iff |
|---|---|---|---|
| CC-ABS | Fixed; `π_0`, B-eq form with `W = {x_3, y_3}` (disjoint from `E` and `Σ`) | G4 | ABSENT (TA (c4); HC-1: `r(w) = 1/8` for every `w`) |
| CC-EXACT | Fixed; `(1 − ε)μ_Q + επ_0`, `ε = 1/20`, `μ_Q` as in CC-IMP, B-pl | G4 | Sharp absent, weak value `153/160` recorded |
| CC-SCOPE | Fixed; `δ_0` (the fixed point `0`) | G4 | BLIND in B-pl, B-eq and B-ct |
| CC-LEDGER | Fixed; a row asserting B-pl sharp readiness under `π_0(· \| ℰ = 0)` (SM:296; HC-1: both shells have 512 states, `D = log 2`) | G3/G4 | VOID[row]: `3 log 2 > log 2` |
| CC-IMP | Fixed; `μ_Q` = `δ_0` on `E`'s cells ⊗ `π_0` elsewhere | G2, G3 | Z1-VOID[IMPORTED]; `D(μ_Q) = 3 log 2` |
| CC-IMP′ | Fixed; (a) `O′` = P3's `O` ∧ "`y_2(t_0) = 0`"; (b) `π_0(· \| x_3 = 0, x_1 = y_1 = x_3)` declared as "`W_eq` is a fan-out copy of ancilla `x_3` prepared in 0" | G2(a) | Both flagged |
| CC-IMP″ | `N = 6`, `q = 2`, `a = 1`; `W` = sites {0, 1}, both slices; `E` := site 2, both slices; `O` = "`W ≡ 0` over `[t_u − 1, t_u]`", `t_u = t_0`; no image stated | G2(a); T1; T2's no-image disjunct | G2(a) passes; T1 fires (literal coordinates); T2 fires (no image stated; `O` fixes `x_2(t_0) = 0`). Proposal r3's hand check: `P(E = 0 \| O) = 1/2` against `1/4` |
| CC-PASS | Fixed; `W = W_eq` by rule; `O₁` = "`W`'s configuration is identical at `t_u − 1` and `t_u`", `t_u = t_0`; stated image `{x_1 + y_1 = 0, x_0 + x_2 = 0}` | G2(b) (must pass) | Neither T1 nor T2 fires; H-sel content `x_1 + y_1` recorded in B-pl, none in B-eq |
| CC-T2 | Fixed; CC-PASS's rule with stated image `{x_1 + y_1 = 0}` | G2(b) T2 | T2 fires through its "differs" disjunct; T1 does not fire |
| POS-X | Fixed; `π_0`, cross time with `W = W_ct` | G3, G4, G7 | G3 does not void; sharp at `w = 0` (mass 1/64), `NB` holds (`V_{t_0+1} = y_0(t_0)` on the event), W-certified; `Λ` equal as a set to {H-μ, finite-`S` posit, H-ret, H-2s (declared), H-cur (declared)}, token CONDITIONAL[Λ] |
| CC-BLIND | Fixed; POS-X with `W_ct ∪ {y_4, x_0}` at `t_u` | G4 | Sharp at `w = 0` (mass 1/256), `NB` fails; BLIND |

## 7. Scope limits and non-claims

- One instance (K-18(b)), single use at `t_0` (K-15). No extrapolation to other tuples, all tori, `ℤ^d` with Haar
  measure, infinite `S` or OI⇔QM without a separate preregistration and proof.
- BLIND and ABSENT are scoped to (prior or member, branch, access, instance). No token states that a ready supply cannot
  exist (MR★:1503–1504). Class failure in P1 is scoped to `𝓘` (K-17(a)).
- A positive is not physical sourcing of a ready state, access, renewal, memory, observer emergence or complete QM.
  Every cross-time positive needs retention outside the state and stays held (O-RET).
- Readiness-dependent work is not reopened: #1023 stays read-only at its held head, and K★ is not reopened
  (MR★:895–898). C §6(b), A §5 and D's conditioned patches stay held until O-RDY is sourced, or until a branch is
  explicitly restricted to a CONDITIONAL row's model. A K1-RDY report lifts no hold.
- The holds on #1009, #1023, #1011, #1003 and #918 are unchanged. #1025 is untouched. No correctness band moves. No
  manuscript, Lean or probe change.

**Rows fixed in advance.** At this instance several tokens follow from the frozen rule before execution:
- P0's B-pl row, from `π_0`'s full support;
- P0's B-eq row, from TA (c4);
- P3's rows, from the image statement of §3 read against `E`;
- every P1 class token, as not positive, from §5.3 with `δ_0` as a member (CC-SCOPE); which non-positive token results depends on the other members.

These rows record the rule's consequences and are not independent tests. The informative content is the P1 member rows.
Verdict text is still generated only from the gate table.

## 8. Results preserved (used as controls; none reopened)

TA (c4), `π_0`'s equal-time independence of disjoint cells (CC-ABS). The budget identity I1/I2 (MR-pre:184–187) and the
bounds (c1)/(c2) (CC-LEDGER, CC-IMP). ℰ's conservation and shell count (SM:294–296; CC-LEDGER). The P1 lemma and the
blindness lemma (CC-SCOPE). MR-1's scoped GAP and C-3 (MR★:1342–1372, 1491–1504). RR-1's STAGE-VOID. D-07(a)'s
CONVENTION-H-2s (O-ACC's scope) and the P2-G corrigendum, as provenance only.

## 9. Invariants → checkpoints (§A.41)

| Invariant | Checkpoint |
|---|---|
| No execution before authorization | The execution log opens by quoting the #1031 gate-3 authorization with author and time. The drafting log lists reads and HC-1 only |
| Rule frozen before rows | The frozen file's blob id is compared by the reviewer with the file used |
| Prior declared before `E` | In the frozen file §3 precedes §6's evaluation of `E` and contains no `E`, `R_E` or readiness symbol (reviewer grep). The reviewer re-derives P3's image from `φ` alone. `E` at this instance already appears in the reviewed proposal (POS-X), so this checkpoint is documentary. The operative guard is G2(b)'s T1, decided from the listed inputs |
| No free parameter | Every symbol maps to a rule or decision in §10. The reviewer checks the map; an unmapped symbol gives UNDECIDED(G1) |
| Exact first | Every G4 row states sharp and weak separately, in exact rationals |
| Non-blindness on every positive | Every positive row carries its `NB` record under the conditioned law |
| Access never native | Each G5 list is checked against §2's labels and D-07(a) |
| Z1/Z2 | Every G2 row records (a), T1, T2 and the H-sel content. A grep of P3 rows for "memory" and "record" outside quoted rules returns nothing |
| Ledger on every positive | Each positive row has a ledger line (equal-time `D` share, or H-ret for B-ct) |
| Ceiling | The token column contains no SOURCED and no grade above AVAILABLE[H-sel] |
| No no-go | An added-lines grep for "no-go", "impossible", "cannot exist", BLIND and ABSENT; each hit is scoped as in §7 |
| Held heads unchanged | `gh api` GET of pulls 1009, 1023, 1011, 1003, 918 and 1025 at the start and end of execution. Heads must equal those recorded at freeze (at drafting: `d4a80fc8`, `af1e9be2`, `947761dd`, `0efd67a6`, `fa32b043`, `e02544d5`) |
| Verdict text generated from gate outcomes | The reviewer recomputes each token from the gate-outcome table by §5.4 and compares. Verdict prose quotes tokens only |
| Structured verdict (§A.44) | Tokens are read from the schema table and enumeration exit statuses, never from printed output |
| Controls green before tokens | S0 rows appear first with outcomes. Any failure gives VOID[stage] |
| Controls run in isolation | Each S0 row records the single gate it ran, and no other gate's output |
| Branch `W` fixed by rule | Each row records its `W`'s rule and inputs. The reviewer recomputes `W` from the rule and compares |
| Operational-usefulness report (O-3) | Every positive row carries the report. The reviewer checks that no token, and no P1 membership, cites it |
| No post-selection (K-17(a)) | Per branch, the P1 member rows are `π_0` plus one row per cycle found, and the cycle sizes sum to `\|S\|`. The reviewer checks both |

## 10. Free-parameter audit

- `d, N, q, a, V, Σ, T` (K-18(b)) · `t_0`: first tick of the readout window (§2) · `μ` at `t_0`, `Σ` included (MR-pre:137).
- `E`: dependency rule (K-9) · `R_E = {0}` (K-13) · `V ∩ Σ = ∅` (K-14) · single use at `t_0` (K-15).
- `W_eq`: `V`'s site set, both slices (K-12(b)'s rule) · B-ct: `W_eq` at `t_u = t_0 − 1` (O-1(b)) · P3's B-pl row, a
  starting-measure diagnostic (O-2) · G1's `NB` scope and the operational-usefulness report (O-3).
- P3: `O`, `k = 2`, `t_u = t_0` (K-12(b)); value-free, configurations only (K-6); H-sel (K-5).
- P1's class `𝓘` with `π_0`, member order and class rule (K-17(a); §5.3, §11 Q4) · P0: `π_0` (Main:56) · P2 inside P1,
  P4 ineligible (K-4).
- Sharp decides, weak reported, no threshold (K-7) · `NB`: definition, no threshold · G2(b): tailoring with T1/T2 (K-16(b)).
- Access labels (K-8, D-07(a); §11 Q3) · overlap rule (§2) · token map and precedence (§5.3–§5.4).
- Control fixtures: `ε = 1/20`; CC-ABS's `W`; CC-LEDGER's shell `ℰ = 0`; CC-IMP′'s ancilla `x_3`; CC-IMP″'s instance and
  `E := site 2`; POS-X's `W_ct`; CC-BLIND's `{y_4, x_0}`; CC-PASS's and CC-T2's `O₁`, `k = 1` and stated images (§6).

## 11. Owner decisions and drafting resolutions

**Decided** (owner decision, 2026-11-02, Issue #1031 thread).
- **O-1: (b).** B-ct reads `W_eq` at `t_u = t_0 − 1`, conditional on H-ret and H-2s (declared), and never as native
  access. A row that is not positive stands as issued (§2).
- **O-2: keep.** P3's B-pl row is kept as a starting-measure diagnostic with its ledger line (§3).
- **O-3: confirmed.** `NB` is recorded at G1 and decides nothing there. B-pl tokens come from G4, and `π_0` stays in
  K-17(a)'s class (§5.2). The operational-usefulness report is a reporting item, not a filter.

**Drafting resolutions** (reviewed as within the decisions).
- **Q3 (previous-slice reads).** `W_eq` and `W_ct` contain previous-slice cells, so their reads add H-2s (declared), a
  named conditional hypothesis under K-8.
- **Q4 (P1 over mixtures).** The extreme-member evaluation, the union-of-cycles condition and the precedence (§5.3).
- **Q5.** Weak values are reported against two references. (c2) uses `|E∖W|`, as the overlap rule implies. G2(a)
  exempts the image statement.
- B-eq's `W_eq` reuses K-12(b)'s rule (input `V`).

**Drafting checks.** HC-1: one labelled `python3 -I` stdin call, 1024 states, no files, for control well-posedness only.
At the fixed instance it gave:
- `E = {x_1, y_1, y_2}`;
- `NB(π_0)` and `NB(δ_0)` false;
- POS-X: mass 16/1024, sharp, `NB` true, W-certified;
- CC-BLIND: mass 4/1024, sharp, `NB` false;
- CC-ABS: `r(w) = 32/256` for all four `w`;
- ℰ conserved, shells 512/512.

No candidate row was evaluated. P3's image and CC-PASS's image are paper derivations; the independent review confirmed
both by enumeration. No check was run in this revision.

***

## 12. Round K1-RDY-1: base, standing, precedence and declarations

**Base.** Lines 1–313 of this file are the K1-RDY preregistration accepted on 2026-11-02, reproduced byte for byte. No
line of them is edited. Check (`AGENTS.md` §A.42 item 1), at any commit that holds this file:
`head -n 313 verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/preregistration.md | sha256sum` prints
`a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`. Provenance: the text was posted as #1031 comment
6567522034 and recovered on PR #1114 (owner, #1031 comment 6650824861: "Recovery").

**Standing.** Lines 3–5 record the base's standing on 2026-11-02: "Not frozen, not an `F` candidate. It authorizes no
execution, enumeration, Lean run, probe, commit, post or premise adoption." For this round that standing is historical.
At the commit `F` that the owner designates, lines 1–313, this section and the files under `amendments/` are the
round's preregistration, frozen under `AGENTS.md` §A.39; the designation is K-11's separate authorization. Execution
needs the further authorization of lines 5, 186 and 252 (#1031 gate 3), which names the exact tools, inputs and scope of
any execution, and which the execution log quotes with author and time (line 252).

**Precedence.** Each file under `amendments/` names the base lines and clauses it governs. For those, the amendment
governs; everywhere else lines 1–313 govern. An amendment changes no gate, token, control or decision except as it
states. Where two amendments touch one line, each governs only the clause it names.

**Owner record in force** (`AGENTS.md` §A.42 item 7). amaybaum, #1031 comment 6651204512, 2026-11-05T06:15:48Z:

> **Ratification: prospective ratification approved.**
> - K-1 through K-18, D-07(a), O-1(b), O-2 KEEP and O-3 CONFIRM are adopted as the specified K1-RDY-1 decisions, **prospectively from this dated owner record**.
> - The original coordinating-session decisions are not retroactively attributed to the owner; their actual provenance is preserved.
> - Interpretations that depend on a proof remain conditional until those proofs pass review.
> - **D-07(a):** the narrower labelling rule. Previous-slice access requires a derived readout or retention mechanism; H-2s remains declared.
> - **O-3:** distinguishability is evaluated through the declared visible readout over the stated finite window. It is not evidence of native access.

From the same record:

> **A4: option (a), with a material-change safeguard.** A mismatch in a referenced historical PR head is recorded, not automatically classified as `VOID[stage]`. If it alters an actual scientific dependency or a frozen input, the affected work stops and is reconciled before proceeding. No silent substitution.
>
> **Enumeration before `F`: not authorized.** No scientific enumeration, model computation or native run. The round may use the existing reviewed paper controls and the permitted static checks. Any later execution needs a separate authorization naming the exact tools, inputs and scope.

The text of each adopted decision, and of the documented owner decisions the base cites, is quoted in
`amendments/A1-attribution.md`.

amaybaum, Claude Code session chat, 2026-11-05, recorded in PR #1114 comment 6653656756 (2026-11-05T08:44:44Z):

> 1\. K1-RDY: Approve OD-1 to OD-7 as recommended. Preserve the 313 recovered lines and all scientific limitations. No additional execution or theorem promotion is authorized beyond the approved decisions.

The decisions approved there that this control plane carries: OD-3, the union clause of lines 159–162 kept with A8's
scope statement; OD-4, paper-only execution (below); OD-5, A2; OD-6, A9. OD-1 and OD-2 are the landings of the
support below.

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6655647525 (2026-11-05T10:27:34Z):

> ### 5. K1-RDY — Drafting approved
> Authorize starting the next K1-RDY round draft from a fresh base `D`, following the accepted preregistration and previously approved OD-1 through OD-7 decisions. Preserve the protected 313-line text and its recorded hash. Drafting only. Designation of `F`, freeze, workflow dispatch and scientific execution each require separate approval.

**Support on `main`.** The lemmas of lines 95–114 and 244:
`verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/LEMMAS.md` (A5), with the record of its
independent review, `REVIEW.md` in the same directory. The items that file leaves unproved:
`verification/programmes/oi-qm/reconstruction/k1-rdy-pref-proofs-20261105/PROOFS.md` (A3, A6, A8), with the record of
its independent review, `REVIEW.md` in the same directory. Both directories are cited at
`4b4b437cfff9dcf32c882251d1a4c3445ca9e8be`, this round's `D`: `LEMMAS.md` entered `main` with the merge
`4f016afd943f5a3939493eab752664949e90dbbb` (#1119); its review record and status lines, `PROOFS.md` and its review
record entered with the merge `4b4b437c` (#1122). Both reviews are model-authored and read-only. The trace of every
other reference is A7.

**Governed paths.** Execution is paper-only (OD-4): its output is the round's record, `result.md` and the gate table
of A9. The governed paths are the round's record directory and its receipt and nothing else, which is the checkpoint
for line 230's "No manuscript, Lean or probe change" (§A.41). No enumeration tool and no workflow path is declared, so
none can be used in execution: the set in force is the set at `F` (architecture `S7`). A gate that the paper
derivations do not decide ends in UNDECIDED(Gk) (line 191).

```v3-round
round K1-RDY-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/
record AM verification/receipts/K1-RDY-1.json
```
