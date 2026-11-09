# MATH-CON-1 Stage 1B, first stage (O-1, O-2, O-3a–e): native round MATH-CON-1-S1B-1 — PREREGISTRATION (draft r13)

**Status: drafting, not a candidate `F`.** This file is the control plane of a native round under `AGENTS.md`
§A.39, drafted on its own guiding pull request from `D`. Only the owner designates `F`; an instruction to proceed is
not a designation. Nothing is executed before `F`. Every `PENDING` field is filled before `F` is requested, and control
P refuses a `PENDING` field under `--freeze`. The last pre-`F` commit replaces this status paragraph with the candidate
form.

```v3-round
round MATH-CON-1-S1B-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/
record AM verification/receipts/MATH-CON-1-S1B-1.json
execution A verification/lean-mathlib/OIBridge/PolarizedProtocol.lean
execution A verification/lean/mathcon1_s1b1_check.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

**Frozen expectation for the two blocks (owner condition: both blocks unchanged).** These values are recorded here,
outside the blocks:
- the round declaration's three lines are `round MATH-CON-1-S1B-1`, `kind non-sealing` and
  `record-directory verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/`;
- the governed-paths digest, computed as `S7` defines it, is `81897a90a068b0402e68393f82cffda8fd83f0bda5283316c38d8c58b28e5107`.

Precondition 7, and control T at S1 and `E`, re-derive both from the blocks at `F` with `tools/v3_verifier.py`'s
`control_plane` and `governed_digest`, and compare them with these values. A mismatch fails.

The record directory holds:
- this preregistration;
- any amendments under `amendments/` (before `F` only);
- `controls.py`;
- retained structured evidence under `evidence/`;
- the result note `result.md`.

The receipt path is `verification/receipts/MATH-CON-1-S1B-1.json`. Every other path the round changes is one of the
five execution paths.

None of these changes under any outcome:
- a manuscript;
- a built artifact;
- `verification/ROADMAP.md`;
- a landed kernel module;
- another round's record;
- the design record `DESIGN.md`.

`DESIGN.md` lies outside every entry above, so a change to it is unauthorized under `S7`.

## Authority (quoted with author and time)

- **Owner decision, #1169 comment 6721662886** (amaybaum, 2026-11-08T12:46:00Z). The passages this round is bound by
  are frozen text 3 (*The result note*), quoted verbatim.
- **Owner decision on VOID handling at `E`** (owner, 2026-11-08, coordinating-session decision, to be quoted in the
  round PR's first comment; that comment's id, author and time: PENDING). The option chosen was "Halt-only (Recommended)", shown to the owner as: "Any result at E
  other than a clean pass halts the round and preserves the evidence. No checker rerun path is pre-registered. Runs
  voided by the host (a cancelled run, a lost runner) can be retaken only by a separate decision you record after the
  evidence is preserved." *Stop rule* implements it.
- **The design.** `verification/programmes/oi-qm/reconstruction/mathcon1-polc-20261108/DESIGN.md`:
  - blob `4d47fbc876427a26dff12a486fa43a67a95aac5b`, sha256
    `6f502c51e2e362621773f84454131671ae0c6baab46f2678b4fa09d174d61e3d`;
  - committed as `06b5d4f23895baebf1372b6a4cbb2c85f5044458` (#1206), whose single parent is
    `41a42cb97e5e044f5a9e906e33fbf6f22de52dc4`. #1206 lands as a merge commit of `06b5d4f2`, so both commits reach
    `main` through its second parent;
  - in `D`'s tree at that blob.

  The owner's decision names it "the MATH-CON-1 preregistration, accepted at `41a42cb9` (#1206)", and its
  confirmation review is #1206 comment 6721645433. `06b5d4f2` adds only the owner-authorized one-line label
  correction of 2026-11-08: line 758, where the R4 row label's first word becomes "review". The accepted blob was
  `27359cbd452a55ba26769b3b9d6fb518630f8898`, and control DS pins the corrected blob. The text still carries its
  drafting-time standing line. Its acceptance is recorded here.

  **The owner's authorization of the label correction** is recorded in #1206 comment 6722716262 (amaybaum,
  2026-11-08T14:28:45Z), the merge record for #1206. The record quotes the owner's chat words verbatim, and the
  authorization rests on those quoted words, not on the comment's posting account:

  > Yes, you have my authorization to make the one-word […] → `review` correction. [Elision ours; the full words are in #1206 comment 6722716262.]
  >
  > This was explicitly approved in my previous decision.
  >
  > The authorization includes creating a new commit, obtaining independent confirmation of the editorial-only change, requiring green exact-head CI, and performing a normal merge after checking compatibility with current `main`.
  >
  > Preserve the accepted `41a42cb9` commit in the ancestry. Verify green post-merge `main` CI.
  >
  > No additional design edits are authorized.

  The record states that #1206 merged as the normal merge commit `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`
  (parents `5ce4f98e…` and `06b5d4f2…`), and that post-merge `main` CI run 42489463543 was green.

  These parts of the design are inputs of this round, read from `D`: the definitions D1–D3, CT, the controls of its
  §5, the outcome partition of its §6 and the obligations of its §3.2.
- **The record directory.** The design's §10.1 has Stage 1B write `RESULT.md` "in this directory", and its §4 places
  amendments in `amendments/`. This round instead uses a sibling record directory: under `G13` a held round's record
  directory can never gain a file, so the design's directory stays open for the round that completes Stage 1B. The
  owner's ruling on this departure is recorded in #1206 comment 6722109292 (amaybaum, 2026-11-08T13:30:27Z), which
  quotes the owner's chat decision, "I approve the recommended path for all four decisions, with the existing
  scientific and execution safeguards preserved.", and records the ruling "Sibling directory | Approved. Use
  `round-mathcon1-s1b-1/` and record the explicit deviation from §10.1." This paragraph is that recorded deviation.

## The objects

- **`D`** = `fd539e150759a6ea51ab279aeeac80fc06050ade`, the head of `main` when the round pull request is cut. #1206
  landed before it as the merge commit `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`. Its push run is recorded in
  `evidence/d-push-run.json`.
- **`F`** is the commit carrying this file that the owner designates. `delta(D, F)` is this file and any amendments.
- **`E`** is the certified execution head, which the owner designates.
- **`Λ`** and **`Q`** are the last reconciliation and the receipt commit (§A.39 items 3–4).

**Drift from the design's snapshot to `D`, measured.** The design cites `main@45eea51d`. No path under
`verification/lean-mathlib/`, `verification/lean/`, `.github/` or `tools/` changed from
`45eea51d67237f2a41865dd7efc1ea97e2bc904f` to `13340732fe7e95466dd64faf3b8307fb386ad091`, or from there to
`b73acf38a7c60026b4b514cd9b5077e1419a9a1d`, or from there to `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`, the head of
`main` after #1206's merge. From there to `D`, no path under `verification/lean-mathlib/`, `verification/lean/` or
`tools/` changed, and the one changed path under `.github/` is `.github/workflows/verify.yml`: #1208 (ARP-1-MARC)
added the shard `probes_arp1marc` after `probes_foundations` and its four aggregate lines. The splice anchors below
are measured at `D`, after that change. Control S2 re-measures it at `D`.

**Branches (owner conditions 1 and 3).** The design branch and the proof dev branch are fixed by the following line.
It stands alone at column 0, is part of the round PR's first control-plane commit, and is byte-identical in every
commit of `D..F`. P reads each of those commits through git:

command-scan branches: design draft/mathcon1-s1b-1-skeleton; dev draft/mathcon1-s1b-1-dev

The design branch's pull request is recorded before `F` on the following line, which stands alone at column 0. It is
`PENDING` until that pull request is opened, and P refuses `PENDING` at `F`:

command-scan design pr: PENDING

At S1 and `E`, P checks all of these:
- `runs-to-f.json`'s `design_branch.name`, and `order.json`'s `design_branch.name` and `dev_branch.name`, equal the
  frozen names;
- every design-branch run has `event` `pull_request` and `head_branch` equal to the frozen design name;
- under the route `dump`, the dump run has `event` `pull_request` and `head_branch` equal to the frozen design name;
- **the design pull request is bound through the pulls API.** `GET /repos/{owner}/{repo}/pulls/<n>`, with `<n>` from
  the `design pr` line, captured with its digest, must show:
  - `head.ref` equal to the frozen design name;
  - `head.repo.full_name` equal to `amaybaum/incompleteness`;
  - `base.ref` equal to `main`.

  This holds whether the pull request is open or closed. The runs' `pull_requests` field is not used: the API
  documents it as listing pull requests open at query time, not the one that triggered the run, and it empties once
  the pull request closes;
- **the commit sets are defined as follows, and both are recorded with their heads as provenance (§A.42 item 8):**
  - the **design commits** are `rev-list <design head> ^D`, minus every commit in `D..F`;
  - the **dev commits** are `rev-list <dev head> ^F`.

  For each commit in either set, `GET …/actions/runs?head_sha=<sha>`, every page, shows only runs that have event
  `pull_request`, or that are entries of `approved_dispatches_to_f` or `approved_dispatches`, matched by `run_id`.
  This closes the case of a dispatch from another branch at the same commit. `D`'s own push run on `main` and the
  `F` attestation lie outside these sets, or are exempt as approved entries, so neither trips the rule. The rule
  rests on the host answers, whose digests are recorded.

The anchors of the shared-file splices, measured at `D`:
- the last import line of `OIBridge.lean` (blob `4a640e9029d3b4c9b393ef168500dc05c023f788`):
  `import OIBridge.PC1Controls` (`:286`);
- the last census family of `verification/lean-manuscript-census.json` (blob
  `03c4f773040c8db7fbc3f08df763d722e368837f`), the 122nd of 122: "SUBSTATE-1 pure-gradient gauge link negative
  control and two-slice inverse" (modules `["GradientLinkFlatness"]`);
- the bridge job's last step in `.github/workflows/verify.yml` (blob `3a9dc8a97fd6f9d6d5f17cf390b5aabf37d65233`):
  "KTRANS-SEP-2 marker complete reports with an axiom outside the three" (`:200`);
- the shard the new shard follows: `probes_arp1marc` (`:713`), the job directly before `probes:` (`:750`);
- the aggregate lines: the `probes_arp1marc` entry at the end of `needs` (`:752`), the `ARP1MARC_RESULT` line in
  `env` (`:781`), its `echo` line (`:806`) and its `test` line (`:834`).

## Scope: what this stage decides, and what it does not

The stage executes only the design's obligations O-1, O-2, O-3a, O-3b, O-3c, O-3d and O-3e (§3.2). It does not
execute O-4 to O-10. It does not run the circularity test CT (O-8). It does not run controls CC-0, CC-1(b), CC-2 and
CC-4. It does not score T1, T3 or T5, and it does not evaluate the design's §6 partition. That partition is
evaluated by the round that completes Stage 1B.

| design item | what this stage supplies | standing after a positive stage |
| --- | --- | --- |
| O-1, "for the system carrier and for every level" | `baseline_level_no_coherentNonMonomial` (every level `n`) and the `S = Fin 2` instance of `baseline_no_coherentNonMonomial`. The general-carrier `monomial_of_coherentBranch` is the means, not an extra obligation | kernel |
| CC-3(a) (no D2 operation in the baseline, every level) | O-1 | passed |
| CC-1(a) (`K*` available in the fiat class) | `fiatC_conjugatedAttempt_available`, O-2's transfer clause applied to O-3e's instrument | passed |
| CC-3(b), the design's definitional calibration of D3 on `drivePhase` (distinct from CC-0, the calibration the owner's item 2 concerns) | CAL in the exact layer, a control of O-3e's D3 check | recorded |
| restricted shortcut, Q2 = no (§4.4 Step 2) | its two inputs, O-1 and O-2 | inputs present; CT not run |
| FC for the object (`PolC ⊆ 𝓕`) | O-2 | input present; CT not run |
| T2 (D3 at the support standard) | O-3e | met for the witness `H·drivePhase·H` |
| T4, finite-depth form | O-3e depth form | availability at every finite depth only; spectator form (O-9) not run |
| CC-0, CC-1(b), CC-2, CC-4, T1, T3, T5, the §6 outcome | nothing | not established |

## The frozen surface (module `OIBridge/PolarizedProtocol.lean`)

The module:
- imports exactly `OIBridge.PolarizationClosure`, `OIBridge.BridgeFiniteProtocol` and
  `OIBridge.PreservationInductionInstances` (an import closure of 93 `OIBridge` modules at `main@b73acf38`);
- opens the namespaces `OIBridge` and `OIBridge.PolarizedProtocol` and closes them at the end of the file;
- carries one `open` line (PENDING; fixed by the statement-elaboration design run).

Everything below is frozen in full: every definition and inductive body, every theorem statement (name, binders,
hypotheses, conclusion), the order of the declarations, and the `#print axioms` list. The theorem proofs are written
after `F`.

