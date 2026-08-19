## L14 (11/18)

### L14-1

**Poisson 过程的独立稀释。**

设自某时刻起走进学校的学生数服从参数为 $\lambda$ 的 Poisson 过程，其中每个学生独立以概率 $p$ 为男生，$1-p$ 为女生。求在时间 $t$ 内走进学校的男生数的分布。

对第 $k$ 个走进学校的学生，记 $X_{k} = \begin{cases}1, &\text{if Male}, \\ 0, &\text{if Female}\end{cases}$，则 **$X_{k} \stackrel{\text{i.i.d}}{\sim} \begin{pmatrix}1 & 0 \\ p &1-p \end{pmatrix}$**，时间 $t$ 内走进学校的男生数为 **$X(t) = \sum\limits_{k=1}^{N(t)} X_{k}$**，其中 $N(t) \sim \text{Poisson}(\lambda t)$。$X(t)$ 为一个[[Poisson 过程#复合 Poisson 过程|复合 Poisson 过程]]，其概率母函数为
$$
\begin{align} 
G_{X(t)}(z) &= G_{N(t)}(G_{X_{k}}(z)) = \exp(\lambda t(G_{X_{k}}(z) - 1)) \\
&= \exp(\lambda t(pz^{1} + (1-p)z^{0} - 1)) = \exp(\lambda p t  (z-1))
\end{align}
$$
因此，时间 $t$ 内走进学校的男生数是一个**参数为 $\lambda p$ 的 Poisson 过程**。

进一步地，可见**从参数为 $\lambda$ 的 Poisson 过程中独立地以概率 $p$ 抽取事件，得到的子过程是参数为 $\lambda p$ 的 Poisson 过程**。

### L14-2

**Poisson 过程的和与差。**

设 $N_{1}(t)$ 和 $N_{2}(t)$ 是两个独立的 Poisson 过程，参数分别为 $\lambda_{1}$ 和 $\lambda_{2}$。求 $N(t) = N_{1}(t) + N_{2}(t)$ 和 $M(t) = N_{1}(t) - N_{2}(t)$ 的分布。

对二者之和 $N(t)$，其概率母函数为
$$
\begin{align}
G_{N(t)}(z) &= \mathbb{E} \left[ z^{N(t)} \right] = \mathbb{E} \left[ z^{N_{1}(t) + N_{2}(t)} \right] = \mathbb{E} \left[ z^{N_{1}(t)} \right] \mathbb{E} \left[ z^{N_{2}(t)} \right]   \\
&= G_{N_{1}(t)}(z) \cdot G_{N_{2}(t)}(z) = \exp(\lambda_{1} t (z-1)) \cdot \exp(\lambda_{2} t (z-1)) \\
&= \exp((\lambda_{1} + \lambda_{2}) t (z-1))
\end{align}
$$
即 $N(t)$ 是一个**参数为 $\lambda_{1} + \lambda_{2}$ 的 Poisson 过程**。

对二者之差 $M(t)$，显然 $P \left\{ M(t) < 0 \right\} > 0$，其Laurent型生成函数为
$$
\begin{align}
G_{M(t)}(z) &= \mathbb{E} \left[ z^{M(t)} \right] = \mathbb{E} \left[ z^{N_{1}(t) - N_{2}(t)} \right] = \mathbb{E} \left[ z^{N_{1}(t)} \right] \mathbb{E} \left[ z^{-N_{2}(t)} \right]   \\
&= G_{N_{1}(t)}(z) \cdot G_{N_{2}(t)}\left( \dfrac{1}{z} \right) = \exp(\lambda_{1} t (z-1)) \cdot \exp\left(\lambda_{2} t \left(\dfrac{1}{z} - 1\right)\right) \\
&= \exp\left(\lambda_{1} t (z-1) + \lambda_{2} t \left(\dfrac{1}{z} - 1\right)\right) \\
&= \exp\left((\lambda_{1} + \lambda_{2}) t \left(\dfrac{\lambda_{1}}{\lambda_{1} + \lambda_{2}} z^{1} + \dfrac{\lambda_{2}}{\lambda_{1} + \lambda_{2}} z^{-1} - 1\right)\right)
\end{align}
$$
可见 $M(t)$ 不是 Poisson 过程，而是一个**复合 Poisson 过程**，其每次跳变的增量服从分布 $\begin{pmatrix}1 & -1 \\ \cfrac{\lambda_{1}}{\lambda_{1} + \lambda_{2}} & \cfrac{\lambda_{2}}{\lambda_{1} + \lambda_{2}} \end{pmatrix}$，跳变发生的次数服从参数为 $\lambda_{1} + \lambda_{2}$ 的 Poisson 过程。

### L14-3

**公交到站问题。**

设某公交车到站的事件服从参数为 $\lambda$ 的 Poisson 过程。

1. 从第 2 次公交车到站开始算起，5 min 内有第 4 次公交车到站的概率为
$$
\begin{align} 
P \left\{ N(5) - N(0) \ge 2 \right\} &= 1 - P \left\{ N(5) = 0 \right\} - P \left\{ N(5) = 1 \right\}  \\
&= 1 - \e^{-5\lambda} - 5\lambda \e^{-5\lambda} 
\end{align}
$$

2. 已知 10 min 内有 20 辆车到站，求至第 15 min 时累计到站的公交车数 $X$ 的分布。
考虑 $X = ( N(15) \mid N(10) = 20) = 20 + (N(15) - N(10) \mid N(10) = 20)$，由 Poisson 过程的**增量独立性**，其中 $N(15) - N(10) \sim \text{Poisson}(5\lambda)$ 与 $N(10)$ 独立，因此
$$
\begin{align} 
P \left\{ X = k \right\} &= P \left\{ N(15) - N(10) = k-20 \right\}  \\
&= \begin{cases}
0, & k < 20,  \\
\dfrac{(5\lambda)^{k-20}}{(k-20)!} \e^{-5\lambda}, & k \ge 20
\end{cases} 
\end{align}
$$

3. 已知 10 min 内有 20 辆车到站，20 min 内累计有 60 辆车到站，求至第 15 min 时累计到站的公交车数 $X$ 的分布。
此即，已知 $[0, 10]$ 时间内有 20 辆车到站（记为 **$[0, 10] = 20$**）、$[10, 20]$ 时间内有 40 辆车到站（记为 **$[10, 20] = 40$**），求 $[10, 15] = X - 20$ 的概率分布。由**增量独立性**，有
$$
\begin{align}
P \left\{ X = k \right\} &= P \left\{ [10, 15] = k - 20 \mid [0, 10] = 20, [10, 20] = 40 \right\} \\
&= \dfrac{P \left\{ [10, 15] = k - 20, [0, 10] = 20, [10, 20] = 40 \right\}}{P \left\{ [0, 10] = 20, [10, 20] = 40 \right\}} \\
&= \dfrac{\cancel{P \left\{ [0, 10] = 20 \right\}} \cdot P \left\{ [10, 15] = k - 20 \right\} \cdot P \left\{ [15, 20] = 60 - k \right\}}{\cancel{ P \left\{ [0, 10] = 20 \right\} } \cdot P \left\{ [10, 20] = 40 \right\}} \\
&= \cfrac{\dfrac{(5\lambda)^{k-20}}{(k-20)!} \e^{-5\lambda} \cdot \dfrac{(5\lambda)^{60-k}}{(60-k)!} \e^{-5\lambda}}{\dfrac{(10\lambda)^{40}}{40!} \e^{-10\lambda}} = \dfrac{40!}{(k-20)!(60-k)!} \left(\dfrac{1}{2}\right)^{40}
\end{align}
$$

4. 该站点有 3 路公交停靠，概率分别为 $\cfrac{1}{2}$、$\dfrac{1}{3}$ 和 $\dfrac{1}{6}$。已知 10 min 内有 30 辆车到站，求 3 路公交车各有 10 辆到站的概率。
3 路公交车到站的事件**各自服从参数为 $\cfrac{\lambda}{2}$、$\dfrac{\lambda}{3}$ 和 $\dfrac{\lambda}{6}$ 的 Poisson 过程**，记 $N_{1}(t)$、$N_{2}(t)$ 和 $N_{3}(t)$ 分别为 3 路公交车在时间 $t$ 内到站的次数。它们相互独立，因此所求为
$$
\begin{align}
&P \left\{ N_{1}(10) = 10, N_{2}(10) = 10, N_{3}(10) = 10 \mid N(10) = 30 \right\} \\
&= \dfrac{P \left\{ N_{1}(10) = 10 \right\} \cdot P \left\{ N_{2}(10) = 10 \right\} \cdot P \left\{ N_{3}(10) = 10 \right\}}{P \left\{ N(10) = 30 \right\}} \\
&= \cfrac{\dfrac{(10 \cdot \lambda/2)^{10}}{10!} \e^{-10 \cdot \lambda/2} \cdot \dfrac{(10\cdot\lambda/3)^{10}}{10!} \e^{-10\cdot \lambda/3} \cdot \dfrac{(10 \cdot \lambda/6)^{10}}{10!} \e^{-10\cdot\lambda/6}}{\dfrac{(10\lambda)^{30}}{30!} \e^{-10\lambda}}  \\
&= \dfrac{30!}{(10!)^{3}} \left(\dfrac{1}{6}\right)^{10} \left(\dfrac{1}{3}\right)^{10} \left(\dfrac{1}{2}\right)^{10}
\end{align}
$$

5. 已知 1 min 内有 2 辆车到站，则第 4 辆车到站的时间 $S_{4}$ 的分布为
$$
\begin{align}
F_{S_{4} \mid N(1) = 2}(t) &= P \left\{ S_{4} \le t \mid N(1) = 2 \right\} = \dfrac{P \left\{ S_{4} \le t, N(1) = 2 \right\}}{P \left\{ N(1) = 2 \right\}} \\
&= \dfrac{P \left\{ N(t) - N(1) \ge 2 \} \cdot P \{ N(1) = 2 \right\}}{P \left\{ N(1) = 2 \right\}} = P \left\{ N(t) - N(1) \ge 2 \right\} \\
&= 1 - P \left\{ N(t) - N(1) = 0 \right\} - P \left\{ N(t) - N(1) = 1 \right\} \\
&= \begin{cases}
0, & t \le 1, \\
1 - \e^{-\lambda (t-1)} - \lambda (t-1) \e^{-\lambda (t-1)}, & t > 1
\end{cases}
\end{align}
$$
因此其期望为
$$
\begin{align}
\mathbb{E} \left[ S_{4} \mid N(1) = 2 \right] &= \dint_{0}^{\infty} (1 - F_{S_{4} \mid N(1) = 2}(t)) \dif t \\
&= \dint_{1}^{\infty} \left( \e^{-\lambda (t-1)} + \lambda (t-1) \e^{-\lambda (t-1)} \right) \dif t = \dfrac{2}{\lambda} + 1
\end{align}
$$

## L15 (11/25)

### L15-1

**一般时间条件下 Poisson 过程的分布。**

我们已知Poisson过程两次事件之间的[[Poisson 过程#事件间隔|事件间隔分布]]为指数分布，即设 $N(t)$ 是参数为 $\lambda$ 的Poisson过程，**已知 $S_{n}$** 时，$(S_{n+1} - S_{n}) \mid S_{n} \stackrel{\text{d}}{=} S_{n+1} - S_{n} \sim \mathrm{Exp}(\lambda)$。

考虑**已知 $N(t_{0}) = n$**，尝试求出此时下一个事件发生时间的分布。一个直观的想法是
$$
P \left\{ S_{N(t_{0})+1} - S_{N(t_{0})} \le x \mid N(t_{0}) = n \right\} \stackrel{\text{?}}{=} P \left\{ S_{n+1} - S_{n} \le x \right\} = 1 - \e^{-\lambda x}
$$
但实际上并不成立。因为**已知 $N(t_{0}) = n$** 相当于**已知 $S_{n} \le t_{0} < S_{n+1}$**，即已知了**从 $S_{n}$ 到 $t_{0}$ 之间没有事件发生**，这会影响下一个事件发生时间的分布。

记 $\begin{cases}A(t_{0}) = S_{N(t_{0})+1} - t_{0}, \\ B(t_{0}) = t_{0} - S_{N(t_{0})}\end{cases}$，则有
$$
P\left\{ A(t_{0}) > x, B(t_{0}) > y \right\} = P \left\{ N(x + y) = 0 \right\} = \e^{-\lambda (x+y)}
$$
因此，对任意的 $t_{0}$，有
$$
\begin{align} 
&P \left\{ A(t_{0}) \le x \right\} = 1 - P \left\{ A(t_{0}) > x \right\} = 1 - P \left\{ A(t_{0}) > x, B(t_{0}) > 0 \right\} = 1 - \e^{-\lambda x} \\
&P \left\{ B(t_{0}) \le y \right\} = 1 - P \left\{ B(t_{0}) > y \right\} = 1 - P \left\{ A(t_{0}) > 0, B(t_{0}) > y \right\} = 1 - \e^{-\lambda y} 
\end{align}
$$
二者独立，且均服从参数为 $\lambda$ 的指数分布。

### L15-2

**固定时间内 Poisson 过程的事件数。**

设 $N(t)$ 是参数为 $\lambda$ 的 Poisson 过程，**已知 $N(t_{0}) = n$**，求在时间区间 $(0, t_{0}]$ 内事件发生的时间点的分布。

显然这就是[[Poisson 过程#等待时间的条件分布|等待时间的条件分布]]，条件联合概率密度函数为
$$
f_{S_{1}, S_{2}, \cdots, S_{n} \mid N(t) = n}(t_{1}, t_{2}, \cdots, t_{n}) = \begin{cases}
\cfrac{ n! }{ t^{n} }, & 0 < t_{1} < t_{2} < \cdots < t_{n} < t, \\
0, & \text{otherwise}
\end{cases}
$$


## L17 (12/02)

### L17-1

某公交站 $[0,T]$ 内共来 $n$ 辆公交车，乘客以参数 $\lambda$ 的 **Poisson 分布** $N(t)$ 到来，每次车到站时将站台所有乘客接走，求使得**平均总等待时间最小**的发车安排。

不妨考虑第一次来车前的情况。设在 $[0,t]$ 内未来车，则乘客的总等待时间为
$$
Y(t) = \sum\limits_{i=1}^{N(t)} (t - \tau_{i})
$$
平均总等待时间即 $Y(t)$ 的期望为
$$
\begin{align} 
\mathbb{E} \left[ Y(t) \right] &= \mathbb{E} \left[ tN(t) - \sum\limits_{i=1}^{N(t)} \tau_{k} \right] = t \mathbb{E} \left[ N(t) \right] - \mathbb{E} \left[ \sum\limits_{i=1}^{N(t)} \tau_{k} \right] \\
&= t \cdot \lambda t - \mathbb{E}_{N(t)} \left[ \mathbb{E}_{\tau \mid N(t)} \left[ \sum\limits_{k=1}^{n} \tau_{k} \mathop{\Bigg|} N(t) = n \right]  \right] = \lambda t^{2} - \dfrac{\lambda}{2}t^{2} = \dfrac{\lambda}{2} t^{2}
\end{align}
$$

这样，设每个发车间隔为 $t_{i}$，则最小化总平均等待时间即在**约束条件 $\sum\limits_{i=1}^{n} t_{i} = T$** 下最小化**凸的**目标函数 $\sum\limits_{i=1}^{n} \cfrac{\lambda}{2} t_{i}^{2}$。由凸优化的**均值不等式**可知，当 $t_{1} = t_{2} = \cdots = t_{n} = \cfrac{T}{n}$ 时取得最小值。

### L17-2

某公园游客的**进入**服从参数 $\lambda$ 的 Poisson 分布 $N(t)$，每个游客的停留时间独立同分布地服从 $f(t)$。设 $Y(t)$ 表示 $t$ 时刻园内游客人数，求 $\mathbb{E} \left[ Y(t) \right]$。

此问题重在**表示出 $Y(t)$**，即需要给出游客的**离开**的分布。不妨先写出
$$
Y(t) =\sum\limits_{k=1}^{N(t)} Y_{k}(t, \tau_{k}), \qquad Y_{k}(t, \tau_{k}) = \begin{cases}
1, & 0 \le t-\tau_{k} \le T_{k}, \\
0, & \text{otherwise}
\end{cases}
$$
其中 $T_{k}$ 就是游客的停留时间，即 $T_{k} \stackrel{\text{i.i.d}}{\sim} f(t)$。

引入特征函数，有
$$
\phi_{Y(t)} (\omega) = \exp\left( \lambda \dint_{0}^{t} (\mathbb{E} \left[ \exp(\J \omega Y_{1}(t,\tau)) \right] - 1 ) \dif \tau \right)
$$
进而
$$
\mathbb{E} \left[ Y(t) \right] = \dfrac{1}{\J} \dfrac{ \partial }{ \partial \omega } \phi_{Y(t)}(\omega) \Big|_{\omega=0} = \lambda \dint_{0}^{t} \mathbb{E} \left[ Y_{1}(t, \tau_{1}) \right] \dif \tau_{1}
$$
当 $t > \tau_{1}$ 时 $Y_{1}(t, \tau_{1})$ 才计入 $Y(t)$ 求和式，此时有
$$
\mathbb{E} \left[ Y_{1}(t, \tau_{1}) \right] = P \left\{ Y_{1}(t, \tau_{1}) = 1 \right\} = P \left\{ T_{1} > t - \tau_{1} \right\} = \dint_{t-\tau_{1}}^{\infty} f(s) \dif s
$$
代入即可。

### L17-3

对参数为 $\lambda$ 的 Poisson 分布 $N(t)$，前两个事件时刻为 $S_{1}$、$S_{2}$。

求 $\mathbb{E} \left[ S_{1} + S_{2} \right]$：直接由期望的线性性质得到 $\mathbb{E} \left[ S_{1} + S_{2} \right] = \cfrac{3}{\lambda}$。

求 $\mathbb{E} \left[ S_{1}S_{2} \right]$：由**增量独立性**，
$$
\mathbb{E} \left[ S_{1}S_{2} \right] = \mathbb{E} \left[ S_{1}(S_{2}-S_{1}+S_{1}) \right] = \mathbb{E} \left[ S_{1} \right] \mathbb{E} \left[ S_{2} - S_{1} \right] + \underbrace{ \mathrm{Var}(S_{1}) + (\mathbb{E} \left[ S_{1} \right] )^{2} }_{ \mathbb{E} \left[ S_{1}^{2} \right]  } = \dfrac{3}{\lambda^{2}}
$$

求 $\mathbb{E} \left[ S_{1} \mid N(t) \ge 1 \right]$：考虑 $S_{1} \mid N(t) \ge 1$ 的条件分布函数 $F_{S_{1} \mid N(t) \ge 1}(x)$，注意到必然有 $t \ge S_{1}$，则限定 $x \le t$，有
$$
\begin{align} 
F_{S_{1} \mid N(t) \ge 1}(x) &= P \left\{ S_{1} \le x \mid N(t) \ge 1 \right\} = \dfrac{P \left\{ S_{1} \le x, N(t) \ge 1 \right\}}{P \left\{ N(t) \ge 1 \right\}} \\
&= \dfrac{P \left\{ N(x) \ge 1, N(t) \ge 1 \right\}}{P \left\{ N(t) \ge 1 \right\}} = \dfrac{P \left\{ N(x) \ge 1 \right\}}{P \left\{ N(t) \ge 1 \right\}} = \dfrac{1 - \e^{-\lambda x}}{1 - \e^{-\lambda t}} 
\end{align}
$$
进而
$$
f_{S_{1} \mid N(t) \ge 1}(x) = \dfrac{\dif}{\dif x} F_{S_{1} \mid N(t) \ge 1}(x) = \dfrac{\lambda \e^{-\lambda x}}{1 - \e^{-\lambda t}}, \qquad 0 \le x \le t
$$
因此
$$
\mathbb{E} \left[ S_{1} \mid N(t) \ge 1 \right] = \dint_{0}^{t} x f_{S_{1} \mid N(t) \ge 1}(x) \dif x = \dfrac{1}{\lambda} - \dfrac{t \e^{-\lambda t}}{1 - \e^{-\lambda t}}
$$

