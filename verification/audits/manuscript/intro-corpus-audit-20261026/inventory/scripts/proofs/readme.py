import json, sys, collections, os
P = sys.argv[1]
d = json.load(open(os.path.join(P, 'proofs.json')))
m = d['meta']
st = d['statements']
lv = collections.Counter(s['ledger']['level'] if s['ledger'] else 'no row' for s in st)
cat = collections.Counter(s['proof_location']['category'] for s in st)
by_paper = collections.Counter(s['paper'] for s in st)
src = collections.Counter(s['source'].split(' (')[0] for s in st)
pred = d['predictions']
kern = d['kernel']
ktree = collections.Counter(k['tree'] for k in kern)
kprint = collections.Counter('recorded output' if k['print_axioms'].startswith('recorded') else
                             ('#print axioms in source' if k['print_axioms'].startswith('printed') else 'no #print axioms') for k in kern)
obl = collections.Counter((o['table'], o['status']) for o in d['obligations'])
g = d['gaps']

L = []
w = L.append
w('# Proof inventory — audit step 1')
w('')
w('Companion to `proofs.json`. This file says what each source contributed, lists the gaps, records early cross-consistency signals, and gives each statement\'s proof location. It judges nothing about the Introduction.')
w('')
w('## Corpus commit and what was read where')
w('')
w('- `corpus_commit`: `%s` (main after #939, "ħ framing and the θ₀ match"). The plan names `b64919cd`; the owner asked for #939\'s corrected statements, so the inventory is taken at `eae01647`.' % m['corpus_commit'])
w('- Read at `eae01647` (read-only `git archive` extraction): every `papers/*.md` and `book/*.md`, `verification/coverage/LEDGER.json`, `verification/ROADMAP.md`, `verification/lean-manuscript-census.json`, `verification/lean/`, `verification/lean-mathlib/OIBridge*`, and the `tools/` scripts that were run.')
w('- Read from the worktree at `b64919cd`: `verification/programmes/**` (the retained `#print axioms` outputs). `.gitattributes` export-ignores that tree, and `git diff b64919cd eae01647` shows no change under it, nor under the Lean trees, `tools/`, ROADMAP or the registry.')
w('- #939 changed, among the in-scope sources: %s. Every entry drawn from these files carries `read_at.changed_by_939: true`.' % ', '.join('`%s`' % f for f in m['files_changed_by_939_in_scope']))
w('')
w('## What each source contributed')
w('')
w('| Source | Contribution | Count |')
w('|---|---|---|')
w('| `tools/proof_census.py --json` | displayed statements in the seven core papers (bold head at line start) | %d (Main 46, SM 39, GR 20, Structure 12, Substratum 5, Methodology 0, Juno 0) |' % src['proof_census'])
w('| manual scan of the core papers | displayed statements the census regex does not match (lower-case "theorem", italic heads, inline bold heads, Markdown headings, the two axioms) | %d |' % (len(st) - src['proof_census']))
w('| `verification/coverage/LEDGER.json` | level, checks, delta, assumptions for each census row | %d core rows: %s |' % (sum(v for k, v in lv.items() if k != 'no row'), ', '.join('%s %d' % (k, v) for k, v in sorted(lv.items()) if k != 'no row')))
w('| `verification/lean-manuscript-census.json` | kernel families and anchors; supersessions | 111 families, 16 supersessions; `tools/lean_manuscript_census.py` OK |')
w('| Lean trees (`verification/lean-mathlib/OIBridge`, `verification/lean`) | cited `theorem`/`lemma` declarations, module:line, `#print axioms` status | %d declarations (OIBridge %d, lean %d) |' % (len(kern), ktree['OIBridge'], ktree['lean']))
w('| `verification/ROADMAP.md` | obligations and their status | %d rows: %s |' % (len(d['obligations']), '; '.join('%s %s ×%d' % (t, s, n) for (t, s), n in sorted(obl.items()))))
w('| `book/appendix-a-prediction-status.md` | prediction rows with class, layer, value, match | %d rows (A.4.1 %d, A.4.2 %d, A.4.3 %d, A.4.4 %d, A.5 %d) |' % (
    len(pred['rows']), *[pred['computed_counts'][k]['rows'] for k in sorted(pred['computed_counts'])]))
w('| `book/appendix-b-derivations.md` | displayed derivations, each paired with its paper statement where one exists | %d statements, %d paired |' % (
    len(d['appendix_b_statements']), sum(1 for b in d['appendix_b_statements'] if b['paper_twin'].get('id') or b['paper_twin'].get('paper'))))
