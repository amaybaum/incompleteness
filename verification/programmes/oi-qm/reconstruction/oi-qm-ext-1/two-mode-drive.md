# Gate B1: a conditional two-mode drive and its readout boundary

**Standing.** Paper-only research under #1169, authorized by #1031 comment 6686727803 and scoped by proposal #1169 comment 6686260789. This candidate and its algebra are submitted for independent review. Source snapshot: `f10bb2dd1a53b587b0060b54570b8264dc00d8f1`. The accepted Gate A contract is `endpoints.md` at `fdc3dd7f7356dc8f83693f1a2bd8b3a12d24b051`.

## 1. Question, source and result scope

Can one specified second-order, two-mode coupling supply a continuously driven mixing transition without postulating a quantum gate? Does a native record of the resulting real configuration then have a quantum measurement law?

The source template is the center-free second-order rule in SM §4.1 (the form lemma at line 224), with its explicit reversible phase-space update; Substratum §3.1 A1/A4/A5 distinguishes the finite symbolic rule from the assumptions of a real observer-level lift. A closed isolated pair is an additional candidate assumption here. No restriction of the full cubic lattice to such a pair is inferred.

GR §3.3 and `OIBridge/MinimalRepertoire.lean` already prove the phase-free control criterion (`control_of_phaseFree`, `oiPlusMin_iff_qm`, `carrier_general_oiPlusMin`) within their given complex operational interface. Those results, their exchanges/ancilla hypotheses, and their all-level quantifiers are reused. This unit does not repeat their Lie/control proof or the GeneralCarrier characterization.

The paper gives two candidate-scoped statements:

- With real two-mode coordinates, exact signed coupling and the specified controller, a finite positive word of reversible updates produces a continuous unitary family on one fixed complex-amplitude representation.
- With a specified native quadrature-sign record, that same amplitude dictionary fails to factor through the standard two-dimensional density matrix. The failure is an explicit two-protocol distinction, not a claim about all OI models or all quantum encodings.

Neither statement derives the required physical real-mode/control/access resources from the finite substratum. Neither establishes a native Born law, physical qubit, full control at all composite levels, or the two whole-model equivalences of Gate A. The elementary matrix identities carry no claim of mathematical novelty.

## 2. Candidate inputs and their status

| Input | Exact content used here | Source / status |
|---|---|---|
| Native update template | Second-order neighbor dependence, with the previous configuration retained | SM §4.1 and Substratum A4/A5 supply the template under their stated assumptions |
| E-pair | One isolated pair with symmetric off-diagonal coupling; all omitted modes are spectators during this protocol | Added candidate restriction; no physical isolation mechanism is derived here |
| E-real | The pair and its one-step memory have real coordinates `(x,y)` in `R^2 × R^2` | Added real-mode extension; not inferred from finite `Z_q` configurations or an unspecified coarse-graining |
| E-control | Each update may use a loaded signed coefficient `k` in `[-1,1]`, including zero, with exact values and repeatable switching | Added intervention resource; native availability and exact continuum precision are unsourced |
| E-clock | One causal reversible controller executes a finite list, with a common fixed macro duration and no future-program influence before the selected interaction | Explicit controller construction below; physical loading/isolation are added obligations under Gate A |
| E-prepare | The held initial law on `(x,y)` and fresh ready records is independent of the selected program | Required Gate A loading/preparation condition; point preparation used in the readout example is an added resource |
| E-read | A native binary sensor can copy `1[x_1>0]` into a fresh ready record; that stored record can then be read persistently | Independently specified candidate access, not a quantum instrument or Born rule; physical implementation is unsourced |

These inputs define a conditional candidate, not an adopted physical extension. The source check does not establish their independence, minimality or universal necessity. Each unsourced entry stays explicit.

## 3. One reversible primitive and one fixed carrier

Let `X = [[0,1],[1,0]]` exchange the two mode coordinates, so `X^2 = I`. Write the current pair as x and its retarded pair as y. For a coefficient k, use

```text
T_k(x,y) = (k X x - y, x),

         [ kX  -I ]
T_k   =  [  I   0 ].
```

The inverse is explicit: `T_k^{-1}(u,v) = (v, k X v - u)`. Thus the update is reversible both over `Z_q` (for coefficients in that ring) and over the reals. Reversibility requires neither a continuous alphabet nor a quantum probability rule. The continuum drive below uses E-real and E-control in addition.

At zero coupling,

```text
J = T_0 = [ 0 -I ],    J^2 = -I,    J^4 = I.
          [ I  0 ]
```

