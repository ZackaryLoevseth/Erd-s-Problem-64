# Independent audit of the canonical excess theorem

## Bound target

- File: `research/theorem_first_20260806/structural/MINIMAL_COUNTEREXAMPLE_EXCESS_THEOREM.md`
- Audited SHA256: `387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444`
- Audit verdict: **PASS — no correction required**
- Novelty verdict: **NOT AUDITED / NOVELTY_NOT_ESTABLISHED**

This audit treats all results imported from
`MINIMAL_COUNTEREXAMPLE_TWO_THIRDS_THEOREM.md` as hypotheses already proved
and independently audited: (B) is independent, (a_0=0), and the simple
auxiliary graph (F) on (B) has (|E(F)|=a_1) and is 2-degenerate.

## Reconstruction

For (b\ge2), write

\[
 \delta=2b-3-a_1\ge0.
\]

The cut identity is exact:

\[
 4b+s=\sum_{v\in B}d(v)=e(A,B)=2a_1+a_2.
\]

It follows that

\[
 a_2=s+6+2\delta,
 \qquad
 |A|=2b+s+3+\delta+a_3.
\]

The degree sum of (G[A]) is (a_1+2a_2+3a_3), so (a_1+a_3) is even.
Since (2b-3) is odd, this is equivalent to (\delta+a_3) being odd.
Thus (\delta+a_3\ge1), proving

\[
 |A|\ge2b+s+4.
\]

For (b=1), simplicity forces (a_1=0), and the cut identity gives
(a_2=4+s).  If (S=A_2=N(v)) and (T=A_3), (C_4)-freeness gives both
(\Delta(G[S])\le1) and at most one (S)-neighbour per vertex of (T).
Since every vertex of (S) has degree two in (G[A]),

\[
 |S|\le e(S,T)\le |T|.
\]

Therefore (a_3\ge a_2=4+s) and, more strongly,

\[
 |A|\ge8+2s.
\]

For (b=0), the graph is simple cubic and has even order.  The order-four
case is (K_4), which has a (C_4).  On six vertices the complement is a
simple 2-regular graph, hence (C_6) or (C_3\sqcup C_3); the corresponding
cubic graphs both contain a (C_4).  Hence (|A|=n\ge8).

Finally,

\[
 n=|A|+b,
 \qquad
 2m=3|A|+4b+s,
 \qquad
 4n-2m=|A|-s.
\]

The uniform bound gives (3|A|\ge2n+s+4) and
(4n-2m\ge2b+4), hence (m\le2n-b-2).  All algebra and all exceptional
cases in the bound target are correct.

## Calibration

The theorem is conditional structure for a hypothetical lexicographically
minimal counterexample.  It neither proves that (B=\varnothing) nor resolves
Erdős Problem #64.  The exact counting script and explicit weakened-hypothesis
falsifiers are recorded beside this audit.
