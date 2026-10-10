"""Second exploratory pass: block structure around the CompositeDimension output.

Usage: python3 -I explore2.py <raw.log>
"""
import sys

with open(sys.argv[1], "r", encoding="utf-8", newline="") as fh:
    lines = fh.read().split("\n")

hits = [i for i, l in enumerate(lines, 1) if "CompositeDimension" in l]
print("hit range:", hits[0], "..", hits[-1], "count", len(hits))
print("hits after L4898:", [i for i in hits if i > 4898])
for i in [i for i in hits if i > 4898]:
    print(f"  L{i}: {lines[i-1][:240]!r}")

print("\n--- L4714..L4835 ---")
for i in range(4714, 4836):
    print(f"L{i}: {lines[i-1][:240]!r}")

print("\n--- L4896..L4930 ---")
for i in range(4896, 4931):
    print(f"L{i}: {lines[i-1][:240]!r}")
