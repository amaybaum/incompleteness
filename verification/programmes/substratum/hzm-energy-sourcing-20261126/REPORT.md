# HZM-ENERGY-SOURCING, unit C (lane 3): do existing premises supply H-ZM and the SM:811 energy? Report

**WIP / UNVERIFIED. Model-written research record, paper-only, pending independent review.
Nothing here is adopted, proposed for the manuscripts or authorized beyond the unit scope. No
premise is adopted, weakened or changed, and no energy is chosen. Evidence layers:**
- source reading at [P], reproducible by the commands of §2;
- mathematical derivation on paper, labelled per step:
  - [A] exact hand algebra here, unreviewed;
  - [W] reasoning here, unreviewed;
  - [P] text quoted at [P];
  - [K] a kernel-checked Lean statement on `main`, cited by module and identifier and not
    rebuilt here.

**No computation was run and no Lean was built.**

- **Plan:** `PLAN.md` in this directory, commit `d4f97b5387fe448baeebe3ebd2caae41da89f259`.
  Targets, decision rule, controls, productivity test and stopping rule are as frozen there.
  Deviations are listed in §1.
- **Pinned main commit [P]:** `353a066f18766837fed8c7f58507e09ff549b1a4`. Every file:line is at
  [P].
- **Accountable Issues:** #1217, #1049; programme #1169.
- **Authorization and Goal link:** as in PLAN.md (#1169 comment 7189139613, author amaybaum,
  created 2026-11-26T10:16:17Z).
- **Coordinator answers to the plan's open points:** the coordinator's message confirmed
  (1) reading at the pin through git objects, (2) `git grep` at the pin as source reading,
  (3) a named unswept remainder of Group B, (4) the T1a/T1b split, (5) T1Z/T2Z as secondary,
  (6) reviewer designation by the coordinator, and (7) unit A's record read only as pointers once
  it is on `main`.
- **Unit A:** not read. Its record is not on `main` at [P].

## 0. Summary

Every verdict is scoped to what §2 records as swept. A target found unsourced means unsourced
within that scope, never impossible, and never evidence that no premise could supply it.

| Target | Verdict (PLAN §5 branch) | Decisive sources |
| --- | --- | --- |
| T1a, invariance under the constant static shift | **Contradicted** at Main's stated interface, which registers absolute visible configurations. **Partially sourced, conditional on an open alternative:** the shift-invariant interface 𝒜_C, or a physical amplitude-scale gauge. The owner classifies both as conditional or unjustified. Individual readouts are invariant: the SM §6.5 link-difference map, E and its shells at α = 1/d, and the uniform counting measure. | Main:84–89; SM:96; Substratum:270; SM:811; A5-LINEAR-AFFINE §3.3.1; owner decisions Q1 and Q2 (#1049 comment 6624263637) |
| T1b, quotient by the constant static mode | **Unsourced** within the searched scope. T1b and T1a coincide for an observer whose register is its visible itineraries (§4.3), so T1b carries T1a's contradiction and its conditional sources. | PassiveQuotient, ObservabilityQuotient [K] |
| T2a, invariance under the staggered static shift | **Contradicted** at Main's stated interface. **Unsourced, even conditionally:** the shift is not an alphabet relabelling, not in 𝒜_C, and not a symmetry of F. | Main:84–89; §5.2 [A]; A5-LINEAR-AFFINE N6 |
| T2b, quotient by the staggered static mode | **Unsourced** within the searched scope. | as T2a |
| T1Z, T2Z (secondary) | **Unsourced** within the searched scope: no stated premise fixes the topology on Z. | §6 |
| T3, the SM:811 energy | **Linear lift: defined but underdetermined.** The text names E, the "total energy" (SM:292–296), but at α = 1/d no conserved function with compact sublevel sets exists on the full phase space of T (Proposition U1 [A]). SM:292's shell exists only on invariant constraint slices, which the text requires and does not specify. **Affine lift at resonance (b ≠ 0): unspecified.** The text does not treat it, and no conserved function meets the requirement (Proposition U2 [A]). The choice among Q′, E_⊥ and E_⊥ + f(Q′_0) is equivalent to a choice of treatment for the uniform sector, not an independent choice of energy (Proposition U3 [A]). No stated premise selects one. | SM:292, SM:294, SM:296, SM:811; GR:699; Main:736 (iv); §7 |

Two further findings fall outside the strict targets but bear on the Goal link:

- **(F-slice)** On T at α = 1/d with b = 0, lane 2's exclusion of the null sector (its
  Proposition 5) can be obtained without H-ZM. Stationary laws disintegrate over the conserved
  static labels, and on each label sector the dynamics is F restricted to V_rest, with its unique
  J (§5.3, [A]/[W], favorable to the framework, flagged for independent re-derivation). The labels
  stay conserved classical data, which agrees with Main's absolute interface.
- **(F-stag)** At α = 1/d with L even, the staggered null direction lies in the non-uniform sector.
  So E_⊥ is only semidefinite and its shells do not confine that direction (§7.4, [A]). Lane 1
  REPORT-r2 line 297 ("with it the shell confines the non-uniform modes again") holds for odd L, or
  with the staggered labels fixed.

