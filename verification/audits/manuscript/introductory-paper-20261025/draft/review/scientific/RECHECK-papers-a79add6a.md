## Re-review of PR #918, Introduction r17 (`a32b769c` → `a79add6a`)

**Verdict: ACCEPT WITH CHANGES.** The recurrence theorem now has the same scope in the abstract, §2.5 and §6, and most of the strengthened claims are supported. Four required corrections remain, all wording-level. Three are newly introduced overclaims: in the abstract's cosmological-constant clause, the summary sentence at L113 and the H-decouple clause. The fourth is a symbol clash in the new (C2) persistence-form sentence.


### Confirmation 1: Scope — confirmed in substance
- **The four sites agree.**
  - The abstract (L16), the §2.5 Corollary (L109) and §6 (L217) all state the same thing. The hidden prior is shared by every root and drawn independently of it. The object is the rooted family, with rows for zero-probability roots. The hypothesis is some rooted matrix that is not a permutation, supplied by every non-deterministic visible step. Under a full-support prior the result is equivalent to M_k>0 below L.
  - Both directions are given at L111. Full support is correctly placed in the converse only, which matches Main's Scope: "Full support enters only in the first of these steps".
- **Small wording gap, not a scope difference.** The Γ_t definition (L101) and Theorem 3 (L103) say only "one hidden prior shared by every root". That is all the rooted family needs. Independence of the root draw matters only for the history clauses, and the Corollary carries it. Adding "drawn independently of it" at L101 would make the wording literally identical (optional).
- **Sources match.**
  - Main at `4449b0d9`: the theorem is at :137, its proof at :139 and its Scope at :141. Main's :124, :126 and :128 are blank lines at that commit, so I used these anchors instead.
  - Main §2.3 is unchanged since `55e3217b`. The only Main hunks between the two commits are at :99, :109, :336 and :652.
  - `CausalReadback.lean:178` (`RootedRealization`, "one fixed hidden prior, common to every rooted visible preparation") matches.
- **Medicine :25 at `652afa09`** has the same hypotheses, object and equivalence. It says "rooted visible map" where the Introduction says "rooted transition matrix", and the Introduction names the zero-probability rows explicitly.

### Confirmation 2: Support of the strengthened claims — confirmed, with one exception (finding 2)
- **Machine-checked part of Theorem 3 (L105, L111).** Correct. From a non-permutation Γ_s the conclusion is Theorem 3 with n=L (`RecurrenceHorizon.lean:148`). Only the supply of the non-permutation is on paper, and the paper says so.
- **Return horizon from routed readback (L111, App. A).** Correct. The kernel proves `∃ n, PIndivisibleWithin n`. The n it reaches is a multiple of |Perm(V×H)| (`rootedMap_periodic` says explicitly that this is not the order L). "At some return horizon" is therefore exactly right.
- **The 1/|𝒰| floor (§6).** Correct. BH-01 gives written proofs C1 and C2, valid for every finite bijection.
- **Rooted-family "exactly when" (L171, App. A).** Correct. `rooted_eq_iff_slice_eq` is an iff. The trajectory-law direction is cited only through `bridge_traj`, and `realData_traj_stochastic` is cited correctly.
- **Persistence form of (C2) necessity (L97).** The coupling-step scope and the absence of any mixing hypothesis are correct (Main :463 and :76). The quantity in the bound is not (finding 2).
- **Bell–lattice clause (L181).** Correct, matching Main §3.3's Corollary.
- **No-signalling (L181).** Now stated as a requirement, and H-Bell is worded as in Main.
- **The 1,376 count.** Correct. It is in the moving-partition layout. The schedule `sched_mp = [(), (2,), (1,2), (0,1,2)]` reads the emitted registers, and message mode 0 is unread after two emissions.
- **Other new content checked.**
  - a/(2−a) is correct: P(x₁=1)=(2−a)/3 and P(x₂=0,x₁=1)=a/3.
  - The off-diagonal entries 4/9 are correct.
  - The spectator-independent readout gloss matches `MapSpectatorIndependent` (`OperationalAssembly.lean:151`).
  - "only components within d_G-distance k" matches Main's cone lemma.
  - The de Sitter dimensional identity matches GR §6.3.
  - "G3 coupling theorem [GR §6.2, §8.5]" matches GR :637.

### Confirmation 3: Scope discipline — three expansions to fix (findings 1, 3, 4)
- **No established result is weakened.**
  - The r17 cuts only remove material repeated elsewhere: the Born-exponent §3.5 sentence (still in §2.3 and open problem 2), "represents, does not derive" in §1.2 (still in §3.1 and §6), the closing line of §6, and attributions moved to where each result is stated.
  - The content `a79add6a` restored is accurate.
- **Three sites state more than the evidence supports:** the abstract's cosmological-constant clause, L113 and the H-decouple clause (findings 1, 3 and 4).

