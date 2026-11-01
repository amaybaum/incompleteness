# MR-1 stage 1 — amendment MR★

**Status: append-only amendment, first section only.** The frozen preregistration
`../preregistration.md` at `1a236f332e8ea12b7fdb125bf8c5098ccd71d36c` is unchanged, and so are
`KS-substitution.md` and the existing entries of `stage1-log.json`. This commit contains §K★ alone.
It contains no candidate screen, no `𝔐★`, no `GAP` token, no `Acc` and no stage-2 interface. No
candidate interface was looked at, designed, derived or evaluated. No computation evaluating any
physical, candidate, control or algebraic quantity was run. The mathematics below is paper reasoning
from the frozen text, the Main anchors and the first-hand reading records, each item marked with its
status. This section is subject to independent review before use.

**Authority.** Stage-1 authorization, PR #1023 comment 6549252522 (owner), step 2: precommit `K★`,
including the independently justified concrete CC2 instance and its OI-held constraint, before any
candidate screen. KS substitution, owner Option 2, comment 6553497955: "An independently justified
concrete CC2 model, with its OI-held constraint, is established before `K★` is frozen"; "If that
construction cannot be justified, the literature gate stays unresolved. CC2 and the nonclassicality
criterion are not weakened."

***

## K★. Outcome: blocked

**`K★` is blocked: the CC2 instance cannot be constructed from the available first-hand sources
without an arbitrary choice.** The Kochen–Specker literature gate stays unresolved. `K★` is not
frozen. The CC2 row (frozen L569), the CC2-instance rule (L559–564), the nonclassicality criterion
(L529–536) and tokens 2.4 and 2.5 (L620–621) are unchanged. No candidate screen starts.

The missing elements are M1 to M4 (§K★.6). M1 is decisive by itself: within the frozen definitions,
no constraint OI holds at `D` selects an instance, and every instance K1 admits is an object of the
type the screen screens.

### K★.1 What the frozen text requires

- **The constraint set.** `K★ ⊆ {K1, …, K6}` (L330–336, L433–436). A member must be a constraint OI
  holds at `D`, cited and not chosen (Q1, L354–365).
- **K1** (L330–331): "the dynamics is the one fixed native `φ`, not a construction made per law".
  Under K1, "`π` and `μ` range over every admissible value (the classes of PC-1's fork rule)"
  (L358–359).
- **The CC2 instance** (L559–564): "fixed by a constraint that OI holds at `D`, cited under Q1's rule
  (§4.4), frozen with `K★` and before the candidate screen; at `D` only K1 qualifies. Under K1 the
  Kochen–Specker-type deterministic class contains `𝔐★`-type models (A1)".
- **The CC2 row** (L569): "a Kochen–Specker-type deterministic model with disturbing readout,
  extended by a disturbing marker". Its reference behaviour is "may return W1". It is separated from
  PC-Q by "a test named at stage 1 among T3, T5 and T6"; non-separation caps the law at `CONTEXTUAL`
  and is not a control failure.
- **CC8** (L575): the per-law A-realization of PC-Q's law (Main:482, Main:566), recorded as
  `CC8-unseparated`. CC2 must be distinct from it.
- **Commit order** (§7.1, L661–664): first `K★`, including the CC2 instance and the constraint that
  fixes it, and only then the screen.

### K★.2 Membership audit of K1–K6

This is a reading, not a freeze. By §7.1, `K★` is frozen together with its CC2 instance, and that
instance is blocked.

| Constraint | OI's holding at `D` | Anchor (Main at `D`) | Usable under Q1's rule |
|---|---|---|---|
| K1, one fixed native `φ` | held on its physical reading | Main:56 (Lemma 3: `φ` is a fixed bijection); Main:62 (finite reversible substratum, a posit) | yes |
| K2, causal-cone locality with measurement independence | relinquished as a conjunction: option (a), ontic parameter dependence, is the option taken | Main:414 | no |
| K3, one finite ontic cardinality for every menu | finiteness is held as a posit, with no bound on `N` | Main:62; Main:488; Main:560 | no: Q1 needs a stated bound (L371–374) |
| K4, generalized noncontextuality | not held: Main:566 clause (3) says Spekkens noncontextuality "is not claimed" | Main:566 (3) | no |
| K5, noninvasive measurability | not held: OI's instruments are invasive | Main:486 | no |
| K6, a bounded resource and reset budget | none stated; the word "budget" does not occur in Main at `D` | §2 inputs | no |

*Result (a reading of the anchors, agreeing with frozen §4.4):* only K1 qualifies. If `K★` were
frozen at `D`, it would be `{K1}`.

### K★.3 What a CC2 instance must specify

So that stage 2 could run it on the T-battery, an instance must specify all of the following:

- **(e1)** the ontic state space, including a carrier and a marker of joint effective dimension at
  least three; a two-path carrier with a two-level marker gives four;
- **(e2)** one dynamics;
- **(e3)** a deterministic readout map whose value may depend on the context, that is, on the
  co-measured readouts and the disposition of the apparatus;
- **(e4)** the post-readout ontic state, which is the disturbing readout;
- **(e5)** the marker's coupling to the carrier's ontic state, with its strength setting (T1), which
  is the disturbing marker;
- **(e6)** how settings enter (`Z`);
- **(e7)** how records and the outgoing carrier `Out` are produced, with every branch mass.

It must also meet four conditions:

- **(c-i)** be fixed by K1;
- **(c-ii)** be distinct from CC8;
- **(c-iii)** be justified independently of every candidate and of the quantum benchmark;
- **(c-iv)** be of Kochen–Specker type: a model whose readouts admit no noncontextual value
  assignment on the menu it is run on, not merely one that carries context labels. An instance whose
  readouts admit a noncontextual assignment would be a weak instance in the role of CC1 or CC4.

### K★.4 Element-by-element sourcing

| Element | First-hand source | Status |
|---|---|---|
| (e3), the context-dependent deterministic outcome, structural form | Bell 1966 p. 451 (LIT-4, B-c), with the §V diagnosis that the result "may reasonably depend … on the complete disposition of the apparatus"; Mermin p. 24 (M-c) in its all-rays form, covered by Bell | sourced. The only sourced construction is ψ-ontic: its thresholds are quantum expectations in ψ, and the threshold order is fixed by the set of projectors but not specified (REV-3) |
| (c-iv) over all rays, `d ≥ 3` | Bell 1966 §V (B-b), a continuity argument over all vectors | sourced, for value assignments to all rays only |
| (c-iv) on a finite menu | Mermin's square (M-b), the product rule and M-c restricted to a finite menu; Kochen–Specker 1967's finite set (pp. 69–87) | blocked: Mermin's errata are unread (REV-1, REV-4), and those Kochen–Specker pages are unread (LIT-3) |
| (e4), the post-readout ontic state | none. Bell gives no measurement dynamics ("we enter upon it no more than is strictly necessary"); Mermin treats disturbance conceptually only (p. 3) | unsourced (LIT-4-C1, LIT-5-C1) |
| (e5), the marker and its coupling | none. No marker, record system or sequential readout appears in either source | unsourced (LIT-4-C1, LIT-5-C1) |
| (e1), dimension | Bell §V ("it is here that we need three dimensions at least"); Mermin fn 11–12 | sourced; carrier ⊗ marker meets it |
| (e2) with (c-i) | K1 (L330–331) | fixes `φ` only (§K★.5) |
| (e6), (e7) | none in the sources. Within MR-1 they are elements of the §3.1 tuple | unsourced |

### K★.5 The K1 tension

