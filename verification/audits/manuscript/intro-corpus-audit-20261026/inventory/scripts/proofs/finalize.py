"""Assemble inventory/proofs.json (audit step 1). Run with cwd = extracted eae01647 tree."""
import json, re, os, sys, glob, difflib
from collections import defaultdict, Counter

W = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
sys.path.insert(0, W)
from proof_overrides import O

CORPUS = 'eae01647d'  # replaced below by full sha
FULLSHA = sys.argv[2]
BASE = 'b64919cdae300c787ff51c8c9bf0355ed6dc1c0e'
CHANGED_939 = set(sys.argv[3].split(','))
CORE = ['Main', 'GR', 'SM', 'Substratum', 'Structure', 'Methodology', 'Juno']

d = json.load(open(os.path.join(W, 'stmts.json')))
statements = d['statements']


def read_at(path):
    return {'commit': FULLSHA, 'changed_by_939': path in CHANGED_939}


# ------------------------------------------------------------------ statements: proof location
for s in statements:
    paper = os.path.splitext(os.path.basename(s['paper']))[0]
    pl = s['proof_location']
    key = None
    for (p, ln, lab), v in O.items():
        if p == paper and ln == s['line'] and (s['label'] or '').startswith(lab) or (p == paper and ln == s['line'] and lab == '' and not s['label']):
            key = (p, ln, lab)
            break
    if key is None and pl['inline_proof_line'] is None:
        for (p, ln, lab), v in O.items():
            if p == paper and ln == s['line']:
                key = (p, ln, lab)
                break
    if key:
        cat, where = O[key]
    elif pl['inline_proof_line']:
        ln = pl['inline_proof_line']
        line = open(s['paper'], encoding='utf-8').read().split('\n')[ln - 1]
        m = re.search(r'\*((?:Conditional p|P)roof[^*]{0,60})\*', line)
        lab = m.group(1).strip(' .') if m else 'Proof'
        cat = 'inline-proof' if lab in ('Proof', 'Conditional proof') or lab.startswith('Proof (') or lab.startswith('Proof,') else 'inline-proof-sketch'
        where = '%s at %s:%d' % (lab, s['paper'], ln)
    else:
        cat, where = 'none-located', 'no proof block found and no manual classification (check)'
    s['proof_location'] = {
        'category': cat,
        'where': where,
        'proof_outside_this_paper': cat in ('companion-paper', 'book-appendix', 'kernel-only', 'external-literature') or 'outside Main' in where,
        'inline_proof_line': pl['inline_proof_line'],
        'references_near_statement': pl['references_in_statement_and_following_paragraph'],
    }
    s['read_at'] = read_at(s['paper'])
    if s['ledger']:
        s['ledger']['read_at'] = read_at('verification/coverage/LEDGER.json')

