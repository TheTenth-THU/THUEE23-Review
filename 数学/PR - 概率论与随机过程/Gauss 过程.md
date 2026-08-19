## Gauss 过程的引入

### 多元 Gauss 分布

对于多维随机变量 $\v{X} = \begin{pmatrix}X_{1} & X_{2} & \cdots & X_{n}\end{pmatrix}^{\mathrm{T}}$，如果 $\mathbb{E} \left[ |X_{k}|^{2} \right] < \infty$，则其**均值向量 (mean vector)** 定义为
$$
\v{\mu} = \mathbb{E}[\v{X}] = \begin{pmatrix} \mathbb{E}[X_{1}] & \mathbb{E}[X_{2}] & \cdots & \mathbb{E}[X_{n}] \end{pmatrix}^{\mathrm{T}}
$$
其**协方差矩阵 (covariance matrix)** 定义为
$$
\boldsymbol{\varSigma} = \mathbb{E} \left[ (\v{X} - \v{\mu})(\v{X} - \v{\mu})^{\mathrm{T}} \right] = \Big( \mathbb{E} \big[ (X_{i} - \mathbb{E} \left[ X_{i} \right] )(X_{j} - \mathbb{E} \left[ X_{j} \right] ) \big]  \Big)_{i,j}
$$

> [!definition] 多元 Gauss 分布
> 设 $\v{X} = \begin{pmatrix}X_{1} & X_{2} & \cdots & X_{n}\end{pmatrix}^{\mathrm{T}}$ 是 $n$ 维随机变量，如果 $\v{X}$ 的联合概率密度函数形如
> $$
> f_{\v{X}}\left( \v{x} \right) = k \exp\left( -\dfrac{1}{2} \left( \v{x} - \v{\mu} \right)^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \left( \v{x} - \v{\mu} \right) \right)
> $$
> 则称 $\v{X}$ 服从 $n$ 元 **Gauss 分布 (Gaussian distribution)**，记为 $\v{X} \sim N(\v{\mu}, \boldsymbol{\varSigma})$，其中 $k \in \mathbb{R}$，$\v{\mu} \in \mathbb{R}^{n}$，$\boldsymbol{\varSigma} \in \mathbb{R}^{n \times n}$ 对称正定。

#### 多元 Gauss 分布的归一化

由 $\boldsymbol{\varSigma}$ 对称正定，可知 $\boldsymbol{\varSigma}$ 可对角化，即存在正交矩阵 $\boldsymbol{U}$ 和对角矩阵 $\boldsymbol{\varLambda} = \mathrm{diag}(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n})$，使得
$$
\boldsymbol{\varSigma} = \boldsymbol{U} \boldsymbol{\varLambda} \boldsymbol{U}^{\mathrm{T}}
$$
其中 $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n} > 0$ 是 $\boldsymbol{\varSigma}$ 的特征值。此处引入
$$
\boldsymbol{B} = \boldsymbol{\varLambda}^{-1/2} \boldsymbol{U}^{\mathrm{T}}
$$
则 $\boldsymbol{\varSigma}^{-1} = \boldsymbol{B} \boldsymbol{B}^{\mathrm{T}}$，进而
$$
\begin{align}
\left( \v{x} - \v{\mu} \right)^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \left( \v{x} - \v{\mu} \right) &= \left( \v{x} - \v{\mu} \right)^{\mathrm{T}} (\boldsymbol{B} \boldsymbol{B}^{\mathrm{T}}) \left( \v{x} - \v{\mu} \right)  \\
&= \left( \boldsymbol{B} (\v{x} - \v{\mu}) \right)^{\mathrm{T}} \left( \boldsymbol{B} (\v{x} - \v{\mu}) \right)
\end{align}
$$
可做变量替换 $\v{y} = \boldsymbol{B} (\v{x} - \v{\mu}) = \boldsymbol{\varLambda}^{-1/2} \boldsymbol{U}^{\mathrm{T}} (\v{x} - \v{\mu})$，这一变换的 Jacobian 行列式为
$$
\left| \dfrac{ \partial \v{y} }{ \partial \v{x} } \right| = |\det \boldsymbol{B}| = |\det \boldsymbol{\varLambda}|^{-1/2} |\det \boldsymbol{U} | = | \det\boldsymbol{\varSigma}|^{-1/2}
$$

尝试**确定归一化系数 $k$**，归一化条件要求
$$
\begin{align}
1 &= \dint_{\mathbb{R}^{n}} f_{\v{X}}(\v{x}) \dif \v{x} = k \dint_{\mathbb{R}^{n}} \exp\left( -\dfrac{1}{2} \left( \v{x} - \v{\mu} \right)^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \left( \v{x} - \v{\mu} \right) \right) \dif \v{x} \\
&= k \dint_{\mathbb{R}^{n}} \exp\left( -\dfrac{1}{2} \v{y}^{\mathrm{T}} \v{y} \right) |\det \boldsymbol{\varSigma}|^{1/2} \dif \v{y} \\
&= k |\det \boldsymbol{\varSigma}|^{1/2} \prod\limits_{i=1}^{n} \dint_{-\infty}^{\infty} \exp\left( -\dfrac{1}{2} y_{i}^{2} \right) \dif y_{i} = k |\det \boldsymbol{\varSigma}|^{1/2} (2\pi)^{n/2}
\end{align}
$$
故 $k = (2\pi)^{-n/2} |\det \boldsymbol{\varSigma}|^{-1/2}$，多元 Gauss 分布的概率密度函数为
$$
\mark{ f_{\v{X}}\left( \v{x} \right) = \dfrac{1}{(2\pi)^{n/2} |\det \boldsymbol{\varSigma}|^{1/2}} \exp\left( -\dfrac{1}{2} \left( \v{x} - \v{\mu} \right)^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \left( \v{x} - \v{\mu} \right) \right) }
$$

