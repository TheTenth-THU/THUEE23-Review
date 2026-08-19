## Laplace 与 Poisson 方程

位势问题的基本形式为

$$
-\Dif u=f\quad\text{in }\Omega.
$$

$f=0$ 时得到 Laplace 方程，解称为**调和函数**。调和函数满足平均值性质和最大值原理，因此内部值受边界值强烈约束。

## 全空间基本解

基本解 $\varPhi$ 满足

$$
-\Dif\varPhi=\delta.
$$

在二维和三维分别为

$$
\varPhi_2(\v x)=-\frac1{2\pi}\ln|\v x|,
\qquad
\varPhi_3(\v x)=\frac1{4\pi|\v x|}.
$$

因此全空间 Poisson 方程的形式解为

$$
u(\v x)=\int_{\mathbb R^n}
\varPhi(\v x-\v y)f(\v y)\dif\v y.
$$

## Green 恒等式

对足够光滑的 $u,v$，Green 第二恒等式为

$$
\int_\Omega(u\Dif v-v\Dif u)\dif V
=\int_{\partial\Omega}
\left(u\frac{\partial v}{\partial n}
-v\frac{\partial u}{\partial n}\right)\dif S.
$$

它把区域内的微分方程与边界上的函数值、法向导数连接起来，是构造 Green 函数的基础。

## Dirichlet Green 函数

对固定场点 $\v x\in\Omega$，Dirichlet Green 函数满足

$$
-\Dif_{\v y}G(\v x,\v y)=\delta(\v y-\v x),
\qquad
G(\v x,\v y)=0\quad\text{on }\partial\Omega.
$$

若 $-\Dif u=f$ 且 $u=g$ 在边界上，则

$$
\mark{u(\v x)=
\int_\Omega G(\v x,\v y)f(\v y)\dif\v y
-\int_{\partial\Omega}g(\v y)
\frac{\partial G}{\partial n_{\v y}}(\v x,\v y)\dif S_{\v y}.}
$$

Green 函数等于自由空间基本解加上一个关于 $\v y$ 的调和修正，使边界条件得到满足。

## 对称性与唯一性

对自伴的 Laplace 算子和齐次 Dirichlet 边界条件，Green 函数满足

$$
G(\v x,\v y)=G(\v y,\v x).
$$

最大值原理说明 Dirichlet 问题至多有一个解。Neumann 问题则需要相容条件

$$
\int_\Omega f\dif V=-\int_{\partial\Omega}g\dif S,
$$

并且解只确定到加法常数。

> [!note] Green 函数与基本解
> 基本解只依赖算子和全空间平移不变性；Green 函数还编码具体区域和边界条件。二者不能混为同一个对象。
