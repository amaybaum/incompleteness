**SC-22 review: branch `corpus/sc22-n-regime` at `eaeed819`, one commit on main `0d917665`**

**Verdict: ACCEPT WITH CHANGES.** The core of the unit holds up:
- The peak definition of 𝒩 is correct.
- The cumulative Breuer–Laine–Piilo (BLP) sum is named and kept apart correctly.
- The XOR remark is right.
- The table is removed and only the conclusions Main supports are kept.
- The FULL mirrors are exact.

Four required findings remain. Two are definition inconsistencies the relabel left in ch15/ch09, one is a G² overclaim on a sentence the unit edited, and one is §A.42 support for the record. A fifth required item, ch18 :86, needs the owner's decision first.

I set the branch ref with `git ls-remote` (`eaeed819…a581`). I reviewed it in a detached worktree and removed that afterwards; no gc or prune was run. I committed, pushed and commented on nothing.

### Checks
- **Release gate** (`python3 -I tools/release_gate.py`): every step passes except `lean-axioms`, which is the expected local failure. Mirror shows 0 lines absent, architecture shows 259 invariants and 0 violations, staleness shows 0 unstamped, voice/claims/citation all OK.
- **`edge_rigidity_probe.py`**: ALL CHECKS PASS.
- **Probes**: I re-ran `regime_exact.py`, `enum_window.py` and `blp_unbounded.py` from the audit branch at `42bbd33c`, in a scratch copy with `python3 -I -B` (Python 3.13). All three outputs match the committed `.out` files byte for byte.
- **`proposals.py`**: run against the `0d917665` chapters, all 56 old strings are unique in their chapter and in FULL.
- **Mirror check (my own script)**: the chapter diff and the FULL diff have equal multisets, 78 lines added and 86 removed on each side. Every chapter line at the head appears in FULL.
- **FULL .tex/.pdf stamp**: the `.tex` stamp equals the sha256 of FULL.md. Regenerating the `.tex` with pandoc matches the committed one exactly, apart from the stamp line. The PDF has 558 pages, the same as at base. Its text carries the new label (60 hits, the 57 text sites plus the 3 renamed headings in the TOC), keeps only the 2 excluded old-label sites, and has no table rows.
- **Re-grep**: matches the record exactly. The old label appears 2/2/0 (chapters/FULL/papers), the new label 57/57/0, the banned vocabulary 0/0/0.
- **Added-lines scan**: no §A.32/§A.33 phrase hits; the only matches are on lines carried over unchanged. Caps tokens (DYNAMICS, OPERATIONAL, MEMORYLESS, PROPOSED) were already present; book prose is exempt in any case. The secrets/URL/IP/e-mail scan is clean.
- **Additional probe I ran**: across the (3,2) population with a gap in the window (616 models), the exact peak revival over general preparation pairs equals the point-root value in every model. So D3 over "pairs of preparations" agrees with the probes' point-root numbers there.

### 1. The 𝒩 definition (ch18 :74, glossary :125)
- **Peak definition: correct.** "The largest d_t − d_s over pairs of preparations and s<t in W" is D3. It lies in [0,1] and is a single increase, not the maximum of d_t.
- **Main §2.3:** "𝒩>0 certifies P-indivisibility; the converse fails" matches it. P-divisibility makes total variation non-increasing, and Main states the converse is false.
- **Cumulative BLP sum: correct.** The periodicity argument is right: Main §2.3 gives Γ_{t+L} = Γ_t. A revival therefore recurs in every period, and the cumulative sum grows without bound. The recorded values 2/3, 4/3, 10/3, 20/3 against a peak of 2/3 replay exactly.
- **XOR remark: correct.** Main §2.3 Scope names XOR as the counterexample to "C4 forces P-indivisibility on short windows". regime_exact row B shows a gap at order 1 and P-divisibility with R = 0 on {0..2}.
- **Optional (ch18 :74, glossary :125, "trace distance … or total variation"):** fix d to the total variation of the visible population laws (equivalently the trace distance of the diagonal states). As written, two metrics could give two different values of 𝒩. TV is what D3, Lean `C4r` and the probes use.
- **Optional (ch18 :74, "on a finite reversible system the rooted laws are periodic"):** add [Main §2.3] there.

