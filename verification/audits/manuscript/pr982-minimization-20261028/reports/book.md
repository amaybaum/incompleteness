# Minimal #982 — group: book

Minimal files: `min982-work/minimal/book/<file>.md` (OLD text + only the N edits below). `The-Incompleteness-of-Observation-FULL.md` not touched (coordinator mirrors).

Class key: N = necessary (G-item or concrete falsity); U = unnecessary, reverted to OLD; UNCERTAIN = kept OLD, flagged. 'nonG-*' = necessary on a concrete falsity outside G1–G7 (coordinator may drop as a group). Branch qualifier used uniformly for G5: “on the nonzero-$Y_Q$ branch”.

## book/ch00-introduction.md

| old line | class | reason |
|---|---|---|
| 95 | N+U | ch00-1 applied; rest of #982 rewrite (Theorem 24 / Pair C narration, "does not recover a unique local branch") U — rewording/new material |
| 97 | N+U | ch00-2, ch00-3 applied; rest of #982 rewrite of Part II summary U |

N edits (exact old → minimal):

- **ch00-1** [G1/G3]  
  OLD: `M1-T, C2-mixing and the semigroup-transfer completeness step, the local propagating lattice/gauge residue is uniquely fixed up to the stated gauge freedoms.`  
  MIN: `M1-T, C2-mixing and the nearest-neighbor restriction, the local propagating lattice/gauge residue is fixed.`
- **ch00-2** [nonG-commutant]  
  OLD: `$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ as the pointwise commutant, chirality`  
  MIN: `$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ from the bicommutant of the cubic-group action, chirality`
- **ch00-3** [G5]  
  OLD: `and anomaly cancellation forcing the observed hypercharges.`  
  MIN: `and anomaly cancellation forcing the observed hypercharges on the nonzero-$Y_Q$ branch.`

## book/ch01-observation.md

| old line | class | reason |
|---|---|---|
| 8 | U | G6: "cannot condition on the complete state" correct for embedded observers; #982 replacement relies on Prop 24.5 (reverted) |
| 213 | U | G6/24.5-dependent rewrite of C1 corollary |
| 229–261 | U | C3-limit rewrite relies on Prop 24.5 / external-record reading (G6). UNCERTAIN note: old "complete failure — N_H→0" of C3 (capacity inequality is vacuous at I*=0) — kept old |

## book/ch02-substratum.md

| old line | class | reason |
|---|---|---|
| 10 | U | three-questions framing; not false |
| 28 | U | is/describes undecidability; no 24.1 dependence |
| 38–42 | U | G6 (incompleteness family, halting analogue) — 24.5 reverted |
| 44 | U | deep-sector gauge relies on (iii)/boundary lemma (G7); q gauge only under stated hypothesis |
| 46 | N | ch02-1 |
| 50 | N+U | ch02-2 applied; #982 rewrite of §2.4 intro / input paragraph otherwise U |
| 52 | U | input-class methodology sentence |
| 88 | N | ch02-3 |
| 94 | U | Stage 2 heading; NN premise already explicit at line 100 |
| 100 | U | link count already conditional on H-link, m=1 disclaimer present |
| 102 | N+UNCERTAIN | ch02-4 (Schur: strict commutant is U(1)^3; old ch03:74 says so). Amplitude-scale reduction of all block phases kept old — UNCERTAIN (audit says one common rescaling gives at most a diagonal circle) |
| 104 | N+UNCERTAIN | ch02-5 (G5). Missing H-χ'/H-spin' in this sentence kept old (UNCERTAIN; stated elsewhere in chapter) |
| 108 | N | ch02-6 |
| 116 | U | heading rename |
| 118 | N | ch02-7 |
| 120 | N+U | ch02-8 (NN premise); rest ("Standard Model gauge group ... derived") U |
| 122 | N | ch02-9 |
| 124 | U | "local-residue uniqueness" retained = uniqueness of Stage-2 invariants (Lemma 23.0 as minimally corrected) |
| 126 | N | ch02-10 |
| 132 | N | ch02-11 |
| 134 | N | ch02-12 |
| 136–138 | U | Lagrangian remark; Generators statement header |
| 140 | N | ch02-13 (G2) |
| 142–148 | U/UNCERTAIN | (ii) conditional; (iii) sound (G7); (iv) graph isomorphism "same emergent physics" vs definition's "same T_ij(t)" — UNCERTAIN, kept old (coordinator: consistency with Substratum Thm 24(iv)); proof paragraph kept |
| 150 | N | ch02-14 |
| 152 | N | ch02-15 false proof step (Stinespring-extended-per-Lemma-24.1) deleted |
| 154–160 | N | ch02-16/17/18; global-phase item unchanged |
| 162–172 | N+UNCERTAIN | ch02-19 at 164. Level-2 "image of G_sub", "eigenspaces of the coupling matrix", Level1⊂2⊂3 nesting, "SM group is the image of G_sub" — UNCERTAIN, kept old (no 24.1 dependence shown; audit flags as unproved) |
| 174 | N | ch02-20 |
| 176 | N | ch02-21 |
| 178 | N | ch02-22 |
| 182 | U | §2.6 intro framing |
| 186 | N+U | ch02-23; rest U (H-Bell scoping already present) |
| 195 | N+U | ch02-24 (gauge-equivalence via T relied on arbitrary relabelling, G2); ordering/CP sentences U |
| 203 | N+U | ch02-25; rest U |
| 213 | U | QM–GR projection framing |
| 217 | UNCERTAIN | "unique image of the substratum's symmetry under partial trace" — kept old; no 24.1 dependence shown |
| 218 | N | ch02-26 (the hunk at old 224 in my analysis = file line 218) |
| 222–228 | U | §2.8 summaries |

