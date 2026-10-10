# Verifier round V3-14 — retirement: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull
request from `D`, the control plane drafted on it, execution after the owner designates `F`, and
the round's protocol record a receipt on which `tools/v3_verifier.py --verify-round` must print
`VERDICT  HOLDS`.

> **V3-14 carries out the retirement `V3-13` froze and could not complete.** `V3-13` halted under
> the specification's `S12` because its guard transformation deleted retained statements, and its
> withdrawal restored every execution path. This round repeats that retirement with the
> transformation corrected, and it freezes what `V3-13` lacked:
> - an edit ledger naming every change the transformation makes;
> - a preservation checker independent of the transformation, mutation-tested in both directions;
> - regression vectors for every statement `V3-13` damaged;
> - an invariant→checkpoint table;
> - a run of the whole predicted execution tree in CI before the freeze.

## The declarations

```v3-round
round V3-14
kind non-sealing
record-directory verification/infrastructure/round-v3-14-retirement/
```

```v3-governed-paths
record AM verification/infrastructure/round-v3-14-retirement/
record AM verification/receipts/V3-14.json
execution M .github/workflows/verify.yml
execution M AGENTS.md
execution D tools/certificate_verifier.py
execution D tools/control_plane_base_check.py
execution D tools/control_plane_lint.py
execution A tools/legacy_records_check.py
execution M tools/release_gate.py
execution M tools/v3_verifier.py
execution M verification/README.md
execution D verification/certificates/conformance/
execution A verification/infrastructure/legacy-records.json
execution M verification/infrastructure/v3/architecture.md
execution AD verification/infrastructure/v3/conformance/
execution M verification/lean/edge_rigidity_probe.py
```

The record directory holds:
- this preregistration;
- the guard transformation `retire.py` and its two text inputs, `messages.json` and `headers.json`;
- the frozen edit ledger `ledger.json`;
- the independent preservation checker `preserve.py`;
- the retirement controls `controls.py`;
- the result note.

The receipt path is `verification/receipts/V3-14.json`. Every other path the round changes is an
execution path listed above, and nothing in the legacy-records population is among them.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects).

- **`D`** = `378073fa9c3ad7a5c6327aa0163dec3619a40d84`, the head of `main` after `V3-13`'s landing.
  - It was certified by push run 36201832097, with all six jobs green, the release gate passing
    with `v3-receipts` holding on four receipts, and the guard 105 PASS and 0 FAIL.
  - `delta(f9a9acaa, D)` is `V3-13`'s six record-directory files and its receipt. The guard, the
    census, the verifier, `AGENTS.md` and `verification/README.md` have the same blobs at `D` as at
    `V3-12`'s landing.
  - Every measurement in this file was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation, a merge whose first parent is `main` when it is built and
  whose second parent is `E` (or a superseded receipt commit). It is built with `--no-ff` if `main`
  is still `D`.
