# Independent review: VERIFY-SL3-CC-r1 (S-L3; CC4, CC5, CC7)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/VERIFY-SL3-CC-r1.md`
at PR #1294 head `d58bd082de379198e91e2216224c231134575511`, blob `4baa0283`. While this review ran, the
RO-1 working branch moved to `4ce925ad` (it adds `U4-SOURCES-r1.md` and one README row). The reviewed blob
is identical at both heads.

**Sources, read at `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b`.** MR★
(`.../measurement-record-formation/amendments/MR-star.md`, blob `45af1678`); PREREG (`.../preregistration.md`,
blob `c36fb14b`, equal to the blob at `1a236f33`); LOG (`.../amendments/stage1-log.json`); PC★
(`.../physical-coupling-pc1/amendments/PC-star.md`, blob `79aad250`, equal at `99dce4b6`); O-OBSMU
`ANALYSIS.md`:483–490; SM.md and Substratum.md at `5914c17c`; Issue #1169 comments 6891189024 and
6891241282 (read with the GitHub read tool). S3-PLAN-r9 was read only to see how S3 uses the items. Every
commit the record cites (`fc68d333`, `99dce4b6`, `cccd69cd`, `1a236f33`, `af1e9be2`, `e16017d6`,
`f1eb719e`, `5914c17c`, `8af2d904`) is reachable from `main`.

**Reviewer independence.** This reviewer authored neither MR-1, MR★, the verification record nor any S3
document. Read-only; hand checking only; no computation, enumeration, Lean or repository edit.

**Verdict: ACCEPT WITH CHANGES.** The algebra the record checks is right, and none of its verdicts should be
NOT VERIFIED. Three changes are required before acceptance. (1) The record labels its block-swap argument
the "unconditional" reading of "no region executes `σ` on another", but the argument covers only global block
maps. In the natural marginal reading, the native step over `ℤ/2` does apply `σ` to a one-site region
(F1). (2) The S-L3 headline should separate S-L3 as stated from the authorization's gloss "erasure
unavailable on K1", which the record itself verifies only at narrower scope (F2). (3) CC5's T7 separation
"under either reading" omits the condition that the record attaches to CC4's (F4). The remaining findings are
precision fixes.

***

## Findings

### F1 (required). The "unconditional" reading of (L3c) is overstated. The supplementary argument is correct for the form it treats, which is narrower.

*The argument itself, re-derived.* Suppose `τ = σ_X ⊕ g`, with `g` an arbitrary map on the complement, and
`τ = φ^n`, so `τφ = φτ`. Take `i ∈ X`, `j ∉ X` with `j ∼ i`, `r ≠ 0`, and `s = (0, rδ_j)`.
- `s_X = 0`, so `(τ s)_X = σ_X(0) = 0`. The previous slice of `φ(τ s)` on `X` is the current slice of `τ s` on
  `X`, which is `0`.
- `φ s = (rδ_j, A rδ_j)`. Its `X`-part is `(0, (A rδ_j)|_X)`, with `i`-entry `a r ≠ 0`, and `σ_X` moves that
  entry to the previous slice.

So `τφ s ≠ φτ s`. The case where `X` is a union of components reduces to (L3b) on `X`. The argument is
correct and complete for global maps of block form `σ_X ⊕ g`. It uses no linearity of `g`.

*What it does not cover.* "A region executes `σ` on `X`" more naturally means the marginal reading. For a
fixed ready content `c` of the complement, `pr_X φ^n(s_X, c) = σ_X(s_X)` for all `s_X`, with the complement
free to change. By S-L1, this holds iff `Φ^n_{X,X^c}(c) = 0` and `Φ^n_{XX} = σ_X`. The record's S-C1(a)
sentence ("another region contributes only an additive offset, and `σ_X` is not an offset") leaves out the
case `Φ^n_{XX} = σ_X`. That case occurs inside frozen K1:
- Take `𝐑 = ℤ/2`, `a = 1`, the cubic torus of side `≥ 3`, `X = {i}` (both slices) and `n = 1`. Then
  `Φ^1_{XX}(x_i, y_i) = (y_i, −x_i) = (y_i, x_i) = σ_X(x_i, y_i)`. The cross term `Φ^1_{X,X^c}(c)` is
  `(0, a Σ_{j∼i} c_{cur,j})`, which vanishes whenever the neighbours' current slice is `0`.
- So in one tick the native step applies `σ` to a one-site region's content, given a zero-current-slice
  neighbourhood. The same holds for any independent set of sites. Over a general `𝐑` the block is the twisted
  swap `(y, −x)`.

