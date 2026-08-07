# Excess-sensitive degree-three bounds for a minimal counterexample

**Public status:** `PROVED_HUMAN_ARGUMENT`  
**Global solution:** `NO`  
**Novelty:** `NOVELTY_NOT_ESTABLISHED`  
**External specialist review:** none claimed

The frozen canonical theorem audited during the theorem-first run has SHA-256
`387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444`.
This public note preserves its mathematical argument while making the current status and prior-work boundary explicit.

## Statement

Let \(G\) be a counterexample to the Erdős–Gyárfás conjecture chosen first with minimum order and then, subject to that, minimum size. Put

\[
A=V_3(G),\qquad B=V_{\ge4}(G),\qquad b=|B|,
\]

and let the excess degree above four on \(B\) be

\[
s=\sum_{v\in B}(d_G(v)-4).
\]

Then

\[
\boxed{|A|\ge 2b+s+4.}
\]

Consequently, writing \(n=|V(G)|\) and \(m=|E(G)|\),

\[
\boxed{3|A|\ge2n+s+4}
\qquad\text{and}\qquad
\boxed{m\le2n-b-2.}
\]

For \(b\ge2\), the proof also gives \(a_2\ge s+6\). For \(b=1\), it gives \(a_2=4+s\), \(a_3\ge4+s\), and \(|A|\ge8+2s\).

## Proof

Every proper subgraph of \(G\) has minimum degree at most two. Otherwise it would itself be a dyadic-cycle-free graph of minimum degree at least three and would contradict the minimum-order choice, or, if spanning, the secondary minimum-size choice.

Applying this to \(G-v\) shows that every vertex of \(G\) has a neighbour of degree exactly three. Also \(B\) is independent: deleting an edge with both endpoints in \(B\) preserves minimum degree at least three and cannot create a cycle, contradicting the minimum-size choice.

For \(0\le i\le3\), let

\[
A_i=\{a\in A:d_{G[A]}(a)=i\},\qquad a_i=|A_i|.
\]

The degree-three-neighbour property implies \(a_0=0\).

Construct an auxiliary graph \(F\) on vertex set \(B\). Each vertex \(a\in A_1\) has exactly two neighbours in \(B\); add to \(F\) the edge between those two neighbours. The endpoints are distinct because \(G\) is simple. Two different vertices of \(A_1\) cannot define the same edge: if they did, the two vertices of \(A_1\) and their two common neighbours in \(B\) would form a \(C_4\) in \(G\). Hence \(F\) is finite and simple and

\[
|E(F)|=a_1.
\]

A simple cycle of length \(r\) in \(F\) lifts, by replacing each auxiliary edge with its distinct length-two path through the corresponding vertex of \(A_1\), to a simple cycle of length \(2r\) in \(G\). Thus a cycle of length \(2^k\), \(k\ge2\), in \(F\) would give a dyadic cycle in \(G\).

Consequently \(F\) is 2-degenerate. If some subgraph \(J\subseteq F\) had minimum degree at least three, then \(J\) would itself be a finite simple dyadic-cycle-free graph of minimum degree at least three. Since the degree-three-neighbour property makes \(A\neq\varnothing\),

\[
|V(J)|\le b<|V(G)|,
\]

contradicting the minimum-order choice of \(G\).

### Case \(b\ge2\)

A simple 2-degenerate graph on \(b\ge2\) vertices has at most \(2b-3\) edges, so

\[
a_1\le2b-3.
\]

Write

\[
\delta=2b-3-a_1\ge0.
\]

Since \(B\) is independent, counting the edges between \(A\) and \(B\) at their two sides gives the exact identity

\[
4b+s=e(A,B)=2a_1+a_2.
\]

Substituting \(a_1=2b-3-\delta\) yields

\[
a_2=s+6+2\delta
\]

and

\[
|A|=a_1+a_2+a_3=2b+s+3+\delta+a_3.
\]

The handshaking lemma in \(G[A]\) says that

\[
a_1+2a_2+3a_3
\]

