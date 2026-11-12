# TUNE-1, Step 2, session 2: rerun of C-POS-2 under addendum 1

**WIP / UNVERIFIED research record.** This reruns C-POS-2 alone, as the owner decided (PR #1237
comment 6822699905). It is a paper derivation; no interpreter was run. No manuscript or Lean file
is changed and no premise is adopted.

**Governing text:**
- the proposal at `e676c42a` (sha256 `2a081101…7499fd5`);
- `TUNE-1-STEP2-AMENDMENT-1-final.md` at `75dfb6d4`;
- `TUNE-1-STEP2-AMENDMENT-1-final-addendum-1.md`, which carries this record's commit.

The derivations are [W]. The per-history continuation bound of `finite-a2-v5/REPORT.md`:205–243
[R] is as read in session 2 §2.3, which the independent review of session 2 confirmed.

## 0. Plain summary

The finite qubit controller (C-POS-2) is checked again with its Bloch-ball precision counted the
way the owner decided. Only preparations that leave two rounds for testing count. The control now
behaves as its row states in every entry, including composition (Q4).

The reviewer's example menu, at horizon 3, confirms two things:
- the new precision is met;
- the old precision would fail inside a window now proved by hand.

All seventeen M1 controls are therefore green, so session 2 is clean. The linear-rule analysis still
waits for independent review of this rerun.

## 1. Expected entries (final B6.1 item 4, with addendum D2)

- **Scope:** separating menus, with the menu's `c₀` and `L = 2`. Session 2 §2.3 shows that `L = 2`
  suffices, and the review agreed.
- **Q3′:** `ε ≥ b + K g`.
- **Q2 and Q5′:** `ε ≥ b + δ`.
- **Q6′:** `ε ≥ b + δ_{K−2}`, posed for `K ≥ 3`.
- **Q1:** on its range.
- **Q4:** proved directly.
- **D-clauses:** D3, D5, D6 and D7 fail.
- **Token:** `OPERATIONAL-ONLY`.

## 2. Obtained

**Credited assignment.** Credit `σ_r` as the ideal conditional state: `R_w v` after a reset or read
along `v`, or the ideal preparation if no read has occurred. The per-history bound holds under
world weights: each history's continuation record is within (reads)`·κ ≤ hκ ≤ b` of the
menu-ideal quantum continuation.

- **Q5′, `F(ε; 𝒯_R)`.** Reads are exact Lüders in the menu ideal, so the error is at most `b`.
  Obtained at `ε ≥ b`, hence at `b + δ`.
- **Q3′, `F(ε; 𝒯_K)`.** Add at most `K` gate uses, each within diamond distance `2 sin(g/2) ≤ g` of
  its target (Main:596 [P]). Obtained at `ε ≥ b + K g`.
- **Q2.** The complete-record TV is at most `hκ ≤ b`
  (`finite-a2-v5/REPORT.md`:205–215 [R]). Obtained at `ε ≥ b`.
- **Q6′.**
  - (ii) holds with the menu's `c₀`.
  - Take a prefix of horizon at most `K − 2` ending at the nearest `R_w n` to `ψ`. Its credited
    mean is that pure state, at trace distance at most `δ_{K−2}` from `ψ`.
  - Its credited error on `𝒯_2` is at most `b + g ≤ b + δ_{K−2}`, since `g ≤ δ_{K−2}` by definition.
  - **Heralded witnesses** (when `v` is a read eigen-direction). Final B1.2 admits a heralded
    witness only with credit on `𝒯_K`. For a witness of length `ℓ`, the tests can then run to
    `K − ℓ` rounds with up to `K − ℓ − 1` gates before a read, giving error up to
    `b + (K − ℓ − 1) g`. The witness is therefore padded [W]:
    - After the heralded read along `v`, repeat the same read `K − 2 − ℓ` times, heralding on
      agreement, then apply the word `w`. The witness is still `R_w v`, now of length `ℓ = K − 2`.
    - In the menu ideal, a Lüders read along `v` leaves `v` unchanged and agrees with probability 1.
      In the world each repeat agrees with probability at least `1 − κ` (:205–215 [R]), so
      `p_acc ≥ p⁰_acc (1 − Kκ) > 0` for `Kκ < 1`, where `p⁰_acc > 0` is the unpadded witness's acceptance. The value of `p_acc` and the trial count `1/p_acc` are
      reported as final B4 requires.
    - The per-history bound applies after the last fresh reset, whatever the herald. Each history's
      continuation is therefore within (reads)`·κ ≤ hκ ≤ b` of the ideal continuation from `R_w v`,
      so the credit holds at conditional error at most `b` against the menu ideal.
    - At `ℓ = K − 2`, every test in `𝒯_K` that fits has at most 2 rounds. Only a gate followed by a
      read lets a gate change the record law, so the target-against-menu cost is at most `g`.
    - The credit on `𝒯_K` therefore holds at error at most `b + g ≤ b + δ_{K−2}`.
  - Obtained at every `ε ≥ b + δ_{K−2}`, for `K ≥ 3`, with heralded and unheralded witnesses alike.
    The stated constant is unchanged. For `K ≤ 2` it is not posed. At `K = 3` no padding is needed,
    since `ℓ = 1 = K − 2`.
