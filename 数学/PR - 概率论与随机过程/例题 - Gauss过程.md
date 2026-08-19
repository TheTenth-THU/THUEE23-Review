## L10 (10/30)

**Gauss 条件分布算例。** 
设 $X_{1}, X_{2} \stackrel{\text{i.i.d.}}{\sim} \mathscr{N}(0, 1)$，尝试求解以下条件期望。

### L10-1

**$\mathbb{E} \left[ X_{1}-X_{2}\mid X_{1}+X_{2} \right]$。**

注意到
$$
\begin{pmatrix}
X_{1} + X_{2} \\ X_{1} - X_{2}
\end{pmatrix} = \begin{pmatrix}
1 & 1 \\ 1 & -1
\end{pmatrix} \begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix}
$$
由于 $X_{1}, X_{2}$ 独立同分布为 Gauss 分布，故 $\begin{pmatrix} X_{1} + X_{2} \\ X_{1} - X_{2} \end{pmatrix}$ 也服从 Gauss 分布，且
$$
\begin{align}
&\v{\mu} = \begin{pmatrix}
1 & 1 \\ 1 & -1
\end{pmatrix} \begin{pmatrix}
0 \\ 0
\end{pmatrix} = \begin{pmatrix}
0 \\ 0
\end{pmatrix} \\
&\boldsymbol{\varSigma} = \begin{pmatrix}
1 & 1 \\ 1 & -1
\end{pmatrix} \begin{pmatrix}
1 & 0 \\ 0 & 1
\end{pmatrix} \begin{pmatrix}
1 & 1 \\ 1 & -1
\end{pmatrix}^{\mathrm{T}} = \begin{pmatrix}
2 & 0 \\ 0 & 2
\end{pmatrix}
\end{align}
$$
因此，依据多元 Gauss 分布各块间的条件分布，有
$$
\mathbb{E} \left[ X_{1}-X_{2}\mid X_{1}+X_{2} = s \right] = 0 + \dfrac{0}{2} (s - 0) = 0
$$

### L10-2

**$\mathbb{E} \left[ (X_{1}-X_{2})^{2} \mid X_{1}+X_{2} \right]$。**

注意到 $\boldsymbol{\varSigma}$ 为对角矩阵，故 $X_{1} - X_{2}$ 与 $X_{1} + X_{2}$ 独立，因此
$$
\mathbb{E} \left[ (X_{1}-X_{2})^{2} \mid X_{1}+X_{2} \right] = \mathbb{E} \left[ (X_{1}-X_{2})^{2} \right] = \mathrm{Var}(X_{1}-X_{2}) = 2
$$

### L10-3

**$\mathbb{E} \left[ (X_{1}-X_{2})^{2n} \mid X_{1}+X_{2} \right]$，$n \in \mathbb{N}^{*}$。**

类似地，由于 $X_{1} - X_{2}$ 与 $X_{1} + X_{2}$ 独立，$\mathbb{E} \left[ (X_{1}-X_{2})^{2n} \mid X_{1}+X_{2} \right] = \mathbb{E} \left[ (X_{1}-X_{2})^{2n} \right]$，而 $X_{1}-X_{2} \sim \mathscr{N}(0, 2)$，因此所求即为 $Y \sim \mathscr{N}(0, 2)$ 的 $2n$ 阶矩，即
$$
\begin{align}
\mathbb{E} \left[ Y^{2n} \right] &= \dfrac{1}{\sqrt{2\pi} \sigma} \dint_{-\infty}^{\infty} y^{2n} \exp\left( -\dfrac{y^{2}}{2\sigma^{2}} \right) \dif y = \dfrac{-\sigma^{2}}{\sqrt{2\pi} \sigma} \dint_{-\infty}^{\infty} y^{2n-1} \dif \exp\left( -\dfrac{y^{2}}{2\sigma^{2}} \right) \\
&= \dfrac{\sigma^{2}}{\sqrt{2\pi} \sigma} \dint_{-\infty}^{\infty} \left( 2n - 1 \right) y^{2n-2} \exp\left( -\dfrac{y^{2}}{2\sigma^{2}} \right) \dif y \\
&= \sigma^{2} \left( 2n - 1 \right) \mathbb{E} \left[ Y^{2(n-1)} \right] = \cdots = \sigma^{2n} (2n - 1)!! = 2^{n} (2n - 1)!!
\end{align}
$$