- **`Q`** — the final receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/V3-14.json`.

## What this round adopts from `V3-13`, and what it corrects

**Adopted, by citation of `verification/infrastructure/round-v3-13-retirement/preregistration.md`:**
- the owner's six decisions on `V3-12`'s questions;
- the two immutabilities, kept apart;
- the eleven constraints from `V3-12`, each met as that freeze states;
- the amendment to `V3-12`'s census, retiring six further predicates for 1,616 in all, with its
  controls `pc4s` and `vacuity`;
- the caller census and the history control;
- stages 3 to 5 as `V3-13` froze them.

`V3-13`'s record is not edited. The stage 3 to 5 files are re-derived at this `D`. Their content
differs from `V3-13`'s only where they name the round, where the documents record `V3-13`'s halt,
and where `AGENTS.md` gains the rules below.

**What `V3-13`'s failed candidate head showed.** Run 36168400287 on `d4143df7` found the Lean
kernel check green. The `Mathlib bridge` was green, with the release gate passing 21 of 21:
- `legacy-records` intact;
- `v3-self-test` OK;
- `v3-corpus` at 140 vectors;
- `v3-receipts` holding.

That is provenance for carrying stages 3 to 5 forward, not certification. The candidate head was
never an `E`.

**Corrected: the damage.** `V3-13`'s result note names five retained statements its transformation
deleted. Measured at `D`, the transformation deleted **ten**. Seven were found by comparing every
retained function and module-level block with its text in `V3-13`'s stage 2 guard. The other three
were found when this round's first rehearsal ran the guard in CI (see the execution evidence
below).

| D line | where | deleted | how |
|---|---|---|---|
| 180–181 | module-level loop in `R3` | `if induced_by(n, perm, E) is not None: continue` | the sweep called the `continue` dead, then the emptied `if` went |
| 193 | the same loop | `break` after `wfound = w` | the sweep called the `break` dead |
| 232–233 | `rank` | `if piv is None: continue` | the emptied-block rule counted `continue` as removed |
| 292 | module-level `while changed:` loop in `R5` | `changed = True` | the sweep's reaching definitions missed a flag set later in the loop and read by its own condition |
| 304–305 | `grow` | `if len(clique) + len(cand) - i <= best: break` | the emptied-block rule |
| 25309–25310 | `_ogs_def_ok` | `if not l.strip(): break` | the emptied-block rule |
| 26777–26778 | `_cgr_token` | `if depth == 0: break` | the emptied-block rule |
| 14250–14252 | `R7-A12P`'s mutation control `m13` | the loop setting the family's status to `kernel-only` in the copied registry | the sweep saw a store into the loop variable `_f`, not into the registry `_f` belongs to |
| 16548–16551 | `R7-A6P`'s mutation control `m8` | the loop appending an `SM.md` anchor to the copied registry | the same |
| 19401–19404 | `R7-A6I`'s mutation control `m15` | the loop appending an `SM.md` anchor to the copied registry | the same |

Three things follow:
- The rows at 193 and 292 were missed by `V3-13`'s own damage census, which looked only for `if`
  blocks holding nothing but control flow.
- The guard at `V3-13`'s candidate head crashed in `R4` before `R5` ran, so the lost
  `changed = True` would have failed `R5` next.
- Without the last three rows, each of those mutation controls tests an unmutated registry, and
  its check fails closed; the candidate head never reached them.

The comparison also found `_blk = _slice(...)` in `CT2`'s loop removed as a dead store; that removal
was harmless. The round's result note restates this table as the correction.

## The scope of the deletion

The round separates four things and decides each in advance.

| layer | decision |
|---|---|
| authority retirement | mandatory: `V2`, the control-plane tools and the per-round chronology predicates stop deciding anything |
| reachability retirement | mandatory: no gate step, workflow job, verifier path or guard path reaches the retired machinery or reads repository history |
| physical deletion | in scope, for the reason below |
| dead-code removal | never authorized by inference: the sweep is a discovery mechanism, not an authorization mechanism. A deletion exists only because its exact splice is in the frozen ledger and passes `L1`, `L2` and `S1`–`S7` |

**Why physical deletion is in scope.** The history control this round adopts is a static criterion.
It counts every history-reading construct in the files the probes job runs: a `subprocess` import, a
`git` command string, an environment read. It does not ask whether the construct is reached. At `D`
the guard has 213 such sites, 189 inside function bodies and 24 in code that runs at module level.
Leaving unreachable code in place would leave most of them, and meeting the control would then need
a reachability analysis in its place, the same kind of inference this section confines. The
alternative was measured. The census's removals alone, without the sweep, leave the machinery that
fed the retired predicates running at module level, including R7-GR1's landing computation, which
reads repository history. They also leave a block with an empty body before its `else`, so the file
does not parse. Retiring authority and reachability therefore requires deleting the code that
becomes unreferenced.

**What makes each deletion individually justified.** The sweep in `retire.py` discovers; it does
not authorize. A deletion it proposes exists only as a splice of the frozen ledger, and
`preserve.py` checks each one against the guard at `D` without reference to the sweep:
- it is not control flow leaving a surviving block (`S3`, `S5`);
- it is not inside a retained function (`S2`);
- it changes no object surviving code reads (`S6`);
- it binds no name surviving code still resolves to (`S7`).

## The transformation

`retire.py` is `V3-13`'s transformation with four changes.

1. **The emptied-block rule.** A compound statement is removed as emptied only if the
   transformation removed content from inside it. A block holding only `continue`, `break` or
   `pass`, from which nothing was removed, is the code and stays.
2. **Control flow is never dead code.** `continue`, `break`, `pass`, `return`, `raise` and `assert`
   are not units of the dead-code sweep. They leave only with a removed enclosing statement.
3. **Dead code stays outside surviving blocks.** A statement the sweep calls dead inside a
   module-level `for`, `while`, `if`, `with` or `try` that survives is kept as a root, and the sweep
   runs again. Only predicates the census retires, their counters and blocks emptied of those
   predicates leave a surviving block. Exactly two statements are kept this way: `changed = True` at
   292, and the dead store at 2128.
4. **A mutation reaches through aliases.** A mutation of a name is also a mutation of what that
   name's reaching definition takes its value from: a loop's iterable, an assigned name or
   subscript, a with-item. Depth is followed: an element of a value is one level down, a shallow
   copy (`dict(x)`, `list(x)`, `sorted(x)` and the like) shares only what lies below its top level,
   and a deep copy (`json.loads`, `copy.deepcopy`) shares nothing. So a loop that mutates a copied
   registry through its loop variable lives while the registry is read.

It also emits the ledger.
- **Ledger:** every change is carried as a splice of the guard at `D`, and `--ledger` writes them
  out.
- **Unchanged from `V3-13`:** the census reading, the amendment, the message and header texts, and
  the comment rules.

It runs under CPython 3.11, the version the census's text hashes come from:

```
python3 retire.py <guard at D> <V3-12 census.json> <output> messages.json headers.json --ledger <out>
```

It prints:
- `1616 predicates retired, 1610 as the census classes them and 6 by the amendment; 2486 retained`;
- `structural rows: 15 removed with the emptied checks, 85 kept`;
- `2 statement(s) kept inside surviving module-level blocks`;
- `91 checks remain`, naming the 14 emptied checks;
- `retained predicates missing: 0`.

**Its output:** blob `8dad60d0aac870fced7deeec44c0dbdfcb3d45de`, 14,816 lines. A second run gives
the same bytes and the same ledger. Its difference from `V3-13`'s stage 2 guard is exactly the ten
damaged sites restored plus the kept dead store at 2128, and nothing else.

## The ledger

`ledger.json` (`schema: v3-14-splice-ledger`) records every change as a splice of the guard at `D`.
It is the authorization: nothing outside it changes.

Each splice gives:
- the span `d_start`..`d_end` (1-based, inclusive);
- the SHA-256 of the old text;
- the new lines (empty for a deletion) and their SHA-256;
- the reasons for the change.

It names the base blob `2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f` and the output blob above.

It holds 556 splices. Their reasons are:
- 299 census and 4 amendment;
- 6 each of `census-structural` and `emptied-check`;
- 366 dead code, 8 counter and 20 emptied block;
- 201 comment and 209 blank;
- 41 message and 20 header.

A splice can carry more than one reason, and 61 splices carry replacement text.

## The preservation checker

`preserve.py` imports nothing from `retire.py`. From the guard at `D`, the census and the ledger
alone, it checks:

| check | what |
|---|---|
| `L1` | the ledger's base and output blobs, its splices in order and disjoint, and every old and new hash |
| `L2` | the guard at `D` with every splice applied, and nothing else, is the output, byte for byte |
| `S1` | every predicate the census retires, and the amendment's six, lies wholly in splices, as does every predicate and check call of the 14 emptied checks; no other census row has a line in a splice |
| `S2` | a function whose `def` line lies in no splice has no line in any splice; a function whose `def` line does lies wholly in splices |
| `S3` | every `continue`, `break`, `return`, `raise` and `assert` in a splice has its governing block wholly in splices: the enclosing loop for `continue` and `break`, otherwise the enclosing function or top-level statement |
| `S4` | the ten damaged sites are in no splice |
| `S5` | inside every surviving module-level block, every wholly-spliced statement is a retired predicate, a counter increment, or a block of nothing but those and control flow |
| `S6` | every wholly-spliced module-level statement that is not a retired predicate and changes an object in place changes nothing a surviving statement reads. The object is followed back through its name's definitions with the depth rule above. A name reached must not be read by a surviving module-level statement after the change and before it is rebound, nor by a surviving function |
| `S7` | every wholly-spliced module-level statement or top-level function that is not a retired predicate binds no name surviving code still resolves to: no surviving module-level read after it with no surviving binding in between, and no read in a surviving function, its own locals aside, of a name left with no surviving binding. A counter increment is not a binding |

On the real inputs every check holds:
- 556 splices;
- 1,616 predicates retired and 2,486 retained;
- 257 retained functions untouched;
- of 1,635 control-flow statements, 1,228 removed with their governing block;
- 10 regression sites preserved;
- 452 surviving module-level blocks;
- 49 removed in-place changes, none to an object a survivor reads;
- 2,088 removed bindings, none still resolved by surviving code.

`preserve.py --self-test` then requires each of sixteen mutants to fail the checks named:

| mutant | must fail |
|---|---|
| each of the ten damaged sites deleted through a consistent splice | `S4`, plus `S2` inside a function, `S5` inside a module-level block, or `S6` for a top-level statement, plus `S3` where the site is `continue` or `break` |
| `CHECK_TAGS = []`, which surviving code reads, deleted through a consistent splice | `S7` |
| one byte of the output changed | `L2` |
| one splice's old hash changed | `L1` |
| a retained predicate deleted through a consistent splice | `S1` |
| a retired predicate restored | `S1` |
| the condition inside `rank` rewritten | `S2` |

**The countercontrol on real damage.** `controls.py v313` derives a ledger from `V3-13`'s stage 2
guard by a line diff; this diff-derived ledger serves only here. `L1`, `L2` and `S1` hold, and `S2`,
`S3`, `S4`, `S5` and `S6` fail, with `S4` naming all ten sites. So the checker rejects the guard
`V3-13` produced. `S5` also names the dead store at 2128.

That line diff pairs some identical lines ambiguously, and those pairings add flags that are not
damage:
- `S2` names four functions besides the damaged ones: `_os_decl`, `_os_section`, `_pra_gates_ok`
  and `_pra_note_ok`;
- `S3` names thirteen `return` statements, at 7324, 7330 and eleven lines from 28415 to 28445.

`V3-13`'s stage 2 guard differs from this round's output only by the ten sites and the line at
2128, and this round's ledger passes `S2` and `S3`. So the extra flags come from the diff, not from
`V3-13`'s edits. The ambiguity is why the round's ledger is carried by the transformation itself.

## The rest of the round

Stages 3 to 5 are `V3-13`'s, re-derived at this `D`:

- **Stage 3 (one commit).**
  - `legacy-records` goes in: the manifest, byte-identical to `V3-12`'s; its checker; its gate step.
  - `V2` comes out: its gate step, workflow job, tool and conformance corpus.
  - The control-plane lint and base check leave with their step and job.
  - `v3-self-test` and `v3-corpus` enter the gate, and the diagnostics job leaves.
  - The probes job takes the depth-1 checkout.
- **Stage 4.**
  - `G12` is restated without `verification/seals/`.
  - `G13` enters `--receipts`.
  - The projection is removed, with the caller census as `V3-13` froze it.
  - The corpus reaches 140 vectors, and the specification carries the same changes.
- **Stage 5.**
  - `AGENTS.md`: §A.37 becomes a record and §A.39 states the two immutabilities, as in `V3-13`.
  - §A.39 also gains a rule for destructive transformations: an edit ledger, an independent
    preservation checker mutation-tested both ways, and execution in CI before the freeze.
  - §A.41 is added: every stated invariant is measured, and a named hazard with a cheap mitigation
    carries it.
  - The lessons register gains a line on `V3-13`.
  - `verification/README.md` describes this round and `V3-13`'s halt.

With the V2 removal, the release gate runs 21 steps and the workflow three jobs.

## The execution evidence before the freeze

The predicted execution tree, less the preregistration and the result note, was committed on a
disposable branch, `claude/v3-14-rehearsal`, and run through the real workflow in both event modes,
`workflow_dispatch` and `pull_request` on draft pull request #745. The pull request is closed
unmerged afterwards. The runs are design evidence, not `check-run` attestations.

**Rehearsal 1** (`e26f919d186d477b1bfa3cad32e4ca8e6394de86`, a child of `D`) carried the first
draft of this round, before the fourth change to the transformation and before `S6`.
- Runs 36204136039 (`workflow_dispatch`) and 36204145655 (`pull_request`).
- The Lean kernel check and the `Mathlib bridge` passed, the release gate 21 of 21, with
  `legacy-records` intact, `v3-corpus` at 140 vectors and `v3-receipts` holding on four receipts.
- `Numerical probes` failed: the guard ran to the end with 88 checks passing and three failing,
  `R7-A12P`, `R7-A6P` and `R7-A6I`. Each had lost the loop that mutates its copied registry, so
  each mutation control tested an unmutated registry and failed closed. These are the last three
  rows of the damage table. The first draft's `preserve.py` held on that ledger, because no check
  covered in-place changes made through an alias.

**Rehearsal 2** (`9dfcfb89ca02d91f2fb17b30c71e06319989490b`, a child of rehearsal 1) carried the
corrected transformation, ledger and checker. Runs 36205594484 (`workflow_dispatch`) and 36205589538
(`pull_request`): all three jobs green in both, `Foundations probes` included. The dispatch run's
guard reports 91 PASS and 0 FAIL, its verdict map `D`'s without the 14 emptied checks, tag for tag and
in order.

**Rehearsal 3** (`ac61e6436b4e8136ea13d53cced9a33ba64713fc`, a child of rehearsal 2) changed only
`AGENTS.md`, recording the ten sites and the aliasing check. Runs 36206306449 (`workflow_dispatch`) and 36206310842
(`pull_request`): all three jobs green in both; in each, the guard reports 91 PASS and 0 FAIL with
that map, and the release gate passes 21 of 21 with `legacy-records` intact, `v3-corpus` at 140
vectors and `v3-receipts` holding on four receipts.

**Rehearsal 4** (`4309dee92f47fe2b40279c4d63fe0e846319e728`, a child of rehearsal 3) adds `S7` to
`preserve.py` and the scope rule to `AGENTS.md`; the guard and the ledger are rehearsal 2's. Runs 36207538183 (`workflow_dispatch`) and
36207541526 (`pull_request`): the same, in both.

**Rehearsal 5** (`1d5c8a70d07bc3f412ba848a45ce8d4e25712589`, a child of rehearsal 4) changes only
`AGENTS.md`, restating the general rule for destructive transformations. Its tree,
`a31642acd97065d990c28d2b5a01e30501da452b`, is the predicted execution tree. Runs 36207977022 (`workflow_dispatch`) and 36207981531
(`pull_request`): all three jobs green in both, `Foundations probes` included; in each, the guard
reports 91 PASS and 0 FAIL, its verdict map `D`'s without the 14 emptied checks, tag for tag and in
order, and the release gate passes 21 of 21 with `legacy-records` intact, `v3-corpus` at 140
vectors and `v3-receipts` holding on four receipts. `D`'s map is the one its certifying push run
36201832097 printed: 105 PASS, 0 FAIL.

The runs bind the round through `C11`: at `E`, the tree of `E` with the preregistration and the
result note removed is `a31642acd97065d990c28d2b5a01e30501da452b`.

## Invariants and their checkpoints

| invariant | checkpoint |
|---|---|
| every stage file is the file frozen here | `C1`–`C5` (blobs) |
| the transformation is deterministic and emits exactly the frozen ledger | `C2` |
| nothing outside the ledger changes in the guard | `C2` (`L1`, `L2`) |
| exactly the 1,616 are retired and the 2,486 retained | `C2` (`retire.py`'s tally; `S1`) |
| retained functions are untouched | `C2` (`S2`) |
| no control flow leaves a surviving block | `C2` (`S3`) |
| the ten damaged sites are preserved | `C2` (`S4`) |
| no dead code leaves a surviving module-level block | `C2` (`S5`) |
| no removed in-place change reaches an object surviving code reads | `C2` (`S6`) |
| no removed binding is still resolved by surviving code | `C2` (`S7`) |
| the preservation checker can fail on each kind of damage | `C2` (`preserve.py --self-test`) |
| the preservation checker rejects `V3-13`'s real output | `C2` (`controls.py v313`) |
| no probe or guard path reads history | `C2`, `C8` (`controls.py history`) |
| no caller of the projection remains | `C3`, `C4` (`controls.py callers`) |
| the amendment's four reads are legacy bytes only; its two predicates are self-satisfying | `C2` (`pc4s`, `vacuity`) |
| the legacy records are untouched | `C3`, `C6` (`legacy_records_check.py`) |
| the native receipts hold at every stage, and after landing with `G13` | `C6`, `C10` |
| the retained anchors in edited files survive | `C9` |
| the transformed guard and the new gate execute green | `C8` (at `E`); the rehearsal runs before `F` |
| `E` is the tree the rehearsal ran, plus this file and the result note | `C11` |

## Hazards and their mitigations

| hazard | mitigation, frozen |
|---|---|
| the guard is run in CI only | the whole predicted tree ran in CI before `F`, in both event modes; `C11` binds `E` to that tree |
| a transformation that reproduces its frozen blob reproduces its defects | the ledger is checked against the guard at `D` by `preserve.py`, independent of `retire.py`, with mutants and the `V3-13` countercontrol |
| a line diff pairs identical lines ambiguously | the ledger is produced by the transformation, not by a diff; the diff is used only in the countercontrol, whose required failures do not depend on the ambiguous pairings |
| the transformation and the checker share one model of aliasing, so a mutation outside it (through a helper function that changes a global, or a call on an argument that is no plain name) could escape both | the whole predicted tree ran in CI before `F`; every retained mutation control executes there and fails closed on an unmutated input, which is how the three aliasing sites were found |
| `ast.unparse` text hashes differ between Python versions | the transformation, the checker and the census run under CPython 3.11, which the rehearsal and every checkpoint use |
| the probes read history some other way | `controls.py history` scans every file the probes job runs; the rehearsal ran the probes on the depth-1 checkout |

## The execution

Five stage commits and the result note, each with one parent, from `F`:

1. **Stage 1** adds the record-directory files:

| path | blob |
|---|---|
| `verification/infrastructure/round-v3-14-retirement/retire.py` | `f2e49fc6a39de15d3fd653502a4946f2406a5016` |
| `verification/infrastructure/round-v3-14-retirement/messages.json` | `96e82a37fe24342a2022829ae78fbf1cd9f0e888` |
| `verification/infrastructure/round-v3-14-retirement/headers.json` | `8c727cad183a54048064013b3805013d35ed9fc1` |
| `verification/infrastructure/round-v3-14-retirement/controls.py` | `0282cbeedd18d67e4746427a9ded9c3b60b7a855` |
| `verification/infrastructure/round-v3-14-retirement/preserve.py` | `37bad5e6281642abfcf2448bf814c01dc4543fa1` |
| `verification/infrastructure/round-v3-14-retirement/ledger.json` | `79a1645d484b2d7ef71b871a612e8d36aafe8e60` |

2. **Stage 2** writes the guard with `retire.py`, run at the stage 1 commit from the repository
   root as `python3 verification/infrastructure/round-v3-14-retirement/retire.py
   verification/lean/edge_rigidity_probe.py
   verification/infrastructure/round-v3-12-retirement-census/census.json
   verification/lean/edge_rigidity_probe.py
   verification/infrastructure/round-v3-14-retirement/messages.json
   verification/infrastructure/round-v3-14-retirement/headers.json --ledger <scratch file>`. The
   ledger it writes must equal the frozen `ledger.json` byte for byte; it is not committed.

| path | blob |
|---|---|
| `verification/lean/edge_rigidity_probe.py` | `8dad60d0aac870fced7deeec44c0dbdfcb3d45de` |

3. **Stage 3** deletes `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
   `tools/control_plane_lint.py` and `verification/certificates/conformance/`, and writes:

