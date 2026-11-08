# A5-Q3 — A6 extended to affine offsets: comparison of E1–E3 (#1049) — DESIGN

**Standing: WIP / UNVERIFIED. Paper-only. Checkpoint 1 of 2.** This file fixes the question, the
three candidate extensions, the evaluation criteria, the decision rule and the controls. It is
committed alone, before any assessment of E1–E3 is written, and it contains no such assessment. It
is a preregistration of a decision *rule* in the sense of `AGENTS.md` §A.29, not a §A.39 native-round
control plane. It adopts no premise, changes no status and authorizes nothing. No code, enumeration
or Lean was written or run.

**Owner authorization [O].** #1049 comment 6719806528, posted from the owner's account (amaybaum) on
2026-11-08T09:27:26Z, recording the owner's chat decision of 2026-11-08:

> GO — paper-only. Authorize Q3 to compare E1–E3 as proposed, now that M-INACC review and FHE-SEL-1
> Stage 0 are complete. The assessment must preserve these boundaries: Evaluate each extension's
> mathematical consequences, physical assumptions, and independent justification. Allow none of
> E1–E3 is selected as a valid outcome. Do not introduce assumptions chosen merely to eliminate
> affine offsets. No scientific computation, manuscript changes, theorem promotion, or merge
> authorization. Keep A5's status unchanged until the evidence has undergone independent review and
> a separate decision.

The same comment records: "The rule for deciding among E1–E3 is preregistered in its own commit,
before any assessment is written. O5, the §7 computation, and the proposed changes to D16/R10/D3
stay unauthorized."

**Standard for candidate restrictions [O].** #1169 comment 6719386464, posted from the owner's
account (amaybaum) on 2026-11-08T08:41:15Z, records two owner statements that this file applies to
E1–E3:
- "A restriction designed to exclude a particular construction is treated as tuned to the target."
- "Every candidate physical restriction must have an independent physical motivation established
  before evaluating whether it selects quantum behaviour. A restriction that eliminates an unwanted
  classical model is not automatically evidence that nature obeys that restriction."

The second was stated for FHE-SEL-1 Stage 1. Here it is applied with "the target" read as T below
(§1.2), not as quantum behaviour.

**Owner decisions Q1 and Q2 [O].** #1049 comment 6624263637, posted from the owner's account
(amaybaum) on 2026-11-04T06:28:45Z:
- Q1: "Preserve Main's currently specified absolute interface as the formal baseline. The
  shift-invariant interface is a legitimate conditional alternative, not yet a derived description
  of all OI observers."
- Q2: "Treat amplitude shifts as mathematical relabellings unless their physical gauge status is
  justified."

**Source snapshot.** `main` at `9c201475ba6fd8f341591d14dd8e88db2e2aaa90`. Every `File:N` below is
`papers/File.md` line N at that commit; Lean paths are under `verification/lean-mathlib/OIBridge/`
at that commit. The two parent notes, at that commit, are:
- the **core file**, `verification/programmes/substratum/a5-linear-affine-20261104/A5-LINEAR-AFFINE.md`,
  cited by section and node (its own `File:N` references are to its base `1609dc44`, and this file
  does not reuse them);
- the **Q4 note**, `verification/programmes/substratum/a5-linear-affine-20261104/A5-Q4-STAGE2D.md`,
  cited by section and node.

**Labels.** [K] kernel-checked Lean on `main`; [P] a paper or record statement at the pin; [D] a
statement made in this file; [L] literature from memory, not re-read; [O] an owner decision, quoted.

***

## §1 The question

### 1.1 Statement

The core file's §6 poses Q3: "Is the local internal group of A6 AddAut(V) or the affine group, and is
an offset untransported, carried in the links, or transported (E1–E3)?" Its node N9 records that the
kernel's A6 predicate `A6Cov` (BackgroundIndependence.lean:131) is stated for link couplings typed
`V →+ V` and says nothing about offsets, so any statement of A6 for an affine rule is an extension
chosen beyond the formalized A6.

