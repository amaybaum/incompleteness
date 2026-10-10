# K/R second pass — read-only, from L42

Baseline `fdebc6e3`. This covers the five items authorized after the owner's review of `KR-DISCRIMINATION.md`, whose
three refinements are adopted.
- The continuity-free route shows only that continuity is **not logically necessary** for a complex-QM
  reconstruction. In CDP, local tomography is one of five elementary axioms and purification is the extra postulate;
  tomography plus purification alone is not claimed to suffice.
- Parameter counts are diagnostics, not reconstruction theorems. The quaternionic `28 vs 36` count is the standard
  parameter-count obstruction, and no naïve quaternionic tensor product is treated as canonical. For field selection
  proper, Barnum–Wilce is the comparison.
- The K/R target is restated structurally. The question is whether native composition plus local tomography plus
  reversible pair mixing forces an **enlargement** of the real structure whose reversible group contains the missing
  phase directions — not whether phase gates, once postulated, give `su(D)`.

Exact checks: `kr_probes2.py` (15 PASS, 0 FAIL, log `kr_probes2.log`), numbered P7–P10 after the first pass's
P1–P6. Nothing is committed.

***

## 1. Native local tomography, stated before any field or algebra

**LT_native.** Take a composite of two visible systems `V₁, V₂`, preparation procedures `𝒫`, local experiment classes
`𝓔₁, 𝓔₂` (what may be done to each part and then read), and joint experiments `𝓔₁₂`. For preparations `P, P′ ∈ 𝒫`:
if every product experiment `(e₁, e₂) ∈ 𝓔₁ × 𝓔₂` gives the same **joint** outcome statistics under `P` and `P′`,
then every joint experiment in `𝓔₁₂` gives the same statistics under `P` and `P′`.

There is no dimension formula, no field and no algebra. The parameter count `K_AB = K_A K_B` is its consequence
inside a finite-dimensional GPT. The statement is **relative to the experiment classes**, and that turns out to be the
decisive point.

## 2. The test on the actual substratum composition

**At a single time, with the native experiment class, LT holds trivially and discriminates nothing.** The native class
is permutation interventions (`permClass`) followed by fixed-basis readout. At one time the visible composite's state
is a joint distribution on `V₁ × V₂` (the hidden sector is marginalized), and every joint statistic is a function of
that distribution. The product readouts' joint statistics recover the distribution. The native layer is a classical
simplex, and classical theories are locally tomographic.

**LT only discriminates fields for coherent completions — and there the native experiment class is not even
single-system tomographic** [P8].
- With only permutations and fixed-basis readout, `|+⟩⟨+|` and `|−⟩⟨−|` (qubit, and equally for rebits) give
  identical statistics in every experiment.
- The same holds for a coherent three-level superposition against the maximally mixed state.
- A non-permutation local operation (a Hadamard) separates them.

So for any coherent completion, single-system tomographic completeness is already a resource beyond the native class.
It is the R-type local operations, and local tomography can only be stated for the completed theory **relative to an
experiment class that already contains them**.

**Verdict on item 2.** OI's product/partition composition **implies** LT for the native classical layer (trivially)
and **leaves it undecided** for any coherent completion, because the experiment classes relative to which LT would
discriminate are not native. This agrees with `Main.md:212`: kinematic locality does not by itself give local
tomography.

This relocates the K question. A native route would have to be a **preservation** principle — "the completion adds no
globally invisible degrees of freedom relative to its own local experiments" — and not LT applied to the native
layer. The real completion violates such a principle [P2, P7]; the complex completion satisfies it. Whether
preservation is a native principle or new physics is exactly the K question, now sharply posed. [open]

## 3. The K/R bridge: countermodels first

The owner's boxed question: does native composition plus local tomography plus reversible pair mixing force an
enlargement of the real operational structure?

**(a) Without an interaction resource: no enlargement is forced (countermodel).** The minimal tensor product of two
discs (rebits):
- is locally tomographic by construction, since the joint space `ℝ³ ⊗ ℝ³` is spanned by products;
- carries local rotations reversibly, mapping product pure states to product pure states (256 exact cases) [P10];
- has no phase directions and no enlargement.

This confirms the owner's point that local tomography cannot manufacture a dynamical resource. Any forcing must come
from an interaction.

**(b) With a continuous reversible interaction (not native).** For bits whose state spaces are balls, local
tomography plus a continuous reversible entangling interaction forces the Bloch ball to be three-dimensional
(Masanes–Müller–Augusiak–Pérez-García 2014, as reported in `literature.md`; premises to be checked in the full text).
This is the forcing the question asks for, but it imports continuity, which a finite substratum does not supply
(§3 of `KR-DISCRIMINATION.md`).

**(c) With the native discrete interaction: the sharp open case.** The substratum's coupling is a bijection, so its
lift is a permutation unitary such as CNOT [P7: a 0/1 permutation matrix]. Two exact facts about the **real**
completion:
- `Y⊗Y` is orthogonal to the entire locally accessible span `L` of real-symmetric products, which is 9-dimensional;
- CNOT is not `L`-invariant: `CNOT (X⊗Z) CNOT^T = −Y⊗Y` [P7].

So in real QM the native permutation coupling carries a locally visible direction onto the locally invisible one and
back. The real completion therefore cannot be made locally tomographic by quotienting out `Y⊗Y` while keeping the
native coupling reversible.

