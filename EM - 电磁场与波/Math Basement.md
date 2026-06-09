## Vector Algebra, 矢量代数

### Introduction, 矢量的定义

Consider a vector $\v{A}$ in 3D space, it can be represented as 
$$\v{A} = A_x\vu{x} + A_y\vu{y} + A_z\vu{z}$$
where $A_x, A_y, A_z$ are the **components** of the vector in the $\vu{x}, \vu{y}, \vu{z}$ directions respectively. It can also be represented as $\v{A} = \begin{pmatrix} A_x \\ A_y \\ A_z \end{pmatrix}$.

**By definition** we denote 
$$A = \| \v{A} \| = \sqrt{A_x^2 + A_y^2 + A_z^2}$$
which is a **scalar** quantity representing the magnitude of the vector.

> [!Note]+ Curvilinear coordinates
> In some cases, we may use **curvilinear coordinates** to represent the vector, such as _cylindrical_ or _spherical_ coordinates. 
> 
> + **Cylindrical coordinates** use $(s, \phi, z)$ to represent the vector, where $s$ is the distance from the $z$ axis, and $\phi$ is the angle from the $x$ axis. 
> 	+ Conversion with Cartesian coordinates: $$x = s\cos\phi,\quad y = s\sin\phi,\quad z = z$$
> 	+ Unit vectors: $$\begin{cases}
> 	  \vu{s} = \cos\phi\vu{x} + \sin\phi\vu{y} \\
> 	  \vu{\phi} = -\sin\phi\vu{x} + \cos\phi\vu{y} \\
> 	  \vu{z} = \vu{z}
> 	  \end{cases}$$
> + **Spherical coordinates** use $(r, \theta, \phi)$ to represent the vector, where $r$ is the distance from the origin, $\theta$ is the angle from the $z$ axis, and $\phi$ is the angle from the $x$ axis.
> 	+ Conversion with Cartesian coordinates: $$x = r\sin\theta\cos\phi,\quad y = r\sin\theta\sin\phi,\quad z = r\cos\theta$$
> 	+ Unit vectors: $$\begin{cases}
> 	  \vu{r} = \sin\theta\cos\phi\vu{x} + \sin\theta\sin\phi\vu{y} + \cos\theta\vu{z} \\
> 	  \vu{\theta} = \cos\theta\cos\phi\vu{x} + \cos\theta\sin\phi\vu{y} - \sin\theta\vu{z} \\
> 	  \vu{\phi} = -\sin\phi\vu{x} + \cos\phi\vu{y}
> 	  \end{cases}$$
> 
> We should be careful with the unit vectors in curvilinear coordinates, since they are **not constant**, unlike the Cartesian coordinates.

