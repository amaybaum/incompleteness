# Recheck of GAUGE-A1-TRACE r2 against REVIEW-GAUGE-A1-TRACE-r1

**Status.** This is a paper-only recheck. No repository file was edited, committed or pushed, no GitHub record was written, and no Lean build or computation was run. All `file:line` references are to `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`.

**Verdict: CONFIRMED WITH NITS.** All 15 review findings are applied at the locations r2 gives, and both of the writer's refinements were checked against the source. The revised headline and bottom line make no claim beyond the evidence, with one exception: the sentence "each proof was read" (N4). Four nits remain. None of them reverses a classification or strengthens a claim.

***

## 1. Findings applied

| Finding | r2 location | Applied correctly? | Note |
|---|---|---|---|
| B1 | §0 (no kernel sentence); summary row 2(d) Theorem 5; §1.3 (d); §3 pass 2; §4.3 | yes | The (N) basis is now the content of the proof. The kernel is described exactly; `A6Instantiation.lean:64–67` was checked and carries the "neither consumed nor judged" sentence. The layer contradiction is recorded. The condensate state is listed as a premise. |
| B1 refinement | §1.3 (d) | yes, correct | Sub:294 says "*Level 2 (emergent QFT):* SU(3)×SU(2)×U(1) is the gauge group acting on the emergent fields". Sub:298 says "a map from $\mathcal{G}_{\text{sub}}$ onto the Standard Model gauge group are not established". So Substratum's own gauge hierarchy places the group at observer level, against SM:428 and :511. The refinement strengthens the record of the contradiction. |
| R1 | §0; §1.3 (b); §3 pass 5; (T-def) class | yes | The full sentence of SM:222 is now quoted. Theorem 1a, Lemma 1c and Corollary 1b (SM:242, :252, :270) are traced. |
| R1 refinement (SM:569) | §1.3 (b), "Not counted here" | partly; see N1 | The algebra of the Schur complement `K_eff = D_eo G_oo D_oe` uses no finiteness of `S`. That part is correct. But the operator it acts on is not separate from the branch, as r2 says. |
| R2 | §2; §3 condition 2 | yes | Main:728 (xiii) is quoted as "a posit of the selected lattice model, not derived and not an axiom of OI". The exclusion is called posited. SM §2.4 is set aside as entailing A1. On "excluded by A4 itself", see N2. |
| R3 | rows for Sub:94 (T-just) and Sub:110 (V); §1.1; §1.5; §0 counts | yes | The counts now agree with the table: five (T) uses in the chain, plus (T-just) and (T-def); the uses outside the chain are listed separately. |
| R4 | §0 bullet 5; §1.3 (a); §3 Answer | yes | The `Z^d` claims carry [IR]. The continuum step on `G_N` is cited at SM:150 (its proof, part (iii), mesoscopic Ollivier curvature) and SM:152 (the contamination diagnostic). |
| R5 | §4.2 (b), (c) | yes | |
| r1 | §1.7 | yes | ch04-methodology.md:116 and FULL:1224 were re-checked and are identical. |
| r2 | §1.3 (e) | yes | |
| r3 | §1.2; table row "partly written" | yes | |
| r4 | §1.5 | yes | The Sub:104 sentence is removed. |
| r5 | §1.3 (b) | yes | |
| r6 | §1.3 (d) | yes | |
| r7 | §1.3 (a) | yes | GR:422–426 hold the ρ_s computation and its cancellation. |
| r8 | §4.1, §4.2 | yes | Now against changemap r3. Its U-21 row is unchanged from r2, and OQ-6 is present (r3 line 635). |
| r9 and the folded Prop. 9.5 point | §1.3 (f); §1.6; §4.4 | yes | |

***

## 2. Headline and bottom line

- **"No written proof step of Stage 2 (a)–(e) uses total finiteness of `S`."** This is accurate as qualified. The qualifications are:
  - (T-def): the observer-level branch is constructed only for finite `S`;
  - A4 as written, together with (viii) and (xiii), makes `S` finite;
  - validity on `Z^d` is [IR].

  r2 states all three in §0 and in the §3 Answer.
