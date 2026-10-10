**MERGE-HELD — native §A.39 round KT4-PREM-1. Do not merge; landing only on explicit owner authorization.**

This round is a premise audit of the Pauli-free four-copy theorem `kt4_forward_ie1` (design module `FourCopyHeadline` at `ff9c3a35`, kernel-checked in a design run, not certified, not on `main`). It records which implications among its five hypotheses and its conclusion fail, what certified `main` supplies toward each hypothesis, and what each would still need. It adds no Lean module and proves no theorem in the kernel. It starts from `D` = `bcbc516f` (`main` after RELC-SELECT-1 landed, certified by push run 37755552123) and is non-sealing.

**Exploratory research and this preregistration.** The models, the probe, the independent check and the dependency assessment come from exploratory work on the disposable branch `claude/network-tool-access-8jtdhm`, done before this preregistration. The preregistration freezes the two scripts as blobs, the rule by which each cell is read, the words the result note must and must not use, and the controls; it does not present the exploratory results as predictions. The round replays that evidence at an exact head and records the current dependency assessment.

**The cells** (positive token / `…-NOT-ESTABLISHED`):
- **Q1-CL** (`CLOSEDNESS-FOIL-VERIFIED`): the closedness foil `M_cl` (`int Q3 ∪ (SEP + cnot SEP)` at every pair, `N = cnot`) satisfies `hcls`, `hadm`, `hgate` and the full four-copy condition `H`, and fails `hcl` and IE₁. So `hcl` cannot be dropped from the theorem.
- **Q1-MAX** (`MAXCONE-MODEL-VERIFIED`): the maximal cone satisfies `hcls`, `hadm`, `hcl`, `H` and the conclusion, and fails `hgate`. So `hgate` is not necessary relative to the rest. This does not establish that `hgate` can be removed: the D-gate model refutes the implication without it.
- **Q1-IND** (`INDEPENDENT-REPLICATION-VERIFIED`): an independent exact check, written by a separate agent from its own transcription of the Lean sources and sharing no code with the probe, reaches the same verdict on all fourteen clauses of `M_cl` and `M_max`, `H` of `M_cl` among them (124 exact checks). This is exact computational evidence, not a Lean kernel proof of either construction.
- **Q1-MAP** (`COUNTERMODEL-MATRIX-VERIFIED`): the remaining models — the D-gate model, a reflected-local model, the identity gate, the classical cone, the mixed ray, the interior model, and the token models — satisfy and fail the clauses their rows state.
- **Q1-NEC** (`CLASSIFICATION-STEPS-VERIFIED`): the finite steps of the written classification (`hcls ∧ hadm ∧ hgate ∧ IE₁ ⇒ K_p ∈ {Q3, twin}`, hence `hcl`) hold exactly. The step from the generated Lie algebra to the generated group is a standard result of Lie theory; the argument is not yet kernel-checked.
- **Q2** (`PAIR-ROUTE-GAP-VERIFIED`): `D` implies neither closedness nor gate preservation for a composite of two balls; the completion layer at `D` is typed for one system (an exact census of every `DirectedStages` mention at `D`).
- **Q3** (`SOURCE-MAP-CITATIONS-VERIFIED`): the 45 landed declarations the source map cites resolve at `D`.

**The earned reading** (frozen, stated only when all seven cells are positive) ends: *On the source map, none of the five hypotheses is yet derived from the observer-native foundations certified on main: each needs an additional premise. The round certifies this dependency assessment; it does not establish the full equivalence theorem.*

**The non-inference rule** (frozen, stated under every outcome) includes: the round derives none of the five hypotheses and does not establish the full equivalence theorem; a model in which `hgate` fails while the other hypotheses and the conclusion hold shows only that `hgate` is not necessary, not that it can be removed from the theorem; the probe and the independent check are exact computations, not Lean kernel proofs, and no countermodel is kernel-checked; the necessity of `hcl` rests on a written argument that is not yet kernel-checked.

**Governed paths:**
- the record directory `verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/`;
- the receipt `verification/receipts/KT4-PREM-1.json`;
- `verification/lean/kt4_prem1_probe.py` and `verification/lean/kt4_prem1_indep_check.py` (A);
- `.github/workflows/verify.yml` (M): one shard, `Numerical probes / KT4-PREM-1 premise audit`, running both scripts, and its result in the aggregate probe job.

No manuscript, no built artifact, no Lean module, `verification/ROADMAP.md` and no certified result changes under any outcome.

**Design evidence:**
- Design run 1, 37958712227 on `e941e708` (disposable branch): the probe shard printed `kt4_prem1_probe: OK -- 79 checks` and the probe aggregate succeeded; the Mathlib bridge failed only at the two gate steps the audited theorem's design modules fail, which this round does not carry.
- The independent check's exploratory runs were local: its first run failed one of its own countercontrols, which it replaced; the frozen version printed `FINAL: 124 exact checks, 0 failed; claims AGREE`, and a replay matched apart from timing.
- **Predicted execution tree** `abb91516` (`claude/kt4-prem-1-predicted`, a single-parent child of `D`, tree `df5d6199`), run 37972004827 (`workflow_dispatch`, attempt 1): all 33 jobs succeeded. The KT4-PREM-1 shard printed 79 `PASS` lines and `kt4_prem1_probe: OK -- 79 checks`, then 124 `ok` lines, the fourteen frozen verdict rows and `FINAL: 124 exact checks, 0 failed; claims AGREE`; the release gate passed all 21 steps (`lean-axioms` 5860, no `sorryAx`; `lean-manuscript` OK; 303 legacy records; 42 receipts hold); the probe aggregate reported `kt4prem1=success`.

**Candidate `F`:** `7ae032174699190086f1e54b7adb7aeb1a80a726`, which is `D` plus the preregistration alone (blob `708feac05e7f0176472e9f381367df9d71bf872a`). The exact-head attestation follows in a comment. `F` is not designated; no C1, S1 or S2 exists.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1

---
_Generated by [Claude Code](https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1)_
