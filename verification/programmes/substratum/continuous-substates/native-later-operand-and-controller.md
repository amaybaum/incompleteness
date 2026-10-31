# Later native operand and public-controller timing

Research-only bounded unit on #1009, based on accepted
`488ee2b90fdd847582d8c7817ea9846fae663310`. The parent has independent
ACCEPT and successful CI #41188641449 (25 passed, one intentionally skipped).
Those verdicts do not accept this unit. No manuscript or physical-premise
change is proposed; no native field simulation is performed.

## Decision rule and inputs

Before the calculation, fix the original fewest-seed source law, rather than
the earlier carrier-changing J2 program:

\[
 E=(1,1\oplus m_Y,1),\qquad N=(m_Y,1,1\oplus m_Y).
\]

Use the retained exact q10 response table at L+1. Compute the complete
six-variable Boolean algebraic normal forms, and test all seven nonzero
linear parities of its three fields with every affine known-seed mask
(six coefficients for 1,u,mY,mR,a,b). The target is
\(t=1\oplus a m_R\). The decision domain is all 48 continuing source rows;
the other 16 rows are terminal diagnostics, never new reads or offered
carriers. Check both unknown x values sharing the same controls. A surviving
mathematical readout would still require native compilation and access.

Separately examine a hypothetical action at the existing public port 5:
can it enter after the prepared input cut, and when must it occur? A
supplied action is only a countercontrol. Do not adopt it as an operation
of the passive/read-stop contract. Retain all fields and correlations; no
reset, private read, nonlinear initial answer or #866 quotient is used.

