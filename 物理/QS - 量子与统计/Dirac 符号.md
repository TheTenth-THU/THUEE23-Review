## 使用 Dirac 符号表示量子态

### 态的 Dirac 符号表示

物理状态是客观存在的，不依赖于选取的表象，因此可以用**抽象矢量空间**中的**态矢量**来表示量子态，即使用 **Dirac 符号 (Dirac notation)** 表示量子态
$$
\begin{align} 
\psi\left( \v{r}, t \right) &\longleftrightarrow \ket{\psi(t)}  \\
\psi^{*} \left( \v{r}, t \right) &\longleftrightarrow \bra{\psi(t)} = (\ket{\psi(t)})^{\dagger}
\end{align}
$$
其中 $\ket{\psi(t)}$ 称为 **ket 矢量**，$\bra{\psi(t)}$ 称为 **bra 矢量**。

Bra 和 ket 之间定义了 **braket 内积**运算
$$
\braket{\phi(t)|\psi(t)} = \dint \phi^{*}\left( \v{r}, t \right) \psi\left( \v{r}, t \right) \dif \v{r}
$$
特别地，若将任意态 $\ket{\psi}$ 在正交归一系 $\left\{ \ket{u_{n}} \right\}$ 下展开为
$$
\ket{\psi} = \sum_{n} c_{n} \ket{u_{n}}
$$
则内积
$$
\braket{ u_{n} | \psi } = \sum\limits_{m} c_{m} \underbrace{ \braket{ u_{n} | u_{m} } }_{ \delta_{m,n} } = c_{n}
$$
即表示展开系数 $c_{n}$。

#### 坐标本征矢

位置算符 $\hat{\v{r}}$ 的本征函数系为 $\left\{ \delta^{3}\left( \v{r} - \v{r}_{0} \right) \right\}$，现在用 Dirac 符号简记为
$$
\ket{\v{r}_{0}} \longleftrightarrow \delta^{3}\left( \v{r} - \v{r}_{0} \right) 
$$
于是，量子态 $\varPsi\left( \v{r}, t \right)$ 在坐标表象下的展开式
$$
\varPsi\left( \v{r}, t \right) = \dint \varPsi\left( \v{r}_{0}, t \right) \delta^{3} \left( \v{r} - \v{r}_{0} \right) \dif \v{r}_{0} = \braket{ \v{r} | \psi(t) }    
$$
这样，坐标表象概率幅 $\varPsi\left( \v{r}_{0}, t \right)$ 即表示为 $\ket{ \psi(t) }$。

坐标本征矢之间的正交归一关系表现为
$$
\braket{ \v{r} | \v{r}' } = \delta^{3}\left( \v{r} - \v{r}' \right)
$$

#### 动量本征矢

动量算符 $\hat{\v{p}}$ 的本征函数系为 $\left\{ \phi_{\v{p}}\left( \v{r} \right) = \cfrac{1}{(2\pi \hbar)^{3/2}} \e^{\J \v{p} \cdot \v{r} / \hbar} \right\}$，现在用 Dirac 符号简记为
$$
\ket{\v{p}} \longleftrightarrow \phi_{\v{p}}\left( \v{r} \right)
$$
于是，量子态 $\varPsi\left( \v{r}, t \right)$ 在动量表象下的展开式
$$
\varPsi\left( \v{r}, t \right) = \dint c\left( \v{p}, t \right) \phi_{\v{p}}\left( \v{r} \right) \dif \v{p} = \braket{ \v{p} | \psi(t) }
$$
这样，动量表象概率幅 $c\left( \v{p}, t \right)$ 即表示为 $\ket{ \psi(t) }$。

上述展开式本质上仍是在坐标表象下的表示，只不过将动量本征函数系作为基底来展开量子态；动量表象下，动量算符 $\hat{\v{p}}$ 的本征函数系为 $\left\{ \delta^{3}\left( \v{p} - \v{p}_{0} \right) \right\}$，这样展开式就为
$$
c\left( \v{p}, t \right) = \dint c\left( \v{p}_{0}, t \right) \delta^{3} \left( \v{p} - \v{p}_{0} \right) \dif \v{p}_{0} = \braket{ \v{p} | \psi(t) }
$$

