## Review of PR #918, `papers/Introduction.md` at `a32b769c`

**Verdict: ACCEPT WITH CHANGES.** Two changes are required. Both are wording fixes, in the abstract and in §6, and both concern the same result. The paper is otherwise correct and states its central results at full strength. I made no edits, commits, pushes or comments. Disk was fine (23 GB free). The worktree is removed, and the scratch extracts of Main and GR are deleted.

### What I checked
- **Sources.** Every cited claim in Main, GR, Book §1.11 and §7.6, BH-01 `REPORT.md`/`PLAN.md` and BH-02 `REPORT.md`, read at `55e3217b`.
- **Lean.** All 29 declarations in Appendix A exist at their stated lines at `17b830bc`, and each appears in `papers/introduction_repro/results-121598983127.json` with the three standard axioms. I read the statement of each one against the paper's description.
- **Lean pins.** `verification/lean-mathlib` is identical at `17b830bc` and `55e3217b`. The only difference between the two commits is a Python probe in `verification/lean/`.
- **Branch sources.** Main, GR, `book/` and the black-hole records on the branch are identical to `55e3217b`.
- **Withdrawn and pending items.** The paper does not cite Main §3.5's rest-frame claim (PR #957). It states nothing that depends on SC-22 or SC-23 (no fast-bath or thermalization claims). It does not contradict PRs #956, #958 or #959.
- **Change record.** I read `CHANGES-r16.md` only after forming my own view. Its strength table says the abstract states the recurrence result at full strength; finding 1 disagrees.

### Question 1: Is every substantive claim supported by its stated evidence and assumptions?
Yes, with one exception. The recurrence-cycle indivisibility result, as stated in the abstract and repeated in §6, drops two hypotheses and names the wrong object (findings 1–2).

Everything else checks out:
- Theorem 1; Theorem 2 and its Corollary; the capacity bound and the least hidden memory; the Pinsker floor.
- (C1) from (C4); (C3) holding unconditionally; the two forms of (C2).
- Theorem 3, the CP-indivisibility scope, the Hadamard example, Theorem 4 and the five-way independence.
- The relating-evolution results, the qubit obstruction and the Bell ceiling.
- The §4 split into the established distinction, the conditional proposal and the missing link G3.
- The §5 numbers and the Page-curve conditions.
- The §2.6 matrices and probabilities: I recomputed the minimal model and the card table by hand.

Each Lean description matches its declaration. "Machine-checked" is used only for formalized declarations. Every displayed equivalence that needs §A.34 directional witnesses has them: Theorem 1 by its three inclusions; the Corollary by Thm 2(a) in each realization one way and `S_imp_D` the other; Theorem 4 by `physical_of_exactAll` and `exactAll_of_physical_general`. The full-support equivalence in §2.5 is proved on paper in both directions (Main §2.3 Scope), but the paper does not say which argument gives which direction (finding 6).

### Question 2: Does the paper state the strongest established results without unnecessary weakening?
Mostly yes. §2.4, §2.5 and §3.2 state the results at full proved strength. There are four mild understatements: the abstract omits the full-support equivalence (inside finding 1), §2.5 places a machine-checked step on paper (finding 3), §6 under-classes the §5 floor (finding 8), and §3.3 leaves an established "exactly when" unstated (finding 9). Two established results are absent: the persistence-form necessity of (C2), which needs no mixing hypothesis, and the Bell–lattice corollary (finding 10).

### Findings

