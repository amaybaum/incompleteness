"""I3 kernel census (stage 6, step 1, coverage control (a)).

DECISION RULE (fixed before the first run):
- Scope: the Lean modules governed (execution path `A`) by the oi-qm reconstruction rounds of the K programme at L,
  as listed in MODULES below (from each round's `v3-governed-paths` block), plus the four-copy design modules [D]
  under pt/inputs/fourcopy/ (listed separately, tagged D, never counted as kernel).
- A declaration line is a line matching, at column 0, optional attributes and modifiers followed by one of
  axiom | opaque | structure | class | def | abbrev | inductive | instance | theorem | lemma.
  Indented matches are counted separately and reported (none expected).
- Census items (mapped one by one in CENSUS.md): every `axiom`, every `opaque`, every `class`, every `structure`
  whose header (text up to `where` or `:=`) ends in `: Prop`, every `def`/`abbrev` whose header ends in `: Prop`
  or `→ Prop` (a predicate), every `inductive` whose header ends in `Prop`.
- Header: the declaration line and following lines up to and including the first line containing `:=` or ending
  in `where` (at most 25 lines). Docstring: the `/-- ... -/` block ending on the line before the declaration
  (attribute lines skipped). Fields of a Prop structure: the following non-blank lines indented by two spaces
  that begin a field `name :` (at most 80 lines scanned, until the next column-0 non-comment line).
- Output is deterministic (sorted by module list order, then line). No timestamps.
"""
import os
import re
import sys

BASE = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
DESIGN = os.path.join("..", "inputs", "fourcopy")

MODULES = [
    ("KINF-1/KINF-2", "KInfFoundations.lean"),
    ("OG-1", "OrbitGeneration.lean"),
    ("OG-1", "OrbitNormalization.lean"),
    ("TRB-1", "TransitiveBody.lean"),
    ("CMP-1", "StageCompletion.lean"),
    ("IIP-1", "InvariantInnerProduct.lean"),
    ("OPACT-1", "CompletionAction.lean"),
    ("ORD-1", "CompositionOrder.lean"),
    ("COMP-1", "CompositeInterface.lean"),
    ("DIM-1", "CompositeDimension.lean"),
    ("EFF-1", "EffectSpace.lean"),
    ("K1-BRIDGE-1", "K1Bridge.lean"),
    ("K1-SHARP-TESTS-1", "SharpTests.lean"),
    ("K2-GUARD-1", "K2Guard.lean"),
    ("KTRANS-DENSE-1", "DenseOrbit.lean"),
    ("NB-1", "NativeGateBall.lean"),
    ("ODD-CHAR-1", "OddChar.lean"),
    ("PARITY-NOT-1", "ParityNot.lean"),
    ("RELC-SELECT-1", "RelcSelectParity.lean"),
    ("RELC-SELECT-1", "RelcSelectBlock.lean"),
    ("RELC-SELECT-1", "RelcSelectSqueeze.lean"),
    ("RELC-SELECT-1", "RelcSelectC5.lean"),
]
DESIGN_MODULES = sorted(f for f in os.listdir(DESIGN) if f.endswith(".lean") and f != "OIBridge.lean")

DECL = re.compile(
    r"^(?P<indent>\s*)(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe|nonrec)\s+)*"
    r"(?P<kind>axiom|opaque|structure|class|def|abbrev|inductive|instance|theorem|lemma)\b\s*(?P<name>[^\s:({\[]*)"
)


def header_of(lines, i):
    out = []
    for j in range(i, min(i + 25, len(lines))):
        out.append(lines[j].rstrip("\n"))
        s = lines[j].rstrip()
        if ":=" in s or s.endswith("where") or re.search(r"\bwhere\b\s*$", s):
            break
    return out


def docstring_of(lines, i):
    j = i - 1
    while j >= 0 and lines[j].strip().startswith("@["):
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith("-/"):
        return None, None
    end = j
    while j >= 0 and "/--" not in lines[j]:
        j -= 1
    if j < 0:
        return None, None
    return j + 1, [l.rstrip("\n") for l in lines[j:end + 1]]


