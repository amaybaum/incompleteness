# NOTES-O5 — KB-D: source it or close it

Thread `research/origin`, round 2, node O5. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1 ([K] kernel at L, [D] design module on a
dev branch, [W] written argument, [X] exact computation, [A] audited archive record, [L] literature named, not
checked here). Script: `experiments/o5_kbd.py` (decision rule fixed in the header before run 1; one pre-run edit
before any run, adding the normalization control the header names; run 1 green, `VERDICT NO-GO-ON-STATED-ACCESS`;
replay byte-identical). Design module: `OIBridge/OriginPassive.lean` on `dev-origin/passive` (§5).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it does more than restate
"KB-D is not in the stated access" (O2-KB): it must either derive KB-D from a named premise with its disguise
test, or locate the exact element of the access that excludes it, with the excluded alternatives closed by
exact instances.

## 0. Verdict

KB-D is **not sourced**. It splits into two parts, and the two parts have opposite fates:

- **KB-D1, the instrument** ("read the frame, re-randomize the memory") is the composite of the native Lüders
  readout with a forgetful map (discard the memory, attach a uniform one) — exactly, branch by branch [X D1].
  Available whenever the forgetful map is.
- **KB-D2, the exclusivity** (no passive repeatable readout of any partition is available on the reachable
  body) is what the toy bit's octahedron needs, and it is excluded on the stated access: one passive readout of
  any of the 14 nontrivial partitions of {0,1}², added to KB-D and the exchanges, makes every point mass
  reachable and the body the simplex [X A2, A4]. The kernel's native readout is the Lüders readout
  (`readout_is_localLuders` [K OperationalAssembly.lean:658]), passive and repeatable on the classical carrier;
  every `FiniteOperationalTheory` carries it (`readout_avail`, the structure field).

The **no-go** is the sharpened Lemma P (§1): passive repeatable readouts make every extreme state of the body
outcome-deterministic, hence (with separating translates) every extreme state a point mass — a simplex — so no
balanced pure state and no Discrete witness, whatever instruments are added. Of the four candidate sources:
(a) the memory bound FAILED (it restricts the observer's posteriors, not the frequencies; §2); (b) the kernel
recorder under a finite-memory bound FAILED (passive on the system, or erasure to a known value; §3); (c) Lüders
∘ forgetful map sources KB-D1 only (§4); (d) **symplectic couplings** force the KB-D form of the disturbance,
CONDITIONAL on unknown pointer conjugates, which is KB-D2 for the pointer (§4). Both outcomes are kept with
their evidence.

## 1. The no-go: sharpened Lemma P

**T1 (passive readouts are deterministic at extreme points; classical carrier).** Let K be a set of probability
vectors on a finite Ω and (C_i) cells of readouts whose native observation is passive and repeatable on K: at
every ω ∈ K whose cell mass m = ω(C_i) lies in (0, 1), ω = m·ω₀ + (1 − m)·ω₁ with ω₀, ω₁ ∈ K and ω₀(C_i) = 1.
Then (i) every extreme point of K has every cell mass in {0, 1}, so no extreme point is balanced; (ii) if the
cells separate the points of Ω, every extreme point of K is a point mass.
*Proof [W].* (i) An extreme ω with 0 < m < 1 lies in the open segment (ω₀, ω₁), so ω₀ = ω, so m = ω₀(C_i) = 1.
(ii) If two configurations x ≠ y carried positive mass, a cell containing x and not y would have mass strictly
between 0 and 1. ∎ Kernel-checked as a design module (§5): `lemmaP_extreme`, `extreme_cellMass_det`,
`extreme_not_balanced`, `pointMass_of_cells`, `extreme_pointMass_of_passive` [D].
Exact instances [X A1, A6]: the access (S₄, passive z) reaches 11 posteriors, all four point masses among them;
its body's extreme points are exactly the point masses, deterministic for all 15 partitions; the passive
decomposition exists at every reachable state for every partition. On the KB-D body the hypothesis fails exactly
where T1's conclusion fails: at x⁺ the only body state with z-mass 1 is z⁺, and 2x⁺ − z⁺ = (1/2, −1/2, 1, 0)
is not a state. Separation is needed: on the segment [z⁺, z⁻] the z-readout is passive and its extreme points
are deterministic but are not point masses.

**T1a (exclusivity; the stated access excludes KB-D's body).** With exchanges (all permutations of Ω) and any
one passive repeatable readout of any nontrivial partition, every point mass is reachable from the uniform seed,
so the body is the full simplex whatever further instruments — KB-D's included — are added [X A2, A4: 14/14
partitions]. The protocol that reaches the point mass is the kernel's own pure-seed derivation (read, correct by
feed-forward, forget the outcome; `pureSeedPrep_available_of_swap` [K OperationalAssembly.lean:675]) applied
to z and then, through the swap, to x: point mass (0, 0) with probability 1 and no persistent memory; the same
pattern with the KB-D readout ends in the pair state x⁺ [X A5]. KB-D's octahedron (7 posteriors: uniform and
six pair states; extreme points the pair states; x⁺ extreme and z-balanced; at x⁺ the z-readout repeatable and
not passive, observe-and-forget(x⁺) = uniform) needs every passive readout removed [X A3].
**Reading.** KB-D is not an addition to the stated access but the removal of its readout. In kernel terms,
KB-D2 contradicts `readout_avail` together with `readout_is_localLuders` for any theory whose reachable classical
states are separated by its exchanges.
**Status.** T1 CONDITIONAL ([W] + [X]; kernel-checked as a design module [D], green in workflow run 38090594001 at
dev commit aef5d446, not certified); T1a CONDITIONAL ([W] + [X]; the kernel facts it uses CERTIFIED at their lines).

