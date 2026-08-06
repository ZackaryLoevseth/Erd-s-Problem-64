# AI assistance, authorship, and claim status

## Human direction and authorship

**Zackary Loevseth** directed the research target, long-horizon execution protocol, preservation requirements, recovery decisions, evaluation criteria, and public-release decision.

## AI assistance

OpenAI systems, including ChatGPT/GPT-5.6 Pro, substantially assisted with:

- reviewing and reconstructing the recovered workspace;
- checking claim boundaries and distinguishing global from restricted results;
- selected independent computational audits represented by the included JSON outputs;
- deriving and drafting the proposed bound
  \(|V_3|\ge2|V_{\ge4}|+3\) from Carr's published structural lemmas;
- preparing the data-significance review and this public release.

The larger research process also used other AI systems. The preserved handoff contains the detailed provenance available at the recovery checkpoint.

## Claim-status ledger

### Open problem

Erdős Problem #64 is not solved by this release.

### Theorem candidate

The note `proofs/minimal-counterexample-plus3.md` gives a complete proof argument for

\[
|V_3|\ge2|V_{\ge4}|+3
\]

in a hypothetical minimum-order counterexample, conditional on the two stated structural lemmas of Avery Carr.

This argument has **not** received external human verification. Until it does, it should be cited as an unverified theorem candidate or research note rather than as an established theorem.

### Restricted computational result

The order-28 JSON audit verifies the recovered class union and exact cycle properties of the stated 251 cubic isomorphism classes, subject to the source-boundary qualification written into the audit itself. It is not a proof of the full conjecture.

### Rejected candidate

The order-31 one-port graph fails the counterexample contract because its minimum degree is two and it contains 138 cycles of length 16.

## Reuse and review expectation

Readers should independently check the mathematical proof and should preserve the stated distinction between:

- a human-checkable structural argument;
- a complete audit of a defined recovered class;
- upstream generator-completeness claims that were not rerun from raw states; and
- broad claims about all finite graphs, which are not made here.
