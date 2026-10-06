#!/usr/bin/env python3
"""controls.py -- round K1-SHARP-TESTS-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the two cells computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  predicate   `HasTwoSharpTests` is the frozen definition whole: two sharp seeds, each separated on a state of the
                  body from the other and from its complement
  S2  classified  the classification theorems have exactly the frozen explicit binders and conclusions and their
                  prints; the seed classification names `sharp_eq_of_certain`; the equivalence names its three
                  directional witnesses (the d = 0 case, the d = 1 case, the axis witness); the cell's verdict has its
                  frozen conclusion
  S3  not implied the d = 1 control and the non-implication have their frozen conclusions; the non-implication's chain of
                  hypotheses is, type for type and in order, the explicit hypotheses other than `2 ≤ d` of the landed
                  relative selector `three_of_nativeGateOf_of_two_le` read from D, and its proof names the control
  S4  scope       no declaration mentions `Entangling` or `EntanglingOf`; `HasTwoSharpTests` is applied in a theorem only
                  to `eball _`; no theorem concludes `2 ≤ d` alone
  S5  reuse       no declaration shares a name with a landed object it reads; the only import is `OIBridge.K1Bridge`
  S6  neutral     no complex, conjugate-transpose, positive-semidefinite, qubit, Bloch, Pauli, density, flow, limit,
                  closure, density-of-subgroup, tensor-product or Hilbert token
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  separation  §A-§C and the classification verdict mention none of the selector's objects; §D and the
                  non-implication verdict do not mention `HasTwoSharpTests`; `2 ≤ d` occurs only in §C, §D and the
                  verdicts
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements by its own frozen rule, independently of the
                  other; at a commit carrying the result note, the note states exactly the computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.K2Guard`
  C   census      the census is D's with exactly the frozen family inserted after the K2-GUARD-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '68b6df0651f14b2c8ab082635b8d2051918617a2'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/SharpTests.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
SELECTOR_SRC = 'verification/lean-mathlib/OIBridge/K2Guard.lean'
SELECTOR_NAME = 'three_of_nativeGateOf_of_two_le'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = 'fd725b5e1a7296a4114a336419bf7e0d00f2d774'
ANCHOR_IMPORT = 'import OIBridge.K2Guard\n'
NEW_IMPORT = 'import OIBridge.SharpTests\n'
PREV_FAMILY_MODULES = ['K2Guard']
CENSUS_FAMILY = json.loads(r'''{
 "name": "the premise 2 <= d of the dimension selector at the elementary ball as two sharp binary tests distinct modulo complementation, and its independence from the selector's other relative hypotheses (round K1-SHARP-TESTS-1, reconstruction)",
 "modules": [
  "SharpTests"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round K1-SHARP-TESTS-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/preregistration.md. HasTwoSharpTests Ω: two sharp seeds e, f of Ω (OG-1's SharpSeed) with some state of Ω separating f from e and some state separating f from 1 - e. Cell 1: sharpEff (-b) x = 1 - sharpEff b x (sharpEff_neg_apply); the sharp seeds of eball d are the sharp effects along unit vectors (sharpSeed_iff, through sharp_eq_of_certain); eball 0 has no sharp seed (not_sharpSeed_zero); on eball 1 two sharp seeds agree or are complementary on every state (eq_or_compl_one); the first two axes witness the predicate for 2 <= d (hasTwoSharpTests_of_two_le); HasTwoSharpTests (eball d) <-> 2 <= d (hasTwoSharpTests_iff); verdict k1sharp_classified. Cell 2: at d = 1, fullEffects (eball 1), fullAut 1, sharpEff z1, neg1 and cnot1 satisfy EffectsOn, PreservesBody, SharpSeed, BoundaryTransitive, SeedOrbitAvailable, IsNot and NativeGateOf while 2 <= 1 fails (two_le_load_bearing_relative, nativeGateOf_cnot1), so those hypotheses do not imply 2 <= d (two_le_not_implied); verdict k1sharp_two_le_not_implied. Carried by no manuscript. The classification is proved for eball d only; nothing here sources HasTwoSharpTests or 2 <= d, or relates the predicate to entanglement."
}''')
DECLS = json.loads(r'''[
 [
  "def",
  "HasTwoSharpTests"
 ],
 [
  "theorem",
  "sharpEff_neg_apply"
 ],
 [
  "theorem",
  "sharpSeed_eq_sharpEff"
 ],
 [
  "theorem",
  "sharpSeed_iff"
 ],
 [
  "theorem",
  "not_sharpSeed_zero"
 ],
 [
  "theorem",
  "not_hasTwoSharpTests_zero"
 ],
 [
  "theorem",
  "eq_or_compl_one"
 ],
 [
  "theorem",
  "not_hasTwoSharpTests_one"
 ],
 [
  "theorem",
  "single_sq"
 ],
 [
  "theorem",
  "sharpEff_single_single"
 ],
 [
  "theorem",
  "hasTwoSharpTests_of_two_le"
 ],
 [
  "theorem",
  "hasTwoSharpTests_iff"
 ],
 [
  "theorem",
  "z1_sq"
 ],
 [
  "theorem",
  "nativeGateOf_cnot1"
 ],
 [
  "theorem",
  "two_le_load_bearing_relative"
 ],
 [
  "theorem",
  "two_le_not_implied"
 ],
 [
  "theorem",
  "k1sharp_classified"
 ],
 [
  "theorem",
  "k1sharp_two_le_not_implied"
 ]
]''')
TEXTS = json.loads(r'''{
 "HasTwoSharpTests": "def HasTwoSharpTests (Ω : Set V) : Prop :=\n  ∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧\n    (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)",
 "sharpEff_neg_apply": "theorem sharpEff_neg_apply (b x : Fin d → ℝ) : sharpEff (-b) x = 1 - sharpEff b x",
 "sharpSeed_eq_sharpEff": "theorem sharpSeed_eq_sharpEff {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (h : SharpSeed (eball d) e) :\n    ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u",
 "sharpSeed_iff": "theorem sharpSeed_iff (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) :\n    SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u",
 "not_sharpSeed_zero": "theorem not_sharpSeed_zero (e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ) : ¬ SharpSeed (eball 0) e",
 "not_hasTwoSharpTests_zero": "theorem not_hasTwoSharpTests_zero : ¬ HasTwoSharpTests (eball 0)",
 "eq_or_compl_one": "theorem eq_or_compl_one {e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ} (he : SharpSeed (eball 1) e)\n    (hf : SharpSeed (eball 1) f) :\n    (∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)",
 "not_hasTwoSharpTests_one": "theorem not_hasTwoSharpTests_one : ¬ HasTwoSharpTests (eball 1)",
 "single_sq": "theorem single_sq (i : Fin d) : ∑ j, (Pi.single i (1 : ℝ) : Fin d → ℝ) j ^ 2 = 1",
 "sharpEff_single_single": "theorem sharpEff_single_single {i k : Fin d} (hik : i ≠ k) :\n    sharpEff (Pi.single k (1 : ℝ)) (Pi.single i (1 : ℝ)) = 1 / 2",
 "hasTwoSharpTests_of_two_le": "theorem hasTwoSharpTests_of_two_le (hd : 2 ≤ d) : HasTwoSharpTests (eball d)",
 "hasTwoSharpTests_iff": "theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d",
 "z1_sq": "theorem z1_sq : ∑ j, z1 j ^ 2 = 1",
 "nativeGateOf_cnot1": "theorem nativeGateOf_cnot1 : NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1",
 "two_le_load_bearing_relative": "theorem two_le_load_bearing_relative :\n    EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧\n      SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧\n      SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧\n      IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧\n      ¬ (2 ≤ 1)",
 "two_le_not_implied": "theorem two_le_not_implied :\n    ¬ (∀ (d : ℕ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))\n        (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n        (T : W d ≃ₗ[ℝ] W d),\n        EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r →\n          BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail → IsNot (eball d) z N →\n          NativeGateOf (eball d) avail z N T → 2 ≤ d)",
 "k1sharp_classified": "theorem k1sharp_classified :\n    (∀ (d : ℕ) (b x : Fin d → ℝ), sharpEff (-b) x = 1 - sharpEff b x) ∧\n      (∀ (d : ℕ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ),\n        SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u) ∧\n      (∀ e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ, ¬ SharpSeed (eball 0) e) ∧\n      (∀ e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ, SharpSeed (eball 1) e → SharpSeed (eball 1) f →\n        (∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)) ∧\n      (∀ d : ℕ, 2 ≤ d → HasTwoSharpTests (eball d)) ∧\n      (∀ d : ℕ, HasTwoSharpTests (eball d) ↔ 2 ≤ d)",
 "k1sharp_two_le_not_implied": "theorem k1sharp_two_le_not_implied :\n    (EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧\n      SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧\n      SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧\n      IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧\n      ¬ (2 ≤ 1)) ∧\n    ¬ (∀ (d : ℕ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))\n        (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n        (T : W d ≃ₗ[ℝ] W d),\n        EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r →\n          BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail → IsNot (eball d) z N →\n          NativeGateOf (eball d) avail z N T → 2 ≤ d)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.SharpTests.sharpEff_neg_apply",
 "OIBridge.SharpTests.sharpSeed_iff",
 "OIBridge.SharpTests.not_sharpSeed_zero",
 "OIBridge.SharpTests.not_hasTwoSharpTests_zero",
 "OIBridge.SharpTests.eq_or_compl_one",
 "OIBridge.SharpTests.not_hasTwoSharpTests_one",
 "OIBridge.SharpTests.hasTwoSharpTests_of_two_le",
 "OIBridge.SharpTests.hasTwoSharpTests_iff",
 "OIBridge.SharpTests.nativeGateOf_cnot1",
 "OIBridge.SharpTests.two_le_load_bearing_relative",
 "OIBridge.SharpTests.two_le_not_implied",
 "OIBridge.SharpTests.k1sharp_classified",
 "OIBridge.SharpTests.k1sharp_two_le_not_implied"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.K1Bridge\n\nnamespace OIBridge\nnamespace SharpTests\n\nopen Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface\nopen EffectSpace K1Bridge\n\nvariable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}\n\n/-- Two sharp binary tests of `Ω`, separated on `Ω` from each other and from each other's\ncomplement. -/\ndef HasTwoSharpTests (Ω : Set V) : Prop :=\n  ∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧\n    (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace SharpTests",
 "open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface",
 "open EffectSpace K1Bridge",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}",
 "end SharpTests",
 "end OIBridge"
]''')
SEL_TYPES = json.loads(r'''["EffectsOn (eball d) avail", "PreservesBody (eball d) G", "SharpSeed (eball d) r", "BoundaryTransitive (eball d) G", "SeedOrbitAvailable G r avail", "IsNot (eball d) z N", "NativeGateOf (eball d) avail z N T"]''')
N_PRINTS = 13

DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]


def check(code, name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name, flush=True)
    if not cond:
        FAILS.append(code)


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = git('show', '%s:%s' % (commit, path))
    return r.stdout if r.returncode == 0 else None


def header(text):
    i = text.find('\nimport ')
    return text[:i] if i != -1 else text


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    """Each context line with its indented continuation lines (a `variable` block spanning several lines)."""
    lines = text.split('\n')
    out = []
    for k, line in enumerate(lines):
        if CTX.match(line):
            block = [line]
            j = k + 1
            while j < len(lines) and lines[j].startswith('  ') and line.startswith('variable'):
                block.append(lines[j])
                j += 1
            out.append('\n'.join(block))
    return out


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def stmt_end(chunk):
    """End of a theorem's statement: the first ` :=`, or a ` where` closing a line, whichever is earlier."""
    ends = [j for j in (chunk.find(' :='),) if j != -1]
    m = re.search(r' where\n', chunk)
    if m:
        ends.append(m.start())
    return min(ends) if ends else -1


