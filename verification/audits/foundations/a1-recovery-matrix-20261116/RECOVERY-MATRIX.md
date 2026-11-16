# A1 recovery matrix

**Status.** WIP, paper-only source audit. The first checkpoint isolates the local algebra in P12(a). The rest of the matrix is pending. Physical source **NOT PASSED**.

**Authority.** On 2026-11-16, owner `amaybaum` said “Sounds good, let's proceed as suggested” in the coordinating session, as recorded in [#1169 comment 6911396632](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6911396632). The quote authorizes the matrix and independent review. The recovery tests below are proposals for later owner decisions.

**Goal link (§A.47).** #1169, priority 2: determine which material claims can be supported without adopting total finiteness and which source or proof gaps carry over.

**Sources.** `main` is pinned at `32322301e4b8c54f000560db73201260c63bf7f8`. All manuscript and Lean locators use that revision unless specified. Main:728(ii) records A1 as open and unadopted. Substratum:98 still specifies a finite periodic lattice. Together with Main:728(viii), (xiii), that specification yields a finite configuration space for the selected lattice model. It does not settle nature's cardinality.

## P12(a) · Local algebra on the specified link and matter data

**Provisional A for the forward, conditional algebra.** Substratum:193 lists A1 for the combined theorem. The local proof steps instead consume the six signed cubic links (SM:374–376), an equivariant single physical copy and custodially scalar kinetics (SM:340–342, :360–370), a generic equivariant condensate, and a specified charged family (SM:579–597). They do not take a count over the total carrier. Corollary 1b's normalized branch and the selection of dimension are inputs to parts of Stage 2, and are traced separately under P12(b).

SM:340–342 proves the unitary stabilizer on the supplied condensate. SM:579–585 constructs a correlated central quotient and states the gap in realizing that quotient on the raw carrier. SM:519–529 establishes availability of charged tensor products and carries chirality and light-mode selection as separate obligations. `OIBridge.LinkDecomposition.theorem_7` (`verification/lean-mathlib/OIBridge/LinkDecomposition.lean:479`) verifies the decomposition on `Fin 3 × Bool`, the link type. SM:390–416's converse Bravais selection is a distinct paper argument within its nearest-neighbour construction.
