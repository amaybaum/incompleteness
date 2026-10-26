# Independent review of the Theorem A.8 restriction (PR #936, head 2d13792d)

This review covers commit `2d13792d` on top of `b61cbaa9`. It is read-only. Checks ran in a detached worktree at
`bhfix/review3/rv`, which was removed afterwards with `git worktree remove`; no gc was run. The drafter's worktree
is unchanged at `2d13792d`.

**Verdict: BLOCK, narrowly.** The mathematics, A.9, H-decouple, the LEDGER and the mirrors are correct. But the
owner's requirement 2 is not met: the manuscript does not say plainly that taking the whole configuration space
as one shell removes the energy constraint. A.8's proof still reads as if energy conservation of the wave
equation delivers that shell. Three small text changes fix this (§4).

**What a re-check needs.** After those changes, a verbatim check plus the usual checks (fingerprint re-affirmation
for A.8, rebuild, mirror check) suffices. A new review is not needed.

## The owner's three questions

### 1. Mathematical validity: YES

The Page-entropy result is applied only to the full product space, under the theorem's stated assumptions.

**What the statement assumes (GR:819–827).**
- Σ_E = C_B × C_R, "its whole configuration space as a single energy shell", whose span is H_B ⊗ H_R.
- H-scramble holds over the pure states of H_B ⊗ H_R.
- S_Page is labelled "the large-dimension form of Page's mean entropy for Haar-random pure states of H_B ⊗ H_R".

**What the proof uses.**
- Exact cycle averages on Σ_E.
- Measure concentration for Haar-random pure states "of H_B ⊗ H_R" (Lévy/HLW, now scoped explicitly).
- H-scramble carrying the η|Σ_E| count to the orbit.

**The statement equals what the proof supports.** One pre-existing nit: for small d_min the displayed
large-dimension form differs from Page's exact mean (for example 0.886 against 0.922 at 4×4). The statement's
O(ε) absorbs this only once d_min is large enough. The formula is labelled "large-dimension form", so this is
acceptable.

**"Proper energy shells" paragraph (GR:845), checked against DIFF-REVIEW §6 and DIFF-RECHECK N1.**
- It says the value "in general differs", not "only when". Correct.
- The diagonal-shell statement is correct: Schmidt probabilities are uniform on the simplex, the mean is
  H_m − 1, and at m = 2 it is ½ against Page's 1/3.
- The Hamming-weight remark, "the value can lie below S_Page(d_B, d_R)", is correct. BH-02 certifies three
  cases below, off half filling. At half filling the Monte Carlo value is also below, but that is not certified.
- The proper-shell versions of A.8 and A.9 are stated as open.
- Nit: "an energy shell for an energy depending only on b − r" needs "whose value at b = r occurs nowhere
  else" for the diagonal to be a whole shell.

**The records match.** README and CHANGE-NOTE §7 now say "does not hold in general", consistent with N1.

### 2. Physical interpretation: NO, not clearly enough. Exact text in §4.

**What the manuscript says:**
- GR:845: "When energy conservation confines the orbit to a shell whose span is a proper subspace … [open]".
- ch07:126: "on a proper energy shell, a subspace fixed by energy conservation, … the derivation below takes the
  shell to be the full product space".
- GR:605, GR:611 and ch07:12, :116: "taking the energy shell … to be their full product space".

**What is missing.** None of these says what that choice means. A single shell C_B × C_R requires the energy to
be **constant on all configurations of B ∪ R**, so energy conservation places **no constraint** on the orbit.
An evaporating black hole whose radiation carries energy is instead the proper-shell case, which is open. As
written, the full-space choice reads as a modelling convention compatible with energy conservation.

**A.8's proof implies the opposite.** It still opens: "The bijection φ conserves energy (the wave equation is
Hamiltonian), so φ restricts to a bijection on each energy shell, here on Σ_E = C_B × C_R." This presents the
full space as an energy shell delivered by the wave equation's energy conservation. That holds only if the
Hamiltonian is constant on C_B × C_R. For a nontrivial Hamiltonian it is false.

### 3. Consistency: YES. No claim silently extends A.8 or A.9 to smaller shells, with one exception (fix A3).

**What I grepped.** "energy shell", "energy-shell", Σ_E, "proper shell", "product space", "Page curve",
"cycle-averaged", "H-decouple" and "conditional on H-scramble", across:
- GR, Main, Substratum and Explainer;
- book ch07, ch09, ch18, ch19, the glossary, appendix-a and README.md;
- FULL.md.

**Sites that state the full-product-space condition or the open proper-shell case:**
- GR: :605, :611, :717, :811 (H-decouple), :819–827, :835, :845, :847 (A.9), :877.
- Book: ch07:12, :116, :126, :130, :147, :149; ch19:72; glossary:113; G11 (appendix-a:116).

**Necessity form, no sufficiency claimed:** ch07:288 and appendix-a:103 ("requires H-scramble and H-decouple").

**Unrelated "energy-shell" uses** (the horizon temperature): GR:28, :30, :58, :617, :623; ch07:14;
ch09:14, :48, :118; Explainer:290.

**Ambiguous mechanism names (nit):** ch18:148 and ch19:72 say "cycle typicality on the energy shell rather than
replica wormhole computation"; ch07:147 and GR:877 say "substratum's cycle structure on the energy shell". These
do not assert the Page value on a proper shell, but "configuration space" would remove the ambiguity.