Identify `(x,y)` with the fixed amplitude vector `z = x + i y` in `C^2`. Multiplication by i is exactly the zero-coupling quarter-turn J. This is a real-linear representation of a pair of classical quadratures, fixed for every program. It does not identify a native configuration or ensemble with a quantum state.

An individual nonzero-coupling step is not complex linear on that carrier:

```text
T_k J - J T_k = [  0  -kX ],
                [ -kX   0 ].
```

It would therefore be incorrect to certify the primitive itself as a qubit unitary. The proposed intervention is a fixed-length macro word whose endpoint returns to the common complex structure. No intermediate step is assigned a quantum-instrument label.

## 4. Exact positive-word synthesis

Define two shears by positive words in the available primitives:

```text
Q_a = T_a T_0^3 = [ I  aX ],
                  [ 0   I ]

P_b = T_0 Q_{-b} T_0^3
    = T_0 T_{-b} T_0^2
    = [  I   0 ].
      [ bX   I ]
```

Products act on a state from right to left. Each shear costs four primitive updates. `T_0^3` supplies the needed inverse quarter-turn by forward steps; no operational inverse or time reversal is assumed.

The symmetric twelve-step word is

```text
C(a,b) = Q_a P_b Q_a
       = [ (1+ab) I   (2a+a^2 b) X ].
         [     b X      (1+ab) I  ]
```

Requiring this endpoint to commute with the fixed quarter-turn J fixes its compensation, rather than adding a fitted outcome probability:

```text
2a + a^2 b = -b
b(a) = -2a / (1+a^2),
c(a) = 1 + a b(a) = (1-a^2)/(1+a^2).
```

Consequently

```text
C(a) = [ c(a) I  -b(a) X ],
       [ b(a) X   c(a) I ]

z -> U(a) z,     U(a) = c(a) I + i b(a) X.
```

Since `c(a)^2 + b(a)^2 = 1`, direct multiplication gives `U(a)^* U(a) = I`. For example `a=1/2` fixes `b=-4/5` and `c=3/5`, yielding `U = (3/5)I - (4i/5)X`, which has two nonzero entries in each row and is non-monomial in this fixed mode basis.

For `|a|<=1`, all used primitive coefficients a and `-b(a)` lie in `[-1,1]`. Write `phi=-2 arctan(a)`; then `U(a)=exp(i phi X)` for `|phi|<=pi/2`. For any real theta, reduce it modulo `2pi` to `theta_bar` in `[-pi,pi]`, and set `a=-tan(theta_bar/4)`. Two identical twelve-step words then give

```text
U(a)^2 = exp(i theta X).
```

The complete family has a common twenty-four-update duration. Zero angle still uses a full program, with all coefficients zero. No data-dependent waiting time or setting-dependent preparation law implements the angle. Exact real parameter loading is precisely the unsourced E-control resource; this construction does not obtain it from a finite controller alphabet.

## 5. Autonomous control and preparation/prefix conditions

A controller contains a fixed list of twenty-four coefficients and a cyclic clock. At each mixing step, one common rule applies `T_{k_clock}` and advances the clock; the list is held unchanged. Given the previous clock value and the new mode coordinates, the explicit inverse of `T_k` recovers the old configuration. This gives one reversible controlled evolution, rather than choosing a new world dynamics for each experiment.

Different setting programs are loaded only into the declared controller fields. Until the first scheduled coupling, the joint law of the modes, environment, controller noise and ready/public records is held fixed. The evolution reads only the current instruction, so shared physical prefixes have identical laws before divergence. The same operation label uses the same program. Realistic preparation, isolation, noise and record mechanisms remain physical obligations; the ideal controller formula does not source them.

The all-level phase-free criterion is not discharged by this single pair. Availability of the same construction on every needed composite carrier, physical exchanges in the chosen carrier dictionary, spectator behavior, and compatible ancilla attachment/discard still require their own source and resource arguments.

## 6. Native readout and an exact density-dictionary obstruction

Use one fixed preparation `(x,y)=(e_1,0)`, independently of the program. Add a fresh ready bit r and the deterministic copy map

```text
(x,y,r) -> (x,y, r XOR 1[x_1>0]).
```

This map is a bijection. Its output bit is a native record obtained directly from a real coordinate; its probability is the held preparation measure of the indicated set. No trace/Born rule is used. Stored bits are read passively without writing them again; further measurements require fresh cells. A complete resource architecture for all Gate A protocols is not established by this one-record example.

Compare two programs, both of twenty-four mixing updates followed by this same fixed record operation:

