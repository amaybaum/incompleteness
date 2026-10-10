"""I3 quote control: every quoted fragment of an INVENTORY.md `statement` field occurs verbatim in a source at L
(or in a PT record / design module) after whitespace normalization.

DECISION RULE (fixed before the first run):
- For each record of INVENTORY.md, take the text of its `- statement` field (from "- statement" to the next line that
  starts with "- " at column 0, joined with single spaces).
- Extract every double-quoted span "...". Split each span into fragments at the separators " · ", "…" and " ... ".
  Strip each fragment of surrounding spaces and of a trailing ":=" (the extractor's cut); keep fragments of at least 25
  characters.
- Corpus: the 22 K modules, the 11 design modules and OIBridge.lean of pt/inputs/fourcopy, ROADMAP.md, the
  reconstruction round result notes, the foundations audits, papers/Main.md, and the PT records PROTOCOL-STAGE3.md,
  PROTOCOL-STAGE4.md, PROTOCOL-STAGE5.md, INTEGRATION-NOTE-STAGE3.md, INTEGRATION-NOTE-STAGE4.md,
  INTEGRATION-ADDENDUM-STAGE2.md, INTEGRATION-REVIEW.md and pt/inputs/ledgers/EQ2-SYNTHESIS.md. Each file's text is
  whitespace-normalized (every run of whitespace becomes one space).
- A fragment is FOUND if its whitespace-normalized form is a substring of some normalized corpus file; otherwise
  NOT-FOUND, printed with its record id. The summary line prints the counts. A NOT-FOUND is a transcription discrepancy
  to be corrected in INVENTORY.md (data), never by changing this rule.
- Deterministic output, no timestamps.
"""
import glob
import os
import re
import sys

PT = ".."
KMODS = ["KInfFoundations", "OrbitGeneration", "OrbitNormalization", "TransitiveBody", "StageCompletion",
         "InvariantInnerProduct", "CompletionAction", "CompositionOrder", "CompositeInterface", "CompositeDimension",
         "EffectSpace", "K1Bridge", "SharpTests", "K2Guard", "DenseOrbit", "NativeGateBall", "OddChar", "ParityNot",
         "RelcSelectParity", "RelcSelectBlock", "RelcSelectSqueeze", "RelcSelectC5"]


def corpus():
    files = [os.path.join(PT, "base", "verification", "lean-mathlib", "OIBridge", m + ".lean") for m in KMODS]
    files += sorted(glob.glob(os.path.join(PT, "inputs", "fourcopy", "*.lean")))
    files += [os.path.join(PT, "base", "verification", "ROADMAP.md"), os.path.join(PT, "base", "papers", "Main.md")]
    files += sorted(glob.glob(os.path.join(PT, "base", "verification", "programmes", "oi-qm", "reconstruction", "*",
                                           "result.md")))
    files += sorted(glob.glob(os.path.join(PT, "base", "verification", "audits", "foundations", "*.md")))
    files += [os.path.join(PT, n) for n in ["PROTOCOL-STAGE3.md", "PROTOCOL-STAGE4.md", "PROTOCOL-STAGE5.md",
                                             "INTEGRATION-NOTE-STAGE3.md", "INTEGRATION-NOTE-STAGE4.md",
                                             "INTEGRATION-ADDENDUM-STAGE2.md", "INTEGRATION-REVIEW.md"]]
    files += [os.path.join(PT, "inputs", "ledgers", "EQ2-SYNTHESIS.md")]
    texts = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            texts.append(re.sub(r"\s+", " ", fh.read()))
    return files, texts


def main():
    files, texts = corpus()
    with open("INVENTORY.md", encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    rid = None
    stmts = []
    i = 0
    while i < len(lines):
        m = re.match(r"^### (I3\.\d+) ", lines[i])
        if m:
            rid = m.group(1)
        if lines[i].startswith("- statement") and rid:
            buf = [lines[i]]
            j = i + 1
            while j < len(lines) and not lines[j].startswith("- ") and not lines[j].startswith("#"):
                buf.append(lines[j].strip())
                j += 1
            stmts.append((rid, " ".join(buf)))
            i = j
            continue
        i += 1
    checked = found = 0
    missing = []
    for rid, st in stmts:
        for span in re.findall(r'"([^"]+)"', st):
            for frag in re.split(r" · |…| \.\.\. ", span):
                frag = frag.strip()
                if frag.endswith(":="):
                    frag = frag[:-2].strip()
                if len(frag) < 25:
                    continue
                checked += 1
                nf = re.sub(r"\s+", " ", frag)
                if any(nf in t for t in texts):
                    found += 1
                else:
                    missing.append((rid, nf))
    print(f"corpus files: {len(files)}; statement fields: {len(stmts)}")
    for rid, nf in missing:
        print(f"NOT-FOUND {rid}: {nf[:300]}")
    print(f"fragments checked = {checked}; found = {found}; not found = {len(missing)}")
    print("END")


if __name__ == "__main__":
    sys.exit(main())
