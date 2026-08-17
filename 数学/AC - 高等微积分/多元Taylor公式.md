## 多元Taylor公式

多元Taylor公式把函数增量分解为梯度给出的一阶线性项、Hessian矩阵给出的二阶型以及余项。沿线段把多元函数限制为一元函数，可以直接从一元Taylor公式得到多元版本。

Peano余项刻画基点附近的渐近结构，Lagrange余项给出连接基点与目标点的线段上的中间点。使用公式前应核对定义域包含该线段，并明确所需的连续偏导阶数。

本章把[[Taylor公式与近似|一元Taylor公式]]推广到多元函数，并为[[多元函数的极值]]提供Hessian二次型。

### 一阶与二阶Taylor公式

> [!definition]
> 我们称函数 $F:\mathbb{R}^n\times\mathbb{R}^n\rightarrow \mathbb{R}$ 为**双线性型**，如果 $\forall X_0,Y_0\in\mathbb{R}^n$，函数 $Y \mapsto F(X_0,Y)$ 和函数 $X \mapsto F(X,Y_0)$ 均为 $\mathbb{R}^n$ 上的线性函数。

对双线性函数 $F(X,Y)$，记 $X=(x_1,\cdots,x_n)^\mathrm{T}=\sum_{i=1}^nx_i\mathbf{e}_i$，$Y=(y_1,\cdots,y_n)^\mathrm{T}=\sum_{j=1}^ny_j\mathbf{e}_j$，则

$$
F(X,Y)=F\left(\sum_{i=1}^nx_i\mathbf{e}_i,Y\right)=\sum_{i=1}^nx_i F(\mathbf{e}_i,Y)
=\sum_{i=1}^nx_i F\left(\mathbf{e}_i,\sum_{j=1}^ny_j\mathbf{e}_j\right)
=\sum_{i=1}^n\sum_{j=1}^n x_i y_j F(\mathbf{e}_i,\mathbf{e}_j)
$$

令 $a_{ij}=F(\mathbf{e}_i,\mathbf{e}_j)$，$A=(a_{ij})_{1\le i,j\le n}$，则

$$
F(X,Y)=\sum_{i=1}^n\sum_{j=1}^n x_i y_j F(\mathbf{e}_i,\mathbf{e}_j)
=\sum_{i=1}^nx_i \sum_{j=1}^na_{ij}y_j
=\sum_{i=1}^nx_i(AY)_i
=X^\mathrm{T} AY
$$

即双线性函数可以用矩阵表示。

> [!theorem] 多元函数的带Lagrange余项的一阶Taylor展式
> 设 $X_0\in\mathbb{R}^n$，$r>0$，实值函数 $f\in\mathscr{C}^{(2)}(B(X_0,r))$，则 $\forall X\in B(X_0,r)$，$\exists \theta\in (0,1)$ 使得
> $$
> \begin{aligned}
> f(X)&=f(X_0)+\sum_{j=1}^n\frac{\partial f}{\partial x_j}(X_0)(x_j-x_j^{(0)})+\frac{1}{2!}\sum_{i=1}^n\sum_{j=1}^n\frac{\partial^2f}{\partial x_i\partial x_j}(X_{\theta})(x_i-x_i^{(0)})(x_j-x_j^{(0)})\\
> &=f(X_0)+\boldsymbol{J_{f}(X_0)}\Delta X+\frac{1}{2!}(\Delta X)^\mathrm{T} \boldsymbol{H_f(X_{\theta})}\Delta X
> \end{aligned}
> $$
> 其中 $\Delta X=X-X_0$，$X_{\theta}=X_0+\theta (X-X_0)$，$J_{f}(X_0) = \bigg(\dfrac{\partial f}{\partial x_1}(X_0),\dfrac{\partial f}{\partial x_2}(X_0),\cdots,\dfrac{\partial f}{\partial x_n}(X_0)\bigg)$ 是 $f$ 在点 $X_0$ 的Jacobi矩阵，
> $H_f(X_{\theta}) = \bigg(\dfrac{\partial^2f}{\partial x_i\partial x_j}(X_{\theta})\bigg)_{1\le i,j\le n}$ 为 $f$ 在点 $X_{\theta}$ 的**Hessian矩阵**。

由这一定理，当 $X\rightarrow X_0$ 时，$H_f(X_\theta)=H_f\left(X_0+\theta(X-X_0)\right)=H_f(X_0)+\v{o}(1)$，则得

> [!theorem] 多元函数的带Peano余项的二阶Taylor展式
> 设 $X_0\in\mathbb{R}^n$，$r>0$，实值函数 $f\in\mathscr{C}^{(2)}(B(X_0,r))$，则 $\forall X\in B(X_0,r)$，当 $X\rightarrow X_0$ 时，
> $$
> f(X)=f(X_0)+J_{f}(X_0)\Delta X+\frac{1}{2!}(\Delta X)^\mathrm{T} H_f(X_0)\Delta X+o(\|\Delta X\|^2)
> $$
