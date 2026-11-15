# Confirmation of S3-U1-r5

**Objects.** `S3-U1-r5.md` (SHA-256 `03d9f20e…7793`) and `RESPONSE-S3-U1-r4.md`, in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at PR #1294 head
`7791c640cb13eb5c6f0be618cba445089efeda18`.
- r4 is unchanged from `7887d33f`.
- The retained `REVIEW-S3-U1-r4.md` is byte-identical to the reviewer's file.

Both were checked.
**Reviewer.** The same separate non-author reviewer. Read-only. The algebra below was checked by
hand; no computation was run.

## Verdict: ACCEPT. r5 is ready for ChatGPT's exact-head review at `7791c640`

The `ℤ/3` control is correct, and every site of r4's rule is reconciled. The binary-XOR "exactly
when affine" claim holds in both directions under the test as defined, which fixes the rest. The
sufficient conditions are stated as sufficient only. `T`, the R-lin conclusions and the coverage
statements stand, and the diff changes nothing else. Three nits follow (§3). None affects a verdict.

## 1. The checks

**(1) The `ℤ/3` control is correct.**
- In `ℤ/3`, `h²` maps `0, 1, 2` to `0, 1, 4 ≡ 1`. An affine `g` with `g(0) = 0` and `g(1) = 1` is
  the identity, so `g(2) = 2 ≠ 1`, and `g` is not affine. Hence `f(h₁, h₂) = g(h₁) + g(h₂)` is not
  affine.
- For each fixed `h₁`, the map `h₂ ↦ g(h₁) + g(h₂)` is a translate of `g`, with level sets
  `{{0}, {1, 2}}`. The pair `({h₂}, {h₁})` behaves the same way.
- The remaining pairs are all translations. These are the pairs with `z` as carrier, with `z` in the
  selector, and with selector `{h₁, h₂}` and carrier `{z}`.
- So the write is I-off, and r4's blanket rule fails on it.

**(2) Every site of the old rule is reconciled.**
- Grep of r5 for "non-affine", "generically", "not affine", "I-sel otherwise" and "over several
  factors" finds only these:
  - the header's description of the fix (r5:12);
  - the §4.2 test and its control (r5:376–388);
  - consistent scoped statements (r5:395–396, :407, :438–439, :694, AW-7 at :899);
  - the unrelated OA-1 row "Non-affine rules" (r5:492).
- r4's "generically I-sel" is gone. AW-7 now says that U1 makes no generic claim, and that U2 applies
  the test per policy.
- n1 is applied at r5:693–694 and in the §9 composition row. n2 is applied in AW-5.

**(3) The binary-XOR claim is correct in both directions.** Setting: `f : 𝔽₂^k → 𝔽₂`,
`z′ = z ⊕ f(h)`.
- *Affine ⇒ I-off.* This is the first sufficient condition. Every comparison is a constant shift.
- *Not affine ⇒ I-sel.*
  - `f` is not affine exactly when its algebraic normal form has degree ≥ 2. Take a monomial of
    maximal degree containing variables `i ≠ j`. Then `D_i D_j f` is a nonzero polynomial, so
    `D_i D_j f(a) = 1` at some point `a`. In characteristic 2, `D_i D_i f ≡ 0`, so the pair must have
    `i ≠ j`.
  - Fix every factor other than `h_i` and `h_j` at its value in `a`. Over `𝔽₂`, `D_j f` does not
    depend on `h_j`.
  - The partition of `h_j`'s two values is therefore a single class when `D_j f = 0`, and two classes
    when `D_j f = 1`.
  - Since `D_j f` differs between `h_i = a_i` and `h_i = a_i ⊕ 1`, selector `{h_i}` and carrier
    `{h_j}` give I-sel at that fixed rest.
- *What the result depends on.* It needs the test's fixed-rest form: I-sel holds if the partition
  changes for some fixed rest. Example: for `f = h₁h₂h₃`, `D₁D₂f = h₃`. The selection appears at
  `h₃ = 1` and not at `h₃ = 0`; the existential quantifier makes the write I-sel.
- *If the rest were averaged.* Under averaging the I-sel direction could fail. That is the flag case
  of §4.3, and the test does not average.
- *Counterexample.* None exists under the stated test. The [A-inf] label is appropriate.

**(4) The sufficient conditions are stated as sufficient only.**
- §4.2 states "These conditions are sufficient, not necessary", with the injective-composition
  example. That example is correct: the level sets of `φ(c + v(h_C))` are those of `v` when `φ` is
  injective.
- The I-sel bullet, "Some split where the selector's value changes the partition", is in fact the
  criterion itself, so calling it sufficient is harmless.
- "The region holding `z′` decides the class" is right for both directions:
  - adding kept factors to the readable region takes a meet with partitions that do not depend on
    `h_S`, so it cannot create I-sel;
  - I-sel is existential over `Y`, so the `z′` region alone exhibits it where it exists.

**(5) `T`, R-lin and coverage still hold.**
- *`T`.* `T` writes `f(x, y, r) = r ⊕ xy` into `B` over `𝔽₂`. This `f` is not affine, and selector
  `{x}` with carrier `{y}` gives I-sel, as before.
- *R-lin.* An affine `φ` effects no write whose function is not affine, of either class. D5's I-sel
  negative is unchanged (r5:438–440).
- *Coverage.* No coverage claim depends on the change. The only availability-facing statements are
  "affine adaptive setting values are not excluded by D5" and "a value write whose function is not
  affine is not effected there". Both are correct and scoped. The AC-1 report and the four outcomes
  are untouched.

**(6) The diff changes nothing else.** The r4→r5 diff of the note touches only the following:
- the header;
- §4.2: the value-write entry, the new test block and the (iv) paragraph;
- §4.3: the I-off list and the R-lin line;
- §4.7: (i) and (iv);
- the S-A2 row of §5.2;
- AW-5 and AW-7;
- the §9 composition row.

## 2. Status discipline

- No new premise.
- The test is U1's [P]; its checks are marked [A-inf].
- No conditional result is stated as established.
- No off-`main` reference is added.

## 3. Nits (optional)

- **n3.** AW-7 (r5:899) says "policies that are separable but not affine are I-off". Write
  "separable across every split", as §4.2 does. Separability across one split is not enough.
- **n4.** In the binary bullet of §4.2, write `i ≠ j`, and add the reason a non-affine `f` has such
  a pair: its normal form has degree ≥ 2.
- **n5.** The owner confirmation, "Confirmed, proceed as suggested" (`amaybaum`, 2026-11-15), is
  quoted without a time or a record, and no comment id is given. §A.42 item 7 asks for author and
  time. The correction rests on its own algebra, not on that confirmation. Add the time, or
  "(chat, relayed by the coordinator)".
