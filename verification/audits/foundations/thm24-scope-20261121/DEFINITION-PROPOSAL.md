# THM24-SCOPE: a candidate definition of $\mathcal G_{\rm sub}$ (proposal)

**Status: proposal only.** This file is not part of any theorem and claims no consistency with
the corpus; whether it is consistent is for independent review. It is kept apart from NOTE.md's
results. Authorized as research at
[#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074),
item 1. Line numbers are those of `main` at `df6da1c6`.

## 1. Objects

A **substratum datum** is $D=(S,\varphi,\mathcal C_V,\mathcal C_H,\omega_H)$, where:

- $S=\mathcal C_V\times\mathcal C_H$, with $\mathcal C_V$ finite (Main Lemma 1) and $\mathcal C_H$ a set, or a measurable space $(\mathcal C_H,\mathcal H)$ for the classical form;
- $\varphi:S\to S$ is the dynamics;
- $\omega_H$ is a normalized hidden prior: a density matrix on $\ell^2(\mathcal C_H)$ ($\operatorname{Tr}\omega_H=1$), or a probability on $(\mathcal C_H,\mathcal H)$ for the classical form.

A parameter $X\subseteq\{\text{A1},\text{A3},\dots,\text{A6}\}$ names the other axioms held fixed. The definition does not choose $X$.

## 2. The two clauses, kept apart

**(B) Bijectivity clause (A2).** $\varphi$ is a bijection of $S$; bimeasurable in the classical form. $D$ satisfies the axioms in $X$.

**(I) Interface clause.** The fixed observation interface $I(D)$ consists of:

- **Partition.** $V\times H$, with $\mathcal H_V=\ell^2(\mathcal C_V)$.
- **Observable algebra.** $\mathcal A_V=\mathcal B(\mathcal H_V)=M_{\mathcal C_V}(\mathbb C)$, the full visible matrix algebra.
- **Preparations.** $\rho_V\otimes\omega_H$, with $\rho_V$ any density matrix on $\mathcal H_V$ and $\omega_H$ the datum's fixed prior.
- **Channels.** The family $\{\Phi^D_t\}_{t\in\mathbb N}$, where $\Phi^D_t(\rho_V)=\operatorname{Tr}_H[\hat\varphi^t(\rho_V\otimes\omega_H)\hat\varphi^{-t}]$ (Substratum:253). In the classical form it is the hidden-prior family of Main:336, $\Phi^D_t=\int\Psi_{t,h}\,\omega_H(dh)$.
- **Readouts.** Every element of $\mathcal A_V$, applied to $\Phi^D_t(\rho_V)$ at a single time $t$.
- **Not part of $I(D)$:**
  - multi-time statistics with intermediate interventions;
  - other partitions;
  - preparations of the hidden sector other than $\omega_H$;
  - readouts on $\mathcal C_H$ or on an added factor.

**Equivalence.** $D\approx_I D'$ iff:

- (B) holds for both $D$ and $D'$; and
- there is a bijection $\iota:\mathcal C_V\to\mathcal C'_V$ with permutation unitary $U_\iota$ such that $\Phi^{D'}_t(U_\iota\rho_VU_\iota^\dagger)=U_\iota\Phi^D_t(\rho_V)U_\iota^\dagger$ for every $t$ and every $\rho_V$.

The bijection $\iota$ is the identification of the two interfaces' configurations and readouts.

