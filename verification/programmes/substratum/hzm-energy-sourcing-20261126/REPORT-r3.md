# HZM-ENERGY-SOURCING, unit C (lane 3): do existing premises supply H-ZM and the SM:811 energy? Report, r3

**WIP / UNVERIFIED. Model-written research record, paper-only.**

Revision r3 is REPORT-r2.md (`04248fc9`) with only these edits: the title, this note, the three
wording corrections N1–N3 of the delta review of r2 (PR #1594 comment 7190223659, ACCEPT WITH
NITS), as the owner directed (#1169 comment 7190274734, amaybaum, 2026-11-26T11:06:26Z: "Apply the
three wording corrections."), and the mention of Main:306–312 in D-1. N1 is in §3, the Main:262
row, reason (2); N2 in §1, W-1; N3 in §1, D-8. Every other line is r2's.

Revision r2 applies findings 1–14 of the independent review of r1. The review text is posted on
PR #1594 as the comment of 2026-11-26T10:56:45Z, from the owner's account (amaybaum), with review
verdict REVISE. r1 is REPORT.md at `266fbc60`, and the changes are listed in CHANGES-r2.md.

Nothing here is adopted, proposed for the manuscripts or authorized beyond the unit scope. No
premise is adopted, weakened or changed, and no energy is chosen.

Evidence layers:
- source reading at [P], reproducible by the commands of §2;
- mathematical derivation on paper, labelled per step:
  - [A] exact hand algebra here;
  - [W] reasoning here;
  - [P] text quoted at [P];
  - [K] a kernel-checked Lean statement on `main`, cited by module and identifier and not rebuilt
    here.

The independent review of r1 re-derived U1–U3, F-stag, §5.2 and F-slice (a)–(d) and re-extracted
every quote. These remain reviewed paper derivations, not independently verified theorems. No
computation was run and no Lean was built.

- **Plan:** `PLAN.md` in this directory, commit `d4f97b5387fe448baeebe3ebd2caae41da89f259`.
  Deviations are listed in §1.
- **Pinned main commit [P]:** `353a066f18766837fed8c7f58507e09ff549b1a4`. Every file:line is at
  [P].
- **Accountable Issues:** #1217 and #1049; programme #1169.
- **Authorization and Goal link:** as in PLAN.md (#1169 comment 7189139613, author amaybaum,
  created 2026-11-26T10:16:17Z).
- **Unit A:** not read; its record is not on `main` at [P].
- **Scope of negatives:** every negative statement below is scoped to the searched scope of §1 and
  §2. A target found unsourced means unsourced within that scope, never impossible, and never
  evidence that no premise could supply it.

## 0. Summary

| Target | Verdict (PLAN §5 branch) | Decisive sources on `main` | Governance records (not scientific support) |
| --- | --- | --- | --- |
| T1a, invariance under the constant static shift | **Substratum interface:** contradicted for the partitions Main specifies. **Observer of SM §4.1:** contradicted conditional on the register transferring through the SM:232 bridge (O2, open); otherwise unsourced within the searched scope. **Conditional sources (partial):** the shift-invariant interface 𝒜_C, or a physical amplitude-scale gauge, both open. Individual readouts are invariant: the SM §6.5 link-difference map, E and its shells at α = 1/d, and the uniform counting measure. | Main:84–89; Main:736 (viii); Main:368; Main:298; Main:376; Substratum:249; SM:96; Substratum:270–272; SM:811; A5-LINEAR-AFFINE §3.3.1 | Owner decisions Q1 and Q2, #1049 comment 6624263637 |
| T1b, quotient by the constant static mode | **Unsourced** within the searched scope. It coincides with T1a for itinerary registers (§4.3) and carries T1a's two-level verdict and conditional sources. | PassiveQuotient, ObservabilityQuotient [K] | — |
| T2a, invariance under the staggered static shift | **Substratum interface:** contradicted for the partitions Main specifies. **Observer of SM §4.1:** contradicted conditional on the transfer (O2); otherwise unsourced within the searched scope. **No conditional source** was found within the searched scope. | as T1a; §5.2 [A]; A5-LINEAR-AFFINE N6 | — |
| T2b, quotient by the staggered static mode | **Unsourced** within the searched scope. | as T2a | — |
| T1Z, T2Z (secondary) | **Unsourced** within the searched scope. | §6 | — |
| T3, the SM:811 energy | **Linear lift: defined (E).** The T3b positive-definiteness requirement fails on the full space (U1) and holds only on invariant constraint slices, which the text requires and does not specify. The selecting condition is named: which conserved labels the observer's records fix. **Affine lift at resonance (b ≠ 0): unspecified.** No conserved function meets the requirement (U2). The choice among Q′, E_⊥ and E_⊥ + f(Q′_0) is a choice of treatment for the uniform sector (U3). | SM:292, SM:294, SM:296, SM:811; GR:699; Main:60; Main:736 (iv) | — |

Two further findings fall outside the strict targets:

- **(F-slice)** An alternative to the H-ZM quotient exists. It yields a unique J on every label
  sector (§5.3, [A]/[W]), conditional on lane 2's Theorem 1, a model-written record. Whether it
  serves the consumers of lane 2's Proposition 5 (Theorem 5's Σ, H-PF) is open (O3).
- **(F-stag)** At α = 1/d with L even, E_⊥ is only semidefinite. Its shells do not confine the
  staggered null direction (§7.4, [A]).

Productivity verdict (§10): **gem**, resting on U1 (modestly NEW), U3 and F-stag (NEW), and on
F-slice (NEW, conditioned as above).

## 1. Execution against the plan, deviations and widenings