特别地，**二维 Gauss 分布**的协方差矩阵常记为 $\boldsymbol{\varSigma} = \begin{pmatrix}\sigma_{1}^{2} & \rho\sigma_{1}\sigma_{2} \\ \rho\sigma_{1}\sigma_{2} & \sigma_{2}^{2}\end{pmatrix}$，其中 $\sigma_{1}^{2} > 0$，$\sigma_{2}^{2} > 0$，$-1 < \rho < 1$，此时其概率密度函数为
$$
\begin{align} 
f_{\v{X}}\left( \v{x} \right) &= \dfrac{1}{2\pi \sigma_{1} \sigma_{2} \sqrt{1 - \rho^{2}}}  \\
&\hspace{1.2em} \cdot \exp\left( -\dfrac{1}{2(1 - \rho^{2})} \left( \dfrac{(x_{1} - \mu_{1})^{2}}{\sigma_{1}^{2}} - \dfrac{2\rho (x_{1} - \mu_{1})(x_{2} - \mu_{2})}{\sigma_{1}\sigma_{2}} + \dfrac{(x_{2} - \mu_{2})^{2}}{\sigma_{2}^{2}} \right) \right) 
\end{align}
$$

#### 多元 Gauss 分布的特征函数

对随机向量 $\v{X} \in \mathbb{R}^{n}$，引入 $\v{\omega} \in \mathbb{R}^{n}$ 的函数
$$
\phi_{\v{X}}(\v{\omega}) = \mathbb{E} \left[ \exp(\J \v{\omega}^{\mathrm{T}} \v{X}) \right]
= \dint_{\mathbb{R}^{n}} \exp(\J \v{\omega}^{\mathrm{T}} \v{x}) f_{\v{X}}(\v{x}) \dif \v{x}
$$
称为 $\v{X}$ 的**特征函数 (characteristic function)**。

对多元 Gauss 分布，有
$$
\begin{align}
\phi_{\v{X}}(\v{\omega}) &= \dint_{\mathbb{R}^{n}} \exp(\J \v{\omega}^{\mathrm{T}} \v{x}) f_{\v{X}}(\v{x}) \dif \v{x} \\
&= \dfrac{1}{(2\pi)^{n/2} |\det \boldsymbol{\varSigma}|^{1/2}} \dint_{\mathbb{R}^{n}} \exp\left( \J \v{\omega}^{\mathrm{T}} \v{x} - \dfrac{1}{2} (\v{x} - \v{\mu})^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} (\v{x} - \v{\mu}) \right) \dif \v{x}
\end{align}
$$
为计算上面积分，首先考虑一元情况，可配方得到
$$
\begin{align}
\J \omega x - \dfrac{1}{2\sigma^{2}} (x - \mu)^{2} &= -\dfrac{1}{2\sigma^{2}} \left( x^{2} - 2(\mu + \J \sigma^{2} \omega) x + \mu^{2} \right) \\
&= -\dfrac{1}{2\sigma^{2}} \left( x - \mu - \J \sigma^{2} \omega \right)^{2} + \J \mu \omega - \dfrac{1}{2} \sigma^{2} \omega^{2}
\end{align}
$$
类似地，对多元情况，有
$$
\begin{align}
&\J \v{\omega}^{\mathrm{T}} \v{x} - \dfrac{1}{2} (\v{x} - \v{\mu})^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} (\v{x} - \v{\mu}) \\
&= -\dfrac{1}{2} \left( \v{x} - \v{\mu} - \J \boldsymbol{\varSigma} \v{\omega} \right)^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \left( \v{x} - \v{\mu} - \J \boldsymbol{\varSigma} \v{\omega} \right) + \J \v{\mu}^{\mathrm{T}} \v{\omega} - \dfrac{1}{2} \v{\omega}^{\mathrm{T}} \boldsymbol{\varSigma} \v{\omega}
\end{align}
$$
因此
$$
\begin{align}
\phi_{\v{X}}(\v{\omega}) &= \dfrac{1}{(2\pi)^{n/2} |\det \boldsymbol{\varSigma}|^{1/2}} \exp\left( \J \v{\mu}^{\mathrm{T}} \v{\omega} - \dfrac{1}{2} \v{\omega}^{\mathrm{T}} \boldsymbol{\varSigma} \v{\omega} \right) \\
&\hspace{1em}\cdot \dint_{\mathbb{R}^{n}} \exp\left( -\dfrac{1}{2} \left( \v{x} - \v{\mu} - \J \boldsymbol{\varSigma} \v{\omega} \right)^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \left( \v{x} - \v{\mu} - \J \boldsymbol{\varSigma} \v{\omega} \right) \right) \dif \v{x} \\
&= \exp\left( \J \v{\mu}^{\mathrm{T}} \v{\omega} - \dfrac{1}{2} \v{\omega}^{\mathrm{T}} \boldsymbol{\varSigma} \v{\omega} \right)
\end{align}
$$

