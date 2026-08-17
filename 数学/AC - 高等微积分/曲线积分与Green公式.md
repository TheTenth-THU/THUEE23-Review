## 曲线积分与Green公式

第一类曲线积分按弧长累积标量，与曲线方向无关；第二类曲线积分按有向位移累积向量场做功，反向会改变符号。二者都可通过正则参数化化为一元积分。

Green公式把平面闭曲线上的第二类积分转化为区域上的二重积分。应用前应检查边界取正向、区域及其孔洞的处理方式，以及偏导数的连续性条件。

本章使用[[空间曲线与曲面|曲线参数化]]与[[重积分|二重积分]]，并在[[保守场与势函数]]中进一步研究第二类曲线积分的路径无关性。

### 第一类曲线积分

> [!definition] 第一类曲线积分
> 假设 $L\subset \mathbb{R}^3$ 为空间曲线，其起点为 $A$，终点为 $B$，而 $F : L\rightarrow\mathbb{R}$ 为函数，对任意的整数 $n\ge 1$，将 $L$ 分割成 $\overset{\frown}{P_0P_1},\ \overset{\frown}{P_1P_2},\ \cdots,\ \overset{\frown}{P_{n-1}P_n}$ 共 $n$ 段，其中 $P_0=A$，$P_n=B$。在每个小段 $\overset{\frown}{P_{i-1}P_i}$ 上取点 $P_i^\ast$，令
> $$
> d=\max_{1\le i\le n}|\overset{\frown}{P_{i-1}P_i}|
> $$
> 并称之为分割的**步长**，定义（若极限存在）
> $$
> \int_{L}F(x,y,z) \dif s=\lim_{d\rightarrow 0}\sum_{i=1}^nF(P_i^\ast)|\overset{\frown}{P_{i-1}P_i}|
> $$
> 并且称之为 $F$ 在曲线 $L$ 上的**第一类曲线积分**，也记之为 $\displaystyle\int_{\overset{\frown}{AB}} F(x,y,z) \dif s$，其中称 $L$ 为**积分路径**，$F$ 为**被积函数**，$F(x,y,z) \dif s$ 为**被积分式**，$\dif s$ 为**曲线元素**或**弧微分**或**弧微元**。

上述极限存在，意味着 $\exists a\in\mathbb{R}$，使得 $\forall \varepsilon>0$，$\exists \delta>0$ 使得当 $d<\delta$ 时，均有 $\left|\sum\limits_{i=1}^nF(P_i^\ast)|\overset{\frown}{P_{i-1}P_i}|-a\right|<\varepsilon$，此时将 $a$ 记作 $\displaystyle\int_{L}F(x,y,z)\dif s$。若 $L$ 为分段光滑曲线（也即 $L$ 可分成有限多段，且每一段均有连续可导的参数表示），而 $F$ 为连续函数，则 $\displaystyle\int_{L}F(x,y,z)\dif s$ 存在。

> [!theorem] 第一类曲线积分与曲线的方向无关
> 函数 $f$ 沿曲线 $\overset{\frown}{AB}$ 和 $\overset{\frown}{BA}$ 的积分相等：
> $$
> \int_{\overset{\frown}{AB}}F(x,y,z)\dif s=\int_{\overset{\frown}{BA}}F(x,y,z)\dif s
> $$

> [!definition]
> 假设 $L\subset\mathbb{R}^3$ 为分段光滑曲线，在它上面分布有质量使得在点 $X\in L$ 处的密度为 $\rho(X)$。若 $\rho$ 连续，则 $L$ 的总质量 $M=\displaystyle\int_{L}\rho(x,y,z)\dif s$，$L$ 的**质心** $(\bar{x},\bar{y},\bar{z})$ 为
> $$
> \bar{x}=\frac{1}{M}\int_{L}x\rho(x,y,z)\dif s,\quad \bar{y}=\frac{1}{M}\int_{L}y\rho(x,y,z)\dif s,\quad \bar{z}=\frac{1}{M}\int_{L}z\rho(x,y,z)\dif s
> $$

