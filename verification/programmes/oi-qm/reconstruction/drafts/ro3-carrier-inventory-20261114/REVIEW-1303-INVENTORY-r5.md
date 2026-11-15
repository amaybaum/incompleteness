# Independent review: RO-3 inventory r5 (PR #1303), with RESPONSE-r4

**Verdict: ACCEPT WITH CHANGES.** No label in r5 is refuted at its stated scope, and the
seventeen findings of the r4 review are applied, three of them only in part (F8 to F11, F12; see §1).
The new §7 map is accurate row by row, but it is not complete. It misses the characterization
theorem itself (Main:536) and the sentence of Main:60 that makes that theorem's physical reading
conditional on the finite representative. §7.3 misreads Main:716. The D-CQ reading is faithful as
far as it goes but leaves out the exclusion purpose of answer 4's last sentence. The required
changes are H1 to H6. None of them requires new mathematics or a status change.

## Object, base and limits

- **Reviewed.** `RO3-INVENTORY-r5.md` (SHA-256 `dd7bb6e8…d3e`) and `RESPONSE-r4.md` (SHA-256
  `a60f3082…eb03`), against `REVIEW-1303-INVENTORY-r4.md`. The r5 header names the last file
  `REVIEW-r4.md`. Its digest `f06d9f16…4e20` matches the file as delivered.
- **Base.** `main` `7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`. PR head
  `78089e5e7540f116f69933efca898a8b86d5f36d`. `OBL-RO3-2-r2.md` at the head is blob `b1edb95f…`, as
  r5 states. Ledger r8 and r9 on `main` are blobs `d6ceba53…` and `7c69662a…`, as r5 states. The
  diff `dfeec843..7ac74a4b` under the paths r5 names matches r5's Standing.
- **Read first-hand.** These GitHub comments, through the API:
  - #1169 c.6891338304 (D-CQ), c.6876591512 (Gate A answers), c.6893456888 and c.6893687398;
  - #914 c.6893722503, c.6883249235 and c.6883931412;
  - the RO-1 split, c.6883250792.
- **Also read.**
  - Main at the base: every line §7 cites, plus :18, :80, :352–356, :445–467, :502–504, :536–544,
    :626, :646, :696, :716, :733 and :742–758.
  - The cited lines of GR, Substratum, Methodology, Computation and Structure.
  - The Lean statements that r5 §2.5 and §7 cite. Every line number I checked was right, including
    `glob_map_of_glob_eq` at QuasilocalAlgebra.lean:1074.
  - The census entries for families 1, 8, 15, 31, 34, 40, 49, 53, 114 and 120.
  - DEPENDENCY-AUDIT.md:277–292.
- **Searched.** I searched `papers/`, `book/`, `verification/lean*` and the verification records for
  "A1", "total-finiteness", "total finiteness", "finiteness posit", "finite total", "finite
  representative" and "recurrence time".
- **Limits.** Paper-only. Nothing was built or run, and no repository, Issue or PR was written. I
  did not re-review the OBL-RO3-2 proof. The owner accepted it at its scope.

## 1. Whether the seventeen findings are applied (check 1)

| Finding | Applied? | Note |
|---|---|---|
| F1 | yes | 1.7 F (r5:339) names [55] as an imported input. The label definition (r5:148–150) was extended to match. |
| F2 | yes | 2.7 (r5:582–586). |
| F3 | yes | 2.6 (r5:554–558). |
| F4 | yes | 1.1 G-fam (r5:235) matches SM:296 and SM:1602–1606. |
| review §1, 1.4 | yes | r5:295: each direction has its own witness. |
| F5 | yes | §3 (r5:590–605). The quotations match #914 c.6883931412 item 2. |
| F6 | mostly | 1.2 G-fact (r5:254) carries an OBL-class statement without the label (H5). |
| F7 | mostly | See H5: short forms of the label, and unlabelled §3 bullets. |
| F8 | in part | The rows listed for Main:60 are there. The characterization theorem and the C2-necessity theorems are missing (H1, H3). |
| F9 | in part | Rows AM-11 to AM-18 are accurate. GR:58, Comp:100, Meth:156, Meth:339–369, census 15 and 31 (as consumers), census 53, and the MR-1 preregistration are missing (H3). |
| F10 | in part | The scope statement is added. But §7.1 claims a corpus-wide map, and §5 says each hit of "A1" was read; Comp:100 contains "A1" and is absent (H3). |
| F11 | in part | §7.3 is added, but it misreads Main:716 and leaves out Main:60's physical-reading sentence (H1, H2). |
| F12 | in part | D-CQ is located and quoted correctly. The reading of answer 4 is incomplete, and Q13 paraphrases answer 4 inaccurately (H4). |
| F13 | yes | Q2 (r5:646–652). The quotation matches c.6883250792. |
| F14 | yes | The blobs are verified. |
| F15 | yes | Status lines updated. |
| F16, F17 | yes, in the inventory | Written into r5 2.5 (ii-b) and correct against the kernel definitions. `OBL-RO3-2-r2.md`, the cited support, still carries the "not looked up" caveat. Under the r5 authorization that is acceptable. An OBL r3 needs its own authorization. |

