# Native short-window gate and complete-pointer audit

24 October 2026. Research only; no observer access, physical premise, operational
map, F/E status or equivalence is adopted. #885 is read-only. Root publishes
this plan to #910 before execution. Native source snapshot is #910 at
`16b154cefe3acd40d5a60d507905709c3cfc19ca`, in particular Native A author
`f24a57a7c23cc1818c04265cec7604f8bc2f410d`.

## Question and fixed bounded family

Does a short continuation of the explicitly source-prepared native lattice
already supply a physical cell from which the intended acceptance decision
can be read? Which useful nonlinear old-input/apparatus interactions are
actually produced before such a pointer is available?

Use the complete second-order six-neighbor rule

    U_(t+1)(v) = U_(t-1)(v) XOR H(XOR_(w~v) U_t(w)),
    H(A,B,D) = (B,D,A XOR BD).

This is a small original-time native control family, NOT a simulation or
substitute proof at the programme's enormous L. Fix n in {1,2,3}. Four
independent initially supplied current triples lie at

    f_old = (-(n-1),0,0),
    f8    = (-n,0,-1),
    f10   = (-n,0,+1),
    f9    = (-n-1,0,0).

Each of the four triples varies over all eight payloads. This gives 4096
worlds per fixed n/background. f_old is the sole old-input source, not a
copy preloaded beside the pool. Both initial slices elsewhere are fixed
by one declared deterministic dirty-background formula. Background seeds
are {0,3}; in addition retain the n=1 all-zero-complement family for the
closed-form nonlinear interaction control. No late apparatus is inserted.
The old source reaches P=U_(n-1)(0), and the three fresh sources do not.
Pool fields are Q8=U_n(0,0,-1), Q10=U_n(0,0,+1). Their source map and the
full U_(n+1)(0) ciphertext law are positive controls inherited in form but
recomputed from actual native evolution. P is not silently assumed clean;
all eight old triples, including failure-like A components, remain present.

Define actual s=P.B, Y=Q8.B, R=Q10.D, and
K=Q8.A+2 Q8.D+4 Q10.A. The fixed desired event is

    A = [K < threshold(Y XOR s,R XOR s)],
    threshold(00,01,10,11)=(5,0,4,1).

## Fixed pointer window and decision rule

Read candidates are every physical current cell at an integer position in
the Manhattan ball of radius two about 0, at each deadline n+d with
1<=d<=3. The family is fixed now, not enlarged after an unfavorable result.
For every candidate retain its complete terminal triple, and also calculate
the complete same-site raw prefix from time n through its deadline. A
Boolean relabelling of the TERMINAL triple is considered only as a generous
comparison class; a prefix decoder does not count as a physical flag.

For each fixed family and for the common pooled family, group the actual
worlds by terminal raw triple. Report both the entire old-P family and the
prepared-shape sector P.A=0, rather than allowing failure-like P.A=1 worlds
to decide the only relevant obstruction. A is exactly readable iff no nonempty raw
cell contains both A values. Otherwise compute the minimum pointwise flag
error as the sum, over raw values, of the smaller A count divided by total
world count. Exhaust all 256 Boolean functions of a raw triple as an
independent control. Record compact collision witnesses. If a terminal
readout succeeds, retain all extra raw fields and prefix cells and report
whether they carry additional input information. Success in this bounded
family is a candidate witness only; no claimed quantum instrument or native
huge-L implementation follows. Failure excludes only this precise family,
window, sites and readout class.

## Native nonlinear interaction and algebra controls

For the n=1 zero-complement family derive the exact polynomial of the
physical origin triple after two ticks in the twelve original payload bits.
Use both direct algebra and exhaustive Boolean Möbius inversion. Isolate
actual products involving old-input and fresh-apparatus bits; verify that
removing the native B*D term changes the physical fields on explicit worlds.
This is a native nonlinear coupling witness, not a synthesized acceptance
circuit.

Separately compute the acceptance ANF in independent logical variables
(s,Q8,Q10), and substitute the seven-site inverse expression for s. Formal
polynomial degree is only a gate-complexity diagnostic. Source-reachable
relations can cancel it, so it will not decide the physical pointer verdict.

## Required controls and deliverables

- Independent scalar integer native recursion agrees with packed Boolean
  evolution on fixed selected worlds, sites and deadlines.
- Old-source/three-fresh-source geometry, bijective old input, and triangular
  pool/current-ciphertext laws are checked from original time.
- Exact threshold counts, logical ANF and truth-table reconstructions agree.
- The explicit native nonlinear polynomial agrees with every zero-complement
  world; removing the nonlinear term and/or old-local term is detected.
- Raw-cell Bayes error agrees with all 256 Boolean readouts. A synthetic
  pointer containing A passes the same collision/readout mechanism so an
  all-fail result is not built into the checker.
- Full raw triples, actual prefixes, zero cells and both A outcomes remain.
  No history/pool independence is inferred beyond computed bounded laws.

Curated output: this PLAN.md, REPORT.md, checks.py, deterministic result.json,
PROVENANCE.json and SHA256SUMS. Normal and -O outputs must be byte-identical.
General/source-scale claims, exhaustive bounded checks, algebraic controls
and internal review remain separate evidence layers. Root handles all Git
publication. No merge, dispatch, branch deletion, force push or #885 write.