N edits (exact old → minimal):

- **ch02-1** [G3]  
  OLD: `from observed physics plus structural assumptions, up to the stated gauge action.`  
  MIN: `from observed physics plus structural assumptions.`
- **ch02-2** [G3]  
  OLD: `observed physics fixes up to a precise equivalence. It establishes uniqueness of that local residue under its stated conditions.`  
  MIN: `observed physics fixes. It establishes uniqueness of that local residue's Stage-2 invariants under its stated conditions.`
- **ch02-3** [G1/G3]  
  OLD: `with M1-T, C2-mixing and the semigroup-transfer completeness step, the **local propagating lattice/gauge residue** is uniquely fixed up to the stated gauge freedoms, including`  
  MIN: `with M1-T, C2-mixing and the nearest-neighbor restriction, the **local propagating lattice/gauge residue** is fixed, including`
- **ch02-4** [nonG-commutant]  
  OLD: `The pointwise commutant of this action — the set of unitary transformations commuting with the cubic-group representation — is`  
  MIN: `The unitary group of the bicommutant of this action — the block algebra generated by the cubic-group representation — is`
- **ch02-5** [G5]  
  OLD: `(1/6, 2/3, -1/3, -1/2, -1)$ uniquely determined.`  
  MIN: `(1/6, 2/3, -1/3, -1/2, -1)$ uniquely determined on the nonzero-$Y_Q$ branch, up to normalization.`
- **ch02-6** [G3]  
  OLD: `and the output is unique up to $\mathcal{G}_{\text{sub}}$.`  
  MIN: `and the output is unique.`
- **ch02-7** [G1/G3]  
  OLD: `and, additionally, the semigroup-transfer completeness step (Substratum Lemma 24.1). Then the **local propagating lattice/gauge residue** is uniquely fixed up to the stated substratum-gauge freedoms:`  
  MIN: `and, additionally, the nearest-neighbor restriction of Stage 2. Then the **local propagating lattice/gauge residue** is fixed:`
- **ch02-8** [G3]  
  OLD: `together with six structural assumptions, the substratum is forced`  
  MIN: `together with six structural assumptions and the nearest-neighbor restriction, the substratum is forced`
- **ch02-9** [G3]  
  OLD: `First, uniqueness is within the structural class A1–A6.`  
  MIN: `First, uniqueness is within the structural class A1–A6 with the nearest-neighbor restriction.`
- **ch02-10** [G1]  
  OLD: `by identifying its generators and showing they exhaust — conditional on the semigroup-transfer lemma — the freedom in the reconstruction.`  
  MIN: `by identifying its generators; whether they exhaust the freedom in the reconstruction is open.`
- **ch02-11** [G1]  
  OLD: `by exhibiting four families of generators and establishing, conditional on the semigroup-transfer lemma (Substratum Lemma 24.1), that they exhaust the group.`  
  MIN: `by exhibiting four families of generators; whether they exhaust the group is open.`
- **ch02-12** [G1/G3]  
  OLD: `is defined by the equivalence relation under which the local reconstruction is unique: $(S`  
  MIN: `is defined by the equivalence relation: $(S`
- **ch02-13** [G2]  
  OLD: `*(i) State relabeling.* For any bijection $\pi: S \to S$, the substratum $(S, \pi \circ \varphi \circ \pi^{-1})$ produces the same emergent physics as $(S, \varphi)$. The transition probabilities depend on the coupling structure of $\varphi$ — which states are sent to which — but not on which labels are attached to which states. This is an $|S|!$-element subgroup,`  
  MIN: `*(i) Hidden-state relabeling.* For any bijection $\sigma$ of the hidden configurations $\mathcal{C}_H$, applied in every visible fibre as $\pi(v,h) = (v, \sigma(h))$, the substratum $(S, \pi \circ \varphi \circ \pi^{-1})$ produces the same emergent physics as $(S, \varphi)$. The transition probabilities depend on the coupling structure of $\varphi$ — which states are sent to which — but not on which labels are attached to which hidden states; a relabeling $(v,h) \mapsto (v, \sigma_v(h))$ that differs between visible fibres preserves the transition probabilities $T_{ij}(t)$ but not, in general, the coherent channels. This is an $|\mathcal{C}_H|!$-element subgroup,`
