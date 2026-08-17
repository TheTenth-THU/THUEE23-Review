## 曲面积分与Gauss-Stokes公式

第一类曲面积分按面积元累积标量，与定向无关；第二类曲面积分计算向量场穿过有向曲面的通量，改变法向会改变符号。参数化计算的核心是切向量叉积及其方向。

Gauss公式连接闭曲面通量与体内散度，Stokes公式连接曲面边界环流与曲面上的旋度。应用时必须先协调闭曲面的外法向，或曲面法向与边界曲线方向。

本章使用[[空间曲线与曲面|曲面参数化和定向]]与[[重积分|三重积分]]，把边界—内部关系推广到通量和旋度。

### 第一类曲面积分

> [!definition] 第一类曲面积分
> 假设 $S\subset \mathbb{R}^3$ 为曲面，$f : S\rightarrow\mathbb{R}$ 为函数。将 $S$ 分割成 $n$ 块 $S_1,\cdots,S_n$，在每块 $S_j$ 上取一点 $X_j$，记 $d$ 为所有 $S_j$ 的直径中的最大者，我们定义（若极限存在）
> $$
> \iint_{S}f(x,y,z)\dif \sigma =\lim_{d\rightarrow 0}\sum_{j=1}^nf(X_j)|S_j|
> $$
> 并称之为函数 $f$ 在曲面 $S$ 上的**第一类曲面积分**，$S$ 为**积分曲面**，$f(x,y,z)\dif \sigma$ 为被积分式，$\dif \sigma$ 则为**面积元素**或**面积微分**或**面积微元**。

上述极限存在，意味着 $\exists a\in\mathbb{R}$，使得 $\forall \varepsilon>0$，$\exists \delta>0$ 使得当 $d<\delta$ 时，均有 $\left|\sum\limits_{j=1}^nf(X_j)|S_j|-a\right|<\varepsilon$，此时将 $a$ 记作 $\displaystyle\iint_{S}f(x,y,z)\dif \sigma$。若 $S$ 为分片光滑曲面（即 $S$ 可分成有限多片，每一片均有连续可导的参数表示），而 $f$ 为连续函数，则 $\displaystyle\iint_{S}f(x,y,z)\dif \sigma$ 存在。

设分片光滑曲面 $S$ 的参数方程为 $\begin{cases} x=x(u,v),\\ y=y(u,v),\\ z=z(u,v), \end{cases}$ $(u,v)\in D$，其中 $D\subset\mathbb{R}^2$ 为 Jordan 可测集，则面积微元为 $\dif \sigma=\sqrt{EG-F^2}\dif u\dif v$，其中
$E=\left(\dfrac{\partial x}{\partial u}\right)^2+\left(\dfrac{\partial y}{\partial u}\right)^2+\left(\dfrac{\partial z}{\partial u}\right)^2$，
$G=\left(\dfrac{\partial x}{\partial v}\right)^2+\left(\dfrac{\partial y}{\partial v}\right)^2+\left(\dfrac{\partial z}{\partial v}\right)^2$，
$F=\dfrac{\partial x}{\partial u}\dfrac{\partial x}{\partial v}+\dfrac{\partial y}{\partial u}\dfrac{\partial y}{\partial v}+\dfrac{\partial z}{\partial u}\dfrac{\partial z}{\partial v}$，
于是
$$
\iint_{S} f(x,y,z)\dif \sigma =\iint_{D} f(x(u,v),y(u,v),z(u,v)) \sqrt{EG-F^2}\dif u\dif v
$$

### 第二类曲面积分

