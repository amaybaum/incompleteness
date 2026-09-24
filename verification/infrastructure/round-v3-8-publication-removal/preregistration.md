# Verifier round V3-8 — publication leaves the V3 validity model: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The amended
specification, the changed shadow verifier, the corpus changes, the README paragraph and the result
note are execution objects, created only after the certified merge of this file.

> **V3 proves what is intrinsic to the repository; the host's own protections decide how changes
> reach `main`.** The formal lifecycle ends when the final receipt commit `Q` is receipted.
> Publication — whether and how `Q`'s work reaches `main` — leaves the specification, and whether
> `Q` is an ancestor of a given commit becomes a diagnostic that no verdict reads.

## The commit vocabulary this freeze uses, fixed first

`V3-8` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `f557b1ccbdf9e441b33f5f70fa163823fc2ca10a`, the drafting snapshot: the certified head of
  `main` after `V3-6`'s landing (push run 36040631789, all six jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before the
  merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The letters `F`, `W`, `Rᵢ`, `Λ`, `LB` and `Q` keep the meanings
`verification/infrastructure/v3/architecture.md` gives them; they name objects of the synthetic
rounds the vectors build, never an object of this round.

## What `V3-8` is, and what it is not

`V3-8` is a **specification and implementation round** with one subject. The specification's
`S10` made a round's publication part of its lifecycle: `main` was to be updated to `Q` itself by a
non-force update, and nothing else was a publication. That rule is about how the host moves a ref,
not about what the repository contains, and it is removed. The formal lifecycle ends at T7; `S9`'s
reconciliations take a base the round chooses, advancing as `K3` already requires, rather than "the
tip of `main` when built"; and the shadow verifier's `--publication` is replaced by `--reachable`,
which reports whether `Q` is an ancestor of a commit and is never a verdict.

It is not:

1. **A change to round validity.** `F`, `E`, reconciliation, `K3`, `G11`, the receipt, `K4`,
   `G12` and every predicate `--verify-round` evaluates are unchanged. A round that holds at `D`
   holds after the round, and one that fails fails.
2. **A promotion.** No act of `V3-2`'s promotion boundary is performed: no release-gate wiring, no
   change to the workflow or to any required check, no receipt, no operative language in
   `AGENTS.md`. `V1` and `V2` stay authoritative; the shadow gates nothing.
3. **A host-configuration round.** No repository setting or ruleset is read as a condition or
   changed.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-8`, `v3-8`, `round-v3-8`, `V38-`, `publication-removal`, `reach-true`, `reach-false`,
`reach-undecidable` and `--reachable` occur nowhere in the tree at `D`. Neither
`verification/receipts/` nor `verification/v3-seals/` exists at `D`.

### `F2` — the objects the round reads or writes, at `D`

| path | blob at `D` |
|---|---|
| `verification/infrastructure/v3/architecture.md` | `12cff3f2c9b2cb7803ed1572c98bccba7590c707` |
| `tools/v3_verifier.py` | `21ea40977655d4a36c6e387b496ec5e353e9196b` |
| `verification/README.md` | `08cb79621b1c0e85d4180d8a00081906f35f11f9` |

`verification/infrastructure/v3/conformance/` holds 133 vectors at `D`. Two exercise publication:
`mc2-counter-host-merge` requires `--publication` of a host merge containing `Q` to fail, and
`mc2-pass-base-drift` ends with `--publication Q₂ Q₂`, required to hold.
`g11-admit-rebuild-from-e-after-failed-publication` names publication but carries no publication
step. At `D`, the architecture's publication rule is stated in the objects table (`R₁ … Rₖ` and
`Q`), the traceability row of `S10`, `S1`, `G8`, `G11`, `S9`, `K3`, `S10` and `K4`, `S11`, `S12`
and `G5`, the lifecycle's `PUBLISHED` state and T8, the lifecycle's closing sentence, and one worked
example.

### `F3` — the execution, simulated at `D`

The execution was simulated at `D` in a scratch worktree, each stage applied at its frozen sites and
committed with its files, every tool run being the committed tool at that commit, run from the
worktree. The results are the predictions below:

| measurement | stage 1 | stage 2 | stage 3 |
|---|---|---|---|
| `architecture.md` blob | `db36dbd1ee4f779eff13525ffd3dc11d9041ab36` | the same | the same |
| `tools/v3_verifier.py` blob | `21ea4097` | `0b3bd87fe52b269e9d7cf0fdb7f47653301ce8fd` | `ccfbe813790e4855f408462449327f32e59d545b` |
| `verification/README.md` blob | `08cb7962` | the same | `55aba15ba3cf57a1fc35232534b6eed810abd920` |
| corpus, exact and as expected | 133 | 135 | 135 |

At stage 2 each of the four new or converted vectors runs not as expected under the stage-1 tool and
as expected under the stage-2 tool. At stage 3, `--reachable <D> <D's first parent>` prints
`REACHABLE true` and exits 0, `--reachable <D's first parent> <D>` prints `REACHABLE false` and
exits 0, and `--publication` is refused as an unknown entry point. `--project` over `D` gives output
identical to the tool at `D`. The own-rule and shadow-report measurements are `C3` and `C5`'s.

