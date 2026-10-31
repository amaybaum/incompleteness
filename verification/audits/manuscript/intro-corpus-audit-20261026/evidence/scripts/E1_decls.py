#!/usr/bin/env python3
"""E1_decls.py - resolve the kernel declarations the Introduction relies on.

For each (module, cited line, short name) in SPEC this reads the module's source
under <lean-mathlib dir>, and records:
  - whether the cited line is the declaration's header (or the line where it is
    actually declared, if not);
  - the enclosing namespaces, hence the full name;
  - the statement text, from the header to the first `:=` or `where`
    (for a structure/class/def, its body up to the next top-level line);
  - every `#print axioms` line in the module naming the declaration;
  - the report for it in the retained expected result, if one is given.

It also scans the whole source tree for the forbidden-construct tokens
(`axiom`/`opaque`/`unsafe` declarations, `sorry`, `admit` tactic,
`native_decide`, `implemented_by`, `extern`, `debug.skipKernelTC`).

Usage:
    python3 -I E1_decls.py <lean-mathlib dir> [--results <results-*.json>] > out.json

Paths are arguments; nothing is written except to stdout. Reading only.
"""
import json
import os
import re
import sys

# (module, cited line, short name, where it is cited)
SPEC = [
    # Appendix A (28)
    ("Equivalence", 462, "finite_horizon_equivalence", "AppA"),
    ("Equivalence", 422, "S_imp_D", "AppA"),
    ("Equivalence", 294, "D_imp_Qfb", "AppA"),
    ("Equivalence", 245, "Qfb_imp_S", "AppA"),
    ("EquivalenceChain", 179, "permMatrix_mem_unitaryGroup", "AppA"),
    ("HiddenMemory", 83, "pushforward_identity", "AppA"),
    ("HiddenMemory", 114, "distinguishability_floor", "AppA"),
    ("HiddenMemory", 170, "capacity_floor", "AppA"),
    ("HiddenMemory", 185, "unavoidable_hidden_predictive_memory", "AppA"),
    ("C3Necessity", 80, "c3_necessity", "AppA"),
    ("C3Necessity", 117, "card_hidden_ge_two_pow_Istar", "AppA"),
    ("EquivalenceChain", 110, "isPermMatrix_of_stochastic_inverse", "AppA"),
    ("RecurrenceHorizon", 148, "pIndivisible_of_rooted_identity_return_of_overlap", "AppA"),
    ("PhysicalC4Discharge", 122, "routed_forces_indivisible_somewhere", "AppA"),
    ("CoherentLiftGauge", 537, "gl2_strong_gauge_moves_relative_candidate", "AppA"),
    ("CoherentLiftGauge", 451, "gl3_constant_gauge_preserves_relative", "AppA"),
    ("TrackBQfbBridge", 276, "bridge_traj", "AppA"),
    ("TrackBQfbBridge", 180, "rooted_eq_iff_slice_eq", "AppA"),
    ("TrackBQfbBridge", 286, "realData_traj_stochastic", "AppA"),
    ("GeneralCarrier", 100, "exactAll_iff_physical_general", "AppA"),
    ("PhysicalCharacterization", 301, "physical_of_exactAll", "AppA"),
    ("GeneralCarrier", 93, "exactAll_of_physical_general", "AppA"),
    ("OperationalValidity", 124, "krausSoundExt_of_validity_inert", "AppA"),
    ("IsometryExtension", 179, "compositeCompleteness_unconditional", "AppA"),
    ("IsometryExtension", 116, "finiteIsometryExtensionSF_discharged", "AppA"),
    ("LevelOneSeam", 196, "exactAll_of_levelOne", "AppA"),
    ("RankGapTheory", 702, "five_way_minimality", "AppA"),
    ("GeneralCarrier", 160, "oi_alone_not_qm", "AppA"),
    # matrix.json kernel-layer chains, not in Appendix A
    ("CausalReadback", 52, "PDivisible", "matrix"),
    ("CausalReadback", 96, "tv_mul_le", "matrix"),
    ("Equivalence", 147, "Stochastic", "matrix"),
    ("Equivalence", 157, "RevReal", "matrix"),
    ("Equivalence", 190, "QfbReal", "matrix"),
    ("Equivalence", 205, "QfbReal.born", "matrix"),
    ("Equivalence", 209, "QfbReal.chain", "matrix"),
    ("EquivalenceChain", 253, "isDiag_Phi", "matrix"),
    ("FiniteEntropy", 372, "cmi_nonneg", "matrix"),
    ("FrozenSourcing", 318, "frozen_sourcing_verdict", "matrix"),
    ("GeneralCarrier", 79, "exactComposite_of_validity_general", "matrix"),
    ("HiddenMemory", 54, "Realization", "matrix"),
    ("HiddenMemory", 138, "memory", "matrix"),
    ("RootedClassification", 135, "rootedMap_periodic", "matrix"),
    ("RootedClassification", 330, "responseRealization", "matrix"),
    ("OperationalAssembly", 594, "FiniteOperationalTheory", "matrix"),
    ("PhysicalC4Discharge", 68, "RoutedReadback", "matrix"),
    ("PhysicalC4StorageReadback", 256, "routedAtStorage_forces_indivisible_somewhere", "matrix+FINDINGS"),
    ("PhysicalCharacterization", 295, "PhysicalCompletionConditions", "matrix+FINDINGS"),
    ("QuantumRepresentationT2", 163, "qStar_not_subset_finiteRootedRealizable", "matrix+FINDINGS"),
    ("ReadWriteControl", 169, "readWriteSourced_not_control", "matrix+FINDINGS"),
    ("ReadWriteControl", 174, "readWriteSourced_not_qm", "matrix+FINDINGS"),
    ("RootedClassificationAllTime", 192, "finiteRootedRealizable_iff_pper", "matrix+FINDINGS"),
    ("StructuralClosure", 383, "substratum_residual", "matrix+FINDINGS"),
    ("StructuralClosure", 408, "substratum_extension_quantum_iff_drives", "matrix+FINDINGS"),
    ("StructuralClosure", 414, "substratum_plus_control_qm", "matrix+FINDINGS"),
    ("TrackBQfbBridge", 43, "realData", "matrix"),
    # FINDINGS.md replacement texts and evidence
    ("OIRealization", 252, "realizesSealedOICore_of_control", "FINDINGS"),
    ("OperationalAssembly", 665, "HasCompositeUnitaryControl", "FINDINGS"),
    ("PhaseSource", 79, "permClass_onesFixing", "FINDINGS"),
    ("PhaseSource", 52, "onesFixing_not_phasesAvailable", "FINDINGS"),
    ("PhaseSource", 196, "substratumClass_not_onesFixing", "FINDINGS"),
    ("StructuralClosure", 370, "substratumClass_not_drivesElementary", "FINDINGS"),
    ("SubstratumInterface", 186, "monomialSource_not_control", "FINDINGS"),
    ("CausalReadback", 178, "RootedRealization", "FINDINGS"),
    # FINDINGS optional changes (O-5, O-14)
    ("CanonicalMeasure", 276, "determinism_reversibility_selected_measure", "FINDINGS-optional"),
    ("RegionLimit", 296, "continuous_extension_not_unique", "FINDINGS-optional"),
]