综上所述，**多元 Gauss 分布的特征函数**为
$$
\mark{ \phi_{\v{X}}(\v{\omega}) = \exp\left( \J \v{\mu}^{\mathrm{T}} \v{\omega} - \dfrac{1}{2} \v{\omega}^{\mathrm{T}} \boldsymbol{\varSigma} \v{\omega} \right) }
$$
$X_{1}, X_{2}, \cdots, X_{n}$ 相互独立的充分必要条件是协方差矩阵 $\boldsymbol{\varSigma}$ 为对角矩阵，此时
$$
\phi_{\v{X}}(\v{\omega}) = \prod\limits_{i=1}^{n} \exp\left( \J \mu_{i} \omega_{i} - \dfrac{1}{2} \sigma_{i}^{2} \omega_{i}^{2} \right) = \prod\limits_{i=1}^{n} \phi_{X_{i}}(\omega_{i})
$$

#### 多元 Gauss 分布的性质

Gauss 变量的分布**完全由其一、二阶矩 $\v{\mu}$、$\boldsymbol{\varSigma}$ 决定**，因此
+ **高阶矩**均可由 $\v{\mu}$、$\boldsymbol{\varSigma}$ 表示，如零均值 Gauss 变量的四阶矩
$$
\begin{align} 
\mathbb{E} \left[ X_{i} X_{j} X_{k} X_{l} \right] &= \boldsymbol{\varSigma}_{i,j} \boldsymbol{\varSigma}_{k,l} + \boldsymbol{\varSigma}_{i,k} \boldsymbol{\varSigma}_{j,l} + \boldsymbol{\varSigma}_{i,l} \boldsymbol{\varSigma}_{j,k} \\
&= \mathbb{E} \left[ X_{i} X_{j} \right] \mathbb{E} \left[ X_{k} X_{l} \right] + \mathbb{E} \left[ X_{i} X_{k} \right] \mathbb{E} \left[ X_{j} X_{l} \right] + \mathbb{E} \left[ X_{i} X_{l} \right] \mathbb{E} \left[ X_{j} X_{k} \right]
\end{align}
$$
+ **线性变换**对 $\v{\mu}$、$\boldsymbol{\varSigma}$ 的影响是线性的，因而对整个分布的影响也是线性的，如 $\v{Y} = \boldsymbol{A} \v{X} + \v{b}$，则 $\v{Y} \sim \mathscr{N}(\boldsymbol{A} \v{\mu} + \v{b}, \boldsymbol{A} \boldsymbol{\varSigma} \boldsymbol{A}^{\mathrm{T}})$，称为**线性变换不变性**。这是 Gauss 分布的**特征性质**。

### Gauss 过程的定义

> [!definition] Gauss 过程
> 设 $X(t)$ 是定义在概率空间 $(\Omega, \mathcal{F}, P)$ 上的随机过程。如果对于任意正整数 $n$ 和任意时刻 $t_{1}, t_{2}, \cdots, t_{n}$，随机变量组 $\v{X} = \begin{pmatrix}X(t_{1}) & X(t_{2}) & \cdots & X(t_{n})\end{pmatrix}^{\mathrm{T}}$ 都服从 $n$ 元 Gauss 分布 $N\left( \v{\mu},\boldsymbol{\varSigma} \right)$，则称 $X(t)$ 为 **Gauss 过程 (Gaussian process)**。

由定义，Gauss 过程的**有限维分布**都是多元 Gauss 分布，因此多元 Gauss 分布的性质均适用于 Gauss 过程。例如，Gauss 过程 $X(t)$ **通过一般线性系统 $h(t, \tau)$** 得到的**输出 $Y(t)$ 仍然是 Gauss 过程**，且
$$
\begin{align}
&\mathbb{E} \left[ Y(t) \right] = \dint_{-\infty}^{\infty} h(t, \tau) \mathbb{E} \left[ X(\tau) \right] \dif \tau, \\
&\mathrm{Cov} \left[ Y(t_{1}), Y(t_{2}) \right] = \dint_{-\infty}^{\infty} \dint_{-\infty}^{\infty} h(t_{1}, \tau_{1}) h(t_{2}, \tau_{2}) \mathrm{Cov} \left[ X(\tau_{1}), X(\tau_{2}) \right] \dif \tau_{1} \dif \tau_{2}
\end{align}
$$


## Gauss 条件分布

