*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and outputs beside this file are the reviewer's; the coordinator re-ran them under `python3 -I -B`, and the `.out` files are the coordinator's re-run outputs (the reviewer kept none). They reproduce the review's figures, including the per-parent counterexamples at d=3 (5.0007 against 4.0002) and d=4 (8.0022 against 4.0016).*

# Independent review: the ε-realization results of `papers/Main.md` (corpus at eae01647)

Objects reviewed: the theorem "finite operational realization and gluing, ε-form" (Main.md:544, with clauses (1)–(5), the
instrument-level Rounding Lemma at :556, and the proof at :558); the Corollary "single controlled dynamics" (:560); the
Remark at :562; the adaptive diamond-telescoping Lemma (:574); the theorem "uniform continuum realization, mutual
ε-density" (:576); the Corollary "finite-test density" (:578); Summary item 4 (:580). Imported results I read: the
response-table / process-dilation theorem (:496–:500), the comb theorem and the no-uniform-realization Proposition
(:460–:464), the memory and capacity floors (:492, :582–:588), the classical-dimension Proposition (:538), and the
probe `papers/oi_lattice_code/foundations/opglue_probes.py`. No Lean module formalizes any of these ε-results. I
searched `verification/lean-mathlib/OIBridge/` for gluing, rounding, telescoping and diamond-norm content and found
none. The results rest on prose proofs and on the probe. Context: Introduction-4a260ca9 abstract (L12) and §3.4
(L126–L132). Neither currently states the ε-result.

Scripts are in `S/proofrev/eps/scripts/`.
All of them use exact `Fraction` arithmetic and were run with `python3 -I -B`.

---

## 1. Verdict

**ACCEPT WITH CHANGES.**

- The exact-arithmetic regime is correct. This covers clause (1) with the bound K(|O_max|−1)/G, clauses (2)–(4),
  the capacity form in clause (5), the single-dynamics Corollary after a trivial re-padding, and the uniform-continuum
  theorem with its ε-budget.
- The existence claim "for every ε there is a finite reversible deterministic realization, uniform over all adaptive
  protocols" therefore stands.
- Named gaps needing changes: G1 and G2 are substantive; G3, G4 and G6 (§3) are minor but are stated wrongly; G5 is I1 below.
  - **G1 (substantive, proof gap).** The finite-precision (fixed-point, b-bit) half of clause (1) is not proved as
    written. The step that extends the clipping/normalization Corollary to Hermitian, non-positive registers
    (the "negativity ledger") is invalid. The per-parent inequality it asserts is false, with exact counterexamples
    below, and the ledger recursion omits the normalization factor s/Q, which amplifies negative mass. I could not
    refute the final bound, and a stopping-time repair recovers a bound of the same order O(K²C_{d,R}2^{−b}) with a
    larger constant. Until that repair is written, the explicit constants (12K²C_{d,R}2^{−b}, b ≥ log₂(24K²C_{d,R}/ε))
    and Summary 4's "proved … AND at finite b" are unproved. So are the fixed-point resource claims that depend on them:
    linear-in-K capacity, and hidden capacity independent of |N|.
  - **G2 (substantive, inconsistency).** In the uniform theorem the ε-budget (Kδ + K(m−1)/G ≤ ε) is computed for the
    exact regime. Its claim that hidden capacity is independent of |N| holds only in the fixed-point regime, whose
    rounding term is not budgeted. In the exact regime the hidden capacity grows with log|N|.
  - **G3 (minor).** The formula G = ⌈2K(m−1)/ε⌉ gives G = 0 when m = 1 (or |O_max| = 1).
  - **G4 (minor).** The lower bound c₁K ≤ log₂|C_H| in clause (5) cites the I* floor. That floor applies to faithful
    realizations, and the constructed realization is ε-faithful only. The inequality holds for a trivial reason
    (K log₂ G ≥ K).
- There are also scope and interpretation corrections, listed in §3 and §6:
  - **(I1)** The Kochen–Specker sentence in clause (3) is overstated.
  - **(I2)** Summary 4 attributes the necessity of ε to Proposition (3). For a fixed finite experiment an exact
    realization exists (the comb theorem with a real-valued product prior). ε is forced only by the rational uniform
    seed prior, or by uniformity over the instrument continuum, where the counting Proposition at :464 already
    suffices.
  - **(I3)** The Corollary at :560 calls the result "the substratum ontology stated as a theorem". The realization's
    hidden state is the (unnormalized) quantum density matrix, held exactly or digitized, and quantum mechanics is an input.

