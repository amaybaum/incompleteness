# A1-EXIT Step 2, unit S2-B (R6 corrections): preregistered edit list

**Authorization.** Owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7056875845](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7056875845):
Step-2 units S2-A to S2-E, manuscript corrections only, each in its own scope. The optional R6 items
#9, #16, #17, #20 and #21 are skipped by that decision; no edit is made for them. A1 and Main ledger
item (ii) are not deleted, their identifiers are not retired and the pointer sites are not rewritten
(the deletion edit is not authorized). No merge and no workflow dispatch.

**Goal link (§A.47).** A1-exit objective (#1169). This unit decides whether the sites of R6 §7 that
rest on A1 can be made true without it, as a proved weaker condition, an explicit finite-only scope or
an open statement.

**Base.** `main` at `1c7eedc40` (drafting snapshot). Line numbers below are at this base. R6's own
pin is `9db51884`; Main lines 1–760 and every other edited file are unchanged between the two, so
R6's `M:n` coordinates hold at this base.

**Sources.** R6 record `verification/audits/foundations/a1exit-r6-20261120/RESULT.md` §7 (edit list),
§§3–5 (proved statements and hypotheses); ledger rows X-50, X-51, X-53
(`verification/audits/foundations/a1exit-ledger-20261120/rows.json`).

**Edit map.**

| R6 §7 item | Kind | Edits |
|---|---|---|
| #1 M:328 | P | E1a, E1b |
| #2 M:328–334 | G | E2 |
| #3 M:60 | G | E3 |
| #4 M:732 item (ii) list | G | E5a, E5b |
| #5 M:742 | G | E7 |
| #6 AppB:92 = FULL:5769 (and proof AppB:94 = FULL:5771) | G | E11a, E11b |
| #7 M:459 | G | E8a, E8b, E8c |
| #8 M:473 | G + P | E9a, E9b |
| #10 M:60 | G | E4 |
| #11 M:732 item (ii) deep-sector clauses | G | E6a, E6b |
| #12 Sub:257–266 | G | E12a, E12b, E12c; consequence E12d (Sub:249) |
| #13 Sub:268 | G | E13a, E13b |
| #14 Sub:92 | G | E14 |
| #15 ch02:144 = FULL:774 | G | E15a, E15b |
| #18 M:336 | G′ | E10 |
| #19 Str:53 | G′ | E16 |
| #9, #16, #17, #20, #21 | O | skipped (owner decision) |

**Hypotheses as R6 proves them.** E2 states R6 Theorem 6 with (H6.1)–(H6.5): fibre-injective
measurable `F`, measurable coincidence sets, `ρ` a probability; the P witness under (NR), assumed as a
hypothesis and not adopted, with the return qualification. (RIG) is not printed in Main: R6 lists (NR)
or (RIG), and Main names (NR) as its weaker condition elsewhere; printing one of two sufficient
conditions states no more than is proved. No Koopman constant-vector form is stated (R6 T6-K (α),
refuted), and nothing is claimed for the Koopman forms (β) on diffuse carriers or (γ). E8 and E9 state
R6 Theorem 7 under (M1) in integrated form, (M0) for the first step, any measurable hidden space and
any reference probability. E4, E6 and E12–E16 state R6 T9(a), (b), (d): normalized (normal) states,
unitary or isometric dynamics (classical form: a probability and any measurable map), unnormalizable
factors excluded, a coupled deep sector outside. T9(c) (ρ-preserving relabelling, Sub:253, item #17)
is optional and not applied.

**X-50 criterion 3.** E2 prints the ledger's queued wording for X-50 verbatim ("under (NR), assumed as a
hypothesis of this result and not adopted; (NR) concerns a time that need not be accessible and then
has no finite-window test; for the selected update on ℤ^d the only laws known to satisfy it are
supported on periodic configurations"). This discharges X-50's criterion-3 item; S2-C skips it.

**Main item (ii).** E5a, E5b, E6a and E6b change only the list inside item (ii). Item (ii) stays, with
its identifier and pointers.

**Mirrors (§A.14, §A.25).** Main has no book mirror of §3.2's Lemma or the new Corollary, of the
M:459 and M:473 theorems, of M:60 or of M:732 (checked by grep of "diagonal preservation",
"permutation-dilation", "reference prior defining", "H_k = h", "uniform-prior bijection marginal").
AppB:92/94 ↔ FULL:5769/5771 and ch02:144 ↔ FULL:774 are edited as pairs. Str:53 restates Theorem
24(iii) (E16). The R6 §11 item 9 grep ("CP-indivisib", "physical-memory", "physical memory",
"finite factor", "finite decoupled", "decoupled finite", "Infinite extensions", "Infinite factors")
is re-run after the edits and every surviving hit is recorded with its reason in RESULT.md.

**Checks.** Register scan of added lines (§A.32, §A.33); `sh ./build.sh Main Substratum Structure`
and `sh ./build.sh --book` with no dropped glyphs, page count and median characters per page;
`python3 tools/coverage_check.py`, updating `verification/coverage/LEDGER.json` if a fingerprint
changes; applicable §A.40 local checks.

## Edits

Each old string is unique in each listed file at the base (checked mechanically before this commit).

### E1a — R6 §7 #1; ledger X-50

Sites: `papers/Main.md:328`

Finding: R6 §7 #1 (P): the Lemma's proof needs a diagonal μ_H, which the statement does not say; Prop. 6.9 and K2(i) show the conclusion fails for every non-diagonal μ_H.

Old (unique in each file):

```text
with $U$ a permutation unitary map computational-diagonal states to computational-diagonal states.*
```

New:

```text
with $U$ a permutation unitary and $\mu_H = \sum_k p_k\,|k\rangle\langle k|$ the diagonal density matrix of a probability $(p_k)$ on $\mathcal{C}_H$ map computational-diagonal states to computational-diagonal states.*
```

### E1b — R6 §7 #1; ledger X-50

Sites: `papers/Main.md:330`

Finding: R6 §7 #1 (P), second clause: for every non-diagonal μ_H some permutation breaks the Lemma (R6 Prop. 6.9).

Old (unique in each file):

```text
$\square$ (Certified exactly for $t = 1, \ldots, 6$ in `c1_cp_scope_probes.py`.)
```

New:

```text
$\square$ (Certified exactly for $t = 1, \ldots, 6$ in `c1_cp_scope_probes.py`.) The diagonal hypothesis on $\mu_H$ is needed: if $n \geq 2$ and $\langle h|\mu_H|h'\rangle \neq 0$ for hidden basis states $h \neq h'$, fix a hidden state $g_0$ and take a bijection with $(x_1, h) \mapsto (x_1, g_0)$, $(x_1, h') \mapsto (x_2, g_0)$ and the other points $(x_1, g)$ sent to distinct points $(x_1, g')$ with $g' \neq g_0$, extended to a bijection of $\mathcal{C}_V \times \mathcal{C}_H$; the only pair of hidden inputs at $x_1$ carried to a common hidden output at $x_1$ and at $x_2$ is $(h, h')$, so $\langle 1|\Phi_1(|1\rangle\langle 1|)|2\rangle = \langle h|\mu_H|h'\rangle \neq 0$.
```

### E2 — R6 §7 #2; ledger X-50

Sites: `papers/Main.md:334`

Finding: R6 §7 #2 (G): the CP-indivisibility apparatus holds on a measurable hidden carrier (R6 Theorem 6, INF), with the P witness under (NR) (WEAK); X-50 criterion 3 queued wording.

Old (unique in each file):

```text
$T_{ij}(t_2) = \langle j|\Lambda(\Phi_{t_1}(|i\rangle\langle i|))|j\rangle = \sum_k T_{ik}(t_1)\,M_{kj}$ — P-divisibility of the population process. The contrapositive gives the result. $\square$
```

New:

```text
$T_{ij}(t_2) = \langle j|\Lambda(\Phi_{t_1}(|i\rangle\langle i|))|j\rangle = \sum_k T_{ik}(t_1)\,M_{kj}$ — P-divisibility of the population process. The contrapositive gives the result. $\square$

*Corollary (measurable hidden carrier).* *Let $\mathcal{C}_V$ be finite with $|\mathcal{C}_V| \geq 2$, let $\rho$ be a probability on a measurable space $(H, \mathcal{H})$, and let $F$ be a measurable map of $\mathcal{C}_V \times H$, $F^t(x, h) = (A_t(x, h), K_t(x, h))$, such that for every $t \geq 1$ and every $h$ the map $x \mapsto F^t(x, h)$ is injective and every coincidence set $\{h : K_t(x, h) = K_t(y, h)\}$ lies in $\mathcal{H}$ (as when $H$ is standard Borel). With $\Psi_{t,h}(|x\rangle\langle y|) = [K_t(x, h) = K_t(y, h)]\,|A_t(x, h)\rangle\langle A_t(y, h)|$, define $\Phi_t(\sigma) = \int_H \Psi_{t,h}(\sigma)\,\rho(dh)$. Then: (a) for finite $H$ and bijective $F$, $\Phi_t$ is the family of the Lemma, with $U$ the permutation unitary of $F$ and $\mu_H = \sum_h \rho(h)\,|h\rangle\langle h|$; (b) each $\Phi_t$ is CPTP, and $\Phi_t(|x\rangle\langle x|) = \sum_b \Gamma_t(x, b)\,|b\rangle\langle b|$ with $\Gamma_t(x, b) = \rho\{h : A_t(x, h) = b\}$, the rooted maps of the near-return corollary of §2.3; (c) if $(\Gamma_t)$ is not P-divisible on $\{0, \ldots, r\}$, there are $0 < t_1 < t_2 \leq r$ with no positive trace-preserving map, in particular no CPTP map, $\Lambda$ satisfying $\Phi_{t_2} = \Lambda \circ \Phi_{t_1}$. If $\Gamma_s$ is not a permutation matrix, the hypothesis of (c) holds under (NR), assumed as a hypothesis of this result and not adopted; (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations.*

*Proof.* $\Psi_{t,h}$ depends on $h$ only through the map $A_t(\cdot, h)$ and the relation $x \sim_h y \iff K_t(x, h) = K_t(y, h)$, which range over a finite set; the set of $h$ giving a fixed pair is a finite Boolean combination of the measurable sets $\{h : A_t(x, h) = b\}$ and of coincidence sets, so $\Phi_t$ is a finite convex combination of the $\Psi_{t,h}$ with weights summing to $\rho(H) = 1$. (a) $\mathrm{Tr}_H\,|F^t(x, h)\rangle\langle F^t(y, h)| = \Psi_{t,h}(|x\rangle\langle y|)$; weight by $\rho(h)$ and sum. (b) If $x \sim_h y$ and $A_t(x, h) = A_t(y, h)$, then $F^t(x, h) = F^t(y, h)$ and $x = y$, so $A_t(\cdot, h)$ is injective on each class $C$ of $\sim_h$; with $K_C = \sum_{x \in C} |A_t(x, h)\rangle\langle x|$, $\Psi_{t,h}(\sigma) = \sum_C K_C\,\sigma\,K_C^\dagger$ and $\sum_C K_C^\dagger K_C = I$, so $\Psi_{t,h}$ is CPTP, and $\Psi_{t,h}(|x\rangle\langle x|) = |A_t(x, h)\rangle\langle A_t(x, h)|$. (c) $\Gamma_0 = I$, so a pair $(s, t)$ at which P-divisibility fails has $s \geq 1$; put $t_1 = s$, $t_2 = t$. The proof of the Theorem uses only positivity and trace preservation of $\Lambda$ and the diagonal form (b), and gives a stochastic $M$ with $\Gamma_{t_2} = \Gamma_{t_1} M$, a contradiction. The last sentence of the statement is the near-return corollary of §2.3. $\square$
```

### E3 — R6 §7 #3; ledger X-50

Sites: `papers/Main.md:60`

Finding: R6 §7 #3 (G): the CP theorem uses the finite representative only through its P witness; under (NR) it holds on measurable carriers.

Old (unique in each file):

```text
(recurrence-scale P-indivisibility, the CP-indivisibility theorem of §3.2, the all-time periodicity of a fixed realization in §3.4)
```

New:

```text
(recurrence-scale P-indivisibility; the CP-indivisibility theorem of §3.2, only through that P-indivisibility, which its measurable-carrier corollary takes from (NR); the all-time periodicity of a fixed realization in §3.4)
```

### E4 — R6 §7 #10; ledger X-53

Sites: `papers/Main.md:60`

Finding: R6 §7 #10 (G): R6 T9(a),(b) prove the decoupled-factor invariance for normalized factors of any cardinality with unitary/isometric (resp. measurable) dynamics; a coupled deep sector stays outside.

Old (unique in each file):

```text
A finite factor adjoined to the hidden sector, prepared independently in a normalized state and evolved by its own permutation, with product dynamics, leaves every visible transition probability unchanged, because the visible coordinate of the product map does not depend on the added coordinate and the added prior has total mass one; the cardinality of such a deep sector is unobservable at the fixed visible/hidden interface. A deep sector that the dynamics couples to the remaining degrees of freedom, and an infinite hidden sector, are outside that statement, and this Remark makes no claim about the observability of their cardinality.
```

New:

```text
A factor of any cardinality adjoined to the hidden sector, prepared independently in a normalized state or law and evolved by its own dynamics — a Hilbert space of any dimension with a normal state and a unitary or isometry, or a measurable space with a probability and a measurable map — with product dynamics, leaves every visible transition probability unchanged, because the visible coordinate of the product map does not depend on the added coordinate and the added state or law has total mass one; the cardinality of such a deep sector is unobservable at the fixed visible/hidden interface. A deep sector that the dynamics couples to the remaining degrees of freedom is outside that statement, and this Remark makes no claim about the observability of its cardinality.
```

### E5a — R6 §7 #4; ledger X-50

Sites: `papers/Main.md:732`

Finding: R6 §7 #4 (G): add (NR) as the weaker condition for the CP theorem's P witness.

Old (unique in each file):

```text
the near-return condition (NR) for the P-indivisibility conclusion of §2.3, the invariant-product condition
```

New:

```text
the near-return condition (NR) for the P-indivisibility conclusion of §2.3 and for the P-indivisibility input of the CP-indivisibility theorem of §3.2 on a measurable hidden carrier, the invariant-product condition
```

### E5b — R6 §7 #4; ledger X-50, X-51

Sites: `papers/Main.md:732`

Finding: R6 §7 #4 (G): R6 Theorem 6 (CP apparatus) and Theorem 7 (physical memory) hold on measurable hidden carriers (INF); neither is a statement about finite representatives.

Old (unique in each file):

```text
the orbit capacity, the CP-indivisibility theorem of §3.2, the physical-memory theorem of §3.4 and the canonical-typicality step of §4.6 are statements about finite representatives
```

New:

```text
the orbit capacity and the canonical-typicality step of §4.6 are statements about finite representatives
```

### E6a — R6 §7 #11; ledger X-53

Sites: `papers/Main.md:732`

Finding: R6 §7 #11 (G), as #10.

Old (unique in each file):

```text
when that sector is a finite factor prepared independently in a normalized state and evolved by its own permutation, with product dynamics,
```

New:

```text
when that sector is a factor of any cardinality prepared independently in a normalized state or law and evolved by its own dynamics (a unitary or isometry, or a measurable map), with product dynamics,
```

### E6b — R6 §7 #11; ledger X-53

Sites: `papers/Main.md:732`

Finding: R6 §7 #11 (G), as #10.

Old (unique in each file):

```text
by such a finite decoupled enlargement
```

New:

```text
by such a decoupled enlargement
```

### E7 — R6 §7 #5; ledger X-50

Sites: `papers/Main.md:742`

Finding: R6 §7 #5 (G).

Old (unique in each file):

```text
| CP-indivisibility of $\{\Phi_t\}$ | Proved for the framework's diagonal-preserving (permutation-dilation) channels;
```

New:

```text
| CP-indivisibility of $\{\Phi_t\}$ | Proved for the hidden-prior (diagonal-preserving) channel family on finite or measurable hidden carriers, given P-indivisible populations;
```

### E8a — R6 §7 #7; ledger X-51

Sites: `papers/Main.md:459`

Finding: R6 §7 #7 (G): R6 Theorem 7(e) proves the quantitative bound for a measurable coupling step on any measurable hidden space with any reference probability, under (M0) for the first step.

Old (unique in each file):

```text
*Model one coupling step as the uniform-prior bijection marginal of §3.2's construction, and between coupling events let the hidden sector evolve by any map on the hidden conditional. Suppose the mixing hypothesis holds: with $\pi_H$ the *reference prior defining $T$* — the uniform hidden prior of the model above — every realized
```

New:

```text
*Let the hidden sector be a measurable space $H$ with a reference probability $\pi_H$, and model one coupling step by a Markov kernel $K(x, h; \cdot)$ on $\mathcal{C}_V$, measurable in $h$: given the visible record, the next visible value has law $\int K(x, h; \cdot)\,\mu(dh)$, with $x$ the current visible value and $\mu$ the hidden conditional at the coupling time; $T := \bar{K}$, $\bar{K}_x = \int K(x, h; \cdot)\,\pi_H(dh)$, and the hidden conditional at the first coupling is $\pi_H$ for each initial visible value. In the finite model of §3.2's construction, $K(x, h; \cdot)$ is the bijection's visible step from $(x, h)$ and $\pi_H$ the uniform hidden prior, so that $T$ is the uniform-prior bijection marginal. Between coupling events let the hidden sector evolve by any map on the hidden conditional. Suppose the mixing hypothesis holds: with $\pi_H$ the *reference prior defining $T$*, every realized
```

### E8b — R6 §7 #7; ledger X-51

Sites: `papers/Main.md:467`

Finding: R6 §7 #7 (G): the proof's sum over h becomes an integral against a finite signed measure (R6 §4.2, Lemma 7.0).

Old (unique in each file):

```text
$$T^{(2)}_{x_0 x_2} - (T^2)_{x_0 x_2} = \sum_{x_1} T_{x_0 x_1} \sum_h \Delta(h)\, P_\varphi(x_2 \mid x_1, h),$$
```

New:

```text
$$T^{(2)}_{x_0 x_2} - (T^2)_{x_0 x_2} = \sum_{x_1} T_{x_0 x_1} \int K(x_1, h; x_2)\,\Delta(dh),$$
```

### E8c — R6 §7 #7; ledger X-51

Sites: `papers/Main.md:469`

Finding: R6 §7 #7 (G): as E8b; (M0) is where the proof uses T^(1) = T.

Old (unique in each file):

```text
where $P_\varphi(x_2 \mid x_1, h) \in \{0, 1\}$ is the bijection's visible step. Taking the row's total variation and the triangle inequality, $\tfrac{1}{2}\sum_{x_2} |\cdot| \leq \sum_{x_1} T_{x_0 x_1} \cdot \tfrac{1}{2} \sum_h |\Delta(h)| \sum_{x_2} P_\varphi(x_2 \mid x_1, h) =
```

New:

```text
where $K(x_1, h; \cdot)$ is the coupling kernel ($P_\varphi(x_2 \mid x_1, h) \in \{0, 1\}$, the bijection's visible step, in the finite model) and the first-coupling condition gives $T^{(1)} = T$. Taking the row's total variation and the triangle inequality, with $|\Delta|$ the total-variation measure of the signed measure $\Delta$, $|\Delta|(H) = 2\,\mathrm{TV}(\mu'_{x_0 x_1}, \pi_H)$ by the Hahn decomposition, $\tfrac{1}{2}\sum_{x_2} |\cdot| \leq \sum_{x_1} T_{x_0 x_1} \cdot \tfrac{1}{2} \int \sum_{x_2} K(x_1, h; x_2)\,|\Delta|(dh) =
```

### E9a — R6 §7 #8; ledger X-51

Sites: `papers/Main.md:473`

Finding: R6 §7 #8 (G + P): conditioning on the point event H_k = h is null for diffuse laws; (M1) is its integrated form (R6 §4.1, §4.2).

Old (unique in each file):

```text
— given the whole visible past and $H_k = h$, $X_{k+1}$ has law $K(x_k, h; \cdot)$, with $\pi_H$ the reference prior —
```

New:

```text
— (M1): for every visible past $x_{\leq k}$ of positive probability, every measurable $B \subseteq H$ and every $y$, $P(X_{\leq k} = x_{\leq k},\, H_k \in B,\, X_{k+1} = y) = \int_B K(x_k, h; y)\, P(X_{\leq k} = x_{\leq k},\, H_k \in dh)$, on any measurable hidden space $H$, with $\pi_H$ the reference probability —
```

### E9b — R6 §7 #8; ledger X-51

Sites: `papers/Main.md:473`

Finding: R6 §7 #8 (G).

Old (unique in each file):

```text
$\bar{K}_{x_k} := \sum_h \pi_H(h)\, K(x_k, h; \cdot)$
```

New:

```text
$\bar{K}_{x_k} := \int K(x_k, h; \cdot)\,\pi_H(dh)$
```

### E10 — R6 §7 #18; ledger X-50

Sites: `papers/Main.md:336`

Finding: R6 §7 #18 (G′ with #2).

Old (unique in each file):

```text
the framework's channels are in that class, which is what licenses the theorem.
```

New:

```text
the framework's channels, including the measurable-carrier family of the Corollary above, are in that class, which is what licenses the theorem.
```

### E11a — R6 §7 #6; ledger X-50

Sites: `book/appendix-b-derivations.md:92`, `book/The-Incompleteness-of-Observation-FULL.md:5769`

Finding: R6 §7 #6 (G).

Old (unique in each file):

```text
across its recurrence cycle (from a non-permutation rooted map and finiteness)
```

New:

```text
(across its recurrence cycle, from a non-permutation rooted map and finiteness; or, on a measurable hidden carrier, from a non-permutation rooted map and the near-return condition (NR) [Main §2.3], assumed as a hypothesis and not adopted, which concerns a time that need not be accessible and then has no finite-window test)
```

### E11b — R6 §7 #6; ledger X-50

Sites: `book/appendix-b-derivations.md:94`, `book/The-Incompleteness-of-Observation-FULL.md:5771`

Finding: R6 §7 #6 (G): proof extended as in #2.

Old (unique in each file):

```text
The framework's $\Phi_t$ are permutation dilations with uniform ancilla, so they map computational-diagonal states to exactly diagonal states (a permutation unitary conjugates a diagonal state to a diagonal state; the partial trace preserves diagonality).
```

New:

```text
The framework's $\Phi_t$ are permutation dilations with uniform ancilla, or, on a measurable hidden carrier with a fibre-injective measurable map $F^t = (A_t, K_t)$ whose coincidence sets are measurable, mixtures over the hidden points $h$ of the channels $|x\rangle\langle y| \mapsto [K_t(x,h) = K_t(y,h)]\,|A_t(x,h)\rangle\langle A_t(y,h)|$ [Main §3.2], so they map computational-diagonal states to exactly diagonal states (a permutation unitary conjugates a diagonal state to a diagonal state; the partial trace preserves diagonality; each mixed channel sends $|x\rangle\langle x|$ to $|A_t(x,h)\rangle\langle A_t(x,h)|$).
```

### E12a — R6 §7 #12; ledger X-53

Sites: `papers/Substratum.md:257`

Finding: R6 §7 #12 (G): R6 T9(a).

Old (unique in each file):

```text
*(iii) Finite decoupled ancillary enlargement.* Fix the visible/hidden interface $V\times H$, the normalized hidden density matrix $\omega_H$, and the permutation unitary $U$ induced by $\varphi$. Adjoin a finite factor $A$, prepared independently in a density matrix $\sigma_A$ with $\operatorname{Tr}\sigma_A=1$, and evolve it by a permutation unitary $W$ with product dynamics $U\otimes W$.
```

New:

```text
*(iii) Decoupled ancillary enlargement.* Fix the visible/hidden interface $V\times H$, the normalized hidden density matrix $\omega_H$, and the permutation unitary $U$ induced by $\varphi$. Adjoin a factor Hilbert space $\mathcal K_A$ of any dimension, prepared independently in a density matrix $\sigma_A$ with $\operatorname{Tr}\sigma_A=1$, and evolve it by a unitary or isometry $W$ with product dynamics $U\otimes W$.
```

### E12b — R6 §7 #12; ledger X-53

Sites: `papers/Substratum.md:262`

Finding: R6 §7 #12 (G): R6 T9(a),(b); unnormalizable factors excluded (R6 §5, P4).

Old (unique in each file):

```text
Consequently every rooted population law $T_{ij}(t)$ is unchanged. Removing the independently prepared decoupled factor reverses this comparison. This is a finite, fixed-interface result; an infinite extension requires its own normalized measure or trace-class state and a well-defined evolution, and is not established by finite uniform counting.
```

New:

```text
Consequently every rooted population law $T_{ij}(t)$ is unchanged. The rooted population laws are likewise unchanged for a classical factor: a measurable space $A$ with a probability $\alpha$, prepared independently and evolved by any measurable map $w$, with product dynamics $\varphi\times w$ and the uniform hidden prior times $\alpha$. Removing the independently prepared decoupled factor reverses this comparison. This is a fixed-interface result for a factor of any cardinality; it uses the normalization $\operatorname{Tr}\sigma_A=1$ (respectively $\alpha(A)=1$), and an unnormalizable factor, such as the identity on an infinite-dimensional $\mathcal K_A$ or counting measure on an infinite $A$, is not covered.
```

### E12c — R6 §7 #12; ledger X-53

Sites: `papers/Substratum.md:266`

Finding: R6 §7 #12 (G): proofs of T9(a) (isometry) and T9(b).

Old (unique in each file):

```text
Partial trace over $H A$ is the original reduced state multiplied by $\operatorname{Tr}(W^t\sigma_AW^{\dagger t})=\operatorname{Tr}\sigma_A=1$. This proves the coherent-channel identity and hence its population restriction.
```

New:

```text
Partial trace over $H A$ is the original reduced state multiplied by $\operatorname{Tr}(W^t\sigma_AW^{\dagger t})=\operatorname{Tr}(\sigma_AW^{\dagger t}W^t)=\operatorname{Tr}\sigma_A=1$, using $W^\dagger W=1$. This proves the coherent-channel identity and hence its population restriction. For a classical factor the visible coordinate of $(\varphi\times w)^t$ does not depend on the factor's coordinate, so each rooted event is its $\mathcal C_H$-section times $A$, of weight $\alpha(A)=1$ times the original.
```

### E12d — R6 §7 #12 (consequence); ledger X-53

Sites: `papers/Substratum.md:249`

Finding: Necessary consequence of #12 (not listed in R6 §7): the section preamble describes the coherent-family form of (iii) as finite; after E12a it holds for a factor of any dimension.

Old (unique in each file):

```text
(i) and the finite normalized-product form of (iii) preserve the coherent family
```

New:

```text
(i) and the normalized Hilbert-space product form of (iii) preserve the coherent family
```

### E13a — R6 §7 #13; ledger X-53

Sites: `papers/Substratum.md:268`

Finding: R6 §7 #13 (G): R6 T9(d).

Old (unique in each file):

```text
For the independently prepared finite decoupled extension of Theorem 24(iii), the full fixed-interface channel family,
```

New:

```text
For the independently prepared decoupled extension of Theorem 24(iii), of any cardinality, the full fixed-interface channel family (for a classical factor, its $T_{ij}(t)$ restriction),
```

### E13b — R6 §7 #13; ledger X-53

Sites: `papers/Substratum.md:268`

Finding: R6 §7 #13 (G).

Old (unique in each file):

```text
 Infinite extensions need a separately specified normalized state or measure and dynamics before any such comparison can be made.
```

New:

```text
 An unnormalizable extension is outside Theorem 24(iii) and this transfer.
```

### E14 — R6 §7 #14; ledger X-53

Sites: `papers/Substratum.md:92`

Finding: R6 §7 #14 (G), as #12.

Old (unique in each file):

```text
Theorem 24(iii) gives an exact freedom to adjoin independently prepared finite decoupled factors at a fixed interface. Infinite extensions require specified normalized measures or states and well-defined dynamics; the finite identity does not supply that construction.
```

New:

```text
Theorem 24(iii) gives an exact freedom to adjoin independently prepared decoupled factors of any cardinality at a fixed interface, each in a normalized state or law with its own unitary, isometric or measurable dynamics; an unnormalizable factor is not covered.
```

### E15a — R6 §7 #15; ledger X-53

Sites: `book/ch02-substratum.md:144`, `book/The-Incompleteness-of-Observation-FULL.md:774`

Finding: R6 §7 #15 (G), as #12.

Old (unique in each file):

```text
*(iii) Finite decoupled ancillary enlargement.* Adjoin a finite factor to the deep hidden sector, prepare it independently in a normalized density matrix, and keep its dynamics exactly decoupled from the original system.
```

New:

```text
*(iii) Decoupled ancillary enlargement.* Adjoin a factor of any dimension to the deep hidden sector, prepare it independently in a normalized density matrix, and keep its dynamics exactly decoupled from the original system, as any unitary or isometry of the factor.
```

### E15b — R6 §7 #15; ledger X-53

Sites: `book/ch02-substratum.md:144`, `book/The-Incompleteness-of-Observation-FULL.md:774`

Finding: R6 §7 #15 (G), as #12.

Old (unique in each file):

```text
Infinite factors require a separately specified normalized state or measure and well-defined dynamics; finite uniform counting does not supply that extension.
```

New:

```text
A classical factor with a probability law and any measurable dynamics likewise preserves every rooted population law. The identity uses the factor's normalization: an infinite factor under uniform counting has none and is not covered.
```

### E16 — R6 §7 #19; ledger X-53

Sites: `papers/Structure.md:53`

Finding: R6 §7 #19 (G′ with #12).

Old (unique in each file):

```text
(iii) *Finite decoupled ancillary enlargement.* An independently prepared, normalized, finite factor with exactly decoupled product dynamics may be adjoined or removed at a fixed visible/hidden interface without changing the coherent channel family; infinite or boundary-coupled extensions are not covered
```

New:

```text
(iii) *Decoupled ancillary enlargement.* An independently prepared, normalized factor of any dimension with exactly decoupled unitary or isometric product dynamics may be adjoined or removed at a fixed visible/hidden interface without changing the coherent channel family; unnormalizable or boundary-coupled extensions are not covered
```