# ------------------------------------------------------------------ appendix B pairing
PAIR = {  # appendix-b label prefix -> (paper, line-pattern label)
    'Lemma B.2.1': ('Main', '(permutation unitarity)'), 'Lemma B.2.2': ('Main', '(Reverse direction, scoped)'),
    'Theorem B.2.3': ('Main', '(Born-form representation of the transition probabilities)'),
    'Lemma 1 (boundary bound)': ('Main', '1 (boundary bound)'), 'Lemma 2 (channel normal form)': ('Main', '2 (channel normal form)'),
    'Theorem (separability threshold)': ('Main', '(separability threshold)'), 'Corollary 1': ('ID', 'MAIN:C-1'), 'Corollary 2': ('ID', 'MAIN:C-2'),
    'Theorem B.2.5': ('Main', '(CP-indivisibility, framework scope)'),
    'Theorem B.3.1': ('SM', 'A.1 (Period formula)'), 'Theorem B.3.2': ('SM', 'A.2 (Jordan-Chevalley decomposition)'),
    'Theorem B.3.3': ('SM', 'A.3 (q-independence of the Weil-Deligne conductor)'), 'Theorem B.3.4': ('SM', 'A.4 (Additive decomposition over gauge irreps)'),
    'Lemma B.4.1': (None, 'no displayed paper statement; GR §3.1 deep-sector / boundary-only dependence material (cf. GR Lemma (Boundary-only dependence))'),
    'Lemma B.4.2': (None, 'no displayed paper statement; GR §3 transition-probability factorization'),
    'Theorem B.5.1': ('SM', '15'), 'Corollary': ('ID', 'SM:C-unnamed-66dedb9a'),
    'Proposition B.6.1': ('SM', '6 (conditional link-carrier count)'), 'Theorem B.6.2': ('SM', '7 (exact link representation; physical reading conditional)'),
    'Lemma B.6b.1': ('SM', '7b'), 'Lemma B.6c.1': (None, 'no displayed paper statement found (SM §4.7 T1 generation assignment)'),
    'Lemma B.7.1': ('Main', '(partition-relativity under the canonical invariant measure)'),
    'Lemma B.7.2': (None, 'no displayed paper statement (Main §2.1 emergent stochasticity, prose)'),
    'Lemma B.7.3': ('Main', '(non-permutation witness)'), 'Lemma B.7.4': ('Main', '(accessible backflow from readback)'),
    'Lemma B.7.5 ': ('Main', '(phase-locking)'), 'Theorem B.7.5a': ('GR', '(Bohr-frequency completeness)'),
    'Lemma B.7.5b': (None, 'no displayed paper statement; step inside the GR D-gauge conditional proof (papers/GR.md, kernel real_to_integer_surrogate)'),
    'Theorem B.7.5c': ('GR', '(D-gauge completeness, two-branch form)'), 'Corollary B.7.5d': ('ID', 'GR:C-operational-antiunitary-invariance'),
    'Theorem B.7.6': ('Main', 'Characterization theorem'),
}
census = {r['id']: r for r in json.load(open(os.path.join(W, '..', 'census.json')))}
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'^\*\*[^*]*\*\*\s*', '', t)).strip()
appb_lines = open('book/appendix-b-derivations.md', encoding='utf-8').read().split('\n')
for b in d['appendix_b_statements']:
    lab = b['label']
    tgt = None
    for k, v in sorted(PAIR.items(), key=lambda kv: -len(kv[0])):
        if (lab + ' ').startswith(k) or lab == k.strip():
            tgt = v
            break
    full = b['statement_300']
    i = b['line']
    body = appb_lines[i - 1]
    j = i
    while j < len(appb_lines) and appb_lines[j].strip():
        body += '\n' + appb_lines[j]; j += 1
    b.pop('closest_paper_statement', None)
    if tgt and tgt[0]:
        if tgt[0] == 'ID':
            cand = [s for s in statements if s['id'] == tgt[1]]
        else:
            cand = [s for s in statements if s['paper'] == 'papers/%s.md' % tgt[0] and (s['label'] == tgt[1])]
        if cand:
            s = cand[0]
            st = census[s['id']]['statement'] if s['id'] else s['statement_300']
            ratio = difflib.SequenceMatcher(None, norm(body)[:2000], norm(st)[:2000]).ratio()
            hb, hs = set(b['named_hypotheses']), set(s['named_hypotheses'])
            b['paper_twin'] = {'id': s['id'], 'paper': s['paper'], 'line': s['line'], 'kind': s['kind'], 'label': s['label'],
                               'text_similarity': round(ratio, 3), 'kind_differs': s['kind'] != b['kind'],
                               'named_hypotheses_only_in_appendix_b': sorted(hb - hs), 'named_hypotheses_only_in_paper': sorted(hs - hb)}
        else:
            b['paper_twin'] = {'unmatched_target': tgt}
    else:
        b['paper_twin'] = {'note': tgt[1] if tgt else 'no mapping'}
    b['read_at'] = read_at('book/appendix-b-derivations.md')

# ------------------------------------------------------------------ hypotheses
SRC = ['papers/%s.md' % p for p in CORE] + ['book/appendix-a-prediction-status.md', 'book/appendix-b-derivations.md',
                                             'book/The-Incompleteness-of-Observation-FULL.md', 'verification/ROADMAP.md']
