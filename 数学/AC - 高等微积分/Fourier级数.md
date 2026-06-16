### Fourier 级数

#### 形式 Fourier 级数

> [!definition] 函数的内积
> $\forall f,g\in\mathscr{C}[a,b]$，$(f,g):=\dint_a^bf(x)g(x) \dif x$ 称之为 $f,g$ 的**内积**。如果 $(f,g)=0$，则称 $f$ 与 $g$ **正交**，记作 $f\perp g$。

> [!definition] 函数的范数
> $\forall f\in\mathscr{C}[a,b]$，$\|f\|=\sqrt{(f,f)} :=\left(\dint_a^b f^2(x) \dif x\right)^{\frac{1}{2}}$ 称为 $f$ 的**范数**。

$f\equiv 0$ 当且仅当 $\|f\|=0$；$\forall f,g \in\mathscr{C}[a,b]$，均有 $\|f+g\|\le \|f\|+\|g\|$。

> [!definition]
> $\varLambda=\{1,\cos x,\sin x,\cdots,\cos nx,\sin nx,\cdots\}$ 称为**三角函数系**。

三角函数系有如下的性质：

> [!lemma] 正交性
> 三角函数系 $\Lambda$ 在 $[a,a+2\pi]$ 上为非零的正交函数系，即 $\forall f,g \in \varLambda$，若 $f\neq g$，则
> $$
> \dint_a^{a+2\pi}f(x)g(x) \dif x=0
> $$

事实上，$\forall n,m\ge 1$ 且 $n\neq m$ 有
$$
\begin{aligned}
&\int_a^{a+2\pi}1\dif x=2\pi,\quad
\int_a^{a+2\pi}\cos^2 nx\dif x=\int_a^{a+2\pi}\sin^2 nx\dif x=\pi,\\
&\int_a^{a+2\pi}\cos nx\dif x =\int_a^{a+2\pi}\sin nx\dif x=0,\\
&\int_a^{a+2\pi}\cos mx\cos nx\dif x =\int_a^{a+2\pi}\cos mx\sin nx\dif x=\int_a^{a+2\pi}\sin mx\sin nx\dif x=0
\end{aligned}
$$

> [!lemma] 完全性
> 如果 $f\in\mathscr{C}(\mathbb{R})$ 是以 $2\pi$ 为周期的周期函数使得 $\forall g\in \varLambda$，均有 $\dint_a^{a+2\pi}f(x)g(x)\dif x=0$，则我们有 $f\equiv 0$。

由此可知，$\varLambda$ 当中的元素在 $\mathbb{R}$ 上线性无关，且 $\varLambda$ 就是 $\mathscr{C}(\mathbb{R})$ 中以 $2\pi$ 为周期的周期函数空间的一组基。

> [!definition] 三角级数
> 形如 $\dfrac{a_0}{2}+\sum\limits_{n=1}^{\infty}(a_n\cos nx+b_n\sin nx)$ 称为**三角级数**。

假设 $f$ 是以 $2\pi$ 为周期的周期函数且 $f(x)=\dfrac{a_0}{2}+\sum\limits_{k=1}^{\infty}(a_k\cos kx+b_k\sin kx)$ 在 $[-\pi,\pi]$ 上一致收敛，则由积分与级数求和可交换性立刻可知
$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\dif x\ (n\ge 0),\qquad
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\dif x\ (n\ge 1)
$$

> [!definition] Fourier 系数
> 假设 $f: \mathbb{R}\rightarrow\mathbb{R}$ 是以 $2\pi$ 为周期的周期函数且 $f\big|_{[-\pi,\pi]}\in\mathscr{R}[-\pi,\pi]$，则称
> $$
> a_n(f)=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\dif x\ (n\ge 0),\qquad
> b_n(f)=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\dif x\ (n\ge 1)
> $$
> 为 $f$ 的 **Fourier 系数**，并记
> $$
> f(x)\sim \frac{a_0(f)}{2}+\sum_{n=1}^{\infty}\left(\boldsymbol{a_n(f)}\cos nx+\boldsymbol{b_n(f)}\sin nx\right)
> $$
> 为 $f$ 的**形式 Fourier 级数**。

