# Native source assessment for one balanced mixer

**Status** Scope checkpoint. The paper assessment and independent review are pending.

**Base** [OI main at 192bbf2](https://github.com/amaybaum/incompleteness/commit/192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7). The owner assigned the bounded paper-only assessment to Codex E in the November 18, 2026 chat. [Accountable bridge issue #1211](https://github.com/amaybaum/incompleteness/issues/1211)

**Goal link** Determine whether one fixed microscopic evolution and its existing observer interface supply a phase-sensitive mixing operation that can be reused. This addresses the forward bridge and informs the operation-source obligations in [#914](https://github.com/amaybaum/incompleteness/issues/914) and [#1169](https://github.com/amaybaum/incompleteness/issues/1169).

## Target and decision rule

The target is one balanced operation on two physically identified alternatives. From either input, one use gives equal weights on the two alternatives. Two consecutive uses without an intermediate read, reset or postselection give certain transfer into the other alternative. The same operation, preparation procedure for each input, and output read apply at every use. To count as an available intervention, the source must specify how it can be applied or bypassed under the same microscopic law. The comparison uses the existing normalized SM wave branch and its even and odd spatial sectors. [SM §4.1](https://github.com/amaybaum/incompleteness/blob/192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7/papers/SM.md#L218-L232) · [SM checkerboard](https://github.com/amaybaum/incompleteness/blob/192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7/papers/SM.md#L531-L539)

The matching frequencies are a benchmark. Qualification requires a forward derivation of the acting carrier, available operations and controls, and record law from one identified physical setup. A proof of conditional amplitude dynamics can locate a missing source. A classical response table or passive time history can match finite frequencies, so those frequencies alone cannot qualify a physical mixer. [Main §3.4](https://github.com/amaybaum/incompleteness/blob/192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7/papers/Main.md#L594-L604)

| Verdict | Criterion |
| --- | --- |
| SOURCE QUALIFIED | The existing sources identify the concrete physical realization, its usable mixer and its record law on the same setup. |
| CONDITIONAL | An independently motivated physical candidate is identified and the operation follows under explicitly stated outstanding conditions. |
| UNSOURCED | The earliest required physical identification has no source on the examined route. A mathematical amplitude benchmark may still be available. |

The paper assessment stops at the first unsupported forward step. It uses the existing field branch and read/write interface as sources. The apparatus and acceptance work are coordinated separately. [Session B's draft #1378](https://github.com/amaybaum/incompleteness/pull/1378) · [Coordination #1169](https://github.com/amaybaum/incompleteness/issues/1169)