**1. Abstract, line 12 — required (overclaim and missing hypotheses).**
- *Current text:* "On a fixed finite reversible system the observed process is stochastically indivisible somewhere in its recurrence cycle whenever a visible transition map from the initial time is not a permutation, which every non-deterministic visible step supplies."
- *Problem:* It drops the hidden prior shared by every root. It also calls the result indivisibility of "the observed process", but the theorem is about the rooted family, which keeps a row for every root, including roots of visible probability zero. Main says the non-permutation can occur "possibly only through a row of a root of visible probability zero". The equivalence with M_k > 0 under a full-support prior is also missing.
- *Evidence:* Main:124 (Theorem, rooted maps, μ_H shared by every root); Main:126 (the zero-probability-root caveat); Main:128 (Scope: the full-support equivalence); Main:20 (Main's own abstract says "the full rooted visible process"); `CausalReadback.lean:178` (`RootedRealization`: "one fixed hidden prior, common to every rooted visible preparation").
- *Proposed replacement:* "On one fixed finite reversible system with a hidden prior shared by every root, the rooted visible family is P-indivisible somewhere in its recurrence cycle whenever some rooted visible map is not a permutation, which every non-deterministic visible step supplies; under a full-support visible prior this indivisibility is equivalent to conditional memory M_k > 0 at some order below the recurrence time."

**2. §6, line 211 — required (the same overclaim).**
- *Current text:* "on a fixed finite reversible system every non-deterministic visible step makes the observed process indivisible somewhere in its recurrence cycle".
- *Problem and evidence:* as in finding 1.
- *Proposed replacement:* "on a fixed finite reversible system with a hidden prior shared by every root, every non-deterministic visible step makes the rooted visible family P-indivisible somewhere in its recurrence cycle".

**3. §2.5, line 103 — optional (weakening).**
- *Current text:* "The step from two histories with a common endpoint to a non-permutation rooted map, and its composition with P-divisibility, are proved on paper."
- *Problem:* Once a non-permutation rooted map is in hand, the conclusion is Theorem 3, which is machine-checked. Only the first step is on paper.
- *Evidence:* `RecurrenceHorizon.lean:148`.
- *Proposed replacement:* "The step from two histories with a common endpoint to a non-permutation rooted map is proved on paper; the conclusion from there is Theorem 3."

**4. §2.5, line 103 — optional (precision).**
- *Current text:* "The conclusion is machine-checked from the *routed* form of (C4)…"
- *Problem:* `routed_forces_indivisible_somewhere` proves `∃ n, PIndivisibleWithin n`, with n = (s+1)·M for M the period. It does not prove failure on {0,…,L}. The module also records that its store clause (`rootedPosterior`) is spelled differently from the discovery round's clause S. Only the overlap consequence is used, and that is the same under either spelling.
- *Evidence:* `PhysicalC4Discharge.lean:122–136` and its header note.
- *Proposed replacement:* "Indivisibility at some return horizon is machine-checked from the routed form of (C4)…"

**5. §3.5, line 175 — optional (reads as assert-then-qualify).**
- *Current text:* "adopts ontic parameter dependence, in which one wing's microstate response depends on the remote setting without operational signalling. Whether that choice is compatible with operational no-signalling … is the open hypothesis H-Bell."
- *Problem:* The sentence asserts no signalling, then names compatibility with no-signalling as open.
- *Evidence:* Main:406 (Corollary paragraph: H-Bell must "preserve operational no-signaling").
- *Proposed replacement:* "adopts ontic parameter dependence: one wing's microstate response may depend on the remote setting, and operational no-signalling is required. Whether a realization on the substratum's coupling graph achieves this and preserves its gravitational continuum limit is the open hypothesis H-Bell."

**6. §2.5, line 103 — optional (§A.34 directions).**
- *Problem:* "is equivalent to M_k>0 at some order k<L" names no direction.
- *Evidence:* Main:128 (Scope).
- *Proposed addition:* "(a gap gives a non-permutation Γ_s, hence indivisibility by Theorem 3; with no gap below L the law on {0,…,L} is Markov, every Γ_s is a permutation, and Γ_s^{-1}Γ_t divides)".

**7. §5, line 203 — optional (precision).**
- *Current text:* "The layout is the framework's nested-partition construction [GR App. A] at small size."
- *Problem:* The 1,376 count is in the moving-partition layout (GR A.7). The nested V/B/D layout gives 2,688.
- *Evidence:* BH-01 `PLAN.md` §2; `REPORT.md`, table of key exact numbers.
- *Proposed replacement:* "The layouts are those of [GR App. A] — the moving partition of A.7 and the nested V/B/D partition of A.1 — at small size; the counts below are in the moving-partition layout."

**8. §6, line 211 — optional (weakening).**
- *Current text:* "the separation of conservation from accessible recovery rests on exact enumeration (§5)".
- *Problem:* The 1/|𝒰| floor and exact recovery under complete access have written proofs for every finite bijection.
- *Evidence:* BH-01 `REPORT.md`, Proofs (C1, C2).
- *Proposed replacement:* "…rests on exhaustive enumeration, with the 1/|𝒰| floor proved (§5)".

**9. §3.3, line 163 — optional (weakening).**
- *Problem:* The two one-way statements together give an "exactly when", which Main states.
- *Evidence:* Main:640; `TrackBQfbBridge.lean:180, :276`.
- *Proposed replacement:* "two such lifts have equal trajectory laws at every horizon exactly when their one-step visible matrices are equal (`bridge_traj` for ⇐; for ⇒, equal trajectory laws give equal rooted families and `rooted_eq_iff_slice_eq`)".

**10. Two established results are omitted — optional (weakening).**
- *The persistence form of (C2) necessity:* in the coupling-step model, observed conditional memory forces some realized hidden conditional at least ε_min(I*, n_V) from π_H, with no mixing hypothesis (Main:465; PR #958). It could go in one sentence after line 93.
- *The Bell–lattice corollary:* the nearest-neighbour cubic graph alone cannot supply ontic parameter dependence for separated wings (Main:406). It could go in one sentence in §3.5.

**11. Open problem 4, line 220 — optional (precision).**
- *Current text:* "…under which observed conditional memory bounds the persistence time of (C2-slow)".
- *Problem:* (C2-slow) is a condition, not a quantity with a persistence time.
- *Evidence:* Main:76, :492; PR #958 (slow-bath form gives "a lower bound on bath persistence").
- *Proposed replacement:* "…under which observed conditional memory lower-bounds the hidden sector's conditional mixing time (the slow-bath form of (C2))".

**12. §4, line 195 — optional (clarity).**
- *Current text:* "…which [GR] names Level G3".
- *Problem:* GR defines its G1–G4 ladder only inside its abstract (GR:12). GR:30, and Structure:154 which it follows, use "Level G3" for the substratum gauge group.
- *Proposed replacement:* "…which [GR] calls the G3 coupling theorem (GR §6.2, §8.5)".

**13. Minor wording — optional.**
- Line 18: "send it to different futures" should be "can send it to different futures" (decoupled bijections do not).
- Line 114: "is P-divisible" should be "is P-divisible on {0,1,2}", to avoid an apparent clash with Theorem 3.
- Line 213: "a single energy shell" should be "with all of 𝒞_B×𝒞_R one energy shell" (GR Thm A.8), and "Page curve" should be "cycle-averaged Page curve".
- Line 28: "§3.2–§3.3" should be "§§3.2–3.5".
- Line 229: "whose Lean sources are identical" should be "whose `verification/lean-mathlib` tree is identical".

**One source note, outside this paper.** In Book §1.11, "a revealed card is burned and replaced" can be read as replacing the hole card, which gives 1, not the book's 1/2. The paper's own rule (overwrite the burn card) is correct, and it states the distinction itself at line 127.

### Strength check

| Central result | Where stated | At full proved strength? |
|---|---|---|
| Theorem 1, S_K = D_K = Q_K at every horizon (machine-checked, three inclusions) | abstract, §1.2, §2.2, §6 | Yes |
| Independent-prior realization for every law (on paper, exact probes) | §2.2 | Yes |
| Theorem 2 (a)–(c) and Corollary M_t>0 ⇔ readout-relevant hidden memory, both directions named | §2.4 | Yes |
| Capacity bound \|C_H\| ≥ 2^{I*}; least hidden memory = I(X<t;X>t\|X_t); Pinsker floor | §2.4 | Yes |
| (C1) from (C4); (C3) unconditional; (C2-structural) and (C2-slow) kept distinct | §2.4 | Yes; the persistence form is omitted (finding 10) |
| Theorem 3, rooted form (machine-checked) | §2.5 | Yes |
| Recurrence-cycle P-indivisibility of the rooted family; full-support equivalence with M_k>0, k<L | §2.5 yes; abstract and §6 no | §2.5 yes; abstract and §6 drop hypotheses (findings 1–2), and §2.5 understates the machine-checked part (finding 3) |
| An in-window revival of distinguishability makes the window P-indivisible; C1–C4 give accessible memory, not window indivisibility | §3.1 | Yes |
| CP-indivisibility for the permutation-dilation family; Hadamard boundary | §3.1 | Yes |
| Theorem 4, both directions, every nonempty finite system; five-way independence; OI alone does not imply QM | §3.2, abstract | Yes |
| Non-selection of the relating evolution | §3.3 | Yes; the "exactly when" could be stated (finding 9) |
| Qubit obstruction (factorization proved, unboundedness imported) | §3.4 | Yes |
| Bell ceiling under (i)–(iv) plus a ±1 outcome every run; mathematics stated separately from interpretation | §3.5 | Yes |
| CC: descriptive distinction established, dissolution conditional on G3 | §4 | Yes, confident, and G3 is named |
| BH: conservation neither implies nor is necessary for recovery; 1/\|𝒰\| floor | §5 | Yes; §6 under-classes the evidence (finding 8) |