is even, hence \(a_1+a_3\) is even. Since \(a_1=2b-3-\delta\) and \(2b-3\) is odd, \(\delta+a_3\) is odd. It is a nonnegative integer, so \(\delta+a_3\ge1\). Therefore

\[
|A|\ge2b+s+4.
\]

This case also gives \(a_2\ge s+6\).

### Case \(b=1\)

An \(A_1\)-vertex would need two distinct neighbours in \(B\), so \(a_1=0\). The edge-cut identity gives

\[
a_2=4+s.
\]

Let \(v\) be the unique vertex of \(B\), put \(S=A_2=N_G(v)\), and put \(T=A_3\). Every vertex of \(S\) has degree two in \(G[A]\). A vertex of \(S\) has at most one neighbour in \(S\), since two such neighbours together with \(v\) would form a \(C_4\). It therefore has at least one neighbour in \(T\), and hence

\[
e(S,T)\ge|S|.
\]

Conversely, a vertex of \(T\) has at most one neighbour in \(S\), because two such neighbours together with \(v\) would again form a \(C_4\). Thus

\[
e(S,T)\le|T|,
\]

so

\[
a_3=|T|\ge|S|=a_2=4+s.
\]

Therefore

\[
|A|=a_2+a_3\ge8+2s\ge2b+s+4.
\]

### Case \(b=0\)

The graph is cubic. Its order is even. The only simple cubic graph on four vertices is \(K_4\), which has a \(C_4\). On six vertices the complement is a simple 2-regular graph, hence is either a six-cycle or two disjoint triangles; the corresponding cubic graphs both contain a \(C_4\). Therefore

\[
|A|=|V(G)|\ge8>2b+s+4.
\]

The three cases prove the first boxed inequality.

Finally, since \(n=|A|+b\), rearrangement gives

\[
3|A|\ge2n+s+4.
\]

The degree sum is

\[
2m=3|A|+4b+s,
\]

and hence

\[
4n-2m=|A|-s\ge2b+4.
\]

Dividing by two gives

\[
m\le2n-b-2.
\]

\(\square\)

## Prior-work and comparison boundary

The proof rederives the two minimality facts it uses, but they have prior provenance. Carr records Markström's observation that the degree-at-least-four vertices form an independent set, and Carr proves that every vertex of a minimal counterexample is adjacent to a degree-three vertex, as well as the published \(4/7\) density bound.

A comment by `jul059` on the Erdős Problems #64 discussion thread dated 26 July 2026 gives \(|V_3|\ge2|V_{\ge4}|+1\). Therefore the coarse “strictly more than two thirds” consequence is not claimed here as new.

Narins–Pokrovskiy–Szabó imply the prior-art bound

\[
m\le2n-3
\]

for a lexicographically minimal counterexample. The excess-sensitive bound \(m\le2n-b-2\) is strictly stronger when \(b\ge2\), equal when \(b=1\), and as a uniform formula weaker when \(b=0\). The cubic case is handled separately above.

No literature-priority claim is made for the exact excess-sensitive inequality or its auxiliary-graph/parity mechanism.

## Local sharpness and non-scope

An exact internal witness attains \(|A|=2b+s+4\) and \(m=2n-b-2\) while satisfying the local counting, parity, 2-degeneracy and \(C_4\)-constraints used above. It contains a \(C_8\), so it is not a counterexample. Thus the constant four is claimed sharp only for those local ingredients, not for the full counterexample class.

The theorem does not prove that \(B=\varnothing\), that a minimal counterexample is cubic, or that Erdős Problem #64 is true or false.

## Verification provenance

- Frozen canonical theorem SHA-256: `387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444`.
- Internal canonical audit: [`../audits/excess-theorem-canonical-audit.md`](../audits/excess-theorem-canonical-audit.md), verdict `PASS — no correction required`.
- Second structurally independent internal reconstruction: [`../audits/excess-theorem-second-audit.md`](../audits/excess-theorem-second-audit.md), verdict `PASS`.
- Promotion record: [`excess-theorem-promotion.md`](excess-theorem-promotion.md).

These checks are not external peer review or formal proof-assistant verification.
