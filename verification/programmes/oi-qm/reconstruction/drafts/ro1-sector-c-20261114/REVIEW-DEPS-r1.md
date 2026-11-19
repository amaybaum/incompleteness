REVISE — `RO1-DEPS-r1.md` at branch head `9504385a8368aa6d504f11bb552918c1fb804ced` (`research/ro1-sector-c-1169-20261114`, PR #1294); base `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`.

# Independent review of RO-1 step 2, `RO1-DEPS-r1.md`

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no post. **Mandate.** #914 c.6883931412 (`amaybaum`, 2026-11-14T20:43:54Z),
item 1, read through the API. **Context read.** `RO1-SPEC-r3.md` and `RO1-OVERLAP-r3.md` at the same
head. Off-`main` sources read at the commits r1 names: RO-3 at `78089e5e`, SEL-EXCL-1 at `0ecfddeb`,
LEDGER-r8 at `9ff3b8d9`. Line numbers below are r1's unless prefixed.

## Summary

The verdict label UNDETERMINED is upheld: nothing on record gives SUFFICIENT or INSUFFICIENT under
the reviewer's standards. The inventory is mostly accurate at source (31 items checked, below). But
the verdict's support does not hold as written:
- the Lean claim is applied beyond the carrier and interface the theorems state;
- the ordering that makes condition (iv) the *first* missing implication is contradicted by Main
  and by the ledger;
- R5/R6 are called proved sufficient for soundness, against r1's own caveats and against
  RO1-SPEC-r3 §7.4;
- one "not INSUFFICIENT" argument holds only under a reading of P-vii that also excludes the
  quantum Bell branch.

Each of these can be fixed in place, but together they change what §7 names as first and what
evidence would settle it. So the verdict here is REVISE, not ACCEPT WITH CHANGES.

## Major findings

**B1. The Lean claim is applied outside its stated scope, and two different "present interfaces" are
merged (ll. 67–69, 122, 230–231, 298, 332–334, 363–365).**
- Scope at source (statements only; `verification/lean-mathlib/OIBridge/FrozenSourcing.lean` on
  `main`):
  - `frozen_sourcing_verdict` is stated for `permTheory (Fin 2)`;
  - `nonnegBounded_verdict` is stated for `FiniteOperationalTheory (Fin 2)`;
  - the dense-control ceiling is stated "on the two-valued carrier, the carrier at which
    `DenseUnitaryControl` is stated" (l. 185);
  - the carrier-general parts (`obsTheory_nonnegBounded`, `phase_ceiling_rule_independent`) need
    `[Fintype 𝒮.ι] [Fintype 𝒮.V]`, "under the finiteness A1 supplies"
    (`SubstratumInterfaceAudit.lean`:766–770).
  - r1's D-nonneg row (l. 122) gives the domain as "The present interface", with no carrier or
    finiteness qualifier. §7 (l. 332) then uses it as the reason the target's coverage fails.
  - The target excludes a fixed finite total carrier (C-2, l. 246; #914 c.6875046763), and l. 246
    lists the uses of A1 that need replacement on I without listing D-nonneg or D-iv. "Coverage fails
    under the present interface" is kernel-checked for finite carriers (the verdict theorems for the
    two-state carrier). It reaches the admitted carrier only through an argument that r1 does not
    state. One partial support is in the corpus and is not cited: Main:588 (`phaseQ_ne_heisQ`), where
    a one-site phase automorphism of the quasilocal completion "preserves locality without arising
    from any reversible finite-range bijection".
- *Two interfaces.*
  - D-iv (`substratumGen_not_control`, `StructuralClosure.lean`:348) concerns `substratumClass`. That
    class *includes* the phase operators (`phaseOperator_supplied`, l. 331). This is Main's "stated
    interventions (its finite bijective read-write dynamics and the phase intervention)" (Main:80;
    :588 "the phase intervention is an assumption on the substratum class"). Its obstruction is
    preservation of the diagonal (monomiality), not nonnegativity.
  - D-nonneg concerns `permTheory`, which excludes the phases (`phaseOperator_outside_ceiling`).
  - r1 cites "D-nonneg; D-iv" as one "presently sourced interface" (ll. 332–334, 357). Its l. 298 says
    "On the present interface, nonnegative operations only", which is false for Main's stated
    interface.
