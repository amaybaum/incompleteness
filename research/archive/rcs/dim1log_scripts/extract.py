"""Decode the saved get_job_logs response and write logs_content verbatim to raw.log.

Usage: python3 -I extract.py <raw_tool_response.json> <raw.log>
"""
import hashlib
import json
import sys

src, dst = sys.argv[1], sys.argv[2]

with open(src, "rb") as fh:
    raw_bytes = fh.read()

obj = json.loads(raw_bytes.decode("utf-8"))
print("top-level type:", type(obj).__name__)
print("keys:", list(obj.keys()))
for k, v in obj.items():
    if k == "logs_content":
        print(f"  {k}: str, {len(v)} chars")
    else:
        print(f"  {k}: {type(v).__name__} = {v!r}")

text = obj["logs_content"]
with open(dst, "w", encoding="utf-8", newline="") as fh:
    fh.write(text)

# Round-trip check: the file must decode to exactly the received string.
with open(dst, "rb") as fh:
    back = fh.read()
assert back.decode("utf-8") == text, "round-trip mismatch"
print("raw.log bytes:", len(back), "sha256:", hashlib.sha256(back).hexdigest())
print("raw_tool_response bytes:", len(raw_bytes), "decoded chars:", len(raw_bytes.decode("utf-8")))
print("round-trip: OK")
