## Laplace 变换引入

### Laplace 变换的定义

> [!definition] Laplace 变换和逆变换
> 对于一个函数 $f(t)$，其 **Laplace 变换**和**逆变换**定义为
> $$
> \begin{aligned} 
> &F(s) = \mathscr{L}\{f(t)\} = \int_{0_{-}}^\infty f(t) \e^{-st} \dif t \\
> &f(t) = \mathscr{L}^{-1}\{F(s)\} = \frac{1}{2\pi \I} \int_{\sigma - \I\infty}^{\sigma + \I\infty} F(s) \e^{st} \dif s \end{aligned}
> $$
> 其中 $s = \sigma + \I \omega$。

一般待研究信号 $f(t)$ 都是因果信号，所以正变换的积分下限取 $0_{-}$，此称**单边（Unilateral）Laplace 变换**。如果下限取到 $-\infty$，则称为**双边（Bilateral）Laplace 变换**。

> [!note]+ Laplace 变换与 Fourier 变换的关系
> + 对于**因果**信号 $f(t)$，Laplace 变换是 **$f(t) \e^{-\sigma t}$ 的 Fourier 变换**。
>     $$ F(s) = \mathscr{L}\{f(t)\} = \int_{0_{-}}^\infty f(t) \e^{-st} \dif t = \int_{0_{-}}^\infty \left(  f(t) \e^{-\sigma t} \right) \e^{-\I \omega t} \dif t = \mathscr{F}[f(t) \e^{-\sigma t}] = F_{1}(\omega) $$
>     其中因果性保证了对 $t < 0$ 有 $f(t) \equiv 0$。
> + 对上面 $F_{1}(\omega)$ 做 Fourier 逆变换，得到
>     $$ f(t) \e^{-\sigma t} = \mathscr{F}^{-1}[F_{1}(\omega)] = \frac{1}{2\pi} \int_{-\infty}^{\infty} F_{1}(\omega) \e^{\I \omega t} \dif \omega$$
>     两侧同时乘以 $\e^{\sigma t}$，得到
>     $$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F_{1}(\omega) \e^{(\sigma + \I \omega) t} \dif \omega = \frac{1}{2\pi\I} \int_{\sigma -\I\infty}^{\sigma + \I\infty} F(s) \e^{st} \dif s = \mathscr{L}^{-1}\{F(s)\} $$
>     其中 $\dif s = \dif \sigma + \I \dif \omega$。
> + **Fourier 变换是虚轴上的 Laplace 变换**。

### Laplace 变换的收敛条件

Laplace 变换**存在**的条件是原函数 $f(t)$ **分段连续**且为**指数阶函数**。即，存在正实数 $\sigma_{0}$ 使得 $\lim_{ t \to \infty }\limits f(t) \e^{-\sigma t} = 0$ 对所有 $\sigma > \sigma_{0}$ 成立。

> [!note] 说明
> 这是为了保证积分 $\displaystyle \int_{0_{-}}^\infty f(t) \e^{-\sigma t} \dif t$ 收敛，即保证 **$f(t) \e^{-\sigma t}$ 绝对可积**。
> 
> 由于 $f(t)$ 乘以衰减函数 $\e^{-\sigma t}$ 后才满足绝对可积，所以**原本不存在 Fourier 变换的信号**（如 $t^{n}$）在 Laplace 变换中也可能可以处理。

### 常见函数的 Laplace 变换

+ **冲激函数 $\delta(t)$**
    $$
    \mathscr{L}\{\delta(t)\} = \int_{0_{-}}^\infty \delta(t) \e^{-st} \dif t = \e^{0} = 1, \quad \forall \sigma
    $$
    注意积分下限为 $0_{-}$，所以**零点出现的冲激量**也包含在内。

+ **阶跃函数 $u(t)$**
    $$
    \mathscr{L}\{u(t)\} = \int_{0_{-}}^\infty u(t) \e^{-st} \dif t = \int_{0_{-}}^\infty \e^{-st} \dif t = \frac{1}{s}, \quad \forall \sigma > 0
    $$

+ **指数函数 $\e^{-at}$**
    $$
    \mathscr{L}\{\e^{-at}\} = \int_{0_{-}}^\infty \e^{-at} \e^{-st} \dif t = \int_{0_{-}}^\infty \e^{-(a+s)t} \dif t = \frac{1}{a+s}, \quad \forall \sigma > -a
    $$