- **Q1.**
  - Lower half: two antipodal prepared states, read along their axis. The ideal TV is 1, and each
    world law is within `b`, so the world TV is at least `1 − 2b`. This holds at `ε ≥ b + δ_1`,
    where `δ_1` is the distance to the nearest antipodal pair in the menu.
  - Upper half: from Q2, by the three-state bound (session 1 §2.3.1), for `ε + b < 0.05`.
  - No heralded witness is needed. The range is that of the row.
- **Q4, proved directly.**
  - Take `π₁ = (prefix, c(θ₁), c(θ₂), continuation)` and
    `π₂ = (prefix, c((θ₁+θ₂) mod 2π), c(0), continuation)`. The continuation does not read the
    gate records.
  - World against the menu ideal: at most `hκ ≤ b` for each protocol.
  - In the menu ideal, replace each of the four gate instances by its exact target rotation. Each
    replacement costs at most its diamond distance `g` (Main:596 [P]). Menu rotations produce no
    outcome, and the target's gate records are trivial.
  - For exact rotations about `n̂`, `Ad U_{θ₂} Ad U_{θ₁} = Ad U_{θ₁+θ₂} Ad U_0`, since `Ad U` has
    period `2π`. So the two protocols then give equal laws for the non-gate records.
  - Total: `TV ≤ 2b + 4g`. If the menu contains the identity, `c(0)` is exact and the bound is
    `2b + 3g`.
  - Obtained: Q4 at every `ε ≥ 2b + 4g`.
- **D-clauses.** D3 fails (hemisphere law supplied), D5 fails (preparation cone and workspace
  isolation), D6(a) fails (rotation primitives), and D7 fails (finite controller carrier, not a
  lattice interface) (`history-architecture-v5/REPORT.md`:305–312 [R]; `finite-a2-v5/REPORT.md`
  :1–8 [R]).
- **Token.** `OPERATIONAL-ONLY`.

**Status: green.** Every expected entry is obtained.

## 3. Check: the reviewer's menu at `K = 3`

**The menu:**
- preparations `±z`;
- rotations about `z` and about `x` by multiples of `2π/m`, so `g = π/m`;
- reads along `z` and `x`.

**The target:**
- `n̂ = z`, `a = z`, `b = x`, so `a·b = 0`;
- `c(θ)` is the nearest rotation about `z`.

**Separation.** "Read `z`" reaches `z`, and "rotate about `z`, then read `x`" reaches the `xy`-plane.
So `c₀ = ½ min_{|x|=1} max(|x₃|, (x₁² + x₂²)^{1/2}) = 1/(2√2)`, with `L = 2`.

At `K = 3`, a Q6′ preparation has `ℓ ≤ 1`. Two accountings of the initial state are checked.

