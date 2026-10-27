# SC-34: cycle ergodicity on energy shells, scoped by map

Base: SC-28 (`corpus/sc28-assumption-scope` at `7a4e4a8d`) with SC-32 (`corpus/sc32-sm-theorem3` at `6d32ce51`)
merged in by a normal merge. Every site below names the map it concerns. Claims are narrowed to what the
computation or the proof supports, and no claim is strengthened.

## The finding, by map

Three maps occur in the corpus.

- **(a) The exact linear rule.** It is x(t+1) = α Σ_nn x(t) − x(t−1) over ℤ/q (SM Lemma, §4.1, and SM §4.2
  "two roles"), and acts on pairs as F(u,v) = (v, Av − u).
  - It conserves E(u,v) = u·u + v·v − u·Av = |v−u|² + u·(2 − A)v.
  - It also conserves Q_B and P_C, one for each symmetric translation-invariant B and each antisymmetric
    translation-invariant C.
  - **Cycle ergodicity on energy shells is false for (a).** There are exhaustive counterexamples, and the class
    theorem below covers prime q.
- **(b) The rounded bijection.** It is x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q on the representatives
  0,…,q−1 (`papers/main_repro/lyapunov_v3.py`); its one-dimensional analog uses ⌊(·+1)/2⌋
  (`papers/main_repro/mixing_battery.py`).
  - It conserves no quadratic energy exactly.
  - Its evidence is numerical chaos.
  - **Shell ergodicity for (b) is unsupported, not false.** Neither exact energy conservation nor single-cycle
    sampling is shown, and exact small censuses give a largest cycle of at most 1.86% of phase space.
- **(c) The state-dependent-geometry map** of SM §3.1. The corpus makes no ergodicity claim for it, and none is
  edited. s3 records its small censuses for completeness.

## The class theorem

**Statement.** Let q = p be prime with p ∤ L, and let G = (ℤ/L)^d with N = L^d. Let A be any translation-invariant
coupling over F_p, which includes α·(neighbour sum) for every α. Let F(u,v) = (v, Av − u) and m = ord_L(p) ≤ L − 1.
Then F^{p(p^{2m}−1)} = I.

**Proof.** It is proved here on paper, re-checked while writing this record, and checked numerically in 113 cases (s2).

1. F is linear over the commutative ring R = F_p[G] acting on R², and its characteristic polynomial is X² − AX + 1.
   By Cayley–Hamilton over the commutative ring R, F² − AF + 1 = 0. So R[X] → End_R(R²), X ↦ F, factors through
   R[X]/(X² − AX + 1). In that quotient X is a unit with inverse A − X, so the order of F divides the exponent of
   the quotient's unit group.
2. Since p ∤ |G|, R is semisimple: R ≅ ∏ F_p(χ) over the Frobenius orbits of characters χ of G. A character of
   order e | L takes values in μ_e, and its orbit has size ord_e(p), which divides ord_L(p) = m. So R is a product
   of fields F_{p^r} with r | m.
3. Then R[X]/(X² − AX + 1) ≅ ∏ K[X]/(X² − aX + 1) with K = F_{p^r}. Each factor is one of three rings:
   - F_{p^{2r}}, when the polynomial is irreducible; its unit group has exponent dividing p^{2r} − 1;
   - K × K, when the polynomial has distinct roots; the exponent divides p^r − 1;
   - K[ε]/ε², when it has a repeated root. Its units a + bε satisfy (a + bε)^{p^r−1} = 1 + cε, and
     (1 + cε)^p = 1. The exponent divides p(p^r − 1).

   Since r | m, each of these exponents divides p(p^{2m} − 1). ∎

**Consequences.**

- Every cycle length divides p(p^{2m} − 1), so no invariant set with more states than that is a single cycle.
- E takes p values. So the largest energy shell has at least p^{2N−1} states. This exceeds p(p^{2m} − 1) because
  m ≤ L − 1 ≤ N − 1.
