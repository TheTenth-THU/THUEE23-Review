## DCT 的定义

### DCT 的引入

图像（信息）压缩中，我们希望用尽量少的数据表达尽量多的信息。考虑一个离散信号 $x[n]$，对其做**离散变换 $\mathscr{T}$** 得到变换域信号 $X[k] = \mathscr{T}\{x[n]\}$，若 $X[k]$ 的大部分能量集中在较小的系数索引集合 $\varLambda$ 上，则可舍弃那些系数较小的部分，即进行**截断**
$$
X_{\varLambda}[k] = \begin{cases}
X[k], & k \in \varLambda, \\
0, & k \notin \varLambda,
\end{cases}
$$
此时，利用 $X_{\varLambda}[k]$ 进行**逆变换**可得到近似信号
$$
x_{\varLambda}[n] = \mathscr{T}^{-1}\left\{ X_{\varLambda}[k] \right\}
$$
我们希望通过选择合适的变换 $\mathscr{T}$，使得在较小的系数集合 $\varLambda$ 下，近似信号 $x_{\varLambda}[n]$ 能较好地逼近原始信号 $x[n]$。为此，引入**编码误差**
$$
|e_{\varLambda}|^{2} = \sum_{n} \left| x[n] - x_{\varLambda}[n] \right|^{2}
$$

