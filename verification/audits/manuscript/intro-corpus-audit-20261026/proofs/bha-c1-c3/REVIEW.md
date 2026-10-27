*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and their outputs beside this file are the reviewer's; both were re-run by the coordinator under `python3 -I -B` and reproduce their outputs byte for byte.*

# Independent review: BH-01 (BHa), `bh01_access_v1/` at corpus commit `eae01647`

Reviewer: independent; I did not write these proofs. The review was read-only. Sources were the
package at `eae01647` and `papers/Introduction.md` at `4a260ca9`. Every script ran under `python3 -I -B`
in this directory. Sections 1–7 were written before I opened `review/` or any audit file. Section 8
is the comparison, written afterwards.

## 0. Verdicts

| object | verdict |
|---|---|
| **C1** (bijective + complete endpoint access ⇒ exact recovery) | **ACCEPT** |
| **C2** (remnant bound `P_succ ≥ 1/|K|`) | **ACCEPT WITH CHANGES** (proof correct; the corollary and the tightness wording need scope) |
| **C3** (factorization / `W`-autonomy is sufficient; "a single B–D coupling defeats recovery") | **ACCEPT WITH CHANGES** (sufficiency proved in general; the coupling sentence is an example, and false as a universal statement) |
| **Overall** | **ACCEPT WITH CHANGES** |

There is no mathematical error in any written proof (Lemma 0, C1, C2, C3, Lemma L/C4, D1). Every
count I re-derived reproduces exactly. The changes are all scope and wording, as follows:

1. The corollary "zero advantage requires `|K| ≥ |M|`" needs either a uniform message prior or
   equal-size supports. A coarse-grained message with a non-uniform prior breaks it (§3.2,
   counterexample). The bound `P_succ ≥ 1/|K|` itself holds for every prior.
2. "A single `B`–`D` coupling step defeats recovery" (REPORT L61–62) is a single example. Read
   universally it is false: 8 of the 24 coupling steps I enumerated preserve exact recovery, and
   4 of those 8 genuinely couple `B` into `D` (§3.3).
3. Tightness of C2 is a measured fact in `S_8`, not a general property. The bound is not attained
   when `|K| > |M|`, nor when `|K|` does not divide `|I|` (§3.2).
4. A side claim in the package's `MANUSCRIPT-AUDIT.md` (ch07 L12) is false as stated: "bijective
   dynamics with zero accessible advantage exist whenever the inaccessible endpoint set has at
   least `|M|` joint values". The counterexample is `|M| = 2`, `|K| = 3` (§3.4).
5. The Introduction (L160) quotes 1,376 without the record mode and dynamics that fix the
   number (§4).

## 1. Definitions as used (PLAN §2, REPORT "Proofs")

- `X = Σ_1 × … × Σ_r` is a finite product of registers. The checked runs use binary registers;
  the structured families use alphabets up to 16.
- The message `m ∈ M` is the value of designated message registers at `t = 0`. Every other
  register is *blank* (a fixed value) or *hidden-uniform*. `μ_m` is uniform on `X_m`, where
  `|X_m| = N` for every `m`. Because the message is the register content, the `X_m` are
  pairwise disjoint, and `I = ⋃ X_m` has `|I| = |M|N`.
- The message prior is **uniform** in every definition (`P_succ = (1/|M|) Σ_y max_m P_m(y)`) and
  in every proof as written. REPORT "Scope" states this: "Uniform message prior with equal-size
  supports".
- The access schedule `α(t)` is fixed in advance, with full-register reads and an external reader
  without back-action. A record is *cumulative*, `ρ_t = (π_{α(s)}(x_s))_{s≤t}`, or a *snapshot*,
  `π_{α(t)}(x_t)`.
- `K` is the set of registers outside `α(T)`. `|K|` is their number of joint values.
- *Exact recovery* means `P_succ = 1`. *Zero advantage* means `P_succ = 1/|M|`, which is
  `δ = 0` for a binary message.

**Quantifiers.** The written proofs quantify over every finite register product, every `T`,
every sequence of bijections `F_1,…,F_T` (time-inhomogeneous allowed), every schedule, and every
encoding of the stated form, with a uniform message prior. The exhaustive checks cover a much
smaller domain: `S_8`, time-homogeneous `F`, `T ≤ 3`. That smaller scope is stated correctly
(REPORT L88, L302; PLAN L240–241). No finite count is presented as a universal proof inside the
package.

## 2. The written proofs, line by line

