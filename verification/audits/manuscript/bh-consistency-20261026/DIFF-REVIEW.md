# Independent review of the BH correction diff (draft PR #936)

**Object.** Branch `fix/bh-consistency-20261026`, head `4c0d705e`, base `main` `687e885b`. Inputs read: the
drafter's change note and the full word-diff of every `.md`, `.py` and `.json` file.

**Read-only.** The drafter's worktree was not touched. My checks ran in a detached review worktree
(`bhfix/review/rv`), which was removed afterwards with `git worktree remove`.

**Verdict: ACCEPT WITH CHANGES.** Four required changes (R1–R4) follow, each with exact text. None of them
requires reopening a decision already made.

## 1. Faithfulness to REVIEW.md

Every correction I confirmed is applied, at every site and FULL mirror, with my changed wording where I
supplied it:
- ch07:110, ch07:126 s1–s2, ch07:132, ch07:159–161 (no "remnant");
- ch18:146 (verbatim), ch18:148, ch18:158 (verbatim), ch19:334;
- GR:611, GR:811, GR:869 (both sentences);
- §C.4 repair (a);
- the missed sites M1 (GR:605), M2 (README:64), M3 (ch07:149), M4 (ch07:116), M5 (GR:717), M6 (A.7),
  M7 (GR:829 / [61]), M8 (bibliography), M9 (ch18:156) and M10 (ch07:130);
- M11, checked and left unchanged; the drafter's reading of ch19:366's ten is correct.

**Mirrors, checked independently.**
- All 28 new chapter lines occur exactly once in FULL.md, and no removed chapter line survives there.
- FULL.md's own diff is exactly +28/−26: the 26 replaced lines, plus the two new bibliography entries.

**One paraphrase was missed.** **ch07:147 / FULL:2024**, the book mirror of GR:869 sentence 1, is not
updated, so the book now lags the paper (R3).

## 2. The drafter's three departures

**(a) The scope of H-decouple.**
- Including V∖R is right. It captures the gap I found at A.7: a pure state on V⊗B restricts to a pure state on
  B⊗R only if V∖R is unentangled with B∪R.
- It adds no physical assumption beyond what A.8 already presupposes, because A.8 is stated "for the dynamics φ
  on the energy shell Σ_E ⊂ H_B ⊗ H_R", which is a closed B∪R system.
- **The definition no longer matches what Theorems A.8–A.9 use once A.9 is a full-cycle average** (R1).
  - As defined, H-decouple holds "over the evaporation", and in a *state* sense: "unentangled with V∖R".
  - A.8, and the restated A.9, require *dynamical* closure: φ must act as a bijection of the B∪R shell, over
    whole cycles of the dynamics and not only over the evaporation. A pure, unentangled B∪R state at each
    time does not by itself make the reduced evolution a permutation of the shell.
  - With H-decouple as drafted, "a cycle-averaged Page curve follows under H-scramble and H-decouple" names a
    condition weaker than the one the derivation uses.
  - Redefining H-decouple as the closure A.8 already presupposes fixes every summary site at once and adds
    nothing new.

**(b) A.7 restated at the scope its proof supports, with error O(t/τ_B^D).**
- Accepted. The error term is what Theorem A.5's step (i) supplies, and the "∼10⁻³²" is correctly removed.
- The new paragraph correctly says that A.7 does not establish the purity of B∪R.
- Observation, no change needed: in the setting of A.7's own proof (a definite initial configuration), the total
  state is a configuration basis state at every t. So ρ_VB and ρ_BR are *exactly* pure, product, with S = 0.
  H-decouple's purity clause bites only outside that setting, which is exactly where H-scramble could hold.
  That is the reason for R2.

**(c) The O-2 fact stated in GR:831.**
- Accepted. The sentence is correct (BH-02 C1, a one-line proof), and it keeps the book from leading the paper.
- But the paper now proves, three lines before calling H-scramble "not established", that H-scramble fails for
  every bijection in the A.7 setting. It still says the Page curve is "reproducible from a finite deterministic
  substratum" (GR:869, ch07:149).