**Q3, as assessed here.** For each of the three extensions E1, E2, E3 of the core file's N9: what
does it entail mathematically, which assumptions does it import beyond the A6 sources on `main`, and
is each imported assumption independently physically justified? Is any of E1–E3 independently
justified as *the* extension of A6 to affine rules?

**Scope.**
- The candidate set is E1–E3 as stated in N9 (§2). The local-group clause of Q3 (AddAut(V) or the
  affine group) is assessed only as far as each extension's statement fixes it. N9 states all three
  with g : Λ → AddAut(V). An extension with an affine local group is not a candidate here. If the
  assessment finds that one of E1–E3 cannot be stated coherently without it, that is recorded as a
  finding for owner decision.
- O5, the promotion of the global group to local gauge invariance (Q4 note §1, Q4-8), is not
  examined. Criterion A3 (§3) records only the local transformation class each extension's own
  statement carries.
- The core file's §7 computation is not run.

### 1.2 The target, named so that it can be excluded

- **T1** — the offset vanishes, b = 0; equivalently A5 on the affine rule class at issue.
- **T2** — any downstream group output of Stage 2(d) in the form the corpus states it: the Q4 note's
  O1–O5, including U(3)×U(2)×U(1) as the Stage 2(d) group, the singlet-block U(1) as hypercharge
  (Substratum:163), S(U(3)×U(2)), SU(3)×SU(2)×U(1) and its local promotion.
- **¬T** — the opposite outcomes: a nonzero offset retained, or a loss of the singlet-block circle.

The decision rule (§4) never rewards an extension for producing T1, T2 or ¬T. The names T1, T2 and ¬T
appear in the rule only to exclude justifications that depend on them (§5.2).

***

## §2 The candidate extensions

### 2.1 Common data [D]

- ι is the site type (the torus Λ), N : ι → Finset ι the neighbourhood, V the alphabet, an additive
  commutative group. The carriers are V = (ℤ/q)^K (K = 1 for S1, K = 6 for the packaged carrier of
  `A6Instantiation`) and the complex lift V = ℂ^6.
- M : ι → ι → (V →+ V) is a link coupling. g : ι → AddAut V is a site-dependent transformation.
  `siteAct g c` and `gaugeLink g M i j = g i ∘ M i j ∘ (g j)⁻¹` are as defined at
  BackgroundIndependence.lean:92 and :124.
- b : ι → V is a site offset. The affine link-coupled update is F_{M,b}(c)_i = linkF N M c i + b_i,
  with `linkF` as at BackgroundIndependence.lean:118. The second-order rule is
  x(t+1) = F(x(t)) − x(t−1) (Main:726 item (xiii)).
- **The baseline** is `A6Cov N M` (BackgroundIndependence.lean:131): for all g and c,
  linkF N (gaugeLink g M) (siteAct g c) = siteAct g (linkF N M c). It is proved for every N and M
  (`a6cov_all`, :161) [K].
- **Transformation classes.** On the finite carrier: AddAut V, as in N9 and `A6Cov`. On the lift:
  AddAut(ℂ^6) (`cx1_complex_covariance`, A6Instantiation.lean:411); site-dependent unitaries
  (`cx2_unitary_gaugeLink`, :459); and, for constant g, the Q4 note's G_0 and Stage 2(d)'s
  U(K) (Substratum:163).

### 2.2 The extensions as given in the core file (verbatim, node N9)