Before `F` the design run may correct the text so that it elaborates, under three restrictions:
- an implicit argument, a coercion, a `noncomputable` marker or a qualified name may change;
- no hypothesis may be added or removed;
- no conclusion may be changed.

Each correction is recorded on the pull request as its own control-plane commit, which changes only the frozen
surface's text. Its commit message carries a before/after unified diff of the affected declaration and names the
restriction it falls under. A reviewer confirms, against that diff, that no hypothesis or conclusion changed, before
`F` is requested.

```lean
-- §A the design's predicates: D2 (§4.2) and D3's non-Clifford clause (§4.3)
def CoherentNonMonomialBranch {S O : Type} [Fintype S] [DecidableEq S] [Fintype O] [DecidableEq O]
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (U : Matrix S S ℂ) : Prop :=
  ∃ (o : O) (p : ℝ), 0 < p ∧ p ≤ 1 ∧ F o = (p : ℂ) • conjChannel U ∧ Uᴴ * U = 1 ∧ ¬ IsMonomial U

def pauliX : Matrix (Fin 2) (Fin 2) ℂ := !![0, 1; 1, 0]
def pauliY : Matrix (Fin 2) (Fin 2) ℂ := !![0, -Complex.I; Complex.I, 0]
def pauliZ : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, -1]

def NonClifford (U : Matrix (Fin 2) (Fin 2) ℂ) : Prop :=
  ∃ P ∈ ({pauliX, pauliZ} : Set (Matrix (Fin 2) (Fin 2) ℂ)),
    ∀ (c : ℂ), ∀ Q ∈ ({1, pauliX, pauliY, pauliZ} : Set (Matrix (Fin 2) (Fin 2) ℂ)), U * P * Uᴴ ≠ c • Q

-- §B O-1
theorem monomial_of_coherentBranch {S O : Type} [Fintype S] [DecidableEq S] [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hF : InstAvail substratumClass S O F)
    {o : O} {p : ℝ} (hp : 0 < p) {U : Matrix S S ℂ} (hU : Uᴴ * U = 1)
    (hb : F o = (p : ℂ) • conjChannel U) : IsMonomial U
theorem baseline_no_coherentNonMonomial {S O : Type} [Fintype S] [DecidableEq S] [Fintype O] [DecidableEq O]
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (U : Matrix S S ℂ) :
    InstAvail substratumClass S O F → ¬ CoherentNonMonomialBranch F U
theorem baseline_level_no_coherentNonMonomial (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)
    (U : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) :
    (substratumTheory (Fin 2)).availExt n F → ¬ CoherentNonMonomialBranch F U

-- §C O-2: the least label-invariant architecture over the monomial class and a family G; the fiat class 𝓕 of CC-1
inductive MonoExt (G : ∀ (T : Type) [Fintype T] [DecidableEq T], Set (Matrix T T ℂ)) :
    ∀ (T : Type) [Fintype T] [DecidableEq T], Matrix T T ℂ → Prop
  | base {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : IsMonomial K) : MonoExt G T K
  | gen {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : K ∈ G T) : MonoExt G T K
  | mul {T : Type} [Fintype T] [DecidableEq T] (K L : Matrix T T ℂ) :
      MonoExt G T K → MonoExt G T L → MonoExt G T (K * L)
  | smul {T : Type} [Fintype T] [DecidableEq T] (a : ℂ) (K : Matrix T T ℂ) (ha : ‖a‖ ≤ 1) :
      MonoExt G T K → MonoExt G T (a • K)
  | proj {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (k : Fin m) :
      MonoExt G (T × Fin m) (Matrix.diagonal fun r => if r.2 = k then 1 else 0)
  | block {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (K : Matrix (T × Fin m) (T × Fin m) ℂ)
      (f e : Fin m) : MonoExt G (T × Fin m) K → MonoExt G T (ancBlock K f e)
  | relabel {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : T ≃ T')
      (K : Matrix T T ℂ) : MonoExt G T K → MonoExt G T' (Matrix.reindex e e K)

inductive FiatC : ∀ (T : Type) [Fintype T] [DecidableEq T], Matrix T T ℂ → Prop
  | base {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : IsMonomial K) : FiatC T K
  | swap (n : ℕ) : FiatC (Fin 2 × Fin n) (siteSwapImage n)
  | mul {T : Type} [Fintype T] [DecidableEq T] (K L : Matrix T T ℂ) :
      FiatC T K → FiatC T L → FiatC T (K * L)
  | smul {T : Type} [Fintype T] [DecidableEq T] (a : ℂ) (K : Matrix T T ℂ) (ha : ‖a‖ ≤ 1) :
      FiatC T K → FiatC T (a • K)
  | proj {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (k : Fin m) :
      FiatC (T × Fin m) (Matrix.diagonal fun r => if r.2 = k then 1 else 0)
  | block {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (K : Matrix (T × Fin m) (T × Fin m) ℂ)
      (f e : Fin m) : FiatC (T × Fin m) K → FiatC T (ancBlock K f e)
  | relabel {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : T ≃ T')
      (K : Matrix T T ℂ) : FiatC T K → FiatC T' (Matrix.reindex e e K)

theorem monoExt_le_substratumClass (G : ∀ (T : Type) [Fintype T] [DecidableEq T], Set (Matrix T T ℂ))
    (hG : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), K ∈ G T → IsMonomial K) :
    ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), MonoExt G T K → substratumClass T K
theorem fiatC_arch : Architecture FiatC
theorem fiatC_labelInvariant : LabelInvariant FiatC
theorem polC_le_fiatC : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), PolC T K → FiatC T K
theorem polGen_le_fiatC : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), PolGen T K → FiatC T K
theorem instAvail_polC_fiatC {S O : Type} [Fintype S] [DecidableEq S] [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} : InstAvail PolC S O F → InstAvail FiatC S O F

-- §D O-3a–c: B23's primitives in PolC. Work = Token × Fin 4; the ancilla register value a encodes two bits.
def ancSign (a b : Fin 4) : ℂ :=
  if (a.val / 2 * (b.val / 2) + a.val % 2 * (b.val % 2)) % 2 = 1 then -1 else 1
/-- `H ⊗ H` on the ancilla register of `Work`, the identity on the token. -/
noncomputable def ancillaHH : Matrix Work Work ℂ := fun r c =>
  if r.1 = c.1 then (1 / 2 : ℂ) * ancSign r.2 c.2 else 0
/-- The Toffoli permutation with the token as target, controlled on ancilla register value `3`. -/
def toffoliToken : Matrix Work Work ℂ := fun r c =>
  if r.2 = c.2 ∧ (if c.2 = 3 then r.1 ≠ c.1 else r.1 = c.1) then 1 else 0

theorem balancedCircuit_eq_word :
    balancedCircuit = ancillaHH * toffoliToken * siteShearImage 4 * toffoliToken * ancillaHH
theorem polC_balancedCircuit : PolC Work balancedCircuit
theorem polC_resetPerm (j : Fin 4) : PolC Work (resetPerm j)
theorem polC_correction (j : Fin 4) : PolC Work (correction j)

-- §E O-3d: B23 in polarizedTheoryC (Fin 2)
theorem polarized_attempt_available : InstAvail PolC Token (Fin 4) (attempt balancedCircuit)
theorem polarized_finite_available (k : ℕ) :
    InstAvail PolC Token Unit
      (fun _ => (1 - (3 / 8 : ℂ) ^ k) • conjChannel drivePhase + (3 / 8 : ℂ) ^ k • LinearMap.id)

-- §F O-3e: system-level H, the conjugated instrument, its D2 and D3 checks, availability at every finite depth
noncomputable def hdh : Matrix (Fin 2) (Fin 2) ℂ := hadamard * drivePhase * hadamard
noncomputable def conjugatedAttempt (j : Fin 4) : Matrix Token Token ℂ →ₗ[ℂ] Matrix Token Token ℂ :=
  (conjChannel hadamard).comp ((attempt balancedCircuit j).comp (conjChannel hadamard))

theorem polC_hadamard : PolC (Fin 2) hadamard
theorem conjugatedAttempt_available : InstAvail PolC Token (Fin 4) conjugatedAttempt
theorem conjugatedAttempt_branch : conjugatedAttempt 0 = ((5 / 8 : ℝ) : ℂ) • conjChannel hdh
theorem hdh_unitary : hdhᴴ * hdh = 1
theorem hdh_not_monomial : ¬ IsMonomial hdh
theorem hdh_nonClifford : NonClifford hdh
theorem polarized_coherentNonMonomial : CoherentNonMonomialBranch conjugatedAttempt hdh
theorem conjugated_finite_available (k : ℕ) :
    InstAvail PolC Token Unit
      (fun _ => (1 - (3 / 8 : ℂ) ^ k) • conjChannel hdh + (3 / 8 : ℂ) ^ k • LinearMap.id)

-- §F2 O-2's transfer clause applied to O-3e's instrument (the design's CC-1(a))
theorem fiatC_conjugatedAttempt_available : InstAvail FiatC Token (Fin 4) conjugatedAttempt

-- §G kernel countercontrols (controls of O-2 and O-3a; not obligations)
theorem fiatC_not_le_substratumClass :
    ¬ ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), FiatC T K → substratumClass T K
theorem word_without_shear_ne : ancillaHH * toffoliToken * toffoliToken * ancillaHH ≠ balancedCircuit
```

`polarized_coherentNonMonomial`, together with O-1, already shows that O-1's class hypothesis is load-bearing: an
`InstAvail PolC` family has a coherent non-monomial branch. No separate theorem restates it.

**`#print axioms` lines (control S5).** There are twenty-six, at the end of the module, in this order, each prefixed
`OIBridge.PolarizedProtocol.`:
- `monomial_of_coherentBranch`, `baseline_no_coherentNonMonomial`, `baseline_level_no_coherentNonMonomial`;
- `monoExt_le_substratumClass`, `fiatC_arch`, `fiatC_labelInvariant`, `polC_le_fiatC`, `polGen_le_fiatC`,
  `instAvail_polC_fiatC`;
- `balancedCircuit_eq_word`, `polC_balancedCircuit`, `polC_resetPerm`, `polC_correction`;
- `polarized_attempt_available`, `polarized_finite_available`;
- `polC_hadamard`, `conjugatedAttempt_available`, `conjugatedAttempt_branch`, `hdh_unitary`, `hdh_not_monomial`,
  `hdh_nonClifford`, `polarized_coherentNonMonomial`, `conjugated_finite_available`;
- `fiatC_conjugatedAttempt_available`;
- `fiatC_not_le_substratumClass`, `word_without_shear_ne`.

None of these short names occurs in a `#print axioms` line at `D` (control S2 measures this).

**Cells.**

| cell | theorems |
| --- | --- |
| O-1 | §B |
| O-2 | §C and §F2 |
| O-3a | `balancedCircuit_eq_word`, `polC_balancedCircuit` |
| O-3b | `polC_resetPerm` |
| O-3c | `polC_correction` |
| O-3d | §E |
| O-3e | §F |
| KC | §G |

**Import line:** `import OIBridge.PolarizedProtocol`, directly after the last import line at `D`.

**Census family**, directly after the last family at `D`, in `D`'s two-space JSON layout:
- **name:** "MATH-CON-1 Stage 1B first stage: monomial baseline (O-1), fiat inclusion (O-2), B23's protocol in PolC
  and its Hadamard-conjugated branch (O-3a–e) (round MATH-CON-1-S1B-1, reconstruction)";
- **modules:** `["PolarizedProtocol"]`;
- **status:** `kernel-only`;
- **manuscript:** `[]`;
- **note:** "Hadamard enters as the polarization map's supplied swap image (PolC.swap); the map's status is
  proposed; no circularity-test verdict, no claim that OI generates the operation."

## Auxiliary declarations and options (frozen policy)

The module may contain declarations outside the frozen surface only in this form:
- `private theorem aux_<name>`, of theorem kind, with an optional docstring.

