# F2-5 — OI's operational primitives through E1-L's dictionary: result

Exploratory research record on the F2 research branch, kept separate from BG-2 and from P0's locality work. It is not
a native round, adopts nothing, and is not for merge without separate review.

## Provenance

- **Rules.** `RULES.md` was committed at `6719ffeb` (blob `da5c3f6c`), before the script existed.
- **Amendments.**
  - `amendments/amendment-1.md` was committed at `9f6d8f20`, before the script existed. It corrects K-weyl's sign and
    defines the `N`-site phase-point operators from `N`-site Weyl operators and parity.
  - `amendments/amendment-2.md` was committed at `cc37d4ab`, after one development run and before the recorded runs.
    - That run used script sha256 `d1c51433…` and gave output sha256 `3c9eda38…`. It printed `OD-NOT-READ`, with OD-AD
      failing and every control green.
    - The diagnosis was a mismatch between the `N`-site site order and the Kronecker order, `A(z₁, z₂) = A(z₂) ⊗ A(z₁)`.
    - The amendment fixes the order and adds the control K-order. The development run's tokens are not used.
- **Files.**
  - `f2_5_dict.py`, sha256 `211ce708…`: standard library only, exact `ℚ(ω)` arithmetic.
  - `f2-5-dict-output.txt`, sha256 `43ddcbd7…`.
  - `supplementary/registered_prior_check.py`, sha256 `a353f050…`, and its output, sha256 `fe0bee06…`. It decides no
    cell, and it pins `f2_5_dict.py` by hash.
- **Replay.** Two parallel runs under `python3 -I`, about 26 s each, are byte-identical (K0). The supplementary check
  also replays identically. These are local runs, not `check-run` attestations.

## Verdict, as printed

```
TOKEN OD-SUB-LINES
TOKEN OD-REV-CLIFFORD
TOKEN OD-PREP-REGISTERED-UNIFORM
TOKEN OD-READ-BACKACTION
TOKEN OD-AD-TRANSFER
TOKEN OD-COMP-STABILIZER
TOKEN OD-HOLD-STROBOSCOPIC
VERDICT OD-READ
checks: 16, failures: 0
```

These controls passed: K-weyl, K-pp, K-psd, K-choi, K-AGL, K-psd-neg, K-order, K-cov-neg and K-psd-agree. The LDL and
characteristic-polynomial PSD tests disagreed on no matrix.

## 1. Measurements (q = 3)

| cell | measured |
| --- | --- |
| OD-SUB | Every `A(z)` is indefinite. Of the 84 three-point subsets of `Conf`, exactly the 12 affine lines give a PSD operator |
| OD-REV | Of all 362880 permutations of `Conf`: 432 preserve lines, and they are exactly `AGL(2,3)`; 216 give a CP map, exactly `ASL(2,3)`; 216 are positive and not CP, `AGL ∖ ASL`, with `Φ ∘ θ` CP. The other 362448 send a stabilizer state to a non-PSD operator |
| OD-PREP | Every point-configuration law maps to a non-state. Of the 84 registered preparations (3 values × 28 hidden priors), exactly 3 are states: the uniform prior at each value. The counting measure maps to `I/3` |
| OD-READ | For `k = 0, 1, 2`: the non-disturbing readout is not CP; the re-randomizing readout equals `ρ ↦ Π_k ρ Π_k`; the two agree on diagonal states |
| OD-AD | At `N = 2`: `A(z₁, z₂) = A(z₁) ⊗ A(z₂)` on all 81 points; attaching the counting measure gives `ρ ⊗ I/3`; marginalizing site 2 gives `tr₂` |
| OD-COMP | At `N = 2`, 40 Lagrangian subspaces. Each maps to a rank-one projector: the 16 products of lines give product states, the other 24 maximally entangled states |
| OD-HOLD | The free leap's covariance unitary satisfies `U A(z) U† = A(Jz)`, `U⁴ ∝ I` and `U² ∝ Π`. Lüders registration is idempotent. After one free tick the registered value is no longer certain; after four it is again |

**Supplementary, deciding nothing.** At `N = 2`, take registered values `(c₁, c₂) = (a, b)` and a hidden prior on
`(p₁, p₂)`:
- the priors `p₁ = p₂` and `p₁ = −p₂` map to non-states at all 9 registered values;
- the uniform prior maps to a state at all 9.

