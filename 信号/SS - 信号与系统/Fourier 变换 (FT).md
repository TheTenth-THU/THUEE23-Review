Fourier's Evaluation of FT:

> Regarding the researches of d’Alembert and Euler could one not add that if they knew this expansion, they made but a very imperfect use of it. *They were both persuaded that an arbitrary and discontinuous function could never be resolved in series of this kind*, and it does not even seem that anyone had developed a constant in cosines of multiple arcs, the first problem which I had to solve in the theory of heat.
> 
> (Joseph Fourier, 1808)

## 从 [[Fourier 级数 (FS)]] 到 Fourier 变换

周期 $T_{1}$ 增大时，
+ 谱线间隔 $\omega_{1} = \dfrac{2\pi}{T_{1}}$ **$\to 0$**，**离散谱变成连续谱**，
+ 谱线强度 $|F(n\omega_{1})|$ **$\to 0$**，而相对长度 $|F(n\omega_{1})|T_{1}$ 仍有意义。
 
![[Pasted image 20250609145107.png]]

### 定义

令所考虑的周期 $T_{1} \to \infty$，得到 Fourier 级数**频谱密度**变为
$$
\lim\limits_{ T_{1} \to \infty } T_{1}F(n\omega_{1}) = \lim\limits_{ T_{1} \to \infty } \dint_{-T_{1}/2}^{T_{1}/2} f(t) \e^{-\I \omega t} \dif t
$$
同时 Fourier 级数展开式变为
$$
\begin{align}
f(t) &= \sum\limits_{n=-\infty}^{\infty} F(n\omega_{1}) \e^{\I n\omega_{1} t} = \dfrac{1}{2\pi} \sum\limits_{n=-\infty}^{\infty} T_{1} F(n\omega_{1}) \e^{\I n\omega_{1} t} \omega_{1} \\
&\xrightarrow[\omega_{1} \to \dif \omega,\ n\omega_{1} \to \omega]{T_{1} \to \infty} \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} F(\omega) \e^{\I \omega t} \dif \omega
\end{align}
$$

> [!definition] Fourier 变换和逆变换
> 对于一个函数 $f(t)$，其 **Fourier 变换**和**逆变换**定义为
> $$
> \begin{align}
> &F(\omega) = \mathscr{F} \{ f(t) \} = \dint_{-\infty}^{\infty} f(t) \e^{-\I\omega t} \dif t \\
> &f(t) = \mathscr{F}^{-1} \{ F(\omega) \} = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} F(\omega) \e^{\I\omega t} \dif \omega
> \end{align}
> $$

其中，$F(\omega)$ 称为**频谱**，一般是复函数，记作
$$
F(\omega) = |F(\omega)| \e^{\I\varphi(\omega)}
$$
+ $|F(\omega)|$ 称为**幅度谱**，表示信号中各频率分量的**相对大小**；
+ $\varphi(\omega)$ 称为**相位谱**，表示各频率分量之间的**相位关系**。

### Fourier 变换的收敛条件

Fourier 变换存在的充分非必要条件是**狄利克雷条件**，要求在无限区间内**绝对可积**，即
$$
\dint_{-\infty}^{\infty} |f(t)| \dif t < \infty
$$
借助**奇异函数**，周期信号、阶跃信号和符号函数等许多不满足绝对可积条件的信号也存在 Fourier 变换。

## Fourier 变换的基本性质

### 对称互易性

若 $F(\omega) = \mathscr{F}\{ f(t) \}$，则
$$
\mathscr{F} \{ F(t) \} = 2\pi f(-\omega), \qquad
\mathscr{F} ^{-1} \{ f(\omega) \} = \dfrac{1}{2\pi} F(-t)
$$

### 线性性（叠加性、齐次性）

给定两个函数 $f_{1}(t)$ 和 $f_{2}(t)$，以及两个常数 $a$ 和 $b$，则有
$$
\mathscr{F}\{a f_{1}(t) + b f_{2}(t)\} = a \mathscr{F}\{f_{1}(t)\} + b \mathscr{F}\{f_{2}(t)\}
$$

### 奇偶虚实性

