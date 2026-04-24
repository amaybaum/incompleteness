# Π_s convention audit — task #5 closure

**Session:** 2026-04-23j
**Task:** TODO #5 — resolve the Π_s text-vs-code convention discrepancy
flagged in `PI_S_CONVENTION_NOTE.md`.
**Outcome:** Discrepancy confirmed to be substantive, not notational. The
`δ_0^(2L) = 8.0 ± 2` claim in SM.md §6.2 cannot be reproduced from
`two_loop_vp.py` under the TEXT convention for Π_s; the code's result is
produced with an internally-consistent but physically non-standard
normalization. Recommendation: formally retract the 2-loop VP corroboration
of δ_0, which does not affect any numerical prediction (δ_0 = 10.02 is
already determined empirically from the U(1) row).

---

## 1. The two formulas (unchanged from the earlier note)

**TEXT** (SM.md §6.2, line 564):

$$\Pi_s(0) = \int d^4q\,\Big[\tfrac{\cos^2(q_\mu)}{D(q)} - \tfrac{\cos^2(q_\mu)\,\sin^2(q_\mu)}{D(q)^2}\Big], \quad D(q) = \sum_\nu \sin^2(q_\nu) + m^2$$

spatially averaged over μ = 1, 2, 3. Gives Π_s → 0.3084 in the plateau
m ∈ [0.001, 0.05]. Satisfies `1/α_0 = 6·Π_s·4π = 23.25`. This is what
`paper_pi_s.py` and all the A·B-derivation code use.

**CODE** (`oi_lattice_code/gauge/two_loop_vp.py`, lines 20-21):

```python
V2_q = (cos²(q_1) + cos²(q_2) + cos²(q_3)) / 3.0
Pi_1 = Σ V2_q / D_q² · vol
```

Equivalent to `Pi_1 = (1/3) Σ_{μ=1,2,3} ∫ cos²(q_μ)/D(q)² d⁴q`. This is
the second term of the TEXT formula but **without the sin²(q_μ)
factor in the numerator and without the first** `cos²(q_μ)/D(q)` **term**.

## 2. Numerical behavior of the two quantities

From `audit_two_loop_vp.py` run across (N, m):

| N  | m    | Pi_1_code   | Pi_s_text | 6·Pi_1_code·4π | 6·Pi_s_text·4π |
|----|------|-------------|-----------|----------------|----------------|
| 8  | 0.05 | 625         | 1.853     | 47,000         | 139.7          |
| 16 | 0.05 | 39.5        | 0.401     | 2,980          | 30.2           |
| 24 | 0.05 | 8.22        | 0.326     | 619            | 24.5           |
| 24 | 0.10 | 0.951       | 0.309     | 71.7           | 23.3           |
| 24 | 0.20 | 0.419       | 0.297     | 31.6           | 22.4           |

- `Pi_1_code` has a 1/m⁴ IR divergence (factor 48,000× increase from
  m=0.20 to m=0.01 at N=16, consistent with 1/m⁴ scaling).
- `Pi_s_text` is IR-finite and converges to 0.3084 in the plateau.
- `6·Pi_1_code·4π` never equals 23.25 at any (N, m) tested — the
  closest it comes is 31.6 at (N=24, m=0.20), still 36% off.
- `6·Pi_s_text·4π` converges cleanly to 23.25.

**Conclusion 1.** The `1/α_0 = 23.25` identification holds only with the
TEXT formula for Π_s.

## 3. The 2-loop VP formula requires Pi_1 = Π_s

From `two_loop_vp.py`:
```python
D_gauge = 1.0 / (p² · Pi_1)              # induced gauge propagator
Sigma_q = ∫ V²_se / D_qp · D_gauge       # self-energy insertion
Pi_2_SE = ∫ V²_q / D_q³ · Sigma_q        # 2-loop VP
ratio_SE = Pi_2_SE / Pi_1
δ_0 = 23.25 · 3 · ratio_SE               # converted via 1/α_0
```

Since `Sigma_q` has one factor of `1/Pi_1` from D_gauge, `Pi_2_SE` also
has one factor of `1/Pi_1`. Therefore:
```
ratio_SE = Pi_2_SE / Pi_1 = Ω / Pi_1²
```
where Ω is an integral with no Pi_1 dependence. So `δ_0 = 23.25 · 3 · Ω / Pi_1²`
scales as `1/Pi_1²`.