- *Consequence for the settling evidence (ll. 363–365).* The proposed negative evidence is "a proof
  that every interface meeting the existing premises preserves nonnegative entries". If the existing
  premises include Main's stated phase intervention, `substratumClass` already refutes it. Yet that
  class still fails (iv). The negative evidence for (iv) has to be stated on the obstruction that
  `substratumGen_not_control` actually uses (monomiality and diagonal preservation). The phases need
  a separate negative statement. FrozenSourcing's own docstring: "`PhasesAvailable` is never
  identified with `DenseUnitaryControl`"; the two are "established separately".
- *Also note.* `sourcing_rule_independent` is `Iff.rfl`, because `obsTheory 𝒮` is defined as
  `permTheory 𝒮.Conf` ("the rule does not occur in it", `SubstratumInterfaceAudit.lean`:773–775).
  Its rule independence is a property of how the interface is defined, not a dynamical result.
- **Fix.**
  - State each kernel result with its carrier (two-state, or finite under A1) and its interface
    (`substratumClass` with phases, or `permTheory` without).
  - Give or name the transfer argument to the admitted carrier.
  - Split the negative evidence into its (iv) and phase parts.

**B2. The claimed ordering of the first missing implication is not supported, and the Bell chain has
its own first link (ll. 348–357, 367–369).**
- L. 354 claims that (iv) with the phases is first "because every later requirement presupposes it:
  coherent preparations, incompatible measurements, composites under (iii) and (v), and the quantum
  Bell value". At source:
  - Main:80 and Main:582: "Bell is a separate constraint rather than one of those conditions" and
    "Bell is not an extra rung of that lift". The owner's decision 3 (#914 c.6875046763) also puts Bell
    on a "separate research track".
  - LEDGER-r8 names separate first missing steps: §2.4 for QM, and §3.4 for Bell ("a specified
    preparation-indexed edge rule (or response map) for which the CHSH value is the quantum one"). r1
    cites §2.4 (l. 356) and not §3.4.
  - Main's realization theorems produce the quantum Bell law and incompatible-measurement statistics
    with no (iv): Main:80 (3) covers "every finite quantum record"; Main:572 (4) composes spatially
    separated instruments as `𝓘_a ⊗ 𝓘_b` on a joint branch register; Main:582 covers "incompatible
    measurements, adaptive interventions".
  - Under global P-vii with (x) and (xiv), the quantum Bell value is excluded for wings outside the
    cone whatever the intervention repertoire is (D-ceil; Main:414; C-1). That obstruction does not
    pass through (iv).
  - (i)–(v) are mutually independent (`five_way_minimality`, Main:562), and Main:80 and GR:224 leave
    open "which of the other conditions the substratum supplies". So "first" is not an order among the
    completion conditions. (iv) is the one *refuted* under the stated interventions, which is a
    different claim.
- **Fix.**
  - Name the first missing implication per chain: the operational-coverage chain (iv), with the phases
    as a separate co-requisite, per B1; and the Bell chain.
  - In the Bell chain, the first open link on the premises as adopted is the resolution of C-1
    (S11, MP-4), since global P-vii excludes the Bell branch before any bound on remote-setting
    response (MP-2) is reached. MP-2 is second there, not "once the first is supplied" (l. 367).
  - Drop or argue the ordering sentence of l. 354.

**B3. R5/R6 are said to be proved sufficient for soundness. Neither r1 nor its sources support this
(ll. 119, 125, 279–280, 285–291, 317–318, 389–391).**
- D-comp and D-OIplus are characterizations of an *endomorphic* theory on one carrier with ancilla
  levels (Main:562 rules (a)–(f); Main:586).
- r1 itself says that the relation of the two-wing Bell composite to D-comp's ancilla levels "is not
  stated (A)" (l. 303), and lists it as untraced (l. 421).
- RO1-SPEC-r3 §7.4, which was accepted, says the OI⁺ principles are "Not stated as a test against
  PR". It adds: "On one carrier without `Θ`, a PR table is an ordinary classical channel and is not
  excluded".
- Even so, l. 286 says "R5 and R6 are the only rows proved sufficient for coverage and soundness",
  §6 groups them as "Covering and sound, on F only", and l. 390 says the OI⁺ principles "supply both"
  MP-1 and MP-2.
- This moves an unproved inference to a proved statement, and goes against the claim/evidence rule.
- *"F" used in two senses.* RO-3's class F is one fixed finite *ontic* carrier. D-comp's "finite
  carrier" is the index set of complex matrices under imported kinematics (P-CK). Placing "sufficient
  … on F" (ll. 279–280, 286) next to C-2 ("exact coverage incompatible with a fixed finite carrier",
  D-dim) reads as a contradiction unless the two senses are separated.
