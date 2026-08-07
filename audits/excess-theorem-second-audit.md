# Independent audit of the minimal-counterexample excess theorem

Canonical target SHA-256: `387ffe0f087e8bf3a66df20d5d267a798f76f5a079e39fcfc70787878b400444`

Verdict: **proof logic passes; no theorem promotion is blocked by a mathematical gap; novelty remains unestablished.** This is conditional structure for a hypothetical minimal counterexample, not a resolution of Erdős Problem 64.

## Minimality facts

For every tested minimum-degree-three graph, the auditor independently verified:

- `min degree(G-v)<=2` for every vertex `v` if and only if every vertex has a degree-three neighbour;
- `min degree(G-e)<=2` for every edge `e` if and only if no edge joins two vertices of degree at least four.

Thus lexicographic minimality supplies the neighbour property and independence of `B`. The neighbour property gives `a0=0`.

## Auxiliary graph `F`

Each `A1` vertex has exactly two distinct `B` neighbours. It defines one auxiliary edge and no loop. If two `A1` vertices define the same edge, their two middle vertices and two endpoints form an explicit `C4`; therefore `C4`-freeness makes `F` simple and `|E(F)|=a1`.

For every simple cycle `b0...b(r-1)b0` in `F`, the unique middle vertices of its distinct auxiliary edges are also distinct. Alternating the `B` vertices and these middle vertices gives a simple cycle of exact length `2r` in `G`. The auditor constructed and checked 5,036 such lifts edge by edge. Hence a dyadic cycle in `F` would produce a dyadic cycle in `G`.

If `F` were not 2-degenerate, its nonempty 3-core would be a finite simple dyadic-free graph of minimum degree at least three. Its order is at most `b<n`, because the neighbour property makes `A` nonempty. It would therefore be a smaller counterexample, contradicting minimum order. This implication uses both exact cycle doubling and minimum-order choice.

All 13,597 unlabeled simple graphs of orders 2 through 8 were checked independently: every 2-degenerate graph obeyed `|E(F)|<=2b-3`, and equality occurred at every tested order. The deletion-order proof is exact: the last vertex contributes zero later edges, the penultimate contributes at most one by simplicity, and every earlier vertex contributes at most two.

## Case `b>=2`

With `delta=2b-3-a1`, exact edge counting gives

```text
a2 = s+6+2delta,
|A| = 2b+s+3+delta+a3.
```

Handshaking in `G[A]` makes `a1+a3` even. Since `a1=2b-3-delta`, the integer `delta+a3` is odd and nonnegative, hence at least one. Therefore

```text
a2 >= s+6,
|A| >= 2b+s+4.
```

The auditor checked 5,346 admissible integer tuples and 737 actual bounded graph instances. Exact local witnesses show the constants cannot be improved from these hypotheses alone:

- ```I?qa``eeO``` attains `|A|=2b+s+4` and `m=2n-b-2`;
- `K?AB?rOi@kHg` attains `a2=s+6`.

Both witnesses contain a dyadic cycle, so they do not challenge the theorem.

## Case `b=1`

An `A1` vertex would need two distinct neighbours in the singleton `B`, so `a1=0`; edge counting gives `a2=4+s`. Put `S=A2=N(v)` and `T=A3`.

Every `S` vertex has two neighbours in `G[A]`. It has at most one neighbour in `S`, because two such neighbours with `v` form a `C4`; hence it has a neighbour in `T` and `e(S,T)>=|S|`. Every `T` vertex has at most one neighbour in `S` by the same square obstruction, so `e(S,T)<=|T|`. Therefore

```text
a3>=a2=4+s,
|A|>=8+2s>=2b+s+4.
```

The exact constructed control ``J{d?`?EBOF?`` is connected, simple, `C4`-free, and has `(a0,a1,a2,a3)=(0,0,4,6)`, exercising every part of the double count. It contains `C8` and is not a counterexample.

The NPS equality theorem independently gives the weaker prior-art consequence `a3>=2`; the canonical proof does not depend on it.

## Case `b=0`

The graph is cubic and has even order. Direct tiny enumeration confirms that the unique cubic order-4 class and both cubic order-6 classes contain `C4`; this matches the human `K4`/complement classification. Hence a dyadic-free graph has order at least eight, which is more than the required four. The same audit additionally found that all five cubic order-8 classes contain `C4`, an unused strengthening.

## Final identities

From `n=|A|+b` and `2m=3|A|+4b+s`, the verified bound gives

```text
3|A| >= 2n+s+4,
4n-2m = |A|-s >= 2b+4,
m <= 2n-b-2.
```

## Weakened-hypothesis falsifiers

- Without `C4`-freeness, `E^rG` produces four parallel auxiliary edges and violates both density conclusions.
- Without the degree-three-neighbour property, a 21-vertex linear-incidence graph has `a0=12`, simple empty `F`, and violates both conclusions.
- Without independence of `B`, ``J?`@dROFbI?`` keeps the other local inputs but violates both conclusions.
- Without the dyadic/minimality step forcing `F` to be 2-degenerate, the 15-vertex `K5`-suppression witness has `F=K5`; its `C4`s lift exactly to `C8`s and both density conclusions fail.

These examples expose the necessary hypotheses; none satisfies the full minimal dyadic-free-counterexample premises.

## Computational scope

The principal bounded census checked 93,637 graphs: every connected simple minimum-degree-at-least-three graph at orders 4–9, plus every connected simple `C4`-free minimum-degree-at-least-three graph at orders 10–14. This is a lemma falsifier, not a broad counterexample search.
