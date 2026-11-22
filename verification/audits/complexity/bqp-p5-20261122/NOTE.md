# BQP-P5: edge generation on the Bell route

**Status: WIP / UNVERIFIED.**
- Paper-only research record under #1169 c.7076731666, item 2. Issue: #1487.
- It walks `PLAN.md`, which was committed first at `7abad0ad`.
- Nothing is run. No manuscript, Lean, registry or rule file is edited, and no premise is adopted.
- It awaits an independent non-author review.

**Inputs.**
- Round 4, #1527 at `d02be567`: DQ-L, Lemma LE, the BQ2 plan, (M1)–(M4), and its reviews
  c.7067386218 and c.7067413567.
- BQ1 and BQ1-D, #1498 §B3 (reviewed).
- Corpus lines are at `d02be567`.

**Labels.**
- [P] is a manuscript statement and [W] is a derivation here, unreviewed. [LIT] is literature and
  [CONJ] is a conjecture.
- (N) and (I) are as in `PLAN.md` §2.
- ESTABLISHED, ASSUMED and MISSING are as the owner standard defines them.

Three things are kept apart throughout:
- computational universality;
- efficient classical simulation, the object of BQ1;
- native BQP.

A failure of H5 is none of the three.

## 0. Summary

1. **The form of the rule is derived; its content is not** (§1).
   - Under A-U, a preparation is a stretch of the one update, and its only trace is the
     configuration. So preparation-indexed adjacency is configuration-indexed adjacency.
   - Under A-13 the reading sets N_i are fixed, so every edge any run can activate is an edge of a
     fixed graph Γ. Natively, edge generation is *activation within Γ*: an edge (i, j) is active
     at x iff F_i is sensitive to x_j at x.
   - No dynamics creates an edge outside Γ. ESTABLISHED [W; (N) for the form, (I) through A-13].
   - The content is not derivable. The native update R_q is nearest-neighbour, so its Γ has no
     long edge and the Bell–lattice Corollary (Main:420) makes it Bell-local. The rule on prepared
     configurations is specified nowhere in the corpus. MISSING.
2. **Bound on L(n) from the rule alone** (§2).
   - By Main's cone lemma, D ⊆ N_Γ^T(R₀), and L(n) ≤ K·|N_Γ^T(R₀)|.
   - Ambient edges and generated edges are all inside Γ, so the decisive quantity is the growth of
     Γ-balls. That is a property of the rule, not of the run or of the environment's history.
   - Round 4's (M1) has no content under A-13 beyond activation, and (M2) follows from polynomial
     growth of Γ (PG). PG is sufficient, not necessary. ESTABLISHED [W].
3. **Scoped OBSTRUCTION (I)** (§3).
   - Let 𝒞 be the class of rules of form (xiii) whose reading sets have a uniform bound K (ix) and
     that commute with translations up to a site-local gauge (xi).
   - For every rule in 𝒞: |D| ≤ |R₀|·C(T+K, K) ≤ |R₀|(T+1)^K, whatever the lengths of the long
     edges.
   - With H1–H4 and BQ1-D, native hosting of BQP by poly(n)-step runs of a rule in 𝒞 implies
     BQP ⊆ BPP. ESTABLISHED as an implication [W].
4. **Is OI's Bell route in 𝒞?** (§4).
   - The corpus does not say. Main's ledger states (ix) and (xi) without restriction and places
     the Bell branch outside (vii) only (Main:424).
   - Substratum applies A3–A6 to the local lattice output and assumes H-Bell separately for the
     Bell completion (Substratum:145, Substratum:191).
   - A4's parenthetical "(the coupling graph is the discrete lattice ℤ^d)" (Substratum:98), read
     on G_φ, admits no long edge at all.
   - MISSING: the scope of (ix), as a bound on the union of reading sets, and of (xi) on the
     prepared class, or PG directly.
5. **Counterexample outside 𝒞** (§5).
   - The rule E1 satisfies (xiii), (ix), the SM §3.1 constraints (i)–(iii) on the reference class,
     center independence, and round 4's (M1), (M3) and (M4). Its long edges are fixed at
     preparation, and no edge is generated.
   - It fails (xi), and its readout depends on exactly 2^T initial sites, so H5 fails.
     ESTABLISHED [W, exact algebra].
   - Its output law is nevertheless trivially samplable. Failure of H5 is not hardness.
