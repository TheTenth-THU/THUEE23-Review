## L19 (12/11)

### L19-1

**一维无限制随机游走 (random walk) 中各状态的性质。**

设随机游走 $S_{n} = \sum\limits_{i=1}^{n} X_{i}$，其中 $X_{i} \stackrel{\text{i.i.d}}{\sim} \begin{pmatrix}1 & -1 \\ p & 1-p \end{pmatrix}$。显然，$S_{n}$ 是一个 $\mathbb{Z}$ 上的 **Markov 链**，所有整数点具有相同的性质，因此我们只需考察**状态 0 的常返性**。

经 $n$ 步从 0 回到 0 的概率为
$$
P_{0,0}(n) = \begin{cases}
\binom{2k}{k} p^{k} (1-p)^{k}, & n = 2k,  \\
0, & n = 2k+1, 
\end{cases} \quad k = 0,1,2,\cdots
$$
故其常返性取决于级数
$$
\sum\limits_{k=1}^{\infty} P_{0,0}(2k) = \sum\limits_{k=1}^{\infty} \binom{2k}{k} (p(1-p))^{k} = \sum\limits_{k=1}^{\infty} \dfrac{(2k)!}{(k!)^{2}} (p(1-p))^{k}
$$

利用 **Stirling 公式** $n! \sim \sqrt{2 \pi n} \left( \cfrac{n}{\e} \right)^{n}$，有
$$
\dfrac{(2k)!}{(k!)^{2}} (p(1-p))^{k} \sim \dfrac{\sqrt{ 4\pi k } \left( \cfrac{2k}{\e} \right)^{2k}}{2 \pi k \left( \cfrac{k}{\e} \right)^{2k}} (p(1-p))^{k} = \dfrac{(4p(1-p))^{k}}{\sqrt{\pi k}} 
$$
+ 若 $p = \cfrac{1}{2}$，则 $4p(1-p) = 1$，级数发散，**状态 0 为常返态**，此时随机游走是**平衡**的；
+ 若 $p \ne \cfrac{1}{2}$，则 $4p(1-p) < 1$，级数收敛，**状态 0 为非常返态**。

### L19-2

**二维无限制平衡随机游走中各状态的性质。**

设二维随机游走 $\v{S}_{n} = \sum\limits_{i=1}^{n} \v{X}_{i}$，其中概率分布取平衡的 $\v{X}_{i} \stackrel{\text{i.i.d}}{\sim} \begin{pmatrix} (1,0) & (-1,0) & (0,1) & (0,-1) \\ \cfrac{1}{4} & \cfrac{1}{4} & \cfrac{1}{4} & \cfrac{1}{4} \end{pmatrix}$。同样地，我们只需考察**状态 $\v{0}$ 的常返性**。

显然奇数步不可返回，经 $2n$ 步从 $\v{0}$ 回到 $\v{0}$ 的概率为
$$
\begin{align} 
P_{\v{0},\v{0}}(2n) &= \sum\limits_{k=0}^{n} \dfrac{(2n)!}{(k!)^{2} ((n-k)!)^{2}} \left( \dfrac{1}{4} \right)^{2n}  \\
&= \left( \dfrac{1}{4} \right)^{2n} \binom{2n}{n} \sum\limits_{k=0}^{n} \binom{n}{k} \binom{n}{n-k} = \left( \dfrac{1}{4} \right)^{2n} \binom{2n}{n}^{2} 
\end{align}
$$
利用 Stirling 公式，有
$$
\left( \dfrac{1}{4} \right)^{2n} \binom{2n}{n}^{2} \sim \left( \dfrac{1}{4} \right)^{2n} \dfrac{4^{2n}}{\pi n} = \dfrac{1}{\pi n}
$$
因此级数 $\sum\limits_{n=1}^{\infty} P_{\v{0},\v{0}}(2n) \sim \sum\limits_{n=1}^{\infty} \cfrac{1}{n}$ 发散，**状态 $\v{0}$ 为常返态**。

## L21 (12/23)

### L21-1

**气体分子的 Ehrenfest 模型。**

