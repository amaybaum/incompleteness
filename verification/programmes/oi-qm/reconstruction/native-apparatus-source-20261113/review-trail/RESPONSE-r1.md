# RESPONSE to the independent review of r1 (TUNE-1 sourcing unit)

Review: `REVIEW-r1.md`, ACCEPT WITH CHANGES (R1–R6 required, m1–m10 minor). Revision: `TUNE-1-SOURCING-r2.md`
and `NOTES-r2.md`; r1 (`TUNE-1-SOURCING-r1.md`, `NOTES-r1.md`) unchanged. Each item was checked against
its cited source before it was applied. **Disagreements: none.** The stop location, the candidate
and the verdict are unchanged.

| Item | Check made | Disposition | Where in r2 |
|---|---|---|---|
| R1 | #1169 c.6854774010 read through the GitHub API: `amaybaum`, `OWNER`, 2026-11-13T13:47:03Z, "Yes, both (Recommended)"; the TUNE-1 bullet matches the review's quotation verbatim. S4:641–644 is the FAIL-CLASS row form; S4:451–458 the theorem's uses | Applied as written: §0 bullet replaced by the quotation; N1 verdict and §5 NL-C bullet reworded (no hypothesis of NL-C fails; the bound applies and is reported; the FAIL-CLASS family condition is not met); §7 relay row replaced; NOTES item 1 resolved | §0; N1 verdict; §5; §7; NOTES-r2 item 1 |
| R2 | OA1:522 ("Under μ-O (derived) and μ-R: N1-K can be native (swap); N1-S is open"; verdict "measure-relative"); OBS:121 and :458–460 (rooted-law conditioning); OBS:888–892 (D-OB7); OA1:168–170 (D4(b) μ-G only) | Applied as written in the header, the (b) row, the status paragraph, N3.2, the N3 verdict, §5 and F-S4 | header; §2 (b) row and status paragraph; N3.2; N3 verdict; §5; F-S4 |
| R3 | AF:169–170 (Q6′(i) credit on `𝒯_L`); AF:171–175 (`L` independent of `n`); S4:444–448 (step 6 uses tests in `𝒯_L`); variable-length count `Σ_{j≤m} Q^j ≤ (4/3)Q^m` with `Q = q^{2|C|} ≥ 4` re-derived by hand, giving `½ log_q((1−4ε)/(8ε))` | Applied as written: proviso `m + 1 ≤ L` kept, `m ≥ L` open, "space to time" sentence removed; F-S1 and AW-SRC-1 narrowed | N1.3; F-S1; AW-SRC-1 |
| R4 | Code Review Rules (necessary → sufficient; no identification without a formal map); the generating rule and `O_n` (P:211–222) | Applied as written: F-S2 states necessity only; AW-SRC-2 and the productivity verdict scoped to TUNE-1's schema with finite alphabet | F-S2; AW-SRC-2; productivity verdict |
| R5 | OA1:523 (gap 2: translation-only action) and OA1:530 ("N2 is the earliest failure that holds under every measure") | Applied as written in the (c) row | §2 (c) row |
| R6 | OBS:69–73 ("H-μ denotes the exact unconditioned uniform probability") against P:145 (TUNE-1's H-μ: independence of the unread world) | Applied as written in N3.5 | N3.5 |
| m1 | Main:724 items (ix) (bounded coupling degree) and (xi) (center independence); P:85–89 (reference instance, SM:296 `α = 1`) | Applied in the (a) row | §2 (a) row |
| m2 | OA1:147 (law uniform at every `t`), OA1:522 ("every bijection") | Applied: citation added in N3.1 | N3.1 |
| m3 | OA1:174, "D4 dissolves under MP-0a" | Applied in the (e) row, with the consequence that in-`V` records consume further designated cells | §2 (e) row |
| m4 | P:206–208 (no record before round `j` depends on `c_j`) | Applied in the (b) row. Propagated with the same qualifier to the two parallel statements of the same fact (N3.1 and F-S2's herald remark), so the three statements agree; no other content changed | §2 (b) row; N3.1; F-S2 |
| m5 | OA1:108–109 (a structured prior as realization datum is a further named premise) | Applied in §1 | §1 |
| m6 | 3A:501 and 3A:794–805 at `8228b3c2`; AF:125–197, P:439–469, OA1:563–564 on `main` | Applied: two §7 rows added | §7 |
| m7 | OA1:561 ("Main §4.6 supplies only selection (Main:742)"); Main:443–449 (mixing hypothesis), :742 | Applied in N3.5 | N3.5 |
| m8 | OA1:111 (φ-written settings), :183, :522 | Applied: node N0.4a added, not selected | N0.4a |
| m9 | P:143, :190 | Applied in NOTES-r2 item 6 | NOTES-r2 item 6 |
| m10 | S4:457 (NL-C uses no rule, law or carrier) | Applied in the (f) row | §2 (f) row |

**Other edits.** The revision line under the title; §6's list of comments read gains
c.6854774010 (read for R1); NOTES-r2 adds items 11 (gates of `m ≥ L` rounds open; the reviewer's
recovery sketch not attempted) and 12 (the μ-O / μ-R conditional route left open), both recording
open points R2 and R3 create. No other change.

**Limits.** Paper-only. No computation on any OI rule; `python3 -I` was used only for literal text
substitutions and for printing the GitHub API response. Nothing committed, pushed or posted.
