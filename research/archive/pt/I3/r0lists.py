"""I3 RESULT §0 lists, generated from rcount.out (run 3, the final tally).

DECISION RULE (fixed before the first run):
- Read the per-record lines of rcount.out (lines starting with "I3.") and their fields id | title | kind | level |
  status | bearing.
- Print, for each bearing class other than "none at L" (in the order: direct, single-token inherited, single-token (not
  inherited), through bridge), the class name, its count, and its records as "id title" joined by "; ", the title cut
  at 64 characters. Then print the ids of the "none at L" class only. Then copy the do-not-assume list of rcount.out.
- No other processing; deterministic output, no timestamps.
"""
import sys


def main():
    with open("rcount.out", encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    rows = []
    for l in lines:
        if l.startswith("I3.") and l.count(" | ") >= 5:
            parts = l.split(" | ")
            rows.append((parts[0], parts[1], parts[5].replace("bearing=", "")))
    order = ["direct", "single-token inherited", "single-token (not inherited)", "through bridge"]
    for cls in order:
        sel = [r for r in rows if r[2] == cls]
        print(f"**{cls}** ({len(sel)}): " + "; ".join(f"{r[0]} {r[1][:64]}" for r in sel))
        print()
    none = [r[0] for r in rows if r[2] == "none at L"]
    print(f"**none at L** ({len(none)}): " + ", ".join(none))
    print()
    k = lines.index("## flag 'do not assume':")
    dna = [l for l in lines[k + 1:] if l.startswith("I3.")]
    print(f"**do not assume** ({len(dna)}): " + "; ".join(x.replace(" | ", " ") for x in dna))
    return 0


if __name__ == "__main__":
    sys.exit(main())
