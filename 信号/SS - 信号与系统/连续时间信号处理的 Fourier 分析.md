## 传输与滤波

### 无失真传输

#### 线性系统无失真传输条件

**无失真传输**期望响应 $r(t)$ 与激励 $e(t)$ 之间**形状相同**，而**幅度可改变、延时可增加**，即
$$
r(t) = K e(t-t_{0})
$$
取 [[Fourier 变换 (FT)]]，得到
$$
R(\I\omega) = K E(\I\omega) \e^{-\I \omega t_{0}} = H(\I\omega) E(\I\omega)
$$
所以无失真传输系统一定表示为
$$
H(\I\omega) = K \e^{-\I \omega t_{0}}, \quad \text{i.e.} \quad \begin{cases}
|H(\I\omega)| = K, \\
\varphi (\omega) = -\omega t_{0}
\end{cases}
$$

#### 传输系统的线性相移特性

对任意实信号 $e(t)$，有分解
$$
e(t) = \sum\limits_{i} e_{i} (t) = \sum\limits_{i} E(\omega_{i}) \sin(\omega_{i} t)
$$
经过相移系统后得到
$$
\begin{align}
r(t) &= \sum\limits_{i} E(\omega_{i}) \sin(\omega_{i} t + \varphi(\omega_{i})) = \sum\limits_{i} E(\omega_{i}) \sin\left( \omega_{i} \left( t + \dfrac{\varphi(\omega_{i})}{\omega i} \right) \right) \\
&= \sum\limits_{i} e_{i}\left( t - \left( - \dfrac{\varphi(\omega_{i})}{\omega_{i}} \right) \right)
\end{align}
$$
**延时统一**要求 $- \dfrac{\varphi(\omega_{i})}{\omega_{i}}$ 为一常数 $t_{0}$；或者要求**群时延**
$$
\lim\limits_{ \omega_i \to \omega_{j} } \left( - \dfrac{\varphi(\omega_{i}) - \varphi(\omega_{j})}{\omega_{i} - \omega_{j}} \right) = - \dfrac{\dif \varphi(\omega)}{\dif \omega} =: \tau(\omega)
$$
为一常数。

### 理想低通滤波器

#### 理想低通滤波器的频率响应

截止于 $\omega_{\mathrm{c}}$ 的理想低通滤波器应**无失真地**传输低于 $\omega_{\mathrm{c}}$ 的信号，同时**完全阻断**高于 $\omega_{\mathrm{c}}$ 的信号，即**频率响应**为
$$
|H(\I\omega)| = \begin{cases}
1, & |\omega| < \omega_{\mathrm{c}}, \\
0, & |\omega| \geq \omega_{\mathrm{c}},
\end{cases}
\qquad
\varphi(\omega) = -\omega t_{0}
$$
求 Fourier 逆变换得到
$$
h(t) = \mathscr{F}^{-1} \{ H(\I\omega) \} = \dfrac{\omega_{\mathrm{c}}}{\pi} \mathrm{Sa} \left( \omega_{\mathrm{c}} (t-t_{0}) \right) 
$$
显然这是一个**非因果系统**，因此**不可实现**。

#### 理想低通滤波器的阶跃响应

在频域，理想低通滤波器的阶跃响应为
$$
\begin{align}
G(\I\omega) &= H(\I\omega) \cdot \mathscr{F}\{ u(t) \} = H(\I\omega) \cdot \left( \pi\delta(\omega) + \dfrac{1}{\I\omega} \right) \\
&= \begin{cases} 
\left( \pi\delta(\omega) + \dfrac{1}{\I\omega} \right) \e^{-\I \omega t_{0}}, & |\omega| < \omega_{\mathrm{c}}, \\
0, & |\omega| \geq \omega_{\mathrm{c}} 
\end{cases}
\end{align}
$$
因此其阶跃响应为
$$
g(t) = \mathscr{F}^{-1} \{ G(\I\omega) \} = \dfrac{1}{2} + \dfrac{1}{\pi} \mathrm{Si} \left( \omega_{\mathrm{c}} (t-t_{0}) \right)
$$
其中 $\mathrm{Si}(x) = \dint_{0}^{x} \mathrm{Sa}(\chi) \dif \chi$ 为**正弦积分**，没有解析表达式。

![[正弦积分.png]]