若 $f$ 为偶函数，则 $\forall n\ge 1$，$b_n(f)=0$，此时 $\forall n\ge 0$，$a_n(f)=\dfrac{2}{\pi}\dint_0^{\pi}f(x)\cos nx\dif x,\ b_n(f)=0$，相应的 Fourier 级数称为**余弦级数**；若 $f$ 为奇函数，则 $\forall n\ge 0$，$a_n(f)=0$，此时 $\forall n\ge 1$，$a_n(f)=0$，$b_n(f)=\dfrac{2}{\pi}\dint_0^{\pi}f(x)\sin nx\dif x$，相应的 Fourier 级数称为**正弦级数**。

> [!example]+ 证明：如果级数 $\dfrac{|a_0|}2+\sum\limits_{k=1}^\infty\left(|a_k|+|b_k|\right)<+\infty$，那么级数 $\dfrac{a_0}2+\sum\limits_{k=1}^\infty\left(a_k\cos kx+b_k\sin kx\right)$ 必为某个周期为 $2\pi$ 的函数的傅里叶级数。
>
>
> ---
>
> **证明：**我们熟知如下引理：
>
> [!lemma]
> 周期为 $2\pi$ 的 $n$ 次三角多项式 $T_n(x) = \sum\limits_{k=0}^n \left(a_k \cos kx + b_k \sin kx\right)$ 的 Fourier 级数就是其本身。

由非负项级数 $\dfrac{|a_0|}2+\sum\limits_{k=1}^\infty\left(|a_k|+|b_k|\right)$ 有上界，知其收敛，则由 Weierstrass 判别法，
$$
\left|\dfrac{a_0}2\right|+\sum\limits_{k=1}^\infty\left|a_k\cos kx+b_k\sin kx\right|
\le \dfrac{\left|a_0\right|}2+\sum\limits_{k=1}^\infty\left(\left|a_k\cos kx\right|+\left|b_k\sin kx\right|\right)
\le \dfrac{|a_0|}2+\sum\limits_{k=1}^\infty\left(|a_k|+|b_k|\right)
$$
知 $\dfrac{a_0}2+\sum\limits_{k=1}^\infty\left(a_k\cos kx+b_k\sin kx\right)$ 绝对且一致收敛于某个函数 $S(x)$。对上述引理取 $n \to \infty$，即知 $S(x)$ 是所求的函数，即该级数是函数 $S(x)$ 的傅里叶级数。

#### Fourier 级数的性质及收敛性

> [!lemma] Riemann-Lebesgue 引理
> 若 $f$ 在 $[a,b]$ 上可积，则
> $$
> \lim\limits_{\lambda\rightarrow \infty}\int_a^b f(x)\sin (\lambda x)\dif x
> =\lim\limits_{\lambda\rightarrow \infty}\int_a^b f(x)\cos (\lambda x)\dif x=0
> $$

这个引理保证了，若 $f:\mathbb{R}\rightarrow\mathbb{R}$ 是以 $2\pi$ 为周期的周期函数且在 $[-\pi,\pi]$ 上可积，则 $\lim\limits_{n\rightarrow \infty}a_n(f)=\lim\limits_{n\rightarrow \infty}b_n(f)=0$。

> [!theorem] Dirichlet-Jordan 定理
> 假设 $f$ 是以 $2\pi$ 为周期的周期函数。如果 $f$ 在 $[-\pi,\pi]$ 上逐段单调有界或逐段可微，那么 $\forall x\in \mathbb{R}$，函数 $f$ 的 Fourier 级数在点 $x$ 处收敛到 $S(x)=\dfrac{1}{2}\left(f(x-0)+f(x+0)\right)$。
>
> > [!definition]
> > 考虑函数 $f:[a,b]\rightarrow\mathbb{R}$ 及区间 $[a,b]$ 的分割 $a=x_0<x_1<\cdots <x_n=b$。
> >
> > （1）若 $f$ 在每个子区间 $(x_{j-1},x_j)$ 上单调，则称函数 $f$ 为**逐段（或分段）单调**。
> >
> > （2）若 $f$ 在每个子区间 $[x_{j-1},x_j]$ 上可微，则称函数 $f$ 为**逐段（或分段）可微**；此时 $f$ 在 $[a,b]$ 上**逐段连续**，因此 $f$ 为有界函数。