设 $S\subset \mathbb{R}^3$ 为连通的光滑曲面，其参数方程为 $\v{r}=(x,y,z)$，$\begin{cases} x=x(u,v),\\ y=y(u,v),\\ z=z(u,v), \end{cases}$ $(u,v)\in D\subset \mathbb{R}^2$，其中 $x(u,v),y(u,v),z(u,v)$ 连续可微，则曲面法向量
$$
\v{n}_{\pm}=\pm \begin{pmatrix} \dfrac{\partial x}{\partial u} \\[7pt] \dfrac{\partial y}{\partial u} \\[7pt] \dfrac{\partial z}{\partial u} \end{pmatrix} \times \begin{pmatrix} \dfrac{\partial x}{\partial v} \\[7pt] \dfrac{\partial y}{\partial v} \\[7pt] \dfrac{\partial z}{\partial v} \end{pmatrix} =\pm \begin{pmatrix} \dfrac{D(y,z)}{D(u,v)} \\[7pt] \dfrac{D(z,x)}{D(u,v)} \\[7pt] \dfrac{D(x,y)}{D(u,v)} \end{pmatrix}
$$
$\forall P\in S$，$\v{n}_{+}(P),\v{n}_{-}(P)$ 在该点处给出曲面 $S$ 的「两个」侧面。

> [!definition]
> 固定 $P_0\in S$ 并在该点处取定单位法方向 $\v{n}(P_0)$（如 $\v{n}_{+}^{0}(P_0)$）为正方向。如果在任意点 $P\in S$ 处可确定单位法方向 $\v{n}^{0}(P)$ 使得 $\v{n}^{0}$ 在连接 $P_0$ 的任意的光滑曲线上连续，则称 $S$ 为**可定向曲面**，否则称为**不可定向曲面**。

> [!theorem]
> 设 $S\subset \mathbb{R}^3$ 为连通的光滑曲面，则 $S$ 为可定向曲面当且仅当按上面定义取得的法向量 $\v{n}$ 永不为零向量。此时曲面 $S$ 只有两个定向，分别为 $\v{n}_{+}$ 和 $\v{n}_{-}$。

> [!definition]
> 假设 $S\subset \mathbb{R}^3$ 为连通的可定向光滑曲面，在 $S$ 上给定一个**定向**并且将相应的单位法向量记作 $\v{n}^{0}_S$，此时我们将 $S$ 称为**定向曲面**。

> [!definition] 第二类曲面积分
> 假设 $\Omega\subset\mathbb{R}^3$ 为开集，$S\subset \Omega$ 为可定向曲面（正侧为 $S^{+}$），而 $\v{F}=(P,Q,R): \Omega\rightarrow\mathbb{R}^3$ 为函数。将 $S$ 分成 $k$ 小块：$S_1,\cdots,S_k$。在 $S_j$ 上取点 $X_j$，并令**有向面积** $\v{S}_j=\v{n}^{0}_S(X_j)|S_j|$。记 $d$ 为所有 $S_j$ 的直径当中的最大者。定义（若极限存在）
> $$
> \iint_{S^{+}}\v{F}(x,y,z)\cdot \dif\v{\sigma} =\lim_{d\rightarrow 0}\sum_{j=1}^k\v{F}(X_j)\cdot \v{S}_j
> $$
> 称为 $\v{F}$ 在定向曲面 $S^{+}$ 上的**第二类曲面积分**。

上述极限存在，意味着 $\exists a\in\mathbb{R}$，使得 $\forall \varepsilon>0$，$\exists \delta>0$ 使得当 $d<\delta$ 时，均有 $\left|\sum\limits_{j=1}^k\v{F}(X_j)\cdot \v{S}_j-a\right|<\varepsilon$，此时将 $a$ 记作 $\displaystyle\iint_{S^{+}}\v{F}(x,y,z)\cdot \dif\v{\sigma}$。若 $\v{F}$ 为分片连续，则 $\displaystyle\iint_{S^{+}}\v{F}(x,y,z)\cdot \mathrm{d}\v{\sigma}$ 存在。

若 $S$ 为封闭曲面，常将外侧取为正侧，并且将第二类曲面积分记作 $\displaystyle\varoiint_{S^{+}}\v{F}(x,y,z)\cdot \mathrm{d}\v{\sigma}$。

