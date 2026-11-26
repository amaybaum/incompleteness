# Issue #1556 (OI-STRING): paper-only bridge audit and dependency map

## 0. Status, pin and sources

- **Status:** paper-only, read-only research record for the Exploratory tier. Nothing was written to the repository, git or GitHub, and nothing was computed. No premise or manuscript change is made or proposed here; inaccuracies are listed in section 9 and not edited. Independent non-author review is still required.
- **Corpus pin:** `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`. Read via `git show` from the full clone.
- **Issue context:** the body and the owner activation comment of #1556 (2026-11-25) were read. The findings comments of #1558 were also read. #1558 found that OI's observer interface is operationally classical (kernel: `obsTheory_nonnegBounded`, `sourcing_rule_independent`), that interference is not derived, and that quantum emergence is open. These are treated as constraints throughout.
- **Corpus read:**
  - `papers/Structure.md`: sections 1-7, 9.1, 9.8, 11, 12.4, 13.1.4 and 14.1-14.6 in full; other sections by grep.
  - `book/ch09-universality.md`: sections 9.5-9.6; its mirror in `book/The-Incompleteness-of-Observation-FULL.md` is confirmed to contain the same text.
  - `papers/GR.md`: sections 2.3, 3.1, 5 and 8.7, plus grep hits.
  - `papers/SM.md`: section 2 (lines 46-122), the area-law lemma and its proof, section 6.5, Theorem 22.
  - `papers/Substratum.md`: E3 and the ER=EPR remark at the end of section 3.
  - `papers/Main.md`: C3, Lemma 1.
  - `book/ch02` and `book/ch07`: grep hits.
  - Corpus-wide grep for: string, holograph, AdS, Bekenstein, area law, WGC, soliton, vortex, flux tube, confinement, winding.
- **Literature retrieved from primary sources:**
  - Ibanez, Martin-Lozano, Valenzuela, arXiv:1706.05392: full text.
  - 't Hooft, "Discreteness and determinism in superstrings", arXiv:1207.3612: abstract only.
- **Literature not retrieved, marked [background] below:** BFSS 1996; Maldacena 1997; Strominger-Vafa 1996; Strominger dS/CFT 2001; Ryu-Takayanagi 2006; Almheiri-Dong-Harlow 2014; Pastawski-Yoshida-Harlow-Preskill 2015; Heemskerk-Penedones-Polchinski-Sully 2009; Srednicki 1993; Eisert-Cramer-Plenio 2010; Bousso 2002; Goddard-Goldstone-Rebbi-Thorn 1973; Polyakov 1981; Luscher 1981; Polchinski-Strominger 1991; Aharony-Komargodski 2013; Lee-Lerche-Weigand 2019; Ooguri-Vafa 2016; Ooguri-Palti-Shiu-Vafa 2018; Agrawal-Obied-Steinhardt-Vafa 2018; Savit 1980; Martin-Odlyzko-Wolfram 1984.
- **Goal link (section A.47):** #1556. This decides whether OI and string theory share more than generic observable-level structure, and where each bridge direction first fails.

***

## 1. The existing correspondence and its support

