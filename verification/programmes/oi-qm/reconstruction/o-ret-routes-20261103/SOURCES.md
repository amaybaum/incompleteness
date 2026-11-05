# Sources for the O-RET route pages (ROUTES.md)

**How these were read.** Repository files were read with `git show ac558b57:<path>` after `git fetch origin main`,
where `origin/main` = `ac558b570d0012a73369ebc1fbc1c09ac523ca94`. Issues and comments were read with `gh api` (REST,
read-only) on 2026-11-03. Each quotation below is verbatim and has been shortened only where `…` appears. Line breaks
inside quotations are collapsed. Issue and comment text is planning provenance (§A.45 rule 1, §A.42 item 2), not
evidence on `main`.

## Authority and question

| Anchor | Verbatim sentence relied on | Used for |
|---|---|---|
| #1032 c.6610742427 (owner decision, 2026-11-03) | "identify the smallest physically justified mechanism producing genuine, carrier-sensitive one-step retention without presupposing the observer or record it is intended to explain. A negative or inconclusive result is acceptable if its scope is precise." | the objective |
| same | "not permitted: computational search, Lean execution, a new physical premise, scientific promotion, merge or publication" | boundaries |
| #1032 body (as read 2026-11-03; `updated_at` 17:20:41Z at that read) | "The second-order rule stores a preceding slice **as state**; that is insufficient to infer an embedded observer's physical ability to *read* it." | framing |
| same, requirement 1 | "An (H\text{-}2s) declaration, identity across time, an observer-chosen decoder or a post hoc moving partition does not count." | route I; OQ-3 |
| same, requirement 2 | "for at least two independently available incoming carrier preparations, some future readable register law differs while the observer's held background and controls are fixed. Reject simple advection/copy or a display of an already computed common record." | NB-1; OQ-1 |
| same, requirement 3 | "Under H-sel the result is conditional. Do not infer a ready state from the record whose production needs one." | route II §3, §6 |
| same, requirement 4 | "distinguish an actual record of an earlier carrier property from the passing field, and specify the time window and budget." | RET-st; window; ledger |
| same, requirement 5 | "do not assume an observer, instrument, noncommutative algebra, Born probabilities or a ready reservoir to generate itself." | circularity checks |
| same, route III | "if it leaves SM's copy-form rule, label it a **new F2 extension** and independently justify it rather than calling it already OI-native." | route III labelling |
| same, countercontrols | "Required: (a) bare previous-slice copy / H-2s; (b) static declarative decoder; (c) conditioned quiet background imported through the prior; (d) moving readout whose schedule is fixed in advance but not physically derived; (e) passive wave/wake with no persistent accessible record; (f) conditioning that makes the carrier indistinguishable" | §5 of each page |
| same, first deliverable | "Obtain independent review of the exact paper before selecting a scientific candidate or fixing a benchmark. A scoped gap is acceptable; neither a broad no-go nor an unconditional physics claim is." | no selection |
| #1032 c.6567189236 (CN control; unreviewed) | "Thus the *readable memory alone* has **zero carrier distinguishability** under this law, despite genuine physical coupling. If instead one stipulates a ready memory \(m=0\), then \(m'=c\) gives a perfect one-bit readable record" | CN; Lemma C |

## Reviewed records in #914