- **The five (T) uses plus Sub:94 are complete for Theorem 23's chain.** I found no further use:
  - Lemma 23.0's `G_sub` sentence is not needed for the invariants [IR].
  - The GR §5 import that E7 carries is not needed for the ratio.
  - Theorems 2 and 13 sit on the branch and so are (T-def), not (T). See N1.
- **N4.** §0 bullet 1 says "Each proof was read". §5 says §4.7.1.2 was not read and r2 relied on the review for it. Make the sentence say so: "Each proof was read, §4.7.1.2 through the independent review."

***

## 3. Owner questions

- **4.1.** Genuine. The options are correct, and the recommendation (a now, b with U-A4 or P12) is sound and agrees with OQ-6 (a). For the wording of (a), see N2.
- **4.2.** Genuine, and it now agrees with R5 and OQ-6. The recommendation (a now, b later) is sound. "(b) adds posited observer-level data but no probability premise" is correct.
- **4.3.** Genuine, and the three findings are correctly identified as matters outside A1:
  1. the inheritance of mixing and M1 (Sub:129);
  2. the identification of the M1-T dilation with the lattice, which is not written (§1.2);
  3. the layer contradiction: SM:312, SM:340 and Sub:294 against SM:428 and SM:511.

  One Issue is permissible, but see N3.
- **4.4.** Genuine. The recommendation is now labelled as sequencing only. It is sound.

***

## 4. Nits

**N1. SM:569 refinement and summary row 2(e).**

- *Problem.* `K_eff` is built from `D_st`, the staggered operator of Theorem 2. Theorem 2 is stated "On the observer-level lattice-wave branch of Theorem 1", and Theorem 1 holds "If the scalar observer-level branch satisfies Corollary 1b". So "It is not Corollary 1b's branch" is inaccurate: only the algebra of the Schur complement is free of finite `S`. Also, the summary row for 2(e) reads "L / N", while §0 and §3 say that (d)–(e) are stated on the branch.
- *Fix.* Replace the sentence with: "Its momentum-space algebra uses no finiteness of `S`; the operator it acts on is Theorem 2's, on Theorem 1's branch (Corollary 1b), so it is (T-def) like the rest of (e)." Change row 2(e) to "L / N; T-def through the branch".

**N2. "Excluded by A4 itself" (§2) and "A4 entails finiteness" (§4.1 (a)).**

- *Problem.* A4 alone excludes only a continuum of sites. Continuous field values are excluded by (xiii), or by the `Z_q` alphabets. Changemap r3 OQ-6 itself says "A2–A6 with $\mathbb{Z}_q$ alphabets entail $\lvert S\rvert<\infty$".
- *Fix.* Write "by A4 with the finite alphabet of (xiii)" in both places.

**N3. The Issue proposed in §4.3.**

- *Problem.* Under §A.45, an Issue that carries several obligations lists them as rows of one table, each with its own identifier and attributes (rule 4), with one accountable Issue per obligation (rule 6). Existing Issues should be searched first, because the M1 or H-Bell threads may already hold item 2 or 3. "No status changes before that Issue's own review" also implies that an Issue confers status, which rule 1 forbids.
- *Fix.* Add "as three rows with their own identifiers, after checking for an existing accountable Issue". Replace the status sentence with "Opening the Issue changes no status (§A.45 rules 1–2)."

**N4.** The wording of §0 bullet 1, as given in §2 above.

***

## 5. New errors

No new error beyond N1–N4. These r2 statements were spot-checked and hold:

- Sub:288, :294 and :298;
- SM:150, :152, :276 and :569;
- `A6Instantiation.lean:64–67`, :484 and :565;
- GR:422–426;
- changemap r3 lines 30, 188–189, 201 and 635.

## What was not checked

- Changemap r3 beyond the rows cited.
- EF-1 r7.
- Candidates P6, P7, P11 and P13.
- Main §2.3 and §3.4 proofs.
