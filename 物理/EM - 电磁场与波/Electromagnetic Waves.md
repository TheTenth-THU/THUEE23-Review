## Solving the Wave Equation, 求解波动方程

### Wave Equation, 波动方程

The wave equation describes **how waves propagate** through space and time. In its most general form, the wave equation is given by
$$
\nabla^2 \psi - \dfrac{1}{v^2} \dfrac{\partial^2 \psi}{\partial t^2} = f(x, t)
$$
where $\v{v}$ is the **wave speed** and $f(x, t)$ is a source term. 

If we set $f(x, t) = 0$, we have the **homogeneous wave equation, 齐次波动方程** as
$$
\square^2 \psi = \nabla^2 \psi - \dfrac{1}{v^2} \dfrac{\partial^2 \psi}{\partial t^2} = 0
$$
where $\square^2 := \nabla^2 - \dfrac{1}{v^2} \dfrac{\partial^2}{\partial t^2}$ is the **d'Alembert operator, 达朗贝尔算子**.

### Homogeneous Solution of Wave Equation, 波动方程的齐次解

#### 1-D Wave Equation and its Solution, 一维波动方程及其解

The solution to a 1-D wave equation $\partial_{xx} f = \dfrac{1}{c^2} \partial_{tt}f$ is in the form of
$$
f(x, t) = g(x - ct) + h(x + ct)
$$

A commonly-used form of $g$ is
$$
g(u) = A_{0} \cos(k u + \phi_{0})
$$
**Inserting $u = x - ct$** yields
$$
f(x, t) = A_{0} \cos(k (x - ct) + \phi_{0}) = A_{0} \cos(k x - kc t + \phi_{0})
$$
where:
+ $A_{0}$ is the amplitude, 
+ $k = \dfrac{2\pi}{\lambda}$ is the **wave number** with unit $\rmu{rad \cdot m^{-1}}$,
+ $\omega = kc$ is the **angular frequency** with unit $\rmu{rad \cdot s^{-1}}$, and
+ $\phi_{0}$ is the phase constant. 

> [!danger] This solution is practically unrealistic
> It is critical to emphasize that the solution described above, while theoretically elegant, is **practically unrealistic**. This dichotomy arises because the cosine function inherently **extends infinitely in both space and time**—a mathematical idealization that cannot physically manifest. 
> 
> Nevertheless, its utility lies in its role as a **foundational basis for Fourier analysis**, wherein nearly any function can be synthesized through superposition of such harmonic components.

Operations involving **cosine functions** can be significantly **simplified** by employing **complex exponential notation, 复指数记号**, i.e.
$$
f(x, t) = \mathfrak{Re}\{ A_{0} \e^{\I(k x - \omega t + \phi_{0})} \} = \mathfrak{Re}\{ \underbrace{ A_{0} \e^{\I \phi_{0}} }_{ \tilde{A}_{0} } \e^{\I(k x - \omega t)} \}
$$

#### 3-D Wave Equation and its Solution, 三维波动方程及其解

The **harmonic solution** to a 3-D wave equation $\nabla^2 f = \dfrac{1}{c^2} \partial_{tt}f$ is in the form of
$$
f(\v{r}, t) = A_{0} \e^{\I(\v{k} \cdot \v{r} - \omega t + \phi_{0})} = \tilde{A}_{0} \e^{\I(\v{k} \cdot \v{r} - \omega t)}
$$
where:
+ $\v{k}$ is the **wave vector** with unit $\rmu{rad \cdot m^{-1}}$, and 
+ $\tilde{A}_{0} = A_{0} \e^{\I\phi_{0}}$ is the **complex amplitude, 复振幅**, subsuming the amplitude and phase constant.

At the same time $t$, if we consider the **phase front, 相位面**, defined by a **certian value of $\v{k}\cdot \v{r} -\omega t$**, we have $\v{k}\cdot \v{r}$ as a **constant**, which means $\v{r}$ is **on the same plane perpendicular to $\v{k}$**. This is why the solution above is called a **plane wave, 平面波**.

##### Separation of Variables, 变量分离

Plane waves are sometimes denoted as
$$
f(\v{r}, t) = \tilde{A}_{0} \e^{\I\v{k}\cdot\v{r}} \e^{- \I \omega t} = R(\v{r}) T(t)
$$
where **the spatial and temporal dependencies are completely separated** in a product form. Take this form into the wave equation, we have
$$
\left( \nabla^2 - \dfrac{1}{c^2}\partial_{tt} \right) R(\v{r}) T(t) = 0
\quad\Longrightarrow\quad
\left( \nabla^2 R(\v{r}) \right) T(t) = \dfrac{1}{c^2} R(\v{r}) \partial_{tt} T(t)
$$
Dividing both sides by $R(\v{r}) T(t)$, we have
$$
\dfrac{\nabla^2 R(\v{r})}{R(\v{r})} = \dfrac{1}{c^2} \dfrac{\partial_{tt} T(t)}{T(t)} =: -\lambda^2
$$
and this **holds** for any other function $f(\v{r},t)$ as long as it can be expressed in the form of $R(\v{r}) T(t)$.