因此阶跃响应存在**上升时间**，为 $t_{\mathrm{r}} = 2 \cdot \dfrac{\pi}{\omega_{\mathrm{c}}} = \dfrac{1}{B}$，其中 $B = \dfrac{\omega_{\mathrm{c}}}{2\pi}$ 表示系统**带宽**。对理想低通滤波器，阶跃响应的**上升时间与带宽呈反比**。**带宽越宽，高频分量损失越小**，上升时间越短。

![[理想低通滤波器的阶跃响应.png]]

##### 矩形脉冲响应

矩形脉冲可表示为阶跃的组合，即
$$
e(t) = u\left( t+\dfrac{\tau}{2} \right) - u\left( t-\dfrac{\tau}{2} \right) 
$$
则**响应**相应为**阶跃响应的差**
$$
r(t) = \dfrac{1}{\pi} \Big( \mathrm{Si} \big( \omega_{\mathrm{c}} (t+\tau/2 - t_{0}) \big) - \mathrm{Si} \big( \omega_{\mathrm{c}} (t-\tau/2 - t_{0}) \big) \Big)
$$

![[矩形脉冲通过不同带宽的理想低通滤波器.png]]

##### Gibbs 现象

**Gibbs 现象**指理想低通滤波器阶跃响应的上升沿处存在**振铃**，即尽管随着**带宽增大**，上升时间缩短，但跳变点处的**过冲幅度不变**，保持为
$$
g(t) \Big|_{\mathrm{max}} = \dfrac{1}{2} + \dfrac{\mathrm{Si}(\pi)}{\pi} \approx 1.0895
$$
约为**阶跃高度的 9\%**。

Gibbs 现象来自理想低通滤波器频域上的**矩形窗**。选择其他形式的窗，如升余弦窗、Hanning、Hamming、Blackman、Kaiser 等，可使开窗后波形无过冲。

## 调制与解调

### 抑制载波调幅 (SC-AM)

#### 调制过程

时域上，
$$
f(t) = g(t) \cos(\omega_{0}t)
$$
频域上，
$$
\begin{align}
F(\omega) &= \dfrac{1}{2\pi} G(\omega) * \left( \pi\delta(\omega + \omega_{0}) + \pi\delta(\omega - \omega_{0}) \right) \\
&= \dfrac{1}{2} \left( G(\omega + \omega_{0}) + G(\omega - \omega_{0}) \right) 
\end{align}
$$

#### 解调过程

1. 用本地载波乘以调制信号
$$
g_{0}(t) = f(t) \cos(\omega t)
$$
即将频谱搬回原来的位置
$$
\begin{align}
G_{0}(\omega) &= \dfrac{1}{2} \left( F(\omega + \omega_{0}) + F(\omega - \omega_{0}) \right) \\
&= \dfrac{1}{2} G(\omega) + \dfrac{1}{4} \left( G(\omega + 2\omega_{0}) + G(\omega - 2\omega_{0}) \right)
\end{align}
$$

2. 经过低通滤波器，去掉高频部分，取出 $G(\omega)$

![[抑制载波调幅.png]]

SC-AM **不发送载波**，用**同步解调**需要本地载波，用晶体 (或锁相环) 恢复，接收机复杂。

### 调幅 (AM)

#### 调制过程

时域上，在发端加入直流分量，
$$
f(t) = A\left( 1 + kg(t) \right) \cos(\omega_{0}t)
$$
其中 $k = \dfrac{1}{A}$ 称为**调制深度**，$A$ 为载波幅度。

#### 解调过程

根据波形，AM 的包络体现调制信号，可**包络检波解调**。

```tikz
\usepackage[american]{circuitikz}

\begin{document}
\large
\begin{tikzpicture}

\draw[thick] (0,0)  to[open, o-o, v^<=$f(t)$] (0,2)
					to[Do] (2,2)
					to[C, l=$C$] (2,0)
					to[short] (0,0)
			 (2,2)  -- (4,2)
				    to[R, l=$R$] (4,0)
				    to[short] (2,0)
			 (4,2)  to[short] (5,2)
					to[open, o-o, v^=$g_1(t)$] (5,0)
					to[short] (4,0);

\end{tikzpicture}
\end{document}
```


### 单边带 (Single-Sideband，SSB)

#### 调制过程

为节省频带，只发半个边带。

![[单边带.png]]

### 残留边带 (Vestigial-Sideband，VSB)

#### 调制过程

VSB 是 DSB 和 SSB 的折衷，使边带滤波器**在 $\omega_{0}$ 附近渐变**，频带节省了不到一半，但是滤波器更容易实现。

![[残留边带.png]]

