# Compact-charge strengthening of the fixed-family anomaly theorem

Frozen mathematical supplement, 2026-10-28. This is the standard arithmetic result of Lohitsiri and Tong, *Hypercharge Quantisation and Fermat's Last Theorem*, SciPost Phys. 8, 009 (2020), [arXiv:1907.00514v3](https://arxiv.org/html/1907.00514v3), equations (6)–(8). The elementary reduction below uses the classical cubic case of Fermat's theorem. It is not a new OI mechanism or a Lean proof.

This supplements, without changing, the self-contained all-real classification assuming `C=W=G=A=0` in `hypercharge_recovery_v1.txt`. The new option replaces the mixed gauge-gravitational equation G=0 by the independent hypothesis of **commensurate charges**. A continuous action of one compact U(1) on the stated fields supplies that hypothesis: in a common circle coordinate its weights are integers. It does not supply the selected chiral field family itself.

Assume exactly the fixed chiral representations `Q_L=(3,2)`, `u_R=(3,1)`, `d_R=(3,1)`, `L_L=(1,2)`, `e_R=(1,1)`, with right-handed particle charges `(a,u,d,l,e)`. There are no additional charged chiral anomaly cancelers. Several identical family copies with universal charges are allowed. Suppose the charges are commensurate, meaning that there exists a nonzero real γ such that all five charges belong to γZ. Require only

\[
C=2a-u-d=0,\qquad W=3a+l=0,\qquad
A=6a^3-3u^3-3d^3+2l^3-e^3=0.
\]

**Claim.** The complete solutions are the same two branches as for the all-real four-equation theorem:

\[
(a,u,d,l,e)=(a,4a,-2a,-3a,-6a)
\quad\text{or}\quad(a,-2a,4a,-3a,-6a),\quad a\ne0,
\]

and `(a,u,d,l,e)=(0,b,−b,0,0)` for `a=0`, including the all-zero case. In every branch `G=6a−3u−3d+2l−e=0` follows. Conversely every commensurate point on those branches cancels C, W and A. Hence nonzero quark-doublet charge gives the standard proportional assignment up to the named uR/dR interchange, without separately assuming the mixed gravitational anomaly or a Higgs/Yukawa sector.

**Proof with all zero cases.** The two linear equations give `u+d=2a` and `l=−3a`.

If `a=0`, then `d=−u` and `l=0`, so the cubic equation becomes `−e³=0`. Thus `e=0`, giving exactly the stated neutral-Q branch and G=0.

If `a≠0`, put

\[
x=e/a,\qquad y=(u-d)/(2a).
\]

Commensurability makes both x and y rational. Since `u=a(1+y)` and `d=a(1−y)`, division of the cubic equation by `−a³` gives

\[
x^3+18y^2+54=0.
\]

There is no lost `x=0` case: it would require `18y²+54=0`, which has no real solution. Therefore define the rational numbers

\[
v=-\frac{3+y}{x},\qquad w=-\frac{3-y}{x}.
\]

The identity `(3+y)³+(3−y)³=54+18y²` and the curve equation imply `v³+w³=1`. Clearing a common denominator, a solution with v and w both nonzero would give nonzero integers p,q,r with `p³+q³=r³`. The classical exponent-3 Fermat theorem excludes this. Its usual positive-integer form also excludes signed nonzero solutions: a negative term can be moved to the other side; both p and q negative cannot sum to positive r³ after choosing r positive.

Thus v=0 or w=0. The zero cases are exactly `(v,w)=(0,1)` or `(1,0)`, since the remaining rational cube is 1. Also `v+w=−6/x`, so both cases give x=−6. From `v−w=−2y/x`, they give y=−3 or y=3, respectively. These are exactly the two stated standard rays. Substitution gives G=0; conversely the rays and neutral-Q branch solve all the displayed equations. There is no additional point excluded by division: a=0 and x=0 were handled separately. □

**Exact boundary without charge commensurability.** Let r be the positive real root of `r³=2` and choose

\[
(a,u,d,l,e)=(1,1,1,-3,-3r).
\]

Then C=W=A=0 exactly, but `G=3r−6≠0`: G=0 would imply r=2 and hence `r³=8`, contradicting `r³=2`. The charges are not commensurate because a=1 and e=−3r have irrational ratio; irrationality follows from the rational-root theorem for `r³−2`. This is a legitimate real-charge countercontrol, rather than a compact-U(1) weight family. It shows why the all-real route needs its G assumption or another independent premise. The charged-neutrino and family-nonuniversal countercontrols in the original supplement remain applicable; compactness does not replace the fixed-family restrictions.

Primitive compact-circle weights reduce the nondegenerate branch to `(1,4,−2,−3,−6)` up to overall sign and the stated naming identification. Choosing physical Y normalization or electric-charge identification is a separate convention/bridge. No selection of the correlated native center K, physical light matter, or global line/bundle data follows from this strengthening.
