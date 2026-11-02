# Independent results review of PE-01 (OI-PE-1): the G_clk n=5 counterexample

- **Run reviewed:** CI run `40271434371`, attempt 1. It was a `workflow_dispatch` of `.github/workflows/pe01-bounded-tests.yml`
  on `research/oi-pseudoentropy-20261025` and concluded `success`. The API confirms `head_sha` = `549641460b8ddb536178f95fac2ec9390e84a987`.
- **Head reviewed:** `549641460b8ddb536178f95fac2ec9390e84a987`, in a fresh blob-filtered clone.
- **Read:**
  - `PLAN.md` in full;
  - `amendments/A1-owner-decisions.md` and `A2-open-items.md` in full;
  - `review/code/REVIEW.md`, which I grepped and read in part;
  - `book/ch18-beyond.md:105–116`;
  - the thread `README.md` sections on the claim and on K0/K1.
- **Data:** `measurements.json` (sha256 `f17109f1…a41f067a`), `verdict.json` and `verdict.txt`, treated as data. I also fetched
  the `shard-n5-clk` and `rp-n5-clk` artifacts myself.
- **Independence:** my code is in `revpe01res/mine/`: `indep.py`, `witness.py`, `mech.py`, `search.py`, `family.py`,
  `plin.py` and `detail.py`. It was written from PLAN.md alone and imports nothing from `pe01/`. The one exception is
  check 5, where I ran the package's own `verdict.py` to regenerate the verdict, as that check requires.
- **Nothing was modified, committed, pushed, dispatched or posted.** Local compute was about 2 minutes in total.

## Verdict: CONFIRMED AT NARROWER SCOPE

The counterexample is real. I recomputed it exactly and it meets (a)–(f) as preregistered. It refutes the universal
form of `ch18-beyond.md:114` only in the following scope:
- the plan's operationalization of prediction: a guess of the visible bit X_{K′} against Q_p;
- one fixed finite reversible realization, G_clk(z^5+z^2+1) at n=5, under μ uniform, with T-level (C1) only and C2–C4
  unchecked;
- one horizon cell, K=7 with window K′=4..7;
- an observer that is active and that depends on φ (K1). It is not family-wide: it fails on all five other primitive
  quintics, the reciprocal included;
- a result that relies on the generator's visible-to-hidden backaction;
- the selected resource model: θ=n+1, footprint = memory + clock + output, with the 31-bit tables held in the dynamics
  and not charged as state.

I found no defect in the computation, the timing or the decision path. The narrower scope is a matter of
interpretation, not a correction to the generated classification (§"Required corrections").

## 1. Independent recomputation

**Construction.** I built the generator and observer from PLAN.md §1–§3:
- G_clk: φ = τ_f∘κ_σ, σ_0 = L_p and σ_1 = L_p², f = h_0;
- L_p is the Fibonacci companion map of p_5 = z^5+z^2+1, with the new bit Σc_i h_i = h_0⊕h_2;
- μ is uniform on {0,1}×F_2^5;
- the observer starts at v_0 = 0, with the clock and the output bit at 0;
- each round is v←ρ_x(v), then x←x⊕a(v), then φ;
- the readout out ⊕= 1[(v,x)∈F] fires when the 3-bit cyclic clock reads K.

**Witness tables** (from `measurements.json`, observer index 2361, χ index 0):
- ρ_0 = [1,0,2,3] and ρ_1 = [0,2,3,1];
- a = [1,0,0,1];
- χ ≡ 0, so F is the graph of χ.

**Exact values.** I enumerated the full joint state (x, v, clk, out, h) exactly with `Fraction`, over 64 initial states
for 7 composite steps:

| K′ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Pr[χ(v_K′)=X_K′] − 1/2 | 0 | 0 | 0 | **1/8** | **5/32** | **5/32** | **1/8** |