- **ch02-14** [G1]  
  OLD: `**Conditional completeness.** For the reconstructed dilation/local datum, and subject to the semigroup-transfer lemma (Substratum Lemma 24.1 — the standard Stinespring/GNS uniqueness extended to the discrete unitary-generated channel family, identified there for specialist verification), the four families **conditionally exhaust** $\mathcal{G}_{\text{sub}}$ — any observables-preserving transformation of that scoped datum decomposes as a composition of generators (i)–(iv). This completeness statement does not classify preparation-indexed Bell adjacency or other Bell-composite data.`  
  MIN: `**Completeness.** For the reconstructed dilation/local datum, whether the four families exhaust $\mathcal{G}_{\text{sub}}$ — whether any observables-preserving transformation of that scoped datum decomposes as a composition of generators (i)–(iv) — is open. This completeness question does not extend to preparation-indexed Bell adjacency or other Bell-composite data.`
- **ch02-15** [G1 (false proof step removed)]  
  OLD: `The argument uses the Stinespring uniqueness theorem of Chapter 1, extended per that lemma. Suppose $g: (S, \varphi) \to (S', \varphi')$ is an observables-preserving transformation between two representatives of the reconstructed dilation/local datum. By assumption, $g$ preserves the visible-sector quantum channel $\Phi$ — the CPTP map that gives the emergent quantum dynamics. Stinespring's uniqueness theorem states that any two dilations of the same channel on the same visible Hilbert space differ by a partial isometry on the hidden sector. At the substratum level, this partial isometry is either a relabeling of hidden-sector states (generator (i) restricted to $\mathcal{C}_H$) when the two hidden sectors have equal cardinality, or a composition of relabeling and deep-sector enlargement/reduction (generators (i) + (iii)) when they differ in size. Under the alphabet-size hypothesis the alphabet may change freely (generator (ii)). The local coupling graph must have the same statistical properties — dimension, spectral structure, isotropy — since these determine the scoped derivation chain's outputs, and two such graphs are related by generator (iv). These four degrees of freedom exhaust — conditional on the semigroup-transfer lemma — the freedom in that reconstructed datum, so the four generators span $\mathcal{G}_{\text{sub}}$ on this domain. The argument does not constrain the separate preparation-indexed Bell-composite rule.`  
  MIN: `[paragraph deleted]`
- **ch02-16** [G1/G2]  
  OLD: `Three candidate fifth generators are explicitly subsumed by the four already listed:`  
  MIN: `Three candidate fifth generators are compared with the four already listed:`
- **ch02-17** [G2]  
  OLD: `This is generator (i) with $\pi = T$.`  
  MIN: `Since $T$ acts on the visible layers, this is not generator (i).`
- **ch02-18** [G1]  
  OLD: `By Stinespring uniqueness, any two same-channel dilations of equal hidden-sector dimension differ by a hidden-sector unitary — generator (i) restricted to $\mathcal{C}_H$.`  
  MIN: `Equality of the visible channel family does not force a hidden-sector unitary relating two dilations of equal hidden-sector dimension: two permutation systems on $\mathbb{Z}_2 \times \mathbb{Z}_3$ have equal visible channels at every time without being unitarily conjugate (Substratum §4). Whether such reparametrizations reduce to generator (i) is the open completeness question.`
- **ch02-19** [G1/G3]  
  OLD: `The local reconstruction theorem holds modulo $\mathcal{G}_{\text{sub}}$; Bell-composite preparation rules are outside this completeness statement.`  
  MIN: `Bell-composite preparation rules are outside its scope.`
- **ch02-20** [G2]  
  OLD: `state relabelings, decoupled deep-sector enlargements`  
  MIN: `hidden-state relabelings, decoupled deep-sector enlargements`
- **ch02-21** [G3/G7]  
  OLD: `The **reconstructed local lattice/gauge residue modulo** $\mathcal{G}_{\text{sub}}$ is uniquely determined — under the reconstruction theorem's stated conditions — by observation plus structural assumptions. Individual representatives of that local residue are gauge expressions`  
  MIN: `The invariants of the **reconstructed local lattice/gauge residue** are uniquely determined — under the reconstruction theorem's stated conditions — by observation plus structural assumptions. Individual representatives of that local residue related by the generators of $\mathcal{G}_{\text{sub}}$ are gauge expressions`
- **ch02-22** [G3]  
  OLD: `fixes that local residue under the theorem's stated conditions up to the specified gauge equivalence.`  
  MIN: `fixes that local residue under the theorem's stated conditions.`
- **ch02-23** [nonG-commutant]  
  OLD: `$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ as the commutant of the cubic-symmetric coupling matrix, three chiral`  
  MIN: `$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ from the commutant of the cubic-symmetric coupling matrix, three chiral`