### L10-4

**$\mathbb{E} \left[ X_1^2 + X_2^2 \mid X_1 + X_2 \right]$。**

**法一**：由期望的线性性，
$$
\mathbb{E} \left[ X_1^2 + X_2^2 \mid X_1 + X_2 \right] = \mathbb{E} \left[ X_1^2 \mid X_1 + X_2 \right] + \mathbb{E} \left[ X_2^2 \mid X_1 + X_2 \right]
$$
注意到类似地有
$$
\begin{pmatrix}
X_{1} + X_{2} \\ X_{1}
\end{pmatrix} = \begin{pmatrix}
1 & 1 \\ 1 & 0
\end{pmatrix} \begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix}
\sim \mathscr{N} \left( \begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
2 & 1 \\ 1 & 1
\end{pmatrix} \right) 
$$
则
$$
\begin{align}
&\mathbb{E} \left[ X_{1} \mid X_{1}+X_{2} \right] = 0 + \dfrac{1}{2} (X_{1}+X_{2} - 0) = \dfrac{X_{1}+X_{2}}{2} \\
&\mathrm{Var} \left[ X_{1} \mid X_{1}+X_{2} \right] = 1 - \dfrac{1^{2}}{2} = \dfrac{1}{2}
\end{align}
$$
因此
$$
\mathbb{E} \left[ X_1^2 \mid X_1 + X_2 \right] = \mathrm{Var} \left[ X_{1} \mid X_{1}+X_{2} \right] + \left( \mathbb{E} \left[ X_{1} \mid X_{1}+X_{2} \right] \right)^{2} = \dfrac{1}{2} + \dfrac{(X_{1}+X_{2})^{2}}{4}
$$

**法二**：注意到所求式可拆成分别关于 $X_{1}+X_{2}$ 和 $X_{1}-X_{2}$ 两独立变量的函数，因而可写成
$$
\begin{align}
\mathbb{E} \left[ X_{1}^{2} + X_{2}^{2} \mid X_{1} + X_{2} \right] &= \mathbb{E} \left[ \dfrac{1}{2} (X_{1} + X_{2})^{2} + \dfrac{1}{2} (X_{1} - X_{2})^{2} \,\Bigg|\, X_{1} + X_{2} \right] \\
&= \dfrac{1}{2} (X_{1} + X_{2})^{2} + \dfrac{1}{2} \mathbb{E} \left[ (X_{1} - X_{2})^{2} \right] \\
&= \dfrac{1}{2} (X_{1} + X_{2})^{2} + \dfrac{1}{2} \cdot 2 \\
&= \dfrac{1}{2} (X_{1} + X_{2})^{2} + 1
\end{align}
$$

### L10-5

**$\mathbb{E} \left[ \exp\left( 2X_1 - X_2 \right) \mid X_1 + X_2 \right]$。**

类似地，注意到
$$
\begin{pmatrix}
X_{1} + X_{2} \\ 2X_{1} - X_{2}
\end{pmatrix} = \begin{pmatrix}
1 & 1 \\ 2 & -1
\end{pmatrix} \begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix} \sim \mathscr{N} \left( \begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
2 & 1 \\ 1 & 5
\end{pmatrix} \right) 
$$
即
$$
\begin{align}
&\mathbb{E} \left[ 2X_{1} - X_{2} \mid X_{1}+X_{2} \right] = 0 + \dfrac{1}{2} (X_{1}+X_{2} - 0) = \dfrac{X_{1}+X_{2}}{2} \\
&\mathrm{Var} \left[ 2X_{1} - X_{2} \mid X_{1}+X_{2} \right] = 5 - \dfrac{1^{2}}{2} = \dfrac{9}{2}
\end{align}
$$
$2X_{1} - X_{2} \mid X_{1}+X_{2}$ 服从 Gauss 分布 $\mathscr{N} \left( \dfrac{X_{1}+X_{2}}{2}, \dfrac{9}{2} \right)$，不妨记之为 $Y$。

