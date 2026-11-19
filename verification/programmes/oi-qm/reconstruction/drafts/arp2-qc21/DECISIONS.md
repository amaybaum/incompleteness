# ARP-2 (Q-C2-1): owner decision sheet for the freeze (preregistration r9a)

WIP / UNVERIFIED. Model-written. This sheet states the questions only and makes no recommendation.

**Markers.**
- **[R]**: the option needs a further control-plane revision and re-review before `F`.
- **[§A.29]**: the option conflicts with §A.29, because the choice fixes the outcome.
- "Drafted": the text that r9a currently carries.

**Sources.**
- "Owner record": what the owner's earlier comments on #1169 (c.6733621500 … c.6734374076) already imply, quoted or
  paraphrased neutrally.
- Levels and the A/B arms are as defined in the preregistration's *Levels* section and its *A/B typing*.

| # | question | options | consequence for the Levels and the A/B arms | owner record |
| --- | --- | --- | --- | --- |
| D1 | Keep r5's direct-access calculations? | (a) keep, as labelled diagnostics. (b) drop | none for either: no token reads them | c.6733711272: they "may remain as separate mathematical diagnostics, but must not determine the quantum-behavior verdict" |
| D2 | How to treat P's known outcome? | (a) run P as a consistency check of a paper derivation (drafted). (b) add a blind P arm **[R]**. (c) defer P | (a): Level 1's condition under L(i) is known before `F`. (b): adds a blind arm to `A_P` and B. (c): no Level 1, so no Level | c.6733796760 element 6 asks for "expected outcomes" to be specified before execution |
| D3 | P's geometry? | (a) encoded path (drafted). (b) also the spatial `F_2` ring **[R]** | (b): a second P instance, wave-like (`α = 2`). The Levels rule would need to say which instance counts | c.6733621500: "as close to the double slit experiment as possible" |
| D4 | Phase settings? | (a) `{0, π}` (drafted). (b) also NNB quarter phases on U′ **[R]** | (b): NNB, a dynamics row, enters both `Adm_A` and `Adm_B`; ABL-NNB is added; P stays at Level 1 at most | c.6733796760 element 2: "Vary the relative phase between the paths and predict how the screen distribution changes" |
| D5 | C's detectors under the test rules? | (a) native-rule detectors in every arm, L-HET (drafted). (b) one homogeneous rule. (c) drop `S_Y` | (b): AND and NAND detectors do not couple, so C decides only OR and NOR. (c): the witness is confined to the `x`–`z` plane. The reach of Level 3 narrows accordingly | c.6734304025: "using the same underlying dynamics wherever possible" |
| D6 | Composition horizons? | (a) `K ∈ {6, 12}` (drafted). (b) other | C-SIZE-DEPENDENT is defined by the pair of horizons | c.6733796760 element 5: "implement it repeatedly, and test its composition" |
| D7 | B's fragments? | (a) B-P, plus B-C for flagged C instances (drafted). (b) B-P only | Level 2 counts B-P only, unless D17(b) | c.6733796760: discrimination as an acceptance test on the double-slit setup |
| D8 | The eraser? | (a) required (drafted). (b) a recorded owner waiver | none for the token; (b) removes the eraser fields | c.6733796760 element 3: "created, kept, or erased"; c.6733711272 item 3 on conditioned subsets |
| D9 | Where does `DESIGN-DS.md` land? | (a) a separate paper record before `D`. (b) the record directory | none | — |
| D10 | The LP method and the gated workflow? | (a) copy ARP-3-QC22 r13's (drafted). (b) a separate method **[R]** | none, provided the copy is reviewed (precondition 5) | c.6726548830: the Environment gate and the execution safeguards |
| D11 | Composition alongside a second system? | (a) a later round, NR-11 (drafted). (b) this round **[R]** | (b): C's Level-3 condition gains a spectator test | c.6733711272 item 4: "behavior under composition" |
| D12 | The Environment (a requirement, not a choice) | E-ID, E-READ, E-BIND, as ARP-3-QC22 precondition 2b | none | c.6726548830: "Require explicit owner approval before every decisive execution" |
| D13 | Intermediate marker strength? | (a) report the finding (`V, D ∈ {0, 1}`; mixtures lie on `V + D = 1`) (drafted). (b) a mixed-setting arm **[R]** | none for the token; (b) adds an arm to B's class | c.6733796760 element 3: "Measure interference visibility and distinguishability quantitatively" |
| D14 | The shams' role | (d) reported, gating nothing (drafted). (a) gate on SH-K **[§A.29]**. (b) gate on SH-0. (c) both, gating on SH-K **[§A.29]** | (d): the token is independent of the choice. (a) and (c): the gate fires whenever the marker suppresses, so P-COMPLEMENTARITY is unreachable for QM, waves and B alike, and with L(i) no Level is ever awarded. (b): the gate never fires, so (b) is equivalent to (d). The A/B readings are the same under every option | c.6733855134: the sham outcome is "a control target, not a guaranteed result"; c.6733935953: screen statistics cannot separate recording from dephasing |
| L | What Level 1 reads | (i) P-COMPLEMENTARITY. (ii) `V(off) > 0` in construction B, two settings | (i): known before `F` (D2(a)). (ii): known on paper, and Levels 2–3 do not depend on P's class-level predicate. Either way, Level 2 needs Level 1 | c.6733796760: Level 1 is "OI produces phase-dependent interference"; c.6733855134: "keep the primary result at Level 1" |
| D15 | B-P's access class `Acc`, and its typing | (a) every SA-1(b) joint registration on the held cells (nine settings) (drafted). (b) a restricted set **[R]**: (b1) screen × arm-cell slots; (b2) screen only; (b3) screen × phase-cell slots | Level 2 requires the owner to type `Acc` as established native or candidate strengthened. Under (b), the completion must also not restore a model. (a): `Acc` is not tomographically complete, so a B-CONTEXTUAL is relative to SA-1(b). B's construction A (complete access) is measured under every option | c.6734304025 lists access restrictions among candidate strengthened principles; c.6733796760 element 4: "explicitly state which classical models it excludes" |
| D16 | Do C's end-of-run carrier meters count as indirect access? | (a) yes (drafted). (b) no: only the screen after recombination, and marker reads correlated with it | (b): C becomes rebit-like (`S_Y` excluded unless NNB) and Level 3 narrows. Marker reads and the eraser are admitted under both | c.6733711272 item 3 and c.6733796760 element 3 admit marker-detector records; c.6733621500: "indirectly through interference" |
| D17 | Does B-C count toward Level 2? | (a) no (drafted). (b) yes | (a): Level 3 joins B-P with C-EXPOSURE, two unrelated instances, and that qualifier is printed. (b): Level 3 needs the same C instance's B-C to be contextual | c.6733796760: two acceptance tests on the double-slit setup |
| D18 | How are L-PATH, L-PORT, L-CAL and L-UPRIME typed? | (a) imported representation, outside the three-way typing (drafted). (b) candidate strengthened principles. (c) imported, admitted only in a benchmark arm | (c): every P and C token becomes a benchmark result, no Level is awardable, and A and B cannot pose P or C. (a) and (b): the Levels are unchanged | c.6734304025: imported quantum assumptions are "Not permitted as unexplained ingredients in the primary derivation". Whether these identifications are quantum structure is the open point |
| A/B | Owner-typing of *The A/B typing* table | (a) adopt the reviewer's typing as frozen. (b) amend individual rows | It fixes which rows are construction A and which are B, each row's kind and `dynamics_credit`, and therefore the A/B readings and the ablation report. Retyping a row as A changes `A_P` | c.6734304025: "Established native principles", "Candidate strengthened principles", "Imported quantum assumptions". c.6734374076: an ablation must test both predictions and mechanisms, and "A stronger principle that merely describes observation differently must not be credited with generating new physical dynamics" |

**A/B arms as drafted.** `A_P` = construction B minus SA-1(c). No substratum-only P can be posed. Paper expectations:
- existence: both succeed;
- universality: A fails and B succeeds (SA-1(c));
- observer-level complementarity is carried by SA-1(b) (ABL-SA1b).
