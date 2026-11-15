# Response to the review of LIT-REUSE r1

**Review:** `REVIEW-LIT-REUSE-r1.md`, ACCEPT WITH CHANGES. **Revision:** `LIT-REUSE-r2.md`;
`LIT-REUSE-r1.md` is unchanged. **Writer:** Claude. **Date:** 2026-11-15. Paper-only: no
repository edits, commits, pushes or Issue changes.

Each change was checked first-hand against the primary text or the bibliographic record before it
was applied.

## Required changes

| ID | Check made | Change in r2 |
|---|---|---|
| C1 | arXiv:1706.07370v2, "Data repository": "The complete raw dataset is publicly available from an open repository"; the dataset "does not include the data purged in real time … due to long sequences of dark measurements"; of 54.5 million measurements about 1 million were ignored because of a thresholding error, leaving "almost 53.5 million" evaluated. The purge rule (more than 55 dark results in a row, attributed to leakage) is in the main text. The repository itself was not opened | §1.12 gains a "Raw data and completeness" row with these statements and a labelled writer's reading that the published record is not the complete record and that the purge is outcome-triggered. §2 table: Leupold "Raw data published" reads "yes", with the exclusions. R-5 rewritten: one paper read (single-ion) publishes raw data; no Bell-type experiment read does |
| C2 | arXiv:2102.02550v2 Eq. (7), S_n = (1/n) Σ_m \|C(x_m, y_m)\|; Eqs. (9)–(10), shared indices k (Alice1, Bob1) and l (Alice2, Bob2); "the measurement directions of Alice and Bob are chosen to be opposite". Supplement §B gives the Bell settings but not the combinations acquired | §1.9 settings row states the matched indices and that the Bell-test combinations are not stated; the bearing row and R-2 now say that the remote policy is never varied with the own policy held. The claim that the scanned configurations would determine the G3 comparison is removed |
| C3 | `S3-U3-r3.md` §5.1 (k3): Alice `(x, x)` with Bob `(0, 0)` and `(0, 1)`, and the mirror pairs; §5.2 (k3′): Alice `(x, x)` with Bob `(0, y₂)` and `(1, y₂)` for one fixed `y₂`; §10.3 wording unchanged from r2 | Reading grid rewritten: §10.3's wording is the headline; G1 is two uses per wing with per-configuration settings; G3 and G4 are the (k3) and (k3′) policy patterns, G4 with law (9)'s repeat. Zhu, White and R-2, R-3, R-6 re-mapped against them. The note now cites U3 r3 |
| C4 | arXiv:1504.02707v2: φ ranges over [0, π/2], "When φ = π/2 this operation becomes a control-NOT gate and implements a projective measurement"; data reported "For projective angles φ ≈ π/2" | §1.10 uses row and bearing row: first use tunable up to projective; G4 fails because the settings change between the uses. §2 table instrument cell corrected. R-6 no longer calls both two-sided experiments unsharp |
| C5 | Crossref doi:10.1103/PhysRevResearch.5.013104: "Recycling nonlocality in quantum star networks", *Phys. Rev. Research* 5, 013104 (2023), the same nine authors in the same order. OpenAlex abstract matches the arXiv abstract with one added sentence | §1.8 citation records it as a candidate published form whose identity with the arXiv text is not established here, as for Xiao. The Research Square sentence is removed |
| C6 | arXiv:0904.1655v2: ⟨X_DHV⟩ = 2.23(5) on Ψ ∝ \|↑↑⟩ + iγ\|↓↑⟩ + γ\|↑↓⟩ + i\|↓↓⟩, γ = √2 − 1, Mermin–Peres square with σ_y and σ_z exchanged, ⟨X_KS⟩ = 5.22(10) | §1.12 key-numbers cell names the state; R-3 says the value was measured on a non-singlet two-ion state |

## Optional changes

| ID | Change in r2 |
|---|---|
| O1 | A *[writer's reading]* label is defined in the method and applied to: Mao (settings per acquisition, not stated; random choice only in the protocol), Xiao (λ not recorded per event), Zhu (settings fixed per configuration; k = l as a repeated own setting from Eq. (10)), and Leupold (completeness reading) |
| O2 | Authorization gives `amaybaum`, 2026-11-15T09:49:19Z, and the full quoted text, "Q4: yes, the performed experiments that use one source twice are read first-hand." |
| O3 | Cheng, Liu, Baker, Hall arXiv:2109.03472 labelled **ABSTRACT**. A **LOCATED** label is added; Cabello arXiv:2103.11844 and Cheng, Liu, Baker, Hall arXiv:2102.11574 (*Phys. Rev. A* 104, L060201, author list checked on Crossref) are listed under it, described only as the review reports them |
| O4 | §1.7 records that the NJP abstract on Crossref matches the arXiv content, with the two phrases, as support for the identification without establishing it |
| O5 | §2 now reads that none of the Bell-type experiments read reports space-like separation of the wings, with the explicit statements cited by paper |

## Central conclusion after C1–C3

R-6 still holds, stated at the scope of the papers read. Leupold's published raw dataset (C1) is a
single-ion record, not a wing of a Bell pair, and its public form excludes purged and
threshold-affected measurements. With (k3) and (k3′) stated correctly (C3), neither two-sided
experiment read realizes the compared policy pattern: Zhu 2022 matches the two wings' settings
(C2), and White 2016 changes both wings' settings in one fixed configuration. No experiment read
reports a same-axis repeat on a wing of an entangled pair after a projective first use. Choi et al.
2020 remains the one located experiment not read in full.
