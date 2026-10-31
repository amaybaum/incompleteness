import json, sys, os, collections
S = sys.argv[1]; OUTDIR = sys.argv[2]; FULL = sys.argv[3]
d = json.load(open(os.path.join(S, 'work', 'proofs_draft.json')))
ledger = json.load(open('verification/coverage/LEDGER.json'))
census = json.load(open(os.path.join(S, 'census.json')))
cen = {r['id']: r for r in census}
CORE = ('papers/Main.md', 'papers/GR.md', 'papers/SM.md', 'papers/Substratum.md', 'papers/Structure.md',
        'papers/Methodology.md', 'papers/Juno.md')

moved = [{'id': e['id'], 'ledger_line': e['line'], 'census_line': cen[e['id']]['line'], 'core': e['paper'] in CORE}
         for e in ledger['entries'] if cen[e['id']]['line'] != e['line']]
no_ledger = [{'paper': s['paper'], 'line': s['line'], 'kind': s['kind'], 'label': s['label'], 'why': s['source']}
             for s in d['statements'] if s['ledger'] is None]

signals = [
 {'id': 'S1', 'topic': 'Characterization theorem has no census/ledger row',
  'sites': ['papers/Main.md:516', 'book/appendix-b-derivations.md:454'],
  'detail': 'Main\'s "**Characterization theorem.**" (lower-case "theorem") is not matched by tools/proof_census.py (regex requires "**Theorem"), so the central equivalence has no LEDGER row; its supporting theorems (MAIN:T-finite-horizon-stochastic-reversible-unitary K3, MAIN:T-finite-horizon-process-dilation, MAIN:T-unavoidable-hidden-predictive-memory) do. Proof at papers/Main.md:608; the (ii)⟹(i) direction is imported under (T).'},
 {'id': 'S2', 'topic': 'D-gauge completeness: H-BG premise status',
  'sites': ['papers/GR.md:178', 'papers/GR.md:182', 'book/appendix-b-derivations.md:426', 'book/appendix-b-derivations.md:444', 'verification/ROADMAP.md:1139', 'LEDGER GR:T-d-gauge-completeness-two-branch (K1)'],
  'detail': 'The theorem and book Lemma B.7.5 / Theorem B.7.5c are conditional on H-BG (global sign-aware classification). The kernel\'s unsigned premise BGIntegerClassification is refuted (GR:182, ROADMAP P2, ledger delta); kernel coverage is K1 (subresults only); the sign-aware replacement and its comparison with Bekir–Golomb are open. GR states this; the book Lemma B.7.5 states the phase-locking determination "up to the lemma\'s full gauge" under H-BG — check that every restatement (Main phase-locking, Appendix B) carries the open status, not only the hypothesis name.'},
 {'id': 'S3', 'topic': 'Appendix B restatements that differ in scope or kind from the paper statement',
  'sites': ['book/appendix-b-derivations.md:92 vs papers/Main.md:326', 'book/appendix-b-derivations.md:302 vs papers/SM.md:372',
            'book/appendix-b-derivations.md:408 vs papers/Main.md:86', 'book/appendix-b-derivations.md:341 vs papers/SM.md:388',
            'book/appendix-b-derivations.md:294 vs papers/SM.md:364'],
  'detail': 'B.2.5 states CP-indivisibility "of the substratum dynamics (under C1–C4)"; Main states it "for the permutation-dilation family" (Main status ledger: fails for general CPTP families). B.6.2 states 6 = 3⊕2⊕1 for "the internal components" without the H-link qualifier that SM Theorem 7 attaches to the physical reading. B.7.1 "Partition relativity" is a different statement from Main\'s Lemma of that name (the canonical-measure uniqueness claim). B.6b.1 is a Lemma with a narrower content than SM Theorem 7b (no Cabibbo-uniqueness clause); B.6.1 is a Proposition, SM 6 a Theorem.'},
 {'id': 'S4', 'topic': 'Appendix A empirical-match cells vs SM/ch06 numbers',
  'sites': ['book/appendix-a-prediction-status.md:75 (row 6)', 'book/appendix-a-prediction-status.md:82 (row 13)', 'book/appendix-a-prediction-status.md:128 (N2)',
            'book/appendix-a-prediction-status.md:90 (row 21)', 'papers/SM.md:1261-1279', 'book/ch06-matter-content.md:298-312'],
  'detail': 'Row 6 Wolfenstein A "Within 1%" — SM/ch06 give 0.8165 vs 0.826 (1.2%, 0.8σ). Rows 13/N2 sin²θ13 "Within 1%" — SM/ch06/Juno give 0.02252 vs 0.02195±0.00056 (≈2.6%, 1.01σ). Row 21 m_b via Q_down "Within 1σ" — SM/ch06 give 4144 vs 4180±30 MeV (0.9%, i.e. 1.2σ by the quoted error). Row 1 1/α0 "Within ~0.5%" — ch06 §6.8 lists it as a structural input with no observed value; SM treats its native hypercharge reading as conditional on H-observer-bundle and H-Y-vertex.'},
 {'id': 'S5', 'topic': 'Wolfenstein A sigma in Juno',
  'sites': ['papers/Juno.md:140', 'papers/SM.md:1263', 'book/ch06-matter-content.md:298'],
  'detail': 'Juno: √(2/3) agrees with A = 0.826 ± 0.012 "at 0.23σ"; SM §7.6 gives 0.8σ (arithmetic (0.826−0.8165)/0.012 ≈ 0.79σ).'},
 {'id': 'S6', 'topic': 'sin²θ13 status in Juno',
  'sites': ['papers/Juno.md:346', 'papers/Juno.md:395', 'papers/SM.md:1276', 'book/appendix-a-prediction-status.md:82'],
  'detail': 'Juno §5.1: "The formula for sin²θ₁₃ is fully derived"; Juno §6 and SM/appendix A classify it C (conditional on the emergent dressing of the Cabibbo identification).'},
 {'id': 'S7', 'topic': 'Internal SM numerical tables disagree',
  'sites': ['papers/SM.md:1316-1317', 'papers/SM.md:1263', 'papers/SM.md:1276', 'papers/SM.md:983-984', 'papers/SM.md:948-949'],
  'detail': 'SM:1317 compares sin²θ13 0.0225 with 0.0224 (0.4%) while SM:1276 uses 0.02195±0.00056 (1.01σ). SM:1316 lists A² = 0.6667 vs 0.683 as 1.2% (the A-level deviation; the A² deviation is ≈2.4%). SM:983-984 give m_e, m_μ at 1.2% (0.505, 104.4 MeV) beside SM:948-949 at 0.003%/0.002% — different constructions in different tables; labels should make the difference explicit.'},
 {'id': 'S8', 'topic': 'm_μ in ch06 vs SM',
  'sites': ['book/ch06-matter-content.md:190', 'book/ch06-matter-content.md:305', 'papers/SM.md:949', 'papers/SM.md:1270'],
  'detail': 'ch06:190 gives m_μ = 105.74 MeV (0.08%) via "Koide closure with the structural m_e/m_τ = 1/(36π⁴)"; ch06 §6.8 (:305) and SM (:949, :1270) give 105.656 MeV (0.002%) from (Q, θ0; m_τ). Same chapter, two values; the SM counterpart table (:948) has only the second.'},
 {'id': 'S9', 'topic': 'Prediction inventories and counts',
  'sites': ['book/appendix-a-prediction-status.md:8', 'book/appendix-a-prediction-status.md:94', 'papers/SM.md:1255', 'papers/SM.md:1298-1300',
            'book/ch06-matter-content.md:12', 'book/ch06-matter-content.md:289-314', 'book/ch07-gravity.md:292-303', 'book/ch07-gravity.md:321'],
  'detail': 'SM §7.6: 22 rows = 2 S + 5 C + 6 L + 3 R + 2 E + 3 M + 1 P (rows recounted). Appendix A A.4.1: 23 rows = 3 S + 7 C + 8 L + 1 M + 2 R + 2 E (recounted; matches its stated count) — explained in-text as broader than SM\'s table (adds 1/α0, A·B, MOND a0, neutrino rows). ch06:12 says §6.8 "collects the twenty-two predictions" but the §6.8 table has 24 rows with a different row set (adds 1/α0, δ0, A·B, θ̄, m_d, m_u; omits α1(M_Z), Q_down, m_b/m_τ, m_u/m_d). ch07:321 counts "the ten entries in this chapter\'s table" while appendix A, preface, ch08, ch09, ch18, ch19 count "eight gravitational-sector entries" — two different gravitational inventories. Headline "twenty-two SM observables, two S and five C" is uniform across SM, Substratum, Structure, the book and FULL (FULL mirrors every chapter verbatim).'},
 {'id': 'S10', 'topic': 'Bijectivity: lemma or part-empirical',
  'sites': ['papers/Methodology.md:235', 'papers/Methodology.md:253', 'papers/Methodology.md:146', 'papers/Main.md:708'],
  'detail': 'Methodology §5.5 and §6.1 list determinism and bijectivity among the rungs that "follow as lemmas"; Methodology §4.4 and Main\'s posit ledger (iii) say the hidden-sector margin is closed with one empirical input, so bijectivity is part-empirical. The qualifier is present at the derivation and absent from the summary statements.'},
 {'id': 'S11', 'topic': 'GR universality theorem without a written proof',
  'sites': ['papers/GR.md:675-679'],
  'detail': 'The "Theorem (universality of the partition-geometry results)" is displayed as a theorem; GR:679 says the theorem-style proof "has not been written out in this paper" and the claim is "established at that level" (the §3–§6 derivations). Ledger GAP.'},
 {'id': 'S12', 'topic': 'Label collisions',
  'sites': ['papers/Main.md:224 (G1)–(G3) genericity', 'papers/GR.md:12 G1–G3 gravity levels', 'papers/Juno.md:225 Condition 1/2', 'papers/SM.md:1046 Cond 2'],
  'detail': 'G1–G3 name both Main\'s phase-locking genericity conditions and GR\'s gravity levels. "Condition 2" (Juno) and "Cond 2" (SM) are the same relation under two spellings; Juno\'s Condition 1 has no SM counterpart name.'},
 {'id': 'S13', 'topic': 'Hypotheses named only in verification records',
  'sites': ['verification/coverage/LEDGER.json backlog[0].route', 'verification/ROADMAP.md P1 H-∞'],
  'detail': "H-functor, H-tensor, H-pure-seed, H-readout, H-monoidal (ledger backlog development notes) and H-∞ (ROADMAP obligation) are not stated in any manuscript; the ledger also spells H-χ' as H-chi'."},
]