---

## 2. The statement as proved

### 2.1 Gluing theorem, exact-arithmetic regime (proved)

The following are fixed, in this order: d; an initial state ρ₀; a finite family F of instruments on ℂ^d, each a finite
family of CP maps with finitely many Kraus operators, summing to a channel; a horizon K ≥ 1; and a grid size G ≥ 1.

The construction then gives a finite set X = V × H and one bijection φ_a of X for each a ∈ F, with a fixed initial
distribution: the visible register empty, the branch register equal to ρ₀, the stack empty, and K seeds i.i.d. uniform
on {0,…,G−1}. **For every** adaptive protocol π over F of horizon ≤ K (deterministic, or randomized by convexity):

  TV(P^R_π, P^Q_π) ≤ K(|O_max|−1)/G.

TV is the half-ℓ¹ distance between outcome-sequence laws. The realization is fixed before the protocol, so the bound is
uniform over protocols. "For every ε" follows by taking G ≥ K(|O_max|−1)/ε. So "for every ε there is a realization
uniform in all adaptive protocols over F" is what is stated and proved. It is stronger than a per-protocol statement.

Hidden alphabet: |H| ≤ (|V_reach|+1)^{K+1}·G^K. An "empty-slot" symbol is needed, which is an off-by-one in clause (5).
V_reach is finite, with |V_reach| ≤ Σ_{k≤K}(Σ_a|O_a|)^k.

Clauses (2)–(4) hold by construction:
- restriction gives identical, not approximate, laws on sub-families and shorter horizons;
- each instrument is one fixed map;
- sequential composition is immediate;
- parallel composition is the gluing theorem applied on ℂ^{d_A d_B} with a joint register.

### 2.2 Gluing theorem, fixed-point regime (claimed; not proved as written)

Claimed:

  TV ≤ K(|O_max|−1)/G + 12K²C_{d,R}2^{−b}, with C_{d,R} = 48Rd⁴.

The parts that are proved:
- the raw-drift Rounding Lemma Σ_o‖Î_o(ρ̃) − I_o(ρ̃)‖₁ ≤ C_{d,R}2^{−b}‖ρ̃‖₁ for Hermitian ρ̃ in the window. I re-derived
  ≈ 17Rd⁴ for real entries; complex rounding costs about another factor √2·1.5, still within 48;
- the raw cq telescoping (no clipping);
- the clipping/normalization Corollary for positive inputs, 2η/(1−η) ≤ 4η, which I re-derived;
- the window management.

Not proved: the Hermitian-input extension and the negativity ledger (G1). What I believe is provable is
TV ≤ K(|O_max|−1)/G + c·K²C_{d,R}2^{−b} for an absolute constant c, by the repair in §3/G1. Then
b = log₂(K²C_{d,R}/ε) + O(1) = O(log(Kd|O|/ε)) and log₂|C_H| = O(Kd² log(Kd|O|/ε) + K log G) both survive, with
different constants.

### 2.3 Corollary at :560 (proved, after a one-line fix)

Φ(x) = φ_{π(x_vis)}(x) is injective on well-formed states: the record fixes the control, and φ_a is injective there.
It extends to a bijection by padding again. Padding each φ_a separately does not make the controlled map injective on
ill-formed states (G6). The program register costs up to Θ(|O_max|^K log|F|) bits and is charged separately, as the
text says. Here the protocol is part of the hidden initial condition.

### 2.4 Uniform theorem at :576 (proved in the exact regime, with G2)

The following are fixed, in this order: d, m, K, ε ∈ (0,1], and the initial reference state, with preparations counted
as steps of the horizon. Take a diamond-norm δ-net N of the ≤m-outcome instruments, with δ = ε/(2K) and
G = ⌈2K(m−1)/ε⌉. This gives **one** finite R such that:
- (i) ∀π (adaptive, continuum instruments, ≤ m outcomes, horizon ≤ K) ∃π̂ (history-wise net rounding) with
  TV(P^Q_π, P^R_π̂) ≤ Kδ + K(m−1)/G ≤ ε;
