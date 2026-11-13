# REC-1 r6: focused confirmation

**Object.** Draft PR #1268 at exact head `1ab6371b16cc9935e8778a712e2d3ec82798e6b8`, a single child of
`6de32c95`.
- `1ab6371b` adds `REC-1-r6.md` and `REC-1-RESPONSE-r5.md`.
- `6de32c95` adds only `REC-1-CONFIRM-r5.md`, which is byte-identical to my `CONFIRM-r5.md`.

I read ChatGPT review 5890968976 (posted by `amaybaum`, 2026-11-13T12:27:37Z, at `6de32c95`) from
the API and diffed `REC-1-r5.md` against `REC-1-r6.md` myself, read-only.

## Verdict: **ACCEPT WITH CHANGES** (2 one-sentence edits)

1. **P0 is three-way and matches the review.**
   - *Pass* holds only when the whole operational witness is validated for the whole class: the
     coset-mixture description, every needed coset reachable, each coset's identity operationally
     determined by held records, and the C-PM indicator and equivalence effects exhibited. The law
     form alone is not a pass. A pass is subject to P4, including O-V.
   - *Out of form*: the preparations are listed, and OBL-SP continues on them.
   - *Unresolved* is O-U unless an independent classicality proof or a contextual counterexample is
     supplied. It is never O-C from the coset form alone and never a non-classical witness.

   One sentence that r6 kept from r5 now contradicts the *Unresolved* case: the P0 lead's "Only
   those preparations carry OBL-SP's open content." In the unresolved case, in-form preparations
   whose checks fail also carry open content (RC-r6-1).

2. **Alignment.**
   - The first bullet of "What P0 may settle" now requires the whole witness and gives O-U for a
     failed or unestablished check. Its second bullet is conditional on a pass. Both are aligned.
   - The ordering rule handles a full pass, the out-of-form case and the unresolved case, and does
     not hand Q4 on in the unresolved case. One gap remains: when P0 finds both out-of-form
     preparations and in-form preparations with failed checks, "continues on those alone" treats the
     in-form part as settled (RC-r6-2).

3. **Scope of the diff.** Apart from the §4 edits above, r5→r6 differs only in the "(r6)" title and
   one Revision sentence. That sentence correctly cites review 5890968976, r5 at `6de32c95`, the
   owner's decision and `REC-1-RESPONSE-r5.md`.

4. **No new overclaim.** Every edit restricts when O-C may be reported. H-xiv, the [R]/[R-off] tags,
   NL-C's form, OA-3's finite-ring scope and the off-`main` gate are unchanged.

5. **`REC-1-RESPONSE-r5.md` references.** It cites only resolvable references: the review id, the
   owner's decision as relayed, `6de32c95` and `REC-1-r5.md`. There is no external diff file. Its
   description matches the diff.

## Required changes (`REC-1-r6.md`, §4)

**RC-r6-1 (P0 lead).**
- Old: "Only those preparations carry OBL-SP's open content. P0 is posed under H-xiv."
- New: "Once the in-form preparations pass the operational witness, only those listed preparations
  carry OBL-SP's open content. P0 is posed under H-xiv."

**RC-r6-2 (ordering rule, mixed case).**
- Old: "If P0 lists preparations outside the coset form, OBL-SP continues on those alone."
- New: "If P0 lists preparations outside the coset form and the in-form preparations pass the
  operational witness, OBL-SP continues on the listed preparations alone; in-form preparations whose
  checks fail or are unestablished are O-U as well (P0)."