**Lemma 0.** `Σ_y max_m c_m(y) ≤ Σ_y Σ_m c_m(y) = |M|N`, with equality iff each `y` has at most one
`m` with `c_m(y) > 0`. Correct. It holds for any prior with full support, not only the uniform
one.

**C1.** Every `F_t` is bijective, so `Φ_T` is bijective. With `α(T)` equal to all registers, `ρ_T`
contains `x_T = Φ_T(x_0)`, so `ρ_T` is injective on `X`. Disjoint `X_m` therefore have disjoint
images, and Lemma 0 gives `P_succ = 1`. Correct and fully general.

- Both hypotheses are used.
- One stated hypothesis is stronger than needed: cumulative records are unnecessary, because the
  endpoint snapshot suffices (REPORT R3 already notes this).
- The conclusion holds for **any** prior and for any message that is a function of `x_0`, coarse
  or not. Injectivity of `ρ_T` separates every function of `x_0`.
- "C1 is the case `|K| = 1` of C2" is correct.

**C2.** Let `s = π_A ∘ Φ_T`. Because `Φ_T` is a bijection and `π_A` has fibres of size `|K|`, the
fibres of `s` have exactly `|K|` points. `ρ_T` refines `s` (the hypothesis that the record
contains the endpoint snapshot of `A`), so its fibres within `I` have at most `|K|` points. So
`ρ_T` takes at least `⌈|I|/|K|⌉` values on `I`, each contributing `max_m c_m(y) ≥ 1`. Hence
`P_succ ≥ ⌈|M|N/|K|⌉/(|M|N) ≥ 1/|K|`. Correct.

- Hypotheses used: bijectivity (fibre size), the endpoint snapshot (refinement), disjoint equal
  supports (`|I| = |M|N`), and the uniform prior (the formula).
- No hypothesis is missing for the statement as written.

The conclusion also holds without the uniform prior and the equal-support hypotheses. Here is the
reviewer's proof. Let `Y = ρ_T` and `Z = π_K(x_T)`. Then `(Y, Z)` determines `x_T`, hence `x_0`,
hence `m`, so `P_guess(M | Y, Z) = 1`. Then

`Σ_y max_m P(m,y) ≥ Σ_y max_m max_z P(m,y,z) = Σ_y max_z max_m P(m,y,z) ≥ (1/|K|) Σ_{y,z} max_m P(m,y,z) = 1/|K|.`

So `P_succ ≥ 1/|K|` holds for every message prior and every hidden distribution, including
message-dependent ones, and for any message that is a function of `x_0`. Probe 1 (§5) finds 0
violations in 3,965 random instances outside the checked domain. Those instances use mixed
alphabets {2,3,4,5}, time-inhomogeneous bijections, `T ≤ 4`, arbitrary schedules, non-uniform
priors, and message-dependent, partly zero hidden weights.

- The entropy corollary `H(M|ρ_T) ≤ H(X_0|ρ_T) ≤ log|K|` is correct.
- "Guessing probability rises by at most a factor `|K|` with `|K|`-valued side information" is
  the correct known fact.

**Boundary of C2.**

- At `|K| = 1` it is C1.
- At `|K| ≥ |M|` it is implied by the blind-guess floor `P_succ ≥ 1/|M|` and has no content.
- It is informative only for `1 < |K| < |M|`.
- The bound that holds in general is `P_succ ≥ max(1/|K|, 1/|M|)`. A sharper form is
  `P_succ ≥ ⌈|M|N/|K|⌉/(|M|N)`.

**Tightness of C2.** REPORT states only that "the bound is attained in `S_8`", and that is
correct: 2,368 instances reach 1/2. In general:

- The bound is not attained when `|K| > |M|`.
- It is not attained when `|K| ∤ |I|`. Probe 4: ternary message, one blank binary register,
  `N = 1`, `|K| = 2`. The exhaustive minimum over `S_6` is 2/3, against the bound 1/2.
- It is attained in the same space with one hidden bit (`N = 2`). Probe 4b: minimum 1/2.

PLAN says "Tightness is tested", and the package reports it as measured. Any reuse should keep it
as "attained in the tested class".

**The 32 counter-maps.** Setup: AM2, all maps `{0,1}^2 → {0,1}^2`, two-bit message equal to the
whole configuration (`N = 1`), register 1 read at `t = 1`, `K` = register 0.

- Here `P_succ = |{F(x)_1}|/4`, so a violation of `≥ 1/2` occurs iff register 1 of `F(x)` is
  constant.