更一般地，就有

> [!theorem] 收敛性定理
> 设 $f$ 是以 $2\pi$ 为周期的周期函数，并且在 $[-\pi,\pi]$ 上可积。如果函数 $f$ 在 $(-\pi,\pi)$ 上连续且逐段单调有界，或者有有界导数，那么 $f$ 的 Fourier 级数在 $(-\pi,\pi)$ 的任意闭子区间上一致收敛到 $f$ 本身。

> [!note] 非 $\mathbb{R}$ 上周期函数的延拓
> 对于定义在区间 $(-\pi,\pi)$ 上的任意函数 $f$，尽管它并不是定义在 $\mathbb{R}$ 上并且以 $2\pi$ 为周期的函数，我们仍然可以将 $f$ 延拓成为以 $2\pi$ 为周期的函数，从而定义其 Fourier 系数（若相关积分均存在），由此得到形式 Fourier 级数。
>
> 为此，我们取 $f(\pi)=f(-\pi)$ 为任意常数，再将 $f$ 以 $2\pi$ 为周期从区间 $[-\pi,\pi]$ 延拓到整个 $\mathbb{R}$ 上。随后再来考虑延拓后的函数 $f$ 的 Fourier 级数。若此时函数 $f$ 满足 Dirichlet-Jordan 定理的条件，则 $\forall x\in (-\pi,\pi)$，函数 $f$ 的 Fourier 级数在点 $x$ 收敛到 $S(x)=\dfrac{1}{2}\left(f(x-0)+f(x+0)\right)$，在两个端点 $x=\pm \pi$ 收敛到 $\dfrac{1}{2}\left(f(-\pi+0)+f(\pi-0)\right)$。

