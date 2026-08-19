## DFT 的定义

### DFT 的引入

[[离散时间 Fourier 变换 (DTFT)]] 是针对**无限长**信号的、**离散域向连续域**的变换，变换后的结果便于分析，但不利于计算机存储和处理。

对于 **$N$ 点长**的离散时间信号 $x[n]$，其 DTFT
$$
X(\omega) = \sum_{n=0}^{N-1} x[n] \e^{-\J \omega n}
$$
仍是**连续频谱**，但若对信号做以 $N$ 为周期的**周期延拓**，则其 DTFT 
$$
\begin{align}
\t{X} (\omega) &= \sum_{n=-\infty}^{\infty} \t{x}[n] \e^{-\J \omega n} = \sum\limits_{r=-\infty}^{\infty} \sum\limits_{n=0}^{N-1} x[n] \e^{-\J \omega (n + rN)} \\
&= X(\omega) \sum_{r=-\infty}^{\infty} \e^{-\J \omega rN} = X(\omega) \cdot \dfrac{2\pi}{N} \sum_{k=-\infty}^{\infty} \delta\left( \omega - \dfrac{2\pi k}{N} \right) \\
&= \dfrac{2\pi}{N} \sum_{k=-\infty}^{\infty} X\left( \omega \right) \Big|_{\omega = \tfrac{2\pi k}{N}} \delta\left( \omega - \dfrac{2\pi k}{N} \right)
\end{align}
$$
变为**离散频谱**，且频谱间隔为 $\dfrac{2\pi}{N}$。因而可以仅取 $N$ 个频点 $\omega_{k} = \dfrac{2\pi k}{N},\ k=0,1,\cdots,N-1$，将其定义为信号的**离散 Fourier 变换 (DFT)**。

> [!definition] 离散 Fourier 变换 (DFT)
> 设 $x[n]$ 是长度为 $N$ 的离散时间信号，则其**离散 Fourier 变换 (discrete Fourier transform, DFT)** 定义为
> $$
> X[k] = \sum_{n=0}^{N-1} x[n] \e^{-\J 2\pi nk/N}, \quad k = 0, 1, \cdots, N-1
> $$
> 其**逆变换 (Inverse DFT)** 为
> $$
> x[n] = \dfrac{1}{N} \sum_{k=0}^{N-1} X[k] \e^{\J 2\pi nk/N}, \quad n = 0, 1, \cdots, N-1
> $$

### DFT 的线性代数解释

DFT 是对离散时间信号各点的**加权求和**，其中权值为**复指数函数** $\e^{-\J 2\pi nk/N}$。将离散时间信号 $x[n]$ 看作是 $N$ 维空间 $\mathbb{C}^{N}$ 中的一个向量 $\v{x}$，其 DFT $X[k]$ 即可表为向量内积
$$
X[k] = \begin{pmatrix}
\e^{-\J 2\pi \cdot \tfrac{0k}{N}} & \e^{-\J 2\pi \cdot \tfrac{1k}{N}} & \cdots & \e^{-\J 2\pi \cdot \tfrac{(N-1)k}{N}}
\end{pmatrix} \begin{pmatrix}
x[0] \\ x[1] \\ \vdots \\ x[N-1]
\end{pmatrix}
= \v{d}_{k}^{\mathrm{H}} \v{x}
$$
其中 $\v{d}_{k} = \begin{pmatrix} \e^{\J 2\pi \cdot \tfrac{0k}{N}} & \e^{\J 2\pi \cdot \tfrac{1k}{N}} & \cdots & \e^{\J 2\pi \cdot \tfrac{(N-1)k}{N}} \end{pmatrix}^{\mathrm{T}}$。

因此，若定义 $\v{X} = \begin{pmatrix} X[0] & X[1] & \cdots & X[N-1] \end{pmatrix}^{\mathrm{T}}$，则 DFT 可写为矩阵形式
$$
\v{X} = \begin{pmatrix}
\v{d}_{0} & \v{d}_{1} & \cdots & \v{d}_{N-1}
\end{pmatrix}^{\mathrm{H}} \v{x} = \boldsymbol{D} \v{x}
$$
其中 $\boldsymbol{D} = \begin{pmatrix} \v{d}_{0} & \v{d}_{1} & \cdots & \v{d}_{N-1} \end{pmatrix}^{\mathrm{H}} = \begin{pmatrix} \v{d}_{0}^{\mathrm{H}} \\ \v{d}_{1}^{\mathrm{H}} \\ \vdots \\ \v{d}_{N-1}^{\mathrm{H}} \end{pmatrix}$ 称为 **DFT 矩阵**。

DFT 矩阵 $\boldsymbol{D}$ 的各列向量 $\v{d}_{k}$ 互相正交，且模长均为 $\sqrt{N}$，因此 DFT 为**离散正交变换**，其逆变换也可表示为矩阵
$$
\boldsymbol{E} = \boldsymbol{D}^{-1} = \dfrac{1}{N} \boldsymbol{D}^{\mathrm{H}}
$$

### DFT 的点数

