# SM Theorem 3 — direction and converse audit (draft; no manuscript change)

Date: 2026-10-27. Target: `papers/SM.md` §4.3, Theorem 3 and adjacent Remark (main at inspection).

## Verified source-level discrepancy

The displayed statement calls **center independence of lattice dynamics equivalent to exact chiral symmetry**. The accompanying proof argues **center independence ⇒ chiral symmetry** on its specified staggered branch; it does not prove **chiral symmetry ⇒ center independence**. The adjacent Remark says the 4D lattice Laplacian has a nonzero diagonal self-term which is *not* a mass term, and its standard staggered factorization has exact chiral symmetry. The text's own scope thus contradicts the unconditional equivalence.

## Direction ledger

1. **Forward implication (conditional):** On the defined staggered branch, center independence leads to exact chiral symmetry. Retain only with the branch's actual operator and lattice assumptions; verify precise Lean theorem and its hypothesis list rather than treating a prose proof as a complete certificate.
2. **Converse (unproved / potentially false):** Exact chiral symmetry does not by itself imply absence of a microscopic center self-term. The existing 4D Laplacian remark is a candidate counterexample; verify which notion of center term is compared (microscopic real update, observer-level kernel, or staggered Dirac operator) and ensure the same domain is used on both sides.
3. **Operator identity:** Where `{D,ε}=0`, `ε²=I`, adding a staggered mass term `m ε` gives `{D+mε,ε}=2mI`. This tests a *specific mass deformation*, not all possible center dependence. A scalar offset `p₀ I` instead gives `2p₀ ε`. Distinguish these cases.
4. **Memory inference:** Neither implication provides observer-level predictive memory or P-indivisibility by itself; those come from independent readback and finite-recurrence hypotheses.

## Proposed manuscript edit (NOT APPLIED)

Replace the unconditional biconditional heading with:
> **Theorem 3 (center independence implies chirality on the stated staggered branch).** Under the branch's specified lattice and operator hypotheses, center independence gives exact staggered chiral symmetry.

Retain the remark on non-masslike center terms and add:
> The converse is not established and does not follow merely by identifying a general diagonal self-term with a mass; the exact relation depends on the operator and the projection used.

## Required verification before editing the theorem

- Inspect the precise Lean declaration and `#print axioms` evidence for the forward implication, including the operator-level identity.
- Check the 4D-lattice counterexample with matched definitions (no shift between microscopic and observer-level center independence).
- Propagate a corrected direction to Main, book/FULL mirrors, Explainer, proof/status ledger, and any theorem references only after a separately reviewed patch.
- Add a regression probe rejecting the bare phrase `equivalent to exact chiral symmetry` at this claim class.
- Record independent review and CI on an exact head; no scientific status upgrade.

This note opens the investigation only. It does not establish a universal countertheorem, change theorem text, or authorize a merge.