DECL_KW = (r'(?:theorem|lemma|def|structure|class|abbrev|inductive|instance|'
           r'noncomputable def|noncomputable abbrev)')
HEADER = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected )?'
                    r'(?:noncomputable )?(theorem|lemma|def|structure|class|'
                    r'abbrev|inductive|instance)\s+([^\s:({\[]+)')
NS_OPEN = re.compile(r'^\s*namespace\s+(\S+)')
NS_END = re.compile(r'^\s*end\s+(\S+)\s*$')
SECTION = re.compile(r'^\s*section\b\s*(\S*)')
PRINT = re.compile(r"^#print axioms\s+([A-Za-z0-9_.']+)\s*$")

FORBIDDEN = {
    'axiom_decl': re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected )?'
                             r'(?:noncomputable )?axiom\s'),
    'opaque_decl': re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected )?'
                              r'(?:noncomputable )?opaque\s'),
    'unsafe': re.compile(r'\bunsafe\b'),
    'sorry': re.compile(r'\bsorry\b'),
    'admit': re.compile(r'^\s*admit\b|\badmit\s*$|;\s*admit\b|·\s*admit\b'),
    'native_decide': re.compile(r'native_decide|decide\s*\+native|ofReduceBool'),
    'implemented_by': re.compile(r'implemented_by'),
    'extern': re.compile(r'@\[\s*extern'),
    'skipKernelTC': re.compile(r'skipKernelTC'),
}


def strip_comments(lines):
    """Blank out comment text (block /- -/ and line --), keeping line count."""
    out, depth = [], 0
    for line in lines:
        res, i = [], 0
        while i < len(line):
            if depth:
                if line.startswith('-/', i):
                    depth -= 1
                    i += 2
                elif line.startswith('/-', i):
                    depth += 1
                    i += 2
                else:
                    i += 1
            else:
                if line.startswith('/-', i):
                    depth += 1
                    i += 2
                elif line.startswith('--', i):
                    break
                else:
                    res.append(line[i])
                    i += 1
        out.append(''.join(res))
    return out