The following are refused at command level (control N1):
- any other new declaration, whether `def`, `abbrev`, `instance`, `inductive`, `structure`, `lemma`, `example`,
  notation, macro or a non-private theorem;
- any attribute on any declaration, `@[simp]` included;
- any `variable`, `section`, `namespace`, `open` or `universe` command beyond the frozen ones.

**Permitted scoped forms (one rule; N1 and N3 implement it, and the self-test drives both).**
- **At command level**, the only form is `set_option maxHeartbeats <n> in` (`n ≤ 4000000`) or
  `set_option maxRecDepth <n> in` (`n ≤ 8192`), on its own column-0 line directly before a frozen or `aux_` theorem
  line. N3's placement rule governs these command-level forms only. Any other command-level `set_option` fails N3.
  That covers another option, a larger bound, a global form, and a form before a `def` or `inductive`.
- **Inside a proof span**, exactly two forms are permitted, each binding only the term or tactic that follows:
  - `open [scoped] <ident> {<ident>} in`;
  - `set_option (maxHeartbeats|maxRecDepth) <n> in`, within the same bounds.

  For example, `open scoped ComplexOrder in` is permitted. Any other occurrence of `open` or `set_option` in a proof
  span is a scan hit (below). That includes a bare `open Foo`, `open Foo hiding x in`, `open Foo (x) in`, and a
  `set_option` with another option or a larger bound.

**Column-0 rule (formatting constraint, enforced by N1).** Every line of a proof, of a statement's continuation, of
an inductive's constructors and of a docstring's continuation is indented. N1 walks the module's non-blank column-0
lines in order. Each must be one of these two kinds:
- **(a) the next column-0 line of the frozen skeleton**, matched exactly. These are the header comment, the imports,
  the `namespace`, `open` and `end` lines, every frozen `def`, `noncomputable def`, `inductive` and `theorem` line,
  their `/--` docstring lines, frozen `--` comments, and the `#print axioms` lines;
- **(b) an auxiliary line**, which is one of:
  - `private theorem aux_<identifier>`, followed by its statement;
  - a single-line `/-- … -/` docstring directly before such a line;
  - a command-level `set_option` of the permitted form;
  - a `--` comment line.

Any other non-blank column-0 line fails N1, wherever it lies. A `--` comment at column 0 that is not a frozen comment
passes N1, but it ends the declaration before it, so it fails N2.

**Command scan of proof spans (also N1).** Lean 4 commands are not tied to column 0. A command may start indented, or
on the same line after a proof (`… := by simp instance : …`), and still parse as a new top-level command. N1 therefore
lexes each elided span, meaning every frozen theorem's proof and every `aux_` theorem's proof, and fails on any token
in the scan list, apart from the tokens of a permitted in-proof form.

*The route line.* Exactly one line of this file, standing alone at column 0, fixes the command-scan route. At `F` it
reads exactly `command-scan route: dump` or exactly `command-scan route: floor-only (completeness unverified)`.
`controls.py` reads that line from the preregistration's blob at `F`. Control P fails if the line is missing, appears
twice, reads anything else (`PENDING` included), or disagrees with a route-dependent site. There are seven
route-dependent sites:
1. the scan list, with scan list (i), its reference-set line, its condition and the dump-run line;
2. the result note's rule for the dump's parser count, with its caveat sentence;
3. precondition 2's dump-step and script paragraph;
4. precondition 3's dump pins;
5. P's list of files pinned at `F`;
6. the dump-consistency self-test cases;
7. the §A.41 command-scan row.

**Site lines.** Each site is marked by one dedicated site line, standing alone at column 0. Sites 1–6 have it directly
before their text. Site 7 has it directly after the §A.41 table. A site line reads exactly
`command-scan site: <route>`, where `<route>` is the route word on the route line, `dump` or `floor-only`. Rule prose
names site lines only inside backticks, never at column 0. P checks agreement by counting site lines and nothing else:
- the file holds exactly seven site lines, and each names the route on the route line;
- under `dump`, the reference-set line and the `command-scan dump run` line each occur exactly once;
- under `floor-only`, neither of those two lines occurs.

The line:

command-scan route: PENDING

*Drafting note (deleted in the last pre-`F` commit; control P fails at `F` if any line beginning "*Drafting note"
remains).* The text below is written for the route `dump`. If the design run's dump fails the reference-set condition
(precondition 2), the last pre-`F` commit sets the route line to `floor-only (completeness unverified)`. At each of the
seven sites it replaces the site line with `command-scan site: floor-only` and the site's text as follows:
1. **The scan list.** Replace it with "*The scan list.* The list is the floor (ii) below." This deletes scan list
   (i), the reference-set condition, the reference-set line and the `command-scan dump run` line. The `dump` entry of
   `evidence/order.json` is then `null`.
2. **The result note.** Replace the parser-count rule and its caveat with: "The control table carries this frozen
   sentence: 'The command scan uses the frozen floor only; its completeness is unverified.'"
3. **Precondition 2.** Replace the dump-step and script paragraph with: "The command-table dump was not admitted: <the
   dump was not produced | the reference-set condition failed>. The design run's id, and a round-branch commit
   carrying the reference-set line, are recorded on the pull request as provenance only."
4. **Precondition 3.** Replace the dump pins with: "- under `floor-only`, no dump pin is required."
5. **P's pinned files.** Replace the list with: "the files pinned at `F` (`evidence/d-push-run.json` and the design-run
   evidence) and `evidence/f-run/results.json`", keeping the rest of that bullet.
6. **Self-test.** Replace the dump-consistency cases with: "N1 scans with the floor alone, and the control table
   carries the floor-only sentence."
7. **The §A.41 row.** Rewrite the row's command-scan entry to name the floor only, and state that its completeness is
   unverified.

command-scan site: dump

*The scan list.* Under the route `dump`, the list is the union of two sets:
- **(i) the environment's command table.** This is the set of leading tokens of the `command` syntax category, in the
  environment of the module's three imports, together with its frozen `namespace` and `open` lines, under the pinned
  toolchain at `D`.
  - **How it is produced.** The statement-elaboration design run dumps it before `F` (*Preconditions of `F`*), and
    the dump is added at S1 as `evidence/command-tokens.json`.
  - **Its schema.** `schema` = `"mathcon1-s1b1-command-tokens"`, `version` = `1`, `toolchain`, `mathlib_rev`, the three `imports`,
    `leading_tokens` (sorted strings), `non_indexed_leading_parsers` (an integer), and `command_kinds` (sorted
    syntax-node kinds). It has no timestamp field.
  - **How it is pinned.** Its sha256 is pinned at `F`. `controls.py` embeds the same token list, and control P
    checks that the file, its pin and the embedded list agree.
  - **The reference-set condition (non-vacuity).** The route `dump` is admissible only when every token of a frozen
    reference set appears **verbatim** in `leading_tokens`: as the literal token text, unescaped, not as `«…»`. The
    environment certainly defines each of these:
    - Lean core: the first thirteen tokens;
    - Batteries: `alias`;
    - Mathlib: `lemma`, `notation3`, `irreducible_def`.

    The set is the following single line, standing alone at column 0:

command-scan reference set: theorem def instance @[ #eval open set_option namespace end variable section private /-- alias lemma notation3 irreducible_def

    If any reference token is absent, the dump is defective and the route is `floor-only`. Absence is not explained
    away. Control P checks this condition against the pinned file at S1 and `E`.

    **The reference set is fixed before the dump is seen, and this is checkable (P).**
    1. The reference-set line is in the round PR's first control-plane commit, which is the oldest commit of
       `rev-list F ^D`. It is byte-identical in every commit of `D..F`, and P reads each through git.
    2. Before `F`, the preregistration records one line, with five fields:

       `command-scan dump run: <run id> on design commit <40-hex> at round-branch commit <40-hex>; toolchain <pin>;
       mathlib <40-hex>; dump sha256 <64-hex>`

       It names:
       - the design run (an ordinary `pull_request` run; nothing is dispatched) that produced the dump;
       - the design-branch commit the dump ran on, that run's `head_sha`;
       - a round-branch commit, which P checks lies in `D..F` and carries the reference-set line;
       - the toolchain pin;
       - the resolved Mathlib commit. The lakefile pins Mathlib only by the tag `v4.33.0`, and no
         `lake-manifest.json` is committed, so the exact command environment needs both Lean and Mathlib;
       - the dump file's sha256.

       By item 3, the round-branch commit's first host run, a `pull_request` run, was created before the dump run.
       Nothing else is claimed about that commit.

       P checks that the provenance items agree with their other sources:
       - **toolchain.** The line's `<pin>` equals the content of `verification/lean-mathlib/lean-toolchain` at `D`,
         which is `leanprover/lean4:v4.33.0`. The normalized version, that content with the prefix
         `leanprover/lean4:v` removed (`4.33.0`), equals the dump file's `toolchain` field, which is
         `Lean.versionString`, exactly and as strings. A mismatch means the dump is not admitted before `F`
         (route `floor-only`); at S1 or `E` it fails P;
       - **Mathlib.** The line's `mathlib` field equals the dump file's `mathlib_rev` field, which is 40 hex. The
         design PR records that it is the commit the tag `v4.33.0` resolves to, as provenance;
       - the sha256 equals the pin and the file at S1 and `E`;
       - the design commit equals `dump.design_commit` in `evidence/order.json`, read from the captured runs answer;
       - the design commit is not an ancestor of `F`, so the design branch never entered the round branch.
    3. The `dump` entry of `evidence/order.json` shows by host timestamps that the named round commit's first host run
       precedes the dump run.
    4. The same entry also shows that **every** run of the design branch was created after the first host run of the
       round PR's first control-plane commit. So no design-branch run, and therefore no dump, existed before the
       reference set was published.

command-scan dump run: PENDING
  - **Why it is complete.** The module cannot add command syntax of its own, because `syntax`, `macro`, `notation`
    and `elab` are themselves in the table and so are refused. The list is therefore complete for every command that
    begins with an indexed token in that environment.
- **(ii) a hand-written floor.** These are always included, whatever the dump contains:
  - `instance`, `attribute`, `@[`, `/--`, `/-!`, `lemma`, `theorem`, `def`, `abbrev`, `example`, `structure`, `class`,
    `inductive`, `axiom`, `opaque`;
  - `alias`, `irreducible_def`, `notation`, `notation3`, `infix`, `infixl`, `infixr`, `prefix`, `postfix`, `macro`,
    `macro_rules`, `syntax`, `elab`, `elab_rules`, `declare_syntax_cat`, `binder_predicate`;
  - `simproc`, `dsimproc`, `unif_hint`, `add_decl_doc`, `run_cmd`, `run_elab`, `run_meta`;
  - `open`, `set_option`, `local`, `scoped`, `variable`, `universe`, `mutual`, `include`, `omit`, `section`,
    `namespace`, `end`, `export`, `initialize`, `private`, `protected`, `noncomputable`, `deriving`;
  - `assert_not_exists`, `suppress_compilation`, `#eval`, `#print`, `#check`, `#reduce`, `#synth`, `#exit`, `#guard`,
    `#lint`, `#help`.

  A bare `#` is not listed, because Mathlib's `#s` card notation can occur in a proof.

**The completeness caveat (route `dump`).** If the dump records `non_indexed_leading_parsers > 0`, some command
parsers in that environment are not indexed by a first token. For those, the scan list's completeness is
**unverified**, and the result note's control table says so. The floor (ii) still applies.

**The lexing rule.** A hit is a Lean token whose text equals a scan-list entry, compared case-sensitively. The span is
lexed as follows:
- Line comments run from `--` to the end of the line.
- Block comments `/- … -/` nest to any depth, and their content is skipped. A `/--` or `/-!` opener is instead itself
  a token, and a scan hit.
- String literals are skipped, with escapes. So are interpolated strings (`s!"…"`, `m!"…"`, `f!"…"`) and raw strings
  (`r"…"`, `r#"…"#`, any number of `#`).
- **Identifier characters** are Lean's own classes, from `src/Init/Meta/Defs.lean` at tag `v4.33.0`. That tag is
  the toolchain `verification/lean-mathlib/lean-toolchain` pins at `D` (`leanprover/lean4:v4.33.0`), and S2 checks
  the pin. The ranges are transcribed verbatim, as range tables, into `controls.py`:
  - `isLetterLike`:
    - `0x3B1–0x3C9` except `0x3BB` (lower Greek except λ);
    - `0x391–0x3A9` except `0x3A0` and `0x3A3` (upper Greek except Π and Σ);
    - `0x3CA–0x3FB` (Coptic);
    - `0x1F00–0x1FFE` (Greek Extended);
    - `0x2100–0x214F` (Letterlike Symbols);
    - `0x1D49C–0x1D59F` (Mathematical Alphanumeric Symbols);
    - `0x00C0–0x00FF` except `0x00D7` (×) and `0x00F7` (÷) (Latin-1 Supplement letters);
    - `0x0100–0x017F` (Latin Extended-A).
  - `isSubScriptAlnum`: `0x2080–0x2089`, `0x2090–0x209C`, `0x1D62–0x1D6A`, and `0x2C7C`.
  - `isIdFirst`: an ASCII letter (`Char.isAlpha`), `_`, or `isLetterLike`.
  - `isIdRest`: `isIdFirst`, an ASCII digit (`Char.isAlphanum`), `'`, `!`, `?`, or `isSubScriptAlnum`.

  So `𝓘`, `ℂ`, `α`, `é` and `ŝ` are identifier characters.
- **Char literals.** A `'` that directly follows an identifier character is part of that identifier, as in `h'` and
  `h𝓘'`. Otherwise, a `'` starts a char literal only when a **complete** char literal follows by the exact grammar:
  - `'`, then either one character other than `\`, `'` and a newline, or one escape (`\\`, `\'`, `\"`, `\n`, `\t`,
    `\r`, `\xHH`, `\uHHHH`), then `'`.

  A complete char literal is skipped. A `'` that does not begin one is an ordinary token and skips nothing.