**The exception: two sufficiency-form status surfaces omit the new condition.** G11 was updated; these were not:
- **ch09:127 / FULL:2607**: "Page curve conditional on H-scramble and H-decouple".
- **README:64**: "a cycle-averaged Page curve conditional on … H-scramble and … H-decouple".

In this corpus "conditional on" is the sufficiency label; dependency_label_check treats it as carrying the
condition. Read with the black hole's conserved energy, these imply the curve under two conditions, which is
the proper-shell case. That is a quiet extension, so it is required (A3). I withdraw the drafter's "claim no
sufficiency" classification for these two sites; it holds only for ch07:288 and appendix-a:103.

## Other checks

- **A.9 and H-decouple are consistent with the restricted A.8.**
  - A.9 takes "the energy shell of Theorem A.8, the full configuration space of B ∪ R at that stage".
  - H-decouple (GR:811) keeps everything that matters:
    - closure: "φ acts as a bijection of its configuration space C_B × C_R", which in A.8 is a single shell;
    - purity: "a pure joint state … stays pure";
    - the time window: "whole cycles, not only the evaporation".
- **The added propagation sites are needed.** GR:605, GR:717, ch07:12 and ch07:116 are all sufficiency
  statements. Leaving ch09:127 and README:64 unchanged is wrong (A3); leaving ch07:288 and appendix-a:103
  unchanged is right.
- **FULL mirror.** All 9 changed chapter lines occur exactly once in FULL, FULL's diff adds exactly 9 lines, and
  mirror_check reports 0 lines absent.
- **LEDGER.**
  - A.8 (line 819) and A.9 (line 847, moved from 843 and matching the file) both stay `"kernel": "GAP"`.
  - coverage_check passes at the head.
  - Countercontrol: restoring the old fingerprints 17e40e97… (A.8) and ed567edf… (A.9) makes each FAIL as
    STALE, naming the new fingerprints 31eafe29… and e3222fa7…. So these are the fingerprints of the new
    statements.
- **Other checks, all OK:** voice_check, claims_check, duplicate_check, dependency_label_check --strict,
  artifact_placement_check, and legacy_records_check (303 records intact).
- **Nothing else broken or overclaimed.** Apart from §2 and the A3 sites, the commit introduces no new claim.
  The Page-curve sufficiency statements are now conditional on the full-space restriction wherever they are
  stated in full.

## 4. Required changes (exact text)

Each chapter edit applies identically to its FULL mirror. Line numbers are at `2d13792d`.

**A1. GR A.8 proof, first sentence (GR:829).** Replace
> *Proof.* The bijection $\varphi$ conserves energy (the wave equation is Hamiltonian), so $\varphi$ restricts to a bijection on each energy shell, here on $\Sigma_E = \mathcal{C}_B \times \mathcal{C}_R$.

with
> *Proof.* By hypothesis the energy is constant on $\mathcal{C}_B \times \mathcal{C}_R$, so energy conservation places no constraint on the orbit and $\varphi$ acts as a bijection of $\Sigma_E = \mathcal{C}_B \times \mathcal{C}_R$.

**A2a. GR "Proper energy shells" paragraph (GR:845).** Replace its first sentence
> Theorem A.8 is stated for the full product space.

with
> Theorem A.8 is stated for the full product space. Its hypothesis requires the energy to be constant on $\mathcal{C}_B \times \mathcal{C}_R$, so that energy conservation places no constraint on the orbit of $B \cup R$; it does not follow from the conservation of a Hamiltonian that takes more than one value there, whose energy shells all span proper subspaces. An evaporating black hole whose radiation carries away its energy is in that proper-shell case.

**A2b. Book, ch07:126 / FULL:2003.** Replace
> so the derivation below takes the shell to be the full product space of the black hole and its radiation, and the energy-shell version is open ([GR Appendix A]).

with
> so the derivation below takes the shell to be the full product space of the black hole and its radiation, which places no energy constraint on them; an evaporating black hole whose radiation carries away its energy is the energy-shell case, and that version is open ([GR Appendix A]).

**A3. Status surfaces.**
- ch09:127 / FULL:2607: "Page curve conditional on H-scramble and H-decouple;" → "Page curve conditional on
  H-scramble and H-decouple, on the full product space;".
- book/README.md:64: "and a cycle-averaged Page curve conditional on the scrambling condition H-scramble and the
  decoupling condition H-decouple." → "and a cycle-averaged Page curve on the full product space of the black
  hole and its radiation, conditional on the scrambling condition H-scramble and the decoupling condition
  H-decouple."

**After A1–A3.** A1 and A2a do not change A.8's statement, so its LEDGER fingerprint should be unaffected;
confirm this with coverage_check. Then:
- rebuild GR and the book;
- run mirror_check;
- re-grep "the wave equation is Hamiltonian), so" (expect 0) and "conditional on H-scramble and H-decouple"
  (every hit should carry the full-space scope or be in necessity form).

## Nits (optional)

- "Cycle typicality on the energy shell" → "cycle typicality on the configuration space" at ch18:148 / FULL:4968
  and ch19:72 / FULL:5248.
- Diagonal-shell parenthetical at GR:845: "an energy depending only on b − r" → "an energy depending only on
  b − r and taking its value at b = r nowhere else".
