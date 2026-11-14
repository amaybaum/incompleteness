# RESPONSE to REVIEW-r1 of NLCAND-r1: dispositions, applied in NLCAND-r2

Writer's dispositions of the independent non-author review `REVIEW-r1.md` (REVISE; R1–R4 major, R5–R9
medium, R10–R11 minor; section C, missing analysis). `NLCAND-r1.md` and `NOTES-r1.md` are unchanged. Each
finding was checked at the source it cites, and each derivation taken from the review was re-derived by hand
before use. Paper-only; no computation on any OI rule; nothing in the repository was edited.

"r2:§" is a section or node of `NLCAND-r2.md`. Citation forms are those of r2. "Lean" is
`verification/lean-mathlib/OIBridge/` on `main` at `c3b5f37a`.

## Findings

| # | Disposition | Source check | Where in r2 | Notes |
|---|---|---|---|---|
| R1 | Applied, in modified form | Sub:131–133 (H-Bell's object is preparation-indexed long edges); Main:414 (which propagation sets the light cone "is not derived here"); r1's own B5 | r2:§0.5; B2 last sentences; new node B7; Verdict (b); §6 "Order" | The sentence about H-Bell (i), (ii) is removed; M3 and Verdict (b) say that nothing here tests H-Bell. Verdict (b) now reads "Member: not supplied at lattice scale. Rule: not established." The cone dichotomy is written out as B7 and each ingredient of its second case is checked there. Modification: B7 names the readout region `{a, a+1}` and states its four limits (lattice scale; the declared `r_O` under S; a sharp cone at one tick; nothing new toward increasing index). The review's reference "R15" does not exist in the review; it is read as section C item 2 |
| R2 | Applied, in modified form | Main:369–372 (single-time readout of the state on `R_A`); 3A:501 and LD:198–200 (complete histories are an imported convention); OA2:803–805 (two record variants); LD:274 (open item) | r2 header (conventions H and S); §1.4 readout row; B4 (0)–(iii) with the table; B5; B6; F4, F5, F11 | Re-derived: under S at `g = 1`, `T = 1` the pad `v_{a+2}(0)` leaves `A`'s state independent of `y` and the one-tick table Bell-local; under S the one-cell table is a product; at `g = 0` with `r_O` and label `0` the member reads `y` under both conventions. r2 says in B4 (0) that this is A1's gated read. Modifications: (1) the dependence at `g = 0` enters through cell `a+1`, at distance two, while cell `a+2` of the block is at distance one; r2 states the readout region for which Main's condition (iii) holds in the nearest-neighbour graph. (2) Under H the ready cell is not needed at `g = 0`. (3) Under S the one-cell table returns when the record cell's pre-setting slot is declared; r2 says so |
| R3 | Applied | LP:245 and SS:59–61 (what O-RDY asks for); r1's B3 and B4 (ii) | r2:§0.7; B3 (the `3k`-cell count); B4 (i); §6 J1 and J2; F6, F10 | J1 is the conditional corridor statement; the sentence that (c) and no-signalling exclude each other is withdrawn; r2 states that the channel is already open under μ-G and H with probability `1/q` per hop, and that "twice the nearest-neighbour speed" presupposes `K_nz` and `q ≥ 3`. The (a)–(b) link is added as J2 |
| R4 | Applied | Lean: `SubstratumInterfaceAudit.lean`:34–35, :770–771, :775, :780–782; `FrozenSourcing.lean`:84–86, :173–188, :295–298, :318–323; `DiscreteCompletion.lean`:45–48; `StructuralClosure.lean`:180, :348–356; `ExecSource.lean`:28–30, :129–134; 3A:498, :783–805, :837 | r2:§0.4, §0.7; P17; A3 (rewritten); Verdict (a); §6 "Order"; F1; §9 | All statements read as the review reports them. The kernel negatives are no longer scored as a failure of the candidate. A3 states what each Lean statement says (rule not an input, by `rfl`; `Fin 2`; the every-`ε` dense ceiling) and that the divide is between observer interfaces, not between rules and not between exact and approximate. "The control gap does not trace to linearity" is withdrawn |
| R5 | Applied | LP:19–21 (the owner's condition, as quoted there); OA2:803–805, :814; OA3:89–92 | r2:A4; §6 "Undecided nodes" and "No computation is proposed" | The "cheapest decisive check" is removed. r2 lists the undecided nodes, quotes the owner's condition, and records what design exists and what controls a B4 (iii) computation would need, without proposing one. The vacuous control (`R ≡ i+1` at `D > T`) is replaced by the linear ring inside its cone. The owner condition is quoted from the landing plan, not from the host record; r2:§10 says so |
| R6 | Applied; one proposed wording declined | S4:26–39 (carriers; R-nl; H-nl); S4:605–606 (NL-P); SM:294 | r2 header (H-ring); §0.3; M1; A5; Verdict (a); F9 | H-nl keeps TUNE-1's meaning; the hypothesis of this file is written H-ring. "The gap is NL-P" becomes "the ring-rule analogue of NL-P", and A5 states that T1's schema is three-dimensional. Declined: the proposed F9 wording (`REVIEW-r1.md`:308–309), which says that no `d = 3` rule whose graph varies with the state is written. Reason: for the rounded rule at `q = 2`, `h(s) = ⌊(s+1)/3⌋` (S4:31–35) changes under a unit change of one neighbour only where `s` crosses `1 ↔ 2` or `4 ↔ 5`, so its dependences are also present at some states and absent at others. r2 writes "no `d = 3` version of the ring rule" and makes no claim about the rounded rule's graph |
| R7 | Applied, with an extension | Main:724 (x); SM:124; SM:112 ("undirected degree in [2, 3] … [2, 4]"); M2:187 | r2:§0.3; M2; §2 preamble; P5–P7; B1; F3 | The outcome label is "`K_nz` only; breaks on the vacuum and uniform readings", and `K_nz` is marked as the writer's choice. B1 states that Main's dependency graph and SM's selected-neighbour graph differ. The invariant part: the review's family `1 + b(i+t)` was re-derived; r2 states the wider family `h(i + t)` and `h(i − t)` for any profile `h` with no zero value, checked by substitution |
| R8 | Applied; one row not assessed | SM:110 ("the gap equation is unchanged"); SM:222, :232, :284; SM:296; Sub:135; GR:78, :144, :154 | r2:§2 preamble and rows P19–P21; §7 | The sentence on the order of writing is replaced by a statement that the list is not a dated preregistration and not a complete inventory. P21 is assessed by hand: `E` is not conserved (values `y²` and `2y²` from a single non-zero cell on a blank ring). P20: the operator identities are unaffected and their attachment to the candidate is undetermined. P19 is not assessed: GR §3 was read only at the three lines cited. `papers/Structure.md` and the book were not read; a word search of `papers/GR.md` and `papers/Structure.md` for the linearity premise was run and its hits were not read through |
| R9 | Applied | SM:112 (the only visible sector it names is one site); OA3:89–92 | r2:§1.4, second table and the observer and one-cell rows | The sensitivity table is added, with B4 (0) as a further row. r2 states that the three-cell block was chosen where results exist and not where the question is open, and that the one-cell record is the manuscript's own visible sector |
| R10 | Applied | LP:248; OA1:156–160 | r2:§0.6; C1; C3; Verdict (c); F7 | "No unconditional supply … a heralded supply costs `q^{−M}`"; "no renewing process is identified" |
| R11 | Applied, all five | M2:157–164; `ExecSource.lean`:129–134 | r2:A2; P10; A3; §7; B2 | Three singly-controlled flips; the identity holds at component `i`; line range corrected and the two `rfl` statements cited; "not shown to meet"; the bound toward increasing index is the window itself |

## Section C (missing analysis)

| Item | Disposition | Where |
|---|---|---|
| C1 record convention | Done | r2:B4, B5, B7 |
| C2 coarse-scale bound | Adopted in part. The exact one-hop bound `|S_CHSH| ≤ 2 + 2/q` at `g = 1`, `T = 1` under H was re-derived and is in B4 (ii). The general chain count is not adopted: the joint uniformity of the gate cells along a chain was not re-derived, and the review itself marks it a sketch | r2:B4 (ii); B4 (iii) stays undecided |
| C3 invariant part of `K_nz` | Partly done: travelling solutions identified; the invariant part is not characterized and its weight under μ-G is not computed | r2:B1, P7 |
| C4 dynamics off `K_nz` | Not done. P7 and P8 now say what breaks for typical configurations; long-wavelength behaviour is not examined | r2:§2, §9 |
| C5 cycle structure and invariants | Not done, beyond P21's witness that `E` is not conserved | r2:C4, P18, P21 |
| C6 added rows; GR and Structure | Rows added; GR and Structure not read | r2:§2 |
| C7 `d = 3` and long-edge versions | Not done; both are different candidates | r2:§9 |
| C8 the instruction's record | Stated as a condition on any citation of the file | r2:§10 |

## Nothing declined in substance

Every finding is applied. Two points differ from the review's proposed text: the F9 wording (R6, reason
above) and the general chain bound of C2 (not re-derived, so not stated). Section D of the review asks for no
change beyond R1–R11.

## Effect on the verdicts

- (a): unchanged in content for A1 and A5; the kernel statement is no longer a verdict about the candidate.
- (b): from "not supplied" to "member: not supplied at lattice scale (B7); rule: not established", stated
  under each record convention.
- (c): from "not supplied under the uniform law" to "no unconditional supply under the uniform law; heralded
  supply at cost `q^{−M}`".
- Joint: from "fails; (b) and (c) exclude each other" to "the member is not shown to meet the three
  requirements and has a derived defect for (b) at lattice scale"; J1 is conditional; J2 is added.

## Length

r2 has 559 lines, above the 450-line aim of the first brief, because every in-cone result is now carried
under two record conventions and the preserved-results list has three more rows.

## Confirmation review (CONFIRM-r2.md)

`CONFIRM-r2.md`: ACCEPT WITH CHANGES, five minor wording edits N1–N5, no verdict change. Each was checked at
its source and applied in `NLCAND-r3.md` with the reviewer's text; only line breaks differ. `NLCAND-r2.md` is
unchanged. "r3:§" is a section or node of `NLCAND-r3.md`.

| # | Disposition | Source check | Where in r3 | Notes |
|---|---|---|---|---|
| N1 | Applied as given | r2's own B4 (ii) under S (total variation `0`, table Bell-local) and B4 (0) (readout region `{a, a+1}`) | r3:§6 "Order" | The sentence that the decided in-window instances signal was untrue under S; the bullet now names the two signalling instances and states that the `g = 1` instance under S is decided and does not signal |
| N2 | Applied as given, at all three places | OA1:156–160: "`P(E) ≤ q^{−M}`, with equality for a visible herald on visible cells" | r3:§0.6; C1; Verdict (c) | The herald cost is a bound, with equality when the herald reads the slots directly |
| N3 | Applied as given, both edits | `FrozenSourcing.lean`:295–299 (`sourcing_rule_independent` is proved by `Iff.rfl`); `DiscreteCompletion.lean`:45–48 (`DenseUnitaryControl` is defined on `Fin 2`) | r3:A3, "What the Lean statements say" and "The divide" | — |
| N4 | Applied as given | r2's B1 and B2 (two cells per tick toward decreasing index, one toward increasing) | r3:§9, second "Shows" bullet | — |
| N5 | Applied as given | P7, P8 of §2; section C item C4 of this response, which placed the item in §9 where r2 did not have it | r3:§9, "Does not show", second bullet | The response's C4 row is now accurate for r3 |

**Other differences between r2 and r3.** The title and status paragraph (r3; both reviews named; model
reviews, not verification), the review row of the reference table, the fixed-point sentence of §8, and a
closing "Not included" note. No node, derivation or verdict differs.

**Not included.** O1 (`CONFIRM-r2.md` §8), the reviewer's optional sketch for convention S with no declared
cell, is not re-derived and not used; r3 mentions it in one closing line and keeps "undecided" for the
member, which the sketch does not cover.