kernel_noprint = [k for k in d['kernel'] if k['print_axioms'].startswith('no #print')]
gaps = {
 'statements_without_ledger_row': no_ledger,
 'ledger_rows_with_moved_line': moved,
 'ledger_rows_with_stale_fingerprint': [],
 'hypotheses_used_but_never_stated_in_manuscripts': d['named_only_outside_manuscripts'],
 'hypotheses_defined_but_not_named_in_any_displayed_statement': [h['name'] for h in d['hypotheses'] if h['used_by_count'] == 0],
 'kernel_anchor_resolution': {'unresolved_manuscript_kernel_citations': d['diag']['unresolved_kernel_citations'],
                              'unresolved_registry_anchor_identifiers': d['diag']['unresolved_registry_anchor_identifiers'],
                              'unresolved_ledger_lean_checks': d['diag']['unresolved_ledger_checks'],
                              'tools/lean_manuscript_census.py': 'OK at eae01647'},
 'cited_kernel_declarations_without_print_axioms': [k['decl'] + ' @ ' + k['location'] for k in kernel_noprint],
 'statements_with_no_proof_located': [{'paper': s['paper'], 'line': s['line'], 'label': s['label'], 'id': s['id'], 'where': s['proof_location']['where']}
                                      for s in d['statements'] if s['proof_location']['category'] in ('none-located', 'not-written')],
}