> - **(E1) Additive links, untransported offset.** For F = `linkF` + b with b not transported,
>   covariance requires g_i b_i = b_i for all g:
>   - **K ≥ 2, any q:** a transvection moves any b ≠ 0, so b = 0, including at q = 2.
>   - **K = 1, odd q:** λ = −1 gives b = 0.
>   - **K = 1, q even > 2:** b ∈ {0, q/2}.
>   - **K = 1, q = 2:** AddAut(ℤ/2) is trivial, so b is unconstrained.
>   - *S1* (K = 1, q = 5) is excluded.
> - **(E2) Affine link maps.** If link couplings may be affine maps V → V, the offset moves into the
>   links. S1 is F_i = (x_{i−1} + 3) + (x_{i+1} + 3) over ℤ/5. Transport g_i ∘ M ∘ g_j⁻¹ keeps them
>   affine, and covariance holds identically, as `a6cov_all` (D3-a) does for additive links. This
>   restricts nothing.
> - **(E3) Transported site offset.** If b_i ↦ g_i b_i is transported with the configuration,
>   covariance again holds identically. This restricts nothing.

The consequences quoted inside these bullets are the core file's unreviewed [D] statements. They are
inputs to be re-derived in the assessment, not results this file relies on.

### 2.3 Precise restatement [D]

Each restatement transcribes the corresponding N9 bullet into the notation of §2.1. None changes it.

- **E1.** Data (N, M, b); transformation class ι → AddAut V; transport of M by `gaugeLink`; b is not
  transported.
  Cov_E1(N, M, b) :⇔ ∀ g c, linkF N (gaugeLink g M) (siteAct g c) + b = siteAct g (linkF N M c + b).
- **E2.** Data (N, A) with A_ij : V → V affine, A_ij(v) = M_ij(v) + a_ij, M_ij : V →+ V, a_ij ∈ V.
  Update F_A(c)_i = Σ_{j ∈ N i} A_ij(c_j); the rule offset is b_i = Σ_{j ∈ N i} a_ij.
  Transformation class ι → AddAut V; transport A_ij ↦ g_i ∘ A_ij ∘ g_j⁻¹.
  Cov_E2(N, A) :⇔ ∀ g c, F_{g·A}(siteAct g c) = siteAct g (F_A c), where (g·A)_ij = g_i ∘ A_ij ∘ g_j⁻¹.
- **E3.** Data (N, M, b); transformation class ι → AddAut V; transport (M, b) ↦ (gaugeLink g M,
  siteAct g b).
  Cov_E3(N, M, b) :⇔ ∀ g c, linkF N (gaugeLink g M) (siteAct g c) + siteAct g b
  = siteAct g (linkF N M c + b).

All three are stated on F, as `A6Cov` is. The phase-space form is not a separate reading
(cf. `leap_siteAct`, BackgroundIndependence.lean:144).

### 2.4 Readings and variants recorded in advance [D]

These are listed so that criterion J5 (§4) has a fixed starting set. The assessment may add others,
and must report each addition.

- **E1 / E1′.** The core file reads E1 as a condition on the rule, quantified over all g. The Q4 note
  (N7) reads it as fixing the local group: "under E1 (untransported offset) the local group at each
  site would be G_v". E1′ is that second reading: covariance in E1's form over those g with
  g_i b_i = b_i at every site.
- **E2.** The split of b_i into link offsets a_ij is not unique. At b = 0 the data space contains
  nonzero link offsets that sum to zero at every site.
- **E3.** The offset transforms as the field does. Other transformation laws for b, by a
  representation other than g itself, are variants. The Q4 note's hypothesis H-b ("the O-action of
  H-link acts on the offset as it acts on the field") is the global, O-action form of this choice.
- **All three.** The transformation class: all of AddAut V, or a subgroup such as the unitaries on the
  lift.

***

## §3 Evaluation criteria (fixed before the assessment)

The assessment fills one entry per extension for each criterion below. Block A is recorded and is
not scored: the decision rule (§4) reads blocks B–D and the controls, and reads A only through J5
and J6, as stated there.

### Block A — mathematical consequences (recorded, not scored)

- **A1. What the extension forces on b.** For E1, the set of b for which Cov_Ek holds. For E2 and
  E3, the transformation law of the rule offset b and whether any b is excluded. Cases: K = 1 and
  K ≥ 2; q odd, q even > 2, q = 2; finite carrier and lift; uniform and non-uniform b; S1.
