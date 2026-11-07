# Classical retention: physical-register and later-read lead screen

**Status: WIP / UNVERIFIED; selection review pending.** This is a new source-gated paper investigation,
accountable to #1032 and feeding #1169. No register is selected and no retention derivation is made
in this checkpoint. The deliverable may be a precise no-qualifying-lead result.

The owner asks: “Name one physically motivated register and its later read interaction. Screen both
against Theorem N and the relevant PAD/NP obstructions before doing the derivation.”
The recorded authorization is [#1032 c.6712887557](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6712887557)
(amaybaum, 7 November 2026). Source/literature reconnaissance, the lead-selection packet, draft
publication and independent review are authorized. Derivation awaits independent source/obstruction
review of a concrete register **and actual later read interaction**. A supplied mechanism or read
port is the stopping point.

## 1. Evidence and scope already fixed by the sources

The pinned starting point is main `b1d782f954f02cec578a10e071b73e48f86eb3dd`. The operative guide is
`AGENTS.md`, blob `496eb7018c736a064dddcf00fd1a278790872f49`. This unit changes only this new
directory; old Phase A inputs, the landed negative and earlier design drafts retain their status.

| Source | Supported statement and role |
| --- | --- |
| [THEOREM-N.md](../phaseB-negative/THEOREM-N.md), §3.2, §4.10, §6 | An independently model-reviewed paper negative for the specified binary K1/SMR family `𝔉`: rings `N∈{5,7,8}`, the stated fixed registers and product preparation laws, four carrier preparations, current-slice read, fixed deterministic decoder, Phase A J-1/ST classifier, `T≥1`, `ε*<1/4`. This is support on main for that scope. |
| [THEOREM-N.md](../phaseB-negative/THEOREM-N.md), §4.1–§4.3, §4.7 | PAD, NP, AE and SS-2 have their own hypotheses; being outside the coverage table does not establish escape from these wider propositions. |
| [REVIEW.md](../phaseB-negative/REVIEW.md), §1, §5, verdict | Supports the landed extract's paper mathematics and citation roles. It supplies no physical preparation, read mechanism or new scientific execution. |
| [README.md](../README.md), “Paper results” | The earlier route lemmas are not independently validated on main and are not imported as established premises. |
| [SOURCES.md](../SOURCES.md), “External literature” | The earlier Landauer, Bennett and Wolpert attributions were from memory; their texts were not read in that unit. Bibliographic metadata and a named citation do not source a new physical mechanism. |

The completed [O5 screen #1177](https://github.com/amaybaum/incompleteness/pull/1177) at
`3ec25f1fbe18e822924f6e834f8fa072a8f4244c` is historical negative context, not a candidate here.
The [completion record](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6693107383)
reports that the binary SMR `N=8` stencil register `A={7,1,2}` lacked physical joint read sourcing
and that PAD/NP covered its retained laws. It supplied no unresolved tuple or second-hold result.
This screen does not substitute another geometry or tune that family's preparation.

## 2. Obstruction screen required before selection

The following are existing paper results, labelled **derived** only on their stated hypotheses.
No row licenses a physical premise merely because one hypothesis fails.

| Result | Hypotheses that must be checked against a physical lead | Consequence |
| --- | --- | --- |
| PAD, §4.1 | Copy form; `x_A(t₀)` uniform on `𝔽₂^A` and independent of `W=(y(t₀),x_{Λ∖A}(t₀))`; carrier `κ` a function of `W` | First-tick current readout is carrier-blind; `ε_max≥1/2`. Full support alone is not this hypothesis. |
| NP, §4.2 | Centre-free copy-form setting of §3.1; product carrier/background law; both `x₀` values available for some fixed `c=y₀`; first-tick current read depends on `c` | Carrier site belongs to structural outside input `Q`; J-i fails unless `G₀(y(t₀))` is uniform. An exception is necessary, not sufficient. |
| AE, §4.3 | Binary additive carrier entry with fixed coefficient; product law; all four carrier preparations; stated locus/read/`Q` | Either first-tick error is at least `1/2`, or exact DIL∃ fails and every consistent Lemma H bound at `t₀+2` is at least `1/2`. |
| SS-2, §4.7 | Centre-free copy form; one-site two-slice locus; current-slice read; register current slice fixed at `t₀` | J-i at `t₀+1` forces carrier-blind current read at `t₀+2`; no product-law assumption is needed. |
| Theorem N, §4.10 | The full family `𝔉` of §3.2 and classifier §3.3 | No storage row at the stated tolerance, for any fixed deterministic decoder or `T≥1`. |

The separate full-support, finite-`S`, copy-form exact-recovery obstruction concerns fixed
current-slice reads at two consecutive ticks. Its precise source and hypotheses must be inspected;
it is not promoted here to a universal physical no-go. Likewise, `t₀+2∈W_T` already for `T≥1`
does not by itself establish a second **hold** tick: the source window and hold conventions must
remain explicit.

## 3. Selection gate and stopping rule

A qualifying lead must come from an independently motivated physical mechanism, with a consequence
independent of the desired retention outcome. The source map must identify the register's degrees
of freedom, physical write process, and an actual later interaction producing a readable output.
A previous-slice copy, static decoder, prescribed moving partition, declared isolation or ready
reservoir is insufficient.

Before derivation, the independent reviewer must check the physical source against the rule,
full joint starting law and preparer, both available carrier preparations, later read timing and
observer access, and every applicable obstruction above. A later decoder's carrier sensitivity
must not be inferred from an input it already knew at the write tick. D1/D2 and write-tick-only
input cases remain owner questions. The corrected criterion's provisional adoption for the old
classical O5 design is not extended to this unit.

If the gate passes, a subsequent authorized paper checkpoint must state all failure outputs,
resources, full outgoing carrier/apparatus/environment state and correlations, absence of automatic
reset, and the readable record through the second hold tick. Any positive also needs common
carrier, fixed update, timing and access compatibility with #866 and Claude's Q-A, including parity
leakage under reuse or recombination. Classical retention alone establishes no coherence across
a read; #1032's separate coherence obligation and #1143's distinguishing test remain separate.

**Current strongest result:** the published obstruction record narrows what can qualify; no
physically sourced register/later-read pair has been selected. Primary-literature and corpus
reconnaissance remain to be completed. No simulation, enumeration, implementation, Lean work,
scientific computational search, new premise adoption, freeze, special dispatch, merge or
manuscript promotion is authorized by this record.
