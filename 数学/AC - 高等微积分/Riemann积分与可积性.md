## Riemann积分与可积性

Riemann积分把区间分割、取样和加权求和的极限作为整体累积量。定义中的关键是：当分割步长足够小时，所有取点方式都必须得到同一极限。

积分性质建立在可积性之上。Darboux和、振幅判据和Lebesgue判别准则从不同角度回答可积性问题，并说明连续、逐段连续和单调函数为何可积。

本章属于[[一元积分学]]，依赖[[一元函数的极限与连续|极限与连续性]]；确认可积后，才能使用[[微积分基本定理与定积分计算|基本定理和计算公式]]。

### Riemann积分

> [!definition] Riemann积分
> 给定区间 $[a,b]$，称 $P:~a=x_0<x_1<\cdots <x_n=b$ 为 $[a,b]$ 的一个**分割**，它将 $[a,b]$ 分成内部不相交的小区间 $\Delta_i=[x_{i-1},x_i]$（$1\le i\le n$），每个小区间的长度为 $\Delta x_i = x_i-x_{i-1}$，称 $\lambda(P)=\max\limits_{1\le i\le n}\Delta x_i$ 为 $P$ 的**步长**。
>
> 任取 $\xi_i\in[x_{i-1},x_i]$（$1\le i\le n$），称 $\xi=\{\xi_1,\ldots,\xi_n\}$ 为分割 $P$ 的**取点**，给出取点 $\xi$ 的分割 $P$ 称为 $[a,b]$ 的**带点分割**，记作 $(P,\xi)$。
>
> 设 $f:[a,b]\rightarrow\mathbb{R}$ 为函数。对 $[a,b]$ 的带点分割 $(P,\xi)$，令 $\sigma(f;P,\xi):=\sum\limits_{i=1}^n f(\xi_i)\Delta x_i$，称 $\sigma(f;P,\xi)$ 为 $f$ 关于带点分割 $(P,\xi)$ 的 **Riemann和**。
>
> 如果存在 $I\in\mathbb{R}$，使得 $\forall \varepsilon>0$，$\exists \delta>0$，对于 $[a,b]$ 的任意带点分割 $(P,\xi)$，当 $\lambda(P)<\delta$ 时，都有 $|\sigma(f;P,\xi)-I|<\varepsilon$，那么记 $I=\lim\limits_{\lambda(P)\rightarrow 0}\sigma(f;P,\xi)=\lim\limits_{\lambda(P)\rightarrow 0}\sum\limits_{i=1}^n f(\xi_i)\Delta x_i$，并称 $I$ 为 $f$ 在 $[a,b]$ 上的**定积分**（或称 **Riemann积分**），记作 $I=\displaystyle{\int_{a}^{b}f(x) \dif x}$；称 $f$ 在 $[a,b]$ 上 **Riemann可积**，记作 $f\in \mathscr{R}[a,b]$。

由此，函数 $f$ 在 $[a,b]$ 上**不可积**当且仅当 $\forall I\in\mathbb{R}$，$\exists \varepsilon_0>0$ 使得 $\forall \delta>0$，存在 $[a,b]$ 的带点分割 $(P,\xi)$ 满足 $\lambda(P)<\delta$，但有 $|\sigma(f;P,\xi)-I|\ge \varepsilon_0$。

