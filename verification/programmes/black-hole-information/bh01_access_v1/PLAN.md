# BH-01 access audit, v1: preregistered plan

Status: exploratory research, unreviewed. This plan is committed before any computation
it describes. It changes no manuscript text and adopts no physical postulate.

Programme: `verification/programmes/black-hole-information/PROGRAMME.md`, item BH-01 and
lane 1 (formal finite access model). Base commit: `809fac52cdf207d24eccc63c734996bcb9d073a0`.

## 1. Question

Does reversible (bijective) evolution make initial-state information recoverable from
emitted radiation records, for a fixed observer-access class?

The owner's safeguard is kept as a definitional separation throughout: **conservation**
(the global configuration at time `t` determines the initial configuration) is a property
of the map `F` alone; **accessibility** (the observer's records determine the message) is a
property of the triple (map, access class, prior). The audit tests how the two are related;
it never treats one as the other.

## 2. Definitions

**Configuration space.** `X = Σ_1 × … × Σ_r`, a finite product of registers; register `j`
has alphabet `Σ_j` of size `q_j` (here `q_j = 2^b`, `b ∈ {1,…,4}`). Registers carry labels.
Two labellings are used:

- *moving-partition layout* — modes `m_1,…,m_n` that begin in the interior `B` and become
  radiation `R` one at a time, matching the setup of [GR Appendix A.7], where modes pass
  from `B` to `R` as the horizon shrinks and `n_B(t) + n_R(t) = n_B(0)`;
- *nested layout* — registers grouped as `V` (visible, containing the radiation registers
  `R_1,…,R_n`), `B` (interior) and `D` (trans-cosmological), matching
  `S = C_V × C_B × C_D` of [GR Appendix A.1].

**Dynamics.** A finite sequence `F_1,…,F_T` of maps `X → X` (time-homogeneous when all
`F_t` are equal); `x_t = F_t(x_{t-1})`. *Reversible* means every `F_t` is a bijection.
Non-bijective maps appear only in countercontrols.

**Message and prior.** A message `m ∈ M` is written into designated registers (the message
registers, in `B` at `t = 0`). Every other register is either *blank* (a fixed known value)
or *hidden-uniform* (uniformly distributed, independent of `m`). The hidden-uniform prior is
the framework's own Liouville marginalization over the hidden sector ([GR Appendix A.2],
uniform average over `C_B × C_D`; A.6(iii)). The initial state for message `m` is the
uniform distribution `μ_m` on its support `X_m ⊂ X`; all `X_m` have the same size `N`.

**Observer-access class.** A schedule `α : {0,…,T} → 2^{registers}` naming which registers
the observer reads at each time. The message registers are never in `α(0)`. Two record
modes:

- *cumulative records*: the record at time `t` is `ρ_t(x_0) = (π_{α(s)}(x_s))_{s ≤ t}` —
  every read is kept;
- *snapshot*: the record at time `t` is `π_{α(t)}(x_t)` alone.

The access class is fixed in advance and does not depend on `F`. "Access grows with time"
means `α(s) ⊆ α(t)` for `s ≤ t`. The *endpoint access* is `α(T)`; the *inaccessible
endpoint set* is `K = registers \ α(T)` (remnant registers and `D`), with `|K|` the number
of joint values of those registers.

**Operational equivalence.** Initial states `μ_m`, `μ_{m'}` are *indistinguishable to the
class at time t* iff their record distributions `P_m^t = (ρ_t)_* μ_m` and `P_{m'}^t`
coincide exactly.

**Figures of merit (exact rationals).**

- binary messages: distinguishing advantage `δ_t = TV(P_0^t, P_1^t)`;
- any `M`, uniform message prior: Bayes success `P_succ(t) = (1/|M|) Σ_y max_m P_m^t(y)`;
- *exactly recoverable* at `t` iff `P_succ(t) = 1`, equivalently the record images
  `ρ_t(X_m)` are pairwise disjoint (Lemma 0 below).

No entropy enters any verdict; all verdict quantities are `fractions.Fraction`.

## 3. Claims to test