The plan says the search may be widened but never narrowed. The execution falls short in the
places below. Each is named, and every verdict is scoped to what was executed.

- **D-1 (S1, reading set).**
  - Read in full:
    - Main §1.2–§1.3 (Main:30–80);
    - Main §1.4 (Main:82–91);
    - Main §3.3 (Main:364–438);
    - the §4.5 posit ledger (Main:726–738);
    - Substratum:90–106 and Substratum:247–300;
    - SM:42–57, SM:88–96, SM:220–283, SM:292–298, SM:585 and SM:799–811.
  - Main §3.1, §3.2 and §3.4 (Main:206–362 and Main:439–671): every sentence was screened with two
    fixed vocabularies:
    - (i) gauge, shift, translat, offset, relabel, absolute, field value, redundan, unobserv,
      indistinguish, "physically equivalent", zero mode, null (50 sentences);
    - (ii) symmetr, readout, interface, registered, lattice, site, field, wave, amplitude,
      "invariant measure", "counting measure".

    Each hit was read in its sentence. Paragraphs were read in full where a hit concerned symmetry,
    readout or the spatial partition: Main:244, 260, 262, 274, 294–304, 346, 598, 632, 662, 666.
    Main:306–312, which the delta review of r2 found with a different vocabulary, was read in full
    for r3: Lemma 2 (channel normal form), with Φ_G a uniform mixture over visible Weyl translations
    α ∈ im(A⁻¹B), written on the absolute configuration basis of the q = 2 realization. It is not a
    candidate, and it supports the absolute register at the specified partitions.
    The rest of §3.1, §3.2 and §3.4 was not read word for word.
  - SM:312–344 and SM:360–374 were read only through lane 2's inputs.
  - Structure, GR, Introduction and Methodology were read through their S4 hits and the passages
    those hits cite.
- **D-2 (S4, Group N in scope D).**
  - Every hit line in scope (D) was read for 25 terms: zero mode, zero-mode, null mode, null
    direction, null sector, constant mode, uniform mode, uniform sector, uniform shift, constant
    shift, static shift, shift symmetry, field translation, staggered mode, alternating mode,
    period two, period-two, Dirichlet, energy seminorm, modulo constants, link difference,
    difference observable, noncompact shell, E_⊥ and energy norm. That is 133 lines outside the
    lane 1 and lane 2 directories.
  - The other Group N terms were read in (D) only within the S3 closure set and the S6 records.
    The rest is the **unswept Group N remainder in (D)**.
- **D-3 (S4, \pi and quotient in scopes A and B).** Match-centred snippets were screened, with
  escalation to full context when a snippet named a mode, a staggered structure, a Brillouin-zone
  corner or a zone.
- **D-4 (S4, Group B in A and B).** Every hit of unobservable, redundan and "where the inverse
  exists" was read. Gauge was widened by W-1, below. Hits of observable, invariant, energy,
  Hamiltonian, shell and regulari were read only where S1–S3 led. The rest is the **unswept Group
  B remainder in (A) and (B)**, beside the remainder in (D) that the plan already provided for.
- **D-5 (S5, Lean).**
  - All 252 `.lean` modules were listed.
  - Read at docstring and statement level: SubstratumInterfaceAudit, WaveSubstratumUnbounded,
    ShellAssignment, PassiveQuotient, ObservabilityQuotient and SecondOrderCircuit, plus the census
    notes that the narrow terms hit.
  - The high-volume Lean hits were read at module level only: quotient 292, Q' 155, positive
    semidefinite 64, k = 0 62.
- **D-6 (S6, records).**
  - Read in full: lane 2 PLAN.md and REPORT-r2.md; lane 1 REPORT-r2.md §2.3–§3 and §8.
  - Read at the passages its hits and §3.3.1 cite: A5-LINEAR-AFFINE.
  - Read at their hit lines: A5-Q4-STAGE2D, q3-a6-offsets ASSESSMENT and reassess-1049.
  - Not read: POSIT-MIN, Q3, Q4 and BRIDGE-UNIT1. These are unverified records, usable only as
    pointers.
- **D-7 (S4, grep mode).** PLAN §4.2 specifies `git grep -n -i -I -E`. The sweep ran
  `git grep -c -i -I -F`, fixed-string matching, because `(-1)^{` is not a valid extended regular
  expression. Counts are matching lines.
- **D-8 (scope gaps).** Two file sets fall outside every scope of PLAN §4.1:
  - the 95 non-`.lean` files under `verification/lean/` and `verification/lean-mathlib/`. Scope C
    takes `*.lean` only, and scope D excludes these directories.
  - the 147 files under `papers/` that are neither `.md`, `.tex` nor `.pdf`.

  Both are **unswept remainders**. The review of r1 read the narrow-term hits it checked: gauge-phase null
  directions and passive-bath energy shells in the first set, and lattice-QCD doubler-mode
  exclusions in the second. None was a field-shift premise. This record does not rest on that
  reading.
- **W-1 (recorded widening, Group B "gauge" in scope A).** Every `papers/*.md` line containing
  "gauge" together with shift, translat, affine, offset, "field value" or "absolute value" or
  "absolute amplitude" was read: 28 lines.
  - Judged elsewhere in §3: Main:262, Main:736, SM:96, Substratum:98, Substratum:270 and
    Structure:260.
  - The other 22 concern:
    - energy shifts or offsets of an emergent generator or of the vacuum: GR:372, 581, 605, 751;
      Main:244, 260, 274, 346, 666;
      Structure:150; Substratum:296, 395;
    - a π-shift in momentum: SM:1202;
    - translation invariance of dispersion or Hamiltonian: SM:50, 561;
    - observer-centred partitions breaking translations: SM:136;
    - fitting or matching-scale offsets and shifts: SM:130, 693, 711, 765, 767;
    - unrelated: GR:356.

  W-1 adds no candidate. The review of r1 ran the same screen with the same outcome.