## 2. Written statements [W]

- **Registered preparations.** In the position basis, `Σ_ξ ν(ξ) A(a, ξ)` has diagonal entry 1 at `|a⟩`. Its only
  other non-zero entries pair `|a + y⟩` with `|a − y⟩`, with value `ν̂(2y)`, for odd `q`.
  - It is PSD iff `ν̂(k) = 0` for every `k ≠ 0`, that is, iff `ν` is uniform.
  - Take a fully registered preparation on `N` sites, with every site's current component fixed. The same argument,
    with `y ∈ V^N`, gives PSD iff the joint hidden prior is uniform on `V^N`, and hence a product across sites.
  - The argument constrains only laws that fix every registered value. It says nothing about laws that leave some
    registered value free.
- **Born weights.** `Σ_ξ A(k, ξ) = q |k⟩⟨k|`. So the registration probability, which is the hidden-half marginal
  `Σ_ξ W_ρ(k, ξ)`, equals `⟨k|ρ|k⟩` for every `ρ`, Wigner-positive or not. OD-READ's equality with the Lüders map
  checks this on the operator basis.
- **Positivity of `AGL ∖ ASL` at `q = 3`.** At `q = 3` every linear part has determinant `±1`. For every
  `π ∈ AGL(2,3) ∖ ASL(2,3)`, `Φ_π = (Φ_π ∘ θ) ∘ θ` is a CP map composed with a positive map, so it is positive.
  Positivity forces lines to lines (OD-SUB at `q = 3`), so at `q = 3` the positive set is exactly `AGL(2,3)`.
  - For `q ≥ 5` this does not extend. A linear part of determinant `d` factors as `diag(1, d)` times a symplectic
    map, and `Φ_{diag(1,d)}` has an exact non-positivity witness for every `d ∉ {1, −1}` at `q = 5, 7, 11, 13`
    (`../f2-census-checks/scale_gauge.py`, check D: written reduction, exact witnesses). Within `AGL(2,q)` the positive images there are those of
    determinant `±1`; whether positivity forces lines to lines at `q ≥ 5` is not checked.

## 3. The five ingredients

The table uses the owner's four categories. "OI" means the adopted kernel on `ℂ^Conf`; "image" means through the
dictionary.

| ingredient | OI on `ℂ^Conf` | image under E1's dictionary | category for E1-L |
| --- | --- | --- | --- |
| **preparation** | Only the uniform attach is granted (OperationalAssembly.lean:630). A pure seed comes from attach, configuration readout and a swap (`pureSeedPrep_available_of_swap` :675; Purification.lean:115) | Point configurations, OI's seeds, are not states. Registered preparations are states exactly with the counting measure on the hidden half. The uniform attach maps to `I/q` | **Derivable with an explicit bridge**, the dictionary, in modified form: uniform attach, then registration (Lüders, OD-READ), then a Clifford shift, gives `|0⟩`. Other pure states need `T`. **Contradicted** by positivity: point-configuration preparations, and every non-uniform hidden prior on a fully registered preparation. That is a special case of Main.md:60's structured priors. Correlated laws that leave registered values free can be states (OD-COMP) |
| **measurement** | Lüders readout of the configuration basis (`readout_is_localLuders` :658), which resolves both components of a site | A non-disturbing readout of the registered component is not CP. The re-randomizing readout is exactly Lüders. The registration law is the hidden-half marginal, which is the Born weight for every `ρ` [W] | **Derivable with the bridge**: projective registration with back-action, and Born weights as the hidden-half marginal. Back-action is forced, not chosen. **Contradicted:** OI's non-disturbing readout. Other bases need `T` followed by registration. POVMs need an ancilla and control (Naimark [L]) |
| **holding a state** | — (not addressed in the kernel) | Every fourth free tick is the identity channel. Registration is repeatable, and one free tick does not hold the value | **Available stroboscopically**, from the substratum's free leap. Holding at arbitrary times needs control. Error accumulation is open |
| **ancillas** | Uniform attach and discard are structure fields (:594–649) | Both transfer exactly (OD-AD) | **Available through the bridge.** A pure ancilla is a registered preparation. Iterated ancilla closure remains its own condition (RankGapTheory.lean:702) |
| **composites** | A product configuration space; spectator adjunction (`instAvail_withSpectator`, ImplementationLocality.lean:820) | Phase-point operators factorize. Correlated laws on Lagrangian subspaces map to entangled stabilizer states (OD-COMP) | **Available through the bridge** for tensor structure and stabilizer entanglement. **Independent** for Bell violation: Wigner-positive states with Clifford operations admit a noncontextual model [L: Veitch et al. 2012; Howard et al. 2014], so violation needs `T`'s sub-period flows. H-Bell stays open |