- (ii) ∀ R-protocol ∃ quantum protocol (the same protocol, run on net members) with TV ≤ K(m−1)/G ≤ ε/2.

The volumetric estimate is correct for δ ≤ 1/2, which holds because ε ≤ 1. Covering in the diamond norm itself gives
|N| ≤ (1+8/δ)^{D} with D ≤ m d⁴, and no d-dependent norm-equivalence constant enters. The telescoping Lemma is correct,
with a factor ½ to spare, since TV ≤ ½‖·‖₁ ≤ ½‖·‖_◇.

### 2.5 Corollary at :578 (proved)

Along K_n → ∞ and ε_n → 0, Q^{(d,m)} ∈ closure(D_finite) in the finite-test topology, at each fixed (d, m). The
corollary marks it as density and not identity, and that marking is correct.

---

## 3. Gaps and errors

### G1. The Hermitian-input step of the Rounding Lemma is invalid (Main.md:556, "The Corollary is exact for positive inputs … with slack")

**What the text asserts:**
- (a) ν_{t+1} ≤ ν_t + η‖σ̂_t‖₁, on the grounds that "clipping or the fallback only removes or relabels mass";
- (b) the Hermitian-input application of the Corollary "costs at most 8ν_t extra across the parents", obtained by
  writing ρ̂ = ρ̂₊ − ρ̂₋, applying the positive estimate to ρ̂₊, and using the triangle inequality on ρ̂₋.

**Why these fail.** The normalized kernel K̃(ρ̂) = ⊕_o (s/Q)C_o is nonlinear. It multiplies every retained block,
including its negative part, by s/Q, where s = Tr ρ̂ and Q is the digitized clipped total. Normalization is neither
"removing" nor "relabelling". Whenever Q < s it **increases** negative mass, which (a) omits.

The triangle-inequality step in (b) would need a Lipschitz bound ‖K̃(ρ̂) − K̃(ρ̂₊)‖ ≲ ‖ρ̂₋‖. No such bound holds near
Q → 0⁺, because s/Q is unbounded there for negativity-dominated registers (‖ρ̂₋‖₁ ≳ Tr ρ̂). On positive-dominated
branches (ν_h ≤ θ s_h) I re-derived a per-parent error ≲ 2E + 3ν_h + O(ηθ s_h), consistent with the claim. The failure
is confined to negativity-dominated branches, but the proof's inequality is stated for all Hermitian parents.

**Exact counterexamples to the per-parent inequality (b)** (`neg_parent4.py`). Setup:
- an outcome-free channel with R = d² diagonal Kraus operators diag(√p_{k,1},…,√p_{k,d}), Σ_k p_{k,i} = 1, which is
  exactly trace-preserving, so I(ρ̂) = ρ̂ and no irrational comparison is needed;
- the Hermitian dyadic register ρ̂ = diag(½+s, −1/(2(d−1)), …), with ‖ρ̂‖₁ = 1+s inside the window and ν = ½;
- the paper's fixed-point model: b fractional bits, round-to-nearest-even per product and per addition, Kraus entries
  rounded.

The Rounding Lemma's raw bound E ≤ η‖ρ̂‖₁ holds in every instance. The normalized-kernel error nevertheless exceeds the
claimed 4ηs + 8ν:

| d | R | b | Tr ρ̂ | Q | s/Q | ‖K̃(ρ̂)−I(ρ̂)‖₁ | claimed 4ηs+8ν |
|---|---|---|---|---|---|---|---|
| 2 | 4 | 16 | 4·2⁻¹⁶ | 1·2⁻¹⁶ | 4 | 3.0002 | 4.0000 (holds) |
| 3 | 9 | 16 | 6·2⁻¹⁶ | 1·2⁻¹⁶ | 6 | **5.0007** | 4.0002 (**fails**) |
| 4 | 16 | 16 | 9·2⁻¹⁶ | 1·2⁻¹⁶ | 9 | **8.0022** | 4.0016 (**fails**) |

The amplification of negative mass in (a) is also exhibited at d = 2 (`neg_parent.py`, b ∈ {12, 16, 20}): the output
negativity (s/Q)‖C₋‖₁ ≈ 2.0, against ν_in + E ≈ 0.5. The error grows like (s/Q − 1)‖ρ̂‖₁, and s/Q can reach the order of
the number of rounding events, about R·d. The claimed 8ν does not scale with R or d.

