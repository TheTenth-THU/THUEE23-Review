# 系统

## 系统模型

一个物理系统可以数学抽象为**系统模型**，表示其对**激励信号** $e(t)$（或一组 $e_{1}(t), e_{2}(t), \cdots$）所输出**响应信号** $r(t)$（或一组 $r_{1}(t), r_{2}(t), \cdots$）的响应关系。

### 系统模型的数学表示

#### 系统数学模型的时域表示

**端口描述**使用**微分方程**或**差分方程**表示系统模型，如
$$
\sum\limits_{i=0}^n C_{i} \dfrac{\dif^{n-i}}{\dif t^{n-i}} r(t) = \sum\limits_{j=0}^m E_{j} \dfrac{\dif^{m-j}}{\dif t^{m-j}} e(t)
$$
![[系统框图-时域端口描述.svg]]

**状态方程描述**使用**状态变量**表示系统模型，如
$$
\dfrac{\dif}{\dif t} \v{s}(t) = A \v{s}(t) + B \v{e}(t), \qquad \v{r}(t) = C \v{s}(t) + D \v{e}(t)
$$
![[系统框图-时域方程描述.svg]]

### 系统模型的方框图表示

方框图用**箭头**表示信号的流动方向，用**方框**表示系统的功能模块，用**线段**表示信号的传递路径。 其中基本的功能模块有：

**相加**：$r(t) = e_{1}(t) + e_{2}(t)$ 表示为
![[系统框图-加法.svg]]

**倍乘**：$r(t) = a e(t)$ 表示为 
![[系统框图-乘法.png]]

**积分**：$r(t) = \dint_{0}^{t} e(\tau) \dif\tau$ 表示为
![[系统框图-积分.png]]