**第二类曲面积分的计算**

由定义可知
$$
\iint_{S^{+}}\v{F}(x,y,z)\cdot \dif \v{\sigma} =\lim_{d\rightarrow 0}\sum_{j=1}^k\v{F}(X_j)\cdot \v{S}_j =\lim_{d\rightarrow 0}\sum_{j=1}^k {\left(\v{F}(X_j)\cdot \v{n}^{0}_S(X_j)\right) } |S_j| =\iint_S(\v{F}\cdot \v{n}^{0}_S)(x,y,z) \dif \sigma
$$
也即我们有
$$
\dif \v{\sigma}=\v{n}^{0}_S(x,y,z)\dif \sigma
$$
若记 $\v{n}^{0}_S=(\cos \alpha,\cos \beta,\cos \gamma)$，那么这里的 $\alpha,\beta,\gamma$ 就是该向量和 $x$ 轴，$y$ 轴，$z$ 轴正向的夹角，则
$$
\begin{align*}
    \iint_{S^{+}}\v{F}(x,y,z)\cdot \dif \v{\sigma}
    &=\iint_S \left(\v{F}\cdot \v{n}^{0}_S\right)(x,y,z)\dif \sigma\\
    &=\iint_S\left(P(x,y,z)\cos \alpha+ Q (x,y,z)\cos \beta + R (x,y,z)\cos \gamma\right)\dif \sigma
\end{align*}
$$
现定义
$$
\dif y\wedge \dif z=\cos \alpha\dif \sigma,\quad \dif z\wedge \dif x=\cos \beta\dif \sigma,\quad \dif x\wedge \dif y=\cos \gamma\dif \sigma
$$
则我们有
$$
\iint_{S^{+}}\v{F}(x,y,z)\cdot \dif \v{\sigma}= \iint_{S^{+}}\left(P (x,y,z)\dif y\wedge \dif z + Q (x,y,z)\dif z\wedge \dif x+ R (x,y,z)\dif x\wedge \dif y\right)
$$

设 $S\subset \mathbb{R}^3$ 为光滑曲面，其参数方程为 $\begin{cases} x=x(u,v),\\ y=y(u,v),\\ z=z(u,v), \end{cases}$ $(u,v)\in D\subset \mathbb{R}^2$，其中 $D$ 为 Jordan 可测，$x,y,z$ 为连续可微，且
$$
\v{n}=\begin{pmatrix} \dfrac{\partial x}{\partial u} \\[7pt] \dfrac{\partial y}{\partial u} \\[7pt] \dfrac{\partial z}{\partial u} \end{pmatrix} \times \begin{pmatrix} \dfrac{\partial x}{\partial v} \\[7pt] \dfrac{\partial y}{\partial v} \\[7pt] \dfrac{\partial z}{\partial v} \end{pmatrix} =\begin{pmatrix} \dfrac{D(y,z)}{D(u,v)} \\[7pt] \dfrac{D(z,x)}{D(u,v)} \\[7pt] \dfrac{D(x,y)}{D(u,v)} \end{pmatrix}\neq \v{0}
$$
$\forall (u,v)\in D$，我们记 $\v{r}(u,v)=\begin{cases} x(u,v),\\ y(u,v),\\ z(u,v), \end{cases}$ 则 $\v{n}(u,v)=\v{r}'_u(u,v)\times \v{r}'_v(u,v)$，并且
$$
\dif \sigma=\sqrt{EG-F^2}\dif u\dif v=\|\v{n}(u,v)\|\dif u\dif v
$$
于是 $\dif \v{\sigma}= \v{n}^{0}_S(\v{r}(u,v))\dif \sigma=\pm\v{n}(u,v)\dif u\dif v$，其中 $\pm$ 在 $\v{n}$ 与 $S^{+}$ 同向时取正号，反向时取负号。由此我们立刻可得
$$
\begin{align*}
    \iint_{S^{+}}\v{F}(x,y,z)\cdot \dif \v{\sigma}
    &=\pm\iint_{D}\v{F}(\v{r}(u,v))\cdot \v{n}(u,v)\dif u\dif v\\
    &=\pm\iint_{D}\bigg(P(x(u,v),y(u,v),z(u,v))\frac{D(y,z)}{D(u,v)}\\
    &\qquad\qquad\;\;+Q(x(u,v),y(u,v),z(u,v))\frac{D(z,x)}{D(u,v)}\\
    &\qquad\qquad\;\;+R (x(u,v),y(u,v),z(u,v))\frac{D(x,y)}{D(u,v)}\bigg)\dif u\dif v
