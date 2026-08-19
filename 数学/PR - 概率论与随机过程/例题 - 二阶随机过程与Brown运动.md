## L5 (09/30)

### L5-1

**滑动平均积分器对随机过程的作用。**

设随机过程 $X(t)$ 的功率谱密度为 $S_{X}(\omega)$，考虑其经过一个积分器
$$
Y(t) = \dfrac{1}{T} \dint_{t - T/2}^{t + T/2} X(\tau) \dif \tau
$$

**微分器**和**积分器**都是 **LTI 系统**。微分器的传递函数为 $H(\J\omega) = \J \omega$；积分器的时域冲激响应为 $h(t) = \begin{cases}  \dfrac{1}{T}, & |t| \leq \dfrac{T}{2} \\ 0, & |t| > \dfrac{T}{2} \end{cases}$，其**频率响应**为
$$
H(\J\omega) = \dint_{-\infty}^{+\infty} h(t) \e^{-\J \omega t} \dif t = \dfrac{1}{T} \dint_{-T/2}^{T/2} \e^{-\J \omega t} \dif t = \dfrac{\sin(\omega T/2)}{\omega T/2}
$$
因此，输出随机过程 $Y(t)$ 的功率谱密度为
$$
S_{Y}(\omega) = S_{X}(\omega) \cdot \dfrac{4\sin^{2}(\omega T/2)}{\omega^2 T^2}
$$

### L5-2

**白噪声通过 LTI 系统。**

考虑随机过程 $B(t)$ 满足
$$
\mathbb{E}\left[ B(t) \right] = 0, \qquad R_{B}(t, s) = \min (t, s)
$$
则 $B(t)$ 的增量过程 $Y(t) = \cfrac{\dif}{\dif t} B(t)$ 的相关为
$$
\begin{align}
R_{Y}(t, s) &= \mathbb{E}\left[ Y(t) Y(s) \right] = \mathbb{E}\left[ \dfrac{\dif}{\dif t} B(t) \dfrac{\dif}{\dif s} B_{s} \right] \\
&= \dfrac{\partial^2}{\partial t \partial s} R_{B}(t, s) = \dfrac{\partial^2}{\partial t \partial s} \min(t, s)  \\
&= \dfrac{\partial^2}{\partial t \partial s} \dfrac{t + s - |t - s|}{2} = - \dfrac{1}{2} \dfrac{\partial^2}{\partial t \partial s} |t - s| = \delta(t - s)
\end{align}
$$
$B(t)$ 称为 **Brown 运动 (Brownian motion)**，$Y(t)$ 称为**白噪声 (white noise)**。尽管 Brown 运动不是平稳的，其导数**白噪声是宽平稳过程**。

白噪声的功率谱密度为
$$
S_{Y}(\omega) = \mathscr{F}\{ R_{Y}(t) \} = \mathscr{F}\{\delta(t)\} = 1
$$
考虑白噪声 $Y(t)$ 经过 LTI 系统，系统的频率响应为 $H(\J\omega)$，则输出随机过程 $Z(t)$ 的功率谱密度为
$$
S_{Z}(\omega) = S_{Y}(\omega) \cdot |H(\J\omega)|^{2} = |H(\J\omega)|^{2}
$$
其相关函数为
$$
R_{Z}(\tau) = \mathscr{F}^{-1} \{ S_{Z}(\omega) \} = \mathscr{F}^{-1} \{ |H(\J\omega)|^{2} \} = h(\tau) * h(-\tau)
$$

### L5-3

**脉冲幅度调制。**

我们考察随机信号
$$
X(t) = \sum\limits_{k=-\infty}^{\infty} \alpha_{k} \phi(t - kT)
$$
其中 $\{\alpha_{k}\}$ 是**平稳**的随机序列，满足
$$
\mathbb{E} \left[ \alpha_{k} \right] = 0, \qquad \mathbb{E} \left[ \alpha_{k} \alpha_{k+m} \right] = R_{\alpha}(m)
$$
而 $\phi(t)$ 是一个给定的**基带 (baseband) 脉冲**，其自相关函数为
$$
R_{\phi}(\tau) = \dint_{-\infty}^{+\infty} \phi(t) \phi(t + \tau) \dif t
$$

