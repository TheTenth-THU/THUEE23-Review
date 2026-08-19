在实际通信系统中，信道通常受到各种噪声的影响，其中最常见和重要的一种噪声类型是**加性白 Gauss 噪声 (Additive White Gaussian Noise, AWGN)**。AWGN 噪声具有以下几个特点：
+ **加性 (additive)**，即噪声直接叠加在信号上，接收信号为发送信号与噪声的和。
+ **白 (white)**，即噪声在整个频谱上均匀分布，具有恒定的功率谱密度 $S_{Z}(f) = \cfrac{n_{0}}{2}$。
+ **Gaussian**，即噪声服从 Gauss 分布，具有均值为零的正态分布特性。

## 离散时间 AWGN

### 离散时间 AWGN 信源

一个离散时间 AWGN 信源可以表示为
$$
Z_{i} \sim \mathcal{N}(0, \sigma^{2}), \quad i = 1, 2, 3, \cdots
$$
其中 $\sigma^{2} = \dfrac{n_{0}}{2}$。该信源的每个样本 $Z_{i}$ **独立同分布**，服从均值为 0、方差为 $\sigma^{2}$ 的 Gauss 分布，因此可只考虑单个样本 $Z$ 的性质。

对 $Z \sim \mathcal{N}(\mu, \sigma^{2})$，有 $p_{Z}(z) = \dfrac{1}{\sqrt{2 \pi \sigma^{2}}} \exp \left( - \dfrac{(z - \mu)^{2}}{2 \sigma^{2}} \right)$，因此其**微分熵**为
$$
\begin{align}
h(Z) &= - \dint_{-\infty}^{+\infty} p_{Z}(z) \log p_{Z}(z) \dif z \\
&= - \dint_{-\infty}^{+\infty} p_{Z}(z) \log \left( \dfrac{1}{\sqrt{2 \pi \sigma^{2}}} \exp \left( - \dfrac{(z - \mu)^{2}}{2 \sigma^{2}} \right) \right) \dif z \\
&= - \dint_{-\infty}^{+\infty} p_{Z}(z) \left( - \dfrac{(z - \mu)^{2}}{2 \sigma^{2}} \log \e - \log \sqrt{2 \pi \sigma^{2}} \right) \dif z \\
&= \dfrac{\log \e}{2 \sigma^{2}} \dint_{-\infty}^{+\infty} (z - \mu)^{2} p_{Z}(z) \dif z + \log \sqrt{2 \pi \sigma^{2}} \dint_{-\infty}^{+\infty} p_{Z}(z) \dif z \\
&= \dfrac{\log \e}{2 \sigma^{2}} \mathbb{E}[(Z - \mu)^{2}] + \log \sqrt{2 \pi \sigma^{2}} \\
&= \dfrac{\log \e}{2 \sigma^{2}} \left( \mathbb{E}^{2}\left[ (Z - \mu) \right] + \mathrm{Var}\left[ (Z - \mu) \right]  \right) + \log \sqrt{2 \pi \sigma^{2}} \\
&= \dfrac{\log \e}{2 \sigma^{2}} \cdot \sigma^{2} + \log \sqrt{2 \pi \sigma^{2}} = \mark{ \log \sqrt{2 \pi \e \sigma^{2}} }
\end{align}
$$

### 离散时间 AWGN 信道