$f(t)$ 奇偶、虚实分量
$$
f(t) = \mathfrak{Re}\{ f_{\mathrm{e}}(t) \} + \I \mathfrak{Im}\{ f_{\mathrm{e}}(t) \}
+ \mathfrak{Re}\{ f_{\mathrm{o}}(t) \} + \I \mathfrak{Im}\{ f_{\mathrm{o}}(t) \}
$$
的 Fourier 变换分别为
$$
\begin{align}
&\mathscr{F} \{ \mathfrak{Re}\{ f_{\mathrm{e}}(t) \} \} &&= 2 \dint_{0}^{\infty} \mathfrak{Re}\{ f_{\mathrm{e}}(t) \} \cos (\omega t) \dif t &&= \mathfrak{Re}\{ F_{\mathrm{e}}(\omega) \} && \text{实、偶}\\
&\mathscr{F} \{ \I\mathfrak{Im}\{ f_{\mathrm{e}}(t) \} \} &&= 2\I \dint_{0}^{\infty} \mathfrak{Im}\{ f_{\mathrm{e}}(t) \} \cos (\omega t) \dif t &&= \I\mathfrak{Im}\{ F_{\mathrm{e}}(\omega) \} && \text{虚、偶}\\
&\mathscr{F} \{ \mathfrak{Re}\{ f_{\mathrm{o}}(t) \} \} &&= -2\I \dint_{0}^{\infty} \mathfrak{Re}\{ f_{\mathrm{o}}(t) \} \sin (\omega t) \dif t &&= \I\mathfrak{Im}\{ F_{\mathrm{o}}(\omega) \} && \text{虚、奇} \\
&\mathscr{F} \{ \I\mathfrak{Im}\{ f_{\mathrm{o}}(t) \} \} &&= 2 \dint_{0}^{\infty} \mathfrak{Im}\{ f_{\mathrm{o}}(t) \} \sin (\omega t) \dif t &&= \mathfrak{Re}\{ F_{\mathrm{o}}(\omega) \} && \text{实、奇}
\end{align}
$$

![[Pasted image 20250609162437.png]]

### $t$ 域微分、积分

对于**可微**函数 $f(t)$，有
$$
\mathscr{F}\left\{ \dfrac{\dif f(t)}{\dif t} \right\} = \I\omega F(\omega)
$$
进一步地，对于 **$n$ 阶可微**函数 $f(t)$，有
$$
\mathscr{F}\left\{ \dfrac{\dif^{n} f(t)}{\dif t^{n}} \right\} = (\I\omega)^{n} F(\omega)
$$

对于**可积**函数 $f(t)$，有
$$
\mathscr{F}\left\{ \int_{-\infty}^{t} f(\tau) \dif \tau \right\} = \dfrac{F(\omega)}{\I\omega} + \pi F(0) \delta(\omega)
$$

### $t$ 域平移

对于函数 $f(t)$，
$$
\mathscr{F}\{f(t-t_{0})\} = F(\omega) \e^{-\I \omega t_{0}}
$$
即，原函数延迟 $t_{0}$，其 Fourier 变换乘以 $\e^{-\I\omega t_{0}}$，**相移改变 $-\omega t_{0}$**。

### $t$ 域缩放

对于函数 $f(t)$，
$$
\mathscr{F}\{f(at)\} = \dfrac{1}{|a|} F\left(\dfrac{\omega}{a}\right)
$$
**时域压缩 $⇔$ 频域扩展；时域扩展 $⇔$ 频域压缩。**

特别地，$\mathscr{F} \{ f(-t) \} = F(-\omega)$。

### $\omega$ 域微分、积分

对于**可微**的 Fourier 变换像函数 $F(\omega)$，有
$$
\dfrac{\dif F(\omega)}{\dif \omega} = \mathscr{F}\{-\I t f(t)\}
$$

对于**可积**的 Fourier 变换像函数 $F(\omega)$，有
$$
\dint_{-\infty}^{\omega} F(\varOmega) \dif \varOmega = \mathscr{F} \left\{ - \dfrac{f(t)}{\I t} + \pi f(0) \delta(t) \right\}
$$

### $\omega$ 域平移

对于 Fourier 变换像函数 $F(\omega)$，
$$
F(\omega - \omega_{0}) = \mathscr{F}\{f(t)\e^{\I\omega_{0} t}\} 
$$
即，原函数被 $\e^{\I\omega t}$ 加权，则像函数**在频域上右移 $\omega_{0}$**。

### 卷积性质

> [!theorem] 时域卷积定理
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Fourier 变换 $F_{1}(\omega)$、$F_{2}(\omega)$ 存在，则
> $$
> \mathscr{F}\{f_{1}(t) * f_{2}(t)\} = F_{1}(\omega) F_{2}(\omega)
> $$