> [!example]+
> 在 $[0,1]$ 上定义 **Dirichlet函数**
> $$
> D(x)=\left\{ \begin{array}{ll}
> 0, &  x\in \mathbb{Q}, \\ 1, & x \notin \mathbb{Q},
> \end{array} \right.
> $$
> 证明 $D \notin \mathscr{R}[0,1]$。
>
> ---
>
> **证明：** 用反证法。假设 $D$ 可积，即存在 $I \in \mathbb{R}$ 为其积分。令 $\varepsilon=\dfrac{1}{4}$，于是由可积性可知，$\exists \delta>0$ 使得对于 $[0,1]$ 的任意带点分割 $(P,\xi)$，当 $\lambda(P)<\delta$ 时，都有 $|\sigma(D;P,\xi)-I|<\dfrac{1}{4}$。
>
> 选取 $n = \left[\dfrac{1}{\delta}\right]+1$，$P: 0=x_0<x_1<\cdots<x_n=1$ 为 $[0,1]$ 的均匀分割，则 $\lambda(P)=\dfrac{1}{n}<\delta$。再取点 $\xi=\{\xi_i\}_{1\le i\le n}$，$\xi'=\{\xi'_i\}_{1\le i\le n}$，使得对 $1\le i\le n$，均有 $\xi_i\in [x_{i-1},x_i]\cap\mathbb{Q}$，$\xi_i'\in [x_{i-1},x_i]\setminus\mathbb{Q}$，那么由上面假设有 $|\sigma(D;P,\xi)-I|<\dfrac{1}{4}$，$|\sigma(D;P,\xi')-I|<\dfrac{1}{4}$。
>
> 注意到
> $$
> \sigma(D;P,\xi)=\sum_{i=1}^nD(\xi_i)\Delta x_i=0
> \qquad
> \sigma(D;P,\xi')=\sum_{i=1}^nD(\xi'_i)\Delta x_i =\sum_{i=1}^n\Delta x_i=1
> $$
> 于是 $|I|<\dfrac{1}{4}$，$|1-I|<\dfrac{1}{4}$，从而我们有 $\dfrac{1}{2}>|I|+|1-I|\ge |I+(1-I)|=1$，矛盾。故不存在 $I$ 为上述积分，即所证结论成立。

定义仅讨论了上限 $b$ 大于下限 $a$ 的情况，我们约定 $\int_b^a f(x) \dif x=-\int_a^b f(x) \dif x$，$\int_a^a f(x) \dif x=0$。

### 定积分的性质

**Riemann积分的线性性。**
设函数 $f,g\in\mathscr{R}[a,b]$，而 $\alpha,\beta\in\mathbb{R}$，则 $\alpha f+\beta g\in\mathscr{R}[a,b]$，且
$$
\int_a^b\big(\alpha f(x)+\beta g(x)\big)\dif x=\alpha\int_a^b f(x)\dif x+\beta \int_a^b g(x)\dif x
$$

**有限点改值不影响积分** $\quad$ 如果 $f\in \mathscr{R}[a,b]$，则在有限多个点处改变 $f$ 的取值，既不改变可积性，也不改变积分。

**可积函数的有界性。**
若 $f\in \mathscr{R}[a,b]$，则 $f$ 在 $[a,b]$ 上有界。

**积分区间的可加性。**
设 $f : [a,b]\rightarrow \mathbb{R}$ 为函数，而 $c\in (a,b)$，则 $f$ 在 $[a,b]$ 上可积当且仅当 $f$ 分别在 $[a,c]$、$[c,b]$ 上可积；此时
$$
\int_a^b f(x)\dif x=\int_a^c f(x)\dif x+\int_c^b f(x)\dif x
$$
由上面的约定，这个定理对任意取的 $a,b,c \in \mathbb{R}$ 都成立。

**保序性。**
若 $f,g \in \mathscr{R}[a,b]$，且 $f \ge g$，则 $\int_a^b f(x) \dif x \ge \int_a^b g(x) \dif x$。

**严格保序性。**
若 $f,g \in \boldsymbol{\mathscr{C}[a,b]}$，且 $f \ge g$，则 $\int_a^b f(x) \dif x \ge \int_a^b g(x) \dif x$，等号成立当且仅当 $f \equiv g$。

