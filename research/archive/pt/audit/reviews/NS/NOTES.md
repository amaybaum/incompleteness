# NS — running notes (thread NS, research-only review)

Protocol: `pt/audit/stage3-inputs/PROTOCOL-NS.md` (`4f61891f…`), over `PROTOCOL-STAGE2-DS.md` (`086a4cb8…`),
`PROTOCOL-STAGE2.md` (`38603692…`), `PROTOCOL.md` (`239dc123…`), amendments 1 (`b41aa0e7…`) and 2 (`2a2f78f3…`).
Input: `pt/audit/stage3-inputs/ns/NS-INPUT.md` (`d8c5a1b3…`), read as data. Base L = `9f9f8257…` at `pt/base/`.
Working directory: `pt/audit/reviews/NS/` (only place written).

## Log

- 12:36:14Z — Step 0 done (read in order: PROTOCOL-NS, PROTOCOL-STAGE2-DS, PROTOCOL-STAGE2, PROTOCOL, amendments 1–2,
  NS-INPUT, DS/RESULT §0–§1, audit/DS/AUDIT-DS, base/AGENTS.md L41–95, L306–342, L417–455). PROTOCOL-STAGE3: hash only.
  Directories listed but not read: `pt/audit/stage3-inputs/` holds OWNER-* files and `qsd_owner_*` scripts; neither is
  among NS's inputs; not opened.
- 12:36:14Z — Step 1: `.start_marker` written first into a freshly created empty `NS/`; every start check OK
  (7 manifests silent; HEAD 9f9f8257…; status empty with `GIT_OPTIONAL_LOCKS=0`; no bytecode; 7 protocol hashes OK).

## Productivity test (fixed before the investigation; §A.31 / PROTOCOL.md L118–120)

A finding is a gem iff it is (1) an exact certificate at a stated instance (derivation with every step checked, or an
exact countermodel), (2) an exact obstruction for a stated class of routes, or (3) an exposed hidden assumption, AND it
is strictly stronger than the obvious restatement. Otherwise record-only. Output classes NEW / POSITIVE / ELABORATING /
CONFIRMING / BORDERLINE. Fixed point: 3–4 passes with no NEW finding, or the questions answered.

## Plan (depth-first; decisive branch first)

- NS.2 first (what the corpus actually says; the input's repository claims hang on it), then NS.5 (decisive: the null
  model), then NS.4 (symbolic identities), NS.6, NS.7, NS.8, NS.3, and NS.1 assembled last from the anchors.

## Node log (depth-first; each node closed by a check)

**N2.1 Where the input's repository paraphrases live.** Read in full or at the cited ranges: PROGRAMME.md (231 lines),
hidden-sector-singularity-hypothesis.md (80), H-B result/prereg, H-A result (H3a, H4a), H-D result (A5S-3, A5S-4), H-F
result (HF5, HF6), H-E result (outcome, HE1), ROADMAP L1158–1233. Checks: quotes copied with line numbers.
- PROGRAMME L51 and L218 already record "The OpenAI Navier–Stokes work announced on 2026-09-08" as external
  target/motivation only, never a premise. L is dated 2026-10-10 (`git log -1`), so the announcement predates L; its
  content (forcing, Clay, Lean) is still not checkable at L. The corpus says nothing about forcing.
- PROGRAMME L231 (one-line state) mentions H-A, H-B, H-E; it does not mention H-D or H-F. H-F L1007 names "which later
  action carries out the refresh of PROGRAMME §8" as an owner decision not made. ROADMAP has rows for H-A, H-B, H-E only.
- Verdict: the input's paraphrases of PROGRAMME L27 and hypothesis L17 are faithful (detail in RESULT §1).