> [!tip] 由参数方程组给定的曲线
> 设分段光滑曲线 $L$ 的参数方程为 $\begin{cases} x=x(t),\\ y=y(t),\\ z=z(t) \end{cases}$（$t\in[\alpha,\beta]$），则其弧微分为
> $$
> \dif s=\sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}\dif t
> $$
> 从而我们有
> $$
> \int_{L}F(x,y,z)\dif s =\int_{\alpha}^{\beta}F(x(t),y(t),z(t)) \sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}\dif t
> $$

> [!example]+
> 求柱面 $x^2+y^2=2ax$（$a>0$）被平面 $z=0$ 以及曲面 $z=\sqrt{x^2+y^2}$ 所截部分的面积。
>
> ---
>
> 设 $L$ 为圆周 $x^2+y^2=2ax$，其参数方程为 $\begin{cases} x=a+a\cos\varphi,\\ y=a\sin \varphi \end{cases}$（$\varphi\in [0,2\pi]$），于是所求面积为
> $$
> S=\int_L\sqrt{x^2+y^2}\dif s =\int_0^{2\pi}\sqrt{(a+a\cos\varphi)^2+(a\sin \varphi)^2}\,a\dif \varphi =8a^2
> $$

> [!tip] 由隐函数方程组给定的曲线
> 若曲线 $L$ 由隐函数方程组 $\begin{cases} \varphi_1(x,y,z)=0,\\ \varphi_2(x,y,z)=0 \end{cases}$ 给出，利用隐函数定理来局部求解上述方程组，由此得到曲线 $L$ 的分段的参数表示，随后再对每段分别利用前面的公式计算。

### 第二类曲线积分

> [!definition] 第二类曲线积分
> 设 $L\subset \mathbb{R}^3$ 为空间曲线，它的起点为 $A$，终点为 $B$，而 $\v{F}=(F_1,F_2,F_3):L\rightarrow\mathbb{R}^3$ 为向量值函数
> $\v{F}(x,y,z)=\left(F_1(x,y,z),F_2(x,y,z),F_3(x,y,z)\right)$，$(x,y,z)\in L\subset\mathbb{R}^3$。
>
> 对任意整数 $n\ge 1$，我们将曲线 $L$ 分割成 $n$ 小段 $\overset{\frown}{P_0P_1},\ \overset{\frown}{P_1P_2},\ \cdots,\ \overset{\frown}{P_{n-1}P_n}$，其中 $P_0=A$，$P_n=B$，并记 $P_i=(x_i,y_i,z_i)\ (0\le i\le n)$，$\v{\ell}=(x,y,z)$。在每个小段 $\overset{\frown}{P_{i-1}P_i}$ 上取点 $X_i=P_i^\ast=(x_i^\ast,y_i^\ast,z_i^\ast)$。令
> $$
> d=\max_{1\le i\le n}|\overline{P_{i-1}P_i}|
> $$
> 并称之为分割的**步长**。定义（若极限存在）
> $$
> \begin{align*}
>     \int_{L(\overset{\frown}{AB})}\v{F}(\v{\ell})\cdot \dif \v{\ell}
>     &=\lim_{d\rightarrow 0}\sum_{i=1}^n\v{F}(X_i)\cdot \overrightarrow{P_{i-1}P_i}\\
>     &=\lim_{d\rightarrow 0}\sum_{i=1}^n\big( F_1(X_i)(x_i-x_{i-1}) + F_2(X_i)(y_i-y_{i-1}) + F_3(X_i)(z_i-z_{i-1}) \big)
> \end{align*}
> $$
> 并且称之为向量值函数 $\v{F}$ 沿曲线 $L$ 由点 $A$ 到点 $B$ 的**第二类曲线积分**。

**第二类曲线积分的计算**

