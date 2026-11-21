# QOPS-P4: which open instruments could be natively non-MIO or non-DIO

**Standing. WIP / UNVERIFIED.** Writer's paper record under `PLAN.md`, which was committed first
at `bc85942e`. It runs no computation and adopts no premise. Every premise below is named, not
adopted.
- **Review.** Independent non-author review at `47148e74`: REVISE (minor)
  ([#1524 c.7067392111](https://github.com/amaybaum/incompleteness/pull/1524#issuecomment-7067392111)).
  R1–R4 and n1–n6 are answered in appended commits.

- **Authorization.** #1169 c.7067281228 (round 4, the native-mechanisms track).
- **Goal link.** The goal link is the one stated in `PLAN.md`.
- **Base.** The base is #1518 at `46240053` (`P3`). Line numbers are at `main` `df6da1c6`; `RA:n`
  is a line of READOUT-ALG's `NOTE.md` at `4554dd63` (#1513, provisional, under review).
- **Inputs.**
  - OPRES (`OP`, #1511 `7669e511`): `𝒩`, `𝒩⁺`, Lemma C and Theorem C.
    - The owner records OPRES as a reviewed stopping point (#1169 c.7066541026).
    - Its own text labels its results "pending review" (`NOTE.md:46`, `:400` at `7669e511`).
    - They are cited at that standing.
  - P2 and P3 as cited.
- **Constraint.** The owner's provisional-readout constraint
  ([#1169 c.7066770882](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066770882)):
  three levels, and native non-DIO is open, not impossible.

**Layers.** The round-4 layer rule is the coordinator's guidance, derived from the owner's
three-level readout decision (#1169 c.7066770882); it is not a separate owner decision. Every
result is labelled on three axes, given in the §4 table:
- the readout level: E effect, I instrument, A accessible algebra;
- the representational layer: O ontic, B Born-form;
- the claim layer: T typing, S soundness, Op operational.

Verification layers are [W] for a proof here, [P] for a manuscript statement and [R] for a record.
Every result here is on countable carriers, and for **normal** CP maps, which are those with a
Kraus form.

**Imports and named premises.**
- KIN (P2) gives "coherence" its meaning, so every MIO and DIO statement is (I) on KIN.
- **CPX** (new): the update on coherent inputs is *some* normal completely positive map whose
  action on configuration states is the item's own defined action. CPX is strictly weaker than
  RA's UPD-C (`RA:280`): UPD-C implies CPX.
- **COH-REC**: a represented record step with at least two branches, whose configuration maps
  collide on a pair `λ ≠ λ'`, carries nonzero collision coherences that cancel across the branches.
  This is RIG(d)'s **exact criterion** for a non-DIO branch, not a weaker premise. It implies that
  the step is not the reduction of the substratum lift, because that reduction is DIO (RIG′).
- **From RA §3.1:** IMPL-R5 (an implementable native instrument with one non-diagonal effect),
  ACC-R5 and REF.
- **LUD**: an IMPL-R5 instrument has the non-destructive Lüders update. This is the hypothesis of
  P3's §2.3 lemma, newly named here.
- **IMPL-R5 and LUD are sufficient, not minimal.**
  - IMPL-R5 suffices for non-DIO but is not necessary: P3's `Ad_H` has a diagonal effect and is
    non-DIO.
  - LUD suffices for non-MIO, through P3's lemma, but is not necessary.

***

## 0. Answers

1. **Q1. The open items, at the instrument level.**
   - **Items 1, 4, 22 (observation, Bell outcome, book mirror).**
     - *MIO.* Their diagonal-sector definition (`Main:664`), with the hidden law diagonal as part
       of the item's definition (ledger posit (iv): laws over configurations), makes them MIO.
     - *DIO under CPX* (RIG′), which is weaker than RA's UPD-C.
     - So **neither** half of O1 can come from them without leaving CPX, or without a coherent
       hidden state. A coherent hidden state would give creation only, and would not be the item
       as defined.
   - **Items 11, 12 (EP-schema record law, A★2 records).**
     - *MIO.* Their defined actions on configuration states are classical (RIG(c)).
     - *Non-DIO: OPEN.* The record actions are non-injective and multi-branch, so they fall outside
       RIG′'s injective class. By RIG(d), a CP extension of them *can* be non-DIO, exactly when it
       satisfies COH-REC.
     - No theorem here excludes the corpus's own record update from satisfying COH-REC. If it did,
       the item would be a **MIO, non-DIO detector**: destructive on its colliding pairs, not
       necessarily elsewhere.
     - They are DIO if the update is a single-branch deterministic channel (RIG(b)), or the
       reduction of the substratum lift (RIG′).
   - **Full-algebra sites 24 and 25** (`Str:742`, `Str:788`; `Main:722`, `GR:366`).
     - *Non-DIO.* IMPL-R5 is a sufficient premise for one element; at site 25, REF must come first.
     - *Non-MIO.* IMPL-R5 ∧ LUD is a sufficient premise.
2. **Q2. Not shown native.** No candidate is shown native.
   - In the class built on the **injective** substratum bijection (CPX on the full carrier,
     configuration readouts, any fixed hidden state, feedforward), none exists, by RIG′.
   - Items 11 and 12 lie outside that class, and their native non-DIO is open.
   - The smallest candidates that supply both halves are single elements, and two tie at one
     element, one site:
     - **H-F1** (FLOW₁; P3 §2.1, with its ties): a dynamics-layer import that `LiftAudit.lean:200`
       excludes from the stated dynamics;
     - **H-R5L** (IMPL-R5 ∧ LUD on one configuration pair of one site): an access-layer premise
       resting on RA's unresolved R5a, which the owner's constraint forbids treating as supplying
       operations.
   - On RES the two **tie**, with both charged like for like (§3). No minimality of either premise
     set is shown.
3. **Productivity (`PLAN.md`): ELABORATING.**
   - Criterion (i) holds, through RIG(b) and RIG′.
   - Criterion (ii) fails. The both-halves sets are {FLOW₁} (from P3) and {IMPL-R5 (from RA),
     LUD}. LUD is only newly named, and no minimality is shown. CPX is new, but it enters the DIO
     direction, not the ranked set.
   - So the record supports ELABORATING, not GEM.

***

## 1. The rigidity results

**Proposition RIG [W; I, B, S; (I): KIN; countable carriers, normal CP maps].** Let `C` be countable.
- **(a) Injective maps.** Let `f : C → C` be injective and let `S ⊆ C`. Every normal CP map `Ψ` with
  `Ψ(|z⟩⟨z|) = [z ∈ S] |f z⟩⟨f z|` for all `z` has Kraus operators of the form
  `K_k = Σ_{z∈S} c_k(z) |f z⟩⟨z|`. These are monomial, so `Ψ` is MIO and DIO.
- **(b) Non-injective maps, one branch.** If `f` is any map and `Ψ` is a normal CPTP map with
  `Ψ(|z⟩⟨z|) = |f z⟩⟨f z|`, then `Ψ` is DIO.
- **(c) Classical diagonal sectors.** Every CP map whose outputs on configuration states are
  diagonal is MIO-type. This is the definition, recorded because it decides Q1.
- **(d) Non-injective maps, several branches.** An instrument whose branches `Ψ_o` act on
  configuration states as configuration maps `f_o` can have non-DIO branches.
  - The total is TP, which forces `Σ_o [f_o λ = f_o λ'] g_o(λ, λ') = 0` for `λ ≠ λ'`, where
    `g_o(λ, λ') = Σ_k c_{o,k}(λ) c̄_{o,k}(λ')`.
  - A branch is non-DIO iff some `g_o` is nonzero on a pair that `f_o` collides (COH-REC).
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

**Corollary RIG′ [W; I, B, S; (I): KIN, CPX].** Take any normal CP update of the full carrier whose
action on full configuration states is conditioning after the **injective** substratum bijection
(`Main:664`'s diagonal sector). Every visible instrument it induces, with any fixed hidden state
`ω`, is DIO. It is MIO **if** `ω` is diagonal.
- *Proof.* RIG(a) applies on the full carrier, since the substratum bijection is injective.
  Appending `ω`, a monomial step and partial trace all preserve DIO. Appending a diagonal `ω` is
  MIO (OPRES Lemma C). ∎
- The converse of the MIO clause is not claimed. It fails, for example, when the visible
  instrument does not depend on the hidden coherences, as with a decoupled hidden sector.
- RIG′ strengthens OPRES A′ from the permutation lift to every CP extension of the native
  injective configuration action. Record steps that are non-injective at the visible level
  (items 11 and 12) are outside RIG′, unless they are reductions of this lift.

***

## 2. Q1: the item table (non-DIO and non-MIO directions)

| RA item | Defined action on configurations | Non-MIO? | Non-DIO? | A sufficient premise for non-DIO (not shown minimal) | Level / layer | Class |
|---|---|---|---|---|---|---|
| 1, observation (`Main:42`, `:664`) | the bijection, then conditioning, with a diagonal hidden law | **no** (RIG(c)), given the diagonal hidden law of the definition | **no** under CPX (RIG′) | none that keeps CPX. Non-DIO needs a non-CP update, or an update that disagrees with `Main:664` on configurations | I, B, S | (I): KIN; CPX for DIO |
| 4, Bell outcome (`Main:376`) | as item 1, on the readout region | as item 1 | **no** under CPX | as item 1 | I, B, S | as item 1 |
| 22, book mirror (`book/glossary.md`:21) | as item 1 | as item 1 | **no** under CPX | as item 1 | I, B, S | as item 1 |
| 11, EP-schema record law (`EP:92`, `:97`, `:100`) | deterministic maps `(ι, Φ, R)`, possibly non-injective; a classical outcome law | **no** (RIG(c)) | **OPEN**. It is DIO if single-branch (RIG(b)) or a reduction of the lift (RIG′) | **COH-REC**, which is the exact criterion. It gives a MIO, non-DIO detector | I, B, S | (I): KIN |
| 12, A★2 records (`RA:192`) | indicator projectors and a positive unital Markov operator | **no** (RIG(c)) | **OPEN**, as item 11 | as item 11 | I, B, S | (I): KIN |
| 24, `Str:742` ("may be taken to be"), `Str:788` | none: a declared algebra, not an instrument (`RA:62`–`73`) | only with a further premise, for example **IMPL-R5 ∧ LUD** | only with a further premise, for example **IMPL-R5** | IMPL-R5 (sufficient; not necessary, since `Ad_H` is non-DIO with a diagonal effect) | A then I; B; Op | (I): KIN, IMPL-R5 (and LUD) |
| 25, `Main:722`, `GR:366` | as item 24 | as item 24, after **REF** = bare OI | as item 24, after REF. Under REF = OI_Q it is item 16, outside 𝒜 via an import | REF, then as item 24 | A then I; B; Op | as item 24, plus REF |

**Reading the table, at its layer.**
- The non-MIO "no" entries are instrument-level and Born-form soundness statements. They follow
  from each item's configuration-level definition, including, for items 1, 4 and 22, the
  diagonal hidden law.
- The DIO entries are conditional on CPX (items 1, 4 and 22), or open (items 11 and 12).
- No entry is an operational-layer statement about record laws. P3's CC-OI shows that invasive
  classical realizations reproduce any record law.

***

## 3. Q2: ranking the candidates for both halves

The order is P3's: the number of elements outside `𝒩`, then support at site granularity, then RES
cost. The layer at which the premise enters is reported, but not ranked.

| Candidate | Elements | Supplies | Premises (sufficient, not shown minimal) | Enters at | Native? |
|---|---|---|---|---|---|
| H-F1, `unit S_m (1/2)` | 1 | non-MIO and non-DIO | FLOW₁ (with CTRL to apply it) | O, dynamics | **not native**: `LiftAudit.lean:200` excludes it from the stated dynamics |
| H-F1′, H-F1(t) | 1 | both | FLOW₁, plus 2 to 4 catalysts for H-F1′ | O | not native |
| **H-R5L**, a non-destructive Lüders readout of `(|x⟩ ± |y⟩)/√2` on one site | 1 | both (P3 §2.3 lemma) | IMPL-R5 (level A), LUD (level I); REF if sited at item 25 | A and I | **not shown native**: R5a is unresolved, and the owner forbids treating the declared algebra as supplying operations |
| destructive IMPL-R5 readout plus a coherent hidden state `ω` (`𝒩⁺`) | 2 | detector plus creator (OP CC-1 pattern) | IMPL-R5; a coherent `ω`, which ledger posit (iv) does not supply, since it gives laws over configurations | A and the preparation | not native |
| items 11 and 12 under COH-REC | 1 | a MIO, non-DIO detector only | COH-REC, the exact criterion | I | **open** |
| items 1, 4, 22 | — | neither under CPX | — | — | — |

**The RES tie-break, charged like for like.** Operational detection in either candidate needs a
readout record.
- H-F1 is read by READ, and under H-RC its record cell needs at least one catalyst (P6).
- H-R5L's record cell has the same cost.

So the two **tie** on RES as well. Neither ranks first by the stated order. They differ in *where*
the premise enters: the ontic dynamics for H-F1, the accessible algebra and the instrument update
for H-R5L.

**One model (O1 with O3).** Neither candidate supplies ready cells. By P3 Q-ind, row 2, a unitary
H-F1 cannot. If a non-destructive measurement H-R5L could, by conditioning, it would pay for that
with its record's entropy (PR1). RES stays the earliest O3 input.

***

## 4. Established, Assumed, Missing

**Established** (all [W], unreviewed).

| Result | Class | Readout level | Representational layer | Claim layer |
|---|---|---|---|---|
| RIG(a), (b), (d) | (I): KIN | I | B | S (properties of CP maps) |
| RIG(c) | (I): KIN | I | B | T (by definition) |
| RIG′ | (I): KIN, CPX | I | B | S |
| The item table: MIO for items 1, 4, 22 (given the diagonal hidden law), 11 and 12 | (I): KIN | I | B | S |
| The item table: DIO for items 1, 4, 22 under CPX; open for items 11, 12 | (I): KIN, CPX | I | B | S |
| The ranking and the RES tie | as in §3 | I and A | O and B | Op (premise placement only) |

**Assumed.** KIN; CPX for the DIO entries of items 1, 4 and 22. The candidates' premises — FLOW₁,
CTRL, IMPL-R5, LUD, REF and COH-REC — are named, not adopted. R-READ is treated as the owner's
provisional constraint.

**Missing.**
- *O1.* The earliest unsupported step is one of the following, each a physical mechanism:
  - FLOW₁, at the ontic dynamics;
  - an operational access to one non-diagonal effect with its update form, IMPL-R5 ∧ LUD, at
    levels A and I;
  - for detection only, a demonstration that the corpus's record update for items 11 and 12
    satisfies COH-REC, or a theorem excluding it. That is mathematics, once the update is defined;
    RA records that the corpus defines none.

  Whether the declared full algebra carries any implementable instrument (R5a against R5b, and
  REF) is RA's owner question.
- *O3.* RES (P2, P3).

***

## 5. Pressure test (§A.31)

1. *RIG(a) is elementary.* It removes one escape: a different lift of the native observation that
   agrees on configurations. It does not remove non-CP or non-agreeing updates, which are
   different instruments.
2. *RIG′ assumes a fixed hidden state.* A hidden state that depends coherently on the input is
   OPRES's coherent controlled append (CM-3), which is DIO. A preparation-dependent classical
   hidden law is in `𝒩`. Neither reopens non-DIO within the injective class.
3. *The favourable branches are H-R5L and items 11 and 12.* H-R5L rests on reading the declared
   algebra operationally, which the owner's constraint forbids assuming. Items 11 and 12 are open,
   because the corpus defines no represented update for them. Both are recorded as candidates
   only.
4. *Measurable carriers.* RIG covers countable carriers and normal maps only. Items 11 and 12 may
   live on measurable seed spaces (`EP:100`), where the instrument-level statement is open
   (cf. OPRES U1′).

| Item | Proposed class |
|---|---|
| RIG(a), RIG(b) | ELABORATING (an elementary Kraus-rigidity argument) |
| RIG′ | ELABORATING: it decides items 1, 4 and 22 at the instrument level from CPX |
| RIG(d) and COH-REC as the exact criterion | ELABORATING: it locates the open non-DIO route for items 11 and 12 |
| The ranking | ELABORATING |
| The round | ELABORATING (`PLAN.md` criterion (i) holds, (ii) fails) |