引入**特征函数**，有
$$
\begin{align}
\mathbb{E} \left[ \exp(Y) \right] &= \mathbb{E} \left[ \exp(\J\omega Y) \right] \Big|_{\omega = -\J} = \phi_{Y}(-\J) \\
&= \exp\left( \J \omega \mu_{Y} - \dfrac{1}{2} \sigma_{Y}^{2} \omega^{2} \right) \Big|_{\omega = -\J} = \exp\left( \mu_{Y} + \dfrac{1}{2} \sigma_{Y}^{2} \right) \\
&= \exp\left( \dfrac{X_{1}+X_{2}}{2} + \dfrac{9}{4} \right)
\end{align}
$$

### L10-6

**$\mathbb{E} \left[ \exp(2X_{1}^{2} + X_{2}^{2}) \mid X_{1} - X_{2} \right]$。**

$2X_{1}^{2} + X_{2}^{2}$ 与 $X_{1} - X_{2}$ 并非线性相关，无法直接应用多元 Gauss 分布各块间的条件分布定理。考察
$$
\begin{pmatrix}
X_{1} \\ X_{2} \\ X_{1} - X_{2}
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\ 0 & 1 \\ 1 & -1
\end{pmatrix} \begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix} \sim \mathscr{N} \left( \begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}, \begin{pmatrix}
1 & 0 & 1 \\ 0 & 1 & -1 \\ 1 & -1 & 2
\end{pmatrix} \right)
$$
这样有
$$
\begin{align}
&\mathbb{E} \left[ \begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix} \,\Bigg|\, X_{1} - X_{2} \right] = \begin{pmatrix}
0 \\ 0
\end{pmatrix} + \begin{pmatrix}
1 \\ -1
\end{pmatrix} \dfrac{1}{2} (X_{1} - X_{2} - 0) = \dfrac{X_{1} - X_{2}}{2} \begin{pmatrix}
1 \\ -1
\end{pmatrix} \\
&\mathrm{Var} \left[ \begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix} \,\Bigg|\, X_{1} - X_{2} \right] = \begin{pmatrix}
1 & 0 \\ 0 & 1
\end{pmatrix} - \begin{pmatrix}
1 \\ -1
\end{pmatrix} \dfrac{1}{2} \begin{pmatrix}
1 & -1
\end{pmatrix} = \dfrac{1}{2} \begin{pmatrix}
1 & 1 \\ 1 & 1
\end{pmatrix}
\end{align}
$$
因此，$\begin{pmatrix} X_{1} \\ X_{2} \end{pmatrix} \mid X_{1} - X_{2}$ 服从二维 Gauss 分布
$$
\begin{align} 
&f_{\begin{pmatrix} X_{1} \\ X_{2} \end{pmatrix} \mid X_{1} - X_{2}} \left( \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \,\Bigg|\, s \right)  \\
&= k \exp\left( -\dfrac{1}{2} \left( \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} - \dfrac{s}{2} \begin{pmatrix} 1 \\ -1 \end{pmatrix} \right)^{\mathrm{T}} \cdot 2 \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \cdot \left( \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} - \dfrac{s}{2} \begin{pmatrix} 1 \\ -1 \end{pmatrix} \right) \right) 
\end{align}
$$
此即关于 $X_{1},X_{2}$ 的联合 Gauss 分布 $f_{X_{1}, X_{2} \mid X_{1} - X_{2}}$，因而
$$
\begin{align} 
&\mathbb{E} \left[ \exp(2X_{1}^{2} + X_{2}^{2}) \mid X_{1} - X_{2} = s \right]  \\
&= \dint_{-\infty}^{\infty} \dint_{-\infty}^{\infty} \exp(2x_{1}^{2} + x_{2}^{2}) \cdot f_{X_{1}, X_{2} \mid X_{1} - X_{2}} \left( x_{1}, x_{2} \mid s \right) \dif x_{1} \dif x_{2}  
\end{align}
$$

