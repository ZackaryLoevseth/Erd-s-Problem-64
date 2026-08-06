# Erdős Problem #64 — structural theorems and certified computational research

> **Status:** Erdős Problem #64 remains open. This repository does **not** claim a proof of the conjecture or a counterexample.

The problem asks whether every finite simple graph of minimum degree at least three contains a cycle of length \(2^k\) for some integer \(k\ge2\).

## Main structural theorem

Let \(G\) be a counterexample chosen with minimum order and, subject to that, minimum size. Define

\[
A=V_3(G),\qquad
B=V_{\ge4}(G),\qquad
b=|B|,\qquad
s=\sum_{v\in B}(d_G(v)-4).
\]

Using Avery Carr's published structural lemmas that \(B\) is independent and every vertex has a degree-three neighbor, the note proves

\[
\boxed{|A|\ge 2b+s+4}
\]

or, equivalently,

\[
\boxed{
|V_3(G)|
\ge
4+\sum_{v\in V_{\ge4}(G)}(d_G(v)-2).
}
\]

Consequently,

\[
\boxed{3|V_3(G)|\ge2|V(G)|+s+4}
\]

and

\[
\boxed{|E(G)|\le2|V(G)|-b-2}.
\]

The proof constructs a simple quotient graph on \(B\), proves that it is 2-degenerate by lifting every dyadic cycle back to \(G\), and then uses an exact parity obstruction to improve the initial \(+3\) count to \(+4\).

See [`proofs/minimal-counterexample-excess-theorem.md`](proofs/minimal-counterexample-excess-theorem.md).

### Sparsity consequences

Because the counterexample is minimal first by order and then by size, every proper subgraph is 2-degenerate. Together with the edge bound above, this yields

\[
\operatorname{mad}(G)<4
\qquad\text{and}\qquad
\operatorname{arb}(G)=2.
\]

The size tie-break is required for proper spanning subgraphs in this deduction; the core \(2b+s+4\) theorem itself uses only order-minimality after Carr's two structural lemmas are available.

## Verification and claim status

The theorem was produced in a theorem-first AI-assisted run and passed:

- structurally independent Codex proof reconstructions;
- clean-clone theorem and post-density checks;
- a sealed 72-entry publication-packet manifest;
- line-by-line review reported by the repository owner.

No external human peer review, formal proof-assistant verification, or novelty claim is asserted. The conjecture remains open.

The exact local seal metadata is recorded in [`recovery/THEOREM_FIRST_SEAL_20260806.md`](recovery/THEOREM_FIRST_SEAL_20260806.md). The machine-local Git bundle named there is not yet stored in this public repository; this branch publishes the human-checkable theorem and its provenance without claiming byte identity to an unavailable public bundle.

## Earlier and supporting material

- [`proofs/minimal-counterexample-plus3.md`](proofs/minimal-counterexample-plus3.md) — earlier \(+3\) theorem candidate, now superseded by the excess-sensitive \(+4\) theorem.
- [`reports/data-and-significance-review.md`](reports/data-and-significance-review.md) — review of the recovered computational workspace.
- [`audits/n28-complete-census-fresh-audit.json`](audits/n28-complete-census-fresh-audit.json) — audit of 251 recovered order-28 connected cubic \(C_4/C_8\)-free classes; every class contains a \(C_{16}\).
- [`audits/one-port-n31-audit.json`](audits/one-port-n31-audit.json) — audit of a rejected order-31 one-port near-candidate.
- [`recovery/RECOVERY_SUMMARY.md`](recovery/RECOVERY_SUMMARY.md) — preservation summary for the earlier multi-gigabyte research checkpoint.
- [`PUBLICATION_STATUS.md`](PUBLICATION_STATUS.md) — exact public claim ledger and merge gates.
- [`AI_USE.md`](AI_USE.md) — human direction, AI assistance, and claim boundaries.

## What is not established

This repository contains neither:

- a finite minimum-degree-three graph avoiding every cycle of length \(2^k\); nor
- a proof that every such graph contains one.

The structural theorem constrains every hypothetical lexicographically minimal counterexample. It does not establish that no counterexample exists.

## References

- T. F. Bloom, “Erdős Problem #64,” Erdős Problems, accessed 2026-08-06: https://www.erdosproblems.com/64
- A. Carr, *Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic*, arXiv:2605.22844.

## Suggested citation

> Zackary Loevseth, “Excess-Sensitive Degree-Three Bounds for Minimal Erdős–Gyárfás Counterexamples,” version 0.2.0, 2026. AI-assisted structural research note; novelty and external review pending.
