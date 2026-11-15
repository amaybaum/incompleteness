# Review of FOUND-ASSESS-r3

**Reviewer.** The independent, non-author reviewer of r1 and of the recheck of r2.

**Scope.** Paper-only and read-only. Sources at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`, read for this review:
- Substratum:
  - :92 and :216 (A1 and its support);
  - :249–:344 (Theorem 24, its proof and Corollary, the completeness remark, Propositions 24.2–24.4, the access remark).
- Main: :334, :445, :524, :642, :656, :722.
- Lean:
  - `RootedClassification.lean` (`PPer`, `FiniteRootedRealizable`);
  - `RootedClassificationAllTime.lean:192` (`finiteRootedRealizable_iff_pper`);
  - `SemigroupTransfer.lean:749` (`ST3_pairC`) and `pairC_wordTraces`.
- Issues:
  - #1169 c.6902061999 (the owner-confirmed central question);
  - #1147 c.6894144708 (the O-RDY plan r5 route table);
  - the A1 audit r9 (§0 categories, AM-2, the §14 P-units).

No computation and no Lean build.

**Verdict: ACCEPT WITH CHANGES.** Counts: blocking 0, required 5 (G1–G5), recommended 9 (G6–G14).

Every item of the recheck is applied correctly. §2b is well sourced and correctly cautious, and it answers the owner's three sub-questions. Five required changes concern §2b:
- G1: the scope of "finite representability constrains nothing at a fixed horizon";
- G2: a level and domain that is on record but missing (passive histories over all time, Main:642);
- G3: an understated claim about fibre-dependent relabelling;
- G4: the invariance criterion displayed as an equivalence;
- G5: a conflict with the exact target that the L-T all-time row omits.

Each is a local edit. None changes the placement verdict in kind, but G1 and G5 change what it says, and in opposite directions; see §3.

***

## 1. Recheck items in r3

| Item | Location in r3 | Confirmed? |
|---|---|---|
| R1 | C5′ premises | Yes |
| R2 | C5′ heading, "Preserves" | Yes. The writer's correction is sound: O-RDY plan r5 (#1147 c.6894144708) has a route row "R4. Recursive substates (#1007)", which requires "a normalized measure on the infinite carrier fixed by a stated principle, and a coupling of the deep sector to `R`". It is a *preparation route* of O-RDY that uses the C5′ carrier, not the carrier candidate itself (G11). The #1007 preregistered controls are quoted accurately |
| R3 | C5 "Excluded by" | Yes |
| R4 | §1.4, thermodynamic route | Yes. One duplicate sentence remains (G13) |
| F26 wording | C2 provenance; §6 | Yes ("one common structured hidden prior") |
| Bell row: frame dependence; frame-independent Bancal argument; balance (keeps (vii) and the SM/GR linear derivations; needs *c* to be the wave speed); Toner–Bacon replacing the pad image | §3 | Yes, all three |
| N1 | §1.2, §1.4 | Yes. Both reasons for the circularity are named. The added parallel with the original A1 justification is correct: Sub:92 and Sub:268 (i) read E3 "as a Hilbert-space dimension cutoff" bounding $\lvert\mathcal C_V\times\mathcal C_B\rvert$, and Sub:216 says "A1 … is supported by E3" |
| N2 | §3 | Yes |
| N3 | §1.4 grid | Yes |
| N4 | §2.4 | Yes |
| N5 | §1.4 | Yes |
| N6 | §2.1; C2 | Yes in §2.1. C2's wording needs a nit (G12) |
| N7 | C2; §6 | Yes |

***

## 2. The new central section §2b, with its entries in §0 and §5 (Q-R)

### What is accurate

**Theorem 24 (Sub:251–266).**
- (i), relabelling with a fibre-independent σ under the uniform hidden prior, preserves every Φ_t (L-C).
- A fibre-dependent relabelling "preserves the transition probabilities $T_{ij}(t)$ but not, in general, the coherent channels" (Sub:253).
- (iii), a finite decoupled factor, preserves the fixed-interface channel family.
- The proof (Sub:266) supports both points.
- Completeness is open (Sub:276).

**`ST3_pairC` (SemigroupTransfer.lean:749).** Two permutation unitaries on `Fin 2 × Fin 3` with equal `familyAt` at every t, and no unitary of any kind (hidden, visible or arbitrary) conjugating them, because their traces are 2 and 0. r3's "no hidden conjugacy" is accurate but weaker than the statement; see G6.

**Propositions 24.2–24.4 (Sub:280, :306, :331, :344).** Cited accurately, including Proposition 24.4's full-support and state-bound hypotheses, the de Bruijn counterexample without a bound, and "does not infer an all-time carrier from arbitrary finite-horizon laws".

**`finiteRootedRealizable_iff_pper`.** I read the Lean statement. `FiniteRootedRealizable Γ` says: there exist a finite hidden type, one `RootedRealization` (one reversible update on V × H and one prior shared by every root) and equality of the rooted maps at every t. `PPer Γ` says: Γ 0 = 1, Γ t is row-stochastic at every t, and Γ has a positive period. Both directions are kernel-proved (`pper_of_finiteRootedRealizable`; `pper_has_responseRealization`) for finite V. r3's "all-time finite representability of the rooted maps ⇔ periodicity (kernel)" is correct. So is "no finite record can test this".

**L-I.**
- E7: one finite representative per bounded instrument family, to any ε.
- E8: no exact qubit theory on a fixed finite carrier.
- E9: no fixed-dimension representation independent of the horizon.

All three are correctly placed.

**"L-H does not imply L-C" via Main:722.** This holds in window form. The law $X_1=0$, $X_2=X_0$ has a ledger realization and a swap realization with an initialized hidden slot, whose two-step maps differ on coherent inputs. The two realizations have different hidden carriers and priors, which is admissible when comparing equivalence classes. G3 gives a stronger witness: same interface, all time.

**The [IR] claim that Theorem 24 (i) and (iii) preserve L-H and every intervention acting on V alone.** Correct. For (i): the conjugation $\mathbb 1_V\otimes P_\sigma$ commutes with every operation on V, and the uniform prior is σ-invariant, so all multi-time and intervened data on V agree. For (iii): the decoupled factor is never accessed and has unit trace. Scope: (i) needs a σ-invariant hidden prior.

**The derivation trace (§2b.3).** Rows and sources check against the audit (AM-1.1 RM, AM-2.1 FIRM as finite-model mathematics, AM-22 with P7, AM-30 with P6, AM-16 and AM-32 RM, Theorem 23 untraced with P12). Its reading, that the gravity calibration and several SM results consume a counting measure or carrier bijectivity which a window representative fixes only by choice, is a fair statement of what the audit found. One row needs a correction (G9).

**The next step (§2b.5).** The level-and-domain table, built from the audit's RU, RD and RM categories, is cheap, paper-only and decisive for the owner's third sub-question. The L-C → L-H check is cheap. See G6 for a ready test object.

### G1 — required — §0 ("finite representability constrains nothing there"), §2b.2 ("Where finite representability constrains anything"), §2b.4 table

**Evidence.** "At a fixed horizon every law has a finite representative (E1)" is true at L-H, and at L-T. At L-I it is true for each finite table of statistics (Main:562: "a fixed finite table of statistics always has one"), and for bounded instrument families to accuracy ε (E7).

It is not true at L-C. A classical bijective representative with a diagonal hidden prior induces reduced channels with 0/1 partial-permutation Kraus operators. Those channels map configuration-diagonal states to diagonal states. Main:334: "the framework's channels are in that class" (diagonal-preserving; kernel `isDiag_Phi`). With E13 and E14 (`substratumGen_not_control`), this means no classical bijective representative reproduces a coherence-generating channel family, such as a Hadamard step. The restriction comes from the representative being *classical and bijective*, not from its being finite. #914 §4 says measure-preserving dynamics on an infinite or continuum carrier "plausibly stays inside the nonnegativity invariant" (unproved).

So at L-C the question "can the structure be represented finitely?" is dominated by "can it be represented classically?". The sentence "which level counts as physical … is the open interface question" understates this: if coherent access is physical, the obstruction is classicality at any cardinality.

**Fix.**
- Restrict "constrains nothing at a fixed horizon" to L-T, L-H and finite L-I tables.
- Add a row to §2b.4: FR(L-C, one window). Classical bijective representatives, finite or not on present evidence, yield only diagonal-preserving channel families (Main:334; E13, E14; #914 §4 for infinite carriers, unproved). The constraint is from classicality, not finiteness, and it is the interface question (O-ACC, O-INS) in L-C form.
- Mirror this in §0.

### G2 — required — §2b.4 table, §0 ("constrains only at two levels")

**Evidence.** Main:642: "any fixed realization with a fixed prior has an exactly L-periodic multi-time law ($\varphi^{k+L}=\varphi^k$) — a nonperiodic target admits no exact all-time realization by one fixed finite substratum." So FR(L-H, all time) implies an exactly periodic passive multi-time law. That is a third place where finite representability constrains, and it is on `main`.

The menu has the level (L-H) and the domain (all time), but §2b.4 has no FR(L-H, all time) row. The converse (every periodic multi-time law has a finite fixed realization) is not on record.

Reviewer's note, unchecked: a deterministic finite permutation with a fixed prior makes the passive record a finite mixture of periodic sequences. Its asymptotic entropy rate is then zero, so the "asymptotic entropy rate", which §2b.2 lists as a window artefact, becomes an invariant (= 0) under FR at this level.

**Fix.** Add the row with Main:642, give its direction only (§A.34), and change "two levels" to three in §0 and §2b.2.

### G3 — required — §2b.1, L-T row ("A fibre-dependent relabelling preserves L-T only (Sub:253)") and "How the levels relate"

**Evidence.** Sub:253 says the fibre-dependent relabelling preserves $T_{ij}(t)$ "but not, in general, the coherent channels". It does not say that it preserves L-T *only*.

Reviewer's argument, elementary, for the paper's uniform hidden prior: let $\pi(v,h)=(v,\sigma_v(h))$ and $\varphi'=\pi\varphi\pi^{-1}$. Then $\pi_V\varphi'^t(x_0,h_0)=\pi_V\varphi^t(x_0,\sigma_{x_0}^{-1}h_0)$. So the whole visible trajectory under φ′ is the trajectory under φ composed with the map $(x_0,h_0)\mapsto(x_0,\sigma_{x_0}^{-1}h_0)$. That map is a bijection preserving every visible root law times the uniform hidden prior. Hence all passive multi-time laws agree at every horizon (L-H, all time).

The same pair differs at L-C (Sub:253), and generally under interventions on V, because an intervention that changes $v$ breaks the fibre-wise correspondence. "Preserves L-T only" is therefore an understatement. The pair is a same-interface, all-time witness that L-H does not imply L-C, stronger than Main:722's window example.

**Fix.**
- L-T row: "preserves L-T and L-H (all time, under the uniform prior), not L-C (Sub:253) [IR]".
- "How the levels relate": add it as the all-time witness.

### G4 — required — §2b.2, "The invariance criterion"

**Evidence.** "A statement is invariant across all finite representatives at level X exactly when it is a function of the level-X data. Sub:268 (iii) states this for the decoupled extension." This is a displayed equivalence, so §A.34 asks for each direction:

- *Function of the data ⇒ invariant.* Immediate. Sub:268 (iii) states this direction only, and only for the decoupled extension.
- *Invariant ⇒ function of the data.* True only under the reading "constant on each equivalence class", where it is definitional.

Under the other natural reading, "true of every finite representative", the criterion fails. Finite order, exact recurrence, and PPer over all time hold in every finite representative, but they are consequences of finiteness, not functions of window data. They are exactly the content §2b.4 assigns to FR.

**Fix.** State the reading ("constant on each class"). Cite Sub:268 (iii) for the transfer direction only. Add one sentence separating class-invariant statements from statements true of every finite representative.

### G5 — required — §2b.4, FR(L-T, all time) row and "Standing"

**Evidence.** PPer requires exactly periodic rooted maps. Exact quantum dynamics at integer times gives $T_{ij}(t)=\lvert\langle i\vert U^t\vert j\rangle\rvert^2$. For eigenphases that are not rational multiples of 2π, this is generically not periodic: for a qubit, $T_{01}(t)\propto\sin^2(\omega t/2)$, which is periodic in integer t only for rational ω/2π. So FR(L-T, all time) also excludes exact QM with incommensurate spectra, the same kind of conflict with #914 decision 2 (exact target) that the table records only for L-I.

The reasoning is the reviewer's own, elementary, and unchecked against a source. In the other direction, FR in any form drops C5's claim about the ontic carrier. It is therefore compatible with #1007's decision ("must not require |S|<∞"), which C5's total form is not.

**Fix.**
- FR(L-T, all time) row: add "excludes exact QM with incommensurate spectra; conflicts with #914 decision 2 in the exact limit".
- "Standing": add "compatible with #1007's decision, unlike C5's total form".

***

### G6 — recommended — §2b.1, L-C row, and next step 2

`ST3_pairC` uses two involutions ($\varphi_C^2=\varphi_C'^2=1$, in its proof) with equal Φ_t at every t. Then $X_2=X_0$ in both, and with equal $T(1)$ the passive laws from every root under the uniform prior agree at all times. This is the reviewer's argument, unchecked: the pair also agrees at L-H. But `pairC_wordTraces` shows unequal block-word traces, which is Proposition 24.2's data. So the menu has a rung between L-C/L-H and L-I, coherent block-word traces, at which this pair already differs. `ST3_pairC` is also a ready test object for next step 2. Add the rung, or a note on it.

### G7 — recommended — §2b.1, definition of L-H

L-H ⇒ L-T holds only if L-H is rooted: passive laws from every root, or under a full-support visible prior. Say so.

### G8 — recommended — line citations

"Sub:247" (the datum sentence, and L-C ⇒ L-T) should be Sub:249. Sub:247 is the section heading.

### G9 — recommended — §2b.3, row "SM results proved for every q"

The results proved for every q need no hypothesis (Sub:266 (ii): "the results [SM, §2.7] proves for every q ≥ 2 are preserved without it"). The alphabet-size hypothesis is needed only for the results that carry q. Note also that results for every finite q do not cover an infinite alphabet (C5′).

### G10 — recommended — Q-R "Separates"

§2b.4 says window-level FR cannot separate C5 from C5′. Q-R should say that it separates which derivations need A1-type premises (a counting measure or carrier bijectivity), and that only the all-time and all-intervention levels bear on C5 versus C5′.

### G11 — recommended — C5′ heading

Write "related O-RDY route R4 (Recursive substates, #1007)", since R4 is a readiness route that uses the infinite carrier, not the carrier candidate itself.

### G12 — recommended — C2 (N6 wording)

D-CQ amends the soundness requirement of the Gate A answers (#1169 c.6876591512). It does not say that it supersedes #914 c.6875548603. §2.1's wording is correct; bring C2 into line with it.

### G13 — recommended — §1.4, thermodynamic route

The sentence "the noise floor needs a source; in OI it could be the trace-out itself" now duplicates the preceding "with the trace-out as the noise". Delete one.

### G14 — recommended — §2b.1, L-H row

The EF-1 r7 statements are a reviewed draft off `main`. They are support off `main` in the sense of §A.42 item 8, and were not checked by this review. Say so beside "checked".

***

## 3. Is the placement verdict fair?

The verdict is: at window level identical to C1; over all time or all interventions, C5 restated on equivalence classes; not a new candidate.

**Does it oversell?** No. The window-level identity with C1 is right at L-T and L-H: E1 and GR:132 give finite representatives for finite and infinite carriers alike. The all-time and all-intervention content (PPer, Main:642's periodic multi-time law, E8) are C5's consequences and cannot be tested from finite records. "Not a new candidate with its own prediction" follows under §A.29.

**Does it undersell?** In two respects, and both should be written in (G1, G5).

1. **The L-C constraint is missed.** At L-C the formulation carries a real window-level constraint that r3 misses, and it is not about finiteness: classical bijective representatives give only diagonal-preserving channel families. That is a substantive answer to the owner's "which predictions are invariant". If coherent channels are physical data, no classical representative of any cardinality matches them on present evidence. The open question is then classicality and access, not finiteness.
2. **FR is weaker than C5 as a premise.** It drops the ontic claim, and so is compatible with #1007's decision where C5's total form is not. It shares the conflict with the exact target (G5).

Neither point makes FR a separate candidate. Both change what the owner is told about where finiteness matters and where it does not.

***

## 4. New errors and balance

- **New errors:** none beyond G1–G14.
- **Null option:** a candidate, not a verdict, in §0, C0 and Q-A.
- **Finiteness:** open throughout.
- **§2b:** no premise adopted and no recovery credit given ("traced, not asserted"; the [IR] items are labelled).
- **Q-R:** ranking it second, under Q-A, is defensible, given the owner's designation and its bearing on every A1-dependent derivation.

***

## 5. Not checked

- EF-1 r7, which is off `main`.
- The separate Theorem 23 trace, which is not yet available.
- External literature.
- My own arguments in G2, G3, G5 and G6 are short and unchecked by a second reader.
- No Lean build; Lean statements were read from source.
