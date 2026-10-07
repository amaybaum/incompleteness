#!/usr/bin/env python3
"""controls.py -- round ODD-CHAR-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the three cells computed from the module's statements at <commit> and the
                                            landed statements at D

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  L   landed      the landed texts the rules read, read from D, are the frozen ones
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  family      the family definitions are the frozen ones; for every `k`, `nK k` is a NOT of `eball (2k+1)` with
                  axis `zK k`, `gRev k` satisfies the landed `NativeGate` frame field read from D at the gate and the
                  axis, and `GateRel (nK k) (gRev k)` holds through the landed `sgate_relT` and `sgate_relC`; the landed
                  `GateRel` fields are the landed `NativeGate` relation fields; no declaration of §A mentions the native
                  gate or positivity
  S2  odd         the characterization's statement is the frozen existential -- `IsNot`, the landed frame field and
                  `GateRel` -- equivalent to `Odd d`; its proof reads the landed `not_even_of_gateRel`, the landed
                  `d = 1` objects `cnot1`, `isNot_neg1` and `cnot1_frame` with the landed relations of `cnot1`, and the
                  family; the landed statements it reads are the frozen ones; §B mentions neither the native gate nor
                  positivity
  S3  positivity  for `k ≥ 1`: the witness definitions are the frozen ones; the image of the frozen product pairs to
                  `-1 / 10` with the two frozen sharp effects; the forward-positivity failure is the negation of the
                  landed `posFwd` field at the body and the gate, proved through that value; the gate is the family's,
                  with its frame and its relations; no declaration of §C names a landed dimension corollary of the
                  native gate or inverse positivity
  S6  scope       no declaration mentions a complex field, a landed dimension selector, inverse positivity or
                  `Entangling`; no theorem concludes an equation or inequation on `d`; no theorem concludes the native
                  gate, the maximal cone or forward positivity without negation
  S7  reuse       no declaration of the module shares its name with an OIBridge declaration visible to it; the only
                  import is `OIBridge.ParityNot`
  S8  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements and the landed statements at D by its own frozen
                  rule, independently of the others; at a commit carrying the result note, the note states exactly the
                  computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.ParityNot`
  C   census      the census is D's with exactly the frozen family inserted after the PARITY-NOT-1 family, byte for
                  byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '3c92d16b2f33d6a6acd32e96922a1f66ee735220'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-odd-char-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = LEAN + 'OddChar.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = 'bbb8a63229870f61445d5dbb3fe9102b826d9208'
ANCHOR_IMPORT = 'import OIBridge.ParityNot\n'
NEW_IMPORT = 'import OIBridge.OddChar\n'
PREV_FAMILY_MODULES = ['ParityNot']
CENSUS_FAMILY = json.loads(r'''{
 "name": "The dimensions carrying a NOT, DIM-1's frame and the two gate relations are exactly the odd ones, and at each odd dimension at least three an explicit gate of the family with the frame and the relations fails forward positivity (round ODD-CHAR-1, reconstruction)",
 "modules": [
  "OddChar"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round ODD-CHAR-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-odd-char-1/preregistration.md. Q-FAM: for every k, nK k = diagSign (cK k), with sign −1 on the homogeneous indices above k, is a NOT of eball (2k+1) with axis the last coordinate zK k, and the sign-free reversal gate gRev k = sgateEquiv (oddK k) Fin.rev satisfies NativeGate's frame and GateRel (nK k) (gRev k) (isNot_nK, gRev_frame, gateRel_gRev). Q-ODD: some z, N, G with IsNot (eball d) z N, the frame and GateRel N G exist exactly when d is odd (exists_frame_gateRel_iff_odd), through PARITY-NOT-1's not_even_of_gateRel one way and DIM-1's cnot1 at d = 1 and gRev k at d = 2k+1 the other. Q-POS: for k ≥ 1 the image under gRev k of the product of the first axis with the corner pairs to −1/10 with the sharp effects of wK k and zK k, so forward positivity fails (gRev_value, not_posFwd_gRev, not_nativeGate_gRev). Carried by no manuscript. With DIM-1's dim_of_nativeGate, the positivity clauses are collectively load-bearing for excluding the odd dimensions above three; the round does not separate forward from inverse positivity, classifies no positive gate, and concerns no complex structure and no NOT of a physical theory."
}''')
DECLS = json.loads(r'''[
 [
  "def",
  "oddK"
 ],
 [
  "theorem",
  "oddK_rev"
 ],
 [
  "def",
  "cK"
 ],
 [
  "def",
  "nK"
 ],
 [
  "def",
  "zK"
 ],
 [
  "def",
  "gRev"
 ],
 [
  "theorem",
  "gRev_apply"
 ],
 [
  "theorem",
  "cK_sq"
 ],
 [
  "theorem",
  "homMap_nK_sign"
 ],
 [
  "theorem",
  "sum_val_ite"
 ],
 [
  "theorem",
  "sum_zK_sq"
 ],
 [
  "theorem",
  "isNot_nK"
 ],
 [
  "theorem",
  "hom_smul_zK"
 ],
 [
  "theorem",
  "hom_zK"
 ],
 [
  "theorem",
  "gRev_frame_aux"
 ],
 [
  "theorem",
  "gRev_frame"
 ],
 [
  "theorem",
  "gateRel_gRev"
 ],
 [
  "theorem",
  "finrank_plus_eq_finrank_minus_nK"
 ],
 [
  "theorem",
  "exists_frame_gateRel_iff_odd"
 ],
 [
  "def",
  "xK"
 ],
 [
  "noncomputable def",
  "wK"
 ],
 [
  "theorem",
  "hom_xK"
 ],
 [
  "theorem",
  "sum_xK_sq"
 ],
 [
  "theorem",
  "sum_wK_sq"
 ],
 [
  "def",
  "entW"
 ],
 [
  "theorem",
  "pairVal_entW"
 ],
 [
  "theorem",
  "gRev_value"
 ],
 [
  "theorem",
  "gRev_not_mem_maxCone"
 ],
 [
  "theorem",
  "not_posFwd_gRev"
 ],
 [
  "theorem",
  "not_nativeGate_gRev"
 ]
]''')
TEXTS = json.loads(r'''{
 "oddK": "def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))",
 "oddK_rev": "theorem oddK_rev (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : oddK k (Fin.rev μ) = !oddK k μ",
 "cK": "def cK (k : ℕ) (j : Fin (2 * k + 1)) : ℝ := if oddK k j.succ then -1 else 1",
 "nK": "def nK (k : ℕ) : (Fin (2 * k + 1) → ℝ) →ₗ[ℝ] (Fin (2 * k + 1) → ℝ) := diagSign (cK k)",
 "zK": "def zK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 2 * k then 1 else 0",
 "gRev": "def gRev (k : ℕ) : W (2 * k + 1) ≃ₗ[ℝ] W (2 * k + 1) := sgateEquiv (oddK k) Fin.rev Fin.rev_rev",
 "gRev_apply": "theorem gRev_apply (k : ℕ) (ω : W (2 * k + 1)) : gRev k ω = sgate (oddK k) Fin.rev ω",
 "cK_sq": "theorem cK_sq (k : ℕ) (j : Fin (2 * k + 1)) : cK k j ^ 2 = 1",
 "homMap_nK_sign": "theorem homMap_nK_sign (k : ℕ) (v : HVec (2 * k + 1)) (μ : Fin (2 * k + 1 + 1)) :\n    homMap (nK k) v μ = (if oddK k μ then -1 else 1) * v μ",
 "sum_val_ite": "theorem sum_val_ite (n m : ℕ) (hm : m < n) (c : ℝ) :\n    ∑ j : Fin n, (if (j : ℕ) = m then c else 0) = c",
 "sum_zK_sq": "theorem sum_zK_sq (k : ℕ) : ∑ j, zK k j ^ 2 = 1",
 "isNot_nK": "theorem isNot_nK (k : ℕ) : IsNot (eball (2 * k + 1)) (zK k) (nK k)",
 "hom_smul_zK": "theorem hom_smul_zK (k : ℕ) (c : ℝ) (μ : Fin (2 * k + 1 + 1)) :\n    hom (c • zK k) μ = if (μ : ℕ) = 0 then 1 else if (μ : ℕ) = 2 * k + 1 then c else 0",
 "hom_zK": "theorem hom_zK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) :\n    hom (zK k) μ = if (μ : ℕ) = 0 then 1 else if (μ : ℕ) = 2 * k + 1 then 1 else 0",
 "gRev_frame_aux": "theorem gRev_frame_aux (k : ℕ) {s t : ℝ} (hs : s = 1 ∨ s = -1) {x y w : Fin (2 * k + 1) → ℝ}\n    (hx : x = s • zK k) (hy : y = t • zK k) (hw : w = (s * t) • zK k) :\n    gRev k (prodState x y) = prodState x w",
 "gRev_frame": "theorem gRev_frame (k : ℕ) (a b : Fin 2) :\n    gRev k (prodState (corner (zK k) a) (corner (zK k) b)) =\n      prodState (corner (zK k) a) (corner (zK k) (a + b))",
 "gateRel_gRev": "theorem gateRel_gRev (k : ℕ) : GateRel (nK k) (gRev k)",
 "finrank_plus_eq_finrank_minus_nK": "theorem finrank_plus_eq_finrank_minus_nK (k : ℕ) :\n    Module.finrank ℝ (plusSpace (nK k)) = Module.finrank ℝ (minusSpace (nK k))",
 "exists_frame_gateRel_iff_odd": "theorem exists_frame_gateRel_iff_odd (d : ℕ) :\n    (∃ (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n      IsNot (eball d) z N ∧\n        (∀ a b : Fin 2,\n          G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧\n        GateRel N G) ↔ Odd d",
 "xK": "def xK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 0 then 1 else 0",
 "wK": "noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i =>\n  if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0",
 "hom_xK": "theorem hom_xK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) :\n    hom (xK k) μ = if (μ : ℕ) = 0 then 1 else if (μ : ℕ) = 1 then 1 else 0",
 "sum_xK_sq": "theorem sum_xK_sq (k : ℕ) : ∑ j, xK k j ^ 2 = 1",
 "sum_wK_sq": "theorem sum_wK_sq (k : ℕ) (hk : 1 ≤ k) : ∑ j, wK k j ^ 2 = 1",
 "entW": "def entW (p q : Fin (d + 1)) : W d := fun μ ν => if μ = p then (if ν = q then 1 else 0) else 0",
 "pairVal_entW": "theorem pairVal_entW (a b : HVec d) (p q : Fin (d + 1)) : pairVal a b (entW p q) = a p * b q",
 "gRev_value": "theorem gRev_value (k : ℕ) (hk : 1 ≤ k) :\n    prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = -1 / 10",
 "gRev_not_mem_maxCone": "theorem gRev_not_mem_maxCone (k : ℕ) (hk : 1 ≤ k) :\n    gRev k (prodState (xK k) (zK k)) ∉ maxCone (eball (2 * k + 1))",
 "not_posFwd_gRev": "theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) :\n    ¬ ∀ x ∈ eball (2 * k + 1), ∀ y ∈ eball (2 * k + 1),\n      gRev k (prodState x y) ∈ maxCone (eball (2 * k + 1))",
 "not_nativeGate_gRev": "theorem not_nativeGate_gRev (k : ℕ) (hk : 1 ≤ k) :\n    ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.OddChar.oddK_rev",
 "OIBridge.OddChar.isNot_nK",
 "OIBridge.OddChar.gRev_frame",
 "OIBridge.OddChar.gateRel_gRev",
 "OIBridge.OddChar.finrank_plus_eq_finrank_minus_nK",
 "OIBridge.OddChar.exists_frame_gateRel_iff_odd",
 "OIBridge.OddChar.sum_wK_sq",
 "OIBridge.OddChar.pairVal_entW",
 "OIBridge.OddChar.gRev_value",
 "OIBridge.OddChar.gRev_not_mem_maxCone",
 "OIBridge.OddChar.not_posFwd_gRev",
 "OIBridge.OddChar.not_nativeGate_gRev"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.ParityNot\n\nnamespace OIBridge\nnamespace OddChar\n\nopen KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot\n\nvariable {d : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace OddChar",
 "open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot",
 "variable {d : ℕ}",
 "end OddChar",
 "end OIBridge"
]''')
LANDED = json.loads(r'''{
 "NativeGate#frame": "frame : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))",
 "NativeGate#posFwd": "posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω",
 "NativeGate#relT": "relT : ∀ ω, actT N (G (actT N ω)) = G ω",
 "NativeGate#relC": "relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "GateRel#fields": "relT relC",
 "GateRel#relT": "relT : ∀ ω, actT N (G (actT N ω)) = G ω",
 "GateRel#relC": "relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "sgate": "def sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1)) (ω : W d) : W d := fun μ ν => if odd ν then ω (p μ) ν else ω μ ν",
 "diagSign#toFun": "fun i => c i * x i",
 "sgate_relT": "{d : ℕ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool} {p : Fin (d + 1) → Fin (d + 1)} (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) * v μ) (ω : W d) : actT N (sgate odd p (actT N ω)) = sgate odd p ω",
 "sgate_relC": "{d : ℕ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool} {p : Fin (d + 1) → Fin (d + 1)} (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) * v μ) (hodd : ∀ μ, odd (p μ) = !odd μ) (ω : W d) : actC N (sgate odd p (actC N ω)) = actT N (sgate odd p ω)",
 "not_even_of_gateRel": "{d : ℕ} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d",
 "isNot_neg1": ": IsNot (eball 1) z1 neg1",
 "cnot1_frame": "(a b : Fin 2) : cnot1 (prodState (corner z1 a) (corner z1 b)) = prodState (corner z1 a) (corner z1 (a + b))",
 "nativeGate_cnot1": ": NativeGate (eball 1) z1 neg1 cnot1",
 "cnot1_relT": "(ω : W 1) : actT neg1 (cnot1 (actT neg1 ω)) = cnot1 ω",
 "cnot1_relC": "(ω : W 1) : actC neg1 (cnot1 (actC neg1 ω)) = actT neg1 (cnot1 ω)"
}''')
N_PRINTS = 12

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

IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def groups(b):
    """The top-level bracketed binder groups of a binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c in BINDER_OPEN:
            if depth == 0:
                start = i
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(norm(b[start:i + 1]))
                start = None
    return out