- That shell therefore carries more than p^{2N−1}/p^{2m+1} = p^{2N−2m−2} cycles, a number exponential in N for
  d ≥ 2. The confirmation report wrote "about p^{2N−2m−1}"; the bound proved here is p^{2N−2m−2}.
- At d = 1 the bound guarantees that the largest shell is not a single cycle, but does not guarantee many cycles.
  Smaller shells are covered only by the exhaustive censuses.

**Conserved quadratic forms.** These need A symmetric, and B and C commuting with A. All translation-invariant
couplings commute with one another.

- E∘F = E: the terms Av·Av − v·AAv cancel, and −2u·Av + v·Au = −u·Av.
- Q_B∘F = Q_B, by the same computation with B inserted.
- P_C∘F = P_C, since CA is antisymmetric when C is antisymmetric and A symmetric. P_C vanishes identically in
  characteristic 2.

**Scope.** No statement is made for:

- composite or prime-power q;
- p | L;
- couplings that are not translation-invariant;
- maps (b) and (c).

The countercontrol (s2, T1c) shows the bound is not vacuous: it fails for 18 of 20 random elements of GL_n(F_p).
Its pass threshold was amended during the confirmation, from "≥ n−1 fail" to "majority fail", and the amendment
is recorded in the confirmation report. Six p | L cases are listed as outside the hypothesis.

## Sites

The "Now" column gives the current branch text in summary. Line numbers are as on this branch.