> [!example]+
> 若 $f \in \mathscr{C}[a-1,b+1]$（$a<b$），求证 $\lim\limits_{t \to 0} \int_a^b |f(x+t) - f(x)| \dif x=0$。
>
> ---
>
> **证明：** 由于 $f\in\mathscr{C}[a-1,b+1]$，则 $f$ 一致连续，从而 $\forall \varepsilon>0$，$\exists \delta_1>0$，使得 $\forall x,y\in [a-1,b+1]$，当 $|x-y|<\delta_1$ 时，我们有 $|f(x)-f(y)|<\dfrac{\varepsilon}{b-a}$。令 $\delta=\min\left(\delta_1,\frac{1}{2}\right)$，于是 $\forall x\in [a,b]$ 以及 $\forall t\in\mathbb{R}$，当 $|t|<\delta$ 时，均有 $|f(x+t)-f(x)|<\dfrac{\varepsilon}{b-a}$，故
> $$
> \int_a^b|f(x+t)-f(x)|\dif x<\frac{\varepsilon}{b-a}\cdot (b-a)=\varepsilon
> $$
> 则 $\lim\limits_{t \to 0} \int_a^b |f(x+t) - f(x)| \dif x=0$。

**绝对值三角不等式的推广。**
若 $f\in \mathscr{R}[a,b]$，则 $|f| \in \mathscr{R}[a,b]$，且 $\left| \int_a^b f(x) \dif x \right| \le \int_a^b |f(x)| \dif x$。

**Cauchy-Schwarz-Buniakowsky不等式（Cauchy不等式的积分形式）。**
若 $f,g \in \mathscr{R}[a,b]$，则
$$
\left(\int_a^b f(x)g(x) \dif x\right)^2 \le \left(\int_a^b f^2(x) \dif x\right)\left(\int_a^b g^2(x) \dif x\right)
$$

**证明：** 令 $F(t) = \int_a^b \left(tf(x)-g(x)\right)^2 \dif x$，则 $F(t) \ge 0$，从而 $\Delta \le 0$。

**Hölder 不等式** $\quad$ 若 $x_k,y_k,p,q>0$（$1\le k\le n$），$\dfrac{1}{p}+\dfrac{1}{q}= 1$，则
$$
\sum\limits_{k=1}^nx_ky_k\le
\left(\sum\limits_{k=1}^nx_k^p\right)^{\frac{1}{p}}\left(\sum\limits_{k=1}^ny_k^q\right)^{\frac{1}{q}}
$$
并且等号成立当且仅当 $x^p_ky^{-q}_k$ 为不依赖 $k$ 的常数。

**积分Hölder不等式。**
若 $f,g\in\mathscr{C}[a,b]$，$p,q> 1$ 且 $\dfrac{1}{p}+\dfrac{1}{q}=1$，则
$$
\left|\int_a^bf(x)g(x) \dif x\right|\le
\left(\int_a^b|f(x)|^p \dif x\right)^{\frac{1}{p}}
\left(\int_a^b|g(x)|^q \dif x\right)^{\frac{1}{q}}
$$

可以看出，Cauchy-Schwarz-Buniakowsky不等式是积分 Hölder不等式在 $p=q=2$ 时的特例；积分的绝对值三角不等式是积分 Hölder不等式在 $p=1,q=\infty,g\equiv 1$ 时的特例。

**积分第一中值定理。**
若 $f\in \mathscr{C}[a,b]$，则 $\exists \xi \in [a,b]$ 使得 $\int_a^b f(x) \dif x = f(\xi) (b-a)$。

**积分第一中值定理（加权形式）。**
若 $f\in \mathscr{C}[a,b]$，$g\in \mathscr{R}[a,b]$ 且 $g$ 不变号，则 $\exists \xi\in[a,b]$ 使得
$$
\int_a^b f(x)g(x) \dif x=f(\xi)\int_a^b g(x) \dif x
$$

**证明：** 由于 $f,g\in \mathscr{R}[a,b]$，则 $fg\in \mathscr{R}[a,b]$。设 $f$ 在 $[a,b]$ 上的最大值和最小值分别为 $M,m$。又 $g$ 在 $[a,b]$ 上不变号，不失一般性，可以假设 $g\ge 0$，否则考虑 $-g$。有
$$
mg(x)\le f(x)g(x)\le Mg(x)
$$
进而就有
$$
m\int_a^bg(x) \dif x\le \int_a^bf(x)g(x) \dif x
\le M\int_a^bg(x) \dif x
$$
如果 $\int_a^b g(x) \dif x= 0$，则 $\int_a^b f(x)g(x) \dif x=0$，此时 $\forall \xi\in[a,b]$，所证结论成立；

