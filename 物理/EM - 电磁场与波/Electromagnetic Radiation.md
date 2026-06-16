## Fundamental Principles about Radiation, 辐射的基本原理

We have a key physical insight that **radiated fields, 辐射场**, must propagate **outward from the source**, with no incoming waves from infinity. Therefore, we seek only the particular solution to the inhomogeneous wave equation — one that corresponds purely to **outgoing radiation fields**.

### Pattern of Radiated Fields, 辐射场的模式

Assume we have a point charge initially at rest. It would produce a **static electric field**, and would not radiate. 

At $t=0$, it begins **accelerating** at constant rate $\ddot{\v{r}}' = a\vu{x}$ for a short duration of time $\Delta t$; after that, it **continues to move** with constant velocity $\dot{\v{r}}' = a \Delta t\ \vu{x}$. 

```tikz
\usepackage{amsmath}
\begin{document}

\large
\begin{tikzpicture}
\draw[thick, dashed, fill=blue!30!white, opacity=0.1] (0,0) circle (3);
\draw[thick, dashed, fill=blue!30!white, opacity=0.1] (0.3,0) circle (2.5);
\draw[thick] (0,0) circle (0.2) -- (-1,0.5) node[above] {$t=0$}
(0.3,0) circle (0.2) -- (0.5,0.5) node[above] {$t=\Delta t$}
(1,0) circle (0.2) -- (2.5,0.5) node[above] {$t=\Delta t+t_{0}$};
\draw[thick, dashed] (0,0) -- (0,-3) node[left, midway] {$c(\Delta t+t_{0})$}; 
\draw[thick, dashed] (0.3,0) -- (0.3,-2.5) node[right, midway] {$ct_{0}$}; 
\draw[very thick, blue!50!white, -latex] (1,0) -- (1,-2.4) -- (0,-3) -- (0,-4) node[right] {$\vec{\boldsymbol{E}}$};
\end{tikzpicture}
\end{document}
```

From the **perspective of information propagation**, 
+ The space **outside the outer circle** and the space **inside the inner circle** believe the charge is producing a **static electric field**, while
+ Only the space **between the two circles** believes the charge is accelerating and producing a **time-varying electric field**.

Such a "distortion" of the electric field is the **radiated field, 辐射场**, which propagates outward at the speed of light $c$.

