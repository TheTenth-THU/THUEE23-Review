## Magnetization of Materials, 材料的磁化

### Magnetization, 磁化强度

An external magnetic field can **affect the spin and orbital motion** of electrons in materials, which are all considered as **[[Magnetostatics#Magnetic Dipole, 磁偶极子|magnetic dipoles, 磁偶极子]]**, and lead to **extra magnetic dipole moments** in the material. 

> [!definition] Magnetization
> The **magnetization $\v{M}$** of a material is defined as the **magnetic dipole moment per unit volume**, i.e.
> $$\v{M} = \dfrac{\sum\limits\v{m}}{V}$$
> The **unit** of magnetization is $\mathrm{A/m}$.

### Bound Current, 磁化电流

For a magnetic dipole, $\v{A}(\vr) = \dfrac{\mu_{0}}{4\pi} \dfrac{\v{m} \times \vu{\sr}}{\sr^2}$. Therefore, for a **volume distribution of magnetic dipoles** $\sum\limits \v{m} = \dint_{V} \v{M} \dif\tau$, we have
$$
\begin{align}
\v{A}(\v{r}) &= \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\v{M}(\v{r}') \times \hat{\sr }}{\sr ^2} \dif \tau'  \\
&= \dfrac{\mu_{0}}{4\pi} \int_{V} \v{M}(\v{r}') \times \left( \nabla' \dfrac{1}{\sr} \right)  \dif \tau' \\
&= \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\nabla' \times \v{M}(\v{r}')}{\sr} \dif \tau' - \dfrac{\mu_{0}}{4\pi} \int_{V} \nabla' \times \left( \dfrac{\v{M}(\v{r}')}{\sr} \right) \dif \tau' \\
&= \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\overbrace{ \nabla' \times \v{M}(\v{r}') }^{ \v{J}_{\mathrm{b}} }}{\sr} \dif \tau' - \dfrac{\mu_{0}}{4\pi} \oint_{\partial V} \dfrac{\overbrace{ \v{M}(\v{r}') \times \hat{n} }^{ \v{K}_{\mathrm{b}} }}{\sr} \dif a'
\end{align}
$$
where the last equality is due to [[Math Basement#Curl version of the Divergence Theorem|the curl version of the Divergence Theorem]].

Inspired by the above equation, and imitating the definition of **[[Electric Displacement#Surface Bound Charges, 面束缚电荷|Surface Bound Charges, 面束缚电荷]]**, and **[[Electric Displacement#Volume Bound Charges, 体束缚电荷|Volume Bound Charges, 体束缚电荷]]**, we can define the **volume bound current density** as
$$
\v{J}_{\mathrm{b}}(\vr) = \nabla \times \v{M}(\vr)
$$
and the **surface bound current density** as
$$
\v{K}_{\mathrm{b}}(\vr) = \v{M}(\vr) \times \hat{n}
$$
where $\hat{n}$ is the unit normal vector pointing out of the surface.

## Ampère's Law for H Field, H 场的安培环路定理

### Magnetic Auxiliary Field H, H 场

With magnetization, we can invoke the [[Magnetic Fields#^7ae464|Ampère's Law]] and get
$$
\nabla \times \v{B} = \mu_{0} \v{J} = \mu_{0} \v{J}_{\mathrm{f}} + \mu_{0} \v{J}_{\mathrm{b}} = \mu_{0} \v{J}_{\mathrm{f}} + \mu_{0} \nabla \times \v{M}
$$
i.e.
$$
\nabla \times \left( \dfrac{\v{B}}{\mu_{0}} - \v{M} \right) = \v{J}_{\mathrm{f}}
$$

> [!definition] Magnetic Auxiliary Field H
> The **magnetic auxiliary field $\v{H}$** is defined as
> $$\v{H} = \dfrac{\v{B}}{\mu_{0}} - \v{M}$$
> where $\v{B}$ is the _total_ magnetic field, $\mu_{0} = 4\pi \times 10^{-7} \mathrm{Tm/A}$ is the vacuum permeability, and $\v{M}$ is the magnetization. The **unit** of $\v{H}$ is $\mathrm{A/m}$.

### Ampère's Law for H Field, H 场的安培环路定理

> [!theorem] Ampère's Law for H Field (differential form)
> The **curl** of the magnetic auxiliary field $\v{H}$ is equal to the **free current density** $\v{J}_{\mathrm{f}}$, i.e.
> $$\nabla \times \v{H} = \v{J}_{\mathrm{f}}$$

> [!theorem] Ampère's Law for H Field (integral form)
> The line integral of the magnetic auxiliary field $\v{H}$ along a closed path $\varGamma$ is equal to the **total free current** $I_{\mathrm{f,enc}}$ passing through the surface $S$ enclosed by the path $\varGamma$, i.e.
> $$\oint_{\varGamma} \v{H}(\v{r}) \cdot \dif \v{l} = I_{\mathrm{f,enc}}$$

### Magnetic Susceptibility and Permeability, 磁化率和磁导率

For most magnetic materials, the magnetization $\v{M}$ is **proportional** to the magnetic field $\v{H}$, i.e.
$$
\v{M} = \chi_{\mathrm{m}} \v{H}
$$
where $\chi_{\mathrm{m}}$ is the **magnetic susceptibility, 磁化率**, of the material. It is a _unitless_ scalar.

In the above circumstance, the magnetic field $\v{B}$ can be expressed as
$$
\v{B} = \mu_{0} (\v{H} + \v{M}) = \mu_{0} (1 + \chi_{\mathrm{m}}) \v{H} = \mu_{0} \mu_{\mathrm{r}} \v{H} = \mu \v{H}
$$
where:
+ $\mu_{0}$ is the **vacuum permeability, 真空磁导率**, which is a constant $\mu_{0} = 4\pi \times 10^{-7} \rmu{T \cdot m/A}$,
+ $\mu_{\mathrm{r}} = 1 + \chi_{\mathrm{m}}$ is the **relative permeability, 相对磁导率**, of the material, which is a _unitless_ scalar,
+ $\mu$ is the **permeability, 磁导率**, of the material, with unit of $\mathrm{T\cdot m/A = H/m}$.

> [!example] B field of a long solenoid with core
> Consider a **long solenoid** along $z$ axis, with radius of $R$ and turns of $N$ per unit length, carrying a **steady current $I$**. We know [[Magnetic Fields#^287a4f|the magnetic field inside the solenoid is uniform]] as $\v{B} = \mu_{0}NI \vu{z}$.
>
> If the solenoid is filled with a magnetic material with **magnetic suscptibility $\chi_{\mathrm{m}}$**, we would have no idea about the **total current distribution**. In this case, we can apply the [[#Ampère's Law for H Field, H 场的安培环路定理|Ampère's Law]] and get
> $$
> \displaystyle\oint_{C} \v{H} \cdot \dif \v{l} = H_{z} h = I_{\mathrm{f,enc}} = NhI
> $$
> where $C$ is a rectangular path with height $h$. Therefore,
> $$
> \v{H} = NI\vu{z}
> $$
> and
> $$
> \v{B} = \mu_{0} (1 + \chi_{\mathrm{m}}) NI \vu{z}
> $$

## Magnetic Boundary Conditions, 磁边界条件

### For Normal (Perpendicular) Component, 法向分量

Applying the [[Magnetic Fields#Gauss's Law for B Field, 磁场高斯定理|Gauss's Law for B Field]] to a thin wafer across the boundary, we have
$$
\oint_{S} \v{B} \cdot \dif \v{a} = 0  \xRightarrow{h \to 0}  B_{1\perp} A - B_{2\perp} A = 0
$$

Thus, on the direction perpendicular, 

+ For magnetic field $B_{\perp}$, 
    $$B_{1\perp} = B_{2\perp}$$
    $B_{\perp}$ is always **continuous** across the boundary.

+ For $H_{\perp}$, since $\v{H} = \dfrac{1}{\mu_{0}}\v{B} - \v{M}$ we have 
    $$H_{1\perp} - H_{2\perp} = M_{2\perp} - M_{1\perp}$$
    So $H_{\perp}$ is **discontinuous** across the boundary generally. 

### For Tangential (Parallel) Component, 切向分量

Applying the Ampère's Circuital Law to a loop along the boundary, we have
$$
\begin{align}
&\text{Perpendicular to the current} && \oint_{C} \v{B} \cdot \dif \v{l} = \mu_{0} KL = (B_{1} - B_{2})L \\
&\text{Parallel to the current} && \oint_{C} \v{B} \cdot \dif \v{l} = 0 = (B_{1} - B_{2})L 
\end{align}
$$

Thus, on the direction parallel, 

+ For magnetic field $\v{B}_{\parallel}$, $$\v{B}_{1\parallel} - \v{B}_{2\parallel} = \mu_{0} (\v{K} \times \vu{n})$$where $\v{K}$ is the surface current density, and $\vu{n}$ is the normal vector pointing from medium 2 to medium 1. $B_{\parallel}$ will be **continuous** across the boundary if there is **no surface current**.

+ For $\v{H}_{\parallel}$, since $\v{H} = \dfrac{1}{\mu_{0}}\v{B} - \v{M}$ we have $$\v{H}_{1\parallel} - \v{H}_{2\parallel} = \v{K}_{\mathrm{f}} \times \vu{n}$$where $\v{K}_{\mathrm{f}}$ is the free surface current density. So $\v{H}_{\parallel}$ will be **continuous** across the boundary if there is **no free surface current**, or there is **only free surface current**.

## Inductors, 电感

### Inductance of a Solenoid, 线圈电感器的电感

From [[Magnetic Fields#^287a4f|the previous calculation]], we have the magnetic field inside a solenoid as
$$
B = \mu_{0} \overline{N}I = \mu_{0} \dfrac{N}{l} I
$$
where $\overline{N}$ is the **number of turns per unit length**, $N$ is the **number of turns** of the solenoid, and $l$ is the length of the solenoid. Assume the **area** of the solenoid is $A$, we have the **total magnetic flux** as
$$
\varPhi_{\mathrm{B}} = NB A = \mu_{0} A I \dfrac{N^2}{l}
$$
Therefore,
$$
\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} = \mu_{0} A \dfrac{N^2}{l} \dfrac{\dif I}{\dif t}
$$

> [!definition] Inductance
> The **inductance $L$** of a solenoid is defined as the ratio of the **total magnetic flux** $\varPhi_{\mathrm{B}}$ to the **current** $I$ through the solenoid, i.e.
> $$L = \dfrac{\varPhi_{\mathrm{B}}}{I}$$
> It is also defined as the ratio of the **variation of the magnetic flux** to the **variation of the current**, i.e.
> $$L = \dfrac{\dif \varPhi_{\mathrm{B}}}{\dif I} = \dfrac{\dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}}}{\dfrac{\dif}{\dif t} I}$$
> The **unit** of inductance is $\rmu{H}$ (henry), and $1 \rmu{H} = 1 \rmu{V \cdot s/A}$.

For the above solenoid, we know the **transformer EMF** is
$$
\mathcal{E} = - \dfrac{\dif}{\dif t} \varPhi_{\mathrm{B}} = - L \dfrac{\dif I}{\dif t}
$$

### Energy Stored in an Inductor, 电感器中的能量

Cositder the situation of charging up an inductor with a **constant-voltage source $V$** and a switch. The **energy stored in the inductor** is the work done to charge the inductor, which is 
$$
U = \int_{0}^{T} P \dif t = \int_{0}^{T} I(t) \cdot L \dfrac{\dif I(t)}{\dif t} \dif t
= \int_{0}^{I_{0}} L I \dif I = \dfrac{1}{2} L I_{0}^2
$$
where $I_{0}$ is the current at time $T$.

Assume $B = \mu_{0} \dfrac{N}{l} I$ and $A$ keeps constant, then $L = \mu_{0} A \dfrac{N^2}{l} \propto l^{-1}$ and $I_{0} \propto l$, therefore **the energy stored $U \propto l \propto V_{\mathrm{volume}}$**, therefore we can introduce 

> [!definition] Energy Density of Magnetic Field
> The **energy densityof the magnetic field** or **magnetic energy density** $w_{\mathrm{m}}$ is defined as
> $$w_{\mathrm{m}} = \dfrac{U}{V_{\mathrm{volume}}} = \dfrac{1}{2\mu_{0}} B^2$$
> where $B$ is the magnitude of the magnetic field.

^0c6e4c



