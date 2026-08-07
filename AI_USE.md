# AI assistance, authorship, and claim status

## Human direction

**Zackary Loevseth** directed the research target, execution protocol, preservation and recovery decisions, theorem-first redirection, evaluation criteria, and public-release decision.

## AI assistance

AI systems substantially assisted with:

- recovering and auditing the large research workspace;
- separating global, structural, restricted-class, computational, historical, and rejected claims;
- deriving and refining the auxiliary-graph mechanism;
- producing structurally separate proof reconstructions;
- exact computational falsification and regression checks;
- prior-art comparison and claim-status calibration;
- drafting and revising the public theorem note, provenance record, and claim ledger.

OpenAI systems, including Codex and ChatGPT/GPT-5.6, were central to the theorem-first run and reconstruction. Anthropic Claude and DeepSeek were also used for adversarial critique and comparison against public prior work.

## Claim-status ledger

### Open problem

Erdős Problem #64 remains open. This repository claims neither a global proof nor a counterexample.

### Structural theorem

[`proofs/minimal-counterexample-excess-theorem.md`](proofs/minimal-counterexample-excess-theorem.md) gives a complete human-checkable argument that every counterexample chosen first with minimum order and then minimum size satisfies

\[
|V_3(G)|\ge
4+\sum_{v\in V_{\ge4}(G)}(d_G(v)-2).
\]

Equivalently, with \(b=|V_{\ge4}(G)|\) and \(s=\sum_{v\in V_{\ge4}(G)}(d_G(v)-4)\),

\[
|V_3(G)|\ge2b+s+4.
\]

The public proof rederives the minimality facts it uses. Their prior provenance is nevertheless acknowledged: Markström observed independence of the degree-at-least-four set, and Carr proved the degree-three-neighbour property and the published \(4/7\) density bound.

### Prior public comparison

A comment by `jul059` on the Erdős Problems #64 discussion thread dated 26 July 2026 gives \(|V_3|\ge2|V_{\ge4}|+1\). Accordingly, no claim is made that this repository first crossed the \(2/3\) threshold.

### Derived edge bound

The theorem gives

\[
|E(G)|\le2|V(G)|-b-2.
\]

This is advertised as an improvement over the prior \(2|V|-3\) consequence only when \(b\ge2\).

### Computational audits

The included finite audits verify only their declared scopes. They are not evidence that all finite graphs have been searched.

## Review boundary

The theorem passed multiple structurally independent **internal AI-assisted** proof reconstructions and exact falsification checks. These do not constitute external human peer review, independent research-group review, or formal proof-assistant verification.

No priority or novelty claim is made. Readers should independently inspect the proof and preserve the distinction among:

- a general structural theorem about a hypothetical minimal counterexample;
- finite computational audits of specified graph classes;
- local sealed provenance;
- internal AI-assisted verification;
- external specialist review, which has not yet occurred;
- and the unresolved global conjecture.