**Scope of the counterexample.**
- It refutes the inequality the proof derives, per parent. It does not refute the aggregated recursion
  δ_{t+1} ≤ δ_t + 4η(1+δ_t) + 8ν_t, nor the final TV bound. A violating branch must carry absolute negativity
  comparable to η ≈ 48Rd⁴2^{−b} to overturn the aggregate, and real rounding errors are about three orders of magnitude
  below η.
- I did not construct a reachable trajectory that ends at such a register. In d = 2 with rank-one projective
  measurements, step-1 rare-outcome blocks have ‖C₋‖/Tr C ≤ 0.618 in every instance I sampled (`zero_outcome2.py`,
  502 unclipped blocks).
- A two-step adversarial instrument plausibly can produce one. Such a step would take a full-rank effect E₁ with
  Tr(E₁ρ̂) ≈ 0 on a ratio-0.6 register, which keeps the negativity while cancelling the trace. I did not build it.
  Such subtrees have exact mass zero and digitized mass ≈ 2^{−b}.

**Why it matters.** The fixed-point half of clause (1), the bit count b ≥ log₂(24K²C/ε), the capacity figure
O(Kd² log(Kd|O|/ε)), and Summary 4's "proved unconditionally … AND at finite b" all rest on this step.

**Fix: a stopping-time argument, needing no change to the simulator.**
- Call a history h *good* if every prefix g satisfies ν(ρ̂_g) ≤ θ·Tr ρ̂_g, with θ = 1/(2K).
- On good parents: Q ≥ s/2. The per-parent error is ≤ c₁ηs + c₂ν. Children's negativity is
  ≤ (1 + 2θ + 3η)(ν + E). The good-tree negativity therefore stays ≤ e^{1+o(1)}·1.5tη, and the good-tree trace-norm
  drift is O(K²η).
- At a first-bad history g: digitized mass Tr ρ̂_g < ν_g/θ = 2Kν_g. The kernel conserves this mass exactly through the
  whole subtree, including the fallback. The exact mass Tr ρ_g is within ‖ρ̂_g − ρ_g‖₁ of it.
- Charge the entire subtree. The cost is ≤ Σ_g(2·2Kν_g + ‖ρ̂_g−ρ_g‖₁). Since the ν_g are bounded by the good-tree
  negativity budget, this is O(K²η).
- Result: TV ≤ K(|O|−1)/G + c·K²C_{d,R}2^{−b}, with an absolute c larger than 12, and b shifts by O(1) bits.

Alternatives: change the simulator to send any branch with Tr C < 2K·(computable norm proxy of C₋) to the fallback.
Or remove the fixed-point claims and rely on the exact regime, which already delivers existence. Either way, the
constants "12" and "24" in clauses (1) and (5) and in the uniform theorem need restating.

**Probe coverage.** Check 16 (`simulator_kernel_clipped_normalized`) does not measure the ledger quantity the proof
uses:
- it sums ‖(raw block)₋‖₁ of the un-normalized chain of raw blocks, never multiplying by the accumulated factors
  Π(s/Q), which are exactly the factors at issue;
- it never applies the window rescaling;
- it is a single d = 2, K = 3 tree with nearly dyadic instruments.

Its "ledger ν_t ≤ 2tη" therefore does not certify the step. The fixed-point rescaling is never exercised in fixed
point: check 10 is exact-ring only.

### G2. Regime mismatch in the uniform theorem (Main.md:576)

Statement (i) budgets Kδ + K(m−1)/G = ε/2 + ε/2 = ε. That accounting is exact-regime only: there is no rounding term.
The same theorem claims that hidden-state capacity is independent of |N|, and that "clause (5)'s hidden bound applies
verbatim".

In the exact regime the hidden registers range over V_reach(N, K):
- distinct net members generically give distinct branch matrices, so |V_reach| ≥ |N|;
- the capacity (K+1)log₂|V_reach| therefore grows at least like K·m d⁴ log(2K/ε).

The |N|-independent figure O(Kd² b + K log G) is a fixed-point property. In fixed point the TV budget acquires the
G1-dependent term c·K²C2^{−b}, and Kδ + K(m−1)/G + c·K²C2^{−b} ≤ ε fails at the stated δ and G. Statement (ii)'s
"≤ ε/2" has the same issue.

