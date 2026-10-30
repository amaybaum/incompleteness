# Group sm — papers/SM.md, book/ch05-gauge-structure.md, book/ch06-matter-content.md

Minimal files: `min982-work/minimal/papers/SM.md`, `min982-work/minimal/book/ch05-gauge-structure.md`,
`min982-work/minimal/book/ch06-matter-content.md` (= OLD + the N edits below, applied by exact unique-string replacement).

Counts (word-diff line hunks): SM 56 hunks — N 25 / U 21 / UNCERTAIN 10; ch05 28 — N 17 / U 8 / UNCERTAIN 3; ch06 4 — N 3 / U 0 / UNCERTAIN 1.

Decisions on the #982 additions: **Proposition 14a, Proposition 15a, Corollary 15b, the compact-charge strengthening, the Yukawa-route paragraph, the new Theorem 15 proof, the Theorem 14 rewrite, refs [43]–[45] and the "Physical scope of the quotient" / central-directions remarks are all reverted (U).** No OLD statement needs them. The OLD statements that are false are fixed in place: the global identity U(n)=SU(n)×U(1) and the "U(n)/U(1) → SU(n)" per-block amplitude-scale reduction; a premise is added to every OLD reduction statement ("a specified charged matter action"); and the hypercharge uniqueness gets the Y_Q≠0 qualifier. The global form SU(3)×SU(2)×U(1) used as the name of the gauge group is kept. It is not shown false: SU(3)×SU(2)×U(1) embeds faithfully in U(3)×U(2)×U(1), for example with hypercharge circle (z^a I3, z^b I2, z).

## SM.md

