# M-INACC-1 amendment A3: post-result note on PROT-R

**This amendment does not affect any decision in this unit.** It is a
post-result amendment under A2.5. It was written after `RESULT.md` first
appeared (at `0e683793466bd4ff337683c15b0e7abd03da0db3`). It changes no
outcome, control, tier or verdict of this unit. `DESIGN.md`, A1 and A2 are not
edited.

WIP / UNVERIFIED. Writer: Claude Code session, 2026-11-08. It applies finding
F2 of the independent results review of `RESULT.md` at `0e683793`.

## 1. The defect

A2.1 added PROT-R to the decision:

> For every protocol of `Π`, every tick `t`, every linear functional `f` on the
> cells active at `t` with `Q*(f) = 1`, and every later tick `t′ ≥ t`: the
> value `f(t)` is neither determined nor biased given the observer's knowledge
> `K` at `t′`.

PROT-R fails in both linear limits `N_1` and `N_0`, and in QA's class N
itself.

**Countercase.** Take a ring, every cell a ready cell with known `u = 0` and
unknown `v`.

1. Tick 1 gives `u_0(1) = v_0(0) + f_0(u(0)) = v_0(0)`, because every `u` is 0.
2. Register `u_0(1)`.
3. The functional `u_0(0) + v_0(0)` of cell 0, which was active at `t = 0`,
   has `Q* = 1` and is determined at `t′ = 1`.

The same holds under `G_σ`. Self-check c5 of `RESULT.md` confirms the identity
on the instance `L = 5`.

**Reason.** AP1 Lemma 3 bounds what is determined about active cells. An
archived cell can be sharp: its registered slot and its transported known slot
need not commute. So `span(I_t ∪ R_t)` can contain `Q* = 1` functionals
supported on archived cells.

## 2. Its source

A2.1 adopted PROT-R on the premise, stated in the reviewer's confirmation of A1
(finding G1), that "`span(I_t) + R` has `Q* ≡ 0` on terminal and active cells
together". The writer's `RESULT.md` §6.3 found the premise false. The
independent results review of `0e683793` confirms the countercase and states
that its own G1 claim was false.

## 3. Consequences in this unit (unchanged by this amendment)

`RESULT.md` §6 applied A2.1's own clause:

- C-LIN is red for PROT-R;
- no (B-R) verdict is issued;
- outcome (A) is unreachable under the amended rule, for every rule.

Both outcomes of this unit are (B-D) exposures of current active functionals.
They rest on PROT-D and PROT-B, whose C-LIN controls are green. No verdict is
voided.

## 4. PROT-R′, offered to successor units only

> **PROT-R′(Π).** For `t ≤ t′` and a `Q* = 1` linear functional `f` on the
> cells active at `t`, such that the value `f(t)` is a function of the
> configuration of the cells active at `t′` alone, `f(t)` is neither
> determined nor biased given `K` at `t′`.

PROT-R′ restricts retrodiction to information still held by the cells that are
active.

**It holds in both linear limits** (`N_1`, `N_0`, under this unit's
conventions: refills as reserve cells, vacancies, multipliers, direct
registration, no heralds). The argument has three steps:

1. **Transport.** Free ticks, symmetric center-free steps and cell swaps are
   linear and symplectic and preserve `Q*`. So `f(t)`, being a function of the
   cells active at `t′` alone, equals `f′(t′)` for a linear functional `f′` on
   those cells with `Q*(f′) = 1`.
2. **Lemma Q(iii) at `t′`.** As extended in `RESULT.md` §6.3 (C-LIN), it gives
   that `f′` is not determined.
3. **(s5).** Uniformity on the affine knowledge set gives that `f′` is not
   biased.

The countercase of §1 is excluded, because its `f(0)` depends on the archived
cell 0.

PROT-R′ is not adopted. It is not part of this unit's decision rule and it
re-decides nothing here. Under `G_σ` in `Π_A`, `E_A` would violate it in any
case, already at `t = t′ = 2`, where PROT-R′ reduces to PROT-D.
