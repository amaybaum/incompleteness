# Report — companions group (Methodology, Explainer, Computation, Complexity, Juno, GR, Main)

Minimal files: `min982-work/minimal/papers/<name>.md` = OLD (0d917665) + the N edits below. Everything else in #982's hunks reverted to OLD.

Class key: N = necessary (minimal edit applied); U = unnecessary (reverted to OLD); UNCERTAIN = OLD kept, flagged.


## papers/Main.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 16 | U | G6: embedded-observer opening correct (records inside carrier; pigeonhole; Breuer 1995); replacement relies on Prop. 24.5 — reverted | — |
| 28 | U | G6: §1.1 'permanently hidden' correct for embedded observers — reverted | — |

## papers/GR.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 206 | U | typesetting only (overwide identifier replaced by link); `orientedShellRepresentation_orientation_sensitive` exists in OIBridge/OrientationClosure.lean:184 — reverted | — |
| 346 | N | G3 + Theorem 23 hypothesis list (E1–E7) | «the empirical inputs E1–E4, and the structural assumptions A1–A6)» → «the empirical inputs E1–E7, and the structural assumptions A1–A6, within the nearest-neighbor class)» |
| 346 (rest) | U | rewrite of 'Ontological commitment' beyond the premise fix — reverted | — |
| 446 | N | concrete: SM Theorem 6 takes d=3 as input; SM Theorem 7b ranges only over 3D Bravais lattices; SM §3.2's three d-filters are gravity, stable matter, boundary entropy | «This boundary-entropy filter is one of three independent $d=3$ selectors in the framework: (i) substratum link counting under H-link (SM §4.5, $K = 2dm$ with $m=1$ giving $K=6$; coupling-degree minimization does not establish it); (ii) Bravais-lattice uniqueness for the SM gauge group (SM Theorem 7b); (iii) the present boundary-entropy filter. The three derive $d=3$ from very different physical considerations (substrate dynamics, crystallographic representation theory, cosmological boundary thermodynamics).» → «This boundary-entropy filter is one of three independent $d=3$ selectors in the framework (SM §3.2): (i) propagating gravity ($d \geq 3$); (ii) stable matter ($d \leq 3$); (iii) the present boundary-entropy filter. The three converge on $d=3$ from very different physical considerations (gravitational dynamics, atomic and orbital stability, cosmological boundary thermodynamics).» |

## papers/Juno.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 6, 12 | U | `---`→`***` stylistic; old file renders correctly under pandoc (checked) — reverted | — |
| 88 | N | G3 (nearest-neighbour premise of Theorem 7b) | «SC is the unique 3D Bravais lattice compatible with the SM gauge group at the commutant level» → «SC is the unique 3D Bravais lattice whose nearest-neighbor link representation is compatible with the SM gauge group at the commutant level» |
| 88 | N | G5 (Theorem 15 hypercharge uniqueness) | «(anomaly cancellation fixing hypercharges uniquely)» → «(anomaly cancellation fixing hypercharges up to normalization on the branch with nonzero quark-doublet hypercharge)» |
| 88 (rest) | U | rest of sentence unchanged | — |
| 104 | N | G3 | «under the commutant construction of [18, §4.6 Theorem 7b]» → «under the nearest-neighbor commutant construction of [18, §4.6 Theorem 7b]» |
| 106 | U | (a) crystallographic irrep-degree argument is correct as stated — reverted | — |
| 110–116 | UNCERTAIN | table header 'Gauge group (commutant)' with SU(3)×SU(2)×U(1) vs exact commutant U(3)×U(2)×U(1): mirrors SM Theorem 7b table; depends on SM group's decision about the U(n)→SU(n) reduction (not a G-item) — OLD kept | — |
| 118 | N | G3 | «the observed Cabibbo angle among all 14 three-dimensional Bravais lattices.» → «the observed Cabibbo angle among all 14 three-dimensional Bravais lattices under nearest-neighbor coupling.» |
| 255–257 | U | Layer-0/1/2(a) definitions are classification definitions, not refuted by G1–G7 — reverted | — |

