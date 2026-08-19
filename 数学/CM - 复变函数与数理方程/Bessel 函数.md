## Bessel 方程

柱坐标中对 Laplace 方程、波动方程或热传导方程分离变量后，径向部分常化为

$$
\mark{x^2y''+xy'+(x^2-\nu^2)y=0,}
$$

称为 $\nu$ 阶 Bessel 方程。$x=0$ 是正则奇点，因此使用 Frobenius 级数求解。

## 第一类与第二类 Bessel 函数

第一类 Bessel 函数定义为

$$
\mark{J_\nu(x)=\sum_{k=0}^\infty
\frac{(-1)^k}{k!\,\Gamma(k+\nu+1)}
\left(\frac x2\right)^{2k+\nu}.}
$$

当 $\nu$ 不是整数时，$J_\nu$ 与 $J_{-\nu}$ 线性无关。第二类 Bessel 函数定义为

$$
Y_\nu(x)=\frac{J_\nu(x)\cos\nu\pi-J_{-\nu}(x)}{\sin\nu\pi},
$$

整数阶情形取 $\nu\to n$ 的极限。一般解为

$$
y=AJ_\nu(x)+BY_\nu(x).
$$

在包含轴线 $r=0$ 的物理区域内，通常要求解有限，因此舍去在原点发散的 $Y_n$。

## 递推与导数公式

第一类 Bessel 函数满足

$$
J_{\nu-1}(x)+J_{\nu+1}(x)=\frac{2\nu}{x}J_\nu(x),
$$

$$
J_{\nu-1}(x)-J_{\nu+1}(x)=2J_\nu'(x).
$$

等价地，

$$
\frac{\dif}{\dif x}[x^\nu J_\nu(x)]
=x^\nu J_{\nu-1}(x),
$$

$$
\frac{\dif}{\dif x}[x^{-\nu}J_\nu(x)]
=-x^{-\nu}J_{\nu+1}(x).
$$

这些公式用于计算边界导数、模值和相邻阶函数。

## 零点与正交性

记 $j_{\nu,n}$ 为 $J_\nu$ 的第 $n$ 个正零点。函数

$$
J_\nu\left(\frac{j_{\nu,n}}Rr\right)
$$

满足圆盘径向 Dirichlet 边界条件 $R(R)=0$。不同零点对应的特征函数关于权 $r$ 正交：

$$
\int_0^R r
J_\nu\left(\frac{j_{\nu,m}}Rr\right)
J_\nu\left(\frac{j_{\nu,n}}Rr\right)\dif r=0,
\quad m\neq n.
$$

模值为

$$
\int_0^R r
J_\nu^2\left(\frac{j_{\nu,n}}Rr\right)\dif r
=\frac{R^2}{2}J_{\nu+1}^2(j_{\nu,n}).
$$

## 圆盘上的分离变量

轴对称圆盘热传导问题的解可展开为

$$
u(r,t)=\sum_{n=1}^\infty c_n
J_0\left(\frac{j_{0,n}}Rr\right)
\exp\left[-a^2\left(\frac{j_{0,n}}R\right)^2t\right].
$$

系数 $c_n$ 由初温关于权函数 $r$ 的 Fourier–Bessel 展开确定。这是[[分离变量法]]在非直角坐标系中的典型形式。
