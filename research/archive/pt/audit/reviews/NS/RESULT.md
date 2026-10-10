# NS — review of the supplied Navier–Stokes / horizon / OI analysis (thread NS, research-only)

Protocol `pt/audit/stage3-inputs/PROTOCOL-NS.md` (`4f61891f…`) over `PROTOCOL-STAGE2-DS.md` (`086a4cb8…`),
`PROTOCOL-STAGE2.md` (`38603692…`), `PROTOCOL.md` (`239dc123…`), amendments 1 (`b41aa0e7…`) and 2 (`2a2f78f3…`). Input
`pt/audit/stage3-inputs/ns/NS-INPUT.md` (`d8c5a1b3…`), read as data; "input Ln" below is a line of that file. Base L =
`9f9f8257a980a1819fbbc1dc0019917cf8678626` at `pt/base/` (commit date 2026-10-10). Not read: `pt/U/`, `pt/X/`,
`pt/audit/U/`, `pt/audit/X/`, `pt/audit/aborted-launches/`, `pt/audit/stage3-inputs/OWNER-*`,
`pt/audit/reviews/coherence-note/`, `pt/audit*-replay/`. No branch, PR, CI run, fetch, publication or repository change.

Evidence levels, kept apart throughout: **[K]** certified at L (module in the certified build; route in §1.1(c) and
§1.2); **[W]** written argument; **[X]** exact computation in this directory, stated for the instance it checks;
**[L, unverified]** literature not read at the source; **NOT CHECKABLE AT L** for events the corpus cannot settle. No
[D], no [N, numerical] and no UNBUILT Lean appear here. Repository facts cite `file:line` at L (paths under `pt/base/`;
"PROGRAMME" and "hypothesis" are `verification/programmes/hydrodynamics/PROGRAMME.md` and
`…/hidden-sector-singularity-hypothesis.md`).

## 0. Answer

**Bottom line.**
1. Corpus reading: the input's paraphrases of the programme and the note are faithful (C11–C14), but its route starts at H3 (H1–H2 are not closed), skips S2, and its theorem drops the gate (hypothesis L9: no question before an explicit map).
2. H-B: the claim is right at its instance [K `hb3a_no_closure`] (L = 4, b = 2, a 2D candidate outside the A5 class) but generic: H-A proved the same non-closure for the linear wave rule [K]. At that instance the pair separates only because of a collision [X].
3. Literature: neither the 2011 reduction nor the sphere/censorship work is cited, and nothing depends on them. Mori–Zwanzig is already a certified corpus theorem (SM Theorem 1a, [K] `mz_identity`), so C34/C37 understate it.
4. September 2026: NOT CHECKABLE AT L. The corpus records the 9/8 announcement only as an external test case (PROGRAMME L51, L218), so no verdict changes if the claims are false.
5. Mathematics [X]: the scaling identities hold. ε^{-3/2} is the L²-critical exponent, not the NS one (ε^{-1}). "Bounded at fixed resolution" holds for every map on a finite set, reversible or not. The dimension count is right [W].
6. Decisive null model: Burgers from −sin x blows up at t = 1 [X], while every closed Galerkin truncation stays regular for all time ([W]; the N = 2 solution exactly [X]). A fully observed finite bijective family realizes the boxed S1 shape with nothing hidden [X].
7. So "regular finite, singular continuum" is not an OI mechanism. The route from it to hidden-sector transfer is refuted, and the input's "OI hidden sector" conflates a map's complement with OI's observer-level hidden sector.
8. Quantum branch: no QM result is consumed (PROGRAMME L9, L216). But A5, which the quantum route needs, is not neutral for hydrodynamics, and the only fluid witness fails A5 (H-D result L683–685, L605–617).
9. Target labels: UNRESOLVED relative to L (it cannot even be stated: there is no continuum map); the generic route is refuted; nothing is INDEPENDENT. The input's "new test" cannot be run at L: four objects are missing (§4).
10. Horizons: the input keeps horizon and singularity apart, as S3 and control 6 require. It drifts toward reading a black-hole interior as an OI hidden sector, which GR L597 does not do.

**Verdict table (NS.1).** The UI line "Worked for 3m 20s" (input L8) is not numbered. 66 assertions: 25 ACCURATE, 24
ACCURATE WITH CORRECTION, 2 OVERSTATED, 2 UNDERSTATED, 0 INACCURATE, 13 NOT CHECKABLE AT L.

