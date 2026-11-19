# Second-use decision for the fixed binary SM ring

**SOURCE GAP. Physical measurement sourcing is NOT PASSED.** The first missing operation is a native producer of the joint ready precursor and selectable recorded request. There is a second, independent constraint on this apparatus design. At the exact ready signature for a common second request, the first result cannot be read from the same four coordinates alone. The design needs a physically readable record that survives re-arming, or a ready interface that leaves room for the first record. This decision concerns the stated ring and observation interface.

**Accountable unit.** #1377, under #866 and #1169, with retention obligations under #1032. Codex B wrote this paper-only assessment for a separate ChatGPT review. The [protocol](PROTOCOL.md) was published at `133dc1ff926e908688ce402e0c47fb8df5aefe4e` in draft #1378. All inherited scientific sources below are pinned to `192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7`.

## Follow the existing interaction

Use the existing binary ring of length $L\ge9$, with
$$
 f_i(u)=u_{i-1}\oplus(u_{i+1}\lor u_{i+2}),\qquad F(u,v)=(f(u)\oplus v,u).
$$
The observer projects the two slices at sites 0 and 1 to $O_t=(R_t,C_t)$. This is the state-dependent example already in SM. Its physical selection is open. The first request is $c_1$, the input bit is $z$, and $\xi$ denotes the other free fields in the supplied initial law. [Ring and observation cut](../native-apparatus-source-20261113/ASSESSMENT.md#L20-L51)

| Step | Evidence under the fixed rule | Physical link |
| --- | --- | --- |
| **Ready**, ticks −1 to 0 | A supplied precursor with $O_{-1}=b_{c_1}=((0,0),(0,c_1))$ and the common hidden law $\eta$ loads the target $I_{c_1}(z,\xi)$ with $O_0=a_{c_1}=((0,0),(c_1,0))$. | **First source gap.** The precursor specifies a request label, three hidden zero pins and five correlations. No executing producer of that joint input and no independently sourced preparation history for it appear in the selected path's evidence. |
| **Write**, tick 1 | Site 0 writes $c_1\lor z$ in its current field. Site 1 has current field $z$. With $c_1=0$ the receiver value distinguishes $z$. With $c_1=1$ the receiver is constant and the controller still distinguishes $z$ in the full projection. | Conditional field transfer. Actual selection and actuation of the request require the missing precursor process. |
| **Retain**, tick 2 | The previous fields at sites 0 and 1 carry $c_1\lor z$ and $z$, respectively. The full outgoing state is $W_2=F^2(I_{c_1}(z,\xi))$. | One tick of native field carry conditional on the prepared input. Persistent accessible storage while re-arming is open. |
| **Read** | The declared projection exposes the controller's $z$ at tick 1 and its later copy at tick 2. | An executing native read, a physically timed opportunity and a retained log for successful and unsuccessful attempts remain unsourced. |

[Preparation contract](../oi-qm-ext-1/preparation-loading.md#L120-L172) · [Inherited complete projection](../oi-qm-ext-1/preparation-loading.md#L239-L288) · [Accepted original source stop](../native-interaction-source-2-20261110/STATUS.md#L23-L41)

The physical path stops at **Ready**. The rest of this record tests the proposed interface even with the inherited prepared input granted as a control. It follows the published field history and uses a direct comparison with the existing ready conditions. The comparison considers the whole observer cut, including the controller.

## What is available at a second opportunity?

**Immediate reuse at tick 2.** The landed trajectory gives $R_2=((1\oplus c_1)z,c_1\lor z)$ and $C_2=(c_1,z)$. Compare it with the same precursor signature $b_{c_2}$ or the same loaded signature $a_{c_2}$ for a fixed second request $c_2$.

| First request $c_1$ | First bit $z$ | $R_2$ | $C_2$ | Exact second ready *projection* at tick 2 |
| --- | --- | --- | --- | --- |
| 0 | 0 | (0,0) | (0,0) | Matches both signatures for $c_2=0$ only. Full input and producer unverified. |
| 0 | 1 | (1,1) | (0,1) | Receiver fails either ready signature. |
| 1 | 0 | (0,1) | (1,0) | Receiver fails either ready signature. |
| 1 | 1 | (0,1) | (1,1) | Receiver fails either ready signature. |

[Inherited row](../oi-qm-ext-1/preparation-loading.md#L244-L257) · [Known outgoing-state limits](../oi-qm-ext-1/preparation-loading.md#L346-L363)

The first row is a necessary visible match only. The full ring state in that row may fail the hidden precursor or loaded-target conditions. Following only this row would discard the other first outcomes and would make a constant first-outcome decoder look successful. No automatic reload of the full target, second-work budget or native selection of $c_2$ follows from these rows.

**A later exact re-arm.** At a common declared second readiness time, fix $c_2$ and compare two admitted first histories at the same stage of the second attempt with different first results. At that stage, either the precursor signature $b_{c_2}$ or the loaded signature $a_{c_2}$ fixes all four coordinates of $O$ equally in the two histories. Any fixed read function of just those coordinates and the common request and clock data has the same input in both histories. It therefore cannot report both first results correctly. At the same tick, bijectivity preserves the distinction between the full ring states. An accessible record at re-arming or a later executing read still requires a physical path.

This comparison covers the specified exact ready signatures, including any later return to either signature at the same declared stage. Its force comes from requiring **one common second request and a readable first result at re-arming**. A clock value, second-setting label or stored history that varies with the first outcome would itself have to carry an accounted accessible record. A native later read that crosses the re-arming interval requires its own causal path and clock. A ready class allowing distinct readable coordinates for different first outcomes is a different interface and would need a derivation showing that the second write operates on both classes. [Fixed, physically readable retention and sourced clock](../o-ret-routes-20261103/DEFINITIONS.md#L23-L73)

## Failures, residuals and control cases

- **Failed preparation or loading.** The counting-law comparison at fixed $b_{c_1}$ gives mass $2^{-8}$ to the eight-constraint precursor event. Its complement also evolves by the full $F$. One explicit wrong-load witness is $X_2=1$, which flips the requested load of $A_1$ under that comparison. The complement can contain other histories and is not an observed failure rate. The physical apparatus has no sourced readiness flag, reject log, failed-try continuation or renewal law. No branch is discarded in the mathematical comparison. [Counting-law and wrong-load control](../oi-qm-ext-1/preparation-loading.md#L211-L237) · [Whole output and failed preparations](../oi-qm-ext-1/preparation-loading.md#L326-L363)
- **No event.** For $c_1=0,z=0$ the receiver has a zero in the supplied model. A laboratory no-event entry would require a physically timed opportunity and a retained completion record even when no event occurs. The sources identify no native completion interaction or calibrated window. Its probability is undetermined.
- **Renewal and the first record.** All fields and correlations in $W_2$ continue under $F$. Supplying a fresh $\eta$ for the second attempt would impose ordered readiness a second time. The inherited eight-bit restriction is an ensemble support account relative to counting. A physical supply, its consumed resources, the changed state of the supplier, and any export of record information still need a native history. A list of the earlier projections held by an analyst gives a correct retrospective decoder yet adds no apparatus memory. [Resource accounting and scope](../oi-qm-ext-1/preparation-loading.md#L292-L324) · [Native access and repeat control](../o-acc-native-record-20261117/O-ACC.md#L323-L381)

## Decision and evidence that would change it

**Source decision.** The path lacks a forward producer of the common precursor and selectable recorded requests, beginning with the physically justified supply for the quiet control neighbors and accompanying correlations. A source witness that would change this stop would identify the producer's cells, its independently justified initial or boundary law and a forward interaction on the same $F$ that delivers this input for both requests while accounting for the producer's residual. For a repeatable proposal it must trace the successor supply from the first attempt, with the status of failed and no-event branches and a physically timed read. The source cannot be inferred from the exact inverse image.

**Apparatus decision.** With the exact ready signature retained, a complete successor proposal must show *where the first record remains readable while the four coordinates are re-used*. The discriminating demonstration would give two positive-mass first histories with different records under one accounted source. Both must reach the full second ready contract for the same request and clock. Show a native read of the differing record through re-arming and a second measurement from both residuals. A separately justified ready interface could instead preserve a discriminating coordinate and demonstrate the second measurement for both values. This selects the **record path and preparation interface** as the design obligation. The incompatibility established here is for one interface, so it provides no basis to adopt a new microscopic update.

Earlier #1358 and #1363 results supply distinct negative source controls for the stipulated Native A input and unsourced chamber gradient. This record uses neither as a premise of the ready/read compatibility check. The inherited conditional route, one-tick field carry and narrower ready/read finding do not establish a working physical instrument. A1 is **OPEN / UNADOPTED**. [Prior producer evidence](../native-producer-2-20261117/SOURCE-SCREEN.md#L69-L115) · [Prior gradient evidence](../diffusion-readiness-20261118/ASSESSMENT.md#L33-L64)

**Review and provenance under §A.42 item 8.** #1377 records owner scope and responsibility. #866 names the physical source obligation, #1169 coordinates it and #1032 names the retention obligation. #1358 and #1363 identify the two prior stops, with their bounded evidence on the pinned tree. Draft #1378 and `133dc1ff926e908688ce402e0c47fb8df5aefe4e` identify the protocol and its order relative to this decision. The separate scientific review should check that the source stop follows from the landed contract, verify all four rows against the original timeline, and check the equal-request/time and fixed-interface restrictions. This record uses source inspection and exact comparison on paper.
