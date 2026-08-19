## Fourier 变换与反演

本课程采用对称归一化约定：

$$
\mark{\hat f(\omega)=\mathcal F[f](\omega)
=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}
f(x)\e^{-\I\omega x}\dif x,}
$$

$$
\mark{f(x)=\mathcal F^{-1}[\hat f](x)
=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}
\hat f(\omega)\e^{\I\omega x}\dif\omega.}
$$

绝对可积保证变换存在且连续，但反演需要附加条件；在 $L^2$ 理论中，变换可通过稠密延拓定义并保持范数。

## 基本性质

在相应积分、导数存在且边界项消失时，有：

```tx
| 原函数 | Fourier 变换 |
|:-------|:-------------|
| $af+bg$ | $a\hat f+b\hat g$ |
| $f(x-x_0)$ | $\e^{-\I\omega x_0}\hat f(\omega)$ |
| $\e^{\I\omega_0x}f(x)$ | $\hat f(\omega-\omega_0)$ |
| $f(ax)$ | $|a|^{-1}\hat f(\omega/a)$ |
| $f^{(n)}(x)$ | $(\I\omega)^n\hat f(\omega)$ |
| $x^nf(x)$ | $\I^n\dfrac{\dif^n\hat f}{\dif\omega^n}$ |
```

若 $f$ 为实函数，则 $\hat f(-\omega)=\hat f(\omega)^*$。若 $f$ 为实偶函数，变换为实偶函数；若 $f$ 为实奇函数，变换为纯虚奇函数。

## 卷积定理

定义卷积

$$
(f*g)(x)=\int_{-\infty}^{\infty}f(x-\xi)g(\xi)\dif\xi.
$$

在对称归一化约定下，

$$
\mark{\mathcal F[f*g]
=\sqrt{2\pi}\,\hat f\,\hat g,}
$$

$$
\mathcal F[fg]
=\frac1{\sqrt{2\pi}}(\hat f*\hat g).
$$

卷积在平移不变线性系统、基本解和概率分布中都表示「输入经过核的加权叠加」。

## Parseval 等式

对 $f,g\in L^2(\mathbb R)$，

$$
\int_{-\infty}^{\infty}f(x)g(x)^*\dif x
=\int_{-\infty}^{\infty}\hat f(\omega)\hat g(\omega)^*\dif\omega.
$$

特别地，

$$
\int|f(x)|^2\dif x=\int|\hat f(\omega)|^2\dif\omega.
$$

这说明 Fourier 变换是 $L^2$ 空间上的幺正变换，时域与频域总能量相同。

## 微分方程中的应用

对全空间常系数方程，Fourier 变换把空间微分替换为 $\I\omega$ 的乘法。例如

$$
-u''+a^2u=f
$$

变换为

$$
(\omega^2+a^2)\hat u=\hat f,
\qquad
\hat u=\frac{\hat f}{\omega^2+a^2}.
$$

反演后得到 $u$ 是 $f$ 与基本解的卷积。点源的变换需要[[Dirac delta 函数]]。
