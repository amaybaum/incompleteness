# PE-02 plan: changes from revision 1 to revision 2

**Status: WIP / UNREVIEWED; planning only; no execution authorized.**

- **From:** revision 1, `902c4c0d`.
- **Review:** `review/REVIEW.md`, committed at `2bb45e0b`: ACCEPT WITH CHANGES, R1–R15.
- **To:** revision 2, uncommitted, drafted on `2bb45e0b`.
- **Instruction:** apply R1–R5, R7–R15, R6's reporting change and the UX specification. R6's choices and O1–O10 are
  left as marked owner placeholders carrying the review's recommendation, and the stage name stays "PE-02" with a
  placeholder note.

Section references are to revision 2's `PLAN.md` unless marked NOTES.

| Item | Review's requirement | Edit in revision 2 |
|---|---|---|
| R1 | `G_weak_mut`: advantage 0 only for 1 ≤ K ≤ 13; K = 0 has 1/2 | §1.3: the countercontrol is stated for $1 \le K \le n$, with K = 0 excluded and why. §5 control 3: "every $1 \le K \le 13$", and no window with $K \le 16$. Parameters: `PL_mut_K_range` [1, 13]. §4.2: K′ = 0 is a zero only where $x_0$ is uniform, which fails on the control generators. |
| R2 | CH-IFF relative to the record's other conditions; specify the synthetic boundary records | §5 control 2 is rewritten. (1) Records meeting (a′)–(e) and (f$_U$): admit iff $F_C \le \theta$, refusal set exactly {(f$_C$)}. (2) Every other record: refusal set equals the independently computed failed set, and contains (f$_C$) iff $F_C > \theta$. Eight synthetic records at K = 7 with (a′)–(e) and (f$_U$) set true: $m \in \{0,1\}$, $C \in \{R, E\}$, $F_C = \theta$ and $\theta+1$, with the n for each given in a table. |
| R3 | Fix the zero argument; rank method not for `G_clkfix`; state methods; start Part B at K = 4 | §4.2: the zero holds at $1 \le K' \le Z$, and at $K' = 0$ iff $x_0$ is uniform. Methods are fixed per generator: rank for `G_lin` and `G_clk` (exhaustive agreement at $n \le 12$); enumeration over $h$ for `G_filt`; enumeration over the conditional support for `G_clkfix` and `G_clkfix_u`. The bound $Z(\cdot) \ge Z(\texttt{G\_clk})$ is added with its proof. §2.4: the K′ = 0 zero on every (a′) generator gives $K \ge 4$. §3.4: Part B starts at K = 4, and Z bounds no search. ZC row added (R11). NOTES M6. |
| R4 | m = 0 identically zero on (a′) generators; keep it as a control; correct the rationale | §2.4: the M0 statement with proof (bijective round, invariant uniform law; balanced law on $\{x \oplus q = at\}$ for the matched prior). §3.1: the class table gets a Role column, `emb_m0_all` becomes the exact-zero control, and the false rationale is replaced. §3.4: $m = 0$ is not searched in Part B (M0 with $K \le 63$). M0 row added. NOTES §3 item 7. |
| R5 | State INC-RE (E ⊆ R for m ≤ 1) and check it | §2.4: INC-RE with the component differences. §3.4: the Part B search uses $K^R_{\max}$, which contains $K^E_{\max}$. §6 item 4: an E-witness without an R-witness at the same n voids the stage. INC-RE row added. O2 recommendation updated. |
| R6 (reporting) | Per-witness $F_C$ with components; per-cell minimum $F_C$; correct NOTES O1 | §2.1: components listed for R and E. $F_C^{\rm TA}$ (transition and action only) is reported per witness. §2.3: θ-independent reporting, applied regardless of O1. §5 schema: `components`, `F_TA`, `min_F`. §6 item 3: each cell prints its minimum F_U, F_R and F_E. NOTES §6 O1: the misstatement of option (ii) is corrected; (i) is the most stringent. |
| R6 / O10 (choice) | Charge scope as an owner decision | §2.1 "Charge scope [OWNER: O10]", with the reason, the effect on m = 1's onset and the review's recommendation. §9 table and parameters block: O10 `OPEN`. NOTES A9. |
| R7 | θ for `G_clkfix` by $\log_2|\mathrm{supp}\,\mu|$; `G_clkfix_u` at n+2 and n+1 | §1.2: the matched-prior θ is justified by the invariant support and the isomorphism with `G_clk`. `G_clkfix_u` is reported at both values, governing value [OWNER: O5]. §6 item 3: cell status per θ where two apply. Parameters: `theta.G_clkfix_u` lists both. AR-C covers both values. |
| R8 | Factor outcomes per n; no pooling across n | §6 item 4: every factor outcome is per n, comparing U-witnesses only with C-cells at the same n (and, in Part B, the same K range); a cross-n summary is only a list of per-n labels with their search ranges. §6 item 5: the activity contrast is per n. |
| R9 | State what PE-01 fixes; add SIM-P1; twin footprint; narrow the backaction sentence | §4.3: the population's extent (m = 2 at n ∈ {4, 5}; K = 7, 8, 9 and 7, 10) and `INTERVENTION_NEEDED` for every member are stated in advance as fixed by PE-01's retained windows, labelled "restates PE-01". `BACKACTION_NEEDED` is stated as open via A-SIM and PE-01's passive m = 3 windows. The drafter read those windows read-only and confirmed them (NOTES §2). SIM-P1 row added. Twin footprint: §3.3, §4.3, §6 item 5. The generated sentence is narrowed to the review's wording. §6 item 10: the intervention labels are recorded only. |
| R10 | §A.44 schema; exit statuses from the host | §5 "Structured evidence": schemas `pe02-shard/1`, `pe02-measurements/1` and `pe02-verdict/1`, with keys; exit statuses as step conclusions; marker steps with frozen `if:`; `host_conclusions.json` fetched from the host API; `verdict.py` reads only those files. The field list may be completed by amendment before code, not after. |
| R11 | §A.41 rows: RF, ZC, M0, INC-RE, SIM-P1, ACT-SIM non-vacuity, RP-01 pins, workflow trigger; EX4 reproduces PE-01 | §5 rows added: RF, ZC, M0, INC-RE, SIM-P1 and WF. ACT-SIM now requires the `G_clk` countercontrol and two mutant sims to fail. RP-01 pins Python 3.12 and numpy 2.2.6 (verified in PE-01's workflow) and records versions in the shard. EX4 reproduces PE-01's n = 3..8 polynomials. |
| R12 | A-SIM: one-step hypothesis; bijectivity step; T2 as an upper bound | §3.3: the hypothesis is restated as a one-step property. Proof step 1 derives $x' = x \oplus b(\eta)$ from injectivity. T2 is stated as $m' \le m + 1$, minimality open, with the review's tightness evidence cited. NOTES O9 corrected. |
| R13 | No-extension clause; complete parameters block | §3.4: no-extension clause for N_max, every K range and every cap. §9: the block lists O1–O10 (each `OPEN` with the review's recommendation), θ per generator, `theta_by_n` for n = 3..24, `partB_K_min`, the $K^R_{\max}$ and $K^E_{\max}$ formulas with per-n values for n = 9..24 (taken from `design/charge_arith.out`), the M0, PL and ACT-SIM ranges, and the RP-01 environment. TH cross-checks formula against values as in PE-01 A1 and refuses any `OPEN`. |
| R14 | E's bit order and labelling | §2.1: γ is MSB-first; the Lehmer rank and $K$ in $S_R$ are MSB-first; truth tables start at $v = 0$; memory states use PE-01's integer labelling (`R[o, x, v]`, `Aact[o, v]`, $v_0 = 0$). EN checks γ MSB-first. |
| R15 | NOTES commit status | NOTES §1 and §4 now say revision 1 and `design/` are committed at `902c4c0d`, and that revision 2 is uncommitted. |
| UX | Full-subclass window counts against PE-01's `windows[subclass]` | §5 UX row: for `G_clk`, n = 3..8, $K \le K_{\rm cx}$, `abs` and `signed`, compared K by K for `emb_m1_all`, `emb_m2_all`, `emb_m1_passive` and `emb_m2_passive`. §3.4 Part A-pop computes every member, not only active ones. |

## Owner placeholders (not decided here)

| Id | Location | Review's recommendation |
|---|---|---|
| O1 | §2.3, §9 | (i) θ = n+1 |
| O2 | §9 | R and E separately |
| O3 | §2.2, §9 | information only, plus the class-code arithmetic |
| O4 | §3.4, §9 | 24, with the no-extension clause |
| O5 | §1.2, §9 | matched primary with uniform variant; θ for `_u` n+2 governing, n+1 reported |
| O6 | §3.4, §9 | not computed |
| O7 | §4.3, §9 | all members |
| O8 | header, §9 | rename to PE-04 before freeze |
| O9 | §3.3, §9 | adopt |
| O10 | §2.1, §9 | full description governs |

## Not applied, and why

- **The review's O3 recommendation** to add its linear-filter class-code arithmetic as a checked design fact is not
  applied. It attaches to an owner decision, and the instruction for this revision was to replay the existing design
  scripts unchanged. §2.2 records the limit instead.
- **The stage rename (O8)** is not applied, by instruction.
- **No owner choice is made.** Each of O1–O10 is a marked placeholder.

## Checks made for revision 2

- `design/least_primitive.py 24` and `design/charge_arith.py`, rerun with `python3 -I`, each reproduce their committed
  `.out` file byte for byte (`cmp`; sha256 `f4c880f4…c5ec` and `51aa19de…7ea`).
- PE-01's retained `windows` entries for `G_clk`, $K \le K_{\rm cx}$, were read (not recomputed) to confirm the §4.3
  statements.
- PE-01's workflow pins were read: `PYTHON_VERSION: "3.12"` and `NUMPY_VERSION: "2.2.6"`.
- No experiment was run, no PE-01 cell was recomputed, and nothing was committed.
