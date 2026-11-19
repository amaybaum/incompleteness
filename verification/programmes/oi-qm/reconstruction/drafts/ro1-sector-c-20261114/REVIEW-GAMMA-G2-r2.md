# Focused confirmation of GAMMA-1 unit G2 r2; independent, non-author, paper-only

**Object.** `GAMMA-G2-r2.md`, blob `77e53801909387c71aca01a7601f4ebb6b2068dc`, with
`RESPONSE-GAMMA-G2-r1.md`, retained on PR #1294 at `225d427a` in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`. The copies read are
byte-identical to the retained ones. Cited r2:N. The review being confirmed is `REVIEW-GAMMA-G2-r1.md`
(blob `65fe08c3`), cited RG2-RN.

**Reviewer.** Claude, the author of RG2 and of none of G2. Read-only: no edits, commits or posts; hand
arithmetic only.

**Blob ids checked** with `git hash-object` and `git rev-parse` at `225d427a`: r1 `a14a195c`, r2
`77e53801`, RG2 `65fe08c3`, U2 r4 `1bcb9e17`, G3 r2 `ef416922`. All agree with r2's inputs and with the
response.

**Verdict: ACCEPT WITH CHANGES.** Fourteen of the fifteen changes are applied as required. R13 has one
residual phrase (C1). R2 was applied as RG2 asked, but RG2-R2 was partly wrong: its G_SM clause
contradicts SIG's proved identification, and r2 inherits the error (C2). §6.2 still asserts that the
controls are green, which RG2 should have raised and did not (C3). The R9 candidate miss is correctly
left uncounted, but its scope is stated too broadly and the targets it concerns are not named (C4).
Only labels and scope changed: every proof is as in r1. The three new statements (r2:445–449, :347–352,
:616–618) each come from a required change and were checked by hand. No D-1 verdict is drawn.

***

## 1. The fifteen changes

| RG2 | Applied? | Check |
|---|---|---|
| R1 | yes | [A1] or [A1; Haar, A-inf] appears on §2.1, Proposition G2-4 and its mass, §2.3, §2.5, Theorem G2-5, §3.2, §3.3, §4.1, Theorem G2-6, Proposition G2-7, the §5 instance and §6.4. Proposition G2-3 is untagged, which is correct |
| R2 | yes, but see C2 | r2:149–151 and :173–178 name (P-a), (P-b) and (P-c), the restriction to `μ-G` and κ-ens, and the exclusion of K-4 |
| R3 | yes | r2:434–449. I checked the new `t = 1` A-reg statement. In `u_1(w) = Σ_{j∼w} y_j − x_w`, the variable `y_{w−e_1}` occurs among the screen's rows only in row `w`, with coefficient 1, because its other neighbours lie off the plane `k_1 = h`. So `u_1(D)` is uniform and independent of `(x_D, y_D)` and of the carrier, and the pair's law is the `y_D`-marginal of the prepared law times the uniform law. Correct; "prepared law" should read "the `y_D`-marginal of the prepared law" |
| R4 | yes | Declared class (r2:434–439); "outside `U`" (r2:452–455); §8 column 2 now gives the joint condition. I re-derived r2's A-reg marker example: a marker at `w + e_1` and the variable `y_{w−(t−1)e_1}` are `t` apart along `e_1`, so `U_t(A)` has coefficient 1 between them |
| R5 | yes | r2:551–564, :579–582, G2-F5, §11. MR★:613–615 is quoted correctly. The surjectivity reason for large regions is right |
| R6 | yes | Cross-model label (r2:68–70); §1.2's split; §6.3; the `b(π)` representation paragraph (r2:597–602); `K_P` in every §8 column with the O11 stop |
| R7 | yes | r2:308–311; the §8 a2/a3 row; G2-F3 |
| R8 | yes | r2:682–699. One characterization, merged with G3-F10(b); the three conditions; owner question 1 merged. "Consistent once read as …" is removed |
| R9 | yes, in form; see C4 | r2:223–239, :772–775, §11 |
| R10 | yes | §8 row 1, column 1 |
| R11 | yes | The CC rule is stated (r2:250–253). CC-1 to CC-5 are relabelled. The new controls G2-C11, C13, C14 and C15 are examined in §2 |
| R12 | yes | r2:344–355. The attempt and success events are kept apart, and cells are counted as slice values |
| R13 | yes except one phrase | G2-F1 is ELABORATING, G2-F6 is scoped, and the [instance; [assumed]; per model] labels are carried, with G1-F8 cited. The header (r2:10) still says "fills NC-copy's slot of G1 §7.1" without scope (C1) |
| R14 | yes | r2:728–736 and AW-G2-3 name the construction (one split intensity), not conditional independence given the field |
| R15 | yes | U2 r4 is cited. I re-checked by diff that its counting text is identical to r3's |

