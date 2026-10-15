# F2-3 — the commuting generator family of E1-L: result

Research record on a research branch. It is not a native round and not adopted, and it is not for
merge without separate review. It records the exact computations frozen in `RULES.md`, as amended
before execution by `amendments/amendment-1.md`. It changes no status and proposes no manuscript
text.

## Provenance

- **Rules.**
  - `RULES.md` was committed at `39033d1b`, before any decisive computation.
  - `amendments/amendment-1.md` was committed at `946e51c9`, before the script existed. It
    replaced one K-gen clause that would have failed a valid generator.
  - The run follows both without further change.
- **Files.**
  - `f2_3_exact.py`, sha256 `21e347a8bbeab66160519ffc9a9b03869b2e8b2d6f2140d7999c0dd82ea5ea4e`.
  - `f2-3-exact-output.txt`, its full stdout, sha256
    `eb9746454a05dad077a8199b8a2e394a693e8688698627de53bccbef994b4ed7`.
  - The script imports, by path and unchanged:
    - `../f2-2-local-continuity/f2_2_exact.py`, sha256 `246adb2b…`;
    - through it, `../f2-1-e1-consistency/e1_exact.py`, sha256 `e7d257bb…`.

    K0 checks both hashes.
- **Replay.** One development run and two recorded runs. All three outputs are byte-identical;
  none needed an implementation fix. The runs use the standard library only and are local, not
  `check-run` attestations.
- **Design evidence** (floating point) is in `design/`, as cited in the rules.

## Verdict, as printed

```
outcome rule: F23-DIAG-FORCED and F23-DIAG-SUFFICES at every N = 3 size, graph and repertoire
VERDICT F23-DIAGONAL-AT-N3
```

Every control passed: K0, K-gen, K-pos (twelve cells), K-neg (two), K-mut (two), K-brute and
K-lie.

## The structural statements, proved [W]

The notation is that of E1-L (F2-2 `RULES.md` with correction 1): q is an odd prime;
δ_jk(b) = diag(ω^{−b y_j y_k}); one generator per gate type; a pair generator acts on {i, j},
i < j, with its first tensor factor at i; absent couplings contribute no term.

**S1, shared-site conservation.** Let G be an operator supported on a set of sites containing j
and not k. Let G′ be supported on {j, k}, with e^{2πiG′} ∝ δ_jk(b), b ≠ 0. If [G, G′] = 0, then G
conserves the registration value y_j.

*Proof.*
- G commutes with every function of G′, in particular with e^{2πiG′}, and so with δ_jk(b).
- Write δ_jk(b) = Σ_{z} Z_j(bz) ⊗ |z⟩⟨z|_k, where Z_j(c) = diag_{y_j}(ω^{−c y_j}).
- G acts trivially on site k, so [G, Z_j(bz)] = 0 for every z.
- At z = 1 the eigenvalues ω^{−b y_j} of Z_j(b) are pairwise distinct, because q is prime and b ≠ 0.
  So G commutes with each spectral projector |y⟩⟨y|_j of Z_j(b). ∎

**S2, diagonality.** Suppose that, for a value m, the repertoire has:

- a layer in which an edge of value m shares its first site with another pair term; and
- a layer in which an edge of value m shares its second site with another pair term.

Then G(m) is diagonal.

*Proof.* G(m) is the generator on every edge of value m. By S1 it conserves its first index and its
second index, so it commutes with every |y₁⟩⟨y₁| ⊗ |y₂⟩⟨y₂|. ∎

- Under the i < j orientation, a chain has both: the coupling with M_12 = m and M_23 ≠ 0 shares
  the second site of (1, 2); the coupling with M_23 = m and M_12 ≠ 0 shares the first site of
  (2, 3).

**S3, site generators.** Under R_self at N ≥ 2, every site generator g(a), a ≠ 0, is diagonal.

*Proof.* The coupling with M_ii = a and M_ij ≠ 0 places g(a) and a pair generator in one layer.
S1 applies with G = g(a), which has a single site. ∎

**S4, the classification.**

- *(⊆)* Under R_cf and R_self at every N ≥ 3, every coupling generator of every member of Γ_comm
  is diagonal: by S2 on the chain couplings both repertoires contain, and by S3 for site
  generators under R_self.
- *(⊇)* Every choice with diagonal coupling generators lies in Γ_comm, because diagonal operators
  in one product basis commute.
- The free-layer and translation generators are unrestricted by Γ_comm. The free layer's gates sit
  on distinct sites, and translations flow alone.