- **ch02-24** [G2]  
  OLD: `The two directions are gauge-equivalent at the substrate level ($\varphi \leftrightarrow \varphi^{-1}$)`  
  MIN: `The two directions are related by the layer swap at the substrate level ($\varphi \leftrightarrow \varphi^{-1}$)`
- **ch02-25** [nonG-commutant]  
  OLD: `The same local lattice sector that gives the Standard Model gauge group as the commutant of the coupling matrix`  
  MIN: `The same local lattice sector that gives the Standard Model gauge group from the commutant of the coupling matrix`
- **ch02-26** [nonG-commutant]  
  OLD: `The same trace-out that gives the Standard Model gauge group as the commutant of the coupling matrix`  
  MIN: `The same trace-out that gives the Standard Model gauge group from the commutant of the coupling matrix`

## book/ch03-structural-realism.md

| old line | class | reason |
|---|---|---|
| 8 | N | ch03-1 |
| 34 | U | G_sub vs universality class; G_sub classifies by definition |
| 40 | N | ch03-2 |
| 66–72 | U/UNCERTAIN | G1 level, G2 level; "every G1 transformation is a G2 transformation" UNCERTAIN, kept |
| 74 | N | ch03-3 (missing NN premise in gauge-group uniqueness) |
| 76 | N | ch03-4 |
| 78–92 | U/UNCERTAIN | image/nesting claims (G1⊂G2⊂G3⊂G4) kept — UNCERTAIN, no 24.1 dependence shown |
| 104 | N | ch03-5 |
| 106 | N | ch03-6 |
| 116 | N | ch03-7 |
| 136–150 | U | hidden-sector relabelling (uniform reading consistent with G2), gauge-incompleteness species, methodology |
| 202–204 | U | Spinoza parallel |
| 208 | N | ch03-8 |
| 214 | U | G6 (Breuer correct) |
| 220 | N | ch03-9/10/11; turtles/simulation reasoning on decoupled deep sector kept (G7) |
| 222 | U | G6 (computational incompleteness of first turtle) |
| 224 | N | ch03-12 |
| 226–228 | U | ledger passage; "below stops referring" relies on (iii) |

N edits (exact old → minimal):

- **ch03-1** [G3]  
  OLD: `and the equivalence class is what observation plus structural assumptions, under Theorem 23's stated conditions, force.`  
  MIN: `and the class's local invariants are what observation plus structural assumptions, under Theorem 23's stated conditions, force.`
- **ch03-2** [G3]  
  OLD: `uniquely fix this **local residue** up to $\mathcal{G}_{\text{sub}}$ under Theorem 23's conditions.`  
  MIN: `fix this **local residue** under Theorem 23's conditions.`
- **ch03-3** [G3]  
  OLD: `depends on the structural inputs A3–A6 plus the empirical input E4`  
  MIN: `depends on the structural inputs A3–A6 and the nearest-neighbor restriction plus the empirical input E4`
- **ch03-4** [G1]  
  OLD: `The Stinespring uniqueness theorem, extended per the semigroup-transfer lemma (Substratum Lemma 24.1, identified there for specialist verification), conditionally establishes that these four families exhaust the freedom.`  
  MIN: `Whether these four families exhaust the freedom is open (Substratum §4).`
- **ch03-5** [G3]  
  OLD: `Chapter 2 shows that this local residue is uniquely fixed under Theorem 23's stated conditions.`  
  MIN: `Chapter 2 shows that the invariants of this local residue are uniquely fixed under Theorem 23's stated conditions.`
- **ch03-6** [G5]  
  OLD: `the anomaly-free hypercharge assignment. This level's`  
  MIN: `the anomaly-free hypercharge assignment on the nonzero-$Y_Q$ branch. This level's`
- **ch03-7** [G5]  
  OLD: `the anomaly-free hypercharges, the composite Higgs — are forced uniquely`  
  MIN: `the anomaly-free hypercharges on the nonzero-$Y_Q$ branch, the composite Higgs — are forced uniquely`
- **ch03-8** [G1]  
  OLD: `with four generator families and a completeness theorem conditional on the semigroup-transfer step (Substratum Lemma 24.1).`  
  MIN: `with four generator families whose completeness is open.`
- **ch03-9** [G3/G7]  
  OLD: `The reconstruction determines the substratum only up to the gauge group`  
  MIN: `The reconstruction determines the substratum at most up to the gauge group`
- **ch03-10** [G7]  
  OLD: `and it is gauge exactly when the group's generators move it`  
  MIN: `and it is gauge when the group's generators move it`
- **ch03-11** [G7]  
  OLD: `which coordinate chart spacetime is really in: there the diffeomorphism invariants exhaust the physics, and here the $\mathcal{G}_{\text{sub}}$ invariants do, conditional on the semigroup-transfer completeness step (that exhaustion is what the reconstruction theorem's equivalence-class form, read through §3.6's identification, conditionally asserts). A question`  
  MIN: `which coordinate chart spacetime is really in. A question`