## 2. Sweep log (S4)

All counts are at [P]: matching lines, case-insensitive, fixed-string, binary files excluded. For
each term t, run from the repository root:

    P=353a066f18766837fed8c7f58507e09ff549b1a4
    A: git grep -c -i -I -F -e "$t" $P -- 'papers/*.md'
    B: git grep -c -i -I -F -e "$t" $P -- 'book/*.md'
    C: git grep -c -i -I -F -e "$t" $P -- 'verification/lean/*.lean' 'verification/lean-mathlib/*.lean' 'verification/lean-manuscript-census.json'
    D: git grep -c -i -I -F -e "$t" $P -- 'verification/*' ':(exclude)verification/lean/*' ':(exclude)verification/lean-mathlib/*' ':(exclude)verification/lean-manuscript-census.json'

Per-file counts are summed within each scope. The review of r1 reproduced every count.

**Group N** (term: A / B / C / D):
- zero mode 2/0/0/20; zero-mode 0/0/3/30; null mode 2/8/0/27; null direction 2/0/0/6;
- null sector 0/0/0/21; null space 2/0/3/4; constant mode 0/2/0/3; uniform mode 0/4/0/25;
- uniform sector 0/0/0/23; uniform shift 0/2/0/70; constant shift 1/0/0/3; static shift 0/0/0/9;
- shift symmetry 2/0/0/5; shift invariance 0/0/0/0; field translation 0/0/0/2; global shift
  0/0/0/0;