| id | claim (short; input line) | verdict | anchor |
|---|---|---|---|
| C1 | a potentially meaningful NS-singularity / horizon / OI connection (L10) | ACCURATE WITH CORRECTION | the corpus keeps S1–S2 and S3–S5 as separate bridges and links NS singularities to horizons nowhere: PROGRAMME L158, L210, L221; L231 "no such result is presently claimed" |
| C2 | established physics already provides part of the bridge (L10) | NOT CHECKABLE AT L | [L, unverified]; not cited at L (git grep: 0 hits, §1.2); no part reaches OI |
| C3 | fluids and horizons can describe related gravitational d.o.f. (L14) | NOT CHECKABLE AT L | [L, unverified] |
| C4 | an effective-equation singularity might reflect inaccessible d.o.f. (L16) | ACCURATE | PROGRAMME L27, L29; hypothesis L17 |
| C5 | the first possibility has established support (L18) | NOT CHECKABLE AT L | [L, unverified] |
| C6 | the second is not currently a theorem of OI (L18) | ACCURATE | hypothesis L3 "not a theorem", L80 "documented but not activated"; PROGRAMME L29 |
| C7 | 2011: Einstein's equations reduce to incompressible NS near horizons (L22) | NOT CHECKABLE AT L | [L, unverified]; Strominger occurs only at Structure.md:1456 (dS/CFT) and :1458 (Strominger–Vafa) |
| C8 | sphere-fluid regularity linked to cosmic censorship (L24) | NOT CHECKABLE AT L | [L, unverified]; "cosmic censorship": 0 corpus hits; that fluid is 2D (C47–C48) |
| C9 | horizon dynamics encoded by fluid equations, not metaphor (L26–28) | NOT CHECKABLE AT L | [L, unverified] |
| C10 | no fluid singularity is thereby a black hole; the interior is not the fluid's hidden sector (L30) | ACCURATE | [W]; hypothesis L72; PROGRAMME L221; GR L597 |
| C11 | a hypothesis note and a programme exist at 9f9f8257 (L34) | ACCURATE | hypothesis L1, L3; PROGRAMME L1 |
| C12 | they consider continuum singularities with regular finite reversible dynamics (L36) | ACCURATE | PROGRAMME L27; hypothesis L17 |
| C13 | not an entirely new direction for OI (L38) | ACCURATE | PROGRAMME L25–29; hypothesis L80 |
| C14 | the question is whether the programme can make it precise (L38) | ACCURATE WITH CORRECTION | gated: "only after … an explicit microscopic-to-continuum map" (hypothesis L9; PROGRAMME L127); the input omits the gate |
| C15 | 2026-09-08 announcement of forced 3D NS blow-up (L42) | NOT CHECKABLE AT L | PROGRAMME L51 records the announcement as "external target/motivation only"; forcing not mentioned at L |
| C16 | from rest; unbounded velocity; finite energy (L42) | NOT CHECKABLE AT L | "finite energy" matches PROGRAMME L51; the rest is absent at L |
| C17 | Clay statement of 2026-09-11 (L44) | NOT CHECKABLE AT L | no corpus mention |
| C18 | proof and Lean formalization public; acceptance under assessment (L44) | NOT CHECKABLE AT L | cf. PROGRAMME L51 "Until independently settled" |
| C19 | the unforced question remains open (L44) | NOT CHECKABLE AT L | [L, unverified] |
| C20 | the result separates unbounded velocity from finite energy (L46–50) | ACCURATE WITH CORRECTION | the separation does not need the 2026 result: kinematic family [X ns4 S2–S4]; it is already S1's form, PROGRAMME L133–141 |
| C21 | no contradiction: intense motion in a small region (L52) | ACCURATE | [X ns4 S2, S3, S4] |
| C22 | OI hypothesis: a finite description fails as structure concentrates (L54) | ACCURATE WITH CORRECTION | = "scale-transfer failure", hypothesis L47; true of any finite description [X ns5 B3, G5, F1] |
| C23 | transfer into an OI hidden sector needs a theorem (L56) | ACCURATE WITH CORRECTION | hypothesis L55, L76; but the note's hidden sector is "relative to the … map" (L34, L38), not OI's observer-level sector, absent a theorem (L72); §3.2 |
| C24 | schema u_ε(t) = P_ε(Φ_ε^{n(t)} s_ε) (L60–66) | ACCURATE WITH CORRECTION | = hypothesis items 1–3 (L31–33); P_ε and n(t) are the unfixed H4 items (H-A result L227–243; H-B result L313–319; ROADMAP L1219–1223); symbols lost in the received text |
| C25 | bounded at fixed resolution because the state space is finite (L68–70) | ACCURATE WITH CORRECTION | true for every map on a finite set, reversible or not [X ns4 F1; W]: it carries no dynamical information |
| C26 | the bound need not be uniform: sup_ε‖u_ε(t*)‖_∞ = ∞ (L72–76) | ACCURATE | [X ns4 F2; ns5 F1]; = PROGRAMME S1, L133–137 |
| C27 | microscopic systems can stay well-defined while the limit is singular (L78) | ACCURATE WITH CORRECTION | true and generic, with nothing hidden [X ns5 B3, G4, G5, F1] |
| C28 | "the precise OI mechanism" / "the crucial distinction" (L58, L78) | OVERSTATED | not OI-specific (C27); the route to hidden-sector transfer is refuted [X ns5]; hypothesis L49 |
| C29 | the family u_ε = ε^{-3/2} f((x − x₀)/ε) (L80–84) | ACCURATE | divergence-free preserved [X ns4 S0, S1; countercontrol CC3] |
| C30 | ‖u_ε‖₂² = ‖f‖₂², ‖u_ε‖_∞ = ε^{-3/2}‖f‖_∞ (L86–92) | ACCURATE | [X ns4 S2, S2t, S3; countercontrols CC1, CC2] |
| C31 | energy constant while the peak diverges (L94) | ACCURATE | [X ns4 S4] |
| C32 | kinematic, not an NS solution (L94) | ACCURATE | [X ns4 S6: the NS symmetry is ε^{-1}, energy ∝ ε; S5: enstrophy ∝ ε^{-2}] |
| C33 | shows finite microscopic regularity and continuum singularity compatible (L94) | ACCURATE WITH CORRECTION | it shows finite energy with unbounded peak; microscopic regularity enters only on finite approximants [X ns4 F2; ns5 F1] |
| C34 | Mori–Zwanzig "already establishes an important connection" (L98) | UNDERSTATED | the corpus has the identity as a certified theorem: SM.md:238–246; [K] `mz_identity` verification/lean/OI_Structural_Core.lean:275 |
| C35 | projected-away d.o.f. return as memory and unresolved-force terms (L100) | ACCURATE | [K] OI_Structural_Core.lean:275, :291; [X ns5 M1, CC-M] |
| C36 | direct applications to turbulent fluids (L100) | NOT CHECKABLE AT L | [L, unverified] |
| C37 | "closely resembles" OI's visible/inaccessible division (L102) | UNDERSTATED | SM.md:246 identifies the corpus's own projected identity as MZ structure; its use for singularities needs a theorem (hypothesis L72) |
| C38 | H-B: equal two-time coarse states, different next momentum; "pointing in this direction" (L104) | ACCURATE WITH CORRECTION | [K] `hb3a_block_state_not_closed` HexLatticeGas.lean:942–958, at L = 4, b = 2 only, a 2D candidate in the A1–A4, ¬A5 class (H-B result L53–62); generic: [K] `h3a_no_closure` HydroSourceAudit.lean:863 |
| C39 | the reduced variables do not close at that scale (L104) | ACCURATE | [K] `hb3a_no_closure` HexLatticeGas.lean:989–997; re-evaluated [X ns2 A1–A5] |
| C40 | a real closure failure due to unresolved microscopic information (L106) | ACCURATE WITH CORRECTION | exact non-closure of one variable at one scale, not a statistical one (H-B result L303–309, H3 HO); the separating information is co-location that triggers a collision [X ns2 CC1, C3, CC3] |
| C41 | next: can the failure grow more severe in a controlled limit (L108) | ACCURATE WITH CORRECTION | downstream of H4–H7 (hypothesis L67); "severity" needs a preregistered measure (L35–36) that separates it from generic non-closure (H-A result L199–225) |
| C42 | black holes a special case: possibly, not automatically (L112) | ACCURATE | PROGRAMME S4 L160–169; L231 final sentence |
| C43 | table: NS blow-up → singular projection or concentration (L116) | ACCURATE WITH CORRECTION | = hypothesis L45, L47; omits "microscopic failure" (L44) as an alternative |
| C44 | table: coarse-graining → hidden degrees give memory and transfer (L117) | ACCURATE WITH CORRECTION | = closure failure (L46) and MZ memory [K]; "hidden" here is the map's complement, not OI's hidden sector (L38, L72) |
| C45 | table: event horizon → causally inaccessible sector (L118) | ACCURATE WITH CORRECTION | S3 L155, S4 L165; GR L597: a BH horizon "does not redefine that observer's epistemic partition"; the interior is a secondary partition only in the nested formalism (GR L599–601; book/ch07-gravity.md:118–122) |
| C46 | table: spacetime singularity → emergent-geometry failure (L119) | ACCURATE | S3 L156, S4 L166; the geometry is not derived at L (GR L691, L697) |
| C47 | 4D Schwarzschild horizon cross-section is 2D (L121) | ACCURATE | [W] D − 2 = 2 |
| C48 | its horizon fluid is 2D, on S² (L121) | ACCURATE | [W]; the manifold symbol is lost in the received text; the construction is [L, unverified] |
| C49 | a 3D horizon fluid needs 5D spacetime (L121) | ACCURATE | [W] D = 3 + 2 |
| C50 | no identification of the Clay problem with a BH-interior singularity (L121) | ACCURATE | [W]: a 4D black hole gives a 2D fluid, which lives on the horizon, not inside |
| C51 | incompressible NS defines no event horizon (L123) | ACCURATE | [W]: pressure is fixed instantaneously by an elliptic equation, so there is no finite signal cone; the corpus's only fluid–horizon touchpoint is Unruh's sonic analogue (GR.md:883, :607) |
| C52 | the route is "already essentially specified" (L127) | ACCURATE WITH CORRECTION | the ladder is specified (PROGRAMME §3, §5, §6); the next round named is H-C (H-F result L937–944); see C53 |
| C53 | H3–H7: mixing, scaling, conservation, viscosity, incompressibility (L129–131) | ACCURATE WITH CORRECTION | H3 L71, H4 L75, H5 L81, H6 L85, H7 L91; omits H1 (L59) and H2 (L65), neither closed for the concrete representative (L231); carrier question open (H-F result L1008) |
| C54 | S1: regular finite dynamics, singular continuum limit (L133–135) | ACCURATE WITH CORRECTION | = PROGRAMME S1, L129–143; opens only after H4–H7 (L127), round S-A only after H-C (L204–206); generic [X ns5] |
| C55 | S2a: whether unresolved transfer is necessary or sufficient (L137–139) | ACCURATE WITH CORRECTION | S2a is in the note (L13–25, L65), not PROGRAMME; L55 asks "necessary, sufficient, both, or neither" and includes closure; S2 (PROGRAMME L145–149) skipped; S2a not activated (L80) |
| C56 | S3–S5 only after an effective causal geometry and horizon criteria (L141–143) | ACCURATE | PROGRAMME L151–182; round S-B L208–210 |
| C57 | "most valuable new test": a known singular NS profile as limit of regular OI systems, transfer controlled (L145) | ACCURATE WITH CORRECTION | respects the gate; = round S-A (L204–206) + S2a (L55) with a named target; not executable at L (§4); without a closed-model countercontrol it does not discriminate [X ns5] |
| C58 | the external force must be accounted for, not relabeled (L147) | ACCURATE | [W]; hypothesis controls 3–4, L73–74 |
| C59 | "a serious mathematical research direction" (L151) | NOT CHECKABLE AT L | evaluative; the corpus calls it "a hypothesis to test" (PROGRAMME L29) |
| C60 | projection → unresolved dynamics and memory → possible failure, "already line up" (L153) | ACCURATE WITH CORRECTION | the first two arrows are exact for any projection ([K] `mz_identity`; [X ns5 C1, C2, M1]) and line up in the non-OI null model; no OI hydrodynamic projection exists at L (H4 HO) |
| C61 | this route does not first require deriving QM (L155) | ACCURATE WITH CORRECTION | PROGRAMME L9, L216; but A5, "needed by the current quantum-completion route" (H-D result L683–685), is not neutral here (H-D result L605–617), and the only fluid witness fails it (H-B result L53–57) |
| C62 | "a separate consequence of OI's finite, reversible, locally interacting substratum" (L155) | OVERSTATED | nothing hydrodynamic is derived (L231; H-D result L621–624); the description drops A5–A6 (papers/Substratum.md:100–102); control 2, PROGRAMME L217 |
| C63 | the BH reading requires an effective horizon with GR's causal properties (L157) | ACCURATE | PROGRAMME S4–S5, L160–182; horizons enter the corpus from GR (GR L40) and the geometry is not derived (GR L691, L697) |
| C64 | the first theorem is not "NS singularities are black holes" (L159) | ACCURATE | PROGRAMME L221; hypothesis L3 |
| C65 | first theorem: singular limit from regular OI dynamics, failure attributable or provably not (L159) | ACCURATE WITH CORRECTION | a weaker restatement of hypothesis L55 (drops the stated map, the regularity class, closure and the four-way outcome); first half generic [X ns5]; §4 |
| C66 | that would be a concrete connection, not an analogy (L161) | ACCURATE WITH CORRECTION | only through the attribution half, at the stated substratum and map (AGENTS.md L45–51 claim/evidence boundary, L89–90 no bridge without an explicit formal map); the emergence half alone is generic [X ns5] |

**Target assessment (NS.5, NS.7), with labels (amendment 2) and evidence levels.**

