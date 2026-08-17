## Taylor公式与近似

Taylor公式用函数在一点的有限阶导数构造局部多项式，并用余项记录尚未解释的误差。Peano余项适合局部渐近比较，Lagrange余项适合给出区间上的显式误差界。

展开函数前应先确定展开点、所需阶数和余项形式。Taylor多项式相同并不自动保证函数等于其Taylor级数；后者还要求余项随阶数趋于零。

本章连接[[中值定理与函数性态|中值定理]]与[[幂级数]]：有限阶Taylor公式总带余项，而函数等于其Taylor级数还需无穷阶余项趋于零。

### 带Peano余项的Taylor公式

> [!theorem] 带Peano余项的Taylor公式
> 假设 $n\ge 1$ 为整数，$x_0\in\mathbb{R}$，$B(x_0)$ 为 $x_0$ 的邻域，函数 $f:B(x_0)\rightarrow \mathbb{R}$ 为 $n-1$ 阶可导且在点 $x_0$ 为 $n$ 阶可导。则当 $x\rightarrow x_0$ 时，
> $$
> f(x)=\sum\limits_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+o\big((x-x_0)^n\big)
> $$
> 其中 $\sum\limits_{k=0}^{n}\dfrac{f^{(k)}(x_0)}{k!}(x-x_0)^k$ 称为 $f$ 在点 $x_0$ 处的 $n$ 阶**Taylor多项式**，$o\big((x-x_0)^n\big)$ 称为**Peano余项**。

**证明：**

令 $r_n(x)=f(x)-\sum\limits_{k=0}^{n}\dfrac{f^{(k)}(x_0)}{k!}(x-x_0)^k$，由于 $r_n$ 为 $n-1$ 阶可导，$r^{(n)}_n(x_0)$ 存在，且

$$
r^{(n-1)}_n(x)=f^{(n-1)}(x)-f^{(n-1)}(x_0)-f^{(n)}(x_0)(x-x_0)
$$

故 $r^{(n-1)}_n(x_0)=0=r^{(n)}_n(x_0)$，由L'Hospital法则，

$$
\lim_{x\rightarrow x_0}\frac{r_n(x)}{(x-x_0)^n}
=\lim_{x\rightarrow x_0}\frac{r_n^{(n-1)}(x)}{n!(x-x_0)}
=\lim_{x\rightarrow x_0}\frac{r_n^{(n-1)}(x)-r_n^{(n-1)}(x_0)}{n!(x-x_0)}=\frac{r_n^{(n)}(x_0)}{n!}=0
$$

因此所证结论成立。

当 $x_0=0$，即 $x\rightarrow 0$ 时，该公式也称为**Maclaurin公式**。基本的Maclaurin公式有

> [!theorem] 基本Maclaurin展开式
> $$
> \begin{aligned}
> &e^x=\sum\limits_{k=0}^n\frac{x^k}{k!}+o(x^n)
> \qquad \ln(1+x)=\sum\limits_{k=1}^n(-1)^{k-1}\frac{x^{k}}{k}+o(x^{n})\\
> &\sin x=\sum\limits_{k=0}^n\frac{(-1)^k x^{2k+1}}{(2k+1)!}+ o(x^{2n+1})\qquad
> \cos x=\sum\limits_{k=0}^n\frac{(-1)^k x^{2k}}{(2k)!}+o(x^{2n})\\
> &(1+x)^{\alpha}=\sum\limits_{k=0}^n\frac{\alpha(\alpha-1)\cdots (\alpha-k+1)}{k!}x^k+o(x^{n})\\
> &\frac{1}{1-x}=\sum\limits_{k=0}^nx^k+o(x^n)
> \end{aligned}
> $$

> [!example]+
> $$
> \begin{aligned}
> &\lim\limits_{x\rightarrow 0^{+}}\frac{e^{\sin^2 x}-\cos(2\sqrt{x})-2x}{x^2}\\
> &=\lim\limits_{x\rightarrow 0^{+}}\frac{1}{x^2}\left[\left(1+\sin^2x+o(\sin^2x)\right)-\left(1-\frac{1}{2!}(2\sqrt{x})^2+\frac{1}{4!}(2\sqrt{x})^4+o(x^2)\right)-2x\right]\\
> &=\lim\limits_{x\rightarrow 0^{+}}\frac{1}{x^2}\left(\sin^2x-\frac{2}{3}x^2\right)
> =1-\frac{2}{3}=\frac{1}{3}
> \end{aligned}
> $$