### Other checks
- **§2.4 Corollary.** Byte-identical to r16 (SHA-256 `b596be8a…`). `INTRODUCTION:C-unnamed-b596be8a` is unchanged.
- **New coverage row.** `INTRODUCTION:C-recurrence-cycle-indivisibility` (MIRROR, fingerprint `d33c081326f983a5`) is at line 109. All six row lines match the paper. `coverage_check` at the head reports OK, with 134 canonical statements.
- **Appendix A.** Every identifier and line number is unchanged from r16, where I resolved all 29 at `17b830bc`. Only two descriptions changed: the routed item and `rooted_eq_iff_slice_eq` ("both directions"). Both are accurate.
- **#957 (rest frame).** It touches Main :253 and :657, SM, Substratum and book ch19. The paper cites none of these.
- **#959 (residual memory scope).** In Main it rewrites the §2.3 Genericity remark (non-permutation T versus (C1)) and some ledger rows. In book ch01 it changes §§1.4, 1.6 and 1.10, not §1.11. In GR it changes §2.2's divisibility sentence. Nothing in the paper contradicts these.
- **#958 (now on main).** The paper's two (C2) forms, the slow-bath form as a lower bound on the mixing time, and (C3) as unconditional all agree with it. Nothing is stale.

### Answers to the owner's standing questions
- **(a) Is every substantive claim supported?** Yes, except findings 1–4.
- **(b) Are the strongest established results communicated without unnecessary weakening?** Yes. The recurrence Corollary, the persistence form of (C2), the Bell–lattice clause, the 1/|𝒰| floor and the rooted "exactly when" are all stated at proved strength.

### Findings

**1. Abstract, L16 — required (overclaim; presents the dissolution as established).**
- *Current text:* "OI separates the zero-point sum from the gravitational source…"
- *Problem:* This reads as gravitational decoupling. GR §6.2 establishes only the two-level distinction. GR :356: "Invisibility to quantum mechanics is not decoupling from gravity; the latter is a coupling theorem and is what G3 names as open." r16's wording was accurate.
- *Replace with:* "OI places the zero-point sum and the effective cosmological constant at different levels of description, and separates conservation of black-hole information from its accessible recovery; open are …"

**2. §2.4, L97 — required (overclaim through notation).**
- *Current text:* "observed conditional memory I*>0 at an accessible order forces … at least ε_min(I*,|𝒞_V|)>0 …"
- *Problem:* L95 defines I* = max_t I(X<t;X>t|X_t), the past–future information. Main's theorem bounds the one-step memory I(X<k;X_{k+1}|X_k) = M_k (Main :463). M_k can be much smaller than I*: Main :610 gives M₁=0 with a 1-bit past–future term. So ε_min(I*) is not justified by the theorem.
- *Replace with:* "observed conditional memory M_k>0 at an accessible order k forces some realized hidden conditional at that coupling time to lie at total-variation distance at least ε_min(M_k,|𝒞_V|)>0 from the model's reference prior…"
- Optionally, define ε_min as the inverse of 2[ε log(n_V−1)+h(ε)].

**3. §2.5, L113 — required (overclaim; contradicts the Corollary's own scope).**
- *Current text:* "Recurrence-cycle indivisibility thus follows from finite reversibility and partial access alone, Markov laws included, and does not distinguish one law from another…"
- *Problems:*
  - It needs a non-permutation Γ_s. A deterministic visible law, or a decoupled hidden sector, gives a divisible family.
  - "Markov laws included" holds only for laws Markov on every accessible window. Under full support, a law with no memory below L is divisible (Main :141).
- *Replace with:* "Recurrence-cycle indivisibility thus needs only finite reversibility and one non-deterministic visible step, and holds also for laws that are Markov on every accessible window, so it does not separate them from memory-bearing laws at accessible orders; what an observer can discriminate is memory at an accessible order, which (C4) asserts [Main §2.3, Scope]."

**4. §5, L213 — required (overclaim; introduced in r17).**
- *Current text:* "*H-decouple* … which the effective-pure-state theorem [GR, Thm A.7] supplies only for times short compared with the D-sector timescale…"
- *Problem:* Theorem A.7 gives only that the joint V–B state is pure at leading order for t≪τ_B^D. GR App. A.7: "Theorem A.7 does not establish this [that V∖R is unentangled with B∪R] … Timescale ordering does not supply it, and H-decouple is not established here." So A.7 does not supply H-decouple at any time.
- *Replace with:* "…which is not established: the effective-pure-state theorem [GR, Thm A.7] gives a pure joint state of V and B only for times short compared with the D-sector timescale τ_B^D∼1/H [GR App. A.5], far shorter than the evaporation [BHa], and does not establish that V∖R is unentangled with B∪R [GR App. A.7]".

**5. §6, L217 — optional (keep verification layers distinct).**
- *Problem:* Under "Machine-checked:", the composite "Theorem 3 …, which with the elementary fact … gives recurrence-cycle P-indivisibility …" also uses Γ_L=I at the order L. That step and the shared-column fact are on paper.
- *Suggestion:* append "(the shared-column fact and Γ_L=I being elementary steps on paper)", or move the composite into the "Proved on paper" list with Theorem 3 named as its machine-checked core.

**6. §5, L209–211 — optional (precision).**
- *Problem:* "the observer reads … in the counts below the emitted radiation registers" and "a message … written into designated interior registers" do not cover every count. The 60-map count reads every register (stated). The 32-map count writes the two-bit message into both registers, B and R, and reads R (`checks.py`, AM2).
- *Suggestion:* scope the reading sentence to the 1,376 count, and note that in the 32-map case the message occupies both registers.

**7. L101 and L103 — optional.** Add "drawn independently of it", for verbatim identity with L16, L109 and L217 (see Confirmation 1).