The primary input is `native_route_v13/result.json` under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`:
4096 native responses in order x,u,mY,mR,a,b,Ecode,Ncode, raw code 4A+2B+D.
Its table-string SHA-256 is
`b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc`.
The reviewed large-time reduction and native table are reused, not recomputed
or replaced by a toy table. The probe pins the complete result file, the
`native_vread_v15/checks.py` preparation declarations and the shared interface
contract by SHA-256. These retained inputs are unchanged in this unit.

## Later computation under the original preparation

Write Q=U_(L+1)(q10), not the entire incoming 42-bit two-slice packet. On
the continuing domain (a,b) != (0,1), put c=a XOR b. Exact substitution in
the native table gives

\[
\begin{aligned}
 Q.A &= x\oplus u\oplus a,\\
 Q.B &=1\oplus a\oplus b\oplus c m_R
             \oplus b m_Y(1\oplus u)\oplus ux,\\
 Q.D &=1\oplus b\oplus c m_R
             \oplus(1\oplus c)(m_Y\oplus u)
             \oplus cx\oplus c m_Rx\oplus b m_Yx(1\oplus u).
\end{aligned}
\]

Multiplication is Boolean AND; addition is XOR. The probe also emits the
unique full-domain ANFs including terminal contexts and checks their direct
evaluation against every original table row. The displayed simplification
uses the continuing-domain relation ab=b; it is not asserted on failures.

In particular, the finite difference of Q.B under mR -> mR XOR 1, holding
x,u,mY,a,b fixed, is a XOR b. Thus the original native evolution does have
later mR-dependent nonlinear arithmetic: eight of 24 continuing pairs change
Q, all in the a=1,b=0 branch. This is a later internal dependence, not a clean
physical operand or an observer-readable calculation. It does not deliver a
signal backward to the previously excluded J2/N4 events.

There are no solutions among the 448 specified parity-plus-affine-mask
readouts, on the continuing rows alone. An additional post-calculation
diagnostic gives a stronger Q-only distinction: in all eight a=b=1 pairs,
the whole Q triple is independent of mR while the target 1 XOR mR changes.
For example, x=u=mY=0, a=b=1 gives Q code 6 for either mR, and opposite
target bits. Hence no function of Q and (x,u,mY,a,b), even a nonlinear
function, can recover this target on all continuing rows without another
mR-bearing input. This statement expressly excludes mR from the decoder's
additional inputs; supplying mR directly trivially changes the question.

These are counts of microscopic contexts, not probabilities. No result here
excludes a larger multi-site/two-slice operand, later computation, a native
route carrying mR separately, or another physical controller. In particular,
Q-only collisions say nothing about equality of the complete 42-bit packet
or its environment. The accepted original incoming preparation is unchanged.

## A conditional public-controller deadline

The old public port 5 is r=(0,S,0). Consider a *supplied* current-slice
perturbation at r at time S+4, holding the remainder of that two-slice
Cauchy state fixed. This is a comparison of hypothetical future trajectories,
not an allowed private write or a realization of a controller.

| Boundary | Earliest possible effect |
| --- | --- |
| Incoming current/previous packet at tau=L+3 | Excluded, by one/two ticks respectively |
| Next packet boundary q10-z | L+4, distance 77 |
| Packet center q10 | L+5, distance 78 |
| Next boundary if the action waits until tau | L+80 |

Here L=S+77. Moving the supplied action one tick earlier to S+3 puts it
in the input's causal cone, a rejection countercontrol. A controller using
this particular L+4 entry window therefore needs its action at S+4, before
the input cut but outside its causal past. The first possible interaction
with the prepared carrier is after the cut. A choice made only at that cut
cannot use this window. These timings do not require an unchanged output
carrier: measurement disturbance after preparation is allowed.

The path from r to q10-z is uniquely axial at first arrival. For fixed other
inputs, each step has form K XOR H(V XOR B), with the old-local K and other
neighbor sum B independent of the supplied first-front perturbation.
H(A,B,D)=(B,D,A XOR BD) is bijective. Their composition is therefore a
permutation of all eight possible triples. Distinct supplied values have
distinct first-contact triples for a fixed background. The probe checks
this bijective first-front control with nonzero varying K/B backgrounds.
It does not simulate native fields at these large times.

This conditional dependence is insufficient for a selectable instrument.
For example, toggling an independent uniform raw register produces a
different pointwise trajectory but exactly the same uniform marginal after
any such permutation. The probe checks that countercontrol as well.
A controller, its correlations and its record must be included before
inferring different operational laws from different conditional trajectories.

## Physical-source gate remains open

The declared passive/read-stop interface does not compile an action at this
public coordinate. Public visibility supplies a place to record a value;
it does not supply the ability to set or couple that value. Neither a
statistical label nor an assumed Cauchy perturbation implements a native
actuator. The broader OI read-write/action-dilation results distinguished
in the accepted parent audit remain separate from a native realization here.

A next candidate must source an autonomous controller under the original
preparation, with a physical setting register and a causal computation by
its stated deadline. Its entire earlier trajectory must preserve the
incoming preparation and relevant correlations; the hypothetical perturbation
alone proves no admissible original-time source for that controller. It
must retain old register information and all B/D residuals, rather than
erase or overwrite them without accounting. It must then establish the
joint law of the public setting/outcome/raw prefixes, timing, terminal
failures, environment and reusable outgoing boundary. Earlier terminal
branches remain terminal with no new attempt, read or offered carrier.
None of these open obligations is discharged by the timing table.

The new unit therefore finds a later original-preparation nonlinear
dependence and a precise prospective public-controller deadline, while
rejecting the specified Q-only compensation class. It does not construct
an available setting, a measurement or operational OI-QM equivalence.

## Bounded checks and replay

Run from the repository root:

```
python3 -B verification/programmes/substratum/continuous-substates/native_later_operand_probe.py
python3 -O -B verification/programmes/substratum/continuous-substates/native_later_operand_probe.py
```

The probe uses exact integers and only the standard library. It emits
structured JSON; any failed control emits VOID and exits 2 before a verdict.
Normal and optimized results agree. The parity solver uses both direct
448-law enumeration and Gaussian elimination, with direct substitution.
A planted nonlinear target plus affine mask is found, and an mR-erased
table is rejected. An independent polynomial fixture checks the ANF
transformation, and all original rows check the compact identities. The
one-tick-earlier geometry and equal-uniform-marginal controls prevent
promotion of causal contact into preparation independence or an instrument.
Four targeted mutation classes (source law, target dependence, input digest,
premature input contact) reject in normal and optimized execution.

The candidate-specific calculations and controls are not Lean-certified.
Independent review of this new unit is pending; parent acceptance is not
transferred. No native simulation, write, reset, new access/preparation,
workflow dispatch, F/E designation, readiness change or merge is included.