meta = {
 'audit_step': 1, 'artifact': 'proof inventory',
 'corpus_commit': FULL,
 'plan_corpus_commit': 'b64919cdae300c787ff51c8c9bf0355ed6dc1c0e',
 'read_at': {
   FULL: 'every manuscript (papers/*.md, book/*.md), verification/coverage/LEDGER.json, verification/ROADMAP.md, verification/lean-manuscript-census.json, both Lean trees and tools/*.py were read from a read-only extraction of eae01647 (git archive)',
   'b64919cdae300c787ff51c8c9bf0355ed6dc1c0e (worktree)': 'verification/programmes/** (retained #print axioms outputs) — export-ignored by .gitattributes, so read from the worktree; git diff b64919cd eae01647 shows no change under verification/programmes, verification/lean*, tools, ROADMAP or the registry',
 },
 'files_changed_by_939_in_scope': sorted(p for p in sys.argv[4].split(',') if p.endswith(('.md', '.json')) and not p.startswith('verification/audits/')),
 'tools_run': ['python3 -I tools/proof_census.py --json', 'python3 -I tools/lean_manuscript_census.py (OK)',
               'ledger/census comparison (completeness and fingerprints: OK; line numbers: see gaps)'],
 'method_notes': [
   'statements: tools/proof_census.py rows for the seven core papers, plus supplementary displayed statements the census regex does not see (source field says why)',
   'hypotheses_as_stated: clauses of the statement text beginning Let/Assume/Suppose/Under/If/Given/Fix/For every, or containing conditional on/under/assuming (extracted mechanically, up to six)',
   'named_hypotheses: named tokens found in the statement text or in the ledger assumptions field; ranges (A1–A6, (C1)–(C4), E1–E7, S1–S4) are expanded',
   'kernel_anchors: ledger lean checks resolved to module:declaration; (kernel: …) citations within the statement span; registry families whose anchor text lies in the span',
   'proof_location.category: inline-proof / inline-proof-sketch (a *Proof* block under the statement), inline-argument (argument in the statement paragraph or adjacent prose, no proof block), elsewhere-in-paper, companion-paper, book-appendix, kernel-only, external-literature, no-proof-obligation (definition, axiom, summary), not-written (the paper says the proof is not written out), none-located',
   'kernel: theorem/lemma declarations cited by a manuscript (any backticked identifier that resolves, and (kernel: …) groups), by the registry (anchors, supersessions) or by a ledger check; print_axioms reports #print axioms sites and any retained output',
 ],
}

out = {'meta': meta, 'statements': d['statements'], 'appendix_b_statements': d['appendix_b_statements'],
       'hypotheses': d['hypotheses'], 'posit_ledger': d['posit_ledger'],
       'obligations': d['obligations'], 'roadmap_not_prioritized': d['roadmap_not_prioritized'],
       'roadmap_declared_inputs_section': d['roadmap_declared_inputs_section'],
       'predictions': d['predictions'], 'kernel': d['kernel'], 'gaps': gaps, 'consistency_signals': signals}
os.makedirs(OUTDIR, exist_ok=True)
json.dump(out, open(os.path.join(OUTDIR, 'proofs.json'), 'w'), ensure_ascii=False, indent=1)
c = collections.Counter(s['proof_location']['category'] for s in d['statements'])
print('statements', len(d['statements']), 'no-ledger', len(no_ledger), 'moved', len(moved), sum(m['core'] for m in moved))
print(c)
print('kernel', len(d['kernel']), 'noprint', len(kernel_noprint))
