## IIR 滤波器的实现结构

**IIR (Infinite Impulse Response) 滤波器**是指具有**无限长冲激响应**的数字滤波器，其差分方程形如
$$
y[n] = - \sum\limits_{k=1}^{N} a_{k} y[n-k] + \sum\limits_{r=0}^{M} b_{r} x[n-r]
$$
其系统函数可表示为**有理分式**
$$
H(z) = \dfrac{B(z)}{A(z)} = \dfrac{\sum\limits_{r=0}^{M} b_{r} z^{-r}}{1 + \sum\limits_{k=1}^{N} a_{k} z^{-k}}
$$
其显著的特征是存在分母上的**反馈**回路，存在极点。

### IIR 的直接实现

#### IIR 的直接 I 型实现

一般地，IIR 滤波器可以拆分成两个**级联**子系统
$$
\begin{cases}
v[n] = \sum\limits_{r=0}^{M} b_{r} x[n-r], & \text{（滑动平均）}\\
y[n] = - \sum\limits_{k=1}^{N} a_{k} y[n-k] + v[n] & \text{（自回归）}
\end{cases}
$$
直接依次实现上述两个子系统，得到**直接 I 型实现结构**。

![[IIR 的直接 I 型实现.png]]

#### IIR 的直接 II 型实现

由于可以交换顺序，可以把延迟单元合并，得到**直接 II 型实现结构**。

![[IIR 的直接 II 型实现.png]]

### IIR 的级联实现

将系统函数 $H(z)$ 分解为若干低阶子系统的乘积
$$
H(z) = \dfrac{\prod\limits_{r=0}^{N} (1 - z_{r} z^{-1})}{\prod\limits_{k=0}^{M} (1 - p_{k} z^{-1})} = \prod\limits_{i=1}^{K} H_{i}(z)
$$
对实系数有理分式，其中每个子系统 $H_{i}(z)$ 为**一阶系统** $\cfrac{1 - g_r z^{-1}}{1 - c_k z^{-1}}$ 或 **二阶系统** $\cfrac{(1 - h_r z^{-1})(1 - h_r^{*} z^{-1})}{(1 - d_{k} z^{-1})(1 - d_k^{*} z^{-1})}$，于是 IIR 滤波器可以实现为这样多个**一阶和二阶子滤波器的级联**。子滤波器的实现可以采用直接 II 型结构。

### IIR 的并联实现

将系统函数 $H(z)$ 分解为若干低阶子系统的和
$$
\begin{align}
H(z) &= \dfrac{\sum\limits_{r=0}^{M} b_{r} z^{-r}}{1 + \sum\limits_{k=1}^{N} a_{k} z^{-k}} \\
&= \sum\limits_{k=0}^{M-N} C_{k} z^{-k} + \sum\limits_{k=1}^{N_{1}} \dfrac{A_{k}}{1 - c_{k} z^{-1}} + \sum\limits_{k=1}^{N_{2}} \dfrac{B_{k} (1 - e_{k} z^{-1})}{(1 - d_{k} z^{-1})(1 - d_{k}^{*} z^{-1})}
\end{align}
$$
即形成若干**一阶和二阶子滤波器的并联**。子滤波器的实现可以采用直接 II 型结构。

## IIR 滤波器的间接设计方法

IIR 滤波器参数量大、较难控制，因此一般采用**间接设计方法**，先设计模拟滤波器，再通过**变换**转换为数字滤波器。

间接法的设计流程为：
+ 根据数字滤波器的需求指标，**$z = g(s)$ 变换**得到模拟滤波器的需求指标；
+ 设计满足模拟滤波器需求指标的模拟滤波器 $H_{\mathrm{a}}(s)$；
+ 通过 **$s = f(z)$ 变换**将模拟滤波器转换为数字滤波器 $H(z) = H_{\mathrm{a}}(f(z))$。

### 模拟滤波器的设计

#### Butterworth 滤波器

Butterworth 滤波器的幅频特性为
$$
A\left( \J\varOmega \right) = |H_{\mathrm{a}}(\J\varOmega)|^{2} = \dfrac{1}{1 + \left( \cfrac{\varOmega}{\varOmega_{\mathrm{c}}} \right)^{2N}}
$$
其中，$-3$ dB 截止频率 $\varOmega_{\mathrm{c}}$ 和阶数 $N$ 是**待定系数**。阶数 $N$ 越大，则滤波器的过渡带越陡峭，但 $-3$ dB 的截止频率不变。

![[Butterworth 滤波器.png]]