*Consequence.* This contradicts no bullet of S-L3: no region *selects* `σ` (S-C1(a)), and the global map is
not of block form, as the record's argument shows. Nor does it give an erasure, since reversing a marking
needs the inverse on the record's whole support, which spreads (S-C4a). But it shows that "no available
operation applies `σ` to a region's content" is false on native scope. Required changes:
- rename the second reading "global block-form reading";
- add the marginal reading with the `ℤ/2` one-site case, recorded as outside what S-L3 or the supplement
  establishes;
- correct the S-C1(a) sentence to "the map on `s_X` is `Φ^t_{XX}`, fixed by `(t, X)` and selectable by no
  region".

### F2 (required). The S-L3 headline: correct for S-L3 as stated. The authorized item, glossed "erasure unavailable on K1", is verified only at narrower scope.

The bullets re-derived:
- **(L3a).** `σφσ(x, y) = σ(x, Ax − y) = ψ(x, y)`. P-1 checks both ways.
- **(L3b).** `σ = φ^k` gives `φ² = id`. The first component of `φ²(x, y)` is `Ay − x = x`, and `x = 0`
  gives `A = 0`. MR★'s route through `y = 0` (`2x = 0`, then `Ay = 2x = 0`) is also valid.
- **(L3d).** On finite `S`, `φ^{−1} = φ^{N−1}`. The record's supplement is also correct: `φ^n φ^m = id` iff
  `ord(φ) | n + m`.

For (L3c), MR★'s stated support is S-C1(a), and the record checks it in that sense. So "VERIFIED at stated
scope" is justified for S-L3's four bullets as stated. The block-swap argument is new: MR★ does not contain
it, and S-L3 as stated does not need it. It is not grounds for downgrading S-L3, but it is not part of S-L3.

Two places need changes:
- The authorization (#1169 c.6891189024) names the item "S-L3 (erasure unavailable on K1)". §1.4 of the
  record itself verifies that gloss "only in the sense" of no `σ`, no block swap, and no inverse of the
  marking within budget. In the record's own taxonomy that is VERIFIED AT NARROWER SCOPE. The headline should
  carry both rows: S-L3 as stated, VERIFIED; the erasure gloss, VERIFIED AT NARROWER SCOPE.
- §6 counts "a block swap `σ_X ⊕ g`" and "the inverse of a marking evolution within a budget below
  recurrence" as what S-L3 verifies. Both are the record's own supplements, and §6 should attribute them as
  "S-L3 with this record's §1.2 supplements".

The same narrowing applies to MR★'s own uses of S-L3, not only to S3's:
- "no subsystem undo exists (S-L2, S-L3, S-L6)" at MR★:648 and MR★:1396;
- "subsystem inverses (S-L3, S-L6)" at MR★:1485;
- "any inverse executed on a subsystem (S-L3, S-L6)" at MR★:856.

The record should note them. It need not correct them: MR★ is frozen.

### F3 (precision). The side-2 edge case is correct, but three statements about it need correcting.

*The edge case is correct.* Under SM's form lemma, `f = α(x_1 + ⋯ + x_{2d})` sums the `2d` neighbouring
values (SM:224–226 at `5914c17c`). On a torus of side 2 in **every** axis, each distinct neighbour is then
counted twice, so `A = 2a·(relation sum)`. Over `ℤ/2` this is `A = 0`, and `φ(x, y) = (y, −x) = σ(x, y)`.

Three corrections:
- *"Side 2" must be "side 2 in every axis".* With any axis of side `≥ 3`, `A ≠ 0`.
- *"2-torsion `𝐑`" (§1.4) must be "`𝐑 = ℤ/2`".* `A = 0` needs `2a = 0` on `𝐑`. Among `ℤ/q`, `ℤ_p` and
  `ℝ/ℤ`, with `a` injective, only `q = 2` gives that. `ℝ/ℤ` has 2-torsion, but `A ≠ 0` there.
- *"Outside the native lattice" is not shown by the cited sources.* Substratum A4 (Substratum:98) admits any
  quotient by a finite-index sublattice, and no minimum side is cited. The correct reason the native scope is
  unaffected is different. Frozen K1 defines `A` as PC★2a's relation sum, "`a·Σ_{j∼i}`" (MR★:358–359;
  PC★:102–106, whose examples include "`(ℤ/L)³` with six nearest neighbours"). On the side-2 torus that sum
  counts each neighbour once, so MR★'s stated hypotheses (`a` injective, a nonempty relation) do imply
  `A ≠ 0` within frozen K1. The multiset count is SM's reading, not K1's.

