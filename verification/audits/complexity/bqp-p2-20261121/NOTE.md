# BQP-P2: native complexity limits, and proof designs for Lean steps L0 and L1

**Status: WIP / UNVERIFIED.** This is the writer's research record for the BQP complexity
thread (P4) under the owner decision of #1169, comment 7064767045. That decision authorizes
research, proof exploration and planning. It does not authorize computation, CI, Lean builds or
manuscript changes, and this record makes none of them. No `.lean` file is written and nothing
is built. It awaits an independent non-author review. The record is stacked on #1488 at
`c8d87ff4`, and #1488 stays as reviewed. Issue: #1487.

**Base.** `main` at `df6da1c6`, the base of #1488. Line numbers are at that commit. `Comp` is
`papers/Computation.md`; `AUDIT` is `../bqp-audit-20261121/AUDIT.md`.

| Label | Meaning |
|---|---|
| [P] | manuscript statement at the cited line |
| [K] | Lean declaration on `main`, cited; nothing built |
| [R] | research record at its stated review standing |
| [W] | derivation in this record; not reviewed; not kernel-checked |
| [M] | Mathlib `v4.33.0` declaration, checked by reading the source file at that tag |
| [LIT2] | literature from memory, not re-located; background only |

## 0. Summary

- **Central question.** Can OI derive a nontrivial native complexity limit from its own premises
  without assuming efficient quantum simulation?
- **Upper limit.** One candidate passes the productivity test (§1), branch B3. Proposition BQ1
  [W] holds under five explicit hypotheses H1–H5 (§2.3), none of which assumes efficient quantum
  simulation. Under them, the output law of any native run with polynomial resources is exactly
  samplable by a classical polynomial-time algorithm. With polynomial resources, native
  bounded-error decision therefore lies in **BPP**.
- **Consequences** (conditional, [W] with [LIT2]):
  - native hosting of BQP under H1–H5 with polynomial resources implies BQP ⊆ BPP;
  - native hosting of IQP sampling to multiplicative error below √2 implies a collapse of the
    polynomial hierarchy.
- **What BQ1 exposes.** It derives, rather than assumes, the "bridge from substratum resources
  to classical simulation cost" that Comp:124 and Comp:134 take as a premise of the §4.5
  ceiling. That derivation consumes measurement independence, posit (xiv), beyond the Bell scope
  in which Main:736 states it. Comp:134 does not list (xiv). This is assumption-watch marker AW-1.