| Site | Map | Was | Now | Source |
|---|---|---|---|---|
| SM :290 | (a)/(b) | "This measure-equivalence statement is established at Level 2 rigor" | Reduces to a hypothesis on the stationary law of the realized bijection, which is open | s1–s3 |
| SM :292 | (a) lift; (b) | The substratum "has a stationary distribution that is Gaussian on energy shell"; equivalence "established up to … (ii) cycle ergodicity for the specific bijection" | Conditional: the Gaussian law follows if the stationary law is uniform on a shell of a real-valued conserved energy (the stationary-law hypothesis). Neither (a), which conserves E only mod q and whose integer lift changes at 46–56% of states, nor (b) supplies such an energy exactly | s5, s3, s6 |
| SM :294 | (a); (b) | "Numerical verification of way out (i) for OI's specific bijection"; non-integrability "demonstrated numerically, as chaos, rather than adopted" | (a) over ℤ/q is not shell-ergodic (Remark). (b) is named, with its formula, and is "chaotic at the sizes measured". It has no degree ≤ 2 invariant over F_3 where (a) has invariant spaces of dimension 25 and 10. Its real energy drifts by up to 3.6×10⁻³ against 3.7×10⁻¹⁴. Its largest cycle is ≤ 1.9% of phase space and visits every modular-energy value | s1, s3, s6 |
| SM :296 (new paragraph) | (a) | No statement | *Remark (cycle structure of the exact linear rule)*: the conserved E, Q_B and P_C; the class theorem with its proof; the exhaustive and exact instances; the scope | s1, s2 |
| SM :298 | (a) vs (b) | "the mod-q wraparound / threshold-crossing … present in any faithful finite realization"; ergodic properties "read the threshold nonlinearity"; "The two are not in tension …" | Mod-q reduction is ℤ/q-linear, and (a) is itself a finite bijection. The nonlinearity is the floor in ⌊(Σ_nn x + 1)/3⌋ of (b). The measure properties cannot be read from (a) and are hypotheses about (b); whether one map carries both is open. The "not in tension" sentence is removed. SC-32's Susskind-factorization parenthetical is kept verbatim | s1, s3 |
| SM :799 | (a)/(b) | "the on-shell measure is the smooth □⁻¹ field of §4.2" | Under the stationary-law hypothesis of §4.2 | as :292 |
| SM :805 | (a)/(b) | Free-sector correspondence "established at Level 2" | Holds at Level 2 given the stationary-law hypothesis, which is open | as :292 |
| SM :807 | (a)/(b) | The measure "is" the uniform measure on the energy shell; kinematic half "raised to theorem level"; "The measure is fixed by the sphere-Gaussian projection" | The measure is taken to be the shell measure of a real-valued conserved energy; that the realized bijection samples it is the open hypothesis. The kinematic half rests on two conditions, the hypothesis for the measure and the amplitude-scale principle for the map. The audit status line names both. Register only: "is now the dynamical statement" → "is the …"; "for scrutiny as a candidate rather than asserted as closed" → "as a candidate" | as :292 |
| SM :1221, gap (i) | (a); (b) | "Level 2 closed via pseudofermion correspondence"; "We adopt the former implicitly" | Conditional on the open stationary-law hypothesis, with the covariance match at Level 2 given it. False for (a), with the class theorem cited. Unsupported for (b), shown chaotic only. "We adopt the former implicitly" is removed | s1–s3 |
| SM :1223, gap (ii) | (a); (b) | Part A "conditional on cycle ergodicity of the realized bijection on a T-invariant set"; "gap (ii) is at Level 2 framework-essentially" | Part A is exact for the uniform shell measure, since E∘T = E with no ergodicity used. The residual is identifying the realized law with that measure: false for (a), where 90 of 2,160 cycles on shell E = 1 are T-self-conjugate (d = 1, L = 5, q = 3), and open for (b). The "Level 2 framework-essentially" sentence is removed | s7 |
| SM :1233, Bridge Theorem (c) | — | SC-28: "a stationary distribution of the bijection" | Unchanged | — |
| SM :1412 | (a); (b) | φ "constrained by linear dynamics, T-invariance, P-indivisibility, and cycle ergodicity"; "essentially unique" | Constrained by linearity up to rounding, T-invariance and P-indivisibility. Cycle ergodicity is not established: it fails for (a) at prime q ∤ L, so (a) does not satisfy linearity and cycle ergodicity jointly, and it is open for (b). The scheme parametrization and "essentially unique" are conditional on it | s1, s2 |
| Juno :397 | (a); (b) | Same constraint list | As SM :1412, cited as [18, §4.2]. Register only: "has since been closed by" → "the staggered calculation answers" | as SM :1412 |
| Juno :399 | — | Same constraint list | Constraint list without cycle ergodicity | as SM :1412 |
| Main :720, posit (v) | (a); (b) | Mixing hypothesis for "linear-mod-q automata" | (a) conserves a quadratic invariant for each symmetric translation-invariant coupling, and at prime q ∤ L its large shells split into many short cycles. The hypothesis rests on the rounding nonlinearity, chaotic numerically, whose cycle structure is open. Register only: "should be read as conditional" → "are conditional" | s1, s2 |
| Main :752 | — | "in its typical orbit phase — equivalently, in its equilibrium macrostate" | "in its equilibrium macrostate". The equivalence needs shell sampling and is removed | s1 |
| Main :754, scope (ii) | (a); (b) | "pathological non-ergodic φ (many short orbits) is excluded by the structural assumptions already in force" | The assumptions do not exclude it. (a) meets bounded coupling and finiteness, its order divides p(p^{2m}−1), and for d ≥ 2 its largest shell splits into exponentially many such cycles, so it fails this necessary condition for (EM). The orbit-length structure of (b) is open | s2 |
| Substratum :135 | (a); (b) | Integrability "requires an extensive set of local conserved quantities, which a … graph without fine-tuned commuting structure does not possess"; "so ETH is the expected case" | (a) carries commuting structure from translation invariance and has such a set (Q_B, local for local B). The argument concerns the rounding nonlinearity of the realized rule, and ETH is "the expected case" for that dynamics | s1, s2 |
| ch18 :191 / FULL :5009 | all | SC-28 text | Unchanged. The zero configuration is fixed under (a), (b) and (c) | — |
| ch18 :184–:187 | — | Recurrence period read as e^n "Landau" | Not edited: SC-31's site (#967). s4 retains the adjacent check (ln g(n) ≈ √(n ln n); 83 against ln lcm(1..1000) ≈ 997) | s4 |

