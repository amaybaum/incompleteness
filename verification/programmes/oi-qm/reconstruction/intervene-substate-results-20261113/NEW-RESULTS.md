# INTERVENE-1 / SUBSTATE-BRIDGE-1: the option-(c) carried results

**Standing.** This record carries the results of the INTERVENE-1 (#1230) and SUBSTATE-BRIDGE-1
(#1232) drafts that are not already on `main`, in the set fixed by the owner decision #1169
c.6855167580 (`PROVENANCE.md`). They are research records, not established claims (§A.46 items 1
and 3). Each is a paper argument [A], not kernel-checked, and conditional on the hypotheses stated
with it. Model-written reviews read every result (`PROVENANCE.md` §2–3); the steps hand-checked
there, and those hand-checked in this record, are cited at each result. None of these reviews is
verification (§A.46 item 7). The accountable Issue is #1169. The open gaps are listed in
`DEPENDENCIES.md`, and verification would be an independent non-model review or a kernel
formalization; T5(c), E1, E2 item 4 and L1 are named kernel targets (I:294, S:347). None supplies an operation
that is physically reachable under the currently demonstrated OI premises (REC-1 Q2-F or Q2-P);
the constructive items are definable or representable (Q2-A), and the remainder are upper bounds,
classifications, a definition with a countercontrol, and an open obligation. Correctness bands are
unchanged: every result here is on the consistency axis (§A.23).

**Pins.**
- `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`. "Main:n" is line n of `papers/Main.md` at
  that commit; "OB/" is `verification/lean-mathlib/OIBridge/` at that commit.
- "I:n" is line n of
  `verification/programmes/oi-qm/reconstruction/drafts/intervene-1-20261111/INTERVENE-UNIT1.md`
  at `ea12fde1bbc4b546f4690bf89817971796aeb501` (blob `06f148e0`).
- "S:n" is line n of
  `verification/programmes/oi-qm/reconstruction/drafts/substate-bridge-1-20261111/SUBSTATE-BRIDGE-UNIT1.md`
  at `86a413c88cd14d344aa41b6f47885aeb24da6910` (blob `9ff0f077`).
- "R3:n" is line n of
  `verification/programmes/oi-qm/reconstruction/drafts/reconcile-1230-1232-20261113/RECONCILE-r3.md`
  at `703ae20e57f9ffeb0eb458ec688883b3fc64a632` (#1271); "RV:n" is line n of `REVIEW-r1.md` in the
  same directory at the same commit.
- "RS/" is `verification/programmes/substratum/recursive-substates/`; "CS/" is
  `verification/programmes/substratum/continuous-substates/`.

**Evidence tags.** [K] kernel theorem or definition on `main` (statement read; build not rerun).
[P] manuscript on `main`. [W] research record on `main`. [D] draft off `main`. [A] paper argument,
hand-checked, not kernel-checked. [X] a generic exact check of the drafts, off `main`
(`DEPENDENCIES.md` row X). [L] external literature, recalled, not read first-hand.

**Text conventions.** Statements and proofs are copied from the drafts. A wording change is marked
[Δn] at the place it occurs; `CHANGES.md` lists every Δ with its reason. Paragraphs headed *Hypotheses*,
*What it adds*, *Scope* (unless marked copied), *Support layer*, *Provenance*, *Hand check* and
*Arithmetic* are written for this record from the sources they cite; they are not draft text. Copied text that cites
"Main:n" carries the line at `c3b5f37a` (re-pin Δ1); copied cross-references to draft sections name
the section of this record where the target is carried, or the draft line where it is not (Δ19).
Inside a quotation, words inserted or replaced by this record are in square brackets, apart from
re-pinned Main lines (Δ1) and the SM anchor of Δ2.

***

## 0. Definitions and hypotheses used below

### 0.1 Hypotheses [Δ3]

**Vocabulary** (REC-1 r7, `research/rec-1-1169-20261113` @ `9f7d2612`, `REC-1-r7.md`:94–104 [D];
restated so that this record does not depend on it). Q1-D: the premises are properties of the
substratum dynamics or of stated substratum posits, and hold for every observer interface. Q1-I: a
premise describes one observer interface (state-space identification, access, record class, effect
class, control schema), and the premise is named. Q1-μ: a premise is a property of the initial law.
Q2-A: a mathematically definable construction or representation. Q2-F: an operation reachable under
one fixed dynamics from stated initial or boundary conditions. Q2-P: a physically derived embedded
access or control family (dynamics and conditions both sourced in OI).

| ID | Content (copied) | Status | Q1 type (REC-1 r7 vocabulary) | Source |
|---|---|---|---|---|
| H3 | "Physical states are probability laws μ ∈ Δ(Ω); there are no amplitudes." (I:68). On a general carrier: "Physical states are probability measures on `Ω_S × R`." (S:80) | posited (part of P-CONF) | the state-space premise (laws on configurations, route C's identification) is Q1-I, as REC-1 r7 classes the same kind of result (its rows 9 and 18) | Main:58 (the measure as a realization datum); Main:718 |
| H4 | "The observer is a proper subsystem. Its records are coordinates of the configuration: Ω = Ω_V × Ω_H, extended by registers as needed." (I:69) | justified | not typed by REC-1 r7 or by the reconciliation | Main:42 (Definition), Main:48 (Lemma 2) |
| H6 | "Readout conditions on a value of a configuration coordinate: μ ↦ 1_{r=k}·μ." (I:71) | justified | not typed | Main:42; Main:590 (record projections) |
| H-IND (H11) | "A procedure fixes a kernel κ(r ∣ s): the conditional law of all degrees of freedom r outside the identified carrier (apparatus, registers, environment, the observer's own state), given the carrier configuration s at the procedure's start. κ is the same for every input law." (I:76) | posited; the defining condition of route C. Where it fails, the route is C-dyn (I:31). | Q1-I/Q1-μ is the reconciliation's reading (R3:43, R3:83); REC-1 r7 has no row for H-IND | I:76. Analogous to MECH-2's H-LIFT (`verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md`:319–321 [W]); the exact relation is not audited (I:299; R3:83). |
| P-CONF∞ | "`(Ω_S, 𝒮)` and `(R, ℛ)` are measurable spaces; `Ω_S` is the identified carrier (finite with the discrete σ-algebra in the case of the brief), `R` collects every other degree of freedom and may be infinite, a continuum or an inverse limit. `φ : Ω_S × R → Ω_S × R` is measurable for the product σ-algebra. Physical states are probability measures on `Ω_S × R`. Records are measurable coordinates (H4, H6)." (S:80) | posited; measurability is a hypothesis | its state-space clause is Q1-I, as for H3. The finite clauses H1–H2 of P-CONF (finite Ω; φ a bijection) are Q1-D (ledger (ii), Main:724); no carried result uses them (RV:153) | S:80 |

**Scope of results stated under these hypotheses [Δ4].** A result stated under P-CONF∞ (or H3), H4
and H-IND holds for every observer protocol within the named route: it does not depend on which
observer access model is used inside that route. It is conditional on those hypotheses, with the Q1
types above, and it is not a consequence of the two OI axioms of Main §1.2.

### 0.2 Kernel objects (all on `main`)

| Object | Anchor |
|---|---|
| `PreservesDiag Φ`: Φ maps every diagonal matrix to a diagonal matrix | OB/DiagonalTheory.lean:68 [K] |
| `IsMonomial K`: K = permMatrix σ · diagonal d | OB/SubstratumInterface.lean:75 [K] |
| `substratumClass` = the monomial class | OB/StructuralClosure.lean:180 [K]; `substratumClass_arch` :231; `substratumClass_labelInvariant` :275 |
| `Architecture` (fields `one`, `mul`, `smul`, `proj`, `block`) | OB/ImplementationLocality.lean:506–516 [K] |
| `InstAvail` (constructors `op`, `readout`, `coarse`, `bind`, `discard`) | OB/ImplementationLocality.lean:268–289 [K]; `instAvail_mono` :305 |
| `genTheory 𝓘 arch` | OB/ImplementationLocality.lean:852 [K] |
| `substratumTheory = genTheory substratumClass substratumClass_arch` | OB/RouteB.lean:284 [K] |
| `LabelInvariant` | OB/ImplementationLocality.lean:364 [K] |
| **FI-1** for a generating architecture 𝓘 on carrier S: ∃ K on S×Fin 1 with 𝓘 K and ¬IsMonomial K. This is the conclusion of `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52 [K]); GR:266 names it "a non-monomial admissible operator at level one" [P]. | definition anchored on `main` (`DEPENDENCIES.md` row B) |
| **CM**, the column-monomial class: at most one nonzero entry in each column (I:157). The predicate is `ColMonomial` (OB/SubstantiveCensus.lean:651 [K]); `preservesDiag_conjChannel_of_colMonomial` (:654 [K]) is its diagonal-preservation lemma. | |

### 0.3 Route E_f terms [Δ5]

- **Frame matrix.** For a linear injective identification L of encoded states with laws on Ω_enc,
  "If a branch T of a family in 𝒦 induces the encoded map E by L∘E = T∘L, then the frame matrix of
  E is T" (I:143).
- **E_f classical class.** For a linear injective L that **spans** ℝ^{Ω_enc}, the maps whose frame
  matrix is entrywise nonnegative (APPROX r4a §4.2, :373–375, there for the spanning R1 and SIC
  identifications; I:123). Spanning makes the frame matrix unique (I:143). Without spanning the
  frame matrix of a map is not unique, and the class is not fixed by the map (R3:44); G1 (§3) is the
  statement for that case.
- **NX-1** (I:123): "some valid native procedure induces a transformation at an ε-independent
  positive distance from the route's classical class"; on E_f the class is the one above [Δ28].
- **T3** (context; not carried, §7). "Let L be linear and injective with Span(L(encoded states)) =
  ℝ^{Ω_enc} (informationally complete), and let H-LIFT hold. If a branch T of a family in 𝒦 induces
  the encoded map E by L∘E = T∘L, then the frame matrix of E is T, which is unique by injectivity
  and spanning, and T ≥ 0 entrywise (T0; T1 for 𝒩). So E lies in the E_f classical class. ∎"
  (I:143). T3 extends MECH-2 Lemma F(b) (`mechanism-2-20261108/DESIGN.md`:325 [W], orthogonal frame
  :322–323) from an orthogonal frame to any **spanning** linear injective frame.

### 0.4 Bell terms [Δ18]

- **Settings, histories, MI.** "Let λ be the complete pre-setting hidden state and `a`, `b` the two
  settings." "A preparation fixes a joint law of `(λ, a, b)`; write `μ_{ab} = μ(· ∣ a, b)` for the
  law of λ given the settings. Measurement independence (MI) is `μ_{ab} = μ` for all settings."
  (S:196)
- **Parameter dependence.** "at a fixed pre-setting state, some record of one wing depends on the
  remote setting" (S:175).
- **(Sep)** (Bell-scope r2, #1231 @ `e1534b08`, §3.1 [D]): "For every `t ∈ [t_s, T_A]`:
  `d_{G_φ}(G_B, R_A^t) > t − t_s`. Symmetrically for B." Main's Corollary (Main:414) states the
  corresponding separation for its wings. Here `G_A, G_B ⊂ V` are the disjoint generator regions
  whose content at the setting time `t_s` fixes the settings, `R_A^t` is the region from which wing
  A's complete record reads at time `t` of its record window `[t_s, T_A]`, and `d_{G_φ}` is graph
  distance in Main's coupling graph (Main:362) (Bell-scope r2 (Gen), (Rec), [D]).
- **Two unrelated routes named C.** "Route C" of INTERVENE-1 is the commutant route for operations
  (diagonal identification); route C of §5 below is within-cone propagation. "The two are unrelated
  and are always named with their source." (S:30)

***

## 1. INTERVENE-1 T5, part (c), given (T5a) and (T5b): `InstAvail CM ↔ InstAvail substratumClass` and `genTheory CM = substratumTheory`

**Draft statement (copied; I:157, I:170, I:177); the record carries it only in the conditional
form below.** "**T5 (FI-1 is not theory-invariant).** Let CM be the
column-monomial class: at most one nonzero entry in each column." "(c) **`InstAvail CM T O F ↔
InstAvail substratumClass T O F`, by induction on the constructors**
(OB/ImplementationLocality.lean:268–289)." "The `genTheory` fields `avail`, `availExt`,
`prepAvail` and `readout` (:852ff) are defined from `InstAvail` and `localLuders` alone. So
**`genTheory CM` = `substratumTheory`** (OB/RouteB.lean:284) on every carrier, by propositional
extensionality."

**Hypotheses carried into the conclusion [Δ6].** Parts (a), (b) and (d) of T5 are not carried
(owner decision c.6855167580: they are in APPROX r4a C1–C3, #1221 @ `e41cf613`,
`APPROX-UNIT1.md`:471–483 [D]). Part (c) uses two of them, and the headline uses the third:

- **(T5a)** CM is an `Architecture` (I:159–166; APPROX r4a C1). Needed for `genTheory CM` to be
  defined. Status: open on `main`; paper proof off `main` (I:159–166 [D]; APPROX r4a C1 [D]);
  hand-checked in RV:48–49.
- **(T5b)** A square CM matrix K with Kᴴ K = 1 is monomial (I:168; APPROX r4a, "CM's isometries are
  exactly the monomial ones"). Needed in the `op` case. Status: open on `main`; paper proof off
  `main` (I:168 [D]; APPROX r4a [D]); hand-checked in RV:50–52.
- **(T5d)** K = |0⟩(⟨0|+⟨1|)/√2 on S×Fin 1 (for |S| ≥ 2) is CM and not monomial, and every member
  of `substratumClass` is monomial by definition (I:179; APPROX r4a C3; OB/StructuralClosure.lean:180).
  Used only for the headline. Status: open on `main`; paper proof off `main` (I:179 [D]; APPROX r4a
  C3 [D]); hand-checked in RV:60.

**Carried form.** Given (T5b): for every carrier T, outcome type O and family F,
`InstAvail CM T O F ↔ InstAvail substratumClass T O F`. Given (T5a) and (T5b):
`genTheory CM = substratumTheory` on every carrier. Given (T5a), (T5b) and (T5d): FI-1 holds for CM
and fails for `substratumClass`, although the two classes generate the same theory, so FI-1 is not
an invariant of the generated theory.

**Proof (copied; I:171–177; no mathematical change).**
- "From substratumClass to CM: `instAvail_mono`, since monomial matrices are CM."
- "From CM to substratumClass, constructor by constructor:
  - `op`: K is CM and an isometry, so K is monomial by (b). [(b) is (T5b) above; Δ29]
  - `readout`: the reindexed `readProj` is a 0/1 diagonal transported by a bijection. It lies in
    substratumClass by `substratumClass_arch.proj` and `substratumClass_labelInvariant`.
  - `coarse`, `bind`, `discard`: structural."
- "The `genTheory` fields `avail`, `availExt`, `prepAvail` and `readout` (:852ff) are defined from
  `InstAvail` and `localLuders` alone. So **`genTheory CM` = `substratumTheory`**
  (OB/RouteB.lean:284) on every carrier, by propositional extensionality."

Anchors on `main` for the cited lemmas [Δ7]: `instAvail_mono` OB/ImplementationLocality.lean:305;
`substratumClass_arch` OB/StructuralClosure.lean:231; `substratumClass_labelInvariant`
OB/StructuralClosure.lean:275; `genTheory` OB/ImplementationLocality.lean:852. The remaining
`genTheory` fields are proofs, equal by proof irrelevance (RV:56–59).

**Support layer.** [A] paper induction over `InstAvail`; not kernel-checked (I:294). Hand-checked
against the Lean source by REVIEW-r1 (RV:47–62, model-written, not verification).

**What it adds, and what it does not.** The step that is not elsewhere is (c), `InstAvail CM ↔
InstAvail substratumClass`, and the theory equality it gives (R3:46; RV:184–186). It bears on the
wording of FI-1 and on `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52), whose
conclusion is FI-1 (R3:46). Its constructive content is a presentation (Q2-A); it concerns
representations and generated theories, not physical reachability (R3:150).

**Provenance.** Draft `ea12fde1`, I:157–183 (T5), carried part I:170–177.

***

## 2. SUBSTATE-BRIDGE-1 Lemma E1: no invariance, no finiteness

**Procedure (copied; S:82).** "A Markov kernel `κ` from `Ω_S` to `R`, the same for every input law
(H-IND); an outcome `a` in a countable alphabet `A`, a stopping time `τ ∈ ℕ ∪ {∞}` and an output
configuration, all measurable functions of finitely or countably many records along the
trajectory."

**Statement (copied; S:84–88).** "*Put `g(s,r)` for the outcome, `f(s,r) = π_S(φ^{τ}(s,r))` on
`{τ < ∞}`, and ⊥ on `{τ = ∞}`. Then*

`T(s, B × {a}) := κ(s, {r : τ(s,r) < ∞, f(s,r) ∈ B, g(s,r) = a})`

*is a sub-Markov kernel from `Ω_S` to `Ω_S × A`; with the ⊥ outcome added it is Markov. For every
input law μ the law of (output, outcome) is `∫ μ(ds) T(s, ·)`.*"

**Hypotheses carried into the conclusion.** P-CONF∞, H3, H4, H6 and H-IND (§0.1), with the scope of
§0.1. The conclusion holds for every procedure in the sense above, on any measurable hidden carrier.

**Proof (copied; S:90; no mathematical change).** "`f`, `g`, `τ` are measurable as countable
combinations of the measurable maps `φ^t` and coordinate maps, so `E = {τ<∞, f ∈ B, g = a}` lies in
`𝒮 ⊗ ℛ`. For a product-measurable set, `s ↦ κ(s, E_s)` is measurable (monotone-class argument,
standard). The initial state is `μ ⊗ κ` by H3 and H-IND, the trajectory is a function of `(s,r)`,
and the law of `(f,g)` is the pushforward of `μ ⊗ κ`, which is the displayed integral. Values of a
measure are nonnegative, and the total mass is `κ(s, R) = 1`. ∎"

*Hand check of the measurability step (this record).* Let 𝒟 be the class of E ∈ 𝒮 ⊗ ℛ such that
every section E_s = {r : (s, r) ∈ E} lies in ℛ and s ↦ κ(s, E_s) is 𝒮-measurable. A rectangle
A × B (A ∈ 𝒮, B ∈ ℛ) has section B for s ∈ A and ∅ otherwise, so it gives 1_A(s)·κ(s, B), which is
measurable because κ is a kernel; in particular Ω_S × R ∈ 𝒟. 𝒟 is closed under proper differences:
for F ⊆ E in 𝒟, (E ∖ F)_s = E_s ∖ F_s and κ(s, E_s ∖ F_s) = κ(s, E_s) − κ(s, F_s), since κ(s, ·) is
finite and additive. 𝒟 is closed under increasing unions: (⋃_n E_n)_s = ⋃_n (E_n)_s, and
κ(s, ⋃_n (E_n)_s) = lim_n κ(s, (E_n)_s) by countable additivity, a pointwise limit of measurable
functions. So 𝒟 is a λ-system. Rectangles form a π-system, since
(A × B) ∩ (A′ × B′) = (A ∩ A′) × (B ∩ B′), and they generate 𝒮 ⊗ ℛ, so 𝒟 = 𝒮 ⊗ ℛ by Dynkin's π–λ
theorem [L].

**What it uses (copied; S:92).** "The proof uses no finiteness, no bijectivity, no invariance of any
measure, and no topology. It also holds verbatim for finitely additive states with `κ` a finitely
additive kernel, provided the sets involved are in the algebra: positivity does not rest on
countable additivity. What it does use: measurability (a non-measurable readout has no law), `κ`
independent of the input law (H-IND), and states that are measures (H3)."

**Termination (copied; S:72).** "on an infinite carrier a stopping time can be infinite on a set of
positive measure. E1 carries a failure outcome ⊥. The same caveat applies to a finite carrier and is
not finiteness-specific." The ⊥ outcome is the failure outcome asked for by review 5857985732
(nit 1) for INTERVENE T0 (R3:41, R3:57) [Δ24].

**Relation to records on `main` (copied; S:98).** "A★2 item 2 states the operator form of the same
fact for a measure-preserving joint process on register × `K`: the induced operator is the
compressed Koopman operator or its adjoint transfer operator, "positive and unital Markov operators
(standard)", entrywise nonnegative in the computed indicator basis
(RS/f2-1-coherence-sourcing/amendments/A-star.md:38–45, frozen [W]); the kernel counterpart for the
generated class is `nonnegClass_nonnegBounded` (OB/F2CoherenceControls.lean:173 [K]). E1 is the
same statement without measure preservation and for adaptive procedures. So the Q1a answer was
already on `main` in operator form for the invariant-measure case." On a finite carrier, OA-2 Lemma 0
(`verification/programmes/oi-qm/reconstruction/oa-2-20261112/OA-2-REPORT-r4.md`:201 [W]) states
the nonnegative-matrix form for protocols with fixed-law attachment, discard, heralds and feedback,
with a fixed lift, analogous to H-IND (the exact relation is not audited; I:299, R3:83); it does not treat adaptive stopping or a κ correlated with
s (RV:158–160; R3:41) [Δ8].

**What it adds.** The removal of measure invariance and of finiteness of the hidden carrier, the
coverage of adaptive stopping, and the ⊥ outcome (R3:57, R3:143). It is an upper bound on induced
maps (Q2 "UB"); it exhibits no operation.

**Support layer.** [A]; not kernel-checked (S:347). The monotone-class step is hand-checked above
from Dynkin's π–λ theorem, a standard theorem [L] (`DEPENDENCIES.md` row L).

**Provenance.** Draft `86a413c8`, S:78–98.

***

## 3. SUBSTATE-BRIDGE-1 G1 and Lemma E2

### 3.1 G1: the E_f classical class is frame-relative without spanning

**Finding (copied; S:278).** "T3's spanning hypothesis is the step that carries finiteness; on
non-spanning frames (finite octahedral, continuum Husimi) non-diagonal-preserving unitaries have
nonnegative frame maps, so E_f's "classical class" is frame-relative; the obstruction is on the
measurement side (E2)." Classification NEW. Assumption-watch marker: "any verdict "NX-1 fails/holds
on E_f" must state whether the frame spans".

**Argument (copied; S:102–108; no mathematical change).**

"**The finiteness-bearing step.** T3 assumes a linear injective `L` with `Span(L(states)) =
ℝ^{Ω_enc}`. The states of a `d`-level system span a real space of dimension `d²`, so spanning
forces `|Ω_enc| ≤ d²`. T3 therefore cannot be instantiated on an infinite encoded carrier, and its
control X5 (a negative entry in the Hadamard's frame matrix) is a property of spanning frames."

"**Counter-structure 1 (finite, non-spanning) [X S2c].** Octahedral frame for a qubit: `Ω_enc` = the
six axis points, `L(ρ)(k) = (1 + r·n_k)/6`. `L` is linear and injective and does not span `ℝ⁶`.
The Hadamard rotation `(x,y,z) ↦ (z,−y,x)` permutes the six points, so it acts on the frame by a
permutation matrix, a member of 𝒦, although its conjugation does not preserve diagonal matrices.
For comparison the spanning tetrahedral frame gives a frame matrix with minimum entry −2/5 for a
rational rotation [X S2b]."

"**Counter-structure 2 (continuum) [X S2].** Husimi frame for a qubit: `Ω_enc` = the unit sphere,
`L(ρ)` has density `1 + r·n` for normalized area. It is linear, injective and nonnegative, and
conjugation by any unitary acts by the point map `n ↦ Rn`: `Q_{UρU†}(n) = Q_ρ(Rᵀn)`. Every unitary
is then induced by a measurable area-preserving bijection of the carrier."

"So on route E_f without spanning, "the induced encoded map has a nonnegative frame representative"
does not separate classical from non-classical transformations; the class INTERVENE-1 calls
classical on E_f is frame-relative. On a profinite (totally disconnected) carrier counter-structure
2 is not available continuously: a continuous action of a connected group on a totally disconnected
space is trivial (compare RS/ANALYSIS.md:169–175 on homomorphisms). It is available measurably,
through a Borel isomorphism that respects no finite stage — the readouts excluded by
RS/ANALYSIS.md:28–30 from the finite-depth theorem."

**Hand checks recorded.** The map (x,y,z) ↦ (z,−y,x) is the Hadamard's Bloch action (HXH = Z,
HYH = −Y), has determinant +1 and permutes the six axis points; spanning forces |Ω_enc| ≤ d² by
linearity (RV:66–67; R3:59).

**Hand checks for the [X] tags of this subsection (this record; paper arithmetic, no script run).**
- *S2c, octahedral frame.* The six values (1 + r·n_k)/6 recover r, so L is injective; they satisfy
  p(+e_i) + p(−e_i) = 1/3 for i = x, y, z, so the image does not span ℝ⁶. The Hadamard sends ρ with
  Bloch vector (x, y, z) to Bloch vector (z, −y, x), so p_{n}(Hρ) = p_{Hᵀn}(ρ): a permutation of the
  six entries. It sends the diagonal state (0, 0, 1) to (1, 0, 0), which is not diagonal.
- *S2, Husimi frame.* With U σ_j U† = Σ_i R_ij σ_i and R orthogonal, U† σ_i U = Σ_j R_ij σ_j, so
  tr(UρU† (1 + n·σ)) = tr(ρ (1 + (Rᵀn)·σ)), that is Q_{UρU†}(n) = Q_ρ(Rᵀn).
- *S2b, tetrahedral frame, the rotation about z with cos = 3/5, sin = 4/5.* The tetrahedral frame is
  p_k(r) = (1 + r_k·r)/4, that is E_k = (1 + r_k·σ)/4, with r_k = σ_k/2 and σ_k ∈ {±1}³ of even sign
  product. Then Σ_k r_k r_kᵀ = I and Σ_k r_k = 0, so Σ_k p_k = 1, Σ_k p_k r_k = r/4 and
  p_k(Rr) = 1/4 + (1/4) r_k·R(4 Σ_j p_j r_j) = Σ_j p_j (1/4 + r_k·(R r_j)): the frame matrix is
  F_kj = 1/4 + r_k·(R r_j), unique because the vectors p(r) span ℝ⁴. Write p = σ_k1σ_j1, q = σ_k2σ_j2; the even-sign constraint gives σ_k3σ_j3 = pq, and
  4 r_k·(R r_j) = (3/5)(p + q) + (4/5)(σ_k2σ_j1 − σ_k1σ_j2) + pq. This is 11/5 for p = q = 1,
  −1/5 for p = q = −1, and ±8/5 − 1 for p = −q. The minimum is −13/5, so min F_kj = 1/4 − 13/20 =
  −2/5.

**Hypotheses.** Counter-structures 1 and 2 are statements about linear identifications of qubit
density matrices with laws; they use no OI hypothesis. The verdict they qualify is NX-1 on route
E_f as defined in §0.3, under H-LIFT and the hypotheses of §0.1.

**What it adds.** On spanning frames the frame matrix is unique, so the E_f class is fixed by the
map (T3); on the tetrahedral frame it excludes a rational rotation (S2b). Without spanning the test
need not separate: on the octahedral and Husimi frames non-diagonal-preserving unitaries have
nonnegative frame representatives (S2c, S2; R3:59), and on the Husimi frame every unitary does. This
bears on REC-1 r7 rows 35 and 40 only as a scope note: their frames are orthogonal or spanning. The
relation to OBL-SP's (SP) condition is an analogy only: G1's non-spanning concerns an encoding frame
on route E_f; OBL-SP's (SP) concerns the reachable record laws of the native affine class under
`D_0`; no map between them is given (R3:85).

**Support layer.** [A]. Each [X] tag of this subsection is hand-checked above; the probe is
provenance (`DEPENDENCIES.md` row X).

**Provenance.** Draft `86a413c8`, S:100–108, S:278.

### 3.2 Lemma E2 (single-POVM lemma; finiteness-free)

**Statement (copied; S:110–115).** "*Let `L` be a linear map from the density matrices of a
`d`-level system into the probability measures on a measurable space `(Ω_enc, Σ)`. Assume
P-CONF∞, H4 and H-IND with the encoded carrier as identified carrier (the role of H-LIFT). Then:*

1. *`E(B)` defined by `tr(ρ E(B)) = L(ρ)(B)` is a POVM on `Ω_enc`.*
2. *Every native procedure with outcome alphabet `A` has statistics `p(a∣ρ) = ∫ k_a dL(ρ)` for
   measurable `k_a : Ω_enc → [0,1]` with `Σ_a k_a = 1`; its effects are `F_a = ∫ k_a dE`.*
3. *Any two native procedures are jointly measurable, with joint POVM `M_{ab} = ∫ k_a k'_b dE`.*
4. *If the effects of two native procedures are all projectors, they commute.*"

**Hypotheses carried into the conclusion.** One linear L defined on **every** density matrix of the
d-level system and shared by all procedures; P-CONF∞, H4 and H-IND on the encoded carrier (§0.1);
E1 (§2) for item 2.

**Proof (copied; S:117; no mathematical change).** "(1) `ρ ↦ L(ρ)(B)` is linear with values in
`[0,1]`, so it is `tr(ρ E(B))` for a unique `0 ≤ E(B) ≤ 1`; σ-additivity of `E` follows from that of
`L(ρ)`. (2) E1 with outputs discarded: `k_a(ω) = T(ω, Ω × {a})`. (3) `M_{ab} ≥ 0`,
`Σ_b M_{ab} = F_a`, `Σ_a M_{ab} = F'_b`. (4) If `F_a = P_a` is a projector then
`0 ≤ M_{ab} ≤ P_a` gives `P_a M_{ab} = M_{ab} = M_{ab} P_a`; summing over `a` after multiplying
`Q_b = Σ_{a'} M_{a'b}` by `P_a` gives `P_a Q_b = M_{ab} = Q_b P_a`. ∎"

Hand check of item 4 (RV:64–65): 0 ≤ M ≤ P gives (1−P)M(1−P) = 0, so M = PM = MP.

Hand checks for the [X] tag and the Husimi bound of the consequence below (this record; paper
arithmetic, no script run). *Tetrahedral POVM (S3).* E_k = (1 + r_k·σ)/4; an effect Σ_k w_k E_k
with w ∈ [0,1]⁴ is t·1 + v·σ with t = Σw/4 and v = Σ w_k r_k/4. A rank-one projector needs t = 1/2
and |v| = 1/2. On {Σw = 2} the convex function |v|² is maximal at a vertex, two weights 1 and two 0;
two distinct even-sign vectors differ in two signs, so r_k + r_l has one coordinate ±1 and the
others 0, and |v|² = 1/16 < 1/4. *Husimi POVM.* E(B) = ∫_B (1 + n·σ) dA for normalized area A, so
E(B) = m(B)·1 + v·σ with v = ∫_B n dA; for a post-processing k ∈ [0,1], |∫ k n dA| is largest for
a hemisphere, where it is 1/4 < 1/2.

**Consequence (copied; S:119).** "Hence under one linear encoding shared by all procedures, on any
carrier, two non-commuting sharp measurements (σ_z and σ_x of a qubit) are never both native; in the
Husimi frame no native readout is sharp at all (an effect `m(B)·1 + v·σ` with `|v| ≤ 1/4 < 1/2`; S3
checks the tetrahedral analogue exactly). This is the known trade-off that a quasi-probability
representation of quantum theory has negativity in states or in effects (Spekkens 2008;
Ferrie–Emerson [L]). E2 replaces T3's role without a finiteness or spanning hypothesis: on route E_f
the missing component is a pair of incompatible sharp measurements with their update rule, not a
transformation."

**Scope (copied; S:121).** "Its hypotheses are one linear encoding `L` shared by every procedure
and procedure kernels that do not depend on the input law (H-IND). "Jointly measurable" in item 3
is a statement about the native procedures of that one encoding under those hypotheses; it is not a
statement about every ontological model of the system. E2 does not apply when the encoding is chosen
by measurement context (a family `L_c`, one per context), and it does not apply to non-linear or
history-dependent realizations, in which an amplitude or ψ-register is itself a hidden coordinate
(routes E_r and C-dyn)." It also does not apply to an encoding that is positive only on a restricted
preparation set: its hypothesis requires L to take every density matrix to a probability measure (R3:60)
[Δ9].

**What it adds.** E2 is finiteness-free and needs no spanning-read certification; it concludes
joint measurability of the native procedures of one encoding, not a noncontextual model (R3:60;
compare MECH-2 Theorem NC, `mechanism-2-20261108/DESIGN.md`:485 [W]). It is an upper bound (UB).

**Support layer.** [A]; not kernel-checked (S:347).

**Provenance.** Draft `86a413c8`, S:110–121.

***

## 4. SUBSTATE-BRIDGE-1 L1 and L4 for infinite site groups

### 4.1 L1 (tower locality)

**Statement (copied; S:143).** "*Let `S = ∏_{i∈V} S_i` with `V` finite and the `S_i` arbitrary
sets, and let `(φ(s))_i` depend only on `(s_j)_{j ∈ N(i)}` for a stencil `N`. Then the dependency
graph of `φ` is contained in the stencil graph, and `(φ^k(s))_i` depends only on the stencil ball of
radius `k`.*"

**Argument (copied; S:143; Δ1).** "Main's cone lemma argues by changing one site component at a
time; it states that "finiteness of `V` is used in the first step" (Main:362) and does not use
finiteness of the `S_i`. Replacing each finite site alphabet by a tower or a continuum at a fixed
stencil therefore adds no edge and leaves the cone unchanged."

**Instances on `main` with infinite site alphabets (copied; S:146–147) [Δ22].**
- "**SUBSTATE-1** refines each site value to `R/Z` or `Z_p` under the same lattice wave map
  (CS/README.md:53–55). Site-fibred; stencil unchanged."
- "**NATIVE-PADIC-1.** `waveStep` is defined for one stencil `neighbors : I → D → I` and any additive
  alphabet (OB/NativePadicReduction.lean:32); `project_waveStep` (:56) shows every additive
  reduction commutes with it. The lifted map has the stencil's dependency graph at every level, and,
  more strongly, a readout that factors through a fixed low quotient evolves autonomously: for such
  a readout the deeper digits are not even a hidden variable."

**Hypotheses.** V finite; φ stencil-respecting. No finiteness or other structure of the S_i.

**Scope.** L1 adds no edge and leaves the within-cone (O2) window of the unchanged stencil as in the
finite model, untested (R3:129; Main:414).

**Support layer.** [A] on Main:362's argument [P] (R3:63); hand-checked against Main:362 in
RV:70–71.

### 4.2 L4 (the graph of an additive update does not depend on the state) [Δ27]

**Statement and proof (copied; S:155; no mathematical change).** "*Let `S = ∏_{i∈V} S_i` with each
`S_i` an abelian group (finite, `R/Z`, `Z_p` or any other), and let `φ(s) = c + Λ(s)` with `Λ`
additive. For a non-empty `K ⊆ S` write `i ∼_K j` when `(φ(s'))_i ≠ (φ(s))_i` for some `s ∈ K` and
some `s'` that differs from `s` in component `j` only. Then `∼_K` is the same relation for every
non-empty `K`.* *Proof.* `(φ(s+δ))_i − (φ(s))_i = (Λδ)_i`, which does not contain `s`; so `i ∼_K j`
iff `(Λδ)_i ≠ 0` for some `δ` supported on component `j`. ∎"

**Relation to `main` [Δ10].** Main:362 defines `G_φ^K` as the symmetrization of `∼_K`, with `V` and
each `S_i` finite; `G_φ = G_φ^S` ("for some state"), and `G_φ^ref` is the graph of the reference
vacuum/uniform state class. Main:362 states that for a linear update (ledger item (vii))
`G_φ^K = G_φ` for every non-empty `K`, and that a graph that differs between state classes requires
an update outside (vii). L4 is the same statement for arbitrary abelian site groups, with no
finiteness hypothesis on the `S_i`, proved here from its own definition. Item (vii) is "linearity of
the substratum update (A5)", which Main:724 states as stronger than the affine restriction "that
every first difference of the update is independent of its base point"; L4 needs only the affine
form.

**Consequences (copied; S:160, S:161, S:163) [Δ11, Δ23].**
- (1) "The per-site lifts of SUBSTATE-1 and NATIVE-PADIC-1 are additive on the lifted alphabets. No
   preparation of substates, with any prior, at any depth, under any conditioning event, creates or
   removes an edge of the dependency graph."
- (2) "Preparation-indexed long edges (O1; route B of §3.3) are unavailable to every update within
   (vii), with or without substates. They need a non-additive update. The explicit state-dependent
   rule of [SM §3.1] is one: it selects a neighbour by a site value (`papers/SM.md`:112), so its
   first differences depend on the base point." [route B is in §5 of this record; Δ19, Δ2]
- (4) Ledger (x) binds the reference-class graph `G_φ^ref` (Main:724: "on the reference vacuum/uniform
   state class the coupling graph `G_φ^ref` of §3.3 is the simple-cubic graph"), and Main:414 states
   that preparation-indexed edges place the update outside (vii). By L4 the same holds for infinite
   abelian site groups: scoping (x) to a state class does not by itself open route B while (vii)
   stands. [Δ11]

**Hypotheses.** Product of abelian groups over a site set V (finite in Main's `G_φ^K`); an affine update with additive
part Λ. The relation `∼_K` is directed; Main's `G_φ^K` is its symmetrization.

**Support layer.** [A], one line of algebra (R3:64); hand-checked against Main:362 in RV:70–71.

**Provenance.** Draft `86a413c8`, S:141–163.

***

## 5. Bell-route classification A/B/C, requirements N1–N4, and SLL

**Statement (copied; S:175).** "With measurement independence kept, a deterministic completion
exceeds the Bell bound only through parameter dependence: at a fixed pre-setting state, some record
of one wing depends on the remote setting. Three structurally different routes can carry that
dependence. They are not exclusive, and only the first needs a new substate object."

| Route | What carries the remote-setting dependence | Non-site-fibred hidden factor needed? | What the draft argues (from S:177–181, with the changes of Δ1 and Δ12) |
|---|---|---|---|
| **A** shared factor | a hidden factor `M`, not site-fibred, written by one wing's setting and read by the other wing's record | yes (N1) | requirements N1–N4 below; none supplied by `main` |
| **B** prepared long edges | preparation-indexed edges between ordinary site-fibred sites (Main §3.3(a), Main:412, Main:414; Bell-scope O1) | no | needs an update outside (vii) (L4; for finite `S_i`, Main:362 and Main:414); H-Bell (i)–(iii) (`papers/Substratum.md`:131–133) open on `main`; N3–N4 apply; not otherwise assessed |
| **C** within-cone propagation | the unchanged stencil itself, for wings that are spacelike at the long-wavelength wave speed and inside the graph cone (the window stated at Main:414; Bell-scope O2) | no | not assessed: no response condition and no no-signalling condition was tested in the window; N3–N4 would apply; subject of the mixed-path unit under #868 |

**Copied (S:183).** "A non-site-fibred shared factor is therefore a possible construction and not a
necessary condition for a Bell escape. For wings outside the graph cone of an unchanged stencil, L1
leaves A and B as the alternatives. For wings inside it, route C is available with neither a new
factor nor a new edge, and site-fibred substates could then enter only as carriers of the dependence
or as a pad (§3.4), subject to the quotient restriction of §3.1." [the pad reading of §3.4 is draft
S:213–221, not carried, and its (NS_A) and (PAD) are §6 here; the quotient restriction of §3.1 is
draft S:165, not carried; Δ19]

| # | Applies to | Property | Why it is needed | Status on `main` (from S:187–190, with the changes of Δ1, Δ13, Δ14 and Δ20) |
|---|---|---|---|---|
| **N1** | route A only | A hidden factor `M` that is not site-fibred: one substate object adjacent to both wings, for example a level-`n` variable belonging to a block of `2^n` sites (hierarchical or ultrametric adjacency), or a deep mode common to a prepared pair | L1: for wings outside the stencil's graph cone, site-fibred factors add no edge | not defined anywhere; conflicts with ledger (viii) as stated (Main:724) unless `M` is counted as a site. Counted as a site, its edges must be absent on the reference class, where (x) fixes `G_φ^ref` as the simple-cubic graph (Main:724); they would then have to be preparation-indexed (H-Bell (i), `papers/Substratum.md`:131–133, open), which no update within (vii) allows (L4; Main:362 for finite `S_i`) |
| **N2** | route A only | A directed path `G_B → M → R_A` inside the record window: the remote setting *writes* `M` and the near wing *reads* it | L3 (draft S:167–171, not carried: a shared factor that both wings read and no setting writes is a common cause); conditional on L3 | not supplied; the only level-mixing coupling on record is the explicitly non-native mutant (RS/README.md:196–199), and it is single-cell |
| **N3** | every route | Masking: complete-history no-signalling to each wing, for every law in the physically preparable family 𝒫, with measurement independence or the conditional-law form of §3.4 [§6 here] | parameter dependence is a signal-capable ontic channel | not supplied. By the preparation-span diagnostic (`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/prepared-pair-source.md` §5 [W], finite Λ), 𝒫 cannot have full affine span; the restriction needs a reason independent of the target table |
| **N4** | every route, for agreement with the quantum set | A selector: the mechanism yields CHSH in `(2, 2√2]` and not more | channel + pad alone is the PR box [X S4] | not supplied; Main:360 records the same over-generation for the unrestricted construction |

Hand check for the [X S4] cell of N4 (this record; no script run). With a fair pad bit p, wing B
outputs p and wing A outputs p ⊕ ab, the channel carrying b to A. Each wing's output is uniform for
every pair of settings, so no-signalling holds exactly, and E(a, b) = (−1)^{ab} gives
CHSH = E(0,0) + E(0,1) + E(1,0) − E(1,1) = 4: the PR box.

N1–N4 are requirements; none is supplied, and stating them sources no Bell or quantum mechanism. No
one of them meets all three §A.29 requirements (controls preserved, an independent prediction, not
adjustable to fit any outcome; S:309), and none supplies the independent controls a Bell or quantum
mechanism would need [Δ15].

**Which Bell hypothesis (copied; S:192; Δ1).** "On each of the routes A, B and C, with measurement
independence kept, the failed hypothesis is parameter independence — Main's adopted option (a)
(Main:412). Outcome independence is automatic under determinism. If instead a substate were a common
cause of a setting generator and the response-relevant variable, the failed hypothesis would be
measurement independence, Main's option (b), "recorded, not adopted" (Main:416), with the necessary
cost `I_ont ≥ 0.0309` bits." (The bound is displayed at Main:423.)

**SLL, the substate linkage lemma: an open obligation (copied; S:270; Δ1, Δ16, Δ17).**
"SLL decides route A only. It is neither necessary nor sufficient for a Bell escape in OI: routes B
and C do not pass through it, and its exclusion branch leaves them open. *Either (existence)* a
native rule on a carrier containing a hidden factor `M` that is not site-fibred, such that: (i) some
physically separated every-run Bell protocol has a directed path generator → `M` → remote record
inside its window; (ii) complete-history no-signalling holds for a preparation class with a stated
resolution-based reason; (iii) CHSH exceeds 2 and is bounded by `2√2` by the mechanism; (iv) on the
reference class the rule reduces to the stencil rule with its dispersion and area-law controls. *Or
(exclusion)* every hidden factor admissible under the ledger is site-fibred — posit (viii) read as
covering all hidden degrees of freedom — which with L1 and L2 would extend class (a)3 to all
substates: no substate-carried dependence between wings that satisfy (Sep)." [L2 is draft S:153, not
carried, and is conditional on Theorem N of Bell-scope r2 (#1231 @ `e1534b08`, [D]) and on Bell's
theorem for a measurable λ [L]; class (a)3 is draft S:263: site-fibred towers under a
stencil-respecting rule, for Bell protocols whose wings satisfy (Sep). The exclusion branch's
consequence is stated conditional on both. Δ16] "That would close route A and leave open route B (an
update outside (vii), with (x) scoped [to `G_φ^ref`, Main:724]), route C ([the window of Main:414;]
Bell-scope's O2) and O3 [(measurement independence, ledger item (xiv), Main:724)]. The text of (viii)
("the configuration space is identified with a product of local configuration spaces over a set of
sites", Main:724) reads as the exclusion; Main §3.3(a)'s preparation-indexed long edges are
compatible with it only as edges between sites. Whether (viii) is meant to bind a deep hidden sector
is an owner question, [of the same kind as the scoping of (x) that Main:724 states (Bell-scope's
finding F1)]." [Δ16]

**Status [Δ17].** SLL is open: neither branch is supplied on `main` or in this record. It is kept as
an open obligation (owner decision c.6855167580), and the Bell ladder (#868) takes the A/B/C
classification and SLL as inputs (owner decision c.6854728636).

**Hypotheses carried.** The opening statement is Bell's theorem under determinism and MI:
Main:366–381, :401–404 [P] for finite Ω; for a measurable λ it is the standard extension [L]
(`DEPENDENCIES.md` row L(iii)). MI throughout; determinism of the completion; the routes are classified for
the coupling-graph cone of Main:362 with its finite site set V; route A's N2 is conditional on L3;
SLL's exclusion consequence is conditional on L2 and Theorem N.

**Support layer.** [A] classification; N1–N4 and SLL are open (R3:68, R3:70). The classification is
consistent with Main:362, :412 and :414 and with REC-1 r7 rows 10–11 (R3:68).

**Provenance.** Draft `86a413c8`, S:173–192 and S:270.

***

## 6. Operational no-signalling (NS_A), the sufficient condition (PAD), and countercontrol S7

**Setting (copied; S:196).** "Let λ be the complete pre-setting hidden state and `a`, `b` the two
settings. On any route of §3.3, wing A's complete history is a function `h_A(λ, a, b)` that depends
on `b` at fixed λ. "Complete" means every record wing A holds or can later obtain under every
continuation protocol available to it (later readouts, a second use of the same hidden factor,
records carried to A within their own cones), not the single outcome. A preparation fixes a joint
law of `(λ, a, b)`; write `μ_{ab} = μ(· ∣ a, b)` for the law of λ given the settings. Measurement
independence (MI) is `μ_{ab} = μ` for all settings." [§3.3 is §5 of this record; Δ19]

**Definition (copied; S:198–202).** "**Operational no-signalling to A** is, for every `a`, `b`, `b'`
and every history value `h`:

`μ_{ab}{λ : h_A(λ,a,b) = h} = μ_{ab'}{λ : h_A(λ,a,b') = h}`  (NS_A)

It is required for every joint law in the physically preparable family 𝒫, for both wings (NS_B is
the same with the roles exchanged), and for complete histories. Equality of the two history laws
computed under the unconditional `μ` is (NS_A) only when MI holds."

**Sufficient condition (copied; S:206; no mathematical change).** "**A sufficient condition
(PAD).** For a triple `(a, b, b')`: a measurable bijection `σ` of the hidden space with
`σ_* μ_{ab} = μ_{ab'}` and `h_A(σλ, a, b') = h_A(λ, a, b)` for `μ_{ab}`-almost every λ. Then (NS_A)
holds for that triple [A]: `μ_{ab'}{h_A(·,a,b') = h} = μ_{ab}{λ : h_A(σλ,a,b') = h} =
μ_{ab}{h_A(·,a,b) = h}`. Under MI the first clause reads "σ preserves μ": the remote setting acts on
the near history only through a measure-preserving relabelling of substates that A cannot resolve."

**Limits, with countercontrol S7 (copied; S:208–211).** "(PAD) establishes no-signalling only within
three limits.
- *The law.* It holds for the law it is verified for: a fixed setting-independent μ under MI, or the
  conditional laws `μ_{ab}` otherwise. A `σ` that preserves the unconditional law of λ, with equal
  unconditional history laws, can coexist with operational signalling when a setting generator is
  correlated with λ. Exact instance [X S7]: one hidden bit `r`, `h_A = r ⊕ b`, `P(b=0) = 1/3`,
  `P(r=0 ∣ b=0) = 1`, `P(r=0 ∣ b=1) = 1/4`. Then `r` is uniform and the flip preserves its law,
  while `P(h_A = 0 ∣ b)` is 1 for `b = 0` and 3/4 for `b = 1`.
- *The family.* It must hold for each law in 𝒫, each triple of settings and each wing.
- *The history.* `h_A` is the complete history, continuations included."

**Arithmetic of S7 (hand check; no script run).** P(r=0) = (1/3)·1 + (2/3)·(1/4) = 1/2, so r is
uniform and the flip r ↦ 1−r preserves its law; under the unconditional law of r, P(h_A = 0) = 1/2
for both b, since h_A = r ⊕ b. Conditionally, P(h_A = 0 ∣ b=0) = P(r=0 ∣ b=0) = 1 and
P(h_A = 0 ∣ b=1) = P(r=1 ∣ b=1) = 3/4. The control of the same check (probe lines 314 and 319, "same marginals, setting
independent of the pad") takes b independent of r with the same marginals; then P(h_A = 0 ∣ b) = 1/2 for both b.

**Hypotheses carried.** (NS_A) is a definition. (PAD) ⇒ (NS_A) for the triple holds for any
measurable hidden space, any joint law of (λ, a, b) with the stated pushforward and almost-sure
history conditions, and the history map h_A as given; no OI hypothesis is used. S7 is a generic
two-bit instance; it encodes no OI rule.

**What it adds.** An explicit counterexample showing that invariance of the unconditional marginal
does not give operational no-signalling when settings are correlated with the hidden state (R3:67).
It is consistent with Main:412 (operational no-signalling is "an additional requirement on the
averaged outcomes") and with REC-1 r7 C12 and H-xiv (R3:67).

**Support layer.** [A]; S7's numbers are hand-checked above and checked by the draft's generic
exact check [X S7].

**Provenance.** Draft `86a413c8`, S:194–211; probe `probes/generic_substate_checks.py` (blob
`fa434cd4`) S7 at its lines 293–319.

***

## 7. Not carried: results referenced where they stand

| Draft item | Where it stands | Why not carried |
|---|---|---|
| INTERVENE T7(b) (I:200–206) | `realized_of_instAvail`, OB/ImplementationLocality.lean:530 [K], same induction; its corollary is the proof pattern of `exists_nonMonomial_of_layerFlowExecutable`, OB/ExecSource.lean:52 [K] | on `main` (owner decision c.6855167580; R3:48) |
| INTERVENE T0, T1, T2 (I:100–104, :129–141) | OA-2 Lemma 0 and N0, `oa-2-20261112/OA-2-REPORT-r4.md`:199–223 [W]; kernel nonnegativity `nonnegClass_nonnegBounded`, OB/F2CoherenceControls.lean:173 [K] | duplicated on `main` (R3:41–43) |
| INTERVENE T3 (I:143) | MECH-2 Lemma F(b), `mechanism-2-20261108/DESIGN.md`:325 [W] (orthogonal frames); T3 is stated in §0.3 as context, with spanning | duplicated in substance (R3:44) |
| INTERVENE T4 (I:151–155) | `preservesDiag_conj_of_monomial`, OB/SubstratumInterface.lean:126 [K]; OA-1 configuration ceiling, `oa-1-20261112/OA-1-REPORT-r5.md`:408–422 [W] | duplicated in substance (R3:45) |
| INTERVENE T5 (a), (b), (d) (I:159–168, :179) | APPROX r4a C1–C3, #1221 @ `e41cf613`, `APPROX-UNIT1.md`:471–483 [D] | owner scope: (c) only; used in §1 as named hypotheses |
| L4 for finite `S_i` | Main:362 [P] | on `main` |
| The O2 window | Main:414 [P] | on `main` |
| INTERVENE T6, T7(a), T7(c), the §3 relation table, the §4 candidates Q1–Q6 and the assumption-watch marker | the draft, `ea12fde1` | outside the owner's set |
| SUBSTATE saturation, E3, L2, L3, §2.4 items 1–5, Q3, §5 scoring | the draft, `86a413c8` | outside the owner's set; L2 and L3 are named as conditions where §5 uses them |