- **Lower limit: open.**
  - A native lower limit is a hosting theorem for the native rule, and it depends on native
    universality, which is unresolved (#1489, F4 open at `2572854b`). It is not assumed here.
  - BQ1 rules out a native lower limit containing BQP under H1–H5 unless BQP ⊆ BPP.
- **Proved resource bounds.**
  - m ≥ 2^{I*} (branch B1) gives only a linear space bound.
  - The zero-entropy-rate bound of Structure:1231 (branch B2) restates BQ1's accounting of random
    bits.
  - Neither is a complexity limit.
- **Lean.** §4 gives proof designs for L0 and L1, with Mathlib names checked at `v4.33.0`.
  - L0 is cheap.
  - L1's definitions are cheap. Every closure lemma needs composition of polynomial-time
    machines, which Mathlib states only as `proof_wanted TM2ComputableInPolyTime.comp`. That
    prerequisite dominates the cost of L1.

## 1. Productivity test (§A.31)

The test was fixed before any branch verdict was recorded. A branch is a **gem** iff both hold:

- **(T1)** it yields a statement about computational resources of native OI runs that is strictly
  stronger than the trilemma of Comp:122, which is the obvious restatement;
- **(T2)** it either constrains a complexity class or resource scaling, or exposes a hypothesis
  that a corpus statement consumes without listing it.

A branch that fails either part is recorded only. Favourable branches get maximum skepticism.
"Favourable" means favourable to any corpus claim; BQ1 counts as unfavourable to the efficiency
reading of §4, so it gets maximum skepticism as well, since it is the branch the record adopts.

## 2. Depth-first branch walk

### B1. The capacity bound m ≥ 2^{I*}

- **Source.** Main:522 is a corollary in Main §3.4 [P]. Any deterministic-bijection realization of
  a process with conditional past–future information I* has m ≥ 2^{I*} hidden states.
- **Check.** An emergent register of n qubits carries conditional memory of at most 2n bits.
  The bound then asks for O(n) hidden bits.
- **Verdict.** It is a space bound, linear in n, on realizing a process. It is not a bound on a
  class of languages or on time. It fails T1. Non-gem: CONFIRMING.

### B2. Zero entropy rate (Structure:1231)

- **Source.** Structure:1231 [P]. Under every invariant prior, the visible factor of a finite
  reversible substratum has zero entropy rate, and recorded randomness is bounded by
  log|C_V × C_H|.
- **Check.** In BQ1 below, the random bits a classical sampler needs are exactly a uniform draw of
  the dependency set's initial state (§2.3, step 2). B2 is the same accounting, taken over the
  whole configuration space.
- **Verdict.** It restates the seed accounting and adds no class or scaling. It fails T1. Non-gem:
  CONFIRMING. It supports BQ1's step 2.

### B3. Native classical simulability (decisive branch)

#### B3.1 Statement

**Proposition BQ1 [W].** Consider a family of native runs indexed by input size n, with these
hypotheses:

- **H1, rule.** The update is the second-order form of ledger item (xiii) (Main:736;
  `ruleDynamics`, `OIBridge/SecondOrderDrive.lean` [K]). The group is ℤ/q with q fixed, and each
  `F_i` is computable in time polynomial in log q. The rounded rule `R_q` (SM:294) satisfies H1.
- **H2, prior.** The pre-run law of the configuration on the dependency set D (H5) is uniform
  (product Haar). On a finite representative this is the counting measure selected by Lemma 3
  under posit (iv) (Main:54, Main:736). On an infinite lattice it is an added hypothesis, which
  the corpus does not state.
- **H3, settings.** The input x is written into a region by an intervention whose pre-setting
  ensemble does not depend on x. This is posit (xiv), measurement independence (Main:736;
  Main:410–416), applied to computational inputs.
- **H4, readout.** The input encoding and the readout map from the visible configuration at time
  T to the output are polynomial-time. Either an outcome is recorded in every run, or
  conditioning on a record has success probability at least 1/poly(n). The second is charged
  postselection, the §4 model's own hypothesis (Comp:106).
- **H5, cone.** The dependency set D of the readout region over T steps has |D| = poly(n). The
  causal-cone lemma (Main:368) [P] is stated on a finite site set. Main's Bell–lattice
  corollary, part (2) (Main:420), carries it to a site set of any cardinality for finite regions
  under the nearest-neighbour update. For that graph on ℤ^d it gives |D| = O((T + R)^d), with R
  the readout radius. So H5 holds whenever T(n) and R(n) are
  polynomial. H5 also holds on any finite site set of size poly(n), whatever the graph.

**Conclusion.** The joint law of the outputs is exactly samplable by a classical algorithm in
expected time poly(n). Hence:

- a language decided with bounded error by such a family lies in BPP;
- the output distributions lie in the class of efficiently samplable distributions.

#### B3.2 Proof sketch [W]

1. By H5 and the cone lemma, the output is a function of the initial configuration on D, which
   is finite and polynomial in size.
2. By H2 and H3, that configuration, given input x, is uniform on D with the input region
   overwritten by the encoding of x. It is samplable with |D|·log₂ q fair bits when q is a power
   of two. Otherwise, rejection sampling gives an exact sampler in expected constant time per
   site.
3. By H1, T steps on D cost O(|D|·T·poly(log q)) operations.
4. By H4, the readout is polynomial-time. Conditioning is simulated by rejection at an expected
   cost of poly(n).
5. A Las Vegas sampler truncated after k times its expected running time errs with probability
   at most 2^{−k}. That additive error is absorbed in the bounded-error decision case. For the
   multiplicative-error corollary below, k is taken polynomially larger than the log of the
   inverse of the postselected probability.

#### B3.3 Corollaries

**Corollary BQ1-D [W].** If a family satisfying H1–H5 decides every language in BQP, then
BQP ⊆ BPP. This needs no conjecture.

**Corollary BQ1-S [W, LIT2].** Suppose a family satisfying H1–H5 reproduces the output
distributions of IQP circuits to multiplicative error below √2. Then PostBPP = PP, and the
polynomial hierarchy collapses to its third level (Bremner–Jozsa–Shepherd 2011 [LIT2]).

Consequently, under non-collapse of PH, any native hosting of IQP sampling fails H1, H2, H3, H4
or H5. For the nearest-neighbour graph, failing H5 means a native time T(n) superpolynomial in
the qubit count n.

#### B3.4 Skepticism checks

Each check names its verdict.

- **(a) Noise.** Physical hosting gives additive (total-variation) error. BQ1-S then needs the
  stronger anticoncentration and average-case conjectures of the sampling literature [LIT2].
  BQ1-D is unaffected. *Scope narrowed accordingly.*
- **(b) Settings.** Without H3, the hidden law conditional on input x can be an arbitrary
  reweighting. Simulating it classically means conditioning on an event of probability about
  2^{−|x|}, which is free postselection, of PostBPP type. So H3 is the native counterpart of the
  §4 model's charged postselection (Comp:106). Main:410–416 retain (xiv) as a posit for the Bell
  analysis. Its use for computational inputs is an extension of that scope, not something the
  corpus states. *Load-bearing: AW-1.*
- **(c) Prior.** If the prior were a non-product invariant measure, such as uniform on one cycle,
  sampling it would require computing φ^t for t up to the cycle length. For reversible cellular
  automata that is not known to be efficient [LIT2]. H2 is therefore load-bearing too.
  #1477's edit D260 rewrites Main:54 to scope the counting-measure selection "on a finite
  representative". BQ1 on an infinite lattice uses product Haar as its own hypothesis, not as a
  corpus measure. *Dependency recorded.*
- **(d) Locality.**
  - For Bell correlations the framework gives up locality through "preparation-indexed
    adjacency", bounded-degree long edges (Main:418; H-Bell, open), not (xiv).
  - With long edges of degree Δ on an unbounded site set, the dependency set can grow as Δ^T,
    and H5 fails at polynomial T.
  - On a finite site set of size N, H5 holds with |D| ≤ N, whatever the graph.
  - So the framework's own Bell mechanism escapes BQ1 only through a superpolynomial dependency
    set. That is horn (III) of Comp:122.
  - *BQ1 is consistent with Comp §4.5 and does not contradict it.*
- **(e) Is the conclusion trivial?** The proof is elementary. Its content is in the hypotheses it
  names. The §4.5 ceiling assumes "a bridge from elementary substratum updates to classical
  sampling cost" (Comp:120, 124, 134). Under H1–H5, BQ1 derives that bridge with the resource
  |D|·T. *T1 holds: this is stronger than the trilemma, which leaves the bridge assumed.*
- **(f) Units in §4.** The §4 model asks for "efficient" encoding, preparation and control
  (Comp:15, 94, 106) without fixing whether "efficient" means polynomial in the emergent qubit
  count or in native sites and steps. Read in native units, the §4 model together with H1–H5
  implies BQP ⊆ BPP (BQ1-D). Read in emergent units, it is consistent with BQ1. The corpus does
  not fix the units. *T2 holds: an unlisted choice is exposed. AW-2. No manuscript change is
  proposed here.*
- **(g) Shared hypotheses with the Bell ceiling.** Main's Bell ceiling (Main:370–397) and BQ1
  share determinism, the cone lemma and measurement independence. This is a shared hypothesis
  set. No identification of the two obstructions is claimed, and no formal map between them is
  given.

**B3 verdict.** Gem. Classification: ELABORATING (BQ1 sharpens horn (III) and derives the §4.5
bridge), with assumption-watch markers:

- **AW-1.** The §4.5 bridge consumes posit (xiv) outside its Bell scope, together with H2.
  Comp:134 lists posits (iv) and (v) but not (xiv).
- **AW-2.** The resource units of the §4 model's efficiency hypotheses are unfixed.

Standing: [W], unreviewed.

### B4. Native lower limits

- A native lower limit asserts that the native rule hosts some class with polynomial overhead.
  For any class containing P, that is efficient native universality. Whether a universal member
  of OI's narrow class exists is open (#1489 F4, at `2572854b`, [R] at its own standing). This
  branch does not assume it.
- **Even a positive answer** gives classical hosting: P with an overhead to be determined. By
  BQ1-D, no lower limit containing BQP holds under H1–H5 unless BQP ⊆ BPP.
- **Verdict.** Open. It depends on #1489, and that dependency is unresolved. Under H1–H5, the
  most a native lower limit can reach is BPP.

### B5. Fixed-point pass

Three re-passes over B1, B2 and B4 found nothing NEW:

1. B1 under the quantum-register reading;
2. B2 with a non-uniform invariant prior, which reduces to B3(c);
3. B4 with Margolus's universal second-order rule (#1489 F2), which lies outside the narrow
   class and does not apply.

Under the §A.31 fixed-point rule the walk stops at B3 for this record.

## 3. Dependencies (none is treated as established)

| Dependency | Used by | Status |
|---|---|---|
| Lemma 3 counting-measure selection, posit (iv) | H2 | posit; Main:54 rewritten by #1477 D260 |
| Measurement independence, posit (xiv), extended to computational inputs | H3 | posit for §3.3 (Main:410–416); extension unstated in the corpus |
| Ledger (xiii) second-order form; polynomial-time F | H1 | posit; R_q satisfies it |
| Causal-cone lemma; its extension to infinite site sets for finite regions | H5 | Main:368 and Main:420, paper argument |
| Bremner–Jozsa–Shepherd 2011 | BQ1-S | [LIT2] |
| Native universality | B4 | open (#1489) |
| Finite representative, total finiteness | not needed | BQ1 uses the cone instead; posit (ii) deleted by #1477 D224 |

## 4. Lean proof designs (plan only; nothing written or built)

All names below were checked in the Mathlib `v4.33.0` source [M]. Cost classes:

- **S**: under a day, Mathlib only;
- **M**: days, a new module of moderate size;
- **L**: weeks, needs absent Mathlib infrastructure.

### L0. Halting within the cardinality bound (I12; Comp:74, Comp:190)

```lean
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Dynamics.PeriodicPts.Lemmas

theorem orbit_meets_iff_meets_before_card {α : Type*} [Fintype α]
    (f : α → α) (H : Set α) (x : α) :
    (∃ n, f^[n] x ∈ H) ↔ ∃ n < Fintype.card α, f^[n] x ∈ H
```

- **Proof design.**
  - (⇐) is immediate.
  - (⇒): take the least n with `f^[n] x ∈ H` (`Nat.find`). Suppose `n ≥ card α`. Apply
    `Fintype.exists_ne_map_eq_of_card_lt` to `fun i : Fin (card α + 1) => f^[i] x` to get
    `i < j ≤ card α ≤ n` with `f^[i] x = f^[j] x`. Then `Function.iterate_add_apply` gives
    `f^[n - (j - i)] x = f^[n] x ∈ H`, which contradicts minimality.
  - Corollary: `Decidable (∃ n, f^[n] x ∈ H)` given `[DecidablePred (· ∈ H)]`, by
    `decidable_of_iff` and `Nat.decidableBallLT`.
- **Alternative for a bijection.** Every point is periodic, and `Function.minimalPeriod_le_card`
  (`Mathlib/Dynamics/PeriodicPts/Lemmas.lean`) bounds the period.
- **Establishes.** The bounded search behind Comp:74 and Comp:190. Decidability alone is trivial
  classically; the bound is the content.
- **Does not establish.** Any time bound in terms of an input size: `card α` is exponential in
  the number of sites. Nothing about complexity classes.
- **Cost.** S. One lemma; no new definitions.
- **Registry.** A new module needs a census family and anchor in the same commit (§A.35).

### L1. Exact-gate-set circuits, uniformity, and BQP as a set of languages

**Definitions** (sketch of the exact statements):

```lean
import Mathlib.Computability.TuringMachine.Computable
import Mathlib.Computability.Encoding
import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.Analysis.SpecialFunctions.Pow.Real

inductive Gate (n : ℕ) | had (i : Fin n) | toff (a b c : Fin n) (h : a ≠ b ∧ b ≠ c ∧ a ≠ c)

/-- the real matrix of a gate on the basis `Fin n → Bool`; `toff` via `Equiv.Perm.permMatrix` -/
noncomputable def Gate.mat {n} : Gate n → Matrix (Fin n → Bool) (Fin n → Bool) ℝ

noncomputable def Circuit.mat {n} (c : List (Gate n)) : Matrix _ _ ℝ := (c.map Gate.mat).prod

/-- acceptance probability on input `x`: qubits `0..|x|-1` carry `x`, the rest start at false,
qubit `0` is read -/
noncomputable def accProb {n} (c : List (Gate n)) (x : Fin n → Bool) : ℝ

/-- a circuit family is uniform when some machine maps the unary size to the gate list's
encoding in polynomial time -/
def Uniform (desc : ℕ → List GateCode) : Prop :=
  Nonempty (Turing.TM2ComputableInPolyTime Computability.unaryEncodingNat.encode
    (encodeGates) desc)

def BQP : Set (List Bool → Prop)  -- languages L with a uniform family and a polynomial width
  -- such that accProb ≥ 2/3 on L and ≤ 1/3 off L
```

- **Mathlib names used** [M]:
  - `Turing.TM2ComputableInPolyTime`, a `structure` with fields `tm`, `time : Polynomial ℕ` and
    `outputsFun`. It is data, so uniformity is `Nonempty (…)`.
  - `Computability.unaryEncodingNat`, `Computability.encodingNatBool`,
    `Computability.FinEncoding`, `Computability.encodingList`;
  - `Equiv.Perm.permMatrix`;
  - `Matrix.orthogonalGroup`;
  - `Turing.idComputableInPolyTime`, the only polynomial-time machine Mathlib constructs.
- **Gate set.** `GateCode` and `encodeGates` would be a small finite alphabet and a list
  encoding over it, which `TM2ComputableInPolyTime` needs as `αΓ`/`βΓ` with `[Fintype]`.
  Hadamard + Toffoli is exact with real entries, so no Solovay–Kitaev is needed.
- **Sanity lemmas** in the design:
  - `Gate.mat` lies in `Matrix.orthogonalGroup`;
  - `accProb ∈ [0, 1]`;
  - a lemma that any language decided by a uniform family of Toffoli-only circuits lies in `BQP`;
  - closure of `BQP` under complement.
- **Establishes.** A definition of BQP over an exact gate set, with uniformity carried by an
  actual polynomial-time machine rather than an abstract predicate.
- **Does not establish.**
  - Any relation to OI.
  - Agreement with Comp:98's H/T/CNOT definition with Solovay–Kitaev. That needs the Shi /
    Aharonov universality of Hadamard + Toffoli [LIT2], and it is not part of L1.
  - That `BQP` contains anything nontrivial beyond the sanity lemmas.
- **Cost.**
  - The definitions and the unitarity and probability lemmas: M.
  - The two closure lemmas need to transform a circuit description in polynomial time: append a
    gate, or compose the size map with a polynomial. That needs `TM2ComputableInPolyTime.comp`,
    which Mathlib `v4.33.0` states as `proof_wanted` (`Computable.lean:284`) and does not prove.
  - With closure: L, dominated by proving TM2 polynomial-time composition. A cheaper variant
    states uniformity relative to an arbitrary polynomial-time-closed class passed as a
    parameter. That variant hollows out "uniform" (AUDIT §4, L1 risk) and is recorded as a
    fallback only.
- **Order.** L0 can start independently. L1 should start with the composition lemma, or with the
  definitions only, and leave both closure lemmas open until that lemma exists.

A Lean statement of BQ1 itself is not designed here. Its formal content needs L1 plus a
`SampBPP`-style notion of classical sampling, which Mathlib does not have. It is noted as a
later rung after L1.

## Files

- `NOTE.md`: this file. No script; no computation was run for this record.