*Status: derived on paper here from the frozen text (L330–331, L356–359, L561–563), Main:488 and the
records of PC-1 at `99dce4b6`.*

1. **K1 fixes one element of the tuple.** It fixes the dynamics, `φ` = the native rule (for the wave
   step, `ψ(x, y) = (Ax − y, x)`, §PC★2a at `99dce4b6`). Under Q1, `π` and `μ` range over the
   admissible classes of PC-1's fork rule, which contain at least two inequivalent members by
   construction (L137–140). The partition of `S`, `Z`, `ρ`, the marker region and its coupling, `Acc`,
   `Out` and `Res` are fixed by no constraint OI holds at `D`, and §K★.2 finds no second qualifying
   constraint. K1 therefore fixes a class, the K1 class, and not an instance.
2. **Every instance in the K1 class is an object of the screen's type.** An instance with a readout
   and a marker on the native `φ` is a record-forming interaction on the native rule: the object
   type of `𝔐★` (L134, L433, L562–563 by A1). Selecting one means choosing a carrier, a marker region,
   a readout and `(π, μ)` on the native rule. That is the act of designing a candidate-type interface.
   Step 2 of the authorization and the boundaries of comment 6553497955 place it after a reviewed
   `K★`. The selection would also be a free choice with no OI-held constraint behind it, which is
   what L561–562 rule out.
3. **No source supplies a native marker coupling.** PC-1 recorded that no screened native source
   supplies a physically executed register operator of the required kind (§PC★4, obstruction G★
   item 3). That finding is scoped to its sources and candidates and is not a no-go (N4). It is
   noted here only because it removes the one place where a sourced native marker could have been
   found.
4. **K1-fixed instances run on finite menus, which blocks (c-iv).** A fixed finite `S` with a fixed
   prior and a fixed bijection supports only finitely many distinct action-labelled conditional
   families (Main:488). So the menu of any instance is finite. Bell's B-b concerns value assignments
   to all rays and does not certify (c-iv) on a finite menu. Only a finite-set theorem could, and
   every such theorem available here is blocked (§K★.4).

Together, items 1–4 mean that no instance meets (c-i), (c-iii) and (c-iv) without a free selection
before the screen. This is the tension the frozen text records at L562–564. Its class-level
consequence, a ceiling of 2.5 with `CC2-unseparated`, is already part of the frozen rule and is not
changed here.

### K★.6 Constructions examined, and why none is admitted

None of these was evaluated on any test, and no law of any of them was derived. Each is excluded by
how it is sourced or fixed, not by how it behaves.

- **C-a: Bell-type, ψ-ontic, with the quantum update.**
  - *The construction:* Bell's p. 451 threshold rule over carrier ⊗ marker; ψ carried in the ontic
    state and moved by the battery's quantum operations; the post-readout state given by the
    quantum update; the marker coupled by PC-Q's controlled unitary.
  - *Its standing:* it is fully specifiable and is the strongest construction available.
  - *Why it is not admitted:*
    - every rule in it is a rule of the quantum benchmark, so its law is defined from the
      benchmark, which (c-iii) excludes;
    - its dynamics is not the native `φ`, and its ontic state carries amplitudes (P-set, A2;
      Corollary U3), so it is not fixed by an OI-held constraint (REV-3);
    - the finite threshold-order realization of this kind in the corpus is Main:566 (clause (3):
      "an outcome's value can depend on the instrument through the threshold order"), which is
      CC8's realization (L575). C-a would therefore duplicate CC8's role, contrary to (c-ii).
- **C-b: Bell-type with a fixed reference.**
  - *The construction:* thresholds taken from one fixed reference distribution rather than from ψ.
  - *Why it is not admitted:*
    - this removes ψ-dependence, but leaves free choices that no first-hand source sources: the
      order within a context (Bell fixes only that the order depends on the set of projectors),
      the post-readout update (e4), the marker map and its strength family (e5), and the
      assignment of preparations to distributions of the hidden variable;
    - its contexts are still the orthonormal bases of the quantum description;
    - it is not the native `φ`, so it is not fixed by K1;
    - each free choice changes behaviour under T3 and T5, so admitting it would fix adjustable
      structure by choice, which §A.29 forbids. Fixing a reference distribution on the grounds
      that it is "canonical" would be a posit, not a first-hand-sourced element.
- **C-c: an instance in the K1 class.**
  - *Why it is not specified:* §K★.5 items 2 and 4.

### K★.7 Missing elements

- **M1, selection within the K1 class (decisive).** No constraint OI holds at `D` and no
  first-hand source selects one instance among the native-rule interfaces with a readout and a
  marker. Any selection is a free choice of a candidate-type object before the screen (§K★.5).
- **M2, disturbing readout (e4).** No first-hand-sourced form exists for the post-readout ontic state
  of a Kochen–Specker-type deterministic model (LIT-4-C1, LIT-5-C1).
- **M3, disturbing marker (e5).** No first-hand-sourced form exists for a marker, its coupling to the
  ontic state, or its strength family (LIT-4-C1, LIT-5-C1; KS-S §4).
- **M4, finite-menu certification of (c-iv).** Bell's B-b covers all rays only. Every finite-set
  result available here is blocked: Mermin's square, the product rule and the finite-menu form of
  M-c await the errata, and Kochen–Specker 1967 pp. 69–87 are unread. Dimension is not the obstacle,
  since carrier ⊗ marker has four.

### K★.8 What would unblock it

None of the following is adopted here. Each is for the owner to decide on #1023.

**Sources**
- The text of Mermin's errata (*Rev. Mod. Phys.* 88, 039902 (2016); 89, 049901 (2017)), or
  Kochen–Specker 1967 pp. 69–87, read first-hand. Either would unblock M4 for the finite set it
  certifies.
- A first-hand source giving a sequential deterministic contextual model with a disturbing readout
  and a memory or marker, for M2 and M3. The following are bibliographic pointers only. They have
  not been read, their content is not asserted, and that they supply M2 or M3 is not claimed:
  - Bohm's measurement theory, *Phys. Rev.* 85, 180 (1952). It is ψ-ontic, so M1 would remain.
  - The literature on the memory cost of sequential contextuality, for example Kleinmann, Gühne,
    Portillo, Larsson and Cabello, *New J. Phys.* 13, 113011 (2011).

  A model built to reproduce quantum statistics is defined from the benchmark, so a source alone
  does not resolve M1.

**Owner decisions**
- **D1.** A stated selection principle for the CC2 instance within the K1 class. It would accept that
  the instance is an interface of `𝔐★`'s type fixed before the screen, and would state how the screen
  treats it.
- **D2.** A posited CC2 form outside K1, recorded as posited and as not fixed by an OI-held
  constraint. This departs from L561–562 and needs its own append-only, reviewed amendment.
- **D3.** CC2 kept at class level, with no instance, so that every positive axis-2 token carries
  `CC2-unseparated` and 2.4 is unreachable. This changes the stage-1 obligation at L559–562, which is
  procedure, while the criterion stays unchanged or stricter. It needs an owner amendment.

### K★.9 Requirements that any later instance preserves (§A.29)

Whatever unblocks K★, the instance it yields is admitted only if:

- it keeps the CC2 row, the nonclassicality criterion and tokens 2.4 and 2.5 unchanged;
- it is distinct from CC8 (c-ii);
- every element (e1)–(e7) is fixed, with its reason, before the screen;
- no element is chosen by reference to a candidate, to PC-Q's law or to a desired outcome;
- it names, at stage 1, its separating test among T3, T5 and T6;
- it carries its (c-iv) argument from a source read first-hand.

