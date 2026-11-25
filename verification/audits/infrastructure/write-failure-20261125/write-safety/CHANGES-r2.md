# Revision r2 of PR #1566 and gate v2: review findings and changes

Review: PR #1566 comment 7166798215 (head ae0da5d8, gate v2 f6312d5c). Owner decision (amaybaum,
2026-11-25): "Correct the containment policy and gate v2's missing run-level stop.", clarified:
"Distinguish two types of containment: * Run-level containment: after an integrity mismatch, the
current automated write sequence must stop completely. Catching an exception must not allow further
writes in that sequence. * Operation-level containment: subsequent independent operations may
continue through validated mechanisms if the evidence supports isolating the defect."

Local revision only: no GitHub write, network write, commit or push. `gate.py`, `mock.py`,
`test_gate.py`, `countercontrol.py` and `mock2.py` are unchanged. "AGENTS.md" below is the PR's
amended copy.

| Finding | Change |
|---|---|
| R1 (rule 3 not decidable, fail-open) | Rule 3 rewritten: the sequence always ends; every automated GitHub text write, for every agent and session, stops by default; narrowed to the failed operation only when four mechanically decided conditions all hold (outcome known; read-back succeeded with no unsent-field, label or state failure; every rejected difference wholly in the trailing tail after the last character of the sent content, defined as the text sent less the newlines and any footer at its very end, not empty and stored unchanged as the start of the stored text; no other operation's mismatch outstanding, defined as not yet resolved by a recorded owner decision). "Sequence" defined as the writes of one run of a writer process or of a plan. |
| R2 (gate: unknown outcome and content change contained to the operation) | `gate2` writes the global marker for every failure except a read-back mismatch meeting all four conditions (`_containment_scope`, `transport_rules.tail_confined`). Tests `q1` (TimeoutError: global), `q2` (0.3 to 0.4: global), `q5`, `q6`; C3 mutant `operation_scope_always` (the pre-r2 containment) fails 25 tests. |
| R3 (no run-level latch) | `Gate2` latches on every `Halted` and every other exception during a write or push; the instance and every `Gate2` in the process then refuse every write and push before any request. No API clears it. Tests `c1`, `c3`, `q3` (loop catching `Halted`, gate reused or per item, operation-level or global: 1 write, then none), `q7`; C3 mutant `no_run_level_latch` fails `c1`, `c3`, `q3`. The former "comment still writable in the same gate" assertions are replaced. |
| R4 (§A.51 item 5 still stops the package on any failed read-back) | Item 5 amended: its first sentence now names a failed preflight or push read-back (item 3); a §A.49 mismatch, a failed text read-back included, stops the package's operations and every automated text write as rule 3 provides, unless rule 3 confines it, in which case the sequence still ends, the operation is suspended and the package's other operations may continue in a later sequence through validated mechanisms. Needs owner confirmation (it narrows the package stop for confined mismatches). |
| R5 (adoption lines) | The §A.49 adoption line's two 2026-11-25 dates replaced by "[date of merge]" and "[merge approval record]", to be filled at merge; §A.51's adoption line gains an item 5 entry in the same form. |
| R6 (a) | Rule 2: "in the body of an Issue, a pull request or a comment only, never in a title, a review or a review comment". The gate has no review operation, so its field-based scope (`body`) coincides. |
| R6 (b) | Rule 2: "once at the very end of the stored text and not repeated there". |
| R6 (c) | Rule 2: "after content that is not empty", matching the code's rejection of a footer on empty content. |
| R6 (d) | Rule 2: the allowlist is "stated in this rule"; "This text is authoritative: a registry in code that applies the allowlist lists the same entries with the same effect, and where the two differ this text governs." No mechanical check between the two is added (AGENTS.md is not in this tree). |
| R7 (unclosed blocks) | Rule 2 states the limit (fenced code, HTML `<pre>`, `<textarea>`, comment, math block); PROTOCOL-v2 §3 likewise. |
| R8 (orphaned record) | All fields and checks are evaluated first; records are written only after all pass. Test `q4` (body permitted, title altered: no record, global or operation scope as the title change decides). A record-write failure halts globally and names records already written. |
| R9 (residual risk) | Bounded as the review proposed: operation-level containment applies only to tail-confined differences; any change before the end of the content is global. Local-file markers and non-atomic check-and-write are stated as limits in PROTOCOL-v2 §5. |
| R10 (ordering) | Rule 3: "Before any later sequence writes, the text sent and the text stored are kept as evidence under §A.26 and the owner is told, through a channel other than an automated GitHub write." `gate2`: while any `HALT.<operation>` lacks `HALT.<operation>.notified` (created by hand, never by the gate), every later sequence refuses every write (tests `c1b`, every operation-level negative control). |
| Nit: "for every agent and session" | Said explicitly for the default stop. |
| Nit: PROTOCOL-v2 §5 wording | §5 rewritten to the amended rule 3; §8 quotes the draft's rule 2, rule 3 and §A.51 item 5 verbatim. |
| Nit: durable evidence destination | PROTOCOL-v2 §4: the evidence directory must be durable; records and halt evidence are copied to the evidence branch under §A.26 and §A.42. |
| Nit: best-effort evidence files | The marker embeds every evidence text (test `q8`). |
| Nit: non-atomic marker check | Stated in `gate2.py`'s docstring and PROTOCOL-v2 §5. |
| Answer 1 nit (does "permitted" pass "exact read-back" for §A.51 item 2 validation?) | Not changed: an owner decision. |
| Answer 3 (operation boundary) | Rule 3 gives one example each of tool (`gh api`), path (`PATCH /repos/{owner}/{repo}/issues/{number}`) and kind of write (a body edit, distinct from closing an Issue through the same endpoint). |
| Answers 2, 4, 5 | Covered by R3, R1, R4 and R5. |

## Other behaviour changes in gate2

- Pre-write refusals (pre-check, grant, fields), failed read-back, bad status, push failures and
  unknown operations write the global marker, where r1 wrote an operation marker. A pre-existing
  operation marker refuses that operation and ends the sequence.
- Halt evidence keys are `<field>.sent`, `<field>.stored`, `<field>.diff` (and
  `unsent-<field>.before` and `.stored`), covering every failing field of a write.

## Results

`test_gate2.py` 49 tests pass; `test_gate.py` 18 pass; `countercontrol.py` and `countercontrol2.py`
pass (C2: 5/5/3/7/3/2 failures; C3: 20/1/11/3/25/13). Recorded in `results-tests2.txt` and
`results-countercontrol2.json`.

## Not updated (outside the files this revision may change)

`../SHA256SUMS` and `../README.md` describe r1 (README: "halts the failed operation only"; the
digests of the six changed files). They need regenerating with this revision.
