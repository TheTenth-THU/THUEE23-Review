## Hilbert 变换的定义

### 连续时间 Hilbert 变换

#### 连续时域信号的 Hilbert 变换

设 $x(t)$ 为连续时间信号，其 Fourier 变换 $X(\J\varOmega)$ 满足
$$
X(\J\varOmega) = \begin{cases}
X(\J\varOmega), & \varOmega \ge 0, \\
0, & \varOmega < 0, \\
\end{cases}
$$
即 $x(t)$ 仅包含正频率成分。我们考虑其**实部 $x_{\mathrm{r}}(t)$ 与虚部 $x_{\mathrm{i}}(t)$ 之间**的关系，设
$$
x_{\mathrm{r}}(t) \longleftrightarrow X_{\mathrm{r}}(\J\varOmega), \qquad x_{\mathrm{i}}(t) \longleftrightarrow X_{\mathrm{i}}(\J\varOmega)
$$
则由 Fourier 变换的线性性质，可设
$$
X(\J\varOmega) = X_{\mathrm{r}}(\J\varOmega) + \J X_{\mathrm{i}}(\J\varOmega) = \begin{cases}
kX_{\mathrm{r}}(\J\varOmega), &  \varOmega \ge 0, \\
0, & \varOmega < 0
\end{cases}
$$
一种可能是
$$
X_{\mathrm{i}}(\J\varOmega) = \begin{cases}
-\J X_{\mathrm{r}}(\J\varOmega), &  \varOmega \ge 0, \\
\J X_{\mathrm{r}}(\J\varOmega), & \varOmega < 0
\end{cases} = H(\J\varOmega) X_{\mathrm{r}}(\J\varOmega)
$$
其中 $H(\J\varOmega) = -\J \sgn(\varOmega)$，其 Fourier 逆变换为
$$
h(t) = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} H(\J\varOmega) \e^{\J \varOmega t} \dif \varOmega = \dfrac{1}{\pi t}
$$
因此有
$$
x_{\mathrm{i}}(t) = x_{\mathrm{r}}(t) * h(t) = \dfrac{1}{\pi} \dint_{-\infty}^{\infty} \dfrac{x_{\mathrm{r}}(\tau)}{t - \tau} \dif \tau
$$
由此可见，信号的实部与虚部之间通过卷积关系联系在一起，这种卷积关系即为**Hilbert 变换**。

> [!definition] 连续时域 Hilbert 变换
> 连续时间信号 $x(t)$ 的 **Hilbert 变换 (Hilbert transform)** 定义为
> $$
> \hat{x}(t) = \dfrac{1}{\pi} \mathrm{P.V.} \dint_{-\infty}^{\infty} \dfrac{x(\tau)}{t - \tau} \dif \tau = x(t) * \dfrac{1}{\pi t}
> $$
> 逆变换为
> $$
> x(t) = - \dfrac{1}{\pi} \mathrm{P.V.} \dint_{-\infty}^{\infty} \dfrac{\hat{x}(\tau)}{t - \tau} \dif \tau = \hat{x}(t) * \left( - \dfrac{1}{\pi t} \right)
> $$
> 其中 $\mathrm{P.V.}\dint$ 表示**主值积分 (Cauchy principal value)**，用于处理积分中的奇点。

连续时域 Hilbert 变换描述了**频域单边**信号的**实部、虚部关系**。信号 $x(t) = x_{\mathrm{r}}(t) + \J \hat{x}_{\mathrm{r}}(t)$ 保留了 $x_{\mathrm{r}}(t)$ 的所有正频率成分，而将负频率成分全部去除，称为信号 $x_{\mathrm{r}}(t)$ 的**解析信号 (analytic signal)**。

#### 连续频域信号的 Hilbert 变换

