# Erdős Problem #64 — recovered-data and significance review

**Review date:** 2026-08-05 Pacific time / 2026-08-06 UTC  
**Recovery commit:** `34683df66206bd188a9f6a67b91fb94289e6d780`

## Bottom-line assessment

The recovered workspace does **not** contain a proof or a counterexample to Erdős Problem #64. It does contain:

1. a high-integrity preservation and audit framework;
2. several exact restricted-family eliminations;
3. a useful one-port classification and a certified lower bound for bridge-containing cubic counterexamples;
4. a reproducible order-28 cubic census audit;
5. a new general structural argument, derived during this review from Carr's lemmas, strengthening the posted `+1` count to
   \(|V_3|\ge2|V_{\ge4}|+3\).

The structural result has the highest global mathematical significance. The large computational counts are valuable negative information about particular construction families, but they do not approximate an exhaustive search over all minimum-degree-three graphs.

## Directly checked during review

- The Git bundle SHA-256 matches the preservation record, and the bundle clones at the recorded commit.
- All 11 reconstructed latest-claim audit files are present and match their recorded SHA-256 values. Every one is explicitly marked as not a global solution.
- A fresh Linux build of nauty `labelg` and the independent C++ cycle auditor rechecked the 251 recovered order-28 connected simple cubic, C4/C8-free classes: every class contains a C16; the minimum C16 count is 153 at index 201.
- The preserved order-31 one-port near-candidate has degree sequence `(2,3,...,3)` and exact cycle vector `(C4,C8,C16)=(0,0,138)`. It is neither minimum-degree three nor power-cycle-free.
- Repository tests yielded 32 passes, one skip, and five failures. Four failures are caused by the unavailable `python-sat` dependency in the review environment. One failure is substantive for bundle-level reproducibility: `sat_proofs/two_odd_cycles_n30_static/proof_check.json` is absent from the Git bundle.

## Evidence hierarchy

### Highest weight

- Human-checkable structural reductions.
- Complete finite classifications whose generator completeness and semantic checks are independently bound.
- Static proof certificates checked by independent implementations.

### Medium weight

- Signed audit summaries whose hashes survive but whose original large packets or `/private/tmp` logs no longer do.
- Exhaustive searches of explicitly defined lift, expansion, or port families.

### Low global weight

- Raw assignment counts without a theorem showing that every possible counterexample belongs to the searched family.
- Heuristic near-candidates and objective improvements.
- Solver-level UNSAT claims for which no static proof packet survives.

## Most significant recovered mathematical results

### 1. Minimal-counterexample density

The posted argument proving \(|V_3|\ge2|V_{\ge4}|+1\) is valid, with the displayed lengths understood as \(2^k\) and \(2^{k+1}\). A stronger quotient argument gives

\[
|V_3|\ge2|V_{\ge4}|+3.
\]

The proof is recorded separately in `ERDOS64_MINIMAL_COUNTEREXAMPLE_PLUS3_LEMMA.md`. This is general: it applies to every hypothetical minimal counterexample, conditional on Carr's two structural lemmas.

### 2. One-port classification and bridge bound

The workspace gives an exact classification of connected one-port graphs through odd order 27 and derives that a cubic counterexample containing a bridge must have at least 58 vertices.

The remaining edge-subdivision branch for one-port order 29 is the rooted-edge order-28 census. Residues 0–23 were last independently observed complete; the safe restart covers residues 24–255. The triangular-port order-26 branch is already audited. Completing the rooted-edge scope would therefore support one-port order 29 and raise the bridge-containing cubic lower bound from 58 to 62.

### 3. Order-28 cubic census

The 251 recovered connected simple cubic C4/C8-free classes all contain a C16. This is a strong and reproducible class-level census, but it no longer defines the broadest finite-order frontier because a separate public 2026 SAT repository claims the general minimum-degree-three case through order 31.

### 4. Lift, expansion, and gadget families

The q=3 lift census, large cyclic/nonabelian lift searches, partial triangle expansions, and three-port replacements eliminate many natural construction mechanisms. Their value is diagnostic: they show where counterexamples are not appearing. They do not become evidence for the universal conjecture until accompanied by a representation theorem reducing every counterexample to one of those mechanisms.

## Current-frontier comparison

- Avery Carr's 2026 preprint proves that high-degree vertices are independent, every vertex touches a degree-three vertex, and at least 4/7 of a minimal counterexample is cubic.
- A public SAT repository claims no minimum-degree-three counterexample through 31 vertices, hence order at least 32. Its principal method reaches 31; its independent CEGAR cross-check reaches 19.
- Julius Tranquilli's August 2026 preprint certifies that every simple cubic bipartite graph through 58 vertices has a C4, C8, or C16, hence a cubic bipartite counterexample has at least 60 vertices.
- The recovered bridge bound 58 and the bipartite bound 60 are incomparable because they concern different subclasses.

## Best use of the recovery

The highest-value theoretical direction is to develop the quotient used in the `+3` lemma. Let `A_i` denote degree-three vertices with `i` neighbors inside `V_3`. The quotient on `V_{>=4}` generated by `A_1` is simple, power-cycle-free after edge doubling, and necessarily 2-degenerate. For at least two high-degree vertices, this forces `|A_2|>=6`. These exact defect constraints are more likely to yield a representation theorem than further unconstrained lift searches.

The highest-value computational continuation is the exact rooted-edge order-28 completion from residue 24 through 255, because it closes a named theorem-level branch rather than merely extending a heuristic lane.

## Reproducibility limits

The full archive set, not the Git bundle alone, is the authoritative binary product. The bundle is excellent for code, tracked audits, and many resident artifacts, but it does not contain every proof packet. Ten shared-state symlinks point to vanished temporary paths, the original final `CLAIMS.jsonl` is unavailable, and several solver-level claims must remain demoted until independently regenerated with static certificates.