- That gives `2 × 2^4 = 32` maps, all non-injective (image size ≤ 2).
- Exhaustive check: the violating set equals the constant-read-register set exactly (32 = 32,
  set equality; `indep.py`). The characterization is exact.

**C3.** Hypothesis: `F_t(w,d) = (G_t(w), H_t(w,d))`.

- `G_t` is a bijection. The preimage of `{w'} × D` has `|G_t^{-1}(w')|·|D|` points and must have
  `|D|` points.
- `w_t` depends on `w_0` only. A record of `W`-registers is a function of `w_0`. Its law is the
  pushforward of the `W`-marginal of `μ_m`.
- C1 and C2 then apply in `W`.

This is correct for every finite `W`, `D`, every `T` and time-inhomogeneous maps. It is a general
proof, not a finite-case result. Notes:

- The hypothesis "initial `D` distribution independent of `m`" (PLAN C3), and the product form
  `μ_m^W ⊗ μ^D` (REPORT), are not used. Only the `W`-marginal enters. Harmless, but stronger than
  needed.
- The finite check of the preregistered C3 verdict covers only the 48 product maps in `S_8`
  (`T = 3`, homogeneous), plus 384 `W`-autonomous maps after review. The universal content rests
  on the written proof. The package says so.
- The converse is false. REPORT reports this correctly: 36,032 recovering bijections have a
  `D`-dependent `W`-update.

**"A single `B`–`D` coupling defeats recovery."** This is the named `B_D_leak` instance:

- `t = 1`: swap `B ↔ D`;
- `t = 2`: swap `V ↔ B`;
- `W` read at `t = 2`; `δ = 0`, against 1 without the leak.

It is an **example**, not a theorem. Probe 3b enumerates every bijection of the `(B,D)` pair as
the coupling step, followed by the same emission:

- 16 of 24 give `δ = 0`;
- 8 give `δ = 1`.

Four of those 8 genuinely couple: `D' = g_B(D)` with `g_0 ≠ g_1`. An example is `D ^= B`, which
recovers exactly. The direction of the coupling decides the outcome:

- `B ^= D` defeats recovery;
- `D ^= B` does not.

The S_8 necessity diagnostics already show many `D`-dependent maps that recover. REPORT L61–62
must therefore read: "a `B`–`D` coupling step can defeat recovery even with all of `W` read (the
leak model: a `B↔D` swap)."

**Lemma L / C4.** Write `y = A_t m + C_t h` with `h` uniform. For each `m`, `y` is uniform on
`A_t m + Im C_t`. Two messages have either equal laws or disjoint supports. So `P_succ` equals
the number of cosets divided by `2^k`, which is `2^{rank[A_t|C_t] − rank C_t − k}`, with
`rank[A_t|C_t] = t` because the rows of `G` are independent.

- The lower bound follows from `rank C_t ≤ min(t, n−k)`.
- The upper bound `r_t ≤ min(k,t)` is stated without proof. It follows from
  `rank[A|C] − rank C ≤ rank A ≤ min(k, t)`.

Correct and general. "C2 specializes to the same lower bound" is correct.

**D1.** Refining `y` into values `y'` gives `max_m Σ_{y'} c_m(y') ≤ Σ_{y'} max_m c_m(y')`.
Total variation is monotone under refinement by the triangle inequality. Correct, for every map
and every schedule. Monotone access is not needed, and the report says so.

**D2.** The counterexample `0,1,0` (swap in and out) is correct.

**D3.** The verdict is formally the conjunction of C1, C2 and D1, and that is fine. PLAN's prose
gloss reads "what produces recovery … is the growth of the accessible record up to an endpoint at
which the inaccessible set is empty or small", and REPORT L62 reads "growth of the accessible
record is what drives recovery". Neither is proved:

- D1 proves monotonicity, not causation.
- C1 and C2 use only the endpoint snapshot.
- In the moving-partition layout, 14,496 bijections recover exactly with `|K| = |M| = 2`, where
  C2 says nothing.

REPORT's "sufficient, not necessary" paragraph corrects the reading. L62–63 should say
"cumulative records make accessible advantage nondecreasing (D1)".

**Endpoint guarantees R1–R4 (REPORT L66–86).** As sufficient conditions they are correctly
derived from C1–C3:

- R1 gives exact recovery (`K = ∅`) or a nonzero advantage (`|K| < |M|`), not recovery.
- R2 is C3.
- R3 is more than needed, as the report notes.
- R4 is a special case of R1.

"Not necessary" is correctly witnessed by the 36,416 / 14,496 / 60 counts, which I reproduced.

