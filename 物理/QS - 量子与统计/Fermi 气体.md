

## Fermi-Dirac 分布与简并条件

Fermi 系统单个量子态的平均占有数为

$$
f(\varepsilon)=\frac1{\e^{(\varepsilon-\mu)/(kT)}+1}.
$$

Pauli 不相容原理保证 $0\le f\le1$。典型 Fermi 气体包括金属中的电子气和致密星体中的中子气；当相空间密度 $n\lambda_T^3\gtrsim1$ 时，全同性效应显著，系统进入量子简并区。

## 零温情形下的 Fermi 气体

$T \to 0 \rmu{K}$ 时，有
$$
\alpha + \beta \varepsilon_{i} = \frac{\varepsilon_{i} - \mu_{0}}{k T} \to \begin{cases}
+\infty, & \varepsilon_{i} > \mu_{0}, \\
0, & \varepsilon_{i} = \mu_{0}, \\
-\infty, & \varepsilon_{i} < \mu_{0},
\end{cases}
$$
引入**单个量子态上的平均粒子数 $f_{i} = \cfrac{n_{i}}{g_{i}}$**，则
$$
f_{i} = \frac{1}{\mathrm{e}^{(\varepsilon_{i} - \mu_{0})/k T} + 1} \to \begin{cases}
1, & \varepsilon_{i} < \mu_{0}, \\
0, & \varepsilon_{i} > \mu_{0}
\end{cases}
\qquad \text{i.e.} \qquad
n_{i} = \begin{cases}
g_{i}, & \varepsilon_{i} < \mu_{0}, \\
0, & \varepsilon_{i} > \mu_{0}
\end{cases}
$$
在零温下，所有能级**从最低能级开始依次被填满**，直到费米能级 $E_{\mathrm{F}} = \mu_{0}$ 处的能级才开始出现空穴。

对近独立非相对论粒子，**态密度**可写为
$$
g\left( \varepsilon \right) \dif \varepsilon = \frac{V \cdot 4\pi p^{2} \dif p}{h^{3}} J = \dfrac{2\pi J (2m)^{3/2}}{h^{3}} V \sqrt{ \varepsilon } \dif \varepsilon
$$
其中 $J = 2S + 1$，对**电子**而言有 $S = \cfrac{1}{2}$，$J = 2$。为简便起见，记 $C = \cfrac{2\pi J (2m)^{3/2}}{h^{3}} = \cfrac{4\pi (2m)^{3/2}}{h^{3}}$。

### Fermi 能级

由粒子数归一化条件
$$
N = \int_{0}^{E_{\mathrm{F}}} g\left( \varepsilon \right) \dif \varepsilon = C V \int_{0}^{\mu_{0}} \sqrt{ \varepsilon } \dif \varepsilon = \dfrac{2}{3} C V \mu_{0}^{3/2} 
$$
可得 **Fermi 能级**为
$$
E_{\mathrm{F}} = \mu_{0} = \left( \dfrac{3}{2C} \dfrac{N}{V} \right)^{2/3} = \dfrac{h^{2}}{2m} \left( \dfrac{3}{8\pi} \dfrac{N}{V} \right)^{2/3}
$$
具体而言，代入铜的电子密度 $N/V = 8.5 \times 10^{28} \rmu{m}^{-3}$，可得 $E_{\mathrm{F}} \sim 10^{-18} \rmu{J}$。

### 内能

零温下的内能为
$$
\begin{align}
\overline{E}_{0} &= \int_{0}^{E_{\mathrm{F}}} \varepsilon \cdot g\left( \varepsilon \right) \dif \varepsilon = C V \int_{0}^{\mu_{0}} \varepsilon \sqrt{ \varepsilon } \dif \varepsilon 
= C V \cdot \dfrac{\mu_{0}^{5/2}}{5/2} = \dfrac{2}{5} CV \mu_{0}^{5/2}  \\
&= \dfrac{2}{5} CV \left( \dfrac{3}{2C} \dfrac{N}{V} \right)^{5/3} = \dfrac{2}{5} C \left( \dfrac{3}{2C} N \right)^{5/3} V^{-2/3}
\end{align}
$$
注意到，单粒子的平均能量为
$$
\overline{\varepsilon}_{0} = \frac{\overline{E}_{0}}{N} = \frac{3}{5} \mu_{0} = \frac{3}{5} E_{\mathrm{F}}
$$

### 简并压强

对近独立非相对论粒子，设在立方体容器 $V =L^{3}$ 内，有
$$
\varepsilon_{i} = \dfrac{p_{i}^{2}}{2m} = \dfrac{\hbar^{2}}{2m} k^{2} = \dfrac{\hbar^{2}}{2m} \left( \left( \dfrac{n_{x}\pi}{L} \right)^{2} + \left( \dfrac{n_{y}\pi}{L} \right)^{2} + \left( \dfrac{n_{z}\pi}{L} \right)^{2} \right) \propto L^{-2} = V^{-2/3}
$$
这与上面内能的结果一致。可设 $\varepsilon_{i} = A_i V^{-2/3}$，其中 $A_i$ 与体积无关，于是 $\cfrac{ \partial \varepsilon_{i} }{ \partial V } = - \cfrac{2}{3} A_{i} V^{-2/3-1} = - \cfrac{2}{3} \cfrac{\varepsilon_{i}}{V}$。则有
$$
P = - \left( \frac{\partial \overline{E}}{\partial V} \right)_{N} = - \sum\limits_{i} n_{i} \dfrac{ \partial \varepsilon_{i} }{ \partial V } = \dfrac{2}{3} \dfrac{1}{V} \sum\limits_{i} n_{i} \varepsilon_{i} = \dfrac{2}{3} \dfrac{\overline{E}}{V}
$$
在零温下，有
$$
P_{0} = \dfrac{2}{3} \dfrac{\overline{E}_{0}}{V} = \dfrac{2}{5} C \left( \dfrac{3}{2C} N \right)^{5/3} V^{-5/3}
$$
