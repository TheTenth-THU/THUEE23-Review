## Bose-Einstein 分布

对近独立玻色子，第 $i$ 个能级的平均粒子数为

$$
n_i=\frac{g_i}{\e^{\beta(\varepsilon_i-\mu)}-1}.
$$

为保证占有数非负，化学势必须满足 $\mu\le\varepsilon_0$，其中 $\varepsilon_0$ 是最低单粒子能量。取基态能量零点 $\varepsilon_0=0$ 后有 $\mu\le0$。

单个量子态的平均占有数为

$$
f(\varepsilon)=\frac1{z^{-1}\e^{\beta\varepsilon}-1},
\qquad z=\e^{\beta\mu}\le1.
$$

## 玻色—爱因斯坦凝聚

对三维均匀理想 Bose 气体，激发态粒子数为

$$
N_{\mathrm{ex}}
=\frac{V}{\lambda_T^3}g_{3/2}(z),
$$

其中 $g_s(z)=\sum_{l=1}^{\infty}\dfrac{z^l}{l^s}$。随温度降低，$z\to1$，激发态最多容纳

$$
N_{\mathrm{ex,max}}=\frac{V}{\lambda_T^3}\zeta\left(\frac32\right)
$$

个粒子。若总粒子数超过该上限，多出的粒子必须宏观占据基态，这就是**玻色—爱因斯坦凝聚 (BEC)**。

临界温度满足

$$
\mark{T_c=\frac{2\pi\hbar^2}{mk}
\left[\frac{n}{\zeta(3/2)}\right]^{2/3}.}
$$

在热力学极限且 $T<T_c$ 时，理想气体的凝聚比例为

$$
\mark{\frac{N_0}{N}=1-\left(\frac{T}{T_c}\right)^{3/2}.}
$$

> [!note] 凝聚不是普通空间液化
> BEC 是单粒子量子态的宏观占据，不要求粒子在实空间聚成小液滴。相互作用、有限尺寸和外部俘获势会改变密度分布与临界行为，但不改变这一核心判据。

## 热力学性质

均匀非相对论理想 Bose 气体的压强和内能满足

$$
p=\frac{kT}{\lambda_T^3}g_{5/2}(z),
\qquad
E=\frac32pV.
$$

凝聚相中 $z=1$，激发态承担熵和压强，而理想模型中的基态凝聚粒子不贡献动能。$T\to0$ 时全部粒子进入基态，熵趋于零。

## 与 Boltzmann 极限的关系

当逸度 $z\ll1$ 时，$g_s(z)\approx z$，Bose 分布化为

$$
f(\varepsilon)\approx z\e^{-\beta\varepsilon}
=\e^{\beta(\mu-\varepsilon)},
$$

即[[Boltzmann 统计理论#Boltzmann 分布|Boltzmann 分布]]。因此量子统计的必要性由相空间密度 $n\lambda_T^3$ 判断，而不是只由温度绝对高低判断。