## The specification, FROZEN as text

At stage 1 the execution applies these twenty edits to `architecture.md` as it stands at `B`, in
order. Each located block occurs exactly once in the file at the time it is applied and is replaced
by its replacement. A block is the text between its fences without the final newline; `N18`'s
located block begins with an empty line. Nothing else in the file changes.

#### `N1` — the reconciliations in the objects table

The located block:

```text
| `R₁ … Rₖ` | the reconciliation commits of the round (`G11`), merges whose first parent is the tip of `main` when each is built |
```

Its replacement:

```text
| `R₁ … Rₖ` | the reconciliation commits of the round (`G11`), merges whose first parents advance along one first-parent chain (`K3`) |
```

#### `N2` — `Q` in the objects table

The located block:

```text
| `Q` | the final receipt commit: a single-parent child of `Λ`, which publication makes the tip of `main` |
```

Its replacement:

```text
| `Q` | the final receipt commit: a single-parent child of `Λ`, which carries the round's receipt and ends its lifecycle |
```

#### `N3` — the traceability row of `S10`

The located block:

```text
| `S10` | publication is a fast-forward to `Q` | `S10`; lifecycle transitions T7 and T8 |
```

Its replacement:

```text
| `S10` | the receipt commit ends the round; publication is outside it | `S10`; lifecycle transition T7 |
```

#### `N4` — `S1`

The located block:

```text
alone. The one operation that reads the live tip of `main` is publication (`S10`), which either
succeeds atomically or leaves `main` untouched; it is never an input to the round's validity.
```

Its replacement:

```text
alone. Whether and how the round's commits reach `main` is not a predicate input and not part of
the round's validity (`S10`).
```

#### `N5` — `G8`

The located block:

```text
result note and read by no predicate. Publication (`S10`) inspects the live tip of `main` as an
operation, and the outcome of that operation is not an input to the round's validity.
```

Its replacement:

```text
result note and read by no predicate. How the round's commits reach `main` is host operation,
outside the specification (`S10`).
```

#### `N6` — `G11`

The located block:

```text
Before publication a round may therefore abandon a reconciliation or receipt commit and build again
```

Its replacement:

```text
A round may therefore abandon a reconciliation or receipt commit and build again
```

#### `N7` — `S9`, the first parent

The located block:

```text
Later `main` enters the round only through reconciliation commits appended to the pull request's
branch after `E`, or after `W` (`S12`). Each reconciliation `Rᵢ` is a merge with exactly two parents:

- the **first parent** is the tip of `main` when `Rᵢ` is built;
```

Its replacement:

```text
Later history enters the round only through reconciliation commits appended to the round's branch
after `E`, or after `W` (`S12`). Each reconciliation `Rᵢ` is a merge with exactly two parents:

- the **first parent** is the later base the round chooses, a commit on whose first-parent chain
  `D` lies, advancing as `K3` requires;
```

#### `N8` — `S9`, the first reconciliation

The located block:

```text
The first reconciliation is always built, with `--no-ff` when `main` has not moved since `D`, so that
`Λ` is always a reconciliation and `LB` is always its first parent. `E` and every earlier commit are
unchanged by reconciliation. `Λ` is the last reconciliation and `LB` is its first parent. `D` lies on
`LB`'s first-parent chain; this, and not the tip of any branch, is how a verifier knows `LB` is later
`main` than `D`.
```

Its replacement:

```text
The first reconciliation is always built, with `--no-ff` when its base is `D` itself, so that `Λ` is
always a reconciliation and `LB` is always its first parent. `E` and every earlier commit are
unchanged by reconciliation. `Λ` is the last reconciliation and `LB` is its first parent. `D` lies on
`LB`'s first-parent chain; this, and not the tip of any branch, is how a verifier knows `LB` is later
than `D`. In operation the base chosen is normally the current tip of `main`; that choice is not
part of the round's validity.
```

#### `N9` — `K3`, consecutive reconciliations

The located block:

```text
Two consecutive reconciliations may have the same first parent, when `main` has not moved between
them. A round in which one reconciliation's first parent lies behind an earlier one's is invalid,
even when a later reconciliation's first parent lies ahead of both.
```

Its replacement:

```text
Two consecutive reconciliations may have the same first parent. A round in which one
reconciliation's first parent lies behind an earlier one's is invalid, even when a later
reconciliation's first parent lies ahead of both.
```

#### `N10` — `S10`, through `K4`'s first sentence

The located block:

```text
## `S10` — publication is a fast-forward to `Q`, and nothing else

`Q` is a single-parent child of `Λ`, and `delta(Λ, Q)` is exactly the receipt path, plus the seal
records a sealing receipt names. The required checks pass on exactly `Q`. Publication is a non-force
update of `main` from `LB` to `Q`: a fast-forward, because `Q` descends from `LB` through `Λ`'s first
parent. After publication the tip of `main` is `Q`; there is no publication commit distinct from
`Q`.

If `main` has moved past `LB` when publication is attempted, the non-force update fails atomically
and `main` is untouched. The round then:

1. builds a further reconciliation, whose first parent is the new tip of `main` and whose second
   parent is either `Q`, which then remains in the round as a superseded receipt commit, or an
   object from which the round builds again (`G11`);
2. builds a new final receipt commit on it, whose receipt names the new `LB` and `Λ` and lists
   every reconciliation of the chain the new `Q` reaches;
3. reruns the required checks on the new `Q`;
4. retries publication.

`F`, `E` and the commits of `F..E` stay as they are.

A `main` that reaches the round's commits through any commit other than `Q` itself — a merge
created on the host, a squash or a rebase — is not a publication of the round.

### `K4` — every receipt commit

`S10`'s rule for `Q` binds every receipt commit of the round (`G11`), superseded or final.
```

Its replacement:

```text
## `S10` — the receipt commit ends the round; publication is outside it

`Q` is a single-parent child of `Λ`, and `delta(Λ, Q)` is exactly the receipt path, plus the seal
records a sealing receipt names. The round's lifecycle ends when `Q` is receipted (T7). Whether the
round holds is decided from `Q` and the commits its receipt names, wherever `Q` lies.

A round that builds again after its first receipt commit — because its chosen base has advanced, or
for any other reason — builds a further reconciliation whose second parent is either the receipt
commit it keeps, which then remains in the round as a superseded receipt commit, or an object from
which the round builds again (`G11`), and a new final receipt commit on it, whose receipt names the
new `LB` and `Λ` and lists every reconciliation of the chain the new `Q` reaches. `F`, `E` and the
commits of `F..E` stay as they are.

**Publication is not part of this specification.** How a round's work reaches `main` — a
fast-forward to `Q`, a merge, or any other operation the host's own protections admit — is
host operation, and no V3 predicate reads it. Whether `Q` is an ancestor of a given commit is a
repository fact, which a verifier may report as a diagnostic; it is never part of a verdict, and a
`Q` that is not an ancestor of a given commit is not thereby invalid.

### `K4` — every receipt commit

The rule for `Q` binds every receipt commit of the round (`G11`), superseded or final.
```

#### `N11` — `S11`

The located block:

```text
receipt carries `seal`, and `Q` publishes the seal state it owns, which is its one seal record
(`G12`); a non-sealing receipt carries no `seal`, and `Q` publishes none.
```

Its replacement:

```text
receipt carries `seal`, and `Q` carries the seal state it owns, which is its one seal record
(`G12`); a non-sealing receipt carries no `seal`, and `Q` carries none.
```

#### `N12` — `S12`, the halted round

The located block:

```text
A halted round publishes its receipt and its result through the same pull request, and never
```

Its replacement:

```text
A halted round records its receipt and its result through the same pull request, and never
```

#### `N13` — `S12`, reconciliation and receipt

The located block:

```text
Reconciliation (`S9`, with `W` in place of `E`) and publication (`S10`) then proceed as for a
complete round.
```

Its replacement:

```text
Reconciliation (`S9`, with `W` in place of `E`) and the receipt commit (`S10`) then follow as for
a complete round.
```

#### `N14` — `S12`, the landed tree

The located block:

```text
- **The halted execution's effects do not survive in the published tree.** No `execution` path
```

Its replacement:

```text
- **The halted execution's effects do not survive in the landed tree.** No `execution` path
```

#### `N15` — `S12`, the execution commits

The located block:

```text
- **The execution commits do remain reachable from `main`**, through `W`, as historical evidence.
```

Its replacement:

```text
- **The execution commits do remain reachable from `Q`**, through `W`, as historical evidence.
```

#### `N16` — `G5`

The located block:

```text
outside the governed paths, and what of the halted execution reaches the published tree is decided
```

Its replacement:

```text
outside the governed paths, and what of the halted execution reaches the landed tree is decided
```

#### `N17` — the lifecycle states

The located block:

```text
| `RECEIPTED` | T7 |
| `PUBLISHED` | T8 |
```

Its replacement:

```text
| `RECEIPTED` | T7 |
```

#### `N18` — the lifecycle transitions

The located block:

```text

| T8: `RECEIPTED` → `PUBLISHED` | none: publication is the non-force update of `main` to `Q` (`S10`), which the host performs or refuses | — |
```

Its replacement:

```text

```

#### `N19` — the lifecycle's closing sentence

The located block:

```text
A verifier asked whether a round holds evaluates T1, T3 (or T5), T6 and T7 from `Q` and the commits
its receipt names. Whether `Q` is the tip of `main` is not part of the answer.
```

Its replacement:

```text
The lifecycle ends at T7. A verifier asked whether a round holds evaluates T1, T3 (or T5), T6 and T7
from `Q` and the commits its receipt names; where `Q` lies, and whether any branch reaches it, is
not part of the answer.
```

#### `N20` — the worked example

The located block:

```text
`main` moved once after the first receipt commit was built, so the landing lists two
```

Its replacement:

```text
The chosen base advanced once after the first receipt commit was built, so the landing lists two
```

## The implementation, FROZEN by site and semantics

The execution changes `tools/v3_verifier.py` at the sites below and nowhere else. Each **site** is
a block of the tool at the stage it is changed in, which must occur there exactly once; each
**semantics** is the rule the changed code must implement. The replacement text shown for each site
is the drafting-time implementation: it is a prediction, as are the blobs it yields. An edit whose
text differs from the prediction is recorded as a divergence, with its diff, and the owner reviews
every divergence for consistency with the frozen semantics before `E` is designated; a divergence
the owner finds inconsistent is a stop outcome for its stage's target.

### Stage 2 — the diagnostic replaces `--publication`

**Semantics.** `reachable(repo, C, Q)` answers `true` when `Q` is an ancestor of `C`, a commit being
its own ancestor; `false` when it is not; and `undecidable`, with the repository's full undecidable
code, when repository evaluation cannot determine ancestry — an absent object, a malformed object id
passed internally, or a shallow history. It never returns a verdict and never calls
`verify_round`. The entry point `--reachable <C> <Q>` first applies `check_oid` to both arguments,
so a malformed argument is refused before any repository read, exactly as for the other entry
points. Otherwise it prints one line — `REACHABLE true`, `REACHABLE false`, or `REACHABLE` followed
by the full code, such as `REACHABLE undecidable:shallow-repository` — and exits 0 in each case.
`--publication` and the function `publication` no longer exist. A repository vector's step
`{"check": "reachable", "args": [C, Q], "expect": {"reachable": …}}` compares the state, and the
code when `expect` names one.

#### Site `s2.1`

The site:

```text
def publication(repo, t, q):
    """S10: a publication of the round is Q itself, and nothing else."""
    try:
        repo.need(t)
        repo.need(q)
    except Undecidable as u:
        return 'UNDECIDABLE', [u.code]
    if t != q:
        return 'FAILS', ['s10:not-q-itself']
    v, codes, _ = verify_round(repo, q)
    return v, codes
```

The drafting-time replacement (a prediction):