考虑有 $N$ 个气体分子的容器分成左右两部分，记左侧部分的分子数为 $X_{n}$。设气体分子的扩散行为为：每个时间单位内有且仅有一个分子移到另一侧。则 $\{X_{n}\}$ 是一个**状态空间为 $S = \{0,1,2,\cdots,N\}$ 的 Markov 链**，其转移概率为
$$
\boldsymbol{P} = \begin{pmatrix}
0 & 1 & 0 & 0 & \cdots & 0 & 0 \\
\cfrac{1}{N} & 0 & \cfrac{N-1}{N} & 0 & \cdots & 0 & 0 \\
0 & \cfrac{2}{N} & 0 & \cfrac{N-2}{N} & \cdots & 0 & 0 \\
0 & 0 & \cfrac{3}{N} & 0 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & \vdots & \vdots & \ddots & \ddots & \ddots & \vdots \\
0 & 0 & 0 & 0 & \cdots & 1 & 0 \\
\end{pmatrix}
$$
易见该 Markov 链**不可约且有限**，因此**所有状态均为常返态**，且周期为 2。将方程 $\v{\pi} = \v{\pi} \boldsymbol{P}$ 展开，有
$$
\begin{cases}
\pi_{0} = \cfrac{1}{N} \pi_{1}, \\
\pi_{1} = \pi_{0} + \cfrac{2}{N} \pi_{2}, \\
\pi_{2} = \cfrac{N-1}{N} \pi_{1} + \cfrac{3}{N} \pi_{3}, \\
\cdots \\
\pi_{k} = \cfrac{N-(k-1)}{N} \pi_{k-1} + \cfrac{k+1}{N} \pi_{k+1}, \\
\cdots \\
\pi_{N} = \cfrac{1}{N} \pi_{N-1}
\end{cases}
$$
注意到此递推关系形如
$$
\binom{N}{k} = \dfrac{N-(k-1)}{N} \binom{N}{k-1} + \dfrac{k+1}{N} \binom{N}{k+1}
$$
因此可猜测平稳分布为二项分布形式 $\pi_{k} = \pi_{0} \binom{N}{k}$，代入归一化条件 $\sum\limits_{k=0}^{N} \pi_{k} = 1$ 可得 $\pi_{0} = \dfrac{1}{2^{N}}$，即
$$
\pi_{k} = \dfrac{1}{2^{N}} \binom{N}{k}, \qquad k = 0,1,2,\cdots,N
$$

## L22 (12/25)

### L22-1

假设某人共有 $N$ 把伞，分别放在家和公司两地。每当他在雨天从家出发去公司时，**若家中有伞则带一把伞**，否则不带；同理，当他在雨天从公司回家时，**若公司有伞则带一把伞**，否则不带。假设每次出行时下雨的概率均为 $p$，求该人**在长期内因忘带伞而被淋湿的概率**。

注意到家中与公司中伞的数量的对称性，设 $X_{n}$ 表示第 $n$ 次出行时**手边**伞的数量，则 $\{X_{n}\}$ 是一个状态空间为 $S = \{0,1,2,\cdots,N\}$ 的 Markov 链，其转移关系为
$$
X_{n+1} = \begin{cases}
N - X_{n}, & \text{没带伞}, & \text{i.e.} & X_{n} = 0 \text{ OR 没下雨}\\
N - X_{n} + 1, & \text{带伞}, & \text{i.e.} & X_{n} \ge 1 \text{ AND 下雨}
\end{cases}
$$
即 1 步转移概率为
$$
\boldsymbol{P} = \begin{pmatrix}
0 & 0 & 0 & \cdots & 0 & 0 & 1 \\
0 & 0 & 0 & \idots & 0 & 1 - p & p \\
0 & 0 & 0 & \idots & 1 - p & p & 0 \\
\vdots & \idots & \idots & \idots & \idots & \idots & \vdots \\
0 & 0 & 1 - p & \idots & 0 & 0 & 0 \\
0 & 1 - p & p & \idots & 0 & 0 & 0 \\
1 - p & p & 0 & \cdots & 0 & 0 & 0 \\
\end{pmatrix}
$$

