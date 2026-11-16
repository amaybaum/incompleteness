# NR-1 — Near-return and distinguishability revival for the selected OI update without total finiteness

**Status:** Paper-only check. Independent review ACCEPT WITH CHANGES at
`4b0c1b8fb5c3f9965a931676ffae540cfeb3fef8`; delta review CONFIRMED WITH NITS at
`164e77de8166e15ffe92cc563d04078220ff6dd5`; nits applied in this revision.
Paper proofs, exact finite computations
(inline script and expected output, §7) and citations only; no Lean module, simulation of a physical
system, manuscript edit or physical premise is added. A1 is neither assumed nor asserted; finite tori
appear only as the comparison carrier of node 4 and as controls. No physical-recovery credit is taken.

**Authority.** Owner decision recorded on #1169 in comment 6925594215 by `amaybaum`,
2026-11-16T18:40:12Z. The comment records the owner's words: "Let's focus on the items related to the
most significant physical claims first", and then, in answer to the ranked proposal to run items 1 and
2 in parallel, "Proceed as suggested". Item 2 of that decision reads: "**NR-1 (near-return for the
actual OI dynamics).** Does OI's selected update supply ladder F11's single common near-return with
margin, without A1? That would give P-indivisibility at recurrence scale on a carrier that is not
finite. Inputs on main are A1-10 and REC-1." The same comment records the work as paper-only, with no
manuscript, Lean or registry edits, A1 open and unadopted, and A4 unchanged.

**Source pin.** `main` at `d6f07dc45bc74ad6cc4391dc699765bda24cec23`. All `file:line` citations are to
that commit.

**Off-`main` references (§A.42 item 8).** The authority comment on #1169 is provenance: no claim below
uses its content beyond the authorization quoted above. The scope note in §0 is the coordinating
session's note on #1169, comment 6926358446 (posted 2026-11-16T19:11:32Z, titled "NR-1 scope note"; written and posted by the coordinating session through the owner's GitHub account; it is not an owner decision),
which is provenance: it orders and generalizes the question within the same authorization and adds no
premise. The RO-3 inventory and its mixing unit, which the premise ladder cites from the unmerged
branch of PR #1303, are not used: every statement below about the prime-alphabet linear update on an
infinite lattice is proved here or computed by the inline script. No other off-`main` content is used.

**Starting records.** `verification/audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md`
("the ladder"; rows F1–F17, controls C+, C−1, C−2) and
`verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md` ("REC-1"; contract
(V)(M)(I)(P)(D), conditions (RET)(PER)(RIG), Propositions 3.2–3.8). This record answers REC-1 §5 open
question 1 for one specified class; it does not restate either record.

## 0. Question

**As authorized.** Does OI's own selected update — the specific substratum dynamics the framework uses,
not an arbitrary bijection — supply ladder F11's single common near-return with margin after a
non-permutation time (PREMISE-LADDER.md:59, :93–105) without total finiteness, on the infinite lattice
$\mathbb Z^d$ with a finite local alphabet and a natural invariant law? If so, P-indivisibility at
recurrence scale would hold without A1 for OI's actual dynamics.

**Scope note (coordinating session, 2026-11-16, under the same authorization; posted on #1169 as
comment 6926358446, "NR-1 scope note").** The C4r/C4e question below is the general form of the
authorized question, P-indivisibility at recurrence scale without A1 for the selected update, and stays
within that authorization; F11 is one sufficient case of it. The primary target is
a distinguishability revival for the selected update, not only F11's near-return:
`c4r_implies_pIndivisible` (CausalReadback.lean:134) gives P-indivisibility from any strict later
increase of rooted total-variation distinguishability (C4r, CausalReadback.lean:67), and
`c4e_implies_pIndivisible` (CausalReadback.lean:148) from a collision followed by separation (C4e,
CausalReadback.lean:62), with no recurrence and no finiteness of the hidden sector. F11's near-return is
one special case of a revival. The questions are therefore taken in the order: (a) does some pair of
roots show C4r or C4e; (b) separately, F11's near-return; (c) is any revival window of accessible order
(Main.md:540–544)? Counterexample-first: a local reversible rule of OI's form whose rooted
distinguishability is monotone non-increasing on $\mathbb Z^d$ is a counterexample to the revival
route.

## 1. Productivity test (fixed before the nodes, §A.31)

REC-1 already shows that the normalized-law contract decides neither near-return nor P-indivisibility
in general (REC-1 Prop. 3.3, node 4) and leaves the selected update open (REC-1 §5 item 1). A node is a
gem only if it yields, for the selected update itself, a fact strictly stronger than "the contract does
not supply it" **and** either decides a route (C4r/C4e, F11, (RIG)) for a named class or exposes a
hidden assumption. Favourable branches (any route that holds without A1) are pressure-tested at the node
where they occur.

## 2. Setting and hypotheses

**The update.** Fix $d\ge1$, an integer $q\ge2$ and a coefficient $\alpha\in\mathbb Z_q$. Each site
$z\in\mathbb Z^d$ carries a current value $u(z)$ and a previous value $v(z)$ in $\mathbb Z_q$. With
$(Sf)(z)=\sum_{j=1}^d\bigl(f(z+e_j)+f(z-e_j)\bigr)$,
$$
F(u,v)=(\alpha Su-v,\ u),\qquad F^{-1}(u,v)=(v,\ \alpha Sv-u),
$$
i.e. $x(t+1)=\alpha Sx(t)-x(t-1)$. On $\Omega=(\mathbb Z_q^2)^{\mathbb Z^d}$ (product topology) $F$ is a
group automorphism, and each output coordinate of $F^{\pm1}$ is a finite linear combination of input
coordinates. The torus version replaces $\mathbb Z^d$ by $(\mathbb Z/L)^d$.

**Readout and rooted maps.** A window is a finite nonempty $W\subset\mathbb Z^d$. The visible value is
$\pi(u,v)=(u,v)|_W\in V:=(\mathbb Z_q^2)^W$, $n=2|W|$; the hidden coordinates are all others,
$H=\{x\in \Omega:\pi x=0\}$, so $\Omega=V\times H$. With a hidden prior $\rho$ shared by every root, Main's rooted
maps are $\Gamma_t(a,b)=\rho\{h:\pi F^t(a,h)=b\}$ (Main.md:135). Total variation $d$, P-divisibility on
$\{0,\dots,n\}$, C4r and C4e are as in Main.md:119, :135 and CausalReadback.lean:54–68. Write
$d_t(a,b)=d(\Gamma_t(a,\cdot),\Gamma_t(b,\cdot))$.

**Notation.** $L_t:V\to V$, $L_t\delta=\pi F^t(\delta,0)$; $K_t=\pi F^t(H)\subset V$ (a subgroup);
$N_t=L_t^{-1}(K_t)$. $\Pi_W$ is the group of characters of $\Omega$ supported on window coordinates
($\Pi_W\cong\widehat V$). For $\ell\in\mathbb Z^d$, $\deg_\ell$ of a nonzero Laurent polynomial
$f\in\mathbb Z_q[x_1^{\pm1},\dots,x_d^{\pm1}]$ is $\max\{\ell\cdot z: f_z\ne0\}$, and
$\deg_\ell 0=-\infty$. $\operatorname{ext}_j(W)=\max_W z_j-\min_W z_j$. $W$ is **lattice-convex** if
$W=\operatorname{conv}(W)\cap\mathbb Z^d$ (boxes and single sites are).

**Hypotheses.**