- The consequence BH-02 C6(a) needs stating. It is a corollary of the drafter's own sentence and adopts no
  remedy (R2). This is not an owner choice: only the *remedy* (a superposed initial state, or a non-aligned
  factorization) is O-2.

## 3. The A.9 restatement

**Is it exactly what A.8 proves?** Yes:
- A.8 fixes (d_B, d_R) and bounds the full-cycle time average by S_Page(d_B, d_R) + O(ε), outside a fraction
  that is exponentially small in d_min.
- A.9 now fixes the stage-t bipartition, takes the exclusion and the O(ε) from A.8 per stage, and substitutes
  d = q^n. The "Direct substitution" proof is now valid.
- The added paragraph correctly separates the single-trajectory S(ρ_R(t)) and states that it is open.

**Every pointwise quotation is updated or scoped:**
- GR:605, :611, :717, :805 (now the provable bound S(ρ_B) = S(ρ_R) ≤ n_R ln q), :865, :869;
- ch07:12, :116, :130–132, :149, :157 (bound ≤ n_R ln q), ch19:72, glossary:113, README:64.
- ch07:134–135 ("entropy rises / falls …") and :137 describe the displayed S̄ just above them, which is
  acceptable.
- **The exception is ch07:147**, "arrives at a Page curve of the same form — rise, turnover, fall". It still
  reads pointwise, and it omits H-decouple (R3).

## 4. Editorial rules

- **Claim/evidence boundary.**
  - The changes are sound apart from R1 (H-decouple as defined is weaker than what is used) and R2 (the
    finite-substratum reproducibility claim stands next to a proved failure in the stated setting).
  - No new physical assumption is introduced silently: H-decouple names what A.8 presupposes, and after R1 it
    names exactly that.
- **§A.27/§A.30.** The added lines contain no self-narration. I scanned them for now / no longer / formerly /
  corrected / withdrawn / previously / reader-instruction phrases: 0 hits.
- **Assert-then-qualify.** "Resolved at the level of information preservation" (ch07:110, ch19:72) is a scoped
  status, not assert-then-qualify.
- **§A.32/§A.33 (GR register).**
  - The GR additions are neutral and technical, with no meta-commentary.
  - ALL-CAPS hits in added lines are only acronyms: CPTP, DESI, LIGO, KAGRA, MOND.
- **§A.25, my own re-grep** (Page curve, S_rad, H-scramble, information paradox, cycle typicality, resol…
  paradox, mass-independent, exponentially small, horizon-factorization, τ_evap):
  - Apart from ch07:147, the only remaining Page-curve hits without "cycle-averaged"/"H-decouple" are the QES
    literature, Page's definition, headings, A.8's statement, Main:66 and :668, and the condition-free status
    surfaces (ch19:30, :334, ch18:130, :343). All are correct.
  - The FULL mirrors are byte-identical.

## 5. Generated files and tools

- **`.tex`.**
  - GR.tex has 20 hunks and FULL.tex 30. All are content corresponding to the `.md` edits, plus pandoc reflow
    (for example the "95%" line in the ch07:12 paragraph).
  - The `% source-sha256` stamps equal the sha256 of `GR.md` and `FULL.md` at `4c0d705e` (verified: 68598662…
    and 17d8e99a…).
- **LEDGER.** Legitimate.
  - Both entries stay `"kernel": "GAP"`, with no checks and delta "not formalized".
  - `coverage_check` passes at the head (128 statements).
  - Countercontrol: restoring A.7's old fingerprint makes it FAIL with "STALE entry GR:T-a.7 … afea3a8c… →
    ef7fd416…". So the new value is the fingerprint of the new statement.
- **`dependency_label_check`.** Adding `decouple` to `CONDITION_TOKENS` is exactly what its comment requires
  ("Add new names here when they are introduced"). `--strict` passes.
- **Other checks at the head, all OK:** `voice_check`, `claims_check`, `duplicate_check`,
  `lean_manuscript_census`.
