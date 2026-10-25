# Fixed 64-case native seed-controller probe

Before computation, fix the actual reset_v9 q9 geometry and all Q,C,G,W.
Let fresh candidate bits be a,b and delta=a XOR b. At the original initial
time prepare J at (0,S,S+154) with payload

    (u XOR a,a,u XOR a) XOR delta*C,

and K at (1,S,S+153) with payload delta*V. C,V each range over eight constant
triples: exactly64 candidates. These initial sourcefields are affine in the
apparatus bits; they never contain unknown x or the later y. K and J are on
the same original q9 ready boundary. All inherited sources and public banks
are preserved. No late state is reset or spliced.

Evaluate the joint Q/C/G/J/K upper strip with signed x (K breaks x reflection)
and the unchanged coupled W lower front, then the complete q9 diamond. Check
all x,u,mY,mR,a,b assignments. Success target is whole raw
q9=(0,y XOR a,y XOR b) for masks00,10,11, with y=x XOR u; separately record
whether01 also works. This is a two-slice phase candidate because previous
q8 carries y, not a same-current-slice public Y port. If no candidate meets
the target, report only this finite affine-source family as excluded.

Controls before verdict: source/ready/bank geometry; K/J exclusion from
q8 throughR+8; exact actual upper-strip period budget18; independent small
coordinate native recursion of the complete upper cluster; K=0 agreement
with the retained axis-only evaluator where C=0; q7/q8 preservation; all
selector masks; normal/-O replay. All source cross-interactions must be kept.
Potential q8 interventions are checked only after a positive native witness.
No nonlinear initial prior, reset claim, premise or calibration is adopted.