$X(t)$ 的相关为
$$
\begin{align}
R_{X}(t,s) &= \mathbb{E} \left[ X(t) X(s) \right] = \sum\limits_{n=-\infty}^{\infty} \sum\limits_{m=-\infty}^{\infty} \mathbb{E} \left[ \alpha_{n} \alpha_{m} \right] \phi(t - nT) \phi(s - mT) \\
&= \sum\limits_{n=-\infty}^{\infty} \sum\limits_{m=-\infty}^{\infty} R_{\alpha}(m - n) \phi(t - nT) \phi(s - mT)
\end{align}
$$
显然 $R_{X}(t, s)$ 不能任意平移而不变，但有
$$
\begin{align}
R_{X}(t + T, s + T) &= \sum\limits_{n=-\infty}^{\infty} \sum\limits_{m=-\infty}^{\infty} R_{\alpha}(m - n) \phi(t + T - nT) \phi(s + T - mT) \\
&= \sum\limits_{n'=-\infty}^{\infty} \sum\limits_{m'=-\infty}^{\infty} R_{\alpha}(m' - n') \phi(t - n'T) \phi(s - m'T) = R_{X}(t,s)
\end{align}
$$
因此，$X(t)$ 是**周期为 $T$ 的循环平稳过程**，进而其移位过程是宽平稳过程，相关函数为
$$
\begin{align}
R_{\hat{X}}(t - s) &= \dfrac{1}{T} \dint_{0}^{T} R_{X}(t - s + \theta, \theta) \dif \theta \\
&= \dfrac{1}{T} \dint_{0}^{T} \sum\limits_{n=-\infty}^{\infty} \sum\limits_{m=-\infty}^{\infty} R_{\alpha}(m - n) \phi(t - s + \theta - nT) \phi(\theta - mT) \dif \theta \\
&= \sum\limits_{n=-\infty}^{\infty} \sum\limits_{m=-\infty}^{\infty} R_{\alpha}(m - n) \cdot \dfrac{1}{T} \dint_{0}^{T} \phi(t - s + \theta - nT) \phi(\theta - mT) \dif \theta
\end{align}
$$
做积分变量替换 $\theta' = \theta - mT$，$n' = n - m$，则 $\theta - nT =\theta' + mT - (n' + m)T = \theta' -n'T$，有
$$
\begin{align}
R_{\hat{X}}(t - s) &= \sum\limits_{n'=-\infty}^{\infty} \sum\limits_{m=-\infty}^{\infty} R_{\alpha}(-n') \cdot \dfrac{1}{T} \dint_{-mT}^{(1 - m)T} \phi(t - s + \theta' - n'T) \phi(\theta') \dif \theta' \\
&= \dfrac{1}{T} \sum\limits_{n'=-\infty}^{\infty} R_{\alpha}(n') \dint_{-\infty}^{+\infty} \phi(t - s + \theta' - n'T) \phi(\theta') \dif \theta' \\
&= \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} R_{\alpha}(n) R_{\phi}(t - s - nT)
\end{align}
$$
即
$$
R_{\hat{X}}(\tau) = \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} R_{\alpha}(n) R_{\phi}(\tau - nT)
$$
这样，脉冲幅度调制信号 $X(t)$ 的移位过程的**功率谱**为
$$
\begin{align}
S_{\hat{X}}(\omega) &= \dint_{-\infty}^{+\infty} R_{\hat{X}}(\tau) \exp(-j\omega \tau) \dif \tau  \\
&= \dint_{-\infty}^{+\infty} \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} R_{\alpha}(n) R_{\phi}(\tau - nT) \exp(-j\omega \tau) \dif \tau \\
&= \dint_{-\infty}^{+\infty} \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} R_{\alpha}(n) R_{\phi}(\tau') \exp(-j\omega (\tau + nT)) \dif \tau' \\
&= \dfrac{1}{T} \underbrace{ \sum\limits_{n=-\infty}^{\infty} R_{\alpha}(n) \exp(-j\omega nT) }_{ \mathrm{DTFT}\left\{ R_{\alpha}(n) \right\} } \cdot \underbrace{ \dint_{-\infty}^{+\infty} R_{\phi}(\tau') \exp(-j\omega \tau') \dif \tau' }_{ \mathcal{F} \left\{ R_{\phi}(\tau') \right\}  } \\
&= \dfrac{1}{T} S_{\alpha}\left( \omega T\right) \cdot S_{\phi}(\omega)
\end{align}
$$

## L6 (10/14)

### L6-1

**Brown 运动的微分。**

考虑 **Brown 运动 (Brownian motion)** $B(t)$，满足
+ $B(0) = 0$；
+ $B(t) - B(s) \sim \mathscr{N}(0, \sigma^{2}(t - s))$；
+ $\forall t_{1} < t_{2} \le t_{3} < t_{4}$，$B(t_{4})-B(t_{3}) \perp B(t_{2}) - B(t_{1})$。

其微分
$$
\dif B(t) = B(t + \dif t) - B(t) \sim N(0, \sigma^{2} \dif t)
$$
则
$$
\mathbb{E} \left[ (\dif B(t))^{2} \right] = \sigma^{2} \dif t, \quad\text{i.e.} \quad \dif B(t) \sim \sigma \sqrt{ \dif t }
$$

