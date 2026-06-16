## Four Equations in Maxwell's Theory, 麦克斯韦电磁场理论的四个方程 

### General Form of Maxwell's Equations, 麦克斯韦方程组的一般形式

We have now completed our study of the four **Maxwell's equations**. 

> [!theorem] Maxwell's Equations ("microscopic", differential form)
> + (i) **[[Electric Fields#^802761|Gauss's Law (for Electric Fields)]]**: 
> $$
> \nabla \cdot \v{E} = \dfrac{\rho}{\varepsilon_0}
> $$
> + (ii) **[[Magnetic Fields#^1da827|Gauss's Law (for Magnetic Fields)]]**:
> $$
> \nabla \cdot \v{B} = 0
> $$
> + (iii) **[[Electromagnetic Induction#^0785d2|Maxwell-Faraday Equation]]**:
> $$
> \nabla \times \v{E} = -\dfrac{\partial \v{B}}{\partial t}
> $$
> + (iv) **[[Electromagnetic Induction#^cf3f14|Ampere's Law with Maxwell's Addition]]**:
> $$
> \nabla \times \v{B} = \mu_0 \v{J} + \mu_0 \varepsilon_0 \dfrac{\partial \v{E}}{\partial t}
> $$

> [!theorem] Maxwell's Equations ("microscopic", integral form)
> + (i) **[[Electric Fields#^b02b31|Gauss's Law (for Electric Fields)]]**:
> $$
> \oint_{S} \v{E} \cdot \dif\v{a} = \dfrac{1}{\varepsilon_0} Q_{\mathrm{enc}}
> $$
> + (ii) **[[Magnetic Fields#^411afe|Gauss's Law (for Magnetic Fields)]]**:
> $$
> \oint_{S} \v{B} \cdot \dif\v{a} = 0
> $$
> + (iii) **[[Electromagnetic Induction#^300a21|Faraday's Law of Induction]]**:
> $$
> \oint_{P} \v{E} \cdot \dif\v{l} = -\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} = - \dfrac{\dif}{\dif t} \int_{S} \v{B} \cdot \dif\v{a}
> $$
> + (iv) **[[Electromagnetic Induction#^cf3f14|Ampere's Law with Maxwell's Addition]]**:
> $$
> \oint_{P} \v{B} \cdot \dif\v{l} = \mu_0 I_{\mathrm{enc}} + \mu_0 \varepsilon_0 \dfrac{\dif}{\dif t} \varPhi_{\mathrm{E}} = \mu_0 I_{\mathrm{enc}} + \mu_0 \varepsilon_0 \dfrac{\dif}{\dif t} \int_{S} \v{E} \cdot \dif\v{a}
> $$

### Maxwell's Equations in Material Media, 麦克斯韦方程组在介质中的形式

We know that **charges** can divided into two types, i.e.
$$
\rho = \rho_{\mathrm{f}} + \rho_{\mathrm{b}}
$$
For free charges, we have
$$
\nabla \cdot \v{J}_{\mathrm{f}} = - \dfrac{\partial}{\partial t} \rho_{\mathrm{f}}
$$
where $\v{J}_{\mathrm{f}}$ is the **free current density**. For bound charges, since $\rho = -\nabla \cdot \v{P}$, we have
$$
\nabla \cdot \v{J}_{\mathrm{p}} = - \dfrac{\partial}{\partial t} \rho_{\mathrm{b}} = \nabla \cdot \dfrac{\partial}{\partial t}\v{P}
$$
i.e. we have $\v{J}_{\mathrm{p}} = \dfrac{\partial}{\partial t}\v{P}$, where $\v{J}_{\mathrm{p}}$ is the **polarization current density, 极化电流密度**. 

Therefore, we can rewrite the **[[Electromagnetic Induction#^cf3f14|Ampere's Law with Maxwell's Addition]]** as
$$
\nabla \times \v{B} = \mu_0 \v{J}_{\mathrm{f}} + \mu_{0} \underbrace{ \nabla \times \v{M} }_{ \v{J}_{\mathrm{b}} } + \mu_{0} \underbrace{ \dfrac{\partial}{\partial t}\v{P} }_{ \v{J}_{\mathrm{p}} } + \mu_0 \underbrace{ \varepsilon_0 \dfrac{\partial \v{E}}{\partial t} }_{ \v{J}_{\mathrm{d}} }
$$
i.e.
$$
\nabla \times \underbrace{ \left( \dfrac{\v{B}}{\mu_{0}} - \v{M} \right) }_{ \v{H} }  = \v{J}_{\mathrm{f}} + \dfrac{\partial}{\partial t} \underbrace{ \left( \v{P} + \varepsilon \v{E}\right) }_{ \v{D} }
$$

Therefore, we have four **"macroscopic" equations**.

> [!theorem] Maxwell's Equations ("macroscopic", differential form)
> + (i) **[[Electric Displacement#^daf806|Gauss's Law (for Electric Displacement)]]**: 
> $$\nabla \cdot \v{D} = \rho_{\mathrm{f}}$$
> + (ii) **[[Magnetic Fields#^1da827|Gauss's Law (for Magnetic Fields)]]**:
> $$
> \nabla \cdot \v{B} = 0
> $$
> + (iii) **[[Electromagnetic Induction#^0785d2|Maxwell-Faraday Equation]]**:
> $$
> \nabla \times \v{E} = -\dfrac{\partial \v{B}}{\partial t}
> $$
> + (iv) **Ampere's Law with Maxwell's Addition for H Field**:
> $$
> \nabla \times \v{H} = \v{J}_{\mathrm{f}} + \dfrac{\partial \v{D}}{\partial t}
> $$

> [!theorem] Maxwell's Equations ("macroscopic", integral form)
> + (i) **[[Electric Displacement#^cf7cdd|Gauss's Law (for Electric Displacement)]]**:
> $$
> \oint_{S} \v{D} \cdot \dif\v{a} = Q_{\mathrm{f,enc}}
> $$
> + (ii) **[[Magnetic Fields#^411afe|Gauss's Law (for Magnetic Fields)]]**:
> $$
> \oint_{S} \v{B} \cdot \dif\v{a} = 0
> $$
> + (iii) **[[Electromagnetic Induction#^300a21|Faraday's Law of Induction]]**:
> $$
> \oint_{P} \v{E} \cdot \dif\v{l} = -\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} = - \dfrac{\dif}{\dif t} \int_{S} \v{B} \cdot \dif\v{a}
> $$
> + (iv) **Ampere's Law with Maxwell's Addition for H Field**:
> $$
> \oint_{P} \v{H} \cdot \dif\v{l} = I_{\mathrm{f,enc}} + \dfrac{\dif}{\dif t} \varPhi_{\mathrm{D}} = I_{\mathrm{f,enc}} + \dfrac{\dif}{\dif t} \int_{S} \v{D} \cdot \dif\v{a}
> $$

### What Maxwell's Equations Don't Tell Us, 麦克斯韦方程组不包含的内容

The **Maxwell's equations** are a set of four equations that describe the behavior of electric and magnetic **fields** with respect to **charges** and **currents**. Conclusions about these **field-generating elements** can be drawn from the equations. For example, the **[[Magnetic Fields#^3a9af4|Continuity Equation]]** of the current density $\v{J}$ can be derived from the **[[Electric Fields#^802761|Gauss's Law (for Electric Fields)]]** and **[[Electromagnetic Induction#^0785d2|Maxwell-Faraday Equation]]**.

The **Maxwell's equations** only discuss the electromagnetic **FIELDs**. They do not tell us anything about the **forces** acting on charges, 电荷所受的**力**, or the **energy** associated with the electromagnetic field, 电磁场的**能量**, since the four equations do not contain any physical quantities related to forces or energy.

## Electromagnetic Forces, 电磁作用

### Lorentz Force, 洛伦兹力

The **Lorentz force**, 洛伦兹力, is the force acting on a **point charge** $q$ moving with velocity $\v{v}$ in an electromagnetic field. The Lorentz force is given by
$$
\v{F} = q \left( \v{E} + \v{v} \times \v{B} \right)
$$

## Electromagnetic Energy, 电磁能量

### Joules' Law, 焦耳定律

For a continuous charge distribution within a volume $V$, the **work, 功**, done by the electromagnetic field on charge $\rho\dif\tau$ is given by
$$
\v{F} \cdot \dif\v{l} = \left( \rho\dif\tau \right) \left( \v{E} + \v{v} \times \v{B} \right) \cdot \v{v}\dif t = \v{E} \cdot \rho \v{v}\dif t\dif\tau = \v{E} \cdot \v{J} \dif t\dif\tau
$$
where $\v{J} = \rho \v{v}$ is the **current density**.

> [!theorem] Joules' Law
> The **power, 功率**, $P$, of the electromagnetic field (electric field $\v{E}$ and magnetic field $\v{B}$) within a volume $V$ is given by
> $$P = \dint_{V} \v{E} \cdot \v{J} \dif\tau$$
> where $\v{J}$ is the **current density**.

### Poynting's Theorem, 坡印亭定理

Consider a volume $V$ with a closed surface $S$. The **energy flow vector, 能量流矢量**, $\v{S}$, is defined as the energy **per unit time per unit area**, i.e.
$$
-\displaystyle\oint_{S} \v{S} \cdot \dif\v{a} = \dfrac{\dif}{\dif t} \text{Energy Saved in }V + \dfrac{\dif}{\dif t} \text{Energy Consumed in }V
$$
where the **energy saved in volume $V$** is given by the **energy density, 能量密度**, $u$, consisting of the [[Electric Displacement#^953b7c|electric energy density]] and [[Magnetic Auxiliary Field H#^0c6e4c|magnetic energy density]], i.e.
$$
u = \dfrac{1}{2} \varepsilon_0 \v{E}^2 + \dfrac{1}{2\mu_0} \v{B}^2 = \dfrac{1}{2} \varepsilon_0 E^2 + \dfrac{1}{2\mu_0} B^2
$$
and the **energy consumed in volume $V$** is given by the [[#Joules' Law, 焦耳定律]]. Thus, we have
$$
\begin{align}
-\displaystyle\oint_{S} \v{S} \cdot \dif\v{a} &= \dfrac{\dif}{\dif t} \dint_{V} u \dif\tau + \dint_{V} \v{E} \cdot \v{J} \dif\tau \\
&= \dfrac{\dif}{\dif t} \dint_{V} u \dif\tau + \dint_{V} \v{E} \cdot \left( \dfrac{1}{\mu_{0}} \nabla \times \v{B} - \varepsilon_{0} \dfrac{\partial}{\partial t} \v{E} \right) \dif\tau \\
&= \dfrac{\dif}{\dif t} \dint_{V} u \dif\tau + \dfrac{1}{\mu_{0}} \underbrace{ \dint_{V} \v{E} \cdot \left( \nabla \times \v{B} \right) \dif\tau }_{ \text{Integration by Parts} } - \varepsilon_{0} \dint_{V} \v{E} \cdot \dfrac{\partial}{\partial t} \v{E} \dif\tau \\
&= \dfrac{\dif}{\dif t} \dint_{V} u \dif\tau + \dfrac{1}{\mu_{0}} \dint_{V} \v{B} \cdot \underbrace{ \left( \nabla \times \v{E} \right) }_{ -\frac{\partial}{\partial t}\v{B} } \dif\tau -\dfrac{1}{\mu_{0}} \dint_{V} \nabla \cdot \left( \v{E} \times \v{B} \right) \dif\tau - \varepsilon_{0} \dint_{V} \v{E} \cdot \dfrac{\partial}{\partial t} \v{E} \dif\tau \\
&= \dfrac{\dif}{\dif t} \dint_{V} u \dif\tau - \underbrace{ \left( \dfrac{1}{\mu_{0}} \dint_{V} \v{B} \cdot \frac{\partial}{\partial t}\v{B} \dif\tau + \varepsilon_{0} \dint_{V} \v{E} \cdot \dfrac{\partial}{\partial t} \v{E} \dif\tau \right) }_{ \int_{V} \frac{\partial}{\partial t}\left( \frac{1}{2\mu_{0}}\v{B}^2 + \frac{1}{2}\varepsilon_{0}\v{E}^2 \right) \dif \tau  } -\dfrac{1}{\mu_{0}} \dint_{V} \nabla \cdot \left( \v{E} \times \v{B} \right) \dif\tau \\
&= - \dfrac{1}{\mu_{0}}\dint_{V} \nabla \cdot \left( \v{E} \times \v{B} \right) \dif\tau = - \dfrac{1}{\mu_{0}} \displaystyle\oint_{S} \left( \v{E} \times \v{B} \right) \cdot \dif\v{a}
\end{align}
$$

> [!definition] Poynting Vector
> The **Poynting vector, 坡印亭矢量**, is defined as
> $$\v{S} = \dfrac{1}{\mu_{0}} \v{E} \times \v{B}$$
> where $\v{E}$ and $\v{B}$ are the electric field and magnetic field, respectively.

> [!theorem] Poynting's Theorem (integral form)
> Poynting vector $\v{S}$ is the **energy flow vector, 能量流矢量**, which describes the energy flow per unit time per unit area, i.e.
> $$-\displaystyle\oint_{S} \v{S} \cdot \dif\v{a} = \dfrac{\dif}{\dif t} \dint_{V} u \dif\tau + \dint_{V} \v{E} \cdot \v{J} \dif\tau$$
> where:
> + $u = \dfrac{1}{2} \varepsilon_0 \v{E}^2 + \dfrac{1}{2\mu_0} \v{B}^2$ is the **energy density, 能量密度**,
> + $\v{J}$ is the **current density**,
> + $\v{E}$ and $\v{B}$ are the electric field and magnetic field, respectively.

It's easy to get the **differential form** of Poynting's theorem. We have

> [!theorem] Poynting's Theorem (differential form)
> The **negative divergence of the Poynting vector** is equal to the **rate of change of energy density** plus the **power density**, i.e.
> $$-\nabla \cdot \v{S} = \dfrac{\partial u}{\partial t} + \v{E} \cdot \v{J}$$
> where:
> + $\v{S} = \dfrac{1}{\mu_{0}} \v{E} \times \v{B}$ is the **Poynting vector, 坡印亭矢量**,
> + $u = \dfrac{1}{2} \varepsilon_0 \v{E}^2 + \dfrac{1}{2\mu_0} \v{B}^2$ is the **energy density, 能量密度**,
> + $\v{J}$ is the **current density**,
> + $\v{E}$ and $\v{B}$ are the electric field and magnetic field, respectively.






