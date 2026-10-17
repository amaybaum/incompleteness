# F2-2 — local continuity for candidate E1: result

Research record on a research branch. It is not a native round and not adopted, and it is not for
merge without separate review. It records the exact computations frozen in `RULES.md`, changes no
status and proposes no manuscript text.

## Provenance

- **Rules.** `RULES.md` was committed at `b5442420` before any computation of the round. The run
  follows it without amendment.
- **Files.**
  - `f2_2_exact.py`, sha256 `246adb2bc6590a3d84234f6937409f2042bba796d646eae633f6383a62a90e57`.
  - `f2-2-exact-output.txt`, its full stdout, sha256
    `e7baf45cfaa3ba33b980f3e3ab8db8b779a389fc17eb56536beaab65b079f0ca`.
  - The script imports `../f2-1-e1-consistency/e1_exact.py` by path, unchanged (sha256
    `e7d257bb…`, K0), and `../f2-1-e1-consistency/corrections/root_scope_check.py` (sha256
    `7c6ed2a0…`). It changes neither.
- **Replay.** `python3 -I f2_2_exact.py` was run twice; the outputs are byte-identical. Each run
  takes about 7 min and uses the standard library only. These are local runs, not `check-run`
  attestations.
- **Development runs.** Before the recorded run, development runs of the same script under the same
  rules fixed implementation errors (a field too small for one countercontrol duration, a vacuous
  form of K-D1, the counting of members at N = 1). No rule was changed, and only the recorded run
  counts.

## The candidate, as frozen

E1-L keeps E1's registration (R1–R4) and replaces F2-1's continuity rule. F2-1 took the principal
logarithm of the whole-system image. E1-L instead uses the update's own factorization into local
gates, ρ(L_M) = u^{⊗N} · Π δ_i(M_ii) · Π δ_ij(M_ij), and continuity acts gate by gate:

- **Each gate flows by its own generator.** The generator is supported on the gate's sites, and
  the same rule applies at every site and every pair.
- **A tick runs in two layers.** The coupling layer runs first and the free layer second, so the
  evolution is time-dependent.
- **The generator is a parameter of the law.**
  - Γ_all: every generator.
  - Γ_spec: the functions of the gate, infinitely many.
  - The principal member.
- **Repertoires.**
  - R_self: every symmetric coupling.
  - R_cf: zero-diagonal couplings only, the centre-free form of SM §3.1's update.
  - Each with the translations, and in an all-duration and a one-duration form.

## Verdict, as printed

```
outcome rule: L0, L1, L3 and C-OI hold; E1L-SELF-FULL and E1L-SELF-DENSE at every control size
VERDICT E1L-LOCAL-AND-SELF-CONTROLLING
```

Every control passed: K0, K1, K-L1, K-L3, and K-Lie, K-D1 (both directions), K-D2 and K-touch at
every size. K-mod p is not engaged: no modular reduction is used, and every decisive line is exact
over ℚ(ζ_n). No separated-failure cell was triggered.

## Cells

Control sizes: (q, N) = (3, 1), (5, 1), (7, 1), (3, 2). Locality cells also run at (3, 3).

### Locality and consistency [X, with W for Γ_all]

- **L0, factorization.**
  - The identity ρ(L_M) = u^{⊗N} D(M) holds exactly for every coupling tested: 3, 5, 7 and 27
    couplings at the control sizes, and 33 at (3, 3).
  - At t = 1 every member of Γ_all gives the update, because each gate's generator exponentiates
    to the gate [W].
  - Token `E1L-FACTORIZED`.
- **L1, uncoupled independence.**
  - U_AB(t) ∝ U_A(t) ⊗ U_B(t), checked by two code paths: 18 block-diagonal couplings at (3, 2)
    and (3, 3), 6 durations, principal and shifted members; 216 checks, all equal.
  - For Γ_all [W]: no gate crosses the blocks, so each layer generator splits.
  - **K-L1:** F2-1's composite principal-logarithm rule fails independence at
    t = 1/6, 1/4, 1/2, 3/4 and 3/2, and agrees only at t = 1.
  - Token `E1L-INDEPENDENT`.