- An identifier is one token. That covers dotted names and `«…»`-escaped parts, so `infer_instance`,
  `ImplementationClass`, `Foo.instance` and `«instance»` never match.
- `#` followed by identifier characters is one token. `@[` is one token.
- Every symbolic scan-list entry is matched literally at a token start.

The scan over-approximates: a false hit can only fail the module, never admit one. N1 runs locally in
`check S1` before any dispatch. A false hit costs a rewrite of the proof, which a repair may do, never a halt.

Auxiliary theorems:
- obey N3's hygiene;
- carry no `#print axioms` line of their own;
- are covered through the frozen theorems' axiom closure, which `#print axioms` reports transitively.

**Proof elision (control N2).** The skeleton the module is compared with is built as follows:
1. Delete every `aux_` theorem, with its docstring and any `set_option … in` prefix.
2. Delete every allowed `set_option … in` prefix of a frozen theorem.
3. For each frozen `theorem`, replace the text from the `:=` that ends its statement to the end of the declaration
   with `:= _`. A declaration ends at the next **non-blank line that starts at column 0, whatever it contains**, or
   at the end of the file. Nothing at column 0 can therefore hide inside an elided proof.
4. Strip trailing whitespace from each line and collapse each run of blank lines to one.

Everything else must equal the frozen skeleton byte for byte. That includes:
- the module header comment;
- the imports, the `namespace`, `open` and `end` lines;
- every docstring and comment outside a proof;
- every `def`, `noncomputable def` and `inductive` in full;
- the `#print axioms` lines.

## The exact layer (`verification/lean/mathcon1_s1b1_check.py`, frozen blob PENDING)

The checker:
- imports only `fractions`, `itertools` and `sys`;
- opens no file and reads no environment variable;
- does not use `__import__`, `importlib`, `exec` or `eval` (static control B checks all of this);
- computes in `ℚ(i)`.

It reconstructs, from their mathematical definitions:
- `drivePhase`, `balancedCircuit` (with `v`), `resetPerm`, `correction` and `siteShearImage 4`;
- the module's `ancillaHH` and `toffoliToken`;
- the scaled Hadamard `H₂ = √2·H`.

It uses `H·M·H = ½·H₂·M·H₂`, so every quantity it checks is rational in `ℚ(i)`.

Checks:
- **X1** the O-3a word equals `balancedCircuit` entrywise;
- **X2** `hdh` is unitary, has two nonzero entries in one row, and meets the non-Clifford clause for some `P` in
  `{X, Z}`, by exact comparison with `c·Q` for `Q` in `{I, X, Y, Z}`;
- **X3** the conjugated attempt, computed on all four matrix units from reset, circuit, readout, correction and discard,
  has outcome-0 branch `(5/8)·Ad(hdh)` and other outcomes `(1/8)·id`;
- **X4** the stopped channel of the conjugated attempt at depths 0–8, on all four matrix units, equals
  `(1 − (3/8)^k)·Ad(hdh) + (3/8)^k·id`. These are controls of the kernel's availability statements at finite depth,
  not a theorem about every depth;
- **CAL** `drivePhase` passes the non-Clifford clause. Its rejection by D2's monomial clause is XC3.

The checks print as twelve lines, in this order: X1, X2a (unitary), X2b (non-monomial), X2c (non-Clifford), X3a
(outcome 0), X3b (outcomes 1–3), X4, CAL, XC1, XC2, XC3, XC4.

Countercontrols, each of which must fail as stated:
- **XC1** the word with `siteShearImage 4` replaced by the identity differs from `balancedCircuit`;
- **XC2** `H` and `H·S·H` are rejected by the non-Clifford clause;
- **XC3** `drivePhase` is rejected by the monomial clause;
- **XC4** the branch with the correction removed differs from `(5/8)·Ad(hdh)`.

**Exit statuses (structured evidence).** The checker prints one line per check and countercontrol, and then one
summary line, `checks: 8, failures: <m>; countercontrols: 4, not-failing: <c>`. The eight checks are X1, X2a–c, X3a–b,
X4 and CAL; the four countercontrols are XC1–XC4. It exits as follows:

| exit status | meaning | route |
| --- | --- | --- |
| 0 | `m = 0` and `c = 0` | exact positive |
| 3 | `m > 0` and `c = 0` | exact negative (`MATHCON1-EXACT-NOT-ESTABLISHED`) |
| 4 | `c > 0`, whatever `m` is | a countercontrol did not fail as stated: control X failed; no exact token; control-failure halt |

It catches no exception, so a crash exits 1. `controls.py` runs the checker itself and reads its exit status and
captured output, never a CI log. The run is **complete** only when all of these hold:
- the exit status is 0, 3 or 4;
- the summary line is present and reports 8 checks and 4 countercontrols;
- the reported `m` and `c` agree with the exit status.

Anything else is VOID, so `verdict` prints no token. At `E`, every exact-layer outcome other than exit 0 halts the
round under *Stop rule*: exit 3, exit 4, a crash, and a missing, cut or inconsistent summary. No checker rerun path is
pre-registered.

**Pre-`F` exercise of every code path (fixtures).** Before `F`, the checker's functions are run only on objects whose
results are already proved on `main`, or on synthetic matrices. Nothing from O-3a–e is computed. Each fixture is
recorded with its expected result, and the self-test replays it:
- **the X3/X4 path** (reset, uniform attach, circuit, readout, correction, discard, stopped loop) on B23's
  **unconjugated** attempt: outcome 0 equals `(5/8)·Ad(drivePhase)` and outcomes 1–3 equal `(1/8)·id`, as
  `attempt_balanced_branch` (BFP:194) states; the stopped channel at depths 0–8 equals
  `(1 − (3/8)^k)·Ad(drivePhase) + (3/8)^k·id`, as `balanced_stopped_formula` (BFP:245) states;
- **the X1 path** (8×8 products on `Work`) on `ancillaHH · ancillaHH = 1`, an identity that is not O-3a's;
- **the X2 and CAL paths** (unitarity, monomiality, non-Clifford test) on synthetic matrices: the rational rotation
  `[[3/5, −4/5], [4/5, 3/5]]`, `H₂/2`-scaled Cliffords, and monomial phases;
- **the exit-status logic** on injected results giving each of exits 0, 3 and 4.

The checker's first computation on O-3a–e's objects (the O-3a word, `hdh`, the conjugated attempt) is in execution,
through code paths that the fixtures have already exercised.

**Source-text control XS.** At the commit under check, XS compares the texts of the definitions the checker
reconstructs, and of everything X3 and X4 compute through, with their frozen texts at `D`:
- `drivePhase`, `balancedCircuit`, `v`, `resetEquiv`, `resetPerm`, `resetChannel`, `correction`,
  `correctedReadout`, `attempt`;
- `InterventionLocality.readProj`, `uniformAttach`, `discardWith`, `ptraceAncL`, `ptraceAnc`, `conjChannel`,
  `stopped`;
- `hadamard`, `hc`, `siteShearImage`, `siteSwapImage`.

The file and line of each, measured at `D`, under `verification/lean-mathlib/OIBridge/`:
- `BridgeFiniteProtocol.lean`: `stopped` `:34`, `resetEquiv` `:103`, `resetPerm` `:106`, `resetChannel` `:108`,
  `v` `:151`, `balancedCircuit` `:153`, `drivePhase` `:167`, `correction` `:170`, `correctedReadout` `:182`,
  `attempt` `:188`;
- `ImplementationLocality.lean`: `InterventionLocality.readProj` `:256`;
- `OperationalAssembly.lean`: `ptraceAnc` `:453`, `ptraceAncL` `:480`, `uniformAttach` `:492`, `discardWith` `:515`;
- `MonoidalCompletion.lean`: `conjChannel` `:360`;
- `C5Discovery.lean`: `hc` `:134`, `hadamard` `:156`, `siteShearImage` `:192`, `siteSwapImage` `:196`.

XS also compares the module's `ancSign`, `ancillaHH`,
`toffoliToken`, `hdh` and `conjugatedAttempt` with the frozen surface. A frozen correspondence table ties each
checker function to the Lean definition it reconstructs.

## The decision rules (frozen; implemented by `controls.py verdict`)

Every fact the verdict reads about a CI run comes from the host's structured records (§A.44):
- `RUN` is the runs API answer for the exact-head run at `E`;
- `JOBS` is the jobs API answer (`?per_page=100`).

`controls.py verdict E --freeze F --run-api RUN --jobs-api JOBS` works in this order:
1. It derives the run result with the frozen recipe `derive-run`.
2. It runs every control of `check E --freeze F`.
3. It prints tokens only from complete evidence.

Otherwise it prints `VERDICT  VOID` with the reason, prints no token, and exits 1. VOID is not an outcome, and no
retake path is pre-registered. A VOID that arises from the checker or the controls halts the round (*Stop rule*). A
VOID that arises from the host may be retaken only as *Stop rule* allows: a cancelled run, missing jobs, or a runner
failure.

**The run.** It is the completed `workflow_dispatch` run of `.github/workflows/verify.yml` in
`amaybaum/incompleteness`, with these properties:
- the head repository is the same;
- it is at `E`'s full commit;
- its run id, attempt and bridge job id are positive integers;
- every job carries the run's id, attempt and commit.

A pull-request run, a push run, and a run of another repository or workflow path are not the run.

**Bridge steps L0, L, A and M.** These are the last four steps of the Mathlib bridge job at `E`:
- **L0**, `MATH-CON-1-S1B-1 build the imports of the module`, runs `lake --rehash build
  OIBridge.PolarizationClosure OIBridge.BridgeFiniteProtocol OIBridge.PreservationInductionInstances` with a
  30-minute limit.
- **L**, `MATH-CON-1-S1B-1 elaborate the module`, runs `lake env lean OIBridge/PolarizedProtocol.lean` into a file.
- **A**, `MATH-CON-1-S1B-1 axiom reports within the three axioms` (id `mathcon1_s1b1_axioms`), prints that file and runs
  `controls.py axioms` on it. The gate records the class of the twenty-six reports as the step output `reports`:
  - `standard`: each frozen print is reported once, in order, within `[propext, Classical.choice, Quot.sound]`, with no
    other report of the namespace, no unparsed report, no error line, and none of `sorryAx`, `Lean.ofReduceBool` and
    `Lean.trustCompiler`;
  - `complete-nonstandard`: each is reported once, in order, every report parses, there is no other report, and some
    report names an axiom outside the three;
  - `incomplete`: anything else.

  A succeeds exactly when the class is `standard`.
- **M**, `MATH-CON-1-S1B-1 marker complete reports with an axiom outside the three`, runs only when A recorded
  `complete-nonstandard`.

L0, L and A run with `if: ${{ !cancelled() }}`. Every reading requires L0 `success`.

