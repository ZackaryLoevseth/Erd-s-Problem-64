# Erdős Problem #64 — structural and computational research notes

> **Status:** Erdős Problem #64 remains open. This branch does **not** claim a proof or a counterexample.

The problem asks whether every finite simple graph of minimum degree at least three contains a cycle of length \(2^k\) for some integer \(k\ge 2\).

This publication records a recovered research state, selected independent audit outputs, and a new **theorem candidate** about hypothetical minimal counterexamples. It is intentionally isolated on the branch [`publication/erdos-problem-64`](../../tree/publication/erdos-problem-64); it is unrelated to the repository's default-branch work on Erdős Problem #409 and is not proposed for merger into that project.

## Main theorem candidate

Assume \(G\) is a minimum-order counterexample and use Avery Carr's two structural results that:

1. the vertices of degree at least four form an independent set; and
2. every vertex has a neighbor of degree exactly three.

Writing

\[
V_3=\{v:d_G(v)=3\},\qquad V_{\ge4}=\{v:d_G(v)\ge4\},
\]

the note proves

\[
\boxed{|V_3|\ge 2|V_{\ge4}|+3}.
\]

Consequently,

\[
3|V_3|\ge 2|V(G)|+3.
\]

The proof uses a simple quotient graph on \(V_{\ge4}\) represented by degree-three vertices with exactly one neighbor in \(V_3\), and shows that quotient must be 2-degenerate. See [`proofs/minimal-counterexample-plus3.md`](proofs/minimal-counterexample-plus3.md).

**Verification status:** the argument was independently derived during an AI-assisted recovery review and has not yet received external human verification. It should be treated as a theorem candidate, not as an established published theorem.

## Contents

- [`proofs/minimal-counterexample-plus3.md`](proofs/minimal-counterexample-plus3.md) — complete human-readable proof of the proposed \(+3\) density bound.
- [`reports/data-and-significance-review.md`](reports/data-and-significance-review.md) — assessment of what the recovered data does and does not establish for Problem #64.
- [`audits/n28-complete-census-fresh-audit.json`](audits/n28-complete-census-fresh-audit.json) — independent audit of 251 recovered order-28 connected cubic \(C_4/C_8\)-free isomorphism classes; every class has a \(C_{16}\).
- [`audits/one-port-n31-audit.json`](audits/one-port-n31-audit.json) — exact audit of an order-31 one-port near-candidate, showing minimum degree two and 138 distinct 16-cycles.
- [`recovery/RECOVERY_SUMMARY.md`](recovery/RECOVERY_SUMMARY.md) — public preservation summary, hashes, bounded gaps, and restart boundary.
- [`AI_USE.md`](AI_USE.md) — authorship, AI assistance, and claim-status disclosure.

## What is established by the included audits

The order-28 audit reports that all 251 recovered connected simple cubic classes with no 4-cycle or 8-cycle contain a 16-cycle. Its scope statement is explicit: it independently verifies the recovered canonical union and cycle properties, but does not rerun the hundreds of millions of raw generator states used upstream.

The order-31 one-port object is **not** a counterexample. Its degree sequence is \((2,3,\ldots,3)\), and its exact cycle vector is

\[
(C_4,C_8,C_{16})=(0,0,138).
\]

## What is not established

This release does not establish either direction of the full conjecture. In particular, it contains neither:

- a finite graph of minimum degree at least three avoiding all cycles of length \(2^k\), nor
- a proof that every such finite graph contains one.

Large lift, expansion, gadget, and port searches in the recovered workspace concern restricted construction families. Their raw assignment counts must not be interpreted as exhaustive coverage of all minimum-degree-three graphs.

## Recovery provenance

The preserved research checkpoint is:

```text
Git commit: 34683df66206bd188a9f6a67b91fb94289e6d780
Freeze UTC: 2026-08-06T00:34:24Z
Files preserved: 23,569
Logical source bytes: 4,649,689,073
Verified restore: YES
```

The concise publication here does not attempt to place the multi-gigabyte archive in GitHub. The public recovery summary records the authoritative checkpoint, principal hashes, bounded gaps, and restart boundary; the full sealed handoff remains part of the preserved archive.

## AI assistance and authorship

The research target, preservation decisions, and publication decision were directed by **Zackary Loevseth**. OpenAI systems, including ChatGPT/GPT-5.6 Pro, substantially assisted with the recovery audit, selected verification work, mathematical derivation, and drafting. The exact disclosure and claim-status boundaries are in [`AI_USE.md`](AI_USE.md).

## References

- T. F. Bloom, “Erdős Problem #64,” Erdős Problems, accessed 2026-08-06: https://www.erdosproblems.com/64
- A. Carr, *Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic*, arXiv:2605.22844.

## Suggested citation

> Zackary Loevseth, “Erdős Problem #64 — structural and computational research notes,” public research branch, 2026. Unverified theorem candidate and computational audit release.
