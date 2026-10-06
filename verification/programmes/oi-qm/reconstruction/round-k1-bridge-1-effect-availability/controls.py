#!/usr/bin/env python3
"""controls.py -- round K1-BRIDGE-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the verdict computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition and structure
                  is the frozen text whole; the preamble and every context block is the frozen text, in order -- a
                  proof may change, a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  relative    `NativeGateOf` is DIM-1's `NativeGate` with `maxConeOf avail` in exactly the two positivity clauses
                  and the frame and the two NOT relations unchanged; `jointStatesOf` and `EntanglingOf` are DIM-1's
                  `jointStates` and `Entangling` with the family's cone; the three are the frozen texts whole
  S2  selectors   `dim_of_nativeGateOf` and `three_of_nativeGateOf` are theorems whose explicit binders are exactly
                  `0 < d`, effect soundness, the four hypotheses, `IsNot` and `NativeGateOf` (and `EntanglingOf` for
                  the second), with the frozen conclusions, and no `MixingClosed`, `unitEff`, `fullEffects` or
                  `sharpFamily` token in their statements
  S3  transparent each selector's proof names EFF-1's `maxConeOf_avail_eq` (through `nativeGate_of_avail`) and DIM-1's
                  landed selector by name; no declaration of the module mentions an eigenspace, a parity, a finrank,
                  a block, a tangent or a corner slice: no new dimension argument
  S4  premises    no theorem concludes `SharpSeed`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`,
                  `EffectsOn`, `IsNot`, `NativeGateOf`, `EntanglingOf` or `MixingClosed` of a hypothesis-bound object;
                  `EffectsOn` is concluded only of the named control family `axisFamily` by `cone_eq_fails_axis` and
                  the verdict; `NativeGate` and `Entangling` are concluded only from `NativeGateOf` and `EntanglingOf`
  S5  reuse       no declaration shares a name with a landed object it reads; the only import is `OIBridge.EffectSpace`
  S6  neutral     no complex, matrix-trace, qubit, Bloch, Pauli, density, drive, flow, limit-closure or tensor-product
                  token; no `MixingClosed` or `unitSpan` token anywhere in the module's code
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  dimension   `0 < d` occurs in exactly the frozen set of statements; outside the control section and the verdict
                  no dimension-three object occurs
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdict     the verdict is computed from the module's statements by the frozen rule; at a commit carrying the
                  result note, the note states exactly the computed outcome token and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.EffectSpace`
  C   census      the census is D's with exactly the frozen family inserted after the EFF-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '20aa54803df5d74e6c67a1341ca022dee340a65b'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/K1Bridge.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '835e801dd8a49635f152dac4b0f65abaa6fcfef9'
ANCHOR_IMPORT = 'import OIBridge.EffectSpace\n'
NEW_IMPORT = 'import OIBridge.K1Bridge\n'
PREV_FAMILY_MODULES = ['EffectSpace']
CENSUS_FAMILY = json.loads(r'''{
 "name": "DIM-1's dimension selectors relative to a family of available test functionals: for every d >= 1, effect soundness with body preservation, K∞-Seed, K∞-Trans and K∞-V4 carry the native-gate and entangling hypotheses stated on the available family's product cone to DIM-1's, so d in {1, 3} and, with the entangling clause, d = 3 (round K1-BRIDGE-1, reconstruction)",
 "modules": [
  "K1Bridge"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round K1-BRIDGE-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/preregistration.md. NativeGateOf Ω avail z N T is DIM-1's NativeGate with maxCone Ω replaced by maxConeOf avail in the two positivity clauses; EntanglingOf Ω avail T is Entangling with the joint states of maxConeOf avail. The cone equality carries the relative hypotheses to DIM-1's (nativeGate_of_cone_eq, entangling_of_cone_eq), and on eball d, 0 < d, EffectsOn (eball d) avail with OG-1's four named hypotheses (PreservesBody, SharpSeed, BoundaryTransitive, SeedOrbitAvailable; in the ROADMAP's labels body preservation, K∞-Seed, K∞-Trans and K∞-V4) give that equality by EFF-1's maxConeOf_avail_eq, so the relative selectors dim_of_nativeGateOf (d = 1 or d = 3) and three_of_nativeGateOf (d = 3) are EFF-1's cone equality, the transport and DIM-1's dim_of_nativeGate and three_of_nativeGate, with no new dimension argument and no mixing closure or unit premise. Controls carried from EFF-1: at d = 0 the cone equality fails (cone_eq_fails_zero); at d = 3 the one-axis family with the unit consists of effects and its cone is not maxCone (eball 3) (cone_eq_fails_axis). The verdict is k1b_core. Carried by no manuscript. Nothing here sources effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, IsNot or the relative native-gate and entangling hypotheses; the product form of the composite tests (DIM-1's carrier W d) is a premise of both rounds and is not addressed; nothing here concerns K2, K∞-Stage, K∞-Act, K∞-Drive, K∞-Copy, K∞-Geom, Kₙ or K3."
}''')
DECLS = json.loads(r'''[
 [
  "structure",
  "NativeGateOf"
 ],
 [
  "def",
  "jointStatesOf"
 ],
 [
  "def",
  "EntanglingOf"
 ],
 [
  "theorem",
  "nativeGate_of_cone_eq"
 ],
 [
  "theorem",
  "jointStatesOf_eq"
 ],
 [
  "theorem",
  "entangling_of_cone_eq"
 ],
 [
  "theorem",
  "nativeGate_of_avail"
 ],
 [
  "theorem",
  "entangling_of_avail"
 ],
 [
  "theorem",
  "dim_of_nativeGateOf"
 ],
 [
  "theorem",
  "three_of_nativeGateOf"
 ],
 [
  "theorem",
  "cone_eq_fails_zero"
 ],
 [
  "theorem",
  "cone_eq_fails_axis"
 ],
 [
  "theorem",
  "k1b_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "NativeGateOf": "structure NativeGateOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ)\n    (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop where\n  frame : ∀ a b : Fin 2,\n    T (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))\n  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail\n  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail\n  relT : ∀ ω, actT N (T (actT N ω)) = T ω\n  relC : ∀ ω, actC N (T (actC N ω)) = actT N (T ω)",
 "jointStatesOf": "def jointStatesOf (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set (W d) :=\n  {ω | ω ∈ maxConeOf avail ∧ ω 0 0 = 1}",
 "EntanglingOf": "def EntanglingOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ))\n    (T : W d ≃ₗ[ℝ] W d) : Prop :=\n  ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ,\n    T (prodState x y) ∈ (jointStatesOf avail).extremePoints ℝ ∧ ¬ IsProduct Ω (T (prodState x y))",
 "nativeGate_of_cone_eq": "theorem nativeGate_of_cone_eq {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (h : maxConeOf avail = maxCone Ω) (hT : NativeGateOf Ω avail z N T) :\n    NativeGate Ω z N T",
 "jointStatesOf_eq": "theorem jointStatesOf_eq {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n    (h : maxConeOf avail = maxCone Ω) : jointStatesOf avail = jointStates Ω",
 "entangling_of_cone_eq": "theorem entangling_of_cone_eq {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n    {T : W d ≃ₗ[ℝ] W d} (h : maxConeOf avail = maxCone Ω) (hE : EntanglingOf Ω avail T) :\n    Entangling Ω T",
 "nativeGate_of_avail": "theorem nativeGate_of_avail (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hT : NativeGateOf (eball d) avail z N T) : NativeGate (eball d) z N T",
 "entangling_of_avail": "theorem entangling_of_avail (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T",
 "dim_of_nativeGateOf": "theorem dim_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3",
 "three_of_nativeGateOf": "theorem three_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)\n    (hEnt : EntanglingOf (eball d) avail T) : d = 3",
 "cone_eq_fails_zero": "theorem cone_eq_fails_zero : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0)",
 "cone_eq_fails_axis": "theorem cone_eq_fails_axis : EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)",
 "k1b_core": "theorem k1b_core :\n    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n        (T : W d ≃ₗ[ℝ] W d), 0 < d → EffectsOn (eball d) avail → PreservesBody (eball d) G →\n        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →\n        IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → d = 1 ∨ d = 3) ∧\n    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n        (T : W d ≃ₗ[ℝ] W d), 0 < d → EffectsOn (eball d) avail → PreservesBody (eball d) G →\n        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →\n        IsNot (eball d) z N → NativeGateOf (eball d) avail z N T →\n        EntanglingOf (eball d) avail T → d = 3) ∧\n    maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) ∧\n    (EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3))"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.K1Bridge.nativeGate_of_cone_eq",
 "OIBridge.K1Bridge.jointStatesOf_eq",
 "OIBridge.K1Bridge.entangling_of_cone_eq",
 "OIBridge.K1Bridge.nativeGate_of_avail",
 "OIBridge.K1Bridge.entangling_of_avail",
 "OIBridge.K1Bridge.dim_of_nativeGateOf",
 "OIBridge.K1Bridge.three_of_nativeGateOf",
 "OIBridge.K1Bridge.cone_eq_fails_zero",
 "OIBridge.K1Bridge.cone_eq_fails_axis",
 "OIBridge.K1Bridge.k1b_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.EffectSpace\n\nnamespace OIBridge\nnamespace K1Bridge\n\nopen Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface\nopen EffectSpace\n\nvariable {d : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace K1Bridge",
 "open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface",
 "open EffectSpace",
 "variable {d : ℕ}",
 "section Bridge",
 "variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}",
 "end Bridge",
 "end K1Bridge",
 "end OIBridge"
]''')
N_PRINTS = 10
# DIM-1's `NativeGate` and `Entangling` at D, the texts the relative forms are compared against (S1)
DIM1_NATIVEGATE = json.loads(r'''"structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n    (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame : ∀ a b : Fin 2,\n    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))\n  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω\n  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n  relT : ∀ ω, actT N (G (actT N ω)) = G ω\n  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)"''')
DIM1_ENTANGLING = json.loads(r'''"def Entangling (Ω : Set (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop :=\n  ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ,\n    G (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧ ¬ IsProduct Ω (G (prodState x y))"''')
DIM1_JOINTSTATES = json.loads(r'''"def jointStates (Ω : Set (Fin d → ℝ)) : Set (W d) :=\n  {ω | ω ∈ maxCone Ω ∧ ω 0 0 = 1}"''')

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

PREFIX = 'OIBridge.K1Bridge.'
# OG-1's four named hypotheses, as they bind in the module (G, r, avail from the section `variable`)
OG4 = ('(hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) '
       '(hV4 : SeedOrbitAvailable G r avail)')
HD = '(hd : 0 < d)'
HE = '(hE : EffectsOn (eball d) avail)'
HN = '(hN : IsNot (eball d) z N)'
HT = '(hT : NativeGateOf (eball d) avail z N T)'
HENT = '(hEnt : EntanglingOf (eball d) avail T)'
SEL_BINDERS = HD + ' ' + HE + ' ' + OG4 + ' ' + HN + ' ' + HT
DIM_CONCL = 'd = 1 ∨ d = 3'
THREE_CONCL = 'd = 3'
SELECTORS = {'dim_of_nativeGateOf': (SEL_BINDERS, DIM_CONCL),
             'three_of_nativeGateOf': (SEL_BINDERS + ' ' + HENT, THREE_CONCL)}
SEL_FORBIDDEN = ('MixingClosed', 'unitEff', 'fullEffects', 'sharpFamily', 'unitSpan')
# S1 -- the relative forms
NG_FIELDS = ['frame', 'posFwd', 'posInv', 'relT', 'relC']
CONE_FIELDS = ('posFwd', 'posInv')
G_TO_T = re.compile(r"(?<![\w.'])G(?![\w'])")
JOINT_BODY = '{ω | ω ∈ maxConeOf avail ∧ ω 0 0 = 1}'
# S3 -- transparent composition
TRANSPARENT = {
    'nativeGate_of_avail': ('maxConeOf_avail_eq', 'nativeGate_of_cone_eq'),
    'entangling_of_avail': ('maxConeOf_avail_eq', 'entangling_of_cone_eq'),
    'dim_of_nativeGateOf': ('dim_of_nativeGate', 'nativeGate_of_avail'),
    'three_of_nativeGateOf': ('three_of_nativeGate', 'nativeGate_of_avail', 'entangling_of_avail'),
}
DIM_ARGUMENT_TOKENS = ('finrank', 'plusSpace', 'minusSpace', 'tangentPlus', 'BlockData', 'blockData_of_nativeGate',
                       'p_le_one_of_blockData', 'finrank_plus_eq_finrank_minus', 'not_even_of_nativeGate', 'Even',
                       'Odd', 'lor_face', 'corner_form', 'gate_corner', 'gt_corner', 'Phi', 'NativeGateBall',
                       'eigenspace', 'parity', 'not_entangling_one', 'omega')
# S4 -- premises concluded only of named witnesses
PREMISES = ('SharpSeed', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable', 'EffectsOn', 'IsNot',
            'NativeGateOf', 'EntanglingOf', 'MixingClosed')
AXIS_CONCL = 'EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)'
ZERO_CONCL = 'maxConeOf (sharpFamily 0) ≠ maxCone (eball 0)'
WITNESS_THEOREMS = {'cone_eq_fails_axis': AXIS_CONCL}
TRANSPORT = {'NativeGate': ('nativeGate_of_cone_eq', 'nativeGate_of_avail'),
             'Entangling': ('entangling_of_cone_eq', 'entangling_of_avail')}
TRANSPORT_FROM = {'NativeGate': 'NativeGateOf', 'Entangling': 'EntanglingOf'}
VERDICT = 'k1b_core'
# S5 -- reuse
REUSED = ('maxCone', 'maxConeOf', 'EffectsOn', 'NativeGate', 'Entangling', 'jointStates', 'IsProduct', 'IsNot',
          'prodState', 'corner', 'actT', 'actC', 'W', 'eball', 'sharpFamily', 'axisFamily', 'dim_of_nativeGate',
          'three_of_nativeGate', 'maxConeOf_avail_eq', 'maxConeOf_sharpFamily_zero_ne', 'maxConeOf_axis_ne',
          'unitEff', 'isEffectOn_unitEff', 'sharpEff_isEffectOn', 'PreservesBody', 'SharpSeed',
          'BoundaryTransitive', 'SeedOrbitAvailable', 'IsEffectOn', 'prodEffVal', 'sharpEff', 'fullEffects')
IMPORT_ONLY = 'import OIBridge.EffectSpace'
# S6 -- field-neutral, no drive, no limit closure, no mixing closure
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'ElementaryDrivability', 'flow', 'Flow', 'rot3', 'J_off_axis', 'LimitClosed', 'closure',
                  'Tendsto', 'Filter', 'TensorProduct', 'Hilbert', 'MixingClosed', 'unitSpan')
CONTROL_ONLY_TOKENS = ('unitEff', 'axisFamily', 'isEffectOn_unitEff', 'sharpEff_isEffectOn', 'sharpFamily')
# S7 -- phrases
PHRASES = ('OI supplies', 'derived from OI', 'sourced from OI', 'mixing closure is derived',
           'local tomography is derived', 'product form is derived', 'product-test completeness is derived',
           'composite premise is discharged', 'K2 is discharged', 'qubit effect space', 'selects d = 3 from OI')
# S8 -- dimension
HD_ONLY = sorted(['nativeGate_of_avail', 'entangling_of_avail', 'dim_of_nativeGateOf', 'three_of_nativeGateOf',
                  'k1b_core'])
HD_RE = re.compile(r'0\s*<\s*d(?![\w\'])|(?<![\w\'])d\s*>\s*0|1\s*≤\s*d(?![\w\'])|(?<![\w\'])d\s*≥\s*1'
                   r'|d\s*≠\s*0')
CONTROL_SECTIONS = ('§D', 'verdict')
DIM3 = re.compile(r'(?<![\w\'.])(Fin|eball|W|HVec|sharpFamily|fullAut|fullEffects|maxCone)\s+3(?![\w\'])'
                  r'|(?<![\w\'.])(ball3|eball_three)(?![\w\'])')
# V -- the frozen decision rule
TOKENS = ('K1-EFFECT-AVAILABILITY-DISCHARGED', 'K1-BRIDGE-NOT-ESTABLISHED')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def theorems_with(texts, kinds, binders, concl):
    out = []
    for n, t in texts.items():
        if kinds.get(n) != 'theorem':
            continue
        bb, cc = stmt_parts(texts, n)
        if explicit_binders(bb) == norm(binders) and cc == norm(concl):
            out.append(n)
    return sorted(out)


def relative_field(name):
    """DIM-1's field with the gate renamed `T` and, in the two positivity clauses, `maxConeOf avail` for
    `maxCone Ω`."""
    line = field_line(DIM1_NATIVEGATE, name)
    if line is None:
        return None
    line = G_TO_T.sub('T', line)
    if name in CONE_FIELDS:
        line = line.replace('maxCone Ω', 'maxConeOf avail')
    return norm(line)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def relative_ok(chunks):
    """S1: the three relative forms are DIM-1's with the family's cone and nothing else changed."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ng = texts.get('NativeGateOf', '')
    if kinds.get('NativeGateOf') != 'structure' or fields(ng) != NG_FIELDS or fields(DIM1_NATIVEGATE) != NG_FIELDS:
        return False
    if any(field_line(ng, f) != relative_field(f) for f in NG_FIELDS):
        return False
    head = norm(def_header(ng))
    if '(avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ))' not in head or '(T : W d ≃ₗ[ℝ] W d)' not in head or \
            'maxCone Ω' in norm(ng):
        return False
    if kinds.get('jointStatesOf') != 'def' or def_body(texts.get('jointStatesOf', '')) != JOINT_BODY or \
            def_body(DIM1_JOINTSTATES).replace('maxCone Ω', 'maxConeOf avail') != JOINT_BODY:
        return False
    want = G_TO_T.sub('T', def_body(DIM1_ENTANGLING)).replace('jointStates Ω', 'jointStatesOf avail')
    if kinds.get('EntanglingOf') != 'def' or def_body(texts.get('EntanglingOf', '')) != want or \
            'jointStatesOf avail' not in want:
        return False
    return True


