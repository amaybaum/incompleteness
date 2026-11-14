# Owner brief: what "full OI ↔ QM equivalence" could mean, and what is left to choose (r4)

Plain-language summary of `TARGET-THEOREM-r4.md`, which keeps r3's statuses (r3 confirmed at `755f9bff`, ACCEPT WITH CHANGES; r4 unreviewed); every line rests on that document, where the sources are cited. No candidate is recommended. "OI ⇒ QM" means the OI side implies the quantum side; "QM ⇒ OI" the reverse. Research findings off `main` are model-reviewed and not independently verified.

## (a) The candidate theorems

- **T0, Main's characterization.** A process has memory exactly when it has a hidden-state realization with readback. Both directions are proved on paper, not in Lean. Neither side is quantum; the quantum representation follows in one direction only.
- **T1, statistics of a single experiment.** The possible outcome laws of finite reversible hidden-state systems and of fixed-basis quantum systems are the same. Both directions are checked in Lean. With one fixed system for all times, QM ⇒ OI fails for the two-state case (Lean).
- **T2, approximation to any accuracy.** QM ⇒ OI: one finite reversible machine reproduces every bounded quantum experiment within ε; paper proof, not in Lean, with the finite-precision bound open. OI ⇒ QM: true for that purpose-built machine only; the class of all such machines contains non-quantum behaviour.
- **T3, exact, with added principles.** Given complex matrices as the setting, exact finite quantum mechanics is equivalent to named added principles. Both directions are checked in Lean for three formulations. The "substratum plus control" formulation is two separate one-way statements, not one equivalence.
- **T4, infinite or limit object.** The infinite-lattice completion is unique (Lean); no converse is proved. An exact limit object equal to full QM is not stated anywhere.
- **T5, native: no added principle.** OI ⇒ QM is refuted for the observer interface as now stated (Lean); what is missing is one continuously tunable mixing operation. A model-level theorem with a derived extension is open in both directions.
- **Clause B, Bell correlations**, which can be added to any candidate. Refuted for the reference nearest-neighbour rule under screened conditions (paper); for the adopted branch it is a posit (H-Bell); nothing selects the quantum bound.

## (b) Already decided in the records

