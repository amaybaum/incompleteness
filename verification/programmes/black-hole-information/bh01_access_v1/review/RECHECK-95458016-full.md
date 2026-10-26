ACCEPT WITH NITS — 954580165a7a1ea9fd58812afc1f23cf71e9af70 (re-check of the fixes for the review of 587d419657404411cc662112829bcf50a32abd9f). Overall verdict on faf9028080b394ed1910e9d85ba9336006983946..954580165a7a1ea9fd58812afc1f23cf71e9af70: ACCEPT WITH NITS. The package is exploratory research with no manuscript change. All of its computations reproduce, item F is confirmed, and every blocking finding is resolved.

Reviewer: independent, read-only. Scratch outputs are in this directory:
- `recheck_indep.py` / `recheck_indep-output.txt`: my own enumeration in both encodings, plus K7.
- `leafdiff.py`: leaf-level diff of result.json.
- `replay/`: logs of the recipe replay and the mutants run.
- `x/`: exported copies of the package files.

The clone worktree was not modified: `git status` is empty, and HEAD is 95458016 before and after.

## Commit shape

- 95458016 has a single parent, 587d4196.
- PLAN.md is byte-identical (blob d8326165, unchanged since faf90280).
- The diff touches only `bh01_access_v1/`: 8 files, and no path outside the package.
- The commit is local. It still has to be pushed to the guiding PR (§A.43).

## Status of each finding from the review of 587d4196

| finding | status | evidence |
|---|---|---|
| F1 necessary vs sufficient | **resolved, accurately** | see below |
| F2 missed sites | **resolved** | see below |
| F3 L155 falsifier | **resolved** | see below |
| F4 claim A qualifier | **resolved** | see below |
| F5 overall label | **resolved** | see below |
| F6 L12/L139 strength | **resolved** | both now read "not supported by bijectivity alone"; the key defines the class |
| F7 item F unguarded | **resolved** | see below |
| F8 C1 count mix | **resolved** | generated text: "25824 … with one mode unread and 3904 with D unread"; total 29728 in result.json |
| F9 "49 models" | **resolved** | "three parametric families (swap 30, wide-alphabet swap 8, CNOT 10 settings) and the GL(4,2) scramble class, 49 items" |
| F10 E as identity | **resolved** | claim E is stated as a Fubini identity for every map, in the proofs, the generated text and the audit |
| F11 vacuous `nondecreasing()` | **resolved** | K8 control plus its mutant, which is caught |
| F12 GR observations | **resolved** | labelled "reviewer observations on GR; not claims of this package"; line refs L819, L821 and L771 are correct at 809fac52 |
| exit-144 incident | recorded | PROVENANCE `execution_incidents` |

### F1: necessary vs sufficient

- R1–R4 are now "Endpoint guarantees (sufficient, not necessary)". The report adds "They are not necessary: the enumeration also exhibits exact recovery when they fail", with the diagnostic counts.
- R1 is now a real condition: K is empty, or has fewer than |M| values.
- The contrapositive of C2 is stated as the one necessary-side fact.
- C3 is restated and proved under W-autonomy, F_t(w,d) = (G_t(w), H_t(w,d)). It states "The converse is false". The proof remains correct, and the bijectivity of G_t follows as stated.
- The pressure test now reads: "bijectivity plus R1–R4 suffices, and … bijectivity alone does not".
- The audit's class is re-keyed to "holds under unstated conditions", with "R1–R4 are sufficient guarantees, not necessary conditions".
- No "only under" or "only when" survives in REPORT.md or MANUSCRIPT-AUDIT.md.

### F2: missed sites

ch09 L108/FULL L2580, ch09 L127/FULL L2599, ch18 L130/FULL L4942, ch18 L158/FULL L4970 and ch19 L334/FULL L5502 have all been added. Each quote is verbatim at 809fac52, and each chapter line is byte-identical to its FULL mirror. The proposed ch19 L334 cell, "Conditional (H-scramble)", fits the table's own idiom; compare the row "Conditional ($a_0 = cH/6$)" two lines above it.

### F3: the L155 falsifier

