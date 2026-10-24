// Cross-check: import card-table engine.js (read-only, by absolute path given as argv[2]) and print exact facts.
const eng = await import(process.argv[2]);
const { enumerate, lineDist, LINE_LO, LINE_N, CARDS, LINE_TEST, SELF_TEST, CAT_TEST } = eng;
console.log("SELF_TEST", JSON.stringify(SELF_TEST));
console.log("CAT_TEST", JSON.stringify(CAT_TEST));
console.log("LINE_TEST", JSON.stringify(LINE_TEST));
console.log("CARDS.length", CARDS.length, "m-values", JSON.stringify(CARDS.map(c=>c.m)));
for (const peek of [false, true]) {
  const d = lineDist(peek); let tot=0, odd=0, oddNZ=0, oddZero=[];
  d.forEach((v,x)=>{ tot+=v; const pos=x+LINE_LO; if (pos%2!==0){ odd+=v; if(v===0) oddZero.push(pos);} });
  console.log(`peek=${peek} total=${tot} oddMass=${odd} zeroOddPositions=${JSON.stringify(oddZero)} zeroAll=${JSON.stringify(d.map((v,x)=>v===0?x+LINE_LO:null).filter(v=>v!==null))}`);
  console.log(`peek=${peek} dist=${JSON.stringify(d)}`);
}