设有因果信号 $x(t) = x(t) u(t)$，其 Fourier 变换为
$$
\mathscr{F} \left\{ x(t) \right\} = X(\J\varOmega) = X_{\mathrm{R}}(\J\varOmega) + \J X_{\mathrm{I}}(\J\varOmega)
$$
由于
$$
\mathscr{F} \left\{ u(t) \right\} = \dfrac{1}{2\pi} \left( \pi \delta(\varOmega) + \dfrac{1}{\J \varOmega} \right)
$$
则由卷积定理，有
$$
X(\J\varOmega) = X(\J\varOmega) * \mathscr{F} \left\{ u(t) \right\} = \dfrac{1}{2\pi} \left( X_{\mathrm{R}}(\J\varOmega) + \J X_{\mathrm{I}}(\J\varOmega) \right) * \left( \pi \delta(\varOmega) + \dfrac{1}{\J \varOmega} \right)
$$
展开后可得
$$
\begin{align}
&X_{\mathrm{R}}\left( \J\varOmega \right) = \dfrac{1}{2\pi} \left( \pi X_{\mathrm{R}}\left( \J\varOmega \right) + X_{\mathrm{I}}\left( \J\varOmega \right) * \dfrac{1}{\varOmega} \right) \\
&X_{\mathrm{I}}\left( \J\varOmega \right) = \dfrac{1}{2\pi} \left( \pi X_{\mathrm{I}}\left( \J\varOmega \right) - X_{\mathrm{R}}\left( \J\varOmega \right) * \dfrac{1}{\varOmega} \right)
\end{align}
$$
解出
$$
\begin{align}
&X_{\mathrm{R}}\left( \J\varOmega \right) = \dfrac{1}{\pi} X_{\mathrm{I}}\left( \J\varOmega \right) * \dfrac{1}{\varOmega} = \dfrac{1}{\pi} \mathrm{P.V.} \dint_{-\infty}^{\infty} \dfrac{X_{\mathrm{I}}(\J\varOmega')}{\varOmega - \varOmega'} \dif \varOmega' \\
&X_{\mathrm{I}}\left( \J\varOmega \right) = -\dfrac{1}{\pi} X_{\mathrm{R}}\left( \J\varOmega \right) * \dfrac{1}{\varOmega} = -\dfrac{1}{\pi} \mathrm{P.V.} \dint_{-\infty}^{\infty} \dfrac{X_{\mathrm{R}}(\J\varOmega')}{\varOmega - \varOmega'} \dif \varOmega'
\end{align}
$$

> [!definition] 连续频域 Hilbert 变换
> 连续频域信号 $X(\J\varOmega)$ 的 **Hilbert 变换 (Hilbert transform)** 定义为
> $$
> \hat{X}(\J\varOmega) = \dfrac{1}{\pi} \mathrm{P.V.} \dint_{-\infty}^{\infty} \dfrac{X(\J\varOmega')}{\varOmega - \varOmega'} \dif \varOmega'
> $$
> 逆变换为
> $$
> X(\J\varOmega) = - \dfrac{1}{\pi} \mathrm{P.V.} \dint_{-\infty}^{\infty} \dfrac{\hat{X}(\J\varOmega')}{\varOmega - \varOmega'} \dif \varOmega'
> $$
> 其中 $\mathrm{P.V.}\dint$ 表示**主值积分 (Cauchy principal value)**，用于处理积分中的奇点。

类似地，连续频域 Hilbert 变换描述了**时域单边**信号的**实部、虚部关系**。信号 $X(\J\varOmega) = X_{\mathrm{R}}(\J\varOmega) + \J \hat{X}_{\mathrm{R}}(\J\varOmega)$ 保留了 $X_{\mathrm{R}}(\J\varOmega)$ 的所有正时间成分，而将负时间成分全部去除，称为信号 $X_{\mathrm{R}}(\J\varOmega)$ 的**解析频谱 (analytic spectrum)**。

### 离散时间 Hilbert 变换

#### 离散时域信号的 Hilbert 变换

连续时间信号的 Hilbert 变换非因果，难以实现。但如果有限长冲激响应，**非因果的离散时间系统**某种意义上是可以实现的。

类比 $H(\J\varOmega) = -\J \sgn(\varOmega)$，设
$$
H(\e^{\J \omega}) = -\J \sgn(\omega) = \begin{cases}
-\J, & 0 < \omega < \pi, \\
0, & \omega = 0, \\
\J, & -\pi < \omega < 0
\end{cases}
$$
则其逆 DTFT 为
$$
h[n] = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} H(\e^{\J \omega}) \e^{\J \omega n} \dif \omega = \begin{cases}
0, & n = 0, \\
\cfrac{2}{\pi} \cfrac{\sin^{2}\left( \cfrac{\pi n}{2} \right)}{n}, & n \neq 0
\end{cases}
$$
因此，若 $z[n] = x_{\mathrm{r}}[n] + \J x_{\mathrm{i}}[n]$ 为解析信号，则与连续时间情形类似，有
$$
x_{\mathrm{i}}[n] = x_{\mathrm{r}}[n] * h[n] = \sum_{m=-\infty}^{\infty} x_{\mathrm{r}}[n - m] h[m] = \dfrac{1}{\pi} \sum_{m=-\infty}^{\infty} \dfrac{x_{\mathrm{r}}[n - (2m+1)]}{2m + 1}
$$

> [!definition] 离散时域 Hilbert 变换
> 离散时间信号 $x[n]$ 的 **Hilbert 变换 (Hilbert transform)** 定义为
> $$
> \hat{x}[n] = x[n] * h[n] = \sum_{m=-\infty}^{\infty} x[n - m] h[m] = \dfrac{1}{\pi} \sum_{m=-\infty}^{\infty} \dfrac{x[n - (2m+1)]}{2m + 1}
> $$
> 逆变换为
> $$
> x[n] = - \hat{x}[n] * h[n] = - \sum_{m=-\infty}^{\infty} \hat{x}[n - m] h[m] = - \dfrac{1}{\pi} \sum_{m=-\infty}^{\infty} \dfrac{\hat{x}[n - (2m+1)]}{2m + 1}
> $$
> 其中 $h[n] = \begin{cases}0, & n = 0, \\\cfrac{2}{\pi} \cfrac{\sin^{2}\left( \cfrac{\pi n}{2} \right)}{n}, & n \neq 0\end{cases}$。

#### 离散频域信号的 Hilbert 变换

任意序列 $x[n]$ 可分解为**奇、偶分量**，为
$$
x[n] = x_{\mathrm{e}}[n] + x_{\mathrm{o}}[n], \qquad \begin{cases}
x_{\mathrm{e}}[n] = \cfrac{1}{2} \left( x[n] + x[-n] \right), \\
x_{\mathrm{o}}[n] = \cfrac{1}{2} \left( x[n] - x[-n] \right)
\end{cases}
$$
设有实因果信号 $x[n] = x[n] u[n]$，则
$$
x[n] = 2x_{\mathrm{e}}[n] u[n] - x_{\mathrm{e}}[0] \delta[n] = 2x_{\mathrm{o}}[n] u[n] + x[0] \delta[n]
$$
解得
$$
\begin{cases}
x_{\mathrm{o}}[n] = x_{\mathrm{e}}[n] \sgn[n], \\
x_{\mathrm{e}}[n] = x_{\mathrm{o}}[n] \sgn[n] + x[0] \delta[n]
\end{cases}
$$
由 **DTFT 的共轭对称关系**，$x_{\mathrm{e}}[n] \longleftrightarrow X_{\mathrm{R}}(\e^{\J \omega})$，$x_{\mathrm{o}}[n] \longleftrightarrow \J X_{\mathrm{I}}(\e^{\J \omega})$，则有
$$
\begin{align}
&X_{\mathrm{R}}(\e^{\J \omega}) = x[0] + \dfrac{1}{2\pi} \mathrm{P.V.}\dint_{-\pi}^{\pi} X_{\mathrm{I}}(\e^{\J \omega'}) \cot\left( \dfrac{\omega - \omega'}{2} \right) \dif \omega' \\
&X_{\mathrm{I}}(\e^{\J \omega}) = -\dfrac{1}{2\pi} \mathrm{P.V.}\dint_{-\pi}^{\pi} X_{\mathrm{R}}(\e^{\J \omega'}) \cot\left( \dfrac{\omega - \omega'}{2} \right) \dif \omega'
\end{align}
$$

> [!definition] 离散频域 Hilbert 变换
> 离散频域信号 $X(\e^{\J \omega})$ 的 **Hilbert 变换 (Hilbert transform)** 定义为
> $$
> \hat{X}(\e^{\J \omega}) = - \dfrac{1}{2\pi} \mathrm{P.V.}\dint_{-\pi}^{\pi} X(\e^{\J \omega'}) \cot\left( \dfrac{\omega - \omega'}{2} \right) \dif \omega'
> $$
> 逆变换为
> $$
> X(\e^{\J \omega}) = \dfrac{1}{2\pi} \mathrm{P.V.}\dint_{-\pi}^{\pi} \hat{X}(\e^{\J \omega'}) \cot\left( \dfrac{\omega - \omega'}{2} \right) \dif \omega'
> $$
> 其中 $\mathrm{P.V.}\dint$ 表示**主值积分 (Cauchy principal value)**，用于处理积分中的奇点。