| path | blob |
|---|---|
| `verification/infrastructure/legacy-records.json` | `9e48bd31797e1673f03807e699a10ae4a0b960c7` |
| `tools/legacy_records_check.py` | `cd1a56c4177a3272a28229df9ecf838b8b331f14` |
| `tools/release_gate.py` | `bd1a58dd4ba607cb4ca762dadc4793a45a233ae7` |
| `.github/workflows/verify.yml` | `ebef32b9fe565ebe2b17322a35b5e97bcc091b44` |

4. **Stage 4** deletes
   `verification/infrastructure/v3/conformance/g12-reject-execution-changes-legacy-seal-namespace.json`
   and writes:

| path | blob |
|---|---|
| `tools/v3_verifier.py` | `681c673734427cb9f316feee09b7c5ffba348004` |
| `verification/infrastructure/v3/architecture.md` | `34bfabb339ca695e6857fa37c788a95a39e7de77` |
| `verification/infrastructure/v3/conformance/g12-admit-execution-changes-legacy-seal-namespace.json` | `f0207794af2eaf6f2c43a7ecd932589aaab51d44` |
| `verification/infrastructure/v3/conformance/g13-admit-records-unchanged-after-later-commit.json` | `3c8f396a5fe0db70519328cf31082225f0143e19` |
| `verification/infrastructure/v3/conformance/g13-reject-record-file-added-after-landing.json` | `6a4a28fc793abe165b8c629465951643ad070231` |
| `verification/infrastructure/v3/conformance/g13-reject-record-file-deleted-after-landing.json` | `311c119ee0c85345e7afcd1068617005d9f67ed6` |
| `verification/infrastructure/v3/conformance/g13-reject-record-file-modified-after-landing.json` | `a474cb4792ab6ac72bea532f74bfcdf6efd615a9` |
| `verification/infrastructure/v3/conformance/g13-reject-seal-record-changed-after-landing.json` | `7e55b7f3176b3707098e97e35b9204be12f996b4` |

