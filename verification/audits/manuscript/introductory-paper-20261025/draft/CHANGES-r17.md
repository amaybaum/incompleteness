# Introduction r17: changes against r16 (`papers/Introduction.md` at `a32b769c`)

r17 integrates the two independent reviews of r16 at `a32b769c`, both ACCEPT WITH CHANGES:

- the scientific review, findings S1–S13;
- the editorial and citations review, findings E1–E20, with its cut package K1–K10.

It follows the owner's decisions of 2026-10-27. Every finding was checked against the sources at `main` `55e3217b`; on
this branch, Main, GR, the book and the black-hole records are identical to that commit. Line numbers below are
`papers/Introduction.md` at the r17 commit.

The focused re-review asks three questions; sections 1–3 answer them in order. Section 4 lists what was not applied, and
section 5 gives length and checks.

## 1. The recurrence theorem's scope is identical in the abstract, §2.5 and §6

The reference is §2.5. The definition sits at L97: "Fix one hidden prior shared by every root, and write Γ_t for the
rooted transition matrix … with a row for every x₀ ∈ 𝒞_V, roots of visible probability zero included". The statement is
the Corollary at L105.

| Scope element | Abstract L12 | §2.5 L97/L105 | §6 L213 |
|---|---|---|---|
| one hidden prior shared by every root, drawn independently of the root | "with a hidden prior shared by every root and drawn independently of it" | L97 "one hidden prior shared by every root"; L105 "shared by every root and drawn independently of it" | "a hidden prior shared by every root and drawn independently of it" |
| the conclusion concerns the rooted family, rows for every root including zero-probability roots | "the rooted visible family, with a row for every root including roots of visible probability zero" | L97 "roots of visible probability zero included"; L105 "let Γ_t keep a row for every root, roots of visible probability zero included … the rooted family" | "the rooted visible family, with a row for every root including roots of visible probability zero" |
| hypothesis | "whenever some rooted transition matrix is not a permutation" | "If some Γ_s with 0<s<L is not a permutation" | "whenever some rooted transition matrix is not a permutation" |
| conclusion | "P-indivisible somewhere in its recurrence cycle" | "not P-divisible on {0,…,L}" | "recurrence-cycle P-indivisibility" |
| supply | "which every non-deterministic visible step supplies" | "Two distinct positive-probability visible histories with a common endpoint, in particular a memory witness, supply such a Γ_s, and so does every non-deterministic visible step, also when the law is Markov on every accessible window" | "every non-deterministic visible step and every memory witness supply a non-permutation rooted transition matrix" |
| full-support equivalence | "with a full-support visible prior this indivisibility is equivalent to conditional memory M_k>0 at some order k below the recurrence time" | "With a full-support visible prior, this failure is equivalent to M_k>0 at some order k<L" | "with a full-support visible prior the indivisibility is equivalent to M_k>0 at some order k below the recurrence time" |

**Source anchors.** Main §2.3:

- Theorem (history readback + finite recurrence implies indivisibility): "μ_H a hidden prior shared by every root … roots of visible probability zero included … root … drawn from a visible prior and the hidden state from μ_H, independently";
- its proof: "possibly only through a row of a root of visible probability zero";
- Scope: "With a full-support visible prior the hypothesis and the conclusion coincide … For every visible prior, a non-deterministic visible step … makes some Γ_s a non-permutation";
- Main :20, the abstract: "the full rooted visible process".

Kernel: `CausalReadback.lean:178`, `RootedRealization`, one hidden prior common to every rooted visible preparation.

**Consistency with #956 (Medicine :25 at `b7632485`).** "on one fixed finite reversible representative, with a hidden prior shared by every root and drawn independently of it, the rooted visible family is P-indivisible somewhere in its recurrence cycle whenever some rooted visible map is not a permutation … Every non-deterministic visible step supplies such a map … With a full-support visible prior this indivisibility is equivalent to M_k > 0 at some order k below the recurrence time". The two texts have the same hypotheses, object and equivalence. The Introduction additionally names the zero-probability rows, which Medicine carries implicitly in "rooted".

