# Issue #1556 (OI-STRING): paper-only bridge audit and dependency map (revision r3)

## 0. Status, pin and sources

- **Status:** paper-only research record for the Exploratory tier, revised (r2) after the independent review of r1 (PR #1563, comment 7166923987, verdict REVISE) and the owner decision of 2026-11-25 (`amaybaum`). The agent that wrote r1 and r2 made no repository, git or GitHub writes during its runs; the record reaches the repository only through the pull request that carries it. No premise or manuscript change is made or proposed here; manuscript inaccuracies are listed in section 9 and not edited.
- **Revision r3:** a minimal revision after the independent delta review of r2 (PR #1563 delta review, verdict ACCEPT-WITH-NITS), made by owner decision (`amaybaum`, 2026-11-25): "Proceed with a minimal r3 addressing F2, F3 and the remaining nits. For F1, retain the transient bound and tube-exit corollary as independently reviewed mathematical results, explicitly distinguishing them from kernel-verified results. No additional formalization is required at this stage. Obtain a short independent delta review. Do not expand the investigation. The confinement result is now substantially better supported, but its physical scope remains limited to the specified microscopic dynamics. It does not exclude emergent observer-level string-like excitations." r3 changes only the status labels of section 5 (finding F1), the d = 1 glider wording (F2), the initial-data convention of the time-reversed point source (F3) and two wording nits; the agent that wrote r3 made no repository, git or GitHub writes, and r3 itself awaits the short independent delta review that the decision asks for.
- **Verification status (section A.46 item 4):** the proposition of section 5 is a paper proof written for this record. It repairs r1's sketch along the reviewer's argument and adds a transient bound (Step 6) and the tube-exit and line-extended Corollaries 2-3. The whole of section 5.3, including Step 6 and Corollaries 2-3, has been checked on paper by one independent non-author review (PR #1563 delta review of r2). These are independently reviewed paper results, not kernel-verified results: no part of section 5 is kernel-checked. The computations of section 5.7 are exact finite spot checks run in scratch scripts that are not in the repository; no conclusion rests on them alone. Accountable Issue: #1556. Remediation: the PR #1563 delta review is the independent review of section 5 and of the section 9 changes; by owner decision no additional formalization is required at this stage, so kernel verification of section 5 remains open; the decision that would settle each other gap is stated where the gap is stated.
- **Corpus pin:** `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`, read via `git show` from a full clone.
- **Issue context:** the body and the owner activation comment of #1556 (2026-11-25), and the findings comments of #1558. #1558 found that OI's observer interface is operationally classical (kernel: `obsTheory_nonnegBounded`, `sourcing_rule_independent`; the review confirms both identifiers exist on `main`, in `verification/lean-mathlib/OIBridge/FrozenSourcing.lean` and the census), that interference is not derived, and that quantum emergence is open. These are treated as constraints throughout.
- **Corpus read:**
  - `papers/Structure.md`: sections 1-7, 9.1, 9.8, 11, 12.4, 13.1.4 and 14.1-14.6 in full; other sections by grep.
  - `book/ch09-universality.md`: sections 9.5-9.6, and lines 224 and 328 for M10; the mirror in `book/The-Incompleteness-of-Observation-FULL.md` contains the same section 9.5 text.
  - `papers/GR.md`: sections 2.3, 3.1, 5 and 8.7, plus grep hits.
  - `papers/SM.md`: section 2 (lines 46-122), lines 92, 224 and 232 (section 4.1), line 809, the area-law lemma and its proof, section 6.5, Theorem 22.
  - `papers/Substratum.md`: E3 and the ER=EPR remark at the end of section 3.
  - `papers/Main.md`: C3, Lemma 1.
  - `book/ch02` and `book/ch07`: grep hits.
  - Corpus-wide grep for: string, holograph, AdS, Bekenstein, area law, WGC, soliton, vortex, flux tube, confinement, winding.
- **External literature.** Each external statement in this record is marked either *verified*, with what was retrieved, or **[background]**, meaning a standard description given from general knowledge and not checked against the source in this investigation.
  - *Verified, full text:* Ibanez, Martin-Lozano, Valenzuela, arXiv:1706.05392 (IMV). Retrieved in full in r1; the independent review also retrieved it and quotes it (M1). Quotations attributed below to the review were taken from the review and not re-retrieved in r2.
  - *Verified, abstract only:* 't Hooft, "Discreteness and determinism in superstrings", arXiv:1207.3612. Retrieved in r1; not re-retrieved in r2. Only what the abstract states is treated as verified; everything else about this paper is [background].
  - *[background], not retrieved:* BFSS 1996; Maldacena 1997; Strominger-Vafa 1996; Strominger dS/CFT 2001; Ryu-Takayanagi 2006; Almheiri-Dong-Harlow 2014; Pastawski-Yoshida-Harlow-Preskill 2015; Heemskerk-Penedones-Polchinski-Sully 2009; Srednicki 1993; Eisert-Cramer-Plenio 2010; Bousso 2002; Goddard-Goldstone-Rebbi-Thorn 1973; Polyakov 1981; Luscher 1981; Polchinski-Strominger 1991; Aharony-Komargodski 2013; Lee-Lerche-Weigand 2019; Ooguri-Vafa 2016; Ooguri-Palti-Shiu-Vafa 2018; Agrawal-Obied-Steinhardt-Vafa 2018; Savit 1980; Martin-Odlyzko-Wolfram 1984; Kramers-Wannier duality.
- **Goal link (section A.47):** #1556. This decides whether OI and string theory share more than generic observable-level structure, and where each bridge direction first fails.

***

## 1. The existing correspondence and its support

| Claim (location) | Support class | Assessment |
|---|---|---|
| BFSS/IKKT fail A1 (without a finite-value regulator), A2 and A5; A3 fails on the natural reading; A4 holds; A6 holds conditionally (Structure section 6) | Paper argument; facts about the matrix models [background] | Sound for the models examined. It is a scoped no-bridge result for matrix models, not for string theory in general. |
| No substratum-level equivalence between OI and string compactifications (sections 4.3, 6.9, 7.1, 7.8) | Paper argument, scoped to matrix models | Sound as scoped. Sections 13.1.4 and 13.4 overgeneralize it (M8). |
| Area law, A/4 and the holographic bound emerge as a "structural consequence of partial-trace observation" (sections 7.7.1, 7.7.4, 12.4) | Actual support: A/4 is a conditional calibration (GR section 5, under H-count, H-slope, H-frame, H-Hawking, boost structure and detailed balance). Area scaling of horizon entropy is the H-count hypothesis (GR section 2.3), motivated by the E3 input (Substratum section 3.1) | Overstated (M3). Area scaling is put in, not derived. The holographic bound for general regions has no support. |
| Full AdS/CFT does not emerge; dS holography open (section 7.7.1) | Analysis | Consistent. Contradicted by ch09 Recovery (i) and by the Substratum ER=EPR remark (M5, M9). |
| Graviton modes open, a Level-G3 target (section 7.7.2) | Correctly scoped | Consistent with GR sections 3.2 and 8.7. |
| T-duality "No"; S-duality speculative (section 7.7.3) | Analysis of momentum-winding T-duality | Consistent as scoped: the "No" concerns momentum-winding T-duality, and universality-class analogues are already labelled speculative there (see M12, not confirmed). |
| Four-feature audit (sections 14.1-14.6) | Representation-level facts true of any quantum theory with subsystems (Stinespring); analogy to holographic EFT [background] | Carefully scoped in section 14 itself. Restated more strongly in the abstract and in sections 1.5, 11.1, 11.3 and 7.7.4 (M6, M7). |
| WGC "cross-validates" OI's Majorana neutrinos (sections 7.5.1, 7.5.5) | Misreported citation (verified against IMV) | Reversed, with conditions (M1). |
| Type II RVM "satisfies" the refined dS conjecture (section 7.5.2) | Unsupported | M2; also contradicts ch09 section 9.6. |
| Observer admission C1-C4 for compactifications (section 7.9) | Candidate translation only; "No such witness is exhibited here" (Structure line 536) | Correctly scoped in section 7.9. |
| ch09: string theory is an emergent description within OI's hierarchy (section 9.5) | None | Contradicts Structure sections 7.1 and 7.8, and the #1556 boundary (M9). |

***

## 2. Direction OI -> strings: dependency map

| Link | Content | Status |
|---|---|---|
| S1 | Confined excitations of a microscopic linear update | **Excluded for one rule:** the linear rule x(t+1) = alpha·(sum of the 2d nearest neighbours) − x(t−1) mod q on the infinite lattice Z^d, d ≥ 2, alpha a unit modulo every prime factor of q (section 5; paper proof checked by one independent review, PR #1563 delta review; not kernel-verified). This rule is not identified with OI's general dynamics, and the result does not bear on observer-level excitations. String-theory strings are not solitons of a linear field, so this link carries little weight for the bridge |
| S1' | Extended excitations at the observer or coarse-grained level | **Unsupported; the earliest unsupported OI -> strings step.** Candidate routes, both open: (a) confining flux tubes of the induced SU(3); (b) vortex lines of the lifted compact phase. Nothing in section 5 excludes them |
| S2 | Effective equations of motion (Nambu-Goto plus corrections) derived from the update | **Unsupported.** A tension needs a real-valued conserved energy; the exact rule conserves energy only mod q (SM section 6.5) |
| S3 | Quantization | **Blocked** by the open OI-QM operational reconstruction (#1558) |
| S4 | Critical-string content: worldsheet CFT, Regge tower, closed-string graviton, T/S-duality | Not derived (Structure section 7.7.4). Graviton sector open at G3 |
| H1 | A finite observable boundary | Conditional: GR section 2 horizon partition, with C4 "not presently discharged" |
| H2 | Area-scaling correlations | Paper proof: I(V;V^c) <= \|dV\| log2 q in the uniform state class under hypothesis H-mu (SM area-law lemma). This is a generic consequence of range-1 locality |
| H3 | Area-scaling horizon entropy | **Posited:** H-count (GR section 2.3), with E3 as theoretical input |
| H4 | The 1/4 coefficient | Conditional calibration (GR section 5). It is equivalent to the Hawking normalization by construction |
| H5 | A holographic entropy bound for general regions | **Unsupported.** The substratum capacity count log2\|C_H\| = \|H\| log2 q scales with volume (SM Theorem 22) |
| H6 | A bulk-boundary duality: boundary system and dynamics, an algebra isomorphism on a code subspace, correlator dictionary, reconstruction | **Absent.** Partial trace is a many-to-one channel, not an isomorphism. OI's cosmology is dS |

**Earliest unsupported step:** S1'. No OI-native description has been shown to contain a stable extended excitation at the observer level. Section 5 excludes confined excitations only for the stated microscopic linear rule; it does not establish the absence of emergent string-like excitations at the observer level, where the nonlinear readout and the induced measure (SM section 6.5) enter. For holography the earliest unsupported step is H5, and H6 is absent.

***

## 3. Direction strings -> OI: dependency map

| Link | Content | Status |
|---|---|---|
| R1 | A specified string model in OI's structural class (A1-A6) | Fails for BFSS/IKKT at A2 and A5 (Structure section 6). One candidate is not examined in the corpus: 't Hooft's discretized light-cone superstring (arXiv:1207.3612). Verified from the abstract: it claims a map from deterministic discrete string states to a basis of the quantized superstring. [background], not checked against the paper: that its worldsheet is free and linear (g_s = 0), that it uses a target-space lattice, and its standing in the literature |
| R2 | A declared visible/hidden partition with record dynamics satisfying C1-C4 | **Unsupported.** Structure section 7.9: "No such witness is exhibited here" (line 536). C1-C4 are formulated for finite deterministic substrata, and a quantum-substratum analogue of C4 needs an instrument specification. Free strings form no bound records |
| R3 | Agreement at the level of record statistics | **Trivially satisfiable and so uninformative.** Main's finite-law and intervention-dilation theorem (cited at GR section 2.3) gives a reversible realization for any finite record table. Representing is not deriving (section A.29) |
| R4 | Observational equivalence (Def. 9.3: a *-isomorphism of algebra-channel pairs) | Open (Structure section 11.2). Precondition 2, that some compactification reproduces the SM, is itself unmet (section 1.2) |

**Earliest unsupported step:** R2. A discriminating test must use the string model's own microdynamics restricted to a declared observer; R3 cannot discriminate. At the structural-class level, R1 is unsettled rather than closed, because the free-string candidate has not been examined.

***

## 4. The six questions

| Question | Conclusion | Support class | Conditions |
|---|---|---|---|
| 1. Emergent strings | Confined excitations are excluded for the linear rule of section 5; this does not establish the absence of emergent string-like excitations at the observer level (S1', open). Observer-level strings are not derived. The QCD-flux-tube route depends on two things: the under-determined induced gauge measure of SM section 6.5 (the natural polar map gives a Haar, confining pushforward numerically, SM line 809, while the near-identity measure is conjectured), and confinement, listed as open in ch10 and Complexity | Paper proof for the linear rule (checked by one independent review; not kernel-verified) plus corpus citations | For the section 5 result: d ≥ 2; alpha a unit modulo every prime factor of q; infinite lattice, or times before wrap-around on a finite torus |
| 2. Effective dynamics | Not derivable now. There is no native real-valued conserved energy, hence no tension. A Nambu-Goto or effective-string description [background] presupposes it | Missing mechanism | |
| 3. Quantization | Classical extended excitations would still need: (a) operational quantum structure, which is open (#1558); (b) for critical strings, anomaly cancellation (D = 26 or 10 [background]), which OI's fixed d = 3 lattice does not supply; (c) for effective (non-critical) strings, only a long-distance EFT [background]. Inserting quantum rules would be representation, not derivation | Missing mechanism | |
| 4. Holography | Restricted observation gives a boundary, locality area laws and a calibrated A/4, all conditional or posited. It does not give a duality. Recovering bulk data from a boundary history over a light-crossing time is classical observability (a control-theory notion, offered as a suggestion only), not equal-time holography | Paper proof (H2), posit (H3), conditional (H4), absent (H5, H6) | |
| 5. Reverse correspondence | No specified string model has a C1-C4 witness. Agreement at the record level is trivial (R3). One structural-class candidate (free discretized superstring) is unexamined | Open | |
| 6. Universality | The similarity is generic-structural: Born-form subsystem statistics and Stinespring dilations hold for any quantum theory with subsystems, so they do not discriminate. Memory and gauge restriction are shared only as patterns. Agreement on the 1/4 coefficient is consistency with the Hawking normalization (section A.23 consistency axis), not shared microphysics. Everything string-specific is analogy | Representation theorem plus analogy | |

***

## 5. Scoped result: no confined excitations of one linear rule

### 5.1 Scope

The rule studied is

  x(t+1) = alpha · Σ_{j=1..d} ( x(t)_{·+e_j} + x(t)_{·−e_j} ) − x(t−1)  (mod q)

on the infinite lattice Z^d. This is the form fixed by the lemma at SM line 224 ("These conditions fix the form, not the observer-level normalization of alpha"). SM section 4.1, Scope (line 232), places the normalization alpha = 1/d at an observer-level operator "not ... the substratum update". The result below does not use alpha = 1/d: it holds for every alpha that is a unit modulo every prime factor of q (for example alpha = 1 for every q). The condition "3 does not divide q" is needed only for alpha = 1/3 to exist and plays no role. The rule is **not** identified here with OI's general dynamics: SM line 106 concerns general, state-dependent f(neighbours), and nonlinear, rounded or state-dependent rules are not covered.

Notation. For a finitely supported configuration f, h_f(u) = max{⟨a,u⟩ : a ∈ supp f} for u ∈ R^d, u ≠ 0. The rate is c(u) = max_j |u_j|, the support function of the ℓ1 unit ball (the octahedron oct = conv{±e_j}); the "light cone" below is this ℓ1 cone. For initial data (x(0), x(1)) put D = supp x(0) ∪ supp x(1) and width_u(D) = h_D(u) + h_D(−u).

### 5.2 Proposition

Let d ≥ 2, q ≥ 2, and alpha a unit modulo every prime factor of q. For every nonzero finitely supported pair (x(0), x(1)) and every u ≠ 0:

- (a) *Light cone.* h_{x(t)}(u) ≤ h_D(u) + t·c(u) for all t ≥ 0.
- (b) *Eventual growth with an explicit transient.* For every t > T*_u := width_u(D)/c(u) + 3/2,
  h_{x(t)}(u) ≥ t·c(u) − h_D(u) − 2h_D(−u) − 3c(u).
- (c) *Prime q.* If q is prime, then for every t > T*_u, h_{x(t)}(u) = t·c(u) − κ_u for a constant κ_u: the support function increases by exactly c(u) per step.

Since width_u(D) ≤ c(u)·diam_1(D), T*_u ≤ diam_1(D) + 3/2 for every u, uniformly in q and alpha, where diam_1 is the ℓ1 diameter of D.

**Corollary 1.** No nonzero finitely supported solution stays in a bounded region for all time.

**Corollary 2 (tube exit time).** If D ⊆ Tube_r := {a : |a_1| ≤ r}, then supp x(t) is not contained in Tube_r for every integer t ≥ 4r + 4. (Take u = e_1: c = 1, width ≤ 2r, so T* ≤ 2r + 3/2, and (b) gives h_{x(t)}(e_1) ≥ t − 3r − 3 > r once t > 4r + 3.) The bound does not depend on q, alpha, d or the extent of D along the other coordinates.

**Corollary 3 (line-extended data).** Let d ≥ 3, with data periodic in the last coordinate z with period L_z, finitely supported in the transverse coordinates, and gcd(L_z, q) = 1. Then (a) and (b) hold for every transverse direction u = (u', 0), with D replaced by the transverse projection of the data and c(u) = max over the transverse |u_j|; in particular Corollary 2 holds for transverse tubes. Data periodic in z with p dividing L_z for some prime p | q, and z-invariant data that are not periodic, are not covered.

### 5.3 Proof

**Step 1 (reduction to prime q).** By the Chinese remainder theorem Z/q ≅ Π Z/p_i^{k_i}, the rule acts componentwise, and supp x(t) is the union of the component supports; a nonzero solution is nonzero in some component Z/p^k, and alpha is a unit mod p. Over Z/p^k, let v < k be the least p-adic valuation among the coefficients of x(0), x(1), and write x(i) = p^v g(i). The g(i) are defined mod p^{k−v}, the rule is linear, so x(t) = p^v y(t), where y solves the rule mod p^{k−v}. Its reduction ȳ mod p solves the rule over F_p with nonzero data (by minimality of v). A coefficient of x(t) is nonzero mod p^k exactly when the corresponding coefficient of y(t) is nonzero mod p^{k−v}, which holds wherever ȳ(t) is nonzero mod p, since k − v ≥ 1. Hence supp x(t) ⊇ supp ȳ(t), and the data support D̄ of ȳ lies in D. Since (b) is monotone in D (h_D̄ ≤ h_D, width_u(D̄) ≤ width_u(D)), (b) for ȳ over F_p implies (b) for x. Part (a) holds over any Z/q by induction: h_{x(t)} ≤ max(h_{x(t−1)} + c, h_{x(t−2)}). From here on q = p is prime.

**Step 2 (algebra).** Finitely supported configurations over F_p form the Laurent ring R = F_p[x_1^±, ..., x_d^±], a UFD, with fraction field K; shifts are multiplication by monomials. The rule reads x(t+1) = P·x(t) − x(t−1) with P = alpha·Σ_j (x_j + x_j^{-1}). Because alpha ≠ 0 in F_p, P has exactly 2d monomials.

**Step 3 (irreducibility; the reviewer's argument, checked).** Suppose X^2 − P X + 1 has a root λ in K. Then λ is integral over R; a UFD is integrally closed, so λ ∈ R. From λ^2 − Pλ + 1 = 0, λ·(P − λ) = 1 with P − λ ∈ R, so λ is a unit of R. The units of a Laurent ring over a field are c·m with c ∈ F_p^× and m a monomial. Then P = λ + λ^{-1} = c m + c^{-1} m^{-1} has at most two monomials. For d ≥ 2, P has 2d ≥ 4. So the polynomial is irreducible over K. No discriminant or division by 2 is used, so this holds for p = 2. Its roots λ, λ^{-1} in the splitting field L = K(λ) are distinct, since λ = λ^{-1} would give λ = ±1 ∈ K.

**Step 4 (closed form).** For t ≥ 0, x(t) = A_+ λ^t + A_- λ^{-t} in L, with
A_+ = (x(1) − λ^{-1} x(0)) / (λ − λ^{-1}) and A_- = (λ x(0) − x(1)) / (λ − λ^{-1})
(check: A_+ + A_- = x(0) and A_+ λ + A_- λ^{-1} = x(1), using λ·λ^{-1} = 1). Their product is
A_+ A_- = −N / (λ − λ^{-1})^2, where N = x(0)^2 − P x(0) x(1) + x(1)^2 ∈ R.
N ≠ 0: if x(1) = 0 then N = x(0)^2 ≠ 0; otherwise N = x(1)^2·(y^2 − P y + 1) with y = x(0)/x(1) ∈ K, which is not a root by Step 3. Hence A_+ ≠ 0 and A_- ≠ 0 for every nonzero datum.

**Step 5 (valuation in direction u).** For f ∈ R nonzero let v(f) = min{⟨a, −u⟩ : a ∈ supp f} = −h_f(u). This is a real-valued valuation on R: the initial forms (the terms attaining the minimum) multiply, and their product is nonzero because R is a domain, so v(fg) = v(f) + v(g); and v(f + g) ≥ min(v(f), v(g)). It extends to K, and further to a real-valued valuation w on L. Since all 2d monomials of P are present, v(P) = −c with c = c(u) > 0. Let s ≥ 0 be such that the roots have valuations −s and s (their product is 1); call λ_+ the root with w(λ_+) = −s and λ_- = λ_+^{-1}. If s < c, w(P) = w(λ_+ + λ_-) ≥ −s > −c; if s > c, the two valuations differ, so w(P) = −s ≠ −c. Hence s = c. (This is the Newton-polygon statement: slopes ±c.) Relabel the closed form as x(t) = A_+ λ_+^t + A_- λ_-^t, with both coefficients nonzero by Step 4. The two terms have valuations w(A_+) − tc and w(A_-) + tc. When the first is strictly smaller, w(x(t)) equals it, and since x(t) ∈ R, h_{x(t)}(u) = −w(x(t)) = tc − w(A_+). This holds for all t > T_u := (w(A_+) − w(A_-)) / (2c), which proves (c) with κ_u = w(A_+).

**Step 6 (transient bound).** From Step 4, w(A_+) + w(A_-) = v(N) − 2w(λ_+ − λ_-) = v(N) + 2c, because w(λ_+ − λ_-) = min(−c, c) = −c. Next, w(A_-) = w(λ_+ x(0) − x(1)) + c ≥ min(v(x(0)), v(x(1)) + c), so −w(A_-) ≤ max(h_{x(0)}(u), h_{x(1)}(u) − c) ≤ h_D(u). The support of N lies in the sumset D + D + ({0} ∪ {±e_j}) (the set {0} ∪ {±e_j} contains 0 and supp P), so v(N) ≤ max{⟨a,−u⟩ : a ∈ D + D + ({0} ∪ {±e_j})} = 2h_D(−u) + c; this uses only N ≠ 0. Therefore
w(A_+) = v(N) + 2c − w(A_-) ≤ 2h_D(−u) + h_D(u) + 3c, and
2c·T_u = w(A_+) − w(A_-) ≤ 2h_D(−u) + 2h_D(u) + 3c,
so T_u ≤ T*_u. Combining with Step 5 gives (b) over F_p, and Step 1 transfers it to every admissible q.

**Step 7 (Corollary 3).** For p ∤ L_z, z^{L_z} − 1 is separable over F_p, so F_p[z]/(z^{L_z} − 1) ≅ Π_i F_{p^{m_i}}, with z mapped to a root of unity ζ_i in the i-th factor. This isomorphism acts coefficientwise on the transverse Laurent expansion, so the transverse support of a configuration is the union of the supports of its components, and each component's data support lies in the transverse projection of D. In component i the ring is F_{p^{m_i}}[transverse x_j^±], again a Laurent ring over a field, with P_i = alpha·Σ_{transverse j}(x_j + x_j^{-1}) + alpha(ζ_i + ζ_i^{-1}). P_i has at least 2(d − 1) ≥ 4 monomials, so Step 3 applies; for transverse u the constant term has valuation 0 > −c, so v(P_i) = −c and Steps 4-6 apply unchanged. The composite-q reduction of Step 1 preserves z-periodicity; gcd(L_z, q) = 1 makes p ∤ L_z for whichever prime the reduction lands on.

**Where r1's sketch failed.** r1's step 3 (Ostrowski: NP(U_t(P) f) = (t − 1)·oct + NP(f)) is correct for each of the two terms of x(t) = U_t(P) x(1) − U_{t−1}(P) x(0) separately, but it does not exclude cancellation *between* the two terms, and that cancellation occurs. Steps 3-6 replace it: cancellation is controlled by the nonvanishing of the norm N, which is where d ≥ 2 enters.

### 5.4 The shrinking transient

Data whose growing coefficient A_+ has large valuation (is "small" in direction u) are dominated for a time by the decaying component A_- λ_-^t, so h_{x(t)}(u) decreases by c per step until t ≈ T_u. The time-reversed point source is the extreme case. Run a point source, with initial data x(0) = 0 and x(1) = δ_0, to time T0 and use (x(T0+1), x(T0)) as data: the solution retraces the point source, the support shrinks for about T0 steps, passes through a zero slice, and then regrows. This is consistent with the proposition, which asserts growth only for t > T*_u. With this convention width_{e_1}(D) = 2T0 (it would be 2T0 + 2 for x(0) = δ_0), so T*_{e_1} = 2T0 + 3/2, while the observed onset is about T0 (section 5.7). It contradicts only r1's step 3, which implied that the hull never shrinks. The example also shows that the transient is genuinely linear in the data width: T_max(r) in section 7 is at least of order r.

### 5.5 Why d = 1 is excluded

For d = 1, P = alpha(x + x^{-1}) has two monomials, and Step 3 fails exactly when alpha^2 ≡ 1 (mod p): then λ = alpha·x is a root in K. For alpha = 1 (= 1/d), the datum x(0) = δ_0, x(1) = δ_1 gives N = 1 − (x + x^{-1})·x + x^2 = 0, hence the coefficient of the root growing in direction −e_1 vanishes (for u = +e_1, where λ_+ = x, this is A_-, while A_+ = 1). The solution is the right-moving d'Alembert component x_i(t) = δ_{i,t}, whose support translates forever without growing (checked exactly, section 5.7). The proposition is stated only for d ≥ 2. (For d = 1 with alpha^2 ≢ 1 mod p the irreducibility step holds, but no d = 1 statement is made here.)

### 5.6 What is proved and what is not

Proved on paper here and checked by one independent review (PR #1563 delta review of r2), not kernel-verified: (a)-(c) and Corollaries 1-3 under the stated conditions, including the transient bound of Step 6 and Corollaries 2-3. These give eventual growth at the ℓ1 light-cone rate in every direction; a transient at most diam_1(D) + 3/2, uniform in q and alpha; exit from a tube of half-width r by time 4r + 4; and no nonzero finitely supported solution that stays bounded for all time on the infinite lattice.

Not proved or not claimed:
- that the constants 3/2, 3 and 4r + 4 are sharp;
- exact per-step growth (c) for composite q (only the lower bound (b) is claimed there);
- a uniform-in-u statement of the form "the hull contains a translate of (t − T)·oct" beyond what (b) gives direction by direction;
- the tube case for periodic data with p | L_z (spot checks in section 5.7 and in the review show growth there; unproved), and for z-invariant non-periodic data;
- anything about finite tori beyond the wrap-around condition below, or about rounded, nonlinear or state-dependent rules.

*Finite torus.* Under A1 the lattice is a finite torus (Z/L)^d, on which every orbit is periodic, so "for all time" fails there. The torus solution is the periodization of the infinite-lattice solution, and by (a) the two agree while every coordinate extent of D + t·oct fits in the torus (max a_j − min a_j over D, plus 2t + 1, at most L, for each coordinate j). The statements above hold on the torus for those times. Corollary 2 applies on a torus whenever its exit time 4r + 4 falls within that window.

*Observer level.* The result excludes confined excitations only for this microscopic linear rule. It does not establish the absence of emergent string-like excitations at the observer level, where a nonlinear readout (for example M = exp(2 pi i Lie[dphi]/q)) and the induced measure enter (SM section 6.5). The section A.29 research target concerns what an embedded observer obtains, so that is the level at which a string bridge would have to be found or excluded. That question is S1', and it is open.

### 5.7 Exact computations run (spot checks, not proofs)

Integer arithmetic mod q (numpy), on boxes large enough that nothing reaches the edge within the run. Three scratch scripts, not in the repository, were used: `check.py` (sha256 ea6154d0a02e48c1d5b3dcb129ff386171acc1898662568c27ad2144adf7130f), `countercontrol.py` (26ca28f87eddb4bc442a707efc4bc2ecff77574624898f5d21120da1c202570a) and `tube.py` (dc20480fedf4001a5eeba8b529c8f8ad7ccf7f389ed204219cc6b0f227d3c979). The checked quantities were the light cone (a), the bound (b), and for prime q the exact increment (c) after T*_u. Directions: all of {−1,0,1}^d \ {0} plus up to twelve directions with entries in {−2..2}.

- Random and sparse data, d = 2 (26 steps) and d = 3 (14 steps); q ∈ {2,3,4,5,6,7,8,9,10,12,25}; alpha ∈ {1, the largest unit below q, 1/d when it exists}. That is 51 (d, q, alpha) cases with 25 or 8 trials each: 0 violations.
- Time-reversed point sources, (d, q, alpha, T0) = (2,5,1/2,6), (3,7,1/3,4), (2,2,1,7), (3,4,1,4). h_{x(t)}(e_1) decreased by 1 per step for T0 steps, hit a zero slice, then grew by 1 per step: 0 violations of (a)-(c).
- z-periodic data, d = 3, L_z ∈ {2,3,4,5,7}, q ∈ {2,3,4,5,7,9,10}, alpha = 1, transverse directions: 355 coprime runs with 0 violations. 163 runs with p | L_z, outside the claim, also showed 0 violations.
- Countercontrols (the checker must fail outside the hypotheses). The d = 1, alpha = 1 glider: 35 violations, with support size 1 translating. alpha = 0, d = 2, q = 7: 364 violations, period 4. alpha = 5, q = 10, with data in the mod-5 component where alpha ≡ 0: 224 violations; the same alpha with data in the mod-2 component, where alpha ≡ 1: 0 violations, as expected. For d = 1 with alpha = 2, q = 5 (alpha^2 ≢ 1), a point datum showed 0 violations; this is reported only and no d = 1 claim is made.

### 5.8 Classification (section A.31)

**ELABORATING**, not NEW. Step 4 of the audit method (literature search) was not done. That a nonzero finite configuration of a linear cellular automaton with a non-monomial rule grows linearly, and that free linear dynamics has no confined excitations, are standard in spirit ([background]: Martin-Odlyzko-Wolfram's polynomial treatment of additive cellular automata). What this record adds is the scoped statement for this rule, with the d ≥ 2 and unit-alpha conditions and an explicit transient. Bearing on Structure section 6.8(ii): the claim that nonlinear EFTs routinely emerge from linear-deterministic dynamics needs the nonlinear readout. For strings it is neither supported nor refuted by this result.

***

## 6. Classification table

| Item | Layer | Class |
|---|---|---|
| BFSS/IKKT outside A1-A6 | Paper | NO BRIDGE (scoped) |
| String theory in general outside A1-A6 | Unsupported generalization | OPEN |
| Confined excitations of the linear rule (d ≥ 2, alpha a unit mod every prime factor of q, infinite lattice) | Paper proof, checked by one independent review; not kernel-verified | EXCLUDED for this rule only; not a no-bridge result for observer-level strings |
| Observer-level strings or flux tubes (S1', earliest unsupported step) | Conditional on SM section 6.5 measure and confinement | OPEN/BLOCKED |
| Effective string dynamics | Missing mechanism | OPEN/BLOCKED |
| Quantum strings | Blocked by OI-QM | OPEN/BLOCKED |
| A/4 | Conditional calibration | SHARED STRUCTURE (consistency only) |
| Area scaling of horizon entropy | Posit (H-count, E3) | Input, not output |
| Holographic bound for general regions | None; tension with volume capacity | OPEN |
| Bulk-boundary duality | Absent | NO BRIDGE as currently specified |
| Four-feature overlap | Representation theorem plus analogy | SHARED STRUCTURE (generic) |
| Reverse C1-C4 witness | None | OPEN |

***

## 7. Smallest decisive mathematical question

**The r1 question, defined precisely.** For r ≥ 0, d ≥ 2 and admissible (q, alpha), let T_max(r) be the supremum, over nonzero finitely supported data with supp x(0) ∪ supp x(1) ⊆ Tube_r = {|a_1| ≤ r}, of the largest t such that supp x(s) ⊆ Tube_r for every 0 ≤ s ≤ t. The initial time is 0. Both initial slices are required to lie in the tube, and "staying" means every slice up to t does. Equivalently, every consecutive pair (x(s), x(s+1)) with s < t lies in the tube. The setting is the infinite lattice, or a torus before wrap-around (section 5.6).

**Reconciliation with section 5.** r1 posed "T_max ≤ c·r for all q, or T_max unbounded" as open while claiming a diameter-bounded transient in section 5; the two were inconsistent. With the transient bound of section 5 (Step 6), Corollary 2 gives T_max(r) ≤ 4r + 3, uniformly in q, alpha and d, and section 5.4 shows that T_max(r) is at least of order r. The same bound holds for transverse tubes and z-periodic data with gcd(L_z, q) = 1 (Corollary 3). So the r1 question is answered for this rule, by a paper proof checked by one independent review (PR #1563 delta review), not by a kernel-verified result. It is not answered for periodic data with p | L_z, for z-invariant non-periodic data, or for any nonlinear or observer-level rule.

**What remains decisive.** For the OI -> strings direction, the decisive link is now S1', the observer level. A decisive question there needs the observer readout and the induced measure of SM section 6.5 to be fixed first. It is not formulated in this revision, by owner decision not to expand the investigation. For holography the decisive question is unchanged: does any premise-admitted state class give an equal-time interior capacity bounded by O(\|dV\|)? Without one, H-count remains an independent posit and H5 fails.

***

## 8. Limitations

- Two primary sources were retrieved in r1: IMV in full and 't Hooft as an abstract only. Neither was re-retrieved in r2. All other literature is [background].
- The proof of section 5 is this record's own paper argument. It follows the reviewer's repair for Steps 3-5 and adds Step 6. Steps 1-6 and Corollaries 1-3 have been checked by one independent review (PR #1563 delta review of r2); they are independently reviewed paper results, not kernel-verified results, and no additional formalization is required at this stage by owner decision.
- The computations of section 5.7 are bounded spot checks (at most 26 steps, small supports, scratch scripts not on `main`).
- Structure sections 8, 10, 13.1.1 and 15 were read only through grep. Book chapters other than ch09 were read only through grep hits.
- No Lean identifiers were checked by this record beyond the two #1558 identifiers confirmed by the review.
- Noted but not audited and not added to section 9: SM line 92 calls alpha = 1/d "the substratum normalisation", while SM line 232 places it at an observer-level operator. Section 5 does not depend on which reading is correct.

***

## 9. Manuscript inaccuracies (listed, not edited)

### 9.1 Confirmed

- **M1. Structure section 7.5.1 and section 7.5.5; section 7.5.4 narrowed (verified against IMV, arXiv:1706.05392).**
  - IMV does not use a U(1)_{B-L} WGC or a tower argument. It applies the Ooguri-Vafa conjecture that non-supersymmetric AdS vacua are not stable to the SM compactified to 3D or 2D. It finds that a simplest scheme with three Majorana neutrinos is ruled out, that an extra very light Weyl fermion makes the Majorana possibility viable, and that Dirac neutrinos are viable for a light enough lightest neutrino. So Structure reverses the source: section 7.5.1 (line 403) attributes to it a U(1)_{B-L} WGC under which Dirac neutrinos need an unobserved tower, and section 7.5.5 (line 431) states that "the WGC predicts Majorana neutrinos because Dirac neutrinos require an unobserved tower of states" as a cross-validation.
  - *Conditions.* IMV's conclusion is conditional on the Ooguri-Vafa conjecture and on the stability of the lower-dimensional vacua concerned. The review reports that IMV itself says the assumption may be unjustified. The finding is therefore a tension with a conditional swampland argument, not a refutation of OI's Majorana branch.
  - *OI as the minimal Majorana case* depends on OI's light spectrum. The Weinberg operator with no gauge-singlet fermion falls into IMV's excluded minimal scheme only if OI has no additional light Weyl fermions or axion-like states. This record does not establish that.
  - *Section 7.5.4, narrowed.* Section 7.5.4 concerns the AdS Distance Conjecture, a different conjecture, so r1's claim that IMV "undercuts" it is withdrawn as stated. The point that survives is that "OI's emergent QFT does not predict an AdS minimum" does not make AdS-based swampland criteria inapplicable. Lower-dimensional compactifications of a dS-like 4D theory can have AdS vacua, which is IMV's method.
- **M2. Structure section 7.5.2.** "Dynamical near-de Sitter satisfies" the refined dS conjecture is unsupported. The conjecture constrains a scalar potential, which the RVM reading does not supply. A near-Lambda quintessence reading conflicts with c ~ O(1) [background: Agrawal-Obied-Steinhardt-Vafa]. It also contradicts ch09 section 9.6 ("in tension").
- **M3. Structure sections 7.7.1, 7.7.4 (table) and 12.4 (Level-1 row).** The "holographic principle holds", "produces the holographic bound", and holography as a "structural consequence of partial-trace observation" and "universal" are all unsupported. Area scaling is the E3 input and the H-count posit, the lattice capacity is volume-scaling, and the area scaling in the SM lemma comes from range-1 locality plus the uniform state class, not from partial trace. The sentence "A is a structural consequence ..." in section 7.7.1 is garbled. Related: book ch07 line 61 says "the emergent theory ... satisfies both bounds", an unsupported universal claim.
- **M4. SM line 46.** "S = A/epsilon^2 ... follows from the holographic entropy bound" conflicts with ch07 line 61 (citing the bounds as motivation is circular), with GR (the count is fixed by definition under H-count) and with Substratum E3 (a theoretical input). It also omits sigma (SM line 90: eta = sigma/epsilon^2).
- **M5. Substratum, ER=EPR remark (end of section 3, lines 239 and 243).** "The holographic dictionary maps shared boundary modes ..." and weak ER=EPR being "reproduced" are unsupported. No dictionary exists (Structure section 7.7.1), the emergent geometry and field equations are open (GR section 8.7, G3), and operational entanglement is not established (#1558). The remark also calls the result a "sharp empirical signature" and then "not a testable one at present".
- **M6. Structure section 7.7.4, final paragraphs.** The claims that the proposal "does hold at the level of IR effective theory" and that the two frameworks "share the IR effective theory" are unsupported. Section 14.6 itself says they are not operationally equivalent, and Precondition 2 is unmet.
- **M7. Structure abstract and sections 1.5, 11.1 and 11.3.** Shared classes are called "Confirmed"; "both frameworks produce Born rule"; "the specific gauge group transports" (section 11.1), which contradicts the abstract's "not as a specific output" and sections 14.4/14.6. AdS/CFT is called "a direct analog" of the Stinespring lift, while section 14.2 leaves the analogy open.
- **M8. Structure sections 13.1.4 and 13.4 (Limit 1).** "All four programs (string theory, ...) fail A1-A6" generalizes from BFSS/IKKT to string theory as a whole (finite test to universal claim).
- **M9. ch09 section 9.5, mirrored in FULL.md.**
  - "String theory is itself an emergent description in the framework's hierarchy; substratum logically prior" contradicts Structure sections 7.1 and 7.8.
  - "Both predict the SM gauge group" is not true of string theory.
  - Recovery (i) lists AdS/CFT as shared content, but Structure says "No".
  - "Some matrix models are bridge-compatible" contradicts Structure section 6.9.
  - The A2 entry ("deterministic Hamiltonian evolution satisfies this") contradicts Structure section 6.2.
  - A5 is misdescribed as visible-sector linearity (against Structure section 6.5).
  - "Structure.md Part II" should be Part I.
  - BFSS is listed twice.
- **M10. ch09 section 9.6 (line 224), narrowed.** The sentence "both are evidence for the universality-class commitment that both programs share" overstates the OI side. OI's 1/4 is a consistency fit to the Hawking normalization (GR section 5), as ch09 line 328 itself states ("a consistency relation of the horizon calibration with no direct test"). ch09 already identifies Strominger-Vafa as concerning extremal black holes. The residual point is that the two coefficients concern different horizons, OI's cosmological-horizon calibration and extremal BPS black holes, so their agreement does not by itself exhibit a shared commitment.

### 9.2 Listed in r1, not confirmed by the review (not findings)

- **M11 (Structure, internal cross-references): not confirmed.** Section 7.6 exists and discusses the partial recoveries, so the section 7 introduction's reference is accurate. The section 6.8 forward reference to section 7.8 points to a section that restates the negative result: awkward, not wrong.
- **M12 (Structure section 7.7.3, "T-duality: No"): not confirmed.** The "No" is explicitly about momentum-winding T-duality, and section 7.7.3 already labels the universality-class analogues speculative. Kramers-Wannier duality and the Pontryagin self-duality of Z/q (position-momentum) [background] are not R ↔ alpha'/R dualities.
