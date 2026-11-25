# #1049 report: changes from r3 to r4

**Basis.** Owner decision (amaybaum, 2026-11-25, #1169 comment 7167657546): "#1049 | Narrow the three passages to support available on main. Retain r5 as provenance only, not acceptance support."; "Both | Add the preservation rationale and remediation plan required by §A.46 item 8."; "Keep r1 and r2 with explicit superseded notices. Each notice should identify the authoritative revision and its corresponding correction record. Preserving the research history is valuable, provided obsolete conclusions cannot be mistaken for current results."; "Do not land #1226 merely to resolve the #1049 dependency when the narrower, independently supported conclusions are sufficient."

**Input.** REPORT-r3.md at `389d6ea46a2bac11f257acd78536a982a5b2c15d`, and the landing assessment's §A.42 item 8 finding: three passages cited the unmerged r5 report (draft PR #1226, branch `research/a5-reassessment-r5-1049-20261110`) as support, and §6 called r5 context only. Manuscript and record pin unchanged: `main` = `e2e2a623265187a28ebec604ab8bcc672742888f`.

**Scope.** Only the changes below were made. Every other line of REPORT-r3.md is carried into REPORT-r4.md byte for byte. No mathematical result changes beyond the narrowing of the three passages; REPORT-r3.md is unchanged.

**Support checked at the pin.** A5-LA Corollary B0.3(a)–(e) (uniform offset; removable by a static uniform shift iff b ∈ (κ − 2)ℤ/q; S1 has no fixed point; a non-uniform fixed point exists for an odd prime q ∣ N), R3, Proposition 2.5 (uniform mode on the lift; secular growth bt²/2 at κ = 2) and D14; Q4 paragraph "Resonance" before §1 (κ_a = 2μ_a; resonant iff μ_a = 1), N0 (offset in A₁ given H-b), N1 (under (A-lin) the linear parts are G_v at every nonzero uniform offset; off resonance a uniform fixed point p and a linear rule in y = z − p; at resonance β ∉ Im(I − L)) and §6 Q4b, Q4c; POSIT-MIN D2, row (xii)(e) and DV-1 (`linkF : V →+ V`); SM:232 (the map φ → L_obs is not proved). A keyword search of `verification/`, `papers/` and `book/` at the pin ("GA7", "link sum", "link-sum", "link-separab", "non-additive link") found no record addressing A6's interface for non-additive link maps.

***

## C1. §0, new line "Revision r4"

Added after the "Revision r3" line.

- Old: (none)
- New:

> **Revision r4.** Revision r4 applies the owner decision "#1049 | Narrow the three passages to support available on main. Retain r5 as provenance only, not acceptance support." and "Both | Add the preservation rationale and remediation plan required by §A.46 item 8." (amaybaum, 2026-11-25, #1169 comment 7167657546). The edited passages are §0 (this line), §1.4 (the last Q-α bullet and the first two Q-β bullets), §3 (one row) and §6 (one limitation), and §7 is new. The narrowed passages rest only on records on `main` at the pin; r5 is provenance only. No other result changes. CHANGES-r4.md lists each change.

## C2. §1.4, Q-α, last bullet (finding (c))

The dependence on A6's interface was supported only by r5 O-G. It is narrowed to what POSIT-MIN states on `main`: a non-affine answer needs A6's formal interface checked for the additivity its type builds in. Whether A6's interface decides where affinity comes from is stated as open.

- Old:

>   - Q-α is open and turns on owner decision POSIT-MIN D2 together with A6's interface (r5 O-G).

- New:

>   - Q-α is open. On the records on `main` it turns on owner decision POSIT-MIN D2, the interface reading of O4. An answer that requires a non-affine update would also need A6's formal interface, which types the link coupling as additive (`linkF : V →+ V`), checked for the additivity it builds in (POSIT-MIN (xii)(e) and DV-1; A5-LA D14). Whether A6's interface, read for non-additive link maps, itself bears on where the affine restriction comes from is not addressed in the records on `main` read for this report (§0); it is open.

## C3. §1.4, Q-β, first two bullets (finding (a))

The locus and its content were supported jointly by r5 §3.3. They are restated from A5-LA and Q4 alone. The restatement narrows r3 in four respects, each following those records: the locus is defined as the content no static uniform shift removes; that every consumer's use of b = 0 reduces to it (r5's contribution) is stated as open and assigned to the §5 trace; "no fixed point" holds on the lift and for S1 but not over ℤ/q with an odd prime q ∣ N (B0.3(e)); and the (A-lin) loss of U(1)_S, which Q4 N1 finds at every nonzero uniform offset, is stated as irremovable on the locus and removable off it.

- Old:

>   - The record narrows this to one locus: the uniform k = 0 A₁ sector at κ ≡ 2, equivalently μ_{A₁} = 1. It is A5-LA R3, Q4c and r5 §3.3 together.
>   - Only there does a nonzero offset carry invariant content: no fixed point, a secular uniform drift on the lift, and loss of the singlet U(1)'s linear part under (A-lin).

- New:

>   - The records on `main` locate the content of a uniform offset that no static uniform shift removes at one locus. For a second-order, translation-commuting rule the offset is uniform, and a static uniform shift removes it iff b ∈ (κ − 2)ℤ/q (A5-LA B0.3(a), (c); R3), so at prime q it is irremovable only at κ ≡ 2. On the lift this is the uniform k = 0 mode (A5-LA Proposition 2.5). With H-b the offset lies in the A₁ block (Q4 N0), and κ_{A₁} = 2μ_{A₁}, so the locus is the A₁ resonance μ_{A₁} = 1 (Q4, paragraph "Resonance" before §1; Q4c). Support: [D]. Whether every consumer's use of b = 0 reduces to this locus is not traced in the records on `main`; that is the §5 trace, and it is open.
>   - On that locus the offset carries content that no static uniform shift removes [D]: on the real lift the uniform mode grows secularly as bt²/2 (A5-LA Proposition 2.5); there is no fixed point on the lift (Q4 N1, resonance case) or for S1 over 𝔽₅ (C2; B0.3(d)), although over ℤ/q with an odd prime q ∣ N a fixed point with a non-uniform profile exists (B0.3(e)); and under (A-lin) the loss of the singlet U(1)'s linear parts, which Q4 finds at every nonzero uniform offset, is removed off the locus by the static uniform shift to the fixed point and is not removed on it (Q4 N1).

## C4. §3, classification table, one row (finding (b))

The off-`main` support is removed and the row is narrowed as in C3.

- Old:

> | b = 0's invariant content is confined to the uniform A₁ sector at κ ≡ 2 | paper derivation (A5-LA); off-`main` r5 §3.3 | A5-LA R3; Q4c; r5 | H-b; lift; uniform offset |

- New:

> | At prime q, the content of a uniform offset that no static uniform shift removes is confined to the uniform sector at κ ≡ 2, which with H-b is the A₁ resonance μ_{A₁} = 1; whether every consumer's use of b = 0 reduces to it is open | paper derivation, model-reviewed | A5-LA R3, B0.3, Proposition 2.5; Q4 N0, N1, Q4c | second-order, translation-commuting rules; prime q; H-b; lift; uniform offset; consumer reduction not traced (§5) |

## C5. §6, Limitations, r5 bullet (finding (d))

Made consistent with C2–C4: r5 is provenance only.

- Old:

> - r5 is off `main`. Its P1/GA7-α results are cited as context only.

- New:

> - r5 (draft PR #1226, unmerged) is off `main` and is provenance only: no conclusion of this report rests on it. §7.8 classifies each reference to it.

## C6. New §7, "Preservation and verification status (§A.46 items 4 and 8)"

Added after §6, separated by a rule. Old: (none). New: the full text of REPORT-r4.md §7, with subsections 7.1 (what the record contains), 7.2 (scope and limits of the evidence), 7.3 (independent reviews: PR #1561 comments 7166779576 and 7167108875 and the r3 delta review), 7.4 (accountable Issue #1049), 7.5 (verification status per claim class), 7.6 (remediation plan, gaps V-1 to V-10), 7.7 (preservation rationale), 7.8 (per-reference §A.42 item 8 trace; support off `main`: none) and 7.9 (status of r4, quoting the owner decision).

## C7. Superseded notices prepended to REPORT.md (r1) and REPORT-r2.md

Each notice is one paragraph followed by a blank line, placed before the file's first line. Nothing else in either file changes.

- REPORT.md, new first paragraph:

> **Superseded; kept as research history.** This file is revision r1 of the #1049 report and is superseded. The authoritative revision is REPORT-r4.md in this directory, and its correction record is CHANGES-r4.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2) and CHANGES-r3.md (r2 to r3). Below this notice the text of r1 is unchanged. It is kept as the research history, and its conclusions are not current results.

- REPORT-r2.md, new first paragraph:

> **Superseded; kept as research history.** This file is revision r2 of the #1049 report and is superseded. The authoritative revision is REPORT-r4.md in this directory, and its correction record is CHANGES-r4.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2) and CHANGES-r3.md (r2 to r3). Below this notice the text of r2 is unchanged. It is kept as the research history, and its conclusions are not current results.

***

**Re-check.** REPORT-r4.md contains no citation of r5, PR #1226 or its commits as support; the remaining references are in §0 (sources read), §1.1 (r5's standing, stated as not support), §6 and §7.8, each classified as provenance in §7.8.
