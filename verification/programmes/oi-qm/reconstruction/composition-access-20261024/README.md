# Finite-depth composition and complete-record access

Research on the conditions under which finite native stages compose into an
instrument with the reference complete public-record law, and on applying
those conditions to the native constructions of
`../native-y-continuation-20261024/`. Each package states its own scope.
None establishes a native gate, native storage, a native reset, an
observer-access rule or full OI-to-QM equivalence. The reviews are
separate-agent internal reviews, distinct from external review, formal
certification and owner adoption. [CURRENT-HANDOFF.md](CURRENT-HANDOFF.md)
states the results and their scope.

## Packages

| Package | Content | Plan | Review |
| --- | --- | --- | --- |
| top level: `REPORT.md`, `checks.py`, `RESULT.json` | conditional finite-depth composition theorem (written proof) and exact toy controls | none | `review/`, accepts `a7f22c38` |
| `native-x-v2/` | the contract applied to the native-X candidate: one-stage success kernel and terminal failure law; one unchanged-carrier continuation rejected | decision rule in `REPORT.md`, committed at `8d1150fe` before the checker | `review/`, accepts `2390b329` |
| `tagged-post-y-v3/` | a fixed tagged decoder for the direct-Y candidate's history tag; unchanged post-Y samples leave the positive decoder cone after X, R or Z reads | `PLAN.md`, committed with the checker at `75619cb7` | `review/`, accepts `75619cb7` |
| `native-phase-v4/` | finite-depth operational comparison; an omitted native neighbour changes the next raw record | `PLAN.md` at `feba7dc6` | `review/`, accepts `5b77352f` |
| `native-coupling-v5/` | coupled native pool: whole-port leak, and Native A's third-source repair as a conditional code/metadata law | `PLAN.md` at `91cc787e`; its flag-only countercontrol item was added with the results at `621e1a05` | `review/`, accepts `621e1a05` |
| `composition_flag_v6/` | explicit 89-tick reversible logical acceptance circuit and its conditional complete pointer/carrier law | `PLAN.md` at `b355f81e` | `review/`, accepts `1cb224db` |
| `delayed_history_v7/` | delayed old-port history for the frozen v6 carrier | `PLAN.md` at `d72ea524` | `review/round1/` blocks `114ad502`; `review/round2/` blocks `74cdd24e`, re-checks `98cf4647` and accepts `65650298` with nits |
| `native_predicate_v8/` | passive native readout as the acceptance flag, class C(4, 16), scaled control: negative | `PLAN.md` at `631bec0c` | `review/round1/` accepts `375a29e4` with nits; `review/round2/` accepts `fc452ea8` |

Every package's files are those its last review covers: the files pinned in
each `review/INPUT-HASHES.json` are unchanged, `delayed_history_v7/` is
unchanged since `65650298` and `native_predicate_v8/` since `fc452ea8`, apart
from their `review/` directories. A plan file is unchanged since its commit
except as stated in the table. `delayed_history_v7/review/README.md` and
`native_predicate_v8/review/README.md` list what the reviewers' directories
held, what is kept, and the one redaction (an absolute scratch prefix removed
from four `err.txt` traceback paths in `delayed_history_v7/review/`).

## Replay

From the repository root, with the Python 3 standard library:

    D=verification/programmes/oi-qm/reconstruction/composition-access-20261024
    (cd $D && python3 -I -B checks.py | cmp - RESULT.json)
    (cd $D/review && python3 -I -B independent_checks.py | cmp - independent-result.json)
    (cd $D/native-x-v2 && python3 -I -B checks.py | cmp - RESULT.json)
    (cd $D/native-x-v2 && python3 -I -B review/checks.py | cmp - review/result.json)
    (cd $D/tagged-post-y-v3 && python3 -I -B checks.py | cmp - result.json)
    (cd $D/tagged-post-y-v3/review && python3 -I -B checks.py | cmp - result.json)
    (cd $D/native-phase-v4 && python3 -I -B checks.py | cmp - result.json)
    (cd $D/native-phase-v4/review && python3 -I -B checks.py | cmp - result.json)
    (cd $D/native-coupling-v5 && python3 -I -B checks.py | cmp - result.json)
    (cd $D/native-coupling-v5/review && python3 -I -B checks.py --author-root .. | cmp - result.json)
    (cd $D/composition_flag_v6 && python3 -I -B checks.py | cmp - result.json)
    (cd $D/composition_flag_v6/review && python3 -I -B checks.py --author-root .. | cmp - result.json)
    python3 -I -B $D/delayed_history_v7/checks.py | cmp - $D/delayed_history_v7/result.json
    python3 -I -B $D/native_predicate_v8/checks.py | cmp - $D/native_predicate_v8/result.json