5. **Stage 5** writes:

| path | blob |
|---|---|
| `AGENTS.md` | `4c7a768f4bf4a00c15c12a9e74c5b81a0fbdadc0` |
| `verification/README.md` | `1be9ab5b4242531025d438ca5db39427feeba859` |

6. **The result note** `result.md`, whose commit is `E`.

## Targets

| target | question | outcome if it holds | predicted |
|---|---|---|---|
| `V314-0` | is `F` attested and designated? | `F-DESIGNATED` | holds, strong |
| `V314-1` | does stage 2 retire exactly the 1,616, keep the rest, and pass the preservation checker? | `GUARD-RETIRED` | holds, strong |
| `V314-2` | does stage 3 swap `V2` for `legacy-records` in one commit with no record written? | `AUTHORITY-SWAPPED` | holds, strong |
| `V314-3` | does stage 4 restate `G12`, add `G13` and remove the projection with no caller left? | `VERIFIER-SETTLED` | holds, strong |
| `V314-4` | does every gate pass at `E`, with the guard's map `D`'s without the 14 emptied checks? | `RETIRED-GREEN` | holds, strong |
| `V314-5` | is `E` attested and designated? | `E-DESIGNATED` | holds, strong |
| `V314-6` | does `--verify-round Q` hold? | `RECEIPT-HOLDS` | holds, strong |