若 $\int_a^b g(x) \dif x\neq 0$，则
$$
m\le \frac{\int_a^b f(x)g(x) \dif x}{\int_a^b g(x) \dif x}\le M
$$
由连续函数最值定理与介值定理知，$\exists\xi\in[a,b]$，使得 $\dfrac{\int_a^b f(x)g(x) \dif x}{\int_a^b g(x) \dif x}=f(\xi)$，故所证结论成立。

> [!example]+
> 若 $f\in\mathscr{C}^{(1)}[a,b]$，求证：
> $$
> \max_{x\in [a,b]}|f(x)|\le \frac{1}{b-a}\left|\int_a^bf(x) \dif x\right|+\int_a^b|f'(x)| \dif x
> $$
>
> ---
>
> **证明：** 由于 $f\in\mathscr{C}^{(1)}[a,b]$，因此 $|f|$ 连续，从而由最值定理知，$\exists \xi\in [a,b]$ 使 $|f(\xi)|=\max\limits_{x\in [a,b]}|f(x)|$。
>
> 又由积分中值定理，$\exists\eta\in [a,b]$ 使得我们有 $\dfrac{1}{b-a}\int_a^b f(x) \dif x=f(\eta)$。而
> $$
> |f(\xi)-f(\eta)|=\left|\int_{\eta}^{\xi} f'(x) \dif x\right|
> \le \left|\int_{\eta}^{\xi} |f'(x)| \dif x\right|
> \le \int_a^b |f'(x)| \dif x
> $$
> 于是
> $$
> \max_{x\in [a,b]}|f(x)|=|f(\xi)|\le |f(\eta)|+|f(\xi)-f(\eta)|
> \le \frac{1}{b-a}\left|\int_a^bf(x) \dif x\right|
> +\int_a^b|f'(x)| \dif x
> $$

**周期连续函数的定积分。**
如果 $f\in\mathscr{C}(\mathbb{R})$ 是周期为 $T>0$ 的周期函数，则 $\forall a\in\mathbb{R}$，$\int_a^{a+T}f(x) \dif x=\int_0^{T}f(x) \dif x$。

### 函数可积的条件

#### 利用Darboux和刻画函数的可积性

> [!definition] Darboux和
> 设 $f:[a,b]\rightarrow \mathbb{R}$ 为有界函数，而 $P: a=x_0<x_1<\cdots<x_n=b$ 为 $[a,b]$ 的分割。对于 $1\le i\le n$，定义
>
> （1）$m_i=\inf\limits_{x\in \Delta_i}f(x)$，$M_i=\sup\limits_{x\in \Delta_i}f(x)$；
>
> （2）$L(f;P)=\sum\limits_{i=1}^{n}m_i\Delta x_i$，称为 **Darboux下和**；
>
> （3）$U(f;P)=\sum\limits_{i=1}^{n}M_i\Delta x_i$，称为 **Darboux上和**。

给定有界函数 $f:[a,b]\rightarrow \mathbb{R}$，$m=\inf\limits_{x\in [a,b]}f(x)$，$M=\sup\limits_{x\in [a,b]}f(x)$，则
$$
m(b-a) \le L(f;P) \le \sigma(f;P,\xi) \le U(f;P) \le M(b-a)
$$

**证明：** $m_i \ge m$，$M_i \le M$。

给定有界函数 $f:[a,b]\rightarrow \mathbb{R}$，若 $P_1,P_2$ 为 $[a,b]$ 的分割且 $P_1\subseteq P_2$，则
$$
L(f;P_1)\le L(f;P_2)\le U(f;P_2)\le U(f;P_1)
$$