动量本征矢之间的正交归一关系表现为
$$
\braket{ \v{p} | \v{p}' } = \delta^{3}\left( \v{p} - \v{p}' \right)
$$

### 算符的 Dirac 符号表示

Dirac 符号并不改写算符的表示形式，但将其迁移到了抽象矢量空间中。给定力学量算符 $\hat{Q}$，作用在态矢量 $\ket{\psi(t)}$ 上时，有
$$
\hat{Q} \ket{\psi(t)} = \ket{\phi(t)}
\longleftrightarrow
\hat{Q}\left( \v{r}, -\I\hbar \nabla \right) \psi\left( \v{r}, t \right) = \phi\left( \v{r}, t \right)
$$

> [!example] Schrödinger 方程的 Dirac 符号表示
> 给定哈密顿算符 $\hat{H}$，时间演化的 Schrödinger 方程可表示为
> $$
> \I \hbar \dfrac{\partial}{\partial t} \ket{\psi(t)} = \hat{H} \ket{\psi(t)}
> $$
> 取坐标表象 $\psi\left( \v{r},t \right) = \braket{ \v{r} | \psi(t) }$，即得到对应的波函数形式
> $$
> \I \hbar \dfrac{\partial}{\partial t} \psi\left( \v{r}, t \right) = \hat{H}\left( \v{r}, -\I\hbar \nabla \right) \psi\left( \v{r}, t \right)
> $$

#### Hermitian 算符的表示

