# SUBSTATE-1 / Yang–Mills / F2: one sourced link–pointer *toy*, not native OI

**Research-only, constructive control.** This is an explicit addition to the microscopic model, not an implementation of the OI cubic wave update, not SU(2)/SU(3), not a gauge-action derivation, not quantum equivalence. It is included to determine **exactly what a shared interaction and record mechanism could establish**, and what it still fails to establish. It follows #1007, #1009 and #1003.

## Defined ontology and finite exact instance

Consider an oriented square with vertices \(0,1,2,3\) and links \(0\to1\to2\to3\to0\). A link is a \(U(1)\) phase. The finite exact test uses the \(8\)-th roots of unity, encoded by \(u_e\in\mathbb Z/8\). The state includes **one apparatus pointer bit** \(b\in\mathbb Z/2\). There are \(8^4\cdot2=8192\) total states. The oriented plaquette holonomy is \(k=\sum_e u_e\bmod8\).

A local gauge transformation with vertex angles \(g_v\in\mathbb Z/8\) sends
\[
u_{v\to w}\mapsto u_{v\to w}+g_v-g_w\pmod8.
\]
It leaves \(k\) invariant. The pointer is gauge-neutral.

Two **specified** settings \(s\in\{0,2\}\) use gauge-invariant readout predicates
\[
h_s(k)={\bf1}_{(k-s)\bmod8<4}.
\]
Define the reversible *read-and-kick* update \(T_s=K\circ R_s\):
\[
R_s:(u,b)\mapsto(u,b'),\qquad b'=b\oplus h_s(k);
\]
\[
K:(u,b')\mapsto(u'_0,u_1,u_2,u_3,b'),\quad u'_0=u_0+4b'\pmod8.
\]
The pointer is a physical state coordinate; its update is not an after-the-fact decoder. \(K\) changes an oriented link by the central group element \(-1\) iff the **updated** pointer is one. The inverse is explicit: undo \(K\) with the *present* pointer, then undo the bit flip using the recovered input plaquette. \(R_s\) is an involution, and \(K\) is a bijection. Hence every \(T_s\) is a bijection.

**Gauge covariance:** \(h_s(k)\) is gauge invariant and the central link multiplication commutes with the local gauge action. Consequently \(T_s\circ G_g=G_g\circ T_s\) for any \(g\). The pointer histories and initial/output loops are also gauge invariant.

**Measure:** uniform counting measure on **all 8192 states** is preserved by each \(T_s\), since it is a permutation. For the experimentally prepared source, take *uniform link variables and a fresh pointer \(b=0\)*. That **conditioned preparation is not stationary** under \(T_s\): it is an explicit preparation resource, not a free part of invariant Haar. A gauge-invariant measurement may change the outgoing link distribution through back-action without violating conservation of the full-state uniform measure. A full experiment must retain pointer preparation, reset cost and reused-pointer history.

## A real coupling and what the exact model shows

On one incident source \(b=0\), the public pointer after the interaction is \(b'=h_s(k)\). Both settings yield pointer-one probability \(1/2\), yet their **unconditional outgoing** loop distributions differ.

- For \(s=0\), the outgoing loop is uniformly supported on \(k'\in\{4,5,6,7\}\): each output appears with probability \(1/4\).
- For \(s=2\), the outgoing loop is uniformly supported on \(k'\in\{0,1,6,7\}\), again each with probability \(1/4\).

The *original incident* loop is uniform on all eight values in either context. Here the outgoing difference is not just accepted-only conditioning: the map contains a physical, reversible, setting-dependent **link kick**. Removing the kick leaves the loop unchanged for every input and setting.

The settings are genuinely distinct reversible **classical** operations. For \(u=(0,0,0,0),b=0\), applying \(s=0\) then \(s=2\) gives \((4,0,0,0),b=0\), while applying \(s=2\) then \(s=0\) gives \((4,0,0,0),b=1\). The two operations **do not commute** as microscopic permutations. Without the kick they are just commuting conditional bit flips.

**Critical negative control:** noncommuting classical reversible operations still do not supply noncommuting *quantum* gates, complex phase interference, complete positivity, a purification resource or the five finite operational completion conditions in \`OIBridge.GeneralCarrier\`. This toy has a perfectly classical joint hidden state and public record. It is **not** a double-slit derivation or a demonstration of coherent quantum measurement.

## Continuous carrier analogue and limits

Replace each \(u_e\in\mathbb Z/8\) by a genuine \(U(1)\) link angle \(\theta_e\in\mathbb R/2\pi\mathbb Z\), and set \(h_s\) to the indicator of a half-circle for the plaquette phase, with the two settings separated by a quarter turn. Keep the pointer bit and the central kick \(\theta_0\mapsto\theta_0+\pi b'\). These maps are Borel measurable, invertible (undo kick, then bit flip), gauge covariant, and preserve **product Haar times uniform pointer** (fiberwise flip and pointer-conditioned Haar translation). They are generally discontinuous as functions of the angle because of the threshold—**continuous carrier** does not mean **continuous-time or smooth interaction**. This is another imposed interaction, not OI-derived.

The exact 8-grid results are checks for one finite subgroup; they do not by themselves establish any observer-level continuum limit, Yang–Mills action or QFT.

## Machine-checkable finite controls

The companion \`gauge_pointer_toy_probe.py\` uses integer arithmetic and exhaustive finite loops to check **8,192 states and 30 positive/countercontrols**:

- Two-way inverses for both settings, and no-kick controls.
- Gauge covariance for all states under each of the four unit vertex-gauge generators (which generate the finite gauge group); explicit loop invariance.
- Both full-source pointer laws and complete joint counts of input loop, output loop and pointer; unconditioned initial Haar on the eight loop values.
- Nontrivial link back-action with the kick, no back-action without it.
- Source-preparation distinction: uniformly counting **all** states keeps the outgoing plaquette loop uniform; initializing the pointer to zero does not.
- Noncommuting settings with kick, commuting settings without kick.

The executed exact probe reports \`PASS_EXACT_GRID_TOY_NOT_NATIVE_OI\` with all 30 controls passing and 8,192 states checked. Normal and Python \`-O\` execution are byte-identical. These are local exact-check results, **not** a Lean theorem or a native OI test.

## Native sourcing test: where OI currently stops

The actual finite cubic OI wave rule in \`papers/oi_lattice_code/trace_out_fractional/wave_eqn.c\` evolves site values over two time slices by a neighbor sum minus the previous value, modulo \(q\). The retained native-Y packages implement further constrained binary/triple interactions, but **none in the inspected source supplies this added \(U(1)\) link carrier, the local gauge action above, a gauge-invariant plaquette-triggered pointer flip, or its central link kick as a native operator**. In particular, \`native-y-continuation-20261024/EQUIVALENCE-OBLIGATIONS.md\` keeps physical access and reusable instrument operations open. This is an evidence-bounded sourcing gap, not a theorem that no future OI extension can implement the update.

A **native bridge** must now give an actual map or encoding from the OI microscopic state into oriented links, a physical evolution preserving the gauge-equivalence relation, a *permitted* setting/measurement apparatus (not simply a decoded private cell), and a full record/carrier reuse law. One must verify these on the same native update and prior before reusing this toy's successful gauge and pointer tests. The new \(U(1)\) link/pointer degree of freedom is an **additional physical premise unless sourced independently**.

## Decision

**ACCEPT** this bounded proof of concept at its explicitly *added toy-model* scope: gauge covariance, deterministic reversible back-action and observation settings are jointly mathematically possible. **FAIL** the hypothesis that those properties (even with noncommuting classical settings) yield quantum operational equivalence or select the Wilson/Yang–Mills action. **BLOCKED** on a physical OI source/encoding and permitted, reusable readout.

Before any claim upgrade, obtain independent mathematical review, then source the link and apparatus directly from the OI microscopic dynamics. An independent prediction must distinguish more than a manually chosen \(h_s\) or kick rule. Keep #1009 draft, no manuscript change, no merge, no workflow dispatch or F/E designation.