Given field point  $\v{r} =\begin{pmatrix} x\\ y \\ z \end{pmatrix}$ and source point $\v{r'} =\begin{pmatrix} x'\\ y' \\ z' \end{pmatrix}$, the **separation vector** is given by $\v{\mathscr{r}} = \v{r} - \v{r'} = \begin{pmatrix} x - x'\\ y - y' \\ z - z' \end{pmatrix}$. Its direction is from the source point to the field point, and can be written as $\vu{\mathscr{r}} = \dfrac{\v{\mathscr{r}}}{\| \v{\mathscr{r}} \|}$.

### Vector Addition & Subtraction, 矢量的加法与减法

Given two vectors $\v{A} = \begin{pmatrix} A_x \\ A_y \\ A_z \end{pmatrix}$ and $\v{B} = \begin{pmatrix} B_x \\ B_y \\ B_z \end{pmatrix}$, their **sum** $\v{A} + \v{B}$ is given by $\begin{pmatrix} A_x + B_x \\ A_y + B_y \\ A_z + B_z \end{pmatrix}$, and their **difference** $\v{A} - \v{B}$ is given by $\begin{pmatrix} A_x - B_x \\ A_y - B_y \\ A_z - B_z \end{pmatrix}$.

### Dot Product, 点积

Given two vectors $\v{A} = \begin{pmatrix} A_x \\ A_y \\ A_z \end{pmatrix}$ and $\v{B} = \begin{pmatrix} B_x \\ B_y \\ B_z \end{pmatrix}$, their **dot product** $\v{A} \cdot \v{B}$ is given by
$$\v{A} \cdot \v{B} = A_xB_x + A_yB_y + A_zB_z$$

We can also write 
$$\v{A} \cdot \v{B} = AB\cos\theta$$
where $A = \| \v{A} \|$, $B = \| \v{B} \|$, and $\theta$ is the angle between the two vectors.

### Cross Product, 叉积

Given two vectors $\v{A} = \begin{pmatrix} A_x \\ A_y \\ A_z \end{pmatrix}$ and $\v{B} = \begin{pmatrix} B_x \\ B_y \\ B_z \end{pmatrix}$, their **cross product** $\v{A} \times \v{B}$ is given by
$$\v{A} \times \v{B} = \begin{pmatrix} A_yB_z - A_zB_y \\ A_zB_x - A_xB_z \\ A_xB_y - A_yB_x \end{pmatrix}$$

Notice that the result is a **vector**, and its direction is perpendicular to both $\v{A}$ and $\v{B}$, so cross product is **not commutative**. In fact, we have $\v{A} \times \v{B} = -\v{B} \times \v{A}$.

> [!Note] Triple product
> Given three vectors $\v{A}, \v{B}, \v{C}$, we have 
> + the **scalar triple product**, which is given by
> $$\v{A} \cdot (\v{B} \times \v{C})$$
> and we have $$\v{A} \cdot (\v{B} \times \v{C}) = \v{B} \cdot (\v{C} \times \v{A}) = \v{C} \cdot (\v{A} \times \v{B})$$
> 
> + and the **vector triple product**, which is given by
> $$\v{A} \times (\v{B} \times \v{C})$$
> and it can be calculated by $$\v{A} \times (\v{B} \times \v{C}) = \v{B}(\v{A} \cdot \v{C}) - \v{C}(\v{A} \cdot \v{B})$$

^f0b7e4

## Vector Derivatives, 矢量微分

### Introduction, 基本规则

For a scalar function $f\colon \mathbb{R}^3→\mathbb{R}$, the **partial derivatives** are
$$
\begin{cases}
\partial_x f = \dfrac{\partial f}{\partial x} = \lim\limits_{\Delta x \to 0} \dfrac{f(x + \Delta x, y, z) - f(x, y, z)}{\Delta x} \\
\partial_y f = \dfrac{\partial f}{\partial y} = \lim\limits_{\Delta y \to 0} \dfrac{f(x, y + \Delta y, z) - f(x, y, z)}{\Delta y} \\
\partial_z f = \dfrac{\partial f}{\partial z} = \lim\limits_{\Delta z \to 0} \dfrac{f(x, y, z + \Delta z) - f(x, y, z)}{\Delta z}
\end{cases}
$$
The **total derivative**, capturing how $f$ changes with all variables, is
$$
\dif f = \partial_x f \dif x + \partial_y f \dif y + \partial_z f \dif z
$$

For a vector function $\v{F}\colon \mathbb{R}^3→\mathbb{R}^3$, the **partial derivatives** are
$$
\partial_x \v{F} = \begin{pmatrix} \partial_x F_x \\ \partial_x F_y \\ \partial_x F_z \end{pmatrix}, \quad \partial_y \v{F} = \begin{pmatrix} \partial_y F_x \\ \partial_y F_y \\ \partial_y F_z \end{pmatrix}, \quad \partial_z \v{F} = \begin{pmatrix} \partial_z F_x \\ \partial_z F_y \\ \partial_z F_z \end{pmatrix}
$$
The **total derivative** is
$$
\dif \v{F} = \partial_x \v{F} \dif x + \partial_y \v{F} \dif y + \partial_z \v{F} \dif z
$$

We have **Jacobian matrix**, which is a matrix containing all partial derivatives of a vector function. For $\v{F} = \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}$, the Jacobian matrix is $J_{\v{F}} = \begin{pmatrix} \partial_x F_x & \partial_y F_x & \partial_z F_x \\ \partial_x F_y & \partial_y F_y & \partial_z F_y \\ \partial_x F_z & \partial_y F_z & \partial_z F_z \end{pmatrix}$. The **determinant** of the Jacobian matrix is called the **Jacobian**.

Similarly, we have **Hessian matrix**, which is a matrix containing all second partial derivatives of a scalar function. For $f(x, y, z)$, the Hessian matrix is $H_f = \begin{pmatrix} \partial_{xx} f & \partial_{xy} f & \partial_{xz} f \\ \partial_{yx} f & \partial_{yy} f & \partial_{yz} f \\ \partial_{zx} f & \partial_{zy} f & \partial_{zz} f \end{pmatrix}$.

> [!note] Derivatives converting between Cartesian and curvilinear coordinates
> In Cartesian coordinates, we can split a curve, a surface or a volume into its **elements** $\dif \v{l}$, $\dif \v{a}$, $\dif \tau$ respectively, and represent them with $\dif x$, $\dif y$, $\dif z$. If we convert them into curvilinear coordinates, we will **still use the notations $\dif \v{l}$, $\dif \v{a}$, $\dif \tau$**, but **their values will change** since the unit vectors are different.
>
> For example, on a sphere surface in spherical coordinates, we have $\dif \v{a} = r^2\sin\theta\dif \theta\dif \phi\vu{r}$, where $\vu{r}$ is the unit vector pointing outward from the sphere. If we convert it into Cartesian coordinates, we will have $\dif \v{a} = r^2\sin\theta\dif \theta\dif \phi\vu{x}$, where $\vu{x}$ is the unit vector pointing outward from the sphere.

### Special Derivatives, 特殊导数

#### Gradient, 梯度

Given a **scalar function** (or call it a **scalar field** in the 3D space) $f(x, y, z)$, its **gradient** is defined as
$$
\mathop{\mathrm{grad}} f(x, y, z) = \left. \begin{pmatrix} \dfrac{\partial f}{\partial x} \\ \dfrac{\partial f}{\partial y} \\ \dfrac{\partial f}{\partial z} \end{pmatrix} \right|_{(x, y, z)} = \left. \begin{pmatrix}
\partial_{x} f \\ \partial_{y} f \\ \partial_{z} f
\end{pmatrix} \right|_{(x, y, z)} = \nabla f(x, y, z) 
$$
here we defined the **Nabla operator $\nabla$** as
$$
\nabla = \begin{pmatrix} \partial_x \\ \partial_y \\ \partial_z \end{pmatrix} = \dfrac{\partial}{\partial x} \vu{x} + \dfrac{\partial}{\partial y}\vu{y} + \dfrac{\partial}{\partial z}\vu{z}
$$

For functions in _spherical coordinates, 球坐标系_, we have the gradient as
$$
\nabla f = \dfrac{\partial f}{\partial r}\vu{r} + \dfrac{1}{r}\dfrac{\partial f}{\partial \theta}\vu{\theta} + \dfrac{1}{r\sin\theta}\dfrac{\partial f}{\partial \phi}\vu{\phi}
$$
and in _cylindrical coordinates, 柱坐标系_,
$$
\nabla f = \dfrac{\partial f}{\partial s}\vu{s} + \dfrac{1}{s}\dfrac{\partial f}{\partial \phi}\vu{\phi} + \dfrac{\partial f}{\partial z}\vu{z}
$$

#### Divergence, 散度

Given a **vector function** (or call it a **vector field** in the 3D space) $\v{F}(x, y, z) = \begin{pmatrix} F_x(x, y, z) \\ F_y(x, y, z) \\ F_z(x, y, z) \end{pmatrix}$, its **divergence** is defined as
$$
\begin{align}
\mathop{\mathrm{div}} \v{F}(x, y, z) 
&= \nabla \cdot \v{F}(x, y, z) 
= \begin{pmatrix} \partial_x \\ \partial_y \\ \partial_z \end{pmatrix} \cdot \left. \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix} \right|_{(x, y, z)} \\
&= \partial_x F_x(x, y, z)  + \partial_y F_y(x, y, z)  + \partial_z F_z(x, y, z) 
\end{align}
$$

