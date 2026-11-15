# Focused review of GAMMA-1 unit G1, r4 (owner answers applied)

**Objects.**
- PR #1294 at `caa389cb91f9b13c01bf04c7f821e922adfff52e`, directory
  `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`:
  - `GAMMA-G1-r4.md` (r4:N);
  - `RESPONSE-G1-r3-OWNER.md` (RESP).
- r3 is unchanged at blob `20166317`, identical at `b3c79f60` and `caa389cb`.
- The owner record #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z), read through the API.
- U4 r2 (blob `d8cced4c`), U4 r3 (blob `54ee9629`) and U4-CALC r2, compared where r4 cites them.

**Reviewer.** Independent, non-author. Read-only; hand checks only.

## Verdict: ACCEPT WITH CHANGES (minor only)

All six answers are applied exactly as worded, and the r3→r4 diff contains nothing beyond them and
their necessary consequences. The added record laws, masses, `K_P`/`K_C` and the O11 stop check out by
hand. The sensitivity set is declared in advance and not fitted. The stability claim is limited to the
hand checks, and it holds there under two conditions that need stating (m2). Both `κ_det` instances
are kept separate, and CC4/CC5 credit does not count. There are three minor findings. None changes a
verdict.

## 1. The answers, and the diff

All six owner quotations in r4:29–36 and RESP match the record. Every r3→r4 hunk (150 insertions,
83 deletions) maps to one of the answers or to a consequence RESP lists.

| Answer | Applied exactly? | Where in r4 |
|---|---|---|
| G1-A1, "all four auxiliary protocols are added" | **yes** | §1 (127); §2.4 (272–323); §9; G1-F1; the cross-propagation |
| G1-A2, "both detection-rule variants are kept, separately" | **yes** | 131–132; 507–510 |
| G1-A3, "no weights chosen before G4" | **yes** | 596–597 |
| G1-A4, "'no marker' means the coupling is absent" | **yes** | 185; the E-prep row (430); §9 |
| G1-A5, "constants fixed … sensitivity analysis over a declared set" | **yes** | 616–617; 702–726; NC-γ1; §9 |
| G1-A6, "separation by scope alone is not sufficient" | **yes** | 880–882; NC-γ6 (936, 961–962, 973); G1-F8 |

**Other changes, all consequential.**
- The scope sentence (r4:4–5).
- The revision note.
- The inputs and labels paragraph, which records U4 r3's acceptance and that the PROVISIONAL citations
  stay on U4 r2.
- The §11 rows.
- §12, rewritten as answered.

I found no unlisted change.

## 2. The four added protocols, by hand

**Encoding 1, all four by E-set.**
- *Masses.* Four disjoint incident events. Each `L_a = (ρ_a)_* L^full|_{𝔈_a}` has total mass
  `μ(z = a)`, with the blocked, undetected and failed mass inside it. The four parts enter `L^full`
  once each.
- *Sum rule.* Holds per protocol against its own unread marginal, because `π` is total on `𝓒_A`.
- *Cross-protocol equality.* `Σ_m L_{a2P} = Σ_m L_{a2C}` is a property of the model, not of the
  definitions. Correct.

**Encoding 2, blocking by E-set and the read by E-read.**
- *Masses.* Two events `𝔈_{b_L}` and `𝔈_{b_R}`. Then a2P and a2C are `(ρ_P)_*` and `(ρ_C)_*` of one
  restriction, each of mass `μ(𝔈_{b_L})`, with the runs entered once.
- *Marginals.* `Σ_m L_{a2P}(s, m, ·) = Σ_m L_{a2C}(s, m, ·) =` the unread marginal of
  `L^full|_{𝔈_{b_L}}`, identically.
- *Normalization.* `μ(𝔈_{b_π})` for both reads. Correct.

**E-prep.** r4 states that E-prep does not encode blocking, which is consistent with §4.2's "not
classified".

**`K_P` and `K_C`.**
- *Source laws.* `c_π(m)` is taken from a2P/a3P for `K_P` and from a2C/a3C for `K_C`, each over its
  own incident mass. The r2 identity `2L − 1 = Σ_m |c_L − c_R| / Σ c` applies unchanged.
- *Encoding 2.* Both statistics come from one full law per path, so the undetected mass is common to
  them. Correct.
- *Detection.* 𝔇 contains a screen detection, so `K_P`, `K_C`, `K_P^∅` and `f_∅` are computed per
  `κ_det` instance. Correct.

**The O11 stop on K1.**
- *Blocking.* Blocking is not available as a setting at D5's scope, on the factor-set condition. A
  blocked transfer is then a change of graph (MR★:471–472 [NP]), so a2P–a3C are programs of other
  geometries. Correct.
- *`K_P` itself.* `K_P` combines the L-blocked and R-blocked laws, two geometries, so on K1 it is
  itself defined only through the stop (r4:313–316). This consequence is correctly drawn.

**m1 (minor).** Under encoding 1 the a2P/a2C read switch is also an E-set read switch. On R-lin it is
not available at D5's scope, as for a5/a6 (§4.2), on the factor-set condition. r4:308–316 mentions
only blocking. Add the read switch, or note that encoding 2 avoids it.

## 3. Sensitivity set and stability, by hand

**The set.**
- `𝒮 = {2,3,4} × {0.4,0.5,0.6} × {0.1,0.2,0.3} × {0.05,0.1,0.2}` has `3⁴ = 81` points, with the
  primary point `(3, 0.5, 0.2, 0.1)`.
- `v_− ≤ 0.3 < 0.4 ≤ v_+`, so `v_− < v_+` at every point.
- The steps are symmetric about the primary point and contain no source value. `ν ≥ 0.05 > 0.047`.
- It is declared before evaluation and added to NC-γ1. No point is selected, and misses are counted
  at the primary point only.
