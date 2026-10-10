# PT stage-2 integration addendum — composition (S3), the pair built from data (S2), and the double-slit review (DS)

Research only, from certified `main` at L = `9f9f8257`.

**Governing texts.**
- `PROTOCOL.md` with amendments 1–2.
- `PROTOCOL-STAGE2.md` (`38603692…`).
- `PROTOCOL-STAGE2-DS.md` (`086a4cb8…`) for DS.

Nothing here is adopted, frozen or governed. No branch, PR, CI run, governed round or repository change was made. The stage-1 review (`INTEGRATION-REVIEW.md`) and its audit corrections stand as recorded; this addendum adds to them. Thread C's narrowed tree obstruction is cited verbatim and not generalized.

| thread | RESULT.md (sha256) | audit | replays | independent check |
|---|---|---|---|---|
| S3 (COMP-CONS) | `80f362db…` | `audit/S3/AUDIT-S3.md` | 5/5 byte-identical | 42/42 |
| S2 (PAIR-CONS) | `b1139809…` | `audit/S2/AUDIT-S2.md` | 7/7 byte-identical | 26/26 |
| DS (double-slit review) | `26c33475…` | `audit/DS/AUDIT-DS.md` | 3/3 byte-identical | 13/13 |

**My own failed runs**, each kept and recorded; neither bore on a thread claim:
- S3 run 1: a tally harness error;
- S2 run 1: a badly chosen countercontrol input.

**One provenance event, accounted for.** DS recorded a transient change to `pt/` at 09:14:01Z. It was my draft of this addendum, moved out of `pt/` so that DS's end-of-run sweep would not meet it.

**Evidence levels** are those of stage 1:
- [K] certified at L;
- [D] design run `ff9c3a35`;
- [W] written argument;
- [X] exact computation, instance-scoped;
- [L, unverified];
- UNBUILT Lean.

**Labels** follow amendment 2. Every INDEPENDENT is relative to the certified premises at L, which define no pair system and nothing with three or more tokens.

## 0. Bottom line

1. **The data do construct a composite.**
   - Products, product tests, the native gate, mixtures and completion generate one consistent pair system, `K_gen = SEP + cnot SEP`. A twin of it arises for the other orientation class.
   - Its finite rank and local tomography are CONDITIONAL on one principle, INV2: the native gate is an operational involution on the pair system. Under the table rule they are built in.
   - It is gate-compatible by construction.
   - Every state and test it generates obeys the quantum consistency rules. Four-copy coherence holds on all generated instances, so it is a sub-theory of two-qubit quantum theory (S2).
2. **What the data do not supply is completeness on the effect side.**
   - The full dual `K_E = dualW K_gen` contains effects that no data generate (`E0`, `F`).
   - Four-copy coherence (FCC), with the no-restriction its proof consumes, excludes `K_gen` only through those effects.
   - S2 found this from the pair side and S3 from the four-token side.
3. **S3's source: FCC is CONDITIONAL on self-duality under composition**, SDC = P3 ∧ OVL4 ∧ CSD2.
   - Sufficiency is proved.
   - It is not a restatement under the frozen renaming test.
   - It is strictly stronger than FCC on admissible closed cones.
   - Relative to the pair hypotheses it is existentially equivalent to FCC. Every quantum-compatible sufficient principle is, so strength cannot separate a source from a renaming.
   - Its load-bearing new content is that the self-dualizing pairing composes multiplicatively (OVL4 across groupings).
   - Its observer-native source is **UNRESOLVED**.
4. **Associativity is not cross-pairing** (exact).
   - Every fixed token order is blind to at least one of the four pairs.
   - Cross-pairing is a free state-level regrouping plus an effect-level part that is exactly famI ∧ famII.
5. **Convergence.** The two threads' open items reduce to one finite-dimensional question, **Q-SD**: *is Q3 the only `cnot`-invariant self-dual cone containing the product states?* (§3)
   - **Yes:** pair self-duality becomes a non-flagged source of the quantum state space.
   - **No:** an exotic cone is a rigorous countermodel to it.