Specifically, if $\v{F}(x, y, z) = \v{r}$, then $\nabla \cdot \v{r} = \nabla \cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \partial_x x + \partial_y y + \partial_z z = 3$.

> [!example]+ Calculate the divergence of $\v{F}(\v{r}) = {\vu{r}}/{r^2}$
> Noticing $\vu{r}$ is difficult to differentiate directly since the square root is involved, we can use the **spherical coordinate** to simplify the calculation. We have
> $$
> \v{F}(\v{r}) = \dfrac{\vu{r}}{r^2} = \dfrac{\v{r}}{r^3}
> $$
> and then we can calculate the divergence as
> $$
> \begin{align}
> \nabla \cdot \v{F}(\v{r}) = \nabla \cdot \left( \dfrac{\v{r}}{r^3} \right) &= \partial_{x} \left( \dfrac{x}{r^3} \right) + \partial_{y} \left( \dfrac{y}{r^3} \right) + \partial_{z} \left( \dfrac{z}{r^3} \right) \\
> &= \dfrac{1}{r^3} - 3x^2 \dfrac{1}{r^5} + \dfrac{1}{r^3} - 3y^2 \dfrac{1}{r^5} + \dfrac{1}{r^3} - 3z^2 \dfrac{1}{r^5}  \\
> &= \dfrac{3}{r^3} - \dfrac{3(x^2 + y^2 + z^2)}{r^5} = 0
> \end{align}
> $$
> So the divergence of $\v{F}(\v{r}) = \dfrac{{\vu{r}}}{r^2}$ is 0.