**Population variant $\approx_I^{\rm pop}$.** Replace the channel identity by $T^{D'}_{\iota(i)\iota(j)}(t)=T^D_{ij}(t)$, where $T_{ij}(t)=\langle j|\Phi_t(|i\rangle\langle i|)|j\rangle$.

**Proposed $\mathcal G_{\rm sub}$.** The groupoid whose objects are the data satisfying (B), and whose arrows $D\to D'$ are the identifications $\iota$ witnessing $D\approx_I D'$. Two substrata are $\mathcal G_{\rm sub}$-equivalent iff some arrow joins them.

It is a groupoid, not a group acting on one set. Enlargement changes $S$, so its arrows join different objects. The transformations that keep $S$ fixed, conjugations $\varphi\mapsto\pi\varphi\pi^{-1}$ by $\pi\in\operatorname{Sym}(S)$, act on the bijections of a fixed $S$ as a group. Those that also give arrows form a subgroup only when $\omega_H$ is fixed accordingly (§4, (i)).

## 3. What (B) and (I) separately exclude

- **(I) without (B).** This is the channel-only relation. It contains every channel-preserving extension of #1477 §28: any unitary or isometric factor, and any measurable $w$. NOTE.md N2 gives an example, $\varphi=\mathrm{id}$ on $2\times2$ with $w\equiv0$ on $\{0,1\}$. That pair satisfies (I) and fails (B).
- **(B) without (I).** Every pair of bijections. (B) imposes no observational content.
- **Comparison with Structure Def. 9.3.** That definition compares a single channel under an arbitrary *-isomorphism $\theta$ of $\mathcal A_V$. (I) compares the whole family $\{\Phi_t\}$ under the configuration identification $\iota$ alone. Taken alone, (I) is therefore stricter than Def. 9.3 in the identification it admits, and stricter in the datum, since it uses the family rather than one channel.

## 4. Against the Theorem 24 proof (Substratum:251–266)

| Family | Under the proposal |
|---|---|
| (i) relabelling $\pi=1\otimes P_\sigma$, $\iota=\mathrm{id}$ | Arrow iff $\Phi$ is unchanged. That holds when $P_\sigma\omega_HP_\sigma^\dagger=\omega_H$, which is Substratum:266's step "leaves $\omega_H$ invariant": for every $\sigma$ when $\omega_H$ is uniform on a finite $\mathcal C_H$ (Substratum:253 with D361). With $\omega_H=\operatorname{diag}(2/3,1/3)$ the swap gives no arrow for 40 of the 96 checked cases (NOTE.md K3). Agrees with the proof. |
| (ii) alphabet change | Arrow only where the alphabet-size hypothesis of [SM §2.7] gives equal $\Phi$. The proposal makes (ii) conditional per instance. Agrees with Substratum:251's "under the alphabet-size hypothesis". |
| (iii) enlargement $D\mapsto D\times A$, prior $\omega_H\otimes\sigma_A$ | Arrow iff (B) holds for $\varphi\times\psi$, i.e. $\psi$ is a bijection, and (I) holds. Substratum:266 proves (I) for any normalized $\sigma_A$. So the arrows are exactly D363/D362's member class, and the extensions of D364 fail (B). Agrees with §28. |
| (iv) graph comparison | Not an arrow in general, since $T_{ij}(t)$ may differ. Agrees with "not a family of $\mathcal G_{\rm sub}$". |

**Consequence for the prior.** (iii) multiplies the prior by $\sigma_A$. If the interface fixed $\omega_H$ to be uniform, as the review's sketch (#1486 c.7064081266) does, then (iii) would give arrows only for uniform $\sigma_A$ on a finite $A$. That excludes infinite $A$ and the non-uniform $\sigma_A$ that D363 admits. The proposal therefore makes $\omega_H$ part of the datum, a general normalized prior. Under that choice, (i) gives arrows only for prior-preserving $\sigma$. This is the dependence that NOTE.md F1–F3 record.

## 5. Against the four prose definitions

| Site | Agrees | Stricter / looser | What adopting the proposal would change |
|---|---|---|---|
| Substratum:300: "a symmetry of the *equivalence class of substrata*, defined by the condition that all observables are preserved" | "equivalence class of substrata" matches (B) plus an equivalence relation | The proposal is **looser** in the preserved datum: $I(D)$ is the fixed interface, not "all observables". Literally read, Substratum:300 admits no member of (iii) that is shown to qualify, because Substratum:266 excludes measurements that access $A$. "symmetry" and the implicit group become a groupoid | "all observables" → the fixed-interface data of §4 (NOTE.md P4a) |
| ch02:136 = FULL:766: "a symmetry of the *equivalence class of substrata* defined by the observability condition" | Compatible; the condition is unnamed | The proposal names the condition, (I) | The condition is named. This line is under #1477's ledger (D128/D129), so routing goes to #1477's final scientific review (NOTE.md P4b) |
| Substratum:276: "*every* observables-preserving transformation lies in the group generated by (i)–(iii)" | Completeness becomes: is every arrow of $\approx_I$ a composite of (i), (iii) and the instances of (ii)? Substratum:276's following sentence (equal visible channels do not fix the bijection up to hidden unitary) keeps the question non-trivial | "group generated" → groupoid generated. "observables-preserving" → (I). (ii) enters per instance | NOTE.md P4c |
| Structure:606: "$\mathcal{G}_{\rm sub}$ is characterized by transformations preserving this pair" (the algebra-channel pair of §8.3, Def. 9.3) | The visible algebra and channel are preserved | The proposal is **stricter** in two ways: it adds (B), whereas Structure's pair is defined for any realization, including non-OI substrata (Def. 9.4); and it uses $\iota$ and the family $\{\Phi_t\}$, not an arbitrary $\theta$ and one channel. Structure:606 as written would admit non-bijective enlargements, which belong to the universality class (G4), not to $\mathcal G_{\rm sub}$ | Add the A2 clause and the fixed interface of [Substratum §4] (NOTE.md P4c) |

## 6. Which class the proposal describes

- **Dynamics:** the class OI's axioms admit. Clause (B) is A2, with $X$ as a parameter.
- **Prior:** a larger class than the uniform-prior baseline. $\omega_H$ ranges over all normalized priors. Without that, (iii) loses part of D363's member class (§4).
- **Dropping (B):** that would describe the larger, channel-only class. A result for that class does not extend the theory to it (#1169 c.7064066427, item 6).

## 7. Open points for review

- Whether to fix $X$, and in particular whether A1 belongs to $X$ once A1 is retired.
- Whether $I(D)$ should include multi-time statistics with visible interventions. (i) and (iii) appear to preserve those as well, but neither the corpus nor this record has checked it.
- The classical form for a measurable $\mathcal C_H$: whether (I) should use the Main:336 family or a Koopman form. The R6 pass records that the constant-vector Koopman form fails diagonal preservation (`a1exit-r6-20261120/RESULT.md:41`).
- Whether $\iota$ should be widened to *-isomorphisms of $\mathcal A_V$. That would move the proposal toward Structure Def. 9.3.