| hunk (old line) | class | reason |
|---|---|---|
| 14 abstract | N (partial) | "compatible with an observed SU(3) factor" is false: Theorem 7b's own table gives BCC SU(3)²×U(1)² and FCC SU(3)³×…, which both contain SU(3). Insert the NN premise (G3). The rest of the hunk (equivalence-class wording, Lie-algebra/Prop 14a wording, tier text) is U. |
| 30 Tier 1 | U | rewording; the equivalence class is still defined with the narrowed G_sub |
| 56 §1 scope | N (partial) | "forced by the observed SU(3) factor" is false for the same reason → "observed gauge group"; the rest is U |
| 300 Thm 3 statement | N | G4: the iff fails for operator coefficients. Add the exact Lean premises (site-independent coefficients mε+p0, no additive 2-torsion, both parity sectors) = `scalar_center_chiral_iff` |
| 302 Thm 3 proof | N | the old proof has no chirality ⇒ center-independence step; one sentence added (anticommutator 2m+2p0ε, two sectors, no 2-torsion) with the kernel citation |
| 304 Remark scope | U | old remark is correct; #982 extension (even perturbations) is new material |
| 306 Revised chain / new remark | U | old text correct under the restricted theorem; ring/q-parity remark is new material (premise now in statement) |
| 342 Thm 5 scope | N | the old text says the U(3)×U(2)×U(1)→SM reduction "carries" the amplitude-scale/background-independence premises. Amplitude normalization removes only the common phase (audit `theorem-recovery-20261028/gauge-global-form/native_carrier_barrier_v1.txt`), so a premise is missing: add "and a specified charged matter action" |
| 372 Thm 7 scope | N | same missing premise; the "Physical scope" header is U |
| 376 M eigenspaces | N | "fixes the multiplicities of M's eigenspaces" contradicts the theorem's own proof ("the coupling matrix itself is scalar"): a scalar M has a single eigenspace. → "fixes the block multiplicities" |
| 386 O(3) aside | UNCERTAIN | "(3,3) under O(3)" is ill-defined but not shown false; kept |
| 388 Thm 7b | N | G3: add the NN premise ("on the nearest-neighbor link representation"); #982's restatement is otherwise U |
| 392–400 table/text | U | SU→U relabelling of the table and the added discussion; the old conclusion "neither matches" stands |
| 412 | U | rewording |
| 414 extension | N | (a) "SC is the unique candidate compatible with an SU(3) gauge factor" is false (BCC/FCC have SU(3)). The true content of the paragraph is that no non-cubic lattice gives SU(3); minimal restatement of the bold claim. (b) "finite subgroups of O(3) only by S4≅O" is false, since O_h⊂O(3) has degrees {1,2,3} → SO(3) |
| 426 layer-split remark | N | "the SM gauge group … is the commutant (stabilizer) of Σ" is false: the stabilizer is U(3)×U(2)×U(1) (Theorem 5) → "descends from the commutant (stabilizer) U(3)×U(2)×U(1)"; the rest of the #982 rewrite is U |
| 454 Thm 10 statement | N | G5: "apart from the exceptional branch Y_Q=0" |
| 458 Thm 10 proof | N | G5 (two sites) |
| 472 fermion-sector claim | N (partial) | G5 qualifier. The claim that the hypercharges follow from placing matter in V_K⊗V_K* is false without a charged action: the singlet sector of the native carrier is neutral and has no charged e_R (audit barrier file), so the same premise is added. "Forced by first principles" etc. are kept (UNCERTAIN, see notes) |
| 483 heading | U | |
| 491 off-block Homs | UNCERTAIN | "retrodicts … cleanly … nothing else": the old text lists the block singlets; overstated but not concretely false; kept |
| 509 | N (one token) | "the commutant SU(3)×SU(2)×U(1)" is false; the commutant is U(3)×U(2)×U(1). The rest is U |
| 513, 515, 519 | U | rewording |
| 523 V3⊗V2 ⊂ V_K⊗V_K* | UNCERTAIN | strictly V3⊗V2*, but isomorphic under SU(2); kept |
| 525 Step 2 | N | G5 and family premise: "fermions in fundamental or singlet representations" admits e.g. a charged ν_R (a second anomaly-free direction) → "each family … in the five … representations of Theorem 15", "apart from the exceptional branch Y_Q=0" |
| 527 closure | N | G5 (two sites). "Every SM multiplet has a carrier" is false for e_R=(1,1)_{−1}: the native V_K⊗V_K* singlets are neutral (audit barrier file) → "a carrier for its non-abelian representation" |
| 531 | N | "both close … forced by theorems" contradicts 527's own open items and the e_R gap → "both close at the level of non-abelian representation availability" |
| 553 | U | already "uniquely in the sense stated there" |
| 565, 567 Nielsen–Ninomiya | UNCERTAIN | the old text already marks the effective-construction question open; "bypassed" overstated, not shown false; kept |
| 573 Thm 14 statement + Prop 14a + scope + remark | U | new propositions not required |
| 575 Thm 14 proof | N | "U(n_i)=SU(n_i)×U(1)_i" is false globally (U(n)≅(SU(n)×U(1))/Z_n) → Lie-algebra form + "G is locally". "Exactly one free parameter / exactly one anomaly-free U(1)" → G5 qualifier |
| 577 Remark (two non-gauge U(1)s) | UNCERTAIN | depends on the charged action; not shown false; kept |
| 579 Thm 15 | N | G5 + family premise (see 525). The OLD statement is kept, with "each family … five representations … family-universal charges" and "apart from the exceptional branch Y_Q=Y_L=Y_e=0, Y_u=−Y_d". The new proof, compact-charge and Yukawa paragraphs are U |
| 583 Corollary → Prop 15a, Cor 15b | U | the old corollary holds on the Y_Q≠0 branch now in Theorem 15 |
| 775 | UNCERTAIN | "properties of the equivalence class vs particular φ": see note (b) |
| 795 | N (one token) | "Q=T³+Y/2" contradicts the paper's normalization (Y_Q=1/6; Theorem 15 uses Q=T₃+Y) → "T³+Y" |
| 807 Layer A | N (partial) | "three eigenspaces of the coupling matrix M": M is scalar (Thm 7 proof) → "condensate Σ"; the GUT-stage rewrite is U |
| 1090 | U | trailing space |
| 1354 OSR | N | "What the framework proves is that (S,φ) is a complete description … up to gauge equivalence (the reconstruction theorem)" rests on completeness of G_sub (G1/G3/G7) → "proposes … ; the completeness of the generators of that gauge equivalence is open [Substratum §4]" |
| 1356 | U | phrased as an assertion of the paper's claim; consistent after 1354 |
| 1378 structural predictions | N (partial) | G5 qualifier on "unique hypercharges"; the rest is U/UNCERTAIN (note b) |
| 1380, 1384, 1420 | UNCERTAIN | equivalence-class/representative framing (note b) and "hold for every bijection"; kept |
| 1386, 1390 | U | |
| 1408 Tier 2 | N (partial) | "Theorem 7b selects it *because* an SU(3) factor is observed" is false (BCC/FCC) → "because SU(3)×SU(2)×U(1) is observed"; the rest is U |
| 1416 Proposition | N (partial) | G5: the hypercharge assignment is a "function of (C,T)" only off the exceptional branch |
| 1572 conclusion | U | already lists the flagged inputs |
| 1744 refs [43]–[45] | U | only cited by reverted material |