给定设计指标 $\left( \varOmega_{\mathrm{p}}, \varOmega_{\mathrm{s}}, \delta_{1}, \delta_{2} \right)$ 后，代入得到
$$
\dfrac{1}{1 + \left( \cfrac{\varOmega_{\mathrm{p}}}{\varOmega_{\mathrm{c}}} \right)^{2N}} = (1 - \delta_{1})^{2}, \qquad 
\dfrac{1}{1 + \left( \cfrac{\varOmega_{\mathrm{s}}}{\varOmega_{\mathrm{c}}} \right)^{2N}} = \delta_{2}^{2}
$$
解得
$$
N = \left\lceil \dfrac{\log \cfrac{{1}/{(1-\delta_{1})^{2}} - 1}{{1}/{\delta_{2}^{2}} - 1}}{2 \log \dfrac{\varOmega_{\mathrm{s}}}{\varOmega_{\mathrm{p}}}} \right\rceil, \qquad
\varOmega_{\mathrm{c}} = \varOmega_{\mathrm{p}} \left( \dfrac{1}{(1-\delta_{1})^{2}} - 1 \right)^{-\tfrac{1}{2N}}
$$
Butterworth 滤波器的极点分布在以原点为中心、半径为 $\varOmega_{\mathrm{c}}$ 的圆周上。$A(s)$ 的极点位置为
$$
s_{k} = \varOmega_{\mathrm{c}} \e^{\J \pi \tfrac{2k + N - 1}{2N}}, \qquad
k = 0, 1, \cdots, 2N-1
$$
选出左半平面的极点 $s_1, s_2, \cdots, s_N$，则 **Butterworth 滤波器的系统函数**为
$$
H_{\mathrm{a}}(s) = \dfrac{\varOmega_{\mathrm{c}}^{N}}{(s - s_{1})(s - s_{2}) \cdots (s - s_{N})}
$$

#### Chebyshev 滤波器

Chebyshev 滤波器分为 **I 型**和 **II 型**两种，分别对应**通带波纹**和**阻带波纹**。

Chebyshev I 型滤波器的幅频特性为
$$
A\left( \J\varOmega \right) = |H_{\mathrm{a}}(\J\varOmega)|^{2} = \dfrac{1}{1 + \varepsilon^{2} T_{N}^{2}\left( \cfrac{\varOmega}{\varOmega_{\mathrm{c}}} \right)}
$$
其中，$T_{N}(x) = \begin{cases}\cos(N \arccos x), & |x| \le 1, \\ \cosh(N \mathop{\mathrm{arcosh}} x), & |x| > 1\end{cases}$ 为 **Chebyshev 多项式**；$\varepsilon$ 为**波纹因子**，$\varOmega_{\mathrm{c}}$ 为等波纹通带的**截止频率**，$N$ 为滤波器阶数，均为**待定系数**。

给定设计指标 $\left( \varOmega_{\mathrm{p}}, \varOmega_{\mathrm{s}}, \delta_{1}, \delta_{2} \right)$ 时，可认为 $\varOmega_{\mathrm{c}} = \varOmega_{\mathrm{p}}$；波纹因子 $\varepsilon$ 与通带最大衰减 $\delta_{1}$ 的关系为
$$
\dfrac{1}{\sqrt{ 1 + \varepsilon^{2} }} = 1 - \delta_{1}, \qquad \text{i.e.} \qquad  \varepsilon = \sqrt{\dfrac{1}{(1 - \delta_{1})^{2}} - 1}
$$
Chebyshev I 型滤波器**在通带内等波纹**，为了满足阻带衰减要求 $\delta_{2}$，需要满足
$$
\dfrac{1}{1 + \varepsilon^{2} T_{N}^{2}\left( \cfrac{\varOmega_{\mathrm{s}}}{\varOmega_{\mathrm{c}}} \right)} = \delta_{2}^{2}
$$
解得
$$
N = \left\lceil \cfrac{\mathop{\mathrm{arcosh}} \left( \cfrac{1}{\varepsilon}\sqrt{ \cfrac{1}{\delta_{2}^{2}} - 1 } \right)}{\mathop{\mathrm{arcosh}} \cfrac{\varOmega_{\mathrm{s}}}{\varOmega_{\mathrm{p}}}} \right\rceil
$$
Chebyshev I 型滤波器的极点位置为
$$
s_{k} = -a \sin \left( \dfrac{(2k - 1) \pi}{2N} \right) + \J b \cos \left( \dfrac{(2k - 1) \pi}{2N} \right), \qquad k = 1, 2, \cdots, N
$$
其中，$a = \varOmega_{\mathrm{c}} \sinh \left( \dfrac{1}{N} \mathop{\mathrm{arcsinh}} \dfrac{1}{\varepsilon} \right)$，$b = \varOmega_{\mathrm{c}} \cosh \left( \dfrac{1}{N} \mathop{\mathrm{arcsinh}} \dfrac{1}{\varepsilon} \right)$。于是，可得到**Chebyshev I 型滤波器的系统函数**为
$$
H_{\mathrm{a}}(s) = \dfrac{\cfrac{\varOmega_{\mathrm{c}}^{N}}{\varepsilon \times 2^{N-1}}}{(s - s_{1})(s - s_{2}) \cdots (s - s_{N})}
$$