TXT = {f: open(f, encoding='utf-8').read().split('\n') for f in SRC}


def occurrences(tok):
    pat = re.compile(r'(?<![A-Za-z0-9])' + re.escape(tok) + r"(?![A-Za-z0-9'-])")
    out = {}
    for f, L in TXT.items():
        ls = [i + 1 for i, l in enumerate(L) if pat.search(l)]
        if ls:
            out[f] = {'count_lines': len(ls), 'lines': ls[:40]}
    return out


def locate(f, pat):
    for i, l in enumerate(TXT[f]):
        if re.search(pat, l):
            return '%s:%d' % (f, i + 1)
    return None


H = [
 # token, defining file, defining regex, status, status source / note
 ('H-slope', 'papers/GR.md', r'\*\*H-slope: the minimal condition', 'conditional (named state condition, not derived; the one load-bearing state condition of the ħ and 1/4 calibration)', 'GR §3.2 ("H-slope is the one load-bearing state condition: H-spectrum ⇒ H-balance ⇒ H-slope"); ROADMAP P2 "H-state / H-frame / H-slope" CONDITIONAL'),
 ('H-frame', 'papers/GR.md', r'they require H-frame \(the substrate', 'conditional (not derived)', 'GR §2 Status of ħ and the 1/4; ROADMAP P2: "H-frame is not derived"'),
 ('H-state', 'papers/GR.md', r'and H-state \(the emergent cutoff-scale modes', 'conditional (requires an additional state-selection principle; split into H-shell, H-energy, H-spectrum)', 'GR §2; ROADMAP P2'),
 ('H-shell', 'papers/GR.md', r'\*\*H-shell\*\*', 'not load-bearing for the calibration', 'GR §2 "Consequences for the named conditions"'),
 ('H-energy', 'papers/GR.md', r'\*\*H-energy\*\*', 'redundant given H-spectrum', 'GR §2 "H-energy is redundant rather than open"'),
 ('H-spectrum', 'papers/GR.md', r'\*\*H-spectrum\*\*', 'not derivable from S1–S4; stronger than the calibration needs', 'GR §2, §3.3'),
 ('H-balance', 'papers/GR.md', r'\*\*H-balance: the minimal load-bearing', 'selection condition (implied by H-spectrum, implies H-slope); not a representation theorem', 'GR §2'),
 ('H-Hawking', 'papers/GR.md', r'call them \*\*H-Hawking\*\*', 'conditional (five named conditions (i)–(v))', 'GR §8.5'),
 ('H-local-lift', 'papers/GR.md', r'\*\*H-local-lift\*\*', 'missing hypothesis (stated as not an impossibility)', 'GR Appendix-adjacent §(additive dissipators)'),
 ('H-orientation', 'papers/GR.md', r'H-orientation transport question', 'open question, not claimed (classical layer settled)', 'GR §3.3'),
 ('H-BG', 'papers/GR.md', r'Assume H-BG:', 'hypothesis of the D-gauge theorem; its unsigned formal premise BGIntegerClassification is refuted; comparison with the published Bekir–Golomb classification open', 'GR §3.3 paragraph after the theorem; ROADMAP P2 "Sign-aware integer classification" OPEN; LEDGER backlog rank 1'),
 ('H-scramble', 'papers/GR.md', r'separate condition, \*\*H-scramble\*\*', 'conditional hypothesis (equidistribution over pure states; not supplied by ergodicity)', 'GR Theorem A.8'),
 ('H-decouple', 'papers/GR.md', r'decoupling condition \*\*H-decouple\*\*', 'conditional hypothesis', 'GR Theorem A.7–A.9'),
 ('H-Bell', 'papers/Substratum.md', r'\*\*Bell–gravity compatibility hypothesis \(H-Bell\)', 'open (existence/compatibility hypothesis, not a consequence of A1–A6)', 'Substratum §3.2; ROADMAP P1 "H-Bell — composite and Bell closure" OPEN'),
 ('H-link', 'papers/SM.md', r'^\*\*H-link \(physical-carrier bridge\)', 'conditional (physical-carrier identification; geometric link decomposition unconditional)', 'SM §4.5; ROADMAP P2 "H-link" CONDITIONAL'),
 ('H-cust', 'papers/SM.md', r'\*\*H-cust\*\* denotes', 'conditional: kinetic clause a theorem at the symmetric point (Proposition 4b), condensate clause open', 'SM §4.5'),
 ('H-blind', 'papers/SM.md', r'is \*\*H-blind\*\*', 'holds at the symmetric point for the component-complete site observer; named condition for other observer classes', 'SM §1, §4.4'),
 ("H-spin'", 'papers/SM.md', r"\*\*Remark \(H-spin' — the physical spin identification", 'open (free-kernel identification settled negative)', 'SM §4.7 Theorem 9 Remark'),
 ("H-χ'", 'papers/SM.md', r"hypothesis H-χ' — which the present construction does not supply", 'open (sharpened; minimal embedding certified vector-like)', 'SM §4.8 Theorem 13(v)'),
 ('H-top', 'papers/SM.md', r'separate condition, \*\*H-top\*\*', 'open (not discharged)', 'SM §5'),
 ('H-det', 'papers/SM.md', r'and \*\*H-det\*\* \(', 'open (not discharged)', 'SM §5'),
 ('H-observer-bundle', 'papers/SM.md', r'recorded below as \*\*H-observer-bundle\*\*', 'open (native hypercharge reading of 1/α0 conditional on it)', 'SM §6.5'),
 ('H-Y-vertex', 'papers/SM.md', r'\*\*H-Y-vertex\*\*: that observer connection', 'open', 'SM §6.5'),
 ('(C1)', 'papers/Main.md', r'^\*\*\(C1\) Non-zero coupling', 'diagnostic of a realization (not a hypothesis of the characterization); necessity proved; follows from (C4) in any faithful realization', 'Main §1.3, status ledger §4.5'),
 ('(C2)', 'papers/Main.md', r'^\*\*\(C2\) Memory persistence', 'physical-regime premise; necessity conditional on the hidden-sector mixing hypothesis; two named forms (C2-structural, C2-slow)', 'Main §1.3, §3.4, status ledger'),
 ('(C3)', 'papers/Main.md', r'^\*\*\(C3\) Sufficient memory capacity', 'diagnostic; necessity proved (data-processing bound)', 'Main §1.3'),
 ('(C4)', 'papers/Main.md', r'^\*\*\(C4\) History readback', 'diagnostic; necessity immediate given non-Markovianity; physical discharge at the cosmological and lattice cuts OPEN', 'Main §1.3; GR §2.2 "Not presently discharged"; ROADMAP P1 "Physical C4 discharge" OPEN'),
 ('(EM)', 'papers/Main.md', r'mixing hypothesis \(EM\)\.\*\*', 'explicit physical hypothesis, conditional (not derived from φ)', 'Main §4.6'),
 ('(T)', 'papers/Main.md', r'\*\*Translation hypothesis \(T\) is the claim', 'hypothesis gating the imported Barandes correspondence (tuple instantiation), checked on representative processes', 'Main §3.4 Definition (unitarily evolving QM), status ledger'),
 ('mixing hypothesis', 'papers/Main.md', r'Suppose the mixing hypothesis holds', 'conditional (hidden-sector mixing, ETH-motivated); conditions the C2-necessity direction', 'Main §3.4; posit ledger item (v)'),
 ('Axiom 1', 'papers/Main.md', r'\*\*Axiom 1\*\* is the evidential floor', 'axiom (stated indubitable)', 'Main §1.2; Methodology §6.1'),
 ('Axiom 2', 'papers/Main.md', r'This is \*\*Axiom 2\*\*', 'posit (recurrence), non-derivable from Axiom 1', 'Main §1.2, posit ledger (i); Methodology §5'),
 ('A1', 'papers/Substratum.md', r'^\(A1\) \*\*Finiteness', 'structural assumption (two-part status: observation-bounded part from E3; total finiteness = gauge choice of minimal representative)', 'Substratum §3.1; Main posit ledger (ii)'),
 ('A2', 'papers/Substratum.md', r'^\(A2\) \*\*Determinism', 'structural assumption (two-part status, part-empirical recovery)', 'Substratum §3.1; Main posit ledger (iii)'),
 ('A3', 'papers/Substratum.md', r'^\(A3\) \*\*Bounded coupling', 'structural assumption', 'Substratum §3.1; Main posit ledger (ix)'),
 ('A4', 'papers/Substratum.md', r'^\(A4\) \*\*Center independence', 'structural assumption (two clauses)', 'Substratum §3.1; Main posit ledger (xi)'),
 ('A5', 'papers/Substratum.md', r'^\(A5\) \*\*Linearity', 'structural assumption, "partly derived" via amplitude-scale gauge; open step', 'Substratum §3.1; Main posit ledger (vii); ROADMAP declared inputs'),
 ('A6', 'papers/Substratum.md', r'^\(A6\) \*\*Background independence', 'structural assumption; ROADMAP P1 A6 CONDITIONAL (covariance holds identically on the link-coupled interface)', 'Substratum §3.1; ROADMAP P1 A6'),
 ('E1', 'papers/Substratum.md', r'^\(E1\) \*\*Unitary quantum mechanics', 'empirical input', 'Substratum §3.1'),
 ('E2', 'papers/Substratum.md', r'^\(E2\) \*\*Bell violations', 'empirical input', 'Substratum §3.1'),
 ('E3', 'papers/Substratum.md', r'^\(E3\) \*\*Finite boundary entropy', 'theoretical input (holographic bounds, not observed)', 'Substratum §3.1'),
 ('E4', 'papers/Substratum.md', r'^\(E4\) \*\*Spatial isotropy', 'empirical input', 'Substratum §3.1; Main posit ledger (vi)'),
 ('E5', 'papers/Substratum.md', r'^\(E5\) \*\*Propagating gravity', 'empirical input', 'Substratum §3.1'),
 ('E6', 'papers/Substratum.md', r'^\(E6\) \*\*Stable matter', 'empirical input', 'Substratum §3.1'),
 ('E7', 'papers/Substratum.md', r'^\(E7\) \*\*Boundary-entropy concordance', 'inferred empirical input (ΛCDM-pipeline quantity)', 'Substratum §3.1'),
 ('M1-T', 'papers/Substratum.md', r'\*\*M1-T\*\*, the observed temporal', 'input premise (temporal data lie in the history-readback / P-indivisible sector)', 'Substratum §3.2'),
 ('M1-B', 'papers/Substratum.md', r'and \*\*M1-B\*\*, Bell-violating composites', 'input premise (adopted ontic-parameter-dependent Bell branch)', 'Substratum §3.2'),
 ('S1', 'papers/GR.md', r'^\(\*S1\*\)', 'sufficient structural condition (universality class)', 'GR §8 universality'),
 ('S2', 'papers/GR.md', r'^\(\*S2\*\)', 'sufficient structural condition', 'GR §8'),
 ('S3', 'papers/GR.md', r'^\(\*S3\*\)', 'sufficient structural condition', 'GR §8'),
 ('S4', 'papers/GR.md', r'^\(\*S4\*\)', 'sufficient structural condition', 'GR §8'),
 ('(G1)', 'papers/Main.md', r'\(G1\) non-degenerate spectrum', 'genericity condition (fails on a measure-zero set) for the phase-locking lemma', 'Main §3.2; NB the labels G1–G3 also name GR\'s gravity levels'),
 ('Cond 2', 'papers/SM.md', r'\*\*Status of Cond 2: structural decomposition', 'Layer 2(b) relation b23=(4/3)(b12+b13); second-order derivation route excluded; O(λ³) route unpursued', 'SM §7.3; Juno §3.4 calls it "Condition 2", a substantive physical input'),
 ('Condition 1', 'papers/Juno.md', r'^\*\*Condition 1 \(natural normalization\)', 'labeling convention (b23 = 1)', 'Juno §3.4'),
 ('amplitude-scale gauge', 'papers/Substratum.md', r'\*\*Remark \(amplitude-scale gauge', 'explicit operational principle adjoined; results invoking it conditional on it (open)', 'Substratum §4 Remark and Status (open, referee-grade)'),
]