DFT 不一定要让频域采样点数与信号长度相同。定义间隔为 $\cfrac{2\pi}{T}$ 的频域采样函数
$$
S_{T}(\omega) = \sum_{k=-\infty}^{\infty} \delta\left( \omega - \dfrac{2\pi k}{T} \right)
$$
其对应于时域上以 $T$ 为周期的冲激串
$$
s_{T}[n] = \sum_{r=-\infty}^{\infty} \delta[n - rT]
$$
使用 $s_{T}[n]$ 与信号 $x[n]$ 卷积进行周期延拓，即相当于频域上使用 $S_{T}(\omega)$ 进行采样。

> [!definition] $T$ 点离散 Fourier 变换
> 设 $x[n]$ 是长度为 $N$ 的离散时间信号，$T \geq N$ 为频域采样点数，则其 **$T$ 点离散 Fourier 变换**定义为
> $$
> X[k] = \sum_{n=0}^{N-1} x[n] \e^{-\J 2\pi nk/T}, \quad k = 0, 1, \cdots, T-1
> $$
> 其逆变换为
> $$
> x[n] = \dfrac{1}{T} \sum_{k=0}^{T-1} X[k] \e^{\J 2\pi nk/T}, \quad n = 0, 1, \cdots, N-1
> $$

### DFT 与其它变换的关系

#### DFT 与 DTFT 的关系

设 $x[n]$ 是长度为 $N$ 的离散时间信号，则其 DTFT 为
$$
X(\e^{\J \omega}) = \sum_{n=0}^{N-1} x[n] \e^{-\J \omega n}
$$
$N$ 点 DFT $X[k]$ 则为 DTFT 在 $N$ 个 **$N$ 等分频点** $\omega_{k} = \dfrac{2\pi k}{N}$ 处的取值，即
$$
X[k] = \sum\limits_{n=0}^{N-1} x[n] \e^{-\J 2\pi nk/N}
= X(\e^{\J \omega}) \Big|_{\omega = \tfrac{2\pi k}{N}},\quad 
k=0,1,\cdots,N-1
$$
而 $T$ 点 DFT $X[k]$ 则为 DTFT 在 $T$ 个 **$T$ 等分频点** $\omega_{k} = \dfrac{2\pi k}{T}$ 处的取值，即
$$
X[k] = \sum\limits_{n=0}^{N-1} x[n] \e^{-\J 2\pi nk/T}
= X(\e^{\J \omega}) \Big|_{\omega = \tfrac{2\pi k}{T}},\quad
k=0,1,\cdots,T-1
$$

#### DFT 与 FT 的关系

设有**连续信号** $s(t)$，其 Fourier 变换为 $S\left( \varOmega \right)$；对 $s(t)$ 以间隔 $T_{\mathrm{s}}$ 进行冲激采样，得到**采样信号** $s_{\mathrm{s}}(t) = s(t)\sum\limits_{n=-\infty}^{\infty}\delta(t-nT_{\mathrm{s}})$ 和**离散时间信号** $s_{\mathrm{D}}[n] = s(nT_{\mathrm{s}})$，则采样信号的 Fourier 变换为
$$
\begin{align} 
S_{\mathrm{s}}\left( \varOmega \right) &= \dint_{-\infty}^{\infty} s(t)\sum\limits_{n=-\infty}^{\infty}\delta(t-nT_{\mathrm{s}}) \e^{-\J \varOmega t} \dif t 
= \sum_{n=-\infty}^{\infty} \dint_{-\infty}^{\infty} s(t) \delta(t-nT_{\mathrm{s}}) \e^{-\J \varOmega t} \dif t \\
&= \sum\limits_{n=-\infty}^{\infty} s(nT_{\mathrm{s}}) \e^{-\J \varOmega nT_{\mathrm{s}}} = \sum\limits_{n=-\infty}^{\infty} s_{\mathrm{D}}[n] \e^{-\J \varOmega nT_{\mathrm{s}}} = S_{\mathrm{D}}\left( \omega \right) \Big|_{\omega = \varOmega T_{\mathrm{s}}} \\
S_{\mathrm{s}}\left( \varOmega \right) &= S\left( \varOmega \right) * \mathscr{F} \left\{ \sum_{n=-\infty}^{\infty} \delta(t-nT_{\mathrm{s}}) \right\} 
= S\left( \varOmega \right) * \dfrac{2\pi}{T_{\mathrm{s}}} \sum_{k=-\infty}^{\infty} \delta\left( \varOmega - \dfrac{2\pi k}{T_{\mathrm{s}}} \right) \\
&= \dfrac{2\pi}{T_{\mathrm{s}}} \sum_{k=-\infty}^{\infty} S\left( \varOmega - \dfrac{2\pi k}{T_{\mathrm{s}}} \right)
\end{align}
$$
进而离散时间信号的 DFT 为
$$
S_{\mathrm{D}}[k] = S_{\mathrm{D}}\left( \omega \right) \Big|_{\omega = \tfrac{2\pi k}{N}} = S_{\mathrm{s}}\left( \varOmega \right) \Big|_{\varOmega = \tfrac{2\pi k}{N T_{\mathrm{s}}}}
$$