| item | label / status | evidence |
|---|---|---|
| T-NS, framework-specific: for an OI substratum with its own continuum map, a singular continuum hydrodynamic description emerges from globally regular reversible dynamics, and the failure is attributable (or provably not) to a specified hidden-sector transfer | **UNRESOLVED** relative to L, and not statable at L: no microscopic-to-continuum map (four of H-A's five scaling items unfixed), no Euler or NS limit, no hidden-sector split or transfer functional; the note's own gate is closed | PROGRAMME L127, L231; hypothesis L9, L29–36, L80; H-E result L381–415 (HE5 "unstatable"); ROADMAP L1219–1225 [record] |
| the generic route: regular finite approximants + singular continuum limit (+ uniform energy bound) ⇒ hidden-sector transfer | **route refuted** (not INDEPENDENT: the countermodels satisfy the route's premises, not every certified premise of an OI substratum, which L does not define for this question) | [X ns5 B1–B5, G1–G7, F1]; [X ns4 F1, F2]; [W] §3.1 |
| the existence half for non-OI systems | holds, generically | exact for the closed truncations and the singular continuum solution [X ns5]; convergence of truncations before t* [L, unverified], not used |
| S1 as an OI obligation (PROGRAMME L129–143) | open; branch closed until H4–H7 | PROGRAMME L127; H-B result L354–357; H-F result L1043–1044 |
| HB3-a as evidence of hidden-sector transfer | not evidence: an instance of the generic H3 closure gap | [K] HexLatticeGas.lean:942, :989; [K] HydroSourceAudit.lean:863, :875; H-E result L185–195; [X ns2] |
| A5 relative to the hydrodynamic branch | the corpus's own labels: needed by the quantum-completion route; hydrodynamic necessity UNDECIDED | H-D result L665–685 [record]; H-A's gate [K, cited by H-D result L594–600] |
| the input's "most valuable new test" | not executable at L; four objects missing (§4) | §4 |
| the black-hole reading (S4) | a programme hypothesis; horizons enter the corpus from GR, not derived | PROGRAMME L160–182; GR L40, L691, L697 |

Kernel results this review leans on [K]: `hb3a_block_state_not_closed`, `hb3a_no_closure`, `h3a_no_closure`,
`h3a_control_L4_closes`, `mz_identity`, `kernel_equivariant`. Exact computations [X]: `ns2_hb3_recheck.py` (12 checks),
`ns4_scaling.py` (14), `ns5_null_model.py` (19), each replayed byte for byte. Written arguments [W]: dimension count,
Chebyshev concentration, global existence on the energy sphere, the Galerkin gradient bound, the NS scaling chain rule,
incompressible signal speed. Literature [L, unverified]: the 2011 reduction, the sphere/censorship work, MZ in
turbulence, Galerkin convergence and thermalization, 2D NS regularity, the Clay problem statement.

**What the owner should take from the input.**
- The forcing caveat (C58) and the dimensional caveat (C47–C51): boundary conditions on any later use of the 2026
  claims or the fluid/gravity literature.
- The attribution-or-non-attribution shape of the target (C65), in the note's fuller form (hypothesis L55), run with
  the decision rule of §3.4: a closed-truncation control and a fully observed control are mandatory.
- The status statements that match the corpus: C6, C23, C42, C56, C63, C64.

**What to discard.**
- "The precise OI mechanism" and "the crucial distinction" (C28): the shape is generic to finite truncations.
- "A separate consequence of OI's finite, reversible, locally interacting substratum" (C62).
- HB3-a read as "pointing in this direction" (C38): it is the generic closure gap, also present in the linear wave rule.
- Mori–Zwanzig as an external resemblance (C34, C37): the corpus has it as a certified theorem.
- The route label "H3–H7" without H1–H2 and without the carrier question (C53).

## 1. Claim by claim (NS.1–NS.3, NS.6, NS.8)

### 1.1 NS.2 — the cited corpus

**(a) What the two documents say, quoted at L.**
- hypothesis L3: "This is a **strategic research note**, not a theorem, preregistration, execution result, manuscript edit, or claim that Operational Incompleteness (OI) resolves Navier–Stokes singularities."
- hypothesis L9, the gate: "The question opens **only after** the programme has an explicit microscopic-to-continuum map and convergence notion of the kind required by H4–H7. Before that point, the phrases *visible sector*, *hidden sector*, *transfer*, *loss of closure*, and *singularity of the projection* do not name sufficiently fixed mathematical objects for a theorem."
- hypothesis L17, the hypothesis: "a putative singularity of the emergent Navier–Stokes variables may occur while the full finite reversible OI evolution remains regular because information, correlations, conserved structure, or other dynamically relevant degrees of freedom leave the resolved hydrodynamic sector and become carried by degrees of freedom hidden from the chosen continuum projection."
- hypothesis L34 and L38, what "hidden" means: "the complementary degrees of freedom called *hidden* relative to that projection"; "The hidden sector is therefore **relative to the proved observation/coarse-graining map**."
- hypothesis L44–49: four outcomes (microscopic failure, projection singularity, closure failure, scale-transfer failure); "None is established by microscopic reversibility alone."
- hypothesis L55, the target: "for a stated OI substratum, a stated continuum map, and a stated regularity class, determine whether finite-time loss of regularity or hydrodynamic closure of the resolved variables can coexist with globally regular microscopic evolution; if it can, determine whether a quantitatively identified transfer into the hidden sector is necessary, sufficient, both, or neither."
- hypothesis L75, control 5: "Unbounded resolved fields and failure of a reduced equation to remain closed are distinct outcomes." L80: "**documented but not activated**".
- PROGRAMME L27 and L29: "a continuum singularity may be a singularity of the emergent observable/continuum description while the underlying finite reversible substratum remains completely regular"; "This is initially a hypothesis to test, not a claim of the corpus." L127: "The singularity programme opens **only after** a controlled continuum bridge such as H4–H7 exists." L143: "If proved, this would establish a precise mathematical sense in which a **continuum singularity need not be a substratum singularity**."

**Faithfulness.**
- **Faithful:** input L36 ("a continuum singularity reflects a failure of the observer's effective description while the underlying finite reversible dynamics remains regular") restates PROGRAMME L27 and hypothesis L17. Input L38 matches L80 ("When that bridge exists, S2a can be turned into its own frozen research round"). Input L56 ("requires a theorem") matches L55 and L76.
- **Added:** input L56 writes "an OI hidden sector". The note's hidden sector is relative to the chosen map (L34, L38); identifying it with any other hidden-sector structure needs "a theorem identifying the same object" (L72). The input adds that identification without one (§3.2).
- **Omitted:** the gate (L9; PROGRAMME L127), in the input's §2 and in its theorem (input L159); the four outcomes (L44–49), reduced to "attributable or not"; the stated regularity class (L55).
- **Respected:** control 5 (L75). The input's table keeps blow-up (input L116) and closure failure (L117) on separate rows, and it calls H-B's result "not a continuum singularity" (L106).

**(b) The route labels against the ladder.**

| input label (input line) | programme object | match | correction |
|---|---|---|---|
| "H3–H7: … Mixing, scaling, conservation, viscosity and incompressibility" (L129–131) | H3 mixing (PROGRAMME L71–73); H4 scaling map (L75–79); H5 "conservative hydrodynamic equations" (L81–83); H6 viscosity (L85–89); H7 incompressible NS (L91–97) | content and order match | the ladder starts at H1 (local conserved observables, L59–63) and H2 (isotropy, L65–69), "in order" (L57); neither is closed for the concrete wave representative (L231); for H-B's candidate both are closed only for the candidate, in the ¬A5 class (ROADMAP L1187–1189); the limit round is H-C (L200–202), named next by H-F (H-F result L937–944) and not commissioned |
| "S1: … Regular finite dynamics, singular continuum limit" (L133–135) | S1 (PROGRAMME L129–143) | exact | gated (L127); round S-A only after H-C (L204–206) |
| "S2a: … necessary or sufficient for the loss of regularity" (L137–139) | S2a of the note (hypothesis L13–25), "downstream of the same H4–H7 prerequisite as S1 and S2" (L67) | close | S2a is not in PROGRAMME.md; S2 (PROGRAMME L145–149, name the failed map) is skipped though S2a refines it (hypothesis L65); the note's outcome is four-way and includes closure (L55) |
| "S3–S5: … Only after deriving an effective causal geometry and horizon criteria" (L141–143) | S3 (PROGRAMME L151–158), S4 (L160–169), S5 (L171–182); round S-B (L208–210) | exact | none |

Rounds: PROGRAMME §6 lists H-A, H-B, H-C, S-A, S-B (L186–210). Executed at L: H-A, H-B, H-D, H-D-SR, H-E and H-F. Their
record directories are under `verification/programmes/hydrodynamics/`. "H-F" is an identifier, not a rung or an S-label
(H-F result L10–13).

**(c) The H-B closure-failure claim (input L104–106).**
- **Record.** Round H-B, result L263–309 (`HB3`): "At `t + 1` the momentum component `P₁` on block `(0, 0)` is `1` for `c` and `0` for `c'`. **Equal coarse two-time states, different coarse states at `t + 1`.**" (L283–284). Then: "**Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility of a statistical closure at some other scale or in some other variable" (L303–304). And: "this block variable needs more than its own two-time state to predict its next value" (L307–309).
- **Kernel statements.** `hb3a_block_state_not_closed` (verification/lean-mathlib/OIBridge/HexLatticeGas.lean:942–958): two configurations, pinned by equation, have equal block sums for every block and every channel weight at t and at t − 1, and P₁ on block (0, 0) at t + 1 is 1 and 0. `hb3a_no_closure` (:989–997): no Ψ maps the (M, P₁, P₂) block charges at t and t − 1 to those of Φc, for all c.
- **Evidence level [K].** The route:
  - root import `import OIBridge.HexLatticeGas` (verification/lean-mathlib/OIBridge.lean:63; HydroSourceAudit :64; HydroClosureBridge :244);
  - `defaultTargets = ["OIBridge"]` (verification/lean-mathlib/lakefile.toml:2);
  - CI job "Mathlib bridge" (.github/workflows/verify.yml:70) runs `lake --rehash build` (:127) and then the release gate (:150), whose `lean-axioms` step reads `#print axioms` (tools/release_gate.py:137–138);
  - no `sorry`, `admit`, `axiom` or `native_decide` in HexLatticeGas.lean, HydroSourceAudit.lean or HydroClosureBridge.lean (grep, empty);
  - census status "kernel-only" with no manuscript anchor (verification/lean-manuscript-census.json:875–880, :866–871, :730–735).

  The record reports evidence level 2 with its axiom table (H-B result L424–503). No Lean was rebuilt here: the [K] rests on L being certified main and the module being in its default build target.
- **Probe scripts at L: none.** The preregistration's recorded analysis was "carried out by hand and by an exact script … **before this file was written**", and "nothing here is evidence at any level above "recorded analysis"" (H-B preregistration L157–160). The witness was "found by exhaustive search over configurations of mass `≤ 3`" (L203). That script is not in the tree: `git ls-files` lists no hydrodynamics script, and `verification/lean/edge_rigidity_probe.py:9474–9484` only checks that the theorem statements are present. Nothing was replayable byte for byte. In its place this review ran an independent exact re-evaluation, [X] and not a replay: `ns2_hb3_recheck.py`, 12/12 (§6).
- **What the re-evaluation adds [X].**
  - The outputs equal the recorded values (preregistration L207–213).
  - Without the collision (pure streaming), the same pair agrees at t + 1 (CC1).
  - At L = 4, b = 2, pure streaming closes even the full block channel histogram, because two steps move every particle by exactly one block (C3: exhaustive lemma plus all 4657 configurations of mass ≤ 2).
  - The gas breaks that rule on c′ (CC3).

  The separating information is sub-block co-location that triggers a collision.
- **Generic, not directional.** H-A proved the same kind of exact non-closure for the *linear* wave representative: `h3a_no_closure` (verification/lean-mathlib/OIBridge/HydroSourceAudit.lean:863; d = 1, L = 6, b = 3, every q ≥ 2), with a proved closing control `h3a_control_L4_closes` (:875); re-evaluated [X ns2 H1, H2, CC4]. H-E reads HB3-a as closure-gap item 1, "The flux term is not a function of the coarse state" (H-E result L185–195): the H3 problem a local-equilibrium condition must solve. The record does not read it as hidden-sector evidence, and nothing in it supports "pointing in this direction" beyond the generic MZ statement (§3.2).

**(d) The programme's one-line state, PROGRAMME L231, verbatim.**

> **A new parallel programme is opened: determine whether the concrete finite, deterministic, reversible, local OI substratum lies in a Navier–Stokes hydrodynamic universality class, first by auditing the exact conservation, isotropy, mixing and scaling obligations and then, only if that bridge closes, test whether continuum fluid and spacetime singularities can arise as failures/incompleteness of the emergent observable description while the underlying substratum dynamics remains regular. Round H-A, the source audit of the concrete wave representative, is executed at evidence level 2 (`round-h-a-source-audit/result.md`): the advection obligation is HI conditional on `ZMod q`-linear coarse variables, with real-valued or nonlinear coarse variables HO; the only total-sum conservation law is conserved in the manuscript instance iff `q ∣ 4`, so that candidate field is not `q`-gauge invariant — HI for that candidate under the `q`-gauge principle, HO for every other candidate conserved field, and not a universal no-go; the axis stencil's fourth moment is proved anisotropic — conditional HI if H5's stress closure consumes this tensor, otherwise H2 remains HO; H3 and H4 are HO. H-B: one candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open (`round-h-b-reversible-fluid-substratum/result.md`). H-E: one candidate bridge condition is stated against the H3 obligation for round H-B's candidate and its product-form, family-invariance and parameter-space flux clauses are established, with the mean charges recovering the parameters on the image of the mean-charge map and nowhere else; the clause that would supply closure is the propagation clause, which is neither stated nor proved, four of the five scaling-skeleton items being unfixed on the record, so H3 stands as a component of a bridge and not as one and the H3 obligation stays HO (`round-h-e-h3-closure-bridge/result.md`). Black-hole horizons are treated as causal/observational boundaries and spacetime singularities as geodesic/path incompleteness; a future OI explanation may connect both to observer-level incompleteness, but the two are not conflated and no such result is presently claimed.**

**(e) What is HO, HI, HC and HD today.** Labels are as the record gives them. H-D and H-F move none (H-F result
L1040–1041).

| object | carrier | label | anchor |
|---|---|---|---|
| advection obligation | wave representative | HI conditional on `ZMod q`-linear coarse variables; HO for real-valued or nonlinear ones | H-A result L64–66; PROGRAMME L231 |
| H1, conserved fields | wave representative | HI for the total-sum candidate under the q-gauge principle; HO for every other candidate | H-A result L117; L231 |
| H1 | H-B candidate (¬A5 class) | HD for mass and momentum, on the sector, for the candidate; HO outside the class | ROADMAP L1187–1188 |
| H2, isotropy | wave representative | conditional HI if H5's stress closure consumes the axis tensor, otherwise HO | H-A result L178–182; L231 |
| H2 | H-B candidate | HD for the stencil tensor; HC for the stress conditional on H5 consuming it; otherwise HO | ROADMAP L1188–1189 |
| H3 | both; H-E's bridge condition | HO ("a component of a bridge and not … one") | L231; ROADMAP L1223–1224 |
| H4 | both | HO; four of five scaling items unfixed; H-B fixes the field lift only | H-B result L313–319; L231 |
| H5, H6, H7 | none | HO; not begun | H-D result L621–622, L739 |
| S1–S5 | none | branch closed until H4–H7 exist | PROGRAMME L127; H-F result L1043–1044 |
| S2a | none | "documented but not activated" | hypothesis L80 |

Owner decisions open on this axis (H-F result L1002–1008):
- the admissibility of the A1–A4, ¬A5 class;
- the carrier a round H-C would run on;
- who refreshes PROGRAMME §8;
- whether the negative resolution of the entailment question propagates;
- the reach of the `R7-HY*` guards.

The one-line state mentions neither H-D nor H-F (marker 1, §1.6).

### 1.2 NS.3 — literature

**Corpus search.** `git grep` over `*.md`, `*.lean`, `*.py`, `*.json`, `*.tex` at L:
- **No hits:** Bredberg, Lysov, Keeler, Minwalla, Bhattacharyya, "fluid/gravity", "fluid-gravity", "membrane paradigm", Damour, "cosmic censorship", Burgers, Galerkin.
- **Strominger, two references, neither about fluids:**
  - papers/Structure.md:1456 [StromingerDS2001], "The dS/CFT correspondence", used at L458 (de Sitter holography, "open");
  - :1458 [StromingerVafa1996], "Microscopic Origin of the Bekenstein-Hawking Entropy", used at L452 (string state counting of the 1/4, set against OI's mode counting).
- **Mori–Zwanzig:** papers/SM.md:246 (also SM.tex:1714) attributes SM Theorem 1a to "standard Mori–Zwanzig/Nakajima–Zwanzig structure and is not claimed as new". papers/Complexity.tex:1911 cites "Zwanzig 1990" in an unrelated context.

**Dependence.**
- **The 2011 reduction and the sphere/censorship work.** Nothing at L depends on them: neither is cited.
- **External precedents in the hydrodynamics programme.** It names two, FHP (PROGRAMME L49) and the 2026 OpenAI work (L51). Control 3 (L218) forbids either as a premise.
- **The Mori–Zwanzig identity.** The corpus does depend on it, in its own certified form: SM Theorem 1a, [K] `mz_identity` and `kernel_equivariant` (verification/lean/OI_Structural_Core.lean:275, :291).
  - Build route: a zero-import file compiled with `lean` in the core job "Kernel check" (.github/workflows/verify.yml:46–56; file list :50; toolchain `leanprover/lean4:stable`, :38); no `sorry`.
  - Use: SM's isotropy argument (SM.md:246).
  - Bearing on singularities: none without "a theorem identifying the same object" (hypothesis L72).

**As recalled [L, unverified]; no verdict relies on these attributions.**
- The 2011 reduction is Bredberg–Keeler–Lysov–Strominger, "From Navier–Stokes to Einstein".
- The sphere work is Bredberg–Strominger on black holes as incompressible fluids on the sphere.
- MZ-based closures for turbulence exist.

None was read at the source.

**The September 2026 claims: NOT CHECKABLE AT L.**
- **What the corpus records.** L is dated 2026-10-10, so the 9/8 announcement predates L, and the corpus records it at PROGRAMME L51: "The OpenAI Navier–Stokes work announced on 2026-09-08 supplies a sharp downstream test case for continuum breakdown: its stated result is a finite-time singular solution of the continuum equations with finite energy. Until independently settled in the normal mathematical process, this roadmap treats that work as an **external target/motivation only**, never as a premise in an OI theorem." See also control 3, L218. That record is a report, not a verification.
- **What the corpus lacks.** None of the input's details: the smooth external force, the start from rest, the 9/11 Clay statement, a public proof and Lean formalization, the open unforced question.
- **If they were false:**
  - **The corpus is unchanged.** Only PROGRAMME.md:51 and :218 mention the work ("OpenAI": 2 hits), both as a test case. S1 (L129–143) and the note are stated without it. No module, round or manuscript consumes it.
  - **The input:** the separation of unbounded velocity from finite energy in the input's §3 survives, because it is kinematic [X ns4]. The "most valuable new test" loses its only candidate 3D NS profile: no singular profile of the unforced 3D equations is known [L, unverified]. It would fall back on model equations (Burgers, as in this review's §3), and C58 becomes moot.
  - **This review:** no verdict uses the claims, so every verdict stands.
- **If true and forced:** the force has to appear in the resolved momentum balance (C58), and the result bears on the forced problem only. As recalled, the official problem statement admits a breakdown with a smooth force as one resolution [L, unverified].

### 1.3 NS.6 — independence from the quantum branch

**What the programme states.** PROGRAMME L9: "it neither advances nor blocks the OI → QM equivalence/classification
chain unless an explicit theorem later connects the two. Conversely, OI → QM results may not be imported here as
evidence without a proved bridge"; control 1 (L216). No obligation H1–H7 names A5 or additivity (H-D result
L516–541). So "does not first require deriving quantum mechanics" (C61) is accurate as to results.

**Declared inputs the hydrodynamic branch rests on.**
1. The concrete OI substratum with A1–A6 (PROGRAMME L35: "finiteness, deterministic reversible dynamics, bounded/local coupling degree, center/translation independence up to gauge, linearity, and background independence"). At source (papers/Substratum.md:90–102) these are "restrictions on the class of candidate substrates": sufficient for the reconstruction, with their independence not established (H-D result L105–106).
2. The kernel's `Substratum` interface, with the kernel A5 as additivity of the rule (SubstratumInterfaceAudit.lean:102). H-A and H-B consume it unmodified.
3. SM's rule and gauge principles (§2.7 alphabet as gauge; §4.1 amplitude-scale gauge and the linearity lemma), consumed and not tested (H-B result L363–366).
4. Control 2 (PROGRAMME L217): "the concrete local OI substratum plus whatever hydrodynamic conditions survive the source audit, not arbitrary finite reversible systems". This covers H3's equilibrium condition, H4's scaling map, and H5's pressure and equation of state, which may be named "as additional constitutive input" (L83).
5. The carrier: the wave representative under H-A's linearity gate, or H-B's gas outside the A5 class. Open owner decision (H-F result L1008).

**Where the branches touch: A5.**
- **(b), quantum-route necessity:** "A5 is used at eight located steps of the reconstruction chain, and each located use is quantum-specific" (H-D result L665–667, medium strength).
- **(c), hydrodynamic necessity:** UNDECIDED. Verbatim: "A5 is needed by the current quantum-completion route, and its necessity for Navier–Stokes remains undecided" (L683–685).
- **The other direction:** A5 "is not neutral for the hydrodynamic target on at least one named class" (L605–606). There, "on substrata satisfying A5, no closed `ZMod q`-linear coarse description carries an advective term" (L599–600).
- **The only fluid witness fails A5-ker** (`hexSubstratum_not_A5`, HexLatticeGas.lean:685), and the admissibility of its class is open (H-B result L58–62).
- **Guardrail:** "H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with the right microscopic ingredients; it does not yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit" (H-D result L577–579).

**Verdict.** The route does not require QM first (C61, ACCURATE WITH CORRECTION). It is not "a separate consequence of
OI's finite, reversible, locally interacting substratum" (C62, OVERSTATED):
- nothing hydrodynamic is derived;
- "finite, reversible, locally interacting" names A1–A3, the class H-B lives in with A4, and drops A5 and A6;
- at L the branch's one fluid witness lives exactly where the quantum route's premise fails.

**Hidden assumption exposed:** the input presumes one substratum serves both branches. If the ¬A5 class is ruled
inadmissible, hydrodynamics is left with the wave representative and the linearity gate. If it is ruled admissible,
the two branches run on different substrata unless A5 is shown dispensable for one of them. The results are separable
(control 1); the premise is shared.

### 1.4 NS.8 — the horizon connection

**The programme's stance.**
- S3 (PROGRAMME L151–158): an event horizon is "a causal/observational boundary"; a singularity is "geodesic/path incompleteness"; "they are distinct mathematical phenomena and require separate bridges".
- S4 (L160–169), the four-item chain, ending: "neither 2 nor 3 is interpreted as failure of the microscopic bijection unless a theorem proves such a failure".
- S5 (L171–182): the recovery obligations, first "an effective Lorentzian metric or causal order".
- Controls 6–7 (L221–222), and the final sentence of L231 (quoted in §1.1(d)).

**Structure.** Horizons appear only through entropy and holography (§7.7.1, L448–462). "OI's [GR §5] derives the
A/4 coefficient" (L450); "OI naturally produces horizon holography … but does not naturally produce full AdS/CFT-style
correspondence" (L462); de Sitter holography is open (L458). There is no causal-structure derivation and no
singularity treatment.

**GR.**
- Horizons are taken from GR: "This is a consequence of GR's causal structure, not a modeling choice" (GR L40). Event and apparent horizons are kept apart (L56).
- Black holes, L597: "A black-hole horizon within the cosmological visible sector is a *local* causal boundary: it prevents an external observer from probing the black-hole interior by direct geometric access, but it does not redefine that observer's epistemic partition … The framework's BH physics for external observers is identical to standard GR plus the cosmological-scale dark-sector effects".
- The nested formalism (L599–605; book/ch07-gravity.md:118–122, where the interior is "the secondary hidden sector") is a self-consistency exercise. It "is *not* a claim that external observers' emergent quantum descriptions acquire BH-horizon-specific features" (L599).
- §8.7: the derivations "all take a smooth Lorentzian metric as given" (L691) and are "not a claim to have derived general relativity from the substratum" (L697).
- "singularit" occurs in neither papers/GR.md nor papers/Main.md.

**The input against this.**
- **Conflations avoided:**
  - horizon versus singularity: separate rows (input L118, L119) and "possibly, but not automatically" (L112) — S3, control 6, L231;
  - fluid singularity versus black hole (L30);
  - the Clay problem versus an interior singularity (L121);
  - the BH reading's need for derived causal structure (L157; S5's first item is open at L, since horizons enter from GR).
