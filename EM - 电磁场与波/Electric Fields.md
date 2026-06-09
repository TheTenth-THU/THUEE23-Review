## Coulomb's Law, 库仑定律

The **electric force** between two point charges is given by **Coulomb's Law**:

> [!theorem] Coulomb's Law 
> Let $q_1$ and $q_2$ be two point charges positioned at $\v{r}_1$ and $\v{r}_2$ respectively, and denote the separation vector as $\vsr{r} = \v{r}_2 - \v{r}_1$. **The electric force $\v{F}$ on $q_2$** due to $q_1$ is given by
> $$
> \v{F}(\v{r}_{2};\v{r}_{1}) = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{\mathscr{r}^2} \vu{\mathscr{r}}
> $$
> where $\varepsilon_0$ is the **vacuum permittivity**.

### Electric Field of a Point Charge, 点电荷的电场

If we denote $q$ as the **source charge** that placed at $\v{r}'$, and $Q$ as the **test charge** that placed at $\v{r}$, then according to **[[#Coulomb's Law, 库仑定律]]**, we have
$$
\v{F}(\v{r};\v{r}') = \dfrac{1}{4\pi\varepsilon_0} \dfrac{qQ}{\mathscr{r}^2} \vu{\mathscr{r}} = \left( \dfrac{q}{4\pi\varepsilon_{0}\mathscr{r}^2} \vu{\mathscr{r}} \right)Q
$$
The quantity in the parentheses is defined as the **electric field $\v{E}$** at $\v{r}$ due to the point charge $q$ at $\v{r}'$, since it is not dependent on the test charge $Q$.

> [!definition] Electric Field of a Point Charge
> The **electric field $\v{E}$** at a point $\v{r}$ due to a point charge $q$ located at $\v{r}'$ is given by 
> $$
> \v{E}(\v{r};\v{r}') = \dfrac{q}{4\pi\varepsilon_{0}\mathscr{r}^2} \vu{\mathscr{r}}
> $$
> where $\v{\mathscr{r}} = \v{r} - \v{r}'$, and $\varepsilon_{0}$ is the vacuum permittivity.

^5995df

Immediately we have: 
$$
\nabla \cdot \v{E}(\v{r};\v{r}') = \nabla \cdot \left( \dfrac{q}{4\pi\varepsilon_{0}\mathscr{r}^2} \vu{\mathscr{r}} \right) = \dfrac{q}{4\pi\varepsilon_{0}} \nabla \cdot \left( \dfrac{\vu{\mathscr{r}}}{\mathscr{r}^2} \right) = \dfrac{q}{\varepsilon_{0}} \delta^{3}(\v{\mathscr{r}})
$$
^d57c08

### Superposition Principle  叠加原理

Generally, the electric field at a point $\v{r}$ due to a collection of point charges $q_{i}$ at positions $\v{r}_{i}$ is given by the the electric field $\v{E}$ due to each charge, and **the total electric field is the sum of these fields**.
$$
\v{E}(\v{r}) = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}^2} \vu{\mathscr{r}_{i}}
$$

As calculated in [[#^d57c08]], for a collection of point charges, the divergence of the electric field is given by
$$
\nabla \cdot \v{E}(\v{r}) = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}} \nabla\cdot \left( \dfrac{\vu{\mathscr{r}_{i}}}{\mathscr{r}_{i}^2} \right) = \dfrac{1}{\varepsilon_{0}} \sum\limits_{i} q_{i} \delta^{3}(\v{\mathscr{r}_{i}})
$$

For continuous charge distributions, the electric field can be calculated by integrating the electric field due to each infinitesimal charge element.

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

> [!example] Electric dipole and dipole moment
> Consider a pair of point charges $q$ and $-q$ separated by a distance $d$, the electric **potential** at a point $\v{r}$ **far away** from the dipole is given by
> $$
> V(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \left( \dfrac{q}{\mathscr{r}_{+}} - \dfrac{q}{\mathscr{r}_{-}} \right) = \dfrac{q}{4\pi\varepsilon_{0}} \dfrac{d}{\mathscr{r}^2} \cos \theta
> $$
> here the 2nd equality is due to the fact that
> $$
> \dfrac{1}{\mathscr{r}_{+}} = \dfrac{1}{\mathscr{r}} \left( 1 - \dfrac{d}{2\mathscr{r}} \cos \theta \right)^{-1} \approx \dfrac{1}{\mathscr{r}} \left( 1 + \dfrac{d}{2\mathscr{r}} \cos \theta \right)
> $$
> and $\dfrac{1}{\mathscr{r}_{-}}$ is similar, where $\theta$ is the angle between $\v{r}$ and the dipole axis.
> 
> > [!definition]+ Electric dipole moment
> > The **electric dipole moment $\v{p}$** of a pair of point charges $q$ and $-q$ separated by a distance $d$ is defined as
> > $$\v{p} = q\v{d}$$
> > where $\v{d}$ is the separation vector from $-q$ to $q$.
> 
> So the electric potential can be written as 
> $$V(\v{r}) = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\v{p} \cdot \vu{\mathscr{r}}}{\mathscr{r}^2}$$
> 
> For more conclusions about electric dipole, please refer to [[Electrostatics#Electric Dipole, 电偶极子]].

## Gauss's Law for E Field  电场高斯定理

According to **[[Math Basement#Gauss' Theorem|Gauss' Theorem]]**, denote $S$ a **closed surface** enclosing a volume $V$, we have
$$
\oint_{S} \v{E}(\v{r}) \cdot \dif \v{a} = \int_{V} \nabla \cdot \v{E}(\v{r}) \dif \tau = \dfrac{1}{\varepsilon_{0}} \int_{V} \sum\limits_{i} q_{i} \delta^{3}(\v{\mathscr{r}_{i}}) \dif \tau = \dfrac{1}{\varepsilon_{0}} \sum\limits_{i} q_{i} = \dfrac{Q_{\text{enc}}}{\varepsilon_{0}}
$$
where $Q_{\text{enc}}$ is the total charge enclosed by the surface $S$.

> [!theorem] Gauss's Law (integral form)
> Integration of the electric field $\v{E}$ over a closed surface $S$, or **the total electric flux through $S$**, is given by
> $$
> \oint_{S} \v{E}(\v{r}) \cdot \dif \v{a} = \dfrac{Q_{\text{enc}}}{\varepsilon_{0}}
> $$
> where $Q_{\text{enc}}$ is the total charge enclosed by the surface $S$.

^b02b31

Consider the divergence of the electric field, according to $\dif \v{E} = \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\rho(\v{r}') \dif \tau'}{\mathscr{r}^2} \vu{\mathscr{r}}$ we have
$$
\begin{align}
\nabla \cdot \v{E}(\v{r}) &= \nabla \cdot \left( \dfrac{1}{4\pi\varepsilon_{0}} \int_{V} \dfrac{\rho(\v{r}') \dif \tau'}{\mathscr{r}^2} \vu{\mathscr{r}} \right) = \dfrac{1}{4\pi\varepsilon_{0}} \int_{V} \nabla \cdot \left( \dfrac{\vu{\mathscr{r}}}{\mathscr{r}^2} \right) \rho(\v{r}') \dif \tau' \\
&= \dfrac{1}{\varepsilon_{0}} \int_{V} \rho(\v{r}') \delta^{3}(\v{\mathscr{r}}) \dif \tau' = \dfrac{\rho(\v{r})}{\varepsilon_{0}}
\end{align}
$$
here the 2nd equality is due to the fact that the nabla operator is operating on $\v{r}$, and the integral is over $\v{r}'$.

> [!theorem] Gauss's Law (differential form)
> The **divergence** of the electric field $\v{E}$ at a point $\v{r}$ is given by
> $$
> \nabla \cdot \v{E}(\v{r}) = \dfrac{\rho(\v{r})}{\varepsilon_{0}}
> $$
> where $\rho(\v{r})$ is the charge density at $\v{r}$.

^802761

**Gauss's Law** states that **the total electric flux** through a closed surface is equal to **the total charge** enclosed by the surface, divided by the vacuum permittivity.

## Circuital Law for Static $\boldsymbol{E}$ Field  静电场的环路定理

For a **closed path** $\varGamma$, which can be considered as from $\v{r}_{1}$ to $\v{r}_{1}$, we have
$$
\oint_{\varGamma} \v{E}(\v{r}) \cdot \dif \v{l} = V(\v{r}_{1}) - V(\v{r}_{1}) = 0
$$

> [!theorem] Circuital Law for Static $\v{E}$ Field (integral form)
> The line integral of the electric field $\v{E}$ along a closed path $\varGamma$ is zero, i.e.
> $$
> \oint_{\varGamma} \v{E}(\v{r}) \cdot \dif \v{l} = 0
> $$

According to **[[Math Basement#Stokes' Theorem|Stokes' Theorem]]**, denote $\varGamma$ a **closed path** enclosing a surface $A$, we have
$$
\oint_{\varGamma} \v{E}(\v{r}) \cdot \dif \v{l} = \int_{A} \nabla \times \v{E}(\v{r}) \cdot \dif \v{a} = 0
$$
Since the path $\varGamma$ is arbitrary, we have

> [!theorem] Circuital Law for Static $\v{E}$ Field (differential form)
> The curl of the electric field $\v{E}$ is zero vector, i.e.
> $$
> \nabla \times \v{E}(\v{r}) = \v{0}
> $$

