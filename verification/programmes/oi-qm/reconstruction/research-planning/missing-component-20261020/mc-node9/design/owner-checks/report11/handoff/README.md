# Native-wave bounded resource handoff v1

Read `REPORT.md` for the construction, proof, assumptions, countercontrols and
limits. This is research for independent review, not an OI-QM equivalence claim.

## Files

- `REPORT.md`: mathematical report and pinned manuscript anchors.
- `native_wave_checks.py`: standalone exact checker, Python 3.9+, standard library only.
- `native_wave_checks.out`: deterministic expected output.
- `SHA256SUMS`: SHA-256 checksums for the preceding files and this README.

The checker makes no file writes or network calls. It does not require a clone,
mpmath, SymPy or Lean. It raises on failure even under `python -O`.

## Replay

From the extracted directory, on a system with Python 3.9+:

```sh
sha256sum -c SHA256SUMS
python3 native_wave_checks.py > replay.out
cmp native_wave_checks.out replay.out
```

On systems without `sha256sum`, verify the manifest with the standard library:

```sh
python3 - <<'PY'
import hashlib
from pathlib import Path
for line in Path('SHA256SUMS').read_text().splitlines():
    wanted, name = line.split('  ', 1)
    actual = hashlib.sha256(Path(name).read_bytes()).hexdigest()
    if actual != wanted:
        raise SystemExit('HASH MISMATCH: ' + name)
    print(name + ': OK')
PY
```

`cmp` should produce no output and exit with status 0. The final checker lines
must report PASS and the explicit NOT CLAIMED scope. A successful replay
reproduces this finite evidence; it does not replace review of the general
proof or of its physical assumptions.

The package was executed twice, with the second run in a separate temporary
directory; stdout matched byte for byte. There are no timing lines or random
seeds. The zip has fixed entry timestamps for reproducible packaging, not for
dating the research. The manifest excludes itself and the enclosing archive
to avoid self-referential hashes.

No repository files, commits, PR comments or CI runs were changed or created
to produce this handoff. Publishing it to #885 is a separate action by the
receiving researcher/owner.
