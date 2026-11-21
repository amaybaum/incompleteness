# QOPS-P4: which open instruments could be natively non-MIO or non-DIO

**Standing. WIP / UNVERIFIED.** Writer's paper record under `PLAN.md`, which was committed first
at `bc85942e`. It has not been independently reviewed. It runs no computation and adopts no
premise. Every premise below is named, not adopted.

- **Authorization.** #1169 c.7067281228 (round 4, the native-mechanisms track).
- **Goal link.** The goal link is the one stated in `PLAN.md`.
- **Base.** The base is #1518 at `46240053` (`P3`). Line numbers are at `main` `df6da1c6`; `RA:n`
  is a line of READOUT-ALG's `NOTE.md` at `4554dd63` (#1513, provisional, under review).
- **Inputs.** OPRES (`OP`, #1511 `7669e511`): `𝒩`, `𝒩⁺`, Lemma C and Theorem C. P2 and P3 as
  cited.
- **Constraint.** The owner's provisional-readout constraint (#1169 c.7066770882): three levels,
  and native non-DIO is open, not impossible.

**Layers.** Every result is labelled with the readout level at which it is proved (E effect, I
instrument, A accessible algebra) and its representational layer (O ontic, B Born-form). Verification
layers are [W] for a proof here, [P] for a manuscript statement and [R] for a record. Every result
here is countable-carrier only.

**Imports and named premises.**
- KIN (P2) gives "coherence" its meaning, so every MIO and DIO statement is (I) on KIN.
- **CPX** (new): the update on coherent inputs is *some* completely positive map whose action on
  configuration states is the item's own defined action. CPX is strictly weaker than RA's UPD-C
  (`RA:280`), which fixes the Kraus operators: UPD-C implies CPX.
- **NONRED** (new): a record step's represented update is *not* the reduction of the substratum
  bijection's lift with a fixed hidden state.
- **COH-REC** (new): a represented record step with at least two branches, whose configuration
  maps collide on a pair `λ ≠ λ'`, carries nonzero collision coherences that cancel across the
  branches.
- **From RA §3.1:** IMPL-R5 (an implementable native instrument with one non-diagonal effect),
  ACC-R5 and REF.
- **LUD** (new): an IMPL-R5 instrument has the non-destructive Lüders update.

***

## 0. Answers

1. **Q1. The open items, at the instrument level.**
   - **Items 1, 4, 22 (observation, Bell outcome, book mirror).**
     - *MIO.* Their own diagonal-sector definition (`Main:664`) makes them MIO, with no premise
       needed.
     - *DIO under CPX alone* (Proposition RIG), which is weaker than RA's UPD-C.
     - So **neither** half of O1 can come from them without leaving CPX. That would mean either a
       non-CP update or an update that disagrees with `Main:664` on configurations, and either way
       the item would no longer be the corpus's instrument.
   - **Items 11, 12 (EP-schema record law, A★2 records).**
     - *MIO.* Their defined actions on configuration states are classical, so they are MIO, with no
       premise needed.
     - *DIO.* This is forced if the update is a deterministic channel (RIG(b)), or if it is the
       reduction of the substratum lift (RIG(a) with OPRES Lemma C).
     - *Non-DIO.* It needs **NONRED ∧ COH-REC**, which is a destructive, `⟨±|`-type detector only.
   - **Full-algebra sites 24 and 25** (`Str:742`, `Str:788`; `Main:722`, `GR:366`).
     - *Non-DIO* needs **IMPL-R5** for one element, preceded at site 25 by REF.
     - *Non-MIO* needs **IMPL-R5 ∧ LUD**.
     - These are the only open sites where one premise set yields both.
2. **Q2. No candidate is native.** The smallest candidates that supply both halves are single
   elements, and two of them tie at one element, one site:
   - **H-F1** (FLOW₁; P3 §2.1, with its ties H-F1′ and H-F1(t)): a dynamics-layer import that
     `LiftAudit.lean:200` excludes from the stated dynamics.
   - **H-R5L** (IMPL-R5 ∧ LUD on one configuration pair of one site): an access-layer premise. Its
     effect half rests on the corpus's own declared algebra, read operationally (RA's R5a,
     unresolved).

   The owner's constraint forbids treating the declared algebra as supplying operations, so H-R5L
   is not native. The two differ in *where* the premise enters:
   - H-F1 at the ontic dynamics;
   - H-R5L at the accessible algebra (level A) plus the instrument update (level I).
