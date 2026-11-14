# Response to the independent review of RO1-DEPS-r1

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-DEPS-r1.md` (REVISE at `9504385a`). They
also cover the reviewer's additions relayed by the coordinator. The changes are in `RO1-DEPS-r2.md`.
`RO1-DEPS-r1.md` is left unchanged (SHA-256
`2d3ce3676d50c829d4684e6d0218d8ad6d307f07aa4b3b99d624bb45de593390`).

Each finding was checked at source before it was applied. Lean files were read and not built. No
finding was found to be wrong. Line numbers in the first column are r1's.

## Blocking

| Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|
| **B1.** The Lean claim is applied outside its scope, and two interfaces are merged | **Confirmed.** `frozen_sourcing_verdict` is stated for `permTheory (Fin 2)` (`FrozenSourcing.lean`:318–321), and `nonnegBounded_verdict` for `FiniteOperationalTheory (Fin 2)` (:327). `obsTheory` is `permTheory 𝒮.Conf` "under the finiteness A1 supplies", and "the rule does not occur in it" (`SubstratumInterfaceAudit.lean`:766–775). `substratumClass` contains `phaseOperator_supplied` (`StructuralClosure.lean`:331). `substratumGen_not_control` is stated on `Fin 2` and uses "every monomial conjugation preserves the diagonal" (:344–348). `phaseOperator_outside_ceiling` is at `FrozenSourcing.lean`:285. "`PhasesAvailable` is never identified with `DenseUnitaryControl`" is at l. 12. Main:588 `phaseQ_ne_heisQ` was confirmed | **Applied.** D-iv and D-nonneg carry their carriers (F₂; F under A1) and interfaces. §2.5 separates Interface A (`substratumClass`, monomial, with the phases) from Interface B (`permTheory`, without the phases). D-phaseQ is added as the one partial transfer to I. The settling evidence is split: (iv) on monomiality, the phases separately. The uses of A1 in C-2 now list D-nonneg and D-iv. `sourcing_rule_independent` is noted as holding by definition | §§1.2, 2.1, 2.5, 3 (C-2), 7.2 |
| **B2.** The ordering of the first missing implication is not supported; Bell has its own first link | **Confirmed.** Main:80, "Bell is a separate constraint rather than one of those conditions"; Main:582, "Bell is not an extra rung of that lift"; owner decision 3. LEDGER §3.4 has its own first step. Main:572 and :582 realize incompatible measurements and separated instruments without (iv). GR:224 and Main:80 leave (iii) and (v) open | **Applied, and extended by the reviewer's addition 1.** The verdict is now reported on four tracks (§7.2–7.5), each with its first unsupported implication. On track (a), "first" is defined as first refuted, not first in an order (§7.2, last paragraph). Track (b)'s first link is the resolution of C-1. r1's ordering sentence is removed | §7 |
| **B3.** R5 and R6 are called proved sound without a two-wing argument; "F" is used in two senses | **Confirmed.** D-comp and D-OIplus are endomorphic theories on one carrier with ancilla levels (Main:562 rules (a)–(f); :586). RO1-SPEC-r3 §7.4: "On one carrier without `Θ`, a PR table is an ordinary classical channel and is not excluded" | **Applied.** R5 and R6 now read: "Sufficient for exact endomorphic coverage within P-CK, on Op"; "Soundness against PR: conditional on a stated two-wing typing under `Θ` (S8) and on access closure; not proved". A new domain label, Op, separates the operational index set from the ontic carrier F. §6's grouping and §8.1's closing note are corrected. Track (c) states that a single-carrier characterization is not enough | Header (domains); §§1.2, 4, 6, 7.4, 8.1 |
| **B4.** The P-vii argument also excludes the quantum Bell branch | **Confirmed.** The PR gate `B⊕r⊕(x∧y)` is at SEL-EXCL-1 l. 33. The adopted branch lies outside (vii) (Main:414, :362; SM:104) | **Applied.** "Why not INSUFFICIENT" is now part of track (d) and of §7.3. Under the global reading, Bell is a coverage problem decided by C-1, and the nonlinearity argument is shown to cut both ways. Under the scoped reading, only the absence of a compatible, executable model remains. For `R*` (RO1-SPEC-r3 §7.3): under global P-vii no Bell-violating K-X exists at all, so `R*`'s test (b) cannot be passed until C-1 is resolved. Track (c) records this dependence | §§7.3, 7.4, 7.5 |

## Medium

| Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|
| **M1.** Omissions: E1/E2, the phase intervention, OA-2 N2.3, isotropy | Confirmed: Substratum:123 lists E1, E2 and M1; Main:80 and :588 give the phase intervention; OA-2 STATUS:58–61 gives N2.3; Main:724 item (vi) is isotropy | **Applied.** Rows added: P-E1E2 (ES; not admissible as premises of C, by non-circularity), P-phase (stated intervention principle, outside the posit ledger, not sourced on Interface B), P-vi, and N2.3 in V-OA2. N2.3 is assessed under track (d). P-mix is narrowed to the mixing operation | §§1.1, 1.3, 7.5 |
| **M2.** Downstream items that bear on the verdict | Confirmed. GR:805, :813 and :823 (A.8 scope; "H-scramble fails for every bijection"). LEDGER §§8.1, 8.4 (superposed initial state; "supplied by the analyst and is not an OI mechanism"). SM:224, SM:60 and LEDGER §9 Bell–SM (A5 uses as controls) | **Applied.** D-A8 and P-super are added and enter the Preparation row of §5 and track (a). SM's A5 uses enter P-vii, C-1 and track (b) as the controls of the scoping test. The rest stays deferred in §10, as the reviewer found no bearing | §§1.1, 1.2, 3, 5, 7.2, 7.3, 10 |
| **M3.** S6 and S7 omitted; S1 dropped without argument | Confirmed (RO1-SPEC-r3 §10) | **Applied.** S6 and S7 are restored with their bearing. S1 is argued: the *label* holds under each candidate relation, because a coarser `≈` creates no sourced experiment and no sufficiency proof. The settling evidence speaks of "one fixed model", so S1 stays open as bearing on what would settle the verdict | §8.2 |
| **M4.** Off-`main` references not traced; RO-3 status misstated; an [IR] reading cited as a result | Confirmed. The RO-3 README reads "UNREVIEWED — NOT AUTHORITATIVE", and `RO3-INVENTORY-r4.md` is headed "UNREVIEWED". Owner item 2 accepts only OBL-RO3-2's direct proofs. RO-3 defines [IR] as "not independently verified … No cell's status rests on it" | **Applied.** A §A.42 item 8 table (§9) classifies each off-main reference as provenance, support on main or support off main. The RO-3 status is restated in the header. The [IR] sentence ("no nonzero finitely supported configuration is periodic") is removed from P-i | Header; §§1.1, 9 |
| **M5.** D-cone and D-ceil use finiteness | Confirmed: "Finiteness of `V` is used in the first step" (Main:362) | **Applied.** D-cone and D-ceil are scoped to F. R3's exclusion is "on F". C-2 lists them, and the transfer rule of §7 (reviewer addition 5) applies | §§1.2, 3, 4, 7 |

## Minor

| Finding | Disposition | Where in r2 |
|---|---|---|
| **N1.** C-1's scope | **Applied.** C-1, P-vii and P-M1B are scoped to the preparation-indexed implementation. The response-map alternative is left without status, quoting LEDGER §9 | §§1.1, 3 |
| **N2.** "Limits come from the rule class" | **Applied.** It is scoped to classical control (V-OA1). The quantum-resource ceiling is attributed to how the interface is defined | §2.1 |
| **N3.** Main:588 against Main:80 and GR:224 on (iii) and (v) | **Applied.** Recorded as C-4, a difference between architecture level and operational level, not reconciled here. It is a §A.25 candidate if unreconciled at source (S12) | §3 |
| **N4.** Inconsistent labels for "not sufficient" | **Applied.** One label is used throughout: [R, kernel] scoped to F₂ | §§7.1, 7.2 |
| **N5.** P-L1's kind | **Applied.** DR from P-Def, with the stipulation in P-Def | §1.1 |

## The reviewer's additions, relayed by the coordinator

| Addition | Disposition | Where in r2 |
|---|---|---|
| 1. Four tracks, each with carrier, dynamics, interface, assumptions, evidence status and first unsupported implication | **Applied.** §§7.2–7.5 give one table per track; §7.6 summarizes them | §7 |
| 2. An incompatible combination is not an executable countermodel | **Applied.** Stated as a rule in §7. Global P-vii blocking Bell is reported as a coverage problem (track (b)), and track (d) keeps INSUFFICIENT's condition separate | §§7, 7.3, 7.5 |
| 3. No claim of minimality | **Applied.** §8.1 is retitled "Earliest unresolved obligations" and states that no minimality is claimed. The items are renamed OB-… | §8.1 |
| 4. Imported structure is not a derivation | **Applied.** Stated as a rule in §7, listing P-E1E2, P-phase, P-super, P-CK and P-mix | §7 |
| 5. No transfer without an argument | **Applied.** Stated as a rule in §7 for the Lean operation ceilings and the Bell cone and ceiling. Each result's domain column states its carrier | §§1.2, 3, 7 |

## Verdict after revision

**UNDETERMINED**, re-derived on four tracks:
- (a) coverage fails on F₂ under both interfaces, with no statement on the target's carrier;
- (b) a coverage problem under global P-vii, C-1;
- (c) soundness is not shown;
- (d) no compatible countermodel is on record.

The first unsupported implication of each track is in §7.6.