**Checked and not edited.**

- GR Theorem A.8 and the GR Page-curve sites. They work cycle by cycle under H-scramble, or with the full product
  space as the shell.
- GR :58. It uses uniform counting on a shell as the measure, not as a dynamical claim.
- Explainer :56 and :115, and Lemma 3's single-orbit uniqueness.
- Main :496. It states numerical chaos for (b), with the cycle structure open.
- The horizon-complement "generic chaotic" sites in GR, Main and ch07. They concern the physical horizon complement.
- Substratum :455 and SM :1219. These record the bridge gaps without a closure claim.

**Mirrors.** No book, FULL or Explainer text mirrors the edited sites. The book is not rebuilt.

**Coverage.** One canonical statement moved: `MAIN:C-past-hypothesis-replacement-rate-condition` (Main :752),
with fingerprint `a178b6cd20049f46` → `9808992426b49dbd`. Its mapping, its level (GAP) and its delta ("not
formalized") were re-read and are unchanged. The new SM text is a Remark, not a census statement, so no ledger
entry is added.

## Evidence level of each claim

| Claim | Level |
|---|---|
| The order bound F^{p(p^{2m}−1)} = I under the class hypotheses | Proved on paper (above); checked exactly in 113 cases (s2 T1) |
| E, Q_B and P_C are conserved by (a) | Algebraic identity (above); exhaustive at d = 1, L = 5, q = 3 and d = 3, L = 2, q = 3 (s1, s2 T2) |
| Shells of (a) split into many cycles in the instances | Exhaustive enumeration with planted controls (s1) |
| Exact ord(F) = 60, 84, 6 on the d = 3, L = 3 torus (p = 5, 7, 2), and the Burnside cycle counts | Exact integer linear algebra mod p (s2 T3) |
| Every shell larger than ord(F) at d = 3, L = 3, p = 5, 7 | Exact rank of E's form with a shell-size bound, checked against the exhaustive shell sizes (s2 T3c) |
| (b) has no nonzero degree ≤ 2 invariant over F_3 at the two sizes | Exact solver, with (a) as positive control (s3 K2) |
| (b) and its 1D analog: largest cycle ≤ 1.86% of phase space; every modular-energy value visited | Exhaustive census, cross-checked by traversal where small (s3 K3, K4) |
| Real-energy drift of (b), 3.6×10⁻³ against 3.7×10⁻¹⁴ | Floating point, one smooth mode, L = 20, q = 2^16 (s6); numerical evidence only |
| Integer lift of (a)'s energy changes at 46–56% of states | Exhaustive, d = 1 (s5) |
| Uniform one-site marginals on (a)'s mod-q shells | Floating point TV printed as 0.0000, exhaustive at d = 1 (s5). Not stated in the manuscript |
| E∘T = E and the T-self-conjugate cycle counts for (a) | Exhaustive (s7) |
| Chaos of (b) | Numerical, from the corpus's existing diagnostics; not re-run here |

## Scripts and replay

The scripts are the confirmation's, unmodified. Each is self-contained (numpy; s2 also needs sympy) and is run
from this directory:

```sh
python3 -I s1_map_a_linear.py > s1_output.txt   # about 10 minutes
python3 -I s2_map_a_theorem.py > s2_output.txt
...                                              # likewise s3–s7
```

They were replayed from this directory under `python3 -I`, with Python 3.13.16, numpy 2.5.3 and sympy 1.14.0.

- s4–s7: the output is byte-identical to the committed files.
- s1–s3: the output is identical except for the last four lines of the committed files. These are a blank line and
  the `real/user/sys` durations of the shell's `time`, which the original captures appended. The durations are not
  expected results.
- Replay times: s1 10.0 min, s2 75 s, s3 100 s, s5 5 s; s4, s6 and s7 under 2 s.

Two cosmetic defects are recorded here and not repaired:

- In s2 T3, for p = 2, the printed witness line labels the compared values "P_C". They are Q_B values, because
  P_C vanishes in characteristic 2 and the code uses Q_B there. The PASS criterion uses the right quantity.
- The confirmation's file index note, not retained here, named two scripts that do not exist. The table below is
  the index.

| Script | Content |
|---|---|
| `s1_map_a_linear.py` | (a): exhaustive cycle census per energy shell, degree ≤ 2 invariant space, controls C0–C6 (bijection, conservation, census = traversal, planted cycle structures) |
| `s2_map_a_theorem.py` | T1: order bound in 113 cases, with the GL_n countercontrol. T2: named invariants. T3: exact orders, Burnside cycle counts, shell-size bounds and witnesses at d = 3, L = 3 |
| `s3_maps_b_c.py` | (b) and (c): fidelity control against the repository step functions, energy non-conservation, invariant space, exhaustive cycle censuses, with (a) as positive control |
| `s4_side_landau.py` | Landau's function against ln lcm(1..n), with a brute-force control. This is the adjacent finding for SC-31 |
| `s5_shell_marginals.py` | (a): one- and two-site marginals on the mod-q shells, conservation of the integer lift, thin-real-shell control |
| `s6_map_b_large.py` | (b) at L = 20, q = 2^16: modular-energy change and real-energy drift, with the exact real linear map as control |
| `s7_gapii_T.py` | (a): TFT = F⁻¹, E∘T = E, T-self-conjugate cycles per shell |

## Re-grep

Over `papers/*.md` and `book/*.md`:

- **Zero hits** remain for each of:
  - "cycle ergodicity for OI"
  - "Level 2 closed via pseudofermion"
  - "We adopt the former implicitly"
  - "present in any faithful finite realization"
  - "raised to theorem level"
  - "structural assumptions already in force"
  - "typical orbit phase"
  - "Level 2 framework-essentially"
  - "is established at Level 2"
  - "for OI's specific bijection"
  - "P-indivisibility, and cycle ergodicity"
  - "not in tension within the local lattice"
  - "demonstrated numerically, as chaos"
  - "mod-$q$ wraparound / threshold"
- **Surviving uses:**
  - "cycle ergodicity": 6 (SM and Juno), all now stated as open or false by map.
  - "essentially unique": 1 (SM :1412), conditional.
  - "typical orbit": 1 (Main :754, "typical orbits of φ", the Koopman remark).
  - "empirically demonstrated": 1 (Bioinformatics :475, external methods).
  - "cycle-ergodicity": 2 (ch18 :191 and FULL :5009, SC-28's text).

## Open questions for #970, track 4

1. Does the rounded bijection sample an energy band? With respect to which approximately conserved energy, and with
   what cycle-length distribution at sizes beyond exact enumeration?
2. Which single map φ carries both the structural chain (proved for the exact linear rule) and the measure
   properties (hypotheses about the rounded bijection)?
3. Derive the stationary law of the rounded bijection, or show that the Gaussian covariance □⁻¹ of the measure
   reduction and of the gauge-measure choice holds for it.
4. Is the maximal-entropy measure selection (Main posit (iv)) a route to the shell measure that needs no
   ergodicity? The uniform shell measure is invariant under (a) and T without it, but it is not the realized cycle
   law.
5. The class theorem outside its hypotheses: composite and prime-power q, p | L, and couplings that are not
   translation-invariant, including the state-dependent graphs of SM §3.1.
6. The orbit-length structure of the rounded bijection, which bears on Main §4.6 scope (ii) and posit (v).