w('| manuscripts and ROADMAP | named hypotheses and premises with definition site, status and users | %d named hypotheses + the twelve-item posit ledger (Main §4.5) |' % len(d['hypotheses']))
w('')
w('Appendix A\'s stated counts agree with the rows recounted from its tables: A.4.1 3 S + 7 C + 8 L + 1 M + 2 R + 2 E = 23; A.4.2 6 C + 2 L = 8; A.4.3 1 S + 1 C + 5 L = 7; A.4.4 12 S + 2 C = 14. SM §7.6 recounts to 22 rows = 2 S + 5 C + 6 L + 3 R + 2 E + 3 M + 1 P, matching its "2 structural + 5 conditional structural" summary. Count differences between documents are listed under signal S9.')
w('')
w('Kernel `#print axioms` status of the %d cited declarations: %s. No cited declaration has a retained output in the repository; the retained outputs (88 declarations, all within {propext, Classical.choice, Quot.sound}) belong to research rounds the manuscripts do not cite. A `#print axioms` line in `OIBridge` is gated by `tools/lean_axiom_check.py`, which fails the build on any other axiom or `sorryAx`. No `axiom`, `sorry` or `native_decide` occurs in either tree.' % (len(kern), ', '.join('%s %d' % kv for kv in kprint.items())))
w('')
w('## Gaps')
w('')
w('1. **Statements with no ledger row: %d.** All are displayed statements the census regex does not recognise. The most consequential is Main\'s **Characterization theorem** (`papers/Main.md:516`, proof at `:608`), the central equivalence of the corpus. The others:' % len(g['statements_without_ledger_row']))
for x in g['statements_without_ledger_row']:
    w('   - `%s:%d` %s %s — %s' % (x['paper'], x['line'], x['kind'], x['label'], x['why'].replace('supplementary (not recognised by tools/proof_census.py: ', '').rstrip(')')))
w('2. **Ledger rows whose paper line has moved: %d** (%d in the core papers; 4 in Explainer). Fingerprints all match, so the mapped text is current; only the recorded `line` is stale. Affected: every GR row from Bohr-frequency completeness onward and every SM row from the area-law lemma to Theorem 22 and its corollary. Each statement entry carries `ledger.line_moved`.' % (len(g['ledger_rows_with_moved_line']), sum(1 for x in g['ledger_rows_with_moved_line'] if x['core'])))
w('3. **Hypotheses used but never stated in a manuscript:** %s. All are named only in verification records (ledger backlog notes, a ROADMAP row, or an ASCII spelling of H-χ\'). Every named hypothesis that a manuscript uses has a definition site in the corpus.' % ', '.join(x['name'] for x in g['hypotheses_used_but_never_stated_in_manuscripts']))
w('4. **Defined hypotheses that no displayed statement names:** %s. They condition prose results or prediction rows (strong CP, the native hypercharge reading of 1/α₀, the ħ calibration split, Condition 2), not bold-headed statements.' % ', '.join(g['hypotheses_defined_but_not_named_in_any_displayed_statement']))
w('5. **Kernel anchors that do not resolve: none.** Every `(kernel: …)` citation, every registry anchor identifier and every ledger Lean check resolves to a declaration. `tools/lean_manuscript_census.py` passes at `eae01647`.')
w('6. **Cited kernel declarations with no `#print axioms` anywhere: %d** — %s.' % (len(g['cited_kernel_declarations_without_print_axioms']), '; '.join('`%s`' % x for x in g['cited_kernel_declarations_without_print_axioms'])))
w('7. **Statements with no proof, or with a proof the paper says is not written: %d.**' % len(g['statements_with_no_proof_located']))
for x in g['statements_with_no_proof_located']:
    w('   - `%s:%d` %s — %s' % (x['paper'], x['line'], x['label'] or x['id'], x['where']))
w('8. Methodology and Juno carry no census statements. Methodology\'s axioms and its §5.5 no-go are indexed as supplementary rows; Juno states its results in prose and tables, which enter through the predictions section.')
w('9. Five Appendix B derivations have no displayed paper twin: B.4.1, B.4.2, B.6c.1, B.7.2, B.7.5b (see `appendix_b_statements[].paper_twin.note`).')
w('')
w('## Early cross-consistency signals')
w('')
w('Listed, not resolved. Each gives its sites; the anchor and the resolution belong to step 4.')
w('')
for s in d['consistency_signals']:
    w('- **%s — %s.** %s Sites: %s.' % (s['id'], s['topic'], s['detail'], '; '.join('`%s`' % x for x in s['sites'])))
w('')
w('## Proof location of every statement')
w('')
w('Two cases are kept apart, as the owner asked: a proof that is **missing** (`none-located`, or `not-written` where the paper says so) and a proof that **lives outside the statement\'s paper** (`companion-paper`, `book-appendix`, `kernel-only`, `external-literature`). For a statement in Main, a proof in GR, SM, Substratum, Structure, Methodology, Appendix B or the kernel is support, not a gap. Categories: %s.' % ', '.join('%s %d' % kv for kv in cat.most_common()))
w('')
w('| Paper:line | Kind | Label / ledger id | Ledger | Proof location |')
w('|---|---|---|---|---|')
for s in st:
    lab = (s['label'] or '').replace('|', '\\|')
    ident = s['id'] or 'no ledger row'
    where = s['proof_location']['where'].replace('|', '\\|')
    w('| `%s:%d` | %s | %s (`%s`) | %s | **%s** — %s |' % (s['paper'], s['line'], s['kind'], lab[:70], ident, s['ledger']['level'] if s['ledger'] else '—', s['proof_location']['category'], where))
w('')
w('## Method notes')
w('')
for x in m['method_notes']:
    w('- ' + x)
w('- The scripts that built `proofs.json` are in `scripts/proofs/`. They read the extracted tree and write nothing else.')
open(os.path.join(P, 'PROOFS-README.md'), 'w').write('\n'.join(L) + '\n')
print(len(L))
