## Poisson 过程的定义

Poisson 过程是一类**时间连续、状态离散**的随机过程，广泛应用于排队论、可靠性工程、通信系统等领域。它描述了在单位时间内某事件发生的次数，且这些事件是独立且均匀分布的。

### 增量独立性、增量平稳性

一个随机过程 $X(t)$ 如果满足
$$
\forall t_{1} < t_{2} \le t_{3} < t_{4}, \qquad X(t_{2}) - X(t_{1}) \perp X(t_{4}) - X(t_{3})
$$
则称其具有**增量独立性 (independent increments)**。

此外，如果对于任意 $s, t, \tau \ge 0$，都有
$$
X(t + \tau) - X(s + \tau) \stackrel{\text{d}}{=} X(t) - X(s)
$$
其中 $\stackrel{\text{d}}{=}$ 表示**同分布 (equal in distribution)**，即 $X(t) - X(s)$ 的分布只与 $t - s$ 有关，而与具体的时间点无关，则称其具有**增量平稳性 (stationary increments)**。

### 概率母函数

对于取非负整数值的随机变量 $X(t)$，参照 $z$ 变换引入其**概率母函数 (probability-generating function, PGF)**，定义为
$$
G_{X(t)}(z) = \mathbb{E}\left[z^{X(t)}\right]
$$
则 $G_{X(t)}(z)$ 可以展开为
$$
G_{X(t)}(z) = \sum_{k=0}^{\infty} P\left\{ X(t) = k \right\} \cdot z^{k}
$$
即 $P\{X(t)=k\}$ 对应概率母函数中 $z^k$ 的系数。

### Poisson 过程的引入

