# K1-P1-1: exact enumeration of the P1 stage of K1-RDY-1 (preregistration, draft)

**Status.** Draft control plane of a native V3 round (`AGENTS.md` §A.39), before `F`. WIP / UNVERIFIED. It authorizes
no code drafting, enumeration, run on model states, workflow dispatch, designation of `F` or `E`, or merge. Each of
those needs its own owner authorization (§13). The owner's rulings on the drafting questions OQ-1 to OQ-7 are quoted in
§17; they authorize none of these. Nothing in this file was computed: every number it states is quoted from a proved
result on `main` or from a frozen K1-RDY-1 record, at the locator given.

- **Drafting snapshot** `D` = `8418ec342420e6921808b4b6d9352f4857afd292` (`main`, 2026-11-05T13:35:27Z).
- **Branch** `round/k1-p1-1-20261105`. **Drafting writer** `writer-k1p1-plan`.
- **Round** `K1-P1-1`, non-sealing. **Record directory**
  `verification/programmes/oi-qm/reconstruction/round-k1-p1-1/`. **Receipt path** `verification/receipts/K1-P1-1.json`
  (named here, not created).
- **Planning issue** #1031. Related round: K1-RDY-1 (PR #1126), not modified by this round.

## 0. Authority (§A.42 item 7)

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6658964414 (2026-11-05T13:16:45Z), "Next
round — Option C":

> Authorize **planning and drafting only** for a new, separately reviewed round that permits exact computational
> treatment of P1. It must have a new D, a preregistered enumeration procedure, full countercontrols, independent
> verification and separate F and execution authorizations. Do not modify K1-RDY-1's frozen F or retroactively broaden
> its execution authorization.

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6659415927 (2026-11-05T13:38:21Z), part D:

> Start the already-authorized planning and drafting of the separate P1 exact-computation round, with its own writer
> and non-overlapping files. Specify the enumeration algorithm, completeness checks, independently reproducible
> calculations, countercontrols and safeguards against post-selection. Do not execute it or freeze its control plane
> without separate approval.

The same comment's part A authorizes an independent review of K1-RDY-1's S0/P0 execution, and its part B makes
K1-RDY-1's S12 halt conditional on that review. This round depends on that review (§3).

***

## 1. Question

**What P1 asks.** K1-RDY-1's frozen preregistration (§2 below, file `K`), lines 72–76:

> **P1 — invariance class** (K-4, K-17(a)). `𝓘` = all φ-invariant probability measures on `S`, i.e. the mixtures of the
> uniform measures `u_c` on the cycles `c` of φ, `π_0` included (MR-pre:137–140, invariance leg; Main:56). No member is
> selected or excluded, by NB or otherwise. P2's energy-shell measures (SM:294–296) are members and are not run
> separately. Hypotheses: H-inv[K-17(a)]. Rule part: inputs `φ` only. Image statement: each member's support is
> φ-invariant, so its image at `t_0` is itself.

and its class rule, lines 156–163 (`K` §5.3), with A2 (fields and order of the class token) and A8 (scope of the union
clause):

> Member rows are evaluated for `π_0` and for every cycle-uniform `u_c`, in increasing order of each cycle's
> lexicographically least state, and every member row is reported. Per branch, if any member row is not a positive, the
> class token is the first of VOID[row], Z1-VOID, UNDECIDED(Gk), ABSENT, BLIND attained by a member row, scoped as "not
> every member of `𝓘`". [...]

**K1-P1-Q.** At K1-RDY-1's fixed instance, in each of the branches B-pl, B-eq and B-ct, what does each P1 member row
(`π_0` and every cycle-uniform `u_c`) yield through G1–G7, and what is the P1 class token, under K1-RDY-1's frozen rule,
when the per-member information is established by exact enumeration of the 1024 states?

The round asks nothing beyond K1-RDY-1's P1 stage. It does not evaluate P0 or P3 as stages, issues no P0 or P3 token,
and changes no gate, token, control, hypothesis or decision of K1-RDY-1. K1-RDY-1's frozen `F` and its execution
authorization are not modified.

## 2. The governing rule text, adopted by reference

`K` denotes K1-RDY-1's control plane at its frozen `F` = `d9b3de012e393262adb20f91ad49627bad48de43`, path prefix
`verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/`. The files and clauses this round adopts, pinned:

| File at `F` | Blob | SHA-256 of the blob's bytes |
|---|---|---|
| `preregistration.md` | `c7505385d70343189f561ddf747d41592ae4782a` | `d593e7209968a8d349dfd64899e71db53d7b03efe27493ab6a9dbaa6c2610be9` |
| `amendments/A2-class-token-fields.md` | `303ddd69dac097dd20a32b143b0bb8befaa428e1` | `31f6bc2405a3d40ef0899865c05419be92096f862904d433f74efd3fb17ef415` |
| `amendments/A3-equal-time-independence.md` | `e6a11893129a5424b9c48f349052f029b7019118` | `bac79f7423cda14800fa83fc78830ceeaf29c7da14b32b9b9f2363c37a7c788e` |
| `amendments/A5-lemmas.md` | `92d8fb7b17ba16dd8f3c229b1ff735db783db7fc` | `cc6a2a8377d555d8aab05f00631991e4ddd68b1c36d4ce82afa99957f91d2472` |
| `amendments/A8-class-rule-scope.md` | `93b67ee08087f00ffc8a4c3b99585c86a3bd4199` | `a28408390c08d19357b33ae6352ef73c81438feb6e7b1ad5c3bef152efebc915` |
| `amendments/A9-gate-table-schema.md` | `d3b5e4b243825a97febb501396cfa4edc2f5b88e` | `76fe2170bdd901388e3f23761abbf67bc592a3ae14e4bc85fa9490decfcb8018` |

The first 313 lines of `preregistration.md` at `F` have the SHA-256 recorded there,
`a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`.

