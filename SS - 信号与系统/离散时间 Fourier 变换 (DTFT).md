## DTFT 及其逆变换

### 序列 DTFT 的引入

**离散时间 Fourier 变换 (DTFT)** 用于研究离散系统频率响应特性。

> [!definition] 离散时间 Fourier 变换 (DTFT)
> 离散时间信号 $x(n)$ 的**离散时间 Fourier 变换**定义为
> $$ 
> x(n) \xrightarrow{\mathrm{DTFT}} X(\omega) = \sum\limits_{n=-\infty}^{\infty} x(n) \e^{-\I n \omega} 
> $$

#### 由抽样信号的 Fourier 变换引入

对连续时间信号 $x(t)$ 以 $T$ 为周期进行**冲激抽样**，得到抽样信号 
$$
x_{\mathrm{s}}(t) = x(t) \delta_{T}(t) = \sum\limits_{n=-\infty}^{\infty} x(nT) \delta(t - nT)
$$
做 Fourier 变换，得到
$$
\mathcal{F}\{x_{\mathrm{s}}(t)\} = \sum\limits_{n=-\infty}^{\infty} x(nT) \e^{-\I n \omega T}
$$
取 $T=1$，即**转入离散时间域**，得到
$$
X(\e^{-\I \omega}) = \mathcal{F}\{ x(n) \} = \sum\limits_{n=-\infty}^{\infty} x(n) \e^{-\I n \omega}
$$

#### 由 $z$ 变换引入

$x(n)$ 的 $z$ 变换为
$$
X(z) = \sum\limits_{n=-\infty}^{\infty} x(n) z^{-n}
$$
令 $z = \e^{-\I \omega}$，即**在单位圆上做 $z$ 变换**，得到
$$
X(z) \Big|_{|z|=1} = X(\e^{\I\omega}) = \sum\limits_{n=-\infty}^{\infty} x(n) \e^{-\I n \omega}
$$

### DTFT 逆变换

> [!definition] DTFT 逆变换
> 离散时间 Fourier 变换的**逆变换**为
> $$ 
> x(n) = \dfrac{1}{2\pi \I} \displaystyle\oint_{|z|=1} X(z) z^{n-1} \dif z = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X(\e^{\I\omega}) \e^{\I n \omega} \dif \omega 
> $$