| Anchor | Verbatim sentence relied on | Used for |
|---|---|---|
| #914 c.6563940598 (summary) | "Under a full-support prior, no nontrivial function is exactly recovered from current-slice readouts at two **consecutive** ticks." | P2-G scope |
| same | "These are scoped negatives, not a no-go. Moving or derived partitions remain undecided." | route I scope |
| #914 c.6563955678 (P2-G note) | "**Claim E (exact; one direction, §A.34).** If `supp μ = S`, no nontrivial `f` is exactly recovered at two consecutive ticks `t, t+1` (any `t ∈ ℤ`)." | P2-G |
| same, §2 | "The proof breaks if `V_{t+1}` or `ρ_{t+1}` depends on `R_t` (retention, adaptivity) or on `x_t`: the time-`t+1` readout is then not a function of `y_{t+1}`." | route I §2 |
| same, §2 | "exact recovery at `t, t+1` of `f` non-constant on `supp μ` ⇒ **every** `X_y` is a proper subset of `X`" | route II §2 |
| same, §4 | "If `μ` is uniform, `μ_t` is uniform, and `P(y_t = y, y_{t+1} = z) = \|F(·,y)^{−1}(z)\|/\|S\| = 1/\|Y\|²`. So `R_t ⫫ R_{t+1}`." | A′ |
| #914 c.6563978459 (O-ACC r2), §5 | "For a fixed declared V no such derivation is available in the framework: the readable σ-algebra is always a datum (Sub:44; Lemma 1c). So (b) is forced by the framework's structure, not by a gap in the sources." | route I §5; OQ-3 |
| same, §5 | "**What (a) would need.** Its only reachable form is non-definitional retention into a fixed declared read (control (ii)'s form): a physical sub-process of V that carries u_{t−1}\|_V into content V reads at t." | O-RET's target |
| same, §6.2 | "a step not of copy form. Every rule of SM:106's second-order form is of copy form, so this means leaving the form fixed by SM's form lemma (SM:224): a change of premise." | route III §2 |
| same, §6.2 | "observer-level apparatus (MR★ M.3 (iii))" | route III circularity |
| same, §3 (hand check) | "\| K1 (y, Ay − x), ring \| 4, 2, 256 · 5, 2, 1024 · 3, 4, 4096 \| true \| 0 · 0 · 0 \| 1 · 1 · 2 bits \| 1 · 1 · 2 \|" (columns: copy, I(cur_t ; cur_{t+1}) [H-cur], I(cur_t ; two-slice_{t+1}) [H-2s], H(cur_t)) | "O-ACC hand check: 1 bit" (Lemma S controls) |
| #914 c.6566997020 (disposition) | "**D-07(a): accept the stricter, operational reading.** Native previous-slice access requires a *derived physical readout/retention mechanism*, not simply the appearance of the previous slice in the update rule." | framing |
| same | "**K-5: YES:** Main:62 record-compatible maximal entropy is an H-sel prior selection in this unit, not a dynamical theorem. Ceiling RR-AVAILABLE[H-sel]." | route II §3 |
| same | "**K-8: YES:** H-cur is **declared**, not native, for V and W; H-2s and H-ret remain named conditional hypotheses." | H-cur (declared) |
| same | "**K-17: (a):** all φ-invariant probability measures on finite S, i.e. mixtures of uniform measures on cycles, **including π₀**." | Lemma S scope |
| same | "**K-18: (b):** fix the first instance to (d,N,q,a,V,Σ,T)=(1,5,2,1,site 1 current slice,site 0 both slices,1)." | HC-K instance |
| same | "**K-12: (b):** retain P3 only with the pre-fixed rule W=V's site set (both slices), O=“W's configuration is identical at each tick in [t_u−2,t_u]”, t_u=t_0." | K-12(b) (route II §3) |
| #914 c.6567198108 (PO-1102), row B | "Derive one first tick that carries a distinguishable carrier property into a **physically readable** register without assuming H-2s, H-ret or a private decoder." | the route question |
| same | "A genuine coupled mechanism can give an unreadable record under full counting measure, while conditioning on a ready bit gives an apparent record without sourcing the bit." | route II §4 |
| #914 c.6563412926 (master matrix r2), §1 row 2 | "\| 2 \| O-RET: native retention beyond one tick (ER); its first tick if O-ACC records a convention \| P \| O-ACC or O-RDY \| recurrence, growing V_t, V∩Σ≠∅, H-ret \|" | L-edge; exclusions |
| same, row O-RET | "\| O-RET \| Retention beyond one tick (ER; persistence on W); its first tick if O-ACC records a convention \| OP (P); C1 copy definitional \| #1009 \| O-ACC or O-RDY \| O-P2G, O-C6A \| recurrence, growing V_t, overlap, H-ret \|" | OQ-6 |
| same, §0 codes | "H-μ: exact unconditioned counting (Haar) measure on a declared product partition, finite S — one reading of OI's measure (Main:56 vs :62; MR★:642, :1353)." | H-μ |
| same, row O-RDY | "a record supplying readiness (Z1); selection as derived" | Z1 |
| same, row O-REC | "\| O-REC \| Accessible record in a distinct sub-state (I13: R1, R2, R3, untailored prior) \| OP; MR-1 scoped GAP \| #1023 \| O-RET, O-ACC \|" | O-REC (marker) |
| same, row O-OBS | "\| O-OBS \| Observer emergence: rule-fixed partition, identity, location \| OP; partition stipulated (I6) \|" | O-OBS (routes I, II) |
| same, row O-SET | "\| O-SET \| Setting-dependent interaction (Enc; NC-1) \| OP; DEFINITION-OPEN, Q1/Q7 open \| #1009 \| display: O-RET \|" | O-SET (marker) |