- **A2. The Q4 stabilizer.** Glob_Ek(𝒢) is the set of constant g in a class 𝒢 that carry the rule
  to itself with the extension's data unchanged. This is Substratum:102's "global commutant
  symmetry", read for each extension's data. Classes 𝒢: AddAut V on the finite carrier; on the lift,
  Stage 2(d)'s U(K) and the Q4 note's G_0. Each entry is compared with the Q4 note's G_0 and G_v
  under its readings (L), (A-lin) and (A-aff), stating whether H-b and the resonance condition
  μ_{A₁} = 1 are used. Each entry also records whether the extension makes the Stage 2(d) object
  rule-level (as `A6Glob`, BackgroundIndependence.lean:111) or coupling-level (as Substratum:102),
  which is the Q4 note's open Q4b.
- **A3. The O5 boundary.** The local transformation class under which Cov_Ek holds with the
  extension's data transported, read from the extension's definition and compared with `A6Cov`'s
  class. No derivation of the A6 promotion, of a local SU(3)×SU(2)×U(1) or of a link action is made.
- **A4. Relations among E1–E3.** Whether two extensions induce the same transformation on the rule
  offset b, or coincide on a subclass.

### Block B — imported assumptions

- **The baseline 𝔅.** These are not counted as imported when used in the role they have on `main`:
  - `A6Cov` with its transformation class and transport, the adopted meaning of A6
    (Substratum:102; Main:726 item (xii); the `P1` A6 row of `verification/ROADMAP.md`);
  - the second-order form and the link-coupled form `linkF`;
  - A1–A4 (Substratum:92–98) and E4;
  - the affine rule class, which amplitude-scale gauge yields (Substratum:100, :270–274; SM:96,
    SM:240);
  - Q1 and Q2;
  - Theorem 7's decomposition (SM:374) and H-link, for block A only.
- **B1.** List every assumption the extension uses beyond 𝔅. For each, give its statement, where it
  appears at the pin (or "not in the corpus"), and its status there: posit, proved, conditional,
  owner decision, or none.
- **B2.** List every element of 𝔅 that the extension uses in a role it does not have on `main`, and
  count it as imported in that role. An example of the pattern: the additive typing `V →+ V` of link
  couplings, whose role on `main` is to carry linear rules, used to constrain an offset.

### Block C — independent physical justification

For each imported assumption of B1 and B2:
- **C1. Source.** The passage at the pin that motivates it, or a literature item marked [L] with the
  specific claim it is cited for. A file's presence on `main` is not a justification (§A.46 item 7).
  For a posit, its justification is its own stated motivation, classified like any other.
- **C2. Classification**, in the Stage 0 vocabulary:
  - **independent** — the stated motivation and its support do not presuppose T1, T2 or ¬T, and are
    not designed to exclude a particular construction (S1, or the class of offset-carrying rules);
  - **target-adjacent** — the motivation presupposes T1 or T2 (or ¬T), is logically equivalent to one
    of them on the rule class at issue, or is supported only by a consequence of one of them;
  - **target-defined** — the stated reason is to obtain T1 or T2, or ¬T; or to exclude a particular
    construction; or to eliminate (or retain) the offset;
  - **mixed** — an independent component together with a target-adjacent one, with each identified;
  - **none found** — no motivation located after the search of C3.
- **C3. Search record.** The corpus locations searched for a motivation, so that "none found" is
  backed by a corpus-wide search (§A.19).

### Block D — consistency

The grades are fixed in advance:
- **consistent** — no conflict;
- **tension** — the extension adds a property the source does not state, or carries the source's
  characterization outside the source's stated scope in a direction its wording does not cover;
- **inconsistent** — at the scope the source states, the extension asserts what the source denies,
  or contradicts a kernel statement.