**One kernel gate (KTRANS-SEP-2's form).** The step conclusions carry one fact about the kernel layer: whether all
twenty-six reports are standard. The verdict therefore attributes no kernel result to a single cell:
- The seven obligation tokens and KC are **one reading of one gate**.
- On the positive reading, each prints PROVED, or HOLD for KC.
- On the negative reading, each prints NOT-ESTABLISHED, with no attribution to a cell.

Per-cell attribution would also mislead, since `#print axioms` reports transitively: O-3d and O-3e consume O-3a–c, and
§F2 consumes O-2 and O-3e. A kernel NOT-ESTABLISHED arises only from complete reports of which one names an axiom
outside the three. That is, in practice, the `sorryAx` that Lean's error recovery records at a term that does not
elaborate. A literal `sorry` in the module fails N3, which voids the verdict before any token is read.

**VOID** when any of these holds:
- a required control failed or did not run;
- `RUN` and `JOBS` are not one complete run with one bridge job;
- the run is not the exact-head run at `E`;
- L0, L, A and M are not each present once, consecutive, last, and after `Release gate`;
- the step conclusions are neither positive nor negative as the table defines. Among these:
  - L0 is not `success`;
  - A and M both succeeded;
  - A failed and M was skipped;
  - A was skipped or cancelled;
  - M failed;
  - `Build` or `Release gate` failed beside otherwise positive steps;
- the exact layer is not complete, or it exits 4 (a countercontrol did not fail as stated).

| reading | tokens printed | rule |
| --- | --- | --- |
| kernel positive | `MATHCON1-O1-PROVED`, `MATHCON1-O2-PROVED`, `MATHCON1-O3A-PROVED`, `MATHCON1-O3B-PROVED`, `MATHCON1-O3C-PROVED`, `MATHCON1-O3D-PROVED`, `MATHCON1-O3E-PROVED`, `MATHCON1-KERNEL-CONTROLS-HOLD` | S1, N1–N3 and S5 hold; `Build`, `Release gate`, L0, L and A `success`; M `skipped` |
| kernel negative | the eight tokens above with `-NOT-ESTABLISHED` in place of `-PROVED` and `-HOLD` | L0 `success`, A `failure`, M `success`, with L `success` or `failure` |
| exact positive | `MATHCON1-EXACT-AGREES` | complete run, exit status 0 |
| exact negative | `MATHCON1-EXACT-NOT-ESTABLISHED` | complete run, exit status 3 |

No reading reads another. The **stage reading** is generated from the tokens:
- `MATHCON1-S1B1-CANDIDATE-C` exactly when the kernel reading and the exact reading are both positive, every control
  of `check E --freeze F` passes, and the exact-head run at `E` is green on every job;
- `MATHCON1-S1B1-HALTED` otherwise (`S12`).

A negative reading fails a job (A, or the shard's checker step), so it always halts the round.

## The result note (generated; frozen texts and template)

`result.md` is generated by `controls.py` from the measurements, in this order:
1. the round, `D`, `F` and `E` (or `W`);
2. the control table, one row per code with PASS or FAIL;
3. the printed tokens;
4. the stage reading;
5. frozen text 1, only under `MATHCON1-S1B1-CANDIDATE-C`;
6. frozen text 2, always;
7. frozen text 3, always;
8. on a halt, the halt section.

The template's own words (headings, row labels, connective sentences) are embedded in `controls.py` and frozen with
it.

**Frozen text 1, the earned reading:**

> Earned reading: in polarizedTheoryC (Fin 2), whose class PolC contains the swap images H ⊗ I_n that the
> polarization map supplies, and with them the Hadamard matrix H on Fin 2, the four-outcome attempt instrument of
> B23's balanced protocol is available, and for every finite depth k the channel
> (1 − (3/8)^k)·Ad(drivePhase) + (3/8)^k·id is available. The attempt conjugated by H is an available four-outcome
> instrument whose outcome-0 branch is (5/8)·Ad(H·drivePhase·H), where H·drivePhase·H is unitary, non-monomial, and
> non-Clifford in the sense of D3; for every finite depth k the channel (1 − (3/8)^k)·Ad(H·drivePhase·H) +
> (3/8)^k·id is available. In the monomial baseline, at every carrier, a branch of an available instrument that
> equals p·Ad(U), with p > 0 and U unitary, has U monomial. Closing the monomial class together with any family of
> monomial matrices under the architecture operations and relabelling yields only monomial matrices. PolC and PolGen
> lie in the fiat class generated by the monomial class and the swap images, and the conjugated instrument is
> available there. This is a candidate for outcome (C) of the MATH-CON-1 preregistration, and nothing more.

**Frozen text 2, the non-inference rule:**

> Non-inference rule: Hadamard is supplied by the polarization map, not derived; the map's status stays proposed.
> The round does not claim that OI independently generates the quantum operation, does not run the circularity test
> or controls CC-0, CC-1(b), CC-2 and CC-4, does not score T1, T3 or T5, and assigns no outcome of the
> preregistration's §6. Outcome (C) still requires obligations O-6, O-8, O-9 and O-10 and the controls they feed,
> including valid instruments and repeatable composition as the owner scoped them. The seven obligation tokens are
> one reading of one kernel gate over all frozen reports. The calibration recorded here is the design's CC-3(b) on
> drivePhase, not the CC-0 calibration. Passing any control is not evidence that a closure law is independently
> physically justified, and no result here bears on the independent physical justification of the map or on its
> derivation from OI.

**Frozen text 3, the owner's boundaries** (#1169 comment 6721662886, amaybaum, 2026-11-08T12:46:00Z, verbatim):

> Authorize the first stage only: O-1, O-2, and O-3a–e.
>
> The objective is to establish whether the proposed construction works mathematically at this level, while
> explicitly recognizing that Hadamard is supplied rather than derived.
>
> Conditions:
> - Freeze `F` before execution.
> - Require exact-head CI at `F` and `E`, with the prescribed receipt.
> - Do not execute O-4 through O-10 without separate authorization.
> - Do not claim that OI independently generates the quantum operation.
> - A successful first stage establishes only a candidate for outcome (C). The complete outcome still depends on the
>   remaining obligations, including valid instruments and repeatable composition.
>
> Important distinction: passing the calibration control must not be presented as evidence that such a closure law
> is independently physically justified. That remains a separate question.
>
> MATH-CON-1 is currently addressing the first question. Success there must not be promoted to success on the
> second or third.

**The halt section** names the halt route and nothing more. One frozen sentence per route:

| route | frozen sentence |
| --- | --- |
| kernel negative | "The kernel gate read complete reports with an axiom outside the three; the frozen statements are not proved in this round; open." |
| exact negative | "The exact layer ran to completion with a failing check: <check ids>." |
| a control failed or evidence could not be completed | "Control <code> failed: <the frozen reason for that code>." |
| an unproved statement (see *Stop rule*) | "<theorem name>: not proved in this round; open." Then the proof-recovery note's location. |

The note interpolates only:
- commit ids;
- check ids from the frozen list (X1 … XC4);
- control codes;
- theorem names from the frozen list;
- the PR comment id of the proof-recovery note.

command-scan site: dump

It also interpolates the dump's `non_indexed_leading_parsers` count, as an integer. It never interpolates any other
measured or free text.

Under the route `dump`, when that count is positive, the control table carries this frozen caveat sentence: "The command scan covers the
indexed command tokens of the dumped environment and the frozen floor; <k> non-indexed command parsers are not
covered, so the scan's completeness for them is unverified."

A control's reason is a frozen string per code:

| code | frozen reason |
| --- | --- |
| T | "the chain from D through F to the commit is not as frozen" |
| G | "the commit's changes lie outside the governed paths" |
| R | "the record directory holds a file outside the frozen list" |
| B | "a pinned blob or the static form of a script differs" |
| DS | "the design record differs from the accepted blob" |
| N1 | "a declaration or column-0 line is outside the frozen list and the auxiliary policy" |
| N2 | "the module differs from the frozen skeleton" |
| N3 | "a forbidden token or option occurs in the module" |
| S1 | "a frozen statement differs" |
| S2 | "a consumed kernel name or the import closure differs from D" |
| S4 | "a screened phrase occurs outside the frozen texts" |
| S5 | "the print list differs" |
| X | "the exact layer is incomplete or a countercontrol did not fail as stated" |
| XS | "a reconstructed definition's source text differs" |
| I, C, W | "a shared file differs from D's with the frozen splices" |
| P | "a pinned file, a run result or the order evidence does not meet its rule" |
| LIVE | "a live self-test fails with the frozen splices" |
| V | "the note differs from its generated form" |
| evidence | "the run evidence could not be completed" |

The self-test screens every frozen reason with S4 and checks it under V.

Failure to prove a statement here is not a disproof. The design's routing for it is "not established", and it
assigns no §6 outcome.

Control V checks the note:
- the computed tokens, exactly;
- the stage reading;
- frozen text 1 exactly when the stage reading is `MATHCON1-S1B1-CANDIDATE-C`;
- frozen texts 2 and 3 always;
- the halt sentences by route;
- the template's words.

All texts are compared whitespace-normalized. S4 screens only the note's text outside the three frozen texts.

## The workflow edit (frozen text embedded in `controls.py`, control W)

- **Bridge steps.** The four steps L0, L, A and M go directly after the bridge job's last step at `D`:
  - L0, L and A have `if: ${{ !cancelled() }}`;
  - L0 has `timeout-minutes: 30`;
  - L redirects to `"$RUNNER_TEMP/mathcon1-s1b1-axioms.log"`;
  - A runs under `set -euo pipefail`, with the gate as its last command;
  - M's condition is `${{ !cancelled() && steps.mathcon1_s1b1_axioms.outputs.reports == 'complete-nonstandard' }}`.
- **Shard.** `probes_mathcon1s1b1`, `Numerical probes / MATH-CON-1-S1B-1 exact layer`, checks out with
  `fetch-depth: 0` and uses Python 3.11. It has two steps:
  - `python3 -I -B verification/lean/mathcon1_s1b1_check.py`;
  - `python3 -I -B verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/controls.py --self-test`.

  It installs no third-party package.
- **Aggregate.** In the `Numerical probes` job, each after the last round's line at `D`:
  - `probes_mathcon1s1b1` in `needs`;
  - `MATHCON1S1B1_RESULT`;
  - its echo;
  - `test "${MATHCON1S1B1_RESULT}" = success`.

No step continues on error, overrides the shell, or masks a status with `||`.

## The controls (in `controls.py`)

`controls.py` imports only the standard-library modules on its frozen allowlist:
- `ast`, `contextlib`, `hashlib`, `io`, `json`, `os`, `re`, `subprocess`, `sys`, `tempfile`, `unicodedata`.

It imports nothing from the repository. It reads `D` and the commits it is given with read-only git commands. Its
write-mode `open` calls are only at two frozen sites:
- `$GITHUB_OUTPUT` in `axioms`;
- a `tempfile` directory in the self-test and `mock-s1`.

Every other output goes to stdout. This includes the generated note (`controls.py note …`), `derive-run`'s run result
and `order`'s order evidence. The executor redirects stdout into the record file and commits it. That is a git
operation outside the script, and controls P and V check the committed bytes against a fresh regeneration.

It embeds every frozen text. Its codes:

**Chain, paths and files**
- **T** (chain): `D..commit` is one chain of single-parent commits through `F`; `delta(D, F)` is the control plane;
  the round declaration and the governed-paths digest, re-derived from `F` with `control_plane` and
  `governed_digest`, equal the frozen expectation;
  the preregistration at the commit is `F`'s; a re-cut `F` fails.
- **G** (governed paths): `delta(D, commit)` is the five execution paths, with their statuses, plus record files.
- **R** (record files): only these are allowed:
  - `preregistration.md`;
  - `amendments/**`, present only if at `F`;
  - `controls.py`;
  - `evidence/**`;
  - at `E` or `W`, `result.md`.
- **B** (blobs and static form):
  - `controls.py` and the checker are at their pinned blobs;
  - an AST check confirms each file's import allowlist;
  - the checker has no `open`, `__import__`, `importlib`, `exec` or `eval`;
  - the write-mode `open` sites in `controls.py` are the two frozen ones.
- **DS** (design): `DESIGN.md` at the commit has blob `4d47fbc876427a26dff12a486fa43a67a95aac5b`, the blob of
  `06b5d4f2`, which differs from the accepted `27359cbd…` in the one owner-authorized label line only.

**Module form**
- **N1** (declarations): the frozen declarations, in order and by kind, plus only `aux_` theorems as the auxiliary
  policy allows.
- **N2** (skeleton): the frozen skeleton, under the elision rule.
- **N3** (hygiene): none of `sorry`, `admit`, `axiom`, `opaque`, `native_decide`, `implemented_by`, `extern` or
  `unsafe`; and no command-level `set_option` other than the permitted form, in its permitted placement. N3 governs
  command-level options only. In-proof `open … in` and `set_option … in` are governed by N1's scan and its exemption
  grammar (*Permitted scoped forms*).

**Statements and text**
- **S1**: the statements of §B–§G.
- **S2**: resolution. Every consumed kernel name has its frozen text at `D` and is declared once in the import
  closure. The module declares no name its closure declares. No frozen short name occurs in a `#print axioms` line at
  `D`.
- **S4**: the phrase screen on the module header and on the result note outside frozen texts 1–3. The phrases:
  - "generated by OI", "OI generates", "independently generates", "derived from OI", "native OI";
  - "physically justified", "physical justification is", "noncircular";
  - "outcome (C) is reached", "outcome (C) holds", "establishes outcome (C)", "(P)", "T5 holds", "CT returns";
  - "installed", " iff ", "if and only if", "is equivalent to", "exactly when".
- **S5**: exactly the twenty-six `#print axioms` lines, in order.

**Exact layer**
- **X**: the exact layer is complete, and its reading.
- **XS**: the source-text control.

**Shared files**
- **I**, **C**, **W**: `OIBridge.lean`, the census and `verify.yml` are `D`'s with exactly the frozen splices.

**Evidence**
- **P** (pins and run results):
command-scan site: dump
  - the files pinned at `F` (`evidence/d-push-run.json`, `evidence/command-tokens.json` and the design-run evidence)
    and `evidence/f-run/results.json`
    are each present with their sha256, and each is a structured result with no timestamp or duration field. This
    clause covers those files only;
  - with `--freeze`, nothing is `PENDING`. A `PENDING` field is an occurrence of the word that lies outside an inline
    code span. Fenced code blocks count as outside, so the dump script's `open`-line comment is a field. An
    occurrence inside backticks is rule prose, which names the word and is not a field;
  - `evidence/f-run/results.json` is `F`'s exact-head run: its identity is right, every job is `success`, its bridge
    steps are those of `D`'s workflow, and the round's shard and steps are absent;
  - `F`'s tree carries no module, checker or import line, read through git, not from the run;
  - `evidence/runs-to-f.json` (added at S1) and `evidence/order.json` (added at S2, or at `W`) each meet their own
    frozen schema (below), and their rules hold. P re-checks `runs-to-f.json` at S1 and at `E`, and `order.json` at
    `E` (or `W`).

**`evidence/runs-to-f.json`, the run events up to `F` (own frozen schema; under both routes).**
- **Producer.** It is produced by `controls.py runs-to-f`, to stdout, from every page of the runs answers for the design
  branch and for the round branch (`GET …/actions/runs?branch=<name>&per_page=100`, `gh api --paginate`). It also
  uses every page of `GET …/actions/runs?head_sha=<sha>&per_page=100` for each design-branch commit, and the
  issue-comments answer of each approval comment. The answers are captured at designation time, and each capture is
  checked against its `total_count`.
- **Keys**, exactly:
  - `schema` (`"mathcon1-s1b1-runs-to-f"`) and `version` (`1`);
  - `design_branch` and `round_branch_to_f`, each
    `{name, total_count, runs: [{run_id, head_sha, head_branch, event, created_at}]}`.
    `round_branch_to_f` keeps the round-branch runs whose `head_sha` lies in `D..F`;
  - `design_head` and `design_commits`: the design head, and `[{sha, runs: [{run_id, event, head_branch}]}]` over the
    design-commit set (*Branches*), from the `?head_sha=` queries;
  - `design_pr`: `{number, head_ref, head_repo, base_ref, state}`, from the pulls API answer;
  - `approved_dispatches_to_f`: approval entries (*Approval entries*, below);
  - `sources`: the sha256 of each page and each captured comment answer.
- **Rule** (owner condition 3, no special CI dispatch):
  - every design-branch run has event `pull_request` and the frozen `head_branch`; every `design_commits` run is
    `pull_request` or an approved entry, matched by `run_id`; `design_pr` binds as *Branches* states;
  - every `workflow_dispatch` run in `round_branch_to_f` appears in `approved_dispatches_to_f`, and every other run
    there has event `pull_request`;
  - exactly one entry of `approved_dispatches_to_f` is the `F` attestation: its `head_sha` is `F` and its `run_id` is
    the run in `evidence/f-run/results.json`. Other entries record owner-approved dispatches of a re-cut candidate
    `F`, or a retaken `F` dispatch;
  - every capture is complete.

**Approval entries.** Each entry of `approved_dispatches_to_f` (in `runs-to-f.json`) and of `approved_dispatches` (in
`order.json`) is `{run_id, head_sha, stage, approval_comment_id, approval_created_at, quoted_words}`. An entry with stage
`retake after host VOID` also carries `voided_run_id`, `preservation_comment_id` and `preservation_created_at`. P accepts
an entry only when all of these hold:
- `quoted_words`, the owner's words as the approval comment quotes them, name the dispatched commit by its full
  40-hex id and name the stage: `F`, `F retaken`, `re-cut candidate F`, `S1`, or `retake after host VOID`;
- the run's `head_sha` equals that quoted id;
- `approval_created_at` is earlier than the run's `created_at`;
- no `approval_comment_id` appears twice across both lists, so each approval authorizes exactly one run;
- for stage `retake after host VOID`, all of these also hold:
  - the preservation comment names `voided_run_id` and the sha256 of that run's `void-run` record (*Stop rule*);
  - `preservation_created_at` is earlier than `approval_created_at`;
  - `approval_created_at` is earlier than the retake run's `created_at`;
  - the retake's `head_sha` equals the voided run's `head_sha`.

  The preservation comment's answer is captured, with its digest in `sources`.

No stage authorizes a new `E` candidate after a result at `E`. A candidate `E` re-cut before its dispatch has produced
no result and needs no dispatch approval. After any exact-layer result at `E` other than exit 0, no further `E` is
dispatched (*Stop rule*).

The approval comments' answers are captured, and their digests are in `sources`. Dispatches at or after `E` lie
outside `order.json`, which is written at S2. They are recorded by the receipt's `check-run` attestations. Each such
record quotes its approval (comment id, author, time, and the words naming the commit and stage) under the same
rules. A host-VOID retake's record also names its voided run and its preservation comment. Review checks those records at `Q`; no predicate reads attestations (`S5`).

**`evidence/order.json`, the order evidence (own frozen schema; timestamps are its content).**
- **Producer.** It is produced by `controls.py order`, to stdout, from these captured API answers:
  - under the route `dump`, the runs answer for the dump's design run (`GET /repos/{owner}/{repo}/actions/runs/{id}`);
  - under both routes, the runs answers for the whole design branch (`GET …/actions/runs?branch=<design branch>&per_page=100`,
    every page);
  - the issue-comments answer for the designation comment (`GET /repos/{owner}/{repo}/issues/comments/{id}`);
  - the runs answers for the proof dev branch (`GET …/actions/runs?branch=<dev branch>&per_page=100`, **every page**,
    taken with `gh api --paginate`);
  - the runs answers for the round branch (`GET …/actions/runs?branch=round/mathcon1-s1b-1-20261108&per_page=100`,
    every page);
  - every page of `GET …/actions/runs?head_sha=<sha>&per_page=100` for each dev-branch commit;
  - the issue-comments answer of each approval comment in `approved_dispatches`.

  These answers are captured beside `RUN` and `JOBS` and are not committed. Each runs capture is complete only when
  the number of runs across its pages equals the `total_count` its first page reports. An incomplete capture fails
  P.
- **Keys**, exactly:
  - `schema`: `"mathcon1-s1b1-order"`;
  - `version`: `1`;
  - `designation`: `{comment_id, author, created_at, quoted_words}`. `quoted_words` is the owner's designation text as
    the comment quotes it;
  - `dev_branch`: `{name, first_run: {run_id, head_sha, created_at} | null, events}`;
  - `design_branch`: `{name, earliest_run_created_at, events}`, under both routes;
  - `round_branch_after_f`: `{runs: [{run_id, head_sha, event, created_at}]}`, the round-branch runs whose `head_sha`
    is not in `D..F`;
  - `approved_dispatches`: approval entries (*Approval entries*), one for each owner-approved `workflow_dispatch` after
    `F` and before S2 (S1 if approved, and host-VOID retakes under separate owner decisions). The `E` dispatch is created after `E` and is
    not in this list: it is the `check-run` attestation that `verdict` reads as `RUN`;
  - `dev_head` and `dev_commits`: the dev head, and `[{sha, runs: [{run_id, event, head_branch}]}]` over the
    dev-commit set (*Branches*), from the `?head_sha=` queries;
  - `dump` (route `dump` only; otherwise `null`): `{run_id, event, design_commit, created_at, round_commit, round_commit_first_run_created_at,
    round_first_commit, round_first_commit_first_run_created_at}`.
    It records the dump's design run, the round-branch commit named on the `command-scan dump run` line, the round
    PR's first control-plane commit (the oldest commit of `rev-list F ^D`) with its first host run;
  - `provenance`: `{dev_first_commit, dev_first_commit_parent}`. These are recorded for the reader and read by no rule.
    They name commits off `main`, and they are classified as provenance under §A.42 item 8;
  - `round_branch_first_execution_run`: `{run_id, head_sha, created_at} | null`, the first host run whose `head_sha`
    is S1 or a later execution commit;
  - `sources`: the sha256 of each captured answer page, and each runs capture's `total_count`;
  - `ordering`: `"designation-before-execution"` or `"violated"`.
- **The ordering holds** exactly when all of these hold:
  - `designation.quoted_words` contains the owner's designation of `F` by its full commit id. The owner's designation
    rests on those quoted words, as in KTRANS-SEP-2's receipt, and not on `author`. `author` is recorded, but the
    coordinating session also posts as `amaybaum`, so the login alone shows no human authorship;
  - `designation.created_at` is earlier than every non-null run `created_at` in the file. Each first run is the
    earliest `created_at` across all pages of its capture;
  - every runs capture is complete;
  - (owner condition: no special CI dispatch) every design-branch run and every dev-branch run has event
    `pull_request`, and every `dev_commits` run is `pull_request` or an approved entry, matched by `run_id`. Every
    run in `round_branch_after_f` has event
    `pull_request` or appears in `approved_dispatches`, and every entry there meets *Approval entries*;
  - under the route `dump`, all four of these hold:
    - `dump.round_commit_first_run_created_at` is earlier than `dump.created_at`;
    - `dump.round_commit` equals the commit on the `command-scan dump run` line;
    - `dump.round_first_commit_first_run_created_at` is earlier than `design_branch.earliest_run_created_at`;
    - `dump.event` is `pull_request`, and `dump.design_commit` equals the design commit on the dump-run line.

  The ordering rests on host timestamps alone. The dev branch's commits are not support.
- **Where it lands.** It is added at S2 (`E`). On a halt before S2, it is added at `W`, with null run entries where no
  execution run exists.
- **What it cannot measure.** It measures the first host-visible execution artifact. Local work before the first push
  is not measurable, and this limit is stated.
- **LIVE**: every self-test the workflow at `D` runs prints its pass line on `D`'s files with the frozen splices
  applied. This runs before `F` locally; at `E` it holds as every job green.
- **V**: the note, as above.

**Self-test** (`controls.py --self-test`, run in the shard). It drives mutations through every control, each failing
with its code (alone where marked).

*Statement and definition mutations (S1, or N2 where a body changes):*
- `hp : 0 < p` dropped from O-1;
- `substratumClass` replaced by `PolC` in O-1's hypothesis;
- a `pol : PolC T K → FiatC T K` constructor added to `FiatC` (N2);
- `swap` added to `MonoExt` (N2);
- `toffoliToken`'s control value `3` changed to `2` (N2 and XS);
- `ancSign`'s parity changed (N2 and XS);
- `(1 / 2 : ℂ)` in `ancillaHH` changed (N2);
- `hdh`'s factors reordered (N2);
- `conjugatedAttempt` with one `conjChannel hadamard` removed (N2);
- `pauliY` added to the `P` set of `NonClifford` (N2);
- `p ≤ 1` dropped from `CoherentNonMonomialBranch` (N2);
- `siteShearImage 4` replaced by `1` in the O-3a word (S1);
- `(5 / 8 : ℝ)` changed in the branch (S1).

*Hygiene, prints, design and note:*
- a `sorry` (N3 alone);
- a twenty-seventh `#print axioms` line (S5);
- `DESIGN.md` changed (DS alone);
- an S4 phrase in the note's template text (S4);
- the earned reading under a halted reading (V);
- frozen text 3 altered (V).

*Column-0 rule (R2-B1).* Each of these is placed directly after a frozen theorem's proof, and each fails N1:
- a column-0 `instance`;
- a column-0 `attribute [simp]`;
- `@[simp] private theorem aux_x`;
- a column-0 `notation`;
- a column-0 `lemma`.

In addition:
- a column-0 `-- comment` inside a proof fails N2;
- a multi-line `aux_` docstring with a column-0 continuation fails N1;
- an **indented** `instance` on the line after a frozen proof fails N1, through the command scan;
- an `instance` on the **same line** after `by simp` fails N1, through the command scan;
- an indented `@[simp] private theorem aux_y` fails N1;
- `open Finset in`, `open scoped ComplexOrder in` and `set_option maxHeartbeats 400000 in` inside a proof pass;
- the word `instance` inside a comment or a string literal in a proof passes.

*Command scan (R3-B1, R3-N2).* Each of these, placed indented in or after a frozen proof, fails N1:
- an indented bare `open Foo` after a term-mode proof;
- `open Foo hiding x in`;
- `set_option maxHeartbeats 9000000 in` inside a proof;
- `set_option autoImplicit true in` inside a proof;
- `alias`;
- `notation3`;
- `run_cmd`;
- `elab_rules`;
- `irreducible_def`;
- a `/--` docstring opener inside a proof;
- a token drawn at random from the embedded dump list but absent from the floor (ii).

Each of these, inside a proof, passes:
- the nested block comment `/- /- instance -/ -/`;
- the escaped identifier `«instance»`;
- the char literal `'"'` followed by the string `"instance"`;
- the raw string `r#"instance"#`;
- the identifiers `infer_instance`, `h'` and `Foo.instance`.

Each of these, placed after a frozen proof, fails N1, because the `'` is part of the identifier or does not begin a
complete char literal, so nothing is skipped:
- `h𝓘' instance`;
- `'a instance`;
- `hŝ' instance` (`ŝ`, U+015D, is Latin Extended-A).

Each of these, inside a proof, passes, because `é` (U+00E9) and `ŝ` are identifier characters and each word is one
identifier: `éinstance`, `ŝinstance`, `instanceé`.

The identifier-class tables in `controls.py` are compared with the ranges above, and `×` (U+00D7) and `÷` (U+00F7) are
checked to be non-identifier characters.

*Frozen block expectation and run events (T, P; both routes):*
- an altered governed-paths block (`execution AM` for `execution A` on the module) at a scratch `F` fails T on the
  digest;
- an altered `kind` line fails T;
- a design-branch run with event `workflow_dispatch` in `runs-to-f.json` fails P;
- a second round-branch `workflow_dispatch` in `D..F` with no approval entry fails P;
- an approved dispatch of a re-cut candidate `F`, and an approved retaken `F` dispatch, each beside the `F`
  attestation entry, pass P;
- `approved_dispatches_to_f` with no entry matching `f-run/results.json`'s run, or with two such entries, fails P;
- a round-branch `workflow_dispatch` after `F` that is missing from `approved_dispatches` fails P;
- each of these approval-entry defects fails P: a reused approval comment, an approval posted after its run, an
  approval whose quoted words name another commit, an approval naming no stage, and a run whose `head_sha` differs
  from the quoted id;
- each of these branch defects fails P: a `branches` line that differs between the first control-plane commit and
  `F`; a captured design branch or dev branch with another name; a design-branch run with another `head_branch`;
  under `dump`, a dump run on another branch; a design pull request whose `head.ref` is another branch, whose
  `head.repo` is a fork, or whose `base.ref` is not `main`; an unapproved `workflow_dispatch` at a design commit, or
  at a dev commit, made from another branch;
- each of these passes P: a closed design pull request that binds; a dump run whose `pull_requests` is empty;
  `D`'s push run on `main` (outside the design-commit set); the `F` attestation run (outside the sets, and an
  approved entry); an approved S1 dispatch at a dev commit pushed to the round branch as S1 (exempt by `run_id`);
- a `design pr` line still `PENDING` at `F` fails P;
- the frozen preregistration with every field filled passes P under `--freeze`, although its rule prose still names
  the backticked word six or more times; one unbackticked occurrence left anywhere, including inside the fenced dump
  script, fails P;
- a dev-branch run with event `push` or `workflow_dispatch` fails P;
- a designation whose quoted words lack `F`'s full id fails P, even under the owner's login;
- a `toolchain` field of `v4.33.0` or `4.33.0-rc1` against the pin `leanprover/lean4:v4.33.0` fails P, and `4.33.0`
  passes.

*Route line and site lines (P; both routes):*
- a preregistration edited exactly as the drafting note prescribes for `floor-only` passes P (positive);
- the unedited `dump` text, with the route line set to `dump` and the dump-run line filled, passes P (positive);
- under either route, each of these fails:
  - the route line reading `PENDING`;
  - the route line appearing twice;
  - a remaining "*Drafting note" line;
  - a site line naming the other route;
  - six or eight site lines;
- under `floor-only`, a remaining reference-set line or dump-run line fails;
- under `dump`, a missing reference-set line or dump-run line fails.

command-scan site: dump

*Dump consistency (P; route `dump`):*
- a dump whose tokens are escaped (`«#eval»`, `«@[»`) fails the reference-set condition;
- a dump with an empty `leading_tokens` fails;
- a dump missing one reference token (`notation3`) fails;
- a reference-set line that differs between the first control-plane commit and `F` fails;
- a `command-scan dump run` line naming a commit outside `D..F`, or one without the reference-set line, fails;
- an `order.json` `dump` entry whose dump run precedes the round commit's first host run fails;
- an `order.json` `dump` entry with a design-branch run created before the first host run of the round PR's first
  control-plane commit fails;
- a design-branch runs capture missing a page fails;
- the embedded list differs from `evidence/command-tokens.json` (fails);
- the file's sha256 differs from its pin (fails);
- a dump with `non_indexed_leading_parsers > 0` passes P, and the generated control table carries the frozen caveat
  sentence;
- a capture of runs answers missing a page fails P.

*Auxiliary policy:*
- a `private theorem aux_col` with a proof passes;
- a `private def` fails N1;
- an `@[simp]` attribute fails N1;
- `set_option maxHeartbeats 2000000 in` before a frozen theorem passes;
- a command-level `set_option maxHeartbeats 9000000 in` fails N3;
- a command-level `set_option autoImplicit true in` fails N3;
- a global `set_option` fails N3;
- a command-level `set_option maxHeartbeats 2000000 in` before a `def` fails N3.

*Static form:*
- the checker importing `os` fails B;
- the checker calling `open` fails B;
- a new write-mode `open` in `controls.py` fails B.

*Exact layer (X):*
- a crash (exit 1) is VOID, and at `E` the stage reading is HALTED, with no retake offered;
- a cut summary line is VOID, and halts at `E`;
- a wrong check or countercontrol count is VOID, and halts at `E`;
- a summary disagreeing with the exit status is VOID, and halts at `E`;
- exit 3 with a failing check reads NOT-ESTABLISHED, and halts;
- exit 4 (XC1 made to pass) fails control X, and halts on the control-failure route;
- a host VOID at `E` (a cancelled run, or missing jobs) with no recorded owner decision is not retaken: the stage
  reading is HALTED;
- a host VOID retake whose approval entry predates the preservation comment, or lacks the stage
  `retake after host VOID`, fails P;
- a host VOID retake with a valid owner decision recorded after preservation is accepted;
- each of these host-VOID retake defects fails P: preservation posted after the approval; an approval posted after
  the retake run; a retake whose `head_sha` differs from the voided run's; a preservation comment that does not name
  the voided run or the sha256 of its `void-run` record; a `void-run` record with a key missing or extra;
- an approval entry with any stage outside the frozen list, `replacement E candidate` included, fails P;
- a second `E` dispatch after an exact-layer result other than exit 0 at `E` halts the round;
- the four pre-`F` fixtures replay with their recorded results (the unconjugated attempt against BFP:194, the stopped
  formula against BFP:245, `ancillaHH · ancillaHH = 1`, and the synthetic X2 matrices).

*Gate and verdict:*
- every VOID rule;
- every class of `axioms`, with and without `GITHUB_OUTPUT`;
- `derive-run`'s refusals of incomplete or foreign jobs answers.

*Order evidence (P):*
- a designation after the first dev-branch run fails;
- a designation after the first S1 run fails;
- a dev branch whose first commit's parent is not `F` fails;
- an author other than `amaybaum` fails;
- a missing key or an extra key fails;
- a `sources` digest that does not match the supplied answers fails.

*Positive cases:*
- a full synthetic `check E --freeze F` on a scratch repository passes. Its `E` carries `evidence/order.json` with its
  timestamps, `evidence/f-run/results.json` and a generated note. This shows that the no-timestamp clause does not
  reach `order.json`;
- the halted variant at `W` with `order.json` and null run entries passes;
- every frozen reason string passes S4 and V.

*Generated notes (B1):* complete notes are generated by the real template code for each of these:
- the positive reading;
- the kernel-negative halt;
- the exact-negative halt;
- a control-failure halt;
- an unproved-statement halt.

Each must pass S4 and V unmodified, so no outcome reads VOID because of its own frozen texts.

*Positive controls:*
- the frozen skeleton completed with proofs;
- the checker on its fixtures;
- run results whose steps read positive.

## Stage requirements

| stage | its tree | its run validates | evidence | control |
| --- | --- | --- | --- | --- |
| `F` | `D` plus the control plane | `D`'s workflow passes on `D` plus this file: the run's identity, every job `success`, and no step of this round | `evidence/f-run/results.json`, by `derive-run`, added at S1 | P: `frun_ok`, `frun_consistent`, and `ftree_ok` through git |
| S1 | `F` plus `controls.py`, the checker, `evidence/` (with `runs-to-f.json`), the module, the import, the census and the workflow | local controls; pull-request runs are diagnostics only | the first host run at S1 (`created_at`); `runs-to-f.json` | `check S1 --freeze F --stage S1` |
| `E` | S1, proof-only repairs, `evidence/order.json`, and `result.md` | the execution: L0, L, A and M conclusions, and every job green | `RUN`, `JOBS`, and the comments and runs answers behind `order.json` | `verdict E --freeze F --run-api RUN --jobs-api JOBS` |

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane, after the owner's designation of `F` | T at S1 and `E`; P on `evidence/order.json` (own schema): host timestamps put the designation comment's `created_at` before the first host run of the proof dev branch and before the first execution run on the round branch, with the dev branch's first commit a child of `F`; carried at `E`, or at `W` on an early halt; commit dates are not used; local work before the first push is outside measurement (stated limit) |
| only O-1, O-2 and O-3a–e are executed | N1 (frozen list plus `aux_` theorems only); G; S4 |
| the design is unchanged | DS at S1 and `E`; `S7`, through `--verify-round Q` |
| statements and definitions are not changed in execution | N2 and S1 at every stage commit; self-test mutations |
| auxiliary declarations and options stay within the frozen policy; no command hides in an elided proof | N1: the column-0 rule, and the token-level scan of proof spans against the scan list of the frozen route line (route `dump`: the dumped command table plus the floor), with exact in-proof exemption grammar and Lean's identifier classes; N3 for command-level options; P for the route line, the dump's pin, the reference-set condition and agreement with the embedded list; the column-0, command-scan, lexing and auxiliary-policy self-test cases. Completeness is relative to the dumped environment, and the caveat applies if non-indexed parsers exist |
| each frozen theorem is kernel-checked within the three axioms, with no `sorryAx` | L0, L, A and M read by `verdict` from `JOBS`; the `axioms` gate's self-test cases |
| no kernel result is attributed to a cell from log text | the one-gate rule; `verdict` reads only step conclusions |
| the exact layer is about the kernel's own objects | XS at `E` |
| the checker uses the standard library only, opens no file and imports nothing from the repository; `controls.py` imports nothing from the repository, writes only at its two frozen sites, and sends the note, run results and order evidence to stdout | B's static checks at S1 and `E`; the static-form self-test cases |
| the exact layer's completeness is read from its exit status and summary, not from a log | X's rules; their self-test cases |
| countercontrols fail as stated, and kernel controls hold | X (XC1–XC4; a countercontrol that does not fail exits 4, which is a failed control, not a scientific reading); the KC token |
| every checker code path is exercised before `F` without computing O-3a–e's objects | the four recorded fixtures (BFP:194, BFP:245, `ancillaHH · ancillaHH = 1`, synthetic X2 matrices), replayed by the self-test |
| the note interpolates no free text | the frozen reason strings; the self-test screens each with S4 and V |
| no token over a failed or missing control; a tooling failure gives VOID, never a token | `verdict`'s gate; its self-test VOID cases |
| every outcome's note passes its own screen | the generated-note self-test cases (B1) |
| verdicts read structured data only | `derive-run` reads only `RUN` and `JOBS`; W pins the four steps and their conditions |
| the evidence is the exact-head run at `E` and no other | the identity rules of *The run*; self-test cases for push, pull-request and foreign runs |
| `F` carries no module | P (`ftree_ok`) at S1 and `E`; `mock-s1` before designation |
| every stage-1 requirement can be met by `F`'s own tree and run | `controls.py mock-s1 <candidate F> --f-run … --run-api RUN --jobs-api JOBS` prints `controls: OK` before designation |
| the shared-file edits are exactly the frozen splices and keep the other rounds' self-tests green | I, C, W; LIVE before `F`; every job green at `E`; after reconciliation, every live self-test on the reconciled tree |
| the result note says no more than the owner authorized | V and S4; frozen texts 1–3 |
| no manuscript or ROADMAP change | G; the release gate at `E` |
| the receipt holds, and the legacy records are untouched | `v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`; `legacy_records_check.py` at `E` and `Q` |

command-scan site: dump

## Stop rule

**Halts** under `S12`. The round appends a withdrawal commit `W` that restores every execution path to `F` and keeps
`result.md`, then reconciles and records a halted receipt. At `W`, the evidence of the failure is also committed,
in structured form and without personal data. The raw `RUN` and `JOBS` answers stay uncommitted:
- `evidence/halt-run.json`, the run result that `derive-run` derives for the failing exact-head run. When `derive-run`
  refuses the answers, as it does for a host VOID, this file is the run's `void-run` record instead;
- `evidence/halt-exact.json`, `{schema, version, exit_status, summary_line}`, the checker's exit status and summary
  line as `controls.py` captured them. This file is written only when the exact layer ran.

It halts on any of these:
- a control of `check` fails;
- **at `E`, any exact-layer outcome other than exit 0** (owner's halt-only decision): exit 3 (a failed check); exit 4
  (a countercontrol that did not fail as stated); a crash; or a missing, cut or inconsistent summary. The evidence is
  preserved at `W`, and the halt record asks the owner for a separate decision. The checker is never rerun and never
  repaired within the round;
- a `verdict` VOID that arises from the checker or the controls;
- a `verdict` VOID that arises from the host (a cancelled run, missing jobs, a runner failure), unless the owner
  records a separate decision to retake it. That decision must come after the evidence is preserved, which means
  the voided run's `void-run` record and its sha256 are posted on the round PR. The `void-run` record has its own frozen
  schema and contains no personal data. It is
  `{schema: "mathcon1-s1b1-void-run", version: 1, run_id, run_attempt, head_sha, event, status, conclusion,
  jobs: [{name, conclusion}], refusal_code}`, taken from the runs and jobs answers, where `refusal_code` is the code
  `derive-run` printed. It is then an approval entry with stage
  `retake after host VOID`, under *Approval entries*, and its `approval_created_at` must be later than that
  preservation comment. Before `E` it is recorded in `approved_dispatches`; at or after `E`, in the receipt's
  `check-run` attestation for the retaken run. Without such a decision, the round halts;
- the kernel reading or the exact reading is negative;
- a frozen statement cannot be proved without changing it, or a repair would touch anything but proofs and `aux_`
  theorems. This halt is decided as follows:
  1. The executor posts a proof-recovery note on the round PR: the statement, the strongest result reached, the
     derivations attempted, the verification performed, and the precise remaining gap.
  2. An independent reviewer records whether the attempt was proportionate.
  3. The owner records the halt decision on the PR.

  The note's halt sentence is then "<theorem name>: not proved in this round; open." The statement is not reported as
  false;
- the control plane would need to change. No amendment is possible after `F`; a successor round is drafted instead;
- execution would need O-4 to O-10, a new premise or a change to `DESIGN.md`.

**Pauses.** A §A.26 provenance anomaly in the round's work area stops all measurement and every push until a full
sweep has resolved it. It is not by itself a halt.

No control-plane defect is repaired in execution.

## Preconditions of `F`

1. **#1206 has landed as a merge commit of `06b5d4f2`.** Both `06b5d4f2` and `41a42cb9` are reachable from `main`, and
   `D` carries `DESIGN.md` at blob `4d47fbc8…`. The owner's ruling on the sibling record directory is quoted under *Authority*.
2. **Statement-elaboration design run.** A disposable design branch with a draft pull request carries the module
   with the frozen surface and `sorry` proofs, the import line, the census family, the workflow edit and
   `controls.py`. The ordinary pull-request CI runs it. The expected step conclusions:
   - L0 and L `success`;
   - A `failure`, with `reports=complete-nonstandard`;
   - M `success`;
   - the release gate fails on `sorryAx`.

   Its result is derived by `derive-run` and pinned as design evidence, not as an attestation. It fixes the `open`
   line and any elaboration corrections allowed above, each recorded as its own commit with a before/after diff.

command-scan site: dump

   **The command-table dump (scan list (i)).** The same design branch carries a design-only workflow step directly
   after `Build` and before `Release gate`. So the round's steps L0, L, A and M remain the bridge job's last four
   steps, and `derive-run` runs on the design run's answers unchanged. The step is not part of the frozen workflow
   edit, and W does not admit it at S1 or `E`. It runs `lake env lean <dump script>`, which writes
   `command-tokens.json` itself with `IO.FS.writeFile` (Lean's own messages go to stdout and never into the file),
   and uploads the file with `actions/upload-artifact`. The file is retrieved through the artifacts API as a structured file, never from a log
   (§A.44). The dump script is embedded verbatim in `controls.py` and in this section once fixed. Its draft, whose API
   names are to be confirmed by that run:

   ```lean
   import OIBridge.PolarizationClosure
   import OIBridge.BridgeFiniteProtocol
   import OIBridge.PreservationInductionInstances
   namespace OIBridge
   namespace PolarizedProtocol
   -- the module's frozen `open` line, verbatim (PENDING until the design run fixes it)
   open Lean Elab Command in
   #eval show CommandElabM Unit from do
     let mrev ← IO.Process.output { cmd := "git", args := #["-C", ".lake/packages/mathlib", "rev-parse", "HEAD"] }
     let st := Lean.Parser.parserExtension.getState (← getEnv)
     let some cat := st.categories.find? `command | throwError "no command category"
     let toks := (cat.tables.leadingTable.toList.map (·.1.toString (escape := false))).toArray.qsort (· < ·)
     let kinds := (cat.kinds.toList.map (·.1.toString (escape := false))).toArray.qsort (· < ·)
     IO.FS.writeFile "command-tokens.json" <| Json.compress <| Json.mkObj
       [("schema", "mathcon1-s1b1-command-tokens"), ("version", 1), ("toolchain", Lean.versionString),
        ("mathlib_rev", mrev.stdout.trim),
        ("imports", toJson #["OIBridge.PolarizationClosure", "OIBridge.BridgeFiniteProtocol",
          "OIBridge.PreservationInductionInstances"]),
        ("leading_tokens", toJson toks), ("non_indexed_leading_parsers", cat.tables.leadingParsers.length),
        ("command_kinds", toJson kinds)]
   end PolarizedProtocol
   end OIBridge
   ```

   The dump is admitted only under the reference-set condition (scan list (i)): every reference token appears
   verbatim and unescaped in `leading_tokens`. If it holds, the route line is set to `dump`, the file's sha256 is
   pinned, and its token list is embedded in `controls.py`. If the dump cannot be produced, or the condition fails,
   the route line is set to `floor-only (completeness unverified)`, and the drafting note's edits are made. Either
   way, the last pre-`F` commit deletes the drafting note, so exactly one route is written at `F`.
3. **No pin pending:**
   - the route line reads `command-scan route: dump` or `command-scan route: floor-only (completeness unverified)`,
     and the drafting note is deleted;
   - the `command-scan design pr` line names the design pull request's number;
   - the blobs of `controls.py` and the checker;
   - the frozen skeleton's digest;
   - XS's frozen texts and lines;
   - `evidence/d-push-run.json`;

command-scan site: dump
   - under `dump`, the `command-scan dump run` line carries all six fields: the run id, the design commit, a
     round-branch commit carrying the reference-set line, the toolchain pin, the Mathlib commit, and the dump file's
     sha256;
   - `evidence/command-tokens.json` (its sha256, and the token list embedded in `controls.py`).
4. **LIVE holds** locally on `D`'s files with the frozen splices.
5. **`mock-s1`** on candidate `F`, with its actual exact-head run, prints `controls: OK`. Its output and the derived
   file's sha256 are recorded on the pull request with the designation request.
6. **Checker fixtures recorded.** The four pre-`F` fixtures of the exact layer have run, with results matching BFP:194,
   BFP:245, `ancillaHH · ancillaHH = 1` and the synthetic X2 expectations. They are recorded with the `controls.py`
   and checker pins. No O-3a–e object has been computed.
7. **Branch restrictions are established.** Each of these must be established before `F` is requested:
   - **every commit of `rev-list <candidate F> ^D` is single-parent and touches only the control plane**, and the
     round declaration and governed-paths digest equal their frozen expectation. `check_t1` and `control_plane` are
     library functions of `tools/v3_verifier.py`, not CLI modes, so the check is this exact command, run from the
     repository root:

     ```sh
     python3 -I -c "import sys; sys.path.insert(0, 'tools'); import v3_verifier as v; r = v.Repo('.'); d, f = sys.argv[1], sys.argv[2]; rd, rid, kind, ent, cp, codes = v.control_plane(r, d, f); t1 = v.check_t1(r, d, f, cp); dig = v.governed_digest(ent) if ent else None; print(rid, kind, rd, dig, codes + t1); sys.exit(0 if not (codes or t1) and (rid, kind, rd) == ('MATH-CON-1-S1B-1', 'non-sealing', b'verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/') and dig == '81897a90a068b0402e68393f82cffda8fd83f0bda5283316c38d8c58b28e5107' else 1)" <D> <candidate F>
     ```

     It must exit 0. So no execution-related commit and no design-only step is on the round branch, and the two
     blocks are unchanged;
   - neither the design head nor, under `dump`, the dump's design commit is an ancestor of the candidate `F`. A design
     commit introduced into `D..F` would also fail the command above through `check_t1`, since it changes
     non-control-plane files;
   - **operational rule:** the design branch and the dev branch are not deleted before their last capture, which is
     `runs-to-f.json` at the designation of `F` for the design branch, and `order.json` at S2 (or `W`) for both. The
     commit sets are read through git from the branches at those captures;
   - every design-branch run is `pull_request` on the frozen design branch, and the design pull request binds
     through the pulls API (`head.ref`, `head.repo`, `base.ref`). Every design commit's `?head_sha=` runs are
     `pull_request` or approved entries. Every round-branch run whose `head_sha` lies in
     `D..<candidate F>` is `pull_request`, or is a `workflow_dispatch` with a valid approval entry. Exactly one such
     entry is the candidate's own `F` dispatch. This is read from the captured runs answers, every page,
     and recorded at S1 as `evidence/runs-to-f.json`.

   **If any of these cannot be established, the round halts before `F`.** No `F` is requested, preparation stops,
   and the finding is reported to the owner on the pull request.
8. **The owner's confirmation** that the exact layer, CAL (CC-3(b)) and KC are within the authorized first stage. It is
   recorded with the designation request.