## ch05-gauge-structure.md

| hunk (old line) | class | reason |
|---|---|---|
| 11 | N | G3: remove "uniquely … up to the stated G_sub freedoms"; add the NN premise |
| 13 | U | |
| 17 | N | "later U→SU reduction carrying amplitude-scale gauge as before" names the false reduction → "later reduction to SU(3)×SU(2)×U(1) carrying amplitude-scale gauge and a specified charged matter action" |
| 19 | N | G3: NN premise inserted ("uniquely fixed" kept, consistent with the Substratum minimal Lemma 23.0 within the NN class) |
| 43 | U | |
| 45 | N | "the overall U(1) phase of each block can be absorbed into a global rescaling … gauge by amplitude-scale invariance" is false: one global rescaling removes only the common phase. The last sentence ("what remains … after gauge d.o.f. stripped") is false because the other phases are not gauge redundancies; it is removed. → common phase only; hypercharge direction selected by a charged matter action and anomaly cancellation (§5.6, already in the OLD chapter) |
| 73, 75, 77 | U | d=3 stays derived (G3) |
| 95 | N | mirror of SM Thm 3 (G4): premise inserted |
| 101 | N | "stabilizer [of Σ] decomposes … one on each eigenspace of M" contradicts the same paragraph (M scalar) → Σ |
| 125 | N | false group reduction (per-block phases; U(n)→SU(n)) → Lie-algebra split, global identity, common phase by amplitude scale, hypercharge by charged action + anomaly (§5.6) |
| 127 | N (delete) | "U(3)=SU(3)×U(1)_color", "U(2)=SU(2)×U(1)_weak" and the per-block amplitude-scale gauge are false; the paragraph is removed |
| 129–131 | N (minimal) | "After the amplitude-scale reduction" → "After this reduction"; the premise list gains "the charged matter action". The A1→U(1)_Y identification is kept; it mirrors SM's "proposed" identification |
| 133 | N | G3: "on the nearest-neighbor link representation" |
| 135 | U | |
| 139 | N (one word) | "The commutant SU(3)×SU(2)×U(1)" → "The group …" (the commutant is U(3)×U(2)×U(1)) |
| 141, 143 | U | |
| 145 | N | "amplitude-scale-invariance argument reduces U(n) to SU(n)" is false → amplitude scale + charged action + anomaly reduce the abelian directions |
| 175, 177 | UNCERTAIN | NN wording, as SM 565/567 |
| 181 | UNCERTAIN | "structural commitments fix the SU(3)×SU(2) representations" overstates (SM 527 says selection is open); kept, flagged |
| 183 | N | G5 + dependent clause ("that reduced U(n) to SU(n)" → "that removes the common phase"). "Normalization fixed by amplitude scale" is kept (UNCERTAIN) |
| 186 | N | G5 |
| 188 | N | arithmetic error "q_e = Y_e + (−1/2)·2 = −1" (= −2) → "q_e = Y_e = −1" |
| 192 | N | false reduction (as 145) + G5 |
| 194 | N | missing premise + G5 ("not chosen from a continuum": the exceptional branch is a continuum) |

