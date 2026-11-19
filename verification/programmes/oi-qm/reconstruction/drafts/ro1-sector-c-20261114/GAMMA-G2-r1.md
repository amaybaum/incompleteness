# GAMMA-1 unit G2, r1; paper-only; the record laws on K1; unreviewed

**What this note does.** It derives by hand, on the native K1 model, the record laws that G1 r4
defines (`GAMMA-G1-r4.md`, cited G1 §N): the record spaces and incident events under the E-set and
E-prep encodings, the masses and normalization `κ_norm`, and the detection laws under each `κ_det`
variant, separately. It settles G1-F3 on K1 (pending review), narrows G1-F4, derives the screen's coset law of G1 §4.2
for declared two-path geometries (PLAN-G's H-1), fills NC-copy's slot of G1 §7.1, and evaluates C0's
additivity defect `Δ` and PC-wave as required controls. It runs no computation, simulation,
enumeration or Lean, edits no manuscript, adopts no premise, extension, sector condition, `μ`, encoding
or detection rule, and changes no Issue. It gives no verdict on D-1 or on (γ) beyond what the
derivations show (§9).

**Authorization.** Owner decision record #1169 c.6893331779 (`amaybaum`, 2026-11-15T11:00:45Z), wave
2, item 1: "**G2:** hand-derived record laws on K1, reusing the accepted 2b calculations." Same record:
"Each unit gets an independent review before it is presented." "**Not authorized:** execution,
computation, merges, manuscript edits and new premises. Physical source remains **NOT PASSED**."
Binding from #1169 c.6893456888 (`amaybaum`, 2026-11-15T11:12:09Z): total finiteness of the bijective
representative is posit (ii) of the posit ledger (Main.md:724), carried as A1, "a premise only of the
results that use it". Results here that use a finite `S` carry **[A1]**. G1's acceptance (#1169
c.6892563291): "Results that depend on U4, and credit by scope alone, stay conditional."

**Issue.** #1305 (GAMMA-1). **Writer:** Claude. **Review:** independent non-author review pending.

**Inputs, at exact objects.**
- RO-1 drafts in `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`,
  branch `research/ro1-sector-c-1169-20261114` at `6ab9515dec3d54ad90058bfec0d24c49c0e78d73`
  (PR #1294). **Off `main`.**
  - `GAMMA-G1-r4.md`, blob `91a5d656bed2b5ef5781106f1e22bfecbf35cd8b` (G1 §N); definitions accepted
    (#1169 c.6892563291), with the focused review's fixes confirmed;
  - `U4-CALC-r2.md`, blob `bef634e2100979d499b87f7139440dd6cff4fc64` (CALC, by result), reviewed
    ACCEPT (`REVIEW-U4-CALC-r2.md`, blob `70eddf2dad303b31c9691ad8ac1dcd3ee4576f8f`), owner-accepted
    as "a bounded paper-only calculation" that "upgrades no named premise and establishes no physical
    source" (#1169 c.6892224647);
  - `S3-U4-r3.md`, blob `54ee962919ab17d04f430b2847ab677cbc444829` (U4 §N), owner-accepted (#1169
    c.6892563291: "D-1 stays undecided at γ. No experimental contradiction is established");
  - `SIGMA12-SCREEN-r2.md`, blob `8d71ff13548a2eb87baf3ddf0a6536fd24421e6f` (SIG §N), accepted as "A
    partial screen only. Nothing counts as a negative under SNR-1" (same record);
  - `S3-U1-r5.md`, blob `68983f8666df0ca6c26ec4b9ec00d0a9e4072f67` (U1:N), accepted criterion;
  - `S3-U2-r3.md`, blob `2711c168a65c0ae4397195593528fcf0ee6a4cba` (U2 §N), for the SNR-1 counting
    condition on U1's factor-set reading (U2 §11.1);
  - `GAMMA-PLAN-r1.md`, blob `77f1fcd8d32403b26fb87c47cfd572bbf982febb` (PLAN-G:N), plan only.
- Corpus at `origin/main` `75cc51009aebcfb17c1bbf76d149760c540aac3b`, read with `git cat-file`:
  `papers/Main.md`, blob `0db17597` (Main:N); MR★, `.../measurement-record-formation/amendments/MR-star.md`,
  blob `45af1678` (MR★:N); SUBSTATE-1's protocol, `.../continuous-substates/observation-context-protocol.md`,
  blob `6ca6f0ab` (OCP:N).
- GitHub records read through the API on 2026-11-15: #1169 c.6893331779, c.6893456888, c.6892563291,
  c.6892224647.
- OA-1 is cited only through U1's quotations (OA1:N via U1).

**Labels.** **[proved here]**: proved by hand in this note, unreviewed. **[instance]**: checked by
hand on one explicit configuration; it shows that a case occurs and nothing beyond it. **[A-inf]**:
author-side inference, not a proof. **[NP]**: named premise (§A.46 item 7). **[CALC]**: an accepted
2b result, cited by its number and used as stated there. **PROVISIONAL**: rests on U4 r3. **[A1]**:
uses a finite `S`. **[assumed]**: an input the corpus does not source (U1 §2.3), here always a carrier
or quiet-region law entered as a datum of a declared `μ`.

***

## 0. Scope, hypotheses, reuse

**G1 §12's list for G2, and where each item is answered.**

| Item | Section |
|---|---|
| both `κ_det` variants, separately | §1.3, §4 |
| `κ_norm` | §2.5 |
| the record spaces | §2.1 |
| the incident events, E-set and E-prep | §2.2–§2.4 |
| G1-F3 | §2.2 (settled on K1, Proposition G2-3) |
| G1-F4 | §4.2 (narrowed, Theorems G2-2 and G2-6) |
| the screen's coset law (G1 §4.2) | §3 (Theorem G2-5) |
| NC-copy's slot (G1 §7.1) | §5 |
| C0's `Δ` and PC-wave as required controls | §6 |

**Hypotheses.** CALC §0's H-K1 (the K1 step `φ(x, y) = (y, A y − x)`, `a = 1`, `𝐑 = ℤ/q`, a torus
`Λ = ∏ ℤ/L_c` with every side `≥ 3`; `d = 3` is the native graph, MR★:467–471), H-μ (an arbitrary
carrier law `λ` on `S_Σ`, every non-carrier region uniform and independent), H-acc (`π_B = id` under
A-reg, the current slice under A-cur) and H-avail, all as stated there. Added here:
- **H-obs** (G1 §2.1). The four observers `V_D ⊇ D`, `V_A ⊇ A`, `V_Z ⊇ Z`, `V_E ⊇ H_e ∪ L` are
  disjoint factor sets of the declared product decomposition (AD-1(a)), the same in every protocol.
  The screen cells `D_1, …, D_n` are disjoint sets of sites.
- **H-rec** (G4; U1 §2.1, "Execution"). Every component of the complete record, and every herald or
  attempt label a law is conditioned on, is a function of the readable configuration of the observers
  at `t_c`.

**Levels used** (U1 §2.3). *Derived*: `μ = μ-G`, the counting probability (Main:54), possibly
conditioned on an executed herald with the complementary mass kept. *Relative to a declared `μ`*:
H-μ with a non-uniform carrier law `λ`, or with further non-uniform regions, each such law a
`μ`-datum, listed. CALC's H-μ states that a prepared carrier "is **[assumed]**"; every result below
that uses a non-uniform `λ` is a statement about laws relative to that declared `μ`, and none is a
claim that such a carrier is sourced.

**Reused, exactly as stated in CALC.** Theorem 1(a)–(c) and its proof (CALC §1.2), applied, as
Proposition 2.8(i) applies it to `D`, to any readable region or union of readable regions: its proof
uses only that `π_B pr_B φ^t` is a homomorphism (for (a)) and surjective (for (b)). Theorem 1′ (§1.3).
Proposition 1.4 (§1.4). The lattice coefficient in Proposition 2.6's proof: on `ℤ^d`, the tick-0
state `(0, rδ_i)` has `ũ_t(i + te) = r`, so `U_t(A)_{i+te, i} = 1`, with the torus lift as there.
Proposition 2.8(i) (§2.6). Instances 1.1 and 1.2 (§1.5). Theorem 2 and Propositions 2.5 to 2.7 are
not used except where §11 names them.

***

## 1. The derived level: one product law for every rule

### 1.1 Lemma G2-1 (single-tick independence and monogamy) [proved here; A1]

*Hypotheses:* any rule with `φ` a bijection of a finite `S = ∏_f S_f` (the declared factors), and
`μ = μ-G`. No K1 hypothesis is used.

(a) At every tick `t`, `φ^t s` is uniform on `S`. Functions of the tick-`t` content of disjoint sets of
factors are independent.

(b) **Monogamy.** If a property `X` of the state (at any tick) is a function of the tick-`t` content of
a factor set `F`, then every function of the tick-`t` content of factors disjoint from `F` is
independent of `X`. In particular `X` cannot be a nonconstant function of two disjoint factor sets at
one tick.

*Proof.* (a) A bijection preserves the counting measure, so `φ^t_* μ-G = μ-G`. The uniform law on a
product is the product of the uniform laws on the factors (Main:58 states this for `𝒞_V × 𝒞_H`).
(b) From (a): `X = g(s_F(t))` and `Y = h(s_G(t))` with `F ∩ G = ∅` are independent. If also
`X = h(s_G(t))`, then `X` is independent of itself, hence constant `μ`-almost surely. `□`

Under A-cur the factors are the current slices of observer sites and the hidden rest (AD-1(b)); under
A-reg, whole sites. (a) is OA-1's D2 ("`H_t` is uniform and independent of every function of `V_t`",
OA1:145–155 via U1) with the visible part split into disjoint observers. OA-1's Gap 1, "a selected
hidden carrier cannot be held together with its choice record, for every bijection" (U1 C-PREP,
"disproved at that scope"), is a case of the same independence; (b) states it for any two disjoint
factor sets.

