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
