# Re-review of AUDIT-C1 r2 against REVIEW-C1.md

- **File reviewed:** `AUDIT-C1.md` (r2), sha256 `230be89b9defed0252b7b104cb5bce76ee56e0779e758760e1c509ec7e6f0a8a` (re-hashed; it matches).
- **Previous version:** r1, preserved as `AUDIT-C1-r1.md`, sha256 `09bdac1c…0ab10` (it matches).
- **Corpus:** `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`.
- **Method:** Read-only. I re-checked every new or changed citation with `git show` and `git grep`.

## Verdict: **ACCEPT WITH CHANGES**

All six blocking findings are closed, and I found no new blocking hole. Four non-blocking items remain: one wrong line number (N1), one quotation attributed to the wrong interface (N2), and two scope notes (N3, N4). None changes an outcome or a class.

***

## The blocking findings

| r1 finding | r2 location | Status | What I checked |
|---|---|---|---|
| **B1** Act 45 evidence layer | r2:619-626, 634, 649, 678 | **Closed** | (a) The kernel verdict `A45-BRIDGE-PROVED` (result.md:3-5, 11-26) is separated from (b) the exact-arithmetic probe, which the record says is "not kernel statements … verdict does not contain them" (result.md:38-39). "Share every column entering the slice" is restored, and the tensor-factor non-separation is added. Summary item 6 now gives Act 45 prominence at both layers. W7 is existential, at the probe layer. `book/ch19-open-problems.md:289-291` is correctly identified as stating the separation with no layer; I verified the lines. |
| **B2** drive i | r2:305-318, 648, 658-664 | **Closed** | The finding is reclassified ELABORATING. The six corpus credits all resolve: GR:250; GR:258; `MinimalRepertoire.lean:13-25`; `LieRankSource.lean:36-43`; Intro:129; `two-mode-drive.md:54, 145-147`. "Hides" is gone. The D ≥ 3 identity `flow(X,π/2)·swap = diag(−i,−i,1)` is present, with the real-rotation contrast `diag(1,−1,1)` and the D = 2 global `−i·I`. The decisive form is the analogue of `diagGen_not_control`, at `LieRankSource.lean:146`, verified. The zero-diagonal lemma is marked non-decisive, citing `ReachabilitySeam.lean:71-72`. "Real QM" is narrowed to "real-matrix-preserving; no control". The check is now tied to the narrow sub-claim, not to F-1. |
| **B3** substratum box | r2:341-362, 646 | **Closed** | "`ExtendsSubstratum` unused" is kept, and the grep claim is accurate (defined `:401`, bound `:409`/`:415`, produced `:419`/`:425`). The diagonal class is credited to `LieRankSource.lean:87-119`, `SubstratumSource.lean:37-46` and `substratum_residual` (`:383-392`). Both gaps are stated correctly: (a) the unformalized step that swaps and `phaseGate` are monomial, so `ExtendsSubstratum` plus flows would give `DrivesElementary`; (b) the hypothesis `hc` is missing from the GR:262 box, from GR:264 and from Main:590, though disclosed at GR:260. The necessary-condition reading of "structural requirement" is acknowledged. |
| **B4** outcome 3 misapplied | r2:153-195, 366-390, 642, 651 | **Closed** | The operational reading of Main:68 is recorded as refuted by `oi_alone_not_qm` (`GeneralCarrier.lean:160-163`; GR:220-222). The scope is stated as `Fin 2`, one sealed core (`RealizesSealedOICore`, `OIRealization.lean:234-242`, verified) and the `FiniteOperationalTheory` interface. MQ-27 and MQ-28 are now texts that read MQ-01 too strongly. F-1 is a separate named question about extended mechanisms, outside the classes of `oi_alone_not_qm` and `substratumGen_not_control`. The latter's two-state scope is stated (`StructuralClosure.lean:348-349`; GR:228). F-1 now cites Q-A, MECH-2, `two-mode-drive.md` and PROG:40; the quotations from Q-A's header and from two-mode-drive §1 (`:18`) are verbatim. See N4 for one direction note. |
| **B5** W5 | r2:75-81, 673-676 | **Closed** | `pper_has_responseRealization` is credited as a kernel proof of the shared root prior for rooted families (Main:640; arc-b result.md:50-56). Zero-prior padding (result.md:86-91) is stated as its scope. Only the multi-time joint-law form is paper-only (Main:520-522). |
| **B6** MQ-12/13 outcomes | r2:297-303, 350-354, 644-646 | **Closed, one cite to fix** | The kernel statements stay at 1, and the statements as made move to 2, with imports and consuming steps named. The MQ-13 step `hc`/`hd` at `StructuralClosure.lean:417` is correct. The MQ-12 consuming-step line number is wrong; see N1. |