def spans(text):
    """[(kind, name, start, statement end or -1, end)] for every declaration, in order."""
    out = []
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        se = -1
        if m.group(1) in ('theorem', 'lemma'):
            j = stmt_end(chunk)
            if j != -1:
                se = start + j
        out.append((m.group(1), m.group(2), start, se if se != -1 else start + len(chunk), nxt, start + len(chunk)))
    return out


def decl_chunks(text):
    """name -> (kind, statement or whole text, proof text after the statement for theorems)."""
    out = {}
    for kind, name, start, se, nxt, cend in spans(text):
        if kind in ('theorem', 'lemma'):
            out[name] = (kind, text[start:se], text[se:nxt])
        else:
            out[name] = (kind, text[start:cend], '')
    return out


def colon_index(stmt):
    """Index of the colon separating binders from the conclusion: the first at bracket depth 0 after the name."""
    m = DECL.match(stmt)
    i = m.end() if m else 0
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return j
    return -1


def split_statement(stmt):
    """(binders, conclusion) of a declaration header."""
    m = DECL.match(stmt)
    i = m.end() if m else 0
    j = colon_index(stmt)
    if j == -1:
        return stmt[i:], ''
    return stmt[i:j], stmt[j + 1:]


def def_header(text):
    """A definition's header: up to ` :=` or a ` where` closing a line."""
    j = stmt_end(text)
    return text[:j] if j != -1 else text


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def norm(s):
    return ' '.join(s.split())


