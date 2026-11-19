# Objects: #1230/#1232 reconciliation records

All four files are working copies written and reviewed on 2026-11-13 before this commit. Where a file contained the session-storage directory name that the SC-42 added-text scan bars, that word is replaced by "working-area" on the listed lines only; restoring the original word reproduces the reviewed bytes exactly (reviewed sha256 in the second column).

| File | Reviewed sha256 | Reviewed blob | Committed sha256 | Substituted lines |
|---|---|---|---|---|
| `RECONCILE-r1.md` | `05ad46b2977055069678f7a911d87bcd59f85408e10786ebcdd57d86cf91a71f` | `c03fe146` | `82fa6ed1e57b559e48d848321266dfdab9364370eeae551d5c6e9935fb8d09a1` | 5 |
| `REVIEW-r1.md` | `4785ec424f30ccd9c24b2ed16c170b167d063ed448770b0be1b86173729e0b69` | `7cd190ce` | `4fbcf865ebe4491455b96d40eccdbbb2631d547f8de237a0354adebf2d413373` | 199, 273, 274 |
| `RECONCILE-r2.md` | `bf9c2acc778a8eaf4212bcf8e8f7306a51c92fb578dcbfb81a05f83bcc60c470` | `1753a236` | `bf9c2acc778a8eaf4212bcf8e8f7306a51c92fb578dcbfb81a05f83bcc60c470` | none |
| `RESPONSE-r1.md` | `6818a0a8211fe37e99d85984a730c6d489fbe695d42235fb222180cfacf89616` | `67bb83d4` | `6818a0a8211fe37e99d85984a730c6d489fbe695d42235fb222180cfacf89616` | none |

## Added with r3

| File | Reviewed sha256 | Committed sha256 | Substituted lines |
|---|---|---|---|
| `CONFIRM-r2.md` | `d324a0c8eaa6b9e0d4b60302fa2e7120d3d78f7ba109b3bc2535a041a5c57473` | `bf6a382813f4167b22cac6520fb8c2be3c893476c47180a5d12ccb2cf400277b` | 22, 64 |
| `RECONCILE-r3.md` | — | `1b68c7c5eecd2c5affd7b2935de89231bc8bc3e64ce388c2d1e32f0b638fd839` | none |

`RECONCILE-r3.md` is `RECONCILE-r2.md` with the two replacements required by the focused confirmation of r2 (`CONFIRM-r2.md`); nothing else changed.