## #1031 (K1-RDY)

| Anchor | Verbatim sentence relied on | Used for |
|---|---|---|
| #1031 c.6567152798 (unreviewed diagnostic) | "So **NB fails for this declared V, Σ, T and event**, even though the event raises the probability of E=0." | countercontrol (f) |
| #1031 c.6567522034 (K1-RDY prereg), §2 | "**Non-blindness** `NB(ν)`. There exist `σ ≠ σ′` with `ν(s_Σ(t_0) = σ), ν(s_Σ(t_0) = σ′) > 0` such that the law under `ν` of `(V_{t_0}, …, V_{t_0+T})` given `s_Σ(t_0) = σ` differs from that given `σ′`" | NB-1 vs path NB (OQ-5) |
| same, §4 | "**Blindness lemma.** Let `μ` be φ-invariant as the joint law of the whole state, `V ∩ Σ = ∅`, `E` given by §2, and `μ(E_{t_0} = 0) = 1`. Then `V_t = 0` μ-a.s. for every `t`, and `NB(μ)` fails." | relation to Lemma S |
| same, §3 (P3) | "`O` conditions on configurations, never on records, and `W`'s persistence is never cited as memory (Z2)." | Z2 |
| same, §2 | "`φ(x, y) = (y, Ay − x)` with `(Ay)_i = y_{i−1} + y_{i+1}`" | HC-K |

## Manuscripts and kernel at `ac558b57`