def fields(structure_text):
    """The field names of a structure chunk: the two-space-indented `name :` lines after `where`."""
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    return [m.group(1) for m in re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M)]


def field_line(structure_text, name):
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    ms = list(re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M))
    for k, m in enumerate(ms):
        if m.group(1) == name:
            return norm(body[m.start():ms[k + 1].start() if k + 1 < len(ms) else len(body)])
    return None


def token(name, text):
    return re.search(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(name), text) is not None


def sections(text):
    """[(position, label)] of the section markers, label `§A` ... or `verdict`."""
    out = []
    for m in re.finditer(r'^/-! ### (§[A-Z]|The verdict)', text, re.M):
        out.append((m.start(), 'verdict' if m.group(1) == 'The verdict' else m.group(1)))
    return out


def section_at(secs, pos):
    lab = None
    for p, l in secs:
        if p <= pos:
            lab = l
    return lab

PREFIX = 'OIBridge.SharpTests.'
# S1 -- the predicate
PRED = 'HasTwoSharpTests'
PRED_BODY = ('∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧ (∃ x ∈ Ω, f x ≠ e x) ∧ '
             '(∃ x ∈ Ω, f x ≠ 1 - e x)')
# S2 -- the classification: name -> (explicit binders, conclusion, names its proof must use)
CLASS = {
    'sharpEff_neg_apply': ('(b x : Fin d → ℝ)', 'sharpEff (-b) x = 1 - sharpEff b x', ()),
    'sharpSeed_eq_sharpEff': ('(h : SharpSeed (eball d) e)',
                              '∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u', ('sharp_eq_of_certain',)),
    'sharpSeed_iff': ('(e : (Fin d → ℝ) →ᵃ[ℝ] ℝ)',
                      'SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u',
                      ('sharpSeed_eq_sharpEff', 'sharpEff_sharpSeed')),
    'not_sharpSeed_zero': ('(e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ)', '¬ SharpSeed (eball 0) e', ()),
    'not_hasTwoSharpTests_zero': ('', '¬ HasTwoSharpTests (eball 0)', ('not_sharpSeed_zero',)),
    'eq_or_compl_one': ('(he : SharpSeed (eball 1) e) (hf : SharpSeed (eball 1) f)',
                        '(∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)', ('sharpSeed_eq_sharpEff',)),
    'not_hasTwoSharpTests_one': ('', '¬ HasTwoSharpTests (eball 1)', ('eq_or_compl_one',)),
    'hasTwoSharpTests_of_two_le': ('(hd : 2 ≤ d)', 'HasTwoSharpTests (eball d)', ('sharpEff_sharpSeed',)),
    'hasTwoSharpTests_iff': ('', 'HasTwoSharpTests (eball d) ↔ 2 ≤ d',
                             ('not_hasTwoSharpTests_zero', 'not_hasTwoSharpTests_one', 'hasTwoSharpTests_of_two_le')),
}
CLASS_PRINTED = ('sharpEff_neg_apply', 'sharpSeed_iff', 'not_sharpSeed_zero', 'not_hasTwoSharpTests_zero',
                 'eq_or_compl_one', 'not_hasTwoSharpTests_one', 'hasTwoSharpTests_of_two_le', 'hasTwoSharpTests_iff')
