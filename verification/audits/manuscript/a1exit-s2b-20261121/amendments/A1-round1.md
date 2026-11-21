# S2-B amendment A1: round-1 review answers

**Trigger.** Independent review of `91e1052d3`, round 1, REVISE (record on
[PR #1473](https://github.com/amaybaum/incompleteness/pull/1473); mathematics confirmed), and the
coordinator's instructions relaying it: B1, B2, nits N1, N2, N3, N6; N4 and N5 skipped (N5 out of scope);
return-form wording aligned with S2-C (#1474). Authorization unchanged: owner `amaybaum`,
[#1169 comment 7056875845](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7056875845);
B2 falls under authorized R6 §7 item #12 ("classical form"), proved in R6 T9(b).

**Edits.** Ten manuscript edits (R1–R6 below; 11 file sites), preregistered here before they are
applied; line numbers at `91e1052d3`. Old strings are checked unique in each file. Plus N6, a
`verification/coverage/LEDGER.json` delta note on the two §3.4 entries
(MAIN:T-c2-necessity-quantitative-mixing-form, MAIN:T-physical-memory-c2-process-form):
`"delta": "no Lean statement"` → `"delta": "no Lean statement; measurable form: paper proof only"`.

**Mirrors.** R2d is the ch02:144 = FULL:774 mirror of R2a; R6 edits AppB:92 = FULL:5769. Str:53 does
not restate the classical case and is not edited. R1 sits at M:224, inside S2-C's range (:131–:224);
it touches only the final clause of that sentence, as the coordinator assigned it here.

## Edits

### R1 — B1

Sites (at `91e1052d3`): `papers/Main.md:224`

Finding: Review B1 (§A.25): the list of results that take a measurable hidden space omitted the results E2, E8 and E9 put on measurable carriers.

Old (unique in each file):

```text
the near-return corollary of §2.3, the index-free form of §2.3 under (FS) and (NR), and the remark of §3.2 under the condition (IP) take a measurable hidden space.
```

New:

```text
the near-return corollary of §2.3, the index-free form of §2.3 under (FS) and (NR), the remark of §3.2 under the condition (IP), the measurable-carrier corollary of §3.2 and the two coupling-step theorems of §3.4 (the quantitative C2 theorem and the physical-memory theorem) take a measurable hidden space.
```

### R2a — B2 (#12 classical form)

Sites (at `91e1052d3`): `papers/Substratum.md:262`

Finding: Review B2: Main item (ii) (E6a) states that a classical factor leaves every reduced visible channel unchanged; R6 T9(b) proves the mixture-family identity, which Theorem 24(iii) did not print.

Old (unique in each file):

```text
The rooted population laws are likewise unchanged for a classical factor: a measurable space $A$ with a probability $\alpha$, prepared independently and evolved by any measurable map $w$, with product dynamics $\varphi\times w$ and the uniform hidden prior times $\alpha$.
```

New:

```text
The rooted population laws, and the hidden-prior channel family of [Main §3.2] (Corollary, measurable hidden carrier), are likewise unchanged for a classical factor: a measurable space $A$ with a probability $\alpha$, prepared independently and evolved by any measurable map $w$, with product dynamics $\varphi\times w$ and the uniform hidden prior times $\alpha$; on the original carrier that family is the coherent family $\Phi_t$.
```

### R2b — B2 (#12 classical form)

Sites (at `91e1052d3`): `papers/Substratum.md:266`

Finding: Review B2: proof line for the mixture-family identity (R6 T9(b)).

Old (unique in each file):

```text
For a classical factor the visible coordinate of $(\varphi\times w)^t$ does not depend on the factor's coordinate, so each rooted event is its $\mathcal C_H$-section times $A$, of weight $\alpha(A)=1$ times the original.
```

New:

```text
For a classical factor $(\varphi\times w)^t(v,(h,a))=(\varphi^t(v,h),w^t a)$, so the visible coordinate and the hidden coincidences of the original coordinates do not depend on $a$; each rooted event, and each set of hidden points on which that family's integrand is constant, is its $\mathcal C_H$-section times $A$, of weight $\alpha(A)=1$ times the original, which proves both identities; on the original carrier the family is $\Phi_t$ by part (a) of that Corollary.
```

### R2c — B2 (consequence)

Sites (at `91e1052d3`): `papers/Substratum.md:268`

Finding: Review B2: with R2a the transfer for a classical factor covers the channel family, read as the hidden-prior family.

Old (unique in each file):

```text
(for a classical factor, its $T_{ij}(t)$ restriction)
```

New:

```text
(for a classical factor, read as the hidden-prior channel family of [Main §3.2])
```

### R2d — B2 (mirror)

Sites (at `91e1052d3`): `book/ch02-substratum.md:144`, `book/The-Incompleteness-of-Observation-FULL.md:774`

Finding: Review B2: mirror of R2a in the chapter restatement.

Old (unique in each file):

```text
A classical factor with a probability law and any measurable dynamics likewise preserves every rooted population law.
```

New:

```text
A classical factor with a probability law and any measurable dynamics likewise preserves the channel family, read as the mixture over hidden points of [Main §3.2], and every rooted population law.
```

### R3 — N1

Sites (at `91e1052d3`): `papers/Main.md:60`

Finding: Review N1: the reason rests on factorization and normalization, not on a classical coordinate.

Old (unique in each file):

```text
because the visible coordinate of the product map does not depend on the added coordinate and the added state or law has total mass one;
```

New:

```text
because the product dynamics factorizes and the added state or law keeps total mass one;
```

### R4 — N2

Sites (at `91e1052d3`): `papers/Main.md:336`

Finding: Review N2: name the σ-algebra on C_V × H (R6 H6.2).

Old (unique in each file):

```text
and let $F$ be a measurable map of $\mathcal{C}_V \times H$, $F^t(x, h)
```

New:

```text
and let $F$ be a map of $\mathcal{C}_V \times H$, measurable for $2^{\mathcal{C}_V} \otimes \mathcal{H}$, $F^t(x, h)
```

### R5 — N3 + S2-C alignment

Sites (at `91e1052d3`): `papers/Main.md:336`

Finding: Review N3 (s introduced; r equals (NR)'s n); return-form wording aligned with S2-C (#1474): "of §3.2".

Old (unique in each file):

```text
If $\Gamma_s$ is not a permutation matrix, the hypothesis of (c) holds under (NR), assumed as a hypothesis of this result and not adopted; (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations.*
```

New:

```text
If some $\Gamma_s$ with $s \geq 1$ is not a permutation matrix, the hypothesis of (c) holds, with $r = n$, under (NR) of that corollary, assumed as a hypothesis of this result and not adopted; (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations.*
```

### R6 — S2-C alignment

Sites (at `91e1052d3`): `book/appendix-b-derivations.md:92`, `book/The-Incompleteness-of-Observation-FULL.md:5769`

Finding: Coordinator alignment with S2-C (#1474): full return form, both clauses, in Theorem B.2.5.

Old (unique in each file):

```text
(NR) [Main §2.3], assumed as a hypothesis and not adopted, which concerns a time that need not be accessible and then has no finite-window test)
```

New:

```text
(NR) [Main §2.3], assumed as a hypothesis and not adopted; (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations)
```

