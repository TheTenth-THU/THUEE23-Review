## DTFT 的定义

### DTFT 的引入

已知连续时间信号 $f(t)$ 的 **Fourier 变换 (FT)** 定义为
$$
F(\J\varOmega) = \dint_{-\infty}^{\infty} f(t) \e^{-\J \varOmega t} \dif t
$$
以间隔 $T$ 对其进行冲激采样，得到
$$
f_{\mathrm{s}}(t) = f(t) \sum_{n=-\infty}^{\infty} \delta(t - nT) = \sum_{n=-\infty}^{\infty} f(nT) \delta(t - nT)
$$
则采样信号的 Fourier 变换为
$$
F_{\mathrm{s}}(\J\varOmega) = \dint_{-\infty}^{\infty} f_{\mathrm{s}}(t) \e^{-\J \varOmega t} \dif t = \sum_{n=-\infty}^{\infty} f(nT) \e^{-\J \varOmega nT}
$$
类比于此，考虑离散时间信号 $x[n] = f(nT)$，记采样得到的离散信号频率为 $\omega = \varOmega T$，可以定义**离散时间 Fourier 变换 (DTFT)** 如

> [!definition] 离散时间 Fourier 变换 (DTFT)
> 离散时间信号 $x[n]$ 的 **离散时间 Fourier 变换 (Discrete-Time Fourier Transform, DTFT)** 定义为
> $$
> X(\omega) = \sum_{n=-\infty}^{\infty} x[n] \e^{-\J \omega n}
> $$
> 其**逆变换 (Inverse DTFT)** 为
> $$
> x[n] = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X(\omega) \e^{\J \omega n} \dif \omega
> $$

### DTFT 与其它变换的关系

#### DTFT 与 Fourier 变换的关系

