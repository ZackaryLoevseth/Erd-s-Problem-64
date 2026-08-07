# Publication status and claim ledger

## Global status

```text
ERDOS_64_GLOBAL_STATUS_OPEN
```

This repository contains neither a proof of the Erdős–Gyárfás conjecture nor a counterexample.

## Principal public theorem

For a finite simple counterexample \(G\) chosen first with minimum order and then, subject to that, minimum size, define

\[
A=V_3(G),\quad B=V_{\ge4}(G),\quad b=|B|,\quad
s=\sum_{v\in B}(d_G(v)-4).
\]

The public proof establishes

\[
|A|\ge2b+s+4
=4+\sum_{v\in B}(d_G(v)-2),
\]

and consequently

\[
3|A|\ge2|V(G)|+s+4,
\qquad
|E(G)|\le2|V(G)|-b-2.
\]

The edge inequality improves the prior-art \(|E(G)|\le2|V(G)|-3\) consequence when \(b\ge2\), is equal at \(b=1\), and is not advertised as an improvement at \(b=0\).

## Verification status

```text
PROVED_HUMAN_ARGUMENT
MATHEMATICAL_THEOREM_INTERNALLY_RECONSTRUCTED
FROZEN_CANONICAL_PROOF_SHA256:
  387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444
NOVELTY_NOT_ESTABLISHED
NO_EXTERNAL_SPECIALIST_REVIEW
NO_FORMAL_PROOF_ASSISTANT_VERIFICATION
```

The internal reconstructions were performed by AI systems in the same research project. They are not represented as independent human or independent research-group review.

## Prior-work boundary

- Markström: independence of the degree-at-least-four set, as recorded by Carr.
- Carr: every vertex has a degree-three neighbour and at least \(4/7\) of the vertices are degree three.
- `jul059`, Erdős Problems #64 discussion comment, 26 July 2026: \(|V_3|\ge2|V_{\ge4}|+1\). The coarse \(2/3\) headline is therefore prior public work.
- Narins–Pokrovskiy–Szabó: prior framework implying \(|E(G)|\le2|V(G)|-3\) for the lexicographically minimal counterexample setting used here.

No novelty or priority claim is made for the excess-sensitive theorem pending specialist literature review.

## Historical and superseded claim

`proofs/minimal-counterexample-plus3.md` proves the weaker bound

\[
|V_3|\ge2|V_{\ge4}|+3.
\]

It remains only as historical provenance. It is mathematically stronger than the public `jul059` \(+1\) bound but is superseded within this repository by \(|A|\ge2b+s+4\). It must not be described as the first public \(2/3\) improvement.

## Local sharpness status

The equality witness cited by the internal audit contains a \(C_8\). Therefore the correct claim is:

```text
CONSTANT_4_SHARP_FOR_LOCAL_INGREDIENTS_ONLY
```

not “sharp for all counterexamples.”

## Supporting computational material

The included older JSON audits concern explicitly bounded graph classes. They do not establish the global conjecture and must not be cited as exhaustive evidence over all finite minimum-degree-three graphs.

The separate two-port theorem from the local theorem-first workspace is not promoted as part of this public release; its evidence status is dual (PASS under the frozen governing-input contract, HOLD under a strict raw-archive replay standard).

## Public provenance decision

The public repository does **not** claim byte identity with the machine-local theorem-first Git bundle. That bundle is not required as a proof premise for the human-checkable structural theorem. The public release instead binds the frozen audited theorem by its SHA-256 and publishes the proof, promotion record, and two internal audit reconstructions.

See [`recovery/THEOREM_FIRST_SEAL_20260806.md`](recovery/THEOREM_FIRST_SEAL_20260806.md) for the reported local seal metadata.

## Publication gates

- [x] Complete human-checkable proof published.
- [x] Public mathematical proof reconciled with the frozen canonical theorem and its audited three-case argument.
- [x] Global open-problem status separated from the structural theorem.
- [x] Markström/Carr attribution corrected.
- [x] `jul059` public \(+1\) comparison recorded; no \(2/3\) priority claim.
- [x] Narins–Pokrovskiy–Szabó edge-bound comparison qualified by \(b\).
- [x] Local sharpness statement calibrated to the actual witness scope.
- [x] AI-use disclosure distinguishes internal AI reconstruction from external review.
- [x] Public bundle boundary explicitly documented; no byte-identity claim.
- [x] Novelty status remains `NOVELTY_NOT_ESTABLISHED`.