6. **The price of 𝒞 on ℤ^d** (§6).
   - For a fixed rule in 𝒞 on ℤ^d, every G_φ edge has length at most ℓ. Main's Bell-ceiling
     theorem then gives |S_CHSH| ≤ 2 for every wing pair beyond the cone of ℓ sites per update.
     ESTABLISHED [W] from Main [P].
   - So the posits that give OBSTRUCTION make option (a) a finite-speed influence in the lattice
     frame.
   - Bancal et al. [LIT1] show that finite-speed influence models reproducing quantum correlations
     predict signalling. Whether OI's construction falls in their model class is [CONJ] here, not
     checked.

**Outcome.**
- For OI's Bell route as the corpus states it: **INCONCLUSIVE**. The missing premise is the scope
  of (ix) and (xi), or PG, on the prepared class (§4).
- Scoped **OBSTRUCTION (I)** via BQ1-D: ESTABLISHED for the class 𝒞, and for the wider class
  𝒞_PG (§3).
- No ESCAPE is derived. E1 shows that the corpus's stated constraints do not exclude H5 failure. E1
  is not a native rule, and it is not a native BQP route.

## 1. Node 1: the form of the edge-generation rule (Q-A)

### 1.1 Preparation-indexed is configuration-indexed

- **A-U.** The dynamics is one fixed map Φ on configurations (SM:104: s(t+1) = φ_{s(t)}(s(t)) is
  one map of s). Setting generators are part of the system (Main:410–416), and so are preparation
  devices, since nothing in the corpus makes them external.
- So a "Bell preparation" (Main:418) or an "entangling preparation" (Substratum:131) is a
  stretch of runs of Φ. After it, the only datum that differs from an unprepared run is the
  configuration: the pair (x(t−1), x(t)) in the second-order form.
- Hence the long edges at time t are a function of the configuration alone. In Main's per-class
  notation (Main:368), they are dependences of Φ that occur at the current configuration.
- [W; (N)]. The only alternative is a preparation that changes Φ from outside. That is an
  intervention on the rule, not a native process, and it is (I).

### 1.2 Activation within a fixed graph

- Under A-13, F_i is a function of the current values on a finite reading set N_i. The update at
  i also reads x_i(t−1). Write N_i⁺ = N_i ∪ {i}.
- **The fixed graph.** Let Γ be the directed graph with an edge i → j iff j ∈ N_i.
- **Activation.** An edge i → j is *active at x* iff some x′ that differs from x only at site j
  has F_i(x′) ≠ F_i(x). This is the per-state dependence of Main:368.
- **Claim [W].**
  - The set of edges active at x is a subset of Γ, for every x.
  - Over all x, it is the edge set of the directed G_φ restricted to the current-value
    dependences.
  - No configuration, and hence no run and no preparation, activates an edge outside Γ.
- **Proof.** If j ∉ N_i, F_i does not depend on x_j, so the edge is never active. ∎
- **The derived rule.** The edge-generation rule *is* the activation map x ↦ {i → j active at x}.
  It is fixed by F, and F determines it. Natively there is no separate generation rule to supply,
  and dynamics that "re-attaches" an edge activates a different edge of Γ.
  ESTABLISHED [W; (N) for §1.1, (I) through A-13].

### 1.3 The content is not derivable from the native update

- **The native update.** The native update is R_q (SM:294–298; round 4 §1.1), with nearest-neighbour reading. Its
  Γ is the nearest-neighbour graph. The Bell–lattice Corollary (Main:420) makes the native
  update Bell-local for wings outside the graph cone.
- **What the corpus says about the prepared class.** It constrains the rule only on the
  reference class, by SM §3.1 (i)–(iii) (SM:108). For prepared configurations it says only
  "bounded-degree, preparation-indexed edges" (SM:110), or "bounded-degree long edges or an
  equivalent nonlocal response map" (Main:418; Substratum:131).
- **Conclusion.** No F on the prepared class follows from these. MISSING: the rule on the prepared
  class.
- **Scope of the "equivalent nonlocal response map".**
  - If it obeys (xiii), it has finite reading sets and falls under §1.2.
  - If it does not, it is outside BQ1's H1 as stated. Round 4 §2.3, item 3 records this, and
    nothing here changes it.

## 2. Node 2: the dependency set and L(n) from Γ alone (Q-B, general)