若变换 $\mathscr{T}$ 是**正交变换**，则有**帕塞瓦尔定理 (Parseval's theorem)** 给出
$$
\begin{align}
|e_{\varLambda}|^{2} &= \sum_{n} \left| x[n] - x_{\varLambda}[n] \right|^{2} \\
&= \left( \boldsymbol{T}^{-1} \v{X} - \boldsymbol{T}^{-1} \boldsymbol{\varLambda} \v{X} \right)^{\mathrm{H}} \left( \boldsymbol{T}^{-1} \v{X} - \boldsymbol{T}^{-1} \boldsymbol{\varLambda} \v{X} \right) \\
&= \v{X}^{\mathrm{H}} \v{X} - \v{X}^{\mathrm{H}} \boldsymbol{\varLambda} \v{X} = \sum_{k \notin \varLambda} |X[k]|^{2} \\
\end{align}
$$
其中 $\boldsymbol{\varLambda} = \mathrm{diag}\left\{ \mathbb{1}_{n \in \varLambda} \right\}$，$\boldsymbol{T}$ 为变换矩阵，$\v{X} = \boldsymbol{T} \v{x}$。可见，此时**编码误差仅与被截断的系数有关**。

DFT 是序列**直接周期延拓**后的 DTFT，在两个周期的交界处会产生**不连续点**，引入了较高频率成分，导致频谱能量分布较为分散，不利于压缩。尝试将原 $N$ 点序列**对称扩展**到 $2N$ 点，然后做 $2N$ 点 DFT，即
$$
\begin{align}
x_{\mathrm{ext}}[n] &= \begin{cases}
x[n], & 0 \leq n < N, \\
x[2N - 1 - n], & N \leq n < 2N,
\end{cases} \\
X_{\mathrm{ext}}[k] &= \sum_{n=0}^{2N-1} x_{\mathrm{ext}}[n] W_{2N}^{nk} = \sum_{n=0}^{N-1} x[n] W_{2N}^{nk} + \sum_{n=N}^{2N-1} x[2N - 1 - n] W_{2N}^{nk} \\
&= \sum_{n=0}^{N-1} x[n] W_{2N}^{nk} + \sum_{m=0}^{N-1} x[m] W_{2N}^{(2N - 1 - m)k} \\
&= \sum_{n=0}^{N-1} x[n] \e^{\J \tfrac{\pi}{2N} k} ( \e^{-\J \tfrac{\pi}{2N} (2n+1)k} + \e^{\J \tfrac{\pi}{2N} (2n+1)k} ) \\
&= 2 \e^{\J \tfrac{\pi}{2N} k} \sum_{n=0}^{N-1} x[n] \cos\left( \dfrac{\pi}{2N} (2n+1)k  \right)
\end{align}
$$
其变化基函数为余弦函数 $\cos\left( \dfrac{\pi}{2N} (2n+1)k \right)$。对其做一些系数调整以保证正交性，由此引入**离散余弦变换 (DCT)**。

> [!definition] 离散余弦变换 (DCT)
> 离散余弦变换 (Discrete Cosine Transform, DCT) 是一种将离散信号转换为余弦基函数系表示的线性变换。对于长度为 $N$ 的序列 $x[n]$，其 DCT 定义为
> $$
> X_{\text{DCT}}[k] = \begin{cases}
> \sqrt{ \cfrac{1}{N} } \sum\limits_{n=0}^{N-1} x[n], & k = 0 \\
> \sqrt{ \cfrac{2}{N} } \sum\limits_{n=0}^{N-1} x[n] \cos\left( \dfrac{\pi}{2N} \left( 2n + 1 \right) k \right), & k = 1, \ldots, N-1
> \end{cases}
> $$

DCT 的输入与输出均为实数，且具有良好的能量集中特性，适用于信号压缩。

## DCT 的快速计算

DCT 可视为对称扩展后的 DFT，因此可以**利用 FFT 算法**进行快速计算。考虑长度为 $N$ 的实序列 $x[n]$，求其 DCT 即是求
$$
\chi[k] = \dfrac{1}{\sqrt{ N }} \sum_{n=0}^{N-1} x[n] \cos\left( \dfrac{\pi}{2N} (2n+1) k \right), \quad k = 0, 1, \ldots, N-1
$$
然后进行适当的系数调整。

### 对称延拓方案

定义长度为 $2N$ 的序列
$$
x_{\mathrm{ext}}[n] = \begin{cases}
x[n], & 0 \leq n < N, \\
x[2N - 1 - n], & N \leq n < 2N,
\end{cases}
$$
对其做 $2N$ 点 DFT，得到
$$
X_{\mathrm{ext}}[k] = 2 \e^{\J \tfrac{\pi}{2N} k} \sum_{n=0}^{N-1} x[n] \cos\left( \dfrac{\pi}{2N} (2n+1)k  \right)
$$
取**前 $n$ 个系数**的模长（或乘以相位因子 $\e^{-\J \tfrac{\pi}{2N} k}$），即可得到
$$
\chi[k] = \dfrac{1}{2\sqrt{N}} \e^{-\J \tfrac{\pi}{2N} k} X_{\mathrm{ext}}[k], \quad k = 0, 1, \ldots, N-1
$$

FFT 求 $X_{\text{ext}}[k]$ 的计算复杂度为 $O(N \log N)$，因此 DCT 的计算复杂度也为 $O(N \log N)$。

### 直接做 $2N$ 点 DFT

另一种方法是直接对 $x[n]$ 做 $2N$ 点 DFT，即
$$
X_{\text{DFT-}2N}[k] = \sum_{n=0}^{N-1} x[n] W_{2N}^{nk} = \sum_{n=0}^{N-1} x[n] \e^{-\J \tfrac{2\pi}{2N} nk}
$$
然后取
$$
\begin{align} 
\mathfrak{Re}\left\{ \e^{-\J \tfrac{\pi}{2N} k} X_{\text{DFT-}2N}[k] \right\} &= \mathfrak{Re}\left\{ \sum_{n=0}^{N-1} x[n] \e^{-\J \tfrac{\pi}{2N} (2n + 1)k} \right\}  \\
&= \sum_{n=0}^{N-1} x[n] \cos\left( \dfrac{\pi}{2N} (2n + 1) k \right) \\
\end{align}
$$
即知
$$
\chi[k] = \dfrac{1}{\sqrt{N}} \mathfrak{Re}\left\{ \e^{-\J \tfrac{\pi}{2N} k} X_{\text{DFT-}2N}[k] \right\}, \quad k = 0, 1, \ldots, N-1
$$

同样，FFT 求 $X_{\text{DFT-}2N}[k]$ 的计算复杂度为 $O(N \log N)$，因此 DCT 的计算复杂度也为 $O(N \log N)$。