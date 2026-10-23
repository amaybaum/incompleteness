# Independent composition review: general AND aggregation

Read-only review of commit `43400ea790d9f021ae46c52379525618d43335eb`,
2026-10-23. No repository writes, comments, pushes or workflow dispatches.

Source: https://github.com/amaybaum/incompleteness/commit/43400ea790d9f021ae46c52379525618d43335eb

The reviewed directory is
`verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node9/design/composition/`.
The `source/` directory in this handoff contains the retrieved, unchanged files.

## Assessment

The general mathematical construction checks out under its stated affine
readiness resources. This is substantive progress beyond gates at selected
sizes: it gives raw AND_n for every n>=2 under one fixed update. The argument
does not depend on extrapolating the finite tests. Its components are a causal
boundary reduction, three linear injection wings, finite permutation-group
certificates, and an induction on the balanced AND formula.

It is not a pass of the original preregistration. The author already correctly
withholds that verdict because held-out full-torus runs were not performed.
There are additional specification and evidence qualifications below. An
unperformed test is not an observed failure of the construction.

The result concerns prearranged, one-shot computation. It does not provide
native preparation of the ready set, a native clock, a protected observation
interface, source freshness conditional on a complete apparatus record,
postmeasurement instruments, or quantum probabilities.

## 1. Provenance and replay

All 14 entries in the supplied `SHA256SUMS` match the retrieved files. The
preregistration hash is
`677d5b8d25388811d485ce1b19181be5d105721f97d0aa6b5ae104a77c5181a8`.
The full report hash is
`c3e908339632e2f4a87a08d17fa83291fc9aab836d90062fb6b2cf774147f8c5`.

The stored Section A digest is reproducible by taking the report prefix before
`## Section B.`, stripping trailing whitespace and adding one newline. That
gives `be34414badaca023d6296eafb4244f423b0264ce4d82f64f4a639ff58f584b8d`.
The hash file names `REPORT.md`, although the digest is of this earlier prefix,
not the final full report. An explicit canonical extraction instruction would
make this easier to audit.

All files are introduced together in the reviewed commit. Their hashes verify
their contents; they do not independently timestamp the author's earlier local
preregistration or pre-held-out hashing. The author's chronology is recorded,
but this review cannot independently attest it from this publication alone.

I read the checker and all imported local modules before execution. They use
the standard library and NumPy, contain no network calls, and their intended
output is stdout. I disabled bytecode-cache writes for replay. Both normal and
optimized executions reproduce the published `composition_checks.out` byte
for byte (about 43 seconds each in this environment).

The two assert statements in source code are disabled in optimized mode;
byte-identical output does not mean every internal assertion remains enabled.
The independent checker uses explicit failure branches. I did not rerun the
separate, substantially longer full-torus n=7,8 job; its stored output has a
verified checksum but those two simulations are not independently replayed here.

## 2. Why the all-n argument works

The rule remains

    U_(t+1)(x) = U_(t-1)(x) XOR H(S U_t(x)),
    H(a,b,d) = (b,d,a XOR bd),

with S the six-neighbour XOR. The previous receiver cone is zero. Current
sources lie exactly on the L1 sphere of radius T; other current cone bits are
zero. At each point inside the cone, no nonzero source can arrive before time
T-|x|. At that first-arrival time, the previous-time term and the inner
neighbours are still zero. Only outer neighbours contribute. This gives the
feed-forward inward sweep used in the report. It is an exact causal identity,
not an approximation or an assumption of a first-order update.

Arbitrary initial data outside current B_T and previous B_(T-1) cannot change
the receiver through T. The torus side 2T+3 prevents wrapping into this cone.
This proves exterior independence for the receiver record through its deadline;
it does not prove independence of every field elsewhere in the apparatus.

For the wing geometry, inward monotone paths cannot create support outside
the source planes. Each open wing contains only one rotated field at a given
depth, so the B*D product vanishes there. Wings on opposite chains meet on the
transverse axis with the same seed field; different-field wings meet on the
intended register axis or at the receiver. Thus the claimed linear wing
propagation has no omitted nonlinear crossing in its first-arrival circuit.