```text
def reachable(repo, c, q):
    """A diagnostic, never a verdict (S10): 'true' when Q is an ancestor of C, a commit being its
    own ancestor; 'false' when it is not; 'undecidable' with a code when the repository cannot
    say. No predicate reads it, and it never changes a verdict."""
    try:
        return ('true' if repo.is_ancestor(q, c) else 'false'), None
    except Undecidable as u:
        return 'undecidable', u.code
```

#### Site `s2.2`

The site:

```text
            elif step['check'] == 'publication':
                got = publication(Repo(workdir), args[0], args[1])
```

The drafting-time replacement (a prediction):

```text
            elif step['check'] == 'reachable':
                state, code = reachable(Repo(workdir), args[0], args[1])
                got = (state, [code] if code else [])
```

#### Site `s2.3`

The site:

```text
            exp = step['expect']
            if 'digest' in exp:
```

The drafting-time replacement (a prediction):

```text
            exp = step['expect']
            if 'reachable' in exp:
                if got[0] != exp['reachable'] or ('code' in exp and got[1] != [exp['code']]):
                    return False, 'REACHABLE %s' % (got[1][0] if got[1] else got[0])
            elif 'digest' in exp:
```

#### Site `s2.4`

The site:

```text
        if argv[:1] == ['--publication'] and len(argv) == 3:
            t, q = check_oid(argv[1]), check_oid(argv[2])
            verdict, codes = publication(Repo(cwd), t, q)
            print('VERDICT  %s%s' % (verdict, '  ' + ', '.join(codes) if codes else ''))
            return 0
```

The drafting-time replacement (a prediction):

```text
        if argv[:1] == ['--reachable'] and len(argv) == 3:
            c, q = check_oid(argv[1]), check_oid(argv[2])
            state, code = reachable(Repo(cwd), c, q)
            print('REACHABLE %s' % (code if code else state))
            return 0
```

#### Site `s2.5`

The site:

```text
         '--publication <T> <Q> | --project <subject> | --mode shadow --subject <commit>')
```

The drafting-time replacement (a prediction):

```text
         '--reachable <C> <Q> | --project <subject> | --mode shadow --subject <commit>')
```

### Stage 3 — the tool's description of itself

**Semantics.** The entry-point list names `--reachable` as a diagnostic that is never a verdict, and
the docstring states that the tool verifies repository facts and provenance, that how a round's
commits reach `main` is outside it, and that `--reachable` is a diagnostic no verdict reads. The
banner, the printed rules and every verdict are unchanged.

#### Site `s3.1`

The site:

```text
    --publication <T> <Q>          S10: whether T is Q itself, and whether Q verifies
```

The drafting-time replacement (a prediction):

```text
    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C
```

#### Site `s3.2`

The site:

```text
It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.
```

The drafting-time replacement (a prediction):

```text
It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.

It verifies repository facts and provenance. Whether a round holds is decided from its final receipt
commit Q and the commits the receipt names; how a round's commits reach main is outside it (round
V3-8). --reachable reports whether Q is an ancestor of a commit, as a diagnostic that no verdict
reads.
```

## The README paragraph, FROZEN as text

At stage 3 the paragraph below, which occurs exactly once in `verification/README.md` at `B`, is
replaced by the second, and nothing else in the file changes.

The paragraph at `B`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the settled protocol-3 rules of
`infrastructure/v3/architecture.md`: the settlements of `K1`–`K4` and `G5`–`G7` that round `V3-3`
fixed (`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`), and the settlements of `G8`–`G12` that
round `V3-5` fixed (`infrastructure/round-v3-5-specification-completion/`) and round `V3-6`
implemented (`infrastructure/round-v3-6-final-conformance/`). It gates nothing: it has no
authoritative mode, no verdict it prints changes an exit status, the release gate does not invoke
it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2` remain
authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an exact
set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

The paragraph at `E`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the settled protocol-3 rules of
`infrastructure/v3/architecture.md`: the settlements of `K1`–`K4` and `G5`–`G7` that round `V3-3`
fixed (`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`), and the settlements of `G8`–`G12` that
round `V3-5` fixed (`infrastructure/round-v3-5-specification-completion/`) and round `V3-6`
implemented (`infrastructure/round-v3-6-final-conformance/`). It verifies repository facts and
provenance: whether a round holds is decided from its final receipt commit and the commits the
receipt names, and how a round's commits reach `main` is outside it
(`infrastructure/round-v3-8-publication-removal/`); `--reachable` reports whether a receipt commit
is an ancestor of a given commit, as a diagnostic that no verdict reads. It gates nothing: it has
no authoritative mode, no verdict it prints changes an exit status, the release gate does not
invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2`
remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