- **ch03-12** [G7]  
  OLD: `from that surface fact, and the reconstruction exhausts its content — conditional on Lemma 24.1's completeness step — exactly where the gauge class begins.`  
  MIN: `from that surface fact.`

## book/ch04-methodology.md

| old line | class | reason |
|---|---|---|
| 26 | N | ch04-1 |
| 32 | U | "beyond what the reconstruction theorem forces" |
| 36 | N | ch04-2 |
| 66–72 | U/UNCERTAIN | Layer 3 wording; "gauge group determined ... by the cubic-group commutant" (loose) kept |
| 118 | N+UNCERTAIN | ch04-3; "falsifies the cubic-group decomposition" (a math fact cannot be falsified) kept — UNCERTAIN |
| 160–172 | U | solution-specific/gauge representatives; definitional |
| 190 | N | ch04-4 |

N edits (exact old → minimal):

- **ch04-1** [G3]  
  OLD: `the framework's uniqueness is *within* the class defined by A1–A6, not absolute.`  
  MIN: `the framework's uniqueness is *within* the class defined by A1–A6 and the nearest-neighbor restriction, not absolute.`
- **ch04-2** [G1]  
  OLD: `a constructively classified gauge structure`  
  MIN: `a constructively generated gauge structure`
- **ch04-3** [nonG-commutant]  
  OLD: `the framework derives this gauge group as the unitary group of the bicommutant`  
  MIN: `the framework derives this gauge group from the unitary group of the bicommutant`
- **ch04-4** [G5]  
  OLD: `the unique anomaly-free hypercharges, and the Cabibbo angle`  
  MIN: `the anomaly-free hypercharges (unique on the nonzero-$Y_Q$ branch, up to normalization), and the Cabibbo angle`

## book/ch07-gravity.md

| old line | class | reason |
|---|---|---|
| 16 | U | Tier 3 rewording |

## book/ch08-juno.md

| old line | class | reason |
|---|---|---|
| 146 | N | ch08-1 (G2: covariance claim relied on arbitrary state relabelling) |
| 148 | U | rewording |

N edits (exact old → minimal):

- **ch08-1** [G2]  
  OLD: `of the equivalence class $[(S, \varphi)] / \mathcal{G}_{\text{sub}}$, gauge-covariant up to state-relabeling under the substratum gauge group.`  
  MIN: `of the equivalence class $[(S, \varphi)] / \mathcal{G}_{\text{sub}}$.`

## book/ch09-universality.md

| old line | class | reason |
|---|---|---|
| 36 | N | ch09-1 |
| 140–158 | U | Tier 2/3 rewording, table status cells |
| 261 | U | conformal-gravity comparison: no sentence shown to rely on 24.1 completeness or arbitrary relabelling (invariant list = observables, invariant by definition) |

N edits (exact old → minimal):

- **ch09-1** [G3]  
  OLD: `the equivalence class $[(S, \varphi)] / \mathcal{G}_{\text{sub}}$ determined by the reconstruction theorem.`  
  MIN: `the equivalence class $[(S, \varphi)] / \mathcal{G}_{\text{sub}}$.`

## book/ch10-chemistry.md

| old line | class | reason |
|---|---|---|
| 28 | N | ch10-1 (typo "link link" kept: stylistic) |

N edits (exact old → minimal):

- **ch10-1** [G3 + missing m=1 premise]  
  OLD: `(The H-link link count $K = 2dm$ and the Bravais-lattice uniqueness theorem then operate`  
  MIN: `(The H-link link count $K = 2dm$ with $m = 1$ and the nearest-neighbor Bravais-lattice uniqueness theorem then operate`

## book/ch12-evolution-intelligence.md

| old line | class | reason |
|---|---|---|
| 191 | N | ch12-1 |
| 199–217 | U | G6 (cannot determine h; Gödel/Turing/OI comparison) — 24.5 reverted |
| 219 | N | ch12-2 |
| 227 | N | ch12-3 (row 1) |
| 229 | U | row "Determine h — provably impossible" (G6) |
| 238 | U | self-reference (G6) |

N edits (exact old → minimal):

- **ch12-1** [G3]  
  OLD: `can discover $(S, \varphi)$ from observations`  
  MIN: `can discover the local invariants of $(S, \varphi)$ from observations`
- **ch12-2** [G1]  
  OLD: `The gauge-classification theorem is precisely the statement`  
  MIN: `The gauge-generator theorem is precisely the statement`
- **ch12-3** [G3]  
  OLD: `| Discover $(S, \varphi)$ from observations |`  
  MIN: `| Discover the local invariants of $(S, \varphi)$ from observations |`

## book/ch14-quantum-computing.md

| old line | class | reason |
|---|---|---|
| 74 | U | G6/24.5 |
| 240 | N | ch14-1 |

