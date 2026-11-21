# REC-1 r7: focused confirmation

**Object.** Draft PR #1268 at exact head `f0757fdbe4b6bfb110a8160a8f6c66f74eff1d33`, a single child of
`1ab6371b`. The commit adds `REC-1-r7.md`, `REC-1-RESPONSE-r6.md` and `REC-1-CONFIRM-r6.md`; no
other file changes. I diffed `REC-1-r6.md` against `REC-1-r7.md` myself, read-only.

## Verdict: **CONFIRMED** (no further changes required)

1. **RC-r6-1 and RC-r6-2 are applied exactly.** The P0 lead sentence and the mixed-case sentence of
   the ordering rule carry my new texts verbatim.
2. **Scope of the diff.** r6→r7 differs only by those two sentences, the "(r7)" title and one
   Revision sentence. The Revision sentence cites RC-r6-1 and RC-r6-2, r6 at `1ab6371b` and
   `REC-1-RESPONSE-r6.md`.
3. **The three-way P0 rule is consistent everywhere in §4:**
   - **P0 lead:** open content rests only on the listed preparations, and only once the in-form
     preparations pass.
   - **P0 outcomes:** Pass requires the whole operational witness; Out of form lists the
     preparations and continues on them; Unresolved is O-U unless an independent classicality proof
     or a contextual counterexample is supplied.
   - **"What P0 may settle":** a pass needs the whole witness; a coset form with a failed or
     unestablished check gives O-U; the residual applies only after a pass.
   - **Ordering rule:** a full pass hands Q4 to AW-OA2-1; the out-of-form case continues OBL-SP only
     if the in-form preparations pass; in-form preparations with failed or unestablished checks are
     O-U; the unresolved case does not hand Q4 on.

   No passage reports O-C from the coset form alone, and none treats a failed check as a
   non-classical witness.
4. **`REC-1-CONFIRM-r6.md` is byte-identical** to my `CONFIRM-r6.md` (`cmp`).
5. **No new overclaim.** Both edits narrow when content counts as settled. `REC-1-RESPONSE-r6.md`
   cites only resolvable references (`1ab6371b`, `REC-1-r6.md`, `REC-1-RESPONSE-r6.md`) and describes
   the change accurately.