def verdicts(chunks):
    """The frozen decision rule, read from the module's statements alone.

    K1-EFFECT-AVAILABILITY-DISCHARGED  the relative forms are DIM-1's with the family's cone (S1); a theorem with
                                       explicit binders exactly `0 < d`, effect soundness, OG-1's four hypotheses,
                                       `IsNot` and `NativeGateOf` concludes `d = 1 ∨ d = 3`; one with `EntanglingOf`
                                       added concludes `d = 3`; and the two controls are theorems with their frozen
                                       statements: `cone_eq_fails_zero` and `cone_eq_fails_axis`
    K1-BRIDGE-NOT-ESTABLISHED          otherwise"""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = relative_ok(chunks)
    for n, (b, c) in SELECTORS.items():
        ok = ok and n in theorems_with(texts, kinds, b, c)
    ok = ok and kinds.get('cone_eq_fails_zero') == 'theorem' and \
        stmt_parts(texts, 'cone_eq_fails_zero') == ('', norm(ZERO_CONCL))
    ok = ok and kinds.get('cone_eq_fails_axis') == 'theorem' and \
        stmt_parts(texts, 'cone_eq_fails_axis') == ('', norm(AXIS_CONCL))
    return [TOKENS[0] if ok else TOKENS[1]]


def hd_violations(texts):
    return sorted(n for n, t in texts.items() if HD_RE.search(code_only(t)))


