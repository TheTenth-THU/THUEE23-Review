## Markov 链的定义

**Markov 链**是描述**离散时间、离散状态**的随机过程的模型，是具有 [[#Markov 性]]的离散时间离散状态随机过程。

### Markov 性

对一个随机过程 $\left\{ X_{k} \right\}_{k=0}^{\infty}$，**Markov 性**表述为 $\forall n$
$$
P \left\{ X_{n} = x_{n} \mid X_{n-1} = x_{n-1}, \cdots , X_{1} = x_{1} , X_{0} = x_{0} \right\} = P \left\{ X_{n} = x_{n} \mid X_{n-1} = x_{n-1} \right\}
$$

若称 $X_{n-1}$ 为**现在**（$B$），之前的状态为**过去**（$A$），之后的状态为**未来**（$C$），则 **Markov 性**表明了条件之间的独立性
$$
P(CA \mid B) = P(C \mid B) P(A \mid B)
$$
「过去」与「未来」之间的联系，只有通过「现在」建立起来。如果掌握了现在，那么过去的信息对于推测未来不起作用。

「过去」和「未来」均可以复杂化，即
+ 将未来 $X_{n}$ **泛化为集合 $A$**，有
$$
\begin{align} 
&P \left\{ X_{n} \in A \mid X_{n-1} = x_{n-1}, \cdots , X_{1} = x_{1} , X_{0} = x_{0}  \right\}  \\
&= \sum\limits_{x_{n} \in A} P \left\{ X_{n} = x_{n} \mid X_{n-1} = x_{n-1}, \cdots , X_{1} = x_{1} , X_{0} = x_{0} \right\}  \\
&= \sum\limits_{x_{n} \in A} P \left\{ X_{n} = x_{n} \mid X_{n-1} = x_{n-1} \right\} = P \left\{ X_{n} \in A \mid X_{n-1} = x_{n-1} \right\}
\end{align}
$$
仍然保持 Markov 性；
+ 将过去 $(X_{n-2}, \cdots, X_{0})$ **泛化为集合 $B$**，有
$$
\begin{align} 
&P \{ X_{n} = x_{n}, (X_{n-2}, \cdots, X_{0}) \in B \mid X_{n-1} = x_{n-1} \} \\
&= \sum\limits_{\{x_{k}\}_{k=0}^{n-2} \in B} P \{ \underbrace{ X_{n} = x_{n} }_{ \text{「未来」} }, \underbrace{ (X_{n-2}, \cdots, X_{0}) \in (x_{n-2}, \cdots, x_{0}) }_{ \text{「过去」} } \mid \underbrace{ X_{n-1} = x_{n-1} }_{ \text{「现在」} } \} \\
&= \sum\limits_{\{x_{k}\}_{k=0}^{n-2} \in B} P \{ \underbrace{ X_{n} = x_{n} }_{ \text{「未来」} } \mid \underbrace{ X_{n-1} = x_{n-1} }_{ \text{「现在」} } \} \\
&\hspace{4.5em} \cdot P \{ \underbrace{ (X_{n-2}, \cdots, X_{0}) \in (x_{n-2}, \cdots, x_{0}) }_{ \text{「过去」} } \mid \underbrace{ X_{n-1} = x_{n-1} }_{ \text{「现在」} } \} \\
&= P \{ X_{n} = x_{n} \mid X_{n-1} = x_{n-1} \} \cdot P \{ (X_{n-2}, \cdots, X_{0}) \in B \mid X_{n-1} = x_{n-1} \}
\end{align}
$$
即
$$
\begin{align}
&P \{ X_{n} = x_{n} \mid (X_{n-2}, \cdots, X_{0}) \in B, X_{n-1} = x_{n-1} \} \\
&= \dfrac{P \{ X_{n} = x_{n}, (X_{n-2}, \cdots, X_{0}) \in B \mid X_{n-1} = x_{n-1} \}}{P \{ (X_{n-2}, \cdots, X_{0}) \in B \mid X_{n-1} = x_{n-1} \}} 
= P \{ X_{n} = x_{n} \mid X_{n-1} = x_{n-1} \}
\end{align}
$$
仍然保持 Markov 性。

但是，「现在」的复杂化将可能破坏 Markov 性。

### Markov 链的迭代表示

我们考虑 Markov 链的 $n$ 维联合概率分布，有
$$
\begin{align}
P(X_{n}, X_{n-1}, \cdots, X_{0}) &= P(X_{n} \mid X_{n-1}, \cdots, X_{0}) \cdot P(X_{n-1}, \cdots, X_{0}) \\
&= P(X_{n} \mid X_{n-1}) \cdot P(X_{n-1}, \cdots, X_{0}) \\
&= \cdots  \\
&= P(X_{n} \mid X_{n-1})  P(X_{n-1} \mid X_{n-2} ) \cdots P(X_{1} \mid X_{0}) P(X_{0})
\end{align}
$$
即，其决定于一组条件概率
$$
P_{i,j} (m, n) = P \left\{ X_{n} = x_{j} \mid X_{m} = x_{i} \right\}
$$
称为 $n - m$ 步**转移概率 (transition probability)**。

#### 平稳转移概率假设

一般地，一个 $n$ 步的转移概率 $P_{i,j}(m, m+n)$ 与其发生的时刻 $m$ 有关。如果其**与发生时刻无关**，即
$$
\forall m, \qquad
P_{i,j}(m, m+n) \equiv P_{i, j}(n)
$$
则称之为**平稳 (stationary)** Markov 链。

在此假设下，特定步数 $n$ 的转移概率只依赖于转移的**起点状态 $i$** 和**终点状态 $j$**，计算 $P_{i,j}^{(n)}$ 只需对起点与终点之间的每一条路径的概率求和即可，尽管也不是非常简便。

#### Chapman-Kolmogorov 方程

> [!theorem] Chapman-Kolmogorov 方程
> 设 Markov 链的状态空间为 $E$，$i,j,k \in E$，对时刻 $r, s, t$，有
> $$
> P_{i,j}(r, t) = \sum\limits_{k} P_{i,k} (r,s) P_{k,j} (s, t)
> $$
> 在[[#平稳转移概率假设]]下，对时间间隔 $m, n$，有
> $$
> P_{i,j}{(m + n)} = \sum\limits_{k} P_{i,k}{(m)} P_{k,j}{(n)}
> $$
^ChapmanKolmogorovIdentity

[[#^ChapmanKolmogorovIdentity|C-K 方程]]的本质是将路径求和**按照中间时刻 $s$（或中间步数 $m$）的状态 $k$ 分组**，因此显然是一个恒等式。具体地，
$$
\begin{align}
P_{i,j}{(m + n)} &= P \left\{ X_{m + n} = x_{j} \mid X_{0} = x_{i} \right\}  \\
&= \sum\limits_{k} P \left\{ X_{m + n} = x_{j} , X_{m} = x_{k} \mid X_{0} = x_{i} \right\} \\
&= \sum\limits_{k} P \left\{ X_{m + n} = x_{j} \mid X_{m} = x_{k}, X_{0} = x_{i} \right\} P \left\{ X_{m} = x_{k} \mid X_{0} = x_{i} \right\} \\
&= \sum\limits_{k} \underbrace{ P \left\{ X_{m + n} = x_{j} \mid X_{m} = x_{k} \right\} }_{ P_{k,j}{(n)} } \underbrace{ P \left\{ X_{m} = x_{k} \mid X_{0} = x_{i} \right\} }_{ P_{i,k}{(m)} }
\end{align}
$$

容易发现，[[#^ChapmanKolmogorovIdentity|C-K 方程]]的形式类似**矩阵乘法**，由此定义
$$
\boldsymbol{P}(n) = \Big( P_{i,j}{(n)} \Big)_{i,j}
$$
称为 **$n$ 步转移概率矩阵**，则立得
$$
\mark{ \boldsymbol{P}(m + n) = \boldsymbol{P}(m) \boldsymbol{P}(n) }
$$

于是，任意步数 $n$ 的转移概率矩阵为
$$
\boldsymbol{P}(n) = \boldsymbol{P}(n-1) \boldsymbol{P}(1) = \boldsymbol{P}(n-2) (\boldsymbol{P}(1))^{2} = \cdots (\boldsymbol{P}(1))^{n}
$$
因此，只要给定
+ **1 步转移概率矩阵** $\boldsymbol{P}(1) = \Big( P_{i,j}{(1)} \Big)_{i,j}$，不妨**记为 $\boldsymbol{P}$**，以及
+ **初始概率分布 $\big\{ P \left\{ X_{0} = x_{i} \right\} \big\}_{i}$**，

则整个 Markov 链的概率分布就确定了。

## Markov 链的常返性

从 Markov 性的「精神」出发，当转移步数 $n$ 即**时间趋于无穷**时，我们希望 Markov 链达到一个**不依赖初始状态的稳定分布**，即希望有
$$
P_{i,j}{(n)} \quad \xrightarrow{n \to \infty} \quad P_{j}
$$

### Markov 链状态的分类

我们期望深入考察 Markov 链的状态空间结构，为此**将状态值 $x_{i}$ 简记为 $i$**，并给出如下几个定义：
+ 若 $\exists n > 0$，$P_{i,j}(n) > 0$，则称 **$i$ 可达 (reachable) $j$**，记作 $i \to j$；
+ 若 $i \to j$ 且 $j \to i$，则称 **$i$、$j$ 相通 (commutative)**，记作 $i \leftrightarrow j$；
+ 如果对集合 $S \subseteq E$，$\forall i \in S$、$j \not\in S$，$i \not\to j$，则称 $S$ 为**闭集 (closed set)**。 ^ClosedSet

> [!def.] 不可约 Markov 链
> 设 Markov 链的状态空间为 $E$，如果子集 $C \subseteq E$ 仅有一个[[#^ClosedSet|闭集]] $C$ 本身，即**不存在闭的真子集**，则称该子集为**不可约 (irreducible)** 的。
> 
> 如果状态空间 $E$ 本身是不可约的，则称该 Markov 链为**不可约**的。
^Bukeyue

设 $C \subseteq E$ 不可约，我们设 $\forall i \in C$，$A_{i} = \left\{ j \in C \mid i \to j \right\}$ 为 $i$ 可达的状态集合，现在我们证明 $A_{i}$ 是闭集，从而得到 $A_{i} = C$。$\forall j \in A_{i}$，假定 $\exists k \not\in A_{i}$，使得 $j \to k$，则由 $i \to j$ 和 $j \to k$ 可知 $i \to k$，从而 $k \in A_{i}$，与假设矛盾，因此 $A_{i}$ 是闭集，只能有 $A_{i} = C$。因此，**不可约 Markov 链中任意两个状态相通**。

### 常返

设 Markov 链的状态空间为 $E$，对 $i, j \in E$，定义从时刻 $n = 0$ 出发到达状态 $j$ 的**首达时间 (first passage time)** 为
$$
\tau_{j} = \inf \left\{ n \geq 1 \mid X_{n} = j \right\}
$$
经 $n$ 步从状态 $i$ 到状态 $j$ 的**首达概率 (first passage probability)** 为
$$
\begin{align} 
f_{i,j}(n) &= P \left\{ \tau_{j} = n \mid X_{0} = i \right\} \\
&= P \left\{ X_{1} \neq j, X_{2} \neq j, \cdots, X_{n-1} \neq j, X_{n} = j \mid X_{0} = i \right\} 
\end{align}
$$

显然，在哪一步首达的事件之间是互斥的，因此有
$$
f_{i,j} = \sum\limits_{n=1}^{\infty} f_{i,j}(n) \leq 1
$$
$f_{i,j}$ 即为**从状态 $i$ 出发「迟早」到达状态 $j$ 的概率**。

> [!def.] 常返性
> 对 Markov 链的状态空间 $E$ 中的状态 $i$，如果 $f_{i,i} = 1$，则称状态 $i$ 为**常返 (recurrent) 态**；否则，$f_{i,i} < 1$，称为**滑过 (transient) 态**或**非常返态**。
> 
> 从常返态 $i$ 出发，将**以概率 1** 返回到状态 $i$ 一次；而从非常返态 $i$ 出发，**有正的概率**永远不返回状态 $i$。

#### 常返性的判据

我们期望利用转移概率 $P_{i,j}{(n)}$ 来研究 $f_{i,j}(n)$，以判定状态 $i$ 的常返性。

类比于 [[#^ChapmanKolmogorovIdentity|C-K 方程]]的推导，我们可以将 $P_{i,j}(n)$ **按照首达时间 $\tau_{j}$ 分组**，有
$$
\begin{align}
P_{i,j}(n) &= P \left\{ X_{n} = j \mid X_{0} = i \right\} 
= \sum\limits_{k=1}^{n} P \left\{ X_{n} = j, \tau_{j} = k \mid X_{0} = i \right\} \\
&= \sum\limits_{k=1}^{n} P \left\{ X_{n} = j \mid \tau_{j} = k, X_{0} = i \right\} \cdot P \left\{ \tau_{j} = k \mid X_{0} = i \right\} \\
&= \sum\limits_{k=1}^{n} P \left\{ X_{n} = j \mid X_{k} = j \right\} \cdot P \left\{ \tau_{j} = k \mid X_{0} = i \right\} \\
&= \sum\limits_{k=1}^{n} P_{j,j}(n-k) f_{i,j}(k)
\end{align}
$$
即
$$
\mark{ P_{i,j}{(n)} = \sum\limits_{k=1}^{n} P_{j,j}{(n-k)} f_{i,j}(k) }
$$

上式表现出**离散时间索引的卷积**形式，因此可做 **$z$ 变换**，定义其**生成函数**为
$$
\t{P}_{i,j} (z) = \sum\limits_{n=0}^{\infty} P_{i,j}{(n)} z^{n} = \delta_{i,j} + \sum\limits_{n=1}^{\infty} P_{i,j}{(n)} z^{n}, \qquad
F_{i,j} (z) = \sum\limits_{n=1}^{\infty} f_{i,j}(n) z^{n}
$$
则有
$$
\begin{align} 
\t{P}_{i,j} (z) &= \delta_{i,j} + \sum\limits_{n=1}^{\infty} \sum\limits_{k=1}^{n} P_{j,j}{(n-k)} f_{i,j}(k) \cdot  z^{n}  \\
&= \delta_{i,j} + \sum\limits_{k=1}^{\infty} \sum\limits_{n=k}^{\infty} (f_{i,j}(k) z^{k}) (P_{j,j}{(n-k)} z^{n-k}) \\
&= \delta_{i,j} + \left( \sum\limits_{k=1}^{\infty} f_{i,j}(k) z^{k} \right) \left( \sum\limits_{m=0}^{\infty} P_{j,j}{(m)} z^{m} \right) 
= \delta_{i,j} + F_{i,j} (z) \t{P}_{j,j} (z)
\end{align}
$$
即
$$
\mark{ \t{P}_{i,j} (z) = \delta_{i,j} + F_{i,j} (z) \t{P}_{j,j} (z) }
$$

> [!note] Markov 链的分解
> Markov 链有两种**分解**方案：
> + 在**空间**上分解，按照先走 $m$ 步时的中间状态 $k$ 分组，得到
> $$
> P_{i,j}{(n)} = \sum\limits_{k} P_{i,k}{(m)} P_{k,j}{(n - m)}
> \quad\text{OR}\quad
> \boldsymbol{P}{(m + n)} = \boldsymbol{P}{(m)} \boldsymbol{P}{(n)}
> $$
> 即 [[#^ChapmanKolmogorovIdentity|C-K 方程]]；
> + 在**时间**上分解，按照首达时间分组，得到上式
> $$
> P_{i,j}{(n)} = \sum\limits_{k=1}^{n} P_{j,j}{(n-k)} f_{i,j}(k)
> \quad\text{OR}\quad
> \t{P}_{i,j} (z) = \delta_{i,j} + F_{i,j} (z) \t{P}_{j,j} (z)
> $$
^MarkovFenjie

从而，令 $i = j$ 并令 $z \to 1_{-}$，得
$$
\sum\limits_{n=0}^{\infty} P_{i,i}{(n)} = \t{P}_{i,i} (1_{-}) = \dfrac{1}{1 - \sum\limits_{n=1}^{\infty} f_{i,i}(n)} = \dfrac{1}{1 - f_{i,i}}
$$
$f_{i,i}$ 是否为 1 取决于左侧级数 $\sum\limits_{n=0}^{\infty} P_{i,i}{(n)}$ 的敛散性，由此给出常返性的第一判据。

> [!theorem] 常返性判据
> 状态 $i$ 为常返态的**充分必要条件**为级数 $\sum\limits_{n=0}^{\infty} P_{i,i}{(n)}$ 发散。
^RecurrentCriterionI

当 $i \neq j$ 时，令 $z \to 1_{-}$ 则得到
$$
\sum\limits_{n=0}^{\infty} P_{i,j}{(n)} = \t{P}_{i,j} (1_{-}) = F_{i,j} (1_{-}) \t{P}_{j,j} (1_{-}) = f_{i,j} \sum\limits_{n=0}^{\infty} P_{j,j}{(n)}
$$
若 $j$ **不是常返态**，则由[[#^RecurrentCriterionI|判据]]有 $\sum\limits_{n=0}^{\infty} P_{j,j}(n) < \infty$，且由 $f_{i,j} \le 1$ 亦知 $\sum\limits_{n=0}^{\infty} P_{i,j}(n) < \infty$，则二者的通项
$$
P_{j,j}(n) \xrightarrow{n \to \infty} 0, \qquad P_{i,j}(n) \xrightarrow{n \to \infty} 0
$$
^NonRecurrentLimit

这也是我们主要研究常返态的原因。

#### 态的返回次数

对常返态 $i$，定义其**返回次数** $N_{i} = \# \left\{ n \mid X_{n} = i, X_{0} = i \right\}$，则 $N_{i}$ 的**期望**为
$$
\mathbb{E} \left[ N_{i} \right] = \mathbb{E} \left[ \sum\limits_{n=0}^{\infty} \mathbb{1}_{\left\{ X_n = i \mid X_{0} = i \right\}} \right] = \sum\limits_{n=0}^{\infty} \mathbb{E} \left[ \mathbb{1}_{\left\{ X_n = i \mid X_{0} = i \right\}} \right] = \sum\limits_{n=0}^{\infty} P_{i,i}{(n)} = \infty 
$$

记从 $i$ 到达 $j$ 至少 $n$ 次的概率为
$$
g_{i,j}(n) = P \left\{ \#\left\{ k \mid X_{k} = j \right\} \geq n \mid X_{0} = i \right\}
$$
利用 Markov 链的[[#^MarkovFenjie|时间分解]]，可知
$$
\begin{align}
g_{i,j}(n) &= \sum\limits_{m=1}^{\infty} P \left\{ \tau_{j} = m, \#\left\{ k > m \mid X_{k} = j \right\} \geq n - 1 \mid X_{0} = i \right\} \\
&= \sum\limits_{m=1}^{\infty} P \left\{ \tau_{j} = m \mid X_{0} = i \right\} \cdot P \left\{ \#\left\{ k > m \mid X_{k} = j \right\} \geq n - 1 \mid X_{m} = j \right\} \\
&= \sum\limits_{m=1}^{\infty} P \left\{ \tau_{j} = m \mid X_{0} = i \right\} \cdot P \left\{ \#\left\{ k \mid X_{k} = j \right\} \geq n - 1 \mid X_{0} = j \right\} \\
&= \sum\limits_{m=1}^{\infty} f_{i,j}(m) \cdot g_{j,j}(n - 1) = f_{i,j} \cdot g_{j,j}(n - 1)
\end{align}
$$
令 $i = j$，则有**递推关系**
$$
g_{i,i}(n) = f_{i,i} \cdot g_{i,i}(n - 1)
$$
由 $g_{i,i}(0) = 1$ 可得
$$
P \left\{ N_{i} = n \right\} = g_{i,i}(n) = (f_{i,i})^{n} \xrightarrow{n \to \infty} \begin{cases}
1, & \text{if } f_{i,i} = 1, \\
0, & \text{if } f_{i,i} < 1
\end{cases}
$$
因此，**常返态几乎必然无限次返回，而非常返态则几乎必然有限次返回**。

#### 常返性与连通性

下面考虑 **$i \leftrightarrow j$**，即 **$i$、$j$ 相通**的情况。由 $i \to j$，可知 $\exists m$ 使得 $P_{i,j}{(m)} > 0$；由 $j \to i$，可知 $\exists n$ 使得 $P_{j,i}{(n)} > 0$。因此，对于任意 $k$，都有
$$
P_{i,i}{(m + n + k)} \geq P_{i,j}{(m)} P_{j,j}{(k)} P_{j,i}{(n)}
$$
即
$$
\sum\limits_{k=0}^{\infty} P_{i,i}{(m + n + k)} \geq P_{i,j}{(m)} P_{j,i}{(n)} \sum\limits_{k=0}^{\infty} P_{j,j}{(k)}
$$
若 **$j$ 为常返态**，则由[[#^RecurrentCriterionI|判据]]知右侧发散，因此左侧亦发散，从而 $\sum\limits_{k=0}^{\infty} P_{i,i}{(k)}$ 发散，由[[#^RecurrentCriterionI|判据]]知 **$i$ 亦为常返态**，故

> [!theorem] 连通状态的常返性
> Markov 链中连通状态的**常返性相同**。

对**有限状态 Markov 链**，倘若所有状态都非常返态，则取定 $\forall i \in E$ 都有 
$$
\forall j \in E, \quad P_{i,j}{(n)} \xrightarrow{n \to \infty} 0
\quad\Longrightarrow\quad
\sum\limits_{j \in E} P_{i,j}{(n)} \xrightarrow{n \to \infty} 0
$$
但由概率归一性知 $\sum\limits_{j \in E} P_{i,j}{(n)} = 1$，与上式矛盾，因此**有限状态 Markov 链中至少存在一个常返态**。进而，**有限[[#^Bukeyue|不可约]] Markov 链中所有状态均为常返态**。

进一步考察任意 Markov 链（也只剩无限状态的情况了），设其存在一个**常返态 $i$**，则知 $g_{i,i}(\infty) = 1$。对此概率表示的「返回无穷次」的路径加以[[#^MarkovFenjie|空间分解]]，有
$$
\begin{align}
1 = g_{i,i}(\infty) &= \sum\limits_{k \in E} P_{i,k}(m) \cdot P \left\{ \#\left\{ n > m \mid X_{n} = i \right\} = \infty \mid X_{m} = k \right\} \\
&= \sum\limits_{k \in E} P_{i,k}(m) \cdot g_{k,i}(\infty), \qquad \forall m > 0
\end{align}
$$
而知 $\sum\limits_{k \in E} P_{i,k}(m) = 1$，因此 $\sum\limits_{k \in E} P_{i,k}(m) \cdot (1 - g_{k,i}(\infty)) = 0$，这一求和中每一项均非负，故必有
$$
\forall m > 0, \quad \forall k \in E, \quad P_{i,k}(m) \cdot (1 - g_{k,i}(\infty)) = 0
$$
对于 $i$ 的某一可达状态 $j$，由 $i \to j$ 可知 $\exists m$ 使得 $P_{i,j}(m) > 0$，因此 $g_{j,i}(\infty) = 1$，即 **$j \to i$**，从而 **$i \leftrightarrow j$** 且 **$j$ 亦为常返态**。

> [!theorem] 可达状态的常返性
> 若 Markov 链中存在常返态 $i$，则 $i$ 的**所有可达状态**均与 $i$ **相通**，且均为常返态。

## 转移概率的极限行为

### Markov 链的周期性

> [!def.] 周期态
> 对状态 $i$，定义其**周期 (period)** 为
> $$
> d_{i} = \gcd \left\{ n \geq 1 \mid P_{i,i}{(n)} > 0 \right\}
> $$
> 其中 $\gcd$ 表示**最大公约数 (greatest common divisor)**。
> 
> 如果 $d_{i} = 1$，则称状态 $i$ 为**非周期 (aperiodic) 态**；否则，$d_{i} \geq 2$，称为**周期 (periodic) 态**。

**非周期**带来的一个直观性质是
$$
\exists N, \quad \forall n \geq N, \quad P_{i,i}{(n)} > 0
$$

考虑两个相通状态 $i$、$j$，即设 $\exists m$ 使得 $P_{i,j}{(m)} > 0$，同时 $\exists n$ 使得 $P_{j,i}{(n)} > 0$，因此
+ $P_{i,i}(m + n) \ge P_{i,j}(m) P_{j,i}(n) > 0$，故 **$d_{i} \mid (m + n)$**；
+ $\forall k \in \left\{ n \geq 1 \mid P_{j,j}{(n)} > 0 \right\}$，有 $P_{i,i}(m + k + n) \ge P_{i,j}(m) P_{j,j}(k) P_{j,i}(n) > 0$，故 **$d_{i} \mid (m + k + n)$**。

由此，**$\forall k \in \left\{ n \geq 1 \mid P_{j,j}{(n)} > 0 \right\}$，$d_{i} \mid k$**，即 $d_{i}$ 是该集合的一个公约数，故 **$d_{i} \mid d_{j}$**。同理可得 $d_{j} \mid d_{i}$，因此 **$d_{i} = d_{j}$**，即**相通状态的周期性相同**。

这样，在[[#^Bukeyue|不可约 Markov 链]]中，所有状态的周期性均相同。若其中有一个状态为非周期态，则所有状态均为非周期态，称该 Markov 链为**非周期的**，并有
$$
\exists N, \quad \forall n \geq N, \quad \forall i,j \in E, \quad P_{i,j}{(n)} > 0
$$

#### 遍历性

在**非周期**的[[#^Bukeyue|不可约 Markov 链]]中，直接有
$$
\lim_{n \to \infty} P_{i,j}{(n)} = \pi_{j}
$$
称为**遍历性 (ergodicity) 定理**，其中 $\pi_{j}$ 与初始状态 $i$ 无关。

若没有非周期的条件，而是在任意[[#^Bukeyue|不可约 Markov 链]]中任取两个状态 $i$、$j$，有
$$
\lim\limits_{ n \to \infty } \dfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)} = \dfrac{1}{a_{j}}
$$
称为**弱遍历性 (weak ergodicity) 定理**，其中 $a_{j} = \sum\limits_{k=1}^{\infty} f_{i,i}(k)\cdot k$ 为状态 $j$ 的**平均返回时间 (mean return time)**，与初始状态 $i$ 无关。由级数知识知，若存在 $\lim\limits_{n \to \infty} P_{i,j}{(n)} = \pi_{j}$，则 $\cfrac{1}{a_{j}} = \lim\limits_{ n \to \infty } \dfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)} = \pi_{j}$。

另外，此处 $\cfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)}$ 可写成
$$
\begin{align} 
\dfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)} &= \dfrac{1}{n} \sum\limits_{k=1}^{n} \mathbb{E} \left[ \mathbb{1}_{\left\{ X_{k} = j \mid X_{0} = i \right\}} \right] 
= \dfrac{1}{n} \mathbb{E} \left[ \sum\limits_{k=1}^{n} \mathbb{1}_{\left\{ X_{k} = j \mid X_{0} = i \right\}} \right] \\
&= \dfrac{\mathbb{E} \left[ \#\left\{ k \mid X_{k} = j, X_{0} = i, 1\le k \le n \right\} \right] }{n} 
\end{align}
$$
其概率意义是在 $n$ 步转移中**到达状态 $j$ 的平均频率**，即 $n$ 步转移中**状态 $j$ 的平均比例**。

#### 正常返、零常返

考虑上述「平均到达频率」的极限 $\lim\limits_{ n \to \infty } \cfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)}$，其与初始状态无关，因此也可称为「平均返回频率」。由[[#^NonRecurrentLimit|非常返态的性质]]知，若状态 $j$ 为非常返态，则 $P_{i,j}{(n)} \xrightarrow{n \to \infty} 0$，从而 $\lim\limits_{ n \to \infty } \cfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)} = 0$，即**平均返回频率为 0**。

但对于常返态，并不一定有正的平均频率，定义：
+ 若状态 $j$ 的**平均返回时间有限**，即 $a_{j} < \infty$，则 $\lim\limits_{ n \to \infty } \cfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)} = \cfrac{1}{a_{j}} > 0$，称状态 $j$ 为**正常返 (positive recurrent) 态**；
+ 若状态 $j$ 的**平均返回时间无限**，即 $a_{j} = \infty$，则 $\lim\limits_{ n \to \infty } \cfrac{1}{n} \sum\limits_{k=1}^{n} P_{i,j}{(k)} = 0$，称状态 $j$ 为**零常返 (null recurrent) 态**。

> [!example] 零常返的实例
> 考虑[[例题 - Markov链#L19-1|一维无限制随机游走]]，已知当 $p=\cfrac{1}{2}$ 时状态 0（以及其他所有状态）为常返态，但有
> $$
> P(z) = \sum\limits_{n=0}^{\infty} P_{0,0}{(2n)} z^{2n} = \sum\limits_{n=0}^{\infty} \binom{2n}{n} \left( \dfrac{1}{2} \right)^{2n} z^{2n} = \dfrac{1}{\sqrt{1 - z^{2}}}
> $$
> 于是
> $$
> \lim\limits_{ n \to \infty } \dfrac{1}{n} \sum\limits_{k=1}^{n} P_{0,0}{(k)} = \lim\limits_{ z \to 1_{-} } (1 - z) P(z) = \lim\limits_{ z \to 1_{-} } \dfrac{1 - z}{\sqrt{1 - z^{2}}} = 0
> $$
> 因此，**常返态中亦可存在平均返回频率为 0 的情况**。



### 平稳分布

由 [[#^ChapmanKolmogorovIdentity|C-K 方程]]，$\boldsymbol{P}(n)$ 有分解
$$
\boldsymbol{P}(n) = \boldsymbol{P}(n-1) \boldsymbol{P}(1) = \boldsymbol{P}(1) \boldsymbol{P}(n-1)
$$
因此，若**极限 $\lim\limits_{n \to \infty} \boldsymbol{P}(n) = \boldsymbol{\varPi}$ 存在**，则有
$$
\boldsymbol{\varPi} = \boldsymbol{\varPi} \boldsymbol{P},
\qquad\text{and}\qquad
\boldsymbol{\varPi} = \boldsymbol{P} \boldsymbol{\varPi}
$$
其中，
+ $\boldsymbol{\varPi} = \lim\limits_{n \to \infty} \boldsymbol{P}(n)$ 显然应**与初状态无关**，即形如
$$
\boldsymbol{\varPi} = \begin{pmatrix}\pi_{1} & \pi_{2} & \pi_{3} & \cdots \\ \pi_{1} & \pi_{2} & \pi_{3} & \cdots \\ \vdots & \vdots & \vdots & \vdots \\ \pi_{1} & \pi_{2} & \pi_{3} & \cdots \end{pmatrix} = \v{1}^{\mathrm{T}} \begin{pmatrix}\pi_{1} & \pi_{2} & \pi_{3} & \cdots \end{pmatrix} = \v{1}^{\mathrm{T}} \v{\pi}
$$
+ 1 步转移概率矩阵 $\boldsymbol{P} = \boldsymbol{P}(1) = \Big( P_{i,j}{(1)} \Big)_{i,j}$ 的各行表示从各状态出发的概率分布，因此**各行和均为 1**，即 $\boldsymbol{P} \v{1}^{\mathrm{T}} = \v{1}^{\mathrm{T}}$。

由此 $\boldsymbol{\varPi} \equiv \boldsymbol{P} \boldsymbol{\varPi}$ 成为恒等式，而 $\boldsymbol{\varPi} = \boldsymbol{\varPi} \boldsymbol{P}$ 则可展开为
$$
\mark{ \v{\pi} = \v{\pi} \boldsymbol{P} }
$$
注意此处的 $\v{\pi}$ 是行向量。

首先确认 $\v{\pi}$ 非零解的存在性。对（更熟悉的列向量形式的）方程 $(\boldsymbol{P}^{\mathrm{T}} - \boldsymbol{I}) \v{\pi}^{\mathrm{T}} = \v{0}^{\mathrm{T}}$，考虑 $\boldsymbol{P}$ 的特征方程
$$
\det (\boldsymbol{P}^{\mathrm{T}} - \lambda \boldsymbol{I}) = \det (\boldsymbol{P} - \lambda \boldsymbol{I}) = 0
$$
由概率矩阵的性质知 $\boldsymbol{P} \v{1}^{\mathrm{T}} = \v{1}^{\mathrm{T}}$，即 $\lambda = 1$ 是其特征值，$\det (\boldsymbol{P}^{\mathrm{T}} - \boldsymbol{I}) = 0$，从而**齐次线性方程组有非零解**。

进一步，向量中各元素 $\pi_{j} = \sum\limits_{i} \pi_{i} P_{i,j}(1)$。当**初始分布 $P(X_{0} = i)$ 即为 $\pi_{i}$** 时，有
$$
P(X_{1} = j) = \sum\limits_{i} P(X_{0} = i) P_{i,j}(1) = \sum\limits_{i} \pi_{i} P_{i,j}(1) = \pi_{j}
$$
即**经过一步转移后分布不变**，这是称 $\v{\pi}$ 为 Markov 链的**平稳分布 (stationary distribution)** 的原因。

## † 连续时间 Markov 链

设有随机过程 $X(t)$，其状态空间记为 $E = \{1, 2, \cdots \}$，其 **Markov 性**定义为
$$
\begin{align} 
\forall t_{1} \le t_{2} \le \cdots \le t_{n}, \quad &P \left\{ X(t_{n}) = x_{n} \mid X(t_{n-1}) = x_{n-1}, \cdots, X(t_{1}) = x_{1} \right\}  \\
&= P \left\{ X(t_{n}) = x_{n} \mid X(t_{n-1}) = x_{n-1} \right\} 
\end{align}
$$
满足上述性质的随机过程称为**连续时间 Markov 链 (continuous-time Markov chain, CTMC)**。

### 转移概率与生成元矩阵

连续时间 Markov 链的**转移概率**定义为
$$
P_{i,j}(t) = P \left\{ X(t + s) = j \mid X(s) = i \right\}, \quad \forall s, t \geq 0
$$
由于状态离散，与离散时间 Markov 链类似可定义 $\boldsymbol{P}(t) = \big( P_{i,j}(t) \big)_{i,j}$，且同样有 **Chapman-Kolmogorov 方程**
$$
\boldsymbol{P}(t + s) = \boldsymbol{P}(t) \boldsymbol{P}(s)
$$

不同于离散时间 Markov 链，连续时间 Markov 链没有「1 步转移」的概念，其转移概率矩阵 $\boldsymbol{P}(t)$ 随时间 $t$ **连续变化**。因此，我们考察
$$
\begin{align} 
\lim\limits_{\Delta t \to 0} \dfrac{\boldsymbol{P}(t + \Delta t) - \boldsymbol{P}(t)}{\Delta t} 
&= \lim\limits_{\Delta t \to 0} \dfrac{\boldsymbol{P}(t) \boldsymbol{P}(\Delta t) - \boldsymbol{P}(t)}{\Delta t}
= \boldsymbol{P}(t) \cdot \lim\limits_{\Delta t \to 0} \dfrac{\boldsymbol{P}(\Delta t) - \boldsymbol{I}}{\Delta t} \\
&= \lim\limits_{\Delta t \to 0} \dfrac{\boldsymbol{P}(\Delta t) \boldsymbol{P}(t) - \boldsymbol{P}(t)}{\Delta t}
= \lim\limits_{\Delta t \to 0} \dfrac{\boldsymbol{P}(\Delta t) - \boldsymbol{I}}{\Delta t} \cdot \boldsymbol{P}(t) 
\end{align}
$$
定义**生成元矩阵 (generator matrix)** 为
$$
\boldsymbol{Q} = \lim\limits_{\Delta t \to 0} \dfrac{\boldsymbol{P}(\Delta t) - \boldsymbol{I}}{\Delta t}
$$
则有 **Kolmogorov 前向方程与后向方程**
$$
\begin{cases}
\cfrac{\dif}{\dif t} \boldsymbol{P}(t) = \boldsymbol{P}(t) \boldsymbol{Q}  & \text{（前向方程）} \\
\cfrac{\dif}{\dif t} \boldsymbol{P}(t) = \boldsymbol{Q} \boldsymbol{P}(t)  & \text{（后向方程）}
\end{cases} 
$$
于是，$\boldsymbol{P}(t)$ 的演化由 $\boldsymbol{Q}$ 决定，有
$$
\boldsymbol{P}(t) = \boldsymbol{P}(0) \e^{\boldsymbol{Q} t} = \boldsymbol{P}(0) \sum\limits_{n=0}^{\infty} \dfrac{(\boldsymbol{Q} t)^{n}}{n!} = \boldsymbol{P}(0) \sum\limits_{n=0}^{\infty} \dfrac{t^{n}}{n!} \boldsymbol{Q}^{n} 
$$

$\boldsymbol{Q}$ 有以下性质：
+ 其**非对角元非负**，即 $Q_{i,j} \geq 0, \forall i \neq j$，表示单位时间内从状态 $i$ 转移到状态 $j$ 的速率；
+ 其**对角元为负**，保证**行和为 0**，即 $Q_{i,i} = - \sum\limits_{j \neq i} Q_{i,j} \leq 0$，表示单位时间内**离开状态 $i$** 的速率。

> [!example] Poisson 过程的生成元矩阵 
> [[Poisson 过程]]即是一个典型的连续时间 Markov 链，由[[Poisson 过程#^XishuxingJiashe|稀疏性假设]]，其在 $\Delta t \to 0$ 间隔内的转移概率为
> $$
> P_{i,j}(\Delta t) = \begin{cases}
> \e^{-\lambda \Delta t} , & j = i, \\
> \lambda \Delta t \cdot \e^{-\lambda \Delta t} , & j = i + 1, \\
> 0 , & \text{otherwise}
> \end{cases}
> $$
> 因此，其生成元矩阵的矩阵元为
> $$
> Q_{i,j} = \lim\limits_{\Delta t \to 0} \dfrac{P_{i,j}(\Delta t) - \delta_{i,j}}{\Delta t} = \begin{cases}
> -\lambda , & j = i, \\
> \lambda , & j = i + 1, \\
> 0 , & \text{otherwise}
> \end{cases}
> $$
> 即生成元矩阵为
> $$
> \boldsymbol{Q} = \begin{pmatrix}
> -\lambda & \lambda \\
> & -\lambda & \lambda \\
> & & -\lambda & \lambda \\
> & & & \ddots & \ddots
> \end{pmatrix}
> $$

### 平稳分布

不同于离散时间 Markov 链，对连续时间 Markov 链，只要**不可约**，则 $P_{i,j}(t)$ 的极限 $\lim\limits_{t \to \infty} P_{i,j}(t) = \pi_{j}$ 总是存在，且与初始状态 $i$ 无关。因此，$\boldsymbol{P}(t)$ 的极限 $\lim\limits_{t \to \infty} \boldsymbol{P}(t) = \boldsymbol{\varPi}$ 亦存在，且形如
$$
\boldsymbol{\varPi} = \begin{pmatrix}
\pi_{1} & \pi_{2} & \pi_{3} & \cdots \\
\pi_{1} & \pi_{2} & \pi_{3} & \cdots \\
\vdots & \vdots & \vdots & \vdots \\
\pi_{1} & \pi_{2} & \pi_{3} & \cdots
\end{pmatrix} = \v{1}^{\mathrm{T}} \v{\pi}
$$
由 Kolmogorov 前向方程知
$$
\boldsymbol{O} = \lim\limits_{t \to \infty} \dfrac{\dif}{\dif t} \boldsymbol{P}(t) = \lim\limits_{t \to \infty} \boldsymbol{P}(t) \boldsymbol{Q} = \boldsymbol{\varPi} \boldsymbol{Q}
\quad \Longrightarrow \quad
\v{\pi} \boldsymbol{Q} = \v{0}
$$
同样需注意此处向量符号默认是**行向量**。

与离散时间 Markov 链类似，$\v{\pi}$ 是连续时间 Markov 链的**平稳分布**，当初始分布为 $\v{\pi}$ 时，经过任意时间 $t$ 的转移后分布仍为 $\v{\pi}$。