## ch06-matter-content.md

| hunk | class | reason |
|---|---|---|
| 8 | N | dependent on the false reduction (amplitude-scale → + charged action + anomaly); G5; qualifier gains the charged-action premise. "forced — uniquely —" kept |
| 44 | N | G5 qualifier on "unique anomaly-free hypercharge assignment" |
| 48 | UNCERTAIN | Higgs mass "depending on the specific representative within the gauge class" (note b); kept |
| 98 | N (partial) | "three eigenspaces of the coupling matrix M" → condensate Σ (M scalar); the GUT rewrite is U |

## Exact old → minimal text of every N edit

### papers/SM.md
| site | old | minimal |
|---|---|---|
| 14 abstract Bravais | «simple cubic is selected as the one compatible with an observed $\mathrm{SU}(3)$ factor (only» | «simple cubic is selected, under the nearest-neighbor commutant construction, as the one compatible with the observed $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ (only» |
| 56 Bravais type | «The cubic Bravais type is an empirically-selected input, forced by the observed $\mathrm{SU}(3)$ factor (§8.3).» | «The cubic Bravais type is an empirically-selected input, forced by the observed gauge group (§8.3).» |
| 300 Thm3 stmt | «**Theorem 3.** *Center independence of the lattice dynamics» | «**Theorem 3.** *For onsite center terms $m\varepsilon+p_0$ with site-independent coefficients in a ring without additive 2-torsion, on a lattice carrying both parity sectors, center independence of the lattice dynamics» |
| 302 Thm3 proof | «invariant under $\chi \to \varepsilon\chi$ (chiral symmetry). $\square$» | «invariant under $\chi \to \varepsilon\chi$ (chiral symmetry). Exact chirality in turn forces center independence: $\{D_{\text{st}}+m\varepsilon+p_0,\varepsilon\}=2m+2p_0\varepsilon$; on the parity sectors $\varepsilon=\pm1$ its vanishing gives, without additive 2-torsion, $m\pm p_0=0$, hence $2m=0$ and $m=p_0=0$. (kernel: `scalar_center_chiral_iff` in `OIBridge/ChiralCenterRecovery.lean`) $\square$» |
| 342 Thm5 scope | «carries the separate amplitude-scale-gauge/background-independence premises discussed in §4.6.» | «carries the separate amplitude-scale-gauge/background-independence premises discussed in §4.6 and a specified charged matter action.» |
| 372 Thm7 scope | «carries the amplitude-scale-gauge and background-independence premises stated below.» | «carries the amplitude-scale-gauge and background-independence premises stated below and a specified charged matter action.» |
| 376 M eigenspaces | «The decomposition therefore fixes the multiplicities of $M$'s eigenspaces uniquely;» | «The decomposition therefore fixes the block multiplicities uniquely;» |
| 388 Thm7b NN | «$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ under the commutant construction of Theorem 5. Furthermore,» | «$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ under the commutant construction of Theorem 5 on the nearest-neighbor link representation. Furthermore,» |
| 414 SU(3) factor claim | «The uniqueness of SC among cubic Bravais lattices extends to a stronger statement: **among all 14 three-dimensional Bravais lattices, SC is the unique candidate compatible with an $SU(3)$ gauge factor**.» | «The uniqueness of SC among cubic Bravais lattices extends to all 14 three-dimensional Bravais lattices: **no non-cubic Bravais lattice is compatible with an $SU(3)$ gauge factor**.» |
| 414 O(3)->SO(3) | «realized among finite subgroups of $\mathrm{O}(3)$ only by $S_4 \cong O$» | «realized among finite subgroups of $\mathrm{SO}(3)$ only by $S_4 \cong O$» |
| 426 commutant id | «it is the commutant (stabilizer) of the $O$-equivariant condensate $\Sigma$» | «it descends from the commutant (stabilizer) $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$ of the $O$-equivariant condensate $\Sigma$» |
| 454 Thm10 | «Anomaly cancellation (Theorem 15) then uniquely fixes the hypercharge assignment as the sole» | «Anomaly cancellation (Theorem 15) then uniquely fixes the hypercharge assignment, apart from the exceptional branch $Y_Q=0$, as the sole» |
| 458 Thm10 proof a | «the SM hypercharges are the unique anomaly-free assignment [16]» | «the SM hypercharges are the unique anomaly-free assignment apart from the exceptional branch $Y_Q=0$ [16]» |
| 458 Thm10 proof b | «anomaly cancellation (step iii) fixes the hypercharge assignment uniquely. $\square$» | «anomaly cancellation (step iii) fixes the hypercharge assignment uniquely apart from that branch. $\square$» |
| 472 hypercharge claim | «are, given the chiral structure (H-χ', §4.8), the unique anomaly-free consequence of placing» | «are, given the chiral structure (H-χ', §4.8) and a specified charged matter action, the unique anomaly-free consequence (apart from the exceptional branch $Y_Q=0$) of placing» |
| 509 commutant name | «the commutant $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ acts block-diagonally on it» | «the commutant $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$ acts block-diagonally on it» |
| 525 Step2 | «with fermions in fundamental or singlet representations, the six anomaly conditions force exactly the SM hypercharge assignment» | «with each family of fermions in the five fundamental or singlet representations of Theorem 15, the six anomaly conditions force, apart from the exceptional branch $Y_Q=0$, exactly the SM hypercharge assignment» |
| 527 (iv) | «Theorem 15 fixes the hypercharges uniquely; (v)» | «Theorem 15 fixes the hypercharges uniquely apart from the exceptional branch $Y_Q=0$; (v)» |
| 527 carriers | «every SM multiplet has a carrier, and the hypercharges are the unique anomaly-free completion given chirality.» | «every SM multiplet has a carrier for its non-abelian representation, and the hypercharges are the unique anomaly-free completion given chirality, apart from the exceptional branch $Y_Q=0$.» |
| 531 closure | «once both questions are asked at the link level, both close, and the closure is forced» | «once both questions are asked at the link level, both close at the level of non-abelian representation availability, and that closure is forced» |
| 575 Thm14 Lie | «Each factor of the commutant decomposes as $\mathrm{U}(n_i) = \mathrm{SU}(n_i) \times \mathrm{U}(1)_i$. For K = 6 with multiplicities (3, 2, 1): $G =» | «Each factor of the commutant decomposes at Lie-algebra level as $\mathfrak{u}(n_i) = \mathfrak{su}(n_i) \oplus \mathfrak{u}(1)_i$ (globally $\mathrm{U}(n_i) \cong (\mathrm{SU}(n_i) \times \mathrm{U}(1))/\mathbb{Z}_{n_i}$). For K = 6 with multiplicities (3, 2, 1), $G$ is locally $» |
| 575 Thm14 unique | «leaving exactly one free parameter (overall normalization). There is therefore exactly one anomaly-free U(1).» | «leaving, apart from the exceptional branch $Y_Q=0$ (Theorem 15), exactly one free parameter (overall normalization). There is therefore exactly one anomaly-free U(1) with $Y_Q \neq 0$.» |
| 579 Thm15 | «with fermions in fundamental or singlet representations, the six anomaly conditions [18] determine the hypercharges uniquely up to» | «with each family of fermions in the five fundamental or singlet representations $Q_L = (\mathbf{3}, \mathbf{2})$, $u_R, d_R = (\mathbf{3}, \mathbf{1})$, $L_L = (\mathbf{1}, \mathbf{2})$, $e_R = (\mathbf{1}, \mathbf{1})$ and family-universal charges, the six anomaly conditions [18] determine the hypercharges, apart from the exceptional branch $Y_Q = Y_L = Y_e = 0$, $Y_u = -Y_d$, uniquely up to» |
| 795 Q convention | «$Q = T^3 + Y/2$» | «$Q = T^3 + Y$» |
| 807 Sigma eigenspaces | «three eigenspaces of the coupling matrix $M$, three commutant factors» | «three eigenspaces of the condensate $\Sigma$, three commutant factors» |
| 1354 completeness | «What the framework proves is that (S, φ) is a *complete description* of reality up to gauge equivalence (the reconstruction theorem, developed in [Substratum]).» | «The framework proposes that (S, φ) is a *complete description* of reality up to gauge equivalence; the completeness of the generators of that gauge equivalence is open [Substratum §4].» |
| 1378 structural preds | «unique hypercharges from anomaly cancellation,» | «unique hypercharges from anomaly cancellation (apart from the exceptional branch $Y_Q=0$),» |
| 1408 Tier2 | «Theorem 7b selects it *because* an $\mathrm{SU}(3)$ factor is observed; §4.6)» | «Theorem 7b selects it *because* $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ is observed; §4.6)» |
| 1416 Proposition | «the anomaly-free hypercharge assignment given the sector pattern, and» | «the anomaly-free hypercharge assignment given the sector pattern (apart from the exceptional branch $Y_Q=0$), and» |