## papers/Computation.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 9,19,33,43,88,114,134,146,212,226,266,292 | U | `---`→`***` stylistic — reverted | — |
| 13 | U | abstract already states cubic lattice empirically anchored — reverted | — |
| 68 | U | 'reconstruct the local lattice/gauge invariants fixed by Theorem 23' is correct under Theorem 23's conditions — reverted | — |
| 70, 72, 86 | U | G6 embedded-observer limits (cannot determine h; permanent floor) — reverted | — |
| 78 | U | table row 'Structurally possible under Theorem 23's conditions' correct — reverted | — |
| 80 | N | concrete misattribution: Main's characterization theorem ((ii)⇔(iii)) contains no impossibility of determining h; the retained embedded-observer bound is T. Breuer 1995 (G6) | «\| Determine the hidden-sector state $h$ \| Provably impossible (characterization theorem) \|» → «\| Determine the hidden-sector state $h$ \| Provably impossible (T. Breuer 1995) \|» |
| 120 | N | G1/G2: Theorem 24 does not classify (completeness open) and concerns transformations of (S,φ), not the actual microstate | «; independently, Theorem 24 of [Substratum §4] classifies the specific microstate as gauge, provably without empirical content, whereas extractable task answers would be empirical content. What remains» → «. What remains» |
| 184 | U | G6 (hidden-sector inaccessibility as boundary result) — reverted | — |
| 258 | U | §7.3 lists generators with 'includes' (no exhaustiveness claim); speculative-hedged — reverted | — |

