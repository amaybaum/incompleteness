"""I3 record tally for RESULT.md §0 (counts by kind, status and level; bearing classes; flags).

DECISION RULE (fixed before the first run):
- A record is a block starting at a line `### I3.<n> ...` of INVENTORY.md and ending before the next such line or a
  `## ` heading. Its fields are read from the text of the block (lines joined with spaces):
  kind = the words after "kind:" up to the first " · " or "(";
  level = the token after "level:" up to " · ";
  status = the text after "status:" up to " - statement" (first 160 characters kept);
  bearing = the text after "bearing:" up to " · flag" or the end of the block;
  flag = the text after "flag:" up to the end of the block.
- Status class (first matching rule, in this order): "not at L" → D (design, not at L); "PT-record" → PT; "refuted" →
  refuted; "conditional" → conditional; "assumed" → assumed; "open" → open; "proved [K]" → proved [K]; else UNCLASSIFIED.
- Level class: the first of H, O, P, M, G, X appearing as a whole word at the start of the level text; "—" → none;
  composite forms such as "O/P", "O→P" are reported as written.
- Bearing class (first matching rule): starts with "none at L" → none at L; starts with "direct" → direct; contains
  "single-token structure the pair inherits" → single-token inherited; contains "only through" → through bridge;
  starts with "constrains the single-token structure" → single-token (not inherited); "as I3." → see referenced record;
  else UNCLASSIFIED. The output lists every record with its classes, then the tallies, then every record whose flag
  contains "do not assume".
- Deterministic output, no timestamps.
"""
import re
import sys


def field(text, name, stops):
    k = text.find(name + ":")
    if k == -1:
        return ""
    rest = text[k + len(name) + 1:]
    cut = len(rest)
    for s in stops:
        j = rest.find(s)
        if j != -1:
            cut = min(cut, j)
    return rest[:cut].strip()


def main():
    with open("INVENTORY.md", encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    recs, cur = [], None
    for l in lines:
        m = re.match(r"^### (I3\.\d+) (.*)$", l)
        if m:
            if cur:
                recs.append(cur)
            cur = [m.group(1), m.group(2), []]
            continue
        if l.startswith("## ") and cur:
            recs.append(cur)
            cur = None
            continue
        if cur:
            cur[2].append(l.strip())
    if cur:
        recs.append(cur)
    rows = []
    for rid, title, body in recs:
        t = " ".join(body)
        kind = field(t, "kind", [" · ", " ("]).strip()
        level = field(t, "level", [" · "])
        status = field(t, "status", ["- statement"])[:160]
        bearing = field(t, "bearing", [" · flag", "- flag"])
        flag = field(t, "flag", ["\u0000"])
        st = ("D" if "not at L" in status else "PT" if "PT-record" in status else "refuted" if "refuted" in status
              else "conditional" if status.startswith("conditional") or " conditional" in status[:30] else
              "assumed" if "assumed" in status[:40] else "open" if "open" in status[:40] else
              "proved [K]" if "proved [K]" in status else "UNCLASSIFIED")
        lv = level.split(" ")[0] if level else ""
        if bearing.startswith("none at L"):
            bc = "none at L"
        elif bearing.startswith("direct"):
            bc = "direct"
        elif "single-token structure the pair inherits" in bearing:
            bc = "single-token inherited"
        elif "only through" in bearing:
            bc = "through bridge"
        elif bearing.startswith("constrains the single-token structure"):
            bc = "single-token (not inherited)"
        elif bearing.startswith("as I3."):
            bc = "see " + bearing.split()[1]
        else:
            bc = "UNCLASSIFIED"
        rows.append((rid, title, kind, lv, st, bc, flag))
    for r in rows:
        print(f"{r[0]} | {r[1][:70]} | kind={r[2]} | level={r[3]} | status={r[4]} | bearing={r[5]}")
    print()
    for name, idx in (("kind", 2), ("level", 3), ("status", 4), ("bearing", 5)):
        tally = {}
        for r in rows:
            tally[r[idx]] = tally.get(r[idx], 0) + 1
        print(f"## by {name}: " + "; ".join(f"{k} = {v}" for k, v in sorted(tally.items())))
    print(f"## records: {len(rows)}")
    print()
    print("## flag 'do not assume':")
    for r in rows:
        if "do not assume" in r[6]:
            print(f"{r[0]} | {r[1][:90]}")
    print("END")


if __name__ == "__main__":
    sys.exit(main())