### L10-7

**$\mathbb{E} \left[ \sin (2X_{1} - X_{2}) \mid X_{1} + X_{2} \right]$。**

同上可设 $Y = 2X_{1} - X_{2} \mid X_{1}+X_{2} \sim \mathscr{N} \left( \dfrac{X_{1}+X_{2}}{2}, \dfrac{9}{2} \right)$。同样引入**特征函数**，有
$$
\begin{align}
\mathbb{E} \left[ \sin(Y) \right] &= \dfrac{1}{2\J} \left( \mathbb{E} \left[ \exp(\J Y) \right] - \mathbb{E} \left[ \exp(-\J Y) \right] \right) \\
&= \dfrac{1}{2\J} \left( \phi_{Y}(1) - \phi_{Y}(-1) \right) \\
\end{align}
$$

> [!note] 特征函数在 Gauss 条件分布问题中的更多用法
> 设 $\begin{pmatrix}X_{1} \\ X_{2}\end{pmatrix} \sim \mathscr{N}\left( \begin{pmatrix}0 \\ 0\end{pmatrix}, \begin{pmatrix}2 & 1 \\ 1 & 2\end{pmatrix} \right)$，考虑 **$\mathbb{E} \left[ X_{1} \sin X_{2} \right]$**，有
> $$
> \begin{align}
> \mathbb{E} \left[ X_{1} \sin X_{2} \right] &= \mathbb{E} \left[ X_{1} \cdot \dfrac{1}{2\J} \left( \exp(\J X_{2}) - \exp(-\J X_{2}) \right) \right] \\
> &= \dfrac{1}{2\J} \left( \mathbb{E} \left[ X_{1} \exp(\J X_{2}) \right] - \mathbb{E} \left[ X_{1} \exp(-\J X_{2}) \right] \right) \\
> &= \mathbb{E} \left[ \dfrac{1}{\J} \dfrac{ \partial }{ \partial \omega_{1} } \exp(\J(\omega_{1}X_{1} + \omega_{2}X_{2})) \right] \Bigg|_{\omega_{1}=0, \omega_{2}=1}
> \end{align}
> $$
> 考虑 **$\mathbb{E} \left[ \sin (X_{1})X_{2}\sin(X_{3}) \right]$**，有
> $$
> \begin{align}
> &\mathbb{E} \left[ \sin (X_{1})X_{2}\sin(X_{3}) \right]  \\
> &= \mathbb{E} \left[ \dfrac{1}{(2\J)^{2}} \left( \exp(\J X_{1}) - \exp(-\J X_{1}) \right) X_{2} \left( \exp(\J X_{3}) - \exp(-\J X_{3}) \right) \right] \\
> &= \dfrac{1}{\J} \dfrac{ \partial }{ \partial \omega_{2} } \mathbb{E} \left[ \dfrac{1}{(2\J)^{2}} \exp(\J(\omega_{1}X_{1} + \omega_{2}X_{2} + \omega_{3}X_{3})) \right] \Bigg|_{\omega_{1}=1, \omega_{2}=0, \omega_{3}=1} \\
> \end{align}
> $$

## L11 (11/04)

### L11-1

**Gauss 过程通过理想限幅器。**

设输入**宽平稳** Gauss 过程 $X(t) \sim \mathscr{N}\left( \v{0}, \boldsymbol{\varSigma}(\sigma^{2}, \rho) \right)$，其中 $\sigma^{2} = R_{\v{X}}(0)$、$\rho(\tau) = \dfrac{R_{\v{X}}(\tau)}{R_{\v{X}}(0)}$，**理想限幅器 (ideal limiter)** 定义为
$$
g(x) = \begin{cases}
-1, & x < 0, \\
1, & x \ge 0
\end{cases}
$$