**Lemma Γ [W, from Main:368 [P]].**
- **Statement.** Let N(S) = ⋃_{i∈S} N_i⁺ and N^T(S) its T-fold iterate. The readout x_{R₀}(T) is a
  function of (x(−1), x(0)) restricted to N^T(R₀). Every long edge used by any T-step run from any
  configuration has its tail in N^{T−1}(R₀). So:
  - |D| ≤ |N^T(R₀)|;
  - L ≤ K·|N^{T−1}(R₀)|, where K bounds |N_i|.
- **Proof.** This is Main's finite-reading-set induction (Main:368, second form), with reading sets
  N_i⁺. By §1.2, every active edge is an edge of Γ. ∎

**Consequences for round 4's premise list [W].**
- **(M1), generation.** Under A-13 no generation outside Γ exists. Generation is activation inside
  Γ, and Lemma Γ holds for every activation pattern. So (M1) adds nothing once Γ's growth is
  bounded.
- **(M2), isolation.** (M2) is implied by **(PG)**: |N^T(R)| ≤ p(|R|, T) for a polynomial p. PG is
  a property of the rule alone, and ambient edges from the environment's history are inside Γ.
  - The implication runs one way only. A run whose environment activates few edges can satisfy
    (M2) while Γ fails PG. Lemma LE of round 4 covers that case, at the price of a run-dependent L.
- **(M3) and (M4) with a finite alphabet imply (ix) for Γ (Lemma U).**
  - Suppose F_i depends on x only through x on B_ref(i, r_s) and on at most Δ further sites
    A_i(x|B_ref(i, r_s)), chosen by that pattern.
  - Then N_i ⊆ B_ref(i, r_s) ∪ ⋃_p A_i(p), so |N_i| ≤ |B_ref(r_s)| + Δ·q^{|B_ref(r_s)|}.
  - **Proof.** There are q^{|B_ref(r_s)|} patterns. ∎
  - They do not imply PG. E1 (§5) satisfies (M3) and (M4) and fails PG.
- **Round 4's "OBSTRUCTION needs all four"** (round 4 §2.3) holds for BQ2's route through Lemma LE.
  It does not hold for OBSTRUCTION in general: §3 obtains OBSTRUCTION without (M1), without (M3)
  and without a run-level (M2).
  - This is a new result, not a defect in the nit commit `d02be567`, which states the list as the
    delta review asked. Round 4's record is not edited.

## 3. Node 3: the scoped OBSTRUCTION (Q-B in the class 𝒞)

**The class 𝒞.** Rules Φ such that:
- Φ is of form (xiii) on ℤ^d, or on a periodic quotient ℤ^d/P;
- (ix): |N_i| ≤ K for all i, uniformly across the family;
- (xi), first clause: Φ∘τ_a = g_a∘τ_a∘Φ for every lattice translation τ_a, with g_a acting site by
  site, by a bijection of each site's values. This is the site-local internal-index form of the
  gauge (A6).

**Proposition AG [W].** For Φ ∈ 𝒞:
- N_i = i + O for one offset set O with |O| ≤ K;
- N^T(R₀) = R₀ + T⊙(O ∪ {0}), where T⊙ denotes the T-fold sumset;
- |D| ≤ |R₀|·C(T+K, K) ≤ |R₀|(T+1)^K;
- L ≤ K·|R₀|(T+1)^K.

These bounds hold whatever the lengths of the offsets in O, and whatever O is for each member of a
family of quotients.

**Proof.**
1. *Translation invariance of the reading sets.* Site-local relabellings preserve the dependence
   of one output component on one input component. So output i+a depends on input j+a iff output
   i depends on input j, hence N_{i+a} = N_i + a, and N_i = i + O with O = N_0 − 0.
2. *The cone.* By induction, N^T(R₀) = R₀ + {o₁ + … + o_T : o_k ∈ O ∪ {0}}.
3. *Counting.* The group is abelian, so a T-term sum depends only on the multiset of its terms.
   There are C(T+K, K) multisets of size T drawn from K+1 elements, and
   C(T+K, K) ≤ (T+1)^K.
4. *The edge bound.* L follows from Lemma Γ. ∎