**证明：** 不妨设 $x_1<x_2<x_3$ 为 $P_2$ 的分割中相邻三点，其中 $x_1,x_3$ 同时为 $P_1$ 的分割中相邻两点，那么 $\inf\limits_{x\in [x_1,x_3]} f(x) \le \inf\limits_{x\in [x_1,x_2]} f(x)$，$\inf\limits_{x\in [x_1,x_3]} f(x) \le \inf\limits_{x\in [x_2,x_3]} f(x)$，则
$$
\begin{aligned}
(x_3-x_1)\inf\limits_{x\in [x_1,x_3]} f(x)
& = (x_2-x_1)\inf\limits_{x\in [x_1,x_3]} f(x) + (x_3-x_2)\inf\limits_{x\in [x_1,x_3]} f(x)\\
& \le (x_2-x_1)\inf\limits_{x\in [x_1,x_2]} f(x) + (x_3-x_2)\inf\limits_{x\in [x_2,x_3]} f(x)
\end{aligned}
$$

给定有界函数 $f:[a,b]\rightarrow \mathbb{R}$，$P_1,P_2$ 为 $[a,b]$ 的分割，则 $L(f;P_1) \le U(f;P_2)$。

**证明：** 取分割 $Q = P_1 \cup P_2$，则 $P_1 \subseteq Q$，$P_2 \subseteq Q$。

设 $f:[a,b]\rightarrow \mathbb{R}$ 为有界函数，而 $P: a=x_0<x_1<\cdots<x_n=b$ 为 $[a,b]$ 的分割，则
$$
L(f;P)=\inf\limits_{\xi}\sigma(f;P,\xi),\qquad U(f;P)=\sup\limits_{\xi}\sigma(f;P,\xi)
$$

> [!definition] 上积分、下积分
> 给定有界函数 $f:[a,b]\rightarrow \mathbb{R}$，称
>
> （1）$\displaystyle{\underline{\int}_a^b} f(x) \dif x=\sup\limits_{P}L(f;P)$ 为 $f$ 在 $[a,b]$ 上的**下积分**；
>
> （2）$\displaystyle{\overline{\int}_a^b} f(x) \dif x=\inf\limits_{P}U(f;P)$ 为 $f$ 在 $[a,b]$ 上的**上积分**。

