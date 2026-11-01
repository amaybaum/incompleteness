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
