# Corpus correction round CC-1 — the premise ledger's 27 drift and tension items: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #784.

- **`D`** — `0f2687b7b87925b53c6e3d8c6d1a233f36624dea`, the head of `main` after `OPACT-1` landed (push run
  37035333423), identical to the premise ledger's audited base.
- **`F`** — `2cd8ff91a8772c300f379469d7789845587eb39e`, parent `cb66db6291b6e2e0b006693dbd1461484fac8cdd` (a drafting
  commit on the first-parent chain from `D`; the two together change only the preregistration);
  `delta(D, F)` is the preregistration alone, blob `1a42e669ca988b90312ee8930d6af2c9f9ff0694`, sha256
  `2d58da2468d650abf44a7eba58dfb0e076ac3df477ac083f84b9a2bf920d732c`. Its exact-head `workflow_dispatch` run
  37142054525 concluded `success`, its `check-run` attestation; the owner designated `F` (PR #784 comment
  5972019225). The first drafting commit's exact-head run 37140734308 failed the release gate's `duplicate` step on
  the preregistration's own chapter/`FULL.md` mirror blocks, corrected in `F` by stating those instances by
  reference; no other step was red.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `CC-1-CORRECTED`

## The execution

| Commit | Content |
|---|---|
| `babad11ad7186609cb6106ffa2623b8883782bc4` | C1: `controls.py`, blob `e14474e7827e4d12891a096522a537878d5cdd7e` (sha256 `d51e6bde4c4f29950662f8b2b296bd9754eb2e0ae0f39a0e79d5217069ebb493`); self-test OK; `--check D` OK at `F` |
| `93bbeb1581c8eba048abc22e11b9332e3df37150` | S1: the 60 substitutions applied verbatim to the eleven sources; seven papers and the book rebuilt; `--check E` OK |
| this commit | S2: this note; candidate `E` |

Every item of section 3 applied; none halted; the five deferred sites are byte-identical to `D` (checked by
`controls.py`). Bands unchanged.

## The closure steps (preregistration section 5)

1. **Frozen disposition table** — preregistration section 3 at `F`; `controls.py` embeds every instance literally
   and the two agree instance by instance (its `--check D` at `F` found each `old` exactly once in its file).
2. **Governed-path census** — sha256 of the 27 governed execution paths at `F` and at S1 (below).
3. **Ledger-source link** — every instance of section 3 carries its frozen ledger source.
4. **Mirrors in the same commit** — S1 is one commit; the `FULL.md` instances are byte-identical to their chapter
   instances; `mirror_check`: 0 chapter lines absent from `FULL.md`.
5. **Regeneration** — `sh ./build.sh Substratum Main GR SM Structure Explainer Methodology` and `sh ./build.sh --book`
   in S1, no dropped glyph; `staleness_check`: 13 matched, 0 unstamped. Page counts: Substratum     ok  50 pages; Main           ok  87 pages; GR             ok  82 pages; SM             ok  145 pages; Structure      ok  98 pages; Explainer      ok  67 pages; Methodology    ok  54 pages; book           ok  540 pages.
   (`D`: 50 / 87 / 82 / 144 / 98 / 67 / 54 / 540; SM gains one page from the longer lemma statement.)
6. **Re-grep counts** — measured at `D` and at S1, corpus-wide (`papers/*.md`, `book/*.md`):

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
7. **§A.32/§A.33 added-text scan** — register families, mid-sentence caps, over the 60 `new` texts: 0 hits.
8. **Claim-surface sweep** — the out-of-scope term list over the 60 `new` texts: 0 hits.

