# NOTES-BG-r3: working log for G3 unit 2(b), revision 3

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`, read from a read-only worktree.
  - Head at reading time: `27c409a07cc26182c695300cc89412629bbf1f35`.
  - `8a3c43e1` adds r2 (`G3-UNIT2B-BG-r2.md`, `NOTES-BG-r2.md`, `RESPONSE-BG-r1.md`).
  - `27c409a0` adds `CONFIRM-BG-r2.md`.
  - The committed r2 files are byte-identical to the writer's r2 (`cmp`).
- **Files.**
  - r1 was written by the writer and committed at `4acb3a49` by the coordinator.
  - r2 was written by the writer and committed at `8a3c43e1` by the coordinator. NOTES-BG-r2 §1 says the
    writer did not commit, push or post r2. That was true when it was written and is inaccurate at the
    head (CONFIRM-BG-r2 BC-13). NOTES-BG-r2's pointer to "RESPONSE-BG-r1 §3" for the hunk map should
    read §4. r1 and r2 are not edited.
  - r3 (`G3-UNIT2B-BG-r3.md`, this file and `RESPONSE-BG-r2.md`) was written in the working area. The
    writer did not commit, push or post it.
- **Authority.** #873 c.6865179466, QU5. The coordinator's request for r3 is a session message, not an
  owner record.

## 2. Reading log (additions in r3)

| Source | What was used |
|---|---|
| CONFIRM-BG-r2.md | in full |
| GR:526–532 | the Bullet Cluster and CMB paragraphs; "requires a non-oscillating gravitational source"; `ρ_E` (i)–(iv); "the Jacobson sourcing is spatially local" (GR:532) |
| GR:354 | item (5): "the Type II channel (a structural reading, not a derived law)" |
| GR:633 | "The Type II running-vacuum functional form is not derived" |
| GR:374–380 | re-read for `Λ_eff(H)`, commitment (i) and Type II |
| SM:160 | "(iii) is a definition and (iv) an identity" |
| U2Ar3:303–304, :548–549, :696 | the witness's partition; the gap wording; Z_0 under Reading G |
| U1r5:222–225, :506 | definition of `Z`; the epoch-differential caveat |

## 3. Corpus search, widened (§A.19; CONFIRM-BG-r2 BC-8)

`git grep -i -E` at `c3b5f37a` over `papers/*.md` and `book/*.md`, with FULL.md excluded. Patterns:
"gravitational source", "source term", "sources? (curvature|gravity|geometry)", "sourcing
(gravity|curvature)", "as a source", "Jacobson sourcing", "in virtue of", and "grounds? (the|its)
(metric|curvature)".

- **Hits in GR.md:** :340, :352, :358, :400, :448, :528, :530, :532, :577 and :581.
- **Hits elsewhere:** Introduction.md:159 and :161; book ch07-gravity.md:167, :175, :177 and :209;
  ch09-universality.md:256; ch18-beyond.md:136; ch19-open-problems.md:38.
- The book hits restate GR §6.2 and §7.1 ("commensurable as gravitational sources", "the stress-energy
  that sources gravity", "whether that response feeds back as a source", "whether the offset sources
  curvature is the coupling step").
- **Result.** No hit states whether a law's source terms ground its solutions. GR:376–380 ("forces") and
  GR:528–530 ("gravitational source", "source term") were added to K3 and to F4-5.

## 4. Order of work

1. Read CONFIRM-BG-r2 in full and checked the committed r2 files with `cmp`.
2. **BC-1 (r2's F1 and F2 are not co-constraint formalizations).** Checked it against r2:314–318 and
   r2:362. It is correct: read literally, r2's rule returned (A). Added F5 as repair R-4 and recorded it
   as a repair.
3. **BC-2 (F4-6).** Checked it against r2's §3.4, which covers a constant Λ term. It is correct. I
   introduced F4-null as the narrower scope under which the Jacobson route leaves the witness unreached.
4. **BC-3 (F4-5).** Read GR:526–532 and re-read GR:374–380.
   - Accepted the cost framing and the extended list.
   - Disagreed in part on the §8.3 branch (GR:573 relocation, RESPONSE-BG-r2 BC-3).
   - Added F4-7 (the label escape) and F4-8 (cost or (b2)).
   - F4-8 found that, without §8.3, uniform F4 on Reading G leaves the running-vacuum channel
     unrealizable. It also found that the corpus states that channel as a structural reading
     (GR:354), not a premise, so this is a cost. QB7 records the alternative.
5. Applied BC-4 to BC-13.
6. Re-applied the rule. Outcome (C). The outcome is unchanged from r2, and the reasons are those of BC-1
   to BC-3.

## 5. Decisions

1. **The outcome stays (C).** With F5 added, both kinds are admissible. The r2 reading that literally
   returned (A) came from an omitted formalization, and R-4 records it.
2. **F4-8 is a cost, not (b2),** on the stated status of the Type II channel (GR:354, GR:633, GR:400).
   If the owner holds the channel as a premise, the branch without §8.3 gives (B) (QB7). This is reported
   as a branch outcome and not adopted.
3. **The §8.3 relocation** is argued in RESPONSE-BG-r2 BC-3, stated in r3 as disputed, and put to the
   owner (QB7).
4. **No premise adopted, no manuscript change, no Lean build, no claim about Λ.**

## 6. Checks

- No computation, script or build was run apart from the three permitted checks.
- **The r2→r3 diff.** `diff G3-UNIT2B-BG-r2.md G3-UNIT2B-BG-r3.md` gives 82 hunks. r3 has 793 lines, of
  which 325 are unchanged from r2. RESPONSE-BG-r2 §4 maps the hunks.
- **Barred-string scan of the three r3 files.** It found no forbidden path prefix and none of the
  §A.32/§A.33 phrase families.

| Check (worktree at `27c409a0`, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `tools/claims_check.py` | exit 0: "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | exit 0: "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | exit 0: "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

None of these scans the drafts. The worktree stayed clean (`git status --short` empty before and after).

## 7. Off-`main` references (§A.42 item 8)

These are as in NOTES-BG-r2 §6, with the following additions:

| Reference | Claim it is attached to | Class |
|---|---|---|
| `CONFIRM-BG-r2.md` at `27c409a0` (branch) | the findings r3 answers | support off `main`; lands with #1275 |
| `G3-UNIT2B-BG-r2.md` at `8a3c43e1` (branch) | the statements r3 withdraws or restates | support off `main`; lands with #1275 |

## 8. Limits

- By hand. Scoped to Reading G, case β, and conditional on N5-G.
- F4 and F5 are readings [P].
- The rule was repaired twice after reviews that named the expected outcome.
- The §8.3 relocation is disputed.
- The §A.31 fixed point is not reached.
