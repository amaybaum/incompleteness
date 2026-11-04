# PR-AUDIT-1 — LA-EQUAL and MR-1 N5: read-only proof review

**Date:** 2026-11-04.
**Reviewer:** ChatGPT (GPT-6), conducting a separate read-only textual review of the work
originally reported in #1009; this is a model-authored review, not an authenticated
human or independently signed reviewer record.
**Scope:** mathematical validity, sourcing of five hypotheses, and support for
the *exact* frozen MR-1 N5 statement. No script, numerical experiment, Lean build,
native-round execution, or modification of frozen records was performed.

**Disposition: GAP for independently establishing the full LA-EQUAL claim.**
The conditional tail-independence step has a coherent triangular argument, but
the reviewed sources do not establish one additional equality needed to conclude
equality of the **complete** joint history under both setting values. This finding
is a missing-proof finding, **not a counterexample** and not a finding that the
reported LA-EQUAL token is false.

## Sources read (paths relative to repository root)

- `verification/programmes/substratum/continuous-substates/later-access-preregistration.md`,
  especially lines 61–75, 117–168, 170–207 and 348–379.
- `verification/programmes/substratum/continuous-substates/later-access-result.md`,
  especially lines 10–33 and 83–99.
- `verification/programmes/substratum/continuous-substates/native_later_access_probe.py`,
  especially lines 1136–1153 and 1182–1204 (decision rule).
- `verification/programmes/substratum/continuous-substates/native-random-setting-test.md`,
  especially lines 67–116 and 118–150.
- `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/history_v11/REPORT.md`,
  especially lines 91–129 (chronological inversion under supplied independent bank).
- Frozen `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md`,
  especially N5 at lines 109–111. The frozen file has not been changed.

## A. Proof validity — PARTIALLY VERIFIED; full claim has a GAP

Let `c=R.A`, `Y` denote all pre-tail coordinates of the comparison window,
including the complete pre-cut public history with `R.A` removed, the incoming
packet, the two subsequent packet slices, and the two recorded increments.
Let `T=Tail`. The comparison keeps unnormalized masses for each `K0=k0`
(including `k0=⊥`).

Under H-prior and the exclusion/order/permutation properties P1–P6b,
the first-arrival triangular mechanism implies that for each fixed original
complement and the earlier 42 keys, the complete tail-output word is a
bijective image of fresh uniform tail-bank triples. Its conditional law is
therefore uniform and does not depend on earlier key, setting or packet
labels. This step has a recognizable argument using the explicit
`v ↦ α XOR H(v XOR β)` permutation and chronological ordering
(`history_v11/REPORT.md:91–108`; `later-access-preregistration.md:178–198`).
It supports the conditional `EMPTY` reading, given the supplied joint prior
and the declared access. The local P6b control is not itself a universal-scale
proof, and no Lean certification is claimed.

**Missing bridge:** the complete-history result `μ_0^k0=μ_1^k0` needs
equality of the *pre-tail* law as well. Tail freshness alone gives, for
each compatible `y,t,c`,

    Pr(Y=y, T=t | R.A=c) = Pr(Y=y | R.A=c) / 8^m

where `m=8(H*−L−5)`. Equality across `c` thus additionally requires

    Pr(Y=y | R.A=0) = Pr(Y=y | R.A=1)

with the same incoming-packet and terminal-branch mass conventions.
This equality is not an automatic consequence of tail-bank freshness.

The earlier port-5 note establishes a setting-independent **future
record/carrier kernel conditional on the full public history**
(`native-random-setting-test.md:109–114`); it does not by itself
establish equality of the full **pre-cut public-history distribution**
after omitting `R.A`. That note explicitly retains and conditions on
`Wτ`, which contains `R` (`:118–127`). The LA probe's
`CP-PRECUT` checks a *small fixture* plus geometric exclusions
(`native_later_access_probe.py:1136–1153`); it does not calculate or
prove this joint equality for the astronomical original preparation.

A complete proof may be possible from the full chronological bank
construction plus the 42-key factorization, but the missing composition
and conditioning step must be supplied and checked. The existing
`LA-EQUAL` token is generated from passing P1–P6b and controls, with
full-TV zero inserted as proof-derived, not enumerated
(`native_later_access_probe.py:1182–1193`).
Therefore its green controls cannot close this paper-proof gap.

## B. Assumption sourcing — PARTIAL; not derived from OI alone

| Hypothesis | Standing in the reviewed sources |
| --- | --- |
| H-prior | Explicit **joint** conditional product/uniform law of the original 42 keys and tail bank. Stipulated; separate marginal source laws do not imply it (`later-access-preregistration.md:147–157`). |
| H-inventory | Completeness of original sources/readiness/bank inventory is declared, not a proof that no further physical interaction or source exists (`:159–163`, `:79–98`). |
| H-access | Retained candidate eight-port passive/read-stop convention, with non-writing read stipulated, **not adopted as a physical OI access law** (`:61–75`). |
| H-rule | The chosen native reversible rule `H(A,B,D)=(B,D,A XOR BD)`, checked for the pinned interface; it is a declared dynamics input (`:164`). |
| H-torus | No-wrap and coordinate-span inequalities checked for this finite window; this is conditional geometry, not a sourced experimental horizon (`:165–168`, P5). |

The theorem cannot be read as deriving preparation, access, inventory
completeness or native measurement control from OI alone.

## C. Frozen MR-1 N5 — PARTIALLY SUPPORTED, NOT ESTABLISHED

N5 accurately **reports** #1009's scoped output:
`LA-EQUAL`, `EMPTY`, the passive read of eight public ports through
`H*=2L`, under all five named hypotheses
(`measurement-record-formation/preregistration.md:109–111`).
Its limitations on active coupling and outgoing environment are proper.

However the full joint-law equality underlying the token has the
unclosed proof bridge in section A, and the hypotheses are not all sourced
as available physical OI operations. N5 is therefore **not verified as an
established scientific result** by this review. It remains a accurately
scoped historical research result with an explicit proof gap. No frozen
MR-1 text, negative-result classification, or manuscript conclusion is
changed.

**Disposition and ownership:** This finishes the *read-only review task*
within administrative #1088. The underlying scientific proof gap belongs
to the pre-existing SUBSTATE-1 scientific owner #1007, and the impact on
MR-1 N5 belongs to #866. They remain scientifically open; closing #1088
must not imply that the gap was proven away. Do not adopt the premise,
or certify complete operational QM, on this record.
