# NOTES-B2 — the embedded-observation principles transcribed to `W 3`, tested against K(Z_F)

Node B2 of `research/bridge`. Base L = `9f9f8257`. Paths under `verification/lean-mathlib/OIBridge/`. Evidence:
- [K] certified at L;
- [W] written here;
- [X] `experiments/b2_transcriptions.py`: 18/18 PASS, VERDICT B2-TRANSCRIPTIONS-EXACT. Run 1 is kept as `.run1.*`;
  it is identical in output, and only its header timestamp was misstated. The final run replays byte-identically;
- [A] audited archive record.

`K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F` is the stage-3 cone, rebuilt from the kernel's definitions. Self-duality, H1 and
H2 are taken from T6 TEST.md §3.3–§3.4 [A]. My own checks use only two elementary facts: `K ⊆ K*`, and the
membership test `y ∈ Q3 ∩ Z_F* ⊆ K`.

**Productivity test (fixed before the run).** The node is a gem iff some principle, transcribed without presupposing
the tensor composite, excludes K(Z_F) through a clause that passes the disguise test. Otherwise it is
CONFIRMING/ELABORATING.

## 1. How the transcriptions are written

A **pair theory on `W 3`** consists of two data:
- a token family `A₁`: affine maps of the ball, each available on one token in isolation;
- a pair family `A₂`: linear maps of `W 3`, each available on the pair. "Available" includes "maps the pair body
  into itself" (validity).

The two families are **independent data**. `A₂` is never constructed as tensor products of members of `A₁`. Writing
it that way would presuppose the composite action, which is what is under test. The kernel's carrier `W 3`, with
`actC` and `actT`, is used as given. It encodes local tomography (CD:96).

## 2. Results, principle by principle

### 2.1 `EmbeddedObservation` (EmbeddedObservation.lean:123; clauses (R) :98, (L) :106, (M) :114)

**Transcription.** There is a family of theories, one for the token carrier and one for the pair carrier, with:
- **(R)** the token's level-1 family, with the second token as ancilla, equals the pair's system family: `availExt₁ := A₂`;
- **(L)** availability is transported along carrier isomorphisms, here `Aut(K)` and SWAP;
- **(M)** the given token theory is the member at the token carrier.

**Derived clause tested.** The derived discard clause (`closure_of_embedded`, :184): for `g ∈ A₂`, the token map
`x ↦ margA (g (prodState x y))` maps the ball into the ball.

**Test.**
- Take `A₁` = all affine self-maps of the ball, so the token is drivable: it contains `rot3 t` and `cyc3`.
- Take `A₂ = Aut(K(Z_F))`. Its generators `cnot`, SWAP, `actC/actT nflip`, `actC/actT rot3 π` and the 32
  signed-diagonal pairs with `det D det D′ = 1` are each certified in `Aut(K)` [X E1a]. Each permutes `Z_F`, is
  orthogonal for `ipW`, and is `M ↦ V M V†` or `V Mᵀ V†` on all 16 basis tables.
- The discard clause holds on the listed points [X E1b].
- (R), (L) and (M) hold by construction: `A₂` is a group containing SWAP [W].

**Verdict: INDEPENDENT.** K(Z_F) satisfies the transcription with a fully drivable token. The reason is structural.
No clause of EO relates a level-0 family to a level-1 family, except (R), which identifies the level-1 families with
the composite's own system families, whatever those are. (L) transports availability along bijections and never
adjoins a spectator. The matrix-level counterpart is certified: `redundancy_fails` (ImplementationLocality.lean:207)
shows that the core, validity, reversible richness and embedded observation do not give observational independence.

### 2.2 `ObserverRecursion` (CompletedOI.lean:327), drivability form (stage 5 ζ)

**Transcription.** The pair slice is itself a drivable system: it carries a flow, a NOT on the flow, and an off-axis
`J`.

**Test.** All three ingredients are realized inside `Aut(K(Z_F))`:
- **Flow.** `U(w) = I + (w − 1) P_(1,1)` with `w = (3+4i)/5` is unitary, and `Ad U(w)` fixes every defect [X E2a].
  Hence it preserves `K(Z_F)` [W: it preserves `Q3`, is `ipW`-orthogonal and fixes `Z_F` pointwise].
- **NOT.** `N = Ad U(−1)` is an involution and moves a certified point of `K(Z_F)` [X E2b].
- **Off-axis J.** `J = actC nflip` is off-axis [X E2c]. The witness `x_i`, a rank-one table on
  `P_(1,1) e₀ + P_(−1,1) e₀`, is fixed by `J N J⁻¹` and moved by `Ad U(w′)` for every `w′ ≠ 1`: the only solution of
  `Ad U(w′) x_i = x_i` is `w′ = 1`, computed symbolically on the unit circle. A second witness `x_ii` is moved by
  `J N J⁻¹` and fixed by `w′ = 1`. Both witnesses are certified in `K`.

**Verdict: INDEPENDENT.** This confirms stage 5 ζ (D5 F1–F3 [A]) with my own exact code. The literal-transitivity
form does not hold even for `Q3`, so it is not admissible [A]. The extreme-ray transitivity form is stage 4's node T:
UNRESOLVED [A].

### 2.3 `HasParallelReferenceExtension` (ReferenceExtension.lean:447) = OI⁺-1 (CompletedOI.lean:129)

**Transcription.** For every `O ∈ A₁`, both `actC O` and `actT O` lie in `A₂`. That is, (b) for every available token
operation. The spectator `R` and the reindexing `e` of the kernel statement become the second token and its
placement.