## The vectors, FROZEN

At stage 2, in the same commit as the tool's change:

- **Retired:** `mc2-counter-host-merge.json` is deleted. The proposition it tests — that a host
  merge containing `Q` is not a publication — is not a proposition of the amended specification.
  Its recipe up to `H` is reused below.
- **Converted:** in `mc2-pass-base-drift.json` the final step
  `{"check": "publication", "args": ["Q2", "Q2"], "expect": {"verdict": "HOLDS"}}` is replaced by
  `{"check": "reachable", "args": ["Q2", "Q"], "expect": {"reachable": "true"}}`: the superseded
  receipt commit is reachable from the final one. Nothing else in the file changes.
- **Added**, each with `settlements` `["S10"]` and kind `repo`, built from
  `mc2-counter-host-merge`'s steps at `D`:

  | id | steps after `D`…`Q` | expected |
  |---|---|---|
  | `reach-true-host-merge-contains-q` | `M2` on `D`; `H` with parents `M2` and `Q`; `reachable(H, Q)` | `true` |
  | `reach-false-moved-base-lacks-q` | `M2` on `D`; `verify-round(Q)` HOLDS; `reachable(M2, Q)` | `false` |
  | `reach-undecidable-shallow-history` | write `.git/shallow`; `reachable(Q, Q)` | `undecidable`, code `undecidable:shallow-repository` |

Every file is serialized as the corpus is (`json.dump` with indent 1, `ensure_ascii` false, a
trailing newline). The drafting-time bytes of the converted and three added files, concatenated in
path order, have SHA-256 `729ac7598d9d3f28a91be1c0f939d38c426ae6b0d8480767c3947e962f38ce49` (a
prediction, not a pin). `g11-admit-rebuild-from-e-after-failed-publication` is unchanged. After
stage 2 the corpus holds 135 vectors.

## The controls, FROZEN

- **`C1` — the corpus at every stage.** At each stage's commit and at `E`,
  `tools/v3_verifier.py --corpus` runs `conformance/` as an exact set, every vector as expected:
  133, 135 and 135 vectors after stages 1 to 3.
- **`C2` — each vector justifies its change.** Each added or converted vector runs not as expected
  under the stage-1 tool and as expected under the stage-2 tool; the retired vector is absent; the
  stage-2 tool contains no `publication(` and no `s10:not-q-itself`.
- **`C3` — own rule.** At `E`, a scratch copy of the tool with `reachable` replaced by a wrong
  diagnostic runs exactly the vectors listed not as expected and every other vector as expected:

  | wrong diagnostic | its vectors |
  |---|---|
  | always `true` | `reach-false-moved-base-lacks-q`, `reach-undecidable-shallow-history` |
  | always `false` | `reach-true-host-merge-contains-q`, `mc2-pass-base-drift`, `reach-undecidable-shallow-history` |
  | ancestry reversed | `reach-true-host-merge-contains-q`, `mc2-pass-base-drift` |

- **`C4` — the census unchanged.** At `E`, `tools/v3_verifier.py --project` over the subject `B`
  gives output identical to the tool at `B` over the same subject.
- **`C5` — the self-description and the diagnostic, by their outputs.** At `E`, the committed tool,
  run from a checkout of `E`: `--mode shadow --subject E` exits 0 and prints the unchanged banner,
  the rules `K1`–`K4` and `G5`–`G12` in order, `CORPUS  135 vector(s), exact and as expected`,
  `PROJECTION  cells 126` and the completion line; `--reachable <B> <B's first parent>` prints
  `REACHABLE true` and `--reachable <B's first parent> <B>` prints `REACHABLE false`, each exiting
  0; `--publication` is refused as an unknown entry point; and neither the tool nor
  `verification/README.md` contains `--publication` or `not-q-itself`. The README's paragraph is the
  frozen text.
- **`C6` — the self-test.** `tools/v3_verifier.py --self-test` passes at every stage's commit.
- **`C7` — the specification.** At stage 1 `architecture.md`'s blob is the predicted one, and it no
  longer contains `PUBLISHED`, `T8`, ``tip of `main` when``, `publication makes`,
  `publication is a fast-forward` or ``live tip of `main` is publication``.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its target
stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V38-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V38-1` | `PUBLICATION-REMOVED` — stage 1 applies the twenty frozen edits and changes nothing else; `C1`, `C6`, `C7` hold | `SPECIFICATION-UNCHANGED` |
| `V38-2` | `DIAGNOSTIC-INSTALLED` — stage 2 changes the tool at its sites and the corpus as frozen; `C1`, `C2`, `C6` hold | `DIAGNOSTIC-WRONG` |
| `V38-3` | `SELF-DESCRIPTION-CURRENT` — stage 3 changes only the tool's text and the README paragraph; `C1`, `C6` hold | `SELF-DESCRIPTION-STALE` |
| `V38-4` | `CONTROLS-HOLD` — `C3`, `C4` and `C5` hold at `E` | `CONTROL-VOID` |
| `V38-5` | `SHADOW-ONLY` — `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard and `AGENTS.md` have their `B` blobs at `E`; neither `verification/receipts/` nor `verification/v3-seals/` exists; the exact-head run on `E` gives the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and the 135-vector corpus | `AUTHORITY-LEAKED` — fails the round |
| `V38-6` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V38-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V38-1` | `PUBLICATION-REMOVED`; `architecture.md` blob `db36dbd1ee4f779eff13525ffd3dc11d9041ab36` | strong | measured at `D` (`F3`) |
| `V38-2` | `DIAGNOSTIC-INSTALLED`; tool blob `0b3bd87fe52b269e9d7cf0fdb7f47653301ce8fd` | strong | measured at `D` (`F3`) |
| `V38-3` | `SELF-DESCRIPTION-CURRENT`; tool blob `ccfbe813790e4855f408462449327f32e59d545b`, README blob `55aba15ba3cf57a1fc35232534b6eed810abd920` | strong | measured at `D` (`F3`) |
| `V38-4` | `CONTROLS-HOLD` | strong | measured at `D` (`F3`) |
| `V38-5` | `SHADOW-ONLY` | strong | no job, gate, guard or authority file is written |
| `V38-6` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V38-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V38-1` | one: the twenty edits to `architecture.md` | `C1`, `C6`, `C7` |
| 2 | `V38-2` | one: the stage-2 sites and the corpus changes | `C1`, `C2`, `C6` |
| 3 | `V38-3` | one: the stage-3 sites and the README paragraph | `C1`, `C6` |
| 4 | `V38-4` to `V38-6` | one: the result note; its commit is `E` | `C3`, `C4`, `C5`, the closing checks, then the exact-head run |

Stage commits are pushed without waiting for continuous integration on them; the certification of
record is the exact-head run on `E`.

## The mutation budget

- **Modified:** `verification/infrastructure/v3/architecture.md`; `tools/v3_verifier.py`;
  `verification/README.md` (the one frozen paragraph);
  `verification/infrastructure/v3/conformance/mc2-pass-base-drift.json`.
- **Added:** `verification/infrastructure/v3/conformance/reach-true-host-merge-contains-q.json`,
  `reach-false-moved-base-lacks-q.json` and `reach-undecidable-shallow-history.json` in that
  directory; `verification/infrastructure/round-v3-8-publication-removal/result.md`.
- **Deleted:** `verification/infrastructure/v3/conformance/mc2-counter-host-merge.json`.
- **Never written:** every other file under `tools/`, `.github/`, `AGENTS.md`, the guard and
  everything under `verification/lean/` and `verification/lean-mathlib/`, `verification/seals/`,
  `verification/certificates/`, `verification/programmes/`, `verification/audits/`,
  `verification/ROADMAP.md`, any other round's directory, `papers/` and `book/`. Neither
  `verification/receipts/` nor `verification/v3-seals/` is created.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
each stage's blobs against their predictions, with the diff of every divergence; the outputs of `C1`
to `C7`, with the SHA-256 of each scratch script, none of which is landed; the corpus count; and
every discrepancy. The exact-head run on `E` is identified by the `E` certification record, since
the note is part of `E`.

## What no outcome of this round licenses

1. Any claim that a round's work reached `main` because `--reachable` says `true`, or that a round
   is invalid because it says `false`.
2. Any wiring of `--reachable`, or of any verdict, into a gate or required check.
3. Any sentence that V3 is operative.
4. Any change to `V1` or `V2` state, or to another round's records.

## Hazards