### 2. The relabel (57 sites, FULL exact)
- The label reads correctly at every site.
- No site suggests a complete quantum theory or a partial reconstruction of one. The anchor at ch18 :74/:76 explicitly says "not a complete operational quantum theory".
- **My view on the label:** it is accurate, not wrong. The description in the regime really is restricted to the transition-statistics layer. But it does not pick out what is distinctive about the regime: as the writer notes, the restriction holds at every value of 𝒩. "Partial-revival regime" would describe it better. The one risk is that "restricted" implies an unrestricted regime elsewhere, and the anchor's disclaimer already rules that out. The owner's choice should stand.

### 3. Table removal and the surviving prose (ch18 :80)
- **Fast-bath lemma: correct.** Main's lemma assumes τB ≪ τS with uniform erosion, and the prose's "fast bath that erodes the stored record uniformly" carries both. Dropping the "memoryless at ∼1" row is correct.
- **Static-bath coin: correct.** Main §2.3 gives zero memory at every horizon for the coin. No revival also follows from Main: a law with no gap is Markov, hence P-divisible.
- **Candidate systems: correctly labelled** as the proposal's conjecture.
- **Optional (ch18 :80, "The timescale ratio τS/τB does not place a system on the revival scale"):** write "does not by itself place". ch15 :190/:204 give the proposal's 𝒩 an explicit (1 − τS/τB) factor. Row E also shows a static bath with readback has memory and R = 1 on {0..3}, against R = 0 for the coin.

### 4. The writer's additions
None of them is scope creep: they are §A.25 propagation of the same vocabulary, or corrections the report's own text needed.
- **ch13 :172:** needed and correct. It is the same "density-matrix structure" diagnostic as B1/B3.
- **"C3 marginality" → "marginal hidden capacity"** (ch15 :146, :220; appendix-c :277; ch01 :263): needed, since r = N_H/N_V is not Main's C3 quantity. Correct.
- **appendix-a :170:** needed and correct.
- **ch09 :283:** needed. Optional: "is satisfied with a finite hidden capacity in … biological partitions" turns the old "can be" into an assertion; restore "can be satisfied".
- **E4 (N_H/N_V ∼1–10 → ∼1):** correct. F(1) = 1, so partial revival on the proposal's own form needs r < 1. It now matches :160 and :246.
- **E7:** correct and needed. The report's "approaching unity from above" is where F = 1, so that text would have been false.
- **ch15 :197, :208:** correct in direction (P-indivisible does not imply revival).
- **ch15 :144 inline argument: sound, and it carries the claim.** An idle register with a product prior leaves the visible law and Γ_t unchanged, while log₂|C_H| (and so the C3 margin and r) grows without limit. Rows C (M = 2, 8) confirm R = 0 with memory on {0..2}. It is better than the Main citation it replaces, which Main does not state for capacity.
  - Optional: "A capacity margin does not produce revival" → "does not by itself produce revival". The example refutes sufficiency only.

### Required findings
- **R1. ch15 :154, :184 (and :152): "complete revival" is used for F(r) = 1.**
  - **Problem:** §18.3 defines complete revival as 𝒩 = 1. But :186–:190 give 𝒩 = 𝒩_max·F·(1 − τS/τB), with 𝒩_max *measured*. So F = 1 is complete revival only if 𝒩_max = 1.
  - **Consequence:** :184 places the regime at F < 1 while §18.3 places it at 0 < 𝒩 < 1. Two incompatible definitions now carry the unit's own vocabulary.
  - **Fix:** use "saturated revival, 𝒩 = 𝒩_max" for F = 1, and describe the regime at :184 as the proposal's sub-saturated case F < 1. Or reconcile the two definitions explicitly. Mirror in FULL :4115, :4145. (This text came from the report's E8/E10.)