def numeral3_violations(mod):
    secs = sections(mod)
    bad = []
    sp = spans(mod)
    first = sp[0][2] if sp else len(mod)
    if DIM3.search(code_only(mod[:first])):
        bad.append('preamble')
    for kind, name, start, se, nxt, cend in sp:
        if section_at(secs, start) in CONTROL_SECTIONS:
            continue
        if DIM3.search(code_only(mod[start:nxt])) or any(token(t, code_only(mod[start:nxt]))
                                                          for t in CONTROL_ONLY_TOKENS):
            bad.append(name)
    return bad


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    check('S1', 'NativeGateOf, jointStatesOf and EntanglingOf are DIM-1\'s forms with the family\'s cone and '
                'nothing else changed' + tag, relative_ok(chunks))
    # S2
    bad2 = []
    for n, (b, c) in SELECTORS.items():
        if kinds.get(n) != 'theorem' or n not in theorems_with(texts, kinds, b, c) or PREFIX + n not in prints:
            bad2.append(n)
        if any(token(t, texts.get(n, '')) for t in SEL_FORBIDDEN):
            bad2.append(n)
    check('S2', 'the two relative selectors with exactly `0 < d`, effect soundness, the four hypotheses, IsNot and '
                'NativeGateOf (and EntanglingOf), their frozen conclusions, and no mixing, unit or full-effect token'
                '%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    bad3 = [n for n, names in TRANSPARENT.items()
            if kinds.get(n) != 'theorem' or not all(token(m, proofs.get(n, '')) for m in names)]
    bad3 += [t for t in DIM_ARGUMENT_TOKENS if token(t, code)]
    check('S3', 'each selector is the cone equality, the transport and DIM-1\'s selector by name; no dimension '
                'argument token%s%s' % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = []
    for n, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            concl = norm(split_statement(t)[1])
        else:
            concl = norm(split_statement(def_header(t))[1])
        if n in WITNESS_THEOREMS:
            if concl != norm(WITNESS_THEOREMS[n]) or k != 'theorem' or PREFIX + n not in prints:
                bad4.append(n)
            continue
        if n == VERDICT:
            cc = concl.replace(norm(AXIS_CONCL), '')
            for p in PREMISES:
                for m in re.finditer(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(p), cc):
                    rest = cc[m.end():]
                    j = rest.find(' →')
                    if j == -1 or any(s in rest[:j] for s in (' ∧ ', ' ∨ ', ') ∧', ') ∨')):
                        bad4.append(n)
            continue
        for p in PREMISES:
            if token(p, concl):
                bad4.append(n)
        for landed, (a, b) in TRANSPORT.items():
            if token(landed, concl):
                binders = norm(split_statement(t)[0])
                if n not in (a, b) or not token(TRANSPORT_FROM[landed], binders):
                    bad4.append(n)
    check('S4', 'the named premises concluded of no hypothesis-bound object; NativeGate and Entangling concluded '
                'only from their relative forms%s%s' % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S5', 'landed objects reused, not re-declared; the only import is OIBridge.EffectSpace%s%s'
          % (tag, (' %s' % clash[:3]) if clash else ''), not clash and imports == [IMPORT_ONLY])
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no drive, flow, limit-closure, mixing-closure or unit-span token%s%s'
          % (tag, (' %s' % hits) if hits else ''), not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    hd = hd_violations(texts)
    n3 = numeral3_violations(mod)
    check('S8', '`0 < d` in exactly the frozen statements; no dimension-three object or control family outside the '
                'controls and the verdict%s%s'
          % (tag, (' %s %s' % (hd, n3)) if hd != HD_ONLY or n3 else ''), hd == HD_ONLY and not n3)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    v = verdicts(chunks)
    check('V', 'the verdict by the frozen rule: %s%s' % (v[0], tag), len(v) == 1 and v[0] in TOKENS)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


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
    check('N2', 'every frozen statement, definition and structure unchanged%s%s'
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
    mod = show(commit, MOD)
    module_checks(mod)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        v = verdicts(decl_chunks(mod)) if mod is not None else []
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed verdict %s and no other outcome token (found %s)'
              % (v, toks), len(v) == 1 and toks == v)
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the EFF-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    v = verdicts(decl_chunks(mod)) if mod is not None else []
    print('VERDICT  %s' % ('/'.join(v) or 'none'))
    check('V', 'exactly one outcome', len(v) == 1)

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
    """Insert a declaration just before the verdict section (inside §D)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


DIM_HEAD = ('theorem dim_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n'
            '    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n'
            '    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n'
            '    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n'
            '    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3 :=\n'
            '  dim_of_nativeGate hN (nativeGate_of_avail hd hE hG hP1 hK hV4 hT)')
GENERIC = ('theorem %s {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
           '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} %s : %s := by\n'
           '  exact absurd %s (by simp)')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    check('T', 'the reference module reads %s' % verdict_of(mod), verdict_of(mod) == [TOKENS[0]])
    check('T', 'DIM-1\'s NativeGate, Entangling and jointStates at D are the embedded texts',
          decl_chunks(show(D, 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'))['NativeGate'][1]
          == DIM1_NATIVEGATE
          and decl_chunks(show(D, 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'))['Entangling'][1]
          == DIM1_ENTANGLING
          and decl_chunks(show(D, 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'))['jointStates'][1]
          == DIM1_JOINTSTATES)
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem k1b_core :', '\ntheorem k1b_core\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace\n', '\n'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, '(h : maxConeOf avail = maxCone Ω) : jointStatesOf avail = jointStates Ω := by',
                           '(h : maxConeOf avail ⊆ maxCone Ω) : jointStatesOf avail = jointStates Ω := by'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.K1Bridge.jointStatesOf_eq\n', ''))
    # S1
    must_fail('S1', 'a positivity clause returned to DIM-1\'s cone',
              replace_once(mod, '  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail',
                           '  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxCone Ω'))
    must_fail('S1', 'the frame weakened',
              replace_once(mod, '  frame : ∀ a b : Fin 2,\n    T (prodState',
                           '  frame : ∀ a : Fin 2, ∀ b : Fin 1,\n    T (prodState'))
    must_fail('S1', 'a NOT relation dropped',
              replace_once(mod, '  relC : ∀ ω, actC N (T (actC N ω)) = actT N (T ω)\n', ''))
    must_fail('S1', 'the entangling clause on DIM-1\'s joint states',
              replace_once(mod, 'T (prodState x y) ∈ (jointStatesOf avail).extremePoints ℝ ∧',
                           'T (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧'))
    # S2
    must_fail('S2', 'the mixing closure added to the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hN : IsNot (eball d) z N)',
                                                           '(hM : MixingClosed avail) (hN : IsNot (eball d) z N)')))
    must_fail('S2', '`0 < d` dropped from the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hd : 0 < d) ', '')
                           .replace('nativeGate_of_avail hd', 'nativeGate_of_avail (by omega)')))
    must_fail('S2', 'effect soundness dropped from the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace(' (hE : EffectsOn (eball d) avail)', '')))
    must_fail('S2', 'DIM-1\'s NOT dropped from the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hN : IsNot (eball d) z N) ', '')))
    must_fail('S2', 'the entangling clause dropped from the three selector',
              replace_once(mod, '    (hEnt : EntanglingOf (eball d) avail T) : d = 3 :=',
                           '    : d = 3 :='))
    # S3
    must_fail('S3', 'the dimension selector proved without DIM-1\'s selector',
              replace_once(mod, '  dim_of_nativeGate hN (nativeGate_of_avail hd hE hG hP1 hK hV4 hT)',
                           '  by exact absurd hd (by simp)'))
    must_fail('S3', 'a dimension-argument token',
              append_control(mod, 'theorem extra_rank : finrank ℝ (Fin 1 → ℝ) = 1 := by simp'))
    # S4
    must_fail('S4', 'the relative native-gate hypotheses concluded from the seed orbit',
              append_control(mod, GENERIC % ('gate_of_orbit', '{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}'
                                             ' {T : W d ≃ₗ[ℝ] W d} (hV4 : SeedOrbitAvailable G r avail)',
                                             'NativeGateOf (eball d) avail z N T', 'hV4')))
    must_fail('S4', 'effect soundness concluded for a hypothesis-bound family',
              append_control(mod, GENERIC % ('effects_of_orbit', '(hV4 : SeedOrbitAvailable G r avail)',
                                             'EffectsOn (eball d) avail', 'hV4')))
    must_fail('S4', 'DIM-1\'s native-gate hypotheses concluded without the relative form',
              append_control(mod, GENERIC % ('gate_free', '{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}'
                                             ' {T : W d ≃ₗ[ℝ] W d} (hd : 0 < d)',
                                             'NativeGate (eball d) z N T', 'hd')))
    # S5
    must_fail('S5', 'a landed definition re-declared', append_control(mod, 'def maxCone : ℕ := 0'))
    must_fail('S5', 'a second import',
              replace_once(mod, 'import OIBridge.EffectSpace\n',
                           'import OIBridge.EffectSpace\nimport OIBridge.SubstratumSource\n'))
    # S6
    must_fail('S6', 'a complex scalar', append_control(mod, 'def cvec (z : Fin d → ℂ) : Fin d → ℂ := z'))
    must_fail('S6', 'a mixing-closure token',
              append_control(mod, 'def mixed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop := MixingClosed A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  Round DIM-1 states', '  OI supplies the effects. Round DIM-1 states'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('The relative selectors remove the full effect set from K1; the four hypotheses are '
                          'named premises.')
          and phrase_hits('Hence local tomography\nis derived.') == ['local tomography is derived'])
    # S8
    must_fail('S8', '`0 < d` added to the cone-equality transport',
              replace_once(mod, 'theorem nativeGate_of_cone_eq {Ω : Set (Fin d → ℝ)}',
                           'theorem nativeGate_of_cone_eq (hd : 0 < d) {Ω : Set (Fin d → ℝ)}'))
    must_fail('S8', 'a dimension-three object in the bridge section',
              replace_once(mod, '/-! ### §C', 'theorem three_ball : eball 3 = eball 3 := rfl\n\n/-! ### §C'))
    must_fail('S8', 'the control family in the bridge section',
              replace_once(mod, '/-! ### §C', 'theorem axis_self : axisFamily = axisFamily := rfl\n\n/-! ### §C'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.K1Bridge.k1b_core\n',
                           '#print axioms OIBridge.K1Bridge.k1b_core\n'
                           '#print axioms OIBridge.K1Bridge.NativeGateOf\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf\n',
                           '#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf\n'
                           '#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf\n'))
    # V -- the decision rule reads the alternatives
    m_mix = replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hN : IsNot (eball d) z N)',
                                                         '(hM : MixingClosed avail) (hN : IsNot (eball d) z N)'))
    check('M', 'decision rule: the dimension selector with the mixing closure reads NOT-ESTABLISHED',
          verdict_of(m_mix) == [TOKENS[1]])
    m_zero = replace_once(mod, 'theorem cone_eq_fails_zero : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) :=',
                          'theorem cone_eq_fails_zero : maxConeOf (sharpFamily 0) = maxConeOf (sharpFamily 0) :=')
    check('M', 'decision rule: the d = 0 control weakened reads NOT-ESTABLISHED', verdict_of(m_zero) == [TOKENS[1]])
    m_axis = replace_once(mod, 'theorem cone_eq_fails_axis : EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily '
                               '≠ maxCone (eball 3) :=',
                          'theorem cone_eq_fails_axis : EffectsOn (eball 3) axisFamily :=')
    check('M', 'decision rule: the one-axis control weakened reads NOT-ESTABLISHED',
          verdict_of(m_axis) == [TOKENS[1]])
    m_rel = replace_once(mod, '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail',
                         '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxCone Ω')
    check('M', 'decision rule: a relative form that is not DIM-1\'s with the family\'s cone reads NOT-ESTABLISHED',
          verdict_of(m_rel) == [TOKENS[1]])
    check('M', 'note tokens: exactly the stated verdict is found',
          note_tokens('Outcome: K1-EFFECT-AVAILABILITY-DISCHARGED.') == [TOKENS[0]]
          and note_tokens('K1-EFFECT-AVAILABILITY-DISCHARGED, not K1-BRIDGE-NOT-ESTABLISHED.') == list(TOKENS)
          and note_tokens('nothing') == [])
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