> [!example]+ $\forall x\in (-\pi,\pi)$，定义 $f(x)=\e^{-x}$。求函数 $f$ 在 $(-\pi,\pi)$ 内的 Fourier 级数并讨论其收敛性。
>
>
> ---
>
> **解：**由定义可知
> $$
> a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}\e^{-x}\dif x =\frac{1}{\pi}(\e^{\pi}-\e^{-\pi }) =\frac{2}{\pi}\sinh\pi
> $$
> 而 $\forall n\ge 1$，我们也有
> $$
> \begin{aligned}
> a_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}\e^{-x}\cos (nx)\dif x =(-1)^n\frac{2}{\pi(1+n^2)}\sinh\pi,\\
> b_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}\e^{-x}\sin (nx)\dif x =(-1)^n\frac{2n}{\pi(1+n^2)}\sinh\pi
> \end{aligned}
> $$
> 由于 $f$ 在 $(-\pi,\pi)$ 上可微，则 $\forall x\in (-\pi,\pi)$，
> $$
> \e^{-x}=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos (nx)+b_n\sin (nx)\right)
> =\frac{2\sinh\pi}{\pi}\left(\frac{1}{2}+ \sum_{n=1}^{\infty}\left(\frac{(-1)^n}{1+n^2}\cos (nx)+\frac{(-1)^nn}{1+n^2}\sin (nx)\right)\right)
> $$
> 上述 Fourier 级数在点 $x=\pm\pi$ 处收敛到 $\dfrac{1}{2}(f(-\pi+0)+f(\pi-0))=\dfrac{1}{2}(\e^{\pi}+\e^{-\pi})$。
>
> 特别地，在 $x=0$ 处，则有 $1=\dfrac{2\sinh\pi}{\pi}\left(\dfrac{1}{2}+\sum\limits_{n=1}^{\infty}\dfrac{(-1)^n}{1+n^2}\right)$，故
> $$
> \sum\limits_{n=1}^{\infty}\dfrac{(-1)^n}{1+n^2}=\dfrac{\pi}{2\sinh\pi}-\dfrac{1}{2}
> $$
> 而在点 $x=\pi$ 处，我们有 $\dfrac{2\sinh\pi}{\pi}\left(\dfrac{1}{2}+\sum\limits_{n=1}^{\infty}\dfrac{1}{1+n^2}\right)=\dfrac{1}{2}(\e^{\pi}+\e^{-\pi})=\cosh\pi$，于是
> $$
> \sum\limits_{n=1}^{\infty}\frac{1}{1+n^2}=\frac{\pi}{2\tanh \pi}-\frac{1}{2}
> $$
>
> [!note] 一般周期函数的 Fourier 级数
> 假设 $\ell>0$ 而 $T=2\ell$。对周期为 $T$ 的周期函数，我们可以相应地引入在任何长度为 $T$ 的区间上均为正交的三角函数系
> $$
> \Big\{1,\cos \dfrac{\pi}{\ell} x,\sin \dfrac{\pi}{\ell} x,\cdots,\cos \dfrac{n\pi}{\ell} x,\sin \dfrac{n\pi}{\ell} x,\cdots\Big\}
> $$
> 关于该函数系，前面介绍的所有结论依然成立。例如对 Dirichlet-Jordan 定理，只需将 $\pi$ 换成 $\ell$。
>
> 特别地，我们可以类似定义：
> $$
> a_n(f)=\frac{1}{\ell}\int_{-\ell}^{\ell}f(x)\cos \frac{n\pi}{\ell} x\dif x\ (n\ge 0),\quad
> b_n(f)=\frac{1}{\ell}\int_{-\ell}^{\ell}f(x)\sin \frac{n\pi}{\ell} x\dif x\ (n\ge 1)
> $$
> 称为 $f$ 的 Fourier 系数，并记
> $$
> f(x)\sim \frac{a_0(f)}{2}+\sum_{n=1}^{\infty}\left(a_n(f)\cos \frac{n\pi}{\ell} x +b_n(f) \sin \frac{n\pi}{\ell} x \right)
> $$
> 称上述函数项级数为 $f$ 的（形式）Fourier 级数。

若只给定 $f(x)$ 是定义在 $(0,L)$ 上的函数，为求其周期为 $2L$ 的 Fourier 级数，有两种延拓方式：

- **奇延拓** $\quad \forall x\in (-L,L)$，定义
  $$
  F(x)=\begin{cases}
      f(x), & \text{若}\ x\in (0,L),\\
      -f(-x), & \text{若}\ x\in (-L,0),
  \end{cases}
  $$
  此时 $\forall n\ge 0$，$a_n=0$，而 $\forall n\ge 1$，我们则有 $b_n=\dfrac{2}{L}\dint_0^{L}f(x)\sin \dfrac{n\pi}{L}x\dif x$，相应的 Fourier 级数为正弦级数。

- **偶延拓** $\quad \forall x\in (-L,L)$，定义
  $$
  F(x)=\begin{cases}
      f(x), & \text{若}\ x\in (0,L),\\
      f(-x), & \text{若}\ x\in (-L,0),
  \end{cases}
  $$
  此时 $\forall n\ge 0$，$b_n=0$，而 $\forall n\ge 1$，我们则有 $a_n=\dfrac{2}{L}\dint_0^{L}f(x)\cos \dfrac{n\pi}{L}x\dif x$，相应的 Fourier 级数为余弦级数。

