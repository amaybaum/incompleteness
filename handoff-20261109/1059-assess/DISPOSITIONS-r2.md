# ASSESS-1059 r2: dispositions of REVIEW-1059

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Maps each finding of
`review/REVIEW-1059.md` (sha256 `8cbfe2271d0ea7ff8650637645d6151704a74faf2ab6475e6c5a786f0c1b7446`,
REVISE) to its change in `ASSESS-1059.md` r2, from r1 = `r1/ASSESS-1059.md`
(`d5b314af26c2f9474b81bc2778c46bb6a558bcf012e2f803f43635af9e2fd931`). Every finding was checked
against its source at `fd539e15` (or the cited draft) before it was applied. No finding was
refused.

| Finding | Verified against | Disposition | Change in r2 |
|---|---|---|---|
| B1 (R2 "unselectable" too wide) | EQ:99 `sum_chain`, EQ:147, EQ:302 `hborn` 0/1 | Accepted. $Q_{\rm fb}^p\subseteq S$ is immediate from the normalisation restriction and $S\subseteq D\subseteq Q_{\rm fb}^p$ from 0/1 weights; the column lemma is not needed for R2 | R2 row: support and conclusion replaced by the review's wording ("realizable law class does not depend on $p$ … selection must come from a constraint on admissible operations"), conditional on the normalisation restriction. Column-lemma paragraph re-scoped to R3-C ("R2 does not use this lemma"). §3 "Answer to Q1" closing paragraph rewritten (no "unselectable") |
| B2(i) (renormalised reading) | rv C3; r2 K4 (own check) | Accepted | §1 H-RF$_p$: "unrenormalised values … $\sum_j|{\rm amp}_j|^p=1$ required on every read"; renormalised reading excluded, citing K4 |
| B2(ii) (preparation class) | rv C4; r2 K5 | Accepted | §1 H-LIN states the preparation class; §3 "R3-N, preparations included" paragraph adds the supplied 2-normalised counterexample |
| B2(iii) (status of H-LIN, H-RF$_p$) | BORN-SRC-1 review 9(i) as quoted in r1 §1; Main:20, Main:218, Main:226, Main:288 | Accepted | §1: both labelled *posited*, H-RF$_p$ open as a sourcing question. R3 column (ii) no longer says "supplied". §4.5 (a-pow) row lists H-LIN and H-RF$_p$ as prerequisites; §0 item 2 and OQ-1 rewritten |
| B2(iv) (read basis) | r1 §4.1 gap 2 | Accepted, extended | R3-N/R3-C antecedents are stated "in the read basis"; FI-1's carrier stated as the configuration carrier at level one (BRIDGE r3). Extended by the non-unitary scope (untraced change U1) |
| B3 (stabilizer claim scoped to (a-gen)) | rv C2; r2 K5 | Accepted | §0 item 3 third bullet, §4.3 second and third bullets: scoped to (a-gen); power-family case stated (dyadic point $2^{-1/2}$ forces $p=2$ under H-RF$_p$); the "does not bear on (a)" reason is the N2 bullet. §0 item 5: "(a-gen) and (d)" |
| B4 (F-d stale) | `git show fd539e15:papers/Main.md` lines 20, 226, 351, 556; `484006b1` (2026-11-07) is an ancestor of `fd539e15`; `book/ch18-beyond.md:34` cites "[Main §3.1]" | Accepted | §6 F-d rewritten as "BORN-SRC-1 F1/F2 overtaken by `484006b1`", quoting the current Main:226 and Main:351; Main:648 kept as O2 candidate |
| B5 (R9 column (ii)) | Main:726 (iv) | Accepted | R9 column (ii): "no: posit (iv), not derived (Main:726)"; §1 adds "A posit is not a column-(ii) 'yes'" |
| N1 (R3 direction labels; define (a-pow)) | §A.34 | Accepted, superseded in form | R3 split into R3-N and R3-C rows, each named by its antecedent; no ⟺ display remains. (a-pow) is defined in §4.5 and §4.4 by its necessary conditions (the review's definition, "under H-LIN ∧ H-RF$_p$, the admissible operations' records force $p=2$", is R3-C's conclusion) |
| N2 (SHM is r5) | first line of `qphen/SHARED-MECHANISM.md` ("draft r5"); `qphen/r4/SHARED-MECHANISM.md` = `23ec1ef1…fd11` | Accepted | Header: SHM cited as r5 `a7206701…cc4d`, with the r4 hash and "the N2 row reads the same in both"; §6 F-a heading |
| N3 (F-c blob wording) | `git rev-parse 8e764171:<T3>` = `b31d0549…`, `fd539e15:<T3>` = `1c077f62…`; `git diff` shows the author-label line only; `23150480` is not an ancestor of `fd539e15` | Accepted | §6 F-c: "same content apart from the author-label line"; `23150480` reference removed |
| N4 (P2 scope; $f\ge0$) | P2 header; rv C5; r2 K6 (own check, interval arithmetic) | Accepted | §4.3: P2 scoped to $n\le3$; all-$n$ statement via $g(u)=u^2(1+\sin^2(\pi\log_2u^2))$; nonnegativity of $f$ stated as immediate from the construction |
| N5 ((d) row cites P2) | rv C6 code read; rv script re-run with `python3 -I`, output byte-identical | Accepted | §4.5 (d) row: stabilizer-scope Gleason route fixes the trace form and fails at state positivity and (d1) covering; labelled as the reviewer's check, generic, two-qubit only, nonnegativity step numeric at 30 digits |
| N6 ("(St)" undefined) | r1 §1 | Accepted | R1 column (ii): "(St)" replaced by "(EQ:205)" |
| N7 (F-a label) | Main:56 Lemma 3; review's citation of `ensembleDetermined_of_transitive` | Accepted | §6 F-a: per-cycle uniqueness stated; suggestion now "posit (Op) for the global selection". §2 (b) bullet adds the per-cycle clause |
| N8 (§A.19 sweep) | Main:684; `book/ch18-beyond.md`:16, :34; `book/glossary.md:21` | Accepted | §8 search bullet names Main:684, ch18 §18.2 and glossary:21 as non-selecting. The glossary line also contradicts Main:20/:226 (exponent named a frontier item); recorded as new finding §6 F-e (untraced change U5) |

## Cross-unit and owner-direction changes

| Source | Change in r2 |
|---|---|
| Coordinator, cross-unit: FI-1 cited as a necessary condition for exact finite endomorphic operational QM on the configuration carrier; never earliest or only; drop "downstream" framing (#1059 B2(iv)) | §0 item 2 (FI-1 paragraph, `obligations_independent` C5Discovery.lean:59, H-Bell third gap); §3 "FI-1 and R3"; §4.2 new "Relation to FI-1" bullet; §4.4 retitled and rewritten (r1's "(a) downstream of #1211's FI-1" removed); §5 *No* branch (r1's "planned as downstream of #1211" removed); BRIDGE cited at r3 `a5d7aad1…78c1` with REVIEW-UNIT1-r2 `3cdf7dc2…4eb3` |
| Owner direction 2026-11-09 (#1059): state mixing necessary, not sufficient for the exponent or the law | §0 item 2 rewritten under that heading; R3-C column (ii) and §4.4 first bullet ("forced by the posited form … not a derivation"); §4.4 "The law" bullet; §4.5 (a-pow) row; §5 *Yes* branch; OQ-1 |
| Owner direction (all units): three distinctions | §1 new "Three distinctions kept apart"; §3 encoded-carrier bullet; §4.1 gap 1 retitled "Mathematical availability versus derivation" and closing sentence on the law; §4.3 "The route's carrier is an encoded one"; §5 NQ-1059 on the configuration carrier, positive branch requires derivation and executability, scope guard adds encoded carriers |

## Untraced changes (not from a review finding)

- **U1. Unitary scope of R3 (necessity, conditional forcing).** BRIDGE r3 §5.1 [D] distinguishes
  non-monomial from state-mixing for Kraus operators, and its *Position* (d) shows a weighted monomial
  Kraus family normalised only at $p=2$. Checked here independently (r2 K1, K2, K3). Consequences in r2:
  H-LIN requires unitary operations; R3-N's scope note; "FI-1 does not entail R3-C's antecedent"
  ($K=\begin{pmatrix}1&1\\0&0\end{pmatrix}$). This is what makes "FI-1 necessary, not sufficient"
  exact rather than a wording change.
- **U2. Anchor for "Born form posited".** r1 cited Main:580 for "OI supplies rather than sources".
  Main:580 is the QM→OI simulator's proof, which computes $q_o={\rm Tr}\,\mathcal I_o(\tilde\rho)$;
  it shows the rule as an input there and is a weak anchor. r2 anchors the status on Main:20,
  Main:226 and Main:288 and on BORN-SRC-1 review 9(i), and drops Main:580.
- **U3. R3-N antecedent anchored on GR:260** ("The interventions of the substratum so stated have
  monomial observable operators").
- **U4. H-Bell independence of FI-1** (§4.2 bullet), from BRIDGE r3 *Position* (c) [D] and
  Main:403–406, Main:566, Main:584.
- **U5. New finding F-e** (glossary:21 versus Main:20/:226), found while doing N8.
- **U6. Header and §8** updated for r2: revision line, owner-direction note, r2 probe, reviewer-script
  re-run, new reads.

## Probe added

`probes/r2_fi1_scope.py` (sha256 `3f32e79f6dc8b9c569718556ddc05dc7a119f15b49e865b5af0636c4c1521091`),
output `probes/r2_fi1_scope.out` (`bbe270c0b7d8a2ead85423bb7b35dacc654013b2eb29627e44f0a0ed05853e70`),
exit 0. Exact generic checks K1–K6 (K6's inequality by mpmath interval arithmetic). Imports no
earlier probe and computes nothing on an OI mechanism. The first run failed with a sympy
`NotImplementedError` on the mixed-base equation in K4; K4 was rewritten as an exact monotonicity
argument (positive sum of decreasing exponentials, $h(2)=1$) before the recorded run.