CLASS_VERDICT = 'k1sharp_classified'
CLASS_VERDICT_CONCL = (
    '(∀ (d : ℕ) (b x : Fin d → ℝ), sharpEff (-b) x = 1 - sharpEff b x) ∧ '
    '(∀ (d : ℕ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ), SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ '
    'e = sharpEff u) ∧ (∀ e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ, ¬ SharpSeed (eball 0) e) ∧ '
    '(∀ e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ, SharpSeed (eball 1) e → SharpSeed (eball 1) f → '
    '(∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)) ∧ '
    '(∀ d : ℕ, 2 ≤ d → HasTwoSharpTests (eball d)) ∧ (∀ d : ℕ, HasTwoSharpTests (eball d) ↔ 2 ≤ d)')
# S3 -- the non-implication
CONTROL = 'two_le_load_bearing_relative'
CONTROL_CONCL = ('EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧ '
                 'SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧ '
                 'SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧ '
                 'IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧ '
                 '¬ (2 ≤ 1)')
GATE = ('nativeGateOf_cnot1', 'NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1')
NOT_IMPLIED = 'two_le_not_implied'
QUANT = ('∀ (d : ℕ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) '
         '(r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d), ')
NOT_IMPLIED_CONCL = '¬ (' + QUANT + ' → '.join(SEL_TYPES) + ' → 2 ≤ d)'
NI_VERDICT = 'k1sharp_two_le_not_implied'
NI_VERDICT_CONCL = '(' + CONTROL_CONCL + ') ∧ ' + NOT_IMPLIED_CONCL
CELL2_OBJECTS = ('NativeGateOf', 'IsNot', 'EffectsOn', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable',
                 'fullAut', 'fullEffects', 'cnot1', 'neg1', 'z1', 'W')
