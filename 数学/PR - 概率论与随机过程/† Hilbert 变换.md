## Hilbert 变换的引入

考虑一个线性滤波器
$$
H(\omega) = -\J \sgn (\omega) = \begin{cases}
-\J, & \omega > 0, \\
0, & \omega = 0, \\
\J, & \omega < 0
\end{cases}
$$
其时域冲激响应为
$$
h(t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} H(\omega) e^{\J \omega t} \dif \omega = \frac{1}{\pi t}
$$
该滤波器称为 **Hilbert 变换 (Hilbert transform)**，记作 $\mathscr{H}_{\mathrm{h}} \left\{ \cdot \right\}$。

### Hilbert 变换对复指数信号的作用

考虑输入信号为**复指数信号 $x(t) = \e^{\J \omega_{0} t}$**，则其频谱为
$$
\hat{x}(\omega) = 2\pi \delta(\omega - \omega_{0})
$$
不妨假设 $\omega_{0} > 0$，经过 Hilbert 变换后，输出频谱为
$$
\hat{y}(\omega) = H(\omega) \hat{x}(\omega) = -\J \sgn(\omega) \cdot 2\pi \delta(\omega - \omega_{0}) = -\J \cdot 2\pi \delta(\omega - \omega_{0})
$$
因此时域输出信号为
$$
y(t) = \mathscr{H}_{\mathrm{h}} \{ x(t) \} = -\J \e^{\J \omega_{0} t} = \e^{\J \left(\omega_{0} t - \tfrac{\pi}{2}\right)}
$$
若输入信号为**负频率**成分 $x(t) = \e^{-\J \omega_{0} t}$，则类似地可得输出信号为
$$
y(t) = \mathscr{H}_{\mathrm{h}} \{ x(t) \} = \J \e^{-\J \omega_{0} t} = \e^{-\J \left(\omega_{0} t - \tfrac{\pi}{2}\right)}
$$
即 Hilbert 变换将正频率成分的相位延迟了 $\cfrac{\pi}{2}$。

因此，
+ 对余弦输入 $\cos (\omega_{0} t) = \cfrac{1}{2} \left( \e^{\J \omega_{0} t} + \e^{-\J \omega_{0} t} \right)$，Hilbert 变换的输出为
$$
\mathscr{H}_{\mathrm{h}} \{ \cos (\omega_{0} t) \} = \frac{1}{2} \left( -\J \e^{\J \omega_{0} t} + \J \e^{-\J \omega_{0} t} \right) = \sin (\omega_{0} t)
$$
+ 对正弦输入 $\sin (\omega_{0} t) = \cfrac{1}{2\J} \left( \e^{\J \omega_{0} t} - \e^{-\J \omega_{0} t} \right)$，Hilbert 变换的输出为
$$
\mathscr{H}_{\mathrm{h}} \{ \sin (\omega_{0} t) \} = \frac{1}{2\J} \left( -\J \e^{\J \omega_{0} t} - \J \e^{-\J \omega_{0} t} \right) = -\cos (\omega_{0} t)
$$

即 Hilbert 变换**将余弦信号变为正弦信号，将正弦信号变为负余弦信号**，相当于将信号相位延迟 $\cfrac{\pi}{2}$。

### Hilbert 变换对带限调制信号的作用

设输入信号 $x(t)$ 为**带限信号**，其频谱 $\hat{x}(\omega)$ 满足
$$
\hat{x}(\omega) = 0, \qquad |\omega| > \omega_{\mathrm{c}}
$$
其可乘以载波 $\cos(\omega_{0}t)$（$\omega_{0} > \omega_{\mathrm{c}}$）进行调制，频谱迁移为 $\cfrac{1}{2} \left( \hat{x}(\omega - \omega_{0}) + \hat{x}(\omega + \omega_{0}) \right)$。对该调制信号进行 Hilbert 变换，输出频谱为
$$
H(\omega) \cdot \dfrac{1}{2} \left( \hat{x}(\omega - \omega_{0}) + \hat{x}(\omega + \omega_{0}) \right)
= \dfrac{1}{2} \left( -\J \hat{x}(\omega - \omega_{0}) + \J \hat{x}(\omega + \omega_{0}) \right)
$$
因此时域输出信号为
$$
\begin{align}
\mathscr{H}_{\mathrm{h}} \{ x(t) \cos(\omega_{0} t) \} &= \mathscr{F}^{-1} \left\{ \dfrac{1}{2} \left( -\J \hat{x}(\omega - \omega_{0}) + \J \hat{x}(\omega + \omega_{0}) \right) \right\} \\
&= \dfrac{1}{2} \left( -\J x(t) \e^{\J \omega_{0} t} + \J x(t) \e^{-\J \omega_{0} t} \right) \\
&= x(t) \cdot \dfrac{1}{2} (-\J) \left( \e^{\J \omega_{0} t} - \e^{-\J \omega_{0} t} \right) = x(t) \sin(\omega_{0} t)
\end{align}
$$
即 Hilbert 变换将调制信号 $x(t) \cos(\omega_{0} t)$ 转换为 $x(t) \sin(\omega_{0} t)$，相当于将载波信号相位延迟 $\cfrac{\pi}{2}$。

