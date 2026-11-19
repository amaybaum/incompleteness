# Response to the re-review of RO1-SPEC-r2

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-SPEC-r2.md` (ACCEPT WITH CHANGES at
`551b2f18`, file SHA-256 `5ea19f79…3528`). The review raised three new major findings (N1–N3) and six
minor ones (N4, m1–m5). The changes are in `RO1-SPEC-r3.md`, a minimal revision.

`RO1-SPEC-r2.md` is left unchanged (SHA-256
`5ea19f790120499b4d6325459f8153d1c5fc831fee07877f4603cc5132fb3528`). Nothing outside these findings
changes.

Each finding was checked at source first. No finding was found to be wrong. Reading only: no
computation, no Lean, no edit, no post. Line numbers in the first column are r2's.

## Major

| Finding | Check at source | Disposition | Where in r3 |
|---|---|---|---|
| **N1.** l. 318 bars "any equivalent condition", which prejudges S9 and contradicts §7.4 | **Confirmed.** Main:584–588 proves the OI⁺ principles equivalent to exact finite endomorphic operational QM on every nonempty finite carrier. #1060 bars choosing C "by testing whether the resulting correlations match quantum predictions". #914 c.6883249235 item 1 bars "a premise merely to reproduce quantum predictions". Both bar a choice, not a logical equivalence | **Applied.** §6.1 now bars two things: adding quantum-set membership as a clause or an assumption, and adopting a clause *because* it yields membership. Justification is judged under §6.1 and §A.29. The OI⁺ question is left to S9. In §7.4, "come nearest" is replaced by a neutral statement of status and dependencies | §§6.1, 7.4 |
| **N2.** R*'s (b) and the parameter-independence step assume (xiv), open as S5; l. 463 contradicts (b) | **Confirmed.** The Bell ceiling needs hypothesis (iv), `p(Ω|a,b) = p(Ω)` (Main:372–374), while K-src deliberately excludes (xiv). Main:416–423: reaching the quantum value under measurement dependence needs `I_ont ≥ 0.0309` bits, "not claimed tight", and Main cites a causal construction at about 0.080 bits [57]. **Refinement:** the review says such a model "can reach" the quantum value. At source, Main gives a necessary bound and cites an external construction. r3 states exactly that | **Applied.** (b) now constrains only the record law (fair marginals, CHSH 2√2, a classical fragment), not the OI model's hidden source. The parameter-independence paragraph is stated as conditional on (xiv) (S5). A paragraph records that without (xiv) the measurement-dependent route stays open. The contradicting clause of l. 463 ("or on a source that depends on it") is removed. S5's row now names both uses | §7.3; §10 S5 |
| **N3.** The O11 answers "yes" under (i) and (ii) overstate the argument | **Confirmed.** Under (i), r2 itself expected the decisions to agree. Under (ii), its argument used record-equivalent lifts, while l. 181 fixed "physically equivalent" as relabelling, decoupled enlargement and change of alphabet (Main:724) | **Applied.** (i) and (ii) now read "not excluded", with the reasons and "no case of differing decisions is exhibited". Record-equivalent lifts are a separate, labelled case. S1's "Why" column is changed to agree | §2.3; §10 S1 |

## Minor

| Finding | Check at source | Disposition | Where in r3 |
|---|---|---|---|
| **N4.** §7.2's conditional has an antecedent the stated tuple cannot meet | Confirmed. `T(x,y,r,A,B) = (x,y,r, …)` leaves `x, y` unchanged (SEL-DISC-1 l. 63) | **Applied.** The conditional now concerns "an enlargement of the PR model … that executes these programs, if one exists". Its clauses are unchecked, and its construction is routed to #1143, with availability at #866 (r3 §4.5.2). The outcome paragraph and §7.3's opening are changed to match | Outcome; §§7.2, 7.3 |
| **m1.** R* is defined by its tests | Confirmed (r2 ll. 449–458 against l. 224) | **Applied.** K-X is stated first with its justification. (a)–(b) are now two necessary tests, which "test K-X; they do not define it". The justification requirement (§6.1, §A.29) comes first. No H-Bell or IC₂ choice is made | §7.3 |
| **m2.** `Θ` (f) has no OI-side criterion | Confirmed | **Applied.** (f) now records, as [A], that no criterion exists yet, and ties it to S5 and S7 | §6.3 |
| **m3.** OI⁺ row and E row overreach | Confirmed. On one carrier without `Θ`, a PR table is a classical channel. SEL-ACCESS-1 at `1b966a03` gives E's CHSH statement at l. 83 ("Under those explicit premises |CHSH| ≤ 2") and l. 90 ("it still obeys CHSH ≤ 2"), not at l. 81 | **Applied.** The OI⁺ inference now runs through `Θ` (a)–(b), and the one-carrier case is noted. The E row reads "obeys CHSH ≤ 2" and cites ll. 83, 90 | §7.4 |
| **m4.** Citations in §§2.1 and 2.3 | Confirmed. B4PRIME §3.5, l. 367: "G⇒O: disproved [D], every `|V| ≥ 2`, witness WE, in `PPer`". Main:588 supports non-entailment, not "no E is adopted" | **Applied.** The `G ⇒ O` citation is now l. 367, with the correct scope. The step from B4′'s `O_C` to relation (iii) is stated as [A-inf]. "No E is adopted" is cited to the #914 record, and Main:588 to non-entailment | §§2.1, 2.3 |
| **m5.** "Verdict of the check" conflicts with §7.1; citing §8 step 2 | Confirmed | **Applied.** It now reads "Outcome of the check", and the control is UNSOURCED "in the sense of §8 step 2" | §7.2 |

## Stops

The stops are unchanged in number: S1, S2, S3, S5, S6, S7, S8 and S9. S1 and S5 have revised "Why"
entries (N3, N2). No stop is resolved.
