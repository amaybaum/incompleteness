# CONFIRM-OQ10-r2: focused confirmation of NOTE-OQ10-r2.md

**Verdict: ACCEPT.** All twelve CONFIRM-OQ10 findings are resolved as `RESPONSE-OQ10.md` states. The
two additions quote the rules accurately and are neutral. r2 still recommends no reading and implies
no waiver or rule change. Nothing changed beyond the stated changes.

One residual Low, N1, is recommended but does not block. The F4 text I supplied put it there.

**Object.**
- Branch `research/integration-assess-20261113`, fetched by name with no `--depth`.
- Head `cc7d3ca690bc882d832b1c2720ec3ed52b9a219a`, the single child of `dc673d62`. It adds
  `NOTE-OQ10-r2.md` (187 lines) and `RESPONSE-OQ10.md` (241 lines) and nothing else.
- `NOTE-OQ10.md` at the head is blob `9e2b4079`, the same blob as at `d82dd02d`, so r1 is unchanged.
- `c7ce4f28..cc7d3ca6` adds four files in the one directory and modifies none.
- Line numbers below are r2's.

**Method.**
- I produced my own `diff -u` from r1 to r2. Ignoring the two header lines, it is identical to the
  diff carried in `RESPONSE-OQ10.md`.
- I mapped each hunk to a finding.
- I re-checked the new quotes against `AGENTS.md` at `c3b5f37a` and against the #1097 body, comparing
  after normalizing whitespace.

***

## 1. The findings, one by one

| Finding | Resolved | Where in r2 | Note |
|---|---|---|---|
| F1 | yes | :41–46; :185–187 | The four facts are added and the flag-based clause is removed. Both #1097 quotes are verbatim. |
| F2 | yes | :113–116, :146, :148–149, :153–154, :172–173 | R-b′ appears in the readings, in the R-c sentence, in the Basis-lines paragraph and in Q1. The §A.45 rule 7 quote is verbatim. |
| F3 | yes | :137–142, :149–151 | The R-a cells read "lands after gates". The item 4 sentence applies under every basis. |
| F4 | yes | :154–160, :178–183 | The operative clause of item 6 is quoted verbatim. |
| F5 | yes | :122–126 | The 5895564670 quote is verbatim. Item 7 is scoped to established claims, and the "[R]" phrase is exact. |
| F6 | yes | :121 | |
| F7 | yes | :68, :70–73 | Both evidence-layer quotes match the notes on `main`. |
| F8 | yes | :88 | |
| F9 | yes | :37, :103–104, :185–186; new row :86 | The §A.42 item 5 quote is verbatim. |
| F10 | yes | :104–107 | |
| F11 | yes | :131, :134, :137 | The "IA2" column header is a consistent consequence of the change. |
| F12 | yes | :65–66, :90 | |

## 2. The additions

1. **Item 6 quoted in §1 (:48–52).**
   - The text is verbatim. "Removal of research evidence from `main` is never automatic." is item 6's
     first sentence. The passage from "Verified evidence …" to "no surviving claim depends on it;"
     is also verbatim.
   - The "…" marks real elisions.
   - The passage sits with the other rule quotes and draws no conclusion, so it is neutral.
2. **The R-a case in Q3 (:181–182).**
   - The point is accurate. Under R-a the records still have not met item 1's standard, so item 6's
     clause reaches them unless their own scoped claim counts as a "surviving claim". Both §A.42 item
     5 and item 6 use that phrase, and the new §3 row (:86) asks the same question.
   - It is phrased as a question and is not answered, so it is neutral.
3. **The revision line (:7) and "(r2)" in the title.**
   - Both are stated in RESPONSE.
   - The line matches the "Revision." line of IA2. §A.32 and §A.33 govern paper prose under
     `papers/`, not audit notes.

## 3. Neutrality, waiver and rule change

- **No recommendation.** The closing sentence (:185–187) now describes each reading's textual
  dependence without evaluating it.
- **Balanced history.** The added facts in the history paragraph (:41–46) sit beside the #1097 flag,
  and neither weighs for a reading.
- **No waiver or rule change.** The Standing text (:3–6) is unchanged. R-c is still "not proposed
  here". R-b′ is stated as a reading of the present text, with the merge decision serving as the
  exception "where the decision says so", and it is not proposed.
- **The owner questions** are precise. Q1 now covers R-b′, and Q3 sets out the consequence of item 6
  under each reading.

## 4. Residual finding

### N1 (Low, non-blocking): item 6 under R-d leaves out item 7, which r2's own R-d text names

- **Where:** NOTE-OQ10-r2.md:159–160 and :182–183.
- **Evidence.**
  - Both places say that under R-d, with model review meeting item 1, the records "are verified
    evidence, which item 6 keeps".
  - r2's own R-d entry (:123–126) adds a further condition. Item 7 requires independent validation of
    each material premise of an established claim, and the OA-1, OA-2 and OA-3 claims rest "partly
    on research records not independently established". So under R-d those three also need their
    [R] premises validated before their claims are established and the records count as verified.
  - W1-1's claim states no such premise.
  - This text came from my F4 fix, which overlooked F5.
- **Fix.**
  - At :159–160, replace "Under R-d, if model review meets item 1, those records are verified
    evidence, which item 6 keeps on `main`." with "Under R-d, if model review meets item 1 and, for
    OA-1 to OA-3, their [R] premises are independently validated (item 7), those records are
    verified evidence, which item 6 keeps on `main`."
  - At :182–183, replace "Under R-d with model review meeting item 1, item 6 keeps them as verified
    evidence." with "Under R-d with model review meeting item 1, and item 7's validation of OA-1 to
    OA-3's [R] premises, item 6 keeps them as verified evidence."

### Info

- :37–38 and :68 have uneven line wraps ("The #1097 PR" alone on a line; one long line). This is
  cosmetic, and nothing needs to change.

## 5. Register

- Neither `NOTE-OQ10-r2.md` nor `RESPONSE-OQ10.md` contains any of the barred strings.
- r2 has no reader-instruction phrases and no caps emphasis.