Each claim is stated as the plan's hypothesis; its verdict is `HOLDS_WITHIN_SCOPE` when the
rule of §4 confirms it and `NEGATIVE_FOR_CONSTRUCTION` when the rule refutes it.

- **Lemma 0 (definitional; proved in writing, cross-checked).** Exact recovery at `t` iff
  the images `ρ_t(X_m)` are pairwise disjoint. This is close to the definition and carries
  no weight as a finding; it is used to give a second, independent computation of
  recoverability (set disjointness) beside the distributional one.
- **A (non-implication).** Bijectivity of `F` does not imply recoverability from the
  accessible records: within the exhaustive classes below there are bijective instances with
  `δ_T = 0` (respectively `P_succ = 1/|M|`) whenever some register is inaccessible at the
  endpoint. Also tested: bijectivity is not *necessary* for recoverability (a non-injective
  map can deliver the message to the accessible records). Together: bijectivity of `F` is
  logically independent of accessible recovery.
- **B (positive transport models).** There is a fixed access class and bijective dynamics
  that transfer the distinguishing information into emitted registers: (B1) a swap cascade
  moving message bits into `R_1,…,R_n`; (B2) a CNOT cascade that spreads one message bit as
  a parity over `n` shares with hidden-uniform keys; (B3) a one-step scramble followed by
  progressive emission. The exact `δ_t` / `P_succ(t)` profile is reported as a function of
  emission step, generated from enumeration.
- **C (sufficient condition and remnant bound).**
  - *C1 (complete endpoint access).* If every `F_t` is bijective and `α(T)` contains every
    register (`K = ∅`: no remnant, no inaccessible `D` at the endpoint), then `ρ_T` is
    injective on `X`, hence the message is exactly recoverable for every encoding and prior
    of the stated form. Neither conjunct alone suffices: tested by dropping bijectivity
    (complete access, non-injective maps) and dropping complete access (bijective maps,
    `K ≠ ∅`).
  - *C2 (remnant bound).* If every `F_t` is bijective, the records include the endpoint
    snapshot of `α(T)`, and `K` is the inaccessible endpoint set, then
    `P_succ(T) ≥ 1/|K|`. An inaccessible endpoint set of `|K| < |M|` values cannot hide the
    message entirely. Tightness is tested; failure without bijectivity is tested.
  - *C3 (decoupled `D`).* If `F_t = G_t × H_t` on `W × D` (`W = V ∪ B`), the initial `D`
    distribution is independent of `m`, and `D ∉ α(t)` for all `t`, then the record
    distributions equal those of the `W`-only model, so `D` may be dropped from `K`. A
    countercontrol couples `B` to `D`.
  - *C4 (linear threshold).* For a GF(2)-linear bijection `G` on `n` modes, message in `k`
    modes and the other `n − k` hidden-uniform, one scramble followed by emission of one
    mode per step (emitted modes thereafter unchanged): the number of recovered message
    dimensions `r_t = log2(2^k · P_succ(t))` satisfies
    `max(0, t − (n − k)) ≤ r_t ≤ min(k, t)`.
- **D (access growth and the endpoint).**
  - *D1 (refinement).* Under cumulative records with nondecreasing access, `δ_t` and
    `P_succ(t)` are nondecreasing in `t` for every map, bijective or not.
  - *D2 (snapshot countercontrol).* Under snapshot access, `δ_t` need not be monotone even
    for bijective `F` (information can return to an inaccessible register).
  - *D3 (endpoint statement).* What produces recovery in the tested class is the growth of
    the accessible record up to an endpoint at which the inaccessible set is empty or
    small; the claims C1–C2 are the precise form. The endpoint/remnant assumption is
    stated explicitly in the report: no remnant register, and `D` exactly decoupled or
    included in the endpoint access.
- **E (nested-trace associativity is independent of recovery).** For every bijection of the
  exhaustive nested layout, the direct and sequential marginal transition matrices of
  [GR Theorem A.1] coincide, including for the instances with zero accessible advantage.