同理，对调制信号 $x(t) \sin(\omega_{0} t)$，Hilbert 变换的输出为
$$
\mathscr{H}_{\mathrm{h}} \{ x(t) \sin(\omega_{0} t) \} = - x(t) \cos(\omega_{0} t)
$$

## 随机过程的 Hilbert 变换

设随机过程 $X(t)$ 有分解
$$
X(t) = \dint_{-\infty}^{\infty} \e^{\J \omega t} \dif F_{X}(\omega)
$$
其中 $F_{X}(\omega)$ 是随机过程 $X(t)$ 的**频率分量随机变量列 (frequency component random variable series)**。 则 Hilbert 变换后的随机过程为
$$
\check{X} (t) = \mathscr{H}_{\mathrm{h}} \{ X(t) \} = \dint_{-\infty}^{\infty} \e^{\J \omega t} \cdot \left( -\J \sgn(\omega) \right) \dif F_{X}(\omega)
$$

### Hilbert 变换对宽平稳随机过程的作用

设随机过程 $X(t)$ 是[[随机过程的平稳性]]，其均值为 $\mu_{X} = \mathbb{E}[X(t)]$，自相关函数为 $R_{X}(\tau) = \mathbb{E}[X(t) X(t+\tau)]$。则 Hilbert 变换后的随机过程 **$\check{X}(t)$ 也是宽平稳随机过程**，有
$$
\begin{align}
R_{\check{X}}(\tau) &= \mathbb{E} \left[ \check{X}(t+\tau) \overline{\check{X}(t)} \right]  \\
&= \mathbb{E} \left[ \dint_{-\infty}^{\infty} \e^{\J \omega (t+\tau)}  \left( -\J \sgn(\omega) \right) \dif F_{X}(\omega) \cdot \dint_{-\infty}^{\infty} \e^{-\J \omega' t} \left( \J \sgn(\omega') \right) \overline{\dif F_{X}(\omega')} \right] \\
&= \dint_{-\infty}^{\infty} \dint_{-\infty}^{\infty} \e^{\J \omega \tau + \J (\omega - \omega') t} \sgn(\omega) \sgn(\omega') \cdot \mathbb{E} \left[ \dif F_{X}(\omega) \overline{\dif F_{X}(\omega')} \right]  \\
&= \dint_{-\infty}^{\infty} \dint_{-\infty}^{\infty} \e^{\J \omega \tau + \J (\omega - \omega') t} \sgn(\omega) \sgn(\omega') \cdot \dfrac{1}{2\pi} \delta(\omega - \omega') S_{X}(\omega) \dif \omega \dif \omega' \\
&= \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} \e^{\J \omega \tau} \sgn^{2}(\omega) S_{X}(\omega) \dif \omega = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} \e^{\J \omega \tau} S_{X}(\omega) \dif \omega = R_{X}(\tau)
\end{align}
$$
即 Hilbert 变换**不改变宽平稳随机过程的自相关函数**。

类似地，我们得到
$$
\begin{align}
R_{\check{X} X} (\tau) &= \mathbb{E} \left[ \check{X}(t+\tau) \overline{X(t)} \right]  = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} \e^{\J \omega \tau} \left( -\J \sgn(\omega) \right) S_{X}(\omega) \dif \omega \\
R_{X \check{X}} (\tau) &= \mathbb{E} \left[ X(t+\tau) \overline{\check{X}(t)} \right]  = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} \e^{\J \omega \tau} \left( \J \sgn(\omega) \right) S_{X}(\omega) \dif \omega
\end{align}
$$