\end{align*}
$$
其中 $\pm$ 由任意一点处 $\v{n},S^{+}$ 是否同向来定。

又由混合积 $\v{F}\cdot (\v{r}'_u\times \v{r}'_v)$ 的表达式可知
$$
\begin{align*}
    \iint_{S^{+}}\v{F}(x,y,z)\cdot \dif \v{\sigma}
    &=\pm\iint_{D}\v{F}(x(u,v),y(u,v),z(u,v))\cdot \boldsymbol{ \v{n}(u,v)}\dif u\dif v\\
    &=\pm\iint_{D}\left(\v{F}\cdot\boldsymbol{(\v{r}'_u\times \v{r}'_v)}\right)(u,v)\dif u\dif v\\
    &=\pm\iint_{D}\begin{vmatrix}
        P & Q & R \\
        \dfrac{\partial x}{\partial u} & \dfrac{\partial y}{\partial u} & \dfrac{\partial z}{\partial u} \\[5pt]
        \dfrac{\partial x}{\partial v} & \dfrac{\partial y}{\partial v} & \dfrac{\partial z}{\partial v}
    \end{vmatrix} (u,v)\dif u\dif v
\end{align*}
$$
形式上，我们有
$$
\begin{align*}
    \dif y\wedge \dif z&=\pm\frac{D(y,z)}{D(u,v)}\dif u\dif v=\cos \alpha \dif \sigma,\\
    \dif z\wedge \dif x&=\pm\frac{D(z,x)}{D(u,v)}\dif u\dif v=\cos \beta \dif \sigma,\\
    \dif x\wedge \dif y&=\pm\frac{D(x,y)}{D(u,v)}\dif u\dif v=\cos \gamma \dif \sigma
\end{align*}
$$
这里 $\dif u\dif v>0$。所以 $\pm\dfrac{D(y,z)}{D(u,v)}$ 与 $\cos \alpha$，$\pm\dfrac{D(z,x)}{D(u,v)}$ 与 $\cos \beta$，$\pm\dfrac{D(x,y)}{D(u,v)}$ 与 $\cos \gamma$ 的符号必须分别一致。

**Gauss公式**

> [!theorem] Gauss公式
> 设 $\Omega\subset\mathbb{R}^3$ 为有界闭区域，其边界 $\partial \Omega$ 为分片光滑可定向曲面且以外侧为正向，而 $\v{F}=(P,Q,R)\in\mathscr{C}^{(1)}(\Omega)$，则
> $$
> \oiint_{\partial \Omega^{+}}\v{F}\cdot \dif \v{\sigma} =\iiint_{\Omega}\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)\dif x \dif y \dif z
> $$