- **`staleness_check` not reproducible here.** The `.tex` files are not checked out in the sparse review
  worktree, so `staleness_check` reports UNSTAMPED. I verified the stamps directly instead.
- **R1–R4 change GR.md and the book.** The `.tex`/`.pdf` must be rebuilt after them. A.7's statement is
  unchanged, so its fingerprint is unaffected.

## 6. Theorem A.8 and BH-02 C6(c): verdict

**A statement-level error, settled by exact algebra.**
- **The counterexample.** Take the diagonal shell Σ = span{|i⟩_B|i⟩_R : i = 1..m}. It is an energy shell for
  any energy depending on b − r.
- **Its Haar mean.** A Haar-random vector there has Schmidt probabilities distributed Dirichlet(1,…,1), so the
  mean entanglement entropy is exactly H_m − 1.
  - At m = 2 this is 1/2 = 2∫₀¹(−p ln p)dp. Page's exact mean is S(2,2) = 1/3, and A.8's displayed formula
    gives ln 2 − ½ ≈ 0.193.
- **Off half filling the gap is leading-order.** BH-02 certifies, for Hamming-weight shells, values below
  S_Page(d_B, d_R) by concavity: at n = 10, w = 2, 1.60 against 2.97.
- **Conclusion.** H-scramble (Haar on the *shell*) plus measure concentration gives a time average equal to the
  Haar-on-shell mean, not S_Page(d_B, d_R). A.8's value holds only when the shell is the full product space, or
  with shell-effective dimensions.
- **Inheritance.** The cycle-averaged A.9, and every statement of the turnover at d_R = d_B and of min·ln q,
  inherit this.