### 1.2 Theorem G2-2 (the compared laws at the derived level) [proved here; A1]

*Hypotheses:* Lemma G2-1's, with H-obs and H-rec; any rule (either reading of P-vii), either slice
form, any geometry, any `t_c`; an incident event `𝔈_a` that is an event on `(V_Z, V_E)`'s readable
configuration at `t_c`. That covers E-set (`𝔈_a = {ζ(Y_{V_Z}(t_c)) = a}`), E-read (`𝔈_*`), E-prep with
its attempt label held at `t_c` in `e` (G1 §3.2), and conditioning on any herald held at `t_c` in
`V_E` (G1 §3.1, §5.3).

Then, writing `Y_B` for the readable configuration of `B` at `t_c`,

    L_a^full(s, c_A, z, e, ℓ) = P_D(s) · U_{𝒞_A}(c_A) · L_a^{ZE}(z, e, ℓ),

with `P_D` the image of the uniform law on `𝒞_{V_D}` under the declared detection map, `U_{𝒞_A}` the
uniform law on `V_A`'s readable configurations, and `L_a^{ZE}` the restriction of `μ-G`'s image on
`(V_Z, V_E)` to `𝔈_a`, of mass `μ(𝔈_a)`. Under `P_D` the cell detections `s_1, …, s_n` are independent,
with `P(s_j = 1) = p_j`:
- `κ_det^part`: `p_j = |C_j| / |𝒞_{D_j}|`, with `C_j` the declared click class;
- `κ_det^rdy`, where the screen preparation's herald is held at `t_c` in `V_E`: `p_j = 1 − r_j`, with
  `r_j` the fraction of `D_j`'s readable states in the declared class of the prepared value. Without a
  held herald `κ_det^rdy` is undefined (G1 §5.2).

*Proof.* By H-rec, `(Y_{V_D}, Y_{V_A})` and `(Y_{V_Z}, Y_{V_E})` are functions of disjoint factor sets
at `t_c` (H-obs), so Lemma G2-1(a) makes them independent and uniform; `𝔈_a` and every conditioning
event lie in the second group. The cells read disjoint factors, so the `s_j` are independent. `□`

**Consequences** [proved here; A1], each read through G1's definitions:
- *Per incident mass* (G1 §5.3): `c_a(j) = p_j` for every protocol `a ∈ 𝒜_10` and every encoding above;
  conditioning on `e = (a, E)` changes nothing on `V_D` or `V_A`.
- *Sum rule and E-read* (G1 §3.3): hold, with every marker-sorted screen law proportional to `P_D`.
- *`κ_cmp`, qualitative* (G1 §5.7): every pair ratio `c₁/(c₁ + c₂)` is the constant
  `|π^{-1}(m₁)| / (|π^{-1}(m₁)| + |π^{-1}(m₂)|)`, so `V_u = 0` and "fringes absent" on every channel, at
  every point of `𝒮` (`V_u = 0 ≤ 0.1`, the least `v_−`): stable. Any ratio against a one-path normalizer
  formed from two laws of this form is `1/2` on the support: absent.
- *`Δ`*: formed from any three laws of this form, `Δ_j = p_j − p_j − p_j = −p_j` (§6.3).
- *`K_P`* (G1 §2.4): per incident mass, `c_L(m) = c_R(m) = p_𝔇 |π_P^{-1}(m)| / |𝒞_A|` for `m ≠ ∅`,
  with `p_𝔇` the detection probability of the declared cell set, so `K_P = P = 0`;
  `f_∅ = |π_P^{-1}(∅)| / |𝒞_A|`; `K_C = 0`.
- *Two-cell coincidences*: `P(s_1 = s_2 = 1) = p_1 p_2`, so the anticorrelation parameter of G1 §7.2 is
  `α = 1`.

**What it settles.** PLAN-G's H-1 asked whether the setting-conditioned detection law on K1 under the
counting measure is uniform (PLAN-G:185–194). At the derived level the answer is stronger and does not
use K1: for G1's instance every compared law is the fixed product law above, independent of the
protocol, the encoding, the geometry, the slice form, the rule and the carrier's dynamics. The screen
may still be correlated with the tick-0 carrier content (R1 in CALC §1.7's derived sense, where the
screen is not masked); that content is not a record held at `t_c`, so the correlation does not appear
in any compared law.

**Pressure test** (the result is unfavourable to route A, and is tested for over-reach):
- *`μ`.* "Derived" also admits "a law PC-1's fork rule fixes within the OI premises" (U1 §2.3), and
  the fork "is not resolved" (MR★:642). Theorem G2-2 covers `μ-G` only.
- *Shared factors.* Records reading overlapping factors can be dependent. G1 §2.1 declares disjoint
  observers, and its screen cells are distinct sites; a declaration in which a herald and a detection
  read the same factors is not G1's (§10, AW-G2-1).
- *Joint hold.* H-rec is U1's G4 with its joint-hold clause (U1's [P], accepted). A record not held at
  `t_c` enters only as R-seq or a conditioned representation (K-4).
- *Finiteness.* For the compact value groups MR★:464 allows (`ℤ_p`, `ℝ/ℤ`), Haar measure is
  preserved by the K1 step, a continuous automorphism, and (a) holds with it [A-inf]; the counting
  measure itself needs A1.
- *No counted miss.* At the derived level a6's sorted channels show "fringes absent" under G1 §5.7's
  rule, against the sources' "fringes and antifringes" (targets typed in G1 §5.4, LIT 1.6–1.8). It is not a counted
  miss: the carrier-preparation input of a6 is unsourced (G1 §4.2; the PC-1 fork above), and on K1
  the herald's retention is unsourced (U1 C-RET). Where a herald retains the carrier's prepared value
  in `V_E`, Lemma G2-1(b) makes the screen independent of that value, so R1 at the screen fails for
  it and C-REC is the failing input: a "not available" at that scope, not a miss (§4.2).

### 1.3 The two detection rules at the derived level

- `I^part`: the product law with `p_j = |C_j| / |𝒞_{D_j}|`, a dark law fixed by the declared click
  classes (G1 §5.2, "the declared partition fixes a dark law"), now shown for every protocol and
  encoding, with independent cells.
- `I^rdy`: undefined without a screen preparation; with one heralded and held in `V_E`, the same product
  form with `p_j = 1 − r_j`. The two instances then give laws of the same form with different
  constants, and are reported separately (G1-A2).

