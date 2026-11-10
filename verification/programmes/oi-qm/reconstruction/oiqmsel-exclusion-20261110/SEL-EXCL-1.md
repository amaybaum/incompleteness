# SEL-EXCL-1 — Operational no-signalling and repeated records do not select the quantum Bell bound

**Accountable Issue:** [#1143](https://github.com/amaybaum/incompleteness/issues/1143) (OI-QM-SEL); coordination [#1169](https://github.com/amaybaum/incompleteness/issues/1169).  
**Owner authorization:** [#1143 comment 6769748021](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6769748021).  
**Writer:** ChatGPT, separate from Codex's PREP-MIN and physical-source work.  
**Date:** 2026-11-10.  
**Standing:** **AUTHOR PAPER-ONLY DRAFT — UNREVIEWED.** No independent verdict, kernel proof, numerical/scientific execution, source-qualified apparatus, or integration to main is claimed.

## 0. Research decision, prior evidence, and exact novelty boundary

The selection hypothesis on #1143 asks which *allowances* in a broad space of deterministic substratum realizations and embedded observer interfaces are excluded by OI-native physical/operational consistency. It must preserve real classical measurement contexts while selecting a quantum-capable theory, and it cannot select the quantum outcome tables by definition.

This paper checks a **specific weak selection package** R:

- a finite deterministic **reversible** global microscopic update;
- fixed, partially informed embedded observers with calibrated local access;
- one common hidden-source law independent of freely chosen local setting labels;
- complete accessible outcome/setting/readback/clock/failure histories for the **admitted** local protocol grammar, with no hidden postselection;
- operational no-signalling during isolated-wing use, including finite sequential reuse with fresh hidden source cells and local adaptive controls;
- an actual nontrivial classical-compatible measurement fragment.

**Question:** Does R alone exclude supraquantum Bell behavior? **Author result:** No. A concrete reversible globally coupled model obeys R under its **explicitly restricted access and protocol grammar**, while its CHSH value is 4. Thus R is insufficient to guarantee **quantum soundness** even when it has more operational information than passive records alone.

**What is NOT new:** PR-box correlations, the algebraic CHSH 4, no-signalling of a PR box, reversibility of XOR-controlled maps, and the Bell-local bound are standard. #1169 already records that globally coupled response tables can admit PR-box behavior while screened separated local examples stay at CHSH ≤ 2 (see its “Operational success criterion and current coverage”). The bounded contribution here is the **fully typed finite reversible micro-map, same source for all settings, calibrated record/readback interface, finite repeated-use/local-adaptive no-signalling proof, and exact missing-locality diagnosis** within the #1143 selection question. This is a countercontrol to an *insufficient criterion*, not a new physical discovery or an OI-native impossibility theorem.

**Separate antecedent:** [SEL-ACCESS-1 draft #1224](https://github.com/amaybaum/incompleteness/pull/1224) establishes a conditional menu-restriction limitation: passive-record properties cannot force the existence of unselected executable operations. SEL-EXCL-1 instead checks the **soundness** of a nonpassive, explicitly available finite operation grammar. Its prior accepted paper/reviews are NOT inherited by this draft.

## 1. A single deterministic reversible global update

Use five microscopic bits, with setting registers x,y, a hidden fair source bit r, and initially blank output registers A,B. Define the global step T on the full five-bit state by

\[
T(x,y,r,A,B)=(x,y,r,A\oplus r,\;B\oplus r\oplus(x\land y)).
\]

For every configuration, T squared is the identity: x,y,r are unchanged and each output flips by the same Boolean expression twice. Hence T is a **permutation**, not an ad hoc irreversible stochastic table. The same T is used for all four setting pairs. The only microscopic source is

\[
r\sim\mathrm{Bernoulli}(1/2),\qquad A=B=0,
\]

independent of settings x,y. The random r is epistemic initialization of a deterministic world, not a physical Born rule.

**Declared observer access.** Alice chooses/records x and reads raw calibrated A; Bob chooses/records y and reads raw calibrated B. Both can reread their own unchanged output register and retain their own controller input, outcomes, clock tick and always-success status. Neither has immediate access to the full five-bit world state; r and the distant registers are not among their unilateral reads. The record meanings are fixed across contexts. Each clocked use applies T **once** to a fresh blank output pair. The allowed use/reuse grammar comprises local settings, such uses, nondemolition raw readbacks, storing local records, and finite sequential local adaptive setting choices; it does **not** grant arbitrary reads of r or unrestricted access to T's internal wires.

This interface is **specified, not derived from the native OI/SM dynamics**. The gate is globally coupled: B depends microscopically on x when y=1. It is *not* a native L≥9 ring construction, not a sourced spacelike-local apparatus, and not a physical Bell experiment. The lack of instant complete access satisfies only a weak embeddedness condition, not the full #866 source gate.

Starting from A=B=0, write the accessible output bits a,b. Direct substitution gives

\[
a=r,\qquad b=r\oplus xy,
\]
\[
P(a,b\mid x,y)=\tfrac12\,\mathbf 1[a\oplus b=xy].
\]

These are joint **accessible** tables, not a claim that the microscopic r cannot be recovered after communication. Jointly shared records may reveal more information than either isolated observer can access during a run, consistently with finite momentary incompleteness.

## 2. Exact single-use test: no-signalling, classical fragment, and supraquantum CHSH

For each x,y, r=0 and r=1 have equal weight; therefore each local output marginal is uniform:

\[
P(a=0\mid x,y)=P(b=0\mid x,y)=1/2.
\]

Hence the local output law of Alice is independent of y, and Bob's is independent of x. Settings are selected before the fresh r is used, and the source law is the **same** for every setting. There are no heralds, failures, hidden rejects, or context-dependent normalization changes; the always-success flag is present in every retained use.

With ±1 outcomes \(\alpha=(-1)^a,\ \beta=(-1)^b\), the correlation is

\[
E_{xy}=\mathbb E[\alpha\beta\mid x,y]=(-1)^{xy}.
\]

Thus

\[
S=E_{00}+E_{01}+E_{10}-E_{11}=1+1+1-(-1)=4.
\]

This exceeds the quantum Tsirelson maximum \(2\sqrt2\) for the corresponding bipartite dichotomic Bell scenario. Consequently, no operational soundness principle that accepts the above admitted two-party table can simultaneously identify **every** such table with a standard quantum one.

**Preserved classical observation context.** Restrict to x=0. Then a=b=r for either y: a conventional uniformly shared classical bit with raw nondemolition record rereads, valid probabilities, and consistent retained logs. The point is not that *this entire operational theory* is quantum/classical-compatible (it is not), but that excluding the supraquantum use must not accidentally outlaw this legitimate classical subexperiment.

## 3. Finite reuse and local adaptive settings: complete-history lemma

For any finite m≥1, prepare **one** common source law of fresh independent cells r_1,...,r_m, each fair and independent of all setting controllers' initial information. Give each cell a fresh blank (A_i,B_i), and apply the **same** T to the i-th registers at each clock tick, retaining prior outputs rather than erasing them. Each finite m construction is a specified reversible circuit family; the construction is not asserted to be a physically available fixed SM ring, nor a size-independent apparatus with demonstrated resources.

During isolation, let Alice choose x_i by any local randomized/adaptive policy using **her own** earlier inputs, outputs and private independent randomness. Likewise Bob chooses y_i from his own earlier records and independent private randomness. There is no cross-wing communication while the m uses occur and no access to the current fresh r_i before the corresponding settings are selected. Copying/storing a previous output may be implemented reversibly with fresh blank record cells and retained garbage; erasure and apparatus sourcing are **not** assumed proved.

**Lemma (isolated local-history no-signalling within this declared grammar).** For either wing and any such finite local policy, its joint retained history of settings, raw output bits, rereads, deterministic clocks and success flags is independent in distribution of the **remote** wing's choice of local setting policy (holding the considered wing's own policy and private-source law fixed).

**Proof.** Condition on all prior histories and all settings chosen before use i. The fresh r_i is fair and independent of these variables. Thus \(a_i=r_i\) is fair regardless of y_i; likewise \(b_i=r_i\oplus(x_i y_i)\) is fair regardless of x_i. Each wing's choice of its **next** setting depends only on its own preceding history and its own independent private random seed. Therefore the conditional next-step kernel for that wing's full local record (including its setting and fixed status/clock fields) has no dependence on the remote policy. Induction over i gives the result. Raw nondemolition rereads are deterministic copies of the same wing's stored bits and do not change the inference. QED.

**Scope limits of the lemma.** It does **not** prove independence of the **joint** Alice/Bob history (which carries PR correlations), nor operational no-signalling after explicit message exchange, nor no-signalling against Bob receiving a new physical probe of r, nor against arbitrary controllers or microscopic interventions outside the grammar. It is a finite, locally wired product of non-signalling boxes with fresh hidden cells, not complete closure under every conceivable OI-native procedure. An invalid extrapolation to unrestricted apparatus access would repeat SEL-ACCESS-1's menu mistake.

**Reversibility and records.** For fixed setting registers, the direct product of the T_i maps is reversible and retains hidden r_i and outputs; sequence controllers can be represented by reversible embeddings retaining input and prior-history registers. This is a mathematical finite-circuit availability claim *inside the declared model grammar*, not a sourced physical clock, writable controller or fault-free preparation technology. All admitted uses have explicit success status; no event is silently discarded. A real proposal with nonzero failure possibilities must retain those branches separately.

## 4. The exact locality gap: why the easy exclusion also excludes quantum Bell behavior

The model has operational no-signalling but **not** Bell-local microscopic response factorization. Given the hidden r and setting y=1, Bob's b depends on Alice's x. Operational averaging over the inaccessible fair r hides that dependence from Bob's isolated output distribution. This is **parameter dependence** at the ontic response level, not a physical derivation of allowed remote influence.

If instead one adds the stronger condition that, for a common setting-independent hidden state λ,

\[
P(a,b\mid x,y,\lambda)
=P(a\mid x,\lambda)\,P(b\mid y,\lambda),
\]

then the familiar Bell/CHSH calculation gives \(|S|\le2\). Such a condition excludes the PR construction, **but it also excludes the quantum target** with \(|S|=2\sqrt2\) in the relevant independent-setting bipartite test. That stronger assumption therefore cannot be adopted as the desired OI→QM selector without separately explaining how the quantum Bell target would still arise. This is a **conditional selection trap**, not a theorem that OI must be nonlocal or can realize PR.

There are at least three distinct statements that should never be substituted for one another:

1. No-signalling of measured local outcome laws during isolation (satisfied here).
2. A specific physical locality/finite-speed condition on native microscopic interactions and records (not established here).
3. Bell-local factorization conditional on a setting-independent complete λ (violated here).

A source-qualified OI programme must identify which of these follows from its native embedding/dynamics, which is an independently stated physical input, and what restrictions on non-factorizing yet no-signalling behavior exclude the **supraquantum** class without excluding the quantum one. Simply choosing the Tsirelson bound as an exclusion axiom would be circular.

## 5. Outcome ledger and next sharply testable question

| Proposed selection requirement or target | Status in this paper | What is and is not shown |
| --- | --- | --- |
| Finite reversible deterministic global law | **CONSTRUCTED (model class R)** | T is an involution; not the native SM map |
| Proper local embedded partial access | **CONSTRUCTED BY ASSUMED INTERFACE** | No instantaneous full-state access; interface itself UNSOURCED |
| Same hidden source for all four settings | **CONSTRUCTED** | One fair r independent of x,y, no postselection |
| Complete calibrated records for admitted local grammar | **CONSTRUCTED (bounded)** | Records, clocks, success and rereads retained; not arbitrary physical access |
| Operational no-signalling for finite local adaptive reuse | **AUTHOR HAND PROOF; REVIEW PENDING** | Holds only under fresh-source, isolation, and declared-menu conditions |
| Classical-compatible context | **CONSTRUCTED** | x=0 preserves shared classical-bit measurements |
| Full quantum soundness | **DISPROVED for R**, conditional on accepted algebra | S=4 is outside standard QM; R is insufficient |
| Exclusion of PR by Bell-local factorization | **STANDARD CONDITIONAL LEMMA** | S≤2 also blocks quantum Bell witness |
| OI-native realization of PR or quantum instruments | **NOT SHOWN / UNSOURCED** | #866 physical-source gate NOT PASSED |
| Positive quantum-selection theorem | **OPEN** | No sound-and-complete native selected repertoire derived |

**First useful next question:** Under a *physically sourced* native observer/controller/interaction interface, can one derive from embeddedness and fixed microscopic dynamics a **non-circular, operationally testable exclusion** of globally coupled PR-type uses while leaving a route to quantum Bell correlations and preserving the classical fragment? This must be tested with all accessible local and later shared histories, including clocks, failures, adaptive control and residual apparatus state. If the physical source is absent, the disposition is **UNSOURCED**, not a positive OI selection result.

A follow-up paper question may compare this countercontrol with #868's local CHSH≤2 scope and #1143's prior classical-only C0/C1 controls, using one explicit typed assumption ledger. That comparison is **not authorized scientific execution** and cannot turn the hand counterexample into an OI-native theorem.

## 6. Independent reviewer requests

A different non-author reviewer should check the exact pushed file and commit, without borrowing acceptance from #1224:

1. Recheck T is bijective/involutive on all five bits, and that all settings use one identical map and one setting-independent r law.
2. Independently enumerate the four (x,y) observable joint tables by hand and verify both local marginals, CHSH signs, and the quantum comparator's assumptions.
3. Test whether the local-adaptive/no-signalling induction remains correct when x_i and y_i depend on *their own* past, and identify hidden correlations or clock/failure fields that would break it.
4. Check that the declared protocol grammar does not secretly allow probing r, and label this menu restriction as **assumed** rather than OI-derived; confirm retained local and joint histories are not conflated.
5. Confirm the classical fragment is nontrivial and that record rereads are genuine raw-register readbacks rather than cosmetic output relabels.
6. Separate Bell-local factorization, physical micro-locality, parameter dependence, measured no-signalling and common-source independence; state exactly why the counterexample is **outside a locally sourced spacelike Bell experiment**.
7. Confirm novelty is not overstated against #1169's prior PR-table note, #868 Bell-local scope, and SEL-ACCESS-1. Do not treat review of those prior off-main sources as proof of the new lemma.
8. Apply AGENTS §§A.29/A.42/A.43/A.45 and return ACCEPT / ACCEPT WITH NITS / REVISE with any scoped corrections. Any eventual integration requires separate owner decision and enduring claim support on main.

**Governance:** One new safe research file only; existing #1143 issue and other #1224/#1226 draft heads untouched. No changed physical law of the selected SM ring, source screen, external numerical/Lean/scientific runs, F/E, workflow dispatch, manuscript edit, merge or scientific claim promotion. **Physical-source gate #866 remains NOT PASSED.**


## 7. Same-source reuse stress test: a stronger admissible-menu distinction (author addendum; REVIEW PENDING)

**Status and relation to §§2–3.** This **author-side additional check** leaves the original model R, its fresh-independent-cell protocol grammar, and its conditional counterexample unchanged. It explicitly **enlarges** the protocol grammar to test whether a *single hidden source bit* may be reused over two ticks with Bob retaining calibrated raw records. It must **not** be represented as a counterexample within the original fresh-source grammar or as an OI-native physical operation.

### Exact two-use protocol

Start with the original state \((x,y,r,A,B)\) where \(A=B=0\) and \(r\) is fair independent of all setting choices. At the first use, Bob chooses \(y_1=0\), Alice's \(x_1\) is arbitrary, the same T acts once, and Bob reads and retains
\[
b_1=0\oplus r\oplus(x_1\land 0)=r.
\]
Before the next use, allow the two controllers to change their setting registers while retaining **the same hidden bit r** and the same physical output register B. Bob chooses \(y_2=1\); Alice independently chooses \(x_2\in\{0,1\}\), with the choice made only after the first record (e.g. an external fair private bit). Apply exactly the same T to the **current** microscopic state. Bob's second raw read becomes
\[
b_2=b_1\oplus r\oplus(x_2\land 1)=r\oplus r\oplus x_2=x_2.
\]
Thus for either \(r\), any first setting \(x_1\), and any Bob local first history \(b_1\), 
\[
\Pr(b_2=1\mid y_1=0,y_2=1,b_1,x_2)=x_2.
\]
Bob can infer Alice's second setting exactly from his own second raw register. The full local Bob history is **not independent of Alice's remote second-setting policy**. This is a two-tick **operational signalling witness under the enlarged same-carrier menu**, despite single-use no-signalling in §2. The global gate is microscopically nonlocal already; this is no claim of a realizable faster-than-light physical signal. It identifies the hidden premise supplied by §3's fresh-cell restriction.

**Fresh output registers do not by themselves repair this.** If the second output register is blank but the old r is retained, the first read still gives \(b_1=r\) while the second gives \(b_2'=r\oplus x_2\), so the local record pair reveals \(b_1\oplus b_2'=x_2\). Both cases violate complete-history no-signalling under same-seed reuse.

**Independent freshness repairs this particular witness, conditionally.** Under §3's explicit source assumption \(r_1,r_2\) independent and fair with separate blank outputs, \(b_1=r_1\) and \(b_2'=r_2\oplus x_2\). Then the *joint* local record \((b_1,b_2')\) is independent of \(x_2\) for fixed Bob settings; §3 proves the more general finite local-adaptive version. That conclusion is **mathematical and menu-relative**. It does not physically produce an unbounded stream of independent source bits, nor show reuse/reset resources are negligible or available on a fixed native apparatus.

### Implication and discriminating question

A candidate OI selection principle requiring no-signalling of **all physically admitted multi-tick local histories** would reject *this specific same-seed reused T implementation*, once its setting switches and repeated reads are physically available. Merely requiring single-time marginal no-signalling would miss the leakage. However, **it would not exclude the entire supraquantum PR class**, because a stipulated product supply of fresh hidden bits restores no-signalling for the finite grammar. Consequently:

- Separate **source renewal availability/cost** from initial setting independence and one-shot no-signalling. Do not infer an autonomous renewable source from a mathematical product law.
- Test whether the complete native observer/controller/record grammar actually admits the same-carrier protocol, a fresh-source protocol, both or neither. This is an #866/INT-AVAIL physical-sourcing question, not assumed resolved.
- If future exclusion rules prohibit free unlimited freshness, independently derive the finite-resource or renewal bound. A ban chosen solely to prohibit PR would be circular; even a scarcity bound must be checked against valid quantum-composite use.
- Keep ordinary classical contexts: the first \(y_1=0\) observation is a legitimate shared-bit record, not a behavior that must be excluded just because the broader global model has a supraquantum menu.

**New focused independent review checks:** rederive both two-use identities and the fresh-output/old-seed variant; verify \(x_2\) is an independent remotely chosen setting; distinguish unconditional one-shot marginals from complete-history conditional laws; confirm §3's different grammar and its fresh-\(r_i\) independence; check no OI-native setting writer, clock, reset or source was inferred. This section is **UNREVIEWED** and changes no original reviewed status (the entire SEL-EXCL-1 draft is awaiting its first independent full review).

**No new authority:** This addendum stays within the owner-authorized bounded paper-only selection countercontrol; no numerical/scientific/Lean execution, changed SM rule, physical-source experiment, new premise, F/E, dispatch, manuscript change, merge or main integration. The physical-source gate remains **NOT PASSED**.