- **`H1` — one author.** The edits, the vectors, the tool and the controls have one author; the
  owner's review of the freeze and of the `E` record is the check on a shared misreading.
- **`H2` — the retired vector.** `mc2-counter-host-merge` was one of `V3-2`'s mutation-class
  counter-vectors. Its retirement follows the removal of the proposition it tests; the reachability
  of the same host merge is kept as `reach-true-host-merge-contains-q`.
- **`H3` — the diagnostic's reach.** `reachable` asks git whether one commit is an ancestor of
  another. It says nothing about the content of `C`; that is deliberate (`R4`).

## Files

### Files this round reads AND writes

`verification/infrastructure/v3/architecture.md`; `tools/v3_verifier.py`;
`verification/README.md` (the one paragraph); `verification/infrastructure/v3/conformance/`.

### Files this round reads and MUST NOT write

`.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`,
`tools/control_plane_base_check.py`, `tools/control_plane_lint.py`, the guard, `AGENTS.md`, and the
other `V3` round directories.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the objects the edits are applied to.

```control-plane-preconditions
d: f557b1ccbdf9e441b33f5f70fa163823fc2ca10a
frozen-blob: verification/infrastructure/v3/architecture.md 12cff3f2c9b2cb7803ed1572c98bccba7590c707
frozen-blob: tools/v3_verifier.py 21ea40977655d4a36c6e387b496ec5e353e9196b
frozen-blob: verification/README.md 08cb79621b1c0e85d4180d8a00081906f35f11f9
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-8' -e 'v3-8' -e 'round-v3-8' -e 'V38-' -e 'publication-removal' -e 'reach-true' -e 'reach-false' -e 'reach-undecidable' -e '--reachable' $D", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
{"id": "d1-v3-seals-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/v3-seals", "expect": "empty"}
# row 2: the vector inventory at D
{"id": "d2-corpus-133", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 133", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-8-publication-removal/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/ tools/v3_verifier.py", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-8-publication-removal | grep -v -x -F 'verification/infrastructure/round-v3-8-publication-removal/preregistration.md'", "expect": "empty"}
{"id": "b4-corpus-133", "scope": "B", "check": "test $(git ls-tree --name-only $REF verification/infrastructure/v3/conformance/ | wc -l) -eq 133", "expect": "exit0"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-8-publication-removal/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. The execution pull request
may be opened after stage 1, held from merging. A stop outcome halts the round; the halt is recorded
in a result note with the outcomes reached, and nothing else of the execution lands. `V3-8` carries
no guard clause, manifest record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — publication removed, not re-modelled.** The declined options are a direct-push path to
  `main`, which needs a host-configuration change, and a publication wrapper — a merge with parents
  `LB` and `Q` and `Q`'s tree — which keeps host topology in the validity model in another form.
- **`R2` — `S10` keeps the receipt-commit rule.** `K4`, T7 and the deltas table rest on `S10`'s rule
  that `Q` is a single-parent child of `Λ` whose delta is the receipt and seal record, so `S10`
  keeps that rule and becomes the end of the lifecycle, with the publication note stated as outside
  the specification. The declined option, deleting `S10`, would leave those references without a
  rule; identifiers are not reused.
- **`R3` — `S9`'s base is chosen.** A reconciliation's first parent is a later base on whose
  first-parent chain `D` lies, advancing as `K3` requires; that it is normally the tip of `main` is
  stated as operation, not validity.
- **`R4` — the diagnostic is ancestry only.** `--reachable` prints `REACHABLE true`,
  `REACHABLE false`, or `REACHABLE` followed by a full undecidable code, and exits 0 for every
  argument pair `check_oid` admits. It does not compare trees or verify the round; a diagnostic
  that did would reintroduce a publication predicate.
- **`R5` — no durability guarantee from host refs.** Refs under `refs/pull/` are host
  implementation details and are not made a V3 guarantee. If `Q` is an ancestor of a durable commit,
  ancestry is the provenance; if not, `--reachable` says so and `Q` is not thereby invalid.
- **`R6` — one combined round.** The specification change and its implementation are small and
  interdependent, so they are frozen and executed together, the specification first (stage 1) so
  that the tool's change is made against the amended text.
- **`R7` — the corpus count measured.** The retirement, conversion and additions were measured at
  `D` (`F3`); 135 is the measured result, not a design target.
- **`R8` — no guard clause, certificate or attestation**, as for `V3-1` to `V3-6`.