对于 Hermitian 算符 $\hat{Q}$，有
$$
\dint \phi^{*}\left( \v{r}, t \right) \hat{Q}\left( \v{r}, -\I\hbar \nabla \right) \psi\left( \v{r}, t \right) \dif \v{r} = \dint \left[ \hat{Q}\left( \v{r}, -\I\hbar \nabla \right) \phi\left( \v{r}, t \right) \right]^{*} \psi\left( \v{r}, t \right) \dif \v{r}
$$
用 Dirac 符号表示为
$$
\braket{ \phi(t) \Big| \hat{Q} \Big| \psi(t) } = \left( \hat{Q} \ket{\phi(t)}  \right) ^{\dagger} \ket{\psi(t)} 
$$
即可有
$$
\bra{\phi(t)} \hat{Q} = \left( \hat{Q} \ket{\phi(t)}  \right) ^{\dagger}
$$
或直接写为
$$
\hat{Q} = \hat{Q}^{\dagger}
$$
与[[矩阵表象#^3e7594|矩阵表象中 Hermitian 算符的表示]]一致。

#### 单位算符的生成

给定正交归一系 $\left\{ \ket{u_{n}} \right\}$，任意态 $\ket{\psi}$ 可展开为
$$
\ket{\psi} = \sum_{n} c_{n} \ket{u_{n}} = \sum\limits_{n} \braket{ u_{n} | \psi } \ket{u_{n}}
= \sum_{n} \ket{u_{n}} \braket{ u_{n} | \psi }
$$
由于上述展开式对任意态 $\ket{\psi}$ 均成立，因此有
$$
\hat{I} = \sum_{n} \ket{u_{n}} \bra{u_{n}}
$$
即生成了**单位算符 $\hat{I}$**。

这一性质可用于在适当情况下插入 $\sum\limits_{n} \ket{u_{n}} \bra{u_{n}}$，可能能起到简化计算的效果。

> [!note] 正交归一基底生成单位算符的波函数形式
> $\sum\limits_{n} \ket{u_{n}} \bra{u_{n}} = \hat{I}$ 并非 Dirac 符号独有的性质，在波函数形式中同样成立。
> 
> 取坐标表象 $\psi\left( \v{r} \right) = \braket{ \v{r} | \psi }$，则有
> $$
> \sum\limits_{n} u_{n}\left( \v{r} \right) u_{n}^{*}\left( \v{r}' \right) = \sum\limits_{n} \braket{ \v{r} | u_{n} } \braket{ u_{n} | \v{r}' } = \braket{ \v{r} \Big| \hat{I} \Big| \v{r}' } = \delta^{3}\left( \v{r} - \v{r}' \right)
> $$
> 
> 对于连续本征值的情形，同样有
> $$
> \dint u_{\lambda}\left( \v{r} \right) u_{\lambda}^{*}\left( \v{r}' \right) \dif \lambda = \dint \braket{ \v{r} | \lambda } \braket{ \lambda | \v{r}' } \dif \lambda = \braket{ \v{r} \Big| \hat{I} \Big| \v{r}' } = \delta^{3}\left( \v{r} - \v{r}' \right)
> $$
> 其中 $\lambda$ 表示连续本征值变量，有 $\hat{I} = \dint \ket{\lambda} \bra{\lambda} \dif \lambda$。

## 使用 Dirac 符号进行表象变换

### Dirac 符号下的表象变换公式

已知 $\left\{ \ket{u_{n}} \right\}$ 和 $\left\{ \ket{v_{m}} \right\}$ 分别为两个正交归一基底，则任意态 $\ket{\psi}$ 在这两个基底下的展开式为
$$
\ket{\psi} = \sum_{n} a_{n} \ket{u_{n}} = \sum_{m} b_{m} \ket{v_{m}}
$$
其中 $a_{n} = \braket{ u_{n} | \psi }$，$b_{m} = \braket{ v_{m} | \psi }$。由此，可有
$$
b_{k} = \braket{ v_{k} | \psi } = \bra{ v_{k} }  \sum_{n} a_{n} \ket{u_{n}} = \sum_{n} \braket{ v_{k} | u_{n} } a_{n}
$$

> [!thm.] Dirac 符号下的表象变换公式
> 同一量子态 $\ket{\psi}$ 在不同正交归一基底 $\left\{ \ket{u_{n}} \right\}$ 和 $\left\{ \ket{v_{m}} \right\}$ 下的展开系数 $a_{n}$ 和 $b_{m}$ 之间的关系为
> $$
> b_{k} = \sum_{n} \braket{ v_{k} | u_{n} } a_{n}
> $$
> 其中，$\braket{ v_{k} | u_{n} }$ 可视为表象变换矩阵的 $(k,n)$ 元，即**表象变换矩阵**为
> $$
> \big( \boldsymbol{S} \big) _{k,n} = \braket{ v_{k} | u_{n} }
> $$

### 表象变换矩阵的性质

注意到表象变换矩阵的元素为两个正交归一基底矢量的内积，考虑其共轭转置
$$
\big( \boldsymbol{S}^{\dagger} \big) _{m,k} = \big( \boldsymbol{S} \big) _{k,m}^{*}  = \braket{ v_{k} | u_{m}}^{*} = \braket{ u_{m} | v_{k} }
$$
有
$$
\begin{align}
\big( \boldsymbol{S}^{\dagger} \boldsymbol{S} \big)_{m,n} &= \sum\limits_{k} \big( \boldsymbol{S}^{\dagger} \big) _{m,k} \big( \boldsymbol{S} \big) _{k,n} = \sum\limits_{k} \braket{ u_{m} | v_{k} } \braket{ v_{k} | u_{n} } \\
&= \bra{ u_{m} } \left( \sum\limits_{k} \ket{ v_{k} } \bra{ v_{k} } \right) \ket{ u_{n} } = \bra{ u_{m} } \hat{I} \ket{ u_{n} }  \\
&= \braket{ u_{m} | u_{n} } = \delta_{m,n}
\end{align}
$$
因此 $\boldsymbol{S}^{\dagger}\boldsymbol{S} = \boldsymbol{I}$，即表象变换矩阵是**酉矩阵 (unitary matrix)**。