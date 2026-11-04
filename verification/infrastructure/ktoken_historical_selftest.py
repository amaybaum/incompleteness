#!/usr/bin/env python3
"""Run frozen KTOKEN controls against their historical synthetic fixture.

The receipt seals controls.py. Subsequent OI research appends unrelated census
families, so a fixture adapter is needed for the self-test on newer heads.
Only in-memory fixture inputs change; the original source, production controls,
receipt, proof and historical evidence are not modified.
"""

import builtins
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[2]
CONTROLS = ROOT / "verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/controls.py"
WORKFLOW = ROOT / ".github/workflows/verify.yml"
REGISTRY = ROOT / "verification/lean-manuscript-census.json"
SEALED_BLOB = "7c9672a170210f8c2496787cb8cb3bc16cb30ba2"
OLD_STEP = "run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/controls.py --self-test"
NEW_STEP = "run: python3 -I -B verification/infrastructure/ktoken_historical_selftest.py"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    frozen_bytes = CONTROLS.read_bytes()
    blob = hashlib.sha1(b"blob %d\0" % len(frozen_bytes) + frozen_bytes).hexdigest()
    require(blob == SEALED_BLOB, "frozen KTOKEN controls blob has changed: " + blob)
    source = frozen_bytes.decode("utf-8")
    spec = importlib.util.spec_from_file_location("frozen_ktoken_controls", CONTROLS)
    require(spec is not None and spec.loader is not None, "cannot load frozen controls")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    workflow = WORKFLOW.read_text(encoding="utf-8")
    require(workflow.count(NEW_STEP) == 1 and workflow.count(OLD_STEP) == 0,
            "expected exactly one adapter step and no direct frozen KTOKEN self-test")
    historical_workflow = workflow.replace(NEW_STEP, OLD_STEP)
    census = json.loads(REGISTRY.read_text(encoding="utf-8"))
    positions = [i for i, family in enumerate(census["families"]) if family == module.FAMILY]
    require(len(positions) == 1, "historical KTOKEN census family not unique")
    # Reconstruct only the historical E snapshot for the synthetic tests.
    census["families"] = census["families"][:positions[0] + 1]
    historical_registry = json.dumps(census, indent=2, ensure_ascii=False) + "\n"

    original_fake_repo = module.fake_repo
    real_open = builtins.open

    def historical_fake_repo(root):
        def fixture_open(file, *args, **kwargs):
            path = Path(file).resolve()
            if path == WORKFLOW:
                return io.StringIO(historical_workflow)
            if path == REGISTRY:
                return io.StringIO(historical_registry)
            return real_open(file, *args, **kwargs)

        module.open = fixture_open
        try:
            return original_fake_repo(root)
        finally:
            del module.open

    module.fake_repo = historical_fake_repo
    result = module.main(["--self-test"])
    require(result == 0, "frozen KTOKEN self-test failed")

    # Extra regression guards, separate from the original 38 checks.
    base = json.dumps({"families": [{"name": "pre-KTOKEN"}]})
    clean = json.dumps({"families": [{"name": "pre-KTOKEN"}, module.FAMILY]})
    later = json.dumps({"families": [{"name": "pre-KTOKEN"}, module.FAMILY, {"name": "later"}]})
    require(module.registry_ok(base, clean) and not module.registry_ok(base, later),
            "production J incorrectly accepts an appended later family")
    synthetic = historical_fake_repo(str(ROOT))
    require(synthetic is not None, "cannot form historical KTOKEN synthetic fixture")
    tampered = {k: dict(v) for k, v in synthetic.items()}
    tampered["E"][module.CONTROLS] = "tampered sealed controls blob (synthetic)\n"
    log = "\n".join("'%s.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" %
                    (module.NS, name) for name in module.PRINTS)
    log += "\n" + module.EVAL_LOG + "\n" + module.A3_LOG + "\n"
    with tempfile.TemporaryDirectory() as tmp:
        log_path = Path(tmp) / "synthetic-bridge.log"
        log_path.write_text(log, encoding="utf-8")
        ok, output, calls = module.end_to_end(source, tampered, str(log_path))
    require(not ok and calls == 0 and "STATIC CONTROLS FAILED: C2" in output
            and not any(token in output for token in module.POSITIVE),
            "production C2 fails to reject a modified frozen controls blob")
    print("PASS KTOKEN frozen-source adapter: historical fixture, production J and C2 tamper")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print("FAIL KTOKEN frozen-source adapter:", exc)
        raise SystemExit(1)