为保证合成后仍可恢复，要求边带滤波器在 $\omega_{0}$ 左右斜对称。

### 调频 (FM) 和调相 (PM)

#### 调制过程

**调频**是调制信号改变载波频率，
$$
f(t) = A \cos \left( \omega_{\mathrm{c}}t + \dint_{-\infty}^t g(\tau) \dif \tau \right) 
$$
**调相**是调制信号改变载波相位，
$$
f(t) = A \cos \left( \omega_{\mathrm{c}}t + g(t) \right)
$$
用 $g(t)$ 调频即用 $\dint_{-\infty}^t g(\tau) \dif \tau$ 调相；用 $g(t)$ 调相即用 $g'(t)$ 调频。

#### 解调过程

1. 对已调信号**求导**得到**变频率的 AM** 信号，
2. 用**包络检波**解调。

## 抽样与恢复

### 信号抽样的 Fourier 分析

#### 时域抽样

设以**周期为 $T_{\mathrm{s}}$ 的脉冲串 $p(t)$** 对连续时间信号 $f(t)$ 抽样，得到抽样信号 $f_{\mathrm{s}}(t) = f(t) p(t)$。由于 $p(t)$ 是周期信号，
$$
P(\omega) = \mathscr{F}\{ p(t) \} = 2\pi \sum\limits_{n=-\infty}^{\infty} P_{n} \delta(\omega - n\omega_{\mathrm{s}}), \qquad \omega_{\mathrm{s}} = \dfrac{2\pi}{T_{\mathrm{s}}}
$$
其中 $P_{n} = \dfrac{1}{T_{\mathrm{s}}} \dint_{-T_{\mathrm{s}}/2}^{T_{\mathrm{s}}/2} p(t) \e^{-\I n\omega_{\mathrm{s}} t} \dif t$ 是脉冲串的 Fourier 系数。由卷积定理得到
$$
F_{\mathrm{s}}(\omega) = \dfrac{1}{2\pi} F(\omega) * P(\omega) = \sum\limits_{n=-\infty}^{\infty} P_{n} F(\omega - n\omega_{\mathrm{s}})
$$
这是将连续信号的频谱 $F(\omega)$ **以 $\omega_{\mathrm{s}} = \dfrac{2\pi}{T_{\mathrm{s}}}$ 为周期延拓**，同时在 $n\omega_{\mathrm{s}}$ 处以 $P_{n}$ 加权。

#### 频域抽样

设在频域有**周期为 $\omega_{\mathrm{s}}$ 的冲激序列** $P(\omega) = \sum\limits_{n=-\infty}^{\infty} \delta(\omega - n\omega_{\mathrm{s}})$，则其在时域为
$$
p(t) = \mathscr{F}^{-1} \{ P(\omega) \} = \dfrac{1}{\omega_{\mathrm{s}}} \sum\limits_{n=-\infty}^{\infty} \delta(t - nT_{\mathrm{s}})
$$
时域得到的抽样信号为
$$
f_{\mathrm{s}}(t) = f(t) * p(t) = \dfrac{1}{\omega_{\mathrm{s}}} \sum\limits_{n=-\infty}^{\infty} f(t - nT_{\mathrm{s}}) 
$$
这是将连续信号 $f(t)$ **以 $T_{\mathrm{s}}$ 为周期延拓**。

### 抽样定理

> [!theorem] 时域抽样定理
> 一个频带受限于 $|\omega| \le \omega_{\mathrm{m}}$ 的连续时间信号 $f(t)$，如果以一定周期进行等间隔的抽样，则只要**抽样周期 $T_{\mathrm{s}} \le \dfrac{\pi}{\omega_{\mathrm{m}}}$**，或者说**抽样频率 $\omega_{\mathrm{s}} \ge 2\omega_{\mathrm{m}}$**，原信号就可以用等间隔的抽样值**唯一**地表示。

这个允许的最低抽样率称为 **Nyquist 频率**，最大抽样间隔称为 **Nyquist 抽样间隔**。

> [!theorem] 频域抽样定理
> 一个时间受限于 $|t| \le T_{\mathrm{m}}$ 的连续时间信号 $f(t)$，如果在**频域内**以一定间隔对其频谱 $F(\omega)$ 进行抽样，则只要**抽样间隔 $\omega_{\mathrm{s}} \le \dfrac{\pi}{T_{\mathrm{m}}}$**，即时域延拓的**重复周期 $T_{\mathrm{s}} \ge 2T_{\mathrm{m}}$**，那么抽样后的频谱 $F_{\mathrm{s}}(\omega)$ 就可以**唯一**地表示原信号。


