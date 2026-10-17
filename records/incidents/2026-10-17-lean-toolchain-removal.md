# Removal of the local Lean toolchain (owner-authorized, 2026-10-17)

- **What:** `/tmp/claude-0/-home-user-incompleteness/ce7104bc-8508-557b-9490-8c1ce0f7a1ca/scratchpad/agent-829/toolchain/`
  (about 3.1 GB).
- **Contents:** one directory, `lean-4.33.0-linux/`, holding `bin/`, `include/`, `lib/`, `share/`, `src/`, `LICENSE` and
  `LICENSES`. No `.git`, no repository file, no evidence, log or shared build artifact.
- **Origin:** the #829 dependency-review agent installed it on 2026-10-16 from the official `lean-4.33.0-linux.zip` of the
  leanprover/lean4 GitHub release, after `release.lean-lang.org` returned 403 through the proxy. Only the zip's digest
  prefix `b6802921…` was recorded; the zip itself was deleted after extraction. It was used only for the #829 toy-model
  controls (27 cases), never for evidence.
- **The binary, before removal:** `Lean (version 4.33.0, x86_64-unknown-linux-gnu, commit
  d8b18978322de05a8f3dba51ef03cf5461676c17, Release)`.

## Checks before removal

- No process had it as working directory or open file, and no command line referenced it.
- No symlink anywhere on the filesystem pointed into it.
- elan registered no toolchain (`~/.elan/toolchains/` empty).
- No running agent needed it. The #829 static review runs no Lean, the bridge experiment would run in CI, and #854's
  reproductions run on GitHub.

## Pins for reinstallation

- `verification/lean-mathlib/lean-toolchain` at `66a981d5`: `leanprover/lean4:v4.33.0`.
- `verification/lean-mathlib/lakefile.toml`: Mathlib `git = "https://github.com/leanprover-community/mathlib4.git"`,
  `rev = "v4.33.0"`. `lake-manifest.json` is gitignored.
- Install with elan: `elan toolchain install leanprover/lean4:v4.33.0`. In this environment that failed (403 from
  release.lean-lang.org). The GitHub release asset `lean-4.33.0-linux.zip` was reachable, but whether that counts as
  routing around a blocked host is the owner's call.
- Mathlib's cache hosts (`lakecache.blob.core.windows.net`, `mathlib4.lean-cache.cloud`) also returned 403, so a local
  Mathlib build was never possible here.

## Consequence

This session has no local Lean execution after removal. Network restrictions may prevent reinstalling it. Lean and
Mathlib work runs in CI.
