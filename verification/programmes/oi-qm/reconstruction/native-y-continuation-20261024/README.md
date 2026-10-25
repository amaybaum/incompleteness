# Native computation and parallel reconstruction research

Bounded research on native instruments for the OI-to-QM reconstruction
programme: the actual masked phase of the native-Y construction and scoped
native tests on it. Every package has a separate-agent internal review
(that of `continuation/` is in `parallel_v3/review/`). The packages from
`reset_v7/` on carry a plan (`PLAN.md` or `PROBE-PLAN.md`); the five
earlier packages, `continuation/`, `parallel_v3/`, `junction_v4/`,
`six_source_v5/` and `outward_v6/`, carry none.
[CURRENT-HANDOFF.md](CURRENT-HANDOFF.md) states the results and their scope.
[EQUIVALENCE-OBLIGATIONS.md](EQUIVALENCE-OBLIGATIONS.md) places them among
the programme's reconstruction paths and open gates.
CHECKPOINT-CHECKS.json records the checks run on this directory.

The native tests exhibit useful physical coupling and close precise shortcut
classes, each for its own construction. They do not supply an implemented
acceptance gate or a reusable instrument. A1 and A2 remain separate, and the
supplied geometric probabilities are not selected by OI. No result here is an
OI-wide no-go, and no full OI-to-QM equivalence follows. Separate-agent
internal reviews are distinct from commissioned independent programme review,
external validation, formal certification and owner adoption.

## Replay

From the repository root, with the Python 3 standard library and a C++17
`g++` (used by `six_source_v5/`):

    D=verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024
    python3 -I -B $D/replay.py
    python3 -I -B $D/replay.py --latest

`replay.py` verifies `SHA256SUMS` and the reviewed input hashes, compiles
every Python file, and runs each checker group on a temporary copy of this
directory, normally and with `-O`, comparing its output byte for byte with
the recorded output. Without arguments it runs all 60 groups; `--latest`
runs the seven groups of `native_gate_v13/`, `native_route_v13/`,
`native_decode_v14/` and `native_vread_v15/`, with the v13 and v14 reviews.
Each checker run is limited to 180 s; on a heavily loaded host a
`TimeoutExpired` stop is that limit, not an output mismatch, and the run can
be repeated.

The whole-V read's own commands add its mutant campaign and nested manifest,
which `replay.py` does not run:

    python3 -I -B $D/native_vread_v15/checks.py | cmp - $D/native_vread_v15/result.json
    python3 -I -B -O $D/native_vread_v15/checks.py | cmp - $D/native_vread_v15/result.json
    python3 -I -B $D/native_vread_v15/mutants/make_mutants.py | cmp - $D/native_vread_v15/mutants/OUTPUT.txt
    (cd $D/native_vread_v15 && sha256sum -c SHA256SUMS)

These are the commands of `native_vread_v15/REPORT.md`, whose replay section
starts from a clone of the research branch; they run unchanged from a
checkout of `main`.

## Labels and provenance

- A1 and A2 name the programme's two reconstruction targets here: exact
  reconstruction and finite operational approximation. They are distinct
  from the structural conditions A1–A6 of the manuscripts.
- Several packages cite off-repository archives by path and SHA-256: the
  combined handoff `OI_combined_handoff_2026-10-24_v1` and the earlier
  `OI_native_Y_continuation_handoff_v1`. Neither is in the repository; both
  are provenance. In `transport_audit_v1/`, "the retained combined handoff"
  is the first of these: the audit restates the lemmas it accepts, and the
  inherited report itself is not retained.
- `parallel_v3/new_geometry/SOURCE-GEOMETRY.json`,
  `parallel_v3/history_control/SOURCE-GEOMETRY.json` and
  `parallel_v3/direct_reset/herald.json` are retained input data. The
  two `SOURCE-GEOMETRY.json` files are taken from `AUTHOR-DATA.json` and
  `herald.json` comes from `compiler.py`, both in the combined handoff and
  not in the repository. The checks establish the stated properties of the
  retained data; that the data is what those handoff files give is
  provenance, not re-derived here.
- The programme synthesis these tests start from is on #885's preserved
  branch, as provenance (CURRENT-HANDOFF.md).

## Related work

Architecture and finite approximation are developed on
[#911](https://github.com/amaybaum/incompleteness/pull/911), complete-record
composition on [#912](https://github.com/amaybaum/incompleteness/pull/912),
and the wider open gates are listed in
[#913](https://github.com/amaybaum/incompleteness/issues/913).
