# Theorem-first local seal — 2026-08-06

This file records provenance supplied by the theorem-first Erdős Problem #64 run. The paths below were machine-local when the run completed and are not represented as public download locations.

## Result

```text
Terminal status: NEW_GENERAL_MECHANISM_PROVED
Global problem: Erdős Problem #64 remains open
```

The sealed theorem states, for a lexicographically minimal counterexample and

\[
A=V_3(G),\quad B=V_{\ge4}(G),\quad b=|B|,\quad
s=\sum_{v\in B}(d_G(v)-4),
\]

that

\[
|A|\ge2b+s+4,
\qquad
3|A|\ge2|V(G)|+s+4,
\qquad
|E(G)|\le2|V(G)|-b-2.
\]

## Local repository and seal

```text
Local repository commit:
3e996e35a408ce03dc3152205799e7619f301fe8

Packet manifest SHA-256:
a34486bfeb3a06b089a75cc90740326d3dc40f6d0f7e629fc156c356af8f8a2e

Packet manifest result:
72/72 PASS

Seal manifest SHA-256:
0124ba1be7ac33a95cba273197ae3b70eea49b64b70db6cdb1b0ce1f1c0f0ce3

Machine-local bundle:
erdos64_theorem_first.bundle
```

Original machine-local bundle path:

```text
/private/tmp/erdos64_theorem_first_seal_20260806/erdos64_theorem_first.bundle
```

Original source files named by the run:

```text
research/theorem_first_20260806/outputs/FINAL_REPORT.md
research/theorem_first_20260806/structural/MINIMAL_COUNTEREXAMPLE_EXCESS_THEOREM.md
research/theorem_first_20260806/REPRODUCE.md
/private/tmp/erdos64_theorem_first_seal_20260806/SEAL_METADATA.json
```

## Reported checks

```text
Clean-clone theorem replay: PASS
Clean-clone post-density replay: PASS
Clean-clone 972-class two-port replay: PASS
Structurally independent Codex proof reconstructions: PASS
```

## Public availability boundary

The public GitHub note transcribes the theorem and its human-checkable proof. This metadata record does not claim that the local bundle has been uploaded to GitHub or that the public transcription is byte-identical to the local canonical proof. That comparison is an explicit pre-merge gate in [`../PUBLICATION_STATUS.md`](../PUBLICATION_STATUS.md).

No external human peer review, novelty determination, or formal proof-assistant verification is implied by the local seal.
