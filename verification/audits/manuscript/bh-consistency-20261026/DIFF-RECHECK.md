# Confirmation re-check of PR #936, head 78705611

- **Object:** the single commit `78705611` on top of `4c0d705e`.
- **Method:** read-only. Checks ran in a detached worktree at `bhfix/review2/rv`, which was removed afterwards with
  `git worktree remove`. Nothing was garbage-collected, and the drafter's worktree is still at `78705611`.

**Verdict: ACCEPT WITH NITS.** The nits are in §5 and §6. None of them touches the manuscript text of this
commit.

## 1. Required changes R1–R4, and the optional nits

**R1–R4.** I extracted each of the six replacement texts in DIFF-REVIEW §7 and searched for it as a fixed string
at `78705611`. Each occurs exactly once where it should:

| Text | Where found |
|---|---|
| R1, GR:811 | GR |
| R1, GR:817 | GR |
| R1, ch07:130 | ch07 and FULL |
| R2, GR:835 | GR |
| R2/R4, ch07:126 | ch07 and FULL |
| R3, ch07:147 | ch07 and FULL |

The re-grep of the superseded phrases is clean:
- "keeps the black hole", "throughout the evaporation" and "arrives at a Page curve" have 0 survivors.

**Optional nits.** All three are applied:
- GR:611 now reads "measure concentration [29, 61]";
- GR:869 reads the same;
- GR:605 has "develops" in place of "resolves".

## 2. The H-decouple definition

**The definition is exactly the closure A.8–A.9 use**, and adds no physical assumption.
- **Closure.** Theorem A.8 is stated "for the dynamics φ on the energy shell Σ_E ⊂ H_B ⊗ H_R". That makes
  φ a bijection of a B∪R shell, which is a closed system.
- **The "pure joint state" clause is also A.8's own assumption:**
  - its proof concerns S(Tr_B |ψ⟩⟨ψ|) for states |ψ⟩ of the shell;
  - H-scramble equidistributes the orbit "over quantum pure states";
  - the concentration bound is for Haar-random pure states.
- **The time-window sentence** ("over whole cycles of the dynamics, not only over the evaporation") correctly
  matches the full-cycle averages of the restated A.9.

## 3. The R2 consequence

It is stated as a fact at GR:835 and ch07:126, with no remedy adopted:
- H-scramble fails in A.7's setting;
- it "requires an initial superposition of configurations or a bipartition not aligned with them";
- "which of these the substratum supplies is open".

The "requires … or …" clause is the contrapositive of BH-02 C6(a), a proved necessary condition. No choice
between the two is made.

## 4. Mirrors, generated files and checks

- **FULL mirror.** All 3 changed ch07 lines occur exactly once in FULL, and FULL's diff adds exactly those 3
  lines. `mirror_check` reports 0 chapter lines absent.
- **`.tex`.** The diffs are content plus reflow only: 7 hunks in GR.tex and 5 in FULL.tex. The
  `source-sha256` stamps match the new `GR.md` (6e33f5fd…) and `FULL.md` (5f5e50a4…).
- **Checks at `78705611`, all OK:**
  - `coverage_check` (128 statements; the A.7 statement is unchanged, so its fingerprint stands);
  - `voice_check`, `claims_check`, `duplicate_check`;
  - `dependency_label_check --strict`;
  - `artifact_placement_check`;
  - `legacy_records_check 78705611…`: 303 records, all intact.

## 5. The committed records (`verification/audits/manuscript/bh-consistency-20261026/`)

**Byte-identical to their sources:**
- `FINDINGS.md`, `REVIEW.md` and `DIFF-REVIEW.md`;
- `CHANGE-NOTE.md`;
- the investigator's probes (`itemF_check.*`, `page_checks.*`);
- my probes, renamed `review-evap.py`, `review-page.py` and `review-r12.py` (from `evap.py`, `page.py` and
  `r12.py`).

**Attribution.** Nothing is misattributed. README's summaries of FINDINGS, REVIEW and CHANGE-NOTE are accurate.

**Nits, all in records only:**
- **N1, README and CHANGE-NOTE §6 overstate the A.8 finding.**
  - They say A.8's value "holds/is correct *only when* the energy shell is the full product space".
  - The evidence supports less: an exact counterexample (the diagonal shell) plus BH-02's certified
    Hamming-weight cases. It shows the value **fails in general on a proper shell subspace** and **holds when
    the shell is the full product space**. It does not exclude a special shell whose Haar mean happens to
    coincide.
  - My own DIFF-REVIEW §6 has the same "only when" phrasing. I correct it here, rather than editing the
    committed copy in place.
  - Suggested README text: "It also shows, by exact algebra, that Theorem A.8's value does not hold in general
    when the energy shell is a proper subspace; it holds when the shell is the full product space. That error
    is left to a separate change."
- **N2, CHANGE-NOTE has a stale header.** Now that it is committed, its header still reads "(draft,
  uncommitted)", and line 7 says "Nothing is committed". Suggest "(record of the change)" and deleting line 7.
- **N3, README's path convention matches no path in the records.** It says "Paths written `S/…`", but the records
  use scratch-relative paths: `paper/r11/…`, `r11/rev/…`, `bhfix/…`, `mainwt`. Suggest: "Relative paths such as
  `paper/r11/…`, `r11/rev/…` and `bhfix/…` refer to the session's scratch directory, which is not part of the
  repository; the reviewer's `r11/rev/{evap,page,r12}.py` are committed as
  `probes/review-{evap,page,r12}.py`."

**No secrets or absolute scratch paths.** I scanned the records for `/tmp`, `@` and `token`: no secrets, no
e-mail addresses, and no absolute scratch paths.

## 6. Remaining overclaim

**Inside the PR's scope there is none.** Every Page-curve statement is cycle-averaged and conditional on
H-scramble and H-decouple, with the single-trajectory reading stated as open.

**The one remaining overclaim is pre-existing: Theorem A.8 / BH-02 C6(c).**
- A.8 still displays S_Page(d_B, d_R) for an arbitrary energy shell Σ_E.
- Every sufficiency statement inherits it: A.9's label, GR:605/611/717/869, ch07:116/:130/:149, ch19:72 and
  glossary:113.
- CHANGE-NOTE §6 records it correctly as a known open error.
- **A same-session tension.** The error is now settled by exact algebra and recorded in a committed record,
  while the manuscript still asserts the unrestricted statement. §A.27 asks that a result bearing on a manuscript
  claim be applied to the text in the same session.
- **Not a reason to block.** The owner directed that the diff not be expanded, and this PR does not worsen the
  gap.
- **Recommendation.** Before any release or DOI deposit, or in this PR if the owner agrees, apply the
  minimal scope sentence below. It restricts scope rather than adding an assumption, and it is the
  "explicit hypothesis" remedy 1 of the change note.

GR, after the display of $S_{\text{Page}}$ in Theorem A.8, add a sentence to the statement:
> *The value $S_{\text{Page}}(d_B, d_R)$ is the large-dimension Haar mean over pure states of the full product space $\mathcal{H}_B \otimes \mathcal{H}_R$; on a proper shell subspace the Haar mean depends on the shell and in general differs from it, so the value as displayed applies with $\Sigma_E = \mathcal{H}_B \otimes \mathcal{H}_R$.*

- **Coverage ledger.** This changes A.8's statement, so its LEDGER fingerprint must be re-affirmed in the same
  commit, as was done for A.7 and A.9.
- **Book.** Mirror it into ch07 §7.6 with a short clause, for example after the ch07:130 display: "with
  the full product space as the shell; on a proper shell subspace the value differs".