## 3. Gaps and errors, with location and fix or counterexample

### 3.1 No proof errors

Lemma 0, C1, C2, C3, Lemma L and D1 are correct as written, and general.

### 3.2 C2 corollary: "zero advantage requires `|K| ≥ |M|`"

Locations: REPORT L42–47, PLAN C2 gloss, Introduction L160.

The corollary is correct for the stated form. Here is the reviewer's argument. Zero advantage
means `P_succ = max_m p_m`. That forces every positive-mass record fibre to contain a point of
every maximizing message. Fibres within `I` have at most `|K|` points, and there are at least
`|I|/|K|` of them. Hence:

- **Uniform message prior** (every message maximizes): each fibre holds points of all `|M|`
  messages, so `|K| ≥ |M|`. This holds for any support sizes and any hidden weights. Probe 6: 0
  zero-advantage instances in 3,000 random coarse-message cases with `|K| < |M|`.
- **Equal-size supports** (any full-support prior): `|M|N/|K| ≤ #fibres ≤ N`, so `|K| ≥ |M|`.
  Probe 2b: 0 of 720 bijections of `Z3 × Z2` with prior (1/2, 1/4, 1/4) reach zero advantage
  at `|K| = 2`.
- **Neither:** the corollary fails. Probe 2 is a coarse-grained message on an identity bijection
  of `{0,1}^2 = (a, k)`, reading `a`. Take `m = 0` on `{(0,0), (1,0)}`, `m = 1` on `(0,1)` and
  `m = 2` on `(1,1)`, with configurations uniform, so the prior is (1/2, 1/4, 1/4). Then
  `|M| = 3`, `|K| = 2`, and `P_succ = 1/2 = max prior`: zero advantage with `|K| < |M|`. The
  general statement is `|K| ≥ |I|/N_{m*}`.

Fix: keep one of the two qualifiers. The Introduction text omits both. The audit's proposed
"uniformly distributed message" is a correct and sufficient fix. C2's own bound `P_succ ≥ 1/|K|`
needs neither qualifier (§2). The scope matters physically, because "what formed the black hole"
is typically a coarse property with a non-uniform prior.

### 3.3 C3 coupling sentence

Location: REPORT L61–62. See §2 for the fix, and Probe 3 / 3b for the counterexamples
(`D ^= B` and three others).

### 3.4 Claim A converse in `MANUSCRIPT-AUDIT.md`

Location: ch07 L12 entry: "bijective dynamics with zero accessible advantage exist whenever the
inaccessible endpoint set has at least `|M|` joint values (for a binary message, whenever any
register is inaccessible)". **This is false as a general statement.**

Probe 5:

- a binary message register, read at the end, with a hidden-uniform ternary register `K`;
- `|K| = 3 ≥ |M| = 2`;
- over all 720 bijections, `δ ∈ {1/3, 1}` and is never 0.

The existence condition for an endpoint-snapshot record is `N ≤ |A|·⌊|K|/|M|⌋`. The claim is true
in the tested binary layouts, and REPORT L45 scopes it that way: "in the tested layouts".

Fix: scope the `MANUSCRIPT-AUDIT` sentence the same way, or state the divisibility condition.

### 3.5 C2 tightness

Location: PLAN C2. Keep tightness as "attained in `S_8`". In general the bound is not attained
for `|K| > |M|` or `|K| ∤ |I|` (Probe 4).

### 3.6 Minor wording

- C1 is stated with "cumulative records", but the snapshot suffices.
- The C3 hypothesis "D independent of m" is unused.
- The upper bound in Lemma L is unproved but trivial.

## 4. Introduction (`4a260ca9`), sentence by sentence

The brief quotes "conserve information but do not by themselves guarantee recovery". That phrase
does not occur at `4a260ca9`. L158 reads "Conservation neither implies nor is necessary for
recovery". Likewise, "60 non-injective maps" does not occur; L158 says "non-injective maps with
exact recovery" without a count. I review the text as it stands.