used_by = defaultdict(list)
for s in statements:
    for h in s['named_hypotheses']:
        used_by[h].append({'id': s['id'], 'paper': s['paper'], 'line': s['line'], 'label': s['label']})
# map statement-level token forms to hypothesis keys
alias = {'Condition 2': 'Cond 2', 'H-χ': "H-χ'", 'H-spin': "H-spin'", 'conditional-mixing hypothesis': 'mixing hypothesis'}

hypotheses = []
for tok, f, pat, status, src in H:
    site = locate(f, pat)
    occ = occurrences(tok if tok not in ('mixing hypothesis', 'amplitude-scale gauge') else tok)
    ub = used_by.get(tok, [])
    hypotheses.append({'name': tok, 'defined_at': site, 'status': status, 'status_source': src,
                       'used_by_statements': ub, 'used_by_count': len(ub), 'occurrences': occ,
                       'read_at': read_at(f)})

# posit ledger items as premises
posits = ['(i) Axiom 2 — recurrence', '(ii) finiteness of the total state space S (A1, gauge choice of minimal representative)',
          '(iii) determinism recovery with one empirical input (part-empirical)', '(iv) maximal-entropy measure selection',
          '(v) hidden-sector mixing hypothesis (ETH-motivated)', '(vi) spatial isotropy (E4)', '(vii) linearity (A5)',
          '(viii) site factorization', '(ix) bounded coupling degree (A3)', '(x) nearest-neighbour range (simple-cubic graph)',
          '(xi) center independence (A4), two clauses', '(xii) background independence (A6)']
