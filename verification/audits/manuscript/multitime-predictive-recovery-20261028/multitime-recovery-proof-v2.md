# Multitime recovery: conditional predictive uniqueness and native quotient identification

Version 2 proof candidate, 2026-10-28. Version 1 bytes are preserved; the v2 addition is §4.5 and its exact quotient-ray/Hankel controls. Source checkpoint: `7c464fcffcdd785c96a646e109433d3377bcfaad`. This document does not amend a manuscript, run a frozen investigation, or assign an acceptance/evidence status. The independent review is separate.

## Result and exact boundary

There are two useful recoveries.

1. Complete freely composable word statistics determine a finite-dimensional reachable and observable **linear predictive realization** up to a unique invertible similarity. If competing dimensions are $n,m$, statistics through length $n+m-1$ suffice. For known minimal dimension $d>0$, a Hankel reconstruction uses prefixes and suffixes of lengths at most $d-1$, plus one intervening letter, hence statistics through $2d-1$.
2. For the native special case of one fixed finite permutation, a passive deterministic visible readout, and a globally full-support initial distribution, the law determines the **future-trace quotient** as a labelled finite permutation with its pushed-forward initial distribution. With a known bound $B\ge2$ on both quotient sizes, length-$(B-1)$ and length-$B$ blocks suffice. The single-state case needs one-letter data. No stationarity of the initial distribution is needed.

The first result is standard realization theory, with its proof and access requirements made explicit here. The second is a finite-state refinement of the repository's existing canonical predictive quotient, not a claim of a newly discovered physical uniqueness principle. Neither identifies unobservable microscopic fibres, the preferred visible/hidden tensor factorization, or the allowed physical gauge group. In particular, these word probabilities are not the coherent block-word traces assumed in Proposition 24.2.

## Existing corpus and what this certificate adds

The pinned `papers/Main.md`, §3.4, already contains the theorem headed “canonical predictive quotient — a purification ingredient, substratum form” (line 616 in the exact pinned file). For a finite-horizon trajectory law it constructs a staged tail predictor, gives the canonical visible-preserving and dynamics-intertwining map from every faithful completion on the prior-supported reachable part, and distinguishes quotient uniqueness from freedom of the hidden fibres. Its history-ledger extension is reversible. `foundations/purification_probes.py` already checks that construction on 2,928 exact realization/prior instances. Those are existing results, not recoveries claimed by this note.

The pinned `papers/Substratum.md`, Proposition 24.2, and `OIBridge/WordTraceSufficiency.lean` already supply a different rigidity theorem: equality of all traces of words in visible blocks and their adjoints, together with source block-word spanning, gives hidden-unitary conjugacy. The target spanning conclusion is part of that result. Equality of separate one-time visible channels, or even the passive scalar probabilities below, does not supply those hypotheses. The single-time counterexample remains respected.

The documentary scope of frozen 24.1B and the algebraic scope of frozen 24.1C were read to avoid conflating their proof obligations with this scratch work. Neither protocol was executed or changed.

This certificate adds a self-contained minimal-linear proof, exact finite access bounds, a countercontrol separating linear similarity from physical gauge, and a sharper native all-time quotient identification lemma with a finite state bound. The native lemma removes the stage ledger when one **already assumes** a single fixed finite reversible carrier and has enough passive records to identify its predictive states. It does not infer that fixed all-time carrier from arbitrary finite-horizon data.

Source bytes, Git blob IDs, and SHA-256 values are listed in `source-manifest.json`; copies under `sources/` are from the pinned checkpoint, not the concurrently edited working tree.

## 1. Word convention and hypotheses

Let $K$ be a field and $\mathcal A$ a finite alphabet. A realization is

\[
\mathcal R=(E,a,b,(M_c)_{c\in\mathcal A}),
\qquad s(w)=bM_wa,
\]

where $E$ is finite-dimensional, $a\in E$, $b\in E^*$, and each $M_c\in\operatorname{End}(E)$. For the chronological word $w=c_1\cdots c_k$, define $M_w=M_{c_k}\cdots M_{c_1}$, and $M_\epsilon=I$. Thus $M_{wu}=M_uM_w$. A continuation $u$ follows a prefix $w$.