| line | sentence | assessment |
|---|---|---|
| L12 | "finite computations separate the conservation of information … from its recovery" | Supported: claim A by counterexample, C1/C2 by written proof. |
| L28 | "written proofs and exact or exhaustive checks, whose novelty has not been established" | Correct. C1 is near-tautological, C2 is the known guessing-probability fact, and Lemma L is the linear (ramp) secret-sharing threshold. |
| L156 | "They concern the framework's nested-partition construction … not a particular black hole" | Partly overstated. The **layout and prior** are the framework's; the **maps are generic permutations**, not the substratum dynamics (REPORT L289–290). Suggest: "They use the framework's nested-partition layout and hidden-uniform prior with generic finite maps." The proofs hold for every bijection, so they apply to the framework's `φ` as theorems. The counts do not describe `φ`. |
| L158 | "Conservation neither implies nor is necessary for recovery … exhaustive computations exhibit bijections with no accessible advantage … and non-injective maps with exact recovery" | Correct as a statement of logical independence between map classes. A single example (swap into a remnant, or the identity with an unread message) already suffices; exhaustiveness adds counts, not force. |
| L160 | "1,376 of 40,320 … zero accessible advantage for a binary message with one register unread after two emissions" | **Reproduced exactly** by independent code, but under-specified. The number requires time-homogeneous `F`, **cumulative** records with reads `(), (2), (1,2)`, and the other two registers hidden-uniform. With the endpoint snapshot only, the count is **10,944** (`indep.py`). Fix: add "time-homogeneous, cumulative records". |
| L160 | "For bijective dynamics, complete endpoint access gives exact recovery" | C1. Correct. |
| L160 | "with `U` inaccessible `P_succ ≥ 1/|U|`" | C2. Correct, and more general than stated (any prior). |
| L160 | "so zero advantage in a bijective instance requires `|U| ≥ |M|`" | Correct under a uniform message prior, or with equal-size supports. It fails for a coarse-grained message with a non-uniform prior (§3.2). The qualifier is not stated. |
| L160 | "32 non-injective maps of `{0,1}^2` violate the bound" | Correct; exactly the maps whose read register is constant. The setup (two-bit message, one register read) is not stated. |
| L160 | "These endpoint guarantees are sufficient, not necessary." | True: 14,496 bijections recover exactly with a register unread, 60 non-injective maps recover, and 200 non-injective maps satisfy the bound. Placed right after the 32 counter-maps, which show bijectivity cannot be dropped *from the bound's hypotheses*, the sentence invites a misreading. Suggest: "These conditions are sufficient for recovery, not necessary for it: exact recovery also occurs with a register unread." |
| L160 | "remnant-capacity form of a known fact … its linear case is the secret-sharing threshold" | Correct. |
| L162 | "timescale ordering does not supply it [BHa, item F]" | Outside C1–C3; checked roughly. Item F shows that the A.7 ordering `τ_evap ≪ τ_B^D` fails above ~10^10–5×10^12 kg (my order-of-magnitude check agrees: Γ = 1 crossover ≈ 1×10^11 kg). For lighter holes the ordering holds at the evaporation scale. It cannot supply decoupling "over whole cycles" for any mass, since cycle times dwarf any finite `τ_B^D`. The sentence is true, but the citation supports the mass-dependent half. |
| L175 | "each proved on paper or checked exhaustively at small size or by exact arithmetic. No claim … that information reaches `D` …" | Matches REPORT "What item F does not show". Correct. |
| L191 | "it separates conservation from accessible recovery" | Supported. |

No Introduction sentence presents a finite count as a universal theorem. The universal sentences
(C1, C2) rest on the written proofs, which are correct.

## 5. Enumerations and searches

**Package replay.** I copied `checks.py` (sha256 `94687760…7fba`, matching `SHA256SUMS`) into
`pkg/` and ran `python3 -I -B checks.py --out run/`. Exit 0, 31 s wall time. The new
`result.json` is **byte-identical** to the committed one (`cmp`), sha256 `0f08dd56…a7ea7`.
I did not run `mutants.py` (6–10 min, not needed for the proofs).

**Independent enumeration** (`indep.py`, own encoding and code, nothing imported from
`checks.py`; output in `indep-output.txt`):

| quantity | package | reviewer |
|---|---|---|
| MP1, `t = 2`, TV histogram 0 / 1/2 / 3/4 / 1 | 1376 / 12672 / 11776 / 14496 | **1376** / 12672 / 11776 / 14496 |
| same, endpoint snapshot only | not reported | 10944 / 25920 / – / 3456 |
| MP2, `t = 2`, `P_succ` 1/2 / 5/8 / 3/4 / 7/8 / 1 | 2368 / 768 / 21120 / 5888 / 10176 | identical; none at 1/4 |
| nested, `t = 3`, TV 0 / 1/2 / 1 | 2688 / 10944 / 26688 | identical |
| nested, `W` read at end, recover / not | 36416 / 3904 | identical |
| `W`-autonomous / products / failing | 384 / 48 / 0 | identical |
| snapshot, decreasing TV | 21632 | identical |
| `{0,1}^2` maps: bij-rec / nonbij-rec / nonbij-norec | 24 / 60 / 172 | identical |
| AM2 violations, = constant read register | 32 | 32, set-equal |
| GL(4,2), k=1 profiles | 10752/5376/2688/1344 | identical (rank formula only) |
| GL(4,2), k=2 profiles | 9216/4608/2304/2304/1152/576 | identical |

