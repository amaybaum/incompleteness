# Node 7 (A2 track, node 2): does a principle stated in the corpus fix the size of the nonclassicality?

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This node
executes the frozen preregistration `PREREG.md` (sha256
`99834efa540bbf0d2f6cd84bc819daa71b7d612864775285785e033739ebd3bc`, committed alone at `73a27ba1`). Deviations are
recorded in `amendments/AMENDMENTS.md` (A-1 to A-10), each with its date, its reason and what was known when it was
written.

**Base.** Thread `research/missing-component-20261020`: preregistration at `73a27ba1`, reviewed head `112ea335`.
`main` = `0fb020c7`. `papers/`, `book/` and `verification/lean-mathlib/` are identical between them, so every corpus
line cited in PREREG holds.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (`probe/`, Python 3.13.16,
SymPy 1.14.0, `-I -B`, every probe run twice with byte-identical output); [NUM] floating-point evidence, never
evidence of exactness; [L] literature, cited from memory unless stated, not read in full; [rec] recorded in the cited
record, not re-derived.

**Owner's framing (2026-10-20).** The objective is to derive why observational limits applied to a single underlying
reality produce exactly quantum behaviour, rather than to make it one of many possible outcomes. A rigorous negative
result that identifies exactly which OI principle is insufficient is a valuable outcome.

**Productivity test (PREREG §7, fixed before the node).** The node is a gem iff a principle passes, or a principle
fails for an identified structural reason that propagates to N1–N3 of `mc-node6`.

***

## 0. Headline

1. **No principle the corpus states derives the quantum CHSH or POM boundary in the families and classes tested
   [EC, W].**
   - Seventeen OI readings were examined, plus the positive control. Fifteen are Failures:
     - twelve admit the PR box or the gbit. For L3-C this holds under one of its two readings; under the other, no
       member satisfies condition O;
     - two (HB-3α, HB-4) admit no nonlocal correlation in the long-edge and gate classes, while admitting the gbit by
       scenario silence;
     - one (L3-D) is Failure-as-stated.
   - Two are Parked: HB-3β and CL. PC-4b's POM part is also Parked, inside a Failure decided in CHSH.
   - The positive control PC-3b (the quantum set itself) passes, by construction. It is Reproduction.
   - Outcome (a) is established for no OI reading, in either scenario, and outcome (b) is not reached by any OI
     reading.
