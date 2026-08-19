## 分布意义下的 delta

Dirac delta 不是普通函数，而是作用在测试函数上的分布：

$$
\mark{\langle\delta,\varphi\rangle=\varphi(0).}
$$

形式上常写为

$$
\int_{-\infty}^{\infty}\delta(x)\varphi(x)\dif x=\varphi(0).
$$

平移后的 delta 满足

$$
\int\delta(x-x_0)\varphi(x)\dif x=\varphi(x_0).
$$

> [!danger] 不把 delta 当作点值无穷大的函数
> 「$x\neq0$ 时为零、$x=0$ 时无穷大」只是帮助记忆的形式图像。严格运算应以它对测试函数的作用为定义。

## 缩放与复合变量

对 $a\neq0$，

$$
\delta(ax)=\frac1{|a|}\delta(x).
$$

若 $g(x)$ 的零点 $x_k$ 都是单零点，则

$$
\delta(g(x))=\sum_k\frac{\delta(x-x_k)}{|g'(x_k)|}.
$$

特别地，$x\delta(x)=0$。delta 与任意合适函数卷积得到

$$
(f*\delta)(x)=f(x).
$$

因此 delta 是卷积运算的单位元，也是线性系统的单位冲激输入。

## delta 的导数

分布导数由分部积分定义：

$$
\langle\delta',\varphi\rangle=-\varphi'(0).
$$

更一般地，

$$
\langle\delta^{(n)},\varphi\rangle
=(-1)^n\varphi^{(n)}(0).
$$

这一规则把点源、偶极源和不连续函数的弱导数统一起来。例如 Heaviside 阶跃函数 $H$ 的分布导数为 $H'=\delta$。

## Fourier 变换

在[[Fourier 变换]]的对称归一化约定下，

$$
\mark{\mathcal F[\delta](\omega)=\frac1{\sqrt{2\pi}},}
\qquad
\mathcal F[1](\omega)=\sqrt{2\pi}\,\delta(\omega).
$$

平移 delta 的变换为

$$
\mathcal F[\delta(x-x_0)]
=\frac1{\sqrt{2\pi}}\e^{-\I\omega x_0}.
$$

## 基本解中的作用

微分算子 $L$ 的基本解 $G$ 满足

$$
LG=\delta.
$$

若 $L$ 为平移不变线性算子，则 $Lu=f$ 的解可写成 $u=G*f$。这一思想在[[热传导方程]]和[[位势方程与 Green 函数]]中反复出现。