由 [[#DTFT 的引入]]可知，离散时间信号 $x[n]$ 的 DTFT 可以看作是其对应的**连续时间信号 $f(t)$ 的采样信号频谱 $F_{\mathrm{s}}\left( \J\varOmega \right)$ 在频点 $\varOmega = \dfrac{\omega}{T}$ 处的取值**，即
$$
X(\omega) = F_{\mathrm{s}}(\J\varOmega) \Big|_{\varOmega = \omega / T}
$$
由于以 $T$ 为周期的冲激采样会使频谱发生 $\dfrac{2\pi}{T}$ 的周期性重复，因此 DTFT 是周期为 $2\pi$ 的周期函数。

#### DTFT 与 $z$ 变换的关系

注意到 $x[n]$ 的 $z$ 变换为
$$
X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}
$$
则 DTFT 可以看作是 **$z$ 变换在单位圆 $z = \e^{\J \omega}$ 上的取值**，即
$$
X(\omega) = X(z) \Big|_{z = \e^{\J \omega}}
$$

### DTFT 的逆变换

将离散时间信号 $x[n]$ 看作是基底为 $\left\{ \delta[n-k] \right\}_{k}$ 的**无限维空间** $\ell^{2}$ 中的一个向量 $\v{x}$，其 DTFT $X(\omega)$ 可以看作是该向量在**另一组单位基底** $\left\{ \vu{\phi}_{\omega} \right\} = \left\{ \phi_{\omega}[n] \right\}_{\omega} = \{ \e^{\J \omega n} \}_{\omega}$ 上的**投影系数**，即
$$
X(\omega) = \left\langle  \v{x}, \vu{\phi}_{\omega}  \right\rangle = \sum_{n=-\infty}^{\infty} x[n] \e^{-\J \omega n}
$$
两组基底之间有对应关系
$$
\mathrm{DTFT}\left\{ \delta[n-k] \right\} = \e^{-\J \omega k}
$$

由于 $\left\{ \vu{\phi}_{\omega} \right\}$ 是**完备的**，因此可以通过投影系数 $X(\omega)$ 重构出原向量 $\v{x}$。考虑其基底 $\e^{\J \omega n}$ 变换回 $\delta[n-k]$ 的过程
$$
\dfrac{1}{2\pi} \dint_{-\pi}^{\pi} \e^{\J \omega n} \e^{-\J \omega k} \dif \omega = \delta[n-k]
$$
则有
$$
x[n] = \mathrm{IDTFT} \left\{ X(\omega) \right\} = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X(\omega) \e^{\J \omega n} \dif \omega
$$

### 典型信号的 DTFT

一些典型离散时间信号及其 DTFT 如下表所示：

| 信号类型        | 信号 $x[n]$                                                                      | DTFT 频谱 $X(\omega)$                                                                                 |
| :---------- | :----------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| 单位样值序列      | $\delta[n]$                                                                    | $\e^{-\J \omega \cdot 0} = 1$                                                                       |
| **矩形窗序列**   | $\begin{cases} 1, & \vert n \vert \le M, \\ 0, & \text{otherwise} \end{cases}$ | $\cfrac{\sin \cfrac{(2M + 1) \omega}{2}}{\sin \cfrac{\omega}{2}}$                                   |
| 全 1 序列      | 1                                                                              | $\sum\limits_{n=-\infty}^{\infty} \e^{\J\omega n} = 2\pi \delta(\omega)$                            |
| 复指数序列       | $\e^{\J \omega_{0} n}$                                                         | $2\pi \delta(\omega - \omega_{0})$                                                                  |
| 余弦序列        | $\cos \omega_{0}n$                                                             | $\pi \big( \delta(\omega - \omega_{0}) + \delta(\omega + \omega_{0}) \big)$                         |
| **sinc 序列** | $\cfrac{\sin \omega_{\mathrm{c}}n}{\pi n}$                                     | $\begin{cases} 1, & \vert \omega \vert < \omega_{\mathrm{c}}, \\ 0, & \text{otherwise} \end{cases}$ |

## DTFT 的性质

### 基本性质

基本变换关系：
+ **线性**，$a x_{1}[n] + b x_{2}[n] \xrightarrow{\text{DTFT}} a X_{1}(\omega) + b X_{2}(\omega)$
+ **反转**，$x[-n] \xrightarrow{\text{DTFT}} X(-\omega)$
+ **共轭**，$x^{*}[n] \xrightarrow{\text{DTFT}} X^{*}(-\omega)$

延时、调制性质： 
+ **时移**，$x[n - n_{0}] \xrightarrow{\text{DTFT}} \e^{-\J \omega n_{0}} X(\omega)$
+ **频移**，$\e^{\J \omega_{0} n} x[n] \xrightarrow{\text{DTFT}} X(\omega - \omega_{0})$

微分性质：
+ **时域差分**，$x[n] - x[n - 1] \xrightarrow{\text{DTFT}} (1 - \e^{-\J \omega}) X(\omega)$
+ **频域微分**，$\J n x[n] \xrightarrow{\text{DTFT}} \cfrac{\dif X(\omega)}{\dif \omega}$

> [!note] DTFT 性质的应用
> 可以利用离散时间信号的**离散特性**简化部分过程，例如**序列解调**中，要将中心频率为 $\omega_{0}$ 的信号变换到基带，连续时间信号中需要乘以 $\cos(\omega_{0} n)$ 再进行低通滤波，而**数字下变频 (DDC)** 任务中限定 $\omega_{0} = \cfrac{\pi}{2}$ 时只需依次**乘以 $\e^{-\J\pi n/2} = (-\J)^{n}$** 即可。
> 
> 此外，也可以利用 DTFT 频谱的**连续性**补足信号序列离散的不足，如在**延时估计**中，可以通过发射波形 $s[n]$ 和接收信号 $r[n] = s[n-n_{0}]$ 的 DTFT 频谱相差 $\e^{-\J\omega n_{0}} = \cfrac{R(\omega)}{S(\omega)}$ 中拟合得到**非整数延时 $n_{0}$**。

信号与其 DTFT 频谱之间的能量归一化关系由 **Parseval 定理**给出：
$$
\sum_{n=-\infty}^{\infty} \vert x[n] \vert^{2} = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} \vert X(\omega) \vert^{2} \dif \omega
$$

### 共轭与对称

