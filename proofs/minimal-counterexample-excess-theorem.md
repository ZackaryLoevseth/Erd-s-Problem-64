# Excess-sensitive degree-three bounds for minimal Erdős–Gyárfás counterexamples

**Public status:** human-checkable structural theorem; internally reconstructed and clean-clone checked; no external peer review or novelty claim.

## 1. Setup

Let \(G\) be a finite simple counterexample to the Erdős–Gyárfás power-of-two cycle conjecture, chosen with minimum order and, subject to that, minimum size. Thus

\[
\delta(G)\ge3
\]

and \(G\) has no cycle of length \(2^k\) for any integer \(k\ge2\).

Use the following two structural properties proved by Avery Carr:

1. \(B:=V_{\ge4}(G)=\{v:d_G(v)\ge4\}\) is independent.
2. Every vertex of \(G\) has a neighbor of degree exactly three.

Set

\[
A:=V_3(G)=\{v:d_G(v)=3\},\qquad
b:=|B|,
\]

and define the total degree excess above four on \(B\) by

\[
s:=\sum_{v\in B}(d_G(v)-4).
\]

Hence

\[
\sum_{v\in B}d_G(v)=4b+s.
\]

## 2. Theorem

\[
\boxed{|A|\ge2b+s+4.}
\]

Equivalently,

\[
\boxed{
|V_3(G)|
\ge
4+\sum_{v\in V_{\ge4}(G)}(d_G(v)-2).
}
\]

Consequently,

\[
\boxed{3|A|\ge2|V(G)|+s+4}
\]

and

\[
\boxed{|E(G)|\le2|V(G)|-b-2.}
\]

## 3. Proof

For \(i\in\{1,2,3\}\), define

\[
A_i=\{x\in A:d_{G[A]}(x)=i\}.
\]

Carr's second property implies that every \(x\in A\) has at least one neighbor in \(A\). Therefore

\[
A=A_1\sqcup A_2\sqcup A_3.
\]

### 3.1. The case \(b\ge2\)

Every \(x\in A_1\) has exactly two neighbors in \(B\). Construct a graph \(H\) on vertex set \(B\) by replacing each \(x\in A_1\), whose two \(B\)-neighbors are \(u_x,v_x\), with the edge \(u_xv_x\).

The map

\[
x\longmapsto u_xv_x
\]

is a bijection from \(A_1\) to \(E(H)\). It creates no loop because \(G\) is simple. It creates no parallel edges: if distinct \(x,y\in A_1\) had the same two neighbors \(u,v\in B\), then

\[
u-x-v-y-u
\]

would be a \(4\)-cycle in \(G\). Hence \(H\) is simple and

\[
|A_1|=|E(H)|.
\]

We next prove that \(H\) is 2-degenerate. Otherwise \(H\) would contain a subgraph \(J\) with minimum degree at least three. Since \(A\neq\varnothing\),

\[
|V(J)|\le b<|V(G)|.
\]

By the minimum-order choice of \(G\), the graph \(J\) cannot itself be a counterexample. Therefore \(J\) contains a cycle \(C\) of length \(2^k\) for some \(k\ge2\).

Replace every edge \(u_xv_x\) of \(C\) by the two-edge path

\[
u_x-x-v_x
\]

in \(G\). Distinct edges of \(C\) have distinct representatives in \(A_1\), and the vertices of \(C\) are distinct, so the lifted closed walk is a simple cycle. Its length is

\[
2\cdot2^k=2^{k+1},
\]

contradicting the definition of \(G\). Thus \(H\) is 2-degenerate.

A simple 2-degenerate graph on \(b\ge2\) vertices has at most \(2b-3\) edges, so

\[
|A_1|=|E(H)|\le2b-3.
\]

Now count the cut \(E(A,B)\). Since \(B\) is independent,

\[
e(A,B)=\sum_{v\in B}d_G(v)=4b+s.
\]

From the \(A\)-side, a vertex of \(A_i\) has exactly \(3-i\) neighbors in \(B\). Hence

\[
e(A,B)=2|A_1|+|A_2|.
\]

Therefore

\[
|A_2|=4b+s-2|A_1|,
\]

and so