- **The four values agree with the run exactly.** The values at K′ = 4..7 match both `adv_pred` and `pred_minus_half`.
- **The readout itself gives the same values.** At K=7 the output register gives Pr[out=1] − 1/2 = 1/8. Separate
  composites, with trigger constants 4, 5, 6 and 7 on the same 3-bit clock, give 1/8, 5/32, 5/32 and 1/8 from the
  output register itself. So reading K′<K from the K-clocked registers (the run's `window_note`) is harmless.
- **The reference law is exactly 1/2.** I computed Q_p separately, with the same observer policy and each generator
  output replaced by a fresh fair bit. It gives exactly 1/2 at K′ = 4..7. The intervention alone therefore cannot
  produce the bias.
- **The polynomial convention matters.** With the reciprocal reading of the taps (h_0⊕h_3, i.e. p′_5), the same
  observer gives 0, −1/16, 1/64 and 3/64, so no window. The run's numbers correspond to the standard reading
  p(z) = z^n + Σc_i z^i, which is the plan's.

## Condition checks (all recomputed from scratch)

| Cond. | Check | Result |
|---|---|---|
| (a) | G_clk(p_5), n=5 ∈ 3..8; it is one of the three fixed primary generators (A2 WIT-A) | holds |
| (a) EX4 | the order of z mod p_5 is 31 = 2^5−1 | holds |
| (a) EX5 | (ℓ, L_p) is observable: the first 5 outputs are injective on F_2^5 | holds |
| (a) EX6 | the one-step visible matrix under μ is [[1/2,1/2],[1/2,1/2]], not a permutation, so T-level (C1) holds | holds |
| (b) EX1 | the ρ-step, a-step, φ-step, clock tick, readout and full composite are each bijections of the 4096-state joint space | holds |
| (b) EX1 | ρ_0 and ρ_1 are permutations of {0..3}; the a-step and the readout are involutions per fixed (v, clk) | holds |
| (b) EX8 | for the ρ-step, a-step, tick and readout, the h-component is the identity and the (x,v,clk,out) image is constant across h | holds |
| (b) EX8 | φ is the identity on (v, clk, out) | holds |
| (b) EX7 | the prior is μ⊗δ_{(v,clk,out)=0}, a product by construction, and EX8 holds | holds |
| (b) IM3 | the aggregated per-step simulation (`indep.adv_curve`) agrees with the full joint-state composite enumeration (`witness.py`) | holds |
| (c) | the orbit lengths of G_clk at n=5 over the 64 μ-states are 1 (×2 fixed points), 22 (×22 states) and 40 (×40 states) | see below |
| (c) | the μ-median is 40 under both the lower and upper median, so K_cx = 20 and K=7 ≤ 20 | holds |
| (d) | \|Pr−1/2\| ≥ 1/8 at every K′ ∈ [4,7], with the same O and χ; K=7 ≥ w=3 | holds |
| (d) | the signs are all positive, so the signed reading holds as well | holds |
| (e) | all 25 checkpoints are green in `measurements.json` with `failures` empty: `status` green, `failed` [], `unevaluated` [] | holds (see §5) |
| (f) | footprint = m + ⌈log₂8⌉ + 1 = 2+3+1 = 6, equal to the visible register width less the system bit; θ = n+1 = 6 | holds |
| (f) | table size = 2·2·4 + 4 + 8 + 3 = 31 bits, as printed | holds |

**The admissible cell.**
- I computed Z(G_clk, 5) = 3 by exhaustive joint-uniformity over every control sequence.
- The window floor is Z+4 = 7.
- The footprint gives ⌈log₂(K+1)⌉ ≤ 3, so K ≤ 7. With K_cx = 20, the cell is [7, 7], which is correct.
- I recomputed Z and K_cx for all three generators at n = 3..8:
  - Z = n for G_lin; 2,2,3,4,5,6 for G_filt; 2,3,3,4,4,5 for G_clk;
  - K_cx = 3,7,15,31,63,127 for G_lin and G_filt; 5,9,20,42,84,168 for G_clk.
- The resulting θ=n+1 region matches the §7 table and the verdict's recomputed region cell for cell.

## 2. Does the observer cheat?

There is no off-by-one, and the observer has no access to the bit it predicts.
- **What v_K′ can depend on.** v_K′ = ρ_{x_{K′−1}}(v_{K′−1}) depends only on X_{0:K′−1}. X_K′ is the post-φ value
  of round K′−1, read before round K′'s ρ- or a-step.
- **Why no off-by-one is possible on the guess side.** The witness's χ is constant (χ ≡ 0), so it cannot read X_K′
  through v even in principle. A readout that used v_{K′+1} would give the same value.
- **The x side.** Changing the definition of X_K′ would change the numbers. My independent implementation of the
  plan's §3 round order reproduces the run's numbers, so the run uses the plan's timing.
- **How the advantage arises.** I checked the mechanism directly in `mech.py`. Since
  X_{t+1} = c_t ⊕ Y_t with c_t = x_t ⊕ a(v_{t+1}):
  - the constant guess is right exactly when c_t = Y_t;
  - Pr[Y_t = c_t] − 1/2 at t = 3..6 is 1/8, 5/32, 5/32, 1/8;
  - c_t is a function of X_{0:t}, while Y_t = f(σ_{c_t} h_t) is the generator's output.
  - The witness is therefore a genuine next-output predictor of the generator's increment stream from the past record.
    The observer steers the self-clocking, choosing which of s_{k+1} or s_{k+2} is emitted, so that the hidden m-sequence
    bits sampled form a correlated pattern. On every path the first control is forced to c_0 = 0.
- **Not every witness in the cell uses a constant guess.** Up to relabelling of memory states fixing v_0, the 36 (O,χ)
  windows in the cell are 3 observers × 6 relabellings × {χ, ¬χ}:
  - **Observer 2361**, χ ≡ 0: positive, 1/8, 5/32, 5/32, 1/8. This is the reported witness.
  - **Observer 2745**, χ non-constant, (0,0,0,1) in canonical labelling: positive, 1/8, 1/8, 11/64, 1/8. This is a
    second sign-consistent witness that does use its memory in the guess.
  - **Observer 3526**: sign-alternating, 1/8, 1/8, −1/8, −1/8. It counts only under `abs`.

## 3. Governing-rule choice (D-SIGN)

- **The witness passes both readings.** It has Pr−1/2 > 0 at all four K′, so it meets (d) under `abs` (governing) and
  under `signed` (sensitivity).
- **The counts match my enumeration.** The run's counts are 36 windows under `abs` and 12 under `signed`. My exhaustive
  enumeration gives 36 abs pairs over 18 observers and 12 signed pairs. 12 of the 36 abs pairs are sign-alternating,
  and 24 are sign-consistent: 12 positive and their 12 complements.
- **Conclusion.** The classification does not depend on D-SIGN. The governing witness is not one of the sign-alternating
  windows that the code review's §(d) note cautioned about.

## 4. Scope

**What the verdict text says.**
- The witness line reads: "COUNTEREXAMPLE (failed: none) … footprint 6 (theta 6); table size 31 bits; K_cx=20; K0
  status: not family-wide; … T-level (C1) holds; C2-C4 not checked".
- The stage outcome reads: "COUNTEREXAMPLE to the universal form … It refutes only the universal form; it says nothing
  about the realization of the actual world, nor about the 10^-32 statement. No finite result here establishes the
  universal form."
- The text also prints the §7 resource-model sentence and the recomputed region.

All of this is accurate.

**What is refuted.** "Every embedded observer of every finite reversible realization is unable to predict." It is
refuted with the following qualifications:
- **Universal form only.** The result says nothing about typical realizations, the actual world, or ch18's 10^-32
  statement.
- **K1.** The observer's tables are chosen for G_clk(p_5).
- **Not family-wide (K0 fails).** I checked all six primitive quintics:
  - the witness gives no window on the other five;
  - per-member window counts at K=7 are [36,0,0,0,0,0], as in the run;
  - zero (O,χ) pairs are windows on every member.
- **One finite configuration.** n=5, K=7, window 4..7, with advantage 1/8 to 5/32. That is a modest constant
  advantage, not near-certain prediction.
- **Realization conditions.** T-level (C1) only, and C2–C4 unchecked. G_clk is the plan's deliberately non-autonomous
  comparator.
- **Selected resource model.**
  - θ = n+1, with footprint 6 = θ exactly. At θ = n (5) the witness would fail (f), and per A1 no conclusion is drawn
    there.
  - The tables are modelled as part of the dynamics. If the 31 table bits were charged as a program register, which
    `Main.md:560` does for its own construction, the witness would not be bounded-resource.
  - The clock is charged.
- **The witness needs activity and backaction.**
  - **Passive observers.** Passive m=2 has no window in the cell (its first window is at K=87). Passive m=3 and
    passive linear-filter m=3 or m=4 reach a K=7 window only at footprint 7 or 8, which fails (f).
  - **Other generators.** G_lin and G_filt have no admissible witness at any n.

**What it does not show.**
- predictability for passive observers;
- predictability for autonomous-hidden generators;
- predictability at K0;
- predictability beyond K=7 within any bounded footprint;
- anything asymptotic in n;
- anything about distinguishing-only, circuit or cryptographic notions;
- anything at θ=n;
- anything about whether G_clk(p_5) satisfies C2–C4, and so whether it is an admissible OI realization in the full
  sense.

## 5. Robustness and completeness

- **The §6 rule is applied mechanically.** (a)–(f) all hold from the recorded fields. CX self-test mutants were each
  refused on their own condition: window value 1/8 − 2^(−K−2) on (d), footprint θ+1 on (f), and K_cx+1 on (c).
- **No missed witness for m ≤ 2.** `search.py` exhaustively enumerated all 16 m=1 and all 9216 m=2 observers, active
  included, with every χ. It covered every θ=n+1 admissible cell of all three primary generators at n = 3..8. The only
  windows meeting (d) in any admissible cell are G_clk n=5 m=2 at K=7: 36 abs and 12 signed pairs. The first is
  (observer 2361, χ 0), the run's representative index.
  - All other m ≤ 2 cells have no window, among them n=4 m=1 [6,7] and [7,7], n=5 m=1 [7,15], and G_filt n=5 m=2 [7,7].
  - This matches the verdict.
- **Spot check of m=3 passive linear filters.** `plin.py` covered all 1344 (A,b) observers with every χ in the m=3 cells
  of n=7 and n=8 for all three generators. It found no window, which matches the verdict.
  - Calibration: at the non-admissible n=5 G_clk K=7, m=3, it finds 336 abs and 168 signed pairs. That equals 2 and 1
    classes × 168 conjugates, consistent with the run's class counts of 2 and 1.
- **Not independently enumerated.** I did not enumerate the general passive m=3 sweep (306k canonical forms at n=8) or
  the linear-filter m=4 sweep at n=8. For those I rely on the run.
- **No INCOMPLETE or VOID masking.**
  - All 38 shards are `complete` and `replay_identical: true` in run 40271434371. `failed` and `unevaluated` are empty,
    and `status` is green.
  - The `shard-n5-clk` artifact hashes to `3f6121e8…`, equal to its `shards` entry.
  - `rp-n5-clk` reads `{"identical": true}`, and the provenance names the reviewed commit.
- **sha256.** `verdict.json.measurements_sha256` equals sha256(`measurements.json`) = `f17109f10379…a41f067a`.
- **VG.** The package's `verdict.py` regenerates `verdict.json` and `verdict.txt` byte-identically from the measurements:
  `COUNTEREXAMPLE`, txt sha `3b8f5924…` and json sha `eeebc219…`. The VG self-test, including the flips and the
  sensitivity checks, passes.

## 6. Literature (A4 / §9)

**What I read in open full text.**
- RSV, arXiv:1306.3004, abstract only. It states the model as *oblivious, read-once, permutation* branching programs:
  passive tests on an input fixed in advance.
- Agievich–Solovey, arXiv:math/0505660, read in full (5 pp.). It confirms Rueppel's construction: an LFSR whose own
  output selects decimation step 1 or 2.

**Unread here** (paywalled or not fetched):
- Rueppel, "When shift registers clock themselves", Eurocrypt '87, LNCS 304, pp. 53–64. This is the self-decimated
  LFSR, essentially the 1/2-step self-clocking of G_clk;
- Gollmann–Chambers 1989 (§9, cited as G_clk's design rationale);
- Meier–Staffelbach 1989, on low-weight parity-check attacks;
- AGHP 1992;
- BDVY 2013.

**Assessment.**
- **The §9 "before candidate-NEW" papers do not cover the witness.** RSV, AGHP and BDVY concern passive or oblivious
  tests and small-bias inputs. The witness is adaptive: its interventions change the hidden trajectory. It lies outside
  their stated model, so they cannot supply a COVERED-literature tag for it. This rests on abstracts for RSV, and on my
  understanding, not on reading, for AGHP and BDVY.
- **The phenomenon itself is well known in stream-cipher cryptanalysis.** A small device that knows the feedback
  polynomial predicts bits of a clock-controlled LFSR with constant advantage, by exploiting the sparse feedback
  relation, here a trinomial. Clocking structure exposes linear relations among the sampled m-sequence positions.
  Rueppel 1987 and the Gollmann–Chambers review are the natural covering references, but I have not read them.
- **Recommendation: claim no novelty for the witness.** Its value is as a falsifier of a universal claim, not as a
  discovery. A candidate-NEW tag for the n5 G_clk emb_m2 horizons (currently "untagged: eligible for candidate-NEW
  review only after the §9 literature check") should not be assigned before Rueppel 1987 and Gollmann–Chambers 1989
  are read.
- **The plan's admissible citation list is a gap.** It does not contain these papers, so the strict L1–L4 or §9
  mechanism cannot produce COVERED-literature here. Whether to extend it is an owner decision. Tags bear on no verdict,
  so this does not affect the classification.

## Required corrections

None to the generated verdict or its classification. The computation, the decision rule, the controls and the
regeneration are all correct.

Required in the interpretation, in any REPORT.md or manuscript-facing summary (§A.25 and Code Review Rules, claim and
evidence):
1. **State that the witness is K1.** The verdict prints only "K0 status: not family-wide". Name the level, and state
   that the witness fails on every other primitive quintic.
2. **State that the witness is active and uses backaction.** It is an active observer exploiting G_clk's
   visible-to-hidden backaction. No passive witness and no autonomous-generator witness exists in any admissible cell.
3. **State that admissibility is model-dependent.** It holds at θ=n+1 with footprint = θ exactly, and with the 31-bit
   tables uncharged (the plan's tables-in-dynamics choice).
4. **"1 witness(es)" counts cells, not observers.** One (generator, n, subclass) cell holds 36 qualifying (O,χ) pairs.
   These are 18 observers, which reduce to 3 up to memory relabelling. Two are sign-consistent and one only
   sign-alternating. The text is not wrong, but it should not be read as a count of observers.
5. **Make no novelty claim**, per §6 above.
6. **No manuscript edit follows automatically.** Any edit to `ch18-beyond.md:114` and its `FULL.md:4932` mirror needs
   owner approval. If made, it should narrow the sentence to what survives rather than replace it with a universal
   negative. Per the plan's §7 and the no-go scope rule, the refutation is of the universal form for this construction
   class, not a claim that typical or actual-world realizations are predictable.