+ **幂函数 $t^{n}$**（其中 $n \in \mathbb{Z}_{+}$）
    $$
    \mathscr{L}\{t^{n}\} = \int_{0_{-}}^\infty t^{n} \e^{-st} \dif t = - \dfrac{t^n\e^{-st}}{s} \Bigg|_{0_{-}}^{\infty} + \dfrac{n}{s} \int_{0_{-}}^\infty t^{n-1} \e^{-st} \dif t = \dfrac{n}{s} \mathscr{L}\{t^{n-1}\}
    $$
    递推得到
    $$
    \mathscr{L}\{t^{n}\} = \dfrac{n!}{s^{n+1}}, \quad \forall \sigma > 0
    $$

## Laplace 变换的基本性质

### 线性性（叠加性、齐次性）

给定两个函数 $f_{1}(t)$ 和 $f_{2}(t)$，以及两个常数 $a$ 和 $b$，则有
$$
\mathscr{L}\{a f_{1}(t) + b f_{2}(t)\} = a \mathscr{L}\{f_{1}(t)\} + b \mathscr{L}\{f_{2}(t)\}
$$

### $t$ 域微分、积分

对于**可微**函数 $f(t)$，有
$$
\mathscr{L}\left\{ \dfrac{\dif f(t)}{\dif t} \right\} = s F(s) - f(0_{-})
$$
进一步地，对于 **$n$ 阶可微**函数 $f(t)$，有
$$
\mathscr{L}\left\{ \dfrac{\dif^{n} f(t)}{\dif t^{n}} \right\} = s^{n} F(s) - \sum_{r=0}^{n-1} s^{n-r-1} f^{(r)}(0_{-})
$$

对于**可积**函数 $f(t)$，有
$$
\mathscr{L}\left\{ \int_{-\infty}^{t} f(\tau) \dif \tau \right\} = \dfrac{F(s)}{s} + \dfrac{\displaystyle\int_{-\infty}^{0_{-}} f(\tau) \dif \tau}{s}
$$
其中 $\displaystyle\int_{-\infty}^{0_{-}} f(\tau) \dif \tau$ 可视为 $t=0_{-}$ 处的积分**初值**。

### $t$ 域平移

对于函数 $f(t)$，
$$
\mathscr{L}\{f(t-t_{0})u(t-t_{0})\} = \e^{-st_{0}} F(s), \quad t_{0}>0
$$
即，原函数延迟 $t_{0}$，其 Laplace 变换乘以 $\e^{-st_{0}}$。

> [!example] 四种延时斜变波形的 Laplace 变换
> ![[四种延时斜变波形.png]]
> $$
> \begin{align}
> & \mathscr{L}\{t u(t)\} = \dfrac{1!}{s^{1+1}} = \dfrac{1}{s^{2}} \\
> & \mathscr{L}\{t u(t-t_{0})\} = \mathscr{L}\{t u(t)\} - \int_{0_{-}}^{t_{0}} t \e^{-st} \dif t = \dfrac{1}{s^{2}} - \dfrac{1}{s^{2}} \left( 1 - st_{0} \e^{-st_{0}} - \e^{-st_{0}} \right) = \dfrac{\e^{-st_{0}}}{s^{2}} + \dfrac{\e^{-st_{0}}}{s} \\
> & \mathscr{L}\{(t-t_{0}) u(t)\} = \mathscr{L}\{t u(t)-t_{0} u(t)\} = \dfrac{1}{s^{2}} - \dfrac{t_{0}}{s} \\
> & \mathscr{L}\{(t-t_{0}) u(t-t_{0})\} = \dfrac{\e^{-st_{0}}}{s^{2}} \\
> \end{align}
> $$

### $t$ 域缩放

对于函数 $f(t)$，
$$
\mathscr{L}\{f(at)\} = \dfrac{1}{a} F\left(\dfrac{s}{a}\right), \quad a>0
$$

### $s$ 域微分、积分

对于**可微**的 Laplace 变换像函数 $F(s)$，有
$$
\dfrac{\dif F(s)}{\dif s} = \mathscr{L}\{-t f(t)\}
$$

