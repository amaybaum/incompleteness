"""I3 kernel census, supplement (coverage control (a), extended).

DECISION RULE (fixed before the first run):
- Same module list and declaration regex as kcensus.py (imported by copy, not by import, so that this script is
  self-contained).
- Supplement A: every column-0 `structure` or `class` whose header does NOT end in `: Prop` (data-carrying
  structures; several are used as hypotheses, e.g. a structure of data with Prop fields). For each: docstring,
  header, and the field names with lines.
- Supplement B: every column-0 `def`/`abbrev` whose header has no explicit result type (the text before `:=`
  contains no `:` outside brackets after the name), so that a Prop-valued def with an inferred type is not missed.
- Supplement C: every column-0 `def`/`abbrev` whose header ends in `: Prop` was already listed by kcensus.py; here
  only a count is printed as a cross-check.
- Deterministic output, no timestamps.
"""
import os
import re
import sys

BASE = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
DESIGN = os.path.join("..", "inputs", "fourcopy")
MODULES = [
    "KInfFoundations.lean", "OrbitGeneration.lean", "OrbitNormalization.lean", "TransitiveBody.lean",
    "StageCompletion.lean", "InvariantInnerProduct.lean", "CompletionAction.lean", "CompositionOrder.lean",
    "CompositeInterface.lean", "CompositeDimension.lean", "EffectSpace.lean", "K1Bridge.lean", "SharpTests.lean",
    "K2Guard.lean", "DenseOrbit.lean", "NativeGateBall.lean", "OddChar.lean", "ParityNot.lean",
    "RelcSelectParity.lean", "RelcSelectBlock.lean", "RelcSelectSqueeze.lean", "RelcSelectC5.lean",
]
DESIGN_MODULES = sorted(f for f in os.listdir(DESIGN) if f.endswith(".lean") and f != "OIBridge.lean")
DECL = re.compile(
    r"^(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe|nonrec)\s+)*"
    r"(?P<kind>axiom|opaque|structure|class|def|abbrev|inductive|instance|theorem|lemma)\b\s*(?P<name>[^\s:({\[]*)"
)


def header_of(lines, i):
    out = []
    for j in range(i, min(i + 25, len(lines))):
        out.append(lines[j].rstrip("\n"))
        s = lines[j].rstrip()
        if ":=" in s or re.search(r"\bwhere\b\s*$", s):
            break
    return out


def pre_body(header):
    text = " ".join(h.strip() for h in header)
    cut = len(text)
    for tok in [":=", " where"]:
        k = text.find(tok)
        if k != -1:
            cut = min(cut, k)
    return text[:cut].rstrip()


def has_explicit_type(text, name):
    k = text.find(name)
    rest = text[k + len(name):] if k != -1 else text
    depth = 0
    for ch in rest:
        if ch in "([{⦃":
            depth += 1
        elif ch in ")]}⦄":
            depth -= 1
        elif ch == ":" and depth == 0:
            return True
    return False


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


def main():
    supA, supB = [], []
    propdefs = 0
    for tag, base, mods in (("K", BASE, MODULES), ("D", DESIGN, DESIGN_MODULES)):
        for mod in mods:
            with open(os.path.join(base, mod), encoding="utf-8") as fh:
                lines = fh.readlines()
            for i, line in enumerate(lines):
                m = DECL.match(line)
                if not m:
                    continue
                kind, name = m.group("kind"), m.group("name")
                header = header_of(lines, i)
                pb = pre_body(header)
                prop = bool(re.search(r"(:|→|->)\s*Prop\s*$", pb))
                if kind in ("structure", "class") and not prop:
                    dl, doc = docstring_of(lines, i)
                    supA.append((tag, mod, i + 1, kind, name, header, dl, doc, fields_of(lines, i, len(header))))
                if kind in ("def", "abbrev"):
                    if prop:
                        propdefs += 1
                    elif not has_explicit_type(pb, name):
                        supB.append((tag, mod, i + 1, kind, name, header))
    print("# I3 kernel census supplement")
    print()
    print(f"cross-check: Prop-valued def/abbrev headers = {propdefs}")
    print(f"supplement A (non-Prop structure/class): K = {sum(1 for x in supA if x[0] == 'K')}, "
          f"D = {sum(1 for x in supA if x[0] == 'D')}")
    print(f"supplement B (def/abbrev with no explicit result type): K = {sum(1 for x in supB if x[0] == 'K')}, "
          f"D = {sum(1 for x in supB if x[0] == 'D')}")
    print()
    print("## Supplement A")
    n = 0
    for (tag, mod, ln, kind, name, header, dl, doc, flds) in supA:
        n += 1
        print(f"### S{n:03d} [{tag}] {mod}:{ln} {kind} {name}")
        if doc:
            print(f"docstring {mod}:{dl}-{dl + len(doc) - 1}:")
            for d in doc:
                print("  | " + d)
        else:
            print("docstring: none")
        print("header:")
        for h in header:
            print("  > " + h)
        print("fields: " + ", ".join(f"{nm}@{l}" for l, nm in flds))
        print()
    print("## Supplement B")
    n = 0
    for (tag, mod, ln, kind, name, header) in supB:
        n += 1
        print(f"### B{n:03d} [{tag}] {mod}:{ln} {kind} {name}")
        for h in header:
            print("  > " + h)
        print()
    print("END")


if __name__ == "__main__":
    sys.exit(main())
