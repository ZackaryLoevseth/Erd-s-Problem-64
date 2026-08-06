# Public recovery summary

## Preservation status

```text
PRESERVATION_COMPLETE
UTC_TIMESTAMP=2026-08-06T00:34:24Z
GIT_BRANCH=checkpoint/erdos64-12h-20260806T003424Z
GIT_COMMIT=34683df66206bd188a9f6a67b91fb94289e6d780
FILE_COUNT=23569
SOURCE_BYTES=4649689073
UNHYDRATED_COUNT=10
ACTIVE_JOB_COUNT=0
VERIFIED_RESTORE=YES
```

## Principal preservation hashes

```text
Git bundle SHA-256:
eafdf9b64c278b1b6bf6926b82a28fca33649f4adbb504dabda77236750cd845

Main workspace archive SHA-256:
a57be426439322d7100bfc82f3ad42422ac3e782606fa47c863576cad239015c

AppleDouble raw supplement SHA-256:
b2ce30266be508fe74e2401ceb54758da07e84958b16b8cf35b0032214cbdf03
```

The full preservation transaction reported matching SHA-256 values for the core external copy, supplements, and seal files, and independently restored the source tree.

## Frozen mathematical state

No complete counterexample and no complete affirmative proof of Erdős Problem #64 had been obtained at the checkpoint. All reconstructed current claims were explicitly scoped as restricted or incomplete rather than as a global solution.

The strongest general mathematical output in this public release is the later Carr-based theorem candidate

\[
|V_3|\ge2|V_{\ge4}|+3,
\]

which was derived during the recovery review and therefore is not part of the frozen checkpoint itself.

## Durable restricted results highlighted by the recovery

- A recovered order-28 connected cubic \(C_4/C_8\)-free census consists of 251 canonical classes, all containing a 16-cycle.
- Connected one-port graphs had been classified through odd order 27, supporting a lower bound of 58 vertices for a cubic counterexample containing a bridge.
- The order-31 one-port near-candidate has minimum degree two and exactly 138 cycles of length 16, so it fails the counterexample contract.
- Numerous lift, triangle-expansion, and gadget families were eliminated within their explicitly defined scopes. These searches do not exhaust all minimum-degree-three graphs.

## Bounded preservation gaps

The Git bundle is a strong code-and-audit recovery product, but it is not the sole authoritative binary archive. The frozen handoff records the following bounded gaps:

- ten shared-state symlinks pointed to unavailable temporary paths;
- the original final `CLAIMS.jsonl` was unavailable and current claims were reconstructed from surviving audits;
- several solver-level claims lacked surviving static proof packets and therefore remain demoted pending regeneration;
- the main tar stream required a small AppleDouble supplement to reproduce six resident byte files exactly.

These gaps do not convert any restricted claim into a global result. They matter primarily for replay strength and evidentiary grading.

## Safe computational successor

The highest-value exact continuation identified at recovery is the rooted-edge order-28 census for the one-port order-29 classification. Residues 0 through 23 were last independently observed complete. The trustworthy restart boundary is therefore:

```text
residues 24 through 255
```

Completing that branch, together with the already audited triangular-port order-26 branch and the one-port classification theorem, would support one-port order 29 and would raise the bridge-containing cubic lower bound from 58 to 62.

## Archive availability

The complete multi-gigabyte archive, sealed index, exact restoration script, and full handoff are intentionally not duplicated in this lightweight GitHub publication branch. Their identities are fixed by the checkpoint and SHA-256 values above.
