# Draft annotation for #914, O-RET edge (OQ-6)

**Status.** WIP / UNVERIFIED. This is draft text. It is to be posted to #914 only after an independent review of the exact
checkpoint that carries it. It is not posted and not adopted. Authority: the owner's decision on OQ-6, recorded at #1032 c.6611966162:

> "record the reviewed constraint against O-RET, citing the exact checkpoint and its unmerged status. Preserve its
> hypotheses: finite state space, time-homogeneous bijection, time-independent retained function, exact holding and
> the distinction between new transfer and pre-existing carrier information. Describe the necessary resource as a
> support restriction excluding overwrites; "quiet" need not mean a low-energy or spatially quiet region. Keep
> approximate retention and changing readouts outside that conclusion. This supports a scoped annotation, not an
> unconditional replacement of the dependency edge."

***

**Text to post (draft):**

**Scoped annotation to the O-RET L-edge "O-ACC or O-RDY" (master matrix r2, #914 c.6563412926).** It annotates the edge
and does not replace it.

- **Source.** PR #1078 at the reviewed checkpoint `b9000ae2410a554ef54616bcfe85d5707f4a307f`. The PR is **unmerged**.
  - The relevant file is `verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/ROUTES.md`: Lemma S′ and
    Lemma Q in §0.3, and the Comparison.
  - The checkpoint was accepted by the owner as the reviewed paper assessment (#1032 c.6611966162).
- **Status.** These are paper results with independent review. They are not kernel-checked and not on `main`.

**Hypotheses, all required.**

1. A finite state space `S`.
2. One bijection `φ : S → S`, applied at every tick (time-homogeneous).
3. A retained function `a = g∘ρ`, where the readout `ρ` and the decoder `g` are the same at every tick. The region may
   be fixed or selected by the state.
4. **Exact** holding over the hold tick: `a(s_{t₀+2}) = a(s_{t₀+1})` almost surely under the declared law `μ`.
5. The distinction between **new transfer** at the write tick `t₀ → t₀+1` and carrier information that `a` already
   carried at `t₀`.

**Constraint (one direction only).**

- *Lemma S′.* If `φ(supp μ) = supp μ`, then exact holding implies `a(s_{t₀+1}) = a(s_{t₀})` almost surely, so the write
  tick transfers nothing. This covers every φ-invariant law and every full-support law.
  - Any carrier dependence of `a` is then pre-existing information, not new transfer.
  - If moreover `a(s_{t₀})` is independent of the carrier, the retained function is blind to it.
- *Lemma Q.* If a set `K` of record values is held from every state with `a ∈ K`, then no state with `a ∉ K` enters `K`.
  So a record that is written and then held exactly requires the law's support to **exclude the configurations that
  would overwrite it** at the hold tick.
- *Together.* Under hypotheses 1–5, exact one-step retention of newly transferred carrier information requires a law
  whose support is not φ-invariant and that excludes the overwriting configurations.
  - It is a preparation resource, the kind the O-RDY branch of the edge supplies. Whether O-RDY's readiness provides
    this particular restriction is not shown.
  - O-ACC, being a convention (CONVENTION-H-2s, D-07(a)), does not discharge it.
  - The resource is necessary, not sufficient.
  - "Quiet" names only this support restriction. It need not be a low-energy or spatially quiet region.

**Outside this conclusion.**

- Approximate retention. In a toy model outside copy form, carrier information is retained approximately under the counting
  measure with no support restriction (worst-case error 1/4 at the hold tick, HC-F0 in the same file); whether this
  meets a tolerance is undecided while `ε*` is unset.
- Readouts or decoders that change with the tick.
- Laws or rules outside hypotheses 1–2.
- Any claim of a no-go for observer-level extensions.

The edge "O-ACC or O-RDY" stands as recorded. This annotation adds the scoped necessary condition above for the exact,
fixed-decoder case.
