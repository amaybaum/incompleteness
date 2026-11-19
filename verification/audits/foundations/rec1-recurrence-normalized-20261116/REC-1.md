# REC-1 — Recurrence under a normalized invariant hidden law

**Status:** Paper-only check. Independent review ACCEPT WITH CHANGES at `8aec80e9`; changes applied at
`b50ee7bc4a85da09563a9c35b0cbae7d036eb737`; delta review CONFIRMED WITH NITS there; nits applied in this revision. Paper proofs and explicit constructions only; no Lean module, simulation, manuscript edit or physical premise is added.
Every statement below is conditional on the hypotheses named with it (§2). A1 is neither assumed
nor asserted; it appears only as the comparison premise of the controls in node 6.

**Authority.** Owner decision recorded on #1169 in comment 6923725531 by `amaybaum`,
2026-11-16T17:21:37Z.
The owner's words: "Proceed as suggested". Item 2 of that decision reads: "**REC-1 (recurrence).**
Recurrence under a normalized invariant hidden law, which A1 implies (the uniform law), in place of
total finiteness. It covers the Poincaré recurrence statement, its relation to the infinite-XOR
counterexample, and the accessible-time question, which stays separate." The same comment records
the attempt as paper-only, independently reviewed, with no manuscript or Lean edits, and A1 open and
unadopted.

**Source pin.** `main` at `9b2ecf86f3d68b295020250cb3220e57f7796684`. All `file:line` citations are
to that commit.

**Off-`main` references (§A.42 item 8).** The authority comment on #1169 is provenance: no claim
below uses its content beyond the authorization quoted above. No other off-`main` content is used.
The RO-3 material that the premise ladder cites from an unmerged branch is not used here.

**Starting record.** `verification/audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md`
(cited as "the ladder", with its row labels F1–F17 and controls C+, C−1, C−2). This check extends
the ladder's rows F8, F10, F11, F16 and its §§3.3–3.4 and 5; it does not restate them.

## 0. Question

OI uses recurrence of the substratum dynamics. On `main` it is obtained from total finiteness: on a
finite bijective $V\times H$ the order $N=\operatorname{ord}(F)$ gives $F^N=\mathrm{id}$. Can
recurrence instead be obtained without total finiteness from a normalized invariant hidden law,
through Poincaré recurrence, and what exactly does that deliver for each use OI makes of recurrence?

## 1. Productivity test (fixed before the nodes, §A.31)

The ladder already records that a.e. Poincaré recurrence gives no common visible return (F8, C−1).
A node counts as a gem only if it yields a fact strictly stronger than that restatement **and**
either constrains a use of recurrence in the corpus or exposes a hidden assumption. Otherwise it is
recorded as confirming. Favourable branches (recoveries) are pressure-tested at the node where they
occur.

## 2. Setting, contract and hypotheses

**Setting.** $V$ is a finite set with $|V|\ge 2$; $(H,\mathcal H)$ is a measurable space;
$\Omega=V\times H$ carries the product $\sigma$-algebra ($V$ discrete); $\pi:\Omega\to V$ is the
projection and $C_a=\pi^{-1}(a)=\{a\}\times H$. $F:\Omega\to\Omega$ is the update. A hidden prior
$\rho$ is a probability on $H$, shared by every root. Main's rooted maps (Main.md:135, :141) are
$$
\Gamma_t(a,b)=\rho\{h:\ \pi F^t(a,h)=b\},\qquad t\ge 0 .
$$
Total variation is $d(p,q)=\tfrac12\sum_k|p_k-q_k|$ (Main.md:119; the kernel's `HiddenMemory.tv`,
HiddenMemory.lean:92). P-divisibility on $\{0,\dots,n\}$ is as in Main.md:135: for all
$s<t\le n$ some row-stochastic $\Lambda$ has $\Gamma_t=\Gamma_s\Lambda$. $\|x\|_{\mathbb Z}$ is
the distance from $x\in\mathbb R$ to the nearest integer.

**The normalized-law contract and the extra conditions.**

| Label | Statement | Status |
|---|---|---|
| (V) | $V$ finite, $\lvert V\rvert\ge2$ | On `main`: Main Lemma 1 (Main.md:46), from the finite-capacity clause of the Definition |
| (M) | $F$ is a bijection; $F$ and $F^{-1}$ are measurable | Posited (contract). Automatic on a finite discrete carrier |
| (I) | A probability $\mu$ on $\Omega$ with $\mu(F^{-1}E)=\mu(E)$ for every measurable $E$ | Posited (contract). On a finite carrier the counting probability satisfies it: on `main`, Main Lemma 3 (Main.md:54) and Main.md:58 |
| (P) | Normalized invariant hidden law: $\mu=\nu\otimes\rho$ with $\nu(a)>0$ for every $a\in V$, and the rooted laws are $\delta_a\otimes\rho$ | Posited (contract). With a finite carrier and uniform $\rho$, holds with $\nu$ uniform |
| (D) | Domination: $\delta_a\otimes\rho\ll\mu$ for every $a$, for some $\mu$ satisfying (I) | Implied by (P) (Lemma 2.4). On a finite carrier holds for every $\rho$ with $\mu$ uniform |
| (RET) | Common rooted identity return: $\Gamma_N=I$ for some $N\ge1$ | Not implied by (V)(M)(I)(P) (node 3). On a finite carrier: on `main`, Main.md:121, :137 |
| (PER) | Exact common period: $F^N x=x$ for $\mu$-a.e. $x$, some $N\ge1$ | Not implied by (V)(M)(I)(P) (node 3). On a finite carrier: on `main`, Main.md:121 |
| (RIG) | Visible-partition rigidity: some $n_k\to\infty$ has $\mu(C_a\,\triangle\,F^{-n_k}C_a)\to0$ for every $a$ | Posited where used; not implied by (V)(M)(I)(P) (node 3); implied by (RET) under (I)(P) (Prop. 3.6′) and by (PER) |
| (FS) | Full-support visible prior for the history law (root drawn from it independently of $\rho$) | Main's own hypothesis at Main.md:139 |
| Nature | That the actual OI update carries a law satisfying (I)/(P), or (RIG) | Open. Not addressed here; no physical-recovery credit is taken |

**Standard theorems used.**

| Theorem | Exact hypotheses | Status here |
|---|---|---|
| Poincaré recurrence (Poincaré 1890; Walters, *An Introduction to Ergodic Theory*, GTM 79, Thm 1.4) | Measurable $F$, finite invariant measure | Proved in full (Thm 2.1) |
| Kac's lemma, inequality form (Kac, Bull. AMS 53 (1947) 1002–1010) | (M), (I), $\mu(A)>0$ | Proved in full (Thm 2.6; rooted form Thm 2.7) |
| Dirichlet approximation | $\alpha$ irrational | Proved in full (inside Prop. 3.3) |
| Ornstein–Weiss return-time theorem (IEEE Trans. Inf. Theory 39 (1993) 78–83) | Stationary ergodic finite-alphabet process | Cited in Remark 5.4 only; nothing depends on it |

**Results on `main` used.**

| Result | Site | Layer |
|---|---|---|
| Stochastic-inverse lemma | Main.md:131–133; `isPermMatrix_of_stochastic_inverse`, EquivalenceChain.lean:110 | Kernel |
| Revival no-go: a strict increase of $d$ between two rooted rows (C4r) forbids P-divisibility within the horizon | `c4r_implies_pIndivisible`, CausalReadback.lean:134 (Section A: finite $V$, real matrices, no carrier, prior or reversibility) | Kernel |
| Collision–revival no-go (C4e) | `c4e_implies_pIndivisible`, CausalReadback.lean:148 | Kernel |
| Identity return plus overlap forbids P-divisibility | `pIndivisible_of_identity_return_of_overlap`, RecurrenceHorizon.lean:119; `pIndivisible_of_visible_identity_return_nonperm`, ObservableFactorRecurrence.lean:68 | Kernel |
| The matrix family $\Gamma_0=I$, $\Gamma_t=J_2$ ($t\ge1$) is P-divisible at every horizon | `pdFamily_pDivisible`, CausalReadback.lean:256 | Kernel |
| A non-permutation square row-stochastic matrix has two distinct rows sharing positive mass | Main.md:137 (kernel note); ladder §3.1 | Paper |
| Markov with full-support initial law implies P-divisible; no readback gap below $n$ implies Markov on $\{0,\dots,n\}$ | Main.md:630, Main.md:139 | Paper |
| One common near-return with margin after an overlap gives P-indivisibility, on any carrier (ladder F11) | PREMISE-LADDER.md:59, :93–105, through `c4r_implies_pIndivisible` | Paper bound plus kernel |
| Cell-conditioned identity return equals $\pi F^N=\pi$ a.e. (ladder F10) | PREMISE-LADDER.md:58, :83–91 | Paper plus kernel (ENNReal form) |
| Infinite-XOR construction and its all-time rooted family | `verification/programmes/substratum/continuous-substates/infinite-xor-counterexample.md`:7–34 | Paper; bounded regression by its probe |

