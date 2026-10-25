ACCEPT WITH NITS — 200fcd9f9265e79167d33d20af62deb543a9a117 (a2_memory_v8, plan 1dfec979721336cc9f0ce703b544f9d6be8e906c, PR #911 head 49e1a1191c9ea5c303883afd2d8d3c28a233f9e5)

Independent, read-only review. The class theorem's proof is correct. Every finite number I re-derived matches.
Replay is byte-identical. Two findings should be fixed before anything cites the package:
- F1: the B=2,3 "memoryless reset" comparisons use a comparator that is not the nearest-dyadic reset, and
  the ordering they report reverses against the nearest-dyadic one.
- F2: the preregistration wording.
Neither finding touches the theorem, the census or the certified RS depths.

Reviewer files (relative to this directory): `indep.py` / `indep.out` (independent exact re-derivation),
`rev_mutants.py` / `rev_mutants.out` (16 reviewer mutants), `pow_probe.py`, `rs_exact_small.py`. Package files
were exported with `git show 200fcd9f:<path>` into `tree/`. All Python ran as `python3 -I -B` (3.13.16) from
empty work directories.

## Ranked findings

**F1 (medium; wording/comparator, post-plan content).** "The memoryless reset" at B=2,3 is RS(B,1), the
ceiling-rounded reset, with agreement ⌈4·2^B/5⌉/2^B: 1 at B=2 and 7/8 at B=3. That is not the nearest dyadic
to 4/5. The nearest is 3/4 at both B=2 and B=3 (distance 0.05, against 0.2 and 0.075). Against the nearest
dyadic, the 3/4 memoryless reset first exceeds T=1/2 at h=127 (exact, `indep.out`).
- B=2: every RS(2,k), k≤16, is certified above 1/2 by h≤48, so every member fails before the 3/4 reset.
  Exact first depths for k=2..5 are 7, 7, 9 and 11 (`rs_exact_small.py`).
- B=3: k=3..15 are certified above 1/2 by h≤120<127. k=2 (170) and k=16 (128) are undetermined. None
  outlasts the 3/4 reset.
- So REPORT's "B=2. Every k ≥ 2 outlasts the memoryless reset" and "B=3. k = 9..16 … outlast the memoryless
  reset" hold only for a suboptimal comparator. The same lists appear in the generated `family_verdict`.
- At B=4, 13/16 is the nearest dyadic, and that ordering claim is correct.
- Fix:
  - Add the nearest-dyadic (best i.i.d.) B-bit memoryless reset as the comparator, or restrict the
    comparison to B=4.
  - Rename RS(B,1) "the ceiling-rounded B-bit reset" wherever it is called "the memoryless reset".
  - Regenerate the verdict text.
  - Against the nearest-dyadic comparator, the RS family is worse than memoryless at all three B on the
    certified depths. That is consistent with the Bhattacharyya mechanism the REPORT describes.

**F2 (medium; preregistration record).**
- PLAN.md says "This plan is committed alone before any computation of this round". PROVENANCE and REPORT
  disclose a floating-point exploration that ran before the plan. The PLAN sentence is therefore inaccurate as
  committed.
- PROVENANCE and REPORT also call the explored object a "different candidate" and say the plan came "before
  any computation on the tested class". A floor-truncated rescaling decoder with a fixed-width register is a
  finite-state controller, so it is a member of the bounded-state class. It is not a member of the RS family.
  The exploration may have shaped hypothesis H and the choice of family.
- Bearing on the results: none on validity. The proof is checked on its merits, the census is exhaustive and
  has no free parameters, and the RS depths are exact certificates. It does bear on what counts as
  preregistered.
- Fix: leave the committed PLAN.md untouched. Add a correction in REPORT ("Departures") and PROVENANCE
  (`plan_commit_note`; the key name `plan_commit_before_computation` is also misleading). The correction
  should say:
  - that PLAN's "alone before any computation of this round" sentence is inaccurate;
  - whether the explored decoder had bounded state, and therefore lies in the class;
  - what it suggested, qualitatively;
  - that it touched neither RS(B,k), the census nor the decision rule.
- Preregistered: the class, H and its proof route, the census populations, K1–K8, RS(B,k) for B=2,3,4 and
  k=1..16, the nc/(1+nc) and min(nT_k, sqrt(2nc)) depth rules with their 1/2 and 1/10 thresholds, the memory
  bits, the VOID rule, and the verdict labels.
- Post-plan:
  - the power-rule depths;
  - the "T ≤ 1/2 for h ≤" threshold (the plan had 1/10);
  - the exact memoryless crossings 4/45/1819 and every before/outlast comparison;
  - the Le Cam checks and the trailing-run diagnostic;
  - the mechanism paragraph;
  - the changed K6 implementation, M9 and M10, and the runner fix.
- The generated `family_verdict` embeds the post-plan power-rule extremes and comparison lists. Label them
  post-plan inside the verdict, or move them out of it. Label the REPORT table's last column as power-rule /
  post-plan as well.

**F3 (low-medium; control coverage of the post-plan power rule).**
- Reviewer mutant R1 replaces T ≥ 1−BC^n with the invalid T ≥ 1−BC^(2n). It exits 0 with changed output:
  no control fails.
- The REPORT table's headline column, the verdict's largest/smallest h and the B=4 ordering all use this rule.
- I recomputed every power-rule depth at 320 bits with a separate engine, and all 48 members match. So the
  numbers stand, but the control is missing.
- `pow_probe.py` shows the invalid variant is violated by the exact memoryless TV at B=3 from h=149.
- Fix: in K7 at k=1, check exact T(h) ≥ 1−BC_upper^h for every h ≤ 2·n_hp (cheap with `tv_iid`). Add the
  power-rule bracket to the n·k ≤ 16 product loop.

**F4 (low; necessary→sufficient wording).** REPORT's "So growing state suffices on this protocol and bounded
state does not" and "The retained-seed reset's linear growth is sufficient" read as sufficiency of growth in
general.
- The theorem gives necessity only.
- Sufficiency is witnessed by one sampler, the retained-seed reset, which is granted the quantum cuts.
- Growing state alone does not suffice: v7's full-record memoryless controllers have growing state and
  T→1.
- Rephrase: "some controller with linearly growing private memory (the retained-seed reset, granted the target
  cuts) keeps T ≤ 1/(2^B−2)".