> [!theorem] 频域卷积定理 
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Fourier 变换 $F_{1}(s)$、$F_{2}(s)$ 存在，则
> $$
> \mathscr{F}\{f_{1}(t) f_{2}(t)\} = \dfrac{1}{2\pi} F_{1}(\omega) * F_{2}(\omega)
> $$

**时域卷积 $=$ 频域相乘；时域相乘 $\propto$ 频域卷积。**

## 典型信号的 Fourier 变换

### 典型非周期信号的 Fourier 变换

#### 指数信号

+ **单边指数信号** $f(t) = \begin{cases} \e^{-at}, &t \ge 0 \\ 0, &t < 0 \end{cases}$（$a > 0$）
    $$
    F(\omega) = \dint_{0}^{\infty} \e^{-at} \e^{-\I\omega t} \dif t = \dfrac{1}{a + \I\omega}
    $$

+ **双边指数信号** $f(t) = \e^{-a|t|}$（$a > 0$）
    $$
    F(\omega) = \dint_{-\infty}^{\infty} \e^{-a|t|} \e^{-\I\omega t} \dif t = \dfrac{2a}{a^{2} + \omega^{2}}
    $$

#### 脉冲信号

+ **矩形脉冲 $\mathrm{rect}(t)$** $= E \big( u(t+\tau/2) - u(t-\tau/2) \big)$
    $$
    \mathscr{F}\{ \mathrm{rect}(t) \} = \dint_{-\tau/2}^{\tau/2} E \e^{-\I\omega t} \dif t = \dfrac{2E}{\omega} \sin \left( \dfrac{\omega\tau}{2} \right) = E\tau \mathrm{Sa} \left( \dfrac{\omega\tau}{2} \right)
    $$

+ **三角脉冲 $\mathrm{tri}(t)$** $= \begin{cases}E\left( 1 - \dfrac{|t|}{\tau} \right), & |t| < \tau, \\ 0, & |t| \ge \tau \end{cases} = \dfrac{1}{E\tau} \mathrm{rect}(t) * \mathrm{rect}(t)$
    $$
    \mathscr{F}\{ \mathrm{tri}(t) \} = \dfrac{1}{E\tau} \mathscr{F}\{ \mathrm{rect}(t) \}^{2} = E\tau \mathrm{Sa}^{2} \left( \dfrac{\omega\tau}{2} \right)
    $$

+ **升余弦脉冲** $f(t) = \begin{cases} \dfrac{E}{2} \left( 1 + \cos \left( \dfrac{\pi t}{\tau} \right) \right), & |t| < \tau, \\ 0, & |t| \ge \tau \end{cases}$
    $$
    F(\omega) = \dint_{-\tau}^{\tau} \dfrac{E}{2} \left( 1 + \cos \left( \dfrac{\pi t}{\tau} \right) \right) \e^{-\I\omega t} \dif t
    = \dfrac{E\tau \mathrm{Sa}(\omega \tau)}{1 - \left( \dfrac{\omega \tau}{\pi} \right)^{2}}
    $$
+ **Gaussian 脉冲** $f(t) = E \e^{-(t/\tau)^{2}}$
    $$
    F(\omega) = \dint_{-\infty}^{\infty} E \e^{-(t/\tau)^{2}} \e^{-\I\omega t} \dif t = E\tau \sqrt{\pi} \e^{-(\omega \tau/2)^{2}}
    $$
Gaussian 脉冲的 Fourier 变换也是 Gaussian 函数，且**宽度与时域宽度成反比**，峰值与时域宽度成正比。

### 奇异信号的 Fourier 变换

+ **冲激函数 $\delta(t)$**
    $$
    \mathscr{F} \{ \delta(t) \} = \dint_{-\infty}^{\infty} \delta(t) \e^{-\I \omega t} \dif t = \e^{0} = 1
    $$
    冲激函数包含幅度相等的**所有频率分量**；由 Fourie 变换的对称性可得
    $$
    \mathscr{F}^{-1} \{ \delta(\omega) \} = \dfrac{1}{2\pi} \quad\Longrightarrow \quad
    \mathscr{F} \{ 1 \} = 2\pi \delta(\omega)
    $$
    直流信号的所有能量都集中在频率为零的地方。