Chebyshev II 型滤波器具有等波纹阻带，其幅频特性为
$$
A\left( \J\varOmega \right) = |H_{\mathrm{a}}(\J\varOmega)|^{2} = 1 - \dfrac{1}{1 + \varepsilon^{2} T_{N}^{2}\left( \cfrac{\varOmega}{\varOmega_{\mathrm{c}}} \right)} =  \cfrac{1}{1 + \cfrac{1}{\varepsilon^{2}} \cfrac{1}{T_{N}^{2}\left( \cfrac{\varOmega_{\mathrm{c}}}{\varOmega} \right)}}
$$
类似可给出其设计。

### $s$ 平面到 $z$ 平面的变换方法

#### 冲激响应不变法

冲激响应不变法基于**采样保持**的思想，将模拟滤波器的冲激响应 $h_{\mathrm{a}}(t)$ 以采样周期 $T$ 采样，得到数字滤波器的冲激响应
$$
h[n] = T h_{\mathrm{a}}(nT)
$$

模拟滤波器的系统函数可表示为
$$
H_{\mathrm{a}}(s) = \sum\limits_{k=1}^{N} \dfrac{A_{k}}{s - p_{k}}, \qquad
A_{k} = (s-s_{k}) H_{\mathrm{a}}(s) \big|_{s = p_{k}}
$$
其冲激响应为
$$
h_{\mathrm{a}}(t) = \mathscr{L}^{-1} \{ H_{\mathrm{a}}(s) \} = \sum\limits_{k=1}^{N} A_{k} \e^{p_{k} t} u(t)
$$
则数字滤波器的冲激响应为
$$
h[n] = T \sum\limits_{k=1}^{N} A_{k} \e^{p_{k} n T} u[n]
$$
得到其系统函数为
$$
H(z) = \sum\limits_{n=0}^{\infty} h[n] z^{-n} = T \sum\limits_{k=1}^{N} A_{k} \sum\limits_{n=0}^{\infty} \left( \e^{p_{k} T} z^{-1} \right)^{n} = T \sum\limits_{k=1}^{N} \dfrac{A_{k}}{1 - \e^{p_{k} T} z^{-1}}
$$

> [!theorem] 冲激响应不变法的 $s$ 到 $z$ 极点对应关系
> 基于模拟滤波器的冲激响应以采样周期 $T$ 采样得到数字滤波器的冲激响应，则模拟滤波器极点 $p_{k}$ 与数字滤波器极点 $z_{k}$ 的对应关系为
> $$
> z_{k} = \e^{p_{k} T}
> $$
> 即系统函数项的对应关系为
> $$
> \dfrac{1}{s - p_{k}} \quad \longleftrightarrow \quad \dfrac{T}{1 - \e^{p_{k} T} z^{-1}}
> $$

#### 双线性变换法

冲激响应不变法会引入**混叠失真**，因此更常用的是**双线性变换法**。其基本思想是通过压缩 $(-\infty, +\infty)$ 的 $s$ 平面 $\J\varOmega$ 轴到 $[-\pi, \pi]$ 的 $z$ 平面的角度区间，从而避免混叠失真。

具体地，令
$$
\J\varOmega = k \cdot \J\tan \left( \dfrac{\varOmega_{1} T}{2} \right) = k \dfrac{\e^{\J \varOmega_{1} T / 2} - \e^{-\J \varOmega_{1} T / 2}}{\e^{\J \varOmega_{1} T / 2} + \e^{-\J \varOmega_{1} T / 2}} 
$$
为保持 $\varOmega_{1} \to 0$ 时 $\varOmega \to 0$，须取 $k = \cfrac{2}{T}$。进而，由虚轴扩展到整个 $s$ 平面，得到
$$
s = \dfrac{2}{T} \dfrac{\e^{s_{1} T / 2} - \e^{-s_{1} T / 2}}{\e^{s_{1} T / 2} + \e^{-s_{1} T / 2}} = \dfrac{2}{T} \dfrac{1 - \e^{-s_{1} T}}{1 + \e^{-s_{1} T}}
$$
令 $z = \e^{s_{1}T}$，即得到**双线性变换**关系
$$
\mark{ s = \dfrac{2}{T} \dfrac{1 - z^{-1}}{1 + z^{-1}} }
$$
可由此将模拟滤波器的系统函数 $H_{\mathrm{a}}(s)$ 转换为数字滤波器的系统函数 $H(z)$。