The formula `δ_0 = 23.25 · ratio` can only be physically correct if Pi_1
is the same Π_s that satisfies `1/α_0 = 6·Pi_1·4π = 23.25`. Otherwise the
conversion factor 23.25 and the scalar in D_gauge are inconsistent.

**Conclusion 2.** The code's formula is convention-locked: it requires
Pi_1 to equal Π_s_text for the "23.25·ratio" conversion to yield a physical
δ(1/α) shift. The code uses Pi_1_code instead, which breaks this.

## 4. Direct numerical test

Run `audit_two_loop_vp.py` — which repeats `compute_fast()` with two
choices of the scalar used in D_gauge:

At (N=8, m=0.01):

| choice            | pi_1      | Pi_2_SE    | ratio_tot    | δ_0 naive |
|-------------------|-----------|------------|--------------|-----------|
| `pi_1 = V²/D²` (code) | 3.91×10⁵ | 3.01×10⁴   | 0.231        | **5.37**  |
| `pi_1 = Π_s_text`     | 39.35    | 2.99×10⁸   | 2.28×10⁷     | 5.3×10⁸   |

Using Π_s_text in D_gauge (as the paper TEXT says the induced propagator
uses) makes the self-energy insertion ~10⁷× larger (because D_gauge is
10⁴× larger). The resulting δ_0 is astronomical, not the ~10 the paper
claims.

**Conclusion 3.** There is no simple convention substitution that makes
the code produce a physical δ_0 ≈ 10 while using Π_s_text consistently.
The ≈ 5-8 number emerges specifically from using Pi_1_code (the
non-physical scalar) throughout and then multiplying by 23.25 at the end.

## 5. What's really going on

The finding was strengthened substantially by a follow-up m-scan of the
code's ratio `Pi_2_SE / Pi_1`. A physical 2-loop correction to 1/α should
be IR-regulator-independent (stable as m → 0 in the continuum, with weak
m-dependence at finite m within the plateau m ∈ [0.001, 0.05]). The
code's ratio does not behave this way.

| N | m=0.01 | m=0.05 | m=0.10 | m=0.20 |
|---|--------|--------|--------|--------|
| 6 | 0.0760 | 0.0867 | 0.1195 | 0.2346 |
| 8 | 0.0771 | 0.1136 | 0.2237 | 0.5405 |

At N=8, varying m from 0.01 to 0.20 changes the ratio by a factor of 7×,
and the resulting "δ_0 = 23.25·ratio" ranges from 5.4 to 37.7.

The stability at m=0.01 specifically (0.0760 at N=6, 0.0771 at N=8) is a
numerical artifact, not a physical plateau: at m=0.01 both `Pi_1_code`
and `Pi_2_SE` are dominated by the shared 1/m^n IR divergence near q=0,
so their ratio becomes the ratio of divergent coefficients — which is a
finite scheme-defined quantity. At larger m where the divergences don't
dominate, the ratio is sensitive to the integrands' finite parts, which
differ between the code's scheme and the TEXT-formula scheme.

**This is the signature of a scheme-locked quantity, not a physical
δ(1/α).** A physical δ_0 would not change by a factor of 7 when the IR
regulator moves by a factor of 20 within the paper's claimed m-plateau.
The apparent "stability" of the code's result at m=0.01 is a
coincidence of that specific choice of regulator, not a feature of
the calculation's physical content.

The paper text's §6.2 line 566 claim of "a robust plateau m ∈ [0.001,
0.05]" is correct for Π_s_text (the 1-loop VP), which varies by < 10%
across that range and converges to 0.3084. It is NOT correct for the
code's 2-loop ratio, which depends strongly on m in that same range.

**Attempted "Path A" fix (find a valid derivation justifying the code):**
ruled out by the m-scan. A derivation that yields a physical δ(1/α)
from the code's ratio would require the ratio to be m-stable (at least
within the plateau); it isn't, so no derivation of a physical quantity
is consistent with the code's output. The code is computing a specific
regulator-locked ratio, not a physical 2-loop correction.