考虑多维随机变量 $\v{X} \in \mathbb{R}^{m}$、$\v{Y} \in \mathbb{R}^{n}$，设其联合服从 $(m+n)$ 元 Gauss 分布 $N\left( \v{\mu}, \boldsymbol{\varSigma} \right)$，其中
$$
\v{\mu} = \begin{pmatrix} \v{\mu}_{X} \\ \v{\mu}_{Y} \end{pmatrix}, \qquad
\boldsymbol{\varSigma} = \begin{pmatrix}
\boldsymbol{\varSigma}_{XX} & \boldsymbol{\varSigma}_{XY} \\
\boldsymbol{\varSigma}_{YX} & \boldsymbol{\varSigma}_{YY} 
\end{pmatrix}
$$
我们考察 **$\v{Y}$ 相对于 $\v{X}$ 的条件分布**，即考察
$$
f_{\v{Y}\mid\v{X}} \left( \v{y} \mid \v{x} \right) = \dfrac{f_{\v{X},\v{Y}}\left( \v{x},\v{y} \right)}{f_{\v{X}}\left( \v{x} \right)}
$$
其中，由 $\v{X}$ 也服从 Gauss 分布，概率密度为
$$
f_{\v{X}}\left( \v{x} \right) = k_{X} \exp\left( -\dfrac{1}{2} \left( \v{x} - \v{\mu} \right)^{\mathrm{T}} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu} \right) \right)
$$
$\v{X}$ 和 $\v{Y}$ 的联合概率分布为
$$
f_{\v{X},\v{Y}}\left( \v{x},\v{y} \right) = k \exp\left( -\dfrac{1}{2} \begin{pmatrix}
\v{x} - \v{\mu}_{X} \\ \v{y} - \v{\mu}_{Y}
\end{pmatrix}^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \begin{pmatrix}
\v{x} - \v{\mu}_{X} \\ \v{y} - \v{\mu}_{Y}
\end{pmatrix} \right)
$$
其中 $k$ 和 $k_{X}$ 是归一化系数。

### 条件概率密度的计算

为计算条件概率密度，首先需计算 $\boldsymbol{\varSigma}^{-1}$。如果能够将右上角块 $\boldsymbol{\varSigma}_{XY}$ 和左下角块 $\boldsymbol{\varSigma}_{YX}$ 消去，则可将 $\boldsymbol{\varSigma}^{-1}$ 写成**分块对角矩阵**的形式，从而简化计算。为此，考虑如下初等变换：
$$
\underbrace{ \begin{pmatrix}
\boldsymbol{I}_{m} &  \\
\boldsymbol{B} & \boldsymbol{I}_{n}
\end{pmatrix} \begin{pmatrix}
\boldsymbol{\varSigma}_{XX} & \boldsymbol{\varSigma}_{XY} \\
\boldsymbol{\varSigma}_{YX} & \boldsymbol{\varSigma}_{YY}
\end{pmatrix} }_{ \begin{pmatrix}
\boldsymbol{\varSigma}_{XX} & \boldsymbol{\varSigma}_{XY} \\
\boldsymbol{B} \boldsymbol{\varSigma}_{XX} + \boldsymbol{\varSigma}_{YX} & \boldsymbol{B} \boldsymbol{\varSigma}_{XY} + \boldsymbol{\varSigma}_{YY}
\end{pmatrix} } \begin{pmatrix}
\boldsymbol{I}_{m} & \boldsymbol{A} \\
& \boldsymbol{I}_{n}
\end{pmatrix} = \begin{pmatrix}
\boldsymbol{C} &  \\
& \boldsymbol{D}
\end{pmatrix}
$$
则右上角块为
$$
\boldsymbol{\varSigma}_{XX} \boldsymbol{A} + \boldsymbol{\varSigma}_{XY} = \boldsymbol{O} \implies \boldsymbol{A} = -\boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY}
$$
左下角块为
$$
\boldsymbol{B} \boldsymbol{\varSigma}_{XX} + \boldsymbol{\varSigma}_{YX} = \boldsymbol{O} \implies \boldsymbol{B} = -\boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1}
$$
因此，有
$$
\begin{pmatrix}
\boldsymbol{I}_{m} &  \\
-\boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} & \boldsymbol{I}_{n}
\end{pmatrix} \boldsymbol{\varSigma} \begin{pmatrix}
\boldsymbol{I}_{m} & -\boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \\
& \boldsymbol{I}_{n}
\end{pmatrix} = \begin{pmatrix}
\boldsymbol{\varSigma}_{XX} &  \\
& \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY}
\end{pmatrix}
$$
得
$$
\boldsymbol{\varSigma} = \begin{pmatrix}
\boldsymbol{I}_{m} &  \\
-\boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} & \boldsymbol{I}_{n}
\end{pmatrix}^{-1} \begin{pmatrix}
\boldsymbol{\varSigma}_{XX} &  \\
& \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY}
\end{pmatrix} \begin{pmatrix}
\boldsymbol{I}_{m} & -\boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \\
& \boldsymbol{I}_{n}
\end{pmatrix}^{-1}
$$
进而
$$
\boldsymbol{\varSigma}^{-1} = \begin{pmatrix}
\boldsymbol{I}_{m} & -\boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \\
& \boldsymbol{I}_{n}
\end{pmatrix} \begin{pmatrix}
\boldsymbol{\varSigma}_{XX}^{-1} &  \\
& \left( \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \right)^{-1}
\end{pmatrix} \begin{pmatrix}
\boldsymbol{I}_{m} &  \\
-\boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} & \boldsymbol{I}_{n}
\end{pmatrix}
$$

