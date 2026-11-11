# Mathematics: choose depth, preserve exactness

Use these topic bands as orientation, not a claim of curriculum alignment.

| Level | Useful representations | Verification |
| --- | --- | --- |
| Grade 5–6 | equal-part fraction bars, number line, units table | same whole; equivalent fractions; division by zero excluded |
| Grade 7–10 | percentage tables, equations, coordinate plots, geometric sketches | substitute results; units; equation versus expression |
| Upper secondary | derivatives, integrals, vectors, probability trees | domains; endpoint behavior; dimensions; total probability |
| Introductory university | complex plane, matrices, linear maps, limits, proofs | original-equation residual; rank; quantifiers; counterexamples |

## Fraction example

For 3/4 + 1/6 choose a common unit (twelfths): 9/12 + 2/12 = 11/12. Two separate wholes are not one additive bar. In hint mode suggest finding equal-sized parts without giving 12 or the result unless requested. The SVG helper renders a single nonnegative fraction, not the derivation of addition.

## Algebra and graphs

State the real/complex domain. For x²−4x+3=0 the factorization (x−1)(x−3) and vertex (2,−1) provide independent checks. A graph suggests roots; substitution proves these exact candidates. The quadratic helper uses floating-point arithmetic and rejects a=0; solve the linear case separately. A finite plot cannot establish global behavior or a limit.

## University examples

- For z³=8i, use modulus 2 and angles π/6+2πk/3 for k=0,1,2. The three roots are √3+i, −√3+i, −2i. Cube each candidate and account for all three distinct roots.
- For |z−i|<|z+1|, put z=x+iy and square nonnegative distances. The result is y>−x; the boundary is excluded. Check z=i and z=−1 to orient the half-plane.
- For A=[[2,1],[1,2]], eigenpairs (3,(1,1)) and (1,(1,−1)) satisfy Av=λv. Do not call every vector an eigenvector; zero is excluded.
- For lim(x→0) sin(x)/x=1, specify radians and x≠0. Use a permitted proof method; do not use L'Hôpital if derivatives have not been introduced.

For proofs, separate exploration from proof, state assumptions, and check logical directions. For solving inequalities, mark whether endpoints are included. Never turn a numerical observation into a proof.
