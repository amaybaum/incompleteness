#!/usr/bin/env python3
"""Scratch: the V3-8 edits, as data. Never landed.

SPEC: (id, old, new) edits to verification/infrastructure/v3/architecture.md, applied in order,
each old text occurring exactly once. SITES: (site, stage, old, new) edits to tools/v3_verifier.py.
README_OLD / README_NEW: the verification/README.md paragraph."""

SPEC = [
    ('N1', "| `R₁ … Rₖ` | the reconciliation commits of the round (`G11`), merges whose first parent is the tip of `main` when each is built |",
     "| `R₁ … Rₖ` | the reconciliation commits of the round (`G11`), merges whose first parents advance along one first-parent chain (`K3`) |"),
    ('N2', "| `Q` | the final receipt commit: a single-parent child of `Λ`, which publication makes the tip of `main` |",
     "| `Q` | the final receipt commit: a single-parent child of `Λ`, which carries the round's receipt and ends its lifecycle |"),
    ('N3', "| `S10` | publication is a fast-forward to `Q` | `S10`; lifecycle transitions T7 and T8 |",
     "| `S10` | the receipt commit ends the round; publication is outside it | `S10`; lifecycle transition T7 |"),
    ('N4', """alone. The one operation that reads the live tip of `main` is publication (`S10`), which either
succeeds atomically or leaves `main` untouched; it is never an input to the round's validity.""",
     """alone. Whether and how the round's commits reach `main` is not a predicate input and not part of
the round's validity (`S10`)."""),
    ('N5', """result note and read by no predicate. Publication (`S10`) inspects the live tip of `main` as an
operation, and the outcome of that operation is not an input to the round's validity.""",
     """result note and read by no predicate. How the round's commits reach `main` is host operation,
outside the specification (`S10`)."""),
    ('N6', """Before publication a round may therefore abandon a reconciliation or receipt commit and build again""",
     """A round may therefore abandon a reconciliation or receipt commit and build again"""),
    ('N7', """Later `main` enters the round only through reconciliation commits appended to the pull request's
branch after `E`, or after `W` (`S12`). Each reconciliation `Rᵢ` is a merge with exactly two parents:

- the **first parent** is the tip of `main` when `Rᵢ` is built;""",
     """Later history enters the round only through reconciliation commits appended to the round's branch
after `E`, or after `W` (`S12`). Each reconciliation `Rᵢ` is a merge with exactly two parents:

- the **first parent** is the later base the round chooses, a commit on whose first-parent chain
  `D` lies, advancing as `K3` requires;"""),
    ('N8', """The first reconciliation is always built, with `--no-ff` when `main` has not moved since `D`, so that
`Λ` is always a reconciliation and `LB` is always its first parent. `E` and every earlier commit are
unchanged by reconciliation. `Λ` is the last reconciliation and `LB` is its first parent. `D` lies on
`LB`'s first-parent chain; this, and not the tip of any branch, is how a verifier knows `LB` is later
`main` than `D`.""",
     """The first reconciliation is always built, with `--no-ff` when its base is `D` itself, so that `Λ` is
always a reconciliation and `LB` is always its first parent. `E` and every earlier commit are
unchanged by reconciliation. `Λ` is the last reconciliation and `LB` is its first parent. `D` lies on
`LB`'s first-parent chain; this, and not the tip of any branch, is how a verifier knows `LB` is later
than `D`. In operation the base chosen is normally the current tip of `main`; that choice is not
part of the round's validity."""),
    ('N9', """Two consecutive reconciliations may have the same first parent, when `main` has not moved between
them. A round in which one reconciliation's first parent lies behind an earlier one's is invalid,
even when a later reconciliation's first parent lies ahead of both.""",
     """Two consecutive reconciliations may have the same first parent. A round in which one
reconciliation's first parent lies behind an earlier one's is invalid, even when a later
reconciliation's first parent lies ahead of both."""),
    ('N10', """## `S10` — publication is a fast-forward to `Q`, and nothing else

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

`S10`'s rule for `Q` binds every receipt commit of the round (`G11`), superseded or final.""",
     """## `S10` — the receipt commit ends the round; publication is outside it

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

The rule for `Q` binds every receipt commit of the round (`G11`), superseded or final."""),
    ('N11', """receipt carries `seal`, and `Q` publishes the seal state it owns, which is its one seal record
(`G12`); a non-sealing receipt carries no `seal`, and `Q` publishes none.""",
     """receipt carries `seal`, and `Q` carries the seal state it owns, which is its one seal record
(`G12`); a non-sealing receipt carries no `seal`, and `Q` carries none."""),
    ('N12', """A halted round publishes its receipt and its result through the same pull request, and never""",
     """A halted round records its receipt and its result through the same pull request, and never"""),
    ('N13', """Reconciliation (`S9`, with `W` in place of `E`) and publication (`S10`) then proceed as for a
complete round.""",
     """Reconciliation (`S9`, with `W` in place of `E`) and the receipt commit (`S10`) then follow as for
a complete round."""),
    ('N14', """- **The halted execution's effects do not survive in the published tree.** No `execution` path""",
     """- **The halted execution's effects do not survive in the landed tree.** No `execution` path"""),
    ('N15', """- **The execution commits do remain reachable from `main`**, through `W`, as historical evidence.""",
     """- **The execution commits do remain reachable from `Q`**, through `W`, as historical evidence."""),
    ('N16', """outside the governed paths, and what of the halted execution reaches the published tree is decided""",
     """outside the governed paths, and what of the halted execution reaches the landed tree is decided"""),
    ('N17', """| `RECEIPTED` | T7 |
| `PUBLISHED` | T8 |""",
     """| `RECEIPTED` | T7 |"""),
    ('N18', """
| T8: `RECEIPTED` → `PUBLISHED` | none: publication is the non-force update of `main` to `Q` (`S10`), which the host performs or refuses | — |""",
     ""),
    ('N19', """A verifier asked whether a round holds evaluates T1, T3 (or T5), T6 and T7 from `Q` and the commits
its receipt names. Whether `Q` is the tip of `main` is not part of the answer.""",
     """The lifecycle ends at T7. A verifier asked whether a round holds evaluates T1, T3 (or T5), T6 and T7
from `Q` and the commits its receipt names; where `Q` lies, and whether any branch reaches it, is
not part of the answer."""),
    ('N20', """`main` moved once after the first receipt commit was built, so the landing lists two""",
     """The chosen base advanced once after the first receipt commit was built, so the landing lists two"""),
]