> [!example]+ $\forall x\in[0,2]$，令 $f(x)=2-x$。将 $f$ 在 $[0,2]$ 上展成以 $4$ 为周期的余弦级数并求和函数。
>
>
> ---
>
> **解：**首先将 $f$ 偶延拓而定义
> $$
> F(x)=\begin{cases}
> 2-x, & \text{若}\ x\in [0,2],\\
> 2+x, & \text{若}\ x\in [-2,0],
> \end{cases}
> $$
> 此时 $T=4$，$\ell=2$。故 $F$ 的 Fourier 系数满足 $b_n=0\ (n\ge 1)$。另外，我们还有
> $$
> a_0=\frac{2}{\ell}\int_0^{\ell}F(x)\dif x =\int_0^2(2-x)\dif x =2
> $$
>
> $\forall n\ge 1$，我们有
> $$
> a_n=\frac{2}{\ell}\int_0^{\ell}F(x)\cos\frac{n\pi}{\ell}x\dif x
> =\int_0^2(2-x)\cos\frac{n\pi}{2}x\dif x
> =\left(\frac{2}{n\pi}\right)^2(1-\cos (n\pi))
> =\left(\frac{2}{n\pi}\right)^2\left(1-(-1)^n\right)
> $$
> 由于函数 $F$ 在 $[-2,2]$ 上为连续并且分段可微，而 $F(-2)=F(2)$，于是 $\forall x\in [0,2]$，我们有
> $$
> f(x)=2-x =1+\sum_{k=1}^{\infty}\frac{8}{(2k-1)^2\pi^2}\cos\frac{(2k-1)\pi}{2}x
> $$
>
> 特别地，在点 $x=0$ 处，我们有 $2=1+\sum\limits_{k=1}^{\infty}\dfrac{8}{(2k-1)^2\pi^2}$，由此立刻可得 $\sum\limits_{k=1}^{\infty}\dfrac{1}{(2k-1)^2}=\dfrac{\pi^2}{8}$。
>
#### Fourier 级数的平方平均收敛

对任意的整数 $n\ge 1$，我们令
$$
\varLambda_n=\{1,\cos x,\sin x,\cdots,\cos (nx),\sin (nx)\}
$$
如果将 $\varLambda_n$ 所张成的实线性空间记作 $\mathcal{W}_n$，那么 $\mathcal{W}_n$ 为 $\mathscr{R}[-\pi,\pi]$ 的 $2n+1$ 维子空间。

> [!theorem] 最佳逼近定理
> $\forall f\in\mathscr{R}[-\pi,\pi]$，令
> $$
> S_n(f)=\frac{a_0(f)}{2}+\sum_{k=1}^{n}\left(a_k(f)\cos (kx)+b_k(f)\sin (kx)\right)
> $$
> 则 $\|f-S_n(f)\|=\min\limits_{g\in \mathcal{W}_n}\|f-g\|$，且最小值仅在 $g=S_n(f)$ 处达到，此时有 $(f-S_n(f)) \perp \mathcal{W}_n$。

**证明：**对任意的整数 $0\le k\le n$，我们有
$$
\begin{aligned}
\bigl(f-S_n(f),\cos (kx)\bigr)
&=\int_{-\pi}^{\pi}f(x)\cos (kx)\dif x-\int_{-\pi}^{\pi}S_n(f)(x)\cos (kx)\dif x \\
&=\pi a_k(f)-\pi a_k(f) =0
\end{aligned}
$$
同样，$\forall 1\le k\le n$，均有 $\bigl(f - S_n(f),\sin (kx)\bigr) = 0$。于是 $f-S_n(f)$ 与 $\varLambda_n$ 中的任意元素正交，从而由线性性可知，$f-S_n(f)$ 与 $\mathcal{W}_n$ 中的任意元素正交，也就是说 $f-S_n(f) \perp \mathcal{W}_n$。

$\forall g\in \mathcal{W}_n$，定义 $F_n=f-S_n(f)$，$G_n=g-S_n(f)$，则 $G_n\in \mathcal{W}_n$，从而 $(F_n,G_n)=0$，且我们有
$$
\|f-g\|^2=\|(f-S_n(f))-(g-S_n(f))\|^2
=\|F_n-G_n\|^2
=\|F_n\|^2+\|G_n\|^2 \ge \|F_n\|^2
$$
上式恰好表明我们有
$$
\min\limits_{g\in \mathcal{W}_n}\|f-g\|=\|F_n\| =\|f-S_n(f)\|
$$
并且仅当 $\|G_n\|^2 = 0$，即 $g=S_n(f)$ 时取到最小值。