### book/ch05-gauge-structure.md
| site | old | minimal |
|---|---|---|
| 11 reconstruction | «under the reconstruction theorem's stated conditions, uniquely fixes the **local propagating lattice/gauge residue** up to the stated $\mathcal{G}_{\text{sub}}$ freedoms while» | «under the reconstruction theorem's stated conditions and its nearest-neighbor premise, fixes the **local propagating lattice/gauge residue** while» |
| 17 U->SU dependent | «with the later $\mathrm U	o\mathrm{SU}$ reduction carrying amplitude-scale gauge as before.» | «with the later reduction to $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ carrying amplitude-scale gauge and a specified charged matter action.» |
| 19 reconstruction | «the stated modeling/completeness conditions under which the **local lattice/gauge residue** is uniquely fixed.» | «the stated modeling/completeness conditions and nearest-neighbor premise under which the **local lattice/gauge residue** is uniquely fixed.» |
| 45 amplitude-scale reduction | «uses it: the overall $\mathrm{U}(1)$ phase of each block can be absorbed into a global rescaling of the field value, which is gauge by amplitude-scale invariance. The Standard Model gauge group is, in this sense, what remains of the natural commutant after the gauge degrees of freedom have been stripped out.» | «uses it: the common overall $\mathrm{U}(1)$ phase can be absorbed into a global rescaling of the field value, which is gauge by amplitude-scale invariance; the hypercharge direction among the remaining abelian phases is selected by a specified charged matter action and anomaly cancellation (§5.6).» |
| 95 Thm3 mirror | «The exact chiral symmetry of the emergent staggered fermions is equivalent to center independence of the substratum dynamics:» | «For site-independent center coefficients in a ring without additive 2-torsion, on a lattice carrying both parity sectors, the exact chiral symmetry of the emergent staggered fermions is equivalent to center independence of the substratum dynamics (SM Theorem 3):» |
| 101 Sigma eigenspaces | «one on each eigenspace of $M$: if $M$ has» | «one on each eigenspace of $\Sigma$: if $\Sigma$ has» |
| 125 reduction para | «The reduction is performed by the amplitude-scale-invariance argument developed in §5.2: each of the three factors has an overall $\mathrm{U}(1)$ phase that can be absorbed into a global rescaling of the field value at the relevant component, and global alphabet rescalings are gauge by amplitude-scale invariance of the substratum gauge group $\mathcal{G}_{\text{sub}}$. The overall $\mathrm{U}(1)$ of each $\mathrm{U}(n)$ factor is therefore not physical, and the commutant reduces to its $\mathrm{SU}(n)$ subgroup for $n \geq 2$.» | «At the level of Lie algebras each factor splits as $\mathfrak{u}(n) = \mathfrak{su}(n) \oplus \mathfrak{u}(1)$, so the commutant carries $\mathfrak{su}(3) \oplus \mathfrak{su}(2)$ and three abelian phase directions (globally $\mathrm{U}(n) \cong (\mathrm{SU}(n) \times \mathrm{U}(1))/\mathbb{Z}_n$). The common overall phase can be absorbed into a global rescaling of the field value, which is gauge by amplitude-scale invariance of the substratum gauge group $\mathcal{G}_{\text{sub}}$ (§5.2); selecting the hypercharge direction among the remaining abelian phases requires a specified charged matter action and anomaly cancellation (§5.6).» |
| 127 delete false para | «The reduction proceeds as follows. Writing $\mathrm{U}(3) = \mathrm{SU}(3) \times \mathrm{U}(1)_{\text{color}}$, the $\mathrm{U}(1)_{\text{color}}$ phase is the overall phase of the three-component $T_1$ block and is gauge by amplitude-scale invariance on those components. Similarly $\mathrm{U}(2) = \mathrm{SU}(2) \times \mathrm{U}(1)_{\text{weak}}$ with the overall phase gauge. The remaining $\mathrm{U}(1)$ block — the single $A_1$ component — has no $\mathrm{SU}$ subgroup since $\mathrm{SU}(1)$ is trivial, but its $\mathrm{U}(1)$ phase is physical (it controls the relative phase between the $A_1$ component and the higher-dimensional blocks), and identifies as the hypercharge $\mathrm{U}(1)_Y$.⏎⏎» | «» |
| 129 after reduction | «After the amplitude-scale reduction, the gauge group is» | «After this reduction, the gauge group is» |
| 131 premises | «after the separate amplitude-scale/background-independence premises are applied.» | «after the separate amplitude-scale/background-independence premises and the charged matter action are applied.» |
| 133 Bravais NN | «the simple cubic lattice is the unique one compatible with the Standard Model gauge group under the commutant construction.» | «the simple cubic lattice is the unique one compatible with the Standard Model gauge group under the commutant construction on the nearest-neighbor link representation.» |
| 139 commutant name | «The commutant $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ derived so far» | «The group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ derived so far» |
| 145 U->SU | «the amplitude-scale-invariance argument reduces $\mathrm{U}(n)$ to $\mathrm{SU}(n)$ for $n \geq 2$;» | «amplitude-scale invariance, a specified charged matter action and anomaly cancellation (§5.6) reduce the three abelian phase directions to the hypercharge;» |
| 183 anomaly uniqueness | «The remaining one-parameter freedom is the overall hypercharge normalization, which the framework fixes by amplitude-scale invariance — the same field-value-rescaling gauge of $\mathcal{G}_{\text{sub}}$ that reduced $\mathrm{U}(n)$ to $\mathrm{SU}(n)$ in §5.5.» | «Apart from the exceptional branch $Y_Q = Y_L = Y_e = 0$, $Y_u = -Y_d$ (SM Theorem 15), the remaining one-parameter freedom is the overall hypercharge normalization, which the framework fixes by amplitude-scale invariance — the same field-value-rescaling gauge of $\mathcal{G}_{\text{sub}}$ that removes the common phase in §5.5.» |
| 186 exactly one | «the six anomaly conditions identify exactly one as anomaly-free:» | «the six anomaly conditions identify exactly one, apart from the exceptional branch $Y_Q=0$, as anomaly-free:» |
| 188 q_e arithmetic | «$q_e = Y_e + (-1/2) \cdot 2 = -1$» | «$q_e = Y_e = -1$» |
| 192 summary reduction | «the amplitude-scale-invariance argument reduces the natural commutant» | «amplitude-scale invariance, a specified charged matter action and anomaly cancellation reduce the natural commutant» |
| 192 summary hypercharge | «the six anomaly conditions force the hypercharges to the observed values.» | «the six anomaly conditions force the hypercharges to the observed values, apart from the exceptional branch $Y_Q=0$.» |
| 194 premises | «conditional on H-link/H-cust and then on amplitude-scale/background-independence premises;» | «conditional on H-link/H-cust and then on amplitude-scale/background-independence premises and a specified charged matter action;» |
| 194 continuum | «The hypercharges are not chosen from a continuum of possibilities; they are determined by anomaly cancellation.» | «The hypercharges are not chosen from a continuum of possibilities; apart from the exceptional branch $Y_Q=0$, they are determined by anomaly cancellation.» |