# S4 -- scope
FORBIDDEN_OBJECTS = ('Entangling', 'EntanglingOf')
PRED_ARG = re.compile(r'HasTwoSharpTests\s+(?!\(eball\s)')
# S5 -- reuse
REUSED = ('SharpSeed', 'IsEffectOn', 'EffectsOn', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable',
          'NativeGate', 'NativeGateOf', 'IsNot', 'eball', 'sharpEff', 'sharpVec', 'sharpEff_apply', 'sharpEff_self',
          'sharpEff_sharpSeed', 'sharpEff_isEffectOn', 'sharp_eq_of_certain', 'mem_eball_of_sphere', 'fullAut',
          'fullEffects', 'preservesBody_fullAut', 'boundaryTransitive_fullAut', 'isEffectOn_seedTransport',
          'maxConeOf', 'maxConeOf_fullEffects', 'maxCone', 'z1', 'neg1', 'cnot1', 'isNot_neg1', 'nativeGate_cnot1',
          'W', 'axisVec', 'axisVec_sq', 'seedTransport', 'dim_of_nativeGateOf', 'three_of_nativeGateOf')
IMPORT_ONLY = 'import OIBridge.K1Bridge'
# S6 -- neutral
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'flow', 'Flow', 'LimitClosed', 'closure', 'Tendsto', 'Filter', 'Dense', 'TensorProduct',
                  'Hilbert', 'MixingClosed', 'commutator', 'Commute')
# S7 -- phrases
PHRASES = ('OI supplies', 'supplied by OI', 'derived from OI', 'sourced from OI', 'StageCompletion supplies',
           'supplied by StageCompletion', 'the observer architecture supplies', 'supplied by the observer architecture',
           'establishes complementarity', 'complementarity is derived', 'is complementarity', 'quantumness',
           'nonclassicality', 'non-classicality', 'establishes incompatibility', 'establishes noncommutativity',
           'every classical theory has', 'equivalent to entanglement', 'implies entanglement',
           'entanglement follows', 'on every convex body', 'for every convex body', 'derives 2 ≤ d',
           '2 ≤ d is derived', '2 ≤ d is sourced', 'qubit')