The side-injection coefficient is a binomial path count. Over F2 the lower
Pascal matrix is its own inverse, since

    sum_k binom(d,k) binom(k,q) = binom(d,q) 2^(d-q).

Modulo two this is zero for d>q and one for d=q. Consequently every prescribed
affine injection profile has the stated affine shell encoding. The final
transverse-axis sources cancel the remaining receiver injection.

Independently enumerating the permutations s -> H(s XOR v) gives all 40320
elements of S8. I independently evaluated every supplied leaf word and every
listed commutator pair. Each five-cycle has equal-length identity and cycle
words of length 6 or 8. The recursive sequence is a commutator: if either
subconjunction is false it evaluates to the identity, and if both are true it
evaluates to the target five-cycle. Induction proves the group-program claim
for every input count, not just the tested counts.

This is an application of Barrington's known branching-program construction:
David A. Barrington, *Bounded-width polynomial-size branching programs recognize
exactly those languages in NC1*, JCSS 38 (1989), 150-164,
https://people.cs.umass.edu/~barring/publications/bwbp.pdf.
The lattice realization, affine resources and receiver interface still need
their own checks; the complexity theorem alone does not certify them.

There is a minor all-size padding detail worth making explicit. Identity words
of lengths 6,8,10 exist. Every even gap at least 6 is a sum of these lengths.
If the two even program lengths differ by 2 or 4, raising the longer target by
6 makes both gaps representable. Otherwise the original maximum length works.
The implemented search through extra lengths therefore terminates for every
n; it need not rely on the finite size tests.

The two chains arrive as (0,F1,0) and (0,0,F2). With the transverse injection
cancelled, H gives exactly (F1,F2,F1*F2). These side fields are part of the raw
terminal record and are not masked.

## 3. Independent computations

`independent_checks.py` imports the reviewed builder only to obtain candidate
layouts, words and commutator pairs. Its permutation operations, full-torus
update, inward simulator, truth-table representation, algebraic-degree
calculation and rank elimination are separate implementations.

* Full scalar 3D update, n=2: all inputs, two dense full-torus backgrounds,
  silent receiver prefix and the entire terminal triple pass.
* General boundary reduction: 24 arbitrary three-dimensional shell assignments
  at T=1..6 match a direct memoized recursion of the raw second-order rule.
  These configurations include nonplanar sources, unlike the supplied
  quadrant-only reduction control.
* Independent integer-bitset sweep: every n=2..13 passes for all 2^n inputs.
  This includes new sizes 10,11,13, not in the published result table. The
  entire terminal triple, degree n and source-map rank n pass.
* Releasing the chain-start D pin breaks the conjunction at every one of these
  sizes. These new countercontrols use the independent inward sweep and are
  post-publication checks, not preregistered raw-torus results.

| New size | Deadline | Nonzero source-field entries | Rank | Output degree |
|---|---:|---:|---:|---:|
| 10 | 169 | 939 | 10 | 10 |
| 11 | 241 | 1352 | 11 | 11 |
| 13 | 313 | 1751 | 13 | 13 |

The measured full-torus memory estimates are correct for the published
all-input packed array: 7,613,149,632 bytes for n=9 and 175,233,216,000 for
n=12, per state array. Several arrays are needed during stepping. These are
costs of that implementation, not a lower bound on every possible exact
verification method. Streaming input assignments changes the memory/time
tradeoff, while the causal proof avoids enumerating irrelevant exterior data.
Neither observation retroactively performs the preregistered runs.

## 4. Preregistration and wording corrections

1. **Unrun versus failed.** The held-out full-torus tests were not run. Keep
   the verdict "preregistered success not established"; do not describe an
   output counterexample at n=9 or n=12.
2. **Countercontrol quantifier.** PREREG requires a nonvacuous control for each
   discovery and held-out size. The published main checker runs the three
   structural controls only at n=4. The report's unqualified statement that
   criterion 3 is met is too broad. This review adds controls at every n=2..13
   in the reduced model but does not rewrite the original evidence record.
