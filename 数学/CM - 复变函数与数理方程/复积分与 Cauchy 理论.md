## 复曲线积分

设分段光滑曲线 $\gamma:z=z(t)$，$a\le t\le b$。复积分定义为

$$
\int_\gamma f(z)\dif z
=\int_a^b f(z(t))z'(t)\dif t.
$$

若 $f=u+\I v$、$\dif z=\dif x+\I\dif y$，则

$$
\int_\gamma f\dif z
=\int_\gamma(u\dif x-v\dif y)
+\I\int_\gamma(v\dif x+u\dif y).
$$

反向曲线使积分变号，曲线拼接使积分相加，并有估计

$$
\left|\int_\gamma f(z)\dif z\right|
\le L(\gamma)\max_{z\in\gamma}|f(z)|.
$$

## 原函数与路径无关

若 $F'(z)=f(z)$，则

$$
\int_\gamma f(z)\dif z=F(z_b)-F(z_a).
$$

在区域内，积分与路径无关、任意闭路积分为零、存在原函数三者等价。

## Cauchy 积分定理

> [!theorem] Cauchy 积分定理
> 若 $f$ 在单连通区域 $D$ 内解析，则对 $D$ 内任意闭曲线 $\gamma$，有
> $$
> \oint_\gamma f(z)\dif z=0.
> $$

在多连通区域中，若函数在区域及边界上解析，则外边界取逆时针、内边界取顺时针后，所有边界积分之和仍为零。该结论允许在不跨越奇点的前提下连续变形积分路径。

## Cauchy 积分公式

若 $f$ 在简单闭曲线 $\gamma$ 及其内部解析，$z_0$ 位于内部，则

$$
\mark{f(z_0)=\frac1{2\pi\I}
\oint_\gamma\frac{f(\zeta)}{\zeta-z_0}\dif\zeta.}
$$

进一步有高阶导数公式

$$
f^{(n)}(z_0)=\frac{n!}{2\pi\I}
\oint_\gamma\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}\dif\zeta.
$$

这说明解析函数由任意包围点的边界值完全确定，并自动无穷次可导。

## 重要推论

+ **Cauchy 不等式**：若 $|f(z)|\le M$ 在 $|z-z_0|=R$ 上成立，则 $|f^{(n)}(z_0)|\le n!M/R^n$。
+ **Liouville 定理**：有界整函数必为常数。
+ **最大模原理**：非常数解析函数的模不能在区域内部取得最大值。
+ **Morera 定理**：连续函数若在区域内任意三角形边界上的积分为零，则它解析。

当围道内部出现孤立奇点时，闭路积分由[[留数定理]]计算。