> [!note] 基本函数在非零处的Taylor展开
> 要求基本函数在非零 $x_0$ 处的Taylor展开，可换元 $t=x-x_0$，对 $t$ 做Maclaurin展开，然后将 $x$ 代回。

### 带Lagrange余项的Taylor公式

> [!theorem] 带Lagrange余项的Taylor公式
> 假设 $n\in\mathbb{N}^{*}$，$f\in\mathscr{C}^{(n)}[a, b]$ 在 $(a, b)$ 上 $n+1$ 阶可导，那么 $\forall x_0, x\in [a, b]\ (x_0\neq x)$，存在 $\xi_{x_0}(x)$ 严格介于 $x_0, x$ 之间使得
> $$
> f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+\frac{f^{(n+1)}(\xi_{x_0}(x))}{(n+1)!}(x-x_0)^{n+1}
> $$
> 其中 $\dfrac{f^{(n+1)}(\xi_{x_0}(x))}{(n+1)!}(x-x_0)^{n+1}$ 称为**Lagrange余项**；$\xi_{x_0}(x)$ 与 $x$ 和 $x_0$ 都有关，也可写成 $x_0+\theta(x-x_0)$（$\theta \in (0, 1)$），$\theta$ 也与 $x$ 和 $x_0$ 有关。

**证明：**

不失一般性，设 $x>x_0$。$\forall t\in [x_0, x]$，令

$$
F(t)=f(x)-\sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k,\quad G(t)=(x-t)^{n+1}
$$

则 $F\in\mathscr{C}[x_0, x]$ 在 $(x_0, x)$ 上可导，$\forall t\in [x_0, x]$，

$$
\begin{aligned}
&F'(t)=-\sum_{k=0}^{n}\frac{f^{(k+1)}(t)}{k!}(x-t)^k-\sum_{k=1}^{n}\frac{f^{(k)}(t)}{(k-1)!}(x-t)^{k-1}\cdot (-1)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n\\
&G'(t)=-(n+1)(x-t)^n
\end{aligned}
$$

又 $F(x)=G(x)=0$，则由Cauchy中值定理可知，$\exists\xi\in (x_0, x)$ 使得

$$
\frac{F(x_0)}{G(x_0)}=\frac{F(x)-F(x_0)}{G(x)-G(x_0)}
=\frac{F'(\xi)}{G'(\xi)}=\frac{f^{(n+1)}(\xi)}{(n+1)!}
$$

即
$$
F(x_0)=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}G(x_0)
=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}
$$
，故所证结论成立。

> [!example]+
> 已知 $f$ 在 $(a, b)$ 上二阶可导，证明：存在 $\xi \in (a, b)$，使
> $$
> f(b)-2f\left(\frac{a+b}{2}\right)+f(a)=\frac{(b-a)^2}{4}f''(\xi)
> $$
>
> ---
>
> **证明：**
>
> 取 $f$ 在 $\dfrac{a+b}{2}$ 处的Taylor展开，即存在 $\xi_x$ 严格介于 $x$ 与 $\dfrac{a+b}{2}$ 之间，有
> $$
> f(x)=f\left(\frac{a+b}{2}\right)+f'\left(\frac{a+b}{2}\right)\left(x - \frac{a+b}{2}\right)+\frac{f''(\xi_x)}{2}\left(x - \frac{a+b}{2}\right)^2
> $$
> 代入 $a$、$b$，即存在 $\xi_1 \in \left(a, \dfrac{a+b}{2}\right)$、$\xi_2 \in \left(\dfrac{a+b}{2}, b\right)$，使得
> $$
> \begin{aligned}
> f(a)&=f\left(\frac{a+b}{2}\right)+f'\left(\frac{a+b}{2}\right)\left(\frac{a-b}{2}\right)+\frac{f''(\xi_1)}{2}\left(\frac{a-b}{2}\right)^2\\
> f(b)&=f\left(\frac{a+b}{2}\right)+f'\left(\frac{a+b}{2}\right)\left(\frac{b-a}{2}\right)+\frac{f''(\xi_2)}{2}\left(\frac{b-a}{2}\right)^2
> \end{aligned}
> $$
> 两式相加，即
> $$
> f(b)-2f\left(\frac{a+b}{2}\right)+f(a)=\frac{(b-a)^2}{4} \cdot \frac{f''(\xi_1)+f''(\xi_2)}{2}
> $$
> 由Darboux定理，存在 $\xi \in (\xi_1, \xi_2) \subseteq (a, b)$，使 $f''(\xi)=\dfrac{f''(\xi_1)+f''(\xi_2)}{2}$，则原式得证。