We can calculate the **radiated electric field**.
+ At a point $\v{r}$ ($\v{r} \perp \ddot{\v{r}}'$) at time $t$, we expect $E_{\parallel}(\v{r}, t) = \dfrac{q}{4\pi \varepsilon_0} \dfrac{1}{r^{2}}$ does not change, and
$$
E_{\perp}(\v{r}, t) = \dfrac{vt_{0}}{c\Delta t} E_{\parallel}(\v{r}, t) = \dfrac{q}{4\pi \varepsilon_0} \dfrac{ar}{c^{2}} \dfrac{1}{r^{2}} = \dfrac{qa}{4\pi \varepsilon_0 c^{2}} \dfrac{1}{r}
$$
where we estimate $t_{0} = \dfrac{r}{c}$.
+ In the **trajectory direction,** apparently $E_{\perp} = 0$.

Therefore, we can expect that 
$$
E_{\perp}(\v{r}, t) = \dfrac{qa}{4\pi \varepsilon_0 c^{2}} \dfrac{1}{r} \sin \left\langle \v{r}, \ddot{\v{r}}' \right\rangle 
$$
where $\left\langle \v{r}, \ddot{\v{r}}' \right\rangle$ is the angle between $\v{r}$ and the acceleration $\ddot{\v{r}}'$.

### Lorenz Gauge, 洛伦兹规范

From the Maxwell's equations, we can derive that
$$
\nabla \times \v{E} = - \partial_{t} \v{B} = - \partial_{t} (\nabla \times \v{A}) 
\quad\Longrightarrow\quad
\nabla \times (\v{E} + \partial_{t} \v{A}) = \v{0}
$$
Because the curl of **any gradient of a scalar field** is zero, we can let $\phi = \v{E} + \partial_{t} \v{A}$, and thus we have
$$
\begin{cases}
\v{B} = \nabla \times \v{A} \\
\v{E} = - \nabla \phi - \partial_{t} \v{A}
\end{cases}
$$

However, the solution of $\phi$ and $\v{A}$ is not unique, since we can **add any $\nabla f$ to $\v{A}$** and **subtract the same $\partial_{t} f$ from $\phi$** without changing the electric and magnetic fields. Any choice of $(\phi, \v{A})$ is called a **gauge, 规范**.

The rest of the Maxwell's equations can be expressed as
$$
\begin{align}
&\nabla \cdot \v{E} = \dfrac{\rho}{\varepsilon_0} \\
&\Longrightarrow \quad
\nabla \cdot (\nabla \phi + \partial_{t} \v{A}) = \nabla^{2} \phi + \partial_{t} (\nabla \cdot \v{A}) =  -\dfrac{\rho}{\varepsilon_0} \\
&\nabla \times \v{B} = \mu_0 \v{J} + \mu_0 \varepsilon_0 \partial_{t} \v{E} \\
&\Longrightarrow \quad
\nabla (\nabla \cdot \v{A}) - \nabla^{2} \v{A} = \mu_0 \v{J} + \mu_0 \varepsilon_0 \partial_{t} (-\nabla \phi - \partial_{t} \v{A}) \\
&\Longrightarrow \quad
\nabla (\nabla \cdot \v{A}) - \nabla^{2} \v{A} = \mu_0 \v{J} - \dfrac{1}{c^{2}} \partial_{t} \nabla \phi - \dfrac{1}{c^{2}} \partial_{tt} \v{A} \\
&\Longrightarrow \quad
\nabla^{2} \v{A} - \dfrac{1}{c^{2}} \partial_{tt} \v{A} = \nabla\left( \nabla \cdot \v{A} + \dfrac{1}{c^{2}} \partial_{t} \phi \right) - \mu_0 \v{J}
\end{align}
$$

**It is possible to choose a gauge such that $$\nabla \cdot \v{A} + \dfrac{1}{c^{2}} \partial_{t} \phi = 0$$**which is called the **Lorenz gauge condition, 洛伦兹规范条件**.

### Retarded Potentials, 推迟势

Under [[#Lorenz Gauge, 洛伦兹规范]], the inhomogeneous wave equations 
$$\begin{cases}\left( \nabla^{2} + \dfrac{1}{c^{2}} \partial_{tt} \right) \phi = -\dfrac{\rho}{\varepsilon_0}, \\\left( \nabla^{2} + \dfrac{1}{c^{2}} \partial_{tt} \right) \v{A} = -\mu_0 \v{J}\end{cases}$$
govern the behavior. **Green functions, 格林函数**, are used to solve these equations.

Consider the response to a **point source** at $(\v{r}',\mathscr{t}')$, satisfying
$$
\left( \nabla^{2} + \dfrac{1}{c^{2}} \partial_{tt} \right) G(\v{r}, \mathscr{t}; \v{r}', \mathscr{t}') = -\delta(\v{r} - \v{r}') \delta(\mathscr{t} - \mathscr{t}')
$$
Using Fourier transforms, we can express the solution as
$$
G(\v{r}, \mathscr{t}; \v{r}', \mathscr{t}') = \dfrac{1}{4\pi} \dfrac{\delta\left( \mathscr{t} - \mathscr{t}' - \dfrac{\sr}{c} \right)}{\sr} 
$$
We can then use this Green function to construct the solution of the potentials.

> [!theorem] Retarded Potentials
> Take the definite propagation speed of the electromagnetic field into account, the **retarded electric potential $\phi$** and the **magnetic vector potential $\v{A}$** are defined as
> $$
> \begin{align}
> &\phi(\v{r}, t) = \dfrac{1}{4\pi \varepsilon_0} \int \dfrac{\rho(\v{r}', t - \dfrac{\sr}{c})}{\sr} \dif V' \\
> &\v{A}(\v{r}, t) = \dfrac{\mu_0}{4\pi} \int \dfrac{\v{J}(\v{r}', t - \dfrac{\sr}{c})}{\sr} \dif V'
> \end{align}
> $$
> where $t_{r} = t - \dfrac{\sr}{c}$ is the **retarded time** at which the source was at $\v{r}'$ when the field is observed at $\v{r}$ at time $t$.


## Electric dipole radiation, 电偶极辐射

Consider an **electric dipole** located at the origin with its dipole moment aligned along the $\vu{z}$ direction, of which the two charges **oscillate harmonically, 简谐振动**, with angular, causing the **dipole moment $\v{p}$** to vary sinusoidally. These charge oscillations produce a **time-varying current** directed along $\vu{z}$. 

### Evaluating the Magnetic Vector Potential, 磁矢势的计算

The **magnetic vector potential** $\v{A}$ can be evaluated as a **retarded potential**, i.e.
$$
\v{A}(\v{r}, t) = \dfrac{\mu_0}{4\pi} \dint \dfrac{\v{J}\left( \v{r}', t - \dfrac{\sr}{c} \right) }{\sr} \dif V'
$$

Since the dipole is **small** compared to $\sr$, we have $r' \ll \sr$ and $r' \ll cT$, we can approximate $\v{A}$ as
$$
\begin{align}
\v{A}(\v{r}, t) &= \dfrac{\mu_0}{4\pi} \dint \dfrac{\v{J}\left( \v{r}', t - \dfrac{\sr}{c} \right) }{\sr} \dif V' \approx \dfrac{\mu_0}{4\pi r} \dint \v{J}\left( \v{r}', t - \dfrac{r}{c} \right) \dif V' \\
&= \dfrac{\mu_0}{4\pi r} \biggl( q\v{v}\left( t-\dfrac{r}{c} \right) + (-q) \left( -\v{v}\left( t-\dfrac{r}{c} \right) \right) \biggr) 
= \dfrac{\mu_0}{4\pi r} \cdot 2q \v{v}\left( t-\dfrac{r}{c} \right) \\
&= \dfrac{\mu_0}{4\pi r} \cdot 2q \dot{\v{z}} \left( t-\dfrac{r}{c} \right)
= \dfrac{\mu_0}{4\pi r} \cdot q \dot{\v{d}} \left( t-\dfrac{r}{c} \right)
= \dfrac{\mu_0}{4\pi r} \dot{\v{p}} \left( t-\dfrac{r}{c} \right) \\
&= \dfrac{\mu_0}{4\pi r} \dot{p} \left( t-\dfrac{r}{c} \right) \vu{z}
\end{align}
$$

### Evaluating the Magnetic Field, 磁场的计算

The **magnetic field** $\v{B}$ can be evaluated as
$$
\begin{align}
\v{B} = \nabla \times \v{A} 
&= \dfrac{1}{r\sin\theta} (\partial_{\theta} (\sin\theta A_{\phi}) - \partial_{\phi} A_{\theta}) \vu{r} + \dfrac{1}{r} \left( \dfrac{1}{\sin\theta} \partial_{\phi} A_{r} - \partial_{r} (rA_{\phi}) \right) \vu{\theta}  \\
&\hspace{1em}+ \dfrac{1}{r} (\partial_{r} (rA_{\theta}) - \partial_{\theta} A_{r}) \vu{\phi} \\
&= \dfrac{1}{r} \left( \partial_{r} \left( r \cdot \left( -\dfrac{\mu_0}{4\pi r} \dot{p} \left( t-\dfrac{r}{c} \right) \sin\theta \right) \right) - \partial_{\theta} \left( \dfrac{\mu_0}{4\pi r} \dot{p} \left( t-\dfrac{r}{c} \right) \cos \theta \right) \right) \vu{\phi} \\
&= -\dfrac{\mu_0}{4\pi r} \sin \theta \left( \partial_{r} \dot{p}\left( t-\dfrac{r}{c} \right) - \dfrac{1}{r} \dot{p}\left( t-\dfrac{r}{c} \right) \right) \vu{\phi} \\
&= \dfrac{\mu_0}{4\pi r} \sin \theta \left( \dfrac{1}{c} \ddot{p}\left( t-\dfrac{r}{c} \right) + \dfrac{1}{r} \dot{p}\left( t-\dfrac{r}{c} \right) \right) \vu{\phi} \\
&= \dfrac{\mu_{0}}{4\pi c} \sin \theta \left( \dfrac{1}{r} \ddot{p}\left( t-\dfrac{r}{c} \right) + \dfrac{c}{r^{2}} \dot{p}\left( t-\dfrac{r}{c} \right) \right) \vu{\phi}
\end{align}
$$

The term $\dfrac{\mu_{0}}{4\pi cr} \ddot{p}\left( t-\dfrac{r}{c} \right)  \sin \theta \,\vu{\phi}$ is the **radiation field**, which is the outgoing wave **propagating at the speed of light $c$** and varying **sinusoidally with $\theta$**.

If the dipole oscillates with angular frequency $\omega$, we have
$$
\begin{align}
&\cpq{p} \left( t - \dfrac{r}{c} \right) = \cpq{p}_{0} \e^{-\I\omega \left( t - r/c \right)} = \cpq{p}_{0} \e^{\I \left(kr - \omega t\right)}  \\
&\dot{\cpq{p}} \left( t-\dfrac{r}{c} \right) = -\I\omega \cpq{p}_{0} \e^{\I \left(kr - \omega t\right)} \\
&\ddot{\cpq{p}} \left( t-\dfrac{r}{c} \right) = -\omega^{2} \cpq{p}_{0} \e^{\I \left(kr - \omega t\right)}
\end{align}
$$
Therefore,
$$
\begin{align}
\cpq{\v{B}} (\v{r}, t) &= - \dfrac{\mu_{0} \omega \cpq{p}_{0}}{4\pi c} \left(\dfrac{\omega}{r} + \I \dfrac{c}{r^{2}} \right)  \sin \theta\, \e^{\I \left(kr - \omega t\right)} \vu{\phi} \\
&= - \dfrac{\cpq{p}_{0}k^{3}}{4\pi \varepsilon_{0} c} \left(\dfrac{1}{kr} + \I \dfrac{1}{(kr)^{2}} \right) \sin \theta\, \e^{\I \left(kr - \omega t\right)} \vu{\phi}
\end{align}
$$
where $k = \dfrac{\omega}{c}$ is the **wave number**.

### Evaluating the Electric Field, 电场的计算

Similarly, we can evaluate the **electric field** $\v{E}$ as
$$
\begin{align}
\cpq{E}_{r} &= \dfrac{2\cpq{p}_{0}k^{3}}{4\pi \varepsilon_{0}} \left( \dfrac{1}{(kr)^{3}} - \I \dfrac{1}{(kr)^{2}} \right) \cos \theta \, \e^{\I \left(kr - \omega t\right)} \\
\cpq{E}_{\theta} &= \dfrac{\cpq{p}_{0}k^{3}}{4\pi \varepsilon_{0} } \left( \dfrac{1}{(kr)^{3}} - \I \dfrac{1}{(kr)^{2}} - \dfrac{1}{kr} \right) \sin \theta\, \e^{\I \left(kr - \omega t\right)}
\end{align}
$$

When $kr < 1$, the **electric field** is dominated by the term associated with $\dfrac{1}{(kr)^{3}}$, which mirrors the [[Electrostatics#Electric Field of an Electric Dipole, 电偶极子的电场|behavior]] of the **static electric field** of a dipole. 

When $kr \gg 1$, the **electric field** is dominated by the term associated with $\dfrac{1}{kr}$, which is the **radiation field**. Only the **$\theta$-component** of the electric field contains the radiation field, and it also varies **sinusoidally with $\theta$**.

## Complex Poynting Vector, 复坡印亭矢量

The **Poynting vector** $\v{S}$ is defined as
$$
\v{S} = \dfrac{1}{\mu_0} \v{E} \times \v{B}
$$
When the field is monochromatic (i.e., of a single frequency), we use **complex notations**, as is done when dealing with the dipole radiation problem. In this case, the Poynting vector can be expressed as
$$
\begin{align}
\v{S} (\v{r}, t) &= \dfrac{1}{\mu_{0}} \left( \dfrac{1}{2} (\cpq{\v{E}}(\v{r}) \e^{-\I\omega t} + \cpq{\v{E}}^{*}(\v{r}) \e^{\I\omega t}) \right) \times \left( \dfrac{1}{2} (\cpq{\v{B}}(\v{r}) \e^{-\I\omega t} + \cpq{\v{B}}^{*}(\v{r}) \e^{\I\omega t}) \right) \\
&= \dfrac{1}{2\mu_{0}} \mathfrak{Re}\left\{  \cpq{\v{E}} \times \cpq{\v{B}}^{*}  \right\} + \dfrac{1}{2\mu_{0}} \mathfrak{Re}\left\{ \cpq{\v{E}} \times \cpq{\v{B}} \e^{-\I 2\omega t} \right\}
\end{align}
$$

> [!definition] Complex Poynting Vector
> The **complex Poynting vector** $\cpq{\v{S}}$ is defined as
> $$ \cpq{\v{S}} = \dfrac{1}{2} \cpq{\v{E}} \times \cpq{\v{H}}^{*}$$
> where $\cpq{\v{E}}$ and $\cpq{\v{H}}$ are the **complex electric field** and the **complex magnetic auxiliary field**, respectively.
> 
> The **unit** of $\cpq{\v{S}}$ is $\mathrm{W/m^{2}}$.

With the **complex Poynting vector**, we can express the **time-averaged Poynting vector** as
$$
\left\langle \v{S}(\v{r}) \right\rangle = \dfrac{1}{2\mu_{0}} \mathfrak{Re}\left\{  \cpq{\v{E}} \times \cpq{\v{B}}^{*}  \right\} = \mathfrak{Re} \left\{ \cpq{\v{S}} \right\}
$$