6. **Labels relative to L.**
   - FCC, the required state space, finite rank and LT are each **INDEPENDENT** (valid countermodels).
   - **K2 remains OPEN.** No obligation is discharged at the certified level.
7. **DS: the supplied double-slit analysis.**
   - Its physics is exact, under stated assumptions.
   - Its caution that describing is not deriving is right.
   - Its strategic claim is wrong. A double-slit derivation is not a target narrower than K2 or independent of S2/S3. The which-path detector is a second system, written into the framework's own native gate applied to a product.
   - For that single coupling, the textbook visibility law already follows from the certified CNOT table: coherence is multiplied by the record overlap [X symbolic over K].
   - Any richer record family, any eraser and any Bell-type readout needs the composite state space that S2 and S3 identify as missing.
   - The framework-specific double-slit derivation is **UNRESOLVED** relative to L. The input's closing route ("incomplete access + reversible dynamics + hidden records must produce the equation") is refuted by the certified realization theorem `S_imp_D`.

## 1. Per thread

### S3 — what composition principle implies FCC

**Strongest result.** FCC is CONDITIONAL on SDC [W over the exact cross identity `<prodA X Y, prodB E F> = fourVal X Y E F`].
- P3: both groupings' independent preparations are states of one four-token system.
- OVL4: four-token states overlap nonnegatively for the composed pairing.
- CSD2: every pair effect is a pair state.

Each conjunct is load-bearing, shown by exact drop-one models, and none restates the cross clause.