**Reversible operations.** At `q = 3, N = 1`, of OI's configuration permutations only `ASL(2,3)` acts as quantum
operations, 216 of 362880. Two kinds of OI's maps are positive but not CP at `q = 3`:
- the exchange `(p, c) ↦ (c, p)`, whose determinant is −1;
- every other `det ≠ 1` linear map, which at `q = 3` has determinant −1.

At `q ≥ 5` a linear map of determinant `d ∉ {1, −1}` is not even positive (check D [X]).

These are transpose-type maps; compare `transposeMap_not_kraus`, CompositeSoundness.lean:382. Both the bare read-write
copy and the non-affine bijections lack a physical image, which agrees with thread H's P6.a and P3.a (numerical there).
So E1-L does not extend OI's operational theory: it keeps its affine symplectic part and adds `T`.

## 4. Findings

**O1. E1-L keeps exactly the Clifford part of OI's reversible operations (OD-REV).** Thread H stated that the
configuration-bijection class is "replaced, not enlarged". At `q = 3, N = 1` this is now exact: of OI's permutations,
CP images are exactly the affine symplectic ones, and positive images exactly the affine ones. The second statement
is specific to `q = 3`; at `q ≥ 5` affine maps of determinant `∉ {±1}` are not positive (check D [X]).
**Classification:** ELABORATING, as an exact upgrade of thread H's E1(b) and P3.a.

**O2. Positivity under the dictionary forces the counting measure on the hidden half of a fully registered preparation,
and forces back-action on registration (OD-PREP, OD-READ, [W]).**
- These are not two choices but one constraint. A registered value is a state only with a uniform hidden half, and a
  registration is CP only if it re-randomizes the hidden half.
- Thread H's P-2 (numerical P2.c) becomes exact here.
- Its conflict with Main.md:60's structured priors becomes a contradiction under the dictionary, but only for fully
  registered preparations: a non-uniform hidden prior with every registered value fixed has no physical image.
- Correlated laws that leave the registered values free are not excluded. OD-COMP maps the uniform laws on
  non-product Lagrangian subspaces, which are correlated across sites in both components, to entangled stabilizer
  states.
- **Classification:** NEW. This is the exact form, plus the identification of preparation and back-action as one
  positivity constraint.

**O3. OI's pure-seed route breaks at the readout under the dictionary, and a back-acting variant replaces it.**
- The kernel route resolves the full configuration of a site: uniform attach, readout, swap
  (`pureSeedPrep_available_of_swap`).
- Under the dictionary, that readout and its point-configuration seed have no physical image.
- The route that does transfer is uniform attach (`I/q`), then registration of the current component (Lüders), then a
  Clifford shift, giving `|0⟩`. This has the same form as `uniform_readout_feedforward_seed` (Purification.lean:115),
  with registration in place of configuration readout.
- **Classification:** NEW. It is a hidden assumption in reading OI's preparation theorems as transferring to E1-L.

**O4. Born weights are the hidden-half marginal under the dictionary, for every state [W, checked through OD-READ].**
- In the linear sector this is F2-1's exact match of the Born marginal with the rooted law (F2-1 RESULT.md:105–106).
- The written statement extends it to every `ρ`, including negative-Wigner states reached by `T`, for registration of
  the current component.
- **Classification:** POSITIVE. It validates the reading "registration = trace-out of the hidden half". It does not
  derive the dictionary.