Fix: in the fixed-point version, split ε three ways: δ = ε/(3K), G = ⌈3K(m−1)/ε⌉, and b with ε/3, after G1 is repaired.
Otherwise, state the uniform theorem in the exact regime and remove the |N|-independence clause.

### G3. G = 0 when m = 1 (Main.md:554, :576)

G = ⌈2K(|O_max|−1)/ε⌉ is 0 for outcome-free families, and seeds on {0,…,−1} do not exist. Write
G = max(1, ⌈…⌉). This is harmless, but the formula as written fails.

### G4. The c₁K lower bound in clause (5) cites a floor for faithful realizations (Main.md:554)

"log₂|C_H| ≥ I* holds universally, for every faithful realization … For the constructed realization on those families,
c₁K ≤ log₂|C_H|." The constructed realization is not faithful (it is ε-approximate), so the cited floor does not apply
directly. A continuity (Fannes-type) argument would give only I* − O(ε log …). The inequality is true anyway, because
log₂|C_H| ≥ K log₂ G ≥ K for G ≥ 2. State that reason, or add the continuity step.

### G5 (I1). The Kochen–Specker sentence in clause (3) (Main.md:550) is overstated

"The outcome VALUES remain contextual — the only combination Kochen–Specker permits of any account reproducing these
statistics." KS forces contextuality only if three things hold: d ≥ 3, the family contains a KS-uncolourable set, and
the statistics are reproduced exactly.
- At d = 2 there are noncontextual models of projective measurements (Bell 1966; the Kochen–Specker qubit model).
- Families without a KS set admit noncontextual assignments.
- For ε-approximate statistics, which is what this theorem delivers, the finite-precision debate applies (Meyer 1999;
  Kent 1999; Clifton–Kent 2000; Barrett–Kent 2004). A robust noncontextuality inequality forces contextuality only
  below a threshold ε.

The constructed realization is contextual, since the outcome depends on the instrument's ordering of outcomes and on
the register. But "the only combination KS permits" is not proved in this scope. Narrow the sentence to: d ≥ 3, F
containing a KS set, and ε below a robust-inequality threshold. Or say only that the constructed realization is
outcome-contextual.

### G6. Re-padding in the single-dynamics Corollary (Main.md:560)

The argument "strip the appended outcome, recompute the control, undo the controlled step" proves injectivity on
well-formed states. Off that set, the separately padded φ_a can collide under different controls. Extend Φ from the
well-formed set to a bijection directly. This is trivial, but the text presents Φ as already bijective.

### Minor points (no change to validity)

- The clause-(5) count needs an empty-slot symbol, giving (|V_reach|+1).
- The per-step grid bound (|O|−1)/G is valid but loose by about 2. The sharp bound is ⌈(|O|−1)/2⌉/G. An exhaustive
  check gave a worst ratio of 0.875 (`exact_regime.py`).
- "The realized law is unchanged" by rescaling is exact only in the exact ring. In fixed point, rescaling changes later
  rounding digits. The Lemma's analysis does not depend on this, but the sentence overstates it.
- R ≤ |O_max|d² presumes minimal Kraus decompositions. The theorem allows arbitrary finite Kraus lists. Either restrict
  to minimal lists or define R as the count used.

---

## 4. Counterexample attempts and outcomes