def group_names(g):
    """The bound names of a binder group (none for an anonymous instance group)."""
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """[(position, variable groups in scope, namespaces in scope, opened namespaces in scope)] at each declaration."""
    stack = [([], [], [])]
    out = {}
    lines = text.split('\n')
    pos = 0
    k = 0
    decl_at = {m.start(): m.group(2) for m in DECL.finditer(text)}
    while k < len(lines):
        line = lines[k]
        block = [line]
        j = k + 1
        if line.startswith('variable') or line.startswith('open '):
            while j < len(lines) and lines[j].startswith('  '):
                block.append(lines[j])
                j += 1
        whole = '\n'.join(block)
        m = re.match(r'^(namespace|section|noncomputable section)\b\s*(\S*)', line)
        if m:
            stack.append(([], [m.group(2)] if m.group(1) == 'namespace' else [], []))
        elif re.match(r'^end\b', line):
            if len(stack) > 1:
                stack.pop()
        elif line.startswith('variable'):
            stack[-1][0].extend(groups(whole[len('variable'):]))
        elif line.startswith('open '):
            stack[-1][2].extend(whole[len('open '):].split())
        if pos in decl_at:
            vs = [g for s in stack for g in s[0]]
            nss = [n for s in stack for n in s[1]]
            ops = [o for s in stack for o in s[2]]
            out[decl_at[pos]] = (vs, nss, ops)
        for l in block:
            pos += len(l) + 1
        k = j
    return out