- **(B) A free initial preparation `±z` at clock 0.**
  - At `ℓ ≤ 1`, the reachable ideal pure states are:
    - the `yz` great circle, at resolution `2π/m`, from one `x`-rotation;
    - `±z`;
    - `±x`, from one `x`-read, heralded with `p_acc = ½` and credited by the per-history bound.
  - So `δ_1 = max(π/m, sin(π/8) + O(m^{−2})) ≈ 0.383` for `m ≥ 9`. This is the trace distance from
    `(x + y)/√2` to its nearest reachable state, at Bloch angle `π/4`, up to the `O(m^{−2})` from the
    circle's resolution.
  - **New form.** Q6′ is expected at `ε ≥ b + 0.383` and obtained there (§2). Green.
  - **Proved failure** (addendum D3).
    - `C_1 = conv(yz circle ∪ {±x}) = {|u| + (v² + w²)^{1/2} ≤ 1}`.
    - `ψ = (1, 1, 0)/√2` lies at Bloch distance `(√2 − 1)/√2 ≈ 0.293` from it, so
      `D_1 ≥ 0.293`.
    - Q6′ fails for `ε < (0.354 · 0.293 − b − g)/1.707 ≈ 0.0607 − 0.586(b + g)`.
    - This is below `b + 0.383`, so it does not conflict with the new form.
  - **Old form.** At horizon 3, `R_z R_x z` reaches every direction to resolution `O(1/m)`, so
    `δ_3 = O(1/m)`. The old entry "Q6′ at `ε ≥ b + δ_3`" is therefore false on the non-empty interval
    `[b + O(1/m), 0.0607 − 0.586(b + g))`, for large `m` and small `b`. This confirms session 2's
    red for the old form, with the proved window.
- **(A) The preparation `±z` counted as a round, with an initial mixture on the `z`-axis.**
  - Let the initial mixture have Bloch vector of length `r₀ < 1` on the `z`-axis.
  - At `ℓ ≤ 1` the reachable pure states are `±z` (preparation or `z`-read) and `±x` (`x`-read). One
    rotation of the initial mixture stays in the `yz` disk of radius `r₀`.
  - So `δ_1 = sin(π/4) ≈ 0.707`, the trace distance from `y` to the nearest of `±z` and `±x`.
  - `C_1 = conv({±x, ±z} ∪ yz disk of radius r₀)`. Its points have `y`-coordinate at most `r₀`, so
    `D_1 ≥ 1 − r₀`.
  - Q6′ provably fails for `ε < (0.354 (1 − r₀) − b − g)/1.707`, which is
    `≈ 0.207 − 0.586(b + g)` at `r₀ = 0`.
  - **New form.** Expected at `ε ≥ b + 0.707` and obtained there. Green. The failure bound lies below
    it.

In both accountings the new form is met. The check is consistent with the addendum's proved failure
bound, and with session 2's finding that the old form fails.

## 4. Corrections to the session-2 record

These are the changes the session-2 review required. They are recorded here; `TUNE-1-STEP2-SESSION2.md`
is left unchanged as the reviewed object.

- **F2.** Session 2 §2.3's window `[b + δ_K, b + δ_{K−2})` is withdrawn. It is replaced by addendum
  D3's proved bound and §3's concrete case.
- **F1.** The final amendment should have restated C-POS-2's `δ` under decision 5 when it adopted
  that decision. Addendum D2 does so.
- **Nit.** In session 2 §4, "wait for two things" should read "wait for three things".
- **C-ISO-2.** Its constant `10^{-3}` is not tight. The review estimates about `1.9 × 10^{-3}` with
  `γ` re-derived, and the row's `7 × 10^{-4}` holds a fortiori.

## 5. Session 2 status

| Control | Status |
|---|---|
| C-SUP-1, C-SUP-2, C-POS-1, C-ISO-1, C-ISO-2, C-FIN, C-TAB, C-B1, C-CARD, C-MEAS, C-EXACT | green (session 2) |
| C-REBIT; C-NULL in exchange mode and in initial-condition mode | green (session 2) |
| C-REP, C-PROG, C-PROG-P | green (session 2) |
| C-POS-2 | green (this rerun, under addendum 1) |
| Proves-too-much check; two-way check of the encoder test | green (session 2; C-POS-2's entries use `δ_{K−2} ≥ δ`, so they are unchanged) |

**Session 2 is CLEAN.** Every control under the governing text is green, and no token other than
the controls' own classifications is computed.

**Gate (final B9; owner comment 6822699905).** L5/M3, its child nodes, the re-derivations of Lemma A
and Lemma F, and R-nl do not start until this rerun has passed independent review and then the
ChatGPT review.

## 6. Disclosure

- **Commands:** `git` (rev-parse, status, add, commit, push), `curl` (GitHub API reads of PR #1237
  comments), `cat`, `grep`, `sed`, `wc`, `sha256sum`. No interpreter was run, and all arithmetic was
  done by hand.
- **Read:** the session-2 review (in full, including its r2 section on this rerun); owner comment 6822699905; the governing texts. Review G1 (credit on `𝒯_K` for heralded Q6′ witnesses) is closed in §2, and G2 in addendum 2.
