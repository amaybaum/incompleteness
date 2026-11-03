# O-RET operational definitions (refinement under the owner's decisions on OQ-1 to OQ-8)

**Status.** WIP / UNVERIFIED. This is a paper-only refinement for #1032 under PO-1102 workstream B, revised after independent review of 7aaf9f97; this revision has not been re-reviewed.

- **Authority.** The owner decisions recorded verbatim at #1032 c.6611966162 (chat, 2026-11-03), on the reviewed checkpoint 3 of PR #1078 at `b9000ae2410a554ef54616bcfe85d5707f4a307f`, which is unmerged.
- **Scope of this document.** It fixes the criteria and the metric. It runs no computation, Lean or search, adopts no premise, and selects no candidate.
- **Proposals.** Proposals marked "awaiting independent review" are not adopted criteria. Placeholders marked
  `[OWNER TO SET]` have no value until the owner sets one.

The setting is that of ROUTES.md §0.1, which is kept unchanged:

- finite `S`;
- a time-homogeneous bijection `φ`;
- the joint law `μ = μ_Σ ⊗ ν` at the preparation tick `t₀`;
- a write tick `t₀ → t₀+1`;
- an H-cur (declared) readout.

A **declared preparation set** `P` is a finite set of carrier values `σ` with `μ_Σ(σ) > 0`, fixed before testing.
"Background held fixed" means the same `ν` for every `σ ∈ P`.

***

## D-RET: retention (OQ-2)

> Decision (verbatim): "do not adopt static cells as the definition. A record may persist in a fixed, physically
> readable function of changing cells. It must retain information acquired during the write, without being continually
> re-supplied by the passing carrier. Readouts that change with the tick remain admissible for investigation when their
> clock, identity and access mechanism are physically accounted for. The reviewer's screening condition needs
> independent review before adoption, including checks for information carried jointly by apparently independent
> inputs."

**Data fixed before any candidate is tested.**

- A register `A`: a declared set of cells, together with its readout `ρ_A`.
    - The readout is a function of `A`'s cells only, the same at every tick. Write `A_t` for `A`'s full cell content at
    `t`.
  - The values of `A`'s cells may change from tick to tick.
- A nonconstant carrier property `f : P → Z`.
- A deterministic decoder `g`.
- A retention window `W_T = {t₀+1, …, t₀+1+T}` with `T ≥ 1` (one-step retention: `T = 1`).
- The tolerance `ε*` of D-MET.

**Definition.** The register *retains `f` over `W_T` within `ε*`* iff (R-a) to (R-d) below all hold.

- **(R-a) Distinct register.**
  - `A`'s cells are disjoint from Σ's cells at `t₀`.
  - `ρ_A(s_{t₀}) ⫫ κ(s_{t₀})` under `μ`. This is automatic under the product law of §0.1.
- **(R-b) Acquired during the write.** The law of `g(ρ_A(s_{t₀}))` given `σ` is the same for every `σ ∈ P`. Any carrier
  dependence at `t₀+1` is therefore new transfer at the write tick, not information already held before it.
- **(R-c) Retained.** `ε_max(t) ≤ ε*` for every `t ∈ W_T`, where `ε_max` is the primary metric of D-MET.
- **(R-d) Not continually re-supplied.** At each hold tick `t → t+1` with `t, t+1 ∈ W_T`, `A`'s update must not draw
  carrier information from cells outside `A`.
  - This requirement is normative. Its operational test is **open**: proposals S-1 and J-1 below await independent
    review.
  - Until a test is adopted, a positive verdict under D-RET is provisional on whichever proposal it uses, and it says
    which one.

**Readouts that change with the tick.** A decoder `g_t` that depends on `t` is admissible only if all three hold:

- (i) `t` is supplied by a declared clock register `K` inside the model, whose cells, dynamics and preparation are
  entered in the resource table (D-SML);
- (ii) the identity of `A` across ticks is fixed by the rule, as a fixed declared region or a function of the state
  fixed by the rule; a schedule fixed in advance but not physically derived is countercontrol (d) and is not
  admissible;
- (iii) the read of `K` is declared under the same access baseline as `A` (D-ACC).

A decoder indexed by an external tick count that is not in the state is not admissible.