- **Fix.**
  - Coverage: "sufficient for exact endomorphic coverage within P-CK".
  - Soundness: "conditional on a stated two-wing typing under `Θ` (S8) and on access closure; not
    proved".
  - Give D-comp and D-OIplus a domain label other than F.

**B4. One reason given for "not INSUFFICIENT" depends on how P-vii is read (ll. 339–346).**
- L. 342: the PR gate `B ⊕ r ⊕ (x ∧ y)` is nonlinear over `F₂`, so it "fails global P-vii". This
  matches the gate at source (SEL-EXCL-1 l. 33).
- But the adopted quantum Bell branch also lies "outside ledger item (vii)" (Main:414; C-1). So the
  argument cuts both ways:
  - *P-vii read globally:* no model of the premises realizes any Bell violation (R3). INSUFFICIENT
    then cannot hold, and the Bell part of coverage fails outright. Both are decided by C-1, not by
    the PR model's linearity.
  - *P-vii scoped to a reference class (the owner's Q2 direction, not done):* l. 342 no longer
    applies, and only the other two reasons remain (ll. 341, 344).
- The verdict survives under both readings; the reason given does not.
- **Fix.** Index "Why not INSUFFICIENT" by the P-vii reading, and say that C-1 decides the Bell side
  under the global reading.

## Medium findings

**M1. Premise inventory: omissions that a §A.19 search finds.**
- *E1 (unitary QM) and E2 (Bell violations).* These are listed as inputs on the same line as M1-B
  (`papers/Substratum.md`:123). LEDGER-r8 §9 (QM–SM row) records that "SM uses QM as input". Read as
  premises of the model, they would give coverage by import. They must be listed with their kind (ES)
  and excluded by non-circularity (RO1-SPEC-r3 §6.1). Otherwise a reader can take "SUFFICIENT" from
  what is already on record.
- *The phase intervention.* It is a stated intervention of the substratum class (Main:80, :588;
  `phaseOperator_supplied`), but r1 merges it into P-mix as "PX, not adopted" (l. 106). Give it its
  own row, with its kind (a stated intervention principle of the conditional extension, outside the
  posit ledger :724) and its sourcing status (not sourced: `phaseOperator_outside_ceiling`).
- *OA-2's designed control N2.3.* A reversible classical computer shows "an exact,
  preparation-contextual gbit at each bounded horizon" (`oa-2-20261112/STATUS.md`:58–61). This is a
  non-quantum prepare–measure behaviour of the same kind as X-PR (designed, not native). It is missing
  from V-OA2 (l. 134) and from "Why not INSUFFICIENT". It should be assessed there alongside D-PR.
- *Minor:* posit (vi), spatial isotropy (Main:724), is not listed.

**M2. Some downstream premises bear on the sector-C verdict and cannot be deferred wholesale
(ll. 62–65, 409–417).**
- *GR, Theorem A.8 scope (proved; GR:805, 813, 823).* "The orbit of a configuration consists of
  configurations, each a product state across that bipartition … H-scramble fails for every
  bijection". This is a corpus result that bijective dynamics on definite configurations never
  prepares a superposition across aligned bipartitions. It bears on the coherent-preparation half of
  coverage (§5 Preparation row, l. 297) and on MP-1.
- *Black-hole information.* The superposed-initial-state premise behind H-scramble (LEDGER-r8 §8.4:
  "A preparation (initial superposition) … that the model supplies") would supply coherent
  preparation if it were adopted. It must be inventoried for C with its status (open, not sourced),
  not deferred.
- *SM.* The uses of A5 (wave equation, Stage 2(b); SM:60, 224; LEDGER-r8 §9, Bell–SM row) are the
  other side of C-1. The owner's Q2 direction makes them the controls for scoping P-vii
  (#914 c.6880010243 item 4). They decide the Bell chain (B2, B4), so "SM … lattice posits beyond
  P-viii–xiii" cannot be deferred as not bearing on C.
- *No bearing found.* Cosmology, the Einstein-equation route (GR:162), and H-count, H-slope, H-frame,
  H-Hawking and G3: none bears on C on what I read.
- **Fix.** Bring these three items into §§1, 5 and 7. Keep the rest of §10 as deferred.

**M3. Stops: two are omitted and one is resolved without argument (ll. 393–407).**
- *S6 (class or sector reading) and S7 (typing) from RO1-SPEC-r3 §10 are missing, with no
  disposition.* Both are live:
  - INSUFFICIENT's "one model" and l. 346's rule against combining separately built countermodels
    depend on S6.
  - MP-1's "in the same fixed substratum and interface" (ll. 351, 360, 384) and the negative evidence
    "every interface meeting the existing premises" (l. 363) depend on where an added operation lives,
    which is S7. Main:588 places the mixing operation as "an empirical controllability resource", so
    it could sit in `φ`, `Γ` or `Obs`.
- *S1 / O11 (l. 401): "not needed for the verdict" has no argument.* It holds only if models whose
  menus differ are never identified. That is RO1-SPEC-r3 §2.3's *proposed* constraint, which is
  itself S1. V-B4 and X-MENU show that record-law identification and menus can come apart. Either
  argue that the verdict holds under each candidate relation, or keep S1 open as bearing on the
  verdict.
- *The other stops are genuine.* S2/Q7, S3, S5, S8, S9, S10, S11 and S12 are genuine and are not
  resolved silently. S10–S12 are new numbers defined in this file. S11 overlaps MP-4 and, under B2,
  belongs to the Bell chain's first link.

**M4. Tracing off-`main` references under §A.42 item 8 (ll. 26–32, 57–60, 92, 142, 356).**
- Only §1.4 carries a gap statement (l. 142). RO-3 and LEDGER references support claims in P-i, P-iv,
  D-memory, C-2, MP-3, and the verdict's "LEDGER §2.4 names the same step". None of these has a
  per-reference classification (provenance, support on `main`, or support off `main`).
  RO1-SPEC-r3 §9 carried an explicit paragraph on the gap.
- L. 31 says RO-3 at `78089e5e` was "accepted at its stated scope by #914 c.6883931412 item 2".
  Item 2 accepts the direct proofs of the OBL-RO3-2 unit and closes that unit. The RO-3 README at
  `78089e5e` reads "UNREVIEWED — NOT AUTHORITATIVE", and the `RO3-INVENTORY-r4.md` header reads
  "UNREVIEWED".
- L. 92 cites "no nonzero finitely supported configuration is periodic" as [R, off-main record].
  RO-3 §1.1 (I-qloc row) marks it [IR], which its status labels define as "not independently
  verified … No cell's status rests on it".

**M5. Finite-to-infinite transfer: D-cone and D-ceil (ll. 116–117, 277).**
- The cone lemma uses finiteness of the site set: "Finiteness of `V` is used in the first step"
  (Main:362). On an infinite site set, a function that is insensitive to each single outside
  component need not depend only on the components inside the set.
- R3's "Yes, for wings outside the cone" is therefore proved on F only. On the admitted carrier it
  needs a stated transfer (for example, finite-range locality of `φ` assumed directly).

## Minor findings

- **N1 (ll. 96, 101, 245).** C-1 is a contradiction with the *preparation-indexed* implementation.
  The "equivalent nonlocal response map" (Main:412) has no stated status, as l. 245 notes. LEDGER-r8
  §9 scopes it this way ("known not to, for global A5 with the preparation-indexed adjacency route;
  undetermined for the 'equivalent response map' alternative"). The P-vii and P-M1B matrix cells
  should carry the same scope.
- **N2 (ll. 161–163).** "Limits on executable interventions found so far come from the rule class".
  This holds for classical control (V-OA1). The quantum-resource ceiling of D-nonneg comes from how
  the interface is defined, and does not depend on the rule (B1). Scope the sentence.
- **N3 (l. 303).** Main:588 says the substratum "supplies the structural architecture". Main:80 and
  GR:224 leave open "which of the other conditions [(iii), (v)] the substratum supplies". r1 cites
  only :588. Either reconcile the two (architecture level against operational-theory level) or record
  the difference as a §A.25 candidate beside C-3.
- **N4 (ll. 67, 332).** The verdict line marks "not sufficient" as [A-inf], and §7 marks it
  [R, kernel, record on main]. Use one label, scoped per B1.
- **N5 (l. 89).** P-L1 "FA (stipulated)": Main:724 says Lemma 1 is delivered from the
  finite-capacity clause of the Definition. Classify it as DR from P-Def, with the stipulation lying
  in P-Def.

## Spot-check at source (31 items; the kind, domain and adoption cells agree unless a finding above
says otherwise)

| Items | Checked against | Result |
|---|---|---|
| P-Ax1, P-Def, P-L1, P-L2, P-L3 | Main:36, 38, 42, 44, 46, 48, 54, 724; GR:138 | quotes and domains agree (N5) |
| P-i, P-ii, P-iv, P-v, P-vii, P-viii–xiii, P-xiv | Main:724, :80; Substratum:100; LEDGER:938 | agree; RO-3 label (M4); (vi) omitted (M1) |
| P-C1–C4, P-EM | Main:34, 72–78, 742, 758; Structure:120 | agree |
| P-M1B, P-HBell | Substratum:123, 133 | agree; E1/E2 on the same line omitted (M1) |
| P-MD, P-CK, P-Born, P-mix, P-OI⁺ | Main:416–423, 562, 18, 584–588; GR:256 | quotes agree; P-mix merges the phase intervention (M1, B1) |
| D-SDQ, D-real, D-PR, D-cone, D-ceil, D-lin | Main:14–18, 80, 360, 362, 364–389, 414; SM:104 | agree; D-ceil transfer (M5) |
| D-comp, D-oi-alone, D-iv, D-nonneg, D-dim, D-approx, D-OIplus, D-sub, D-memory | Main:80, 558, 562, 586–588, 596–598; PROGRAMME.md:40, 82; Lean statements named in B1 | quotes agree; scope (B1, B3) |
| V-OA1, V-OA2, V-OA3 | `oa-1`/`oa-2`/`oa-3` STATUS on `main` | agree; N2.3 omitted (M1) |
| X-PR | SEL-EXCL-1 at `0ecfddeb` ll. 33, 46 | agree |
| C-3 | Structure:872, 886 against Main:18, 554, 562 | real; both sides cited |

## Contradictions C-1 to C-3

- **C-1.** Real for the preparation-indexed route, with both sides cited (Main:724 (vii); Main:414;
  SM:104). The label is too broad (N1).
- **C-2.** Real between a premise and the target, with both sides cited (Main:558, 562;
  #914 c.6875046763). Its list of A1 uses needing replacement omits D-nonneg, D-iv and D-cone/D-ceil
  (B1, M5).
- **C-3.** Real; both sides cited; correctly routed outside the unit.

## Countermodels

No countermodel is presented as one model without a compatibility argument. L. 346 states the rule,
and l. 264 marks the joint posit model as not constructed. The exception is B3: R5/R6 are summarized
as covering and sound without the two-wing argument that soundness needs.

## Verdict

UNDETERMINED is the right label on the record. No reading I found gives SUFFICIENT, unless E1 is
read as a premise, which non-circularity bars (M1). No reading gives INSUFFICIENT, because no premise
model with a sourced supraquantum experiment is on record: D-PR, X-PR and OA-2 N2.3 are designed,
not native. What must change is the support for the verdict, which needs B1–B4 and M1–M3 before a
ChatGPT exact-head review.
