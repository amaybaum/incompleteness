#!/usr/bin/env python3
"""Generate a concise back-of-book index for The Incompleteness of Observation.
Page numbers are derived from the compiled FULL.pdf (PDF page == printed page).
Emits index.md with three sections: Concepts, Names, Symbols & Notation.
"""
import json, re

pages = json.load(open('/tmp/pages.json'))  # list[str], idx 0 == printed page 1
NPAGES = len(pages)

# Front matter ends p27; Ch1 starts p28. Restrict concept/name scan to body+appendices.
BODY_START = 27  # 0-indexed -> printed page 28

def norm(s):
    return re.sub(r'\s+', ' ', s).lower()

PAGE_NORM = [norm(p) for p in pages]

def find_pages(patterns, start=BODY_START, max_hits=8):
    """Return sorted printed-page numbers where any pattern (regex, lowercased) appears."""
    hits = []
    for i in range(start, NPAGES):
        txt = PAGE_NORM[i]
        if any(re.search(p, txt) for p in patterns):
            hits.append(i + 1)
    # collapse: keep at most max_hits, preferring spread
    if len(hits) > max_hits:
        step = len(hits) / max_hits
        hits = [hits[int(k*step)] for k in range(max_hits)]
    return hits

def rng(nums):
    """Format a page list as a compact reference string with ranges."""
    if not nums:
        return None
    nums = sorted(set(nums))
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j+1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if j == i else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ', '.join(out)

# ---- CONCEPT INDEX: (display term, [regex patterns], [subentries]) ----
# subentry = (label, [patterns])
CONCEPTS = [
    ("arrow of time", [r'arrow of time'], []),
    ("Bell inequalities", [r'bell inequalit', r'chsh'], []),
    ("BQP (bounded-error quantum polynomial time)", [r'\bbqp\b'], []),
    ("Bullet Cluster", [r'bullet cluster'], []),
    ("chemistry, emergence of", [r'emergence of chemistry', r'chemical bond'], []),
    ("coherence, quantum", [r'quantum coherence', r'coherence time'],
        [("in photosynthesis", [r'photossynthe']),
         ("vibronic", [r'vibronic'])]),
    ("computational irreducibility", [r'computational irreducib', r'\birreducib'], []),
    ("decoherence", [r'decoherence'],
        [("gravitationally induced", [r'gravitational.{0,15}decoher', r'dsw ']),
         ("from horizons", [r'horizon.{0,20}decoher'])]),
    ("DSW (Danielson-Satishchandran-Wald) effect", [r'danielson', r'\bdsw\b'], []),
    ("epigenetic clock", [r'epigenetic clock', r'methylation age'], []),
    ("evolution, molecular", [r'molecular clock', r'overdispers'], []),
    ("falsifiability", [r'falsifiab', r'falsification'], []),
    ("gauge structure", [r'gauge structure', r'gauge symmetr'], []),
    ("gene regulatory networks", [r'gene regulatory network', r'\bgrn\b'], []),
    ("gravitational waves, echoes", [r'gravitational.wave echo', r'echo'], []),
    ("gravity, emergent", [r'emergent gravity', r'entropic force', r'gravity.{0,12}emerg'], []),
    ("holographic principle", [r'holographic principle', r'holography'], []),
    ("incompleteness of observation", [r'incompleteness'], []),
    ("JUNO experiment", [r'\bjuno\b'], []),
    ("Kochen-Specker theorem", [r'kochen.specker'], []),
    ("MOND (modified Newtonian dynamics)", [r'\bmond\b', r'modified newtonian'], []),
    ("neutrino mass ordering", [r'neutrino mass', r'mass ordering'], []),
    ("origin of life", [r'origin of life'], []),
    ("PBR (Pusey-Barrett-Rudolph) theorem", [r'pusey.barrett', r'\bpbr\b'], []),
    ("quantum biology", [r'quantum biology'], []),
    ("quantum computing", [r'quantum comput'], []),
    ("quantum error correction", [r'error correction'], []),
    ("radical-pair mechanism", [r'radical.pair', r'magnetorecept'], []),
    ("reconstruction theorem", [r'reconstruction theorem'], []),
    ("running-vacuum model", [r'running.vacuum', r'running vacuum'], []),
    ("structural realism", [r'structural realism'], []),
    ("substratum", [r'substratum'],
        [("finite deterministic", [r'finite determin']),
         ("bijection", [r'bijection'])]),
    ("topology of the universe", [r'topology of the univers', r'cosmic topology'], []),
    ("unitarity", [r'unitarit', r'unitary'], []),
    ("universality", [r'universalit'], []),
]