*Remark C (paper derivation, unreviewed).* Under (i) to (iii), `(ρ_A, ρ_K)` is a function of the state that is the
same at every tick, and `g'(ρ_A, ρ_K) := g_{ρ_K}(ρ_A)` is a fixed decoder. So for **exact** retention Lemma S′ of
ROUTES.md applies unchanged to readouts that change with the tick through an accounted clock. Approximate retention is not addressed by this remark. A clock that indicates `t − t₀` is prepared at a fixed phase, so
its support is not φ-invariant and Lemma S′ does not apply to it. The remark reduces accounted-clock readouts to fixed
decoders. It does not exclude them, and the clock's preparation restriction enters D-SML.

**Proposals awaiting independent review (not adopted).**

For each proposal, `B_t` is the set of cells outside `A` on which `A`'s values at `t+1` depend, as functions of the
state at `t` on the support of `μ_t`. It is computed from `φ`.

- **S-1, the reviewer's screening condition (proposed by the review, awaiting independent review).**
  - Statement: each cell of `B_t` has a value at `t` that is independent of the carrier.
  - The review's sorting: it admits `M_F` and the swapped pair, and rejects HC-K3, HC-K4, HC-P and K1 generally. That
    sorting is the review's claim and has not been checked independently here.
- **J-1, the check the owner asked for: information carried jointly by apparently independent inputs (proposed here,
  awaiting independent review).**
  - *Why a cell-by-cell test is not enough.* With `u` uniform and independent of a carrier bit `c`, the cells `u` and
    `u ⊕ c` are each independent of `c`, yet together they determine `c`. S-1 read cell by cell would pass them.
  - *Proposed J-1 at a hold tick `t`.*
    - (J-i) the **joint** vector `B_t` is independent of `κ`;
        - (J-ii) `κ ⫫ B_t | A_t`.
  - *Consequence of (J-ii), one direction.* `A_{t+1}` is a function of `(A_t, B_t)`. The chain
    `κ → A_t → (A_t, B_t) → A_{t+1}` is then Markov, so `I(κ; A_{t+1}) ≤ I(κ; A_t)` (data processing): the register's
    full content gains no carrier information at the hold tick. A readout of part of `A` can still gain information
    from `A`'s unread cells.
  - *Why both parts are needed (hand examples).*
    - (J-ii) alone admits HC-P. There `A = {u₂}` holds `c`, and `B = (u₁, u₀) = (c, 0)` at `t₀+1` is a function of
      `A`, so (J-ii) holds, but the value is re-supplied. (J-i) rejects it.
    - (J-i) alone admits a "share completion". Take `A = c ⊕ n` and `B = n`, with `n` uniform and independent. Then `B`
      is independent of `c`, yet the update `A′ = A ⊕ B = c` creates the record at the hold tick. (J-ii) rejects it.
  - *Checks on witnesses already in ROUTES.md.*
    - `M_F`: `B` is the arriving background channel cell, independent of `(κ, r)`, so J-1 holds.
    - The swapped pair: `B` is empty.
    - Neither check is a verdict, because J-1 is not adopted.
  - *Limitation (found in review).* S-1 and J-1 test re-supply from outside `A` only. They do not exclude advection
    inside a declared register: HC-P with `A = {u₁, u₂}` and `g = u₂` satisfies (R-a) to (R-c), S-1, J-1 and D-TRN's
    'left' over `W₁`, while the pulse passes through `A`. Requirement 2's rejection of simple advection within the
    register has no operational test yet.
- **Countercontrol (h), the duplicated passing pulse (HC-P of ROUTES.md; proposed by the review, awaiting independent
  review).** A candidate must not be counted as retention when its register value is re-supplied, over the hold tick,
  by a ready background's duplicate of the passing imprint.

***

## D-MET: metric (OQ-7)

> Decision (verbatim): "approximate retention is admissible. Use worst-case decoding error over the declared carrier
> preparations as the primary metric, for a fixed nonconstant carrier property and decoder chosen beforehand. Also
> report total-variation distinguishability between the preparation-conditioned register laws at each tick. Specify the
> retention window, failures and any conditioning explicitly. Choose the error tolerance from the intended record's
> requirements before further candidate testing; the toy model's ¼ error is a result, not an automatically accepted
> success threshold."

**Primary metric.** For each `t ∈ W_T`,
`ε_max(t) := max_{σ ∈ P} μ( g(ρ_A(s_t)) ≠ f(σ) | σ )`.

- `f`, `g` and `P` are fixed before testing.
- A decoder of a blind register has `ε_max ≥ 1 − 1/m`, where `m = |f(P)|`, and a deterministic decoder reading a
  uniform blind register attains it. A tolerance `ε* ≥ 1 − 1/m` is therefore vacuous.

