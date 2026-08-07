# Promotion record: excess-degree theorem

Promotion time: 2026-08-06T09:50:54Z

Status: **PROVED_HUMAN_ARGUMENT**  
Global solution: **NO**  
Novelty: `NOVELTY_NOT_ESTABLISHED`

## Exact promoted statement

Let \(G\) be a counterexample to Erdős Problem #64 chosen first with
minimum order and then with minimum size. Set

\[
A=V_3(G),\qquad B=V_{\ge4}(G),\qquad b=|B|,
\qquad s=\sum_{v\in B}(d_G(v)-4).
\]

Then

\[
|A|\ge 2b+s+4,
\qquad 3|A|\ge2|V(G)|+s+4,
\qquad |E(G)|\le2|V(G)|-b-2.
\]

For \(b\ge2\), the proof also gives \(a_2\ge s+6\). For \(b=1\),
it gives \(a_2=4+s\), \(a_3\ge4+s\), and
\(|A|\ge8+2s\).

## Binding

- Frozen proof target:
  `MINIMAL_COUNTEREXAMPLE_EXCESS_THEOREM.md`, SHA-256
  `387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444`.
- Structurally independent Codex proof reconstruction (not an external human
  or research-group review):
  `../audits/AUDIT_OF_CANONICAL_EXCESS_THEOREM.md`, SHA-256
  `e6f8f5463f2ad7d6c1b01d978d878c08fbe00ca0cd219c352893fdce03aa3f0b`;
  verdict `PASS — no correction required`.
- Second structurally independent Codex proof-and-certificate reconstruction:
  `../audits/DENSITY_THEOREM_AUDIT_SECOND.md`, with executable
  `../audits/density_certificate_audit.py`, SHA-256
  `6a1b9051748ea4a0c410c734d2560e6cf5a4a4bfd12612474858138a1fb67d0a`.
  It checked 93,637 graph instances, 13,597 auxiliary graphs, 5,346
  integer tuples, and 5,036 exact auxiliary-cycle lifts; verdict `PASS`.
- Independent executable falsifier/checker:
  `post_density_falsifier.py`, SHA-256
  `86587ebd89ad662068ccaf8d57803e211aaba5ee35c35f27eac7746a837b349e`.
- Frozen checker result:
  `POST_DENSITY_FALSIFIER_RESULTS.json`, SHA-256
  `7d5f7df7c621fc4470d1477a73ca460f4419b40959641d18f960046b6fcf5e47`.
  A clean temporary-directory replay was byte-identical and checked
  4,756,950 admissible integer tuples with no violation.
- Primary-source boundary:
  `../sources/NPS_SOURCE_AUDIT.md` and
  `../sources/EXCESS_THEOREM_COLLISION_VERDICT.json`.

The canonical proof file retains its pre-audit “theorem candidate” header so
that every audit remains bound to the exact bytes it reviewed. This separate
integrator record, not a mutation of the audited target, performs promotion.

## Scope and non-scope

This is a conditional structural theorem about every hypothetical
lexicographically minimal counterexample. It does not prove that \(B\) is
empty, that a minimal counterexample is cubic, or that Erdős Problem #64 is
true or false. The weaker bound \(|E(G)|\le2|V(G)|-3\) and the conclusion
that the average degree is below four are prior-art consequences of
Narins–Pokrovskiy–Szabó; they are not claimed as new.

The exact 16-vertex equality witness shows that the count, parity,
2-degeneracy, and local \(C_4\)-constraints alone cannot improve the uniform
constant four. The exact 11-vertex closure obstruction shows that naive
deletion-and-pairing at a degree-four vertex does not preserve dyadic cycle
lengths. Both graphs contain dyadic cycles and are not counterexamples.