易见该 Markov 链**不可约且有限**，因此**所有状态均为常返态**。将方程 $\v{\pi} = \v{\pi} \boldsymbol{P}$ 展开，有
$$
\begin{cases}
\pi_{0} = (1-p) \pi_{N}, \\
\pi_{1} = (1-p) \pi_{N-1} + p \pi_{N}, \\
\pi_{2} = (1-p) \pi_{N-2} + p \pi_{N-1}, \\
\cdots \\
\pi_{k} = (1-p) \pi_{N-k} + p \pi_{N-(k-1)}, \\
\cdots \\
\pi_{N-1} = (1-p) \pi_{1} + p \pi_{2}, \\
\pi_{N} = \pi_{0} + p \pi_{1}
\end{cases}
$$
由 $\pi_{N} = \pi_{0} + p \pi_{1} = (1-p) \pi_{N} + p \pi_{1}$，可得 **$\pi_{1} = \pi_{N} = \cfrac{1}{1-p} \pi_{0}$**。进而，可依次得到 $\pi_{N-1} = \pi_{N}$、$\pi_{2} = \pi_{N}$、$\pi_{N-2} = \pi_{N}$、$\cdots$，最终可得**平稳分布**为
$$
\pi_{1} = \pi_{2} = \cdots = \pi_{N} = \dfrac{1}{1-p} \pi_{0}
$$
归一化有 $\sum\limits_{k=0}^{N} \pi_{k} = \cfrac{N + (1-p)}{1-p} \pi_{0} = 1$，得 $\pi_{0} = \dfrac{1-p}{1 - p + N}$，即所求长期内因忘带伞而被淋湿的概率为 $\pi_{0} \cdot p = \dfrac{p(1-p)}{1 - p + N}$。

### L22-2

考虑下面有限状态 Markov 链：

![[L22-2.png]]

显然可以分为 3 个强连通分支：$\left\{ 1, 2 \right\}$、$\left\{ 3, 4, 5 \right\}$、$\left\{ 6, 7 \right\}$。其中，$\left\{ 1, 2 \right\}$ 存在出口，因此为瞬态分支；$\left\{ 3, 4, 5 \right\}$ 和 $\left\{ 6, 7 \right\}$ 均无出口，因此为**常返**分支。

**周期性**同样按照分支讨论。对于瞬态分支 $\left\{ 1, 2 \right\}$，只能在偶数步内回到状态 1 或状态 2，因此周期均为 2；对于常返分支 $\left\{ 3, 4, 5 \right\}$，可以**经 2 步或 3 步**回到出发态，因此周期为 1；对于常返分支 $\left\{ 6, 7 \right\}$，状态 6 上**有自环**，因此周期为 1。

考虑**从状态 1 出发经无穷步后到达状态 5 的概率 $\lim\limits_{ n \to \infty }P \left\{ X_{n} = 5 \mid X_{0} = 1 \right\}$**，分为两步讨论：
1. 首先考虑**从状态 1 出发最终进入常返分支 $\left\{ 3,4,5 \right\}$ 的概率**，设从状态 1 和状态 2 出发最终处于 $\left\{ 3,4,5 \right\}$ 的概率分别为 $f_{1}$ 和 $f_{2}$，则有 
$$
\begin{cases}
f_{1} = \cfrac{1}{3} \times 1 + \cfrac{2}{3} f_{2}, \\
f_{2} = \cfrac{2}{3} f_{1} + \cfrac{1}{3} \times 0
\end{cases}
\implies
\begin{cases}
f_{1} = \cfrac{3}{5}, \\
f_{2} = \cfrac{2}{5}
\end{cases}
$$
2. 接着考虑**在进入常返分支 $\left\{ 3,4,5 \right\}$ 后最终到达状态 5 的概率**，此为该分支内的平稳分布 $\pi_{5}$，由方程 $\v{\pi} = \v{\pi} \boldsymbol{P}$ 可得
$$
\boldsymbol{P} = \begin{matrix}
3 \\[8pt] 4 \\[8pt] 5
\end{matrix} \begin{pmatrix}
0 & \cfrac{1}{3} & \cfrac{2}{3} \\
\cfrac{2}{3} & 0 & \cfrac{1}{3} \\
\cfrac{1}{3} & \cfrac{2}{3} & 0
\end{pmatrix}
\implies
\v{\pi} = \begin{matrix}
3 \\[8pt] 4 \\[8pt] 5
\end{matrix} \begin{pmatrix}
\cfrac{1}{3} \\ \cfrac{1}{3} \\ \cfrac{1}{3}
\end{pmatrix}
$$