## DFT 的性质

### 基本性质

由于 DFT 是 [[离散时间 Fourier 变换 (DTFT)|DTFT]] 的离散化，自然地保持了 [[离散时间 Fourier 变换 (DTFT)#DTFT 的性质|DTFT 的许多性质]]，如：
+ 线性，$a x_{1}[n] + b x_{2}[n] \xrightarrow{\mathrm{DFT}} a X_{1}[k] + b X_{2}[k]$。
+ 共轭，$x^{*}[n] \xrightarrow{\mathrm{DFT}} X^{*}[N-k]$，后者索引按模 $N$ 计算，实质是下述[[#循环反转]] $X^{*}[((-k))_{N}]R_{N}[k]$。
+ **对称**，$x_{\mathrm{e}}[n] \xrightarrow{\mathrm{DFT}} \Re\{ X[k] \}$，$x_{\mathrm{o}}[n] \xrightarrow{\mathrm{DFT}} \J \Im\{ X[k] \}$，$x_{\mathrm{R}}[n] \xrightarrow{\mathrm{DFT}} X_{\mathrm{e}}[k]$，$x_{\mathrm{I}}[n] \xrightarrow{\mathrm{DFT}} X_{\mathrm{o}}[k]$，其中共轭对称、共轭反对称分量也由循环反转定义。
	+ 特别地，当 $x[n]$ 为实序列时，$X[k]$ 具有共轭对称性 $X[k] = X^{*}[N-k]$。
+ Parseval 定理，$\sum\limits_{n=0}^{N-1} \vert x[n] \vert^{2} = \dfrac{1}{N} \sum\limits_{k=0}^{N-1} \vert X[k] \vert^{2}$。

### 周期性质

虽然 DFT 只定义在 $0, 1, \cdots, N-1$ 上，但由于其本质是 DTFT 在等分频点处的取值，因此 DFT 也具有**周期性**，即允许定义
$$
X[k] = X[k \bmod N]
$$
对原有的 $X[k]$ 进行**周期延拓**。

引入以 $T$ 为周期延拓的记号
$$
\t{x}[n] = x[((n))_{T}] = x [n \bmod T]
$$
当原序列长度 $N < T$ 时，空处补零；当 $N > T$ 时，**截断**为前 $T$ 点后再做**延拓**，不发生混叠。

![[延拓与混叠.png|延拓与混叠]]

#### 循环位移

对于 $N$ 点长序列 $x[n]$，其 **$m$ 点循环位移**定义为
$$
x[((n - m))_{N}] R_{N}[n]
$$

![[循环位移.png|循环位移示例]]

> [!theorem] DFT 的循环位移性质
> 设 $x[n]$ 的 DFT 为 $X[k]$，则其 $m$ 点循环位移序列 $x[((n - m))_{N}]R_{N}[n]$ 的 DFT 为
> $$
> \mathrm{DFT} \left\{ x[((n - m))_{N}] R_{N}[n] \right\} = W_{N}^{mk} X[k]
> $$
> 其中 $W_{N} = \e^{-\J 2\pi / N}$。
> 
> **时域循环位移对应频域线性相移。**

#### 循环反转

对于 $N$ 点长序列 $x[n]$，其**循环反转**定义为
$$
x[((-n))_{N}] R_{N}[n]
$$
注意循环反转是反转后延拓到原区间截断，其结果中 **0 时刻保持不变**，其余时刻按循环方式反转。

![[循环反转.png|循环反转示例]]

> [!theorem] DFT 的循环反转性质
> 设 $x[n]$ 的 DFT 为 $X[k]$，则其循环反转序列 $x[((-n))_{N}] R_{N}[n]$ 的 DFT 为
> $$
> \mathrm{DFT} \left\{ x[((-n))_{N}] R_{N}[n] \right\} = X[((-k))_{N}] R_{N}[k]
> $$
> **时域循环反转对应频域循环反转。**

#### 循环卷积

由[[#循环反转]]和[[#循环位移]]可组合为**循环卷积**，其定义为
$$
x[n] * y[n] = \sum_{m=0}^{N-1} x[((n - m))_{N}] y[m] = \sum_{m=0}^{N-1} x[m] y[((n - m))_{N}]
$$
考虑到 DTFT 中相乘与卷积有对应关系，考察 DFT 频域相乘的逆变换
$$
\begin{align}
\mathrm{IDFT} \left\{ X[k]Y[k] \right\} &= \dfrac{1}{N} \sum_{k=0}^{N-1} X[k] Y[k] W_{N}^{-nk} \\
&= \dfrac{1}{N} \sum_{k=0}^{N-1} \left( \sum_{m=0}^{N-1} x[m] W_{N}^{mk} \right) Y[k] W_{N}^{-nk} \\
&= \sum_{m=0}^{N-1} x[m] \left( \dfrac{1}{N} \sum_{k=0}^{N-1} Y[k] W_{N}^{-(n - m)k} \right) \\
&= \sum_{m=0}^{N-1} x[m] y[((n - m))_{N}]
\end{align}
$$

> [!theorem] DFT 的循环卷积性质
> 设 $x[n]$ 的 DFT 为 $X[k]$，$y[n]$ 的 DFT 为 $Y[k]$，则其循环卷积序列 $x[n] * y[n]$ 的 DFT 为
> $$
> \mathrm{DFT} \left\{ x[n] * y[n] \right\} = X[k] Y[k]
> $$
> **时域循环卷积对应频域相乘。**

## DFT 的快速计算

直接计算 DFT 需要 $O(N^{2})$ 的时间复杂度，**快速傅里叶变换 (FFT)** 则可以将时间复杂度降为 $O(N \log N)$。

### FFT 的基本思想

FFT 的基本思想是**分治法 (divide and conquer)**，将 $N$ 点 DFT 拆解为两个 $\cfrac{N}{2}$ 点 DFT 来计算。

记 $W_{N} = \e^{-\J 2\pi / N}$，称为**旋转因子 (twiddle factor)**，其性质有
+ 周期性：$W_{N}^{k+N} = W_{N}^{k}$；
+ 齐次性：$W_{N}^{k} = W_{N/m}^{k/m}$；
+ 共轭对称性：$W_{N}^{(N-n)k} = W_{N}^{-nk} = (W_{N}^{nk})^{*}$。

旋转因子幂次项中有许多特殊值可以简化计算，例如
$$
W_{N}^{0} = 1, \quad W_{N}^{N/2} = -1, \quad W_{N}^{N/4} = -\J, \quad W_{N}^{3N/4} = \J
$$
所对应项的计算均不需要复乘。在长序列中，这些项比例较小，对计算量影响不大；但**在短序列中，则可以显著减少计算量**，特别是在 $N = 2$ 与 $N = 4$ 时可**不需要任何复乘**即得到 DFT。

### 基 2 的频率抽取 FFT <br>(Decimation-in-Frequency FFT with Radix-2)

设 $N$ 为偶数，将 $x[k]$ **拆分为前后两半**，则 $N$ 点 DFT 可写为
$$
\begin{align}
&k = 2r, & X[k] &= \sum_{n=0}^{N-1} x[n] W_{N}^{nk} = \sum_{n=0}^{N/2-1} x[n] W_{N}^{n(2r)} + \sum_{n=N/2}^{N-1} x[n] W_{N}^{n(2r)} \\
&&&= \sum_{n=0}^{N/2-1} x[n] W_{N/2}^{nr} + W_{N}^{Nr} \sum_{n=0}^{N/2-1} x\left[ n + \dfrac{N}{2} \right] W_{N/2}^{nr} \\
&&&= \sum_{n=0}^{N/2-1} \left( x[n] + x\left[ n + \dfrac{N}{2} \right] \right) W_{N/2}^{nr} \\
&k = 2r + 1, & X[k] &= \sum_{n=0}^{N-1} x[n] W_{N}^{n(2r+1)} = \sum_{n=0}^{N/2-1} x[n] W_{N}^{n(2r+1)} + \sum_{n=N/2}^{N-1} x[n] W_{N}^{n(2r+1)} \\
&&&= \sum_{n=0}^{N/2-1} x[n] W_{N}^{n(2r+1)} + W_{N}^{N(2r+1)/2} \sum_{n=0}^{N/2-1} x\left[ n + \dfrac{N}{2} \right] W_{N}^{n(2r+1)} \\
&&&= \sum_{n=0}^{N/2-1} x[n] W_{N}^{n(2r+1)} - \sum_{n=0}^{N/2-1} x\left[ n + \dfrac{N}{2} \right] W_{N}^{n(2r+1)} \\
&&&= \sum_{n=0}^{N/2-1} \left( x[n] + x\left[ n + \dfrac{N}{2} \right] \right) W_{N}^{n} W_{N/2}^{nr} 
\end{align}
$$
这相当于将 $N$ 点 DFT 拆解为两个 $\cfrac{N}{2}$ 点 DFT 来计算：
+ 偶数序号 DFT 系数 $X[2r]$ 由  点长**序列 $e[n] = x[n] + x\left[ n + \cfrac{N}{2} \right]$** 的 DFT 给出；
+ 奇数序号 DFT 系数 $X[2r+1]$ 由 $\cfrac{N}{2}$ 点长**序列 $o[n] = \left( x[n] - x\left[ n + \cfrac{N}{2} \right] \right) W_{N}^{n}$** 的 DFT 给出。

对 $N = 8$ 情形，其蝶形图表示为：

![[基 2 的频率抽取 FFT 的蝶形图表示.png|基 2 的频率抽取 FFT 的蝶形图表示]]

可见：
+ 每一级蝶形运算将 $N$ 点 DFT 拆解为两个 $\cfrac{N}{2}$ 点 DFT 来计算，**共需 $\log_{2} N$ 级**，每级需 $N/2$ 个蝶形单元；
+ 每个蝶形单元共有 1 次复乘和 2 次复加。

因此，基 2 的频率抽取 FFT 的时间复杂度为 $O(N \log N)$。

上图中，输入信号 $x[k]$ 的索引顺序为自然顺序 $0, 1, 2, \cdots, 7$，而输出信号 $X[k]$ 的下标顺序为 $0, 4, 2, 6, 1, 5, 3, 7$，为原序号**二进制按位次序反转**得到的序列，称为**倒位序 (bit-reversed order)**。若需要按自然顺序输出，则需在计算后进行一次倒位序操作。

### 基 2 的时间抽取 FFT <br>(Decimation-in-Time FFT with Radix-2)

设 $N$ 为偶数，将 $x[n]$ **按奇偶项拆分**，则 $N$ 点 DFT 可写为
$$
\begin{align}
X[k] &= \sum_{n=0}^{N-1} x[n] W_{N}^{nk} = \sum_{r=0}^{N/2-1} x[2r] W_{N}^{(2r)k} + \sum_{r=0}^{N/2-1} x[2r+1] W_{N}^{(2r+1)k} \\
&= \sum_{r=0}^{N/2-1} x[2r] W_{N/2}^{rk} + W_{N}^{k} \sum_{r=0}^{N/2-1} x[2r+1] W_{N/2}^{rk}
\end{align}
$$
其中：
+ 偶数项组成 $\cfrac{N}{2}$ 点长**序列 $x_{\mathrm{e}}[r] = x[2r]$**，其 DFT 为 $X_{\mathrm{e}}[k] = \sum\limits_{r=0}^{N/2-1} x[2r] W_{N/2}^{rk}$；
+ 奇数项组成 $\cfrac{N}{2}$ 点长**序列 $x_{\mathrm{o}}[r] = x[2r+1]$**，其 DFT 为 $X_{\mathrm{o}}[k] = \sum\limits_{r=0}^{N/2-1} x[2r+1] W_{N/2}^{rk}$。

因此，$N$ 点 DFT 可写为
$$
X[k] = X_{\mathrm{e}}[k] + W_{N}^{k} X_{\mathrm{o}}[k]
$$
由于 $X_{\mathrm{e}}[k]$ 和 $X_{\mathrm{o}}[k]$ 均为周期为 $\cfrac{N}{2}$ 的序列，与 $W_{N}^{k}$ 的周期不一致，**截取到 $k = 0, 1, \cdots, N-1$** 时，$X[k]$ 可分两部分写为
$$
\begin{cases}
X[k] = X_{\mathrm{e}}[k] + W_{N}^{k} X_{\mathrm{o}}[k], \\
X\left[ k + \dfrac{N}{2} \right] = X_{\mathrm{e}}[k] - W_{N}^{k} X_{\mathrm{o}}[k], 
\end{cases}\quad
k = 0, 1, \cdots, \dfrac{N}{2}-1
$$

![[基 2 的时间抽取 FFT 的蝶形图表示.png|基 2 的时间抽取 FFT 的蝶形图表示]]

类似地，基 2 的时间抽取 FFT 的时间复杂度也为 $O(N \log N)$；得到的 DFT 系数 $X[k]$ 按照自然顺序排列，而**输入信号 $x[n]$ 则按倒位序排列**。

### 组合数 FFT

FFT 的基本思想是**分治**，将 $N$ 点 DFT 拆解为多个较小点数的 DFT 来计算。若 $N$ 可分解为多个因子之积 $N = N_{1} N_{2} \cdots N_{m}$，则可将 $N$ 点 DFT 拆解为 $N_{1}$ 个 $N_{2} N_{3} \cdots N_{m}$ 点 DFT 来计算，再将每个 $N_{2} N_{3} \cdots N_{m}$ 点 DFT 拆解为 $N_{2}$ 个 $N_{3} \cdots N_{m}$ 点 DFT 来计算，依此类推，直至拆解为若干个小点数 DFT 来计算。

对 $N = N_{1} N_{2} \cdots N_{m}$，我们将时域索引 $n$ 表示为
$$
\begin{align}
n = n_{1} + N_{1} n_{2} + N_{1} N_{2} n_{3} + \cdots + N_{1} N_{2} \cdots N_{m-1} n_{m}, \\
\begin{cases}
n_{1} = 0, 1, \cdots, N_{1}-1, \\
n_{2} = 0, 1, \cdots, N_{2}-1, \\
\vdots \\
n_{m} = 0, 1, \cdots, N_{m}-1
\end{cases}
\end{align}
$$
将频域索引 $k$ 表示为
$$
\begin{align}
k = k_{m} + N_{m} k_{m-1} + N_{m} N_{m-1} k_{m-2} + \cdots + N_{m} N_{m-1} \cdots N_{2} k_{1}, \\
\begin{cases}
k_{1} = 0, 1, \cdots, N_{1}-1, \\
k_{2} = 0, 1, \cdots, N_{2}-1, \\
\vdots \\
k_{m} = 0, 1, \cdots, N_{m}-1
\end{cases}
\end{align}
$$
引入记号 $\mathop{N}\limits_{a}^{b} = N_{a}N_{a+1} \cdots N_{b-1}N_{b}$，将 $nk$ 展开为
$$
\begin{align}
nk &= \left( n_{1} + n_{2} N_{1} + \cdots + n_{m} \mathop{N}\limits_{1}^{m-1} \right) \left( k_{m} + N_{m}k_{m-1} + \cdots + \mathop{N}\limits_{2}^{m} k_{1} \right) \\
&= \mark{ n_{1} \mathop{N}\limits_{2}^{m} k_{1} } + n_{1} \mathop{N}\limits_{3}^{m} k_{2} + \cdots + n_{1} N_{m} k_{m-1} + n_{1} k_{m} \\
&\hspace{1em}+\mathop{}\! n_{2} N k_{1} + \mark{ n_{2} N_{1} \mathop{N}\limits_{3}^{m} k_{2} } + n_{2} N_{1} \mathop{N}\limits_{4}^{m} k_{3} + \cdots + n_{2} N_{1}N_{m} k_{m-1} + n_{2} N_{1} k_{m} \\
&\hspace{1em}+\mathop{}\! \cdots \\
&\hspace{1em}+\mathop{}\! n_{m} N\mathop{N}\limits_{2}^{m-1} k_{1} + \cdots + n_{m} N k_{m-1} + \mark{ n_{m} \mathop{N}\limits_{1}^{m-1} k_{m} }
\end{align}
$$
其中，每行标记项之前的项均为 $N$ 的整数倍，第 $r$ 行标记项的 $N$ 连乘缺 $N_{r}$ 因子，故
$$
\begin{align}
W_{N}^{nk} &= \mark{ W_{N_{1}}^{n_{1} k_{1}} } \times W_{\mathop{N}\limits_{1}^{2}}^{n_{1} k_{2}} \cdots W_{\mathop{N}\limits_{1}^{m-1}}^{n_{1} k_{m-1}} W_{N}^{n_{1} k_{m}} \\
&\hspace{1em} \times 1 \times \mark{ W_{N_{2}}^{n_{2}k_{2}} } \times W_{\mathop{N}\limits_{2}^{3}}^{n_{2} k_{3}} \cdots W_{\mathop{N}\limits_{2}^{m-1}}^{n_{2} k_{m-1}} W_{\mathop{N}\limits_{2}^{m}}^{n_{2} k_{m}} \\
&\hspace{1em} \times \cdots \\
&\hspace{1em} \times 1 \times \mark{ W_{N_{m-1}}^{n_{m-1} k_{m-1}} } \times W_{N_{m-1} N_{m}}^{n_{m-1} k_{m}} \\
&\hspace{1em} \times 1 \times \mark{ W_{N_{m}}^{n_{m} k_{m}} }
\end{align}
$$
这里的每个标记项 $W_{N_{r}}^{n_{r}k_{r}}$ 都可**视为 $r$ 点 DFT 的变换基**，因此 $N$ 点 DFT 可展开为
$$
\begin{align}
X[k] &= \sum\limits_{n=0}^{N-1} x[n] W_{N}^{nk}  \\
&= \sum\limits_{n_{1}=0}^{N_{1}-1} \sum\limits_{n_{2}=0}^{N_{2}-1} \cdots \sum\limits_{n_{m}=0}^{N_{m}-1} x \left[ n_{1} + N_{1} n_{2} + \cdots + \mathop{N}\limits_{1}^{m-1} n_{m} \right] W_{N}^{{nk}} \\
&= \sum\limits_{n_{1}=0}^{N_{1}-1} \mark{ W_{N_{1}}^{n_{1} k_{1}} } \cdot W_{\mathop{N}\limits_{1}^{2}}^{n_{1} k_{2}} \cdots W_{\mathop{N}\limits_{1}^{m-1}}^{n_{1} k_{m-1}} W_{N}^{n_{1} k_{m}} &\text{（$N_{1}$ 点）} \\
&\hspace{2em}\mathop{} \sum\limits_{n_{2}=0}^{N_{2}-1} \mark{ W_{N_{2}}^{n_{2}k_{2}} } \cdot W_{\mathop{N}\limits_{2}^{3}}^{n_{2} k_{3}} \cdots W_{\mathop{N}\limits_{2}^{m-1}}^{n_{2} k_{m-1}} W_{\mathop{N}\limits_{2}^{m}}^{n_{2} k_{m}} &\text{（$N_{2}$ 点）} \\
&\hspace{3em}\mathop{} \cdots \\
&\hspace{3em}\mathop{} \sum\limits_{n_{m-1}=0}^{N_{m-1}-1} \mark{ W_{N_{m-1}}^{n_{m-1} k_{m-1}} } \cdot W_{N_{m-1} N_{m}}^{n_{m-1} k_{m}} &\text{（$N_{m-1}$ 点）} \\
&\hspace{4em}\mathop{} \sum\limits_{n_{m}=0}^{N_{m}-1} \mark{ W_{N_{m}}^{n_{m} k_{m}} } \cdot x \left[ n_{1} + N_{1} n_{2} + \cdots + \mathop{N}\limits_{1}^{m-1} n_{m} \right] &\text{（$N_{m}$ 点）}
\end{align}
$$
这里每个标记项 $W_{N_{r}}^{n_{r} k_{r}}$ 都可视为 $N_{r}$ 点 DFT 的变换基，因此 $N$ 点 DFT 可拆解为多个较小点数 DFT 来计算。

## FFT 的应用

### FFT 计算线性卷积

LTI 系统的输出 $y[n]$ 可由输入 $x[n]$ 与系统冲激响应 $h[n]$ 的**线性卷积**给出，我们期望通过 FFT 快速得到 $X[k]$ 和 $H[k]$ 来高效计算线性卷积。

一般情况下，$h[n]$ 的长度 $P$ 远小于 $x[n]$ 的长度 $N$，若直接计算 $N$ 点 DFT，则需要对 $h[n]$ 进行**大量补零**，导致计算量增大。为此，可采用**重叠保留法 (overlap-save method)** 或**重叠相加法 (overlap-add method)** 来分段计算线性卷积。

#### 重叠保留法

设输入信号 $x[n]$ 的长度为 $N$，系统冲激响应 $h[n]$ 的长度为 $P$，则线性卷积 $y[n] = x[n] * h[n]$ 的长度为 $N + P - 1$。选择分段长度 $L$，满足 $L \geq P$，则每段信号**循环卷积**贡献给线性卷积的**无混叠有效输出**长度为 $L - P + 1$。

> [!algo.] 重叠保留法计算线性卷积
> **重叠保留法**计算线性卷积的基本思想为，将输入信号 $x[n]$ 分段，每段长度为 $L$，相邻两段**重叠** $P - 1$ 点，分别与系统冲激响应 $h[n]$ 做**循环卷积**，再**保留**每段循环卷积的第 $P - 1$ 点到第 $L - 1$ 点作为线性卷积的有效输出，最后将各段有效输出**串联**得到完整线性卷积结果。
> 
> ![[重叠保留法.png]]
> 
> ---
> 
> **GIVEN —** 
> $N$ 点长输入信号 $x[n]$，长度为 $P$ 的系统冲激响应 $h[n]$
> 
> **STEPS —**
> 1. 对 $h[n]$ 做 $L$ 点 FFT，得到 $H^{L}[k] = \mathrm{DFT}_{L}\left\{ h[n] \right\}$
> 2. 将 $x[n]$ 分段，每段长度为 $L$，相邻两段重叠 $P - 1$ 点，记第 $r$ 段为 $x_{r}[n]$
> 3. 对每段 $x_{r}[n]$ **做 $L$ 点 FFT**，得到 $X_{r}^{L}[k] = \mathrm{DFT}_{L}\left\{ x_{r}[n] \right\}$，并求 $y_{rp}[n] = \mathrm{IDFT} \left\{ X_{r}^{L}[k] H^{L}[k] \right\}$
> 4. 保留 $y_{rp}[n]$ 的第 $P - 1$ 点到第 $L - 1$ 点，作为线性卷积的有效输出 $y_{r}[n]$
> 
> **OUTPUT —**
> 线性卷积结果 $y[n]$，由各段有效输出串联得到
> $$
> y[n] = \sum_{r} y_{r}[n - r(L - P + 1) + P - 1]
> $$
> 
> ---
> 
> 其中：
> + $L$ — 分段长度，满足 $L \geq P$。

#### 重叠相加法

同样给定输入信号 $x[n]$ 的长度为 $N$，系统冲激响应 $h[n]$ 的长度为 $P$。
将 $x[n]$ 分为长度为 $L$ 的子段 $x_{r}[n] = \begin{cases}x[n+rL], & 0 \le n \le L-1, \\ 0, & \text{otherwise}\end{cases}$，则线性卷积 $y[n] = x[n] * h[n]$ 可表示为
$$
y[n] = h[n] * \sum_{r=0}^{\infty} x_{r}[n - rL] = \sum_{r=0}^{\infty} h[n] * x_{r}[n - rL] 
$$

> [!algo.] 重叠相加法计算线性卷积
> **重叠相加法**计算线性卷积的基本思想为，将输入信号 $x[n]$ 分段，每段长度为 $L$，分别与系统冲激响应 $h[n]$ 做**线性卷积**，再将各段线性卷积结果**平移相加**得到完整线性卷积结果。
> 
> ---
> 
> **GIVEN —**
> $N$ 点长输入信号 $x[n]$，长度为 $P$ 的系统冲激响应 $h[n]$
> 
> **STEPS —**
> 1. 对 $h[n]$ 做 $L + P - 1$ 点 FFT，得到 $H^{L+P-1}[k] = \mathrm{DFT}_{L+P-1}\left\{ h[n] \right\}$
> 2. 将 $x[n]$ 分段，每段长度为 $L$，记第 $r$ 段为 $x_{r}[n]$
> 3. 对每段 $x_{r}[n]$ **补零做 $L + P - 1$ 点 FFT**，得到 $X_{r}^{L+P-1}[k] = \mathrm{DFT}_{L+P-1}\left\{ x_{r}[n] \right\}$，并求 $y_{r}[n] = \mathrm{IDFT} \left\{ X_{r}^{L+P-1}[k] H^{L+P-1}[k] \right\}$
> 
> **OUTPUT —**
> 线性卷积结果 $y[n]$，由各段线性卷积结果平移 $rL$ 后相加得到
> $$
> y[n] = \sum_{r} y_{r}[n - rL]
> $$
> 
> ---
> 
> 其中：
> + $L$ — 分段长度。

### 梳状滤波器组与短时傅里叶变换

#### DFT 作为滤波器组

梳状**滤波器组 (filter bank)** 由多个带通滤波器组成，每个带通滤波器提取信号的一个频段成分。

考虑一个简单的低通滤波器
$$
y[n] = \sum\limits_{k=0}^{N-1} x[n-k] ,\qquad\text{i.e.}\qquad h[n] = R_{N}[n]
$$
它输出 $x[n]$ 在**直流附近**的频率分量。若希望提取 $x[n]$ 在其他频段的频率成分，可在**频域**做 $\cfrac{2k\pi}{N}$ **移位**，相当于**时域调制**
$$
h[n] = \e^{\J \tfrac{2k\pi}{N} n} R_{N}[n]
$$
则滤波器输出为
$$
y[n] = \sum\limits_{m=0}^{N-1} x[n-m] \e^{\J \tfrac{2k\pi}{N} m}
$$
此时注意到
$$
y[N] = \sum\limits_{m=0}^{N-1} x[N-m] \e^{\J \tfrac{2k\pi}{N} m} = \sum\limits_{m'=1}^{N} x[m'] \e^{\J \tfrac{2k\pi}{N} (N-m')} = X[k]
$$
其中假定 $x[0] = x[N]$，则滤波器在 $n = N$ 处的输出即为 **$x[n]$ 的 DFT 系数 $X[k]$**。因此，每个 DFT 系数 $X[k]$ 都可视为一个中心频率在 $\cfrac{2\pi k}{N}$ 的**带通滤波器**在 $N$ 时刻的输出。

#### 短时傅里叶变换 (STFT)

短时傅里叶变换 (STFT) 是对信号的**局部时间窗**内的信号做 Fourier 变换，得到信号在**时频平面**上的表示。

> [!definition] 短时傅里叶变换 (STFT)
> 设有离散时间信号 $x[n]$，选取长度为 $W$ 的**分析窗**，则信号 $x[n]$ 的**短时傅里叶变换 (short-time Fourier transform, STFT)** 为
> $$
> X[k, n] = \mathrm{DFT} \left\{ x[n - W + r + 1] \right\} = \sum_{r=0}^{W-1} x[n - W + r + 1] \e^{-\J 2\pi kr / W}
> $$
> 其中 $k = 0, 1, \cdots, W-1$，$n$ 为时间索引。

STFT 可视为对信号 $x[n]$ 中**从 $n - W + 1$ 到 $n$** 的长度为 $W$ 的**局部时间窗**内的信号做 $W$ 点 DFT，得到该时间窗内信号的频谱表示。

即使使用 FFT，直接计算 STFT 的复杂度仍为每个时间样点 $O(W\log W)$，仍然需要较大的计算量。注意到 STFT 相邻时间窗之间**有大量重叠**，可利用这一点来减少计算量。对比
$$
\begin{align}
&X[k, n+1] = \sum\limits_{r=0}^{W-1} x[(n + 1) - W + r + 1] \e^{-\J 2\pi kr / W} \\
&X[k, n] = \sum_{r=0}^{W-1} x[n - W + r + 1] \e^{-\J 2\pi kr / W} 
\end{align}
$$
得到
$$
\begin{align}
X[k, n+1] &= \sum\limits_{r=0}^{W-2} x[(n + 1) - W + r + 1] \e^{-\J 2\pi kr / W} + x[n + 1] \e^{-\J 2\pi k (W-1) / W} \\
&= \sum\limits_{r'=1}^{W-1} x[n - W + r' + 1] \e^{-\J 2\pi k (r' - 1) / W} + x[n + 1] \e^{\J 2\pi k / W} \\
&= \left( \sum\limits_{r'=0}^{W-1} x[n - W + r' + 1] \e^{-\J 2\pi k r' / W} - x[n - W + 1] \right) \e^{\J 2\pi k / W} \\
&\hspace{1em}+ x[n + 1] \e^{\J 2\pi k / W} \\
&= \e^{\J 2\pi k / W} \left( X[k, n] - x[n - W + 1] + x[n + 1] \right) 
\end{align}
$$
即通过利用上一时刻 STFT 结果 $X[k, n]$，仅需**两次复加与一次复乘**即可得到下一时刻 STFT 结果 $X[k, n+1]$，每个时间样点的计算复杂度降为 $O(W)$。

### 正交频分复用 (OFDM)

正交频分复用 (orthogonal frequency-division multiplexing, OFDM) 是一种多载波调制技术，广泛应用于无线通信系统中，如 Wi-Fi、4G 和 5G 移动通信等。

在 OFDM 系统中，**高速数据流**被分割成多个**低速子载波**，每个子载波使用较低的符号速率进行调制。由于子载波之间是正交的，可以有效地利用频谱资源，减少符号间干扰 (inter-symbol interference, ISI)。