Gate steps that read the manuscripts, run locally at S1: `duplicate_check` OK; `voice_check` OK (40 files);
`claims_check` OK; `citation_check` 112 citations, 0 broken; `dependency_label_check` OK.

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
```

At S1:

```text
2099e31ce0d23751d299eec73cc41cef255a9316b4bfb7cb65c05d21a8ea2cd8  papers/Substratum.md
136946fb38a19ee2b149ed58a799ef99fe5a6df83b39363c86328a9bc0cb2e06  papers/Substratum.tex
05069b4c58a9c0382f981e816f61cf09cda1a20ef81b24f570bc4727d1333fb7  papers/Substratum.pdf
4621abc1ea77b9a6cfdcc5ec72855f4e914b38d8abb649295c6299192cf5fb23  papers/Main.md
98597966254c8d041bb3ad71ee48726ad30ebb37be8ff8b4f1619c17852c05c6  papers/Main.tex
c082c711052ef2e1c6a316a0a8975e9c061f4982ea4e5637c9d6a0cf57bc7d46  papers/Main.pdf
0f41f3c494a0550f6b1112daeac536e964f3f185a16d9b7387fd5b71dbc0cbe2  papers/GR.md
5d89aaaa47fc4b0dd8fbcdc80f5339320c45e17d6d5481c48e56d42566dfac50  papers/GR.tex
6b7353a10a607288735aabbf332a946c32018a1781cdb91056f9ecf0fa0fe4a6  papers/GR.pdf
d0d7fe770fcc8366b76c79b3412827860fd7763f2745aacfa689ff8159d00545  papers/SM.md
41ff7fdd6c3d78a1acb8f463c080b877d18e32af54ccf049550116f396be61f5  papers/SM.tex
331156f478d4fbb434067c5e8f2d960ef29c83f9c5c03d4783a73ddd4c9c1fd0  papers/SM.pdf
b80cff63d884aec2cbcc3318553ea4ed3a2edc99fca7d009face2bc5e21070dd  papers/Structure.md
e114bfb3ce535157f29fb68ee27855cb2ebb6a06bb771d0b689c623cc8e1dfb1  papers/Structure.tex
381844dcca3a82ef1a47f06c14b3c615c245a2cedce5ea9e56efdbaa2dd8bc41  papers/Structure.pdf
7c266955142d735bd939681b930170a33ec0e64a69093f29180fd2191ad34db6  papers/Explainer.md
d8e679a508209957e1d35b2a87f0b049bc2b00684b159f9dc3a5117693654249  papers/Explainer.tex
33c259c8eedfb18886063a4a3d7195df011395537f87754c7233e9366843470a  papers/Explainer.pdf
8c3dc391734fdfa924e3e67be1db2c6bea1aa199cf8706574514af1bf3c9e5d8  papers/Methodology.md
9ea3ecfb769efaa47a39acf73c11415a9a843ec9f27c6b0998092fd84502f8f8  papers/Methodology.tex
1eb80b4595ab7e7356f2948c55ef109155b042e28ea0c2d270031e24c29b7060  papers/Methodology.pdf
2318fbce880103462a66dae8a1c283b9e6b40f68118d85bfb5196b220998a2cd  book/ch02-substratum.md
46357566ccb9638ad52c9cb754a445f2272d0db97287411f1e779f51eccd462f  book/ch05-gauge-structure.md
50248d340d1de9bf5d5be6dca5e7c668e697b0a284bb7df600e3f1f9098051ee  book/ch09-universality.md
771696067e4566eab267d1d653d69055913a91e88db7363301b896ce6c6df10e  book/The-Incompleteness-of-Observation-FULL.md
c060e35ce2a45f58b2ca4952fa2226e1dd4abdf527a66299723c03518e5e5a68  book/The-Incompleteness-of-Observation-FULL.tex
542906796d2109b4aa6d8a89f9bc97844901cc3aaa6cfc8349faa84d72b69f14  book/The-Incompleteness-of-Observation-FULL.pdf
```

## What stays open

The five deferred items (R3, R9, R10, T-HT1-1, T-E-3) are untouched, for the reasons the preregistration gives; they
belong to the round after 3B. No ledger replacement obligation is discharged by this round.