| Attempt | Script | Outcome |
|---|---|---|
| Exact regime: 3-outcome instrument, two-Kraus mixed-conditional outcome, 3-4-5 and 5-12-13 rotations, outcome-free unitary, random adaptive protocols, K = 1..3, G ∈ {1..9, 16, 64}, rational non-diagonal ρ₀ (1980 runs) | `exact_regime.py` | 0 violations of TV ≤ K(\|O\|−1)/G; worst TV/bound 0.46 |
| Per-step grid lemma, exhaustive: \|O\| ≤ 4, G ≤ 12, all distributions with denominators ≤ 8 | `exact_regime.py` | Bound holds (strict when nonzero); worst 0.875 of the bound |
| Hermitian-input normalized kernel versus the claimed per-parent 4ηs + 8ν | `neg_parent.py`, `neg_parent4.py` | **Fails** at (d,R) = (3,9) and (4,16). Holds narrowly at (2,4). Negativity amplified ×4 at d = 2 |
| Same with multi-outcome random and balanced instruments, d = 2 | `neg_parent2.py`, `neg_parent3.py` | Clipping of negative-trace outcomes raises Q, so no per-parent violation at d = 2 |
| Reachability: do zero- or rare-probability outcomes produce negativity-dominated unclipped blocks at step 1? (d = 2, rank-one projectors, rational states and bases) | `zero_outcome.py`, `zero_outcome2.py` | None found. Max ‖C₋‖/Tr C = 0.618. A multi-step adversarial path is plausible but was not constructed |
| m = 1 (outcome-free only) | by inspection | G = 0: the formula is degenerate (G3) |
| K = 1; ε → 0; ε > 1 | by inspection | K = 1 is fine. As ε → 0, G, b and capacity grow as stated. For ε > 1 with K = 1, δ > ½ and the volumetric form exp(C m d⁴ log(1/δ)) goes vacuous or negative. WLOG ε ≤ 1 is needed and is used implicitly |
| Degenerate states (pure, zero-probability outcomes) | exact regime by analysis; fixed point by script | Exact regime: zero-probability outcomes get zero grid count, no issue. Fixed point: their noise blocks are where negativity enters (G1) |
| Adaptive and randomized protocols | by analysis and script | The chain rule and hybrid argument are fine. Randomized protocols follow by convexity |

---

## 5. Assumptions

**Mathematical:**
- finite d;
- finitely many outcomes, with a uniform bound m or |O_max|;
- finite horizon K;
- finite instrument family F, or a finite net for the uniform theorem;
- exact trace preservation of the instruments;
- TV on outcome sequences as the accuracy measure (post-measurement states and intervention labels are not compared);
- ε ≤ 1, used WLOG;
- in the fixed-point regime: round-to-nearest with absolute error ≤ 2^{−b}, upper-triangle Hermiticity, and a decidable
  trace-norm window rule.

**Resources supplied** (each is a choice in the construction, not a consequence of OI):
- a hidden branch register holding the unnormalized quantum density matrix: quantum theory enters as input;
- a predecessor stack of depth K, which carries reversibility;
- K pre-loaded uniform seeds;
- in the Corollary, a read-only program register carrying the whole protocol, exponential in K;
- for composites, a joint register (non-factorized hidden state);
- for the uniform theorem, a net whose description complexity scales as exp(m d⁴ log(K/ε)), deliberately excluded from
  "capacity".

**Access and control:**
- In the controlled model the agent is external. It chooses which bijection φ_a is applied at each step from the visible
  record. The instrument choice is not dynamics of the system.
- In the Corollary, the policy is part of the hidden initial condition, independent of the seeds and the register, so
  measurement independence holds by construction.
- A global step counter imposes one time order even on spacelike-separated local instruments.

**Prior:**
- The seed prior is uniform, so the probabilities are rational with denominator G^K. This choice, and not the
  mechanism, makes ε necessary at fixed F (see I2).

**Physical content:** the identification of "hidden sector" with a register that stores a quantum state, the external
agent, the global clock and the joint composite register. None of C1–C4 is checked for this realization, and none is
claimed.

---

## 6. Proof correctness and physical interpretation, kept separate

**What is proved mathematically.**
- (Exact regime, proved.) For every finite quantum experiment, and uniformly over all adaptive protocols, there is a
  finite reversible deterministic system with uniformly random pre-loaded seeds that reproduces every protocol's
  outcome-sequence law to TV K(|O|−1)/G. Each instrument is one fixed bijection, and gluing is exact.
- (Exact regime, proved.) For fixed (d, m, K, ε) one such system ε-approximates all continuum adaptive protocols, and
  everything it does is ε/2-close to quantum.
- (Proved.) Hence quantum operational theory at fixed (d, m) lies in the finite-test closure of finite reversible
  deterministic theories.
- (Not proved; plausible and repairable, G1.) The polynomial hidden-resource figures in the fixed-point regime.

**What the corpus reads into it, and whether the proof supports the reading.**
1. "Crosses most of the gap between Q_fb and operational quantum experiments … at finite resolution" (:562); "covers
   bounded quantum instrument envelopes to arbitrary requested finite accuracy" (:542); "the uniform continuum theorem
   gives arbitrary finite experimental accuracy" (:534). **Supported**, as statements about outcome statistics.