- Goldstone 5/4/0/5; staggered mode 0/0/0/3; alternating mode 0/0/0/2; period-two 0/0/5/1;
- period two 0/0/1/5; pi mode 0/0/0/0; π-mode 0/0/0/0; \pi 217/293/0/566; (-1)^{ 9/4/0/16;
- (−1)^ 0/0/8/29; k = 0 0/0/62/104; k=0 4/2/0/46; zero momentum 0/0/0/0; Dirichlet 0/0/0/7;
- energy norm 0/2/0/7; energy seminorm 0/0/0/2; seminorm 0/0/1/4; quotient 28/36/292/1198;
- modulo constants 0/0/0/2; up to a constant 0/0/3/10; up to gauge 7/4/1/68;
- link difference 0/0/0/5; first difference 12/4/2/28; difference observable 0/0/0/2;
- relational observable 0/0/0/0; noncompact shell 1/0/0/6; positive definite 1/0/6/50;
- positive-definite 2/0/4/38; positive semidefinite 4/2/64/53; energy shell 24/18/1/222;
- on-shell 6/0/0/26; microcanonical 3/0/0/12; conserved energy 6/4/0/96; real-valued 5/0/7/143;
- E_⊥ 0/0/0/17; E_\perp 0/0/0/0; Q′ 0/0/0/41; Q' 5/2/155/199; quadratic invariant 5/0/5/44;
- Liouville 8/8/1/37; maximal entropy 2/6/0/65; maximum entropy 0/0/0/6;
- stationary law 4/2/0/62.

**Group B** (A / B / C / D): gauge 518/575/585/4295; observable 240/349/156/1302; unobservable
6/8/3/44; invariant 168/123/897/4205; redundan 18/28/111/1872; energy 210/252/41/1434;
Hamiltonian 76/72/43/262; shell 53/34/194/1386; regulari 13/16/17/141; "where the inverse exists"
1/0/0/1.

**S3 closure set.** The files at [P] matching the extended regular expression

    SM:? ?(811|29[2-6])\b|SM L(811|29[2-6])|SM §6\.5|real-valued conserved energy|treatment of zero modes

are:
- 6 manuscript `.md` files: papers/SM, Substratum, Structure and Complexity; book FULL and ch10;
- their 5 `.tex` derivatives;
- 1 `.py` file under papers/ (`papers/oi_lattice_code/foundations/coherence_boundary_probes.py`,
  outside scope A, D-8);
- 60 files under `verification/`. Their hit lines that also name energy, zero, shell, null, shift
  or measure were read.

The citation chase from SM:292, 294, 296 and 811 led to SM §4.1, SM:96, Substratum:270–272, GR:699
and GR §2.3. Nothing further was added after one iteration.

## 3. Premise rows (S1, S2)

Verdict codes:
- **E**: entails the target;
- **E|c**: entails it under the named condition c;
- **X**: contradicts it;
- **N**: does not entail it (reason given);
- **I**: irrelevant (reason given).

Columns T1/T2 refer to T1a and T2a; T1b and T2b follow §4.3. Every N is scoped to the searched
scope.

**Main.**
- **Axiom 1, Axiom 2, the Definition, Lemmas 1–3** (Main:36, 44, 46–56).
  - T1/T2: N. They define an observer as a proper subsystem with finitely many distinguishable
    internal states (Main:44) and a product model Γ_V × Γ_H (Main:52). Which functions of state are
    registered is fixed only once a partition is specified.
  - T3: Lemma 3 selects the counting measure; see ledger (iv).
- **Remarks at Main:60–66 and (C1)–(C4) at Main:70–80.** I for T1/T2: they concern finiteness,
  bijectivity and the hidden-sector conditions, not field values.
- **Main §1.4 (Main:84–89).** T1/T2: X|p, where p is a partition whose visible factor carries the
  values of visible sites. The lemma is partition-relative ("each partition 𝒫 determines the
  reduced law"), and it indexes the visible process by visible configurations x_i ∈ Γ_V.
- **The partitions Main specifies.** Main's spatial instantiation supplies p:
  - ledger (viii), site factorization: Main:368, "Write the spatial substratum as
    $S=\prod_{i\in V}S_i$";
  - the visible sector as the sites of a region: Main:298, "the visible sector being the sites of a
    region $R \subseteq \Lambda$", stated there for the q = 2 linear realization;
  - readout regions: Main:376, a "±1-valued function of the state on a readout region".

  For these partitions T1/T2 is X (§4.1). Substratum:249 states the requirement in general: "The
  observational datum must specify the visible/hidden interface, the admissible preparations and
  the readouts."
- **Main:262.** "a symmetry that *does* factorize as $S_V\otimes S_H$ descends to the visible
  symmetry $S_V$ of $\hat{H}_{\text{eff}}$ [...] the visible-internal ones among them — those acting
  entirely within the visible sector and commuting with the trace-out — are precisely the gauge
  symmetries of the emergent description. Gauge degeneracies correspond to physically equivalent
  states". **T1/T2: N.** The reasons:
  - (1) At κ = 2 and b = 0, σ_c is a site-wise product, so it factorizes. But it acts nontrivially
    on hidden sites, so it is not visible-internal.
  - (2) The restriction of σ_c (or τ_c) to the visible sites of a proper region is not a symmetry
    of F [A]. Shifting the visible sites of a proper region R alone does not commute with F, because
    A𝟙_R ≠ 2𝟙_R at the boundary of R. The staggered shift restricted to R fails likewise.
  - (3) Reading the descended S_V as gauge would identify visible configurations that T_ij
    distinguishes. S_V maps T_ij to T_{S_V i, S_V j}, which is a symmetry of the transition data,
    not an identity of records. That conflicts with Main §1.4 at the specified partitions.
  - (4) Main:262 states a criterion for gauge degeneracies of $\hat{H}_{\text{eff}}$ in the
    phase-locking context. It does not state a premise about the substratum field value.
- **Main:244, 260, 274, 346, 666** (phase-locking gauge: energy shift, rephasing, antiunitary
  conjugate). A near miss: gauge of the emergent Hamiltonian, not of the field value.
- **Main §3.3** (Main:364–438). I for T1/T2. Readouts are arbitrary functions on readout regions,
  and nothing restricts them to shift-invariant ones.
- **Main:598.** "The stated substratum dynamics with the observer's read and write access". This
  supports the absolute register at the substratum level, as for SubstratumInterfaceAudit below.
- **Ledger (i)–(iii), (v), (vi), (ix), (x), (xiv).** I for the targets beyond setting the carrier.
  The shifts commute with the point group.
- **Ledger (iv), measure selection** (Main:736; Main:60, "the selection among orbits is fixed by
  maximal entropy compatible with the observer's records").
  - T1/T2: N.
  - T3: E|r, where r names the conserved quantities whose values the records fix. It selects no
    energy by itself (GR:699; §7.1).
- **Ledger (vii), A5** (Main:736; SM:240; Substratum:100). T1/T2: E only for the constraint
  w = 0, together with stationarity (C+1); N for the quotient. T3: it fixes b = 0, the case of
  §7.2.
- **Ledger (viii).** It anchors the absolute register for specified partitions; see above.
- **Ledger (xi), A4** (Substratum:98, "with gauge acting by site-wise bijections of each site's
  (previous, current) pair"). N.
  - Site-wise bijections of the pairs act transitively on configurations, so if A4's gauge meant
    unobservability, every two configurations would be identified [A].
  - The kernel takes the gauge as a parameter `G` (SubstratumInterfaceAudit `A4` [K]).
- **Ledger (xii), A6** (Substratum:102). N: G(n)MG(n+e)^{-1} acts on link data, not by field
  translations.
- **Ledger (xiii).** I beyond the setting: site values lie in an abelian group, so translations
  are defined.

**SM.**
- **SM:96.** "Within one alphabet, the proposed amplitude-scale gauge uses affine relabellings
  $x\mapsto\lambda x+c$ with $\lambda$ a unit. Translations are part of this affine group. [...]
  Independent operational warrant remains open."
  - T1: E|g, where g is the physical gauge status of the translation clause (§4.2).
  - T2: N, because the staggered shift is not a relabelling (§5.2).
- **SM:224–228**, the form lemma. I.
- **SM:230.** "$\alpha=1/d$ is what makes the spectrum gapless, $\omega(0)=0$". T1: N. The text
  treats k = 0 as a mode of the observer-level spectrum.
- **SM:232.** The SM:232 bridge is the operator map φ → L_obs → Δ_g. It states nothing about the
  register (O2).
- **SM:240.** A5.
- **SM:242–258, Theorem 1a and Lemma 1c.** T1/T2: N. The observer projection P is required to be
  equivariant for the spatial group only. T3: N.
- **SM:270, Corollary 1b** ("constant-preserving"). T1: N. T𝟙 = 𝟙 is a normalization of the
  kernel.
- **SM:276–282, Theorem 1.** T1/T2: N. The observer-level field, its k = 0 mode included, is the
  branch's variable.
- **SM:292–296.** T1/T2: N as premises. They state the requirement (C−1), and "unless additional
  constraints are imposed" (SM:292) names constraints, not a quotient. T3: §7.
- **SM:292**, "on a sector where the inverse exists". Class K8, a stipulation for the scalar
  proposal's covariance. N for T1b.
- **SM:585.** I for field shifts: it concerns the common-phase circle of an assumed observer
  action.
- **SM:811**, the gauge map $M = \exp(\tfrac{2\pi i}{q}\mathrm{Lie}[\phi(\mathbf n+\hat e_j)-\phi(\mathbf n)])$
  and "The physical gauge is the alphabet's additive-automorphism group — not arbitrary
  relabellings of $\mathbb{Z}/q\mathbb{Z}$ [...]".
  - T1: this readout is invariant under the constant shift [A]. Partial: one readout.
  - T2: the readout changes by a lattice gradient [A]. In the abelian row SM:811 states that an
    induced gradient connection is pure gauge. The non-abelian case is not settled here [W] (O4).
- **SM:136.** An observer-centred partition breaks translations. Consistent with Main:262. I for
  field shifts.
- **SM:312–344, SM:360–374.** Not read beyond lane 2's inputs (D-1).

**Substratum.**
- **A1–A6** (Substratum:92–102). As the ledger rows above.
- **Substratum:249.** "The observational datum must specify the visible/hidden interface, the
  admissible preparations and the readouts." It bears on O2: the register is part of the datum, not
  a consequence of the dynamics.
- **Theorem 24, families (i)–(iv)** (Substratum:253–262). T1/T2: N. Family (i) relabels hidden
  coordinates "applied identically in every visible fibre", and a field shift moves visible values.
- **Substratum:270**: "**Remark (amplitude-scale gauge).** The proposed fixed-alphabet
  relabellings are affine maps $\phi\mapsto\lambda\phi+c$, with $\lambda$ a unit. [...]"; and
  **Substratum:272**: "*Status (open).*". T1: E|g, as SM:96.
- **Substratum:296 and 395** (level-1 D-gauge, "Energy shifts [...] are also invisible"). A near
  miss: emergent Hamiltonian.

**Other papers.**
- **Introduction:159; GR §6.2; book ch07:173.** Near misses: energy offset.
- **Methodology:435–473.** N: its gauge is 𝒢_sub (Methodology:473).
- **Structure:220, Structure:260.** N: restatements of SM:96 and of the ledger.
- **GR:699.** "The shell is assumed, as in §2.3; it is not a consequence of Lemma 3, which supplies
  determinism, injectivity and the selected measure but no conserved energy." T3 (§7.1).

**Lean [K].**
- **SubstratumInterfaceAudit.** The module docstring describes "an embedded observer with read and
  write access to its visible configurations". This supports X at the substratum level. `A4`
  takes the gauge `G` as a parameter, and `A5` is additivity.
- **PassiveQuotient, ObservabilityQuotient** (`itiSetoid`, `branchDomain_span_eq_itineraryInvariant`,
  `quotient_itinerarySeparating`). The mechanism of §4.3.
- **ShellAssignment** (`shellWeight_invariant`, `joint_stationary`). T3: N; it selects no conserved
  function.
- **HydroSourceAudit** (census note). N for T1: the total sum is treated as a candidate variable.
- **WaveSubstratumUnbounded, SecondOrderCircuit.** I.

**Verification records** (pointers only, §A.46 item 7):
- A5-LINEAR-AFFINE §3.3.1, §3.3.8 item 1 (A5-LINEAR-AFFINE:484), N6, N8′, and Q1 and Q2
  (A5-LINEAR-AFFINE:601, :608);
- A5-Q4-STAGE2D:39–42 (Q2 only) and :307;
- reassess-1049 CHANGES-r3:49;
- W1-1 REPORT r2–r4, REVIEW-W1-1, SC34-cycle-ergodicity README and a1-07-p7 DECISION, which restate
  SM:292.

## 4. T1: the constant static mode

### 4.1 The register (T1a)

**Substratum interface.** For the partitions Main specifies, the visible factor carries the values
of the visible sites:
- site factorization, ledger (viii), Main:368;
- the visible sector as the sites of a region, Main:298;
- readout regions, Main:376.

Main §1.4 indexes the visible process by those configurations (Main:84–89). The kernel observer
reads and writes configurations (SubstratumInterfaceAudit; Main:598). The constant static shift
σ_c(u, v) = (u + c𝟙, v + c𝟙) moves every visible value. So for c ≠ 0, states related by σ_c carry
distinct registered records [A]. **T1a is contradicted at the substratum interface for these
partitions.**

§1.4 alone does not exclude a partition whose visible factor holds only differences, with the
global offset hidden. Main specifies none. The A5 assessment's 𝒜_C is such a reading (§4.2), and it
is not stated as Main's interface.

**Observer of SM §4.1.** The SM:232 bridge, as SM:232 states it, is the operator map
φ → L_obs → Δ_g. It does not carry a register. Substratum:249 makes the register part of the
observational datum. For this observer, then: contradicted, conditional on the register
transferring through the bridge (O2, open); otherwise unsourced within the searched scope.
- The observer projection P is required to be equivariant for the spatial group only (SM:242–258).
- The observer-level field, with its k = 0 mode, is the branch's variable (SM:230; Theorem 1).
- No premise within the searched scope fixes the register as shift-invariant.

**Governance.** #1049 comment 6624263637 (author amaybaum, created 2026-11-04T06:28:45Z) records
the owner's decisions:
- overall: "Retain linearity as a posit. Do not assume all observers are shift-invariant.";
- Q1: "Preserve Main's currently specified absolute interface as the formal baseline. The
  shift-invariant interface is a legitimate conditional alternative, not yet a derived description
  of all OI observers.";
- Q2: "Treat amplitude shifts as mathematical relabellings unless their physical gauge status is
  justified."

On `main`, Q1 and Q2 are quoted at A5-LINEAR-AFFINE:601 and :608, and Q2 at A5-Q4-STAGE2D:39–42.
The overall sentence is not on `main`. These records are governance. No verdict here rests on
them.

### 4.2 Conditional sources (partial)

1. **The shift-invariant interface 𝒜_C** (A5-LINEAR-AFFINE §3.3.1, a research record). Its
   diagonal readouts are functions of (x_V(t−1) mod a constant, x_V(t) mod a constant), with
   independent constants on the two slices. It is therefore invariant under the whole uniform
   sector, s and w alike. It is not a stated interface of the manuscripts.
2. **A physical amplitude-scale gauge** (SM:96; Substratum:270–272). The alphabet translation
   x ↦ x + c acts on every value at every time, so on phase space it is σ_c. At κ = 2 and b = 0,
   σ_c commutes with F ([A]: A(c𝟙) = 2c𝟙; lane 2 Proposition 5; A5-LINEAR-AFFINE N8′). A passive
   relabelling that preserves φ, declared physically void, would then identify x and σ_c x [W].
   - The principle is "proposed", and its warrant is open (SM:96; Substratum:272).
   - SM:811 names it the "additive-automorphism" group, which excludes translations (O1).

Single invariant readouts, partial only:
- the SM §6.5 link-difference map [A];
- E, which is σ_c-invariant at α = 1/d since (2 − A)𝟙 = 0 [A], and every E-shell with it;
- the uniform counting measure on (ℤ/q)^{2N} at κ ≡ 2 [A].

### 4.3 T1a and T1b

The kernel's passive quotient identifies two states exactly when their visible itineraries agree
(PassiveQuotient `itiSetoid`; ObservabilityQuotient [K], for the carrier class stated there).
Hence [W, for transfer to the real lift]:
- T1b implies T1a for any register that factors through the quotient.
- T1a implies T1b for the itinerary register, provided the shift normalizes F. Normalization makes
  invariance of the readout at one time give invariance of the whole itinerary. σ_c commutes with
  F at κ = 2 for any b; τ_c anticommutes in the sense of §5.2.

So T1b coincides with T1a for such observers and carries §4.1–§4.2.

### 4.4 Verdict

- **T1a:**
  - at the substratum interface, contradicted for the partitions Main specifies;
  - for the SM §4.1 observer, contradicted conditional on the transfer (O2, open), otherwise
    unsourced within the searched scope;
  - partially sourced, conditional on 𝒜_C or on a physical amplitude-scale gauge, both open.
- **T1b:** unsourced within the searched scope, with the same conditional sources.

**Named gap.** One of the following:
- an established derivation that the SM §4.1 observer registers only shift-invariant functions;
- a justified physical gauge status for the translation clause.

## 5. T2: the staggered static mode, and lane 2's Proposition 5

### 5.1 The register

The staggered static shift τ_c adds c·v⊗e, with v = (s, −s), s_n = (−1)^{abs(n)} and L even. It
moves visible values, so §4.1 applies unchanged. **T2a is contradicted at the substratum interface
for the partitions Main specifies.** For the SM §4.1 observer it is contradicted conditional on the
transfer (O2), and otherwise unsourced within the searched scope.

### 5.2 No conditional source

At α = 1/d, A s = −2s, so F(s, −s) = (−s, A(−s) − s) = (−s, 2s − s) = −v. Hence

    τ_c⁻¹ ∘ F ∘ τ_c (x) = F x + cFv − cv = F x − 2cv.   [A]

So τ_c is not a symmetry of F. The conjugate map has first output component v_x − 2cs, so it is
not even of second-order form, and A5 excludes it.

τ_c is also outside each alternative for T1:
- it depends on site and time, so it is not an alphabet relabelling;
- 𝒜_C is built from uniform constants;
- A5-LINEAR-AFFINE N6 records that "site-dependent translations are gauge, which the corpus does
  not state".

E is τ_c-invariant, because the null vectors of a semidefinite form lie in its radical [A]. That is
one readout only.

**Verdict.** T2a takes the two-level form of §5.1. T2a and T2b are unsourced within the searched
scope, even conditionally.

### 5.3 (F-slice) An alternative to the H-ZM quotient

The inputs are those of lane 2's Proposition 4: b = 0, on T at α = 1/d, and an F-stationary law
with finite second moments.

- **(a)** The law is supported on L_0 ⊕ V_rest. [A]
  - On the uniform block, w ↦ w and s ↦ s − 2w, which forces w = 0.
  - On the staggered block, with p = h_u + h_v and r = h_u − h_v: p ↦ −p and r ↦ 2p − r, so F²
    gives r ↦ r − 4p, which forces p = 0.
- **(b)** On L_0 ⊕ V_rest, F acts as +1 on the constant static labels c ∈ R^6, as −1 on the
  staggered labels a ∈ R^6, and as F on V_rest. So c and the pair {a, −a} are invariant. [A]
- **(c)** Disintegrating the law over (c, {a, −a}) gives conditionals on the two slices
  x*(±) + V_rest, with x*(±) = c(1, 1) ± a(1, −1). These conditionals are F-invariant for almost
  every label, and F swaps the two slices. [W; standard disintegration over an invariant
  measurable map on a standard Borel space]
- **(d)** In deviation coordinates y = x − x*(t), with x*(t) = c(1, 1) + (−1)^t a(1, −1), y lies in
  V_rest and y(t+1) = F y(t). E is positive definite on V_rest at α = 1/d, because
  abs(αΣ cos k_j) = 1 only at k = 0 and k = (π, …, π). So lane 2's Theorem 1 gives the unique tamed
  commuting J on every label sector. [A, conditional on lane 2 Theorem 1, a model-written record]

**Consequence, conditioned.** An alternative to the H-ZM quotient exists that yields a unique J on
every label sector. The null sector is kept as conserved classical labels, consistent with Main's
specified partitions, and no unobservability is assumed. The construction is a family of label
sectors with centring, which differs from Proposition 5's single reduced phase space. Whether it
serves Proposition 5's consumers (Theorem 5's Σ, H-PF) is open (O3). So is whether lane 2's
"requires the named hypothesis H-ZM" can be weakened.

**Pressure test:**
- stationarity with finite second moments is needed;
- the centre has period at most two (lane 2 §2.6, time-dependent on the staggered labels);
- uncentred moments carry (c, a) (lane 2 §4.1 and its Proposition 11);
- nothing is shown for carrier Z;
- nothing is shown about H-PF;
- step (c) is [W].

## 6. T1Z and T2Z (secondary)

Within the searched scope, no stated premise fixes the topology on Z: neither K nor H_E (lane 2's
H-top). Lane 2's Proposition 6(c) holds for d = 1, 2 only, and it is a model-written record (C−2).
**Unsourced within the searched scope.**

## 7. T3: the SM:811 energy

### 7.1 What the text defines and requires (T3a, T3b)

- **Linear lift.** SM:296 defines the conserved E(u, v) = u·u + v·v − u·Av. SM:294 calls it the
  "total energy". SM:292 evaluates it on the real lift: "positive definite for $|\alpha|<1/d$,
  positive semidefinite at $\alpha=1/d$, with constant and, for even $L$, staggered null modes".
- **Affine lift.** Not treated: the selected model is linear (SM:240).
- **Requirements.** SM:292: "a specified real positive-definite quadratic shell; it requires an
  energy, a limiting regime and treatment of zero modes", and "noncompact shells unless additional
  constraints are imposed". SM:811: "a real-valued conserved energy", a candidate on the open
  stationary-law hypothesis.
- **Status.** GR:699: the shell is assumed and is not a consequence of Lemma 3. Main ledger (iv)
  selects the maximal-entropy invariant measure "compatible with the observer's records" (Main:60,
  Main:736).

### 7.2 Proposition U1 [A]

On T at α = 1/d, for any b, no conserved function on the full phase space has compact sublevel
sets. In particular, no conserved positive-definite quadratic form exists.

*Proof.*
- On the uniform components, w ↦ w − b and s ↦ s − 2w + b.
- For b ≠ 0, every orbit is unbounded in w.
- For b = 0, every orbit with w ≠ 0 is unbounded in s.
- A conserved function with compact sublevel sets would bound every orbit.
- For quadratic forms: on the uniform block, (F − I)² = 0 with F ≠ I. With L even, on the
  staggered block, (F + I)² = 0 with F ≠ −I. An invariant positive-definite form would make F
  diagonalizable, which it is not. ∎

U1 extends SM:292's statement about E's shells to every conserved function with compact sublevel
sets.

At b = 0 the invariant constraint slices of §5.3 exist, and on them E restricted to V_rest is
positive definite [A]. SM states that constraints are needed and does not specify them.

**Linear verdict (PLAN §5, "defined").** Defined (E). The T3b positive-definiteness requirement
fails on the full space (U1). It holds only on invariant constraint slices, which the text requires
and does not specify.

The selecting condition is named: which conserved labels the observer's records fix (Main ledger
(iv)). At the specified partitions the static labels are registered and conserved, so fixing them
agrees with the records [W]. No premise within the searched scope states the selection.

### 7.3 Propositions U2 and U3 (affine, at resonance, b ≠ 0) [A]

- **U2.** No orbit is bounded (U1). So no conserved function meets the requirement on the full
  space, and no invariant constraint confined to the uniform sector exists. This confirms lane 1
  §2.4.
- **U3.** E = E_⊥ + E_0, with E_0 = N w², and S_u + S_v = N s. Hence

      Q′ = E_⊥ + (N w² − bN s) = E_⊥ + Q′_0,

  with Q′_0 a function of (w, s) alone. Every candidate is E_⊥ plus a function of the uniform
  variables.
  - Any reading whose shell keeps the uniform sector fails the requirement (U2). That includes E_⊥
    on the full space.
  - Removing the uniform sector, both s and w, reduces every candidate to E_⊥. Projection onto C^⊥
    commutes with F_b.
  - That removal is stronger than H-ZM. It is supplied only by an interface like 𝒜_C (§4.2), and
    within the searched scope by no stated premise. At the specified partitions it is contradicted
    for visible sites.

**Affine verdict (PLAN §5, "unspecified").** The text does not treat this case, and no conserved
function meets the requirement on the full space. The residual choice is a treatment of the uniform
sector. No stated premise within the searched scope selects one.

### 7.4 (F-stag) E_⊥ at even L [A]

For L even, Σ_n s_n = 0, so v⊗e lies in C^⊥ and E_⊥(v⊗e) = E(v⊗e) = 0. Since F v = −v, every E_⊥
shell contains the line x + t·v⊗e.
- Lane 1 REPORT-r2 line 116 ("Each of them confines E_⊥") is correct.
- Line 297 ("E_⊥ (the energy of the non-uniform modes) is conserved for affine rules, and with it
  the shell confines the non-uniform modes again") holds for odd L, or with the staggered labels
  fixed.

### 7.5 Consequences for #1049 D5

Lane 1's class-(c) placement of D5 does not depend on reading the energy as Q′. At resonance,
every reading that keeps the uniform sector fails SM:292's requirement when b ≠ 0, while at b = 0
the invariant slice cures it (U1–U3). The dependence on b is the availability of an invariant
uniform-sector constraint, which is lane 1's own criterion.

The alternative-energy branch (a) needs the uniform sector removed from the description. No stated
premise within the searched scope supplies that removal, and at the specified partitions it is
contradicted for visible sites. At even L the branch also needs a treatment of the staggered labels
(F-stag). D5's placement therefore rests on the stated reading, and the E_⊥ branch on an unstated
interface choice together with a staggered-label treatment.

## 8. Controls

Every control is green. The writer extracted each quote at [P], and the review of r1 re-extracted
them.

| Control | Outcome |
| --- | --- |
| C+1 | A5 found (Main:736 (vii); SM:240; Substratum:100). b = 0, w conserved, and with stationarity w = 0 [A]. Classified as supplying the constraint, not the quotient. **Green.** |
| C+2 | SM:296's E and SM:292's definiteness found. Classified as the energy SM:292 names. **Green.** |
| C+3 | The sweep returned SM:292 ("zero mode") and SM:811 ("real-valued", "conserved energy"). **Green.** |
| C−1 | SM:292's requirement rejected as a source. **Green.** |
| C−2 | Lane 2 Proposition 6(c) rejected for T and for d = 3. **Green.** |
| C−3 | Commutation of σ_c with F rejected as a source on its own. Main:262's symmetry-to-gauge statement judged N (§3). **Green.** |
| C−4 | Writer extraction at [P], re-extracted by the review of r1, with positions corrected as in finding 12. **Green.** |
| C−5 | Q_B and P_C not accepted. **Green.** |

## 9. Passes and stopping rule

- **Pass 1** (S4, papers): no NEW.
- **Pass 2** (ledger, Substratum): ELABORATING.
- **Pass 3** (D-2 records): §4.1 and §5.2 applied to H-ZM, ELABORATING.
- **Pass 4** (Lean): §4.3, ELABORATING.
- **Pass 5** (T3 algebra): U1 modestly NEW; U2 CONFIRMING; U3 and F-stag NEW.
- **Pass 6** (lane 2 Proposition 5): F-slice, NEW, conditioned.
- **Pass 7** (GR, book mirrors): no NEW.
- **Pass 8** (Group B: unobservable, redundan): no NEW.
- **Pass 9** (r2: Main §1.2–§1.3 and §3.3 in full, the §3.1/§3.2/§3.4 screen, Main:262, W-1): no
  NEW.

**Stopping rule (c) applies.** Stages S1–S6 are incomplete (D-1 to D-8). The partial state is
returned, and every verdict is scoped to the part swept.

## 10. Productivity verdict (PLAN §7)

**Gem.**
- **Criterion 1.** U1, U3 and F-stag give T3 a verdict strictly stronger than lane 1's ("the energy
  reading is not stated"). They add an exact selecting condition, and U1 extends SM:292 to every
  conserved function with compact sublevel sets. T1 and T2 reach a two-level contradiction branch
  and, for T1, a conditional source with an exact gap. These rest on facts already on `main`
  (ELABORATING).
- **Criterion 2.** For #1049, D5's placement rests on the stated reading, and the E_⊥ branch on an
  unstated interface and staggered-label choice. For #1217, F-slice exposes that excluding the null
  sector was equated with a quotient. An alternative exists, and its service to Proposition 5's
  consumers is open (O3).

**Classification:**
- NEW: U3, F-stag, F-slice (conditioned);
- modestly NEW: U1;
- ELABORATING: §4.1, §4.3, §5.2;
- CONFIRMING: U2;
- POSITIVE: C+1.

## 11. Open nodes

- **O1.** The amplitude-scale gauge: the physical status of its translation clause, and the
  variance between SM:96 (affine, translations included) and SM:811 ("additive-automorphism", which
  strictly excludes translations).
  - The variance is immaterial for SM:811's map. The map uses link differences, which translations
    leave unchanged, and its argument against nonlinear relabellings applies equally to affine
    maps.
  - It is a manuscript-consistency defect, outside this unit's authority.
  - Proposed accountable Issue: #1049, where the owner's decision Q2 on this gauge is recorded,
    unless the owner names another (§A.47 item 4).
- **O2.** Whether the register of the SM §4.1 observer is fixed by Main's specified partitions
  through the SM:232 bridge. Open, with the bridge. Substratum:249 places the register in the
  observational datum.
- **O3.** F-slice: whether label-sector J with centring serves Theorem 5's Σ and H-PF (unit A,
  lane 2). It is also conditional on lane 2 Theorem 1.
- **O4.** The non-abelian case of the staggered change in the SM §6.5 map.
- **O5.** The unswept remainders D-1 to D-8.
- **O6.** Carrier Z (H-top).

## 12. References not on `main` (§A.42 item 8)

- **#1049 comment 6624263637.** Governance. Q1 and Q2 are quoted on `main` at
  A5-LINEAR-AFFINE:601 and :608, and Q2 at A5-Q4-STAGE2D:39–42. The overall sentence is not on
  `main`. No scientific claim rests on the comment.
- **#1169 comments 7189139613 and 7189143747:** provenance and authorization.
- **PR #1594 review comment (2026-11-26T10:56:45Z):** review provenance.
- **Commits `d4f97b53` (PLAN) and `266fbc60` (r1):** on the unit branch. They land with this
  record.
- **Lane 2 Theorem 1:** on `main`, used as a premise of F-slice (d) and carried as a condition.
- Every other reference is on `main` at [P].