Reachability means $\operatorname{span}\{M_wa:w\in\mathcal A^*\}=E$. Observability means $\bigcap_{u\in\mathcal A^*}\ker(bM_u)=\{0\}$. These are **linear-span** conditions, not assertions that every normalized state can be physically prepared or every positive effect implemented.

Every word must be admissible in the same stationary realization: the operator for a letter is fixed across positions, and arbitrary prefixes and suffixes can be concatenated. For controlled experiments a letter may include an action and its recorded outcome; use its unnormalized linear update, not a nonlinear normalized posterior update. A protocol grammar, an external clock, a changing apparatus, or inaccessible reset history can invalidate this free-word model. One must first include the necessary controller/clock/memory in the state, with the resulting finite dimension bound, or prove a version for the actual admissible language. No bound here automatically applies to unaugmented, time-dependent experiments.

In a probabilistic column-state realization one additionally has $M_c\ge0$, $a\ge0$, $b=\mathbf1^T$, $\mathbf1^Ta=1$, and $\mathbf1^T\sum_cM_c=\mathbf1^T$. The algebraic theorem does not need positivity. Exact word values are assumed; finite noisy samples alone do not establish its equalities or its rank bound.

## 2. Minimal-realization uniqueness

**Theorem L.** Let $\mathcal R,\mathcal R'$ be reachable and observable finite-dimensional realizations with $s(w)=s'(w)$ for every word. Then they have the same dimension and there is exactly one linear isomorphism $S:E\to E'$ satisfying

\[
Sa=a',\qquad SM_c=M_c'S\quad(c\in\mathcal A),\qquad b'S=b.
\]

It is given, on any finite linear combination of reachable vectors, by

\[
S\!\left(\sum_i t_iM_{w_i}a\right)=\sum_i t_iM'_{w_i}a'.
\]

**Proof.** Suppose $\sum_i t_iM_{w_i}a=0$, and write $z'=\sum_i t_iM'_{w_i}a'$. For every continuation $u$,

\[
b'M'_uz' =\sum_i t_is'(w_iu)
=\sum_i t_is(w_iu)
=bM_u\sum_i t_iM_{w_i}a=0.
\]

