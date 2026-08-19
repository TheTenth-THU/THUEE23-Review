## FIR 滤波器的实现结构

**FIR (Finite Impulse Response) 滤波器**是指具有**有限长冲激响应**的数字滤波器，冲激响应 $h(t)$ 时宽有限，意味着系统函数 $H(z)$ 是**有限长多项式**
$$
h[n] = \sum\limits_{k=0}^{M} b_{k} \delta[n-k] \quad\implies\quad H(z) = \sum\limits_{k=0}^{M} b_{k} z^{-k}
$$
故 FIR 滤波器的差分方程为
$$
y[n] = \sum\limits_{k=0}^{M} b_{k} x[n-k]
$$
FIR 滤波器**没有反馈**回路，极点在 $z=0$ 处，天然稳定。

### FIR 的直接实现

FIR 滤波器可以直接根据差分方程实现：

![[FIR 的直接实现.png]]

也可以先加权、后延时，即形成**转置结构**：

![[FIR 的转置实现.png]]

### FIR 的级联实现

对 FIR 滤波器，其系统函数 $H(z)$ 可分解为若干低阶多项式的乘积
$$
H(z) = A \prod\limits_{k=1}^{M_{1}} (1 - g_{k} z^{-1}) \prod\limits_{l=1}^{M_{2}} (1 - h_{k}z^{-1}) (1 - h_{k}^{*}z^{-1})
$$
其中，$g_{k} \in \mathbb{R}$，$h_{k} \in \mathbb{C}$。则 FIR 滤波器可以实现为多个**一阶和二阶子滤波器的级联**。

### FIR 的频率取样实现

我们希望直接根据频率响应设计 FIR 滤波器。考虑到
$$
\begin{align}
H(z) &= \sum\limits_{n=0}^{N-1} h[n] z^{-n} = \sum\limits_{n=0}^{N-1} z^{-n} \cdot \dfrac{1}{N} \sum\limits_{k=0}^{N-1} H[k] W_{N}^{-kn} \\
&= \dfrac{1}{N} (1 - z^{-N}) \sum\limits_{k=0}^{N-1} \dfrac{H[k]}{1 - W_{N}^{-k} z^{-1}}
\end{align}
$$
其中，$W_{N}^{k} = \e^{-\J \tfrac{2\pi}{N}k}$，$H[k] = H(z) \big|_{z = W_{N}^{k}}$。因此，可以通过 $N$ 个**频率取样**回路**并联**的方式设计 FIR 滤波器。

![[FIR 的频率取样实现.png]]

这一方案为 FIR 滤波器**引入了极点**且极点在单位圆上，为稳定性考虑，可以稍微缩小极点模值。借助 DFT 的频移性质，亦可使用 $H(\e^{\J (\tfrac{2\pi k}{N} + \alpha)})$ 的值进行频率取样。

## 线性相位 FIR 滤波器

### 线性相位滤波器的实现

对**线性相位** LTI 系统，应有
$$
\begin{align} 
H(\e^{\J \omega}) &= \hat{H}(\e^{\J\omega}) \e^{-\J (\alpha\omega - \beta)} \\
&= \hat{H}(\e^{\J\omega}) \cos(\alpha\omega - \beta) - \J \hat{H}(\e^{\J\omega}) \sin(\alpha\omega - \beta) 
\end{align}
$$
其中 $\hat{H}(\e^{\J\omega})$ 为实函数；由频率响应定义，
$$
H(\e^{\J \omega}) = \sum\limits_{n=-\infty}^{\infty} h[n] \e^{-\J \omega n} = \sum\limits_{n=-\infty}^{\infty} h[n] \cos(\omega n) - \J \sum\limits_{n=-\infty}^{\infty} h[n] \sin(\omega n)
$$
两式**相位相同**，应有
$$
-\dfrac{\sin(\alpha\omega - \beta)}{\cos(\alpha\omega - \beta)} = -\dfrac{\sum\limits_{n=-\infty}^{\infty} h[n] \sin(\omega n)}{\sum\limits_{n=-\infty}^{\infty} h[n] \cos(\omega n)}
$$
即得
$$
\sum\limits_{n=-\infty}^{\infty} h[n] \sin(\omega (n - \alpha) + \beta) = 0
$$
为使上式对任意 $\omega$ 成立，
1. 若 **$\beta = 0$ 或 $\beta = \pi$**，则 $h[n]$ 应**关于 $n = \alpha$ 偶对称**；
2. 若 **$\beta = \pm\cfrac{\pi}{2}$**，则 $h[n]$ 应**关于 $n = \alpha$ 奇对称**。

