## Polarization of a dielectric material, 电介质的极化

### Dipole moment of continuous charge distributions, 连续电荷分布的电偶极矩

We have **electric dipole moment** $\v{p}=q\v{d}$ for a pair of point charges $q$ and $-q$ separated by a distance $d$ when analyzing the [[Electric Fields#Electric Dipole|electric dipole]]. Given the two point charges are placed at $\v{r}'_{1}$ and $\v{r}'_{2}$, the electric dipole moment can be written as 
$$
\v{p} = q(\v{r}'_{1} - \v{r}'_{2}) = q\v{r}'_{1} + (-q)\v{r}'_{2}
$$
For **continuous charge distributions**, the electric dipole moment is defined as
$$
\v{p} = \int_{V} \v{r}' \rho(\v{r}') \dif \tau'
$$
and there is still 
$$
V(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\v{p} \cdot \vu{\mathscr{r}}}{\mathscr{r}^2}
$$

### Polarization and Bound Charges, 极化与束缚电荷

The electric field tends to **induce dipole moments** in the atoms and molecules of the material, which, when superimposed, manifests as macroscopic polarization of the material.

The **induced dipole moment** $\v{p}_{\text{ind}}$ is linearly related to the local electric field. Generally, we have
$$
\v{p}_{\text{ind}} = \boldsymbol{\alpha} \v{E}
$$
where $\boldsymbol{\alpha}$ is the **polarizability** of the material, which is a tensor in general. 

> [!definition]+ Polarization
> The **polarization** $\v{P}$ of a dielectric material is defined as the **dipole moment per unit volume** of the material, i.e., 
> $$
> \v{P} = \dfrac{\sum \v{p}}{V}
> $$
> The **unit** of polarization is $\mathrm{C/m^{2}}$.

> [!Note]- The Unit of Polarization
> The unit of polarization is 
> $$ 
> [\v{P}] = \dfrac{[\v{p}]}{[\Delta V]} = \dfrac{\rmu{C \cdot m}}{\rmu{m^{3}}} = \rmu{C/m^{2}} 
> $$
> which is the same as the unit of **surface charge density** $\sigma$.

#### Surface Bound Charges, 面束缚电荷

Consider a dielectric $x-y$ plane, which is uniformly polarized in the $z$ direction, then the **surface bound charge density** can lead to **dipole moments** in the material. Denote $d$ as the thickness of the dielectric, then on $x-y$ surface element $\dif a$ we have
$$
\v{p} = q\v{d} = (\sigma_{\mathrm{b}} \dif a) \v{d} = \v{P} \dif V = \v{P} (\dif a \dif z)
$$
therefore the **surface bound charge density** is 
$$
\sigma_{\mathrm{b}} = \v{P} \cdot \vu{n}
$$
where $\vu{n}$ is the unit normal vector of the surface.

#### Volume Bound Charges, 体束缚电荷

For a volume $V$ of the dielectric, denote its **volume bound charge density** inside as $\rho_{\mathrm{b}}$, then we have the total bound charge inside as
$$
\int_{V} \rho_{\mathrm{b}} \dif \tau = -\oint_{\partial V} \sigma_{\mathrm{b}} \dif a = -\oint_{\partial V} \v{P} \cdot \dif \v{a} = -\int_{V} \nabla \cdot \v{P} \dif \tau
$$
therefore the **volume bound charge density** is
$$
\rho_{\mathrm{b}} = -\nabla \cdot \v{P}
$$

> [!danger]+ Free Charges and Bound Charges
> The term **"bound charges"** has clear definitions in the context of polarization of dielectric materials. **Free charges** are _not only_ the charges that are free to move, but also the charges that are not induced from atomic and molecular dipoles. 
> 
> Put simply, **free charges are all charges except bound charges**.

## Gauss's Law for D Field, 电位移的高斯定理

### Electric Displacement, 电位移 

With dielectric materials, we can invoke the [[Electric Fields#Gauss's Law for E Field 电场高斯定理|Gauss's Law]] and get
$$
\nabla \cdot \v{E} = \dfrac{\rho}{\varepsilon_{0}} = \dfrac{1}{\varepsilon_{0}} \left( \rho_{\text{f}} + \rho_{\text{b}} \right) = \dfrac{1}{\varepsilon_{0}} \left( \rho_{\text{f}} - \nabla \cdot \v{P} \right)
$$
i.e., 
$$
\nabla \cdot \left( \varepsilon_{0} \v{E} + \v{P} \right) = \rho_{\text{f}}
$$

> [!definition]+ Electric Displacement
> The **electric displacement field** $\v{D}$ is defined as 
> $$
> \v{D} = \varepsilon_{0} \v{E} + \v{P}
> $$
> where $\v{P}$ is the polarization of the dielectric material, and $\v{E}$ is the _total_ electric field. The **unit** of $\v{D}$ is $\mathrm{C/m^{2}}$.

### Gauss's Law for D Field, 电位移的高斯定理 

From the introduction of electric displacement above we immediately have

> [!theorem] Gauss's Law for $\v{D}$ Field (differential form)
> The divergence of the electric displacement field $\v{D}$ at a point $\v{r}$ is given by
> $$
> \nabla \cdot \v{D}(\v{r}) = \rho_{\text{f}}(\v{r})
> $$
> where $\rho_{\text{f}}$ is the free charge density at $\v{r}$.

^daf806

Integrate the above equation over a volume $V$ and we have
$$
\int_{V} \nabla \cdot \v{D}(\v{r}) \dif \tau = \oint_{\partial V} \v{D}(\v{r}) \cdot \dif \v{a} = \int_{V} \rho_{\text{f}}(\v{r}) \dif \tau
$$

> [!theorem] Gauss's Law for $\v{D}$ Field (integral form)
> Integration of the electric displacement field $\v{D}$ over a closed surface $S$, or **the total electric displacement flux through $S$**, is given by
> $$
> \oint_{S} \v{D}(\v{r}) \cdot \dif \v{a} = Q_{\text{f, enc}}
> $$
> where $Q_{\text{f, enc}}$ is the total free charge enclosed by the surface $S$.

^cf7cdd

> [!danger]- There is NO Coulomb's Law for $\v{D}$ Field
> The electric displacement field $\v{D}$ is not a fundamental field, and it is not a conservative field. Therefore, there is no Coulomb's Law for $\v{D}$ field.

### Linear, Isotropic and Homogeneous Dielectrics, 线性各向同性均匀电介质 

[[#Gauss's Law for D Field  电位移的高斯定理|Gauss's Law]] for $\v{D}$ field provides a a convenient way to analyze the electric field in dielectric materials. However, the relationship between $\v{D}$ and $\v{E}$ is not simple because of the presence of polarization, which is a function of $\v{E}$ but _not directly proportional_ to it.

We hope to **simplify the relationship between $\v{P}$ and $\v{E}$**, so that we consider the following special cases:

+ **Linear, 线性**: $\v{P}(\v{r}) = \varepsilon_{0}\boldsymbol{\chi}_{\mathrm{e}}(\v{r})\v{E}(\v{r})$, where $\boldsymbol{\chi}_{\mathrm{e}}$ is a spatially-varying tensor.
+ Linear and **Isotropic, 各向同性**: $\v{P}(\v{r}) = \varepsilon_{0}\chi_{\mathrm{e}}(\v{r})\v{E}(\v{r})$, where $\chi_{\mathrm{e}}$ is a spatially dependent scalar.
+ Linear, Isotropic and **Homogeneous, 均匀**: $\v{P} = \varepsilon_{0}\chi_{\mathrm{e}}\v{E}$, where $\chi_{\mathrm{e}}$ is a constant scalar.

For **linear, isotropic and homogeneous (LIH) dielectrics**, the polarization is linearly related to the electric field, i.e., 
$$
\v{P} = \boldsymbol{\alpha} \v{E} = \varepsilon_{0} \chi_{\mathrm{e}} \v{E}
$$
where $\chi_{\mathrm{e}}$ is the **electric susceptibility, 电极化率**, of the material, which is a _unit-less_ constant scalar, and $\v{E}$ is the **total** electric field.

Therefore, the electric displacement field in LIH dielectrics is 
$$
\v{D} = \varepsilon_{0} \v{E} + \v{P} = \varepsilon_{0} \v{E} + \varepsilon_{0} \chi_{\mathrm{e}} \v{E} = \varepsilon_{0} (1 + \chi_{\mathrm{e}}) \v{E} = \varepsilon \v{E}
$$
where:
+ $\varepsilon = \varepsilon_{0} (1 + \chi_{\mathrm{e}})$ is the **permittivity, 介电常数**, of the material, and 
+ $\varepsilon_{\mathrm{r}} = 1 + \chi_{\mathrm{e}}$ is the **relative permittivity, 相对介电常数**, of the material.

## Electric Boundary Conditions, 电边界条件 

### For Perpendicular Component, 垂直分量 

For an interface in space, consider a cylinder with height $h$ and cross-sectional area $A$ which goes through the interface perpendicularly. Apply Gauss's Law within the cylinder, we have
$$
\oint_{S} \v{E} \cdot \dif \v{a} = \dfrac{Q_{\text{enc}}}{\varepsilon_{0}} = \dfrac{\sigma A}{\varepsilon_{0}} \xRightarrow{h \to 0} AE_{1\perp} - AE_{2\perp} = \dfrac{\sigma A}{\varepsilon_{0}}
$$

Thus, on the direction perpendicular, 

+ For **electric field** $E_{\perp}$, $$E_{1\perp} - E_{2\perp} = \dfrac{\sigma}{\varepsilon_{0}}$$where $E_{1\perp}$ is pointing from the surface to the dielectric 1, and $E_{2\perp}$ is pointing from dielectric 2 to the surface.
	$E_{\perp}$ is **NOT continuous** across the boundary if there are charges on the surface.

+ For **electric displacement** $D_{\perp}$ $$D_{1\perp} - D_{2\perp} = \sigma_{\mathrm{f}}$$$D_{\perp}$ is **continuous** across the boundary if there are only free charges (or no charges) on the surface. ^ef3fb6

### For Parallel Component, 平行分量 

For an interface in space, on the direction parallel (the direction is **not fixed**), we can integrate the electric field along a rectangular loop across the boundary, and we have
$$
\oint_{C} \v{E} \cdot \dif \v{l} \equiv 0 \xRightarrow{h \to 0} \v{E}_{1\parallel} \cdot \v{l} - \v{E}_{2\parallel} \cdot \v{l} = 0
$$
where $\v{l}$ is the direction of the long side of the rectangle, and is **arbitrary** in the parallel direction.

Therefore, on the direction parallel, 

+ For **electric field** $\v{E}_{\parallel}$, 
    $$
    \v{E}_{1\parallel} = \v{E}_{2\parallel}
    $$
	$\v{E}_{\parallel}$ is **continuous** across the boundary.

+ For **electric displacement** $\v{D}_{\parallel}$, 
    $$
    \v{D}_{1\parallel} - \v{D}_{2\parallel} = \v{P}_{1\parallel} - \v{P}_{2\parallel}
    $$
    where $\v{P}_{\parallel}$ is the projection of polarization in the parallel plane. 
	$\v{D}_{\parallel}$ is **continuous** across the boundary.


### For Electric Potential, 电势 

For the electric potential $V$, we have
$$
V_{1} - V_{2} = -\int_{(2)}^{(1)} \v{E} \cdot \dif \v{l} \stackrel{h \to 0}{=\!=\!=} 0
$$
therefore, the electric potential is always **continuous** across the boundary.

Given $E_{\perp}$ is not continuous across the boundary, we have
$$
\dfrac{\partial V_{1}}{\partial \vu{n}} - \dfrac{\partial V_{2}}{\partial \vu{n}} = -E_{1\perp} - (-E_{2\perp}) = -\dfrac{\sigma}{\varepsilon_{0}}
$$
where $\vu{n}$ is the unit normal vector pointing from dielectric 2 to dielectric 1 (in consistent with the direction of $E_{\perp}$).

## Capacitor, 电容

### Capacitance of a Parallel-Plate Capacitor, 平行板电容器的电容

Suppose a plate in vacuum with **surface charge density $\sigma$**, then the electric field above and below the plate is 
$$
E = \dfrac{\sigma}{2\varepsilon_{0}}
$$
If $+\sigma$ and $-\sigma$ plates are **separated by a distance $d$**, then the electric field between the plates is $E = \dfrac{\sigma}{\varepsilon_{0}}$ which is a constant, and outside the plates $E = 0$.

Given the constant electric field between the plates, the potential difference between the plates is
$$
V = Ed = \dfrac{\sigma d}{\varepsilon_{0}}
$$
which is proportional to the surface charge density $\sigma$, or the charge $Q$ on the plates with constant area $A$.

> [!definition]+ Capacitance ^9bb28d
> The **capacitance** $C$ of a capacitor is defined as the ratio of the charge $Q$ on the plates to the potential difference $V$ between the plates, i.e., 
> $$
> C = \dfrac{Q}{V} \stackrel{\scriptstyle\text{for parallel-plate}\atop\scriptstyle\text{in vaccum}}{=\!=\!=\!=\!=\!=\!=\!=\!=\!=} \dfrac{\sigma A}{\dfrac{\sigma d}{\varepsilon_{0}}} = \dfrac{\varepsilon_{0} A}{d}
> $$
> where $A$ is the area of the plates, and $d$ is the separation between the plates.



### Energy Stored in a Capacitor, 电容器的储能

Cositder the situation of charging up a capacitor with a current $I$, The **energy stored in the capacitor** is the work done to charge the capacitor, which is 
$$
U = \int_{0}^{T} P\dif t = \int_{0}^{T} V(t) \cdot C \dfrac{\dif V(t)}{\dif t} \dif t = \int_{0}^{T} V(t) \cdot C \dif V(t) = \dfrac{1}{2} CV_{0}^{2}
$$
where $V_{0}$ is the final potential difference between the plates.

Assume $\v{E}$ and $A$ keeps constant, then $C \propto d^{-1}$ and $V_0 \propto d$, therefore **the energy stored $U \propto d \propto V_{\mathrm{volume}}$**, therefore we can introduce 

> [!definition]+ Energy Density of Electric Field ^953b7c
> The **energy density of electric field** or **electric energy density** $w_{\mathrm{e}}$ is defined as the energy stored per unit volume, i.e., 
> $$
> w_{\mathrm{e}} = \dfrac{U}{V_{\mathrm{volume}}} = \dfrac{1}{2} \varepsilon_{0} E^{2}
> $$
> where $E$ is the magnitude of the electric field.

### Dielectric Capacitor, 电介质电容器

When a dielectric material is inserted between the plates of a capacitor, the **capacitance increases** because the electric field is reduced by the polarization of the dielectric. The **capacitance of a dielectric capacitor** is 
$$
C = \dfrac{Q}{V} = \dfrac{A\sigma}{\dfrac{\sigma}{\varepsilon_{0}\varepsilon_{\mathrm{r}}}} = \left( \dfrac{\varepsilon_{0}A}{d} \right) \cdot \varepsilon_{\mathrm{r}} = C_{0} \varepsilon_{\mathrm{r}} 
$$
where $C_{0} = \dfrac{\varepsilon_{0}A}{d}$ is [[#^9bb28d|the capacitance of the capacitor in vacuum]], and $\varepsilon_{\mathrm{r}}$ is the relative permittivity of the dielectric material.

> [!example]+ A More Complex Situation 
> For more complex situations, where a vacuum gap (of width $d$) is left between the dielectric slab (of width $h$) and the capacitor plate on both sides. 
> 
> According to the conclusion that **[[#^ef3fb6|D is continuous across the boundary]]**, we have 
> $$
> \varepsilon_{0}E_{1} = \varepsilon E_{2}
> $$
> so that the electric field in the dielectric is 
> $$
> E_{1}d + E_{2}h + E_{1}d = V \Longrightarrow E_{1} = \dfrac{V}{2d + h/\varepsilon_{\mathrm{r}}}
> $$ 
> and the **induced charge density** on the surface of the dielectric is 
> $$
> \sigma_{\mathrm{b}} = -\varepsilon_{0} (E_{1} - E_{2}) = -\varepsilon_{0} \left( 1 - \dfrac{1}{\varepsilon_{\mathrm{r}}} \right) \dfrac{V}{2d + h/\varepsilon_{\mathrm{r}}} = -\dfrac{ \varepsilon_{0}(\varepsilon_{\mathrm{r}} - 1)V}{2\varepsilon_{\mathrm{r}}d + h}
> $$
> Given $E_{1} = \dfrac{\sigma_{\mathrm{f}}}{\varepsilon_{0}}$, we also have
> $$
> \sigma_{\mathrm{b}} = -\left( 1 - \dfrac{1}{\varepsilon_{\mathrm{r}}} \right) \sigma_{\mathrm{f}}
> $$
> where $\sigma_{\mathrm{f}}$ and $\sigma_{\mathrm{b}}$ are on the same side of the dielectric.