posit_site = locate('papers/Main.md', r'^\*\*The posit ledger\.\*\*')

# names used but not stated in the manuscripts
research_only = [{'name': n, 'where': 'verification/coverage/LEDGER.json backlog[0].route (development notes)',
                  'stated_in_manuscripts': False} for n in ['H-functor', 'H-tensor', 'H-pure-seed', 'H-readout', 'H-monoidal']]
research_only.append({'name': 'H-∞', 'where': 'verification/ROADMAP.md P1 row (obligation name: finite → continuum completion)',
                      'stated_in_manuscripts': False})
research_only.append({'name': "H-chi'", 'where': 'verification/coverage/LEDGER.json entries (ASCII spelling of H-χ\')',
                      'stated_in_manuscripts': False})

# ------------------------------------------------------------------ obligations
R = open('verification/ROADMAP.md', encoding='utf-8').read().split('\n')
obligations = []
section = None
for i, l in enumerate(R):
    if l.startswith('#'):
        section = l.lstrip('# ').strip()
        continue
    if l.startswith('| **P') or (section and section.startswith('Settled negatively') and l.startswith('| ') and not l.startswith('| Finding') and not l.startswith('| ---')):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if section.startswith('Settled'):
            obligations.append({'table': 'settled negatively', 'line': i + 1, 'priority': None, 'obligation': cells[0],
                                'status': cells[1].strip('*'), 'status_detail': cells[1]})
        else:
            st = re.match(r'\*\*([A-Z]+)\*\*', cells[3])
            obligations.append({'table': 'queue', 'line': i + 1, 'priority': cells[0].strip('*'), 'obligation': cells[1],
                                'track': cells[2], 'status': st.group(1) if st else cells[3][:40],
                                'status_detail': cells[3][:1500], 'unlocks': cells[4] if len(cells) > 4 else None})