def effective(text, name):
    """The effective statement of a declaration: the section variables its statement uses (closed under use by the
    included groups, an instance group included with a variable it mentions), in declared order, then its own binders
    and conclusion. None when the declaration is absent."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    vs = scopes_at(text).get(name, ([], [], []))[0]
    b, c = split_statement(stmt)
    used = norm(b) + ' : ' + norm(c)
    inc = [False] * len(vs)
    changed = True
    while changed:
        changed = False
        hay = used + ' ' + ' '.join(g for g, i in zip(vs, inc) if i)
        for n, g in enumerate(vs):
            if inc[n]:
                continue
            names = group_names(g)
            if names and any(token(x, hay) for x in names):
                inc[n] = True
                changed = True
            elif not names and g.startswith('[') and any(token(x, g) for gg, i in zip(vs, inc) if i
                                                          for x in group_names(gg)):
                inc[n] = True
                changed = True
    pre = ' '.join(g for g, i in zip(vs, inc) if i)
    return norm(pre + ' ' + norm(b) + ' : ' + norm(c))


_INV_CACHE = {}


def inventory(files):
    """{fully qualified name} of every declaration in the given module texts, with the namespaces they declare."""
    names, spaces = set(), set()
    for text in files:
        if text in _INV_CACHE:
            n, sp = _INV_CACHE[text]
            names |= n
            spaces |= sp
            continue
        n, sp = inventory_one(text)
        if len(_INV_CACHE) < 4096:
            _INV_CACHE[text] = (n, sp)
        names |= n
        spaces |= sp
    return names, spaces


def inventory_one(text):
    names, spaces = set(), set()
    for text in [text]:
        sc = scopes_at(text)
        for kind, name in decls(text):
            nss = sc.get(name, ([], [], []))[1]
            prefix = '.'.join(nss)
            names.add((prefix + '.' if prefix else '') + name)
            for i in range(1, len(nss) + 1):
                spaces.add('.'.join(nss[:i]))
    return names, spaces


def visible(nss, ops, spaces):
    """The namespaces whose members are in scope: every prefix of the current namespace, and each opened namespace,
    resolved against the current namespace prefixes when that names an OIBridge namespace."""
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
    """Index of the first colon at bracket depth 0 that is not part of `:=`."""
    depth = 0
    for j, c in enumerate(s):
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            return j
    return len(s)


def strip_binders(eff):
    """The identifiers of an effective statement, without the names it binds: the names of its binder groups and the
    names bound by `∃`, `∀` and `fun` in its conclusion."""
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]

PREFIX = 'OIBridge.OddChar.'
LANDED_GATE = ('CompositeDimension', 'NativeGate')
LANDED_REL = ('ParityNot', 'GateRel')
# the positivity-free sections read none of these
FREE_OF_POS = ('NativeGate', 'posFwd', 'posInv', 'maxCone', 'prodEffVal', 'IsEffectOn', 'sharpEff')
# S1 -- the family (whole normalized definition texts)
FAM_DEFS = {
    'oddK': 'def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))',
    'cK': 'def cK (k : ℕ) (j : Fin (2 * k + 1)) : ℝ := if oddK k j.succ then -1 else 1',
    'nK': 'def nK (k : ℕ) : (Fin (2 * k + 1) → ℝ) →ₗ[ℝ] (Fin (2 * k + 1) → ℝ) := diagSign (cK k)',
    'zK': 'def zK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 2 * k then 1 else 0',
    'gRev': 'def gRev (k : ℕ) : W (2 * k + 1) ≃ₗ[ℝ] W (2 * k + 1) := sgateEquiv (oddK k) Fin.rev Fin.rev_rev',
}
FRAME_SUB = {'G': 'gRev k', 'z': '(zK k)'}
FAM_THEOREMS = {
    'oddK_rev': ('(k : ℕ) (μ : Fin (2 * k + 1 + 1))', 'oddK k (Fin.rev μ) = !oddK k μ', ()),
    'isNot_nK': ('(k : ℕ)', 'IsNot (eball (2 * k + 1)) (zK k) (nK k)', ()),
    'gRev_frame': ('(k : ℕ) (a b : Fin 2)', None, ()),
    'gateRel_gRev': ('(k : ℕ)', 'GateRel (nK k) (gRev k)', ('sgate_relT', 'sgate_relC', 'oddK_rev')),
    'finrank_plus_eq_finrank_minus_nK': ('(k : ℕ)', 'Module.finrank ℝ (plusSpace (nK k)) = '
                                         'Module.finrank ℝ (minusSpace (nK k))', ('finrank_plus_eq_finrank_minus_rel',)),
}
# the landed ParityNot objects the family is built from, read from D
LANDED_SGATE = 'def sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1)) (ω : W d) : W d := ' \
               'fun μ ν => if odd ν then ω (p μ) ν else ω μ ν'
LANDED_DIAG = 'fun i => c i * x i'
LANDED_SGATE_REL = {
    'sgate_relT': '{d : ℕ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool} '
                  '{p : Fin (d + 1) → Fin (d + 1)} (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) '
                  '* v μ) (ω : W d) : actT N (sgate odd p (actT N ω)) = sgate odd p ω',
    'sgate_relC': '{d : ℕ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool} '
                  '{p : Fin (d + 1) → Fin (d + 1)} (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) '
                  '* v μ) (hodd : ∀ μ, odd (p μ) = !odd μ) (ω : W d) : '
                  'actC N (sgate odd p (actC N ω)) = actT N (sgate odd p ω)',
}
# S2 -- the characterization
ODD = 'exists_frame_gateRel_iff_odd'
ODD_BINDERS = '(d : ℕ)'
ODD_HEAD = '(∃ (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N ∧ ('
ODD_TAIL = ') ∧ GateRel N G) ↔ Odd d'
ODD_PROOF = ('not_even_of_gateRel', 'cnot1', 'isNot_neg1', 'cnot1_frame', 'gRev', 'isNot_nK', 'gRev_frame',
             'gateRel_gRev')
ODD_PROOF_D1_REL = (('nativeGate_cnot1',), ('cnot1_relT', 'cnot1_relC'))
LANDED_ODD = {
    'not_even_of_gateRel': '{d : ℕ} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
                           '(hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d',
    'isNot_neg1': ': IsNot (eball 1) z1 neg1',
    'nativeGate_cnot1': ': NativeGate (eball 1) z1 neg1 cnot1',
    'cnot1_relT': '(ω : W 1) : actT neg1 (cnot1 (actT neg1 ω)) = cnot1 ω',
    'cnot1_relC': '(ω : W 1) : actC neg1 (cnot1 (actC neg1 ω)) = actT neg1 (cnot1 ω)',
}
# S3 -- positivity at k >= 1
POS_DEFS = {
    'xK': 'def xK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 0 then 1 else 0',
    'wK': 'noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => '
          'if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0',
    'entW': 'def entW (p q : Fin (d + 1)) : W d := fun μ ν => if μ = p then (if ν = q then 1 else 0) else 0',
}
HK = '(k : ℕ) (hk : 1 ≤ k)'
BODY = 'eball (2 * k + 1)'
VALUE = '-1 / 10'
POS_THEOREMS = {
    'sum_wK_sq': (HK, '∑ j, wK k j ^ 2 = 1', ()),
    'pairVal_entW': ('(a b : HVec d) (p q : Fin (d + 1))', 'pairVal a b (entW p q) = a p * b q', ()),
    'gRev_value': (HK, 'prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = '
                   + VALUE, ()),
    'gRev_not_mem_maxCone': (HK, 'gRev k (prodState (xK k) (zK k)) ∉ maxCone (%s)' % BODY,
                             ('gRev_value', 'sharpEff_isEffectOn', 'sum_wK_sq', 'sum_zK_sq')),
    'not_posFwd_gRev': (HK, None, ('gRev_not_mem_maxCone',)),
    'not_nativeGate_gRev': (HK, '¬ NativeGate (%s) (zK k) (nK k) (gRev k)' % BODY, ('not_posFwd_gRev',)),
}
SELECTORS = re.compile(r'(?<![\w.\'])\w*_of_nativeGate\w*|(?<![\w.\'])three_of_\w+|(?<![\w.\'])dim_of_\w+')
# S6 -- scope
SCOPE_TOKENS = ('Complex', 'ℂ', 'posInv', 'Entangling', 'dim_of_nativeGate', 'ne_five_of_nativeGate',
                'three_of_nativeGate', 'dim_of_nativeGateOf', 'three_of_nativeGateOf',
                'three_of_nativeGateOf_of_two_le')
D_EQ = re.compile(r'(?<![\w.\'])d\s*(=|≠)\s*\d')
POSITIVE = re.compile(r'(?<![\w.\'])(NativeGate|maxCone|posFwd)(?![\w\'])')
# S7 -- reuse
IMPORT_ONLY = 'import OIBridge.ParityNot'
# S8 -- phrases
PHRASES = ('individually necessary', 'individually load-bearing', 'separately necessary', 'each necessary',
           'posFwd is necessary', 'posInv is necessary', 'forward positivity is necessary',
           'inverse positivity is necessary', 'forward positivity alone', 'inverse positivity alone',
           'posFwd alone', 'posInv alone', 'forward positivity excludes', 'inverse positivity excludes',
           'positivity selects', 'selects d = 3', 'selects `d = 3`', 'forces d = 3', 'forces `d = 3`',
           'd = 3 is forced', 'd = 3 is selected', 'selects the dimension', 'dimension selection',
           'the relations select', 'positive gates are classified', 'classifies the positive', 'classification of '
           'positive', 'only positive gate', 'relT is necessary', 'relC is necessary', 'the frame is necessary',
           'complex structure is', 'yields a complex structure', 'gives a complex structure', 'reconstructs ℂ',
           'reconstructs the complex', 'J² = −1', 'J^2 = -1', 'J² = -1', 'physically carried', 'physical NOT',
           'physically realizable', 'physically realized', 'positivity follows from', 'positivity is derived',
           'implies positivity', 'OI supplies', 'OI provides', 'derived from OI', 'sourced from OI',
           'premise adopted', 'adopts a premise', 'qubit', 'all odd dimensions', 'design (round', 'not for landing')
# V -- the frozen decision rule
FAM_TOKENS = ('ODD-FAMILY-PROVED', 'ODD-FAMILY-NOT-ESTABLISHED')
ODD_TOKENS = ('ODD-CHARACTERIZATION-PROVED', 'ODD-CHARACTERIZATION-NOT-ESTABLISHED')
POS_TOKENS = ('HIGHER-ODD-POSFWD-FAILURE-PROVED', 'HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED')
ALL_TOKENS = FAM_TOKENS + ODD_TOKENS + POS_TOKENS


def tsub(text, mapping):
    """Token-bounded simultaneous substitution."""
    pat = re.compile(r'(?<![\w.\'])(%s)(?![\w\'])' % '|'.join(re.escape(k) for k in mapping))
    return pat.sub(lambda m: mapping[m.group(1)], text)


def kinds_texts_proofs(mod):
    chunks = decl_chunks(mod)
    return ({n: k for n, (k, _, _) in chunks.items()}, {n: c for n, (_, c, _) in chunks.items()},
            {n: p for n, (_, _, p) in chunks.items()})


def section_decls(mod, labels):
    secs = sections(mod)
    return [(name, mod[start:nxt]) for kind, name, start, se, nxt, cend in spans(mod)
            if section_at(secs, start) in labels]


DOTTED = ('posFwd', 'posInv')


def mentions(text, toks):
    """The tokens the code of `text` mentions; a positivity field also as a projection (`hG.posInv`)."""
    c = code_only(text)
    return [t for t in toks if token(t, c) or (t in DOTTED and re.search(r'(?<![\w\'])%s(?![\w\'])' % t, c))]


def landed_field(landed, owner, f, prefix):
    v = landed.get('%s#%s' % (owner, f))
    return v[len(prefix):] if v is not None and v.startswith(prefix) else None


def landed_frame(landed):
    return landed_field(landed, LANDED_GATE[1], 'frame', 'frame : ')


def relations_bad(landed):
    """The landed GateRel is exactly the landed NativeGate relation fields (read from D)."""
    bad = []
    for f in ('relT', 'relC'):
        a = landed.get('%s#%s' % (LANDED_REL[1], f))
        if a is None or a != landed.get('%s#%s' % (LANDED_GATE[1], f)):
            bad.append('GateRel#' + f + ' at D')
    if landed.get('%s#fields' % LANDED_REL[1]) != 'relT relC':
        bad.append('GateRel fields at D')
    return bad


def theorem_bad(kinds, texts, proofs, n, b, c, deps):
    bb, cc = split_statement(texts.get(n, ''))
    return kinds.get(n) != 'theorem' or norm(bb) != norm(b) or c is None or norm(cc) != norm(c) or \
        not all(token(m, proofs.get(n, '')) for m in deps)


def family_bad(mod, landed):
    """S1: the frozen family definitions; IsNot, the landed frame field and GateRel for every k; the landed GateRel
    and sgate objects at D; §A free of the native gate and positivity."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, t in FAM_DEFS.items():
        if kinds.get(n) != 'def' or norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    frame = landed_frame(landed)
    if frame is None or not frame.startswith('∀ a b : Fin 2, '):
        return bad + ['NativeGate#frame at D']
    want_frame = tsub(frame[len('∀ a b : Fin 2, '):], FRAME_SUB)
    for n, (b, c, deps) in FAM_THEOREMS.items():
        if theorem_bad(kinds, texts, proofs, n, b, want_frame if c is None else c, deps):
            bad.append(n)
    bad += relations_bad(landed)
    if landed.get('sgate') != norm(LANDED_SGATE) or landed.get('diagSign#toFun') != LANDED_DIAG:
        bad.append('sgate or diagSign at D')
    for n, e in LANDED_SGATE_REL.items():
        if landed.get(n) != norm(e):
            bad.append(n + ' at D')
    for name, body in section_decls(mod, ('§A',)):
        if mentions(body, FREE_OF_POS):
            bad.append(name)
    return bad