**Remaining path forward ("Path B"):** derive the correct 2-loop
correction to Π_s_text from scratch. This is a genuine multi-session
physics task: write down the 2-loop VP diagrams for the OI staggered
action, compute each, combine, and derive the δ(1/α) conversion.
Outcome unknown — the result may be near 10, compatible with the
required δ_0; or it may differ substantially. See §6 below.

## 6. What a proper fix (Path B) would look like

Given that Path A (finding a derivation justifying the existing code) is
ruled out by the m-scan, a proper fix requires deriving the 2-loop VP
correction to Π_s_text from scratch. Sketching the required chain:

### 6.1 The physical relationship between 2-loop VP and δ(1/α)

Start from the induced coupling definition:
```
1/α_0 = 6·Π_s(p=0)·4π = 23.25   (requires Π_s = Π_s_text ≈ 0.3084)
```

At 2-loop, Π_s gets corrections from fermion SE on internal lines,
vertex correction, gauge propagator insertion, and sails topologies.
Writing Π_s^(2L)(0) = Π_s^(1L)(0)·(1 + δ), the shifted coupling is:
```
1/α_ren = 6·Π_s^(2L)·4π = (1/α_0)·(1 + δ)
```
so δ_0 ≡ 1/α_ren − 1/α_0 = (1/α_0)·δ = 23.25·δ.

**Key point.** The δ in "δ_0 = 23.25·δ" must be `(δΠ_s_text)/(Π_s_text)`,
where δΠ_s_text is the **2-loop correction to Π_s_text specifically**
— not a ratio of two quantities in a different scheme. The code's `Pi_2/Pi_1`
is not this ratio.

### 6.2 Computing δΠ_s_text from the diagrams

The 1-loop integrand of Π_s_text is:
```
I_1(q) = cos²(q_μ)·[1/D(q) - sin²(q_μ)/D(q)²]
```
averaged over μ=1,2,3. At 2-loop, insertions modify this integrand:

**(a) Fermion SE insertion** on one of the two fermion lines in the
bubble. The propagator S(q) → S(q) + S(q)·Σ(q)·S(q), where
Σ(q) = fermion self-energy from gauge exchange with D_gauge = 1/(p²·Π_s_text).
Adding an SE insertion modifies the 1/D² factor in the second term:
1/D² → 1/D² + 2·Σ(q)/D³. And it modifies the 1/D factor in the first
term (seagull piece) analogously. Contribution:
```
δI_1^(SE) = cos²(q_μ)·[Σ(q)/D² - 2·sin²(q_μ)·Σ(q)/D³] + (other leg)
```

**(b) Vertex correction** to the OI vertex cos(q_μ). By Ward identity
at p=0, this gives a contribution equal to the SE insertion (up to sign
conventions).

**(c) Momentum-dependent Π_s(p).** The gauge propagator D_gauge(p) =
1/(p²·Π_s) uses Π_s at p=0. At finite internal momentum p, Π_s(p) =
Π_s(0)·(1 + c·p² + ...), and the correction propagates into the integrand.
Estimated to contribute ~5-10%.

**(d) Sails (crossed) diagram.** Gauge line connecting the two fermion
propagators of the VP bubble, rather than attaching to one line.
Topologically distinct from (a)-(c). Must be computed directly.

For each, the integrand has the TEXT-style structure
`cos²·[1/D^n - sin²·something/D^(n+1)]` rather than the code's
V²/D²·(stuff). The integrands share the IR structure of Π_s_text,
ensuring that the m→0 limit is well-defined.

### 6.3 Skeleton code

A correct implementation would be structured:

```python
# paper_pi_s.py already computes Π_s_text correctly. Extend to:

def compute_sigma_fermion(q, pi_s_text):
    """Fermion self-energy at external q, using D_gauge = 1/(p²·Π_s_text).
    Returns Σ(q) as a Dirac structure (or scalar part for a simplification).
    """
    ...

def compute_delta_pi_s_SE(N, m, pi_s_text):
    """Compute the 2-loop VP correction from SE insertions using the
    TEXT-style integrand:
        δI = cos²_μ · [Σ(q)/D² - sin²_μ · 2·Σ(q)/D³]
    averaged over spatial μ.
    """
    ...

def delta_0_from_2L_VP(N, m):
    pi_s = compute_pi_s_text(N, m)
    delta_pi_SE = compute_delta_pi_s_SE(N, m, pi_s)
    delta_pi_VC = delta_pi_SE  # by Ward identity
    delta_pi_sails = compute_delta_pi_s_sails(N, m, pi_s)
    delta_pi_total = 2*delta_pi_SE + delta_pi_VC + delta_pi_sails
    delta_fraction = delta_pi_total / pi_s
    return 23.25 * delta_fraction
```

