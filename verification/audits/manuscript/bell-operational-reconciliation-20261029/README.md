# Bell and operational-completion integration

Base: `ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf`. The guiding draft is #1000.
The correction combines SC-33 #968, SC-39 #977, SC-42 #976 and SC-17 #963's
Bell clauses; their original branches and evidence remain unchanged. Source
checkpoint `efafee4fa677e424175faa10e6aeb5df61791f36` began the forward response
to [integration review 6497997935](https://github.com/amaybaum/incompleteness/pull/1000#issuecomment-6497997935).

**Current checkpoint: WIP / UNVERIFIED publication artifacts.** The source and
successor checks below are complete, but generated TeX/PDF artifacts are stale
until the canonical rebuild. Independent exact-final-head review and ordinary CI
remain separate. Earlier source acceptance and green CI at `4b49669a` apply only
to that earlier tree, not to this amended source.

## Review dispositions

| Finding | Source disposition |
|---|---|
| 1 — complete Methodology argument | Abstract, overview, Part III, §15, later comparison and conclusions state distinct substantive premises; no shared automatic escape is asserted. All further same-claim summary hits were propagated. |
| 2 — book summaries | Chapters 2, 4, 12 and 19, book index and FULL use separate premise checks. Chapter 19 distinguishes the observer-relative account from a resolution of every measurement protocol. |
| 3 — live SC-42 verification | `check_sc42_integration.py`, the annotated static site table and deterministic results are forward successors. Historical scripts/results remain unchanged. |
| 4 — substantive §15 rationale | The actual deterministic Bell ceiling and matrix-setting operational-completion theorem show why a common fixed-basis representation leaves distinct operational premises. No unsupported design chronology is claimed. |
| 5 — no-signaling scope | Adopted physical-branch summaries require no-signaling. Main distinguishes an explicitly realized no-signaling target law (PR) from the open H-Bell physical realization. Conditional H-Bell statements retain both no-signaling and continuum-curvature requirements. |
| 6 — entanglement hedge | Chapter 3 retains “in the framework's mechanism proposal”; the fixed Bell ceiling is kept separate. |
| 7 — edited-paper register | Process commentary is replaced by mathematical content; the edited Explainer emphasis is lowercase. |
| Direct FR/PBR summary follow-up | Main retains the same joint law and marginals. Methodology, Chapter 4, Appendix C and glossary require the actual operational protocol and certainty/consistency/single-outcome premises, rather than inferring an FR escape from multiple partitions or epistemic states. Appendix C's PBR, Colbeck-Renner and extended-Wigner-friend summaries retain their own premises. |

The FR scope correction was checked against the primary article's Introduction,
which distinguishes ordinary differences in observer knowledge from the protocol's
(Q), (C), (S) contradiction: Frauchiger and Renner, Nature Communications 9, 3711
(2018), [doi:10.1038/s41467-018-05739-8](https://doi.org/10.1038/s41467-018-05739-8).
This is a scope correction, not a new derivation or resolution of that theorem.

## Scientific invariants

The GR setting still matches every field of `FiniteOperationalTheory`, including
the assumed complex matrices and tensor composite, ancilla-level validity,
single-outcome preparation closure and branchwise spectator-independent Lüders
readout. Both characterization directions and the per-principle converse
hypotheses remain. The card boundary still covers every post-deal operation,
scheduling and readout, chance jointly independent of settings with the deal,
and an outcome every run with none discarded.

No Lean source or proof grade changes. `MAIN:T-statement` remains SUM with its
existing mapping and empty delta; its required-no-signaling wording changes the
fingerprint from `e70a32287a2f57e0` to `d523a2d67d4e4451`. The earlier
`70572f0b3e1aa833` fingerprint belongs to the pre-integration source. Main's exact
joint-law formula and the two observer marginals are unchanged. Regress/gauge
classification prose, #998 and #918 are outside this branch's writing scope.
SC-17's dynamics/chirality/Higgs clauses remain with the SM workstream.

## Successor checker and controls

The successor retains the historical field checks, unchanged theorem comparison,
stale-scope exclusions, directional witnesses, per-principle hypothesis checks,
source pins and mirror predicates. It adds explicit current paragraph anchors,
required-no-signaling and non-automatic FR guards, and checks all changed book
sources against FULL. The baseline-zero kinematics guard remains at pinned main.

`sc42-intended-sites.json` is a static intended table with **68** mentions and an
explicit role for every paragraph. Methodology has **3**: the original SC-42
three-status overview, the earlier integration's scoped §15 conclusion and the
new substantive Bell/completion comparison. The other per-file counts retain the
original table. Counts are never inferred as the expected values at test time.

The paper register/capitals/history scan follows AGENTS §§A.32–A.33 and applies
to `papers/`; security-pattern checks still cover added text. Scientific acronyms
such as CHSH are allowed. CLPW (Chandrasekaran–Longo–Penington–Witten, GR [39]) is likewise a cited scientific initialism; allowing it resolves six post-integration caps hits in GR and Main without disabling the `paper_caps` negative control. Retained historical code comments are not paper prose.
The historical checker remains unchanged at blob `fe433673a6c007b9436a0796d496c7f34c893362`;
its earlier failures remain in `validation.json` as a historical result, not a
current passing result.

The successor passes **498 predicates** at #997's head: 338 non-mirror predicates and 160 chapter/FULL mirror predicates (133 at #1000's landing, the rest for chapter lines #997 changes). Its bounded control suite contains one
unmodified positive source and **8 must-fail variants**: remove single-outcome
preparation closure, move validity to the system alone, derive rather than assume
kinematics, break the glossary/FULL mirror, add an unlisted kinematics occurrence,
insert paper caps emphasis, assert achieved rather than required no-signaling,
and restore a partition-only FR escape. Each negative control must exit 1 and
fail its named scientific or register predicate. Normal and optimized runs agree
byte for byte for both source and controls. Result files include the checker and
site-table hashes and deterministic predicate records.

From the repository root:

```sh
python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py
python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py --self-test
```

Outputs replay `sc42-integration-result.json` and `sc42-integration-controls.json`.
The existing ordinary core-B job fetches the single pinned baseline tree, compares
normal/optimized source and control outputs and replays both retained results.
Its event modes are unchanged; this adds no special launch or native attestation.

## Landing limits

Canonical rebuilds and selected rendered-page checks are required on the completed
candidate, followed by independent scientific/editorial review and fresh ordinary
CI on that exact head. No merge, release, correction-unit closure, branch rewrite,
workflow dispatch or F/E designation is authorized. Introduction #918 stays
read-only; its card sentence and operational setting still need final reconciliation
with the accepted sources. Native instrument construction and physical H-Bell
remain open.
