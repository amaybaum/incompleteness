# Independent review: PR #885 checkpoint `mc-node9/design/native-instrument/` at `455eb092`

Reviewer scripts and outputs (in this directory; none import the author's checker):
`indep_register.py` (sampler, Born, identities via an independent affine-in-w test, two-read, closure, C-ND,
Q6a/b, entropy), `indep_cher.py`, `indep_native.py` + `indep_native.out` (own lattice simulator with
gather-based neighbour XOR; L = 44 and L = 40; seeds 11, 12, 13, 303, 404; permuted-layout Q6c),
`indep_degree_qm.py` + `indep_degree_qm.out` (GF(2) degrees, lower-degree flags, density-matrix/Lüders check).
`run_normal.out`, `run_O.out` are replays of the author's checker.

## Integrity

- `sha256sum -c SHA256SUMS`: all 6 OK; `PREREG.sha256` matches `PREREG.md` (e92724ca…).
- Move `9283b435 → 455eb092`: all six files are R100 with identical blob ids; `design/instrument/` at `455eb092` is
  byte-identical to `a7b7cb72` (the SHA256SUMS that `9283b435` had overwritten is restored).
- **Preregistration precedence is not verifiable from history.** PREREG.md, the checker and the output were first
  committed together in `9283b435`; no ref holds an earlier commit of PREREG. The only evidence of precedence is
  the self-written timestamp `2026-10-23T11:00:02Z` in `PREREG.sha256` (7 min before the commit).
- Replay: `python3 -I -B instrument_checks.py` and with `-O`, cwd = record directory: both byte-identical to
  `instrument_checks.out` (about 13 s). The checker has no `assert`, so `-O` cannot change it.
- C-NAT and Q5 use the report18 rule itself: `step` = (A_old⊕SB, B_old⊕SD, D_old⊕SA⊕SB·SD), with S the
  six-neighbour XOR. This is identical to `report18/coordinator_frontier_checks.py` and the handoff REPORT. No
  surrogate is involved.

## Claims

| # | Claim | Verdict |
|---|---|---|
| 1 | Eight preparations as four independent bits, P(λ_c=1)=(1+c·w)/2; heralded rejection, acceptance 625/4096, station-independent | **CONFIRMED.** Brute force over 16 fair bits per attempt: acceptance is 625/4096 for all 8 stations; the conditional law is exactly the product law. |
| 2 | Read carries λ_a to the receiver at tick 2; linear re-prep with 3 fresh biased bits; access list; 467 pins | **CONFIRMED WITH SCOPE NOTE.** Own simulator: receiver triple = (0, λ_a, 0); outgoing = (0, λ_a⊕1⊕r_c, 0); silent at ticks 0–1. 467 = 95 + 4·93 is a hard-coded formula that agrees with the layout. Beyond the odd-distance current pins it names, the previous-slice pin at the receiver itself (d = 0) is also outside the tick-2 cone. |
| 3a | Identities exact on the single-read record and on the two-read record (16 pairs); Born values; closure | **CONFIRMED WITH SCOPE NOTE.** Reproduced with an independent affine-in-w test (not the author's REL). Second-read Born (1+s·a·c)/2 is exact. A sympy density-matrix/Lüders computation agrees with the Bloch formula the checker uses. These results are **register-level**. Closure holds for the 4-bit hidden law λ′. The outgoing native register (one copy per component, field B) is not in the prepared format (five copies, field A), and native reuse is not built. |
| 3b | Native registers = register map "for 1024 inputs × 2 dense backgrounds" | **CORRECTED.** The code counts 4 settings × 128 inputs × 2 seeds = 1024 *runs*: **512 input assignments × 2 backgrounds**. The equality itself is confirmed: own simulator, L = 44 and 40, three further seeds. |
| 4a | Unread hidden components → identities fail, TV ≈ 0.0886 | **CONFIRMED.** TV = 95155025/2³⁰ for every setting. |
| 4b | Fresh bits → identities hold, closure fails | **CONFIRMED** for all four settings. The checker's closure test here is a proxy (`any(max(fresh_law)<1)`), not the preregistered conditional-law comparison. |
| 4c | Record site read 8–10 ticks later → X, Y, Z fail; R's dependence invisible | **CONFIRMED WITH SCOPE NOTE.** First violation at D = 8/10/8/None. TV@10 = 0.24/0.06/0.117/0; background-independent (seeds 303 and 404). The pattern is **a layout artifact**: copy rows are spaced 8 apart in the order X, Y, Z, R, so only row-adjacent components leak. With rows in the order Z, X, R, Y, R *fails* (TV@10 ≈ 0.298, leaks λ_X and λ_Y) and Z becomes the invisible case. |
| 5a | Statistics supplied, not native; entropy deficits 0.531, 0.278, 0, 0.809 | **CONFIRMED.** The deficits are hand-computed in the record and recomputed here; they count only the three fresh bits, not the sampler's fair-bit cost. |
| 5b | "Exact R-menu Born values need a non-subspace event; affine readiness gives only dyadic probabilities" | **CONFIRMED WITH SCOPE NOTE.** True under uniform counting: an affine subspace has 2^k points, so conditionals are dyadic. The operative condition is stronger than "non-subspace": the count must have odd part divisible by 5 per component, or by 25 for one joint herald. |
| 5c | "A native sampler needs a degree-12 acceptance flag" (REPORT: "degree up to 12") | **CORRECTED.** 12 is the exact degree of *this construction* only: per component, u<10 = 1+b₃b₂+b₃b₁+b₃b₂b₁ has degree 3, and four disjoint copies give degree 12 (verified by Möbius transform). It is **neither necessary nor a lower bound.** The only proved lower bound is degree ≥ 2, since degree ≤ 1 gives weight 0, 2ⁿ⁻¹ or 2ⁿ. Three exhibited alternatives give the exact product law for all 8 stations with station-independent acceptance: (i) per-component 1+x₀x₁+x₂x₃ (weight 10, degree 2), with a joint flag of degree 8; (ii) one joint flag 1+x₀x₁x₂+x₃x₄x₅ on 6 bits (weight 50, degree 3) plus 3 free fair bits; (iii) one degree-2 flag on 20 bits (weight 2⁹·1025, divisible by 50). |
| 5d | Access decides identities and closure | **CONFIRMED WITH SCOPE NOTE.** Shown by three existence witnesses (Q6a–c) for this instrument and layout. It is not a general theorem, and the heading "Access decides everything" overstates it. |

## Controls

- **C-RANK** is valid.
- **C-ND** is non-vacuous: 6 of 16 pairs fail ({X,Y}, {X,R}, {Y,R} both orders); TV 2684038546875/2⁴⁷ reproduced.
- **C-HER** is non-vacuous: all 4 settings fail; TV 9068125/2²⁶ reproduced.
- **C-AFF** is a valid scope control, but only on a toy one-atom record.
- **C-QM** reproduces the Bloch formula used to build the instrument, not the preregistered density matrices.
  Equivalence is confirmed here independently, so it is not void.
- **C-NAT** is non-vacuous. The pin was chosen after a first odd-distance attempt did not change the record; this
  is disclosed, and parity justifies it.
- Q3's "complete law = quantum law" holds by construction, because the instrument's marginals are p_plus. It is
  made independent only by the density-matrix check above.

No verdict rests on a failed or vacuous control.

## Required corrections

1. Replace the degree-12 statement (PR comment and REPORT §3.2) with: "the threshold sampler's joint flag has
   degree 12; any exact sampler needs a flag of degree ≥ 2 (non-power-of-two count); degree 2 per component (joint
   8), and degree 3 or degree 2 for a single joint flag, suffice." Also correct the REPORT header's "four
   components give degree 12" wording.
2. Q5 count: "512 input assignments (128 per setting) × 2 backgrounds = 1024 runs" (checker string, REPORT, PR).
3. Scope the README outcome line "identities, Born values and closure all hold exactly, under a native
   realization": only the single-read transport, record plus outgoing registers at tick 2, is native. The
   following are register-level or supplied:
   - preparation;
   - copies;
   - heralds;
   - fresh bits;
   - the second read;
   - closure in the prepared format.
4. Scope Q6(c), "X, Y, Z fail; R invisible; D = 8", to this layout (copy-row order X, Y, Z, R, spacing 8), or add
   the permuted-layout result.
5. The checker's VERDICT hard-codes the Q6(a)/(b) sentences; they are not conditioned on `junk`, `fresh_id` or
   `fresh_closure_fails`. The preregistration requires verdict text generated from measurements. Also make the
   Q6(b) closure test a per-setting conditional-law comparison.
6. Record that preregistration precedence rests on a self-reported timestamp, because PREREG and code share
   commit `9283b435`.

Minor:
- The "non-dyadic" PASS line prints an unchecked obstruction claim.
- Q5 is gated as a control, so a negative Q5 could only print NO VERDICT.

## Overall verdict: **ACCEPT WITH CORRECTIONS**

Every exact number reproduces independently, and the native comparison uses the actual report18 rule. Two
claims are overstated and one is miscounted: the degree-12 "need", the README's "native" scope, and the Q5
input count.