输出过程 $Y(t) = g(X(t))$ 显然服从**两点分布**，
$$
P \left\{ Y(t) = 1 \right\} = P \left\{ X(t) \ge 0 \right\} = \dfrac{1}{2}, \quad P \left\{ Y(t) = -1 \right\} = P \left\{ X(t) < 0 \right\} = \dfrac{1}{2}
$$
立得 $\mathbb{E} \left[ Y(t) \right] = 0$。

进一步考虑 $Y(t)$ 的**相关函数**
$$
R_{Y}(t, s) = \mathbb{E} \left[ Y(t) Y(s) \right] = P\left\{ X(t) X(s) \ge 0 \right\} - P\left\{ X(t) X(s) \le 0 \right\}
$$
当 $\rho \equiv 0$ 时，$X(t)$ 与 $X(s)$ 独立，立得 $R_{Y}(t, s) = 0$。当 $\rho \neq 0$ 时，须计算
$$
\begin{align} 
I &= P\left\{ X(t) \ge 0, X(s) \ge 0 \right\} = \dint_{0}^{\infty} \dint_{0}^{\infty} f_{X(t), X(s)}(x_{1}, x_{2}) \dif x_{1} \dif x_{2} \\
&=  \dint_{0}^{\infty} \dint_{0}^{\infty} \dfrac{1}{2\pi \sigma^{2} \sqrt{1-\rho^{2}}} \exp\left( -\dfrac{1}{2\sigma^{2}(1-\rho^{2})} \left( x_{1}^{2} - 2\rho x_{1} x_{2} + x_{2}^{2} \right) \right) \dif x_{1} \dif x_{2}
\end{align}
$$
做**变量替换 $u = \cfrac{x_{1}}{\sigma \sqrt{2(1-\rho^{2})}}$、$v = \cfrac{x_{2}}{\sigma \sqrt{2(1-\rho^{2})}}$**，则
$$
I = \dfrac{\sqrt{ 1-\rho^{2} }}{\pi} \dint_{0}^{\infty} \dint_{0}^{\infty} \exp\left( -( u^{2} - 2\rho uv + v^{2} ) \right) \dif u \dif v
$$
进一步做**变量替换 $u = \cfrac{r}{\sin \alpha} \cos\left( \cfrac{\alpha}{2} + \theta \right)$、$v = \dfrac{r}{\sin \alpha} \cos\left( \cfrac{\alpha}{2} - \theta \right)$，其中 $\cos \alpha = \rho$**，则有 $u^{2} + v^{2} - 2\rho uv = r^{2}$、$\left|\cfrac{ D (u,v) }{ D (r, \theta) }\right| = \dfrac{r}{\sin \alpha}$，得
$$
\begin{align}
I &= \dfrac{\sqrt{ 1-\rho^{2} }}{\pi} \dfrac{1}{\sin \alpha} \dint_{0}^{\infty} \dint_{-\tfrac{\pi-\alpha}{2}}^{\tfrac{\pi-\alpha}{2}} r \exp(-r^{2}) \dif r \dif \theta \\
&= \dfrac{\sqrt{ 1-\rho^{2} }}{\pi} \dfrac{\pi - \alpha}{\sin \alpha} \cdot \dfrac{1}{2} = \dfrac{1}{4} + \dfrac{1}{2\pi} \arcsin \rho
\end{align}
$$
因此，**$Y(t)$ 的相关函数**为
$$
R_{Y}(t, s) = 2I - (1 - 2I) = \dfrac{2}{\pi} \arcsin \rho(t - s)
$$
其也为**宽平稳过程**。

### L11-2

**Gauss 过程通过全波线性检波器。**

设输入**宽平稳** Gauss 过程 $X(t) \sim \mathscr{N}\left( \v{0}, \boldsymbol{\varSigma}(\sigma^{2}, \rho) \right)$，其中 $\sigma^{2} = R_{\v{X}}(0)$、$\rho(\tau) = \dfrac{R_{\v{X}}(\tau)}{R_{\v{X}}(0)}$，**全波线性检波器 (full-wave rectifier)** 定义为
$$
g(x) = |x| = \begin{cases}
-x, & x < 0, \\
x, & x \ge 0
\end{cases}
$$