### K★.10 Commands and hygiene runs for this section

- **Read-only commands:**
  - `git rev-parse HEAD` (`a9bdeca24f038b592d8a5880e64f2facd7c5f7ab`), `git status`, `git log`;
  - `git show 5914c17c:papers/Main.md | sed -n` over Main:44, 56, 60, 62, 368–372, 408–410, 414,
    418, 482, 486, 488, 560 and 566–574, and `grep` of the same text for "contextual", "Spekkens" and
    "budget";
  - `git show 99dce4b6:…/PC-star.md` with `grep` and `sed -n` over §PC★2 and §PC★4;
  - display of the frozen preregistration, `KS-substitution.md`, `stage1-log.json` and the
    off-repository reader records for LIT-3, LIT-4 and LIT-5.
- **Hygiene, run 1 (on the staged draft of this file):**
  - `python3 -I tools/artifact_placement_check.py`: exit 0, "OK (no unaccounted root artifact; 95
    name(s) permitted, self-test passed)";
  - `python3 -I tools/lean_manuscript_census.py`: exit 0, "OK (every cited identifier and path
    resolves, …; complete relative to the maintained registry)";
  - `python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py`:
    exit 0, verdict `PASS`, "added-text scan: 0 hit(s)". That scan diffs `*.md` and `*.py` against
    its fixed base, so it covered this file. It does not cover `stage1-log.json` (REV-6), which was
    checked by a `grep` for local paths instead.
- **Hygiene, run 2 (on the staged final content):** the same three tools, then
  `git diff --cached --stat 1a236f33 -- ../preregistration.md` and the single commit. This run is
  declared here before it is made. Its outcome is stated in the commit message, since recording it
  in this file would change the file.

### K★.11 Review corrections

**Source.** Independent review of `3d475935` (verdict: accept with changes), relayed by the
coordinator. The review agrees that the block is genuine: L561–562 require the OI-held constraint
itself to fix the CC2 instance, and K1 fixes only `φ`.

**How to read this section.** The text above is kept as written, and the corrections below
supersede the passages they name. This section is numbered K★.11 because the requested number,
K★.9, is already taken. Each item was checked against its source before it was applied, and all
seven are applied.

- **RC-1. M1's grounding (§K★.5 item 2, second-to-last sentence; §K★.7 M1).**
  - *What is withdrawn:* the sentence "Step 2 of the authorization and the boundaries of comment
    6553497955 place it after a reviewed `K★`." It overreads the authorization. L562–564 already
    anticipate a CC2 instance of `𝔐★`'s type under K1, and the ordering rule (§7.1, L661–664)
    forbids only screening before `K★`.
  - *M1 now reads:* no constraint OI holds at `D`, and no first-hand source or independent
    justification, selects one instance within the K1 class. L561–562 require the OI-held constraint
    to fix the instance. K1 fixes only `φ`, leaving the partition, `ρ`, the marker region and
    `(π, μ)` free. So every K1 instance requires a free choice.
  - *Effect on the outcome:* none. The block rests on this alone.
- **RC-2. Scope of M2 and M3 (§K★.4, rows (e4) and (e5); §K★.7 M2 and M3).**
  - *On the K1 route:* once the carrier and marker regions and the readout are chosen, the native
    `φ` supplies both the post-readout state and the marker coupling, since every operation is a
    composition of `φ`-steps (L134–136). On this route M2 and M3 are not literature gaps; they
    reduce to M1.
  - *As literature gaps:* M2 and M3 apply only to forms that are not native, such as C-b, where the
    update and the marker map would have to come from a source.
- **RC-3. Condition (c-iv) (§K★.3).**
  - *Its status:* (c-iv) is this section's reading, not frozen text. The frozen reference behaviour
    of CC2 is "may return W1" (L569), and LIT-5-C3 reads "Kochen–Specker-type" as contextual
    deterministic. (c-iv) is relabelled a **proposed reading for the owner**.
  - *A conflation, removed:* the sentence calling an instance that admits a noncontextual value
    assignment "a weak instance in the role of CC1 or CC4" conflates two notions. Kochen–Specker
    noncontextuality of value assignments is one; generalized (Spekkens) noncontextuality, the
    notion by which CC1 and CC4 are characterized (L559–560), is the other. The sentence is
    withdrawn.
  - *Effect on M4:* M4 holds only under the proposed reading. The block stands on M1 regardless.
- **RC-4. The native step (§K★.5 item 1).** The text gives `ψ(x, y) = (Ax − y, x)` as the native
  step, but that is its inverse. Per §PC★2a at `99dce4b6`, the native step is
  `φ(u_prev, u) = (u, A u − u_prev)`, and P-1 there proves that `ψ` is its inverse.
- **RC-5. The fork's two legs (§K★.5 item 1).** "At least two inequivalent members by construction"
  holds only on the fork's invariance leg (L139–140; PC-1 preregistration §4 at `99dce4b6`: "A leg
  taken under invariance must have at least two inequivalent admissible members"). A leg fixed by a
  selection principle carries its necessity assessment instead. The statement is scoped to the
  invariance leg. M1 is unaffected: on either leg, `(π, μ)` is not fixed by K1.
- **RC-6. The finite-`S` premise (§K★.5 item 4).**
  - *The premise:* Main:488 assumes a finite `S`. For OI that finiteness is the total-finiteness
    posit (Main:62).
  - *Where it does not apply:* §PC★2a at `99dce4b6` also allows the value groups `ℤ_p` and `ℝ/ℤ`, on
    which `S` is not finite. There Main:488 does not apply as stated, and the finiteness of the menu
    is not established here.
  - *Scope of item 4:* it holds for finite `S` under Main:62. Since it bears only on M4, which RC-3
    already makes conditional, the block is unaffected.
- **RC-7. D3 (§K★.8).** D3 removes only the obligation to fix an instance (L559–562). The class-level
  ceiling, 2.5 with `CC2-unseparated`, is already frozen at L563–564 and is not introduced by D3.

**Hygiene for this section.**
- *Run 3 (on the staged draft):*
  - `python3 -I tools/artifact_placement_check.py`;
  - `python3 -I tools/lean_manuscript_census.py`;
  - `python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py`.

  Results are recorded in `stage1-log.json` under `kstar_corrections`.
- *Run 4 (on the staged final content, before the single commit):* the same three tools, then
  `git diff --cached --stat 1a236f33 -- ../preregistration.md` and `git diff --cached -U0` as the
  deleted-line check. This run is declared before it is made, and its outcome is stated in the
  commit message.

### K★.12 Pointers

- **D3.** Owner decision D3 (PR #1023 comment 6554185786; amendment `D3-CC2-class-level.md`) removes
  the CC2-instance obligation that blocked `K★` under M1 (§K★.7, as restated in §K★.11 RC-1).
  - *`K★` under D3* would be `{K1}`, with CC2 at class level and no instance (§D3.4 there).
  - *It is not frozen.* Freezing `K★` is a separate owner decision.
- **REV-8.** Correction REV-8 in `stage1-log.json` (under `lit5_errata`) changes §K★.8's two Mermin
  errata to three: *Rev. Mod. Phys.* 85, 919 (2013); 88, 039902 (2016); 89, 049901 (2017).

### K★.F — K★ frozen (owner decision)

**Decision and source.** Owner decision, PR #1023 comment 6554399670 (created
2026-11-01T06:23:32Z). It was given in the coordinating session's chat, replying to comment
6554387397.

