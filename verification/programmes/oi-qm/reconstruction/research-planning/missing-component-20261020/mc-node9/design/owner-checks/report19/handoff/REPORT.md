# Fixed-rule aggregation: three finite components

## Result and status

Under the unchanged report18 update, explicit one-shot layouts write AND4, AND5 and AND6 into one raw D register at deadlines 3, 4 and 5. Their output degrees are exactly 4, 5 and 6 under affine input encoding. Every input-caused write through the deadline is covered by the record supplied here. A remote source simultaneously supplies a uniform independent word under the reserved-frontier prior.

**This is not an all-size aggregation construction.** There is no general layout algorithm, composition lemma, or untested-size prediction. The three verified sizes are finite component results. The user's scaling criterion, including a size beyond those used in discovery, remains unmet. A restricted extension search did not find a seven-input continuation from selected six-input layouts; this is neither an exhaustive search nor an obstruction theorem. No repository files were changed.

The construction also does not supply native preparation, an internal clock, reset, repeated use, angular emission laws, station-indexed preparations, or quantum equivalence. It does not alter the necessary-conditions checklist.

## Fixed dynamics

All bits and polynomials are over F2. On a cubic periodic lattice let S be the XOR of the six nearest neighbors, separately for each field. At every site and tick:

    A(t+1) = A(t-1) XOR S B(t)
    B(t+1) = B(t-1) XOR S D(t)
    D(t+1) = D(t-1) XOR S A(t) XOR [(S B(t)) AND (S D(t))].

Write U(t+1)=U(t-1)+H(SU(t)), where H(a,b,d)=(b,d,a+bd). The global update on two time slices is reversible: given U(t),U(t+1), recover U(t-1)=U(t+1)+H(SU(t)). The on-site H is also bijective, with inverse H^{-1}(x,y,z)=(z+xy,x,y). No rule, coupling or external control changes during a run.

## Explicit layouts

Coordinates in this table are before translation. Start with the three rows marked 3. Include rows marked 4 for the four-input device, rows marked 5 as well for five inputs, and all rows for six. Any slot not listed is zero within the readiness buffer specified below. Different occurrences of the same letter are constrained affine copies, not additional independent inputs.

| Added at size | Initial tick | Field | Position | Value |
|---|---:|---|---|---|
| 3 | 0 | B | (1,1,0) | a |
| 3 | 0 | D | (1,-1,0) | b |
| 3 | 0 | D | (0,0,2) | c |
| 4 | 0 | A | (0,0,4) | d |
| 4 | -1 | B | (0,0,3) | c |
| 5 | 0 | B | (4,-1,1) | e |
| 5 | -1 | B | (0,2,1) | c |
| 6 | 0 | D | (-6,-1,1) | f |
| 6 | -1 | A | (-1,-5,1) | e |

| Inputs | Deadline T | Receiver before translation | Terminal (A,B,D) |
|---:|---:|---|---|
| 4 | 3 | (0,0,1) | (d, abc XOR cd, abcd) |
| 5 | 4 | (0,-1,1) | (e, abcd, abcde) |
| 6 | 5 | (-1,-1,1) | (f, abcde, abcdef) |

Translate every position by minus the receiver position, putting the receiver at the origin. In these normalized coordinates all current payloads lie in B_T and all previous-slice copies in B_(T-1), where B_r is the integer L1 ball of radius r. The checker implements this translation explicitly. The extra cd in the four-input B output is disclosed, not discarded; the D register is nonetheless exactly abcd.

## Readiness, resources and access

For a device with deadline T use torus side L=6T+3 and source q=(3T+1,3T+1,3T+1), with coordinates modulo L. Pin all three current fields on B_(3T)(0) to zero except the n free input slots. Pin all three previous fields on B_(3T-1)(0) to zero except the indicated affine copies. Also pin both source triples U(-1,q),U(0,q) to zero. Everything outside these constraints is initially independent and fair. Inputs are initially independent and fair as well; any fixed input can instead be selected for the conditional statement.

This is an imposed ready distribution. Copies are preloaded and their correlations are charged. There is no native procedure here that prepares or tests this event. The device is one-shot: nothing is restored, erased or reset. Previous slices and intermediate fields retain information.

The specified device record contains **all three fields at every site of B_(2T)(0), at every tick -1,0,...,T**. Thus it exposes the original inputs, all copies, the intermediate signals, any return to the receiver, and the terminal output. This is deliberately not a privacy claim. The source record is all three fields at q at ticks 1,...,T. There are no calls, retries, heralds or physical clock registers in this model; tick labels are mathematical indices.

The initial cold buffer makes this entire device record deterministic given the inputs, for every exterior background. The current-slice backward dependency radius for a site recorded at tick t is at most t, and the previous-slice radius at most t-1. Hence B_(2T) through T depends only on current B_(3T) and previous B_(3T-1). No wrap occurs there because L>6T.

Conversely every input-dependent perturbation starts in current B_T or previous B_(T-1), and can move at most one edge per tick. It stays in B_(2T) through the deadline. Thus the record covers every input-caused write, including in the other fields. Background registers elsewhere can still change under their own dynamics; they are not claimed to be zero or publicly recorded. This specified access interface is not a physical access-closure theorem.

Let v(r)=(4r^3+6r^2+8r+3)/3 and M=3[v(3T)+v(3T-1)]. If m is the number of copy slots, the readiness event has M-n-m+6 zero pins and m independent copy equalities. Its codimension under uniform counting is J=M-n+6, with probability 2^{-J}. Each equality fixes one otherwise distinct previous-slice bit, so no input freedom is double-counted.

