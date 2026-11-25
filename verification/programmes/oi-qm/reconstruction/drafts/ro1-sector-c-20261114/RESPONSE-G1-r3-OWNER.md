# Owner answers to G1 r3's questions, and where r4 applies them

**Record.** #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z), read through the API. G1 r3
(`GAMMA-G1-r3.md`, blob `20166317`, PR #1294 at `b3c79f60`) is accepted: "The definitions are
accepted. Results that depend on U4, and credit by scope alone, stay conditional." The revision is
`GAMMA-G1-r4.md` (cited r4 §N). r3 is unchanged. r4 applies the six answers and their necessary
consequences and nothing else. Paper-only: no computation, Lean, manuscript, Issue change or commit.

| Answer | Owner text | Applied in r4 | Necessary consequences carried |
|---|---|---|---|
| G1-A1 | "all four auxiliary protocols are added" | §1, the family `𝒜_10`; §2.4, the program specifications of a2P, a3P, a2C, a3C, with their record laws and masses in two encodings (all by E-set; blocking by E-set with the read by E-read) and the sum rule in each | `K_P` and `K_C` are defined on them per encoding and per `κ_det` instance. `π_P`, `π_C` have an operational test on `𝒜_10`. On K1 the four protocols, and `K_P` itself, are comparable within one instance only through the unresolved O11 stop (§2.4, §9). G1-F1's class note and its cross-propagation are updated (§10) |
| G1-A2 | "both detection-rule variants are kept, separately" | §5.2: two instances `I^rdy` and `I^part`, identical in every other component, evaluated, reported and counted separately, never combined | §1's reporting line; quantities defined through a detection are computed per instance (§2.4, §5.2); AW-det updated (§10); §9's list |
| G1-A3 | "the orbit-frequency report is accepted, with no weights chosen before G4" | §5.6 | none beyond the text |
| G1-A4 | "'no marker' means the coupling is absent" | §2.3, a1's requirement | §4.2's E-prep row: a marker law that masks completely is a4, not a1. §9's a1-against-a4 stop. The encodings of §2.2 are unchanged and none is selected (§12) |
| G1-A5 | "the comparison constants are fixed, and a sensitivity analysis over a declared set is added" | §5.7: the constants fixed; the sensitivity set `𝒮` for `(k, v_+, v_−, ν)` declared in advance (81 stated points, primary point `(3, 0.5, 0.2, 0.1)`), with its reporting rule. Each comparison gives a primary verdict, its verdict at every point and a stability label. No point is selected, and no miss is counted off the primary | The hand checks of §5.7 re-checked over `𝒮` by hand: all stable. `𝒮` is added to NC-γ1's declared items (§7.4) and to §9's list, and its size is reported beside the trial count |
| G1-A6 | "separation by scope alone is not sufficient, so the CC4/CC5 credit stays conditional" | §7.2: a credit that needs (s2) is reported as conditional on that member's separation, and it does not count toward AC-1's coverage half until each such member is separated by (s1) | NC-γ6's checkpoint row and its hand evaluation (§7.4), and G1-F8 (§10) |

**Kept as they were.** Every entry resting on U4 stays PROVISIONAL and keeps pointing to U4 r2. The
same record accepts U4 r3. Re-pointing the citations needs a check of each cited section against r3,
and that is not among these answers (r4, labels paragraph). §12 now lists the questions as answered,
with the citation.

## Dispositions for the focused review of r4

`REVIEW-GAMMA-G1-r4.md` (PR #1294 commit `c3353dc5`), verdict ACCEPT WITH CHANGES (minor only). The fixes
are made in place in `GAMMA-G1-r4.md`, and nothing else is changed.

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| 1 (m2) | State the conditions for the stability of the §5.7 hand checks | **applied** | §5.7, sensitivity analysis: check 4 is stable when the slit separation is at least the slit width, `d ≥ a`, since the `ν = 0.2` support holds `1.29 d/a` fringe periods. Check 2 is stable for a shift of at most about 0.8 rad, from `δ < π − x_ν` with `sinc²(x_ν) = 2ν` at `ν = 0.05`. Both were re-derived by hand, and the closing sentence carries the two conditions |
| 2 (m3) | The marker row must use the per-pair masking condition | **applied** | §4.2, marker row: "unsourced at (β)–(δ)" holds only where the declared point-path pair is masked, `M_t(x_L − x_R) ∈ K_t` (CALC Theorem 1(b)). That always holds when `K_t = R_A`, and it can hold with `K_t ≠ R_A` (U4 r3 §3.2) |
| 3 (m1) | Under the all-E-set encoding the read switch is also unavailable | **applied** | §2.4, O11 paragraph: the switch between a2P and a2C (and between a3P and a3C) is an E-set read switch. It is not available on R-lin at D5's scope, on the factor-set condition, as for a5 and a6. The second encoding avoids it |
| 4 | Re-point U4 citations to U4 r3, keeping them PROVISIONAL, and say where content changes | **applied** | Inputs, the labels paragraph and §11 now cite U4 r3 (blob `54ee9629`, accepted, c.6892563291), section for section. Every U4-dependent item stays PROVISIONAL. Changes from re-pointing are stated where they occur. **U4 r3 §2.1** ("Beyond H-μ") supports the E-prep row and changes none of it (§4.2). **U4 r3 §3.2**'s per-pair masking is carried in the marker row (item 2). **U4 r3 §§6.1, 6.3** restrict PK-2 to fixed geometry, tick and background, and that scope is now attached to every PK-2 citation: NC-copy and NC-noise (§7.1), and §8's two rows. This narrows the scope stated for those items. **U4 r3 §5.4** makes the Case Pk typing of the delayed-choice erasers conditional; G1 defines none of the three eraser cases, so §2.3's content is unchanged. The NC-rep item's reading of U4 §6.3 (AV-t, and Schwindt's polarization taken as unheld) is unchanged in r3 |