+ **冲激偶函数 $\delta'(t)$**
    $$
    \delta'(t) = \dfrac{\dif}{\dif t} \left( \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} \e^{\I \omega t} \dif t \right)
    = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} \I\omega \e^{\I \omega t} \dif t 
    \quad \Longrightarrow \quad
    \mathscr{F}\{ \delta'(t) \} = \I\omega
    $$

+ **符号函数 $\mathrm{sgn}(t)$**
    由于符号函数不满足绝对可积条件，考虑辅助函数 $f(t) = \mathrm{sgn}(t) \e^{-a|t|}$，
    $$
    F(\omega) = \dint_{-\infty}^{0} -\e^{at} \e^{-\I\omega t} \dif t + \dint_{0}^{\infty} \e^{-at} \e^{-\I\omega t} \dif t = - \dfrac{2\I\omega}{a^{2} + \omega^{2}}
    $$
    则
    $$
    \mathscr{F}\{ \mathrm{sgn}(t) \} = \lim\limits_{ a \to 0 } F(\omega) = \dfrac{2}{\I\omega}
    $$

+ **阶跃函数 $u(t)$**
    $$
    \mathscr{F} \{ u(t) \} = \dfrac{1}{2} \mathscr{F} \{ 1 \} + \dfrac{1}{2} \mathscr{F} \{ \mathrm{sgn}(t) \} = \pi\delta(\omega) + \dfrac{1}{\I\omega}
    $$
    阶跃信号中有直流分量，因而其频谱在 $ω = 0$ 处有一个冲激函数；阶跃信号中有跳变，因而它还含有其他频率分量。

### 周期信号的 Fourier 变换

**复指数函数**的 Fourier 变换可基于 $\mathscr{F} \{ 1 \} = 2\pi \delta(\omega)$ 由[[#$ omega$ 域平移|频移特性]]直接得到：
$$
\mathscr{F} \{ \e^{\I\omega_{0} t} \} = 2\pi \delta(\omega - \omega_{0})
$$
于是由[[#线性性（叠加性、齐次性）]]可得
$$
\begin{align}
&\mathscr{F} \left\{ \cos(\omega_{1}t) \right\} = \mathscr{F} \left\{ \dfrac{\e^{\I\omega_{1}t} + \e^{-\I\omega_{1}t}}{2} \right\} = \pi \big( \delta(\omega + \omega_{1}) + \delta(\omega - \omega_{1}) \big) \\
&\mathscr{F} \left\{ \sin(\omega_{1}t) \right\} = \mathscr{F} \left\{ \dfrac{\e^{\I\omega_{1}t} - \e^{-\I\omega_{1}t}}{2\I} \right\} = \I\pi \big( \delta(\omega + \omega_{1}) - \delta(\omega - \omega_{1}) \big)
\end{align}
$$

一般地，周期为 $T_{1}$ 的周期信号 $f(t)$ 可展成 [[Fourier 级数 (FS)]]
$$
f(t) = \sum\limits_{n=-\infty}^{\infty} F(n\omega_{1}) \e^{\I n\omega_{1} t}, \qquad \omega_{1} = \dfrac{2\pi}{T_{1}}
$$
其中频谱系数
$$
F(n\omega_{1}) = \dfrac{1}{T_{1}} \dint_{t_{0}}^{t_{0}+T_{1}} f(t) \e^{-\I n\omega_{1} t} \dif t
$$
则其 **Fourier 变换**即为
$$
\mathscr{F} \{ f(t) \} = \mathscr{F} \left\{ \sum\limits_{n=-\infty}^{\infty} F(n\omega_{1}) \e^{\I n\omega_{1} t} \right\} = 2\pi \sum\limits_{n=-\infty}^{\infty} F(n\omega_{1}) \delta(\omega - n\omega_{1})
$$

另一方面，若采周期信号的**主值区间**为 $f_{0}(t) = f(t) \big(u(t) - u(t - T_{1})\big)$，则上面频谱系数可写为
$$
F(n\omega_{1}) = \dfrac{1}{T_{1}} \dint_{0}^{T_{1}} f_{0}(t) \e^{-\I n\omega_{1} t} \dif t = \dfrac{1}{T_{1}} \mathscr{F} \{ f_{0}(t) \} \Big|_{\omega=n\omega_{1}}
$$
整个周期信号的 Fourier 变换可写为
$$
\mathscr{F} \{ f(t) \} = \dfrac{2\pi}{T_{1}} \sum\limits_{n=-\infty}^{\infty} \mathscr{F} \{ f_{0}(t) \} \Big|_{\omega=n\omega_{1}} \delta(\omega - n\omega_{1}) = \omega_{1} \sum\limits_{n=-\infty}^{\infty} \mathscr{F}\{ f_{0}(t) \} \delta(\omega - n\omega_{1})
$$