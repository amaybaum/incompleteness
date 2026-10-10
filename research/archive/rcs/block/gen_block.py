"""Generate RelcSelectBlock.lean from RelcSelectBlock.template.lean.

Each template line `-- @@COPY <landed name>` is replaced by the landed declaration body, renamed by
RENAME and with the EDITS applied. Nothing else in the template is touched.
"""
import sys
from rcs_common import LANDED, TEMPLATE, OUT, COPIES, EDITS, rename, extract_decls

landed = extract_decls(LANDED)
edits = {}
for name, old, new in EDITS:
    edits.setdefault(name, []).append((old, new))

copied = dict(COPIES)
out = []
seen = []
for ln in open(TEMPLATE, encoding="utf-8").read().split("\n"):
    if ln.startswith("-- @@COPY "):
        name = ln[len("-- @@COPY "):].strip()
        if name not in copied:
            sys.exit(f"template asks for {name}, which is not in COPIES")
        _, body = landed[name]
        body = [rename(b) for b in body]
        for old, new in edits.get(name, []):
            hits = [k for k, b in enumerate(body) if b == old]
            if len(hits) != 1:
                sys.exit(f"edit for {name}: expected exactly one line {old!r}, found {len(hits)}")
            body[hits[0]] = new
        out.extend(body)
        seen.append(name)
    else:
        out.append(ln)
missing = [n for n, _ in COPIES if n not in seen]
if missing:
    sys.exit(f"template lacks copies of {missing}")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(f"wrote {OUT}: {len(seen)} copied declarations")
