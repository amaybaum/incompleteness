# Manuscript propagation items found by the stage-6 inventory (recorded, not applied; manuscript hold)

Collected 2026-10-10 from the audited step-1 records (I1, I2) and the stage-5 integration note, each spot-checked
by the coordinator at L = `9f9f8257…`. Every item is a §A.25 consistency matter (book versus papers, or a
dangling anchor), not a correctness claim; none changes a band. Nothing is edited under the standing manuscript
hold; the list is for the owner's disposition.

| # | site(s) at L | what diverges | source record |
|---|---|---|---|
| 1 | `book/ch01-observation.md:55` vs `papers/Main.md:76` | the book defines (C2) as "Slow-bath timescale separation" (τ_S ≪ τ_B, Hubble timescale); Main states "(C2) Memory persistence … in two named forms (C2-structural, C2-slow)" | I1.21/I1.22 |
| 2 | `book/ch01-observation.md:71` vs `papers/Main.md:602` | the book: "The framework's four conditions are therefore *logically* independent"; Main: "only (C4) is logically independent. (C1) follows from it … and (C3) follows by data processing" | I1.25/I1.26 |
| 3 | `book/ch01-observation.md:26` vs `papers/Main.md:44` | "a deterministic dynamics" (book) versus "a dynamics" (Main) in the Definition of an observation | I1.6 |
| 4 | `papers/Methodology.md:251` vs `papers/Main.md:38, :62` | bijectivity stated as a lemma versus "a representation choice — the minimal recurrent bijective representative" | I1.10 |
| 5 | `papers/Main.md:562` | "The Kochen–Specker inheritance (§3.2)" — Main §3.2 is the Stinespring section and contains no Kochen–Specker statement (the only occurrence of "Kochen" in Main is this line); the inheritance statement is in the book (FULL.md:1042, ch03:168) | I2.14 |
| 6 | `papers/Main.md:500` and `OIBridge/Equivalence.lean:150–155` | the cited kernel anchor `S_imp_D` proves class (D) with an arbitrary initial law; the manuscript's finite-horizon process-dilation theorem needs a hidden prior independent of the visible initial state, which the kernel docstring says "is NOT what this theorem's class `(D)` asks for" | I2.40 |
| 7 | `papers/GR.md:328`; `papers/SM.md:791`; `verification/ROADMAP.md` | named hypotheses with no ROADMAP row: H-local-lift, H-observer-bundle, H-Y-vertex; H-blind named only inside the H-link paragraph (ROADMAP.md:1122) | I2.108, I2.112, I2.113 |
| 8 | book mirrors | the book never restates the canonical predictive quotient or the process-dilation theorem by name, and never names local tomography | I2.45, I2.40, I2.2/I2.3/I2.63 |
| 9 | `papers/GR.md:212` vs `OIBridge/PhysicalCharacterization.lean:295` | the five completion conditions are numbered (i) validity, (ii) trivial-ancilla consistency, (iii) inert spectators, (iv) full reversible control, (v) iterated composition in GR; the kernel conjunct order is validity, inert, control, closure, level-one (a numbering mismatch, not a content one) | I4 marker 2 |
| 10 | operational-completion route statements (GR.md:228, :256, :262; Main.md:350–352, :628) | stage-5 obligation M1: the condition (b) is not supplied by any principle at L; any statement of the route should name the spectator clause for the drive and one off-frame partner as the premise it is | `pt/INTEGRATION-NOTE-STAGE5.md` §5 |
| 11 | `papers/Main.md:552, :562` (scope note, not a divergence) | the gluing theorem's composition clause (Main.md:552) takes the local instruments' action `I_a ⊗ I_b` as input; the realization theorem's "non-quantum finite instrument families" (Main.md:562) are stated at the hidden-history level for the matrix carrier, not for cones in `W 3`. Any manuscript statement that a non-quantum composite is "realizable" by the same machinery should say which composite action it assumes; at L no realization or obstruction is attached to any pair cone | R6 §6 (assumption-watch marker), AUDIT-R §4 item 3 |

Also recorded (no manuscript site): the dictionary between `W 3` and complex matrices (`pauliW`, `Q3`, `dualW`)
exists only in design modules at L; a future manuscript statement of the K-programme results must not cite the
matrix-level PSD self-duality as if it were a `W 3` theorem (I3 fact 4, I4 marker 1).