For functions in _spherical coordinates_, we have the divergence as
$$
\nabla \cdot \v{F} = \dfrac{1}{r^2}\dfrac{\partial}{\partial r}(r^2 F_r) + \dfrac{1}{r\sin\theta}\dfrac{\partial}{\partial \theta}(\sin\theta F_{\theta}) + \dfrac{1}{r\sin\theta}\dfrac{\partial F_{\phi}}{\partial \phi}
$$
and in _cylindrical coordinates_
$$
\nabla \cdot \v{F} = \dfrac{1}{s}\dfrac{\partial}{\partial s}(sF_s) + \dfrac{1}{s}\dfrac{\partial F_{\phi}}{\partial \phi} + \dfrac{\partial F_z}{\partial z}
$$

#### Curl, 旋度

Given a **vector function** (or call it a **vector field** in the 3D space) $\v{F}(x, y, z) = \begin{pmatrix} F_x(x, y, z) \\ F_y(x, y, z) \\ F_z(x, y, z) \end{pmatrix}$, its **curl** is defined as
$$
\mathop{\mathrm{curl}} \v{F}(x, y, z) 
= \nabla \times \v{F}(x, y, z) 
= \begin{pmatrix} \partial_x \\ \partial_y \\ \partial_z \end{pmatrix} \times \left. \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix} \right|_{(x, y, z)} = \begin{pmatrix} \partial_y F_z - \partial_z F_y \\ \partial_z F_x - \partial_x F_z \\ \partial_x F_y - \partial_y F_x \end{pmatrix}
$$

> [!example]+ Calculate the curl of $\v{F}(\v{r}) = -x \v{y} + y \v{x}$
> We can calculate the curl as
> $$
> \nabla \times \v{F}(\v{r}) = \nabla \times \begin{pmatrix} y \\ -x \\ 0 \end{pmatrix} = \begin{pmatrix} 0 - 0 \\ 0 - 0 \\ \partial_x y - \partial_y x \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix} = 2\vu{z}
> $$
> In fact, the given field is **circulation** in the $xy$ plane, and that's why the curl is in the $z$ direction.