- **The decision:** once CI is green on the exact commit, and provided the reviewed amendment is
  unchanged, freeze `K★ = {K1}`, "the single native OI dynamics constraint".
- **CC2:** retained as the full classical comparison class, not an arbitrarily selected model.
- **Nonclassicality:** token 2.4 stays unavailable, and the contextuality ceiling stays explicit.
- **The owner's words:** "Only after that freeze should the paper-only candidate search begin. The
  goal is still to find a physical measurement mechanism arising from OI itself, rather than
  reproduce quantum predictions by construction."

**Conditions, verified by this writer with read-only GitHub connector calls.**

- **CI:** workflow run 41279841361 (`verify`, event `pull_request`) has `head_sha`
  `dbf78a86d38d80827c46a49a5c601d2a2e6ae6f8`, status `completed` and conclusion `success`. It was
  updated at 2026-11-01T06:21:38Z.
- **Unchanged reviewed head:** PR #1023's head is `dbf78a86d38d80827c46a49a5c601d2a2e6ae6f8`. That is
  the commit the independent reviewer accepted, and this freeze commit's parent. No change followed
  the review.
- **The reviewed amendment itself** (`D3-CC2-class-level.md`, with §D3.9) is unchanged at that head.

**The freeze: `K★ = {K1}`.**

- **K1, frozen L330–331, verbatim:**

  > **K1** the dynamics is the one fixed native `φ`, not a construction made per law (the battery
  > freezes `π` and `μ` for `𝔐★`; Q1 lets them range over their admissible classes, §4.4);

- **The native step:** `φ(u_prev, u) = (u, A u − u_prev)`, with `A` the neighbour sum `a·Σ_{j∼i}` on
  a finite site set and the value group as stated there (§PC★2a at `99dce4b6`). P-1 there proves it
  a bijection, with inverse `ψ(x, y) = (A x − y, x)`.
- **Not a per-law construction:** it is one fixed bijection, the same for every law the battery
  examines (Main:56, Lemma 3). It is not built from a target law, unlike CC8 (L575; Main:482,
  Main:566).
- **Under Q1:** "Under K1, `π` and `μ` range over every admissible value (the classes of PC-1's fork
  rule), not the frozen pair of `𝔐★`." (frozen L358–359).

**K2–K6, excluded (from §K★.2).**

| Constraint | Why it is excluded | Citation |
|---|---|---|
| K2 | relinquished as a conjunction: option (a), ontic parameter dependence, is the option taken | Main:414 |
| K3 | finiteness is a posit, with no bound on `N`; Q1 needs a stated bound (L371–374) | Main:62; Main:560 |
| K4 | Spekkens noncontextuality "is not claimed" | Main:566 clause (3) |
| K5 | OI's instruments are invasive | Main:486 |
| K6 | no resource or reset budget is stated; "budget" does not occur in Main at `D` | §2 inputs; Main at `D` |

**CC2 and the tokens, per D3 (`D3-CC2-class-level.md`).**

- **CC2 is kept at class level.** The class is the L569 description, unrestricted, and under K1 it
  contains `𝔐★`-type models (L562–563). No instance is fixed, no separating test is named, and CC2
  is not executed; its separation fields are "not separated (class level, D3)".
- **Token 2.4 is unreachable.** Token 2.5 is the ceiling on axis 2, with `CC2-unseparated` and
  `CC8-unseparated`.

**Timing.**

- **The freeze precedes every candidate law.** No candidate law has been derived or considered, on
  paper or otherwise. No candidate interface appears in any record of this unit, and this writer has
  looked at, designed or derived none.
- **The frozen requirements this meets:** 0(iii), "`K★` fixed after any candidate law has been
  derived"; 0(vi), "a paper derivation of a candidate's law before `K★` and the battery definitions are frozen"; and the
  checkpoint at L712, "`K★` frozen before any candidate law is derived".
- **Next step:** the paper-only structural screen under frozen §3–§7 and D3. It ends in one fully
  specified `𝔐★` or a scoped `GAP`, with the stage-2 interface frozen. It is not started in this
  commit, and it follows independent review and CI of this freeze (comment 6554399670).

**Hard to vary (§A.29).**

- **No adjustable element.** `K★` has one member. That member's only content is the fixed native
  rule, and `π` and `μ` range over admissible classes rather than being chosen. Nothing in `K★` can
  be tuned to an outcome.
- **No later change.** Any change to `K★` after this commit, whether before or after any outcome,
  voids the run under 0(iii).
- **Re-admitting 2.4** needs a new, independently reviewed amendment that supplies a CC2 instance:
  an OI-held selection principle or an independently justified instance from new first-hand sources
  (§K★.7 M1, as restated in §K★.11 RC-1). Under L561–562 such an instance belongs to `K★`, so it
  cannot be introduced after this freeze without voiding the run.

**Commands and hygiene.**

- **Read-only GitHub connector calls:** the comment page of PR #1023 holding 6554399670; workflow
  run 41279841361; PR #1023's head.
- **Git:** `git rev-parse HEAD` (`dbf78a86`).
- **Hygiene runs F-1 (staged draft) and F-2 (staged final content, then the single commit):**
  placement, census and SC-42. F-1's results are in `stage1-log.json` under `kstar_freeze`. F-2 is
  declared there before it is made, and its outcome is stated in the commit message.

### K★.F note — wording of the hard-to-vary clause (review nit)

**Source.** Independent review of the freeze commit `e16017d6` (accepted), relayed by the
coordinator. The text above is kept as written; this note states how two of its sentences read.

- **What overstates.** Under "Hard to vary", the sentence "Any change to `K★` after this commit,
  whether before or after any outcome, voids the run under 0(iii)" cites 0(iii) for more than it
  says. Frozen 0(iii) (L594–596) voids `K★` "chosen or changed after any outcome", and "`K★` fixed
  after any candidate law has been derived, on paper or otherwise". It does not void a change made
  before any outcome and before any candidate law.
- **The stricter rule, restated as this freeze's own commitment.** `K★ = {K1}` is not changed after
  this commit, before or after any outcome. That is a commitment of this freeze, not a consequence
  of 0(iii). A change made before any outcome and before any candidate law would breach the
  commitment; it would need its own reviewed owner amendment, and the record would name the breach.
  A change after any outcome, or after any candidate law, is void under 0(iii) as frozen.
