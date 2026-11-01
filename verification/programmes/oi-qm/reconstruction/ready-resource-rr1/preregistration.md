# RR-1 stage 1: ready-resource sourcing (proposed preregistration)

**PROPOSAL ONLY.** Not frozen, not an `F` candidate, not a native V3 control plane. It authorizes no
execution, computation, Lean run, PR commit or premise adoption.
- **Authority to draft:** #914 comment 6556989366, item 2. Any stage here needs separate owner
  authorization after independent review.
- **Review provenance:** reviewed in three rounds (final: accept with changes, C-1–C-8 applied); a reviewer's empty-heredoc `python3 -` call executed no code; the files were seen reflowed after writes (cause not determined; content verified by the drafter).
- **Anchors and grades** are as in the RR-1 assessment (`5914c17c`, `af1e9be2`, `d4a80fc8`,
  `2af1d5d5`). NC1 is an unaccepted draft (REVISE, paused), tagged [draft] wherever cited.

## 1. Question

**RR-Q.** Take the native-Y public-port interface: the rule `U_{t+1}=U_{t−1}⊕h(⊕U_t)`, the 42-bit
packet on B1(q10), P0_NY with the v14 fewest-seed law, and the windows L+1→L+5. For each candidate
ready element E, the stage asks three questions:
1. What is the **irreducible hypothesis list** under which E is ready, occurs, and is accessible?
2. Which items on that list are original-time pins, and which are observer premises?
3. Does E's readiness persist over a stated window?

Conditions of the stage (not further questions):
- **Primary output:** that list for each candidate, from the ordered ablation of G7. The list depends on the preregistered order.
- **Single-use suffices.** A fresh package and renewal are recorded separately.
- **Imprint (Q3) is out of scope.** A positive token establishes no record, apparatus or instrument.
- **Paper-only** (written derivations, source audits on symbolic coordinates). Any step not decidable
  on paper ends in UNRESOLVED(that step).

## 2. Definitions (fixed before any assessment; identical to the assessment's)

- **Reference priors.**
  - **π_0** is the counting measure on two-slice configurations of the declared torus (Main:56).
  - **π_NY** is the P0_NY prior: the pins (25 ready balls, 1479 sources, 17 exceptions, the source-law
    payloads), with independent-uniform values on every unpinned cell (kernel:94–96; NC1:142–146 [draft]).
  - **π_sel** is a named prior-selection class, entered only as hypothesis H-sel with its necessity
    unassessed. Its candidates are MR★:1364–1366 route (i) and Main §4.6 under (EM). Whether it is admitted at all is an owner question.
- **Hypotheses.** *Standing* (never ablated): H-prior-NC, H-torus, H-inventory, H-rule. *Ablatable:* H-sel;
  **H-law** ("the observer's knowledge of the declared preparation law"); H-access (stipulated reads, NC1:150–152 [draft]); pins.
- **Pinned cell:** a cell whose π_NY law is not independent-uniform given the other cells.
- **Ready element E:** a declared site set, a time t_r with use time t_u ≤ t_r, a declared ready set R_E of
  two-slice values, and a stated prior. The ready event is {E_{t_r} ∈ R_E}.
- **E is ready** if, under the stated prior and given W_{t_u}=w, P(ready | w) > π_0(R_E) for some
  positive-mass w. Here π_0(R_E) is the π_0 marginal mass of R_E. The test is on joint laws, never
  marginals (cf. kernel:163–164). A known reference state relative to records counts.
- **(a) occurs:** P(ready) > 0 under the stated prior, at E's own site set and time. Under π_0 every
  finite pattern has positive mass (Main:56), so "occurs naturally" requires H-sel.
- **(b) accessible:** there is a positive-mass W_{t_u}-event on which P(ready | event) = 1 under the
  stated prior, found using no private read, inverse or decoder. This uses H-law.
- **W-certified:** (b) still holds after H-law is ablated. W-certified is exactly the outcome of that ablation step in G7.
  - Ablating H-law means deciding from W alone, by a fixed function f with ready = f(W) almost surely
    under both the stated prior and π_0. Since π_0 has full support, this reduces to f(W) = 1[ready] at
    every configuration. This f-test, not the general G7 removal rule, decides the H-law ablation.
  - When W-certified is no, H-law is in the token.