## 2. The §7 map (check 2)

**Verified first-hand, accurate at the stated scope:**
- AM-1, AM-2, AM-4, AM-6, AM-8, AM-9, AM-10;
- AM-11, AM-12 (Sub:123, :125, :189, :193, :253–268);
- AM-13, AM-14 (GR:112–114, :132–134), AM-15, AM-16, AM-17, AM-18, AM-19;
- the Lean pointers: `injective_imp_bijective` (CanonicalMeasure.lean:63, `[Fintype S]` at :54),
  `orbit_invariant_unique` (:178), `counting_maximal_entropy` (:227), `permMatrix_mem_unitaryGroup`
  (EquivalenceChain.lean:179) and `isDiag_Phi` (:253, under the section variables at :195).

Main:758's scope does list "finiteness of $S$", and Main:758 (ii) is quoted correctly.

### H1 (required): §7.3 and AM-5 misread Main:716

Main:716 says the theorem "requires Lemma 1, the stochastic-quantum bridge (§3.1 and §3.2; two
routes reach its transition-statistics layer …)". The two routes are §3.1, the Barandes route,
and §3.2, the Stinespring route. Main:352 compares those same two ("The two routes agree on the
configuration-transition probabilities"), and Main:356 opens "Both routes above are constructive".
The §3.4 permutation-unitary representation is a third, "internal" route (Main:352, :354).

r5 says otherwise in two places:
- AM-5 (r5:814) cites Main:716 for a "§3.4 route".
- §7.3 (r5:859–860): "The §3.2 route uses A1 (AM-5); the §3.4 route does not."

The conclusion that some route to the transition statistics avoids A1 survives, on different
support:
- §3.1 needs only finite `C_V` and (T) (Main:208, :354);
- the in-house fixed-basis representation exists for every finite-horizon law (Main:354, :60).

**Change:** cite Main:352–354 and Main:60 for this conclusion, and state that Main:716's two routes
are §3.1 and §3.2.

### H2 (required): §7.3 leaves out a reading that the source supports

Main:60, the sentence r5 relies on, also says: "The physical reading of the characterization
theorem — the identification of nature with a finite reversible substratum — is accordingly
conditional on that representation choice, an empirically motivated reconstruction rather than a
pure derivation; the law-level equivalence of §3.4 itself holds for every finite-horizon law."
DEPENDENCY-AUDIT.md:282 says the same of the equivalence: "existence of finite representatives of
finite visible laws; not a characterization of the actual infinite substrate".

§7.3 offers the owner only two readings of "the main equivalence": the §3.4 equivalence and the
§3.2 route. There is a third, closer to the comment's words: the characterization theorem
(Main:536), and in particular its physical reading. By Main:60's own text that reading is
conditional on A1.

**Change:**
- Quote both halves of Main:60.
- Present the three readings.
- Reword "does not treat the §3.4 equivalence as conditional on A1" (r5:866) so that it covers the
  law-level statement only.
- Add DEPENDENCY-AUDIT.md:282 to 1.6 (r5:324) and to §7.3.

The difference stays a finding for the owner. It is not settled by the inventory.

### H3 (required): A1 consumers that the map does not list

Add these as rows, or as named items in §7.4:

- **(a) The characterization theorem (Main:536).** The statement restricts to "accessible
  timescales $t \ll t_R$ where $t_R$ is the Poincaré recurrence time of any realizing substrate".
  Item (ii) uses "$k\tau_S \ll t_R$" (:540).
  - Related sites: Main:733 (the "bare-recurrence form … at $t_R$"), Main:18 and Main:80 item (2)
    (recurrence-cycle content), and Main:626.
  - **Where A1 enters.** `t_R` is defined through exact recurrence of the realizing substrate.
    Recurrence holds on a finite substrate, which A1 makes nature's substrate. It fails, for
    example, in the OBL class, where `F` has infinite order (support off `main`, PR #1303). The
    physical reading also uses A1 (Main:60).
  - **What survives.** (ii) ⟺ (iii) and (i) under (T), as law-level statements. (iii) builds a
    finite `C_H` for each horizon, and Main:60 and :354 place the readback lemma and the in-house
    representation outside A1.
  - **Status.** The law-level content is established at its scope. The accessible-timescale
    qualifier, read for an infinite substrate, is not stated on `main`. The physical reading is
    conditional[A1].
- **(b) The C2-necessity theorems.** These are Main:453 and :467, with the mechanism at Main:445–449
  and the slow-bath remark at Main:502. Each is stated for "the uniform-prior bijection marginal of
  §3.2's construction", with `π_H` the uniform hidden prior. So they inherit AM-5 (`C_H` under A1,
  Main:266). Theorem 23 consumes the slow-bath form (Sub:193). Add them to AM-5 or give them their
  own row.
- **(c) GR:58, the classical horizon temperature under H-count.** "Restrict the finite total system
  to a conserved energy shell … uniform counting gives …". This uses A1 and the counting measure,
  together with H-count. The finite-reservoir correction `δ_bath ∼ 1/(4s_H)` is a finite-total
  statement. DEPENDENCY-AUDIT row :289, which r5 leaves "not traced", is probably the same item.
- **(d) Comp:100, the super-BQP exclusion.** Hypercomputation "would require either continuum
  precision (violating A1), unbounded coupling (violating A3) …". This is a consumer: without A1 the
  exclusion loses one of its legs.
- **(e) Methodology.**
  - Meth:156 says that "the exact-recurrence step and the eventual-image restriction … consume
    finiteness of the hidden factor". It mirrors AM-1 and AM-3.
  - Meth:339–369: the constructive-OSR claim "within the nearest-neighbor A1–A6 class". It is a
    consumer of the AM-11 kind.
- **(f) Lean, census 15 and 31 (kernel-only).** These are consumers, which r5 does not record:
  - `obsTheory` and the sourcing theorems of SubstratumInterfaceAudit.lean Section E (:765–800), "the
    sourced theory on its configuration space, under the finiteness A1 supplies", with
    `[Fintype 𝒮.ι] [Fintype 𝒮.V]`;
  - `obsTheory_nonnegBounded` (FrozenSourcing.lean:83, "at every substratum satisfying the
    finiteness A1 supplies").

  Both face carrier 3, the operational theory, and so bear on EXACT. r5 cites census 15 only for
  `waveSubstratum_A1`, which is an instance that satisfies A1.
- **(g) Lean, census 53.** `cx3b_complex_not_A1` (A6Instantiation.lean:512) is a kernel negative: the
  complex carrier on which the SM derivation it names is conducted is not an A1 substratum, and the
  docstring adds that "A1 is not weakened". This belongs in §7.2 or AM-16, as an SM derivation
  carried out on an infinite carrier. Census 49 `hexSubstratum_A1` is an instance that satisfies
  A1.
- **(h) Records.** `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md`
  :260, :361 and :372 take "(P-set) … finite under the total-finiteness posit". It is a
  research-only record, so list it as context.
- **(i) Mirrors.** GR:90, a mirror of AM-1, and GR:342, which frames the result with A1–A6 and
  mirrors AM-11.

**Also correct §5 and §7.1.** §5 (r5:747–754) lists "A1" as a search phrase and says each hit was
read. Comp:100 is such a hit and is absent, so either that claim or the map is wrong. §7.1 should
describe the map as bounded by §5's phrases, as §7.4 already does, and not as corpus-wide.

### H6 (minor): AM-3's "what survives" leaves out the second prong

AM-3 records surjectivity as the A1 step. Main:60's injectivity argument has two prongs.
- The record prong is free of A1.
- The hidden-sector prong uses double stochasticity under the uniform prior, or the eventual-image
  restriction. Both are finite constructions.

[IR], checked by hand: the doubling map on the circle with Lebesgue measure preserves the measure,
is onto and is 2-to-1 everywhere. Its eventual image is the whole circle, so no restriction
removes the merge. The infinite substitute is the natural extension, which is a factor relation,
not a restriction, and Main:60 keeps the two apart. AM-3 should therefore record that without A1
the hidden-sector injectivity prong is unsupported, and not only surjectivity. This bears on the
recommendation in §7 below.

## 3. The causal-cone claim (check 3)

The kernel statement, read at the base:
- `iterate_dependsOnlyOn_ball` (RegionTower.lean:283) has signature
  `(G : CouplingGraph φ) (f : (ι → Q) → Q) (A : Finset ι) (hf : DependsOnlyOn f A) (k : ℕ)`. Its
  conclusion is `DependsOnlyOn (fun s => f (φ^[k] s)) (ball G A k)`.
- The section variables (:246) are `{ι Q : Type} [DecidableEq ι]`. They impose no finiteness on `ι`
  or `Q`.
- `CouplingGraph` (:254) is data: `nbhd : ι → Finset ι` and
  `local_dep : ∀ i, DependsOnlyOn (fun s => φ s i) (nbhd i)`.
- `readout_unaffected_outside_ball` (:304) is the same statement applied to two configurations. It
  is census family 8, status current.

r5 AM-7 is correct that the cone is proved for infinite site sets given a `CouplingGraph`, and that
this is a hypothesis there. It is correct that Main:362 derives the graph from single-component
insensitivity only for finite `V`.

### H6′ (minor, part of check 3)

**Finite-neighbourhood dependence is not derived without A1. It is a further hypothesis.**

- [IR] countercontrol, checked by hand. On `(Z/q)^Z` let `T` be the set of `s` with `s_i ≠ s_{i+1}`
  for infinitely many `i`, and set `φ(s) = s + 1_T(s)·(1,1,…)`.
  - Adding a constant does not change membership of `T`. So `φ` is a bijection: a translation on `T`
    and the identity off it.
  - Each output `φ(s)_i` is insensitive to every single component `j ≠ i`.
  - Yet `φ(s)_i` is not a function of any finite set of components.

  So single-component insensitivity together with bijectivity does not give a coupling graph on an
  infinite site set.
- On the classes r5 uses, the hypothesis comes from named posits, not "by definition" (r5:816):
  - posit (xiii) (Main:724: "each $F_i$ reading the current values at finitely many sites and each
    site read by finitely many $F_i$");
  - posit (viii), site factorization;
  - GR:132's "each component's update depends on finitely many components";
  - in the kernel, `ReversibleDynamics` carrying `FiniteRange`, which extends `CouplingGraph`
    (QuasilocalAlgebra.lean:919), with `leapFiniteRange` (SecondOrderDrive.lean:306) for
    `ruleDynamics`.

  I-meas has no such structure, so the cone is unavailable there unless that hypothesis is added.
- **Scope of the kernel statement.** It covers `Q`-valued functions `f : (ι → Q) → Q`. A readout
  into another alphabet needs a one-line paper step through `site_iterate_dependsOnlyOn` (:297).

**Change to AM-7:**
- name posits (xiii) and (viii), or GR:132, as the source of the hypothesis;
- cite `FiniteRange` and `leapFiniteRange`;
- state that the kernel statement is for `Q`-valued functions;
- state that the hypothesis is not derivable from insensitivity on infinite sets.

## 4. The D-CQ reading (check 4)

### H4 (required): the D-CQ reading

**What D-CQ says** (c.6891338304, read first-hand): it "amends the soundness requirement in the
Gate A answers (c.6876591512). Soundness is now an open question, subject to the
agreement-with-data requirement." It also says:
- "C may lie inside Q (soundness), or C may intersect other subsets of OI with different
  properties. An intersection with stronger-than-quantum behaviour in experiments not yet performed
  would be a testable prediction, not a defect."
- In the restated AC-1: "Excluding PR is no longer a goal."

**What answer 4 says** (c.6876591512): "Require quantum behaviour for every physically performable
experiment within C. This includes accessible preparations, interventions, compositions and
complete records under the retained contract. Access closure must prevent a model from qualifying
through selected quantum experiments while also permitting stronger-than-quantum experiments."

**The most faithful reading.** D-CQ amends three things:
- the soundness half of answer 2;
- answer 4's first sentence;
- the exclusion purpose of answer 4's last sentence, which is to bar a model that permits
  stronger-than-quantum experiments. D-CQ states this purpose is no longer a goal.

Two things are left untouched by D-CQ's text:
- answer 4's second sentence, the experiments counted;
- the anti-selection content of access closure, which stays at most as a coverage and
  agreement-with-data condition. That is itself a reading, the #914 c.6893722503 §4 proposal.

#914 c.6893722503 §3 corroborates this. It lists r3's "§7 answers 2 and 4" as still stating
soundness.

**What r5 gets right, and what it misses.** r5's [IR] reading (r5:92–100, Q13) covers the first two
items and correctly leaves answer 3 unamended. It treats the third item as an open question.

**Defects:**
- Q13 (r5:719–720) paraphrases the clause's purpose as "to prevent stronger-than-quantum
  experiments". That misstates it: the clause prevents a model *qualifying through selected quantum
  experiments* while it permits stronger-than-quantum ones.
- Standing (r5:97–98) says that c.6893722503 §4 "makes the same point". It addresses a different
  clause.

**Change:**
- Quote the purpose clause verbatim in Q13.
- Read its exclusion purpose as amended, marked [IR].
- Leave as the owner question only whether the anti-selection part survives as a coverage and
  agreement condition.

## 5. Labels on moved cells (check 5)

### H5 (minor): label coverage

Cells that use the full label: 1.1, 1.2 and 1.3 for I-qloc and I-meas; 2.3 G-fact; 2.5 (i), (ii-a)
and (ii-b); 2.6; Q6; the context paragraph after 1.2; and AM-1, AM-2, AM-4 and AM-8.

Gaps:
- **1.2 G-fact (r5:254).** "OBL class: no nontrivial finite factor exists (2.3)" has no label.
- **Short forms.** §0 (r5:221), 2.3 (r5:446–447) and AM-16 (r5:825) write "(OBL §4.1, support off
  `main`)" and omit "(PR #1303)". Use the defined label.
- **§3's preservation-control bullets (r5:608–613).** They rest on OBL §4 and carry no label, though
  §3's lead sentence says that every consequence below is labelled.
- **§6 (r5:770).** The "Use here" cell should also list 1.2 G-fact, 2.2, 2.6, §3, and AM-1, AM-2,
  AM-4, AM-8 and AM-16.

## 6. Premises, directions and finiteness (check 6)

- **No new premise is adopted.** AM-7's `CouplingGraph` and AM-4's normalized measure are recorded,
  not adopted (r5:877–879).
- **§A.34 is kept.**
  - 1.4 F cites one witness per direction.
  - 1.7 I-qloc states a uniqueness.
  - The AM-3 candidate states "onto up to a null set", not a bijection, and is marked [IR].
  - The 1.6 row "applies … whatever the carrier" is a statement about laws. With H2's audit
    qualifier added, it does not read as a characterization of an infinite substrate.
- **Finiteness.** No passage assumes a finite total substratum except where A1 is named. The F
  cells and AM rows name A1 at each use.

## 7. Recommended first recovery target (check 7; a recommendation only)

**Goal link.** By H1 to H3, A1 does not block the law-level equivalence (Main:60, :354;
DEPENDENCY-AUDIT.md:282). It blocks the physical reading of the characterization theorem, which
Main:60 makes conditional on the bijective representative, and recurrence-scale nontriviality
(Main:354: P-indivisibility's "role is confined to nontriviality at the recurrence scale"). Every
infinite class in r5 §0 already takes bijectivity as a hypothesis (r5:213–215). So the most
upstream A1 use behind the owner's sentence is AM-3.

**Recommended first: AM-3, the measure form of the eventual-image and surjectivity steps.** Two
questions, preregistered separately:

- **Q-A, surjectivity (expected short).**
  - *Setting.* `(X, μ)` is a standard Borel probability space, and `φ` is an injective Borel map
    with `μ ∘ φ⁻¹ = μ`.
  - *Claim.* `X∞ := ⋂_{n≥0} φⁿ(X)` is Borel, `μ(X∞) = 1` and `φ(X∞) = X∞`. So `φ|X∞` is a Borel
    bijection that preserves `μ`.
  - *Proof outline.*
    - The images are Borel by the Lusin–Souslin theorem, an external standard input to be cited.
    - `μ(φⁿX) ≥ μ(φ⁻¹φⁿX) ≥ μ(φⁿ⁻¹X) = 1`.
    - Injectivity gives `φ(⋂Aₙ) = ⋂φ(Aₙ)`.
  - *Scope.* This is the measure analogue of Main:60's `E`.
- **Q-B, the hidden-sector injectivity prong.** Without A1, does any restriction argument remove a
  merge that leaves no statistical trace? The expected candidate for a negative is H6's doubling
  map.

**Why first.**
- It is the most upstream of the A1 uses behind the physical reading.
- It is cheap.
- Either outcome is informative. A negative on Q-B would show that A1 carries injectivity, not only
  surjectivity. That fact is stronger than restating the posit, and so passes the §A.31 test for a
  gem.

**Skepticism, stated in advance.**
- Q-A is textbook measure theory.
- The invariant probability is a replacement premise. Lemma 3's selection stays tied to A1 (AM-4).
  Sub:262 already demands such a measure for any infinite extension.
- Whatever the outcome, it must not be presented as removing the posit.
- It has no Layer-0 standing under §A.29 and moves no correctness.

**Controls, fixed in advance.**
- With `X` finite and counting measure, `X∞ = E`, and the result reproduces Main:60 and
  `injective_imp_bijective`.
- Main:60's three-state example, in which counting measure on `E` is not doubly stochastic, is
  reproduced, so its measure-correspondence caveat stands.
- Every F cell, `S ⟺ D ⟺ Q_fb`, the readback lemma and Theorem 24(iii) are unchanged.
- In the OBL class, `F` is already bijective, so `X∞ = X`.

**Countercontrols, each of which must fail at a named step.**
- `n ↦ n+1` on `N` has no invariant probability, and `X∞ = ∅`. It fails at the normalization step.
- The doubling map, and the one-sided Bernoulli shift, fail at the injectivity hypothesis.
- A non-Borel injection, or a non-standard space, fails at the Lusin–Souslin step.

**Decision rule.**
- **Recovery (Q-A).** A complete paper proof with every hypothesis labelled. AM-3's steps are then
  recorded as conditional[standard Borel space, invariant probability, injectivity].
- **Negative (Q-B).** An explicit map in I-meas that preserves `μ` and has no injective restriction
  to a set of full measure, with its consequence for the visible statistics stated. A1 is then
  recorded as carrying that prong.
- **Anything else.** Open, with the remaining gap stated.
- No outcome is expected in advance.

**Second:** the infinite form of Theorem 24(iii), on the terms of the r4 review §6.

**Not first:**
- the §3.2 route on I-qloc, which needs (ii-c);
- recurrence-scale P-indivisibility on a coupled infinite sector, which has no bounded mechanism
  (OBL 3.3).

The owner chooses. Nothing here chooses a target (#1169 c.6893687398).

## Required changes

- **H1.** In §7.3 and AM-5: correct the Main:716 citation, and support the free-of-A1 route with
  Main:352–354 and Main:60.
- **H2.** In §7.3: quote both halves of Main:60, present three readings, narrow r5:866, and add
  DEPENDENCY-AUDIT.md:282 to 1.6 and §7.3.
- **H3.** Add the characterization theorem row, and add the C2-necessity theorems to AM-5. Add GR:58,
  Comp:100, Meth:156, Meth:339–369, census 15 and 31 as consumers, census 53 to §7.2, the MR-1
  preregistration as a record, and GR:90 and :342 as mirrors. Correct §5's statement of what was
  read, and §7.1's claim that the map is corpus-wide.
- **H4.** Read the exclusion purpose of answer 4's last sentence as amended ([IR]), quote that
  sentence verbatim in Q13, and correct the "same point" sentence at r5:97–98.
- **H5.** Apply the full label at r5:221, :254, :446–447, :608–613 and :825, and extend §6's
  "Use here" cell.
- **H6 / H6′ (minor).** Add the hidden-sector prong to AM-3. In AM-7, source the coupling-graph
  hypothesis to posits (xiii) and (viii) and the kernel's `FiniteRange`, and state the kernel
  statement's `Q`-valued scope.

No finding requires withdrawing a result, and no cell's status changes.
