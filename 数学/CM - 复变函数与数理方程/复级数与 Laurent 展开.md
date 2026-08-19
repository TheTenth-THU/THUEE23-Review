## 复数项级数与函数项级数

复级数 $\sum_{n=0}^\infty w_n$ 收敛，当且仅当其实部级数与虚部级数都收敛。绝对收敛 $\sum|w_n|<\infty$ 蕴含收敛，并允许重排。

对函数项级数，紧子集上一致收敛是逐项积分、解析性保持和逐项求导的重要条件。解析函数列若在紧子集上一致收敛，其极限仍解析。

## 幂级数与收敛圆

幂级数

$$
\sum_{n=0}^\infty a_n(z-z_0)^n
$$

存在收敛半径 $R$，满足

$$
\frac1R=\limsup_{n\to\infty}|a_n|^{1/n}.
$$

它在 $|z-z_0|<R$ 内绝对且局部一致收敛，在 $|z-z_0|>R$ 发散；圆周上需逐点判断。

## Taylor 展开

若 $f$ 在圆盘 $|z-z_0|<R$ 内解析，则

$$
\mark{f(z)=\sum_{n=0}^\infty
\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n.}
$$

展开的收敛半径延伸到距 $z_0$ 最近的奇点。不同中心的 Taylor 展开在重叠圆盘中表示同一解析函数，由此形成解析延拓。

## Laurent 展开

若 $f$ 在环域 $R_1<|z-z_0|<R_2$ 内解析，则唯一展开为

$$
\mark{f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n,}
$$

其中

$$
a_n=\frac1{2\pi\I}\oint_\gamma
\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}\dif\zeta.
$$

同一函数在由不同奇点划分的环域上可能有不同 Laurent 展开，因此展开时必须同时写明收敛域。

## 孤立奇点的分类

设 $z_0$ 是孤立奇点，根据 Laurent 展开的主部：

+ 主部为零时，$z_0$ 是**可去奇点**。
+ 主部只有有限项且最高负幂为 $(z-z_0)^{-m}$ 时，$z_0$ 是 $m$ 阶**极点**。
+ 主部有无穷多项时，$z_0$ 是**本性奇点**。

等价判据为

$$
\begin{aligned}
&\lim_{z\to z_0}f(z)\text{ 有限} &&\Longleftrightarrow \text{可去奇点},\\
&\lim_{z\to z_0}|f(z)|=\infty &&\Longleftrightarrow \text{极点}.
\end{aligned}
$$

Laurent 系数 $a_{-1}$ 是该点的留数，见[[留数定理]]。