设 $X(t)$ 是一个具有[[#增量独立性、增量平稳性]]的随机过程，我们尝试构造一个关于其[[#概率母函数]]的微分方程。

为此，求概率母函数对时间的导数，即
$$
\begin{align} 
\dfrac{\dif}{\dif t} G_{X(t)}(z) &= \lim_{\Delta t \to 0} \dfrac{G_{X(t + \Delta t)}(z) - G_{X(t)}(z)}{\Delta t}
= \lim_{\Delta t \to 0} \dfrac{\mathbb{E}\left[z^{X(t + \Delta t)} - z^{X(t)}\right]}{\Delta t}  \\
&= \lim_{\Delta t \to 0} \dfrac{\mathbb{E}\left[z^{X(t)} \left( z^{X(t + \Delta t) - X(t)} - 1 \right) \right]}{\Delta t}
\end{align}
$$
令**初态 $X(0) = 0$**，则由增量独立性有 $X(t) - X(0)$ 与 $X(t + \Delta t) - X(t)$ 独立，由增量平稳性有 $X(t + \Delta t) - X(t) \stackrel{\text{d}}{=} X(\Delta t)$，因此上式可写为
$$
\begin{align}
\dfrac{\dif}{\dif t} G_{X(t)}(z) &= \lim_{\Delta t \to 0} \dfrac{\mathbb{E}\left[z^{X(t)}\right] \cdot \mathbb{E}\left[z^{X(t + \Delta t) - X(t)} - 1\right]}{\Delta t} \\
&= G_{X(t)}(z) \cdot \lim_{\Delta t \to 0} \dfrac{\mathbb{E}\left[z^{X(\Delta t)} - 1\right]}{\Delta t} \\
&= G_{X(t)}(z) \cdot \lim_{\Delta t \to 0} \dfrac{1}{\Delta t} \left( \sum\limits_{k=0}^{\infty} P\{X(\Delta t) = k\} \cdot z^{k} - 1 \right)
\end{align}
$$
^JumuHanshuDeDaoshu

括号中的因子可展开为
$$
\begin{align}
&\sum\limits_{k=0}^{\infty} P\{X(\Delta t) = k\} \cdot z^{k} - 1 \\
&= \underbrace{ P\{X(\Delta t) = 0\} - 1 }_{ \#1 } + \underbrace{ P\{X(\Delta t) = 1\} \cdot z^{1} }_{ \#2 } + \underbrace{ \sum\limits_{k=2}^{\infty} P\{X(\Delta t) = k\} \cdot z^{k} }_{ \#3 }
\end{align}
$$
分别处理上述三项。

#### 零事件项的极限

注意到
$$
\begin{align}
P\{X(t) = 0\} &= P\{ X(s) = 0, X(t) - X(s) = 0 \} \quad(\forall s \in [0, t]) \\
&= P\{ X(s) = 0 \} \cdot P\{ X(t) - X(s) = 0 \} \\
&= P\{ X(s) = 0 \} \cdot P\{ X(t - s) = 0 \}
\end{align}
$$
因此，$H(t) = P\{X(t) = 0\}$ 满足**函数方程**
$$
H(t) = H(s) \cdot H(t - s)
$$
在**有界**的条件下，唯一解为**指数函数**，即知
$$
P\{X(\Delta t) = 0\} = \e^{-\lambda \Delta t}, \qquad \lambda \ge 0
$$
因此
$$
\lim\limits_{ \Delta t \to 0 } \dfrac{1}{\Delta t} \left( P\{X(\Delta t) = 0\} - 1 \right) = \lim\limits_{ \Delta t \to 0 } \dfrac{ \e^{-\lambda \Delta t} - 1 }{ \Delta t } = -\lambda
$$

#### 单事件项的极限

已知
$$
P \left\{ X(\Delta t) = 0 \right\} + P \left\{ X(\Delta t) = 1 \right\} + P \left\{ X(\Delta t) \ge 2 \right\} = 1
$$
即有
$$
\dfrac{1 - P \left\{ X(\Delta t) = 0 \right\}}{\Delta t} = \dfrac{P \left\{ X(\Delta t) = 1 \right\}}{\Delta t} \left( 1 + \dfrac{P\left\{ X(\Delta t) \ge 2 \right\}}{P\left\{ X(\Delta t) = 1 \right\}} \right)
$$
为了使得上式在 $\Delta t \to 0$ 时有界，必须引入**稀疏性假设 (sparsity assumption)**，即要求
$$
\lim_{\Delta t \to 0} \dfrac{1}{\Delta t} \dfrac{P\left\{ X(\Delta t) \ge 2 \right\}}{P\left\{ X(\Delta t) = 1 \right\}} = 0
$$
^XishuxingJiashe

在此假设下，有
$$
\lim\limits_{ \Delta t \to 0 } \dfrac{1}{\Delta t} P \left\{ X(\Delta t) = 1 \right\} = \lambda
$$

#### 多事件项的极限

我们先考察这个求和项的收敛，有
$$
\begin{align}
\left| \sum\limits_{k=2}^{\infty} P\{X(\Delta t) = k\} \cdot z^{k} \right| &\le \sum\limits_{k=2}^{\infty} P\{X(\Delta t) = k\} \cdot |z|^{k} \\
&= \sum\limits_{k=2}^{\infty} P\{X(\Delta t) = k\} = P\{X(\Delta t) \ge 2\}
\end{align}
$$
因此，在稀疏性假设下，有
$$
\dfrac{\left| \sum\limits_{k=2}^{\infty} P\{X(\Delta t) = k\} \cdot z^{k} \right|}{P \left\{ X(\Delta t) = 1 \right\}} \le \dfrac{P\{X(\Delta t) \ge 2\}}{P \left\{ X(\Delta t) = 1 \right\}} \xrightarrow{\Delta t \to 0} o(\Delta t)
$$
故由夹逼准则知
$$
\lim\limits_{ \Delta t \to 0 } \dfrac{1}{\Delta t} \cdot P\left\{ X(\Delta t) = 1 \right\} \cdot \dfrac{\sum\limits_{k=2}^{\infty} P\{X(\Delta t) = k\} \cdot z^{k}}{P\left\{ X(\Delta t) = 1 \right\}} = 0
$$

综上，将三项结果代入概率母函数的导数表达式中，得到
$$
\dfrac{\dif}{\dif t} G_{X(t)}(z) = G_{X(t)}(z) \cdot \left( -\lambda + \lambda z + 0 \right ) = (-\lambda + \lambda z) G_{X(t)}(z)
$$
该微分方程的初始条件为
$$
G_{X(0)}(z) = \mathbb{E}\left[z^{X(0)}\right] = z^{0} = 1
$$
故解得
$$
G_{X(t)}(z) =  \mark{ \e^{(-\lambda + \lambda z) t} } = \e^{-\lambda t} \cdot \e^{\lambda t z} = \e^{-\lambda t}  \sum\limits_{k=0}^{\infty} \dfrac{(\lambda t)^{k}}{k!}  z^{k}
$$
对比[[#概率母函数]]的定义式，可知
$$
P\{X(t) = k\} = \dfrac{(\lambda t)^{k}}{k!} \e^{-\lambda t} , \qquad k = 0, 1, 2, \cdots
$$
这是一个以 $\lambda t$ 为参数的 **Poisson 分布**。

> [!def.] Poisson 过程
> 设 $N(t)$ 是一个随机过程，满足以下条件：
> 1. $N(t)$ 的取值为非负整数，且**初态 $N(0) = 0$**，
> 2. $N(t)$ 具有**增量独立性**和**增量平稳性**，
> 3. $N(t)$ 满足**稀疏性假设**，即 $\cfrac{P\left\{ N(\Delta t) \ge 2 \right\}}{P\left\{ N(\Delta t) = 1 \right\}} = o(\Delta t)$（$\Delta t \to 0$），
> 
> 则称 $N(t)$ 为 **Poisson 过程 (Poisson process)**，其概率分布为
> $$
> P\{N(t) = k\} = \dfrac{(\lambda t)^{k}}{k!} \e^{-\lambda t} , \qquad k = 0, 1, 2, \cdots
> $$
> 其中 $\lambda > 0$ 称为 Poisson 过程的**强度 (intensity)**。

由增量平稳性，概率分布也写为
$$
P\{N(t) - N(s) = k\} = \dfrac{(\lambda (t - s))^{k}}{k!} \e^{-\lambda (t - s)} , \qquad k = 0, 1, 2, \cdots
$$

## Poisson 过程的基本性质

### 非宽平稳

由 Poisson 过程的概率分布可知
$$
\mathbb{E}[N(t)] = \lambda t, \qquad \mathrm{Var}[N(t)] = \lambda t, \qquad
\mathbb{E} \left[ N^{2}(t) \right] = \lambda t + (\lambda t)^{2}
$$
Poisson 过程的相关函数为
$$
R_{N}(t_{1}, t_{2}) = \mathbb{E}[N(t_{1}) N(t_{2})] = \underbrace{ \lambda \min(t_{1}, t_{2}) }_{ C_{N}(t, s) } + \lambda^{2} t_{1} t_{2}
$$
因此，Poisson 过程既不满足**均值平稳 (mean stationary)**，也不满足**相关平稳 (correlation stationary)**，故 Poisson 过程是一个**非宽平稳**的随机过程，我们需要借助其他方法来分析其性质。

### 条件均值

设 $N(t)$ 是一个 Poisson 过程，且 $0 \le s < t$，则**沿时间方向**有
$$
\begin{align}
\mathbb{E} \left[ N(t) \mathop| N(s) \right] &= \mathbb{E} \left[ N(t) -N(s) + N(s) \mathop| N(s) \right]  \\
&= \mathbb{E} \left[ N(t) - N(s) \mathop| N(s) \right] + \mathbb{E} \left[ N(s) \mathop| N(s) \right] \\
&= \mathbb{E} \left[ N(t) - N(s) \right] + N(s) = \lambda (t - s) + N(s)
\end{align}
$$
即 Poisson 过程的条件期望是**时间线性**的，事件继续发生的速率仍为 $\lambda$。

反过来，我们考虑**逆时间方向**的条件概率分布，有
$$
\begin{align}
P \left\{ N(s) = k \mathop| N(t) = n \right\} &= \dfrac{P \left\{ N(s) = k, N(t) = n \right\}}{P \left\{ N(t) = n \right\}} \\
&= \dfrac{P \left\{ N(s) = k, N(t) - N(s) = n - k \right\}}{P \left\{ N(t) = n \right\}} \\
&= \dfrac{P \left\{ N(s) = k \right\} \cdot P \left\{ N(t) - N(s) = n - k \right\}}{P \left\{ N(t) = n \right\}} \\
&= \cfrac{ \dfrac{(\lambda s)^{k}}{k!} \e^{-\lambda s} \cdot \dfrac{(\lambda (t - s))^{n - k}}{(n - k)!} \e^{-\lambda (t - s)} }{ \dfrac{(\lambda t)^{n}}{n!} \e^{-\lambda t} } \\
&= \binom{n}{k} \left( \dfrac{s}{t} \right)^{k} \left( 1 - \dfrac{s}{t} \right)^{n - k}
\end{align}
$$
即在给定 $N(t) = n$ 的条件下，此前的 $N(s)$ 将转而服从**二项分布** $B\left( n, \cfrac{s}{t} \right)$，从而
$$
\mathbb{E} \left[ N(s) \mathop| N(t) \right] = N(t) \cdot \dfrac{s}{t}
$$
同样也是时间线性的，但不同的是，此时的**系数与 Poisson 过程的强度 $\lambda$ 无关**，因为 Poisson 过程的增量独立性使得过去的信息无法影响未来的分布，但已知的信息可以推测过去的分布。

### 事件间隔

由增量独立性和增量平稳性，我们只需研究从初态开始到第一个事件的间隔 $T_{1}$ 的分布，其定义为
$$
F_{T_{1}}(t) = P\{T_{1} \le t\} = P \left\{ N(t) \ge 1 \right\} = 1 - P \left\{ N(t) = 0 \right\} = 1 - \e^{-\lambda t}
$$
因此
$$
f_{T_{1}}(t) = \dfrac{\dif}{\dif t} F_{T_{1}}(t) = \lambda \e^{-\lambda t}, \qquad t \ge 0
$$
于是事件间隔均服从参数为 $\lambda$ 的**指数分布**，即 $\left\{ T_{k} \right\} \stackrel{\text{i.i.d}}{\sim} \text{Exp}(\lambda)$，有
$$
\mathbb{E}[T_{k}] = \dfrac{1}{\lambda}, \qquad \mathrm{Var}[T_{k}] = \dfrac{1}{\lambda^{2}}
$$

由独立性，容易得到事件间隔 $T_{1}, \cdots, T_{k}$ 的**联合概率密度函数**为
$$
f_{T_{1}, T_{2}, \cdots, T_{k}}(t_{1}, t_{2}, \cdots, t_{k}) = \prod\limits_{i=1}^{k} f_{T_{i}}(t_{i}) = \lambda^{k} \e^{-\lambda \sum\limits_{i=1}^{k} t_{i}}, \qquad t_{i} \ge 0
$$

### 等待时间

#### 等待时间的边缘分布

设第 $n$ 个事件发生的时间为 $S_{n} = \sum\limits_{k=1}^{n} T_{k}$。引入**特征函数 $\phi_{X}(\omega) = \mathbb{E}\left[ \e^{\J \omega X} \right]$**，则由事件间隔的独立性，有
$$
\phi_{T_{k}}(\omega) = \int_{0}^{\infty} \lambda \e^{-\lambda t} \cdot \e^{\J \omega t} \dif t = \dfrac{\lambda}{\lambda - \J \omega}  
\implies
\phi_{S_{n}}(\omega) = \left( \phi_{T_{k}}(\omega) \right)^{n} = \left( \dfrac{\lambda}{\lambda - \J \omega} \right)^{n}
$$
因此可以通过逆变换求得 **$S_{n}$ 的概率密度函数**为
$$
f_{S_{n}}(t) = \dint_{-\infty}^{\infty} \phi_{S_{n}}(\omega) \cdot \e^{-\J \omega t} \dfrac{\dif \omega}{2 \pi}
= \begin{cases}
\dfrac{\lambda (\lambda t)^{n - 1}}{(n - 1)!} \e^{-\lambda t}, & t \ge 0, \\
0, & t < 0
\end{cases}
$$
此为参数为 $(n, \lambda)$ 的 **Erlang 分布 (Erlang distribution)**。

> [!note] 等待时间分布与 Poisson 过程概率分布的转换
> 设 $N(t)$ 是参数为 $\lambda$ 的 Poisson 过程，第 $n$ 个事件发生的时间为 $S_{n}$，则有重要关系
> $$
> P\{ S_{n} \le t \} = P\{ N(t) \ge n \}, \qquad P\{ S_{n} > t \} = P\{ N(t) < n \}
> $$
> 
> 由此关系也可以导出等待时间的概率密度函数，即
> $$
> F_{S_{n}}(t) = P\{ S_{n} \le t \} = P\{ N(t) \ge n \} = \sum\limits_{k=n}^{\infty} P\{ N(t) = k \}
> = \sum\limits_{k=n}^{\infty} \dfrac{(\lambda t)^{k}}{k!} \e^{-\lambda t}
> $$
> $$
> \begin{align}
> f_{S_{n}}(t) = \dfrac{\dif}{\dif t} F_{S_{n}}(t) &= \sum\limits_{k=n}^{\infty} \left( \dfrac{\lambda (\lambda t)^{k-1}}{(k - 1)!} \e^{-\lambda t} - \dfrac{\lambda (\lambda t)^{k}}{k!} \e^{-\lambda t} \right) \\
> &= \dfrac{\lambda (\lambda t)^{n - 1}}{(n - 1)!} \e^{-\lambda t} + \lim\limits_{ n \to \infty } \dfrac{\lambda (\lambda t)^{n}}{n!} \e^{-\lambda t} = \dfrac{\lambda (\lambda t)^{n - 1}}{(n - 1)!} \e^{-\lambda t}
> \end{align}
> $$

为将 $n$ 推广为任意正实数，可引入 **$\boldsymbol{\varGamma}$ 函数 $\varGamma(\alpha) = \dint_{0}^{\infty} t^{\alpha - 1} \e^{-t} \dif t$** 替代阶乘，则 $S_{n}$ 的概率密度函数可写为
$$
f_{S_{n}}(t) = \begin{cases}
\dfrac{\lambda (\lambda t)^{n - 1}}{\varGamma(n)} \e^{-\lambda t}, & t \ge 0, \\
0, & t < 0
\end{cases}
$$
此即参数为 $(n, \lambda)$ 的 **$\boldsymbol{\varGamma}$ 分布 (Gamma distribution)**。

#### 等待时间的联合分布

可以用**微元法**导出 $S_{1},S_{2}, \cdots, S_{k}$ 的联合概率密度函数。设 $0 < t_{1} < t_{2} < \cdots < t_{k}$，并取足够小的正数 $h_{1}, \cdots, h_{k}$，有
$$
\begin{align}
&P \left\{ t_{1} \le S_{1} < t_{1} + h_{1}, t_{2} \le S_{2} < t_{2} + h_{2}, \cdots, t_{k} \le S_{k} < t_{k} + h_{k} \right\} \\
&= P \big\{ N(t_{1}) = 0, N(t_{1} + h_{1}) - N(t_{1}) = 1, N(t_{2}) - N(t_{1} + h_{1}) = 0, \cdots,  \\
&\hspace{2.6em} N(t_{k}) - N(t_{k-1} + h_{k-1}) = 0,N(t_{k} + h_{k}) - N(t_{k}) = 1 \big\} \\
&= P \left\{ N(t_{1}) = 0 \right\} \cdot P \left\{ N(t_{1} + h_{1}) - N(t_{1}) = 1 \right\}  \cdots \\
&\hspace{1.2em} \cdot P \left\{ N(t_{k}) - N(t_{k-1} + h_{k-1}) = 0 \right\} \cdot P \left\{ N(t_{k} + h_{k}) - N(t_{k}) = 1 \right\} \\
&= \e^{-\lambda t_{1}} \cdot (\lambda h_{1} \e^{-\lambda h_{1}}) \cdot \e^{-\lambda (t_{2} - t_{1} - h_{1})} \cdots (\lambda h_{k} \e^{-\lambda h_{k}}) \\
&= \lambda^{k} \e^{-\lambda (t_{k} + h_{k})} \cdot h_{1} h_{2} \cdots h_{k}  \\
&\xrightarrow{h_{i} \to 0} f_{S_{1}, S_{2}, \cdots, S_{k}}(t_{1}, t_{2}, \cdots, t_{k}) \cdot h_{1} h_{2} \cdots h_{k}
\end{align}
$$
因此，得到 **$S_{1}, S_{2}, \cdots, S_{k}$ 的联合概率密度函数**
$$
f_{S_{1}, S_{2}, \cdots, S_{k}}(t_{1}, t_{2}, \cdots, t_{k}) = \begin{cases}
\lambda^{k} \e^{-\lambda t_{k}}, & 0 < t_{1} < t_{2} < \cdots < t_{k}, \\
0, & \text{otherwise}
\end{cases}
$$

#### 等待时间的条件分布

给定 $N(t) = n$，考察前 $n$ 个事件发生时间的条件联合分布。同样由微元法，设 $0 < t_{1} < t_{2} < \cdots < t_{n} < t$，并取足够小的正数 $h_{1}, \cdots, h_{n}$，有
$$
\begin{align}
&P \left\{ t_{1} \le S_{1} < t_{1} + h_{1}, t_{2} \le S_{2} < t_{2} + h_{2}, \cdots, t_{n} \le S_{n} < t_{n} + h_{n} \mid N(t) = n \right\} \\
&= \dfrac{ P \left\{ t_{1} \le S_{1} < t_{1} + h_{1}, t_{2} \le S_{2} < t_{2} + h_{2}, \cdots, t_{n} \le S_{n} < t_{n} + h_{n}, N(t) = n \right\} }{ P \left\{ N(t) = n \right\} } \\
&= \dfrac{ P \left\{ N(t_{1}) = 0, N(t_{1} + h_{1}) - N(t_{1}) = 1, \cdots, N(t) - N(t_{n} + h_{n}) = 0 \right\} }{ P \left\{ N(t) = n \right\} } \\
&= \dfrac{ \lambda^{n} \e^{-\lambda (t_{n} + h_{n})} \cdot h_{1} h_{2} \cdots h_{n} \cdot \e^{-\lambda (t-t_{n} - h_{n})} }{ \dfrac{(\lambda t)^{n}}{n!} \e^{-\lambda t} } 
= \dfrac{ n! }{ t^{n} } \cdot h_{1} h_{2} \cdots h_{n}  \\
&\xrightarrow{h_{i} \to 0} f_{S_{1}, S_{2}, \cdots, S_{n} \mid N(t) = n}(t_{1}, t_{2}, \cdots, t_{n}) \cdot h_{1} h_{2} \cdots h_{n}
\end{align}
$$
即得到**条件联合概率密度函数**
$$
f_{S_{1}, S_{2}, \cdots, S_{n} \mid N(t) = n}(t_{1}, t_{2}, \cdots, t_{n}) = \begin{cases}
\cfrac{ n! }{ t^{n} }, & 0 < t_{1} < t_{2} < \cdots < t_{n} < t, \\
0, & \text{otherwise}
\end{cases}
$$

> [!note] 顺序统计量
> 设 $X_{1}, X_{2}, \cdots, X_{n}$ 是来自某一分布 $F_{X}(x)$ 的 $n$ 个**独立同分布**随机变量，则将它们按从小到大的顺序排列，记为 $Y_{1} \le Y_{2} \le \cdots \le Y_{n}$，即称 $\left\{ Y_{i} \right\}_{i=1}^{n}$ 为 $X_{1}, X_{2}, \cdots, X_{n}$ 的**顺序统计量 (order statistics)**。第 $k$ 顺序统计量 $Y_{k}$ 即为 $X_{1}, X_{2}, \cdots, X_{n}$ 中第 $k$ 小的值。
> 
> 对于两个极端情况，容易得到
> $$
> \begin{align}
> &F_{Y_{n}}(x) = \prod\limits_{i=1}^{n} P\{ X_{i} \le x \} = \left( F_{X}(x) \right)^{n} \\
> &F_{Y_{1}}(x) = 1 - \prod\limits_{i=1}^{n} P\{ X_{i} > x \} = 1 - \left( 1 - F_{X}(x) \right)^{n}
> \end{align}
> $$
> 对于一般的 $Y_{k}$，设有充分小的 $h$ 使得 $x < Y_{k} \le x + h$，即 $k-1$ 个 $X_{i}$ 落在 $(-\infty, x]$，1 个 $X_{i}$ 落在 $(x, x+h]$，其余 $n-k$ 个 $X_{i}$ 落在 $(x+h, +\infty)$，则有
> $$
> \begin{align}
> f_{Y_{k}}(x) &= \lim\limits_{ h \to 0 } \dfrac{ P \left\{ x < Y_{k} \le x + h \right\} }{ h } \\
> &= \lim\limits_{ h \to 0 } \dfrac{1}{h} \binom{n}{k-1} \binom{n - k + 1}{1} \binom{n - k}{n - k} \\
> &\hspace{3em} \cdot \left( F_{X}(x) \right)^{k - 1} \cdot \left( F_{X}(x + h) - F_{X}(x) \right) \cdot \left( 1 - F_{X}(x + h) \right)^{n - k} \\
> &= \binom{n}{k-1} \binom{n - k + 1}{1} ( F_{X}(x) )^{k - 1} ( 1 - F_{X}(x) )^{n - k}  f_{X}(x) \\
> \end{align}
> $$
> 同理，通过微元法拆分，可以得到**顺序统计量的联合概率密度函数**
> $$
> f_{Y_{1}, Y_{2}, \cdots, Y_{n}}(y_{1}, y_{2}, \cdots, y_{n}) = \begin{cases}
> n! \prod\limits_{i=1}^{n} f_{X}(y_{i}), & y_{1} < y_{2} < \cdots < y_{n}, \\
> 0, & \text{otherwise}
> \end{cases}
> $$
> 
> 注意到，$n$ 个在 $(0, t)$ 上**独立同分布**的**均匀分布**随机变量的**顺序统计量**的联合概率密度函数与上述条件联合概率密度函数形式完全相同，因此 **等待时间 $S_{1}, S_{2}, \cdots, S_{n}$ 在条件 $N(t) = n$ 下可视为 $n$ 个在 $(0, t)$ 上独立同分布的均匀分布随机变量的顺序统计量**。这意味着，就**总等待时间**而言，可以将 Poisson 过程视为在时间轴上随机均匀分布的事件集合。

对条件联合概率密度函数进行边缘化，有
$$
\begin{align} 
f_{S_{k} \mid N(t) = n}(s_{k}) &= \dint_{0}^{s_{k}} \dif s_{k-1} \dint_{0}^{s_{k-1}} \dif s_{k-2} \cdots \dint_{0}^{s_{2}} \dif s_{1} \cdot \dint_{s_{k}}^{t} \dif s_{k+1} \cdots \dint_{s_{n-1}}^{t} \dif s_{n} \\
&\hspace{1em} \cdot f_{S_{1}, S_{2}, \cdots, S_{n} \mid N(t) = n}(s_{1}, s_{2}, \cdots, s_{n}) \\
&= \dfrac{n!}{t^{n}} \cdot \dfrac{s_{k}^{k-1}}{(k-1)!} \dfrac{(t - s_{k})^{n - k}}{(n - k)!} \\
&= \dfrac{1}{t} \dfrac{n!}{(k-1)! (n - k)!} \left( \dfrac{s_{k}}{t} \right)^{k-1} \left( 1 - \dfrac{s_{k}}{t} \right)^{n - k},
\quad 0 < s_{k} < t
\end{align}
$$
这即为参数为 $(k, n-k+1, t)$ 的 **Beta 分布 (Beta distribution)**。利用 Beta 函数与 Gamma 函数的关系
$$
B(\alpha, \beta) = \dint_{0}^{1} t^{\alpha - 1} (1 - t)^{\beta - 1} \dif t = \dfrac{\varGamma(\alpha) \varGamma(\beta)}{\varGamma(\alpha + \beta)}
\stackrel{\alpha, \beta \in \mathbb{Z}_{+}}{=\!=\!=\!=\!=} \dfrac{(\alpha - 1)! (\beta - 1)!}{(\alpha + \beta - 1)!}
$$
可得
$$
\begin{align}
&\mathbb{E} \left[ S_{k} \mid N(t) = n \right] = \dfrac{k}{n+1} t, \quad \mathbb{E} \left[ S_{k}^{2} \mid N(t) = n \right] = \dfrac{k (k+1)}{(n+1)(n+2)} t^{2} \\
&\mathrm{Var} \left[ S_{k} \mid N(t) = n \right] = \dfrac{k (n - k + 1)}{(n + 1)^{2} (n + 2)} t^{2}
\end{align}
$$


## Poisson 过程的拓广

### 非齐次 Poisson 过程

对于某些实际问题，事件发生的强度并非恒定不变，而是随着时间变化的。为此，考虑**削弱 Poisson 过程的增量平稳性**，即不再有
$$
\Delta N(t) = N(t + \Delta t) - N(t) \stackrel{\text{d}}{=} N(\Delta t)
$$

此时，[[#^JumuHanshuDeDaoshu|概率母函数的导数式]]中 $N(\Delta t)$ 应全部保留为 $\Delta N(t)$，处理[[#零事件项的极限]]时不再有 $P\{\Delta N(t) = 0\} = \e^{-\lambda \Delta t}$，我们引入
$$
\lim\limits_{ \Delta t \to 0 } \dfrac{1}{\Delta t} \left( 1 - P\{\Delta N(t) = 0\} \right) = \lambda(t)
$$
对[[#单事件项的极限]]，仍有
$$
\dfrac{1 - P \left\{ \Delta N(t) = 0 \right\}}{\Delta t} = \dfrac{P \left\{ \Delta N(t) = 1 \right\}}{\Delta t} \left( 1 + \dfrac{P\left\{ \Delta N(t) \ge 2 \right\}}{P\left\{ \Delta N(t) = 1 \right\}} \right)
$$
且仍保留[[#^XishuxingJiashe|稀疏性假设]]
$$
\lim_{\Delta t \to 0} \dfrac{1}{\Delta t} \dfrac{P\left\{ \Delta N(t) \ge 2 \right\}}{P\left\{ \Delta N(t) = 1 \right\}} = 0
$$
因此有
$$
\lim\limits_{ \Delta t \to 0 } \dfrac{1}{\Delta t} P \left\{ \Delta N(t) = 1 \right\} = \lambda(t)
$$
这也使得 $\lambda(t)$ 可视为**事件发生速率**；类似地，[[#多事件项的极限]]仍为 $0$，故得到关于概率母函数的微分方程
$$
\dfrac{\dif}{\dif t} G_{N(t)}(z) = (-\lambda(t) + \lambda(t)z) G_{N(t)}(z), \qquad G_{N(0)}(z) = 1
$$
解得
$$
G_{N(t)}(z) = \exp\left( \dint_{0}^{t} \lambda(\tau) \dif \tau \cdot (z-1) \right) = \exp\left( z\dint_{0}^{t} \lambda(\tau) \dif \tau \right) \exp\left( -\dint_{0}^{t} \lambda(\tau) \dif \tau \right)
$$
故得
$$
P\left\{ N(t) = k \right\} = \dfrac{\left( \dint_{0}^{t} \lambda(\tau) \dif \tau \right)^{k}}{k!} \exp\left( - \dint_{0}^{t} \lambda(\tau) \dif \tau \right)
$$
当 $\lambda(t)$「齐次」为 $\lambda(t) \equiv \lambda$ 时，即得到 Poisson 分布的概率分布，故此分布称为**非齐次 Poisson 过程 (non-homogeneous Poisson Process)**。

类似于参数为 $\lambda$ 齐次 Poisson 过程 $N(t)$ 服从**参数为 $\lambda t$ 的 Poisson 分布**，事件发生速率为 $\lambda(t)$ 的非齐次 Poisson 过程 $N(t)$ 服从**参数为 $\dint_{0}^{t} \lambda(\tau) \dif \tau$ 的 Poisson 分布**，有
$$
\mathbb{E} \left[ N(t) \right] = \mathrm{Var} \left[ N(t) \right] = \dint_{0}^{t} \lambda(\tau) \dif \tau
$$

### 复合 Poisson 过程

#### 从事件「效果」引入复合 Poisson 过程

考虑**发生次数服从 Poisson 过程**的随机过程 $X(t) = \sum\limits_{k=1}^{N(t)} X_{k}$，其中单个事件的「效果」$\left\{ X_{k} \right\}_{k=1}^{\infty}$ 独立同分布且独立于 $N(t)$。

已知 $G_{N(t)}(z) = \mathbb{E} \left[ z^{N(t)} \right] = \e^{(-\lambda + \lambda z) t}$，若跳变量 $X_k$ 取非负整数值，则 $X(t)$ 的概率母函数为
$$
\begin{align}
G_{X(t)} (z) &= \mathbb{E} \left[ z^{X(t)} \right] = \mathbb{E} \left[ z^{\sum_{k=1}^{N(t)}X_{k}} \right] = \mathbb{E}_{N(t)} \left[ \mathbb{E}_{X_{k} \mid N(t)} \left[ z^{\sum_{k=1}^{n}X_{k}} \mathop{\Big|} N(t) = n \right]  \right] \\
&= \mathbb{E} \left[ \left( \mathbb{E} \left[ z^{X_{k}} \right] \right)^{N(t)}  \right] = G_{N(t)}(G_{X_{k}}(z)) = \e^{(-\lambda + \lambda G_{X_{k}}(z)) t}
\end{align}
$$
可见，$X(t)$ 的概率母函数是 $N(t)$ 的概率母函数与跳变量 $X_k$ 的概率母函数的复合。若 $X_k$ 不取非负整数值，则相同结构应改用特征函数。因此，该过程称为**复合Poisson过程 (compound Poisson process)**。

> [!example] [[例题 - Poisson过程#L14-1|L14-1]]：Poisson过程的独立稀释

> [!example] [[例题 - Poisson过程#L14-2|L14-2]]：Poisson过程的和与差

#### 从事件稀疏性引入复合 Poisson 过程

另一方面，对于某些实际问题，时间微元内出现 2 次或以上事件的概率不可忽略，需要考虑**削弱 Poisson [[#^XishuxingJiashe|稀疏性假设]]**，即设定
$$
P\left\{ X(\Delta t) = k \mid X(\Delta t) \ge 1 \right\} \xrightarrow{\Delta t \to 0} p_{k}
$$
这对[[#零事件项的极限]]没有影响；对[[#单事件项的极限]]和[[#多事件项的极限]]不再需要分开讨论，有
$$
\begin{align}
&\lim_{\Delta t \to 0} \dfrac{1}{\Delta t} \sum\limits_{k=1}^{\infty} P\left\{ X(\Delta t) = k \right\} \cdot z^{k}  \\
&= \lim_{\Delta t \to 0} \dfrac{1}{\Delta t} P\left\{ X(\Delta t) \ge 1 \right\} \cdot \sum\limits_{k=1}^{\infty} P\left\{ X(\Delta t) = k \mid X(\Delta t) \ge 1 \right\} \cdot z^{k} \\
&= \lim_{\Delta t \to 0} \dfrac{1}{\Delta t} (1 - P \left\{ X(\Delta t) = 0 \right\}) \underbrace{ \sum\limits_{k=1}^{\infty} p_{k} z^{k} }_{ P(z) }= \lambda P(z)
\end{align}
$$
即得到关于概率母函数的微分方程
$$
\dfrac{\dif}{\dif t} G_{X(t)}(z) = \lambda(P(z) - 1) G_{X(t)}(z), \qquad G_{X(0)}(z) = 1
$$
解得
$$
G_{X(t)}(z) = \exp\left( \lambda t (P(z) - 1) \right) = \exp\left( \lambda t P(z) \right) \exp\left( -\lambda t \right) = G_{N(t)}(P(z))
$$
此即上述复合Poisson过程的概率母函数。

### 过滤 Poisson 过程

在复合 Poisson 过程中，若将事件「效果」看作是由 $\left\{ X_{k} \right\}_{k=1}^{\infty}$ 决定的**某个随机系统的输出**，则该过程可视为**过滤 Poisson 过程 (filtered Poisson process)**。设该随机系统的**冲激响应 (impulse response)** 为 $h(t; x)$，则系统输出为
$$
Y(t) = \sum\limits_{k=1}^{N(t)} h(t - S_{k}; X_{k})
$$
其中 $S_{k} = \sum\limits_{i=1}^{k} T_{i}$ 为第 $k$ 个事件发生的时间，$T_{i}$ 为事件间隔。

**$Y(t)$ 的特征函数**为
$$
\begin{align}
\phi_{Y(t)}(\omega) &= \mathbb{E} \left[ \e^{\J \omega Y(t)} \right] = \mathbb{E} \left[ \exp\left( \J \omega \sum\limits_{k=1}^{N(t)} h(t - S_{k}; X_{k}) \right) \right] \\
&= \mathbb{E}_{N(t)} \left[ \mathbb{E}_{\{S_{k}, X_{k}\}} \left[ \exp\left( \J \omega \sum\limits_{k=1}^{n} h(t - S_{k}; X_{k}) \right) \mathop{\Bigg|} N(t) = n \right]  \right] \\
&= \mathbb{E}_{N(t)} \left[ \mathbb{E}_{\{U_{k}, X_{k}\}} \left[ \prod\limits_{k=1}^{n} \e^{ \J \omega h(t - U_{k}; X_{k}) } \mathop{\Bigg|} N(t) = n \right]  \right] \\
&= \mathbb{E}_{N(t)} \left[ \left( \dint_{0}^{t} \mathbb{E}_{X_{k}} \left[ \e^{ \J \omega h(t - u; X_{k}) } \right] \dfrac{1}{t} \dif u \right)^{N(t)}  \right] \\
&\stackrel{\mathbb{E} \left[ z^{N(t)} \right] = \e^{\lambda t (z-1)}}{=\!=\!=\!=\!=\!=\!=\!=\!=} \exp\left( \lambda t \left( \dint_{0}^{t} \mathbb{E} \left[ \e^{ \J \omega h(t - u; X_{k}) } \right] \dfrac{1}{t} \dif u - 1 \right) \right) \\
&= \exp\left( \lambda \dint_{0}^{t} \left( \mathbb{E} \left[ \e^{ \J \omega h(t - u; X_{k}) } \right] - 1 \right) \dif u \right)
\end{align}
$$
其中 $\{U_{k}\}$ 为在 $(0, t)$ 上独立同分布的均匀分布随机变量，其顺序统计量即为条件 $N(t) = n$ 下的 $\{S_{k}\}$，在求和意义下二者等价。

由特征函数，容易得到 $Y(t)$ 的**均值与方差**
$$
\mathbb{E} \left[ Y(t) \right] = \lambda \dint_{0}^{t} \mathbb{E} \left[ h(t - u; X_{k}) \right] \dif u, \quad
\mathrm{Var} \left[ Y(t) \right] = \lambda \dint_{0}^{t} \mathbb{E} \left[ h^{2}(t - u; X_{k}) \right] \dif u
$$
若事件的影响是**因果**的，即 $h(t; x) = 0$ 对 $t < 0$ 成立，则用类似的方法可以计算过滤 Poisson 过程的二维特征函数
$$
\begin{align}
\phi_{Y(t_{1}), Y(t_{2})}(\omega_{1}, \omega_{2}) &= \mathbb{E} \left[ \e^{\J \omega_{1} Y(t_{1}) + \J \omega_{2} Y(t_{2})} \right] \\
&= \exp\left( \lambda \dint_{0}^{\max\{t_{1}, t_{2}\}} \left( \mathbb{E} \left[ \e^{ \J \omega_{1} h(t_{1} - u; X_{k}) + \J \omega_{2} h(t_{2} - u; X_{k}) } \right] - 1 \right) \dif u \right)
\end{align}
$$
从而得到**协方差函数**
$$
C_{Y}(t_{1}, t_{2}) = \lambda \dint_{0}^{\min\{t_{1}, t_{2}\}} \mathbb{E} \left[ h(t_{1} - u; X_{k}) h(t_{2} - u; X_{k}) \right] \dif u
$$

特别地，**波形 $h$ 不具有随机性**时，有
$$
\begin{align}
&\phi_{Y(t)}(\omega) = \exp\left( \lambda \dint_{0}^{t} \left( \e^{ \J \omega h(t - u) } - 1 \right) \dif u \right), \\
&\mathbb{E} \left[ Y(t) \right] = \lambda \dint_{0}^{t} h(t - u) \dif u, \quad \mathrm{Var} \left[ Y(t) \right] = \lambda \dint_{0}^{t} h^{2}(t - u) \dif u, \\
&C_{Y}(t_{1}, t_{2}) = \lambda \dint_{0}^{\min\{t_{1}, t_{2}\}} h(t_{1} - u) h(t_{2} - u) \dif u
\end{align}
$$