# non-table programme / long-range sections
for i, l in enumerate(R):
    if l.startswith('### ') and any(k in l for k in ('Hydrodynamics', 'The 3×3', 'residual deformation', 'census of', 'Minimal support',
                                                      'three-parameter family', 'Gauge/QFT')):
        obligations.append({'table': 'outside the active queue', 'line': i + 1, 'priority': None,
                            'obligation': l.lstrip('# ').strip(), 'status': 'long-range direction / programme record (not queued)'})
not_prior = [l.strip('- ')[:160] for l in R if l.startswith('- **') and any(k in l for k in ('Infinite-support', 'Hilbert-space representation', "CT3's", 'Finite-horizon', 'double-slit'))]
declared_inputs_line = next(i + 1 for i, l in enumerate(R) if l.startswith('## Declared inputs'))

# ------------------------------------------------------------------ predictions (appendix A)
def mdsplit(l):
    cells, cur, inmath = [], '', False
    for ch in l.strip().strip('|'):
        if ch == '$':
            inmath = not inmath
        if ch == '|' and not inmath:
            cells.append(cur.strip()); cur = ''
        else:
            cur += ch
    cells.append(cur.strip())
    return cells

A = open('book/appendix-a-prediction-status.md', encoding='utf-8').read().split('\n')
preds = []
table = None
for i, l in enumerate(A):
    if l.startswith('### A.4.1'): table = 'A.4.1 Standard Model observables'
    elif l.startswith('### A.4.2'): table = 'A.4.2 Gravitational-sector observables'
    elif l.startswith('### A.4.3'): table = 'A.4.3 Neutrino-sector observables'
    elif l.startswith('### A.4.4'): table = 'A.4.4 Biology and medicine'
    elif l.startswith('## A.5'): table = 'A.5 Forward predictions'
    elif l.startswith('## A.6'): table = None
    if table and l.startswith('| ') and not l.startswith('| #') and not l.startswith('|---'):
        c = mdsplit(l)
        if table.startswith('A.5'):
            preds.append({'table': table, 'line': i + 1, 'id': c[0], 'prediction': c[1], 'value': c[2], 'class': None,
                          'layer': None, 'testability': c[3], 'chapter': c[4] if len(c) > 4 else None})
        else:
            preds.append({'table': table, 'line': i + 1, 'id': c[0], 'prediction': c[1], 'value': c[2], 'class': c[3],
                          'layer': c[4], 'empirical_match': c[5], 'chapter': c[6] if len(c) > 6 else None})