For functions in _spherical coordinates_, we have the curl as
$$
\begin{align}
\nabla \times \v{F} = \dfrac{1}{r\sin\theta}\left( \dfrac{\partial}{\partial \theta}(\sin\theta F_{\phi}) - \dfrac{\partial F_{\theta}}{\partial \phi} \right)\vu{r} + \dfrac{1}{r}\left( \dfrac{1}{\sin\theta}\dfrac{\partial F_r}{\partial \phi} - \dfrac{\partial}{\partial r}(rF_{\phi}) \right)\vu{\theta} \\
+ \dfrac{1}{r}\left( \dfrac{\partial}{\partial r}(rF_{\theta}) - \dfrac{\partial F_r}{\partial \theta} \right)\vu{\phi}
\end{align}
$$
and in _cylindrical coordinates_
$$
\nabla \times \v{F} = \left( \dfrac{1}{s} \dfrac{\partial F_z}{\partial \phi} - \dfrac{\partial F_{\phi}}{\partial z} \right)\vu{s} + \left( \dfrac{\partial F_s}{\partial z} - \dfrac{\partial F_z}{\partial s} \right)\vu{\phi} + \dfrac{1}{s} \left( \dfrac{\partial}{\partial s}(sF_{\phi}) - \dfrac{\partial F_s}{\partial \phi} \right)\vu{z}
$$

#### Product Rules of Special Derivatives, 乘积法则

Given two scalar functions $f(x, y, z)$ and $g(x, y, z)$, and two vector functions $\v{F}(x, y, z)$ and $\v{G}(x, y, z)$, we have the following product rules.

+ If at least one of the two functions is a scalar, then we can say the product is a **scalar product**. Rules for scalar products are similar to the scalar derivatives.
	+ *Gradient of a scalar product*: 
	$$\nabla (fg) = f \nabla g + g \nabla f$$
	+ *Divergence of a scalar product*: 
	$$\nabla \cdot (f\v{F}) = f \nabla \cdot \v{F} + \v{F} \cdot \nabla f$$
	+ *Curl of a scalar product*: 
	$$\nabla \times (f\v{F}) = f \nabla \times \v{F} - \v{F} \times \nabla f$$
+ If both functions are vectors, then we can say the product is a **vector product**. Rules for vector products are more complicated. 
	+ ***Gradient of vectors' dot product***: 
	$$\nabla (\v{F} \cdot \v{G}) = \v{F} \times (\nabla \times \v{B}) + \v{G} \times (\nabla \times \v{F}) + (\v{F} \cdot \nabla) \v{G} + (\v{G} \cdot \nabla) \v{F}$$
	+ ***Divergence of vectors' cross product***: 
	$$\nabla \cdot (\v{F} \times \v{G}) = \v{G} \cdot (\nabla \times \v{F}) - \v{F} \cdot (\nabla \times \v{G})$$
	It's just like the behavior of the [[#^f0b7e4|vector triple product]].
	
	+ ***Curl of vectors' cross product***: 
	$$\nabla \times (\v{F} \times \v{G}) = (\v{G} \cdot \nabla) \v{F} - (\v{F} \cdot \nabla) \v{G} + \v{F}(\nabla \cdot \v{G}) - \v{G}(\nabla \cdot \v{F})$$

### Second Derivatives, 二阶导数

Given a scalar function $f(x, y, z)$,  or a vector function $\v{F}(x, y, z)$, we have the following second derivatives.

#### Laplacian

**Laplacian** of a _scalar_ function $f(x, y, z)$ is defined as
$$
\nabla^2 f(x, y, z) = \nabla \cdot \nabla f(x, y, z) = \nabla \cdot \begin{pmatrix} \partial_x f \\ \partial_y f \\ \partial_z f \end{pmatrix} = \partial_{xx} f + \partial_{yy} f + \partial_{zz} f
$$
and for a _vector_ function $\v{F}(x, y, z)$, its Laplacian is defined as
$$
\begin{align}
\nabla^2 \v{F}(x, y, z) &= (\nabla \cdot \nabla) \v{F}(x, y, z) \\
&= (\partial_{xx} + \partial_{yy} + \partial_{zz}) \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix} = \begin{pmatrix} \partial_{xx} F_x + \partial_{yy} F_x + \partial_{zz} F_x \\ \partial_{xx} F_y + \partial_{yy} F_y + \partial_{zz} F_y \\ \partial_{xx} F_z + \partial_{yy} F_z + \partial_{zz} F_z \end{pmatrix} \\
&= (\nabla^2 F_x) \vu{x} + (\nabla^2 F_y) \vu{y} + (\nabla^2 F_z) \vu{z}
\end{align}
$$
Put simply, we can just see the Laplacian operator $\nabla^2 = \partial_{xx} + \partial_{yy} + \partial_{zz}$ as a **special scalar**, which can be applied to both scalar and vector functions.

