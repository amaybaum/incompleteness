# SC-40: the (C2) contrapositive and the source of (C3) (Main §1.3, §3.4; companions; book)

Base `main` at `0d917665`. Branch `corpus/sc40-c2-c3-statements`.

## Findings

| Finding | Where recorded |
|---|---|
| **F1.** The (C2) contrapositive is stated with $I^*$, "$I^*>0$ … $\varepsilon_{\min}(I^*,n_V)$". Main defines $I^*=\sup_t I(X_{<t};X_{>t}\mid X_t)$, while the physical-memory theorem bounds only the one-step memory $M_k=I(X_{<k};X_{k+1}\mid X_k)$. | `FULL-CORPUS-AUDIT-CONSOLIDATED-60c976fe.md` row "Main:465"; `FULL-CORPUS-AUDIT-60c976fe-A.md` (Main §1.3 L76, §3.4 L465/L470); `-VERIFY.md` item 7 (branch `draft/oi-introductory-paper-20261025` at `9dc2b069`). |
| **F2 (SC-19).** "(C1) and (C3) follow from (C4)", with the reason "the observed conditional information must pass through the hidden sector". (C3) holds in every faithful realization by the whole-future data-processing bound, so the reason given is not its source. | `FINDINGS.md` R-36 (I-108, re-rated by S9-A5) on `audit/intro-corpus-20261026` at `16fc745d`; `-A.md` (Main §1.3 L72, L78); `-VERIFY.md` item 9; `CORRECTIONS-LEDGER.md` open list ("SC-19"). |