因此，因果的线性相位滤波器**一定是 FIR 滤波器**，且其冲激响应 $h[n]$ 满足以下四种情况之一：

```tx
| 阶数 $M = 2\alpha$ | 对称性 $\beta$ ||
| ^^ | 偶对称 $\beta = 0, \pi$ | 奇对称 $\beta = \pm \pi/2$ |\
|    | $h[n] = h[M - n]$ | $h[n] = -h[M - n]$ |
| :---- | :---- | :---- |
| 偶数 | **[[#第 I 类线性相位 FIR 滤波器]]** | **[[#第 III 类线性相位 FIR 滤波器]]** |\
|      | 低通、高通、带通 | 带通 |
| 奇数 | **[[#第 II 类线性相位 FIR 滤波器]]** | **[[#第 IV 类线性相位 FIR 滤波器]]** |\
|      | 低通、带通 | 高通、带通 |
```

由于 $h[n] = \pm h[M-n]$ 的对称性，亦有
$$
H(z) = \pm z^{-M} H(z^{-1})
$$
FIR 滤波器没有极点，其**零点分布**受到这一对称性约束，呈现为
+ 若 $z_{0} = r \e^{\J\varphi}$ 是零点，则其关于单位圆的倒数 $z_{0}' = \cfrac{1}{z_0} = \cfrac{1}{r} \e^{\J\varphi}$ 也是零点，二者的共轭复数亦是零点；特别地，
	+ 若实数 $z_{1}$ 是零点，则其关于单位圆的倒数 $z_{1}' = \cfrac{1}{z_1}$ 也是零点；
	+ 若单位圆上的零点 $z_{2} = \e^{\J\varphi}$ 是零点，则其共轭复数 $\e^{-\J\varphi}$ 也是零点。
+ 单位圆与实轴的交点 $\pm 1$ 至少有一个是零点。

#### 第 I 类线性相位 FIR 滤波器

第 I 类线性相位 FIR 滤波器满足 **$M$ 为偶数**且 **$h[n] = h[M-n]$**，频率响应为
$$
\begin{align}
H(\e^{\J\omega}) &= \sum\limits_{n=0}^{M} h[n] \e^{-\J \omega n} = \sum\limits_{n=0}^{\tfrac{M}{2}-1} h[n] \e^{-\J \omega n} + h\left[ \dfrac{M}{2} \right] \e^{-\J \omega \tfrac{M}{2}} + \sum\limits_{n=\tfrac{M}{2}+1}^{M} h[n] \e^{-\J \omega n} \\
&= \e^{-\J \omega \tfrac{M}{2}} \left( h\left[ \dfrac{M}{2} \right] + 2 \sum\limits_{n=0}^{M/2-1} h[n] \cos\left( \omega \left( n - \dfrac{M}{2} \right) \right) \right) \\
&= \e^{-\J \omega \tfrac{M}{2}} \left( h\left[ \dfrac{M}{2} \right] + 2 \sum\limits_{m=1}^{M/2} h\left[ \dfrac{M}{2} - m \right] \cos(\omega m) \right) \\
&= \e^{-\J \omega \tfrac{M}{2}} \sum\limits_{m=0}^{M/2} a_{m} \cos(\omega m) = \e^{-\J \omega \tfrac{M}{2}} \hat{H}(\e^{\J\omega})
\end{align}
$$
其中，$a_{0} = h\left[ \cfrac{M}{2} \right]$，$a_{m} = 2 h\left[ \cfrac{M}{2} - m \right]$，$m = 1, 2, \cdots, \cfrac{M}{2}$。由于 $\hat{H}(\e^{\J\omega})$ 偶对称且关于 $\omega = \pi$ 也偶对称，**第 I 类线性相位 FIR 滤波器可以实现低通、高通、带通滤波器**。

#### 第 II 类线性相位 FIR 滤波器