Productivity verdict (§10): **gem**. NEW: §4.1, §7.2–7.4 and §5.3. POSITIVE: control C+1
confirms lane 2's constraint half.

## 1. Execution against the plan, and deviations

The plan says the search may be widened but never narrowed. The execution falls short of the plan
in the places below. Each is named, and every verdict is scoped to what was executed.

- **D-1 (S1, reading in full).** These were read in full:
  - Main §1.4 (Main:82–91) and the §4.5 posit ledger (Main:726–738), each item;
  - Substratum §3.1 structural assumptions (Substratum:90–106) and §4 (Substratum:247–300);
  - SM:42–57, SM:88–96, SM:220–283, SM:292–298, SM:585 and SM:799–811.

  Main §1.2–§1.3 and §3.3–§3.4 were read through the passages that S4 hits and the citations led
  to (Main:36, 44, 60, 70, 78, 260, 368, 420–424, 455, 736, 770), not in full. SM:312–344 and
  SM:360–374 (the Theorem 5 setting, unit A's domain) were read only through lane 2's inputs.
  Structure, GR, Introduction and Methodology were read through their S4 hits and the passages
  those hits cite (GR:20, 58, 60, 86, 88, 294, 603, 699, 715, 833; Introduction:159;
  Methodology:435–473; Structure:68, 154, 214, 220), not in full.
- **D-2 (S4, Group N in scope D).**
  - Every hit line in scope (D) was read for these 25 terms: zero mode, zero-mode, null mode, null
    direction, null sector, constant mode, uniform mode, uniform sector, uniform shift, constant
    shift, static shift, shift symmetry, field translation, staggered mode, alternating mode,
    period two, period-two, Dirichlet, energy seminorm, modulo constants, link difference,
    difference observable, noncompact shell, E_⊥ and energy norm. That is 133 lines outside the
    lane 1 and lane 2 directories.
  - The other Group N terms in (D) were read only within the S3 closure set and the S6 records:
    null space, shift invariance, global shift, Goldstone, pi mode, π-mode, \pi, (-1)^{, (−1)^,
    k = 0, k=0, zero momentum, seminorm, quotient, up to a constant, up to gauge, first
    difference, relational observable, positive definite, positive-definite, positive
    semidefinite, energy shell, on-shell, microcanonical, conserved energy, real-valued, E_\perp,
    Q′, Q', quadratic invariant, Liouville, maximal entropy, maximum entropy and stationary law.
    Their remaining hits in (D) are the **unswept Group N remainder**.
- **D-3 (S4, \pi and quotient in scopes A and B).** These were screened as match-centred snippets.
  A hit was escalated to full context when its snippet named a mode, a staggered structure, a
  Brillouin-zone corner or a zone. That is snippet-level reading, not line-level.
- **D-4 (S4, Group B in scope A).** Every hit of unobservable, redundan and "where the inverse
  exists" was read in (A) and in the book chapters. Hits of gauge, observable, invariant, energy,
  Hamiltonian, shell and regulari in (A) and (B) were read only where S1–S3 led. Their other hits
  are the **unswept Group B remainder in (A) and (B)**, alongside the remainder in (D) that the
  plan already provided for.
- **D-5 (S5, Lean).** All 252 modules were listed. These were read at docstring and statement
  level: SubstratumInterfaceAudit, WaveSubstratumUnbounded, ShellAssignment, PassiveQuotient,
  ObservabilityQuotient and SecondOrderCircuit (the modules whose names or docstrings concern
  shifts, translations, energy, the wave rule or observer readout), plus every census-note hit of
  the narrow terms. The high-volume Lean hits (quotient 292, Q' 155, positive semidefinite 64,
  k = 0 62) were read at module level only.
- **D-6 (S6).** These were read in full: lane 2 PLAN.md and REPORT-r2.md; lane 1 REPORT-r2.md
  §2.3–§3 and §8; and the A5-LINEAR-AFFINE passages its hits and §3.3.1 cite. A5-Q4-STAGE2D,
  q3-a6-offsets ASSESSMENT and reassess-1049 were read at their hit lines. POSIT-MIN, Q3, Q4 and
  BRIDGE-UNIT1 were not read.

## 2. Sweep log (S4)

All counts are at [P]. Each count is the number of matching lines, case-insensitive, fixed-string,
binary files excluded. They come from this command, run per term from the repository root:

    P=353a066f18766837fed8c7f58507e09ff549b1a4
    A: git grep -c -i -I -F -e "$t" $P -- 'papers/*.md'
    B: git grep -c -i -I -F -e "$t" $P -- 'book/*.md'
    C: git grep -c -i -I -F -e "$t" $P -- 'verification/lean/*.lean' 'verification/lean-mathlib/*.lean' 'verification/lean-manuscript-census.json'
    D: git grep -c -i -I -F -e "$t" $P -- 'verification/*' ':(exclude)verification/lean/*' ':(exclude)verification/lean-mathlib/*' ':(exclude)verification/lean-manuscript-census.json'

Each scope's per-file counts are summed. The pathspec `*` matches across directories, so 'papers/*.md'
includes the subdirectory READMEs.

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

**S3 closure set.** Files at [P] matching
`SM:? ?(811|29[2-6])\b|SM L(811|29[2-6])|SM §6\.5|real-valued conserved energy|treatment of zero modes`:
- 6 manuscript files (papers/SM, Substratum, Structure, Complexity; book FULL and ch10);
- 61 verification files. Their hit lines that also name energy, zero, shell, null, shift or
  measure were read.

The citation chase from SM:292, 294, 296 and 811 led to SM §4.1 (SM:220–283), SM:96, Substratum:270,
GR:699 and GR §2.3. Nothing further was added after one iteration.

## 3. Premise rows (S1, S2)

Verdict codes:
- **E**: entails the target;
- **E|c**: entails it under the named condition c;
- **X**: contradicts it;
- **N**: does not entail it (reason given);
- **I**: irrelevant (reason given).

Columns T1/T2/T3 refer to T1a, T2a and T3. T1b and T2b follow §4.3.

**Main.**
- **Axiom 1 and the Definition** (Main:36, Main:44), "registers changes", V ⊊ S. T1/T2: N, since
  they leave open which functions of state are registered; S2 continues at Main §1.4. T3: I, since
  no energy is involved.
- **Axiom 2** (Main:36), recurrence. I for all three: it concerns the temporal domain, not the
  field value.
- **Main §1.4 (Main:84–89)**, [P]:
  "$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu_H(h\mid x_i)$$".
  T1/T2: **X** at the substratum level. The visible process is indexed by absolute visible
  configurations x_i, so two states that differ by a nonzero shift of the visible values are
  distinct registered records. T3: I.
- **Ledger (i), Axiom 2.** I.
- **Ledger (ii), total finiteness.** I for T1/T2. T3: N; it bears on finiteness of shells, not on
  which energy.
- **Ledger (iii), injectivity and bijectivity.** I.
- **Ledger (iv), measure selection** (Main:736; Main:60, [P]: "the selection among orbits is fixed
  by maximal entropy compatible with the observer's records"). T1/T2: N; it selects a measure,
  not a register. T3: E|r, where r names the conserved quantities whose values the records fix. It
  passes the selection on to the records, and selects no energy by itself. GR:699 states this
  explicitly (§7.1).
- **Ledger (v), mixing hypothesis.** I.
- **Ledger (vi), isotropy.** I; the shifts commute with the point group.
- **Ledger (vii), A5** (Main:736; SM:240; Substratum:100). T1/T2: E only for the constraint w = 0,
  together with stationarity (C+1), and N for the quotient. T3: it fixes b = 0, the case of §7.2.
- **Ledger (viii) site factorization, (ix) A3, (x) nearest-neighbour range.** I for the targets
  beyond setting the carrier.
- **Ledger (xi), A4** (Main:736; Substratum:98, [P]: "with gauge acting by site-wise bijections of
  each site's (previous, current) pair"). T1/T2: N. Site-wise bijections of the pairs act
  transitively on configurations, so if A4's gauge meant unobservability every two configurations
  would be identified [A]. A4's gauge is therefore a relabelling of the representation, used to
  state translation commutation. The kernel takes it as a parameter `G` (SubstratumInterfaceAudit,
  `A4` [K]). T3: I.
- **Ledger (xii), A6** (Substratum:102). N: internal-index transformations act on the link data by
  G(n)MG(n+e)^{-1}, not by field translations.
- **Ledger (xiii), the second-order form.** I beyond the setting: site values lie in an abelian
  group, so translations are defined.
- **Ledger (xiv), measurement independence.** I.

**SM.**
- **SM:96**, [P]: "Within one alphabet, the proposed amplitude-scale gauge uses affine relabellings
  $x\mapsto\lambda x+c$ with $\lambda$ a unit. Translations are part of this affine group. [...]
  Independent operational warrant remains open." T1: E|g, where g is the physical gauge status of
  the translation clause (§4.2). T2: N, since the staggered shift is not a relabelling (§5.2).
  T3: I.
- **SM:224–228**, the form lemma. I: it fixes the rule's form.
- **SM:230** (the coefficient's reading): "$\alpha=1/d$ is what makes the spectrum gapless,
  $\omega(0)=0$". T1: N, and it treats k = 0 as a mode of the observer-level spectrum. T3: I.
- **SM:232.** A setting input (SM:232 bridge).
- **SM:250–258, Theorem 1a and Lemma 1c** (linear observer projection P equivariant for spatial
  symmetries; invariant-measure options). T1/T2: N. Equivariance is required for the spatial group
  only. No premise requires P to commute with field translations, still less to be invariant under
  them. T3: N; the measure options do not fix an energy.
- **SM:270, Corollary 1b** ("constant-preserving" observer Markov part). T1: N. Preserving
  constants is a normalization of the kernel (T𝟙 = 𝟙). It makes the constant a stationary mode of
  the observer dynamics, not an unregistered one.
- **SM:276–282, Theorem 1** (the observer-level field φ). T1/T2: N. The field, its k = 0 mode
  included, is the variable of the observer-level branch.
- **SM:292–296.** T1/T2: N for invariance as a premise. They state the requirement (C−1). They also
  state that "the null directions ... have noncompact shells unless additional constraints are
  imposed" (SM:292), which names constraints, not a quotient. T3: these define and require the
  energy (§7).
- **SM:292**, "a covariance proportional to $\Box_{\mathrm{lat}}^{-1}$ on a sector where the
  inverse exists". Class K8, a stipulation: it restricts the scalar proposal's covariance to the
  complement of ker □ without deriving the restriction. It is recorded as stated, not derived. N
  for T1b as a premise.
- **SM:585.** The amplitude-scale principle "supplies at most the common-phase circle for the
  assumed observer action". I for field shifts.
- **SM:811.** The gauge map is $M = \exp(\tfrac{2\pi i}{q}\mathrm{Lie}[\phi(\mathbf n+\hat e_j)-\phi(\mathbf n)])$,
  together with "The physical gauge is the alphabet's additive-automorphism group — not arbitrary
  relabellings of $\mathbb{Z}/q\mathbb{Z}$ [...]". T1: this readout is invariant under the constant
  shift [A], which is partial: one readout (lane 1 D4). T2: this readout changes under the
  staggered shift by a lattice gradient [A]. In the abelian row SM:811 states that an induced
  gradient connection is pure gauge with constant determinant, so the change is gauge-equivalent
  there. The non-abelian case is not settled here [W]. T3: the measure clause is §7.
  - Also recorded (§4.2): the additive automorphisms of ℤ/q are the maps x ↦ λx with λ a unit, so
    "additive-automorphism group" at SM:811 excludes the translations that SM:96 includes in the
    same principle. This is a cross-passage variance in what the principle contains.

**Substratum.**
- **A1–A6** (Substratum:92–102). As for the ledger rows above.
- **Theorem 24, families (i)–(iv)** (Substratum:253–262). T1/T2: N.
  - Family (i) relabels hidden coordinates "applied identically in every visible fibre". A field
    shift that moves visible values is not in (i).
  - Families (ii)–(iv) concern the alphabet, decoupled factors and graphs.
- **Substratum:270**, [P]: "**Remark (amplitude-scale gauge).** The proposed fixed-alphabet
  relabellings are affine maps $\phi\mapsto\lambda\phi+c$, with $\lambda$ a unit. [...]" and
  "*Status (open).*". T1: E|g, as SM:96.
- **The gauge hierarchy, level 1** ("Energy shifts and the antiunitary reflection are also
  invisible"). A near miss: this is a shift of the emergent Hamiltonian, not of the substratum
  field value. Rejected under §3 of the plan (wrong object).

**Other papers.**
- **Introduction:159, GR §6.2** ("A constant shift of quantum energy changes no visible
  probability"). A near miss for the same reason (energy offset, not field shift). The book mirror
  ch07:173 is likewise.
- **Main:260**, diagonal-gauge null directions. A near miss: a phase gauge of the reconstructed
  Hamiltonian.
- **Methodology:435–473**, "physics modulo gauge". N: the gauge it names is 𝒢_sub (Methodology:473),
  which contains no visible field shift.
- **Structure:220.** It restates SM:96's status. N.
- **GR:699**, [P]: "The shell is assumed, as in §2.3; it is not a consequence of Lemma 3, which
  supplies determinism, injectivity and the selected measure but no conserved energy." T3: a stated
  negative about the source (§7.1).

**Lean [K].**
- **SubstratumInterfaceAudit** (module docstring: "an embedded observer with read and write access
  to its visible configurations"; `obsTheory`). T1/T2: X-supporting, since the kernel observer
  reads absolute configurations. `A4` takes the gauge `G` as a parameter, and `A5` is additivity.
- **PassiveQuotient, ObservabilityQuotient** (`itiSetoid`, `branchDomain_span_eq_itineraryInvariant`,
  `quotient_itinerarySeparating`). These are the mechanism of §4.3. They identify states exactly
  when their visible itineraries agree. They supply neither T1 nor T2 without an invariant `vis`.
- **ShellAssignment** (`shellWeight_invariant`, `joint_stationary`). Uniform counting on any
  invariant shell is stationary. T3: N; it does not select the conserved function.
- **HydroSourceAudit**, through the census note on totalSum and the zero-mode second difference.
  Kernel facts about the dynamics of the uniform sector over ℤ/q. N for T1: the round treats the
  total sum as a candidate variable, not as unregistered.
- **WaveSubstratumUnbounded, SecondOrderCircuit.** I: translation commutation of the rule and
  circuit structure.

**Verification records** (pointers only; §A.46 item 7). These were used as finding aids, and every
scientific step that a verdict uses is re-checked on the manuscript or kernel text above:
- A5-LINEAR-AFFINE §3.3.1 and Q1 (the readout classes 𝒜_C, 𝒜_W and 𝒜_abs; "Main §1.4 indexes T_ij by
  absolute visible configurations"; "𝒜_C is a *reading* of Substratum:270 [...] not a stated
  interface"), N6 ("site-dependent translations are gauge, which the corpus does not state") and
  N8′ (shift as a dynamical symmetry iff κ ≡ 2);
- A5-Q4-STAGE2D:39 and :307;
- reassess-1049 CHANGES-r3:49;
- W1-1 REPORT r2–r4, REVIEW-W1-1, SC34-cycle-ergodicity README, a1-07-p7 DECISION (restatements of
  SM:292's semidefiniteness and null modes).

## 4. T1: the constant static mode

### 4.1 The register at Main's stated interface (T1a)

Main §1.4 indexes the visible process by absolute visible configurations (Main:88). The kernel
observer of SubstratumInterfaceAudit reads and writes configurations. The constant static shift
σ_c(u, v) = (u + c𝟙, v + c𝟙) moves every visible value whenever the visible sector is nonempty. So
for c ≠ 0, two states related by σ_c carry distinct registered records [A]. **T1a is contradicted
at Main's stated interface** (substratum level).

The owner adopted that interface as the baseline. #1049 comment 6624263637 (author amaybaum,
created 2026-11-04T06:28:45Z; quoted on `main` at A5-LINEAR-AFFINE Q1 and at
A5-Q4-STAGE2D:39–42) records: "Retain linearity as a posit. Do not assume all observers are
shift-invariant." and, under Q1, "Preserve Main's currently specified absolute interface as the
formal baseline. The shift-invariant interface is a legitimate conditional alternative, not yet a
derived description of all OI observers."

The contradiction is a mathematical fact about Main's text. The owner record is governance, cited
as such. It reaches the real lift through the SM:232 bridge, a setting input. For the observer of
SM §4.1 itself, no stated premise fixes the register. The observer projection P is required to be
equivariant for the spatial group only (SM:250–258), and the observer-level field, with its k = 0
mode, is the branch's variable (SM:230, Theorem 1).

### 4.2 Conditional sources (partial)

Two open alternatives would supply T1a for the constant mode.

1. **The shift-invariant interface 𝒜_C** (A5-LINEAR-AFFINE §3.3.1, a research record). Its
   diagonal readouts are functions of (x_V(t−1) mod a constant, x_V(t) mod a constant), with
   independent constants on the two slices. It is therefore invariant under the whole uniform
   sector: the static direction s, and the drift direction w as well. It is not a stated interface
   of the manuscripts (Q1, quoted above).
2. **A physical amplitude-scale gauge** (SM:96, Substratum:270). The global translation x ↦ x + c
   of the alphabet acts on every value at every time, so on phase space it is exactly σ_c. At
   κ = 2 and b = 0, σ_c commutes with F (lane 2 Proposition 5; A5-LINEAR-AFFINE N8′; [A]:
   A(c𝟙) = 2c𝟙). Then a passive relabelling that preserves φ, declared physically void, identifies
   the active states x and σ_c x [W].
   - The principle is "proposed", with "Independent operational warrant remains open" (SM:96) and
     "*Status (open)*" (Substratum:270).
   - The owner decision Q2 (same comment) reads: "Treat amplitude shifts as mathematical
     relabellings unless their physical gauge status is justified."
   - SM:811 names the principle the "additive-automorphism" group, which excludes translations.
     Its content is therefore stated in two non-equivalent ways at [P].

Single invariant readouts, which are partial sources only:
- the SM §6.5 link-difference map [A];
- E, since (2 − A)𝟙 = 0 at α = 1/d gives E(σ_c z) = E(z) [A], and with it every E-shell;
- the uniform counting measure on (ℤ/q)^{2N} at κ ≡ 2, for which E-shells are unions of σ-orbits
  (lane 1 §2.4 control, re-derived [A]).

None of these is the observer's complete register.

### 4.3 T1a and T1b

For a register given by visible itineraries, the kernel's passive quotient identifies two states
exactly when all their visible itineraries agree (PassiveQuotient `itiSetoid`;
ObservabilityQuotient, span(𝒟_K) equal to the ∼_K-invariant functions [K], for the carrier class
stated there). Hence [W, for transfer from the kernel's carrier to the real lift]:
- T1b implies T1a for any register that factors through the quotient;
- T1a for the itinerary register implies T1b, as the identification in the canonical quotient.

T1a and T1b therefore coincide for such observers, and T1b inherits §4.1–§4.2. Lane 2's further
equivalence with "taking the energy seminorm as the topology" is a statement about carrier Z
(T1Z, §6) and adds nothing on T, which is finite-dimensional.

### 4.4 Verdict

- **T1a:** contradicted at Main's stated interface. Partially sourced, conditional on 𝒜_C or on a
  physical amplitude-scale gauge, both open and classified by the owner as a conditional
  alternative and an unjustified relabelling respectively.
- **T1b:** unsourced within the searched scope, with the same conditional sources.

The gap is named: an established derivation that the observer of SM §4.1 registers only
shift-invariant functions, or a justified physical gauge status for the translation clause.

## 5. T2: the staggered static mode, and what lane 2's Proposition 5 consumes

### 5.1 The register

The staggered static shift τ_c adds c·(s, −s)⊗e, with s_n = (−1)^{abs(n)} and L even. It moves
visible values, so §4.1 applies unchanged: **T2a is contradicted at Main's stated interface** [A].

### 5.2 No conditional source

Write v = (s, −s). Since A s = −2s at α = 1/d, F v = (−s, −2s + s)·(−1)... directly:
F(s, −s) = (−s, A(−s) − s) = (−s, s) = −v. Then τ_c⁻¹ ∘ F ∘ τ_c (x) = F x − 2c v [A].

So τ_c is not a symmetry of F. As a passive relabelling it carries the linear rule to an affine
rule with a non-uniform (staggered) offset, which A5 excludes from the selected model [A].

It is also outside each alternative found for T1:
- it is not an alphabet relabelling, since it depends on site and time (SM:96 and Substratum:270
  name a single affine map of the alphabet);
- it is not in 𝒜_C, which is built from uniform constants;
- A5-LINEAR-AFFINE N6 records that "site-dependent translations are gauge, which the corpus does
  not state".

E is invariant under τ_c, because v is E-null and a positive semidefinite form's null vectors lie
in its radical [A]. That is one readout only.

**Verdict.** T2a is contradicted at Main's stated interface. T2a and T2b are unsourced within the
searched scope, even conditionally.

### 5.3 (F-slice) Proposition 5's exclusion without H-ZM

Lane 2's Proposition 5 obtains V_rest as the coisotropic reduction: the constraint w = 0 followed
by the quotient by L_0, the quotient being H-ZM. Here is a route that uses only the inputs of
lane 2's Proposition 4, namely b = 0 and an F-stationary law with finite second moments.

- (a) By Proposition 4(a), re-derived for C+1, the law is supported on L_0 ⊕ V_rest: zero drift
  in both null sectors. [A]
- (b) On L_0 ⊕ V_rest, F acts as +1 on the constant static labels c ∈ R^6, as −1 on the staggered
  labels a ∈ R^6, and as F on V_rest. So c and the pair {a, −a} are invariant. [A]
- (c) Disintegrate the law over (c, {a, −a}). Each conditional law lives on the union of the two
  affine slices x*(±) + V_rest, with x*(±) = c(1, 1) ± a(1, −1). It is F-stationary for almost every
  label, since F swaps the two slices and fixes the label. [W; standard disintegration over an
  invariant function]
- (d) In deviation coordinates y = x − x*(t), with x*(t) = c(1, 1) + (−1)^t a(1, −1) a static orbit
  of period at most two, y lies in V_rest and y(t+1) = F y(t) exactly. Lane 2's Theorem 1 applies
  there: E is positive definite on V_rest at α = 1/d, because the only k with abs(α Σ cos k_j) = 1
  are k = 0 and k = (π, …, π). This gives the unique tamed commuting J on every label sector.
  [A, using lane 2 Theorem 1]

**Consequence.** The null sector leaves the dynamical phase space as fixed, conserved classical
labels, not as a gauge quotient. No unobservability is assumed. The labels stay registered, which
agrees with Main's baseline interface. Lane 2's statement that exclusion "requires the named
hypothesis H-ZM" is therefore stronger than its proof shows. What Proposition 5 consumes is
supplied, on T at b = 0 under stationarity, by the constraint together with the disintegration.

**Pressure test** (favorable to the framework, so maximum skepticism):
1. It needs stationarity with finite second moments, exactly Proposition 4's input. With b_A1 ≠ 0
   it fails as lane 2's does (no stationary law).
2. J is centred on a static orbit of period at most two. This is lane 2 §2.6's centred structure,
   with a time-dependent centre on the staggered labels.
3. The uncentred second moment carries the labels (c, a), so J-Hermiticity of the uncentred Σ needs
   centring, as lane 2 §4.1 and its Proposition 11 already record.
4. Nothing is shown for carrier Z.
5. Nothing is shown about H-PF or Theorem 5's other inputs, which are unit A's and lane 2's
   questions.
6. Step (c) is [W]. The reviewer re-derives (a)–(d) independently (PLAN §9 item 4).

## 6. T1Z and T2Z (secondary)

No stated premise fixes the topology on Z: neither the one-particle space K nor the energy
completion H_E (lane 2's H-top). Lane 2's Proposition 6(c) holds for d = 1, 2 only, and it is a
model-written record (C−2). **Unsourced within the searched scope.**

## 7. T3: the SM:811 energy

### 7.1 What the text defines and requires (T3a, T3b)

- **Defined, for the linear lift.** SM:296 defines the conserved E(u, v) = u·u + v·v − u·Av and
  calls it the kinetic-plus-potential energy at α = 1/d. SM:294 calls it the "total energy". SM:292
  evaluates exactly this E on the real lift: "positive definite for $|\alpha|<1/d$, positive
  semidefinite at $\alpha=1/d$, with constant and, for even $L$, staggered null modes". [P]
- **Not treated, for the affine lift.** The selected model is linear (SM:240, A5).
- **Requirements** (SM:292): "a specified real positive-definite quadratic shell; it requires an
  energy, a limiting regime and treatment of zero modes"; "The null directions [...] have
  noncompact shells unless additional constraints are imposed". SM:811: "a real-valued conserved
  energy", a "candidate" resting on the open stationary-law hypothesis.
- **Status of the shell.** GR:699: "The shell is assumed [...]; it is not a consequence of Lemma 3,
  which supplies determinism, injectivity and the selected measure but no conserved energy."
  Main's ledger (iv) selects the maximal-entropy invariant measure "compatible with the observer's
  records" (Main:60, Main:736). It therefore selects an energy shell only through which conserved
  values the records fix. [P]

### 7.2 Proposition U1 (no conserved coercive function on the full space at α = 1/d) [A]

On T at α = 1/d, take any b. No conserved function on the full phase space has compact sublevel
sets. In particular, no conserved positive-definite quadratic form exists.

*Proof.*
- The uniform components (g_u, g_v) evolve as (g_v, 2g_v − g_u + b). With w = g_u − g_v and
  s = g_u + g_v, this gives w ↦ w − b and s ↦ s − 2w + b.
- If b ≠ 0, every orbit is unbounded in w.
- If b = 0, every orbit with w ≠ 0 is unbounded in s.
- A conserved function with compact sublevel sets would bound every orbit. ∎

For quadratic forms, the restriction of F to the invariant uniform sector, [[0, 1], [−1, 2]], has
(F − I)² = 0 with F ≠ I. A positive-definite invariant form would make F orthogonal and hence
diagonalizable, which it is not. With L even, the staggered sector gives [[0, 1], [−1, −2]], with
eigenvalue −1 double and non-diagonalizable, and the same conclusion.

So SM:292's "positive-definite quadratic shell" exists at the normalized branch only on a reduced
space, as SM:292 itself says ("unless additional constraints are imposed"). SM:811's stated
covariance proportional to □_lat⁻¹ is the massless operator, which places the measure at α = 1/d
(lane 1 D5). So the requirement binds exactly where it fails on the full space.

At b = 0 the invariant constraint slices exist: {w = 0, s = s₀}, with the staggered drift zero and
the level fixed up to sign, as in §5.3. On them E restricted to V_rest is positive definite [A].
SM states that constraints are needed and does not specify them. **Linear verdict: defined (E),
requirement met only on constraint slices, which are required but unspecified.** The selecting
condition is which conserved labels the observer's records fix (Main ledger (iv)). At Main's
absolute interface the static labels are registered and conserved, so fixing them agrees with the
records [W]. No premise states it.

### 7.3 Proposition U2 and Proposition U3 (affine, at resonance, b ≠ 0) [A]

- **U2.** For b ≠ 0, no orbit is bounded (U1), so no conserved function meets SM:292's requirement
  on the full space. No invariant constraint confined to the uniform sector exists, because w
  drifts (lane 1 §2.4, re-derived).
- **U3.** E = E_⊥ + E_0, with E_0 = N w² depending only on uniform variables (since A𝟙 = 2𝟙), and
  S_u + S_v = N s. Hence

      Q′ = E − b(S_u + S_v) = E_⊥ + (N w² − bN s) = E_⊥ + Q′_0,

  with Q′_0 a function of (w, s) alone. Every candidate (Q′, E_⊥, E_⊥ + f(Q′_0)) is E_⊥ plus a
  function of the uniform variables. Choosing among them is therefore choosing how the uniform
  sector enters the observer's description.
  - Any reading whose shell keeps the uniform sector fails the requirement (U2). That includes the
    E_⊥ reading on the full space, since E_⊥ leaves (w, s) unconfined.
  - A reading that removes the uniform sector, both s and the drift w (projecting onto C^⊥, which
    commutes with the dynamics because a uniform offset enters only the uniform sector), reduces
    every candidate to E_⊥.
  - That removal is stronger than H-ZM, which quotients static modes only. It is supplied only by
    an interface like 𝒜_C (§4.2, item 1), not by a stated one, and Main's absolute interface
    contradicts it for visible sites.

**Affine verdict: unspecified.** The text does not treat this case. No conserved function meets
the requirement on the full space. The residual choice is a uniform-sector treatment, not an
independent choice of energy, and no stated premise selects one.

### 7.4 (F-stag) E_⊥ at even L

At α = 1/d with L even, the staggered null vector (s, −s)⊗e is orthogonal to 𝟙, so it lies in the
non-uniform sector and is E_⊥-null [A]. E_⊥-shells therefore do not confine it.
- Lane 1 REPORT-r2 line 116 ("Each of them confines E_⊥") is correct as stated.
- Lane 1 line 297 ("with it the shell confines the non-uniform modes again") holds for odd L, or
  with the staggered labels fixed (§7.2).

The finding is offset-independent and leaves lane 1's class labels unchanged.

### 7.5 Consequence for #1049 D5

Lane 1's class-(c) placement of D5 does not depend on reading the energy as Q′. By U1–U3, at
resonance every reading that keeps the uniform sector fails SM:292's requirement when b ≠ 0, while
at b = 0 the invariant slice cures it. The dependence on b is the availability of an invariant
uniform-sector constraint, which is lane 1's own criterion.

The alternative-energy branch (a) needs the uniform sector removed from the description. No stated
premise supplies that removal, and Main's baseline interface contradicts it for visible sites. So
D5's placement rests on what the manuscript states, and the E_⊥ branch rests on an unstated
interface choice.

## 8. Controls

All controls are green on the writer's side. C−4 awaits the reviewer.

| Control | Outcome |
| --- | --- |
| C+1 | Found A5 (Main:736 (vii); SM:240; Substratum:100). From it: b = 0, w conserved, and with stationarity w = 0, since a nonzero conserved w would translate s with no invariant probability law [A]. Classified as supplying the constraint and not the quotient. **Green.** |
| C+2 | Found SM:296's E and its conservation for symmetric A, and SM:292's definiteness statement. Classified as the energy SM:292 names for the linear real lift (§7.1). **Green.** |
| C+3 | The sweep returned SM:292 for "zero mode" and SM:811 for "real-valued" and "conserved energy" (S4 hit lists). **Green.** |
| C−1 | SM:292's "requires an energy, a limiting regime and treatment of zero modes" was rejected as a source (requirement, §3). **Green.** |
| C−2 | Lane 2 Proposition 6(c) was rejected for T and for d = 3. It is a model-written record (§6). **Green.** |
| C−3 | Commutation of σ_c with F at κ = 2 and b = 0 was rejected as a source on its own. It enters §4.2 item 2 only together with the open gauge principle. **Green.** |
| C−4 | Every quote above was extracted with `git show` at [P] by the writer. The reviewer's re-extraction is pending. |
| C−5 | Q_B and P_C (SM:296) were not accepted as SM:811's energy. The text names E (§7.1). **Green.** |

## 9. Passes (§A.31 node log)

- **Pass 1** (S4 narrow terms, papers): SM:292–296 and SM:811 confirmed; near misses at
  Introduction:159, GR §6.2 and Main:260. No NEW finding.
- **Pass 2** (S1 ledger and Substratum §3.1, §4): the A4 transitivity reductio; the amplitude-scale
  Remark's open status. ELABORATING.
- **Pass 3** (D-2 records): A5-LINEAR-AFFINE §3.3.1, N6, owner decisions Q1 and Q2. **NEW:** §4.1
  and §5.2.
- **Pass 4** (Lean): the absolute observer of SubstratumInterfaceAudit; passive-quotient mechanism.
  ELABORATING: §4.3.
- **Pass 5** (T3 algebra): U1, U2, U3 and F-stag. **NEW:** §7.
- **Pass 6** (consumer check of lane 2 Proposition 5): F-slice. **NEW**, favorable, flagged.
- **Pass 7** (GR, Main §1.2 hits, book mirrors): GR:699; the book mirror of SM:96 (ch05:45,
  FULL:1360) agrees with "proposed". No NEW finding.
- **Pass 8** (Group B: unobservable, redundan): no new candidate. No NEW finding.

Stopping rule (a) applies, with the remainder of §1 named.

## 10. Productivity verdict (PLAN §7)

**Gem.**
- **Criterion 1.** T1 and T2 reach a contradiction branch at the baseline interface, together with
  a conditional source for T1 whose gap is exact. Both are strictly stronger than lane 2's "not
  supplied". T3 reaches an exact underdetermination, with the selecting condition named (U1–U3).
- **Criterion 2.** These decide what the Goal link asks:
  - for #1217, Proposition 5's exclusion rests on an unstated choice (H-ZM), which conflicts with
    the baseline interface and, by F-slice, can be replaced by constraint plus disintegration;
  - for #1049, D5's placement rests on the stated reading, and the E_⊥ branch on an unstated
    interface choice.

  They also expose two hidden assumptions:
  - in lane 2: exclusion of the null sector equated with a quotient;
  - in lane 1: confinement of the non-uniform modes at even L.

Classification: NEW for §4.1/§5.2, §7.2–7.4 and §5.3; POSITIVE for C+1; ELABORATING for §4.3.

## 11. Open nodes

- **O1.** The physical status of the amplitude-scale gauge's translation clause, and the variance
  between SM:96 (affine, translations included) and SM:811 (additive automorphisms). A
  manuscript-consistency question, outside this unit's authority.
- **O2.** Whether the observer of SM §4.1 inherits Main's absolute register through the SM:232
  bridge. Open, with the bridge.
- **O3.** F-slice: independent re-derivation. Whether Theorem 5's Σ (unit A, lane 2 H-PF) accepts
  label-sector J and centring.
- **O4.** The non-abelian case of the staggered change in the SM §6.5 map (§3, SM:811 row).
- **O5.** The unswept remainders of §1 (D-1 to D-6).
- **O6.** Carrier Z (H-top).

## 12. References not on `main` (§A.42 item 8)

- **#1049 comment 6624263637** (owner decisions Q1 and Q2, amaybaum, 2026-11-04T06:28:45Z).
  Classification: governance record, quoted. It is also on `main` in A5-LINEAR-AFFINE Q1 and
  A5-Q4-STAGE2D:39–42. The scientific claims of §4.1 rest on Main:88 and on the kernel, not on the
  comment.
- **#1169 comments 7189139613 and 7189143747:** provenance.
- **PLAN commit `d4f97b53`:** on the unit branch. This report lands with it.
- Every other reference is on `main` at [P].