For scalar functions in _spherical coordinates_, we have the Laplacian as
$$
\nabla^2 f = \dfrac{1}{r^2}\dfrac{\partial}{\partial r}\left( r^2 \dfrac{\partial f}{\partial r} \right) + \dfrac{1}{r^2\sin\theta}\dfrac{\partial}{\partial \theta}\left( \sin\theta \dfrac{\partial f}{\partial \theta} \right) + \dfrac{1}{r^2\sin^2\theta}\dfrac{\partial^2 f}{\partial \phi^2}
$$
and in _cylindrical coordinates_
$$
\nabla^2 f = \dfrac{1}{s}\dfrac{\partial}{\partial s}\left( s \dfrac{\partial f}{\partial s} \right) + \dfrac{1}{s^2}\dfrac{\partial^2 f}{\partial \phi^2} + \dfrac{\partial^2 f}{\partial z^2}
$$

#### Curl of Gradient

Curl of the gradient of a scalar function $f(x, y, z)$ is always 0, which is
$$
\nabla \times \left(\nabla f(x, y, z)\right) \equiv 0
$$

#### Divergence of Curl

Divergence of the curl of a vector function $\v{F}(x, y, z)$ is always 0, which is
$$
\nabla \cdot \left(\nabla \times \v{F}(x, y, z)\right) \equiv 0
$$

#### Curl of Curl

Curl of the curl of a vector function $\v{F}(x, y, z)$ is given by
$$
\nabla \times \left(\nabla \times \v{F}(x, y, z)\right) = \nabla \left(\nabla \cdot \v{F}(x, y, z)\right) - \nabla^2 \v{F}(x, y, z)
$$

## Vector Integrals, 矢量积分

Integral of a vector should be based on a derivative.

### Line Integral, 线积分

Given a vector function $\v{F}(x, y, z)$, and a curve $C$ with parameter $t$, we have the **line integral** of $\v{F}$ along $C$ as
$$
\int_C \v{F} \cdot \dif \v{l} = \int_C \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix} \cdot \begin{pmatrix}  \dif x \\ \dif y \\ \dif z \end{pmatrix} = \int_C F_x \dif x + F_y \dif y + F_z \dif z
$$

Here, $\dif \v{l}$ is the **line element** along the curve $C$, which can be represented in _Cartesian coordinates_ as 
$$
\dif \v{l} = \dif x \, \vu{x} + \dif y \, \vu{y} + \dif z \, \vu{z}
$$
and in _spherical coordinates_ as
$$
\dif \v{l} = \dif r \, \vu{r} + r \dif \theta \, \vu{\theta} + r\sin\theta \dif \phi \, \vu{\phi}
$$
in _cylindrical coordinates_ as
$$
\dif \v{l} = \dif s \, \vu{s} + s \dif \phi \, \vu{\phi} + \dif z \, \vu{z}
$$


#### Fundamental Theorem for Gradients, 基本定理

Specifically, if $\v{F} = \nabla f$, then the line integral can be written as
$$
\int_C \nabla f \cdot \dif \v{r} = f(\v{r}_2) - f(\v{r}_1) = \int_{\v{r}_1}^{\v{r}_2} \nabla f \cdot \dif \v{r}
$$
where $\v{r}_1$ and $\v{r}_2$ are the initial and final points of the curve $C$, and the value of the integral is **independent of the path**.

### Surface Integral, 面积分

Given a vector function $\v{F}(x, y, z)$, and a surface $S$ with parameter $u, v$, we have the **surface integral** of $\v{F}$ over $S$ as
$$
\int_S \v{F} \cdot \dif \v{a} = \int_S \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix} \cdot \begin{pmatrix}  \dif a_x \\ \dif a_y \\ \dif a_z \end{pmatrix} = \int_S F_x \dif a_x + F_y \dif a_y + F_z \dif a_z
$$