- **F (endpoint-decoupling arithmetic; audit, not a model claim).** C1–C3 need `D` decoupled
  or read at the endpoint. [GR Appendix A.7] supplies decoupling by the statement that `D`
  is frozen on evaporation timescales, `τ_evap ≪ τ_B^D`, with `τ_B^D ∼ 1/H ∼ 10^{17}` s
  ([GR Appendix A.5]). The check compares the standard evaporation time
  `t_evap = 5120 π G² M³ / (ħ c⁴ Γ)` (the A.7 trajectory with `α = ħc⁴Γ/(15360πG²)`) with
  `τ_B^D` for the A.5 example mass `30 M_⊙`, by interval arithmetic on rationals
  (`3 < π < 22/7`, `Γ` allowed up to a stated generous ceiling, `1/H` at the largest value in
  a stated range), and reports the mass at which `t_evap = τ_B^D`.

## 4. Preregistered decision rule

The rule fixes how verdicts follow from measurements; it fixes no expected numbers.

1. **VOID.** If any required control in §5 fails, the run prints `VOID`, writes no claim
   verdict, and exits 2.
2. **Claim A** holds within scope iff the exhaustive bijective enumeration contains at
   least one instance with minimal accessible figure of merit (`δ_T = 0`, or
   `P_succ = 1/|M|`) whose bijectivity is confirmed by the independent checker, and the
   all-maps enumeration contains at least one non-injective map with exact recovery.
   Otherwise `NEGATIVE_FOR_CONSTRUCTION`.
3. **Claim B** holds within scope iff each named model is bijective (independent checker),
   has `δ_0 = 0` (or `P_succ(0) = 1/|M|`) and reaches exact recovery at some step `t ≤ T`.
   Otherwise `NEGATIVE_FOR_CONSTRUCTION` for that model. The profiles are reported as
   measured.
4. **Claim C1, C2, C3, C4** each hold within scope iff (i) the written proof is present in
   the report and (ii) exhaustive enumeration over every tested instance satisfying the
   hypothesis finds zero violations. Any violation makes that claim
   `NEGATIVE_FOR_CONSTRUCTION`, and the counterexample is printed. Separately, each
   countercontrol (hypothesis dropped) must find at least one violation; a countercontrol
   that finds none is reported as "hypothesis not shown necessary in the tested class" — it
   does not void the run and does not strengthen the claim. For C2, tightness is reported as
   measured (whether `min P_succ = 1/|K|` is attained).
5. **Claim D1** holds iff zero violations; **D2** holds iff at least one bijective snapshot
   instance has `δ_{t+1} < δ_t`. **D3** is the conjunction of C1, C2 and D1 and takes their
   verdicts; it carries no separate computation.
6. **Claim E** holds iff exact equality at every enumerated bijection, and the set of those
   bijections includes at least one with zero accessible advantage.
7. **Item F** reports the A.7 decoupling statement as *contradicted at mass M* iff the
   rational lower bound on `t_evap / τ_B^D` exceeds 1, *supported* iff the upper bound is
   below 1, and *undecided* otherwise. Item F is an audit observation and does not enter
   the overall verdict.
8. **Overall.** `HOLDS_WITHIN_SCOPE` iff every claim A–E holds within scope;
   `NEGATIVE_FOR_CONSTRUCTION` if any claim is refuted (each refuted claim named); `VOID` per
   item 1. All verdict text is generated from the measured values.

## 5. Controls and countercontrols

Each control has a mutant (§7) demonstrating that it can fail.

| id | control | fails when |
|---|---|---|
| K1 | independent bijectivity checker (image size equals domain size), applied to every map labelled bijective; plus rejection of a known non-bijection | a non-bijection is accepted, or a labelled bijection is not one |
| K2 | hand-derived exact values: identity with unread message `δ = 0`; direct read `δ = 1`; one-time pad (`R = m ⊕ k`, `k` hidden-uniform) each share alone `δ = 0`, both `δ = 1`; AND leak (`R = m ∧ k`) `δ = 1/2` | any computed value differs |
| K3 | second implementation of recoverability by set disjointness of record images (Lemma 0) and, for binary messages, the identity `P_succ = (1 + δ)/2`, compared on every enumerated instance | any disagreement |
| K4 | enumeration completeness: `|S_8| = 40320` distinct; `|GL(4,2)| = 20160` distinct and invertible; all maps on 4 points `= 256` | count or distinctness differs |
| K5 | linear-threshold cross-check: `P_succ` by enumeration equals `2^{r_t − k}` with `r_t` from GF(2) ranks computed independently | any disagreement |
| K6 | determinism: `result.json` byte-identical under `python3 -I -B` and `python3 -I -B -O` | bytes differ |