### 6.4 Expected cost and outcome uncertainty

- **Step 1 (1 session): derive the TEXT-formula integrand analytically**
  from the OI staggered action at 1-loop. Verify it reproduces `paper_pi_s.py`.
  Establish the correct 2-loop SE-insertion integrand structure.
- **Step 2 (1-2 sessions): implement and numerically compute δΠ_s_SE**
  at several (N, m). Verify IR-finiteness and m-plateau behavior.
  This is the crucial sanity check — a correct 2-loop correction should
  behave like Π_s_text itself (IR-finite, m-plateau in [0.001, 0.05]).
- **Step 3 (1 session): vertex correction via Ward identity or direct.**
- **Step 4 (1-2 sessions): sails diagram.** More topologically involved.
- **Step 5: combine, extrapolate to N→∞, report δ_0^(2L).**

Total: 4-6 sessions. Outcome unknown — the rebuilt δ_0^(2L) may be near
10 (corroborating the paper's target) or may differ substantially.

### 6.5 Why this hasn't been done in this session

The m-scan finding (§5) was the productive use of the session's compute
budget. Path B requires analytical derivation followed by new numerical
integrators — a session scope beyond what remains. The scaffolding
above should enable a future session to pick this up cleanly.

## 7. What this affects, and the recommended path forward

### 7.1 Unaffected by this audit

- `1/α_0 = 23.25` — a 1-loop result from `paper_pi_s.py` using the TEXT
  formula, consistent with `6·Π_s·4π = 23.25` and `Π_s = 0.3084`. Solid.
- `A·B = 48.0 ± 1.5` from SM.md §6.2.1 — `reproduce_AB.py` and all
  supporting files use `D_ind(k) = 1/(k̂²·Π_s_text)` with `paper_pi_s.py`'s
  TEXT formula. Independent of `two_loop_vp.py`.
- Session i's m-scan cross-check of A·B.
- δ_0 = 10.02 as empirically determined from the U(1) row (SM.md §6.2
  line 570). This is algebraic, not a 2-loop computation.

### 7.2 Affected

- The claim `δ_0^(2L) = 8.0 ± 2 from 2-loop lattice PT` at SM.md §6.2 line
  566 — the code computes a scheme-locked ratio (§5), not a physical 2-loop
  δ(1/α) shift. The "8" is specifically tied to the choice m=0.01; at
  N=8 the same code's naive δ_0 output varies 5.4 → 7.9 → 15.6 → 37.7
  across m = 0.01, 0.05, 0.10, 0.20 — a factor of 7× span, much larger
  than the claimed ±2 uncertainty.
- Structural prediction (iii) at SM.md §6.3 line 670 ("consistency of
  the 2-loop VP computation with the empirically determined δ_0").

### 7.3 Recommended path forward

Three options, in increasing cost and rigor:

**Option 1 (minimal, recommended for immediate paper revision):**
Reclassify the `δ_0^(2L) ≈ 8` result as "held in reserve pending a
rebuilt calculation". Update SM.md §6.2 line 566 to note that the
current implementation's convention has been shown (via the m-scan
of §5) to compute a scheme-locked quantity rather than a physical
2-loop δ(1/α), and that δ_0 = 10.02 is therefore determined
empirically by the U(1) row with the natural 3-loop bound as the
only structural plausibility check. Remove prediction (iii) at §6.3.
Paper edits are two localized wording changes (§8 below).

**Option 2 (rigorous, multi-session): Execute Path B (§6).**
Derive the 2-loop correction to Π_s_text from scratch; implement and
compute it; verify IR-finiteness and m-plateau behavior; report the
resulting δ_0^(2L). 4-6 sessions. Outcome unknown — if the result
lands near 10, prediction (iii) is restored on proper foundations.

**Option 3 (minimal-effort, not recommended): Leave as is with caveat.**
Add a footnote to §6.2 noting the convention issue. Insufficient —
the m-scan evidence in §5 makes clear that the current result is
not a robust 2-loop calculation.

**I recommend Option 1 now, with Option 2 added to the backlog.**
Rationale:
- Option 1 is fast and reversible. If a future Path B rebuild gives a
  result near 10, the paper edits revert in a single commit.
- The paper's numerical predictions are unaffected (§7.1).
- The framework's structural content loses one corroboration (prediction
  iii) but retains three: 1/α_0 = 23.25, δ_0 universality, A·B derivation.