对于**可积**的 Laplace 变换像函数 $F(s)$，有
$$
\int_s^{\infty} F(s_{1}) \dif s_{1} = \mathscr{L}\left\{ \dfrac{f(t)}{t} \right\}
$$

### $s$ 域平移

对于 Laplace 变换像函数 $F(s)$，
$$
F(s+a) = \mathscr{L}\{f(t)\e^{-at}\} 
$$
即，原函数被 $\e^{-at}$ 加权，则像函数在复频域上平移 $a$。

### 初值定理和终值定理

> [!theorem] 初值定理
> 若函数 $f(t)$ 及其导数 $\dfrac{\dif f(t)}{\dif t}$ 的 Laplace 变换存在，则
> $$
> \lim_{ t \to 0_{+} } f(t) = f(0_{+}) = \lim_{ s \to \infty } s F(s)
> $$

> [!theorem] 终值定理
> 若函数 $f(t)$ 及其导数 $\dfrac{\dif f(t)}{\dif t}$ 的 Laplace 变换存在，极限 $\lim\limits_{ t \to \infty } f(t)$ 也存在，则
> $$
> \lim_{ t \to \infty } f(t) = \lim_{ s \to 0 } s F(s)
> $$

### 卷积性质

> [!theorem] 时域卷积定理
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Laplace 变换 $F_{1}(s)$、$F_{2}(s)$ 存在，则
> $$
> \mathscr{L}\{f_{1}(t) * f_{2}(t)\} = F_{1}(s) F_{2}(s)
> $$

> [!theorem] 频域卷积定理 
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Laplace 变换 $F_{1}(s)$、$F_{2}(s)$ 存在，则
> $$
> \mathscr{L}\{f_{1}(t) f_{2}(t)\} = \dfrac{1}{2\pi \I} \int_{\sigma - \I\infty}^{\sigma + \I\infty} F_{1}(p) F_{2}(p) \dif p = \dfrac{1}{2\pi\I} F_{1}(s) * F_{2}(s)
> $$

## Laplace 逆变换