2. **Measure selection does not bound the magnitude on the architectures the §3.1 readings admit [EC].**
   - Every §3.1 reading that admits the counting measure on LE(1,1)'s hidden bit admits LE(1,1). That covers L3-0,
     L3-A, L3-B, L3-C under reading (α) of A-4 (whose prior is L3-A's), and L3-PR through L3-A. LE(1,1) is the PR box
     from the nonaffine gate r ^= a·b, with no control register (`mc-node6` B2).
   - LE(1,1)'s correlators are E(a, b) = (−1)^{ab} for every value of λ, so S_max = 4 under every prior on λ. The prior
     decides only operational no-signalling, which holds iff P(λ = 0) = 1/2. Each of the ten priors j/9 checked gives a
     signalling box; the counting measure gives the PR box.
   - On an architecture class containing this gate, no constraint on μ alone that admits the counting measure excludes
     the PR box. This applies `mc-node6` B2/N2 and Methodology.md:393 to every §3.1 reading: BORDERLINE under PREREG §7.
3. **H-Bell's curvature clause, in the readings decided, admits every preparation weight or none [EC, W].**
   - *HB-2, the corpus's sparse local diagnostic (SM.md:154).* It holds whatever w is, so it admits S_max = 4.
   - *HB-3α, the hop-metric mesoscopic Ollivier curvature.* At the long edge's endpoints κ(A,B) ≤ −5/4 at every
     mesoscopic radius δ ≥ 1 and every weight w ∈ (0, 1], under both weightings of amendment A-3. The reference value
     tends to 0.
   - *HB-4, Gromov–Hausdorff closeness.* The rescaled distance between the glued and the reference torus is at least
     3/8 − 1/(4L).
   - Under HB-3α and HB-4, for one preparation-indexed edge between antipodal wing sites, every admitted realization
     in LE and the gate class is edge-free and local (S_max ≤ 2). Local realizations that use the edge are excluded
     too (F(a, b, c) = a). In these readings H-Bell's clauses (i) and (iii) cannot hold together.
   - The cause is the hop metric of the support graph. An edge of any positive weight shortens d(A, B) from 3L/2 to 1,
     so these functionals jump at w = 0.
     - In option 2 the weight enters only through the measures, and κ(A, B) increases with w: as δ → ∞ it tends to −2
       at w = 1 and to −∞ for w < 1.
     - HB-4's distance does not depend on w.
     - No tolerance yields an interior band in either reading. With tolerance τ in the limit form, HB-3α admits {0},
       or {0, 1} once τ reaches 2; HB-4 admits {0} or every w.
   - HB-3β, the generator-based route the corpus names for clause (iii) (SM.md:150, route (A)), is Parked. These
     statements do not cover it, nor the "equivalent nonlocal response map" alternative of Main.md:392.
4. **The two families' quantum points differ in kind [EC, W].**
   - LE's only quantum member is w = 0 (control K-7). So the value 2√2 is reached in LE only by a post-quantum
     correlation.
   - DR(w), by contrast, equals a qubit with Lüders readouts for every w ≤ 1/√2 on the sequences of length ≤ 3 (K-11 at
     three weights; both laws are affine in w [W]). Its quantum boundary is the preparation condition 2w² ≤ 1, the
     Bloch ball.
   - In LE the weight w = k/n is a preparation property too, but the post-quantum value S = 4 needs no weight: it is
     set by the admitted gate. In DR the post-quantum region is reached only through the preparation weight.
5. **G6: none.** No OI reading passes, and PC-3b reproduces QM by construction.
6. **Productivity: gem, narrow, for §3.3 only** (the H-Bell readings, propagating to N2 and N3). §3.1 is BORDERLINE.
   The literal first clause is met only by PC-3b, which carries no information (amendment A-7). Overall: ELABORATING
   with CONFIRMING parts, no NEW item.

All verdicts are provisional on K-10 at n = 4, which runs in CI and needs owner approval (amendment A-2). No verdict is
decided through the K-10 reduction.

***

## 1. Controls (PREREG §5), run before any candidate

All checks are green, with 37 PASS and 0 FAIL in `p7.run1.out` and `p7.run2.out`, which are byte-identical. Verdicts
are computed from the measured clauses. Each candidate's verdict is printed only if its own checks pass (A-10). I-6's
gate held twice during development: K-7 failed because of a certifier bug (A-9), and later an own-check failure printed
L3-C's verdict as void (A-10).

| # | check | type | outcome |
|---|---|---|---|
| I-1 | PREREG digest equals the frozen digest; rule parameters printed with their digest before any candidate | must-hold | holds |
| K-1 | LE(n,k) under the counting measure = LE(w) with a structured prior = `p6.py`'s B2b box, with S = 2 + 2w at w ∈ {0, 1/5, 2/5, 1/2, 3/5, 1}. DR(n,k) = DR(w) = `p6.py`'s P5 law on all 14 sequences × 4 preparations, with POM = (1+w)/2 at w ∈ {1, 7/10, 1/2} | must-hold, three code paths | holds |
| LEARCH, DRARCH | every LE(n,k) with n ≤ 100 computed from the architecture: S_max = 2 + 2k/n, no-signalling. Every DR(n,k) with n ≤ 40: POM = (1 + k/n)/2 | must-hold | holds |
| K-2, K-3 | PR box, gbit, and LE(2,1) with S = 3, each excluded by K-P | must-fail | excluded |
| K-4 | toy bit: a counting-measure realization satisfying condition O equals the qubit's sequential Lüders record law on all 234 protocols. Delay line: equals a two-qubit projective protocol with SWAP (exact 4×4 density matrices) | must-hold | admitted |
| K-5 | C3: across 144 LE realizations the conditional-support bound on 2^I* is at most 4. An idle hidden register pads any realization without changing its law | countercontrol | vacuous |
| K-5b | patch budget (under 10³ bits against about 10^145); passive-observation obstruction (appendix-c:226 [rec]) | countercontrol | vacuous |
| K-P | PC-3b, the quantum set: passes the family stage, (a), (a-POM) and (b1); derived class Reproduction | positive control | passes |
| K-N1 to K-N6 | synthetic principles: K-N1 and K-N2 fail (i); K-N3 fails (ii-S) in both scenarios; K-N4 fails (iii); K-N5 passes the family stage and fails (F1) (it admits PR in 𝒜_CHSH); K-N6 passes (a) and (a-POM) and fails (b1) (it admits T1 = LE(5,2)) | checker controls | as expected |
| K-M4 | the reviewer's mutant m4 (L3-A admitting only k = 0): the derived labels change to under-generation (CHSH), so no over-generation verdict is printed | mutation control | caught |
| K-M2 | a candidate whose own check fails gets "void", no verdict | mutation control | caught |
| K-7 | LE is quantum only at w = 0: the exact perfect-correlation argument (if three correlators are ±1 the fourth equals their product) excludes every LE(n,k) with k ≥ 1, n ≤ 12 (all n [W]). T1: E = (1,1,1,1/5), S_max = 14/5 | must-hold | holds |
| K-8 | 𝒜_CHSH contains the PR/anti-PR point (an O-checked realization with λ ∈ ℤ₆₈) with correlators (12/17)(−1)^{ab}, zero marginals and entries in (1/68)ℤ. K-P admits it through the exact isotropic TLM condition. Each correlator is within ε/4 of 1/√2, and S_max = 48/17 is within ε of 2√2. The gate class reaches the same box at n = 34 (A-1) | must-hold | holds |
| K-9 | condition O (bijectivity on Ω, point-mass visible marginal, normalized prior): 416 realizations before the candidates, 2624 with the candidate measurements | must-hold | holds |
| K-10 | the 256-count and eight-coordinate forms of 𝒜_CHSH(n) are the same set: 16, 136 and 752 boxes at n = 1, 2, 3. [W] for all n, both directions: a uniform mixture of n response pairs has entries in (1/n)ℤ, and the class requires no-signalling; conversely, any box with entries in (1/n)ℤ is such a mixture (assign the n values of λ to outcomes one setting pair at a time), so a no-signalling one is in the class | must-hold | holds at n ≤ 3 and [W]; n = 4 pending (CI) |
| K-11 | K-P's POM witness ρ_x = ½(I + w((−1)^{x₀}Z + (−1)^{x₁}X)) equals DR(w) exactly on all 14 sequences × 4 preparations for w ∈ {0, 1/2, 12/17}. ρ₀₀ + ρ₁₁ = ρ₀₁ + ρ₁₀ | must-hold | holds |
| SOS | exact identity (1/√2)[(A₀ − (B₀+B₁)/√2)² + (A₁ − (B₀−B₁)/√2)²] = 2√2 − CHSH (SymPy, noncommutative) | must-hold | holds |
| I-17, I-2, I-4 | classifier precedence on five synthetic clause vectors; `law()` reads only (prior, steps, readout); no float constant or `float()` outside `num_*` functions (an AST scan) | must-hold | hold |

***

## 2. Candidates: clause outcomes and classification (§6 precedence, derived from the measurements)

Family-stage witnesses:
- the PR box is LE(1,1) (S_max = 4), and the gbit is DR(1,1) (POM = 1);
- (ii-S) is met by LE(12,5) (S = 17/6, within ε of 2√2) and by DR(17,12) (POM = 29/34, within ε/8);
- the classical controls LE(0), DR(0) and DR(1/2) are family members.

The delay line and the toy bit are admitted, wherever a candidate admits LE(0) and DR(0), through the K-4 realizations:
counting measure, one system, no long edge [W].

"Vacuous" below means the reading admits every family member. Each candidate's own checks are listed in `p7.py`'s
`candidates()`.

| candidate | CHSH: (i) / (ii-S) / (iii) | POM: (i) / (ii-S) / (iii) | class (derived) |
|---|---|---|---|
| L3-0 (realization datum, Main.md:60) | fail / holds / holds | fail / holds / holds | Failure: over-generation; vacuous |
| L3-A (counting measure) | fail / holds / holds | fail / holds / holds | Failure: over-generation |
| L3-B (record-conditioned) | fail / holds / holds | fail / holds / holds | Failure: over-generation |
| L3-C (orbit-invariant, cycle equilibrium) | (α): fail / holds / holds (LE(1,1), S_max = 4; (α)'s prior is L3-A's). (β): the invariant measure's visible marginal at the readout phase is not a point mass, so no LE member, w = 0 included, satisfies condition O: holds / fail / fail | as CHSH | Failure under both A-4 readings: over-generation (α); under-generation and classical exclusion (β) |
| L3-D (moment constraints) | not computed | not computed | Failure-as-stated (the constraint values are parameters OI does not fix) |
| L3-PR (partition-relativity) | as L3-A | as L3-A | Failure: over-generation (not independent of L3-A) |
| PC-1 (marginal consistency) | fail / holds / holds | fail / holds / holds | Failure: over-generation; vacuous |
| PC-2 (no-signalling form) | fail / holds / holds | fail / holds / holds | Failure: over-generation; vacuous on the families |
| PC-3a (Q_fb representability) | fail / holds / holds | fail / holds / holds | Failure: over-generation; vacuous |
| PC-3b (quantum set; K-P) | holds / holds (in 𝒜_CHSH) / holds | holds / holds / holds | Reproduction |
| PC-4a (nested reversibility, κ2-closed) | fail / holds / holds | fail / holds / holds | Failure: over-generation; vacuous |
| PC-4b (nested reversibility, the family's own accessible set) | readout reapplied to its own pointer allowed: fail / holds / holds; not allowed: holds / fail / fail | Parked (A-5) | Failure (CHSH): over-generation if a readout may be reapplied to its own pointer; classical exclusion if not (the A-5 choice); POM part Parked (A-5) |
| HB-1 (long edges, no-signalling, degree ≤ D) | fail / holds / holds | fail (silent) / holds / holds | Failure: over-generation; vacuous on the families |
| HB-2 (sparse diagnostic) | fail / holds / holds | fail (silent) / holds / holds | Failure: over-generation; vacuous on the families |
| HB-3α (hop-metric Ollivier stability) | holds / fail (family and gate class) / holds | fail (silent) / holds / holds | Failure: under-generation (CHSH); over-generation (POM) |
| HB-3β (Bakry–Émery) | — | — | Parked (the mesoscopic functional is undefined in the corpus) |
| HB-4 (GH closeness) | holds / fail (family and gate class) / holds | fail (silent) / holds / holds | Failure: under-generation (CHSH); over-generation (POM) |
| CL (Barandes–Hasan–Kagan causal locality) | — | — | Parked (definition not retrieved; arXiv unreachable at drafting and at execution) |

No candidate other than PC-3b passed the clauses of either scenario. So no follow-up ran for any OI reading, and no OI
reading reached outcome (b).

**Corpus searches behind L3-D and L3-PR (§A.19).**
- *L3-D.* `git grep -i -E "jaynes|moment constraint|maximum.entropy.*constraint|maximal-entropy.*subject to|expectation
  constraint"` over `papers/` and `book/` finds no constraint value for the measure selection. The only hit,
  Main.tex:1036, is the Jaynes–Cummings model, which is unrelated.
- *L3-PR.* `git grep -i -E "properties of the partition boundary|geometric and thermodynamic"` finds the lemma
  (Main.md:86; book ch01:79 and FULL.md:423) and its use for ħ and the horizon (GR.md:20, book ch07). Nothing fixes
  these properties for a Bell or prepare-and-measure architecture.

### 2.1 Outcomes (a) and (b), reported separately

| | CHSH (a) | POM (a-POM) | (b1) TLM | (b2) tilted CHSH | (b3) chained, three settings |
|---|---|---|---|---|---|
| every OI reading | not established (family stage fails) | not established | not reached | not reached | not reached |
| PC-3b (positive control) | established by construction: (F1) by the SOS witness, (ii-Q) at v = 12/17, (iii-𝒜) local boxes | established by construction: (F2) [L], (ii-Q-POM) by K-11, (iii-𝒜) [W] | holds by construction: T1 and every LE member with w > 0 excluded; on the grid instance n ≤ 12, 54 374 admitted boxes, none violating TLM in a [NUM] cross-check, and 26 000 undetermined (A-6) | holds by construction for the admitted (inner) set [L: Acín–Massar–Pironio]; maximizing boxes and NPA status not computed | incomplete: admitted maximum ≤ 3√3 [L: Wehner]. The best isotropic quantum point in the class has I₃ = 57/11 at n = 88, not within ε of 3√3. Non-isotropic points were not searched |

***

## 3. Branch nodes

### 3.1 L1: the measure readings of Lemma 3 (PREREG §3.1)

**Checks [EC].**
- *L3-A-priorfree.* LE(1,1) gives S_max = 4 at P(λ = 0) = j/9, j = 0, …, 9, and each of these ten boxes is
  signalling. P(λ = 0) = 1/2 gives the no-signalling PR box, which is LE(1,1) under the counting measure.
- *L3-C-readings.*
  - (α): the orbit-invariant prior on the protocol cycle (clock included), conditioned on the initial slice, gives
    exactly the counting-measure law for every LE(n,k) with n ≤ 12 and every DR(n,k) with n ≤ 4.
  - (β): the invariant measure at the readout phase has a visible marginal that is not a point mass. For LE(1,1) at
    a = b = 0 it is 2/5, 1/5, 1/5, 1/5 (review check `l3c.py`). Condition O fails for all 90 LE and 14 DR members
    computed.
  - For all n [W]: an orbit through a slice point with λ = 1 (LE), or with a nonzero pointer after one cycle (DR),
    carries another visible configuration at the readout phase.

**Verdict.** The §3.1 readings admit LE(1,1) whenever they admit the counting measure on its hidden bit. S_max = 4
holds for every prior, and the counting measure is the prior that makes the box no-signalling. A principle that
constrains only μ cannot exclude a box whose correlators do not depend on the hidden state. The magnitude on these
architectures is set by the admitted gate (`mc-node6` B2/N2). Methodology.md:393 already states that no-signalling
does not select the quantum set. BORDERLINE.

**Pressure test (§A.31).** The tension between Main.md:60 ("not a constraint on representations") and
Computation.md:120 ("excludes a planted-measure escape") does not matter: both readings fail at the same witness, and
that witness needs no planted measure.

### 3.2 L2: partition covariance (PREREG §3.2)

- PC-1 holds for every member computed (LE with n ≤ 12): an expected countercontrol, confirmed.
- PC-2 is operational no-signalling, which every LE member satisfies. CONFIRMING Methodology.md:393.
- PC-3a holds for every LE and DR member with n ≤ 3, through the realization's own permutation unitary
  (Main.md:82).
- PC-4a is vacuous: under κ2 every readout has an accessible inverse.
- PC-4b: if a readout may be reapplied to its own pointer (the choice A-5 names), every LE member is admitted.
  Otherwise no LE readout is invertible, and PC-4b excludes every LE member. Its POM part is Parked.

**Verdict.** In GPTs, reversibility constrains correlations because reversible transformations must preserve the
operational state space. In a κ1–κ4 realization every process is already a bijection, so nested-observer reversibility
constrains nothing unless the accessible set is restricted. When it is restricted, as in PC-4b's second reading, it
removes the classical models along with the rest. Record-only.

### 3.3 L3: H-Bell (PREREG §3.3), the decisive branch

**Scope.** One preparation-indexed edge {A, B} between antipodal sites of the periodic simple-cubic reference graph of
side L, realized by LE's gate r ^= a·b·[u < k] or by the gate class. G(ω) carries the edge iff the gate depends on a at
ω (Main.md:358). The "equivalent nonlocal response map" alternative of Main.md:392 is not tested.

- **HB-1 [EC].** For every LE(n,k) with n ≤ 12, Bob's readout step depends on Alice's setting (one long edge, added
  degree 1) iff k > 0, and the box is no-signalling. S_max = 4 at LE(1,1).
- **HB-2 [W, EC].** L_N·m_N/N ≤ P(6r_N + 1)³/L³ → 0 for every schedule r_N → ∞ with r_N/L → 0. Instances at r = 1:
  21/32, 5/18 and 63/512 at L = 4, 6, 8. The condition does not involve w.
- **HB-3α [EC, W].**
  - *Closed form.* Across the edge, every transport plan costs the same, so W1 = |ν⁺| + 2∫r_A dν⁺, valid when
    3L/2 ≥ 4δ + 1. It is affine in w; option 1 is w = 1.
  - At w = 1: W1 = 3(8δ³ + 4δ² + 4δ + 2)/(8δ³ + 16δ). Here W1 ≥ 9/4 ⟺ δ³ + 2δ² − 4δ + 1 ≥ 0, which is 0 at δ = 1
    and increasing for δ ≥ 1. As δ → ∞, W1 → 3 and κ(A,B) → −2. At finite δ, κ dips below −2 before the limit, for
    example −2.12 at δ = 5 (review check `hb3a_indep.py`).
  - As w → 0⁺: W1 = 1 + 2E r ≥ 19/7, and E r increases with δ. So W1 ≥ 9/4 for every δ ≥ 1 and w ∈ (0, 1], and
    κ(A,B) ≤ −5/4. For w < 1, κ → −∞.
  - The exact min-cost-flow W1 equals the closed form at L ∈ {6, 8, 10, 12}, δ ∈ {1, 2}, w ∈ {1/4, 1/2, 1}. The
    reviewer's independent network-simplex check agrees, including w = 1/100 and L = 14 at δ = 3.
  - The reference curvature on lattice edges is ≥ 0 at every L, exactly 0 for L ≥ 10, and 0 on ℤ³ [W]. The reference
    curvature of the pair (A,B) lies in [0, 4E r/(3L)] → 0.
  - *Supplementary, not decision-bearing* (`sup_hb3a_edge.py`). On the lattice edge (A, A+e₁) at the endpoint, the
    glued curvature at w = 1 is −11/56 at δ = 1 and −17/32 at δ = 2, at each of L = 10, 12, 14. At δ = 3 it is
    −2297/3080, −2367/3080 and −343/440 at L = 10, 12, 14: torus-size dependent, about −0.75 to −0.78. At w = 1/2 the
    values are about half.
  - *Verdict.* Only w = 0 is admitted in LE. In the gate class, a realization is admitted only if no control value of
    positive weight carries the edge (check `GATE`). The 128 edge-free slices have S_max ≤ 2. Of the slices with the
    edge, the nonaffine ones reach 4 and the 128 local ones (for example F(a, b, c) = a) are excluded too.
    (ii-S) fails: under-generation.
- **HB-4 [W, EC].**
  - *Lemma.* If a correspondence between X and Y has distortion < 2r, then rad Y ≤ rad X + 2r, and symmetrically.
    Hence |rad X − rad Y| ≤ 2 d_GH.
  - On the ℓ₁ torus d(z,A) + d(z,B) = 3L/2, so ecc_Y(A) ≤ (3L/2 + 1)/2, while rad X = 3L/2. Hence the rescaled
    d_GH ≥ 3/8 − 1/(4L).
  - Exact radii at L = 4, 6, 8, 10; the reviewer adds L = 12, with ecc_Y(A) = 9.
  - The distance does not depend on w. Same admitted set as HB-3α: under-generation. SM.md:150 already states that a
    macroscopically cheap preparation-indexed edge destroys Gromov–Hausdorff closeness: CONFIRMING.
- **HB-3β.** Parked (PREREG §3.3 rule; route (A) of SM.md:150 is unconstructed).

**Verdict.** In HB-2, HB-3α and HB-4 the functional is built on the hop metric of the prepared graph's support. That
metric is the same for every w > 0, because one edge shortens d(A, B) from 3L/2 to 1. So the readings decided admit
every weight (HB-2) or none (HB-3α, HB-4), and no tolerance gives an interior band. Under HB-3α and HB-4, H-Bell's
clauses (i) and (iii) (Substratum.md:132) cannot hold together for this edge. Only the sparse diagnostic HB-2 is
compatible, and SM.md:156 says it is not a convergence theorem.

**Pressure test (§A.31).** Could a weighting other than A-3's rescue HB-3α?
- The weighted random walk puts mass w/(6 + w) on B in m_A at δ = 1. It gives κ(A, B) = (2w − 12)/(6 + w) ∈
  (−2, −10/7] for w ∈ (0, 1] [EC, reviewer check `rw.py`].
- Any weighting that keeps the support's hop metric has d(A, B) = 1 for every w > 0, so it cannot approach the
  reference continuously as w → 0.
- In both computed weightings κ increases with w, so a tolerance admits the top of the weight range first. It yields
  no interior band.

### 3.4 L4: CL and the countercontrols

- **CL.** Parked: the definition was not retrieved.
- **C3, patch budget, passive observation.** All vacuous (K-5, K-5b).

***

## 4. Classification of the node's findings

| finding | class | why |
|---|---|---|
| measure-only principles admit the PR box on these architectures (§3.1) | BORDERLINE | applies `mc-node6` B2/N2 and Methodology.md:393; S_max = 4 for every prior, no-signalling only at the counting measure |
| HB-3α's endpoint curvature κ(A,B) ≤ −5/4 at every scale and weight (§3.3) | ELABORATING | an exact constant for a functional the corpus already treats as failed at the reference (SM.md:150, Main.md:394); SM.md:156 already flags endpoint curvature as uncontrolled |
| the same incompatibility under HB-4 | CONFIRMING | SM.md:150 states it |
| hop-metric support functionals are all-or-nothing in w for every tolerance | ELABORATING | N2, N3 |
| LE's only quantum member is w = 0; DR(w ≤ 1/√2) equals a qubit on the sequences checked (K-7, K-11) | ELABORATING | refines `mc-node6` N3: the families' quantum points differ in kind |
| partition covariance vacuous, equal to no-signalling, or excluding the classical models (§3.2) | CONFIRMING (Methodology.md:393), record-only | — |

***

## 5. Productivity verdict (PREREG §7, amendment A-7)

- *First clause, literal:* met by PC-3b, which passes as Reproduction with outcome (a). PC-3b is the quantum set, so
  the pass carries no information. It is not counted.
- *Second clause (§3.3):* under hop-metric functionals of the support graph, a long edge of any weight is excluded
  (HB-3α, HB-4) or admitted (HB-2), and no tolerance gives an interior band. The parameter-dependence branch through
  long edges (N2) is incompatible with hop-metric curvature or GH stability at every weight. These functionals cannot
  fix an interior magnitude (N3). Scope: the readings decided, and one edge between antipodal wing sites.
- *§3.1:* BORDERLINE. It applies `mc-node6` B2/N2 and Methodology.md:393.

**Gem: yes, narrow (§3.3 only).** Overall classification: ELABORATING with CONFIRMING parts; no NEW item.

**Answer to the node question.** No principle stated in the corpus, in the readings preregistered here, derives the
quantum boundary in the families and classes tested.
- Lemma 3's readings and partition covariance do not constrain the magnitude on these architectures. One reading of
  each excludes even the classical models: L3-C (β) and PC-4b's second reading.
- H-Bell's geometric clause, in each decidable reading, either does not constrain the magnitude (S up to 4) or excludes
  every long-edge correlation (S ≤ 2).
- The quantum values 2√2 and (1+1/√2)/2 are reached only by the positive control, which assumes the quantum set.

***

## 6. G6

None. The rule (PREREG §7) needs a principle that passes. No OI reading does, and PC-3b reproduces QM by construction.

***

## 7. Hidden-assumption markers

| # | assumption | where | finding | class |
|---|---|---|---|---|
| HA-7.1 | the size of the nonclassicality is a prior weight, so a measure principle could fix it | `mc-node6` §12, candidate list | S_max = 4 for every prior, but no-signalling only at the counting measure; the magnitude is fixed by the admitted gate (`mc-node6` B2) | BORDERLINE |
| HA-7.2 | matching the value 2√2 in a family shows a quantum correlation is reachable | `mc-node6` §12 (ii), N3 | LE at S = 2√2 is post-quantum; LE's only quantum member is w = 0 (K-7) | ELABORATING |
| HA-7.3 | the two families show "one convexity pattern in two settings" | `mc-node6` N3, L5 | DR(w ≤ 1/√2) equals a qubit on the sequences checked (K-11), with its boundary set by preparation purity; LE's post-quantum value needs no weight | ELABORATING |
| HA-7.4 | H-Bell's clause (iii) is compatible with clause (i) and open | Main.md:392, :394; Substratum.md:132 | under HB-3α and HB-4, for one edge between antipodal wings, they cannot hold together; only the sparse diagnostic is compatible; HB-3β and the response-map alternative untested | ELABORATING (HB-3α); CONFIRMING (HB-4) |
| HA-7.5 | nested-observer reversibility constrains correlations as it does in GPTs | PREREG PC-4 | vacuous under κ2; restricting the accessible set removes the classical models too | record-only |
| HA-7.6 | the tension between Main.md:60 and Computation.md:120 matters for the magnitude | §3.1 | both readings fail at the same witness | record-only |

Assumption-watch markers:
- **AW-MC7-1.** A magnitude claim tested on a family tests correlations, not only values (HA-7.2).
- **AW-MC7-2.** On architectures that include a response independent of the hidden state and nonaffine in the
  settings, a principle that constrains only the prior, and admits the counting measure, does not exclude the PR box.
- **AW-MC7-3.** A curvature or metric condition built on the hop metric of the prepared graph's support cannot confine
  the preparation weight to an interior value: the metric is the same for every w > 0, and in the readings decided no
  tolerance yields an interior band.

***

## 8. Not verified

- **K-10.** n = 4 is pending in CI with owner approval (A-2). The two-direction written argument (K-10 row) has been
  reviewed.
- **HB-3α.**
  - The limit statement rests on the closed form and its algebra [W]. It is checked by flow at L ∈ {6, 8, 10, 12} with
    δ ≤ 2, and by the reviewer at L = 14 with δ = 3. The closed form needs 3L/2 ≥ 4δ + 1.
  - Weightings beyond A-3's two options and the reviewer's random walk were not computed.
  - The supplementary edge curvature covers δ ≤ 3 only.
- **HB-4.** The radius argument is [W], with exact radii at even L from 4 to 12.
- **H-Bell scope.** One edge between antipodal wing sites. More edges, other placements and the "equivalent nonlocal
  response map" alternative (Main.md:392) are untested.
- **Parked parts.** HB-3β not evaluated; CL not formalized; PC-4b's POM part.
- **L3-C.** Computed for LE with n ≤ 12 and DR with n ≤ 4; [W] beyond. **L3-D** not computed (Failure-as-stated).
- **Other written arguments.**
  - Dense forms of (iii) are [W] (rational weights are dense), not computed.
  - The admission of the delay line and toy bit by each candidate is [W] from the K-4 realizations.
  - The admitted sets of PC-1, PC-3a and PC-4 beyond the measured n are [W].
- **DR as a qubit.** Equality is computed at three weights on the sequences of length ≤ 3. For all w ≤ 1/√2 it rests
  on [W]: each record probability is affine in w for both laws, because DR's preparation prior is affine in w and the
  qubit's initial Bloch vector is linear in w. Longer sequences were not checked.
- **Bijectivity on Ω.** Checked exhaustively for LE with n ≤ 12 and for the 2624 realizations in the O log. For all n
  it rests on the involution argument [W]. DR checked from the architecture for n ≤ 40, with the closed form beyond
  [W].
- **C3 (K-5)** checked on a sample of 144 realizations; all members by the padding argument [W].
- **Passive-observation vacuity (K-5b)** [rec], not computed.
- **TLM certification** is exact only for perfect correlations, isotropic zero-marginal correlators and local boxes
  (Fine's theorem [L]). Other zero-marginal points are "undetermined"; the grid instance cross-check is [NUM].
- **PC-3b's (b2)**: maximizing boxes not exhibited, NPA 1+AB status not computed. **(b3)**: the non-isotropic search
  was not run.
- **Literature not read in full:** Fine 1982; Spekkens et al. 2009; Tsirelson 1980; Landau 1988; Masanes 2003;
  Acín–Massar–Pironio 2012; Wehner 2006; Navascués–Pironio–Acín; Lin–Yau; Kelly et al.; van der Hoorn et al.;
  Barandes–Hasan–Kagan; Gross–Müller–Colbeck–Dahlsten.
- **Amendment timing** rests on the author's record; git does not confirm it (`amendments/AMENDMENTS.md`).

***

## 9. Files (`probe/`)

| file | role |
|---|---|
| `p7.py` | controls, mutation controls and static checks, then the candidate measurements and the derived verdicts, in PREREG §9 order; 37 checks |
| `p7.run1.out`, `p7.run2.out` | 37 PASS, 0 FAIL; byte-identical |
| `k10.py`, `k10.run{1,2}.out` | K-10 at n ≤ 3; byte-identical |
| `sup_hb3a_edge.py`, `sup_hb3a_edge.run{1,2}.out` | supplementary HB-3α edge curvature (not decision-bearing); byte-identical |
| `SHA256SUMS` | digests of the nine files above |
| `review/` | the reviewer's checks, copied unchanged (`hb3a_indep.py`, `hb4.py`, `l3c.py`, `priorfree.py`, `rw.py`), each run twice with byte-identical outputs, and `SHA256SUMS`. The mutants are not copied |

Run from `probe/`:
- `python3 -I -B p7.py` (SymPy; about one minute);
- `python3 -I -B k10.py`;
- `python3 -I -B sup_hb3a_edge.py p7.py`.

Run from `probe/review/`:
- `python3 -I -B hb3a_indep.py`, `python3 -I -B hb4.py` and `python3 -I -B rw.py .` (networkx 3.4.2 for the first and
  last);
- `python3 -I -B l3c.py ../p7.py` and `python3 -I -B priorfree.py ../p7.py`.

***

## 10. Proposed PLAN text

**Status bullet (after `mc-node6/`):**

> - **`mc-node7/`, A2 track node 2, does a principle stated in the corpus fix the size of the nonclassicality:
>   ELABORATING, [EC/W]. Preregistered at `73a27ba1`; amendments A-1 to A-10; independently reviewed.**
>   - Seventeen readings of Lemma 3's measure selection, partition covariance, H-Bell and Barandes–Hasan–Kagan causal
>     locality were tested on the long-edge and destructive-readout families under condition O (one substratum, one
>     bijective dynamics).
>   - None derives the quantum CHSH or POM boundary in the families and classes tested. Fifteen are Failures:
>     - twelve admit the PR box or the gbit (L3-C under one of its two readings; under the other, no member satisfies
>       condition O);
>     - two admit no nonlocal correlation in the long-edge and gate classes, while admitting the gbit by scenario
>       silence;
>     - one is Failure-as-stated.
>
>     Two are Parked (HB-3β, CL). The quantum set passes, as Reproduction by construction. Outcome (a) is not
>     established for any OI reading, and outcome (b) is not reached.
>   - On architectures that include the nonaffine gate r ^= a·b (`mc-node6` B2), no constraint on the prior that admits
>     the counting measure excludes the PR box. Its correlators do not depend on the hidden bit, and the prior decides
>     only operational no-signalling.
>   - H-Bell's clause (iii), in the readings decided and for one preparation-indexed edge between antipodal wings,
>     admits every weight (the sparse diagnostic) or none (endpoint hop-metric Ollivier curvature κ ≤ −5/4 at every
>     scale and weight; Gromov–Hausdorff distance ≥ 3/8 − 1/(4L)). The support graph's hop metric is the same for every
>     positive weight, and no tolerance yields an interior band. The generator-based route the corpus names for clause
>     (iii) is Parked.
>   - The long-edge family is quantum only at w = 0. The destructive-readout family equals a qubit with Lüders readouts
>     for w ≤ 1/√2 on the sequences checked.
>   - G6: none. Verdicts are provisional on K-10 at n = 4 (CI); no verdict is decided through K-10.

**Next node for the A2 track (proposed): does a limit on what an embedded observer's records carry, derived from OI's
premises, restrict the admitted response maps?**

> - *Question.* `mc-node7` found no corpus principle that fixes the magnitude in the readings tested. On its
>   architectures the magnitude is set by which response maps are admitted, not by the prior. Two literature principles
>   bound correlations without a quantum ingredient, and neither appears in the corpus:
>   - macroscopic locality: coarse-grained records of many copies admit a classical description. It is equivalent to
>     NPA level 1, which gives Tsirelson's bound and, for zero marginals, the TLM boundary, and is strictly larger than
>     the quantum set with nonzero marginals [L: Navascués–Wunderlich 2010];
>   - information causality: m transmitted bits give at most m bits of accessible information. It gives Tsirelson's
>     bound for CHSH, and its full correlation set is not known [L: Pawłowski et al. 2009].
>
>   Does either follow from OI's premises (finite resolution, Lemma 1; trace-out; C3; condition O) as a statement about
>   an embedded observer's records, with no free parameter? If so, which admitted response maps does it exclude?
> - *Decision rule.* `mc-node7`'s rule, unchanged: the family stage, the per-scenario follow-up, outcomes (a) and (b)
>   kept apart, condition O, and the same controls. Additions:
>   - a principle counts as an OI candidate only through a derivation from OI premises, preregistered with its steps; a
>     principle applied without one is external, and a pass is an external pass, never Emergence;
>   - the known [L] relations enter as controls, not expectations: macroscopic locality admits NPA-level-1 points
>     outside the quantum set, so it cannot establish (b2) alone; information causality's set is unknown, so its (b)
>     clauses are decided only by exact witnesses;
>   - the classification is computed from the measured clauses, with a mutation control.
> - *Productivity test.* Gem iff a derivation of either principle from OI premises is found, or the derivation fails
>   at an identified step that bears on N1–N3, such as a premise of the principle that OI's records do not supply.

***

## Review outcome

The independent review returned accept with notes, on head `112ea335`, where `mc-node7/` was byte-identical to the
working copy. The reviewer's checks (`hb3a_indep.py`, `hb4.py`, `l3c.py`, `priorfree.py`, `rw.py`) are copied unchanged
into `probe/review/`, each run twice with byte-identical outputs, with `SHA256SUMS`. The reviewer's mutants (m1 to m4)
are not copied. m1 and m3 were caught by the I-6 gate. m2 and m4 are now caught, by own-check gating (void) and by
derived verdicts (K-M4).

The corrections are applied in place above, and amendment A-10 records the probe changes. The pre-review text is not
kept here. Pre-review sha256s:
- `NODE.md`: `1d9b34665e1d7862bf3154a2268398202ac8c8bbd45f9f906b001275cd7ec39a`;
- `p7.py`: `f787b28deffa000ff1772922a895237741c57f2d593902173e0cc125bda95b6b`;
- `AMENDMENTS.md`: `695b97e92d3a01d44a5a9bc35e9ebc24984bd6080767eec0bfecdf54841869d3`.

| item | verdict | applied as |
|---|---|---|
| all 15 Failures and both Parked classifications | CONFIRMED | — |
| M1, the reason for H-Bell being "all-or-nothing" | CORRECTED | the cause is the hop metric of the support graph, the same for every w > 0; κ(A,B) increases with w; tolerances give {0} or {0, 1} (HB-3α) and {0} or every w (HB-4); random-walk weighting added (§0 item 3, §3.3, §4, §5, AW-MC7-3, PLAN) |
| M2, "PR box for every prior" | CORRECTED | S_max = 4 for every prior, no-signalling only at P(λ = 0) = 1/2; §3.1 BORDERLINE (§0 item 2, §3.1, §4, §5, HA-7.1, PLAN; probe check and message) |
| M3, verdict text not generated from measurements | CORRECTED | classes and sub-labels derived from the measured clauses; own-check gating; K-M4 and K-M2 added; everything rerun twice (A-10) |
| M4, L3-C (β) violates condition O | CORRECTED | (β) admits no member; L3-C is Failure under both readings (over-generation; under-generation and classical exclusion); the L3-C, gate and K-8 realizations go through the engine (K-9: 2624) |
| D1, classification | CORRECTED | HB-3α ELABORATING; no NEW item; gem narrow, §3.3 only. The LE/DR quantum-point finding is also ELABORATING, consistent with "no NEW item" |
| D2, scope of the H-Bell result | CORRECTED | HB-2, HB-3α and HB-4 only; one antipodal edge; the response-map alternative untested |
| D3, §A.34 overstatement | CORRECTED | "edge-free and local", with local edge-using realizations excluded (F = a; 128 such slices) |
| D4, PC-4b against A-5 | CORRECTED | two readings: over-generation or classical exclusion; POM part Parked |
| D5, amendments | CORRECTED | moved to `amendments/`; the timing limits stated; A-8's post-verdict L extension recorded; A-10 added |
| minor: δ = 3 edge values; algebraic closure; GH lemma; K-10 converse; the "dynamical" sentence; gbit admitted by the under-generators; scope of §5's answer; the L3-D and L3-PR searches; DR affinity | CORRECTED | applied in §0, §1, §2, §3.3, §5 and §8 |
| reviewer's text: κ range for the random walk | CORRECTED | the range is (−2, −10/7] for w ∈ (0, 1], since −2 is the w → 0 limit and is not attained |
| reviewer's text: tolerance threshold | CORRECTED | "{0, 1} once τ reaches 2 in the limit form". At finite δ, κ(w = 1) dips below −2 (−2.12 at δ = 5), so the threshold depends on how the limit is taken |