- R1. Main defines the phrase at theorem level as T1 with the readback clause, and says full operational equality needs more (`papers/Main.md`:774).
- R2. Endpoint F1 (full conditional equivalence) is retired for the present architecture; F2 (a named extension proved sufficient, necessity assessed separately) is active (`PROGRAMME.md`:40, :515–523, :634; #914).
- R3. For F2: target "A1 exact" on qubit-power registers, all finite dimensions later; strict extension criterion G1–G8; narrowed necessity scope (#875, owner decisions of 2026-10-17; the memo defining the terms was not read).
- R4. The approximate question is its own programme with Level B, one reusable mechanism, as main target (#1216; no owner comment traced for that sentence).
- R5. #1169's target is the accepted Gate A contract: one model for all finite experiments, both directions, deterministic dynamics allowed; assuming the quantum setting from the outset counts as a conditional reconstruction only (#1169).
- R6. Tunable mixing should arise from OI's own principles, without a postulated quantum rule; finite access is not to be equated with finite underlying dynamics; Born, Kochen–Specker and Bell are separate obligations; TUNE-1 is paused (#1236, owner decision of 2026-11-11).
- R7. Bell branch: measurement independence kept, parameter independence given up (`papers/Main.md`:404–416).
- R8. Bell ladder: linearity is a conditional ledger posit; independence of generator residues is a separate hypothesis (#1273, as quoted in the Bell status note; not read at source).
- R9. The infinite-lattice result is stated as uniqueness, not equivalence (`AGENTS.md` §A.34; #899).

## (c), (d) Questions still open, with options, what each commits to, and the record that bears on it

1. **Which target, and which kind of endpoint?** Main's meaning (T1 with T0): both directions are already proved, and the operational layer stays outside "full". F2's sufficiency form: commits to naming and sourcing an extension, with necessity separate. #1169's two-directional model-level target (T5b): commits to both open directions and a nonempty class of native models. Classification (F3): commits to mapping the whole OI-compatible theory space. *On record: R1, R2, R5.*
2. **What is the OI side?** Law level only: T1 and T2 apply and no lattice posit is used. The stated observer interface: T5a is refuted, so an extension or changed interface is needed. The lattice model: commits to the native preparation and control obligations. Keeping one finite total system together with an exact full-qubit target is excluded. *On record: R6; #1007, #1055.*
3. **Which initial law?** A free datum: T1 holds for all laws. The global counting measure: QM ⇒ OI in T1 covers only rational laws (a reading), and an unconditional supply of prepared cells is excluded (off-`main` finding). A record-conditioned law: undecided in the records. *On record: none; #914 row 14 lists it as unsourced.*
4. **Exact or approximate?** Exact: one fixed finite system cannot carry the full qubit theory, so a completed or infinite carrier, or a per-menu family, is required. Approximate: T2 exists on paper for a constructed machine; the finite-precision bound and a native mechanism are open. *On record: R3 ("exact"), R4 (Level B), R5 (exact).*
5. **One realization for what?** Per law and horizon: T1 suffices. Per bound on dimension, outcomes, horizon and ε: T2. One for all experiments: exact forms meet the no-uniform-realization and horizon-growth obstructions, and a resource law must be stated. *On record: R4, R5 ("no fixed menu or horizon cutoff").*
6. **Which carriers?** Two-state: several Lean results exist only there. Every finite carrier: T3's three formulations hold. Typed: the QM ⇒ OI direction is a composition, not a named theorem. Infinite lattice: uniqueness only. *On record: R3.*
7. **May the complex-matrix setting stay an input?** Yes: T3 is available as it stands. No: commits to deriving it, where three of five parts are open. *On record: R5 calls the first a conditional reconstruction.*
8. **May OI carry added principles?** Yes: each needs its own sourcing argument and a consequence beyond the gap it fills. No: T5a is refuted for the stated interface, and every route on record adds a premise. *On record: R2, R3, R6.*
9. **Must every OI model behave quantum-mechanically?** Yes: a selection principle is needed, a new premise. No, a constructed or selected subclass suffices: T2's constructed family meets it on paper. *On record: R5 ("account for every operation the … interface admits").*
10. **How strong must QM ⇒ OI be, and what is a native model?** Containment of properties: already in Lean (T5a). Realization of every quantum experiment by a native model: open, and excluded for one fixed finite system with the full qubit theory. Adopting the Gate A contract as the definition makes a nonempty model class an obligation. *On record: R5.*
11. **Is the readback sector part of the target?** Yes: T0's paper proofs and the physical readback condition become part of it. No: T1 alone. *On record: R1 includes it.*
12. **Is Bell part of "full"?** No: it stays a separate obligation. Yes, on the adopted branch: H-Bell is a posit outside the linear rule, and a selector for the quantum bound is not supplied. Further choices: exclude super-quantum correlations; require no-signalling on complete histories or on a selected read; which cone is physical. *On record: R6, R7, R8.*
13. **What belongs to "QM"?** Each of these, if included, adds an open obligation: the quadratic Born exponent, the evolution relating two times, continuous time, infinite-region instruments, typed operations, Kochen–Specker contextuality. *On record: R5 (Born frequencies derived), R6.*
14. **Limit object: uniqueness or converse?** Uniqueness: nothing further to prove. Converse: a new theorem. *On record: R9.*
15. **What evidence standard?** Lean for each direction: T0 and T2 need formalizing. Paper proof with independent review: T0 and T2 need no formalization, and whether an independent review of their proofs is on record is not assessed here; T2's finite-precision bound stays open either way. *On record: none traced.*