**Proofs.** The r1-to-r2 diff was read in full. Lemma G2-1, Theorem G2-2, Propositions G2-3 and G2-4
and Theorems G2-5 and G2-6 keep their proofs verbatim. Proposition G2-7(i) gains only the condition
`d_L + d_R > 0` and the masked-case formula `|d_L − d_R|/(d_L + d_R)`, both from RG2 §3, and both
check. The E-prep masses at r2:347–352 assume an attempt declared independent of `P`, which is stated
there, and they check: `μ(𝔄_a)|B_a|/|S_P|` for the success mass, and the complement for the failed
mass. No other mathematical statement changed.

## 2. The four new controls: a failing case for each, by hand

| Control | Can it fail? | Failing case derived here |
|---|---|---|
| **G2-C11** (r2:661, the dual side of the `K_P = 1` instance) | yes; independent of CC-5's direct expansion, since it uses CALC Theorem 1(d)'s covector recurrence | The same ring and regions at `t = 1`. Proposition 1.4 gives `K_1 = R_{{1,2}}`, so `𝒟_1 = 0`: no annihilating readout exists, and the check returns nothing with the required support. Directly, the non-carrier parts of `u_1(1)` and `u_1(2)` are `y_2 − x_1` and `y_1 − x_2`, which are independent, so `K_P = 0`, as G2-C12 finds. The dual check therefore separates `t = 2` from `t = 1`. Wording: "`K_P` would be 0" should read "`K_P` would not reach 1 through this readout". A readout mixing other coordinates could still couple the two cells partly |
| **G2-C13** (r2:259, shared factor) | only at design level: as stated, the two records are one function (`c mod 2 = 1` iff `c ∈ {1, 3}`), so its outcome cannot vary | A variant on the same factor: herald `c mod 2` and detection `[c ∈ {0, 1}]`, with `c` uniform on `ℤ/4`. `P(both = 1) = P(c = 1) = 1/4 = (1/2)(1/2)`, so the two are independent although they read the same factor. Sharing a factor is necessary for dependence (Lemma G2-1), not sufficient, so the countercontrol's outcome was not forced. It is of G2-C2's kind, a necessity example. Required: replace its "yes" with "a necessity example; the variant `[c ∈ {0, 1}]` gives independence" (C5) |
| **G2-C14** (r2:491, citation of SIG C-5) | yes | I re-derived SIG C-5's table by hand. Path `L` gives `(U_2, a, b)` masses `(0,1,1): 2/8`, `(0,1,0): 1/8`, `(0,0,1): 1/8`, `(1,0,1): 3/8`, `(1,1,0): 1/8`. Path `R` gives `(0,1,1): 2/8`, `(0,1,0): 1/8`, `(0,0,0): 1/8`, `(1,1,1): 2/8`, `(1,0,0): 1/8`, `(1,1,0): 1/8`. They overlap with mass `1/2` in each, equal, so `I = 1/2` bit, as SIG states. Failing case: the same G-ring geometry at `t = 1`, where SIG G-4 (CALC Proposition 1.4 for every rule of form (2.1)) gives complete masking, `I = 0`. That value is all-or-nothing, so the citation there would show no partial masking. Wording: an all-or-nothing value "would make the additive mechanism unnecessary" overstates. It would only fail to show that the mechanism is necessary (C5) |
| **G2-C15** (r2:576, Theorem G2-6 at `t = 2` on a ring) | yes, at design level; within H-K1 only through an expansion error. It reuses G2-C5's expansion, so C5 and C15 are one computation, not two | The same ring with the step `φ(x, y) = (y, aAy − x)` at `a = 2` over `ℤ/4`, outside H-K1's `a = 1`. Then `U_1 = 2·adj`, the coefficient of `x_{−1}` in `u_2(0)` is `−2`, which is not a unit, and `u_2(0) mod 2 = y_0 mod 2`. So the reduction mod 2 of the tick-2 current slice carries the tick-0 current slice at `0`: no erasure. That is the failure the check guards against. Required: note that C5 and C15 share their expansion (C5) |

## 3. R9: the candidate miss and the reported disagreement

**What r2 states** (r2:223–239, :772–775, :845–846). It reports the product law's qualitative
disagreement with the fringe targets. It labels the retained-herald step [A-inf, a reading of
U1:514]. On the other reading, "once C-RET is sourced the a6 product law would be a candidate counted
miss at the scope `(M, κ, μ-G)`". It selects neither reading.

**Is it a miss under SNR-1?** No, only a candidate, and r2 counts nothing. SNR-1 counts only *not
available* as a negative. A counted miss (G1 §6) needs every U1 action of `g_a` *available* with every
input derived, the §7 controls green for that comparison, and disagreement under `κ_cmp`. Here C-RET
is unsourced on K1, the reading of U1:514 is open, and the controls are not yet green against any
target (C3). r2 is right not to count it. Even counted, it would falsify `(M, κ)` at its scope only,
not every observer-level extension (G1 §6).

**Is it stated at its proved scope?** Only partly. What is proved is the product law at `μ-G`, possibly
conditioned on a herald held at `t_c` (Theorem G2-2). Two proved results of the note itself narrow
the candidate, and r2 does not carry them into its scope:
1. **Slice form.** The route needs a heralded carrier preparation. Under A-cur, Theorem G2-6 erases a
   one-tick preparation from every later readable record of a region meeting (NW), so the screen
   cannot depend on the prepared value on either reading. The candidate is therefore A-reg, or A-cur
   for regions outside (NW), where nothing is claimed.