**Remedy (owner's choice, in a separate change).** Either:
1. restrict A.8 and A.9 to Σ_E = H_B ⊗ H_R, an explicit hypothesis; or
2. replace S_Page(d_B, d_R) by the Haar-on-shell mean and restate the turnover in shell terms.

**Not blocking for this diff.** The diff does not worsen the defect, and ch07:149's "the open steps include …"
is non-exhaustive. The PR description should record that the sufficiency statements "under H-scramble and
H-decouple" (GR:869 last sentence, A.9's label, ch07:116, ch07:149, ch19:72) remain subject to this open
statement-level gap.

## 7. Required changes (exact text)

Each required change applies to the chapter and, identically, to its FULL mirror. Line numbers are at `4c0d705e`.

**R1. H-decouple = the closure A.8 presupposes.**

GR:811, replace
> Theorem A.7 is stated for $t \ll \tau_B^D$. Theorems A.8–A.9 work with a pure joint state of $B$ and $R$ at the Page time and over the evaporation, and so rely on the decoupling condition **H-decouple**: over the evaporation, $B \cup R$ stays decoupled from the trans-cosmological sector $D$ and unentangled with the rest of the visible sector, $V \setminus R$, so that its joint state remains effectively pure. Timescale ordering does not supply H-decouple, and it is not established here.

with
> Theorem A.7 is stated for $t \ll \tau_B^D$. Theorems A.8–A.9 treat $B \cup R$ as a closed system, on which $\varphi$ acts as a bijection of an energy shell $\Sigma_E \subset \mathcal{H}_B \otimes \mathcal{H}_R$, so that a pure joint state of $B$ and $R$ stays pure; applied to the black hole and its radiation, they therefore rely on the decoupling condition **H-decouple**: $B \cup R$ evolves with no coupling to the trans-cosmological sector $D$ or to the rest of the visible sector, $V \setminus R$, and its joint state is pure. The full-cycle averages of Theorem A.9 use H-decouple over whole cycles of the dynamics, not only over the evaporation. Timescale ordering does not supply it, and H-decouple is not established here.

GR:817, replace the last sentence
> Theorems A.8–A.9 take the joint state of $B$ and $R$ to be pure, on $\mathcal{H}_B(t) \otimes \mathcal{H}_R(t)$, throughout the evaporation; that is the condition H-decouple.

with
> Theorems A.8–A.9 take $B \cup R$ to be a closed system in a pure joint state on $\mathcal{H}_B(t) \otimes \mathcal{H}_R(t)$; that is the condition H-decouple.

ch07:130 / FULL:2007, replace
> which keeps the black hole and its radiation in an effectively pure joint state over the evaporation,

with
> which treats the black hole and its radiation as a closed system in a pure joint state,

**R2. State the C6(a) consequence (a fact, not a remedy).**

GR:835, replace
> Under H-scramble the counting step below goes through with $\eta|\Sigma_E|$ as written.

with
> Under H-scramble the counting step below goes through with $\eta|\Sigma_E|$ as written. By the preceding paragraph, H-scramble fails for every bijection in the setting of Theorem A.7's proof, a definite initial configuration with the bipartition aligned to the configuration coordinates: it requires an initial superposition of configurations or a bipartition not aligned with them, and which of these the substratum supplies is open.

ch07:126 / FULL:2003, replace
> Applying it to the substratum requires H-scramble: uniformity over classical microstates is not uniformity over quantum pure states, and every finite bijection acting on a definite configuration, with the bipartition aligned to the configuration coordinates, visits only product states, however uniformly it counts its energy-shell cycles ([GR Appendix A]); the condition is named, not established.

with
> Applying them to the substratum requires H-scramble: uniformity over classical microstates is not uniformity over quantum pure states, and every finite bijection acting on a definite configuration, with the bipartition aligned to the configuration coordinates, visits only product states, however uniformly it counts its energy-shell cycles ([GR Appendix A]). H-scramble therefore fails in that setting and requires an initial superposition of configurations or a bipartition not aligned with them; which of these the substratum supplies is open, and the condition is not established.

This also fixes the antecedent of "it", since "results" is now plural (R4).

**R3. ch07:147 / FULL:2024, the mirror of GR:869.**

Replace
> The framework arrives at a Page curve of the same form — rise, turnover, fall — through a substantially different mechanism. The cycle-typicality argument invokes the Popescu-Short-Winter theorem applied to the deterministic substratum dynamics on the energy shell, under the scrambling condition H-scramble of [GR Appendix A] — uniformity over classical microstates is not uniformity over quantum pure states, and that condition is not established — with no replica trick and no gravitational path integral.

with
> The framework arrives at a cycle-averaged Page curve of the same form — rise, turnover, fall — through a substantially different mechanism. The cycle-typicality argument applies Popescu-Short-Winter measure concentration to the deterministic substratum dynamics on the energy shell, under the scrambling condition H-scramble and the decoupling condition H-decouple of [GR Appendix A] — uniformity over classical microstates is not uniformity over quantum pure states, and neither condition is established — with no replica trick and no gravitational path integral.

**R4. "Applying it" → "Applying them" in ch07:126.** This is included in the R2 text.

**After R1–R4:**
- rebuild GR and the book;
- rerun `mirror_check`, `coverage_check`, `voice_check` and `dependency_label_check --strict`;
- re-grep "keeps the black hole", "throughout the evaporation" and "arrives at a Page curve" (expect 0
  surviving).

## 8. Optional

- **GR:611, "Popescu-Short-Winter typicality [29]"** → "measure concentration [29, 61]", to match GR:829's
  attribution. The same applies to GR:869's "applies Popescu-Short-Winter [29]".
- **GR:605, "Appendix A resolves the formal nested-partition machinery"** → "develops".
- **Introduction r4:201 and :241.** Use the drafter's proposed wording. With R1, the r4:241 form "only under
  H-scramble and H-decouple" stands.

## 9. Nothing else broken

- The checks pass (§5).
- No count moves: G11 stays class C.
- ch19:370's "ten" excludes black-hole information.
- The change makes no OI–QM equivalence claim.
- The diff does not newly overclaim beyond R1 and R2, both of which are pre-existing tensions that the diff's own
  correct additions made visible.