The checkpoints:

- **`C1`** (stage 1): the six files have their frozen blobs; `controls.py --self-test` passes.
- **`C2`** (stage 2), all of the following:
  - `retire.py` exits 0 printing the five lines above, and writes a ledger byte-identical to
    `ledger.json`;
  - the guard has its frozen blob and compiles;
  - `preserve.py` prints `preserve: all hold`, and `preserve.py --self-test` prints
    `preserve: self-test OK` with all sixteen mutants failing as required;
  - `controls.py v313 . 0811754da89dd5e3674ec913c0c89a24462a88fd D`, run on `V3-13`'s stage 2
    commit, fails the five checks and names all ten sites;
  - `controls.py history` reports 0 sites at stage 2 and 213 at `D`;
  - `controls.py pc4s` and `controls.py vacuity` give `V3-13`'s frozen outcomes.
- **`C3`** (stage 3), all of the following:
  - the four files have their frozen blobs, the manifest byte-identical to `V3-12`'s;
  - `legacy_records_check.py` passes at stage 3 and fails at stage 2, the manifest being absent;
  - `controls.py callers` reports 0;
  - the V3 self-test and corpus pass.
- **`C4`** (stage 4): the eight files have their frozen blobs; the V3 self-test passes; the corpus
  reports 140 vectors; `controls.py callers` reports 0 with seven names removed.
