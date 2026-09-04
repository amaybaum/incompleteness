# Audit A — C1/C4, hidden memory, and the minimality machinery

`verification/lean/partition_coupling_probe.py` — checks P1–P5, exact rational arithmetic.

The audit cycle opened after the passive/minimal quotient work and left unfinished. Its question is
narrow: does any live manuscript use of C1 coupling, C4 readback, hidden predictive memory, raw
versus minimal carrier, the observability quotient, or passive minimality say more than the frozen
formal results support? The census is recorded here in full, including the axes that came back
clean, because an audit that reports only its hits cannot be checked.

## The frozen baseline the census is read against

| Result | What it bounds |
|---|---|
| `[Main]` §2.3, Chapter 1 §1.7 | the recurrence route uses **finiteness and C1**, and nothing else |
| `[Main]` §3.4, *which condition is primitive* | C4 is the independent one; C1 and C3 follow from it in any faithful realization |
| `[Main]` §3.4, canonical predictive quotient | the **tail** object `T(P)` is terminal among faithful realizations of a finite-horizon law |
| `PassiveQuotient.lean` | `S/∼_∞` is the minimal carrier; `itiRelInf_greatest_congruence`; `quotient_itinerarySeparating`; `passiveMinimal_iff_itinerarySeparating`; `minimal_realization_bijective` (Nerode uniqueness among **separating** realizations) |
| `ObservabilityQuotient.lean` | `branchDomain_span_eq_itineraryInvariant`; `classicalBranchDomain_iff_horizon`; `domainGlue_classification_mod_itineraryFibres` |
| `Structure.md` Corollary 9.8 | the embedded-observer triple does **not** determine a unique substratum realization |

Two of these bound different objects and must not be traded for one another: the **predictive**
quotient is built from the law and is terminal among realizations of it; the **passive** quotient is
built from the dynamics and the cut, and is minimal among carriers. Neither implies the other.

## Finding A1 — the recurrence chain dropped C1

`book/ch18-beyond.md` §18.7 and its parallel source `book/The-Incompleteness-of-Observation-FULL.md`
stated the framework's logical chain as

> Finiteness of `S` guarantees recurrence (Poincaré). Recurrence guarantees that **any partition** of
> `S` into visible and hidden sectors will exhibit returns of information from hidden to visible over
> the recurrence timescale (P-indivisibility).

C1 is absent, and it is load-bearing. Everywhere else the corpus is exact — `[Main]` §2.3 and Chapter
1 §1.7 both read "the proof uses only Lemma 1 (finiteness, hence Step 1's recurrence) **and condition
C1** (non-trivial coupling, hence Step 2's overlap)" — so this is a local defect in an
exposition summary, not a disagreement between manuscripts.

**The countermodel**, certified in the probe. Take `S = V × H` with `V = ℤ/3`, `H = ℤ/4` and
`φ(v,h) = (v+1, h+1)`: a bijection on 12 states, with `φ¹² = id`, so recurrence holds and the
partition is available. Every two-time visible matrix is the cyclic **permutation** — the same matrix
for a uniform hidden prior and for a point prior, so the visible sector evolves autonomously and C1
fails at every order. The family factors as `T(t) = T(t−s)T(s)` through stochastic matrices at every
intermediate time, so it is divisible; and the total variation between two visible point
distributions is `1` at every `t = 0..12`. Nothing contracts, so nothing is restored, recurrence
notwithstanding. "Any partition" is therefore false as stated.

**The control** is the corpus's own coin-and-die example: `S = {0,1} × {1..6}`,
`φ(v,h) = (v ⊕ [h ≤ 2], h)`, an involution, where C1 holds. There the one-step visible matrix is
`[[2/3,1/3],[1/3,2/3]]`, not a permutation; total variation contracts `1 → 1/3` at `t = 1` and is
restored in full at `t = 2`. The measurement used against the countermodel is not blind: same
recurrence, opposite verdict, and the difference is exactly C1.

**The repair**, in both parallel sources: recurrence *together with C1* gives the returns, with the
uncoupled product system named as the reason the coupling cannot be dropped.

## The axes that came back clean

**C-condition dependency.** `[Main]` §3.4 records C4 as the only logically independent condition,
with C1 following (a readback gap requires hidden mediation) and C3 by data processing, both
certified in `primitive_probes.py`. Chapter 1 carries the same dependency at §1.7, §1.9 and §1.11
("C4 primitive, C1 and C3 its checkable consequences, C2 the physical regime"). No location asserts
the reverse entailment, and none claims C4 follows from C1.

**Raw versus minimal carrier.** No manuscript assumes the substratum is passively minimal or that
its cut is itinerary-separating. The vocabulary reaches the manuscripts in exactly one place,
`Structure.md` Corollary 9.8, which states the negative: the embedded-observer triple does not
determine a unique substratum realization, with the three pieces of gauge freedom named. The
minimality that appears in `Structure.md` §9 is Kraus-family linear independence, correctly labelled.

**Substratum determination.** No location claims the observer's data recovers the substratum up to
isomorphism. `Substratum.md` §§ on the reconstruction theorem claim uniqueness of the *local
reconstructed residue up to gauge* and explicitly do not claim the Bell-inclusive substratum unique.

**Automatic consequence.** No location says hidden memory or the observer distinction follows
automatically from coupling. The "follows automatically" occurrences in the corpus are in `GR.md`
(H-energy from H-spectrum, correctly derived) and in `Methodology.md` (an explicit warning *against*
the automatic reading of the trace-out).

**Partition universality.** `[Main]` §5's structural observer-selection theorem quantifies over "any
partition `V` of bounded coupling-graph diameter" and is conditional on (EM); it is properly
qualified and is a different statement from the recurrence chain.

## A status fact, recorded rather than repaired

No entry in `coverage/LEDGER.json` attaches to `PassiveQuotient.lean` or
`ObservabilityQuotient.lean`. The minimal-carrier machinery — the greatest congruence, the
separating quotient, minimality-is-separation, Nerode uniqueness — is kernel-proved infrastructure
that currently underwrites no canonical manuscript statement. That is not a defect: it is the
reason the raw-versus-minimal axis came back clean, since no exposition leans on it. It does mean
that if a future round wants to *use* passive minimality in the physical story, the ledger entry and
the manuscript statement have to be written first, not assumed.

## What this audit does not claim

That C1 is sufficient for P-indivisibility, or for anything else. That the recurrence route is the
only route to the framework's memory content — the C4 readback route to accessible non-Markovianity
is separate and does not pass through recurrence. That the census exhausts the corpus: it covers the
six vocabularies named in the audit's charter across `papers/*.md` and the book sources, and a
different charter would find different things. That any conclusion of `[Main]`, `[GR]` or the
equivalence theorem is affected — the defect was in one exposition summary, and its repair restores
the form the technical papers already carried.
