# MI+ screen: native meter coupling and an observer-level update constraint — result

Research only. No native round, no F or E, no merge, no adoption of any X, no status change, no full-equivalence
claim (consistency axis, §A.23). Preregistration: `PREREG.md`, committed alone at C_P = `80cafca5`, blob `9c84914d`,
sha256 `0b605612…ea03d`, unchanged. Amendment: `amendments/A1-A2-sources.md`. No commit adds a file under
`probes/`, `runs/`, `check/` or `runs-check/`, and no probe was run. Tags as in PREREG. Scope: owner decision of
2026-10-18 on PR #864.

## Outcome

**EARLY-STOP: insufficient alone / unsourced.** The outcome is reached from the source ledger alone: PREREG §2 as
amended by A1–A2, and the SRC column of §4. No MI+ candidate clause has an independently established OI source.
Every clause constructible from the ledger falls into one of three classes (PREREG §2, Finding):

- **(a)** it holds on every domain cone SEP ⊆ K ⊆ maxCone, or does not mention K (SRC = DERIVED, excluding nothing);
- **(b)** it has force only by asserting compatibility: a membership "native coherent output ∈ K", which MI already
  carries unsourced, or the unsourced validity premise S13;
- **(c)** it replaces the native readout, in conflict with M1 (S15).

By PREREG §5.3 a candidate qualifies only if SRC ∈ {TRUE, DERIVED} and no disguise flag is raised. Under the ledger
every candidate has SRC = FALSE, or SRC = DERIVED with a clause that holds on every domain cone, which §5.3 records
as a D1 flag. No candidate qualifies, and the rule's reachable labels are VOID and EARLY-STOP (§5.3, final
paragraph). The independent review of the preregistration at `80cafca5` confirms the central source finding after a
fresh corpus search: no candidate gains SRC = TRUE, and the rows it adds (S18–S24) change no SRC value.

| id | clause | SRC | class | first failing predicate (§5.3 order) |
|---|---|---|---|---|
| C0 | MI | FALSE | (b) membership | SRC |
| C1 | RO, readout compatibility | DERIVED | (a), S11/N2 [WA] | D1 |
| C2 | RO∘MI | DERIVED | (a), S11/N2 [WA] | D1 |
| C3 | REP, record consistency | DERIVED | (a), a matrix identity [WA] | D1 |
| C4 | EO ⊕ B | FALSE | (b), B is the S16 preservation premise [UP] | SRC |
| C5 | DIAG, native statistics | DERIVED | (a), N3 [WA] | D1 |
| C6 | NS, meter no-signalling | DERIVED | (a), a matrix identity [WA] | D1 |
| C7 | REC, the recorder | DERIVED | (a), `recordInstr_apply` InternalObserver.lean:252 [AT] | D1 |
| C8 | MI-24 | FALSE | (b) membership | SRC |
| C9 | MI-ent | FALSE | (b) membership; reduces to C0 by N4 [WA] | SRC |
| C10 | MI-3 | FALSE | (b) membership | SRC |
| C11 | OV-nat | FALSE | (b), the validity premise S13 [UP]; clarification (b) below | SRC |
| C12 | MI ⊕ OV-nat | FALSE | (b), as C0 and C11 | SRC |
| C13 | SYM | FALSE | (c), S15; check B `634e1639…` [EC-up] | SRC |

The DERIVED determinations are the written arguments of PREREG N2–N5 [WA]; their exact instances were not computed.
The exact countercontrols that §5.3 attaches to an EARLY-STOP record were not computed either; the record above
names the first failing predicate from the ledger only.

**The two source clarifications** (A1–A2):

- **(a)** The proposed sharp-update principle (K∞-Geom, S18) is unproved, and it cannot serve as a derived
  observer-level measurement principle.
- **(b)** Native complete-positivity and operational-validity results exist on the PSD matrix carrier (S14, S19,
  S20). Their extension to arbitrary candidate cones K with SEP ⊆ K ⊆ maxCone is not established.

## Scope

This is a finding about the candidate clauses C0–C13 constructible from the cited corpus at `80cafca5`, for the
native class of PREREG §3.2. It is not an impossibility theorem, and it does not say that OI cannot supply an
observer-level measurement or compatibility principle that excludes K(Z_F) and Γ(Q3). Node hypothesis H-DICH
(PREREG §7) is not closed by computation, and its preregistered §A.31 classification is not assigned. The outcome
agrees with the S2 finding of `../REPORT.md` that MI is insufficient alone, and adds the source clarifications (a)
and (b).

## Why the unperformed probes cannot change this verdict

- **SRC is not computed.** Every SRC value is a written determination of the ledger, made before computation
  (PREREG §0, §4). The only computed path that touches SRC is the refutation clause of §4, which can turn DERIVED
  into FALSE; a candidate with SRC = FALSE does not qualify, so the outcome stays EARLY-STOP.
- **Only VOID or EARLY-STOP is reachable.** Branches 3–5 of §5.3 are not reachable under the ledger (§5.3, final
  paragraph; the review, item 3(f)). Branches 4 and 5 require a pre-probe amendment adding a sourced candidate, and
  the review's search found none. A failed method control gives VOID, which reports no candidate value and leaves
  the ledger as it stands.