# ---- NAME INDEX ----
NAMES = [
    ("Afshordi, N.", [r'afshordi']),
    ("Barandes, J. A.", [r'barandes']),
    ("Bekenstein, J. D.", [r'bekenstein']),
    ("Cao, J.", [r'\bcao\b']),
    ("Cornish, N. J.", [r'cornish']),
    ("Danielson, D.", [r'danielson']),
    ("Fleming, G. R.", [r'fleming']),
    ("Gralla, S. E.", [r'gralla']),
    ("Hawking, S. W.", [r'hawking']),
    ("Horvath, S.", [r'horvath']),
    ("Hummer, G.", [r'hummer']),
    ("Komatsu, E.", [r'komatsu']),
    ("Maldacena, J.", [r'maldacena']),
    ("Penington, G.", [r'penington']),
    ("Preskill, J.", [r'preskill']),
    ("Pusey, M. F.", [r'pusey']),
    ("Satishchandran, G.", [r'satishchandran']),
    ("Slagle, K.", [r'slagle']),
    ("Spergel, D. N.", [r'spergel']),
    ("Starkman, G. D.", [r'starkman']),
    ("Szabo, A.", [r'szabo']),
    ("Verlinde, E. P.", [r'verlinde']),
    ("Wald, R. M.", [r'\bwald\b']),
    ("Witten, E.", [r'witten']),
]

# ---- SYMBOL / NOTATION INDEX ----
# (symbol, definition, [patterns], chapter-fallback)
SYMBOLS = [
    (r"$(S, \varphi)$", "the substratum: a finite set $S$ with deterministic bijection $\\varphi$",
        [r'\(s,?\s*\\?varphi\)', r'substratum'], "Ch. 2"),
    (r"$\varphi$", "substratum update map (finite deterministic bijection)",
        [r'\\varphi', r'bijection'], "Ch. 2"),
    (r"$\tau_S$", "substratum time scale (fundamental update interval)",
        [r'XXX_no_match_force_fallback'], "Introduction; Ch. 4"),
    (r"$\tau_B$", "boundary (observable) time scale",
        [r'tau_b'], "Introduction; Ch. 4"),
    (r"$l_p$", "Planck length",
        [r'l_p', r'planck length'], "Ch. 5"),
    (r"$\hbar$", "reduced Planck constant (emergent in the framework)",
        [r'hbar', r'planck constant'], "Ch. 1"),
    (r"$a_0$", "MOND acceleration scale, $a_0 = cH/6$",
        [r'a_0', r'acceleration scale'], "Ch. 7"),
    (r"$\nu$", "running-vacuum parameter",
        [r'running.vacuum parameter', r'vacuum parameter'], "Ch. 6"),
    (r"$T_1$", "qubit energy-relaxation time; also the three-dimensional gauge component",
        [r'energy.relaxation', r'relaxation time'], "Ch. 5; Ch. 14"),
    (r"$\mathcal{O}(\tau_S/\tau_B)$", "framework correction scale to standard kinetics",
        [r'corrections to standard', r'kinetics scale'], "Ch. 16"),
    (r"$\Delta t$", "gravitational-wave echo delay",
        [r'gravitational.wave echo'], "Ch. 7"),
    (r"$r_+$", "outer horizon radius",
        [r'horizon radius', r'outer horizon'], "Ch. 7"),
]

def emit():
    L = []
    L.append("# Index\n")
    L.append("*Page numbers refer to the print edition. Entries marked with a "
             "page range span a continuous discussion; comma-separated numbers "
             "indicate distinct treatments.*\n")

    # --- Concepts ---
    L.append("## Concepts and topics\n")
    cur_letter = None
    for term, pats, subs in sorted(CONCEPTS, key=lambda x: x[0].lower()):
        first = term.lstrip('(').lstrip()[0].upper()
        if first != cur_letter:
            cur_letter = first
            L.append(f"\n**{cur_letter}**\n")
        pp = rng(find_pages(pats))
        line = f"{term}" + (f", {pp}" if pp else "")
        L.append(line + "  ")
        for slabel, spats in subs:
            sp = rng(find_pages(spats))
            if sp:
                L.append(f"&nbsp;&nbsp;&nbsp;&nbsp;*{slabel}*, {sp}  ")

    # --- Names ---
    L.append("\n## Names\n")
    cur_letter = None
    for name, pats in sorted(NAMES, key=lambda x: x[0].lower()):
        first = name[0].upper()
        if first != cur_letter:
            cur_letter = first
            L.append(f"\n**{cur_letter}**\n")
        pp = rng(find_pages(pats, max_hits=6))
        if pp:
            L.append(f"{name}, {pp}  ")
        else:
            L.append(f"{name}  ")

    # --- Symbols ---
    L.append("\n## Symbols and notation\n")
    L.append("*Each entry gives the symbol, its meaning, and where it is "
             "introduced.*\n")
    for sym, defn, pats, chap in SYMBOLS:
        pp = find_pages(pats, max_hits=1)
        ref = f"p. {pp[0]}" if pp else chap
        L.append(f"{sym} &mdash; {defn} ({ref})  ")

    return '\n'.join(L) + '\n'

if __name__ == '__main__':
    out = emit()
    open('index.md', 'w').write(out)
    n_concept = len(CONCEPTS) + sum(len(s) for _,_,s in CONCEPTS)
    print(f"index.md written: {n_concept} concept entries, "
          f"{len(NAMES)} names, {len(SYMBOLS)} symbols")