**Findings closed here:**

- S1 = E1: the abstract, required.
- S2: §6, required.
- E6: the result is displayed as the Corollary at L105. This is a different paragraph from the §2.4 Corollary at L89, which stays byte-identical, so `INTRODUCTION:C-unnamed-b596be8a` is unchanged. The display adds one coverage row, `INTRODUCTION:C-recurrence-cycle-indivisibility` (MIRROR, fingerprint d33c081326f983a5); no ID is retired.
  - The reviewer's proposed text is changed in one respect. A non-deterministic step is listed separately from "two histories with a common endpoint": its histories end at different states, so it is not an instance of that clause. Main's Scope supplies the non-permutation for it directly.
- S6: the directions of the equivalence are given at L107: "a memory witness below L gives a non-permutation Γ_s; conversely, with none the law on {0,…,L} is Markov, Γ_L=I makes every Γ_s a permutation by the stochastic-inverse lemma, and Γ_s⁻¹Γ_t is a stochastic divisor, full support being needed only in this converse". Source: Main §2.3 Scope.

## 2. Each strengthened claim, with its proof and verification status

| Site | Claim added or raised | Proof and status | Anchor |
|---|---|---|---|
| L107 (S3, owner: include) | from a non-permutation Γ_s, the conclusion is Theorem 3 with n=L, machine-checked in its rooted form; only the supply of the non-permutation is on paper | kernel, plus the elementary step "a non-permutation square stochastic matrix has two rows sharing a positive column" (Main §2.3, first theorem's proof, Step 2), which is stated, not called machine-checked | `RecurrenceHorizon.lean:148` `pIndivisible_of_rooted_identity_return_of_overlap` |
| L107 (S4) | "Indivisibility at some return horizon is also machine-checked from the routed form of (C4)" | kernel: `∃ n, PIndivisibleWithin n` | `PhysicalC4Discharge.lean:122`; App. A says "indivisibility at some return horizon" |
| L213 §6 (S8, owner: include) | the separation of conservation from recovery "rests on exhaustive enumeration with the 1/\|𝒰\| floor proved" | written proofs C1 (exact recovery under complete access) and C2 (P_succ ≥ 1/\|K\|), valid for every finite bijection | BH-01 `REPORT.md`, Proofs |
| L167 (S9, owner: only if established) | "two lifts have equal rooted families exactly when their one-step visible matrices are equal, and equal one-step matrices give equal trajectory laws at every horizon (machine-checked, both directions)" | kernel iff for rooted families; one direction for trajectory laws | `TrackBQfbBridge.lean:180` `rooted_eq_iff_slice_eq` (↔); `:276` `bridge_traj` (equal G ⇒ equal `rootTraj`). Main :640 states the non-selection; no "exactly when" is claimed for trajectory laws, because the marginalization step from trajectory laws to rooted families is not a cited kernel statement |
| L93 (S10a, owner: include, coupling-step scope, no mixing assumption) | "The necessity of (C2) is a theorem in the coupling-step model … observed conditional memory I*>0 at an accessible order forces some realized hidden conditional at a coupling time to lie at total-variation distance at least ε_min(I*,\|𝒞_V\|)>0 from the model's reference prior, with no mixing hypothesis" | paper proof (Fannes–Audenaert), certified by the probe `c2_mixing_probes.py`; the persistence form takes ε as the realized maximum, so the hypothesis holds by definition | Main §3.4, Theorem (physical memory: C2, process form), the final paragraph of its statement |
| L177 (S10b, owner: one clause at most) | the nearest-neighbour cubic update of [SM] alone cannot supply ontic parameter dependence for wings beyond its graph cone | paper proof: Main's corollary, which applies the Bell ceiling | Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape) |
| L91 (E7, §2.4 significance) | "measurable conditional information fixes a lower bound on the hidden sector's size and the exact minimum of the predictive memory a deterministic completion must carry" | restates the capacity bound (kernel, joint-law form) and the variational value (paper; lower bound kernel for bijective realizations) | Main §3.4, Corollary (per-process capacity bound); Remark (a variational question); `C3Necessity.lean:88, :117` |
| L93 (E12) | I* = max_t I(X_<t;X_>t\|X_t); (C3) given its content log₂\|𝒞_H\| ≥ I* | Main writes sup_t; on a finite horizon it is a maximum, and the kernel takes the maximum over a finite family | Main :78, :508; `C3Necessity.lean:94–117` |
| L85 (E8 / attribution) | "(b) and the first inequality of (c) are data-processing inequalities" | attribution only: standard | — |

## 3. Nothing weakened, nothing expanded beyond the evidence

**Corrected to the evidence (no strengthening):**

- **L177 (S5, owner: correct).** No-signalling is now a requirement: "one wing's microstate response may depend on the remote setting … while operational no-signalling is required. That a preparation-indexed coupling graph can supply it while preserving operational no-signalling and the gravitational continuum limit is the open hypothesis H-Bell". Source: Main §3.3, H-Bell, "the prepared graph family must preserve operational no-signaling and satisfy a curvature/metric convergence condition".
- **L205 (E3 = S7, owner: name the layout).** "The layout is that of the Page-curve setup [GR App. A.7] at small size". The 1,376/40,320 count is in the moving-partition layout; the nested V/B/D layout gives 2,688 (BH-01 `REPORT.md`, key numbers).
- **L207 (E2, required).** Shamir is no longer credited with a bound: "so hiding the message completely needs at least as many hidden values as messages, as in perfect secret sharing, of which Shamir's threshold scheme is the standard example [Sha79]".
- **L209 (E4).** τ_B^D is "the D-sector timescale τ_B^D ∼ 1/H [GR App. A.5]", which is GR's own term (GR :759, :809). The reviewer's "B–D coupling time" is not GR's term.
- **L222 (S11).** "gives a lower bound on the hidden sector's coarse-grained mixing time, the slow-bath form of (C2)" (Main :76, :465).
- **L197 (S12).** "the G3 coupling theorem … [GR §6.2, §8.5]" (GR :28, :615, :637).
- **L149 (E11).** "spectator-independent" is glossed from the kernel definition: "one that acts on every product input as the identity on the system" (`MapSpectatorIndependent`, `OperationalAssembly.lean:147–151`). The reviewer's gloss, "does not depend on untouched systems", is not what the definition says.
- **L18, L120, L215 and Code L229 (S13).**
  - "can send it to different futures";
  - "P-divisible on {0,1,2}";
  - "cycle-averaged Page curve … with all of 𝒞_B×𝒞_R one energy shell";
  - "`verification/lean-mathlib` tree is identical".
- **L28 (S13).** Contributions say "§§3.2–3.5" and identify the Bell ceiling as Bell's theorem under the framework's hypotheses. The novelty statement covers only §§3.2–3.3 and §5.

**Not adopted, because it would expand the claim:** E7's proposed §2.5 sentence, "generic for embedded observers" and "the feature the correspondence ties to quantum behaviour". It is replaced by "Recurrence-cycle indivisibility thus follows from finite reversibility and partial access alone, Markov laws included, and does not distinguish one law from another; what an observer can discriminate is memory at an accessible order, which (C4) asserts".

**Limitations consolidated (E8), each kept at its derivation site and in §6:**

- "represents, does not derive": L143 (§3.1) and L213 (§6); removed from §1.2;
- the Born exponent: L66 (§2.3) and open problem 2; the §3.5 sentence is removed, and the section is retitled "3.5 Bell structure";
- G3: L197 (§4) and the §6 applications list; the closing line of §6 is removed;
- the Page-curve open items: §6 only;
- the vanishing-criterion evidence class: L85 (§2.4), and the L89 Corollary is unchanged; removed from Appendix A's Theorem 2 item.

No established result is removed.

**Notation and definition only (E5, E9, E10, E13–E16, E19, E20), no change of claim:**

- the dilation is written |𝒞_V|²-dimensional (E5);
- the CP/[BBS24] paragraph moves to §3.1 at L143, entanglement-breaking is glossed as measure-and-prepare, and the decomposition sentence is repaired (E9);
- "memory witness" replaces "(C4) gap", and the causal cone is glossed (E10);
- "rooted transition matrix", visible/hidden configurations and "initial law (the prior)" are used, and "street" is deleted (E13);
- g_#μ is defined in §2.1 (E14);
- the §6 apposition is fixed (E15);
- §5 access: the observer reads the emitted radiation registers on a schedule fixed in advance (BH-01 claim A) (E16);
- the TV arguments are μ, ν and the graph distance is d_G (E19);
- the Cal26 DOI is added (E20);
- "determinism is part of OI" (E17).

## 4. Not applied, with reasons

| Item | Reason |
|---|---|
| K8 as proposed; E18 | rewrites the L89 Corollary and would retire `INTRODUCTION:C-unnamed-b596be8a`; owner decision pending. L89 is byte-identical |
| K9: §3.2 setup compression | drops structure fields (preparation followed by an operation; composition at every ancilla level) that the r11 final review's B1 required against `OperationalAssembly.lean:594` |
| K9: §3.3 compression | drops the "exactly when" the owner kept (S9) |
| `cut8.md` reference edits | they strip the arXiv identifiers from 25 entries (for example "(2019).08762"), a corruption |
| `cut8.md` Contributions | drops the novelty statement that citation finding M3 requires |
| `cut8.md` §3.4 | collapses "Montina reports Hardy's result" into a bare citation of [Har04], which was not read first-hand |
| E17: "no earlier statement … is identified" | would report a literature search that was not made; the novelty statement is kept |
| E17: "status ledger" | kept, since it is Main's own term |
| Book §1.11 card-burn note | not part of #918 (owner); tracked as a separate source correction |

**Applied from the cut package:**

- K1: `\parskip` 1pt in the references and Appendix A; Appendix A in `\footnotesize`;
- K2, with the S10a sentence added;
- K3;
- K4;
- K5;
- K7;
- K9: Realization, Attribution, §3.4, the code note, and the L38 and L139 merges;
- K10: the heading is shortened, and the abstract is 233 words, because the owner-required scope elements lengthen it;
- K6, in the Contributions paragraph only.

## 5. Length and checks

- **Length:** 18 pages at r16, 17 at r17 in the default geometry. The main text (§§1–6) is about 13.8 pages and ends on p. 14, followed by the code note, Appendix A and the references on pp. 14–17. This is the closest reachable without removing an established result, an owner-required addition or the L89 paragraph. The 15-page target depends on the owner's two open decisions: one-inch margins, and the L89 ID.
- **Build:** `sh ./build.sh Introduction` is OK, with 0 overfull boxes and 0 missing characters.
- **Release gate:** every step passes except `lean-axioms`, which needs `lake` and cannot run locally; it passes in CI. `voice`, `claims`, `duplicate`, `coverage` (134 canonical statements) and `mirror` all pass. `verification/lean/edge_rigidity_probe.py` reports ALL CHECKS PASS.
- **Appendix A:** all 29 declarations resolve at their stated lines at `17b830bc` and at the head; no name is unlisted or missing.
- **Coverage:**
  - T-1, T-2, T-3, T-4 and `C-unnamed-b596be8a` are unchanged;
  - `C-recurrence-cycle-indivisibility` is added;
  - no ID is retired.
- **Added-lines scans:** the §A.32/§A.33 phrase families, caps emphasis, markers and secrets give no hits, and neither do "generic" and "constitutional".

## 6. Addendum: one-inch margins (owner decision, 2026-10-27)

**Owner decisions.**

- One-inch margins are approved, "provided the resulting manuscript remains readable and the mathematical expressions,
  figures and references render correctly".
- Retiring the L89 coverage ID is not approved: "scientific content and verification integrity take precedence over
  page-count targets".

**Change.** A YAML metadata block, `geometry: margin=1in`, follows the `%` title block of `papers/Introduction.md`; the
generated `.tex` carries `\usepackage[margin=1in]{geometry}`. Neither `build.sh` nor any other paper is changed. The
title text is unchanged.

**Line shift.** The block shifts every line of the paper by 4. The anchors in sections 1–3 refer to the paper before
the block; after it, the abstract is L16, the Γ_t definition L101, the recurrence Corollary L109, its proof paragraph
L111, §6's established results L217, and the §2.4 Corollary L93 (still byte-identical).

**Cuts restored now that the length allows.** Each was made only for length and removed useful content; nothing new is
added.

- **§2.6, minimal model** (cut in r16): the off-diagonal entries 4/9 of Γ₁², and the value a/(2−a) for P(x₀=0)=a.
- **§2.5** (cut in r17): "Monotone distance is necessary for P-divisibility but not sufficient [Main §2.3]".
- **§2.2, Realization** (cut in r17): the rational-kernel form of the process dilation, with the visible initial law arbitrary.
- **§3.3** (cut in r16): "each such trajectory law is a fixed-basis Born record and stochastic" (`realData_traj_stochastic`, already listed in Appendix A).
- **§3.4** (cut in r17): the explicit attribution "explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's result … [Mon08; Har04]".
- **§4** (cut in r16): the de Sitter entropy dimensional identity.
- **Appendix A** (cut in r17): the scope notes "Prior independence is proved on paper"; the Theorem 2 item's "the time-t identification and the standard vanishing criterion … are proved on paper"; and the capacity item's "for bijective realizations in the same joint-law form". The block is back in `\small` (the references keep `\footnotesize` with 1pt paragraph skip).

The closing line of §6 is not restored. It was removed as a repeated limitation (E8), not for length.

**Coverage.** All fingerprints are unchanged. The `line` fields of the six Introduction rows are updated to the new lines
(T-1 52, T-2 78, C-unnamed-b596be8a 93, T-3 103, C-recurrence-cycle-indivisibility 109, T-4 161).

**Measurements.**

- 12 pages (letter, one-inch margins). The main text (§§1–6) is about 9.4 pages and ends on p. 10; the code note,
  Appendix A and the references take pp. 10–12.
- Median 3,550 characters per page (range 2,500–4,500); no table collapse.
- LaTeX log: 0 overfull boxes, 0 missing characters, and 1 underfull line (the code note's 40-character hash;
  benign).
- **Spot-check renders** (PNG at 80 dpi):
  - p. 1, title and abstract: title on two lines, abstract and §1 on p. 1;
  - p. 5, the display-heavy page: the Γ matrices display in full within the margins, and the card-table rule and caption-free table align;
  - p. 8: both field-equation displays are within the margins;
  - p. 11: Appendix A's `\small` group, then the references' `\footnotesize` group, with clean wrapping and no overflow from long titles or arXiv identifiers.

**Checks.**

- The release gate passes every step except `lean-axioms`. That step needs `lake`, which is not installed here; it passes in CI.
- `voice`, `claims`, `duplicate`, `staleness`, `coverage` (134 canonical statements) and `mirror` all pass.
- `edge_rigidity_probe`: ALL CHECKS PASS.
- Appendix A: all 29 declarations resolve at their stated lines at `17b830bc` and at the head.
- Added-lines scans (voice phrases, caps, markers, secrets): no hits.