3. **Productivity (`PLAN.md`): GEM (candidate).**
   - Criterion (i) holds. RIG decides items 1, 4 and 22 at the instrument level from CPX, which is
     weaker than UPD-C, and decides MIO for items 1, 4, 11, 12 and 22 with no premise.
   - Criterion (ii) holds. NONRED, COH-REC, LUD and CPX are new, and the ranking is given.

***

## 1. The rigidity results

**Proposition RIG [W; levels I and B; (I): KIN; countable carriers].** Let `C` be countable.
- **(a) Injective maps.** Let `f : C → C` be injective and let `S ⊆ C`. Every CP map `Ψ` with
  `Ψ(|z⟩⟨z|) = [z ∈ S] |f z⟩⟨f z|` for all `z` has Kraus operators of the form
  `K_k = Σ_{z∈S} c_k(z) |f z⟩⟨z|`. These are monomial, so `Ψ` is MIO and DIO.
- **(b) Non-injective maps, one branch.** If `f` is any map and `Ψ` is a CPTP map with
  `Ψ(|z⟩⟨z|) = |f z⟩⟨f z|`, then `Ψ` is DIO.
- **(c) Classical diagonal sectors.** Every CP map whose outputs on configuration states are
  diagonal is MIO-type. This is the definition, recorded because it decides Q1.
- **(d) Non-injective maps, several branches.** An instrument whose branches `Ψ_o` act on
  configuration states as configuration maps `f_o` can have non-DIO branches.
  - The total is TP, which forces `Σ_o [f_o λ = f_o λ'] g_o(λ, λ') = 0` for `λ ≠ λ'`, where
    `g_o(λ, λ') = Σ_k c_{o,k}(λ) c̄_{o,k}(λ')`.
  - A branch is non-DIO iff some `g_o` is nonzero on a pair that `f_o` collides.
  - The destructive `⟨±|` readout is an instance (`OP` CC-1): `f_± ≡ const` and
    `g_± (0, 1) = ±1/2`.

*Proof.*
- (a) `Σ_k K_k|z⟩⟨z|K_k†` has rank at most one, with range `|f z⟩` or 0. Each summand is
  positive, so `K_k|z⟩ ∈ span(|f z⟩)`, and so `K_k` is CM. Injectivity of `f` puts one entry in
  each row, so `K_k` is RM. Monomial Kraus operators give MIO and DIO (`OP` §2).
- (b) As in (a), `K_k|λ⟩ = c_k(λ)|fλ⟩`. TP gives `Σ_k ⟨λ|K_k†K_k|λ'⟩ = [fλ = fλ'] g(λ, λ') = δ_{λλ'}`.
  So `g` vanishes on every colliding pair, and those coherences are exactly what reaches the
  output diagonal: `⟨y|Ψ(|λ⟩⟨λ'|)|y⟩ = [fλ = fλ' = y] g(λ, λ')`.
- (c) The definition of MIO-type (`OP` §2).
- (d) As in (b), branch by branch. Only the sum is constrained by TP. ∎