2. "Density, not identity" (:578, :580). **Supported and respected** at every site I read. Summary 4 correctly declines
   exact class identity at a fixed carrier.
3. Summary 4: "Per (3), density is the maximum" (I2). This is **mis-attributed for a fixed experiment**.
   - For a fixed finite F and K, the comb theorem (:460) realizes the whole action-labelled outcome family exactly,
     with a real-valued product prior u_c ∼ P(·|c), and with fixed per-action bijections.
   - The response-table construction and `S_imp_D` likewise realize any fixed finite law exactly.
   - ε is forced only by two things. One is the rational (sector-uniform) seed prior chosen here (cf. :496,
     "rationality tracks the prior"). The other is uniformity over the instrument continuum, for which the counting
     Proposition at :464 already suffices, and (3) is a stronger result than needed.
   - What the ε-form actually adds over the comb theorem is resource efficiency and uniformity. Its hidden state is
     polynomial in K, d and log(1/ε), against the comb's response table, which is exponential in K. Its mechanism
     computes the quantum update, so one system serves the continuum.
4. ":560 — 'One law, initial conditions vary — the substratum ontology stated as a theorem at finite resolution.'"
   **Not supported** as a physical reading. The theorem is an existence result for some reversible map. In kind it is
   the standard fact that a reversible machine with pre-loaded randomness (Bennett-style history tape) can simulate any
   finite stochastic computation, here applied to the Born-rule update. Its hidden variable is the digitized ψ/ρ. It
   uses none of the substratum's specific structure (lattice, C1–C4), and it places the experimenter's choices in the
   hidden initial data. It shows that the ontology is *not refuted* by finite-accuracy statistics. It does not show
   that the ontology is the one realized.
5. Substratum.md:482: "No finite-accuracy experiment contradicts this commitment by itself." **Supported**, with two
   caveats. The supporting realization is non-local for composites, since it uses a joint register and a global clock.
   And the hidden-memory requirement grows with K and log(1/ε).
6. :562's use of GR §3.3 to say the coherent/composite lift is "settled" on both its uniqueness and existence sides.
   No formal map is given from the gluing realization (a classical simulation) to GR's operational-theory
   characterization. The remark should read as "what remains is named by GR's conditions", not as a bridge theorem.

---

## 7. Bearing on the broader framework

- **Why the ε appears.** The ε-result is the first place where the rational, sector-uniform prior is load-bearing for a
  headline claim. Elsewhere the corpus allows real-valued fixed priors (:60, :460). If the framework's canonical measure
  (counting or invariant) is the intended reading, the ε is physical. If arbitrary fixed priors are allowed, fixed
  experiments are exact and only the uniform statement needs ε. Either way, the Introduction must say which.
- **Assumption-watch marker: nonlinear normalization of non-positive digitized states.** Any finite-precision simulator
  that clips and renormalizes a non-positive register amplifies negative mass by s/Q. Error ledgers that treat
  renormalization as "relabelling" undercount it. This applies to any other corpus claim that telescopes
  finite-precision cq errors.
- **Probe-to-claim mismatch.** The probe's ledger quantity is not the proof's quantity (check 16). This is an instance
  of the review rule against a control that does not measure the claimed object.
- **The capacity-floor citation pattern.** Citing faithful-realization floors for approximate realizations (G4) may
  recur elsewhere.
- **For the Introduction (abstract L12, §3.4 L126–L132).** Neither mentions the ε-result. If a statement is added, the
  licensed form is roughly:

  > For fixed system dimension d, outcome bound m, horizon K and accuracy ε, a single finite reversible deterministic
  > system, whose hidden state carries the unnormalized density matrix, a predecessor record and uniform random seeds,
  > reproduces the outcome-sequence law of every adaptive protocol of horizon K to total-variation distance ε. Its
  > hidden memory grows with K and log(1/ε). This is finite-test density, not identity: no fixed finite carrier
  > reproduces a qubit exactly (§3.4), and the same machinery realizes non-quantum instrument families.

  Until G1 is repaired, state the exact-arithmetic form, or omit explicit bit counts. It belongs in §3.4 as the
  positive counterpart of the obstruction. It must not be stated as a derivation of quantum mechanics, since quantum
  mechanics is the input.

