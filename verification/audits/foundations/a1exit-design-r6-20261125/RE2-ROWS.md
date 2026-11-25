# RE-2: the 43 controls proposed to need no separate restored case (for owner review)

v6.0e sec. 10 (D:2081-2082): "Each control runs in both directions: the mutant gives the stated outcome, and the restored tree returns to its control outcome." The argument for (b) is textual: the second direction is defined as the restored tree of a mutant. Where a control applies no mutation, its own run is the control outcome and there is no restored tree. The column "Mutation in the case?" is a mechanical scan of the row and its design text for a mutation (mutant, mutated, planted, removed, changed, rewritten, added, edit, wrong, broken); every "yes" or "check" row stays a verification defect unless review shows no mutation is applied.

| Control | Direction | Design expectation (source) | Mutation in the case? |
|---|---|---|---|
| B1 | positive | authorized-removal; hit at offset 'in image' D:2109 | yes |
| B2 | positive | authorized-replacement with line range D:2110 | no |
| B3 | positive | overlap rule of sec. 5 D:2111 | no |
| B4 | positive | located, spanned to EOF D:2112 | no |
| B6 | positive | site unchanged D:2114 | yes |
| EI8 | positive | pre-run passes, entry runs D:2318 | no |
| K10 | positive | PASS D:2303 | no |
| K2 | positive | PASS, context_changed true D:2101 | yes |
| K9 | positive | PASS; partial_quote; toggle invariant D:2108 | no |
| L1 | positive | PASS D:2130 | no |
| L2 | positive | PASS D:2131 | no |
| N-W | positive | no deny match D:2158 | no |
| O9 | positive | record admitted D:2185 | no |
| R17 | positive | PASS for that commit D:2289 | no |
| RT-A | positive | PASS; ref 0 errors, 697 anchors D:2206 | no |
| RT-C | positive | checks as sec. 11; PASS only with contract evidence D:2211 | no |
| RT-D | positive | 0 deny; 11 W1/W2 PASS; GR.md:58; 45 resid REVIEW, 17 only resid D:2212 | no |
| RT-D-gr58 | positive | GR.md:58 PASS with its record D:2212 | no |
| RT-DR | adversarial | FAIL deny-match; 6 targets by id; H 86/61/28/1; E 95; T1' 0 D:2213 | check |
| RT-DR3W | adversarial | one DR-3 sentence at H line 37-38; 0 at T1' D:2214 | no |
| RT-E | positive | PASS; 697 unchanged D:2207 | yes |
| RT-H0 | adversarial | FAIL all HP; 113; 7 meaning; 7 structure D:2208 | check |
| RT-I7 | adversarial | FAIL both; T1' 7/0/0, A1 4; H 11/1/2, A1 179 D:2215 | no |
| RT-I7A | adversarial | H 86+123=209 (93/216), 95 retired FAIL; T1' 0/12 D:2216 | no |
| RT-T | positive | PASS only with all records; NOT RUN until then D:2210 | no |
| RT-T0 | adversarial | FAIL HP 113/7/7; RET 19/5/3; counts D:2209 | check |
| S11-56 | positive | 0 findings = P static_new; mutants FAIL D:2292 | yes |
| S11-57d | positive | split as P; = static_new D:2296 | no |
| TR48 | positive | accepted; T recorded D:2278 | no |
| TR5 | positive | chain admission, all snapshot fields (CI only) D:2269 | no |
| TR5-sim | positive | in-memory TR5 (no row) D:2269 | no |
| U1 | positive | none in v6.0e (D:2096 'stand'; DESIGN.md:347) | check |
| U10 | positive | none in v6.0e (DESIGN.md:356) | no |
| U11 | positive | none in v6.0e (DESIGN.md:357) | check |
| U2 | positive | none in v6.0e (DESIGN.md:348) | no |
| U3 | positive | none in v6.0e (DESIGN.md:349) | no |
| U6 | positive | none in v6.0e (DESIGN.md:352) | no |
| V27 | positive | PASS (no hit) in both D:2138 | no |
| V27-glossary | positive | second case of V27 D:2138 | no |
| V4 | positive | PASS (no hit) D:2137 | no |
| WB1 | positive | PASS both lines D:2250 | no |
| WB13 | positive | PASS D:2262 | no |
| WB8 | positive | PASS D:2257 | no |
