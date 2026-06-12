## 金属-半导体接触基础

金属与半导体接触时，根据界面特性可分为两类：
+ **整流接触**（{Schottky|肖特基}接触）：具有类似 _pn_ 结的单向导通特性；
+ **欧姆接触 (ohmic contact)**：电流-电压关系为线性，不限制电流方向。

接触类型由金属的**功函数** $W_{\mathrm{m}}$ 与半导体的**功函数** $W_{\mathrm{s}}$ 及**电子亲合能** $\chi$ 共同决定。详见[[固体的电特性#功函数|功函数的定义]]。

## 理想 Schottky 势垒

### 能带模型

以 _n_ 型半导体与金属的接触为例。接触前，两者具有各自的 Fermi 能级和真空能级。接触后，热平衡要求两者 Fermi 能级对齐，电子将从功函数较小的一侧流向另一侧，在界面处形成空间电荷区。

若 $W_{\mathrm{m}} > W_{\mathrm{s}}$，半导体中的电子流向金属，半导体表面留下带正电的电离施主，形成**耗尽层**。能带在界面处向上弯曲，对半导体中的电子形成一个势垒。

> [!definition] {Schottky|肖特基}势垒高度
> 在不考虑界面态的理想情况下，_n_ 型半导体一侧的 **Schottky 势垒高度**（从金属 Fermi 能级到半导体导带底的能量差）为
> $$
> \mark{ \phi_{\mathrm{Bn}} = W_{\mathrm{m}} - \chi }
> $$
> 半导体侧的**内建电势**（能带弯曲量）为 $V_{\mathrm{bi}} = W_{\mathrm{m}} - W_{\mathrm{s}} = \phi_{\mathrm{Bn}} - (E_{\mathrm{c}} - E_{\mathrm{F}})$。

对于 _p_ 型半导体，势垒高度为 $\phi_{\mathrm{Bp}} = E_{\mathrm{g}} + \chi - W_{\mathrm{m}}$（单位为能量），方向与 _n_ 型相反。

### 耗尽层特性

与 _pn_ 结类似，Schottky 结的耗尽层宽度由 Poisson 方程导出。对均匀掺杂的 _n_ 型半导体
$$
W = \sqrt{ \frac{2 \varepsilon_{\mathrm{s}} (V_{\mathrm{bi}} - V)}{q N_{\mathrm{D}}} }
$$
空间电荷密度为常数 $q N_{\mathrm{D}}^{+}$，电场线性分布，电势抛物线分布。最大电场在界面处
$$
E_{\max} = \frac{q N_{\mathrm{D}} W}{\varepsilon_{\mathrm{s}}} = \sqrt{ \frac{2 q N_{\mathrm{D}} (V_{\mathrm{bi}} - V)}{\varepsilon_{\mathrm{s}}} }
$$

## 电流输运机制

Schottky 结的电流输运由**多数载流子**主导——这与 _pn_ 结的少数载流子注入有本质区别，因此 Schottky 二极管具有更高的开关速度。

### 热电子发射理论

对于迁移率较高的半导体（如 Si、GaAs），电流的主要机制是**热电子发射 (thermionic emission)**：电子以热运动方式越过势垒顶部。

由 Richardson-Dushman 方程，从半导体流向金属的电流密度为
$$
J_{\mathrm{s} \to \mathrm{m}} = A^{*} T^{2} \exp\left( -\frac{q \phi_{\mathrm{Bn}}}{k_{\mathrm{B}}T} \right) \exp\left( \frac{q V}{k_{\mathrm{B}}T} \right)
$$
其中 $A^{*} = \dfrac{4\pi q m^{*} k_{\mathrm{B}}^{2}}{h^{3}}$ 是**有效 Richardson 常数**。从金属流向半导体的电流与偏压无关，为
$$
J_{\mathrm{m} \to \mathrm{s}} = - A^{*} T^{2} \exp\left( -\frac{q \phi_{\mathrm{Bn}}}{k_{\mathrm{B}}T} \right)
$$

> [!theorem] Schottky 二极管的 I-V 特性（热电子发射模型）
> 总电流密度为两方向电流之和
> $$
> \mark{ J = J_{\mathrm{ST}} \left( \exp\left( \frac{q V}{k_{\mathrm{B}}T} \right) - 1 \right) }
> $$
> 其中反向饱和电流密度为
> $$
> J_{\mathrm{ST}} = A^{*} T^{2} \exp\left( -\frac{q \phi_{\mathrm{Bn}}}{k_{\mathrm{B}}T} \right)
> $$

这一形式与[[𝑝𝑛结#Shockley 方程|pn 结的 Shockley 方程]]相同，但物理机制不同：
+ Schottky 结的 $J_{\mathrm{ST}}$ 远大于 _pn_ 结的反向饱和电流（因 $\phi_{\mathrm{Bn}} < E_{\mathrm{g}}$，且为多数载流子过程）；
+ Schottky 结的开启电压较低（通常 $0.2 \sim 0.5\rmu{V}$，而 Si _pn_ 结约 $0.7\rmu{V}$）。

### 扩散理论

对于迁移率较低的半导体，电子在耗尽层中的漂移和扩散可能成为限速步骤。此时电流密度由**扩散理论**描述
$$
J = q \mu_{\mathrm{n}} N_{\mathrm{c}} E_{\max} \exp\left( -\frac{q \phi_{\mathrm{Bn}}}{k_{\mathrm{B}}T} \right) \left( \exp\left( \frac{q V}{k_{\mathrm{B}}T} \right) - 1 \right)
$$
其形式与热电子发射理论相似，但前置因子不同。

### 实际 Schottky 结的 I-V 特性

实际 Schottky 二极管的 I-V 特性通常表示为
$$
J = J_{\mathrm{s}} \left( \exp\left( \frac{q(V - I R_{\mathrm{s}})}{\eta k_{\mathrm{B}}T} \right) - 1 \right)
$$
其中 $R_{\mathrm{s}}$ 是串联电阻，$\eta$ 是理想因子（通常 $1.0 \sim 1.1$，比 _pn_ 结更接近 1）。

## 界面态的影响与 Fermi 能级钉扎

### 界面态

实际半导体表面存在大量由**悬挂键、表面重构、吸附杂质**等引入的**界面态 (interface states)**，在禁带中形成连续分布的能级。界面态可捕获或释放电荷，对 Schottky 势垒高度产生重要影响。

高密度界面态下，半导体表面的 Fermi 能级被**钉扎 (pinning)** 在界面态的**电荷中性能级** $E_{0}$ 附近，此时
$$
\phi_{\mathrm{Bn}} \approx E_{\mathrm{g}} - E_{0}
$$
势垒高度几乎与金属功函数无关。例如，共价半导体（Si、GaAs）通常表现出较强的 Fermi 能级钉扎效应，使得不同金属形成的 Schottky 势垒高度变化远小于理想模型的预测。

### 镜像力降低

电子靠近金属表面时，在金属中感应出镜像正电荷，对电子产生吸引力。这一镜像力使势垒高度实际降低
$$
\Delta \phi = \sqrt{ \frac{q E_{\max}}{4 \pi \varepsilon_{\mathrm{s}}} }
$$
反向偏压越大，$E_{\max}$ 越大，势垒降低越多——这解释了实际 Schottky 二极管的反向电流随反向偏压缓慢增大的现象。

## 欧姆接触

当金属与半导体形成的接触不具备整流特性时，称为**欧姆接触**。理想欧姆接触的 I-V 特性为线性，接触电阻极小，不影响器件性能。

形成欧姆接触的条件：
+ 对 _n_ 型半导体，需 $W_{\mathrm{m}} < W_{\mathrm{s}}$，此时半导体表面能带向下弯曲，形成**积累层**而非耗尽层；
+ 极高浓度的掺杂（$> 10^{19}\rmu{cm}^{-3}$）使耗尽层极薄，电子可通过隧穿穿透势垒——即使 $W_{\mathrm{m}} > W_{\mathrm{s}}$ 也能形成欧姆接触。

实际器件中广泛采用**重掺杂隧穿欧姆接触**，如 Si 工艺中的金属硅化物技术。

> [!note] Schottky 结与 _pn_ 结的对比
> 
> | 特性 | Schottky 结 | _pn_ 结 |
> |------|------------|--------|
> | 载流子类型 | **多数载流子** | 少数载流子 |
> | 反向饱和电流 | 较大 | 较小 |
> | 开启电压 | $0.2\sim0.5\rmu{V}$ | $0.6\sim0.8\rmu{V}$（Si） |
> | 开关速度 | 极快（无少子储存） | 受少子储存限制 |
> | 主要应用 | 高频整流、微波检测 | 整流、稳压、发光 |

## MIS 结构

**MIS 结构（金属-绝缘体-半导体）** 是 MOSFET 器件的核心。在半导体与金属之间加入绝缘层（通常是 SiO$_{2}$），避免了 Schottky 结中的电流导通，转而通过**场效应**控制半导体表面载流子浓度。

### 表面状态

在 MIS 结构上加栅压 $V_{\mathrm{G}}$，半导体表面可能出现三种状态：
+ **积累 (accumulation)**：$V_{\mathrm{G}}$ 吸引多数载流子到表面（如 _p_ 型半导体加负压），表面电导增强；
+ **耗尽 (depletion)**：$V_{\mathrm{G}}$ 排斥多数载流子（如 _p_ 型半导体加正压），表面形成耗尽层；
+ **反型 (inversion)**：$V_{\mathrm{G}}$ 足够大时，表面的少数载流子浓度超过多数载流子浓度，表面导电类型反转。

反型状态的 onset 条件为表面势 $\psi_{\mathrm{s}} = 2 \phi_{\mathrm{F}}$，其中 $\phi_{\mathrm{F}} = (E_{\mathrm{i}} - E_{\mathrm{F}}) / q$ 是体 Fermi 势。对应的栅压称为**阈值电压** $V_{\mathrm{th}}$。

> [!note] MOSFET 的阈值电压
> MOSFET 的阈值电压由平带电压、耗尽层电荷和表面反型条件共同决定
> $$
> V_{\mathrm{th}} = V_{\mathrm{FB}} + 2\phi_{\mathrm{F}} + \frac{\sqrt{4 \varepsilon_{\mathrm{s}} q N_{\mathrm{A}} \phi_{\mathrm{F}}}}{C_{\mathrm{ox}}}
> $$
> 其中 $V_{\mathrm{FB}}$ 是平带电压（补偿功函数差和氧化层电荷影响），$C_{\mathrm{ox}}$ 是单位面积氧化层电容。