## papers/Complexity.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 9,19,31,111,154,190,292,340,398,533,539 | U | `---`→`***` stylistic — reverted | — |
| 13 | U | abstract consistent with SM's own cubic-commitment statement — reverted | — |
| 27 | UNCERTAIN | 'determines the Standard Model's complete structure [2]' is loose but not a G-item; OLD kept | — |
| 119 | U | conditional on the framework fixing structure — reverted | — |
| 198 | U | uses only soundness (invariance under generators) — G7-type; reverted | — |
| 202 | N | G3 (premises of Theorem 23 incl. nearest-neighbour) | «the structure is the only structure consistent with embedded observation (characterization theorem» → «the structure is the only structure consistent with embedded observation under the reconstruction theorem's stated inputs, within the nearest-neighbor class (characterization theorem» |
| 206 | N | G1 (completeness open; Lemma 24.1 false) | «The completeness of $\mathcal{G}_{\text{sub}}$ [33, Theorem 24] closes this argument conditionally: the four generator families exhaust all observables-preserving transformations conditional on Lemma 24.1's semigroup-transfer step (the standard Stinespring/GNS uniqueness extended to the discrete unitary-generated semigroup, identified in [33, §4] for specialist verification). No finer distinction between substrata is empirically accessible. The structural preconditions for complexity are therefore as immutable» → «The completeness of $\mathcal{G}_{\text{sub}}$ [33, Theorem 24] would close this argument; whether the four generator families exhaust all observables-preserving transformations is open [33, §4]. The structural preconditions for complexity are as immutable» |
| 298 | N | G3 (premise) | «The reconstruction theorem [33, §3] establishes:» → «The reconstruction theorem [33, §3] establishes, under its stated inputs within the nearest-neighbor class:» |
| 300, 302 | UNCERTAIN | display 'Observed physics ↔ [(S,φ)]/∼' kept; following text uses only existence. Coordinator may want '↔' narrowed if Theorem 23's uniqueness clause is removed | — |
| 312 | U | 'fixes the local lattice/gauge residue ... under its stated inputs' — correct with Theorem 23's premises — reverted | — |
| 314 | N | G3/G1 (drop 'up to the stated gauge freedoms'; add premise) | «the structural inputs select one local lattice/gauge residue up to the stated gauge freedoms.» → «the structural inputs, within the nearest-neighbor class, select one local lattice/gauge residue.» |

## papers/Explainer.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 74, 76, 78 | U | G6 embedded-observer / horizon inaccessibility; replacement relies on Prop. 24.5 — reverted | — |
| 605–629 | U | G6 / philosophical comparisons (claims list, Gödel, Wolpert, Breuer, Hofstadter, Cusa) — reverted | — |
| 637, 647, 655 | U | philosophical lineage; G6 — reverted | — |
| 662 | N | concrete: Main §3.4 Remark 'representability, not selection of the relating evolution' and Main §5 'narrower than an unqualified claim that C1–C4 uniquely generate operational QM' | « from non-quantum premises and proves the derivation is the only possible one.» → « from non-quantum premises.» |
| 662 (rest) | U | remainder of FAQ answer unchanged | — |
| 668 | U | G6 (randomness from ignorance of hidden sector) — reverted | — |
| 684 | UNCERTAIN | 'SM gauge group is forced uniquely from cubic-group representation theory in the framework's account' omits H-link/H-cust (pre-#982 issue, not a G-item) — OLD kept | — |
| 686, 691–692 | U | hedged comparison / philosophical FAQ — reverted | — |
| 735 | N | same as Expl-663 (no uniqueness of the reconstruction) | «the characterization theorem dictates the unique form of the resulting reconstruction.» → «the characterization theorem dictates the form of the resulting reconstruction.» |
| 745 | N | same as Expl-663 | « Its artifacts are our physics. And the characterization theorem proves that no other reconstruction is possible — this is the unique algorithm, and its artifacts are the unique artifacts. Quantum mechanics is not one possible decompression of incomplete cosmological data. It is the only one.» → « Its artifacts are our physics.» |
| 826 | U | uses only the true direction of SM Thm 3 (center terms vanish ⇒ chirality); G4 concerns the converse — reverted | — |
| 830–842 | U | Schur decomposition of an O-equivariant M on 6=T1⊕E⊕A1 is correct; commutant U(3)×U(2)×U(1) ⊃ SU(3)×SU(2)×U(1) correct; not a G-item — reverted | — |
| 854 | N | G5 | «and anomaly cancellation uniquely determines the hypercharge assignments.» → «and anomaly cancellation determines the hypercharge assignments uniquely up to normalization on the branch with nonzero quark-doublet hypercharge.» |
| 856 | N | G5 + concrete (anomaly cancellation does not determine the matter content; SM Theorem 15 fixes charges for given content) | «Anomaly cancellation with SU(3) × SU(2) × U(1) uniquely determines the matter content per generation: Q$_L$, u$_R$, d$_R$, L$_L$, e$_R$ with specific hypercharges. The lattice gives the gauge group and the generation count; the observer's self-consistency gives the representations.» → «For the matter content per generation Q$_L$, u$_R$, d$_R$, L$_L$, e$_R$, anomaly cancellation with SU(3) × SU(2) × U(1) determines specific hypercharges, unique up to normalization on the branch with nonzero Q$_L$ hypercharge. The lattice gives the gauge group and the generation count; the observer's self-consistency constrains the representations.» |
| 858 | U | not a G-item — reverted | — |
| 898 | UNCERTAIN | 'C3 means ... store the full interaction history' paraphrases Main's C3 (log|C_H| ≥ I*) loosely; OLD kept | — |
| 900, 902 | U | not refuted — reverted | — |
| 942, 944, 948 | U | G6 — reverted | — |
| 946 | U | G7 (decoupled deep sector gauge) — reverted | — |
| 968 | N | G1/G3 (drop 'modulo gauge') | «with the reconstruction theorem fixing the local lattice/gauge structural residue modulo gauge;» → «with the reconstruction theorem fixing the local lattice/gauge structural residue;» |
| 970 | N | G1/G3 (drop 'up to substratum gauge'; add nearest-neighbour premise) | «Starting from the observed physics and the theorem's structural inputs, the reconstruction fixes the **local lattice/gauge residue** up to substratum gauge.» → «Starting from the observed physics and the theorem's structural inputs, within the nearest-neighbor class, the reconstruction fixes the **local lattice/gauge residue**.» |
| 972, 982, 984, 986, 988 | U | not dependent on G1–G7 refuted content — reverted | — |
| 974 | N | G3 | «it's the unique dynamics consistent with QM emergence, isotropy, and linearity.» → «it's the unique nearest-neighbor dynamics consistent with QM emergence, isotropy, and linearity.» |
| 976 | N | G1 (unique G_sub class needs completeness) | «the observed inputs determine a unique **local-sector equivalence class** — the lattice/gauge data pinned up to the substratum gauge group $\mathcal{G}_{\text{sub}}$ [Substratum §4]. The Bell preparation rule is extra composite data: H-Bell conditions its compatibility/existence, and its uniqueness is open. This gauge group has four generators: state relabeling (permuting the elements of S while conjugating φ),» → «the observed inputs determine the **local-sector** lattice/gauge data. The Bell preparation rule is extra composite data: H-Bell conditions its compatibility/existence, and its uniqueness is open. The substratum gauge group $\mathcal{G}_{\text{sub}}$ [Substratum §4] contains four generator families: state relabeling (permuting the hidden states uniformly in every visible fibre while conjugating φ),» |
| 976 | N | G1 (Stinespring/Lemma 24.1 completeness route fails) | «The reconstruction theorem establishes this list for the state-channel content via Stinespring uniqueness;» → «Whether this list is complete is open [Substratum §4];» |
| 978 | N | G1 | «the local reconstruction determines its lattice/gauge residue modulo the OI gauge freedoms — not a unique representative» → «the local reconstruction determines its lattice/gauge residue — not a unique representative» |
| 980 | N | G1/G3 | «determine each other up to gauge under the reconstruction theorem's stated conditions;» → «determine each other under the reconstruction theorem's stated conditions;» |

## papers/Methodology.md

| old line | class | reason | old → minimal |
|---|---|---|---|
| 9,15,47,93,116,168,237,285,307,319,481,575,581 | U | `---`→`***` stylistic; old renders correctly — reverted | — |
| 13 | N | G1 | «; the residual gauge freedom of the reconstructed dilation/local datum is explicitly classified conditional on Lemma 24.1's completeness step.» → «; the residual gauge freedom of the reconstructed dilation/local datum is explicitly exhibited, with the completeness of its classification open.» |
| 33 | N | G1 | «and the residual gauge freedom of the reconstructed dilation/local datum is explicitly classified conditional on Lemma 24.1's completeness step.» → «and the residual gauge freedom of the reconstructed dilation/local datum is explicitly exhibited, with the completeness of its classification open.» |
| 43 | U | §1.3 status paragraph; label 'gauge-classification theorem' kept as a name — reverted | — |
| 283 | N | G1 | «the framework's gauge structure is constructively classified and its selection principle» → «the framework's gauge structure is constructively exhibited, with its classification's completeness open, and its selection principle» |
| 323 | U | Part II italic intro: label use only — reverted | — |
| 333 | N | G1 | «is exhibited and classified, exhaustively conditional on Lemma 24.1's completeness step.» → «is exhibited and classified, with exhaustiveness open.» |
| 335, 349 | U | section headings kept (residue uniqueness = Lemma 23.0 invariants; label) | — |
| 337 | N | G1/G3 (drop gauge clause) | «answers that this residue is unique — under the stated conditions — up to the gauge equivalence classified next.» → «answers that this residue is unique under the stated conditions.» |
| 339 | N | G1 (drop Lemma 24.1) + G3 (nearest-neighbour premise; drop gauge clause) | «the C2 mixing hypothesis and Lemma 24.1's completeness step, the **local propagating lattice/gauge residue** is uniquely fixed up to the stated substratum-gauge freedoms.» → «the C2 mixing hypothesis and the nearest-neighbor premise, the **local propagating lattice/gauge residue** is uniquely fixed.» |
| 343 | N | G1/G3 | «back out* to a unique **local structural residue** modulo the classified gauge directions.» → «back out* to a unique **local structural residue**.» |
| 345 | N | G3 (premise beyond A1–A6) | «The uniqueness is uniqueness *within* the A1–A6 class.» → «The uniqueness is uniqueness *within* the A1–A6 class with nearest-neighbor dynamics.» |
| 347 | U | finite-data scope paragraph correct — reverted | — |
| 351 | N | G1 | «The framework's second theorem supplies this: it classifies the gauge group $\mathcal{G}_{\text{sub}}$ — the transformations relating distinct constructions that produce identical observables — into an explicit list, exhaustive conditional on the semigroup-transfer completeness step (Substratum Lemma 24.1, identified there for specialist verification).» → «The framework's second theorem supplies part of this: it exhibits generators of the gauge group $\mathcal{G}_{\text{sub}}$ — the transformations relating distinct constructions that produce identical observables — as an explicit list, whose exhaustiveness is open.» |
| 353 | N | G1 ('generated by' asserts completeness) | «the substratum gauge group $\mathcal{G}_{\text{sub}}$ is generated by four families of transformations.» → «the substratum gauge group $\mathcal{G}_{\text{sub}}$ contains four families of transformations.» |
| 353 | N | G2 | «*State relabeling* — conjugating the bijection by any permutation of the configuration space; transition probabilities depend on the coupling structure, not on the labels, and this family alone» → «*State relabeling* — conjugating the bijection by a permutation of the hidden states applied uniformly in every visible fibre, which preserves every channel (a fibre-dependent hidden relabeling preserves the transition probabilities but not coherent channels in general); this family alone» |
| 355 | N | G1 | «The decisive word is *exhaustive*. The framework does not merely list four families it has noticed; it argues their completeness. For the state-channel generators (state relabeling and deep-sector enlargement) the argument is routed through the uniqueness clause of Stinespring's dilation theorem: two dilations of the same visible-sector channel differ only by hidden-sector transformations of exactly the kinds those families enumerate — extended to the full channel family per the semigroup-transfer step (Substratum Lemma 24.1), on which the classification's completeness is conditional.» → «The decisive word is *exhaustive*, and exhaustiveness is open. For the state-channel generators (state relabeling and deep-sector enlargement) the uniqueness clause of Stinespring's dilation theorem relates two dilations of the same visible-sector channel by a hidden-sector transformation, but equality of the full visible channel family does not extend this to a single conjugation of the generated dynamics (Substratum §4), so the classification's completeness is open.» |
| 355 | N | G1 | « The surplus is not just exhibited; it is closed conditional on the semigroup-transfer completeness step (Substratum Lemma 24.1) — and would be closed outright once that lemma is verified.» → « The surplus is exhibited; whether it is closed is open.» |
| 357 | N | G1 | «That a gauge freedom can be exhibited and bounded is worth contrasting» → «That a gauge freedom can be exhibited is worth contrasting» |
| 357 | N | G1 | «the gauge-classification theorem is what the finiteness buys: the analogue of "which representation" is "which representative within the equivalence class," and that question is not left as an open interpretive choice but answered by a classification exhaustive conditional on the semigroup-transfer completeness step (Substratum Lemma 24.1).» → «the gauge-classification theorem is what the finiteness buys: the analogue of "which representation" is "which representative within the equivalence class," and that question is not left as an open interpretive choice but posed as a finite classification, whose completeness is open.» |
| 357 | N | G1 | «a classification that becomes closed once the semigroup-transfer completeness step is verified, where» → «a finite classification problem, where» |
| 359 | N | G1 | «and *here*, in four enumerated families — complete conditional on Lemma 24.1's semigroup-transfer step — is exactly the surplus. The two theorems together leave, in the position's promissory note, exactly one named item: that completeness lemma, identified for specialist verification. What is real is the equivalence class; what is gauge is the four-family freedom;» → «and *here*, in four enumerated families — whose completeness is open — is the exhibited surplus. The two theorems together leave, in the position's promissory note, exactly one named item: that completeness question. What is real is the equivalence class; what is gauge includes the four-family freedom;» |
| 365 | N | G1 | «It can exhibit the local residue, bound its gauge surplus by the four-family classification (conditional on the completeness step), and state exactly where the result stops.» → «It can exhibit the local residue, exhibit its gauge surplus through the four-family generators (whose completeness is open), and state exactly where the result stops.» |
| 367 | N | G3 (premise beyond A1–A6) | «Second, the constructive-OSR claim is conditional on the structural assumptions A1–A6, which are not themselves derived; the claim is "constructive OSR within the A1–A6 class,"» → «Second, the constructive-OSR claim is conditional on the structural assumptions A1–A6 and the nearest-neighbor premise, which are not themselves derived; the claim is "constructive OSR within the nearest-neighbor A1–A6 class,"» |
| 369 | N | G1/G3 + old §10's own statement that Bell-inclusive full-substratum uniqueness is not established | «but of a complete substratum-equivalence-class from which» → «but of a local substratum-equivalence-class from which» |
| 425 | N | G1 | «Part II found that the structure consistent with the empirical inputs is unique, but only up to a gauge equivalence — and that the gauge freedom is not noise to be discarded but a four-family group exactly classified conditional on the semigroup-transfer completeness step, the precise specification of which differences between descriptions are differences that make no difference.» → «Part II found that the structure consistent with the empirical inputs has a unique local residue — and that the gauge freedom is not noise to be discarded but a four-family group, whose exhaustiveness is open, specifying differences between descriptions that make no difference.» |
| 427 | N | G1 | «that the gauge freedom Part II classifies is not gauge after all but conceals a genuine further fact. The reconstruction and gauge-classification theorems say there is no such further fact: the equivalence class is fixed by the evidence, and within it the choice» → «that the gauge freedom Part II exhibits is not gauge after all but conceals a genuine further fact. The reconstruction and gauge-classification theorems say there is no such further fact: within the equivalence class the choice» |
| 433 | N | G1 | «the gauge-classification theorem gives its representatives by enumerating the relevant transformations.» → «the gauge-classification theorem gives its representatives by enumerating the relevant transformations, whose completeness is open.» |
| 433 | N | G1 | «asks for exactly the two things the framework's theorems deliver.» → «asks for exactly the two things the framework's theorems address.» |
| 435 | U | statement of the proposed posture — reverted | — |
| 437 | N | G1 | «when the gauge group is *exhaustively classified* — conditionally, per Part II's completeness step — as in Part II, the freedom» → «when the gauge group is *exhaustively classified* — which Part II leaves open — the freedom» |
| 439 | N | G1/G3 (drop gauge clause) | «determine each other up to the stated gauge freedoms under the theorem's assumptions.» → «determine each other under the theorem's assumptions.» |
| 441 | U | Tegmark selection remark relies on C1–C4 characterization, not completeness — reverted | — |
| 453 | N | G1 (step two requires an exhaustiveness proof; step three's certification rests on it) | «a case where the three steps have been carried out, with» → «a case where the three steps have been carried out up to the open exhaustiveness of step two's classification, on which step three's certification also rests, with» |
| 455 | N | G1 | «in which the three steps are carried out and the realism question» → «in which the three steps are carried out, up to that open exhaustiveness, and the realism question» |
| 461, 463 | U | G6 (embedded observer cannot fully resolve the system; relabelings in G_sub are surplus) — reverted | — |
| 467 | N | G2 (arbitrary relabelling not observables-preserving at a fixed interface) | «the labels on substratum states,» → «the labels on hidden substratum states,» |
| 469 | UNCERTAIN | 'to compute that future the observer would need to be a system at least as large as the whole' — not a G-item; OLD kept | — |
| 473 | N | G1 | «the substratum gauge group, classified by the gauge-classification theorem, with the equivalence class taken as what is real — is interpretational surplus, unambiguously: the theorem classifies transformations that preserve every observable.» → «the substratum gauge group, exhibited by the gauge-classification theorem, with the equivalence class taken as what is real — is interpretational surplus, unambiguously: the theorem exhibits transformations that preserve every observable.» |
| 477, 479 | U | Deutsch comparison uses soundness only — reverted | — |
| 485 | N | G1 | «given the substratum gauge group classified by Part II,» → «given the substratum gauge group exhibited by Part II,» |
| 489 | N | G1 | «and the gauge group classified by the gauge-classification theorem,» → «and the gauge group exhibited by the gauge-classification theorem,» |
| 497, 503, 505 | U | no-go status/examples not refuted — reverted | — |
| 499 | N | G1 | «denote the substratum gauge group classified in Part II (the group» → «denote the substratum gauge group of Part II (the group» |
| 501 | N | G1 (the proof needs only the definition of G_sub, not a completed classification) | «The proof is short. By the gauge-classification theorem (Part II), the equivalence class» → «The proof is short. By the definition of $\mathcal{G}_{\text{sub}}$, the equivalence class» |
| 507 | U | the invariant-computability converse (see note) — reverted | — |
| 529, 531, 539, 541, 543, 547 | U | Part V unification/audit paragraphs not refuted — reverted | — |
| 569 | N | G1 | «and its relevant gauge freedom is exhibited and shown exhaustively classified conditional on the completeness step;» → «and its relevant gauge freedom is exhibited, with exhaustive classification open;» |
| 571 | U | label use only — reverted | — |

## Notes

**Methodology §22 invariant-computability converse (old line 507).** Asserted: “Quantities that *are* $\mathcal{G}_{\text{sub}}$-invariant — the equivalence-class invariants — are determined by substrate computation … These are not bijection-specific; the substrate determines them.” Under §22's own definitions (a substrate-only computation is any procedure operating on one representative and producing a number; an invariant quantity takes the same value on every representative; the configuration space is finite) the converse is immediate: evaluating the quantity on any representative determines it, and algorithmic computability is not at issue on a finite set. It is therefore not unsupported; #982's retraction is U and the OLD text is kept. The no-go proof itself (old 501) needs only the definition of $\mathcal{G}_{\text{sub}}$ as the observable-preserving group, so the minimal fix replaces the appeal to “the gauge-classification theorem” by “the definition of $\mathcal{G}_{\text{sub}}$” and “classified in Part II” by “of Part II”; #982's “conditional” restatement is U.

**Theorem 23 dependents.** Following G3, only “up to (the stated) gauge / modulo gauge” clauses and Lemma 24.1 conditions were removed; “unique local residue” wording was kept where it concerns the residue's invariants (supported by Lemma 23.0's “same Stage-2 invariants”). The nearest-neighbor premise was inserted only where a sentence lists the premises explicitly or states the reconstruction with no premise; sentences saying “under Theorem 23's stated conditions” are left as is, since those conditions include it once Theorem 23 is fixed.

**Non-G concrete fixes (coordinator may veto):** GR 346 (E1–E4 → E1–E7: Theorem 23's hypotheses list E1–E7, and d=3 needs E5/E6); GR 446 (SM Theorem 6 says “for the selected spatial dimension d=3”, SM Theorem 7b ranges over “all 14 three-dimensional Bravais lattices”, so neither selects d; SM §3.2/line 30 names the three filters as gravity, stable matter, boundary entropy); Explainer 662/735/745 (uniqueness of the quantum reconstruction contradicts Main §3.4 Remark “scope: representability, not selection of the relating evolution” and Main §5 “narrower than an unqualified claim that C1–C4 uniquely generate operational quantum mechanics”); Explainer 856 (anomaly cancellation does not determine the matter content; SM Thm 15 fixes the charges of a given content); Computation 80 (attribution: the characterization theorem is (ii)⇔(iii); the retained embedded-observer bound is T. Breuer 1995); Computation 120 (Theorem 24 concerns transformations of (S,φ), not the actual microstate, and does not classify); Methodology 369 (“complete substratum-equivalence-class” contradicts old §10: “No theorem here establishes Bell-inclusive full-substratum uniqueness”).

**Kept but possibly affected by the Substratum group's choices:** Methodology 355 “Candidate fifth families — time reversal, hidden-sector dynamical reparametrization — are shown to be already contained in the four” (with relabeling narrowed to uniform hidden permutations, containment of time reversal may need re-checking against minimal Substratum).

## Statements whose text differs OLD vs MINIMAL (ledger)

- Methodology §22, the gauge-invariance no-go (prose theorem): set-up sentence “$\mathcal{G}_{\text{sub}}$ … classified in Part II” → “… of Part II”; proof step “By the gauge-classification theorem (Part II)” → “By the definition of $\mathcal{G}_{\text{sub}}$”. The statement's content (no substrate-only computation determines a bijection-specific quantity) is unchanged.
- No numbered theorem/proposition/lemma/corollary/definition statement in Main, GR, Juno, Computation, Complexity or Explainer changed. Citations of SM Theorem 7b (Juno 88, 104, 118) and SM Theorem 15 (Juno 88; Explainer 854, 856) now carry the nearest-neighbor premise and the nonzero-$Q$-branch qualification respectively and must match the SM group's minimal wording.
