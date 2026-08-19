## Boltzmann 分布

对可分辨定域粒子，或满足半经典条件 $n\lambda_T^3\ll1$ 的稀薄气体，平衡时第 $i$ 个能级的平均粒子数为

$$
\mark{n_i=g_i\e^{-\alpha-\beta\varepsilon_i}
=g_i\e^{\beta(\mu-\varepsilon_i)},}
$$

其中 $g_i$ 是能级简并度，$\beta=1/(kT)$，$\alpha=-\mu/(kT)$。

定义单粒子配分函数

$$
\mark{z=\sum_i g_i\e^{-\beta\varepsilon_i}.}
$$

由 $\sum_i n_i=N$ 得 $\e^{-\alpha}=N/z$，故

$$
n_i=N\frac{g_i\e^{-\beta\varepsilon_i}}{z}.
$$

这表明单粒子处于能级 $i$ 的概率正比于 Boltzmann 因子 $\e^{-\beta\varepsilon_i}$。

## 多粒子配分函数

若 $N$ 个定域、可分辨且相互独立的粒子具有相同单粒子配分函数 $z$，则

$$
Z_N=z^N.
$$

对不可区别但处于 Boltzmann 极限的理想气体，应消除粒子标签造成的重复计数：

$$
\mark{Z_N=\frac{z^N}{N!}.}
$$

> [!danger] $1/N!$ 的适用边界
> 定域在不同格点、因位置可区分的粒子不除以 $N!$；可在整个容器中交换位置的同类理想气体需要该因子。二者混用会导致熵和化学势错误。

若平动、转动、振动和电子自由度近似独立，则单粒子能量可加，配分函数可乘：

$$
z=z_{\mathrm{tr}}z_{\mathrm{rot}}z_{\mathrm{vib}}z_{\mathrm{el}}.
$$

这使不同自由度对热力学量的贡献可以分别计算，典型应用见[[理想气体]]。

## 由配分函数计算热力学量

在正则系综中，Helmholtz 自由能为

$$
\mark{F=-kT\ln Z_N.}
$$

进而

$$
E=-\frac{\partial\ln Z_N}{\partial\beta},
\qquad
S=k(\ln Z_N+\beta E),
$$

$$
p=kT\left(\frac{\partial\ln Z_N}{\partial V}\right)_{T,N},
\qquad
\mu=-kT\left(\frac{\partial\ln Z_N}{\partial N}\right)_{T,V}.
$$

定容热容量可写为

$$
C_V=\left(\frac{\partial E}{\partial T}\right)_{V,N}
=k\beta^2\frac{\partial^2\ln Z_N}{\partial\beta^2}.
$$

## 态密度与准连续近似

能级足够密集时，可用态密度 $g(\varepsilon)$ 将求和化为积分：

$$
z=\sum_i g_i\e^{-\beta\varepsilon_i}
\longrightarrow
\int_0^\infty g(\varepsilon)\e^{-\beta\varepsilon}\dif\varepsilon.
$$

三维自由粒子的态密度与 $V\sqrt\varepsilon$ 成正比，因此平动配分函数为

$$
z_{\mathrm{tr}}=\frac{V}{\lambda_T^3},
\qquad
\lambda_T=\frac{h}{\sqrt{2\pi m kT}},
$$

若还有内部简并度 $g$，右侧再乘 $g$。

## 熵的统计意义

最可几分布处的微观态数 $W_{\max}$ 给出

$$
S=k\ln W_{\max}.
$$

与配分函数形式 $S=k(\ln Z_N+\beta E)$ 相比，两种路线分别从状态计数和状态概率出发，在热力学极限下给出相同的平衡熵。