- **D1. With the A6 sources at the pin:** Substratum:102; Main:726 item (xii); SM:104; SM:114–118;
  BackgroundIndependence.lean (module statement, and `A6Inv` :104, `A6Glob` :111, `A6Cov` :131,
  `a6cov_all` :161); A6Instantiation.lean (module statement, `pk3e_A5` :306, `pk5_symmetric_point`
  :366, `cx1_complex_covariance` :411, `cx2_unitary_gaugeLink` :459); the `P1` A6 row and section of
  `verification/ROADMAP.md`; and `verification/programmes/substratum/a6-status-adjudication/result.md`.
- **D2. With Q1.** The extension's statements must hold at Main's absolute interface. They must not
  depend on the relational readout classes 𝒜_C or 𝒜_W of the core file's §3.3.
- **D3. With Q2.** The extension must not give amplitude shifts, or any identification of rules that
  differ in b, physical gauge status without a justification. This includes the #1049 safeguard that
  the admissibility of site-dependent or time-dependent transformations "as OI gauge transformations
  must be established separately".
- **D4. With the preserved results (§A.29).** Stated in advance, these are the controls every
  extension must leave intact on its stated scope:
  - P1: `A6Cov` and `a6cov_all` on additive link data (C-LIN, §5.1);
  - P2: the kernel A6 statements listed in D1, on the linear class;
  - P3: the core file's controls C1–C8 (§1.2);
  - P4: the Q4 note's controls (C-a)–(C-c), on the linear class;
  - P5: Main:726 items (vii) and (xii) at their stated scope;
  - P6: S1's properties at SM:240.

  Contradicting any of P1–P6 at its stated scope is graded inconsistent.

***

## §4 Decision rule (fixed before the assessment)

**Per extension.** Ek is **independently justified** iff all of J1–J6 hold.

- **J1. Well-posed.** Ek is a predicate on stated data, with a stated transformation class and
  transport, on each carrier where it is assessed. Where its source text admits more than one
  reading (§2.4), each reading is assessed, and J5 applies to the set of readings.
- **J2. Linear limit.** Ek passes C-LIN (§5.1).
- **J3. Independent justification.** Every imported assumption (B1, B2) is classified
  **independent**, or **mixed** with an independent component that motivates it on its own. No
  imported assumption is target-adjacent, target-defined or none-found only.
- **J4. Consistency.** No entry under D1–D4 is graded **inconsistent**. Tensions do not fail J4, but
  each is named in the outcome.
- **J5. Hard to vary.** Consider each variant or reading of Ek (§2.4, plus any found in the
  assessment) that Ek's own justification supports equally well. No such variant may give a
  different A1 or A2 entry, unless that justification itself selects among the variants.
- **J6. Independent consequence (§A.29).** Ek has at least one consequence that goes beyond stating
  A6 for offset-carrying rules and beyond its A1 and A2 entries. That consequence must be checkable
  against a result at the pin that was not used to formulate Ek. A consequence that is T1, T2 or ¬T,
  or restates one of them, does not count.

**Conditional justification.** An extension that meets J1–J6 only given a named open hypothesis
(for example H-b) is listed in J_c with the hypothesis and its status (justified, posited or open).
J_c is reported with the outcome and is never counted into J.

**Outcome.** Let J be the set of extensions among E1, E2, E3 that are independently justified
unconditionally on the record at the pin.
- **(S)** |J| = 1: exactly one extension is independently justified. It is recommended for a
  separate owner decision after independent review. Nothing is adopted.
- **(M)** |J| ≥ 2: more than one is justified, and the choice stays open. No tie-break is applied.
  In particular, A1 and A2 entries are never used to rank members of J.
- **(N)** |J| = 0: none is independently justified. **(N) is a valid outcome.** It states that none of
  E1–E3 is independently justified on the record at the pin. It does not state that each is false,
  that no extension of A6 to offsets exists, or anything about A5's truth.

