# Publication status and claim ledger

## Global status

```text
ERDOS_64_GLOBAL_STATUS_OPEN
```

This repository does not contain a proof of the Erdős–Gyárfás conjecture and does not contain a counterexample.

## Established in the public theorem note

For a finite simple counterexample \(G\) chosen with minimum order and, subject to that, minimum size, define

\[
A=V_3(G),\quad
B=V_{\ge4}(G),\quad
b=|B|,\quad
s=\sum_{v\in B}(d_G(v)-4).
\]

Using Carr's published structural lemmas, the public proof establishes

\[
|A|\ge2b+s+4
=
4+\sum_{v\in B}(d_G(v)-2),
\]

and consequently

\[
3|A|\ge2|V(G)|+s+4,
\qquad
|E(G)|\le2|V(G)|-b-2.
\]

With the order-then-size minimality convention, it also establishes

\[
\operatorname{mad}(G)<4,
\qquad
\operatorname{arb}(G)=2.
\]

## Verification status

```text
MATHEMATICAL_THEOREM_INTERNALLY_RECONSTRUCTED
HUMAN_CHECKABLE_PROOF_PUBLISHED
LOCAL_CLEAN_CLONE_CHECKS_REPORTED_PASS
NOVELTY_NOT_ESTABLISHED
NO_EXTERNAL_PEER_REVIEW
NO_FORMAL_PROOF_ASSISTANT_VERIFICATION
```

The local theorem-first seal is recorded in
[`recovery/THEOREM_FIRST_SEAL_20260806.md`](recovery/THEOREM_FIRST_SEAL_20260806.md).
The public repository does not yet contain the machine-local Git bundle named in that record.

## Superseded claim

The earlier note

```text
proofs/minimal-counterexample-plus3.md
```

proved the weaker bound

\[
|V_3|\ge2|V_{\ge4}|+3.
\]

It remains in the repository as historical provenance but is superseded by the excess-sensitive \(+4\) theorem.

## Supporting computational material

The included JSON audits concern explicitly bounded graph classes. They do not establish the global conjecture and must not be cited as exhaustive evidence over all finite minimum-degree-three graphs.

## Publication merge gates

Before this branch is squash-merged into `main`:

- [x] Publish a complete human-checkable proof.
- [x] State the order-then-size minimality convention consistently.
- [x] Separate the global open problem from the structural theorem.
- [x] Record the local sealed commit and manifest hashes.
- [x] Update citation and AI-use disclosures.
- [x] Add an integrity-manifest CI check for the public packet.
- [ ] Compare the public transcription byte-for-byte or line-for-line with the canonical local proof at commit `3e996e35a408ce03dc3152205799e7619f301fe8`.
- [ ] Import the exact sealed bundle or explicitly decide to publish it as a separate release asset.
- [ ] Obtain external specialist review of correctness and priority before making any novelty claim.

The intended final action is a **squash merge through GitHub**, so the public `main` publication commit is GitHub-created and displays a verified signature.
