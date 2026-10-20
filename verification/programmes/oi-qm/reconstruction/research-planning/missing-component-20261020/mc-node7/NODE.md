# Node 7 (A2 track, node 2): does a principle stated in the corpus fix the size of the nonclassicality?

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This node
executes the frozen preregistration `PREREG.md` (sha256
`99834efa540bbf0d2f6cd84bc819daa71b7d612864775285785e033739ebd3bc`, committed alone at `73a27ba1`). Deviations are
recorded in `AMENDMENTS.md` (A-1 to A-9), each with its date, its reason and what was known when it was written.

**Base.** Thread `research/missing-component-20261020` at `73a27ba1`. `main` = `0fb020c7`. `papers/`, `book/` and
`verification/lean-mathlib/` are identical between the two, so every corpus line cited in PREREG holds.

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

1. **No principle the corpus states derives the quantum CHSH or POM boundary within the families tested
   [EC, W].**
   - Seventeen OI readings were examined, plus the positive control.
   - Fifteen are Failures. Twelve over-generate, admitting the PR box or the gbit. Two under-generate, admitting no
     nonlocal correlation at all. One (L3-D) is Failure-as-stated.
   - Two are Parked: HB-3β and CL. PC-4b's POM part is also Parked, inside a Failure decided in CHSH.
   - The positive control PC-3b (the quantum set itself) passes, by construction. It is Reproduction.
   - Outcome (a) is therefore established for no OI candidate, in either scenario, and outcome (b) is not reached by
     any OI candidate.
2. **Measure selection cannot bound the magnitude at all [EC].**
   - Every reading of Lemma 3 and the measure posit (L3-0, L3-A, L3-B, L3-C, and L3-PR through L3-A) admits LE(1,1),
     the PR box built from one deterministic nonaffine gate.
   - LE(1,1) reaches S_max = 4 for every prior on its hidden bit (check `L3-A-priorfree`). The responses do not depend
     on the prior, so the maximal violation is a property of the admitted dynamics, not of the measure.
   - This is the one property responsible for the failure of every §3.1 reading. That meets the bar PREREG §7 sets
     for this case, narrowly.
3. **H-Bell's curvature clause is all-or-nothing in the preparation weight [EC, W].**
   - *HB-2, the corpus's sparse local diagnostic (SM.md:154).* It holds whatever w is, so it admits S_max = 4.
   - *HB-3α, the hop-metric mesoscopic Ollivier curvature.* At the long edge's endpoints κ(A,B) ≤ −5/4 at every
     mesoscopic radius δ ≥ 1 and every weight w ∈ (0, 1], under both weightings of amendment A-3. The reference value
     tends to 0, so every w > 0 is excluded.
   - *HB-4, Gromov–Hausdorff closeness.* The rescaled distance between the glued and the reference torus is at least
     3/8 − 1/(4L).
   - Under HB-3α and HB-4, H-Bell's clauses (i) and (iii) cannot hold together for a long edge between the wings: the
     admitted realizations are exactly the local ones (S_max ≤ 2).
   - A zero-tolerance limit condition on prepared graphs cannot fix an interior magnitude. A bound strictly between 2
     and 4 would need a finite tolerance, which OI does not fix.
4. **The two families carry their nonclassicality differently [EC, W].**
   - LE's only quantum member is w = 0 (control K-7). So the value 2√2 is reached in LE only by a post-quantum
     correlation.
   - DR(w), by contrast, is exactly a qubit with Lüders readouts for every w ≤ 1/√2 (control K-11). Its quantum
     boundary is a preparation-purity condition, 2w² ≤ 1, the Bloch ball.
   - In LE the magnitude is dynamical; in DR it is a property of the preparation. This refines `mc-node6`'s reading
     of N3 as "one convexity pattern in two settings".
5. **G6: none.** No OI candidate passes, and PC-3b reproduces QM by construction.
6. **Productivity: gem, narrow,** on the second clause: items 2 and 3, propagating to N3 and N2. On the literal first
   clause PC-3b would also count, but that pass carries no information (amendment A-7).

All verdicts are provisional on K-10 at n = 4, which runs in CI and needs owner approval (amendment A-2). No clause in
this node is decided through the K-10 reduction.

