# Scientific confirmation: Introduction r9

- **Object:** `draft/Introduction-r9.md` at `33f1e75d`, sha256 `880ee98d…c552` (verified).
- **Diff:** `git -c gc.auto=0 -c maintenance.auto=false diff --no-index` from r8 to r9 changes 7 lines: 7 insertions,
  7 deletions. All of them are covered below.
- **Read-only.**

## Verdict: ACCEPT

| Change | Verdict |
|---|---|
| N1, §5: "…for factor dimensions $d_B,d_R$, up to the correction term of Theorem A.8 [Pag93; GR, Thms A.8–A.9]" | **The departure is accurate and better than my wording.** Theorem A.8 states $\overline{S(\rho_R)}=S_{\rm Page}+\mathcal O(\epsilon)$, where $\epsilon$ is a concentration tolerance. GR also uses $\epsilon$ for the discreteness scale $\epsilon=2\sqrt\sigma\,l_p$, and this paper never defines $\epsilon$. "The correction term of Theorem A.8" names the same quantity and points to where it is stated, so nothing is lost |
| N2, §5: "timescale ordering does not supply it [BHa, item F]" | Correct. Item F is the exact interval bound behind this clause, and it gives §6.2 item 4's three non-claims their referent back |
| N3, six comments changed from VERIFY to "Read first-hand … SUPPORTED" | Each comment's passages match FINDINGS (`fa50caae…6ea1`): BBS24 Def. 1, pp. 1–2; Cal26 abstract and §2, Thm 1, p. 4; EvEMU11 abstract, §2 and §6; KP14 abstract and p. 6; tH14 abstract and Ch. 2 §2.1 (it keeps "no priority is assigned"); Vol06 abstract and §5.2. CT06, Har04 and Sha79 keep their VERIFY markers, as FINDINGS requires, since those sources were unreachable |

No other change.
