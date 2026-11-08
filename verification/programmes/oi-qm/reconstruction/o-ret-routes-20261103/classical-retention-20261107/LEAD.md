# Classical retention: one external register/read lead, stopped before native derivation

**Author source-selection finding: no qualifying native candidate. Independent selection review is recorded on [guiding PR #1186](https://github.com/amaybaum/incompleteness/pull/1186#pullrequestreview-5815049227).**
The single physical lead examined is an optically trapped colloidal position bit, with later camera
position readout. It has an external experimental source. The inspected OI sources do not supply
its native register, carrier write or later read process. Stop at that bridge; no retention
trajectory, second-hold result, storage row or counted pass is claimed.

This is the new paper-only unit authorized in
[#1032 c.6712887557](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6712887557)
(amaybaum, 7 November 2026), feeding #1169. The owner requires a physically motivated register
**and actual later read interaction**, screened against Theorem N and PAD/NP before derivation.
A no-qualifying-lead result is permitted. The starting point is main
`b1d782f954f02cec578a10e071b73e48f86eb3dd`, with `AGENTS.md` blob
`496eb7018c736a064dddcf00fd1a278790872f49`. Only this new directory changes.

## 1. What was read, and the role of each source

| Source | Role and limit |
| --- | --- |
| Bérut et al., *Experimental verification of Landauer's principle linking information and thermodynamics*, Nature 483, 187–189 (2012), [DOI](https://doi.org/10.1038/nature10872), [paper with Methods](https://www.physics.rutgers.edu/~morozov/677_f2023/Physics_677_2023_files/Berut_Lutz_Nature2012.pdf) | Primary external experimental evidence for the one physical lead below. The article and full Methods were read directly. No OI realization is inferred from it. |
| [THEOREM-N.md](../phaseB-negative/THEOREM-N.md), §§3–4, 6–7; [REVIEW.md](../phaseB-negative/REVIEW.md), §§1, 5, verdict | Support on main for the scoped paper obstruction and its exact hypotheses; independent model review, not an experimental or kernel result. |
| [Main](../../../../../../papers/Main.md), §1.3 C2/C4 | Structural reversible persistence, coarse-grained slow-bath persistence and accessible routing are distinguished. Slow-bath persistence is a physical-regime premise; it supplies no particular trap, write or camera interface. |
| [SM](../../../../../../papers/SM.md), §§3.1, 4.1; [Substratum](../../../../../../papers/Substratum.md), §2 | The second-order local rule and its scope; observer access is supplied by the partition. A two-slice state is not itself a physical read. |
| [MR-star](../../measurement-record-formation/amendments/MR-star.md), C-2–C-4 | The ready-supply gap and wake/record distinction, with the explicit refusal to infer that no ready supply can exist. Historical research context, not a universal absence theorem. |
| [Native link sourcing gate](../../../../substratum/continuous-substates/native-link-sourcing-gate.md), “Actual OI reference input” and “Fully specified but non-native link/pointer model” | Distinguishes the microscopic wave rule from an added pointer model. Its added apparatus is not imported as an available resource. |
| [Native apparatus register](../../../../substratum/continuous-substates/native-apparatus-register.md); [setting-source feasibility](../../../../substratum/continuous-substates/native-setting-source-feasibility.md), source trace and public-access sections | Existing conditional research constructions distinguish microscopic influence, preparation compatibility and public read access. They do not identify the colloidal experiment with the native carrier. Their probe results are not rerun or used as a general no-go. |
| [Substratum source audit](../../../../substratum/source-audit.md); [observer-interface audit](../../../../../audits/operational/stochastic-observer-interface-audit.md) | Source reviews of generic implementation, read/write, observation and ensemble structures. Their quantum off-diagonal-control limitations are not used to deny classical memory or actuation. |
| [O-RET README](../README.md), “Paper results”; [SOURCES.md](../SOURCES.md), “External literature” | Earlier route lemmas are not imported as established premises. The old Landauer/Bennett/Wolpert attributions were not textual literature reads in that unit; they do not source this lead. |

The repository-wide source search used `double-well`, `Kramers`, `Berut`, `metastab`, `optical`
and `Brownian`. Returned manuscript contexts were read in Main, Structure, Complexity and
book chapters 1, 3 and 13, alongside the source records above. The biology/optical and
non-Markovian examples concern their named effective systems; none of these inspected passages
specifies this trap-to-native-register and camera-to-native-record map. This is a bounded
source-search finding, not a proof that every possible OI apparatus lacks one. No new geometry
or preparation was selected from the old obstruction family.

## 2. The one physical lead and its later read

**External empirical source.** The register is the bead's left/right well occupancy.
The double well is maintained optically; a barrier suppresses thermal crossings. A fast camera
records later bead positions, sampled at 502 Hz. The experiment changes the barrier and applies
a controlled tilt to erase the bit. Its Methods reports barrier-dependent Kramers hopping and
an explicit reinitialization procedure. These identify a physical persistence mechanism,
a later implemented read, failure through thermal motion, and apparatus preparation, rather than
a static decoding function. The independent experimental consequence is the measured
erasure-heat dependence; the well geometry was not chosen to evade an O-RET lemma.
[Primary paper, main text and Methods](https://www.physics.rutgers.edu/~morozov/677_f2023/Physics_677_2023_files/Berut_Lutz_Nature2012.pdf).

**Limit of that source.** Camera tracking is an actual experimental output. It is not yet a
microscopic OI interaction law for generating a later public record. In particular, an image
sequence is not a specification of the imaging degrees of freedom, back-action, detector state
or subsequent readable register under the same native update.

The source studies erasure of a prepared memory. It does not identify an independent OI incoming
carrier whose unknown property is physically written into a distinct bead register while background
and controls are held fixed. Reusing the experiment's externally known preparation label would
therefore not demonstrate the requested carrier-sensitive write and later retrieval.

## 3. Screen against existing obstructions, before any candidate derivation

**Derived paper negative.** Theorem N covers its family `𝔉`: binary K1/SMR on rings
`N∈{5,7,8}`; the registers and product preparation laws of §3.2; a site-0 two-slice carrier with all
four preparations and target `y₀(t₀)`; current-slice read; fixed deterministic decoder;
the stated J-1/ST classifier, `T≥1` and `ε*<1/4`. It is not a universal retention no-go.
PAD, NP, AE and SS-2 also have wider individual hypotheses.

The external bead description is not specified as a tuple of that family. This fact supplies
**no certified escape**: without a native microstate map, the relevant joint law, locus, structural
parents and actual read are unknown.

| Existing result | Register and later-read screen for this lead |
| --- | --- |
| Theorem N, §§3.2, 4.10, 6 | A two-valued effective occupancy is not an identification with the binary K1/SMR ontology. No ring, native register geometry, allowed preparation family or fixed native read/decoder is supplied. Neither exclusion nor escape is inferred. |
| PAD, §4.1 | For copy form, uniform `x_A(t₀)∈𝔽₂^A` independent of `W=(y(t₀),x_{Λ∖A}(t₀))`, with `κ` a function of `W`, makes the first current-slice register read blind, `ε_max≥1/2`. The external thermal/controlled preparation has not been translated into those native variables. A barrier is not proof that this pad hypothesis fails. The camera output must be included in the read process, not granted as an extra decoder input. |
| NP, §4.2, within §3.1's centre-free binary setting | Under a product law with both `x₀` values for some fixed `c=y₀`, an informative first write places `y₀` in structural outside input `Q`; J-i fails unless `G₀(y(t₀))` is uniform. The lead supplies no native carrier/preparer, product-law proof, `G₀` or read-parent set. Neither the uniform exception nor failure of a hypothesis is established. |
| AE, §4.3 | Binary additive carrier entry with fixed coefficient, product law and all four preparations obstructs ST by first-tick error or the exact DIL∃/Lemma H alternatives at `t₀+2`. An effective nonlinear potential is not proof of non-additive carrier entry in the native register map. |
| LS/U, §§4.4–4.5 | These concern SMR geometry, readiness and structural carrier reach. No native geometry or readiness has been sourced here, so applicability is unassessed, rather than evaded. |
| SS-2, §4.7 | A centre-free copy-form one-site register with fixed initial current slice and current-slice read is blind at `t₀+2` if J-i holds at `t₀+1`, for any law. A single effective position bit need not be one native lattice site. Appending camera memory by declaration is not an escape. |

**Separate exact-recovery scope guard.** The historical P2-G statement in
[#914 c.6563955678](https://github.com/amaybaum/incompleteness/issues/914#issuecomment-6563955678)
concerns finite `S=X×Y`, a copy-form bijection `φ(x,y)=(y,F(x,y))`, full-support prior, and
single-time readouts `ρ_t(y_t)` with no retained previous read; a nonconstant function cannot be
exactly recovered at two consecutive ticks. Prescribed time dependence, or choosing a read
from the current slice alone, does not remove that scope. It does not settle adaptive/history
access, non-copy rules, infinite or continuous state spaces, or approximate recovery under
arbitrary nonuniform full-support priors. Full support alone supplies no prior-uniform approximate
bound. This host record is historical scope provenance here, not an off-main proof used to
reject the bead lead. The stop below follows from the missing physical map independently of it.

## 4. First missing physical ingredient and fixed stop

**First missing ingredient:** a source-level realization of the controlled bead register and its
carrier-to-register write within one stated OI state space and fixed update. It must identify the
degrees of freedom sustaining the trapping potential, the preparer and independent incoming
carrier, and how that carrier changes the register under held controls. Supplying an effective
potential or declaring a prepared bath does not establish that realization.

**The later read has its own missing bridge:** an executing interaction from that native register
through the imaging apparatus into a public output, with detector state, timing, effects on the
stored bit and all outgoing correlations retained. Naming the camera or applying a sign decoder
to a privately known bead coordinate does not supply this interaction. A change of physical rule
would be a proposed extension requiring independent justification, not a result already native to OI.

| Status label | What is supported |
| --- | --- |
| Empirically sourced, external | The single register/read lead of §2, in its laboratory apparatus. |
| Derived, scoped | The landed Theorem N/PAD/NP/AE/SS-2 statements under their respective hypotheses. |
| Assumed if imported | Identifying the external apparatus with native degrees of freedom; its effective preparation and controls as an available OI realization. None is adopted. |
| Unsourced in this screen | The native trap/write map, complete joint starting law/preparer, and native later read/output process. |
| Refuted, limited | Storage certification for `𝔉` by Theorem N, not colloidal memory or OI retention generally. |
| Not established | An admissible native candidate, a second-hold result, non-tautological counted pass or operational reuse. |

Because the first source gate fails, no hold law or retention calculation is performed.
The complete state a later proposal would need is not only the bead: it includes the incoming
carrier, trap field/source, controller and clock, surrounding medium, imaging degrees of freedom,
detector/register and remaining environment, with their joint correlations. A reduced noisy
equation is not that full outgoing state.

Likewise, any later proposal would have to retain incorrect writes, thermal transitions,
unresolved or failed reads and preparation failures as outputs; derive their probabilities rather
than postselect them away; and account for energy, space, time and consumed preparation resources.
Reset, fresh bath or a new blank camera register cannot be inserted for free. These are unfilled
requirements, not a constructed failure kernel or a claim that a complete physical model is impossible.

## 5. Knowledge, timing and compatibility limits

A later camera value cannot count as retained carrier information merely because the decoder
already knows the selected preparation or write-time input. A future proposal must state exactly
what the decoder knew at write and what interaction provides genuinely later evidence.
This packet supplies no decoder and resolves none of the owner's ambiguous D1/D2 or
write-tick-only input cases. The corrected criterion's provisional adoption for old O5 is not
extended to this unit.

There is no conversion from laboratory sampling or residence time to a native hold tick here.
In the old source convention, `T=2` has hold ticks `t₀+1,t₀+2` and window
`t₀+1,t₀+2,t₀+3`; the second hold value alone would not satisfy that whole window.
No such trajectory, error bound or window is asserted for this lead.

Any eventual positive must use a common carrier, fixed update, timing and observer access
compatible with #866 and Claude's Q-A. The read must not expose the hidden parity during reuse
or recombination. Q-A's proposed NNB/R-ONE resources and supplied P1–P3/E-iso/H-PREP are not
physical sources for this lead; its unreviewed conservation/privacy claims are not imported.
Classical retention would establish neither a coherent carrier nor coherence surviving a read.
That separate #1032 obligation remains blocked on its own sources; #1143 keeps the distinguishing
test.

The completed O5 [draft #1177](https://github.com/amaybaum/incompleteness/pull/1177) at
`3ec25f1fbe18e822924f6e834f8fa072a8f4244c` remains historical negative context:
its `N=8`, `A={7,1,2}` geometry lacked physical joint-read sourcing, and its retained laws were
covered by PAD/NP. Its [independent stopped-screen review](https://github.com/amaybaum/incompleteness/pull/1177#issuecomment-6692903227)
is not support for a physical lead here. No replacement geometry or tuned prior revives it.
All old Phase A/frozen records remain unchanged.

**Strongest supported outcome:** one independently motivated external memory/read pair has been
located, but no qualifying native register/write/read pair has been sourced in this bounded
screen. The author recommends non-selection and stopping at §4. Independent review may accept
this only as a source-gap record; it cannot certify physical retention from it. Any continuation
requires the missing physical source and its independent selection review. A decisive scientific
search would require a separately scoped, owner-authorized V3 round and is not executed here.
No simulation, enumeration, implementation, Lean/scientific computational search, new premise
adoption, freeze, special dispatch, merge or manuscript promotion was performed.
