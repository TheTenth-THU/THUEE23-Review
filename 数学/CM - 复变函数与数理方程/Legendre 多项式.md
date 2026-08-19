## Legendre 方程

球坐标中对轴对称位势问题分离变量后，令 $x=\cos\theta$，角向方程化为

$$
\mark{(1-x^2)y''-2xy'+\lambda y=0,
\qquad -1<x<1.}
$$

要求在 $x=\pm1$ 有限，使级数在某阶终止，得到

$$
\lambda=n(n+1),
\qquad n=0,1,2,\ldots
$$

以及 $n$ 次 Legendre 多项式 $P_n(x)$。

## Rodrigues 公式与前几项

Legendre 多项式可由 Rodrigues 公式定义：

$$
\mark{P_n(x)=\frac1{2^n n!}
\frac{\dif^n}{\dif x^n}(x^2-1)^n.}
$$

前几项为

$$
P_0=1,
\quad P_1=x,
\quad P_2=\frac12(3x^2-1),
\quad P_3=\frac12(5x^3-3x).
$$

其宇称满足

$$
P_n(-x)=(-1)^nP_n(x).
$$

## 生成函数与递推关系

生成函数为

$$
\frac1{\sqrt{1-2xt+t^2}}
=\sum_{n=0}^\infty P_n(x)t^n,
\qquad |t|<1.
$$

由此可导出三项递推

$$
\mark{(n+1)P_{n+1}(x)
=(2n+1)xP_n(x)-nP_{n-1}(x).}
$$

导数关系包括

$$
(1-x^2)P_n'(x)
=n[P_{n-1}(x)-xP_n(x)].
$$

## 正交性与模值

Legendre 方程是权函数 $w(x)=1$ 的 Sturm–Liouville 问题，因此

$$
\mark{\int_{-1}^1P_m(x)P_n(x)\dif x
=\frac{2}{2n+1}\delta_{mn}.}
$$

合适函数可展开为 Legendre 级数

$$
f(x)=\sum_{n=0}^\infty a_nP_n(x),
\qquad
a_n=\frac{2n+1}{2}\int_{-1}^1f(x)P_n(x)\dif x.
$$

## 球对称边值问题

轴对称三维 Laplace 方程的分离变量解具有形式

$$
u(r,\theta)=\sum_{n=0}^\infty
\left(A_nr^n+B_nr^{-n-1}\right)P_n(\cos\theta).
$$

区域是否包含原点或无穷远决定舍去哪一支径向解，球面边界数据的 Legendre 展开决定系数。更一般的非轴对称问题会出现缔合 Legendre 函数和球谐函数。

> [!note] 几何意义
> $P_n$ 不是孤立的公式表，而是球坐标角向自伴特征值问题的本征函数；其正交性正是边界数据可按角向模态分解的原因。