***

## 1. Controls (PREREG §5), run before any candidate

All controls are green, with 30 PASS and 0 FAIL in `p7.run1.out` and `p7.run2.out`, which are byte-identical. I-6's
gate held during debugging: a certifier bug made K-7 fail, and every verdict was suppressed until the bug was fixed
(amendment A-9).

| # | check | type | outcome |
|---|---|---|---|
| I-1 | PREREG digest equals the frozen digest; rule parameters printed with their digest before any candidate | must-hold | holds |
| K-1 | LE(n,k) under the counting measure = LE(w) with a structured prior = `p6.py`'s B2b box, with S = 2 + 2w at w ∈ {0, 1/5, 2/5, 1/2, 3/5, 1}. DR(n,k) = DR(w) = `p6.py`'s P5 law on all 14 sequences × 4 preparations, with POM = (1+w)/2 at w ∈ {1, 7/10, 1/2} | must-hold, three code paths | holds |
| LEARCH, DRARCH | every LE(n,k) with n ≤ 100 computed from the architecture: S_max = 2 + 2k/n, no-signalling. Every DR(n,k) with n ≤ 40: POM = (1 + k/n)/2 | must-hold | holds |
| K-2 | PR box (S_max = 4) and gbit (POM = 1) excluded by K-P | must-fail | excluded |
| K-3 | LE(2,1), S = 3, excluded by K-P | must-fail | excluded |
| K-4 | toy bit: a counting-measure realization satisfying condition O equals the qubit's sequential Lüders record law on all 234 protocols. Delay line: equals a two-qubit projective protocol with SWAP (exact 4×4 density matrices) | must-hold | admitted |
| K-5 | C3: across 144 LE realizations the conditional-support bound on 2^I* is at most 4 and no hidden padding is needed. An idle hidden register pads any realization without changing its law, so C3 admits every member | countercontrol | vacuous |
| K-5b | patch budget (realizations use under 10³ bits against about 10^145) and the passive-observation obstruction (appendix-c:226 [rec]) | countercontrol | vacuous |
| K-P | PC-3b, the quantum set: passes the family stage, (a), (a-POM) and (b1) | positive control | passes; Reproduction |
| K-N1 | "S_max ≤ 3, POM ≤ 7/8" | must fail (i) | fails (i), witness LE(2,1) |
| K-N2 | "w ≤ 1/2 in LE, w ≤ 1/√2 in DR" | must fail (i) | fails (i) |
| K-N3 | "S_max ≤ 2, POM ≤ 3/4, everywhere" | must fail (ii-S), both scenarios | fails (ii-S), CHSH and POM |
| K-N4 | "1/4 ≤ w ≤ √2 − 1 in LE, 1/2 ≤ w ≤ 1/√2 in DR" | must fail (iii) | fails (iii) |
| K-N5 | LE restricted to S ≤ 2√2, DR as K-P, 𝒜_CHSH unrestricted | passes the family stage, must fail (F1) | passes family (witness LE(17,7)); admits PR in 𝒜_CHSH; fails (F1) |
| K-N6 | "S_max ≤ 2√2 on every admitted box; POM as K-P" | must pass (a), (a-POM), fail (b1) | passes; admits T1 = LE(5,2); fails (b1) |
| K-7 | LE is quantum only at w = 0: the exact perfect-correlation argument excludes every LE(n,k) with k ≥ 1, n ≤ 12 (all n [W]). T1: E = (1,1,1,1/5), S_max = 14/5 | must-hold | holds |
| K-8 | 𝒜_CHSH contains the PR/anti-PR point with correlators (12/17)(−1)^{ab}, zero marginals and entries in (1/68)ℤ. K-P admits it through the exact isotropic TLM condition. Each correlator is within ε/4 of 1/√2, and S_max = 48/17 is within ε of 2√2. The gate class reaches the same box at n = 34 (amendment A-1) | must-hold | holds |
| K-9 | condition O (bijectivity on Ω, point-mass visible marginal, normalized prior) for all 404 realizations checked | must-hold | holds |
| K-10 | the 256-count and eight-coordinate forms of 𝒜_CHSH(n) are the same set: 16, 136 and 752 boxes at n = 1, 2, 3 (`k10.run*.out`). [W] for all n: any box with entries in (1/n)ℤ is a uniform mixture of n deterministic response pairs, assigning the n values of λ to outcomes one setting pair at a time | must-hold | holds at n ≤ 3 and [W]; n = 4 pending (CI) |
| K-11 | K-P's POM witness ρ_x = ½(I + w((−1)^{x₀}Z + (−1)^{x₁}X)) equals DR(w) exactly on all 14 sequences × 4 preparations for w ∈ {0, 1/2, 12/17}. ρ₀₀ + ρ₁₁ = ρ₀₁ + ρ₁₀ | must-hold | holds |
| SOS | exact identity (1/√2)[(A₀ − (B₀+B₁)/√2)² + (A₁ − (B₀−B₁)/√2)²] = 2√2 − CHSH (SymPy, noncommutative): the outer-set witness K-P uses | must-hold | holds |
| I-17 | classifier precedence on five synthetic clause vectors, Emergence included | must-hold | holds |
| I-2, I-4 static | `law()` reads only (prior, steps, readout). No float constant or `float()` outside `num_*` functions (an AST scan) | must-hold | holds |