### 典型抽样方式

#### 自然抽样（矩形脉冲抽样）

**[[Fourier 级数 (FS)#周期矩形脉冲信号|周期矩形脉冲信号]]**的 Fourier 级数的系数为
$$
\begin{align}
P_{n} &= \dfrac{1}{T_{\mathrm{s}}} \dint_{-T_{\mathrm{s}}/2}^{T_{\mathrm{s}}/2} E \left(u\left( t+\dfrac{\tau}{2} \right) - u\left( t-\dfrac{\tau}{2} \right) \right) \e^{-\I n\omega_{\mathrm{s}} t} \dif t \\
&= \dfrac{E\tau}{T_{\mathrm{s}}} \mathrm{Sa} \left( \dfrac{n\omega_{\mathrm{s}} \tau}{2} \right) 
\end{align}
$$
代入得到
$$
F_{\mathrm{s}}(\omega) = \dfrac{E\tau}{T_{\mathrm{s}}} \sum\limits_{n=-\infty}^{\infty} \mathrm{Sa} \left( \dfrac{n\omega_{\mathrm{s}} \tau}{2} \right) F\left( \omega - n\omega_{\mathrm{s}} \right)
$$

#### 冲激抽样

##### 抽样过程

用**冲激串 $\delta_{T_{\mathrm{s}}}(t) = \sum\limits_{n=-\infty}^{\infty} \delta(t - nT_{\mathrm{s}})$** 对 $f(t)$ 相乘得到抽样信号 $f_{\mathrm{s}}(t)$，由卷积定理得到
$$
\begin{align}
F_{\mathrm{s}} (\omega) &= \dfrac{1}{2\pi} F(\omega) * \mathscr{F} \{ \delta_{T_{\mathrm{s}}} (t) \} = \dfrac{1}{2\pi} F(\omega) * \omega_{\mathrm{s}} \sum\limits_{n=-\infty}^{\infty} \delta(\omega - n \omega_{\mathrm{s}}) \\
&= \dfrac{1}{T_{\mathrm{s}}} \sum\limits_{n=-\infty}^{\infty} F\left( \omega - n \omega_{\mathrm{s}} \right)
\end{align}
$$
冲激抽样信号的频谱是**原信号频谱的周期延拓**。

##### 恢复过程

取[[#理想低通滤波器]] $H(\omega) = \begin{cases}T_{\mathrm{s}}, & |\omega| \le \omega_{\mathrm{c}} \\ 0, & |\omega| > \omega_{\mathrm{c}} \end{cases}$，冲激响应为
$$
h(t) = T_{\mathrm{s}} \dfrac{\omega_{\mathrm{c}}}{\pi} \mathrm{Sa}(\omega_{\mathrm{c}} t)
$$
则冲激抽样信号的恢复为
$$
\begin{align}
\hat{f}(t) = f_{\mathrm{s}}(t) * h(t) 
&= \sum\limits_{n=-\infty}^{\infty} f(nT_{\mathrm{s}}) \delta(t - nT_{\mathrm{s}}) * T_{\mathrm{s}} \dfrac{\omega_{\mathrm{c}}}{\pi} \mathrm{Sa}(\omega_{\mathrm{c}} t) \\
&= T_{\mathrm{s}} \dfrac{\omega_{\mathrm{c}}}{\pi} \sum\limits_{n=-\infty}^{\infty} f(nT_{\mathrm{s}}) \mathrm{Sa}(\omega_{\mathrm{c}} (t - nT_{\mathrm{s}})) \\
\end{align}
$$
设频谱 $F(\omega)$ 限于 $|\omega| \le \omega_{\mathrm{m}}$，则**只要 $\omega_{\mathrm{m}} < \omega_{\mathrm{c}} < \omega_{\mathrm{s}} - \omega_{\mathrm{m}}$**，即可选出
$$
\hat{F}(\omega) = H(\omega) F_{\mathrm{s}}(\omega) = F(\omega)
$$

#### 零阶抽样保持

##### 抽样过程

用**零阶抽样序列**对 $f(t)$ 抽样得到抽样信号 $f_{\mathrm{s}0}(t)$，即 
$$
\begin{align}
f_{\mathrm{s}0}(t) &= f(t) \cdot \sum\limits_{n=-\infty}^{\infty} \big(u(t - nT_{\mathrm{s}}) - u(t - (n+1)T_{\mathrm{s}})\big) \\
&= \underbrace{ f(t) \cdot \underbrace{ \sum\limits_{n=-\infty}^{\infty} \delta(t - nT_{\mathrm{s}}) }_{ \delta_{T_{\mathrm{s}}}(t) } }_{ f_{\mathrm{s}}(t) } * \underbrace{ \big(u(t) - u(t - T_{\mathrm{s}})\big) }_{ h_{0}(t) }
\end{align}
$$
宽为 $T_{\mathrm{s}}$ 的**矩形脉冲**的 Fourier 变换为
$$
H_{0}(\omega) = T_{\mathrm{s}} \mathrm{Sa}\left( \dfrac{\omega T_{\mathrm{s}}}{2} \right) \e^{-\I \tfrac{\omega T_{\mathrm{s}}}{2}}
$$
则抽样信号的频谱为
$$
F_{\mathrm{s}0}(\omega) = F(\omega) H_{0}(\omega) = \sum\limits_{n=-\infty}^{\infty} F(\omega - n \omega_{\mathrm{s}}) \cdot \mathrm{Sa} \left( \dfrac{\omega T_{\mathrm{s}}}{2} \right) \e^{-\I \tfrac{\omega T_{\mathrm{s}}}{2}}
$$

##### 恢复过程

为复原 $F(\omega)$ 频谱，除了使用低通滤波器取出 $\omega = 0$ 附近的频率分量外，还需要**补偿幅度加权和相位延迟**，即
$$
H_{0\mathrm{r}} (\omega) = \begin{cases}
\dfrac{\e^{\I \tfrac{\omega T_{\mathrm{s}}}{2}}}{\mathrm{Sa} \left( \dfrac{\omega T_{\mathrm{s}}}{2} \right)}, & |\omega| \le \omega_{\mathrm{c}}  \\
0, & |\omega| > \omega_{\mathrm{c}}
\end{cases}
$$
注意相频特性斜率为正，即**超前**而非延迟，完全恢复**非因果、不可实现**。一般通信系统只要求幅频特性满足补偿条件即可。

#### 一阶抽样保持

##### 抽样过程

用**一阶抽样保持序列**对 $f(t)$ 抽样得到抽样信号 $f_{\mathrm{s}1}(t)$，即
$$
\begin{align}
f_{\mathrm{s}1}(t) &= f(t) \cdot \sum\limits_{n=-\infty}^{\infty} \left( 1 - \dfrac{|t - nT_{\mathrm{s}}|}{T_{\mathrm{s}}} \right) \big( u(t - (n-1)T_{\mathrm{s}}) - u(t - (n+1)T_{\mathrm{s}}) \big) \\
&= \underbrace{ f(t) \cdot \underbrace{ \sum\limits_{n=-\infty}^{\infty} \delta(t - nT_{\mathrm{s}}) }_{ \delta_{T_{\mathrm{s}}} (t) } }_{ f_{\mathrm{s}}(t) } * \underbrace{ \left( 1 - \dfrac{|t|}{T_{\mathrm{s}}} \right) \big( u(t-T_{\mathrm{s}}) - u(t + T_{\mathrm{s}}) \big) }_{ h_{1}(t)  }
\end{align}
$$
每个抽样单元是**宽为 $T_{\mathrm{s}}$ 的三角脉冲**，其 Fourier 变换为
$$
H_{1}(\omega) = T_{\mathrm{s}} \mathrm{Sa} ^{2} \left( \dfrac{\omega T_{\mathrm{s}}}{2} \right) 
$$
由于其时域上有**超前**，因此不可实现，但可引入延迟而实现。抽样信号的频谱即为
$$
F_{\mathrm{s}1}(\omega) = F(\omega) H_{1}(\omega) = \sum\limits_{n=-\infty}^{\infty} F(\omega - n \omega_{\mathrm{s}}) \cdot \mathrm{Sa} ^{2} \left( \dfrac{\omega T_{\mathrm{s}}}{2} \right)
$$

##### 恢复过程

为复原 $F(\omega)$ 频谱，除了使用低通滤波器取出 $\omega = 0$ 附近的频率分量外，还需要**补偿幅度加权**，即
$$
H_{1\mathrm{r}}(\omega) = \begin{cases}
\dfrac{1}{\mathrm{Sa} ^{2} \left( \dfrac{\omega T_{\mathrm{s}}}{2} \right)}, & |\omega| \le \omega_{\mathrm{c}}  \\
0, & |\omega| > \omega_{\mathrm{c}}
\end{cases}
$$