**O5. Attach, discard and site composition transfer exactly, and stabilizer entanglement is already in the image of
OI's correlated laws (OD-AD, OD-COMP).**
- What separates the image from full composite quantum mechanics is contextuality and Bell violation, which require
  `T`. The corpus records the same boundary for OI's own monomial protocols: every available effect is diagonal, and
  the protocols give CHSH ≤ 2 (E-bell-composite.md:205–213, :369–371).
- **Classification:** CONFIRMING.

## 5. The weakest additional principles, on this evidence

Relative to OI's adopted structure, which here means the counting measure as default, the product configuration space,
and the linear symplectic leap, the audit gives the following.

**What E1-L must posit:**
- **R, the dictionary.** An amplitude description of registered sites, with positivity of descriptions as the
  criterion for being physical.
- **T, sub-period flows.** These are needed for non-Clifford control, non-stabilizer states, other measurement bases
  and Bell violation.

**What follows from R together with OI's adopted structure** [X at `q = 3`, `N ≤ 2`; W]:
- registered preparations with the counting hidden prior;
- registration with Lüders back-action;
- Born weights as hidden-half marginals;
- the uniform attach and the discard;
- tensor composition with stabilizer entanglement;
- Clifford reversible dynamics;
- stroboscopic holding.

**What R excludes from OI's admitted operational content:**
- point-configuration preparations;
- non-uniform hidden priors on fully registered preparations;
- non-disturbing readouts;
- non-symplectic configuration bijections.

E1-L is therefore not a conservative extension of OI's operational theory. Which of these exclusions OI can afford is a
question for the framework, recorded in §6.

**Still not supplied by R and T on this evidence:**
- **iterated ancilla closure**, an independent completion condition;
- **holding at arbitrary times**, and error accumulation;
- **the measurement model**, meaning what in the substratum realizes registration;
- **local dimensions other than powers of an odd prime**;
- **H-Bell's spatial realization.**

## 6. Cross-propagation and assumption-watch

- **To P0's locality work** (branch `research/p2-locality-sources-20261015`, `p0-locality-sources/RESULT.md` L3).
  There, hidden-sector independence across an uncoupled cut held under the counting or record-conditioned
  maximal-entropy reading of Main Lemma 3. It failed under the actual-orbit law and under structured priors.
  - **What is established.** Under the introduced dictionary, positivity selects the uniform hidden prior for a fully
    registered preparation [W]. The two tested correlated priors, `p₁ = p₂` (P0's E-pri) and `p₁ = −p₂`, fail
    positivity at every registered value at `N = 2` (supplementary [X]).
  - **What is not established.**
    - That every correlated physical state is excluded. Correlated laws on Lagrangian subspaces map to entangled
      stabilizer states (OD-COMP).
    - That any of P0's ensemble readings is globally forbidden. Those readings are laws on OI's `Conf`, and only their
      restriction to fully registered preparations is constrained here.
    - That the selection follows from OI's axioms alone. It is a consequence of the dictionary E1-L introduces.
- **Assumption-watch marker.** A claim that an OI theorem on `ℂ^Conf` transfers to E1-L must check whether the theorem
  uses:
  - a point configuration;
  - a readout of both components of a site;
  - a non-uniform hidden prior on a fully registered preparation;
  - a non-disturbing readout of the registered component (OD-READ);
  - a non-symplectic bijection.

  Each of these has no physical image under the dictionary.
- **Tension recorded for review.** Main.md:60 admits structured hidden priors as realization data. E1-L's dictionary
  excludes the non-uniform ones on fully registered preparations, and only those. This is the case of the conflict
  thread H listed as a control conflict that is now exact at `q = 3`.

## 7. Open, and non-claims

**Open.**
- General odd `q`, and `N ≥ 3`. Here only the literature and [W] cover them.
- The written statements' independent review, and Lean certification where feasible, before any adoption.
- The measurement model, error accumulation in holding, iterated ancilla closure, non-prime-power local dimensions, and
  H-Bell.

**Non-claims.**
- **The dictionary is E1's posit.** Physicality is judged in the quantum description E1 assumes. Nothing here shows
  that OI forces quantum mechanics.
- **Nothing is adopted, and nothing is said about `q = 2`.**
- **No manuscript text is proposed.** The Main.md:60 tension is recorded, not resolved.
- **Correctness bands are unchanged.** This is consistency-axis work (§A.23).