***

## 2. Candidates: clause outcomes and classification (§6 precedence)

Family-stage witnesses:
- the PR box is LE(1,1) (S_max = 4), and the gbit is DR(1,1) (POM = 1);
- (ii-S) is met by LE(12,5) (S = 17/6, within ε of 2√2) and by DR(17,12) (POM = 29/34, within ε/8);
- the classical controls LE(0) and DR(0), DR(1/2) are family members.

The delay line and the toy bit are admitted by every candidate through the K-4 realizations: counting measure, one
system, no long edge [W].

| candidate | CHSH: (i) / (ii-S) / (iii) | POM: (i) / (ii-S) / (iii) | class |
|---|---|---|---|
| L3-0 (realization datum, Main.md:60) | fail / holds / holds | fail / holds / holds | Failure (over-generation; vacuous) |
| L3-A (counting measure) | fail / holds / holds | fail / holds / holds | Failure (over-generation) |
| L3-B (record-conditioned) | fail / holds / holds | fail / holds / holds | Failure (over-generation) |
| L3-C (orbit-invariant, cycle equilibrium) | fail under both A-4 readings (LE(1,1): S_max = 4 under (α), 3 under (β)) / holds / holds | fail / holds / holds | Failure (over-generation) |
| L3-D (moment constraints) | not computed | not computed | Failure (Failure-as-stated: the constraint values are parameters OI does not fix) |
| L3-PR (partition-relativity) | as L3-A | as L3-A | Failure (over-generation; not independent of L3-A) |
| PC-1 (marginal consistency) | fail / holds / holds | fail / holds / holds | Failure (over-generation; vacuous, as expected) |
| PC-2 (no-signalling form) | fail / holds / holds | fail / holds / holds | Failure (over-generation) |
| PC-3a (Q_fb representability) | fail / holds / holds | fail / holds / holds | Failure (over-generation; vacuous) |
| PC-3b (quantum set; K-P) | holds / holds (in 𝒜_CHSH) / holds | holds / holds / holds | Reproduction |
| PC-4a (nested reversibility, κ2-closed) | fail / holds / holds | fail / holds / holds | Failure (over-generation; vacuous) |
| PC-4b (nested reversibility, family's own accessible set) | fail / holds / holds | Parked (A-5) | Failure (over-generation, CHSH) |
| HB-1 (long edges, no-signalling, degree ≤ D) | fail / holds / holds | fail (silent) / holds / holds | Failure (over-generation) |
| HB-2 (sparse diagnostic) | fail / holds / holds | fail (silent) | Failure (over-generation) |
| HB-3α (hop-metric Ollivier stability) | holds / fail (family and gate class) / holds | fail (silent) | Failure (under-generation, CHSH; over-generation, POM) |
| HB-3β (Bakry–Émery) | — | — | Parked (the mesoscopic functional is undefined in the corpus) |
| HB-4 (GH closeness) | holds / fail (family and gate class) / holds | fail (silent) | Failure (under-generation, CHSH; over-generation, POM) |
| CL (Barandes–Hasan–Kagan causal locality) | — | — | Parked (definition not retrieved; arXiv unreachable at drafting and at execution) |

No candidate other than PC-3b passed the clauses of either scenario. So no follow-up ran for any OI candidate, and no
OI candidate reached outcome (b).

### 2.1 Outcomes (a) and (b), reported separately

| | CHSH (a) | POM (a-POM) | (b1) TLM | (b2) tilted CHSH | (b3) chained, three settings |
|---|---|---|---|---|---|
| every OI candidate | not established (family stage fails) | not established | not reached | not reached | not reached |
| PC-3b (positive control) | established by construction: (F1) by the SOS witness, (ii-Q) at v = 12/17, (iii-𝒜) local boxes | established by construction: (F2) [L], (ii-Q-POM) by K-11, (iii-𝒜) [W] | holds by construction: T1 and every LE member with w > 0 excluded; on the grid instance n ≤ 12, 54 374 admitted boxes, none violating TLM in a [NUM] cross-check, and 26 000 undetermined (A-6) | holds by construction for the admitted (inner) set [L: Acín–Massar–Pironio]; maximizing boxes and NPA status not computed | incomplete: admitted maximum ≤ 3√3 [L: Wehner]. The best isotropic quantum point in the class has I₃ = 57/11 at n = 88, not within ε of 3√3. Non-isotropic points were not searched, so (b3) is not established |

***

## 3. Branch nodes

### 3.1 L1: the measure readings of Lemma 3 (§3.1 of PREREG)

**Check [EC].**
- Every §3.1 reading that admits counting-measure architectures admits LE(1,1). That is B2's gate with its control
  register removed: r ^= a·b.
- LE(1,1) has S_max = 4 for P(λ = 0) = j/9, j = 0, …, 9.
- L3-C's orbit-invariant prior was computed on the protocol cycle with the clock included, for LE(n,k) with
  (n,k) ∈ {(1,1), (2,1), (3,2), (4,4)}:
  - reading (α), one pass from the slice, reproduces the counting measure on the slice;
  - reading (β), stationary readout-phase statistics, gives S_max = 3 at LE(1,1);
  - both exceed 2√2 + ε, so the A-4 choice does not affect the verdict.

**Verdict.** A principle that constrains only μ admits S_max = 4 whenever the admitted architectures include a
response that does not depend on the prior and is nonaffine in the settings (`mc-node6` B1a, N2). Threshold registers
then make the weights dense in [0, 1] as well (`mc-node6` §12). The magnitude of nonclassicality, for CHSH, is fixed by
the admitted response maps, not by the measure.

**Pressure test (§A.31).** The tension between Main.md:60 ("not a constraint on representations") and
Computation.md:120 ("excludes a planted-measure escape") does not matter here: both readings fail at the same witness,
which needs no planted measure.

### 3.2 L2: partition covariance (§3.2 of PREREG)

- PC-1 holds for every realization: the joint law of V_A ∪ V_B marginalizes to each wing's law, checked [EC]. It is
  an expected countercontrol, confirmed.
- PC-2 is operational no-signalling, which every LE member satisfies. It admits PR, as Methodology.md:393 already
  states. CONFIRMING.
- PC-3a holds for every realization: the realization's own permutation unitary, with ρ = diag(μ) and fixed-basis Born
  readout, reproduces LE(1,1) and DR(1,1) exactly [EC].
- PC-4a is vacuous. Under κ2 the inverse of each readout bijection is accessible and restores the pre-readout law
  [EC].
- PC-4b admits LE(1,1), because LE's readouts are self-inverse [EC]. Its POM part is Parked (A-5).

**Verdict.** The structural reason is reversibility at the ontic level. In GPTs, reversibility constrains correlations
because reversible transformations must preserve the operational state space. In a κ1–κ4 realization every process is
already a bijection with an accessible inverse, so nested-observer reversibility constrains nothing unless the
accessible set is restricted. A restricted accessible set is an architectural choice (`mc-node6` A3). Record-only.

### 3.3 L3: H-Bell (§3.3 of PREREG), the decisive branch

**Embedding.** LE's gate r ^= a·b·[u < k] is the preparation-indexed edge {A, B} between antipodal sites of the
periodic simple-cubic reference graph of side L. The prepared graph G(ω) carries the edge iff [u < k] = 1.

- **HB-1 [EC].** LE(1,1) has one long edge (added degree 1, so D = 1 already admits it), ontic parameter dependence
  and operational no-signalling. S_max = 4.
- **HB-2 [W, EC].** With P long edges, L_N·m_N/N ≤ P(6r_N + 1)³/L³ → 0 for every schedule r_N → ∞ with r_N/L → 0,
  because m_N ≤ |ℓ₁ ball of radius 3r_N| ≤ (6r_N + 1)³. Instances at r = 1: L_N m_N/N = 21/32, 5/18 and 63/512 at
  L = 4, 6, 8. The condition does not involve w, so HB-2 admits LE(1,1).
- **HB-3α [EC, W].**
  - On the glued graph, the signed difference of the two ball measures at the endpoints of {A, B} has its positive
    part around A and its negative part around B. Every path between those regions crosses the edge, so every
    transport plan costs the same: W1 = |ν⁺| + 2∫r_A dν⁺. This holds whenever 3L/2 ≥ 4δ + 1.
  - Option 1 (uniform balls of the support graph) is the w = 1 case of option 2 (the ensemble mixture), and W1 is
    affine in w.
  - At w = 1: W1 = 9/4, 45/16, 187/60 at δ = 1, 2, 5, and W1 → 3, so κ(A,B) → −2. At w < 1 the term
    (1 − w)(1 + 2E r) grows like (3/2)(1 − w)δ, so κ → −∞.
  - For every δ ≥ 1 and every w ∈ (0, 1], W1 ≥ 9/4, so κ(A,B) ≤ −5/4.
  - The exact min-cost-flow W1 equals the closed form at every instance with L ∈ {6, 8, 10, 12}, δ ∈ {1, 2} and
    w ∈ {1/4, 1/2, 1}.
  - The reference curvature on lattice edges is ≥ 0 at every L, exactly 0 for L ≥ 10, and 0 on ℤ³ [W]. The reference
    curvature of the pair (A,B) lies in [0, 4E r/(3L)] → 0.
  - Supplementary, not decision-bearing (`sup_hb3a_edge.py`): on the ordinary lattice edge (A, A+e₁) at the endpoint,
    the glued curvature is −11/56, −17/32 and about −0.78 at δ = 1, 2, 3 for w = 1, and about half that at w = 1/2,
    the same at L = 10, 12, 14. The failure is not confined to the long-edge pair.
  - Verdict: only w = 0 is admitted in LE. In the gate class only realizations with no edge at any control value of
    positive weight are admitted. These are local: all 128 edge-free slices have S_max ≤ 2, while slices with the
    edge reach 4 (check `GATE`). (ii-S) fails: under-generation.
- **HB-4 [W, EC].** |rad X − rad Y| ≤ 2 d_GH. On the ℓ₁ torus d(z,A) + d(z,B) = 3L/2, so
  ecc_Y(A) ≤ (3L/2 + 1)/2, while rad X = 3L/2. Hence the rescaled d_GH ≥ 3/8 − 1/(4L), with exact radii at
  L = 4, 6, 8, 10. Same admitted set as HB-3α: under-generation. SM.md:150 already states that a macroscopically cheap
  preparation-indexed edge destroys Gromov–Hausdorff closeness: CONFIRMING.
- **HB-3β.** Parked. The rule in PREREG §3.3 applies: a mesoscopic Bakry–Émery functional needs a scale and an
  averaging that the corpus does not define (route (A) of SM.md:150 is unconstructed).

**Verdict.** Every reading of H-Bell's clause (iii) that this node could decide is evaluated on the support of the
prepared graph, or depends on w only through a mixture whose limit condition has zero tolerance. Either it is blind to
the edge (HB-2, S_max = 4) or it forbids it (HB-3α, HB-4, S_max ≤ 2). No reading constrains w to an interior value.
Under HB-3α and HB-4, clauses (i) and (iii) of H-Bell (Substratum.md:132) are jointly unsatisfiable for a long edge
between the wings. Only the sparse diagnostic HB-2 is compatible, and SM.md:156 says it is not a convergence theorem.

**Pressure test (§A.31).** Could a weighting other than A-3's options rescue HB-3α? A weighted random-walk measure
puts mass of order w across the edge, which leaves an O(1) imbalance across a bottleneck of length growing with the
walk's spread. By that [W] it does not converge to 0 either, but it was not computed. A finite tolerance would admit
w up to tolerance/constant. That is the parameter PREREG §3 disqualifies.

### 3.4 L4: CL and the countercontrols

- **CL.** Parked: the definition was not retrieved.
- **C3, patch budget, passive observation.** All vacuous, as preregistered (K-5, K-5b).

***

## 4. Classification of the node's findings

| finding | class | why |
|---|---|---|
| measure-only principles cannot bound the CHSH magnitude: LE(1,1) reaches 4 for every prior (§3.1) | ELABORATING; meets PREREG §7's bar narrowly | `mc-node6` §12 framed the magnitude as a prior weight. This identifies the single property behind the failure of every §3.1 reading |
| H-Bell's clause (iii) under HB-3α is incompatible with clause (i): κ(A,B) ≤ −5/4 at every scale and weight (§3.3) | NEW, narrow | an exact closed form for the corpus's named functional at the defect. The corpus treats H-Bell as open (Main.md:394, Substratum.md:132) |
| the same incompatibility under HB-4 | CONFIRMING | SM.md:150 states it |
| zero-tolerance geometric conditions are all-or-nothing in w | ELABORATING | propagates to N3 |
| LE's only quantum member is w = 0; DR(w ≤ 1/√2) is exactly a qubit (K-7, K-11) | NEW, narrow (found at preregistration review, confirmed here) | refines `mc-node6` N3: the families' quantum points differ in kind |
| partition covariance vacuous or equal to no-signalling (§3.2) | CONFIRMING (Methodology.md:393), record-only | — |

***

## 5. Productivity verdict (PREREG §7, amendment A-7)

- *First clause, literal:* met by PC-3b, which passes as Reproduction with outcome (a). PC-3b is the quantum set, so
  the pass is guaranteed by construction and carries no information. It is not counted.
- *Second clause:* met, narrowly, by two failures with identified structural reasons that propagate.
  - *§3.1, to N3.* A magnitude-fixing principle must restrict the admitted response maps (the dynamics), not the
    measure. This is strictly stronger than `mc-node6` §12's record ("weights fixed by architecture, rational"),
    because the PR value needs no weight at all.
  - *§3.3, to N3 and N2.* A zero-tolerance limit condition on preparation-indexed graphs cannot fix an interior
    magnitude. Under HB-3α and HB-4 the parameter-dependence branch through long edges is incompatible with metric or
    curvature stability.

**Gem: yes, narrow.** Overall classification: ELABORATING, with one NEW (narrow) item (the HB-3α incompatibility) and
CONFIRMING parts.

**Answer to the node question.** No principle stated in the corpus, in the readings preregistered here, derives the
quantum boundary. Lemma 3 and partition covariance do not constrain the magnitude at all. H-Bell's geometric clause,
in each decidable reading, either does not constrain it (S up to 4) or excludes all nonlocality (S ≤ 2). The quantum
values 2√2 and (1+1/√2)/2 are reached only by the positive control, which assumes the quantum set. Exactly which OI
principles are insufficient, and why, is stated in §3.

***

## 6. G6

None. The rule (PREREG §7) needs a principle that passes. No OI candidate does, and PC-3b reproduces QM by construction,
so it differs from QM nowhere.

***

## 7. Hidden-assumption markers

| # | assumption | where | finding | class |
|---|---|---|---|---|
| HA-7.1 | the size of the nonclassicality is a prior weight, so a measure principle could fix it | `mc-node6` §12, candidate list | in LE the PR value needs no weight: LE(1,1) gives S_max = 4 for every prior | ELABORATING |
| HA-7.2 | matching the value 2√2 in a family shows a quantum correlation is reachable | `mc-node6` §12 (ii), N3 ("the quantum values sit inside the ranges") | LE at S = 2√2 is post-quantum; LE's only quantum member is w = 0 (K-7) | NEW, narrow (a correction to N3's reading) |
| HA-7.3 | the two families show "one convexity pattern in two settings" | `mc-node6` N3, L5 | DR(w ≤ 1/√2) is exactly a qubit (K-11), with its boundary set by preparation purity; LE's nonclassicality is dynamical | ELABORATING |
| HA-7.4 | H-Bell's clause (iii) is compatible with clause (i) and open | Main.md:392, :394; Substratum.md:132 | under the HB-3α and HB-4 readings they are jointly unsatisfiable for a long edge between the wings; only the sparse diagnostic is compatible | NEW, narrow (HB-3α); CONFIRMING (HB-4, SM.md:150) |
| HA-7.5 | nested-observer reversibility constrains correlations as it does in GPTs | PREREG PC-4 | vacuous under κ2: the inverse is accessible at the ontic level | record-only |
| HA-7.6 | the tension between Main.md:60 and Computation.md:120 matters for the magnitude | §3.1 | both readings fail at the same witness | record-only |