**What no outcome does.** None changes A5's status (owner, c.6719806528), adopts a premise, edits a
manuscript or ROADMAP row, or bears on O5. A6 remains `A6Cov` on `main` under every outcome.

**Verdict text.** For each extension, the per-extension verdict lists each J-clause as held or
failed, and for each failed clause names the finding (B, C or D entry) behind it. The outcome is
generated from |J| alone.

***

## §5 Controls

### 5.1 C-LIN — the linear-limit control (per candidate)

For each of E1, E2, E3 and the countercontrol E★, the following must hold on `A6Cov`'s own data
(b = 0; for E2, all link offsets a_ij = 0):
- Cov_Ek reduces to `A6Cov N M`;
- the transformation class is the same;
- the transport of M is `gaugeLink`.

A candidate that fails is not an extension of A6, and fails J2.

In addition, the following is recorded and not scored: whether Ek's data space at b = 0 is strictly
larger than `A6Cov`'s. For E2 this concerns the zero-sum link offsets of §2.4.

### 5.2 C-TI — the target-import check

The check: no criterion of §3 and no clause of §4 takes as a merit or a demerit whether an
extension yields T1, T2 or ¬T, or refers to the desired gauge group or to b = 0 in that role.

Permitted references are listed below. Each is outcome-neutral or exclusionary:

| Clause | Reference to b = 0 or to a group of T2 | Role |
|---|---|---|
| §1.2 | defines T1, T2, ¬T | naming, for exclusion |
| A1 | "what the extension forces on b" | recorded, not scored |
| A2 | G_0, G_v, U(K) | recorded, not scored |
| A3 | "no derivation of … a local SU(3)×SU(2)×U(1)" | scope exclusion |
| B (𝔅) | Theorem 7 for block A only | baseline, recorded |
| C2 | T1, T2, ¬T in the definitions of target-adjacent and target-defined | penalizes dependence on T, symmetrically for ¬T; never rewards attaining T |
| J5 | variants that change A1 or A2 | penalizes outcome-adjustability, in either direction |
| J6 | a consequence that is T1, T2 or ¬T does not count | exclusion |
| §4 (M) | A1 and A2 never used to rank | exclusion |
| C-LIN | b = 0 as `A6Cov`'s own data | control, identical for every candidate |
| E★ | the target, by design | countercontrol |

**Result at checkpoint 1 [D]:** no clause uses T1, T2 or ¬T as a merit or a demerit. The reviewer
re-checks this table against §3 and §4. At checkpoint 2 the reviewer also checks that no
per-extension verdict cites an A1 or A2 entry as its reason, except through J5 or J6 as worded.

### 5.3 C-CC — the countercontrol: a deliberately target-tuned extension

**E★ (stipulated offset identification).**
- **Data and covariance:** E1's data, and covariance in E1's form for g : ι → AddAut V.
- **The added stipulation:** two rules F_{M,b} and F_{M,b′} are declared the same physical rule, for
  all b and b′.
- **Justification offered with it:** "the offset would remove the singlet-block U(1) that
  Substratum:163 identifies as hypercharge, so it is unphysical."

On `A6Cov`'s data E★ reduces to `A6Cov` (C-LIN passes by design). Its rejection must therefore come
from the substantive clauses. The rule must reject E★. The clauses expected to reject it are listed
in advance:
- J3: the justification is target-defined (T2), and the stipulation exists to eliminate the offset;
- J4/D3: it identifies rules that differ in b without a justified gauge status. No time-independent
  relabelling linearizes S1 (SM:240), so the identification is not a relabelling;
- J4/D2: at Main's absolute interface S1 and its linear part are distinguishable (core file,
  Proposition 2.6(a));
- J5: variants that identify b only in the A₁ block, or only modulo a chosen subgroup, are equally
  supported and change A1 and A2;
- J6: it has no consequence beyond T.

### 5.4 When the verdict is void

