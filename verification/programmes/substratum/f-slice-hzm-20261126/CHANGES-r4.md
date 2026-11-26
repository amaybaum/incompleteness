# F-SLICE-HZM: changes from REPORT-r3.md (r3) to REPORT-r4.md (r4)

r3 is `REPORT-r3.md` at `89c496b98130ff821baf60a1268bc5ae0572c61f`, kept unchanged with r1 and r2. The review is the independent delta review of r3, posted verbatim on PR #1611, comment 7201639742 (posted from the account amaybaum, created 2026-11-26T19:29:04Z), verdict ACCEPT WITH NITS. The coordinator's instruction directed applying findings 1–4. Finding 5 reports no register finding and needs no change. All changes are textual: no derivation, witness or classification changes.

| Finding | Change in r4 |
| --- | --- |
| 1 (Low): ρ_T needs O to be the rotation group | §3.4 ρ_T's range now states that O is the cubic rotation group, of order 24. The "only h = id contributes" step gives its reason: with distinct nonzero absolute values, hk_0 = ±k_0 forces h = id, because −I is not a rotation. It notes that [A-rec] Proposition A's W uses the same assumption. It adds the O_h caveat: inversion sends Q to −Q and cancels 𝒲, so an O_h version needs an inversion-odd spatial factor, such as i(P_{k_0} − P_{−k_0}). The §13 row for ρ_T records the r3 delta review |
| 2 (Nit): the N-1 qualifier and the uncentred case | The R2 condition reads "if N-1 (extension) is admitted and any of N-2, N-8 or N-9 is taken as a premise". R3 gains the case "or if the uncentred reading is the only admitted reading of φ" (P2a OB, §6). Applied in §0, §8, §10 (N-1, N-2, N-8, N-9) and §13 |
| 3 (Nit): N-2's status | §8 gains a clause saying why LI is not counted as carried, although §3.3 identifies it with H6-Φ read on V_rest. [A-rec] states H6-Φ for the one-fibre reduced space of the H-ZM route. On the F-slice the stated premises do not fix whether "commuting with the update" refers to the deviation dynamics on V_rest or only to the pair of slices, which admits Proposition P's family |
| 4 (Nit): §13 uniform | The ρ_W row's Missing entry reads "independent non-model verification", resolved by "recorded review". The ρ_T row, now model-reviewed, takes the same entries |

Consequential edits:
- the header, the revision note and the r3 pin;
- §1's pass count;
- §9's Pass 7 (textual; no classification change);
- §10 N-7;
- §12's provenance rows: comment 7201639742 and commit `89c496b9`.