在复数域中，函数 $f(x)$ 是**共轭对称 (conjugate symmetric)** 的，当且仅当 $f(x) = f^{*}(-x)$；函数 $f(x)$ 是**共轭反对称 (conjugate anti-symmetric)** 的，当且仅当 $f(x) = -f^{*}(-x)$。

任意离散时间信号 $x[n]$ 都可以分解为**共轭对称分量** $x_{\mathrm{e}}[n]$ 和**共轭反对称分量** $x_{\mathrm{o}}[n]$，即
$$
x[n] = x_{\mathrm{e}}[n] + x_{\mathrm{o}}[n], \qquad
\begin{cases}
x_{\mathrm{e}}[n] = \cfrac{1}{2} \left( x[n] + x^{*}[-n] \right), \\
x_{\mathrm{o}}[n] = \cfrac{1}{2} \left( x[n] - x^{*}[-n] \right)
\end{cases}
$$
考察其 DTFT，对共轭对称分量有
$$
\begin{align}
\mathrm{DTFT} \left\{ x_{\mathrm{e}}[n] \right\} &= \sum_{n=-\infty}^{\infty} x_{\mathrm{e}}[n] \e^{-\J \omega n} = \dfrac{1}{2} \sum_{n=-\infty}^{\infty} \left( x[n] + x^{*}[-n] \right) \e^{-\J \omega n} \\
&= \dfrac{1}{2} X(\omega) + \dfrac{1}{2} \sum_{m=-\infty}^{\infty} x^{*}[m] (\e^{-\J \omega m})^{*}  \\
&= \dfrac{1}{2} X(\omega) + \dfrac{1}{2} X^{*}(\omega) = \Re\{ X(\omega) \}
\end{align}
$$
类似地，对共轭反对称分量有
$$
\begin{align}
\mathrm{DTFT} \left\{ x_{\mathrm{o}}[n] \right\} &= \sum_{n=-\infty}^{\infty} x_{\mathrm{o}}[n] \e^{-\J \omega n} = \dfrac{1}{2} \sum_{n=-\infty}^{\infty} \left( x[n] - x^{*}[-n] \right) \e^{-\J \omega n} \\
&= \dfrac{1}{2} X(\omega) - \dfrac{1}{2} X^{*}(\omega) = \J \Im\{ X(\omega) \}
\end{align}
$$

另一方面，谱 $X(\omega)$ 也可以分解为**共轭对称分量** $X_{\mathrm{e}}(\omega) = \cfrac{X(\omega) + X^{*}(-\omega)}{2}$ 和**共轭反对称分量** $X_{\mathrm{o}}(\omega) = \cfrac{X(\omega) - X^{*}(-\omega)}{2}$，对其做 IDTFT，有
$$
\begin{align}
\mathrm{IDTFT} \left\{ X_{\mathrm{e}}(\omega) \right\} &= \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X_{\mathrm{e}}(\omega) \e^{\J \omega n} \dif \omega = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} \dfrac{X(\omega) + X^{*}(-\omega)}{2} \e^{\J \omega n} \dif \omega \\
&= \dfrac{1}{2} x[n] + \dfrac{1}{2} \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X^{*}(-\omega) \e^{\J \omega n} \dif \omega \\
&= \dfrac{1}{2} x[n] + \dfrac{1}{2} \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X^{*}(\omega') (\e^{-\J \omega' n})^{*} \dif \omega' \\
&= \dfrac{1}{2} x[n] + \dfrac{1}{2} x^{*}[n] = \Re\{ x[n] \} \\
\mathrm{IDTFT} \left\{ X_{\mathrm{o}}(\omega) \right\} &= \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X_{\mathrm{o}}(\omega) \e^{\J \omega n} \dif \omega = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} \dfrac{X(\omega) - X^{*}(-\omega)}{2} \e^{\J \omega n} \dif \omega \\
&= \dfrac{1}{2} x[n] - \dfrac{1}{2} x^{*}[n] = \J \Im\{ x[n] \}
\end{align}
$$