综上所述，有
$$
\lim\limits_{ n \to \infty }P \left\{ X_{n} = 5 \mid X_{0} = 1 \right\} = f_{1} \cdot \pi_{5} = \dfrac{3}{5} \times \dfrac{1}{3} = \dfrac{1}{5}
$$

### L22-3

两个赌徒 A 和 B 对赌，每次赌注 1 元，A 每次赢的概率为 $p$，输的概率为 $1-p$，当一方输光钱时对赌结束。设初始 A 有 2 元，B 有 1 元，求 A 赢得对赌的时间的分布。

设 $X_{n}$ 表示 A 在第 $n$ 次赌注后所持有的金额，则 $\{X_{n}\}$ 是一个状态空间为 $S = \{0,1,2,3\}$ 的 Markov 链，其转移概率为
$$
\boldsymbol{P} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
1-p & 0 & p & 0 \\
0 & 1-p & 0 & p \\
0 & 0 & 0 & 1 \\
\end{pmatrix}
$$
显然状态 0 和状态 3 为吸收态进而常返，状态 1 和状态 2 为滑过态。

考虑**从状态 2 到达状态 3 的首达概率分布 $f_{2,3}(n)$**。$n$ 为偶数时，必然无法首次到达状态 3，因此 $f_{2,3}(n) = 0$；当 $n = 2k + 1$ 为奇数时，有
$$
f_{2,3}(2k+1) = (p(1-p))^{k} p = p^{k+1} (1-p)^{k}
$$
进而，**$n$ 步内到达状态 3 的概率**为
$$
P_{2,3}(n) = \sum\limits_{k=0}^{\lfloor (n-1)/2 \rfloor} f_{2,3}(2k+1) = \sum\limits_{k=0}^{\lfloor (n-1)/2 \rfloor} p^{k+1} (1-p)^{k} = p \cdot \dfrac{1 - (p(1-p))^{\lfloor (n+1)/2 \rfloor}}{1 - p(1-p)}
$$

## L23 (12/30)

### L23-1

**生灭模型 (Birth-Death model)。**

设 $\{X(t), t \ge 0\}$ 是一个状态空间为 $S = \{0,1,2,\cdots\}$ 的 Markov 过程，且其状态转移分为**独立**的两部分：
+ **生 (birth)**：状态从 $i$ 增加 1 的概率为 $\lambda_{i} \Delta t + o(\Delta t)$，增加 $\ge 2$ 的概率为 $o(\Delta t)$；
+ **灭 (death)**：状态从 $i$ 减少 1 的概率为 $\mu_{i} \Delta t + o(\Delta t)$，减少 $\ge 2$ 的概率为 $o(\Delta t)$。