- **`C5`** (stage 5): the two files have their frozen blobs.
- **`C6`** (every stage commit and `Q`): `--receipts` holds on `V3-10`'s to `V3-13`'s receipts, and
  from stage 3 `legacy_records_check.py` passes.
- **`C7`** (`E`): `git diff --no-renames --name-status D E` lists only governed paths, each change
  authorized, and no path of the legacy-records population.
- **`C8`** (`E`), for the dispatch run at `E`:
  - its three jobs are green;
  - the guard reports 91 PASS and 0 FAIL, with a verdict map equal to `D`'s without the 14 emptied
    checks;
  - the release gate passes 21 of 21, with `legacy-records` intact and `v3-receipts` holding on four
    receipts.
- **`C9`** (`E`): the retained anchors hold. These are:
  - in `verification/README.md`, every string literal of the stage 2 guard that it carries at `D`,
    the anchor "`.github/workflows/verify.yml` runs" among them, and no over-reading in the
    slices `R7-A6P` and `R7-A6I` scan;
  - in the workflow, `repertoire_lie`, and no `lake build OIBridge.` or `lake env lean OIBridge/`
    line;
  - in `AGENTS.md`, the §A.35 heading and its registry sentence;
  - in the gate, `"lean-manuscript"`.
- **`C10`** (`Q`): `--verify-round Q` prints `VERDICT  HOLDS`; `--receipts Q` holds on five receipts;
  `legacy_records_check.py Q` passes.
- **`C11`** (`E`): the tree of `E` with the preregistration and the result note removed is
  `a31642acd97065d990c28d2b5a01e30501da452b`.

**The status rule.** Each target's outcome is its checkpoints' verdict.
- If any of `C1` to `C5` fails, the stage is not the one frozen here: the round halts under `S12`
  and records the discrepancy, and the freeze is not repaired.
- A `C8` failure the round's paths cannot cause is diagnosed and recorded before `E` is brought for
  designation. A `C8` failure the round's paths cause halts the round.

## What this round does not do or license

1. It changes no mathematics, no manuscript, no Lean file and no record of another round.
   `V3-13`'s record stands as landed, and this file records the correction to it.
2. It retires no check of content beyond the census and the amendment. The 2,486 retained
   predicates keep their text, and the new messages and headers say less than the old ones, never
   more.
3. It licenses no sentence that a retired check was wrong. Each was true of its round, and its
   facts remain recorded in that round's notes, seal record and certificate.
4. It re-preregisters none of the five legacy rounds that were frozen and never executed.
