## Brown运动

> [!definition] 标准Brown运动
> 随机过程 $\{B(t),t\geq 0\}$ 称为**标准Brown运动 (standard Brownian motion)**，若满足：
> + $B(0)=0$ 几乎必然成立；
> + 它具有独立增量；
> + 对任意 $0\leq s<t$，有 $B(t)-B(s)\sim\mathscr{N}(0,t-s)$；
> + 样本路径几乎必然连续。

Brown运动是零均值Gauss过程。由独立增量可得

$$
\begin{aligned}
\mathbb{E}\{B(t)\}&=0,\\
R_B(t,s)
&=\mathbb{E}\{B(t)B(s)\}
=\min(t,s).
\end{aligned}
$$

其方差 $\operatorname{Var}(B(t))=t$ 随时间增长，所以Brown运动不是宽平稳过程；但增量 $B(t+\tau)-B(t)$ 的分布只依赖 $\tau$，即具有平稳增量。

> [!note] 与Gauss过程、Markov过程的关系
> Brown运动既是[[Gauss 过程]]，也是连续时间Markov过程。Gauss性使其有限维分布由均值和协方差完全确定，独立增量则赋予它Markov性。

带尺度参数 $\sigma^2$ 的Brown运动可写成 $X(t)=\sigma B(t)$，其增量方差为 $\sigma^2(t-s)$。

## Brown运动与白噪声

考察差商

$$
\dfrac{B(t+h)-B(t)}{h}.
$$

其方差为 $1/|h|$，在 $h\to 0$ 时发散。因此，Brown运动的样本路径几乎必然处处不可导，也不存在通常意义下的均方导数。

**白噪声 (white noise)** $W(t)$ 可以形式化地写为Brown运动的广义导数

$$
W(t)=\dfrac{\dif B(t)}{\dif t}.
$$

它不是逐时刻具有有限方差的普通随机过程，而应理解为广义随机过程，满足

$$
\mathbb{E}\{W(t)\}=0,
\qquad
R_W(t,s)=\delta(t-s).
$$

其双边功率谱密度为常数

$$
S_W(\omega)=1.
$$

> [!danger] 「白噪声是Brown运动的导数」的含义
> 该等式只在分布或广义函数意义下成立，不能把 $W(t)$ 当作Brown样本路径的普通导数。白噪声经过稳定LTI系统后才通常得到具有有限功率的平稳输出，相关谱关系见[[随机过程的平稳性#LTI 系统对宽平稳随机过程的作用|随机过程通过LTI系统]]。

反过来，Brown运动可形式化地视作白噪声的积分

$$
B(t)=\int_0^t W(\tau)\dif\tau.
$$

## Itô微积分

对小时间增量 $\Delta t$，有

$$
\Delta B=B(t+\Delta t)-B(t)
\sim\mathscr{N}(0,\Delta t).
$$

因此 $\Delta B$ 的典型量级为 $\sqrt{\Delta t}$，其平方与 $\Delta t$ 同阶。在Itô微积分中使用记号规则

$$
(\dif B)^2=\dif t,
\qquad
\dif B\,\dif t=0,
\qquad
(\dif t)^2=0.
$$

> [!theorem] Itô公式
> 若 $X(t)$ 满足随机微分方程
> $$
> \dif X(t)=a(t,X)\dif t+b(t,X)\dif B(t),
> $$
> 且 $f(t,x)$ 足够光滑，则
> $$
> \dif f(t,X)
> =\left(
> \dfrac{\partial f}{\partial t}
> +a\dfrac{\partial f}{\partial x}
> +\dfrac{1}{2}b^2\dfrac{\partial^2 f}{\partial x^2}
> \right)\dif t
> +b\dfrac{\partial f}{\partial x}\dif B.
> $$

与普通链式法则相比，额外的二阶导数项来自 $(\dif B)^2=\dif t$。

## 几何Brown运动

**几何Brown运动 (geometric Brownian motion)**满足

$$
\dif S(t)=\mu S(t)\dif t+\sigma S(t)\dif B(t),
\qquad S(0)>0.
$$

对 $f(S)=\ln S$ 使用Itô公式可得

$$
\dif\ln S
=\left(\mu-\dfrac{\sigma^2}{2}\right)\dif t
+\sigma\dif B,
$$

因而

$$
S(t)
=S(0)\exp\!\left[
\left(\mu-\dfrac{\sigma^2}{2}\right)t+\sigma B(t)
\right].
$$

这里的 $-\sigma^2t/2$ 是Itô修正项，并保证 $\mathbb{E}\{S(t)\}=S(0)\e^{\mu t}$。相关Black–Scholes推导保留在[[例题 - 二阶随机过程与Brown运动#L6-2|几何Brown运动例题]]中，作为应用性拓展。
