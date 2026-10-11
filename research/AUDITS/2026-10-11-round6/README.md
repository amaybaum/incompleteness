# Round-6 closure audit

Audited source: research/round6-transfer-sourcing at
694219a43bc9af449784c2b4dbc5b38b44df96a2. Certified base:
9f9f8257a980a1819fbbc1dc0019917cf8678626. Overview checked at
5d3ccb3e737ded9dfccaabacc3ee901312cf5b20. EVIDENCE.json records the source
blob IDs, inbox identities, chronological LOG prefix checks and thread diffs.

| result | audit disposition | evidence and limit |
|---|---|---|
| B22-1, unitary transfer source | OPEN upheld | I3.150-I3.153 and I3.165 are open or introduced; existing test bridges give an upper bound, not operation invariance |
| B22-2, channel transfer source | OPEN upheld | I4.66 explicitly preserves PSD matrix states; I4.38 at ImplementationLocality:971 derives that validity, not preservation of an arbitrary P-level pair cone |
| B22-3, countercontrol | scoped construction-level obstruction upheld | full class with K(Z_F); independently rebuilt dual tests give drive -1/10 and mixer -1/8 in round7-channel/channel_check.py ZF; not full-model independence |
| B22-4 and B22-AW | conditional statement upheld at written level | arbitrary identified state space C requires validity on C, dict '' K identification, ContextStable and LabelInvariant for the spectator step; at C=PSD the identification is K=Q3 |
| E23-1, H2 | OPEN upheld | I3.148 is assumed; availability of a CNOT permutation does not give preservation of K without pair transfer |
| E23-2, H3 | OPEN upheld | I3.149 is unsourced; the nearest CSD2 source is unresolved; single-token Lorentz self-duality is not pair self-duality |
| E23-3, A_miss | OPEN upheld | the available-operation routes still require transfer; E19 supplies a conditional characterization, not its premises |
| B23-1 | FAILED upheld | exact run 38151796092, head fd364020, Build errors at lines 100,103,105, PartialOrder complex; six standard axiom reports, one sorryAx; release gate skipped |

## Provenance and scope

Ten cross-thread inbox copies have the same Git blob IDs as the issued handoffs.
The LOG at each of all seven source commits extends its predecessor byte for
byte (six comparisons). The initial preregistration is an unchanged prefix of
the final one. NOTES-B23 and NOTES-E23 retain their first committed texts as
prefixes. NOTES-B22 has two in-place clarifications adding "in its actT form"
to the rotation reading, plus an appended failed-build update; it must not be
described as wholly append-only. The LOG append-only requirement is satisfied.
All 20 changed paths from overview 1325160c to the cross-thread head are
inside research/round6-transfer/. The saved failed Lean source has the same
blob 2c7c56b63c7ac82f95a63e566c7c431870914e0c as the dispatched source.

The four threads' new inbox copies are independently checked here as 4/4,
5/5, 6/6 and 8/8 identical for bridge, countermodels, origin and equivalence.
Their endpoint LOG diffs have zero deleted lines; countermodels' NOTES-C23
and RESULTS and origin's RESULTS also have zero deleted lines. This confirms
the endpoint preservation. The launching coordinator's recorded replay of
c23f_correction.py (6/6) and origin rendering check are prior audit evidence;
this audit does not relabel them as newly replayed here.

The job log was independently retrieved in full, 38,860 lines, on 2026-10-11,
not limited to the earlier record's 5,000-line tail. SHA256 of the decoded
retrieval: 664b88467cb9027e70de42e92ecee0125520d12974ef7f1268a17dfa4c132a79.
The diagnostic excerpt is saved in CI-FAILED-B23.log; the full run remains at
https://github.com/amaybaum/incompleteness/actions/runs/38151796092.
No untested 6136-result census or expected release-gate count is reported as
observed. No statement of the failed module becomes [D].

## Findings and forward corrections

F-R6-1: overview's central-question paragraph overstates independence as
covering all 199 applicable rows of the 633-record inventory. The supported
countermodel statement covers the 118 reached rows; 68 NOT REACHED rows
remain unresolved. Correct the live overview forward, leaving archived
records untouched. Full-OI independence and unconditional reconstruction are
OPEN. This correction does not change a mathematical verdict.

F-R6-2: the missing ComplexOrder scope is confirmed; the repair is registered
as new round-7 work before its one design run. Preserve the failed source and
run. The module still assumes its availability/convergence witness.

Round 6 is closed at its narrowed scope. Deferred research remains deferred,
except the channel controls and repair explicitly taken up by round 7. The
new saved checker and written arguments are new round-7 evidence, not results
retroactively credited to round 6. Full-model counterexamples, token geometry,
general-k Lean availability and S6 integration remain separate obligations.
