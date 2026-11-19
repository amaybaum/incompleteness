#!/usr/bin/env python3
"""Locate A1-09 registry statements and evidence in a specified source checkout.

The output is a source index. It does not establish dependency or proof scope.
"""

import argparse
from bisect import bisect_right
from collections import defaultdict
from functools import cache
import json
from pathlib import Path
import re
import subprocess
import sys


DECLARATION = re.compile(
    r"^\s*(?:@\[[^\n\]]*\]\s*)?(?:(?:noncomputable|private|public|protected|local|scoped)\s+)*"
    r"(?:theorem|lemma|def|abbrev|structure|instance|class|inductive|axiom|opaque)"
    r"\s+([\w'.]+)(?=\s|[:({\[])",
    re.MULTILINE,
)
MANUSCRIPT_TOKEN = re.compile(r"(?<![\w'])\w[\w']*")
BRIDGE = Path("verification/lean-mathlib/OIBridge")
IMPORT = re.compile(r"^import\s+(OIBridge\.[\w.]+)", re.MULTILINE)
LEAN_CUES = {
    "carrier_or_type": re.compile(r"\b(?:Finite|Fintype|FiniteDimensional|Fin|ZMod)\b"),
    "set_or_count": re.compile(r"\b(?:Finset|Nat\.card|Fintype\.card|Set\.Finite)\b"),
    "iterate_or_return": re.compile(
        r"\b(?:orderOf|exists_ne_map_eq_of_infinite|surjective_of_injective|"
        r"iterate|FiniteOrderOn|[Ii]dentityReturn)\b"
    ),
}


@cache
def declare(path):
    source = read(path)
    offsets = [match.start() for match in re.finditer("\n", source)]
    return [(match[1], line_at(offsets, match.start(1))) for match in DECLARATION.finditer(source)]


@cache
def read(path):
    return path.read_text(encoding="utf-8")


def line_at(newlines, offset):
    return bisect_right(newlines, offset) + 1


@cache
def flattened(path):
    source = read(path)
    parts = list(re.finditer(r"\s+|\S+", source))
    newlines = [match.start() for match in re.finditer("\n", source)]
    offsets = []
    cursor = 0
    for part in parts:
        offsets.append(cursor)
        cursor += 1 if part[0].isspace() else len(part[0])
    return re.sub(r"\s+", " ", source), parts, offsets, newlines


def anchor_lines(path, anchor):
    flat, parts, offsets, newlines = flattened(path)
    for match in re.finditer(re.escape(anchor), flat):
        index = bisect_right(offsets, match.start()) - 1
        yield line_at(newlines, parts[index].start())


def registry_index(root):
    registry = json.loads(read(root / "verification/lean-manuscript-census.json"))
    families = registry["families"]
    module_names = defaultdict(set)
    for module in sorted((root / BRIDGE).glob("*.lean")):
        for name, _ in declare(module):
            module_names[name.rsplit(".", 1)[-1]].add(module.stem)

    no_anchor = {module for family in families if not family["manuscript"] for module in family["modules"]}
    unique_names = {
        name: next(iter(modules))
        for name, modules in module_names.items()
        if len(modules) == 1 and modules <= no_anchor and (len(name) >= 12 or "_" in name)
    }
    mentions = defaultdict(set)
    # FULL is recorded below alongside its chapter copies so that duplicate surfaces remain visible.
    for directory in ["papers", "book"]:
        for path in sorted((root / directory).glob("*.md")):
            for number, line in enumerate(read(path).splitlines(), 1):
                for token in MANUSCRIPT_TOKEN.findall(line):
                    if token in unique_names:
                        mentions[unique_names[token]].add((str(path.relative_to(root)), number, token))

    rows = []
    for family in families:
        anchors = [
            dict(anchor, lines=list(anchor_lines(root / anchor["file"], anchor["anchor"])))
            for anchor in family["manuscript"]
        ]
        rows.append({
            "name": family["name"],
            "status": family["status"],
            "modules": family["modules"],
            "anchors": anchors,
            "mention_candidates": sorted({
                mention for module in family["modules"] for mention in mentions[module]
            }),
        })

    supersessions = []
    for old, new in registry["supersessions"].items():
        supersessions.append({
            "old": old,
            "new": new,
            "successor_modules": sorted(module_names.get(new, set())),
        })
    return rows, supersessions


def coverage_index(root):
    ledger = json.loads(read(root / "verification/coverage/LEDGER.json"))
    result = subprocess.run(
        [sys.executable, "-I", "-B", str(root / "tools/proof_census.py"), "--json"],
        capture_output=True, text=True, check=True, timeout=30,
    )
    statements = {row["id"]: row for row in json.loads(result.stdout)}
    rows = []
    for entry in ledger["entries"]:
        checks = []
        for check in entry["checks"]:
            path = root / check["path"]
            record = dict(check, exists=path.is_file())
            if check["kind"] == "lean" and path.is_file():
                identifiers = check.get("names", [])
                if not identifiers and check.get("basis") == "named":
                    identifiers = [check["evidence"]]
                record["declarations"] = {
                    name: [line for declared, line in declare(path)
                           if declared.rsplit(".", 1)[-1] == name.rsplit(".", 1)[-1]]
                    for name in identifiers
                }
            if check.get("basis") == "named" and path.is_file():
                source = read(path)
                offsets = [match.start() for match in re.finditer("\n", source)]
                record["evidence_lines"] = [
                    line_at(offsets, match.start())
                    for match in re.finditer(re.escape(check["evidence"]), source, re.IGNORECASE)
                ]
            checks.append(record)
        statement = statements.get(entry["id"])
        rows.append({
            "id": entry["id"],
            "recorded_line": entry["line"],
            "ledger_paper": entry["paper"],
            "grade": entry["kernel"],
            "fingerprint_matches": statement is not None and statement["fingerprint"] == entry["fingerprint"],
            "statement": statement,
            "checks": checks,
        })
    registered = {row["id"] for row in rows}
    unattached = [dict(row, exists=(root / row["path"]).is_file()) for row in ledger["unattached"]]
    return rows, sorted(statements.keys() - registered), unattached


def lean_source_index(root):
    bridge = root / BRIDGE
    files = [bridge.with_suffix(".lean"), *sorted(bridge.rglob("*.lean"))]
    files.extend(sorted((root / "verification/lean").rglob("*.lean")))
    rows = []
    for path in files:
        source = read(path)
        lines = source.splitlines()
        rows.append({
            "file": str(path.relative_to(root)),
            "imports": IMPORT.findall(source),
            "declaration_candidates": declare(path),
            "cue_lines": {
                label: [number for number, line in enumerate(lines, 1) if pattern.search(line)]
                for label, pattern in LEAN_CUES.items()
            },
        })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--lean", action="store_true", help="also index Lean sources and finite-object cues")
    args = parser.parse_args()
    root = args.checkout.resolve()
    families, supersessions = registry_index(root)
    entries, unregistered, unattached = coverage_index(root)
    index = {
        "families": families,
        "supersessions": supersessions,
        "entries": entries,
        "unregistered_statements": unregistered,
        "unattached": unattached,
    }
    if args.lean:
        index["lean_sources"] = lean_source_index(root)
    print(json.dumps(index, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