Laplace 变换像函数 $F(s)$ [[#用 Laplace 变换解系统微分方程的一般步骤|一般]]形如
$$
\begin{align}
F(s) &= \dfrac{B(s)}{A(s)} = \dfrac{b_{m}s^m + b_{m-1}s^{m-1} + \cdots + b_{1}s + b_{0}}{a_{n}s^n + a_{n-1}s^{n-1} + \cdots + a_{1}s + a_{0}} \\
&= \dfrac{b_{m}}{a_{n}} \dfrac{(s-z_{1})(s-z_{2})\cdots(s-z_{m})}{(s-p_{1})(s-p_{2})\cdots(s-p_{n})}
= \dfrac{b_{m}}{a_{n}} \dfrac{\prod\limits_{j=1}^m (s-z_{j})}{\prod\limits_{i=1}^n (s-p_{i})}
\end{align}
$$
其中，$z_{j}$ 和 $p_{i}$ 分别称为 $F(s)$ 的**零点**和**极点**。一般地，假设 $m < n$，即 $F(s)$ 为**真分式**。

### 部分分式分解法

#### $\{ p_{i} \}_{1 \le i \le n}$ 全为实数轴上单极点

若 $p_{i}$ 全为**实数轴上的单极点**，则 $F(s)$ 可分解为
$$
F(s) = \dfrac{K_{1}}{s-p_{1}} + \dfrac{K_{2}}{s-p_{2}} + \cdots + \dfrac{K_{n}}{s-p_{n}}
$$
其中 $K_{i} = \lim\limits_{ s \to p_{i} } (s-p_{i})F(s)$。 

做逆变换得到
$$
f(t) = \left( K_{1} \e^{p_{1}t} + K_{2} \e^{p_{2}t} + \cdots + K_{n} \e^{p_{n}t} \right) u(t)
$$

#### $\{ p_{i} \}_{1 \le i \le n}$ 中有共轭复极点

设 $p_{i}$ 中有一对**共轭复极点** $-\alpha \pm \I\beta$，则 $F(s)$ 可分解为
$$
F(s) = \dfrac{K_{1}}{s + \alpha - \I\beta} + \dfrac{K_{2}}{s + \alpha + \I\beta} + \cdots 
$$
其中
$$
\begin{cases}
K_{1} = \lim\limits_{ s \to -\alpha + \I\beta } (s + \alpha - \I\beta)F(s) \\
K_{2} = \lim\limits_{ s \to -\alpha - \I\beta } (s + \alpha + \I\beta)F(s)
\end{cases}
$$

记 $K_{1} = A + \I B$，则共轭复极点逆变换对应的原函数为
$$
\mathscr{L}^{-1} \left\{ \dfrac{K_{1}}{s + \alpha - \I\beta} + \dfrac{K_{2}}{s + \alpha + \I\beta} \right\} 
= 2\e^{-\alpha t} \left( A \cos \beta t - B \sin \beta t \right) u(t)
$$

> [!note] 说明
> 实际上，也可以**直接看出结果**，如
> $$
> \dfrac{s+\gamma}{(s+\alpha)^2 + \beta^2} = \underbrace{ \dfrac{s+\alpha}{(s+\alpha)^2 + \beta^2} }_{ \e^{-\alpha t} \cos\beta t } - \dfrac{\alpha-\gamma}{\beta} \underbrace{ \dfrac{\beta}{(s+\alpha)^2 + \beta^2} }_{ \e^{-\alpha t} \sin\beta t }
> $$

#### $\{ p_{i} \}_{1 \le i \le n}$ 中有高阶极点

设 $p_{i}$ 中有一个 **$k$ 阶极点** $p_{1}$，则 $F(s)$ 可分解为
$$
F(s) = \dfrac{K_{11}}{(s-p_{1})^k} + \dfrac{K_{12}}{(s-p_{2})^{k-1}} + \cdots + \dfrac{K_{1k}}{s-p_{1}} + \cdots
$$
其中 $K_{11} = \lim\limits_{ s \to p_{1} }(s-p_{1})^kF(s)$，$K_{1i} = \dfrac{1}{(i-1)!} \lim\limits_{ s \to p_{1} } \dfrac{\dif^{i-1}}{\dif s^{i-1}}(s-p_{1})^kF(s)$。

已知 $\mathscr{L}\left\{ t^n u(t) \right\} = \dfrac{n!}{s^{n+1}}$，则知
$$
\mathscr{L}^{-1}\left\{ \dfrac{K_{1,k+1-r}}{(s-p_{1})^r} \right\} = K_{1,k+1-r}\dfrac{t^{r-1} \e^{p_{1}t}}{(r-1)!} u(t)
$$
故上面 $k$ 阶极点 $p_{1}$ 对应的原函数为
$$
\begin{align}
\mathscr{L}^{-1}\left\{ \dfrac{K_{11}}{(s-p_{1})^k} + \dfrac{K_{12}}{(s-p_{2})^{k-1}} + \cdots + \dfrac{K_{1k}}{s-p_{1}} \right\} \hspace{10em} \\
= \sum\limits_{r=1}^k \dfrac{t^{r-1}}{(k-r)!(r-1)!} \lim\limits_{ s \to p_{1} } \dfrac{\dif^{k-r}}{\dif s^{k-r}}(s-p_{1})^kF(s) \cdot \e^{p_{1}t} u(t)
\end{align}
$$

### 留数法

[[#部分分式分解法]]中已经表现出部分**留数**的应用特征。一般地，对于一个 Laplace 变换**像函数** $F(s)$，其逆变换为
$$
f(t) = \dfrac{1}{2\pi \I} \int_{\sigma - \I\infty}^{\sigma + \I\infty} F(s) \e^{st} \dif s
= \underbrace{ \dfrac{1}{2\pi \I} \int_{C} F(s) \e^{st} \dif s }_{ \sum\limits_{i=1}^n \mathrm{Res} \left[ F(s)\e^{st}, p_{i} \right]  } - \dfrac{1}{2\pi \I} \underbrace{ \int_{C_{\infty}} F(s) \e^{st} \dif s }_{ 0 }
$$
其中 $C_{\infty}$ 是半径 $R \to \infty$ 的圆弧，$C$ 是 Laplace 逆变换**积分路径**与 $C_{\infty}$ 构成的**闭合曲线**。故有
$$
f(t) = \mathscr{L}^{-1} \{F(s)\} = \sum\limits_{i=1}^n \mathrm{Res} \left[ F(s)\e^{st}, p_{i} \right]
$$
