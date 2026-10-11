# NOTES-B19 — pair availability is token availability, in design

Node B19 of `research/bridge` (round 5). Base L = `9f9f8257`. Evidence levels as in NOTES-B14. Reading: every
statement of this node is an availability statement (the kernel's `InstAvail` protocols on the token and pair
carriers); none is about the invariance of a pair cone on `W 3`.

## 0. Question

NOTES-B14 §2 argued in writing, from kernel lemmas, that for a context-stable, label-invariant architecture the two
predicates of `BridgeAvail.lean` coincide: `PairAvailAt 𝓘 arch U n ↔ TokenAvailAt 𝓘 arch U n`. The round-5 directive:
state and prove it as a design theorem, both directions or the provable direction with the other stated as the open
half, so that "the decision falls at the token, not in the pair context" (B14-2, B14-4) is [D].

## S0. Design, productivity test and predictions (written 2026-10-11T07:39:54Z, before any run or dispatch)

**Design.**
- **token ⇒ pair** (`pairAvail_of_tokenAvail`, hypotheses `ContextStable 𝓘` (I4.29) and `LabelInvariant 𝓘` (I4.30)).
  From `InstAvail 𝓘 (Fin 2 × Fin n) Unit (conjChannel (tokOp U n))`, the kernel's `instAvail_spectator`
  (ImplementationLocality.lean:789) adjoins token A as an uncoupled spectator: `InstAvail` at
  `Fin 2 × (Fin 2 × Fin n)` of `amplRefL (Fin 2) (conjChannel (tokOp U n)) = conjChannel (1 ⊗ tokOp U n)`
  (`amplRefL_conjChannel`, :697); `instAvail_transport` (:644) along the associator
  `(Equiv.prodAssoc (Fin 2) (Fin 2) (Fin n)).symm` carries it to the pair carrier `(Fin 2 × Fin 2) × Fin n`, where
  `transport e (conjChannel V) = conjChannel (reindex e e V)` (`transport_conjChannel`, SpectatorBridge.lean:357) and
  the reindexed `1 ⊗ (U ⊗ 1ₙ)` is `(1 ⊗ U) ⊗ 1ₙ = pairOp U n` entrywise (`reindex_assoc_tokOp`, a `ring` identity).
- **pair ⇒ token** (`tokenAvail_of_pairAvail`, hypothesis `LabelInvariant 𝓘` (I4.30) only). From
  `InstAvail 𝓘 ((Fin 2 × Fin 2) × Fin n) Unit (conjChannel (pairOp U n))`, transport along the relabelling `toEnd n`
  that moves token A to the last factor gives `conjChannel (tokOp U n ⊗ 1₂)` on `(Fin 2 × Fin n) × Fin 2`
  (`reindex_toEnd_pairOp`, entrywise); the kernel's discard protocol `InstAvail.discard` with `m = 2`
  (ImplementationLocality.lean:285) gives `discardWith 2 (uniformAttach 2) (conjChannel (tokOp U n ⊗ 1₂))` on
  `Fin 2 × Fin n`, which is `conjChannel (tokOp U n)` by the kernel's `discard_tensorOf_one`
  (MinimalRepertoire.lean:495, through `discardWith_uniform_conjChannel`, AncillaClosure.lean:461: the discard of
  `conj (V ⊗ 1)` over a uniformly attached ancilla is `conj V`).
- **The equivalence** `pairAvail_iff_tokenAvail` under (C) and (L). Both directions hold for every level `n` (level
  `0` included: nothing in either direction needs `0 < n`).
- **Module** `lean/BridgeToken.lean` §A, importing `BridgeAvailFull` (for §B of the same module, node B18) and the
  kernel. Preflight `experiments/b19_preflight.py` (exact, Gaussian rationals): the two reindex identities on random
  one-token matrices at `n = 1, 2, 3`; the discard identity on random `V` and `ρ`; the spectator identity
  `amplRef (Fin 2) (conjChannel V) = conjChannel (1 ⊗ V)` on random inputs; a countercontrol fixing the role of the
  uniform normalization (an ancilla attached as `1` instead of `1/2` gives `2 · conj V`).
