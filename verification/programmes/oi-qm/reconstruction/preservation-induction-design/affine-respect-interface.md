# Separate affine-respect interface note

This note supports #840 and is separate from preservation induction.
It proposes a conditional interface only; no external label-dual source
or completion-continuity premise has been supplied or kernel certified.

Let x_p be preparation vectors in a real vector space E, and y_p=T.τ p
the completion-valued outputs in F. Let L be a family of linear functionals
on F that jointly separates vectors. Assume that for every ℓ∈L there is
a linear functional f_ℓ on E and a scalar b_ℓ such that, for every p,

    ℓ(y_p) = f_ℓ(x_p) + b_ℓ.

Then the operation datum satisfies `CompletionAction.AffineRespect`:
for every finite coefficient family with ∑c_p=0 and ∑c_p x_p=0,

    ℓ(∑c_p y_p) = f_ℓ(∑c_p x_p) + b_ℓ ∑c_p = 0.

Joint separation gives ∑c_p y_p=0. This proves the implication from the
named label-dual evaluation premise to affine respect. It does not show
that the framework supplies the pulled-back tests f_ℓ or the separating
family L. Using every mathematical linear functional would be a distinct,
stronger test premise; the physical label/test inventory must be stated.

The offset is harmless for affine relations; a strictly linear label-dual
interface may set b_ℓ=0. Continuity is unnecessary for the finite-relation
claim. The implication does not rely on the preservation induction or
matrix positivity. Existing code anchors at D are `OpDatum`,
`StateRespect` and `AffineRespect` in `CompletionAction.lean:46–61`.

Nonvacuous counterexample separating the interfaces: preparations x=0,1,2
with outputs y=x² satisfy state respect, since equal preparation vectors
have equal outputs. The affine coefficients (1,-2,1) obey ∑c=0 and ∑cx=0,
but ∑cy=2. Thus state respect alone does not establish affine respect.
The same relation is preserved by the affine output y=3x+2. These are
exact written arithmetic checks, not claims about admitted framework
preparations or a new physical countermodel. A future build should express
the actual completion-valued separating tests and compile this implication
against `AffineRespect` before its native round is frozen.
