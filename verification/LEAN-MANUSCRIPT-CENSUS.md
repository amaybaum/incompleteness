# The Lean-to-manuscript census — every manuscript claim against the strongest theorem proved

`tools/lean_manuscript_census.py` (the check, run by the release gate as `lean-manuscript`),
`verification/lean-manuscript-census.json` (the registry it reads), `OIBridge/TypedPositive.lean`
(the one kernel result the census required), guard `R7-MSP` in
`verification/lean/edge_rigidity_probe.py`.

**Status: complete relative to the maintained registry, and enforced.** Every kernel identifier
cited in a manuscript resolves to a declaration; no manuscript paragraph cites a superseded theorem
without its successor; every `OIBridge` module carries a disposition; every family the manuscripts
carry names at least one anchor, and every anchor is present in the manuscript it names. The gate
fails on any of these. What the gate cannot do is infer that a theorem inside an existing module
has become stronger: a strengthening whose supersession entry or anchor is not recorded passes all
four checks. The guarantee therefore rests on one contract, stated in `AGENTS.md` §A.35 and pinned
by `R7-MSP`: every publication-facing strengthening of a theorem inside an existing module updates
the registry in the same commit, with a supersession entry for the identifier it replaces and an
anchor for the statement the manuscripts must now carry. Under that contract, a strengthening that
reaches the verification notes and the guards and not the papers is caught at the next run; a
strengthening that reaches neither the papers nor the registry is a contract violation, caught in
review and not by the gate.

## The rule

> Every manuscript-level scientific claim reflects the strongest applicable Lean theorem currently
> proved. Verification-only machinery is not narrated.

The registry makes the rule mechanical. Each module belongs to exactly one family, and each family
has one of five dispositions:

| disposition | meaning |
|---|---|
| `current` | the manuscripts state the family's conclusion in the form of its strongest theorem, and the registry names anchors that must be present |
| `consistent-uncited` | the manuscripts state the conclusion in their own derivation and place no kernel pointer; the wording is consistent, anchored, and a pointer pass is an owner decision |
| `scope-consistent` | the manuscripts carry the family's scope qualification, anchored; the positive result itself is not narrated |
| `kernel-only` | a publication-facing result with no manuscript occurrence; no manuscript sentence contradicts it; adding it is an owner decision |
| `verification-only` | helper lemmas, assembly, boundary ledgers, countercontrols and independence scaffolding; no manuscript propagation |

The three dispositions under which the manuscripts carry the family, `current`,
`consistent-uncited` and `scope-consistent`, each require at least one anchor, so a result the
manuscripts are recorded as carrying cannot disappear from them unnoticed. A citation of a
superseded identifier is legitimate only in a paragraph that also cites the successor, which is
how a historical form (the five-condition characterization, the OI⁺ layered form, the
dagger-stable package) is stated as what it is next to the current statement.

## The census at this commit

| family | modules | disposition | manuscript |
|---|---|---|---|
| representation bridge and counting | 7 | consistent-uncited | SM §4.6: the cubic counting layer, stated in the paper's own derivation, anchored at the link-representation decomposition and its multiplicities |
| equivalence chain and memory | 17 | consistent-uncited | Main §3.4: the finite-horizon equivalence, memory and necessity, separability threshold |
| Hamiltonian reconstruction | 11 | current | GR §3.3: the two-branch D-gauge theorem, thermodynamic orientation |
| coherent completions | 16 | current | GR §3.3: lift obstructions, the coherent-completion classification, the orientation no-go; the quotients underwrite no manuscript statement |
| instruments, dilation and assembly | 16 | verification-only | machinery of the completion classification; `countermodel` is cited as a witness |
| completion classification and the primitive-source chain | 26 | current | GR §3.3, Main §3.4, Explainer, book chapters 1 and 19: five conditions, OI⁺, `OIPlusPos` |
| substratum source | 4 | current | GR §3.3 substratum-source form and its endpoint |
| typed completion | 2 | current | GR §3.3 typed form, cited from the current package |
| quasilocal completion | 4 | current | GR §3.3 infinite-region completion with its scope |
| instrument audit | 2 | scope-consistent | the infinite-instrument scope qualification |
| continuous time (CT2) | 4 | kernel-only | the norm-continuous local automorphism path; the manuscripts' statement that a continuous-time Hamiltonian law is additional structure is consistent with it |
| minimal repertoire | 1 | current | GR §3.3 states phase-free richness as the second primitive-source principle, `OIPlusMin` boxed, the elementary repertoire as its stronger form; Main §3.4, the Explainer, book chapters 1 and 19 carry the summary; `carrier_general_oiPlusPos`, `oiPlusPos_iff_qm`, `hControl_star` and `typed_determined_of_oiPlusPos` are superseded and cited beside their successors |
| OI-N passive observation | 4 | kernel-only | the frozen exploratory thread; not narrated |

## What the census found and repaired

Three stale citations, all in the primitive-source chain and all at the seam the inverse-clause
result moved:

1. The strongest characterization named reversible implementation locality and cited the
   dagger-stable package (`carrier_general_oiPlusElem`) in GR §3.3, Main §3.4, the Explainer and
   both book chapters with their mirrors. Repaired to implementation locality and
   `carrier_general_oiPlusPos`, with the well-formedness qualification on the derived inverse
   accessibility.
2. The OI⁺ reversible-richness certificate cited the reachability theorem with the inverse clause
   (`universalReachability_of_lieRank_unconditional`). Repaired to state that the Lie-rank clause
   alone supplies control, citing `control_of_lieRank` from
   `universalReachability_of_lieRank_positive`; the OI⁺ principle itself is unchanged, as the
   layered form.
3. The typed form cited the package-level corollary from the dagger-stable package
   (`typed_determined_of_oiPlusElem`). The kernel had no corollary from the current package, so
   `TypedPositive.typed_determined_of_oiPlusPos` supplies it, one result, and GR cites it.

Nothing else was stale: the five-condition characterization and the OI⁺ layered form are stated
as such next to the strongest statement; the elementary repertoire, the substratum endpoint, the
typed and quasilocal scopes, the reconstruction and coherent-completion results are current.

## Two families with no manuscript occurrence

`CT2` and `OI-N` are proved, publication-facing, and absent from the papers. No manuscript sentence
contradicts either. The owner has decided to narrate both, CT2 in the continuous-time discussion
and OI-N visibly outside the equivalence theorem; the registry keeps them `kernel-only` until those
rounds land, each entering its anchors with its manuscript edits.

## The minimal repertoire, propagated under the contract

The minimal-repertoire round strengthened `carrier_general_oiPlusPos` to `carrier_general_oiPlusMin`
inside the corpus, and its propagation entered the four supersessions (`carrier_general_oiPlusPos`,
`oiPlusPos_iff_qm`, `hControl_star`, `typed_determined_of_oiPlusPos`) into the registry in the same
commit as the manuscript edits, with `TypedPositive.typed_determined_of_oiPlusMin` supplying the
typed corollary. That is §A.35 in use: every paragraph that cites a superseded name cites its
successor beside it, and the family's anchors pin the phase-free statement in every manuscript
that carries the summary.

## What this note does not claim

That the gate infers semantic supersession: it checks the supersessions and anchors the registry
records, and the registry contract of §A.35 is what makes the record complete. That the
`consistent-uncited` families have been re-derived against the kernel statement by statement; the
disposition records that the paper's own derivation carries them and that no kernel pointer is
placed. That the census reads the generated `.tex` forms beyond what `R7-MSP` pins; the
staleness check ties those to their sources. That the one driven transition of phase-free richness
is minimal in any stronger sense, or that the substratum supplies it.
