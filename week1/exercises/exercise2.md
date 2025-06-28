# Fermat's Little Theorem Proof

Consider the multiplicative group $\mathbb{Z/pZ}^*$, and $a \in \mathbb{Z/pZ}^*$

Let’s define a mapping $f: \mathbb{Z/pZ}^* → \mathbb{Z/pZ}^*$, such that

$$
f(x) = a \cdot x
$$

Then

$$
\begin{align*}
 \mathbb{Z/pZ}^* &= \{1, 2, ..., p-1\} \\
 f(\mathbb{Z/pZ}^*) &= \{a \cdot 1, a \cdot 2, ..., a\cdot (p-1)\}
\end{align*}
$$

**Claim**: $f$ is a bijection

1. $f$ is onto
    - $a^{-1}$ exists in $\bmod p$ and is unique (because $p$ is prime)
    - Hence, for any image $a \cdot i$ there exists a pre-image $a^{-1} \cdot a \cdot i = i$
2. $f$ is one-one
    - let $f(i) = f(j)$
    $$
    \begin{align*}
    a \cdot i &\equiv a \cdot j \mod p \\
    a^{-1} \cdot a \cdot i &\equiv a^{-1} \cdot a \cdot j \mod p \\
    i &\equiv j \mod p \\
    \end{align*}
    $$
    - Therefore, $i \neq j \implies f(i) \neq f(j)$, hence one-one

> Note: $f$ is not an automorphism. That is, $f(i \cdot j) \neq f(i) \cdot f(j)$, structure not preserved. $f$ is just a bijection

Since, $f$ is a bijection, it simply permutates the group elements. Meaning the product of all elements must remain the same.

$$
\begin{align*}
\prod_{i\in \mathbb{Z/pZ}^*} i &\equiv \prod_{i\in \mathbb{Z/pZ}^*} f(i)  \mod p\\
\prod_{i\in \mathbb{Z/pZ}^*} i &\equiv \prod_{i\in \mathbb{Z/pZ}^*} a \cdot i \mod p \\
\prod_{i\in \mathbb{Z/pZ}^*} i &\equiv a^{p-1}\prod_{i\in \mathbb{Z/pZ}^*} i \mod p \\
1 &\equiv a^{p-1} \mod p
\end{align*}
$$