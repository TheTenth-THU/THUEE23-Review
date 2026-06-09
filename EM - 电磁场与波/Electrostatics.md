## Key Concepts of Electrostatics  静电学的关键概念

> [!note]- Relation among $\v{\boldsymbol{E}}$, $\boldsymbol{V}$ and $\boldsymbol{\rho}$
> ![[relation_E_V_rho.drawio.svg]]

### Electric Fields  电场

#### Coulomb's Law  库仑定律

The **electric force** between two point charges is given by **[[Electric Fields#Coulomb's Law, 库仑定律|Coulomb's Law]]**:
$$\v{F}(\v{r}_{2};\v{r}_{1}) = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{\mathscr{r}^2} \vu{\mathscr{r}}$$
where:
+ $q_1$ and $q_2$ are two point charges positioned at $\v{r}_1$ and $\v{r}_2$ respectively,
+ $\vsr{r} = \v{r}_2 - \v{r}_1$ is the separation vector,
+ $\varepsilon_0$ is the **vacuum permittivity**.

##### Electric Field of a Point Charge  点电荷的电场

The **[[Electric Fields#^5995df|electric field]] $\v{E}$** at a point $\v{r}$ due to a point charge $q$ located at $\v{r}'$ is given by 
$$\v{E}(\v{r};\v{r}') = \dfrac{q}{4\pi\varepsilon_{0}\mathscr{r}^2} \vu{\mathscr{r}}$$
where:
+ $\v{\mathscr{r}} = \v{r} - \v{r}'$, 
+ $\varepsilon_{0}$ is the vacuum permittivity.

Immediately we have: 
$$
\nabla \cdot \v{E}(\v{r};\v{r}') = \nabla \cdot \left( \dfrac{q}{4\pi\varepsilon_{0}\mathscr{r}^2} \vu{\mathscr{r}} \right) = \dfrac{q}{4\pi\varepsilon_{0}} \nabla \cdot \left( \dfrac{\vu{\mathscr{r}}}{\mathscr{r}^2} \right) = \dfrac{q}{\varepsilon_{0}} \delta^{3}(\v{\mathscr{r}})
$$
^d57c08

##### Superposition Principle  叠加原理

**[[Electric Fields#Superposition Principle 叠加原理|The superposition principle]]** states that the total electric field is the **sum of the fields** due to each charge, like
$$
\v{E}(\v{r}) = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}^2} \vu{\mathscr{r}_{i}}
$$
where:
+ $q_i$ are point charges at positions $\v{r}_{i}$,
+ $\v{\mathscr{r}_{i}} = \v{r} - \v{r}_{i}$.

For continuous charge distributions, 
+ For a **line charge** $\lambda(\v{r}')$ on $\dif l'$, the electric field at $\v{r}$ is given by
$$
\dif \v{E} = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\lambda(\v{r}') \dif l'}{\mathscr{r}^2} \vu{\mathscr{r}}
$$
+ For a **surface charge** $\sigma(\v{r}')$ on $\dif a'$, the electric field at $\v{r}$ is given by
$$
\dif \v{E} = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\sigma(\v{r}') \dif a'}{\mathscr{r}^2} \vu{\mathscr{r}}
$$
+ For a **volume charge** $\rho(\v{r}')$ in $\dif \tau'$, the electric field at $\v{r}$ is given by
$$
\dif \v{E} = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\rho(\v{r}') \dif \tau'}{\mathscr{r}^2} \vu{\mathscr{r}}
$$

#### Gauss's Law for E Field  电场高斯定理

**[[Electric Fields#Gauss's Law for E Field 电场高斯定理|Gauss's Law]]** states that **the total electric flux** through a closed surface is equal to **the total charge** enclosed by the surface, divided by the vacuum permittivity.

> [!theorem] Gauss's Law (integral form)
> Integration of the electric field $\v{E}$ over a closed surface $S$, or **the total electric flux through $S$**, is given by
> $$\oint_{S} \v{E}(\v{r}) \cdot \dif \v{a} = \dfrac{Q_{\text{enc}}}{\varepsilon_{0}}$$
> where $Q_{\text{enc}}$ is the total charge enclosed by the surface $S$.

> [!theorem] Gauss's Law (differential form)
> The **divergence** of the electric field $\v{E}$ at a point $\v{r}$ is given by
> $$\nabla \cdot \v{E}(\v{r}) = \dfrac{\rho(\v{r})}{\varepsilon_{0}}$$
> where $\rho(\v{r})$ is the charge density at $\v{r}$.

#### Circuital Law for Static E Field  静电场的环路定理

**[[Electric Fields#Circuital Law for Static $ boldsymbol{E}$ Field 静电场的环路定理|Circuital Law]]** states that the line integral of the **static electric field $\v{E}$** along a closed path is zero.

> [!theorem] Circuital Law for Static $\v{E}$ Field (integral form)
> The line integral of the electric field $\v{E}$ along a closed path $\varGamma$ is zero, i.e.
> $$\oint_{\varGamma} \v{E}(\v{r}) \cdot \dif \v{l} = 0$$

> [!theorem] Circuital Law for Static $\v{E}$ Field (differential form)
> The curl of the electric field $\v{E}$ is zero vector, i.e.
> $$\nabla \times \v{E}(\v{r}) = \v{0}$$

### Electric Potential  电势

#### Electric Potential of Point Charges  点电荷的电势

Noticing $\v{E}(\v{r}) = - \nabla \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}}$ is the gradient of some scalar field, we define this scalar field as the **electric potential $V$**.
$$V(\v{r}) = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}}$$
where: 
+ $q_{i}$ are point charges at positions $\v{r}_{i}$,
+ $\v{\mathscr{r}_{i}} = \v{r} - \v{r}_{i}$,
+ $\varepsilon_0$ is the vacuum permittivity.

Then, the electric field can be calculated by $\v{E}(\v{r}) = - \nabla V(\v{r})$.

#### Conservative Property of Static Electric Fields  静电场的保守性

The integration of the static electric field $\v{E}$ is **independent of the path taken**, so we say the electric field $\v{E}$ is **conservative**, and the electric potential $V$ is well-defined as **a function of charge distribution** like
$$
V(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \int_{\mathbb{R}^3} \dfrac{\rho(\v{r})}{\mathscr{r}} \dif \tau = \dfrac{1}{4\pi\varepsilon_{0}} \int_{\mathbb{R}^3} \dfrac{\dif q}{\mathscr{r}} 
$$

#### Poisson's Equation  泊松方程

For a charge distribution $\rho(\v{r})$, the electric field $\v{E}$ and the electric potential $V$ are related by $\nabla \cdot \v{E} = \dfrac{\rho}{\varepsilon_{0}}$ and $\v{E} = - \nabla V$, so we have **[[Electric Potential#^db59a9|Poisson's Equation]]**
$$\nabla^2 V(\v{r}) = - \dfrac{\rho(\v{r})}{\varepsilon_{0}}$$
Especially, at the point with zero charge density, the electric potential satisfies **[[Electric Potential#^127adf|Laplace's Equation]]**
$$\nabla^2 V(\v{r}) = 0$$

### Electric Displacement  电位移



## Applications of Electrostatics, 静电学的应用

### Electric Dipole, 电偶极子

#### Electric Dipole Moment, 电偶极矩

Consider a pair of point charges $q$ and $-q$ separated by a distance $d$, the electric **potential** at a point $\v{r}$ **far away** from the dipole is given by
$$V(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \left( \dfrac{q}{\mathscr{r}_{+}} - \dfrac{q}{\mathscr{r}_{-}} \right) 
= \dfrac{q}{4\pi\varepsilon_{0}} \dfrac{d}{\mathscr{r}^2} \cos \theta$$
here the 2nd equality is due to the fact that
$$
\dfrac{1}{\mathscr{r}_{+}} = \dfrac{1}{\mathscr{r}} \left( 1 - \dfrac{d}{2\mathscr{r}} \cos \theta \right)^{-1} \approx \dfrac{1}{\mathscr{r}} \left( 1 + \dfrac{d}{2\mathscr{r}} \cos \theta \right)
$$
and $\dfrac{1}{\mathscr{r}_{-}}$ is similar, where $\theta$ is the angle between $\v{r}$ and the dipole axis.

> [!definition]+ Electric dipole moment
> The **electric dipole moment $\v{p}$** of a pair of point charges $q$ and $-q$ separated by a distance $d$ is defined as
> $$\v{p} = q\v{d}$$
> where $\v{d}$ is the separation vector from $-q$ to $q$.

#### Electric Field of an Electric Dipole, 电偶极子的电场

So the **electric potential** can be written as 
$$V_{\mathrm{dip}}(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\v{p} \cdot \vu{\mathscr{r}}}{\mathscr{r}^2}$$
Then we can calculate the **electric field of the dipole** by
$$
\v{E}_{\mathrm{dip}}(\v{r}) = - \nabla V_{\mathrm{dip}}(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{1}{r^3} \left( 3 (\v{p} \cdot \vu{r} )\vu{r} - \v{p} \right)
$$
If we put the dipole at the origin, we have the **electric field of a dipole** under _spherical coordinates_ as
$$
\v{E}_{\mathrm{dip}}(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{p}{r^3} \left( 2 \cos \theta \,\vu{r} + \sin \theta \,\vu{\theta} \right)
$$
where the dipole moment $\v{p}$ is in the direction of $\vu{z}$. 

The results above for an ideal dipole are **_identical_** to the **[[Magnetostatics#Magnetic Field of a Magnetic Dipole, 磁偶极子的磁场|magnetic field of a magnetic dipole]]**.

#### Electric Force upon an Electric Dipole, 电偶极子上的电场力

An electric dipole placed in a **_non-uniform_** electrostatic field will experience a force.

The **total electric energy** of an electric dipole in an electric field is given by
$$
\begin{align}
U_{\mathrm{E}} &= U_{+} + U_{-} = q \dint_{\v{r}_{+}}^{\infty} \v{E} \cdot \dif \v{l} + (-q) \dint_{\v{r}_{-}}^{\infty} \v{E} \cdot \dif \v{l}  \\
&= q \left( \dint_{\v{r}_{+}}^{\infty} \v{E} \cdot \dif \v{l} + \dint^{\v{r}_{-}}_{\infty} \v{E} \cdot \dif \v{l} \right)  \\
&= q \dint_{\v{r}_{+}}^{\v{r}_{-}} \v{E} \cdot \dif \v{l} = -q \v{E}(\v{r}) \cdot \v{d} = - \v{p} \cdot \v{E}(\v{r})
\end{align}
$$
Thus, **the electric force** on the dipole is the negative gradient of the potential energy, i.e.
$$
\v{F}_{\mathrm{E}} = - \nabla U_{\mathrm{E}} = \nabla \left( \v{p} \cdot \v{E}(\v{r}) \right) = \v{p} \cdot \nabla \v{E}(\v{r})
$$

### Conductors  电导体

In the context of classical electrodynamics, conductors are treated as materials having an **infinite supply of free charges**. Here, free charges refer to electrons or ions that are free to move when subject to an electric field. 

> [!definition] Stable State of Conductors
> Consider a conductor placed in a steady electric field. The conductor is in a **stable state** if the **free charges** inside the conductor are no longer moving, or in **equilibrium**.

For a perfect conductor in a **stable state** (i.e., supporting an electrostatic field), the following properties apply:

+ $\v{E} = \v{0}$ everywhere **inside** the conductor,
+ $\rho = 0$ everywhere **inside** the conductor,
+ All net charge resides **on the surface**,
+ The whole conductor must be an **equipotential**, meaning $V = \text{constant}$ everywhere inside the conductor, and
+ The electric field outside the conductor is **perpendicular** to the surface.

### Dielectrics  电介质


## Solving Electrostatic Problems  解静电问题

### The Uniqueness Theorem  唯一性定理

> [!theorem] Lemma: Green's First Identity
> For any **two scalar fields $\phi$ and $\psi$** that are twice continuously differentiable in a region $\varOmega$, **Green's first identity** states that
> $$ \int_{\varOmega} \left( \phi \nabla^2 \psi + \nabla \phi \cdot \nabla \psi \right) \dif V = \oint_{\partial \varOmega} \phi \dfrac{\partial \psi}{\partial \vu{n}} \dif a$$
> where $\vu{n}$ is the outward unit normal vector of the boundary $\partial \varOmega$.
> > [!note]- Proof
> > Let $\v{F} = \phi \nabla \psi$, then $\nabla \cdot \v{F} = \nabla \phi \cdot \nabla \psi + \phi \nabla^2 \psi$. By [[Math Basement#Gauss' Theorem|the divergence theorem]], the left-hand side of the equation equals the right-hand side.

^055d9b

We can use **Green's first identity** to prove that the solution of the **Poisson's equation** is unique.

Assume that $\phi_1$ and $\phi_2$ are two solutions of the Poisson's equation $\begin{cases}\nabla^2 \phi = - \dfrac{\rho}{\varepsilon_{0}} \\ \phi \Big|_{\partial \varOmega} = f \text{ or } \left.\dfrac{\partial \phi}{\partial \vu{n}}\right|_{\partial\varOmega} = g\end{cases}$. Then, the difference $\varPhi = \phi_1 - \phi_2$ satisfies the **homogeneous** Laplace's equation $\nabla^2 \varPhi = 0$ with the **homogeneous** boundary conditions $\varPhi \Big|_{\partial \varOmega} = 0$ or $\left.\dfrac{\partial \varPhi}{\partial \vu{n}}\right|_{\partial\varOmega} = 0$.

Put $\phi = \varPhi$ and $\psi = \varPhi$ into **[[#^055d9b|Green's First Identity]]**, we have
$$
\int_{\varOmega} ( \varPhi \underbrace{\nabla^2 \varPhi}_{0} + \nabla \varPhi \cdot \nabla \varPhi ) \dif V = \oint_{\partial \varOmega} \underbrace{\varPhi \dfrac{\partial \varPhi}{\partial \vu{n}}}_{0} \dif a
\quad \Longrightarrow \quad \int_{\varOmega} \left\| \nabla \varPhi \right\|^2 \dif V \equiv 0
$$
So we have $\nabla \varPhi = \v{0}$ everywhere in $\varOmega$, which means $\varPhi = \text{constant}$, and $\varPhi \Big|_{\partial \varOmega} = 0$ implies $\varPhi = 0$ everywhere in $\varOmega$. Therefore, $\phi_1 = \phi_2$, so **the solution of the Poisson's equation is unique**.

> [!theorem] Uniqueness Theorem
> The solution of the Poisson's equation $\nabla^2 \phi = \dfrac{\rho}{\varepsilon_{0}}$ with region $\varOmega$ is **unique** under the given boundary conditions of the following form:
> + **Dirichlet**: $\phi \Big|_{\partial \varOmega}$ is given,
> + **Neumann**: $\left.\dfrac{\partial \phi}{\partial \vu{n}}\right|_{\partial\varOmega}$ is given, or
> + **Robin**: $\alpha \phi + \beta \left.\dfrac{\partial \phi}{\partial \vu{n}}\right|_{\partial\varOmega}$ is given.

Uniqueness theorem is a powerful tool in solving electrostatic problems, especially when the boundary conditions are given. It guarantees that ***if A SOLUTION is found, then THE SOLUTION is it***.

### The Method of Images  镜像法

The **method of images** is a powerful technique based on [[#The Uniqueness Theorem 唯一性定理|the uniqueness theorem]] to solve electrostatic problems with **boundary conditions**. 

> [!example]
> 