| Program | Endpoint on z | Native x at the endpoint | Recorded bit |
|---|---|---|---|
| Two words at `a=0` | `I` | `e_1` | 1 |
| Two words at `a=1` | `(-iX)^2 = -I` | `-e_1` | 0 |

The native probabilities are 1 and 0 under the same point preparation law. The setting acts through the declared coupling after loading; there is no change of seed, decoder or held incoming preparation.

Under the proposed standard pure-state assignment `rho_z = z z^* / (z^* z)`, z and -z have the same density matrix, and conjugation by -I is the identity channel. Every fixed quantum instrument therefore gives the same outcome probabilities in these two programs. No such instrument can match the native bits above while preserving this carrier/operation/record dictionary.

This proves failure of that particular density-matrix factorization and dictionary. It does not rule out other native readouts, restrictions of accessible preparation, nonlinear/larger quantum encodings, or a physical phase-reference treatment on a different declared carrier. It preserves Main's general finite observable-law representation result. A classical amplitude mixer alone does not determine a quantum state/readout interface.

Any repair must physically establish an appropriate phase-congruent preparation/readout quotient, as well as the desired probability law. Simply declaring the native readout to be Born sampling, or choosing a hidden distribution to encode the desired quantum table, would add the answer as an assumption. No such repair is adopted here.

## 7. Paper controls and an independent consequence

| Check | Algebraic result | What it controls |
|---|---|---|
| Primitive inverse | `(u,v) -> (v,kXv-u)` inverts every T_k | Reversibility is independently checked |
| No-drive program | `a=b=0`, so C is identity with the same macro duration | No angle is hidden in a changed preparation or waiting time |
| Wrong compensation | `C(a,0)=Q_(2a)` fails to commute with J for `a!=0` | A generic pulse word is not silently called a quantum unitary |
| Endpoint norm | `c^2+b^2=1` conserves `||x||^2+||y||^2` at macro endpoints | Unit-amplitude norm is derived, not interpreted as probability |
| Fixed carrier | The same J and z-map are used for every setting | No per-setting complex-coordinate replacement |
| Loaded law / prefix | The held mode/ready-record law is independent of program until interaction; only the current instruction is read | Gate A's setting and causal requirements remain explicit |
| Readout counterexample | I and -I have the same density-channel action but yield opposite native sign records | Matrix control cannot substitute for a native measurement derivation |

The same dynamics also fixes sequential composition beyond the chosen non-monomial example. For two twelve-step macros, multiplication yields

```text
U(a_1) U(a_2)
 = (c_1 c_2 - b_1 b_2) I + i (b_1 c_2 + c_1 b_2) X.
```

Where `1-a_1 a_2 != 0`, this is `U((a_1+a_2)/(1-a_1 a_2))`; at a singular parameter, the displayed c/b formula still applies. If the combined parameter falls outside the single-block control range, keep the composed blocks or use the twenty-four-step angle construction rather than silently enlarging a knob's range. This composition and the norm law are consistency consequences of the same primitive, not new empirical predictions or adjustable fit parameters.

## 8. Source ledger and conclusion

| Obligation | What this unit supplies | What remains |
|---|---|---|
| Reversible mode coupling | Explicit T_k and inverse, following a stated second-order template | Physical isolation, real-mode realization, signed tunable coupling and exact precision are added unsourced resources |
| Continuous mixing | An exact finite positive pulse word on one fixed real/complex amplitude carrier | Native supply of E-real/E-control, not merely a formal observer-level lift |
| Quantum preparation/state map | A candidate amplitude representation and an explicit test of the standard rank-one density dictionary | The native preparation/readout quotient is not established and the chosen sign readout refutes this dictionary |
| Native probabilities | Deterministic pushforward of the held initial law for the named readout example | Born frequencies are not derived |
| Composite/full operational scope | Existing MinimalRepertoire and GeneralCarrier results are retained as conditional benchmarks | Their ambient interface and all-carrier/exchange/ancilla requirements are not supplied by one pair |
| Exactness | Exact real algebra and finite update count under listed ideal inputs | Finite-alphabet versions or approximation limits do not automatically supply J_exact(A) |

The outcome is a conditional amplitude-control component together with a concrete readout/dictionary obstruction and named physical sourcing gaps. It is not a native physical OI-to-QM reconstruction. No universal minimality, impossibility or irreducibility claim is made. The next scientific decision should address the physical status of these explicit inputs and the readout quotient, rather than reprove the already available control/characterization theorems.

All checks in this note are paper algebra. No code, numerical experiment, Lean build, simulation, physical test, manuscript edit or governed execution was performed for this unit.