> [!lemma] Bessel 不等式
> $\forall f\in\mathscr{R}[-\pi,\pi]$，均有
> $$
> \frac{1}{2}\left(a_0(f)\right)^2+\sum_{k=1}^{\infty}\left(\left(a_k(f)\right)^2+\left(b_k(f)\right)^2\right)
> \le \frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)\right)^2\dif x
> $$

**证明：**对任意整数 $n\ge 1$，我们有
$$
\begin{aligned}
0&\le \|f-S_n(f)\|^2
=\|f\|^2+\|S_n(f)\|^2-2(f,S_n(f)) \\
&=\int_{-\pi}^{\pi}\left(f(x)\right)^2\dif x
+ \pi\left(\frac{a_0^2}{2}+\sum_{k=1}^n(a_k^2+b_k^2)\right)
- \pi \left(a_0^2+2\sum_{k=1}^{n}\left(a_k^2+b_k^2\right)\right) \\
&=\int_{-\pi}^{\pi}\left(f(x)\right)^2\dif x-\pi\left(\frac{a_0^2}{2}+\sum_{k=1}^n(a_k^2+b_k^2)\right)
\end{aligned}
$$
由此立得
$$
\frac{a_0^2}{2}+\sum_{k=1}^n(a_k^2+b_k^2)\le \frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)\right)^2\dif x
$$
随后让 $n\rightarrow\infty$，可知
$$
\frac{a_0^2}{2}+\sum_{k=1}^{\infty}(a_k^2+b_k^2)\le \frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)\right)^2\dif x
$$

> [!corollary]
> $\forall f\in\mathscr{R}[-\pi,\pi]$，级数 $\dfrac{1}{2}\left(a_0(f)\right)^2+\sum\limits_{k=1}^{\infty}\left(\left(a_k(f)\right)^2+\left(b_k(f)\right)^2\right)$ 收敛。

> [!theorem] Parseval 等式
> $\forall f\in\mathscr{R}[-\pi,\pi]$，均有
> $$
> \frac{1}{2}\left(a_0(f)\right)^2+\sum_{k=1}^{\infty}\left(\left(a_k(f)\right)^2+\left(b_k(f)\right)^2\right)
> =\frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)\right)^2\dif x
> $$

> [!corollary] 唯一性
> 若 $f,g\in\mathscr{R}[-\pi,\pi]$ 有相同的 Fourier 级数，则 $f,g$ 几乎处处相等；若 $f,g\in\mathscr{C}[-\pi,\pi]$ 有相同的 Fourier 级数，则 $f \equiv g$。

**证明：**由于 $a_0(f-g)=a_0(f)-a_0(g)=0$，而且 $\forall n\ge 1$，同样也有 $a_n(f-g)=0$，$b_n(f-g)=0$，于是由 Parseval 等式可知 $\dint_{-\pi}^{\pi}\left(f(x)-g(x)\right)^2\dif x=0$。

> [!theorem] Fourier 级数在范数意义下的收敛（平方平均收敛）
> $\forall f\in\mathscr{R}[-\pi,\pi]$，均有 $\lim\limits_{n\rightarrow\infty}\|S_n(f)-f\|=0$。

**证明：**$\|f-S_n(f)\|^2=\dint_{-\pi}^{\pi}\left(f(x)\right)^2\dif x-\pi\left(\dfrac{a_0^2}{2}+\sum\limits_{k=1}^n(a_k^2+b_k^2)\right)$，再让 $n\rightarrow\infty$。

> [!corollary] 广义 Parseval 等式
> $\forall f,g\in\mathscr{R}[-\pi,\pi]$，均有
> $$
> \frac{1}{2}a_0(f)a_0(g)+\sum_{k=1}^{\infty}\left(a_k(f)a_k(g)+b_k(f)b_k(g)\right)=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)g(x)\dif x
> $$

