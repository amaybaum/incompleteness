REVISE — `RO1-DEPS-r2.md` at branch head `3b7d5aac10576903a3c5ac004b66a33135c06e53` (`research/ro1-sector-c-1169-20261114`, PR #1294); base `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`.

# Independent review of RO-1 step 2, `RO1-DEPS-r2.md`

## Scope and method

- **Role.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no Lean
  build, no edit, no post.
- **What was read.** `RO1-DEPS-r2.md` (SHA-256 `01809afb…d6545e`, the value the README gives) and
  `RESPONSE-DEPS-r1.md`, both at the head above. The new citations were checked at source on `main`,
  and at `9ff3b8d9` for the ledger.
- **Preservation.** `REVIEW-DEPS-r1.md` is preserved byte-identical to the review delivered. r1 is
  unchanged.
- **Line numbers.** Line numbers are r2's unless stated otherwise.

## Summary

- **Findings from the r1 review.** All blocking findings, B1–B4, are resolved. M1–M5 and N1–N5 are
  applied, with two small residues (R4, R7).
- **Requested checks.** S6 and S7 are restored (ll. 490–491). No minimality is claimed (ll. 463–466;
  no other occurrence).
- **Verdict.** UNDETERMINED is supported.
- **Why REVISE.** Two of the coordinator's added checks fail:
  - **Not first.** On tracks (c) and (d), the step named as first presupposes an interface and an
    availability criterion that are not yet specified. Those are the earlier open steps. Track (a)
    partly has the same problem.
  - **Cross-track conflicts.** Several track routes rely on assumptions that conflict with another
    track or with an adopted premise, and r2 does not flag them.
- **Consequence.** Criterion 2 is NOT MET. The fixes are confined to §7, §8.1 and one row of §5.

## Dispositions of the r1 findings

| Finding | Verdict | Check |
|---|---|---|
| **B1**: Lean scope; two interfaces | **Resolved** | D-iv is scoped to `Fin 2` with phases (l. 152). D-nonneg's verdicts are scoped to F₂, and its carrier-general parts to F under A1 (l. 153). Interfaces A and B are separated (ll. 248–263). D-phaseQ is added (l. 154). The settling evidence is split into the monomial part and the phase part (l. 396). C-2 lists the kernel results (l. 272). There is a transfer rule (ll. 370–373). Residue R1 below |
| **B2**: ordering of the first link; Bell separate | **Resolved** | Four tracks. "First" on track (a) is redefined as "the one refuted" (ll. 398–400). Bell is separate, citing Main:80, :582 and decision 3 (ll. 358–361). Track (b)'s first link is C-1 (l. 414). r1's ordering sentence is gone |
| **B3**: R5/R6 soundness; the two senses of F | **Resolved** | Op is a separate domain (ll. 72–73). R5/R6: coverage is on Op within P-CK; soundness is "not proved" (ll. 308–309, 314–319). §6 and §8.1 are corrected (ll. 345, 479–480). Residue R2 |
| **B4**: the P-vii argument cuts both ways | **Resolved** | ll. 413, 444 |
| **M1**: E1/E2, phase intervention, N2.3, (vi) | **Resolved** | ll. 122, 128, 132, 167, 444 |
| **M2**: GR A.8, P-super, SM uses of A5 | **Resolved** | ll. 123, 137, 160, 325, 415. Residue R3 |
| **M3**: S6, S7, S1 | **Resolved** | ll. 486, 490–491 |
| **M4**: tracing under §A.42 item 8; RO-3 status; the [IR] item | **Resolved** | ll. 46–49, 118, §9. Residue R4 |
| **M5**: finite V in D-cone and D-ceil | **Resolved** | ll. 147–148, 306, 409. Residue R5 |
| **N1–N5** | **Resolved** | ll. 123, 129, 190–193, 276–283, 115 |

New citations were verified at source:
- Main:
  - :80, :572, :582 and :588;
  - Main:724 items (vi), (xiii) and (xiv);
- Lean:
  - `StructuralClosure.lean`:327–335 and :344–348;
  - `FrozenSourcing.lean`:12, :285, :318 and :327;
  - `SubstratumInterfaceAudit.lean`:766–775;
- other papers:
  - GR:805, :823–827, including `S(ρ_R(t)) ≤ H(p_t)`;
  - Substratum:123, :171 and :193 (Theorem 23 lists E1–E7);
  - SM:224;
- ledger and records:
  - LEDGER-r8 l. 812 ("supplied by the analyst and is not an OI mechanism");
  - the script `papers/oi_lattice_code/foundations/equivalence_recovery_probes.py` (on `main`);
  - OA-2 STATUS:58–61.

## Required changes (these block acceptance)

**F1. On tracks (c) and (d) the named step is not the first open step. Track (a) has the same issue
in part (ll. 395, 414, 430, 445, 452–455; §8.1).**
- **Track (c).** Its first unsupported implication is a bound on remote-setting response under `Θ`
  and access closure (l. 430, OB-c1). Such a bound can be stated only after four things are fixed,
  and r2's own tables show that none of them is fixed:
  - the permitted setting operations: S3, "Availability of setting … operations" (l. 488);
  - the causal structure the wings sit in: whether the graph is global-linear or
    preparation-indexed (C-1, track (b));
  - the two-wing interface and its typing: `Θ` (S8, proposed, l. 427), where operations live (S7),
    and the reading (S6);
  - the criterion for "executes through `Obs`": RO1-SPEC-r3 S3's second question.

  r2 lists these as "Assumptions" or "Interface" (ll. 427–428) and records the dependence on C-1
  (l. 430). It still names the bound as first. The first open step on track (c) is the specification
  of the two-wing interface and of setting availability (S3, S6–S8), after C-1. The bound comes after
  them.
- **Track (d).** The named first implication is INSUFFICIENT's own condition (l. 445). It restates
  the target, not a step. The earliest open step is an availability criterion. For the one concrete
  model, X-PR, the interface is "specified, not derived" and "`T` writes no setting" (l. 442). Until
  "executable" is defined (S3; RO1-SPEC-r3 S3), no construction can be checked "clause by clause"
  (l. 446). Name that as the first step, with checking against the premises second.
- **Track (a).** The implication is placed "in one fixed model on the target's carrier" (l. 395),
  but neither the carrier nor the interface typing is fixed: OB-T (l. 477) and S7 (l. 491). The
  refutation on F₂ is valid. On the target's carrier, however, the first open step is the choice of
  carrier and of the admissible interface, and only then the sourcing of (iv). State the ordering
  explicitly, or say that (iv) is first *given* a carrier and a typing.
- **Track (b).** C-1 is first. It is a consistency question among premises and does not need the
  interface. One precondition should be named: an independently defined reference class, which the
  owner's direction requires (#914 c.6880010243 item 4). No change is needed beyond naming it.

**F2. Cross-track compatibility is not checked. Four places where one track's route undercuts
another track or an adopted premise:**
- **(a) against P-iv and P-xiv.** OB-a3 and track (a) take a superposed initial state (P-super) as
  the route to coherent preparation (ll. 395, 472). P-iv selects a probability measure on
  configurations as the source law (:54, :724 (iv)). P-xiv is stated on a distribution of Ω (:724).
  A superposed initial state is neither. Adopting P-super therefore needs P-iv replaced, and P-xiv
  restated, for the Bell track. r2 lists no such conflict (§3). Also, a "non-aligned cut" (ll. 160,
  472) is a change of bipartition, not a preparation. Making it physically available presupposes
  observables outside the configuration basis, so this alternative is not independent of OB-a1.
- **(a) against (b).** Track (a)'s only evidence on I uses the globally linear second-order rule
  (l. 391: OBL-RO3-2; D-phaseQ concerns "the reversible finite-range substratum update"). Track (b)'s
  route to Bell coverage scopes P-vii to a reference class and admits preparation-indexed nonlinear
  dependence elsewhere (ll. 413–415). On that route, the I-evidence of track (a) does not cover the
  states where the Bell branch lives. Either state this, or restrict track (a)'s I-evidence to the
  reference class.
- **(a) against P-L3, through S7.** Track (a)'s positive route asks for a sourced operation "that
  does not preserve the diagonal" (l. 396). If it is placed in `φ`, then `φ` is no longer a bijection
  of configurations, against P-L3 (:54). Main places the mixing operation as an operational
  "empirical controllability resource" (:588). So the route is compatible with P-L3 only if it is
  typed into `Γ`/`Obs`. S7 is listed (l. 491), but this consequence is not stated.
- **(a) against (c) and (d), through access closure.** Track (c) requires complete access closure:
  every executable program counts (l. 427). Track (a)'s route enlarges `Γ`. Under access closure, the
  enlarged `Γ` also contains every composite of the new operation with the existing reversible
  machinery. That machinery realizes "non-quantum finite instrument families" and PR "with globally
  coupled setting-dependent hidden dynamics" (D-glue, D-PR; :582, :360; X-MENU). An operation that
  supplies coverage can therefore make a track-(d) countermodel executable unless the same interface
  restricts it. This is the central question of the mandate, and l. 479 ("whether one principle could
  discharge several tracks is open") does not state the hazard.

**Fix for F1 and F2.**
- Restate the first open step of tracks (a), (c) and (d) as above.
- Add a short §7.7 on cross-track compatibility with the four points of F2.
- Make the matching edits in §7.6 and §8.1. Nothing else needs to change.

## Nonblocking residues and minor findings

- **R1 (ll. 152, 378–379, 394, 452).** "(iv) not supplied on F₂ under … B" is labelled
  [R, kernel]. The kernel states ¬`DenseUnitaryControl (permTheory (Fin 2))`, not
  ¬`HasCompositeUnitaryControl`. The step is immediate: exact control gives dense control with
  `V = U`, `c = 1` (`DiscreteCompletion.lean`:45–48). It is still an inference; mark it as one.
- **R2 (l. 380).** "The combinations proved sufficient for coverage (R5, R6)" should read
  "sufficient for exact endomorphic coverage on Op", as l. 315 does.
- **R3 (l. 334).** "It does not constrain … reuse" is too strong. Retention by reversibility
  (C2-structural, :80) together with same-seed reuse is the one mechanism on record that separates
  the two: it rejects the same-seed PR implementation (SEL-EXCL-1 §7, reviewed, not merged). A
  stipulated fresh-cell supply defeats it (§3 there). SEL-DISC-1 P5 records that "Scarcity alone is
  not a separator". So the discriminating question moves to renewal and resources. §5 should say so
  (see the central question below).
- **R4 (l. 513).** The BH-02 sentence quoted in P-super is classed "support off main". BH-02's
  report is on `main`
  (`verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`:8, 16, "SUPPLIED marks
  a quantum ensemble, circuit or superposition chosen by the analyst"). Reclassify it as support on
  main.
- **R5 (ll. 409, 534).** The transfer of D-cone to I is listed as open. Main:724 (xiii) supplies
  the key hypothesis directly: "each `F_i` reading the current values at finitely many sites and each
  site read by finitely many `F_i`". With finite range assumed, the cone needs no finiteness of `V`.
  The transfer is not given in r2. Naming (xiii) as the route would make OB-T concrete for track (b).
- **R6 (l. 512).** "D-cone's kernel cone" via "the kernel module": name the module.
- **R7 (l. 509).** RO-3's citation "Main:113–157" for the underlying statements is a range. Pin the
  lines used.

## ChatGPT's acceptance criteria

1. **Premise completeness: MET.**
   - E1/E2 (l. 128), the phase intervention (l. 132), N2.3 (l. 167), GR:805–823 (D-A8, l. 160),
     P-super (l. 137) and SM's uses of A5 (ll. 123, 271) are inventoried.
   - Their sources, domains and evidence states were checked.
   - The residues R4 and R7 do not affect completeness. The deferrals in §10 are justified: nothing
     found there bears on C.
2. **Track independence: NOT MET.**
   - Each track has a dependency chain, and track (b)'s first step is correct.
   - On tracks (c) and (d), the named first step presupposes interface definition and availability.
     Track (a) partly does too (F1).
   - Cross-track compatibility is unchecked (F2).
3. **Logical correctness: MET.**
   - Incompatible premises (C-1–C-3, C-4 kept as a difference), missing coverage (tracks (a) and
     (b)) and executable countermodels (track (d)) are kept apart by the rule at ll. 364–366.
   - Each kernel result stays on its carrier, and the transfer rule holds (ll. 370–373).
   - Imported structure is not counted as a derivation (ll. 367–369).
   - Residues R1 and R2 are labelling only. The one omitted incompatibility, P-super against P-iv, is
     taken up under F2.
4. **Verdict support: MET.**
   - UNDETERMINED follows from the four tracks. No track establishes SUFFICIENT or INSUFFICIENT.
   - What is stronger is reported at its scope: refutation of (iv) on F₂ under both interfaces, and
     exclusion of Bell on F under global P-vii (l. 457).
   - Correcting F1 changes which step is first, not the verdict.

## The central question

Can the same embedded-observer limitations both support quantum operations and exclude non-quantum
correlations? r2's answer is **mostly correct, but incomplete**.
- **What r2 shows correctly.** Every limitation on record either excludes quantum and non-quantum
  together, or excludes neither (§§2.1, 2.3, 5, 6):
  - limitations that exclude both: the interface ceilings (D-iv, D-nonneg), the preparation limit
    (D-A8) and the Bell ceiling (D-ceil);
  - limitations that exclude neither: access, capacity and retention as stated.
- **Gap 1: reuse.** r2 misses the one partial discriminator on record: retention with reuse (R3).
- **Gap 2: one interface.** r2 does not state that the question has to be answered on one interface.
  The operation that would supply coverage enlarges the executable set that soundness must then
  control (F2, fourth point).

Both belong in r2's answer.