## 3. Nodes

### Node 1 — Inventory of uses

Categories: **(i)** exact periodicity of the global map, $F^N=\mathrm{id}$; **(i\*)** common rooted
identity return $\Gamma_N=I$ (implied by (i), and by (ii) since $\Gamma_0=I$; under (I)(P) it
implies visible (ii), Prop. 3.6′); **(ii)** periodicity
of time-indexed visible laws (rooted maps or multi-time laws); **(iii)** almost-every-point
recurrence; **(iv)** return of a visible event or cylinder; **(v)** a return time within an
accessible range.

| Use | Site on `main` | What the use consumes | Category |
|---|---|---|---|
| U1 One-step theorem, Step 1 | Main.md:121, :129; mirrors SM.md:44, GR.md:90, book/ch01-observation.md:111 (FULL:446), book/appendix-b-derivations.md:413–417 (FULL:6164) | $T^{(N)}=I$ under the uniform hidden prior, from $\varphi^N=\mathrm{id}$ | (i) ⇒ (i\*) |
| U2 History readback + finite recurrence | Main.md:135–139; mirrors book/ch01-observation.md:181 (FULL:516), book/glossary.md:117 | $\Gamma_L=I$; periodicity $\Gamma_{t+L}=\Gamma_t$ to place a non-permutation map at $1\le s\le\min(k,L-1)$; the full-support equivalence over $\{0,\dots,L\}$ | (i) ⇒ (i\*), (ii) |
| U3 Overlap and return | Main.md:141–143 | $\Gamma_n=I$ taken as a hypothesis; nothing derived from recurrence | (i\*) as input |
| U4 Continuous-time extension | Main.md:155; mirror book/ch01-observation.md:119 | One common near-total return at some $t_R>t_1$; states that Poincaré recurrence does not supply it | weakened (i\*): one common near-return (ladder F11) |
| U5 Summary and scope statements of U1–U2 | Main.md:18, :80, :157, :178, :180, :338, :630, :720, :728, :735, :737; Introduction.md:12; Substratum.md:44, :137, :268; Structure.md:1024, :1140–1177, :1189, :1255; GR.md:138, :585; SM.md:112, :236, :308; Complexity.md:430, :474; Methodology.md:156; Medicine.md:13, :25, :35; Bioinformatics.md:14; book/ch00-introduction.md:53; book/ch02-substratum.md:32; book/ch03-structural-realism.md:36, :102, :114, :240; book/ch05-gauge-structure.md:95; book/ch09-universality.md:106; book/ch15-quantum-engineering.md:114; book/preface.md:3; book/appendix-c-objections.md:120; further sites inheriting U1/U2 or U11: book/ch01-observation.md:89, :93, :133, :139, :201; book/ch18-beyond.md:20, :190, :192; book/appendix-b-derivations.md:194, :421, :451, :454; book/glossary.md:105 | Inherit U1/U2 | (i\*) |
| U6 Non-permutation witness lemma | Main.md:439–441 | "The indivisibility is §2.3's recurrence theorem" | (i\*) |
| U7 CP-indivisibility | Main.md:330; book/appendix-b-derivations.md:92 (FULL:5843) | P-indivisibility of U1/U2, then a conditional implication for diagonal-preserving channels | inherits (i\*) |
| U8 Consolidation and rooted all-time classification | Main.md:642; `pper_of_finiteRootedRealizable`, RootedClassification.lean:339 | Finite order $L$ ⇒ $L$-periodic multi-time law; forward direction of the classification | (i) ⇒ (ii) |
| U9 Finite representative | Main.md:60 | $f^L=\mathrm{id}$ on the eventual image; "no construction is given for an infinite $S$" | (i), definitional |
| U10 §4.6 Setup and Scope (ii) | Main.md:746, :748, :762 | §4.6 is scoped to "a finite bijective $(S, \varphi)$" (Main.md:746). The exact Koopman operator is "unitary, with modulus-one spectrum and exact recurrence. It has no dissipative gap; exponential mixing cannot hold for it" (Main.md:748); exact compressions recur (Main.md:762) | (i) |
| U11 Recurrence time as a scale | Main.md:139 ($k\tau_S\ll t_R$), :449, :453, :540, :544 (condition (ii): accessible order $k\tau_S\ll t_R$), :642 (open question (b): windows $t\ll t_R$); Structure.md:718; book/ch01-observation.md:121 (FULL:456); book/ch18-beyond.md:174–188 (FULL:4980) | $t_R$ as the scale beyond accessible windows; upper bounds $N\le g(\lvert S\rvert)$, $N\mid\operatorname{lcm}(1,\dots,\lvert S\rvert)$ | (v) as scope |
| U12 Cycle averages | GR.md:807–839 (Theorems A.8, A.9) | Cycle decomposition of a bijection of a specified finite shell $\Sigma_E$; exact cycle time averages | (i) on a specified finite subsystem |
| U13 Axiom 2 | Main.md:36, :60; Methodology.md:227; Substratum.md:403 | "Differentiation recurs": more than one moment. Main.md:60: "not that every microstate returns" | not dynamical recurrence; out of scope |
| U14 Routed readback | Main.md:145 | "not P-divisible on $\{0,\ldots,n\}$ for every $n>s$ with $\Gamma_n=I$" ($\Gamma_n=I$ an input), "and so for some $n$, because $(\Gamma_t)$ is periodic and $\Gamma_0=I$" | (i\*) as input; (ii) ⇒ (i\*) |
| U15 Constraint surface | GR.md:587 | Finite $\varphi$-invariant representative of the constraint surface, order $L$, $K_{mL}=I$; hidden prior on each root's fibre, not one shared prior | (i) on a specified finite subsystem |
| U16 Cumulative backflow | book/ch18-beyond.md:74 (FULL:4880) | Periodic rooted laws: a revival in one period recurs in every later one, so the cumulative backflow is unbounded | (ii) |
| U17 No asymptotic decay | book/ch18-beyond.md:40 (FULL:4846) | Recurrence under A1 excludes asymptotic convergence to zero of the history-dependent departures | (i); sibling of U10 |
| U18 The finite-recurrence route | book/ch18-beyond.md:166–172 (FULL:4972–4978) | "needs every root's visible law to return to certainty at a common time, $\Gamma_n = I$"; "Infinite hidden sectors would break the recurrence argument that drives recurrence-scale P-indivisibility; that route would close" | (i\*) |

**Node 1 verdict.** Every dynamical use (U1–U12, U14–U18) consumes (i), (i\*) or (ii), or uses $t_R$ as a scope
scale. No use consumes (iii) or (iv). Class: CONFIRMING (inventory).

### Node 2 — Poincaré recurrence and Kac's lemma under the contract

**Theorem 2.1 (Poincaré).** Let $(\Omega,\mathcal F,\mu)$ be a probability space and
$F:\Omega\to\Omega$ measurable with $\mu(F^{-1}E)=\mu(E)$ for all $E\in\mathcal F$. For every
$A\in\mathcal F$, $\mu$-a.e. $x\in A$ satisfies $F^nx\in A$ for infinitely many $n\ge1$.

*Proof.* Let $B=A\setminus\bigcup_{n\ge1}F^{-n}A$. The sets $F^{-j}B$, $j\ge0$, are pairwise
disjoint: if $x\in F^{-i}B\cap F^{-j}B$ with $i<j$, then $y=F^ix\in B$ and $F^{j-i}y\in B\subset A$,
contradicting $y\in B$. Each has measure $\mu(B)$ by invariance, and their union has measure at
most $1$, so $\mu(B)=0$. For infinitely many returns, fix $N\ge1$; $F^N$ is measurable and
preserves $\mu$, so $B_N=A\setminus\bigcup_{j\ge1}F^{-jN}A$ is null. A point of $A$ with no return
at any time $n\ge N$ lies in $B_N$. Hence the set of points of $A$ with finitely many returns,
$\bigcup_{N\ge1}\bigl(A\setminus\bigcup_{n\ge N}F^{-n}A\bigr)\subset\bigcup_N B_N$, is null.
$\square$