> [!note] 用微分形式表述的Gauss公式
> 因 $\displaystyle\oiint_{\partial \Omega^{+}}\v{F}\cdot \dif \v{\sigma}=\oiint_{\partial \Omega^{+}}P\dif y\wedge \dif z+Q\dif z\wedge \dif x+R\dif x\wedge \dif y$，于是 Gauss 公式也可以表述成
> $$
> \oiint_{\partial \Omega^{+}}P\dif y\wedge \dif z+Q\dif z\wedge \dif x +R\dif x\wedge \dif y =\iiint_{\Omega}\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)\dif x \dif y \dif z
> $$
> 考虑引入 *2次微分形式*
> $$
> \omega=P\dif y\wedge \dif z+Q\dif z\wedge \dif x+R\dif x\wedge \dif y
> $$
> 及其 *外微分*
> $$
> \begin{align*}
>     \dif \omega &=\dif P\wedge \dif y\wedge \dif z+\dif Q\wedge \dif z\wedge \dif x+\dif R\wedge \dif x\wedge \dif y\\
>     &=\left(\frac{\partial P}{\partial x}\dif x+\frac{\partial P}{\partial y}\dif y+\frac{\partial P}{\partial z}\dif z\right)\wedge \dif y\wedge \dif z\\
>     &\quad +\left(\frac{\partial Q}{\partial x}\dif x+\frac{\partial Q}{\partial y}\dif y+\frac{\partial Q}{\partial z}\dif z\right)\wedge \dif z\wedge \dif x\\
>     &\quad +\left(\frac{\partial R}{\partial x}\dif x+\frac{\partial R}{\partial y}\dif y+\frac{\partial R}{\partial z}\dif z\right)\wedge \dif x\wedge \dif y\\
>     &=\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)\dif x\wedge \dif y\wedge \dif z
> \end{align*}
> $$
> 则 Gauss 公式也可表述成
> $$
> \oiint_{\partial \Omega^{+}}\omega=\iiint_{\Omega} \dif \omega
> $$

**Stokes公式**

给定空间的一张有向曲面 $S$，带有边界 $\partial S$。若曲面的方向与边界曲线的方向满足：当你沿着边界曲线方向走的时候，你的头指向曲面的方向，而且与你临近的曲面在你的左侧；或者满足右手螺旋法则：右手握着该曲面，大拇指指向曲面的正向，其余四个指头就指向边界曲线的正向；则称曲面及其边界的定向**协调**。

> [!theorem] Stokes公式
> 假设 $\Omega\subset\mathbb{R}^3$ 为非空开集，$S\subset \Omega$ 为分片光滑可定向有界曲面，其边界 $\partial S$ 为分段光滑闭曲线并且 $S^{+}$ 与 $\partial S^{+}$ 的定向协调，$\v{F}=(P,Q,R)\in\mathscr{C}^{(1)}(\Omega)$，则
> $$
> \oint_{\partial S^{+}}\v{F}\cdot \dif \v{\ell} =\oint_{\partial S^{+}}P\dif x+Q\dif y+R\dif z =\iint_{S^{+}}(\v{\nabla}\times \v{F} )\cdot \dif \v{\sigma}
> $$
> 其中 $\v{\nabla}\times \v{F}$ 被称为向量场 $\v{F}$ 的旋度。

> [!note] 散度与旋度
> 利用 Nabla 算子 $\v{\nabla}=\begin{pmatrix} \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \end{pmatrix}^\mathrm{T}$，可以定义
>
> > [!definition]
> > 向量场 $\v{F} = \begin{pmatrix} P & Q & R \end{pmatrix}^\mathrm{T}$ 的*散度*为
> > $$
> > \mathop{\mathrm{div}} \v{F} = \v{\nabla} \cdot \v{F} = \dfrac{\partial P}{\partial x} + \dfrac{\partial Q}{\partial y} + \dfrac{\partial R}{\partial z}
> > $$
>
> > [!definition]
> > 向量场 $\v{F} = \begin{pmatrix} P & Q & R \end{pmatrix}^\mathrm{T}$ 的*旋度*为
> > $$
> > \mathop{\mathrm{rot}} \v{F} = \v{\nabla} \times \v{F} = \begin{vmatrix} \hat{\boldsymbol{x}} & \hat{\boldsymbol{y}} & \hat{\boldsymbol{z}} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ P & Q & R \end{vmatrix} = \begin{pmatrix} \dfrac{\partial R}{\partial y} - \dfrac{\partial Q}{\partial z} \\[7pt] \dfrac{\partial P}{\partial z} - \dfrac{\partial R}{\partial x} \\[7pt] \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} \end{pmatrix}
> > $$