- The reachable-state formulation of the resource statement should also say "from a finite initial support".

**F5 (low; verbatim verdict).** REPORT introduces the verdicts as "generated from the measured values".
- Its class verdict differs from `result.json`: "(proof below)" against "(proof in REPORT.md)".
- Its family verdict is only the label plus "(details in the table below)".
- Fix: quote both verbatim, or mark them as abbreviated. Apart from that one parenthesis, the class verdict
  text matches `result.json` word for word.

**F6 (low; proof nit).** Step 3: under Q the overlapping windows of 1^n are not i.i.d. The frequency claim
follows from the strong law applied to each of the n residue subsequences, or from the ergodic theorem for the
Bernoulli shift. Say so.

**F7 (low; propagation, v7 attribution).** See check 5. Once the result is accepted, update the mutable
`CURRENT-HANDOFF.md` §"Depth extension". Its "Arbitrary depth is therefore open for controllers that carry
randomness across slots" is now partly answered. Leave the reviewed v7 REPORT unchanged (forward only).

**Nits.**
- (a) `solve()` raises StopIteration on a singular system. Reviewer mutant R4 (closedness test removed) exits
  1 with a traceback instead of a clean VOID.
- (b) The `result.json` K6 string says "RS(B,k>=h) equals the retained-seed reset", but the check is the
  unrestarted machine. That departure is disclosed; align the string.
- (c) The census counts and the memory column are not controlled: reviewer mutants R10 (one composition
  dropped) and R15 (record bits dropped) exit 0. Add closed-form checks: Σ_B(2^B+1)=518, C(5,3)²=100,
  C(7,3)²=1225, C(11,3)²=27225, C(7,5)³=9261. I verified both counts and memory independently.
- (d) The PLAN's computation 3 mentions "the two concrete class members of computation 1", but only one
  executed chain is reported.