Neither invertibility nor $\mu(\Omega)=1$ beyond finiteness is used. Finiteness of $\mu$ is
load-bearing: $F(n)=n+1$ on $\mathbb Z$ preserves counting measure and $A=\{0\}$ never returns.

**Corollary 2.2 (topological form).** If moreover $\Omega$ is a separable metric space with its
Borel $\sigma$-algebra, then for $\mu$-a.e. $x$, $\liminf_{n\to\infty}d(F^nx,x)=0$.

*Proof.* Let $\{U_i\}$ be the countable family of open balls with centres in a countable dense set
and rational radii. Apply Theorem 2.1 to each $U_i$ and discard the countable union of exceptional
null sets. For a remaining $x$ and $\varepsilon>0$ some $U_i\ni x$ has diameter $<\varepsilon$, and
$x$ returns to $U_i$ infinitely often, so $d(F^nx,x)<\varepsilon$ for infinitely many $n$. $\square$

**Remark 2.3 (exact return is not given).** On $\{0,1\}^{\mathbb Z}$ with the shift and the fair
product measure, each point has measure $0$ and the shift has $2^n$ points of period $n$, so the
periodic points form a countable null set: $\mu$-a.e. point never returns exactly. Exact microscopic
return of a.e. point, and a fortiori (PER), is outside what Theorem 2.1 gives.

**Lemma 2.4 (transfer to rooted laws).** (P) implies (D), and $\delta_a\otimes\rho=\mu(\,\cdot\mid
C_a)$. Under (D), every $\mu$-a.e. statement holds $(\delta_a\otimes\rho)$-a.s. for every root $a$.

*Proof.* For measurable $E$, $\mu(E\cap C_a)=\nu(a)\,(\delta_a\otimes\rho)(E)$ by the definition of
the product measure, so $(\delta_a\otimes\rho)(E)=\mu(E\cap C_a)/\nu(a)\le\mu(E)/\nu(a)$. The second
sentence is the definition of absolute continuity. $\square$