**Secondary metric (reported, not deciding).** For each `t ∈ W_T` and each pair `σ ≠ σ′` in `P`,
`TV_t(σ, σ′) := TV( L(ρ_A(s_t) | σ), L(ρ_A(s_t) | σ′) )`, computed on the full register readout.

**Tolerance.** `ε* := [OWNER TO SET]`.

- It is chosen from the requirements of the intended record, before any further candidate is tested.
- No value is proposed here.
- The figure ¼ below is a result for one toy model, not a threshold.

**Required fields in every report.**

1. `P`, `f` and `g`, with their date relative to testing.
2. The retention window `W_T`.
3. `ε_max(t)` and `TV_t` for every `t ∈ W_T`.
4. Failures: each `(σ, t)` with nonzero error, the configurations that produce it, and their probabilities.
5. Conditioning: the full joint law, every conditioning event, `ν`, and the ledger `D(μ)`.
6. Hypotheses: the access baseline (D-ACC) and any new F2 extension.
7. The (R-d) test used (S-1, J-1 or none), labelled as unadopted.

**Example (a result only, from ROUTES.md HC-F0).**

- *Setup.* `M_F` under `π₀`, with `P = {(1,0), (1,1)}`, `f = v₀`, `g` the identity read of `r` and `T = 1`.
- *Primary metric.* `ε_max(t₀+1) = 0` and `ε_max(t₀+2) = 1/4`.
- *Secondary metric.* `TV_{t₀+1} = 1` and `TV_{t₀+2} = 1/2`.
- *Failures.* The arriving cell has `p = 1` and swaps in a `v ≠ f(σ)`. This happens with probability 1/4 for each `σ`.
- *Conditioning.* None (`D = 0`).

***

## D-TRN: transfer and exchange (OQ-1)

> Decision (verbatim): "exchange can count as nontrivial transfer. Carrier preservation is a separate property, not a
> universal requirement for recording. It still needs a distinct readable register and demonstrated retention after
> the incoming carrier has left. Correct the claim that Lemma C makes exchange the only possible write: the inequality
> establishes an entropy trade-off, not uniqueness of a mechanism."

**Definition.** A write, exchange included, is **nontrivial transfer** iff both of the following hold:

- (T-1) the register is distinct (R-a), and the transfer is new (R-b);
- (T-2) retention per D-RET is shown over a window whose hold ticks all come after the incoming carrier has left. "Left"
  means the joint vector `B_t` is independent of the carrier (cf. J-1 (J-i)); a cell-by-cell test is insufficient.
  - Testing "left" uses the same (R-d) operationalization, which is still open (S-1 and J-1 above).
  - A report states which proposal it used.

**Carrier preservation (CP), a separate property.** After the write, `f(σ)` is decodable from cells outside `A`. CP is
reported with its own error and is not required for transfer.

**Lemma C read correctly.** `I(c; r′) ≤ D(μ_R ‖ u_R) + H(c′|c)` is an entropy trade-off.

- With a maximal-entropy register (`D = 0`), a carrier-sensitive write must leave the outgoing carrier with
  conditional entropy at least the information gained.
- Exchange is one write with that property. Writes that disturb the carrier partially, and writes that use readiness
  (`D > 0`) in place of disturbance, are others.
- The inequality does not single out a mechanism.

***

## D-ACC: access baseline (OQ-3)

> Decision (verbatim): "accept H-cur (declared) as the named conditional baseline for this unit, consistently with the
> existing owner record. Keep physical sourcing of access as an explicit outstanding obligation when assessing a
> SOURCE-CANDIDATE."

- Every classification in this unit names H-cur (declared) among its hypotheses.
- Any assessment of a SOURCE-CANDIDATE carries the line "physical sourcing of access: outstanding". That line is not
  discharged by the baseline.
- Requirement 1 of #1032 is not met by the baseline.

***

## D-SEN: carrier sensitivity (OQ-5)

> Decision (verbatim): "accept NB-1's single-time preparation-conditioned laws. A path-law comparison may be additional
> mathematical evidence, but must not silently supply physical access across time."

**NB-1.** There are `σ ≠ σ′` in `P` and a tick `t ∈ W_T` with `L(ρ_A(s_t) | σ) ≠ L(ρ_A(s_t) | σ′)`, with `ν` held
fixed. Equivalently, `TV_t(σ, σ′) > 0`.

A path-law comparison over several ticks may be reported as additional evidence. Any claim that uses it to establish
reading across time names H-ret explicitly.