对任意含 Brown 运动的函数 $f(t, B(t))$，其微分应为
$$
\dif f(t, B(t)) = \dfrac{\partial f}{\partial t} \dif t + \dfrac{\partial f}{\partial B} \dif B + \mark{ \dfrac{1}{2} \dfrac{\partial^{2} f}{\partial B^{2}} (\dif B)^{2} }
$$
这称为随机微积分的 **Ito 引理**。

### L6-2

**使用 Brown 运动模型描述证券价格变化。**

Bachelier (1900) 使用 Brown 运动模型来描述证券价格的变化，其假设证券价格 $S(t)$ 满足
$$
S(t) = S(0) + \mu t + \sigma B(t)
$$
其中 $\mu$ 是证券的期望收益率，$\sigma$ 是证券的波动率，$B(t)$ 取为**标准 Brown 运动**。Samuelson (1965) 进一步认为证券价格应服从**几何 Brown 运动 (geometric Brownian motion)**，即
$$
S(t) = S(0) \exp \left( \left( \mu - \dfrac{1}{2} \sigma^{2} \right) t + \sigma B(t)\right)
$$
微分形式为
$$
\dif S(t) = \mu S(t) \dif t + \sigma S(t) \dif B(t)
$$
其中 $-\cfrac{1}{2}\sigma^{2} t$ 项是为了保证 $\mathbb{E}[S(t)] = S(0) \exp(\mu t)$。这是现代金融工程的基本假设，在此基础上，Black 与 Scholes (1973) 提出了著名的 **Black-Scholes 期权定价公式 (Black-Scholes option pricing formula)**。

考虑**对冲投资组合 (hedged portfolio)** $\varPi(t) = V(t, S(t)) - \delta S(t)$，其中 $V$ 为期权价格，$\delta$ 为对冲比率，表示每持有一份标的于证券 $S$ 的期权 $V$ 都持有 $\delta$ 份证券 $S$ 以对冲风险。假定投资的无风险收益率为 $r$，即
$$
\dif V(t, S(t)) - \delta \dif S(t) = r (V(t, S(t)) - \delta S(t)) \dif t
$$
由 Ito 引理，
$$
\begin{align}
\dif V(t, S(t)) &= \dfrac{\partial V}{\partial t} \dif t + \dfrac{\partial V}{\partial S} \dif S + \dfrac{1}{2} \dfrac{\partial^{2} V}{\partial S^{2}} (\dif S)^{2} \\
&= \dfrac{\partial V}{\partial t} \dif t + \dfrac{\partial V}{\partial S} (\mu S \dif t + \sigma S \dif B) + \dfrac{1}{2} \sigma^{2} S^{2} \dfrac{\partial^{2} V}{\partial S^{2}} \dif t \\
&= \left( \dfrac{\partial V}{\partial t} + \mu S \dfrac{\partial V}{\partial S} + \dfrac{1}{2} \sigma^{2} S^{2} \dfrac{\partial^{2} V}{\partial S^{2}} \right) \dif t + \sigma S \dfrac{\partial V}{\partial S} \dif B
\end{align}
$$
其中 $(\dif S)^{2}$ 中高于 1 阶的 $\dif t$ 项均被忽略。代入对冲投资组合，得
$$
\begin{align}
\dif \varPi &= \left( \dfrac{\partial V}{\partial t} + \mu S \dfrac{\partial V}{\partial S} + \dfrac{1}{2} \sigma^{2} S^{2} \dfrac{\partial^{2} V}{\partial S^{2}} \right) \dif t + \sigma S \dfrac{\partial V}{\partial S} \dif B - \delta (\mu S \dif t + \sigma S \dif B) \\
&= \left( \dfrac{\partial V}{\partial t} + \mu S \dfrac{\partial V}{\partial S} + \dfrac{1}{2} \sigma^{2} S^{2} \dfrac{\partial^{2} V}{\partial S^{2}} - \delta \mu S \right) \dif t + (\sigma S \dfrac{\partial V}{\partial S} - \delta \sigma S) \dif B
\end{align}
$$
为了使 $\varPi$ 无风险，可令 $\delta = \dfrac{\partial V}{\partial S}$，则
$$
\dif \varPi = \left( \dfrac{\partial V}{\partial t} + \dfrac{1}{2} \sigma^{2} S^{2} \dfrac{\partial^{2} V}{\partial S^{2}} \right) \dif t
= r  \left( V - S \dfrac{\partial V}{\partial S} \right) \dif t
$$
消去 $\dif t$，即得 **Black-Scholes 偏微分方程**
$$
\dfrac{\partial V}{\partial t} + \dfrac{1}{2} \sigma^{2} S^{2} \dfrac{\partial^{2} V}{\partial S^{2}} + r S \dfrac{\partial V}{\partial S} - r V = 0
$$