**N2.2 The H-B closure-failure claim.** Located: H-B result L263–309 (HB3-a), kernel `hb3a_block_state_not_closed`
HexLatticeGas.lean:942–958 and `hb3a_no_closure` :989–997. Evidence: [K] — root import OIBridge.lean:63;
lakefile.toml:2 `defaultTargets = ["OIBridge"]`; verify.yml:70 job "Mathlib bridge", :127 `lake --rehash build`, :150
release gate; release_gate.py:137–138 `lean-axioms`; no `sorry`/`admit`/`axiom`/`native_decide` in the three hydro
modules (grep empty); census lean-manuscript-census.json:875–880 status "kernel-only", manuscript []. H-B result L424:
evidence level 2. Probe script at L: none. The prereg (L157–160, L203–215) says the witness was found by an exact
script "before this file was written", recorded as analysis only; that script is not in the tree (`git ls-files` has no
hydro script; edge_rigidity_probe.py:9474–9484 only checks the theorem text). Nothing to replay byte for byte; an
independent exact re-evaluation is planned (ns2_hb3_recheck.py), labelled [X], not a replay.
- Gem candidate (generic non-closure): H-A already proved the same kind of exact non-closure for the LINEAR wave
  representative (`h3a_no_closure`, HydroSourceAudit.lean:863, d=1, L=6, b=3, every q≥2), with a proved closing control
  (`h3a_control_L4_closes`, :875). So exact non-closure of a block variable is not specific to H-B's gas or to any
  hidden-sector structure. H-E (result L185–195) reads HB3-a as closure-gap item 1 ("the flux term is not a function of
  the coarse state"), i.e. the H3 problem, not hidden-sector evidence.

**N6.1 Declared inputs of the hydrodynamic branch.** PROGRAMME L9, L216 (parallel track; no OI→QM result counts here);
L35 (A1–A6, including linearity); L217 (control 2: the concrete local substratum, not arbitrary finite reversible
systems). H-D L683–685 verbatim: "A5 is needed by the current quantum-completion route, and its necessity for
Navier–Stokes remains undecided"; L599–617: A5 is not neutral (H-A's linearity gate). H-B's candidate fails A5-ker;
admissibility of its class open (H-B L58–62; H-F L1005). Carrier question open (H-F L1008).
- Hidden assumption in the input (C61/C62): "finite, reversible, locally interacting" drops A5 and A6; the only fluid
  witness lives exactly in the class that drops A5, the premise the quantum route uses.

**N8.1 Horizons.** GR L40 (cosmological horizon partition from GR's causal structure, taken as given); GR L597 (a
black-hole horizon is a local causal boundary, does not redefine the external observer's partition; BH physics for
external observers = standard GR); GR L599–605 + Appendix A and book ch07 L118–122 (nested partition: interior as a
secondary hidden sector, a self-consistency exercise); GR §8.7 L691, L697 (smooth Lorentzian metric taken as given;
full nonlinear GR not derived). "singularit" occurs in no paper's GR treatment; spacetime singularities appear only in
PROGRAMME S3–S5. Fluid–horizon touchpoint in the corpus: only Unruh's sonic analogue (GR.md:883) and an analogue-gravity
remark (GR.md:607).

**N3.1 Literature in the corpus.** `git grep` (md, lean, py, json, tex): Bredberg, Lysov, Keeler, Minwalla,
Bhattacharyya, fluid/gravity, membrane paradigm, Damour, cosmic censorship, Burgers, Galerkin: 0 hits each. Strominger:
Structure.md:1456 (dS/CFT, used L458) and :1458 (Strominger–Vafa, used L452) only. Mori–Zwanzig: SM.md:246 attributes
SM's Theorem 1a (L238–244, the exact projected identity for a finite bijection) to "standard Mori–Zwanzig/
Nakajima–Zwanzig structure". So the corpus already has the MZ identity as its own theorem (input C34/C37 understate).

## Script log

- **ns2_hb3_recheck.py** (12 checks): run 1 green, 12/12. VERDICT-HB3 "re-evaluated exactly at L=4, b=2; the separating
  information is collision-dependent"; VERDICT-H3A "re-evaluated". Output values equal the recorded ones (prereg
  L207–213). New [X]: with collisions removed (pure streaming) the H-B pair no longer separates at t+1 (CC1), and at
  L=4, b=2 pure streaming closes even the full block channel histogram (two steps move every particle by exactly one
  block; C3, exhaustive lemma + all 4657 configurations of mass ≤ 2); the gas breaks that rule on c′ (CC3).
- **ns4_scaling.py** (14 checks). Pre-run edits before run 1 (no run had happened): S6 moved from generic sympy
  Functions (`sp.doit` does not exist) to two concrete smooth test pairs plus the chain rule [W]; F1 made non-trivial
  (orbit max over 4 steps = over 64); CC4 made exact (no `nsimplify`, no symbolic `max`; peak = value at j = N/4 with
  |sin| ≤ 1 [W]); header text updated to match, decision rule unchanged. **Run 1: 13/14, S2t FAIL** — harness:
  sympy returned √2π^{3/2}(3 − erf z − erfc z)/4, equal to ‖f‖² by erf + erfc = 1, but `simplify` did not apply it;
  verdict correctly withheld (NO VERDICT). Kept as `ns4_scaling.run1.{py,out,err}`. Fix: `val.rewrite(sp.erf)` before
  simplify (exact identity). **Run 2: 14/14**, both verdicts printed. Note for RESULT: VERDICT-FINITE's "only under
  concentration" rests on Chebyshev [W] (vol{|u| > M} ≤ E/M²), CC4 being the instance.
- **ns5_null_model.py** (decisive). Pre-run edits before run 1: an always-false conditional in Part F replaced by the
  plain conjunction; G5 bounds made exact (values at τ = 0, 2/√5, 1 plus monotonicity [W], scoped to t ≥ 0) instead of
  sympy Min/Max comparisons; CC-F made to compute energy and sup explicitly; header wording for B3/G5. **Run 1: 17/18,
  G2 FAIL** — a real error in my preregistered claim, not a harness defect: the sine-only Galerkin field restricted to
  the invariant odd subspace is not volume-preserving (N=2 field (a1a2/2, −a1²/2), divergence a2/2). Verdict withheld.
  Kept as `ns5_null_model.run1.{py,out,err}`. **Run-2 amendment, written into the header**: G2 tests Liouville, energy
  and V(−c) = V(c) on the full mean-zero sine–cosine truncation (N = 1..4) with an exact cross-check that the odd
  subspace is invariant and carries the sine field; G2-odd records run 1's fact; verdict text names the
  volume-preserving object. **Run 2: 19/19**, VERDICT-NULL printed.
