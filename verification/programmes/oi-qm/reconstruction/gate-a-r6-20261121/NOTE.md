# GATE-A r6: premise reconciliation and exact decision wording (research note)

**WIP / UNVERIFIED. Design and paper research only.** This note walks `PLAN.md`, which was
committed before it at `02b1f040`. Revision r2 answers the review at `a1d5bbc0` (#1522
c.7067367430; the reviewer's O6 disclosure is recorded there); r2 is not yet re-reviewed. It adopts nothing and edits no reviewed record. It runs no
computation, edits no manuscript and posts nothing on #1169. Physical source remains NOT PASSED.

**Base and citations.** GA = GATE-A r5.8 (`verification/programmes/oi-qm/reconstruction/gate-a-r5-20261121/PROPOSAL.md`
at `109b9590`, #1503, confirmed at c.7067277470). The other records cited are:
- I3S: #1508 NOTE at `df520f3b`;
- T12: #1510 at `c45b82cf`;
- OPRES: #1511 NOTE at `7669e511`, `verification/programmes/oi-qm/reconstruction/opres-20261121/NOTE.md`.

All of these are off `main`. They are cited as reviewed research records, not as results on `main`.

**Layers.** X is exact algebra on paper and P is a paper argument. Each result also names its layer
on three axes: effect, instrument or accessible algebra; ontic or Born-form; and typing, soundness
or operational.

## 1. Task 1: the premises, where they enter, and their labels (Q1)

| Premise | What it is | Where it enters | Layer | Label | Status |
|---|---|---|---|---|---|
| **E** | the set of additional conditions the reconstruction requires (#1169 c.7064859041) | every clause of I★ through M* ∈ M(E, `J_exact(A)`) (GA §2) | typing (container) | — | open; no E proposed |
| **I-3** | the sourcing clause: E and M* pass a sourcing criterion | GA §2 I★ clause (I-3) | soundness (physical) | — | open: D5 decided as a research unit (c.7065620072); I3S found no independently justified criterion |
| **J-coh** | protocols with coherent preparations and readouts outside the configuration basis, beyond the native single-time interface | I★ over `J_exact`; the coherent variants of I★_st; L-H; Theorem C's target class | typing (interface) | (I) wherever used (c.7065620072, Stage 2) | named; unsourced |
| **FE-ADM** | free evolution with a loaded setting is the witness's label interpretation of Λ_t | P-ST items 1 and 2 (GA §2.4, T12) | operational (instrument level, label rule) | (I) | named; does not exclude D-W |
| **BF** | the Born-form family equals the model's operational law | P-ST item 2 only | Born-form (KIN applied to M*) | (I) on KIN | named |
| **O1-C** | a coherence-creating element: an operation that is not MIO-type | OPRES Theorem C(a), (d) | Born-form, instrument level | (I) on KIN, countable carriers | necessary for a Born-form non-monomial realization; not supplied by OI's stated operations, conditional on R-READ (OPRES §5) |
| **O1-D** | a coherence-detecting element: an operation that is not DIO-type | OPRES Theorem C(b), (d); Proposition D; Remark D′ | Born-form, instrument level (not effect level) | (I) on KIN and, for measurable carriers, nonsingularity and normality (D) or finite visible carriers (D′) | as O1-C; R-READ unresolved |

O1-C and O1-D are kept separate, as #1169 c.7066541026 requires. The table does not identify either
of them with I-3 (§3, Q4).

## 2. Implications and independences (Q2, Q3)

### 2.1 Q3: P-ST item 2 entails the O1 pair (Proposition R6-1)

**Proposition R6-1 ((I) on KIN and countable carriers; layer X; Born-form, instrument level;
CONFIRMING).** Suppose:
- M* has a countable configuration space;
- M* meets I★_st-coh (Born form, GA §2.4) for a unitary target Λ_t = Ad_{W^t}, with W
  non-monomial at t = 1;
- the family is typed (b) of GA §2.4, with one hidden prior ω_H and a controller configuration
  c_{s_Λ}.

Then no such model exists: within GA's typing, the conclusion is non-existence. (A statement that
a witness "contains a non-DIO element" would need a Born-form family beyond permutation dilations,
which GA §2.4 does not define; it is not made here.) The same holds under typing (a), since ω_{s_Λ}
is a fixed append for each s.

*Proof.*
- The GA §2.4 family at t = 1 is the composition Φ_1 = O_3 ∘ O_2 ∘ O_1 of three operations:
  - O_1 appends the state |c_{s_Λ}⟩⟨c_{s_Λ}| ⊗ ω_H;
  - O_2 = Ad_{φ̂}, with φ̂ the permutation unitary of the bijection;
  - O_3 is the partial trace over C × H.
- None of the three detects coherence in OPRES's sense, which is that the diagonal of the output
  depends on an off-diagonal entry of the input. Each case:
  - O_2 permutes configuration basis vectors, so the output diagonal is a permutation of the
    input diagonal.
  - O_3 sums diagonal entries.
  - O_1 gives the output diagonal diag(ρ) ⊗ diag(|c⟩⟨c| ⊗ ω_H), whatever ω_H is.
- By OPRES Lemma C, Φ_1 is then DIO. Theorem C(b) requires ‖Φ_1 − Ad_W‖_⋄ ≥ 2κ_row(W), which is
  positive for non-monomial W (C(c)). So Φ_1 ≠ Ad_W.
- I★_st-coh in Born form is itself the statement Φ_1 = Ad_W, so the hypotheses cannot all hold.
  FE-ADM and BF are not used; with them, the statement is P-ST item 2 composed with this
  non-existence.
- For the creation half: O_1 is MIO exactly when ω_H is diagonal, and O_2 and O_3 are MIO. So with
  a diagonal prior, Theorem C(a) also excludes Φ_1 = Ad_W. With a coherent ω_H, O_1 is a creator
  but there is still no detector. ∎

**Scope and grade.**
- This is a second route, through OPRES's MIO/DIO theorems, to I3S's Lemma S1 at the scope where
  the two overlap. GA §2.4 already records the consequence ("by #1508's Lemma S1 … BF and I-4 are
  jointly unsatisfiable for such models on non-monomial targets"). S1 uses a spectral argument under its (a)–(e); R6-1 uses Theorem C on countable
  carriers with one prior, which is S1's (c).
- On measurable carriers the detection half follows from OPRES Proposition D for a nonsingular
  bijection and a normal ω_H, or from Remark D′ when the visible carriers are finite. The singular
  case is OPRES's open Conjecture D″.
- Grade: **CONFIRMING** of S1 and of GA §2.4. It is not an implication between premises, and it does
  not count toward the productivity test (§2.5).
- **Layer.** The result holds at the Born-form, instrument level. It says nothing at the operational
  layer: P-ST item 1, which needs no BF, needs no O1 element. D-W meets item 1 classically
  (sketch), and OPRES's operational scope shows no non-classical resource to be necessary. Nor does
  it say anything at the effect level. Native readout effects lying in the configuration algebra
  (R-READ, unresolved) would not by itself make every native instrument DIO (c.7066770882).

### 2.2 Q2: independences

| Pair | Independent? | Separating example | Layer, label |
|---|---|---|---|
| O1-C, O1-D | yes | OPRES CC-1: one-bit teleportation realizes Hadamard with a \|+⟩ ancilla, a creator that is DIO-type by the O_1 computation in §2.1, and a destructive ⟨±\| readout, a detector that outputs a classical record and so maps diagonal inputs to diagonal outputs (MIO-type) | Born-form, instrument; X; (I) on KIN |
| FE-ADM, J-coh | not an independence question: the two are of different types (FE-ADM constrains a witness's label rule; J-coh is an assumption about the interface) | — | typing |
| FE-ADM, BF: BF without FE-ADM | yes | a GA-typed model: a bijective M* with identity free dynamics, a **monomial** target Λ_t = Ad_X^t on a qubit level, and labels realized by interventions. BF holds, since the Born-form family and the free operational law are both the identity; FE-ADM fails, since free evolution is not the label interpretation of Ad_X | Born-form vs operational; P; this example is from the review c.7067367430 |
| FE-ADM, BF: FE-ADM without BF | yes, for non-monomial targets, on the reading that BF holds only when its family is defined; conditional on Remark D′ (pending review) and on D-W meeting FE-ADM (sketch) | the stepwise D-W meets FE-ADM by a loaded program (T12). Its visible carrier X_A is finite, so normality is not needed (OPRES Remark D′). The remaining premise is nonsingularity of its reversible step with respect to the reference measure ν = (counting measure on X_A × program fields × records) ⊗ (the seed tape's product law) ⊗ (Lebesgue measure on the register's real coordinates). If the step is ν-nonsingular, Remark D′ makes the Born-form family DIO, so it is not Ad_W and BF fails; if it is ν-singular, the Koopman operator φ̂ is not unitary on L²(ν), the Born-form family is undefined, and BF is not met. A countable-seed variant (alphabet weights 2^{−k}, whose subset sums give every t ∈ [0, 1]) would allow ℓ² with counting measure, where S1 and Lemma C apply directly, if the register's content can also be carried on a countable alphabet; that is not checked | Born-form vs operational; P |
| E, I-3 | not independent | I-3 is a test on E and M* | typing |

### 2.3 Q4: O1 and I-3

No formal map between O1 and I-3 is established, and none is claimed (bridge rule).
- **O1 does not give I-3.** An E that posits a quantum register supplies both O1 elements in its
  Born-form description, yet it is a D-W-type posit, which I3S's representational condition R-EX
  admits and which is not a sourcing criterion.
- **I-3 does not require O1 in general.** Under a criterion stated at the operational layer, P-ST
  item 1 needs no O1 element.
- **The conditional relation.** If the I-3 criterion is representational, requiring BF, then by
  R6-1 no bijective model with the GA §2.4 family passes on a non-monomial unitary target; a
  passing model would need Born-form dynamics outside permutation dilations, which GA does not yet
  type, and under OPRES Theorem C such dynamics would contain a creator and a detector (O1-C and
  O1-D), natively if the criterion also requires substratum dynamics (as T-SUB′ would). This is a conditional
  relation, not an identification.

### 2.4 Layer check of the existing records

GA, T12 and I3S were checked against the three-level readout rule and the layer rule. No statement
was found one layer above its proof.

The provisional READOUT-ALG reading in the common brief, "no native readout supplies non-DIO",
passes from effects to instruments. The owner corrected that inference at c.7066770882, and none of
GA, T12 or I3S relies on it.

### 2.5 Outcome (PLAN §1)

**Gem by the fixed test, on §2.2 alone:** three independences with separating examples (O1-C
and O1-D; BF without FE-ADM; FE-ADM without BF, conditional as stated). R6-1 is CONFIRMING and
does not count. FE-ADM and J-coh are of different types, so no independence is claimed for them. No
layer error was found in the existing records. The r1 INCONCLUSIVE item is closed conditionally in
§2.2.

### 2.6 The three questions (R6-1)

1. **Established.** R6-1 (CONFIRMING) at layer X, Born-form, instrument level, on countable
   carriers, under either typing of s_Λ, with its measurable extensions conditional on OPRES D and
   D′; the review of `a1d5bbc0` found its proof correct.
2. **Assumed.**
   - KIN (the Born form);
   - countable carriers, or OPRES D's or D′'s hypotheses;
   - a unitary target;
   - typing (b);
   - J-coh, through the coherent inputs of I★_st-coh.
3. **Missing.** A physical mechanism that supplies a coherence detector and a coherence creator
   inside one model. This is OPRES's U2, and OPRES records the physical question as INCONCLUSIVE.
   Without that mechanism, P-ST item 2 has no satisfiable instance with bijective dynamics on
   non-monomial targets.

## 3. Task 2: exact decision wording for D1–D4 and D7

Each block gives the text the owner would adopt, the alternatives word for word, and what each
choice changes. No option is recommended or adopted. `GA §n` refers to GA at `109b9590`.

### D1. The statement of I★

- **D1-A (adopt as stated).** "I adopt I★ as stated in GATE-A r5.8 §2 (#1503 at `109b9590`) as the
  model-level target of part 1 over `J_exact(A)`. This includes the encoding rule enc_A, the
  design choices of a single label rule and a single resource policy, and the single-law reading of
  `Q_exact(A)` in clause I-4. Clause I-3 is governed by the D5 research unit and is not discharged
  by this adoption."
  - *Changes:* I★ becomes the adopted target of part 1. `endpoints.md`:51–69 on `main` is unchanged
    until a landing (D4). The single-law reading becomes binding, and D1-C is closed.
- **D1-B (one model, without the two design choices).** "I adopt I★ as stated in GATE-A r5.8 §2,
  with one model throughout (Φ, Λ, μ, ι, R and τ independent of A), except that the single label
  rule and the single resource policy are not required: the label rule and the resource policy may
  depend on A through enc_A, each fixed before comparison and never computed from p_T."
  - *Changes:* the target keeps answer 3's single model. By GA §5 (L-T), satisfiability inside
    `J_exact` is unchanged, and the resource policy is no longer required to be one rule.
- **D1-B′ (the architecture form).** "I adopt the architecture form: GATE-A r5.8 §2 with clause
  I-2★ replaced by r4's clause I-2 (one architecture 𝔄, one instance per (A, T), dependence on A or
  T only through a parameter map fixed in advance and never computed from p_T), as the target of
  part 1."
  - *Changes:* this departs from answer 3 of c.6876591512, which makes the single model the
    ultimate target and the architecture an intermediate milestone, unless that answer is amended.
    On the scope of `J_exact`, L-T (GA §5) makes the two forms coincide.
- **D1-C (adopt with the family reading of `Q_exact(A)`, indexed by T).** "I adopt I★ as stated in
  GATE-A r5.8 §2, except that clause I-4 is read with `Q_exact(A)` as a family: for every T in
  `Q_exact(A)` there is a setting s_T, fixed from the typed data of T before comparison and loaded
  as in GATE-A r5.8 §2.4, such that the A-subsystem of M* with s_T loaded reproduces p_T exactly
  under its label interpretation."
  - *Changes:* I-4 quantifies over every member of `Q_exact(A)`. Without the index s_T, one model
    with one label interpretation cannot reproduce two distinct laws on the same (p, π, h), so the
    unindexed family reading is unsatisfiable whenever `Q_exact(A)` has two or more distinct laws.
    If `Q_exact(A)` has one member, as EP:43 and EP:110 suggest, D1-C coincides with D1-A.
- **D1-D (defer).** "I defer the adoption of I★. GATE-A r5.8 §2 remains a reviewed proposal."
  - *Changes:* nothing is adopted. Stage 1 and Stage 2 (c.7065620072) proceed against the proposal
    as a working target.

### D2. Soundness, access closure and B⇒

There is no separate "defer" option: GA's default, absent a decision, is D2-A (GA §9).

- **D2-A (the 15 November amendment governs).** "#1169 c.6891338304 governs:
  - soundness (S⇒) is an open question, reported as a finding and subject to agreement with
    performed experiments (S-D);
  - the exclusion of stronger-than-quantum experiments within C, both in access closure (S-A) and
    in B⇒, is not a requirement;
  - the accessibility half of answer 4 of c.6876591512 is kept on the coverage side.

  The line 'The 14 November decisions are authoritative inputs' (c.7064859041) does not restore
  answers 2 and 4 as they stood."
  - *Changes:* GA §2.3 stands as written. S⇒, S-A (exclusion half) and B⇒ are findings, not
    obligations. BELL-QSET (#1060) needs its own wording decision.
- **D2-B (answers 2 and 4 restored).** "Answers 2 and 4 of #1169 c.6876591512 are restored as they
  stood: soundness (S⇒), access closure (S-A) including the exclusion of stronger-than-quantum
  experiments within C, and B⇒ are required. The amendment of soundness at c.6891338304 is
  withdrawn."
  - *Changes:* GA §2.3's rows for S⇒, S-A and B are restored to required. The C/Q definitions of
    c.6891338304 stand, including C's independence from quantum outcomes and the noncircularity
    requirement; only the openness of C ⊆ Q is withdrawn.
- **D2-C (soundness open, Bell exclusion required).** "#1169 c.6891338304 governs soundness (S⇒)
  and access closure (S-A). B⇒ ('exclude supraquantum ones', decision 3 of #914 c.6875046763) is
  required."
  - *Changes:* only B⇒ becomes an obligation again. BELL-QSET's text stands as written.

### D3. H-PI

- **D3-A (not a requirement; preconditions recorded).** "H-PI is not added to the contract.
  U-completeness (EP:77) and isolation (EP:79) are recorded as explicit preconditions of every
  exactness and readout result."
  - *Changes:* L-H stays conditional on H-PI as a stated hypothesis. L-H′ stands without it. No EP
    line changes.
- **D3-B (a requirement).** "H-PI, 'the controller fields loaded for an instrument do not depend on
  the preparation', is added to the admissibility schema of `endpoints.md` §2.1 as a requirement on
  every candidate."
  - *Changes:* L-H's preparation-independent response classes hold for every admitted model. A
    future landing would add an EP line. Models whose instrument controllers read the preparation
    become inadmissible.
- **D3-C (no decision).** "No decision on H-PI is needed; it remains a hypothesis of L-H only."
  - *Changes:* nothing. The preconditions of D3-A are not recorded.

### D4. The r4 route, the r5 landing and #1428

- **D4-A (answer 5 as directed).** "r4 (`3a1c8e97`) and its status note r6 are prepared for
  preservation on `main` through the normal gates, as answer 5 of #1169 c.6876591512 directs.
  GATE-A r5.8 lands afterwards, after independent review, as a forward amendment in its own record
  directory. The #1428 GATE-A row is corrected to the text of D4-row below."
  - *Changes:* two landings, with r4's 34 files reaching `main` first. `endpoints.md` is unchanged.
    r5.8 cites off-`main` reviewed records (#1506, #1508, #1510, #1511) and relies on them for D-W,
    S1, P-ST and Theorem C; its landing needs that content restated in r5.8 or retained on `main`
    under §A.42 items 1–3 and 8, or the landed record cites content not on `main`.
- **D4-B (r4 by reference; departure from answer 5 approved).** "r4 stays on its branch and is cited
  by reference. GATE-A r5.8 restates every clause it uses. This departure from answer 5 of #1169
  c.6876591512 is approved. GATE-A r5.8 lands after independent review as a forward amendment in its
  own record directory. The #1428 GATE-A row is corrected to the text of D4-row below."
  - *Changes:* one landing. r4's text stays off `main`, and is provenance under §A.42 item 8. The
    same off-`main` dependency of r5.8 as in D4-A (#1506, #1508, #1510, #1511) must be restated or
    retained under §A.42 items 1–3 and 8 before the landing.
- **D4-C (no landing yet).** "Neither r4 nor r5.8 lands now. The #1428 GATE-A row is corrected to
  the text of D4-row below."
  - *Changes:* only the tracker is corrected.

**D4-row (for every D4 option; it supersedes the row proposed at GA §8, which predates D5, D6 and
the T1/T2 fold).**

| ID | Item | Tier | Prerequisites | Readiness | Authorization |
|---|---|---|---|---|---|
| GATE-A | Gate A forward amendment for the superset target: r4 and r4's status note r6 (#1289), consolidated as GATE-A r5.8 (#1503 at `109b9590`) | supporting (provisional) | owner answers at #1169 c.6876591512; soundness amended at c.6891338304; D5 and D6 decided at c.7065620072; T1/T2 folded under c.7067233614; owner decisions D1–D4 and D7 | r5.8 reviewed (c.7067277470); decision wording prepared (GATE-A r6) | preparation and review authorized; adoption, landing and merge not authorized |

Proposed open-work note: "GATE-A. The four owner questions were answered at #1169 c.6876591512. Soundness was amended at c.6891338304, and D5 and D6 were decided at c.7065620072. GATE-A r5.8 (#1503) carries the target and awaits decisions D1–D4 and D7, whose exact wording is in GATE-A r6. The contract `oi-qm-ext-1/endpoints.md` on `main` is unchanged."

### D7. Scalability

D7-B, D7-C and D7-D can be combined (D7-C contains D7-B); D7-A excludes the others.

- **D7-A (record as open).** "Inside `J_exact` the scalability safeguard of #1169 c.7064859041 is
  recorded as nominal (GATE-A r5.8 §2.1). A substantive scalability constraint is an open question.
  None of SG-1 to SG-4′ is adopted."
  - *Changes:* nothing in I★. O2 continues as research (#1516).
- **D7-B (SG-1 as a scope extension).** "SG-1 (coexistence of separately addressable subsystems
  X_A and X_{A′} with a typed joint interface) is adopted as a scope extension of part 1. It is to
  be typed with the remainder of part 1 and with B."
  - *Changes:* it widens the interface beyond `J_exact`. It adds a typing obligation, and its force
    against D-W comes only through E and I-3.
- **D7-C (SG-1 to SG-3 as scope extensions).** "SG-1, SG-2 (encoding compatibility under subsystem
  inclusion, with an inert complement) and SG-3 (typed system-changing maps) are adopted as scope
  extensions of part 1. They are to be typed with the remainder of part 1 and with B."
  - *Changes:* as D7-B, with nested and system-changing interfaces added.
- **D7-D (SG-4′ as a resource requirement).** "SG-4′ is adopted. Ω is declared site-factorized,
  with a finite local alphabet and finite-range dynamics. The number of sites read or written by
  any protocol of depth K with at most m outcomes per step on carrier A is at most f(|A|, K, m), for
  an f fixed before comparison."
  - *Changes:* it adds a precise constraint and puts a site structure into E. By #1504's
    Proposition U (as reported in the #1506 review c.7065065491 R8; Proposition U is at #1504
    `31594967` and is not read here), it is probably unsatisfiable for any finite f.

## 4. What this note does not do

It edits nothing in #1503, #1508, #1510, #1511, `main`, any manuscript or any Issue body. It runs no
computation, adopts no premise, criterion, interface or decision, and posts nothing on #1169.