输出过程 $Y(t) = g(X(t))$ 的分布为
$$
\begin{align}
&\begin{aligned} 
F_{Y}(y) &= P \left\{ Y(t) \le y \right\} = P \left\{ |X(t)| \le y \right\} = P \left\{ -y \le X(t) \le y \right\} \\
&= \dint_{-y}^{y} \dfrac{1}{\sqrt{2\pi} \sigma} \exp\left( -\dfrac{x^{2}}{2\sigma^{2}} \right) \dif x = 2\varPhi\left( \dfrac{y}{\sigma} \right) - 1, \quad y \ge 0
\end{aligned} \\
&f_{Y}(y) = \dfrac{\dif F_{Y}(y)}{\dif y} = \begin{cases}
\cfrac{2}{\sqrt{2\pi} \sigma} \exp\left( -\cfrac{y^{2}}{2\sigma^{2}} \right), & y \ge 0, \\
0, & y < 0
\end{cases}
\end{align}
$$
其**均值**为
$$
\mathbb{E} \left[ Y(t) \right] = \dint_{0}^{\infty} y f_{Y}(y) \dif y = \dfrac{2\sigma}{\sqrt{2\pi}} = \sqrt{\dfrac{2}{\pi} \sigma^{2}}
$$
相关函数为
$$
\begin{align} 
R_{Y}(t, s) &= \mathbb{E} \left[ Y(t) Y(s) \right] = \mathbb{E} \left[ |X(t)| |X(s)| \right] \\
&= \left( \dint_{0}^{\infty} \dint_{0}^{\infty} + \dint_{-\infty}^{0} \dint_{-\infty}^{0} \right) x_{1} x_{2} f_{X(t), X(s)}(x_{1}, x_{2}) \dif x_{1} \dif x_{2} \\
&\hspace{1em} - \left( \dint_{0}^{\infty} \dint_{-\infty}^{0} + \dint_{-\infty}^{0} \dint_{0}^{\infty} \right) x_{1} x_{2} f_{X(t), X(s)}(x_{1}, x_{2}) \dif x_{1} \dif x_{2}
\end{align}
$$
只需专注于计算
$$
\begin{align} 
I &= \dint_{0}^{\infty} \dint_{0}^{\infty} x_{1} x_{2} f_{X(t), X(s)}(x_{1}, x_{2}) \dif x_{1} \dif x_{2} \\
&= \dfrac{1}{2\pi \sigma^{2} \sqrt{1-\rho^{2}}} \dint_{0}^{\infty} \dint_{0}^{\infty} x_{1} x_{2} \exp\left( -\dfrac{x_{1}^{2} - 2\rho x_{1} x_{2} + x_{2}^{2}}{2\sigma^{2}(1-\rho^{2})} \right) \dif x_{1} \dif x_{2} \\
&\stackrel{\text{换元 }u,v}{=\!=\!=\!=\!=} \dfrac{2\sigma^{2} (1-\rho^{2})^{3/2}}{\pi} \dint_{0}^{\infty} \dint_{0}^{\infty} u v \exp\left( -(u^{2} - 2\rho uv + v^{2}) \right) \dif u \dif v \\
&= \dfrac{2\sigma^{2} (1-\rho^{2})^{3/2}}{\pi} \cdot \dfrac{1}{2} \dfrac{\dif}{\dif \rho} \dint_{0}^{\infty} \dint_{0}^{\infty} \exp\left( -( u^{2} - 2\rho uv + v^{2} ) \right) \dif u \dif v \\
&\stackrel{\text{\href{#L11-1}{L11-1}}}{=\!=\!=\!=} \dfrac{\sigma^{2} (1-\rho^{2})^{3/2}}{\pi} \cdot \dfrac{\dif}{\dif \rho} \dfrac{\pi - \arccos \rho}{2 \sqrt{ 1-\rho^{2} }} 
= \dfrac{\sigma^{2} }{2\pi} \left( \sqrt{ 1-\rho^{2} } + \rho \left( \dfrac{\pi}{2} + \arcsin \rho \right) \right)
\end{align}
$$
注意到 $X(t)$ 的相关函数 $R_{X}(t, s) = \sigma^{2} \rho(t-s)$ 是 $R_{Y}(t, s)$ 两部分积分的和，因此，**$Y(t)$ 的相关函数**为
$$
R_{Y}(t, s) = I - (\sigma^{2} \rho - I) = \dfrac{2\sigma^{2}}{\pi} \left( \sqrt{ 1-\rho^{2} } + \rho \arcsin \rho \right)
$$
同样也为**宽平稳过程**。

### L11-3

**Gauss 过程通过半波线性检波器。**

**半波线性检波器 (half-wave rectifier)** 定义为
$$
g(x) = \begin{cases}
0, & x < 0, \\
x, & x \ge 0
\end{cases} = \mathrm{ReLU} (x)
$$
在相同的输入假定下，可利用 [[#L11-2]] 的结果直接得到输出过程 $Y(t) = g(X(t))$ 的**均值**
$$
\mathbb{E} \left[ Y(t) \right] = \dint_{0}^{\infty} y f_{Y}(y) \dif y = \dfrac{\sigma}{\sqrt{2\pi}}
$$
及**相关函数**
$$
R_{Y}(t, s) = I_{\text{\href{#L11-2}{L11-2}}} = \dfrac{\sigma^{2} }{2\pi} \left( \sqrt{ 1-\rho^{2} } + \rho \left( \dfrac{\pi}{2} + \arcsin \rho \right) \right)
$$
同样，输出也为**宽平稳过程**。

### L11-4

**Gauss 过程通过平方律检波器。**

**平方律检波器 (square-law detector)** 即 $g(x) = x^{2}$，设输入**宽平稳** Gauss 过程 $X(t) \sim \mathscr{N}\left( \v{0}, \boldsymbol{\varSigma}(\sigma^{2}, \rho) \right)$，其中 $\sigma^{2} = R_{\v{X}}(0)$、$\rho(\tau) = \dfrac{R_{\v{X}}(\tau)}{R_{\v{X}}(0)}$，立得输出过程 $Y(t) = g(X(t))$ 的**均值**为 $\mathbb{E} \left[ Y(t) \right] = \mathbb{E} \left[ X^{2}(t) \right]  = \sigma^{2}$，**相关函数**为
$$
\begin{align} 
R_{Y}(t, s) &= \mathbb{E} \left[ Y(t) Y(s) \right] = \mathbb{E} \left[ X^{2}(t) X^{2}(s) \right] \\
&= \mathbb{E} \left[ X^{2}(t) \right] \mathbb{E} \left[ X^{2}(s) \right] + 2 \left( \mathbb{E} \left[ X(t) X(s) \right] \right)^{2}  \\
&= R_{X}^{2}(0) + 2 R_{X}^{2}(t - s) = \sigma^{4} (1 + 2 \rho^{2}(t - s))
\end{align}
$$
同样也为**宽平稳过程**。

更一般地，$Y(t)$ 的分布为
$$
\begin{align} 
&\begin{aligned}
F_{Y}(y) &= P \left\{ Y(t) \le y \right\} = P \left\{ X^{2}(t) \le y \right\}  \\
&= P \left\{ -\sqrt{y} \le X(t) \le \sqrt{y} \right\}
= 2\varPhi\left( \dfrac{\sqrt{y}}{\sigma} \right) - 1, \quad y \ge 0
\end{aligned} \\
&f_{Y}(y) = \dfrac{\dif F_{Y}(y)}{\dif y} = \begin{cases}
\cfrac{1}{\sqrt{2\pi} \sigma \sqrt{y}} \exp\left( -\dfrac{y}{2\sigma^{2}} \right), & y \ge 0, \\
0, & y < 0
\end{cases}
\end{align}
$$