**OBSTRUCTION (I) [W].**
- *Argument.* Add H1–H4 at the scopes of round 4 §1.1, and T = poly(n). By Proposition AG, H5
  holds with |D| = poly(n), and BQ1 and BQ1-D (#1498) apply.
- *Conclusion.* If a family of poly(n)-step runs of one rule in 𝒞 decides every language in BQP
  with bounded error, then BQP ⊆ BPP. Under BQ1-S, IQP-type sampling collapses PH in the same way.
- *Layer.* Ontic and operational, not Born-form.

**The exact excluded class.**
- *Excluded:* efficient native hosting of BQP, in the sense of BQ1-D, by any rule satisfying all of
  the following:
  - (xiii), (ix) and (xi) as above;
  - H1, with each F_i, and each gauge map g_a used by the simulator, computable in polynomial time;
  - H2, a prior on D that does not depend on the input and is samplable in poly(|D|) time;
  - H3, (xiv) for inputs;
  - H4, polynomial-time readout and charged conditioning;
  - polynomial T.
- The same holds for the wider class 𝒞_PG, in which (ix) and (xi) are replaced by PG.
- *Not excluded:*
  - rules outside 𝒞_PG;
  - superpolynomial T;
  - priors failing H2;
  - conditioning beyond H4;
  - failure of (xiv);
  - response maps outside (xiii).
- It does not exclude computational universality, which concerns what is hosted, not at what
  cost. It does not assert that any rule in 𝒞 hosts anything.

## 4. Node 4: does the corpus place the Bell route in 𝒞? (Q-C)

| Source | What it states | Reading for the prepared class |
|---|---|---|
| Main:736, ledger (ix), (xi) | (ix): one degree bound across the family. (xi): commutes with translations up to gauge. No restriction to a state class | (R1) Read literally, both apply, so the Bell route is in 𝒞 and OBSTRUCTION (I) applies |
| Main:424 | the Bell branch's update "lies outside ledger item (vii)" | names (vii) only, and is silent on (ix) and (xi) |
| Substratum:98, A4 | "commutes with lattice translations up to gauge (the coupling graph is the discrete lattice ℤ^d …)" | (R2) If the parenthetical is read on G_φ, no long edge is admitted, and the Bell branch lies outside A4 by definition |
| Substratum:145, 191 | A3–A6 enter the local lattice output. Its identification with the Bell completion "additionally assumes H-Bell", and the gauge statement does "not compare preparation-indexed Bell edges" | (R3) A3 and A4 are scoped to the local sector, and the prepared class is open |
| Main:418, Substratum:131, SM:110 | "bounded-degree" long edges | a bound per preparation or per configuration. By Lemma U it implies (ix) for Γ only together with (M3) and a finite alphabet |

- **Result.** The three readings disagree, and none is stated for the prepared class.
- **MISSING.** The single premise that decides between OBSTRUCTION and no OBSTRUCTION through this
  route is the following.
  - **(S-𝒞)** The rule on the prepared class satisfies (ix), as a uniform bound on the reading sets
    N_i (the union over configurations, not a bound per configuration), and (xi) with a
    site-local gauge.
  - Or, more weakly, **(PG)** holds for its Γ.
- This needs a specification of H-Bell's mechanism, not mathematics: §5 shows the stated
  constraints leave it open.
- The (R1)/(R2) tension is a scope ambiguity in the corpus. It is recorded here only, and no
  manuscript change is proposed or made.

## 5. Node 5: a counterexample outside 𝒞 (P3)

**Rule E1 (a mathematical counterexample, not a proposed rule).**
- **Sites and values.** Sites i ∈ {1, …, N}, with N = 2^{h+1} − 1. Each site carries values in
  ℤ/q × ℤ/2: a wave value c_i and a tag τ_i. Values outside the range are set to 0.
- **Form (xiii).** One step is
  - c_i(t+1) = F_i(x(t)) − c_i(t−1), with
    F_i = (1 − τ_{i+1})(c_{i−1} + c_{i+1}) + τ_{i+1}(c_{2i} + c_{2i+1});
  - τ_i(t+1) = −τ_i(t−1). With τ(−1) = τ(0) the tag is constant.
- **Reference class (τ ≡ 0).** The rule is the nearest-neighbour chain wave rule.
- **Prepared class.** τ_i = 1 exactly for 2 ≤ i ≤ 2^h. Then every internal node i ≤ 2^h − 1 reads
  its two children 2i and 2i+1, and every leaf reads its chain neighbours. The prepared long
  edges i → 2i, 2i+1 are fixed by the tags, and no edge is ever generated.

**Properties [W, by inspection].**
- **Bijective.** It is a second-order form (SM:106).
- **Center independent.** F_i reads τ_{i+1}, c_{i±1}, c_{2i} and c_{2i+1}, and never site i's
  present value.
- **SM §3.1 (i)–(iii).** They hold on the reference class: range 1, center independence, and
  translation invariance of the chain's interior.
- **(ix).** It holds with K ≤ 5.
- **Round 4's premises.** (M3) holds with r_s = 1, (M4) with Δ = 2, and (M1) as no generation.
- **(xi).** It fails: the long partners are addresses specific to each site, with lengths up to
  N/2.

**Claim [W, exact algebra].** On the prepared class, with T ≤ h:
c_1(T) = Σ_{depth(j)=T} c_j(0) + (a linear form in the c_k(0) and c_k(−1) with depth(k) < T),
with every displayed coefficient equal to 1. So c_1(T) depends on all 2^T sites at depth T, and
|D| ≥ 2^T. With T = h = n, H5 fails.

**Proof.**
1. *Linear recursion.* With τ fixed, c(t+1) = A c(t) − c(t−1), where A is the fixed reading
   matrix. So c(T) = U_T(A)c(0) − U_{T−1}(A)c(−1), with U_0 = I, U_1 = A and
   U_{k+1} = A U_k − U_{k−1}. Each U_k is monic of degree k in A.
2. *Walks.* From node 1, every node at depth < h reads only its children. So a walk of length m ≤ T
   from node 1 in the reading graph ends at depth exactly m, and reaches each node at depth m by
   the unique tree path.
3. *Coefficients.* Hence (A^m)_{1j} = 0 unless depth(j) = m, and it is 1 there. For depth(j) = T,
   the coefficient of c_j(0) is the leading term (A^T)_{1j} = 1, and the coefficient of c_j(−1),
   which comes from U_{T−1}, is 0. ∎

**What E1 shows, and what it does not.**
- **It shows** that the corpus's stated constraints fix neither PG nor (S-𝒞). Bounded degree,
  local selection, preparation-fixed edges and the reference-class constraints all hold while H5
  fails. The premise doing the work is (xi), or PG, not generation.
- **It does not show** that the output is hard to sample. c_1(T) is a linear form over ℤ/q with a
  unit coefficient, so under the uniform prior it is uniform and trivially samplable. Failure of
  H5 is neither inefficiency of classical simulation nor native BQP.
- **It is not native.** E1 is not derived from the native update and is not proposed. It is a
  counterexample to "stated constraints ⇒ PG".

**A second route: failure of (ix) [W, remark].**
- **The rule.** On a ring of N sites, let F_0 read c at the address decoded from the tags on a
  register of ⌈log₂ N⌉ adjacent sites.
- **Properties.**
  - It is translation covariant after extension to every site.
  - Each configuration activates one long edge per site.
  - The union N_0 is the whole ring, so (ix) fails in family form, and so does (M3), since the
    register grows.
  - H5 fails at T = 1.
- **Scope.** The adaptive set of sites actually read at T = 1 has ⌈log₂ N⌉ + 2 elements. This
  route is not analysed further.

## 6. Node 6: the price of 𝒞 for option (a) on ℤ^d

**Proposition FS [W, from Main's Bell-ceiling theorem [P], Main:410–420].**
- **Hypotheses.**
  - A fixed rule in 𝒞 on ℤ^d. Let ℓ = max_{o∈O} ‖o‖₁, which is finite since O is a fixed finite
    set.
  - The Corollary's remaining hypotheses: setting interventions applied at one step to disjoint
    wing regions, each reading and writing only its own; finite setting and readout regions; and
    (xiv).
- **Conclusion.** |S_CHSH| ≤ 2 for every wing pair whose readout region lies at ℓ₁-distance > ℓk
  from the other wing's setting region, where k is the number of updates from setting to readout.
- **Proof.**
  1. Every edge of the symmetrized G_φ joins sites at ℓ₁-distance ≤ ℓ, so the G_φ-distance is at
     least the ℓ₁-distance divided by ℓ.
  2. The cone condition (iii) of Main's theorem therefore holds for such wings. The proof of the
     Corollary's part (2) then goes through with nearest-neighbour balls replaced by Γ-balls,
     which are finite for finite regions. ∎

**Consequence [W].**
- For a fixed rule in 𝒞 on ℤ^d, option (a) is an influence of finite maximal speed: ℓ sites per
  update in the lattice frame.
- So the posits that give OBSTRUCTION in §3 also bound the Bell mechanism's speed.
- In family form, with O depending on the quotient, Proposition AG still holds and Proposition FS
  does not follow.

**Literature [LIT1].**
- **The result.** Bancal, Pironio, Acín, Liang, Scarani and Gisin, "Quantum non-locality based on
  finite-speed causal influences leads to superluminal signalling", Nature Physics 8, 867 (2012),
  arXiv:1110.3795. For hidden influences of any finite speed v > c, defined in a privileged frame,
  models that reproduce quantum correlations predict correlations that can be used for signalling.
  The construction is multipartite.
- **The lower bound.** Empirical lower bounds on such speeds exist. They are satisfied by a large
  enough ℓ, and they bound nothing here.
- **[CONJ].** It is conjectured, not checked, that a rule in 𝒞 on ℤ^d meeting H-Bell (i) falls in
  the model class of [LIT1] as that paper defines it. That needs the paper's precise hypotheses on
  which configurations must reproduce quantum predictions.
  - If it does, H-Bell (i) and (ii) cannot both hold, for multipartite configurations, for a fixed
    rule in 𝒞 on ℤ^d.
  - Then (S-𝒞) on ℤ^d would conflict with H-Bell. The only remaining route to OBSTRUCTION through
    Proposition AG would be family-form offsets, or PG without (xi).
  - This round does not establish it.

## 7. Fixed point and stop

- **Classification of the nodes.**
  - Nodes 1, 2, 3, 5 and 6 are NEW. Node 4 is ELABORATING: a source analysis that names the
    premise.
  - Node 1 meets P1, nodes 2 and 3 meet P2, node 5 meets P3, and node 2 meets P4.
- **Why the round stops.** Further steps would need one of the following, each excluded or
  outside scope:
  - a specification of the prepared-class rule, a physical rule this round may not choose;
  - a check of [LIT1]'s model class against H-Bell. That is literature work beyond the bounded
    question, and it is named as [CONJ];
  - an analysis of adaptive dependency sets (§5, remark).
- The question is answered under `PLAN.md` §4: INCONCLUSIVE for OI's Bell route, with a scoped
  OBSTRUCTION (I) established for 𝒞 and 𝒞_PG.

## 8. Established / Assumed / Missing

**ESTABLISHED** [W, unreviewed]:
- the form of the edge-generation rule, as activation within the fixed graph Γ (§1.2), with no
  generation outside Γ;
- preparation-indexed adjacency is configuration-indexed under A-U (§1.1);
- Lemma Γ (§2), from Main:368 [P];
- Lemma U (§2);
- Proposition AG and the scoped OBSTRUCTION (I) for 𝒞 and 𝒞_PG, with the excluded class of §3;
- the properties of E1 and its 2^T dependency (§5);
- Proposition FS (§6), from Main's theorem [P];
- the refinement of round 4's premise list (§2): (M1) is redundant under A-13; (M2) follows from
  PG; (M3) and (M4) with a finite alphabet imply (ix) for Γ but not PG; "needs all four" holds for
  the Lemma LE route only.

**ASSUMED:**
- A-U (N);
- A-13 (xiii), A-9 (ix) and A-11 (xi) with a site-local gauge, each (I), in §3 and §6 only;
- H1–H4 at round 4's scopes (I);
- BQ1 and BQ1-D (#1498, reviewed);
- polynomial T (AW-2);
- for §6, Main's Bell-ceiling theorem and the Corollary's hypotheses, including (xiv).

**MISSING:**
- the rule on the prepared class (§1.3);
- the scope of (ix), as a uniform bound on the union reading sets, and of (xi) on the prepared
  class, that is (S-𝒞), or PG directly (§4). This is the single premise that decides OBSTRUCTION
  (I) for OI's Bell route through this route;
- whether H-Bell's "equivalent nonlocal response map" obeys (xiii) (§1.3);
- [CONJ] whether 𝒞 on ℤ^d is incompatible with H-Bell (i) and (ii) through [LIT1] (§6).

## 9. What this record does not claim

- It does not claim that OI's Bell route is in 𝒞, or outside it.
- It does not claim that efficient native QC is impossible, possible, or universal.
- It does not claim that E1, or any rule here, is OI's rule or a candidate for it.
- It does not claim that failure of H5 implies hardness of classical simulation (§5).
- It adopts no premise. It proposes no manuscript change. Comp:120 and the Computation and
  Complexity papers are untouched.