| Claim (location) | Support class | Assessment |
|---|---|---|
| BFSS/IKKT fail A1 (without a finite-value regulator), A2 and A5; A3 fails on the natural reading; A4 holds; A6 holds conditionally (Structure section 6) | Paper argument; standard facts [background] | Sound for the models examined. It is a scoped no-bridge result for matrix models, not for string theory in general. |
| No substratum-level equivalence between OI and string compactifications (sections 4.3, 6.9, 7.1, 7.8) | Paper argument, scoped to matrix models | Sound as scoped. Sections 13.1.4 and 13.4 overgeneralize it (M8). |
| Area law, A/4 and the holographic bound emerge as a "structural consequence of partial-trace observation" (sections 7.7.1, 7.7.4, 12.4) | Actual support: A/4 is a conditional calibration (GR section 5, under H-count, H-slope, H-frame, H-Hawking, boost structure and detailed balance). Area scaling of horizon entropy is the H-count hypothesis (GR section 2.3), motivated by the E3 input (Substratum section 3.1) | Overstated (M3). Area scaling is put in, not derived. The holographic bound for general regions has no support. |
| Full AdS/CFT does not emerge; dS holography open (section 7.7.1) | Analysis | Consistent. Contradicted by ch09 Recovery (i) and by the Substratum ER=EPR remark (M5, M9). |
| Graviton modes open, a Level-G3 target (section 7.7.2) | Correctly scoped | Consistent with GR sections 3.2 and 8.7. |
| T-duality "No"; S-duality speculative (section 7.7.3) | Analogy | The support only shows that winding modes and compact dimensions are absent. Lattice dualities are not examined (M12, low confidence). |
| Four-feature audit (sections 14.1-14.6) | Representation-level facts true of any quantum theory with subsystems (Stinespring); analogy to holographic EFT [background] | Carefully scoped in section 14 itself. Restated more strongly in the abstract and in sections 1.5, 11.1, 11.3 and 7.7.4 (M6, M7). |
| WGC "cross-validates" OI's Majorana neutrinos (sections 7.5.1, 7.5.5) | Misreported citation (verified) | Reversed (M1). |
| Type II RVM "satisfies" the refined dS conjecture (section 7.5.2) | Unsupported | M2; also contradicts ch09 section 9.6. |
| Observer admission C1-C4 for compactifications (section 7.9) | Candidate translation only; "no such witness is exhibited" | Correctly scoped in section 7.9. |
| ch09: string theory is an emergent description within OI's hierarchy (section 9.5) | None | Contradicts Structure sections 7.1 and 7.8, and the #1556 boundary (M9). |

***

## 2. Direction OI -> strings: dependency map