def type_tail(header):
    text = " ".join(h.strip() for h in header)
    text = re.sub(r"--.*?$", "", text)
    cut = len(text)
    for tok in [":=", " where"]:
        k = text.find(tok)
        if k != -1:
            cut = min(cut, k)
    return text[:cut].rstrip()


def is_prop_valued(kind, header):
    t = type_tail(header)
    if kind in ("structure", "def", "abbrev", "inductive"):
        return bool(re.search(r"(:|→|->)\s*Prop\s*$", t))
    return False


def fields_of(lines, i, header_len):
    out = []
    for j in range(i + header_len, min(i + header_len + 80, len(lines))):
        s = lines[j].rstrip("\n")
        if s and not s.startswith(" ") and not s.startswith("--") and not s.startswith("/-"):
            break
        m = re.match(r"^  (?:\(|\{)?([A-Za-z_][A-Za-z0-9_'.]*)\s*:", s)
        if m:
            out.append((j + 1, m.group(1)))
    return out


def scan(path, tag, rnd, report, items, totals):
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    kinds = {}
    indented = []
    for i, line in enumerate(lines):
        m = DECL.match(line)
        if not m:
            continue
        kind = m.group("kind")
        if m.group("indent"):
            indented.append((i + 1, kind, m.group("name")))
            continue
        kinds[kind] = kinds.get(kind, 0) + 1
        header = header_of(lines, i)
        in_census = kind in ("axiom", "opaque", "class") or is_prop_valued(kind, header)
        if in_census:
            dl, doc = docstring_of(lines, i)
            flds = fields_of(lines, i, len(header)) if kind == "structure" else []
            items.append((tag, rnd, os.path.basename(path), i + 1, kind, m.group("name"), header, dl, doc, flds))
    totals.append((tag, rnd, os.path.basename(path), len(lines), kinds, indented))


def main():
    items, totals = [], []
    for rnd, mod in MODULES:
        scan(os.path.join(BASE, mod), "K", rnd, None, items, totals)
    for mod in DESIGN_MODULES:
        scan(os.path.join(DESIGN, mod), "D", "fourcopy", None, items, totals)
    print("# I3 kernel census — modules, declaration counts, census items")
    print()
    print("## Declaration counts per module (column-0 declarations)")
    allk = ["axiom", "opaque", "class", "structure", "def", "abbrev", "inductive", "instance", "theorem", "lemma"]
    print("tag | round | module | lines | " + " | ".join(allk) + " | indented")
    sums = {k: 0 for k in allk}
    for tag, rnd, mod, n, kinds, ind in totals:
        print(f"{tag} | {rnd} | {mod} | {n} | " + " | ".join(str(kinds.get(k, 0)) for k in allk) + f" | {len(ind)}")
        if tag == "K":
            for k in allk:
                sums[k] += kinds.get(k, 0)
    print("K-total | | | | " + " | ".join(str(sums[k]) for k in allk) + " |")
    for tag, rnd, mod, n, kinds, ind in totals:
        for (ln, kd, nm) in ind:
            print(f"INDENTED {tag} {mod}:{ln} {kd} {nm}")
    print()
    print("## Census items (axiom | opaque | class | Prop-valued structure/def/abbrev/inductive)")
    cnt = {}
    for it in items:
        cnt[(it[0], it[4])] = cnt.get((it[0], it[4]), 0) + 1
    for key in sorted(cnt):
        print(f"count {key[0]} {key[1]} = {cnt[key]}")
    print(f"count K total = {sum(v for (t, k), v in cnt.items() if t == 'K')}")
    print(f"count D total = {sum(v for (t, k), v in cnt.items() if t == 'D')}")
    print()
    n = 0
    for (tag, rnd, mod, ln, kind, name, header, dl, doc, flds) in items:
        n += 1
        print(f"### C{n:03d} [{tag}] {mod}:{ln} {kind} {name} (round {rnd})")
        if doc:
            print(f"docstring {mod}:{dl}-{dl + len(doc) - 1}:")
            for d in doc:
                print("  | " + d)
        else:
            print("docstring: none")
        print("header:")
        for h in header:
            print("  > " + h)
        if flds:
            print("fields: " + ", ".join(f"{nm}@{l}" for l, nm in flds))
        print()
    print("END")


if __name__ == "__main__":
    sys.exit(main())