##### Helmholtz Equation, 亥姆霍兹方程

For a **single-frequency wave**
$$
f(\v{r}, t) = R(\v{r})T(t) = \tilde{A}_{0}(\v{r}) \e^{-\I \omega t}
$$
where $\tilde{A}_{0}(\v{r})$ is a **spatially varying amplitude** and $\omega$ is a **constant frequency**, we have
$$
\dfrac{1}{c^2} \dfrac{\partial_{tt} T(t)}{T(t)} = \dfrac{1}{c^2} \dfrac{-\omega^2 \e^{-\I \omega t}}{\e^{-\I \omega t}} = -\dfrac{\omega^2}{c^2} = -k^2
$$
where $k = \dfrac{\omega}{c}$ is the **wave number**. Therefore, we have
$$
\dfrac{\nabla^2 R(\v{r})}{R(\v{r})} = -k^2
$$

> [!theorem] Helmholtz Equation
> For a **single-frequency wave**, the **Helmholtz equation** is given by
> $$ \nabla^2 R(\v{r}) + k^2 R(\v{r}) = 0 $$
> where $k = \dfrac{\omega}{c}$ is the **wave number**.

## Homogeneous Solution of the Maxwell's Equations, 麦克斯韦方程组的齐次解

### Solving Maxwell's Equations as a Wave Equation, 以波动方程的形式求解麦克斯韦方程

The wave equation can be derived from Maxwell's equations, which describe the behavior of electric and magnetic fields. From [[Maxwell's equations]], in a vacuum with no free charges or currents, we have the **homogeneous solution, 齐次解**, of the Maxwell's equations, which satisfies
$$
\begin{align}
\nabla \times \v{E} = - \dfrac{\partial \v{B}}{\partial t} 
&\Longrightarrow \nabla \times \left( \nabla \times \v{E} \right)  = - \dfrac{\partial}{\partial t} \left( \nabla \times\v{B} \right)  \\
&\Longrightarrow \nabla \left( \nabla\cdot \v{E} \right) - \nabla^2 \v{E} = - \dfrac{\partial}{\partial t} \left( \mu_{0} \varepsilon_{0} \dfrac{\partial}{\partial t} \v{E} \right)  \\
&\Longrightarrow \nabla^2 \v{E} - \mu_{0} \varepsilon_{0} \dfrac{\partial^2}{\partial t^2} \v{E} = 0
\end{align}
$$
and **is in the form of a [[#Wave Equation, 波动方程]]**. Therefore, Maxwell predicted the existence of **electromagnetic waves** that propagate at the speed of $c = \dfrac{1}{\sqrt{ \mu_{0}\varepsilon_{0} }}$ in a vacuum.

In the same way, we can derive the wave equation for the magnetic field $\v{B}$, thus
$$
\begin{cases}
\nabla^2 \v{E} - \dfrac{1}{c^2} \dfrac{\partial^2}{\partial t^2} \v{E} = 0 \\
\nabla^2 \v{B} - \dfrac{1}{c^2} \dfrac{\partial^2}{\partial t^2} \v{B} = 0
\end{cases}
$$
therefore, we have the **homogeneous solution** for the electric and magnetic fields in a vacuum as
$$
\begin{cases}
\v{E}(\v{r}, t) = \cpq{\v{E}}_{0} \e^{\I(\v{k}\cdot\v{r} - \omega t)} \\
\v{B}(\v{r}, t) = \cpq{\v{B}}_{0} \e^{\I(\v{k}\cdot\v{r} - \omega t)}
\end{cases}
$$
where $\cpq{\v{E}}_{0}$ and $\cpq{\v{B}}_{0}$ are the **complex amplitudes** of the electric and magnetic fields, respectively.

Substituting the above solution into the Maxwell-Faraday equation $\nabla \times \v{E} = -\partial_{t}\v{B}$, we have
$$
\I \v{k} \times \v{E} = \I \omega \v{B}
$$
and therefore
$$
\v{B}(\v{r}, t) = \dfrac{\v{k} }{\omega} \times \v{E}(\v{r}, t)
$$

## Inhomogeneous Solution of the Maxwell's Equations, 麦克斯韦方程组的非齐次解

We only care about two kinds of the inhomogeneous solution.