- **The diagnostics are record-only.** Δ1 and Δ2 enter no branch of §5.3 and cannot be cited as sourced (PREREG §7).
  The countercontrols attach to the EARLY-STOP record; they do not select it.

No computational verdict is rendered here, so no verdict stands over unrun controls.

## Gates

| gate | finding | source |
|---|---|---|
| G2, G3 (MI) | unchanged: G2 FAIL (borderline), G3 PASS | `../REPORT.md` S2 |
| G5 (MI) | unchanged: FAIL (standalone, read per owner decision D1); K(Z_F) satisfies MI | `../REPORT.md` S2, gate legend |
| G6 | OPEN; no prediction or postdiction attempted, since no candidate is sourced | PREREG §9 |
| M1 | not tested here; M1-CP1 to M1-CP4 were not run | PREREG §8 |
| conditional sufficiency | untested: whether a candidate would exclude K(Z_F), Γ(Q3) and K_B if it were independently sourced has no EXZ, EXG or EXB value | review A9, recorded below |

The remaining rows of the `../REPORT.md` S2 gate table are unchanged.

## Next effort

Derive the missing compatibility or measurement principle from native OI structure: an OI-internal, non-definitional
source fixing how a native entangling bijection acts on coherence-level joint descriptions, or a proved observer-level
update principle with a pair-level form. Testing a further assumed strengthening of MI does not address the source
gap this screen records.

## Research notes for any future preregistration

These are review amendments A3–A16 and review findings, recorded and not applied. They are [WA] determinations of
the review, not tested here.

**Findings.**

- The fixed tests are not native. Their availability is `avail_eq_fullEffects` (EffectSpace.lean:727) under
  `BoundaryTransitive`, which no countable family satisfies (`not_boundaryTransitive_of_countable` :858). The phrase
  "fixed tests and native operations" therefore refers to two different resource bases.
- C11's exclusion power comes from non-configuration, hence non-native, tests. With configuration tests only, C11
  reduces to C5 by N3, which holds on every domain cone.
- Rule defects in §5.3 and §5.2: UNDECIDED is unreachable, since rule 2's "no candidate qualifies" also holds when a
  predicate is undecided; D1 mislabels clauses that hold on every cone as restating PC; D3 has no must-not-flag
  control, so a D3 that flags every clause passes its known-answer test.

**Amendments A3–A16.**

- A3: state the native class as `InstAvail permClass` (ImplementationLocality.lean:268) with branches given by
  `realized_of_instAvail`, and exhibit every witness operation as a branch of a named InstAvail construction.
- A4: record that the fixed test family is not native, tag predicate values that use non-configuration effects
  `tests=full`, and state the configuration-test reading of C11 and C12.
- A5: make UNDECIDED reachable by requiring a decided failing predicate for EARLY-STOP; rule 4 reads "no qualifying
  candidate has".
- A6: add a predicate VAC (the clause holds on maxCone, hence on every domain cone), ordered after SRC, with D1 firing
  only for non-VAC clauses.
- A7: add the D3 must-not-flag controls PC and C11.
- A8: define STR as non-implication by PC, entailing non-implication by MI, with no implication claim made without a
  witness for each direction.
- A9: add a record-only conditional-sufficiency line reporting EXZ, EXG and EXB for candidates failing only at SRC/D6
  or D2.
- A10: strike Δ1; fold Δ2 into N6 as the EXZ determination for C11 and C12, exhaustive over native protocols with pair
  output by `realized_of_instAvail` and convexity of maxCone.
- A11: add M1-CP5 (the branch-level identity licensing "adds no protocol" for C2, C9, C10) and M1-CP6 (the rooted law),
  and label M1-CP4's unregistered-start check a replay of N3.
- A12: define CRIT, thread I, thread H, P831 and memo by path and commit; correct the `RevReal.traj` anchor to
  Equivalence.lean:176; retag the ready-meter attachment "[AT] on matrices; on tables [WA] given H-CAR".
- A13: key the amendment window to `probes/`, `runs/`, `check/` and `runs-check/`, forbid candidate evaluation in or
  outside the repository before the last amendment, and add an ancestry checkpoint from C_P.
- A14: record that drafting check X8 ran twice with an unkept first run, and that the (s,t) ↦ (b,d) map was found by
  search.
- A15: add K2 controls (CN Γ(B) CN ∉ maxCone; B ∉ SEP and a product ∈ SEP by PPT) and §11 rows for probe
  independence, `check/` independence, a record-only self-test mutation, printed versions and wall time.
- A16: extend the independent review to the SRC determination of C11 against S19, and to the exclusion of S18.

## Scope guards

Research only: no adoption of X, no native round, no F or E designation, no merge, no status, ROADMAP, programme,
manuscript or theorem change, and no full-equivalence or iff claim. The negative outcome is stated for the closed
candidate list and the native class of PREREG §3.2 only. `PREREG.md`, the frozen `op-fork/` files and the parent
`../probes/`, `../runs/` and `../src/` are unchanged.
