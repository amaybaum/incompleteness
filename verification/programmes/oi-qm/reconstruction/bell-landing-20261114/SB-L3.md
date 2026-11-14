# SB L3: a shared factor that no setting writes is a common cause (narrow extract)

This record carries one lemma of SUBSTATE-BRIDGE-1 unit 1 r2, L3 (its §3.2), as a narrow extract:
the five source lines S:167–171, quoted verbatim in §1, and nothing else from that file. Every line
outside the fenced quotation in §1 is an addition made for this extract, is not text of the source,
and is labelled **[+n]** with its attribution.

## 0. Pin block [+0]

*Addition [+0], by the extract's writer, from `STATUS-SB-L3.md` (Bell landing plan, `3859c3ef`).*

- **Source file.**
  `verification/programmes/oi-qm/reconstruction/drafts/substate-bridge-1-20261111/SUBSTATE-BRIDGE-UNIT1.md`
  at `86a413c88cd14d344aa41b6f47885aeb24da6910` (branch `research/substate-bridge-1-20261111`,
  PR #1232, r2; parent `b94b283a`, r1; base `cac5d264`), blob `9ff0f0774e403ed782354c0b10986a0fe5dc5ed8`,
  SHA-256 `662b9cbaab4237a357174b675c7ee7734c4d4512ef68d530555111230bde48fd`, 356 lines. "S:n" is
  line n of that file.
- **Extract.** S:167–171 (§3.2, L3): 5 lines, 1,364 bytes including the final newline, SHA-256
  `f1450a7a07f3efdbdbc391d4e1c697dd2a046c08ec10a1b0555dd359c8efcb87`. Recipe: `git show
  86a413c88cd14d344aa41b6f47885aeb24da6910:<source file> | sed -n 167,171p`; the lines between the
  fence markers in §1 equal that output byte for byte.
- **Bell-scope.** "BS:n" is line n of
  `verification/programmes/oi-qm/reconstruction/drafts/bell-scope-868-20261111/BELL-SCOPE-UNIT1.md`
  at `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918` (PR #1231, r2), blob
  `5814e479b16929fe8ab045a3f3b8fc4987704633`, which lands in the same package.
- **Main.** "Main:n" is line n of `papers/Main.md`; at the source's pin and base it is read at
  `86a413c8`/`cac5d264`, and the extract re-pins it to `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`
  ([+1]).
- **Owner decision.** #868 comment 6874036684 (`amaybaum`, 2026-11-14), route item OQ-3: "SB L3 is
  carried as a narrow extract. The N′ composition is marked as an addition." The package that
  carries it is option (1) of #868 comment 6873193841: "one combined Bell package: BS Theorem N and
  N′ (#1231), SB L3 (#1232) and the ladder r3 (#1273)".
- **Narrow extract.** No other line of SUBSTATE-BRIDGE-1 is carried: not its L1, L2, L4, routes
  A/B/C, N1–N4, §6 or probe files. The quoted lines keep the source's references; §3 resolves each.

## 1. Quotation: S:167–171, verbatim

~~~~text
### 3.2 L3: a shared factor is harmless unless a setting writes it [A; X S5]

Main's `G_φ` is "symmetrized for the spatial graph" (Main:364), and Bell-scope's (Sep) uses that symmetrized distance. The induction in the cone lemma is directed: output `i` depends on the inputs that have an edge *into* `i`. Let `M` be a hidden factor read by both wings (edges `M → R_A`, `M → R_B`). If there is no directed path from `G_B` to `R_A^t` of length at most `t − t_s`, then step 1 of Theorem N goes through with directed distance, `M`'s content at `t_s` is part of Ω, and the conclusion is unchanged: `M` is a common cause. S5 checks 300 random response tables with a shared mode and correlated priors: `|CHSH| ≤ 2` in each.

Two consequences. (i) A shared, static or autonomously evolving substate — B1's static bit, a conveyor of fresh digits delivered to both wings — cannot produce a Bell violation, however deep. (ii) Bell-scope's statement that a wing–mode–wing path "breaks (Sep) at graph distance ≤ 2" is correct for (Sep) as written, but parameter independence fails only if the path is directed generator → mode → record. (Sep) is sufficient, not sharp; this is a remark for that draft's review, not a correction made here. The independent re-review of Bell-scope r2 records the same point as a nonblocking note (review 5857981727, §6).
~~~~

## 2. Additions

### [+1] Re-pin of Main:364 to Main:362

*Addition, by the extract's writer; source drift measured in `STATUS-SB-L3.md` ("Source drift").*

S:169 cites Main:364 for the definition of `G_φ`. At `c3b5f37a` (`main`) the same sentence is
Main:362: "define the coupling graph $G_\varphi$ by one-step dependency: $i\sim j$ whenever the $i$th
output component of $\varphi$ depends on the $j$th input component for some state (symmetrized for
the spatial graph)", followed by the cone lemma, "Then, by induction, $(\varphi^k(s))_i$ depends
only on initial components in the graph ball $B_{G_\varphi}(i,k)$." The five sentences of the
paragraph at Main:364 (`86a413c8`) recur unchanged at Main:362 (`c3b5f37a`). Main:362 also defines
`G_φ^K` and states the linear-update clause; L3 uses neither. The quotation is not edited: "Main:364"
in S:169 reads as Main:362 on `main`.

### [+2] Hypotheses

*Addition, by the extract's writer; from BS §3.1–3.2 (BS:139–196) and `STATUS-SB-L3.md`
("Hypotheses").*

- Every hypothesis of Bell-scope Theorem N (BS:159–178): (D), (F), (Gen), (Rec), (GI), every-run
  outputs with a fixed local failure rule, a finite jointly admissible menu, no postselection and
  (MI) for Ω; or of Theorem N′ (BS:185–191) with (MI\*) for λ\* = (Ω, ρ_A, ρ_B) in place of (GI) and
  (MI). In either case (Sep) (BS:150) is read with the directed distance: for every
  `t ∈ [t_s, T_A]`, no directed `G_φ` path of length at most `t − t_s` runs from `G_B` into `R_A^t`,
  and symmetrically for B.
- The directed reading of Main's cone lemma: `(φ^k(s))_i` depends only on components with a
  directed path into `i` of length at most `k`. Main:362 states the lemma for the symmetrized graph;
  the directed form follows by the same induction and is part of L3's argument (tag [A]).
- The shared factor `M`'s content at `t_s` lies outside the generator regions, so it is part of
  `W = V ∖ (G_A ∪ G_B)` and of Ω = `x_{t_s}|_W` (BS:144–145), and (MI) or (MI\*) applies to it.

(D) and (F) are posits of the framework; (Gen), (Rec), (Sep), (GI) and the failure rule (BS's
⊥-rule) are properties of a protocol (BS:156–157); (MI) is posited (BS:153), and (MI\*) is a posited
hypothesis of Theorem N′ (BS:99, :187).

### [+3] Composition with Theorem N′

*Addition, by the extract's writer, as specified by the Bell landing plan (`LANDING-PLAN.md` §2.5,
`3859c3ef`); its source is BS:190–191 at `e1534b08`. Not in SUBSTATE-BRIDGE-1.*

The quotation names Theorem N only. Two cited statements compose to cover Theorem N′:

1. S:169: under the directed no-path condition, "step 1 of Theorem N goes through with directed
   distance".
2. BS:190–191, the proof of Theorem N′: "Step 1 does not use (GI) and gives `h_A` as a function of
   `(x_{t_s}|_W, x_{t_s}|_{G_A}) = (Ω, ρ_A, a)`, which is a function of `(λ*, a)`; symmetrically for
   B. Steps 3–4 apply with λ* in place of Ω. ∎"

Theorem N′'s proof consists of step 1 and steps 3–4, so with step 1 read as in statement 1 the
conclusion of Theorem N′ holds under (D), (F), (Gen), (Rec), directed (Sep) and (MI\*): `M`'s content
at `t_s` is part of Ω, hence of λ\*, and `M` is a common cause. This is the composition of the two
statements and adds no step to either.

### [+4] Finite depth

*Addition, by the extract's writer; from review r1 of the landing plan, finding S8
(`REVIEW-BELL-PLAN-r1.md`), as adopted in `STATUS-SB-L3.md`.*

Consequence (i) of S:171 ("however deep") holds under the hypotheses of [+2]: with (MI) for Ω (or
(MI\*)) and directed (Sep), a shared static or autonomously evolving substate of any finite depth
cannot by itself produce a Bell violation. L3 inherits (F), finite `V` and finite `S_i`. An infinite
tower needs SB L2 (S:153, Bell ceiling for a measurable hidden carrier), which this extract does not
carry; that is gap D3 of #1274 (`intervene-substate-results-20261113/DEPENDENCIES.md`:24 at
`fef94857`), open under #1169. Parameter independence fails only through a directed path
generator → factor → record, requirement N2 of route A, which #1274 carries conditional on L3
(`NEW-RESULTS.md`:507 at `fef94857`).

### [+5] Measurement independence kept

*Addition, by the extract's writer; from `STATUS-SB-L3.md` ("Hypotheses", "Limitations") and review
5858000929 ("The classical common-cause observation is also correct under MI").*

L3 and [+3] assume (MI) for Ω or (MI\*) for λ\*. A law in which the settings depend on Ω or λ\* is
outside their hypotheses, and nothing here is stated for it. L3 also says nothing about a factor
that a setting writes (route A with N2), about routes B and C, or about the window in which (Sep)
fails.

### [+6] B1 through its finite factor

*Addition, by the extract's writer; wording from confirmation r2 of the landing plan, finding C3
(`CONFIRM-BELL-PLAN-r2.md`).*

"B1's static bit" (S:171) is Model B1 of the recursive-substates record,
`verification/programmes/substratum/recursive-substates/README.md`:23 on `main`. B1 reads and writes
only `b_0` and `b_m` for one fixed finite `m` (README.md:23); the remainder of its sequence is fixed
and unread, so the finite-depth consequence applies to B1 through that finite factor.

### [+7] The check S5

*Addition, by the extract's writer; from review r1 of the landing plan, finding S7, and
`STATUS-SB-L3.md` ("Limitations").*

The tag "[X S5]" (S:167) and the sentence "S5 checks 300 random response tables …" (S:169) refer to
`probes/generic_substate_checks.py`:241–259 at `86a413c8`, which this extract does not carry. S5
draws response tables `h_A(m, l_A, a)`, `h_B(m, l_B, b)` that already factorize through the shared
mode, with setting-independent weights; it checks the CHSH bound for local models, cannot fail, and
does not exercise the directed-cone step that is L3's content. It is provenance, not support.

### [+8] Support layer

*Addition, by the extract's writer; from `STATUS-SB-L3.md` ("What the record supports").*

L3 is a paper argument [A] on Main's cone lemma (Main:362, paper proof on `main`) and on Bell-scope
Theorem N, itself a paper argument on that lemma (BS:159–178). [+3] is a paper composition on
S:169 and BS:190–191. No kernel statement, exact computation or exhaustive check supports the
directed-cone step. L3 is one paragraph; the directed induction is stated, not written out.

## 3. Reference resolution

*Addition, by the extract's writer. Classes, as in `STATUS-SB-L3.md` and `LANDING-PLAN.md` §6.3: **support
on `main`**; **in the package** (support on `main` once the Bell package lands, in the same merge);
**provenance** (the extract's claims do not rest on the referenced content).*

| Reference in S:167–171 | Resolves to | Class |
|---|---|---|
| "Main's `G_φ` is 'symmetrized for the spatial graph' (Main:364)" (S:169) | `papers/Main.md`:362 at `c3b5f37a` ([+1]) | support on `main` |
| "the cone lemma" (S:169) | Main:362, "Then, by induction, …"; its directed reading is L3's argument ([+2]) | support on `main` (symmetrized form); directed reading [A] in this record |
| "Bell-scope's (Sep)" (S:169) | BS:150 at `e1534b08` | in the package |
| "step 1 of Theorem N" (S:169) | BS:168–170 (Theorem N, BS:159–178) | in the package |
| "Ω" (S:169) | BS:144–145, `Ω = x_{t_s}\|_W` | in the package |
| "[X S5]" (S:167); "S5 checks 300 random response tables …" (S:169) | `probes/generic_substate_checks.py`:241–259 at `86a413c8` ([+7]) | provenance; not carried |
| "B1's static bit" (S:171) | Model B1, `verification/programmes/substratum/recursive-substates/README.md`:23 ([+6]) | support on `main` |
| "Bell-scope's statement that a wing–mode–wing path 'breaks (Sep) at graph distance ≤ 2'" (S:171) | BS:247–249 | in the package |
| "review 5857981727" (S:171) | ChatGPT re-review of Bell-scope r2 at `e1534b08` | provenance (review) |
| "§6" (S:171) | SUBSTATE-BRIDGE-1 §6, its off-`main` reference table (S:313–331), which lists that review | provenance; not carried |

References in the additions: BS:185–191 (Theorem N′) is in the package; `NEW-RESULTS.md`:507 and
`DEPENDENCIES.md`:24 at `fef94857` (#1274) are support on `main` once #1274 lands ahead of the
package, and provenance until then; S:153 (SB L2) is provenance and is not carried; reviews 5858000929
and 5857981727, `REVIEW-BELL-PLAN-r1.md`, `CONFIRM-BELL-PLAN-r2.md`, `STATUS-SB-L3.md` and
`LANDING-PLAN.md` are provenance; #868 comments 6874036684 and 6873193841 are governance provenance.

## 4. Status

*Addition, by the extract's writer.*

**Status:** partially verified (model-reviewed, not independently verified); conditional on the
hypotheses of [+2]; accountable Issue #1169. The composition [+3] has had no review yet; it is
reviewed with this record. Not adopted; no manuscript claim is affected.