- **L3, strict causal cone (3, 3).**
  - On four chains, at five durations up to t = 1, the Heisenberg images of X_1 and Z_1 commute
    with X_3 and Z_3, and conversely, for both members.
  - For Γ_all [W]: the coupling layer is a product of commuting gates on sites and edges, and the
    free layer is a product of one-site gates.
  - **K-L3:** a δ_13 term is detected on every chain.
  - **Comparison (not a control):** F2-1's composite rule breaks the cone on all four chains at
    t = 1/2.
  - Token `E1L-CAUSAL`.
- **C-OI.**
  - By L0 the integer-time images are F2-1's, so F2-1's C1 and C2 tokens at (3, 1), (3, 2) and
    (5, 1) apply. They are cited, not re-measured.
  - At (7, 1), F2-1's own functions give:
    - genuine images, generating a group of order 336 = |SL(2, 7)|;
    - intertwiner dimension 1 for all 7 couplings;
    - the Born law equal to the rooted law on all 889 words of length ≤ 6, from all 7 starts;
    - the two-time law exact on 49 protocols;
    - normalization and back-action exact.
  - C4(a) at q = 7: 42 of 49 output entries are not nonnegative reals.
  - Token `E1L-CONSISTENT`. The token covers these equalities only. Their two-time law is the law with one
    symplectic, back-acting meter; OI's monitored law, which reads the visible value without disturbance, is not
    reproduced (`../f2-census-checks/monitored_law.py`, check B [X]).

### Control content

The measured dimensions modulo the identity are 8, 24, 48 and 80 at the four sizes; full is
q^{2N} − 1. With the translations removed (K-Lie), the dimensions fall to:

- R_self: 4, 12, 24, 40;
- R_cf: 1, 1, 1, 22.

| repertoire | (3,1) | (5,1) | (7,1) | (3,2) |
|---|---|---|---|---|
| R_self, all durations | full, Γ_all | full, Γ_all | full, Γ_all | full, Γ_all |
| R_self, one duration (D1+D2) | dense, 16/16 Γ_spec | dense, 2048/2048 | dense, 2 097 152/2 097 152 | dense, 256/256 |
| R_cf, all durations | full, Γ_all | full, Γ_spec | full, Γ_spec | full: principal + 8 computed members |
| R_cf, one duration (D1+D2) | dense, 4/4 Γ_spec | dense, 8/8 | dense, 8/8 | dense, 64/64 |

How each entry is established:

- **R_self, all durations [principal X; Γ_all W].**
  - The integer-time group is the full Clifford group modulo phases: orders 216, 3000, 16464 and
    4 199 040.
  - Sp(2N, q) is transitive on nonzero vectors, so the Clifford adjoint action on sl(q^N) is
    irreducible.
  - For any choice of generators, the generated algebra is adjoint-invariant and contains a
    non-scalar element, so it contains su(q^N).
  - Reachability of the whole group from forward flows is Jurdjevic–Sussmann [L].
- **R_cf, all durations.**
  - The integer-time group is not Clifford. Its symplectic part has order 4, 4, 4 and 48, with
    2, 6, 12 and 4 orbits on nonzero vectors.
  - The principal member is full at every size [X].
  - Robustness comes from the touching test [X: integer feasibility, exact]:
    - **At (3, 1)** every orbit is touched for every member by a gate with one-dimensional
      eigenspaces, so the result holds over Γ_all.
    - **At (5, 1) and (7, 1)** the free-layer generator touches every orbit for every member of
      Γ_spec, so the result holds over Γ_spec.
    - **At (3, 2)** the orbits of size 16 and 48 are touched robustly; the two of size 8 are not.
      For each of them the joint system has lattice points, members whose generators all vanish
      on the orbit. The eight such members computed exactly are all full, through brackets.
      Fullness over Γ_spec at (3, 2) is therefore not established.
