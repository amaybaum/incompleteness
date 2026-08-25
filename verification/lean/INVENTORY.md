# b403 — LEAN-FULL step one: the formalization-target inventory and the dependency order (not Main-first)

Research-only; 3.0.0 untouched. Directed round (owner-requested first step of LEAN-FULL),
executed on the review side. Companion probe `probes_b403/b403_inventory_anchor_probe.py`
(AP1–AP4): every line-anchor cited below is machine-verified against the frozen corpus.

## 1. The ordering recommendation

**Not Main first.** Formalizability runs opposite to the papers' conceptual order. The
dependency graph and value-per-risk both say: **gate → bridge → SM structural chain → GR
finite algebra → Main last**, with Main contributing mostly *interface axioms* whose
justifications remain prose. Concretely:

**Step 0 (owner, one command, already queued):** `lean probes_b399/OI_B397_Pilot.lean`. The
L1 kernel check is the program's entry gate and has never run (fork casualty). No further
Lean files are authored ahead of this verdict — one unchecked file with a defined gate is a
pilot; a stack of them is a liability.

**Step 1 (this round, gate-independent):** this inventory. The audit's real trust boundary
is statement-faithfulness, so the first executable step is extracting and classifying every
claim with its Lean shape and dependencies — done below.

**Step 2 (L2, on gate-pass):** the Mathlib bridge file. Its centerpiece — the averaging /
character-orthogonality identity dim Fix = |G|⁻¹Σχ — discharges the pilot's one deferred
bridge (turning 72/288/144 into 3/12/6 with the (3,4,5) split) **and kernel-checks the
b402 regulator trap with the same machinery** (Sym²(ℝ⁴) fixed dims: H(4) → 1 vs native
96-element group → 2). One formalized identity closes the counting layer of b397 *and* the
load-bearing theorem of the current physics frontier. Also in L2: ZMod q instances making
the odd-q censuses corollaries of `trivial_connection`; `Matrix.PosSemidef`/Schur for b389.

**Steps 3–5:** the L3 ledger sweep and SM structural chain; then GR's finite algebra over
axiomatized interfaces; then Main's formalizable fragments. Out-of-scope items recorded.

## 2. Why Main last

Main's load-bearing content is the observer/characterization thesis: its mathematics leans
on ergodic hypotheses (ETH conditioning, [Main §3.4] via SM:292), operational measurement
independence ([Main §3.3]), and measure-theoretic arguments that enter Lean as *interfaces*,
not theorems — plus Tier-4 positioning material. Starting there maximizes friction and
minimizes kernel-checked yield. Main's role in LEAN-FULL: the axiom file (each interface
axiom named, stated, and justified by prose citation), authored *after* the algebra it feeds
exists.

## 3. The inventory

**L2 — bridge file (next Lean file, on gate-pass).**
(B1) Averaging identity dim Fix_G = |G|⁻¹Σ_g χ(g) for finite G on finite-dim ℚ/ℝ-spaces;
corollaries: b397 counts 3/12/6 + (3,4,5) split; **b402 trap dims 1 vs 2** (H(4) = 384
generated; native = 96). (B2) ZMod q instances: censuses for q ∈ {3,…,13} as corollaries.
(B3) b389 Schur/PosSemidef: ΔH⁽²⁾ ⪯ 0 under positive gap + the below-channel necessity
control. (B4) AddChar alignment of the pilot's Ch layer.

**L3 — ledger sweep (Tier 1, exact finite/algebraic; each: source → Lean shape).**
(S1) b317 B₆ realization — finite group action, `decide`-able. (S2) b379 block-uniqueness
scan — decidable enumeration over Hom-blocks. (S3) b383/b384 M*/Q± algebra + b387 hypercube
local rep — 16×16 over ℤ[i]; exact matrix identities. (S4) b388 exchange zeros, +1/12,
crossed +1/4 — exact rational arithmetic on 36-dim space. (S5) b385/b386 commutant dim-3 +
ε-alternation ⟺ [T,U] = 0 — branch-independent legs. (S6) b391 triple ensembles (exact
rational moments: bc / 0 / bc·p⁻¹) + adjoint mass law with 12/6/4 multiplicities. (S7) b393
evenness theorem + b394 per-channel-pair sharpening — determinant-conjugation identity over
a block-sign family. (S8) b395/b396 relative-generator-geometry invariance. (S9) **b401
boost-Ward residual = 2ωk_i(Z_s−Z_t)** — a polynomial identity; near-free in Lean; plus the
two-level counterexamples as existence statements. (S10) b400 one-particle boost commutator
identities (exact leg; the O(a²p²) defect stays numeric).

**SM structural chain (Tier 1 unless noted).**
(M1) SM:238 Theorem 1a — equivariant finite projection preserves spatial symmetry: pure
finite linear algebra ([U,R]=[P,R]=0 ⇒ block-commutation); direct. (M2) SM:282 Theorem 2 —
Susskind factorization D²st = −¼□lat: finite operator identity on the lattice; direct.
(M3) SM:296 Theorem 3 — center independence ⟺ staggered chiral symmetry: algebraic
equivalence; direct. (M4) SM:334 Theorem 5 — Schur ⇒ Σ = aP+bP+cP and generic stabilizer
U(3)×U(2)×U(1): Mathlib Schur + a genericity lemma. (M5) SM:667 Dynkin equality T₃=T₂=T₁
for fundamentals — finite rep computation. (M6) Theorem 7 (3,2,1) cubic-commutant
decomposition — the L2 machinery reused. (M7) SM:274 Theorem 1 / SM:312 Theorem 4 —
conditional branches: the algebraic legs formalize; the branch conditions are interfaces.
(M8) §6.5/SM:791 map material — pilot T1/T2 already cover the closure; the near-identity
pushforward claims are Tier 3.

**GR (finite algebra over interfaces).**
(G1) GR:64 detailed-balance ⇒ Gibbs on a connected transition graph — a clean finite Markov
lemma; direct Tier 1, and a genuinely nice early target. (G2) Wald contraction E:ε:ε = −2F
as finite multilinear algebra over an axiomatized tensor interface. (G3) dim ≤ 4 operator
census — finite enumeration over a declared basis. (G4) N⁴ = det C/ρ reconstruction algebra
— algebraic identities over interfaces. (G5) The continuum Einstein derivation and GR:541
H-Hawking conditional — Tier 2: interface-axiomatized statements only; Mathlib lacks
working-strength curvature (blocker on record).

**Main (last; mostly interfaces).**
(N1) Finite characterization-theorem fragments where definitions pin down — candidate
Tier 1 toys. (N2) ETH conditioning, operational independence, C2 necessity — Tier 2
interface axioms with prose justification. (N3) Convergence/positioning material — Tier 4,
out of scope, recorded.

**Out of scope (recorded):** the register items (facts about prose); production numerics
(HMC measurements; Lean certifies estimator algebra only); citation findings.

## 4. Protocol reminder

Statement-faithfulness review stays two-sided: whichever side authors a Lean file, the other
reviews that each statement renders the note's claim before the proof is trusted; statements
freeze at review, proofs stay repairable. Anchors in this inventory are probe-verified
(AP1–AP4). Next Lean authoring event: L2, immediately on a clean pilot kernel check. No
manuscript claim; 3.0.0 immutable.
