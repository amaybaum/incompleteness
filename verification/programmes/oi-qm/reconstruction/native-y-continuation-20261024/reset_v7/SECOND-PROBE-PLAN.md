# Follow-up decision rule: general two-code routing

The first exact probe excluded the stipulated one-hop code `(0,y,0)` for
every G(u), but that alone does not exclude a different common encoding of y.
Before evaluating this broader question, fix its decision rule:

- Enumerate the 64 pairs `(G(0),G(1))` in the already computed exact table.
- Accept a native encoding only if every x and selector-mask row with
  `p=x XOR u` gives the same full triple for the same y, and the two y triples
  are distinct.
- Test the separate q7.D intervention similarly, now requiring the entire
  endpoint to depend only on p7 for all x,u and masks, with distinct outputs.
- Print either the complete candidate list or the finite-family exclusion.
  No decoder reading u, x, history, or another site is allowed.

Also export exact algebraic normal forms of the native q7 incoming interface
and of q8 under the q7.D intervention. These expressions must be verified
against every relevant measured row. They explain any obstruction, rather
than expanding it to other directions, several new sources, or later ticks.