The proposal is withdrawn. The sentence is diagnosed as "unfalsifiable as stated", with both reasons given: claim A, and nested-trace consistency holding for every map (claim E). The audit explains why C1 cannot supply a physical falsifier, citing item F. The wording is left to the Page lane.

### F4: claim A qualifier

- REPORT.md now reads "Zero accessible advantage … requires the inaccessible endpoint set to have at least |M| joint values", with the C2 argument.
- The audit's L12 entry has the same qualifier.
- REPORT.md acknowledges that PLAN.md states claim A without it.

### F5: overall label

- The generated text now opens: "Preregistered hypotheses: all confirmed in the tested finite classes … this is not a verdict on the framework's resolution of the paradox".
- It includes a headline line, and each claim carries its programme tag.
- result.json gains `overall_scope_note`.
- The `HOLDS_WITHIN_SCOPE` token itself is kept, for PLAN compatibility, and is explained above the generated block.

### F7: item F unguarded

- New control K7 checks a reference value and cubic mass scaling.
- The M² mutant is now caught.
- π is bounded by 333/106 and 355/113.
- Upper bounds are rounded up. The rewritten `sci(up=True)` takes a ceiling and handles the carry.
- A Page-time bound is added. The step (354/1000)² ≥ 1/8, giving 1 − 2^{-3/2} ≥ 0.646, is correct.
- The "shows / does not show" statement is present.

## Independent re-derivations

**C3 under W-autonomy: 384 maps, 336 not products.** My own code (`recheck_indep.py`) gives the same counts in the author's encoding (index = V + 2B + 4D) and in mine (4V + 2B + D):

| quantity | count |
|---|---|
| W-autonomous bijections | 384 |
| of which products | 48 |
| of which not products | 336 |
| W-autonomous bijections that fail to recover | 0 |
| bijections recovering with D never read | 36416 |
| of those, not products | 36368 |
| of those, with a W-update that depends on D | 36032 |

The analytic count 384 = 24 · 2⁴ is right: a bijection G of W, then for each of the four w a bijection of the 1-bit D.

**The example [0,1,2,3,4,5,7,6], author's encoding.**
- It swaps states 6 = (V=0, B=1, D=1) and 7 = (V=1, B=1, D=1). So it flips V exactly when B = D = 1, as the report states.
- My classifier returns: W-autonomous False, product False, recovers True. So it is a correct instance of "recovers exactly with a D-dependent W-update".
- The same list happens to be the W-autonomous example under my encoding, where D flips iff V∧B. The two readings differ only by encoding, and REPORT.md states its encoding explicitly.

**K7 reference value.**
- My bracket, computed independently: Γ = 1, 1 M_⊙, M taken from [1.9884, 1.9890]×10^30 kg, G² rather than (GM)³/G, and ħ = h/2π with the tighter π bounds. Result: [2.0952, 2.0976]×10^67 yr.
- The package's bracket, [2.095, 2.096]×10^67 yr with fixed GM_⊙, lies inside mine.
- Cubic scaling, lo(2M) = 8·lo(M), is an exact rational identity of `evap_time`.

**K7 tolerance.** The window [2.0, 2.2]×10^67 yr (about ±5%) is the right size. The external reference is the textbook value of the same Γ = 1 formula, quoted to two significant figures, so a tighter window would not be anchored. The window catches every structural error: exponent, the 5120/15360 prefactor, ħ↔h, the power of c, unit slips. It does not catch errors of a few percent, which cannot affect item F's margin of at least 10^57. Note that K7 validates the implementation, not the physical normalization of Γ. Γ is covered by the stated interval [1/100, 1000].

**Item F numbers.** The ratio [1.785e57, 1.786e65], crossover [1.059e10, 4.918e12] kg and t_P/τ_B^D ≥ 1.153e57 are consistent with my earlier bounds, which used wider constant intervals: [1.785e57, 1.787e65] and [1.059e10, 4.92e12].

## The new "contradicts" classifications

