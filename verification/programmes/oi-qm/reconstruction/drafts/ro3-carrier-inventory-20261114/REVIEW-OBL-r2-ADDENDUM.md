CONFIRMED — at `ef8d353e4c05e6e4de2f813478bc279f3fa00eb4`, `OBL-RO3-2-r2.md` and `RO3-INVENTORY-r4.md` keep (a), (b) and (c) distinct; every link between them states its implication and hypotheses (four nonblocking nits)

# Addendum to REVIEW-OBL-r2: separation of recurrence, exact return and P-indivisibility

The three properties:
- **(a)** Recurrence of individual configurations or measurable sets almost everywhere, at times that
  depend on the point (Poincaré recurrence).
- **(b)** Exact return of every visible cell at one common positive time: `Γ_n = I`, equivalently
  `π ∘ F^n = π` almost everywhere.
- **(c)** P-indivisibility of the rooted transition family.

The texts also use a fourth property, **(m)**: exact microscopic return, `φ^L = id` (inventory 1.1).
It is neither (a) nor (b), so links through it are listed too.

The texts were read in full at the commit above. Paper-only and read-only.

## Links in OBL-RO3-2-r2.md

| Line | Link | Justified? |
|---|---|---|
| 215–216 | (b) `Γ_n = I` ⟺ `π ∘ F^n = π` almost everywhere | Yes. This is a restatement within (b), by `measuredGamma_eq_one_iff`. Only the forward direction is used. See nit n2 on that theorem's hypothesis that every cell has positive mass |
| 217–220 | (b) at `n` ⟹ (b) at every `kn`; mixing ⟹ not (b) | Yes. The first step uses measure preservation. The second uses mixing along `kn` and two cells of positive measure. Neither step uses (a) or (m) |
| 229–231 | mixing ⟹ every row of `Γ_t` tends to the marginal; Main:155's late-time form | Yes. This is a statement about rows only. No inference is made to (c) |
| 234–238 | not (m): `F^n ≠ id`; no nonzero finitely supported periodic configuration | Yes, from Step 8 and Steps 5–7. Not (b) is never inferred from not (m): 3.1 proves not (b) directly from mixing |
| 239–241, 259–260 | (a) holds | Yes. Measure preservation on a compact metric probability space gives it. The text explicitly does not use (a) to obtain (b), or (b) to refute (a). Since 3.1 refutes (b) in the same system, the pair exhibits (a) ⟹̸ (b) without saying so. See nit n1 |
| 242–258 | (m) on a `μ`-null set of points; periodic points `μ`-null | Yes, by ergodicity and full support. No inference is made to (b): a null set of exactly periodic points gives no return of a cell |
| 263–269 | not (b) ⟹ the route "(b) together with an earlier non-permutation or overlapping rooted map ⟹ (c)" is unavailable | Yes. Every cited theorem (Main:121, :135–137, :141–143; GR:587; `RecurrenceHorizon.lean:119`; `ObservableFactorRecurrence.lean:68`) consumes (b). The text identifies (b) as the hypothesis consumed. Main:121 reaches (b) through (m), stated as "through `φ^N = id`". The route's other hypotheses are not restated, but nothing depends on them: the claim is only that a necessary hypothesis fails. Line 264 says "the route itself is not refuted" |
| 270–275 | mixing ⟹ no near-total common return at late times; bounded times open | Yes. The `δ` bound is sufficient. Main's continuous-time theorem is not applied to discrete `F`; only its hypothesis is examined |
| 276–278 | not (b) ⟹̸ P-divisibility; (c) open | Yes. The text states explicitly that it shows neither P-divisibility nor its negation, and needs another mechanism |
| 279 | readback-lemma memory is unaffected | Yes. Conditional memory is kept apart from (c), as at Main:157 |
| 339–340 | non-ergodicity in the countercontrols is "consistent with" exact return of the named readouts | Yes. This states consistency with the sources' (b) instances, not an implication |
| 376–378 | the summary rows for 3.1–3.3 | Yes. They match the body: (b) refuted; route unavailable; (c) open |
| 388–396 | inventory moves, as proposals: 1.2 refuted within the class; the 1.3 route unavailable; 1.1 I-qloc context unchanged | Yes. The separation is preserved: 1.1 (m) is not moved on the strength of not (b) |