Countercontrols (hypothesis dropped, must find a violation): C1 without bijectivity; C1
without complete endpoint access; C2 without bijectivity; C3 with `B`–`D` coupling; D1
under snapshot records (this is D2).

## 6. Enumerated classes (size bounded for a run of seconds to minutes)

- `S_8`: all 40320 bijections of `{0,1}^3`, in the moving-partition layout (one message mode,
  two hidden-uniform; and two message modes, one hidden-uniform) and in the nested layout
  (`V`, `B`, `D` one bit each), time-homogeneous `F`, `T ≤ 3`.
- All 256 maps on `{0,1}^2` (`B` message bit, `R` hidden-uniform or blank), complete access
  at `t = 1`.
- `GL(4,2)`: all 20160 linear bijections of `{0,1}^4`, `k ∈ {1,2}`, emission order fixed.
- Structured families at larger size: swap and CNOT cascades with `n` up to 6 modes and
  `k` up to 3 message bits; register alphabets of 2 to 16 values (1–4 bits); a `B`–`D`
  leakage model.

## 7. Mutants

`mutants.py` loads `checks.py` as a module, replaces one function per mutant, reruns the
targeted control, and counts the mutant as caught only if that control reports failure on
its named case. Planned mutants: bijectivity checker accepting every map (K1); prior
ignored, hidden registers fixed at 0 (K2 one-time pad); total variation without the 1/2
factor (K2 direct read); disjointness decoder using union in place of intersection (K3);
truncated permutation enumeration (K4); rank routine off by one (K5); records not
accumulated (D1 control). Script and its output are kept.

## 8. Invariant → checkpoint table (§A.41)

| invariant asserted of the execution | checkpoint |
|---|---|
| plan committed before any computation | commit order: this file alone in its commit, parent `809fac52` |
| every exact claim uses integers/`Fraction` only | `checks.py` imports no `math`/float routine in verdict paths; result values serialized as `"p/q"` strings |
| every map labelled bijective is bijective | K1 |
| figures of merit are computed correctly | K2, K3 |
| enumeration is complete | K4 |
| linear claims computed two independent ways | K5 |
| output deterministic, both optimization modes | K6, and `SHA256SUMS` |
| verdict text generated from measurements | `result.json` field `verdict_text` built from counts; `REPORT.md` verdict block copied from it |
| a failed control voids the run | exit status 2 and `VOID` printed; exercised by mutants (each mutant run reports the voiding control) |
| each control can fail | `mutants-output.json`: every mutant caught |
| no `assert` used for checks | source scan in `checks.py` self-check (counts `assert` statements in its own source; must be 0) |
| run time bounded | measured wall time recorded in `PROVENANCE.json` (informational, not in `result.json`) |

## 9. What this would and would not establish

Would establish, for the stated finite classes: whether bijectivity alone implies
accessible recovery (by counterexample or its absence), an exact sufficient condition with
a written proof checked exhaustively, a remnant capacity bound, and the role of growing
cumulative access.

Would **not** establish: anything about black-hole physics, Hawking radiation, horizons or
evaporation; anything about OI's actual substratum dynamics (the wave equation on the
cubic lattice), since `F` here ranges over generic finite maps and is not derived from that
construction — only the hidden-uniform prior and the nested layout are taken from the
framework's construction; anything about quantum messages in superposition, entanglement
entropy or the Page curve (BH-02 / Page lane), since the records are configuration reads
of a classical permutation; anything about H-scramble. Finite observation-horizon results
are not physical event horizons. Exhaustive results at small size are finite checks of
statements proved in writing; they are not themselves universal proofs.