> [!theorem] Darboux判别准则
> 设 $f:[a,b]\rightarrow \mathbb{R}$ 为有界函数，则下述结论等价：
>
> （1）$f$ 在 $[a,b]$ 上Riemann可积；
>
> （2）$\forall \varepsilon>0$，存在 $[a,b]$ 的分割 $P$ 使得 $U(f;P)-L(f;P)<\varepsilon$；
>
> （3）$\displaystyle\underline{\int}_a^b f(x) \dif x=\overline{\int}_a^b f(x) \dif x$。
>
> **证明：** 首先给出下面引理。
>
> > [!lemma]
> > 设 $f:[a,b]\to\mathbb{R}$ 为有界函数，而 $P:a=x_0<x_1<\cdots<x_n=b$ 为 $[a,b]$ 的分割。在 $P$ 的基础上多加一个分点，组成一个具有 $n+2$ 个分点的分割，记为 $P^{\prime}$，则
> > $$
> > \begin{aligned}
> > & L(f;P)\le L(f;P')\le L(f;P)+\omega\lambda(P)\\
> > & U(f;P)-\omega\lambda(P) \le U(f;P') \le U(f;P)
> > \end{aligned}
> > $$
> >
> > **证明：** 设在第 $i$ 个区间 $[x_{i-1},x_i]$ 内部加上了一个分点 $x^*$，得到：
> > $$
> > P':a=x_0<x_1<\cdots<x_{i-1}<x^*<x_i<\cdots<x_n=b
> > $$
> > 这时下和 $L(f;P)$ 与下和 $L(f;P')$ 的不同之处在于，前者中一项 $m_i\Delta x_i$ 被后者中两项之和 $(x^*-x_{i-1})\inf\limits_{x\in[x_{i-1},x^*]}f(x)+(x_i-x^*)\inf\limits_{x\in[x^*,x_i]}f(x)$ 代替。而
> > $$
> > \begin{aligned}
> > &(x^*-x_{i-1})\inf\limits_{x\in[x_{i-1},x^*]}f(x)+(x_i-x^*)\inf\limits_{x\in[x^*,x_i]}f(x)\\
> > &\ge (x^*-x_{i-1})\inf\limits_{x\in[x_{i-1},x_i]}f(x)+(x_i-x^*)\inf\limits_{x\in[x_{i-1},x_i]}f(x) \\
> > &= (x_i-x_{i-1})m_i = m_i \Delta x_i
> > \end{aligned}
> > $$
> > 故有 $L(f;P')-L(f;P) \ge 0$。
> >
> > 另一方面，令 $\omega=M-m$，$\omega_i = M_i - m_i$，有
> > $$
> > \begin{aligned}
> > L(f;P')-L(f;P) &= (x^*-x_{i-1})\inf\limits_{x\in[x_{i-1},x^*]}f(x)+(x_i-x^*)\inf\limits_{x\in[x^*,x_i]}f(x) - (x_i-x_{i-1})m_i\\
> > &\le (x_i-x_{i-1})M_i - (x_i-x_{i-1})m_i\\
> > &\le \omega_i \Delta x_i \le \omega \Delta x_i \le \omega \lambda(P)
> > \end{aligned}
> > $$
> > 故 $L(f;P)\le L(f;P')\le L(f;P)+\omega\lambda(P)$。
> >
> > 类似地，有 $U(f;P)-\omega\lambda(P) \le U(f;P') \le U(f;P)$。
>
> 以此类推，有
>
> > [!lemma]
> > 设 $f:[a,b]\to\mathbb{R}$ 为有界函数，$P,P'$ 为 $[a,b]$ 的两个分割，其中 $P^{\prime}$ 是在 $P$ 的基础上多加 $n$ 个新分点，则：
> > $$
> > \begin{aligned}
> > & L(f;P)\le L(f;P')\le L(f;P)+n\omega\lambda(P)\\
> > & U(f;P)-n\omega\lambda(P) \le U(f;P') \le U(f;P)
> > \end{aligned}
> > $$
>
> 由这两个引理易证。

#### 利用振幅刻画函数的可积性

> [!definition] 振幅
> 假设 $X$ 为非空数集，而 $f:X\rightarrow \mathbb{R}$ 为有界函数。对于任意非空子集 $J\subseteq X$，定义 $\omega(f;J):=\sup\limits_{x,y\in J}|f(x)-f(y)|$，称为 $f$ 在 $J$ 上的**振幅**。

容易看出，$\omega(f;J)=\sup\limits_{x\in J}f(x) - \inf\limits_{x \in J}f(x)$。

> [!theorem] 利用振幅刻画可积性
> 设 $f:[a,b]\rightarrow \mathbb{R}$ 为有界函数，则 $f\in \mathscr{R}[a,b]$ 当且仅当 $\lim\limits_{\lambda(P) \to 0} \sum\limits_{i=1}^n \omega(f;\Delta_i)\Delta x_i=0$。

由此我们可以很容易地得到一大类函数的可积性。

> [!theorem] 连续函数的可积性
> 闭区间上的连续函数一定可积，即 $\mathscr{C}[a,b] \subseteq \mathscr{R}[a,b]$。
>
> **证明：** 由于 $f\in \mathscr{C}[a,b]$ 在 $[a,b]$ 上一致连续，故 $\forall \varepsilon>0$，$\exists \delta>0$，使得 $\forall x,y\in [a,b]$，若 $|x-y|<\delta$，则 $|f(x)-f(y)|<\dfrac{\varepsilon}{b-a+1}$。对 $[a,b]$ 的任意分割 $P: a=x_0<\cdots<x_n=b$，当 $\lambda(P)<\delta$ 时，$\sum\limits_{i=1}^n\omega(f;\Delta_i)\Delta x_i \le \sum\limits_{i=1}^n\dfrac{\varepsilon}{b-a+1}(x_i-x_{i-1}) <\varepsilon$，因此所证结论成立。

称函数 $f:[a,b]\rightarrow \mathbb{R}$ 为**逐段**（或**分段**）**连续函数**，如果 $f$ 在 $[a,b]$ 上至多只有有限多个间断点，且均为第一类间断点。

**逐段连续函数的可积性。**
闭区间上的逐段连续函数一定可积。

**单调函数的可积性。**
若 $f:[a,b] \to \mathbb{R}$ 单调，则 $f \in \mathscr{R}[a,b]$。

**证明：** 不失一般性，假设 $f$ 为单调递增（否则可考虑 $-f$），$\forall \varepsilon>0$，选取 $\delta=\dfrac{\varepsilon}{f(b)-f(a)+1}$，则对于区间 $[a,b]$ 的任意分割 $P:a=x_0<\cdots< x_n=b$，当 $\lambda(P)<\delta$ 时，我们均有
$$
\sum_{i=1}^n\omega(f;\Delta_i)\Delta x_i
\le \sum_{i=1}^n\big(f(x_i)-f(x_{i-1})\big)\delta
= \big(f(b)-f(a)\big)\delta<\varepsilon
$$
因此所证结论成立。

> [!example]+
> 证明：若 $f,g\in \mathscr{R}[a,b]$，则 $fg\in\mathscr{R}[a,b]$。
>
> ---
>
> **证明：** 定义 $M=\sup\limits_{x\in [a,b]}|f(x)|$，则 $\forall x,y\in [a,b]$，
> $\big|(f(x))^2-(f(y))^2\big|=\big|f(x)+f(y)\big|\cdot\big|f(x)-f(y)\big| \le 2M\big|f(x)-f(y)\big|$。于是对于区间 $[a,b]$ 的任意分割 $P$，我们有
> $$
> \sum_{i=1}^n\omega(f^2;\Delta_i)\Delta x_i
> \le 2M\sum_{i=1}^n\omega(f;\Delta_i)\Delta x_i
> $$
> 由于 $f\in\mathscr{R}[a,b]$，则由夹逼原理可知
> $$
> \lim\limits_{\lambda(P)\rightarrow 0}\sum\limits_{i=1}^n\omega(f^2;\Delta_i)\Delta x_i=0
> $$
> 故 $f^2\in \mathscr{R}[a,b]$。则由 $f,g\in\mathscr{R}[a,b]$，有 $f+g,f-g\in\mathscr{R}[a,b]$，由此可得 $fg=\frac{1}{4}\big((f+g)^2-(f-g)^2\big)\in\mathscr{R}[a,b]$，从而所证结论成立。

#### 利用Lebesgue测度刻画函数的可积性

> [!definition] 零测度集
> 称数集 $X$ 为**零测度集**，若 $\forall \varepsilon>0$，存在至多可数的一列开区间 $\{(a_n,b_n)\}$ 使得 $X\subseteq \bigcup\limits_{n=1}^{\infty}(a_n,b_n)$，且 $\lim\limits_{n\rightarrow \infty}\sum\limits_{k=1}^n(b_k-a_k)<\varepsilon$。

显然 $\varnothing$ 是零测度集；容易看出，至多可数的数集（如有理数集）是零测度集。

**零测度集的性质。**
（1）零测度集的子集也为零测度集；

（2）至多可数个零测度集的并集是零测度集。

> [!theorem] Lebesgue判别准则
> 区间 $[a,b]$ 上的有界函数 $f$ Riemann可积当且仅当由 $f$ 的所有间断点所构成的集合为零测度集。

如果 $f: [a,b]\rightarrow [c,d]$ 可积，而 $g\in \mathscr{C}[c,d]$，则 $g\circ f\in\mathscr{R}[a,b]$。

**证明：** $g \circ f$ 的间断点一定是 $f$ 的间断点。