- So, for N ≥ 3, Γ_comm is exactly the set of choices with Γ_diag coupling generators.
- At N = 2:
  - under R_cf no layer has two terms, so Γ_comm = Γ_all;
  - under R_self, g(a) is diagonal (S3), and G(b) must commute with δ(b) and with the diagonal
    g(a) ⊗ 1 and 1 ⊗ g(c). That is, G(b) conserves y₁y₂ and every level set of the chosen site
    generators.

**When non-diagonal coupling generators coexist with commuting layers.** The two directions are
stated separately.

- *(Necessity, S1.)* A non-diagonal G(m) requires that, among the layers carrying an edge of value
  m, the shared sites never play both factor roles. Its off-diagonal entries are then confined to
  the unconserved directions:
  - if only first-site sharing occurs: between (0, y) and (0, y′);
  - if only second-site sharing occurs: between (y, 0) and (y′, 0);
  - if no pair term ever shares a site with it: within the classes of y₁y₂, intersected under
    R_self with the level sets of the site generators.
- *(Sufficiency, for the star.)* On R_star at (3, 3), take any choice in which every G(m) is a
  generator of δ(m) lying in the first-site-conserving commutant (of dimension 2q² − q = 15).
  Every such choice commutes on every layer.
  - On y₁ = 0, the two edges act on different sites.
  - On y₁ ≠ 0, both generators are diagonal.

  This is a written argument; K-mut checks one member exactly.

## Cells

### E1, the necessary commutant, and E2, sufficiency [X]

| (q, N) | graph | R_cf: layers, dim 𝒦(m) | R_self: layers, dim 𝒦(m) | E1 | E2 |
|---|---|---|---|---|---|
| (3, 3) | chain | 9, 9 for all m | 243, 9 | `F23-DIAG-FORCED` | `F23-DIAG-SUFFICES` |
| (3, 3) | complete | 27, 9 | 729, 9 | forced | suffices |
| (5, 3) | chain | 25, 25 | 3 125, 25 | forced | suffices |
| (5, 3) | complete | 125, 25 | 15 625, 25 | forced | suffices |
| (7, 3) | chain | 49, 49 | 16 807, 49 | forced | suffices |
| (7, 3) | complete | 343, 49 | 117 649, 49 | forced | suffices |

In every cell 𝒦(m) is the diagonal algebra, of dimension q², for every m ≠ 0.

- The conserved quantities are derived mechanically from every layer of the repertoire, not
  assumed.
- E2 checks two diagonal members on every distinct pair of co-occurring terms: the principal member
  and a state-dependent lift outside Γ_spec. Both commute exactly.

### E3, the N = 2 residual under R_self [X]

| q | site commutant | pair commutant, principal site generators | pair commutant, y/−y-separating site generators |
|---|---|---|---|
| 3 | dim 3, diagonal (`F23-SITE-DIAG`) | dim 17 > 9 (`F23-N2-NONDIAG`) | dim 9, diagonal (`F23-N2-DIAG`) |
| 5 | dim 5, diagonal | dim 49 > 25 | dim 25, diagonal |

So at N = 2 under R_self, non-diagonal pair generators exist exactly to the extent the chosen site
generators are degenerate.

- The principal choice is degenerate on y ↔ −y and leaves the extra dimensions.
- A diagonal choice with different integer lifts for y and −y removes them.

### C1 and C2, the surviving members at (3, 2) under R_self [X]

| member | all-duration algebra, dim mod I | half-layer at [[0,1],[1,0]] and [[1,1],[1,1]]: Schmidt rank | Clifford | diagonal |
|---|---|---|---|---|
| diagonal principal | 80 = full | 3 | no | yes |
| M_φ: G₀ + \|φ⟩⟨φ\| | 80 = full | 5 | no | no |
| M_C: G₀ + (1 − C⊗C)/2 | 80 = full | 3 | no | no |

- **`F23-NONDIAG-FULL` and `F23-NO-NEW-ALGEBRA`.** All-duration control is full for both
  non-diagonal members, as it already is for the diagonal member. They add nothing to all-duration
  control.
- **`F23-GATE-DIFFERENCES`.** They change the one-duration half-layer gates:
  - M_φ's half-layer has operator-Schmidt rank 5 rather than 3;
  - both of their half-layers are non-diagonal.
- These are differences of available gates at one duration, not a capability beyond it. Whether
  they change the closure of a one-duration repertoire was not part of the frozen cells.