### 1.4 Controls for §1

| # | Check | Could it fail? | Result |
|---|---|---|---|
| G2-C1 | Lemma G2-1 on a rule that is not K1: two binary cells, `φ(a, b) = (a, a + b)` over `ℤ/2`. The four states map to `(0,0), (0,1), (1,1), (1,0)`: uniform, so `a` and the new `b` are independent | yes: a repeated image would make the law non-uniform and the cells dependent | holds |
| G2-C2 | Countercontrol for the `μ-G` hypothesis: the same map with `b` fixed at `0` (a blank, not `μ-G`) gives `(a, a)`, perfectly correlated | yes: it shows the hypothesis is needed | correlated, as required |
| G2-C3 | Theorem G2-2 against CALC Theorem 1(a) with `λ` uniform: `Y_A` uniform on the union of the cosets `M_t x + K_t` over uniform `x`, which is `R_A` since `im M_t + K_t = R_A` (CALC Theorem 1(b) proof) | consistency check; cannot fail independently | holds |

***

## 2. Record spaces, incident events and masses on K1

### 2.1 The record space (G1 §3.1) on K1

[proved here, from MR★ and G1's definitions] For `V_A` of `k` sites, `𝒞_A = (ℤ/q)^{2k}` under A-reg
and `(ℤ/q)^k` under A-cur. A single-site cell `D_j` has `𝒞_{D_j} = (ℤ/q)²` (A-reg) or `ℤ/q` (A-cur).
- `s`: the declared detection map per cell (§4).
- `m`: `π_P` or `π_C` on `𝒞_A`, with `∅` among the values.
- `z`: `ζ(Y_{V_Z}(t_c))`. On K1, `Z`'s content radiates (S-L1; MR★ §S.3 σ1, `Z` row), so the held value
  at `t_c` is a record of the use-tick value only if retained (C-RET, unsourced; U1:590–599).
- `e`: no heralding process exists on K1 (MR★:639 [NP]); the visible herald is a read at the
  preparation tick (OA1:328 via U1:284), which enters `e` at `t_c` only if retained. Natively, all mass
  is at `e = ⊥`, and `(a, E)`, `(a, ¬E)` have mass 0 by specification (G1 §3.1; U1 G5).
- `ℓ`: no executing process writes a mark (MR★:639 [NP]); every mark has mass 0 by specification.

So natively `𝓡^full` carries its mass on `𝓢 × 𝓒_A × 𝓩 × {⊥} × {no mark}`. A blocked flux cannot be
booked as loss: no process writes the mark (it bears on a2, a3 and the auxiliary protocols, §2.2).

### 2.2 E-set: G1-F3 settled on K1

**Proposition G2-3 (no selected operation on an affine rule)** [proved here]. Let `φ^t` be affine on
`S = ⊕_X S_X`, the declared factors being direct summands, and let `π_Y` be a homomorphism. For every
pair of nonempty disjoint factor sets, selector `Z′` and carrier `C`, every readable `Y`, every tick
`t`, every fixed value `r` of the remaining factors and every selector value `z`, the partition of
`S_C` induced by `s_C ↦ π_Y pr_Y φ^t(s_C, z, r)` is the coset partition of `ker(π_Y pr_Y Φ^t_{YC})`.
It depends on neither `z` nor `r`. Hence no operation is I-sel in U1 §4.3's sense.

*Proof.* A homomorphism on a direct sum is the sum of its restrictions, so
`π_Y pr_Y φ^t(s) = F(s_C) + G(z) + H(r) + c` with `F = π_Y pr_Y Φ^t_{YC}` a homomorphism. The nonempty
level sets of `s_C ↦ F(s_C) + w`, for any fixed `w`, are the cosets of `ker F`. `□`

*Scope.* K1 under both slice forms, by H-K1 (CALC's re-derivation of S-L1); every R-lin member whose
`t`-step map is affine in the declared factors (OA-1 D5's form, "Every record is
`H_O r_O + H_P c + H_U u + const`", OA1:176–193 via U1 [M-r]). This is the content of U1's factor-set
reading ("An affine map restricted to any pair of disjoint factor sets keeps this property", U1 §4.3,
[A-inf] there), now proved at this scope. *Countercontrol (G2-C4):* on the non-additive σ12 members
native-Y and G-ring, S-C1(a) fails by instance (SIG §3, C-1, C-2): the proof must use affinity, and it
does, in its first line.

**Consequence for G1-F3** [proved here]. On K1 under the global reading, blocking a path, switching the
marker coupling, and a `φ`-effected read switch are not available as settings of one program, at every
slice form, `μ`, geometry and tick: each needs the induced partition to differ between two setting
values. U2 §11.1 counts such negatives "only once" U1's factor-set reading is verified; on K1 that
condition is met by Proposition G2-3 once this note is reviewed. The negative remains conditional on
the global reading of P-vii (#1234). For the scoped reading see §7.

**Proposition G2-4 (the setting record's effect on the screen law, relative to a declared `μ`)**
[proved here]. Under H-K1, H-μ and H-acc, let `W := (Y_D, Y_Z)` at `t_c`. By CALC Theorem 1(a) applied
to `D ∪ Z`, `W` given `s_Σ = x` is uniform on `M^W x + K^W`. Let `K_0 := {d : (d, 0) ∈ K^W}`. If `Z` is
carrier-masked (`pr_Z K^W = R_Z`), there are a homomorphism `τ : R_Z → R_D / K_0` and a homomorphism
`c` of the carrier content, both fixed by geometry and tick, such that

    Y_D given (s_Σ = x, Y_Z = z) is uniform on c(x) + τ(z) + K_0,

and, since `Y_Z` is then uniform and independent of `x`, `Y_D` given `(x, ζ(Y_Z) = a)` is the average
of these laws over `z ∈ ζ^{-1}(a)`.

*Proof.* For `(d, k) ∈ K^W`, the class of `d` modulo `K_0` depends only on `k`: two such `d` differ
by an element of `K_0`. This defines `τ` on `pr_Z K^W = R_Z`, a homomorphism since `K^W` is a
subgroup. The fibre of `M^W x + K^W` over `z` is `M^D x + τ(z − M^Z x) + K_0`; take
`c(x) := M^D x − τ(M^Z x)` modulo `K_0`. The uniform law on a coset conditions to the uniform law on
each fibre. `□`

So for each exact setting record value the screen law is a translate of one carrier-dependent coset
law; at the level of operations nothing is selected (Proposition G2-3). Where `τ ≠ 0`, the setting
record and the screen share background, and a declared class `ζ^{-1}(a)` acts as a herald on that
background: classes with different images under `τ` average different sets of translates, so the
screen's carrier dependence can differ between setting values, through the declared partition `ζ`
and not through `φ`. That is a conditioning effect (PLAN-G's H-8), and it books nothing as loss, so it
does not meet a2's specification. If `Z` is not carrier-masked, conditioning on the setting record also
selects carrier contents. Where `D ∪ Z` meets Theorem G2-5's hypothesis, `K^W = R_D × R_Z`, `K_0 = R_D`
and the setting record has no effect on the screen law. The setting record's mass is
`μ(𝔈_a) = Σ_x λ(x) |ζ^{-1}(a) ∩ (M^Z x + K^Z)| / |K^Z|`; under `μ-G`, `|ζ^{-1}(a)| / |R_Z|`, positive iff
`ζ^{-1}(a) ≠ ∅` (C-SET's "positive mass", derived).

### 2.3 E-prep

[proved here, from S-L1 and independence] Under E-prep, `𝔄_a` is an event `{s_P ∈ B_a}` on a
preparation region `P` at the preparation tick (tick 0, without loss, since `μ-G` is `φ`-invariant).
Conditioning `μ-G` on `𝔄_a` replaces `P`'s law by `U_{B_a}`, a law independent of the carrier:
CALC Theorem 1′'s setting. Its mass is `μ(𝔄_a) = |B_a| / |S_P|`; for a point preparation of `M` cells
of `𝐑 = ℤ/q`, `q^{−M}` (OA-1 D3's cost, OA1:156–160 via U1), with the failed mass `1 − q^{−M}` at
`(a, ¬E)` (G1 §3.2).
- *Readable law at `D`.* `Y_D = M^D s_Σ + Σ_{X≠Σ} π_D Φ^t_{DX} s_X` (S-L1, re-derived in CALC §0),
  with independent summands, so `D`'s law given `x` is `ν^D_a(· − M^D x)`, with `ν^D_a` the convolution of the
  images of the independent non-carrier laws. A change of `P`'s preparation changes `ν^D_a` through
  `P`'s image alone. This is U4 r3 §2.1's "Beyond H-μ" [A-inf], proved here directly, so the statement
  is not PROVISIONAL.
- *When it changes nothing.* If the sites Theorem G2-5 uses at `D` lie outside `P` and are uniform,
  `D`'s law is uniform for every `a`. Under A-cur, if `B_a` constrains current slices only,
  Theorem G2-6 makes every readable law at a later tick independent of `a`.
- *At the derived level.* With the attempt label held at `t_c` in `V_E` (G1 §3.2), Theorem G2-2 makes
  every compared law on `V_D`, `V_A`, `V_Z` independent of `a`. Without it held, the law conditioned on
  `𝔄_a` is a representation (U1 §2.1; K-4), and on K1 the retention is unsourced.
- *Which protocols.* E-prep encodes only a4-type marker preparations; a1 ("coupling absent", G1-A4) is
  not realized (G1 §4.2, PROVISIONAL on U4 §2.1).

**Blocking by a prepared content, the independent case** (G1 §4.2's "not classified" row, narrowed)
[proved here]. For a prepared law independent of the carrier, `D`'s law given `x = x_L + x_R` is
`ν(· − M^D x_L − M^D x_R)`. It is free of `x_R` for every `x_R` iff `ν` is invariant under translation
by `im(M^D restricted to the R-path content)` (Theorem 1′ applied at `D`). Such a law makes the R path's
contribution noise at `D`; it does not remove it, and books nothing as loss. So it does not meet a2's
specification ("that flux booked as loss", G1 §2.3). A prepared content correlated with the carrier
under `μ` (C-9's caveat, MR★:1433–1437) stays not classified.

### 2.4 E-read

Unchanged from G1 §3.3. Theorem G2-2 adds that at the derived level the three laws a4–a6 are
`P_D ⊗ (π)_* U_{𝒞_A}` times `μ(𝔈_*)`.

### 2.5 `κ_norm`

[proved here] On K1, with no herald process (MR★:639 [NP]), the incident mass is `μ(𝔈_a)`, unless the
visible-herald route of G1 §4.2 is used with a retained herald (unsourced): E-set
`|ζ^{-1}(a)| / |R_Z|` under `μ-G`, or Proposition G2-4's sum relative to a declared `μ`; E-prep
`|B_a| / |S_P|`; E-read `μ(𝔈_*)`, the same for each protocol it encodes. Counts per incident mass at the
derived level are `p_j` for every protocol (Theorem G2-2). On K1 nothing is a particle: "per incident
particle" means per unit of the incident event's `μ`-mass, the reading G1 §5.3 fixes.

***

## 3. The screen's coset law, relative to a declared `μ` (H-1 for a declared two-path geometry)

G1 §4.2's screen row: "the screen's law given carrier `x` is uniform on `M^D_t x + K^D_t` under μ-G"
(CALC Proposition 2.8(i)), "a single-tick dependence on the carrier exists where `K^D_t ≠ R_D`; whether
it does for a declared two-path geometry is G2's (H-1)."

### 3.1 Theorem G2-5 (far-side masking) [proved here]

*Hypotheses:* H-K1 in any dimension `d ≥ 1`; a declared `μ` under which the content of a set `U` of
sites (both slices) is uniform and independent of all other content (under H-μ, `U ⊇ Σ^c`); a set `D`
of sites, a tick `t ≥ 1` and an axis direction `e = ±e_c`. **(NW)** `2t < L_{c′}` for every axis `c′`,
and the sites used below lie in a box with fewer than `L_{c′}/2` consecutive residues along every axis.

(a) **A-cur.** If `D − te ⊆ U`, then `Y_D(t)` (the current slice of `D` at `t`) is uniform on `R^D` and
independent of all tick-0 content other than the current slices at `D − te`; in particular `K^D_t = R_D` and `D`'s law does not
depend on the carrier, for every carrier law.

(b) **A-reg.** If moreover `D − (t−1)e ⊆ U` and no two sites of `D` differ by `e`, the same holds for
both slices of `D`.

*Proof.* (a) The coefficient of `y_p` in `u_t(w)` is `U_t(A)_{w,p}`. On `ℤ^d` it vanishes unless
`|w − p|_1 ≤ t` (`U_t` has degree `t` in `A`). Under (NW) the torus coefficient between sites of the
box equals the lattice one: a translate `k ≠ 0` has some `k_{c′} ≠ 0`, and then
`|Δ_{c′} − k_{c′}| ≥ L_{c′} − |Δ_{c′}| > L_{c′}/2 > t`. For `p = v − te` and `w, v ∈ D`,
`(w − v)·e + t ≤ |w − v + te|_1 ≤ t` forces `(w − v)·e ≤ 0`, and equality forces `w = v`. So the matrix
`[U_t(A)_{w, v−te}]_{w,v ∈ D}`, ordered by the `e`-coordinate, is triangular, with diagonal
`U_t(A)_{v, v−te} = 1` (CALC Proposition 2.6's coefficient). It is invertible over `ℤ/q`, so the map
from the variables `(y_{v−te})_{v∈D}`, which are distinct, uniform and independent of everything else,
onto `Y_D(t)` is a bijection for every value of the other content. (b) Take the coordinates `(s′, w)`,
`s′ ∈ {t − 1, t}`, `w ∈ D`, of `(u_{t−1}(D), u_t(D))` and the variables `y_{v − se}`; they are distinct
because no two sites of `D` differ by `e`. A nonzero coefficient of `y_{v−se}` in `u_{s′}(w)` needs
`w·e − s′ ≤ v·e − s`, with equality only if `v − se = w − s′e`, the same variable. Ordered by the key
`v·e − s`, the matrix is triangular with unit diagonal (`u_0 = y` for `s′ = 0`). `□`

The masking variable is the content on the side of `D` away from `e`'s tip, at axial distance `t`: it
reaches `D` at the same tick as any content at distance `t` on the other side, with coefficient 1.

### 3.2 The declared two-path geometry

[proved here, from Theorem G2-5] Take the screen in a plane transverse to `e_1`,
`D ⊆ {k : k_1 = h}`, and the source `Σ` and the path regions `P_L`, `P_R` at `k_1 > h`, with uniform
content at `k_1 < h` (H-μ; or any declared `μ` that leaves that half uniform). Then `D − te_1` and
`D − (t−1)e_1` lie at `k_1 < h`, no two sites of `D` differ by `e_1`, and under (NW):
- **`K^D_t = R_D` under both slice forms, at every `t ≥ 1`, for every carrier law `λ`**, including
  assumed point preparations of the two paths, and whether or not `P_L`, `P_R` are themselves prepared.

So for this geometry H-1's subgroup is the whole screen group, relative to every declared `μ` that
leaves the far side uniform. Contrapositively, a carrier-dependent screen law needs, for **every**
axis direction `e`, some site of `D − te` with non-uniform content (carrier, or a quiet region entered
as a `μ`-datum) under A-cur; under A-reg, for a single-site cell `v`, some non-uniform site among
`v − te`, `v − (t−1)e`, for every `e`. The screen must be surrounded. This
places MR★ C-3's quiet ready region (MR★:1344–1359 [NP]) geometrically: it must cover the screen's far
side, not only the carrier. Beyond (NW) (ticks of half a side or more) nothing is decided here.

**The same theorem at the marker** [proved here: Theorem G2-5 with `A` in place of `D`]. A marker
region `A` with uniform content at `A − te` (and at `A − (t−1)e`, with no two sites of `A` differing
by `e`, for A-reg) is completely masked at `t` under (NW): `K_t = R_A`. CALC-F2's failures of masking
lie outside these hypotheses: Instance 1.2's marker is surrounded by the carrier, and Instance 1.1
fails (NW). [A-inf] This bears on D-1's (β) (U4 §3.2, PROVISIONAL) by giving a sufficient geometric
condition for complete masking; whether a declared marker is surrounded is part of (γ)'s mapping.

### 3.3 A surrounded screen: coset law and additive cancellation [instance]

CALC Instance 1.2 read with the single-site region at `0` as a screen cell `D_1 = {0}` (CALC
Proposition 2.8(i) is Theorem 1 applied at `D`): `d = 3`, `L ≥ 5`, `Σ = {k : 1 ≤ |k|_1 ≤ 2}`, `t = 2`,
`q = 5`. Then `u_2(0) = 5y_0 + f(s_Σ) = f(s_Σ)`, so under A-cur `K^D_2 = 0` and the readable value is
`f`. With CALC's pair `L: x_{−e_1} = 1` and `R: y_{2e_1} = 1`, `f = −1` and `f = +1`; with both
contents, `f = 0`. Under `κ_det^part` with `C_1 = ℤ/5 ∖ {0}` the cell clicks with probability 1 for
each one-path content and 0 for both: complete cancellation. With `C_1 = {1}`: `0`, `1`, `0`.
- Each content is a different carrier law, so each is a different declared `μ`, hence a different
  model (U1 G3). The three laws are reported per model and never combined (NC-γ3); no within-instance
  `Δ` is formed from them (§6.3).
- The cancellation is the additive (classical-field) interference of S-L1 at the level of the coset
  law, with all-or-nothing clicks for point contents, as CALC Theorem 1(c) gives at the marker.
- Under A-reg the readable pair is `(u_1(0), u_2(0))` with `K^D_2 = 𝐑 ⊕ 0`; a click class read on the
  current coordinate gives the same values.

### 3.4 Controls for §3

| # | Check | Could it fail? | Result |
|---|---|---|---|
| G2-C5 | Direct expansion on a ring `ℤ/L`, `L ≥ 7` (instance of the algebra, not the native graph): `Σ = {1, 2}`, `D = {0}`, `t = 2`. `u_2(0) = y_{−2} + y_0 + y_2 − x_{−1} − x_1` and `u_1(0) = y_{−1} + y_1 − x_0`. Theorem G2-5 (`e = +e_1`, variables `y_{−2}`, `y_{−1}`) predicts masking in both forms | yes: if `y_{−2}` had a non-unit coefficient, or `y_{−1}` entered `u_2(0)`, (a) or (b) would fail | `y_{−2}` has coefficient 1 in `u_2(0)` and is absent from `u_1(0)`; `y_{−1}` has coefficient 1 in `u_1(0)` and is absent from `u_2(0)`: masked in both forms; holds |
| G2-C6 | Native `d = 3`: Instance 1.2 with `L ≥ 7` (for (NW)) and `Σ′ := Σ ∩ {k_1 ≥ 0}`, `t = 2`, `e = +e_1` (variables `y_{−2e_1}`, `y_{−e_1}` now uniform). Prediction: masked in both forms, for every `q` | yes: CALC's direct expansion could show `y_{−2e_1}` absent from `u_2(0)`, or `y_{−e_1}` present with a coefficient that breaks triangularity | `f` contains `y_{−2e_1}` with coefficient 1 (CALC Instance 1.2); `u_1(0) = Σ_{j∼0} y_j − x_0` contains `y_{−e_1}`; `y_{−e_1}` is absent from `u_2(0) = (A² − I)y − Ax` at `0`, since `(A²)_{0,−e_1}` counts the walks of two unit steps from `0` to `−e_1`, and two unit steps never sum to a unit vector on a torus with sides `≥ 4`: holds |
| G2-C7 | Non-prediction where CALC finds a proper subgroup: Instance 1.2 itself (`±2e_c, ±e_c ∈ Σ` for every `c`) and Instance 1.1 (`L = 4`, `t = 2`, so `2t < L` fails) | yes: if the hypothesis held there, Theorem G2-5 would contradict CALC's `K_2 ≠ R_A` | the hypothesis fails in both: holds |
| G2-C8 | §3.3's values over `ℤ/5` from CALC's `f` | yes: `f(L + R) ≠ 0` would refute the cancellation | `−1 + 1 = 0`: holds |

***

## 4. The two detection rules, separately

### 4.1 `I^part` (readout partition, no ready reference)

- *Derived level* (Theorem G2-2): independent cells, `p_j = |C_j| / |𝒞_{D_j}|`, for every protocol and
  encoding. **Comparable** law, setting-independent clicks, as G1 §5.2 anticipated, now for every rule.
- *Relative to a declared carrier `μ`-datum, one-sided geometry* (§3.2): the same dark law for every
  `λ`; R1 fails at the screen, so C-REC for the screen is not available at that `μ`'s scope.
- *Surrounded geometry* (§3.3): click mass `|C_j ∩ (M^{D_j} x + K^{D_j})| / |K^{D_j}|` given `x`; for
  point contents and `C_j` a union of `K^{D_j}`-cosets, 0 or 1. Joint cells: CALC Theorem 1(a) applied
  to `D`, with joint coset `M^D x + K^D`; cells are dependent where `K^D` is not a product (§5, §6.4).

### 4.2 `I^rdy` (departure from a ready value), and G1-F4

G1-F4: "`κ_det^rdy` needs a prepared screen. On the counting-measure route (γ→) is unsourced at C-PREP;
on the visible-herald route the preparation is native at the D3 cost and the first missing step is the
herald's retention to `t_c` (C-RET)." Three routes:

1. **Counting-measure route.** Unchanged: no ready region (MR★:642 [NP]); unsourced at C-PREP.
2. **Visible-herald route.** Narrowed in two ways.
   - *Retention in `V_E` does not help* [proved here; A1; any rule]. G1 §2.1 holds the herald in `V_E`,
     disjoint from `V_D`. If the herald is retained to `t_c` there, Theorem G2-2 makes the screen's
     `t_c` law the product dark law with `p_j = 1 − r_j`, the same with or without conditioning on it;
     by Lemma G2-1(b) the screen is independent of any prepared value the herald retains. So C-RET is
     not the only missing step: under G1's declaration, at the derived level, the route yields the dark
     law, not a carrier-dependent detection law. Read under U1's outcomes, C-REC's R1 at `t_c` for a
     property the herald retains is disproved, so the route is **not available** for a detection law
     that depends on the herald-certified preparation, at that scope (`μ-G`, G1 §2.1's disjoint
     observers, H-rec). Without retention the route is unsourced at C-RET and its
     conditioned law is a representation.
   - *Under A-cur the ready value is erased in one tick* [proved here; K1]. Theorem G2-6 below.
3. **Declared `μ` with ready cells as `μ`-data** (U1:275, :524–525). Available relative to `μ` (G1
   §4.2). Two conditions from this note: the ready data must cover the screen's far side at the
   readout distance (Theorem G2-5 with `U` the unready set); under A-cur they must include hidden
   previous slices (Theorem G2-6). For a screen read only at `t_c`, retention of the screen record is
   C-RET with `t_1 = t_2 = t_c`, which U1:553–556's readback clause meets trivially [A-inf, a reading of
   U1]; G1 §4.2's remaining blocker, "R1's persistence on K1", then bears only on records first held
   before `t_c`.

**Theorem G2-6 (A-cur: one-tick erasure of current-slice preparations)** [proved here]. *Hypotheses:*
H-K1, A-cur, and a declared `μ` under which the previous slices are independent and uniform and
independent of the current slices (for example `μ-G` conditioned on any event of the current slices at tick `t_0`, which
is every visible-herald event at one tick under A-cur). For any set `D` of sites and `t ≥ 1` with (NW)
for `D ∪ (D − (t−1)e)` and some axis direction `e`, the current slice of `D` at `t_0 + t` is uniform on
`R^D` and independent of every tick-`t_0` current slice.

*Proof.* `u_t = U_t(A) y − U_{t−1}(A) x` (CALC §0). At `t = 1`, `u_1 = A y − x` with `x` uniform and
independent of `y`. For `t ≥ 2` the coefficient of `x_{v−(t−1)e}` in `u_t(w)` is `−U_{t−1}(A)_{w,
v−(t−1)e}`; Theorem G2-5(a)'s triangularity argument with `t − 1` in place of `t` gives a triangular
matrix with diagonal `−1`, a unit. The variables `x_{v−(t−1)e}` are uniform and independent of all
current slices, so the map onto `u_t(D)` is a bijection for every value of the rest. `□`

Consequences:
- A screen prepared by a visible herald at `t_0` under A-cur is uniform at every later tick within
  (NW), whatever the carrier: `κ_det^rdy` then gives the dark law `p_j = 1 − r_j`. At `t_c = t_0` every
  herald-executed run reports no departure.
- The same holds for a carrier prepared by a visible herald under A-cur: its current-slice content
  reaches no readable region at a later tick within (NW). U1's "visible carriers native at the D3 cost"
  (U1:284 [M-r]) stands as a preparation; on K1 under A-cur its prepared content leaves no trace in
  later readable records.
- So on K1 under A-cur, the visible-herald route is not available for a ready screen or a
  carrier-dependent screen at `t_c > t_0`, independently of retention, at the scope of the hypotheses.
  Any K1 detection law that depends on a preparation under A-cur needs a `μ`-datum on hidden previous
  slices. [A-inf] This is the dynamical form of S-L7's single-time restriction (MR★:613–615, [NP]).

*Consistency with CALC.* Instance 1.2 under A-cur holds `f(s_Σ) + 5𝐑`, and `f` contains `−Σ_{j∼0} x_j`; with
the carrier's previous slices uniform, as Theorem G2-6 assumes, `f` is uniform (G2-C9, below). CALC
assumes a carrier law on both slices, which under A-cur includes a hidden-slice preparation.

| # | Check | Could it fail? | Result |
|---|---|---|---|
| G2-C9 | Theorem G2-6 against CALC Instance 1.2 (A-cur, `t = 2`): the record `f` must contain a previous-slice carrier variable with a unit coefficient | yes: an `f` free of `x` would hold information that Theorem G2-6 says is erased | `f` contains `−x_j`, `j ∼ 0`, coefficient `−1`: holds |
| G2-C10 | Theorem G2-6 at `t = 1` against CALC Instance 1.1's `u_1(i) = y_{i−1} + y_{i+1} − x_i` | yes | `−x_i` with coefficient `−1` at every site: holds |

**G1-F4, as narrowed** [proved here, at the stated scopes]. On the counting-measure route,
unsourced at C-PREP. On the visible-herald route: under A-cur on K1, not available for `t_c > t_0`
(Theorem G2-6); under either form and any rule, with the herald retained in `V_E` per G1 §2.1, the
screen's `t_c` law is the dark law (Theorem G2-2); without retention, unsourced at C-RET. Under a
declared `μ` with ready data: available relative to `μ` where those data cover the far side (and, under
A-cur, hidden slices). Under SNR-1 the two "not available" items count only at their scopes, only
after review, and the global reading of P-vii conditions the K1 one.

***

## 5. NC-copy's slot: `K_P` on K1 (G1 §7.1)

G1 §7.1: "For two point-prepared paths the K1 marker's marginal is all-or-nothing (CALC Theorem 1(c));
whether `K_P` on K1 is then 1 or `P` also depends on the conditioning on a screen detection, which
couples the background images at `A` and at `D`, and is G2's."

**Proposition G2-7 (`K_P` is a functional of the joint coset law)** [proved here]. Under H-K1, H-μ with
point carrier contents `x_L`, `x_R` for the programs `b(L)`, `b(R)` (each a declared `μ`, [assumed]),
CALC Theorem 1(a) applied to `A ∪ D` gives `(Y_A, Y_D)` given `x_π` uniform on `M^{AD} x_π + K^{AD}`,
and

    c_π(m) = |{(α, δ) ∈ M^{AD} x_π + K^{AD} : π_P(α) = m, δ ∈ C}| / |K^{AD}|,

per unit incident mass, with `C` the declared detection set. Hence:
- (i) *Product background* (`K^{AD} = K^A × K^D`): `c_π(m) = P(π_P(Y_A) = m | x_π) · P(Y_D ∈ C | x_π)`;
  conditioning on detection does not change the marker law, and at equal detected masses `K_P` is the
  total-variation distance between the two marker laws. If `M^A(x_L − x_R) ∉ K^A` and `π_P` is
  constant on cosets of `K^A` and separates `q^A(x_L)` from `q^A(x_R)` without `∅`, then `K_P = 1`
  (the marker's class is deterministic given `x_π`, CALC Theorem 1(a)). If the pair is masked at `A`,
  `K_P = |w_L − w_R| = P` (G1 §2.4, check 3).
- (ii) *Shared background:* `K_P` can differ from every marker-only statistic; the instance below has
  `K_P = 1` with the marker completely masked.
- (iii) *Far-side masked:* where `A ∪ D` meets Theorem G2-5's hypothesis, `(Y_A, Y_D)` is uniform for
  both contents and `K_P = P = 0`.
- (iv) *Derived level:* `K_P = P = 0` (Theorem G2-2).

*Proof.* The displayed formula is the conditional law of the joint coset. (i): the uniform law on a
product coset is a product. (iii): Theorem G2-5. (iv): §1.2. `□`

**Instance (shared background)** [instance; a ring, an instance of the algebra, not the native graph].
CALC Instance 1.1 (`Λ = ℤ/4`, `Σ = {3, 0}`, A-reg, `t = 2`) with its marker region split into a marker
`A′ = {1}` and a screen cell `D′ = {2}`, over `ℤ/2`, with CALC's pair `L: y_3 = 1`, `R: y_0 = 1`. Declare
the marker report `m := u_1(1)` and the detection `u_2(2) = 1`.
- From CALC's expansions, `u_1(1) = y_0 + y_2 − x_1` and `u_2(2) = y_2 + 2y_0 − x_1 − x_3`. Their
  non-carrier parts are equal, `y_2 − x_1`, so `u_1(1) − u_2(2) = x_3 − y_0`.
- `A′` alone receives `(y_2 − x_1, y_1 − x_2)`, and `D′` alone `(y_1 − x_2, y_2 − x_1)`: both are uniform,
  so the marker and the screen cell are each completely masked; each path gives the marker law
  `(1/2, 1/2)` and the detection probability `1/2`.
- Jointly: under `L`, `u_1(1) = u_2(2)`, so every detected run reports `m = 1`; under `R`,
  `u_1(1) = u_2(2) + 1`, so every detected run reports `m = 0`. Then `c_L = (m = 1 : 1/2)`,
  `c_R = (m = 0 : 1/2)`, and `K_P = (1/2 + 1/2)/(1/2 + 1/2) = 1`, while the marker-only statistic is 0.

**What fills the slot** [proved here; the comparison with a1 is PROVISIONAL].
- On K1, `K_P` reads the joint record of the marker and the screen. It equals the marker's own path
  knowledge only when the background at `A` and at `D` is a product (i). The Wootters–Zurek reading of
  `K = 2L − 1` as knowledge held by the marker (G1 §2.4; LIT 1.12 via G1) presupposes that the marker
  and the detection are independent given the path, which is the product case: assumption-watch marker
  **AW-G2-2** (§10).
- NC-copy's law (`K_P = 1` with the fringe intact) is met in case (i) with an unmasked marker pair:
  `D`'s law does not depend on any marker declaration (CALC Proposition 2.8(i)), which is the
  non-invasive "CC1 kind" of S-L5 (MR★:592–593 [NP]). "Fringe intact" compares a4 with a1, and a1
  ("coupling absent") is another geometry on K1 (G1 §9, O11; PROVISIONAL on U4 §2.1). So `K_P² + V² > 1`
  is not formable within one instance on K1.
- Case (ii) reaches `K_P = 1` without any marker record. It is not NC-copy: there the path knowledge is
  in the marker; here it is in the marker–screen pair.

| # | Check | Could it fail? | Result |
|---|---|---|---|
| G2-C11 | The instance by direct expansion from CALC's `u_1(i)`, `u_2(i)` | yes: different non-carrier parts at `A′` and `D′` would make the background product, and then `K_P = 0` | `y_2 − x_1` at both: `K_P = 1`; holds |
| G2-C12 | Proposition G2-7(i) on the same ring: `m := u_1(1)`, detection `u_1(2) = 1`. Their non-carrier parts `y_2 − x_1` and `y_1 − x_2` share no variable, so the background is a product and the masked marker predicts `K_P = 0` | yes: a shared variable would allow `K_P > 0` | direct: `u_1(1) = y_0 + (y_2 − x_1)`, `u_1(2) = y_3 + (y_1 − x_2)` are independent and uniform under both contents, so `c_L = c_R` and `K_P = 0`; holds |

***

## 6. Required controls: C0's `Δ` and PC-wave (G1 §7.1)

The controls specify their own detection event, so their images are the same in `I^rdy` and `I^part`;
the instances differ only for native laws.

### 6.1 C0, with and without background [proved here]

G1 §7.1: C0 "has `Δ ≡ 0`, since `δ_blk` has no detection", and its required result is to fail "whenever
the target's `Δ` differs from 0". G1 §5.4: "`κ` compares the model's law with the background added as
stated in the source", and §5.1 applies `κ` identically to control laws. Add an independent
carrier-free dark detection of probability `b_j` per run at cell `j`. With C0's screen responses
`r_1(j) + r_2(j) = r_{12}(j)`,

    Δ_j = [1 − (1−b)(1−r_{12})] − [1 − (1−b)(1−r_1)] − [1 − (1−b)(1−r_2)]
        = −1 + (1−b)(1 − r_1 − r_2 + r_{12}) = −b_j,

for every response. So, through `κ` with §5.4's background rule, **C0's image has `Δ_j = −b_j`**, and
its required result reads: C0 fails whenever the target's `Δ` differs from `−b_j` under `κ_cmp`. With
no background this is G1's statement. A raw-direct `Δ` that differs from 0 by dark counts alone does not
fail C0. G1's text is consistent once §7.1's "`Δ ≡ 0`" is read as the background-free case; this note
changes no definition (§13, question 1).

### 6.2 PC-wave [proved here]

With fields `f_L(j)`, `f_R(j)`, a square-law detector of efficiency `η` in the linear regime and an
independent dark probability `b_j`: `Δ_j = (1 − b_j) η · 2 Re(f_L(j) \overline{f_R(j)}) − b_j`. It differs
from C0's `−b_j` wherever the cross term is nonzero, and, without background, at four cells per fringe
period it gives G1 §5.7 check 4's classification "fringes present". So the two required controls are green on the
fringe statistics, with the background treated alike: C0 fails, PC-wave passes.

### 6.3 The native laws against the controls

- *Derived level* (Theorem G2-2): any three laws of the product form give `Δ_j = −p_j`, which is C0's
  image with zero response and `b_j = p_j`. The native derived-level law is a member of C0 with dark
  counts: it reproduces nothing C0 does not (OCP:34–36, "a native law that C0 also reproduces gains
  nothing"). It also has `α = 1` (§1.2).
- *Within one instance on K1* `Δ` is not formable: no program of the instance meets a2's or a3's
  specification (Proposition G2-3; §2.1, no loss mark; §2.3), as G1 §5.7 records for the one-path
  normalizer ("not tested").
- *Per model, surrounded screens* (§3.3): the coset laws give all-or-nothing clicks and complete
  cancellation. As laws they are not C0's, but they are an additive classical field with a
  group-valued click class. On `𝒜_10`'s observables no observable is established to separate PC-wave
  (G1 §7.4: PC-wave is separated only by X-2, which lies outside `𝒜`), so `S(PC-wave) = ∅` there and,
  under OCP:45 and the owner's Q6 answer, such a result is at most "interference compatible with
  classical coherent waves; no quantum completion". It rests on assumed carrier contents and on
  laws from different declared `μ`.

### 6.4 A remark on X-2 (outside `𝒜_10`), for G3 and G5 [instance]

PC-wave's bound `α ≥ 1` (G1 §7.2) uses detections that are conditionally independent given the field.
§5's instance read as two output cells (`u_1(1)` and `u_2(2)`, click on value 1): under `R` exactly one
cell clicks in every run, `P(both) = 0` and `α = 0`; under `L` both or neither, `α = 2`; under `μ-G`,
`α = 1` (§1.2). So an additive classical field whose two outputs share uniform background reaches
`α = 0` for one assumed point content. This is G1's AW-hyb realized by the K1 algebra: a classical
model outside `𝒦` that is particle-like on X-2. It is an instance on a ring with an assumed preparation,
not a coverage result and not a beam-splitter geometry (**AW-G2-3**).

***

## 7. The scoped reading and value groups (owner Q7)

- **Lemma G2-1 and Theorem G2-2** use only bijectivity, `μ-G`, H-obs and H-rec: they hold on every σ12
  member (native-Y, G-ring, and any member of form SIG (2.1)) as on K1. At the derived level the
  compared laws are the product law under either reading of P-vii.
- **Propositions G2-3, G2-4 and Theorems G2-5, G2-6** use additivity. On native-Y and G-ring, S-C1(a)
  and S-L5's structural part fail by instance (SIG §3, C-1 to C-3), and CALC Theorem 1(a) "does not
  apply" (SIG §3). They are not claimed there; the σ12 outcome stays unsourced or not classified (G1
  §4.2), pending #866.
- **Value groups.** §§2–6 use `𝐑 = ℤ/q` (CALC's H-K1). The triangularity arguments hold over any
  commutative ring in which the diagonal entries `±1` are units, so over `ℤ_p` and `ℝ/ℤ` with Haar
  measure in place of the counting measure [A-inf].

***

## 8. Outcomes per protocol, on K1 under the global reading

U1's outcomes; "law" names what the executable part of the program gives. Every row is reported per
slice form, per `κ_det` instance and per `μ`, never combined (NC-γ3).

| Protocols | Derived level (`μ-G`) | Relative to a declared carrier `μ`-datum, far side uniform | Surrounded screen, declared `μ` |
|---|---|---|---|
| a1, a4–a6 (E-read for a4–a6) | law: the product dark law (Theorem G2-2), both instances; carrier preparation unsourced (PC-1 fork) and, on the herald route, not available under G1 §2.1 at its scope (§4.2); outcome **unsourced** | law: the dark law for every `λ` (Theorem G2-5); C-REC's R1 at the screen not available at that `μ`'s scope; outcome **unsourced** (the quiet far-side region, MR★ C-3) | coset laws of §3.3 type; classical-field interference; `S(PC-wave) = ∅` on `𝒜_10`; never combined across `μ` |
| a2, a3, a2P, a3P, a2C, a3C as E-set settings | **not available** (Proposition G2-3), at K1 scope, after review; conditional on the global reading | as derived | as derived |
| the same as programs of other geometries | outside `I` (G1 §9, O11) | outside `I` | per model only |
| a1 vs a4 by E-prep | a1 not realized (G1-A4; PROVISIONAL on U4 §2.1); a4 variants give equal compared laws when the label is held at `t_c` (§2.3) | equal screen laws where the far side lies outside `P` (§2.3) | `ν^D_a` differs through `P`'s image (§2.3) |
| `K_P`, `K_C` | `0` (`= P`) | `0` (`= P`) where `A ∪ D` is far-side masked | joint-coset functional (Proposition G2-7); within one instance only through O11 |

No protocol reaches *available* with every input derived. No counted miss arises (§1.2, pressure test).

***

## 9. What this shows for (γ), and what it does not

- **(γ→), route A, derived level.** For G1's instance the compared laws are one product dark law for
  every protocol, encoding, geometry, slice form and rule (Theorem G2-2). Route A at the derived level
  therefore carries no setting, marker or herald effect: PLAN-G's "(γ) on K1 under the counting measure
  reduces to preparation sourcing" holds, and is sharpened: the missing input is a non-uniform law (a
  `μ`-datum or the unresolved PC-1 fork law), since a herald retained in another observer cannot supply
  it (Lemma G2-1(b)).
- **Relative to a declared `μ`.** A carrier `μ`-datum alone does not suffice for a carrier-dependent
  screen in a source-in-front geometry: the far side must also be non-uniform (Theorem G2-5), and under
  A-cur the data must sit on hidden previous slices (Theorem G2-6). Where they do, the K1 laws are coset
  laws with additive interference, of classical-wave type on `𝒜_10`.
- **D-1** stays undecided at (γ) (U4 §3.3). Nothing here decides whether the partition a screen reveals
  corresponds to observed fringes, or whether any K1 configuration corresponds to a performed apparatus.
- **(γ←).** Not addressed beyond the observation that, on `𝒜_10`, no K1 result found here separates
  PC-wave (§6.3).

***

## 10. Findings and assumption-watch markers (§A.31)

**Productivity test, fixed before the walk:** a gem is a fact strictly stronger than the obvious
restatement that either constrains (γ) or exposes an assumption. Favourable readings were
pressure-tested: Theorem G2-2's apparent counted miss on a6 (§1.2) and §3.3's cancellation (§6.3).

| # | Finding | Check | Class |
|---|---|---|---|
| G2-F1 | At the derived level, for G1's instance, every compared law is one product dark law, for every rule, slice form, geometry, encoding and protocol; a herald, setting or attempt label held at `t_c` by another observer changes no law on `V_D`, `V_A` (Lemma G2-1, Theorem G2-2) | §1; G2-C1 to G2-C3 | NEW in its consequences (D2 and Gap 1 are its special cases): H-1 settled at the derived level without K1 |
| G2-F2 | G1-F4's visible-herald route is not repaired by retention: a herald retained in `V_E` leaves the screen's `t_c` law the dark law, and makes the screen independent of the value it retains (monogamy) | §4.2 | NEW: exposes that G1-F4 placed the missing step at C-RET |
| G2-F3 | On every affine rule with direct-summand factors, no operation is I-sel (Proposition G2-3); on K1 each exact setting record value acts on the screen law by translation, and a coarse setting class can act only as a conditioning on background the setting region shares with the screen (Proposition G2-4) | §2.2; G2-C4 | POSITIVE: verifies U1's factor-set reading at the affine scope; settles G1-F3 on K1, pending review; the conditioning effect is ELABORATING (H-8) |
| G2-F4 | Far-side masking: uniform content at axial distance `t` behind a screen masks it at `t`, both forms, for every carrier law (Theorem G2-5); every source-in-front two-path geometry has `K^D_t = R_D` | §3; G2-C5 to G2-C8 | NEW: H-1 answered for declared two-path geometries; places MR★ C-3's quiet region geometrically |
| G2-F5 | Under A-cur on K1, any preparation confined to current slices is erased from every later readable record within (NW) (Theorem G2-6) | §4.2; G2-C9, G2-C10 | NEW: the visible-herald route fails under A-cur independently of retention |
| G2-F6 | `K_P` conditioned on a detection reads the joint marker–screen coset; with shared background it reaches 1 with the marker completely masked (Proposition G2-7, instance) | §5; G2-C11, G2-C12 | NEW: fills NC-copy's slot; exposes AW-G2-2 |
| G2-F7 | Through `κ` with §5.4's background rule, C0's image has `Δ_j = −b_j`; the derived-level native law is C0 with dark counts | §6.1, §6.3 | NEW (control statement): C0's required result is relative to the stated background |
| G2-F8 | Surrounded K1 screens show additive cancellation with all-or-nothing clicks for point contents | §3.3 | CONFIRMING (S-L1 at the coset-law level) |
| AW-G2-1 | Derived-level correlations between records need records that read shared factors; G1 §2.1's disjoint observers exclude them | §1.2 | marker for G5 and any OI coincidence observable (X-2, X-4, X-5) at the derived level |
| AW-G2-2 | Reading `K = 2L − 1` as marker knowledge presupposes marker and detection independent given the path | §5 | marker for G3 (Schwindt's T-block counts) and G5 |
| AW-G2-3 | PC-wave's `α ≥ 1` needs detections conditionally independent given the field; a classical field with shared background reaches `α = 0` (instance) | §6.4 | marker for G1's AW-hyb, G3's X-2 and G5's credit set |

**Cross-propagation.** G2-F1 and AW-G2-1 apply to every derived-level OI claim about a joint law of
records held by disjoint observers at one tick, including U2's coverage half and #914 row 17c. G2-F4
applies to the marker (D-1's (β), §3.2) and to MR-1's screen. G2-F5 applies to every A-cur preparation
route on K1.

**Fixed point.** This is one bounded pass; §A.31's fixed-point criterion is not claimed.

***

## 11. Not decided

- Ticks beyond (NW) (half a torus side or more), where wrap-around enters; Theorem G2-5 and
  Theorem G2-6 make no statement there.
- A-reg screens with two sites differing by `e` in Theorem G2-5(b) (the variables coincide).
- Correlated carrier–background `μ` (C-9's caveat), including blocking by a correlated prepared content.
- Whether the derived level's PC-1 fork law, if fixed, avoids Theorem G2-2.
- Sorted-fringe laws (a6) on surrounded geometries with shared background: the joint coset of
  `A ∪ D` under a two-path content is not computed here.
- a6-delayed: the marker's retention to `t_c` (C-RET); CALC Theorem 2(d) makes every joint-law return
  global, and nothing here adds to it.
- The orbit-frequency reading (G1 §5.6): every law here is a κ-ens object; κ-orb is G4's.
- Every σ12 statement beyond §7's first item.

## 12. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it is attached to here | Classification |
|---|---|---|
| G1 r4 at `6ab9515d` | every definition used (`𝓡`, `𝔈_a`, encodings, `κ`, `K_P`, controls, G1-F3, G1-F4) | support off `main` (gap); accepted, c.6892563291 |
| CALC r2 at `6ab9515d` | Theorem 1(a)–(c), 1′, Propositions 1.4, 2.6 (coefficient), 2.8(i), Instances 1.1, 1.2 | support off `main` (gap); reviewed ACCEPT; accepted, c.6892224647 |
| U1 r5 | criterion, levels, AD-1, C-PREP, C-REC, C-RET, C-INT classes; OA-1 quotations | support off `main` (gap); accepted, c.6891241282 |
| U4 r3 | every PROVISIONAL item (§2.3 a1, §5 comparison with a1, §8 a1 row) | support off `main` (gap); accepted; U4-dependent results stay conditional |
| SIG r2 | §7, G2-C4 | support off `main` (gap); accepted as a partial screen |
| U2 r3 | the SNR-1 counting condition (§2.2) | support off `main` (gap); accepted |
| PLAN-G r1 | H-1, H-8, the route A framing | provenance and context; plan not reviewed |
| #1169 c.6893331779, c.6893456888, c.6892563291, c.6892224647; #1305 | authorization, A1, acceptances | governance |

Every statement resting on an [OFF], [NP] or PROVISIONAL row carries that gap. This note is itself
off `main` and unreviewed; nothing in it counts under SNR-1 before its review.

## 13. Owner questions, and what later units can use

1. **C0's background clause.** Should G1 §7.1's required result for C0 be read against `−b_j` (§6.1),
   as G1 §5.4's background rule implies?
2. **Observer declaration.** Theorem G2-2 shows that under G1 §2.1's disjoint observers no derived-level
   law shows any cross-record dependence. Is that declaration to be kept as the instance for (γ), with
   this consequence reported, or is a variant with records reading shared factors to be defined as a
   separate instance (NC-γ5: declared beside, not replacing)?
3. **Routing.** Should Theorem G2-5's marker corollary (§3.2) and G2-F5 be routed to #866 for D-1's (β)
   and MR-1's screen, and AW-G2-2 and AW-G2-3 to G3?

**For G5:** §8's table, §9, G2-F1 to G2-F8 and the three markers. **For G3:** AW-G2-2 (whether
Schwindt's T-block analysis assumes marker–detection independence) and AW-G2-3 (X-2). **For G4:** none
beyond §11's κ-orb item.

Nothing here authorizes G3–G5, a calculation, or any change of Issue, plan or manuscript.