**Analytic checks.**

- 84 recovering maps of `{0,1}^2`: the image `f` of the `m=0` pair has size 1 (4 ways, with the
  `m=1` pair mapped into the other 3 points: 9 ways) or size 2 (12 ways × 4). That gives
  `36 + 48 = 84 = 24 + 60`, and `256 − 84 = 172`.
- The 32 counter-maps: `2 × 16`.
- The GL counts match REPORT's analytic cross-checks.

**Probes outside the checked domain** (`probes.py`, output `probes-output.txt`):

| probe | content | result |
|---|---|---|
| 1 | C2, random: mixed alphabets {2,3,4,5}, `≤ 400` states, `T ≤ 4` inhomogeneous bijections, random cumulative schedules, non-uniform priors, message-dependent hidden weights with zeros | 0 violations / 3,965; min `P_succ·|K|` = 1 (bound attained) |
| 2 | coarse message, identity bijection, `|M| = 3`, `|K| = 2` | `P_succ = 1/2 = max prior`: zero advantage with `|K| < |M|` |
| 2b | equal supports on `Z3 × Z2`, prior (1/2, 1/4, 1/4), `|K| = 2` | 0 of 720 at zero advantage (corollary holds) |
| 3 / 3b | single `B`–`D` coupling then emission | swap 0, `B^=D` 0, `D^=B` 1; over 24 couplings: 16 → 0, 8 → 1 |
| 4 / 4b | C2 tightness, `|K| = 2`, `|M| = 3`, `N = 1` / `N = 2` | min 2/3 (not tight) / 1/2 (tight) |
| 5 | `|M| = 2`, `|K| = 3`, endpoint read of the message register | TV ∈ {1/3, 1}; no zero-advantage bijection |
| 6 | uniform message prior, coarse messages with unequal supports and random weights, `|K| < |M|`, 3,000 random cases | 0 zero-advantage instances (corollary holds under uniform prior) |

## 6. Proof correctness versus physical interpretation

**What is proved.**

- For any finite register product, any bijective `F_1..F_T` and any fixed full-register read
  schedule:
  - a complete joint endpoint read determines `x_0` (C1);
  - an endpoint read missing a set of `|K|` joint values leaves Bayes success at least `1/|K|`
    for any message that is a function of `x_0` (C2; the package proves it for a uniform prior,
    and it holds for any prior);
  - if the `W`-update never depends on `D`, then `D` can be ignored (C3);
  - cumulative records make success monotone (D1).
- Bijectivity alone does not make the message recoverable from a proper projection, and
  bijectivity is not needed for recovery. These are elementary facts about bijections and
  projections, and they are rigorous.
- **None of them uses anything specific to OI.** C1–C3 and D1 are prior-independent. The
  hidden-uniform Liouville prior, cited as "taken from the framework's construction", matters
  only for the counts, not for the theorems.

**What is claimed or implied physically, and whether it is supported.**

- *"Conservation does not imply recovery."* Supported, as a statement that conservation of the
  global configuration is a property of the map and recovery is a property of the map plus the
  access class. It says nothing about whether any real black hole's radiation carries its
  information. The counts (1,376, 2,688) are counting measure on generic permutations and carry
  no physical weight, as the package says.
