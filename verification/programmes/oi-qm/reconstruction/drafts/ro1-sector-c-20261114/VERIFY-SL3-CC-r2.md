# Independent paper verification: MR★ S-L3 and countercontrols CC4, CC5, CC7 (r2)

## 0. Header

**Purpose.** A paper-only independent verification of four items that S3-PLAN-r9 carries as named
premises: MR-1 stage 1's lemma S-L3, and the countercontrols CC4, CC5 and CC7 of MR★ §M.6 (S3's
M-1, M-2, M-3). For each item the record states what is claimed, checks it by hand, traces its
dependencies, and returns one of VERIFIED, VERIFIED AT NARROWER SCOPE, NOT VERIFIED or REFUTED.
Nothing here is upgraded beyond what the checked argument reaches.

**Revision.** r2 applies every finding (F1–F7) of the independent review of r1
(`REVIEW-VERIFY-SL3-CC-r1.md`, ACCEPT WITH CHANGES; PR #1294 at `c2da5530`). r1 is kept unchanged.
The disposition of each finding is in `RESPONSE-VERIFY-SL3-CC-r1.md`.

**Authorization.** Issue #1169, comment 6891189024 (account `amaybaum`, 2026-11-15T07:39:57Z), item
4: "a paper-only check of MR-1's S-L3 (erasure unavailable on K1) and of MR★ §M.6's controls CC4,
CC5 and CC7, at their recorded scope"; "No MR-1 stage 2, no computation, and no running of the
controls"; "Until that record is reviewed and accepted, the four items stay named premises."

**Standing of this record.** Until this record is itself reviewed and accepted, the four items stay
named premises (the authorization's own condition). This record changes no file on `main`, no
Issue and no status.

**Sources, read at `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b`.**

| Short name | Path | Blob | Last commit touching it |
|---|---|---|---|
| MR★ | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md` | `45af1678` | `cccd69cd` |
| PREREG | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md` | `c36fb14b` (identical to the frozen `1a236f33` blob) | `cccd69cd` |
| LOG | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/stage1-log.json` | at `75cc5100` | `cccd69cd` |
| PC★ | `verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/amendments/PC-star.md` (§PC★2a, P-1 to P-3) | `79aad250` (identical at `99dce4b6`, the commit MR★ cites) | — |
| O-OBSMU | `verification/programmes/oi-qm/reconstruction/observer-interface-obsmu-20261104/ANALYSIS.md` | at `75cc5100` | — |

Line numbers `MR★:N`, `PREREG:N`, `LOG:N`, `PC★:N` refer to those blobs.

**Off-`main` references, classified (§A.42 item 8).**
- S3-PLAN-r9 and S3-U1-r5 (drafts under
  `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/` on the RO-1 working
  branch): provenance; read only to identify how the items are used.
- PR #1023 c.6554399670 (owner decision freezing `K★ = {K1}`): support on `main`; its content is
  quoted in MR★ §K★.F (MR★:327–416).
- PR #1023's relayed review of `fc68d333` (MR★:1297–1300; LOG:773): provenance only; not used as
  evidence.

**Verifier independence.** This verifier authored neither MR-1's preregistration, MR★, nor any of
their amendments or review records, and did not take part in the review of `fc68d333` whose relayed
report is the items' only recorded verification. Every step below was re-derived from the source
text.

**Method and limits.** Paper reasoning only. No computation, simulation, enumeration, script, Lean
or numerical evaluation was run; the small finite laws below were worked by hand. No repository file
was edited.

***

## 1. S-L3 — "time reversal is representable, not available; proved here"

### 1.1 What is claimed (MR★:517–530)

With `σ(x, y) = (y, x)` on `S = 𝐑^Λ × 𝐑^Λ` and the K1 step `φ(u_prev, u) = (u, A u − u_prev)`,
`(A u)_i = a Σ_{j∼i} u_j` (MR★:464–466; frozen as `K★ = {K1}` at MR★:355–360):

- (L3a) `ψ = σφσ`, where `ψ(x, y) = (A x − y, x)` is the inverse of `φ` (PC★ P-1).
- (L3b) `σ` is not a time shift: `σ ≠ φ^k` for every integer `k`. Hypotheses used: `a` injective on
  `𝐑`, a nonempty neighbour relation.
- (L3c) "No region executes `σ` on another (S-C1(a))."
- (L3d) On finite `S`, `φ^{−1} = φ^{N−1}` with `N` the order of `φ`, so the inverse is executed only
  as a global wait acting on every region, the observer included (S-L6).

"Not available" is relative to MR-1's frozen availability standard (PREREG:190–196; restated
MR★:451–457): an operation counts only if it is a finite composition of `φ`-steps on the declared
state, under the declared access, with a sourced setting. S-L2 (MR★:511–515) records the
consequence: the available transformations of the joint state are the time shifts `φ^n`, `n` within
the budget; observer-side choices change only which region and tick are read.

### 1.2 Step-by-step check of S-L3 as stated

**(L3a).** `φ(y, x) = (x, A x − y)`, so `σφσ(x, y) = σ(x, A x − y) = (A x − y, x) = ψ(x, y)`.
Checked. P-1 (PC★ §PC★2a): `ψ(φ(u_prev, u)) = ψ(u, A u − u_prev) = (u_prev, u)` and
`φ(ψ(x, y)) = φ(A x − y, x) = (x, y)`. Checked; it uses no property of `A`.

**(L3b).** Suppose `σ = φ^k`. Then `σ` commutes with `φ`, and with `σ² = id`,
`φ^{−1} = σφσ = φσσ = φ`, so `φ² = id`. Directly,
`φ²(x, y) = φ(y, A y − x) = (A y − x, A(A y − x) − y)`. The first component gives `A y − x = x` for
all `(x, y)`; `x = 0` gives `A y = 0` for all `y`, so `A = 0`. MR★'s route (`y = 0` gives `2x = 0`,
then `A y = 2x = 0`) is also valid. Hence `A ≠ 0` implies `σ` is no time shift. Checked.

*`A ≠ 0` under the stated hypotheses, within frozen K1.* Frozen K1 defines `A` as PC★2a's relation
sum, "`a·Σ_{j∼i}`" (MR★:358–359; PC★:102–106, whose examples include "`(ℤ/L)³` with six nearest
neighbours"). That sum counts each neighbour `j` of `i` once. If `j ∼ i` and `r ∈ 𝐑` is nonzero,
`(A(rδ_j))_i = a·r ≠ 0` by injectivity. So MR★'s stated hypotheses imply `A ≠ 0` within frozen K1,
on every side length. Checked.

*Boundary case under a different stencil reading.* If `A` is instead read with SM's form lemma, which
sums the `2d` neighbouring values `x_1 + ⋯ + x_{2d}` (SM:224–226 at `5914c17c`) as a multiset of
offsets `±e`, then on a torus of side 2 in every axis each distinct neighbour is counted twice and
`A = 2a·(relation sum)`. This vanishes exactly when `2a` annihilates `𝐑`; among `ℤ/q`, `ℤ_p`
(p-adic, torsion-free) and `ℝ/ℤ` with `a` injective, that is `𝐑 = ℤ/2` only. There `A = 0` and
`φ(x, y) = (y, −x) = (y, x) = σ(x, y)`, so `σ` is a time shift. With any axis of side `≥ 3`,
`A ≠ 0`. Under this multiset reading, and only under it, the operative hypothesis is `A ≠ 0` rather
than "nonempty relation". The case does not affect S-L3 within frozen K1, which uses the relation sum.

**(L3c).** MR★ supports (L3c) by S-C1(a) (MR★:498–503). Checked in that sense: by S-L1
(MR★:491–496; from additivity, PC★ P-2), region `X`'s content at time `t` is
`Φ^t_{XX} s_X + Σ_{Z≠X} Φ^t_{XZ} s_Z`, with every `Φ^t_{YX}` fixed by `(t, X, Y)`. So the map on
`s_X` is `Φ^t_{XX}`, fixed by `(t, X)` and selectable by no region; every other region contributes
only an additive offset. No region's content can make `σ` (or any other map) the one applied to `X`.
S-L1 checked: `φ^t` is additive and `s = Σ_X ι_X s_X`.

**(L3d).** `φ` is a bijection (P-1); on finite `S` it has finite order `N` and `φ^{−1} = φ^{N−1}`.
Every available operation is some `φ^n` (S-L2), which acts on all of `S`. Checked. On infinite `S`
(`ℤ_p`, `ℝ/ℤ`) the finite-`S` bullet does not apply, and (L3b) holds unchanged.

### 1.3 This record's supplements (not part of S-L3's proof)

The following are this verifier's additions. MR★ does not contain them, and S-L3 as stated does not
need them. They are credited to this record, not to S-L3.

- **(Sup-1) Global block-form reading of (L3c).** No global map of block form `τ = σ_X ⊕ g`, with `X`
  a proper nonempty region and `g` any map on the complement, is a time shift. *Proof.* Suppose
  `τ = φ^n`; then `τφ = φτ`. Pick `i ∈ X`, `j ∉ X` with `j ∼ i` (exists for a proper nonempty `X` in a
  connected graph such as the native cubic torus), `r ≠ 0`, and `s = (0, rδ_j)`. Since `s_X = 0`,
  `(τ s)_X = 0`, so the previous slice of `φ(τ s)` on `X` is `0`. But `φ s = (rδ_j, A rδ_j)` has
  `X`-part `(0, (A rδ_j)|_X)` with `i`-entry `a r ≠ 0`, and `σ_X` moves it to the previous slice. So
  `τφ s ≠ φτ s`. If `X` is a union of connected components, (L3b) applied to `X` alone covers it when
  `A|_X ≠ 0`. The argument uses no linearity of `g`.
- **(Sup-2) Inverse of a marking within budget.** An `m`-step evolution `φ^m` is inverted by an
  available `φ^n` only if `ord(φ) | n + m`. With budget `T` and `T + m < N` (the budget below
  recurrence of MR★ §M.1, MR★:857–865, and S-L6) no available operation inverts it.
- **(Sup-3) Marginal reading, not covered by S-L3 or by (Sup-1).** "A region executes `σ` on `X`" can
  also mean: for a fixed content `c` of the complement, `pr_X φ^n(s_X, c) = σ_X(s_X)` for all `s_X`,
  the complement being free to change. By S-L1 this holds iff `Φ^n_{XX} = σ_X` and
  `Φ^n_{X,X^c}(c) = 0`. That case occurs within frozen K1. Take `𝐑 = ℤ/2`, `a = 1`, a cubic torus,
  `X = {i}` (both slices), `n = 1`: `Φ^1_{XX}(x_i, y_i) = (y_i, −x_i) = (y_i, x_i) = σ_X(x_i, y_i)`,
  and the cross term `(0, a Σ_{j∼i} c_{cur,j})` vanishes whenever the neighbours' current slice is
  `0`. So one native tick swaps a one-site region's two slices under a zero-current-slice
  neighbourhood (likewise for any independent set of sites; over a general `𝐑` the block is the
  twisted swap `(y, −x)`). This contradicts no bullet of S-L3: no region selects `σ` (S-C1(a)), and
  the global map is not of block form (Sup-1). It gives no erasure: reversing a marking needs the
  inverse on the record's whole support, which spreads (S-C4a). It shows that "no available
  operation applies `σ` to a region's content" is false within frozen K1. This record does not
  decide whether `Φ^n_{XX} = σ_X` can hold for regions with internal edges or for `n ≥ 2`.

### 1.4 Dependencies and their status

| Dependency | Source | Status found here |
|---|---|---|
| K1 step and its freeze | MR★ §K★.F (MR★:327–416), owner decision PR #1023 c.6554399670 quoted there | frozen record on `main`; used as the defining hypothesis |
| P-1 (bijectivity, `ψ`), P-2 (additivity) | PC★ §PC★2a, blob `79aad250` on `main` | re-derived here; exact algebra for every abelian `𝐑`, integer `a`, any relation |
| S-L1, S-C1(a) | MR★:491–503 | re-derived here from P-2 |
| availability standard; S-L2 | PREREG:190–196 (frozen); MR★:511–515 | definitional consequence of the frozen standard; checked |
| finite order of `φ` (S-L6, first bullet) | MR★:595–597 | elementary (bijection of a finite set); checked |
| `a` injective, `A ≠ 0` | MR★:473–477 ("reading": `a = 1`); MR★:358–359; PC★:102–106 | `A ≠ 0` follows from MR★'s hypotheses under K1's relation sum |

No dependency of S-L3 as stated rests on an unverified record: its proof uses exact algebra on the
frozen step and the frozen availability standard. The relayed review report is not among its
supports here.

### 1.5 Verdicts

| Item | Verdict | Scope |
|---|---|---|
| **S-L3 as stated** (bullets L3a–L3d) | **VERIFIED** | `K★ = {K1}` with PC★2a's relation sum; MR-1's frozen availability standard via S-L2; `a` injective, a nonempty relation; any value group of PC★2a; (L3c) in the sense of its stated support S-C1(a) |
| **The authorization's gloss, "erasure unavailable on K1"** | **VERIFIED AT NARROWER SCOPE** | only in the sense: no available operation is `σ` (S-L3), a global block swap `σ_X ⊕ g` (Sup-1), or the inverse of a marking evolution within a budget below recurrence (Sup-2); and no region selects the map applied to another (S-C1(a)) |

**What is not verified under the gloss.**
- That no available `φ^n`, at `n` below `ord(φ)`, returns the carrier–marker preparation to one
  §5.3-equivalent over `Acc` to the pre-marking preparation (T3's sense, PREREG:485–487), whether by
  an `Acc`-relative or an orbit-level return.
- That the record cannot leave the marker by transport (by S-C4a it leaves every confined region).
  Transport relocates the record rather than erasing it, so this bears only on a marker-local reading
  of "uncomputation".
- That no available operation applies `σ` to a region's content in the marginal sense: (Sup-3) shows
  that it does, within frozen K1, without giving an erasure.

**The same narrowing binds MR★'s own uses of S-L3.** MR★ states "no subsystem undo exists (S-L2,
S-L3, S-L6)" (MR★:648 and MR★:1396), "any inverse executed on a subsystem (S-L3, S-L6)" (MR★:856),
and "subsystem inverses (S-L3, S-L6)" (MR★:1485). Read as claims about operational undo in T3's
sense, they go beyond what S-L3, S-L2 and S-L6 establish; at verified scope they cover the swap, the
exact inverse as a global wait, and (with this record's supplements) global block swaps and marking
inverses within budget. MR★ is frozen and is not corrected here (§A.42 item 6).

***

## 2. Common checks for the three countercontrols

**Specification sites.** MR★ §M.6 (MR★:1018–1074): Lemma G (MR★:1022–1042), the classical carrier
common to CC1, CC3, CC5, CC7 (MR★:1044–1058), the instance rows (CC4 MR★:1066, CC5 MR★:1067, CC7
MR★:1069); test menu §M.7 (MR★:1076–1124); T7 rules §M.8 (MR★:1126–1159); T8/T9 references §M.9
(MR★:1161–1188); C-8's pinned T7 references (MR★:1423–1431). Frozen obligations: PREREG:551–583, in
particular PREREG:552–554 (control separation "from PC-Q's law"), PREREG:559–560 (each instance
"fixed at stage 1 together with a paper proof that each admits a generalized-noncontextual model")
and the frozen rows (CC4 PREREG:571, CC5 PREREG:572, CC7 PREREG:574).

**Lemma G** (dependency of all three). Re-derived. Under (i) (point preparations and a complete
readout `RDALL` in `Acc`), equivalence of two preparations gives equal `RDALL` laws, hence equal
distributions; `δ_λ`, then a procedure, then `RDALL` returns `K(r, λ′ | λ)`, so equivalent procedures
have equal kernels. Under (ii), the mass `Σ μ(λ) K(r, λ′ | λ) e(λ′)` is bilinear and spanning sets on
both sides determine each `K(r)`. Checked. Reading needed for (ii) on a multi-bit `Λ`: "single
readouts" must include sequences of single-bit readouts on distinct bits, whose response functions
are products (a readout's disturbance acts only on its own bit, after it is read); with three bits and
`T = 8` such sequences fit in `Acc_ctrl`. Under that reading (ii) holds for CC4.

**PC-Q references used for separation** (checked as dependencies only). B-T1 at `θ = π/2`:
`|L0⟩ + |R1⟩`, orthogonal markers, `(V, D) = (0, 1)`. B-T2 (used for CC4's comparison): the three
laws of MR★ §M.5. B-T4: masses `(1 ± cos ϕ)/4` at `β = π/4`, `¼` at `β = 0`. B-T7: Bloch points
`(±√2/2, ±√2/2)`, antipodal pair mixtures both `I/2`, `V + P = √2 > 1`. Checked. PC-Q's W1 is reached
only after stage 2 checks Eqs. (10)–(11) against the source; if that check fails, stage 2 halts before
any T7 step (MR★:1145–1147). That check is not done. Every T7 separation decided at the verdict level
is conditional on it.

**The `separated` gap (specification gap common to all controls).**
- §M.11's schema records `control_separation: {test, separated}` (MR★:1233), and §M.7 says only that
  control separation "is decided by the named test, as in §M.6" (MR★:1122). No rule for computing
  `separated` is stated.
- The frozen text defines control separation as separation "from PC-Q's law" (PREREG:552). Under that
  law reading, a T7 separation is computable only where the control and PC-Q run the same T7
  protocols. CC4 runs `Q_{s₁s₂}` and PC-Q runs `P_{r,ϕ}`, which CC4 cannot prepare, so CC4's T7
  separation is not computable under the law reading (§3). Readings that do not compare laws (the W1
  verdict, or the derived `(P, V)` values) are not stated in the frozen text.
- The decision function's Row 0 (MR★:1243–1248) has no `control_separation` clause, while frozen
  0(i) makes "a countercontrol not separated where §5.8 requires" `VOID` (PREREG:592–593). Whether
  `reference_match` covers separation is not stated.

**Genuineness criteria applied.** A control is genuine here when its reference is computed from its
own primitives (not copied from the claimed formula or from PC-Q), it can fail under a plausible
implementation or mutation error, and its separating test distinguishes it from PC-Q.

***

## 3. CC4 — epistemically restricted classical field (S3's M-1)

### 3.1 What is specified (MR★:1066; frozen row PREREG:571)

Toy bits `(x, p) ∈ (ℤ/2)²`; valid states uniform on a coset of a one-dimensional subspace (six) or on
the whole space; carrier `x` = path, `p` = port; `PH(π)`: `p ← p + 1`; `MK_j(g)`:
`x_{M_j} ← x_{M_j} + g·x`, `p ← p + g·p_{M_j}`; ready marker `x_M = 0` known; readouts of `x`, `p`,
`x + p` with the toy disturbance; `TZ`, `RD_j(0)` = `x` readouts, `TX`, `RD_j(π/4)` = `p` readouts;
`DP`: `p ← p + f`; products of valid single-bit states prepared; GNC by Lemma G(ii); T7 quadruple
`Q_{s₁s₂} = ½ z_{s₁} + ½ x_{s₂}`. Reference: no W1, T7 quadruple certified, `V + P = 1`. Separated
from PC-Q by T7; T1 a consistency check. §M.9: passes every applicable T8 row; T9 undo is the
involution `MK₁(π/2)` in `Acc`.

### 3.2 Checks

- *Primitives.* `MK_j` is the toy CNOT, symplectic; applied twice it returns `x_M` and `p` (`p_M` is
  unchanged by `MK_j`), so it is an involution on the ontic state. `PH` and the three readouts map
  valid states to valid states. `DP` keeps states valid only if `f` is uniform: with a biased `f`, the
  state "`p = 0` known" goes to a non-uniform distribution on `p`, a convex mixture of valid states
  that the row's list of valid states does not contain. Checked.
- *Spanning identity.* `δ_{(x₀,p₀)} = (1{x=x₀} + 1{p=p₀} + 1{x+p=x₀+p₀} − 1)/2`: value `1` at
  `(x₀, p₀)`, `0` at the three other points. Each indicator is twice a pure-state distribution, and
  `1 = 1{x=0} + 1{x=1}`. So the six pure distributions span `ℝ⁴`, and the indicators are the
  readouts' response functions. Checked.
- *T7 reference.* Reading `z_s` as the pure state "`x = s` known" and `x_s` as "`p = s` known",
  `Q_{s₁s₂}` gives `⟨Z⟩ = ½(−1)^{s₁}` and `⟨X⟩ = ½(−1)^{s₂}`, so `P = V = ½` for all four members and
  `V + P = 1`. Antipodal pairs `{00, 11}` and `{01, 10}`: each pair mixture is
  `¼(z₀ + z₁ + x₀ + x₁)`, the uniform distribution, so the Eq. (11)-type equivalence holds at model
  level (equal distributions imply equal future laws). Certified; `1 > 1` is false; no W1. Checked.
  `Q_{s₁s₂}` is not itself a listed valid state (its distribution takes values `½, ¼, ¼, 0`); it is a
  declared mixture preparation, which the row defines explicitly.
- *T0, T1, T2, T3, T4, T8 (under the readings of §3.3).* With `P_bal` = "`p = 0` known, `x` uniform",
  `f` uniform and `g = [θ ≠ 0]`:
  - T0: T0-c(π, π) gives outcome 0 with mass 1; T0-d gives `½`. T0 positive.
  - T1: `MK₁(1)` sets `x_M = x` and `p ← p_M` (uniform), so `(V, D) = (0, 1)` at `θ = π/2` and
    `(1, 0)` at `0`, matching PC-Q, consistent with "T1 is a consistency check only".
  - T2: `P_bal, TZ, TZ`: `x` uniform, read twice, equal outcomes with mass `½` each.
    `P_bal, TZ, TX, TZ`: the first read randomizes `p`, `TX` is uniform and randomizes `x`, the last
    `TZ` is uniform: each triple `⅛`. `P_bal, TX, TZ, TX`: first outcome 0 with mass 1, then each pair
    `¼`. All three match B-T2.
  - T3: `MK₁(π/2)` twice returns the ontic state exactly and T0's witness returns: `unconditional`.
  - T4: at `β = π/4`, `port = m + [ϕ = π]`, masses `½` on the matching pairs; at `β = 0`, all `¼`;
    sums equal T1-V. Matches B-T4.
  - T8: each capability vanishes under its null counterpart.
- *Separation from PC-Q by T7.* CC4 and PC-Q run T7 on different quadruples, so the separation cannot
  be computed under the frozen law reading (§2). It holds under a reading that does not compare laws:
  the W1 verdict (PC-Q positive, CC4 negative), or the derived values `(P, V) = (½, ½)` against
  `(√2/2, √2/2)`. The verdict reading is conditional on PC-Q's W1 and the pending Eqs. (10)–(11)
  check. That CC4 has no violating certified quadruple at all follows from Lemma G(ii) with LIT-1-C4
  (LOG:67–70) and LIT-1-C7 (LOG:433–435), external inputs consumed as recorded there, not from the
  single quadruple examined.
- *Genuineness.* The reference is computed from CC4's own distributions, not from the bound; it sits
  exactly on the boundary `V + P = 1`, so it exercises the strict inequality and the certification
  path of the decision function. It can fail (a wrong mixture weight or a non-model-level certificate
  changes `V + P` or the certificate). Genuine as a control of the T7 machinery.

### 3.3 Gaps found

- (G-CC4-1) MR★:1044 excludes CC4 from the common carrier, and the CC4 row does not supply its own
  versions of the following, all undefined for CC4:
  - `P_bal` (and `P_{r,ϕ}`). The T7 reference does not depend on it; T0–T6, the §M.9 T8 references
    and the T9 `unconditional` undo do. They hold under the evident reading "`p = 0` known, `x`
    uniform"; under "uniform on the whole space" T0 is negative and T3 is `none`.
  - the strength map `θ ↦ g = [θ ≠ 0]` (MR★:1051), without which T1 cannot run;
  - the T6 settings `B₀ = RD₁(0)`, `B₁ = RD₁(π/4)` (MR★:1056);
  - the symbols `z_s`, `x_s` in `Q_{s₁s₂}`, read as above.
- (G-CC4-2) The law of `f` in CC4's `DP` is not stated. T0-d, T8's `DP` row and the validity of `DP`'s
  output states need it uniform, as in the common carrier's `DP` (MR★:1050).
- (G-CC4-3) Lemma G(ii) needs the readout-sequence reading of §2.
- (G-CC4-4) The T7 separation is computable only under a reading the frozen text does not state (§2),
  and in its verdict form rests on PC-Q's W1, which waits for the stage-2 Eqs. (10)–(11) check.

### 3.4 Verdict

**CC4: VERIFIED AT NARROWER SCOPE.** Verified as written: GNC (Lemma G(ii), readout-sequence reading),
the T7 reference (certified quadruple, `V + P = 1`, no W1) under the evident reading of `z_s` and
`x_s`, and its genuineness. Verified only under the readings of G-CC4-1 and G-CC4-2: its T0–T4
behaviour and its §M.9 T8/T9 references, including the reproduction of PC-Q's T1, T2, T3 and T4 laws.
The T7 separation from PC-Q is verified only under a reading that does not compare laws (the W1
verdict or the derived `(P, V)`), which PREREG:552's "from PC-Q's law" does not state; in the verdict
form it is conditional on PC-Q's B-T7 W1 and its pending Eqs. (10)–(11) check.

***

## 4. CC5 — classical eraser (S3's M-2)

### 4.1 What is specified (MR★:1067, with C-8 at MR★:1423–1431; frozen row PREREG:572)

Common carrier `(p, k)`, `P_bal`: `p` uniform, `k = 0`; markers `m_j = (a_j, b_j)`; `MK_j(1)`:
`a_j ← a_j + p`, fresh `e`, `k ← k + e`, `b_j ← b_j + e`; `RD_j(0)` reads `a_j`, `RD_j(π/4)` reads
`b_j`; `MK_j(−π/2)` unavailable; GNC by Lemma G(i). Reference: no W1 (C-8: `T7-UNCERTIFIED`, no W1
decided); T4's conditional masses sum to the marked law. Separated from PC-Q by T7 (T4 is
bookkeeping). §M.9: every applicable T8 row passes; no undo.

### 4.2 Checks (with ready markers `(a_j, b_j) = (0, 0)` and `e` uniform where stated)

- *T4.* After `MK₁(1)`: `a = p`, `k = b = e`. `PH(ϕ)`: `k = e + [ϕ = π]`. `β = π/4`: `m = e`,
  `port = e + [ϕ = π]`: mass `½` on `(0, 0), (1, 1)` at `ϕ = 0` and on `(0, 1), (1, 0)` at `ϕ = π`,
  which equals B-T4's `(1 ± cos ϕ)/4` exactly. `β = 0`: `m = p`, port independent and uniform: `¼`
  each, as PC-Q. Summed over `m`, port 0 has mass `½` = CC5's T1-V(π/2, ϕ). Checked. The bookkeeping
  identity holds for any law of `e` and any initial marker content, since `RD₁` does not touch `k`; it
  fails only if a branch is dropped or renormalized (CP-MASS, CP-BRANCH).
- *T1.* `(V, D) = (1, 0)` at `g = 0` and `(0, 1)` at `g = 1` (`RD₁(0)` reads `a = p`), as PC-Q. Not a
  separating test, consistent with the row.
- *T7 (C-8).* `P_{r,ϕ}`: `P = |2r − 1| = √2/2`; `TX` reads the fixed `k = [ϕ = π]`, so `V = 1`. Pair
  mixtures: `{(r₊,0), (r₋,π)}` gives masses `(r₊, 1−r₊, r₋, 1−r₋)/2` on `(0,0), (1,0), (0,1),
  (1,1)`; `{(r₊,π), (r₋,0)}` gives `(r₋, 1−r₋, r₊, 1−r₊)/2`. They differ since `r₊ ≠ r₋`, so `RDALL`
  separates them: `T7-UNCERTIFIED`, no W1. Checked.
- *Separation from PC-Q by T7.*
  - *Law level, as written.* On `P_{r,ϕ}, TX`, CC5 is deterministic and PC-Q gives `(1 ± √2/2)/2`.
    Both run the same protocol, so this is the frozen law reading of PREREG:552. Checked.
  - *Verdict level, conditional.* CC5 `T7-UNCERTIFIED` against PC-Q W1 positive. PC-Q's W1 is
    conditional on the pending Eqs. (10)–(11) check (MR★:1145–1147), as for CC4 (G-CC4-4).
- *T8, T9, T0, T5.* `MK₁(0)` gives `D = 0`, so the marking capability vanishes; `DP` row as the common
  carrier; undo row "not attributed". T0 positive (classical phase label). T5 at `{π/2}²`: order
  independence and dependence on `ϕ₁ + ϕ₂` alone hold for any law of `e`; the value `p₀ = ½`, matching
  B-T5, needs `e` uniform. Checked.
- *GNC.* `Λ = (p, k, a₁, b₁, a₂, b₂)` finite; point preparations and `RDALL` in `Acc` (MR★:1058);
  Lemma G(i) applies. Checked.
- *Genuineness.* Its references are computed from its own primitives. As a T7 control it is weak: its
  "no W1" is reached by non-certification, so the inequality is never evaluated on it. Its substantive
  role is T4: it reproduces PC-Q's conditional eraser fringes with full branch masses, the point of the
  frozen requirement "Consistency only: CC4 and CC5 reproduce erasers" (PREREG:490–491).

### 4.3 Gaps found

- (G-CC5-1) The initial marker content is not stated. The §M.9 T8 marking row (`D(π/2) > 0`) and the
  conditional fringes need ready markers with known content (read here as `(0, 0)`, as PC-Q's `|0⟩`
  and §M.7's "ready markers").
- (G-CC5-2) The law of "a fresh `e`" is not stated. None of CC5's stated references depends on it; the
  exact match to PC-Q's T4 fringes, `V(π/2) = 0` and T5's `p₀ = ½` need it uniform.
- (G-CC5-3) `MK_j(0)` is not defined in the row (only `MK_j(1)`); T1 at `θ = 0` and T8's null
  counterpart need it, read as the identity (`g = 0`).
- (G-CC5-4) `RD_j` is not stated to be nondemolition on `k`; T4's bookkeeping needs that it does not
  act on `k`, which the row's "reads" implies.

### 4.4 Verdict

**CC5: VERIFIED AT NARROWER SCOPE.** Verified as written: GNC, `T7-UNCERTIFIED` with no W1 (C-8), T4
bookkeeping, and separation from PC-Q by T7 at the law level. The verdict-level T7 separation is
conditional on PC-Q's W1 and the pending Eqs. (10)–(11) check. Verified only under G-CC5-1 and
G-CC5-3: the §M.9 T8 references. Verified only under G-CC5-1 to G-CC5-3, with `e` uniform: the
statement S3 relies on, that CC5 reproduces PC-Q's conditional-fringe (T4) law exactly with full
branch masses. CC5 has no undo, so it says nothing about unconditional return of interference (T3).

***

## 5. CC7 — classical dephasing with no record (S3's M-3)

### 5.1 What is specified (MR★:1069; frozen row PREREG:574)

Common carrier; `MK_j(g)`: `k ← k + g·f`, `f` fresh and discarded; markers untouched; `MK_j(−π/2)`
unavailable; GNC by Lemma G(i). Reference: at `g = 1`, `V = 0` and `D = 0`, i.e. §3.5 (ii) with R1
failing. Separated from PC-Q by §3.5 (PC-Q at `θ = π/2`: `V = 0`, `D = 1`, decoherence). §M.9: T8
marking-row capability "`V(π/2) < V(0)`"; no undo. C-8: `T7-UNCERTIFIED`.

### 5.2 Checks

Write `q = P(f = 1)`. `V(θ) := p₀(ϕ=0) − p₀(ϕ=π)` is signed (MR★:972).

- *`V`.* At `g = 1`, `k = f + [ϕ = π]`, so `p₀(0) = 1 − q`, `p₀(π) = q` and `V(π/2) = 1 − 2q`; at
  `g = 0`, `V = 1`.
  - The stated reference value `V = 0` needs `q = ½`.
  - (ii), a `𝒯`-contrast below the pre-interaction contrast (PREREG:206–208), needs `|1 − 2q| < 1`,
    that is `0 < q < 1`.
  - The T8 marking-row capability `V(π/2) < V(0)`, read with the signed `V`, needs `q > 0`.
- *`D` and R1.* The markers are untouched, so their content is independent of `p`; for any readout
  acting on the markers alone, `P(m, z)` factorizes and `D = 0`. `f` is independent of `p` and
  discarded. No subsystem of `A × E` correlates with the path: R1 fails (PREREG:162). These hold for
  every law of `f`. Checked.
- *Separation from PC-Q.*
  - *Through `D`, as written.* PC-Q has `D(π/2) = 1`, CC7 has `D(π/2) = 0`; the T1-D laws differ.
  - *Through the §3.5 classification, conditional.* "Dephasing" is (ii) with no record
    (PREREG:208–209); PC-Q's case is decoherence. The dephasing classification needs (ii), hence
    `0 < q < 1`, which the row does not state; reading "fresh" as random supplies it.
- *T8, T9, T7.* Under `MK₁(0)`, `V(π/2) = V(0) = 1`, so `V(π/2) < V(0)` vanishes (for any `q > 0`);
  `D(θ) > 0` is absent in the full interface, "not attributed". T9: no undo. T7 as in §4.2's C-8
  computation (same carrier); any verdict-level T7 comparison with PC-Q carries the same Eqs.
  (10)–(11) condition, though CC7's named separating test is §3.5, not T7. Checked.
- *Genuineness.* The reference is computed from CC7's own primitives; it fails if an implementation
  copies `p` into a marker (`D` becomes 1) or uses a degenerate or biased `f`. It is the control for
  Proposition S's "(ii) does not imply a record" (PREREG:224–226). Genuine.

### 5.3 Gaps found

- (G-CC7-1) The marker alphabet and the conjugate readout `RD_j(π/4)` ("defined per control",
  MR★:1055) are not defined for CC7. `D = 0` holds for every marker-only readout, so the reference is
  unaffected; the T6 law (`B₁ = RD₁(π/4)`) and T4 at `β = π/4` are undefined until one is chosen. No
  stated CC7 reference reads them.
- (G-CC7-2) "`f` fresh" does not state its law. Loss of interference (ii), and with it the dephasing
  classification, needs `0 < q < 1`; the T8 marking row needs `q > 0`; the reference value `V = 0`
  needs `q = ½`, as the common carrier's `DP` (MR★:1050) states for its own `f`.
- (G-CC7-3) Initial marker content unstated (as G-CC5-1); immaterial to `D = 0`.

### 5.4 Verdict

**CC7: VERIFIED AT NARROWER SCOPE.** Verified as written: `D = 0` and R1 failing at `g = 1` (for every
marker-only readout and every law of `f`), GNC, `T7-UNCERTIFIED`, and separation from PC-Q through `D`.
Verified only with a nondegenerate `f` (`0 < q < 1`): (ii), the dephasing classification and hence the
§3.5 separation, and the T8 marking-row reference (which needs only `q > 0`). Verified only with `f`
uniform: the stated reference value `V = 0`. Not verifiable as specified: CC7's T6 law and its T4 law
at `β = π/4` (G-CC7-1); neither is a stated reference.

***

## 6. Consequences for S3 (no edit to S3 is made or implied)

- **S-L3 in SNR-1 (S3-PLAN-r9 §8.4 check 1, the "disproved-erasure" case; §8.6).** Once this record
  is accepted:
  - S-L3 as stated can count as verified: `σ` is not available, the inverse is representable as
    `σφσ` and executed only as a global wait, and no region selects the map applied to another, under
    K1 and MR-1's frozen availability standard.
  - S-L3 with this record's supplements (Sup-1, Sup-2) adds: no global block swap `σ_X ⊕ g` is
    available, and no available operation inverts a marking evolution within a budget below
    recurrence. These are this record's results, not S-L3's.
  - Neither covers erasure in T3's sense (an available `φ^n` returning the carrier–marker
    preparation to one §5.3-equivalent to the pre-marking one), nor a marker-local reading of
    "uncomputation" under transport, and (Sup-3) shows that a native tick can apply `σ` to a one-site
    region's content. S3's conditional reading "[A-inf] subsystem uncomputation of a which-path
    record is not available on K1" is broader than both. A miss that needs it stays conditional on an
    unproved step. S3's own second condition (a re-check under the U1 §3 criterion) is not addressed
    here.
- **CC4 (M-1) and CC5 (M-2) in (e′).** At verified scope: classical models reproduce PC-Q's T4
  conditional fringes with full branch masses (CC4 and CC5), its T1 values at `θ ∈ {0, π/2}` (both),
  its T2 laws (CC4), and an unconditional undo with returned T0 witness (CC4 only), under the readings
  of G-CC4-1, G-CC4-2 and G-CC5-1 to G-CC5-3 (with `e` uniform for CC5). Running them as controls
  (stage 2) is still owed for (e′), as S3 states; this record verifies the paper specification only.
  Their separation from PC-Q at T7 is conditional as stated in §3.4 and §4.4.
- **CC7 (M-3).** Usable at verified scope for "loss of interference without any record" with a
  nondegenerate `f`: `D = 0`, R1 failing, (ii) holding; the value `V = 0` needs `f` uniform.
- **Specification repairs** for a stage-2 control plane, under its own authorization: G-CC4-1 to
  G-CC4-4, G-CC5-1 to G-CC5-4, G-CC7-1 to G-CC7-3; a rule for computing `separated`, consistent with
  PREREG:552's "from PC-Q's law" or explicitly departing from it for CC4; and a Row 0 clause (or a
  stated coverage by `reference_match`) for frozen 0(i)'s non-separation case. MR★ is a frozen record
  and is not edited (§A.42 item 6).

## 7. What was checked and what was not

**Checked by hand:** S-L3 (all four bullets), P-1, P-2, S-L1, S-C1(a), S-L2's derivation from the
frozen standard, S-L6's first bullet; the supplements Sup-1 to Sup-3; the side-2 stencil case against
SM:224–226, MR★:358–359 and PC★:102–106; Lemma G (i) and (ii); CC4's primitives, spanning identity,
T0–T4, T7 and T8 references; CC5's T0, T1, T4, T5, T7 (C-8), T8 and T9 references; CC7's `V`, `D`,
R1, T7, T8 and T9; PC-Q's B-T1 at `θ = π/2`, B-T2, B-T4 and B-T7 as comparison values; the frozen
rows and definitions at PREREG:162, 190–196, 206–209, 224–226, 485–491, 551–583 and 592–593; the
decision function's Row 0 (MR★:1243–1248).

**Not checked:** S-L4, S-L5, S-L7, S-C4a/b, except as cited; whether `Φ^n_{XX} = σ_X` holds for regions
with internal edges or for `n ≥ 2`; CC1, CC3, CC6, CC8; PC-Q's other closed forms (B-T0, B-T3, B-T5,
B-T6) beyond the values used; CC4's T5 and T6 laws, and CC5's and CC7's T2 and T6 laws; the §M.10
mutation table; the identification of CC4 with Catani et al. 2023's model; the LIT-1 reader record's
reading of Catani et al. (consumed as recorded at LOG:55–80 and LOG:433–435, an external input with
its stated caveats); the Eqs. (10)–(11) check owed at stage 2; whether K1 is the physics (a posit,
MR★ C-1). No control was run.