## 2. Candidate (a): incompleteness read as a memory bound — FAILED

1. *Procedures.* Preparations are procedures whose records are kept by the protocol (OI-STAGE's P_n labels
   (σ, r) [A oistage §1.1]). With a one-bit memory and acceptance at the time — CNOT z→m, accept m = 0, swap,
   CNOT z→m, accept m = 0, swap — the point mass (0, 0) is prepared [X B1]. A memory bound does not restrict
   procedures.
2. *Embedded observer, no acceptance* (the observer's state is P(system | its memory)). Over all 8! = 40320
   bijections of (z, x, m) from unif(z, x) ⊗ [m = 0], 18432 give a point-mass posterior [X B2]: a memory bound
   limits the average information (one bit), not the support of a posterior. **With affine (linear) dynamics**
   — the 1344 elements of AGL(3, 2) — every posterior is uniform on a pair or on all of Ω, and all six pair
   states occur: memory bound + linear dynamics gives exactly the knowledge-balanced *posteriors* [X B2aff].
3. *But not the frequencies.* In that embedded affine world the owner's sandwich, with the path dephasing
   realized as a record into the observer's memory, has frequencies (given the preparation) 1 and 1, V = 0; the
   observer's memory-conditioned predictions are 1 and 1/2, and the 1/2 arises because the which-path record
   overwrites the preparation's record; with a fresh blank bit for the which-path record the prediction is 1
   [X B3]. This is O1-T7a's memory erasure in embedded form, not a disturbance of the system.
**Verdict.** FAILED as a source of KB-D. Recorded separately (NEW, O5-N2): the *epistemic* half of the toy bit
(knowledge-balanced posteriors) is supplied by a finite memory under linear dynamics; its *ontic* half (reading
disturbs the memory, which the witness measures) is not.

## 3. Candidate (b): the kernel recorder under a finite-memory bound — FAILED

The recorder `recordInstr` [K InternalObserver.lean:249] has branch a: X ↦ (Σ_b X_{(a,b),(a,b)}) E_{(a,a),(a,a)}
(`recordInstr_apply`). On the classical carrier [X C1]: written into a separate register it leaves the system's
marginal unchanged — its non-passivity (`recordInstr_not_passive` [K :290]) is the reset of its own register;
written into the memory x it sets x := z, and the posterior of outcome a is the point mass (a, a) — erasure to a
known value, so point masses are reachable and the body is the simplex (O1-T7a). Under a finite-memory bound the
register is reused, and its reset needs a reversible dilation [X C2]: among the 576 bijections of (z, x, r)
fixing z, none writes a perfect record into a register of unknown content (counting: four inputs, two outputs
with r = z), and the 16 that write a perfect record into a blank register all keep x as a known bijective
relabeling. "Perfect record and x re-randomized" needs a register with an unknown part coupled into x — the
structure of candidate (d).

## 4. Candidates (c) and (d)

**(c) Lüders ∘ forgetful map — sources KB-D1 only.** KB-D_z = forget_x ∘ Lüders_z, branch by branch, on all
reachable states [X D1]. The forgetful map is native to the kernel's operational structure (ancilla discard
`prepAvail_discard` [K OperationalAssembly.lean:649] with `discardWith` [K :515]; uniform attach
`prepAvail_uniform`, `uniformAttach` [K :492]) when the memory is an ancilla [W]. But the stated access keeps the
passive readout, so the body stays the simplex [X D2 = A2]. The instrument is sourced; the exclusivity is not.

