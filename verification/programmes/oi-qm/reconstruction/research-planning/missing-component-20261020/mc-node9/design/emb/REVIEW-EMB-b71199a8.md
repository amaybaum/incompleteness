*Redaction (on committing this review to `design/emb/`): one absolute path, the reviewer's session scratchpad directory path in the system temporary directory, is replaced by the descriptive reference "the reviewer's session scratchpad directory `revemb/`" (§Reviewer artifacts). No other change.*

# Review: node 9 embedded-observer follow-up (EMB) at `b71199a8`

Reviewed: `mc-node9/design/emb/` at `b71199a86eeb8e600905c369c89731de3c43d05a` (draft PR #885), from a fresh detached worktree. I did not use git for anything but reading. Below, `EMB` means `EMB-REPORT.md` and line numbers are that file's. Arithmetic is exact F₂ bitmask throughout. My own checks use an engine I wrote separately, `indep.py`. It imports nothing from the reviewed scripts, simulates states directly from the update equations, and has its own rank code. The one shared piece is `iso_graphs`, which I used only to enumerate graph representatives. The local compute stayed bounded: about 9 min of replays, plus under 30 s for my own checks.

## Disposition: **REVISE** (four blocking findings; each needs a text or rerun correction, no new research)

L1 is correct and the main witnesses hold. Four things need correcting before acceptance:
- one verdict cell applies L1 outside its hypotheses (F1);
- one reported result is an artifact of a script bug (F2);
- the headline "budget" reading names the wrong resource (F3);
- one NEW classification restates something C-i already recorded (F4).

## Status of the lemmas

| lemma | status |
|---|---|
| **L1** (one-pair lemma) | **Proof: correct and complete** in substance. Its presentation needs two one-line additions (F5). Every hypothesis is used, and two of them are each load-bearing: one read-out pair, and one clean pair (F3). |
| **L2**, capacity m ≤ r | **Theorem**, by a one-line rank argument. The report does not write it out. |
| **L2**, r = m non-degeneracy | **Correct necessary condition, but no derivation in the report**: B and B\* are undefined (EMB l.108). I reconstructed a proof (F6) and checked it exactly in all 734 learnt r = m cases at n ≤ 6, with 0 failures. Sufficiency is not claimed; that m ≥ 2 "can hold" rests on the witnesses. |
| **L2**, counts | **Exhaustive observations at n ≤ 6.** My own algebra reproduces every count. The r = 1 row is also a corollary of L1 plus capacity. |
| **L3** | A trivially correct identity: ω(f, g′) = 0 and ω(g, g′) = 1. Classifying it as CONFIRMING is right. |

## Findings

### F1 (blocking): the E2 Q-forget cell applies L1 outside its hypotheses, and W-E2 contradicts it

At EMB l.15 the E2 Q-forget cell reads "Same as E1 … L1 applies unchanged". But L1 explicitly excludes "more than one visible site" (l.105), and E2 by definition adds visible sites (l.36).

The reading "condition only on the pointer" fails too. L1 also needs the clean span K to be a single pair, and in E2 K has dimension ≥ 4.

Direct counter-evidence (`witness_check.out`): in W-E2 the **pointer site's cells alone** give toy support 1 at t = 4 and t = 12, with prior 4. In E2 the pointer apparatus therefore does not forget.

Replacement for the E2 Q-forget cell:
> Under H1, E2 is not a separate regime: it is E1 with |R| ≥ 2. L1 does not apply, since it needs a single visible site and a single clean pair. With two clean visible sites the apparatus does not forget. In W-E2 the pointer site's cells alone give a point mass at t = 4 and t = 12, with prior 4.

### F2 (blocking): every FULL `persist` result is a variable-reuse artifact

`e12_exhaustive.py:131` sets `T0` to the toy's initial functionals, and l.145 tests `persist` against `T0`. But at the first learning time, l.175 overwrites `T0` with the B0-background toy rows. Every later `persist` test in that case then checks the wrong functional.

I renamed that one variable, so lines 175–176 use `Tb` (`patched/e12_patched_n6.out`), and reran n ≤ 6. Results:
- Every FULL `persist` count is **0**, in every |R| and every n ≤ 6. My independent recount over all labelled graphs at n ≤ 5 (`persist_check.py`) agrees: FULL total 0.
- The named "first FULL instance", n = 5, edges (0,1),(0,3),(0,4),(1,2), R = (2,3), toy 1, t = 3, has initial-toy support 2 at t = 3. It is not an instance.
- U and V counts change too, which is why U ≠ V in the published file:
  - n = 5: 112 → 114 (|R| = 2) and 221 → 232 (|R| = 3);
  - n = 6: 643 → 645 (|R| = 2);
  - n = 6, |R| = 3: U 1683 / V 1679 → 1733 for both;
  - n = 6, |R| = 4: U 1671 / V 1653 → 1709 for both.
- NONE counts are unchanged.
- No other field changes: `learn`, `minF`, `minH`, `dist:*` and the controls are identical.

Affected text: the `persist` column of the table at EMB l.126–136 (31, 111, 1272, 603), and footnote ¹ at l.138 ("The displayed lattice does supply it; the first FULL instance is at n = 5, |R| = 2, t = 3"). Replacement for the footnote:
> ¹ `persist`: at some t, the current visible cells determine the toy's initial state while its current state keeps support ≥ 2. Under FULL this never occurs at n ≤ 6. Under NONE, U and V it occurs from n = 2, |R| = 1.

Fix the script, rerun, and replace the column, or drop it. The L0 bullet at l.89 concerns NONE and is unaffected.

### F3 (blocking): the restriction is not a clean budget, and not only a memory budget

This finding concerns EMB l.18, l.20, l.215–217 (H2) and l.227. L1's proof uses two separate hypotheses:
- dim W_V = 2: one read-out pair;
- dim K = 2: one clean pair.

It never uses that they belong to the same site. Relaxing either hypothesis alone lifts the restriction:
- **One clean pair, two visible sites** (`l1_attack.py` [5]). Take R = {a FULL, b NONE}, with b visible but uniformly unknown at t = 0.
  - Learning occurs at n = 3, 4, 5: in 9, 96 and 1650 (labelled graph, R, toy) cases.
  - First instance: the star with centre 0, R = {0 FULL, 1 NONE}, toy 2, t = 2. The toy's state is then (u₁⁽⁰⁾, q), fully determined by the visible cells (u₀, v₀, u₁, v₁) = (v₁⁽⁰⁾ + q, u₁⁽⁰⁾ + p, p, v₁⁽⁰⁾), with prior 4. The forward state simulation confirms it.
  - "a U, b U" (two clean bits in total) also learns.
- **One read-out pair, two clean pairs.** This is W-E2 read at the pointer only (F1).

So H2's "The clean budget is the operative resource … A model that withholds clean visible pairs changes the answer" is false as stated. Withholding the second clean pair while keeping a second visible site does not restore the restriction.

What does hold, by the rank count in F6, is a pair of necessary conditions: at least 2m clean coordinates, and at least m read-out pairs. L1 rules out the boundary case of one read-out pair and one clean pair for m = 1.

Replacement for l.18:
> Within these bounds, the restriction is the case of one read-out pair with one clean pair (L1). Adding a second visible site, even one with no clean coordinate, or a second clean visible pair, even if only the pointer is read, lifts it. Two clean visible sites determine the toy completely from the current visible cells alone, on fixed graphs with no external choices.

Replace the last two sentences of H2 with:
> Both the number of clean coordinates and the number of visible pairs are operative. Complete learning of m target pairs needs at least 2m clean coordinates and at least m visible pairs. One visible pair with one clean pair never suffices (L1). One clean pair with two visible sites can (n = 3, t = 2).

### F4 (blocking for the classification line; the text is otherwise fine): the K-EXTHIST dependence is not NEW

EMB l.239 classes "the K-EXTHIST dependence of the C-i counterexample" as **NEW**. But C1-REPORT §9.1 (l.398–400) already states it: "The accumulated history is held by the interface (κ4 readout, records so far), not in any lattice cell … The waiting counterexample (C1.6) uses that history with no observer operation".

What EMB adds is the exact computation that the same apparatus without the history never reaches a point mass for L = 1..6. That is ELABORATING. For learning it is also a corollary of L1.

Replacement for l.239:
> Classification:
> - **NEW** within the programme, pending the literature gate (Step 4): L1, and the r = m form of L2. Epistemically restricted symplectic theories (Spekkens-type knowledge balance) should be checked before NEW stands.
> - **ELABORATING:** the K-EXTHIST dependence, which C-i §9.1 already records; EMB computes it exactly.
> - **CONFIRMING:** L3.

### F5 (non-blocking): L1 proof presentation (EMB l.91–99)

The proof is correct. I checked each line, including 1 = ω(g₁, g₂) = 1 + 1 + 1 + ω(k₁, k₂), which gives ω(k₁, k₂) = 0.

Four edits:
- (a) State the contradiction hypothesis. Open with: "Suppose the posterior support is 1. Then each toy functional lies in W_V + K: …"
- (b) Justify that both kᵢ are nonzero: "k₁ ≠ 0 since ω(φ₂, k₁) = 1, and k₂ ≠ 0 since ω(φ₁, k₂) = 1."
- (c) Justify that k₁ = k₂: "In the 2-dimensional symplectic space K, any two distinct nonzero vectors pair to 1."
- (d) Add a scope sentence: "The proof uses only that Φ is symplectic, that the read-out is one canonical pair of the image, that K is one hyperbolic pair, and that the prior support is 4. It does not use the lattice, or that the clean pair and the read-out are the same site. Each of the two one-pair hypotheses is necessary (see F3)."

"Every E3 word" holds: each gated step is M_S = [[L_S, I], [I, 0]] with L_S symmetric, so M_SᵀJM_S = J. An idle site maps (u, v) → (v, u), which is the L_S row-zero case. Self-loops (L_xx = 1) and multi-edges (an even multiplicity cancels over F₂) keep L symmetric, so L1 covers them.

R2 holds: with |R| = 1 the single site is all of the visible sector, and both of its functionals are conditioned on.

Break attempts, all exact, 0 violations (`l1_attack.py`):
- every symmetric L with self-loops at n ≤ 4, at every t in the period: 171,868 checks;
- 1,200 random E3 words with self-loops and multi-edges at n = 3–6, depth 40: 168,000 checks;
- 2,000 random symplectic maps (products of transvections) at n = 2–6, with the clean site and the read site chosen independently: 28,000 checks.

A non-symplectic bijective countercontrol breaks the bound (support 4 → 1). So symplecticity is load-bearing, and the attack harness can go red.

### F6 (non-blocking): give L2 its derivation (EMB l.106–113)

Proposed text:
> **Capacity.** Rows F (2r of them) and T (2m) of the invertible Φ are independent. Complete learning means T_u ⊆ span F_u. The span of F ∪ T then meets span K (the vectors with zero unknown part) in dimension ≥ 2m. Hence 2m ≤ dim K = 2r, and m ≤ rank F_u ≤ r.
>
> **r = m.** Write g = ψg + κg with ψg ∈ W_V and κg ∈ K. Full prior makes ψ injective, hence bijective onto W_V. Orthogonality ω(W_V, W_T) = 0 gives ω(ψh, κg) = ω(ψh, ψg). Since W_V is non-degenerate, κ is injective, hence bijective onto K. Expanding ω(g, g′) gives ω(κg, κg′) = ω(g, g′) + ω(ψg, ψg′) = ω(g, (I + ψ†ψ)g′), where ψ† is the symplectic adjoint. K is non-degenerate, so I + ψ†ψ must be invertible. For m = 1, ψ†ψ = det ψ · I = I, so the condition fails, which is L1.

This is stated for FULL: K is the clean span of the same r sites. As F3 shows, with a different number of clean coordinates the binding constraints differ.

Counts (`l2_check.py`, own algebra), matching `mtarget_n6.out` exactly:
- r = 1: 0 learnt for m = 1..5;
- r = 2: 1061 (m = 1), 140 (m = 2), 0 (m = 3, 4);
- r = 3: 5026, 2913, 594;
- r = 4: 3374, 1210;
- r = 5: 628.

The identity, together with non-degeneracy, held in all 734 = 140 + 594 learnt r = m cases.

### F7 (non-blocking): what W-E2 knows, and the "copying" claim (EMB l.20, l.146, l.170–179)

I confirmed W-E2 independently by forward state simulation:
- period 16;
- support given all visible cells: 2 2 2 **1** 2 2 2 4 2 2 2 **1** 2 2 2 (t = 1..15), with prior 4 throughout;
- this is learning in the report's sense, not overwrite.

Three facts the report should state, because they change how the witness reads:
- (i) **The memory site alone carries no information about the current toy at any t** (support 4 at all t = 1..16), and **the pointer alone gives the point mass**. The second site acts as a second clean supply. It does not store the current state.
- (ii) **None of the toy's own content remains in its current state**: own-content rank 0 at both learning times. At t = 4 the toy is (v₃ + v₄ + u₂, u₃ + u₄ + v₂): the bath's bright mode plus the memory site's clean pair. What is known is a bath mode that both toy and pointer received. The toy's initial state is also recoverable at t = 4, from pointer plus memory.
- (iii) The non-copying background removes the pointer–memory edge, which isolates the second clean pair. So the background comparison shows that coupling in the second clean pair matters, not that copying does.

Replace the last sentence of l.179 with:
> Coupling the second clean pair into the dynamics, not the mere passage of time, makes the current state learnable. The memory site's cells alone never carry information on the current toy (support 4 at every t). The toy's current content at t = 4 and t = 12 is the bath's bright mode plus a known displacement, and the pointer holds the same mode.

Q-build, read literally, stands. Witnesses that keep the toy's own content also exist:
- the n = 3 witness, where the toy at t = 2 equals its initial state and each visible site holds a copy;
- with a hidden bath, for example n = 4, path 3–0–1–2, R = {2, 3}, t = 2, with own-content rank 2;
- with a single apparatus (exactly one visible site touching the hidden sector) and a bath: n ≤ 6 gives 50 cases. 6 of them never retain any own content (W-E2 is one); the rest retain rank 1 (19) or rank 2 (25) (`single_app.py`).

I suggest the report cite a single-apparatus case with own-content rank 2 beside W-E2.

### F8 (non-blocking): E2 is vacuous under H1 and should be presented that way (EMB l.15, l.36, l.212–214)

The E2 → E1 reduction is correct. With a linear update, the clean values enter every cell as a known affine shift M^t(c − c′). So the posterior support is independent of the "program", and the set of reachable Φ stays {M^t}. A linear embedded controller cannot reproduce E3's gating.

H1 states this candidly. But the verdict table still presents E2 as a regime with its own verdicts, and calls W-E2 "itself an E2 arrangement". W-E2 is E1 with |R| = 2: no site acts as a controller, and per F7 no site acts as memory of the current state.

The claim "smaller E2 witnesses from n = 3" (l.15) is numerically correct, and I confirmed it:
- the path visible–toy–visible learns at t = 2 and t = 6;
- n = 2 is impossible by L1;
- t = 1 gives support 2.

But that case is two pointers, not apparatus plus memory. The "E2" label adds nothing to it.

Proposed table change: merge the E2 row into E1, as "|R| ≥ 2 (pointer plus further clean visible sites)". Add: "A controller inside the linear lattice is vacuous (H1); conditional control inside the lattice would need a nonlinear update, which was not searched."

### F9 (non-blocking): missing hidden assumptions (§6)

- **H9 (building).** "Building an apparatus" here means an external, design-time choice of graph, region and clean supply. No process inside the dynamics constructs it, so the Q-build verdicts are existence statements over fixed arrangements. Add this, and qualify l.20's "an observer who builds one more memory site".
- **H10 (learning definition).** "Learning" means prior 4 at the evaluation time. That definition puts replacement by a mode the pointer shares (W-E2) in the same class as knowing the toy's own content (F7). It also says nothing about partial gains when the prior is 2.
- **H11 (resource status of FULL).** FULL is the clean-visible-site resource that C-i declared (C1-REPORT l.41: "clean visible pointer site (Q and Q̄)"). The corpus does not derive it. PREREG §4's draft declaration supplies only the pointer coordinates clean, and makes it an open postulate that pointer conjugates are never clean. Under the region partition a site's conjugate is visible, so supplying several FULL sites is a model declaration that every Q-build witness depends on: W-E3 uses 4 clean pairs.
- H4 already covers knowledge of t. Note there that every verdict of the form "some t" is realized only by an observer who stops at that t.
- H6 should note that L1 needs the read-out to be a whole canonical pair, i.e. the site-level partition. The owner's coordinate-level form, Q visible with P hidden, is not covered.

### F10 (non-blocking): controls labelled as controls but implied by the engine (EMB l.78–80)

- **NONE** (posterior = prior) and **CAP** follow from Φ being invertible: rows F and T are disjoint rows of a basis.
- **SYMP** is L3's algebra, which follows from symplecticity.

These three can fail only if the engine is broken. They are consistency identities, not controls on the verdicts (AGENTS: a control that "merely reproduces the claimed formula").

The controls that bear on the verdicts are:
- the `check_core` brute force;
- E1-K2 and E1-C1;
- the K-EXTHIST replay;
- the W4 green/red split.

All are green, and I reproduced them.

`check_core` is independent of the support formula: it enumerates explicit states and groups them by observation. It does share `f2.lattice_update` and `f2.apply` with the formula path, and it covers only t ≤ 6 and n ≤ 4. My equation-level simulation (`indep.step_state`) and my own-algebra recounts agree with it, which covers the shared-matrix gap.

The counts 92,424 cases with 0 mismatches, and 1, 2, 4, 11, 34, 156 isomorphism classes, are reproduced byte for byte.

Relabel NONE, CAP and SYMP as "engine identities".

### F11 (non-blocking): smaller wording points

- **E1-K2 (l.61).** All three point masses are overwrite. My state simulation gives the toy's prior at t = 2, 3, 4 as 2, 1, 2. The report mentions only t = 2. Say "at t = 2, 3, 4 the prior is 2, 1, 2."
- **l.193.** "Retention costs one fresh clean memory pair per read" is observed in one witness, and minimality is not shown. Write "In W-E3, each retained read uses one fresh clean memory pair."
- **"Not a barrier to accumulating records" (l.18, l.227).**
  - In E1 the knowledge is transient: W-E2 reaches support 1 at 2 of 15 stopping times.
  - Accumulation of retained records is shown only in E3 (W-E3), under external gating, which is AP-2.
  - Say this explicitly.
- **l.194.** "With full history it behaves as the owner's REC model does" is an analogy that was not checked. Drop it, or compute it.
- **l.115.** "(requirement 5)" names nothing in the repository; quote the owner's requirement or remove the reference. "Provides no restriction" is an interpretation; scope it as "within this lattice, under FULL".
- **l.10.** "C5 needs Q-build" should carry its source, the owner on 2026-10-21, or be stated as the report's own framing.
- **Base.** The report says its base is `231ec13c`, but the commit's parent is `49033a3e`. I checked that `c1/f2.py` and `c1/lifecycle.out` are identical in both, so this is harmless. State it in one clause.
- **Replay recipe.** `e12_exhaustive_n6.out` contains an `[elapsed … s]` line, so a replay is byte-identical except for that line: mine printed 108 s, the published file 107 s. `e3_gating.out` captures stderr. Give the recipe as `python3 e3_gating.py > e3_gating.out 2>&1`.

### What I checked and found correct (no change needed)

- **No M0–M5 verdict and no claim about OI in general.** l.3 disclaims both, and nothing contradicts that. H1 cites Main.md l.320's scope correctly. The Main.md l.290 and l.292 citations are accurate.
- **E1 Q-forget (|R| = 1, FULL, learning sense).** Proved by L1.
- **E1 Q-forget (U/V, no point mass at all).** Correctly marked as computational, at n ≤ 6.
- **E1-C1.** Period 8 (M⁸ = I on all 16 states); minimum support 4 2 2 4 4 4 2 2; the six two-point preparations give support 2 throughout. Reproduced both by the script replay and by my equation-level simulation.
- **K-EXTHIST replay.** The sequences equal `c1/lifecycle.out` exactly:
  - L = 1..5 with reset;
  - L = 1 without reset, 2 2 2 1 1 1 1 1.
  With embedded memory only, the minimum support is 2 for L = 1..6.
- **W-E3** (confirmed by state simulation, `witness_check.out`):
  - support given all visible cells: 2 × 9, then 1 1 1 1 at t = 10..13;
  - memory sites alone: 1 from t = 10;
  - prior 4 throughout;
  - final toy (q + u₅, p), so the toy's own content is retained: genuine learning;
  - stores idle: support 2 throughout, while K-EXTHIST still reaches 1 at t = 10. The W4 control is therefore green and the embedded copy is what moves the record;
  - fresh bath per read: 2 throughout, K-EXTHIST included, so red. The report correctly draws no verdict there.
- **The 12-element group claim.** Correct as worded: the exact site exchange lies in the group, but only at odd lengths (EEE, OOEEE, …), so no even-length exchange exists.
- **E3 arenas.** Depths and product counts are as stated, and K₄ depth 5 is correctly reported as not completed.
- **Table values other than `persist`.** At EMB l.128–136, every case, point-mass, learning and with-bath count matches the output. The single-apparatus learning totals (17 at n = 5, 131 at n = 6) match my own recount.

## Replay results

All replays ran from a copy of the committed scripts in `revemb/replay/`.

| script | result |
|---|---|
| `check_core.py` | byte-identical |
| `e1_controls.py` | byte-identical |
| `e2_families.py` | byte-identical |
| `e3_w4.py` | byte-identical |
| `mtarget.py 6` | byte-identical |
| `e12_exhaustive.py 6` | identical except the `[elapsed]` line (108 s vs 107 s); 1 min 48 s |
| `e3_gating.py` | stdout lines 1–87 byte-identical; with stderr appended and the path redacted, sha256 `10727e23…` equals the published file; 6 min 17 s |

- **SHA256SUMS:** all 18 entries OK. EMB-REPORT.md is not listed, which is fine.
- **Redaction.** The coordinator's unredacted original is still in the session scratchpad, at `scratchpad/emb/e3_gating.out`; I read it and did not modify it. Its sha256 is `012365ff…d8cd8`, exactly the hash the publication note states. It differs from the published copy only in the two traceback path lines. The redacted path was a session scratchpad path. Every other file in that directory is byte-identical to the committed file.

## Reviewer artifacts (scratch, not for the repo)

All in the reviewer's session scratchpad directory `revemb/`:
- `indep.py`
- `l1_attack.py`
- `witness_check.py` and `witness_check.out`
- `persist_check.py`
- `content_check.py`
- `single_app.py`
- `l2_check.py`
- `misc_check.py`
- `patched/e12_patched_n6.out`
- `replay/`
