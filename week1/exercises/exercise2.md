# Fermat's Little Theorem Proof

Consider the multiplicative group $\mathbb{Z/pZ}^{\times}$, and $a \in \mathbb{Z/pZ}^{\times}$

Let’s define a mapping $f: \mathbb{Z/pZ}^{\times} → \mathbb{Z/pZ}^{\times}$, such that

$$
f(x) = a \cdot x
$$

Then

$$
\begin{align*}
 \mathbb{Z/pZ}^{\times} &= \{1, 2, ..., p-1\} \\
 f(\mathbb{Z/pZ}^{\times}) &= \{a \cdot 1, a \cdot 2, ..., a\cdot (p-1)\}
\end{align*}
$$

**Claim**: $f$ is a bijection

$f$ is onto
- $a^{-1}$ exists in $\bmod p$ and is unique (because $p$ is prime)
- Hence, for any image $a \cdot i$ there exists a pre-image $a^{-1} \cdot a \cdot i = i$

$f$ is one-one
- let $f(i) = f(j)$

$$
\begin{align*}
a \cdot i &\equiv a \cdot j \mod p \\
a^{-1} \cdot a \cdot i &\equiv a^{-1} \cdot a \cdot j \mod p \\
i &\equiv j \mod p \\
\end{align*}
$$

- Therefore, $i \neq j \implies f(i) \neq f(j)$, hence one-one

Hence, $f$ is a bijection

> Note: $f$ is not an automorphism. That is, $f(i \cdot j) \neq f(i) \cdot f(j)$, structure not preserved. $f$ is just a bijection

Since, $f$ is a bijection, it simply permutates the group elements. Meaning the product of all elements must remain the same.

$$
\begin{align*}
\prod_{i\in \mathbb{Z/pZ}^{\times}} i &\equiv \prod_{i\in \mathbb{Z/pZ}^{\times}} f(i)  \mod p\\
\prod_{i\in \mathbb{Z/pZ}^{\times}} i &\equiv \prod_{i\in \mathbb{Z/pZ}^{\times}} a \cdot i \mod p \\
\prod_{i\in \mathbb{Z/pZ}^{\times}} i &\equiv a^{p-1}\prod_{i\in \mathbb{Z/pZ}^{\times}} i \mod p \\
1 &\equiv a^{p-1} \mod p
\end{align*}
$$

> Note: A similar proof can be given for $a^{\varphi(m)} \equiv 1 \mod m$, where $\gcd(a, m) = 1$. Here, we take the group $\mathbb{Z_m}^{\times} = \{x : \gcd(x,m) = 1 \}$ where $x \in \mathbb{Z_m}$