Assumption-watch markers:
- **AW-MC7-1.** A magnitude claim tested on a family tests correlations, not only values (HA-7.2).
- **AW-MC7-2.** A principle that constrains only the prior cannot bound a Bell value while the admitted architectures
  include responses that do not depend on the prior and are nonaffine in the settings.
- **AW-MC7-3.** A zero-tolerance limit condition on prepared graphs is all-or-nothing in the preparation weight. An
  interior bound from geometry needs a tolerance, which is a parameter.

***

## 8. Not verified

- **K-10.** n = 4 is pending in CI with owner approval (A-2). The written argument for all n is short (K-10 row), but
  it has not been reviewed.
- **HB-3α.**
  - The limit statement rests on a closed form [W], checked by flow at L ∈ {6, 8, 10, 12} with δ ≤ 2. The closed form
    needs 3L/2 ≥ 4δ + 1.
  - Weightings other than A-3's two options (for example random-walk measures) were not computed.
  - The supplementary edge curvature covers δ ≤ 3 only.
- **HB-4.** The radius argument is [W], with exact radii at L = 4, …, 10 (even L).
- **HB-2.** [W] algebra plus three instances.
- **HB-3β** not evaluated (Parked). **CL** not formalized (Parked). **PC-4b's POM part** Parked (A-5).
- **L3-C** computed for four architectures, enough for the failure witness. **L3-D** not computed (Failure-as-stated).
- **Dense forms of (iii)** for the candidates are [W] (rational weights are dense), not computed. The admission of
  the delay line and toy bit by each candidate is [W] from the K-4 realizations.