- **Uninformative invariant.** The frozen Wigner invariant is uninformative here: |00⟩ is fixed,
  up to phase, by every diagonal phase and by both corrections, so h|00⟩ is a stabilizer state for
  all three members.

### Controls

- **K-gen.** Each exhibited K is a Hermitian projector commuting with G₀ and block-diagonal over
  the gate's classes. M_φ's and R_star's lie inside one class, and M_C's spans several
  (amendment 1).
- **K-neg.** M_φ and M_C fail on the (3, 3) chain. The first failing layer is [[0,1,0],[1,0,1],
  [0,1,0]], and their off-diagonal units lie outside the chain's diagonal 𝒦(m).
- **K-mut.**
  - R_star (site 1 is the first factor of both edges) gives dim 𝒦(m) = 15 > 9.
  - The member G₀(m) + |0⟩⟨0| ⊗ |χ⟩⟨χ| commutes on every R_star layer and fails on the chain.
  - S2's two-role hypothesis is therefore needed, and E1's test is not vacuous.
- **K-brute.** The nullspace of the commutation map, computed by explicit matrix arithmetic over
  ℚ(ζ₃) on all 81 matrix units, has dimension 9 for m = 1 and m = 2. This agrees with E1's
  combinatorial count.
- **K-lie.** Without translations, the principal member's algebra at (3, 2) has dimension 40 < 80.

## Findings

1. **Consistent local evolution has diagonal coupling generators from three sites on.**
   - Under E1-L's rule, requiring every coupling layer's generators to commute forces every
     coupling generator to be diagonal in the registration basis at every N ≥ 3, under both
     repertoires.
   - This is proved in general [W] and computed exactly at (3, 3), (5, 3) and (7, 3) on chains and
     complete graphs.
   - The freedom that remains in the coupling generators is discrete: an integer lift of the
     eigenphase at each basis state (Γ_diag). This is the per-mode logarithm freedom.
2. **The non-diagonal members are an artifact of small or single-role layer patterns.**
   - They exist at N = 2 under R_self, exactly when the site generators are degenerate. They also
     exist under single-role layer patterns such as R_star.
   - S1 states exactly where their off-diagonal entries may sit. None survives on a chain.
3. **Where they exist, they supply no additional all-duration control.**
   - At (3, 2) both named non-diagonal members give the full algebra, like the diagonal member.
   - They change only the one-duration half-layer gates.
4. **Consequence for the candidate.**
   - From N = 3 on, every coupling-layer flow e^{2πisG_coup(M)} is a diagonal phase flow at every
     duration. All basis-changing dynamics in E1-L come from the free layer and the translations.
   - F2-2's control results stated over Γ_comm are, at N ≥ 3, results over Γ_diag.
   - Γ_diag is strictly larger than Γ_spec, because the lifts may depend on the state and not only
     on the eigenvalue.

## Classification (owner framing)

- **Extension-dependent.** Everything here is conditional on E1-L: R1–R4, T_loc, T1–T3, complex
  kinematics inherited, one generator per gate type and the i < j orientation. Nothing is
  OI-derived.
- **Evidence levels.**
  - S1–S4 and the coexistence statement: written proofs, general in q and N, not kernel-checked.
  - E1–E3 and C1–C2: exact at the listed sizes, with K-brute as an independent recomputation at
    (3, 3).
- **Open.**
  - **Γ_diag robustness of F2-2's control results.** This is now the sharp form of the robustness
    question:
    - one-duration density under both repertoires (F2-2 established it over Γ_spec only);
    - all-duration fullness under R_cf at N ≥ 3. Under R_self the Clifford argument already covers
      every choice.
  - Orientation conventions other than i < j, and swap-symmetric generators. For the latter every
    shared site plays both roles, so S2 applies directly.
  - Time-independent generators for a whole tick, which neither F2-2 nor F2-3 considers.
- **Physical sourcing.** Local continuity, the commuting-layer requirement and the gate-only rule
  remain added hypotheses with no physical source. This round shows what they force; it does not
  show that nature imposes them.

## Non-claims

From RULES.md:

- no kernel proof;
- nothing about other orientations except K-mut's single-role example;
- nothing about time-independent tick generators, other gate sets or other locality notions;
- nothing about which alphabet nature uses, or whether nature realizes E1-L.

Added by this run:

- C2 compares gates at one duration. It does not decide whether the non-diagonal members change
  the closure of any one-duration repertoire.