So the sentence "the operative hypothesis is `A ≠ 0`, not 'nonempty relation' alone" holds only under the
multiset reading.

### F4 (required). CC5's T7 separation: "separated under either reading" overstates the verdict reading.

At the law level, the separation holds as written. On `P_{r,ϕ}, TX`, CC5 is deterministic and PC-Q gives
`(1 ± √2/2)/2`. The verdict level is different. PC-Q's W1 is reached only after stage 2 checks Eqs.
(10)–(11) against the source, and if that check fails, stage 2 halts before any T7 step (MR★:1145–1147). So
verdict-level separation is conditional, exactly as the record says for CC4 (G-CC4-4). The same holds for
CC7's T7, though CC7's named separating test is §3.5, not T7. §4.2 should state the condition, and §4.4
correctly keeps only the law level.

### F5 (precision). CC7: the law of `f`.

- *What the definitions need.* `V(θ) := p₀(ϕ=0) − p₀(ϕ=π)` is signed (MR★:972). With `P(f=1) = q`,
  `V(π/2) = 1 − 2q`, not `|1 − 2q|`.
- *Too strict.* (ii), loss of contrast (PREREG:206–208), and the T8 marking-row capability `V(π/2) < V(0)`
  need only `0 < q < 1`. Only the stated reference value `V = 0` needs `q = ½`.
- *Too generous.* §5.4 lists "separation through the §3.5 classification" as holding as written. "Dephasing"
  is (ii) with no record (PREREG:208–209), and (ii) needs a nondegenerate `f`, which the row does not state.
  As written, only the `D` part of the separation holds (`D = 0` against PC-Q's `D = 1`). The dephasing
  classification needs `0 < q < 1`; reading "fresh" as random would supply that.

### F6 (precision; it strengthens the record's common gap). §M.11's `separated` gap is real, and wider than stated.

*Confirmed.* §M.11 (MR★:1233) records `control_separation: {test, separated}` but states no rule for
computing it. §M.7 says only "decided by the named test, as in §M.6" (MR★:1122).

Two facts the record does not cite:
- *The frozen text leans to the law reading.* PREREG:552 defines control separation as separation "from PC-Q's
  law". Under the law reading, CC4's T7 separation is not computable: CC4 runs `Q_{s₁s₂}` and PC-Q runs
  `P_{r,ϕ}`, which CC4 cannot prepare. So the record's verdict-level separation for CC4 uses a reading that the
  frozen wording does not state and arguably disfavours. One alternative is a test-level comparison of the
  derived `(P, V)` values: `(½, ½)` against `(√2/2, √2/2)`. §3.4 should say that CC4's T7 separation is
  verified only under a reading that does not compare laws.
- *The decision function never reads `separated`.* Row 0 of the decision function (MR★:1243–1248) lists no
  `control_separation` clause, while frozen 0(i) makes "a countercontrol not separated where §5.8 requires"
  `VOID` (PREREG:592–593). Whether `reference_match` covers separation is not stated. This also belongs in
  the specification-repair list of §6.

### F7 (minor).

- *CC4 primitives.* §3.2 says `DP` maps valid states to valid states. That holds only for uniform `f`
  (G-CC4-2); a biased `f` produces a non-uniform, invalid state. It should say so.
- *More CC4 gaps of the G-CC4-1 kind.* MR★:1044 excludes CC4 from the common carrier, so these are also
  undefined for CC4: the strength map `θ ↦ g = [θ ≠ 0]` (MR★:1051), which T1 needs to run at all; the T6
  settings `B₀`, `B₁` (MR★:1056); and the symbols `z_s`, `x_s` in `Q_{s₁s₂}`. The record's evident readings
  are the natural ones.
- *CC5 T5.* "`p₀ = ½`" needs `e` uniform. The frozen T5 records (order independence, dependence on
  `ϕ₁ + ϕ₂` alone) hold for any law of `e`.
- *A citation.* LIT-1-C7 sits at LOG:433–435 (a screen correction), not in LOG:55–80.
- *Consistency.* §3.2's heading lists T2 among the checked tests, but no T2 law is shown, and §7 says T2 was
  not checked beyond what is stated. I checked them: CC4's three T2 laws under the `P_bal` reading match
  B-T2.

***

## Answers to the six checks

1. **S-L3 algebra and the block swap.** (L3a), (L3b), (L3d) and P-1 re-derived: correct. The block-swap
   argument is correct and complete for global block maps `σ_X ⊕ g` and new relative to MR★. It does not
   cover the marginal reading, which fails on `ℤ/2` (F1). "VERIFIED at stated scope" is justified for S-L3's
   four bullets as stated. The authorized gloss "erasure unavailable on K1" should be VERIFIED AT NARROWER
   SCOPE, and the supplements belong to the record, not to S-L3 (F2).
2. **The side-2 case.** Correct for every axis of side 2 and `𝐑 = ℤ/2` under SM's multiset sum. The native
   scope is unaffected, because frozen K1 uses PC★2a's relation sum. "Outside the native lattice" is not the
   reason (F3).
3. **The narrowing for S3.** Correct. S-L3 excludes neither a `φ^n` that restores the carrier–marker
   preparation to one §5.3-equivalent over `Acc` (T3, PREREG:486–487), at `n` below `ord(φ)` (Acc-relative
   or orbit-level return), nor transport of the record out of the marker. To be stated precisely: transport
   relocates the record rather than erasing it, so it bears only on a marker-local reading of
   "uncomputation"; the narrowing also binds MR★'s own uses (F2); and F1's one-site `σ` should be added.
4. **CC4, CC5, CC7.**
   - Every "holds as written" that I re-derived is correct: Lemma G (i) and (ii), the CC4 spanning identity,
     CC4's T7 reference (`P = V = ½`, both pair mixtures uniform), CC5's T4 bookkeeping and C-8 mixtures, and
     CC7's `D = 0`.
   - Every "needs an unstated reading" is real: `P_bal` for CC4; the laws of `f` and `e`; the ready-marker
     content; `MK_j(0)` for CC5; CC7's marker alphabet and `RD_j(π/4)`; and (ii) for multi-bit `Λ` under
     Lemma G.
   - No verdict should be NOT VERIFIED.
   - Too generous: CC5's T7 separation "under either reading" (F4); CC7's §3.5 classification "as written"
     (F5); CC4's T7 separation, in view of PREREG:552 (F6).
   - Too strict: CC7's (ii) and T8 row, which need a nondegenerate `f`, not a uniform one (F5).
5. **The `separated` gap.** Real. The frozen "from PC-Q's law" (PREREG:552) and the decision function's
   silence on `separated` widen it (F6).
6. **Standing and provenance.**
   - The record keeps all four items as named premises until it is reviewed and accepted (§0, §6), which
     matches #1169 c.6891189024 (quoted accurately, with author and time) and c.6891241282.
   - It claims only paper verification and does not use the relayed `fc68d333` report as evidence.
   - Off-`main` references: S3-PLAN-r9 and S3-U1-r5 are read only for how they use the items (provenance).
     The PR #1023 owner decision is cited for the K1 freeze, whose content is on `main` in MR★ §K★.F (support
     on `main`). The record does not label this classification explicitly; adding it is optional.
   - No conditional claim is presented as established, apart from the attribution in §6 (F2).