则知转移概率为
$$
\begin{align} 
&
\begin{aligned}
P_{n, n}(\Delta t) &= (1 - \lambda_{i} \Delta t + o(\Delta t))(1 - \mu_{i} \Delta t + o(\Delta t))  \\
&\hspace{1em} + (\lambda_{i} \Delta t + o(\Delta t))(\mu_{i} \Delta t + o(\Delta t)) + o(\Delta t) \\
&= 1 - (\lambda_{i} + \mu_{i}) \Delta t + o(\Delta t), 
\end{aligned} \\
&
\begin{aligned}
P_{n, n+1}(\Delta t) &= (\lambda_{i} \Delta t + o(\Delta t)) (1 - \mu_{i} \Delta t + o(\Delta t)) \\
&\hspace{1em} + o(\Delta t) (\mu_{i} \Delta t + o(\Delta t)) + o(\Delta t) \\
&= \lambda_{i} \Delta t + o(\Delta t), \\
\end{aligned} \\
&
\begin{aligned}
P_{n, n-1}(\Delta t) &= (1 - \lambda_{i} \Delta t + o(\Delta t)) (\mu_{i} \Delta t + o(\Delta t)) \\
&\hspace{1em} + (\lambda_{i} \Delta t + o(\Delta t)) o(\Delta t) + o(\Delta t) \\
&= \mu_{i} \Delta t + o(\Delta t),
\end{aligned} \\
& P_{n, j}(\Delta t) = o(\Delta t), \qquad |j - n| \ge 2
\end{align}
$$
给出 $\boldsymbol{Q}$ 矩阵为
$$
\boldsymbol{Q} = \begin{pmatrix}
-\lambda_{0} & \lambda_{0}  \\
\mu_{1} & -(\lambda_{1} + \mu_{1}) & \lambda_{1} \\
& \mu_{2} & -(\lambda_{2} + \mu_{2}) & \lambda_{2}  \\
& & \ddots & \ddots & \ddots
\end{pmatrix}
$$
解方程 $\v{\pi} \boldsymbol{Q} = \v{0}$，展开有
$$
\begin{cases}
-\lambda_{0} \pi_{0} + \mu_{1} \pi_{1} = 0,  & \Longrightarrow \quad \pi_{1} = \cfrac{\lambda_{0}}{\mu_{1}} \pi_{0}, \\
\lambda_{0} \pi_{0} - (\lambda_{1} + \mu_{1}) \pi_{1} + \mu_{2} \pi_{2} = 0, & \Longrightarrow \quad \pi_{2} = \dfrac{\lambda_{1}}{\mu_{2}} \pi_{1}, \\
\cdots & \Longrightarrow \quad \cdots \\
\lambda_{n-2} \pi_{n-2} - (\lambda_{n-1} + \mu_{n-1}) \pi_{n-1} + \mu_{n} \pi_{n} = 0, & \Longrightarrow \quad \pi_{n} = \dfrac{\lambda_{n-1}}{\mu_{n}} \pi_{n-1}, \\
\cdots & \Longrightarrow \quad \cdots
\end{cases}
$$
因此可递推得到
$$
\pi_{n} = \dfrac{\lambda_{0} \lambda_{1} \cdots \lambda_{n-1}}{\mu_{1} \mu_{2} \cdots \mu_{n}} \pi_{0} = \prod\limits_{i=0}^{n-1} \dfrac{\lambda_{i}}{\mu_{i+1}} \pi_{0}
$$
归一化条件为 $\sum\limits_{n=0}^{\infty} \pi_{n} = \pi_{0} \left( 1 + \sum\limits_{n=1}^{\infty} \prod\limits_{i=0}^{n-1} \dfrac{\lambda_{i}}{\mu_{i+1}} \right) = 1$，当**级数收敛**时，有
$$
\pi_{0} = \dfrac{1}{1 + \sum\limits_{n=1}^{\infty} \prod\limits_{i=0}^{n-1} \dfrac{\lambda_{i}}{\mu_{i+1}}}
$$

### L23-2

**M/M/1 队列模型。**

设顾客到达服从参数为 $\lambda$ 的 Poisson 过程，服务时间服从参数为 $\mu$ 的指数分布，且假设系统中有且仅有 1 个服务台，则该排队系统可表示为一个**生灭模型**，其**生灭率**分别为
$$
\lambda_{n} = \lambda, \qquad \mu_{n} = \mu
$$
因此平稳分布为
$$
\pi_{n} = \left( \dfrac{\lambda}{\mu} \right)^{n} \pi_{0} 
= \cfrac{\left( \cfrac{\lambda}{\mu} \right)^{n}}{\sum\limits_{n=0}^{\infty} \left( \cfrac{\lambda}{\mu} \right)^{n}} 
= \cfrac{\left( \cfrac{\lambda}{\mu} \right)^{n}}{\cfrac{1}{1 - \cfrac{\lambda}{\mu} }} 
= \left( 1 - \dfrac{\lambda}{\mu} \right) \left( \dfrac{\lambda}{\mu} \right)^{n}
$$
注意，当且仅当 $\lambda < \mu$ 时级数收敛、系统稳定。

### L23-3

**M/M/$N$ 队列模型。**

设顾客到达服从参数为 $\lambda$ 的 Poisson 过程，服务时间服从参数为 $\mu$ 的指数分布，且假设系统中有 $N$ 个服务台，则该排队系统可表示为一个**生灭模型**，其**生灭率**分别为
$$
\lambda_{n} = \lambda, \qquad \mu_{n} = \begin{cases}
n \mu, & 1 \le n \le N, \\
N \mu, & n \ge N+1
\end{cases}
$$
因此平稳分布为
$$
\pi_{n} = \begin{cases}
\dfrac{(\lambda/\mu)^{n}}{n!} \pi_{0}, & 0 \le n \le N, \\
\dfrac{(\lambda/\mu)^{n}}{N! N^{n-N}} \pi_{0}, & n \ge N+1
\end{cases}
$$

