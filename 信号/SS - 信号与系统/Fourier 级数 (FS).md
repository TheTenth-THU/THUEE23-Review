## 周期信号的 Fourier 级数分析

### 定义

#### 三角函数形式

周期函数可表示为三角函数的线性组合，即 **Fourier 级数**。

> [!definition] Fourier 级数（三角函数形式）
> 周期为 $T_{1}$ 的函数 $f(t)$ 可表示为三角函数的级数：
> $$
> \begin{align}
> f(t) &=a_{0}+a_{1}\cos(\omega_{1}t)+b_{1}\sin(\omega_{1}t)+a_{2}\cos(2\omega_{1}t)+b_{2}\sin(2\omega_{1}t)+\cdot\cdot\cdot\\
> &=a_{0}+\displaystyle\sum_{n=1}^{\infty}\big(a_{n}\cos(n\omega_{1}t)+b_{n}\sin(n\omega_{1}t)\big) \\
> \end{align}
> $$
> 其中，$a_{0}$ 为**直流分量**，$a_{n}$ 和 $b_{n}$ 为**交流分量**，其值为
> $$
> \begin{align}
> a_{0} &=\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t) \dif t \\
> a_{n} &=\frac{2}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\cos(n\omega_{1}t) \dif t, \quad 
> b_{n} =\frac{2}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\sin(n\omega_{1}t) \dif t
> \end{align}
> $$
> $T_{1}$ 为周期，$\omega_{1}=\dfrac{2\pi}{T_{1}}$ 称为**基频**。

^e6092d

也可用辅助角公式将三角级数中的正余弦项**合并为余弦项**，即
$$
\begin{align}
f(t) &=a_{0}+\displaystyle\sum_{n=1}^{\infty}\big(a_{n}\cos(n\omega_{1}t)+b_{n}\sin(n\omega_{1}t)\big) \\
&=c_{0}+\displaystyle\sum_{n=1}^{\infty}c_{n}\cos(n\omega_{1}t+\varphi_{n})
\end{align}
$$
其中 $c_{0}=a_{0}$，$c_{n}=\sqrt{a_{n}^{2}+b_{n}^{2}}$，$\varphi_{n}$ 满足 $\tan\varphi_{n}=-\dfrac{b_{n}}{a_{n}}$。

> [!danger] 相位谱 $\varphi_{n}$ 的计算
> **不可使用 $\varphi_{n}=-\arctan\dfrac{b_{n}}{a_{n}}$ 计算相位谱**，其正确值为先计算
> $$
> \varphi_{n}=\begin{cases} 
> -\arctan\dfrac{b_{n}}{a_{n}}, & a_{n}\ge0 \\
> \pi-\arctan\dfrac{b_{n}}{a_{n}}, & a_{n}<0
> \end{cases}
> $$
> 再将 $\varphi_{n}$ 由 $\left(-\dfrac{\pi}{2},\dfrac{3\pi}{2}\right)$ 转换到 $\left(0,2\pi\right)$ 或 $\left(-\pi,\pi\right)$。

同理还可**合并为正弦项**，即
$$
\begin{align}
f(t) &=a_{0}+\displaystyle\sum_{n=1}^{\infty}\big(a_{n}\cos(n\omega_{1}t)+b_{n}\sin(n\omega_{1}t)\big) \\
&=d_{0}+\displaystyle\sum_{n=1}^{\infty} d_{n}\sin(n\omega_{1}t+\theta_{n}) 
\end{align}
$$
其中 $d_{0}=a_{0}$，$d_{n}=\sqrt{a_{n}^{2}+b_{n}^{2}}$，$\theta_{n}$ 满足 $\tan\theta_{n}=\dfrac{a_{n}}{b_{n}}$。

#### 复指数形式

由欧拉公式
$$
\cos(\omega t) = \frac{1}{2}\left(e^{\I \omega t}+e^{-\I \omega t}\right), \quad \sin(\omega t) = \frac{1}{2\I }\left(e^{\I \omega t}-e^{-\I \omega t}\right)
$$
代入[[#^e6092d|三角函数形式的 Fourier 级数]]，可得
$$
\begin{align}
f(t)&=a_{0}+\displaystyle\sum_{n=1}^{\infty}\left[\displaystyle\frac{a_{n}}{2}\left(\mathrm{e}^{\I n\omega_{1}t}+\mathrm{e}^{-\I n\omega_{1}t}\right)+\displaystyle\frac{b_{n}}{2\I }\left(\mathrm{e}^{\I n\omega_{1}t}-\mathrm{e}^{-\I n\omega_{1}t}\right)\right] \\
&=a_{0}+\displaystyle\sum_{n=1}^{\infty}\left(\displaystyle\frac{a_{n}-\I b_{n}}{2}\mathrm{e}^{\I n\omega_{1}t}+\displaystyle\frac{a_{n}+\I b_{n}}{2}\mathrm{e}^{-\I n\omega_{1}t}\right) \\
&=a_{0}+\displaystyle\sum_{n=1}^{\infty}\displaystyle\frac{a_{n}-\I b_{n}}{2}\mathrm{e}^{\I n\omega_{1}t}+\displaystyle\sum_{n=-\infty}^{-1}\displaystyle\frac{a_{-n}+\I b_{-n}}{2}\mathrm{e}^{\I n\omega_{1}t}
\end{align}
$$
其中
$$
\begin{align}
\frac{a_{n}-\I b_{n}}{2} & =\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\left[\cos(n\omega_{1}t)-\I\sin(n\omega_{1}t)\right]\dif t \\ & =\frac{1}{T_1}\int_{t_0}^{t_0+T_1}f(t)\mathrm{e}^{-\I n\omega_1t}\dif t, \quad &n=1,2,3,\cdots 
\end{align}
$$
$$
\begin{align}\frac{a_{-n}+\I b_{-n}}{2} & =\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\left[\cos(-n\omega_{1}t)+\I\sin(-n\omega_{1}t)\right]\dif t \\[1ex] & =\frac{1}{T_1}\int_{t_0}^{t_0+T_1}f(t)\mathrm{e}^{-\I n\omega_1t}\dif t &\hspace{-5em} n = -1,-2,-3,\cdots 
\end{align}
$$
$$
a_{0}  =\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\mathrm{e}^{-\I 0\omega_{1}t}\dif t
$$

> [!definition] Fourier 级数（复指数形式）
> 周期为 $T_{1}$ 的函数 $f(t)$ 可表示为复指数的级数：
> $$
> f(t)=\sum_{n=-\infty}^{\infty} F_{n}\mathrm{e}^{\I n\omega_{1}t}
> $$
> 其中 $F_{n}$ 为**频谱系数**，其值为
> $$
> F_{n}=\frac{1}{T_{1}}\int_{t_{0}}^{t_{0}+T_{1}}f(t)\mathrm{e}^{-\I n\omega_{1}t} \dif t
> $$
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
	$$
	a_{n} = \dfrac{4}{T_{1}}\int_{0}^{\frac{T_{1}}{2}}f(t)\cos(n\omega_{1}t) \dif t, \quad b_{n} = \dfrac{4}{T_{1}}\int_{0}^{\frac{T_{1}}{2}}f(t)\sin(n\omega_{1}t) \dif t
	$$

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