> [!example]+
> 设 $x_0\in (a, b)$，函数 $f$ 在 $(a, b)$ 上可导，在 $x_0$ 处二阶可导且 $f''(x_0) \neq 0$。求证：
>
> （1）$\forall x \in (a, b)\backslash \{x_0\}$，$\exists \theta(x) \in (0, 1)$，使得 $f(x)=f(x_0)+f'(x_0+\theta(x)(x-x_0))(x-x_0)$；
>
> （2）由（1）给出的 $\theta(x)$ 满足 $\lim\limits_{x \to x_0}\theta(x)=\dfrac{1}{2}$。
>
> ---
>
> **证明：**
>
> 由带Lagrange余项的Taylor定理，令 $\xi = x_0 + \theta(x)(x-x_0)$，则知 $\forall x \in (a, b)\backslash \{x_0\}$，存在 $\xi$ 严格介于 $x_0, x$ 之间，也即 $\exists \theta(x) \in (0, 1)$，使得
> $$
> f(x)=f(x_0)+f'(\xi)(x-x_0)=f(x_0)+f'(x_0+\theta(x)(x-x_0))(x-x_0)
> $$
>
> 由夹逼原理，知 $\lim\limits_{x \to x_0}\theta(x)(x-x_0)=0$。则由导数定义知
> $$
> \begin{aligned}
> f''(x_0) &= \lim\limits_{\xi \to x_0}\frac{f'(\xi)-f'(x_0)}{\xi-x_0}
> = \lim\limits_{x \to x_0}\frac{f'(x_0 + \theta(x)(x-x_0))-f'(x_0)}{\theta(x)(x-x_0)}\\
> &= \lim\limits_{x \to x_0}\frac{\dfrac{f(x)-f(x_0)}{x-x_0}-f'(x_0)}{\theta(x)(x-x_0)}
> = \lim\limits_{x \to x_0}\frac{f(x)-f(x_0)-f'(x_0)(x-x_0)}{\theta(x)(x-x_0)^2}
> \end{aligned}
> $$
> 而 $\dfrac{f(x)-f(x_0)-f'(x_0)(x-x_0)}{(x-x_0)^2}$ 的极限可求：
> $$
> \lim\limits_{x \to x_0}\frac{f(x)-f(x_0)-f'(x_0)(x-x_0)}{(x-x_0)^2}
> \xlongequal{\textup{L'Hospital}}\lim\limits_{x \to x_0}\frac{f'(x)-f'(x_0)}{2(x-x_0)}
> =\frac{f''(x_0)}{2}
> $$
> 即 $f''(x_0) = \lim\limits_{x \to x_0} \dfrac{1}{\theta(x)} \cdot \dfrac{f''(x_0)}{2}$，又 $f''(x_0) \neq 0$，故 $\lim\limits_{x \to x_0}\theta(x)=\dfrac{1}{2}$。

当 $x_0=0$，即 $\xi_{x_0}(x)=\theta x$（$\theta \in (0, 1)$）时，有

> [!theorem] 带Lagrange余项的基本Taylor公式
> $$
> \begin{aligned}
> &e^x=\sum\limits_{k=0}^n\frac{x^k}{k!}+\frac{e^{\theta x}}{(n+1)!}x^{n+1}\\
> &\sin x=\sum\limits_{k=0}^n(-1)^{k}\frac{x^{2k+1}}{(2k+1)!}+(-1)^{n+1}\frac{\sin(\theta x)}{(2n+2)!}x^{2n+2}\\
> &\cos x=\sum\limits_{k=0}^n(-1)^k\frac{x^{2k}}{(2k)!}+(-1)^{n+1}\frac{\sin(\theta x)}{(2n+1)!}x^{2n+1}\\
> &\log(1+x)=\sum\limits_{k=1}^n(-1)^{k-1}\frac{x^{k}}{k}+\frac{(-1)^{n}x^{n+1}}{(n+1)(1+\theta x)^{n+1}}\\
> &(1+x)^{\alpha}=\sum\limits_{k=0}^n\frac{\alpha(\alpha-1)\cdots (\alpha-k+1)}{k!}x^k+\frac{\alpha(\alpha-1)\cdots (\alpha-n)}{(n+1)!}(1+\theta x)^{\alpha-n-1}x^{n+1}
> \end{aligned}
> $$
