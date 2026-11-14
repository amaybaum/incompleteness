ACCEPT WITH CHANGES — `S3-PLAN-r5.md` at `ac70c70ae5c75fd2466860c694b789f54d429770` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Focused confirmation of the S3 plan, r5

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**What was read.**
- `S3-PLAN-r5.md` and `RESPONSE-S3-PLAN-r4.md`. The copies supplied to me are identical to the
  committed files.
- `S3-PLAN-r4.md` is unchanged, and `REVIEW-S3-PLAN-r4.md` is preserved as delivered.
- The full diff from r4 to r5.

**Line numbers** are r5's.

## 1. R5 at every site

R5 is resolved at every site:
- **The D-1 coupling bullet (ll. 540–550).**
  - It quotes the MR-1 caveat: "the absence of a proved ready supply is an open sourcing problem, not
    a proof that no ready supply can exist".
  - It reports a failure of (β) that rests only on unsourced retention of `s_A` as "unsourced at
    (β)–(δ)", not "empty on K1".
- **D-1's outcomes, now four (ll. 551–566).**
  - The new outcome is "Unsourced at (β)–(δ) … an open sourcing gap, not a failure. Route M stays open
    on K1, and this outcome does not count toward (a′)".
  - "Empty on K1" is narrowed to a failure "for a reason that does not rest on unsourced retention of
    `s_A`".
- **(a′) (ll. 650–653).** The four outcomes are listed, and "unsourced at (β)–(δ)" leaves route M
  open.
- **The U4 row (l. 700).** It adds "or reported unsourced at (β)–(δ)".

## 2. Nothing else changed

- The diff touches only the title, the revision header, and the four sites above.
- The response says the r3 and r4 revision notes are kept as historical, and the diff confirms it.

## 3. The native-marker miss branch

**It is not fully consistent with R5 (ll. 560–566; l. 651).**
- (a′) counts "a native-marker miss once (γ) is supplied" toward closure.
- By the coupling bullet, a native uniform marker is a which-path detector only if `s_A` is held
  elsewhere: (β) "generically fails unless `s_A` is held elsewhere".
- So the native-marker miss branch is reached only when (β) holds through retention of `s_A`.
  - If that retention is *sourced*, the miss rests on sourced structure, and counting it toward
    closure is correct.
  - If the retention is *assumed*, (β) holds only through an assumed component. The miss then
    concerns a partly assumed apparatus, exactly as the quiet-marker case does, which r5 reports "as
    such" and does not count.
- The miss branch does not say this. It can be read as reachable with an assumed retention of `s_A`,
  and as counting toward (a′) all the same. That reopens, for the miss branch, the gap R5 closed for
  "empty on K1".

**R6 (required, one sentence).** Add to the *Native marker* bullet:
> This branch requires (β) to hold with a sourced retention of `s_A`. If the retention is assumed,
> the miss concerns an assumed apparatus, is reported as such, like the quiet marker, and does not
> count toward (a′).

Optionally, make (a′) say the same: "a native-marker miss with sourced retention of `s_A`, once (γ)
is supplied".

**No other new issue.** There is no new premise, no authorization, and no conditional result stated
as established. The new outcome is an open gap, explicitly not a failure.

## 4. Verdict

**ACCEPT WITH CHANGES.**
- R5 is resolved at every site, and nothing else changed.
- R6 is a one-sentence clarification of the same kind as R5. With it applied, a diff check suffices.