# S8 -- separation
TWO_LE_RE = re.compile(r'2\s*≤\s*d(?![\w\'])')
TWO_LE_SECTIONS = ('§C', '§D', 'verdict')
# V -- the frozen decision rule
CLASS_TOKENS = ('K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED', 'K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED')
NI_TOKENS = ('K1-TWO-LE-NOT-IMPLIED', 'K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def binder_types(b):
    """The types of the top-level `( ... : T)` binder groups of an explicit binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c == '(':
            if depth == 0:
                start = i
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0 and start is not None:
                grp = b[start + 1:i]
                j = grp.find(' : ')
                if j != -1:
                    out.append(norm(grp[j + 3:]))
                start = None
    return out


def selector_types(text):
    """The explicit hypothesis types of the landed relative selector, `2 ≤ d` removed."""
    chunks = decl_chunks(text)
    if SELECTOR_NAME not in chunks:
        return None
    b, c = split_statement(chunks[SELECTOR_NAME][1])
    if norm(c) != 'd = 3':
        return None
    return [t for t in binder_types(explicit_binders(b)) if t != '2 ≤ d']


def classified_cell(chunks):
    """K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED iff: `HasTwoSharpTests` is the frozen definition; every classification
    theorem has exactly its frozen explicit binders and conclusion and names its frozen proof dependencies (the
    equivalence its three directional witnesses); and the cell's verdict has its frozen conclusion. Otherwise
    K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED. Reads no selector statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    ok = kinds.get(PRED) == 'def' and def_body(texts.get(PRED, '')) == norm(PRED_BODY)
    for n, (b, c, deps) in CLASS.items():
        bb, cc = stmt_parts(texts, n)
        ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == norm(b) and cc == norm(c) and \
            all(token(m, proofs.get(n, '')) for m in deps)
    ok = ok and kinds.get(CLASS_VERDICT) == 'theorem' and stmt_parts(texts, CLASS_VERDICT)[1] == norm(CLASS_VERDICT_CONCL)
    return [CLASS_TOKENS[0] if ok else CLASS_TOKENS[1]]


def not_implied_cell(chunks):
    """K1-TWO-LE-NOT-IMPLIED iff: the d = 1 control, the gate instance and the non-implication are theorems with their
    frozen conclusions, the non-implication's hypothesis chain being the landed selector's hypotheses other than
    `2 ≤ d` (frozen from D); the non-implication's proof names the control; and the cell's verdict has its frozen
    conclusion. Otherwise K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED. Reads no classification statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    ok = len(SEL_TYPES) == 7
    for n, c in ((CONTROL, CONTROL_CONCL), GATE, (NOT_IMPLIED, NOT_IMPLIED_CONCL), (NI_VERDICT, NI_VERDICT_CONCL)):
        bb, cc = stmt_parts(texts, n)
        ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == '' and cc == norm(c)
    ok = ok and token(CONTROL, proofs.get(NOT_IMPLIED, ''))
    return [NI_TOKENS[0] if ok else NI_TOKENS[1]]


def verdicts(chunks):
    return classified_cell(chunks), not_implied_cell(chunks)


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    ok1 = kinds.get(PRED) == 'def' and texts.get(PRED) == TEXTS.get(PRED) and \
        def_body(texts.get(PRED, '')) == norm(PRED_BODY)
    check('S1', 'the predicate is the frozen definition: two sharp seeds separated on states from each other and from '
                'the complement' + tag, ok1)
    # S2
    bad2 = []
    for n, (b, c, deps) in CLASS.items():
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c) or \
                not all(token(m, proofs.get(n, '')) for m in deps):
            bad2.append(n)
    bad2 += [n for n in CLASS_PRINTED if PREFIX + n not in prints]
    if stmt_parts(texts, CLASS_VERDICT)[1] != norm(CLASS_VERDICT_CONCL) or PREFIX + CLASS_VERDICT not in prints:
        bad2.append(CLASS_VERDICT)
    check('S2', 'the classification with its frozen binders, conclusions, proof dependencies and prints; the '
                'equivalence through its three directional witnesses%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''),
          not bad2)
    # S3
    bad3 = []
    for n, c in ((CONTROL, CONTROL_CONCL), GATE, (NOT_IMPLIED, NOT_IMPLIED_CONCL), (NI_VERDICT, NI_VERDICT_CONCL)):
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or explicit_binders(bb) != '' or cc != norm(c) or PREFIX + n not in prints:
            bad3.append(n)
    if not token(CONTROL, proofs.get(NOT_IMPLIED, '')):
        bad3.append(NOT_IMPLIED + ' proof')
    check('S3', 'the d = 1 control and the non-implication with their frozen conclusions, over the landed selector\'s '
                'hypotheses%s%s' % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = [t for t in FORBIDDEN_OBJECTS if token(t, code)]
    for m, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            if PRED_ARG.search(t):
                bad4.append(m)
            if stmt_parts(texts, m)[1] == norm('2 ≤ d'):
                bad4.append(m)
    check('S4', 'no entangling object; the predicate applied in theorems only to eball; no theorem concluding 2 ≤ d%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S5', 'landed objects reused, not re-declared; the only import is OIBridge.K1Bridge%s%s'
          % (tag, (' %s' % clash[:3]) if clash else ''), not clash and imports == [IMPORT_ONLY])
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no flow, limit, closure or density token%s%s' % (tag, (' %s' % hits) if hits else ''),
          not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    secs = sections(mod)
    bad8 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        sec = section_at(secs, start)
        body = code_only(mod[start:nxt])
        if (sec in ('§A', '§B', '§C') or name == CLASS_VERDICT) and any(token(t, body) for t in CELL2_OBJECTS):
            bad8.append(name)
        if (sec == '§D' or name == NI_VERDICT) and token(PRED, body):
            bad8.append(name)
        if sec not in TWO_LE_SECTIONS and TWO_LE_RE.search(body):
            bad8.append(name)
    check('S8', 'the cells are separated; 2 ≤ d only in §C, §D and the verdicts%s%s'
          % (tag, (' %s' % bad8[:3]) if bad8 else ''), not bad8)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    a, b = verdicts(chunks)
    check('V', 'one outcome per cell by the frozen rules: %s, %s%s' % (a, b, tag), len(a) == 1 and len(b) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in CLASS_TOKENS + NI_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context block unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s'
          % (tag, (' (changed: %s)' % ', '.join(bad[:4])) if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, chunks, prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_want(d_text):
    d = json.loads(d_text)
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['modules'] == PREV_FAMILY_MODULES]
    if len(k) != 1:
        return None
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        want = census_want(d_text)
    except Exception:
        return False
    return want is not None and e_text == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    sel = show(D, SELECTOR_SRC)
    check('S3', 'the landed relative selector at D has exactly the frozen hypotheses other than 2 ≤ d',
          sel is not None and selector_types(sel) == SEL_TYPES)
    mod = show(commit, MOD)
    module_checks(mod)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b, toks), len(a) == 1 and len(b) == 1 and sorted(toks) == sorted(a + b))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the K2-GUARD-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    a, b = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
    print('VERDICT  CLASSIFIED   %s' % ('/'.join(a) or 'none'))
    print('VERDICT  NOT-IMPLIED  %s' % ('/'.join(b) or 'none'))
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1)

def must_fail(code, label, mod2):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mod2)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    """Insert a declaration just before the verdict section (inside §P)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_before(text, anchor, decl):
    i = text.index(anchor)
    return text[:i] + decl + '\n\n' + text[i:]

def append_control(text, decl):
    """Insert a declaration just before the verdict section."""
    i = text.index('\n/-! ### The verdicts')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


CTL_TAIL = ('      IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧\n'
            '      ¬ (2 ≤ 1) :=\n  ⟨fun _ he')
NI_TAIL = 'IsNot (eball d) z N →\n          NativeGateOf (eball d) avail z N T → 2 ≤ d) := by'
NI_PROOF = '  obtain ⟨hE, hG, hP1, hK, hV4, hN, hT, h2⟩ := two_le_load_bearing_relative\n'
PRED_TAIL = '    (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)\n'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    a, b = verdict_of(mod)
    check('T', 'the reference module reads %s and %s' % (a, b), a == [CLASS_TOKENS[0]] and b == [NI_TOKENS[0]])
    sel = show(D, SELECTOR_SRC)
    check('T', 'the landed relative selector at D yields the frozen hypothesis types', selector_types(sel) == SEL_TYPES)
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem k1sharp_classified :', '\ntheorem k1sharp_classified\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}\n',
                           '\nvariable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ} {Ω : Set V}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace K1Bridge\n', '\nopen EffectSpace\n'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem z1_sq : ∑ j, z1 j ^ 2 = 1 := by', 'theorem z1_sq : ∑ j, z1 j ^ 2 ≤ 1 := by'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.SharpTests.eq_or_compl_one\n', ''))
    # S1
    must_fail('S1', 'the predicate without the complement clause',
              replace_once(mod, PRED_TAIL, '    (∃ x ∈ Ω, f x ≠ e x)\n'))
    must_fail('S1', 'test identity as equality of maps',
              replace_once(mod, PRED_TAIL, '    f ≠ e ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)\n'))
    # S2
    must_fail('S2', 'the witness requiring 3 ≤ d',
              replace_once(mod, 'theorem hasTwoSharpTests_of_two_le (hd : 2 ≤ d)',
                           'theorem hasTwoSharpTests_of_two_le (hd : 3 ≤ d)'))
    must_fail('S2', 'the equivalence weakened to one direction',
              replace_once(mod, 'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d := by',
                           'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) → 2 ≤ d := by'))
    must_fail('S2', 'the complement identity changed',
              replace_once(mod, 'sharpEff (-b) x = 1 - sharpEff b x := by', 'sharpEff (-b) x = sharpEff b x := by'))
    must_fail('S2', 'the equivalence proved without the d = 1 case',
              replace_once(mod, '    · exact not_hasTwoSharpTests_one h\n', '    · exact absurd h (by simp)\n'))
    must_fail('S2', 'the seed classification without sharp_eq_of_certain',
              replace_once(mod, '  exact ⟨u, sharp_eq_of_certain he hu hw h1 h0⟩', '  exact ⟨u, by simpa using he⟩'))
    # S3
    must_fail('S3', 'a hypothesis dropped from the d = 1 control',
              replace_once(mod, CTL_TAIL, CTL_TAIL.replace('IsNot (eball 1) z1 neg1 ∧ ', '')))
    must_fail('S3', 'a hypothesis dropped from the non-implication',
              replace_once(mod, NI_TAIL, NI_TAIL.replace('IsNot (eball d) z N →\n          ', '')))
    must_fail('S3', 'the non-implication proved without the control',
              replace_once(mod, NI_PROOF, NI_PROOF.replace('two_le_load_bearing_relative', 'k1sharp_aux')))
    sel_m = replace_once(sel, '    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by',
                         '    (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by')
    check('M', 'selector types: a landed selector with a hypothesis dropped does not yield the frozen types',
          selector_types(sel_m) != SEL_TYPES)
    # S4
    must_fail('S4', 'an entangling object mentioned',
              append_control(mod, 'theorem ent_free : True := by\n  have := @Entangling\n  trivial'))
    must_fail('S4', 'the predicate concluded of a general body',
              append_control(mod, 'theorem pred_general (Ω : Set (Fin 2 → ℝ)) (h : HasTwoSharpTests Ω) : '
                                  'HasTwoSharpTests Ω := h'))
    must_fail('S4', 'a theorem concluding 2 ≤ d',
              append_control(mod, 'theorem two_le_free (hd : 3 ≤ d) : 2 ≤ d := by omega'))
    # S5
    must_fail('S5', 'a landed definition re-declared', append_control(mod, 'def fullAut : ℕ := 0'))
    must_fail('S5', 'a second import',
              replace_once(mod, 'import OIBridge.K1Bridge\n', 'import OIBridge.K1Bridge\nimport OIBridge.K2Guard\n'))
    # S6
    must_fail('S6', 'a complex scalar', append_control(mod, 'def cvec (z : Fin 3 → ℂ) : Fin 3 → ℂ := z'))
    must_fail('S6', 'a closure token',
              append_control(mod, 'def closedFamily (A : Set (Fin 2 → ℝ)) : Prop := closure A ⊆ A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  (B) At `d = 1`', '  This is quantumness. (B) At `d = 1`'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('Two sharp binary tests distinct modulo complementation exist exactly when 2 ≤ d; '
                          'the round does not show that OI provides them.')
          and phrase_hits('Hence OI\nsupplies two tests.') == ['OI supplies'])
    # S8
    must_fail('S8', 'a selector object in the classification sections',
              insert_in_section(mod, '/-! ### §C', 'theorem fa_one : fullAut 1 = fullAut 1 := rfl'))
    must_fail('S8', 'the predicate in the selector section',
              append_control(mod, 'theorem pred_d : ¬ HasTwoSharpTests (eball 1) := not_hasTwoSharpTests_one'))
    must_fail('S8', '2 ≤ d in §A',
              insert_in_section(mod, '/-! ### §B', 'theorem two_le_A (hd : 2 ≤ d) : 1 ≤ d := by omega'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.SharpTests.k1sharp_two_le_not_implied\n',
                           '#print axioms OIBridge.SharpTests.k1sharp_two_le_not_implied\n'
                           '#print axioms OIBridge.SharpTests.z1_sq\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.SharpTests.sharpSeed_iff\n',
                           '#print axioms OIBridge.SharpTests.sharpSeed_iff\n'
                           '#print axioms OIBridge.SharpTests.sharpSeed_iff\n'))
    # V -- each cell reads its alternative, independently of the other
    m_pred = replace_once(mod, PRED_TAIL, '    (∃ x ∈ Ω, f x ≠ e x)\n')
    check('M', 'decision rule: the predicate without the complement clause reads MULTIPLICITY-NOT-CLASSIFIED and '
               'leaves the other cell unchanged', verdict_of(m_pred) == ([CLASS_TOKENS[1]], [NI_TOKENS[0]]))
    m_ctl = replace_once(mod, CTL_TAIL, CTL_TAIL.replace('IsNot (eball 1) z1 neg1 ∧ ', ''))
    check('M', 'decision rule: a hypothesis dropped from the control reads NON-IMPLICATION-NOT-ESTABLISHED and leaves '
               'the other cell unchanged', verdict_of(m_ctl) == ([CLASS_TOKENS[0]], [NI_TOKENS[1]]))
    m_iff = replace_once(mod, 'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d := by',
                         'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) → 2 ≤ d := by')
    check('M', 'decision rule: the equivalence weakened to one direction reads MULTIPLICITY-NOT-CLASSIFIED',
          verdict_of(m_iff)[0] == [CLASS_TOKENS[1]])
    m_ni = replace_once(mod, NI_PROOF, NI_PROOF.replace('two_le_load_bearing_relative', 'k1sharp_aux'))
    check('M', 'decision rule: the non-implication proved without the control reads NON-IMPLICATION-NOT-ESTABLISHED',
          verdict_of(m_ni)[1] == [NI_TOKENS[1]])
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED and K1-TWO-LE-NOT-IMPLIED.')
          == ['K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED', 'K1-TWO-LE-NOT-IMPLIED']
          and note_tokens('K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED, not K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED.')
          == ['K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED', 'K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED'])
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES][0]
    bad_status = json.loads(good)
    bad_status['families'][k + 1]['status'] = 'carried'
    bad_status = json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n'
    moved = json.loads(good)
    moved['families'].insert(k, moved['families'].pop(k + 1))
    moved = json.dumps(moved, indent=2, ensure_ascii=False) + '\n'
    check('M', 'census: the frozen edit passes; a changed status, a moved family, a whitespace change and the '
               'unchanged file fail',
          census_ok(d_cen, good) and not census_ok(d_cen, bad_status) and moved != good
          and not census_ok(d_cen, moved) and not census_ok(d_cen, good.replace('\n', '\n ', 1))
          and not census_ok(d_cen, d_cen))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) == 2 and argv[0] == 'verdict':
        print_verdicts(argv[1])
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