- **Bijectivity on Ω** checked exhaustively for LE with n ≤ 12 and for every realization in the O log (404). For all n
  it rests on the involution argument [W]. DR checked from the architecture for n ≤ 40, with the closed form beyond
  [W].
- **C3 (K-5)** checked on a sample of 144 realizations; all members by the padding argument [W].
- **Passive-observation vacuity (K-5b)** [rec], not computed.
- **TLM certification** is exact only for perfect correlations, isotropic zero-marginal correlators and local boxes
  (Fine's theorem [L]). Other zero-marginal points are "undetermined"; the grid instance cross-check is [NUM].
- **PC-3b's (b2)**: maximizing boxes not exhibited, NPA 1+AB status not computed (no SDP tooling). **(b3)**: the
  non-isotropic search was not run.
- **Literature not read in full:** Fine 1982; Spekkens et al. 2009; Tsirelson 1980; Landau 1988; Masanes 2003;
  Acín–Massar–Pironio 2012; Wehner 2006; Navascués–Pironio–Acín; Lin–Yau; Kelly et al.; van der Hoorn et al.;
  Barandes–Hasan–Kagan.
- **Independent review** not yet performed.

***

## 9. Files (`probe/`)

| file | role |
|---|---|
| `p7.py` | controls K-1 to K-9, K-11, SOS, K-P, K-N1 to K-N6, the static checks, then the candidates in PREREG §9 order; 30 checks |
| `p7.run1.out`, `p7.run2.out` | 30 PASS, 0 FAIL; byte-identical |
| `k10.py`, `k10.run{1,2}.out` | K-10 at n ≤ 3; byte-identical |
| `sup_hb3a_edge.py`, `sup_hb3a_edge.run{1,2}.out` | supplementary HB-3α edge curvature (not decision-bearing); byte-identical |
| `SHA256SUMS` | digests of the nine files above |

Run from `probe/`:
- `python3 -I -B p7.py` (SymPy needed; about one minute);
- `python3 -I -B k10.py` (about ten seconds);
- `python3 -I -B sup_hb3a_edge.py p7.py`.

`AMENDMENTS.md` (beside this file) records A-1 to A-9.

***

## 10. Proposed PLAN text

**Status bullet (after `mc-node6/`):**

> - **`mc-node7/`, A2 track node 2, does a principle stated in the corpus fix the size of the nonclassicality:
>   ELABORATING, one NEW (narrow) item, [EC/W]. Preregistered at `73a27ba1`; amendments A-1 to A-9.**
>   - Seventeen readings of Lemma 3's measure selection, partition covariance, H-Bell and Barandes–Hasan–Kagan causal
>     locality were tested on the long-edge and destructive-readout families, under condition O (one substratum, one
>     bijective dynamics).
>   - None derives the quantum boundary. Fifteen fail: twelve over-generate (PR box or gbit admitted), two
>     under-generate (no nonlocality admitted), and one is Failure-as-stated. Two are Parked. The quantum set itself
>     passes, as Reproduction.
>     Outcome (a) is not established for any OI principle, and outcome (b) is not reached.
>   - Measure selection cannot bound the magnitude: the PR box is reached by one deterministic gate for every prior,
>     so the magnitude is a property of the admitted dynamics.
>   - H-Bell's curvature clause is all-or-nothing in the preparation weight. The sparse diagnostic admits S = 4.
>     Endpoint Ollivier curvature (κ ≤ −5/4 at every scale) and Gromov–Hausdorff closeness (distance ≥ 3/8 − 1/(4L))
>     exclude every long edge, so under those readings H-Bell's clauses (i) and (iii) cannot hold together.
>   - The long-edge family is quantum only at w = 0. The destructive-readout family is exactly a qubit for w ≤ 1/√2.
>   - G6: none. Verdicts are provisional on K-10 at n = 4 (CI).

**Next node for the A2 track (proposed): can a limitation on what an embedded observer's records carry select the
quantum correlation set?**

> - *Question.* The corpus's own principles do not fix the magnitude (`mc-node7`). Two principles from the literature
>   are stated as limits on observation, and both bound correlations:
>   - macroscopic locality: coarse-grained records of many copies admit a classical description. It yields exactly
>     the NPA level-1 set, hence Tsirelson's bound and the TLM boundary for zero marginals [L: Navascués–Wunderlich
>     2010];
>   - information causality: m transmitted bits give at most m bits of accessible information. It yields Tsirelson's
>     bound for CHSH, while its full correlation set is open [L: Pawłowski et al. 2009].
>
>   Does either follow from OI's premises (finite resolution, Lemma 1; trace-out; C3; condition O) as a statement about
>   an embedded observer's records, with no free parameter? Since measure-only and graph-geometric conditions are
>   insufficient (AW-MC7-2, AW-MC7-3), a candidate must restrict the admitted response maps.
> - *Decision rule.* `mc-node7`'s rule, unchanged: the family stage, the per-scenario follow-up, outcomes (a) and (b)
>   kept apart, condition O, and the same controls. Two additions:
>   - a derivation from OI premises is required before any candidate is applied; a principle imported as an
>     assumption is Reproduction at best;
>   - outcome (b) is expected to separate the two principles, since macroscopic locality gives NPA level 1, which is
>     strictly larger than Q with nonzero marginals.
> - *Productivity test.* Gem iff a derivation from OI premises of either principle is found, or fails for an
>   identified structural reason that bears on N1–N3.