- (e) K2's count of 43 includes the two K6 checks.

## Check 1 — preregistration integrity

- The plan commit 1dfec979 is a single-parent child of 49e1a119 and touches PLAN.md alone.
- The execution commit carries PLAN.md unchanged: both have SHA-256 b7f7eaae…a275, which matches PROVENANCE.
- The execution commit, 21 minutes after the plan, is consistent with a 72–84 s checker run.
- The disclosure is present in PROVENANCE and REPORT, but is incomplete as described in F2.
- Verdict: **nit-level defect in the record. Correct it in REPORT and PROVENANCE, not in PLAN.**

## Check 2 — the proof (verdict: correct, correctly scoped)

- Step 1: Z_t=(σ_t, o_t, t mod 2) is time-homogeneous from read 1. The initial law of Z_1 is arbitrary, which
  covers the unconstrained first read and non-dyadic initial laws. g_(t+1) is a function of (Z_t, Z_(t+1)).
  The entries of D_g are counts/2^B. ✓
- Step 2: TV of the marginals is nondecreasing and converges to TV on the generated σ-field. ✓
- Step 3: ν ≤ Q gives ν(F_n^c)=0, and ν ≤ P gives P(∩F_n) ≥ |ν| > 0. ✓ (F6 nit)
- Step 4: a finite chain enters a closed class a.s.
  - There are finitely many classes, so some class C has P(enter C ∩ ∩F_n) > 0.
  - On entering C, the ergodic theorem for the irreducible path chain on positive-probability (n+1)-paths in
    C applies from any start state and holds for periodic classes, since it concerns Cesàro averages.
  - All n are handled simultaneously by a countable intersection, so a_n(C)=π_C D_1^n 1=(4/5)^n for every n.
  - Closedness makes (D_1^n 1)|_C=(D_1|_C)^n 1. ✓
- Step 5: A=2^B D_1|_C has nonnegative integer entries, so χ is monic with integer coefficients.
  - Cayley–Hamilton gives Σ c_i π A^i 1=0 for any π, including a non-dyadic one.
  - π A^i 1=(2^B·4/5)^i=λ^i, so χ(λ)=0.
  - λ=2^(B+2)/5 is not an integer, which contradicts the rational root theorem. Hence T_∞=1 and T(h)→1, not
    merely T bounded away from 0. ✓
- The "mismatch at some n ≤ |C|" remark follows. The "(1/N)Z with 5∤N" remark follows.
- The uniformity remark is valid:
  - min(Σμ_z p_z, q) ≤ Σ_z min(p_z, q), so 1−T_μ ≤ Σ_z(1−T_z).
  - There are finitely many (rule, start) pairs for fixed |Σ| and B.
  - Only the existence of h* is claimed, and no rate.
- Scope is stated correctly: dyadic fresh randomness, finite whole state including any clock or record
  register read, a time-independent rule, and this protocol.
- The class boundary is stated correctly:
  - v7's class (no private memory, full-record dependence) and v8's class (finite whole state) are
    incomparable.
  - Bounded private memory with unbounded public state is correctly listed as not covered. The v7 argument
    fails there, because posterior mixing over private states makes the conditional laws non-dyadic.
  - The v8 argument fails there too, because the chain is infinite.

## Check 3 — exact finite checks (independent code: `indep.py`, different methods)

Methods: stationary laws by the Markov-chain tree theorem; χ by Faddeev–LeVerrier on the integer matrix, with
a Cayley–Hamilton identity check; RS blocks in absolute integer-seed coordinates; BC at 320 bits.

