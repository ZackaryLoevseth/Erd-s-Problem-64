# Theorem-first local seal — 2026-08-06

This file records provenance reported by the theorem-first Erdős Problem #64 run. The paths below were machine-local when the run completed and are not represented as public download locations.

## Result

```text
Terminal status: NEW_GENERAL_MECHANISM_PROVED
Global problem: Erdős Problem #64 remains open
Novelty: NOVELTY_NOT_ESTABLISHED
```

For a lexicographically minimal counterexample and

\[
A=V_3(G),\quad B=V_{\ge4}(G),\quad b=|B|,\quad
s=\sum_{v\in B}(d_G(v)-4),
\]

the sealed theorem states

\[
|A|\ge2b+s+4,
\qquad
3|A|\ge2|V(G)|+s+4,
\qquad
|E(G)|\le2|V(G)|-b-2.
\]

## Frozen canonical proof binding

The canonical theorem file audited during the run is

```text
research/theorem_first_20260806/structural/MINIMAL_COUNTEREXAMPLE_EXCESS_THEOREM.md
SHA-256: 387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444
```

The public theorem note is a publication transcription of that mathematical argument with updated status and attribution language. The frozen audited file was deliberately not mutated after audit.

## Reported local repository and seal metadata

```text
Local repository commit reported by the theorem-first release:
3e996e35a408ce03dc3152205799e7619f301fe8

Packet manifest SHA-256:
a34486bfeb3a06b089a75cc90740326d3dc40f6d0f7e629fc156c356af8f8a2e

Packet manifest result:
72/72 PASS

Seal manifest SHA-256:
0124ba1be7ac33a95cba273197ae3b70eea49b64b70db6cdb1b0ce1f1c0f0ce3

Machine-local bundle name:
erdos64_theorem_first.bundle
```

Original machine-local bundle path reported by the run:

```text
/private/tmp/erdos64_theorem_first_seal_20260806/erdos64_theorem_first.bundle
```

## Reported checks

```text
Clean-clone theorem replay: PASS
Clean-clone post-density replay: PASS
Clean-clone 972-class two-port replay: PASS
Structurally independent Codex proof reconstructions: PASS
```

## Public availability boundary

The machine-local theorem-first Git bundle is not part of this GitHub publication. The human theorem does not depend on that bundle for validity. The public release therefore does not claim byte identity to the bundle; instead it publishes the human-checkable proof, the promotion record, two internal proof reconstructions, and the frozen canonical proof SHA-256.

No external human peer review, novelty determination, or formal proof-assistant verification is implied by the local seal.