### book/ch06-matter-content.md
| site | old | minimal |
|---|---|---|
| 8 reduction | «the amplitude-scale-invariance argument reduced the natural commutant to» | «amplitude-scale invariance, a specified charged matter action and anomaly cancellation reduced the natural commutant to» |
| 8 hypercharges | «anomaly cancellation forced the observed hypercharges.» | «anomaly cancellation forced the observed hypercharges, apart from the exceptional branch $Y_Q=0$.» |
| 8 qualifier | «is conditional on amplitude-scale gauge invariance, an explicit adjoined principle (Chapter 5 §5.2), and» | «is conditional on amplitude-scale gauge invariance, an explicit adjoined principle (Chapter 5 §5.2), together with a specified charged matter action, and» |
| 44 Higgs hypercharge | «combined with the unique anomaly-free hypercharge assignment.» | «combined with the unique anomaly-free hypercharge assignment apart from the exceptional branch $Y_Q=0$.» |
| 98 Sigma eigenspaces | «three eigenspaces of the coupling matrix $M$ and three commutant factors» | «three eigenspaces of the condensate $\Sigma$ and three commutant factors» |

## Statements whose text differs between OLD and MINIMAL (ledger updates)
- SM **Theorem 3** (statement and proof; new kernel citation `scalar_center_chiral_iff`, OIBridge/ChiralCenterRecovery.lean)
- SM **Theorem 7b** (statement: NN-premise insertion)
- SM **Theorem 10** (statement and proof: Y_Q=0 branch)
- SM **Theorem 14** (proof only: Lie-algebra form; Y_Q≠0)
- SM **Theorem 15** (statement: five-representation family, family-universal charges, exceptional branch)
- SM §8.3 **Proposition** ("Formal statement of the determination": Y_Q=0 branch)
- ch05: no numbered statements. The mirrored Theorem 3 sentence (§5.4) and the Bravais-uniqueness paragraph (§5.5) change.
- Unchanged: Theorems 5, 7, 16; the SM Corollary (|q_p|=|q_e|); ch05 Corollary (d=3).