| n | T | L | Zero pins | Copy equalities | Total J |
|---:|---:|---:|---:|---:|---:|
| 4 | 3 | 21 | 5977 | 1 | 5978 |
| 5 | 4 | 27 | 14015 | 2 | 14017 |
| 6 | 5 | 33 | 27237 | 3 | 27240 |

These are conservative costs for the full quiet record buffer, not minimal gate costs. They should not be compared directly with report18's smaller receiver-only readiness event. The formulas for buffer counts are general geometry; T=n-1 is only an observation about these three layouts, not an all-n latency theorem.

## Exact record specification and finite verification

RECORDS.json gives the complete nonzero algebraic-normal-form (ANF) record. Its top-level keys are "4", "5", "6". Each value is a list of T+2 snapshots in time order -1,0,...,T. A snapshot consists of entries:

    [[x,y,z], field, [monomial_masks...]]

Fields 0,1,2 mean A,B,D. Bit j of a monomial mask selects input j (a,b,c,...); mask 0 means constant 1. Multiply selected inputs within each monomial and XOR the monomials. Every omitted site/field in B_(2T) is exactly zero. The table is the full device law, not only its final flag. There are respectively 208, 454 and 1022 nonzero coordinate-time-field polynomials.

The sparse polynomial recurrence in the checker independently derives these tables from the raw update on the infinite zero-background lattice. XOR is symmetric difference of monomial sets; multiplication unions variable masks with parity cancellation, enforcing x^2=x. Direct comparison with the included tables and with the monomial containing every input is exact. This gives a reproducible finite algebraic verification for each layout, not a proof for arbitrary n.

A second implementation updates every site of the actual periodic torus using bitpacked truth tables. Every unconstrained initial bit on both full-torus slices is assigned a seeded dense random value, held constant across all inputs. For each of two different dense backgrounds per size, the checker runs all 2^n assignments, compares every field in the entire specified device record against the ANF tables, and directly computes the output's ANF degree by a Boolean Mobius transform. Thus the degree check does not merely read the symbolic reference polynomial.

Finite random backgrounds are implementation checks. The causal-buffer argument above establishes background independence for arbitrary exterior values; the random samples alone do not.

## Source freshness and joint law

Reserve the three initial current bits at q+t e_x for each t=1,...,T. These 3T bits are outside all readiness constraints. The source dependency ball B_T(q) is disjoint from the device record's initial dependency balls, including its affine copies. On this torus the center distance is 9T+3, larger than 4T; the local source cone also does not wrap because L>2T+1.

Condition on every initial bit except this reserved frontier. For source tick t the triple at q+t e_x can reach q only by the unique shortest axial path. No source reading at earlier ticks depends on it. Along that path, with other frontier triples fixed, every intervening map in this triple has form z -> H(z+c)+d, a bijection. The second-order old term cannot contain that triple at the earliest arrival. Hence the current source triple is bijective in the new reserved triple conditional on the preceding frontier. The map from all reserved triples to the source word is triangular and bijective.

Consequently the source word is uniform on 8^T possibilities, for any complement assignment satisfying readiness, and independent of every input and the entire device record. No device signal reaches the source by T. This proves the joint factorization; independence is not inferred from separate marginal frequencies.

The checker additionally enumerates all 8^T reserved-frontier assignments (512, 4096, 32768), for each of the two dense backgrounds. It computes the shrinking exact source cone from the fully specified torus state and verifies that every source word appears once. This is **not** a full-torus simulation of every input-times-frontier combination. The full-torus input enumeration and the source-cone frontier enumeration are separate exhaustive factors, joined by the disjoint-dependency proof.

Writing U for the n inputs, Z for the source word, R for the device record and E for readiness, the exact claimed law is

    P(U=u, Z=z, R=r | E) = 2^{-n} 8^{-T} 1{r=R_n(u)}.

For fixed chosen u omit the factor 2^{-n}. An observer allowed to read reserved initial source bits would destroy the stated fresh-symbol interface; that expanded access model is not claimed here.

## Controls, replay and interpretation

The checker uses only the Python standard library, reads RECORDS.json, and writes only stdout. It has no network or subprocess calls, file writes or compilation. Checks use explicit exceptions and remain active under -O. The seeded generator is used only for reproducible dense-background tests, not as the asserted physical source.

A countercontrol changes a specified zero pin to one and recomputes the exact AND truth table. In normalized coordinates the first detected controls are current A at (T,0,0): 4/16 wrong flags at n=4, 24/32 at n=5, and 26/64 at n=6. These counts are conditional on the pin being one; they are not the error probabilities for a uniformly released pin. They establish sensitivity to a readiness violation, not minimality of every pin.

The package includes deterministic stdout and SHA256SUMS. The producer replayed the checker from a separate directory, normally and with -O, matching stdout byte for byte. This is reproducibility within the same investigation, not an independent external review.

The useful new result is that raw conjunctions beyond three inputs coexist with a complete bounded device record and a fresh remote source under the fixed nonlinear update. The unresolved aggregation task is a general wiring or interference-cancellation lemma that composes such stages with controlled copies, side signals, latency and workspace. Larger isolated search successes would not by themselves satisfy that task. Native preparation and a clock remain separate obligations even if that lemma is found.
