# Owner's independent review of the composition checkpoint, and the coordinator's response

> **DRAFT — research record.** The roles are reversed from earlier reports. The coordinator's session wrote the
> composition investigation (`design/composition/`, checkpoint `43400ea7`). The owner's session reviewed it
> independently, and this report records that review with the coordinator's verification and the corrections applied.
> It adopts no premise.

## Verification of the review package

- **Archive.** The sha256 is `f132873c615c5e8cda34035c298b04af4f34e447a7f8c3ae56decc3f60431f02`, as stated. The
  files in `handoff/` are its contents, unchanged. Both `SHA256SUMS` manifests verify: the review's own, and the one
  in `source/`.
- **The reviewed source is unchanged.** The 15 files in `handoff/source/` are byte-identical to
  `design/composition/` at `43400ea7`.
- **Code review before running.** `independent_checks.py` uses only the standard library. It imports the reviewed
  `builder.py` as the candidate under test, disables bytecode writes, and writes only to stdout.
- **Replay.** Run from a separate directory with `python3 -I`, normally and with `-O`, the output is byte-identical
  to `independent_checks.out`. Each run takes about 4 s. The review's own replays of the source checker
  (`normal.out`, `optimized.out`) equal its saved output.

## What the review establishes

- **The all-n argument holds** under the stated affine readiness resources:
  - the first-arrival reduction is exact;
  - the wings are linear, with no omitted crossings;
  - the Pascal inverse is proved;
  - the S₈ group and its commutator certificates were recomputed independently;
  - the balanced AND formula follows by induction;
  - the identity padding terminates for every n.
- **Separate implementations confirm it:**
  - a scalar full-torus update at n = 2, on dense backgrounds, with a silent prefix;
  - 24 arbitrary non-planar 3-D shell cases against a raw second-order recursion;
  - an integer-bitset sweep of n = 2–13, including the new sizes 10, 11 and 13, giving the full terminal triple,
    degree n and source rank n;
  - a released-chain-pin countercontrol at every one of those sizes.
- **All-size resource formulas.** With k = ⌈n/2⌉ and G(k) = 2^h(3k − 2^(h+1)), h = ⌊log₂ k⌋:
  - 6G(k) + 1 ≤ T(n) ≤ 8G(k) + 7, so the latency is Θ(n²);
  - C(n) = 8T³ + 16T − n = Θ(n⁶);
  - the ready set has exactly 2ⁿ cone states.
- **A new corollary.** ANDₙ for arbitrarily large n rules out any conjugacy of this rule to linear dynamics with
  forward and inverse degrees bounded uniformly in lattice size and time. That is stronger than report18's finite
  g·g′ < 10.

## Corrections: accepted and applied

1. **Unrun is not failed.** The verdict stands as "preregistered success not established".
2. **Countercontrol coverage.** The published checker runs criterion 3's structural controls at n = 4 only.
   `REPORT.md` Section B no longer says criterion 3 is met; it cites the review's reduced-model controls at
   n = 2–13 as a post-publication check.
3. **Resource contract.** The builder uses multi-input affine XORs (at n = 12, 644 of 1342 source entries), not the
   preregistered single-input copies, and gives no closed-form copy count. Section B records this expansion and the
   review's all-size bounds.
4. **Unused option.** The checker's docstring no longer advertises `--with-3d-78`; it names `check3d.py 7 8`. The
   output is unchanged; a replay is byte-identical.
5. **Chronology.** Section B and the composition README state that hashes establish content consistency, and that
   the preregistration and Section A predating the held-out runs is the author's attestation. All files were first
   published together at `43400ea7`.

Two further clarifications are added to the composition README:
- the canonical extraction behind `REPORT-sectionA.sha256` (the prefix before `## Section B.`, trailing whitespace
  stripped, one newline added). The Section A digest is unchanged: `be34414b…`.
- the two `assert` statements, which `-O` disables.

`CONDITIONS.md` entry 1 now records the corollary as proved and independently reviewed, with its scope.

## Relevance to the next target

The review names the next deliverable: one bounded native instrument with all of the following stated:
- explicit prepared distributions;
- herald and clock records;
- side-register access;
- outgoing state;

followed by the complete-record identities and the instrument-closure test. The aggregation construction is a
component for that. It neither selects the angular law nor supplies native preparation.

The review also cites a "preparation-geometry handoff" with hidden-overlap requirements for prepared ensembles. That
handoff has not reached the coordinator and is not recorded here. The C-SPH-1 checkpoint stays closed.