> [!tip]
> 由于**微分**运算在系统可逆性的角度**不[[#可逆系统与不可逆系统|可逆]]**，因此在系统模型中**不考虑微分运算**。 

### 系统模型的信号流图表示

**信号流图**是代数方程的图形化表示，是一种简化系统的方法。信号流图用一些**点**和**支路**构成的图形描述系统，引入若干术语和性质简化图形。
- **点**：表示系统的变量，通常用圆圈表示。在每个点处，对所有进入该点的支路进行代数相加，得到该点的变量值。
	- **源点**：只有输出，没有输入的点，表示系统的激励。
	- **阱点**：只有输入，没有输出的点，表示系统的观测。
- **支路**：表示变量之间的关系，通常用箭头表示。支路上有一个增益值，表示该支路对变量的影响程度。


```tikz
\usepackage{circuitikz}

\begin{document}
\large
\begin{tikzpicture}
	\draw (0,0) node[left] {$X(s)$}
		to[short, o-o, i={$H(s)$}] ++(2,0) node[right] {$Y(s)$};
	\draw (5,0) node[left] {$x(t)$}
		to[short, o-o, i={$h(t)$}] ++(2,0) node[right] {$y(t)$};
	\draw (0,-1) node[left] {$X(z)$}
		to[short, o-o, i={$H(z)$}] ++(2,0) node[right] {$Y(z)$};
	\draw (5,-1) node[left] {$x(n)$}
		to[short, o-o, i={$h(n)$}] ++(2,0) node[right] {$y(n)$};
\end{tikzpicture}
\end{document}
```

信号流图中，变量可以是**变换域**或**时域**，系统可以是**离散**或**连续**时间。

## 系统的性质分类

### 线性时不变（LTI）系统

#### 线性性

**线性性**是指系统的响应与激励成正比关系，即若已知系统对激励 $e_{1}(t)$、$e_{2}(t)$ 的响应分别为 $r_{1}(t)$、$r_{2}(t)$，则系统对**激励 $e(t) = a_{1}e_{1}(t) + a_{2}e_{2}(t)$** 的**响应为 $r(t) = a_{1}r_{1}(t) + a_{2}r_{2}(t)$**。

线性性要求系统同时满足**叠加性**和**齐次性**。

#### 时不变性

**时不变性**是指系统的响应与绝对时间无关，即若系统对激励 $e(t)$ 的响应为 $r(t)$，则系统对延时 $t_{0}$ 的激励 $e(t - t_{0})$ 应是响应 $r(t - t_{0})$。

时不变性要求系统**参数不随时间变化**。

> [!definition] 线性时不变系统
> **线性时不变（LTI）系统**是同时满足**线性性**和**时不变性**的系统。在线性时不变系统中，允许**叠加**和**延时**操作。 

> [!theorem] LTI 系统的微分、积分特性
> LTI 系统允许**微分**操作，即若系统对激励 $e(t)$ 的响应为 $r(t)$，则
> + 系统对激励 $\dfrac{\dif}{\dif t} e(t)$ 的响应为 $\dfrac{\dif}{\dif t} r(t)$；
> + 系统对激励 $\dint_{0}^{t} e(\tau) \dif\tau$ 的响应为 $\dint_{0}^{t} r(\tau) \dif\tau$。

### 因果系统与非因果系统

**因果系统**的响应 $r(t)$ 只与当前和过去的激励 $e(t)$ 有关，而与未来的激励无关。

定义**因果信号**为 $\forall t < 0$，$x(t) = 0$ 的信号，则**因果信号 $e(t)$ 激励因果系统的响应 $r(t)$ 也为因果信号**。

若信号自变量不是时间，如数字图像处理，研究因果性意义不大。

### 稳定系统和不稳定系统

系统的**稳定**有多种判别准则，如 **BIBO 稳定性**、**Lyapunov 稳定性**等。

#### 输入有界输出有界（BIBO）稳定

对所有的激励信号 $e(t)$ **满足 $|e(t)| \le M_{e}$**，系统的响应信号 $r(t)$ 都**满足 $|r(t)| \le M_{r}$**，则称该系统是 **BIBO 稳定**的。

### 连续时间系统与离散时间系统

**连续时间系统**的输入和输出都是**连续时间信号**，一般记作 $e(t)$ 和 $r(t)$；**离散时间系统**的输入和输出都是**离散时间信号**，记作 $e[n]$ 和 $r[n]$。

### \*动态系统与即时系统

**动态**系统是**系统状态随时间而变化**的系统，也称动力（学）系统，一般用微分方程描述，其系统的状态变量是时间的函数。

### 可逆系统与不可逆系统

> [!definition] 可逆系统
> 若系统在**不同激励**作用下产生**不同的响应**，则称为**可逆系统**；每个可逆系统都对应一个「逆系统」，两者级联后的输出信号和输入信号相同。

此处的「可逆」**与数学上的可逆不同**，它只要求系统在不同激励下产生不同响应，即对系统的响应存在**唯一的激励信号**。

### \*集总参数系统与分布参数系统

只由**集总参数元件**组成的系统称为**集总参数系统**；含有**分布参数元件**的系统是**分布参数系统**。

+ 若分布在空间中的电磁过程可以用 $R$、$C$、$L$ 等一些**基本电路参数**集中表示，称这部分物理空间为**集总参数元件**，用常微分方程描述。
+ 若分布在空间中的电磁过程不能简单地用基本电路参数表示，而需要考虑具体空间中的电磁场能量损耗与存储，称这部分物理空间为**分布参数元件**，用偏微分方程描述。



# Fourier 级数 (FS)

## 周期信号的 Fourier 级数分析

### 定义

#### 三角函数形式

周期函数可表示为三角函数的线性组合，即 **Fourier 级数**。

> [!definition] Fourier 级数（三角函数形式）
> 周期为 $T_{1}$ 的函数 $f(t)$ 可表示为三角函数的级数：
> $$\begin{align}
> f(t) &=a_{0}+a_{1}\cos(\omega_{1}t)+b_{1}\sin(\omega_{1}t)+a_{2}\cos(2\omega_{1}t)+b_{2}\sin(2\omega_{1}t)+\cdot\cdot\cdot\\
> &=a_{0}+\displaystyle\sum_{n=1}^{\infty}\big(a_{n}\cos(n\omega_{1}t)+b_{n}\sin(n\omega_{1}t)\big) \\
> \end{align}$$
> 其中，$a_{0}$ 为**直流分量**，$a_{n}$ 和 $b_{n}$ 为**交流分量**，其值为
> $$\begin{align}
> a_{0} &=\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t) \dif t \\
> a_{n} &=\frac{2}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\cos(n\omega_{1}t) \dif t, \quad 
> b_{n} =\frac{2}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\sin(n\omega_{1}t) \dif t
> \end{align}$$
> $T_{1}$ 为周期，$\omega_{1}=\dfrac{2\pi}{T_{1}}$ 称为**基频**。

^e6092d

也可用辅助角公式将三角级数中的正余弦项**合并为余弦项**，即
$$\begin{align}
f(t) &=a_{0}+\displaystyle\sum_{n=1}^{\infty}\big(a_{n}\cos(n\omega_{1}t)+b_{n}\sin(n\omega_{1}t)\big) \\
&=c_{0}+\displaystyle\sum_{n=1}^{\infty}c_{n}\cos(n\omega_{1}t+\varphi_{n})
\end{align}$$
其中 $c_{0}=a_{0}$，$c_{n}=\sqrt{a_{n}^{2}+b_{n}^{2}}$，$\varphi_{n}$ 满足 $\tan\varphi_{n}=-\dfrac{b_{n}}{a_{n}}$。

> [!danger] 相位谱 $\varphi_{n}$ 的计算
> **不可使用 $\varphi_{n}=-\arctan\dfrac{b_{n}}{a_{n}}$ 计算相位谱**，其正确值为先计算
> $$\varphi_{n}=\begin{cases} 
> -\arctan\dfrac{b_{n}}{a_{n}}, & a_{n}\ge0 \\
> \pi-\arctan\dfrac{b_{n}}{a_{n}}, & a_{n}<0
> \end{cases}$$
> 再将 $\varphi_{n}$ 由 $\left(-\dfrac{\pi}{2},\dfrac{3\pi}{2}\right)$ 转换到 $\left(0,2\pi\right)$ 或 $\left(-\pi,\pi\right)$。

同理还可**合并为正弦项**，即
$$\begin{align}
f(t) &=a_{0}+\displaystyle\sum_{n=1}^{\infty}\big(a_{n}\cos(n\omega_{1}t)+b_{n}\sin(n\omega_{1}t)\big) \\
&=d_{0}+\displaystyle\sum_{n=1}^{\infty} d_{n}\sin(n\omega_{1}t+\theta_{n}) 
\end{align}$$
其中 $d_{0}=a_{0}$，$d_{n}=\sqrt{a_{n}^{2}+b_{n}^{2}}$，$\theta_{n}$ 满足 $\tan\theta_{n}=\dfrac{a_{n}}{b_{n}}$。

#### 复指数形式

由欧拉公式
$$
\cos(\omega t) = \frac{1}{2}\left(e^{\I \omega t}+e^{-\I \omega t}\right), \quad \sin(\omega t) = \frac{1}{2\I }\left(e^{\I \omega t}-e^{-\I \omega t}\right)
$$
代入[[#^e6092d|三角函数形式的 Fourier 级数]]，可得
$$\begin{align}
f(t)&=a_{0}+\displaystyle\sum_{n=1}^{\infty}\left[\displaystyle\frac{a_{n}}{2}\left(\mathrm{e}^{\I n\omega_{1}t}+\mathrm{e}^{-\I n\omega_{1}t}\right)+\displaystyle\frac{b_{n}}{2\I }\left(\mathrm{e}^{\I n\omega_{1}t}-\mathrm{e}^{-\I n\omega_{1}t}\right)\right] \\
&=a_{0}+\displaystyle\sum_{n=1}^{\infty}\left(\displaystyle\frac{a_{n}-\I b_{n}}{2}\mathrm{e}^{\I n\omega_{1}t}+\displaystyle\frac{a_{n}+\I b_{n}}{2}\mathrm{e}^{-\I n\omega_{1}t}\right) \\
&=a_{0}+\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{a_{n}-\I b_{n}}{2}\mathrm{e}^{\I n\omega_{1}t}+\displaystyle\sum_{n=-\infty}^{-1}\displaystyle\frac{a_{-n}+\I b_{-n}}{2}\mathrm{e}^{\I n\omega_{1}t}
\end{align}$$
其中
$$
\begin{align} \frac{a_{n}-\I b_{n}}{2} & =\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\left[\cos(n\omega_{1}t)-\I\sin(n\omega_{1}t)\right]\mathrm{d}t \\ & =\frac{1}{T_1}\int_{t_0}^{t_0+T_1}f(t)\mathrm{e}^{-\I n\omega_1t}\mathrm{d}t, \quad &n=1,2,3,\cdots 
\end{align}$$
$$\begin{align}\frac{a_{-n}+\I b_{-n}}{2} & =\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\left[\cos(-n\omega_{1}t)+\I\sin(-n\omega_{1}t)\right]\mathrm{d}t \\[1ex] & =\frac{1}{T_1}\int_{t_0}^{t_0+T_1}f(t)\mathrm{e}^{-\I n\omega_1t}\mathrm{d}t &\hspace{-5em} n = -1,-2,-3,\cdots 
\end{align}$$
$$
a_{0}  =\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\mathrm{e}^{-\I 0\omega_{1}t}\mathrm{d}t
$$

> [!definition] Fourier 级数（复指数形式）
> 周期为 $T_{1}$ 的函数 $f(t)$ 可表示为复指数的级数：
> $$f(t)=\sum_{n=-\infty}^{\infty} F_{n}\mathrm{e}^{\I n\omega_{1}t}$$
> 其中 $F_{n}$ 为**频谱系数**，其值为
> $$F_{n}=\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\mathrm{e}^{-\I n\omega_{1}t} \dif t$$
> $T_{1}$ 为周期，$\omega_{1}=\dfrac{2\pi}{T_{1}}$ 为**基频**。

### 函数的对称性

#### 偶函数

若 $f(t)=f(-t)$，则**正弦分量 $b_{n}=0$**，**Fourier 系数**简化为
$$
\begin{align}
&c_{n} = d_{n} = |a_{n}| = 2|F_{n}|, \quad &&\varphi_{n} = \{0, \pi\}, \\
&F_{n} = F_{-n} = \dfrac{a_{n}}{2}, \quad &&\theta_{n} = \dfrac{\pi}{2}
\end{align}
$$

#### 奇函数

若 $f(t)=-f(-t)$，则**余弦分量 $a_{n}=0$**，**Fourier 系数**简化为
$$
\begin{align}
&c_{n} = d_{n} = |b_{n}| = 2|F_{n}|, \quad &&\varphi_{n} = -\dfrac{\pi}{2}, \\
&F_{n} = -F_{-n} = -\I\dfrac{b_{n}}{2}, \quad &&\theta_{n} = \{0, \pi\}
\end{align}
$$

#### 奇谐函数

若 $f(t)=-f \left(t\pm \dfrac{T_{1}}{2}\right)$，则
+ 对**偶数 $n$**，偶次余弦项 $a_{n}=0$，偶次正弦项 $b_{n}=0$，因**偶次谐波均不满足奇谐函数的平移对称性**；
+ 对**奇数 $n$**，有
	$$a_{n} = \dfrac{4}{T_{1}}\int_{0}^{\frac{T_{1}}{2}}f(t)\cos(n\omega_{1}t) \dif t, \quad b_{n} = \dfrac{4}{T_{1}}\int_{0}^{\frac{T_{1}}{2}}f(t)\sin(n\omega_{1}t) \dif t$$

## 典型周期信号的 Fourier 级数

### 周期矩形脉冲信号

周期为 $T_{1}$，脉宽为 $\tau$ 的矩形脉冲信号 $f(t)$ 可表示为
$$
f(t) = E \sum_{n=-\infty}^{\infty} \left( u\left(t + \dfrac{\tau}{2} - nT_{1}\right) - u\left( t-\dfrac{\tau}{2} -nT_{1} \right)  \right) 
$$
![[周期矩形脉冲信号_时域.png]]

其**频谱系数**为
$$
F_{n} = \dfrac{E}{n\pi} \sin\left(\dfrac{n\omega_{1}\tau}{2}\right) = \dfrac{E\tau}{T_{1}}\mathop{\mathrm{Sa}}\left(\dfrac{n\omega_{1}\tau}{2}\right) = \dfrac{E\tau}{T_{1}} \mathop{\mathrm{sinc}} \left(\dfrac{n\omega_{1}\tau}{2\pi}\right)
$$

+ **谱线间隔**为基频 $\omega_{1}=\dfrac{2\pi}{T_{1}}$；
+ **谱线强度**正比于**脉幅** $E$，反比于**周期** $T_{1}$，直流分量为 $F_{0}=\dfrac{E\tau}{T_{1}}$；
+ **频带宽度**为 $B_{\omega} = \dfrac{2\pi}{\tau}$，或记作 $B_{f} = \dfrac{1}{\tau}$。

![[Pasted image 20250609144621.png]]

### 方波信号

周期为 $T_{1}$ 的方波信号 $f(t)$ 是**脉宽 $\tau = \dfrac{T_{1}}{2}$** 的周期矩形脉冲信号的**交流分量**，其**频谱系数**为
$$
\begin{align}
F_{n} &= \dfrac{E \dfrac{T_{1}}{2}}{T_{1}} \mathrm{Sa} \left( \dfrac{n\omega_{1} \cdot \dfrac{T_{1}}{2}}{2} \right) = \dfrac{E}{2} \mathrm{Sa} \left( \dfrac{n\pi}{2} \right) = \dfrac{E}{n \pi} \sin \left( \dfrac{n\pi}{2} \right) \\
&=\begin{cases}
\dfrac{E}{n\pi}, & n \equiv 1 \pmod{4} \\
-\dfrac{E}{n\pi}, & n \equiv 3 \pmod{4} \\
0, & \text{elsewhere}
\end{cases}
\end{align}

$$

![[Pasted image 20250609144526.png]]






# Fourier 变换 (FT)

Fourier's Evaluation of FT:

> Regarding the researches of d’Alembert and Euler could one not add that if they knew this expansion, they made but a very imperfect use of it. *They were both persuaded that an arbitrary and discontinuous function could never be resolved in series of this kind*, and it does not even seem that anyone had developed a constant in cosines of multiple arcs, the first problem which I had to solve in the theory of heat.
> 
> (Joseph Fourier, 1808)

## 从 [[#Fourier 级数 (FS)]]到 Fourier 变换

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
> $$\begin{align}
> &F(\omega) = \mathscr{F} \{ f(t) \} = \dint_{-\infty}^{\infty} f(t) \e^{-\I\omega t} \dif t \\
> &f(t) = \mathscr{F}^{-1} \{ F(\omega) \} = \dfrac{1}{2\pi} \dint_{-\infty}^{\infty} F(\omega) \e^{\I\omega t} \dif \omega
> \end{align}$$

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
$$\mathscr{F}\{a f_{1}(t) + b f_{2}(t)\} = a \mathscr{F}\{f_{1}(t)\} + b \mathscr{F}\{f_{2}(t)\}$$

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
$$\mathscr{F}\left\{ \dfrac{\dif f(t)}{\dif t} \right\} = \I\omega F(\omega)$$
进一步地，对于 **$n$ 阶可微**函数 $f(t)$，有
$$\mathscr{F}\left\{ \dfrac{\dif^{n} f(t)}{\dif t^{n}} \right\} = (\I\omega)^{n} F(\omega)$$

对于**可积**函数 $f(t)$，有
$$\mathscr{F}\left\{ \int_{-\infty}^{t} f(\tau) \dif \tau \right\} = \dfrac{F(\omega)}{\I\omega} + \pi F(0) \delta(\omega)$$

### $t$ 域平移

对于函数 $f(t)$，
$$\mathscr{F}\{f(t-t_{0})\} = F(\omega) \e^{-\I \omega t_{0}}$$
即，原函数延迟 $t_{0}$，其 Fourier 变换乘以 $\e^{-\I\omega t_{0}}$，**相移改变 $-\omega t_{0}$**。

### $t$ 域缩放

对于函数 $f(t)$，
$$\mathscr{F}\{f(at)\} = \dfrac{1}{|a|} F\left(\dfrac{\omega}{a}\right)$$
**时域压缩 $⇔$ 频域扩展；时域扩展 $⇔$ 频域压缩。**

特别地，$\mathscr{F} \{ f(-t) \} = F(-\omega)$。

### $\omega$ 域微分、积分

对于**可微**的 Fourier 变换像函数 $F(\omega)$，有
$$\dfrac{\dif F(\omega)}{\dif \omega} = \mathscr{F}\{-\I t f(t)\}$$

对于**可积**的 Fourier 变换像函数 $F(\omega)$，有
$$
\dint_{-\infty}^{\omega} F(\varOmega) \dif \varOmega = \mathscr{F} \left\{ - \dfrac{f(t)}{\I t} + \pi f(0) \delta(t) \right\}
$$

### $\omega$ 域平移

对于 Fourier 变换像函数 $F(\omega)$，
$$ F(\omega - \omega_{0}) = \mathscr{F}\{f(t)\e^{\I\omega_{0} t}\} $$
即，原函数被 $\e^{\I\omega t}$ 加权，则像函数**在频域上右移 $\omega_{0}$**。

### 卷积性质

> [!theorem] 时域卷积定理
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Fourier 变换 $F_{1}(\omega)$、$F_{2}(\omega)$ 存在，则
> $$\mathscr{F}\{f_{1}(t) * f_{2}(t)\} = F_{1}(\omega) F_{2}(\omega)$$

> [!theorem] 频域卷积定理 
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Fourier 变换 $F_{1}(s)$、$F_{2}(s)$ 存在，则
> $$\mathscr{F}\{f_{1}(t) f_{2}(t)\} = \dfrac{1}{2\pi} F_{1}(\omega) * F_{2}(\omega)$$

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

一般地，周期为 $T_{1}$ 的周期信号 $f(t)$ 可展成 [[#Fourier 级数 (FS)]]
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

# Laplace 变换 (LT)

## Laplace 变换引入

### Laplace 变换的定义

> [!definition] Laplace 变换和逆变换
> 对于一个函数 $f(t)$，其 **Laplace 变换**和**逆变换**定义为
> $$\begin{align} &F(s) = \mathscr{L}\{f(t)\} = \int_{0_{-}}^\infty f(t) \e^{-st} \dif t \\
> &f(t) = \mathscr{L}^{-1}\{F(s)\} = \frac{1}{2\pi \I} \int_{\sigma - \I\infty}^{\sigma + \I\infty} F(s) \e^{st} \dif s \end{align}$$
> 其中 $s = \sigma + \I \omega$。

一般待研究信号 $f(t)$ 都是因果信号，所以正变换的积分下限取 $0_{-}$，此称**单边（Unilateral）Laplace 变换**。如果下限取到 $-\infty$，则称为**双边（Bilateral）Laplace 变换**。

> [!note]+ Laplace 变换与 Fourier 变换的关系
> + 对于**因果**信号 $f(t)$，Laplace 变换是 **$f(t) \e^{-\sigma t}$ 的 Fourier 变换**。
> $$ F(s) = \mathscr{L}\{f(t)\} = \int_{0_{-}}^\infty f(t) \e^{-st} \dif t = \int_{0_{-}}^\infty \left(  f(t) \e^{-\sigma t} \right) \e^{-\I \omega t} \dif t = \mathscr{F}[f(t) \e^{-\sigma t}] = F_{1}(\omega) $$
> 其中因果性保证了对 $t < 0$ 有 $f(t) \equiv 0$。
> + 对上面 $F_{1}(\omega)$ 做 Fourier 逆变换，得到
> $$ f(t) \e^{-\sigma t} = \mathscr{F}^{-1}[F_{1}(\omega)] = \frac{1}{2\pi} \int_{-\infty}^{\infty} F_{1}(\omega) \e^{\I \omega t} \dif \omega$$
> 两侧同时乘以 $\e^{\sigma t}$，得到
> $$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F_{1}(\omega) \e^{(\sigma + \I \omega) t} \dif \omega = \frac{1}{2\pi\I} \int_{\sigma -\I\infty}^{\sigma + \I\infty} F(s) \e^{st} \dif s = \mathscr{L}^{-1}\{F(s)\} $$
> 其中 $\dif s = \dif \sigma + \I \dif \omega$。
> + **Fourier 变换是虚轴上的 Laplace 变换**。

### Laplace 变换的收敛条件

Laplace 变换**存在**的条件是原函数 $f(t)$ **分段连续**且为**指数阶函数**。即，存在正实数 $\sigma_{0}$ 使得 $\lim_{ t \to \infty }\limits f(t) \e^{-\sigma t} = 0$ 对所有 $\sigma > \sigma_{0}$ 成立。

> [!note] 说明
> 这是为了保证积分 $\displaystyle \int_{0_{-}}^\infty f(t) \e^{-\sigma t} \dif t$ 收敛，即保证 **$f(t) \e^{-\sigma t}$ 绝对可积**。
> 
> 由于 $f(t)$ 乘以衰减函数 $\e^{-\sigma t}$ 后才满足绝对可积，所以**原本不存在 Fourier 变换的信号**（如 $t^{n}$）在 Laplace 变换中也可能可以处理。

### 常见函数的 Laplace 变换

+ **冲激函数 $\delta(t)$**
$$\mathscr{L}\{\delta(t)\} = \int_{0_{-}}^\infty \delta(t) \e^{-st} \dif t = \e^{0} = 1, \quad \forall \sigma$$
注意积分下限为 $0_{-}$，所以**零点出现的冲激量**也包含在内。

+ **阶跃函数 $u(t)$**
$$\mathscr{L}\{u(t)\} = \int_{0_{-}}^\infty u(t) \e^{-st} \dif t = \int_{0_{-}}^\infty \e^{-st} \dif t = \frac{1}{s}, \quad \forall \sigma > 0$$

+ **指数函数 $\e^{-at}$**
$$\mathscr{L}\{\e^{-at}\} = \int_{0_{-}}^\infty \e^{-at} \e^{-st} \dif t = \int_{0_{-}}^\infty \e^{-(a+s)t} \dif t = \frac{1}{a+s}, \quad \forall \sigma > -a$$

+ **幂函数 $t^{n}$**（其中 $n \in \mathbb{Z}_{+}$）
$$\mathscr{L}\{t^{n}\} = \int_{0_{-}}^\infty t^{n} \e^{-st} \dif t = - \dfrac{t^n\e^{-st}}{s} \Bigg|_{0_{-}}^{\infty} + \dfrac{n}{s} \int_{0_{-}}^\infty t^{n-1} \e^{-st} \dif t = \dfrac{n}{s} \mathscr{L}\{t^{n-1}\}$$
递推得到
$$\mathscr{L}\{t^{n}\} = \dfrac{n!}{s^{n+1}}, \quad \forall \sigma > 0$$

## Laplace 变换的基本性质

### 线性性（叠加性、齐次性）

给定两个函数 $f_{1}(t)$ 和 $f_{2}(t)$，以及两个常数 $a$ 和 $b$，则有
$$\mathscr{L}\{a f_{1}(t) + b f_{2}(t)\} = a \mathscr{L}\{f_{1}(t)\} + b \mathscr{L}\{f_{2}(t)\}$$

### $t$ 域微分、积分

对于**可微**函数 $f(t)$，有
$$\mathscr{L}\left\{ \dfrac{\dif f(t)}{\dif t} \right\} = s F(s) - f(0_{-})$$
进一步地，对于 **$n$ 阶可微**函数 $f(t)$，有
$$\mathscr{L}\left\{ \dfrac{\dif^{n} f(t)}{\dif t^{n}} \right\} = s^{n} F(s) - \sum_{r=0}^{n-1} s^{n-r-1} f^{(r)}(0_{-})$$

对于**可积**函数 $f(t)$，有
$$\mathscr{L}\left\{ \int_{-\infty}^{t} f(\tau) \dif \tau \right\} = \dfrac{F(s)}{s} + \dfrac{\displaystyle\int_{-\infty}^{0_{-}} f(\tau) \dif \tau}{s}$$
其中 $\displaystyle\int_{-\infty}^{0_{-}} f(\tau) \dif \tau$ 可视为 $t=0_{-}$ 处的积分**初值**。

### $t$ 域平移

对于函数 $f(t)$，
$$\mathscr{L}\{f(t-t_{0})u(t-t_{0})\} = \e^{-st_{0}} F(s), \quad t_{0}>0$$
即，原函数延迟 $t_{0}$，其 Laplace 变换乘以 $\e^{-st_{0}}$。

> [!example] 四种延时斜变波形的 Laplace 变换
> ![[四种延时斜变波形.png]]
> $$\begin{align}
> & \mathscr{L}\{t u(t)\} = \dfrac{1!}{s^{1+1}} = \dfrac{1}{s^{2}} \\
> & \mathscr{L}\{t u(t-t_{0})\} = \mathscr{L}\{t u(t)\} - \int_{0_{-}}^{t_{0}} t \e^{-st} \dif t = \dfrac{1}{s^{2}} - \dfrac{1}{s^{2}} \left( 1 - st_{0} \e^{-st_{0}} - \e^{-st_{0}} \right) = \dfrac{\e^{-st_{0}}}{s^{2}} + \dfrac{\e^{-st_{0}}}{s} \\
> & \mathscr{L}\{(t-t_{0}) u(t)\} = \mathscr{L}\{t u(t)-t_{0} u(t)\} = \dfrac{1}{s^{2}} - \dfrac{t_{0}}{s} \\
> & \mathscr{L}\{(t-t_{0}) u(t-t_{0})\} = \dfrac{\e^{-st_{0}}}{s^{2}} \\
> \end{align}$$

### $t$ 域缩放

对于函数 $f(t)$，
$$\mathscr{L}\{f(at)\} = \dfrac{1}{a} F\left(\dfrac{s}{a}\right), \quad a>0$$

### $s$ 域微分、积分

对于**可微**的 Laplace 变换像函数 $F(s)$，有
$$\dfrac{\dif F(s)}{\dif s} = \mathscr{L}\{-t f(t)\}$$

对于**可积**的 Laplace 变换像函数 $F(s)$，有
$$\int_s^{\infty} F(s_{1}) \dif s_{1} = \mathscr{L}\left\{ \dfrac{f(t)}{t} \right\}$$

### $s$ 域平移

对于 Laplace 变换像函数 $F(s)$，
$$ F(s+a) = \mathscr{L}\{f(t)\e^{-at}\} $$
即，原函数被 $\e^{-at}$ 加权，则像函数在复频域上平移 $a$。

### 初值定理和终值定理

> [!theorem] 初值定理
> 若函数 $f(t)$ 及其导数 $\dfrac{\dif f(t)}{\dif t}$ 的 Laplace 变换存在，则
> $$\lim_{ t \to 0_{+} } f(t) = f(0_{+}) = \lim_{ s \to \infty } s F(s)$$

> [!theorem] 终值定理
> 若函数 $f(t)$ 及其导数 $\dfrac{\dif f(t)}{\dif t}$ 的 Laplace 变换存在，极限 $\lim\limits_{ t \to \infty } f(t)$ 也存在，则
> $$\lim_{ t \to \infty } f(t) = \lim_{ s \to 0 } s F(s)$$

### 卷积性质

> [!theorem] 时域卷积定理
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Laplace 变换 $F_{1}(s)$、$F_{2}(s)$ 存在，则
> $$\mathscr{L}\{f_{1}(t) * f_{2}(t)\} = F_{1}(s) F_{2}(s)$$

> [!theorem] 频域卷积定理 
> 若函数 $f_{1}(t)$ 和 $f_{2}(t)$ 的 Laplace 变换 $F_{1}(s)$、$F_{2}(s)$ 存在，则
> $$\mathscr{L}\{f_{1}(t) f_{2}(t)\} = \dfrac{1}{2\pi \I} \int_{\sigma - \I\infty}^{\sigma + \I\infty} F_{1}(p) F_{2}(p) \dif p = \dfrac{1}{2\pi\I} F_{1}(s) * F_{2}(s)$$

## Laplace 逆变换

Laplace 变换像函数 $F(s)$ [[#用 Laplace 变换解系统微分方程的一般步骤|一般]]形如
$$\begin{align}
F(s) &= \dfrac{B(s)}{A(s)} = \dfrac{b_{m}s^m + b_{m-1}s^{m-1} + \cdots + b_{1}s + b_{0}}{a_{n}s^n + a_{n-1}s^{n-1} + \cdots + a_{1}s + a_{0}} \\
&= \dfrac{b_{m}}{a_{n}} \dfrac{(s-z_{1})(s-z_{2})\cdots(s-z_{m})}{(s-p_{1})(s-p_{2})\cdots(s-p_{n})}
= \dfrac{b_{m}}{a_{n}} \dfrac{\prod\limits_{j=1}^m (s-z_{j})}{\prod\limits_{i=1}^n (s-p_{i})}
\end{align}$$
其中，$z_{j}$ 和 $p_{i}$ 分别称为 $F(s)$ 的**零点**和**极点**。一般地，假设 $m < n$，即 $F(s)$ 为**真分式**。

### 部分分式分解法

#### $\{ p_{i} \}_{1 \le i \le n}$ 全为实数轴上单极点

若 $p_{i}$ 全为**实数轴上的单极点**，则 $F(s)$ 可分解为
$$
F(s) = \dfrac{K_{1}}{s-p_{1}} + \dfrac{K_{2}}{s-p_{2}} + \cdots + \dfrac{K_{n}}{s-p_{n}}
$$
其中 $K_{i} = \lim\limits_{ s \to p_{i} } (s-p_{i})F(s)$。 

做逆变换得到
$$
f(t) = \left( K_{1} \e^{p_{1}t} + K_{2} \e^{p_{2}t} + \cdots + K_{n} \e^{p_{n}t} \right) u(t)
$$

#### $\{ p_{i} \}_{1 \le i \le n}$ 中有共轭复极点

设 $p_{i}$ 中有一对**共轭复极点** $-\alpha \pm \I\beta$，则 $F(s)$ 可分解为
$$
F(s) = \dfrac{K_{1}}{s + \alpha - \I\beta} + \dfrac{K_{2}}{s + \alpha + \I\beta} + \cdots 
$$
其中
$$\begin{cases}
K_{1} = \lim\limits_{ s \to -\alpha + \I\beta } (s + \alpha - \I\beta)F(s) \\
K_{2} = \lim\limits_{ s \to -\alpha - \I\beta } (s + \alpha + \I\beta)F(s)
\end{cases}$$

记 $K_{1} = A + \I B$，则共轭复极点逆变换对应的原函数为
$$
\mathscr{L}^{-1} \left\{ \dfrac{K_{1}}{s + \alpha - \I\beta} + \dfrac{K_{2}}{s + \alpha + \I\beta} \right\} 
= 2\e^{-\alpha t} \left( A \cos \beta t - B \sin \beta t \right) u(t)
$$

> [!note] 说明
> 实际上，也可以**直接看出结果**，如
> $$\dfrac{s+\gamma}{(s+\alpha)^2 + \beta^2} = \underbrace{ \dfrac{s+\alpha}{(s+\alpha)^2 + \beta^2} }_{ \e^{-\alpha t} \cos\beta t } - \dfrac{\alpha-\gamma}{\beta} \underbrace{ \dfrac{\beta}{(s+\alpha)^2 + \beta^2} }_{ \e^{-\alpha t} \sin\beta t }$$

#### $\{ p_{i} \}_{1 \le i \le n}$ 中有高阶极点

设 $p_{i}$ 中有一个 **$k$ 阶极点** $p_{1}$，则 $F(s)$ 可分解为
$$
F(s) = \dfrac{K_{11}}{(s-p_{1})^k} + \dfrac{K_{12}}{(s-p_{2})^{k-1}} + \cdots + \dfrac{K_{1k}}{s-p_{1}} + \cdots
$$
其中 $K_{11} = \lim\limits_{ s \to p_{1} }(s-p_{1})^kF(s)$，$K_{1i} = \dfrac{1}{(i-1)!} \lim\limits_{ s \to p_{1} } \dfrac{\dif^{i-1}}{\dif s^{i-1}}(s-p_{1})^kF(s)$。

已知 $\mathscr{L}\left\{ t^n u(t) \right\} = \dfrac{n!}{s^{n+1}}$，则知
$$
\mathscr{L}^{-1}\left\{ \dfrac{K_{1,k+1-r}}{(s-p_{1})^r} \right\} = K_{1,k+1-r}\dfrac{t^{r-1} \e^{p_{1}t}}{(r-1)!} u(t)
$$
故上面 $k$ 阶极点 $p_{1}$ 对应的原函数为
$$\begin{align}
\mathscr{L}^{-1}\left\{ \dfrac{K_{11}}{(s-p_{1})^k} + \dfrac{K_{12}}{(s-p_{2})^{k-1}} + \cdots + \dfrac{K_{1k}}{s-p_{1}} \right\} \qquad\qquad\qquad\qquad\qquad \\
= \sum\limits_{r=1}^k \dfrac{t^{r-1}}{(k-r)!(r-1)!} \lim\limits_{ s \to p_{1} } \dfrac{\dif^{k-r}}{\dif s^{k-r}}(s-p_{1})^kF(s) \cdot \e^{p_{1}t} u(t)
\end{align}$$

### 留数法

[[#部分分式分解法]]中已经表现出部分**留数**的应用特征。一般地，对于一个 Laplace 变换**像函数** $F(s)$，其逆变换为
$$
f(t) = \dfrac{1}{2\pi \I} \int_{\sigma - \I\infty}^{\sigma + \I\infty} F(s) \e^{st} \dif s
= \underbrace{ \dfrac{1}{2\pi \I} \int_{C} F(s) \e^{st} \dif s }_{ \sum\limits_{i=1}^n \mathrm{Res} \left[ F(s)\e^{st}, p_{i} \right]  } - \dfrac{1}{2\pi \I} \underbrace{ \int_{C_{\infty}} F(s) \e^{st} \dif s }_{ 0 }
$$
其中 $C_{\infty}$ 是半径 $R \to \infty$ 的圆弧，$C$ 是 Laplace 逆变换**积分路径**与 $C_{\infty}$ 构成的**闭合曲线**。故有
$$
f(t) = \mathscr{L}^{-1} \{F(s)\} = \sum\limits_{i=1}^n \mathrm{Res} \left[ F(s)\e^{st}, p_{i} \right]
$$


# z 变换

**$z$ 变换**是**求解差分方程**的有力工具，类似于连续时间系统的 **Laplace 变换**。

## $z$ 变换及其收敛域

### 单边 $z$ 变换

可比照冲激抽样序列的 **Laplace 变换**
$$\begin{align}
&x_{\mathrm{s}} (t) = x (t) \delta_{T} (t) = \sum\limits_{n=0}^{\infty} x(nT) \delta(t - nT) \\
&\mapsto X_{\mathrm{s}}(s) = \mathscr{L} \{ x_{\mathrm{s}} (t) \} = \sum\limits_{n=0}^{\infty} x(nT) \e^{-s n T}
\end{align}$$
取 $z = \e^{sT}$ 并令 $T = 1$，得到离散时间序列 $x(n)$ 的单边 $z$ 变换为

> [!definition] 单边 $z$ 变换
> 离散时间序列 $x(n)$ 的**单边 $z$ 变换**定义为
> $$ X(z) = \mathscr{Z} \{ x(n) \} = \sum\limits_{n=0}^{\infty} x(n) z^{-n} $$

另一方面，也可由 Laurent 级数
$$
f(z) = \sum\limits_{n=-\infty}^{\infty} a_{n} (z - z_{0})^n
$$
定义 $z$ 变换为**复变量 $z^{-1}$ 的幂级数**，即 $z_{0} = 0$ 的 Laurent 级数。

### 双边 $z$ 变换

> [!definition] 双边 $z$ 变换
> 离散时间序列 $x(n)$ 的**双边 $z$ 变换**定义为
> $$ X(z) = \mathscr{Z} \{ x(n) \} = \sum\limits_{n=-\infty}^{\infty} x(n) z^{-n} $$

**因果序列的单边 $z$ 变换与双边 $z$ 变换相同**。Laplace 变换侧重单边，因为连续系统中非因果信号和系统的应用极少；而离散系统**非因果有些应用**，所以兼顾研究单边和双边。

### $z$ 变换的收敛域

$z$ 变换的收敛域（ROC）是指使得 **$z$ 变换级数收敛**的 $z$ 的值的集合。该级数收敛的充分条件是**绝对可和**，即
$$
\sum\limits_{n=-\infty}^{\infty} |x(n) z^{-n}| < \infty
$$
这又可引入判定法判别，即收敛条件为
$$\begin{align}
&\begin{cases}
\lim\limits_{ n \to \infty } \left| \dfrac{x(n+1) z^{-n-1}}{x(n) z^{-n}} \right| = \dfrac{1}{|z|} \lim\limits_{ n \to \infty } \left| \dfrac{x(n+1)}{x(n)} \right| < 1  \\
\lim\limits_{ n \to -\infty } \left| \dfrac{x(n-1) z^{-n+1}}{x(n) z^{-n}} \right| = |z| \lim\limits_{ n \to -\infty } \left| \dfrac{x(n-1)}{x(n)} \right| < 1
\end{cases}  \\
& \Longrightarrow \lim\limits_{ n \to \infty } \left| \dfrac{x(n+1)}{x(n)} \right| < |z| < \lim\limits_{ n \to -\infty } \left| \dfrac{x(n)}{x(n-1)} \right|
\\
\text{OR} \quad &\begin{cases}
\lim\limits_{ n \to \infty} \sqrt[n]{ |x(n) z^{-n}| } = |z^{-1}| \lim\limits_{ n \to \infty} \sqrt[n]{ |x(n)| } < 1 \\
\lim\limits_{ n \to -\infty} \sqrt[-n]{ |x(n) z^{-n}| } = |z| \lim\limits_{ n \to -\infty} \sqrt[-n]{ |x(n)| } < 1
\end{cases} \\
& \Longrightarrow \lim\limits_{ n \to \infty} \sqrt[n]{ |x(n)| } < |z| < \lim\limits_{ n \to -\infty} \sqrt[-n]{ |x(n)| }
\end{align}
$$

与 Laplace 变换类似，$z$ 变换的 ROC 取决于序列 $x(n)$ 的性质。

$z$ 变换的收敛域可借助 **Laplace 变换**的收敛域进行分析。设 $z = r\e^{\I \theta}$，则
$$
z = \e^{sT} = \e^{(\sigma + \I \omega)T} = \e^{\sigma T} \e^{\I \omega T}
$$
即得
$$
r = \e^{\sigma T}, \quad \theta = \omega T
$$
此为 **$s$ 平面和 $z$ 平面之间的映射关系**。

#### 有限时宽信号 $\mapsto$ 有限时宽序列

有限时宽信号如 $x(t) = u(t) - u(t-t_{0})$ 的 Laplace 变换为
$$
\mathscr{L} \{ x(t) \} = \dfrac{1}{s} \left( 1 - \e^{-st_{0}} \right) 
$$
其 ROC 为**全平面**。

对应地，有限时宽序列如 $x(n) = \delta(n)$ 的 $z$ 变换为
$$
\mathscr{Z}\{ x(n) \} = \sum\limits_{n=-\infty}^{\infty} \delta(n) z^{-n} = 1
$$
其 ROC 为**全平面**。

#### 右边信号 $\mapsto$ 右边序列

右边信号如 $x(t) = \e^{-at} u(t)$ 的 Laplace 变换为
$$
\mathscr{L} \{ x(t) \} = \dfrac{1}{s+a}
$$
其 ROC 为 **$\mathfrak{Re} \{ s \} = \sigma > -a$**。

对应地，右边序列如 $x(n) = \e^{-an} u(n)$ 的 $z$ 变换为
$$
\mathscr{Z} \{ x(n) \} = \sum\limits_{n=0}^{\infty} \e^{-an} z^{-n} = \dfrac{1}{1 - \e^{-a} z^{-1}} = \dfrac{z}{z - \e^{-a}}
$$
其 ROC 为 **$|z| > \e^{-a}$**，是 $z$ 平面上一**圆盘之外**的区域。

#### 左边信号 $\mapsto$ 左边序列

左边信号如 $x(t) = -\e^{-at} u(-t)$ 的 Laplace 变换为
$$
\mathscr{L} \{ x(t) \} = \dfrac{1}{s+a}
$$
其 ROC 为 **$\mathfrak{Re} \{ s \} = \sigma < -a$**。

对应地，左边序列如 $x(n) = -\e^{-an} u(-n-1)$ 的 $z$ 变换为
$$
\mathscr{Z} \{ x(n) \} = \sum\limits_{n=-\infty}^{-1} -\e^{-an} z^{-n} = \dfrac{z}{z - \e^{-a}}
$$
其 ROC 为 **$|z| < \e^{-a}$**，是 $z$ 平面上一**圆盘之内**的区域。

#### 双边信号 $\mapsto$ 双边序列

双边信号如 $x(t) = \e^{-at}u(t) + \e^{bt}u(-t)$ 的 Laplace 变换为
$$
\mathscr{L} \{ x(t) \} = \dfrac{1}{s+a} - \dfrac{1}{s-b}
$$
其 ROC 为 **$-a < \sigma < b$**。

对应地，双边序列如 $x(n) = \e^{-an} u(n) + \e^{bn} u(-n-1)$ 的 $z$ 变换为
$$
\mathscr{Z} \{ x(n) \} = \sum\limits_{n=-\infty}^{-1} \e^{-an} z^{-n} + \sum\limits_{n=0}^{\infty} \e^{bn} z^{-n}
= \dfrac{z}{z - \e^{-a}} - \dfrac{z}{z - \e^{b}}
$$
其 ROC 为 **$\e^{-a} < |z| < \e^{b}$**，是 $z$ 平面上一**圆环之内**的区域。

## 逆 $z$ 变换

逆 $z$ 变换是从 $z$ 变换结果恢复原始序列的过程。一般地，有计算式
$$
x(n) = \mathscr{Z}^{-1} \{ X(z) \} = \dfrac{1}{2\pi \I} \oint_{C} X(z) z^{n-1} \dif z
$$
其中 $C$ 是包含 $X(z)z^{n-1}$ 所有**极点**的**逆时针**闭合曲线。

### 部分分式分解

对于有理函数 $X(z)$，可使用**部分分式分解**将其分解为简单的形式，然后**查表**计算逆 $z$ 变换。由于表中变换域函数**分子均带有至少一个 $z$**，因此通常先**将 $\dfrac{X(z)}{z}$ 展开**为分式和再乘以 $z$。

### 幂级数展开

左边、右边序列的有理函数式可分别在**升幂**、**降幂**形式下进行**长除法**，得到 $z^{-1}$ 的幂级数。

### 留数法

对于一般函数 $X(z)$，可使用**留数法**计算逆 $z$ 变换。由留数定理有
$$
x(n) = \dfrac{1}{2\pi\I} \oint_{C} X(z) z^{n-1} \dif z = \sum\limits_{k} \operatorname{Res} \left( X(z) z^{n-1}, z_k \right)
$$
其中 $\operatorname{Res} \left( X(z) z^{n-1}, z_k \right)$ 是极点 $z_k$ 处的**留数**。

对于 $s$ 阶极点 $z_k$，
$$
\operatorname{Res} \left( X(z) z^{n-1}, z_k \right) = \dfrac{1}{(s-1)!} \lim\limits_{z \to z_k} \dfrac{\dif^{s-1}}{\dif z^{s-1}} \left( (z - z_k)^s X(z) z^{n-1} \right)
$$
对于一阶极点，留数可简化为
$$
\operatorname{Res} \left( X(z) z^{n-1}, z_k \right) = \lim\limits_{z \to z_k} (z - z_k) X(z) z^{n-1}
$$

## $z$ 变换的基本性质

### 线性性质

已知 $X_{1}(z) = \mathscr{Z} \{ x_{1}(n) \}$ 和 $X_{2}(z) = \mathscr{Z} \{ x_{2}(n) \}$，则
$$
\mathscr{Z} \{ a_{1} x_{1}(n) + a_{2} x_{2}(n) \} = a_{1} X_{1}(z) + a_{2} X_{2}(z)
$$

### 时移性质

#### 双边 $z$ 变换的时移性质

已知 $X(z) = \mathscr{Z} \{ x(n) \}$，收敛域为 $R_{1} < |z| < R_{2}$，则
$$
\mathscr{Z} \{ x(n - n_{0}) \} = z^{-n_{0}} X(z)
$$
其中 $n_{0}$ 为整数；收敛域不变。

#### 单边 $z$ 变换的时移性质

已知 $X(z) = \mathscr{Z} \{ x(n) \}$，收敛域为 $R_{1} < |z| < R_{2}$，则
$$
\mathscr{Z} \{ x(n - n_{0}) \} = z^{-n_{0}} \left( X(z) + \sum\limits_{k=-n_{0}}^{-1} x(k) z^{-k} \right) 
$$
$$
\mathscr{Z} \{ x(n + n_{0}) \} = z^{n_{0}} \left( X(z) - \sum\limits_{k=0}^{n_{0}-1} x(k) z^{-k} \right)
$$
其中 $n_{0}$ 为正整数；收敛域不变。

特别地，对**因果**序列，时域右移时有
$$
\mathscr{Z} \{ x(n - n_{0}) \} = z^{-n_{0}} X(z)
$$

### 序列的时域加权

#### 线性加权：$z$ 域微分

已知 $X(z) = \mathscr{Z} \{ x(n) \}$，则
$$
\mathscr{Z} \{ n x(n) \} = -z \dfrac{\dif X(z)}{\dif z}
$$
收敛域不变。

#### 指数加权：$z$ 域压扩

已知 $X(z) = \mathscr{Z} \{ x(n) \}$，收敛域为 $R_{1} < |z| < R_{2}$，则
$$
\mathscr{Z} \{ a^{n} x(n) \} = X\left( \dfrac{z}{a} \right)
$$
收敛域变为 $R_{1} |a| < |z| < R_{2} |a|$。

### 初值定理、终值定理

对因果序列 $x(n)$，其单边 $z$ 变换为 $X(z)$，则
+ **初值定理**：$x(0) = \lim\limits_{z \to \infty} X(z)$
+ **终值定理**：$x(\infty) = \lim\limits_{z \to 1} \left( (z-1) X(z) \right)$
其中，终值定理要求 $X(z)$ 的极点在单位圆 $|z| < 1$ 内。

### 卷积定理

#### 时域卷积、$z$ 域乘积

已知 $X_{1}(z) = \mathscr{Z} \{ x_{1}(n) \}$ 和 $X_{2}(z) = \mathscr{Z} \{ x_{2}(n) \}$，则
$$
\mathscr{Z} \{ x_{1}(n) * x_{2}(n) \} = X_{1}(z) X_{2}(z)
$$
收敛域通常为**二者收敛域的交集**；在 $X_{1}(z)$ 与 $X_{2}(z)$ 出现（边缘）**零极点相消**时，**收敛域可能会扩大**。

#### $z$ 域卷积、时域乘积

已知 $X_{1}(z) = \mathscr{Z} \{ x_{1}(n) \}$ 和 $X_{2}(z) = \mathscr{Z} \{ x_{2}(n) \}$，则
$$
\begin{align}
\mathscr{Z} \{ x_{1}(n) x_{2}(n) \} &= \dfrac{1}{2\pi \I} \oint_{C_{1}} X_{1}\left( \dfrac{z}{v} \right) X_{2} (v) v^{-1} \dif v \\
&= \dfrac{1}{2\pi \I} \oint_{C_{2}} X_{1} (v) X_{2}\left( \dfrac{z}{v} \right) v^{-1} \dif v
\end{align}
$$
其中 $C_{1}$ 和 $C_{2}$ 分别是 $\left\{ X_{1}\left( \dfrac{z}{v} \right), X_{2}(v) \right\}$ 收敛域重叠区域、$\left\{ X_{1}(v), X_{2}\left( \dfrac{z}{v} \right) \right\}$ 收敛域重叠区域的**逆时针闭合曲线**。

# 离散余弦变换 (DCT)

## 一维离散余弦变换

> [!definition] 离散余弦变换 (DCT)
> 矢量 $\v{x} = \begin{pmatrix} x_{0} \\ x_{1} \\ \cdots \\ x_{N-1} \end{pmatrix}$ 的**离散余弦变换 (DCT)** 定义为 $\v{y} = \begin{pmatrix} y_{0} \\ y_{1} \\ \cdots \\ y_{N-1} \end{pmatrix}$，其中
> $$\begin{align}
> &y_{0} = \sqrt{\dfrac{1}{N}} \sum\limits_{n=0}^{N-1} x_{n}  \\
> &y_{k} = \sqrt{\dfrac{2}{N}} \sum\limits_{n=0}^{N-1} x_{n} \cos \dfrac{(2n + 1)k\pi}{2N}, \quad k=1,2,\cdots,N-1
> \end{align}$$
> 由 $\v{y}$ 所做的**逆变换 (IDCT)** 为 $\v{x}$，其中
> $$
> x_{n} = \sqrt{ \dfrac{1}{N} } \sum\limits_{k=0}^{N-1} y_{k} \cos \dfrac{(2n + 1)k\pi}{2N}, \quad n=0,1,\cdots,N-1
> $$

可将 DCT 写成**矩阵形式**，即
$$
\v{y} = \boldsymbol{D}_{N} \v{x}, \quad \v{x} = \boldsymbol{D}_{N}^\mathrm{T} \v{y}
$$
其中
$$
\boldsymbol{D}_{N} = \sqrt{ \dfrac{2}{N} } \begin{pmatrix}
\sqrt{ \dfrac{1}{2} } & \sqrt{ \dfrac{1}{2} } & \cdots & \sqrt{ \dfrac{1}{2} } \\
\cos \dfrac{\pi}{2N} & \cos \dfrac{3\pi}{2N} & \cdots & \cos \dfrac{(2N-1)\pi}{2N} \\
\vdots & \vdots & \ddots & \vdots \\
\cos \dfrac{(N-1)\pi}{2N} & \cos \dfrac{(N-1)(3\pi)}{2N} & \cdots & \cos \dfrac{(N-1)(2N-1)\pi}{2N}
\end{pmatrix}
$$

## 二维离散余弦变换

> [!definition] 二维离散余弦变换 (2D-DCT)
> **二维离散余弦变换 (2D-DCT)** 是对二维矩阵 $\boldsymbol{X}$ 的每一行和每一列分别进行一维离散余弦变换 (DCT)，即得到
> $$
> \boldsymbol{Y} = \boldsymbol{D}_{N} \boldsymbol{X} \boldsymbol{D}_{N}^\mathrm{T} = \sum\limits_{m,n} x_{m,n} \boldsymbol{D}_{\mathrm{II}}(m,n)
> $$
> 其**逆变换 (2D-IDCT)** 为
> $$
> \boldsymbol{X} = \boldsymbol{D}_{N}^\mathrm{T} \boldsymbol{Y} \boldsymbol{D}_{N} = \sum\limits_{m,n} y_{m,n} \boldsymbol{D}_{\mathrm{II}}(m,n)
> $$
> 其中，变换系数 $\boldsymbol{D}_{\mathrm{II}}(m,n)$ 定义为
> $$
> \boldsymbol{D}_{\mathrm{II},i,j}(m,n) = \boldsymbol{D}_{N,i,m} \boldsymbol{D}_{M,j,n}
> $$



# 离散时间 Fourier 变换 (DTFT)

## DTFT 及其逆变换

### 序列 DTFT 的引入

**离散时间 Fourier 变换 (DTFT)** 用于研究离散系统频率响应特性。

> [!definition] 离散时间 Fourier 变换 (DTFT)
> 离散时间信号 $x(n)$ 的**离散时间 Fourier 变换**定义为
> $$ x(n) \xrightarrow{\mathrm{DTFT}} X(\omega) = \sum\limits_{n=-\infty}^{\infty} x(n) \e^{-\I n \omega} $$

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
> $$ x(n) = \dfrac{1}{2\pi \I} \displaystyle\oint_{|z|=1} X(z) z^{n-1} \dif z = \dfrac{1}{2\pi} \dint_{-\pi}^{\pi} X(\e^{\I\omega}) \e^{\I n \omega} \dif \omega $$



# 连续时间系统时域分析

## 连续时间系统的数学描述

### 基本的连续时间信号

#### 指数信号 (Exponential signal)
$$f(t) = K \mathrm{e}^{at}$$
+ 单边指数衰减信号 $f(t) = \begin{cases} K\mathrm{e}^{-t/\tau}, &t\ge 0,\\ 0, &\mathrm{elsewhere}.\end{cases}$

#### 正弦信号 (Sinusoidal signal)
$$f(t) = K \sin(\omega t + \theta)$$
+ 指数衰减的正弦信号 $f(t) = \begin{cases} K\mathrm{e}^{-t/\tau} \sin(\omega t), &t\ge 0,\\ 0, &\mathrm{elsewhere}.\end{cases}$

#### 复指数信号 (Complex exponential signal)
$$f(t) = K\mathrm{e}^{st}$$

#### Sa 信号 (抽样信号，Sampling signal)

$$\mathrm{Sa}(t) = \dfrac{\sin t}{t}$$
或
$$\mathrm{\mathrm{sinc}(t)} = \dfrac{\sin(\pi t)}{\pi t} = \mathrm{Sa}(\pi t)$$

+ $\mathrm{Sa}(0) = 1$，$\mathrm{Sa}(n\pi) = 0$
+ $\displaystyle \int_{0}^\infty \mathrm{Sa}(t) \mathop{}\mathrm{d}t = \dfrac{\pi}{2}$，$\displaystyle \int_{-\infty}^\infty \mathrm{Sa}(t) \mathop{}\mathrm{d}t = \pi$

#### 钟形信号 (高斯函数，Gaussian function)

### 奇异信号

本身有不连续点（跳变点），或其导数、积分有不连续点的函数。

![[奇异信号.png]]

#### 单位斜变信号 (Unit ramp signal)
$$f(t) = \begin{cases} t, &t\ge 0,\\ 0, &\mathrm{elsewhere}\end{cases}=tu(t)$$

#### 单位阶跃信号 (Unit step signal)
$$u(t) = \begin{cases} 1, &t > 0,\\ 0, &t < 0.\end{cases}$$
其物理意义是在 $t=0$ 时刻接入直流信号。

> [!TIP] 注意
> $u(t)$ 在跳变点 0 处未定义；或者也可定义为
> $$
> u(t) = \begin{cases} 1, &t > 0,\\ \dfrac{1}{2}, &t = 0,\\ 0, &t < 0.\end{cases}
> $$

单位阶跃信号可以用于：
+ 表示**矩形脉冲**：$R_{\mathrm{T}}(t) = u\left(t - T_{\mathrm{start}}\right) - u\left(t - T_{\mathrm{end}}\right)$
+ 表示**信号接入特性**：e.g. $f_{1}(t) = \sin t\left[ u\left(t - T_{\mathrm{start}}\right) - u\left(t - T_{\mathrm{end}}\right) \right]$
+ 表示**符号函数**：$\mathrm{sgn}(t) = 2u(t) - 1$
+ 表示任意**分段信号**：$f(t) = \sum\limits_{i} f_{i}(t)u(t_{i,\mathrm{start}} - t_{i,\mathrm{end}})$

#### 单位冲激信号 (Unit impulse signal)
$$\delta(t) = \begin{cases} +\infty, &t = 0,\\ 0, &t \neq 0.\end{cases}$$
通常，$\delta(t)$ 用 $u(t)$ 定义，即：
$$
\delta(t) = \lim_{\varepsilon \to 0} \dfrac{1}{\varepsilon} \left[ u\left( t + \dfrac{\varepsilon}{2} \right) - u\left( t - \dfrac{\varepsilon}{2} \right)   \right] 
$$
单位冲激信号描述**持续时间极短、幅度极大**的信号。##### 性质

+ 冲激信号是**偶函数**，$\dint_{-\infty}^\infty \delta(t) \dif t = 1$。
+ 冲激信号具有**筛选特性**，即

> [!theorem] 冲激信号的筛选特性
> 若 $f(t)$ 在 $t=0$ 连续且处处有界，则 $\delta(t)f(t) = f(0)\delta(t)$；进一步，有
> $$\dint_{-\infty}^{\infty} \delta(t)f(t) \dif x = f(0)$$

^288668
+ 由筛选特性，与**时移的冲激信号相卷积**等价于时移，即
$$f(t) * \delta(t - t_{0}) = f(t - t_{0})$$

#### 冲激偶信号 (Doublets signal)
$$\delta'(t) = \dfrac{\mathrm{d}\delta(t)}{\mathrm{d}t}$$

+ 冲激偶信号是**奇函数**，$\displaystyle \int_{-\infty}^\infty \delta'(t) \mathop{}\mathrm{d}t = 0$。
+ 冲激偶信号也具有**筛选特性**，即

> [!theorem] 冲激偶信号的筛选特性
> 若 $f(t)$ 在 $t=0$ 连续且处处有界，则有
> $$\dint_{-\infty}^{\infty} \delta'(t)f(t) \dif x = -f'(0)$$

### 信号的分解

#### 直流分量与交流分量

信号 $f(t)$ 可分解为直流分量 $f_{\mathrm{D}}$ 和交流分量 $f_{\mathrm{A}}$：
$$f(t) = f_{\mathrm{D}} + f_{\mathrm{A}}, \qquad \mathrm{where} \quad \begin{cases}
f_{\mathrm{D}} = \dfrac{1}{t_{2}-t_{1}} \displaystyle\int_{t_{1}}^{t_{2}} f(t) \mathop{}\mathrm{d}t,\\
f_{\mathrm{A}} = f(t) - f_{\mathrm{D}}.
\end{cases}$$

#### 偶分量与奇分量

信号 $f(t)$ 可分解为偶分量 $f_{\mathrm{e}}$ 和奇分量 $f_{\mathrm{o}}$：
$$f(t) = f_{\mathrm{e}} + f_{\mathrm{o}},\qquad \mathrm{where} \quad \begin{cases}
f_{\mathrm{e}} = \dfrac{1}{2} \left( f(t) + f(-t) \right),\\
f_{\mathrm{o}} = \dfrac{1}{2} \left( f(t) - f(-t) \right).
\end{cases}$$

#### 脉冲分量

信号 $f(t)$ 可以基于 $\delta(t)$ 的线性组合表示：
$$
\begin{align}
f(t) &= \lim_{ \Delta t_{1} \to 0 } \sum\limits_{n=-\infty}^{\infty} f(n\Delta t_{1}) \dfrac{u(t - n\Delta t_{1}) - u(t - (n+1)\Delta t_{1})}{\Delta t_{1}} \Delta t_{1} \\
&= \displaystyle\int_{-\infty}^{\infty} f(t_{1}) \delta(t - t_{1}) \dif t_{1}
\end{align}
$$
这是由[[#^288668|冲激函数的筛选特性]]所决定的。

#### 阶跃分量

信号 $f(t)$ 可以基于 $u(t)$ 的线性组合表示：
$$
\begin{align}
f(t) &= f(0) u(t) + \lim_{ \Delta t_{1} \to 0 } \sum\limits_{n=1}^{\infty} \dfrac{f(n \Delta t_{1}) - f((n-1) \Delta t_{1})}{\Delta t_{1}} u(t - n\Delta t_{1}) \Delta t_{1} \\
&= f(0) u(t) + \displaystyle\int_{0}^{\infty} f'(t_{1}) u(t - t_{1}) \mathop{}\mathrm{d}t_{1}
\end{align}
$$

#### 实部分量与虚部分量

信号 $f(t)$ 可分解为实部分量 $f_{\mathrm{R}}$ 和虚部分量 $f_{\mathrm{I}}$：
$$f(t) = f_{\mathrm{R}} + \I f_{\mathrm{I}},\qquad \mathrm{where} \quad \begin{cases}
f_{\mathrm{R}} = \dfrac{1}{2} \left( f(t) + f^{*}(t) \right),\\
f_{\mathrm{I}} = \dfrac{1}{2\I} \left( f(t) - f^{*}(t) \right).
\end{cases}$$

#### 正交函数分解

信号 $f(t)$ 可分解为正交函数的线性组合，得到**相互正交**的组成分量，（对线性系统）可独立分析处理。

正交函数分解的典型例子是 **[[#Fourier 级数 (FS)]]**：
$$
f(t) = a_{0} + \sum\limits_{n=1}^{\infty} \left( a_{n} \cos(n\omega t) + b_{n} \sin(n\omega t) \right)
$$
其中：
+ $a_{0} = \dfrac{1}{T} \displaystyle\int_{0}^{T} f(t) \mathop{}\mathrm{d}t$，$a_{n} = \dfrac{2}{T} \displaystyle\int_{0}^{T} f(t) \cos(n\omega t) \mathop{}\mathrm{d}t$，
+ $b_{n} = \dfrac{2}{T} \displaystyle\int_{0}^{T} f(t) \sin(n\omega t) \mathop{}\mathrm{d}t$。

### 连续时域系统数学模型的建立

连续时间系统在时域上有一般的[[#系统#系统数学模型的时域表示|数学模型表示]]。基于元器件的物理特性和电路的拓扑结构，可以建立连续时间系统的数学模型。

## 时域经典法求解 LTI 系统微分方程

#### 求齐次解

1. 令 $e(t)$ 及其各阶导数为零，即
$$
C_{0}p^{n}r(t) + C_{1}p^{n-1}r(t) + \cdots + C_{n}r(t) = 0
$$
2. 齐次解是**形如 $A\e^{\alpha t}$ 函数的线性组合**，令 $r(t) = A\e^{\alpha t}$，代入并化简得到特征方程
$$
C_{0}\alpha^{n} + C_{1}\alpha^{n-1} + \cdots + C_{n} = 0
$$
称其 $n$ 个根 $\{\alpha_i\}_{i = 1,2,\cdots,n}$ 为**特征根**。
3. 无重根情况下微分方程的**齐次解**为
$$
r_{\mathrm{h}}(t) = A_1 \e^{\alpha_1 t} + A_2 \e^{\alpha_2 t} + \cdots + A_n \e^{\alpha_n t} = \sum\limits_{i=1}^n A_i \e^{\alpha_i t}
$$

#### 求特解

特解 $r_{\mathrm{p}}(t)$ 形式由**激励函数的形式**决定，分为以下几种情况：
+ $e(t) = E$ 为常数，响应的特解为 $r_{\mathrm{p}}(t) = B$；
+ $e(t) = t^p$，响应的特解为 $r_{\mathrm{p}}(t) = B_1 t^p + B_2 t^{p-1} + \cdots + B_{p+1}$；
+ $e(t) = \e^{\alpha t}$，响应的特解为 $r_{\mathrm{p}}(t) = B \e^{\alpha t}$；
+ $e(t) = \sin(\omega t)$ 或 $\cos(\omega t)$，响应的特解为 $r_{\mathrm{p}}(t) = B_1 \sin(\omega t) + B_2 \cos(\omega t)$。

特解的系数 $B_i$ 结合**原方程和激励函数**可以唯一确定。

#### 微分方程的完全解

微分方程的**完全解**为齐次解与特解之和，即
$$
r(t) = r_{\mathrm{h}}(t) + r_{\mathrm{p}}(t) = \underbrace{ \sum\limits_{i=1}^n A_i \e^{\alpha_i t} }_{ \scriptstyle\text{齐次解}\atop\scriptstyle\text{自由响应} } + \underbrace{ r_{\mathrm{p}}(t) }_{ \scriptstyle\text{特解}\atop\scriptstyle\text{强迫响应} }
$$
其中，齐次解又称**自由响应**，特解又称**强迫响应**。

自由响应部分的系数 $A_i$ 可由**一个时刻的初始条件**唯一确定。一般情况下，这个时刻取为 $t = 0_+$，即**激励接入后的初始时刻**。

##### 起始状态与初始状态

+ **起始状态**是指系统在 $t = 0_-$ 时、激励还未接入的响应 **$\v{r}(0_{-})$**，
+ **初始状态**是指系统在 $t = 0_+$ 时、激励已经接入的响应** $\v{r}(0_{+})$**。

对实际的系统模型，初始条件要根据激励信号**接入瞬时**系统所处的状态，即**初始状态**决定，但物理上往往只知道**起始状态**。在某些情况下，初始状态可能**发生跳变**。

##### 初始条件确定的物理方法

利用电路内部元器件储能（包括电容储存电荷以及电感储存磁链）的连续性，有：
+ 若无冲激电流（或阶跃电压）强迫作用，电容两端的电压 $v_{C}(t)$ 不发生跳变，即
$$v_C(0_+) = v_C(0_−)$$
+ 若无冲激电压（或阶跃电流）强迫作用，流经电感的电流 $i_{L}(t)$ 不发生跳变，即
$$i_L(0_+) = i_L(0_−)$$

##### 初始条件确定的数学方法

将 $e(t) = u(t)$ 代入微分方程，并**检查等式左右两边奇异函数的平衡**，推测 $r(t)$ 中包含的奇异函数的形式。这称为 **$\delta$ 函数匹配法**。

## 响应信号的分解

上述微分方程的求解结果 $r(t)$ 可以有多种分解方式。

```tx
| 分量 | 分解方式 | 含义 |
| :---- | :-------- | :---- |
| **自由响应 $r_{\mathrm{h}}(t)$** | 微分方程的求解 | 对应于**系统特征**，是求解微分方程得到的**齐次解**，满足 $$\sum\limits_{i=0}^n C_{i} \dfrac{\dif^{n-i}}{\dif t^{n-i}} r(t) = 0$$ |
| **强迫响应 $r_{\mathrm{p}}(t)$** | ^^             | 对应于**激励信号**，是求解微分方程得到的**特解**，满足 $$\sum\limits_{i=0}^n C_{i} \dfrac{\dif^{n-i}}{\dif t^{n-i}} r(t) = \sum\limits_{j=0}^m E_{j} \dfrac{\dif^{m-j}}{\dif t^{m-j}} e(t)$$   |
| **零输入响应 $r_{\mathrm{zi}}(t)$** | 系统响应的起因 | 由系统**原始储能**引起，满足 $$\sum\limits_{i=0}^n C_{i} \dfrac{\dif^{n-i}}{\dif t^{n-i}} r(t) = 0$$ |
| **零状态响应 $r_{\mathrm{zs}}(t)$** | ^^             | 由系统**激励信号**引起，满足 $$\sum\limits_{i=0}^n C_{i} \dfrac{\dif^{n-i}}{\dif t^{n-i}} r(t) = \sum\limits_{j=0}^m E_{j} \dfrac{\dif^{m-j}}{\dif t^{m-j}} e(t)$$ |
| 瞬态响应 | 响应信号的结果 | 系统在引入激励后短时间内的表现 |
| 稳态响应 | ^^             | 系统在引入激励后长时间内的表现 |
```

### 零输入响应和零状态响应

> [!definition] 零输入响应与零状态响应
> 没有外加激励信号的作用，只由起始状态（起始时刻系统储能）产生的响应称为**零输入响应**，记为 $r_{\mathrm{zi}}(t)$；没有起始状态的作用，只由外加激励信号产生的响应称为**零状态响应**，记为 $r_{\mathrm{zs}}(t)$。零输入响应和零状态响应之和即为系统的总响应。 

零输入响应是**齐次解的一部分**，可展开为
$$r_{\mathrm{zi}}(t) = \sum\limits_{k=1}^n A_{\mathrm{zi}k} \e^{\alpha_{k} t}$$
其中系数 $A_{\mathrm{zi}k}$ 由**起始状态 $r_{\mathrm{zi}}(0_{-})$** 决定。
+ 对稳定的 LTI 系统，零输入响应在 $t \to +\infty$ 时趋于零，应**有 $\mathfrak{Re}\{ \alpha_{k} \} < 0$**，即特征根位于复平面左半边。
+ 零输入响应中的 $\alpha_{k}$ 称为**模式**，稳定的 LTI 系统的零输入响应沿多种模式**指数衰减**，不同的收敛模式对应不同的复指数函数 $\e^{\alpha_{k} t}$。

> [!danger] 自由响应与零输入响应
> 自由响应和零输入响应**都满足齐次方程**，其区别在于零输入响应的 $A_{\mathrm{zi}k}$ 是**起始状态**决定的，而自由响应的 $A_{k}$ 是**初始状态**决定的。零输入响应是自由响应的一部分。 
> 
> 若系统起始无储能，即 $0_{-}$ 状态为零，则**零输入响应为零**，但**自由响应可以不为零**，由激励信号与系统参数共同决定。

零状态响应包含**特解**和**齐次解的一部分**，可展开为
$$r_{\mathrm{zs}}(t) = \sum\limits_{k=1}^n A_{\mathrm{zs}k} \e^{\alpha_{k} t} + r_{\mathrm{p}}(t)$$
其中系数 $A_{\mathrm{zs}k}$ 由**激励信号 $e(t)$ 在零时刻的跳变**决定，特解 $r_{\mathrm{p}}(t)$ 按[[#求特解]]的方法由**激励信号的形式**决定。
+ 对稳定的 LTI 系统，零状态响应中的**齐次解部分**终将随 $t \to \infty$ 而趋于零。
+ 对于复指数信号 $e(t) = \e^{\alpha t}$，特解 $r_{\mathrm{p}}(t)$ 也是**相同模式**的**复指数信号**。

#### LTI 系统的特征函数

LTI 系统对 **从 $-\infty$ 即加入的理想复指数激励 $\e^{\beta t}u(t)$** 的响应是相同模式的复指数函数 $B \e^{\beta t}u(t)$，即
$$\e^{\beta t} \quad \xrightarrow{\text{LTI 系统}} \quad B \e^{\beta t}u(t)$$
故**复指数函数是 LTI 系统的特征函数**，$B$ 是系统的特征值。
+ **零输入响应**由复指数函数 $\e^{\alpha t}$ 组成，**模式 $\alpha_{k}$** 由系统决定；
+ 零时刻加入的复指数激励 $\e^{\beta t}u(t)$ 的**稳态零状态响应**是相同模式的复指数函数 $B\e^{\beta t}u(t)$，**特征值 $B$** 由系统决定。

#### 零输入线性和零状态线性

当起始状态为零时，系统的**零状态响应对应于激励信号呈线性**，称为**零状态线性**；当激励为零时，系统的**零输入响应对应于起始状态呈线性**，称为**零输入线性**。

仅以激励信号而论，上面讨论的**存在零输入响应**的系统均为**增量线性系统**，其全响应与激励不成线性关系，但任意两个输入的响应之差是两个输入之差的线性函数。

![[系统框图-增量线性系统.svg]]

### 冲激响应与阶跃响应

> [!definition] 冲激响应
> **冲激响应**是指系统对**单位冲激函数 $\delta(t)$** 的响应，记作 $h(t)$，即
> $$ h(t) = r(t) \big|_{e(t) = \delta(t)} $$

冲激信号作用下的**特解为零**，故冲激响应的主体是**齐次解**，兼有冲激信号导致的**冲激项**甚至**冲激项的各阶导数**，即其一般形式为
$$
h(t) = \sum\limits_{i=0}^m D_{i}\delta^{(i)}(t) + \left( \sum\limits_{k=1}^n A_{k} \e^{\alpha_{k} t} \right) u(t)
$$

> [!definition] 阶跃响应
> **阶跃响应**是指系统对**单位阶跃函数 $u(t)$** 的响应，记作 $g(t)$，即
> $$ g(t) = r(t) \big|_{e(t) = u(t)} $$

阶跃响应可以由冲激响应积分得到。

#### 由冲激响应求零状态响应

激励信号 $e(t)$ 可以[[信号#脉冲分量|脉冲分量]]形式分解为
$$
e(t) = \dint_{-\infty}^{+\infty} e(\tau) \delta(t - \tau) \dif\tau
$$
由 LTI 系统的叠加性、齐次性和时不变性，可以得到 **LTI 系统对激励信号 $e(t)$ 的零状态响应**为
$$
r(t) = \dint_{-\infty}^{+\infty} e(\tau) h(t - \tau) \dif\tau = e(t) * h(t)
$$

> [!theorem] 卷积的性质
> 卷积运算满足以下性质：
> + 代数性质——
> 	+ **交换律**，即 $f_{1}(t) * f_{2}(t) = f_{2}(t) * f_{1}(t)$
> 	+ **结合律**，即 $f_{1}(t) * (f_{2}(t) * f_{3}(t)) = (f_{1}(t) * f_{2}(t)) * f_{3}(t)$
> 	+ **分配律**，即 $f_{1}(t) * (f_{2}(t) + f_{3}(t)) = f_{1}(t) * f_{2}(t) + f_{1}(t) * f_{3}(t)$
> + 拓扑性质——
> 	$$p^i \left( f_{1}(t) * f_{2}(t) \right) = p^j f_{1}(t) * p^{i-j} f_{2}(t)$$
> 	+ 两信号卷积后的**导数**等于一个的导数与另一个的卷积，即 $\dfrac{\dif}{\dif t} \left( f_{1}(t) * f_{2}(t) \right) = \dfrac{\dif f_{1}(t)}{\dif t} * f_{2}(t) = f_{1}(t) * \dfrac{\dif f_{2}(t)}{\dif t}$；
> 	+ 两信号卷积后的**积分**等于一个的积分与另一个的卷积，即 $\dint_{-\infty}^{+\infty} f_{1}(t) * f_{2}(t) \dif t = \dint_{-\infty}^{+\infty} f_{1}(\tau) \dif \tau * f_{2}(t) = f_{1}(t) * \dint_{-\infty}^{+\infty} f_{2}(\tau) \dif \tau$；
> 	+ 特别地，**$f_{1}(t) * f_{2}(t) = \dfrac{\dif f_{1}(t)}{\dif t} * \dint_{-\infty}^{+\infty} f_{2}(\tau) \dif \tau$**。
> + 位移性质——
> $$f_{1}(t - T_{1}) * f_{2}(t - T_{2}) = (f_{1} * f_{2}) (t - T_{1} - T_{2})$$


# 连续时间系统频域分析

## Laplace 变换与系统分析

### 用 Laplace 变换解系统微分方程的一般步骤

#### 零起始状态

1. 建立**系统微分方程**
$$\sum\limits_{i=0}^n a_{i} \dfrac{\dif^i}{\dif t^i}r(t) = \sum\limits_{j=0}^m b_{j} \dfrac{\dif^j}{\dif t^j} e(t)$$
2. 对方程两边**同时进行 Laplace 变换**，化为代数方程
$$\sum\limits_{i=0}^n a_{i} s^i R(s) = \sum\limits_{j=0}^m b_{j} s^j E(s)$$
3. 解代数方程得到响应 $R(s)$
$$R(s) = \dfrac{\sum\limits_{j=0}^m b_{j}s^j}{\sum\limits_{i=0}^n a_{i}s^i} E(s) = \dfrac{B(s)}{A(s)}E(s)$$
4. 对 $R(s)$ 进行 **Laplace 逆变换**，得到**零起始状态响应** $r(t)$

#### 非零起始状态

1. 建立**系统微分方程**
$$\sum\limits_{i=0}^n a_{i} \dfrac{\dif^i}{\dif t^i}r(t) = \sum\limits_{j=0}^m b_{j} \dfrac{\dif^j}{\dif t^j} e(t)$$
2. 对方程两边**同时进行 Laplace 变换**，化为代数方程
$$\sum\limits_{i=0}^n a_{i} \left( s^i R(s) - \sum\limits_{k=0}^{i-1} s^{i-1-k} r^{(k)}(0_{-}) \right) = \sum\limits_{j=0}^m b_{j} s^j E(s)$$
整理得到
$$\underbrace{ \sum\limits_{i=0}^n a_{i} s^i }_{ A(s) } R(s) = \underbrace{ \sum\limits_{j=0}^m b_{j} s^j }_{ B(s) } E(s) + \underbrace{ \sum\limits_{i=0}^n a_{i} \sum\limits_{k=0}^{i-1} s^{i-1-k} r^{(k)}(0_{-}) }_{ C(s) }$$
3. 解代数方程得到响应 $R(s)$
$$R(s) = \underbrace{ \dfrac{B(s)}{A(s)}E(s) }_{ \text{零状态响应} } + \underbrace{ \dfrac{C(s)}{A(s)} }_{ \text{零输入响应} }$$
4. 对 $R(s)$ 进行 **Laplace 逆变换**，得到**非零起始状态响应** $r(t)$

### $\boldsymbol{s}$ 域电路元件模型

考察电路元件的**电压-电流关系**，在时域有
$$\begin{align}
& v_{R}(t) = R i_{R}(t) \\
& v_{L}(t) = L \dfrac{\dif}{\dif t} i_{L}(t) \\
& v_{C}(t) = \dfrac{1}{C} \int_{-\infty}^{t} i_{C}(\tau) \dif \tau
\end{align}$$
在复频域即有
$$\begin{align}
& V_{R}(s) = R I_{R}(s) &&&& I_{R}(s) = \dfrac{1}{R} V_{R}(s) \\
& V_{L}(s) = sLI_{L}(s) - Li_{L}(0_{-}) && \text{或} && I_{L}(s) = \dfrac{1}{sL} V_{L}(s) + \dfrac{1}{s} i_{L}(0_{-}) \\
& V_{C}(s) = \dfrac{1}{sC} I_{C}(s) + \dfrac{1}{s} v_{C}(0_{-}) &&&& I_{C}(s) = sCV_{C}(s) - Cv_{C}(0_{-})
\end{align}$$

> [!note]+ 说明
> 上面 $i_{L}(0_{-})$、$v_{C}(0_{-})$ 等是**初始条件**，可等效为**电流源**或**电压源**。

## 系统函数

> [!definition] 系统函数
> 系统**零状态响应**的 Laplace 变换与**激励**的 Laplace 变换之比称为 **[[系统函数]]**（或**网络函数**），以 $H(s)$ 表示，即
> $$H(s) = \dfrac{R(s)}{E(s)} = \dfrac{A(s)}{B(s)}$$
> 其中，$R(s)$ 为系统 $s$ 域的**零状态响应**，$A(s)$、$B(s)$ 来自[[#Laplace 变换 (LT)#零起始状态|零起始状态]]的系统方程。
>
> 如果 $E(s)$ 和 $R(s)$ 在同一端口，则称为**策动点函数**（driving point function）；否则，称为**传递函数**（transfer function）。

### $\boldsymbol{H(s)}$ 的零、极点分布与系统时域特性

Laplace 变换建立起时域和频域的对应关系，因此，系统函数的零、极点分布对应于系统的时域特性。

#### $\boldsymbol{h(t)}$ 的波形特征

设 $H(s)$ 由 $n$ 个**子系统 $H_i(s)$** 并联组成，每个子系统有唯一的**一阶极点 $p_i$**，即
$$
H(s) = \sum_{i=1}^n H_i(s) = \sum_{i=1}^n \dfrac{K_i}{s - p_i}
$$
则系统的**冲激响应**为
$$
h(t) = \mathscr{L}^{-1}\{H(s)\} = \sum_{i=1}^n K_i \e^{p_i t} u(t)
$$
其中 $p_{i}$ 可以是实数，也可以和 $p_j$ 构成一对共轭复数。

![[极点位置与原函数时域波形_1.png]]

![[极点位置与原函数时域波形_2.png]]

若 $p_{i}$ 是一个二阶极点，即
$$
H_{i}(s) = \dfrac{K_{i}}{(s - p_{i})^{2}} = K_{i} \dfrac{1}{s - p_{i}} \dfrac{1}{s - p_{i}}
$$
则
$$\begin{align}
h_{i}(t) &= K_{i} \mathscr{L}^{-1}\left\{\dfrac{1}{s - p_{i}}\right\} * \mathscr{L}^{-1}\left\{\dfrac{1}{s - p_{i}}\right\} \\
&= K_{i} \left( \e^{p_{i} t} u(t) \right)  * \left( \e^{p_{i} t} u(t) \right)  = K_{i} t \e^{p_{i} t} u(t)
\end{align}$$

![[极点位置与原函数时域波形_3.png]]

> [!theorem] 结论
> + 若系统函数 $H(s)$ 极点位于左半平面，则 $h(t)$ 波形为**衰减**形式；
> + 若一阶极点且位于虚轴上，则为**等幅**（常量或振荡）形式；
> + 其他情况（位于右半平面或二阶虚轴上）则为**增长**形式。

**极点**分布和时域波形形式有**明确的对应关系**，但**零点**分布不会对时域波形发生实质影响。

#### $\boldsymbol{r(t)}$ 的分解

系统响应 $R(s) = H(s)E(s)$ 的极点分别来自**系统 $H(s) = \dfrac{\prod\limits_{j=1}^m (s - z_{j})}{\prod\limits_{i=1}^n (s - p_{i})}$** 和**激励 $E(s) = \dfrac{\prod\limits_{l=1}^u (s - b_{l})}{\prod\limits_{k=1}^v (s - a_{k})}$**，即
$$
R(s) = H(s) E(s) = \sum\limits_{i=1}^{n} \dfrac{K_{i}}{s - p_{i}} + \sum\limits_{k=1}^{m} \dfrac{W_{k}}{s - a_{k}}
$$
对应地，系统响应 $r(t)$ 可分解为**自由响应** $r_{\mathrm{f}}(t)$ 和**强迫响应** $r_{\mathrm{p}}(t)$，即
$$
r(t) = \mathscr{L}^{-1}\{R(s)\} = \underbrace{ \sum\limits_{i=1}^{n} K_{i} \e^{p_{i} t} }_{ r_{\mathrm{f}}(t) } + \underbrace{ \sum\limits_{k=1}^{m} W_{k} \e^{a_{k} t} }_{ r_{\mathrm{p}}(t) }
$$
自由响应的形式只与系统函数的极点有关，而强迫响应的形式只与激励的极点有关。

### $\boldsymbol{H(s)}$ 的零、极点分布与系统频响特性

使用**正弦激励源** $E(s) = \dfrac{A\omega_{0}}{s^{2} + \omega_{0}^{2}}$ 激励一个 **LTI 系统**，则系统响应为
$$
R(s) = H(s) E(s) = \dfrac{K_{-\I\omega_{0}}}{s + \I\omega_{0}} + \dfrac{K_{\I\omega_{0}}}{s - \I\omega_{0}} + \sum\limits_{i=1}^{n} \dfrac{K_{i}}{s - p_{i}}
$$
前两项来自于激励的极点，表示 $r(t)$ 中**含有频率为 $\omega_{0}$ 的振荡**成分，系数为
$$\begin{align}
K_{\I\omega_{0}}^* = K_{-\I\omega_{0}} = (s + \I\omega_{0}) H(s) E(s) \bigg|_{s = -\I\omega_{0}} = \dfrac{A}{-2\I} H(-\I\omega_{0})
\end{align}$$
假设 $h(t)$ 是实的，则 $H(-\I\omega_{0}) = H^*(\I\omega_{0}) = H_{0} \e^{-\I\varphi_{0}}$，上述两项在时域即
$$\begin{align}
r'(t) &= \mathscr{L}^{-1} \left\{ \dfrac{K_{-\I\omega_{0}}}{s + \I\omega_{0}} + \dfrac{K_{\I\omega_{0}}}{s - \I\omega_{0}} \right\} = \mathscr{L}^{-1} \left\{ \dfrac{A}{-2\I} \left( \dfrac{H(-\I\omega_{0})}{s + \I\omega_{0}} - \dfrac{H(\I\omega_{0})}{s - \I\omega_{0}} \right)  \right\} \\
&= \mathscr{L}^{-1} \left\{ \dfrac{AH_{0}}{-2\I} \left( \dfrac{\e^{-\I\varphi_{0}}}{s + \I\omega_{0}} - \dfrac{\e^{\I\varphi_{0}}}{s - \I\omega_{0}} \right)  \right\} \\
&= \dfrac{AH_{0}}{-2\I} \left( \e^{-\I\omega_{0} t} \e^{-\I\varphi_{0}} - \e^{\I\omega_{0} t} \e^{\I\varphi_{0}} \right) = A H_{0} \sin(\omega_{0} t + \varphi_{0})
\end{align}$$

## 系统的物理可实现性

### Paley-Wiener 准则

**Paley-Wiener 准则**是一个重要的系统可实现性准则，给出了一个系统模型的**幅度特性**是否可以在物理上实现的**必要条件**。

> [!theorem] Paley-Wiener 准则
> 一个非全零的线性时不变系统模型 $e(t) \mapsto r(t)$ 是物理可实现的，**仅当**其系统函数 $H(s)$ 满足
> $$\int_{-\infty}^{+\infty} \dfrac{\big| \ln|H(\I\omega)| \big|}{1 + \omega^2} \dif\omega < \infty$$

Paley-Wiener 准则说明了**理想滤波器**的幅频特性不能在物理上实现：
+ $|H(\I\omega)|$ **不能**在任意 $\omega$ 的**连续区间**上**为 $0$**，否则 $\displaystyle \int_{-\infty}^\infty \big| \ln|H(\I\omega)| \big| \dif \omega \to \infty$；
+ $\omega \to \infty$ 时，$|H(\I\omega)| \to 0$ 的**衰减速度受限**，如 $|H(\I\omega)| \sim \e^{-\omega^2}$ 不满足。

### 可实现系统 $H(\I\omega)$ 实部和虚部的关系

对**因果系统**，如果它是**稳定**的，则 Fourier 变换存在
$$
H(\I\omega) = \mathcal{F}\{ h(t) \} = R(\I\omega) + \I X(\I\omega)
$$
故有
$$
\begin{align}
h(t) &= h(t) u(t) = h(t) \mathop{\mathrm{sgn}}(t) \\
H(\I\omega) &= \dfrac{1}{2\pi} H(\I\omega) * \mathcal{F}\{\mathrm{sgn}(t)\} \\
R(\I\omega) + \I X(\I\omega) &= \dfrac{1}{2\pi} \left(  \left( R(\I\omega) + \I X(\I\omega) \right) * \dfrac{2}{\I\omega}  \right) \\
&= - \dfrac{\I}{\pi} \dint_{-\infty}^\infty \dfrac{R(\lambda)}{\omega-\lambda} \dif \lambda + \dfrac{1}{\pi} \dint_{-\infty}^\infty \dfrac{X(\lambda)}{\omega-\lambda} \dif \lambda
\end{align}
$$
即
$$
R(\I\omega) = \dfrac{1}{\pi} \dint_{-\infty}^\infty \dfrac{X(\lambda)}{\omega-\lambda} \dif \lambda, \qquad
X(\I\omega) = - \dfrac{1}{\pi} \dint_{-\infty}^\infty \dfrac{R(\lambda)}{\omega-\lambda} \dif \lambda
$$

> [!definition] Hilbert 变换
> 信号 $f(x)$ 的 **Hilbert 变换**定义为
> $$\mathcal{H}\left\{ f(x) \right\} = \hat{f}(x) = \dfrac{1}{\pi} \dint_{-\infty}^\infty \dfrac{f(y)}{x-y} \dif y = f(x) * \dfrac{1}{\pi x} $$
> 对应地，**Hilbert 逆变换**定义为
> $$\mathcal{H}^{-1}\left\{ \hat{f}(x) \right\} = f(x) = - \dfrac{1}{\pi} \dint_{-\infty}^\infty \dfrac{\hat{f}(y)}{x-y} \dif y = \hat{f}(x) * \left( - \dfrac{1}{\pi x} \right) $$

因果稳定系统的系统函数**实部是虚部的 Hilbert 变换**。


# 连续时间信号处理的 Fourier 分析

## 传输与滤波

### 无失真传输

#### 线性系统无失真传输条件

**无失真传输**期望响应 $r(t)$ 与激励 $e(t)$ 之间**形状相同**，而**幅度可改变、延时可增加**，即
$$
r(t) = K e(t-t_{0})
$$
取 [[#Fourier 变换 (FT)]]，得到
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
$$\begin{align}
F(\omega) &= \dfrac{1}{2\pi} G(\omega) * \left( \pi\delta(\omega + \omega_{0}) + \pi\delta(\omega - \omega_{0}) \right) \\
&= \dfrac{1}{2} \left( G(\omega + \omega_{0}) + G(\omega - \omega_{0}) \right) 
\end{align}$$

#### 解调过程

1. 用本地载波乘以调制信号
$$
g_{0}(t) = f(t) \cos(\omega t)
$$
即将频谱搬回原来的位置
$$\begin{align}
G_{0}(\omega) &= \dfrac{1}{2} \left( F(\omega + \omega_{0}) + F(\omega - \omega_{0}) \right) \\
&= \dfrac{1}{2} G(\omega) + \dfrac{1}{4} \left( G(\omega + 2\omega_{0}) + G(\omega - 2\omega_{0}) \right)
\end{align}$$

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

**[[#Fourier 级数 (FS)#周期矩形脉冲信号|周期矩形脉冲信号]]**的 Fourier 级数的系数为
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


# 离散时间系统频域分析

## 离散时间系统 $z$ 域分析

### 常系数线性差分方程的 $z$ 域求解

离散线性时不变系统的输入输出关系为
$$
\sum\limits_{k=0}^{N} a_{k} y(n-k) = \sum\limits_{r=0}^{M} b_{r} x(n-r)
$$
对其进行 $z$ 变换，得到
$$
\sum\limits_{k=0}^{N} a_{k} z^{-k} \left( Y(z) + \sum\limits_{l=-k}^{-1} y(l) z^{-l} \right) = \sum\limits_{r=0}^{M} b_{r} z^{-r} \left( X(z) + \sum\limits_{m=-r}^{-1} x(m) z^{-m} \right)
$$

#### 零输入响应

零输入情况下，$\sum\limits_{k=0}^{N} a_{k} z^{-k} \left( Y(z) + \sum\limits_{l=-k}^{-1} y(l) z^{-l} \right) = 0$，即
$$
Y(z) = -\dfrac{\sum\limits_{k=0}^{N} \left( a_{k} z^{-k} \sum\limits_{l=-k}^{-1} y(l) z^{-l} \right)}{\sum\limits_{k=0}^{N} a_{k} z^{-k}}
$$
**零输入响应**即为 $y_{\mathrm{zi}}(n) = \mathscr{Z}^{-1} \left\{ Y(z) \right\}$，由起始状态 $y(l)$ 确定。

#### 零状态响应

起始状态 $y(l) = 0$（$-N \le l \le -1$），即处于零状态。若激励为**因果序列**，则
$$
\sum\limits_{k=0}^{N} a_{k} z^{-k} Y(z) = \sum\limits_{r=0}^{M} b_{r} z^{-r} X(z) 
$$
解得
$$
Y(z) = \dfrac{\sum\limits_{r=0}^{M} b_{r} z^{-r}}{\sum\limits_{k=0}^{N} a_{k} z^{-k}} X(z) = H(z) X(z)
$$
**零状态响应**即为 $y_{\mathrm{zs}}(n) = \mathscr{Z}^{-1} \left\{ H(z)X(z) \right\}$，由输入 $x(n)$ 确定。

### 离散时间系统的系统函数

由因果序列激励离散时间系统的零状态响应分析，得到**系统函数**为
$$
H(z) = \dfrac{Y(z)}{X(z)} = \dfrac{\sum\limits_{r=0}^{M} b_{r} z^{-r}}{\sum\limits_{k=0}^{N} a_{k} z^{-k}} 
$$
其为系统**单位样值响应** $h(n)$ 的 $z$ 变换，即 $H(z) = \sum\limits_{n=0}^{\infty} h(n) z^{-n}$。对上式因式分解得到
$$
H(z) = A \dfrac{\prod\limits_{r=1}^M (1 - z_{r} z^{-1})}{\prod\limits_{k=1}^N (1 - p_{k} z^{-1})} = A \dfrac{\prod\limits_{r=1}^M (z - z_{r})}{\prod\limits_{k=1}^N (z - p_{k})} z^{N-M} 
$$
其中 $z_{r}$ 为**零点**，$p_{k}$ 为**极点**。

#### 由极点分布判断 $h(n)$ 波形特征

![[H(z)的极点和h(n)波形特征的对应关系.png]]

#### 由极点分布判断系统因果性

系统因果的充要条件是 $h(n) = h(n) u(n)$，即 $H(z) = \sum\limits_{k=0}^{\infty} h(k) z^{-k}$，故其**收敛域应包含无穷远点**。

#### 由极点分布判断系统稳定性

系统稳定的充要条件是 $h(n)$ 的**绝对可和性**，即 $\sum\limits_{n=0}^{\infty} |h(n)| < \infty$。

因此 $H(z)$ 的**收敛域应包含单位圆**。


## 离散时间系统的频率响应特性

### 离散时间系统频响特性的意义

离散时间系统的**频率响应特性**描述了系统对**不同频率**信号的响应情况。

考察**单频信号 $x(n) = A\sin(n\omega)$** 激励**稳定**的离散时间系统的响应 $y(n)$，有
$$
\begin{align}
X(z) &= \dfrac{Az \sin \omega}{z^2 - 2z\cos\omega + 1} = \dfrac{Az \sin \omega}{(z - \e^{\I\omega})(z - \e^{-\I\omega})} \\
Y(z) &= X(z) H(z) = \dfrac{Az \sin \omega}{(z - \e^{\I\omega})(z - \e^{-\I\omega})} H(z) 
= \dfrac{az}{z - \e^{\I\omega}} + \dfrac{bz}{z - \e^{-\I\omega}} + \sum\limits_{m=1}^M \dfrac{A_{m} z}{z - z_{m}}
\end{align}
$$
其中 $H(z)$ 为系统的 $z$ 变换，$z_{m}$ 为**系统的极点**。

待定系数可得
$$
\begin{align}
a &= Y(z) \dfrac{z - \e^{\I\omega}}{z} \Bigg|_{z=\e^{\I\omega}} = \dfrac{A \sin \omega}{\e^{\I\omega} - \e^{-\I\omega}} H(\e^{\I\omega}) = \dfrac{A}{2\I} H(\e^{\I\omega}) \\
b &= Y(z) \dfrac{z - \e^{-\I\omega}}{z} \Bigg|_{z=\e^{-\I\omega}} = \dfrac{A \sin \omega}{\e^{-\I\omega} - \e^{\I\omega}} H(\e^{-\I\omega}) = -\dfrac{A}{2\I} H(\e^{-\I\omega})
\end{align}
$$
因此
$$
\begin{align}
Y(z) &= \dfrac{A}{2\I} \left( H(\e^{\I\omega}) \dfrac{z}{z - \e^{\I\omega}} - H(\e^{-\I\omega}) \dfrac{z}{z - \e^{-\I\omega}} \right) + \sum\limits_{m=1}^M \dfrac{A_{m} z}{z - z_{m}} \\
&= \dfrac{A|H(\e^{\I\omega})|}{2\I} \left( \dfrac{z \e^{\I\varphi(\omega)}}{z - \e^{\I\omega}} - \dfrac{z \e^{-\I\varphi(\omega)}}{z - \e^{-\I\omega}} \right) + \sum\limits_{m=1}^M \dfrac{A_{m} z}{z - z_{m}}
\end{align}
$$
做**逆 $z$ 变换**，得到
$$
\begin{align}
y(n) &= \dfrac{A|H(\e^{\I\omega})|}{2\I} \left( \e^{\I(n\omega + \varphi(\omega))} - \e^{-\I(n\omega + \varphi(\omega))} \right) u(n) + \sum\limits_{m=1}^M A_{m} z_{m}^{n} u(n) \\
&= \underbrace{ A|H(\e^{\I\omega})| \sin(n\omega + \varphi(\omega)) u(n) }_{ y_{\mathrm{ss}}(n) } + \sum\limits_{m=1}^M A_{m} z_{m}^{n} u(n)
\end{align}
$$

这一**稳态响应**相比于输入信号，
+ 幅度放大 $|H(\e^{\I\omega})|$ 倍，即**幅频响应**，
+ 相位延迟 $\varphi(\omega)$，即**相频响应**。

### 频响特性的几何确定法

系统函数的**零极点**表示为
$$
H(z) = \dfrac{\prod\limits_{r=1}^M (1 - z_{r}z^{-1})}{\prod\limits_{k=1}^N (1 - p_{k}z^{-1})} = \dfrac{\prod\limits_{r=1}^M (z - z_{r})}{\prod\limits_{k=1}^N (z - p_{k})} z^{N-M}
$$
代入 $z = \e^{\I\omega}$ 等同于连续时间系统中代入 $s = \I\omega$，得到
$$
H(\e^{\I\omega}) = \dfrac{\prod\limits_{r=1}^M (\e^{\I\omega} - z_{r})}{\prod\limits_{k=1}^N (\e^{\I\omega} - p_{k})} \e^{\I(N-M)\omega} = |H(\e^{\I\omega})| \e^{\I\varphi(\omega)}
$$

引入**几何分析**，将 $(\e^{\I\omega} - z_{r})$、$(\e^{\I\omega} - p_{k})$ 视为**复平面上的向量**，分别记作 $A_{r} \e^{\I\psi_{r}}$、$B_{k} \e^{\I\theta_{k}}$，则
$$
|H(\e^{\I\omega})| = \dfrac{\prod\limits_{r=1}^M A_{r}}{\prod\limits_{k=1}^N B_{k}}, \qquad \varphi(\omega) = \sum\limits_{r=1}^M \psi_{r} - \sum\limits_{k=1}^N \theta_{k} + (N-M)\omega
$$

![[频响特性的几何确定法.png]]

由图可知，$\omega$ 处的频率响应对应于**各零极点到单位圆上 $\omega$ 处向量**的**模长比**和**幅角差**。

## 数字滤波器的基本原理

用数字方法按预定要求对输入信号进行处理，**改变信号的频谱特性**，达到**滤波**的目的。数字滤波器是「数字信号处理」课程的主要内容。

![[数字滤波器的基本原理.png]]

### A/D 抽样

输入**带宽受限于 $-\omega_{\mathrm{m}} < \omega < \omega_{\mathrm{m}}$** 的连续信号 $x(t)$，令 $X(\omega) = \mathcal{F}\{ x(t) \}$，对其以周期 $T$ 进行冲激抽样，得到抽样信号变换为
$$
\begin{align}
\mathcal{F}\{ x(t)\delta_{T}(t) \} &= \mathcal{F}\left\{ \sum\limits_{n=-\infty}^{\infty} x(nT) \delta(t-nT) \right\}  \\
&= \sum\limits_{n=-\infty}^{\infty} x(nT) \mathcal{F}\{ \delta(t-nT) \} 
= \sum\limits_{n=-\infty}^{\infty} x(nT) \e^{-\I n \omega T} \\
&= \mathrm{DTFT} \{ x(nT) \} =: \widehat{X}(\e^{\I\omega T}) 
\end{align}
$$
另一方面
$$
\begin{align}
\mathcal{F}\{ x(t) \delta_{T}(t) \} &= \dfrac{1}{2\pi} X(\omega) * \dfrac{2\pi}{T} \sum\limits_{n=-\infty}^{\infty} \delta(\omega - n\omega_{\mathrm{s}}) \\
&= \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} X(\omega - n\omega_{\mathrm{s}}), \qquad \omega_{\mathrm{s}} = \dfrac{2\pi}{T} \ge 2\omega_{\mathrm{m}}
\end{align}
$$
因而**数字域**中信号的**频谱**为
$$
\widehat{X}(\e^{\I\omega T}) = \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} X(\omega - n\omega_{\mathrm{s}})
$$
其中，$\omega T$ 为**数字域的频率变量**，记为 $\varOmega$；$\omega_{\mathrm{s}}$ 为**数字域的采样频率**。

### 数字滤波

数字滤波器的**输入**为
$$
x(n) = x(t) \Big|_{t=nT} ,\qquad
\widehat{X}(\e^{\I\varOmega}) = \dfrac{1}{T} \sum\limits_{n=-\infty}^{\infty} X\left( \dfrac{\varOmega}{T} - n\omega_{\mathrm{s}} \right)
$$
输入即为
$$
\widehat{Y}(\e^{\I\varOmega}) = \widehat{H}(\e^{\I\varOmega}) \widehat{X}(\e^{\I\varOmega})
$$
其中 $\widehat{H}(\e^{\I\varOmega}) = \widehat{H}(z) \Big|_{z=\e^{\I\varOmega}}$ 为**数字滤波器的频率响应**。

### D/A 重建

记模拟低通滤波器的传递函数为 $G(\omega)$，则输出信号为
$$
\begin{align}
Y_{\mathrm{o}}(\omega) &= G(\omega) \widehat{Y}(\e^{\I\varOmega}) = G(\omega) \widehat{H}(\e^{\I\varOmega}) \widehat{X}(\e^{\I\varOmega})  \\
&= \dfrac{1}{T} G(\omega) \widehat{H}(\e^{\I\omega T}) \sum\limits_{n=-\infty}^{\infty} X(\omega - n\omega_{\mathrm{s}})
\end{align}
$$

![[数字滤波器的DA重建.png]]

假定模拟低通滤波器是一个理想的低通滤波器，
$$
G(\omega) = \begin{cases}
1, & |\omega| < \omega_{\mathrm{c}} \\
0, & |\omega| \ge \omega_{\mathrm{c}}
\end{cases}
$$
且 $\omega_{\mathrm{m}} < \omega_{\mathrm{c}} < \omega_{\mathrm{s}} - \omega_{\mathrm{m}}$，则
$$
Y_{\mathrm{o}}(\omega) = \dfrac{1}{T} \widehat{H}(\e^{\I\omega T}) X(\omega)
$$




# 离散时间系统时域分析

## 离散时间信号的数学表示

对模拟信号等间隔 $T$ 采样，得到一组**序列值的组合**记为
$$
\{ x(n) \}, \quad n = 0, \pm 1, \pm 2, \cdots
$$
称为**序列**。注意对 $n$ 非整数时无定义。

### 序列的基本运算

#### 序列的加法、乘法、数乘

对序列内所有值可做**加法** $z(n) = x(n) + y(n)$、**乘法** $z(n) = x(n) \cdot y(n)$、**数乘** $z(n) = a \cdot x(n)$。

#### 序列的移位、反褶、压扩

序列的**移位**分为**右移/后移**
$$
z(n) = x(n - m), \quad m > 0
$$
和**左移/前移**
$$
z(n) = x(n + m), \quad m > 0
$$

序列的**反褶**为
$$
z(n) = x(-n)
$$

序列的**压扩**为
$$
z(n) = x(an), \quad a > 0
$$
其中 $a > 1$ 为**压缩**，$0 < a < 1$ 为**扩展**。压缩中会存在**值的舍弃**，扩展中会存在 **0 的插入**。

#### 序列的累加与差分

序列的**累加**即求至 $n$ 项的和
$$
z(n) = \sum\limits_{k=-\infty}^{n} x(k)
$$

序列的**差分**可定义为
+ **前向差分**：$\Delta x(n) = x(n+1) - x(n)$
+ **后向差分**：$\nabla x(n) = x(n) - x(n-1)$

序列有**高阶差分**，递推地定义为
$$\begin{align}
&\Delta^m x(n) = \Delta \left(\Delta^{m-1} x(n)\right),\\
&\nabla^m x(n) = \nabla \left(\nabla^{m-1} x(n)\right), \quad m = 2, 3, \cdots
\end{align}$$

### 常用的典型序列

#### 单位样值信号

**单位样值信号**对应于连续时间的**[[信号#单位冲激信号 (Unit impulse signal)|单位冲激信号]]** $\delta(t)$，即
$$
\delta(n) = \begin{cases}
1, & n = 0,\\
0, & \text{elsewhere}
\end{cases}
$$
但在离散时间中，单位样值信号在 $n = 0$ 处取**有限值**为 $1$。

> [!theorem] 单位样值信号的筛选特性
> 单位样值信号 $\delta(n)$ 具有类似 $\delta(t)$ 的**筛选特性**，即对任意序列 $x(n)$，有
> $$x(n) \delta(n-m) = x(m) \delta(n-m) = \begin{cases}
> x(m), & n = m,\\
> 0, & \text{elsewhere}
> \end{cases}$$

^2e3750

#### 单位阶跃序列

**单位阶跃序列**对应于连续时间的**[[信号#单位阶跃信号 (Unit step signal)|单位阶跃信号]]** $u(t)$，即
$$
u(n) = \begin{cases}
1, & n \ge 0,\\
0, & \text{elsewhere}
\end{cases}
$$
其在 $n = 0$ 处取**有限值为 $1$**，而非 $\dfrac{1}{2}$。

> [!theorem] 单位样值信号与单位阶跃序列的关系
> **单位样值信号 $\delta(n)$** 与**单位阶跃序列 $u(n)$** 之间有如下关系：
> + $\delta(n) = u(n) - u(n-1)$,
> + $u(n) = \sum\limits_{k=0}^{n} \delta(n - k)$。

^3f41ad

#### 矩形序列、斜变序列、单边指数序列

基于单位阶跃序列 $u(n)$，可以定义一些常用的序列，如**矩形序列**为
$$
R_{N}(n) = \begin{cases}
1, & 0 \le n < N,\\
0, & \text{elsewhere}
\end{cases}
= u(n) - u(n-N)
$$
**斜变序列**为
$$
x(n) = \begin{cases}
n, & n \ge 0,\\
0, & \text{elsewhere}
\end{cases}
= nu(n)
$$
**单边指数序列**为
$$
x(n) = \begin{cases}
\alpha^n, & n \ge 0,\\
0, & \text{elsewhere}
\end{cases} = \alpha^n u(n), \quad
\alpha \neq 0, \pm1
$$

### 序列的分解表示

由上面[[#^3f41ad|单位样值信号与单位阶跃序列的关系]]可知，任意序列可表示为**加权、延迟的单位脉冲之和**，即
$$
x(n) = \sum\limits_{k=-\infty}^{\infty} x(k) \delta(n - k)
$$

## 离散时间系统的数学模型

离散时间系统的数学模型可以用**差分方程**来描述，对于通常的**线性时不变系统（LTI 系统）**，表示为**常系数线性差分方程**：
$$
\sum\limits_{k=0}^{N} a_{k} y(n-k) = \sum\limits_{r=0}^{M} b_{r} x(n-r)
$$

### 常系数线性差分方程的时域求解

1. 求解对应齐次方程 $\sum\limits_{k=0}^{N} a_{k} y(n-k) = 0$ 的**特征方程**，得到差分方程的**特征根**
$$
\sum\limits_{k=0}^{N} a_{k} \alpha^{n-k} = 0
\quad \Longrightarrow \quad
\alpha = \alpha_{1}, \alpha_{2}, \cdots, \alpha_{N}
$$
据此确定**齐次解**的形式
$$
y(n) = \sum\limits_{k=1}^{N} C_{k} \alpha_{k}^{n} u(n)
$$
2. 将激励代入方程右端得到**自由项**，据此形式确定**特解** $D(n)$ 的形式，回代求解特解系数。
	+ 若自由项为常数，则特解形式为 $D(n) = D_{0}$；
	+ 若自由项为多项式，则特解形式为相同次数的 $D(n) = D_{0} + D_{1} n + D_{2} n^2 + \cdots + D_{M} n^{M}$；
	+ 若自由项为指数 $\beta^{n}$，其中 $\beta$ 不与齐次解的 $\alpha_{k}$ 相同，则特解形式为 $D(n) = D_{0} \beta^{n}$；
	+ 若自由项为指数 $\alpha_{k}^{n}$，其中 $\alpha_{k}$ 为齐次解的一特征根，则特解形式为 $D(n) = D_{0} n \alpha_{k}^{n}$。 
3. 将齐次解与特解相加得到**通解**
$$
y(n) = \sum\limits_{k=1}^{N} C_{k} \alpha_{k}^{n} u(n) + D(n)
$$
代入边界条件求解齐次解中的常数。

#### 自由响应与强迫响应

完全响应中，**齐次解**称为**自由响应**，**特解**称为**强迫响应**。 

#### 零状态响应与零输入响应

**零输入响应** $y_{\mathrm{zi}}(n)$ 是指系统在无输入时的响应，是系统**对应齐次差分方程的解**，即
$$
y_{\mathrm{zi}}(n) = \sum\limits_{k=1}^{N} C_{\mathrm{zi},k} \alpha_{k}^{n} u(n)
$$
**零状态响应** $y_{\mathrm{zs}}(n)$ 是指系统在无初始条件时的响应，由**完全响应**与**零输入响应**之差计算。

### 离散时间系统的单位样值响应

离散时间系统的单位样值响应是指系统对单位样值信号 $\delta(n)$ 的响应，记为 $h(n)$。

由[[#^2e3750|样值信号的筛选特性]]，系统对激励 $x(n)$ 的响应 $y(n)$ 可表示为
$$
y(n) = \sum\limits_{k=-\infty}^{\infty} x(k) h(n-k) = x(n) * h(n)
$$
其中 $*$ 表示**卷积**（卷积和）运算。

### 解卷积（反卷积）

解卷积是指从输出 $y(n)$ 和输入 $x(n)$ 中恢复系统的单位样值响应 $h(n)$，即求解
$$
\begin{pmatrix}
y(0) \\ y(1) \\ \vdots \\ y(N-1)
\end{pmatrix}
= \begin{pmatrix}
h(0) \\
h(1) & h(0) \\
\vdots & \vdots & \ddots \\
h(N-1) & h(N-2) & \cdots & h(0)
\end{pmatrix}
\begin{pmatrix}
x(0) \\ x(1) \\ \vdots \\ x(N-1)
\end{pmatrix}
$$

在 $h(n)$ **离散有限**的情况下，可以通过**矩阵求逆**或**最小二乘法**等方法求解。

## 离散信号的相关特性

### 互相关函数

**互相关函数**描述两个离散信号之间的相关性，定义为
$$
R_{xy}(m) = \sum\limits_{n=-\infty}^{\infty} x(n) y(n-m) = x(n) * y(-n-m)
$$
其中 $m$ 为**延迟参数**。

### 自相关函数

特别地，使用**自相关函数**描述离散信号自身的相关性，定义为
$$
R_{xx}(m) = \sum\limits_{n=-\infty}^{\infty} x(n) x(n-m) = x(n) * x(-n-m)
$$
其中 $m$ 为**延迟参数**。



# 信号的相关性分析

## 信号矢量空间

### 范数与线性赋范空间

> [!definition] 范数
> 对矢量空间 $\mathbb{S}$ 中的元素 $x$，实函数 **$\|x\|$** 称为**范数**，如果它满足以下条件：
> + 对任意 $x \in \mathbb{S}$，$\|x\| \ge 0$，当且仅当 $x=0$ 时 $\|x\| = 0$；
> + 对任意正标量 $\alpha$ 和任意 $x \in \mathbb{S}$，$\|\alpha x\| = \alpha \|x\|$；
> + 对任意 $x,y \in \mathbb{S}$，$\|x+y\| \le \|x\| + \|y\|$。

> [!definition] 线性赋范空间
> 如果 $\mathbb{S}$ 是一个线性矢量空间，$\|\cdot\|$ 是定义在 $\mathbb{S}$ 上的范数，则称 $\mathbb{S}$ 为**线性赋范空间**，记作 **$(\mathbb{S}, \|\cdot\|)$**。

范数有多种定义方式。

#### Euclidean 范数

> [!definition] Euclidean 范数
> **Euclidean 范数**以「$\sqrt{ \sum |\cdot|^2 }$」的形式定义：
> + 对于 **$n$ 维矢量** $\v{x} = (x_1, x_2, \cdots, x_n)^{\mathrm{T}} \in \mathbb{R}^n$，Euclidean 范数定义为
> $$ \|\v{x}\|_2 = \sqrt{\sum\limits_{n=1}^N |x_{n}|^2} = \sqrt{\v{x}^{\mathrm{T}} \v{x}} $$
> + 对于**连续信号** $x(t) \in \mathscr{C}^1$，Euclidean 范数定义为
> $$ \|x(t)\|_2 = \sqrt{\int_{-\infty}^{+\infty} |x(t)|^2 \dif t} $$

#### $l_{p}$ 范数

> [!definition] $l_{p}$ 范数
> **$l_{p}$ 范数**以「$(\sum |\cdot|^p)^{1/p}$」的形式定义：
> + 对于 **$n$ 维矢量** $\v{x} = (x_1, x_2, \cdots, x_n)^{\mathrm{T}} \in \mathbb{R}^n$，$l_{p}$ 范数定义为
> $$ \|\v{x}\|_p = \left( \sum\limits_{n=1}^N |x_{n}|^p \right)^{1/p} $$
> + 对于**连续信号** $x(t) \in \mathscr{C}^1$，$l_{p}$ 范数定义为
> $$ \|x(t)\|_p = \left( \int_{-\infty}^{+\infty} |x(t)|^p \dif t \right)^{1/p} $$

由上面记号也可看出，**[[#Euclidean 范数]]即是 $l_{2}$ 范数**。

特别地，有**无穷范数**（$l_{\infty}$ 范数）：
+ 对于 **$n$ 维矢量** $\v{x} = (x_1, x_2, \cdots, x_n)^{\mathrm{T}} \in \mathbb{R}^n$，无穷范数定义为
$$ \|\v{x}\|_{\infty} = \max\limits_{1 \le n \le N} |x_{n}| $$
+ 对于**连续信号** $x(t) \in \mathscr{C}^1$，无穷范数定义为
$$ \|x(t)\|_{\infty} = \max\limits_{-\infty < t < +\infty} |x(t)| $$

### 内积与内积空间

> [!definition] 内积
> 对标量域 $\mathbb{R}$ 上定义的矢量空间 $\mathbb{S}$，函数 **$\langle \cdot, \cdot \rangle \colon \mathbb{S} \times \mathbb{S} \to \mathbb{R}$** 称为**内积**，如果它满足以下条件：
> + 对任意 $x,y \in \mathbb{S}$，$\langle x,y \rangle = \langle y,x \rangle$；
> + 对任意 $x,y \in \mathbb{S}$，$a \in \mathbb{R}$，$\langle ax,y \rangle = a \langle x,y \rangle$；
> + 对任意 $x,y,z \in \mathbb{S}$，$\langle x+y,z \rangle = \langle x,z \rangle + \langle y,z \rangle$；
> + 对任意 $x \in \mathbb{S}$，$\langle x,x \rangle \ge 0$，当且仅当 $x=0$ 时 $\langle x,x \rangle = 0$。

> [!definition] 内积空间
> 如果 $\mathbb{S}$ 是一个线性矢量空间，$\langle \cdot, \cdot \rangle$ 是定义在 $\mathbb{S}$ 上的内积，则称 $\mathbb{S}$ 为**内积空间**。

内积描述两矢量的相对位置，即**两信号的相对关系**。

#### 实空间 Euclidean 内积

> [!definition] 实空间 Euclidean 内积
> + **离散情形**：对于 **$n$ 维矢量** $\v{x}, \v{y} \in \mathbb{R}^n$，**Euclidean 内积**定义为
> $$ \langle \v{x}, \v{y} \rangle = \sum\limits_{n=1}^N x_{n} y_{n} = \v{x}^{\mathrm{T}} \v{y} $$
> + **连续情形**：对于**连续信号** $x(t), y(t) \in \mathscr{C}^1$，**Euclidean 内积**定义为
> $$ \langle x(t), y(t) \rangle = \int_{-\infty}^{+\infty} x(t) y(t) \dif t $$

#### 内积空间的范数

> [!definition] 内积空间的范数
> 如果 $\mathbb{S}$ 是一个内积空间，则对于任意 $x \in \mathbb{S}$，定义
> $$ \|x\| = \sqrt{\langle x,x \rangle} $$
> 为该内积空间的**诱导范数**。

### Cauchy-Schwarz 不等式

> [!theorem] Cauchy-Schwarz 不等式
> 对于内积空间 $\mathbb{S}$ 中的任意 $x,y \in \mathbb{S}$，有
> $$ |\langle x,y \rangle|^2 \le \langle x,x \rangle \langle y,y \rangle $$

^4e145c

Cauchy-Schwarz 不等式表明，**能量受限**（即 $\langle x,x \rangle < +\infty$）的信号之间的**内积存在**，这类信号简称为**能量信号**。

## 信号的正交函数分解

### 信号的正交性

用 $c_{12}f_{2}(t)$ 在 $(t_{1},t_{2})$ 上表示 $f_{1}(t)$，在**最小二乘意义下**的**代价函数**为
$$
\begin{align}
\varepsilon &= \dint_{t_{1}}^{t_{2}} \left( f_{1}(t) - c_{12}f_{2}(t) \right)^2 \dif t \\
&= \dint_{t_{1}}^{t_{2}} f_{1}^2 (t) \dif t - 2c_{12} \dint_{t_{1}}^{t_{2}} f_{1}(t)f_{2}(t) \dif t + c_{12}^2 \dint_{t_{1}}^{t_{2}} f_{2}^2(t) \dif t
\end{align}
$$
对 $c_{12}$ 求导并令其为零，得到 **$c_{12}$ 的最佳值**
$$
c_{12}^{*} = \frac{\dint_{t_{1}}^{t_{2}} f_{1}(t)f_{2}(t) \dif t}{\dint_{t_{1}}^{t_{2}} f_{2}^2(t) \dif t} = \frac{\langle f_{1},f_{2} \rangle}{\langle f_{2},f_{2} \rangle}
$$
对应的**最佳近似**误差为
$$
\varepsilon^* = \| f_{1}(t) \|^{2} - \dfrac{\langle f_{1},f_{2} \rangle^{2} }{\|f_{2}(t) \|^{2}} 
$$

当 $\langle f_{1},f_{2} \rangle = 0$ 时，$f_{1}(t)$ 中所含 $f_{2}(t)$ 的成分即为 $c_{12}^{*} = 0$，此时称 $f_{1}(t)$ 和 $f_{2}(t)$ 两信号**正交**。

> [!definition] 正交信号
> 如果在 $(t_{1},t_{2})$ 上 $\langle f_{1},f_{2} \rangle = 0$，则称 $f_{1}(t)$ 和 $f_{2}(t)$ 为 $(t_{1},t_{2})$ 上的**正交信号**。

对**复指数函数**，在 $(-\infty,+\infty)$ 上有
$$
\left\langle e^{\I \omega_{1} t}, e^{\I \omega_{2} t} \right\rangle = \int_{-\infty}^{+\infty} \e^{\I (\omega_{1} - \omega_{2}) t} \dif t = 2\pi \delta(\omega_{1} - \omega_{2})
$$
因此**单位复指数函数两两正交**。

### 正交函数集

在 $(t_{1},t_{2})$ 上两两**相互正交**的一组信号可构成 $(t_{1},t_{2})$ 上的**正交函数集**，用以表示 $(t_{1},t_{2})$ 上的任意信号。

> [!definition] 正交函数集
> 函数集 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ 称为 $(t_{1},t_{2})$ 上的**正交函数集**，如果对任意 $r, s \in \{ 1,2,\cdots,n \}$，都有
> $$
> \langle g_{r},g_{s} \rangle = \begin{cases}
> K_{r}, & r=s \\
> 0, & r \ne s
> \end{cases}
> $$

函数 $f(t)$ 在正交函数集 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ 上的**正交展开**为
$$
f(t) \approx \sum\limits_{r=1}^{n} \dfrac{\langle f(t), g_{r}(t) \rangle}{\langle g_{r}(t), g_{r}(t) \rangle} g_{r}(t)
$$
这一近似的**能量误差**为
$$
\varepsilon^* = \langle f(t),f(t) \rangle - \sum\limits_{r=1}^{n} \dfrac{|\langle f(t), g_{r}(t) \rangle|^2}{\langle g_{r}(t), g_{r}(t) \rangle}
$$

> [!definition] 归一化正交函数集
> 函数集 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ 称为 $(t_{1},t_{2})$ 上的**归一化正交函数集**，如果对任意 $r, s \in \{ 1,2,\cdots,n \}$，都有
> $$
> \langle g_{r},g_{s} \rangle = \begin{cases}
> 1, & r=s \\
> 0, & r \ne s
> \end{cases}
> $$

> [!theorem] 归一化正交函数集上的函数近似表示
> 如果 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ 是 $(t_{1},t_{2})$ 上的**归一化正交函数集**，则函数 $f(t)$ 在该正交函数集上的**最佳近似表示**为
> $$
> f(t) \approx \sum\limits_{r=1}^{n} c_{r}^* g_{r}(t) = \sum\limits_{r=1}^{n} \langle f(t), g_{r}(t) \rangle g_{r}(t)
> $$
> 这一近似的**能量误差**为
> $$
> \varepsilon^* = \langle f(t),f(t) \rangle - \sum\limits_{r=1}^{n} |\langle f(t), g_{r}(t) \rangle|^2
> = \| f(t) \|^2 - \| \v{c}^* \|^2
> $$
> 其中 $\v{c}^* = \begin{pmatrix} c_{1}^* \\ c_{2}^* \\ \vdots \\ c_{n}^* \end{pmatrix} = \begin{pmatrix} \langle f(t), g_{1}(t) \rangle \\ \langle f(t), g_{2}(t) \rangle \\ \vdots \\ \langle f(t), g_{n}(t) \rangle \end{pmatrix}$ 为**系数矢量**。

### 完备正交函数集

> [!definition] 完备正交函数集
> 如果 $(t_{1},t_{2})$ 上的任意函数 $f(t)$ 都可以在正交函数集 $\{ g_{r}(t) \}_{r \in \mathbb{Z}_{+}}$ 上获得表示
> $$
> f(t) \approx \sum\limits_{r=1}^{\infty} \dfrac{\langle f(t), g_{r}(t) \rangle}{\langle g_{r}(t), g_{r}(t) \rangle} g_{r}(t)
> $$
> 并且**最佳近似误差**为
> $$
> \varepsilon^*(\infty) = \lim\limits_{ n \to \infty } \varepsilon^*(n) = \lim\limits_{ n \to \infty } \dint_{t_{1}}^{t_{2}} \left( f(t) - \sum\limits_{r=1}^{n} \dfrac{\langle f(t), g_{r}(t) \rangle}{\langle g_{r}(t), g_{r}(t) \rangle} g_{r}(t) \right)^2 \dif t = 0
> $$
> 则称 $\{ g_{r}(t) \}_{r \in \mathbb{Z}_{+}}$ 为 $(t_{1},t_{2})$ 上的**完备正交函数集**。

若能找到一个满足 $0 < \dint_{t_{1}}^{t_{2}} \hat{g}^2(t) \dif t < \infty$ 的 $\hat{g}(t)$ 存在于正交函数集 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ 之外，而其使得
$$
\langle \hat{g}(t), g_{r}(t) \rangle = 0, \quad r=1,2,\cdots,n
$$
则 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ **不是完备正交函数集**，可将 $\hat{g}(t)$ 加入到 $\{ g_{r}(t) \}_{r=1,2,\cdots,n}$ 中，形成新的正交函数集 $\{ g_{r}(t) \}_{r=1,2,\cdots,n+1}$。

> [!theorem] Parseval 定理
> 任意函数 $f(t)$ 用完备正交函数集 $\{ g_{r}(t) \}_{r \in \mathbb{Z}_{+}}$ 展开为 $f(t) = \sum\limits_{r=1}^{\infty} c_{r}^* g_{r}(t)$ 时，有 **Parseval 等式**
> $$ \dint_{t_{1}}^{t_{2}} f^2(t) \dif t = \sum\limits_{r=1}^{\infty} (c_{r}^*)^2 \langle g_{r}(t), g_{r}(t) \rangle $$
> 特别地，对**归一化**完备正交函数集 $\{ g_{r}(t) \}_{r \in \mathbb{Z}_{+}}$，有
> $$ \| f(t) \|^2 = \sum\limits_{r=1}^{\infty} (c_{r}^*)^2 = \| \v{c}^* \|^2 $$

**单位复指数函数** $\{ e^{\I \omega t} \}_{\omega \in \mathbb{R}}$ 构成在 $(-\infty,+\infty)$ 上的**完备正交函数集**，任意 $f(t)$ 均可在该基底上展开为
$$
f(t) = \dfrac{1}{2\pi} \int_{-\infty}^{+\infty} F(\omega) \e^{\I \omega t} \dif \omega
$$
Fourier 变换 $F(\omega)$ 即是 $f(t)$ **在基函数 $\e^{\I \omega t}$ 上投影**的坐标，简记为 $F(\omega) = \left\langle f(t), \e^{\I \omega t} \right\rangle$。

## 信号的相关

### 能量信号的相关

> [!definition] 相关系数
> 定义 $f_{1}(t)$ 和 $f_{2}(t)$ 两信号的**相关系数**为
> $$
> \rho_{12} = \dfrac{\langle f_{1}(t),f_{2}(t) \rangle}{\sqrt{\langle f_{1}(t),f_{1}(t) \rangle} \sqrt{\langle f_{2}(t),f_{2}(t) \rangle}} 
> = \dfrac{\langle f_{1},f_{2} \rangle}{\| f_{1} \| \| f_{2} \|}
> = \left\langle \dfrac{f_{1}(t)}{\| f_{1} \|}, \dfrac{f_{2}(t)}{\| f_{2} \|} \right\rangle
> $$

基于此，$f_{1}(t)$ 用 $f_{2}(t)$ 的**最佳表示**可记为
$$
f_{1}(t) \approx \dfrac{\left\langle f_{1}(t),f_{2}(t) \right\rangle}{\langle f_{2}(t),f_{2}(t) \rangle} f_{2}(t) = \rho_{12} \dfrac{\| f_{1}(t) \|}{\|f_{2}(t)\|} f_{2}(t)
$$

由 [[#^4e145c|Cauchy-Schwarz 不等式]]可知，$|\rho_{12}| \le 1$。

也可由**最佳近似误差**求相关系数，由 $\varepsilon^* = \| f_{1}(t) \|^{2} - \dfrac{\langle f_{1},f_{2} \rangle^{2} }{\|f_{2}(t) \|^{2}}$ 有
$$
\dfrac{\varepsilon^*}{\| f_{1}(t) \|^{2}} = 1 - \dfrac{\langle f_{1},f_{2} \rangle^{2} }{\|f_{1}\|^{2} \|f_{2}\|^{2}} = 1 - \rho_{12}^{2}
$$

> [!definition] 相关函数
> 定义能量信号 $f_{1}(t)$ 与 $f_{2}(t)$ 的**相关函数**为
> $$
> \begin{align}
> R_{12}(\tau) &= \langle f_{1}(t),f_{2}(t-\tau) \rangle = \int_{-\infty}^{+\infty} f_{1}(t) f_{2}^{*}(t-\tau) \dif t \\
> &= \langle f_{1}(t+\tau),f_{2}(t) \rangle = \int_{-\infty}^{+\infty} f_{1}(t+\tau) f_{2}^{*}(t) \dif t \\
> R_{21}(\tau) &= \langle f_{2}(t),f_{1}(t-\tau) \rangle = \int_{-\infty}^{+\infty} f_{1}^{*}(t-\tau) f_{2}(t) \dif t \\
> &= \langle f_{2}(t+\tau),f_{1}(t) \rangle = \int_{-\infty}^{+\infty} f_{1}^{*}(t) f_{2}(t+\tau) \dif t
> \end{align}
> $$
> 其中宗量 $\tau$ 为**时延**。

两信号的相关函数满足 
$$
R_{12}(\tau) = R_{21}^{*}(-\tau)
$$
但一般 $R_{12}(\tau) \ne R_{21}(\tau)$。

> [!definition] 自相关函数
> 定义能量信号 $f(t)$ 的**自相关函数**为
> $$
> R(\tau) = \langle f(t),f(t-\tau) \rangle = \int_{-\infty}^{+\infty} f(t) f^{*}(t-\tau) \dif t
> $$

自相关函数满足 $R(\tau) = R^{*}(-\tau)$。

### 功率信号的相关

> [!definition] 功率信号的相关函数
> 定义功率信号 $f_{1}(t)$ 与 $f_{2}(t)$ 的**相关函数**为
> $$
> \begin{align}
> R_{12}(\tau) &= \lim\limits_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} f_{1}(t) f_{2}^{*}(t-\tau) \dif t \\
> R_{21}(\tau) &= \lim\limits_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} f_{1}^{*}(t-\tau) f_{2}(t) \dif t
> \end{align}
> $$
> 特别地，定义功率信号 $f(t)$ 的**自相关函数**为
> $$
> R(\tau) = \lim\limits_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} f(t) f^{*}(t-\tau) \dif t
> $$

对功率信号，同样有
$$
R_{12}(\tau) = R_{21}^{*}(-\tau), \qquad R(\tau) = R^{*}(-\tau)
$$

### Fourier 变换的相关定理

> [!theorem] Fourier 变换的相关定理
> 设 $\mathscr{F}\{ f(t) \} = F(\omega)$，$\mathscr{F}\{ f_1 (t) \} = F_1(\omega)$，$\mathscr{F}\{ f_2 (t) \} = F_2(\omega)$，则
> + $f_{1}$、$f_{2}$ 的**相关函数 $R_{12}$** 满足
> $$
> \mathscr{F}\{ R_{12}(\tau) \} = F_{1}(\omega) F_{2}^{*}(\omega) 
> $$
> + $f$ 的**自相关函数 $R$** 满足
> $$
> \mathscr{F}\{ R(\tau) \} = |F(\omega)|^2
> $$

对能量信号，$|F(\omega)|^{2}$ 描述了信号的**能量谱密度**，记作
$$
\mathcal{E}(\omega) = |F(\omega)|^{2} = \mathscr{F}\{ R(\tau) \}
$$
信号能量可由此表示为 $E = \dfrac{1}{2\pi} \dint_{-\infty}^{+\infty} \mathcal{E}(\omega) \dif \omega$。

对功率信号，我们取其**截尾函数**
$$
f_{T} (t) = \begin{cases}
f(t), & |t| \le \dfrac{T}{2} \\
0, & |t| > \dfrac{T}{2}
\end{cases}\quad \stackrel{\mathscr{F}}{\longmapsto} \quad
F_{T}(\omega) 
$$
由 Parseval 定理得到**平均功率**表示为
$$
\begin{align}
P &= \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} |f(t)|^2 \dif t = \lim_{T \to \infty} \dfrac{1}{T} \int_{-\infty}^{+\infty} |f_{T}(t)|^2 \dif t \\
&= \lim_{T \to \infty} \dfrac{1}{2\pi} \int_{-\infty}^{+\infty} \dfrac{|F_{T}(\omega)|^2}{T} \dif \omega \\
&= \dfrac{1}{2\pi} \int_{-\infty}^{+\infty} \underbrace{ \lim_{T \to \infty} \dfrac{|F_{T}(\omega)|^2}{T} }_{ \mathcal{P}(\omega) } \dif \omega 
= \dfrac{1}{2\pi} \int_{-\infty}^{+\infty} \mathcal{P}(\omega) \dif \omega
\end{align}
$$
其中 $\mathcal{P}(\omega)$ 称为**功率谱密度**，它描述了信号的平均功率分布，并且有
$$
\mathcal{P}(\omega) = \lim_{T \to \infty} \dfrac{1}{T} |F_{T}(\omega)|^2 = \mathscr{F}\{ R(\tau) \}
$$
这称为 **Wiener-Khintchine 定理**。

### 线性系统对信号作用的相关性分析

激励信号 $e(t)$ 通过线性系统 $H$ 作用后输出响应信号 $r(t)$，由
$$
R(\omega) = H(\omega) E(\omega)
$$
对**能量信号**和**功率信号**分别有
$$
\mathcal{E}_{r}(\omega) = |H(\omega)|^2 \mathcal{E}_{e}(\omega), \qquad \mathcal{P}_{r}(\omega) = |H(\omega)|^2 \mathcal{P}_{e}(\omega)
$$

又由系统的**自相关函数**的 Fourier 变换为
$$
\begin{align}
\mathscr{F}\{ R_{h}(\tau) \} &= \mathscr{F} \{ h(\tau) * h^{*}(-\tau) \} 
= \mathscr{F}\{ h(\tau) \} \mathscr{F}\{ h^{*}(-\tau) \} \\
&= H(\omega) \dint_{-\infty}^{\infty} h^{*}(-\tau) \e^{-\I\omega\tau} \dif \tau = H(\omega) \dint_{-\infty}^{\infty} h^{*}(\tau) \e^{\I\omega\tau} \dif \tau \\
&= H(\omega) \dint_{-\infty}^{\infty} \left(h(\tau) \e^{-\I\omega\tau}\right)^{*} \dif \tau \\
&= H(\omega) H^{*}(\omega) = |H(\omega)|^2
\end{align}
$$
得到
$$
R_{r}(\tau) = R_{e}(\tau) * R_{h}(\tau)
$$

## 匹配接收问题

欲判断接收到的信号 $e(t)$ 是否为已知信号 $s(t)$，可将 $e(t)$ 通过根据 $s(t)$ 设计的**匹配滤波器**处理，得到响应即相关函数 $R_{e,s}(\tau)$。

### 匹配滤波器设计

若 $s(t)$ 时宽为 $T$，则匹配滤波器的**冲激响应**设计为
$$
h(t) = s(T - t)
$$
这样响应即为
$$
r(t) = e(t) * s(T - t) = \int_{-\infty}^{+\infty} e(\tau) s(T - t + \tau) \dif \tau = R_{e,s}(t - T)
$$
当接收信号 $e(t)$ 与 $s(t)$ 有某种相关性时，**输出得到尖峰**，从而抑止噪声。

### 匹配滤波器的输出

当 $e(t) = s(t)$ 时，输出响应为
$$
r(t) = \int_{-\infty}^{+\infty} s(\tau) s(T - t + \tau) \dif \tau = R_{s,s}(t - T)
$$
特别地，在 $t=T$ 处，**响应取得最大值 $R_{s,s}(0) = \|s(t)\|^2 = E_{s}$**，为信号 $s(t)$ 的**能量**。





# 系统的状态变量分析

## 系统的信号流图表示

### 信号流图

**信号流图**是代数方程的图形化表示，是一种简化系统的方法。信号流图用一些**点**和**支路**构成的图形描述系统，引入若干术语和性质简化图形。
- **点**：表示系统的变量，通常用圆圈表示。在每个点处，对所有进入该点的支路进行代数相加，得到该点的变量值。
	- **源点**：只有输出，没有输入的点，表示系统的激励。
	- **阱点**：只有输入，没有输出的点，表示系统的观测。
- **支路**：表示变量之间的关系，通常用箭头表示。支路上有一个增益值，表示该支路对变量的影响程度。

信号流图中，变量可以是**变换域**或**时域**，系统可以是**离散**或**连续**时间。

```tikz
\usepackage{circuitikz}

\begin{document}
\large
\begin{tikzpicture}
	\draw (0,0) node[left] {$X(s)$}
		to[short, o-o, i={$H(s)$}] ++(2,0) node[right] {$Y(s)$};
	\draw (5,0) node[left] {$x(t)$}
		to[short, o-o, i={$h(t)$}] ++(2,0) node[right] {$y(t)$};
	\draw (0,-1) node[left] {$X(z)$}
		to[short, o-o, i={$H(z)$}] ++(2,0) node[right] {$Y(z)$};
	\draw (5,-1) node[left] {$x(n)$}
		to[short, o-o, i={$h(n)$}] ++(2,0) node[right] {$y(n)$};
\end{tikzpicture}
\end{document}
```

### 信号流图的代数运算

#### 串联、并联

- **串联支路**：两个或多个支路连接在一起，形成一个新的支路。串联的增益是**各支路增益的乘积**。
- **并联支路**：两个或多个支路连接在一起，形成一个新的支路。并联的增益是**各支路增益的和**。

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[6]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node[above] {#4};} 
	}, postaction={decorate}]
	#1 .. controls #3 .. #5;
	\draw #1 node[above] {#2} [fill=white] circle (1.5pt);
	\draw #5 node[above] {#6} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\draw (0,0) node[above] {$x_{1}$}
	to[short, o-o, i={$a$}] ++(2,0) node[above] {$x_{2}$}
	to[short, o-o, i={$b$}] ++(2,0) node[above] {$x_{3}$};
	\draw[-latex] (5,0) -- (7,0) node[above, midway] {simplified};
	\draw (8,0) node[above] {$x_{1}$} 
	to[short, o-o, i={$ab$}] ++(2,0) node[above] {$x_{3}$}; 
	
	\flow{(0,-2)}{$x_{1}$}{(2,-1)}{$a$}{(4,-2)}{$x_{2}$}; 
	\flow{(0,-2)}{$x_{1}$}{(2,-3)}{$b$}{(4,-2)}{$x_{2}$};
	\draw[-latex] (5,-2) -- (7,-2) node[above, midway] {simplified};
	\flow{(8,-2)}{$x_{1}$}{++(1,0)}{$a+b$}{(10,-2)}{$x_{2}$}; 
\end{tikzpicture}
\end{document}
```

#### 混合支路

混合结点所相连的支路构成**混合支路**，其增益为各支路增益的**乘积和**，即 

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node[above] {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{(0,1)}{$x_{1}$}{(1,0.5)}{$a$}{(2,0)}{}; 
	\flow[left]{(0,-1)}{$x_{2}$}{(1,-0.5)}{$b$}{(2,0)}{};
	\flow{(2,0)}{$x_{3}$}{(3,0)}{$c$}{(4,0)}{$x_{4}$};
	
	\draw[-latex] (5,0) -- (7,0) node[above, midway] {simplified};
	
	\flow[left]{(8,1)}{$x_{1}$}{(9,0.5)}{$ac$}{(10,0)}{}; 
	\flow[left]{(8,-1)}{$x_{2}$}{(9,-0.5)}{$bc$}{(10,0)}{};
	\node at (10,0) [right] {$x_{3}$};
\end{tikzpicture}
\end{document}
```

#### 反馈环路

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node[above] {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow{(0,0)}{$x_{1}$}{(1,0)}{$a$}{(2,0)}{}; 
	\flow{(2,0)}{$x_{2}$}{(3,0)}{$b$}{(4,0)}{};
	\flow{(4,0)}{$x_{3}$}{(3,-1)}{$c$}{(2,0)}{$x_{2}$};
	
	\draw[-latex] (5,0) -- (7,0) node[above, midway] {simplified};
	
	\flow[left]{(8,0)}{$x_{1}$}{(9,0)}{$\dfrac{ab}{1-bc}$}{(10,0)}{}; 
	\node at (10,0) [right] {$x_{3}$};
\end{tikzpicture}
\end{document}
```

### 梅森 (Mason) 公式

**Mason 公式**用于计算信号流图的传递函数。

> [!theorem] Mason 公式
> 一个信号流图中，**源点信号 $X$** 到**阱点信号 $Y$** 的变换域传递函数 $H = \dfrac{Y}{X}$ 为
> $$ H = \dfrac{1}{\Delta} \sum\limits_{k} g_{k}\Delta_{k} $$
> 其中：
> + $\Delta$ 为信号流图的**特征行列式**，其值为
> $$ \Delta = 1 - \sum\limits_{a} L_{a} + \sum\limits_{a \cap b = \varnothing} L_{a}L_{b} - \sum\limits_{a \cap b \cap c = \varnothing} L_{a}L_{b}L_{c} + \cdots $$
> 其中 $L_{a}$ 表示**环路 $a$ 的增益**，$a \cap b = \varnothing$ 表示环路 $a$ 和环路 $b$ 没有共同的点，即**不接触**。 
> + $g_{k}$ 为源点 $X$ 到阱点 $Y$ 的第 $k$ 条**前向通路增益**，前向通路是指从源点到阱点通过任意结点均不多于 1 次的路径。
> + $\Delta_{k}$ 为第 $k$ 条前向通路的**特征行列式余因子**，其值为除去与第 $k$ 条前向通路相接触的所有环路后，剩余环路的特征行列式。

#### 由流图求传递函数

> [!question] 由信号流图求传递函数
> 根据下面的信号流图，求传递函数 $H = \dfrac{Y}{X}$。
> ```tikz
> \usepackage{amsmath}
> \usepackage{amssymb}
> \usepackage{graphicx}
> \usepackage{tikz}
> \usetikzlibrary{decorations.markings}
> \usepackage{circuitikz}
> 
> \newcommand{\flow}[7][above]{
> 	\draw [thick, decoration={
> 		markings, 
> 		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
> 	}, postaction={decorate}]
> 	#2 .. controls #4 .. #6;
> 	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
> 	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
> }
> 
> \begin{document}
> \large
> \begin{tikzpicture}
> 	\flow[left]{(0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
> 	\flow{(2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
> 	\flow{(4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
> 	\flow{(6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
> 	\flow[right]{(8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
> 	
> 	\flow{(2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
> 	\flow{(4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
> 	
> 	\flow{(8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
> 	\flow{(10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
> \end{tikzpicture}
> \end{document}
> ```
> 

图中共 4 个环路：
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{(0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{(2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{(4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{[red!50](6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{(8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{(2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{(4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{[red!50](8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{(10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{(0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{[red!50](2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{(4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{(6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{(8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{(2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{[red!50](4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{(8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{[red!50](10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{(0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{(2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{(4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{[red!50](6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{[red!50](8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{[red!50](2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{(4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{(8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{[red!50](10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{(0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{[red!50](2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{[red!50](4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{[red!50](6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{[red!50](8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{(2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{(4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{(8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{[red!50](10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
其中前两个环路不相接触，故特征行列式为
$$
\begin{align}
\Delta &= 1 - \left( -H_{4}G_{1} -H_{2}H_{7}G_{2} -H_{4}H_{5}H_{6}G_{2} - H_{2}H_{3}H_{4}H_{5}G_{2} \right)  \\
&\hspace{1em} + \left( (-H_{4}G_{1}) \cdot (-H_{2}H_{7}G_{2}) \right) 
\end{align}
$$

图中共有 3 个前向通路：
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{[blue!50](0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{[blue!50](2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{[blue!50](4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{[blue!50](6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{[blue!50](8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{(2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{(4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{(8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{(10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
$$
g_{1} = H_{1}H_{2}H_{3}H_{4}H_{5}, \qquad \Delta_{1} = 1
$$

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{[blue!50](0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{(2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{(4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{[blue!50](6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{[blue!50](8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{[blue!50](2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{(4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{(8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{(10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
$$
g_{2} = H_{1}H_{6}H_{4}H_{5}, \qquad \Delta_{2} = 1
$$

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{[blue!50](0,0)}{$X$}{++(1,0)}{$H_{1}$}{++(2,0)}{}; 
	\flow{[blue!50](2,0)}{}{++(1,0)}{$H_{2}$}{++(2,0)}{};
	\flow{(4,0)}{}{++(1,0)}{$H_{3}$}{++(2,0)}{};
	\flow{[red!50](6,0)}{}{++(1,0)}{$H_{4}$}{++(2,0)}{};
	\flow[right]{(8,0)}{}{++(1,0)}{$H_{5}$}{++(2,0)}{$Y$};
	
	\flow{(2,0)}{}{++(2,1.5)}{$H_{6}$}{++(4,0)}{};
	\flow{[blue!50](4,0)}{}{++(3,2)}{$H_{7}$}{++(6,0)}{};
	
	\flow{[red!50](8,0)}{}{++(-1,-0.7)}{$-G_{1}$}{++(-2,0)}{};
	\flow{(10,0)}{}{++(-4,-2)}{$-G_{2}$}{++(-8,0)}{};
\end{tikzpicture}
\end{document}
```
$$
g_{3} = H_{1}H_{2}H_{7}, \qquad \Delta_{3} = 1 - (-H_{4}G_{1})
$$

故系统传递函数为
$$
H = \dfrac{1}{\Delta} \left( g_{1} + g_{2} + g_{3} (1 + H_{4}G_{1}) \right) 
$$

#### 由传递函数绘制流图

> [!question] 由传递函数绘制信号流图
> 给出一个符合传递函数
> $$ H(s) = \dfrac{\sum\limits_{k=0}^m b_{k}s^{m-k}}{\sum\limits_{r=0}^n a_{r}s^{n-r}}, \qquad a_{0} = 1, n \ge m$$
> 的系统，以信号流图表示。

所给式可化为 **$\dfrac{1}{s}$ 的有理分式**，即
$$
\begin{align}
H(s) &= \dfrac{b_{0}s^{m} + b_{1}s^{m-1} + \cdots + b_{m-1}s +b_{m}}{s^{n} + a_{1}s^{n-1} + a_{2}s^{n-2} + \cdots + a_{n-1}s + a_{n}} \\
&= \dfrac{b_{0} \dfrac{1}{s^{n-m}} + b_{1} \dfrac{1}{s^{n-m+1}} + \cdots + b_{m-1} \dfrac{1}{s^{n-1}} + b_{m} \dfrac{1}{s^{n}}}{1 + a_{1} \dfrac{1}{s} + a_{2} \dfrac{1}{s^{2}} + \cdots + a_{n-1} \dfrac{1}{s^{n-1}} + a_{n} \dfrac{1}{s^{n}}} 
\end{align}
$$
分母可视为所求流图的**特征行列式**，分子每一项都对应一条**前向通路**。为简便起见，令**各环路之间、前向通路与环路之间均有接触**，则流图可表示为
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}
\newcommand{\dashflow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}, dashed]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\large
\begin{tikzpicture}
	\flow[left]{(0,0)}{$X$}{++(1,0)}{$1$}{++(2,0)}{}; 
	\flow[right=3pt, below=3pt]{(2,0)}{}{++(1,0)}{$1/s$}{++(2,0)}{$X_{1}$};
	\flow[right=3pt, below=3pt]{(4,0)}{}{++(1,0)}{$1/s$}{++(2,0)}{$X_{2}$};
	\dashflow[right=3pt, below=3pt]{(6,0)}{}{++(1,0)}{}{++(2,0)}{$X_{n-m}$};
	\dashflow[right=3pt, below=3pt]{(8,0)}{}{++(1,0)}{}{++(2,0)}{$X_{n-2}$};
	\flow[right=3pt, below=3pt]{(10,0)}{}{++(1,0)}{$1/s$}{++(2,0)}{$X_{n-1}$};
	\flow[right=3pt, below=3pt]{(12,0)}{}{++(1,0)}{$1/s$}{++(2,0)}{$X_{n}$};
	
	\flow{(8,0)}{}{++(6,3.5)}{$b_{0}$}{++(8,0)}{};
	\flow{(10,0)}{}{++(4.5,2.5)}{$b_{m-2}$}{++(6,0)}{};
	\flow{(12,0)}{}{++(3,1.5)}{$b_{m-1}$}{++(4,0)}{};
	\flow[right]{(14,0)}{}{++(1.5,0.5)}{$b_{m}$}{++(2,0)}{$Y$};
	
	\flow{(4,0)}{}{++(-1.5,-0.5)}{$-a_{1}$}{++(-2,0)}{};
	\flow{(6,0)}{}{++(-3,-1.5)}{$-a_{2}$}{++(-4,0)}{};
	\flow{(8,0)}{}{++(-4.5,-2.5)}{$-a_{n-m}$}{++(-6,0)}{};
	\flow{(10,0)}{}{++(-6,-3.5)}{$-a_{n-2}$}{++(-8,0)}{};
	\flow{(12,0)}{}{++(-7.5,-4.5)}{$-a_{n-1}$}{++(-10,0)}{};
	\flow{(14,0)}{}{++(-9,-5.5)}{$-a_{n}$}{++(-12,0)}{};
\end{tikzpicture}
\end{document}
```

## 连续时间系统的状态变量分析

**状态方程方法**通过选取**状态变量** $\v{\lambda}$ 来描述系统的状态，进而构建系统的**状态方程**，将系统的状态变量与系统的**激励** $\v{e}$ 和**响应** $\v{r}$ 之间的关系描述为一个方程组。

### 连续时间系统状态方程的建立

连续时间系统的状态方程通常由以下形式的微分方程组描述：
$$
\begin{cases}
\dot{\v{\lambda}}_{k \times 1} (t) = \boldsymbol{A}_{k \times k} \v{\lambda}_{k \times 1} (t) + \boldsymbol{B}_{k \times m} \v{e}_{m \times 1} (t), & \text{状态转移方程} \\
\v{r}_{r \times 1} (t) = \boldsymbol{C}_{r \times k} \v{\lambda}_{k \times 1} (t) + \boldsymbol{D}_{r \times m} \v{e}_{m \times 1} (t), & \text{输出响应方程} 
\end{cases}
$$
其中：
+ $\v{\lambda}_{k \times 1} (t)$ 为 $k$ 个**状态变量**，
+ $\v{e}_{m \times 1} (t)$ 为 $m$ 个**输入激励**，
+ $\v{r}_{r \times 1} (t)$ 为 $r$ 个**输出响应**，
+ $\boldsymbol{A}_{k \times k}$、$\boldsymbol{B}_{k \times m}$、$\boldsymbol{C}_{r \times k}$、$\boldsymbol{D}_{r \times m}$ 为 4 个描述系统的矩阵。

在已知激励与响应之间具体关系的情况下，只需**确定状态变量**即可建立状态方程。

#### 由信号流图选取状态变量

取每个**积分器的输出**作为状态变量是常用的选取方式。每个积分器的输出代表系统状态的一部分，状态变量的个数通常与系统的阶数相同。

#### 由算子表达式分解选取状态变量

对于算子 $p$ 的有理分式形式的传递函数 $H(p)$，可将其分解为多个形如
$$
H_{i}(p) = \dfrac{\beta_{i}}{p + \alpha_{i}} = \dfrac{\beta_{i}/p}{1 + \alpha_{i}/p}
$$
因子的积或和的形式，**每个传函因子 $H_{i}(p)$ 对应一个状态变量 $\lambda_{i}(t)$**，其流图为
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}
\usepackage{circuitikz}

\newcommand{\flow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}
\newcommand{\dashflow}[7][above]{
	\draw [thick, decoration={
		markings, 
		mark=at position 0.5 with {\arrow{latex} \node at (0, .3) {#5};} 
	}, postaction={decorate}, dashed]
	#2 .. controls #4 .. #6;
	\draw #2 node[#1] {#3} [fill=white] circle (1.5pt);
	\draw #2 #6 node[#1] {#7} [fill=white] circle (1.5pt);
}

\begin{document}
\Large
\begin{tikzpicture}
	\flow[left]{(0,0)}{$x(t)$}{++(1,0)}{$1$}{++(2,0)}{}; 
	\flow{(2,0)}{$\dot{\lambda}_{i}$}{++(1,0)}{$1/p$}{++(2,0)}{$\lambda_{i}$};
	\flow[right]{(4,0)}{}{++(1,0)}{$\beta_{i}$}{++(2,0)}{$y(t)$};

	\flow{(4,0)}{}{++(-1,-0.5)}{$-\alpha_{i}$}{++(-2,0)}{};
\end{tikzpicture}
\end{document}
```

### 连续时间系统状态方程的求解

以下针对状态方程
$$
\begin{cases}
\dot{\v{\lambda}} (t) = \boldsymbol{A} \v{\lambda} (t) + \boldsymbol{B} \v{e} (t), \\
\v{r} (t) = \boldsymbol{C} \v{\lambda} (t) + \boldsymbol{D} \v{e} (t)
\end{cases}
$$
展开求解。

#### Laplace 变换法

对状态方程两边做 Laplace 变换，可将**微分**转化为**算子乘法**，得到
$$
\begin{cases}
s \v{\varLambda}(s) - \v{\lambda}(0_{-}) = \boldsymbol{A} \v{\varLambda}(s) + \boldsymbol{B} \v{E}(s), \\
\v{R}(s) = \boldsymbol{C} \v{\varLambda}(s) + \boldsymbol{D} \v{E}(s)
\end{cases}
$$
由状态转移方程解出状态变量
$$
\v{\varLambda}(s) = (s\boldsymbol{I} - \boldsymbol{A})^{-1} \v{\lambda}(0_{-}) + (s\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} \v{E}(s)
$$
代入输出响应方程，得到
$$
\v{R}(s) = \boldsymbol{C} (s\boldsymbol{I} - \boldsymbol{A})^{-1} \v{\lambda}(0_{-}) + \left( \boldsymbol{C}(s\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} + \boldsymbol{D} \right) \v{E}(s)
$$

> [!definition] 特征矩阵
> 状态转移方程 $\dot{\v{\lambda}(t) = \boldsymbol{A} \v{\lambda}(t) + \boldsymbol{B} \v{e}(t)}$ 在 Laplace 变换域的**特征矩阵**为
> $$ \boldsymbol{\varGamma}(s) = (s\boldsymbol{I} - \boldsymbol{A})^{-1} $$

即解出
$$
\begin{cases}
\v{\varLambda}(s) = \boldsymbol{\varGamma}(s) \v{\lambda}(0_{-}) + \boldsymbol{\varGamma}(s) \boldsymbol{B} \v{E}(s), \\
\v{R}(s) = \boldsymbol{C} \boldsymbol{\varGamma}(s) \v{\lambda}(0_{-}) + \left( \boldsymbol{C} \boldsymbol{\varGamma}(s) \boldsymbol{B} + \boldsymbol{D} \right) \v{E}(s)
\end{cases}
$$
做 **Laplace 逆变换**，得到
$$
\begin{align}
\v{\lambda} (t)
&= \mathscr{L}^{-1} \left\{ \boldsymbol{\varGamma}(s) \v{\lambda}(0_{-}) + \boldsymbol{\varGamma}(s) \boldsymbol{B} \v{E}(s) \right\} \\
&= \underbrace{ \boldsymbol{\gamma}(t) \v{\lambda}(0_{-}) }_{ \text{零输入解} } + \underbrace{ \boldsymbol{\gamma}(t) \boldsymbol{B} * \v{e}(t) }_{ 零状态解 } \\
\v{r} (t) 
&= \mathscr{L}^{-1} \left\{ \boldsymbol{C} \boldsymbol{\varGamma}(s) \v{\lambda}(0_{-}) + \left( \boldsymbol{C} \boldsymbol{\varGamma}(s) \boldsymbol{B} + \boldsymbol{D} \right) \v{E}(s) \right\} \\
&= \underbrace{ \boldsymbol{\gamma}(t) \boldsymbol{C} \v{\lambda}(0_{-}) }_{ 零输入响应 } + \underbrace{ \left( \boldsymbol{C} \boldsymbol{\gamma}(t) \boldsymbol{B} + \boldsymbol{D} \delta(t) \right) * \v{e}(t) }_{ 零状态响应 }
\end{align}
$$
其中
$$
\boldsymbol{\gamma}(t) = \mathscr{L}^{-1} \left\{ \boldsymbol{\varGamma}(s) \right\} = \mathscr{L}^{-1} \left\{ (s\boldsymbol{I} - \boldsymbol{A})^{-1} \right\}
$$
**求解特征矩阵 $(s\boldsymbol{I} - \boldsymbol{A})^{-1}$ 是 Laplace 变换法求解状态方程的核心**。

#### 时域法

> [!definition] 矩阵指数
> 矩阵 $\boldsymbol{A}$ 的 **e 指数**依 Taylor 级数定义为
> $$ \e^{\boldsymbol{A}} = \sum\limits_{k=0}^{\infty} \dfrac{1}{k!} \boldsymbol{A}^{k} = \boldsymbol{I} + \boldsymbol{A} + \dfrac{1}{2!} \boldsymbol{A}^{2} + \dfrac{1}{3!} \boldsymbol{A}^{3} + \cdots $$
> 矩阵指数的性质与实数指数类似。

以 $\e^{-\boldsymbol{A}t}$ 求解状态转移方程，可得
$$
\e^{-\boldsymbol{A}t} \dot{\v{\lambda}}(t) - \e^{-\boldsymbol{A}t} \boldsymbol{A} \v{\lambda}(t) = \dfrac{\dif}{\dif t} \left( \e^{-\boldsymbol{A}t} \v{\lambda}(t) \right) = \e^{-\boldsymbol{A}t} \boldsymbol{B} \v{e}(t)
$$
同时积分，得
$$
\e^{-\boldsymbol{A}t} \v{\lambda}(t) - \v{\lambda}(0_{-}) = \int_{0_{-}}^{t} \e^{-\boldsymbol{A}\tau} \boldsymbol{B} \v{e}(\tau) \dif \tau
$$
乘以 $\e^{\boldsymbol{A}t}$，即解出
$$
\v{\lambda}(t) = \e^{\boldsymbol{A}t} \v{\lambda}(0_{-}) + \dint_{0_{-}}^{t} \e^{\boldsymbol{A}(t - \tau)} \boldsymbol{B} \v{e}(\tau) \dif \tau
= \e^{\boldsymbol{A}t} \v{\lambda}(0_{-}) + \e^{\boldsymbol{A}t} \boldsymbol{B} * \v{e}(t)
$$

> [!definition] 状态转移矩阵
> 状态转移方程 $\dot{\v{\lambda}}(t) = \boldsymbol{A} \v{\lambda}(t) + \boldsymbol{B} \v{e}(t)$ 对应的**状态转移矩阵**为
> $$ \boldsymbol{\gamma}(t) = \e^{\boldsymbol{A}t} $$
> 其与**特征矩阵**是一对 **Laplace 变换对**，即我们有
> $$\mathscr{L} \left\{ \boldsymbol{\gamma}(t) \right\} = \mathscr{L} \left\{ \e^{\boldsymbol{A}t} \right\} = (s\boldsymbol{I} - \boldsymbol{A})^{-1} = \boldsymbol{\varGamma}(s)$$

代入输出响应方程，得到
$$
\begin{align}
\v{r}(t) &= \boldsymbol{C} \v{\lambda}(t) + \boldsymbol{D} \v{e}(t) \\
&= \boldsymbol{C} \left( \e^{\boldsymbol{A}t} \v{\lambda}(0_{-}) + \e^{\boldsymbol{A}t} \boldsymbol{B} * \v{e}(t) \right) + \boldsymbol{D} \v{e}(t) \\
&= \underbrace{ \boldsymbol{C} \e^{\boldsymbol{A}t} \v{\lambda}(0_{-}) }_{ \text{零输入响应} } + \underbrace{ \left( \boldsymbol{C} \e^{\boldsymbol{A}t} \boldsymbol{B} + \boldsymbol{D} \delta(t) \right) * \v{e}(t) }_{ \text{零状态响应} }
\end{align}
$$
**求解状态转移矩阵 $\e^{\boldsymbol{A}t}$ 是时域法求解状态方程的核心**。求解此矩阵需要使用 **Kelly-Hamilton 定理**（$\det(\lambda \boldsymbol{I} - \boldsymbol{A}) \Big|_{\lambda=\boldsymbol{A}} = \boldsymbol{A}^{n} + a_{n-1} \boldsymbol{A}^{n-1} + \cdots + a_{0}\boldsymbol{I} = O$）将定义中无穷级数**截断**为
$$
\e^{\boldsymbol{A}t} = \sum\limits_{k=0}^{\infty} \dfrac{1}{k!} (\boldsymbol{A}t)^{k} = \sum\limits_{k=0}^{n-1} \alpha_{k}(t) \boldsymbol{A}^{k}
$$
然后解微分方程组确定待定系数 $\alpha_{k}(t)$，较为繁琐。

### 连续时间系统函数与状态方程的关系

连续时间系统的零状态响应由上表示为
$$
\v{R}_{\mathrm{zs}} (s) = \left( \boldsymbol{C} \boldsymbol{\varGamma}(s) \boldsymbol{B} + \boldsymbol{D} \right) \v{E}(s) = \boldsymbol{H}(s) \v{E}(s)
$$
即知**系统函数**（矩阵）为
$$
\begin{align}
\boldsymbol{H}(s) &= \boldsymbol{C} \boldsymbol{\varGamma}(s) \boldsymbol{B} + \boldsymbol{D} = \boldsymbol{C} (s\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} + \boldsymbol{D} \\
&= \begin{pmatrix}
H_{11}(s) & H_{12}(s) & \cdots & H_{1m}(s) \\
H_{21}(s) & H_{22}(s) & \cdots & H_{2m}(s) \\
\vdots & \vdots & \ddots & \vdots \\
H_{r1}(s) & H_{r2}(s) & \cdots & H_{rm}(s)
\end{pmatrix}
\end{align}
$$

特别地，对于**单输入单输出**（SISO）系统，转移函数为
$$
H(s) = \boldsymbol{C}_{1 \times k} (s\boldsymbol{I}_{k} - \boldsymbol{A}_{k \times k})^{-1} \boldsymbol{B}_{k \times 1} + D
= \dfrac{\boldsymbol{C}_{1 \times k} \mathop{\mathrm{adj}} (s\boldsymbol{I}_{k} - \boldsymbol{A}_{k \times k}) \boldsymbol{B}_{k \times 1}}{\det(s\boldsymbol{I}_{k} - \boldsymbol{A}_{k \times k})} + D
$$
其中：
+ $\mathop{\mathrm{adj}}(s\boldsymbol{I} - \boldsymbol{A})$ 为**伴随矩阵**，
+ $\det(s\boldsymbol{I} - \boldsymbol{A})$ 的根即为**系统的极点**，同时也是 $\boldsymbol{A}$ 的**特征值**。

## 离散时间系统的状态变量分析

### 离散时间系统状态方程的建立

离散时间系统的状态方程通常由以下形式的微分方程组描述：
$$
\begin{cases}
\v{\lambda}_{k \times 1} (n + 1) = \boldsymbol{A}_{k \times k} \v{\lambda}_{k \times 1} (n) + \boldsymbol{B}_{k \times m} \v{x}_{m \times 1} (n), & \text{状态转移方程} \\
\v{y}_{r \times 1} (n) = \boldsymbol{C}_{r \times k} \v{\lambda}_{k \times 1} (n) + \boldsymbol{D}_{r \times m} \v{x}_{m \times 1} (n), & \text{输出响应方程}
\end{cases}
$$

将信号流图中每个**延时器的输出**作为状态变量是常用的选取方式。每个延时器的输出代表系统状态的一部分，状态变量的个数通常与系统的阶数相同。

在实际的离散系统中，可以直接根据**具体系统结构**直观地选取状态变量。

> [!example] 人口增长的动态模型
> 将某地区人口**按年龄分组**为
> $$ \v{\lambda}(n) = \begin{pmatrix}
> \lambda_{0}(n) & \lambda_{1}(n) & \cdots & \lambda_{k-1}(n)
> \end{pmatrix}^{\mathrm{T}} $$
> 其中 $\lambda_{i}(n)$ 为第 $i$ 年龄组在第 $n$ 周期的人口数，$0 \le i < k$，$n > 0$。
> 
> 那么**人口随时间变化的规律**可描述为
> $$\begin{cases}
> \lambda_{0}(n + 1) = \alpha_{0} \lambda_{0}(n) + \alpha_{1} \lambda_{1}(n) + \cdots + \alpha_{k-1} \lambda_{k-1}(n), \\
> \lambda_{i}(n + 1) = \beta_{i-1} \lambda_{i-1}(n), \quad 1 \le i < k
> \end{cases}$$
> 其中：
> + $\alpha_{i}$ 刻画第 $i$ 年龄组人口的**生育率**，
> + $\beta_{i}$ 刻画第 $i$ 年龄组人口的**存活率**。 

### 离散时间系统状态方程的求解

以下针对状态方程
$$
\begin{cases}
\v{\lambda}(n + 1) = \boldsymbol{A} \v{\lambda}(n) + \boldsymbol{B} \v{x}(n), \\
\v{y}(n) = \boldsymbol{C} \v{\lambda}(n) + \boldsymbol{D} \v{x}(n)
\end{cases}
$$
展开求解。

#### 时域迭代法

自**已知状态** $\v{\lambda}(n_{0})$ 出发，**归纳**得
$$
\v{\lambda}(n) = \boldsymbol{A}^{n - n_{0}} \v{\lambda}(n_{0}) + \sum\limits_{k=n_{0}}^{n-1} \boldsymbol{A}^{n - k - 1} \boldsymbol{B} \v{x}(k)
$$
以 $n_{0} = 0$ 为例，得到
$$
\begin{align}
\v{\lambda}(n) &= \boldsymbol{A}^{n} \v{\lambda}(0) u(n) + \left( \sum\limits_{k=0}^{n-1} \boldsymbol{A}^{n - k - 1} \boldsymbol{B} \v{x}(k) \right) u(n - 1) \\
&= \boldsymbol{A}^{n} \v{\lambda}(0) u(n) + \boldsymbol{A}^{n-1}\boldsymbol{B} u(n - 1) * \v{x}(n) 
\end{align}
$$
输出响应即
$$
\v{y}(n) 
= \underbrace{ \boldsymbol{C} \boldsymbol{A}^{n} \v{\lambda}(0) u(n) }_{ \text{零输入响应} } 
+ \underbrace{ \left( \boldsymbol{C} \boldsymbol{A}^{n-1} \boldsymbol{B} u(n - 1) + \boldsymbol{D} \delta(n) \right) * \v{x}(n) }_{ \text{零状态响应} }
$$
于是**单位样值响应**为
$$
\boldsymbol{h}(n) = \boldsymbol{C} \boldsymbol{A}^{n-1} \boldsymbol{B} u(n - 1) + \boldsymbol{D} \delta(n)
$$

#### $z$ 变换法

对状态方程两边做 $z$ 变换，得到
$$
\begin{cases}
z \v{\varLambda}(z) - z\v{\lambda}(0) = \boldsymbol{A} \v{\varLambda}(z) + \boldsymbol{B} \v{X}(z), \\
\v{Y}(z) = \boldsymbol{C} \v{\varLambda}(z) + \boldsymbol{D} \v{X}(z)
\end{cases}
$$
由状态转移方程解出状态变量
$$
\v{\varLambda}(z) = (z\boldsymbol{I} - \boldsymbol{A})^{-1} z\v{\lambda}(0) + (z\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} \v{X}(z)
$$
取**逆 $z$ 变换**解出
$$
\begin{align}
\v{\lambda}(n) &= \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} z\v{\lambda}(0) + (z\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} \v{X}(z) \right\} \\
&= \underbrace{ \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} z \right\} \v{\lambda}(0) }_{ \text{零输入解}  } 
+ \underbrace{ \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} \right\} \boldsymbol{B} * \v{x}(n) }_{ 零状态解 } 
\end{align}
$$
代入输出响应方程，得到
$$
\v{y}(n) = \underbrace{ \boldsymbol{C} \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} z \right\} \v{\lambda}(0) }_{ \text{零输入响应} } 
+ \underbrace{ \left( \boldsymbol{C} \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} \right\} \boldsymbol{B} + \boldsymbol{D} \delta(n) \right) * \v{x}(n) }_{ \text{零状态响应} }
$$
与[[#时域迭代法]]的结果对照，可得到**对应关系**有
$$
\begin{align}
&\boldsymbol{A}^{n} u(n) = \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} z \right\}, \\
&\boldsymbol{A}^{n-1} u(n - 1) = \mathscr{Z}^{-1} \left\{ (z\boldsymbol{I} - \boldsymbol{A})^{-1} \right\}
\end{align}
$$

类比连续时间系统，可称 $\boldsymbol{\varGamma}(z) = (z\boldsymbol{I} - \boldsymbol{A})^{-1}$ 为**特征矩阵**，$\boldsymbol{A}^{n}$ 为**状态转移矩阵**。

## 状态矢量的线性变换

同一系统可选择**不同的状态矢量 $\v{\lambda}$**，对应于系统状态方程中**不同的 $\boldsymbol{A}$、$\boldsymbol{B}$、$\boldsymbol{C}$、$\boldsymbol{D}$ 矩阵**。对状态矢量的线性变换也会影响状态方程。

### $\v{\lambda}$ 矢量的线性变换

若对状态矢量 $\v{\lambda}$ 做**线性变换 $\boldsymbol{P}$** 得到 $\v{\gamma} = \boldsymbol{P} \v{\lambda}$，简单起见令 **$\boldsymbol{P}$ 可逆**，则将 $\v{\lambda} = \boldsymbol{P}^{-1} \v{\gamma}$ 代入状态方程，可得
$$
\begin{cases}
\dot{\v{\gamma}}(t) = \boldsymbol{P} \boldsymbol{A} \boldsymbol{P}^{-1} \v{\gamma}(t) + \boldsymbol{P} \boldsymbol{B} \v{e}(t) =: \hat{\boldsymbol{A}} \v{\gamma}(t) + \hat{\boldsymbol{B}} \v{e}(t), \\
\v{r}(t) = \boldsymbol{C} \boldsymbol{P}^{-1} \v{\gamma}(t) + \boldsymbol{D} \v{e}(t) =: \hat{\boldsymbol{C}} \v{\gamma}(t) + \hat{\boldsymbol{D}} \v{e}(t)
\end{cases}
$$
故状态方程的矩阵变换为
$$
\hat{\boldsymbol{A}} = \boldsymbol{P} \boldsymbol{A} \boldsymbol{P}^{-1}, \quad
\hat{\boldsymbol{B}} = \boldsymbol{P} \boldsymbol{B}, \quad
\hat{\boldsymbol{C}} = \boldsymbol{C} \boldsymbol{P}^{-1}, \quad
\hat{\boldsymbol{D}} = \boldsymbol{D}
$$
新的**转移函数**为
$$
\begin{align}
\hat{\boldsymbol{H}}(s) &= \hat{\boldsymbol{C}} \boldsymbol{\varGamma}(s) \hat{\boldsymbol{B}} + \hat{\boldsymbol{D}}
= \boldsymbol{C} \boldsymbol{P}^{-1} \left( s\boldsymbol{I} - \boldsymbol{P}\boldsymbol{A}\boldsymbol{P}^{-1} \right)^{-1} \boldsymbol{P} \boldsymbol{B} + \boldsymbol{D} \\
&= \boldsymbol{C} \boldsymbol{P}^{-1} \left( \boldsymbol{P} (s\boldsymbol{I} - \boldsymbol{A}) \boldsymbol{P}^{-1} \right)^{-1} \boldsymbol{P} \boldsymbol{B} + \boldsymbol{D} \\
&= \boldsymbol{C} \boldsymbol{P}^{-1} \boldsymbol{P} (s\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{P}^{-1} \boldsymbol{P} \boldsymbol{B} + \boldsymbol{D} \\
&= \boldsymbol{C} (s\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} + \boldsymbol{D} = \boldsymbol{H}(s)
\end{align}
$$
即**转移函数不变**。
+ 从实际系统的角度看，**系统内部**状态变量的选取**不会影响**系统的输入输出关系，因此**系统物理本质不变**，转移函数不变。
+ 从状态变换的角度看，状态变量的线性变换对应于**状态转移方程矩阵 $\boldsymbol{A}$ 的相似变换**，因此系统的**特征值（极点）不变**。

### $\boldsymbol{A}$ 矩阵的对角化

若 $\boldsymbol{A}$ 可**对角化**，即存在可逆矩阵 $\boldsymbol{P}$ 使得
$$
\boldsymbol{A} = \boldsymbol{P} \hat{\boldsymbol{A}} \boldsymbol{P}^{-1}, \qquad \hat{\boldsymbol{A}} = \mathop{\mathrm{diag}} (p_{i})
$$
则以 $\boldsymbol{P}^{-1}$ 对状态变量 $\v{\lambda}$ 做线性变换，得到新的状态变量 $\v{\gamma} = \boldsymbol{P}^{-1} \v{\lambda}$，**状态转移方程**可写为
$$
\dot{\v{\gamma}}(t) = \boldsymbol{P}^{-1} \boldsymbol{A} \boldsymbol{P} \v{\gamma}(t) + \boldsymbol{P}^{-1} \boldsymbol{B} \v{e}(t) = \hat{\boldsymbol{A}} \v{\gamma}(t) + \boldsymbol{P}^{-1} \boldsymbol{B} \v{e}(t)
$$
因 $\hat{\boldsymbol{A}}$ 为**对角阵**，$\hat{\boldsymbol{A}} \v{\gamma}(t) = \begin{pmatrix}p_{i}\gamma_{i}(t)\end{pmatrix}_{0 < i \le k}$，即**各状态变量之间解耦**，系统变换成并联结构。

## 由状态方程判断系统性质

### BIBO 稳定性

**连续时间系统**的系统转移函数为
$$
\boldsymbol{H}(s) = \boldsymbol{C} (s\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} + \boldsymbol{D}
$$
其中 $\det(s\boldsymbol{I} - \boldsymbol{A}) = 0$ 的根，即 $\boldsymbol{A}$ 的**特征值**，为系统的**极点**。若 $\boldsymbol{H}(s)$ 的所有极点、$\boldsymbol{A}$ 的所有特征值均在 **$s$ 平面的左半平面**，则系统 **BIBO 稳定**。

**离散时间系统**的系统转移函数为
$$
\boldsymbol{H}(z) = \boldsymbol{C} (z\boldsymbol{I} - \boldsymbol{A})^{-1} \boldsymbol{B} + \boldsymbol{D}
$$
其中 $\det(z\boldsymbol{I} - \boldsymbol{A}) = 0$ 的根，即 $\boldsymbol{A}$ 的**特征值**，为系统的**极点**。若 $\boldsymbol{H}(z)$ 的所有极点、$\boldsymbol{A}$ 的所有特征值均在 **$z$ 平面的单位圆内**，则系统 **BIBO 稳定**。

### 可控性与可观性

> [!definition] 可控性
> **可控性 (Controllability)** 是指系统的状态变量 $\v{\lambda}$ 能否通过输入容许的**控制矢量** $\v{e}$ 在有限时间内转移到零状态。
> 
> 若对起始状态 $\v{\lambda}(0)$，存在激励 $\v{e}(t)$ 使得
> $$ \v{\lambda}(t) = \boldsymbol{0}, \qquad \exists 0 < t_{0} < \infty,\ \forall t > t_{0}  $$
> 则称系统**完全可控**。

在**线性时不变**系统中，可控性等价于**可达性**，即系统的状态变量 $\v{\lambda}$ 能否通过输入容许的控制矢量 $\v{e}$ 在有限时间内转移到**任意状态**。

> [!definition] 可观性
> **可观性 (Observability)** 是指给定输入 $\v{e}(t)$ 后，能否通过系统有限时间内的输出响应 $\v{r}(t)$ 唯一地确定系统的起始状态。
> 
> 若对激励信号 $\v{e}(t)$，存在变换 $P$ 使得
> $$ \v{\lambda}(0) = P(\v{r}(t); t_{0}), \qquad \exists 0 < t_{0} < \infty $$
> 则称系统**完全可观**。

#### 可控阵与可观阵

+ 若**可控阵**
$$
\boldsymbol{M}_{k \times km} = \begin{pmatrix}
\boldsymbol{B} & \boldsymbol{A}\boldsymbol{B} & \boldsymbol{A}^{2}\boldsymbol{B} & \cdots & \boldsymbol{A}^{k-1}\boldsymbol{B}
\end{pmatrix}
$$
为**行满秩**，即 $\mathrm{rank}(\boldsymbol{M}) = k$，则系统**完全可控**；
+ 若**可观阵**
$$
\boldsymbol{N}_{rk \times k} = \begin{pmatrix}
\boldsymbol{C} \\
\boldsymbol{C}\boldsymbol{A} \\
\boldsymbol{C}\boldsymbol{A}^{2} \\
\vdots \\
\boldsymbol{C}\boldsymbol{A}^{k-1}
\end{pmatrix}
$$
为**列满秩**，即 $\mathrm{rank}(\boldsymbol{N}) = k$，则系统**完全可观**。