在双线性变换法下，模拟频率 $\varOmega$ 与数字频率 $\omega$ 的关系为
$$
\varOmega = \dfrac{2}{T} \tan \left( \dfrac{\omega}{2} \right)
$$
数字滤波器的指标也需要相应调整。

### 数字频率变换

数字频率变换法通过对数字滤波器的系统函数进行变量替换，实现不同频率特性的滤波器设计。设有数字滤波器 $H_{\mathrm{L}}(z)$，通过**变量替换 $z = G(Z)$** 得到新的数字滤波器 
$$
H_{\mathrm{d}} (Z) = H_{\mathrm{L}}(G(Z))
$$

变量替换函数应满足：
+ 保持单位圆映射，即当 $Z = \e^{\J \omega}$ 时，$G(Z)$ 也应在单位圆上；
+ 单位圆内映射到单位圆内，以保证稳定性，即当 $|Z| < 1$ 时，$|G(Z)| < 1$。

**全通系统**的系统函数即满足上述条件，因而通常取 1 阶全通系统作为变量替换函数
$$
G(Z) = \dfrac{Z - \alpha}{1 - \alpha Z}
$$

#### 低通到低通的频率变换

设有低通滤波器 $H_{\mathrm{L}}(z)$，变量替换要求
+ 保持**通带中心频率不变**：$G(\e^{\J 0}) = \e^{\J 0}$；
+ **调整通带截止频率**位置：$z = \e^{\J \theta_{\mathrm{c}}} \longrightarrow Z = \e^{\J \omega_{\mathrm{c}}}$。

代入 $\e^{\J \theta_{\mathrm{c}}} = G(\e^{\J \omega_{\mathrm{c}}})$，解得
$$
\alpha = \cfrac{\sin \cfrac{\theta_{\mathrm{c}} - \omega_{\mathrm{c}}}{2}}{\sin \cfrac{\theta_{\mathrm{c}} + \omega_{\mathrm{c}}}{2}}
$$

#### 低通到高通的频率变换

设有低通滤波器 $H_{\mathrm{L}}(z)$，变量替换要求
+ 移动**通带中心频率到 $\pi$**：$G(\e^{\J 0}) = \e^{\J \pi}$；
+ **调整通带截止频率**位置：$z = \e^{\J \theta_{\mathrm{c}}} \longrightarrow Z = \e^{-\J \omega_{\mathrm{c}}}$。

代入 $\e^{\J \theta_{\mathrm{c}}} = G(\e^{-\J \omega_{\mathrm{c}}})$，解得
$$
\alpha = - \cfrac{\cos \cfrac{\theta_{\mathrm{c}} + \omega_{\mathrm{c}}}{2}}{\cos \cfrac{\theta_{\mathrm{c}} - \omega_{\mathrm{c}}}{2}}
$$

#### 低通到带通的频率变换

设有低通滤波器 $H_{\mathrm{L}}(z)$，变量替换要求
+ 移动**通带中心频率到 $\omega_{0}$**：$G(\e^{\J 0}) = \e^{\J \omega_{0}}$；
+ **调整通带宽度**位置：$z = \e^{\J \theta_{\mathrm{c}}} \longrightarrow Z = \e^{\J \omega_1}$ 和 $z = \e^{-\J \theta_{\mathrm{c}}} \longrightarrow Z = \e^{-\J \omega_{2}}$。

两处位置调整，使用 2 阶全通系统作为变量替换函数，代入解得
$$
\begin{cases} 
\alpha_{1} = \cfrac{-2\alpha k}{k + 1},\\
\alpha_{2} = \cfrac{k - 1}{k + 1},
\end{cases} \qquad \text{其中} \quad k = \frac{\tan \cfrac{\theta_{\mathrm{c}}}{2}}{\tan \cfrac{\omega_{2} - \omega_{1}}{2}}, \quad \alpha = \frac{\cos \cfrac{\omega_{2} + \omega_{1}}{2}}{\cos \cfrac{\omega_{2} - \omega_{1}}{2}}
$$