N edits (exact old → minimal):

- **ch14-1** [G2]  
  OLD: `the gauge group includes state relabeling,`  
  MIN: `the gauge group includes hidden-state relabeling,`

## book/ch18-beyond.md

| old line | class | reason |
|---|---|---|
| 106–108 | U | G6/24.5 |
| 205 | U | G6 |

## book/ch19-open-problems.md

| old line | class | reason |
|---|---|---|
| 200 | U | deep-sector cardinality gauge (G7) |
| 208 | N | ch19-1 |
| 210–216 | U | rewording |
| 220 | U | standard-status framing |
| 222 | N | ch19-2 |
| 224 | N+UNCERTAIN | ch19-3; old text contains revision-history narration ("The earlier framing of this as ... mistook ...") — kept old (not a #982-necessary correction), flagged for coordinator under §A.30 |
| 234 | U | framing note |

N edits (exact old → minimal):

- **ch19-1** [G1/G3]  
  OLD: `under its stated modeling, mixing and completeness premises — uniqueness only of the **local propagating lattice/gauge residue modulo the stated gauge freedoms**.`  
  MIN: `under its stated modeling, mixing and nearest-neighbor premises — uniqueness only of the **local propagating lattice/gauge residue**.`
- **ch19-2** [G5]  
  OLD: `the generation count of three, the anomaly-free hypercharges, and the Cabibbo angle`  
  MIN: `the generation count of three, the anomaly-free hypercharges (on the nonzero-$Y_Q$ branch, up to normalization), and the Cabibbo angle`
- **ch19-3** [G3]  
  OLD: `a "uniquely-fixed-modulo-gauge" result`  
  MIN: `a "uniquely-fixed" result`

## book/glossary.md

| old line | class | reason |
|---|---|---|
| 9 | N | gl-1 |
| 75 | N | gl-2 |
| 79 | U | God's-eye (G6, consistent with ch01 kept) |
| 89 | N | gl-3 |

N edits (exact old → minimal):

- **gl-1** [G5]  
  OLD: `from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$, with no free parameters.`  
  MIN: `from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ on the nonzero-$Y_Q$ branch, with no free parameters.`
- **gl-2** [nonG-commutant]  
  OLD: `the framework derives this gauge group as the unique commutant of a cubic-symmetric coupling matrix`  
  MIN: `the framework derives this gauge group from the unique commutant of a cubic-symmetric coupling matrix`
- **gl-3** [G5]  
  OLD: `The framework derives these values as the unique anomaly-free solution.`  
  MIN: `The framework derives these values as the unique anomaly-free solution on the nonzero-$Y_Q$ branch.`

## book/README.md

| old line | class | reason |
|---|---|---|
| 52 | N+UNCERTAIN | rd-1 (Grassmann-valued/bilinear contradicts ch05:175 "no Grassmann variables"); "low-energy projection ... /Z6" kept — UNCERTAIN |
| 54 | N | rd-2 |

N edits (exact old → minimal):

- **rd-1** [nonG-false-description]  
  OLD: `Develops the cubic three-dimensional lattice with Grassmann-valued site variables and the bilinear, block-diagonal dynamics that constitutes the substratum.`  
  MIN: `Develops the cubic three-dimensional lattice and the dynamics that constitutes the substratum.`
- **rd-2** [G1]  
  OLD: `with the gauge group constructively classified rather than postulated.`  
  MIN: `with the gauge group constructively generated rather than postulated.`

## book/appendix-b-derivations.md

| old line | class | reason |
|---|---|---|
| 18 | N | apb-1 |
| 20 | U | B.6 summary ("coupling matrix's eigenvalue multiplicities") kept |
| 227 | N | apb-2 |
| 229 | N | apb-3 (Theorem B.5.1 statement) |
| 276–278 | U | Conclusion correct: ν_L neutrality fixes Y_Q=1/6≠0, excluding the neutral branch |
| 280 | N | apb-4 (false arithmetic "+1 = … = 2 … no, let me reorganize") |
| 282 | UNCERTAIN | "free parameter in the SM … theorem of the framework" kept |
| 288 | U | B.6 intro |
| 315 | U | identification paragraph |
| 317 | N | apb-5 |
| 321 | N | apb-6 |
| 323 | U | (ii) |
| 325 | N | apb-7 |
| 327 | U | (iv) |
| 329 | N | apb-8 |
| 333 | U | "no phenomenological inputs beyond d=3" (hypotheses are not phenomenological inputs; conditional framing present) |
| 339–357 | U/UNCERTAIN | B.6b intro, Lemma (already NN), Steps 1–2 (loose "commutant with two SU(3)") kept |
| 359 | N | apb-9 |
| 361–363 | U | single-basis Bravais commitment |
| 367 | N | apb-10 |
| 373–383 | UNCERTAIN | B.6c: physical spin from Gamma matrices without H-spin' — kept old |
| 385 | N+UNCERTAIN | apb-11; "anomaly cancellation operates generation-by-generation: each generation must independently satisfy" is false in general (anomalies cancel on the total spectrum) — kept old, flagged |
| 387–396 | U/UNCERTAIN | Step 5, verification |
| 398 | N | apb-12 |
| 400 | U | combination summary |
| 472 | N | apb-13 |

N edits (exact old → minimal):

- **apb-1** [G5]  
  OLD: `derives the unique hypercharge assignment from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. This appendix gives`  
  MIN: `derives the unique hypercharge assignment on the nonzero-$Y_Q$ branch from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. This appendix gives`
- **apb-2** [G5]  
  OLD: `derives the unique hypercharge assignment from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. The derivation establishes that the observed hypercharges are not phenomenological inputs but the unique anomaly-free completion of the framework's gauge structure.`  
  MIN: `derives the unique hypercharge assignment on the nonzero-$Y_Q$ branch from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. The derivation establishes that the observed hypercharges are not phenomenological inputs but the unique anomaly-free completion on the nonzero-$Y_Q$ branch of the framework's gauge structure.`
- **apb-3** [G5]  
  OLD: `the six anomaly conditions determine the hypercharges uniquely up to the overall normalization and the interchange $Y_u \leftrightarrow Y_d$, the latter`  
  MIN: `the six anomaly conditions determine the hypercharges on the nonzero-$Y_Q$ branch uniquely up to the overall normalization and the interchange $Y_u \leftrightarrow Y_d$, the latter`
- **apb-4** [nonG-false-arithmetic]  
  OLD: `**Corollary.** $|q_p| = |q_e|$ is a *theorem*, not a coincidence: proton charge $+1 = 2 Y_u + Y_d + 2 \cdot 1/2 = 4/3 - 1/3 + 1 = 2$... no, let me reorganize.`  
  MIN: `**Corollary.** $|q_p| = |q_e|$ is a *theorem*, not a coincidence.`
- **apb-5** [nonG-commutant]  
  OLD: `is the maximal group preserving the eigenvalue structure: $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.`  
  MIN: `is the maximal group preserving the eigenvalue structure: $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$, the group from which Chapter 5 §5.5 obtains $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.`
- **apb-6** [nonG-anchor (SM §4.5: minimization does not fix K)]  
  OLD: `(i) Coupling-degree minimization on the $d = 3$ cubic lattice fixes $K = 6$ internal components per site.`  
  MIN: `(i) The H-link link count with $m = 1$ on the $d = 3$ cubic lattice fixes $K = 6$ internal components per site.`
- **apb-7** [nonG-commutant]  
  OLD: `(iii) The commutant of the coupling matrix with these multiplicities is $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.`  
  MIN: `(iii) The commutant of the coupling matrix with these multiplicities is $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$, from which Chapter 5 §5.5 obtains $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.`
- **apb-8** [G5]  
  OLD: `(v) Anomaly cancellation (Appendix B.5) uniquely determines the hypercharges.`  
  MIN: `(v) Anomaly cancellation (Appendix B.5) uniquely determines the hypercharges on the nonzero-$Y_Q$ branch.`
- **apb-9** [G3 + anchor]  
  OLD: `The framework's coupling-degree minimization argument (Chapter 5 §5.4) rules out this alternative by forcing $K = 2d = 6$ internal components and *nearest-neighbor* coupling specifically — BCC's axial directions are next-nearest rather than nearest, and the framework's commitment to minimal coupling degree excludes them.`  
  MIN: `The framework's nearest-neighbor restriction (an assumption beyond bounded coupling) rules out this alternative — BCC's axial directions are next-nearest rather than nearest, and the nearest-neighbor restriction excludes them.`
- **apb-10** [G3]  
  OLD: `consistent with the Standard Model gauge group under the framework's commutant construction.`  
  MIN: `consistent with the Standard Model gauge group under the framework's commutant construction on nearest-neighbor links.`
- **apb-11** [G5]  
  OLD: `The unique anomaly-free hypercharge assignment (Appendix B.5) requires`  
  MIN: `The anomaly-free hypercharge assignment (Appendix B.5) requires`
- **apb-12** [nonG-anchor (SM §4.5)]  
  OLD: `(simple cubic lattice, $K = 2d$ minimization, staggered-Dirac reconstruction, anomaly cancellation)`  
  MIN: `(simple cubic lattice, $K = 2d$ link count under H-link, staggered-Dirac reconstruction, anomaly cancellation)`
- **apb-13** [G5]  
  OLD: `- B.5 establishes the unique anomaly-free hypercharge assignment, fixing`  
  MIN: `- B.5 establishes the unique anomaly-free hypercharge assignment on the nonzero-$Y_Q$ branch, fixing`

## book/appendix-c-objections.md

| old line | class | reason |
|---|---|---|
| 224 | U | G6 / 24.5 |
| 289 | N | apc-1 |

N edits (exact old → minimal):

- **apc-1** [nonG-anchor (SM §4.5: minimization does not fix K)]  
  OLD: `Coupling-degree minimization, which fixes $K=2d=6$, is a definition of a "site" given a bijection rather than a tunable preference, under H-link $K=2dm$ follows from the link count rather than as a selection rule; a different $K$ corresponds to a different bijection.`  
  MIN: `Under H-link $K=2dm$ follows from the link count rather than as a selection rule, with $m=1$ giving $K=6$; a different $K$ corresponds to a different bijection.`

## Statement-level changes (OLD vs MINIMAL) needing ledger updates

- ch02 **Reconstruction Theorem** (book form of Theorem 23): premise "semigroup-transfer completeness step (Substratum Lemma 24.1)" → "nearest-neighbor restriction of Stage 2"; conclusion "uniquely fixed up to the stated substratum-gauge freedoms" → "fixed" (ch02-7).
- ch02 **definition of $\mathcal G_{\rm sub}$**: "equivalence relation under which the local reconstruction is unique" → "equivalence relation" (ch02-12).
- ch02 **Theorem (Generators)**, family (i): arbitrary $\pi:S\to S$ / $|S|!$ → hidden relabelling $\pi(v,h)=(v,\sigma(h))$ uniform over visible fibres / $|\mathcal C_H|!$; fibre-dependent relabelling preserves $T_{ij}(t)$ only (ch02-13).
- ch02 **Conditional completeness** → **Completeness: open**; supporting Stinespring-per-Lemma-24.1 argument paragraph deleted; "hidden-sector reparametrization" and "time reversal" no longer subsumed under (i) (ch02-14…18).
- ch03 Level G3 description: completeness "conditionally established" → open (ch03-4); Worrall passage completeness theorem → open (ch03-8).
- appendix-b **Theorem B.5.1** statement: uniqueness now "on the nonzero-$Y_Q$ branch" (apb-3); B.5 intro/summary/§B.8 summary likewise (apb-1, -2, -13).
- appendix-b **Corollary** to B.5.1: erroneous arithmetic fragment removed (statement unchanged) (apb-4).
- appendix-b **B.6 "link to gauge invariance" and Combined structural result (i), (iii), (v)** (apb-5…8).
- appendix-b **Lemma B.6b.1** proof Step 3 and Consequences (statement unchanged) (apb-9, -10); **Lemma B.6c.1** proof Step 4 and Consequences (statement unchanged) (apb-11, -12).
- glossary definitions: **Anomaly cancellation**, **Gauge group**, **Hypercharge** (gl-1…3).

## Items for coordinator decision

1. nonG-commutant group (ch00-2, ch02-4/23/25/26, ch04-3, gl-2, apb-5/7): the old text identifies SU(3)×SU(2)×U(1) literally with a commutant (Schur: strict commutant of the multiplicity-free cubic action is U(1)^3 — old ch03:74 and old SM:334 say so; commutant of diag(μ_c I3, μ_w I2, 1) is U(3)×U(2)×U(1)). Minimal fix: "as" → "from", or name the correct group (appendix-b defers the SU-reduction to Chapter 5 §5.5). The coordinator can drop these as a group if only G1–G7 count. Consistency: the ch05 minimal (another group) rewrites the amplitude-scale reduction (it removes only the common phase, and the hypercharge direction needs a specified charged matter action). My ch02:102 and ch03:70 keep the old "each block phase stripped by amplitude-scale invariance" sentence as UNCERTAIN, so align them with ch05 if that ch05 edit is accepted. The ch05 G5 wording is "apart from the exceptional branch $Y_Q=0$"; mine is "on the nonzero-$Y_Q$ branch", which is equivalent.
2. nonG-anchor "coupling-degree minimization fixes K=6" (apb-6, apb-9, apb-12, apc-1): contradicts SM §4.5 "Scope of K=2d" and the book's own B.6 paragraph.
3. apb-4: old Corollary contains a false equation and draft text ("… = 2... no, let me reorganize.").
4. rd-1: README describes "Grassmann-valued site variables"; ch05:175 states there are none.
5. Old ch19:224 contains revision-history narration ("The earlier framing of this as … mistook …") that #982 removed; it is not a falsity, so it is kept here, but it conflicts with §A.30.
6. UNCERTAIN, kept old: B.6c Step 4 per-generation anomaly cancellation (false as a general QFT statement); Theorem (Generators) (iv) vs the G_sub definition (same $T_{ij}(t)$); gauge-hierarchy nesting/image claims (ch02 §2.5, ch03 §3.4); missing H-χ'/H-spin' in single summary sentences already conditioned elsewhere in the same chapter.
7. Old ch02 line 106 (unchanged by #982) still says θ "is exactly zero as a consequence of the substratum's structural T-symmetry", which contradicts the preceding sentence ("does not fix θ̄, which is open"). It is outside #982's hunks and left alone.
