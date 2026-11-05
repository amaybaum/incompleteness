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
`result.md` (A11), and records:

1. its author or producing session;
2. whether the second writer had access to the first derivation;
3. any relevant dependency or shared intermediate result, recording "none" explicitly where there is none.

Shared permitted inputs, namely the frozen rule, the declared hypotheses (the row's list `Λ`) and the row specification,
are not dependencies under item 3; an intermediate result taken from the first derivation is. Access to the first
derivation does not by itself establish dependence. A second derivation that relies on an intermediate result of the
first does not meet the first condition above, so the row ends in UNDECIDED(G6). These records are procedural: they
introduce no gate or token, and recording them does not by itself establish independence. A written derivation is
recorded as a paper derivation and is never presented as a computational or kernel-checked result.

**Source.** amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6656166518
(2026-11-05T10:54:11Z):

> **R2 — Choose Option A.** A positive P1 member row requires a second, independent written derivation, even when no enumeration is performed. The two derivations must genuinely be independent, not merely restatements. Both must establish the relevant claim under the same declared assumptions. If the requirement cannot be satisfied, the row remains UNDECIDED(G6). Do not treat a paper-only derivation as a computational or kernel-verified result. Record this as a narrowly scoped amendment, without silently rewriting the protected base text.

**Source of the recording requirement.** amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment
6657308064 (2026-11-05T11:53:35Z), quoted in part:

> **A10 — KEEP.** Keep the additional recording obligation in A10. Each independent derivation must identify: Its author or producing session. Whether the second derivation's writer had access to the first. Any relevant dependency or shared intermediate result. This information is useful for evaluating genuine independence under G6. It introduces no new scientific gate or token and does not establish independence merely by declaring it. I approve retaining it as a procedural recording requirement.

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6657384912 (2026-11-05T11:57:45Z):

> I choose Option (b): add the third recording requirement to A10.
> The additional verification work is justified because independence is important to the credibility of a positive K1-RDY result. We should be able to audit how the two derivations were produced, not merely rely on a declaration that they are independent.
>
> Authorize one narrowly scoped control-plane commit adding the third A10 recording requirement. Each derivation must record: 1. Its author or producing session. 2. Whether the second writer had access to the first derivation. 3. Any relevant dependency or shared intermediate result, explicitly recording "none" where appropriate. Distinguish shared permitted inputs (the frozen rule, declared hypotheses and row specification) from intermediate results taken from the first derivation. Access alone does not automatically establish dependence. However, a second derivation that relies on the first derivation's intermediate results cannot satisfy G6's independence requirement.
>
> Required checks: Preserve the protected 313 lines and their hash. Do not alter scientific hypotheses, gates, tokens or conclusions. Obtain an independent delta review of the new exact head. Re-read all A4 historical heads. Repeat the applicable preservation and control-plane checks. Present the revised exact SHA for approval of a new `verify.yml` dispatch.
>
> The verification already running at `9fa37d0a` remains valid evidence for that historical head, but it must not be treated as the final verification of the revised candidate F. **Do not designate F yet.**
