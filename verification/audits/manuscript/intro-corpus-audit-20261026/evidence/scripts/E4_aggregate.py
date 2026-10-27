#!/usr/bin/env python3
"""E4: aggregate the evidence verification of step 7 (parts E1-E3) into one evidence level per matrix row.

Reads matrix.json (each row's chain) and evidence/part-E1.json, part-E2.json and part-E3.json. Writes evidence.json and
renders EVIDENCE.md from it. merge_matrix.py then copies each row's level into matrix.json.

The rule (EVIDENCE.md states it in prose):
- Levels, strongest first: reproduced, certificate-checked, traced-only. "failed" is separate and overrides.
- Evidence-bearing chain layers: kernel, exhaustive-computation, numerical, exact-algebra. Links of the other layers
  (paper-derivation, literature, conjecture, none) have no artifact of a step-7 type; steps 2-3 verified their status.
- A kernel link whose source is a file, not a declaration (a retained result, the coverage ledger), is matched to
  the E1 or E3 items that name the same file; it takes the weakest such item's level, and no match counts as
  traced-only.
- A kernel link is matched by its declaration (the module and name of its `lean:Module:line:Name` source) to the E1
  items of type lean-certificate and formal-coverage that name the same declaration. Its level is the weaker of the two
  matches; a missing match counts as traced-only.
- An exhaustive-computation, numerical or exact-algebra link is matched to the E2 items of type exhaustive-computation
  or numerical that list the row's id. Its level is the weakest matched item's; no match counts as traced-only.
- A row whose id an item with outcome "fail" lists is "failed".
- A row with no evidence-bearing link but with ci-receipt items listing it (claims about the build, the toolchain or
  CI) takes the weakest of those items' levels.
- Otherwise a row's level is its weakest evidence-bearing link's. A row with no evidence-bearing link is traced-only,
  with basis "no step-7 artifact".
- Otherwise, items of type ci-receipt and open-obligation that list a row are recorded with it as context and do not
  set its level. Matched items with outcome "partial" are listed with the row.

Usage (from the audit directory): python3 -I -B evidence/scripts/E4_aggregate.py [--check]
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AUDIT = Path(__file__).resolve().parents[2]
RANK = {"traced-only": 1, "certificate-checked": 2, "reproduced": 3}
BEARING = ("kernel", "exhaustive-computation", "numerical", "exact-algebra")
KERNEL_TYPES = ("lean-certificate", "formal-coverage")
COMPUTE_TYPES = ("exhaustive-computation", "numerical")
CONTEXT_TYPES = ("ci-receipt", "open-obligation")
DECL = re.compile(r"^lean:(?:OIBridge/)?([A-Za-z0-9_/]+?)(?:\.lean)?:(\d+):([^\s]+)(?:\s+\(.*\))?$")


def decl_key(source):
    """(module, short name) of a `lean:Module:line:Name` source, or None."""
    m = DECL.match(source.strip())
    if not m:
        return None
    return m.group(1).split("/")[-1], m.group(3).split(".")[-1]


def path_key(source):
    """The repository path of a file source, without its `@commit` and `:line` suffixes."""
    s = source.strip().split("@")[0]
    return re.sub(r":[\d\-]+$", "", s)


def weakest(levels):
    return min(levels, key=lambda lv: RANK[lv]) if levels else "traced-only"


def load():
    rows = json.loads((AUDIT / "matrix.json").read_text(encoding="utf-8"))["rows"]
    items = []
    for part in ("E1", "E2", "E3"):
        for it in json.loads((AUDIT / "evidence" / f"part-{part}.json").read_text(encoding="utf-8")):
            items.append(dict(it, part=part))
    return rows, items


def aggregate(rows, items):
    ids = {r["id"] for r in rows}
    by_claim = defaultdict(list)
    by_finding = defaultdict(list)
    for it in items:
        for c in it["claims"]:
            (by_claim if c in ids else by_finding)[c].append(it["item"])
    by_item = {it["item"]: it for it in items}
    by_decl, by_path = defaultdict(list), defaultdict(list)
    for it in items:
        for s in it["sources"]:
            k = decl_key(s)
            if k and it["type"] in KERNEL_TYPES:
                by_decl[k].append(it["item"])
            elif not k and it["type"] in KERNEL_TYPES + ("ci-receipt",):
                by_path[path_key(s)].append(it["item"])
    claims = {}
    for r in rows:
        attached = [by_item[i] for i in by_claim.get(r["id"], [])]
        failed = [it["item"] for it in attached if it["outcome"] == "fail"]
        links, partial = [], set()
        for ln in r["chain"]:
            layer = ln.get("layer")
            if layer not in BEARING:
                continue
            entry = {"source": ln.get("source"), "layer": layer}
            if layer == "kernel" and not decl_key(ln.get("source", "")):
                found = sorted(set(by_path.get(path_key(ln.get("source", "")), [])))
                lv = [by_item[i]["evidence_level"] for i in found if by_item[i]["evidence_level"] in RANK]
                entry.update(items=found, level=weakest(lv),
                             gap=[] if found else ["kernel-layer link without a declaration source; no item names its file"])
            elif layer == "kernel":
                k = decl_key(ln.get("source", ""))
                found = sorted(set(by_decl.get(k, []))) if k else []
                cert = [by_item[i]["evidence_level"] for i in found if by_item[i]["type"] == "lean-certificate"]
                cov = [by_item[i]["evidence_level"] for i in found if by_item[i]["type"] == "formal-coverage"]
                lv = [weakest([x for x in cert if x in RANK]), weakest([x for x in cov if x in RANK])]
                entry.update(items=found, level=weakest(lv),
                             gap=[g for g, xs in (("no lean-certificate item", cert), ("no formal-coverage item", cov))
                                  if not xs])
            else:
                found = [it["item"] for it in attached if it["type"] in COMPUTE_TYPES]
                lv = [by_item[i]["evidence_level"] for i in found if by_item[i]["evidence_level"] in RANK]
                entry.update(items=found, level=weakest(lv), gap=[] if found else ["no computation item"])
            partial.update(i for i in entry["items"] if by_item[i]["outcome"] == "partial")
            links.append(entry)
        if failed:
            level, basis = "failed", "an item listing the row failed: " + ", ".join(failed)
        elif links:
            level = weakest([e["level"] for e in links])
            basis = "weakest evidence-bearing link"
        elif any(it["type"] == "ci-receipt" for it in attached):
            ci = [it["evidence_level"] for it in attached if it["type"] == "ci-receipt" and it["evidence_level"] in RANK]
            level, basis = weakest(ci), "CI-receipt items, for a row with no evidence-bearing link"
            partial.update(it["item"] for it in attached if it["type"] == "ci-receipt" and it["outcome"] == "partial")
        else:
            level, basis = "traced-only", "no step-7 artifact (paper, literature, conjecture or none)"
        claims[r["id"]] = {
            "evidence_level": level, "basis": basis, "verdict": r["verdict"], "proof_status": r["proof_status"],
            "links": links, "failed_items": failed, "partial_items": sorted(partial),
            "context_items": [it["item"] for it in attached if it["type"] in CONTEXT_TYPES],
        }
    return claims, dict(by_finding)


def counts(claims):
    lv = Counter(c["evidence_level"] for c in claims.values())
    bearing = Counter(c["evidence_level"] for c in claims.values() if c["links"])
    return {"rows": len(claims), "by_level": dict(lv), "rows_with_evidence_bearing_links": sum(bearing.values()),
            "by_level_among_evidence_bearing": dict(bearing)}


def build():
    rows, items = load()
    claims, findings = aggregate(rows, items)
    item_counts = Counter((it["part"], it["evidence_level"], it["outcome"]) for it in items)
    return {
        "_note": "Generated by evidence/scripts/E4_aggregate.py from matrix.json and evidence/part-E1..E3.json; "
                 "the rule is stated in the script and in EVIDENCE.md.",
        "counts": counts(claims),
        "items": {"total": len(items), "by_part_level_outcome": [list(k) + [v] for k, v in sorted(item_counts.items())]},
        "claims": claims,
        "finding_items": {k: sorted(v) for k, v in sorted(findings.items())},
    }


def render(ev, items):
    by_item = {it["item"]: it for it in items}
    c = ev["counts"]
    order = ["reproduced", "certificate-checked", "traced-only", "failed"]
    L = ["# Evidence verification (step 7): the evidence layer of the matrix", "",
         "This file aggregates the three evidence parts into one evidence level per matrix row. It is rendered from "
         "`evidence.json` by `evidence/scripts/E4_aggregate.py`; the parts are `evidence/part-E1.md` (Lean "
         "certificates and formal coverage), `evidence/part-E2.md` (exhaustive computations and numerics) and "
         "`evidence/part-E3.md` (CI receipts and open obligations).", "",
         "## The rule", "",
         "- **Levels,** strongest first: *reproduced* (the audit regenerated the result and compared it), "
         "*certificate-checked* (checked against a retained certificate, expected result or kernel output) and "
         "*traced-only* (traced to a report whose evidence the audit did not check). *Failed* is separate: a row that "
         "an item with outcome *fail* lists is failed, whatever its other links.",
         "- **Evidence-bearing links** are those of layer kernel, exhaustive-computation, numerical or exact-algebra. "
         "Paper derivations, literature, conjectures and links with no support have no artifact of a step-7 type; "
         "steps 2–3 verified their status, and step 7 adds nothing to them.",
         "- **A kernel link** is matched by its declaration to the E1 items that name it: a *lean-certificate* item "
         "(name, axioms, kernel acceptance) and a *formal-coverage* item (the manuscript claim against the Lean "
         "statement). It takes the weaker of the two; a missing item counts as traced-only. A kernel-layer link whose "
         "source is a file rather than a declaration (a retained result, the coverage ledger) is matched to the E1 or "
         "E3 items naming that file, and takes the weakest of them.",
         "- **An exhaustive-computation, numerical or exact-algebra link** is matched to the E2 computation items "
         "that list the row. It takes the weakest; no match counts as traced-only.",
         "- **A row** takes its weakest evidence-bearing link. A row with no evidence-bearing link takes the weakest "
         "of the CI-receipt items that list it, if there are any (claims about the build, the toolchain or CI); "
         "otherwise it is traced-only, on the basis *no step-7 artifact*.",
         "- Otherwise, CI-receipt and open-obligation items that list a row are recorded with it as context. They "
         "state limits; they do not set its level.", "",
         "## Counts", "",
         "| Evidence level | All rows | Rows with evidence-bearing links |", "|---|--:|--:|"]
    for lv in order:
        L.append(f"| {lv} | {c['by_level'].get(lv, 0)} | {c['by_level_among_evidence_bearing'].get(lv, 0)} |")
    L.append(f"| **Total** | **{c['rows']}** | **{c['rows_with_evidence_bearing_links']}** |")
    L += ["", f"Items: {ev['items']['total']} (E1–E3). By part, level and outcome:", "",
          "| Part | Level | Outcome | Items |", "|---|---|---|--:|"]
    for p, lv, oc, n in ev["items"]["by_part_level_outcome"]:
        L.append(f"| {p} | {lv} | {oc} | {n} |")
    claims = ev["claims"]
    failed = sorted(k for k, v in claims.items() if v["evidence_level"] == "failed")
    L += ["", "## Failed rows", ""]
    for k in failed:
        v = claims[k]
        L.append(f"- **{k}** ({v['verdict']}, {v['proof_status']}): {v['basis']}. "
                 + " ".join(f"{i}: {by_item[i]['outcome']}, \"{by_item[i]['what'][:160]}…\"" for i in v["failed_items"]))
    if not failed:
        L.append("None.")
    gaps = sorted(k for k, v in claims.items() if v["evidence_level"] == "traced-only" and v["links"])
    L += ["", "## Evidence-bearing rows left at traced-only", "",
          "Each row below has a kernel or computation link that no evidence item reached, or reached only at "
          "traced-only.", "", "| Row | Verdict | Proof status | Link | Gap |", "|---|---|---|---|---|"]
    for k in gaps:
        v = claims[k]
        for e in v["links"]:
            if e["level"] == "traced-only":
                L.append(f"| {k} | {v['verdict']} | {v['proof_status']} | `{e['source']}` ({e['layer']}) | "
                         f"{'; '.join(e['gap']) or 'matched only at traced-only: ' + ', '.join(e['items'])} |")
    L += ["", "## Matrix labels that disagree with the chains", "",
          "The evidence rule reads the chain's layers. These rows' labels disagree with their own chains; each is a "
          "correction for the matrix, recorded here and not applied.", ""]
    strong = ("proved-kernel", "exhaustive-exact", "numerical")
    noart = sorted(k for k, v in claims.items() if v["proof_status"] in strong and not v["links"])
    L.append("- **Proof status implies an artifact, but the chain has no evidence-bearing link:** "
             + (", ".join(f"{k} ({claims[k]['proof_status']}; evidence {claims[k]['evidence_level']}, "
                          f"{claims[k]['basis']})" for k in noart) or "none") + ".")
    mislab = sorted({(k, e["source"]) for k, v in claims.items() for e in v["links"]
                     if e["layer"] == "kernel" and not e["source"].startswith("lean:")
                     and not e["items"]})
    L.append("- **Kernel-layer links whose source is a paper, ledger or roadmap line, not a declaration or a "
             "certified file:** " + ("; ".join(f"{k} `{s}`" for k, s in mislab) or "none") + ". Each holds its row at "
             "traced-only under the weakest-link rule.")
    part = sorted(k for k, v in claims.items() if v["partial_items"])
    L += ["", "## Rows resting on partial items", "",
          "The level stands; the partial item's limits apply to the row (see the part files).", "",
          "| Row | Level | Partial items |", "|---|---|---|"]
    for k in part:
        L.append(f"| {k} | {claims[k]['evidence_level']} | {', '.join(claims[k]['partial_items'])} |")
    L += ["", "## Limits that apply across rows", "",
          "- No Lean toolchain is available here, so no kernel item is *reproduced*: *certificate-checked* is the "
          "highest level a kernel link can reach (E1).",
          "- The CI jobs examined replayed the OIBridge build from the Actions cache (E1-122, E3-11). Their axiom "
          "reports are the retained certificate; a fresh elaboration is proposed for owner authorization.",
          "- Kernel declarations outside the 14 retained modules have axiom reports only in CI logs that expire "
          "(E3-14).", "",
          "## Proposed for owner authorization (not dispatched)", "",
          "- A fresh-build CI reproduction of `introduction_repro` at `17b830bc`.",
          "- An extended expected result covering the additional modules (OD-15), made before their CI logs expire.",
          "- BHa and BHb `mutants.py` replays in CI (E2).", ""]
    return "\n".join(L)


def main():
    ev = build()
    _, items = load()
    text_json = json.dumps(ev, indent=1, ensure_ascii=False) + "\n"
    text_md = render(ev, items)
    out_json, out_md = AUDIT / "evidence.json", AUDIT / "EVIDENCE.md"
    if "--check" in sys.argv[1:]:
        ok = out_json.exists() and out_json.read_text(encoding="utf-8") == text_json \
            and out_md.exists() and out_md.read_text(encoding="utf-8") == text_md
        print("evidence.json and EVIDENCE.md match" if ok else "evidence.json or EVIDENCE.md differs from the rendering")
        sys.exit(0 if ok else 1)
    out_json.write_text(text_json, encoding="utf-8")
    out_md.write_text(text_md, encoding="utf-8")
    print(json.dumps(ev["counts"]))


if __name__ == "__main__":
    main()
