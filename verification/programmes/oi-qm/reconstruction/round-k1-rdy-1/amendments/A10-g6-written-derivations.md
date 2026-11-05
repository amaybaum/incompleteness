# A10. G6 for P1 member rows under paper-only execution

**Governs:** base line 151, the clause "For enumerated rows (including P1 member rows), "independently" means a second,
separately written enumeration that imports nothing from the first and matches it row by row" (continued on line 152).
No base text is edited. The rest of G6 (lines 150–153) stands.

**Addition.** Execution is paper-only (§12, OD-4), so no row is enumerated. A P1 member row that reaches a positive
passes G6 only if a second written derivation of its token is made independently of the first:

- the second derivation is not a restatement of the first and takes none of its intermediate results as given;
- both establish the same claim, the row's token, under the same declared assumptions: the frozen rule and the row's
  list `Λ`;
- both, and the adversarial note of lines 150–151, give the same token, with G2(b) recomputed from the rule part alone.

If this requirement cannot be met, the row ends in UNDECIDED(G6). Each derivation is a separate derivation file named in
`result.md` (A11), and records its author or session and whether the second writer had access to the first derivation. A written derivation is recorded as a paper derivation and is never presented as a computational or
kernel-checked result.

**Source.** amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6656166518
(2026-11-05T10:54:11Z):

> **R2 — Choose Option A.** A positive P1 member row requires a second, independent written derivation, even when no enumeration is performed. The two derivations must genuinely be independent, not merely restatements. Both must establish the relevant claim under the same declared assumptions. If the requirement cannot be satisfied, the row remains UNDECIDED(G6). Do not treat a paper-only derivation as a computational or kernel-verified result. Record this as a narrowly scoped amendment, without silently rewriting the protected base text.