这样，**联合概率密度**指数部分中的**二次型**可写成
$$
\begin{align}
&\begin{pmatrix}
    \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}} & \v{y}^{\mathrm{T}} - \v{\mu}_{Y}^{\mathrm{T}} 
\end{pmatrix} \boldsymbol{\varSigma}^{-1} \begin{pmatrix}
    \v{x} - \v{\mu}_{X} \\ \v{y} - \v{\mu}_{Y} 
\end{pmatrix} \\
&= {\color{ violet } \begin{pmatrix}
    \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}} & \v{y}^{\mathrm{T}} - \v{\mu}_{Y}^{\mathrm{T}} 
\end{pmatrix} \begin{pmatrix}
    \boldsymbol{I}_{m} & -\boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \\
    & \boldsymbol{I}_{n}
\end{pmatrix} }  \\
&\hspace{1em}\mathop{}\begin{pmatrix}
    \boldsymbol{\varSigma}_{XX}^{-1} &  \\
    & \left( \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \right)^{-1}
\end{pmatrix} {\color{ orange } \begin{pmatrix}
    \boldsymbol{I}_{m} &  \\
    -\boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} & \boldsymbol{I}_{n}
\end{pmatrix} \begin{pmatrix}
    \v{x} - \v{\mu}_{X} \\ \v{y} - \v{\mu}_{Y}
\end{pmatrix} } \\
&= {\color{ violet } \begin{pmatrix}
    \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}}  &
    \v{y}^{\mathrm{T}} - \v{\mu}_{Y}^{\mathrm{T}} - \left( \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}} \right) \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY}
\end{pmatrix} }  \\
&\hspace{1em}\mathop{}\begin{pmatrix}
    \boldsymbol{\varSigma}_{XX}^{-1} &  \\
    & \left( \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \right)^{-1}
\end{pmatrix} {\color{ orange } \begin{pmatrix}
    \v{x} - \v{\mu}_{X} \\
    \v{y} - \v{\mu}_{Y} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right)
\end{pmatrix} } \\
&= \mathop{} \left( \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}} \right) \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right)  \\
    &\hspace{1em} + \left( \v{y}^{\mathrm{T}} - \v{\mu}_{Y}^{\mathrm{T}} - \left( \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}} \right) \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \right) \left( \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \right)^{-1} \\
    &\hspace{2em} \mathop{}\cdot\mathop{} \left( \v{y} - \v{\mu}_{Y} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right) \right)
\end{align}
$$
于是，**条件概率密度**的指数部分即为
$$
\begin{align}
&\left(  -\dfrac{1}{2} \begin{pmatrix}
\v{x} - \v{\mu}_{X} \\ \v{y} - \v{\mu}_{Y}
\end{pmatrix}^{\mathrm{T}} \boldsymbol{\varSigma}^{-1} \begin{pmatrix}
\v{x} - \v{\mu}_{X} \\ \v{y} - \v{\mu}_{Y}
\end{pmatrix} \right) - \left( -\dfrac{1}{2} \left( \v{x} - \v{\mu}_{X} \right)^{\mathrm{T}} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right) \right) \\
&= -\dfrac{1}{2} \left( \v{y}^{\mathrm{T}} - \v{\mu}_{Y}^{\mathrm{T}} - \left( \v{x}^{\mathrm{T}} - \v{\mu}_{X}^{\mathrm{T}} \right) \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} \right) \\
&\hspace{3em} \mathop{}\cdot\mathop{} \big( \underbrace{ \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY} }_{ \boldsymbol{\varSigma}_{Y\mid X} } \big)^{-1} 
\Big( \v{y} - \Big(\underbrace{ \v{\mu}_{Y} + \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right) }_{ \v{\mu}_{Y\mid X} }\Big) \Big) \\
&= -\dfrac{1}{2} \left( \v{y} - \v{\mu}_{Y\mid X} \right)^{\mathrm{T}} \boldsymbol{\varSigma}_{Y\mid X}^{-1} \left( \v{y} - \v{\mu}_{Y\mid X} \right)
\end{align}
$$