第 II 类线性相位 FIR 滤波器满足 **$M$ 为奇数**且 **$h[n] = h[M-n]$**，频率响应为
$$
\begin{align}
H(\e^{\J\omega}) &= \sum\limits_{n=0}^{M} h[n] \e^{-\J \omega n} = \sum\limits_{n=0}^{\tfrac{M-1}{2}} h[n] \e^{-\J \omega n} + \sum\limits_{n=\tfrac{M+1}{2}}^{M} h[n] \e^{-\J \omega n} \\
&= \e^{-\J \omega \tfrac{M}{2}} \sum\limits_{m=1}^{(M+1)/2} b_{m} \cos\left( \omega \left( m + \dfrac{1}{2} \right) \right) = \e^{-\J \omega \tfrac{M}{2}} \hat{H}(\e^{\J\omega})
\end{align}
$$
其中，$b_{m} = 2 h\left[ \cfrac{M + 1}{2} - m \right]$，$m = 1, 2, \cdots, \cfrac{M+1}{2}$。由于 $\hat{H}(\e^{\J\omega})$ 偶对称而关于 $\omega = \pi$ 奇对称，**第 II 类线性相位 FIR 滤波器可以实现低通、带通滤波器**。

#### 第 III 类线性相位 FIR 滤波器

第 III 类线性相位 FIR 滤波器满足 **$M$ 为偶数**且 **$h[n] = -h[M-n]$**，频率响应为
$$
\begin{align}
H(\e^{\J\omega}) &= \sum\limits_{n=0}^{M} h[n] \e^{-\J \omega n} = \sum\limits_{n=0}^{\tfrac{M}{2}-1} h[n] \e^{-\J \omega n} + h\left[ \dfrac{M}{2} \right] \e^{-\J \omega \tfrac{M}{2}} + \sum\limits_{n=\tfrac{M}{2}+1}^{M} h[n] \e^{-\J \omega n} \\
&= \e^{\J \left( \tfrac{\pi}{2} - \tfrac{M}{2} \omega \right)} \sum\limits_{m=1}^{M/2} c_{m} \sin(\omega m) = \e^{\J \left( \tfrac{\pi}{2} - \tfrac{M}{2} \omega \right)}  \hat{H}(\e^{\J\omega})
\end{align}
$$
其中，$c[0] = h \left[ \cfrac{M}{2} \right]$，$c_{m} = 2 h\left[ \cfrac{M}{2} - m \right]$，$m = 1, 2, \cdots, \cfrac{M}{2}$。由于 $\hat{H}(\e^{\J\omega})$ 奇对称且关于 $\omega = \pi$ 也奇对称，**第 III 类线性相位 FIR 滤波器只能实现带通滤波器**。

#### 第 IV 类线性相位 FIR 滤波器

第 IV 类线性相位 FIR 滤波器满足 **$M$ 为奇数**且 **$h[n] = -h[M-n]$**，频率响应为
$$
\begin{align}
H(\e^{\J\omega}) &= \sum\limits_{n=0}^{M} h[n] \e^{-\J \omega n} = \sum\limits_{n=0}^{\tfrac{M-1}{2}} h[n] \e^{-\J \omega n} + \sum\limits_{n=\tfrac{M+1}{2}}^{M} h[n] \e^{-\J \omega n} \\
&= \e^{\J \left( \tfrac{\pi}{2} - \tfrac{M}{2} \omega \right)} \sum\limits_{m=1}^{(M+1)/2} d_{m} \sin\left( \omega \left( m - \dfrac{1}{2} \right) \right) = \e^{-\J \omega \tfrac{M}{2}} \hat{H}(\e^{\J\omega})
\end{align}
$$
其中，$d_{m} = 2 h\left[ \cfrac{M+1}{2} - m \right]$，$m = 1, 2, \cdots, \cfrac{M+1}{2}$。由于 $\hat{H}(\e^{\J\omega})$ 奇对称而关于 $\omega = \pi$ 偶对称，**第 IV 类线性相位 FIR 滤波器可以实现高通、带通滤波器**。

### 窗函数法设计线性相位 FIR 滤波器

