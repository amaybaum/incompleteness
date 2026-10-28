# Labelled triple-support identification in a finite companion family

This is an exact classical result within a specified finite dynamical family and observation interface. It supplies an inverse for that family, rather than a physical selection of the family in Theorem 23.

## Fixed family and readout

Let $G$ be a known finite abelian group, with fixed labels and addition, and let $F:G\to G$ be any function. Put
$$
\Phi_F(x,y)=(F(x)-y,x),\qquad X_{t+1}=F(X_t)-X_{t-1}.
$$
The readout is the entire labelled current field $X_t$. The phase ensemble at the observation time is a probability measure $\mu$ on $G\times G$, with coordinates $(X_t,X_{t-1})$. Equality of observations here keeps this group, its labels and the readout fixed; it does not transport the readout along an arbitrary state relabelling.

## Proposition: identification from labelled triple support

If $\mu$ has full support on $G\times G$, exact support of the labelled law of $(X_{t-1},X_t,X_{t+1})$ determines $F$ uniquely. In particular, two such systems with equal labelled triple laws have the same $F$, even if their full-support phase measures differ. No stationarity or linearity assumption is needed for this implication.

Under uniform phase counting, $\Phi_F$ preserves that measure, every consecutive pair has probability $|G|^{-2}$, and
$$
\Pr(X_{t+1}=c\mid X_t=b)=|G|^{-1},\qquad
\Pr(X_{t-1}=a,X_t=b,X_{t+1}=c)
=|G|^{-2}\mathbf 1_{\{a+c=F(b)\}}.
$$
The first formula is a **classical one-step population kernel**, identical for every $F$ in this family. It is not an equality of coherent channels or a scalar spatial wave kernel.

*Proof.* The inverse is $\Phi_F^{-1}(u,v)=(v,F(v)-u)$, so the phase map is a permutation. A supported triple satisfies $a+c=F(b)$. Full phase support supplies a supported triple for every $b$, and any such triple gives $F(b)=a+c$; hence the triple support determines $F$ everywhere. Under uniform counting, exactly one old field $a=F(b)-c$ produces a specified pair $(b,c)$, which proves the pair and conditional formulas. The initial phase pair also has weight $|G|^{-2}$, giving the triple formula. $\square$

## Complete local parent access

Suppose $G=(\mathbb F_q)^\Lambda$ and the target row $F_0(x)$ depends only on a known set $R$ of current parent sites. Exact labelled records of $X_{t-1,0}$, $X_t|_R$ and $X_{t+1,0}$ recover that row from
$$
F_0(b_R)=X_{t-1,0}+X_{t+1,0}.
$$
Full phase support supplies every assignment of the previous target and current parent values. The conclusion requires all active parents, or an independently justified sufficient causal patch. It cannot be applied to omitted coordinates or an averaged spatial kernel. The construction of a physically accessible readout and persistent record is a separate premise.

## Coarse-readout control

Let $G=(\mathbb F_5)^2$, $F_c(u,v)=(v,cu)$ for $c\in\{1,2\}$, and observe only $Y_t$, the first coordinate of $X_t$. Use uniform phase counting. From initial phase $((u,v),(p,q))$, the first four readings are
$$
(Y_0,Y_1,Y_2,Y_3)
=\bigl(u,v-p,(c-1)u-q,(c-2)v+(1-c)p\bigr).
$$
The coefficient matrix from $(v,p)$ to $(Y_1,Y_3)$ has determinant $-1$; the four readings therefore parametrize all $5^4$ phases bijectively. Every word law through length four is uniform and is the same for the two rules. But $F_c^2=cI$ gives
$$
Y_{t+4}+(2-c)Y_{t+2}+Y_t=0.
$$
Consequently the five-word $(0,0,1,0,0)$ has probability $0$ for $c=1$ and $1/625$ for $c=2$. In this example the fifth-word law distinguishes the rules although their coarse triple laws agree. The full-current-field proposition cannot be applied to this missing-coordinate interface.

## Ensemble and physical limits

Full support is an ensemble coverage hypothesis, not a consequence of stationarity or of recording a single deterministic orbit. A single orbit or a root-restricted preparation may omit current field values and leave $F$ undetermined there. The result concerns an exact law or exact support; a finite sample does not by itself establish that support.

Uniform phase counting is essential to the flat-kernel conclusion as stated. For example, take $G=\mathbb F_5$, $F(x)=x$, and assign weight $2$ to each phase in the invariant six-cycle of $(1,0)$ and weight $1$ to every other phase. The normalized measure is stationary and has full support, but
$$
\Pr(X_{t+1}=1\mid X_t=0)=2/7\ne1/5.
$$
Triple-support identification still holds. Thus the structured priors permitted by [SM, Lemma 1c] must be kept distinct from uniform phase counting.

Neither formula supplies the spatial positivity, real lift, speed calibration, nearest-neighbor coupling or H-link premise needed for a physical branch selector. The known family, field/site labels, readout, preparations and record coverage remain assumptions. The inverse selection of a physical substratum in Theorem 23 remains open, as do the broader gauge and coherent-channel classification questions.

The reversible second-order construction is standard; see A. Yu. Vlasov, [On generalization of reversible second-order cellular automata](https://arxiv.org/abs/1311.4297), Eq. (2). The statements above concern its observation interface and exact support.
