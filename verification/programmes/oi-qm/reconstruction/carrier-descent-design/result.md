# Carrier-descent design rebuild

Research-only work for [#823](https://github.com/amaybaum/incompleteness/pull/823).
Drafting snapshot D is `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.
This branch starts at finite-reconstruction design commit
`05d96d71e55a6c008f53c5b568e8523d6e849256`; its landed Lean imports agree with D.
No native F has been designated. This record does not execute KN-DESC-1,
adopt a kernel module, or change a manuscript or the ROADMAP.

## Mathematical surface and retained premises

`KnDescentDesign.lean` rebuilds the original research proof in namespace
`OIBridge.KnDescentDesign`, outside the adopted `OIBridge` module directory.
Its twelve theorems and twelve axiom prints cover:

- Admissible operators compress along any injection `S ↪ T`, with `S` nonempty.
  The proof uses `ContextStable` at spectator `S`, `LabelInvariant`, and
  `Architecture.block`. It does not use the other architecture fields.
- The three elementary generators compress to their counterparts on `S`:
  transition flows (including `a = b`), transpositions, and quarter-phase gates.
- Elementary drivability descends along embeddings; drivability at all
  `Fin (2 ^ k)` gives `DrivesElementary` at every finite carrier. The empty
  carrier is treated by vacuity, not by the nonempty compression lemma.
- `QuantumArchitecture` with its existing closure clauses has the equivalent
  formulation using drivability at the power-of-two carriers. The forward
  direction names `drivesElementaryAt_of_drives`; the reverse direction names
  `drivesElementary_of_pow`. `DaggerStable` is retained on both sides of the
  architecture statement, although descent itself does not require it.

These are implementation-repertoire statements in an already carrier-general
matrix formalism. They do not construct a physical odd-dimensional carrier,
identify an admitted state cone with PSD, derive its preservation, or source
the power-carrier drivability premise. In particular, descent to `Fin 3`
uses an odd-sized spectator through carrier-general `ContextStable`. It cannot
be interpreted as a construction using only physical qubit systems.

The companion k-token reconstruction work concerns matrix state cones and
exact gate generation. To use it here one still needs a dictionary into the
same implementation class and admission of the exact finite words. A cone
identification alone does not give that repertoire interface.

## Provenance

Original source: research thread `research/equivalence` at
`424aa33bf16c5160c00e6f6aea974d00c0d745dd`, node E8:

| Original path | Git blob |
| --- | --- |
| `research/equivalence/lean/EqvKnDesc.lean` | `8157f8eaf77a080391c54e518f4c6f3bb4de8f56` |
| `research/equivalence/NOTES-E3.md` | `ebb062e91d608c204a8dde1128724e93a519387c` |
| `research/equivalence/experiments/e3_compress.py` | `a8f1ef39b11179fbbf0aacf836d7dc8c1558f8be` |
| `research/equivalence/experiments/e3_compress.out` | `ad606f0eaa8aec9b14f79c3a80157016572df6ac` |

The Lean proof body is retained. Only its header and namespace are changed
for the research-only rebuild. Historical design run 38090116254 is evidence
for the original module at its historical base, not a fresh build at D.
The exact source and expected output are copied byte-for-byte, with the
original Git blobs verified above. `independent_check.py` is newly written
without importing that source or using SymPy.

## Exact evidence and design-build status

The original probe reproduces its saved output byte-for-byte: seven checks,
zero failures, empty stderr. It requires SymPy (rerun with 1.14.0).
Its symbolic time controls exercise 32 ordered distinct-index pairs across
three carrier embeddings. The new standard-library Gaussian-rational checker
passes 2410 controls with empty stderr. It checks all ordered pairs including
self-index flows, all spectator choices, four exact points on the unit circle,
non-Hermitian arbitrary-kernel compression, and negative controls for an
incorrect relabelling and a flow that leaves the compressed subspace.

These finite checks supplement the universal proof. They do not certify a
universal claim by themselves. A fresh Lean run against D's library is
pending; compilation and the twelve axiom prints must be checked before
calling this rebuild kernel-checked. There is no local Lean executable or
Mathlib cache in this workspace. Root's disposable research CI will perform
the rebuild without adding an adopted import or a permanent job on main.

Replay commands from the repository root:

```sh
/workspace/incompleteness-venv/bin/python -I verification/programmes/oi-qm/reconstruction/carrier-descent-design/source_e3_compress.py
python3 -I verification/programmes/oi-qm/reconstruction/carrier-descent-design/independent_check.py
```

Compile from `verification/lean-mathlib` after building the landed imports:

```sh
lake build OIBridge.SubstratumSource OIBridge.LiftAudit
lake env lean ../programmes/oi-qm/reconstruction/carrier-descent-design/KnDescentDesign.lean
```

## Items to correct in the un-frozen control-plane draft

At #823 head `c83954a5b7b8971eb3e5296912e403423fe0167e`, the exact-layer
paragraph calls `e3_compress.py` standard-library-only. Its original source
imports SymPy; that environment dependency should be explicit before F.
The listed Lean surface has thirteen declarations: one definition and twelve
theorems, alongside twelve axiom prints. The draft's phrase “twelve
declarations” needs that distinction. The source sample excludes `a = b`;
the new independent checks cover that case and the Lean proof has a separate
idempotent-exponential argument for it. The historical warning-cleanup choice
remains a pre-F design decision; this rebuild keeps the effective signatures.

Under §A.31 this rebuild is CONFIRMING. The original node's discovery and
priority remain with its research thread; these new controls do not produce
a new physical principle or discharge the Kₙ source obligation.