- *C1 as a guarantee for an OI observer.* Under OI's own premise the observer is a proper part
  with a hidden sector, `D` beyond the cosmological horizon. `K = ∅` therefore never holds for an
  OI observer. Any guarantee for radiation records must come through C3 (`D` decoupled: R2) or
  C2 (`D` small, which it is not). The package says so ("the guarantee for radiation records
  draws on R2"), and item F removes the stated support for R2. So within the framework,
  C1–C3 give **no** established recovery guarantee for Hawking radiation. They give a
  conditional one, conditional on H-decouple. The Introduction is consistent with this (L162,
  L175).
- *C2 as a "remnant bound".* The bound is classical. For an emergent quantum remnant of Hilbert
  dimension `d` the analogous bound is `1/d²`, not `1/d`. Superdense coding: a two-bit message
  in one of four Bell states on (radiation qubit, remnant qubit) gives `P_succ = 1/4` from the
  radiation alone, with `d = 2`. The classical `1/|K|` applies to OI only if `|K|` counts the
  remnant's **substratum configurations**, including any hidden-sector memory, not its emergent
  quantum dimension. The model does not make that identification. "Remnant-capacity" readings
  must therefore stay in the configuration-count register, and the Introduction does keep them
  there ("toy models of configurations, permutations and configuration reads").
- *Emission.* In the `S_8` moving-partition runs nothing is emitted. A homogeneous permutation
  keeps acting on registers already read, and "emission" is a read schedule. In GR A.7 emitted
  modes leave `B`, which is a structural difference between the two.
- *Reads.* Full-register, back-action-free, fixed-schedule reads by an external reader do not
  model an embedded observer whose records are registers of `X`. The package states this
  limitation (REPORT L285–294).
- The package does not claim, and the Introduction does not claim, that the information paradox
  is resolved, that information reaches `D`, or that the Page curve follows. I found **no
  physical reading exceeding the model** in the Introduction's BHa sentences, apart from the
  "concern the framework's nested-partition construction" phrasing (L156, §4).

## 7. Bearing on the broader framework

1. The positive results (C1–C3) are generic facts about bijections. They neither use nor support
   any OI-specific structure. They can be cited for OI only as constraints any bijective
   substratum satisfies.
2. For an OI observer, recovery of black-hole information rests entirely on a decoupling
   hypothesis (H-decouple / R2) for the always-present hidden sector. This is a standing
   assumption-watch marker. It applies to every framework claim of the form "bijectivity
   ⇒ information is in the radiation" (cf. the package's `MANUSCRIPT-AUDIT` entries on ch07
   L12/L110).
3. Quantum-versus-classical capacity (§6): any later lane that moves from configuration reads to
   emergent quantum remnants needs the `d²` form, or an argument for why substratum
   configuration counts are what bound hiding.
4. Coarse-grained messages (§3.2): the zero-advantage corollary needs a uniform prior or
   equal-size supports. Physical "what formed the hole" questions are coarse and have non-uniform
   priors.

## 8. Comparison with the package's `review/` and the audit's rows (written after §§0–7)

I compared after writing and fixing the verdict. One change followed the comparison: §3.2 was
refined by a further probe (Probe 6). Reading the audit's R-20 had prompted me to check whether
"uniform message prior" alone suffices for the corollary. It does. The verdicts did not change.

### 8.1 Package `review/` (REVIEW of `587d4196`, RECHECKs of `95458016` and `df2ea6f5`)

**Agreement.** The internal review found the proofs of Lemma 0, C1, C2, C3 (sufficiency),
Lemma L and D1 correct, and every count reproduced. I agree on all of these, from independent
code. The current REPORT already carries its F1 fix: R1–R4 are sufficient conditions, not
necessary ones, and the C3 converse is false. Its F4 fix (claim A qualified by `|K| ≥ |M|`) and
F8 split (25,824 / 3,904) are also in place, and I confirm both. Its observation that
`W`-autonomy suffices for C3 is what the REPORT now proves. I checked that proof and it is
correct.

**Findings here that are not in `review/`:**

1. **The `|K| ≥ |M|` existence wording is false in general (§3.4, Probe 5).** The internal F4
   fix itself introduced the wording "zero advantage exists whenever the inaccessible endpoint
   set has at least `|M|` joint values". MANUSCRIPT-AUDIT ch07 L12 carries it unscoped. It fails
   for `|M| = 2`, `|K| = 3`. REPORT L45 scopes the binary case "in the tested layouts", which is
   fine.
2. **"A single `B`–`D` coupling defeats recovery" is an example, not a theorem (§3.3, Probe 3b:
   16 of 24 couplings defeat recovery, 8 do not).** The review did not flag it. It flagged the
   converse of C3 instead, which overlaps but is distinct.
3. **The C2 bound holds for every prior, and the corollary's precise hypothesis** is a uniform
   prior *or* equal-size supports (§2, §3.2). The internal review called C2 "the min-entropy
   chain rule" but kept the uniform-prior scope.
4. **Tightness of C2 fails for `|K| > |M|` or `|K| ∤ |I|`** (Probe 4).
5. **Physical interpretation (§6).** The internal review says the F3 falsifier moves "a classical
   finite toy result into a physical falsifier about quantum radiation". It does not give the
   quantum `1/d²` superdense-coding counterpoint to the remnant bound. It also does not observe
   that `K = ∅` never holds for an OI observer, so every OI guarantee routes through R2/C3.
