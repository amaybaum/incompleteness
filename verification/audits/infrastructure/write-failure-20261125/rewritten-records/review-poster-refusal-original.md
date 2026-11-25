Verdict: ACCEPT WITH NITS. Nothing blocking.

I ran everything on copies in a new review directory. The files under review are unchanged: the post.py hashes match the original. I made no gh, network or git writes.

Findings

1. **The diff adds only the refusal (check 1).** The diff from post.py.pre-ltbang to post.py is one added block: `if '<!' in body:`, then a printed REFUSED message and `sys.exit(4)`. It sits after the existing checks (halt marker, footer form, character precheck, long link, oi- form). It runs before `find_existing()`, so it comes before the pre-write listing, the POST and the read-back.
   - It never changes `body`: no escaping, no substitution.
   - The message says what was found, where (character offset and a short excerpt), that nothing was sent, and that the writer must reword so no '<' is immediately followed by '!'.
   - It does not call `die()`, so it writes no halt marker.

   Not halting here fits the owner decision. The decision asks for rejection, an explanation and rewording by the writer, and does not ask for a halt. A refusal sends nothing, so there is no write of unknown outcome to stop on. Nothing earlier is weakened: every earlier check comes first and still halts with exit 3 and a marker. A body that fails the precheck (for example, it contains the at-sign) and also contains '<!' halts on the precheck. A body without the footer halts on the footer check. An existing marker still exits 3 before the new check runs.

2. **The read-back and all earlier checks are unchanged (check 2).** The diff touches no other line. The exact read-back is still byte-for-byte with no normalization, and still halts with MISMATCH.

3. **Controls (check 3).**
   - Against post.py: 11/11 PASS.
   - Against post.py.pre-ltbang: 8/11. The three new refusal controls fail as they should: two post and read back "OK", and the strip_lt_bang case halts on MISMATCH. So the negative control works, and the strip_lt_bang case also shows the read-back still catches the alteration seen on GitHub. The positive control (`< !b`, `x<y!`) posts normally on both versions.
   - Fake gh diff: it adds only the call counter (incremented when gh starts) and the strip_lt_bang mode. I re-ran all 11 cases against post.py with the previous gh.bak, and the seven earlier cases give the same results (codes and output) as with the new gh.

4. **Nit: the zero-call assertions can pass with no counter at all.** The checks read `s.get('calls',0)==0`, and the state file starts with no `calls` key. With a gh that has no counter, those checks pass anyway: with gh.bak, all 11 still PASS against post.py, including existing_marker. The shipped gh does count (3 calls on a normal post), so the controls hold as delivered. To make them independent of that, initialise `calls: 0` in the state and add an assertion that the ok case records exactly 3 calls.

5. **Probes of the refusal (check 4, report only).** Each refused probe ended with exit 4, zero gh calls, no posts and no marker:
   - '<!' at the very start: refused.
   - '<!' at the end just before the footer: refused.
   - '<!' inside a fenced code block: refused.
   - '<!' between Greek and accented letters: refused.

   These go through and post normally, which is correct under the rule as authorized:
   - '<' followed by U+01C3 or by U+FF01;
   - fullwidth U+FF1C followed by '!';
   - '<', a newline, then '!';
   - `&lt;!`;
   - `<?`;
   - `!<`.

   There is no evidence that GitHub alters any of these. A '<!' split by a zero-width character is already halted by the existing precheck. If the alteration comes from HTML-like parsing of '<!', other markup openers such as `<?` or `</` might also be at risk. That is untested and outside the authorized rule; it is reported only.

6. **Titles (check 5).** post.py only creates issue comments: it POSTs to `issues/{n}/comments` with a JSON object holding only `body`. Comments have no title, so there is no title to check here. If the rule is ever applied to Issue or pull-request writes, their titles would need the same check.

7. **Minor:** the reported offset counts code points, not bytes. That is fine and readable.