# THM24-DEF: the candidate definition of $\mathcal G_{\rm sub}$ against the corpus

**Status: research, unreviewed (WIP / UNVERIFIED).** Authorized as the Theorem 24 supporting
thread at [#1169 c.7064767045](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064767045).
Stacked on #1486's reviewed head `8b478284`. Nothing here edits a manuscript or touches #1477,
#1492, #1493 or #1494. No new computation was run; Lean results are cited at the strength their
modules prove, and every step of my own is marked as paper-level.

The proposal under test is `DEFINITION-PROPOSAL.md` at `8b478284`, written $\approx_I$:

- clause (B) is A2, a bijection;
- clause (I) is equality of the single-time coherent family $\{\Phi_t\}$ at a fixed partition, with prior $\omega_H$ part of the datum and identification $\iota:\mathcal C_V\to\mathcal C'_V$;
- the population variant $\approx_I^{\rm pop}$ is defined beside it.

Line numbers are those of `main` at `df6da1c6`. "Ledger" names a #1477 edit on the line; those
lines are frozen and route only to #1477's final scientific review.

## 1. Classification rule (fixed before the sweep)

Each use of $\mathcal G_{\rm sub}$ or a synonym ("substratum gauge group", "equivalence class of
substrata", "$[(S,\varphi)]/\mathcal G_{\rm sub}$", "representative freedoms", "Level G3") gets one of
three verdicts under $\approx_I$:

- **T**: true as written.
- **H**: true under a stated hypothesis, which is named.
- **F**: false as written.

A sentence that defines or describes $\mathcal G_{\rm sub}$ is T when its description is an accurate
description of $\approx_I$. Every verdict is evidence about the proposal, not about the corpus's
intended meaning.

Sweep: every line of `papers/*.md` and `book/*.md` (FULL.md located by exact-line mirror) matching
`G}_{\text{sub}}`, `G}_{\rm sub}`, `G_sub`, "substratum gauge group", "substratum-gauge",
"equivalence class of substrata", `]/\mathcal`, "gauge-equivalent representative" or
"representative freedoms". The sweep found 119 matching lines. One of them, ch15:196 ($G_{\text{sub}}^{(2)}$, a density correlation), is unrelated, which leaves 118 uses; the review reproduced about 117 with its own escaping. After review, the sweep was extended to "gauge-classification theorem" (§3a). Lean and record hits are in §4.

## 2. The decisive branch: completeness under the proposal

The proposal's (I) is the single-time family. The corpus's Lean modules on Theorem 24's
completeness question (Substratum Lemma 24.1/24.1A, `OIBridge/SemigroupTransfer.lean`,
`OIBridge/WordTraceSufficiency.lean`, cited at Substratum:276–282) bear on it directly.

**Lean, as proved.** `ST3_pairC` exhibits two permutations $\varphi_C,\varphi_C'$ of
$\mathrm{Fin}\,2\times\mathrm{Fin}\,3$ with:

- trivial hidden commutants;
- equal uniform-prior families `familyAt U t = familyAt U' t` at every $t$;
- traces $2$ and $0$.

`ST4_pairC` adds that no $P_\sigma\otimes W$ ($\sigma$ any visible permutation, $W$ any hidden
unitary on $\mathbb C^{H\times D}$) relates $\varphi_C'\otimes\delta'$ and $\varphi_C\otimes\delta$
for any unitaries $\delta,\delta'$ on any finite non-empty $D$. Lemma 24.1's preregistration frames
ST4 as a single-step bound and says it does not settle completeness
(`programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md:264–321`).

**Consequence 1 (exact from Lean).** $\varphi_C\approx_I\varphi_C'$, with $\iota=\mathrm{id}$ and
$\omega_H$ uniform on both: (B) holds because both are permutations, and (I) is `pairC_family`.

**Proposition A (paper-level proof sketch; mine; unreviewed).** No finite sequence of the
following moves carries $U_{\varphi_C}$ to $U_{\varphi_C'}$:

- (M1) hidden unitary conjugation, which contains generator (i);
- (M2) visible relabelling by $P_\sigma\otimes 1$, which is the proposal's $\iota$;
- (M3) decoupled enlargement $U\mapsto U\otimes\delta$ by a unitary $\delta$ on a finite non-empty $D$, which contains generator (iii) with a finite factor, $\delta=P_\psi$;
- (M4) reduction, the inverse of M3, applicable when $U=U_0\otimes\delta$.

*Sketch.* For a balanced block word $w$ (plain and adjoint letters equal in number), put
$\tau_w(U)=\operatorname{Tr}\,\mathrm{wordEval}(U,w)/\lvert H\rvert$.

- M1 leaves $\tau_w$ unchanged (`trace_wordEval_hiddenConjugate`).
- M3 multiplies the trace by $\lvert D\rvert$ (`trace_wordEval_enlarge`) and the hidden dimension by $\lvert D\rvert$, so it leaves $\tau_w$ unchanged; so does M4, its inverse.
- M2 replaces $w$ by $\sigma\cdot w$ (`trace_wordEval_conj`).

So for a $\mathrm{Sym}(V)$-orbit $\Omega$ of balanced words, the multiset
$J_\Omega(U)=\{\tau_w(U)\}_{w\in\Omega}$ is invariant under M1–M4. Take
$\Omega=\{w_0,w_1\}$, $w_1=\mathrm{swap}\cdot w_0$, the two words of `pairC_wordTraces`:

- $J_\Omega(\varphi_C')=\{0,0\}$ (that theorem's second and third conjuncts);
- $J_\Omega(\varphi_C)$ contains $\tau_{w_0}(\varphi_C)=1/3$ (its first conjunct).

The multisets differ, so no chain exists. $\square$

**Consequence 2.** Under $\approx_I$, the groupoid generated by (i) and finite-factor (iii)
(widened to M1–M4) does **not** exhaust $\mathcal G_{\rm sub}$. The pair is joined by an arrow that
no such chain reaches.

- *Dependencies:* the four Lean lemmas named, at the strength their module proves.
- *Not covered:*
  - family (ii);
  - enlargements by infinite or classical measurable factors (where $\tau_w$ is undefined);
  - moves of any other form.

  It is open whether these reach the pair.
- *Classification:* NEW relative to the corpus, which states completeness as open (Substratum:276). Admitted class (both endpoints and every M3 with $\delta=P_\psi$ satisfy A2).

**The interface hinge has three branches (paper-level; confirmed by review c.7064909915).**

- **Interventional multi-time.** With coherent visible interventions $
ho\mapsto K
ho L^\dagger$
  between steps, the hidden operator evolves as $X\mapsto BXB'^\dagger$. A three-time correlation is
  then $\operatorname{Tr}(B_3B_2B_1B_1'^\dagger B_2'^\dagger B_3'^\dagger)/\lvert H
vert$. The word
  $w_0=U_{00}U_{10}U_{01}U_{00}^\dagger U_{01}^\dagger U_{10}^\dagger$ has exactly this form, with
  ket-path blocks $(01,10,00)$ and bra-path blocks $(00,01,10)$. So such data separate pair C, and
  Proposition A is vacuous for that interface.
- **Passive multi-time.** Readouts with equal ket and bra paths do not yield $w_0$.
- **Single-time family.** The family sums over internal indices and does not yield $w_0$.

The corpus states $\sim$ as the single-time family: Substratum:249/253, Structure Def. 9.3, and
Substratum:276's framing of ST3. `PassiveQuotient.lean:57–66` treats interventions as outside the
specified data. **On that stated reading, Proposition A refutes completeness for (i) plus
finite-factor (iii), with visible relabelling.** Substratum:276's "open" then survives only
through (ii) and infinite or classical factors.

**Earlier note on the definition, superseded by the three-branch statement above.** Lemma 24.1's preregistration describes the full block-word traces as
"all multi-time correlation data, not only the family" (`…/preregistration.md:126, 281–285`), and
`pairC_wordTraces` shows the pair differs on them. That reading is a dependency I have not
verified. If it holds, then adding multi-time statistics with visible interventions to $I(D)$, the
open point of `DEFINITION-PROPOSAL.md` §7, would likely separate $\varphi_C$ from $\varphi_C'$. The
choice of interface therefore decides whether Proposition A refutes completeness or is vacuous.
This is the main open decision for the definition.

## 3. Corpus uses under the proposal (papers and book)

Sites not listed below are T. That covers the definitional or descriptive uses of
$[(S,\varphi)]/\mathcal G_{\rm sub}$ as the framework's object, the Level D × G3 placements and the
"not established" inclusions. The T sites are: Substratum:16, 26, 32, 36, 201, 241, 249, 251, 292,
298, 367, 393, 395, 429, 451, 455, 471; Structure:13, 27, 29, 56, 86, 88, 132, 142, 158, 167, 179,
193, 196, 206, 258, 331, 359, 373, 377, 644–654, 679, 687, 693, 695, 742, 780, 848, 1301;
SM:14, 1370, 1372, 1400, 1586; GR:30, 561; Computation:254 = ch14:234 (on the proposal the relation
partitions the A2 data, so "partitions the space of bijections" is exact); ch02:10, 126, 132, 138,
162, 168, 182, 200, 210, 220, 222; ch03:8, 12, 82, 88, 92, 98, 104, 202, 204, 234; ch05:43;
glossary:137; README:52. Structure:64/68 are a proposal that Structure §6 itself rejects; under
$\approx_I$ they are F, since the matrix-model formulations fail (B), in agreement with Structure §6.

| Site (mirror) | Ledger | Verdict | Reason under $\approx_I$ |
|---|---|---|---|
| Methodology:473 | — | **F** | "classified by the gauge-classification theorem … the theorem classifies transformations that preserve every observable". Theorem 24 classifies nothing: completeness is open (Substratum:276), and under the proposal finite (i)+(iii) are shown not to generate (§2). "every observable" also exceeds (I) |
| Methodology:485 | — | **F** | "given the substratum gauge group classified by Part II": as for :473 |
| Structure:347 | — | **F** | "classifies observationally-equivalent substrata within OI's structural class": as for :473 |
| Structure:375 | D074 | **F** | "it classifies equivalence among substrata satisfying OI's A1–A6". D074's new text keeps "classifies" |
| ch09:258 = FULL:2673 | — | **F** | Three problems: (a) "the invariance group of embedded observation itself … that no observation can distinguish" exceeds (I); (b) "the phase conventions of quantum mechanics are among its gauge directions" and the vacuum-energy offset "is another" place Level-1 emergent freedoms in $\mathcal G_{\rm sub}$, whereas Substratum:298 says inclusions between levels are not established and Substratum:288 says the emergent global phase is the identity on $(S,\varphi)$; (c) "the boundary … is drawn by $\mathcal G_{\rm sub}$-invariance itself" presupposes the classification |
| Substratum:300 (ch02:136 = FULL:766; ch03:84 = FULL:945) | ch02:136 D128, FULL:766 D129; ch03:84 D142, FULL:945 D143 | **H** | "all observables are preserved" / "the observability condition": true when read as (I). #1493 corrects Substratum:300; ch02:136 is routed (P4b); **ch03:84 is a further mirror under the ledger (D142), not listed before** |
| Substratum:24 | — | **H** | "the kernel of this inverse map … whose exhaustion of all observables-preserving operations … is open": true with "observables" read as (I); the kernel is the fibre relation of $D\mapsto I(D)$ |
| Substratum:276 | — | **H** | "observables-preserving": as for :24 (corrected in #1493). Its question "lies in the group generated by (i)–(iii)" is answered **negatively** under $\approx_I$ for finite factors without (ii) (§2) |
| ch19:234 = FULL:5304 | — | **H** | "the transformations preserving all observables of $(S,\varphi)$": hypothesis (I); otherwise as Substratum:300 |
| Structure:49 | — | **H** | "the equivalence class of substrata producing the same emergent physics": hypothesis (I) |
| Methodology:351, 463 | — | **H** | :351 "produce identical observables", :463 "no observation distinguishes the relabeled substrata": hypothesis (I) with a uniform (or $\sigma$-invariant) prior |
| Methodology:283 = ch04:36 | — | **H** | "the substratum gauge group identifying which structure is observable": hypothesis (I) |
| Structure:156 = Prop. 9.5 (:646) | :646 D076 | **H** | (i), (iii) arrows give the same $(\mathcal A_V,\Phi_t)$ under the *-isomorphism induced by $\iota$, so G4 contains them. True for (i) with a $\sigma$-invariant prior |
| SM:563 | — | **H** | "$(S,\varphi)/\mathcal G_{\rm sub}$ is invariant under the cubic translation group (NN3)": a translation conjugate of $\varphi$ at a fixed partition is an arrow only if the rule commutes with translations, i.e. under A4 (up to its gauge). Hypothesis A4 |
| SM:1394 | — | **H** | "properties of the equivalence class … hold for every bijection satisfying the six structural properties": the $\approx_I$-class of one $\varphi$ is not the set of A1–A6 bijections. True for properties derived from A1–A6 alone |
| ch06:199 = FULL:1710; ch06:323 = FULL:1834 | — | **H** | "not derivable … in any framework consistent with $\mathcal G_{\rm sub}$-invariance" / "gauge-forbidden": needs an arrow that exchanges the generation assignments. No such member is exhibited, so this is a dependency, not established |
| ch02:150, 174 | — | **H** | "any observables-preserving transformation of that scoped datum" / "related by the generators": hypothesis (I), already scoped by "that scoped datum" |
| Substratum:233 (box) | D028 | **H** | a displayed ⟷ whose right side is the class modulo $\mathcal G_{\rm sub}$. Its §A.34 directional witnesses are Theorem 23's business and were not checked here |
| ch03:34 | D134 | **T** | "relates some … within OI's specific structural class" |
| ch09:36 = FULL:2451 | D170 | **T** | descriptive |

**Population variant.** Every **H** verdict above that rests on (I) is **F** under
$\approx_I^{\rm pop}$ wherever the sentence names coherent channels. For example, Substratum:249/253 state
(i) on the coherent family, and fibre-dependent relabelling preserves populations but not
coherences (Substratum:253). In addition, `OIBridge/PassiveQuotient.lean:57–66` places
`hiddenExt φ σ` "at the observational-equivalence level (Structure's Level G4) … NOT at the
substratum gauge group G3". `hiddenExt` is a bijection (an `Equiv.Perm`). It preserves the passive
visible law for every prior with the right marginal (`hiddenExt_same_law`), so it satisfies
(B) and $\approx_I^{\rm pop}$. With a fibre map that depends on the visible coordinate it changes
the coherent family: #1486's replayed control K2 (classical) changes the family in 20 of 96 cases.
$\approx_I$ therefore agrees with the module's placement, and $\approx_I^{\rm pop}$ contradicts it.
**Recommendation:** the proposal should not offer $\approx_I^{\rm pop}$ as a reading of
$\mathcal G_{\rm sub}$, only as a separately named population relation.

## 3a. The "gauge-classification theorem" family (added after review c.7064909915)

The sweep's patterns did not include the title Methodology uses for Theorem 24. Every non-FULL hit
for "gauge-classification" is classified below. There is no book hit, and no FULL.md hit.
**No line is under the #1477 ledger** (checked against `edits.json` at `55544cc3`). Within the same
paper, Methodology:355 says "exhaustiveness is open".

The title itself names Theorem 24 a classification, which it does not give: it gives generators
whose completeness is open, and under $\approx_I$ completeness fails for (i) plus finite (iii)
(§2). A title-only use is graded **H**: true when the title is read as naming Theorem 24 and the
sentence claims nothing beyond it. A use that asserts the classification, or a consequence that
needs it, is graded **F**.

| Site | Text (abridged) | Verdict |
|---|---|---|
| Methodology:43 | "the uniqueness and gauge-classification theorems — established in the framework's technical papers" | **F**: "established" for a classification |
| Methodology:323 | "Two theorems carry the claim — a reconstruction theorem and a gauge-classification theorem" | **H** (title) |
| Methodology:349 | heading "THE GAUGE-CLASSIFICATION THEOREM: EXHIBITING THE SURPLUS" | **H** (title) |
| Methodology:357 | "posed as a finite classification, whose completeness is open" | **H**: self-scoped |
| Methodology:427 | "say there is no such further fact: within the equivalence class the choice of representative is, provably, without empirical content" | **H**: "empirical content" read as the fixed-interface data; another interface may distinguish (`PassiveQuotient.lean:57–66`) |
| Methodology:433 | "gives its representatives by enumerating the relevant transformations, whose completeness is open" | **H**: self-scoped |
| Methodology:453 | "carried out up to the open exhaustiveness of step two's classification" | **H**: self-scoped |
| Methodology:473 | "classified by the gauge-classification theorem … the theorem classifies transformations that preserve every observable" | **F** (§3) |
| Methodology:477 | "The structural form is the one the framework's gauge-classification theorem identifies" | **H** (title) |
| Methodology:479, first use | "the gauge-classification theorem establishes that observation, structurally, cannot reach the substrate's gauge equivalence class" | **F**: same status claim as :473, and it exceeds (I) |
| Methodology:479, second use | "in a way the gauge-classification theorem makes precise" | **H** (title) |
| Methodology:485 | "given the substratum gauge group classified by Part II" | **F** (§3) |
| Methodology:489 | "the gauge group classified by the gauge-classification theorem" | **F**: repeats :485 |
| Complexity:214 | "not an all-observations gauge-classification theorem" | **T**: a negative, scoped |

The F class in Methodology is therefore :43, :473, :479 (first use), :485 and :489, all off the
ledger, together with Structure:347 (off) and Structure:375 (D074).

Proposed minimal correction, as a record only: replace "classified/classifies" by "with
generators exhibited by" at the F sites. Optionally, rename the title "gauge-generator theorem" at
all eleven Methodology title sites. Routing is an owner decision.

## 4. Lean and records

- **Lean.**
  - No module defines $\mathcal G_{\rm sub}$.
  - `SemigroupTransfer` and `WordTraceSufficiency` concern Theorem 24's completeness question (§2): Proposition 24.2, cited at Substratum:282, is `WT3_spanning_iff`.
  - `PassiveQuotient` places its passive quotient at G4, not G3 (§3).
  - `OperationalSourcing.padData_rooted` is a population-level padding identity with no membership claim.
  - *Correction to #1486:* NOTE.md §7 ("No Lean statement concerns $\mathcal G_{\rm sub}$ or Theorem 24") overstated the absence. The completeness modules concern Theorem 24. The forward correction is in NOTE.md on this branch.
- **Records.** 34 record files mention $\mathcal G_{\rm sub}$ or a synonym. Most quote manuscript text inside frozen audits (`pr982-minimization-20261028/reports/*`, `post982-minimum-diff-20261030/*`, `a1exit-regression-20261121/snapshot.json`, SC-42 predicates). Those are provenance, not claims, and I did not classify them. Records that make claims of their own:
  - `audits/foundations/phase-source-audit.md:43,74,262`: the emergent global phase is the identity on $(S,\varphi)$. **T**, and consistent with ch09:258 being **F**.
  - `intro-corpus-audit-20261026/tracks/SC45-generator-soundness/README.md:45`: already asks whether the object is "an equivalence relation or groupoid". The proposal answers: a groupoid.
  - `programmes/substratum/interface-audit.md:104`: A4's gauge is a parameter subgroup of $\mathrm{Perm}(\mathrm{Conf})$, a different object (A4's translation gauge). No conflict.
  - `programmes/hydrodynamics/round-h-d-source-reconciliation/result.md:266,337,342`: quotes "the four $\mathcal G_{\rm sub}$ generators" from an older ch05:47. That text is not on `main` now (no hit for "four … generators"). Historical; no action.
  - `programmes/substratum/lemma-24-1*`: §2.

## 5. Theorem 24 scope beyond the sites already found

Labels (#1169 c.7064066427 item 6):
- **admitted**: A2 dynamics, finite $\mathcal C_H$ with the uniform prior for (i);
- **larger**: non-bijective or non-permutation dynamics, a non-uniform prior.

| Site | Ledger | Finding | Class |
|---|---|---|---|
| ch03:84 = FULL:945 | D142 (FULL:945 D143) | F4 mirror (see §3); add to #1477's final scientific review with P4b | interface scope |
| Methodology:473, :485; Structure:347; Structure:375 (D074) | :375 D074 | "classified/classifies": stronger than Theorem 24, a soundness statement whose completeness is open | admitted (the claim is about A2 substrata); an overstatement of status, not of class |
| ch09:258 = FULL:2673 | — | Places Level-1 emergent freedoms (QM phase conventions, the vacuum-energy offset) in $\mathcal G_{\rm sub}$ | outside both classes: not a transformation of $(S,\varphi)$ (Substratum:288, 298) |
| ch06:199, 323 | — | Uses $\mathcal G_{\rm sub}$-invariance to exclude a derivation, with no member exhibited that acts on the assignment | admitted; dependency unestablished |
| SM:563 | — | NN3 invariance holds under A4 | admitted, under A4 |
| Methodology:463 | — | Relabelling surplus "because no observation distinguishes": prior and interface unstated | admitted dynamics, larger prior class (as F1–F3) |
| Appendix tables (`book/appendix-a…`, `-b…`, `-c…`) | — | No Theorem 24 or $\mathcal G_{\rm sub}$ row | — |

Proposed corrections, as a record only (routing is an owner decision):

- **Off-ledger:**
  - Methodology:473/485, Structure:347: "classified" → "with the generators exhibited by" (or "whose exhibited generators"); "every observable" → "the specified fixed-interface data".
  - ch09:258: remove the two Level-1 items from $\mathcal G_{\rm sub}$, and state the invariance as relative to the fixed interface.
  - ch19:234: as P4a.
- **Under the ledger, for #1477's final scientific review:**
  - Structure:375 (D074), "classifies" → "relates";
  - ch03:84 (D142) and FULL:945 (D143), as P4b, which also covers ch02:136 (D128) and FULL:766 (D129).

## 6. Lean design (design only; nothing written or built)

The existing modules already carry every ingredient for the finite form:

- `SemigroupTransfer`: `familyAt` (uniform-prior family), `HiddenConjugate`, `enlarge`, `wordEval`, and the trace lemmas;
- `PassiveQuotient`: `trajProb` (population law) and `hiddenExt` (negative control);
- `OperationalSourcing.padData`.

```lean
-- Finite form of DEFINITION-PROPOSAL.md (proposal only).
structure SubDatum (V : Type) [Fintype V] [DecidableEq V] where
  H : Type
  [fH : Fintype H] [dH : DecidableEq H] [nH : Nonempty H]
  φ : Equiv.Perm (V × H)                -- clause (B): A2 holds by typing
  ω : Matrix H H ℂ                       -- the prior is part of the datum
  hω : ω.PosSemidef ∧ ω.trace = 1

/-- The single-time coherent family at the fixed partition (Substratum:253). -/
noncomputable def SubDatum.family (D : SubDatum V) (t : ℕ) (ρ : Matrix V V ℂ) : Matrix V V ℂ :=
  traceH ((D.φ.permMatrix ℂ) ^ t * (ρ ⊗ₖ D.ω) * ((D.φ.permMatrix ℂ) ^ t)ᴴ)
  -- `traceH` is the partial trace over H; reuse the block-trace form of `familyAt`

/-- Clause (I) with the identification ι of the interfaces. -/
def Arrow (D : SubDatum V) (D' : SubDatum V') : Type :=
  { ι : V ≃ V' // ∀ t ρ, D'.family t (ρ.submatrix ι.symm ι.symm)
                       = (D.family t ρ).submatrix ι.symm ι.symm }
```

Targets, in order of cost:

1. `family_uniform_eq_familyAt`: with `ω = (card H)⁻¹ • 1`, `family = familyAt`. This is the bridge that lets the existing results be consumed.
2. `Arrow.id`, `Arrow.comp`, `Arrow.symm`, then `CategoryTheory.Groupoid` on `Σ V, SubDatum V` or on a fixed `V`, and `Equivalence (fun D D' => Nonempty (Arrow D D'))`.
3. `gen_i`: a hidden permutation `σ` with `P_σ ω P_σᴴ = ω` gives an arrow (`ι = id`). A control: `ω` non-invariant gives none for some φ (the K3 pattern).
4. `gen_iii`: `enlarge` by `P_ψ` with prior `ω ⊗ σ_A` gives an arrow. A control: an unnormalized `σ_A` scales the family (K1).
5. `pairC_arrow`: from `pairC_family`.
6. `pairC_not_generated`: no `Relation.ReflTransGen` chain of M1–M4 joins pair C. Proved by the invariant `J_Ω`, through `trace_wordEval_hiddenConjugate`, `trace_wordEval_enlarge`, `trace_wordEval_conj` and `pairC_wordTraces`. The new content is the chain invariance (Proposition A); the M4 step needs a uniqueness-of-factorization hypothesis, or M4 can be stated as "an M3 read backwards".
7. `hiddenExt_pop_not_coherent`: `hiddenExt` with a visible-dependent fibre map gives a population arrow and no `Arrow`. That puts PassiveQuotient's placement into the kernel.

Out of scope for a first round: the classical measurable form (the Main:336 family; would need
`MeasureTheory`), infinite factors, family (ii), and multi-time interfaces. Lean work needs its
own authorization and preregistration.

## 7. Established / Assumed / Missing (owner standard, #1169 c.7064859041)

Labels used in this record (assumptions are numbered AS1–AS6, to keep them apart from the axioms A1–A6):

- **(N)** holds from the corpus's own definitions and Lean results, with no imported assumption;
- **(I)** holds conditionally on a named imported assumption, listed under *Assumed*.

**Established**

| Result | Layer | Label |
|---|---|---|
| Pair C: two permutations, equal uniform-prior single-time families at every $t$, trivial hidden commutants (`ST3_pairC`, `pairC_family`) | Lean, cited | (N) |
| Pair C is an arrow of $\approx_I$ | Lean plus definition | (I): single-time interface (AS1 below) |
| `ST4_pairC`: no single step $P_\sigma\otimes W$ after unitary finite enlargement | Lean, cited | (N) |
| Proposition A: no finite M1–M4 chain joins pair C | paper-level; confirmed by review | (N) as mathematics. Its reading as "(i) plus finite (iii) do not generate $\mathcal G_{
m sub}$" is (I): AS1 |
| $w_0$ is a three-time interventional correlation; passive and single-time data do not yield it | paper-level; confirmed by review | (N) |
| `PassiveQuotient` places `hiddenExt` at G4, so $\approx_I^{
m pop}$ conflicts with it | Lean comment plus prose | (N) |
| The verdicts of §§3, 3a and 5 | prose reading | (I): AS1 and AS5 |
| The K2 (classical) control of #1486, replayed | exact computation, enumerated set | (N) |

**Assumed** (each with where it enters)

- **AS1. Single-time interface.** $\sim$ is equality of the single-time coherent family $\{\Phi_t\}$
  at a fixed partition. It enters in §2, where pair C becomes an arrow, and in every **H**/**F**
  verdict that reads "observables" as (I). Source: Substratum:249/253, Structure Def. 9.3. It is not
  derived from OI; it is the corpus's stated reading.
- **AS2. Finite non-empty factors with unitary $\delta$.** Enters M3 and M4 and `trace_wordEval_enlarge`.
- **AS3. Uniform prior on pair C.** Enters through `familyAt`, which is uniform-prior by definition.
- **AS4. M4 factorization.** A reduction applies only to an exact product $U_0\otimes\delta$, read as
  M3 backwards. Enters Proposition A's chain.
- **AS5. Prose readings.** The verdicts of §§3, 3a and 5 rest on my reading of each sentence's scope.
  Enters every verdict.
- **AS6. Lean hypotheses, as the cited theorems state them.** `[Fintype D] [Nonempty D]`; `δᴴ * δ = 1`;
  a balanced word (`hw`); `Wᴴ * W = 1`.

**Missing**

- **The earliest unsupported step is the interface choice: single-time, passive multi-time or
  interventional multi-time** (§2). It is a definitional or physical decision, not mathematics. On
  the single-time branch the corpus states, completeness of (i) plus finite (iii) fails. On the
  interventional branch, pair C is not an arrow.
- **Mathematics:** Proposition A's extension to family (ii) and to infinite or classical factors.
- **Mathematics or Lean:** a kernel statement of Proposition A (§6 target 6).

## 8. Summary of earlier findings, by layer


- **Lean (cited, not re-run):** pair C is $\approx_I$-equivalent (`ST3_pairC`/`pairC_family`). The one-step bound is `ST4_pairC`.
- **Paper-level (mine, unreviewed):** Proposition A, the chain invariance.
- **Prose reading (mine, unreviewed):** the verdicts of §3 and §5, and the `PassiveQuotient` agreement.
- **Replayed control:** K2 (classical) of #1486, as already recorded there. No new computation.
- **Open:**
  - family (ii) and infinite or classical factors in Proposition A;
  - whether $I(D)$ should be multi-time;
  - whether the corpus intends single-time data.
- **Owner decisions:**
  - the interface choice (§2);
  - routing of §5's proposed corrections and of the ch03:84 ledger mirror;
  - any Lean round.