Each command also holds with `python3 -I -B -O`. The top-level and
`native-x-v2/` checkers compare against their retained `RESULT.json` and
create it only when it is absent. The two last checkers take about one minute
each and exit with status 2, printing `VOID`, if a required control fails;
the others take seconds. The mutant campaign of `native_predicate_v8/` runs
from an empty directory in about six minutes:

    mkdir mut && python3 -I -B $D/native_predicate_v8/mutants/run_mutants.py \
      $D/native_predicate_v8/checks.py mut | cmp - $D/native_predicate_v8/mutants/mutants.out

Each directory with a `SHA256SUMS` verifies with `sha256sum -c SHA256SUMS`
from that directory. The reviewers' scripts and outputs are records of their
reviews; `delayed_history_v7/review/README.md` gives the command that
regenerates its round-2 mutant summaries.

## Provenance

- The #910 commits the packages cite (`f24a57a7`, `1c91d315`, `1b729355`,
  `1324d9a8`, `05397c79`, `71d29129`, `9b334367`, `5f6786d6`, `f264dff4`)
  are on `main`. The #910 files read at those commits for results
  (`native_x_v12/`, `native_seed_v12/`, `history_v11/`,
  `shared_v12/INTERFACE-CONTRACT.md` at `05397c79`, `phase_joint_v10/`,
  `reset_v8/`, `parallel_v3/direct_reset/`) are unchanged on `main`; its
  `CURRENT-HANDOFF.md` and `EQUIVALENCE-OBLIGATIONS.md` are read at the
  commits cited.
- `native-coupling-v5/PROVENANCE.json` pairs `shared_interface_commit`
  `1324d9a854da60d0274ba77fe80d08e7cf2b1ef1` with `shared_interface_sha256`
  `1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633`. That
  digest is of `shared_v12/INTERFACE-CONTRACT.md` at
  `05397c79370f66c88f0bf8fdaedb09297ba358a9` (blob `03857785`, the file on
  `main`), which adds the fixed local two-slice identity the package uses
  (its `PLAN.md` item 1); the file at `1324d9a8` has digest
  `95cd4d20222f92ed…` and lacks that identity. The contract the package
  rests on is the file at `05397c79`, as `composition_flag_v6/PROVENANCE.json`
  records; `1324d9a8`, named in its `PLAN.md` and `REPORT.md`, is the commit
  that first published the contract. The provenance file is pinned by its
  review and is not edited.
- `REPORT.md`, `native-x-v2/REPORT.md` and `review/REVIEW.md` cite the
  programme's acceptance rule at commit `2d555f17`, on #885's branch
  `research/missing-component-20261020`, as provenance. No result here rests
  on it.
- `native-x-v2/SOURCE-EXCERPTS.json` holds verbatim excerpts, with their
  source digests, of the native-X candidate in the off-repository archive
  `OI_combined_handoff_2026-10-24_v1`. The checks establish properties of the
  retained excerpts; that they are what the archive holds is provenance.

## Related work

Native construction is in `../native-y-continuation-20261024/` (#910), and
architecture and finite approximation in `../states-dynamics-audit-20261024/`
(#911). Wider gates are tracked in Issue
[#913](https://github.com/amaybaum/incompleteness/issues/913). No result of
theirs is restated here.