> [!thm.] 多元 Gauss 分布各块间的条件分布
> 设多维随机变量 $\v{X} \in \mathbb{R}^{m}$、$\v{Y} \in \mathbb{R}^{n}$ 的联合**服从 $(m+n)$ 元 Gauss 分布 $\mathscr{N}\left( \v{\mu}, \boldsymbol{\varSigma} \right)$**，其中
> $$
> \v{\mu} = \begin{pmatrix} \v{\mu}_{X} \\ \v{\mu}_{Y} \end{pmatrix}, \qquad
> \boldsymbol{\varSigma} = \begin{pmatrix}
> \boldsymbol{\varSigma}_{XX} & \boldsymbol{\varSigma}_{XY} \\
> \boldsymbol{\varSigma}_{YX} & \boldsymbol{\varSigma}_{YY}
> \end{pmatrix}
> $$
> 则 $\v{Y}$ 相对于 $\v{X}$ 的条件分布**仍然服从 Gauss 分布**，概率密度为
> $$
> f_{\v{Y}\mid\v{X}} \left( \v{y} \mid \v{x} \right) = k_{Y\mid X} \exp\left( -\dfrac{1}{2} \left( \v{y} - \v{\mu}_{Y\mid X} \right)^{\mathrm{T}} \boldsymbol{\varSigma}_{Y\mid X}^{-1} \left( \v{y} - \v{\mu}_{Y\mid X} \right) \right)
> $$
> 即 **$\v{Y} \mid \v{X} \sim \mathscr{N}\left( \v{\mu}_{Y\mid X}, \boldsymbol{\varSigma}_{Y\mid X} \right)$**，其中
> $$
> \v{\mu}_{Y\mid X} = \v{\mu}_{Y} + \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right), \qquad
> \boldsymbol{\varSigma}_{Y\mid X} = \boldsymbol{\varSigma}_{YY} - \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \boldsymbol{\varSigma}_{XY}
> $$

特别地，对二维情形 $\begin{pmatrix}X \\ Y\end{pmatrix} \sim \mathscr{N}\left( \begin{pmatrix}\mu_{X} \\ \mu_{Y}\end{pmatrix}, \begin{pmatrix}\sigma_{X}^2 & \rho \sigma_{X} \sigma_{Y} \\ \rho \sigma_{X} \sigma_{Y} & \sigma_{Y}^2\end{pmatrix} \right)$，则有
$$
\begin{align}
&\mathbb{E} \left[ Y \mid X \right] = \mu_{Y \mid X} = \mu_{Y} + \rho \dfrac{\sigma_{Y}}{\sigma_{X}} (X - \mu_{X}), \\
&\mathrm{Var} \left[ Y \mid X \right] = \sigma_{Y \mid X}^{2} = (1 - \rho^{2}) \sigma_{Y}^{2}
\end{align}
$$