- **No local Lean**; every kernel name read at L in this tree, every Mathlib name read in the pinned sources.

**Productivity test (§A.31), fixed now.** B19 is a gem iff it yields more than "the written argument of NOTES-B14 §2
now builds": a direction needing strictly fewer hypotheses than stated there, a failure of the written argument, or an
assumption of the bridge vocabulary the kernel's protocols do not share. Expected: ELABORATING, with one POSITIVE
sharpening already visible in the design (pair ⇒ token needs label invariance alone; context stability enters only in
token ⇒ pair).

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | `reindex assoc⁻¹ (1 ⊗ (U ⊗ 1ₙ)) = (1 ⊗ U) ⊗ 1ₙ` and `reindex toEnd ((1 ⊗ U) ⊗ 1ₙ) = (U ⊗ 1ₙ) ⊗ 1₂`, exactly, random Gaussian-rational `U`, `n = 1, 2, 3` | P1 |
| S0-2 | `ptrace₂ ((V ⊗ 1₂)(ρ ⊗ ½ 1₂)(V ⊗ 1₂)ᴴ) = V ρ Vᴴ` exactly on random `V`, `ρ` (the discard identity); with the ancilla attached as `1₂` the result is `2 V ρ Vᴴ` (countercontrol) | P2, P4 |
| S0-3 | `amplRef (Fin 2) (conjChannel V) M = (1 ⊗ V) M (1 ⊗ V)ᴴ` exactly on random inputs | P3 |
| S0-4 | `BridgeToken.lean` §A builds: `pairAvail_of_tokenAvail`, `tokenAvail_of_pairAvail`, `pairAvail_iff_tokenAvail`, every `#print axioms` line standard | dispatch, job log |
| S0-5 | pair ⇒ token uses (L) only; token ⇒ pair uses (C) and (L); neither uses `0 < n`, dagger stability or saturation | module statement |
| S0-6 | Gem: ELABORATING with the POSITIVE sharpening of S0-5 | §3 |

### S0 addendum (written 2026-10-11T08:07:01Z, after the owner's further distinctions, before any dispatch)

**Domains, theorem by theorem** (the owner's distinction (1)). `TokenAvailAt` and `PairAvailAt` are availabilities of
one-outcome conjugation channels (reversible operations) in the theory an architecture generates, i.e. in the
InstAvail closure, which includes the non-invertible protocols (readout, coarse-graining, ancilla attachment and
discard). token ⇒ pair (`pairAvail_of_tokenAvail`) stays inside the reversible operations: the spectator rule carries
the conjugation by `U ⊗ 1ₙ` to the conjugation by `1 ⊗ (U ⊗ 1ₙ)` (`amplRefL_conjChannel`) and the transport rule to
the conjugation by the reindexed operator (`transport_conjChannel`); both are closure rules of the InstAvail
predicate, and no ancilla is attached or discarded. pair ⇒ token (`tokenAvail_of_pairAvail`) leaves the reversible
group: the discard rule is a non-invertible protocol (uniform attachment of a two-level ancilla, then the partial
trace), and the kernel's `discardWith_uniform_conjChannel` (AncillaClosure.lean:461, through
`discard_tensorOf_one`, MinimalRepertoire.lean:495) is the lemma that says the result is again a conjugation — by the
operator itself, with the scalar `(1/2) · 2` cancelling. So the equivalence `pairAvail_iff_tokenAvail` lives in the
InstAvail closure with ancillas and discard; its token ⇒ pair half lives in the reversible operations alone; no
group-generation step occurs in either (no product of operations is formed). Every RESULTS row of B19 carries this
domain statement.
