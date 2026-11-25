# #1049 report: changes from r4 to r5

**Basis.** Owner decision (amaybaum, 2026-11-25T16:29:44Z, #1169 comment 7169907126): "Authorize the final bounded text-only revisions for all three packages, and add the superseded notices."; "#1049 — Linearity | Resolve nits 1–6. Add the superseded notice to REPORT-r3.md."; "Resolve the identified findings directly. Preserve the necessary supporting evidence and provenance."; "Earlier revisions should carry a short superseded notice identifying the authoritative report. No elaborate historical annotation is needed."; "Correct genuine errors and satisfy existing requirements, but do not turn minor editorial preferences into additional revision cycles."

**Input.** REPORT-r4.md at `46e82783ad2f33e3ce956e3189ad9c54ca541bab`, and the bounded delta review of r4 (nits 1–6; nit 7 was put to the owner and is resolved by the notice on REPORT-r3.md). Manuscript and record pin unchanged: `main` = `e2e2a623265187a28ebec604ab8bcc672742888f`.

**Scope.** Only the changes below were made. Every other line of REPORT-r4.md is carried into REPORT-r5.md byte for byte. No mathematical result changes. C4, C7 (second part) and C9 are consequences of r5 itself and of the new notices. The paragraph "Support checked at the pin" of CHANGES-r4.md lists B0.3(a)–(e), Proposition 2.5 and Q4 N0, N1, which C5 now places under V-1.

***

## C1. §0, new line "Revision r5" (owner decision)

- Old: (none)
- New:

> **Revision r5.** Revision r5 applies the owner decision "#1049 — Linearity | Resolve nits 1–6. Add the superseded notice to REPORT-r3.md." (amaybaum, 2026-11-25T16:29:44Z, #1169 comment 7169907126), resolving nits 1–6 of the delta review of r4. The edited passages are §0 (this line), §1.4 (one clause of the second Q-β bullet), §7.3 (the r3 and r4 lines), §7.6 (V-1 and V-2), §7.7 and §7.8 (three rows, one of them new). No result changes. CHANGES-r5.md lists each change.

## C2. §1.4, second Q-β bullet, last clause (nit 5)

- Old:

> is removed off the locus by the static uniform shift to the fixed point and is not removed on it (Q4 N1).

- New:

> is removed off the locus by the static uniform shift to the fixed point, as a relabelling (owner Q2), and is not removed on it (Q4 N1, (L) and (A-aff) off-resonance branches; [D]+[W]).

## C3. §7.3, r3 line (nit 1)

- Old:

> - r3 (REPORT-r3.md, commit `389d6ea46a2bac11f257acd78536a982a5b2c15d`): delta review on PR #1561, verdict ACCEPT.

- New:

> - r3 (REPORT-r3.md, commit `389d6ea46a2bac11f257acd78536a982a5b2c15d`): delta review, PR #1561 comment 7169919290, verdict ACCEPT.

## C4. §7.3, r4 line (consequence of r5: the review it described as not yet made has been made)

- Old:

> - r4: a bounded independent review of the r4 changes is required by the owner's decision (§7.9) and has not yet been made.

- New:

> - r4 (REPORT-r4.md, commit `46e82783ad2f33e3ce956e3189ad9c54ca541bab`): bounded delta review, as the owner's decision requires (§7.9); it is not yet recorded on GitHub, and its verdict is not stated here. Its nits 1–6 are applied in r5.

## C5. §7.6, V-1 (nit 3)

- Old:

> | V-1. A5-LA R2, R3, R6, R7 and Proposition 2.6(c), on which §§2.2–2.3 and the narrowed §1.4 rest | [D], model-reviewed | exact finite controls, or an independent non-model mathematical review | #1049 | A5-LA §7's exact controls run under a separate owner authorization (CI-scale), with green controls; or a recorded independent review |

- New:

> | V-1. A5-LA R2, R3, R6, R7, Proposition 2.6(c), B0.3(a), (c), (d), (e) and Proposition 2.5, and Q4 N0, N1 and outcome (iii), on which §§2.2–2.3, the narrowed §1.4 and §3 rest | [D], model-reviewed | exact finite controls, or an independent non-model mathematical review | #1049 | A5-LA §7's exact controls run under a separate owner authorization (CI-scale), with green controls, for R2, R3, R6, R7 and Proposition 2.6(c); exact controls for B0.3, Proposition 2.5 and Q4 N0, N1 and outcome (iii), which A5-LA §7 does not cover; or a recorded independent review |

## C6. §7.6, V-2 (nit 4)

- Old:

> landing #1226 is not the route (owner decision, §7.9) |

- New:

> landing #1226 solely to resolve this dependency is not authorized (owner decision, §7.9) |

## C7. §7.7 (nit 6; and the superseded notices on REPORT-r3.md and REPORT-r4.md)

- Old:

> Its negative findings are kept with the same care as its positive ones (§A.29). Preservation establishes no claim (§A.46 item 1). REPORT.md (r1) and REPORT-r2.md are kept with superseded notices as the research history, and REPORT-r3.md as the reviewed revision r4 corrects; this revision, REPORT-r4.md, is authoritative, and CHANGES-r2.md, CHANGES-r3.md and CHANGES-r4.md record the corrections.

- New:

> Preservation establishes no claim (§A.46 item 1). REPORT.md (r1), REPORT-r2.md, REPORT-r3.md and REPORT-r4.md are kept with superseded notices as the research history; this revision, REPORT-r5.md, is authoritative, and CHANGES-r2.md, CHANGES-r3.md, CHANGES-r4.md and CHANGES-r5.md record the corrections.

## C8. §7.8, review row (nit 1)

- Old:

> | PR #1561 comments 7166779576 and 7167108875, and the r3 delta review on PR #1561 | §0, §7.3 |

- New:

> | PR #1561 comments 7166779576 and 7167108875, the r3 delta review (PR #1561 comment 7169919290) and the r4 delta review (not yet recorded on GitHub) | §0, §7.3 |

## C9. §7.8, owner-decision row (the r5 authority record)

- Old:

> | #1169 comments 7166418469, 7166845267 (the owner decision applied in r2), 7167242160 and 7167657546 |

- New:

> | #1169 comments 7166418469, 7166845267 (the owner decision applied in r2), 7167242160, 7167657546 and 7169907126 |

## C10. §7.8, new row before the last row (nit 2)

- Old:

> (none)

- New:

> | commits `8aef91cf`, `0c058645`, `389d6ea4`, `46e82783` (reviewed revision heads, PR #1561 branch) | §7.3 | provenance |

## C11. Superseded notices

REPORT-r3.md and REPORT-r4.md each gain one prepended paragraph followed by a blank line, in the form of the notices on REPORT.md and REPORT-r2.md; nothing else in either file changes. In the notices on REPORT.md and REPORT-r2.md the authoritative revision and its correction record are changed from r4 to r5, and CHANGES-r4.md is added to the earlier corrections.

- Old (REPORT.md and REPORT-r2.md):

> The authoritative revision is REPORT-r4.md in this directory, and its correction record is CHANGES-r4.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2) and CHANGES-r3.md (r2 to r3).

- New (all four files):

> The authoritative revision is REPORT-r5.md in this directory, and its correction record is CHANGES-r5.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2), CHANGES-r3.md (r2 to r3) and CHANGES-r4.md (r3 to r4).

- REPORT-r3.md, new first paragraph:

> **Superseded; kept as research history.** This file is revision r3 of the #1049 report and is superseded. The authoritative revision is REPORT-r5.md in this directory, and its correction record is CHANGES-r5.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2), CHANGES-r3.md (r2 to r3) and CHANGES-r4.md (r3 to r4). Below this notice the text of r3 is unchanged. It is kept as the research history, and its conclusions are not current results.

- REPORT-r4.md, new first paragraph:

> **Superseded; kept as research history.** This file is revision r4 of the #1049 report and is superseded. The authoritative revision is REPORT-r5.md in this directory, and its correction record is CHANGES-r5.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2), CHANGES-r3.md (r2 to r3) and CHANGES-r4.md (r3 to r4). Below this notice the text of r4 is unchanged. It is kept as the research history, and its conclusions are not current results.