| Label | Statement | Status |
|---|---|---|
| (U) | The update is $x(t+1)=\alpha Sx(t)-x(t-1)$ over $\mathbb Z_q$ with $S$ the nearest-neighbour sum | On `main`: Main.md:728 item (xiii) (second-order form, finite abelian group per site; kernel `ruleDynamics`), SM.md:224–228 (form lemma: center-free, cubic-isotropic, linear, "for one coefficient $\alpha$"), Substratum.md:159; the instance $q=2$, $\alpha=1$ at Main.md:292. Linearity (A5) is ledger item (vii), Main.md:728. Posit of the selected lattice model, not derived (Main.md:728 (xiii)) |
| (Λ) | Carrier $\mathbb Z^d$ (infinite) in place of A4's finite periodic lattice | Posited for this check (the A1-free carrier of the question). A4 (Substratum.md:98) states a finite periodic lattice; SM.md:222 represents the substratum by $\mathbb Z^d$. Not adopted here as physics |
| (Q) | $q$ prime and $\alpha\ne0$ | Used only where marked (nodes 3, 4, 6 and §4). Main.md:292 ($q=2$), Main.md:324 and Main.md:728 item (v) work at prime $q$; main does not fix $q$ or $\alpha$ for the substratum (SM.md:230, coefficient's reading) |
| (NN) | $\alpha$ is not nilpotent in $\mathbb Z_q$ ($\alpha^t\not\equiv0$ for all $t$; for prime $q$: $\alpha\ne0$) | Used where marked; its negation is the branch of node 5 |
| (Haar) | Hidden prior $\rho$ = uniform product law on hidden coordinates; equivalently the invariant law is Haar measure $\mu$ on $\Omega$ | Posited for this check as the natural infinite-volume law; justified as the weak limit of the uniform laws on cubic tori $(\mathbb Z/L)^d$, a subclass of A4's periodic lattices (Prop. 4.3) and as the counterpart of Main Lemma 3's counting measure (Main.md:54, :58). Non-product invariant laws are not treated (§5) |
| (R) | Window readout $\pi=(u,v)\vert_W$, $W$ finite | On `main` as the readout of Main §3.2 ("the visible sector being the sites of a region $R$", Main.md:292, with $s=2\lvert R\rvert$). Other readouts: §5 |
| (LC) | $W$ lattice-convex | Used only in Theorem 3.3 |

**Results on `main` used.** Rooted maps and P-divisibility (Main.md:135); C4r ⇒ P-indivisible
(`c4r_implies_pIndivisible`, CausalReadback.lean:134; finite $V$, real matrices, no carrier, prior or
reversibility); C4e ⇒ P-indivisible (`c4e_implies_pIndivisible`, CausalReadback.lean:148); ladder F11
(PREMISE-LADDER.md:59, :93–105); REC-1 Lemma 3.1 and Props. 3.2, 3.4, 3.8; the finite-carrier theorems of
Main.md:113–145.

**Standard facts used** (each also proved inline where short). (S1) A translation-invariant probability
on a product of finite groups is the uniform product law (proof: for a finite coordinate set $C$, the
translations supported on $C$ act transitively on the cylinders over $C$). (S2) The pushforward of a
uniform law on a finite group under a homomorphism is uniform on the image (fibres are cosets of the
kernel). (S3) Linear duality over the field $\mathbb F_q$: $(\ker\phi)^\perp=\operatorname{im}\phi^*$,
$N^{\perp\perp}=N$. (S4) $\mathbb F_q[x_1^{\pm1},\dots,x_d^{\pm1}]$ is an integral domain, so for every
$\ell$ the $\ell$-leading form of a product is the product of the $\ell$-leading forms. (S5) A point
outside a polytope with integer vertices is separated from it by an integer linear functional.

## 3. Nodes

### Node 1 — What the selected update is on `main`

1. *Form.* Main.md:728 item (xiii): "each site of (viii) carries a previous and a current value in a
   finite abelian group, and one step is $x(t+1)=F(x(t))-x(t-1)$ … the update displayed in §3.2 being its
   instance with $q=2$ and $F$ the nearest-neighbour sum". SM.md:224–228 selects $F=\alpha\sum_{\rm nn}$
   under center independence, cubic isotropy and linearity, "for one coefficient $\alpha$", and
   Substratum.md:159 repeats it. Main.md:292 displays $u'_x=\sum_{z\sim x}u_z+v_x$, $v'_x=u_x$ over
   $\mathbb F_2$, which is (U) with $q=2$, $\alpha=1$ (signs coincide mod 2).
2. *What is not fixed.* $q$ and $\alpha$ at substratum level: SM.md:230 places the normalization
   $\alpha=1/d$ at the observer level and notes that $1/d$ need not exist in $\mathbb Z_q$; Main.md:728
   item (v) speaks of prime $q$ for its shell statement; the rounded nonlinear rule of SM.md:294, :298 is
   a separate realization that does not inherit (A5) (SM.md:1416) and is not the selected linear update.
   The carrier: A4 (Substratum.md:98) takes a finite periodic lattice; no invariant law on an infinite
   lattice is selected on `main` (Main Lemma 3, Main.md:54, selects the counting measure of a finite
   carrier).
3. *Readout.* Main §3.2 reads all sites of a region (Main.md:292); the rooted maps are Main.md:135.

**Node 1 verdict.** The update is pinned on `main` up to the parameters $(q,\alpha)$ and the carrier;
the instance $q=2$, $\alpha=1$, $d=3$ is explicit. The question is answerable class by class in
$(q,\alpha)$ once (Λ) and (Haar) are posited; no PARKED outcome. Class: CONFIRMING (inventory), with one
assumption-watch marker: **main does not exclude nilpotent $\alpha$** (node 5).

### Node 2 — Exact structure of the rooted family on $\mathbb Z^d$ under Haar

**Lemma 2.1 (contract).** Under (U), (Λ), (Haar): $F$ is a bimeasurable bijection preserving Haar
measure $\mu$, and $\mu=\mathrm{Unif}(V)\otimes\rho$. So REC-1's (V)(M)(I)(P), hence (D), hold.

*Proof.* $F$ is an automorphism with continuous inverse (displayed in §2). For a translation by $g\in \Omega$,
$F_*\mu(A+g)=\mu(F^{-1}A+F^{-1}g)=\mu(F^{-1}A)$, so $F_*\mu$ is translation invariant and equals $\mu$ by
(S1). The product form is (S1) applied coordinatewise. $\square$

**Lemma 2.2 (coset form).** Under (U), (Λ), (Haar), (R), for every $t\ge0$ and root $a\in V$,
$\Gamma_t(a,\cdot)$ is the uniform law on the coset $L_ta+K_t$. Hence two rows are either equal or have
disjoint supports: $d_t(a,b)=0$ if $a-b\in N_t$ and $d_t(a,b)=1$ otherwise.

*Proof.* $\pi F^t(a,h)=L_ta+\pi F^t(0,h)$ by linearity. The map $h\mapsto\pi F^t(0,h)$ depends only on
the finitely many hidden coordinates within graph distance $t$ of $W$ (each step reads nearest
neighbours), which are independent and uniform under $\rho$; it is a homomorphism with image $K_t$, so
by (S2) its law is uniform on $K_t$. Two cosets of $K_t$ are equal or disjoint, and
$L_ta+K_t=L_tb+K_t$ iff $L_t(a-b)\in K_t$ iff $a-b\in N_t$. $\square$

**Proposition 2.3 (no near-return; F11 and (RIG) fail).** Under (U), (Λ), (Haar), (R), (NN) — any $q$ —
$K_t\ne\{0\}$ for every $t\ge1$. Consequently, for every $t\ge1$ and every root $c$,
$\Gamma_t(c,c)\le1/|K_t|\le1/2$; every $\Gamma_t$ ($t\ge1$) is a non-permutation; F11's hypothesis
$\Gamma_n(c,c)\ge1-\varepsilon$ with $2\varepsilon<m\le1$ fails at every $n\ge1$ for every pair; and
(RIG) fails along every sequence.

*Proof.* The $u$-component at time $t$ is $u_t=A_tu_0+B_tv_0$ with $A_t=p_t(\alpha S)$,
$B_t=-p_{t-1}(\alpha S)$, where, with $X:=\alpha S$, $p_{-1}=0$, $p_0=1$, $p_{k+1}=Xp_k-p_{k-1}$ (check: $A_1=\alpha S$,
$B_1=-1$, and both sequences satisfy the update's recursion). $p_t$ is monic of degree $t$ in $X$. As a
Laurent polynomial in the shifts, $S^k$ contains only monomials of $\ell^1$-length $\le k$, and in $S^t$
the monomial $x_1^t$ has coefficient $1$ (one nearest-neighbour walk of length $t$ from $0$ to $te_1$).
Hence the coefficient of $u_0(w+te_1)$ in $u_t(w)$ is $\alpha^t\ne0$ by (NN) ($S$ is symmetric, so the
coefficient of $u_0(z)$ in $u_t(w)$ is the coefficient of $x^{z-w}$ in $A_t$). Take $w\in W$ with
maximal first coordinate; for $t\ge1$, $w+te_1\notin W$ is a hidden coordinate, and setting it to $1$
and every other coordinate to $0$ gives $\pi F^t(0,h)\ne0$. So $K_t\ne\{0\}$, $|K_t|\ge2$, and by
Lemma 2.2 every row of $\Gamma_t$ is uniform on a set of size $\ge2$. F11 needs
$\Gamma_n(c,c)\ge1-\varepsilon>1/2$ (since $2\varepsilon<m\le1$), impossible. By REC-1 Lemma 3.1,
$\mu(C_a\triangle F^{-t}C_a)=2\nu(a)(1-\Gamma_t(a,a))\ge\nu(a)>0$ for all $t\ge1$, so (RIG) fails.
$\square$

**Lemma 2.4 (P-divisibility in the coset class).** Under the hypotheses of Lemma 2.2, the rooted family
is P-divisible on $\{0,\dots,n\}$ iff $N_s\subseteq N_t$ for all $0\le s<t\le n$. When it fails, it fails
by C4e (and hence C4r): a pair $a-b\in N_s\setminus N_t$ has $d_s(a,b)=0$ and $d_t(a,b)=1$. In this
class C4r, C4e and P-indivisibility within $n$ are equivalent, and $t\mapsto d_t(a,b)$ is
non-increasing for every pair iff $(N_t)$ is increasing.

*Proof.* ($\Leftarrow$) Given $s<t$ with $N_s\subseteq N_t$, define $\Lambda(y,\cdot)=\Gamma_t(a,\cdot)$
for $y\in L_sa+K_s$, and $\Lambda(y,\cdot)=\delta_y$ for $y$ in no such coset. It is well defined: if
$y$ lies in the cosets of $a$ and $b$, they coincide, so $a-b\in N_s\subseteq N_t$ and
$\Gamma_t(a,\cdot)=\Gamma_t(b,\cdot)$ (Lemma 2.2). Then
$(\Gamma_s\Lambda)(a,\cdot)=\sum_{y\in L_sa+K_s}|K_s|^{-1}\Gamma_t(a,\cdot)=\Gamma_t(a,\cdot)$, and
$\Lambda$ is row-stochastic. ($\Rightarrow$) If $\delta\in N_s\setminus N_t$, take $a=\delta$, $b=0$:
Lemma 2.2 gives $\Gamma_s(a,\cdot)=\Gamma_s(b,\cdot)$ and $\Gamma_t(a,\cdot)\ne\Gamma_t(b,\cdot)$, which
is C4e; `c4e_implies_pIndivisible` (CausalReadback.lean:148) gives P-indivisibility on $\{0,\dots,t\}$,
and `c4e_implies_c4r` (CausalReadback.lean:126) gives C4r. The last sentence is Lemma 2.2. $\square$

**Node 2 verdict.** For the selected update under Haar, rooted distinguishability takes only the
values $0$ and $1$, near-total return never occurs under (NN) (node 5 treats nilpotent $\alpha$), and every revival is a collision-then-separation
detected by the subgroups $N_t$. Class: NEW for F11 and (RIG) on the selected update (decided negative
for every finite window and every non-nilpotent $\alpha$), ELABORATING for Lemma 2.4.

### Node 3 — The revival route (primary target): no C4r/C4e on $\mathbb Z^d$ for lattice-convex windows

**Lemma 3.1 (duality).** Under (U), (Λ), (Haar), (R), (Q): $N_t=E_t^\perp$, where
$E_t:=\Pi_W\cap\widehat F^{\,t}(\Pi_W)$ and $\widehat F\chi=\chi\circ F$.

*Proof.* Identify $\lambda\in\widehat V$ with $\lambda\pi\in\Pi_W$. By (S3),
$N_t^\perp=(L_t^{-1}K_t)^\perp=L_t^*(K_t^\perp)$ (the kernel of $V\to V/K_t$, $\delta\mapsto L_t\delta+K_t$,
has annihilator the image of the dual map). Now $\lambda\in K_t^\perp$ iff the character
$\widehat F^{\,t}(\lambda\pi)=\lambda\pi F^t$ is trivial on $H$, i.e. supported on window coordinates,
i.e. $\widehat F^{\,t}(\lambda\pi)\in\Pi_W$; and then $L_t^*\lambda=\lambda\pi F^t(\cdot,0)$ is that same
element of $\Pi_W$. So $N_t^\perp=\{\widehat F^{\,t}\chi:\chi\in\Pi_W\}\cap\Pi_W=E_t$, and
$N_t=E_t^\perp$ by (S3). $\square$

**Lemma 3.2 (no bulging of the wave recursion).** Assume (Q). Let $X=\alpha\sum_j(x_j+x_j^{-1})$ in
$R=\mathbb F_q[x_1^{\pm1},\dots,x_d^{\pm1}]$ and let $g_{-1},g_0,\dots,g_t\in R$ satisfy
$g_{r+1}=Xg_r-g_{r-1}$. Then for every $\ell\in\mathbb Z^d\setminus\{0\}$ and $-1\le s\le t$,
$\deg_\ell g_s\le\max(\deg_\ell g_{-1},\deg_\ell g_t)$. Consequently every exponent occurring in $g_s$
lies in $\operatorname{conv}(\operatorname{supp}g_{-1}\cup\operatorname{supp}g_t)$.

*Proof.* Put $D_r=\deg_\ell g_r$ and $m=\deg_\ell X=\max_j|\ell_j|\ge1$; the $\ell$-leading form of $X$
is $\alpha\sum_{j:|\ell_j|=m}x_j^{\operatorname{sgn}\ell_j}\ne0$. (K1) If $g_r\ne0$ and $D_r+m>D_{r-1}$,
then by (S4) the leading form of $Xg_r$ is nonzero of degree $D_r+m$, and $g_{r-1}$ cannot cancel it:
$D_{r+1}=D_r+m$. Then $g_{r+1}\ne0$ and $D_{r+1}+m>D_r$, so (K1) applies again: $D$ increases strictly
from $r$ up to $t$. (K2) If $g_r=0$ then $g_{r+1}=-g_{r-1}$. If two consecutive $g$'s vanish, all
vanish and the claim is trivial. Fix $s\in[0,t]$. If some $r\in[0,s]$ has $g_r\ne0$ and
$D_r+m>D_{r-1}$, then by (K1) $D_s\le D_t$. Otherwise, if some $r\in[0,s-1]$ has $g_r=0$, then
$g_{r-1}\ne0$, $g_{r+1}=-g_{r-1}\ne0$ and $D_{r+1}+m>-\infty=D_r$, so $r+1\le s$ satisfies the first
case, a contradiction; hence every $r\in[0,s-1]$ has $g_r\ne0$ and $D_r\le D_{r-1}-m<D_{r-1}$, and
either $g_s=0$ or $D_s<D_{s-1}$ as well, so $D_s<D_{-1}$ or $D_s=-\infty$. The case $s=-1$ is trivial.
The convex-hull statement follows by (S5) applied to each exponent. $\square$

**Theorem 3.3 (monotone distinguishability; the revival route is closed).** Assume (U), (Λ), (Haar),
(R), (Q), (LC). Then $N_s\subseteq N_t$ for all $0\le s\le t$. Hence for every pair of roots
$t\mapsto d_t(a,b)$ is non-increasing, there is no C4r and no C4e at any horizon, and the rooted family
is P-divisible on $\{0,\dots,n\}$ for every $n$. Since $\Gamma_1$ is a non-permutation
(Prop. 2.3), the selected update on $\mathbb Z^d$ under Haar is a counterexample to "non-permutation
rooted map $\Rightarrow$ P-indivisible at some horizon" for every lattice-convex window.

*Proof.* By Lemmas 2.4 and 3.1 it suffices that $E_t\subseteq E_{t-r}$ for $0\le r\le t$. Let
$\eta\in E_t$: $\eta\in\Pi_W$ and $\eta=\widehat F^{\,t}\chi$ with $\chi\in\Pi_W$. Write characters as
pairs of finitely supported $\mathbb Z_q$-valued functions, $\chi(u,v)=\sum_z\Phi(z)u(z)+\Psi(z)v(z)$,
read as Laurent polynomials. Since $S$ is symmetric,
$\chi\circ F(u,v)=\sum_z(\alpha S\Phi+\Psi)(z)u(z)-\Phi(z)v(z)$, so
$\widehat F(\Phi,\Psi)=(X\Phi+\Psi,-\Phi)$. Put $\eta_r=\widehat F^{\,r}\chi=(\Phi_r,\Psi_r)$,
$g_r=\Phi_r$ ($r\ge0$) and $g_{-1}=-\Psi_0$. Then $\Psi_r=-g_{r-1}$ for $r\ge0$ and
$g_{r+1}=Xg_r-g_{r-1}$, and $\eta_r\in\Pi_W$ iff $\operatorname{supp}g_r,\operatorname{supp}g_{r-1}\subset W$.
From $\eta_0,\eta_t\in\Pi_W$, Lemma 3.2 and (LC) give $\operatorname{supp}g_r\subset W$ for
$-1\le r\le t$, so $\eta_r\in\Pi_W$ for $0\le r\le t$. Then $\eta=\widehat F^{\,t-r}\eta_r$ with
$\eta_r\in\Pi_W$, so $\eta\in E_{t-r}$. The counterexample sentence combines this with Prop. 2.3.
$\square$

**Corollary 3.4 (single site, explicit).** For $W=\{w\}$, any $q$ and $\alpha$ a unit of $\mathbb Z_q$:
with roots $a=(a_u,a_v)$, $\Gamma_0=I$,
$\Gamma_1(a,(y_u,y_v))=q^{-1}\,[y_v=a_u]$, and $\Gamma_t=J/q^2$ (every entry $q^{-2}$) for all $t\ge2$.
The family is P-divisible at every horizon although $\Gamma_1$ is not a permutation.

*Proof.* $u_1(w)=\alpha\sum_{z\sim w}u_0(z)-a_v$ is uniform (hidden neighbours, $\alpha$ a unit), and
$v_1(w)=u_0(w)=a_u$. For $t\ge2$, $u_0(w+te_1)$ enters $u_t(w)$ with coefficient $\alpha^t$ and does not
enter $v_t(w)=u_{t-1}(w)$ (graph distance $t>t-1$); $u_0(w+(t-1)e_1)$ enters $v_t(w)$ with coefficient
$\alpha^{t-1}$ and not $u_t(w)$, because every monomial of $A_t$ has $\ell^1$-length of the parity of
$t$. The two contributions $(\alpha^t,0)$ and $(0,\alpha^{t-1})$ generate $\mathbb Z_q^2$, so
$K_t=V$. Then $N_0=\{0\}\subseteq N_1=\{0\}\times\mathbb Z_q\subseteq N_t=V$, and Lemma 2.4 applies.
$\square$

This is the selected rule's own analogue of the ladder's Bernoulli control C−1 (PREMISE-LADDER.md:117–128)
and of the infinite-XOR record: the same matrix pattern ($\Gamma_t$ constant for $t\ge2$), here produced by
the update OI selects.

**Non-convex windows.** Lemma 3.2 places the intermediate supports in $\operatorname{conv}(W)$, not in
$W$, so Theorem 3.3 does not cover non-convex windows. Exact computation (§7, part A) over all horizons
listed finds $N_s\subseteq N_t$ for every listed non-convex window ($\{0,5\}$ and $\{0,1,4\}$ in $d=1$;
two-site windows in $d=2,3$ at separations up to $4$). This is a finite computation, not a theorem.

**Node 3 verdict.** For the selected update with prime $q$, $\alpha\ne0$, Haar prior and any
lattice-convex window on $\mathbb Z^d$ — in particular the explicit instance $q=2$, $\alpha=1$, $d=3$ —
rooted distinguishability is monotone non-increasing for every pair: no C4r, no C4e, no
P-indivisibility at any horizon. This is the counterexample the scope note names. Class: NEW (a decided
negative for the revival route on OI's own rule; REC-1's models, Prop. 3.3 and 3.5, were not of OI's
form).

*Pressure on this (unfavourable) branch.* (1) The verdict depends on (Haar); a non-product invariant
law could change it (§5). (2) It depends on the window readout; other readouts are not treated (§5).
(3) An independent brute-force enumeration on a torus (§7, part C), which uses no coset or duality
lemma, reproduces the predicted TV values $\{0,1\}$, the monotone segment and the revival time, and the
revival detector fires on tori (part B), so the absence of revivals on $\mathbb Z^d$ is not a detector
artefact.

### Node 4 — Comparison with cubic tori $(\mathbb Z/L)^d$ (a subclass of A4's periodic lattices)

**Proposition 4.1 (light-cone agreement).** Let the torus side $L$ satisfy
$\operatorname{ext}_j(W)+2t<L$ for every $j$. Then the rooted maps $\Gamma_r$, $0\le r\le t$, of the
torus (uniform prior) equal those of $\mathbb Z^d$ (Haar prior).

*Proof.* The visible values at time $r\le t$ depend on initial coordinates in $W+B_t$ ($B_t$ the
$\ell^1$-ball). Its coordinate extents are $\operatorname{ext}_j(W)+2t<L$, so it maps injectively to the
torus; the torus coefficients, which are sums of the $\mathbb Z^d$ coefficients over preimages, equal
them, and the coordinates involved are independent and uniform under both priors. $\square$

**Corollary 4.2 (where recurrence-scale witnesses live).** On the cubic torus $(\mathbb Z/L)^d$: (a) under (NN), any $n\ge1$ with
F11's near-return (in particular $\Gamma_n=I$) satisfies $n\ge(L-\max_j\operatorname{ext}_j(W))/2$; (b)
under (Q) and (LC), any C4r or C4e witness $(s,t)$ has $t\ge(L-\max_j\operatorname{ext}_j(W))/2$. Both
bounds diverge as $L\to\infty$: no near-return and no revival survives at a fixed time.

*Proof.* Below the bound Prop. 4.1 identifies the torus family with the $\mathbb Z^d$ family, where
Prop. 2.3 excludes (a) and Theorem 3.3 excludes (b) (a witness $(s,t)$ involves only times $\le t$).
$\square$

**Proposition 4.3 (Haar is the infinite-volume limit of the cubic-torus laws).** For every finite box
$B\subset\mathbb Z^d$ and every $L$ exceeding its coordinate extents, the uniform law on torus states,
lifted to $L$-periodic configurations of $\mathbb Z^d$, has uniform marginal on $B$. Hence these laws
converge to $\mu$ on every cylinder.

*Proof.* $B$ maps injectively into the torus. $\square$

*Computation (§7, part B).* On tori with a single visible site: $d=1$, $q=2$: order of $F$ is $2L$
($L$ odd) or $L$ ($L$ even) for $3\le L\le9$; the first $t\ge1$ with $K_t=0$ equals the order and is also
the first identity return; the first revival is at $(1,L)$ for odd $L$ and $(1,L-1)$ for even $L$, a
wave circumnavigating the torus, earlier than the order. $d=3$, $q=2$: orders $6,4,30$ at $L=3,4,5$,
first revivals at $t=3,3,15$. $d=3$, $q=3$, $\alpha=1$: orders $12,120$ at $L=4,5$, first revivals at
$t=11,40$. Every first revival respects Cor. 4.2, and $\dim K_t$ and $\dim N_t$ of the torus and
$\mathbb Z^d$ families agree for $t\le(L-1)/2$ in every case (equality of the families is Prop. 4.1).

**Node 4 verdict.** On cubic tori $(\mathbb Z/L)^d$ (a subclass of A4's periodic lattices) the selected
update reaches P-indivisibility through revivals and exact return, but never before the light-crossing
scale $(L-\operatorname{ext}W)/2$ (revivals: under (Q) and (LC)); as $L\to\infty$ the witnesses recede to
infinity and the $\mathbb Z^d$ limit has none (prime $q$, convex windows). The recurrence
route of Main.md:121, :135 is therefore genuinely a finite-$L$ effect for this dynamics. Class: NEW
(lower bound on the time of every recurrence-scale witness, for the selected update).

### Node 5 — Counterexample-first, and the favourable branches: nilpotent coefficient components

**Proposition 5.1 (exact global period on $\mathbb Z^d$).** If $\alpha\not\equiv0$ but $\alpha$ is
nilpotent in $\mathbb Z_q$ (every prime factor of $q$ divides $\alpha$; requires $q$ not squarefree,
e.g. $q=4$, $\alpha=2$), then $F^N=\mathrm{id}$ on all of $(\mathbb Z_q^2)^{\mathbb Z^d}$ for some
$N\ge1$. Under (Haar) and (R), $\Gamma_1$ is not a permutation and $\Gamma_N=I$: (RET), (PER), F11 with
$\varepsilon=0$, and P-indivisibility on $\{0,\dots,N\}$ (overlap-and-return, RecurrenceHorizon.lean:119)
hold with no finiteness of the carrier.

*Proof.* Let $\alpha^r\equiv0$. Then $X^r=\alpha^rS^r=0$, so $F$ acts on $\Omega$ through the matrix
$M=\bigl(\begin{smallmatrix}X&-1\\1&0\end{smallmatrix}\bigr)$ with entries in the ring
$\mathbb Z_q[X]$, which has at most $q^r$ elements. $\det M=1$, so $M$ lies in the finite group
$GL_2(\mathbb Z_q[X])$ and has finite order $N$. For $\Gamma_1$: a hidden neighbour $z$ of $w\in W$
contributes $\alpha u_0(z)$ to $u_1(w)$, uniform on the nonzero subgroup $\alpha\mathbb Z_q$, so
$K_1\ne\{0\}$. Since $|V/K_1|<|V|$, two distinct roots share a coset of $K_1$ (Lemma 2.2, which does not
use (Q)), so two rows of $\Gamma_1$ coincide and $\Gamma_1$ is not a permutation. $\square$

Computed (§7, part D) on $\mathbb Z^3$: $N=4$ for $(q,\alpha)=(4,2),(8,4),(12,6)$; $N=8$ for $(8,2)$;
$N=12$ for $(9,3)$.

*Maximum skepticism on this favourable branch.* (1) Every entry of $F^t$ is a polynomial in $X$ of
degree $<r$, so the value at a site depends on initial data within graph distance $r-1$ **for all
times**: the update has bounded causal support and no propagation (for $q=4$, $\alpha=2$, radius 1). It
cannot carry the wave propagation and dispersion that SM §4.1 attaches to the selected rule
(SM.md:230; Theorem 1, SM.md:278). (2) The period is a small constant independent of the lattice, so this is a
recurrence at accessible order rather than at a recurrence scale; it is finitely realizable in the sense
of Main.md:642. (3) The instance on `main` ($q=2$, $\alpha=1$) and the prime-$q$ statements
(Main.md:324; Main.md:728 item (v)) do not cover it (Main.md:324 states that composite $q$ "is not
covered"); nothing on `main` excludes it explicitly (assumption-watch: the form lemma, SM.md:224, admits
every $\alpha$). (4) For composite $q$, $\mathbb Z_q\cong\prod_p\mathbb Z_{p^{k_p}}$ and $F$, (Haar) and
(R) split over the primary components: $\Gamma_t=\bigotimes_p\Gamma^{(p)}_t$, $N_t=\prod_pN^{(p)}_t$. In
each component $\alpha$ is a unit, zero, or a nonzero nilpotent (needs $k_p\ge2$, $p\mid\alpha$). If it is
a nonzero nilpotent in some component, Prop. 5.1 applies there, $N^{(p)}_1\ne0=N^{(p)}_N$, and the full
family has a C4e witness at a lattice-independent time although $\alpha$ need not be nilpotent in
$\mathbb Z_q$ (computed, §7 part E: $q=12$, $\alpha=2$, $W=\{0\}$ and $W=\{0,1\}$ in $d=1$, witness
$(1,3)$); F11 still fails by Prop. 2.3. The witness is carried entirely by the bounded-support
component, dynamically decoupled from the propagating unit component. *Proof of the splitting.* The
Chinese remainder isomorphism acts sitewise and commutes with $F$ (integer coefficients), carries Haar
measure to the product of the components' Haar measures and the window readout to the product of the
components' readouts; so the rooted law of a root is the product of the components' rooted laws, two
rows coincide iff they coincide in every component, and $N_t=\prod_pN^{(p)}_t$. A $\delta$ whose
$p$-component lies in $N^{(p)}_1\setminus\{0\}$ and whose other components vanish lies in
$N_1\setminus N_N$ (since $\Gamma^{(p)}_N=I$ gives $N^{(p)}_N=0$), which is C4e by Lemma 2.4 (which does
not use (Q)). Controls (part E): $q=4$ and $q=8$ with $\alpha=2$ show the witness $(1,3)$, before the
exact return; $q=6$, $\alpha=2$ (components: zero and unit) shows none. **Verdict: these branches are
formally A1-free but carried by a non-propagating component; they are not credited as a recovery.**

The coupled case $\alpha=0$ is excluded: then $F(u,v)=(-v,u)$, every $\Gamma_t$ is a permutation, and
there is no (C1).

**Node 5 verdict.** Counterexample-first succeeds for prime $q$, $\alpha\ne0$ (Prop. 2.3, Thm 3.3,
Cor. 3.4). The A1-free positive branches are those in which $\alpha$ is a nonzero nilpotent in some
primary component of $\mathbb Z_q$ (Prop. 5.1, remark (4)); each witness is carried by a
non-propagating component. Class: NEW (assumption-watch marker: the selected-model posit
does not state that $\alpha$ is a unit or that $q$ is prime, and the A1-free recurrence verdict depends
on it).

### Node 6 — Verdicts per route and for the manuscript sites

| Route | Verdict on $\mathbb Z^d$ under (Haar), window readout | Exact obstruction / scope |
|---|---|---|
| C4r / C4e revival (primary) | **Fails** for prime $q$, $\alpha\ne0$, every lattice-convex window, every horizon (Thm 3.3); no revival found for the listed non-convex windows (computed). **Holds** at a lattice-independent time when $\alpha$ is a nonzero nilpotent in some primary component of $\mathbb Z_q$, even if $\alpha$ is not nilpotent in $\mathbb Z_q$ (node 5 remark (4); computed $q=12$, $\alpha=2$) | Monotone $N_t$ from the convexity of the dual wave recursion (Lemma 3.2). General non-convex windows and composite $q$ with unit components of prime-power order: open. Mixed-case witnesses are carried by a non-propagating component; not credited |
| F11 near-return with margin | **Fails** for every non-nilpotent $\alpha$, every $q$, every finite window, every $t\ge1$ (Prop. 2.3) | $\Gamma_t(c,c)\le1/2$ because hidden data always reach the window ($K_t\ne0$) |
| Exact return (RET), (PER) | Fail under (NN) (Prop. 2.3); **hold** when $\alpha$ is nilpotent or zero in every primary component and nonzero nilpotent in one (Prop. 5.1) | Nilpotent components have bounded causal support; not credited. In the mixed case (some unit component) they fail by Prop. 2.3 |
| Rigidity (RIG) | **Fails** under (NN) (Prop. 2.3); so REC-1 Prop. 3.4 is unavailable. REC-1 Prop. 3.8's zero-entropy constraint is not needed for this verdict | — |
| Cubic torus $(\mathbb Z/L)^d$, accessible time | Witnesses exist (exact return at the order; earlier revivals) but all at $t\ge(L-\operatorname{ext}W)/2$ (Cor. 4.2; revivals under (Q), (LC)) | Diverges with $L$; no fixed accessible time survives |

*Main.md:121, :129, :135–:145.* The finite-carrier theorems are unaffected (the torus computations
reproduce them). On $\mathbb Z^d$, for prime $q$, $\alpha\ne0$ and lattice-convex windows, the infinite-carrier
analogue of Main.md:139's equivalence (REC-1 Prop. 6.2, labels (a)–(c) there) loses (b)⇒(c), since
$\Gamma_1$ is a non-permutation and the family is P-divisible at every horizon (Thm 3.3); Main.md:139,
stated for a finite representative of order $L$, is not contradicted, and the new content is that OI's
own update is such an instance. Whether REC-1's (a), a readback gap, holds there was not computed.

*Main.md:155 ($t_R$).* The continuous-time paragraph conditions on a common near-total return at
$t_R$ and notes that Poincaré recurrence does not supply it. For the discrete selected update on
$\mathbb Z^d$ under Haar with $\alpha$ non-nilpotent there is no common near-total return at any $t\ge1$
(Prop. 2.3); Main.md:155's Hamiltonian statement itself is not tested. On tori, $t_R$ in the sense of $\Gamma_{t_R}=I$ equals the order of $F$ in
every computed case and is at least $(L-\operatorname{ext}W)/2$ (Cor. 4.2).

*Main.md:540–544 (accessible order, $k\tau_S\ll t_R$).* Condition (ii) concerns conditional memory, not
revival, and is not tested here. The revival route of this record has no witness of accessible order:
on $\mathbb Z^d$ none at all (prime $q$, $\alpha\ne0$, convex windows), on cubic tori none before $(L-\operatorname{ext}W)/2$ steps.

*book/ch18-beyond.md:170–172.* REC-1 (verdict U18) flagged that ch18:170, read as closing every route to
recurrence-scale P-indivisibility on an infinite hidden sector, was stronger than the record then
supported. For the selected update with prime $q$, $\alpha\ne0$, Haar prior and lattice-convex
windows, ch18:170's sentence holds in its strong form: on $\mathbb Z^d$ no rooted route (exact return,
near-return, rigidity or any revival) gives P-indivisibility. This supports the sentence for that class
only. It does not hold as stated when $\alpha$ is a nonzero nilpotent in some primary component of
$\mathbb Z_q$ (Prop. 5.1; node 5 remark (4)), nor for infinite carriers in general (REC-1 Prop. 3.4
under (RIG)). Finding for the coordinator; no
manuscript edit is made.

### Node 7 — Reproducible computation and controls

The script below uses only the Python standard library and exact integer arithmetic modulo $q$ (rank
computations over the prime field). On $\mathbb Z^d$ it is exact, because the visible values at time
$t$ depend on finitely many initial coordinates (those within graph distance $t$ of $W$), and it
enumerates exactly those. Run: `python3 nr1_probe.py` (about ten seconds).

- **Part A** prints, for each window, $\dim K_t$ and $\dim N_t$ for $t=0,\dots,T$ and the first pair
  $(s,t)$ with $N_s\not\subseteq N_t$ (a C4e witness by Lemma 2.4); "none" means none up to $T$.
- **Part B** (positive control for the detector, and node 4): tori; order of $F$, first $t$ with
  $K_t=0$, first $\Gamma_t=I$, first revival, and agreement with the $\mathbb Z^d$ family for
  $t\le(L-1)/2$.
- **Part C** (independent control, no use of Lemmas 2.2–3.1): brute-force enumeration of all $2^{12}$
  hidden states of the $d=1$ torus with $L=7$, $q=2$, $\alpha=1$, one visible site; prints the set of TV
  values over all pairs and times, monotonicity for $t\le3=(L-1)/2$, the first strict TV increase and
  the first identity time. Predicted by Lemma 2.2, Prop. 4.1 and Cor. 3.4: $\{0,1\}$, monotone, $7$,
  $14$ (part B's $(1,7)$ and order $14$).
- **Part D** (node 5): least $N$ with $F^N=\mathrm{id}$ on $\mathbb Z^3$ for nilpotent $\alpha$.
- **Part E** (node 5 remark (4)): composite $q$ in $d=1$, computed by direct convolution of the uniform
  hidden coordinates through the linear forms (no coset, subgroup or splitting lemma used), in exact
  rationals: $\min_c\Gamma_t(c,c)$ for $t=0,\dots,6$, the set of TV values and the first strict TV
  increase over all pairs of roots for $W=\{0\}$; for $W=\{0,1\}$ the pair of roots $0$ and
  $(u(0),v(0),u(1),v(1))=(0,6,0,0)$ up to $t=3$. Run time about ten seconds.

```python
# NR-1 exact probe: second-order rule x(t+1) = alpha*S x(t) - x(t-1) mod q,
# S = nearest-neighbour sum on Z^d (or the torus (Z/L)^d), window readout
# (current and previous value at every window site), Haar (uniform product) prior.
# Exact arithmetic: ranks over the prime field F_q (parts A, B); exact integer and rational
# arithmetic modulo composite q (parts D, E); no floating point.
import itertools, sys

def add(a, b, q, c=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = (r.get(k, 0) + c * v) % q
    return {k: v for k, v in r.items() if v}

def mulS(a, q, d, alpha, L=None):
    r = {}
    for k, v in a.items():
        for j in range(d):
            for s in (1, -1):
                kk = list(k); kk[j] += s
                if L: kk[j] %= L
                kk = tuple(kk)
                r[kk] = (r.get(kk, 0) + alpha * v) % q
    return {k: v for k, v in r.items() if v}

def plist(T, q, d, alpha, L=None):
    """P[t+2] = p_t for t = -2..T; p_{-2} = -1, p_{-1} = 0, p_0 = 1, p_{t+1} = alpha S p_t - p_{t-1}."""
    z = tuple([0] * d)
    P = [{z: q - 1}, {}, {z: 1}]
    for t in range(0, T):
        P.append(add(mulS(P[-1], q, d, alpha, L), P[-2], q, -1))
    return P

def rowsys(P, t, W, q, L=None):
    """Visible state at time t as linear forms in the initial data.
    Returns list of dicts: column key (z, comp) -> coefficient; rows (w,'u'), (w,'v')."""
    p = lambda k: P[k + 2]
    rows = []
    for w in W:
        for (Au, Bv) in ((p(t), p(t - 1)), (p(t - 1), p(t - 2))):
            r = {}
            for off, c in Au.items():
                z = tuple((w[i] + off[i]) % L if L else w[i] + off[i] for i in range(len(w)))
                r[(z, 'u')] = (r.get((z, 'u'), 0) + c) % q
            for off, c in Bv.items():
                z = tuple((w[i] + off[i]) % L if L else w[i] + off[i] for i in range(len(w)))
                r[(z, 'v')] = (r.get((z, 'v'), 0) - c) % q
            rows.append({k: v for k, v in r.items() if v})
    return rows

def echelon(vecs, q):
    """Row-reduce list of length-n vectors over F_q; return dict pivot -> normalized vector."""
    basis = {}
    for v in vecs:
        v = reduce_(v, basis, q)
        piv = next((i for i, x in enumerate(v) if x), None)
        if piv is None: continue
        inv = pow(v[piv], q - 2, q)
        v = [(x * inv) % q for x in v]
        for p2 in list(basis):
            b = basis[p2]
            if b[piv]:
                c = b[piv]; basis[p2] = [(bi - c * vi) % q for bi, vi in zip(b, v)]
        basis[piv] = v
    return basis

def reduce_(v, basis, q):
    v = list(v)
    for piv, b in basis.items():
        if v[piv]:
            c = v[piv]; v = [(vi - c * bi) % q for vi, bi in zip(v, b)]
    return v

def kernel(M, n, q):
    """Kernel of the map e_i -> M[i] (list of n image vectors), as a list of basis vectors of F_q^n."""
    # Gaussian elimination on augmented [image | identity]
    m = len(M[0]) if M else 0
    rows = [list(M[i]) + [1 if j == i else 0 for j in range(n)] for i in range(n)]
    r = 0
    for col in range(m):
        pr = next((i for i in range(r, n) if rows[i][col]), None)
        if pr is None: continue
        rows[r], rows[pr] = rows[pr], rows[r]
        inv = pow(rows[r][col], q - 2, q)
        rows[r] = [(x * inv) % q for x in rows[r]]
        for i in range(n):
            if i != r and rows[i][col]:
                c = rows[i][col]; rows[i] = [(a - c * b) % q for a, b in zip(rows[i], rows[r])]
        r += 1
    return [row[m:] for row in rows[r:]]

def analyse(d, W, q, alpha, T, L=None):
    Wset = set(W); n = 2 * len(W)
    vis = [(w, c) for w in W for c in ('u', 'v')]
    P = plist(T, q, d, alpha, L)
    out = []
    for t in range(T + 1):
        rows = rowsys(P, t, W, q, L)
        hidden = sorted({k for r in rows for k in r if k[0] not in Wset})
        Kgen = [[r.get(k, 0) for r in rows] for k in hidden]
        Kb = echelon(Kgen, q)
        Lt = [[r.get(vk, 0) for r in rows] for vk in vis]   # image of e_i (initial visible coordinate i)
        red = [reduce_(col, Kb, q) for col in Lt]
        N = kernel(red, n, q)
        out.append(dict(t=t, dimK=len(Kb), dimN=len(N), N=N, Kb=Kb, Lt=Lt))
    return out

def revivals(res, q):
    """All (s,t), s<t, with N_s not contained in N_t (C4e: collision at s, separation at t)."""
    bad = []
    for s in range(len(res)):
        for t in range(s + 1, len(res)):
            Kb, Lt = res[t]['Kb'], res[t]['Lt']
            for delta in res[s]['N']:
                img = [sum(delta[i] * Lt[i][j] for i in range(len(delta))) % q for j in range(len(Lt[0]))]
                if any(reduce_(img, Kb, q)):
                    bad.append((s, t, delta)); break
    return bad

def box(d, sides):
    return [tuple(x) for x in itertools.product(*[range(s) for s in sides])]


def brute_torus_1d(L, q, alpha, T):
    """Independent control: enumerate every state of the 1-d torus, single visible site 0
    (current u and previous v), hidden = all other coordinates, uniform prior."""
    from itertools import product
    roots = [(a, b) for a in range(q) for b in range(q)]
    G = {r: [dict() for _ in range(T + 1)] for r in roots}
    for hid in product(range(q), repeat=2 * (L - 1)):
        for (a, b) in roots:
            u = [a] + list(hid[:L - 1]); v = [b] + list(hid[L - 1:])
            for t in range(T + 1):
                key = (u[0], v[0]); G[(a, b)][t][key] = G[(a, b)][t].get(key, 0) + 1
                u, v = [(alpha * (u[(i - 1) % L] + u[(i + 1) % L]) - v[i]) % q for i in range(L)], u
    tot = q ** (2 * (L - 1))
    def tv(r, s, t):
        ks = set(G[r][t]) | set(G[s][t])
        return sum(abs(G[r][t].get(k, 0) - G[s][t].get(k, 0)) for k in ks) / (2 * tot)
    D = [{(r, s): tv(r, s, t) for r in roots for s in roots if r < s} for t in range(T + 1)]
    ident = [all(G[r][t].get(r, 0) == tot for r in roots) for t in range(T + 1)]
    return D, ident

from fractions import Fraction
from itertools import product

def pushforward(rows, W, q, root):
    """Exact law of the visible vector at time t for a given root: direct convolution over the
    independent uniform hidden coordinates (no coset or subgroup lemma used)."""
    Wset = set(W); vis = [(w, c) for w in W for c in ('u', 'v')]
    n = len(rows)
    base = tuple(sum(r.get(vk, 0) * root[i] for i, vk in enumerate(vis)) % q for r in rows)
    dist = {base: 1}
    hidden = sorted({k for r in rows for k in r if k[0] not in Wset})
    for k in hidden:
        col = [r.get(k, 0) for r in rows]
        nd = {}
        for y, m in dist.items():
            for h in range(q):
                z = tuple((y[i] + h * col[i]) % q for i in range(n))
                nd[z] = nd.get(z, 0) + m
        dist = nd
    tot = sum(dist.values())
    return {y: Fraction(m, tot) for y, m in dist.items()}

def tv(p, r):
    return sum(abs(p.get(k, 0) - r.get(k, 0)) for k in set(p) | set(r)) / 2

def study(q, alpha, W, T, all_pairs=True, pairs=None):
    d = len(W[0]); P = plist(T, q, d, alpha)
    roots = list(product(range(q), repeat=2 * len(W)))
    use = roots if all_pairs else sorted({x for pr in pairs for x in pr})
    G = []
    for t in range(T + 1):
        rows = rowsys(P, t, W, q)
        G.append({a: pushforward(rows, W, q, a) for a in use})
    diag = [min(G[t][c].get(c, 0) for c in use) for t in range(T + 1)]
    prs = [(a, b) for i, a in enumerate(use) for b in use[i + 1:]] if all_pairs else pairs
    D = [{pr: tv(G[t][pr[0]], G[t][pr[1]]) for pr in prs} for t in range(T + 1)]
    vals = sorted({v for t in range(T + 1) for v in D[t].values()})
    first = min(((s, t) for t in range(T + 1) for s in range(t) for pr in prs if D[t][pr] > D[s][pr]), default=None)
    return diag, vals, first

if __name__ == '__main__':
    print("== A. Z^d, Haar prior, window readout: dims of K_t and N_t; first collision-then-separation ==")
    cases = [
        (1, box(1, (1,)), 2, 1, 10), (1, box(1, (1,)), 3, 2, 10), (1, box(1, (1,)), 5, 2, 10),
        (1, box(1, (3,)), 2, 1, 10), (1, box(1, (5,)), 3, 1, 12),
        (2, box(2, (2, 2)), 3, 1, 8), (2, box(2, (3, 3)), 2, 1, 8),
        (3, box(3, (1, 1, 1)), 2, 1, 6), (3, box(3, (1, 1, 1)), 3, 1, 6),
        (3, box(3, (2, 2, 2)), 3, 2, 6), (3, box(3, (3, 3, 3)), 2, 1, 6),
        (1, [(0,), (5,)], 2, 1, 12), (1, [(0,), (1,), (4,)], 2, 1, 10),
        (2, [(0, 0), (1, 1)], 2, 1, 8), (2, [(0, 0), (3, 0)], 2, 1, 8),
        (3, [(0, 0, 0), (1, 1, 1)], 3, 1, 6), (3, [(0, 0, 0), (4, 0, 0)], 3, 2, 7),
    ]
    for d, W, q, alpha, T in cases:
        res = analyse(d, W, q, alpha, T)
        rv = revivals(res, q)
        first = min(rv, key=lambda x: (x[1], x[0])) if rv else None
        print(f"d={d} |W|={len(W)} W={W if len(W) < 4 else 'box'} q={q} alpha={alpha} "
              f"dimK={[r['dimK'] for r in res]} dimN={[r['dimN'] for r in res]} "
              f"revival={'none' if not first else first[:2]}")
    print("== B. Tori (Z/L)^d: order of F, first t>=1 with K_t = 0, first t with Gamma_t = I, first revival ==")
    for d, q, alpha, Ls in [(1, 2, 1, range(3, 10)), (1, 3, 1, range(3, 8)),
                            (2, 2, 1, range(3, 8)), (3, 2, 1, range(3, 6)), (3, 3, 1, range(4, 6))]:
        for L in Ls:
            zero = tuple([0] * d)
            P = plist(1, q, d, alpha, L); t = 1; order = None
            while t <= 4000:
                if P[t + 2] == {zero: 1} and P[t + 1] == {}:
                    order = t; break
                P.append(add(mulS(P[-1], q, d, alpha, L), P[-2], q, -1)); t += 1
            W = box(d, tuple([1] * d))
            res = analyse(d, W, q, alpha, order, L)
            dec = next((r['t'] for r in res[1:] if r['dimK'] == 0), None)
            ret = next((r['t'] for r in res[1:] if r['dimK'] == 0 and
                        all(r['Lt'][i][j] == (1 if i == j else 0) for i in range(2) for j in range(2))), None)
            rv = revivals(res, q)
            first = min(rv, key=lambda x: (x[1], x[0])) if rv else None
            inf = analyse(d, W, q, alpha, (L - 1) // 2)
            agree = all(res[t]['dimK'] == inf[t]['dimK'] and res[t]['dimN'] == inf[t]['dimN'] for t in range((L - 1) // 2 + 1))
            print(f"d={d} q={q} alpha={alpha} L={L} order={order} K_t=0 first at {dec}; Gamma_t=I first at {ret}; "
                  f"first revival {first[:2] if first else None}; torus=Z^d for t<=(L-1)//2: {agree}")
    print("== C. Independent brute-force control: 1-d torus L=7, q=2, alpha=1, single visible site ==")
    D, ident = brute_torus_1d(7, 2, 1, 14)
    vals = sorted({v for t in range(15) for v in D[t].values()})
    mono = all(D[t + 1][k] <= D[t][k] for t in range(3) for k in D[0])
    firstrev = min((t for t in range(1, 15) for s in range(t) for k in D[0] if D[t][k] > D[s][k]), default=None)
    print("TV values taken:", vals, "| TV non-increasing on t<=3:", mono,
          "| first t with a strict TV increase:", firstrev, "| first t>=1 with Gamma_t=I:", next(t for t in range(1, 15) if ident[t]))
    print("== D. Nilpotent coefficient: least N>=1 with F^N = id on all of Z^3 ==")
    for q, a in [(4, 2), (8, 2), (8, 4), (9, 3), (12, 6)]:
        z = (0, 0, 0); P = plist(1, q, 3, a); t = 1; order = None
        while t <= 60:
            if P[t + 2] == {z: 1} and P[t + 1] == {}:
                order = t; break
            P.append(add(mulS(P[-1], q, 3, a), P[-2], q, -1)); t += 1
        print(f"q={q} alpha={a}: F^N = id on Z^3 at N={order}")
    print("== E. Composite q, d = 1, Haar prior, direct pushforward (exact rationals) ==")
    for q, a, T in [(12, 2, 6), (6, 2, 6), (4, 2, 6), (8, 2, 6)]:
        diag, vals, first = study(q, a, [(0,)], T)
        print(f"q={q} alpha={a} W={{0}}: min_c Gamma_t(c,c) t=0..{T} = {[str(x) for x in diag]}; "
              f"TV values {[str(v) for v in vals]}; first strict TV increase {first}")
    # W = {0,1}, q = 12, alpha = 2: root pair (delta, 0) with delta = (u0,v0,u1,v1) = (0,6,0,0)
    delta = (0, 6, 0, 0); zero = (0, 0, 0, 0)
    diag, vals, first = study(12, 2, [(0,), (1,)], 3, all_pairs=False, pairs=[(zero, delta)])
    print(f"q=12 alpha=2 W={{0,1}} roots 0 and {delta}: TV values {[str(v) for v in vals]}; first strict TV increase {first}")
```

Expected output:

```
== A. Z^d, Haar prior, window readout: dims of K_t and N_t; first collision-then-separation ==
d=1 |W|=1 W=[(0,)] q=2 alpha=1 dimK=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] dimN=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] revival=none
d=1 |W|=1 W=[(0,)] q=3 alpha=2 dimK=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] dimN=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] revival=none
d=1 |W|=1 W=[(0,)] q=5 alpha=2 dimK=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] dimN=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] revival=none
d=1 |W|=3 W=[(0,), (1,), (2,)] q=2 alpha=1 dimK=[0, 2, 4, 5, 6, 6, 6, 6, 6, 6, 6] dimN=[0, 2, 4, 5, 6, 6, 6, 6, 6, 6, 6] revival=none
d=1 |W|=5 W=box q=3 alpha=1 dimK=[0, 2, 4, 6, 8, 9, 10, 10, 10, 10, 10, 10, 10] dimN=[0, 2, 4, 6, 8, 9, 10, 10, 10, 10, 10, 10, 10] revival=none
d=2 |W|=4 W=box q=3 alpha=1 dimK=[0, 4, 8, 8, 8, 8, 8, 8, 8] dimN=[0, 4, 8, 8, 8, 8, 8, 8, 8] revival=none
d=2 |W|=9 W=box q=2 alpha=1 dimK=[0, 8, 16, 17, 18, 18, 18, 18, 18] dimN=[0, 8, 16, 17, 18, 18, 18, 18, 18] revival=none
d=3 |W|=1 W=[(0, 0, 0)] q=2 alpha=1 dimK=[0, 1, 2, 2, 2, 2, 2] dimN=[0, 1, 2, 2, 2, 2, 2] revival=none
d=3 |W|=1 W=[(0, 0, 0)] q=3 alpha=1 dimK=[0, 1, 2, 2, 2, 2, 2] dimN=[0, 1, 2, 2, 2, 2, 2] revival=none
d=3 |W|=8 W=box q=3 alpha=2 dimK=[0, 8, 16, 16, 16, 16, 16] dimN=[0, 8, 16, 16, 16, 16, 16] revival=none
d=3 |W|=27 W=box q=2 alpha=1 dimK=[0, 26, 52, 53, 54, 54, 54] dimN=[0, 26, 52, 53, 54, 54, 54] revival=none
d=1 |W|=2 W=[(0,), (5,)] q=2 alpha=1 dimK=[0, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] dimN=[0, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] revival=none
d=1 |W|=3 W=[(0,), (1,), (4,)] q=2 alpha=1 dimK=[0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6] dimN=[0, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6] revival=none
d=2 |W|=2 W=[(0, 0), (1, 1)] q=2 alpha=1 dimK=[0, 2, 4, 4, 4, 4, 4, 4, 4] dimN=[0, 2, 4, 4, 4, 4, 4, 4, 4] revival=none
d=2 |W|=2 W=[(0, 0), (3, 0)] q=2 alpha=1 dimK=[0, 2, 4, 4, 4, 4, 4, 4, 4] dimN=[0, 2, 4, 4, 4, 4, 4, 4, 4] revival=none
d=3 |W|=2 W=[(0, 0, 0), (1, 1, 1)] q=3 alpha=1 dimK=[0, 2, 4, 4, 4, 4, 4] dimN=[0, 2, 4, 4, 4, 4, 4] revival=none
d=3 |W|=2 W=[(0, 0, 0), (4, 0, 0)] q=3 alpha=2 dimK=[0, 2, 4, 4, 4, 4, 4, 4] dimN=[0, 2, 4, 4, 4, 4, 4, 4] revival=none
== B. Tori (Z/L)^d: order of F, first t>=1 with K_t = 0, first t with Gamma_t = I, first revival ==
d=1 q=2 alpha=1 L=3 order=6 K_t=0 first at 6; Gamma_t=I first at 6; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=1 q=2 alpha=1 L=4 order=4 K_t=0 first at 4; Gamma_t=I first at 4; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=1 q=2 alpha=1 L=5 order=10 K_t=0 first at 10; Gamma_t=I first at 10; first revival (1, 5); torus=Z^d for t<=(L-1)//2: True
d=1 q=2 alpha=1 L=6 order=6 K_t=0 first at 6; Gamma_t=I first at 6; first revival (1, 5); torus=Z^d for t<=(L-1)//2: True
d=1 q=2 alpha=1 L=7 order=14 K_t=0 first at 14; Gamma_t=I first at 14; first revival (1, 7); torus=Z^d for t<=(L-1)//2: True
d=1 q=2 alpha=1 L=8 order=8 K_t=0 first at 8; Gamma_t=I first at 8; first revival (1, 7); torus=Z^d for t<=(L-1)//2: True
d=1 q=2 alpha=1 L=9 order=18 K_t=0 first at 18; Gamma_t=I first at 18; first revival (1, 9); torus=Z^d for t<=(L-1)//2: True
d=1 q=3 alpha=1 L=3 order=9 K_t=0 first at 9; Gamma_t=I first at 9; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=1 q=3 alpha=1 L=4 order=12 K_t=0 first at 12; Gamma_t=I first at 12; first revival (1, 11); torus=Z^d for t<=(L-1)//2: True
d=1 q=3 alpha=1 L=5 order=15 K_t=0 first at 15; Gamma_t=I first at 15; first revival (1, 5); torus=Z^d for t<=(L-1)//2: True
d=1 q=3 alpha=1 L=6 order=18 K_t=0 first at 18; Gamma_t=I first at 18; first revival (1, 17); torus=Z^d for t<=(L-1)//2: True
d=1 q=3 alpha=1 L=7 order=21 K_t=0 first at 21; Gamma_t=I first at 21; first revival (1, 7); torus=Z^d for t<=(L-1)//2: True
d=2 q=2 alpha=1 L=3 order=6 K_t=0 first at 6; Gamma_t=I first at 6; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=2 q=2 alpha=1 L=4 order=4 K_t=0 first at 4; Gamma_t=I first at 4; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=2 q=2 alpha=1 L=5 order=30 K_t=0 first at 30; Gamma_t=I first at 30; first revival (1, 15); torus=Z^d for t<=(L-1)//2: True
d=2 q=2 alpha=1 L=6 order=12 K_t=0 first at 12; Gamma_t=I first at 12; first revival (1, 11); torus=Z^d for t<=(L-1)//2: True
d=2 q=2 alpha=1 L=7 order=126 K_t=0 first at 126; Gamma_t=I first at 126; first revival (1, 63); torus=Z^d for t<=(L-1)//2: True
d=3 q=2 alpha=1 L=3 order=6 K_t=0 first at 6; Gamma_t=I first at 6; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=3 q=2 alpha=1 L=4 order=4 K_t=0 first at 4; Gamma_t=I first at 4; first revival (1, 3); torus=Z^d for t<=(L-1)//2: True
d=3 q=2 alpha=1 L=5 order=30 K_t=0 first at 30; Gamma_t=I first at 30; first revival (1, 15); torus=Z^d for t<=(L-1)//2: True
d=3 q=3 alpha=1 L=4 order=12 K_t=0 first at 12; Gamma_t=I first at 12; first revival (1, 11); torus=Z^d for t<=(L-1)//2: True
d=3 q=3 alpha=1 L=5 order=120 K_t=0 first at 120; Gamma_t=I first at 120; first revival (1, 40); torus=Z^d for t<=(L-1)//2: True
== C. Independent brute-force control: 1-d torus L=7, q=2, alpha=1, single visible site ==
TV values taken: [0.0, 1.0] | TV non-increasing on t<=3: True | first t with a strict TV increase: 7 | first t>=1 with Gamma_t=I: 14
== D. Nilpotent coefficient: least N>=1 with F^N = id on all of Z^3 ==
q=4 alpha=2: F^N = id on Z^3 at N=4
q=8 alpha=2: F^N = id on Z^3 at N=8
q=8 alpha=4: F^N = id on Z^3 at N=4
q=9 alpha=3: F^N = id on Z^3 at N=12
q=12 alpha=6: F^N = id on Z^3 at N=4
== E. Composite q, d = 1, Haar prior, direct pushforward (exact rationals) ==
q=12 alpha=2 W={0}: min_c Gamma_t(c,c) t=0..6 = ['1', '0', '1/36', '0', '1/9', '0', '1/36']; TV values ['0', '1']; first strict TV increase (1, 3)
q=6 alpha=2 W={0}: min_c Gamma_t(c,c) t=0..6 = ['1', '0', '1/9', '0', '1/9', '0', '1/9']; TV values ['0', '1']; first strict TV increase None
q=4 alpha=2 W={0}: min_c Gamma_t(c,c) t=0..6 = ['1', '0', '1/4', '0', '1', '0', '1/4']; TV values ['0', '1']; first strict TV increase (1, 3)
q=8 alpha=2 W={0}: min_c Gamma_t(c,c) t=0..6 = ['1', '0', '1/16', '0', '1/4', '0', '1/16']; TV values ['0', '1']; first strict TV increase (1, 3)
q=12 alpha=2 W={0,1} roots 0 and (0, 6, 0, 0): TV values ['0', '1']; first strict TV increase (1, 3)
```

Control verdicts: part B's detector finds a revival on every torus (positive control); part E finds
the predicted witness $(1,3)$ for $q=4,8,12$ with $\alpha=2$ and none for $q=6$, $\alpha=2$; part C agrees
with the linear-algebra predictions in every printed quantity (independent control); part A's
convex-window rows agree with Theorem 3.3 (no revival), and its $\dim K_t\ge1$ for $t\ge1$ agrees with
Prop. 2.3. The verdicts above are stated from these measurements and the proofs; none is rendered over a
failed control.

## 4. Result

1. **Selected update pinned.** On `main` the selected update is $x(t+1)=\alpha Sx(t)-x(t-1)$ over
   $\mathbb Z_q$ with $S$ the nearest-neighbour sum (Main.md:728 (xiii), SM.md:224–228), explicit at
   $q=2$, $\alpha=1$ (Main.md:292); $q$, $\alpha$ and an infinite-lattice law are not fixed on `main`.
2. **F11 fails without A1.** On $\mathbb Z^d$ with the Haar (uniform product) law, the infinite-volume
   limit of the uniform laws on cubic tori, and any finite window readout, for every non-nilpotent $\alpha$: every
   rooted row at every $t\ge1$ is uniform on a coset of a nonzero subgroup, so
   $\Gamma_t(c,c)\le1/2$; F11's near-return with margin, exact return and rigidity all fail
   (Prop. 2.3).
3. **The revival route fails too (primary target).** In this class rooted distinguishability takes
   only the values $0,1$, and P-indivisibility is equivalent to a collision-then-separation
   (Lemma 2.4). For prime $q$, $\alpha\ne0$ and every lattice-convex window, distinguishability is
   monotone non-increasing for every pair at every time: no C4r, no C4e, P-divisible at every horizon,
   although $\Gamma_1$ is a non-permutation (Thm 3.3; single site explicit in Cor. 3.4). OI's own rule
   is therefore a counterexample to the revival route on an infinite lattice under the natural law.
   Non-convex windows: no revival in the exact computations listed; general case open.
4. **Tori.** On cubic tori $(\mathbb Z/L)^d$ (a subclass of A4's periodic lattices) every near-return
   and every revival (prime $q$, convex windows) occurs at
   $t\ge(L-\operatorname{ext}W)/2$ (Cor. 4.2); computed first revivals are wave circumnavigations at
   $t\approx L$ in $d=1$, before the exact return at the order of $F$. No witness survives at a fixed
   time as $L\to\infty$.
5. **A1-free positive branches.** When $\alpha$ is a nonzero nilpotent in some primary component of
   $\mathbb Z_q$ (some prime $p$ with $p^{k}\,\Vert\,q$, $k\ge2$, $p\mid\alpha$ and $p^{k}\nmid\alpha$; e.g. $q=4,\alpha=2$, or
   $q=12,\alpha=2$; not $q=12,\alpha=4$, whose $\mathbb Z_4$ component is zero), a C4e witness occurs on $\mathbb Z^d$ at a lattice-independent time; when every
   component is nilpotent or zero, $F^N=\mathrm{id}$ (Prop. 5.1). The witness lives in a component with
   bounded causal support; these branches lie outside the explicit instance and the prime-$q$
   statements on `main`, and are not credited.
6. **Consequence.** For prime $q$ and $\alpha\ne0$ (the class of the explicit instance),
   recurrence-scale P-indivisibility does not hold A1-free under (Haar) with a window readout, and for
   lattice-convex windows no rooted P-indivisibility holds at all. For every $q$ and non-nilpotent
   $\alpha$, near-return, exact return and rigidity fail (Prop. 2.3), but a revival can occur
   (Result 5). Total finiteness (or another source of a
   common return) remains load-bearing for this conclusion, as Main.md:113–129 and ch18:170 state.
7. A1 remains open and unadopted; A4 is unchanged; physical source NOT PASSED. No manuscript, Lean or
   registry edit.

**Hypothesis ledger.** (U): on `main` (Main.md:728 (xiii); SM.md:224–228; Substratum.md:159; instance
Main.md:292), a posit of the selected model. (Λ): posited for this check. (Q), (NN), (LC): conditions of
the stated propositions; (Q) holds in the instance on `main`. (Haar): posited; proved to be the
cylinder limit of the cubic-torus uniform laws (Prop. 4.3) and invariant (Lemma 2.1). (R): on `main` as Main
§3.2's region readout. (S1)–(S5): standard, short proofs or textbook linear algebra; (S4) is the
integral-domain property of Laurent polynomial rings over a field. Kernel theorems:
`c4r_implies_pIndivisible` (CausalReadback.lean:134), `c4e_implies_pIndivisible` (:148),
`c4e_implies_c4r` (:126), overlap-and-return (RecurrenceHorizon.lean:119), on `main`. New statements
(Lemmas 2.1–2.4, 3.1–3.2, Thm 3.3, Cor. 3.4, Props. 4.1–4.3, Cor. 4.2, Prop. 5.1 with the primary-component splitting of node 5 remark (4)): proved here on paper,
not kernel-certified. Supply of (Λ) or (Haar) by nature: open.

**Productivity outcome (§A.31).** NEW: Prop. 2.3 (F11, exact return and rigidity decided negative for
the selected update), Thm 3.3 with Cor. 3.4 (revival route decided negative for convex windows; the
selected update's own counterexample), Cor. 4.2 (light-crossing lower bound on every torus witness),
Prop. 5.1 with node 5 remark (4) (assumption-watch: a nonzero nilpotent coefficient in some primary
component of $\mathbb Z_q$ gives a revival on $\mathbb Z^d$ even when $\alpha$ is not nilpotent).
ELABORATING: Lemma 2.4, Lemma 3.1, Props. 4.1,
4.3. CONFIRMING: node 1. One depth-first pass was made; the fixed-point criterion of 3–4 passes without
NEW findings is not claimed. Cross-propagation marker: any A1-free claim about the selected update must
state its law, its readout geometry, whether $q$ is prime, and how $\alpha$ reduces in each primary
component of $\mathbb Z_q$.

## 5. Open questions

1. Non-convex windows: whether $N_s\subseteq N_t$ holds for every finite $W$ (computed instances say
   yes; Lemma 3.2 gives only the convex hull).
2. Other readouts: non-linear coarse-grainings of window data, and linear readouts that do not split
   as $V\times H$ coordinates. Whether Prop. 2.3 extends to every nonzero finitely supported linear
   readout is not proved here.
3. Other invariant laws on $\mathbb Z^d$: non-product translation-invariant laws, and laws concentrated
   on spatially periodic configurations (which reproduce a finite torus and so reintroduce total
   finiteness under another name).
4. Composite $q$: Prop. 2.3 holds for non-nilpotent $\alpha$, and the mixed case has revivals (node 5
   remark (4)). Whether Theorem 3.3 extends to unit components of prime-power order is open: its proof
   uses (S4) over a field, and the expected route (McCoy's theorem in place of (S4) and finite-group
   duality in place of (S3)) is not written out here. An exact characterization of the windows with
   monotone $N_t$ is likewise open.
5. Whether a readback gap (C4 memory) holds on $\mathbb Z^d$ for the selected update; it would give
   accessible conditional memory with a P-divisible rooted family, as in Main's XOR control.
6. Whether the selected-model posit (Main.md:728 (xiii)) should state that $q$ is prime, or that
   $\alpha$ is a unit in every primary component of $\mathbb Z_q$; this decides whether the branches of
   Prop. 5.1 and node 5 remark (4) belong to the selected class.