- **(c) reliably preparable:** a native procedure under declared access yields E with a stated success
  mass, every failure branch retained (MR-pre:162–169, R5). (c) is recorded beside the token.
- **Pullback:** the original-time cells on which the joint law of (E, W_{t_u}) depends, as in
  `CS/native-causal-interface.md:79–89` and `CS/native-apparatus-register.md:58–77`. Each cell is
  classified against the full declared inventory (vread_v15:112–113).
- **Stipulated reads are not sourced record formation.** A read under H-access is a convention, "not an adopted
  access rule" (NC1:150–152 [draft]). It does not meet R3, "executed by a native readout process" (MR-pre:165).

## 3. Decision procedure

**Tokens, stated in advance:** RR-AVAILABLE[irreducible list], RR-NOT-OCCURRING, RR-NOT-READY,
RR-REPRESENTABLE-ONLY, RR-NOT-ACCESSIBLE, UNRESOLVED(Gk), CANDIDATE-VOID and STAGE-VOID.
**RR-DERIVED is not reachable in this stage.** Every path that passes G1–G7 meets one of three cases:
- **A pin stays on the list.** Pins are supplied initial data.
- **Readiness rests on correlation with stipulated reads.** That case gives UNRESOLVED(G8:regress).
- **H-sel stays on the list.** H-sel caps the token at AVAILABLE.

*Reviewer argument (RR-1 round-2 review, R2-3; not a sourced result).* Suppose the pullback of (E, W)
holds no pinned cell. Under π_NY those cells are independent-uniform given the rest (kernel:94–95),
so the joint law of (E, W) equals its law under π_0. Any readiness then comes only from correlation
of E with W, which routes the case to H-access and G8.

**S0 (stage gate, run once first).** POS-1, NEG-1 and CC-2 (§4). Any control that fails or cannot be
decided on paper gives **STAGE-VOID**, and no candidate token is issued.

**Per-candidate gates.** Each gate has three outcomes: *pass* (go to the next gate), *fail* (the token
named), and *undecided on paper* (UNRESOLVED(Gk)). Every path issues exactly one token.

| Gate | Pass condition | Fail token |
|---|---|---|
| G1 completeness | Site set, t_r, t_u, R_E, stated prior, π_0(R_E) and the inventory-classified pullback are all written | CANDIDATE-VOID if not written; UNRESOLVED(G1) if not writable from sources without computation |
| G2 (a) | P(ready) > 0 under the stated prior | RR-NOT-OCCURRING |
| G3 background | E is ready (§2) | RR-NOT-READY |
| G4 private means | No private read, inverse, decoder, late write, reset or supplied actuator is used | RR-REPRESENTABLE-ONLY |
| G5 (b) | (b) holds. *Fires* when every positive-mass W_{t_u}-event has P(ready \| event) < 1, so the observer, even under H-law, is never certain of readiness | RR-NOT-ACCESSIBLE |
| G6 entropy (CC-4) | Lower local entropy than E's source cells is accounted for, with the joint law kept (MR-pre:184–187), or no reduction is claimed | CANDIDATE-VOID |
| G7 ablation (CC-1) | The irreducible list Λ and the W-certified flag are computed. *No token is issued.* | — |
| G8 regress (CC-5) | Fails when H-access ∈ Λ and Λ contains no pin and no H-sel, so readiness exists only through stipulated reads | UNRESOLVED(G8:regress) |
| G9 skepticism (CC-7, §A.31) | Runs in full (a second, independent written pullback and an adversarial note must agree) when Λ contains no pin, when W-certified = yes, or when H-access was ablated and readiness survived; otherwise passes | UNRESOLVED(G9) |
| G10 issue | Reached only after G1–G9 pass | RR-AVAILABLE[Λ] |

**G7 procedure (fixed order).** Λ starts as the ablatable hypotheses the assessment uses plus the pins meeting
the pullback. Ablate sequentially: (1) H-sel, replaced by π_NY; (2) H-law, decided by the §2 f-test; (3) H-access,
removing every stipulated read from W; (4) pins, one inventory item at a time (ready ball, compiled source,
named exception, source-law payload) in source-table order, each given π_0 on its cells. With earlier removals
kept, every h other than H-law stays removed iff G2–G5 still pass and P(ready) is unchanged; otherwise it is restored. An ablation not
decidable on paper gives UNRESOLVED(G7:h). Λ is *irreducible* for this order and may differ under another.