**Corollary RIG′ (the native lift is forced) [W; I, B; (I): KIN, CPX].** Take any CP update of
the full carrier whose action on full configuration states is conditioning after the substratum
bijection (`Main:664`'s diagonal sector). Every visible instrument it induces, with any fixed
hidden state `ω`, is DIO. It is MIO iff `ω` is diagonal.
- *Proof.* RIG(a) applies on the full carrier, since the substratum bijection is injective.
  Appending `ω`, a monomial step and partial trace all preserve DIO, and appending `ω` is MIO iff
  `ω` is diagonal (OPRES Lemma C). ∎
- This strengthens OPRES A′ from the permutation lift to every CP extension of the native
  configuration action. The coherent-input freedom that `Main:664` leaves to the bridge cannot
  produce non-DIO without leaving CPX.

***

## 2. Q1: the item table (non-DIO and non-MIO directions)

| RA item | Defined action on configurations | Non-MIO? | Non-DIO? | Smallest additional premise for non-DIO | Level / layer of the result | Class |
|---|---|---|---|---|---|---|
| 1, observation (`Main:42`, `:664`) | the bijection, then conditioning (diagonal sector) | **no**, by RIG(c), with no premise | **no** under CPX (RIG′) | none that keeps CPX. Non-DIO needs a non-CP update, or an update that disagrees with `Main:664` on configurations | I, B | (I): KIN; CPX for DIO |
| 4, Bell outcome (`Main:376`) | as item 1, on the readout region | **no** (RIG(c)) | **no** under CPX | as item 1 | I, B | as item 1 |
| 22, book mirror (`book/glossary.md`:21) | as item 1 | **no** | **no** under CPX | as item 1 | I, B | as item 1 |
| 11, EP-schema record law (`EP:92`, `:97`, `:100`) | deterministic maps `(ι, Φ, R)`, possibly non-injective; a classical outcome law | **no** (RIG(c)) | **no** for a single-branch deterministic channel (RIG(b)), and **no** if the record step is the reduction of the substratum lift (RIG′) | **NONRED ∧ COH-REC**, for a record with at least two branches that collide on a pair. It yields a destructive detector only | I, B | (I): KIN; and NONRED, COH-REC for the non-DIO direction |
| 12, A★2 records (`RA:192`) | indicator projectors and a positive unital Markov operator | **no** (RIG(c)) | as item 11 | as item 11 | I, B | as item 11 |
| 24, `Str:742` ("may be taken to be"), `Str:788` | none: a declared algebra, not an instrument (`RA:66`–`73`) | only with **IMPL-R5 ∧ LUD** (P3 §2.3 lemma) | only with **IMPL-R5** | **IMPL-R5** for one non-diagonal effect, which gives a detector. **LUD** adds the creator | A then I; B | (I): KIN, IMPL-R5 (and LUD) |
| 25, `Main:722`, `GR:366` | as item 24 | as item 24, after **REF** = bare OI | as item 24, after REF. Under REF = OI_Q it is item 16, outside 𝒜 via an import | **REF**, then as item 24 | A then I; B | as item 24, plus REF |

**Reading the table, at its layer.**
- The "no" entries for non-MIO are instrument-level and Born-form, and they follow from the
  items' own configuration-level definitions.
- The DIO entries are conditional on CPX (items 1, 4 and 22) or on reduction (items 11 and 12).
- No entry is an operational-layer statement. P3's CC-OI shows that invasive classical
  realizations reproduce any record law, so no record law alone decides MIO or DIO.

***

## 3. Q2: ranking the candidates for both halves

The order is P3's: the number of elements outside `𝒩`, then support at site granularity, then RES
cost. To it is added the layer at which the premise enters, ontic dynamics or accessible algebra,
which is reported but not ranked.

| Candidate | Elements | Supplies | Premises | Enters at | Native? |
|---|---|---|---|---|---|
| H-F1, `unit S_m (1/2)` | 1 | non-MIO and non-DIO | FLOW₁ (with CTRL to apply it) | ontic dynamics (O) | **no**: `LiftAudit.lean:200` excludes it from the stated dynamics |
| H-F1′, H-F1(t) | 1 | both | FLOW₁ and 2 to 4 catalysts (H-F1′) | O | no |
| **H-R5L**, a non-destructive Lüders readout of `(|x⟩ ± |y⟩)/√2` on one site | 1 | both (P3 §2.3 lemma) | IMPL-R5 (level A), LUD (level I); REF if sited at item 25 | accessible algebra and instrument | **no**: R5a is unresolved, and the owner forbids treating the declared algebra as supplying operations |
| destructive IMPL-R5 readout plus a coherent hidden state `ω` (`𝒩⁺`) | 2 | detector plus creator (OP CC-1 pattern) | IMPL-R5; a coherent `ω`, which is not native, since ledger posit (iv) gives laws over configurations | A and the preparation | no |
| items 11 and 12 with NONRED ∧ COH-REC | 1 | detector only | NONRED, COH-REC | I | no |
| items 1, 4, 22 | — | neither under CPX | — | — | — |

**The answer.**
- No native candidate exists in the class {CP extensions of the native configuration action (CPX),
  configuration readouts, any fixed hidden state, feedforward}. By RIG′, every element of that class
  is DIO, and it is non-MIO only with a coherent hidden state, which is creator-only.
- The smallest candidates for both halves are single elements:
  - H-F1 (dynamics) and H-R5L (access) tie on the order's first two criteria;
  - H-F1 needs no RES beyond the protocol's;
  - H-R5L needs a record cell, which under H-RC means at least one catalyst (P6).
- H-F1 is therefore the representative minimum by the stated order. H-R5L is the minimum among
  candidates whose effect half the corpus itself declares, if R5a were read operationally.

**One model (O1 with O3).** Neither candidate supplies ready cells. By P3 Q-ind, row 2, a unitary
H-F1 cannot. Whether a non-destructive measurement H-R5L can, by conditioning, costs its record's
entropy (PR1). RES stays the earliest O3 input.

***

## 4. Established, Assumed, Missing

**Established** (all [W], unreviewed).

| Result | Class | Level / layer |
|---|---|---|
| RIG(a)–(d) | (I): KIN | I, B |
| RIG′ | (I): KIN, CPX | I, B |
| The item table: "MIO" for items 1, 4, 11, 12 and 22 with no premise | (I): KIN | I, B |
| The item table: "DIO" | (I): KIN, with CPX or reduction | I, B |
| The ranking | as in §3 | as in §3 |

**Assumed.** KIN; CPX for the DIO entries of items 1, 4 and 22; reduction to the substratum lift
for items 11 and 12. The candidates' premises — FLOW₁, CTRL, IMPL-R5, LUD, REF, NONRED and COH-REC
— are named, not adopted. R-READ is treated as the owner's provisional constraint.

**Missing.**
- *The earliest unsupported step for O1.*
  - Either a physical mechanism at the ontic dynamics, FLOW₁.
  - Or an operational access to one non-diagonal effect, IMPL-R5, together with its update form,
    LUD. That is a physical mechanism at levels A and I.
  - Settling whether the declared full algebra carries any implementable instrument (R5a against
    R5b, and REF) is the owner question that RA raises. It is a question of definition and
    physical interpretation, and mathematics alone does not settle it.
- *O3.* RES (P2, P3).

***

## 5. Pressure test (§A.31)

1. *RIG(a) is elementary.* It removes one escape: a "different lift" of the native observation
   that agrees on configurations. It does not remove non-CP or non-agreeing updates, which are
   different instruments.
2. *RIG′ assumes a fixed hidden state.* A hidden state that depends on the input coherently is
   OPRES's coherent controlled append (CM-3), which is DIO. A preparation-dependent classical
   hidden law is in `𝒩`. Neither reopens non-DIO.
3. *The favourable branch is H-R5L.* It rests on reading the declared algebra operationally,
   which the owner's constraint forbids assuming. It is recorded as a candidate only.
4. *Measurable carriers.* RIG is countable-only. Items 11 and 12 may live on measurable seed
   spaces (`EP:100`), and there the instrument-level statement is open (cf. OPRES U1′).

| Item | Proposed class |
|---|---|
| RIG(a), RIG(b) | ELABORATING (an elementary Kraus-rigidity argument) |
| RIG′ | NEW (candidate): it decides items 1, 4 and 22 at the instrument level from CPX |
| RIG(d) and the NONRED / COH-REC premise | NEW (candidate): it locates the only non-DIO route among the open record items |
| The ranking | ELABORATING |