def odd_want(landed):
    frame = landed_frame(landed)
    return None if frame is None else norm(ODD_HEAD + frame + ODD_TAIL)


def odd_bad(mod, landed):
    """S2: the frozen existential equivalent to `Odd d`, the frame clause the landed frame field read from D; the
    proof through the landed parity theorem, the landed d = 1 objects and the family; §B free of the native gate and
    positivity."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    want = odd_want(landed)
    b, c = split_statement(texts.get(ODD, ''))
    pr = proofs.get(ODD, '')
    if kinds.get(ODD) != 'theorem' or norm(b) != ODD_BINDERS or want is None or norm(c) != want or \
            not all(token(m, pr) for m in ODD_PROOF) or \
            not any(all(token(m, pr) for m in alt) for alt in ODD_PROOF_D1_REL):
        bad.append(ODD)
    bad += relations_bad(landed)
    for n, e in LANDED_ODD.items():
        if landed.get(n) != norm(e):
            bad.append(n + ' at D')
    f1 = landed.get('cnot1_frame')
    if f1 is None or want is None or f1 != norm('(a b : Fin 2) : ' + tsub(landed_frame(landed)[
            len('∀ a b : Fin 2, '):], {'G': 'cnot1', 'z': 'z1'})):
        bad.append('cnot1_frame at D')
    for name, body in section_decls(mod, ('§B',)):
        if mentions(body, FREE_OF_POS):
            bad.append(name)
    return bad


def positivity_bad(mod, landed):
    """S3: for k >= 1, the frozen witness, the value -1 / 10, the negation of the landed posFwd field at the body and
    the gate through that value; the gate the family's, with its frame and its relations; §C free of the landed
    dimension corollaries and inverse positivity."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n in ('oddK', 'zK', 'nK', 'gRev'):
        if kinds.get(n) != 'def' or norm(texts.get(n, '')) != norm(FAM_DEFS[n]):
            bad.append(n)
    for n, t in POS_DEFS.items():
        if norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    frame = landed_frame(landed)
    posfwd = landed_field(landed, LANDED_GATE[1], 'posFwd', 'posFwd : ')
    if frame is None or posfwd is None or not frame.startswith('∀ a b : Fin 2, '):
        return bad + ['NativeGate fields at D']
    want_pf = '¬ ' + tsub(posfwd, {'G': 'gRev k', 'Ω': '(%s)' % BODY}).replace('∈ (%s),' % BODY, '∈ %s,' % BODY)
    for n, (b, c, deps) in POS_THEOREMS.items():
        if theorem_bad(kinds, texts, proofs, n, b, want_pf if c is None else c, deps):
            bad.append(n)
    want_frame = tsub(frame[len('∀ a b : Fin 2, '):], FRAME_SUB)
    for n in ('gRev_frame', 'gateRel_gRev'):
        b, c, deps = FAM_THEOREMS[n]
        if theorem_bad(kinds, texts, proofs, n, b, want_frame if c is None else c, ()):
            bad.append(n)
    bad += relations_bad(landed)
    for name, body in section_decls(mod, ('§C',)):
        if SELECTORS.search(code_only(body)) or mentions(body, ('posInv',)):
            bad.append(name)
    return bad