**(d) Symplectic couplings — KB-D's form, CONDITIONAL.** The substratum's rule is second-order, reversible and
linear (Substratum.md:158, the wave equation), and a second-order linear update (v^{t−1}, v^t) ↦
(v^t, F v^t − v^{t−1}) is symplectic for ω = [[0, I], [−I, 0]] exactly when F is symmetric [W: MᵀJM =
[[0, I], [−I, F − Fᵀ]]], as the nearest-neighbour sum is. Take four bits (z, x, q, p): q a blank pointer, p its
conjugate, ω = zx′ + xz′ + qp′ + pq′ (mod 2). Among the affine bijections with z′ = z and a perfect record q′ = z
from q = 0 [X E1]: all 32 symplectic ones re-randomize x when p is uniform (the kickback x′ = x + p, Spekkens'
measurement), none keeps x; 128 non-symplectic ones keep x (the plain CNOT among them); with p known, x′ is a
known function of (z, x) for all. By hand [W]: ω(Me_q, Me_p) = 1 forces α b_p = 1, and ω(Me_z, Me_p) = 0 forces
a_p = b_p, so a_p = 1 — the record coupling's p-coefficient on x is 1.
*Disguise test.* No complex number, unitary or non-monomial operator: the premise passes syntactically. *But*
(i) it is a restriction of the stated access, not an addition: the plain CNOT is a permutation of
configurations, available under A2 (`bijectiveOperator`, the exchanges); (ii) it yields KB-D only with the
pointer's conjugate unknown, and on one elementary system the affine symplectic group of F₂² is all of S₄
(|ASp(2, F₂)| = 4·|SL(2, F₂)| = 24 [W]), so a passive readout of the pointer and its own symplectic swap reveal
the conjugate (T1a applied to the pointer). The unknown pointer conjugate is KB-D2 for the pointer.
**Status.** CONDITIONAL on SYMP (every coupling, the observer's included, symplectic) and UPC (pointer conjugates
unknown); UPC is circular as a source of KB-D2; SYMP is in tension with A2.

## 5. Kernel design module

`OIBridge/OriginPassive.lean` on `dev-origin/passive` at dev commit `aef5d446` (branched from `dev-origin/envelope`
@ `c3f7fbb2`; one import line added to the aggregator). Section A `lemmaP_extreme` (abstract Lemma P); Section B
`cellMass`, `extreme_cellMass_det`, `extreme_not_balanced`, `pointMass_of_cells`, `extreme_pointMass_of_passive`
(T1); Section C the finite-order step used by O6. Workflow run 38090594001 (`workflow_dispatch`, dispatch 1 of 3 this
round): Mathlib bridge Build completed successfully (3645 jobs), all eleven declarations on [propext,
Classical.choice, Quot.sound], two unused-section-variable linter warnings; release gate red only on `claims`,
`duplicate`, `lean-manuscript` (by construction), `lean-axioms` PASS (5882 named results, no sorry). Copied verbatim
to `lean/OriginPassive.lean` (blob `9ef2a18d`, sha256 `8fac1f7f…17bf978`). Design evidence, not certification.

## 6. Scope

