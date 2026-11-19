# Response to the review of S3-U4 r1

**Review answered.** `REVIEW-S3-U4-r1.md` (blob `63c95b30`), on S3-U4 r1 (blob `e6d8101a`) at PR #1294
head `3a08a446`. The verdict was REVISE, with 13 findings.

**Revision.** `S3-U4-r2.md`. r1 is left unchanged.

**Writer:** Claude. This is a paper-only response with no computation. It makes no commit, and no
Issue is changed.

**New inputs used in r2:**
- `LIT-ERASER-r3` (blob `2b414173`, accepted), for every claim about performed experiments;
- `U4-CALC-r2` (blob `bef634e2`, at `213e3981`). Its mathematics was reviewed at r1 (ACCEPT WITH
  CHANGES); r2 applies that review and is not yet re-reviewed;
- owner records #1169 c.6891511297 (VER r2 accepted; items (2a), (2b) and (2c) authorized),
  c.6891710167 (three cases kept separate) and c.6891808569 (U4 r2 starts; it uses LIT-ERASER-r3).

Every finding is accepted. None is rejected.

| # | Finding | Disposition | Where in r2 |
|---|---|---|---|
| 1 | PK-4 / U4-F4 false: recovery from neighbours' reads keeps S-L7's restriction; only holding a conjugate pair breaks it, and it breaks without parking | **Accepted.** The review's bracket `(U_{k−1}(A))_{vw}` was re-derived by hand. PK-4 is withdrawn and restated: the restriction fails exactly when `V` holds a pair with nonzero bracket; recovering or retaining parked values does not by itself remove it; reading both slices under A-reg removes it with no parking. U4-F4 is reclassified, and the assumption-watch marker is restated as AW-U4-1. The computed pair governs, not S-L7's broader wording | §6.1 PK-4; §8 U4-F4 |
| 2 | QM-4 overstates `D² + V² ≤ 1` | **Accepted.** QM-4 is restated as the trade-off `V ≤ √(1 − D_whole²)`: equality for a pure complement, inequality for mixed markers (LIT §3; Schwindt [FULL]). `D_whole` and `D_acc` are kept apart. "Exclude each other" is false about states and true about processes under the equality (LIT C6). A record return raises `D_acc`, not `D_whole`. The comparison across ticks relies explicitly on QM-1's invariance. Englert 1996 is labelled [LIT: ABSTRACT, theory] | §6.2 QM-4; §6.3 |
| 3 | "Explanatory compatibility" misapplied: PK-2 with a quiet marker, given (γ), predicts fringes despite a stored record, against E-1 | **Accepted, and extended.** By CALC r2 Prop. 2.8(i), the tension also holds for the native marker where masking is incomplete (point-prepared carrier assumed). r2 reports: no distinguishing observable; no independent experimental support; compatibility not shown for the native K1 mechanism, as a potential raw-direct conflict undecided at (γ). The compatibility label applies only to the class-(ii) reading. Routed to the γ plan | §6.3; §8 U4-F8; §10 |
| 4 | Status inputs out of date: VER r2 accepted (c.6891511297); Sup-3 contradicts §2.2's μ-datum bullet | **Accepted.** All sites are updated: §2.2 (S-L3's four bullets [V]; Sup-1 and Sup-2 credited to the record; Sup-3 reflected, with the μ-datum bullet corrected); PK-1 cross-referenced to Sup-3 (U4-F10); SNR-1 standing in §4.2; the CC scopes in §6.4 taken from VER r2; r1's owner questions 2 and 3 removed as answered | §§2.2, 4.2, 4.3, 6.1, 6.4, 8, 10 |
| 5 | U4-F2 conflates conditional decoding with unconditional restoration | **Accepted.** §4.2 now has two routes. Route 1 is unconditional restoration at `D` (Case Rv), with CALC Prop. 2.8 and Theorem 2. Route 2 is conditional recovery through a retained copy, the OAC identity, which is Case S and outside the branch. "Does not count" is marked as a U4 finding against PLAN §8.6, pending owner question 3 | §4.2; §8 U4-F2 |
| 6 | The accessibility reading is defined inconsistently with its prediction | **Accepted.** Two readings are defined: AV-p (retrievable in principle), which coincides with QM; and AV-t (held at the recombination tick, in G4's sense), which predicts fringes while unheld. AV-t is tested against Schwindt 1999 [FULL, non-delayed], not against the delayed-choice data, which report no unsorted pattern. The classification of an unanalysed degree of freedom is put to the owner | §6.3; §10 owner question 2 |
| 7 | §6.4 generalizes from two toy controls | **Accepted.** The statement is restricted to Case S, T4-type conditional-fringe recovery, at VER r2's scopes. W1-type behaviour is stated as not addressed | §6.4 |
| 8 | §5 mixes performed experiments, proposals, theory and reviews | **Accepted.** §5 is rebuilt from LIT by the three cases, with each source typed and given its LIT read status. Case Pk is restricted to Kim 2000, Walborn 2002 (delayed erasure) and Ma 2013, with LIT's point that access consumes the record. The two raw-direct checks (singles against summed coincidences; sums only with full masses) are carried forward | §5; §8 U4-F6 |
| 9 | The C/Q sentence needs the performed-Bell-data condition | **Accepted.** A C that yields PR statistics is a prediction only for unperformed configurations, and only if its predictions for performed Bell experiments match the data; otherwise it is a raw-direct miss | §7 |
| 10 | Tier stated favourably | **Accepted.** "Weaker tier not reached; definitional and conditional groundwork recorded" | §10 |
| 11 | PK-2 and §4.2 wording should follow C-9 | **Accepted.** r2 uses "content that is not a function of the carrier's content", and notes that a `μ` correlating non-carrier content with the carrier is not covered without a check | §§2.1, 6.1 PK-2 |
| 12 | Masking is complete at `t = 1` | **Accepted, superseded by CALC.** Proposition 1.4 proves completeness at `t ≤ 1` in every geometry. Theorem 1 gives the exact condition `K_t = R_A` at `t ≥ 2`, which fails in Instances 1.1 and 1.2. "(β) generically fails" holds only where masking is complete | §3.2; §8 U4-F1 |
| 13 | Provenance and minor items | **Accepted.** (a) The owner refinement is quoted as relayed; a REST search of #1169 found no comment carrying it, which is stated. (b) Inputs are re-pinned to `b547c9f2`, with CALC r2 at `213e3981`. (c) R-c and R-b are replaced by named processes, "record return" and "coherence revival". (d) QM-5's second sentence is marked as a class-(ii) inference, not [M]. (e) The D–V observable is a joint statistic over runs at one tick. (f) The ch18:78 quotation carries its continuation, and ch15:156's `𝓕(r)` status is cited. (g) PK-1 is scoped to same-site slice parking | header; §§6.1–6.3 |

**Coordinator inputs, applied.**
- *LIT-ERASER-r3.* The following are taken from LIT and labelled there:
  - recovered fringes are coincidence data sorted by marker outcome (C2);
  - "no fringes while parked" and "whatever the later choice" are QM predictions, not measurements
    (C2, C4);
  - no reversal-type eraser was found among the papers read (C8);
  - equality for pure markers and inequality for mixed ones; "exclude each other" is false for states
    and true for processes (§3, C6).
- *U4-CALC-r2.* r2 is cited instead of r1, with its status. These statements are used as r2 gives them:
  - CALC-F2;
  - Theorem 2 with `d = 3` (Prop. 2.5(b)) and a prime-power `q` for the A-cur ticks;
  - Theorem 2(c) given S-L2 [NP], while (a), (b) and (d) do not use it;
  - Theorem 2(b) limited to the §5.3-equivalence part of T3;
  - the `ℤ/6` countercontrol, in which only the algebraic step fails and extra ticks are left open
    (R-3);
  - rings excluded by Prop. 2.5(c);
  - CALC-F5 as ELABORATING.

  D-1 stays undecided at (γ), and nothing counts under SNR-1.
- *Three cases* (c.6891710167). Sorting (Case S), reversal (Case Rv) and the parked record (Case Pk) are
  defined in the header and kept apart in §§4.2, 5, 6 and 10. No experiment of one case is used for
  another.

**Unchanged.** r2 remains paper-only and adopts no new premise. The C/Q target and AC-1, SNR-1 and the
gating stay as before, and route M stays open. The text rules were checked by grep on the output.
