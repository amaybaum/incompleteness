# #941 audit, round 2026-11-04: Introduction re-baseline against `main` `f5c281ae`

**Status: WIP / UNVERIFIED.** Nothing in this round is independently reviewed. Every finding,
classification and correction below is the designated writer's (`writer-941`) and stays
provisional until the independent review that the coordinator commissions separately. This round
confers no scientific status (`AGENTS.md` §A.45 rule 1, §A.46) and authorizes nothing.

## 1. Objects and baselines

| Object | Exact id |
|---|---|
| Introduction under audit (start) | #918 head `4028e45db1ba520dc6a1bfb44a26b76a112ba575` |
| Corpus baseline | `main` `f5c281ae10a913ec68fa41b3b839ad0b164979cd` |
| Correction commits (this round) | `340961ceb9aa1d9d3b1230cc6a905898644051d8`, `690790584a53813439e6d9b5db3a6e7e5f5ea075`; after the independent review (#918 c.6643385201) of `b935150b`: `a17216815d29f0358f3316a110a4c4784ab37f1c`; after the owner decisions ([#941 c.6643474520](https://github.com/amaybaum/incompleteness/issues/941#issuecomment-6643474520)): `25a9d9fdc0bfd0ee2aff9d3da3f8d425452a1efe` |
| Prior audit record (provenance only) | #942 branch `audit/intro-corpus-20261026` at `16fc745dd0d787d100ca09553bd0342873f26771` |
| Handoff and retention records (provenance only) | #941 comments 6628558706, 6631126662; activation 6642597102 |

Authorization: #941 activation record (owner, 2026-11-04,
https://github.com/amaybaum/incompleteness/issues/941#issuecomment-6642597102), a paper-only audit
workstream on #918's branch. The owner's authorization of arXiv reads and PDF builds was relayed to
this writer by the coordinator during the session, before the corrections were committed; its
written records, #941 c.6643207092
(https://github.com/amaybaum/incompleteness/issues/941#issuecomment-6643207092) and #866
c.6643204362 (https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6643204362), were
posted after commits `340961ce`, `69079058` and `b935150b`. Not authorized and not done: merge or
publication of #918, workflow dispatch or re-run, scientific computations, new physical premises,
edits outside `papers/Introduction.*` and this directory, changes to frozen records.

## 2. Scope and method

1. A claim-to-source map of every substantive claim of `papers/Introduction.md`
   (`CLAIM-MAP.md`, 111 rows). Each claim is traced across the core corpus at `f5c281ae` (Main,
   GR, Substratum, the Book, the OIBridge Lean sources and the census registry, the BH programme
   records) before any negative classification (§A.19), and classified as exactly one of proved
   (with support layer), conditional (with hypotheses), posit, open or refuted.
2. Reconciliation with the #942 handoff (rows R-01–R-40, OD-1–OD-15, FA slice 2 D1–D6, Track C
   I-1–I-12, optional O-items) against `f5c281ae`, which moved after the handoff's corpus pin
   `27dc3443` (notably #1085, #1046, #1051, #1056 and the census changes).
3. Only clear-cut, minimum-diff corrections to the Introduction (§A.25), each mapped to a finding.
   Items whose resolution needs an owner choice, a census or Main change, an axiom report or a
   review are listed with options and not applied.
4. Lean identifiers were checked by reading the sources at `17b830bc` and `f5c281ae`; no Lean build
   ran. Commit reachability was read from the GitHub compare API (the local clone is shallow).

## 3. Findings: open items first

Class: **corrected** (applied this round), **owner** (needs an owner decision; options in §5),
**routed** (belongs to another Issue; §6), **blocked** (needs an action outside this
authorization).

### 3.1 Open: need an owner decision, another Issue or a blocked action

| ID | Severity | Locator (Introduction at `69079058`) | Finding and evidence | Class |
|---|---|---|---|---|
| F-14 | high | L116, L126–132, L158, L174, L322; App. A L357–360 | NEW-1 / OD-4. Four families the Introduction states as machine-checked (`RecordFibreIdentification`, `RootedRecurrenceBridge`, `TrajectoryMemory`, `FullFutureMemory`) are `kernel-only` in `verification/lean-manuscript-census.json` at `f5c281ae`, with `manuscript: []`; the TrajectoryMemory note reads "No publication-facing promotion or K3 change is made before successful CI and independent proof review". `papers/Introduction.md` is not among the census's 13 manuscripts. The modules are imported by `verification/lean-mathlib/OIBridge.lean` (L21–24), so `main`'s build includes them, and their blobs are unchanged from the checkpoints. The gap is the census contract and proof review, not verification or a known error. Partly resolved since the handoff: `RecurrenceHorizon`, `PhysicalC4Discharge`, `PhysicalC4StorageReadback` and `RootedClassification*` are now `current` with Main anchors. | decided ([#941 c.6643474520](https://github.com/amaybaum/incompleteness/issues/941#issuecomment-6643474520)): not promoted; applied E22 |
| F-18 | high | Abstract L17; L238; L320; L328 | OD-2 / R-06. The Introduction states as open which of (iii)–(v) a physical substratum supplies. Kernel statements at `f5c281ae` (families current): `permClass_onesFixing` (PhaseSource:79: the permutation class fixes the all-ones ray) and `onesFixing_not_phasesAvailable` (PhaseSource:52: a ones-fixing class generates no theory with the phases available, on carriers with at least two states); `substratumClass_not_onesFixing` (PhaseSource:196: once the quarter phase is stipulated, the class is not ones-fixing); `readWriteSourced_not_qm` (ReadWriteControl:174: a read-write-sourced `FiniteOperationalTheory (Fin 2)` is not exact finite endomorphic QM); `substratumClass_structurallyClosed` (StructuralClosure:316: the stated substratum class is closed under the architecture operations, stable under a spectator, relabelling-invariant and adjoint-closed, which bears on (iii) and (v)). That condition (iv) fails for finite bijective read-write dynamics with the stated access follows from these by a one-line inference (no kernel statement names (iv)), and GR:260 states it in prose. What remains open is a substratum with a further intervention principle. Underclaim. The owner disposition (2026-10-27) adopted reporting these results with Appendix A declarations; that needs their axiom reports in `papers/introduction_repro/` (OD-15), which needs an authorized CI run. | decided: scoped deduction stated, E21; Appendix A entries still blocked (OD-15) |
| F-19 | high | §3.4, L252–258 | OD-3 / R-07 / R-40. The ε-realization half of Main §3.4 (Main:566–602) is not reported; the owner disposition adopted adding it; R-40 and #945 require that any text rest on the exact regime only (#945's finite-b repair unproved). Needs a drafted text and its review; not a minimum-diff correction. | owner (drafting) |
| F-15 | high | [CE] L387 (used L314), [CR] L389 (used L316) | NEW-3 / item 26. `bdcbd32bb55a5464d72b61682721f0b4bfaf446c` and `2624d49cffc0794b300517719c879de6b57d395e` diverge from `main` and from #918's head (compare API). The proof and control blobs they contain are byte-identical in #918's tree: `entropy-profile-proof.md` `16bdf99a…`, `exact-results.json` `908608ae…`, `exact_controls.py` `dc6c3483…`, `sequential-release.md` `3f7669ec…`, `sequential-release-results.json` `f9b77129…`, `sequential_release_controls.py` `f005d996…` (READMEs differ). Owner obligation (c.6631126662): durable retention on `main` before any dependent claim lands. | owner |
| F-16 | high (blocking for landing) | L316, L322 | [CR] (`sequential-release.md`) has no independent review: the in-tree `independent-core/review.md` reviews [CE] at `bdcbd32` only, and the obligation is homed on #970 (c.6631126662). The Introduction lists [CR] under "Established mathematical results … Proved on paper also" (§A.46 items 1 and 3). | decided: moved out of the established list, E19; review stays on #970 |
| F-17 | high (blocking for landing) | L371, L379 | Corpus pin and citations disagree. L371 pins Main, SM and the black-hole computations at `20ca05fe`; the Introduction's Main citations are correct against `f5c281ae` and not all at `20ca05fe`. Absent at `20ca05fe` and used before this round: "Theorem (overlap and return)" and `pIndivisible_of_rooted_identity_return_of_overlap` (Theorem 3), `routed_forces_indivisible_somewhere`, the rooted classification (`finiteRootedRealizable_iff_pper`). Made consistent with `f5c281ae` and not with `20ca05fe` by this round: E3 (Main §2.4's title reads "A Minimal Model" at `20ca05fe`), E5 (Main at `20ca05fe` carries the older gluing wording), E8 (Main §3.3 at `20ca05fe` still carries H-Bell's continuum clause). Separately, the pins `021850d9` and `a2be1e45` diverge from `main` and #918's head; the content used (GR:839–853; `book/ch03-structural-realism.md`:218) is on `main`. Re-pinning was assigned to R0-B (#918 c.6603786828: "pins and labels"); the owner then authorized it for this round (#941 c.6643474520), and it is applied by E18 after the verification of §14.1. | decided: re-pinned to `f5c281ae` after verification, E18 (§14) |
| F-20 | low | L174; App. A L356 | OD-5 / R-13. Main:147 gives two formalizations of the routed-readback realization clause, neither implying the other. The Introduction's gloss at L174 is the reading-neutral clause of Main:147, and App. A cites one formalization, the seed-conditioned `routed_forces_indivisible_somewhere`; the storage-time `routedAtStorage_forces_indivisible_somewhere` (`PhysicalC4StorageReadback`) is not listed. A completeness finding, not a mismatch. Adding the declaration needs its axiom report (OD-15). | blocked (OD-15) |
| F-21 | low | L304; [Sha79] L475 | OD-8 / R-19. [Sha79] (Commun. ACM; not on arXiv) is not read first-hand. CT06 locators (L118–138) also unchecked. | owner |
| F-23 | low | L41, L304–306, L322; refs L383–385 | CON-03 / O-17. The BH-01 record's own status line reads "exploratory research, unreviewed for adoption" (`bh01_access_v1/REPORT.md`:3) while its review directory exists; the Introduction lists the enumeration and the $1/\vert\mathcal U\vert$ floor among established results. The enumeration reproduces from `main` (`checks.py`, `result.json`). | owner (O-17) / #1029 (record status) |
| F-24 | low | L41 | NEW-5. The Contributions sentence names [BHa; BHb] as the records of §5's results; the §5 coherent-entropy results are in [CE; CR]. Depends on F-15, F-16. | applied with E20 |
| F-25 | low | refs L441 [HLW06], L469 [PSW06] | Two reference entries are cited nowhere in the text. No scientific misstatement; not edited (owner guidance: scientific corrections first). | owner (editorial) |
| F-26 | — | whole paper | OD-13. The PDF is 25 pages; the main text runs to p. 22 (Code, data and Appendix A begin on p. 22). The audit plan's 12-page budget is exceeded; the owner disposition keeps required qualifications regardless of length. | owner |
| F-27 | — | — | Optional items O-1, O-2, O-3, O-4, O-10, O-13, O-14, O-17, O-23, O-26 (handoff §6) are neither adopted nor waived. | owner |

### 3.2 Corrected this round (not reviewed)

| ID | Severity | Locator | Finding | Edit |
|---|---|---|---|---|
| F-01 | medium | L43, L124 | R-03 / OD-7: "exact probe" defined as exhaustive; the Pinsker probe computes information quantities in floating point (Main:176); the dilation probes are exact on instances, not exhaustive (Main:520, :522). Owner disposition (2026-10-27): correct the definition rather than overstate numerical verification. | E1, E2 |
| F-02 | low | L178 | R-04 / OD-10: "A minimal model" reads as a size claim; no corpus document at `f5c281ae` states minimality (Main §2.4 title; at the pin `20ca05fe` the title read "A Minimal Model", F-17), and a three-hidden-state model reproduces every displayed number (hand derivation: $\varphi$ swaps $(0,1)\leftrightarrow(1,1)$ and fixes the rest; uniform $h$ gives $\Gamma_1$ as displayed, $\Gamma_2=I$ since $\varphi$ is an involution, and $P(x_2{=}0\mid x_1{=}1)=(1/6)/(1/2)=1/3$ for uniform $x_0$). Owner disposition: no minimality claim. | E3 |
| F-03 | medium | L324 | R-05 remainder: fixed-basis statistics stated as the visible laws of an embedded observer without the per-horizon scope; Theorem 1 is per horizon and a nonperiodic law has no exact all-time realization by one fixed substratum (Main:640). | E4 |
| F-04 | medium | L331 | R-09: open problem 4 listed exact gluing for recurrent target families as open; Main:640 now states the rooted classification (`finiteRootedRealizable_iff_pper`, family current) and narrows the open question to multi-time laws. Outdated relative to `f5c281ae` (not relative to the pin `20ca05fe`; F-17). | E5 |
| F-05 | low | L332 | R-27: open problem 5 listed only §§2.2–2.5; §3's Bell ceiling, factorization half and Hadamard example are also paper-only or instance-checked. | E6 |
| F-06 | low | L242 | R-28: the §3.3 heading read as "nothing selects the relating evolution"; Main:646 says representability (with ordinary coherence) does not select it. | E7 |
| F-07 | medium | L268 | New. H-Bell's continuum-limit clause was cited to [Main §3.3]; at `f5c281ae` Main §3.3 states only the response-dependence and no-signalling part (Main:416, :429; changed by #1085/#1046); the continuum clause is Substratum:133 (§3.2). Outdated relative to `f5c281ae` (not relative to the pin `20ca05fe`; F-17). | E8 |
| F-08 | medium | L216 | NEW-2 / SC-41: [Main §4.5] closed the Pauli-twirl sentence; Main §4.5 (Main:720) supports only the fixed-card half. The twirl identity is now stated in-line. | E9 |
| F-09 | low | L83, ref. | #941 orphan 36, owner decision 11: [Sch21] was used as support without a first-hand read. Bar26 (arXiv:2608.04354v1, fn. 1, read first-hand) reports that Schmidt's construction "appears to have an error". Main no longer cites Sch21. | E10 |
| F-10 | low | L172 | R-15: "Doukas states the same argument" overstated: Dou26 Prop. 1 is a no-revival obstruction by ℓ1 contraction under Chapman–Kolmogorov composition, with no overlap or return. | E11 |
| F-11 | low | L148 | R-16: RHP14 Thm 2.4 is an equivalence of which the text uses one direction; BD16's classical case is Cor. 1. | E12 |
| F-12 | low | L256 | R-17: Mon08 gives no explicit task; it proves a lower bound of 2N−2 continuous ontic variables for Markovian (deterministic or stochastic) ontological theories, and reports Hardy's result. The explicit tasks are GH03 and HKLP24 Thm 4. | E13 |
| F-13 | low | L300, ref. | R-14 / OD-8: [Pag93] ("Average entropy of a subsystem") does not state the black-hole information problem (no occurrence of "black hole" outside its references). Page's "Information in black hole radiation" does. | E14 |
| F-28 | medium | L41 | Review item 3 (C-020): "The results of §§3.2–3.5 are proved in [GR] and [Main]" overstated §3.4, whose unbounded classical dimension is imported from [HKLP24] (Main:560 imports it as [55]); Main proves the factorization half. | E15; provenance made explicit by E20 (owner decision) |

No claim of the Introduction was found refuted on `main`.

## 4. Corrections applied

All edits are to `papers/Introduction.md`; `.tex` and `.pdf` were regenerated from the same
commit's source in the same commit (§9).

| Edit | Finding | Commit | Before → after |
|---|---|---|---|
| E1 | F-01 | `340961ce` | "an exhaustive computation in exact rational arithmetic at small size" → "a computation in exact rational arithmetic on stated small instances" |
| E2 | F-01 | `340961ce` | Pinsker bound "(proved on paper, with exact probes)" → "(proved on paper)" |
| E3 | F-02 | `340961ce` | "**A minimal model.**" → "**A six-hidden-state model.**" |
| E4 | F-03 | `340961ce` | "are the visible laws of an embedded observer" → "are, at every finite horizon, visible laws of an embedded observer" |
| E5 | F-04 | `340961ce` | "for recurrent target families" → "for recurrent families of multi-time laws" |
| E6 | F-05 | `340961ce` | "steps of §§2.2–2.5 proved on paper" → "steps of §§2–3 proved on paper" |
| E7 | F-06 | `340961ce` | "### 3.3 The evolution relating two times is not selected" → "### 3.3 Representability does not select the evolution relating two times" |
| E8 | F-07 | `340961ce` | "H-Bell [Main §3.3]" → "H-Bell [Main §3.3; Substratum §3.2]" |
| E9 | F-08 | `340961ce` | twirl sentence: adds "which sums to it because $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)\,I$" and scopes [Main §4.5] to "with a fixed initial hidden card the swap admits no such decomposition" |
| E10 | F-09 | `340961ce` | "[Bar26, Thm 3.3; Sch21, Thm 2]" → "[Bar26, Thm 3.3]"; uncited [Sch21] entry removed |
| E11 | F-10 | `69079058` | "Doukas states the same argument concurrently" → "Doukas states the contraction argument concurrently, as a no-revival obstruction to Markovian realizers" |
| E12 | F-11 | `69079058` | "the divisibility criterion of [RHP14, Thm 2.4] … [BD16, Prop. 1]" → "the "only if" half of the divisibility criterion of [RHP14, Thm 2.4] … [BD16, Prop. 1 and Cor. 1]" |
| E13 | F-12 | `69079058` | "and Montina [Mon08], and" → "and Heinosaari et al. [HKLP24, Thm 4], and" |
| E14 | F-13 | `69079058` | [Pag93] entry → Page, "Information in black hole radiation," PRL 71, 3743 (1993); arXiv:hep-th/9306083v2 |
| E15 | F-28 | `a1721681` | Contributions: adds "and the unbounded classical dimension of §3.4 an imported result [HKLP24]" |
| E16 | review item 8 | `a1721681` | "the one-step $\vert\mathcal C_V\vert^2$-dimensional ancilla dilation of [Main §3.1]" → "the one-step ancilla dilation of [Main §3.1], of total dimension $\vert\mathcal C_V\vert^2$," |
| E17 | review item 8 | `a1721681` | "Page's Haar mean" (L314) cited to [Pag93a] = arXiv:gr-qc/9305007v2 (restored entry); the E14 entry relabelled [Pag93b] at L300 and in the references |
| E18 | F-17 | `25a9d9fd` | L371 corpus snapshot → `f5c281ae10a913ec68fa41b3b839ad0b164979cd` for Main, SM, GR, Substratum, the Book and the BH computations (`20ca05fe`, `021850d9`, `a2be1e45` not named); L379's separate Substratum pin removed (covered by L371); L342 probe/BH snapshot `55e3217b` → `f5c281ae` |
| E19 | F-16 | `25a9d9fd` | L316: "[CR], proved on paper and not independently reviewed,"; L322: [CR] removed from "Proved on paper also" |
| E20 | F-28, F-24 | `25a9d9fd` | L41: "…, with one imported component: in §3.4 the factorization through finitely many ontic states is proved in [Main], and the unbounded classical dimension of qubit prepare-and-measure behaviour is the result of [HKLP24, Thm 4]. Those of §5 are in unpublished research records … [BHa; BHb; CE; CR]" |
| E21 | F-18 | `25a9d9fd` | abstract L17, L238, L320, L322, L328: failure of (iv) for the theory generated by the operations of finite bijective dynamics under the stated observer access, on at least two states, stated as a one-step deduction from two statements checked in Lean in [GR §3.3]; "open" kept for substrata with further intervention principles |
| E22 | F-14 | `25a9d9fd` | L340: the four modules "are built and checked with the library on `main`, their proofs have not been independently reviewed"; L322: one sentence saying the same of the trajectory, entire-future, record-fibre and actual-return statements |

Propagation (§A.25) was confined to the Introduction and its `.tex`/`.pdf`, as authorized. The
`verification/coverage/LEDGER.json` rows `INTRODUCTION:*` cite lines 67, 103, 120, 154, 160 and
234, none of which moved or changed; `tools/coverage_check.py`, `voice_check.py`,
`claims_check.py`, `duplicate_check.py`, `staleness_check.py` and `lean_manuscript_census.py`
passed after the first commit; staleness, voice, claims and duplicate checks after the second, and the coverage, census and artifact-placement checks on the tree that adds this record.

## 5. Owner decisions

The owner decided F-14, F-16, F-17, F-18 and F-28 on 2026-11-04 ([#941 c.6643474520](https://github.com/amaybaum/incompleteness/issues/941#issuecomment-6643474520)); their application is in §14. The options listed below for those findings are kept as the record of what was decided between. The other items still need a decision.

- **F-14 (OD-4).** (a) Promote the four families in the census (status `current`, anchors, and
  `papers/Introduction.md` added to the census manuscripts) after the CI evidence and independent
  proof review their notes require; the census and any Main anchors are outside this
  authorization. (b) Narrow the Introduction to the anchored route: Theorem 3 and the
  stochastic-inverse lemma machine-checked, the record-fibre, trajectory, whole-future and
  actual-return statements proved on paper with the modules named as unpromoted formalizations.
  (c) Remove those statements.
- **F-18 (OD-2) and F-20 (OD-5).** Authorize the axiom-report regeneration of `papers/introduction_repro/` (OD-15) so the declarations can enter Appendix A; or report the PhaseSource, ReadWriteControl and StructuralClosure results as proved in [GR §3.3], with the failure of (iv) for the stated class stated as an inference from them, without the "machine-checked" label until then; or defer.
  `papers/introduction_repro/` (OD-15) so the declarations can enter Appendix A; or report the
  GR:260 results as proved in [GR §3.3] without the "machine-checked" label until then; or defer.
- **F-19 (OD-3).** Commission a drafted ε-realization paragraph restricted to the exact regime,
  with its review; or defer to #945.
- **F-15.** (a) Land #989's two commits on `main` by an owner-authorized retention change;
  (b) at landing, cite the in-tree files with their blob ids and treat the two commit ids as
  provenance; (c) remove the [CE]/[CR] claims until retained.
- **F-16.** Before landing, either (a) [CR] receives an independent review (#970), or (b) [CR] leaves "Established mathematical results" (and, if wanted, L316 states it as a written proof without independent review). Option (b) is a change of status for the owner to decide; it is not made here.
  established list until reviewed; (c) remove the [CR] paragraph.
- **F-17.** (a) In R0-B, re-pin L371 (and L379) to a `main` commit such as `f5c281ae`, re-confirming the SM and black-hole content the Introduction uses; (b) keep `20ca05fe` and revert the citations that rely on later Main content (this would undo E3, E5, E8 and earlier rows such as Theorem 3's source); (c) retain `021850d9` and `a2be1e45` on `main` or replace them in the re-pin.
- **F-21 (OD-8).** Read [Sha79] first-hand before landing, or replace "as in perfect secret
  sharing, … [Sha79]" by the BHa rank law alone (R-19 text). Check the CT06 locators.
- **F-23 (O-17).** Add "not adopted" to the [BHa]/[BHb] entries, or leave them; the record's own
  status line is #1029's.
- **F-24, F-25, F-26, F-27.** As stated in §3.1.

## 6. Items routed to other Issues (proposed destinations; not edited here)

| Item | Site at `f5c281ae` | Proposed home |
|---|---|---|
| Main:22 cites "[Substratum §3.3]" for H-Bell; the definition is in Substratum §3.2 (:131–133) | Main:22 | #1029 (citations) |
| Main's CP-indivisibility lemma does not state $\mu_H$ diagonal (S9-A7); "the exact conditions" (S9-I6) | Main:328, :340 | #1028 |
| "Certified exactly" for floating-point probes (CON-25; OD-7 corpus side) | Main:176 and related labels | #1029 orphan 39 |
| R-30 corpus side: "send it to different futures" reads universally | Main:105 | #1028 |
| Finite total S in Main's ledger and Main:720/722/726 (NEW-4 Main side) | Main:720–726 | #1015 |
| OD-1: Main's title broader than its theorem | Main:1–2 | #1015 / #1029 |
| BH-01 record S9-M5/M6, S9-A2; status line (SC-7, CON-03) | `bh01_access_v1/REPORT.md`:3, :42–47, :61–62 | #1028 / #1029 |
| Workflow pin `e73f7be3` (evidence-replay.yml) | `.github/workflows/evidence-replay.yml`:52–53 | stays recorded on #941; not an Introduction reference |
| #918 CI hygiene (local paths in `introductory-paper-20261025/` records; checker scope) | §8 | R0-B or a separately authorized cleanup |

## 7. Handoff reconciliation

- **R-01–R-40.** The 20 rows "applied on #918" (R-01, R-08, R-12, R-20–R-26, R-29–R-33, R-35–R-39)
  remain applied and unreviewed; they are in the review packet. Of the 15 open rows: R-03, R-04,
  R-05 (remainder), R-09, R-14, R-15, R-16, R-17, R-27 and R-28 are corrected here; R-18 is
  corrected in its Sch21 part (Bar26 wording kept: read first-hand, Thm 3.3 has the same
  $N^2$-dimensional form); R-06 (F-18), R-07/R-40 (F-19), R-13 (F-20) and R-19 (F-21) stay open.
  The five "changed" rows (R-02, R-10, R-11, R-19, R-34) were re-read against `f5c281ae`; R-02,
  R-10, R-11 and R-34 need no further edit, R-19 is F-21.
- **OD-1–OD-15.** OD-1 routed; OD-2 F-18; OD-3 F-19; OD-4 F-14 (partly resolved on `main`);
  OD-5 F-20; OD-6 consistent; OD-7 applied (E1, E2), corpus side routed; OD-8: Pag93 applied (E14),
  Sha79 and CT06 open (F-21), Har04 cited only as reported by Mon08 (consistent); OD-9 resolved on
  `main`; OD-10 applied (E3); OD-11 consistent (open problem 3 states no distinguishing experiment
  is established); OD-12 consistent; OD-13 F-26; OD-14 resolved on `main`; OD-15 blocked (needs an
  authorized CI run).
- **FA slice 2 D1–D6.** Re-read at `69079058` against Main:76, :82, :137–141, :404–407, :469 and
  :518: consistent; still unreviewed.
- **Track C I-1–I-12.** Recorded on #918 as applied (r16); not re-checked item by item this round;
  in the review packet.
- **Handoff §3–§4 items.** Their destinations are owner proposals and unchanged by this round,
  except NEW-2 (F-08) and the Sch21 item (F-09), corrected here.

## 8. §A.42 item 8 trace of the Introduction's off-`main` references

Reachability from `main` `f5c281ae` and from #918's head `4028e45d` was read with the GitHub
compare API on 2026-11-04.

| Reference | Introduction | Reachable from `main` | Classification |
|---|---|---|---|
| `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86` (baseline Lean pin) | L340, L348 | yes | support on `main`; cited modules' sources equal at `f5c281ae` except a doc comment in `C3Necessity.lean` |
| `4f962b6`, `3d54ae74`, `a958bc54`, `96a3020b` (module checkpoints) | L340 | yes | support on `main`; publication status F-14 |
| `55e3217b` (probe snapshot) | L342 at `a1721681`; not named at `25a9d9fd` (E18) | yes | support on `main`; the BH records are unchanged to `f5c281ae`, and four probe files differ only in wording and in `memory_probes.py`'s grouping by law |
| `20ca05fe` (Main, SM, BH snapshot; Substratum statements) | L371, L379 at `a1721681`; not named at `25a9d9fd` (E18) | yes | support on `main` for the Substratum statements and the BH computations; for Main the pinned version differs from the one the Introduction cites: Theorem (overlap and return), `pIndivisible_of_rooted_identity_return_of_overlap`, `routed_forces_indivisible_somewhere`, the rooted classification and the §2.4 title "A Six-Hidden-State Model" are absent at `20ca05fe`, and Main §3.3 there carries H-Bell's continuum clause (F-17) |
| `f5c281ae10a913ec68fa41b3b839ad0b164979cd` (corpus snapshot, E18) | L342, L371 at `25a9d9fd` | yes (it is `main`'s head at the baseline) | support on `main`; every citation verified there (§14) |
| `021850d9`, `a2be1e45` | L371 at `a1721681`; not named at `25a9d9fd` (E18) | no (diverged) | support off `main` as pins; the content used is on `main` (F-17) |
| `bdcbd32`, `2624d49` ([CE], [CR]) | L387, L389 | no (diverged) | support off `main`; content byte-identical in #918's tree, so it lands with #918; commit reachability unresolved (F-15) |
| `papers/introduction_repro/` (expected Lean result, recipe) | L340 | not on `main` | in #918's tree; lands with #918 |
| `verification/audits/manuscript/page-coherent-recovery-20261028/` | L387 | not on `main` | in #918's tree; lands with #918 (F-15, F-16) |
| `verification/programmes/black-hole-information/` ([BHa], [BHb]) | L342, L383–385 | yes | support on `main` |
| concept DOI 10.5281/zenodo.19060318 | L342, L371 | external | provenance |
| `17b830bc` recipe's `tools/release_gate.py` | L340 | yes | support on `main` |

This record itself cites #942's branch (`16fc745d`), #941 and #918 comments and CI run
41634688564 as provenance only: no claim here uses their content as sole support.

## 9. Build reproducibility

| Item | Value |
|---|---|
| Toolchain | pandoc 3.1.3; XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian) |
| Command | `sh ./build.sh Introduction`, from the worktree root |
| Source commit `340961ce` | 25 pages; median 3,891 characters per page (pdftotext); 0 "Missing character" warnings |
| Source commit `69079058` | 25 pages; median 3,898 characters per page; 0 "Missing character" warnings |
| Source commit `a1721681` | 25 pages; median 3,898 characters per page; 0 "Missing character" warnings; stamp `bb045f94…` |
| Source commit `25a9d9fd` | 25 pages; median 3,884 characters per page; 0 "Missing character" warnings; stamp `9f6fcdcb…` |
| Stamp | each `.tex` ends with `% source-sha256:` of its own commit's `Introduction.md` (`3a1b988d…` and `94a2cff2…`) |

Each commit's `.md`, `.tex` and `.pdf` are from that commit's source. No claim is made that the
output is byte-identical or equivalent to any earlier PDF.

## 10. Literature read this round

| Source | Read | Passage | Bears on |
|---|---|---|---|
| Montina, arXiv:0711.4770v2 | first-hand | abstract; §I, pp. 1–2 | F-12: the 2N−2 bound covers Markovian ontological theories; no explicit task; reports Hardy's finite-ontic-state result |
| Galvão–Hardy, arXiv:quant-ph/0110166v3 | first-hand | abstract | F-12: an explicit task |
| Heinosaari–Kerppo–Leppäjärvi–Plávala, arXiv:2308.07727v4 | first-hand | abstract; Thm 4 | F-12: explicit task family with unbounded classical dimension |
| Doukas, arXiv:2602.22095v3 | first-hand | §4.2.1, Prop. 1 and proof; App. A | F-10; C-055 |
| Rivas–Huelga–Plenio, arXiv:1405.0303v2 | first-hand | Thm 2.4 and proof | F-11 |
| Buscemi–Datta, arXiv:1408.7062v3 | first-hand | Prop. 1, Cor. 1 | F-11 |
| Page, arXiv:gr-qc/9305007v2 | first-hand | abstract (average entropy of a subsystem in a random pure state); full text searched for "black hole" | F-13; E17 |
| Page, arXiv:hep-th/9306083v2 | first-hand | abstract; first paragraph; journal reference from the arXiv record | F-13 |
| Barandes, arXiv:2608.04354v1 | first-hand | Thm 3.3, eqs. (43), (50), fn. 1 | F-09; C-027 |
| Schmidt, Sch21 | not read | — (Bar26 fn. 1 is the secondary source) | F-09 |
| Shamir, Sha79; Hardy, Har04; Cover–Thomas, CT06 | not read | — | F-21 |

These sources support or challenge what the Introduction says the literature establishes; none
of them shows that a result follows from OI's own premises.

## 11. #918 CI failure at `4028e45d` (read-only diagnosis)

From the host's job and step records for run 41634688564 (pull-request event, `head_sha`
`4028e45d…`, so a synthetic merge with `main`), read through the Actions API: 23 jobs succeeded,
"A42 exclusion" was skipped, and two failed: "Numerical probes / core B" at its step 8, "SC-42
integration source scope and must-fail controls", and the aggregate "Numerical probes" at "Require
every probe shard". "Mathlib bridge" (build and release gate) and "Lean kernel check" succeeded.
That step runs `check_sc42_integration.py`, whose added-text scan diffs the whole tree against the
fixed base `ca3a5bb2` over `*.md` and `*.py`, so it scans every file #918 adds, and fails on any
local-path, e-mail-like, history-voice or capitals hit. The diagnosis on #918 c.6603786828 (21
hits: false positives in matrix code and a pattern name, the Introduction's "no longer" about a
face-up card, three code identifiers, and real local paths in records under
`verification/audits/manuscript/introductory-paper-20261025/` and one SC36 script) is consistent
with that scope; its hit list comes from the job log and is provenance (§A.44). The fix touches
files outside this authorization. This round's additions were written to add no such hit. No
re-run was made.

## 12. Review packet

**Head to review:** the record revision that follows `25a9d9fdc0bfd0ee2aff9d3da3f8d425452a1efe`
on `draft/oi-introductory-paper-20261025`; confirm the exact SHA from the #918 checkpoint comment.
Corpus: `main` `f5c281ae`. The owner asks the reviewer to focus on the corpus pin (E18, §14.1), the
[CR] classification (E19), the scope of F-18 (E21) and the provenance at L41 (E20); items 1–8 below
stand for the earlier edits.

The reviewer is asked to check, one by one:

1. E1–E17 against their findings and sources (§3.2, §4), including that each is the minimum
   change and adds no claim beyond its source. E15–E17 are new since the first review.
2. The first-hand literature readings in §10 at the cited passages (F-09–F-13).
3. The hand derivation in F-02 (three-hidden-state model).
4. The claim map's part A and the classifications of part B, especially C-006, C-007, C-024,
   C-037, C-041, C-047, C-062, C-065, C-079, C-094.
5. The previously applied, unreviewed rows: R-01, R-08, R-12, R-20–R-26, R-29–R-33, R-35–R-39;
   D1–D6; I-1–I-12.
6. The §A.42 item 8 trace (§8).
7. The build record (§9): `.md`, `.tex`, `.pdf` of each commit from that commit's source.
8. That nothing in this round decides an owner question (§5) or edits outside the authorized
   files.

Nothing in this record is independently reviewed yet.

## 13. Response to the independent review of `b935150b` (#918 c.6643385201)

| Review item | Disposition |
|---|---|
| 1 (blocking): corpus pin vs citations | At `c806fb67`, not re-pinned (the owner's decision of #941 c.6643474520 then authorized it; applied by E18, §14.1): #918 c.6603786828 assigns "pins and labels" to R0-B, which this workstream is not authorized to carry out. Recorded as an owner item with F-17, raised to high (§3.1, §5); the §8 `20ca05fe` row now states the differences; F-02, F-04 and F-07 are qualified as relative to `f5c281ae`. |
| 2 (blocking for landing): [CR] unreviewed | F-16 raised to high; options (#970 review, or moving [CR] out of the established list) stated in §5, not decided. |
| 3: L41 overstates §3.4 | New finding F-28; corrected by E15 (`a1721681`). CLAIM-MAP C-020 updated. |
| 4: F-18 rescope | F-18 rewritten with the kernel statements as stated in the modules, the one-line inference to (iv) marked as such, and `substratumClass_structurallyClosed`; CLAIM-MAP C-238 updated. |
| 5: F-20 | Rewritten: L174's gloss is the reading-neutral clause of Main:147; a completeness finding, severity low. CLAIM-MAP C-174r updated. |
| 6: Montina's scope | F-12, §10 and CLAIM-MAP C-072 state that the bound covers Markovian ontological theories. |
| 7: authorization links | §1 links the activation record, #941 c.6643207092 and #866 c.6643204362, and states their timing. |
| 8: editorial | E16 (L83 "of total dimension") and E17 ([Pag93a] for "Page's Haar mean", the information paper relabelled [Pag93b]) in `a1721681`, rebuilt (§9). |

## 14. Owner decisions of 2026-11-04 and their application

Decision record: [#941 c.6643474520](https://github.com/amaybaum/incompleteness/issues/941#issuecomment-6643474520)
(amaybaum, 2026-11-04). The edits are in `25a9d9fd`; E1–E17 are kept.

### 14.1 Corpus pin (F-17, E18): verification at `f5c281ae`

Before re-pinning, every result the Introduction cites was checked at `f5c281ae` by reading the
sources (no build, no computation):

- **Main.** Every named anchor the Introduction cites is present: Remarks (status of the early
  commitments) :62, (the measure as a realization datum) :60, (what this equivalence does and does
  not say) :556, (a variational question) :616, (why (C4) is a separate condition) :178, (three
  notions, kept apart) :340, (scope: P-indivisibility is not quantum non-Markovianity) :336,
  (representation, not explanation) :638, (scope: representability, not selection of the relating
  evolution) :646; Theorems (finite-horizon process dilation) and its Extension :518–520,
  (finite-horizon stochastic–reversible–unitary equivalence) :548, (physical memory: C2, process
  form) :469, (unavoidable hidden predictive memory) :604, (history readback + finite recurrence
  implies indivisibility) :137 with its Scope :141, (overlap and return) :143, (CP-indivisibility,
  framework scope) :332, (Bell ceiling for a screened local completion) :366; Lemma (accessible
  conditional memory from readback) :173; Proposition (finite-substratum operational obstruction —
  classical-dimension form) :560; Corollary (Bell–lattice obstruction and state-dependent escape)
  :416; §1.5 corollary :99; §2.4 six-hidden-state model :184; §3.1 one-step dilation :212; §4.5
  :720; the rooted classification :640. The title matches the [Main] entry.
- **GR.** §2.2 :44 ((C4) not demonstrated at the horizon, :52), §3.3 :168 with Theorem 4 :218 and
  its kernel identifiers, :220 (independence, `oi_alone_not_qm`), :260 (substratum source),
  §6.2 :342 (offset invariance and the G3 condition, :356), §6.3 :364, §8.5 :613 (:637), App. A.6
  :793, A.7 :807 (Thm A.7 :813), A.8 :821 with its scope :839–853, A.9 :855. Title matches.
- **Substratum.** §§3–4 :66, :247; H-Bell §3.2 :131–133; Theorem 24(iii) :251–261;
  Proposition 24.5 :348–360. Title matches.
- **SM.** Title matches; the Introduction cites SM only through Main §3.3's Corollary (:416).
- **Book.** §1.11 (`ch01`, :265), §3.8 with the regress paragraph (`ch03-structural-realism.md`
  :190, :218), §7.6 (`ch07-gravity.md` :108).
- **BH records.** `bh01_access_v1/REPORT.md` :18, :21, :101–111, :148–155 (all §5 counts and the
  floor; title matches [BHa]); `bh02_scramble_v1/REPORT.md` :1 (title matches [BHb]). Both
  directories are unchanged between `55e3217b`, `20ca05fe` and `f5c281ae`.
- **Lean.** Every Appendix A identifier resolves at `f5c281ae` at the line Appendix A gives (the
  baseline module sources equal `17b830bc` except a doc comment in `C3Necessity.lean`; the four
  additional modules' blobs equal their checkpoints).
- **Superseded pins.** `021850d9` (GR SC-36 scope) and `a2be1e45` (Book regress): the content the
  Introduction uses is on `main` at `f5c281ae` (GR :839–853; Book `ch03` :218), so L371 cites
  `f5c281ae` for GR and the Book as well.

No citation failed. The Lean pin `17b830bc` (L340, L348) is not changed: Appendix A's axiom reports
and expected result were produced at that commit, which is an ancestor of `main`. No rebase or
merge into #918 was made.

### 14.2 [CR] (F-16, E19)

[CR] is out of "Established mathematical results" (L322) and is stated at L316 as "proved on paper
and not independently reviewed"; its review stays an obligation on #970. [CE] stays in the list
(its in-tree review covers `bdcbd32`). The Contributions sentence (L41) now names [CE; CR] among
§5's records (F-24), without a status claim.

### 14.3 L41 provenance (F-28, E20)

L41 states that in §3.4 the factorization through finitely many ontic states is proved in [Main]
(Main:560) and that the unbounded classical dimension is the result of [HKLP24, Thm 4]
(arXiv:2308.07727v4, read first-hand). The literature result is cited as the literature's, not as a
consequence of OI's premises.

### 14.4 Condition (iv) (F-18, E21)

The statement made, and its assumptions:

- **Class.** The operations that finite bijective dynamics supplies under the stated observer
  access: in the kernel, `permClass` (`SubstratumInterfaceAudit.lean`:236, scaled partial
  permutations), the class GR:260 describes.
- **Carrier.** A nonempty finite system with at least two states (`2 ≤ Fintype.card A`).
- **Kernel statements used.** `permClass_onesFixing` (PhaseSource:79: every isometry of the class
  maps the all-ones vector to a multiple of itself) and `onesFixing_not_phasesAvailable`
  (PhaseSource:52: for a ones-fixing class, the generated theory does not have the quarter phase
  available at every level; `PhasesAvailable`, RouteB:132). Their composite is also stated as
  `permTheory_not_phasesAvailable_onesFixing` (PhaseSource:104).
- **The one step, not itself a kernel statement.** Condition (iv) requires every finite unitary on
  every composite to be available; the quarter-phase gate (`phaseGate`, LieRankSource:209) is a
  finite unitary; so (iv) fails for that theory.
- **Not claimed.** Nothing about a substratum with further intervention principles (open, L238,
  L328); nothing about (iii) or (v), on which `substratumClass_structurallyClosed`
  (StructuralClosure:316) bears for the class with the stipulated phase.
- **Appendix A.** No entry is added: an entry would need its `#print axioms` report in the retained
  result (OD-15, not authorized). The text says the two statements are checked in Lean in
  [GR §3.3], outside the checkpoints of Appendix A, so the paper's "machine-checked" convention
  (L43) is not extended to them.

### 14.5 The four Lean families (F-14, E22)

The text at L322 and L340 says the four modules are built and checked with the library on `main`
and that their proofs have not been independently reviewed. Evidence for "built and checked":
`verification/lean-mathlib/OIBridge.lean` imports them (L21–24), and the `verify` workflow's push
run on `main` at `f5c281ae` (run 41908494436) concluded `success` (Actions API, structured run
conclusion). The census side is kept out of the paper: the four families are `kernel-only` in
`verification/lean-manuscript-census.json`, and their registration as `current` with manuscript
anchors is outstanding. "Census registration" names an internal registry, which §A.27 keeps out of
manuscript voice; the reader-facing content of the owner's decision, that the formal proofs exist
and are checked but have not been independently reviewed, is fully stated by the chosen wording, so
no neutral paraphrase of the registry step was needed.

### 14.6 Checks and build

`sh ./build.sh Introduction` on `25a9d9fd`: 25 pages, 0 "Missing character" warnings, median 3,884
characters per page (§9). Local checks passed on that tree: staleness, voice, claims, duplicate,
coverage and the Lean-manuscript census. The `INTRODUCTION:*` ledger lines (67, 103, 120, 154,
160, 234) did not move.