> [!theorem] DTFT 的共轭与对称性质
> 离散时间信号 $x[n]$ 的**共轭对称**分量 $x_{\mathrm{e}}[n] = \cfrac{1}{2} \left( x[n] + x^{*}[-n] \right)$ 和**共轭反对称**分量 $x_{\mathrm{o}}[n] = \cfrac{1}{2} \left( x[n] - x^{*}[-n] \right)$ 的 DTFT 分别为频谱 $X(\omega)$ 的**实部**和**虚部**，即
> $$
> \mathrm{DTFT} \left\{ x_{\mathrm{e}}[n] \right\} = \Re\{ X(\omega) \}, \qquad
> \mathrm{DTFT} \left\{ x_{\mathrm{o}}[n] \right\} = \J \Im\{ X(\omega) \}
> $$
> $x[n]$ 的**实分量** $x_{\mathrm{R}}[n] = \Re\{ x[n] \}$ 和**虚分量** $x_{\mathrm{I}}[n] = \J\Im\{ x[n] \}$ 的 DTFT 分别为频谱 $X(\omega)$ 的**共轭对称**分量和**共轭反对称**分量，即
> $$
> \begin{align} 
> &\mathrm{DTFT} \left\{ x_{\mathrm{R}}[n] \right\} = X_{\mathrm{e}}(\omega) = \dfrac{X(\omega) + X^{*}(-\omega)}{2}, \\
> &\mathrm{DTFT} \left\{ x_{\mathrm{I}}[n] \right\} = X_{\mathrm{o}}(\omega) = \dfrac{X(\omega) - X^{*}(-\omega)}{2} 
> \end{align}
> $$

### 卷积性质

类似于 Fourier 变换，DTFT 也具有卷积性质：
+ 时域两信号 $x_{1}[n]$ 和 $x_{2}[n]$ 的**线性卷积**的 DTFT 是其 **DTFT 频谱的乘积**：
$$
x_{1}[n] * x_{2}[n] \xrightarrow{\text{DTFT}} X_{1}(\omega) \cdot X_{2}(\omega)
$$
+ 频域两信号 $X_{1}(\omega)$ 和 $X_{2}(\omega)$ 的**线性卷积**（的 $\cfrac{1}{2\pi}$）是其时域信号的**乘积**的 DTFT：
$$
x_{1}[n] \cdot x_{2}[n] \xrightarrow{\text{DTFT}} \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X_{1}(\theta) X_{2}(\omega - \theta) \dif \theta = \dfrac{1}{2\pi} X_{1}(\omega) * X_{2}(\omega)
$$
这里的常数因子与 Parseval 定理中的因子一致。

可以引入**互相关函数** $r_{x_{1}x_{2}}[k] = \sum\limits_{n=-\infty}^{\infty} x_{1}[n] x_{2}^{*}[n-k]$，其 DTFT 为
$$
R_{x_{1}x_{2}}(\omega) = X_{1}(\omega) X_{2}^{*}(\omega)
$$
特别地，当 $x_{1}[n] = x_{2}[n] = x[n]$ 时，互相关函数即为**自相关函数** $r_{xx}[k] = \sum\limits_{n=-\infty}^{\infty} x[n] x^{*}[n-k]$，其 DTFT 为 $R_{xx}(\omega) = \vert X(\omega) \vert^{2}$。

### 周期性质

我们已知 $X(\omega)$ 是 **$2\pi$ 周期**函数，即 $X(\omega) = X(\omega + 2k\pi),\ k \in \mathbb{Z}$。

对于周期 $T$ 信号 $x[n] = x[n + T]$，记其在一个周期内的**截断序列**为 $\t{x}[m] = x[m],\ m = 0, 1, \cdots, T-1$，则该周期信号可表示为
$$
x[n] = \sum_{k=-\infty}^{\infty} \t{x}[n - kT] = \t{x}[n] * \sum_{k=-\infty}^{\infty} \delta[n - kT]
$$
其 DTFT 为
$$
X(\omega) = \t{X}(\omega) \cdot \dfrac{2\pi}{T} \sum_{k=-\infty}^{\infty} \delta\left( \omega - \dfrac{2\pi}{T} k \right)
$$
其中 $\t{X}(\omega)$ 是有限长信号 $\t{x}[m]$ 的 DTFT。