- **A soft conflation made.** Row 3's "Causally inaccessible sector" gives the black-hole interior the role of an OI hidden sector. In the corpus the external observer's partition is the cosmological horizon. The interior is a secondary partition only in a self-consistency formalism, and it yields no OI-specific black-hole signature (GR L597: echo search null). A "causally inaccessible region" (GR's causal structure, taken as given) and an "OI hidden sector" (an epistemic partition with C1–C4, GR L46–52) are different objects. The input runs them together, as §4 of the input runs the map's complement together with OI's hidden sector (§3.2).
- **Fluids and horizons in the corpus.** The only touchpoint is Unruh's sonic analogue (GR.md:883) and "analogue gravity systems where the hidden sector capacity is tunable" (GR.md:607). Both are compressible-fluid analogues, distinct from the fluid/gravity reduction and from incompressible NS (C51).

### 1.5 Remaining claims (NS.1): what the table compresses

- **C1–C2:** the "bridge" credited to established physics joins horizons and fluids [L, unverified]. Nothing at L joins either to the hydrodynamic branch, and the corpus never links NS singularities with horizons.
- **C20–C22:** the separation of velocity from energy, and the "OI hypothesis" drawn from it, need no OI premise: the kinematic family [X ns4] and the null model [X ns5] show both.
- **C25:** "if the observed values are finite" is automatic for real-valued observations, and reversibility plays no role [X ns4 F1].
- **C40:** "real" holds exactly, for one variable at one instance; statistical closure is HO.
- **C53, C61, C62:** see §1.1(b) and §1.3. **C57, C65:** see §4.

### 1.6 Corpus markers found on the way (record-only; assumption-watch; nothing edited)

1. PROGRAMME L231 mentions H-A, H-B and H-E, not H-D or H-F, and ROADMAP has no H-D or H-F row (L1158–1233). H-F names "which later action carries out the refresh of `../PROGRAMME.md` §8" as an owner decision not made (H-F result L1007). The labels in L231 are still correct.
2. PROGRAMME L143, "a continuum singularity need not be a substratum singularity", is already exemplified by closed truncations of a non-OI PDE [X ns5]. An S1 result for OI would carry H4–H7's content; S1's OI-specific value lies in S2/S2a with discriminating controls (§3.3).
3. hypothesis L34, L38: "hidden relative to the map" makes S2a's hidden sector the MZ complement of that map. Transfer into such a complement exists for every nonlinear cascade [X ns5 C2]. OI-specificity must come from the substratum, the map and a control, or from the theorem control 2 (L72) asks for.
4. H-B preregistration L157–160, L214: the exact script that found HB3-a and ran the bounded search at L = 2, 3 is not in the tree. The kernel carries the witness; the bounded search is unreplayable at L.
5. Structure.md:496 tabulates horizon holography as "Yes | Structural consequence of partial-trace observation". GR L701 states the 1/4 coefficient "carrying the same condition together with the horizon and frame conditions of §2 and §8.5" (Structure L452 mentions the horizon conditions). This is a status cell without its conditions: a §A.25/§A.30 item for an owner-authorized change.

## 2. Mathematics (NS.4)

All results below are [X] in `ns4_scaling.py`: run 2, 14/14; replay byte-identical. Run 1 failed one check on a
simplification, §6. Profile: f = curl(0, 0, G), G = e^{−|y|²}, so f = (−2y₂G, 2y₁G, 0); ε > 0 and x₀ are symbolic.

**2.1 The scaling family (C29–C31).**
- **Divergence:** div f = 0 and div u_ε = 0 identically (S0, S1).
- **L² norm:** ‖f‖₂² = ‖u_ε‖₂² = √2 π^{3/2}/2 for every ε > 0, at x₀ = 0 (S2) and at x₀ = (1/3, −2, 5/7) (S2t).
- **Peak:** sup|f| = √(2/e), attained where y₁² + y₂² = 1/2 and y₃ = 0. The reason: g(r) = 4re^{−2r} has its only critical point at r = 1/2, with g″ = −8/e, and |f|² = g(r)e^{−2y₃²} ≤ g(r).
- **Peak of the family:** ‖u_ε‖_∞ = ε^{−3/2}√(2/e), checked exactly at x₀ + εy* (S3). It tends to ∞ as ε → 0⁺ (S4). The input's ‖u_ε‖_∞ = ε^{−3/2}‖f‖_∞ holds because x ↦ (x − x₀)/ε is a bijection of ℝ³ [W].
- **Countercontrols:**
  - exponent −1 gives ‖·‖₂² = ε‖f‖₂² (CC1);
  - in d = 2, exponent −3/2 gives π/ε while −1 = −d/2 gives π (CC2);
  - the non-solenoidal profile ∇G loses divergence-freeness under the same rescaling (CC3).

**2.2 What the family is and is not (C32).**
- **Exponent.** ε^{−3/2} is the L²-critical exponent in d = 3 (−d/2) [W; X CC2]. It is not an NS symmetry.
- **The NS symmetry** is u_λ = λu(λx, λ²t), p_λ = λ²p(λx, λ²t). Each of ∂_t u, (u·∇)u, νΔu and ∇p scales by λ³ (S6: exact on two concrete smooth test pairs; the chain rule [W]). Energy scales as ‖λf(λx)‖₂² = ‖f‖₂²/λ (S6), so NS-self-similar concentration to scale 1/λ needs only energy ‖f‖₂²/λ → 0. The energy is supercritical, and an energy bound alone does not exclude blow-up [W].
- **Enstrophy.** ‖∇u_ε‖₂² = ε^{−2}‖∇f‖₂², with ‖∇f‖₂² = 5√2π^{3/2}/2 (S5).
- **Energy budget.** For a smooth solution, d/dt ½‖u‖₂² = −ν‖∇u‖₂² + ∫F·u, with F the external force [W: multiply by u and integrate; the nonlinear and pressure terms vanish by incompressibility]. An unforced flow passing through the family at scale ε therefore dissipates at rate νε^{−2}‖∇f‖₂², and with energy about ½‖f‖₂² available it can stay near scale ε for at most a time of order ε²‖f‖₂²/(2ν‖∇f‖₂²). A forced flow has the source ∫F·u. The family is kinematic, as the input says.

**2.3 Finite state space, boundedness and non-uniformity (C25, C26, C33).**
- **F1 [X + W].** All 256 maps on a 4-element set were checked (24 bijections), from every start. The orbit maximum of the observation over 4 steps equals that over 64 steps. In general, an orbit in a finite set visits at most |S| states, so sup_t ‖P(T^t s)‖ is a maximum over at most |S| values, for every map, reversible or not. "Bounded at fixed resolution" is true and says nothing about the dynamics.
- **F2 [X], an exact finite divergence-free family.**
  - Setup: N = 4^m and h = 1/N on (ℤ_N)³, with u_N = curl_h(ψe₃), ψ = 2^{m−1}δ₀, and forward differences.
  - Exact values: the discrete divergence is 0; the discrete energy is 1 for every m; sup = 2^{3m−1} = N^{3/2}/2 (4, 32, 256, 2048, 16384 for m = 1..5).
  - Dynamics: translation by one cell is a bijection of the finite torus and preserves both. The family is bounded at each N and unbounded in N.
- **CC4 [X], uniform without concentration.** The sampled field (sin 2πx₂, 0, 0) has energy exactly 1/2 and sup exactly 1 for N = 4, 8, 16.
- **Concentration is necessary [W, Chebyshev].** With discrete energy ≤ E, the volume where |u_N| > M is at most E/M². A uniform energy bound with sup_N ‖u_N‖_∞ = ∞ therefore puts the large values on sets of vanishing volume.

**2.4 Dimensional bookkeeping (C47–C50) [W].**
- In D-dimensional spacetime, a horizon is a null hypersurface of dimension D − 1 and its spatial cross-section has dimension D − 2. A horizon fluid lives on that cross-section.
- So D = 4 gives a 2D fluid (on S² for Schwarzschild), and a 3D fluid needs D = 5.
- The Clay problem is posed on ℝ³ and on T³ [L, unverified].
- As recalled, incompressible NS in 2D with smooth data is globally regular [L, unverified]. A 4D horizon fluid then admits no 3D-type blow-up at all, which supports the input's own caveat (C50).

**2.5 Blow-up and closure failure, kept distinct (hypothesis L75), with exact instances.**

| case | closed? | regular? | instance |
|---|---|---|---|
| closure failure, no blow-up | the coarse variable does not close | fields bounded (Boolean occupations) | HB3-a [K HexLatticeGas.lean:989; X ns2 A1–A5]; H-A H3a [K HydroSourceAudit.lean:863; X ns2 H1] |
| blow-up, no closure failure | inviscid Burgers is a closed PDE | gradient blow-up at t = 1 | [X ns5 B1–B5] |
| closed and regular | every Galerkin truncation | regular for all t | [X ns5 G1–G5], with N = 2 exact; [W] for every N |
| projected exact dynamics | not closed: the rate of a₁ depends on a₂, a₃ | smooth for t < 1 | [X ns5 C1, C2] |

The input keeps the two apart in its table (L116–117) and in L106. Its next question (L108) joins them without naming
a severity measure (hypothesis items 5–6, L35–36). Exact non-closure is generic (H-A's linear wave rule), so a measure
that does not separate OI from generic coarse-graining would not discriminate.

## 3. The mechanism and the null model (NS.5)

**3.1 The null model.** All [X] in `ns5_null_model.py`: run 2, 19/19; replay byte-identical. Run 1 failed a
preregistered claim, §6.

*(a) The continuum equation.*
- Equation: inviscid Burgers, u_t + uu_x = 0 on the circle, with u(x, 0) = −sin x.
- Exact solution: the characteristics x = ξ − t sin ξ, u = −sin ξ (B1, B2).
- Blow-up: the Jacobian 1 − t cos ξ ≥ 1 − t > 0 for t < 1 and vanishes at (ξ, t) = (0, 1). So u_x(0, t) = −1/(1 − t) → −∞ as t → 1⁻, and t* = −1/min u₀′ = 1 (B3).
- Bounded velocity: |u| ≤ 1 throughout (B4). The singularity is a gradient blow-up, i.e. shock formation.
- Energy: ∫u² dx = π for every t < 1 (B5).

*(b) The truncations.* Sine–Galerkin u_N = Σ_{k≤N} a_k(t) sin kx, with a_k′ = −(1/π)∫u_N(u_N)_x sin kx dx; the odd
subspace is invariant.
- **Energy and reversibility.** The energy πΣa_k² is conserved identically, N = 1..5 (G1). V(−a) = V(a), so a(t) ↦ −a(−t) maps solutions to solutions (G3).
- **Exact N = 2 solution.** a₁′ = a₁a₂/2, a₂′ = −a₁²/2. From a(0) = (−1, 0) the solution is a₁ = −sech(t/2), a₂ = −tanh(t/2). N = 1 is stationary (G4).
- **Bounded gradient.** Along the N = 2 solution, a₁² + a₂² = 1 and the gradient at 0, a₁ + 2a₂, stays in [−√5, −1] for all t ≥ 0 (G5). The PDE from the same data has −1/(1 − t).
- **General N [W].** A polynomial ODE on the compact sphere Σa_k² = 1 has global solutions. Also ‖∂_x u_N‖_∞ ≤ Σk|a_k| ≤ (N(N+1)(2N+1)/6)^{1/2}: finite for each N, growing with N.
- **Liouville.** Volume preservation holds for the full mean-zero sine–cosine truncation, N = 1..4; its odd subspace is invariant and carries the sine field (G2). It fails for the flow restricted to the odd subspace (divergence a₂/2 at N = 2 and 3; G2-odd). Run 1 had preregistered Liouville on that subspace and failed (§6).
- **Countercontrols.**
  - y′ = y², y(0) = 1 blows up at t = 1. It is exactly the gradient law along ξ = 0, with w = −u_x (G6). Closedness and finiteness alone do not give regularity; the conserved energy on a compact sphere does.
  - The truncation (a₁a₂, −a₁²/2), which breaks the triad antisymmetry, does not conserve energy (G7).

*(c) Closure failure of the projected exact dynamics.*
- **Rate.** For u = a₁ sin x + a₂ sin 2x + a₃ sin 3x the exact rate of a₁ is (a₁a₂ + a₂a₃)/2. At a₁ = −1 it is 0 for (a₂, a₃) = (0, 0) and 1/4 for (−1/2, 0): the same resolved state with a different resolved rate (C1).
- **Flux.** The resolved-energy flux d(πa₁²)/dt = πa₁²a₂ + πa₁a₂a₃ is not identically 0, while the N = 1 truncation has none (C2).

This is Mori–Zwanzig memory and transfer with no OI content. M1 checks the exact projected identity for a 5-cycle; the
Markov part alone fails (CC-M).

*(d) A fully observed finite bijective family with the boxed S1 shape (F1).*
- **System.** N = 4^m. The states are j ∈ ℤ_{m+1} with Φ_N(j) = j + 1 mod (m + 1), a bijection. The observation is the field (8^j, 0, 0) on a cube of side 4^{−j} = 1 − t_j at t_j = 1 − 4^{−j}. The time map n(t) saturates at n(1) = m.
- **Nothing hidden.** P_N is injective.
- **Energy and peak.** The discrete energy is 1 in every state. The sup over the orbit is 8^m = N^{3/2} (8, 64, 512, 4096): finite at each N, unbounded in N.
- **Resolution independence.** The field at t_j is the same for every N ≥ 4^j.
- **Countercontrol.** The unconcentrated cube has energy 1 and sup 1 for every N (CC-F).

Not exact here, and used by no check: convergence of the Galerkin truncations to the smooth solution for t < 1, and
their thermalization after t* instead of convergence to the shock [L, unverified].

**3.2 What this does to S1 and to the attribution claim.**
- **Finite boundedness is automatic.** "Regular at every finite resolution" holds for every finite state space [X ns4 F1; W].
- **The S1 shape needs nothing hidden.** "Regular finite approximants, a singular continuum limit and a uniform energy bound" is realized by:
  - a fully observed finite bijective family, exactly [X ns5 F1];
  - the closed, reversible, energy-conserving truncations of a non-OI PDE, whose approximants have no complementary sector [X ns5 G; convergence L, unverified].

  The route "S1 shape ⇒ hidden-sector transfer" is **refuted**. The label is "route refuted", not INDEPENDENT.
- **Two notions of "hidden" (exposed hidden assumption; NEW for this review).**
  - (i) The complement of a coarse-graining or truncation map. This is Mori–Zwanzig's notion and the note's own definition for S2a (hypothesis L34, L38). Transfer into it exists for every nonlinear cascade [X ns5 C2].
  - (ii) OI's observer-level hidden sector (Main's partition; GR L40–52).

  "Transfer into an OI hidden sector" (input L56) asserts (ii), while every computation the input points to concerns (i). Control 2 (L72) requires a theorem identifying the objects first. Assumption-watch markers: hypothesis L34/L38 and PROGRAMME L143.
- **S1 remains a meaningful obligation for OI.** It would show that OI's own map reaches a singular continuum field. Its interpretive sentence (L143) is already true generically, so its OI-specific value has to come from H4–H7 and from S2/S2a under discriminating controls.

**3.3 What an OI-specific attribution theorem must add beyond truncation.**
1. **A specified projection.** The H4 map from an admissible OI substratum, with all five skeleton items fixed (lattice spacing, time step, field lift, carrier growth, convergence topology), and a stated regularity class (hypothesis L55). Not a truncation chosen for convenience.
2. **A specified hidden sector.** Either the complement of that map, in which case the claim concerns that map and must beat the controls below; or OI's observer-level hidden sector, which needs the identifying theorem of control 2 first.
3. **A transfer quantity with an exact balance law at every finite resolution** (control 4, L74): change of resolved quantity = −transfer + resolved terms + external force, elementwise on the substratum, before any limit.
4. **A closed-model control.** The same target reached by a closed truncation, or by a fully observed family. The attribution must be false, or measurably different, there; otherwise it is a statement about truncation.
5. **A non-OI microscopic control with a complement.** A reversible lattice gas with the same target and without OI's premises (FHP-type; PROGRAMME L49 as precedent [L, unverified]). Identical transfer statements mean the result is coarse-graining-generic, not an OI attribution.
6. **Forcing as an explicit source.** A forced target's external force enters the resolved balance as a source, never as transfer (C58).

**3.4 The decision rule a future probe needs.** All objects are frozen and hashed before any computation.
- **Frozen objects:**
  - O1, the substratum family (S_ε, Φ_ε), admissible under the owner's rulings on the A5 class and the carrier;
  - O2, the map P_ε with its five scaling items;
  - O3, the resolved/hidden split;
  - O4, the transfer functional and its balance law;
  - O5, the regularity or closure criterion (hypothesis L36);
  - O6, the continuum target, a singular solution, with its force.
- **Controls** (all green before any verdict prints):
  - K1: O4's balance law holds exactly, elementwise, at every tested ε;
  - K2: P_ε(Φ_ε^{n(t)}s_ε) converges to the target in O2's topology for t < t*, with a rate;
  - K3: byte-identical deterministic replay.
- **Countercontrols** (each must behave as stated):
  - CC1, a closed truncation reaching the same target: the attribution fails there, or its transfer measure is identically 0 while the OI family's is not;
  - CC2, a fully observed family (P injective) with the same boxed shape: the same requirement;
  - CC3, a non-OI reversible microscopic model with a complement and the same target: the statement's OI-specific part must distinguish OI from it, or the result is reported coarse-graining-generic;
  - CC4, for a forced target, the force relabelled as transfer: this must break K1;
  - CC5, a randomized split O3 of the same dimensions: the transfer statement must change, or it does not depend on the split.
- **Outcomes**, relative to the base at the time:
  - DERIVED: the attribution follows for an admissible OI substratum from certified premises, with K1–K3 green and CC1–CC5 discriminating.
  - CONDITIONAL: it needs named principles (an H3 equilibrium condition, H4 choices), each stated and tested for restatement.
  - INDEPENDENT: only with a model satisfying every certified premise bearing on the target (an admissible substratum and map) in which the singular limit occurs without the transfer, or the transfer without the singularity; scope stated.
  - UNRESOLVED: otherwise.
  - "Route refuted": for a model of a route's premises in which its conclusion fails, as §3.1 is for the S1-shape route.

## 4. The proposed theorem and test (NS.7)

**4.1 The input's "first theorem" (input L159) against the note's target (hypothesis L55, with L9, L36, L75).**

| element | the note | the input | assessment |
|---|---|---|---|
| substratum | "a stated OI substratum" | "globally regular, reversible OI dynamics" | unspecified; control 2 (PROGRAMME L217) and the A5 question (§1.3) decide which |
| map | "a stated continuum map"; gate L9 | absent from the theorem | the gate is stated only for the test (input L145, "once a continuum map exists") |
| regularity class | "a stated regularity class"; item 6, L36 | absent | the failure criterion is unspecified |
| event | "finite-time loss of regularity or hydrodynamic closure" | "a singular continuum hydrodynamic description" | closure dropped; L75's distinction kept in the input's table, not in the theorem |
| coexistence | "determine whether … can coexist" | "can emerge" | an existence framing; generic for non-OI truncations [X ns5] |
| attribution | a "quantitatively identified transfer" … "necessary, sufficient, both, or neither" | "precisely attributable—or provably not attributable—to a specified hidden-sector transfer" | four outcomes collapsed to two |
| hidden sector | "relative to the proved observation/coarse-graining map" (L38) | "hidden-sector transfer"; "an OI hidden sector" (L56) | notion (ii) asserted for computations about notion (i) (§3.2) |

**What the input adds.**
- A named target for the test: a known singular NS profile.
- The forcing caveat (C58), consistent with controls 3–4 and worth keeping.
- The dimension caveat on the gravity side.

None of these changes the theorem's content.

**Gating.** The input respects the gate in the test, not in the theorem (input L159) and not in its §2 or §4. Its
route order (H3–H7, then S1 and S2a, then S3–S5) fits PROGRAMME L127 but skips H1–H2 and S2.

**4.2 Labels relative to L (amendment 2).**
- **T-NS (framework-specific): UNRESOLVED,** and not statable at L. There is no map (H4 HO; H-E's HE5 "unstatable"), no Euler or NS limit (H5–H7 HO), and no transfer functional. There is neither a derivation nor a model of every certified premise bearing on the target, since L defines no OI continuum map. So it is not INDEPENDENT.
- **The emergence half, for non-OI systems:** holds [X ns5]. Its OI content can come only through the map, i.e. through H4–H7.
- **The generic route,** S1 shape ⇒ attribution: route refuted [X ns5 F1, G; ns4 F1].
- Nothing is INDEPENDENT.

**4.3 Is the "most valuable new test" (input L145) executable at L? No.** Missing objects:
1. **The continuum map P_ε.** Four of its five scaling items are unfixed (H-B result L313–319; ROADMAP L1219–1223).
2. **A 3D carrier with a hydrodynamic limit.**
   - The wave representative faces the linearity gate (H-A).
   - H-B's gas is 2D and lies in the ¬A5 class (H-B result L53–62, L369–372).
   - No Euler or NS limit is derived (H5–H7 HO).
   - The carrier question is an open owner decision (H-F result L1008).
3. **The hidden-sector split and a transfer functional with a balance law** (hypothesis items 4–5, L34–35; controls 3–4, L73–74).
4. **A known singular 3D NS profile.** None is known for the unforced equations [L, unverified]; the forced construction is NOT CHECKABLE AT L.

Discrimination additionally needs the controls CC1–CC3 of §3.4. With all of these the test is round S-A (PROGRAMME
L204–206) with a named target, plus S2a: what the programme already plans, after H-C.

## 5. What is not claimed

- **The 2026 events.** Nothing about the truth of the announcement, the Clay statement, or any proof or formalization; nothing about whether a forced or unforced 3D NS blow-up exists.
- **The literature.** Nothing about the 2011 reduction or the sphere/censorship work beyond the input's own words; the attributions in §1.2 are [L, unverified] and no verdict relies on them.
- **The scope of "route refuted".** It covers the route's stated premises (finite regular approximants, a singular limit, an energy bound) and not the framework. The null model does not show that OI cannot attribute a singularity to hidden-sector transfer; it shows that the S1 shape cannot do so alone, and what an attribution must add.
- **Galerkin convergence.** Nothing about Galerkin truncations converging to the Burgers solution, or thermalizing after t*: [L, unverified], unused.
- **Liouville.** The finding that Liouville fails on the odd invariant subspace is exact for the sine–Galerkin restriction of inviscid Burgers at N = 2 and 3, and claims nothing beyond that.
- **The kernel results.** No claim that HB3-a, H-A's H3a or SM Theorem 1a is wrong. The [X] re-evaluations are instance-scoped and add nothing to their [K] status.
- **A5.** No status is asserted for the kernel or the manuscript A5 relative to either branch; H-D's labels are quoted, not extended.
- **Repository.** No edit; the §1.6 markers are record-only. No Lean was written or rebuilt: [K] rests on the build route at L.
- **Evaluative claims.** No verdict on the input's evaluative sentences (C59) beyond NOT CHECKABLE AT L.

## 6. Evidence log

Environment: Python 3.11.15, sympy 1.14.0. Each script was run as `python3 -I -B <script>` from
`pt/audit/reviews/NS/`, with stdout to `<name>.out` and stderr plus an appended exit line to `<name>.err`. Each final
version was replayed into `<name>.replay.{out,err}` and compared with `cmp`. Failed runs are kept as `<name>.run1.*`.
Every decision rule was written in the script header before its first run. The one amendment, to ns5 after its run 1,
is marked in that script's header and in the table below. Nothing nondeterministic is printed.

| script | checks | runs | outcome | replay |
|---|---|---|---|---|
| `ns2_hb3_recheck.py` | 12 | 1 | 12/12; VERDICT-HB3 and VERDICT-H3A printed | byte-identical |
| `ns4_scaling.py` | 14 | 2 | run 1: 13/14, S2t FAIL (harness: sympy left erf + erfc unsimplified), verdict withheld; run 2 (`erfc` rewritten as `1 − erf`, an exact identity): 14/14 | byte-identical (run 2) |
| `ns5_null_model.py` | 19 (run 1: 18) | 2 | run 1: 17/18, G2 FAIL (my preregistered Liouville claim is false for the odd subspace), verdict withheld; run 2 (amendment written into the header: G2 on the full truncation, G2-odd records the fact): 19/19 | byte-identical (run 2) |

Pre-run edits made before any run are recorded in NOTES.md: ns4 (S6 on concrete test pairs, F1, CC4 exactness) and
ns5 (Part F conjunction, G5 exactness, CC-F, header wording).

| file | sha256 |
|---|---|
| `ns2_hb3_recheck.py` | `873599a549991020a9ce325a5ffc940a979037ef27a9ca9d481a15d1a02078ec` |
| `ns2_hb3_recheck.out` = `.replay.out` | `b7de57d062a70e77fa6b1b962d9f669978eea49e06c45b09bf985646476c47f4` |
| `ns4_scaling.py` | `46c9e10ebe4dbb5bc9c7e2bc28888aa0b65170140740235515a30ed621d147d4` |
| `ns4_scaling.out` = `.replay.out` | `afc8af7dd9371fb557995ac6c739c135adbc6aeafba1696ae51c9fbd51cc2ae6` |
| `ns4_scaling.run1.py` | `36247dcace7d188abc442685de0babf80f0e00df9407d247d53e8f5a22b56078` |
| `ns4_scaling.run1.out` | `cb06a7d83d3c2924cee18c514514ac45587f95832255f79a91ef649bc1723849` |
| `ns5_null_model.py` | `d12f32fbdcf3dc6d8fcf9d06d064900318ea598bb52c60c18f9740853cae0856` |
| `ns5_null_model.out` = `.replay.out` | `2f6fc1103a3d7d31087e8cca7e5a3a7f79b872b421b177a12cad994a67a7ba4e` |
| `ns5_null_model.run1.py` | `1e2ae4ec9d2d8d830c5ecb3ae493e3bca343282cc58b4abdf3086dd3826286da` |
| `ns5_null_model.run1.out` | `c91090b8b9ce72bd42f54de80bf8a71fe624079d14dca8e0014c833f653601db` |
| every `.err`, `.replay.err` and `.run1.err` (content `exit 0`) | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |

Non-script checks: `git grep` literature and topic searches at L (§1.2); reads of every cited range; the [K] build
route (§1.1(c), §1.2). Read-only git commands only.

## 7. Integrity

**Start: 12:36:14Z, written first into a freshly created, empty `pt/audit/reviews/NS/`** (`.start_marker`, written
by one mechanical shell command).
- **Manifests:** `sha256sum -c --quiet` was silent, exit 0, on `inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4` (in `pt/`) and `ns.manifest.sha256` (in `pt/audit/stage3-inputs/`).
- **Base:** `git -C pt/base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`. `git status --porcelain` was empty; it ran with `GIT_OPTIONAL_LOCKS=0`, so status refreshed no index. No bytecode under `pt/base/`.
- **Protocol files:** the seven hashes matched (`PROTOCOL.md`, both amendments, `PROTOCOL-STAGE2.md`, `PROTOCOL-STAGE2-DS.md`, `PROTOCOL-STAGE3.md`, `PROTOCOL-NS.md` = `PROTOCOL-NS.sha256`).

**End: 13:22:23Z, every start check repeated.**
- **Repeated checks:** all seven manifests silent, exit 0; HEAD `9f9f8257…`; status empty; no bytecode under `pt/base/` or under this directory; all seven protocol hashes match.
- **Files newer than `.start_marker`** under `pt/`, excluding `pt/U/`, `pt/X/` and `pt/audit/`: **none**, with those subtrees pruned unconditionally. `pt/` itself is unchanged since 11:23:27Z. No anomaly, so nothing was quarantined.
- **Hashes:** every hash in §6 was re-verified against the files, 10/10 OK. The three `.replay.out` equal their `.out`, and all eight `.err` files hash `28d3b9e8…`.
- **Observation, not an anomaly.** Inside the coordinator's area, which the protocol excludes from the sweep, three new top-level entries appeared after the start marker: `pt/audit/U` (13:14:33Z), `pt/audit/NS` (13:21:19Z) and `pt/audit/X` (13:22:19Z). Only their names and mtimes were listed; none was read. They are not this thread's: every write of this thread is under `pt/audit/reviews/NS/`.
- **Directory contents:** only files this thread wrote: `.start_marker`, `NOTES.md`, `RESULT.md`, the three scripts with their `.out`, `.err`, `.replay.*`, and the two kept failed runs `*.run1.{py,out,err}`.
- **Limits observed:** no git write, branch, PR, CI, GitHub, fetch, search, publication or agent.
- **Not read:** `pt/U/`, `pt/X/`, `pt/audit/U/`, `pt/audit/X/`, `pt/audit/aborted-launches/`, `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/reviews/coherence-note/`, any `pt/audit*-replay/`. The `qsd_owner_*` files in `pt/audit/stage3-inputs/` (not NS inputs) and the new `pt/audit/NS` were not opened either.

The sha256 of this file is reported with the final reply, since a file cannot contain its own hash.