**Recorded beside the token, never changing it:** (c), W-certified, the persistence window, consumption, next-trial (i) as
FRESH-PACKAGE yes/no/unresolved, and renewal (ii) as RENEWABLE / SINGLE-USE / RENEWAL-UNRESOLVED.

## 4. Controls

| Id | Scope, position | Fixture | Fails when (→ STAGE-VOID) |
|---|---|---|---|
| POS-1 | Stage, S0 | The current q10 ready ball at t_r = t_u = 0, with R_E = its pinned values (`CS/native-causal-interface.md:24–25`) | The token is not RR-AVAILABLE with Λ ⊇ {H-law, the q10-ball pin}, or W-certified is not no |
| NEG-1 | Stage, S0 | The single bank cell f_5(L+4) = port5 + (L+4)·e_y (kernel:77–78; direction e_y from history_v9:58), with t_r = t_u = 0 and R_E = {000} | The token is not RR-NOT-READY at G3 |
| CC-2 relabeling/representation | Stage, S0 | A bijective relabeling of a uniform cell with R_E relabeled; a private-inverse coordinate (chi_H, NC1:57–59 [draft]) | Not rejected at G3 (relabeling) or at G4 (private inverse) |

The per-candidate controls CC-1, CC-4, CC-5 and CC-7 are gates G7, G6, G8 and G9, with the tokens given there.

## 5. Scope limits
Only the native-Y interface above; Native A (v11/v12) is kept separate (`CS/native-actuation-boundary.md:53–58`);
K1 transport, lane C links and per-law realizations (Main:566, 582) are out of scope. No premise, prior, access
rule, pin or source is adopted; H-sel and H-law are named hypotheses only. No imprint, record, setting,
contextuality, instrument or thermodynamic-cost claim (MR-pre:184–185). A failure refutes only its candidate;
no token states that a ready supply cannot exist (MR★:1504).

## 6. Results preserved (used as controls; none reopened)
MR-1's scoped GAP and C-3/C-14 (MR★:1342–1372, 1491–1504); Lemma R and entropy invariance (MR-pre:177–187);
kernel `923be23b`; passive selectors `53bf7ac8`, `c981a006`; LA-EQUAL/EMPTY `8af2d904`; register obstruction
(apparatus-register, `d4a80fc8`); port-5 masking (cone-reduction:51); #912:57–69; Main:56, 60; PC-1's scoped
negative (25 rules, G★ item 3, "not a universal no-go", #914 c. 6548543096). NC-1 is used only as definitions and hypotheses.

## 7. Invariant → checkpoint table (§A.41)

| Invariant | Checkpoint |
|---|---|
| No computation run | The command log lists only read commands; the reviewer checks it |
| Rule fixed before assessment | §2–§4 are frozen before any candidate row is written. **The freeze itself needs its own owner authorization (no commit is authorized here).** Method: record the git blob id of the frozen file, and have the reviewer compare it with the file used |
| Every path ends in one token | The reviewer traces S0 and G1–G10 for each candidate, and checks that each row shows the deciding gate |
| Stop at UNRESOLVED when not decidable on paper | Every UNRESOLVED names its gate; no row cites a computed value absent from a source |
| Joint law, never marginal | G3 and G6 rows state the joint conditional law in writing; a marginal-only row is rejected |
| H-law carried when W-certified is no | The reviewer checks that each such token lists H-law |
| Q3 kept out of the verdict | A grep for "record" or "imprint" restricted to the token column |
| Every token anchored | Each row cites file:line at an exact SHA; the reviewer samples ≥ 20 |
| Occurs / accessible / preparable kept separate | Columns (a), (b) with W-certified, and (c) filled for every E |
| Single-use not penalized | Next-trial columns are separate; no token cites them |
| S0 green before tokens | The S0 rows appear first, with outcomes |
| Native A kept separate | No P0_NY row cites a Native A anchor (native_v11, native_x_v12, INTERFACE-CONTRACT:44–54); reviewer grep |
| Preserved results not reopened | Every §6 item is cited only as stated; no row restates one with a different scope |
| NC-1 only as definition or hypothesis | Each NC1 citation carries [draft] and sits in a definition or hypothesis cell |
| No no-go; no premise adopted | An added-lines grep for "no-go", "impossible", "cannot exist" and "adopt"; each hit is scoped or removed |