- **One duration [X for D1 and D2, W for the inference].**
  - **D1** is irreducibility of the generated group's adjoint action, decided exactly by the
    touching closure over the integer-time orbits.
  - **D2** is an element of infinite order modulo scalars, certified by |tr g|² ∉ ℤ[ζ_n].
  - D1 and D2 together give closure ⊇ SU(q^N). The first certified word is (free half-layer)·X_1
    for every free pattern at every size.
  - Under R_cf no Clifford generation is used: density is reached from a proper subgroup of the
    Clifford group together with the half-layer gates. F2-1 found that its own one-duration route
    needs self-couplings (its finding 2); under local continuity, at the tested sizes and for every
    Γ_spec member, it does not.
  - For R_self the [L] route (Campbell–Anwar–Browne Appendix D, owner's reading) also applies. It
    holds over Γ_all at q = 3 and 5, because no S ∈ SL(2, q) squares to J′ there, and over Γ_spec
    at q = 7.

### Escape from the known obstructions

- **(a)** u preserves no nonnegativity. This is F2-1 C4(a) at q = 3, 5, and C-OI above at q = 7.
- **(b)** (free half-layer)|0…0⟩ is Wigner-negative for every Γ_spec pattern at every size.
  - Over Γ_all at N = 1 the stabilizer-reachability test gives 0 of 12 rays at q = 3, 0 of 30 at
    q = 5 and **2 of 56 at q = 7**.
  - At (3, 2) the result follows from the product argument with correction 1 [W].
- **(c)** One-duration generating sets are finite, so the groups they generate are countable; the
  all-duration repertoires are continua.

## Findings

1. **Locality is a property of the continuity rule, not of the update.**
   - Gate-wise continuity gives exact uncoupled independence and a strict one-edge causal cone, for
     every generator choice.
   - The composite principal logarithm of F2-1 fails both.
   - The principal logarithm is not needed for any result here: the control results hold across
     the stated generator families.
2. **Control survives locality.**
   - With self-couplings, the all-duration algebra is full for every generator choice.
   - With self-couplings, one-duration density holds for every spectral choice.
3. **Control survives locality and the centre-free restriction at the tested sizes.**
   - All durations: full for the principal member everywhere, robustly over Γ_all or Γ_spec at
     N = 1. At (3, 2), full for the computed members only.
   - One duration: dense for every spectral choice, without Clifford generation.
4. **An alphabet dependence at gate level.**
   - At q = 7, SL(2, 7) contains S with S² = J′ (2 such S). Some non-spectral square roots of u are
     therefore Clifford, and two stabilizer states are reachable.
   - The Γ_all form of the free half-layer's non-Clifford and Wigner-negativity properties holds at
     q = 3 and 5 and fails at q = 7. The Γ_spec results are unaffected.
   - This limits a robustness statement at one alphabet. It says nothing about which alphabet
     nature uses.

## Classification (owner framing)

- **Extension-dependent.** Every positive result here is conditional on R1–R4 and T_loc, with
  T1–T3. None is OI-derived.
- **Open.**
  - Γ_all robustness for R_cf at N = 1 when q ∈ {5, 7}, and Γ_spec robustness for R_cf at (3, 2).
  - Any N > 3 and any size not tested.
  - A time-independent generator for a whole tick, which this round does not consider.
  - Whether the measured (c1) and (c2) meet Campbell–Anwar–Browne's hypotheses as that appendix
    states them.
- **Obstructed.** None found under E1-L at the tested sizes.

## Non-claims

From RULES.md:

- no general-N theorem, no kernel proof, nothing OI-derived;
- complex kinematics inherited;
- local continuity is an added hypothesis, not sourced;
- nothing about time-independent generators, minimality, dimensions other than q^N, or which
  alphabet nature uses.

Added by this run:

- Every result is internal consistency at the tested sizes; none is an empirical confrontation.
- The causal-cone cell is exact at (3, 3) only, with the general statement [W].
- Density is not exactness: the one-duration sets are countable.
- Exact availability from all durations rests on Jurdjevic–Sussmann [L].