***

## D-SML: resource comparison instead of "smallest" (OQ-8)

> Decision (verbatim): "use a resource comparison rather than one scalar minimum. Report added dynamical assumptions,
> access/clock assumptions, preparation restriction, register and interaction size, write probability, retention
> duration and error. Compare mechanisms at fixed performance requirements. A vanishing write probability must not win
> merely by reducing the preparation ledger."

**Performance requirements.** These are fixed before any comparison: `P`, `f`, `T* = [OWNER TO SET]`, `ε*` (D-MET),
and a minimum write probability `w* = [OWNER TO SET]`.

**Write probability.** `w` is the probability under the declared law that the declared write event occurs at the write
tick.

**Comparison rule.**

- Only mechanisms that meet every requirement (`T ≥ T*`, `ε_max ≤ ε*` on `W_T`, `w ≥ w*`) are compared.
- Among them, no column outranks another by itself. One mechanism is reported as using fewer resources than another
  only if it is no worse in every column.
- Write probability is a requirement, not a column traded against the ledger. A mechanism whose `w` falls below `w*` is
  not compared, however small its preparation restriction.
- While `T*`, `ε*` and `w*` are unset, no comparison is issued.

**Table for the witnesses in ROUTES.md (entries as stated there; the `M_F` write probability and the HC-K3 ledger follow directly from the stated laws).**

| Mechanism | Added dynamical assumptions | Access and clock assumptions | Preparation restriction | Register and interaction size | Write probability | Retention duration | Error |
|---|---|---|---|---|---|---|---|
| `M_F` (HC-F) | new F2 extension E-reg: Fredkin gate on `(p₀, v₀, r)`, presence-bit channel, identity self-update of `r` | H-cur (declared) read of `r`; no clock | `π₀(· \| p_{L−1} = 0)`, `D = log 2` | 1 register bit; 3-bit gate; channel of `L ≥ 2` two-bit cells | write iff `p₀ = 1`; `w = 1/2` under the stated law | one hold tick. `k` ticks need `k` quiet cells and `L ≥ k+1` | 0 on the support |
| `M_F` under `π₀` (HC-F0) | as `M_F` | as `M_F` | none, `D = 0` | as `M_F` | write iff `p₀ = 1`; no probability stated in ROUTES | one hold tick | `ε_max`: 0 at `t₀+1`, 1/4 at `t₀+2`. TV: 1, then 1/2 |
| `M_T` (variant) | new F2 extension E-reg: Toffoli write `r ← r ⊕ p₀v₀` | as `M_F` | quiet bit and `r = 0`, `D = 2 log 2` | 1 register bit; 3-bit gate | write iff `p₀ = 1`; no probability stated in ROUTES | one hold tick | 0 on the support |
| HC-K3 | none (K1 at K-18(b)) | H-cur (declared) read of sites 1–4; the decoder reads a marker planted by the background as a tick indicator, with no accounted clock | `ν = δ_b`, a point mass on the 8 background cells. `D = 8 log 2`, as for any point mass on 8 bits | 4 readable cells; K1 nearest-neighbour update | imprint for every carrier value (linear); no probability stated | `t₀+1` to `t₀+2` | 0 (fixed decoder) |
| HC-P | a toy rule outside the corpus: `u₁ ← u₁ ⊕ u₀`, then shift | declared read of `u₂`; no clock | `π₀(· \| u₁ = 0, u_{L−1} = 0)`, `D = 2 log 2` | 1 register cell; 2-cell gate; ring of `L ≥ 4` | no probability stated | one hold tick, then the pulse moves on | 0 at `u₂` |

**Notes, not part of the comparison.**

- HC-K3 fails countercontrol (g). HC-P is countercontrol (e) and the proposed (h).
- `M_F` and `M_T` are toy witnesses conditional on an unjustified new F2 extension (ROUTES.md route III).
- ROUTES.md's statement that a trigger on `k` presence bits lowers the ledger to `log(2^k/(2^k−1))`, at write
  probability `2^{−k−1}`, is the kind of trade the comparison rule prevents from winning by the ledger alone.
- No ranking is issued, because `T*`, `ε*` and `w*` are unset.

***

## OQ-4: computation

> Decision (verbatim): "no computational check yet. First settle and review the criterion and metric, then present the
> proposed nonlinear rule, fixed instance and law, controls, budget and stopping rule for separate authorization."

Nothing in this document authorizes or prepares a computation beyond fixing the criteria above.