- So the set is declared in advance and not fitted.

**What "stable" covers.** r4:719–726 claims stability for the **hand checks**, not for the statistics
in general. That is the correct scope.

| Check | Re-derived over `𝒮` | Result |
|---|---|---|
| 1 | `n = (0×12, 4,4,4,4)`, so `J` is cells 13–16 at every `ν`; `V_u = 1` with an interior minimum; the total is constant | **stable** |
| 3 | two cells, `V_u ∈ {0, 1}`, the monotonicity clause omitted | **stable** |
| 4 | `u = 1 + cos θ`, `V_u = 1`. At `ν = 0.2`, `J` is where `sinc² ≥ 0.2`, `|x| ≤ 2.02` rad on the slit scale, a width of about `1.29 λf/a`. One fringe period is `λf/d`. So `J` holds `1.29 d/a` periods, which is ≥ one period with an interior minimum for any `d ≥ a`, as for physical slits | **stable, given `d ≥ a`** and the stated four-cell sampling |
| 2 | equal channels give `u = ½`; for the shifted partner, monotonicity needs `J` inside **both** main lobes | **stable for small shifts**; see below |
| 5 | quarter period `V_u = √2/2 ≈ 0.707 ≥ 0.6`; the pair ratio over a period is `(2/3, 1/3, 0, 1)`, so `V_u = 1`; C0 and the in-phase pair give `V_u = 0` | **stable** |

**Check 2 in detail.** With max `n ≈ 2`, `J` includes cells where `e(j − δ) ≥ 2ν` while `e(j)` may have
passed its zero. There `u` dips and rises again, and is not monotone. In the sinc argument, with the
zero at π, this is excluded when the shift satisfies `δ < π − x_ν`, where `sinc²(x_ν) = 2ν`.

| `ν` | `x_ν` | Bound on the shift `δ` |
|---|---|---|
| 0.05 | ≈ 2.33 | ≈ 0.81 rad |
| 0.1 | ≈ 2.02 | ≈ 1.12 rad |
| 0.2 | ≈ 1.60 | ≈ 1.54 rad |

r4's "small against the lobe width" is right, but it is tightest at the lowest `ν`, so "stable at every
point" holds for `δ ≲ 0.8` rad, about a quarter of the main-lobe half-width.

**m2 (minor).** State the two conditions where the stability is claimed (r4:719–726):
- `d ≥ a` for check 4;
- the shift bound of about 0.8 rad at `ν = 0.05` for check 2.

## 4. `κ_det` instances and CC4/CC5

- **`κ_det` instances.** `I^rdy` and `I^part` are identical apart from `κ_det`. They are evaluated,
  reported and counted on their own and never combined; neither is selected after evaluation
  (r4:507–510, NC-γ3, NC-γ5). Every detection-defined quantity is computed per instance. Correct.
- **CC4/CC5.** A credit needing (s2) is "conditional on the separation of that member, not as
  credited", and it "does not count toward AC-1's coverage half until each such member is separated
  by (s1)" (r4:880–882). This is carried consistently into NC-γ6 and G1-F8, and no unconditional
  "creditable" remains. Correct.

## 5. Should the PROVISIONAL citations now point to U4 r3?

**Yes, as a scoped follow-up.** Citing a superseded version of an accepted unit is not the best record.
r4's choice to apply only the six answers is defensible. In either case the items stay conditional
("Results that depend on U4 … stay conditional", c.6892563291).

The section numbering is identical in r2 and r3, so the pointers move one-to-one. The content differs
in the cited sections:
- **§2.1.** r3 adds the "Beyond H-μ" extension: no marker-region declaration changes `D`'s law under
  any fixed `ν`, while a change of marker preparation changes it. This agrees with r4's E-prep row
  (430) and **strengthens** its support, so no change is needed.
- **§3.2.** r3 adds that masking is **pair-relative**: a declared point-path pair is masked iff
  `M_t(x_L − x_R) ∈ K_t`, which can hold where `K_t ≠ R_A`. This bears on r4:433 (see m3).
- **§6.3.** r3 restricts PK-2's exclusion of AV-t to "fixed geometry, tick and background", and makes
  the potential conflict conditional on how (γ) maps the compared runs. That agrees with r4's NC-rep
  and E-prep treatment. No change is needed, but the qualifier should be carried if the pointers move.

**m3 (minor; carried from r2 and r3, which I missed).** r4:433 says the marker is "unsourced at
(β)–(δ) only where `K_t = R_A`". CALC Theorem 1(b), owner-accepted, gives `K_t = R_A` as the
condition for masking **every** path variable. For the declared two-path pair the condition is
`M_t(x_L − x_R) ∈ K_t`, which `K_t = R_A` implies but which can also hold with `K_t ≠ R_A`
(U4 r3 §3.2, Instance 1.2's mirror-related pairs). Restate the row as "where the declared pair is
masked, `M_t(x_L − x_R) ∈ K_t` (always when `K_t = R_A`)". This rests on CALC directly, so it needs no
U4 pointer.

## Checked and not checked

**Checked by hand.**
- Every r3→r4 hunk against RESP and the owner record.
- The two encodings' events, masses, marginals and normalizers.
- `K_P`/`K_C` per encoding and per instance.
- The O11 stop.
- `𝒮`'s composition and constraints.
- The five hand checks over `𝒮`, with the two bounds above.
- U4 r2 against r3 in §§2.1, 3.2 and 6.3.
- CALC Theorem 1(a)–(c).

**Not checked.**
- Other U4 r3 sections.
- VER2.
- External sources.