**证明：**对任意的整数 $n\ge 1$，我们有
$$
\begin{aligned}
\frac{1}{\pi}\int_{-\pi}^{\pi} f(x)g(x)\dif x
&=\frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)-S_n(f)\right)g(x)\dif x
+\frac{1}{\pi}\int_{-\pi}^{\pi} S_n(f)(x)g(x)\dif x \\
&=\frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)-S_n(f)\right)g(x)\dif x \\
&\quad+\frac{1}{\pi}\int_{-\pi}^{\pi} \left(\frac{a_0(f)}{2}+\sum_{k=1}^{n}\left(a_k(f)\cos (kx)+b_k(f)\sin (kx)\right)\right)g(x)\dif x \\
&=\frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)-S_n(f)\right)g(x)\dif x +\frac{a_0(f)}{2}\frac{1}{\pi}\int_{-\pi}^{\pi}g(x)\dif x \\
&\quad+ \sum_{k=1}^{n}\left(a_k(f)\frac{1}{\pi}\int_{-\pi}^{\pi}\cos (kx)g(x)\dif x +b_k(f)\frac{1}{\pi}\int_{-\pi}^{\pi}\sin (kx)g(x)\dif x \right)\\
&=\frac{1}{\pi}\int_{-\pi}^{\pi}\left(f(x)-S_n(f)\right)g(x)\dif x+\frac{1}{2}a_0(f)a_0(g)+\sum_{k=1}^{n}\left(a_k(f)a_k(g)+b_k(f)b_k(g)\right)
\end{aligned}
$$
由 Cauchy 不等式，我们立刻有
$$
\begin{aligned}
\left|\int_{-\pi}^{\pi}\left(f(x)-S_n(f)\right)g(x)\dif x\right|
&\le \int_{-\pi}^{\pi}|f(x)-S_n(f)|\cdot |g(x)|\dif x \\
&\le \left(\int_{-\pi}^{\pi}|f(x)-S_n(f)|^2\dif x\right)^{\frac{1}{2}}\cdot
\left(\int_{-\pi}^{\pi}|g(x)|^2\dif x\right)^{\frac{1}{2}}
= \|f-S_n(f)\| \cdot \|g\|
\end{aligned}
$$
又 $\lim\limits_{n\rightarrow\infty}\|f-S_n(f)\|=0$，于是由夹逼原理可知所证结论成立。

> [!theorem] Fourier 级数求和与积分的可交换性
> $\forall f\in\mathscr{R}[-\pi,\pi]$ 以及 $\forall a,x\in [-\pi,\pi]$，均有
> $$
> \int_{a}^{x}f(t)\dif t
> =\frac{1}{2}a_0(f)(x-a)
> +\sum_{k=1}^{\infty}\int_a^x\left(a_k(f)\cos (kt)+b_k(f)\sin (kt)\right)\dif t
> $$
> 也即 Fourier 级数求和（即便它**不是点态收敛**时也成立）总是可以与积分交换次序。

**证明：**固定 $a,x\in [-\pi,\pi]$。不失一般性，我们可假设 $a<x$。$\forall t\in [-\pi,\pi]$，令
$$
g(t)=\begin{cases}
    1, & \text{若}\ t\in [a,x],\\
    0, & \text{若}\ t\notin [a,x],
\end{cases}
$$
则 $g$ 在 $[-\pi,\pi]$ 上可积。于是我们有
$$
\begin{aligned}
\int_{a}^{x}f(t)\dif t=\int_{-\pi}^{\pi}f(t)g(t)\dif t
&=\frac{\pi}{2}a_0(f)a_0(g)
+\pi\sum_{k=1}^{\infty}\left(a_k(f)a_k(g)+b_k(f)b_k(g)\right) \\
&=\frac{\pi}{2}a_0(f)\int_a^x \dif t
+\pi\sum_{k=1}^{\infty}\left(a_k(f)\int_a^x \cos kt \dif t+b_k(f)\int_a^x \sin kt \dif t\right) \\
&=\frac{1}{2}a_0(f)(x-a)
+\sum_{k=1}^{\infty}\int_a^x\left(a_k(f)\cos (kt)+b_k(f)\sin (kt)\right)\dif t
\end{aligned}
$$
