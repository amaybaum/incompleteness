# Focused confirmation: RO-3 inventory r7 (PR #1303), with RESPONSE-r6

**Verdict: REVISE.** The revision should be narrow: complete the map again, with no new mathematics
and no change of status.

Most of r7 checks out:
- Rows AM-27 to AM-35 add every consumer my r6 review listed, and they add them correctly.
- The r6 authority citation and AM-3 are right.
- The recipe reruns exactly as stated.

The recipe is not yet adequate for the owner's condition ("The A1 map must be complete before it is
accepted", #1169 c.6894115930). There are two reasons:
- Step 3 has no pattern for the corpus's most common phrasing of total finiteness, "finite
  deterministic …" or "finite configuration space/set/shell". That phrase family hides at least five
  further consumers.
- The L5 rule that classifies modules by the absence of a word misfiles four kernel modules that
  work on a finite microstate space with a permutation.

**So r7 does not yet meet the owner's condition.** Each fix is cheap.

## Object, base and limits

- **Reviewed.** `RO3-INVENTORY-r7.md` (SHA-256 `ae29f7d3…3bd8`) and `RESPONSE-r6.md`, against my
  review of r6. That review's digest `dfaaab89…a672` matches the one r6 cites.
- **Base.** `main` `7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`.
- **Limits.** Read-only: `git show`, `git grep` and the census. Nothing was built or run, and
  nothing was posted.

## 1. Rows AM-27 to AM-35

Every row was checked at source, and each is correct at its stated scope.

- **AM-27.**
  - `obs_not_layerFlowExecutable` is at `ExecSource.lean:129`, under the substratum context at :125.
  - `coherentLiftClass_eq_substratumClass` is at `LiftSource.lean:164`, with substratum sections at
    :196 and :296.
  - Census 6, 14 and 19–22 are current; 18, 23–27 and 29 are kernel-only, as stated.
  - Their modules put `[Fintype S]` on the sourced theory's carrier.
  - The row's hedge is apt: "conditional[A1], or about a finite stage".
- **AM-28.** `PhysicalC4Discharge` (:101, :109, :122) and `PhysicalC4StorageReadback` (finite `V` and
  `H` at :48 and :238) are census 35 and 36. Main:145's "for some `n`, because `(Γ_t)` is periodic"
  is traced to `rootedMap_periodic`.
- **AM-29.** `ensemble_underdetermined` is at :118 and `stochastic_interface_gap` at :182, which
  corrects my line :111. The [IR] about the OBL class is labelled correctly.
- **AM-30 and AM-31.** `theorem_19` is at `Reciprocity.lean:129`, with `[Fintype H]` at :40. The
  `Cut` section is at `PhysicalC4Discharge.lean:574`. SM:1376–1384, :52 and :92 are as quoted.
- **AM-32.** SM:22, :44, :112, :236, :308, :336 and :1654 are classified correctly.
- **AM-33.** A.8 and A.9 (GR:791 "The total system evolves unitarily under $U_\varphi$"; GR:807)
  match §1.5.
- **AM-34.** Sub:331 ("Let $P$ be a permutation of a nonempty finite set $\Omega$") and Sub:333
  ("Since $P$ has a finite order …") are as quoted. Census 61 and 62 are kernel-only, with
  `[Fintype H]` at :78 and :85.
- **AM-35.**
  - `MR-star.md:296`: "Main:488 assumes a finite `S`. For OI that finiteness is the total-finiteness
    posit". Its line numbers refer to that record's own base.
  - `TUNE-1-SOURCING-r2.md:139` lists ledger item (ii) among its premises.
  - Both use the posit as a premise. Treating them as context only is right.

The other new finds are verified:
- the AM-1 mirrors: `Introduction.md:12`, :93; `Medicine.md:13`, :25; `Bioinformatics.md:14`;
  `Complexity.md:430`, :474;
- the C3 mirror `Medicine.md:98`.

## 2. The recipe of §7.0, rerun

I reran it by reading only, at the base.
- **The Lean steps.** L1 returns the 6 modules stated, L2 the 4, L3 the 12, L4 20 and L5 79. Of the
  79, 37 contain "substrat"; the other 42 do not.
- **Step 3.** Over `papers/*.md` it gives 206 distinct lines.
- **Rerunnability.** The recipe can be rerun as stated.

### M1 (required): step 3 misses the phrase family "finite deterministic …"

I added the patterns
`finite \$S\$|finiteness of \$S\$|\$S\$ finite|eventual image|finite bijective|bijection (on|of) a finite|finite deterministic|finite reversible (substrat|world|system)|finite substrat`.
They give 45 lines that step 3 does not reach. Read in context, these are consumers, or mirrors of
rows, that r7 does not carry:

- **GR:613, the universality claim.** "Let $\mathcal{S}$ be any finite deterministic substratum …".
  §7.2 classes GR's universality results as not consuming A1, on the strength of GR:669 ("A1 …
  implies S3"). But the claim as stated at GR:613 puts finiteness in its hypothesis. Trace (U1)–(U3)
  through GR:613–669. Then:
  - keep the §7.2 entry with a reason that covers GR:613; or
  - move it to a row.