**Refuted by exact models:**
- ordered associativity in any fixed order;
- every chart-invariant single-pair principle without uniformity;
- each half of self-duality under uniformity: `K_gen` from below, and the new `K_gen*` (= S2's `K_E`) from above, both −1;
- orientation coherence alone;
- one-sided conditioning;
- entanglement-swapping consistency;
- four-token no-restriction together with P3.

**UNRESOLVED:**
- uniform full self-duality, and self-duality with orientation coherence. Both are the exotic-cone gap, which is Q-SD at the `cnot` instance;
- purification;
- the OI source of SDC.

**Audit notes** (wording; no label changes):
- The thread's "full no-restriction on both sides is needed" is overstated. What the foils show is that *non-generated* arguments are needed on each side. Full no-restriction is sufficient, not shown necessary.
- The Barker–Foran stall condition is a negative overlap, not a zero one.
- The associativity refutation as written is for one order. It extends to every order.

### S2 — a pair system built from data

**Strongest results.**
- **Theorem N, exact.**
  - Among the 4096 signed-diagonal dressings of `cnot`, the landed `NativeGate` predicates select exactly 32 gates.
  - A set of them is consistent iff all share one orientation class.
  - The generated cone is then `K_gen` or `σ K_gen`.
  - My independent re-implementation of the landed predicates reproduces every number.
- **INV2 ⇒ LT** for data-generated systems, equivalent at the completion level.
- **INV2, or a finite operation group, ⇒ finite rank.**
- **Generativity ⇒ gate compatibility** for the generated cone.
- **The no-restriction exposure**: FCC fails on `K_gen` only through non-generated effects.

**Models.**
- Register: product action, finite rank, not LT.
- Clock: reversible, infinite rank; exact Hankel ranks 8, 16, 32, 48, 64.
- Hidden-parameter: generation is load-bearing.
- Rebit: the table datum is load-bearing.

**Classes that cannot reach Q3 or IE1:**
- `𝒞_nat` (fixed-frame native sets): exact;
- `𝒞_mono` (frame-monomial operations, including `CtrlGate` and SWAP): [W + L];
- `𝒞_fin` (finite groups): [W + L].

**What reaches Q3 among the routes examined:**
- local agency or frame covariance. Both are flagged; FC ⟺ IE1 given hgate, with exact words confirmed;
- FCC with its full-dual effects, through the design theorem.

**Audit qualification.** GC is DERIVED *relative to the construction*: generation and the table rule, which are the adopted meaning of "from data". Relative to L alone, the gate premise keeps its stage-1 status, INDEPENDENT.

### DS — review of the supplied double-slit analysis

**Strongest results.**
- Fifty-five claims were checked against L with anchors.
- **Accurate:**
  - the formulas;
  - the definite-path caveat;
  - the description/derivation distinction;
  - the finite-horizon equivalence and its universality;
  - the AncillaInterference result, which excludes one specific non-quantum surplus operation.
- **Corrected:**
  - Level 1 drops "fixed-basis" from the ROADMAP's own sentence.
  - Level 3 is understated. Relative to the stated architecture the corpus already shows that the double-slit structure is *not* forced: every finite law is realized by reversible dynamics with incomplete access [K]; read-write dynamics does not generate state mixing [K]; phases and nonclassical control are INDEPENDENT.
  - "The machinery exists" reads available-to-represent as available-to-derive.
  - The §4.1 paraphrase puts the apparatus in the hidden sector; Main places it in the visible one.
  - "Narrower than K2 and independent of S2/S3" is inaccurate.
  - "Must produce that equation" is refuted.

**The proposed target.**
- **Not well-posed at L.** L has no double-slit arrangement, no observation map or ensemble, no OI-native pair system in the substratum, and no non-insertion criterion.
- **Non-discriminating as stated.** A classical reversible model with a definite path and no amplitudes meets all three of its requirements exactly. The reason is simple: with a real record overlap, the quantum screen law is a mixture of the two classical endpoint laws.
- **The hard-to-vary form** (DS §3(d)):
  - a construction frozen before computing;
  - complementarity over a detector family;
  - an eraser readout;
  - a Bell-type test;
  - no third-order interference.

  Those parts are exactly where the pair system, IE1 and Q3 enter.

**Corpus markers found** (record-only; nothing edited):
- `Explainer.md:568` calls its double-slit account "a derivation".
- `Methodology.md:401` cites "Main §3.4" for a treatment that is at §4.1.
- Main L664 speaks of "eliminating the interference terms", but the certified representation has none.

## 2. Property by property (stage-1 rows updated)

| property | stage 1 | stage 2 | relative to L | evidence |
|---|---|---|---|---|
| finite rank of a data-generated pair completion | not separately posed | CONDITIONAL on INV2 or a finite operation group; strictly stronger than FR (register model) | INDEPENDENT (clock model; A's `D_cl`) | [W + X] |
| LT of that completion | U6, open | CONDITIONAL on INV2 with the product action and generation; equivalent at the completion level, strictly stronger at the carrier level; built in under the table rule | INDEPENDENT (register model; landed `paddedBall3`) | [W + X] |
| gate compatibility (`hgate`, `hinv`) | INDEPENDENT; weaker clauses sufficient [W over D] | holds by construction for generated cones; validity from [K] facts | INDEPENDENT for given cones (unchanged) | [X + W] |
| closedness (`hcl`) | INDEPENDENT; compactness suffices for the read-out cone | unchanged; compactness does not give finite rank (compact padded model) | INDEPENDENT | [W + X] |
| FCC | CONDITIONAL on regrouping invariance (a renaming) | CONDITIONAL on SDC (not a restatement); exact refutations of associativity, single-pair, one-sided and conditioning routes | INDEPENDENT (`M_tok`, uniform `K_gen`, uniform `K_gen*`) | [W + X], [D] for the strength results |
| the required state space (Q3 at the instance; IE1) | flagged routes only | unreachable in `𝒞_nat` (exact), `𝒞_mono` and `𝒞_fin` ([W + L]); reached by local agency, frame covariance or FCC's no-restriction | INDEPENDENT (the `K_gen` system); a non-flagged source in general is UNRESOLVED and decided for the self-duality route by Q-SD | [X + W + L] |

## 3. The central question — "why should independently observable systems, when combined, obey the same consistency rules that produce quantum entanglement?"

As far as stage 2 reaches, the answer splits in two.

**What the data already explain.** Combine two independently observable systems using only:
- independent preparation;
- product tests;
- the one native interaction, taken as an involution;
- mixing and completion.

The result is a consistent composite whose every generated state and test obeys the quantum consistency rules. Nothing about the *consistency* of the generated composite needs an extra principle: four-copy coherence holds on everything the data produce.

**What they do not explain.** They do not explain why the composite's state and effect spaces are *complete*. That is, why every functional that is nonnegative on the generated states is a physically available test, and why every such test is a state.

That completeness is exactly what turns the generated sub-theory `K_gen` into the quantum cone Q3. The two threads name it in two forms:
- **no-restriction** on the pair: the full dual is the effect set. This is the form the four-copy proof consumes.
- **self-duality under composition**: states and effects coincide, with multiplicative pairing. This is S3's SDC.

**The decisive open question (Q-SD).** Consider any cone `K` with `cnot K = K`, `K = dualW K` and `SEP ⊆ K`.
- `K` automatically satisfies the pair hypotheses with uniform `cnot` gates [W]:
  - `K ⊆ dualW SEP = maxCone`;
  - `K` is closed;
  - `K ⊇ K_gen`.
- If Q3 is the only such cone:
  - pair self-duality, imposed on the data-generated system, yields Q3, hence IE1 and FCC at the instance;
  - it would then be a non-flagged source for S2's state-space target and for S3's uniform rows.
- If an exotic such cone exists, it is a valid countermodel showing that pair self-duality cannot source FCC. The remaining routes would then be:
  - the four-token multiplicativity, OVL4;
  - the flagged local agency, or frame covariance.

**What is known about Q-SD** [W + X, with L steps marked].
- `twin` is not `cnot`-invariant: `cnot idW = chainW ∉ maxCone`, so Q-SD is not trivial.
- No cone linearly isomorphic to a Lorentz cone qualifies (S3 (a)).
- Orthogonal images of Q3 that qualify send pure products to pure states. That only Q3 and twin arise this way is a Wigner-type step [L, unverified] (S3 (b)).
- Every element of a qualifying cone satisfies `|y₋| ≤ |y₊|` for `cnot`'s eigenspaces. Their dimensions are 10 (+1) and 6 (−1), and its fixed part is self-dual in the 10-dimensional fixed space. Both follow from `<y, cnot y> ≥ 0` and averaging [W].
- An exotic cone containing `E0` would follow from a `cnot`-equivariant Barker–Foran extension. Such extensions are not automatic: for g = −id none exists in any nonzero dimension. Neither existence nor non-existence is established.

## 4. INDEPENDENT versus UNRESOLVED (stage 2)

**INDEPENDENT of L** (valid countermodels to the certified premises):
- **FCC**: `M_tok`, uniform `K_gen`, uniform `K_gen*`.
- **the required state space**: the `K_gen` system.
- **finite rank**: the clock model.
- **LT**: the register model and `paddedBall3`.

**UNRESOLVED:**
- Q-SD;
- the OI source of SDC, OVL4 in particular;
- purification;
- non-monomial, non-local operation families;
- a four-pair derivation of EvenCycle. S2 shows that one consistent pair system carries one orientation class; the four-pair parity is not derived.
- the framework-specific double-slit derivation (DS). L has no double-slit arrangement, observation ensemble or substratum pair system with which to state a countermodel.

**Route refuted** (a model of one route's premises in which the target fails), never INDEPENDENT:
- ordered associativity;
- induced pairs of a one-grouping composite;
- chart-invariant single-pair principles;
- uniform one-sided self-duality, both halves;
- orientation coherence alone, equivalently all-generated conditioning;
- one-sided conditioning C1 and C2;
- entanglement-swapping consistency;
- four-token no-restriction together with P3;
- "test generation ⇒ LT";
- "reversible gate with the product action and test generation ⇒ finite rank";
- "compactness ⇒ finite rank";
- "FCC on generated effects plus the pair hypotheses ⇒ the conclusion";
- (DS) "incomplete access plus reversible dynamics plus hidden records must produce the double-slit formula": refuted by `S_imp_D` [K] and exact non-quantum two-slit laws [X].

## 5. How much of K2 is resolved
None, at the certified level. On the routes examined, the composite-cone obligation now decomposes as follows:
- local tomography: CONDITIONAL on INV2 for data-generated systems;
- gate compatibility: by construction for generated cones;
- **completion of the state and effect spaces**: the missing ingredient, decided for the self-duality route by Q-SD;
- four-copy coherence: CONDITIONAL on SDC.

## 6. Kinds of evidence, for any external presentation
- **Computational findings**: exact, instance-scoped, every script replayed byte for byte and independently re-checked.
  - The 32-gate native family and its consistency rule.
  - The −1, −1/8 and −2 witnesses.
  - The clock ranks.
  - The register, rebit and hidden-parameter models.
  - The monomial witness ψ_w.
  - The frame-covariance words.
  - DS's checks:
    - the two double-slit formulas and their assumptions;
    - the CNOT-record visibility law on the certified table;
    - the classical model meeting the input's three requirements;
    - the coherent versus separable record and the eraser;
    - CHSH 2√2;
    - the phase-kick record outside `K_gen`.
- **Written arguments**:
  - SDC ⇒ FCC;
  - the meta-obstruction on renaming;
  - INV2 ⇒ LT;
  - finite-group rank bounds;
  - the clock pigeonhole step;
  - Theorems M and F;
  - the Lorentz exclusion;
  - the Q-SD structural facts.
- **Design-checked Lean [D]**: `kt4_forward_ie1`, Lemma B1 and the consumption sites.
- **UNBUILT Lean**: S3 §1.7 (`fourCopyCoherent_of_sdc`), S2 §1 (`ptq_of_invol`, `frameCov_iff_ie1`).
- **Certified [K]**: only the cited landed facts (`cnot`, `NativeGate`, ball self-duality, PSD self-duality, COMP-1, StageCompletion). No new kernel result.
- **Literature [L, unverified]**: Milman's converse, Schmidt, a Wigner-type classification, Aut(Lorentz), Kronecker's Hankel theorem, Barker–Foran, Müller–Ududec (a lead only).

## 7. Recommended next research (research-only; no governed rounds, no CI)
1. **Q-SD.** Decide whether a `cnot`-invariant self-dual cone containing the product states other than Q3 exists. Begin with the sharpest instance: is there one containing `E0`? This single question decides the self-duality route for both S2 and S3.
2. **OVL4's source.** Does the certified elementary self-duality of the ball, with a composition rule for the self-dualizing pairing, give multiplicativity for composites? This is S3's open motivation step.
3. **Orientation coherence across pairs.** Can the single-pair consistency classification (S2) be lifted to the four-pair parity EvenCycle without a frame or idle-extension premise?
4. **The double slit, if pursued.** Use DS's preregistrable rule (§3(d)), with the construction frozen and hashed first.
   - The single-CNOT-record visibility law is already computable from certified objects. It is a useful consistency-axis illustration, not a derivation from the substratum: the single system's own substratum sourcing is open.
   - The eraser, detector-family and Bell parts are downstream of Q-SD and the S2/S3 gap. Pursuing them first would not be a shortcut.
5. **Corpus hygiene.** The markers DS found (Explainer "derivation", Methodology's section citation, Main L664's "interference terms") are candidates for a future, owner-authorized propagation pass under AGENTS.md §A.25 and §A.30. They are held, as all repository changes are.

## 8. What is not claimed
- **No DERIVED label relative to L.** K2 is open, and nothing here is a kernel proof beyond the cited [K] and [D].
- **INV2 and SDC are named principles, not results.** Their observer-native sources are open.
- **Class impossibility statements are for the stated classes only.**
- **Bands are unchanged.** This is consistency-axis work.