6. **D3 and REPORT L62 "growth … is what drives recovery"** overstate D1, which proves
   monotonicity, not causation. The review accepted D1 without comment on this gloss.
7. **The 1,376 count depends on the record mode.** It is 10,944 with snapshot records. This
   bears on the Introduction's under-specified L160 sentence.

No finding in `review/` contradicts mine.

### 8.2 Audit matrix rows I-210–I-222 and I-305 (`intro-corpus-audit-20261026`, read at worktree `a9f06a5b`)

| row | audit verdict | my assessment |
|---|---|---|
| I-210 (global conservation from bijectivity, a premise) | FAITHFUL, conditional | Agree. |
| I-211 (does not imply recovery) | FAITHFUL, proved-paper | Agree. A single counterexample suffices; the "uniform prior / equal supports" assumptions the row lists are not needed for a non-implication. |
| I-212 (not necessary) | FAITHFUL, exhaustive-exact | Agree (60 reproduced; analytic 84 − 24). |
| I-213 (bijections with zero advantage) | FAITHFUL | Agree (1,376 and 2,688 reproduced). |
| I-214 (non-injective exact recovery) | FAITHFUL | Agree. |
| I-215 (1,376 of 40,320) | FAITHFUL | Count correct and reproduced. **I would mark it IMPRECISE:** the number needs time-homogeneous `F` and cumulative records; snapshot records give 10,944. |
| I-216 (C1) | FAITHFUL, proved-paper | Agree; general. The row's listed toy-model assumptions (uniform prior etc.) are not needed by C1. |
| I-217 (`P_succ ≥ 1/|U|`) | IMPRECISE; fix adds "uniformly distributed message, uniform unread data" | **Partly disagree.** The bound holds for every prior and hidden distribution (§2, reviewer's proof; Probe 1, 0/3,965). The added qualifiers are safe but unnecessary. R-20's pressure test calls the any-prior remark "an auditor's argument, not a corpus result", which is accurate about provenance, but the remark is correct. If the text keeps the qualifier, attach it to the corollary (I-218), not to the bound. |
| I-218 (zero advantage ⇒ `|U| ≥ |M|`) | IMPRECISE | **Agree.** The audit's "uniformly distributed message" is a sufficient fix (§3.2; Probe 6). Equal-size supports would also do. The counterexample when both fail is Probe 2. |
| I-219 (32 counter-maps) | IMPRECISE; population and bound unstated; "the read register is constant" | **Agree.** The characterization is verified exactly (set equality). |
| I-220 ("sufficient, not necessary") | IMPRECISE; fix "sufficient for recovery, not necessary" | **Agree**, the same fix as mine (§4). |
| I-221 (remnant-capacity form of a known fact) | FAITHFUL; no literature source | Agree; correct fact. The quantum analogue is `1/d²` (§6), which matters if the sentence is read physically. |
| I-222 (linear case = secret-sharing threshold) | IMPRECISE (Sha79 unread) | Agree on the citation point. The mathematics (Lemma L) is correct. As a GF(2)-linear threshold with `r_t ≥ t − (n−k)` it is a linear ramp-type scheme, and a ramp/linear secret-sharing reference may fit better than Shamir's polynomial `(k,n)` scheme. Reviewer's recollection, not checked first-hand. |
| I-305 (L191 "separates conservation from accessible recovery") | FAITHFUL | Agree. |

**Not covered by those rows.**

- L156: the audit's I-209/R-21 already flags "concern the framework's nested-partition
  construction" as IMPRECISE, with a fix ("arbitrary bijections in place of its dynamics"). I
  agree with it.
- The audit has no row on the `B`–`D` coupling sentence, which is not in the Introduction, or on
  the MANUSCRIPT-AUDIT existence wording, which is outside the Introduction. These are package
  findings only.

**Net.** The audit and this review agree on every Introduction verdict except two:

- I-215: I would downgrade it to IMPRECISE.
- I-217: the proposed qualifier is unnecessary for the bound, though harmless.

No row the audit marks FAITHFUL is contradicted by a counterexample.

## 9. Files

All files are in `S/proofrev/bha/`:

- `REVIEW.md`: this file.
- `indep.py`, `indep-output.txt`: independent enumeration.
- `probes.py`, `probes-output.txt`: probes 1–6.
- `pkg/`: a copy of `checks.py`, `result.json` and `SHA256SUMS` as committed.
- `run/result.json`, `run/stdout.txt`: the replay output, byte-identical to the committed
  `result.json`.