# N10 is split at the unchanged `K4` heading, so that neither block carries a heading line, and the
# later edits are renumbered.
_H = "\n\n### `K4` — every receipt commit\n\n"
_out = []
for _nid, _old, _new in SPEC:
    if _nid == 'N10':
        (_o1, _o2), (_n1, _n2) = _old.split(_H), _new.split(_H)
        _out += [('N10', _o1, _n1), ('N11', _o2, _n2)]
    else:
        _k = int(_nid[1:])
        _out.append(('N%d' % (_k + 1 if _k > 10 else _k), _old, _new))
SPEC = _out

SITES = [
    ('s2.1', 2, '''def publication(repo, t, q):
    """S10: a publication of the round is Q itself, and nothing else."""
    try:
        repo.need(t)
        repo.need(q)
    except Undecidable as u:
        return 'UNDECIDABLE', [u.code]
    if t != q:
        return 'FAILS', ['s10:not-q-itself']
    v, codes, _ = verify_round(repo, q)
    return v, codes''', '''def reachable(repo, c, q):
    """A diagnostic, never a verdict (S10): 'true' when Q is an ancestor of C, a commit being its
    own ancestor; 'false' when it is not; 'undecidable' with a code when the repository cannot
    say. No predicate reads it, and it never changes a verdict."""
    try:
        return ('true' if repo.is_ancestor(q, c) else 'false'), None
    except Undecidable as u:
        return 'undecidable', u.code'''),
    ('s2.2', 2, """            elif step['check'] == 'publication':
                got = publication(Repo(workdir), args[0], args[1])""",
     """            elif step['check'] == 'reachable':
                state, code = reachable(Repo(workdir), args[0], args[1])
                got = (state, [code] if code else [])"""),
    ('s2.3', 2, """            exp = step['expect']
            if 'digest' in exp:""",
     """            exp = step['expect']
            if 'reachable' in exp:
                if got[0] != exp['reachable'] or ('code' in exp and got[1] != [exp['code']]):
                    return False, 'REACHABLE %s' % (got[1][0] if got[1] else got[0])
            elif 'digest' in exp:"""),
    ('s2.4', 2, """        if argv[:1] == ['--publication'] and len(argv) == 3:
            t, q = check_oid(argv[1]), check_oid(argv[2])
            verdict, codes = publication(Repo(cwd), t, q)
            print('VERDICT  %s%s' % (verdict, '  ' + ', '.join(codes) if codes else ''))
            return 0""",
     """        if argv[:1] == ['--reachable'] and len(argv) == 3:
            c, q = check_oid(argv[1]), check_oid(argv[2])
            state, code = reachable(Repo(cwd), c, q)
            print('REACHABLE %s' % (code if code else state))
            return 0"""),
    ('s2.5', 2, """         '--publication <T> <Q> | --project <subject> | --mode shadow --subject <commit>')""",
     """         '--reachable <C> <Q> | --project <subject> | --mode shadow --subject <commit>')"""),
    ('s3.1', 3, """    --publication <T> <Q>          S10: whether T is Q itself, and whether Q verifies""",
     """    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C"""),
    ('s3.2', 3, """It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.""",
     """It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.

It verifies repository facts and provenance. Whether a round holds is decided from its final receipt
commit Q and the commits the receipt names; how a round's commits reach main is outside it (round
V3-8). --reachable reports whether Q is an ancestor of a commit, as a diagnostic that no verdict
reads."""),
]

README_OLD = """`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
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
"""

README_NEW = """`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
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
"""
