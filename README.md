# Erdős Problem #64 — excess-sensitive structure of minimal counterexamples

> **Global status:** Erdős Problem #64 remains open. This repository does **not** claim a proof of the conjecture or a counterexample.

The problem asks whether every finite simple graph of minimum degree at least three contains a cycle of length \(2^k\) for some integer \(k\ge2\).

## Main structural theorem

Let \(G\) be a counterexample chosen first with minimum order and then, subject to that, minimum size. Define

\[
A=V_3(G),\qquad
B=V_{\ge4}(G),\qquad
b=|B|,\qquad
s=\sum_{v\in B}(d_G(v)-4).
\]

Then

\[
\boxed{|A|\ge 2b+s+4}
\]

or equivalently

\[
\boxed{
|V_3(G)|\ge 4+\sum_{v\in V_{\ge4}(G)}(d_G(v)-2).
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

The proof suppresses the degree-three vertices having two neighbours in \(B\) to a simple auxiliary graph on \(B\). Exact cycle doubling and minimum-order minimality force that auxiliary graph to be 2-degenerate; an exact cut identity retaining the excess \(s\), followed by a parity argument, yields the additional unit in the bound.

**Full proof:** [`proofs/minimal-counterexample-excess-theorem.md`](proofs/minimal-counterexample-excess-theorem.md)

**Promotion record:** [`proofs/excess-theorem-promotion.md`](proofs/excess-theorem-promotion.md)

**Independent internal reconstructions:**
[`audits/excess-theorem-canonical-audit.md`](audits/excess-theorem-canonical-audit.md) and
[`audits/excess-theorem-second-audit.md`](audits/excess-theorem-second-audit.md).

## Prior-work boundary

The theorem is presented without a novelty or priority claim.

- Markström observed that, in a minimal counterexample, the vertices of degree at least four form an independent set; Carr records this observation and proves that every vertex is adjacent to a degree-three vertex, together with the published \(4/7\) degree-three density bound.
- A comment by `jul059` on the Erdős Problems #64 discussion thread dated 26 July 2026 gives the stronger public bound \(|V_3|\ge2|V_{\ge4}|+1\). Thus the coarse “more than \(2/3\)” conclusion is not claimed here as new.
- Narins–Pokrovskiy–Szabó imply \(|E(G)|\le2|V(G)|-3\) for a lexicographically minimal counterexample. The displayed excess-sensitive edge bound improves that inequality when \(b\ge2\), is equal when \(b=1\), and as a uniform formula is weaker when \(b=0\). In the cubic case \(b=0\), the proof separately gives \(|V(G)|\ge8\) and \(|E(G)|=3|V(G)|/2\).

The earlier note [`proofs/minimal-counterexample-plus3.md`](proofs/minimal-counterexample-plus3.md) proves the weaker \(|V_3|\ge2|V_{\ge4}|+3\) bound. It is retained only as historical provenance and is superseded by the excess-sensitive theorem above.

## Verification and claim status

The theorem has a human-checkable proof. During the theorem-first run it passed two structurally independent Codex proof reconstructions and extensive exact falsification checks. Those are **internal AI-assisted checks**, not independent external human review.

Current status:

```text
PROVED_HUMAN_ARGUMENT
GLOBAL_SOLUTION: NO
NOVELTY_NOT_ESTABLISHED
NO_EXTERNAL_SPECIALIST_REVIEW
NO_FORMAL_PROOF_ASSISTANT_VERIFICATION
```

The frozen canonical theorem used by the audits had SHA-256
`387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444`.
The public proof is a publication transcription of that mathematical argument, with updated status and attribution language; the frozen local file itself was deliberately not mutated after audit.

See [`PUBLICATION_STATUS.md`](PUBLICATION_STATUS.md) for the public claim ledger and [`AI_USE.md`](AI_USE.md) for the AI-use disclosure.

## Local sharpness and non-scope

The internal audit supplies an exact graph attaining both \(|A|=2b+s+4\) and \(|E|=2|V|-b-2\) while satisfying the local counting, parity, 2-degeneracy and \(C_4\)-constraints used in the argument. That graph contains a \(C_8\), so it is **not** a counterexample. Accordingly, the constant four is only claimed sharp for those local ingredients, not for the full counterexample class.

The theorem does not prove that \(B=\varnothing\), that every minimal counterexample is cubic, or that no counterexample exists.

## Supporting computational material

The older computational audits in this repository concern explicitly bounded graph classes. They are retained as research provenance and do not establish exhaustive coverage of all finite minimum-degree-three graphs.

- [`reports/data-and-significance-review.md`](reports/data-and-significance-review.md)
- [`audits/n28-complete-census-fresh-audit.json`](audits/n28-complete-census-fresh-audit.json)
- [`audits/one-port-n31-audit.json`](audits/one-port-n31-audit.json)
- [`recovery/RECOVERY_SUMMARY.md`](recovery/RECOVERY_SUMMARY.md)

## References

- T. F. Bloom, “Erdős Problem #64,” Erdős Problems: https://www.erdosproblems.com/64
- Erdős Problems #64 discussion thread: https://www.erdosproblems.com/forum/thread/64?order=oldest
- A. Carr, *Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic*, arXiv:2605.22844.
- L. Narins, A. Pokrovskiy, T. Szabó, *Graphs without proper subgraphs of minimum degree 3 and short cycles*, arXiv:1408.5289.

## Suggested citation

> Zackary Loevseth, “Excess-Sensitive Degree-Three Bounds for Minimal Erdős–Gyárfás Counterexamples,” version 0.2.0, 2026. AI-assisted structural research note; external review and novelty determination pending.
