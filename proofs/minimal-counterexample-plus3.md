# A stronger Carr-based density bound for a minimal Erdős–Gyárfás counterexample

**Status:** independently derived during the recovery review on 2026-08-05 Pacific time. The proof below has not yet received external human verification.

## Assumptions

Let \(G\) be a finite simple counterexample to the Erdős–Gyárfás conjecture, chosen with minimum order and, subject to that, minimum size. Thus \(\delta(G)\ge 3\), and \(G\) has no cycle of length \(2^k\) for any integer \(k\ge 2\).

Use the two structural properties proved by Avery Carr in *Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic* (arXiv:2605.22844):

1. \(B:=V_{\ge 4}=\{v:d_G(v)\ge4\}\) is independent.
2. Every vertex of \(G\) has a neighbor of degree exactly three.

Let \(A:=V_3=\{v:d_G(v)=3\}\).

## Theorem

\[
|A|\ge 2|B|+3.
\]

Consequently,

\[
3|A|\ge 2|V(G)|+3,
\qquad
|A|\ge \left\lceil\frac{2|V(G)|+3}{3}\right\rceil.
\]

This strengthens the previously proposed bound \(|A|\ge2|B|+1\).

## Proof

For \(i\in\{1,2,3\}\), define

\[
A_i=\{a\in A:d_{G[A]}(a)=i\}.
\]

Carr's second property ensures that every \(a\in A\) has at least one neighbor in \(A\), so \(A=A_1\sqcup A_2\sqcup A_3\).

Assume first that \(|B|\ge2\). For each \(x\in A_1\), the vertex \(x\) has exactly two neighbors in \(B\). Form a graph \(H\) on vertex set \(B\) by adding, for each \(x\in A_1\), an edge joining those two neighbors.

The graph \(H\) is simple. A loop is impossible because \(G\) is simple. If two distinct vertices \(x,y\in A_1\) generated the same edge \(uv\), then

\[
u-x-v-y-u
\]

would be a 4-cycle in \(G\), contrary to the counterexample hypothesis.

The graph \(H\) is 2-degenerate. Otherwise, some subgraph \(J\subseteq H\) would have minimum degree at least three. Since

\[
|V(J)|\le |B|<|V(G)|,
\]

minimality of \(G\) implies that \(J\) contains a cycle of length \(2^k\) for some \(k\ge2\). Replace each edge of that cycle by the corresponding two-edge path through its unique vertex of \(A_1\). Because \(H\) is simple and distinct edges have distinct representing vertices, this produces a simple cycle in \(G\) of length

\[
2\cdot2^k=2^{k+1},
\]

which is impossible.

Every simple 2-degenerate graph on \(|B|\ge2\) vertices has at most \(2|B|-3\) edges. Therefore

\[
|A_1|=|E(H)|\le2|B|-3.
\]

Because \(B\) is independent, all edges incident with \(B\) go to \(A\). Counting this cut from the \(A\)-side gives

\[
e(A,B)=2|A_1|+|A_2|,
\]

while counting from the \(B\)-side gives

\[
e(A,B)=\sum_{b\in B}d_G(b)\ge4|B|.
\]

Hence

\[
|A_2|\ge4|B|-2|A_1|.
\]

It follows that

\[
\begin{aligned}
|A|
&=|A_1|+|A_2|+|A_3|\\
&\ge |A_1|+4|B|-2|A_1|\\
&=4|B|-|A_1|\\
&\ge4|B|-(2|B|-3)\\
&=2|B|+3.
\end{aligned}
\]

The small cases are immediate or short:

- If \(|B|=0\), then \(G\) is cubic and \(|A|=|V(G)|\ge4>3\).
- If \(|B|=1\), then \(A_1=\varnothing\), because a vertex of \(A_1\) would need two distinct neighbors in the one-vertex set \(B\). The unique vertex of \(B\) has at least four neighbors, all in \(A_2\), so \(|A|\ge4\). Equality would force \(G[A]\) to be a simple 2-regular graph on four vertices, hence a 4-cycle, impossible. Thus \(|A|\ge5=2|B|+3\).

This proves the theorem. \(\square\)

## Additional structural consequence

When \(|B|\ge2\), the same inequalities give

\[
|A_2|\ge4|B|-2(2|B|-3)=6.
\]

Thus every noncubic minimal counterexample with at least two vertices of degree at least four must contain at least six degree-three vertices having exactly two degree-three neighbors and exactly one high-degree neighbor.

## Scope warning

This is a structural theorem about a hypothetical minimal counterexample. It does not prove that no minimal counterexample exists, and therefore does not solve Erdős Problem #64.
