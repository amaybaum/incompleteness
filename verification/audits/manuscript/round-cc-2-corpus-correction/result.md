# Corpus correction round CC-2 — the premise ledger's 27 drift and tension items, with the verification surfaces they move: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #785.

- **`D`** — `6d335d0ad7a19092b6a10098afcea162a632a402`, the head of `main` after `CC-1`'s halted record landed (push run
  37147553791, every job green); every execution path of this round byte-identical at `D` to its state at `0f2687b7`,
  the premise ledger's audited base.
- **`F`** — `d914af838f709f42cdd973cef3322872901a282e`, parent `D`; `delta(D, F)` is the preregistration alone, blob
  `2e08e0d6f0e3267b308a0f0b2c2f52d61deefb08`, sha256 `20a99c9fe2f8f710…`. Its exact-head `workflow_dispatch` run
  37148141531 (attempt 1) concluded `success`, 32 of 32 jobs, its `check-run` attestation; the owner designated `F`
  (PR #785 comment 5972886667).
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `CC-2-CORRECTED`

## The execution

| Commit | Content |
|---|---|
| `171bb10d2be5053b02e4884221e70bae1b8c2d6b` | C1: `controls.py`, blob `2fa1e022ea6683c0446f73fbb34355c5600c823c` (sha256 `9e0fda111337d08810983029720397607946538041420a2bfa4d58471bbee079`); self-test OK; `--check D` OK at `F` |
| `7f926d6f51cd7b6ee00adbfe7cba4e15faffbba8` | S1: the 60 substitutions applied verbatim to the eleven sources and the six verification-surface instances (V-1 … V-5) to the ledger and the probe; seven papers and the book rebuilt; `--check E` OK; exactly the 29 governed execution paths changed |
| this commit | S2: this note; candidate `E` |

Every item of section 3 applied; none halted; the five deferred sites are byte-identical to `D` (checked by
`controls.py`). Bands unchanged.

## The closure steps (preregistration section 5)

1. **Frozen disposition table** — preregistration section 3 at `F`; `controls.py` embeds every instance literally
   (60 manuscript, 6 verification-surface) and the two agree instance by instance (its `--check D` at `F` found each
   `old` exactly once in its file).
2. **Governed-path census** — sha256 of the 29 governed execution paths at `F` and at S1 (below).
3. **Ledger-source link** — every instance of section 3 carries its frozen ledger source; the verification-surface
   instances name the substitution that forces each.
4. **Mirrors in the same commit** — S1 is one commit; the `FULL.md` instances are byte-identical to their chapter
   instances; `mirror_check`: 0 chapter lines absent from `FULL.md`.
5. **Regeneration** — `sh ./build.sh Substratum Main GR SM Structure Explainer Methodology` and `sh ./build.sh --book`
   in S1, no dropped glyph; `staleness_check`: 13 matched, 0 unstamped. Page counts: Substratum 50; Main 87; GR 82;
   SM 145; Structure 98; Explainer 67; Methodology 54; book 540 (`D`: 50 / 87 / 82 / 144 / 98 / 67 / 54 / 540; SM
   gains one page from the longer lemma statement).
6. **Re-grep counts** — measured at `F` (= `D` for every source) and at S1, corpus-wide (`papers/*.md`, `book/*.md`):

| phrase | D | S1 | predicted |
|---|---|---|---|
| `establishes the same conclusion` | 1 | 0 | ok |
| `convenience of proof, not a physical restriction` | 1 | 0 | ok |
| `provided the partial-trace machinery` | 1 | 0 | ok |
| `conditional on finite reversible substratum dynamics` | 1 | 0 | ok |
| `excluded by the observed unitarity` | 2 | 0 | ok |
| `observed unitarity of quantum dynamics` | 4 | 0 | ok |
| `scales as $S(V) = \eta` | 1 | 1 | ok |
| `The *area law*` | 3 | 0 | ok |
| `The *area* of a region` | 3 | 0 | ok |
| `translation-invariant, isotropic, and reversible` | 1 | 0 | ok |
| `now derived rather than postulated` | 1 | 0 | ok |
| `is therefore complete.` | 2 | 0 | ok |
| `**Theorem** (Discrete Einstein equation)` | 1 | 0 | ok |
| `discrete Einstein theorem` | 1 | 0 | ok |
| `fixed by relativistic causality` | 3 | 0 | ok |
| `propagation speed $v = \alpha$` | 1 | 0 | ok |
| `rests on $q$-gauge invariance` | 1 | 0 | ok |
| `separate derivation chain not developed here` | 2 | 0 | ok |
| `substratum's sole free parameter` | 2 | 0 | ok |
| `This is the input from Lemma` | 4 | 0 | ok |
| `The framework requires finite $|S|$` | 2 | 0 | ok |
| `physically finite` | 2 | 2 | ok |
| `## 3. Background Independence and the Selection` | 1 | 0 | ok |
| `By the bounded coupling degree of` | 1 | 0 | ok |
| `couples nearest neighbors; any edge` | 1 | 0 | ok |
| `The observed physics is quantum mechanical` | 1 | 0 | ok |
| `supported by holographic bounds` | 1 | 0 | ok |
| `seven structural facts` | 2 | 0 | ok |
| `The observed cosmological structure` | 3 | 0 | ok |

   The two surviving counts are the legitimate uses named in the preregistration (R8's corrected sentence; the real
   Gaussian area-law statement).
7. **§A.32/§A.33 added-text scan** — register families, mid-sentence caps, over the 60 manuscript `new` texts: 0 hits.
8. **Claim-surface sweep** — the out-of-scope term list over the 60 manuscript `new` texts: 0 hits.
9. **Verification surfaces** — at S1: `coverage_check: OK (129 canonical statements, 19 unattached checkers)`; the
   census carries `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` at `papers/Substratum.md` line 262 with
   fingerprint `f7e912991de09137` and `SM:L-unnamed-ff7b7d06` at `papers/SM.md` line 118 with fingerprint
   `ff7b7d068e326e1f`, and carries neither `SM:T-unnamed-f1d3c661` nor `SM:L-unnamed-332dde89`; 129 ledger entries;
   the probe's delimiter sentence occurs exactly once in SM.md section 3.1; `edge_rigidity_probe: ALL CHECKS PASS`.

Gate steps that read the manuscripts, run locally at S1: `duplicate_check` OK; `voice_check` OK (40 files);
`claims_check` OK; `citation_check` 112 citations, 0 broken; `dependency_label_check` OK (41 files).

## Census

At `F` (= `D` for every governed execution path):

```text
33c1f14476ba9a3e999debd79ed01c6af8a2bde792f4e013f7a79a3186e6965b  papers/Substratum.md
e5156c802795cc47ae36e7c64e10b8d2e94192a3465653cff8f313fa222c3b46  papers/Substratum.tex
5f77436b7a7b1a8bbe55192a35abc82b80a122819e02a9e412b5168fe88e2f7b  papers/Substratum.pdf
4a9ad4b97a1c341f81ba3d5163dd11b43472e8f8bac170ae11c58e411affbff2  papers/Main.md
7d2dafed6121ee24064b2c9240c8c7955e28b7e23b20dcd7ba4003bcac35853c  papers/Main.tex
e69b86a8ce10489dc5109faf80bfedeca393e2c0f348082146be013432d3c596  papers/Main.pdf
fbd2c410adadc09c125b7c72dc36557bffbaf197ac635333d8436eb8907a7a69  papers/GR.md
9252e32f0e2ecdd7e1a20b0c493d87090585dd2fad899967a8acaf5dd6873bc8  papers/GR.tex
a924251d68de3863c2dbbe6f7a611aa9a5fba4a44e9187b99652f414c5d4d829  papers/GR.pdf
6346c2d0f634a3b5a4d178397fad45d91f34bc59acb1638ac7c024fb7c0ff43e  papers/SM.md
1d098306d24bc652b4d387cd4d67616274144bf16df71a2243b164da0fb51e47  papers/SM.tex
79e5bb953608f717ecd333b96d6efb76c6099886685ce9c0064074d86c89f15e  papers/SM.pdf
56342557856a42cb84c1c8a3f9b5cae1829b338264492a8fbbcbcf612fd12ce8  papers/Structure.md
36e772533c855d627ab961ff999eabc87e69e260c6fd984094471422cad6d866  papers/Structure.tex
3ffec2e5d1c39bded377b7492792cf7cb2a5eabee79335b5e2cb968ed39bb734  papers/Structure.pdf
7ff34ef2863995322517acb1b386ce199bcf2457da42519b3eed7e77bb55a841  papers/Explainer.md
476e34600f6e8d456788aea146dba367efb71bd78858d64b095e5bb1592882ab  papers/Explainer.tex
30ab1e88c56614bdf53745f03bb9dad9528f3563e711f999c73bfc7fbaa16b93  papers/Explainer.pdf
ac969da2354253fb8a89bfbf46c80dd0a39793257e591c260fecc01eed5374f7  papers/Methodology.md
4d31e328f09b388d31d52614126d0d2b7831bf75de0befdd7ebd1fc6ac8c7313  papers/Methodology.tex
a87e1833b6cdc3fe5e694070594e4319f814282fcd2f265e7f9b60cc58ce70ec  papers/Methodology.pdf
df4f32c0592ffa1201f86ed8b6d0e4442ef0a8e0353dcd57c7053162170db3d1  book/ch02-substratum.md
52f1427ba71fa380293cd722ec8ad2345b6bff20a0912ac51fde9473d0368eb3  book/ch05-gauge-structure.md
95810f8f5e7916d4ff0aaa44d945ccd94957756a39ff597ef5d30e447bb8b9f8  book/ch09-universality.md
dbeb4dd8be5641d0f2dedf9fce18bb10bfcf3685323a43b2a430d28456e8355f  book/The-Incompleteness-of-Observation-FULL.md
1bda0bd4c9413ba794ea86c27a0e814dde8ceffb600d16c661f792017c3a1971  book/The-Incompleteness-of-Observation-FULL.tex
c36178581e327f8c8accf2042ebd166de99edc8666df2ccfa03e704fd08f3a42  book/The-Incompleteness-of-Observation-FULL.pdf
d0a10c58efd08c581b1bc5ce2c7c5d17cb6c05d827739a407c0ee32d09076151  verification/coverage/LEDGER.json
e5fe0af947ec4941512f823e07516ab3f382868c7cfc6d4b08f351d08d62ed7d  verification/lean/edge_rigidity_probe.py
```

At S1:

```text
2099e31ce0d23751d299eec73cc41cef255a9316b4bfb7cb65c05d21a8ea2cd8  papers/Substratum.md
136946fb38a19ee2b149ed58a799ef99fe5a6df83b39363c86328a9bc0cb2e06  papers/Substratum.tex
c6fe0880a17b36c9784320ce07b881fb070bf9a9696aac4afa096b342dbe063f  papers/Substratum.pdf
4621abc1ea77b9a6cfdcc5ec72855f4e914b38d8abb649295c6299192cf5fb23  papers/Main.md
98597966254c8d041bb3ad71ee48726ad30ebb37be8ff8b4f1619c17852c05c6  papers/Main.tex
bc3b4447a1785da82d6085381defb510745432bd1fa1382ec150d5569c2e2fdd  papers/Main.pdf
0f41f3c494a0550f6b1112daeac536e964f3f185a16d9b7387fd5b71dbc0cbe2  papers/GR.md
5d89aaaa47fc4b0dd8fbcdc80f5339320c45e17d6d5481c48e56d42566dfac50  papers/GR.tex
9231ca9a852eb2d8182732bb88722901606d65676564ba63938fd92cf17ce02c  papers/GR.pdf
d0d7fe770fcc8366b76c79b3412827860fd7763f2745aacfa689ff8159d00545  papers/SM.md
41ff7fdd6c3d78a1acb8f463c080b877d18e32af54ccf049550116f396be61f5  papers/SM.tex
d492f671bbd4f8fc5eacc9ded562a6c47b29332324c8d66a5eec30420f58fb23  papers/SM.pdf
b80cff63d884aec2cbcc3318553ea4ed3a2edc99fca7d009face2bc5e21070dd  papers/Structure.md
e114bfb3ce535157f29fb68ee27855cb2ebb6a06bb771d0b689c623cc8e1dfb1  papers/Structure.tex
bd65e65a2404d7963999a1e710a0042607acffc6461e84e03058187120df5555  papers/Structure.pdf
7c266955142d735bd939681b930170a33ec0e64a69093f29180fd2191ad34db6  papers/Explainer.md
d8e679a508209957e1d35b2a87f0b049bc2b00684b159f9dc3a5117693654249  papers/Explainer.tex
efda5b30e87718e87c290f04958176917ad9466e0bac89b591b3b6f6c1237653  papers/Explainer.pdf
8c3dc391734fdfa924e3e67be1db2c6bea1aa199cf8706574514af1bf3c9e5d8  papers/Methodology.md
9ea3ecfb769efaa47a39acf73c11415a9a843ec9f27c6b0998092fd84502f8f8  papers/Methodology.tex
5240b9584f9ffd4a0f4d95d56418db9b85b0a4b7fe5a243344730c08d4728937  papers/Methodology.pdf
2318fbce880103462a66dae8a1c283b9e6b40f68118d85bfb5196b220998a2cd  book/ch02-substratum.md
46357566ccb9638ad52c9cb754a445f2272d0db97287411f1e779f51eccd462f  book/ch05-gauge-structure.md
50248d340d1de9bf5d5be6dca5e7c668e697b0a284bb7df600e3f1f9098051ee  book/ch09-universality.md
771696067e4566eab267d1d653d69055913a91e88db7363301b896ce6c6df10e  book/The-Incompleteness-of-Observation-FULL.md
c060e35ce2a45f58b2ca4952fa2226e1dd4abdf527a66299723c03518e5e5a68  book/The-Incompleteness-of-Observation-FULL.tex
ca7d37410f82ccd49765f013055470983fe94a7efa07535316dc74f1f6ca39ea  book/The-Incompleteness-of-Observation-FULL.pdf
71820f0baee7a49d5eaf4282322e4a31bd8171273badf6d4039ebf66be7a2702  verification/coverage/LEDGER.json
b1f29bfeb1f66754d28b83780073c0b576967d896b814e505f063771f0ca2898  verification/lean/edge_rigidity_probe.py
```

## What stays open

The five deferred items (R3, R9, R10, T-HT1-1, T-E-3) are untouched, for the reasons the preregistration gives; they
belong to the round after 3B. No ledger replacement obligation is discharged by this round. The two re-affirmed
coverage entries keep `kernel` `GAP`; the removed entry's statement is no longer a canonical theorem of the corpus.