> [!example]+
> 求 $\displaystyle\oint_{L^{+}}\frac{x\dif x+y\dif y+z\dif z}{x^2+y^2+z^2}$，其中曲线 $L$ 为球面 $S: x^2+y^2+z^2=a^2$ 在第一卦限中与坐标平面相交的圆弧 $\overset{\frown}{AB}$，$\overset{\frown}{BC}$，$\overset{\frown}{CA}$ 连接而成的闭曲线。
>
> ---
>
> 记球面 $S$ 的第一卦限部分为 $S'$，定义其正向背离原点，则 $L^+=\partial S'^+$。由 Stokes 公式可知
> $$
> \oint_{L^{+}}\frac{x\dif x+y\dif y+z\dif z}{x^2+y^2+z^2} =\frac{1}{a^2}\oint_{L^{+}}x\dif x+y\dif y+z\dif z =\frac{1}{a^2}\iint_{S'^{+}}\v{\nabla}\times (x,y,z)^\mathrm{T}\cdot \dif \v{\sigma} =0
> $$

> [!example]+
> 计算 $\displaystyle\oint_{L^{+}}\frac{x\dif y-y\dif x}{x^2+y^2}$，
>
> （1）其中 $L$ 是不经过也不围绕 $z$ 轴的闭曲线；
>
> （2）其中 $L$ 是围绕 $z$ 轴一圈的闭曲线，从 $z$ 的正向向下看，曲线 $L$ 的正向为逆时针方向。
>
> ---
>
> （1）由于闭曲线 $L$ 不经过也不围绕 $z$ 轴，因此存在以 $L$ 为边界且与 $z$ 不相交的曲面 $S$，取 $S$ 的正向使之与 $L^{+}$ 满足右手螺旋法则，则
> $$
> \oint_{L^{+}}\frac{x\dif y-y\dif x}{x^2+y^2} =\iint_{S^{+}}\v{\nabla}\times \Big(\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2},0\Big)^\mathrm{T} \cdot \dif \v{\sigma} =0
> $$
>
> （2）以 $L^{+}$（逆时针）为准线、$z$ 轴为母线作一个柱面，记该柱面与 $xy$ 平面的交线为 $L_1^{+}$（逆时针），该柱面的侧面为 $S^+$，其正向向外，则知 $\partial S^+ = L^- + L_1^+$，由 Stokes 公式可知
> $$
> \oint_{L^{-}+ L_1^{+}}\frac{x\dif y-y\dif x}{x^2+y^2} =\iint_{S^{+}}\v{\nabla}\times\Big(\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2},0\Big)^\mathrm{T} \cdot \dif \v{\sigma} =0
> $$
> 即有 $\displaystyle \oint_{L^{+}}\frac{x\dif y-y\dif x}{x^2+y^2}=\oint_{L_1^{+}}\frac{x\dif y-y\dif x}{x^2+y^2}$。设 $L_1$ 在 $xy$ 平面所围区域为 $D$，取 $\delta>0$ 使得 $B((0,0);\delta)\subset D$，令 $L_2=\partial B((0,0);\delta)$，则由 Green 公式可得
> $$
> \oint_{L_1^++L_2^-} \frac{x\dif y-y\dif x}{x^2+y^2} =\iint_{D \setminus B((0,0);\delta)} \left(\dfrac{\partial}{\partial x}\frac{x}{x^2+y^2}+\dfrac{\partial}{\partial y}\frac{y}{x^2+y^2}\right) \dif x \dif y =0
> $$
> 于是
> $$
> \oint_{L^{+}}\frac{x\dif y-y\dif x}{x^2+y^2} =\oint_{L_1^{+}}\frac{x\dif y-y\dif x}{x^2+y^2} =\oint_{L_2^{+}}\frac{x\dif y-y\dif x}{x^2+y^2} =2\pi
> $$