stated = {}
for i, l in enumerate(A):
    m = re.search(r'Counts: ([^.]*)\. Total: (\d+)', l) or re.search(r'Counts: ([0-9 SCLRMEP+]+)\.', l)
    if m:
        stated[i + 1] = m.group(0)
counts = {}
for t in sorted(set(p['table'] for p in preds)):
    if t.startswith('A.5'):
        counts[t] = {'rows': sum(1 for p in preds if p['table'] == t)}
        continue
    cls = Counter(re.sub(r'[^SCLRMEP]', '', p['class'] or '') for p in preds if p['table'] == t)
    counts[t] = {'rows': sum(1 for p in preds if p['table'] == t), 'by_class_from_rows': dict(cls)}
for p in preds:
    p['read_at'] = read_at('book/appendix-a-prediction-status.md')

json.dump({'meta': {}, 'statements': statements, 'appendix_b_statements': d['appendix_b_statements'],
           'hypotheses': hypotheses, 'posit_ledger': {'site': posit_site, 'items': posits, 'read_at': read_at('papers/Main.md')},
           'named_only_outside_manuscripts': research_only,
           'obligations': obligations, 'roadmap_not_prioritized': not_prior,
           'roadmap_declared_inputs_section': 'verification/ROADMAP.md:%d' % declared_inputs_line,
           'predictions': {'rows': preds, 'computed_counts': counts, 'stated_counts_in_appendix_a': stated},
           'kernel': d['kernel'], 'diag': d['diag']},
          open(OUT, 'w'), ensure_ascii=False, indent=1)
print(len(statements), len(hypotheses), len(obligations), len(preds), len(d['kernel']))
print(Counter(s['proof_location']['category'] for s in statements))
print(counts); print(stated)
print([h['name'] for h in hypotheses if not h['defined_at']])