\[
\begin{aligned}
|A|
&=|A_1|+|A_2|+|A_3|\\
&=4b+s-|A_1|+|A_3|\\
&\ge4b+s-(2b-3)\\
&=2b+s+3.
\end{aligned}
\]

The handshaking lemma now supplies the strict improvement. Since

\[
2|E(G)|=3|A|+4b+s,
\]

we have

\[
|A|\equiv s\pmod2.
\]

But

\[
2b+s+3\equiv s+1\pmod2.
\]

Thus the value \(2b+s+3\) is impossible, and

\[
|A|\ge2b+s+4.
\]

### 3.2. The case \(b=1\)

Write \(B=\{z\}\). A vertex in \(A_1\) would require two distinct neighbors in the one-vertex set \(B\), which is impossible in a simple graph. Hence

\[
A_1=\varnothing.
\]

The exact cut count gives

\[
|A_2|=d_G(z)=4+s.
\]

The handshaking lemma in \(G[A]\) shows that \(|A_3|\) is even, because

\[
\sum_{x\in A}d_{G[A]}(x)=2|A_2|+3|A_3|
\]

is even.

If \(|A_3|=0\), then \(G[A]\) is 2-regular and every vertex of \(A\) is adjacent to \(z\). Choose three consecutive vertices \(x,y,w\) on any cycle component of \(G[A]\). Then

\[
z-x-y-w-z
\]

is a \(4\)-cycle, a contradiction. Thus \(|A_3|\) is a positive even integer, so \(|A_3|\ge2\). Therefore

\[
|A|=|A_2|+|A_3|\ge4+s+2=s+6=2b+s+4.
\]

### 3.3. The case \(b=0\)

Then \(G\) is cubic, so \(A=V(G)\). A finite simple graph of minimum degree three has at least four vertices. Hence

\[
|A|\ge4=2b+s+4.
\]

This completes the proof. \(\square\)

## 4. Corollaries

Let \(n=|V(G)|=|A|+b\) and \(m=|E(G)|\).

The main inequality is equivalent to

\[
3|A|\ge2n+s+4.
\]

Also,

\[
2m=3|A|+4b+s.
\]

Using \(|A|\ge2b+s+4\),

\[
2m\le4|A|+2b-4=4n-2b-4,
\]

and therefore

\[
m\le2n-b-2.
\]

In particular,

\[
\frac{2m}{n}\le4-\frac{2b+4}{n}<4.
\]

### 4.1. Maximum average degree

Every proper subgraph \(F\subsetneq G\) is 2-degenerate. Indeed, if some subgraph \(J\subseteq F\) had minimum degree at least three, then \(J\) would contain no dyadic cycle because \(G\) contains none. If \(|V(J)|<|V(G)|\), this contradicts minimum order; if \(V(J)=V(G)\) and \(E(J)\subsetneq E(G)\), it contradicts the minimum-size tie-break.

Thus every proper subgraph on at least two vertices has at most \(2|V|-3\) edges, while the displayed edge bound handles \(G\) itself. Consequently,

\[
\boxed{\operatorname{mad}(G)<4.}
\]

The minimum-size tie-break is used here for proper spanning subgraphs.

### 4.2. Arboricity

Every subgraph \(J\) on at least two vertices satisfies

\[
|E(J)|\le2(|V(J)|-1).
\]

The Nash-Williams arboricity criterion gives

\[
\operatorname{arb}(G)\le2.
\]

Since \(\delta(G)\ge3\), the graph \(G\) is not a forest. Therefore

\[
\boxed{\operatorname{arb}(G)=2.}
\]

## 5. Scope and provenance

This theorem constrains a hypothetical lexicographically minimal counterexample. It does not prove that such a counterexample exists or does not exist, and it does not solve Erdős Problem #64.

The theorem-first run reported:

```text
Local sealed commit:
3e996e35a408ce03dc3152205799e7619f301fe8

Packet manifest:
a34486bfeb3a06b089a75cc90740326d3dc40f6d0f7e629fc156c356af8f8a2e
72/72 entries PASS

Seal manifest:
0124ba1be7ac33a95cba273197ae3b70eea49b64b70db6cdb1b0ce1f1c0f0ce3
```

The proof passed structurally independent Codex reconstructions and clean-clone executable checks in that local sealed workspace. No external human peer review, formal proof-assistant verification, or novelty claim is represented by this note.