def scan_forbidden(root):
    hits = {k: [] for k in FORBIDDEN}
    nfiles = 0
    for dp, _, fs in os.walk(root):
        if '.lake' in dp.split(os.sep):
            continue
        for f in sorted(fs):
            if not f.endswith('.lean'):
                continue
            nfiles += 1
            p = os.path.join(dp, f)
            code = strip_comments(open(p, encoding='utf-8').read().split('\n'))
            for i, line in enumerate(code, 1):
                for k, rx in FORBIDDEN.items():
                    if rx.search(line):
                        hits[k].append(f"{os.path.relpath(p, root)}:{i}: {line.strip()[:120]}")
    return nfiles, hits


def namespaces_at(code, upto):
    stack = []
    for line in code[:upto - 1]:
        m = NS_OPEN.match(line)
        if m:
            stack.append(('ns', m.group(1)))
            continue
        m = SECTION.match(line)
        if m:
            stack.append(('sec', m.group(1)))
            continue
        m = NS_END.match(line)
        if m:
            # pop the matching namespace or section
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][1] == m.group(1):
                    del stack[j:]
                    break
        elif re.match(r'^\s*end\s*$', line):
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][0] == 'sec' and stack[j][1] == '':
                    del stack[j:]
                    break
    return '.'.join(n for kind, n in stack if kind == 'ns')


def statement(raw, code, i0):
    """Statement text from header line i0 (1-based)."""
    kind = HEADER.match(code[i0 - 1]).group(1)
    out = []
    i = i0 - 1
    while i < len(raw) and len(out) < 80:
        out.append(raw[i].rstrip())
        c = code[i]
        if kind in ('theorem', 'lemma', 'instance'):
            if ':=' in c:
                break
        else:
            # def/structure/class/abbrev/inductive: stop at the next top-level line
            if i > i0 - 1 and i + 1 < len(raw):
                nxt = code[i + 1]
                if nxt and not nxt[0].isspace() and nxt.strip():
                    break
                if not raw[i + 1].strip() and (i + 2 >= len(raw) or (code[i + 2][:1] and not code[i + 2][0].isspace())):
                    break
        i += 1
    return kind, '\n'.join(out)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    root = sys.argv[1]
    results = None
    if '--results' in sys.argv:
        results = json.load(open(sys.argv[sys.argv.index('--results') + 1]))
    out = []
    cache = {}
    for module, line, name, where in SPEC:
        path = os.path.join(root, 'OIBridge', module + '.lean')
        if module not in cache:
            raw = open(path, encoding='utf-8').read().split('\n')
            cache[module] = (raw, strip_comments(raw))
        raw, code = cache[module]
        short = name.split('.')[-1]
        headers = []
        for i, c in enumerate(code, 1):
            m = HEADER.match(c)
            if m and (m.group(2) == name or m.group(2).split('.')[-1] == short
                      and m.group(2).endswith(name)):
                headers.append(i)
        rec = {'module': module, 'cited_line': line, 'name': name, 'cited_in': where,
               'header_lines': headers}
        if not headers:
            rec['resolves'] = False
            out.append(rec)
            continue
        found = min(headers, key=lambda h: abs(h - line))
        rec['found_line'] = found
        rec['resolves_at_cited_line'] = found == line
        rec['offset'] = found - line
        ns = namespaces_at(code, found)
        rec['full_name'] = (ns + '.' if ns else '') + name
        kind, st = statement(raw, code, found)
        rec['kind'] = kind
        rec['statement'] = st
        prints = []
        for i, c in enumerate(raw, 1):
            m = PRINT.match(c)
            if m and (m.group(1) == rec['full_name'] or m.group(1).endswith('.' + name)
                      or m.group(1) == name):
                prints.append({'line': i, 'target': m.group(1)})
        rec['print_axioms'] = prints
        if results is not None:
            mod = results['expected']['modules'].get('OIBridge/' + module + '.lean')
            if mod is None:
                rec['retained_report'] = None
                rec['retained_module'] = False
            else:
                rec['retained_module'] = True
                reps = [r for r in mod['reports']
                        if r['name'] == rec['full_name'] or r['name'].endswith('.' + name)]
                rec['retained_report'] = reps
                rec['retained_module_status'] = mod.get('status')
        out.append(rec)
    nfiles, hits = scan_forbidden(root)
    json.dump({'declarations': out,
               'forbidden_scan': {'files': nfiles, 'hits': hits}},
              sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == '__main__':
    main()