## Notes for the coordinator
(a) **Lean/manuscript census**: #982 registered family "restricted first-order center and chirality recovery" with anchors "first-order operator with arbitrary onsite coefficients" (SM) and "arbitrary site-dependent onsite coefficients" (ch05). Neither anchor is in the minimal texts. The registry entry needs new anchors (e.g. "site-independent coefficients in a ring without additive 2-torsion"), or the census step fails. Check the coverage LEDGER rows for Theorem 3/14/15/Props 14a/15a the same way.
(b) A corpus-wide pattern that #982 also rewrote in SM 775/1378–1420 and ch06 48: an observable (masses, couplings) is said to "depend on the representative within the gauge class [(S,φ)]/G_sub". This conflicts with G_sub preserving all observables. The fix is cross-cutting (Methodology layer definitions), so these are kept as UNCERTAIN.
(c) Hypercharge as a combination αB+βL+γS of block phases (SM Thm 14 proof, Remark; ch05 §5.6 "identified as B and L") cannot reproduce e_R on the native carrier. Kept (UNCERTAIN). The minimal reduction sentences carry "a specified charged matter action" as an explicit premise instead.
(d) Propagation: the ch05/ch06 edits must be mirrored into FULL.md. Also update SM.tex/pdf and any Structure/appendix-b(B.6b)/glossary restatements of SM Theorem 3, Theorem 15 uniqueness and the U(n)→SU(n) reduction. The wording "apart from the exceptional branch $Y_Q=0$" matches the Substratum group's minimal file.
