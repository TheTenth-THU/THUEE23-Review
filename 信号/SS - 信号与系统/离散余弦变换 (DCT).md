## 一维离散余弦变换

> [!definition] 离散余弦变换 (DCT)
> 矢量 $\v{x} = \begin{pmatrix} x_{0} \\ x_{1} \\ \cdots \\ x_{N-1} \end{pmatrix}$ 的**离散余弦变换 (DCT)** 定义为 $\v{y} = \begin{pmatrix} y_{0} \\ y_{1} \\ \cdots \\ y_{N-1} \end{pmatrix}$，其中
> $$
> \begin{align}
> &y_{0} = \sqrt{\dfrac{1}{N}} \sum\limits_{n=0}^{N-1} x_{n}  \\
> &y_{k} = \sqrt{\dfrac{2}{N}} \sum\limits_{n=0}^{N-1} x_{n} \cos \dfrac{(2n + 1)k\pi}{2N}, \quad k=1,2,\cdots,N-1
> \end{align}
> $$
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