SC-27 (#958) already corrected Main :610 ("(C3) by the data-processing argument of (c) applied to the whole visible future …, a bound that holds in every faithful realization") and Substratum :137 (C3 with no mixing hypothesis). Those sites are not changed here.

## Per-claim record

### F1. The (C2) contrapositive

**Original claim** (Main.md:465, the physical-memory theorem):
> Contrapositive: observed conditional memory $I^* > 0$ at an accessible order forces $\varepsilon \geq \varepsilon_{\min}(I^*, n_V) > 0$ — the hidden sector has not mixed by the coupling time.

**Defect.**
- The proof bounds $I(X_{<k};X_{k+1}\mid X_k)\le 2[\varepsilon\log(n_V-1)+h(\varepsilon)]$ at one coupling time $k$, with $\varepsilon$ the distance at that time. Its contrapositive is in $M_k$, not in $I^*$.
- By the chain rule, $I(X_{<t};X_{>t}\mid X_t)=\sum_{j\ge t}I(X_{<t};X_{j+1}\mid X_{t..j})\le\sum_{j\ge t}M_j$. So $I^*$ can exceed every single $M_k$, and the $I^*$ form does not follow.
- $\varepsilon_{\min}$ was never defined. Read as the inverse of the bound on $[0,1-1/n_V]$, $\varepsilon_{\min}(I,n_V)$ exists only for $I\le 2\log n_V$. But $I^*$ reaches $K\log n_V$. The check gives an exact example with $I^*=3$ bits at $n_V=2$, above $2\log_2 2=2$. There the $I^*$ statement has no meaning, and the theorem's own parenthesis "$\varepsilon_{\min}<1-1/n_V$" fails.
- Since $M_k\le\log n_V<2\log n_V$, the $M_k$ form is always well defined.

**Correction.**
- The contrapositive is stated in $M_k$ at the coupling time $k$, keeping every hypothesis: the coupling-step model, the reference prior $\pi_H$, the realized-$\varepsilon$ reading without mixing, and the mixing hypothesis for the slow-bath form.
- $\varepsilon_{\min}(M,n_V)$ is defined in the theorem as the least $\varepsilon\in[0,1-1/n_V]$ at which the right-hand side equals $M$. The theorem also states why it exists and why it lies below $1-1/n_V$.

**Downstream consequences.**
- Every restatement now carries $M_k$ at an accessible order $k$, and "that coupling time". These are Main :76, :453, :472, :492 and :732, Substratum :129 (twice) and :137, and glossary :27 with its FULL mirror.
- The slow-bath form in Substratum :129 becomes "a lower bound on the relaxation residue at coupling time $k$".
- No result that uses (C2) changes:
  - The characterization does not use (C2) (Main §3.4, Remark "(C2)'s role").
  - The Introduction's L122 already has the $M_k$ form.

### F2. The source of (C3)

**Original claims.**
- Main.md:72: "(C1) and (C3) follow from (C4) in any faithful realization".
- Main.md:78: "Dependency — like C1, C3 follows from C4 within any faithful realization: the observed conditional information must pass through the hidden sector, so data processing gives $\log_2|\mathcal{C}_H| \geq I^*$ automatically. Exhaustive enumeration confirms it and finds the bound SATURATED …"
- Main.md:620: "(C3) follows by data processing, with the bound … saturated …; both are certified by exhaustive enumeration in `primitive_probes.py`."
- GR.md:52: "since [Main §3.4] derives (C1) and (C3) from (C4)".
- Substratum.md:129: "C1, C3, and C4 for the memory-bearing temporal sector are derived from E1–E3, A1–A2 together with **M1-T** … conditional on M1-T, they hold without further hypothesis."
- ch00-introduction.md:37 (FULL :273): "C1 and C3 follow from C4".
- ch01-observation.md:133 (FULL :477): "with C1 and C3 its consequences in any faithful realization".
- ch01-observation.md:201 (FULL :545): "C4 coincides with the non-Markovianity clause and C1 and C3 follow from it".
- ch01-observation.md:259 (FULL :603): "C4 primitive, C1 and C3 its checkable consequences".
- ch07-gravity.md:30 (FULL :1909): "since C1 and C3 follow from C4 in any faithful realization".
- glossary.md:29 (FULL :6629): "$\log_2 |\mathcal{C}_H| \geq I^*$, the capacity floor — the data-processing bound $M_t \leq I(X_{<t}; H_t \mid X_t) \leq \log_2|\mathcal{C}_H|$ in per-process form".

**Defect.**
- (C3) does not depend on (C4). In every deterministic realization the whole visible future is a function of $(X_t,H_t)$, so $I(X_{<t};X_{>t}\mid X_t)\le I(X_{<t};H_t\mid X_t)\le\log_2|\mathcal C_H|$. Markov realizations are included (Theorem (C3 necessity), §3.4).
- "Follows from (C4)" is true only vacuously, and the reason given misattributes the source.
- Substratum made (C3) conditional on M1-T.
- The glossary derived $I^*$ from the one-step bound on $M_t$, which gives only $\log_2|\mathcal C_H|\ge\sup_t M_t$. This is R-36's point: $M_1=0$ is possible while (C3) needs one bit.
- At Main:78 the cited enumeration checks only realizations with a readback gap, and only in the per-order form $\max_k M_k\le\log_2|\mathcal C_H|$, by floating point. "Confirms it" overstated what it checks.

**Correction.**
- (C1) follows from (C4). (C3) holds in every faithful realization by the capacity bound.
- At Main:78 the enumeration is described as what it is. Attainment of $I^*=\log_2|\mathcal C_H|$ follows from the squeeze $M_k\le I^*\le\log_2|\mathcal C_H|$.
- The caps word "SATURATED" (§A.33) becomes "attained".
- The glossary's derivation is the whole-future bound.

**Downstream consequences.**
- Nothing that used (C3) loses support: (C3) holds more broadly than the old sentences said.
- The arguments "verifying (C1) and (C3) does not supply (C4)" (GR:52, ch07:30) stand, with the corrected reason.
- Main :620's "The equivalence could therefore be stated with (C4) alone" stands.

## Site table

| Site (at `0d917665`) | Was | Now | Source |
|---|---|---|---|
| Main :72 | (C1) and (C3) follow from (C4) | (C1) follows from (C4); (C3) holds in every faithful realization by the capacity bound of §3.4 | Main §3.4 C3 necessity; :610 |
| Main :76 | $I^*>0$ … $\varepsilon_{\min}(I^*,n_V)$ at the coupling time | $M_k=I(X_{<k};X_{k+1}\mid X_k)>0$ at accessible order $k$ … $\varepsilon_{\min}(M_k,n_V)$ at that coupling time | physical-memory theorem |
| Main :78 | like C1, C3 follows from C4 …; enumeration "confirms it", "SATURATED" | C3 does not depend on C4, by the whole-future data-processing bound; the enumeration is stated at its actual scope; attainment by the squeeze | C3 necessity; `primitive_probes.py`; check (4) |
| Main :453 | $\varepsilon\ge\varepsilon_{\min}(I^*,n_V)$ | $\varepsilon\ge\varepsilon_{\min}(M_k,n_V)$ | physical-memory theorem |
| Main :465 | contrapositive in $I^*$; $\varepsilon_{\min}$ undefined | contrapositive in $M_k$ at order $k$; $\varepsilon_{\min}(M,n_V)$ defined, with existence and the bound $<1-1/n_V$ | proof of the theorem; check (1) |
| Main :472 | memory $I^*$ … $\varepsilon_{\min}(I^*,n_V)$ | $M_k>0$ at order $k$ … $\varepsilon_{\min}(M_k,n_V)$ at that coupling time | same |
| Main :492 | $\varepsilon\ge\varepsilon_{\min}(I^*,n_V)$ | $\varepsilon\ge\varepsilon_{\min}(M_k,n_V)$ | same |
| Main :620 | (C3) follows by data processing; "both are certified" | (C3) holds in every faithful realization by data processing over the whole visible future; "both are checked by exhaustive enumeration at small sizes" | C3 necessity; `primitive_probes.py` |
| Main :732 (ledger table) | memory $I^*$ … $\varepsilon_{\min}(I^*,n_V)$ | $M_k>0$ at order $k$ … $\varepsilon_{\min}(M_k,n_V)$ | physical-memory theorem |
| Substratum :129 | C1, C3, C4 derived with M1-T; $I^*>0$ … $\varepsilon_{\min}(I^*,n_V)$ (twice) | C1, C4 derived with M1-T; C3 holds in every faithful realization; $M_k$ form (twice) | Main §3.4 |
| Substratum :137 | memory … $\varepsilon_{\min}(I^*,n_V)$ | $M_k>0$ at order $k$ … $\varepsilon_{\min}(M_k,n_V)$ at that coupling time | Main §3.4 |
| GR :52 | [Main §3.4] derives (C1) and (C3) from (C4) | (C1) follows from (C4) and (C3) holds in every faithful realization [Main §3.4] | Main §3.4 |
| ch00 :37, FULL :273 | C1 and C3 follow from C4 | C1 follows from C4, C3 holds in every faithful realization by the capacity bound | Main §1.3 |
| ch01 :133, FULL :477 | C1 and C3 its consequences | C1 its consequence, C3 holding in every faithful realization by the capacity bound | Main §1.3 |
| ch01 :201, FULL :545 | C1 and C3 follow from it | C1 follows from it, and C3 holds in every faithful realization by the capacity bound | Main §1.3 |
| ch01 :259, FULL :603 | C1 and C3 its checkable consequences | C1 its checkable consequence, C3 a capacity bound every faithful realization meets | Main §1.3 |
| ch07 :30, FULL :1909 | since C1 and C3 follow from C4 | since C1 follows from C4 and C3 holds in every faithful realization | Main §1.3 |
| glossary :27, FULL :6627 | observed conditional memory … at least $\varepsilon_{\min}$ | $M_k>0$ at order $k$ … $\varepsilon_{\min}(M_k,n_V)$ at that coupling time | Main §3.4 |
| glossary :29, FULL :6629 | $\log_2\lvert\mathcal C_H\rvert\ge I^*$ from $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2\lvert\mathcal C_H\rvert$ | from $I(X_{<t};X_{>t}\mid X_t)\le I(X_{<t};H_t\mid X_t)\le\log_2\lvert\mathcal C_H\rvert$ over the whole visible future, in every faithful realization | Main §3.4 C3 necessity |

Rebuilt: `papers/{Main,Substratum,GR}.{tex,pdf}` and `book/The-Incompleteness-of-Observation-FULL.{tex,pdf}`.

| Document | Pages before → after | Median characters per page before → after |
|---|---|---|
| Main | 96 → 96 | 3273.5 → 3299 |
| Substratum | 53 → 53 | 3254 → 3254 |
| GR | 88 → 88 | 3179.5 → 3179.5 |
| Book | 558 → 558 | 3045 → 3046.5 |

## Evidence level of each corrected claim

- **Physical-memory theorem, $M_k$ contrapositive.**
  - The bound itself is a written proof (Fannes–Audenaert). It is probe-certified on a parametric family by `c2_mixing_probes.py`, whose exact CMI is the $M_1$ form.
  - The theorem has no Lean statement, and its coverage level stays P.
  - The definition and range of $\varepsilon_{\min}$ are elementary algebra. With $g(\varepsilon)=2[\varepsilon\log(n-1)+h(\varepsilon)]$, $g'(\varepsilon)=2[\log(n-1)+\log\frac{1-\varepsilon}{\varepsilon}]>0$ for $\varepsilon<1-1/n$, and $g(1-1/n)=2\log n$.
  - The check gives a float control of the endpoint and of monotonicity for $n=2..11$.
- **(C3) in every faithful realization.**
  - Written proof (§3.4, data processing over the whole future).
  - Kernel-checked in joint-law form: `c3_necessity`, ledger `MAIN:T-c3-necessity`. The time-$t$ reading is on paper; SC-29/#961 records this.
  - No kernel identifier was added to any edited paragraph.
- **Attainment of $I^*=\log_2|\mathcal C_H|$ at $(2,2)$ and $(3,2)$.**
  - Exact, dyadic: check (4) shows bijections with $M_1=I(X_0;X_2,X_3\mid X_1)=1$ bit.
  - The probe `primitive_probes.py` (rerun: ALL CHECKS PASS) is a floating-point enumeration of the per-order form over gap realizations.
- **The $I^*$ form is ill-posed in general.** Exact: check (2) gives the copy process with $I^*=3$ bits at $n_V=2$.
- **The chain-rule bound $I(X_{<t};X_{>t}\mid X_t)\le\sum_{j\ge t}M_j$.** Written proof (above), with a float control on 300 random laws, check (3). It is used only in this record, not added to the manuscript.

Check script: `c2_c3_check.py`, run as `python3 -I c2_c3_check.py`, with output in `c2_c3_check.out` (ALL PASS).

## Coverage, census, Lean

- **Coverage.** `MAIN:T-physical-memory-c2-process-form` was re-affirmed, with its fingerprint moved `4c4f0d290436802c` → `0680344cc441317c`. The ID, level P, checks and assumptions are unchanged, and the assumptions field already names both forms. No other canonical statement moved.
- **Lean census.** Not touched. No cited identifier changed.
- **Lean.** No correction here needs a Lean change; nothing **requires formal change**.

## Re-grep (papers/*.md, book/*.md)

| Pattern | Count | Note |
|---|---|---|
| `varepsilon_{\min}(I^*` | 0 | |
| `memory $I^* > 0$` | 0 | |
| `(C1) and (C3) follow` | 0 | |
| `derives (C1) and (C3)` | 0 | |
| `C3 follows from C4` | 0 | |
| `C1 and C3 its` | 0 | |
| `C3) follows by data` | 0 | |
| `varepsilon_{\min}(M_k, n_V)` | 12 | |
| `C3 holds in every faithful realization` | 7 | |
| `(C3) holds in every faithful realization` | 3 | |
| `C1 and C3 follow` | 1 | Main :82, deliberately left; see Not changed |

Legitimate uses that survive:
- "C1 and C3 are necessary diagnostics" at Main :20 and :764, and "C1 and C3 diagnose" at Substratum :323. Necessity is correct, since (C3) holds always.
- ch01 :155, "C1 and C3 are its preconditions". These are necessary conditions, which is correct.
- Explainer :352, "⟹ C1, C3, C4 (necessity)", which is correct.

## Claims made conditional or removed

- **Removed:**
  - the $I^*$ form of the (C2) contrapositive, at all 10 sites;
  - the stated reason "the observed conditional information must pass through the hidden sector" as the source of (C3);
  - "certified" for the enumeration at Main :620, which is now "checked".
- **Made conditional:** nothing.
- **Strengthened:** (C3) is stated as unconditional where it was attributed to (C4) or to M1-T. That is its proved scope (SC-27).

## Not changed, and why

- **Main :82** ("C1 and C3 follow as necessary diagnostics of the mediation and its capacity"). #968 (SC-33) changes this line. The phrase is ambiguous rather than false. After #968 lands, it should read "C1 follows as a necessary diagnostic of the mediation, and C3 holds in every faithful realization". This is the one open item of the unit.
- **`papers/oi_lattice_code/foundations/primitive_probes.py`.**
  - Its header and print say "C1 and C3 are its consequences" and "C4 forces C3".
  - Section (B) restricts to gap realizations and uses $\max_k M_k$ under the name I*.
  - Its result lines are accurate, so the code is left unchanged.
  - Follow-up: run (B) over all realizations with Main's past–future $I^*$, in exact arithmetic.

## Overlap with open PRs

**#964 (SC-22).** It changes glossary :29 and FULL :6629 later in the same line, renaming "partially-quantum" to "restricted quantum-statistical". This unit changes only the C3 derivation clause at the start of the line. The textual conflict is resolved by keeping both edits.

No other edited line is changed by #961, #962, #963, #967, #968, #969 or #971 at `0d917665`, checked with `git diff 0d917665...origin/<branch>`.

## Cross-unit dependencies (shared definitions, scopes, sentences)

1. **$\varepsilon_{\min}(M,n_V)$** is now defined at Main §3.4 (physical-memory theorem). Any unit or PR that writes $\varepsilon_{\min}(\cdot)$ must use the $M_k$ argument. #962 (SC-28, "C2 scope") and #961 (SC-29) touch nearby C2 text; neither edits these lines.
2. **The physical-memory theorem statement** has a new fingerprint (coverage ledger). Any unit that edits the same statement must re-affirm it again.
3. **(C3) scope: "holds in every faithful realization".** This relies on Theorem (C3 necessity) and on #961's joint-law scoping of `c3_necessity`, whose time-$t$ reading is on paper. A unit narrowing C3's scope (#961) must keep this wording consistent.
4. **The sentence at Main :72** ("Companions and independence") and the C3 Dependency clause at Main :78.
5. **Substratum :129's first sentence.** C3 is no longer listed among the M1-T-derived conditions. SC-34 (#971) changes Substratum :135, an adjacent line not shared.
6. **Main :620** (Remark, which condition is primitive) and **Main :82** (#968; see above).
7. **The Introduction (r32)** already states the $M_k$ form and "(C3) holds by the capacity bound". It cites Main §1.3 and §3.4, which now agree with it.

## Open research questions (for #970)

- **A quantitative $I^*$ form.** Does some bound of $I^*$ in terms of the realized distances hold?
  - The chain rule gives $I^*\le\sum_{j}2[\varepsilon_j\log(n_V-1)+h(\varepsilon_j)]$ over the coupling times of the window.
  - The same Fannes argument applied to the hidden posteriors suggests $I(X_{<t};X_{>t}\mid X_t)\le I(X_{<t};H_t\mid X_t)\le 2[\varepsilon_t\log(|\mathcal C_H|-1)+h(\varepsilon_t)]$, with $|\mathcal C_H|$ in place of $n_V$. This needs the future to depend on the past only through $(X_t,H_t)$.
  - That is a two-line argument, not added to the manuscript, and not reviewed. If wanted, it should be stated and proved as a separate result.
- **The probe.** Exact rework of `primitive_probes.py` (B), as above.

## Checks

- `python3 tools/release_gate.py`: all steps pass except `lean-axioms`, which needs the local toolchain.
- `python3 tools/coverage_check.py`: OK (128 canonical statements).
- `python3 verification/lean/edge_rigidity_probe.py`: ALL CHECKS PASS.
- Scan of added lines: no §A.32/§A.33 phrase, caps, revision voice, local path or secret.
- `sh ./build.sh Main Substratum GR` and `sh ./build.sh --book`: OK, with no dropped glyphs.