**Adopted** ("line N" is line N of `K`'s `preregistration.md`):
- §2 (lines 29–62): the instance, `E`'s rule, `R_E`, the branches and their `W` rules, the overlap rule, sharp and
  weak readiness, `NB`, W-certification, the access labels, the ledger;
- §3's P1 block (lines 72–76), quoted in §1;
- §4 (lines 95–114), with A5 for its support;
- §5.2 (lines 120–154), G1–G7 as applied to P1 member rows, including line 151's clause "For enumerated rows
  (including P1 member rows), "independently" means a second, separately written enumeration that imports nothing from
  the first and matches it row by row";
- §5.3 (lines 156–163) with A2 and A8; §5.4 (lines 165–184), the token map and precedence;
- §6 (lines 196–216), the eleven controls and their pass conditions, as this round's stage S0 (§11.1);
- §7 (lines 218–239), scope limits and non-claims, except the sentence of lines 229–230, "No manuscript, Lean or probe
  change", which is K1-RDY-1's and is replaced here by the governed-path set of §16;
- A3 for the citations of TA (c4); A9's row fields for the row objects of §10.

**Not adopted:** `K`'s §12 governed paths and OD-4 (paper-only execution), A10 (G6 under paper-only execution: this
round enumerates, so line 151's enumeration clause governs G6 directly), A11 (the paper-only checkpoint), A4 (holds and
historical heads; this round has no dependency on those pull requests), A6 and A7 (K1-RDY-1's disclosure and trace),
A1 (attribution; the decisions it quotes are in force through `K`'s text as adopted), and the P0 and P3 row
evaluations of §5.5.

**Precedence.** Where this file and the adopted text differ on a gate, token, control, hypothesis or decision, the
adopted text governs; this file governs procedure only (enumeration, exactness, completeness, independence, outputs,
checkpoints). A difference found at execution is stop condition H7 (§14), never resolved in the execution.

## 3. Dependencies and their status

| Dependency | Where | Status at `D` | Use in this round |
|---|---|---|---|
| `K` (rule text, §2) | K1-RDY-1's `F`, branch `round/k1-rdy-1-20261105`, PR #1126 | frozen; not reachable from `main` | governing rule; start condition SC-2 |
| K1-RDY-1's S0 outcomes (11 pass) and P0 rows (three ABSENT) | `result.md`, `gate-table.json`, `derivations/` at `da1d939e52e71110008cd6534a672897c64c3339` | paper derivations, model-authored; independently reviewed (model-authored): ACCEPT WITH CHANGES, all non-material (PR #1126 comment 6659587647), changes rechecked (comment 6659744122); not on `main` at `D` | agreement controls only (PR-S0, PR-P0); readings RD-1 to RD-3 |
| `LEMMAS.md` (Lemma P1, blindness lemma, L-O) | `verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/`, blob `bef4441cb9ec885879f29689c581c51499a7df4a` at `D` | written proofs, independently reviewed (model-authored) | controls PR-P1c, PR-BLIND |
| `PROOFS.md` (`E`, CYC, IND, EN, CR-1 to CR-6, LEDGER) | `verification/programmes/oi-qm/reconstruction/k1-rdy-pref-proofs-20261105/`, blob `b50e23e47e107934fb5637158cd9148433d62bc9` at `D` | written proofs, independently reviewed (model-authored) | controls PR-E, PR-CYC, PR-IND, PR-EN, PR-CR6, PR-LEDGER |

The reviews of `LEMMAS.md`, `PROOFS.md` and K1-RDY-1's S0/P0 count at the internal-verification level only (owner ruling R5, quoted in
`K`'s A5). No row token of this round rests on them: every row value is computed (§6), and each proved result enters
only as a control whose failure stops the round (§4, §14).

**Readings carried from K1-RDY-1's execution.** K1-RDY-1's `result.md` marks three readings, which its independent
review evaluated (PR #1126 comment 6659587647 §4, with change C2 rechecked in comment 6659744122 §2). The owner accepted
them subject to that review (§17, OQ-3). This round adopts them in the reviewed form:
- **RD-1** (CC-IMP): when G2(a) and G2(b) both flag, the subtype is taken from (a). Grounds (review §4(i)): §5.4
  defines single-subtype row tokens only, A2's subtype set belongs to the class token, and G2 decides (a) first;
- **RD-2:** when G4 issues a token, G5, G6 and G7 are recorded as `not-reached` (`K` line 183, A9);
- **RD-3:** two sets are kept distinct for a row that stops at G4. **(i) The `hypotheses` field** holds the
  declaration's hypotheses (here H-inv[K-17(a)]) and the §2 access labels its token names. It is not `Λ`: `Λ` is
  written only at G5, and no token of such a row carries it. **(ii) The hypotheses `Λ` would contain at G5** are that
  set plus H-law exactly when the row is not W-certified (`K` line 56), plus H-sel exactly when R5 recorded non-empty
  H-sel content. They are not entered in the row; they are fixed by its recorded `w_certified` and H-sel content.
  For a row that reaches G5, the `hypotheses` field is `Λ` (A9).

**Start conditions** (each is checked before `F` is proposed for designation):
- **SC-1.** The independent review of K1-RDY-1's S0/P0 has returned ACCEPT, or ACCEPT WITH CHANGES with every change
  independently rechecked, as recorded by the owner. Satisfied in part: the review returned ACCEPT WITH CHANGES, all
  non-material, with no material defect and no change to frozen rules (PR #1126 comment 6659587647); C1 to C4 were
  rechecked at the exact head of K1-RDY-1's `W` (comment 6659744122); the owner accepted the review (§17, OQ-3).
  Outstanding: the independent exact-head recheck of K1-RDY-1's corrective `W′` (W1 to W3), which the owner's ruling
  of #1031 comment 6660591343, item 2, requires.
- **SC-2.** K1-RDY-1's verified halted landing is on `main`: `d9b3de012e393262adb20f91ad49627bad48de43` and K1-RDY-1's
  record directory are reachable from `main`, with a receipt `Q` on which `tools/v3_verifier.py --verify-round Q`
  prints `VERDICT  HOLDS`, so that the rule this round adopts is on `main` (§A.42 items 2, 3 and 8; §17, OQ-2). Not
  met at this revision.
- **SC-3.** The implementations and `controls.py` exist as reviewed blobs on a pushed staging branch and are frozen by
  an amendment before `F` (§8.4; §17, OQ-1). Code drafting needs its own owner authorization (§13 (a)).
- **SC-4.** The owner has answered the drafting questions of §17. Satisfied (#1031 comment 6660591343).

## 4. Preserved results used as controls (§A.29)

No existing result is reopened. Each result below is computed again from the enumeration and must match; a mismatch is
stop condition H3 (a preserved result fails) or H10 (a K1-RDY-1 outcome differs), never a token.

| Id | Result | Source | Pass condition |
|---|---|---|---|
| PR-E | `E = {x_1, y_1, y_2}`, `W_eq = {x_1, y_1}` | `PROOFS.md` §1 | `E` computed from the dependency rule (§6, R0) and `W_eq` computed from its rule equal these sets |
| PR-CYC | `φ^{10}` is the identity; 156 cycles: the fixed points `0` and `(𝟙, 𝟙)`, the 2-cycle `{(0, 𝟙), (𝟙, 0)}`, 102 cycles of length 5, 51 of length 10 | `PROOFS.md` §2 | the enumerated partition and the second count (§9, CC-CYC2) both give these lengths and these short cycles |
| PR-EN | `ℰ ∘ φ = ℰ`; `{ℰ = 0}`, `{ℰ = 1}` have 512 states each | `PROOFS.md` §5 | `ℰ(φ(s)) = ℰ(s)` at every `s`; shell sizes 512 and 512 |
| PR-IND | `π_0(E_t = 0 \| W_t = w) = q^{−\|E∖W\|}` if `w` is 0 on `W ∩ E`, else 0 (equal time) | A3; `PROOFS.md` §4 | the `π_0` member row's B-eq weak values, and CC-ABS's, equal this formula |
| PR-P1c | the support of every member is φ-invariant | `LEMMAS.md` Lemma P1(c) | `φ(supp m) = supp m` for every member `m` |
| PR-BLIND | an invariant `μ` with `μ(E_{t_0} = 0) = 1` has `NB(μ)` false | `LEMMAS.md` §2 | no B-pl member row is sharp with `NB` true |
| PR-LEDGER | an equal-time sharp row satisfies its G3 bound | `PROOFS.md` §7.3 | no B-pl or B-eq member row reaches VOID[row] |
| PR-CR6 | the member row of `δ_0` is not a positive in B-pl, B-eq or B-ct | `PROOFS.md` §6, CR-6 | the computed `δ_0` rows are not positive, and no branch reaches the union clause |
| PR-S0 | the eleven S0 controls pass | K1-RDY-1 at `da1d939e` (paper; reviewed, §3) | every computed S0 part (§11.1) passes |
| PR-P0 | `π_0`'s G4 outcome is ABSENT in each branch, with weak values B-pl `{"": 1/8}`; B-eq `{00: 1/2, 01: 0, 10: 0, 11: 0}`; B-ct `{00: 1/4, 01: 0, 10: 1/4, 11: 0}`; not W-certified in any branch | K1-RDY-1's `gate-table.json` at `da1d939e` (paper; reviewed, §3) | the `π_0` member rows' `sharp_w`, `weak` and `w_certified` equal these |

PR-P0 compares the `π_0` member row of P1 with K1-RDY-1's P0 rows on G4's measured fields only. The two rows carry
different hypotheses (H-inv[K-17(a)] against H-μ and the finite-`S` posit), so their tokens differ in their fields and
are not compared.

***

## 5. Instance, encoding and member space

- **Instance** (`K` lines 31–35). `(d, N, q, a) = (1, 5, 2, 1)`, `Λ = ℤ/5`, `𝐑 = ℤ/2`, `S = 𝐑^Λ × 𝐑^Λ`,
  `φ(x, y) = (y, Ay − x)`, `(Ay)_i = y_{i−1} + y_{i+1}`, `φ^{−1}(x, y) = (Ax − y, x)`. `Σ = {x_0, y_0}`, `V_t = y_1(t)`,
  `T = 1`. The state at tick `t` is `s(t) = φ^{t − t_0}(s(t_0))`, and a member is the law of `s(t_0)`.
  CC-IMP″ alone uses `(N, q, a) = (6, 2, 1)` (`K` line 212).
- **State encoding.** A state is the string of its cells in A2's order `x_0, …, x_4, y_0, …, y_4`, each `0` or `1`.
  The lexicographic order of these strings with `0 < 1` is A2's member order. A value `w` of a cell set `X` is the
  string of `X`'s cells in the same order (A9); in B-pl, where `W` is trivial, the only value is `""`.
- **Member space.** `M = (π_0, u_{c_1}, u_{c_2}, …)`: `π_0` first, then one member per cycle of `φ`, in increasing order
  of each cycle's least state (`K` line 157; A2). A member is keyed `pi0` or by its cycle's least state (A9).
- **Rows.** One row per (member, branch), branches in the order B-pl, B-eq, B-ct: `3 · (1 + number of cycles)` rows.
- **No symmetry reduction.** Every row is evaluated on the full set of states it concerns; the computation is small, so no
  reduction is used. A reduction may be introduced only by an amendment before `F` that states it, proves that it preserves every field of §10, and adds a
  control comparing reduced and unreduced results.

## 6. The enumeration algorithm

Both implementations (§8) realize this specification; §8.2 fixes where their methods must differ. "Count" means an
exact integer count of states; every probability is a ratio of counts.

```text
STAGE M (members)
M1  S := all 2^(2N) strings over {0,1} of length 2N, in lexicographic order.
    Check: |S| = q^(2N) and the strings are distinct.
M2  For every s in S compute phi(s) and phiinv(s) from the definitions of section 5.
    Check: phiinv(phi(s)) = s and phi(phiinv(s)) = s for every s; {phi(s)} = S.
M3  visited := {}.  For s in S in lexicographic order, if s not in visited:
        c := [s]; t := phi(s)
        while t != s: append t to c; t := phi(t)        (at most |S| steps; else fail)
        add every state of c to visited; record cycle (least state s, length |c|, sorted states of c)
    The first unvisited state in lexicographic order is the least state of its cycle: every smaller state was
    visited, so it lies in another cycle, and cycles are disjoint.
M4  Coverage: every s in S lies in exactly one recorded cycle; the lengths sum to |S|; phi(c) = c for each c.
M5  Output: the member list (pi0, then cycles by least state), each with key, size and sorted states;
    the histogram of cycle lengths.

STAGE R (rows), per branch b in (B-pl, B-eq, B-ct) and per member m in the order of M5
R0  Region and readout (computed once per instance, not per row):
      E := cells outside Sigma with a nonzero coefficient in y_1(t_0 + t), as an F_2-linear form in s(t_0),
           for some 0 <= t <= T                                                     (K lines 36-38)
      W, t_u by the branch rule: B-pl: W empty, t_u = t_0; B-eq: W_eq = V's site set, both slices, t_u = t_0;
           B-ct: W_eq, t_u = t_0 - 1                                                 (K lines 40-47)
      W_{t_u}(s) := restriction of phi^(t_u - t_0)(s) to W;  Z := {s : restriction of s to E is 0}
R1  supp(m) := S for pi0, the cycle's states for u_c; m(s) := 1/|supp(m)| on supp(m).
R2  For every w in F_2^W:  B_w := {s : W_{t_u}(s) = w};  n_w := |supp(m) ∩ B_w|.
      mass(w) := n_w / |supp(m)|.  For n_w > 0:
        weak(w) := |supp(m) ∩ B_w ∩ Z| / n_w ;  ref(w) := |B_w ∩ Z| / |B_w|   (pi_0's value);  q^(-|E|).
      sharp_w := [w : n_w > 0 and weak(w) = 1], in lexicographic order.
R3  NB: for nu := m(. | B_w) (B-pl: nu := m), and each sigma in F_2^Sigma with nu(Sigma_{t_0} = sigma) > 0:
        L_sigma := law under nu, given Sigma_{t_0} = sigma, of (V_{t_0}, V_{t_0+1}) = (y_1(s), y_1(phi(s))),
                   an exact distribution on {00, 01, 10, 11}.
      NB(nu) := exists sigma != sigma' with L_sigma != L_sigma'.
      Computed for every sharp w (G4), and in B-pl also for nu = m as G1's record (K line 123).
      Usefulness (positive rows only): pairs (sigma, sigma') whose L-supports are disjoint; pairs whose laws
      differ and whose supports intersect.
R4  W-certified (per branch, over all of S): for every w, B_w ⊆ Z or B_w ∩ Z = ∅.
R5  G2(b) for the member's support restriction (reading RD-4 for T1; RD-5, RD-6 below):
      Im := supp(m). T2: stated image "itself"; computed image phi(Im); T2 fires iff phi(Im) != Im.
      For each w with n_w > 0:  I_w := {s|E : s in Im ∩ B_w};  J_w := {s|E : s in B_w}.
      H-sel content at w := I_w (sorted E-values) if I_w is a proper subset of J_w; none otherwise.
R6  G3: D(m) = log(|S| / |supp(m)|), recorded as the exact ratio |S|/|supp(m)|.
      B-pl bound (c1): holds iff q^|E| * |supp(m)| <= |S|.
      B-eq bound (c2), per sharp w with mass a/b in lowest terms, k := |E \ W| (overlap cells counted in W):
        holds iff q^(a*k) * |supp(m)|^b <= |S|^b.
      B-ct: no bound; the ledger line names H-ret (K line 62).
R7  G4: no sharp w -> ABSENT[m; b; access].  Else, equal time: a sharp w breaking its bound -> VOID[row].
      Else NB false at every sharp w -> BLIND[m; b; access].  Else G4 passes.
R8  G5: Lambda := {H-inv[K-17(a)]} ∪ access labels (H-cur (declared) for V; H-2s (declared) when W contains
      a previous-slice cell; H-ret in B-ct) ∪ {H-law if not W-certified} ∪ {H-sel if R5 recorded content};
      the row's hypotheses field := Lambda. A row stopped at G4 forms no Lambda; its hypotheses field is as
      RD-3 (i) states.
R9  G6 (rows that pass G5): implementation A's row = implementation B's row, and the adversarial note's token
      equals that row's token (section 8.3); if the note's token differs, UNDECIDED(G6). If A's and B's rows
      differ, no token is issued for the row and the round stops (H1, section 8.3). Without the adversarial
      record the row's G6 and token are "pending".
R10 G7: AVAILABLE[H-sel](Lambda) if H-sel in Lambda, else CONDITIONAL[Lambda]; precedence of K section 5.4.

CLASS (per branch, A2): computed only when the row set is complete (section 9, CT-INC) and no row is pending.
      If some member row is not a positive: the first type in the order VOID[row], Z1-VOID, UNDECIDED(Gk),
      ABSENT, BLIND attained by a member row, with A2's fields.
      If every member row is a positive: emit union_clause_reached = true and no class token (stop condition H3,
      against PR-CR6). The union clause of K lines 159-162 is not implemented.
```

**Gates decided on paper.** G1 (the P1 block is complete and every symbol is mapped in `K` §10), G2(a) on the P1 rule
part and on the member support restriction, and T1, are decided once for the class in the written derivation
`derivations/P1-class-paper.md` (§13, X1), committed before any run on the instance. Both implementations read its three
outcomes from `class-decisions.json` (§10) and apply them to every member row; G1 removes no member (`K` line 124).

**Readings introduced by this round** (accepted by the owner, §17, OQ-3):
- **RD-4.** A member's support restriction is "a cycle of `φ`", whose only input is `φ`. The least state is a report
  key and enters no token (A2), so T1 does not read it as a literal-coordinate input. (Suggested by the feasibility
  review, #1031 comment 6658841280 §1.)
- **RD-5.** "The function of `E_{t_0}`'s cells that `Im ∩ {W_{t_u} = w}` fixes and `{W_{t_u} = w}` does not" (`K` lines
  133–134) is recorded by the set `I_w`. A function of `E`'s cells that is constant on `Im ∩ B_w` but not on `B_w`
  exists exactly when `I_w ⊊ J_w` (take the indicator of `I_w`; conversely, if `I_w = J_w`, a function constant on
  `I_w` is constant on `J_w`), so content is recorded exactly then.
- **RD-6.** The image G2 computes for a member's support restriction is the support at `t_0`, and T2 compares it with
  the stated image "itself" through `φ(supp m) = supp m`.
- **RD-7.** Inequalities between logarithms are decided by the equivalent integer inequalities of R6.

## 7. Exactness

- Arithmetic is on Python `int` and `fractions.Fraction` only. No `float`, no `math.log` or other transcendental
  function, and no numeric library.
- A rational is serialized as `"p/q"` in lowest terms with `q > 0`; zero is `"0/1"` (as in K1-RDY-1's gate table). A
  logarithm is serialized as the exact ratio inside it.
- Before writing, each implementation walks its output and exits with status 3 if any value is a `float`, or any
  rational string fails to parse as `p/q` in lowest terms.

## 8. Two independent implementations

### 8.1 Writers and independence

- **Implementation A**, `verification/lean/k1p1_enum_a.py`, writer `writer-k1p1-impl-a`.
- **Implementation B**, `verification/lean/k1p1_enum_b.py`, writer `writer-k1p1-impl-b`.
- **Controls**, `controls.py` in the record directory, writer `writer-k1p1-ctl`, distinct from both.
- **Adversarial notes** (§8.3), writer `writer-k1p1-adv`. **Executor** `writer-k1p1-exec`, the sole committer to this
  round's branch from `F` on (§13). These five designated sessions are accepted by the owner (§17, OQ-7).
- **Placement** (§17, OQ-6): A and B in `verification/lean/`, as for KT4-PREM-1, each named as an `execution` path in
  the `v3-governed-paths` block at the end of this file; `controls.py` and every output in the record directory.
- Each writer receives this preregistration and the adopted text (§2) only, and no other writer's code until its own
  blob is delivered. The coordinator records each hand-off (what was given, when) and the SHA-256 of each delivered
  file. Each file's header records, as `K`'s A10 does for derivations: its author session; whether its writer had
  access to another implementation; and any shared dependency, "none" where there is none.
- No implementation imports, copies or execs another, or `controls.py`. `controls.py` imports neither implementation:
  it runs each with `python3 -I` as a subprocess and reads its output file.
- Standard library only: `fractions`, `itertools`, `json`, `hashlib`, `sys`, `os`, `subprocess` (`controls.py` only).
  Python 3.11, as in `.github/workflows/verify.yml`.

### 8.2 Method diversity

- **A** represents states as tuples of cells, applies `φ` and `φ^{−1}` from the coordinate formulas, finds `E` by
  propagating symbolic `𝔽_2`-linear forms through `φ`, and walks orbits as in M3.
- **B** represents states as 10-bit integers, builds the 10×10 matrix of `φ` over `𝔽_2` from the definition, applies
  it by matrix-vector products, finds `E` from the rows of the matrix powers `M^t`, and partitions `S` into orbits by its
  own traversal. B also computes the second cycle count of §9 (CC-CYC2) from ranks of `M^k − I`, without enumerating
  states.
- Both compute every field of §10 independently, including tokens and class tokens.

### 8.3 G6 for positive rows

Line 151 of `K` defines independence for enumerated rows as a second, separately written enumeration that imports
nothing from the first and matches it row by row: implementations A and B. The adversarial note of lines 150–151 is
written by `writer-k1p1-adv`, a fourth session, after both outputs exist. It addresses each row that passes G5 by its
key, recomputes G2(b) from the rule part alone, attempts to break the token, and states the token it finds. Its
structured record is `adversarial.json` (§10). A row passes G6 exactly when A's and B's rows are identical and the
note's token equals theirs. If A's and B's rows are identical and the note's token differs, the row ends UNDECIDED(G6).

A disagreement between A and B on any output, a positive row included, is stop condition H1 (§17, OQ-4). H1 is an
integrity stop on this round's procedure. It changes no gate or token of the adopted rule, under which a positive row
whose two enumerations disagree takes the path to UNDECIDED(G6) (`K` line 151). The round issues no token for a
disputed row and no row or class token from outputs that disagree, and halts under `S12` (§14).

### 8.4 When the code is written and frozen

Drafting code is not authorized by this file (§13). Sequence (§17, OQ-1):
1. After the owner approves code drafting, the three writers draft A, B and `controls.py` on a linked staging branch,
   never on this round's branch before `F` (§A.43 item 1).
2. Before `F` the code is reviewed statically, and is run only on the synthetic fixtures of §11.2, which are not the
   K1 dynamics at any instance. No run before `F` touches `φ` or any state of the instance. This applies here the
   owner's ruling for K1-RDY-1 (amaybaum, #1031 comment 6651204512, 2026-11-05T06:15:48Z): "Enumeration before `F`: not
   authorized."
3. An amendment `amendments/A1-frozen-code.md` records each file's blob id and SHA-256, the exact `verify.yml` edit
   (§13), the mutation patches of §11.3, and the synthetic fixtures with their hand-derived answers. `F` freezes them.
4. A defect found after `F` is not repaired in the round: it is stop condition H6, and a successor round corrects it.

***

## 9. Completeness checks

| Id | Check | Method |
|---|---|---|
| CC-COUNT | `\|S\| = q^{2N}` = 1024, states distinct | M1 count against the formula |
| CC-BIJ | `φ` is a bijection with inverse `φ^{−1}` | M2, both composites at every state |
| CC-PART | every state in exactly one cycle; lengths sum to `\|S\|`; each cycle closed under `φ` and a single orbit | M3–M4 |
| CC-CYC2 | second count, by linear algebra: `\|Fix(φ^k)\| = 2^{10 − rank(M^k − I)}` for `k = 1, …, 10`; states of exact period `d` = `Σ_{e \| d} μ(d/e) \|Fix(φ^e)\|`; cycles of length `d` = that number divided by `d`; `M^{10} = I` | B; compared with A's histogram, B's enumerated histogram and PR-CYC |
| CC-ROWS | per branch, the member keys are `pi0` and each least state exactly once, in M5's order; `3 · (1 + number of cycles)` rows in all | `controls.py` |
| CC-MASS | for every row, `Σ_w mass(w) = 1`; for every `ν` of R3, `Σ_σ ν(σ) = 1` and each `L_σ` sums to 1 | both implementations; `controls.py` re-sums |
| CT-INC | the class token is computed only when CC-PART and CC-ROWS hold and no row is pending | both implementations refuse with exit status 2; `controls.py` refuses independently |

The coverage argument: M3 assigns every state to the cycle of the first unvisited state, so each state is assigned
once; CC-PART checks it; R runs over M5's list without filtering, and CC-ROWS checks that each member is evaluated
exactly once per branch.

## 10. Outputs and the replay recipe (§A.42, §A.44)

Files in the record directory, each written by `controls.py run` from the implementations' outputs:

- `members.json`: `{"schema": "k1p1-members", "version": 1, "cell_order": [...], "members": [...], "histogram":
  {...}}`; each member `{"key", "size", "states"}` (`states` omitted for `pi0`).
- `class-decisions.json`: the outcomes of G1, G2(a) and T1 for the class, with the derivation they come from (§6).
- `gate-table.json`: `{"schema": "k1p1-gate-table", "version": 1, "instance", "region": {"E", "W_eq"},
  "completeness": {...}, "controls": [...], "rows": [...], "class_tokens": {...}, "union_clause_reached": {...}}`.
  Each row carries A9's fields (`candidate` = `"P1"`, `member`, `branch`, `gates`, `w_rule`, `w_inputs`, `g2`,
  `sharp_w`, `weak`, `nb`, `w_certified`, `usefulness`, `hypotheses`, `ledger`, `token`) and adds `support_size`,
  `mass` (each positive-mass `w` to its rational), `pi0_ref` (each positive-mass `w` to `π_0`'s value), `d_ratio` and
  `bound_ok`. `class_tokens` uses A2's fields. Each control carries `id`, `gate`, `computed`, `expected`, `outcome`.
- `adversarial.json`: for each row that passes G5, its key and the note's token, written by `writer-k1p1-adv`.
- `derivations/adversarial-<branch>.md` (§17, OQ-5): one file for each branch with a row that passes G5. It opens with
  an index listing, by key in M5's order, every row of that branch that passes G5 (so every positive row), followed by
  one note per indexed row. `controls.py check` requires each index, and `adversarial.json`, to list exactly the rows of that branch that
  pass G5 in `gate-table.json`.

Canonical bytes: UTF-8 JSON with sorted keys, separators `(",", ":")`, `ensure_ascii` false, one trailing LF. Token
strings: the access field lists the labels in the order H-cur (declared), H-2s (declared), H-ret (as K1-RDY-1's P0
tokens do); `Λ` and `hypotheses` are sorted by code point; a row's `hypotheses` field is `Λ` when the row reaches G5 and the set
of RD-3 (i) when it stops at G4. A member is named `π_0` or `u_c[<least state>]` in a token.

**Recipe.** At a commit holding the outputs, `python3 -I controls.py check` (from the record directory) runs A and B,
compares each of their outputs byte for byte with the other's and with the committed file, runs every check of §9 and
§11, and exits 0 exactly when all hold. Its exit status and the committed files are the evidence; printed output is
diagnostic only (§A.44). The workflow job of §13 runs this command; its conclusion is the job's conclusion. Expected
outputs are the committed files; nothing in them depends on time, randomness, environment or iteration order.

## 11. Countercontrols

### 11.1 Known-answer controls at the instance (stage S0 and the preserved results)

S0 runs first. Each computable part of `K`'s eleven controls is computed by both implementations; the parts that are
decisions on the text of a declaration are decided in `derivations/P1-class-paper.md`'s companion
`derivations/S0-paper.md`, committed with it (X1).

| Control | Computed part | Paper part |
|---|---|---|
| CC-ABS | `π_0`, `W = {x_3, y_3}`, equal time: `r(w)` for every `w`; no sharp `w` (ABSENT) | — |
| CC-EXACT | `(1 − ε)μ_Q + επ_0`, `ε = 1/20`, B-pl: not sharp; weak value `153/160` | — |
| CC-SCOPE | `δ_0` in B-pl, B-eq, B-ct: sharp, `NB` false (BLIND) | — |
| CC-LEDGER | `π_0(· \| ℰ = 0)`: shell size, `D`; the asserted B-pl readiness breaks (c1) (VOID[row]) | that the row's readiness is asserted (injected) |
| CC-IMP | `D(μ_Q) = 3 log 2` (support size 128) | G2(a) flags (Z1-VOID[IMPORTED], RD-1) |
| CC-IMP′ | — | both declarations flagged by G2(a) |
| CC-IMP″ | at `N = 6`, `O` fixes `x_2(t_0) = 0` | G2(a) passes; T1 fires; T2 fires (no image stated) |
| CC-PASS | `O₁`'s image equals the stated `{x_1 + y_1 = 0, x_0 + x_2 = 0}` (T2 does not fire); H-sel content in B-pl is `I = {e : e_{x_1} + e_{y_1} = 0}`, none in B-eq | T1 does not fire |
| CC-T2 | the computed image differs from the stated `{x_1 + y_1 = 0}` (T2 fires) | T1 does not fire |
| POS-X | `π_0`, cross time, `W = W_ct`: mass of `w = 0` is `1/64`, sharp, `NB` true, W-certified, G3 does not void; token CONDITIONAL[Λ] with `Λ` as `K` line 215 states | — |
| CC-BLIND | `W_ct ∪ {y_4, x_0}`: mass `1/256`, sharp, `NB` false (BLIND) | — |

POS-X is the positive control (a known positive token), CC-ABS and CC-BLIND the negative ones, CC-EXACT the exactness
control. A computed S0 part that fails gives VOID[stage] under `K`'s §5.4: no row or class token is issued. Because
K1-RDY-1's paper S0 passed, such a failure is also stop condition H10. The preserved-result controls of §4 run after S0
and before any row token is written.

### 11.2 Synthetic fixtures (not the K1 dynamics)

Fixed, with hand-derived answers, in the code-freeze amendment. Proposed:
- **SF-1:** the permutation of `{0, …, 11}` with cycles `(0)(1 2)(3 4 5)(6 7 8 9 10 11)`: cycle lengths 1, 2, 3, 6,
  least elements 0, 1, 3, 6, coverage 12.
- **SF-2:** `𝔽_2` ranks of fixed matrices: the 3×3 identity (rank 3), the zero matrix (rank 0), and
  `[[1,1,0],[0,1,1],[1,0,1]]` (rank 2).
- **SF-3:** a two-cell toy system with a stated `E`, `W`, `Σ` and readout whose sharp `w`, weak values and `NB` are
  derived by hand in the amendment, with one positive and one blind case.

### 11.3 Mutation controls (`controls.py --self-test`)

Each mutation must make the named check fail; a mutation that passes fails the self-test.

| Id | Mutation | Must fail |
|---|---|---|
| MU-1 | delete one member row from one branch | CC-ROWS; CT-INC refuses the class token |
| MU-2 | duplicate one member row | CC-ROWS |
| MU-3 | move one state between two cycles in `members.json` | CC-PART |
| MU-4 | cycle lengths summing to 1023 | CC-PART; CT-INC |
| MU-5 | replace one rational by `"0.5"` | exactness guard (§7) |
| MU-6 | change one `weak` value by `1/1024` | A/B and replay comparison |
| MU-7 | swap two members' order | CC-ROWS |
| MU-8 | remove `y_2` from `E` | PR-E |
| MU-9 | change one token against §5.4's precedence | token recomputation |
| MU-10 | set `union_clause_reached` | H3 flag |
| MU-11 | one adversarial token differing | that row recorded UNDECIDED(G6) |
| MU-12 | one S0 outcome `fail` | VOID[stage]; no row token written |
| MU-13 | one byte of a committed output changed | replay comparison |
| MU-C1 | implementation A with `T = 2` (frozen patch) | PR-E |
| MU-C2 | implementation B with a wrong `φ^{−1}` (frozen patch) | CC-BIJ |
| MU-C3 | implementation A with exact division replaced by floating division (frozen patch) | exactness guard |

The code mutations MU-C1 to MU-C3 are applied by `controls.py` to temporary copies, from patches frozen in the
code-freeze amendment; the implementations carry no test hooks.

## 12. Safeguards against post-selection

1. **Rule before results.** The decision rule (`K` §5.2–§5.4, A2, A8), the member set and order, the row set, the output
   schema, the token strings and every check are fixed at `F`. The code is fixed at `F` by blob (§8.4).
2. **No run on the instance before `F`.** Pre-`F` runs use the synthetic fixtures only; the drafting log (the commits
   `D..F` and the pull request's checkpoint comments) lists every run made.
3. **Members before rows.** Stage M's output is committed and checked (X2) before any row is evaluated (X3).
4. **No stopping rule.** Every member row of every branch is evaluated and reported, whatever earlier rows yield, even
   once a branch's class token is determined. No member is excluded by `NB` or any other outcome (`K` lines 73–74).
5. **One run of record.** The committed outputs are those of the frozen code on the frozen inputs; CI replays them at
   `E`. There is no rerun with changed code, inputs or readings.
6. **All controls reported**, failed ones included.
7. **No reading after outcomes.** A question of interpretation that this file and the adopted text do not settle is stop
   condition H7.
8. **Verdict text generated from data.** `result.md`'s tables of tokens are rendered by `controls.py render` from
   `gate-table.json` and checked byte for byte by `controls.py check`; prose quotes tokens only (`K` line 165).

## 13. Execution procedure (after separate authorizations)

Owner approvals, in order, each separate: (a) code drafting on a staging branch (§8.4); (b) the code-freeze amendment
and any revision of this file before `F`; (c) a `verify.yml` dispatch on the candidate `F`, with the branch held there;
(d) designation of `F`; (e) execution, naming tools (Python 3.11 with `python3 -I`, `git`, the static checks), inputs
(the frozen blobs and `K`), scope (§6 at the fixed instance, `N = 6` for CC-IMP″ only) and writers; (f) a dispatch on
the candidate `E` and its designation; (g) reconciliation, receipt and merge.

Execution commits, each a single-parent child of the previous, starting at `F`:
- **X1** adds A, B (execution paths), `controls.py`, the `verify.yml` edit (one job, "Numerical probes / K1-P1-1 exact
  P1 enumeration", running `python3 -I controls.py check` with Python 3.11, and its entry in the aggregate `probes`
  job's `needs` and result lines), `derivations/P1-class-paper.md`, `derivations/S0-paper.md` and
  `class-decisions.json`. No output file. Checkpoint: each blob equals the frozen one.
- **X2** adds `members.json` and the S0 and completeness parts of `gate-table.json`.
- **X3** adds the rows and provisional class tokens (positive rows `pending`).
- **X4** adds `adversarial.json` and the adversarial notes, when any row passes G5.
- **X5** adds the final `gate-table.json` and `result.md` (execution log quoting authorization (e) with author and
  time, the hand-off records, the rendered token tables, scope and non-claims).

The executor produces X2–X5's outputs by running `controls.py run` locally under authorization (e); the computation is
bounded and deterministic (§A.40), and the CI job at `E` replays it (§10). Candidate `E` is X5 or a later single-parent
commit. Before its designation the independent reviewer checks every
checkpoint of §15 at the exact head.

## 14. Stop conditions and halt

**Stop and return to the owner** (execution stops; only a factual note in `result.md` is committed):
- **H1** A and B disagree on any output, a positive row included: an integrity stop on procedure, not a token (§8.3);
- **H2** a completeness check of §9 fails;
- **H3** a preserved-result control of §4 fails, or a branch reaches the union clause; this is also reported as a
  finding against the cited proof;
- **H4** replay mismatch: CI's regenerated outputs differ from the committed files;
- **H5** the mutation self-test fails;
- **H6** a frozen blob differs from the file run, or a defect is found in the frozen code;
- **H7** a question of interpretation not settled by this file and `K`;
- **H8** a provenance anomaly (§A.26: sweep, then halt);
- **H9** any need for a tool, input, path or computation outside the execution authorization;
- **H10** a computed S0 or PR-P0 outcome differs from K1-RDY-1's reviewed outcome.

**Scientific outcomes** that complete the round: every token of `K` §5.4, including VOID[stage] (subject to H10),
UNDECIDED(Gk), Z1-VOID, ABSENT and BLIND.

**Halt** (architecture `S12`). With execution commits: a withdrawal commit `W`, a single-parent child of the last of
them, restores every `execution` path to its state at `F` (A, B removed; `verify.yml` as at `F`) and carries
`result.md` with the reason and every measured head; no `E` is designated. Without execution commits: a single-parent
child of `F` changing only record paths carries `result.md`. Then reconciliation, a halted receipt built by
`tools/v3_receipt.py`, and `tools/v3_verifier.py --verify-round Q` printing `VERDICT  HOLDS`.

## 15. Invariants and checkpoints (§A.41)

| Invariant | Checkpoint |
|---|---|
| No execution before authorization | `result.md` opens by quoting authorization (e) with author and time; the drafting log lists only reads, static checks and synthetic-fixture runs |
| Rule and code frozen before rows | the reviewer compares the blobs at X1 and at `E` with the code-freeze amendment, and `K`'s files with §2's table |
| Adopted text unchanged | the six SHA-256 values of §2 and the 313-line digest recomputed from `K` |
| Exact arithmetic | §7's guard (exit 3); MU-5, MU-C3 |
| Complete member space | CC-COUNT, CC-BIJ, CC-PART, CC-CYC2; MU-3, MU-4 |
| Every member evaluated once per branch | CC-ROWS; MU-1, MU-2, MU-7 |
| No class token from an incomplete list | CT-INC; MU-1, MU-4 |
| Independent implementations | file headers and hand-off records; the reviewer checks no import or shared code between A, B and `controls.py` |
| Elementwise agreement | `controls.py check` compares A's and B's outputs byte for byte; MU-6 |
| Deterministic replay | the CI job at `E` regenerates every output and compares with the committed bytes; MU-13 |
| Structured verdict | tokens read from `gate-table.json`; the job's conclusion is `controls.py check`'s exit status (§A.44) |
| Controls green before tokens | S0 entries precede rows in `gate-table.json`; MU-12 |
| Preserved results hold | PR-E to PR-P0 in `controls`; MU-8, MU-10 |
| Verdict text from data | `controls.py check` compares `result.md`'s rendered tables with `render`'s output |
| No post-selection | §12 items 1–8, each checked by the reviewer at `E` |
| Governed paths only | `tools/v3_verifier.py` (`S7`) on the round's deltas |
| Scope | an added-lines grep of `result.md` for "no-go", "impossible", "cannot exist", BLIND and ABSENT; each hit scoped as `K` §7 requires |

## 16. Scope and non-claims

- One instance (`K` §7). Tokens are scoped to (member, branch, access, instance). No ABSENT or BLIND token states that a
  ready supply cannot exist. A class token is scoped to `𝓘` at the instance, as "not every member of `𝓘`" where `K`
  says so.
- The P1 class token is not positive at this instance by CR-6 (`K` line 236; A8); the informative content is the member
  rows (`K` line 238).
- A positive member row is at most AVAILABLE[H-sel], with its named hypotheses. It is not physical sourcing of a ready
  state, access, renewal, memory, observer emergence or complete QM. Cross-time positives need retention outside the
  state (H-ret).
- The round's computations are exact finite enumerations, not Lean kernel proofs. Agreement of A and B is independent
  replication, not proof of correctness of either.
- No manuscript or Lean change. The only paths outside the record directory are the two implementations and the
  `verify.yml` job. No correctness band moves. Readiness-dependent work stays as `K` lines 226–229 and A4 leave it.

## 17. Owner rulings on the drafting questions

amaybaum, Claude Code session chat, 2026-11-05, adopted about 14:31Z, recorded in #1031 comment 6660591343
(2026-11-05T14:32:02Z), item 3:

> #1135 P1 computational round — Resolve OQ-1 through OQ-7 as follows. Choose OQ-1's recommended pre-F code freeze,
> allowing synthetic-fixture testing only before F; no K1-instance computation. For OQ-2, require K1-RDY-1's verified
> halted landing on `main` before F. For OQ-3, accept RD-1–RD-7, subject to the accepted review and precise distinction
> between unevaluated hypotheses and hypotheses that would apply at G5. For OQ-4, halt on any A/B disagreement as an
> integrity failure rather than publishing a disputed classification. For OQ-5, use one indexed adversarial file per
> branch covering every positive row. For OQ-6, retain the proposed `verification/lean/` placement and explicit
> execution-path governance. For OQ-7, accept the five designated sessions, with the executor as sole branch
> committer. These decisions do not authorize F designation, code drafting, execution or merge; those remain separate
> gates.

The same comment records how OQ-4 is carried out: "The halt on A/B disagreement is to be stated in #1135's
preregistration as an integrity stop on procedure, not as a change to any gate or token of K1-RDY-1's adopted rule,
whose positive-row path is UNDECIDED(G6)."

| Question | Ruling | Applied at |
|---|---|---|
| OQ-1 code timing | code drafted and frozen by blob before `F`; before `F`, synthetic-fixture runs only and no computation on the K1 instance | §8.4; SC-3; §12 item 2 |
| OQ-2 adopted text | K1-RDY-1's verified halted landing on `main` before `F`; the adopted clauses are not carried verbatim | SC-2; §18 |
| OQ-3 readings | RD-1 to RD-7 accepted, subject to the accepted review, with unevaluated hypotheses kept distinct from those `Λ` would contain at G5 | §3 (RD-1 to RD-3, SC-1); §6 (R8, RD-4 to RD-7); §10 |
| OQ-4 A/B disagreement | any A/B disagreement halts the round as an integrity stop on procedure; no gate or token of the adopted rule changes | §6 R9; §8.3; §14 H1 |
| OQ-5 adversarial notes | one indexed file per branch covering every row that passes G5 | §10 |
| OQ-6 placement | `verification/lean/`, with the implementations governed as `execution` paths | §8.1; `v3-governed-paths` block |
| OQ-7 writers | `writer-k1p1-impl-a`, `writer-k1p1-impl-b`, `writer-k1p1-ctl`, `writer-k1p1-adv`, `writer-k1p1-exec`; the executor is the sole branch committer from `F` on | §8.1 |

## 18. References to content not on `main` (§A.42 item 8)

| Reference | Claim | Class |
|---|---|---|
| K1-RDY-1's `F` `d9b3de01` and its files (§2) | the rule this round adopts | support off `main` at `D`; closed by SC-2 before `F` (§17, OQ-2) |
| K1-RDY-1 at `da1d939e` (`result.md`, `gate-table.json`, `derivations/`) | PR-S0, PR-P0, RD-1 to RD-3 | support off `main` at `D`, reviewed (§3), reaching `main` with K1-RDY-1's halted landing (SC-2); used only as controls and as readings stated in §3 |
| PR #1126 comments 6659587647 and 6659744122 (independent reviews of K1-RDY-1) | SC-1; the reviewed form of RD-1 to RD-3 | provenance: the readings are stated in §3 and accepted by the ruling quoted in §17 |
| #1031 comment 6660591343 | the rulings on OQ-1 to OQ-7 | quoted in §17 with author and time |
| #1031 comments 6658964414 and 6659415927 | this round's authority | quoted in §0 with author and time |
| #1031 comment 6658841280 (feasibility review), 6658598399 (gate-3 plan); PRs #1114, #1126 | the 471-row count and RD-4's suggestion | provenance |
| #1031 comment 6651204512 | no enumeration before `F` (K1-RDY-1), applied here | quoted in §8.4 with author and time |

***

```v3-round
round K1-P1-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-k1-p1-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-k1-p1-1/
record AM verification/receipts/K1-P1-1.json
execution A verification/lean/k1p1_enum_a.py
execution A verification/lean/k1p1_enum_b.py
execution M .github/workflows/verify.yml
```