## What I checked and did not check

**Checked by hand:**
- S-L3 (all bullets), P-1, P-2, S-L1, S-C1(a), and the record's block-swap and `ord(φ) | n + m` supplements;
- the side-2 case against SM:224–226, Substratum A4, MR★:358–359 and PC★:102–106;
- Lemma G (i) and (ii), including the readout-sequence reading for multi-bit `Λ`, and that 5 primitives fit
  in `T = 8`;
- CC4: primitives, spanning identity, T0–T5 under `P_bal` = "`p = 0` known", T7, the T8 rows;
- CC5: T1, T4, T5, T7 (C-8), the T8 rows, GNC;
- CC7: `V`, `D`, R1, the T8 row, the separation;
- PC-Q's B-T1, B-T2, B-T4 and B-T7 values used for comparison;
- the frozen rows PREREG:555–575, §3.4, §3.5 and 0(i);
- the record's citations of MR★, PREREG and LOG lines, and the blob ids;
- the authorization text.

**Not checked:**
- S-L4 to S-L7 and S-C4a/b, except as cited;
- CC1, CC3, CC6, CC8;
- the identification of CC4 with Catani et al. 2023's model, and LIT-1's reading of the source;
- PC-Q's other closed forms (B-T0, B-T3, B-T5, B-T6) beyond the values used;
- CC4 T6, and CC5/CC7 T2 and T6;
- §M.10's mutation table;
- whether `Φ^n_{XX} = σ_X` can hold for regions with internal edges or for `n ≥ 2`. F1 does not depend on
  this.

No control was run, and nothing was computed.
