## Changing Magnetic Field Produces Electric Field, 磁生电

### The Maxwell-Faraday Equation, 麦克斯韦—法拉第方程

> [!theorem] The Maxwell-Faraday Equation
> Generally, the **curl of the electric field $\v{E}$** is equal to the negative time derivative of the magnetic field $\v{B}$, i.e.
> $$\nabla \times \v{E} = -\dfrac{\partial}{\partial t} \v{B}$$

^0785d2

This equation describes how a **changing magnetic field** induces an electric field, which is the principle behind electromagnetic induction.

### Faraday’s Law of Induction, 法拉第电磁感应定律

We can integrate the Maxwell-Faraday equation over an **open surface** $S(t)$ bounded by a **closed curve** $P(t)$, which both can **change with time**. This gives us
$$
\oint_{P(t)} \v{E} \cdot \dif\v{l} = -\int_{S(t)} \dfrac{\partial}{\partial t} \v{B} \cdot \dif\v{a}
$$
According to [[Math Basement#Generalized Leibniz Integral Rule, 广义莱布尼兹积分法则|generalized Leibniz integral rule]], we have 
$$
\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} = \dfrac{\dif}{\dif t} \int_{S(t)} \v{B} \cdot \dif\v{a} = \int_{S(t)} \dfrac{\partial}{\partial t} \v{B} \cdot \dif\v{a} - \oint_{P(t)} \left( \v{v} \times \v{B} \right) \cdot \dif\v{l}
$$
where $\v{v}$ specifies the **spatially-dependent velocity of the boundary, 边界上各点的速度**. Therefore, we can rewrite the above equation as
$$
\oint_{P(t)} \v{E} \cdot \dif\v{l} = -\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} - \oint_{P(t)} \left( \v{v} \times \v{B} \right) \cdot \dif\v{l}
$$
i.e.
$$
\oint_{P(t)} \left( \v{E} + \v{v} \times \v{B} \right)  \cdot \dif\v{l} = -\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}}
$$
With stationary boundaries and time-varying magnetic field, we have

> [!theorem] Faraday’s Law of Induction
> The **induced EMF** around a closed path $P$ is equal to the negative time derivative of the magnetic flux $\varPhi_{\mathrm{B}}$ through the surface $S$ bounded by the path, i.e.
> $$
> \oint_{P} \v{E} \cdot \dif\v{l} = -\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} = - \dfrac{\dif}{\dif t} \int_{S} \v{B} \cdot \dif\v{a}
> $$

^300a21

### Transformer EMF \& Motional EMF, 感生电动势和动生电动势

In the above equation, the term $\displaystyle\oint_{P(t)} \left( \v{E} + \v{v} \times \v{B} \right)  \cdot \dif\v{l}$ is called the **total electromotive force (EMF)** around the closed path $P(t)$, which consists of two components:

+ $\displaystyle\oint_{P(t)} \v{E} \cdot \dif \v{l}$ is the **induced EMF** due to the changing magnetic field, which is also called the **transformer EMF, 感生电动势**, and

+ $\displaystyle\oint_{P(t)} \left( \v{v} \times \v{B} \right)  \cdot \dif\v{l}$ is the **motional EMF, 动生电动势**, due to the motion of the conductor in the magnetic field.

## Changing Electric Field Produces Magnetic Field, 电生磁

### The Maxwell-Ampère Equation, 麦克斯韦—安培方程

We recall [[Magnetic Fields#^7ae464|Ampere's Law]] in the form
$$
\nabla \times \v{B} = \mu_{0} \v{J}
$$
where $\v{J}$ is the **total current density**. Take the **divergence** of both sides, we have
$$
\nabla \cdot \left( \nabla \times \v{B} \right)  = \nabla \cdot \left( \mu_{0} \v{J} \right)
$$
and the left side is always zero, but **$\nabla \cdot \v{J}$ in general is not zero.** 

Applying [[Magnetic Fields#^3a9af4|Contiuity Equation]] and [[Electric Fields#^802761|Gauss's Law]], Maxwell proposed an identity as
$$
\nabla \cdot \v{J} = - \dfrac{\partial}{\partial t} \rho = - \dfrac{\partial}{\partial t} \left( \varepsilon_{0} \nabla \cdot \v{E} \right) = - \nabla \cdot \left( \varepsilon_{0} \dfrac{\partial}{\partial t} \v{E} \right)
$$
where $\rho$ is the **total charge density**. Therefore, we can rewrite the above equation as

> [!theorem] The Maxwell-Ampère Equation
> The **curl of the magnetic field $\v{B}$** is equal to the sum of the **current density $\v{J}$** and the **displacement current density $\varepsilon_{0} \dfrac{\partial}{\partial t} \v{E}$**, i.e.
> $$
> \nabla \times \v{B} = \mu_{0} \left( \v{J} + \varepsilon_{0} \dfrac{\partial}{\partial t} \v{E} \right)
> $$

^cf3f14

### Displacement Current, 位移电流

The term $\varepsilon_{0} \dfrac{\partial}{\partial t} \v{E}$ is called the **displacement current density, 位移电流密度**, which is not a real current density, but it **has the same effect** as a real current density **in producing a magnetic field**.

> [!example] The necessity of the displacement current
> ![[necessity_of_displacement_current.png]]