| item | result |
| --- | --- |
| census, all 12 populations | chains, closed classes, exact-4/5 classes and largest least mismatch all equal the author's (38,329 / 39,425 / 182 / 2); every exact-4/5 class mismatches at n=2 |
| base-5 control | 1/6 one-state chains and 209 classes among 3,136 two-state chains match; χ(4)=0 for each |
| memoryless crossings | exact first T>1/2 at 4 (agreement 1), 45 (7/8) and 1819 (13/16); also 127 for 3/4 (F1) |
| RS(B,k), all 48 members | block TV digests and displays, 1−BC lower, preregistered half and tenth depths, power-rule depths and memory bits all equal `result.json` (0 mismatches) |
| B=4 ordering | "fails before" holds for k=4..16 exactly; B=3 "outlasts" holds for k=9..16 (against 7/8) |
| product structure | own brute-force simulation equals the product of own block laws for (B,k,h) = (2,3,9), (2,4,10), (3,2,6), (4,2,5) |
| exact crossings, small RS | RS(2,2..5) exact crossings 7, 7, 9 and 11 lie inside the certified windows |

The memory accounting (k−1)B + (k−1) + ⌈log2 k⌉ is checked for all rows. It is a valid upper bound; the record
bits are redundant, since the record is a function of the seed.

## Check 4 — controls and mutants

- The author's runner reproduces `mutants/mutants.out` byte for byte; all 10 author mutants are caught.
- Reviewer mutants (`rev_mutants.out`) caught with VOID on a sensible control:
  - R2: run comparator shifted; caught by K5.
  - R3: λ off by one; caught by K4 χ(4)=0.
  - R5: K5 vacuous.
  - R6: cut 13/16; caught by K2.
  - R7 and R8: inflated c_low ×2 and ×1.2; caught by the K7 exact bracket.
  - R9: uniform π; caught by the stationary equation.
  - R11: K3 source 13/16; caught by K3.
  - R12: power-upper exponent; caught by K7.
  - R13: restart off by one; caught by K8.
  - R14: QUANTUM=3/4; caught by K1.
  - I1: tampered v7 input; caught by the pinned hash.
- Not caught: R1 (F3), R10 and R15 (nit c), and R4, which crashes instead of printing VOID (nit a).
- K1 hashes the raw bytes before `json.loads` (I1 and M9 confirm this).
- K3/K4 are genuine countercontrols. The same `class_analysis` code returns "no mismatch" and χ=0 when N=5,
  and M4 and R3 show the controls bite. K4 does not reproduce the claim: it exercises the opposite outcome
  through the same path.

## Check 5 — wording

- A1 and A2 are kept separate. Finite results are labelled finite.
- The theorem rests on the written proof, not on the census.
- The mechanism paragraph is limited to "measured for the RS family only", and the word NEW does not appear.
- Fixes needed: F1, F4 and F5.
- **The v7 attribution.** The author proposes to qualify v7's "resets that carry no randomness across slots"
  to "bounded persistent state with dyadic fresh randomness". That is correct as a qualification of *v8's*
  reach but wrong as a replacement attribution for v7:
  - v7's class allows full-record dependence, so its state is unbounded and the v8 theorem does not cover it.
  - v7's obstruction rests on the per-slot conditional agreement being dyadic.
- Suggested wording: "On this protocol the obstruction is arithmetic: dyadic fresh randomness against a run law
  with ratio 4/5. It holds for every reset that carries no private randomness across slots, whatever its record
  dependence (`a2_depth_v7/`), and for every controller with finite whole state (`a2_memory_v8/`). The
  retained-seed reset, whose private memory grows linearly and which is granted the target cuts, escapes it.
  Bounded private memory with unbounded public state is open."
- Put this in mutable dependents (CURRENT-HANDOFF, v8 REPORT), never in the reviewed v7 files.

## Check 6 — replay and hygiene

- Normal and `-O` replays from empty directories are byte-identical to `result.json`: 84 s normal.
- The mutant runner, with TMPDIR inside the review directory, is byte-identical to `mutants/mutants.out`.
- `SHA256SUMS` verifies all 7 files. The pinned v7 `result.json` hash matches.
- Package text: no absolute paths, emails, IPs, tokens or `__pycache__`.
- Repository state:
  - `git diff 49e1a119 200fcd9f` touches only `a2_memory_v8/` (8 files).
  - `tools/duplicate_check.py` (whole repo and package), `tools/voice_check.py` and
    `tools/artifact_placement_check.py` all pass.
  - The worktree is clean before and after; HEAD is 200fcd9f.