**Test.**
- `K(Z_F)` satisfies the transcription iff `A₁ ⊆ Stab_loc(K(Z_F))`.
- `V4 = {I, R_x(π), R_y(π), R_z(π)}` on either token is certified in `Aut(K)` [X E3a].
- `S = R_z(π/2)`, `cyc3^{±1}`, `R_z(θ)` and `R_x(θ)` (`cos θ = 3/5`) on either token move `K` out [X E3b]. The
  witnesses pair to `−1/8` for `S` and `cyc3^{±1}` and to `−1/10` for `R_z(θ)` and `R_x(θ)`, each against a certified
  rotated Bell projector. All 64 pool elements are certified.

**Verdict: CONDITIONAL(α; L1).** The transcription excludes `K(Z_F)` as soon as one of these operations is available
on a token. L1 is the availability of the drive or `J` on a token; K∞-Act and K∞-Drive are OPEN. **The clause doing
the work is the transcription itself, the spectator clause. Disguise test: FAILS.** It restates I3.165's local-action
clause and I3.150–I3.153. The do-not-assume flag is on the transcription, not on the kernel definition.

### 2.4 `ContextStable` (ImplementationLocality.lean:359) and its one certified instance

**The certified instance.** `ContextStable substratumClass` (StructuralClosure.lean:261), where `substratumClass` is
`IsMonomial` (SubstratumInterface.lean:75): a permutation times an arbitrary diagonal.

**Transcription.** On one token the monomial qubit unitaries become `O(2)` about `z`. The dictionary check: `diag(1,
(3+4i)/5) ↦ R_z(θ)` and `X ↦ nflip` [X E4]. Context stability then becomes (b) for `R_z(φ)` (all `φ`) and for
`R_x(π)`, on either token.

**Test.** The symbolic flow law `⟨R_z(c,s)_τ z_t, R_z(π/2)_τ p_t⟩ = −s/8` holds identically in `(c, s)`, against a
certified witness. At `(3/5, 4/5)` the value is `−1/10` [X E4].

**Verdict.** The transcription of a **certified** kernel theorem excludes `K(Z_F)`. Three facts qualify this:
1. **No M→P bridge.** The transcription is by analogy. The matrix carrier's composite is the Kronecker product with
   the PSD cone by construction (T6 D1 [A]), so the exclusion is CONDITIONAL on the M→P transcription, which no item
   at L supplies.
2. **Disguise.** The clause doing the work is context stability's spectator clause for the continuous phase flow,
   which is (b) for `R_z(φ)`. **Disguise test: FAILS.**
3. **It does not force `Q3`.** The monomial seed (`φ₀ = (1,2,3,4)/√30`, `c = 513/512`) yields an exotic cone invariant
   under the whole monomial group (D5 §1.3(i) [A]).

This is the one place at L where a theorem, not a hypothesis, would exclude K(Z_F) after transcription. It does so
only through the spectator clause, and only for a class that is itself insufficient. ELABORATING.

### 2.5 `LayerFlowExecutable` (LiftAudit.lean:112; `levelPerm` :51)

**Transcription.** `gateFlow σ t` for `σ` the NOT is `P₊ + e^{iπt} P₋`. Its Bloch image is `R_x(πt)` [X E5]: `v = i`
gives `R_x(π/2)`, `v = −1` gives `nflip`, and `v = (3+4i)/5` gives `R_x(θ)`. `levelPerm σ n` keeps the ancilla a
spectator, so the every-level clause is (b) for the NOT's flow on one token. Level 1 alone is single-token and
pair-blind.

**Test.** `R_x(θ)` moves `K(Z_F)` out (`−1/10`) [X E5]. Level 1 holds: the rotation preserves the ball.

**Verdict.** The every-level clause is the spectator clause, so the transcription is CONDITIONAL on it. **Disguise
test: FAILS.** The drive alone is also insufficient: stage 4's Y4 seed, `c = 4609/4608`, gives an EXOTIC-E cone [A].
Inside `DerivedOI`, the every-level clause is redundant given level 1 and `HasParallelReferenceExtension` (D5 N1c
[A]).

## 3. Verdict of B2 (gem classification §A.31)

| principle | transcription vs K(Z_F) | clause that excludes K(Z_F) | disguise | outcome |
|---|---|---|---|---|
| EmbeddedObservation | satisfied (token fully drivable) | none | — | INDEPENDENT |
| ObserverRecursion (drivability) | satisfied | none | — | INDEPENDENT |
| HasParallelReferenceExtension (OI⁺-1) | violated iff `A₁ ⊄ Stab_loc` | the spectator clause | FAILS | CONDITIONAL(α; L1) |
| ContextStable (substratum class, certified) | violated (phase flow) | spectator clause for `R_z(φ)` | FAILS | CONDITIONAL (on the M→P transcription); insufficient (A4c seed) |
| LayerFlowExecutable | every-level clause violated; level 1 satisfied | the every-level clause | FAILS | CONDITIONAL (every-level clause); drive alone insufficient |

**Gem classification.**
- **CONFIRMING** stage 5. No principle at L excludes K(Z_F) through a clause that passes the disguise test. The two
  principles that are genuinely about embedded observation and observer recursion are satisfied by K(Z_F), even with
  a fully drivable token.
- **ELABORATING.**
  - The independence of EO is structural: no clause of EO adjoins a spectator. The matrix-level counterpart is the
    certified `redundancy_fails`.
  - The one certified spectator theorem, for the substratum class, transcribes to (b) for the continuous phase flow.
    That would exclude K(Z_F), but only through the spectator clause, and it is insufficient for `Q3`.
- **No NEW finding.**