- **R2. ch15 :210 ("shows a revival, which certifies P-indivisibility") and :197 ("For dynamics with 𝒩 > 0, this should be non-monotonic").**
  - **Problem:** a revival of the density autocorrelation G² is not a distinguishability revival.
  - **Counterexample (exact):** the time-homogeneous Markov chain T = [[1/10, 9/10], [9/10, 1/10]] is P-divisible with d_t = (4/5)^t, so 𝒩 = 0. Its G² is 2, 1/5, 41/25, 61/125, … — non-monotone.
  - **Fix:** drop "which certifies P-indivisibility". Tie the G² step to the proposal, or to the trace-distance observable at :168. Mirror FULL :4171.
- **R3. ch09 :285 ("when N_H/N_V is finite, it predicts partial distinguishability revival").**
  - **Problem:** this contradicts the E4 narrowing to ∼1 and ch09 :283's own "where that capacity is marginal". On F(r), a finite r ≫ 1 gives F → 1.
  - **Fix:** use "marginal (N_H/N_V ∼ 1)". Mirror FULL :2765.
- **R4. §A.42: the record's numbers have no support on main.** The record on the SC22-N-regime-fix path cites rows B, C and E, the monotonicity of F(r), the cumulative 2/3…20/3, and "matches its committed .out". All of these rest on scripts held only at `42bbd33c`, which is not reachable from main.
  - **Minimal set:** `regime_exact.py` + `.out`, and `blp_unbounded.py` + `.out` (it imports `regime_exact`).
  - **Conditional additions:** add `enum_window.py` + `.out` only if the record keeps naming it; it quotes no number from it. Add `proposals.py` only if "56 old strings re-verified unique" stays as a claim rather than provenance.
  - **Placement:** land them byte-identical at the audit track path `tracks/SC22-N-regime/`, so the audit branch's later landing does not conflict. Not in the frozen evidence-retention archive.
  - **Alternative:** move the numbers to the PR description, or leave the record off main as SC-24 to SC-27 did. No book claim depends on the probes; the prose rests on Main alone.

### Optional findings
- **ch18 :72:** "the the coherent operational lift". The typo predates the unit but sits on a line it edited.
- **ch13 :134:** "Partial revival … quantified by the Breuer–Laine–Piilo measure". By the unit's own definition, partial revival is a range of the peak measure. Write "revival … quantified in the literature by BLP".
- **ch13 :138:** "a conjecture that the capacity ratio does not fix" understates the problem. On the proposal's own F(r), capacities of 10^30 to 10^200 give F → 1, which works against the conjecture. Also, a capacity is compared there with a ratio N_H/N_V.
- **Guard coverage:** label-specific patterns in `architecture_check.py` (e.g. "partially-quantum theorems") no longer cover the new label. That is a follow-up, not this unit.

### 6. The writer's "needs the owner" list
- **(2) ch01 :225 and appendix-c :62.** Leave them to their owning units, but track them. Now that the glossary entry is renamed, both use a term that is no longer defined, and appendix-c :62 points at the old §18.3 name.
  - A purely mechanical relabel would itself assert something new. At ch01 :225 it would make decoherence a transition from a *capacity-revival* regime toward C2 failure.
  - The owning unit should relabel when it rewrites those lines.
- **(3)/(7) The algebraic-predictions family.** Split it:
  - **ch18 :86** ("A density-matrix description requires specific algebraic constraints … the proposal predicts … violate"): I would treat this as required in this unit. The unit edited that sentence, and it now contradicts the new anchor at :74 ("every finite law at every 𝒩 admits the quantum representation") in the same section. The minimal fix is "A memoryless (divisible) density-matrix description requires…", the wording ch13 :144 already uses. The owner has to decide this, because the report did not assign it.
  - **ch13 :136:** self-hedged ("not about whether a dilation exists"); leave it.
  - **ch13 :142, :146, :170:** "specific algebraic predictions" that are stated nowhere. Send these to a follow-up unit.
- **(4) 𝒩 symbol collision (SM §7.2, ch06 :179).** Leave it. Each use is defined locally, chapters apart, and renaming would touch many sites. Low priority; a 𝒩_W subscript in the book could be considered later.

### Scratch-space note
My probe copies went into a scratch folder that already held another agent's earlier outputs from about 11:58. None of their names collided with mine, and the copies I wrote are byte-identical to the audit-branch blobs. Nothing in the repository was affected.
