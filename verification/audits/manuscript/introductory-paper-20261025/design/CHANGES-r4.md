# Changes in revision 4 of the paper design

**Applies:** `paper/review/RECHECK-r3.md` (BLOCK, wording only): RC-A and nits n-A to n-F.

**Kept unchanged:** revision 3 (sha256 prefixes: `OUTLINE-r3.md` `fc5b7d6057af7a67`, `CONTRIBUTION-r3.md` `3e9eb43a26e869b6`, `SOURCES-r3.md` `172e073900bd6331`, `CHANGES-r3.md` `9c01d69126429d8c`), together with revisions 1 and 2.

**New:** `OUTLINE-r4.md`, `CONTRIBUTION-r4.md`, `SOURCES-r4.md` and this file.

**Repository:** no file changed; the worktree is clean at `687e885b`. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.

**Verified at `687e885b` before applying:**
- **Main:286.** For $\varphi(x,h)=(h,x)$, $\Phi(\rho)=I/2$ identically: a constant channel.
- **Main:326.** Theorem: for the permutation-dilation family, P-indivisibility implies CP-indivisibility.
- **Main:334.** Notion (2), "Stochastic P-indivisibility", is the population notion.
- **Main:666.** The double-slit paragraph is interpretive. Its next sentence reads "The Everettian measure problem dissolves".
- **Main:702.** The swap realization has two-step maps $\rho\mapsto|0\rangle\langle0|$ and $\rho\mapsto\rho$, and "this swap realization admits no classical-memory decomposition".

## Required change

**RC-A.** Applied in three places, with the re-check's exact wording.

- **OUTLINE-r4 §5-h.** The scope sentence now reads:

  > Stated scope: on configuration (card) inputs the game is a classical stochastic process, and its P-indivisibility is the population notion (2) of Main:334. Under the permutation-unitary embedding (§3-d) the one-step channel is the constant, entanglement-breaking channel (Main:286), but the two-step map is the identity channel; the family is CP-indivisible (Main:326) and this swap realization admits no classical-memory decomposition (Main:702). A card arrangement violates no Bell inequality (ch01:286; Main §3.3).

- **CONTRIBUTION-r4 non-claim 13.** It now reads: "On card inputs its statistics are classical stochastic ones; its one-step channel is entanglement-breaking, though its two-step map under the unitary embedding is not (Main:286, :702); and it violates no Bell inequality (ch01:286)."

- **CONTRIBUTION-r4 item 8.** "its classical scope" becomes "its scope".

**Mirrored.** The SOURCES-r4 §5-h register row now carries the same scope and cites Main:326 and :334.

**Also added to §5-h.** The re-check's independent finding: a passive look with no replacement also gives odds of 1, so the 1/2 comes from the intervention on the record.

## Nits

| Nit | Applied |
|---|---|
| n-A | §5-h now says "with a burn card uniform and independent of the hole card. With anticorrelated cards (a two-card deck, $b_0 = 1-h_0$), $\Gamma_1$ is a permutation and the game is divisible." SOURCES-r4 §5-h repeats it. |
| n-B | The quantum-weirdness absorption candidate now cites Main:666 "only as interpretation, class (e) as in §1-a and §6-a, never as a result", and quotes its "dissolves" sentence as not carried. |
| n-C | Title lines now read "revision 4" in all three files. The header paragraphs are replaced by one history line pointing to CHANGES-r2, CHANGES-r3 and CHANGES-r4. Every cross-reference to an earlier revision now points to r4: the OUTLINE ones formerly at r3:141, :149 and :236; SOURCES' §8 line and decision 1 heading; CONTRIBUTION's header and its "SOURCES-r2, Kernel" and "OUTLINE-r3 §8-d" pointers. A grep finds no remaining `-r2`/`-r3` file reference other than CHANGES and RECHECK names. |
| n-D | Decision 1's mathematics list now reads "§5-b to §5-h". |
| n-E | Appendix A's alternative cut no longer names §9. It now reads "§8 to 0.75 pp and §7 to the BH-01-conflict-free variant, about 1.0 pp". §9 is recorded as the next section to give way, since it is tight at 0.5 pp (re-check §4). |
| n-F | Decision 1(a) option (ii) now reads "free of contradiction with the live corpus, though ch18:148 / FULL:4968 remains a conditions-level site against §7-i (R12)". |

## Not adopted

None.

## Owner decisions

The list is unchanged from revision 3. See SOURCES-r4.

1. Scope, with (a) the R11 sites to correct first or the two variants, and (b) the worked example.
2. Wording of the Lean-check claim. Retention is required in every case.
3. Provenance of the design inputs.
4. Census registration and anchors.
5. A separate check of GR:226's box.
6. Page format and the scope of Appendix A.
7. The Explainer: decided (replace). What remains is the retirement change and the content-migration audit.

**Flagged:** the title (R1). The ch01 §1.11 sites (R23) are a book matter.
