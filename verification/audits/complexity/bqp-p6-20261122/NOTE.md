# BQP-P6: (ix), (xi) or PG on the prepared class

**Status: WIP / UNVERIFIED.**
- Paper-only research record under #1169 c.7078857457, BQP row. Issue: #1487.
- It walks `PLAN.md`, which was committed first at `8126b3e7`.
- Nothing is run. No manuscript, Lean, registry or rule file is edited, and no premise is adopted.
- It awaits an independent non-author review.

**Inputs.**
- BQP-P5 at `ab67a0fc` (`verification/audits/complexity/bqp-p5-20261122/NOTE.md`): Lemma Γ,
  Proposition AG, E1, Proposition FS, (S-𝒞) and the readings (R1)–(R3) of its §4. Its reviews
  c.7076936181 and c.7076963950 on #1546.
- BQ1, BQ1-D and BQ1-S (#1498 §B3); H1–H5 at the scopes of #1527 §1.1; rounds #1488 and #1514 as
  BQP-P5 cites them.
- Corpus lines are at `ab67a0fc`.
- LIT1: J.-D. Bancal, S. Pironio, A. Acín, Y.-C. Liang, V. Scarani and N. Gisin, "Quantum
  non-locality based on finite-speed causal influences leads to superluminal signalling", Nature
  Physics 8, 867 (2012), arXiv:1110.3795. Read at the abstract and the HTML of v2.

**Labels.**
- [P] is a manuscript statement, [W] a derivation here (unreviewed), [LIT] literature, [CONJ] a
  conjecture, [SA] a source analysis of the corpus's text.
- (N) and (I) are as in `PLAN.md` §2.
- ESTABLISHED, ASSUMED and MISSING are as the owner standard defines them.

Three things are kept apart throughout:
- computational universality;
- efficient classical simulation, the object of BQ1;
- native BQP.

A failure of H5 is none of the three. No imported quantum operation is counted as native.

## 0. Summary

1. **There is no separate prepared-class rule** (§1).
   - Under A-U and A-G, the prepared class is a state class K of the one map Φ, and its graph
     G_φ^K is a subgraph of G_φ.
   - Read literally (R1), ledger item (ix) is a bound on G_φ, and item (xi) is a statement about
     Φ as a map. On that reading neither has a state-class scope to fix.
   - So, under (R1), "(ix) and (xi) on the prepared class" is the same statement as "the Bell
     branch's Φ satisfies (ix) and (xi)". The union clause of (S-𝒞) is then (ix) itself, up to the
     factor 2 between out-degree and symmetrized degree (§1.1).
   - The per-state bounds the corpus states for the branch do not imply (ix). These are the
     "bounded-degree" of Main:418 (a per-preparation bound on G_φ^K), Substratum:131 and SM:110,
     and SM:104's bound on each G_{φ_x}. ESTABLISHED [W; (N)] for the graph inclusions;
     [SA] for what the ledger items bound.
2. **(N) alone does not give (ix), (xi) or PG** (§1.3). E1 and the address-decoding rule of
   BQP-P5 §5 are maps of the kind A-U and A-G describe, and both fail PG. So HOLDS in the sense of
   `PLAN.md` §4 is excluded. ESTABLISHED [W].
3. **The gauge class carries content** (§2).
   - With an unrestricted gauge, (xi) holds for every bijection Φ, so it constrains nothing.
   - The class the corpus states, site-wise bijections (Substratum:98), preserves dependence. So
     does any product of bijections of the factors of (viii), which covers (xii)'s
     internal-index transformations when the link coupling is a factor.
   - Proposition AG extends from (xiii) to every site-factorized map. ESTABLISHED [W].
4. **On a fixed infinite lattice, (ix) follows from (xi)** (§3, Lemma R).
   - On ℤ^d, finite reading sets and (xi) with a site-wise gauge give N_i = i + O with O finite.
     So (ix) holds with K = |O|.
   - (ix) is independent only in family form, as Main:736 itself says. ESTABLISHED [W].
5. **The corpus readings: one is excluded, and the corpus does not decide between the others**
   (§4).
   - (R2) is not the corpus's reading. A4's parenthetical contrasts ℤ^d with "a continuous space"
     and admits "a finite periodic quotient ℤ^d/P", which is language about the site set.
   - (R1) is the literal reading. Main:736 and Substratum:96, 98 state (ix) and (xi) of φ.
   - Neither (R3) nor a per-φ_s reading is excluded. On the per-φ_s reading, the posits bound
     each G_{φ_s} of SM:104's state-dependent branch.
     - SM:104, Substratum:131 and SM:108 state the branch's constraints per state or on the
       reference class.
     - Main:424 is silent on the items other than (vii). That silence does not state that the
       branch keeps them.
     - The wording of A5 (Substratum:100) against that of A3 and A4 (Substratum:96, 98) is the only
       textual evidence for (R1) over (R3), and it is modest.
   - So the corpus does not decide whether the Bell branch's Φ keeps (ix) and (xi). [SA]
6. **Which failure leaves room** (§5).
   - Within site-factorized maps with finite reading sets, superpolynomial |D| needs PG to fail.
   - On a fixed ℤ^d that needs (xi) to fail. In family form it needs (ix) or (xi) to fail.
   - E1-type growth, |D| ≥ 2^T, arises in the (xi)-failure branch on ℤ itself: E1 extends to the
     site set ℤ with one rule.
   - The (ix)-failure branch has a one-step blow-up of the non-adaptive set only.
     ESTABLISHED [W].
7. **LIT1 bears on the fixed-lattice case** (§6).
   - A fixed rule in 𝒞 on ℤ^d with (xiv) meets the hypotheses of LIT1's v-causal models, with the
     update foliation as the privileged frame and v = ℓ sites per update. [W, hypothesis mapping]
   - Corollary VC needs three (I) hypotheses:
     - H-Bell (i) read as reproducing the quantum correlations in the sequential orderings of
       LIT1's four-party configuration;
     - H-Bell (ii) read as four-party operational no-signalling;
     - timing independence of λ's law.
   - Under them, H-Bell (i) and (ii) cannot both hold for such a rule. This is ESTABLISHED as an
     implication [W from LIT], with an explicit wing placement. LIT1's Lemma 1, including its
     proof and the explicit S, is imported [LIT] and was not read.
   - So on a fixed ℤ^d, both an H-Bell branch under that reading and H5 failure need (xi) to fail.

**Outcome: INCONCLUSIVE.** (R2) is excluded. The corpus is shown not to decide between (R1) and
(R3) or a per-φ_s reading. This is the route of `PLAN.md` §4 in which the corpus is shown not to
decide.
- **Conditional result.** Let Φ be a Bell-route dynamics such that:
  - (a) Φ is a map of (viii)'s configuration, on the site set ℤ^d or on each member of a family
    ℤ^d/P;
  - (b) Φ has finite reading sets, by (xiii) or by Main:368's second form;
  - (c) (ix) holds for G_φ as a bound on the union over all states, in family form on quotients.
    On ℤ^d, (c) follows from (b) and (d) by Lemma R;
  - (d) (xi) holds with a factor-wise gauge. The corpus states that gauge class only in
    Substratum:98's context: second-order rules over ℤ_q on a periodic cubic lattice of side at
    least 3. Outside that context the class is MISSING.

  Then Φ ∈ 𝒞′ and |D| ≤ |R₀|·C(T+K, K) (§2.3). Add H1, extended to polynomial-time computability of
  each output component and each gauge map; H2–H4 at #1527's scopes; BQ1-D; polynomial T; and
  |R₀| = poly(n). Then BQP-P5's OBSTRUCTION (I) applies: native hosting of BQP by such runs implies
  BQP ⊆ BPP.
- **Whether OI's Bell route meets (c) and (d)** is not decided by the corpus (§4).
- **Why this is not HOLDS.** (ix) and (xi) are ledger posits (I), and the (N) structure does not
  give them (item 2).
- **Undecided by the corpus.**
  - Whether the Bell branch's Φ keeps (ix) and (xi).
  - Whether H-Bell's "equivalent nonlocal response map" (Main:418, Substratum:131) is a map of
    (viii)'s configuration.
  - The gauge class away from the periodic cubic context in which Substratum:98 states it.
- **Not FAILS.**
  - **Under (R1) [SA].** No rule that satisfies (ix) and (xi) as properties of Φ has a prepared
    configuration violating (S-𝒞′). By Lemma S they hold at every state.
  - **Outside (R1).** FAILS is not reached either, because the corpus does not fix the posit set
    for the branch.
    - Under a per-configuration or per-φ_s reading, the address-decoding rule meets the
      per-state degree bounds and (xi), and fails the union bound (ix).
    - Neither it nor E1 supplies a Bell mechanism. Neither is shown to give H-Bell (i)'s parameter
      dependence together with (ii)'s no-signalling.
    - So neither is a rule meeting every posit the corpus states for the Bell route, in the sense
      of `PLAN.md` §4.

## 1. Node 1: the scope of (ix) and (xi) is the scope of Φ (Q1)

### 1.1 The scope lemma

**Lemma S [W; (N)].**
- **Statement.** Let K be any class of states, the prepared class included. Then G_φ^K ⊆ G_φ.
  A degree bound on G_φ bounds G_φ^K, and the minimal reading set of F_i is contained in i's
  out-neighbourhood in the unsymmetrized G_φ, together with i.
- **Proof.**
  1. Main:368 defines G_φ by dependence "for some state", and G_φ^K by dependence at some state of
     K, with G_φ = G_φ^S. SM:104 restates it: "one graph collecting the dependences at all
     states". So G_φ^K ⊆ G_φ^S = G_φ.
  2. The minimal reading set N_i^min = {j : the ith output depends on the jth input at some
     state}. By definition this is i's out-neighbourhood in G_φ before symmetrization, with i
     added for the second-order form.
  3. In the phase-space form of (xiii), output pair i is (x_i(t), F_i(x(t)) − x_i(t−1)). It
     depends on input pair j ≠ i iff F_i depends on x_j. So item 2 holds there as well. ∎

**What the ledger items bound [SA].**
- (ix) is a bound on G_φ. Main:736: "(x) implies the bound of (ix) for G_φ^ref, and with (vii) for
  G_φ". Substratum:96, A3: "coupled to a bounded number of neighbors in φ's action". Both name
  the whole map, not a state class.
- (xi) is a statement about Φ as a map: "the update commutes with lattice translations up to
  gauge" (Main:736); "φ commutes with lattice translations up to gauge" (Substratum:98).
- This is the literal reading (R1). §4 records that the corpus does not exclude readings on which
  the branch's constraints are per state.
- **Consequence [W], under (R1).**
  - If the Bell branch's Φ satisfies (ix) with bound K on the symmetrized G_φ, then
    |N_i^min| ≤ K + 1 at every site, on the union over all configurations: the out-degree is at
    most K.
  - Conversely, a union out-degree bound K together with an in-degree bound K gives (ix) with
    bound 2K.
  - So the union clause of (S-𝒞) is (ix) as the ledger states it, up to that factor 2.
  - The per-state bounds the corpus states for the branch are of three kinds. Main:418's
    "bounded-degree long edges ... supplied by a Bell preparation" bounds G_φ^K for each
    preparation class K. The "bounded-degree" of Substratum:131 and SM:110 bounds G_φ^{x}. SM:104's
    state-dependent form s(t+1) = φ_{s(t)}(s(t)) bounds each G_{φ_x}.
  - By BQP-P5 §5 (remark), the address-decoding rule has one long edge per configuration and an
    unbounded union. So none of these per-state bounds implies (ix).

### 1.2 Preparations

- Under A-U, a preparation is runs of Φ interleaved with configuration writes (BQP-P5 §1.1, as
  amended at c.7076963950 item 4). Neither changes Φ. So a preparation selects a state class K and
  changes no ledger property of Φ.
- A preparation that changes Φ is an intervention on the rule. It is (I), and outside this round.

### 1.3 (N) alone does not decide

- **Claim [W].** No argument from A-U and A-G alone gives (ix), (xi) or PG on the prepared class.
- **Proof.** E1 (BQP-P5 §5) and the address-decoding rule are single maps of site-factorized
  configurations, with G_φ as Main:368 defines it.
  - E1 has a prepared class on which |D| ≥ 2^T, so PG fails, and it fails (xi).
  - The address-decoding rule fails (ix) in family form.
  - Both are consistent with A-U and A-G, which therefore do not exclude either failure. ∎
- Neither rule carries a Bell mechanism: neither is shown to supply H-Bell (i)'s parameter
  dependence with (ii). HOLDS is still excluded, because `PLAN.md` §4 requires a derivation from
  (N) assumptions alone, and H-Bell (i)–(ii) are not (N). Whether adding H-Bell would force (ix),
  (xi) or PG is not shown here. Corollary VC (§6) bears on it only on a fixed ℤ^d under (xi).
- So HOLDS in `PLAN.md` §4's sense is excluded. Any positive result rests on (I) posits.

## 2. Node 2: the gauge class (hidden assumption in Proposition AG)

### 2.1 An unrestricted gauge makes (xi) vacuous

**Lemma V [W, exact].**
- **Statement.** For any bijection Φ of S and any bijection τ of S, set g = Φ∘τ∘Φ⁻¹∘τ⁻¹. Then
  Φ∘τ = g∘τ∘Φ.
- **Proof.** g∘τ∘Φ = Φ∘τ∘Φ⁻¹∘τ⁻¹∘τ∘Φ = Φ∘τ. ∎
- So "commutes with translations up to gauge" constrains Φ only through the class the gauge g is
  drawn from.

### 2.2 The corpus's class preserves dependence

- **The stated class [P].** Substratum:98 states the gauge for second-order rules over ℤ_q on a
  periodic cubic lattice of side at least 3, acting "by site-wise bijections of each site's
  (previous, current) pair". It states the consequence: "Such a gauge preserves which sites each
  update reads, so a rule that commutes with translations up to gauge reads its sites in a
  translation-invariant pattern."
- **Factor-wise gauges [W].** Let g be a product of bijections of the individual factors of
  (viii)'s configuration space. Then output component i of g∘Ψ is a function of output
  component i of Ψ alone, so g∘Ψ and Ψ have the same dependence sets.
  - (xii)'s transformations (Main:736; Substratum §3.1) act on site-dependent internal indices,
    "with the link coupling transformed alongside". Their parameters are fixed, so each acts as a
    bijection on each site factor and each link factor. When the link coupling is a factor of
    (viii), they are factor-wise.
- **Not covered.** Gauges of bounded range that mix factors. For them, step 1 of Proposition AG
  does not follow as stated, and no bound is derived here. The corpus states no such class.

### 2.3 Proposition AG without (xiii)

**Proposition AG′ [W, from Main:368 [P]].**
- **Hypotheses.** Φ is a map of (viii)'s configuration on ℤ^d/P, or on ℤ^d with finite reading
  sets. (ix) holds for G_φ, and (xi) holds with a factor-wise gauge. Call this class 𝒞′. BQP-P5's
  𝒞 is its subclass of form (xiii).
- **Conclusion.** N_i^min = i + O with |O| ≤ K + 1, and the T-step readout on R₀ depends only on
  the initial components in R₀ + T⊙(O ∪ {0}). So |D| ≤ |R₀|·C(T+K, K), since O ∪ {0} has at most K + 1 elements.
- **Proof.**
  1. By §2.2, N^min_{i+a} = N^min_i + a.
  2. On finite V, Main:368's first form gives the cone B_{G_φ}(R₀, T). On ℤ^d its second form does,
     with the reading sets N_i^min.
  3. The count is BQP-P5's Proposition AG, step 3. ∎
- So OBSTRUCTION (I) applies to 𝒞′ with BQP-P5's excluded-class list. H1 becomes polynomial-time
  computability of each output component and each gauge map.
- **Consequence for the response-map alternative.** The "equivalent nonlocal response map" of
  Main:418 and Substratum:131 escapes 𝒞′ only if it is not a map of (viii)'s configuration, or if
  it fails (ix) or (xi). The corpus does not say which it is. MISSING.

## 3. Node 3: Lemma R, (ix) on a fixed infinite lattice

**Lemma R [W].**
- **Statement.** Let Φ act on (viii)'s configuration over ℤ^d, with finite reading sets (xiii, or
  Main:368's second form) and (xi) with a factor-wise gauge. Let K₀ = |N_0^min \ {0}|. Then:
  - every site has out-degree and in-degree K₀ in the unsymmetrized G_φ;
  - (ix) holds for the symmetrized G_φ with bound 2K₀;
  - Φ ∈ 𝒞′.
- **Proof.** By §2.2, N_i^min = i + N_0^min, and N_0^min is finite by hypothesis. So every site
  reads K₀ sites other than itself. Each site is read by the same number of sites, since
  j ∈ N_i^min iff j − i ∈ N_0^min. The symmetrized degree is at most the sum of the two. ∎

**Scope.**
- On one fixed rule on ℤ^d, (ix) is implied by (xi) and finite reading sets. For complexity, a
  family of inputs of growing size placed on that one lattice is a valid family, and OBSTRUCTION
  (I) then needs (xi) only.
- In family form over quotients ℤ^d/P, (ix) is independent of (xi). The address-decoding rule
  satisfies (xi) on each member, and its union reading set is the whole ring.
- This matches Main:736: "at a single finite lattice the bound holds automatically, so the item has
  content only in family form". Lemma R adds that on the infinite lattice the bound follows from
  (xi).

## 4. Node 4: the corpus readings (Q2)

| Reading | Claim | Verdict | Grounds |
|---|---|---|---|
| (R1) | (ix) and (xi) bind the Bell branch's Φ | The literal reading; not shown to be the reading that governs the branch [SA] | Lemma S; Main:736 and Substratum:96, 98 state the items of φ |
| (R2) | A4's parenthetical, read on G_φ, admits no long edge | Not the corpus's reading [SA] | The parenthetical's site-set language |
| (R3), or per-φ_s | A3–A6 are scoped to the local sector, or bound each G_{φ_s}, so the prepared class is open | Not excluded [SA] | Substratum:100's wording for A5; SM:104; Substratum:131; SM:108; Substratum:145's joint list |

**(R2).**
- Read on G_φ, "the coupling graph is the discrete lattice ℤ^d" makes G_φ the nearest-neighbour
  hypercubic graph at every state.
- The parenthetical contrasts ℤ^d with "a continuous space" and admits "a finite periodic quotient
  ℤ^d/P". That is language about the site set and its translation group, and it is the ground for
  excluding (R2).
- Under (R2), the "bounded-degree Bell-relevant long edges" of Substratum:131 would place the
  branch outside A4 by definition. That is a consequence of (R2), not a contradiction, so it is not
  a separate ground.
- So the corpus does not use (R2), and the parenthetical names the site set.

**(R3).**
- **Substratum:145** lists A3–A6 among the inputs of the Stage-2 derivation. "Identification of
  this local lattice output with the Bell-violating Stage-1 completion additionally assumes
  H-Bell": H-Bell is added to those inputs. The sentence does not say which of them the
  completion keeps.
- **Substratum:191** says the Stage-2 statements "do not compare preparation-indexed Bell edge
  rules ... because the Stage-2 uniqueness argument does not act on that extra structure". That
  limits what the uniqueness comparison determines. It does not limit which posits Φ satisfies.
- **Substratum:133** says H-Bell is "not a consequence of A1–A6". That says H-Bell is not derived
  from them.
- **Substratum:193**, Theorem 23, takes A1–A6 among its hypotheses, together with M1-B, and
  concludes that a single Bell completion "exists conditional on H-Bell".
- **A5 differs in wording.** A3 is stated of "φ's action" and A4 of "the dynamics φ"
  (Substratum:96, 98). A5 is stated of "the selected wave-equation model" (Substratum:100).
  - Under A-U, a Bell branch with preparation-indexed edges lies outside A5 (SM:104; Main:424).
  - Substratum:145 lists A3–A6 together, and the branch already lies outside one of them. So the
    joint list is read as scoped to the Stage-2 derivation, at least for A5.
  - That A3 and A4 carry no such wording is modest evidence that they are not scoped that way. It
    does not show that they bind the branch.
- **Text that scopes the branch's constraints per state or to the reference class.**
  - SM:104 writes the state-dependent branch as s(t+1) = φ_{s(t)}(s(t)), "where each φ_s is a
    bijection but G_{φ_s} varies with s". A3 and A4, read of each φ_s, bound each G_{φ_s}, a
    per-state bound (§1.1).
  - Substratum:131 assigns "the geometric bounded-range graph" to "the vacuum/uniform reference
    class", and to the entangling preparation only "bounded-degree" long edges.
  - SM:108 states constraints (i)–(iii) "in the reference vacuum/uniform state class".
  - None of these states that the composite Φ satisfies A3 or A4, and none states that it does not.

**(R1).**
- By Lemma S, the ledger's (ix) and (xi), read literally of Φ, have no state-class restriction to
  interpret.
- Main:424 states that the branch's update "lies outside ledger item (vii)". It is silent on the
  other items. That silence is not a statement that the branch keeps them.
- Main:736 states that the framework's claims are "conditional on the full list". That makes the
  posits conditions on the framework's claims. It does not bind every branch: Main:424 places the
  branch outside (vii) without contradiction.
- So (R1) is the literal reading, and the corpus does not establish that it governs the branch.
  The direct support of c.7076936181 nit 5 stands: the corpus derives (ix) for the branch's G_φ
  nowhere.

**Result [SA].**
- Under (R1), (S-𝒞), restated as (S-𝒞′) by §2.3, is the content of ledger items (ix) and (xi) for
  the Bell branch's Φ.
- Under (R3) or a per-φ_s reading, the corpus states for the branch only per-state or
  reference-class bounds. These do not imply (S-𝒞′) (§1.1).
- The corpus does not decide which reading governs the branch. MISSING. It derives (S-𝒞′) under
  none of them.

## 5. Node 5: which failure leaves room (Q3)

**Proposition RM [W].** Let Φ be a map of (viii)'s configuration with finite reading sets. If the
T-step dependency set of a poly(n) readout region is superpolynomial in T for some family of
prepared configurations, then PG fails for Γ, and:
- on a fixed ℤ^d, (xi) with a factor-wise gauge fails;
- in family form over ℤ^d/P, (ix) or (xi) fails.

**Proof.** The first clause follows from Lemma Γ (BQP-P5 §2), since D ⊆ N_Γ^T(R₀). The rest is the
contrapositive of Proposition AG′ together with Lemma R. ∎

**The branches.**

| Failure | Site set | Example | Dependency growth |
|---|---|---|---|
| (xi) fails, (ix) holds | ℤ (fixed rule) | E1 on ℤ, below | E1-type: \|D\| ≥ 2^T for every T ≤ h |
| (xi) fails, (ix) holds | family of chains | E1 (BQP-P5 §5) | \|D\| ≥ 2^T |
| (ix) fails, (xi) holds | family of rings | address decoding (BQP-P5 §5, remark) | non-adaptive \|D\| = N at T = 1; adaptive set ⌈log₂ N⌉ + 2 |
| (ix) fails, (xi) holds | ℤ (fixed rule) | none: excluded by Lemma R | — |
| both hold | either | — | \|D\| ≤ \|R₀\|·C(T+K, K) (AG′) |
| not a map of (viii)'s configuration | — | H-Bell's response-map alternative, if it is one | outside Lemma Γ and outside H1 |

**E1 on ℤ [W, from BQP-P5's proof].**
- **The rule.** Take E1's formula on the site set ℤ, with the long reads restricted to i ≥ 1.
  Let σ_i = 1 for i ≥ 1 and σ_i = 0 otherwise. Then
  F_i = (1 − σ_iτ_{i+1})(c_{i−1} + c_{i+1}) + σ_iτ_{i+1}(c_{2i} + c_{2i+1}) and
  τ_i(t+1) = −τ_i(t−1).
  - It is one rule on one infinite lattice, with |N_i| ≤ 5 at every i ∈ ℤ.
  - It is center independent: for i ≥ 1, 2i ≠ i and 2i + 1 ≠ i, and for i ≤ 0 only the chain
    neighbours and τ_{i+1} are read. Without the restriction, F_0 would read c_0 when τ_1 = 1, and
    F_{−1} would read c_{−1}.
  - It is nearest-neighbour on τ ≡ 0, and fails (xi).
- **The prepared configurations.** For each h, set τ_i = 1 exactly for 2 ≤ i ≤ 2^h.
- **The dependence.** The proof of BQP-P5 §5 uses only the reading pattern of the nodes
  1, …, 2^h − 1, which is unchanged. So c_1(T) depends on all 2^T depth-T sites with coefficient 1,
  for T ≤ h, and |D| ≥ 2^T.
- **Edge lengths.** Its edge lengths i → 2i are unbounded, so no finite ℓ bounds its speed, and
  Proposition FS does not apply to it.
- **What it is not.** As in BQP-P5, its readout is a linear form with a unit coefficient. Under the
  uniform prior it is trivially samplable. It is not a native rule, and it is not a native BQP
  route.

**Answer to Q3.**
- Within maps of (viii)'s configuration, room for H5 failure exists only where (xi) fails or, in
  family form, where (ix) fails (Proposition RM). It is exhibited in the (xi)-failure branch by E1,
  and in the (ix)-failure branch by address decoding, in the non-adaptive sense.
- E1-type 2^T growth is exhibited in the (xi)-failure branch, on ℤ and in family form.
- In the (ix)-failure branch only the one-step non-adaptive blow-up is exhibited. Whether it gives
  superpolynomial adaptive dependency growth is not analysed.

## 6. Node 6: LIT1 and the fixed lattice (Q4)

### 6.1 LIT1's hypotheses and result [LIT]

- **v-causal models.** Influences propagate at a finite speed v in a privileged reference frame,
  or a foliation into spacelike hyperplanes. Bell's local causality is applied with c replaced by
  v.
  - With hidden variable λ of law q(λ), and A's measurement before B's: P(ab|xy) =
    Σ_λ q(λ) P(a|x,λ) P(b|y,ax,λ).
  - For events outside each other's v-cones, written A∼B: P(ab|xy) = Σ_λ q(λ) P(a|x,λ) P(b|y,λ).
    These correlations are local.
- **Free choice.** Settings are free variables, uncorrelated with the outcomes, the other settings
  and λ.
- **Lemma 1.** Four parties A, B, C, D, with binary inputs and outputs. If the BC|AD correlations
  are local and the four-party law is no-signalling, a Bell expression S satisfies S ≤ 7. Quantum
  measurements reach S ≃ 7.2, and S involves only the ABD and ACD marginals.
- **The result.** A v-causal model that reproduces the quantum correlations "when the different
  systems are each within the range of causal influences of previously measured systems" leads to
  superluminal signalling, for any finite v.
  - The orderings used are A < D < B < C and A < D < C < B, in which influence can reach each
    party from the earlier ones.
  - Reproducing them fixes the ABD and ACD marginals, which no-signalling carries over to the
    ordering A < D < (B∼C). There S ≤ 7, which contradicts those marginals. So no-signalling fails
    in some configuration.
- Measurement in a configuration with A∼B is not required to reproduce quantum predictions.

### 6.2 The mapping [W]

**Proposition VC [W].**
- **Hypotheses.** A fixed rule in 𝒞′ on ℤ^d, ℓ = max_{o∈O} ‖o‖₁, and (xiv).
- **Statement.** The rule is a v-causal model in LIT1's sense, with:
  - the update foliation as the privileged frame;
  - v = ℓ sites per update;
  - λ the configuration outside the setting regions;
  - (xiv) as free choice.
- **Proof.**
  1. By Proposition AG′ and Proposition FS (BQP-P5 §6), a readout taken k updates after a setting
     intervention depends on that setting only if the readout region lies within ℓ₁-distance ℓk of
     the setting region.
  2. Each outcome is a deterministic function of λ and of the settings within its cone. That is
     LIT1's factorized form, with P(b|y,ax,λ) where A's setting is in B's cone and P(b|y,λ) where
     it is not. Deterministic responses are a special case of LIT1's λ formalism.
  3. (xiv) gives p(λ | settings) = p(λ), which is LIT1's free choice. ∎

**Corollary VC [W from LIT].**
- **Hypotheses.**
  - A fixed rule in 𝒞′ on ℤ^d, with (xiv).
  - **(TI) timing independence (I).** λ, the configuration at a reference time before every
    setting, has a law that does not depend on which of the three timing configurations below is
    run. (xiv) covers the settings only.
  - **H-Bell (i), sequential reading (I).** The rule reproduces the quantum correlations of
    LIT1's four-party configuration in the orderings A < D < B < C and A < D < C < B.
  - **H-Bell (ii), four-party reading (I).** The four-party outcome law is operationally
    no-signalling, which is LIT1 Lemma 1's hypothesis (b).
- **Statement.** These hypotheses are jointly inconsistent. So H-Bell (i) and (ii)
  (Substratum:133), read this way, do not both hold for that rule.
- **The wing placement.**
  - Work along one lattice axis e. Each wing W has a setting region and a readout region of
    ℓ₁-radius at most r about a point p_W. The setting is applied at time t_W, and the readout is
    taken at t_W + 1.
  - By Proposition FS, wing W′'s readout can depend on W's setting only if
    ‖p_W′ − p_W‖₁ ≤ ℓ(t_W′ + 1 − t_W) + 2r. Call W′ *inside W's cone* when this holds, and
    *outside* when it fails.
  - A and D are early, near the midpoint: p_A = 0, t_A = 0; p_D = δe with δ > 2r, and t_D > δ/ℓ.
    Then D is inside A's cone.
  - B and C are placed symmetrically: p_B = Xe and p_C = −Xe, with
    X > max(δ + 2r, (ℓ + 2r)/2). Fix a time t₀ with ℓ(t₀ − t_D) > X + δ + 2r. Then B and C are
    inside the cones of A and D whenever t_B, t_C ≥ t₀.
  - **A < D < (B∼C).** Set t_B = t_C = t₀. Then ‖p_B − p_C‖₁ = 2X > ℓ + 2r, so each of B and C is
    outside the other's cone.
  - **A < D < B < C.** Set t_B = t₀ and t_C = t₀ + Δ, with Δ ≥ 1 and ℓΔ ≥ 2X. Then C is inside
    B's cone. C's setting comes after the readouts of A, B and D, so they are outside its cone.
  - **A < D < C < B.** The same, with B and C exchanged.
- **Proof.**
  1. By Proposition VC, in each timing configuration the rule is a v-causal model with the cone
     relations above.
  2. By (TI), the three configurations share one law of λ.
  3. In the third configuration, B and C are outside each other's cones. So, for each value of
     A's and D's inputs and outputs, the BC correlations take LIT1's local form, with
     (λ, a, x, d, w) as the shared variable. This is Lemma 1's hypothesis (a) as the literature
     reading of this round reports it. Its exact form is in LIT1's appendix, which is [LIT] and was
     not read.
  4. B is set and read at the same times in the first and third configurations. Each outcome is a
     deterministic function of λ and of the settings in its cone, and by (TI) λ has one law. So the
     ABD marginal of the third configuration equals that of the first. Likewise, the ACD marginal
     of the third configuration equals that of the second.
  5. Under the sequential reading of (i), these marginals are the quantum ones, and they fix
     S ≃ 7.2. Under (ii), Lemma 1's hypothesis (b) holds in the third configuration, so Lemma 1
     gives S ≤ 7 there. ∎
- **Labels.**
  - The three readings, (TI), (i) and (ii), are (I). Substratum:133 states (i) as "supply the
    required ontic parameter dependence", without naming configurations.
  - LIT1's Lemma 1, its proof and the explicit Bell expression S are imported [LIT] and were not
    read. They are in LIT1's appendices, and this round read the abstract and the HTML body
    only.
  - The placement is checked against Proposition FS's cone condition only.

### 6.3 Consequence

- **On a fixed ℤ^d [W].** By Lemma R, if the Bell branch's Φ has finite reading sets and satisfies
  (xi) with a factor-wise gauge, it is in 𝒞′.
  So OBSTRUCTION (I) applies, and by Corollary VC, under (TI) and the readings of H-Bell (i) and
  (ii) stated there, H-Bell (i) and (ii) fail together. Both a working H-Bell branch under that reading and H5 failure
  require (xi) to fail.
- **In family form.** The offsets O may depend on the quotient, so no fixed v exists, and
  Corollary VC does not follow. OBSTRUCTION (I) still applies under (ix) and (xi).
- **Relation to BQP-P5 §6.** For a fixed rule in 𝒞′ on ℤ^d and the sequential reading of
  H-Bell (i), Corollary VC establishes the implication that BQP-P5 §6 records as [CONJ]. Its
  family-form part is not addressed here.

## 7. Fixed point and stop

- **Classification.** Nodes 1, 2, 3, 5 and 6 are NEW. Node 4 is NEW for the site-set exclusion
  of (R2) and for showing that the corpus does not decide between (R1) and (R3) or a per-φ_s
  reading. It is ELABORATING otherwise.
- **Productivity test.** Node 1 meets P1, node 4 P2, node 5 P3, node 2 P4 and node 6 P5.
- **Why the round stops.** Q1–Q4 are answered under `PLAN.md` §4. Each further step would need
  something excluded here:
  - a choice of the Bell mechanism, which is a physical rule;
  - a decision on which reading governs the branch, that is, whether ledger posits (ix) and (xi)
    are kept for it. That is a premise decision;
  - an analysis of adaptive dependency sets, or of bounded-range gauges.

## 8. Established / Assumed / Missing

**ESTABLISHED** [W, unreviewed]:
- Lemma S: the prepared class has no rule apart from Φ, and, under (R1), (ix) is the union bound
  up to a factor 2 (§1.1);
- (N) alone does not give (ix), (xi) or PG (§1.3), so the outcome is not HOLDS;
- Lemma V: an unrestricted gauge makes (xi) vacuous (§2.1);
- factor-wise gauges preserve dependence (§2.2), and Proposition AG′ with OBSTRUCTION (I) holds for
  𝒞′ (§2.3);
- Lemma R: on a fixed ℤ^d, (xi) with finite reading sets implies (ix), with bound 2K₀ (§3);
- Proposition RM and the failure table, including E1 on ℤ, with long reads restricted to i ≥ 1,
  with |D| ≥ 2^T (§5);
- Proposition VC, and Corollary VC as an implication from LIT1 under (TI) and the stated readings
  of H-Bell (i) and (ii), with an explicit wing placement (§6);
- [SA]: (R2) is excluded; (R1) is the literal reading; neither (R3) nor a per-φ_s reading is
  excluded; the corpus does not decide (§4);
- not FAILS under (R1), and FAILS not reached outside it (§0, Outcome).

**ASSUMED:**
- A-U and A-G (N);
- (viii), A-13 or Main:368's finite-reading-set form, A-9, A-11 with the gauge class of
  Substratum:98, each (I);
- H1–H4 at #1527's scopes, BQ1, BQ1-D, BQ1-S and polynomial T (I), as in BQP-P5;
- (xiv) (I), for §6;
- the sequential reading of H-Bell (i), the four-party no-signalling reading of H-Bell (ii) and
  timing independence (TI), each (I), for Corollary VC;
- LIT1's Lemma 1, its proof and the explicit S, and LIT1's main result [LIT], not read in their
  appendix form;
- for OBSTRUCTION (I) on 𝒞′: H1 extended to polynomial-time gauge maps, and |R₀| = poly(n).

**MISSING:**
- whether H-Bell's mechanism, including the "equivalent nonlocal response map", is a map of (viii)'s
  configuration (§2.3);
- which reading governs the Bell branch, and so whether its Φ keeps ledger posits (ix) and (xi).
  The literal reading (R1) states them of Φ. Neither (R3) nor a per-φ_s reading is excluded. The
  corpus derives them under none of these (§4);
- the gauge class outside the periodic cubic second-order context of Substratum:98, and bounded-range
  gauges (§2.2);
- adaptive dependency growth in the (ix)-failure branch (§5);
- the family-form compatibility of 𝒞′ with H-Bell (§6.3).

## 9. What this record does not claim

- It does not claim that OI's Bell route is in 𝒞′, or outside it. It claims three things: the
  defining items, read literally, are stated of Φ; other readings are not excluded; and the items
  are not derived.
- It does not claim that efficient native QC is impossible, possible, or universal.
- It does not claim that E1, or any rule here, is OI's rule or a candidate for it.
- It does not claim that H5 failure implies hardness of classical simulation.
- It does not claim that H-Bell fails. Corollary VC is conditional on a fixed rule in 𝒞′ on ℤ^d,
  on (TI), and on the stated readings of H-Bell (i) and (ii).
- It adopts no premise and proposes no manuscript change.