> [!tip] 由参数方程组给定的曲线
> 设分段光滑曲线 $L$ 的参数方程为 $\begin{cases} x=x(t),\\ y=y(t),\\ z=z(t), \end{cases}$ $t\in[\alpha,\beta]$，其中起点 $A$ 和终点 $B$ 所对应的参数分别为 $\alpha,\beta$，则
> $$
> \begin{align*}
>     \int_{L(\overset{\frown}{AB})} \v{F}(\v{\ell})\cdot \dif \v{\ell}
>     &=\int_{L(\overset{\frown}{AB})} F_1(x,y,z)\dif x + \int_{L(\overset{\frown}{AB})} F_2(x,y,z)\dif y + \int_{L(\overset{\frown}{AB})} F_3(x,y,z)\dif z\\
>     &=\int_{\alpha}^{\beta}F_1\left(x(t),y(t),z(t)\right)x'(t)\dif t +\int_{\alpha}^{\beta}F_2\left(x(t),y(t),z(t)\right)y'(t)\dif t\\
>     &\quad +\int_{\alpha}^{\beta}F_3\left(x(t),y(t),z(t)\right)z'(t)\dif t
> \end{align*}
> $$

设路径 $L\subset\mathbb{R}^3$ 是起点为 $A$，终点为 $B$ 的分段光滑曲线，其参数方程为 $\v{\ell}(t)=\left(x(t),y(t),z(t)\right)$，$t\in [a,b]$，而 $\v{F}=(F_1,F_2,F_3): L\rightarrow \mathbb{R}^3$ 为分段连续函数。$\forall P\in L$，设 $L$ 在点 $P$ 处的单位切向量为 $\v{\tau}^{0}(P)=\left(\cos \alpha(P),\cos \beta(P),\cos \gamma(P)\right)$。而 $\forall t\in [a,b]$，我们有
$$
\v{\tau}^{0}(\v{\ell}(t))=\frac{\v{\ell}'(t)}{\|\v{\ell}'(t)\|} =\frac{\left(x'(t),y'(t),z'(t)\right)}{\sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}}
$$
由此立刻可得
$$
\begin{align*}
    \cos\alpha\left(\v{\ell}(t)\right)&=\frac{x'(t)}{\sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}},\\
    \cos\beta\left(\v{\ell}(t)\right)&=\frac{y'(t)}{\sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}},\\
    \cos\gamma\left(\v{\ell}(t)\right)&=\frac{z'(t)}{\sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}}
\end{align*}
$$
注意到 $\dif \ell =\sqrt{(x'(t))^2+(y'(t))^2+(z'(t))^2}\dif t$，即写出
$$
\dif x =x'(t)\dif t=\cos\alpha \dif \ell,\quad \dif y =y'(t)\dif t=\cos\beta\dif \ell,\quad \dif z =z'(t)\dif t=\cos\gamma\dif \ell
$$
进而我们就有
$$
\begin{align}
    \int_{L(\overset{\frown}{AB})}\v{F}(\v{\ell})\cdot \dif \v{\ell}
    &=\int_{L(\overset{\frown}{AB})}F_1(\v{\ell})\dif x+F_2(\v{\ell})\dif y+F_3(\v{\ell})\dif z\\
    &=\int_{a}^{b}\left(F_1(\v{\ell}(t))x'(t)+ F_2(\v{\ell}(t))y'(t) + F_3(\v{\ell}(t))z'(t)\right)\dif t\\
    &=\int_L\left(F_1(x,y,z)\cos\alpha + F_2(x,y,z)\cos\beta + F_3(x,y,z)\cos \gamma\right)\dif \ell\\
    &=\int_L(\v{F}\cdot\v{\tau}^{0})(x,y,z)\dif \ell
\end{align}
$$
其中，最后一行已是第一类曲线积分的形式。

**Green公式**

> [!definition]
> 称 $D \subset\mathbb{R}^2$ 为单连通集，若 $D$ 中的任意闭曲线所围的区域仍包含在 $D$ 中（也即 $D$ 中的任意闭曲线可连续地收缩成为一点）。若 $D$ 不为单连通集，则称之为复连通集。

> [!theorem] 单连通平面向量场的Green公式
> 假设 $\Omega\subset\mathbb{R}^2$ 为单连通的有界闭区域，它的边界 $\partial \Omega$ 为分段光滑闭曲线，该曲线的正方向为逆时针方向，记 $\v{n}_{0}$ 为 $\partial \Omega$ 的单位外法向量。如果 $\v{F}= (F_1,F_2)^\mathrm{T}:\Omega\rightarrow \mathbb{R}^2$ 为连续可导的向量值函数，则
> $$
> \oint_{\partial \Omega}\v{F}\cdot \v{n}_{0}\dif \ell =\iint_{\Omega}\left(\dfrac{\partial F_1}{\partial x}(x,y)+\dfrac{\partial F_2}{\partial y}(x,y)\right)\dif x\dif y
> $$

> [!theorem] 推论
> $\displaystyle|\Omega| =\iint_{\Omega}1\dif x\dif y =\oint_{\partial \Omega^{+}}x\dif y =-\oint_{\partial \Omega^{+}}y\dif x =\frac{1}{2}\oint_{\partial \Omega^{+}}x\dif y-y\dif x$。

$\forall P\in\partial \Omega$，假设 $\v{\tau}_{0}(P)=(\cos \alpha,\sin \alpha)^\mathrm{T}$ 为 $\partial \Omega$ 在点 $P$ 处的单位切向量，则我们有 $\v{n}_{0}(P)=(\sin \alpha,-\cos \alpha)^\mathrm{T}$。又 $\dif x=\cos \alpha \dif \ell$，$\dif y=\sin \alpha\dif \ell$，于是我们有
$$
\v{F}\cdot \v{n}^{0}\dif \ell=(F_1\sin \alpha-F_2\cos \alpha)\dif \ell =F_1\dif y-F_2\dif x
$$
从而 Green 公式又可以表述成
$$
\oint_{\partial \Omega^{+}}F_1\dif y-F_2\dif x =\iint_{\Omega}\left(\frac{\partial F_1}{\partial x}+\frac{\partial F_2}{\partial y}\right)\dif x\dif y
$$
若将 $F_2$ 换成 $-F_1$，$F_1$ 换成 $F_2$，则对 $\v{F} = (F_2,-F_1)^\mathrm{T}$ 有
$$
\oint_{\partial \Omega}\v{F}\cdot \dif \v{\ell} =\oint_{\partial \Omega^{+}}F_1\dif x+F_2\dif y =\iint_{\Omega}\left(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)\dif x\dif y
$$

> [!theorem] 复连通平面向量场的Green公式
> 如果 $\mathbb{R}^2$ 上的闭区域 $\Omega$ 是由有限条分段光滑的曲线围成的，假设 $P,Q: D \to \mathbb{R}$ 是连续的函数并且具有连续的偏导数，那么
> $$
> \int_{\partial D} P \dif x+ Q \dif y = \iint_{D} \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) \dif x\dif y
> $$
> 其中 $\partial D$ 是 $D$ 的边界的正向按照「左侧」原则定义：当一个人沿着 $\partial D$ 正向前行时，区域 $D$ 总是在这个人的左手边。

> [!example]+
> 计算 $\displaystyle\int_{L_1^{+}}(1+y\e^x)\dif x+(x+\e^x)\dif y$，其中 $L_1$ 沿 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ 的上半周由 $A(a,0)$ 到 $B(-a,0)$。
>
> ---
>
> 设 $L^{+}=L_1^{+}\cup\overrightarrow{BA}$，并且将 $L$ 所围成的区域记作 $\Omega$。则由 Green 公式可知
> $$
> \begin{align*}
>     \oint_{L^{+}}(1+y\e^x)\dif x+(x+\e^x)\dif y
>     &=\iint_{\Omega}\left(-\frac{\partial (1+y\e^x)}{\partial y}+\frac{\partial(x+\e^x)}{\partial x}\right)\dif x\dif y\\
>     &=\iint_{\Omega}(-\e^x+1+\e^x)\dif x\dif y
>     =\iint_{\Omega}1\dif x\dif y
>     =\frac{\pi}{2}ab
> \end{align*}
> $$
> 另一方面，我们也有
> $$
> \int_{\overrightarrow{BA}}(1+ye^x)\dif x+(x+e^x)\dif y =\int_{-a}^a1\dif x =2a
> $$
> 由此可得
> $$
> \int_{L_1^{+}}(1+y\e^x)\dif x+(x+\e^x)\dif y =\oint_{L^{+}}(1+y\e^x)\dif x+(x+\e^x)\dif y -\int_{\overrightarrow{BA}}(1+y\e^x)\dif x+(x+\e^x)\dif y =\frac{\pi}{2}ab-2a
> $$

> [!example]+
> 计算 $\displaystyle\int_{L}\frac{(x+y)\dif y+(x-y)\dif x}{x^2+y^2}$，其中 $L$ 是 $x^{\frac{2}{3}}+y^{\frac{2}{3}}=1$，逆时针方向。
>
> ---
>
> 假设曲线 $L: x^{\frac{2}{3}}+y^{\frac{2}{3}}=1$ 所围的区域为 $\Omega$，那么原点为 $\Omega$ 的内点，但被积函数及 $P,Q$ 在原点不连续，不能在 $\Omega$ 上使用 Green 公式。但是，存在 $\delta>0$ 使得 $\Omega$ 包含 $L_\delta: x^2+y^2=\delta^2$，可令 $\Omega_{\delta}$ 是以 $L\cup L_{\delta}$ 为边界的区域，其中 $L$ 沿逆时针方向，而 $L_{\delta}$ 沿顺时针方向。
>
> 则由 Green 公式可知
> $$
> \begin{align*}
>     \oint_{L\cup L_{\delta}}\frac{(x+y)\dif y+(x-y)\dif x}{x^2+y^2}
>     &=\iint_{\Omega_{\delta}}\left(\frac{\partial}{\partial x}\frac{x+y}{x^2+y^2}-\frac{\partial}{\partial y}\frac{x-y}{x^2+y^2}\right)\dif x \dif y\\
>     &=\iint_{\Omega_{\delta}}\left(\frac{(x^2+y^2)-(x+y)(2x)}{(x^2+y^2)^2}-\frac{-(x^2+y^2)-(x-y)(2y)}{(x^2+y^2)^2}\right)\dif x \dif y\\
>     &=\iint_{\Omega_{\delta}}\left(\frac{y^2-x^2-2xy}{(x^2+y^2)^2}-\frac{y^2-x^2-2xy}{(x^2+y^2)^2}\right)\dif x \dif y =0
> \end{align*}
> $$
> 由此可得
> $$
> \begin{align*}
>     \oint_{L}\frac{(x+y)\dif y+(x-y)\dif x}{x^2+y^2}
>     &=-\oint_{L_{\delta}}\frac{(x+y)\dif y+(x-y)\dif x}{x^2+y^2}\\
>     &=-\left(-\int_0^{2\pi}\frac{(\delta\cos \varphi+\delta\sin \varphi)\dif (\delta\sin \varphi)}{\delta^2} +\frac{(\delta\cos \varphi-\delta\sin \varphi)\dif (\delta\cos \varphi)}{\delta^2}\right)\\
>     &=\int_0^{2\pi}\left((\cos \varphi+\sin \varphi)\cos \varphi-(\cos\varphi-\sin \varphi)\sin \varphi\right)\dif \varphi\\
>     &=\int_0^{2\pi}(\cos^2\varphi+\sin^2\varphi)\dif \varphi=2\pi
> \end{align*}
> $$

此例中，实际上不论 $L$ 取何包围原点的闭合曲线，都有 $\displaystyle\int_{L}\frac{(x+y)\dif y+(x-y)\dif x}{x^2+y^2}=2\pi$。