| Link | Content | Status |
|---|---|---|
| S1 | Stable extended excitations of the native substratum update | **Negative under the proposition of section 5** (paper derivation by this investigation, unreviewed) |
| S1' | Extended excitations at the observer or coarse-grained level | **Unsupported.** Candidate routes, both open: (a) confining flux tubes of the induced SU(3); (b) vortex lines of the lifted compact phase |
| S2 | Effective equations of motion (Nambu-Goto plus corrections) derived from the update | **Unsupported.** A tension needs a real-valued conserved energy; the exact rule conserves energy only mod q (SM section 6.5) |
| S3 | Quantization | **Blocked** by the open OI-QM operational reconstruction (#1558) |
| S4 | Critical-string content: worldsheet CFT, Regge tower, closed-string graviton, T/S-duality | Not derived (Structure section 7.7.4). Graviton sector open at G3 |
| H1 | A finite observable boundary | Conditional: GR section 2 horizon partition, with C4 "not presently discharged" |
| H2 | Area-scaling correlations | Paper proof: I(V;V^c) <= \|dV\| log2 q in the uniform state class under hypothesis H-mu (SM area-law lemma). This is a generic consequence of range-1 locality |
| H3 | Area-scaling horizon entropy | **Posited:** H-count (GR section 2.3), with E3 as theoretical input |
| H4 | The 1/4 coefficient | Conditional calibration (GR section 5). It is equivalent to the Hawking normalization by construction |
| H5 | A holographic entropy bound for general regions | **Unsupported.** The substratum capacity count log2\|C_H\| = \|H\| log2 q scales with volume (SM Theorem 22) |
| H6 | A bulk-boundary duality: boundary system and dynamics, an algebra isomorphism on a code subspace, correlator dictionary, reconstruction | **Absent.** Partial trace is a many-to-one channel, not an isomorphism. OI's cosmology is dS |

**Earliest unsupported step:** S1/S1'. No OI-native description has been shown to contain a stable extended excitation. At the substratum level such excitations are excluded if the proposition of section 5 holds. For holography the earliest unsupported step is H5, and H6 is absent.

***

## 3. Direction strings -> OI: dependency map

| Link | Content | Status |
|---|---|---|
| R1 | A specified string model in OI's structural class (A1-A6) | Fails for BFSS/IKKT at A2 and A5 (Structure section 6). One candidate is not examined in the corpus: 't Hooft's discretized light-cone superstring (arXiv:1207.3612, abstract verified). It claims a map from deterministic discrete string states to a basis of the quantized superstring, and its free worldsheet is linear. It is free (g_s = 0), uses a target-space lattice, and its status is single-author [background] |
| R2 | A declared visible/hidden partition with record dynamics satisfying C1-C4 | **Unsupported.** Structure section 7.9: "No such witness is exhibited". C1-C4 are formulated for finite deterministic substrata, and a quantum-substratum analogue of C4 needs an instrument specification. Free strings form no bound records |
| R3 | Agreement at the level of record statistics | **Trivially satisfiable and so uninformative.** Main's finite-law and intervention-dilation theorem (cited at GR section 2.3) gives a reversible realization for any finite record table. Representing is not deriving (section A.29) |
| R4 | Observational equivalence (Def. 9.3: a *-isomorphism of algebra-channel pairs) | Open (Structure section 11.2). Precondition 2, that some compactification reproduces the SM, is itself unmet (section 1.2) |

**Earliest unsupported step:** R2. A discriminating test must use the string model's own microdynamics restricted to a declared observer; R3 cannot discriminate. At the structural-class level, R1 is unsettled rather than closed, because the free-string candidate has not been examined.

***

## 4. The six questions

| Question | Conclusion | Support class | Conditions |
|---|---|---|---|
| 1. Emergent strings | No stable extended excitations exist in the exact linear substratum (section 5). Observer-level strings are not derived. The QCD-flux-tube route depends on two things: the under-determined induced gauge measure of SM section 6.5 (the natural polar map gives a Haar, confining pushforward numerically, while the near-identity measure is conjectured), and confinement, listed as open in ch10 and Complexity | Paper derivation (unreviewed) plus corpus citations | 3 does not divide q; exact linear rule; infinite lattice or times before wrap-around |
| 2. Effective dynamics | Not derivable now. There is no native real-valued conserved energy, hence no tension. A Nambu-Goto or effective-string description [background] presupposes it | Missing mechanism | |
| 3. Quantization | Classical extended excitations would still need: (a) operational quantum structure, which is open (#1558); (b) for critical strings, anomaly cancellation (D = 26 or 10 [background]), which OI's fixed d = 3 lattice does not supply; (c) for effective (non-critical) strings, only a long-distance EFT [background]. Inserting quantum rules would be representation, not derivation | Missing mechanism | |
| 4. Holography | Restricted observation gives a boundary, locality area laws and a calibrated A/4, all conditional or posited. It does not give a duality. Recovering bulk data from a boundary history over a light-crossing time is classical observability (a control-theory notion, offered as a suggestion only), not equal-time holography | Paper proof (H2), posit (H3), conditional (H4), absent (H5, H6) | |
| 5. Reverse correspondence | No specified string model has a C1-C4 witness. Agreement at the record level is trivial (R3). One structural-class candidate (free discretized superstring) is unexamined | Open | |
| 6. Universality | The similarity is generic-structural: Born-form subsystem statistics and Stinespring dilations hold for any quantum theory with subsystems, so they do not discriminate. Memory and gauge restriction are shared only as patterns. Agreement on the 1/4 coefficient is consistency with the Hawking normalization (section A.23 consistency axis), not shared microphysics. Everything string-specific is analogy | Representation theorem plus analogy | |

***

## 5. New finding, scoped: no confined excitations of the exact linear rule

**Proposition (paper derivation by this investigation; unreviewed; needs independent check).** Take the OI update x(t+1) = P x(t) - x(t-1) mod q (SM line 106), with symbol P = alpha * (sum of the six nearest-neighbour shifts) and alpha = 1/d, which exists only when 3 does not divide q (SM line 92). Then for every nonzero, finitely supported initial pair, after a transient bounded by the diameter of the initial data, the convex hull of the support expands at unit (light-cone) speed in every direction. No nonzero solution stays confined to a bounded region or a bounded transverse tube for all times.

**Sketch.**
1. For prime q, finitely supported configurations form the Laurent ring F_p[x^±, y^±, z^±], which is an integral domain.
2. The solution is x(t) = U_t(P) f1 - U_{t-1}(P) f0, where U_t is a monic Dickson-type polynomial of degree t-1 in P.
3. Newton polytopes multiply under products (Ostrowski), so NP(U_t(P) f) = (t-1) * octahedron + NP(f). The vertex terms cannot cancel: the lower powers of P have smaller polytopes.
4. For composite q, use the Chinese remainder theorem, and for prime powers the p-adic filtration: divide out the minimal valuation and reduce mod p.
5. Line-extended excitations, periodic in z with p not dividing L_z, reduce to the same argument over F_{p^m}.
6. Frobenius sparsity at times p^k [background: Martin-Odlyzko-Wolfram] thins the interior of the support but leaves its extreme points occupied.

**Scope and limits:**
- It covers the exact linear rule only, not rounded or nonlinear variants.
- It concerns exact confinement. Long but finite confinement is excluded only beyond the transient.
- It applies equally to particle-like localization. Native strings would therefore have to be observer-level objects, created by the nonlinear readout (for example M = exp(2 pi i Lie[dphi]/q)) and the measure, which moves the question onto SM section 6.5 and the OI-QM programme.

**Section A.31 classification:** NEW (scoped negative). The Structure section 6.8(ii) claim, that nonlinear EFTs routinely emerge from linear-deterministic dynamics, needs exactly this nonlinear readout and is not supported for strings.

***

## 6. Classification table

| Item | Layer | Class |
|---|---|---|
| BFSS/IKKT outside A1-A6 | Paper | NO BRIDGE (scoped) |
| String theory in general outside A1-A6 | Unsupported generalization | OPEN |
| Native substratum strings | Paper derivation (unreviewed) | NO BRIDGE (scoped, pending review) |
| Observer-level strings or flux tubes | Conditional on SM section 6.5 measure and confinement | OPEN/BLOCKED |
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

Independently verify the proposition of section 5, then decide its finite-time strengthening. For tube radius r and alphabet q (3 not dividing q), find the maximal time T_max(r, q) for which a nonzero configuration of the exact OI rule stays within the tube.

- If T_max <= c*r for all q, native strings are excluded at the substratum level.
- If T_max grows without bound for some q, quasi-stable linear strings exist.

This is finite linear algebra over Z/q, so it is decidable, and it decides link S1. The secondary decisive question for holography is whether any premise-admitted state class gives an equal-time interior capacity bounded by O(\|dV\|). Without one, H-count remains an independent posit and H5 fails.

***

## 8. Limitations

- Only two primary sources were retrieved, one of them as an abstract only. All other literature is [background].
- The proposition of section 5 is my own unreviewed derivation.
- Structure sections 8, 10, 13.1.1 and 15 were read only through grep.
- No Lean identifiers were checked, and no computation was run.
- The T-duality lattice-duality point (M12) is unverified.
- The book chapters other than ch09 were read only through grep hits.

***

## 9. Manuscript inaccuracies found (listed, not edited)

- **M1. Structure section 7.5.1, also sections 7.5.5 and 7.5.4 (verified against arXiv:1706.05392).** The paper does not use a U(1)_{B-L} WGC. It applies the Ooguri-Vafa non-SUSY AdS conjecture to the SM compactified to 3D or 2D. It finds that a minimal scheme with three Majorana neutrinos is ruled out (an extra light Weyl fermion makes it viable), and that Dirac neutrinos are viable for a light enough lightest neutrino. OI's branch, the Weinberg operator with no gauge-singlet fermion, is the minimal Majorana case. So this is tension, not cross-validation. The argument also applies to any SM-like 4D EFT, which undercuts section 7.5.4's "not directly applicable".
- **M2. Structure section 7.5.2.** "Dynamical near-dS satisfies" the refined dS conjecture is unsupported. The RVM has no scalar potential, and a near-Lambda quintessence reading conflicts with c ~ O(1) [background: Agrawal-Obied-Steinhardt-Vafa]. It also contradicts ch09 section 9.6 ("in tension").
- **M3. Structure sections 7.7.1, 7.7.4 (table) and 12.4 (Level-1 row).** The "holographic principle holds", "produces the holographic bound", and holography as a "structural consequence of partial-trace observation" and "universal" are all unsupported. Area scaling is the E3 input and the H-count posit, the lattice capacity is volume-scaling, and partial trace does not imply area laws. In addition, the sentence "A is a structural consequence ..." in section 7.7.1 is garbled. Related: book ch07 line 61 says "the emergent theory ... satisfies both bounds", an unsupported universal claim.
- **M4. SM line 46.** "S = A/epsilon^2 ... follows from the holographic entropy bound" conflicts with ch07 line 61 (citing the bounds as motivation is circular), with GR (the count is fixed by definition under H-count) and with Substratum E3 (a theoretical input). It also omits sigma.
- **M5. Substratum, ER=EPR remark (end of section 3).** "The holographic dictionary maps shared boundary modes ..." and weak ER=EPR being "reproduced" are unsupported. No dictionary exists (Structure section 7.7.1), the emergent geometry and field equations are open (GR section 8.7, G3), and operational entanglement is not established (#1558). The remark also calls the result a "sharp empirical signature" and then "not testable".
- **M6. Structure section 7.7.4, final paragraphs.** The claims that the proposal "does hold at the level of IR effective theory" and that the two frameworks "share the IR effective theory" are unsupported. Section 14.6 itself says they are not equivalent operationally, and Precondition 2 is unmet.
- **M7. Structure abstract and sections 1.5, 11.1 and 11.3.** Shared classes are called "Confirmed"; "both frameworks produce Born rule"; "specific gauge group transports" (section 11.1), which contradicts section 14.4/14.5 "not as a specific output"; and AdS/CFT is called "a direct analog" of the Stinespring lift, while section 14.2 leaves the analogy open.
- **M8. Structure sections 13.1.4 and 13.4 (Limit 1).** "All four programs (string theory, ...) fail A1-A6" generalizes from BFSS/IKKT to string theory as a whole (finite test to universal claim).
- **M9. ch09 section 9.5, mirrored in FULL.md.**
  - "String theory is itself an emergent description in the framework's hierarchy; substratum logically prior" contradicts Structure sections 7.1 and 7.8.
  - "Both predict the SM gauge group" is not true of string theory.
  - Recovery (i) lists AdS/CFT as shared content, but Structure says "No".
  - "Some matrix models are bridge-compatible" contradicts Structure section 6.9.
  - The A2 entry ("deterministic Hamiltonian evolution satisfies this") contradicts Structure section 6.2.
  - A5 is misdescribed as visible-sector linearity.
  - "Structure.md Part II" should be Part I.
  - BFSS is listed twice.
- **M10. ch09 section 9.6.** The 1/4 agreement is called "evidence for the universality-class commitment". It is a consistency fit to the Hawking normalization (GR section 5), and Strominger-Vafa concerns extremal BPS black holes, not dS horizons.
- **M11. Structure, internal cross-references.** Section 6.8 says "the negative conclusion in section 7.8"; the section 7 introduction places the recoveries in section 7.6, but they are in section 6.8.
- **M12. Structure section 7.7.3 (low confidence).** "T-duality: No" is stronger than its support. Lattice dualities (Kramers-Wannier/Z_N; Z/q is Pontryagin self-dual [background]) are not examined; "not established" would match the support.
