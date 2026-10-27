#!/usr/bin/env python3
"""E4: aggregate the evidence verification of step 7 (parts E1-E3) into one evidence level per matrix row.

Reads matrix.json (each row's chain, after matrix/chain-relabels.json) and evidence/part-E1.json, part-E2.json and
part-E3.json. Writes evidence.json and renders EVIDENCE.md from it. merge_matrix.py then copies each row's level into
matrix.json; the order is merge_matrix.py, this script, merge_matrix.py, render_matrix.py.

The level grades the evidence for the row's chain as the matrix records it, not the claim: for a row whose chain
refutes the claim it grades the counter-evidence, which is recorded as the row's artifact level. The rule
(EVIDENCE.md states it in prose):

- Levels, strongest first: reproduced, certificate-checked, traced-only. "failed" is separate and overrides.
- Each link gets a level.
  - kernel, with a declaration source (`lean:Module:line:Name`): matched by (module, short name) to the E1 items of
    type lean-certificate and formal-coverage naming it, leaving out a formal-coverage item whose not_covered names
    the row. The link takes the weaker of the two; a missing item counts as traced-only.
  - kernel, with a file source (a retained result): matched by path to the items of type lean-certificate,
    formal-coverage or ci-receipt naming that file.
  - exhaustive-computation, numerical, exact-algebra: matched to the items listing the row that are of type
    exhaustive-computation or numerical, or are ci-receipt replays of a whole record (a directory source), except an
    item that names research records or probe files of which the link names none (the link names others), and, for a
    link that names manuscript lines and no record or probe file, an item that names none of those manuscript files
    (matched by file, not by line range).
    The link takes the weakest matched item.
  - none, in a chain of none links only (claims about the build, the toolchain, CI or the records): the weakest of
    the ci-receipt items listing the row.
  - Every other link (paper-derivation, literature, conjecture, or none beside other layers) is traced-only: step 7
    has no artifact type for it, and steps 2-3 verified its status.
  - A matched item with outcome "fail" fails the link. A link whose status is not "proved" counts as traced-only for
    the row, whatever its artifact.
- The load-bearing links of a row: for proved-kernel, its kernel links, or all its links if it has none; its paper,
  literature, computation and none links restate the result in the corpus, check it in parallel or record related
  obligations, and are recorded without grading the row; for proved-paper, exhaustive-exact, numerical
  and calibration, all its links. A row whose proof status is open, conditional, conjecture or unsupported is
  traced-only: the chain does not establish the claim, so no artifact raises it.
- A row is "failed" when an item listing it has outcome "fail" (the item's failure_scope says what failed) or a
  load-bearing link failed. Otherwise it takes its weakest load-bearing link.
- Every row also records its artifact level: the weakest level over its evidence-bearing links (kernel, computation
  and all-none links), or none; for an UNSUPPORTED or OVERCLAIM row with no such link, the computation items listing
  it, as counter-evidence. For a row graded traced-only by its status or by a paper step, this says what the
  checked artifacts reach.

Usage (from the audit directory): python3 -I -B evidence/scripts/E4_aggregate.py [--check]
--check exits 1 if evidence.json or EVIDENCE.md differs from the rendering, if any matrix.json row's
evidence_level or evidence_basis differs from evidence.json's, or if matrix.json's chains do not carry exactly the
corrections of matrix/chain-relabels.json. merge_matrix.py --check checks matrix.json against the part files.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AUDIT = Path(__file__).resolve().parents[2]
RANK = {"traced-only": 1, "certificate-checked": 2, "reproduced": 3}
COMPUTE_LAYERS = ("exhaustive-computation", "numerical", "exact-algebra")
KERNEL_TYPES = ("lean-certificate", "formal-coverage")
COMPUTE_TYPES = ("exhaustive-computation", "numerical")
CONTEXT_TYPES = ("ci-receipt", "open-obligation")
BY_ALL_LINKS = ("proved-paper", "exhaustive-exact", "numerical", "calibration")
BY_STATUS = ("open", "conditional", "conjecture", "unsupported")
DECL = re.compile(r"^lean:(?:OIBridge/)?([A-Za-z0-9_/]+?)(?:\.lean)?:(\d+):([^\s]+)(?:\s+\(.*\))?$")
PATH = re.compile(r"(?:\.github|papers|verification|book|tools)/[^\s;,@]*")


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


def paths(source):
    """Every repository path named in a link or item source."""
    return {re.sub(r":[\d\-]+$", "", p) for p in PATH.findall(source)}


def artifacts(ps):
    """The research records (verification/programmes/<programme>/<record>) and probe files that paths name."""
    out = set()
    for p in ps:
        parts = p.rstrip("/").split("/")
        if p.startswith("verification/programmes/") and len(parts) >= 4:
            out.add("/".join(parts[:4]))
        elif p.startswith("papers/oi_lattice_code/"):
            out.add(p)
    return out


def manuscripts(ps):
    """The manuscript files (papers/*.md, book/*.md) that paths name."""
    return {p for p in ps if p.endswith(".md") and (p.startswith("papers/") or p.startswith("book/"))}


def contradicted(link_paths, item):
    """True when the item cannot be the check of this link: the link and the item both name records or probe files
    and none is common, or the link names manuscript lines and no record or probe file, and the item names none of
    those manuscript files (a check of a record or probe is not a check of a paper's derivation)."""
    item_paths = {q for s in item["sources"] for q in paths(s)}
    a, b = artifacts(link_paths), artifacts(item_paths)
    if a:
        return bool(b) and not (a & b)
    m = manuscripts(link_paths)
    return bool(m) and not (m & item_paths)


def weakest(levels):
    return min(levels, key=lambda lv: RANK[lv]) if levels else "traced-only"


def item_level(it):
    return "failed" if it["outcome"] == "fail" else it["evidence_level"]


def combine(levels):
    """failed if any is failed, else the weakest (traced-only if empty)."""
    return "failed" if "failed" in levels else weakest(levels)


def load():
    rows = json.loads((AUDIT / "matrix.json").read_text(encoding="utf-8"))["rows"]
    items = []
    for part in ("E1", "E2", "E3"):
        for it in json.loads((AUDIT / "evidence" / f"part-{part}.json").read_text(encoding="utf-8")):
            items.append(dict(it, part=part))
    return rows, items


def grade_link(r, k, ln, attached, by_item, by_decl, by_path, all_none):
    layer, src = ln.get("layer"), ln.get("source", "")
    e = {"index": k, "source": src, "layer": layer, "link_status": ln.get("link_status"), "items": [], "gap": []}
    if layer == "kernel" and decl_key(src):
        found = sorted(set(by_decl.get(decl_key(src), [])))
        excl = [i for i in found if r["id"] in by_item[i].get("not_covered", {})]
        use = [i for i in found if i not in excl]
        cert = [item_level(by_item[i]) for i in use if by_item[i]["type"] == "lean-certificate"]
        cov = [item_level(by_item[i]) for i in use if by_item[i]["type"] == "formal-coverage"]
        e["items"] = use
        e["gap"] = [g for g, xs in (("no lean-certificate item", cert), ("no formal-coverage item", cov)) if not xs]
        e["gap"] += [f"{i} does not cover this row: {by_item[i]['not_covered'][r['id']]}" for i in excl]
        e["level"] = combine([combine(cert), combine(cov)])
        e["bearing"] = True
    elif layer == "kernel":
        found = sorted(set(by_path.get(path_key(src), [])))
        e["items"] = found
        e["gap"] = [] if found else ["kernel-layer link without a declaration source; no item names its file"]
        e["level"] = combine([item_level(by_item[i]) for i in found])
        e["bearing"] = True
    elif layer in COMPUTE_LAYERS:
        lp = paths(src)
        cand = [it for it in attached if it["type"] in COMPUTE_TYPES
                or (it["type"] == "ci-receipt" and any(s.split("@")[0].endswith("/") for s in it["sources"]))]
        found = [it["item"] for it in cand if not contradicted(lp, it)]
        e["items"] = found
        e["not_matched"] = [it["item"] for it in cand if contradicted(lp, it)]
        why = ("listed items name other records or probes" if artifacts(lp)
               else "listed items do not name this manuscript file")
        e["gap"] = [] if found else ["no computation item for this link" + (
            " (%s: %s)" % (why, ", ".join(e["not_matched"])) if e["not_matched"] else "")]
        e["level"] = combine([item_level(by_item[i]) for i in found])
        e["bearing"] = True
    elif layer == "none" and all_none:
        found = [it["item"] for it in attached if it["type"] == "ci-receipt"]
        e["items"] = found
        e["gap"] = [] if found else ["no ci-receipt item lists the row"]
        e["level"] = combine([item_level(by_item[i]) for i in found])
        e["bearing"] = True
    else:
        e["level"] = "traced-only"
        e["gap"] = ["no step-7 artifact type (%s)" % layer]
        e["bearing"] = False
    return e


def aggregate(rows, items):
    ids = {r["id"] for r in rows}
    by_claim, by_finding = defaultdict(list), defaultdict(list)
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
        chain = r["chain"]
        all_none = bool(chain) and all(ln.get("layer") == "none" for ln in chain)
        links = [grade_link(r, k, ln, attached, by_item, by_decl, by_path, all_none)
                 for k, ln in enumerate(chain)]
        st = r["proof_status"]
        kernel = [e for e in links if e["layer"] == "kernel"]
        if st == "proved-kernel" and kernel:
            load_bearing, scope = kernel, "its kernel links"
        else:
            load_bearing, scope = links, "all its links"
        tag_failed = [it["item"] for it in attached if it["outcome"] == "fail"]
        link_failed = [e["index"] for e in load_bearing if e["level"] == "failed"]
        bearing = [e for e in links if e["bearing"]]
        artifact = combine([e["level"] for e in bearing]) if bearing else None
        refuting = any(e["link_status"] == "refuted" and e["bearing"] for e in links)
        listed = [it for it in attached if it["type"] in COMPUTE_TYPES]
        if artifact is None and listed and r["verdict"] in ("UNSUPPORTED", "OVERCLAIM"):
            # A computation that refutes a claim with no artifact link in its chain (E2-13 for I-123, I-124).
            artifact, refuting = combine([item_level(it) for it in listed]), True
        weak = [e for e in load_bearing if e["link_status"] != "proved" or e["level"] == "traced-only"]
        if tag_failed or link_failed:
            level = "failed"
            parts = [f"{i} failed: {by_item[i].get('failure_scope') or by_item[i]['limits']}" for i in tag_failed]
            parts += [f"load-bearing link {k} matched a failed item" for k in link_failed]
            basis = "; ".join(parts)
        elif st in BY_STATUS:
            level = "traced-only"
            basis = f"proof status {st}: the chain does not establish the claim"
        elif st not in BY_ALL_LINKS and st != "proved-kernel":
            raise SystemExit(f"{r['id']}: unknown proof status {st!r}")
        else:
            level = weakest([e["level"] if e["link_status"] == "proved" else "traced-only" for e in load_bearing])
            if level == "traced-only":
                why = sorted({e["layer"] if not e["bearing"] else
                              ("link not proved" if e["link_status"] != "proved" else "unmatched " + e["layer"])
                              for e in weak})
                basis = f"weakest of {scope}: traced-only ({', '.join(why)})"
            else:
                basis = f"weakest of {scope}"
        partial = sorted({i for e in load_bearing for i in e["items"] if by_item[i]["outcome"] == "partial"})
        claims[r["id"]] = {
            "evidence_level": level, "basis": basis, "artifact_level": artifact,
            "artifact_role": ("counter-evidence" if refuting else "support") if artifact else None,
            "verdict": r["verdict"], "proof_status": st, "load_bearing": scope,
            "links": links, "failed_items": tag_failed, "partial_items": partial,
            "context_items": [it["item"] for it in attached if it["type"] in CONTEXT_TYPES],
        }
    return claims, dict(by_finding)


def counts(claims):
    lv = Counter(c["evidence_level"] for c in claims.values())
    by_status = Counter((c["proof_status"], c["evidence_level"]) for c in claims.values())
    art = Counter(c["artifact_level"] for c in claims.values()
                  if c["evidence_level"] == "traced-only" and c["artifact_level"] not in (None, "traced-only"))
    return {"rows": len(claims), "by_level": dict(lv),
            "by_status_level": [list(k) + [v] for k, v in sorted(by_status.items())],
            "traced_only_rows_with_checked_artifacts": dict(art)}


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


def render(ev, items, relabels):
    c = ev["counts"]
    order = ["reproduced", "certificate-checked", "traced-only", "failed"]
    claims = ev["claims"]
    L = ["# Evidence verification (step 7): the evidence layer of the matrix", "",
         "This file aggregates the three evidence parts into one evidence level per matrix row. It is rendered from "
         "`evidence.json` by `evidence/scripts/E4_aggregate.py`; the parts are `evidence/part-E1.md` (Lean "
         "certificates and formal coverage), `evidence/part-E2.md` (exhaustive computations and numerics) and "
         "`evidence/part-E3.md` (CI receipts and open obligations).", "",
         "## The rule", "",
         "The level grades the evidence for the row's chain, not the claim. For a row whose chain refutes the claim, "
         "the checked artifact is counter-evidence, and its level is recorded as the row's artifact level.", "",
         "- **Levels,** strongest first: *reproduced* (the audit regenerated the result and compared it), "
         "*certificate-checked* (checked against a retained certificate, expected result or kernel output) and "
         "*traced-only* (traced to a report whose evidence the audit did not check, or a step with no artifact of a "
         "step-7 type). *Failed* is separate and overrides.",
         "- **Each link gets a level.**",
         "  - *A kernel link* with a declaration source is matched by declaration to the E1 items naming it: a "
         "*lean-certificate* item (name, axioms, kernel acceptance) and a *formal-coverage* item (the manuscript claim "
         "against the Lean statement). It takes the weaker; a missing item counts as traced-only. A formal-coverage "
         "item that records it does not cover the row is left out for that row. A kernel link whose source is a file "
         "(a retained result) is matched to the lean-certificate, formal-coverage or CI-receipt items naming that file.",
         "  - *An exhaustive-computation, numerical or exact-algebra link* is matched to the items listing the row "
         "that are computations, or replays of a whole research record (CI-receipt items whose source is the record's "
         "directory). An item is not matched to a link that names other research records or probe files than the "
         "item does (a BH-01 item does not reach a BH-02 link), nor to a link that names only manuscript lines "
         "in files the item does not name (a check of a record is not a check of a paper's derivation; the match is by "
         "file, not by line range). It takes the weakest "
         "matched item.",
         "  - *A link with no support (layer none)*, in a chain of such links only, is a claim about the build, the "
         "toolchain, CI or the records. It takes the weakest of the CI-receipt items listing the row.",
         "  - *Every other link* (paper derivation, literature, conjecture) is traced-only: step 7 has no artifact "
         "type for it, and steps 2–3 verified its status.",
         "  - A matched item with outcome *fail* fails the link. A link whose status is not *proved* counts as "
         "traced-only for the row, whatever its artifact.",
         "- **The load-bearing links.** For a proved-kernel row, its kernel links. Its other links restate the result "
         "in the corpus, check it in parallel or record related obligations; they are recorded and do not grade it. For a proved-paper, exhaustive-exact, "
         "numerical or calibration row, all its links, so a paper step in the chain holds the row at traced-only "
         "whatever its computations reach. A row whose proof status is open, conditional, conjecture or unsupported "
         "is traced-only, since its chain does not establish the claim.",
         "- **A row** is *failed* when an item listing it fails, with the item's failure scope as the basis, or when "
         "a load-bearing link fails. Otherwise it takes its weakest load-bearing link.",
         "- **The artifact level** of a row is the weakest level over its kernel, computation and build links. For a "
         "row held at traced-only by its status or by a paper step, it records what the checked artifacts reach. For an "
         "UNSUPPORTED or OVERCLAIM row whose chain has no such link, it grades the computation items listing the row, "
         "as counter-evidence.",
         "- CI-receipt and open-obligation items that list a row are recorded with it as context; apart from the "
         "two uses above, they do not set its level.", "",
         "## Counts", "",
         "| Evidence level | Rows |", "|---|--:|"]
    for lv in order:
        L.append(f"| {lv} | {c['by_level'].get(lv, 0)} |")
    L.append(f"| **Total** | **{c['rows']}** |")
    st_order = ["proved-kernel", "exhaustive-exact", "numerical", "calibration", "proved-paper",
                "conditional", "open", "conjecture", "unsupported"]
    tab = defaultdict(dict)
    for st, lv, n in c["by_status_level"]:
        tab[st][lv] = n
    L += ["", "By proof status:", "", "| Proof status | " + " | ".join(order) + " |", "|---|" + "--:|" * len(order)]
    for st in st_order:
        if st in tab:
            L.append(f"| {st} | " + " | ".join(str(tab[st].get(lv, 0)) for lv in order) + " |")
    art = c["traced_only_rows_with_checked_artifacts"]
    L += ["", "Traced-only rows whose checked artifacts reach a higher level: "
          + (", ".join(f"{n} {lv}" for lv, n in sorted(art.items(), key=lambda x: -RANK[x[0]])) or "none")
          + " (listed below).", "",
          f"Items: {ev['items']['total']} (E1–E3). By part, level and outcome:", "",
          "| Part | Level | Outcome | Items |", "|---|---|---|--:|"]
    for p, lv, oc, n in ev["items"]["by_part_level_outcome"]:
        L.append(f"| {p} | {lv} | {oc} | {n} |")
    failed = sorted(k for k, v in claims.items() if v["evidence_level"] == "failed")
    L += ["", "## Failed rows", "",
          "Each failure is of the evidence statement the row carries, as the basis states; it is not a failure of "
          "the claim unless the basis says so.", ""]
    for k in failed:
        v = claims[k]
        L.append(f"- **{k}** ({v['verdict']}, {v['proof_status']}): {v['basis']}")
    if not failed:
        L.append("None.")
    L += ["", "## Rows held at traced-only by an unmatched or failed load-bearing artifact link", "",
          "Each row below has a load-bearing kernel, computation or build link that no evidence item reached at "
          "certificate-checked or better.", "", "| Row | Verdict | Proof status | Link | Gap |", "|---|---|---|---|---|"]
    for k in sorted(claims):
        v = claims[k]
        if v["evidence_level"] != "traced-only" or v["proof_status"] in BY_STATUS:
            continue
        lb = v["links"] if v["load_bearing"] == "all its links" else [e for e in v["links"] if e["layer"] == "kernel"]
        for e in lb:
            if e["bearing"] and e["level"] == "traced-only":
                gap = "; ".join(e["gap"]) or "matched only at traced-only: " + ", ".join(e["items"])
                L.append(f"| {k} | {v['verdict']} | {v['proof_status']} | `{e['source'][:90]}` ({e['layer']}) | {gap} |")
    L += ["", "## Traced-only rows whose checked artifacts reach a higher level", "",
          "The row's level is traced-only because of its proof status or a paper step; the artifact level records what "
          "its kernel, computation or build links reach. For a refuted claim the artifact is counter-evidence.", "",
          "| Row | Verdict | Proof status | Held by | Artifact level | Role |", "|---|---|---|---|---|---|"]
    for k in sorted(claims):
        v = claims[k]
        if v["evidence_level"] == "traced-only" and v["artifact_level"] not in (None, "traced-only"):
            held = (v["basis"].split("traced-only (", 1)[-1].rstrip(")") if v["proof_status"] not in BY_STATUS
                    else v["basis"].split(":")[0])
            L.append(f"| {k} | {v['verdict']} | {v['proof_status']} | {held} | {v['artifact_level']} | "
                     f"{v['artifact_role']} |")
    L += ["", "## Chain-link corrections applied", "",
          "`matrix/chain-relabels.json`, applied by `matrix/scripts/merge_matrix.py` with the mapper's layer kept as "
          "`mapper_layer`:", ""]
    for i, fixes in relabels.items():
        if i.startswith("_"):
            continue
        for fx in fixes:
            L.append(f"- **{i}** link {fx['index']} (`{fx['source'][:80]}`): {fx['from']} → {fx['to']}; {fx['reason']}.")
    part = sorted(k for k, v in claims.items() if v["partial_items"])
    L += ["", "## Rows resting on partial items", "",
          "The item's limits apply to the row (see the part files). A formal-coverage item that does not cover a row "
          "is left out of that row's grading and appears above as a gap.", "",
          "| Row | Level | Partial items |", "|---|---|---|"]
    for k in part:
        L.append(f"| {k} | {claims[k]['evidence_level']} | {', '.join(claims[k]['partial_items'])} |")
    L += ["", "## Limits that apply across rows", "",
          "- No Lean toolchain is available here, so no kernel item is *reproduced*: *certificate-checked* is the "
          "highest level a kernel link can reach (E1).",
          "- The CI jobs examined replayed the OIBridge build from the Actions cache (E1-122, E3-11), and for 9 of the "
          "14 Appendix A modules no fresh elaboration was observed at these sources (E3-11). The axiom reports are "
          "lake replays of an elaboration of byte-identical sources; a fresh elaboration is proposed for owner "
          "authorization.",
          "- For the 21 printed declarations outside the retained result, \"exactly the three axioms\" is read from "
          "CI job-log text, which is diagnostic. The structured certificate there is the Release gate step's "
          "conclusion, which under `tools/lean_axiom_check.py`'s contract establishes that every printed report lies "
          "within the allow-list and that every declared `#print axioms` has a report. No row's level rests on the "
          "log text alone. The logs expire (E3-14).",
          "- The concept DOI and the release archive that the Introduction cites (L197–200) were not checked (E3-16).",
          "", "## Proposed for owner authorization (not dispatched)", "",
          "- A fresh-build CI reproduction of `introduction_repro` at `17b830bc`.",
          "- An extended expected result covering the additional modules (OD-15). It can be re-derived from the "
          "digest-checked log of job 121598983127 without a rebuild while that log is available; landing it in "
          "`papers/introduction_repro/` is a change on #918.",
          "- BHa and BHb `mutants.py` replays, and the BHb `-O` replay, in CI (E2). The BHb `checks.py` replay is "
          "done (E3-18).", ""]
    return "\n".join(L)


def main():
    ev = build()
    rows, items = load()
    relabels = json.loads((AUDIT / "matrix" / "chain-relabels.json").read_text(encoding="utf-8"))
    text_json = json.dumps(ev, indent=1, ensure_ascii=False) + "\n"
    text_md = render(ev, items, relabels)
    out_json, out_md = AUDIT / "evidence.json", AUDIT / "EVIDENCE.md"
    if "--check" in sys.argv[1:]:
        ok = out_json.exists() and out_json.read_text(encoding="utf-8") == text_json \
            and out_md.exists() and out_md.read_text(encoding="utf-8") == text_md
        print("evidence.json and EVIDENCE.md match" if ok else "evidence.json or EVIDENCE.md differs from the rendering")
        drift = [r["id"] for r in rows if (r.get("evidence_level"), r.get("evidence_basis"))
                 != (ev["claims"][r["id"]]["evidence_level"], ev["claims"][r["id"]]["basis"])]
        byid = {r["id"]: r for r in rows}
        unapplied = [f"{i}:{fx['index']}" for i, fixes in relabels.items() if not i.startswith("_") for fx in fixes
                     if (byid[i]["chain"][fx["index"]].get("layer"), byid[i]["chain"][fx["index"]].get("mapper_layer"),
                         byid[i]["chain"][fx["index"]].get("source")) != (fx["to"], fx["from"], fx["source"])]
        relabelled = sum(1 for r in rows for ln in r["chain"] if "mapper_layer" in ln)
        if unapplied or relabelled != sum(len(v) for k, v in relabels.items() if not k.startswith("_")):
            print("matrix.json chains disagree with matrix/chain-relabels.json:", ", ".join(unapplied) or
                  f"{relabelled} relabelled links")
            ok = False
        if drift:
            print("matrix.json evidence levels differ from evidence.json:", ", ".join(drift[:20]))
        sys.exit(0 if ok and not drift else 1)
    out_json.write_text(text_json, encoding="utf-8")
    out_md.write_text(text_md, encoding="utf-8")
    print(json.dumps(ev["counts"]))


if __name__ == "__main__":
    main()