离散时间 AWGN 信道即 [[电平信道#^AWGNDianpingXindao|AWGN 电平信道]]，其噪声源是离散时间 AWGN 信源 $z \sim \mathscr{N}(0, \sigma^{2})$。信道输入 $x$ 和输出 $y$ 之间有条件概率关系
$$
p(y \mid x) = \dfrac{1}{\sqrt{2 \pi \sigma^{2}}} \exp \left( - \dfrac{(y - x)^{2}}{2 \sigma^{2}} \right)
$$
因此，在给定 $x$ 下输出 $y$ 向单侧偏移 $A$ 以上的概率为
$$
\begin{align}
\Pr \left\{ y < x - A \mid x \right\} &= \dint_{-\infty}^{x - A} p(y \mid x) \dif y 
= \dint_{-\infty}^{-A} \dfrac{1}{\sqrt{2 \pi \sigma^{2}}} \e^{ - \tfrac{z^{2}}{2 \sigma^{2}} } \dif z \\
&= \int_{A}^{+\infty} \dfrac{1}{\sqrt{2 \pi \sigma^{2}}} \e^{-\tfrac{z^{2}}{2 \sigma^{2}}} \dif z 
= \dint_{A/\sigma}^{+\infty} \dfrac{1}{\sqrt{2 \pi}} \e^{-\tfrac{z^{2}}{2}} \dif z  \\
&= Q\left( \dfrac{A}{\sigma} \right) \\
\Pr \left\{ y > x + A \mid x \right\} &= \dint_{x + A}^{+\infty} p(y \mid x) \dif y
= \dint_{A}^{+\infty} \dfrac{1}{\sqrt{2 \pi \sigma^{2}}} \e^{ - \tfrac{z^{2}}{2 \sigma^{2}} } \dif z  \\
&= Q\left( \dfrac{A}{\sigma} \right)
\end{align}
$$
这里 $Q(x)$ 是 **Q 函数 (Q-function)**，定义为
$$
Q(x) = \dint_{x}^{+\infty} \dfrac{1}{\sqrt{2 \pi}} \e^{-\tfrac{z^{2}}{2}} \dif z
$$
在 CASIO fx-991CN X 计算器中，可以通过「统计」页面「单变量统计计算」中的「`正态分布`」>「`R(`」选项计算 $Q(x)$。

## 连续时间 AWGN

### 连续时间 AWGN 信源

一个连续时间 AWGN 信源 $z(t)$ 满足
1. 对任意时刻 $t$，$z(t)$ 服从均值为 0 的 Gauss 分布；
2. 对任意时刻序列 $t_{1}, t_{2}, \cdots, t_{n}$，随机变量组 $\{ z(t_{1}), z(t_{2}), \cdots, z(t_{n}) \}$ 服从均值为 $\v{0}$ 的 $n$ 元 Gauss 分布；
3. **功率谱密度函数 $S_{z}(f) \equiv \cfrac{n_{0}}{2}$**，其中 $n_{0}$ 为常数。

即，$z(t)$ 是一个 [[数学/PR - 概率论与随机过程/Gauss 过程|Gauss过程]]，其自相关函数为
$$
R_{z}(\tau) = \mathbb{E}\left[ z(t) z(t + \tau) \right] = \dint_{-\infty}^{+\infty} S_{z}(f) \e^{j 2 \pi f \tau} \dif f = \dint_{-\infty}^{+\infty} \dfrac{n_{0}}{2} \e^{j 2 \pi f \tau} \dif f = \dfrac{n_{0}}{2} \delta(\tau)
$$
任意时刻其方差都为 $\mathbb{E}\left[ z^{2}(t) \right] = R_{z}(0) = +\infty$。

### 连续时间 AWGN 信道

连续时间 AWGN 信道即 [[波形信道#^AWGNBoXingXindao|AWGN 波形信道]]，其噪声源是连续时间 AWGN 信源 $z(t)$。信道输入 $x(t)$ 和输出 $y(t)$ 之间满足
$$
y(t) = x(t) + z(t)
$$

其化归为[[波形信道#标准等价电平信道|标准等价电平信道]]的过程中，将对 $z(t)$ 做线性处理 $z = \dint_{-\infty}^{\infty} z(t) g(t) \dif t$，所得 $z$ 的方差为
$$
\begin{align}
\mathbb{E}\left[ z^{2} \right] &= \mathbb{E} \left[ \left( \dint_{-\infty}^{+\infty} z(t) g(t) \dif t \right)^{2} \right] 
= \dint_{-\infty}^{+\infty} \dint_{-\infty}^{+\infty} g(t) g(s) \mathbb{E}\left[ z(t) z(s) \right] \dif t \dif s \\
&= \dint_{-\infty}^{+\infty} \dint_{-\infty}^{+\infty} g(t) g(s) R_{z}(t - s) \dif t \dif s \\
&= \dint_{-\infty}^{+\infty} \dint_{-\infty}^{+\infty} g(t) g(s) \cdot \dfrac{n_{0}}{2} \delta(t - s) \dif t \dif s \\
&= \dint_{-\infty}^{+\infty} g^{2}(t) \cdot \dfrac{n_{0}}{2} \dif t = \dfrac{n_{0}}{2} \dint_{-\infty}^{+\infty} g^{2}(t) \dif t
\end{align}
$$
即 $z \sim \mathscr{N}\left( 0, \cfrac{n_{0}}{2} \dint_{-\infty}^{\infty} g^{2}(t) \dif t \right)$。当 $g(t)$ 能量归一化时，$z \sim \mathscr{N}\left( 0, \cfrac{n_{0}}{2} \right)$。
