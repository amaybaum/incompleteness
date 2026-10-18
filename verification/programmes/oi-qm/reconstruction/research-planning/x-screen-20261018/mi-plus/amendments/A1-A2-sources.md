# Amendment A1–A2: source-ledger rows S18–S24 and the S14 characterization

Amends `../PREREG.md` (C_P `80cafca5`, blob `9c84914d`, sha256 `0b605612…ea03d`), §2 only. Tags and abbreviations
as in PREREG. Kernel paths are under `verification/lean-mathlib/OIBridge/`.

**Admission.** This amendment is admitted under PREREG §0. No commit adds a file under `mi-plus/probes/`,
`mi-plus/runs/`, `mi-plus/check/` or `mi-plus/runs-check/`, and no such file exists in the tree that carries this
amendment. The text is that of amendments A1 and A2 of the independent review of the preregistration at `80cafca5`
(owner decision of 2026-10-18, PR #864), with each anchor checked at `80cafca5`.

**Effect on source decisions: none.** No SRC value of §4 changes, the `mi-plus-ledger` block is unchanged, and the
§2 Finding stands. Every new row has effect "none" on SRC. No candidate, predicate, control or rule changes.

## A1. Rows S18–S24

The search of §2 and drafting check X7 is extended with the terms detector, apparatus, which-path, observation
interaction, sharp update, Kraus, transpos and validity, over the same scope. The corpus states the notion of an
observer-level update constraint under these names, not under "meter". The hits are recorded as follows.

| # | object | location | tag | cone-level content on SEP ⊆ K ⊆ maxCone | effect on SRC |
|---|---|---|---|---|---|
| S18 | K∞-Geom, a sharp-update or singleton-face principle (the certain outcome of a proper sharp binary test identifies one state), and the research direction "physical observation interaction", in which sharp outcomes carry a sourced update rule | `verification/ROADMAP.md`:1044–1046, :1088–1091; `verification/audits/foundations/kinf-seams-audit.md`; KINF-1 halted under S12 (ROADMAP:1082–1084) | [UP]: a research direction, unproved; its corrected statement is not frozen | a single-body face principle; no pair form is frozen | none |
| S19 | complete positivity and composite operational validity of native availability | `cp_of_instAvail` ImplementationLocality.lean:541; `krausSoundExt_of_implementationGenerated` :963; `validity_of_implementationLocality` :971 | [AT] parts; composition [WA] | PSD → PSD on the matrix carrier; mentions no K | none; D3 if imported as a clause on K |
| S20 | transposition exposure | `factorExchange_exposes_ancTranspose` FactorExchange.lean:140; `ancTranspose_not_cp` PartialTranspose.lean:123; AncillaInterference.lean header | [AT], conditional on KrausSound | excludes the Γ operation relative to complete positivity on the PSD carrier; does not exclude Γ(Q3) as a state cone | none; D3 if imported as a clause on K |
| S21 | measurement as detector coupling | `papers/Main.md`:664–666 (a which-path detector couples to further visible degrees of freedom and changes the transition matrix); `papers/Methodology.md`:401; `book/ch14-quantum-computing.md`:78 (the dilation picture, stated as a hypothesis of closure under quantum instruments) | [WA]; the ch14 statement is an explicit hypothesis | an operation (dephasing, cf. N4); the ch14 statement is D5 | none |
| S22 | readback | `CausalReadback.lean`; `RoutedReadbackAtStorage` PhysicalC4StorageReadback.lean; `PhysicalC4Discharge.lean` | [AT] | visible-law (configuration-diagonal) content; class (a) by N3 | none |
| S23 | Bell ceiling for a screened local completion | `papers/Main.md`:362–373 | [WA] | \|S_CHSH\| ≤ 2; Q3 violates it, so as a clause on K it fails QM | none (not a candidate) |
| S24 | rank-one selector; monomial–Lüders compatibility | `BranchSelector.lean` | [AT] | an update form on the matrix carrier; class (a) | none |

Considered and not added: StateMixingCoupling (its datum is a non-native rotation postulate, D4); HiddenCoherence
and InstrumentAvailability (they concern operations, not K); Separability (the PPT implication, a tool rather than a
source); `papers/Substratum.md`:228 E1–E7 (empirical quantum mechanics, an E-input rather than an OI source);
ROADMAP P0/P1 (no MI content).

Added to the §2 Finding: S18 is the corpus's named observer-level update principle. It has no frozen statement and
is unproved, so it fails "independently derived". No pair-level form of it is frozen here, since freezing one would
introduce a premise.

## A2. S14 rewritten

Row S14 reads:

| # | object | location | tag | cone-level content on SEP ⊆ K ⊆ maxCone |
|---|---|---|---|---|
| S14 | composite operational validity: available branches send PSD to PSD and are trace-preserving in sum | `CompositeOperationalValidity` OperationalValidity.lean:88. For the observer theory it follows from `validity_of_implementationLocality` (ImplementationLocality.lean:971) and `implementationLocality_of_reversible` (MicroscopicReversibility.lean:227) applied to `obs_reversibleImplementationLocality` (SubstratumInterfaceAudit.lean:823) | [AT] parts; composition [WA] | its domain is the PSD cone of the matrix carrier, so as a clause on K it presupposes PSD (D3) |

For the observer theory, composite operational validity is derived in the kernel by the composition above; the
EmbeddedObservation.lean header's "treated as admissibility and no source for it is proposed" is local to that module
and is not the ledger's characterization. The D3 classification of S14 is unaffected: the derived validity is
PSD → PSD on the matrix carrier.

## The two source clarifications

**(a) The sharp-update principle.** The proposed sharp-update principle (K∞-Geom, S18) is unproved, and it cannot
serve as a derived observer-level measurement principle. It supplies no source for any candidate of §4.

**(b) CP and operational validity.** Native complete-positivity and operational-validity results exist on the PSD
matrix carrier (S14, S19, S20). Their extension to arbitrary candidate cones K with SEP ⊆ K ⊆ maxCone is not
established. In particular they supply no source for C11 (OV-nat) or C12, whose SRC stays FALSE.
