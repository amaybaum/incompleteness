## Confirmation of PR #918 r18 at `0ce9cda9`: CONFIRM

All seven of my findings are fixed correctly against their sources. Nothing new is overstated or weakened. One optional item remains: ε_min is still not defined in the paper.

I compared r18 with `a79add6a` word by word (one commit, `0ce9cda9`). The worktree I used, `rev918r18-sci`, is removed, and I edited, pushed or commented nothing. The line numbers below are r18's. The added `fontsize: 11pt` line shifts each by one from the numbers in your message: the persistence sentence is L98, the Corollary L110, the summary sentence L115 and the H-decouple clause L219.

### 1. Findings 1–4: fixed
- **Abstract, L17.** It now reads "places the zero-point sum and the effective cosmological constant at different levels of description". That is the established distinction (GR §6.2), with no claim of decoupling.
- **(C2) persistence sentence, L98.** This matches the physical-memory theorem (Main :463, "Theorem (physical memory: C2, process form)").
  - The coupling-step model is defined: the next visible state is a function of the current visible and hidden states, and π_H is the reference hidden law.
  - The bound now uses M_k at order k, with ε_min(M_k,|𝒞_V|) at that coupling time, measured from π_H.
  - "No mixing hypothesis" is correctly given as the persistence form. The slow-bath form is stated as a lower bound on the mixing time, which is also consistent with #958.
  - The new (C4) gloss, "an order short compared with the recurrence time", matches Main §2.3 Scope (kτ_S ≪ t_R).
- **Summary sentence, L115.** It now says "needs only finite reversibility and one non-deterministic visible step, and holds also for laws that are Markov on every accessible window". This matches Main :141.
- **H-decouple, L219.** It now says "is not established". Thm A.7 gives a pure V–B state only for t ≪ τ_B^D ~ 1/H (GR App. A.5, A.7), and "does not establish that V∖R is unentangled with B∪R", which is GR A.7's own statement.

### 2. Findings 5–7 and editorial M5: fixed
- **Finding 5 (§6).** Recurrence-cycle indivisibility is now listed under "Proved on paper", with Theorem 3 as the machine-checked core. The shared-column fact and Γ_L=I are named as elementary steps.
- **Finding 6 (§5).** The reading schedule is now scoped to the first count. The 32-map case now states the two-bit message in both registers with one register read, which matches `checks.py` AM2.
- **Finding 7.** "Drawn independently of it" is now at L101 and L103.
- **M5.** The Corollary at L110 reads "of equal length". This matches Main :137, where both histories run from x₀ to x_k.

### 3. My earlier confirmations still hold
- **Recurrence scope.** The abstract, L101/L103/L110/L112 and §6 state the same scope: the shared prior drawn independently of the root; the rooted family including zero-probability roots; some rooted matrix that is not a permutation; and the full-support equivalence, with both directions at L112. The abstract's "initial visible state (root)" defines the term in place and changes no scope. It is still consistent with Medicine :25 at `652afa09`.
- **Support for the strengthened claims.** This still holds. The Bell–lattice rewrite matches Main §3.3's Corollary: "outside each other's causal cone"; a Bell preparation adds "bounded-degree long-range edges", where Main says "bounded-degree long edges or an equivalent nonlocal response map". The new `[SM]` entry matches the title of `papers/SM.md`.
- **Scope discipline.** This still holds. The dimensional identity moved to §4's opening, now cited to [GR §6.3] with the "Hubble-scale density" qualifier GR states. The Attribution rewording is editorial only.

### 4. Coverage
- The §2.4 Corollary is byte-identical (`b596be8a…`).
- T-3 has a new fingerprint, `67e2d2a4f01999ed`, after "drawn independently of it" was added. The recurrence Corollary has a new fingerprint, `603c7f6d12b01679`, after "of equal length" was added. Both remain MIRROR rows with no other changes.
- `coverage_check` at `0ce9cda9` reports OK, with 134 canonical statements.

### 5. Nothing new is overstated or weakened
- Theorem 3's added clause "drawn independently of it" is harmless: the kernel's `RootedRealization` proves the result without it.
- **Optional:** ε_min(·,|𝒞_V|) is still not defined. It could be given as the inverse of 2[ε log(|𝒞_V|−1)+h(ε)], as in Main :463.

### Answers to the owner's two questions
- **(a) Is every substantive claim supported by its stated evidence and assumptions?** Yes.
- **(b) Does the paper communicate the strongest established results without unnecessary weakening?** Yes.
