# AI assistance, authorship, and claim status

## Human direction and authorship

**Zackary Loevseth** directed the mathematical target, long-horizon execution protocol, preservation requirements, recovery decisions, evaluation criteria, theorem-first redirection, and public-release decision. The repository owner also reported completing a line-by-line review of the reconstructed proof.

## AI assistance

OpenAI systems, including Codex and ChatGPT/GPT-5.6 Pro, substantially assisted with:

- recovering and auditing the multi-gigabyte research workspace;
- distinguishing global, structural, restricted-class, computational, and rejected claims;
- deriving the quotient-graph mechanism from Carr's structural lemmas;
- producing structurally separate proof reconstructions;
- checking the parity step and the \(b=0,1\) boundary cases;
- clean-clone and manifest verification in the local sealed workspace;
- drafting the public theorem note, provenance record, and claim ledger.

The larger research process also used Anthropic systems for adversarial review and mathematical critique.

## Claim-status ledger

### Open problem

Erdős Problem #64 remains open. This repository claims neither a global proof nor a counterexample.

### Structural theorem

The note

```text
proofs/minimal-counterexample-excess-theorem.md
```

gives a complete human-checkable proof that every lexicographically minimal counterexample satisfies

\[
|V_3(G)|
\ge
4+\sum_{v\in V_{\ge4}(G)}(d_G(v)-2).
\]

Equivalently, with \(b=|V_{\ge4}(G)|\) and
\(s=\sum_{v\in V_{\ge4}(G)}(d_G(v)-4)\),

\[
|V_3(G)|\ge2b+s+4.
\]

The proof depends on two published structural lemmas of Avery Carr: high-degree vertices are independent, and every vertex has a degree-three neighbor.

### Derived sparsity consequences

Under the minimum-order, then minimum-size convention, the note derives

\[
|E(G)|\le2|V(G)|-b-2,\qquad
\operatorname{mad}(G)<4,\qquad
\operatorname{arb}(G)=2.
\]

### Superseded theorem candidate

The earlier `proofs/minimal-counterexample-plus3.md` note is retained for provenance but is strictly superseded by the excess-sensitive \(+4\) theorem.

### Computational audits

The included order-28 and one-port JSON files verify only their declared finite scopes. They are not evidence that all finite graphs have been searched.

## Review boundary

The theorem was internally reconstructed, clean-clone checked, and reviewed line by line by the repository owner. It has not received external specialist peer review or formal proof-assistant verification. No priority or novelty claim is made.

Readers should independently inspect the proof and preserve the distinction between:

- a general structural theorem about a hypothetical minimal counterexample;
- finite computational audits of specified graph classes;
- local sealed provenance;
- and the unresolved global conjecture.