- If C-TI fails at assessment, the affected clause is void. No outcome is rendered until a disclosed
  amendment repairs the clause (§6, I2).
- If E★ meets J1–J6, the rule is void and no outcome is rendered.
- If the assessment cannot evaluate a clause for some extension, the clause counts as not held for
  that extension. The reason is stated, and the outcome is qualified accordingly.

***

## §6 Invariants and their checkpoints (§A.41)

| # | Invariant | Checkpoint that measures it |
|---|---|---|
| I1 | The rule is fixed before any assessment exists | `git show --stat` of the checkpoint-1 commit lists exactly this file, and its parent is `9c201475` |
| I2 | The rule is unchanged after checkpoint 1, except by disclosed amendment | At checkpoint 2, `git diff <ckpt1> <head> -- DESIGN.md` is empty. Any amendment is a file under `q3-a6-offsets-20261108/amendments/`, states whether it was written after any assessment text, and is cited by the result |
| I3 | Every `File:N` and Lean line resolves at the pin | Reviewer reads each cited line with `git show 9c201475:<path>` |
| I4 | Paper only: no computation, code or Lean | `git diff --name-only 9c201475 <head>` lists only `.md` files under `q3-a6-offsets-20261108/`. The result states that every step was done by hand |
| I5 | No manuscript, ROADMAP or kernel change; A5's status unchanged | `git diff --name-only 9c201475 <head> -- papers book verification/ROADMAP.md verification/lean verification/lean-mathlib` is empty |
| I6 | No target import | C-TI table (§5.2) at checkpoint 1. At checkpoint 2, the reviewer checks the verdict text against it |
| I7 | C-LIN evaluated for E1, E2, E3 and E★ before J3–J6 | One C-LIN entry per candidate in the result |
| I8 | Countercontrol rejected | The result names the failing clauses for E★. If there are none, no outcome is rendered (§5.4) |
| I9 | (N) admissible; no tie-break | The outcome is computed from \|J\| alone, and the result contains no ranking of members of J |
| I10 | O5 boundary | Reviewer checks that the A3 entries are read from the definitions of E1–E3 only |
| I11 | Owner decisions quoted with author and time | The header of this file; repeated in the result |
| I12 | Off-main references traced | §7 here; the result carries its own trace |
| I13 | Neutral register | Reviewer scans the added lines for the §A.32 and §A.33 phrase families |

***

## §7 References not on `main` (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1049 c.6719806528 | authorization and its boundaries | support, by quotation with author and time (§A.42 item 7) |
| #1049 c.6624263637 | Q1, Q2 (D2, D3) | support, by quotation; also quoted on `main` in the core file §6 |
| #1169 c.6719386464 | the standard applied in C2 and J3 | support, by quotation |
| #1169 c.6719708521 (Stage 0 map; `STAGE0-MAP.md` is not on `main`) | context; the classification vocabulary of C2 | provenance. C2 defines every term it uses here, so no content of the map is relied on |
| #1083 (review records of the parent notes) | context | provenance |
| An earlier owner request relayed by the coordinating session ("compare E1–E3 against the existing A6 sources, identify which assumptions each imports, and recommend whether any extension is independently justified. It must not simply choose the extension that produces the desired gauge group") | guidance | provenance only. This drafting session did not locate its record. Its requirements are covered by c.6719806528, §A.29 and C-TI, and no clause rests on it alone |
| branch `research/a5-q3-a6-offsets-20261108` | this work | provenance |

***

## §8 Drafting disclosure

Before writing §3–§5, the drafting session read the core file in full, including N9's preliminary
pressure test of E1–E3 ("additivity relocated to the links, not derived") and its §5–§6, and the Q4
note in full, including N7's remark on E1. It also read the A6 sources listed in D1. The rule above
was therefore written with those partial analyses known. It is a preregistration of the rule, not a
rule written blind to prior work. No assessment of E1–E3 under this rule has been written.