The remaining countermodel question is **not** answered here: does *some* locally tomographic composite of two discs
exist — neither real QM nor its quotient — carrying local rotations **and** a reversible map that acts as CNOT on the
classical corners? If none exists, native permutation coupling + LT + real pair mixing forces local systems larger
than discs. That would be the enlargement, reached **without continuity in the interaction**.

This is a finite convex-geometry problem, and the next computation to attempt: find a bounded group generated by
local rotations and a CNOT-on-corners map that keeps the product states inside the maximal tensor product. Two
approaches were considered and are not sufficient:
- a forward-positivity linear programme alone does not decide it, because the projection of real CNOT is forward
  positive but singular;
- reversibility (bounded orbits) has to be imposed.

[open]

## 4. C versus purification, clause by clause

| clause | C (`IteratedAncillaClosure`) | CDP purification |
| --- | --- | --- |
| logical type | a closure rule on **operations** | an existence-and-uniqueness statement on **states** |
| object | attach a fresh **uniform (mixed)** ancilla to a composite, run an available enlarged operation, discard the ancilla ⇒ available | every state is the marginal of a **pure** state of a larger system |
| purity | none; the ancilla is maximally mixed | essential |
| marginalization | discard is the content of the rule | the marginal defines the purified state |
| uniqueness up to reversible | none | two purifications with the same purifying system are related by a reversible map on it |
| direction relative to dilation | *soundness* of dilation: dilate-then-discard stays inside | *completeness* of dilation: every process arises as a reversible interaction plus discard |

**C ⇏ purification — two exact countermodels** [P9].
- **(a) The classical simplex.** It satisfies the C-type closure (50 random rational maps). Every pure (vertex) joint
  state has pure marginals, so no mixed state has a pure dilation.
- **(b) The dephased class** — the kinematic content of the census cell with control failing (`diagTheory`). Diagonal
  states are closed under uniform attachment, diagonal-preserving channels and partial trace. A pure diagonal joint
  state is a basis state with a pure marginal, so the maximally mixed qubit has no purification among reachable
  states.
- **Control:** the Bell state purifies `I/2` — a **real** state, so purification does not separate ℝ from ℂ.

**What purification tracks in the kernel.**
- The pure seed is derived from a uniform ancilla, rank-one Lüders readout and reversible feed-forward
  (`uniform_readout_feedforward_seed`, `Purification.lean`), with Lüders licensing as the stated guard.
- Purification exists as mathematics (`purification_of_factorization`); Uhlmann uniqueness is proved inside ℂ
  (`UhlmannUniqueness.lean`).
- **Preparing** the purifying state, or realizing the relating reversible map, needs composite unitary control
  (`pureSeedPrep_available` with `hctrl`, `AncillaInterference.lean`).

So in this corpus operational purification tracks **R**, not **C**. The answer to "C + already-derived structure ⇒
some purification?" is: not without R-type control (countermodels (a) and (b), in which C holds and control fails).
With control, the existence clause follows from the derived pure seed; uniqueness remains a ℂ-internal mathematical
fact (a lead, stated without an operational proof here).

## 5. Literature closure

The primary texts cannot be read from this environment: the egress proxy blocks `arxiv.org`, and the earlier agent
found the publisher sites blocked too.
- **Confirmed from primary sources by the owner (recorded as such, not re-verified here):**
  - Pechukas: correlated initial states need not give CP reduced dynamics on the whole state space; product initial
    conditions do.
  - Buscemi: CP survives initial correlations exactly under the information-flow condition.
  - CDP: local distinguishability is one of five elementary axioms, and purification is the additional postulate.
  - Barnum–Wilce: within homogeneous self-dual/Jordan systems with a qubit and natural composite assumptions, local
    tomography selects complex QM.
- **Still UNVERIFIED:**
  - de la Torre–Masanes–Short–Müller (details);
  - Masanes–Müller–Augusiak–Pérez-García's premises;
  - Selby–Scandolo–Coecke's postulate list;
  - whether real QM satisfies all CDP axioms except local distinguishability;
  - Gross et al. on boxworld dynamics;
  - Hall's count of order-16 Hadamard classes;
  - the Vinberg citation;
  - Renou et al.'s full author list;
  - some page and volume numbers.

  These need a network policy that allows arXiv, or the owner's copies, before any interpretation is frozen.

## 6. Where K now stands

1. **Native LT is real but vacuous where it matters.** It holds for the native classical layer and is silent on
   completions, because the experiments that make it bite are R-type resources [P8].
2. **The live K principle is LT-preservation under completion**, not LT itself. The real completion breaks it, and
   under the native permutation coupling it cannot be repaired by quotienting [P7]; the complex completion keeps it.
   Whether preservation is native or additional physics is the falsifiable K-level question.
3. **The enlargement question has a clean answer only at the extremes.**
   - No forcing without an interaction [P10].
   - Forcing with a *continuous* interaction (literature; imports continuity).
   - The decisive case — the native *discrete* permutation coupling — is a finite, well-posed convex-geometry
     computation, not yet done [§3(c)].
4. **C is not purification and does not imply it** [P9]. In this corpus operational purification tracks R. The
   continuity-free lesson from CDP therefore does not move the field question onto C.

**Next computation, on direction:** the §3(c) existence question — a locally tomographic disc composite with local
rotations and a reversible CNOT-on-corners map. It is the first place where OI's native discrete coupling could force
the complex enlargement without continuity, or fail to.
