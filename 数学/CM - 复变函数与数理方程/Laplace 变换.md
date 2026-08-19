## 定义与收敛域

对 $t\ge0$ 的函数 $f(t)$，Laplace 变换定义为

$$
\mark{\bar f(p)=\mathcal L[f](p)
=\int_0^\infty f(t)\e^{-pt}\dif t,}
$$

其中 $p=\sigma+\I\omega$。若 $f$ 分段连续且至多按 $\e^{\sigma_0t}$ 增长，则变换在半平面 $\operatorname{Re}p>\sigma_0$ 收敛并解析。

Laplace 变换可看作对 $f(t)H(t)\e^{-\sigma t}$ 作 Fourier 变换，因此指数权重扩大了可变换函数的范围。

## 基本性质

在收敛域内有

$$
\mathcal L[f'](p)=p\bar f(p)-f(0^+),
$$

$$
\mathcal L[f^{(n)}](p)
=p^n\bar f(p)-\sum_{k=0}^{n-1}p^{n-1-k}f^{(k)}(0^+).
$$

因此初值会自动进入变换域方程。另有

$$
\mathcal L[t^nf(t)]=(-1)^n\frac{\dif^n\bar f}{\dif p^n},
$$

$$
\mathcal L[\e^{at}f(t)](p)=\bar f(p-a),
$$

$$
\mathcal L[H(t-a)f(t-a)](p)=\e^{-ap}\bar f(p).
$$

## 卷积定理

半轴卷积定义为

$$
(f*g)(t)=\int_0^t f(t-\tau)g(\tau)\dif\tau.
$$

其变换满足

$$
\mark{\mathcal L[f*g](p)=\bar f(p)\bar g(p).}
$$

这使线性常微分方程的受迫响应自然表示为冲激响应与输入的卷积。

## 反演公式

若 $\bar f(p)$ 在竖直线 $\operatorname{Re}p=\gamma$ 右侧解析，且 $\gamma$ 位于所有奇点右侧，则 Bromwich 反演公式为

$$
\mark{f(t)=\frac1{2\pi\I}
\int_{\gamma-\I\infty}^{\gamma+\I\infty}
\bar f(p)\e^{pt}\dif p.}
$$

对 $t>0$，若可向左闭合围道且大圆弧贡献消失，则可用[[留数定理]]求得

$$
f(t)=\sum_k\operatorname{Res}
\left(\bar f(p)\e^{pt},p_k\right).
$$

## 初值问题

以

$$
y''+ay'+by=g(t),
\qquad y(0)=y_0,\quad y'(0)=v_0
$$

为例，变换后得到

$$
(p^2+ap+b)\bar y
=\bar g+(p+a)y_0+v_0.
$$

解出 $\bar y$ 后通过部分分式、卷积或复反演得到 $y(t)$。最后应检查初值和可能的冲激项，而不能只做形式代数运算。