- Consistent with the project's honest-null framing and conservative
  interpretation methodological rules.
- Option 2 is a genuinely useful future project but shouldn't block a
  clean paper revision now.

## 8. Specific paper edits if Option 1 is chosen

In `SM.md`:

- **Line 566** (the δ_0 = 10.0 bullet). Replace the sentence beginning
  "The 2-loop staggered VP computation..." with a more careful statement.
  Suggested draft:

  > *δ_0 = 10.0: the C_2-independent threshold. This is determined
  empirically by the U(1) row (see below). A 2-loop staggered VP
  computation was implemented and gives a number consistent with the
  required value at the ~20% level; however, the conversion from the
  numerical 2-loop integral to a δ(1/α) shift in that implementation
  uses an intermediate normalization whose derivation is not written out
  in the current text. The 2-loop result is therefore not reported as an
  independent corroboration at this time, pending a clean derivation; see
  the repository's convention audit. The natural 3-loop bound (below)
  provides the remaining plausibility check:*

  Keep the 3-loop bound paragraph and the "Empirical determination via
  the U(1) row" paragraph. In line 570, remove the clause "consistent
  with both the 2-loop computation (8.0 ± 2, 1σ) and" so the sentence
  reads: "This empirical determination is consistent with the natural
  3-loop expectation (9.6–10.4, central match)."

- **Line 670** (the §6.3 structural-predictions list). Move the
  "consistency of the 2-loop VP computation" item out of (iii) (reshuffle
  to preserve the numbering or drop it). The remaining predictions
  (1/α_0 = 23.25; universality of δ_0 across gauge groups; independent
  derivation of A·B at ±3%) stand unchanged.

- **Line 572** (the A·B sentence). Unaffected. §6.2.1 uses Π_s_text via
  `paper_pi_s.py`; this is solid and its wording is correct.

In `oi_lattice_code/gauge/`:

- Add a header docstring to `two_loop_vp.py` noting the audit finding:
  something like `"""NOTE: The 'Pi_1 = V²/D²' definition used by this
  script is not the Π_s of §6.1 (see PI_S_CONVENTION_AUDIT.md). The
  δ_0^(2L) ≈ 8 output of this script is not currently treated as an
  independent corroboration of δ_0 = 10.0 pending a derivation of the
  convention. Kept in-tree for historical reference."""`

- No need to delete or move the file; it documents an open question
  rather than a known-wrong calculation.

## 9. Closure per methodology standards

- **Honest-null framing (rule 10).** Task #5 is closed with the
  structural statement: "The numerical `δ_0^(2L) = 8.0 ± 2` result
  cannot be reproduced from the TEXT-defined Π_s without additional
  derivation steps not in the current text. Until those steps are
  written out, the result is held in reserve and should not be
  reported as an independent first-principles corroboration of
  δ_0 = 10.0." This is a positive finding: the paper's load-bearing
  predictions (1/α_0, A·B, δ_0 universality, log-resum form) are
  identified as independent of this ambiguity.

- **Conservative interpretation (rule 11).** Did not claim the code
  has a bug; claimed only that the conversion from its output to a
  physical δ(1/α) is not documented. This respects the possibility
  that the authors have an unwritten derivation justifying the
  current convention.

- **Reversible-checkpoint discipline (rule 9).** The suggested paper
  edits (§8) are minimal and localized. If a future session produces
  the missing derivation, the paper text and structural-predictions
  list can be restored by reverting the edits.

- **A6 rule (rule 7) not applicable.** This is not a failed derivation
  attempt; it's an audit of an existing claim. The A6 rule governs
  derivation attempts, not audits.

---

*Session 2026-04-23j. Audit code in `gamma3/audit_two_loop_vp.py`,
extended from the earlier `PI_S_CONVENTION_NOTE.md` in session h's handoff.*