> [!example] [[例题 - Gauss过程#L10-1|L10-1]] 至 [[例题 - Gauss过程#L10-7|L10-7]]：Gauss 条件分布算例
> 设 $X_{1}, X_{2} \stackrel{\text{i.i.d.}}{\sim} \mathscr{N}(0, 1)$，尝试求解以下条件期望。
> + 直接求解：
> 	+ [[例题 - Gauss过程#L10-1|L10-1]]　$\mathbb{E} \left[ X_{1}-X_{2}\mid X_{1}+X_{2} \right]$；
> + 利用独立性简化计算：
> 	+ [[例题 - Gauss过程#L10-2|L10-2]]　$\mathbb{E} \left[ (X_{1}-X_{2})^{2} \mid X_{1}+X_{2} \right]$；
> 	+ [[例题 - Gauss过程#L10-3|L10-3]]　$\mathbb{E} \left[ (X_{1}-X_{2})^{2n} \mid X_{1}+X_{2} \right]$，$n \in \mathbb{N}^{*}$；
> 	+ [[例题 - Gauss过程#L10-4|L10-4]]　$\mathbb{E} \left[ X_1^2 + X_2^2 \mid X_1 + X_2 \right]$；
> + 利用特征函数简化计算：
> 	+ [[例题 - Gauss过程#L10-5|L10-5]]　$\mathbb{E} \left[ \exp\left( 2X_1 - X_2 \right) \mid X_1 + X_2 \right]$；
> 	+ [[例题 - Gauss过程#L10-6|L10-6]]　$\mathbb{E} \left[ \exp(2X_{1}^{2} + X_{2}^{2}) \mid X_{1} - X_{2} \right]$；
> 	+ [[例题 - Gauss过程#L10-7|L10-7]]　$\mathbb{E} \left[ \sin (2X_{1} - X_{2}) \mid X_{1} + X_{2} \right]$。

### 条件分布的几何直观

观察条件均值 $\v{\mu}_{Y\mid X}$ 的表达式
$$
\v{\mu}_{Y\mid X} = \v{\mu}_{Y} + \boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1} \left( \v{x} - \v{\mu}_{X} \right)
$$
其可视为**对无条件均值 $\v{\mu}_{Y}$ 的修正**，且
+ 修正量与 $\v{X}$ 偏离其均值 $\v{\mu}_{X}$ 的程度 $\left( \v{x} - \v{\mu}_{X} \right)$，即 $\v{X}$ 中的**随机成分**成正比；
+ 修正量与上述随机成分的**比例系数**为 $\boldsymbol{\varSigma}_{YX} \boldsymbol{\varSigma}_{XX}^{-1}$，其中 $\boldsymbol{\varSigma}_{XX}^{-1}$ 起到「标准化」的作用，而 $\boldsymbol{\varSigma}_{YX}$ 则反映了 $\v{X}$ 和 $\v{Y}$ 之间的**相关性**。

因此，$\v{Y}$ 相对于 $\v{X}$ 的条件分布可看做**依据 $\v{X}$ 的随机成分在 $\v{Y}$ 上的投影 (projection)** 对 $\v{Y}$ 的分布进行调整后的结果。


## Gauss 过程通过非线性系统

### 典型非线性系统下的 Gauss 过程

非线性系统的解析结构通常较为复杂，难以泛泛讨论其对 Gauss 过程的影响，需要具体问题具体分析。

> [!example] [[例题 - Gauss过程#L11-1|L11-1]]：Gauss 过程通过理想限幅器
> **理想限幅器 (ideal limiter)** 定义为
> $$
> g(x) = \begin{cases}
> -1, & x < 0, \\
> 1, & x \ge 0
> \end{cases}
> $$

> [!example] [[例题 - Gauss过程#L11-2|L11-2]]：Gauss 过程通过全波线性检波器
> **全波线性检波器 (full-wave rectifier)** 定义为
> $$
> g(x) = |x| = \begin{cases}
> -x, & x < 0, \\
> x, & x \ge 0
> \end{cases}
> $$

> [!example] [[例题 - Gauss过程#L11-3|L11-3]]：Gauss 过程通过半波线性检波器
> **半波线性检波器 (half-wave rectifier)** 定义为
> $$
> g(x) = \begin{cases}
> 0, & x < 0, \\
> x, & x \ge 0
> \end{cases} = \mathrm{ReLU} (x)
> $$

> [!example] [[例题 - Gauss过程#L11-4|L11-4]]：Gauss 过程通过平方律检波器
> **平方律检波器 (square-law detector)** 即 $g(x) = x^{2}$。

### Price 定理

**Price 定理**是分析 Gauss 过程通过非线性系统后输出统计特性的有力工具。

> [!theorem] Price 定理
> 设 $(X, Y)$ 服从二元 Gauss 分布 $\mathscr{N}(\mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho)$，$r = \mathrm{Cov}(X, Y) = \rho\sigma_{1}\sigma_{2}$，$g(x,y)$ 是满足一定正则性条件的二元函数，则
> $$
> \dfrac{\partial^{n}}{\partial r^{n}} \mathbb{E} \left[ g(X, Y) \right] = \mathbb{E} \left[ \dfrac{\partial^{2n} g(X, Y)}{\partial x^{n} \partial y^{n}} \right]
> $$
> 特别地，$n=1$ 时即
> $$
> \dfrac{\partial}{\partial \rho} \mathbb{E} \left[ g(X, Y) \right] = \sigma_{1} \sigma_{2} \mathbb{E} \left[ \dfrac{\partial^{2} g(X, Y)}{\partial x \partial y} \right]
> $$

使用 Price 定理的核心是，选取合适的函数 $g(x,y)$，从而**将待求的统计量 $\mathbb{E} \left[ Y(t) Y(s) \right]$ 表示为 $\mathbb{E} \left[ g(X(t), X(s)) \right]$**，以使用 $\mathbb{E} \left[ X(t)X(s) \right]$ 简化计算。通常直接选取 $g(x, y) = g(x)g(y)$，其中 $g(\cdot)$ 为非线性系统的输入输出关系。

Gauss 过程的 **Bussgang 性质 (Bussgang property)** 是 Price 定理的一个重要推论，描述了 Gauss 过程通过非线性系统后输出与输入之间的相关性关系。

> [!theorem] Bussgang 性质
> 设 $(X, Y)$ 服从零均值二元 Gauss 分布，$h(\cdot)$ 为满足一定正则性条件的无记忆非线性函数，则
> $$
> \mathbb{E} \left[ X h(Y) \right] = C \mathbb{E} \left[ XY \right] 
> $$
> 其中 $C$ 是仅依赖于 $Y$ 的常数，具体为 $C = \cfrac{\mathbb{E} \left[ Y h(Y) \right]}{\mathbb{E} \left[ Y^{2} \right]} = \mathbb{E} \left[ \cfrac{\dif}{\dif Y} h(Y) \right]$。

## † 窄带 Gauss 过程

### 二维 Gauss 分布的幅度分布

设 $\begin{pmatrix}X \\ Y\end{pmatrix} \sim \mathscr{N}\left( \v{\mu}, \sigma^{2} \boldsymbol{I} \right)$， 不失一般性地设 $\v{\mu} = \begin{pmatrix}A \cos \phi \\ A \sin \phi\end{pmatrix}$，则联合概率密度为
$$
\begin{align}
f_{X,Y}(x,y) &= \dfrac{1}{2\pi \sigma^{2}} \exp\left( -\dfrac{1}{2\sigma^{2}} \left( (x - A \cos \phi)^{2} + (y - A \sin \phi)^{2} \right) \right) \\
&= \dfrac{1}{2\pi \sigma^{2}} \exp\left( -\dfrac{1}{2\sigma^{2}} \left( x^{2} + y^{2} + A^{2} - 2A (x \cos \phi + y \sin \phi) \right) \right)
\end{align}
$$
转换到**极坐标系 $(R, \varTheta)$**，其中 $R = \sqrt{X^{2} + Y^{2}}$、$\varTheta = \arctan \dfrac{Y}{X}$，则
$$
\begin{align}
f_{R,\varTheta}(r,\theta) &= f_{X,Y}(r \cos \theta, r \sin \theta) \left| \dfrac{ D (x, y) }{ D (r, \theta) }  \right| \\
&= \dfrac{r}{2\pi \sigma^{2}} \exp\left( -\dfrac{1}{2\sigma^{2}} \left( r^{2} + A^{2} - 2A r \cos(\theta - \phi) \right) \right)
\end{align}
$$
对 $\theta$ 积分即得到幅度 $R$ 的概率密度
$$
\begin{align}
f_{R}(r) &= \dint_{0}^{2\pi} f_{R,\varTheta}(r,\theta) \dif \theta  \\
&= \dfrac{r}{2\pi \sigma^{2}} \exp\left( -\dfrac{r^{2} + A^{2}}{2\sigma^{2}} \right) \dint_{0}^{2\pi} \exp\left( \dfrac{A r}{\sigma^{2}} \cos(\theta - \phi) \right) \dif \theta \\
&= \dfrac{r}{\sigma^{2}} \exp\left( -\dfrac{r^{2} + A^{2}}{2\sigma^{2}} \right) I_{0} \left( \dfrac{A r}{\sigma^{2}} \right), \quad r \ge 0
\end{align}
$$
称 $R$ 服从 **Rician 分布**；当 $A=0$ 时，$R$ 的概率密度化为
$$
f_{R}(r) = \dfrac{r}{\sigma^{2}} \exp\left( -\dfrac{r^{2}}{2\sigma^{2}} \right), \quad r \ge 0
$$
称 $R$ 服从 **Rayleigh 分布**，此时 $f_{R, \varTheta}(r, \theta) = \cfrac{f_{R}(r)}{2\pi} = f_{R}(r) f_{\varTheta}(\theta)$，即幅度和相位**统计独立**。

### 零均值窄带 Gauss 过程

设联合平稳的零均值实宽平稳 Gauss 过程 $X(t)$、$Y(t)$ 满足：
+ 相关函数 $R_{X}(\tau) = R_{Y}(\tau)$，$R_{XY}(\tau) = -R_{YX}(\tau)$；
+ $|\omega|\ge \omega_{0}$ 上功率谱密度 $S_{X}(\omega) = S_{Y}(\omega) = 0$。

则可构造 Gauss 过程
$$
Z(t) = X(t) \cos \omega_{\mathrm{c}} t - Y(t) \sin \omega_{\mathrm{c}} t
= V(t) \cos \left( \omega_{\mathrm{c}} t + \varTheta(t) \right)
$$
称为零均值**窄带 Gauss 过程**，其中 $V(t) = \sqrt{X^{2}(t) + Y^{2}(t)}$ 为**包络过程**，$\varTheta(t) = \arctan \cfrac{Y(t)}{X(t)}$ 为**相位过程**，调制频率 $\omega_{\mathrm{c}} \gg \omega_{0}$。

由[[#二维 Gauss 分布的幅度分布]]中的结论立得，**$V(t)$ 服从 Rayleigh 分布**，$\varTheta(t)$ 服从均匀分布，且 $V(t)$ 和 $\varTheta(t)$ 统计独立。

### 非零均值窄带 Gauss 过程

设窄带 Gauss 的非零均值是由**正弦波随机相位过程**叠加引入的，即考虑
$$
\xi(t) = p \sin \left( \omega_{\mathrm{c}} t + \varPhi \right) + Z(t)
$$
其中 $p$ 为常数，$\varPhi$ 为均匀分布在 $[0, 2\pi)$ 上的随机变量，$Z(t)$ 为[[#零均值窄带 Gauss 过程]]。

$\xi(t)$ 可写成
$$
\begin{align}
\xi(t) &= \underbrace{ p \sin \varPhi }_{ \mu_{X} } \cos \omega_{\mathrm{c}} t + \underbrace{ p \cos \varPhi }_{ \mu_{Y} } \sin \omega_{\mathrm{c}} t + X(t) \cos \omega_{\mathrm{c}} t - Y(t) \sin \omega_{\mathrm{c}} t \\
&= \left( X(t) + \mu_{X} \right) \cos \omega_{\mathrm{c}} t - \left( Y(t) - \mu_{Y} \right) \sin \omega_{\mathrm{c}} t \\
&= V_{\xi}(t) \cos \left( \omega_{\mathrm{c}} t + \varTheta_{\xi}(t) \right)
\end{align}
$$
其中
$$
V_{\xi}(t) \cos \varTheta_{\xi}(t) = X(t) + p \sin \varPhi, \qquad
V_{\xi}(t) \sin \varTheta_{\xi}(t) = Y(t) - p \cos \varPhi
$$
则 **$V_{\xi}(t)$ 服从 Rician 分布**，概率密度为
$$
f_{V_{\xi}}(v) = \dfrac{v}{\sigma^{2}} \exp\left( -\dfrac{v^{2} + p^{2}}{2\sigma^{2}} \right) I_{0} \left( \dfrac{p v}{\sigma^{2}} \right), \quad v \ge 0
$$