- Gem (NEW, structural): the analogy "finite bijection ↔ measure-preserving truncation" is subspace-sensitive: the
  symmetric invariant subspace that carries the data is not volume-preserving even when the full truncation is.
  Record-only for this review (the null model's conclusions use energy conservation and closedness, not Liouville).

**N5.1 What the null model decides.** Exact [X]: Burgers from −sin x blows up in the gradient at t = 1 with bounded
velocity and conserved energy; every Galerkin truncation is closed, energy-conserving, reversible, globally regular
(exact closed form at N = 2: a1 = −sech(t/2), a2 = −tanh(t/2), gradient at 0 in [−√5, −1] for all t ≥ 0); the
projected exact dynamics is not closed (rate of a1 = (a1a2 + a2a3)/2) and carries a resolved-energy flux; a fully
observed finite bijective family realizes the boxed S1 shape exactly (energy 1, sup N^{3/2}). Not exact here:
convergence of truncations to the smooth solution before t* and their thermalization after it [L, unverified]; no
check uses either.
- Consequence for S1: "regular at every finite resolution" is automatic for finite state spaces (ns4 F1, [W]); the
  boxed non-uniformity with an energy bound is realized with nothing hidden (ns5 F1) → the route "S1 shape ⇒
  hidden-sector transfer" is refuted (route refuted, not INDEPENDENT).
- Hidden assumption (NEW): two notions of "hidden" travel together in the input — (i) the complement of a
  coarse-graining map (Mori–Zwanzig; hypothesis L34, L38 define S2a's hidden sector this way) and (ii) OI's
  observer-level hidden sector (Main's partition; GR L40). Transfer into (i) exists for every nonlinear cascade (ns5
  C2). Hypothesis control 2 (L72) requires a theorem identifying the objects; the input writes "OI hidden sector"
  (input L56) without one. Assumption-watch marker on hypothesis L34/L38 and PROGRAMME L143: an S1/S2a result is
  OI-specific only through the substratum, the map and a discriminating control, not through the word "hidden".

**N3.2 MZ in the kernel.** SM Theorem 1a is [K] at operator level: `mz_identity` OI_Structural_Core.lean:275,
`kernel_equivariant` :291; built by the core job "Kernel check" (verify.yml:46–56, file list :50), zero-import file,
no `sorry`. So C34/C37 understate: the corpus has the identity as a certified theorem.

**N4/N8/N3 passes after N5.** The horizon node (GR L40, L597–605, §8.7; Structure §7.7.1; book ch07) and the
literature node produced corrections and one record-only marker (Structure L496 vs GR L701) but no NEW finding. The
final re-read of RESULT produced precision fixes only: [W] scoping of "every truncation", the input-L38 match, exact
quotes, the energy-supercritical phrasing, and the ns5 amendment sentence in §6. That is three consecutive passes
without NEW, so the fixed point is reached and the questions are answered.

## Findings, classified (§A.31)

- **NEW.**
  - Two notions of "hidden" travel together in the input. The note's S2a defines its hidden sector as the complement of the map, i.e. the MZ complement, so an S1/S2a result is OI-specific only through the substratum, the map and discriminating controls (RESULT §3.2, markers 2–3).
  - The S1-shape route is refuted exactly: by a fully observed finite bijective family, and by closed Galerkin truncations of Burgers against the exact gradient blow-up (§3.1).
  - The odd invariant subspace of a volume-preserving truncation is not volume-preserving (record-only analogy caveat; it came from run 1's failed G2).
- **POSITIVE.**
  - MZ is [K] in the corpus (`mz_identity`), stronger than the input says.
  - The input's dimension and forcing caveats are right [W].
- **ELABORATING.**
  - HB3-a's separation is collision-dependent at its instance [X ns2]; the same kind of non-closure holds for the linear wave rule [K h3a].
  - A5 is the shared premise between the hydrodynamic and quantum branches (H-D records it; the input misses it).
- **CONFIRMING.** The scaling identities and countercontrols (ns4).
- **BORDERLINE.** The Structure L496 status cell (marker 5).

## Writing and end checks

- 13:13–13:23Z: RESULT.md written in parts (§0 table and assessment; §1.1; §1.2–§1.6; §2–§3; §4–§6), re-read in full, precision fixes applied, §7 appended last.
- 13:22:23Z end checks: 7 manifests silent; HEAD 9f9f8257…; status empty (GIT_OPTIONAL_LOCKS=0); no bytecode under base/ or NS/; 7 protocol hashes OK.
- Newer-than-marker sweep outside U/X/audit: empty with unconditional pruning. A first expression pruned conditionally; it was also empty, and was redone for rigour.
- §6 hashes 10/10 OK; replay outs equal outs; all .err files = `exit 0`.
- Observation, not an anomaly: `pt/audit/U` (13:14:33Z), `pt/audit/NS` (13:21:19Z) and `pt/audit/X` (13:22:19Z) appeared in the coordinator's area. Names and mtimes only; not read; not written by this thread.