---

## 8. Comparison with the audit's FINDINGS R-07

I wrote this section after the verdict above, and the verdict is unchanged. I read
`FINDINGS.md` R-07, at the audit worktree head `a44003a0`, file `FINDINGS.md:191–:216`.

**Where we agree.**
- No Lean kernel statement covers these results. They are proved on paper.
- The probes are instance evidence, not certification. R-07 notes that checks 1–9 compare TV in floating point with
  tolerances 1e-15 and 1e-12, and I agree. My point about check 16 is complementary: there the comparison is exact, but
  the quantity measured is not the proof's ν_t.
- It is density and not identity. Non-quantum families are realized too. A single autonomous dynamics needs a program
  register exponential in K. The initial state is fixed, and preparations enter as channels.
- R-07's proposed L130 text and abstract clause are supported by the exact-arithmetic regime, and they carry no bit
  counts. That is the form my §7 recommends while G1 is open.

**Where I disagree or would add.**
1. **"Digitized copy of the unnormalized quantum state".** In the proved regime, the exact one, the register holds the
   unnormalized state exactly over the instruments' entry ring. Only the outcome sampling is digitized, through the
   grid G. "Digitized" ties the sentence to the fixed-point regime, whose proof has gap G1.
   - Suggested wording: "a finite encoding of the unnormalized quantum state, updated exactly", or "the unnormalized
     quantum state, held exactly in a finite register".
2. **R-07 does not register G1.** The finite-precision half of clause (1), its explicit constants, and the resource
   figures that depend on it (linear-in-K capacity in fixed point; |N|-independent hidden capacity) are not proved as
   written. R-07's text happens to avoid them. Summary 4's "proved … AND at finite b" and the corpus mirrors that cite
   the capacity figures should still be corrected or qualified at source (Main.md:546, :554, :556, :576, :580). That is
   a corpus correction, outside the Introduction.
3. **R-07 does not register G2**, the regime mismatch in the uniform theorem's ε-budget and capacity claim. G3, G4 and
   G6 are also absent. They are minor.
4. **"At finite accuracy the realization direction holds … Classical action-labelled interventions are realized exactly
   by one fixed realization."** Placed side by side, these suggest that quantum experiments over a fixed finite family
   cannot be realized exactly. They can.
   - The outcome family of a fixed finite instrument set is itself a finite action-labelled family.
   - The comb theorem (Main.md:460) realizes it exactly with a real-valued product prior and fixed per-action
     bijections, and so does the response-table Extension (Main.md:498) that R-08 cites.
   - ε is forced only by two things: the rational uniform-seed presentation, and uniformity over the instrument
     continuum. For the second, the counting Proposition at Main.md:464 suffices.
   - What the ε-form adds is uniformity, and hidden memory polynomial in K, d and log(1/ε), where the response table
     is exponential in K.
   - Suggestion: replace "At finite accuracy the realization direction holds" with a sentence that puts the ε on the
     uniform, resource-efficient realization. For example: "For a fixed finite family the outcome law is realized
     exactly by the comb construction; a single realization that serves every instrument with at most m outcomes,
     with hidden memory polynomial in K and log(1/ε), reproduces all of them within ε."
5. **The abstract clause "every finite quantum experiment to any stated accuracy"** should keep the qualifiers that
   make it true: finite dimension, finitely many outcomes, finite horizon. "Finite quantum experiment" may be enough if
   §3.4 defines it. Its proposed position also needs care. Next to "exact finite operational quantum mechanics is
   characterized by five completion conditions", it should not read as a derivation of quantum mechanics: the
   realization takes the quantum update as input (my §6, item 4).
6. **R-07 does not touch the interpretive overreaches** inside Main itself: the Kochen–Specker sentence in clause (3)
   (I1), "the substratum ontology stated as a theorem" at :560 (I3), and the "Per (3)" attribution in Summary 4 (I2).
   They do not affect R-07's Introduction text, but they belong in the corpus-correction list.

**Net.** Subject to points 1, 4 and 5, R-07's proposed Introduction text is accurate. The audit has not found the
proof-level gaps G1 and G2. They need corpus corrections at Main.md:546–:580 whether or not R-07 lands.
