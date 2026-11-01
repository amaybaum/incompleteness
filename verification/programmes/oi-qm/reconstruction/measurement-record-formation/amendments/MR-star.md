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
