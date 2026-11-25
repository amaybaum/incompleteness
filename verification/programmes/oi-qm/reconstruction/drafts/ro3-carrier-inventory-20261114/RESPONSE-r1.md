# RO-3: response to the review of inventory r1

**UNREVIEWED.** This file gives the writer's disposition of each finding in `REVIEW-r1.md`
(ACCEPT WITH CHANGES, at `0d6d8812`). r1 is left unchanged. The changes are in `RO3-INVENTORY-r2.md`.
Each finding was checked at `main` `dfeec843` with `git show origin/main:<path>` before it was
applied. Paper-only: nothing was built or run.

Dispositions:
- **accepted**: applied as the review proposes;
- **accepted, modified**: applied with a stated difference;
- **noted**: no change needed.

Section numbers below refer to r2.

## Major

### M1. The recommendation OBL-RO3-1

**Disposition: accepted. OBL-RO3-1 is withdrawn as the recommendation, and the review's alternative
is proposed as OBL-RO3-2, labelled unverified.**

- **Checked.** Each point holds at source.
  - Translation invariance makes the periodic sets invariant almost by construction.
  - Gate A answer 3 reads "support subsystems realizing every quantum carrier" and answer 4 requires
    "accessible preparations" (#1169 comment 6876591512).
  - A preparation confined to a periodic sector fixes infinitely many sites, and the sector has
    measure zero under any prior of full support.
- **What was missing from r1.** Confinement to a finite invariant stage makes the support of the
  state finite. It is a finiteness posit of A1's kind, placed on the support of the state rather than
  on `S`. r2 says so in 0, 2.3 and §3, and adds Q10.
- **The alternative, checked as a paper reading only.**
  - Step (b): the dual of `F(u, v) = (v, Av − u)` satisfies `t^2 − A t + 1 = 0` over the Laurent ring
    `F_p[T_j^{±1}]`, an integral domain, so `det(F^n − I) = 2 − D_n(A)` with `D_n` the monic Dickson
    polynomial. For `α ≢ 0`, the top-degree term of `D_n(A)` in `T_1` is `α^n T_1^n`, so the
    determinant is nonzero. Over a domain, a nonzero determinant makes `F^n − I` injective on the
    dual module, so there is no nontrivial finite dual orbit.
  - Steps (c) and (d) rest on the Halmos criterion and on Rokhlin's theorem that ergodic
    automorphisms of compact abelian groups are mixing. They were not checked against the literature
    here.
  - r2 labels the whole argument unverified and makes the literature check its first step.
- **Is it discriminating?** Yes, but it largely tests a negative, and r2 says so. It decides, for
  the posited linear rule and the interface's own state, whether the recurrence route survives on
  the completion (Q3). Its failure branches are informative: a finite dual orbit would give a finite
  factor and open the G-fact route.
- **A tension found while checking.** `papers/SM.md:294` states that the exact linear rule "is not
  ergodic on its energy shells" and conserves further quadratic invariants. That statement concerns
  the finite torus, where the conserved quantities are functions. On the infinite lattice, sums of
  local densities are not functions under Haar measure, so the two statements need not conflict.
  This has not been shown. r2 adds the reconciliation as a preservation control of OBL-RO3-2.
- **Also added.** Two countercontrols that the mixing argument must not pass. The `p`-adic map has
  finite dual orbits, and the finite-dimensional real torus map has `F^L − I` nilpotent. These are
  the RR cases of M3.

### M2. `referenceState` omitted from I-qloc

**Disposition: accepted.**

- **Checked.**
  - `referenceState` is defined at `QuasilocalAlgebra.lean:901`, with `referenceState_stage` at :904
    and `uniformFamily_isStateFamily` at :887. The audit calls it "the tracial reference state"
    (`quasilocal-completion-audit.md:212`).
  - `RegionTower.lean`, header item (3), calls the uniform family "the only preparation the
    interface assumes" and proves it unique among families invariant under every local unitary, at
    finite stages.
  - Main:588 says no representation or sector is *selected* at the level of the laws.
  - `heisQ` is defined at `QuasilocalAlgebra.lean:1264`. No statement of the state's invariance under
    it was found (r2 §5).
- **Applied.** 0, 1.7, 2.5 and Q6 now name the state. The first missing step for I-qloc is its
  invariance under `heisQ` for the OI update (`ruleDynamics`, `SecondOrderDrive.lean:339`). r2 states
  two short [IR] routes: uniqueness of the tracial state, and Haar invariance for the linear rule.
  Neither is checked. The Hedlund lead is dropped.

### M3. On-`main` finite invariant subgroups and `p`-adic factors

**Disposition: accepted.**

- **Checked.**
  - `continuous-substates/README.md:105–107`: "`(Z/N)^{2L}` is a finite `F`-invariant subgroup of
    the torus, and its uniform measure is the finite substratum with alphabet `Z/NZ`".
  - :113–121 and :135–137: the `p`-adic lowest-digit readout, and readouts factoring through
    `Z_p → Z/p^kZ`.
  - Both are RR, for the free 1-D map.
- **Applied.**
  - r1's G-nest is split into G-sub (finite invariant sub-carriers) and G-fact (finite factors). The
    affected cells of 1.1–1.5 and 1.7 are redone.
  - The G-fam first missing step in 2.2 now names both forms of link: an embedding, and a projective
    system of factor maps.
  - The negative statement in 2.3 is narrowed to "for the Z/q lattice update on `Z^d`".
  - §5 lists the new hits and admits that r1's phrase list missed them.
- **One point added beyond the review.** The finite subgroups `(Z/N)^{2L}` are Haar-null in the torus
  [IR]. So they face the same access objection as the periodic sectors, while the factors do not. r2
  says so in 0 and 2.3.

## Medium

### m1. The 1.2 I-meas status rested on [IR]

**Disposition: accepted.** The cell now reads "conditional[`π ∘ T^L = π` almost everywhere]; open
otherwise". The mixing argument is moved to a context note, which says that no cell rests on it. The
[IR] label now covers readings by the review as well as by the inventory.

### m2. The scope of Main:155

**Disposition: accepted.**

- **Checked.** `papers/Main.md:155` concerns continuous-time Hamiltonian flows and mixing flows, and
  near-total common return of the visible cell at every sufficiently late time.
- **Applied.**
  - The 1.1 I-meas cell no longer cites Main:155 as a refutation of microscopic `φ^L = id`; it reads
    "open as a microscopic statement".
  - The 1.2 I-meas cell states Main:155's scope exactly.
  - 2.6 is reworded to match.

### m3. 1.4 G-nest rested on an unrecorded transfer

**Disposition: accepted.** The G-sub and G-fact cell is now marked [IR], with H-product on the stage
or factor as its hypothesis. It also notes that GR:587's constraint surface, with its fibre priors, is
not of product form as stated. Checked at `RootedClassificationAllTime.lean:176–193`.

### m4. The phase intervention principle was missing

**Disposition: accepted.**

- **Checked.** `papers/Main.md:588` lists "as a stated intervention principle rather than a
  consequence of its finite states and bijective dynamics, the phases", beside the state-mixing
  operation.
- **Applied.** In 1.7 the operational row is now its own row, "Carrier 3, operational". It carries all
  three conditions and says that it is not a property of I-qloc.

### m5. A status cited only to the off-`main` ledger

**Disposition: accepted.**

- **Checked.**
  - `papers/Main.md:556`: "the all-horizons fixed-representation question remains open".
  - `papers/Main.md:588`: the completion removes the cutoff "rather than characterizing all
    infinite-dimensional quantum instruments".
- **Applied.** Both now source the 1.7 "exact equivalence" cell. §6 records the change.

### m6. The #1055 controls were misidentified

**Disposition: accepted.**

- **Checked.** The #1055 body lists:
  - the finite-horizon equivalence;
  - readback and C4 content;
  - reverse finite realization;
  - every finite-carrier theorem;
  - the phase-locking lemma under (G1)–(G4);
  - Theorem 24(iii);
  - the observer-relative finiteness reading of #1053 and #1054.
- **Applied.** 1.6 now opens with that list. It adds rows for the controls r1 lacked:
  - reverse finite realization (`papers/Main.md:80` item (3), :516–520, :596);
  - the phase-locking lemma (`papers/Main.md:228–260`, preserved, with its dependence on A1 not
    traced here);
  - the observer-relative finiteness reading (`papers/Main.md:60`; `papers/Substratum.md:54`, :92).

  2.1 no longer says that 1.1–1.6 "are" the #1055 controls.

### m7. A resource statement omitted an open condition

**Disposition: accepted.**

- **Checked.** `papers/Main.md:574` ("depends on the open finite-`b` bound of clause (1)") and :596
  ("whose finite-`b` accuracy bound is open").
- **Applied.** Added to the resources bullet in 2.2.

## Minor

- **n1. Kernel citations.** Accepted. 1.1 F now cites `iterate_return_at_order` alone. 1.2 F adds K
  support: `rootedMap_at_order` (`RootedRecurrenceBridge.lean:55`, checked) and `rootedMap_periodic`.
- **n2. Rooted conventions.** Accepted. The 1.2 header states Main's convention, and the I-meas cell
  states the cell-conditioned convention of `measuredGamma`. Its docstring was checked at
  `ObservableMeasureReturn.lean:76–82`: "invertibility or measure preservation is not used".
- **n3. The `L ≥ 3` restriction.** Accepted. The operator convention of `papers/SM.md:296` gives the
  torus model for every `L ≥ 1`. The circulant adjacency of `papers/SM.md:1602` differs at `L = 2`.
  2.3 names the convention.
- **n4. "Countable completion".** Accepted. OBL-RO3-1 is withdrawn, and with it the phrase. For the
  record: the union of the periodic sectors is a countable dense invariant subset, directed by
  divisibility, not a completion.
- **n5. Readings that are cheap to decide.** Accepted, as [IR] context and secondary candidates in 1.1
  I-qloc, 1.4 and §3.
  - The first reading follows from the same determinant argument as M1: finitely supported
    configurations form the same Laurent module.
  - The Bernoulli shift reading is elementary.
  - Neither moves a status.
- **n6. The update and its kernel object.** Accepted. §3 names posit (vii) and `ruleDynamics`
  (`SecondOrderDrive.lean:339`, cited at `papers/Main.md:724`), and excludes the rounded rule
  (`papers/SM.md:294`, :298).
- **n7. Ledger standing.** Accepted.
  - Checked: #914 comment 6880700869 (`amaybaum`, 2026-11-14T16:31:06Z), "Yes. I accept ledger r8 as
    the successor to r5."; branch README at `4470bd02`, line 69.
  - r9 at `4470bd02` is a draft pending review. A diff of r8 against r9 on the cited identifiers shows
    one added row citing B-QM-16/17 and no changed row, so r2 keeps r8 as its ledger base.

## Owner questions

- **Q10 (sectors as subsystems).** Accepted. It follows from M1.
- **Q11 (the canonical state).** Accepted. It follows from M2. r2 notes that OBL-RO3-2 presumes a
  yes for its own scope.
- **Q12 (D2).** Accepted.
  - Checked: the #1055 body lists D2.
  - r2 cites what Main already says: `papers/Main.md:638`, for exact all-time realization by one
    fixed finite substratum; and :496 and :556, for growing horizons. It asks whether more is in
    scope.

## Controls

The six binding controls are unchanged in r2.

- r2 now states that sector confinement is a support-level finiteness posit, so finite access stays
  separate from finiteness (M1).
- No infinite class inherits recurrence: every infinite-class cell is open or conditional.
- A1 stays a posit.
- `referenceState` is examined as the interface's existing preparation, not selected for quantum
  reproduction (Q11).
- G-fam remains a family, and the factor route is a hypothesis on one fixed model, not an
  identification of the family with one.