Here, $\dif \v{a}$ is the **surface element** on the surface $S$, which can also be represented in _spherical coordinates_: for integrating **over the surface of a sphere** we have
$$
\dif \v{a} = r^2 \sin\theta \dif \theta \dif \phi \, \vu{r}
$$
and for integrating **in $x-y$ plane**, we have
$$
\dif \v{a} = r \dif r \dif \phi \,\vu{\theta}
$$

#### Stokes' Theorem, 斯托克斯定理

Given a vector function $\v{F}(x, y, z)$ on a surface $S$, we have the **Stokes' theorem** as
$$
\int_S \nabla \times \v{F} \cdot \dif \v{a} = \oint_{\partial S} \v{F} \cdot \dif \v{r}
$$
where $\partial S$ is the boundary of the surface $S$. The direction how line element $\dif \v{r}$ is taken along the boundary is determined by the right-hand rule with the direction of the normal $\vu{n}$ of $\dif  \v{S}$.

#### Generalized Leibniz Integral Rule, 广义莱布尼兹积分法则

If an open surface $S(t)$ is varying with $t$, we have the **generalized Leibniz integral rule** as
$$
\dfrac{\dif}{\dif t} \left( \dint_{S(t)} \v{F} \cdot \dif \v{a} \right)
= \int_{S(t)} \left( \dfrac{\partial \v{F}}{\partial t} + (\nabla \cdot \v{F})\v{v} \right)  \cdot \dif \v{a} 
- \oint_{\partial S(t)} (\v{v} \times \v{F}) \cdot \dif \v{l}
$$
where $\partial S(t)$ is the **boundary of the surface $S(t)$**, and $\v{v}$ is the **velocity of points on the boundary $\partial S(t)$**.

### Volume Integral, 体积分

Given a scalar function $f(x, y, z)$, and a volume $V$, we have the **volume integral** of $f$ over $V$ as
$$
\int_V f \dif \tau = \int_V f(x, y, z) \dif \tau = \int_V f(x, y, z) \dif x \dif y \dif z
$$

Here, $\dif \tau$ is the **volume element** in the volume $V$, which can be represented in _spherical coordinates_ as
$$
\dif \tau = r^2 \sin\theta \dif r \dif \theta \dif \phi
$$
and in _cylindrical coordinates_ as
$$
\dif \tau = s \dif s \dif \phi \dif z
$$

#### Gauss' Theorem, 高斯定理

Specifically, if $f = \nabla \cdot \v{F}$, then the volume integral can be written as
$$
\int_V \nabla \cdot \v{F} \dif \tau = \oint_{\partial V} \v{F} \cdot \dif \v{a}
$$
where $\partial V$ is the surface of the volume $V$, and $\dif \v{a}$ is the surface element upon it with outward normal $\vu{n}$.

#### Curl version of the Divergence Theorem, 旋度版本的散度定理

For any vector field $\v{F}$, we have
$$
\int_{V} \nabla \times \v{F} \dif \tau = - \oint_{\partial V} \v{F} \times \dif \v{a}
$$
where $\partial V$ is the surface of the volume $V$.

This can be proven by analyzing
$$
\begin{align}
\int_{V} \nabla \cdot \left( \v{F} \times \v{c} \right) \dif \tau &= \int_{V} \v{c} \cdot (\nabla \times \v{F}) \dif \tau - \int_{V} \v{F} \cdot \underbrace{ (\nabla \times \v{c}) }_{ \v{0} } \dif \tau 
= \v{c} \cdot \int_{V} (\nabla \times \v{F}) \dif \tau \\
&\stackrel{\scriptstyle\text{directly apply}\atop\scriptstyle\text{Gauss' Theorem}}{=\!=\!=\!=\!=\!=\!=\!=\!=} \displaystyle\oint_{\partial V} \left( \v{F} \times \v{c} \right) \cdot \dif \v{a} = \left( -\oint_{\partial V} \v{F} \times \dif \v{a} \right) \cdot \v{c} 
\end{align}
$$
where $\v{c}$ is an **arbitrary constant vector**. Since the above equation holds for any $\v{c}$, we can conclude to the identity above.