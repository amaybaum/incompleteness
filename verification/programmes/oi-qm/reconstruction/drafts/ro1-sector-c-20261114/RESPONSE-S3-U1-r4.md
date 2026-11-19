# Response for S3-U1-r4: the owner-confirmed fix and the two confirmation nits

**Inputs.**
- The fix on separable non-affine value writes, relayed by the coordinator with the owner's
  confirmation: "Confirmed, proceed as suggested" (`amaybaum`, 2026-11-15).
- The confirmation of r4, `REVIEW-S3-U1-r4.md`: ACCEPT at `7887d33f`, with nits n1 and n2.

**Revision.** `S3-U1-r5.md` applies the fix, n1 and n2, and nothing else.
- r4 is left unchanged; I checked that it is byte-identical to the branch copy.
- r5 is unreviewed and paper-only, under #1169 c.6890079967.
- No new premise is adopted. The S7 and O11 stops, S5's separation, H-RR as a hypothesis, AC-1 and
  SNR-1 are unchanged.

## The fix: separable non-affine value writes. Applied.

**The error, checked.** r4 said that a value write `z ⊕ f(h)` with `f` not affine over several
record factors is I-sel. That is false. Take `z′ = z + h₁² + h₂²` over `ℤ/3`:
- `g(h) = h²` sends `0, 1, 2` to `0, 1, 1`, so `g` is not affine;
- with selector `{h₁}` and carrier `{h₂}`, the outputs are `(0, 1, 1)` for `h₁ = 0` and `(1, 2, 2)`
  for `h₁ = 1, 2`;
- the partition of `h₂` is `{{0}, {1, 2}}` every time;
- the reversed pair is the same by symmetry, and a pair with `z` as carrier is a translation;
- so the write is I-off.

**What r5 does (§4.2).** It removes the blanket rule. Value writes are classified by the explicit
partition test over every selector/carrier pair of declared factor sets (P1(a)). The test is stated
on the region holding `z′`. Adding kept factors to the readable region joins the partition with
partitions that do not depend on the selector, so it cannot change the class. `z` itself never
selects.

**Conditions, each checked by hand ([A-inf]).**
- **Sufficient for I-off.** Each of these makes every comparison a constant shift:
  - `f` affine;
  - a single-factor record;
  - `f` additively separable across the split, `u(h_S, rest) + v(h_C, rest)`. Separable across
    every split, for example `Σᵢ gᵢ(hᵢ)`, means the whole write is I-off.

  These are stated as sufficient, not necessary: an injective map composed after a separable form is
  also I-off.
- **Sufficient for I-sel.** A split where the selector's value changes the partition induced on the
  carrier. `x∧y` is the example: constant for `x = 0`, injective for `x = 1`.
- **Binary factors with XOR.** [A-inf] Here the write is I-off exactly when `f` is affine. If `f` is
  not affine, some second difference `D_i D_j f` is nonzero, so the selector `{h_i}` changes the
  partition of `{h_j}` from one class to two. So r4's rule was correct on bits and false on larger
  alphabets.
- **Worked control.** The `ℤ/3` write above is included as the worked control.

**Sites reconciled.**

| Site | r5 |
|---|---|
| §4.2, the value-write bullet | Defers to the test; the write falls under C-INT when the test makes it I-sel |
| §4.2(iv) | Class by the test. D5 leaves affine value writes in place. A value written by a function that is not affine needs a rule that is not affine, whether the write is I-sel or I-off |
| §4.3, the I-off list | A value write that passes the test, with the three sufficient conditions as examples; `x∧y` is I-sel |
| §4.3, the R-lin line | "A value write whose function is not affine is not effected by an affine `φ`, whatever its class" |
| §4.7(i) | "I-off or I-sel by §4.2's partition test" |
| §4.7(iv) | n1, below |
| §5.2, the S-A2 row | Classification by the explicit test, with the conditions and the control in §4.2 |
| AW-5 | n2, below |
| AW-7 | Restated, below |
| §9, composition row | n1, below |

**The SEL-EXCL-1 statement, at its correct scope (AW-7).** r4's "generically I-sel" is removed.
- Over binary factors written by XOR, a policy is I-sel exactly when it is not affine.
- Over larger alphabets, policies that are separable but not affine are I-off.
- U1 makes no generic claim. U2 applies the test per policy on the declared factors.

**Confirmations.**
- **`T` stays I-sel.** Selector `{x}`, carrier `{y}`: the map `y ↦ B₀⊕r⊕(x∧y)` is constant for
  `x = 0` and injective for `x = 1` (§4.2 example; §5.1(iv) unchanged).
- **The R-lin conclusions are unchanged.**
  - An affine `φ` gives no I-sel for any pair of factor sets (D5, OA1:176–183), and affine value
    writes stay in place.
  - A value write whose function is not affine is not effected by an affine `φ`, whatever its class.
    The previous wording, "is I-sel and not affine, so it is not available", is replaced by this one,
    with the same conclusion.
  - The §9 intervention and composition verdicts are unchanged in substance.
- **No coverage claim depends on the change.**
  - U1's coverage half is "criterion-neutral, coverage absent by model" for bare models (§5.3).
  - No coverage statement uses an adaptive setting value.
  - The reclassification moves some value writes from I-sel to I-off. That changes which requirement
    they meet, not whether any program U1 treats as available is available.
  - The confirmation of r4 found likewise (its §2, "Coverage after the reclassification").

## Nits

| # | Disposition | Where |
|---|---|---|
| n1 | Applied. §4.7(iv) now reads "Affine adaptive setting values are not excluded there by D5; a value write whose function is not affine is not effected there". The §9 composition row now reads "affine adaptive setting values not excluded there by D5" | §4.7(iv); §9 |
| n2 | Applied under the corrected classification. AW-5 now reduces adaptive values to a record-conditioned value write with a blank target (C-PREP), "or to C-INT when §4.2's test makes the write I-sel (for example a write by a function such as `x∧y`)". This keeps the nit's intent, C-INT for the I-sel case, without reinstating "non-affine" as the condition | AW-5 |

## Not changed

- Everything else is as in r4. That includes the verdict, AD-1, the four outcomes, the comparison-tick
  rule, the S7(a) stop and its narrowing, AW-3, the §5.1(iv) table, and NC-1's standing.
- The r4 revision block is kept as history. Its line "scoped to a function affine in the record's
  factors, or to a single-factor record" describes r4.

## Not checked in this revision

These are as in r1–r4:
- the Lean statements;
- the internal proofs of the records cited;
- whether Theorem N's criteria are at least as weak as C-RET's;
- NC-1's clauses (A1)–(A3) and (A5).