def fam_cell(mod, landed):
    """ODD-FAMILY-PROVED iff S1: for every k, nK k is a NOT of eball (2k+1) with axis zK k, gRev k satisfies the
    landed frame field and GateRel (nK k) (gRev k), the landed GateRel being the landed relation fields, and §A reads
    neither the native gate nor positivity. Otherwise ODD-FAMILY-NOT-ESTABLISHED. Reads no §B-§C statement."""
    return [FAM_TOKENS[1] if family_bad(mod, landed) else FAM_TOKENS[0]]


def odd_cell(mod, landed):
    """ODD-CHARACTERIZATION-PROVED iff S2: the existential of IsNot, the landed frame field and GateRel is
    equivalent to Odd d, proved through the landed parity theorem one way and the landed d = 1 gate and the family the
    other. Otherwise ODD-CHARACTERIZATION-NOT-ESTABLISHED. Reads no §C statement."""
    return [ODD_TOKENS[1] if odd_bad(mod, landed) else ODD_TOKENS[0]]


def pos_cell(mod, landed):
    """HIGHER-ODD-POSFWD-FAILURE-PROVED iff S3: for every k >= 1 the family's gate with its frame and relations
    fails the landed posFwd field at eball (2k+1), through the explicit value -1 / 10, without a landed dimension
    corollary. Otherwise HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED. Reads no §B statement."""
    return [POS_TOKENS[1] if positivity_bad(mod, landed) else POS_TOKENS[0]]