## Links in RO3-INVENTORY-r4.md

| Line | Link | Justified? |
|---|---|---|
| 109–112 | carrier-level recurrence vs rooted-map P-indivisibility: "does not transfer ... without a stated map" | Yes. This is a general guard |
| 148, 165 | F: (m) ⟹ (b) under H-product | Yes. The sources are Main:137 and `rootedMap_at_order`, and the hypotheses are listed |
| 167–168 | G-sub and G-fact: (b) on the stage or factor | Yes. Conditional, with the hypotheses stated |
| 154 | I-meas, (m) open "as a microscopic statement"; "see 1.2" | Yes. Its RR source, `continuous-substates/README.md:85–91`, states that pointwise recurrence (a) does not give `Γ_L = I` |
| 171 | I-meas: (b) ⟺ `π ∘ T^L = π` almost everywhere; mixing flows fail late-time near-return | Yes. The convention and the positive-finite-mass hypotheses are stated |
| 174–179 | mixing ⟹ not (b), in discrete time | Yes. The context is [IR], and "no cell above rests on it". It is now proved in OBL 3.1 |
| 191–194 | F, G-sub, G-fact: (b) + non-permutation rooted map ⟹ (c) | Yes. Hypotheses listed. Scope: "recurrence-cycle result" only |
| 197 | I-meas: (c) conditional on (b), a row-stochastic rooted family, a root-shared prior and an earlier non-permutation `Γ_s`; "without the return hypothesis: open" | Yes. Not (c) is never inferred from not (b). RR context records P-divisible infinite families, with no implication claimed |
| 370–371, 418–420 | I-deep and I-meas need (b) or a replacement; 1.3 is conditional on 1.2 | Yes. See nit n3 on the citation at 418–419 |
| 440 | I-nonorm: no rooted law; a remark on (a) | No link to (b) or (c). See nit n4 |
| 485–486, 492–494 | proposal: mixing ⟹ not (b), then the route to (c) unavailable, with (c) needing "a different proof" | Yes. Not (c) is not inferred |
| 512–517 | countercontrols: (b) instances on other carriers | Yes. Stated as source facts |

No passage in either file infers (b) from (a), infers (c) from (a), or infers not (c) from not (b).
No passage presents (m) as (a). Every inference from (b) to (c) names the extra hypotheses (a
non-permutation or overlapping earlier map, row-stochasticity, a root-shared prior), or is stated
only as "the route is unavailable".

## Nonblocking nits

- **n1. OBL lines 239–241 against 262–265, and r4 line 493.** "Recurrence" names (a) in 3.2 and the
  route through (b) in 3.3. A clause after line 241 would remove the overload. Suggested wording:
  "Poincaré recurrence does not supply `Γ_n = I`: its return times depend on the point, and 3.1
  excludes a common exact return." This is Main:155's own distinction.
- **n2. OBL line 215.** `measuredGamma_eq_one_iff` assumes that every cell has positive, finite mass.
  The definition at line 211 requires only two cells of positive measure.
  - The forward direction still holds: in the kernel convention a null cell's row is zero, so
    `Γ_n = I` forces every cell to have positive mass.
  - Either say this, or restrict `V` to the cells of positive measure. For `π = res_Λ` every cell is
    positive.
- **n3. r4 lines 418–419.** The Main:155 citation supports the failure of (b) for mixing flows. It
  does not support the non-inheritance of 1.1 (m), although it is attached to "1.1 and 1.2". The
  claim of non-inheritance is true without it. Attach the citation to 1.2 only.
- **n4. r4 line 440.** "Poincaré recurrence needs a finite invariant measure" is a sufficient
  condition stated as a necessary one: conservative infinite-measure systems also recur. It is
  attributed to the #1055 body and is outside OBL-RO3-2. Suggested wording: "Poincaré recurrence is
  not available without a finite invariant measure or conservativity."
