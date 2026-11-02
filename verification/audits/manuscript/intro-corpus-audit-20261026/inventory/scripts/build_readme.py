import json, sys, collections
CLAIMS, OUT = sys.argv[1], sys.argv[2]
c = json.load(open(CLAIMS, encoding="utf-8"))
sec = collections.OrderedDict()
for r in c:
    sec.setdefault(r["section"], collections.Counter())[r["type"]] += 1
TYPES = ["theorem-statement", "result", "negative", "status", "scope", "numerical", "attribution", "definition-used"]
LEVELS = ["proved-kernel", "proved-paper", "conditional", "calibration", "numerical", "conjecture", "open", "unstated"]
tot_t = collections.Counter(r["type"] for r in c)
tot_l = collections.Counter(r["status_as_stated"]["level"] for r in c)
first = {}
for r in c:
    first.setdefault(r["section"], r["id"])
last = {}
for r in c:
    last[r["section"]] = r["id"]

rows = ["| Section | IDs | Total | " + " | ".join(TYPES) + " |", "|---|---|--:|" + "--:|" * len(TYPES)]
for s, cnt in sec.items():
    rows.append(f"| {s} | {first[s]}–{last[s]} | {sum(cnt.values())} | " + " | ".join(str(cnt.get(t, 0)) for t in TYPES) + " |")
rows.append(f"| **Total** | | **{len(c)}** | " + " | ".join(f"**{tot_t[t]}**" for t in TYPES) + " |")
lvl = ["| Level | Entries |", "|---|--:|"] + [f"| {l} | {tot_l.get(l, 0)} |" for l in LEVELS]
dirs = [f"- {r['id']} (line {r['line']}): {r['direction']['kind']}; sub-claims "
        + ", ".join(s['id'] for s in r['direction']['sub_claims']) for r in c if r["direction"]]
att = [f"- **{r['id']}** (line {r['line']}): {r['attention']}" for r in c if "attention" in r]

md = open(sys.argv[3], encoding="utf-8").read()
md = (md.replace("{{TOTAL}}", str(len(c)))
        .replace("{{SUBS}}", str(sum(len(r['direction']['sub_claims']) for r in c if r['direction'])))
        .replace("{{SECTION_TABLE}}", "\n".join(rows))
        .replace("{{LEVEL_TABLE}}", "\n".join(lvl))
        .replace("{{DIRECTIONS}}", "\n".join(dirs))
        .replace("{{ATTENTION}}", "\n".join(att))
        .replace("{{NATT}}", str(len(att))))
assert "{{" not in md
open(OUT, "w", encoding="utf-8").write(md)