def verdicts(mod, landed):
    return fam_cell(mod, landed), odd_cell(mod, landed), pos_cell(mod, landed)


def semantic_checks(mod, chunks, prints, tag, landed, inv_files):
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad1 = family_bad(mod, landed)
    check('S1', 'the family: IsNot, the landed frame field and GateRel for every k; §A free of the native gate and '
                'positivity%s%s' % (tag, (' %s' % bad1[:3]) if bad1 else ''), not bad1)
    bad2 = odd_bad(mod, landed)
    check('S2', 'IsNot, the landed frame field and GateRel exist exactly at odd d, through the landed parity theorem '
                'and the landed d = 1 gate%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    bad3 = positivity_bad(mod, landed)
    check('S3', 'for k >= 1 the family gate fails the landed posFwd field through the value -1 / 10%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    bad6 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        if mentions(mod[start:nxt], SCOPE_TOKENS):
            bad6.append(name)
        if kind in ('theorem', 'lemma'):
            _, c = split_statement(texts.get(name, ''))
            c = norm(c)
            if D_EQ.search(c) or (POSITIVE.search(c) and not c.startswith('¬') and '∉' not in c):
                bad6.append(name)
    check('S6', 'no complex field, dimension selector, inverse positivity or Entangling; no conclusion on d; no '
                'positive gate conclusion%s%s' % (tag, (' %s' % bad6[:3]) if bad6 else ''), not bad6)
    names, spaces = inventory(inv_files + [mod])
    others = inventory(inv_files)[0]
    msc = scopes_at(mod)
    clash = []
    for kind, name in decls(mod):
        sc = msc.get(name, ([], [], []))
        if resolve(name, visible(sc[1], sc[2], spaces), others):
            clash.append(name)
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S7', 'no declaration shares a name with a visible OIBridge declaration; the only import is '
                'OIBridge.ParityNot%s%s' % (tag, (' %s' % clash[:3]) if clash else ''),
          not clash and imports == [IMPORT_ONLY])
    ph = phrase_hits(header(mod))
    check('S8', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    local = {n for _, n in decls(mod)}
    pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(pnames) == N_PRINTS
          and all(n in local for n in pnames))
    a, b, c = verdicts(mod, landed)
    check('V', 'one outcome per cell by the frozen rules: %s, %s, %s%s' % (a, b, c, tag),
          len(a) == 1 and len(b) == 1 and len(c) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ALL_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


_INV = []


def d_inventory_files():
    """Every OIBridge module at D (read once)."""
    if not _INV:
        r = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in r.stdout.split() if p.endswith('.lean'))
    return list(_INV)


def module_checks(mod, tag='', landed=None, inv_files=None):
    if landed is None:
        landed = LANDED
    if inv_files is None:
        inv_files = d_inventory_files()
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
    semantic_checks(mod, chunks, prints, tag, landed, inv_files)


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


def landed_texts(show_d):
    """The landed texts the rules read, from D: NativeGate's fields, GateRel's fields, sgate, diagSign's map, the
    sgate relation lemmas, the parity theorem and the d = 1 objects, as effective statements."""
    out = {}
    cd = show_d(LEAN + LANDED_GATE[0] + '.lean')
    pn = show_d(LEAN + LANDED_REL[0] + '.lean')
    if not cd or not pn:
        return out
    ch = decl_chunks(cd).get(LANDED_GATE[1])
    if ch and ch[0] == 'structure':
        for f in ('frame', 'posFwd', 'relT', 'relC'):
            v = field_line(ch[1], f)
            if v is not None:
                out['%s#%s' % (LANDED_GATE[1], f)] = v
    pch = decl_chunks(pn)
    ch = pch.get(LANDED_REL[1])
    if ch and ch[0] == 'structure':
        out['%s#fields' % LANDED_REL[1]] = ' '.join(fields(ch[1]))
        for f in ('relT', 'relC'):
            v = field_line(ch[1], f)
            if v is not None:
                out['%s#%s' % (LANDED_REL[1], f)] = v
    if 'sgate' in pch and pch['sgate'][0] == 'def':
        out['sgate'] = norm(pch['sgate'][1])
    if 'diagSign' in pch and 'toFun x :=' in pch['diagSign'][1]:
        out['diagSign#toFun'] = norm(pch['diagSign'][1].split('toFun x :=', 1)[1].split('\n')[0])
    for n in list(LANDED_SGATE_REL) + ['not_even_of_gateRel']:
        e = effective(pn, n)
        if e is not None:
            out[n] = e
    for n in ('isNot_neg1', 'cnot1_frame', 'nativeGate_cnot1', 'cnot1_relT', 'cnot1_relC'):
        e = effective(cd, n)
        if e is not None:
            out[n] = e
    return out


def landed_at_d():
    return landed_texts(lambda p: show(D, p))


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    landed = landed_at_d()
    check('L', 'the landed texts read from D are the frozen ones', landed == LANDED)
    mod = show(commit, MOD)
    module_checks(mod, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S8', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b + c, toks), len(a) == 1 and len(b) == 1 and len(c) == 1 and sorted(toks) == sorted(a + b + c))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the PARITY-NOT-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    landed = landed_at_d()
    a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
    print('VERDICT  FAM  %s' % ('/'.join(a) or 'none'))
    print('VERDICT  ODD  %s' % ('/'.join(b) or 'none'))
    print('VERDICT  POS  %s' % ('/'.join(c) or 'none'))
    check('V', 'the landed texts read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1 and len(c) == 1)

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


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def append_end(text, decl):
    """Insert a declaration at the end of §C, before `end OddChar`."""
    return replace_once(text, '\nend OddChar\n', '\n' + decl + '\n\nend OddChar\n')


def verdict_of(mod2, landed=None):
    return verdicts(mod2, LANDED if landed is None else landed)

ODDK_DEF = 'def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))'
FRAME_HEAD = ('theorem gRev_frame (k : ℕ) (a b : Fin 2) :\n'
              '    gRev k (prodState (corner (zK k) a) (corner (zK k) b)) =\n'
              '      prodState (corner (zK k) a) (corner (zK k) (a + b)) := by')
REL_HEAD = 'theorem gateRel_gRev (k : ℕ) : GateRel (nK k) (gRev k) :='
ISNOT_HEAD = 'theorem isNot_nK (k : ℕ) : IsNot (eball (2 * k + 1)) (zK k) (nK k) where'
SECA_PROOF = '  have hμ := μ.isLt\n    have hν := ν.isLt\n    have hr : ((Fin.rev μ : Fin (2 * k + 1 + 1)) : ℕ) = ' \
             '2 * k + 1 - μ := by\n      rw [Fin.val_rev]; omega\n    simp only [gRev_apply, sgate, prodState_apply, ' \
             'hom_smul_zK'
ODD_FRAME = ('      IsNot (eball d) z N ∧\n'
             '        (∀ a b : Fin 2,\n'
             '          G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧\n'
             '        GateRel N G) ↔ Odd d := by')
ODD_D1 = '      exact ⟨z1, neg1, cnot1, isNot_neg1, cnot1_frame, gateRel_of_nativeGate nativeGate_cnot1⟩'
ODD_FWD = '    exact Nat.not_even_iff_odd.mp (not_even_of_gateRel hN hR)'
VALUE_HEAD = ('theorem gRev_value (k : ℕ) (hk : 1 ≤ k) :\n'
              '    prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = -1 / 10 := by')
WK_DEF = ('noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i =>\n'
          '  if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0')
PF = ('theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
      '    ¬ ∀ x ∈ eball (2 * k + 1), ∀ y ∈ eball (2 * k + 1),\n'
      '      gRev k (prodState x y) ∈ maxCone (eball (2 * k + 1)) :=\n'
      '  fun h => gRev_not_mem_maxCone k hk\n'
      '    (h _ (mem_eball_of_sphere (sum_xK_sq k)) _ (mem_eball_of_sphere (sum_zK_sq k)))')
NG = ('theorem not_nativeGate_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
      '    ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k) :=\n'
      '  fun hG => not_posFwd_gRev k hk hG.posFwd')
NOTE_OK = ('The frame and both relations admit exactly the odd dimensions. For every odd dimension at least 3, an '
           'explicit member of this family fails forward positivity. Combined with DIM-1, the positivity assumptions '
           'are therefore collectively load-bearing for excluding the higher odd dimensions.')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    landed = landed_at_d()
    check('T', 'the landed texts read from D are the frozen ones', landed == LANDED and len(LANDED) == 17)
    module_checks(mod, ' [reference]')
    a, b, c = verdict_of(mod)
    check('T', 'the reference module reads %s, %s and %s' % (a, b, c),
          a == [FAM_TOKENS[0]] and b == [ODD_TOKENS[0]] and c == [POS_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem sum_xK_sq ', '\ntheorem sum_xK_sq\' '))
    must_fail('N2', 'a changed binder context', replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {m : ℕ}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, 'CompositeDimension EffectSpace ParityNot\n',
                                                       'CompositeDimension EffectSpace\n'))
    must_fail('N3', 'a sorry', append_end(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.OddChar.gRev_value\n', ''))
    # S1 -- the family
    must_fail('S1', 'the sign classes changed', replace_once(mod, ODDK_DEF, ODDK_DEF.replace('k <', 'k ≤')))
    must_fail('S1', 'the frame changed', replace_once(mod, FRAME_HEAD, FRAME_HEAD.replace('(zK k) (a + b))', '(zK k) b)')))
    must_fail('S1', 'the relations weakened to the target relation',
              replace_once(mod, REL_HEAD, REL_HEAD.replace('GateRel (nK k) (gRev k)',
                                                           '∀ ω, actT (nK k) (gRev k (actT (nK k) ω)) = gRev k ω')))
    must_fail('S1', 'the NOT with another axis',
              replace_once(mod, ISNOT_HEAD, ISNOT_HEAD.replace('(zK k) (nK k)', '(xK k) (nK k)')))
    must_fail('S1', 'a §A proof reading positivity',
              replace_once(mod, SECA_PROOF, SECA_PROOF.replace(
                  '  have hμ := μ.isLt', '  have _hp : maxCone (eball 1) = maxCone (eball 1) := rfl\n    have hμ := μ.isLt')))
    m = replace_once(mod, FRAME_HEAD, FRAME_HEAD.replace('(zK k) (a + b))', '(zK k) b)'))
    check('M', 'decision rule: a broken family frame reads ODD-FAMILY-NOT-ESTABLISHED and '
               'HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED and leaves the characterization',
          verdict_of(m) == ([FAM_TOKENS[1]], [ODD_TOKENS[0]], [POS_TOKENS[1]]))
    m = replace_once(mod, ISNOT_HEAD, ISNOT_HEAD.replace('(zK k) (nK k)', '(xK k) (nK k)'))
    check('M', 'decision rule: a broken NOT reads ODD-FAMILY-NOT-ESTABLISHED and leaves the other cells',
          verdict_of(m) == ([FAM_TOKENS[1]], [ODD_TOKENS[0]], [POS_TOKENS[0]]))
    lm = dict(LANDED)
    lm['GateRel#relC'] = lm['GateRel#relC'].replace('actT N (G ω)', 'G ω')
    check('M', 'relations: a landed GateRel that differs from the landed NativeGate relations fails all three cells',
          verdict_of(mod, lm) == ([FAM_TOKENS[1]], [ODD_TOKENS[1]], [POS_TOKENS[1]]))
    lm = dict(LANDED)
    lm['sgate_relC'] = lm['sgate_relC'].replace('(hodd : ∀ μ, odd (p μ) = !odd μ) ', '')
    check('M', 'family: a landed sgate relation lemma that differs fails only the family cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[1]], [ODD_TOKENS[0]], [POS_TOKENS[0]]))
    # S2 -- the characterization
    must_fail('S2', 'the frame dropped from the existential',
              replace_once(mod, ODD_FRAME, ODD_FRAME.replace(
                  '        (∀ a b : Fin 2,\n'
                  '          G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧\n', '')))
    must_fail('S2', 'forward positivity added to the existential',
              replace_once(mod, ODD_FRAME, ODD_FRAME.replace(
                  '        GateRel N G) ↔', '        GateRel N G ∧ (∀ x ∈ eball d, ∀ y ∈ eball d, '
                                             'G (prodState x y) ∈ maxCone (eball d))) ↔')))
    must_fail('S2', 'the equivalence weakened to one direction',
              replace_once(mod, ODD_FRAME, ODD_FRAME.replace('GateRel N G) ↔ Odd d', 'GateRel N G) → Odd d')))
    must_fail('S2', 'the right side strengthened', replace_once(mod, ODD_FRAME, ODD_FRAME.replace('↔ Odd d', '↔ Odd d ∧ 3 ≤ d')))
    must_fail('S2', 'd = 1 through gRev 0 instead of the landed cnot1',
              replace_once(mod, ODD_D1, '      exact ⟨zK 0, nK 0, gRev 0, isNot_nK 0, gRev_frame 0, gateRel_gRev 0⟩'))
    must_fail('S2', 'the forward direction not through the landed parity theorem',
              replace_once(mod, ODD_FWD, '    exact Nat.not_even_iff_odd.mp (fun h => absurd h sorry)'))
    m = replace_once(mod, ODD_FRAME, ODD_FRAME.replace('GateRel N G) ↔ Odd d', 'GateRel N G) → Odd d'))
    check('M', 'decision rule: a broken characterization reads ODD-CHARACTERIZATION-NOT-ESTABLISHED and leaves the '
               'other cells', verdict_of(m) == ([FAM_TOKENS[0]], [ODD_TOKENS[1]], [POS_TOKENS[0]]))
    lm = dict(LANDED)
    lm['not_even_of_gateRel'] = lm['not_even_of_gateRel'].replace('¬ Even d', 'Odd d')
    check('M', 'characterization: a landed parity theorem that differs fails only the characterization cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[0]], [ODD_TOKENS[1]], [POS_TOKENS[0]]))
    lm = dict(LANDED)
    lm['cnot1_frame'] = lm['cnot1_frame'].replace('(corner z1 (a + b))', '(corner z1 b)')
    check('M', 'characterization: a landed d = 1 frame that differs fails only the characterization cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[0]], [ODD_TOKENS[1]], [POS_TOKENS[0]]))
    # S3 -- positivity at k >= 1
    must_fail('S3', 'the value changed to a sign', replace_once(mod, VALUE_HEAD, VALUE_HEAD.replace('= -1 / 10', '< 0')))
    must_fail('S3', 'the witness direction changed', replace_once(mod, WK_DEF, WK_DEF.replace('-4 / 5', '4 / 5')))
    must_fail('S3', 'the positivity failure weakened to one input',
              replace_once(mod, PF, 'theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
                                    '    ¬ gRev k (prodState (xK k) (zK k)) ∈ maxCone (eball (2 * k + 1)) :=\n'
                                    '  gRev_not_mem_maxCone k hk'))
    must_fail('S3', 'the range k >= 1 dropped',
              replace_once(mod, VALUE_HEAD, VALUE_HEAD.replace('(k : ℕ) (hk : 1 ≤ k)', '(k : ℕ)')))
    must_fail('S3', 'the failure read from a landed dimension corollary',
              replace_once(mod, NG, 'theorem not_nativeGate_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
                                    '    ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k) :=\n'
                                    '  fun hG => by have := dim_of_nativeGate (isNot_nK k) hG; omega'))
    m = replace_once(mod, VALUE_HEAD, VALUE_HEAD.replace('= -1 / 10', '< 0'))
    check('M', 'decision rule: a broken value reads HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED and leaves the other '
               'cells', verdict_of(m) == ([FAM_TOKENS[0]], [ODD_TOKENS[0]], [POS_TOKENS[1]]))
    lm = dict(LANDED)
    lm['NativeGate#posFwd'] = lm['NativeGate#posFwd'].replace('maxCone Ω', 'jointStates Ω')
    check('M', 'positivity: a landed posFwd that differs fails only the positivity cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[0]], [ODD_TOKENS[0]], [POS_TOKENS[1]]))
    lm = dict(LANDED)
    lm['NativeGate#frame'] = lm['NativeGate#frame'].replace('(corner z (a + b))', '(corner z b)')
    check('M', 'frame: a landed frame field that differs fails all three cells',
          verdict_of(mod, lm) == ([FAM_TOKENS[1]], [ODD_TOKENS[1]], [POS_TOKENS[1]]))
    # S6 -- scope
    must_fail('S6', 'inverse positivity read as a projection',
              append_end(mod, 'theorem inv_pos (k : ℕ) (hG : NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k)) :\n'
                              '    True := by have := hG.posInv; trivial'))
    must_fail('S6', 'a dimension conclusion', append_end(mod, 'theorem d_sel {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} '
                                                           '{G : W d ≃ₗ[ℝ] W d} (h : GateRel N G) : d ≠ 2 := sorry'))
    must_fail('S6', 'a positive native gate', append_end(mod, 'theorem pos_gate : NativeGate (eball 3) (zK 1) (nK 1) '
                                                            '(gRev 1) := sorry'))
    must_fail('S6', 'a complex field', append_end(mod, 'theorem cplx : (Complex.I : ℂ) = Complex.I := rfl'))
    # S7 -- reuse
    must_fail('S7', 'a landed definition re-declared', append_end(mod, 'def sgate : ℕ := 0'))
    must_fail('S7', 'a second import',
              replace_once(mod, 'import OIBridge.ParityNot\n', 'import OIBridge.ParityNot\nimport OIBridge.K2Guard\n'))
    # S8 -- phrases
    must_fail('S8', 'a forbidden phrase in the header',
              replace_once(mod, '  (C) Positivity.', '  Forward positivity is individually necessary. (C) Positivity.'))
    must_fail('S8', 'the design header', replace_once(mod, 'round ODD-CHAR-1:', 'design (round ODD-CHAR-1, not for landing):'))
    check('M', 'the result-note phrase test passes the frozen wording and fails each individual-necessity claim',
          not phrase_hits(NOTE_OK)
          and phrase_hits('Hence posFwd is necessary.') == ['posFwd is necessary']
          and phrase_hits('so inverse positivity alone\nexcludes them') == ['inverse positivity alone']
          and phrase_hits('Each of posFwd and posInv is individually necessary.') == ['individually necessary'])
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.OddChar.not_nativeGate_gRev\n',
                           '#print axioms OIBridge.OddChar.not_nativeGate_gRev\n'
                           '#print axioms OIBridge.OddChar.sum_xK_sq\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.OddChar.gRev_value\n',
                           '#print axioms OIBridge.OddChar.gRev_value\n#print axioms OIBridge.OddChar.gRev_value\n'))
    # V
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('ODD-FAMILY-PROVED, ODD-CHARACTERIZATION-PROVED and HIGHER-ODD-POSFWD-FAILURE-PROVED.')
          == ['ODD-FAMILY-PROVED', 'ODD-CHARACTERIZATION-PROVED', 'HIGHER-ODD-POSFWD-FAILURE-PROVED']
          and note_tokens('HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED') == ['HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED'])
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