2. **Geometry.** The alternative reading needs the screen to depend on unprepared tick-0 carrier
   content, so `K^D_t ≠ R_D`. Theorem G2-5 excludes that throughout §3.2's declared class. The
   candidate is confined to screens outside that class: surrounded screens, or screens beyond (NW).

Further conditions of the definition: the κ instance (`I^part`, or `I^rdy` with a held screen herald),
κ-ens with H-ens, C-REC and C-RET for the marker as well as the screen, and green controls.
`(M, κ, μ-G)` should be expanded to this list (C4).

**Which experiments and which observable.** a6 is the marker read in the complementary partition,
compared with T-coinc targets (G1 §5.4). The observable is the qualitative "fringes and antifringes"
feature of the `π_C`-sorted pair. On K1 the one-path normalizer lies outside the instance, so only the
first clause is tested (G1 §5.7): the pair ratio `c₁/(c₁ + c₂)` must show fringes. The product law
gives a constant pair ratio, `V_u = 0`, "absent": the opposite classification. The sources (LIT 1.6–1.8):
- **Walborn et al. 2002**, Figs. 4–5 (polarizer at `θ` and `θ + π/2`, 800 s): fringes and antifringes,
  non-delayed, plotted counts with no numbers. This is the cleanest a6 target.
- **Kim et al. 2000**, `R01`, `R02` with a π shift: plotted, no numbers. The idler is detected about
  8 ns after the signal, so this is a6-delayed (G1 §2.3), which also needs the screen record retained
  (C-RET) or the R-seq representation.
- **Ma et al. 2013**, R/L-conditioned counts, `V(ii) = 0.951(18)`: quantitative, but over an
  interferometer phase scan, which on K1 is a family of geometries, not one program (G1 §5.8,
  PROVISIONAL). It is not comparable within one instance without `κ_scale`.

For **a1**, r2's "against fringes present" has no target that `κ` compares in the sources read. The
T-sing sources for X-1 were not read. Schwindt's `V` is background-subtracted, hence inferred. Dürr is
SECONDARY. The a1 item is therefore cross-model and has no comparable target, and r2 should say so
(C4).

**Plainly:** if the screen counts as recording the carrier merely by depending on unprepared tick-0
carrier content, and retention were sourced, K1 under `μ-G` would predict no fringes in the sorted
eraser channels where Walborn and Kim observe fringes and antifringes. That would be a miss once the
controls were green. As things stand it is a candidate, not a counted miss, and it holds only under
A-reg and with a screen surrounded by carrier content.

## 4. D-1

No verdict. r2:13–14 gives none, r2:464–465 is an [A-inf] bearing on (β) only, and r2:796–797 keeps
D-1 undecided. Confirmed.

## 5. Required changes

| # | Lines | Change |
|---|---|---|
| C1 | 10 | Scope "fills NC-copy's slot" as G2-F6 does: the formula and cases (i), (iii), (iv), with (ii) a ring witness |
| C2 | 149–151, 744–748, 844 | **Correction of RG2-R2.** SIG r2's identification check (SIG:78–81, [proved here] there) shows that U1's binary SM ring G_SM is G-ring at `q = 2`. So G_SM meets Theorem G2-2's hypothesis exactly as G-ring does. G-ring's state space is a product over sites and slices, so G1's observers, as sets of sites, are factor sets. Remove "G_SM … is not shown to meet the hypothesis" and the §11 item, and state the identification. Members of the SM:104–106 class beyond SM:112 stay as SIG screens them |
| C3 | 705–707 | "So the two required controls are green … C0 fails, PC-wave passes" needs target data, which G3 has not supplied (G3: Sinha's `δ` not reported). What §6.1–§6.2 show is that the two control images separate: C0's is `−b_j`, and PC-wave's departs from it wherever the cross term is nonzero. Restate it so. RG2 omitted this item |
| C4 | 223–235, 772–775, 845–846 | Expand `(M, κ, μ-G)` into §3's list: A-reg (or A-cur outside (NW)); screens outside §3.2's class; the κ instance; κ-ens with H-ens; C-REC and C-RET for marker and screen; green controls. Name the a6 targets and observable (Walborn Figs. 4–5; Kim `R01`/`R02` as a6-delayed; Ma only through `κ_scale`; first clause only), and state that a1 has no compared target in the sources read |
| C5 | 259, 491, 576, 661 | Wording of the new controls: G2-C13 as a necessity example with the independent variant; G2-C14's "unnecessary" changed to "not shown necessary"; G2-C15 sharing G2-C5's expansion; G2-C11's "`K_P` would be 0" changed to "would not reach 1 through this readout". Optionally, r2:448: "the `y_D`-marginal of the prepared law" |

Nothing here counts under SNR-1. r2 stays unreviewed for SNR-1 purposes until C1–C5 are applied and
confirmed.