- **The same reading applies** to the next bullet ("cannot be introduced after this freeze without
  voiding the run"), and to the mirror sentence in `stage1-log.json`, field
  `kstar_freeze.hard_to_vary`. That file is append-only and is not edited.
- **Unchanged:** `K★ = {K1}`, its membership reading, CC2 at class level and the timing record.

**Hygiene for this note:** placement, census and SC-42 on the staged note, then the single commit.
Their outcome is stated in the commit message.

## S. Structural screen (paper-only)

**Status.** Append-only. This section screens the candidate sources of a record-forming
interaction under the frozen §3–§7, amendment D3 and `K★ = {K1}` (§K★.F). It is paper-only:
- it derives no record law, of any candidate or control;
- it evaluates no T-test, no control and no countercontrol;
- it runs no computation.

Each mathematical item carries its status: **proved here** (on paper, in this section), **cited**
(with anchor), or **reading** (an interpretation of a cited text, open to review). `Main:N`, `SM:N`
and `Substratum:N` are lines of `papers/` at `D` = `5914c17c`. Frozen line numbers `L…` refer to
`../preregistration.md` at `1a236f33`. The fixing of `𝔐★` or of the `GAP` token, and the stage-2
interface, are in §M.

**The standard applied throughout** (frozen L37–43, §3.4, §5.3). An operation counts only if it is
**available**: a finite composition of `φ`-steps on the declared state, under the declared access,
with a sourced setting. A mathematical inverse, a supplied decoder or a map that exists only as a
representation is not an allowed continuation without its native implementation (#866; frozen
L193–194, L451–452). A setting change needs a sourced operation, because the controlled lift
`F(x, s) = (T_s x, s)` conserves `s` (N7).

### S.1 What K1 fixes

- **The step** (§K★.F). `φ(u_prev, u) = (u, A u − u_prev)` on `S = 𝐑^Λ × 𝐑^Λ`, with
  `(A u)_i = a Σ_{j∼i} u_j`. The value group `𝐑` is `ℤ/q`, `ℤ_p` or `ℝ/ℤ` (§PC★2a at `99dce4b6`).
  The map is additive (P-2) and fixes the zero configuration (P-3).
- **The graph** (reading). The native coupling graph is the simple-cubic lattice (Main:726, posit
  (x)). The step's form is SM's form lemma: SM:224 for nearest neighbour, centre-free, isotropic
  and linear. The graph is a finite periodic lattice (Substratum A3–A4, Substratum:96–98).
  - §PC★2a proves P-1 to P-3 for any neighbour relation. That generality is a proof generality.
  - A graph chosen for a purpose (a waveguide, a cavity, a junction) would be a per-design
    construction, which K1 excludes ("not a construction made per law").
- **The coefficient** (reading). The microscopic coefficient is the integer `a = 1`: the
  unnormalized update of SM's Theorem A.1 ring rule and of the lattice code cited by SUBSTATE-1.
  - The normalization `α = 1/d` belongs to the observer-level operator (SM §4.1, Scope).
  - Where `1/3` exists in `ℤ/q` (`3 ∤ q`), it is a unit.
  - So for every coefficient the corpus uses, multiplication by `a` is injective on `𝐑`.
- **Linearity is an axiom of the substratum construction** (cited). Substratum A5 (Substratum:100)
  states it, and calls it "partly derived" through amplitude-scale gauge (Substratum:270–274).
  - The step governs the full local lattice sector: "Visible and hidden lattice degrees of freedom
    in that sector run the same wave equation" (Substratum:48).
  - The coupling matrix is scalar, `M = μI` (SM:428).
  - So the K1 step is a free field: it has no interaction term between any two regions.

### S.2 Structural lemmas

Notation. A declared partition of the sites into regions `X` (each region carrying both slices)
gives `S = ⊕_X S_X`, with inclusion `ι_X` and projection `pr_X`. `Σ` is the carrier region, `A` the
apparatus or marker region, `E` the environment, `Z` the setting source and `L` the ledgers.

**S-L1 (superposition; proved here).** For all `t` and all regions `X`, `Y`,

    pr_Y φ^t (s) = Σ_X Φ^t_{YX}(s_X),   with   Φ^t_{YX} = pr_Y ∘ φ^t ∘ ι_X.

Each `Φ^t_{YX}` is a homomorphism that depends on `(t, X, Y)` only. *Proof.* `φ^t` is additive
(P-2) and `s = Σ_X ι_X s_X`. `□`

**S-C1 (no conditional dynamics; proved here, from S-L1).** Changing `s_Z` by `δ` changes every
region `Y` at time `t` by `Φ^t_{YZ}(δ)`, whatever the other regions hold. Hence:
- **(a) No selection of operations.** No internal setting, program register or marker selects or
  modulates the operation applied to the carrier. The carrier's contribution to every region at
  every time is `Φ^t_{YΣ}(s_Σ)`: the same homomorphism for every value of every other region. A
  setting enters only as an additive offset.
- **(b) Every record is a post-processing of one fixed map.** Every record an observer region `V`
  holds is a function of the one fixed map `s ↦ (pr_V φ^t s)_{t ≤ T}`. Readouts that depend on a
  setting held in `V` are post-processings of that map, so all of them are coarse-grainings of one
  joint record.
- **(c) No adaptive operation.** No record-conditioned operation on the carrier exists: it would
  make the carrier's transfer depend on another region's state, contrary to (a).

**S-L2 (available operations; from the frozen standard and S-C1).** The available transformations
of the joint state are the time shifts `φ^n`, `n` within the budget. Observer-side choices change
only which region and tick are read. The set `{φ^n}` is commutative, since `φ^m φ^n = φ^{m+n}`.
SUBSTATE-1's operational-control countercontrol at `8af2d904` (provenance) records the same point:
time shifts have an abelian image.

**S-L3 (time reversal is representable, not available; proved here).** Let `σ(x, y) = (y, x)`.
- **`ψ = σφσ`.** `σφσ(x, y) = σφ(y, x) = σ(x, A x − y) = (A x − y, x) = ψ(x, y)`, the inverse of
  P-1.
- **`σ` is not a time shift.** If `σ = φ^k`, then `σ` commutes with `φ`, so `φ^{−1} = σφσ = φ` and
  `φ² = id`. Now `φ²(x, y) = (A y − x, A(A y − x) − y)`.
  - Equality with `(x, y)` at `y = 0` gives `2x = 0` for every `x`.
  - Then `A y = 2x = 0` for every `y`, so `A = 0`.
  - With `a` injective and a nonempty neighbour relation, `A ≠ 0`, so `σ` is no time shift.
- **No region executes `σ` on another** (S-C1(a)).
- **On finite `S`, `φ^{−1} = φ^{N−1}`,** where `N` is the order of `φ`. So the inverse is executed
  only as a global wait of `N − 1` steps, which acts on every region, the observer included (S-L6).

**S-L4 (no confinement; proved here).**
- **Hypotheses.** `Λ = ℤ^d` with nearest neighbours, and multiplication by `a` injective on `𝐑`.
  Let `(u_t)` solve `u_{t+1} = A u_t − u_{t−1}`, with `(u_{−1}, u_0) ≠ 0` of finite support.
- **Claim.** Fix an axis `e`, a width `w ≥ 1` and an offset `b`. If every `u_t` with
  `−1 ≤ t ≤ T` is supported in the slab `{i : b ≤ i·e ≤ b + w − 1}`, then `T ≤ 2w − 1`.

*Proof.* Write `f(t) = max{i·e : u_t(i) ≠ 0}`, with `f(t) = −∞` when `u_t = 0`. Let `C(t)` be the
condition "`u_t ≠ 0` and `f(t−1) ≤ f(t)`".
1. **`C(t)` implies `f(t+1) = f(t) + 1`, and hence `C(t+1)`.** Put `F = f(t)` and pick `v` with
   `v·e = F` and `u_t(v) ≠ 0`. Take `i = v + e`.
   - Every neighbour of `i` other than `v` has `·e ≥ F + 1`, so `u_t` vanishes there.
   - `u_{t−1}(i) = 0`, since `F + 1 > f(t−1)`.
   - So `u_{t+1}(i) = a·u_t(v) ≠ 0`.
   - At every site with `·e ≥ F + 2`, every term vanishes.
2. **If `u_s = 0` for some `s ≥ 0`, then `C(s+1)`.** `(u_{s−1}, u_s) = φ^s(u_{−1}, u_0) ≠ 0`, so
   `u_{s−1} ≠ 0`, and `u_{s+1} = −u_{s−1}`.
3. **Counting.**
   - *Case 1: some `t ∈ {0, …, T}` satisfies `C(t)`.* Let `t_0` be the least such `t`. Before it,
     every nonzero `u_t` has `f(t−1) > f(t)`, and by step 2 at most `u_{t_0−1}` vanishes. So
     `f(−1) > f(0) > ⋯ > f(t_0−2)` are at least `t_0` distinct values among `w` integers, and
     `t_0 ≤ w`. By step 1, `f(t_0 + k) = f(t_0) + k ≥ b + k`, which leaves the slab once `k ≥ w`.
     Hence `T ≤ t_0 + w − 1 ≤ 2w − 1`.
   - *Case 2: no `t ∈ {0, …, T}` satisfies `C(t)`.* Then `f(−1) > f(0) > ⋯ > f(T−1)` are `T + 1`
     distinct values among `w` integers, so `T ≤ w − 1`. `□`

*On the torus* of side `N ≥ 5w + 2`, no nonzero solution stays in a slab of `w` consecutive
residues for every `−1 ≤ t ≤ 2w`.
- Lift the initial pair to `ℤ^d` inside one period. By finite speed (Main's cone theorem, as
  quoted at SM:230), the lifted solution's slices up to `T` lie within the slab widened by `T + 1`
  on each side.
- By P-2 and translation covariance, the torus solution is the sum of the lifted solution's
  `N`-periodic translates.
- For `N ≥ w + 2(T + 1)`, those translates do not meet within the window. So the torus solution
  agrees there with the lifted one, which by the claim cannot stay in the slab up to `T = 2w`.

**S-C4a (no confined pointer; proved here, from S-L1 and S-L4).**
- *The branch difference is a free solution.* Let two carrier cells differ by `δ ∈ S_Σ`, with every
  other region equal. By S-L1, the two branches differ at time `t` by `φ^t(ι_Σ δ)`. That is a
  solution of the free step, whatever every other region holds.
- *No region confines it.* By S-L4, no region of width `w` along any axis confines that difference
  over `2w + 1` consecutive slices.
- *Consequence.* A record cannot be held as a confined pattern for longer than about twice the
  pointer's width, its light-crossing time.

**S-C4b (conserved linear quantities are global; proved here, `𝐑 = ℤ/q`, `a` a unit).**
- *Fixed points.* A fixed point of `φ` is `(u, u)` with `(A − 2I)u = 0`. Indeed,
  `φ(x, y) = (y, A y − x)` equals `(x, y)` exactly when `y = x` and `A x = 2x`.
- *Invariant functionals.* A homomorphism `c(u_prev, u) = c₁·u_prev + c₂·u` satisfies `c ∘ φ = c`
  exactly when `c₁ = −c₂` and `(A − 2I)c₂ = 0`. This follows by comparing coefficients in
  `c ∘ φ(x, y) = −c₂·x + (c₁ + A c₂)·y`, using `A = Aᵀ`.
- *Both are stationary solutions.* By S-L4 (any `T`), neither has a nonzero form supported in a slab
  of width `w` on `ℤ^d`, or on a torus of side `N ≥ 5w + 2`.
- *Consequence.* Every stationary configuration, and every `φ`-invariant linear functional, extends
  over at least `(N − 2)/5` sites along every axis. No local occupation is conserved.

**S-L5 (marking and interference loss are decoupled; proved here, from S-L1).**
- *The carrier's later state.* It is `Φ_{ΣΣ} s_Σ + Σ_{X≠Σ} Φ_{ΣX} s_X`. Likewise, any recombination
  region `D` receives `Φ_{DΣ} s_Σ` from the carrier.
- *Marking leaves the carrier's transfers unchanged.* A marker region that records the carrier
  (`Φ_{AΣ} s_Σ ≠ 0`) changes neither `Φ_{ΣΣ}` nor `Φ_{DΣ}`. The marker affects any later test of the
  carrier only through the offset `Φ_{DA} s_A`, which comes from its own initial content and does
  not depend on `s_Σ`.
- *In §3.5's terms.* (ii), loss of observed interference, can arise only by additive injection from
  regions whose content does not depend on the carrier. A record (R1) never causes (ii): marking is
  non-invasive, which is the CC1 kind.

**S-L6 (budget below recurrence; proved here).**
- On finite `S`, `φ` has finite order `N`, and `φ^N = id`. At `t_0 + N`, every region's state equals
  its state at `t_0`.
- If the observer's state at `t_0` does not depend on the carrier cell (a ready observer), it
  carries no information about the cell at `t_0 + N`.
- So R2 needs a budget below the period of the orbits in `μ`'s support. On finite `S`, every
  effective irreversibility of §3.5 (iii) is relative to such a budget.

**S-L7 (the epistemic-restriction sub-question of AW-MR5; proved here, conditional on the
access).**
- *The bracket.* For linear readouts `c = (c₁, c₂)` and `c′`, the bracket of `J` is
  `cJc′ᵀ = c₁·c₂′ − c₂·c₁′`. It is time-independent, because `MᵀJM = J` (AW-MR5).
- *Current-slice readouts are isotropic.* Any two readouts of the current slice (`c₁ = c₁′ = 0`)
  have bracket `0`.
- *Two conjugate pairs.*
  - The current and previous slice of one site, `(0, e_v)` and `(e_v, 0)`, have bracket `−1`.
  - The current slice of one site at two consecutive ticks, `(0, e_v)` and `(−e_v, A e_v)`, has
    bracket `1`.
- *Answer.* An access that reads the current slice at a single time is an epistemic restriction
  in Spekkens' sense: its readouts are isotropic. An access that reads both slices, or retains the
  earlier of two consecutive reads, is not.
- *Which slices the access reads is not fixed by the sources.* SM's companion realization takes
  the current field as visible and the retarded register as hidden (SM:252). So the answer is
  conditional on the declared access.

### S.3 The sources screened

Thirteen sources were considered. They are the native structures of the corpus that could form a
record or supply a setting, the constructions it uses in their place, and the candidates of the
preserved negatives. Every source keeps P-set, P-bij and P-obs, and none uses a fresh kernel or a
non-functional relation. So every source is **class A** (A1, A2). None is B, since no kernel's
randomness is a sourced, conditionally fresh latent resource (B2). None is C: none drops a premise.

**σ1. Native transport.** A carrier region is coupled to an apparatus or marker region by the free
step. This includes PC-1's Q1, the native interferometer read by a site detector. It is the one
native source with content, so its elements are identified one by one:

| Element (§3.1) | What the K1 step supplies | Status |
|---|---|---|
| `Σ` | a region of sites carrying the carrier's field, both slices | kinematics derived; partition posited |
| `A` | a region of the same free field; no dynamics of its own beyond transport (S-L1); no confined pointer (S-C4a); no amplifier gain, only linear fan-out | **unsourced as an apparatus** |
| `E` | every other site within the budget's causal cone | derived |
| `Z`, and how `s` changes | a region whose initial content is the setting. Unlike N7's lift, `s` is not conserved: its region radiates and receives like any other (S-L1). But no process writes a chosen value into it, and its value selects no operation (S-C1(a)). | no operation-selecting setting |
| `L` | a clock or ledger needs a confined periodic pattern; there is none (S-C4b). Timing ticks are global step counts, held by no subsystem. | unsourced |
| `R`, the record alphabet | values of `ρ` on `V`'s configuration at each tick. No heralding, failure or rejection process exists: `⊥` and attempt marks have no executing process, and `∅` is a coarse value (for example the zero value). | partial |
| `Out` | the carrier's continuation, `φ^t(ι_Σ s_Σ)` plus additive offsets. The same field carries the record (S-L1), so record and outgoing carrier coincide. | derived |
| adaptive operations; inverses | none (S-C1(c)). `σ` is not available (S-L3). `φ^{−1}` exists only as a global wait (S-L3, S-L6). | none |
| `μ`, `π`, fork | **μ leg.** Main Lemma 3's selection principle gives the counting measure (Main:56), under which every region's marginal is uniform, so there is no ready region. The zero configuration is fixed (P-3), and invariance does not select a law (`ensemble_underdetermined`, PC-1 §4 at `99dce4b6`). **π leg.** Readouts of `V`'s configuration; translation-related readouts count as one member (§PC★5). The fork is not resolved. | not resolved |
| dephasing; record process | dephasing only as additive injection from regions independent of the carrier (S-L5); recording only as transport | transport only |

**Call for σ1: G.** The decisive element is the apparatus pointer (S-C4a; §S.4(a) for the
remaining route). Q is not supplied, for two separate reasons:
- Q presupposes a measurement, and R is not sourced.
- Marking cannot cause interference loss (S-L5), and no subsystem undo exists (S-L2, S-L3, S-L6).

An additive offset can still act as a classical phase label, of the CC1 or CC4 kind. So Q fails
on the measurement and the undo, not on T0. That T0 fails is not claimed.

The other sources, with the element at which each fails:

| Source | Anchor | Elements and status | A/B/C | R/Q/G |
|---|---|---|---|---|
| σ2. Internal settings | Main:408; AW-MR7 | The setting is part of the initial state of a region `Z`. It enters additively (S-C1(a)), selects no operation, and folds into σ1's preparation. | A | G (no setting selection; no separate record mechanism) |
| σ3. Program register | Main:582 | `Φ(x) = φ_{π(x_vis)}(x)` selects the instrument from a register. That is a controlled map, contrary to S-C1(a) for one additive `φ`, and it is constructed per instrument family on Main:566's realization. | A | excluded: not the K1 step (CC8's class) |
| σ4. Exogenous action labels | Main:482 | The bijections `I_a` are applied between steps from outside, which is an external switch (frozen L134–136; N7). | A (A1, second clause) | excluded: not available |
| σ5. Controlled lift | N7 | An additive lift `F(x, s) = (Tx + Bs, s)` has `T` independent of `s` (S-C1). A lift with `s`-dependent `T_s` is not the K1 step. Either way, `s` is conserved. | A | excluded |
| σ6. Global recurrence | S-L3, S-L6; Main §2.3 | `φ^{N−1}` is executed by waiting, but it acts on all of `S`, erases every record including the observer's, and lies beyond any budget that R2 admits. A reversal of all of `S` is not an operation of an embedded observer (frozen L194–195). | A | excluded as an undo |
| σ7. Time-reversal swap | S-L3 | `ψ = σφσ`, so the inverse is representable; `σ` is not available. | A | representation only (CC6's class) |
| σ8. Global conserved and parabolic modes | S-C4b; SM Theorems A.1–A.2 | Invariants and accumulating modes extend over the torus. Reading them needs an observer of torus-wide support, contrary to `V ⊊ S` with bounded diameter (Main §4.6, scope (i)). An invariant cannot be written by the carrier. | A | excluded: no embedded readout |
| σ9. Per-law realizations | Main:482, Main:518–520, Main:566, Main:582 | These are built from a target law. | A | excluded: CC8's role |
| σ10. Engineered coupling graphs | §PC★2a generality | Such a graph is not the native graph (§S.1). S-L1–S-L3 and S-L5 hold on every graph, so Q stays excluded. S-L4 uses the cubic lattice, so trapping, and with it R, is the one capability an engineered graph could change. | A | excluded by K1; the scope boundary for R |
| σ11. Other value groups in K1 | §PC★2a; SUBSTATE-1 (`ℝ/ℤ`, `ℤ_p`) | S-L1–S-L3 and S-L5 hold. S-L4 holds when `a` is injective: `a = ±1` on `ℝ/ℤ`, and any `a ≠ 0` on `ℤ_p`, a domain. | A | as σ1: G |
| σ12. Non-additive native-type rules | native-Y's rule `U_{t+1} = U_{t−1} ⊕ H(⊕_{w∼v} U_t(w))` with `H(A, B, D) = (B, D, A ⊕ BD)` (on `main`, `native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md`); SM:104–106, state-dependent coupling graph; SM §6.5, dynamical links | These are outside `K★ = {K1}` as frozen: the `BD` product, a state-dependent graph and dynamical links are not the additive step. They are not screened for R or Q here. | A | outside K★; not screened |
| σ13. Candidates of the preserved negatives | N1–N7 | Respected at their scopes and not reopened. PC-1's Q1 is σ1's interferometer; its remaining candidates (Q2–Q12) and F2-1's rules are posits or representations, not K1 couplings, and their G★ item 3 concerns register operators, consistent with S-C1(b). N5 concerns the native-Y rule. N6 is a composition contract, not a source. N7 is σ5. N1 and N2 are not record sources. | — | as recorded in each unit |

For σ12, the units that worked with those rules recorded their own scoped results, which stand
unchanged:
- **native-Y.** Actual fields contain nonlinear products of the old sign with pool operands; no
  isolated available gate was found (`CURRENT-HANDOFF.md`).
- **SUBSTATE-1, at `8af2d904`** (provenance):
  - a clean single-register pair violates the preparation;
  - the raw echo is masked;
  - a native random setting fails the distinct-interaction test;
  - the audited passive-native and read contract supplies no selectable setting operation.

These are the rules on which conditional dynamics, and so pointers and settings, are not excluded
by S-C1.

### S.4 Maximum skepticism (§A.31), on the screen's negative calls

**(a) The trace route: recording without a confined pointer.** S-L4 excludes a confined pointer. It
does not exclude a region `V` whose later content, made of the difference solution passing through
it, still determines the record. The trace route is not refuted here; it is not admitted, for three
reasons:
1. **No apparatus process.** `V` does nothing but carry the free field. Record and outgoing carrier
   are one field (S-L1). None of the stages of §3.2 has an executing apparatus process distinct
   from transport.
2. **A free choice would fix the outcome.**
   - Under a prepared zero configuration on `V`'s causal neighbourhood, R2 holds by injectivity
     alone whenever `V` contains the difference solution's support over the whole budget, which
     is a region of radius about `T` around `Σ`. That is Main Lemma 3's record preservation,
     restated (A1).
   - For a smaller `V`, R2 is a property of the free propagator restricted to `V`, which no source
     fixes.
   - So the axis-1 outcome would be set by the choice of `V` relative to `T`. Freezing that choice
     would freeze structure that decides the outcome by itself (§A.29; frozen §7.3).
3. **No sourced ready supply.**
   - The route needs the zero configuration over `V`'s causal neighbourhood for the whole budget, a
     resource whose size grows with the budget.
   - The canonical measure supplies none (§S.3, σ1).
   - Main §4.6 (Main:744–760, conditional on EM) places observers in a non-equilibrium phase, but
     supplies no prepared region.
   - The ready supply of frozen §3.3 is of pointer states, and there is no pointer.

**(b) Loopholes in S-L4.**
- *A zero-divisor coefficient.* With `a·x = 0` for some `x ≠ 0` (for example `a = 2` on `ℤ/4`),
  values in `ker a` do not propagate. They can be written when `a𝐑 ∩ ker a ≠ 0`, so a confined
  pointer would exist. No coefficient the corpus uses is a zero divisor (§S.1). The case lies
  outside K1 as the corpus fixes it, and is recorded as a scope boundary.
- *Engineered graphs:* σ10.
- *Tori smaller than `5w + 2`:* a "pointer" then extends over the whole torus.

**(c) Q.** An additive offset can serve as a classical phase label, and it composes as a group. So
T0's composed-phase test is not excluded for σ1 or σ2. Q's exclusion rests on S-L5 and on
S-L2–S-L3–S-L6, as stated in §S.3.

**(d) Is additivity what OI holds?** Yes, at `D`, for the local lattice sector: Substratum A5 with
`M = μI` (§S.1). The nonlinear alternatives form "the separate class one obtains exactly when that
gauge principle is dropped" (Substratum:220).

### S.5 Selection rule for `𝔐★`

This rule is fixed by reasons that do not refer to any outcome. `𝔐★` is chosen among the sources
that meet all of:
- **(s1)** run on K1's step, on the native cubic graph, with a coefficient the corpus uses;
- **(s2)** supply every §3.1 element by an executing native process under the declared access.
  This includes the apparatus: a pointer that holds the record over the budget, or another
  persistence mechanism with an executing apparatus process, with its ready supply sourced or
  booked as a pointer resource (§3.3);
- **(s3)** are not excluded by N1–N7 at their scopes;
- **(s4)** involve no per-law or per-design construction, and no free structural choice that by
  itself fixes an axis-1 outcome.

Among the sources that qualify, the one with the fewest posited elements is chosen; a tie goes to
the smallest finite state space.

**Application: no source qualifies.**
- σ1 fails (s2) at the pointer (S-C4a). Its trace route fails (s4) and the ready-supply part of
  (s2) (§S.4(a)).
- σ2 folds into σ1, and σ11 is σ1 on another value group.
- σ3, σ4, σ5, σ9 and σ10 fail (s1) or (s4). σ6 and σ7 fail availability. σ8 fails (s2), since it
  has no embedded readout.
- σ12 lies outside (s1).

The rule selects none. The result is frozen §6 row 1.1, `GAP`, with its element named in §M.

### S.6 Gem-finding, depth-first (§A.31)

**Productivity test, fixed before the walk.** A finding is a gem if it is strictly stronger than a
restatement and either constrains something or exposes a hidden assumption.

**The walk.** Each node is closed by the check named.

1. **Does K1 admit conditional dynamics?** No. Check: S-L1 and S-C1.
2. **Can a record persist without conditional dynamics?**
   - 2.1, as a confined pattern: no (S-L4, S-C4a).
   - 2.2, as a trace: not admitted (§S.4(a)).
   - 2.3, in global modes: not embedded (S-C4b).
   - 2.4, with a zero-divisor coefficient or an engineered graph: outside K1 (§S.4(b)).
3. **Is additivity what OI holds?** Yes: Substratum A5 with `M = μI` (§S.4(d)).
4. **Where could a native mechanism live?** In a non-additive rule, or at the observer level
   (AW-MR8, AW-MR9).

The favourable-to-OI branch is 2.2, a record "for free" by injectivity. It was given maximum
skepticism, and it reduces to a restatement of Main Lemma 3 (§S.4(a), reason 2).

**Assumption-watch markers.**
- **AW-MR8 (NEW): a free substratum and an interacting apparatus.** Under Substratum A5 with
  `M = μI`, the K1 step is a free field on the full local lattice sector. S-C1 and S-C4a then
  exclude conditional dynamics and confined pointers at the substratum level.
  - *The hidden presupposition.* MR-1's question (frozen §1) asks "which microscopic interaction
    forms a record". It presupposes an interaction at the substratum. Under `K★ = {K1}` there is
    none.
  - *What it constrains.* A native record mechanism needs either a non-additive rule, which drops
    A5's amplitude-scale gauge (Substratum:220), or the observer level. SM:428's commitment, "group
    structural, couplings emergent", places interactions at the observer level.
  - *Reach.* It constrains every record-formation or instrument unit on the K1 step. PC-1's Q1
    detector, for instance, is transport.
  - *Gem test.* It passes: S-L1 and S-L4 are proved facts, not restatements, and the
    presupposition was nowhere stated in the unit.
- **AW-MR9 (NEW): stable matter is an input, not a substratum structure.**
  - *E6's status.* Substratum's E6 (Substratum:86: "Atoms, planets, and bound states exist on
    observed timescales") is an empirical filter, evaluated with continuum Coulomb and Tangherlini
    physics.
  - *No substratum carrier.* By S-L4, the K1 step has no confined pattern, so bound states and
    pointers have no carrier at the substratum level under A5. If they exist, they are emergent.
  - *The hazard.* A record mechanism built from emergent bound states risks presupposing the
    emergent quantum description that MR-1 is meant to bear on. That is a hazard at the trace-out
    interface, to be checked by any successor unit.
- **AW-MR10 (ELABORATING): a ready supply presupposes pointers.** Frozen §3.3 books "a ready
  supply of low-entropy pointer states". Without a pointer, the only ready resource is a prepared
  zero region over the observer's causal neighbourhood, whose size grows with the budget (§S.4(a)).
- **AW-MR11 (ELABORATING): budgets lie below recurrence.** On finite `S`, every R2 and every
  effective irreversibility is relative to a budget below the order of `φ`. At that order, the
  global wait executes every inverse and erases every record (S-L6).
- **AW-MR12 (ELABORATING): proof generality is not licence.** §PC★2a's generality over neighbour
  relations and coefficients supports P-1 to P-3. It does not make an engineered graph, or a
  zero-divisor coefficient, native under K1 (§S.1, §S.4(b)).
- **The AW-MR5 sub-question** is answered by S-L7, conditional on the declared access.

**Fixed point.** It is not claimed. One depth-first pass was run on the decisive branch, the
pointer, to its wall. Further passes belong to a successor unit.

### S.7 What this section does not do

- It fixes no `𝔐★`, no `GAP` token and no stage-2 item; those are in §M.
- It derives no record law of any source, candidate or control, and evaluates no test.
- It does not establish a no-go for OI, for non-additive native rules or for observer-level
  apparatus.
- It does not claim that classical explanations are excluded (D3).
- It changes no frozen file, `K★` or earlier amendment.

### S.8 Commands and hygiene for this section

- **Read-only commands:**
  - `git rev-parse HEAD`, `git status`, `git log`;
  - display of the frozen preregistration, `KS-substitution.md`, `D3-CC2-class-level.md`,
    `MR-star.md` and `stage1-log.json`;
  - `git show 99dce4b6:` of PC-1's `preregistration.md` (§4) and `amendments/PC-star.md`;
  - `git ls-tree` of F2-1 at `4e7ddb70` and of SUBSTATE-1 at `8af2d904`;
  - `git show 8af2d904:` of `README.md`, `later-access-result.md`, `native-apparatus-register.md`,
    `native-sign-echo.md`, `cubic-wave-revival.md`, and the heads of eight further notes there;
  - `git show 2af1d5d5:` of #912's `REPORT.md` (equation (1));
  - `git show 5914c17c:` with `sed -n` and `grep` over `papers/Main.md` (44–62, 408, 482, 486, 520,
    566, 582, 726, 742–760), `papers/SM.md` (92, 104–106, 222–232, 252, 428, 1604–1612) and
    `papers/Substratum.md` (48, 86, 96–104, 220, 270–274);
  - display of `native-y-continuation-20261024/README.md`, `CURRENT-HANDOFF.md` and
    `shared_v12/INTERFACE-CONTRACT.md` on the current tree.
- **Hygiene (run S-1, on the staged section):** placement, census and SC-42, then the single
  commit. Their outcome is stated in the commit message and logged in `stage1-log.json` under
  `screen`.