- HO-3 v1 item 3 [W] (received; relied on for scope only): a construction from product registers with local
  readout and π × id token operations is Bell-local, so a KB-D toy built from such registers — Spekkens' toy
  theory is local [L] — would not reach the entangled sector of a candidate pair cone even if KB-D were sourced.
- T1 is a statement about bodies of classical states. It does not concern the matrix carrier, where O1-T3
  (monomiality) is the envelope.

## 7. Classification (§A.31)

- **NEW, O5-N1.** KB-D splits into an instrument (sourced: Lüders ∘ forgetful map) and an exclusivity (excluded:
  one passive readout of any partition restores the simplex, 14/14); the exclusivity contradicts the kernel's
  native readout. Hidden assumption exposed: "KB-D" as used in round 1 silently carried the removal of the
  native readout.
- **NEW, O5-N2.** A finite memory under linear dynamics supplies the knowledge-balanced posteriors (the toy bit's
  epistemic half) but not the disturbance the witness measures (frequencies V = 0; the memory-conditioned 1/2 is
  memory erasure).
- **NEW, O5-N3.** Symplectic couplings force the KB-D form of the disturbance (32/32), given unknown pointer
  conjugates; the substratum's second-order linear rule is symplectic. Assumption-watch marker: the premise
  pair SYMP + UPC is the narrowest classical premise found that yields KB-D's form; UPC is KB-D2 relocated.
- **ELABORATING, O5-E1.** T1, the sharpened Lemma P (deterministic extreme points; point masses under
  separation), with a design module.
- **CONFIRMING, O5-C1.** O1-T7a (memory erasure fakes the witness) recurs as B3; O2-KB's four closed sources.

## 8. The SRC side of HO-5's joint statement (if KB-D were SRC's source)

Script `experiments/o5_src.py` (decision rule in the header before run 1; two pre-run cleanups before any run — an
unused stub removed and one print expression simplified; run 1 `VERDICT SRC-KB-TOKEN-ONLY`; replay byte-identical).

**The premise SRC would be.** SRC_KB(J): on one token the configurations are {0,1}², every permutation of them is
available (A2, the exchanges), and the frame's native readout is the measure-and-re-prepare law KB-D with no passive
readout of any partition (KB-D2, exclusivity). Then J = `cyc3` [K KInfFoundations.lean:425, :427] is available on the
token: exactly one permutation of the four configurations induces cyc3 on the six pure states — σ fixes (0,0) and
cycles (0,1) → (1,0) → (1,1) — of order 3, acting as a rotation (determinant +1; a transposition acts as a
reflection, determinant −1) [X S1]; σ maps the pure frame state z⁺ to the pure balanced state x⁺, and the owner's
sandwich with σ, σ⁻¹ and the KB-D frame dephasing is exactly (1, 1/2) [X S2].

**Disguise test.** The operation σ is a permutation of configurations: monomial, no complex number, no unitary, no
non-monomial operator in its interface — it passes the owner's letter. The non-classical structure (balanced pure
states) is carried by KB-D2, an observation law, which (i) is not an addition to the stated access but the removal of
its native readout (O5-T1a), and (ii) does not reach the composite: every composite of such tokens built from product
registers with local readouts has |S_CHSH| ≤ 2 exactly (the 16 joint configurations, all setting pairs: max 2,
min −2) [X S3], whereas every candidate pair cone contains phiW with S = 14/5 (HO-3 v1 items 1–2, received; item 1's
identity CERTIFIED at CompositeDimension.lean:1220–1222, membership [W]; item 2 [X]). So SRC_KB(J) gives J on a token
but no composite that SPEC's target concerns. The continuous version (the re-preparing sphere tower of O6-I) is the
same in this respect: its single-token law is a local hidden-variable model, and a product-register composite is
Bell-local (HO-3 item 3 [W]).
**Status.** SRC_KB(J): CONDITIONAL on KB-D2 (exclusivity), which the stated access excludes; as a source for HO-5's
joint statement it is token-only. A source of SRC that could serve SPEC would have to come with a composite outside
product registers — the branch-(a) nonlocal response HO-3 names — which nothing in this thread sources.