- **ch09 L108.** The parenthetical "(resolving the BH information paradox in Chapter 7 §7.6)" draws the resolution from bijectivity's information preservation alone. Unlike L12, this sentence carries no Page-curve leg. It is the same inference as ch07 L110 sentence 2, so under the key's definition "contradicts" is fair and consistent. "Not supported by bijectivity alone" would also be defensible, and more conservative. The proposal, "the information-preservation half …" or removing the parenthetical, is sound.
- **ch18 L158.** "(which it does, through the nested partition)" credits the nested partition with radiation-level preservation. Claim E shows that nested-trace consistency is an identity for every map, including the 2688 zero-advantage bijections. So "contradicts" fairly targets the mechanism. The bare claim that Hawking radiation preserves substratum information is unsupported rather than refuted; the entry's wording ("attributes … to the nested partition") already scopes it that way.

## No new overclaim

- The re-grep of REPORT.md and MANUSCRIPT-AUDIT.md finds no "only under" or "only when".
- The C3 converse is explicitly false.
- Necessity counts are reported as diagnostics, not verdicts.
- The F12 items are labelled as reviewer observations.
- Item F keeps its "does not show" list.

## result.json, leaf diff 587d4196 → 95458016 (`leafdiff.py`)

- **Removed:** only `claims/C1/countercontrol_without_complete_access_violations` (5280).
- **Added:**
  - programme tags;
  - the post-review diagnostics, with the counts above;
  - the C1 split (25824 / 3904, total 29728);
  - `MP1/not_exact_t2` 25824;
  - claim-B parameter settings;
  - the E note;
  - controls K7 and K8, all true;
  - item F `page_time_over_tau_lower_bound`, `printed_bounds` and `reference_value_1Msun_gamma1_yr`;
  - `overall_scope_note`.
- **Changed:**
  - `K1_maps_checked`, 60682 → 61018 (+336, the added W-autonomous G checks);
  - item F `pi_interval`, `t_evap_s_interval`, `ratio…` and `crossover…`;
  - `verdict_text`.
- **Unchanged:** every preregistered verdict, histogram and count. `overall` is still HOLDS_WITHIN_SCOPE, and the item F status is still "contradicted".

This matches the author's description. The REPORT.md generated block equals `verdict_text` exactly.

## Replay and hygiene

- **Recipe.** Run as written, from an empty directory, extracting files with `git show`.
- **Checksums.** `sha256sum -c` gives OK for all 8 files, before and after the runs.
- **`checks.py` (-B).** Exit 0. result.json is byte-identical to the committed file.
- **-B -O.** Byte-identical (`cmp`).
- **`mutants.py`.** Caught 12 of 12, exit 0. mutants-output.json is regenerated byte-identical, and the checksums still verify.
- **Scan.** No absolute paths, secrets, e-mail addresses or session paths in the package.
- **Repository tools.** `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py`, run read-only from the clone root, all print OK. The worktree was unchanged afterwards.

## Remaining nits (non-blocking)

1. **The W-autonomous check is not wired into the C3 verdict.** `C3w_violations` and `w_autonomous_not_recover` are measured (both 0) but not added to `c3_viol`, so a nonzero value would not change the C3 verdict. The C3 statement in REPORT.md is now the W-autonomous one. Either label these counts "post-review diagnostic, not verdict-bearing", or add a separate post-review verdict field. The preregistered verdict must stay the product-map check.
2. **ch19 L334's class label does not fit its reason.** It is classified "not supported by bijectivity alone", but the cell does not invoke bijectivity. The real issue is the status mismatch with ch19 L72, which the second bullet already gives. "Holds under unstated conditions (H-scramble)" fits better.
3. **The L12 proposal lists "the trans-cosmological sector decoupled" without a pointer to item F,** which removes that condition's stated support for astrophysical masses. Add the pointer.
4. **The assumption-watch mass fraction is loose.** "At most a fraction of order 10^-57 of its mass" is a valid upper bound, but the computed bound is ≈ 2×10^-58: mass loss ≈ t/(3 t_evap) with t/t_evap ≤ 5.6×10^-58. Optionally tighten.
5. **R3 is stronger than C1 and C2 need.** It asks for cumulative joint records, but the joint endpoint snapshot already suffices for both. This is harmless for a sufficient condition; the parenthetical already notes it.
6. **Push 95458016 to the guiding PR,** and record this re-check there (§A.43).