3. **Resource specification.** PREREG asks for input/copy slots, including
   "which input", and closed forms for T(n) and m(n). The construction instead
   uses affine XORs of multiple inputs and gives an algorithm, recursive cost
   optimization, asymptotic bounds and finite counts. The report acknowledges
   that these are not single-input copies. This is a material expansion of
   the preparation contract and should be recorded as such; the promised
   closed-form copy count is absent. The construction remains valid under
   the broader affine-resource contract.
4. **Unused command-line option.** The checker docstring advertises
   `--with-3d-78`, but the code never parses or acts on it. The actual separate
   command is `python3 check3d.py 7 8`. The option should be removed or
   implemented before relying on it for coverage.
5. **Chronology.** Preserve the distinction between the author's local timing
   attestation and independently timestamped publication. Hash consistency
   alone cannot prove that a specification predated testing.

None of these findings changes the measured conjunction truth tables. They
do prevent an unqualified claim that the original acceptance criteria have
all been met apart from memory capacity alone.

## 5. Resource accounting and a new consequence

Let k=ceil(n/2) and define the balanced recursion weight

    G(1)=1,
    G(k)=2G(ceil(k/2))+2G(floor(k/2)),
    G(k)=2^h (3k-2^(h+1)), h=floor(log2 k).

Each leaf word has length between 6 and 8. Therefore every k-input group
program has length between 6G(k) and 8G(k). With at most six padding steps,

    6G(k)+1 <= T(n) <= 8G(k)+7.

This supplies explicit all-size bounds, not an exact closed form for the
particular optimized builder. Since G(k)=Theta(k^2), its latency is
Theta(n^2). The cone codimension simplifies exactly to

    C(n)=3[|B_T|+|B_(T-1)|]-n = 8T^3+16T-n = Theta(n^6).

There are at most 6(T-1)+3 nonzero source-field entries. Their value functions
can contain multiple inputs; for example, n=12 has 644 such multi-input
entries among 1342 entries. Counting each affine equality once gives the
correct codimension but does not supply a physical procedure for preparing it.

The input-to-source map has rank n for every n, not merely at tested sizes.
It is affine. If its linear part had a nonzero kernel vector d, inputs x and
x XOR d would give exactly the same complete prepared state. Taking x to be
all ones would contradict exact AND_n. Thus the ready set has exactly 2^n
cone states, and under the uniform counting prior its probability is 2^-C(n).
The large cold-resource requirement remains.

**New corollary, relative to the earlier degree-10 evidence.** Suppose this
fixed rule could be conjugated to a linear evolution by maps of algebraic
degrees at most g and g', uniformly in lattice size and time. Every raw output
at any deadline would then have degree at most g*g' in the initial bits.
Restriction to the builder's affine initial encoding cannot increase degree.
But the construction produces AND_n, of degree n, for arbitrarily large n.
Taking n>g*g' is a contradiction.

Hence the all-n construction rules out such a uniformly bounded-degree
linearization. This is stronger than the finite report18 observation, which
only excluded g*g'<10. It does not rule out size-dependent degree bounds,
unrestricted nonlocal encodings, or other representations outside the stated
conjugacy class.

## 6. Relevance to full equivalence

This resolves the narrow aggregation question under supplied affine readiness:
the fixed nonlinear rule can implement unbounded-degree conjunctions. It does
not establish plug-and-play composition of already-running devices, reusable
workspace, or native production of their many affine input copies.

The next useful work should use this capability to define and analyze an
actual preparation/read instrument. The preparation-geometry handoff remains
applicable: more gates cannot repair input ensembles that have insufficient
distinguishability. The prepared ensembles must first meet the hidden-overlap
requirements, and the physically accessible record must then conceal the
necessary mixture differences.

A suitable next deliverable is one bounded native instrument with explicit
prepared distributions, herald/clock records, side-register access and outgoing
state, followed by the complete-record identities and instrument-closure test.
The general aggregation lemma is a component available to that construction;
it neither selects the angular law nor proves OI-quantum equivalence.