Target observability gives $z'=0$, proving well-definedness. Source reachability makes the formula a map on all of $E$. Reverse the two models to construct a well-defined map $T:E'\to E$; on each reachable generator $TS(M_wa)=M_wa$ and $ST(M'_wa')=M'_wa'$. Reachability makes $TS=I_E$, $ST=I_{E'}$. Hence $S$ is invertible and dimensions agree.

The empty word gives $Sa=a'$. Appending a letter gives

\[
SM_cM_wa=SM_{wc}a=M'_{wc}a'=M'_cSM_wa,
\]

so reachability proves intertwining on all of $E$. Word equality with no continuation gives $b'S(M_wa)=bM_wa$, hence $b'S=b$. Any other intertwiner carrying $a$ to $a'$ must agree on every $M_wa$, so is $S$. Conversely, these three identities imply all word equalities by induction. $\square$

If either model is nonminimal, the correct statement first restricts to its reachable subspace and quotients by the subspace invisible to all continuations. There is no uniqueness claim about discarded states. The exact controls below separately show failure when observability or reachability is omitted.

## 3. Finite access bounds and Hankel construction

### 3.1 Comparison at dimensions $n,m$

For any $N$-dimensional realization with nonzero initial vector, let

\[
R_k=\operatorname{span}\{M_wa:|w|\le k\}.
\]

Then $R_{k+1}=R_k+\sum_cM_cR_k$. If $R_k=R_{k+1}$, the subspace is invariant under every letter, so the filtration has already stabilized. Otherwise dimension increases. Starting at dimension one, it must stabilize by $R_{N-1}$. A zero initial vector is immediate.

For two realizations of dimensions $n,m\ge1$, form the discrepancy realization

\[
\widetilde M_c=M_c\oplus M'_c,\quad
\widetilde a=(a,a'),\quad
\widetilde b=(b,-b').
\]

It has dimension $N=n+m$ and word value (s(w)-s'(w)). If this vanishes for every $|w|\le n+m-1$, its evaluation annihilates $R_{N-1}=R_\infty$. Therefore it vanishes for every word. No positivity or minimality is needed for this comparison bound.

The assumption is a known finite **upper bound on the competing realization dimensions**. Equality of finitely many observations without such a bound does not prove global equivalence. In particular, observed finite Hankel rank is a lower bound on full Hankel rank unless a dimension/rank upper bound is independently justified.

### 3.2 Reconstruction at known minimal rank $d>0$

For a reachable and observable $d$-dimensional realization, the reachability argument chooses $d$ prefix words $w_1,\ldots,w_d$, all of length at most $d-1$, for which the columns of

\[
R=[M_{w_1}a\ \cdots\ M_{w_d}a]
\]

are a basis. Applying the same filtration argument to the row span chooses suffixes $u_1,\ldots,u_d$ of lengths at most $d-1$ for which the rows of $O=[bM_{u_i}]_i$ are a basis. The Hankel block and its one-letter extensions are

\[
H_{ij}=s(w_ju_i)=(OR)_{ij},\qquad
(H_c)_{ij}=s(w_jcu_i)=(OM_cR)_{ij}.
\]

Both $O,R$ are invertible, hence so is $H$. Therefore the realization in reachable-basis coordinates is computed directly from these scalar word values:

\[
\widehat M_c=H^{-1}H_c=R^{-1}M_cR,\quad
\widehat a=H^{-1}(s(u_i))_i=R^{-1}a,\quad
\widehat b=(s(w_j))_j=bR.
\]

The longest queried word has length $(d-1)+1+(d-1)=2d-1$. The order $H^{-1}H_c$, not $H_cH^{-1}$, follows from the stated chronological convention. The factorization also proves that the infinite Hankel matrix has rank exactly $d$: its rank is at most $d$, and this $d\times d$ minor is invertible. This is why “minimal dimension” and “Hankel rank” coincide here.

This construction needs the required prefixes, suffixes, and their one-letter extensions to be accessible. If only selected interventions or restricted words are available, linear reachability/observability for the free alphabet is not established by naming it. For a model known to have dimension at most $d$, agreement through $2d-1$ identifies its series among all such competitors. If only a larger upper bound $D\ge d$ is known for a possible competitor, compare a constructed $d$-state model through $d+D-1$, or retain the uniform bound $2D-1$.

The length bound cannot generally be reduced to $2d-2$: the exact two-state mixtures in §7 agree on every binary word through length 2 but differ at length 3.

## 4. Native passive finite-permutation recovery

Let $\Omega$ be a nonempty finite set, $P:\Omega\to\Omega$ a permutation, $r:\Omega\to\mathcal A$ a deterministic readout, and $\mu$ an initial probability distribution. An observed length-$\ell$ word starts at time zero:

\[
s(x_0\cdots x_{\ell-1})
=\sum_{\omega\in\Omega}\mu(\omega)
\prod_{t=0}^{\ell-1}\mathbf1\{r(P^t\omega)=x_t\}.
\]

This is a passive classical cylinder law. It uses no hidden-state measurement, quantum probability postulate, coherent input, or hidden control. It assumes the record corresponds to the stated deterministic readout along the same undisturbed permutation trajectory. An apparatus that changes the trajectory must be included in the model instead.

There is a linear word realization of dimension $|\Omega|$: write $D_x=\operatorname{diag}(\mathbf1\{r(\omega)=x\})$, represent $P$ as a column permutation matrix, and use $M_x=PD_x$, $a=\mu$, $b=\mathbf1^T$. Reading then advancing produces the cylinder above because the last advance drops out under $\mathbf1^TP=\mathbf1^T$. The sum of letter operators is $P$. This connects native passive words to Theorem L, but special deterministic structure yields a stronger quotient result without assuming linear minimality.

### 4.1 The all-time predictive quotient is a permutation

Define

\[
\omega\sim\eta\quad\Longleftrightarrow\quad
r(P^t\omega)=r(P^t\eta)\text{ for every }t\ge0.
\]

Forward invariance is immediate. For backward invariance, take a common finite order $L\ge1$ with $P^L=I$. Every $P^{t-1}$, including $t=0$, is a nonnegative power modulo $L$; thus equal futures give equal readouts after $P^{-1}$ at every nonnegative time. Consequently $Q=\Omega/{\sim}$ inherits a permutation $\overline P$, readout $\overline r$, and prior $\overline\mu=q_\#\mu$. By construction distinct quotient states have different future traces. If $\mu(\omega)>0$ for every microstate, then $\overline\mu(q)>0$ for every quotient state. In fact the quotient theorem only needs this latter full-support condition.

The quotient map is visible-preserving and intertwines $P$ with $\overline P$. This is the time-homogeneous all-time version of the pinned finite-horizon tail idea. It is not a reversible identification of microscopic states within a fibre.

### 4.2 Prefix separation at $N-1$, with edge cases

For any deterministic finite labelled system on $N$ states, let $C_k$ partition states by their first $k$ readouts; $C_0$ has one block. The recurrence

\[
\omega\equiv_{k+1}\eta
\quad\Longleftrightarrow\quad
r(\omega)=r(\eta)\ \text{and}\ P\omega\equiv_kP\eta
\]

shows that if $C_k=C_{k+1}$, then all later partitions agree with it: its equivalence is forward invariant, so no later output can split a class. Before stabilization every refinement increases the number of blocks by at least one. Therefore $C_{N-1}$ equals the full future-equivalence partition for $N\ge2$. If the system is future-observable, $C_{N-1}$ is discrete. This does not assume $P$ is invertible; invertibility is needed above for the quotient itself to remain reversible.

For $N=1$ zero-length words cannot reveal the label. One-letter data is necessary and sufficient. A constant readout on any finite carrier has a one-state quotient, irrespective of its microscopic cycle structure. These are not exceptions hidden in the notation.

### 4.3 Finite-block identification with a known state bound

**Theorem N.** Consider two native passive models as in §4.1. Assume their initial distributions have full support on their respective future-trace quotients, and a known common upper bound $B$ on the two quotient sizes. If $B\ge2$ and their word probabilities agree for every word of length at most $B$, their quotients are uniquely isomorphic by a readout-preserving permutation transporting the initial prior and intertwining their dynamics. For $B=1$, agreement of one-letter data suffices.

**Proof for $B\ge2$.** Put $\ell=B-1\ge1$. By §4.2 each quotient state is uniquely labelled by its length-$\ell$ future block. Full support means these labels are exactly the positive-probability words of length $\ell$, not merely an unknown subset. The common word law therefore gives the same state-label set

\[
W=\{w\in\mathcal A^\ell:s(w)>0\}.
\]

For every $w\in W$ there is exactly one symbol $x$ with $s(wx)>0$, since $w$ identifies one deterministic quotient state. Its successor has label equal to the last $\ell$ symbols of (wx). Hence the length-$B$ support determines the transition

\[
T(w)=\operatorname{suffix}_{\ell}(wx).
\]

This is a permutation because it is the original quotient permutation written in block labels. Its readout is the first symbol of $w$, and its initial mass is (s(w)). Thus both quotients are conjugate to exactly this same labelled state set, permutation, and initial measure. The isomorphism matching block labels is unique: any readout-preserving dynamics intertwiner preserves the entire future trace, and future observability forces it to match each state to that trace. No invariance of $\mu$ was used. For $B=1$, each quotient is a single state; its one-letter law determines its label and the permutation is the identity. $\square$

The maximum observed block length is $B$, counting the time-zero readout. If the recording convention starts strictly after an initial rooted state, shift the indexing rather than silently adding or deleting one observation. The theorem uses exact word probabilities; merely knowing that a finite observed sample did not contain an extension cannot certify zero extension probability.

### 4.4 Missing hypotheses have concrete consequences

Without a known bound, even full-support stationary laws on future-observable native models can agree through an arbitrarily long finite window and differ later. Uniform starting points on binary de Bruijn cycles of orders $k$ and $k+1$ produce every word of length at most $k$ with probability $2^{-|w|}$, yet differ on length-$(k+1)$ words: the smaller cycle has only $2^k$ supported words of that length, the larger has all $2^{k+1}$. Their states are future-observable because the cyclic readout strings have no smaller period. The script verifies this for $k=2,3,4$; the construction proves the obstruction for every $k\ge1$.

Without full support, an extra future-distinguishable state with zero initial mass need leave no trace in the law. The control adds an unoccupied fixed state labelled 1 to a two-state alternating process. Both entire laws agree, but the total future-observable carriers have different cardinalities. The theorem can still identify the appropriate prior-supported predictive content, not the unvisited carrier.

Even with full support, an unobservable microscopic fibre is not recovered. On $\{0,1\}\times\{0,1,2\}$, compare

\[
P_A(v,h)=(1-v,h),\qquad P_B(v,h)=(1-v,h+1\bmod3)
\]

with uniform initial distributions and visible readout $v$. Both have the same two-state alternating future quotient and the same law for every word, but their full cycle types are $(2,2,2)$ and $(6)$. Hence they are not conjugate as full permutations. These are decoupled hidden extensions: permitted ancilla/deep-sector gauge moves may already relate them. This is a fibre-freedom control, not a counterexample to the repository's full proposed gauge relation.

### 4.5 Native quotient minimality, Hankel rank, and cone saturation

There is an exact bridge to Theorem L **on this quotient**. Suppose the future-observable quotient has $N$ states and full-support prior $\overline\mu$. Fix one **common** separating word length
\[
\ell\ge \max(1,N-1).
\]
In Theorem N one may use $\ell=B-1$ for $B\ge2$, or $\ell=1$ for $B=1$. Write $w_q$ for the length-$\ell$ output block of state $q$, and work in quotient coordinate vectors. With $M_x=\overline P D_x$,
\[
bM_{w_q}=e_q^T,\qquad
M_{w_q}\overline\mu=\overline\mu(q)e_{\overline P^\ell q}.
\]
Indeed the block condition selects exactly the singleton start state $q$, and then advances it exactly $\ell$ times. Full support makes the displayed scalar strictly positive. Because the same power $\overline P^\ell$ is a permutation, its end states cover every quotient coordinate. Thus the nonnegative cone generated by unnormalized retained-word state vectors is the entire quotient state cone, and the corresponding block effects include every coordinate indicator. In particular the quotient is linearly reachable and observable, and its Hankel rank is exactly $N$.

Using a common length is essential to this coverage argument: arbitrary different lengths $\ell_q$ would not ensure that $q\mapsto\overline P^{\ell_q}q$ is surjective. The $N=1$ case is included by the chosen positive length.

Consequently the unique similarity from Theorem L between two such quotients is a permutation: matching common-length block probabilities and labels makes it carry each positive coordinate ray to the corresponding coordinate ray with the same weight, so the scalar factors are 1. This agrees with the direct finite-block reconstruction in Theorem N. Deterministic structure, full support, and reversibility supply more than generic linear minimality, explaining why the native block bound $B$ can improve on the general linear bound $2B-1$.

This is algebraic saturation of the **predictive quotient** cone by retained-word vectors, not an assertion that every microscopic state is externally selectable. If quotient fibres contain several microstates, no passive block separates them. Physical implementation of conditional preparations further needs the record-retention, nondisturbance, and postselection access discussed in §5. No hidden-factor or coherent-channel gauge conclusion is added.

## 5. The conditional simplex/order-isomorphism bridge

**Lemma G.** Suppose an invertible real linear map $S:\mathbb R^d\to\mathbb R^d$ maps the entire normalized classical simplex

\[
\Delta_d=\{p\ge0:\mathbf1^Tp=1\}
\]

onto itself. Then $S$ is a permutation matrix.

**Proof.** An affine bijection of a convex set maps extreme points bijectively to extreme points: otherwise a nontrivial convex decomposition of the image pulls back to one of the source. The extreme points of $\Delta_d$ are the coordinate vectors. Thus $S$ permutes that basis. $\square$

An equivalent usable hypothesis is $S\ge0$, $S^{-1}\ge0$, and $\mathbf1^TS=\mathbf1^T$. The first two properties make $S$ an order isomorphism of the nonnegative cone, hence a positive monomial matrix (its extreme rays must be permuted); normalization fixes every positive scale to 1. Equivalently, inverse normalization follows from the stated row identity, and both maps preserve $\Delta_d$. Without normalization, cone automorphisms may have positive diagonal scale factors.

This is strictly stronger than Theorem L. Linear reachability says reachable vectors span $\mathbb R^d$; it does not say their positive cone is the whole state cone or their normalized convex hull is $\Delta_d$. Linear observability says effects separate vectors; it does not give every positive effect. Even strictly positive normalized minimal models can have a unique nonmonomial similarity whose inverse has a negative entry; §7 gives one.

To derive Lemma G from an operational interface, the corresponding preparations must saturate the normalized state simplex in **both** representations, and $S$ must carry those preparations consistently; or an equivalent state/effect order characterization must be independently proved. Merely preparing each visible $v$ with one fixed hidden prior $\mu_H$ does not do this on the microscopic simplex.

There is a limited native way to obtain simplex access on the **future-observable quotient** without hidden control: under the passive, nondisturbing recording assumptions of §4 and full-support prior, a sufficiently long visible block singles out each quotient state. If postselection/retention of those records is operationally available, conditioning on a block prepares a point mass on a known end-of-block quotient state; finite invertibility makes the end states cover the quotient. Randomizing these conditional preparations yields its full simplex. The corresponding block events give separating point indicators on the initial quotient. This argument does not split microscopic states with identical future readouts, and the required nondisturbing records, full support, conditioning, and time access must be justified in a physical application. The statistical identification theorem itself does not assume that all these conditional preparations can be externally implemented.

Finally, even a recovered **readout-preserving global permutation** is generally weaker than a factor-preserving hidden gauge. On $V\times H$, a visible-preserving permutation has the form $(v,h)\mapsto(v,\sigma_v(h))$, with a possibly different hidden permutation in each visible fibre. It becomes $I_V\otimes P_H$ only under an additional interface restriction, for example commutation with every fixed visible matrix-unit map $E_{vw}\otimes I_H$: applying the commutation identity to ((w,h)) forces $\sigma_v(h)=\sigma_w(h)$ for all $v,w,h$. Access to those same-state hidden-preserving visible transfers is not supplied by merely resetting a visible marginal, and is not assumed here. A classical permutation proof also does not by itself classify coherent hidden unitaries, visible phases, ancillary equivalences, graph changes, or all admissible partitions.

## 6. Actual native preparation and readout access

The pinned corpus gives a finite reversible ontology, a visible projection, and priors as realization data. `Main`, §1.2, explicitly distinguishes the default invariant counting measure from structured hidden priors. Its §1.4 formula integrates over the hidden coordinate at a fixed visible input; the baseline rooted maps in §2.3 are one-time marginals from such preparations. Its general finite-horizon faithful realizations permit a joint initial law that may correlate visible and hidden coordinates (§1.5/§3.4). These scopes must not be interchanged.

A rooted visible preparation has microscopic law

\[
\mu_v(v',h)=\mathbf1\{v'=v\}\mu_H(h).
\]

For more than one visible state this is not globally full-support on $V\times H$, even when $\mu_H$ is uniform or otherwise fully supported. A known positive mixture over all roots would have global full support if every root is available with the **same** fixed dynamics, hidden prior, readout, and preparation meaning. That is an additional consistent-family access hypothesis, not an automatic consequence of one rooted transition table. Full-support visible priors in recurrence/memory statements are likewise not the same as full-support microscopic priors.

Joint passive trajectory frequencies are stronger data than the separate quantities (T^{(k)}_{ij}$. Distinct process laws can share their one-time marginals. Where the observer can retain all the visible records, a passive family supplies these cylinder statistics; where records or time horizons are restricted, it supplies only that restriction. Nothing in this note assumes that all potentially available microscopic labels can be read, that hidden states can be set, or that arbitrary coherent operations can be implemented.

The generic intervention-word theorem needs an independently defined stationary alphabet of allowed outcome-labelled instruments and all concatenations queried by the Hankel construction. The repository's classical finite-context response-table/comb constructions show representability of stipulated finite controlled families; they do not establish physical access to every microscopic preparation/effect, a universal experimental reset, or one common coherent instrument/composite theory. The pinned corpus explicitly retains that operational lift as open. Replacing missing native access with an arbitrary hidden-state oracle would not repair Theorem 24.

The selector track's separate native statement is logically compatible: for a finite abelian group and $\Phi_F(x,y)=(F(x)-y,x)$, full labelled three-time current-field records determine (F(x_t)=x_{t-1}+x_{t+1}$, although the one-step visible law under uniform phase counting does not determine (F). That theorem uses enough labelled local information to invert the update. Coarse projections may need longer words or fail to distinguish a microscopic fibre. Its source/control receipt is owned by the selector track; this document does not count their verification as a test run here.

## 7. Exact controls and their conclusions

`exact-controls-v2.py` uses only Python standard-library rational arithmetic. It does not call the existing governed protocols or manipulate the repository. Its output is `exact-controls-v2-results.json`.

### 7.1 Strictly positive minimal models with a nonphysical similarity

Take

\[
A_0=\begin{pmatrix}1/4&1/10\\1/10&1/5\end{pmatrix},\quad
A_1=\begin{pmatrix}7/20&3/10\\3/10&2/5\end{pmatrix},\quad
a=\begin{pmatrix}2/3\\1/3\end{pmatrix},\quad b=(1,1).
\]

Their sum is the column-stochastic matrix with diagonal $3/5$, off-diagonal $2/5$. Let

\[
S=\begin{pmatrix}1&1/10\\0&9/10\end{pmatrix},\quad
S^{-1}=\begin{pmatrix}1&-1/9\\0&10/9\end{pmatrix},\quad
a'=Sa=(7/10,3/10)^T.
\]

Then $A'_c=SA_cS^{-1}$ are

\[
A'_0=\begin{pmatrix}13/50&47/450\\9/100&19/100\end{pmatrix},\quad
A'_1=\begin{pmatrix}19/50&151/450\\27/100&37/100\end{pmatrix}.
\]

All four letter matrices and both initial distributions are strictly positive; both summed transitions are column stochastic. Both reachability and observability ranks are 2. Since $\mathbf1^TS=\mathbf1^T$, the two models have the same probabilities for every word. The controls independently sum all hidden paths and compare with matrix products through length 6, verify normalization, reconstruct the unique $S$ from the reach basis $a,A_0a$, and reconstruct the linear model from the scalar Hankel data through length 3.

The map $S$ is neither monomial nor orthogonal/unitary, and its inverse has entry $-1/9$. It does not map the entire simplex onto itself. Because the models are minimal, the displayed intertwiner is unique; there is no different state-permutation intertwiner fixing their labelled series. These models are positive stochastic predictive models, **not** fixed finite-permutation native models: they do not disprove Theorem N or the OI gauge conjecture. They refute the proposed automatic bridge from general minimal predictive similarity to physical state relabeling/unitarity.

### 7.2 Controls for omitted minimality

Without observability, use the same initial vector $(1,0)^T$ and $b=(1,1)$, and set both letter operators to $T/2$, once with $T$ having diagonal $3/4$, off-diagonal $1/4$, and once with diagonal $2/3$, off-diagonal $1/3$. Both models are positive and normalized, reachable of rank 2, but observation rank 1. Every word has probability $2^{-|w|}$. Their letter-operator traces are $3/4$ and $2/3$, so they cannot be similar.

Without reachability, set $a=(1/2,1/2)^T$, $b=(1,1)$, total transition all entries $1/2$, and compare

\[
A_0=\begin{pmatrix}3/10&1/5\\2/5&1/10\end{pmatrix},\quad
B_0=\begin{pmatrix}7/20&3/20\\1/4&1/4\end{pmatrix},
\]

with the other letter equal to total transition minus the displayed matrix. Both models are strictly positive and normalized, observation rank 2, reachability rank 1. Each letter takes $a$ to $a/2$, giving the same fair word law for all lengths, yet their letter traces (2/5,3/5) differ. The all-word facts have these algebraic witnesses, independently supplemented by checks through length 6.

### 7.3 A necessary third-order distinction at dimension 2

Use static two-atom Bernoulli mixtures: $M_0=\operatorname{diag}(p_1,p_2)$, $M_1=I-M_0$. One model has $p=(1/4,3/4)$ and weights ((1/2,1/2)). The other has $p=(1/5,17/24)$ and weights ((25/61,36/61)). Both are normalized, reachable and observable of dimension 2. Every word through length 2 agrees, but

\[
s_A(000)=7/32,\qquad s_B(000)=409/1920,
\qquad s_A(000)-s_B(000)=11/1920.
\]

Thus length 2 cannot replace the general $2d-1=3$ bound even for positive normalized series (the letter matrices here are nonnegative, with zeros off-diagonal).

### 7.4 Native controls

The grid covers all 24 permutations on 4 states, all 16 binary readouts, and two globally full-support priors: uniform and ((1,2,3,4)/10). The latter is not assumed invariant. Across 768 cases, 368 have a nonstationary prior and 96 have constant readout. The quotient-size histogram is (96,192,96,384) for sizes (1,2,3,4).

For each model an independent pairwise trace comparison through $4!=24$ steps checks full future equivalence; the script compares this with length-(3) block equivalence, checks forward and backward invariance, reconstructs solely from length-$3/4$ word laws, verifies the quotient conjugacy and pushed-forward prior, and predicts the word law through length 7. Two separate $N=B=1$ cases test both visible labels. All 770 grid/edge instances additionally verify the common-length singleton effects and positive coordinate rays, their complete coordinate coverage, exact linear reachability/observability, and exact rank of the separating-block Hankel matrix. The missing-bound de Bruijn controls and the missing-full-support and hidden-fibre controls in §4.4 also pass.

These are bounded checks of explicit examples and a small finite grid. They do not substitute for the universal partition and realization proofs, nor establish physical access or the remaining gauge bridge.

## 8. Primary literature and remaining research obligation

The minimal-realization theorem is standard, not novel: Berstel and Reutenauer, *Noncommutative Rational Series with Applications*, chapter 2, “Minimization,” explicitly treats uniqueness of minimal linear representations up to similarity (Theorem 2.4). Thon and Jaeger, “Links between multiplicity automata, observable operator models and predictive state representations: a unified learning framework,” *JMLR* 16 (2015), 103–147, gives the common sequential-system/Hankel setting and reconstruction equations. This note supplies its own elementary proofs and exact controls rather than importing a physical interpretation from that literature.

- Official Cambridge chapter: https://www.cambridge.org/core/books/abs/noncommutative-rational-series-with-applications/minimization/ACD53CC08C3CB9451564D3488D24FE22 (DOI 10.1017/CBO9780511760860.003).
- JMLR primary article and full paper: https://jmlr.org/papers/v16/thon15a.html ; https://jmlr.org/papers/volume16/thon15a/thon15a.pdf.
- Jaeger's original observable-operator article, author-hosted: https://www.ai.rug.nl/minds/uploads/oom_neco00.pdf.

The remaining Theorem-24 recovery obligation is substantive: identify the actual accessible word algebra and prior/preparation family, establish any necessary native minimality or cone-saturation property, and prove that the resulting intertwiner lies in the specified physical gauge relation for the stated observational equivalence. Proposition 24.2 addresses a strong coherent trace algebra; Theorems L/N address scalar predictive data under different explicit hypotheses. No implication between these interfaces, and no full all-partitions completeness result, is established here.
