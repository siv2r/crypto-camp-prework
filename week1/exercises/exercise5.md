# ElGamal Encryption over an Arbitrary Finite Abelian Group

Let $(G, \cdot)$ be an arbitrary finite abelian group with order $m$

By fundamental theorem of finite abelian groups says:

$$
G \cong \mathbb{Z_{n_1}} \times \mathbb{Z_{n_2}} \times ... \times \mathbb{Z_{n_k}}
$$

where $\mathbb{Z_{n_i}}$ are prime powered cyclic groups, with generator $g_i$.

Then there exists an isomorphism $a: G → \mathbb{Z_{n_1}} \times \mathbb{Z_{n_2}}  \times ... \times \mathbb{Z_{n_k}}$ which breaks down an $X \in G$:

$a(X) = (x_1, x_2, …, x_k)$

Now we can define ElGamal cipher component-wise for each of these cyclic groups

## Key Generation

$\text{KeyGen}: \mathbb{Z_m} \rightarrow G$

- $f(x) = (g_1^x, g_2^x, ..., g_k^x)$

## Encryption

$\text{Enc}_{X \in G} (m) : G \rightarrow G \times G$

- Here $a(X) = (x_1, x_2, …, x_k)$ and $a(M) = (m_1, m_2, …, m_k)$
- randomly sample $r \xleftarrow{\\$} \mathbb{Z_m}$
- $c_1 = (g_1^r, g_2^r, …, g_k^r)$
- $c_2 = (m_1, m_2, …, m_k) \cdot (x_1^r, x_2^r, …, x_k^r) = (m_1 \cdot x_1^r, m_2 \cdot x_2^r …, m_k \cdot x_k^r)$
- Return $(c_1, c_2)$

## Decryption

$\text{Dec}_{x \in \mathbb{Z_m}} (c_1, c_2) :  G \times G \rightarrow G$

- $c_1^x = (\{g_1^r\}^x, \{g_2^r\}^x, …, \{g_k^r\}^x)$
- Return $c_2 \cdot (c_1^x)^{-1}$
