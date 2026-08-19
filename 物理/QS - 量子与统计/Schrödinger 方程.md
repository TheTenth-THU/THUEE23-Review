## 含时 Schrödinger 方程

非相对论量子态的幺正演化由 Hamilton 算符生成：

$$
\mark{\I\hbar\frac{\partial}{\partial t}\varPsi(\v r,t)=\hat H\varPsi(\v r,t).}
$$
^SchrodingerFangcheng

对质量为 $m$、处于实标量势 $V(\v r,t)$ 中的单粒子，

$$
\hat H=-\frac{\hbar^2}{2m}\nabla^2+V(\v r,t),
$$

因而

$$
\I\hbar\frac{\partial\varPsi}{\partial t}
=-\frac{\hbar^2}{2m}\nabla^2\varPsi+V\varPsi.
$$

Schrödinger 方程对时间是一阶方程，给定某时刻的完整量子态即可确定封闭系统此后的演化；方程的线性性保证态的叠加仍是解。

## 概率守恒

定义概率密度与概率流密度

$$
\rho=|\varPsi|^2,\qquad
\v J=\frac{\hbar}{2m\I}\left(\varPsi^*\nabla\varPsi-\varPsi\nabla\varPsi^*\right).
$$

将 Schrödinger 方程及其复共轭式组合可得连续性方程

$$
\mark{\frac{\partial\rho}{\partial t}+\nabla\cdot\v J=0.}
$$

若无穷远处概率流为零，则对全空间积分得到 $\dfrac{\dif}{\dif t}\int\rho\dif^3r=0$，即总概率守恒。

## 定态 Schrödinger 方程

若势能不显含时间，可令 $\varPsi(\v r,t)=\psi(\v r)T(t)$。分离变量后得到

$$
T(t)=\e^{-\I Et/\hbar},\qquad
\mark{\hat H\psi(\v r)=E\psi(\v r).}
$$
^DingtaiSchrodingerFangcheng

后一式是**定态 Schrödinger 方程**，本质上是 Hamilton 算符的本征值问题。单个能量本征态的概率密度 $|\varPsi|^2=|\psi|^2$ 与时间无关，因此称为定态；多个不同能量本征态的叠加一般会出现随时间变化的干涉项。

> [!note] 定态与静止
> 定态只表示概率密度和力学量统计分布不随时间变化，不表示粒子具有一条静止轨迹。定态仍可具有非零概率流。

## 一般解与能量展开

若 $\{\psi_n\}$ 是离散能谱的完备正交本征函数系，则任意初态可展开为

$$
\varPsi(\v r,0)=\sum_n c_n\psi_n(\v r),\qquad
c_n=\int\psi_n^*(\v r)\varPsi(\v r,0)\dif^3r.
$$

其时间演化为

$$
\varPsi(\v r,t)=\sum_n c_n\psi_n(\v r)\e^{-\I E_nt/\hbar}.
$$

测量能量得到 $E_n$ 的概率为 $|c_n|^2$。若存在连续谱，求和应相应替换为积分。

## 一维定态问题的一般性质

对实势 $V(x)$，一维定态方程为

$$
-\frac{\hbar^2}{2m}\frac{\dif^2\psi}{\dif x^2}+V(x)\psi=E\psi.
$$

若 $E$ 低于两侧无穷远处的势能，波函数在无穷远处衰减，形成束缚态；若至少在一侧振荡，则形成散射态。由 Wronskian 与束缚边界条件可证明一维束缚态不简并。

若势满足 $V(-x)=V(x)$，则 Hamilton 算符与宇称算符对易；一维束缚态又不简并，因此每个束缚态都可取确定的奇宇称或偶宇称。 ^YuchengDingli

典型边界条件与解析解分别见[[一维束缚态与散射]]和[[一维线性谐振子]]。