设我们期望实现频响为 $H_{\mathrm{d}}(\e^{\J\omega})$ 的滤波器，为此设计 $h[n]$，使其 DTFT $H(\e^{\J\omega})$ 尽可能接近 $H_{\mathrm{d}}(\e^{\J\omega})$。在**均方误差**意义下，即希望
$$
h[n] = \arg\limits_{h[n]} \min \| H(\e^{\J\omega}) - H_{\mathrm{d}}(\e^{\J\omega}) \|^{2}
= \arg\limits_{h[n]} \min \dfrac{1}{2\pi} \int_{-\pi}^{\pi} | H(\e^{\J\omega}) - H_{\mathrm{d}}(\e^{\J\omega}) |^{2} \dif \omega
$$
设 $h_{\mathrm{d}}[n] = \mathrm{IDTFT}\left\{ H_{\mathrm{d}}(\e^{\J\omega}) \right\}$，由 Parseval 定理，有
$$
\begin{align} 
\| H(\e^{\J\omega}) - H_{\mathrm{d}}(\e^{\J\omega}) \|^{2} &= \sum\limits_{n=-\infty}^{\infty} | h[n] - h_{\mathrm{d}}[n] |^{2}  \\
&= \sum\limits_{n=0}^{M} | h[n] - h_{\mathrm{d}}[n] |^{2} + \underbrace{ \sum\limits_{n = -\infty}^{-1} | h_{\mathrm{d}}[n] |^{2} + \sum\limits_{n = M+1}^{\infty} | h_{\mathrm{d}}[n] |^{2} }_{ \text{与 $h[n]$ 无关} }
\end{align}
$$
因此，**均方误差**意义下的**最优 $M$ 阶 FIR 滤波器**冲激响应为
$$
h[n] = \begin{cases} h_{\mathrm{d}}[n], & 0 \le n \le M, \\ 0, & \text{otherwise}, \end{cases}
= \mathrm{IDTFT}\left\{ H_{\mathrm{d}}(\e^{\J\omega}) \right\} \cdot w_{\text{rect},M}[n]
$$
即 $\mathrm{IDTFT}\left\{ H_{\mathrm{d}}(\e^{\J\omega}) \right\}$ 加**矩形窗**截断得到。

然而，矩形窗截断会引入 **Gibbs 现象**，导致频率响应出现较大波纹。为减小 Gibbs 现象，可采用其他窗函数 $w[n]$ 截断理想冲激响应，从而设计 FIR 滤波器。

#### 固定窗

固定窗具有**不可调节**的主瓣宽度与阻带衰减特性，常用的固定窗函数及其性能如下表所示：

| 窗函数         | 过渡带宽度 $\Delta \omega$ ($\times \cfrac{2\pi}{N}$) | 最小阻带衰减 $\alpha_{2}$ (dB) |
| :---------- | :----------------------------------------------- | :----------------------- |
| 矩形窗         | 0.89                                             | 21                       |
| 三角窗         | 2.1                                              | 25                       |
| **Hanning** | 3.1                                              | 44                       |
| **Hamming** | 3.3                                              | 53                       |
| Blackman    | 5.5                                              | 74                       |

使用时，只需根据所需的过渡带宽度与阻带衰减选择合适的窗函数，并根据线性相位 FIR 滤波器的特性确定窗长 $M$，然后截断理想冲激响应即可。

#### Kaiser 窗

Kaiser 窗是一种**参数化**窗函数，可通过调整参数 $\beta$ 控制主瓣宽度与旁瓣高度之间的权衡。Kaiser 窗定义为
$$
w_{\text{Kaiser},M;\beta}[n] = \begin{cases}
\dfrac{I_{0}\left( \beta \sqrt{1 - \left( \cfrac{n}{\alpha} - 1 \right)^{2}} \right)}{I_{0}(\beta)}, & 0 \le n \le M, \\
0, & \text{otherwise},
\end{cases}
$$
其中，$\alpha = \dfrac{M}{2}$，$I_{0}(\cdot)$ 是**零阶修正贝塞尔函数 (modified Bessel function of the first kind of order zero)**，定义为
$$
I_{0}(x) = \sum\limits_{m=0}^{\infty} \dfrac{1}{(m!)^{2}} \left( \dfrac{x}{2} \right)^{2m} = 1 + \sum\limits_{k=1}^{\infty} \left( \dfrac{(x/2)^{k}}{k!} \right)^{2} 
$$

Kaiser 窗的参数由经验公式给出，即对于给定的**阻带波纹** $\delta_{2}$（$\alpha_2 = -20 \log_{10} \delta_{2}$ dB）和**过渡带宽度** $\Delta \omega = |\omega_{\mathrm{s}} - \omega_{\mathrm{p}}|$，有
$$
\begin{align} 
&\beta = \begin{cases}
0.1102 (\alpha_2 - 8.7), & \alpha_2 > 50, &\hspace{-1em}\text{（深阻带）} \\
0.5842 (\alpha_2 - 21)^{0.4} + 0.07886 (\alpha_2 - 21), & 21 \le \alpha_2 \le 50, &\hspace{-1em}\text{（中阻带）} \\
0, & \alpha_2 < 21, &\hspace{-1em}\text{（浅阻带）}
\end{cases} \\
&M = \dfrac{\alpha_2 - 8}{2.285 \Delta \omega} 
\end{align}
$$