## r1's non-blocking findings

All are applied as the disposition table says. The checks behind that:
- **N1 (r1):** `MinimalRepertoire.lean:423-428`, the programme-level `amendments/amendment-1.md:19` and PROG:23/25 are all correct.
- **N2 (r1):** the `RevReal` docstring phrase is now attributed to the independent-prior form, which is correct.
- **N3 (r1):** the law-class wording is correct.
- **N4 (r1):** the "function of a Markov chain" description and the downstream U_φ/ħ cross-reference are correct.
- **N6–N9 (r1):** as stated in the table.
- **N5 (r1):** applied, with one attribution slip; see N2 below.

***

## Remaining findings (all non-blocking)

**N1. Wrong line for `control_of_phaseFree`.**
- **Where:** r2:291, "`MinimalRepertoire.lean:106`, inside `:552-560`".
- **Problem:** the theorem is defined at `MinimalRepertoire.lean:529` and invoked at `:559` inside `qm_of_oiPlusMin`. Line 106 is not it.
- **Fix:** cite `:529` for the definition and `:559` for the invocation.

**N2. The "no quantum content" quotation belongs to the typed interface.**
- **Where:** r2:252 and W3 at r2:667.
- **Problem:** both cite "carries no quantum content" (Main:590; GR:276-280) for the endomorphic `FiniteOperationalTheory` setting. In both sources the phrase is said of the *typed* carrier-general interface. My r1 N5 was equally loose here.
- **Fix:** the claim about the endomorphic setting already rests on `diagTheory` (GR:220; `GeneralCarrier.lean:157-163`), which suffices. Attribute the quotation to the typed interface, or drop it.

**N3. The tensor-factor fact also has a kernel anchor.**
- **Where:** r2:624 and summary item 6.
- **What is right:** Act 45 places tensor-factor invisibility in its probe layer, as R-I2 states. r2's assessment of Main:646's layering as correct is also right.
- **What is missing:** Main:646 tags the same fact `(kernel: padData_rooted)`. `padData_rooted` (`OperationalSourcing.lean:476`) is a general kernel theorem: padding with any ancilla unitary and weight leaves the rooted family unchanged.
- **Fix:** add one clause naming that anchor, so a reader of summary item 6 does not infer the tensor-factor half is unformalized anywhere.

**N4. State that the refutation runs in one direction (owner's symmetry rule).**
- **Where:** r2:158-166 and summary item 2.
- **Problem:** `oi_alone_not_qm` refutes the sufficiency reading only: that C1–C4 at that interface entail operational QM. The core is also realized by every theory with full control (`realizesSealedOICore_of_control`). So C1–C4 neither entail nor exclude QM.
- **Fix:** one clause making this explicit, so the refutation is not read as "OI excludes QM".

***

## Overreach (item F)

No overreach found. W2 and F-1 are marked [named question], each with its cheapest check, and no outcome is adopted. F-1 states that it proposes "no new check beyond those the cited records already set".

The D ≥ 3 identity is presented as an exact-algebra observation, labelled [audit derivation]. It is not a follow-up result being adopted. No replacement wording is drafted, and the ROADMAP item correctly routes any correction to a mutable record.
