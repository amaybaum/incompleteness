# Independent paper verification: MR★ S-L3 and countercontrols CC4, CC5, CC7 (r1)

## 0. Header

**Purpose.** A paper-only independent verification of four items that S3-PLAN-r9 carries as named
premises: MR-1 stage 1's lemma S-L3, and the countercontrols CC4, CC5 and CC7 of MR★ §M.6 (S3's
M-1, M-2, M-3). For each item the record states what is claimed, checks it by hand, traces its
dependencies, and returns one of VERIFIED, VERIFIED AT NARROWER SCOPE, NOT VERIFIED or REFUTED.
Nothing here is upgraded beyond what the checked argument reaches.

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

Line numbers `MR★:N`, `PREREG:N` refer to those blobs. S3-PLAN-r9 and S3-U1-r5 (drafts under
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/` on the RO-1 working
branch, not on `main`) were read only to identify how the items are used.

**Verifier independence.** This verifier authored neither MR-1's preregistration, MR★, nor any of
their amendments or review records, and did not take part in the review of `fc68d333` whose relayed
report (MR★:1297–1300; LOG:773) is the items' only recorded verification. That report was not used
as evidence here; every step below was re-derived from the source text.

**Method and limits.** Paper reasoning only. No computation, simulation, enumeration, script, Lean
or numerical evaluation was run; the small finite laws below (two-valued and four-valued
distributions) were worked by hand. No repository file was edited.

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

The conclusion "not available" is relative to MR-1's frozen availability standard (PREREG:190–196;
restated MR★:451–457): an operation counts only if it is a finite composition of `φ`-steps on the
declared state, under the declared access, with a sourced setting. S-L2 (MR★:511–515) records the
consequence: the available transformations of the joint state are the time shifts `φ^n`, `n`
within the budget; observer-side choices change only which region and tick are read.

### 1.2 Step-by-step check

**(L3a).** `φ(y, x) = (x, A x − y)`, so `σφσ(x, y) = σ(x, A x − y) = (A x − y, x) = ψ(x, y)`.
Checked. P-1 itself (PC★, §PC★2a): `ψ(φ(u_prev, u)) = ψ(u, A u − u_prev) = (u_prev, u)` and
`φ(ψ(x, y)) = φ(A x − y, x) = (x, y)`. Checked; it uses no property of `A`.

**(L3b).** Suppose `σ = φ^k`. Then `σ` commutes with `φ`, and with `σ² = id`,
`φ^{−1} = σφσ = φσσ = φ`, so `φ² = id`. Directly, `φ²(x, y) = φ(y, A y − x) = (A y − x, A(A y − x) − y)`.
Equality with `(x, y)` for all `(x, y)` gives, from the first component, `A y = 2x` for all `x, y`;
`x = 0` gives `A y = 0` for all `y`, so `A = 0`. (MR★ routes through `2x = 0` first; that step is
correct but not needed, and it is not a contradiction by itself on 2-torsion groups such as `ℤ/2`
or `ℝ/ℤ`. The argument as written still reaches `A = 0` correctly.) Hence `A ≠ 0` implies `σ` is no
time shift. Checked.

*`A ≠ 0` under the stated hypotheses.* PC★2a defines `∼` as a relation and sums over the `j` with
`j ∼ i`. If `j ∼ i` and `r ∈ 𝐑` is nonzero, `(A(rδ_j))_i = a·r ≠ 0` by injectivity. Checked. Scope
note: if instead the stencil is read as a multiset of offsets `±e` (SM's "six nearest neighbours"),
then on a torus of side 2 the two offsets coincide and `(A u)_i = 2a Σ u_j`, which vanishes on
`𝐑 = ℤ/2`. There `φ(x, y) = (y, −x) = (y, x) = σ`, so `σ` is a time shift. This lies outside the
native lattice (and outside the `N ≥ 5w + 2` tori S-L4 uses), but it shows the operative hypothesis
is `A ≠ 0`, not "nonempty relation" alone. Under the relation reading of PC★2a, or for side `≥ 3`,
or for `2a` injective, the hypothesis holds.

**(L3c).** Two readings, checked separately.
- *Conditional reading (MR★'s citation).* By S-L1 (MR★:491–496; from additivity, PC★ P-2), region
  `X`'s content at time `t` is `Φ^t_{XX} s_X + Σ_{Z≠X} Φ^t_{XZ} s_Z`, with every `Φ^t_{YX}` fixed by
  `(t, X, Y)`. So no region's content changes the map applied to `s_X`; another region contributes
  only an additive offset, and `σ_X` is not an offset. This is S-C1(a) (MR★:498–503). Checked.
  S-L1 checked: `φ^t` is additive and `s = Σ_X ι_X s_X`.
- *Unconditional reading (not argued in MR★; supplied here).* Is a slice swap on one proper region
  `X`, of block form `τ = σ_X ⊕ g` with any `g` on the complement, a time shift? Suppose `τ = φ^n`;
  then `τφ = φτ`. Pick `i ∈ X`, `j ∉ X` with `j ∼ i` (exists for a proper nonempty `X` in a connected
  graph, such as the native cubic torus), `r ≠ 0`, and `s = (0, rδ_j)`. Then `τ s = g s` is supported
  off `X`, so the previous-slice part of `φ(τ s)` on `X` is the current slice of `g s` on `X`, which is
  `0`. But `φ s = (rδ_j, A rδ_j)` has `X`-part `(0, (A rδ_j)|_X)` with `(A rδ_j)_i = a r ≠ 0`, and
  `τ` swaps it to previous-slice part `(A rδ_j)|_X ≠ 0`. So `τφ s ≠ φτ s`: no such `τ` is a time
  shift. If `X` is a union of connected components, the global argument applies to `X` alone when
  `A|_X ≠ 0`. So (L3c) holds in both readings, the second by this supplementary argument.

**(L3d).** `φ` is a bijection (P-1); on finite `S` it has finite order `N` and `φ^{−1} = φ^{N−1}`.
Every available operation is some `φ^n` (S-L2), which acts on all of `S`. Checked. Supplementary,
for S3's use: an `m`-step marking evolution `φ^m` is inverted by an available `φ^n` only if
`ord(φ) | n + m`; with budget `T` and `T + m < N` (the "budget below recurrence" of MR★ §M.1,
MR★:857–865, and S-L6) no available operation inverts it. On infinite `S` (`ℤ_p`, `ℝ/ℤ`) the
finite-`S` bullet does not apply, and (L3b) holds unchanged.

### 1.3 Dependencies and their status

| Dependency | Source | Status found here |
|---|---|---|
| K1 step and its freeze | MR★ §K★.F (MR★:327–416), owner decision PR #1023 c.6554399670 | frozen record; used as the defining hypothesis |
| P-1 (bijectivity, `ψ`), P-2 (additivity) | PC★ §PC★2a, blob `79aad250` on `main` | re-derived here; exact algebra, holds for every abelian `𝐑`, integer `a`, any relation |
| S-L1, S-C1(a) | MR★:491–503 | re-derived here from P-2 |
| availability standard; S-L2 | PREREG:190–196 (frozen); MR★:511–515 | definitional consequence of the frozen standard; checked |
| finite order of `φ` (S-L6, first bullet) | MR★:595–597 | elementary (bijection of a finite set); checked |
| `a` injective, `A ≠ 0` | MR★:473–477 ("reading": `a = 1`) | `a = 1` is a reading of SM's rule; S-L3 needs only `A ≠ 0`, which holds for every coefficient the corpus uses under the relation convention |
| subsystem form of (L3c) | not argued in MR★ beyond S-C1(a) | supplied in §1.2 |

No dependency of S-L3 rests on an unverified record: its proof uses only exact algebra on the frozen
step and the frozen availability standard. The relayed review report is not among its supports here.

### 1.4 Verdict

**S-L3: VERIFIED, at its stated scope** — `K★ = {K1}`, MR-1's frozen availability standard via
S-L2, `A ≠ 0` (implied by `a` injective with the relation convention of PC★2a; fails only on
degenerate side-2 multiset stencils over 2-torsion `𝐑`), on any value group of PC★2a and any graph
with an edge. Bullet (L3c) is verified in the conditional sense by S-C1(a) and in the unconditional
block-swap sense by the supplementary argument of §1.2.

**What S-L3 does not establish.** S-L3 concerns the swap `σ`, its subsystem block forms and the exact
inverse `ψ`. It does not show that no available time shift `φ^n` returns a subsystem (carrier and
marker) to a preparation §5.3-equivalent to the pre-marking one, for example by partial revival, nor
that a which-path record cannot leave the marker region by transport (by S-C4a it does leave any
confined region). "Erasure unavailable on K1" is therefore verified only in the sense "no available
operation executes `σ`, a block `σ_X ⊕ g`, or the inverse of the marking evolution within a budget
below recurrence"; it is not verified in the operational sense of T3 (no `unconditional` or
probabilistic restoration of the joint law by any available policy).

***

## 2. Common checks for the three countercontrols

**Specification sites.** MR★ §M.6 (MR★:1018–1074): Lemma G (MR★:1022–1042), the classical carrier
common to CC1, CC3, CC5, CC7 (MR★:1044–1058), the instance rows (CC4 MR★:1066, CC5 MR★:1067, CC7
MR★:1069); test menu §M.7 (MR★:1076–1124); T7 rules §M.8 (MR★:1126–1159); T8/T9 references §M.9
(MR★:1161–1188); C-8's pinned T7 references (MR★:1423–1431). Frozen obligations: PREREG:555–583,
in particular PREREG:559–560 (each instance "fixed at stage 1 together with a paper proof that each
admits a generalized-noncontextual model") and the frozen rows for CC4, CC5, CC7.

**Lemma G** (dependency of all three). Re-derived. Under (i) (point preparations and a complete
readout `RDALL` in `Acc`), equivalence of two preparations gives equal `RDALL` laws, i.e. equal
distributions; `δ_λ`, then a procedure, then `RDALL` returns `K(r, λ′ | λ)`, so equivalent procedures
have equal kernels. Under (ii), the mass `Σ μ(λ) K(r, λ′ | λ) e(λ′)` is bilinear and spanning sets on
both sides determine each `K(r)`. Checked. Reading needed for (ii) on a multi-bit `Λ`: "single
readouts" must include sequences of single-bit readouts on distinct bits, whose response functions
are products (a readout's disturbance acts only on its own bit, after it is read); with three bits and
`T = 8` such sequences fit in `Acc_ctrl`. Under that reading (ii) holds for CC4.

**PC-Q references used for separation** (checked as dependencies only). B-T1 at `θ = π/2`:
`|L0⟩ + |R1⟩`, orthogonal markers, `(V, D) = (0, 1)`. B-T7: Bloch points `(±√2/2, ±√2/2)`,
antipodal pair mixtures both `I/2`, `V + P = √2 > 1`. Checked. PC-Q's W1 also carries §M.8's
recorded condition that stage 2 checks Eqs. (10)–(11) against the source before any T7 step
(MR★:1137–1145); that check is not done.

**Specification gap common to all controls.** §M.11's schema records `control_separation:
{test, separated}` (MR★:1233), but no rule for computing `separated` is stated: neither "laws of the
named test differ" nor "the test's verdicts differ". Where the two readings give the same answer this
record says so.

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
  unchanged by `MK_j`), so it is an involution on the ontic state. Checked. `PH`, `DP` and the three
  readouts map valid states to valid states. Checked.
- *Spanning identity.* `δ_{(x₀,p₀)} = (1{x=x₀} + 1{p=p₀} + 1{x+p=x₀+p₀} − 1)/2`: value `1` at
  `(x₀, p₀)`, `0` at the three other points. Each indicator is twice a pure-state distribution, and
  `1 = 1{x=0} + 1{x=1}`. So the six pure distributions span `ℝ⁴`, and the indicators are the
  readouts' response functions. Checked.
- *T7 reference.* `Q_{s₁s₂}` gives `⟨Z⟩ = ½(−1)^{s₁}` and `⟨X⟩ = ½(−1)^{s₂}`, so `P = V = ½` for all
  four members and `V + P = 1`. Antipodal pairs `{00, 11}` and `{01, 10}`: each pair mixture is
  `¼(z₀ + z₁ + x₀ + x₁)`, the uniform distribution, so the Eq. (11)-type equivalence holds at model
  level (equal distributions imply equal future laws). Certified; `1 > 1` is false; no W1. Checked.
  `Q_{s₁s₂}` is not itself a listed valid state (its distribution takes values `½, ¼, ¼, 0`); it is a
  declared mixture preparation, which the row defines explicitly.
- *T1, T3, T4, T0, T2 (under the reading in §3.3).* With `P_bal` = "`p = 0` known, `x` uniform":
  `MK₁(1)` sets `x_M = x` and `p ← p_M` (uniform), so `(V, D) = (0, 1)` at `θ = π/2` and `(1, 0)` at
  `0`, matching PC-Q, consistent with "T1 is a consistency check only". T3 returns the ontic state
  exactly, T0's witness returns: `unconditional`. T4 at `β = π/4` gives `port = m + [ϕ = π]`, masses
  `½` on the matching pairs; at `β = 0` all `¼`; sums equal T1-V. T0-c(π, π) gives outcome 0 with
  mass 1, T0-d gives `½`: T0 positive. T8 rows: each capability vanishes under its null counterpart.
  Checked.
- *Separation from PC-Q by T7.* CC4 and PC-Q run T7 on different quadruples (`Q` against `P_{r,ϕ}`,
  which CC4 cannot prepare), so the separation is at the level of the W1 verdict: PC-Q positive, CC4
  negative. That CC4 has no violating certified quadruple at all follows from Lemma G(ii) with
  LIT-1-C4 and LIT-1-C7 (LOG:55–80, the reader record of Catani et al. 2022), not from the single
  quadruple examined.
- *Genuineness.* The reference is computed from CC4's own distributions, not from the bound; it sits
  exactly on the boundary `V + P = 1`, so it exercises the strict inequality and the certification
  path in the decision function. It can fail (a wrong mixture weight or a non-model-level certificate
  changes `V + P` or the certificate). Genuine as a control of the T7 machinery.

### 3.3 Gaps found

- (G-CC4-1) `P_bal` (and `P_{r,ϕ}`) are not defined for CC4: the common carrier excludes CC4
  (MR★:1044), and the CC4 row defines only `Q`. The T7 reference does not depend on it; T0–T6, the
  §M.9 T8 references and the T9 `unconditional` undo do. They hold under the evident reading "`p = 0`
  known, `x` uniform" (the analogue of `|+⟩`, `TX` outcome 0 certain); under "uniform on the whole
  space" T0 is negative and T3 is `none`.
- (G-CC4-2) The law of `f` in CC4's `DP` is not stated; T0-d and T8's `DP` row need it uniform, as in
  the common carrier's `DP` (MR★:1050).
- (G-CC4-3) Lemma G(ii) needs the readout-sequence reading of §2.
- (G-CC4-4) The T7 separation rests on PC-Q's W1, which waits for the stage-2 read of Eqs. (10)–(11).

### 3.4 Verdict

**CC4: VERIFIED AT NARROWER SCOPE.** Verified as written: GNC (Lemma G(ii), readout-sequence reading),
the T7 reference (certified quadruple, `V + P = 1`, no W1) and its genuineness. Verified only under
the readings of G-CC4-1 and G-CC4-2: its T0–T6 behaviour and its §M.9 T8/T9 references, including
the reproduction of PC-Q's T1, T3 and T4 laws. The T7 separation from PC-Q is verified at the
W1-verdict level, conditional on PC-Q's B-T7 W1 and its pending Eqs. (10)–(11) read.

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
  which equals PC-Q's B-T4 `(1 ± cos ϕ)/4` exactly. `β = 0`: `m = p`, port independent and uniform:
  `¼` each, as PC-Q. Summed over `m`, port 0 has mass `½` = CC5's T1-V(π/2, ϕ). Checked. The
  bookkeeping identity holds for any law of `e` and any initial marker content, since `RD₁` does not
  touch `k`; it fails only if a branch is dropped or renormalized (CP-MASS, CP-BRANCH).
- *T1.* `(V, D) = (1, 0)` at `g = 0` and `(0, 1)` at `g = 1` (`RD₁(0)` reads `a = p`), as PC-Q. Not a
  separating test, consistent with the row.
- *T7 (C-8).* `P_{r,ϕ}`: `P = |2r − 1| = √2/2`; `TX` reads the fixed `k = [ϕ = π]`, so `V = 1`. Pair
  mixtures: `{(r₊,0), (r₋,π)}` gives masses `(r₊, (1−r₊), r₋, (1−r₋))/2` on `(0,0), (1,0), (0,1),
  (1,1)`; `{(r₊,π), (r₋,0)}` gives `(r₋, (1−r₋), r₊, (1−r₊))/2`. They differ since `r₊ ≠ r₋`, so
  `RDALL` separates them: `T7-UNCERTIFIED`, no W1. Checked.
- *Separation from PC-Q by T7.* The `P_{r,ϕ}, TX` law is deterministic for CC5 and
  `(1 ± √2/2)/2` for PC-Q, and the verdicts differ (uncertified against W1 positive). Separated
  under either reading of `separated`. Checked.
- *T8, T9, T0, T5.* `MK₁(0)` gives `D = 0`, so the marking capability vanishes; `DP` row as the common
  carrier; undo row "not attributed". T0 positive (classical phase label). T5 at `{π/2}²`: `p₀ = ½`,
  order independent. Checked.
- *GNC.* `Λ = (p, k, a₁, b₁, a₂, b₂)` finite; point preparations and `RDALL` in `Acc` (MR★:1058);
  Lemma G(i) applies. Checked.
- *Genuineness.* Its references are computed from its own primitives. As a T7 control it is weak: its
  "no W1" is reached by non-certification, so the inequality is never evaluated on it. Its substantive
  role is T4: it reproduces PC-Q's conditional eraser fringes with full branch masses, which is the
  point of the frozen requirement "T4 is consistency only: CC4 and CC5 reproduce erasers"
  (PREREG:490–491).

### 4.3 Gaps found

- (G-CC5-1) The initial marker content is not stated. The §M.9 T8 marking row (`D(π/2) > 0`) and the
  conditional fringes need ready markers with known content (read here as `(0, 0)`, as PC-Q's `|0⟩`
  and §M.7's "ready markers").
- (G-CC5-2) The law of "a fresh `e`" is not stated. None of CC5's stated references depends on it;
  the exact match to PC-Q's T4 fringes and `V(π/2) = 0` need it uniform.
- (G-CC5-3) `MK_j(0)` is not defined in the row (only `MK_j(1)`); T1 at `θ = 0` and T8's null
  counterpart need it, read as the identity (`g = 0`).
- (G-CC5-4) `RD_j` is not stated to be nondemolition on `k`; T4's bookkeeping needs that it does not
  act on `k`, which the row's "reads" implies.

### 4.4 Verdict

**CC5: VERIFIED AT NARROWER SCOPE.** Verified as written: GNC, `T7-UNCERTIFIED` with no W1 (C-8), T4
bookkeeping, and separation from PC-Q by T7 at the law level. Verified only under G-CC5-1 and
G-CC5-3: the §M.9 T8 references. Verified only under G-CC5-1 to G-CC5-3, with `e` uniform: the
statement S3 relies on, that CC5 reproduces PC-Q's conditional-fringe (T4) law exactly with full
branch masses. CC5 has no undo, so it says nothing about unconditional return of interference (T3).

***

## 5. CC7 — classical dephasing with no record (S3's M-3)

### 5.1 What is specified (MR★:1069; frozen row PREREG:574)

Common carrier; `MK_j(g)`: `k ← k + g·f`, `f` fresh and discarded; markers untouched; `MK_j(−π/2)`
unavailable; GNC by Lemma G(i). Reference: at `g = 1`, `V = 0` and `D = 0`, i.e. §3.5 (ii) with R1
failing. Separated from PC-Q by §3.5 (PC-Q at `θ = π/2`: `V = 0`, `D = 1`, decoherence). §M.9: T8
marking row capability "`V(π/2) < V(0)`"; no undo. C-8: `T7-UNCERTIFIED`.

### 5.2 Checks

- *`V`.* `T1-V(1, ϕ)`: `k = f + [ϕ = π]`; with `f` uniform, `p₀ = ½` for both `ϕ`, `V = 0`; at
  `g = 0`, `V = 1`. So (ii) holds (PREREG:206–208). If `f` is biased, `V(π/2) = |1 − 2P(f = 1)|`,
  so the reference needs `f` uniform.
- *`D` and R1.* The markers are untouched, so their content is independent of `p`; for any readout
  acting on the markers alone, `P(m, z)` factorizes and `D = 0`. `f` is independent of `p` and
  discarded. No subsystem of `A × E` correlates with the path: R1 fails (PREREG:162). Checked.
- *Separation from PC-Q.* PC-Q has `D(π/2) = 1`; CC7 has `D(π/2) = 0`. The T1-D laws differ and the
  §3.5 classification differs (decoherence against dephasing). Checked.
- *T8.* Under `MK₁(0)`, `V(π/2) = V(0) = 1`, so `V(π/2) < V(0)` vanishes; `D(θ) > 0` is absent in the
  full interface, "not attributed". T9: no undo. T7 as in §4.2's C-8 computation (same carrier).
  Checked.
- *Genuineness.* The reference is computed from CC7's own primitives; it fails if an implementation
  copies `p` into a marker (`D` becomes 1) or uses a biased `f`. It is the control for Proposition S's
  "(ii) does not imply a record" (PREREG:224–226). Genuine.

### 5.3 Gaps found

- (G-CC7-1) The marker alphabet and the conjugate readout `RD_j(π/4)` ("defined per control",
  MR★:1055) are not defined for CC7. `D = 0` holds for every marker-only readout, so the reference is
  unaffected; the T6 law (`B₁ = RD₁(π/4)`) and T4 at `β = π/4` are undefined until one is chosen. No
  stated CC7 reference reads them.
- (G-CC7-2) "`f` fresh" does not state its law; `V = 0` needs it uniform, as the common carrier's
  `DP` (MR★:1050) states for its own `f`.
- (G-CC7-3) Initial marker content unstated (as G-CC5-1); immaterial to `D = 0`.

### 5.4 Verdict

**CC7: VERIFIED AT NARROWER SCOPE.** Verified as written: `D = 0` and R1 failing at `g = 1` (for every
marker-only readout), GNC, `T7-UNCERTIFIED`, separation from PC-Q through `D` and the §3.5
classification. Verified only with `f` uniform (G-CC7-2): `V = 0` at `g = 1`, hence (ii), and the T8
marking-row reference. Not verifiable as specified: CC7's T6 law and its T4 law at `β = π/4`
(G-CC7-1); neither is a stated reference.

***

## 6. Consequences for S3 (no edit to S3 is made or implied)

- **S-L3 in SNR-1 (S3-PLAN-r9 §8.4 check 1, the "disproved-erasure" case; §8.6).** Once this record
  is accepted, S-L3 can count as a verified disproof, but only for: no available operation executes
  `σ`, a block swap `σ_X ⊕ g`, or the inverse of a marking evolution within a budget below recurrence,
  under K1 and MR-1's frozen availability standard, with `A ≠ 0`. S3's conditional reading "[A-inf]
  subsystem uncomputation of a which-path record is not available on K1" is broader than S-L3: S-L3
  does not exclude an available `φ^n` that restores the carrier–marker joint law (T3 in the §5.3
  sense), nor the record's leaving the marker by transport. A miss that needs the broader statement
  stays conditional on an unproved step. S3's own second condition (a re-check under the U1 §3
  criterion) is not addressed here.
- **CC4 (M-1) and CC5 (M-2) in (e′).** At verified scope: classical models reproduce PC-Q's T4
  conditional fringes with full branch masses (CC4 and CC5), its T1 values at `θ ∈ {0, π/2}` (both),
  and an unconditional undo with returned T0 witness (CC4 only), under the readings of G-CC4-1/2 and
  G-CC5-1 to G-CC5-3. Running them as controls (stage 2) is still owed for (e′) as S3 states; this
  record verifies the paper specification only.
- **CC7 (M-3).** Usable at verified scope, with `f` uniform, for "loss of interference without any
  record": `V = 0`, `D = 0`, R1 failing.
- **Specification repairs** (G-CC4-1, G-CC5-1 to G-CC5-3, G-CC7-1/2, and the missing rule for
  `separated`) are for a stage-2 control plane under its own authorization; MR★ is a frozen record and
  is not edited (§A.42 item 6).

## 7. What was checked and what was not

**Checked by hand:** S-L3 (all four bullets), P-1, P-2, S-L1, S-C1(a), S-L2's derivation from the
frozen standard, S-L6's first bullet; Lemma G (i) and (ii); the CC4 spanning identity, primitives and
T7 reference; CC5's and CC7's T0, T1, T4, T5, T7 (C-8), T8 and T9 references; PC-Q's B-T1 at
`θ = π/2` and B-T7 as separation dependencies; the frozen rows PREREG:555–583.

**Not checked:** S-L4, S-L5, S-L7, S-C4a/b; CC1, CC3, CC6, CC8; PC-Q's other closed forms; T2, T5 and
T6 laws beyond what is stated above; the §M.10 mutation table and the §M.11 decision function; the
LIT-1 reader record's reading of Catani et al. (consumed as recorded at LOG:55–80, an external input
with its stated caveats); the Eqs. (10)–(11) read owed at stage 2; whether K1 is the physics (a posit,
MR★ C-1). No control was run.