| Anchor | Verbatim sentence relied on | Used for |
|---|---|---|
| papers/Main.md:44 | "an observer $V \subsetneq S$ — a proper subsystem with finitely many distinguishable internal states, coupled to the complement $H = S \setminus V$ through $\varphi$." | setting |
| Main:50 | "This partition is not a modeling choice but the definition of embedded observation" | fixed region |
| Main:54 | "The product decomposition is idealized; §4.5 addresses approximation quality." | H-product |
| Main:56 (Lemma 3) | "On each accessible orbit the invariant measure is unique (uniform on the cycle); globally, the counting measure is selected among invariant measures as the maximal-entropy one — a selection principle, not uniqueness from invariance alone." | canonical laws are invariant (Lemma S) |
| Main:60 | "It does not preclude structured preparations: a realization in the sense of §3.4 carries its own fixed hidden prior $\mu_H$ as part of the realization datum" | route II §3 |
| Main:62 | "the selection among orbits is fixed by maximal entropy compatible with the observer's records" | route II circularity |
| Main:88 (§1.4 proof) | "By Lemma 2, the partition is fixed." | route I §2 |
| Main:115 (§2.3, theorem) | "Let $\mathcal{C}_V$ and $\mathcal{C}_H$ be finite sets with $|\mathcal{C}_V| \geq 2$, and let $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ be a bijection." | finite-S setting |
| Main:222 | "The transition probabilities $T_{ij}$ are projections of the full phase-space flow onto the configuration sector of $\Gamma_V$, with momenta and hidden-sector degrees of freedom absorbed into the Liouville marginalization." | H-cur analogue |
| Main:604 (§3.4) | "**Theorem (unavoidable hidden predictive memory).**" | memory sits in H, not in a readable register (context) |
| Main:744 (§4.6) | "under (EM) it is derived from the framework's own definitions" | context for Lemma S (related, not derived) |
| papers/SM.md:106 | "The phase-space map F: (x(t−1), x(t)) → (x(t), x(t+1)) has an explicit inverse that uses x(t) to determine which graph to apply." | copy form |
| SM:112 | "This satisfies: constraint (i) with range 1 ($R(i,x)$ depends only on $x_{i+1}$); constraint (ii) exactly ($R(i,x)$ does not depend on $x_i$)" | center-freeness; nonlinear rule |
| SM:112 | "With the visible sector one site's two time slices $(x_0(t-1), x_0(t))$, … it is not a statement about accessible windows." | H-2s declared |
| SM:224 | "a second-order reversible nearest-neighbor rule that is center-free, cubic-isotropic, and linear has the form $x_i(t+1)=\alpha\sum_{j\sim i}x_j(t)-x_i(t-1)$ for one coefficient $\alpha$." | route III leaves this form |
| SM:252 (Lemma 1c(ii)) | "it depends only on the visible $\sigma$-algebra, not on the coordinate split" | observer content depends on the visible σ-algebra (the word "datum" is O-ACC's) |
| SM:296 | "For symmetric $A$ the map $F$ conserves $E(u,v)=u\cdot u+v\cdot v-u\cdot Av$" ; "for local $B$ and $C$ these are sums of local densities." | route I selector |
| SM:811 | "First, the measure feeding the pushforward is taken to be the uniform measure *on the energy shell* of a real-valued conserved energy, not the independent-uniform measure on $(\mathbb{Z}/q\mathbb{Z})^{K \times N}$" | energy-shell candidate (route II §3) |
| papers/Substratum.md:44 | "The partition $V$ defines the observer's *access* — both read and write." | access is the partition |
| Sub:48 | "Visible and hidden lattice degrees of freedom in that sector run the same wave equation; the partition $V$ imposes observer access without changing the local update." | coupling the same under every access declaration |
| papers/GR.md:591 | "Lemma 2's product decomposition $\Gamma = \Gamma_V \times \Gamma_H$ is the kinematic phase space." | H-product |
| verification/lean-mathlib/OIBridge/HiddenMemory.lean:54–55 | "structure Realization (Hist V H : Type*) [Fintype Hist] [Fintype V] [Fintype H] where" / "  step : V × H ≃ V × H" | the split is a datum |
| verification/lean-mathlib/OIBridge/CausalReadback.lean:180 | "  step : V × H ≃ V × H" | the same (RootedRealization) |
| verification/lean-mathlib/OIBridge/IndependenceCensus.lean:97, :100 | "def vis (p : Core) : Bool × Bool := (p.1.1, p.2)" ; "def swapFn : Core → Core := fun p => ((p.1.2, p.1.1), p.2)" | Lemma S control (inert b) |

## External literature (cited from memory, not re-read in this session)

- R. Landauer, "Irreversibility and heat generation in the computing process", IBM J. Res. Dev. 5(3) (1961) 183–191,
  doi:10.1147/rd.53.0183. Background for Lemma C (the cost of erasure), not a source of the inequality.
- C. H. Bennett, "The thermodynamics of computation — a review", Int. J. Theor. Phys. 21(12) (1982) 905–940,
  doi:10.1007/BF02084158. Cited for Lemma C in substance: reversible measurement with a memory in a standard blank state.
- D. H. Wolpert, "Memory systems, computation, and the second law of thermodynamics", Int. J. Theor. Phys. 31(4) (1992)
  743–785, doi:10.1007/BF00670829. Cited for records requiring an initialized memory (the context of Lemmas S and Q).

Bibliographic metadata was checked on Crossref by the independent review; the texts were not read by the author or the
reviewer.

These attributions are to be verified by the reviewer. No claim in ROUTES.md rests on them. Lemmas C, S, Q and L
are proved on the page.

## Context only (not imported)

#866 (P0: physical observable carrier and evolution selection), #1007 (SUBSTATE-1), #1010 (SUBSTATE-2) and #1033 (BSEL-2)
were read for their titles and status only. None of their open results is used.