- **GR:70, the thermal rate ratio.** It comes "from finite deterministic reversible counting", with
  `N_i = |M_i|` on a shell. This is a separate result beside AM-22.
- **GR:28, the Tier 1 scope.** "For any finite deterministic system meeting the four conditions at
  its cosmological horizon". It frames AM-22 and the results that follow.
- **SM:1225–1227, the stationary-law gaps.** "A uniform measure on any invariant finite energy shell
  …"; "The $\varphi$-invariant distributions of a bijection of a finite set are exactly those constant
  on each of its cycles". These use the counting measure on finite cycles, so they belong with AM-4.
- **SM:1388, the Corollary of Theorem 22.** "Any finite deterministic system with energy-conserving
  dynamics and bounded-degree coupling …". It belongs in AM-31.
- **Complexity:374.** "The characterization theorem is proved for a *closed, reversible* substratum
  (a bijection on a finite configuration space; [Main] §2.3)".
  - This mirrors AM-20.
  - It is also a finding to propagate. It assigns a finite-substratum scope to the theorem, while
    AM-20 and Main:60 place its law-level content outside A1.
- **Framing statements of the AM-10 kind**, each stated with a finite substratum:
  - Main:710; GR:20 and :705; SM:1592;
  - Sub:14, :16, :22, :367, :429 and :465;
  - Struct:21, :45, :108, :377, :528 and :741; Meth:517;
  - Introduction:36, :53 and :129; Complexity:21 and :27; Computation:21 and :180.
- **Eventual-image mirrors.** Sub:94, a mirror of AM-3, and GR:861, a mirror of AM-33.
- **No change needed.** Main:578, a constructed finite superset, belongs in §7.2. Juno:261 is a false
  hit.

**Change:** add this pattern family to step 3, read the hits, and place each one.

### M2 (required): the L5 classification by absence misfiles modules

Within the 42 unread modules, a dynamics discriminator (`Equiv.Perm S|orderOf|φ\^\[|vis `) hits nine:
- ObservabilityQuotient, DomainGlue, ControlledQuotient and CoherentExtension (census 3);
- MonoidalCompletion, LieRankSource, SpectatorBridge, DiagonalTheory and BranchSelector.

The first four work on a finite microstate set `S` with a permutation `φ` and a visible map:
- `itiRelK` uses `vis(φ^k s)`;
- "horizons stabilize at `orderOf φ`" (`itiRelInf_iff_orderOf`);
- ControlledQuotient uses `orderOf` (:103);
- the ObservabilityQuotient header asks "whether minimality of the physical representative removes
  forever-indistinguishable microstates".

These are statements about finite reversible realizations, not about finite operational carriers.
§7.2 files census 3 under "finite operational carriers". That is right for GR:194, which is on
finite visible dimension. It is wrong for these modules.

The census note says that these quotients "underwrite no manuscript statement". So no manuscript
consumer is lost. They are kernel-only statements, in the same position as the census 1 entries
of §7.2: about nature only through A1.

**Change:**
- Read the nine modules, a cheap step (§A.16).
- Reclassify these four.
- Keep "classified, not read" as a stated scope limit only for the 33 modules that the discriminator
  does not hit.

### M3 (minor)

- State that `verification/lean/*.lean`, the six non-Mathlib modules, has no `Fintype`, `orderOf` or
  recurrence hits. That makes the Lean step cover all of `verification/lean*`.

### Is "complete relative to the recipe" honest?

As a literal statement, yes. r7 states the recipe and the limit of the 42 modules (§7.0, §7.4).

As support for the owner's condition, no. The recipe's prose patterns miss a phrase family that is
common in the corpus (M1). Its classification rule is unsound for at least four modules (M2).

The limit of the 42 does not block acceptance once M2 is applied. It can then stand as a stated
scope limit for the remaining 33. It blocks acceptance while that rule stays unchecked.

## 3. AM-3 and authority

- **Authority.** The r6 authority citation (r7:48–58) quotes #1169 c.6894115930 verbatim, and its
  goal link is correct.
- **AM-3.**
  - It is stated in the owner's words (r7 §3).
  - It is "proposed, not chosen".
  - O1 and O2 are labelled [IR] and used as no premise.
  - The first missing step, the controls, the countercontrols, the independent-consequence
    requirement and the decision rule match my r6 review.

Nothing further.

## Required changes

- **M1.** Extend step 3 with the phrase family "finite deterministic / finite configuration
  space, set or shell / finite \$S\$ / eventual image", and place every hit. In particular:
  - correct the §7.2 entry for GR:613;
  - add GR:70 and GR:28 at AM-22;
  - add SM:1225–1227 at AM-4;
  - add SM:1388 at AM-31;
  - add Complexity:374 at AM-20, as a mirror and as a propagation finding;
  - add the framing lines at AM-10 or AM-17.
- **M2.** Read the nine discriminator hits, reclassify census 3's four quotient modules as
  kernel-only statements on finite realizations, and narrow the "classified, not read" limit to the
  remaining 33.
- **M3.** Record that `verification/lean/` has no hits.

If M1 to M3 are applied and no new hit is found, I would expect the map to meet the owner's
condition. It would then be complete relative to a recipe that reaches the corpus's phrasing.