**Remark 2.4′ (domination).** Main's overlap theorem and rooted classification allow any
hidden prior, full support not required (Main.md:141, :642). On a finite carrier the uniform
invariant probability dominates every such prior, so a.e. statements always transfer. Without total
finiteness this transfer is a separate hypothesis, (D): a point-mass prior $\rho=\delta_{h_0}$
makes every $\mu$-a.e. statement silent about the rooted laws whenever $\{(a,h_0)\}$ is $\mu$-null.
Poincaré recurrence of $\mu$ says nothing about a rooted family whose prior is singular to every
invariant probability. Ladder §3.3 (PREMISE-LADDER.md:91) already states that the invariant-law and
rooted conventions agree only under a product disintegration; this remark isolates (D) as the
weaker sufficient condition for transferring a.e. statements. Among the Poincaré sites of node 1
(Main.md:155, :449; book/ch01-observation.md:119; book/ch18-beyond.md:166–172), none transfers a
$\mu$-a.e. statement to an undominated rooted law; Main.md:155 takes the invariant Liouville
measure itself as the hidden prior. Class: ELABORATING (assumption-watch marker: "a.e. under the
invariant law" is "a.s. under the rooted law" only under domination).

**Corollary 2.5 (visible cylinders).** For a visible word $w=(w_0,\dots,w_{k-1})\in V^k$ let
$[w]=\{x:\ \pi F^jx=w_j,\ 0\le j<k\}$, a measurable set. Under (M), (I) and (D): for every root
$a$, $(\delta_a\otimes\rho)$-almost every point whose visible trajectory begins with $w$ shows $w$
again in its visible trajectory, starting at infinitely many times.

*Proof.* Theorem 2.1 for $A=[w]$ makes the exceptional set of $[w]$ $\mu$-null; Lemma 2.4 makes it
null for $\delta_a\otimes\rho$. $\square$

**Theorem 2.6 (Kac, inequality form).** Assume (M) and (I), and let $\mu(A)>0$. With
$\tau_A(x)=\min\{n\ge1:F^nx\in A\}$,
$$
\int_A\tau_A\,d\mu=\mu\Bigl(\bigcup_{k\ge1}\bigcup_{0\le j<k}F^j A_k\Bigr)\le 1,
\qquad\text{hence}\qquad \mathbb E_\mu[\tau_A\mid A]\le\frac1{\mu(A)},
$$
where $A_k=\{x\in A:\tau_A(x)=k\}$.

*Proof.* By Theorem 2.1, $A=\bigcup_{k\ge1}A_k$ up to a null set. The sets $F^jA_k$
($k\ge1$, $0\le j<k$) are measurable since $F^{-1}$ is measurable, and pairwise disjoint: if
$F^jx=F^{j'}x'$ with $x\in A_k$, $x'\in A_{k'}$, $0\le j<k$, $0\le j'<k'$ and $j\ge j'$, then
$F^{j-j'}x=x'\in A$ by injectivity; $j>j'$ would give a return of $x$ to $A$ at time
$0<j-j'<k=\tau_A(x)$, so $j=j'$, $x=x'$ and $k=k'$. Since $F$ is bijective and $F^{-1}$ measurable,
$\mu(F^jE)=\mu(F^{-j}(F^jE))=\mu(E)$. Therefore
$\int_A\tau_A\,d\mu=\sum_k k\,\mu(A_k)=\sum_k\sum_{j<k}\mu(F^jA_k)$, which is the measure of a
disjoint union and so at most $1$. $\square$

(Equality $\mathbb E_\mu[\tau_A\mid A]=1/\mu(A)$ holds when the tower has full measure, e.g. for
ergodic $\mu$; only the inequality is used.)

**Theorem 2.7 (rooted form).** Under (M), (I), (P): for every root $a$ and every visible word $w$
with $w_0=a$ and $\mu([w])>0$,
$\mathbb E_{\delta_a\otimes\rho}\bigl[\tau_{[w]}\mid [w]\bigr]\le 1/\mu([w])$. In particular the
mean first return of the visible label to the root satisfies
$\mathbb E_{\delta_a\otimes\rho}[\tau_{C_a}]\le 1/\nu(a)$, and
$(\delta_a\otimes\rho)(\tau_{C_a}\ge n)\le 1/(n\,\nu(a))$.

*Proof.* $[w]\subset C_a$, so by Lemma 2.4 the rooted law conditioned on $[w]$ is $\mu(\cdot\mid
[w])$; apply Theorem 2.6, and Markov's inequality for the tail. $\square$

**Node 2 verdict.** Under (V)(M)(I)(D): (iii) holds in measurable and, on separable metric
carriers, topological form; exact microscopic return does not follow. (iv) holds for every visible
event and cylinder of positive measure. The only time bound is Kac's, a bound on the conditional
mean of a point-dependent first return of one event. Class: ELABORATING (2.4′ included).

### Node 3 — Which of (i)–(v) the contract gives

**Lemma 3.1 (rooted maps under (P)).** Under (M), (I), (P), each $\Gamma_t$ is a real row-stochastic
matrix and
$$
\Gamma_t(a,b)=\frac{\mu(C_a\cap F^{-t}C_b)}{\nu(a)},\qquad
1-\Gamma_t(a,a)=\frac{\mu(C_a\,\triangle\,F^{-t}C_a)}{2\nu(a)} .
$$

*Proof.* $\{h:\pi F^t(a,h)=b\}$ is the $a$-section of the measurable set $F^{-t}C_b$, hence
measurable; entries are nonnegative and a row sums to $\rho(H)=1$. Lemma 2.4 with
$E=F^{-t}C_b$ gives the first identity. For the second, $\mu(C_a\setminus F^{-t}C_a)
=\nu(a)(1-\Gamma_t(a,a))$, and by invariance
$\mu(F^{-t}C_a\setminus C_a)=\mu(C_a)-\mu(C_a\cap F^{-t}C_a)=\nu(a)(1-\Gamma_t(a,a))$. $\square$

So under (P) Main's rooted family coincides with the ladder's cell-conditioned family (ladder §3.3).

**Proposition 3.2 (rigidity characterizes convergence to the identity).** Under (M), (I), (P), for a
sequence $n_k$:

- (a) if $\mu(C_a\triangle F^{-n_k}C_a)\to0$ for every $a$, then $\Gamma_{n_k}\to I$ entrywise;
- (b) if $\Gamma_{n_k}\to I$ entrywise, then $\mu(C_a\triangle F^{-n_k}C_a)\to0$ for every $a$.

*Proof.* (a) Lemma 3.1 gives $\Gamma_{n_k}(a,a)\to1$, and row sums force the off-diagonal entries
to $0$. (b) Lemma 3.1 gives $\mu(C_a\triangle F^{-n_k}C_a)=2\nu(a)(1-\Gamma_{n_k}(a,a))\to0$.
$\square$

The two directions are stated separately (§A.34); both rest on the one exact identity of Lemma 3.1.
The same identity with one fixed $n$ gives the exact form: $\Gamma_n=I$ iff
$\mu(C_a\triangle F^{-n}C_a)=0$ for all $a$, i.e. $\pi F^n=\pi$ $\mu$-a.e.; that is ladder F10 in
the rooted convention under (P). A single common near-return $\Gamma_n(c,c)\ge1-\varepsilon$ at one
time (Main.md:155; ladder F11) is weaker than (RIG), which asks for arbitrarily accurate return
along unbounded times. Class: ELABORATING.

**Proposition 3.3 (the contract does not give (i), (i\*) or (ii)).** There is a model satisfying
(V), (M), (I), (P), hence Theorems 2.1–2.7, with a non-permutation $\Gamma_1$, in which
$\Gamma_n\ne I$ for every $n\ge1$ and $(\Gamma_t)_{t\ge0}$ is not periodic.

*Construction (irrational rotation).* Fix an irrational $\alpha$. On the circle
$\mathbb T=\mathbb R/\mathbb Z$ with Lebesgue measure $\lambda$ let $R(x)=x+\alpha$. Take
$V=\{0,1\}$, $H=[0,\tfrac12)$ with $\rho=2\lambda|_H$, and
$\Psi(v,h)=v/2+h\bmod 1$, a bimeasurable bijection $V\times H\to\mathbb T$ carrying
$\mathrm{Unif}(V)\otimes\rho$ to $\lambda$. Set $F=\Psi^{-1}R\Psi$. Then (M) holds, $\lambda$ is
$R$-invariant, so $\mu=\mathrm{Unif}(V)\otimes\rho$ is $F$-invariant: (I) and (P) hold.

*Computation.* For $\delta\in\mathbb R$, the arcs $I=[0,\tfrac12)$ and $I-\delta$ overlap in length
$\tfrac12-\|\delta\|_{\mathbb Z}$: for $\delta\in[0,\tfrac12]$ the overlap is
$[0,\tfrac12-\delta)$; for $\delta\in(\tfrac12,1)$ it is $[1-\delta,\tfrac12)$, of length
$\delta-\tfrac12=\tfrac12-(1-\delta)$. The same holds for $[\tfrac12,1)$ by translation. Hence
$$
\Gamma_t=\begin{pmatrix}1-p_t&p_t\\ p_t&1-p_t\end{pmatrix},\qquad p_t=2\|t\alpha\|_{\mathbb Z},
\qquad d\bigl(\Gamma_t(0),\Gamma_t(1)\bigr)=\bigl|1-4\|t\alpha\|_{\mathbb Z}\bigr| .
$$
Since $\alpha$ is irrational, $0<\|t\alpha\|_{\mathbb Z}<\tfrac12$ for $t\ge1$: $\Gamma_t$ has all
entries in $(0,1)$, so $\Gamma_1$ is not a permutation and $\Gamma_t\ne I$ for every $t\ge1$. If
$\Gamma_{t+M}=\Gamma_t$ for some $M\ge1$ and all $t\ge0$, then $\Gamma_M=\Gamma_0=I$, a
contradiction. $\square$

*The same model is rigid.* Dirichlet: for $Q\ge1$ the $Q+1$ points $0,\alpha,\dots,Q\alpha$ mod $1$
lie in $Q$ intervals of length $1/Q$, so two share one and $\|q\alpha\|_{\mathbb Z}\le1/Q$ for some
$1\le q\le Q$. As $\|q\alpha\|_{\mathbb Z}>0$ for every $q\ge1$, given $q_1,\dots,q_j$ choose
$Q>1/\min_{i\le j}\|q_i\alpha\|_{\mathbb Z}$; the $q$ obtained is new. This yields distinct, hence
unbounded, $q_k$ with $\|q_k\alpha\|_{\mathbb Z}\to0$; ordered increasingly they give $q_k\to\infty$, so $\Gamma_{q_k}\to I$ and (RIG) holds by Proposition 3.2(b).
Exact return never occurs; near-return at common times does.

The bilateral Bernoulli shift (ladder C−1, PREMISE-LADDER.md:117–128) and the infinite-XOR model
(node 4) are further models of (V)(M)(I)(P) with $\Gamma_t=J_2$ for all $t\ge1$: there neither
exact nor near common return occurs.

**Proposition 3.4 (rigidity plus a non-permutation map gives P-indivisibility; favourable branch).**
Assume (V), (M), (I), (P), (RIG) along $n_k$, and that $\Gamma_s$ is not a permutation for some
$s\ge1$. Then for all sufficiently large $k$ the rooted family is not P-divisible on
$\{0,\dots,n_k\}$.

*Proof.* $\Gamma_s$ is square and row-stochastic (Lemma 3.1) and not a permutation, so two distinct
roots $a\ne b$ and a value $x$ have $m=\min(\Gamma_s(a,x),\Gamma_s(b,x))>0$ (Main.md:137; if the
$|V|$ nonempty row supports were pairwise disjoint they would be singletons partitioning $V$). Then
$d(\Gamma_s(a),\Gamma_s(b))=1-\sum_y\min(\Gamma_s(a,y),\Gamma_s(b,y))\le1-m$. Put
$\delta_n(c)=1-\Gamma_n(c,c)$; (RIG) and Proposition 3.2(a) give $\delta_{n_k}(c)\to0$. Testing the
event $\{a\}$, and using $\Gamma_n(b,a)\le1-\Gamma_n(b,b)$,
$$
d(\Gamma_n(a),\Gamma_n(b))\ge\Gamma_n(a,a)-\Gamma_n(b,a)\ge1-\delta_n(a)-\delta_n(b).
$$
Choose $k$ with $n_k>s$ and $\delta_{n_k}(a)+\delta_{n_k}(b)<m$. Then
$d(\Gamma_{n_k}(a),\Gamma_{n_k}(b))>1-m\ge d(\Gamma_s(a),\Gamma_s(b))$, which is C4r on horizon
$n_k$, and `c4r_implies_pIndivisible` (CausalReadback.lean:134) gives the conclusion. This is
ladder F11 / §3.4 (PREMISE-LADDER.md:59, :93–105), one common near-return with margin, at a time
$n_k$ supplied by (RIG). $\square$

*Skeptical pressure on this branch.* (1) Poincaré recurrence contributes nothing to the proof: the
input is (RIG), a common-time property that Theorem 2.1 does not give (Bernoulli, XOR). (2) (RIG)
is posited; the contract does not supply it (Proposition 3.3's companions). (3) The times $n_k$ are
unbounded and not located (node 5). (4) For the golden rotation $\alpha=(\sqrt5-1)/2$ the
revival is early: $\|2\alpha\|_{\mathbb Z}=\sqrt5-2$, $\|3\alpha\|_{\mathbb Z}=(7-3\sqrt5)/2$, so
$d_2=9-4\sqrt5$ and $d_3=6\sqrt5-13$, and $d_3>d_2$ iff $\sqrt5>11/5$: P-indivisible on $\{0,1,2,3\}$.
That early revival comes from the rotation's almost periodicity, not from any recurrence time.
Class: ELABORATING (an instance of ladder F11, with the near-return time supplied by (RIG)).

**Proposition 3.5 (the converse of 3.4 fails).** There is a model of (V)(M)(I)(P) that is not
rigid, has $\Gamma_t=J_2$ for all $t\ge3$, and is P-indivisible on $\{0,1,2\}$.

*Construction.* Let $\sigma$ be the shift $(\sigma x)_k=x_{k+1}$ on $\{0,1\}^{\mathbb Z}$ with the
fair product measure, and $X_t=\operatorname{maj}(x_t,1-x_{t+1},1-x_{t+2})$, the visible bit of
$\sigma^tx$. Each value of $X_0$ is taken by exactly four of the eight triples $(x_0,x_1,x_2)$; fix
bijections $\beta_a$ from $\{0,1,2,3\}$ onto them and put
$H=\{0,1,2,3\}\times\{0,1\}^{\mathbb Z\setminus\{0,1,2\}}$ with uniform-times-fair-product $\rho$,
and $\Psi(a,z,y)=(\beta_a(z),y)$. $\Psi$ is a bimeasurable bijection carrying
$\mathrm{Unif}(V)\otimes\rho$ to the product measure (each triple has mass $\tfrac12\cdot\tfrac14$),
so $F=\Psi^{-1}\sigma\Psi$ satisfies (M), (I), (P).

*Computation.* Condition on $(x_1,x_2)$; $x_0$ and $x_3$ are independent fair bits.
$(0,0)$: $X_0=1$, $X_1=1-x_3$. $(0,1)$: $X_0=x_0$, $X_1=0$. $(1,0)$: $X_0=x_0$, $X_1=1$.
$(1,1)$: $X_0=0$. Hence $\Pr(X_0=1,X_1=1)=\tfrac14(\tfrac12+0+\tfrac12+0)=\tfrac14$ and
$\Gamma_1=J_2$. For lag $2$, $\Pr(X_0=1\mid x_2=0)=\Pr(x_0\vee\neg x_1)=\tfrac34$ and
$\Pr(X_0=1\mid x_2=1)=\tfrac14$, so $\Pr(x_2=1\mid X_0=1)=\tfrac14$; $\Pr(X_2=1\mid x_2=1)=\tfrac34$
and $\Pr(X_2=1\mid x_2=0)=\tfrac14$, with $x_3,x_4$ independent of $X_0$ given $x_2$. So
$\Gamma_2(1,1)=\tfrac14\cdot\tfrac34+\tfrac34\cdot\tfrac14=\tfrac38$ and, by the symmetry
$x\mapsto1-x$, $\Gamma_2=\begin{pmatrix}3/8&5/8\\5/8&3/8\end{pmatrix}$. For $t\ge3$, $X_0$ and
$X_t$ depend on disjoint coordinates, so $\Gamma_t=J_2$. The rows of $\Gamma_1$ coincide and those
of $\Gamma_2$ differ: C4e, and `c4e_implies_pIndivisible` gives P-indivisibility on $\{0,1,2\}$.
By Lemma 3.1, $\mu(C_a\triangle F^{-t}C_a)=2\cdot\tfrac12\cdot\tfrac12=\tfrac12$ for $t\ge3$: not
rigid. $\square$

**Proposition 3.6 ((PER) gives (ii)).** Under (M), (I), (D) and (PER) with period $N$, every rooted
map and every multi-time law of the rooted process is $N$-periodic in time.

*Proof.* Let $E=\{x:F^Nx\ne x\}$, $\mu(E)=0$. For $x\notin E$ and $t\ge0$,
$F^{t+N}x=F^t(F^Nx)=F^tx$. By (D), $E$ is null for each $\delta_a\otimes\rho$. $\square$

**Proposition 3.6′ ((RET) gives visible periodicity).** Under (M), (I), (P) and (RET) with
$\Gamma_N=I$: for every root $a$, $(\delta_a\otimes\rho)$-a.s. the visible path satisfies
$X_{t+N}=X_t$ for all $t\ge0$, where $X_t=\pi F^t$. Hence $\Gamma_{t+N}=\Gamma_t$ for all $t$, every
visible multi-time law of the rooted process is $N$-periodic, and (RIG) holds with $n_k=kN$.

*Proof.* By Lemma 3.1, $\mu(C_a\triangle F^{-N}C_a)=0$ for every $a$, so
$E=\{x:\pi F^Nx\ne\pi x\}$ is $\mu$-null. For $t\ge0$, $\pi F^{t+N}x\ne\pi F^tx$ only if
$F^tx\in E$, i.e. $x\in F^{-t}E$, which is $\mu$-null by (I). The countable union
$\bigcup_{t\ge0}F^{-t}E$ is $\mu$-null, hence null for each $\delta_a\otimes\rho$ by Lemma 2.4. Off
it the visible path is $N$-periodic, which gives the periodicity of every visible law, and
$X_{kN}=X_0$ gives $\Gamma_{kN}=I$. $\square$

The hidden state need not return: (RET) gives visible, not microscopic, periodicity (ladder §5).
Class: ELABORATING.

**Proposition 3.7 (rigidity extends to cylinders and lags).** Under (M), (I), (P) and (RIG) along
$n_k$: (a) $\mu([w]\triangle F^{-n_k}[w])\to0$ for every visible word $w$; (b)
$\Gamma_{n_k+t}\to\Gamma_t$ entrywise for every $t\ge0$.

*Proof.* (a) For a word $w=(w_0,\dots,w_{\ell-1})$, $[w]=\bigcap_{j<\ell}F^{-j}C_{w_j}$ and $F^{-n}[w]=\bigcap_{j<\ell}F^{-j}F^{-n}C_{w_j}$. A
symmetric difference of two intersections lies in the union of the termwise symmetric differences,
and $\mu(F^{-j}A\triangle F^{-j}B)=\mu(A\triangle B)$ by (I), so
$\mu([w]\triangle F^{-n_k}[w])\le\sum_{j<\ell}\mu(C_{w_j}\triangle F^{-n_k}C_{w_j})\to0$. (b) By
Lemma 3.1, $|\Gamma_{n+t}(a,b)-\Gamma_t(a,b)|=|\mu(C_a\cap F^{-t}F^{-n}C_b)-\mu(C_a\cap
F^{-t}C_b)|/\nu(a)\le\mu(F^{-t}(F^{-n}C_b\triangle C_b))/\nu(a)=\mu(C_b\triangle
F^{-n}C_b)/\nu(a)$, which tends to $0$ along $n_k$. $\square$

**Proposition 3.8 (rigidity forces zero visible entropy rate).** Assume (M), (I) and (RIG) along
$n_k$. Let $X_t=\pi F^t$, $t\in\mathbb Z$, a stationary process under $\mu$ (since $F$ is
invertible and preserves $\mu$), and $h=\lim_{n\to\infty}H(X_0\mid X_{-1},\dots,X_{-n})$, a
non-increasing limit. Then $h=0$.

*Proof.* Put $p_n=\mu(X_0\ne X_{-n})$. Applying the measure-preserving $F^n$,
$p_n=\mu(X_n\ne X_0)=\sum_a\mu(C_a\setminus F^{-n}C_a)=\tfrac12\sum_a\mu(C_a\triangle F^{-n}C_a)$,
the last step by invariance as in Lemma 3.1, so $p_{n_k}\to0$. With
$E=\mathbf 1\{X_0\ne X_{-n}\}$,
$H(X_0\mid X_{-n})\le H(X_0,E\mid X_{-n})=H(E\mid X_{-n})+H(X_0\mid E,X_{-n})\le
h_2(p_n)+p_n\log|V|$, because $X_0=X_{-n}$ on $\{E=0\}$. Conditioning on more variables does not
increase entropy, so $H(X_0\mid X_{-1},\dots,X_{-n_k})\le h_2(p_{n_k})+p_{n_k}\log|V|\to0$, and the
non-increasing limit $h$ is $0$. $\square$

So Proposition 3.4's hypothesis can hold only where the visible process has zero entropy rate under
$\mu$: its present is determined by its infinite past ($H(X_0\mid X_{-\infty}^{-1})=h=0$ by martingale convergence). On a finite carrier the visible process is
periodic and the same holds. Proposition 3.8 does not bear on ladder F11's single near-return.
Class: BORDERLINE (the standard fact that rigid systems have zero entropy, proved here directly for
the visible process; it narrows the scope of Proposition 3.4).

**Node 3 summary.**

| Category | Given by (V)(M)(I)(P)? | Evidence |
|---|---|---|
| (i) $F^N=\mathrm{id}$ | No | Remark 2.3; Prop. 3.3 |
| (i\*) $\Gamma_N=I$ | No | Prop. 3.3; ladder C−1; node 4 |
| (ii) periodic visible laws | No; given by (RET) under (I)(P), and by (PER) | Prop. 3.3, 3.6, 3.6′ |
| (iii) a.e. recurrence | Yes, measurable/topological; not exact | Thm 2.1, Cor. 2.2, Rem. 2.3 |
| (iv) visible event/cylinder return | Yes, point-dependent times | Cor. 2.5 |
| (v) accessible return time | Only Kac's event-mean bound | Thm 2.6–2.7; node 5 |
| P-indivisibility of the rooted family | Not determined by the contract: both outcomes occur | XOR and Bernoulli P-divisible at every horizon; rotation and Prop. 3.5 P-indivisible |

### Node 4 — Relation to the infinite-XOR counterexample

What is true is the opposite of exclusion: the infinite-XOR model **satisfies** the contract, and
fails (RET) and (RIG).

1. *Contract.* Its carrier $\Omega=\mathbb Z/3\times(\{0,1\}^2)^{\mathbb Z}$ carries uniform phase
   times independent fair block pairs (infinite-xor-counterexample.md:7). The update advances the
   phase and shifts the block tape at the wrap (ibid.:9). Invariance checked here: the phase
   advance permutes the uniform phase, and the conditional tape law given the phase is the same
   product law at every phase, preserved by the shift. The record's $\Psi$ (ibid.:11–16) maps
   $\mathrm{Bern}(\tfrac12)\otimes\rho$ to this law: at each phase,
   $(x,z)\mapsto(A_0,B_0)$ is a bijection of $\{0,1\}^2$, and the visible bit is $x$ at each phase
   ($A_0$, $B_0$, $A_0\oplus B_0$ respectively). So (M), (I), (P) hold with $\nu$ uniform, and
   Theorems 2.1–2.7 apply: a.e. recurrence, cylinder recurrence, and
   $\mathbb E[\tau_{C_a}]\le 2$.
2. *No common return.* The record proves $\Gamma_0=I$, $\Gamma_t=J_2$ for every $t\ge1$
   (ibid.:20–25); the matrix family is P-divisible at every horizon
   (`pdFamily_pDivisible`, CausalReadback.lean:256). By Lemma 3.1, for the conjugated update
   $F=\Psi^{-1}T\Psi$ on $V\times H$,
   $\mu(C_a\triangle F^{-n}C_a)=2\cdot\tfrac12\cdot\tfrac12=\tfrac12$ for every $n\ge1$: (RET) and
   (RIG) fail, and the rooted family is not periodic.
3. *Not a mixing artefact.* The model is not weakly mixing: $g(p,\cdot)=e^{2\pi ip/3}$ satisfies
   $g\circ T=e^{2\pi i/3}g$. The failure of return is a property of the visible partition: the
   centred indicator $f=\mathbf 1_{C_0}-\tfrac12$ has $\int f\cdot f\circ T^t\,d\mu
   =\tfrac14-\tfrac14=0$ for every $t\ge1$.
4. *Choice of invariant law.* The rooted family depends only on $(F,\pi,\rho)$. Any invariant
   probability satisfying (D) for this $\rho$ leaves $\Gamma_t=J_2$, so no such law yields (RET)
   or (RIG). Invariant probabilities with exact return exist: the configurations whose block tape
   has period $q$ form a finite $T$-invariant set of $3\cdot4^q$ points, on which $T$ is a
   permutation and the uniform law is invariant. That law is singular to $\delta_a\otimes\rho$
   ($\rho$ is nonatomic), so it says nothing about this rooted family.
5. *Readback.* The model's three-time law has a readback gap with
   $I(X_0;X_2\mid X_1)=1-h_2(2/3)$ on a two-step window (ibid.:27–34). That route uses no
   recurrence and is unaffected by the contract.

**Node 4 verdict.** The infinite-XOR model is a model of the normalized-law contract in which
Poincaré recurrence holds and the common return used by U1–U8 fails. It is a counterexample to
"(V)(M)(I)(P) ⇒ (i\*), (ii), or recurrence-route P-indivisibility", not a model the contract
excludes. Class: ELABORATING (the record states normalization and invariance; items 3–4 are added).

### Node 5 — The accessible-time question

**Proposition 5.1 (no bound from total finiteness or from the normalized law).** For every
$K\ge1$ there is a finite bijective model with uniform law, hence satisfying (V), (M), (I), (P),
(PER), (RET) and (RIG), with $|V|=2$ and a non-permutation $\Gamma_1$, whose rooted family is
P-divisible on $\{0,\dots,K\}$ and whose least $n\ge1$ with $\Gamma_n=I$ exceeds $K$.

*Construction.* Take $m\ge2K+2$, $V=\{0,1\}$, $H=\mathbb Z/m$ with uniform $\rho$, and
$F(v,k)=(v\oplus\mathbf 1_{k=m-1},\,k+1\bmod m)$, a bijection.

*Proof.* For $n\le m$ the residues $k,k+1,\dots,k+n-1$ are distinct, so at most one flip occurs in
$n$ steps, and exactly one iff $m-1-k\bmod m\in\{0,\dots,n-1\}$, which holds for $n$ of the $m$
seeds. So $\Gamma_n$ is binary symmetric with $p_n=n/m$ for $0\le n\le m$; $\Gamma_1$ is not a
permutation. For $s<t\le K<m/2$, $p_s\le p_t<\tfrac12$, and the binary symmetric $\Lambda$ with
$1-2q=(1-2p_t)/(1-2p_s)\in(0,1]$ is stochastic and satisfies $\Gamma_t=\Gamma_s\Lambda$ (binary
symmetric parameters compose as $1-2p\mapsto(1-2p)(1-2q)$): P-divisible on $\{0,\dots,K\}$.
$F^m(v,k)=(1-v,k)$, so $\Gamma_m$ is the swap, $\Gamma_n(a,a)=\Gamma_{n-m}(1-a,a)=(n-m)/m<1$ for
$m<n<2m$, and $\Gamma_{2m}=I=\Gamma_0$; the least identity time is $2m>K$, which is also the order
of $F$. $\square$

The first P-indivisibility witness of this model lies after $m/2$: $d_n=|1-2n/m|$ decreases on
$[0,m/2]$ and increases on $[m/2,m]$.

**Proposition 5.2 (what total finiteness bounds).** On a finite carrier the order satisfies
$N\le g(|S|)$ (Landau's function) and $N\mid\operatorname{lcm}(1,\dots,|S|)$
(book/ch18-beyond.md:176, :186; book/ch01-observation.md:121). The bound is a function of $|S|$,
which visible data do not fix (book/ch18-beyond.md:178; Main.md:60). No lower bound on $N$ is
given (book/ch18-beyond.md:186), and Proposition 5.1 shows none on the identity time from the
premises listed there.

**Proposition 5.3 (what the normalized law bounds).** Under (M), (I), (P) the only time bound is
Theorem 2.7: $\mathbb E[\tau_{[w]}\mid[w]]\le1/\mu([w])$ and
$\Pr(\tau_{C_a}\ge n)\le1/(n\nu(a))$ under the rooted law. These bound point-dependent first
returns of one visible event. They do not bound a common return time, which need not exist
(Proposition 3.3, node 4), nor the rigidity times $n_k$ of Proposition 3.4.

**Remark 5.4 (cylinder returns grow with the word).** For a stationary ergodic finite-alphabet
process, the first return time $R_k$ of the initial $k$-word satisfies
$\tfrac1k\log R_k\to h$ almost surely, $h$ the entropy rate (Ornstein–Weiss 1993). When $h>0$, Kac
means for long visible histories exceed any fixed window. This remark is cited and nothing depends
on it.

**Node 5 verdict.** Neither total finiteness nor a normalized invariant law places any common return
time, or the earliest recurrence-route P-indivisibility witness, in an accessible range. Total
finiteness bounds the order above by a function of an unobserved cardinality; the normalized law
bounds only means of point-dependent event returns, by $1/\mu(A)$. The accessible-time question
stays separate, as the authority states. Class: CONFIRMING, with Proposition 5.1 as an explicit
witness for every $K$.

### Node 6 — Downstream verdicts and A1-preserved controls

**Proposition 6.1 (readback gives a non-permutation map without recurrence).** With $F$
measurable and a hidden prior $\rho$, with roots drawn from any visible prior independently of $\rho$: if two distinct
positive-probability visible histories $(x_0,\dots,x_k)$, $(x_0',\dots,x_k')$ have $x_k=x_k'$, then
some $\Gamma_s$ with $1\le s\le k$ is not a permutation. The same holds if some visible step up to
time $k$ is non-deterministic.

*Proof.* If $\Gamma_1,\dots,\Gamma_k$ are permutation matrices, $\Gamma_t(a,\cdot)=
\delta_{\sigma_t(a)}$ with $\sigma_t$ bijective, then for each root $a$, $\rho$-a.s.,
$\pi F^t(a,h)=\sigma_t(a)$ for all $t\le k$ (finitely many full-measure sets). Every
positive-probability history is $(a,\sigma_1(a),\dots,\sigma_k(a))$, and its endpoint $x_k$ fixes
$a=\sigma_k^{-1}(x_k)$, so two such histories with one endpoint coincide; and
$X_{t+1}=\sigma_{t+1}\sigma_t^{-1}(X_t)$ a.s. is deterministic. $\square$

This is the first half of Main's readback theorem (Main.md:135) with $\min(k,L-1)$ replaced by $k$;
neither recurrence nor an invariant law is used.

**Proposition 6.2 (the recurrence-cycle equivalence under rigidity).** Assume (V), (M), (I), (P),
(RIG) and (FS). The following are equivalent:
(a) a readback gap at some finite order (two positive-probability histories with a common endpoint
and different next-step laws);
(b) some $\Gamma_s$, $s\ge1$, is not a permutation;
(c) the rooted family is not P-divisible on $\{0,\dots,n\}$ for some $n$.

*Proof, one direction at a time.* (a)⇒(b): the two histories are distinct, so Proposition 6.1
applies. (b)⇒(c): Proposition 3.4; this is the only direction that uses (RIG). (c)⇒(a): if there
were no gap at any order below $n$, the law on $\{0,\dots,n\}$ would be Markov (Main.md:139), and a
Markov law with full-support initial distribution has $\Gamma_t=\Gamma_s(Q_s\cdots Q_{t-1})$ with
stochastic factors (Main.md:630), contradicting (c). $\square$

Without (RIG), (b)⇒(c) fails: the infinite-XOR model has (a) and (b) and is P-divisible at every
horizon (node 4). Under total finiteness the equivalence is Main.md:139, which additionally places
the gap below $L$. Step (b)⇒(c) is ladder F11 at a time supplied by (RIG) (Prop. 3.4); it holds
equally whenever a single common near-return with F11's margin follows the non-permutation time.
Class: ELABORATING.

**Verdict table.** "Recovered" means: recovered under (V)(M)(I)(P) alone. The named gap is always a
hypothesis the contract does not supply.

| Use | Verdict | Precise statement / gap |
|---|---|---|
| U1 One-step theorem | Not recovered; recovered in weaker form under (RIG) | Counterexample under the contract: XOR and Bernoulli (non-permutation $\Gamma_1$, P-divisible at every horizon). Under (RIG): P-indivisible on $\{0,\dots,n_k\}$ for large $k$ (Prop. 3.4, an instance of ladder F11). Under (RET): Main's conclusion verbatim (`pIndivisible_of_visible_identity_return_nonperm`). Gap: (RIG) or (RET) |
| U2 Readback + recurrence | Split | Non-permutation $\Gamma_s$, $1\le s\le k$, recovered without recurrence (Prop. 6.1). P-indivisibility and the equivalence: not recovered; recovered in weaker form under (RIG)+(FS) (Prop. 6.2). The bound $s\le L-1$ and the horizon $\{0,\dots,L\}$ need (RET) at $L$ (Prop. 3.6′) |
| U3 Overlap and return | Recovered as stated | Its hypothesis $\Gamma_n=I$ is an input; the matrix form needs only row-stochastic $\Gamma_s$ (RecurrenceHorizon.lean:119), which Lemma 3.1 supplies. The contract does not supply $\Gamma_n=I$ |
| U4 Continuous time | Unchanged; condition identified | Main already conditions on one common near-total return. Its discrete-time form is ladder F11's single near-return with margin; (RIG) (Prop. 3.2) is the stronger condition of arbitrarily accurate return at unbounded times. A flow version is not proved here |
| U5 Summary statements | Inherit U1/U2 | "Recurrence-scale" conclusions are finite-carrier statements; A1-free analogues hold only under (RET), (RIG) or a single near-return with the margin of ladder F11 |
| U6 Non-permutation witness lemma | Not recovered; weaker form under (RIG) | As U1 |
| U7 CP-indivisibility | Inherits U1/U2 | The conditional implication from population P-indivisibility to CP-indivisibility is carrier-independent for a diagonal-preserving channel family; such a family on an infinite carrier is not constructed here (ladder F15) |
| U8 Consolidation and classification | Not recovered; the A1-free class is larger | Non-periodic rooted families occur under the contract (Prop. 3.3, node 4); (ii) for visible laws needs (RET) (Prop. 3.6′), microscopic periodicity needs (PER) (Prop. 3.6). The finite theorem is unchanged |
| U9 Finite representative | Not applicable | Definitional for finite carriers; no infinite construction is supplied here |
| U10 §4.6 Setup | Theorem unaffected; the reason is correct in its own scope and does not transfer | §4.6 is scoped to a finite bijective $(S,\varphi)$ (Main.md:746), where its reason holds. Modulus-one spectrum and the absence of a dissipative gap hold for every unitary Koopman operator, including mixing ones (Bernoulli shift: functions $f,g$ of coordinates in $[-r,r]$ satisfy $\int f\cdot g\circ F^n\,d\mu=\int f\,d\mu\int g\,d\mu$ for $n>2r$, by independence of disjoint coordinates); the exclusion of mixing at Main.md:748, :762 rests on exact recurrence of a finite permutation. Assumption-watch: an A1-free transfer of §4.6 would have to re-derive where (EM) is placed. The theorem's conclusion is conditional on (EM) for the compression and does not consume recurrence; its finiteness use through canonical typicality is outside REC-1 |
| U11 $t_R$ as scale | Scope label; no common $t_R$ under the contract | No common recurrence time exists in general (Prop. 3.3, node 4); only Kac means per event (Prop. 5.3). In Main §3.4, $t_R$ occurs at Main.md:540, :544 (the accessible-order clause of condition (ii)) and :642; under the contract no common $t_R$ exists, so condition (ii) needs an accessibility scale stated independently of recurrence |
| U12 Cycle averages | Not recovered; not addressed | Exact cycle averages need a finite invariant shell (a hypothesis of GR Theorem A.8); an invariant law gives ergodic-theorem limits, a different object (ladder F17) |
| U13 Axiom 2 | Out of scope | Not dynamical recurrence |
| U14 Routed readback | Split | "For every $n>s$ with $\Gamma_n=I$": recovered under the contract, since both proofs use only the store clause's two positivity conditions (Main.md:145), which is the overlap-and-return matrix form (RecurrenceHorizon.lean:119) with $\Gamma_s$ row-stochastic by Lemma 3.1; the cited routed kernel theorems themselves are stated for finite $H$. "For some $n$": needs (RET); weaker form under (RIG) or a single F11 near-return (Prop. 3.4). The write clause's seed with $\mu_H(h)>0$ has no counterpart under a nonatomic prior unless restated for a positive-measure seed set; it is not consumed by the P-indivisibility conclusion |
| U15 GR constraint surface | Different convention; not addressed | Priors sit on each root's fibre, so (P) does not apply. The A1-free analogue is the cell-conditioned family of an invariant law (ladder §3.3, F10), whose exact identity return is F10's condition $\pi F^N=\pi$ a.e.; GR supplies it through a specified finite invariant subsystem |
| U16 Cumulative backflow | Not recovered; recovered under (RET) or (RIG), given one revival | Under (RET) the rooted laws are $N$-periodic (Prop. 3.6′) and the argument of ch18:74 applies. Under (RIG), a revival $d_t>d_s$ ($s<t$) gives $d_{n_k+t}-d_{n_k+s}\ge(d_t-d_s)/2$ for large $k$ (Prop. 3.7(b)); passing to $n_k$ with $n_{k+1}>n_k+t$ gives disjoint windows, each contributing at least $(d_t-d_s)/2$ to the cumulative increase, which is therefore unbounded. Under the contract alone: XOR and Bernoulli have no revival; Prop. 3.5 has one revival and $\Gamma_t=J_2$ for $t\ge3$, so a bounded cumulative increase |
| U17 No asymptotic decay | Correct in its A1 scope; the reason does not transfer | Under the contract correlations may decay (Bernoulli, U10) or not (rotation). The sentence's "neither … follows" remains true under the contract, but the A1 reason, exclusion of decay by recurrence, does not. Assumption-watch sibling of U10 |
| U18 Finite-recurrence route | Finding for the coordinator; no manuscript edit | Read as a statement about deriving the return from finiteness, ch18:170 holds. Read as saying that recurrence-scale P-indivisibility has no route on an infinite hidden sector, it is stronger than the record on `main` supports: ladder F11 gives P-indivisibility on any carrier from one common near-return with margin, Prop. 3.4 gives it from (RIG), and the rotation (Prop. 3.3) is an infinite hidden sector on which P-indivisibility holds by both, with no identity return. Likewise ch18:172's "needs … $\Gamma_n = I$" is what the exact route uses, not what P-indivisibility at that scale requires. The conditional routes keep their premises posited. ch18:170 ("this route") and ch18:172 ("one particular route") favour the route-specific reading, under which the passage is correct; the note concerns only the unrestricted reading |

**A1-preserved controls.** Take $\Omega$ finite, $F$ a bijection and $\mu$ the uniform law
(Main Lemma 3), so that every existing A1 result applies; check each statement of this record
against it.

| Control | Check | Result |
|---|---|---|
| K1 Contract | (M) automatic; counting measure invariant; (P) with $\nu$ and $\rho$ uniform; (D) for every prior $\rho$, since only $\emptyset$ is $\mu$-null | Holds |
| K2 Extra conditions | Finite order $N$ gives (PER), hence (RET), and (RIG) with $n_k=kN$ (Prop. 3.6′) | Holds; the controls pass because finiteness supplies (PER), not because the contract does |
| K3 Prop. 3.4 | With $n_k=kN$, $\delta_{n_k}=0$, giving P-indivisibility on $\{0,\dots,N\}$ | Reduces to Main.md:121–127 and :135 |
| K4 Prop. 6.2 | Reduces to Main.md:139 with the gap localized below $L$ by finiteness | Consistent |
| K5 Prop. 3.6, 3.6′ | $\Gamma_{t+N}=\Gamma_t$ | Reduces to Main.md:137 and the forward classification (RootedClassification.lean:339) |
| K6 Kac | $\mathbb E[\tau_A\mid A]\le\lvert\Omega\rvert/\lvert A\rvert$; for $A=\{x\}$, cycle length $\le\lvert\Omega\rvert$; for $A=C_a$, $\le\lvert V\rvert$ | Consistent |
| K7 Counterexamples | Rotation, Bernoulli, XOR and Prop. 3.5 have uncountable carriers; none contradicts a finite-carrier theorem. Prop. 5.1 is finite and satisfies Main's one-step theorem: $d_1=1-2/m<1=d_{2m}$ | Consistent |
| K8 Overlap theorem | Hypotheses and proof unchanged | Unchanged |
| K9 Prop. 3.7, 3.8 | $\Gamma_{kN+t}=\Gamma_t$ exactly; the visible process is periodic, so its entropy rate is $0$ | Consistent |

Every existing A1 result is recovered when $\mu$ is the uniform law on a finite set. In each case
the return input is supplied by finiteness through (PER).

## 4. Result

1. Under a normalized invariant hidden law, (V)(M)(I)(P), Poincaré recurrence gives a.e.
   recurrence (measurable and topological, not exact) and recurrence of every visible event and
   cylinder of positive measure, at point-dependent times, with Kac's bound
   $\mathbb E[\tau_A\mid A]\le1/\mu(A)$ (Theorems 2.1–2.7). Transfer to Main's rooted laws needs
   domination (D), which (P) supplies and total finiteness supplies for every prior.
2. No use of recurrence in the corpus consumes (iii) or (iv). Every dynamical use consumes (i),
   (i\*) or (ii), which the contract does not give: the irrational rotation, the Bernoulli shift
   and the infinite-XOR model satisfy the contract with no common return and non-periodic rooted
   laws (Prop. 3.3, node 4).
3. P-indivisibility of the rooted family is not determined by the contract: the XOR and Bernoulli
   models are P-divisible at every horizon; the rotation and Prop. 3.5 are P-indivisible.
4. Convergence $\Gamma_{n_k}\to I$ along $n_k\to\infty$ is exactly rigidity of the visible partition
   (Prop. 3.2); a single common near-return (Main.md:155, ladder F11) is weaker and already suffices
   for P-indivisibility. Rigidity supplies such near-returns, so it gives P-indivisibility without
   any exact return (Prop. 3.4), and the recurrence-cycle equivalence of Main.md:139 survives with
   (RIG) in place of total finiteness (Prop. 6.2); both are instances of ladder F11. The converse of
   Prop. 3.4 fails (Prop. 3.5). (RIG) is posited, extends to all visible cylinders (Prop. 3.7) and
   forces zero visible entropy rate (Prop. 3.8). (RET) alone gives periodic visible laws under
   (I)(P) (Prop. 3.6′).
5. The infinite-XOR model satisfies the contract; it fails (RET) and (RIG), and no invariant law
   dominating its rooted laws changes that.
6. Neither total finiteness nor the normalized law bounds any common return time into an accessible
   range (Prop. 5.1–5.3).
7. §4.6's exclusion of mixing for the exact dynamics holds in its stated scope, a finite bijective
   $(S,\varphi)$, where it rests on exact recurrence. Under the contract the exact dynamics can mix
   (Bernoulli shift), so an A1-free transfer of §4.6 would have to re-derive where (EM) is placed.
   The §4.6 theorem is unaffected. The same holds for book/ch18-beyond.md:40 (U17).
8. Cross-document finding (U18): book/ch18-beyond.md:170, read as closing every route to
   recurrence-scale P-indivisibility on an infinite hidden sector, is stronger than ladder F11 on
   `main` supports. ch18:170 ("this route") and ch18:172 ("one particular route") favour the
   route-specific reading, under which the passage is correct; the note concerns only the unrestricted
   reading. Flagged; no manuscript edit is made.
9. A1 remains open and unadopted. Whether nature supplies (I), (P) or (RIG) is open. No physical
   recovery is claimed.

**Hypothesis ledger.** (V): on `main` (Main.md:46). (M), (I), (P): posited contract; the uniform
law on a finite carrier satisfies them (Main.md:54, :58). (D): proved from (P) (Lemma 2.4).
(RET), (PER): not implied by the contract; on `main` for finite carriers. (RIG): posited where used;
not implied by the contract; implied by (RET) under (I)(P) (Prop. 3.6′). (FS): Main's hypothesis (Main.md:139). Poincaré, Kac (inequality),
Dirichlet: standard, proved here. Ornstein–Weiss: standard, cited in a remark only. Kernel results:
on `main` as listed in §2. Supply of (I), (P), (RIG) by nature: open.

**Productivity outcome (§A.31).** No NEW finding remains after review. ELABORATING: node 2 and
Remark 2.4′ (credited to ladder §3.3), Prop. 3.2 (ladder F10), Prop. 3.4 and 6.2 (instances of
ladder F11), Prop. 3.5, Prop. 3.6′, node 4, U10/U17 (assumption-watch for any A1-free transfer of
§4.6), U18 (cross-document finding). BORDERLINE: Prop. 3.8 (zero visible entropy rate under
rigidity). CONFIRMING: nodes 1 and 5. One depth-first pass was made; the fixed-point
criterion of 3–4 passes without NEW findings is not claimed.

## 5. Open questions

1. Whether the selected OI update, with some invariant law satisfying (P) for a declared prior, is
   rigid for the visible partition, or has one common near-return with the margin of ladder F11.
   Open, class by class.
2. Whether nature supplies a normalized invariant law with (P) for the OI carrier. Open.
3. A continuous-time form of Propositions 3.2 and 3.7 for measure-preserving flows (rigidity along
   real times $t_k\to\infty$). Not proved here. For Main.md:155 a single common near-return with
   the margin of ladder F11 already suffices.
4. Whether some condition weaker than (RIG) holds for the selected OI update; under one common
   near-return with the margin of ladder F11 after a non-permutation time, (b)⇒(c) holds by F11.
5. Any bound placing a rigidity time or a near-return time in an accessible window. Open; neither
   total finiteness nor the contract supplies one.
