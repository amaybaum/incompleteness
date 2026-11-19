# A retained write can change a neighboring fresh response

**Paper result.** Under the binary rounded-cubic rule and the two-slice
product reference law, a recorded request can identify the older symbol
subtracted at the next receiver. In the declared adjacent-pair protocol,
varying the retained first write flips the fresh second symbol with all
other second inputs fixed. The complete second-label laws given the two
first outcomes have total-variation distance \(3/32\). The third read
exhibits a same-present history gap of \(9/16\) and an observable support
obstruction to the positive labelled operation required by P8.

**Scope and evidence.** Worker P, 2026-11-19. Paper-only result for
[Issue #1409][issue] under the [owner decision][authority]. The drafting
and rounded-rule source pin is
5809c6c7537f9844f643a94ba1a65b281b47bc1a. The [fixed-site test][fixed] and
the [constructed bridge][bridge] specify the comparison questions.
The native responses and probabilities below follow from the stated
recurrence and reference law.

**Goal link (§A.47).** Decide whether spatial transfer under the unchanged
native update supplies a recoverable first outcome and a history-dependent
neighboring response.

## Fixed model and three-read schedule

Use \(\Lambda=\mathbb Z^3\) with six nearest neighbors \(N(i)\) at each
site, alphabet \(\{0,1\}\), and the published [rounded update][rule].
Write addition modulo two as \(\oplus\). Taking the binary
representatives of the symbols, the rule is

$$
g_i(y)=\left\lfloor\frac{\sum_{j\in N(i)}y_j+1}{3}\right\rfloor\bmod 2,
\qquad F(x,y)=(y,g(y)\oplus x).
$$

For six binary inputs, \(g_i=1\) exactly when the sum is 2, 3 or 4.
The phase-space law \(\mu\) gives independent fair bits on the two
slices. For fixed \(y\), subtraction of the independent fair \(x\)
coordinates gives a uniform product law on each finite cylinder of
\(g(y)\oplus x\). Its conditional probabilities are constant in \(y\).
Thus \(\mu\) is invariant under \(F\). The inverse is
\(F^{-1}(y,z)=(g(y)\oplus z,y)\).

Fix \(A=0\), \(B=e_1\), and the ancillary request coordinate \(C=2e_1\).
Let \(u,v,w,z\) be four successive slices. Start the read window at
update \(u\to v\), and use the fixed schedule below. A request is a
flag value 1. A flag value 0 displays \(\bot\).

| Tick | Before and after slices | Response site | Request flag | Label on a request |
| --- | --- | --- | --- | --- |
| 1 | \(u,v\) | \(A\) | \(u_B\) | \(v_A\) |
| 2 | \(v,w\) | \(B\) | \(v_C\) | \(w_B\) |
| 3 | \(w,z\) | \(A\) | \(w_B\) | \(z_A\) |

These are stipulated mathematical read projections under one fixed
schedule. The field follows the same rule on every tick. Each request
coordinate is a native stencil input. With exactly one of the other
five neighbors equal to 1 and the subtracted bit fixed, changing that
input changes the fresh field symbol.

Write \(L_i\) for the label at tick \(i\). The observable history through
each tick consists of these labels through that tick. In the state
\((v,w)\), \(v_A\) is in the older slot and \(u_B=g_B(v)\oplus w_B\)
is recoverable, so the observer can project the retained \(L_1\),
including \(\bot\). At tick 3 the observer can first recover
\(v_j=g_j(w)\oplus z_j\) for each \(j\in N(B)\) and then use the same
projection for \(L_1\) and the declared flags for \(L_2\). A fixed
finite patch of radius two about \(B\) supplies these coordinates.
The read projections expose the specified labels and their recovered
history.

## Supported change in the second field response

For \(a\in\{0,1\}\), prescribe two cylinders in the product state
\((u,v)\) as follows. Take \(D=e_2\) as a first-stencil data input,
distinct from the request coordinate \(B\).

| Slice | Coordinates prescribed |
| --- | --- |
| \(u\) | \(u_B=1,\ u_D=a\), with all other neighbors of \(A\) equal to 0 |
| \(v\) | \(v_A=a,\ v_C=1\), with all other neighbors of \(B\) equal to 0 |

Each cylinder fixes six bits in each slice and has mass \(2^{-12}\).
In its native precursor, the older \(A\) symbol is
\(g_A(u)\oplus v_A=0\), since \(g_A(u)=a\). The two cases have the
same first request and old \(A\) input, and changing the first data
input \(u_D\) changes the fresh first write \(v_A\).

Both cases have the same second request \(v_C=1\), older receiving
input \(u_B=1\), receiver \(B\) and other second stencil values. At
\(B\) the sum is \(1+a\), so \(g_B(v)=a\) and \(w_B=1-a\).
The first write remains readable as \(v_A\) in the older slice after
this second update. This compares the newly computed \(w_B\) at
fixed other inputs while changing the first write.

## Complete second-label law

Put \(m=u_B,\ a=v_A,\ r=v_C,\ b=w_B\). The bits \(m,a,r\) are
independent and fair under \(\mu\). They have these roles in the first
two ticks:

- \(m\) is the first request bit and the bit subtracted at \(B\).
- \(a\) is the first write and the input at \(A\) to the second stencil.
- \(r\) gates the second label and also enters that second stencil.

Conditional on \(m,a,r\), the four remaining neighbors in the second
stencil are independent fair bits. Let \(S\) be their sum. For
\(a+r=0,1,2\), the event \(g_B(v)=1\) requires \(S\) in
\(\{2,3,4\},\{1,2,3\},\{0,1,2\}\), respectively. Their binomial
masses are \(11/16,14/16,11/16\). Thus

$$
p(a,r)=\Pr(g_B(v)=1\mid m,a,r)
=\begin{cases}11/16 & a=r,\\14/16 & a\ne r,\end{cases}
\qquad b=g_B(v)\oplus m.
$$

The first-label marginal in order \(0,1,\bot\) is
\((1/4,1/4,1/2)\). From the law above, the second-label rows are

| First label | \(\Pr(L_2=0\mid L_1)\) | \(\Pr(L_2=1\mid L_1)\) | \(\Pr(L_2=\bot\mid L_1)\) |
| --- | ---: | ---: | ---: |
| \(0\) | \(7/16\) | \(1/16\) | \(1/2\) |
| \(1\) | \(11/32\) | \(5/32\) | \(1/2\) |
| \(\bot\) | \(7/64\) | \(25/64\) | \(1/2\) |

A real first label determines \(a\) and certifies \(m=1\), so a
request at the second tick gives \(b=0\) with probability \(p(a,1)\).
For \(L_1=\bot\), \(m=0\) and \(a\) is fair. Given \(r=1\) in
that row, \(b=1\) has probability \((14+11)/32=25/32\). The
two real first labels give second laws at total-variation distance
\(3/32\), with both \(\bot\) masses included. The older receiving
value \(m\) is identified by the first label within the ordinary
product ensemble.

For the masking control, compare the conditional laws given only
the raw first value \(v_A=a\). In that conditioning, \(u_B\) remains
fair and independent of \(v\). At fixed \(v\), subtracting \(u_B\)
makes \(w_B\) fair. The row of \(L_2\) is then
\((1/4,1/4,1/2)\) for each \(a\). The recorded first request supplies
the information about \(u_B\) that removes this uniform mask.

## Third-label law and the P8 support test

Conditional on \((v,u_B)\), the bits \(w_j\) for \(j\ne B\)
are independent fair bits. Indeed each is \(g_j(v)\oplus u_j\),
with a distinct independent uniform mask. In particular the five
neighbors of \(A\) other than \(B\) in \(w\) are independent of
\((m,a,r,b)\) and of both earlier labels. For \(b=0\) the third
label is \(\bot\). For \(b=1\), the other five neighbors must
sum to 1, 2 or 3 for \(g_A(w)=1\). This has probability \(25/32\).
The raw third response is \(z_A=g_A(w)\oplus a\).

The resulting factors specify the full three-label law. Start with
the fair independent \(m,a,r\), use \(p(a,r)\) and the subtracting bit
\(m\) for \(b\), and use the following conditional terminal rows:

| Active values at the third response | \(L_3=0\) | \(L_3=1\) | \(L_3=\bot\) |
| --- | ---: | ---: | ---: |
| \(b=0\), either \(a\) | \(0\) | \(0\) | \(1\) |
| \(b=1,\ a=0\) | \(7/32\) | \(25/32\) | \(0\) |
| \(b=1,\ a=1\) | \(25/32\) | \(7/32\) | \(0\) |

Here \(L_1\) is \(a\) when \(m=1\), and \(L_2\) is \(b\) when
\(r=1\). For \(h=(0,1)\), the mass is
\((1/4)(1/2)(1/8)=1/64\). For \(h'=(1,1)\), the mass is
\((1/4)(1/2)(5/16)=5/128\). They share present \(1\), and the
last two rows of the terminal table give their total-variation gap
\(9/16\). That gap comes from the subtraction of \(v_A=a\) at the
third update with the same \(w_B=1\). The distinct spatial influence
on the second response was established by the fixed-input cylinders
and the second-label law.

For the tested transitions, the active bits can be taken to be
\((m,a)\) before tick 2 and \((a,b)\) before tick 3. Each step has
an independent uniform five-bit input. Before tick 2 it comprises
\(r\) and the four remaining second neighbors. Before tick 3 it
comprises the five neighbors of \(A\) other than \(B\). These inputs
are independent of the active bits and complete past at their step
by the two product arguments above. A phase tag describes the two
lookups on this finite schedule.

The [P8 positivity condition][p8] requires that each label matrix
be identically zero or strictly positive in every entry. For a
matrix \(M_\ell\) and any supported history with active-state
posterior \(p_h\), freshness and a fixed operation give the next-label
probability \(p_h M_\ell\mathbf 1\). This quantity is zero for all
histories if \(M_\ell=0\) and strictly positive for all histories
if \(M_\ell\) has strictly positive entries.

At the same third phase, \((0,0)\) has mass \(7/64\) and gives
\(\Pr(L_3=\bot\mid 0,0)=1\), while \((0,1)\) has positive mass
and gives \(\Pr(L_3=\bot\mid 0,1)=0\). Either choice for the
\(\bot\) matrix contradicts one of these laws. The contradiction
comes from the exposed histories and applies independently of the
finite active encoding, even if a separate positive table were
allowed at the known third phase. Thus the fixed positive
operation required for the P8 bound fails on this schedule.

## Scope of the result

The adjacent-pair comparison establishes a causal neighboring response
and an observed history law for the declared binary product preparation
and three-read projections. The third-phase obstruction is specific to
the gate that uses the second receiver's fresh bit as the next request.
Physical preparation, request production and an executing read coupling
remain open under [#866][physical].

[issue]: https://github.com/amaybaum/incompleteness/issues/1409
[authority]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7011681058
[rule]: https://github.com/amaybaum/incompleteness/blob/5809c6c7537f9844f643a94ba1a65b281b47bc1a/papers/SM.md#L294
[fixed]: https://github.com/amaybaum/incompleteness/blob/c7109d93099f8aa0c24f1d8885c0c10702bd1d87/verification/audits/foundations/p8-p12-rounded-cubic-20261119/RESULT.md#L102-L130
[bridge]: https://github.com/amaybaum/incompleteness/blob/1cf5374c25cef1bbc41db38c89a55cda7bc49033/verification/audits/foundations/p8-p12-bridge-20261119/RESULT.md#L143-L209
[p8]: https://github.com/amaybaum/incompleteness/blob/62edb8168ceeaa1cb5c5e6e779217aed069d63b1/verification/audits/foundations/a1-p8-history-bridge-20261119/RESULT.md#L9-L29
[physical]: https://github.com/amaybaum/incompleteness/issues/866
