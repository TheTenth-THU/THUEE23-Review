## Preparatory Concepts, 准备概念

### Wave Impedance, 波阻抗

For a plane wave in a **source-free, homogeneous medium**, we have $\v{E} \perp \v{B} \perp \v{k}$, and
$$
\cpq{B} = \dfrac{\cpq{E}}{v} = \dfrac{n\cpq{E}}{c}, \qquad
\cpq{H} = \dfrac{\cpq{B}}{\mu} = \dfrac{n\cpq{E}}{\mu c}
$$
This leads to the **ratio of electric to magnetic field magnitudes**, defined as the **wave impedance, 波阻抗**.

> [!definition] Wave Impedance
> The **wave impedance, 波阻抗**, is defined as the ratio of the **electric field** to the **magnetic field** in a plane wave within a dielectric medium, i.e.
> $$ \eta = \dfrac{E}{H} = \dfrac{\mu c}{n} = \sqrt{ \dfrac{\mu}{\varepsilon} } $$
> where $\mu = \mu_{0}\mu_{\mathrm{r}}$ is the **magnetic permeability, 磁导率**, $\varepsilon = \varepsilon_{0}\varepsilon_{\mathrm{r}}$ is the **electric permittivity, 电容率**, and $n = \sqrt{ \mu_{\mathrm{r}} \varepsilon_{\mathrm{r}} }$ is the **refractive index, 折射率**. 
>
> For free space, we have 
> $$ \eta_{0} = \sqrt{ \dfrac{\mu_{0}}{\varepsilon_{0}} } = \mu_{0} c = 377 \rmu{\Omega} $$
> 
> The **unit** of wave impedance is $\mathrm{\Omega}$.

The relationship between the **wave impedance** and the **refractive index** can be derived as
$$
\eta = \dfrac{1}{n} \cdot \mu_{\mathrm{r}} \sqrt{ \dfrac{\mu_{0}}{\varepsilon_{0}} } 
$$
For two **non-magnetic ($\mu_{\mathrm{r}} = 1$) and non-absorbing** media, the ratio of their impedances is
$$
\dfrac{\eta_{1}}{\eta_{2}} = \sqrt{ \dfrac{\varepsilon_{2}}{\varepsilon_{1}} } = \dfrac{n_{2}}{n_{1}}
$$

### Standing Wave, 驻波

Assume two plane waves with the **same frequency** and **wavelength** propagate in **opposite directions** along the $z$-axis, i.e.
$$
\cpq{u}_{1} = \cpq{A} \e^{\I(k z - \omega t)}, \qquad
\cpq{u}_{2} = \cpq{A} \e^{\I(-k z - \omega t)}
$$
The **superposition** of these two waves yields
$$
\cpq{u} = \cpq{u}_{1} + \cpq{u}_{2} = \cpq{A} \e^{-\I \omega t} \left( \e^{\I k z} + \e^{-\I k z} \right) = 2\cpq{A} \e^{-\I \omega t} \cos(k z)
$$
Since the notation $\cpq{A} = A \e^{\I \phi_{0}}$, we have
$$
\mathfrak{Re}\{ \cpq{u} \} = 2 A \cos(k z) \cos(\omega t + \phi_{0})
$$
which is a **standing wave, 驻波**, with
+ **spatial oscillation, 空间振荡**, as $\cos(kz)$, 
+ **temporal oscillation, 时间振荡**, as $\cos(\omega t + \phi_{0})$,
+ **nodes, 节点**, at $z = \dfrac{(2n+1)\lambda}{4}$ where $n$ is an integer, and
+ **antinodes, 腹点**, at $z = n\lambda$ where $n$ is an integer.

## Reflection \& Transmission at Planar Boundaries, 平面边界的反射与折射

### Snell's Law, 斯涅尔定律

Assume an electromagnetic **plane wave** travels from one medium (denoted as 1) to another (denoted as 2). Build the $z$-axis **along the boundary normal, 沿边界法线**, and the $x$-axis **along the boundary** to contain the incident wave vector $\v{k}_{\mathrm{i}}$ within the $xOz$-plane, called the **plane of incidence, 入射面**. 

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}

\begin{document}
\large
\begin{tikzpicture}[decoration={
	markings, 
	mark=at position 0.5 with {\arrow{latex}} 
}]
	\draw[fill=gray, opacity=0.3, draw=none] (-3,-3) rectangle (3,0);
	\draw[thick, ->] (0,-3) -- (0,3) node[above] {$z$};
	\draw[thick, ->] (-3,0) -- (3,0) node[right] {$x$};
	\draw[thick, postaction={decorate}] (0,0) +(-150:4) -- +(0,0) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{i}}$};
	\draw[thick, postaction={decorate}, blue!50!white] (0,0) +(0,0) -- +(-30:4) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{r}}$};
	\draw[thick, postaction={decorate}, purple!50!white] (0,0) +(0,0) -- +(50:4) node[right, midway] {$\vec{\boldsymbol{k}}_{\mathrm{t}}$};
	\draw[thick, -latex] (0,0) +(-90:0.7) arc (-90:-150:0.7) node[below, midway] {$\theta_{\mathrm{i}}$};
	\draw[thick, -latex, blue!50!white] (0,0) +(-90:1) arc (-90:-30:1) node[below, midway] {$\theta_{\mathrm{r}}$};
	\draw[thick, -latex, purple!50!white] (0,0) +(90:1) arc (90:50:1) node[above, midway] {$\theta_{\mathrm{t}}$};
\end{tikzpicture}
\end{document}
```

The waves can be expressed in the most general form as
$$
\begin{align}
\cpq{\v{E}}_{\mathrm{i}} &= \cpq{\v{E}}_{0\mathrm{i}} \e^{\I(\v{k}_{\mathrm{i}} \cdot \v{r} - \omega_{\mathrm{i}} t)} = \cpq{\v{E}}_{0\mathrm{i}} \e^{\I(k_{\mathrm{i}x} x + k_{\mathrm{i}z} z - \omega_{\mathrm{i}} t)} \\
\cpq{\v{E}}_{\mathrm{r}} &= \cpq{\v{E}}_{0\mathrm{r}} \e^{\I(\v{k}_{\mathrm{r}} \cdot \v{r} - \omega_{\mathrm{r}} t)} = \cpq{\v{E}}_{0\mathrm{r}} \e^{\I(k_{\mathrm{r}x} x + k_{\mathrm{r}y} y + k_{\mathrm{r}z} z - \omega_{\mathrm{r}} t)} \\
\cpq{\v{E}}_{\mathrm{t}} &= \cpq{\v{E}}_{0\mathrm{t}} \e^{\I(\v{k}_{\mathrm{t}} \cdot \v{r} - \omega_{\mathrm{t}} t)} = \cpq{\v{E}}_{0\mathrm{t}} \e^{\I(k_{\mathrm{t}x} x + k_{\mathrm{ty}} y + k_{\mathrm{tz}} z - \omega_{\mathrm{t}} t)}
\end{align}
$$
According to the [[Electric Displacement#Electric Boundary Conditions, 电边界条件|electric boundary conditions]], we have the **tangential components** at the boundary $z=0$ as
$$
\cpq{\v{E}}_{\mathrm{i}, \parallel} (z=0) + \cpq{\v{E}}_{\mathrm{r}, \parallel} (z=0) = \cpq{\v{E}}_{\mathrm{t}, \parallel} (z=0)
$$
so **the exponential factors** of all waves must **match** in both space and time, i.e.
$$
k_{\mathrm{i}x} = k_{\mathrm{r}x} = k_{\mathrm{t}x}, \qquad
k_{\mathrm{r}y} = k_{\mathrm{t}y} = 0, \qquad
\omega_{\mathrm{i}} = \omega_{\mathrm{r}} = \omega_{\mathrm{t}}
$$

Since $k = \dfrac{n\omega}{c} = nk_{0}$, The $x$-components of the wave vectors can be expanded as
$$
n_{1}k_{0} \sin \theta_{\mathrm{i}} = n_{1}k_{0} \sin \theta_{\mathrm{r}} = n_{2}k_{0} \sin \theta_{\mathrm{t}}
$$

> [!theorem] Law of Refraction
> + The reflection wave has **the same frequency** as the incident wave, 反射波与入射波的**频率相同**,
> + The reflection wave lies **in the same plane** as the incident wave and the normal to the boundary, 反射波与入射波及边界法线**在同一平面内**, and
> + The **reflection angle** is equal to the **incident angle**, 反射角等于入射角, i.e.
> $$ \theta_{\mathrm{r}} = \theta_{\mathrm{i}} $$

> [!theorem] Law of Transmission (Snell's Law)
> + The transmission wave has **the same frequency** as the incident wave, 折射波与入射波的**频率相同**,
> + The reflection wave lies **in the same plane** as the incident wave and the normal to the boundary, 折射波与入射波及边界法线**在同一平面内**, and
> + The **transmission angle** $\theta_{\mathrm{t}}$ is related to the **incident angle** $\theta_{\mathrm{i}}$ by
> $$ n_{1} \sin \theta_{\mathrm{i}} = n_{2} \sin \theta_{\mathrm{t}} $$
> where $n_{1}$ and $n_{2}$ are the **refractive indices** of the two media.

### Fresnel's Equations, 菲涅耳方程

The **Fresnel equations** describe how the **complex amplitudes** $\cpq{E}_{0}$ and $\cpq{H}_{0}$ bahaves in the **reflection and transmission of electromagnetic waves** at the interface between two media with different refractive indices. 

Since $\v{k} \perp \v{E} \perp \v{H}$, we can divide $\v{E}$ and $\v{H}$ into **tangential** and **normal** components each, i.e. decompose the wave into **two orthogonally polarized components**:
+ **S-polarized wave, S 偏振波**, with the electric field $\v{E}$ **perpendicular** (_senkrecht_ in German) to the plane of incidence, and
+ **P-polarized wave, P 偏振波**, with the electric field $\v{E}$ **parallel** to the plane of incidence.

#### S-Polarization, S 偏振

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}

\begin{document}
\large
\begin{tikzpicture}[decoration={
	markings, 
	mark=at position 0.5 with {\arrow{latex}} 
}]
	\draw[fill=gray, opacity=0.3, draw=none] (-3,-3) rectangle (3,0);
	\draw[thick, ->] (0,-3) -- (0,3) node[above] {$z$};
	\draw[thick, ->] (-3,0) -- (3,0) node[right] {$x$};
	// k
	\draw[thick, postaction={decorate}] (0,0) +(-150:4) -- +(0,0) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{i}}$};
	\draw[thick, postaction={decorate}] (0,0) +(0,0) -- +(-30:4) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{r}}$};
	\draw[thick, postaction={decorate}] (0,0) +(0,0) -- +(50:4) node[right, midway] {$\vec{\boldsymbol{k}}_{\mathrm{t}}$};
	// E \& H
	\draw[thick, -latex, purple!50!white] (-150:3) node {\LARGE$\boldsymbol{\otimes}$} 
	node[below=5pt] {$\vec{\boldsymbol{E}}_{\mathrm{i}}$}
	[blue!50!white]	-- +(120:1) 
	node[left] {$\vec{\boldsymbol{H}}_{\mathrm{i}}$};
	\draw[thick, -latex, purple!50!white] (-30:3) node {\LARGE$\boldsymbol{\otimes}$} 
	node[below=5pt] {$\vec{\boldsymbol{E}}_{\mathrm{r}}$}
	[blue!50!white]	-- +(60:1) 
	node[right] {$\vec{\boldsymbol{H}}_{\mathrm{r}}$};
	\draw[thick, -latex, purple!50!white] (50:3.5) node {\LARGE$\boldsymbol{\otimes}$} 
	node[right=5pt] {$\vec{\boldsymbol{E}}_{\mathrm{t}}$}
	[blue!50!white]	-- +(140:1) 
	node[left] {$\vec{\boldsymbol{H}}_{\mathrm{t}}$};
	// theta
	\draw[thick, -latex] (0,0) +(-90:0.7) arc (-90:-150:0.7) node[below, midway] {$\theta_{\mathrm{i}}$};
	\draw[thick, -latex] (0,0) +(-90:1) arc (-90:-30:1) node[below, midway] {$\theta_{\mathrm{r}}$};
	\draw[thick, -latex] (0,0) +(90:1) arc (90:50:1) node[above, midway] {$\theta_{\mathrm{t}}$};
\end{tikzpicture}
\end{document}
```

According to the [[Electric Displacement#Electric Boundary Conditions, 电边界条件|electric boundary conditions]], the **tangential components** of the electric fields at the boundary $z=0$ are
$$
\cpq{E}_{0\mathrm{i}} + \cpq{E}_{0\mathrm{r}} = \cpq{E}_{0\mathrm{t}}
\tag{S1}
$$
And according to the [[Magnetic Auxiliary Field H#Magnetic Boundary Conditions, 磁边界条件|magnetic boundary conditions]], the **tangential components** of the magnetic fields at the boundary $z=0$ are
$$
- \cpq{H}_{0\mathrm{i}} \cos \theta_{\mathrm{i}} + \cpq{H}_{0\mathrm{r}} \cos \theta_{\mathrm{r}} = - \cpq{H}_{0\mathrm{t}} \cos \theta_{\mathrm{t}}
$$
Substituting $\cpq{H} = \dfrac{\cpq{E}}{\eta} = \dfrac{n\cpq{E}}{\eta_{0}}$, we have
$$
- n_{1} \cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{i}} + n_{1} \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{r}} = - n_{2} \cpq{E}_{0\mathrm{t}} \cos \theta_{\mathrm{t}}
\tag{S2}
$$
Then we can put (S1) into (S2) and get
$$
-n_{1} \cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{i}} + n_{2} \cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{t}} = - n_{1} \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{r}} - n_{2} \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{t}} 
$$

> [!theorem] Fresnel's Equations for S-Polarization
> For the **S-polarized component** of the electromagnetic wave, the **amplitude reflection coefficient, 反射振幅系数**, is given by
> $$ \cpq{r}_{\mathrm{S}} = \dfrac{\cpq{E}_{0\mathrm{r}}}{\cpq{E}_{0\mathrm{i}}} = \dfrac{n_{1} \cos \theta_{\mathrm{i}} - n_{2} \cos \theta_{\mathrm{t}}}{n_{1} \cos \theta_{\mathrm{i}} + n_{2} \cos \theta_{\mathrm{t}}} $$

#### P-Polarization, P 偏振

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}

\begin{document}
\large
\begin{tikzpicture}[decoration={
	markings, 
	mark=at position 0.5 with {\arrow{latex}} 
}]
	\draw[fill=gray, opacity=0.3, draw=none] (-3,-3) rectangle (3,0);
	\draw[thick, ->] (0,-3) -- (0,3) node[above] {$z$};
	\draw[thick, ->] (-3,0) -- (3,0) node[right] {$x$};
	// k
	\draw[thick, postaction={decorate}] (0,0) +(-150:4) -- +(0,0) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{i}}$};
	\draw[thick, postaction={decorate}] (0,0) +(0,0) -- +(-30:4) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{r}}$};
	\draw[thick, postaction={decorate}] (0,0) +(0,0) -- +(50:4) node[right, midway] {$\vec{\boldsymbol{k}}_{\mathrm{t}}$};
	// E \& H
	\draw[thick, -latex, blue!50!white] (-150:3) node {\LARGE$\boldsymbol{\odot}$} 
	node[below=5pt] {$\vec{\boldsymbol{H}}_{\mathrm{i}}$}
	[purple!50!white]	-- +(120:1) 
	node[left] {$\vec{\boldsymbol{E}}_{\mathrm{i}}$};
	\draw[thick, -latex, blue!50!white] (-30:3) node {\LARGE$\boldsymbol{\odot}$} 
	node[below=5pt] {$\vec{\boldsymbol{H}}_{\mathrm{r}}$}
	[purple!50!white]	-- +(60:1) 
	node[right] {$\vec{\boldsymbol{E}}_{\mathrm{r}}$};
	\draw[thick, -latex, blue!50!white] (50:3.5) node {\LARGE$\boldsymbol{\odot}$} 
	node[right=5pt] {$\vec{\boldsymbol{H}}_{\mathrm{t}}$}
	[purple!50!white]	-- +(140:1) 
	node[left] {$\vec{\boldsymbol{E}}_{\mathrm{t}}$};
	// theta
	\draw[thick, -latex] (0,0) +(-90:0.7) arc (-90:-150:0.7) node[below, midway] {$\theta_{\mathrm{i}}$};
	\draw[thick, -latex] (0,0) +(-90:1) arc (-90:-30:1) node[below, midway] {$\theta_{\mathrm{r}}$};
	\draw[thick, -latex] (0,0) +(90:1) arc (90:50:1) node[above, midway] {$\theta_{\mathrm{t}}$};
\end{tikzpicture}
\end{document}
```

According to the [[Electric Displacement#Electric Boundary Conditions, 电边界条件|electric boundary conditions]], the **tangential components** of the electric fields at the boundary $z=0$ are
$$
-\cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{i}} + \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{r}} = -\cpq{E}_{0\mathrm{t}} \cos \theta_{\mathrm{t}}
\tag{P1}
$$
And according to the [[Magnetic Auxiliary Field H#Magnetic Boundary Conditions, 磁边界条件|magnetic boundary conditions]], the **tangential components** of the magnetic fields at the boundary $z=0$ are
$$
\cpq{H}_{0\mathrm{i}} + \cpq{H}_{0\mathrm{r}} = \cpq{H}_{0\mathrm{t}}
$$
i.e.
$$
n_{1} \cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{t}} + n_{1} \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{t}} = n_{2} \cpq{E}_{0\mathrm{t}} \cos \theta_{\mathrm{t}}
\tag{P2}
$$
Then we can put (P2) into (P1) and get
$$
-n_{2} \cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{i}} + n_{1} \cpq{E}_{0\mathrm{i}} \cos \theta_{\mathrm{t}} = -n_{2} \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{r}} - n_{1} \cpq{E}_{0\mathrm{r}} \cos \theta_{\mathrm{t}}
$$

> [!theorem] Fresnel's Equations for P-Polarization
> For the **P-polarized component** of the electromagnetic wave, the **amplitude reflection coefficient, 反射振幅系数**, is given by
> $$ \cpq{r}_{\mathrm{P}} = \dfrac{\cpq{E}_{0\mathrm{r}}}{\cpq{E}_{0\mathrm{i}}} = \dfrac{n_{2} \cos \theta_{\mathrm{i}} - n_{1} \cos \theta_{\mathrm{t}}}{n_{2} \cos \theta_{\mathrm{i}} + n_{1} \cos \theta_{\mathrm{t}}} $$

#### Brewster's Angle, 布鲁斯特角

The **Brewster's angle** $\theta_{\mathrm{B}}$ is defined as the angle of incidence at which the reflected light is **completely polarized perpendicular** to the plane of incidence, i.e. $\cpq{r}_{\mathrm{P}} = 0$. This occurs when
$$
n_{2} \cos \theta_{\mathrm{B}} = n_{1} \cos \theta_{\mathrm{t}}\Big|_{\theta_{\mathrm{i}} = \theta_{\mathrm{B}}}
$$
Applying the **Snell's Law**, we have
+ $\theta_{\mathrm{B}}$ and $\theta_{\mathrm{t}} \Big|_{\theta_{\mathrm{i}} = \theta_{\mathrm{B}}}$ are **complementary angles**, i.e. $\theta_{\mathrm{t}} + \theta_{\mathrm{B}} = \pi/2$, and
+ The value of the Brewster's angle is
$$
\theta_{\mathrm{B}} = \arctan \left( \dfrac{n_{2}}{n_{1}} \right)
$$

### Total Internal Reflection, 全反射 

The **total (internal) reflection** occurs when the refractive index of the second medium is **lower** than that of the first medium, i.e. $n_{2} < n_{1}$, and the incident angle $\theta_{\mathrm{i}}$ exceeds the **critical angle**, defined as
$$
\theta_{\mathrm{c}} = \arcsin \left( \dfrac{n_{2}}{n_{1}} \right)
$$

For $\theta_{\mathrm{i}} > \theta_{\mathrm{c}}$, the **[[#Snell's Law, 斯涅尔定律]]** predicts $\sin\theta_{\mathrm{t}} > 1$, therefore 
+ The transmission angle $\theta_{\mathrm{t}}$ becomes **imaginary**, and
+ $k_{\mathrm{t}x} = n_{2} k_{0} \sin \theta_{\mathrm{t}} > n_{2} k_{0} = k_{\mathrm{t}}$, and $k_{\mathrm{t}z} = \sqrt{ k_{2}^2 - k_{\mathrm{t}x}^2 }$ becomes **imaginary** as well, leading to an **exponentially decaying wave** in the second medium as
$$ \cpq{\v{E}}_{\mathrm{t}} = \cpq{\v{E}}_{0\mathrm{t}} \e^{\I(k_{\mathrm{t}x} x + k_{\mathrm{tz}} z - \omega t)} = \cpq{\v{E}}_{0\mathrm{t}} \e^{|k_{\mathrm{t}z}|z} \e^{\I(k_{\mathrm{t}x}x-\omega t)} $$

This means that the wave does not transmit into the second medium, but instead reflects back into the first medium.

The **amplitude reflection coefficient, 反射振幅系数**, for both S- and P-polarized waves **approaches 1** as $\theta_{\mathrm{i}}$ approaches $\theta_{\mathrm{c}}$. Then, the **phase, 相位** of the coefficient $\cpq{r}$ changes **from $0$ to $-\pi$** as $\theta_{\mathrm{i}}$ goes from $\theta_{\mathrm{c}}$ to $\pi/2$.

![[Pasted image 20250612133358.png]]

### Energy Conservation in Reflection and Transmission, 反射与折射中的能量守恒

Consider the following field configuration, in which:
+ An **S-polarized wave** is incident from medium 1 to medium 2, with the **incidence angle** $\theta_{\mathrm{i}}$,
+ Medium 1 ($n_{1}$) is an **optically denser medium** than medium 2 ($n_{2}$), i.e. $n_{1} > n_{2}$.

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{decorations.markings}

\begin{document}
\large
\begin{tikzpicture}[decoration={
	markings, 
	mark=at position 0.5 with {\arrow{latex}} 
}]
	\draw[fill=gray, opacity=0.3, draw=none] (-3,-3) rectangle (3,0);
	\draw[thick, ->] (0,-3) -- (0,3) node[above] {$z$};
	\draw[thick, ->] (-3,0) -- (3,0) node[right] {$x$};
	// k
	\draw[thick, postaction={decorate}] (0,0) +(-150:4) -- +(0,0) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{i}}$};
	\draw[thick, postaction={decorate}] (0,0) +(0,0) -- +(-30:4) node[below, midway] {$\vec{\boldsymbol{k}}_{\mathrm{r}}$};
	\draw[thick, postaction={decorate}] (0,0) +(0,0) -- +(20:4) node[above, midway] {$\vec{\boldsymbol{k}}_{\mathrm{t}}$};
	// E \& H
	\draw[thick, -latex, purple!50!white] (-150:3) node {\LARGE$\boldsymbol{\otimes}$} 
	node[below=5pt] {$\vec{\boldsymbol{E}}_{\mathrm{i}}$}
	[blue!50!white]	-- +(120:1) 
	node[left] {$\vec{\boldsymbol{H}}_{\mathrm{i}}$};
	\draw[thick, -latex, purple!50!white] (-30:3) node {\LARGE$\boldsymbol{\otimes}$} 
	node[below=5pt] {$\vec{\boldsymbol{E}}_{\mathrm{r}}$}
	[blue!50!white]	-- +(60:1) 
	node[right] {$\vec{\boldsymbol{H}}_{\mathrm{r}}$};
	\draw[thick, -latex, purple!50!white] (20:3.5) node {\LARGE$\boldsymbol{\otimes}$} 
	node[below=5pt] {$\vec{\boldsymbol{E}}_{\mathrm{t}}$}
	[blue!50!white]	-- +(110:1) 
	node[left] {$\vec{\boldsymbol{H}}_{\mathrm{t}}$};
	// theta
	\draw[thick, -latex] (0,0) +(-90:0.7) arc (-90:-150:0.7) node[below, midway] {$\theta_{\mathrm{i}}$};
	\draw[thick, -latex] (0,0) +(-90:1) arc (-90:-30:1) node[below, midway] {$\theta_{\mathrm{r}}$};
	\draw[thick, -latex] (0,0) +(90:1) arc (90:20:1) node[above, midway] {$\theta_{\mathrm{t}}$};
\end{tikzpicture}
\end{document}
```

#### Partial Reflection Case, 部分反射情形

For $\theta_{\mathrm{i}} < \theta_{\mathrm{c}}$, the reflected and incident waves are **in phase, 同相**, and according to the boundary conditions, 
$$
\cpq{E}_{0\mathrm{i}} + \cpq{E}_{0\mathrm{r}} = \cpq{E}_{0\mathrm{t}}
$$

The **time-averaged Poynting vector, 平均坡印亭矢量**, is $\left\langle \v{S} \right\rangle \propto nE^{2}$. The **normal components** of the Poynting vectors in the two media are
$$
\begin{align}
\left\langle S_{z}^{(1)} \right\rangle &= \left\langle \left\lVert \v{E}_{\mathrm{i}} \times \v{H}_{\mathrm{i}x} \right\rVert \right\rangle + \left\langle \left\lVert \v{E}_{\mathrm{r}} \times \v{H}_{\mathrm{r}x} \right\rVert \right\rangle  \\
&= n_{1} \sqrt{ \dfrac{\varepsilon_{0}}{\mu_{0}} } \left( \left\lvert \cpq{E}_{0\mathrm{i}} \right\rvert^{2} + \left\lvert \cpq{E}_{0\mathrm{r}} \right\rvert^{2} \right) \cos \theta_{\mathrm{i}}  \\
\left\langle S_{z}^{(2)} \right\rangle &= \left\langle \left\lVert \v{E}_{\mathrm{t}} \times \v{H}_{\mathrm{tx}} \right\rVert \right\rangle
= n_{2} \sqrt{ \dfrac{\varepsilon_{0}}{\mu_{0}} } \left\lvert \cpq{E}_{0\mathrm{t}} \right\rvert^{2} \cos \theta_{\mathrm{t}}
\end{align}
$$
Substituting the Fresnel coefficients and simplifying confirms the **energy conservation** $\left\langle S_{z}^{(1)} \right\rangle = \left\langle S_{z}^{(2)} \right\rangle$.

#### Total Reflection Case, 全反射情形

For $\theta_{\mathrm{i}} > \theta_{\mathrm{c}}$, the **transmitted electric field** (S-polarization, which oscillates in the $y$-direction) takes the form
$$
\cpq{E}_{\mathrm{t}} (x, z, t) = \cpq{E}_{0\mathrm{t}} \e^{-|k_{\mathrm{tz}}|z} \e^{\I(k_{\mathrm{tx}} x - \omega t)}
$$
because $k_{\mathrm{tz}} = \I |k_{\mathrm{tz}}|$ is imaginary. This indicates that the wave **decays exponentially along the $z$-direction, 沿 $z$ 方向指数衰减**. 

The corresponding **magnetic field components** become
$$
\cpq{H}_{\mathrm{t}x} = \dfrac{\cpq{E}_{\mathrm{t}}}{\eta_{2}} (-\cos\theta_{\mathrm{t}}) = -\dfrac{n_{2} \cpq{E}_{\mathrm{t}}}{\eta_{0}} \dfrac{\I |k_{\mathrm{t}z}|}{k_{\mathrm{t}}},
\qquad
\cpq{H}_{\mathrm{tz}} = \dfrac{\cpq{E}_{\mathrm{t}}}{\eta_{2}} \sin\theta_{\mathrm{t}} = \dfrac{n_{2} \cpq{E}_{\mathrm{t}}}{\eta_{0}} \dfrac{k_{\mathrm{i}}\sin\theta_{\mathrm{i}}}{k_{\mathrm{t}}}
$$
The **normal component** of the Poynting vector in the Medium 2 is
$$
\left\langle S_{z}^{(2)} \right\rangle = \mathfrak{Re}\left\{  \dfrac{1}{2} \cpq{E}_{\mathrm{t}} (-\cpq{H}_{\mathrm{t}x}^{*}) \right\}
= \dfrac{1}{2} \mathfrak{Re} \left\{  -\dfrac{n_{2}}{\eta_{0}} \dfrac{\I|k_{\mathrm{t}z}|}{k_{\mathrm{t}}} |\cpq{E}_{0\mathrm{t}}|^{2} \e^{-2|k_{\mathrm{t}z}|z} \right\}
= 0
$$
Therefore, **NO ENERGY is transmitted into Medium 2**.

![[Pasted image 20250612143925.png]]

## Waveguides, 波导

A **waveguide, 波导**, is a structure that guides electromagnetic waves, typically in the form of **microwave or optical signals**. It consists of a hollow metallic or dielectric structure that confines the wave within its boundaries.

### Fundamental Principle of Waveguides, 波导的基本原理

We know that electromagnetic waves can be [[#Total Internal Reflection, 全反射|totally internally reflected]] at the interface of two media with **no energy loss**, if it is originally propagating in the **denser medium** and the angle of incidence exceeds the **critical angle**.

If we place a second, parallel interface below the first at just the right spacing, letting **each round-trip reflection interfere constructively with the next, 每次往返反射都与下一次干涉相长**, the wave will be **confined** between the two interfaces, forming a **standing wave** propagating along the interface.

![[Pasted image 20250612145108.png]]

### Rectangular Metallic Waveguide, 矩形金属波导 

We idealize the waveguide walls as **perfect electric conductors (PECs), 理想导体**, in which both the **electric field $\v{E}$** and the **magnetic field $\v{H}$** are $\v{0}$, and on the boundaries 
$$
\v{E}_{\parallel} = \v{0}, \qquad
\v{H}_{\perp} = \v{0}
$$

Assume the waveguide walls are at $x=0,a$ and $y=0,b$, and the waveguide extends (wave propagates) along the $z$-direction, i.e. **all fields vary as $\e^{\I(k_{z}z - \omega t)}$.**

#### Electric Boundary Condition at $x$-Walls, 横侧壁面的电边界条件

Assume we have the wave **S-polarized** in the $y$-direction, i.e. $\cpq{\v{E}} = \cpq{E}_{y} \vu{y}$. At the $x=0$ and $x=a$ walls, in order to satisfy the boundary condition $\v{E}_{\parallel} = \v{0}$, the phase of the electric field must **undergo a $\pi$ shift** at each reflection. 

This leads to the **standing wave** condition
$$
E(x) \propto \sin \left( \dfrac{m \pi x}{a} \right), \quad m = 1, 2, \cdots
$$
The sinusoidal variation ensures that the boundary condition is satisfied at the conducting walls, and that the field is self-consistent after multiple reflections inside the waveguide.

#### Electric Boundary Condition at $y$-Walls, 纵侧壁面的电边界条件

It appears that placing two additional metal plates **parallel to the $x-z$ plane**, i.e., at $y=0$ and $y=b$, **does not violate the boundary conditions**, because the electric field $\cpq{\v{E}}$ is perpendicular to the planes of the plates.

To maintain the electric field at the $y$-walls, there should be **charge accumulation** on the plates, satisfying
$$
\sigma = \varepsilon_{0} E
$$

#### Magnetic Boundary Condition, 磁边界条件

The electric field $\cpq{\v{E}}$ satisfying all the above conditions can be expressed as
$$
\cpq{\v{E}}(x, y, z, t) = \cpq{E}_{0} \sin \left( \dfrac{m \pi x}{a} \right) \e^{\I(k_{z}z - \omega t)} \vu{y}
$$
Applying the **Faraday's law of induction** in its time-harmonic form
$$
\nabla \times \cpq{\v{E}} = - \I \omega \mu \cpq{\v{H}}
$$
we can find the magnetic field $\cpq{\v{H}}$ has components $\cpq{H}_{x}$ and $\cpq{H}_{z}$ as spatial derivatives of $\cpq{E}_{y}$:
$$
\begin{align}
\cpq{H}_{x} &= \dfrac{1}{-\I\omega \mu} (-\partial_{z}\cpq{E}_{y}) = \dfrac{1}{\I \omega \mu} \I k_{z} \cpq{E}_{0} \sin \left( \dfrac{m \pi x}{a} \right) \e^{\I(k_{z}z - \omega t)}  \\
&= \dfrac{k_{z}}{\omega \mu} \cpq{E}_{0} \sin \left( \dfrac{m \pi x}{a} \right) \e^{\I(k_{z}z - \omega t)} \\
\cpq{H}_{z} &= \dfrac{1}{-\I\omega \mu} \partial_{x}\cpq{E}_{y} = \dfrac{1}{-\I\omega \mu} \cpq{E}_{0} \dfrac{m \pi}{a} \cos \left( \dfrac{m \pi x}{a} \right) \e^{\I(k_{z}z - \omega t)} \\
&= -\dfrac{m \pi}{\I \omega \mu a} \cpq{E}_{0} \cos \left( \dfrac{m \pi x}{a} \right) \e^{\I(k_{z}z - \omega t)}
\end{align}
$$
Therefore, the **magnetic field** in the waveguide has a **circulating** pattern.

To maintain such a circulating magnetic field, according to the boundary condition $\v{H}_{\parallel} = \v{K} \times \vu{n}$, or expressed as $\v{K} = \vu{n} \times \v{H}_{\parallel}$, the **surface current density** should be in the pattern shown below (for $m=1$).

![[Pasted image 20250612161640.png]]

### Modes of Waveguides, 波导模

We use the **mode number** $(m, n)$ to label the **modes of waveguides**, where $m$ and $n$ are the number of half-wavelengths along the $x$- and $y$-directions, respectively.

#### TE Mode, 横电模

What we have described above is all about **TE mode, 横电模**, where the electric field $\cpq{\v{E}}$ has no component in the direction of propagation, i.e. $\cpq{E}_{z} = 0$. More precisely, the formulas above are discussing the **TE$_{m,0}$ mode**.

The most typical TE$_{m,0}$ mode is the **TE$_{10}$ mode**, which has **one half-wavelength along the $x$-direction** and **no variation along the $y$-direction**. The electric field in a TE$_{10}$ mode is given by
$$
\cpq{\v{E}}(x, y, z, t) = \cpq{E}_{0} \sin \left( \dfrac{\pi x}{a} \right) \e^{\I(\beta z - \omega t)} \vu{y}
$$
where $\beta = k_{z}$ is the **propagation constant** along the $z$-direction.

Since $a > b$ by convention, **TE$_{01}$ mode** has different properties. The electric field in a TE$_{01}$ waveguide is given by
$$
\cpq{\v{E}}(x, y, z, t) = \cpq{E}_{0} \sin \left( \dfrac{\pi y}{b} \right) \e^{\I(\beta z - \omega t)} \vu{x}
$$

Most generally, the electric field in a TE$_{m,n}$ mode is given by
$$
\cpq{\v{E}}(x, y, z, t) = \cpq{E}_{0} \sin \left( \dfrac{m \pi x}{a} \right) \sin \left( \dfrac{n \pi y}{b} \right) \e^{\I(\beta z - \omega t)} \vu{z}
$$

For all cases the **total wavenumber** satisfies 
$$
\v{k}^{2} = k^{2} = k_{x}^{2} + k_{y}^{2} + k_{z}^{2} = \left( \dfrac{\omega}{c} \right)^{2}
$$

#### TM Mode, 横磁模

The **TM mode, 横磁模**, is another type of waveguide mode where the magnetic field $\cpq{\v{H}}$ has no component in the direction of propagation, i.e. $\cpq{H}_{z} = 0$.

Since $E_{z} = 0$ on the walls implies **both $m$ and $n$ must be non-zero**, there are no **TM$_{m,0}$ or TM$_{0,n}$ modes**. The lowest order mode is the **TM$_{1,1}$ mode**, which has one half-wavelength along both the $x$- and $y$-directions.

![[Pasted image 20250612163448.png]]

#### Propagation in Waveguides, 波导中的传播

##### Cutoff of Waveguide Modes, 波导模的截止

We have
$$
k_{z} = \beta = \sqrt{ \left( \dfrac{\omega}{c} \right)^{2} - \left( \dfrac{m \pi}{a} \right)^{2} - \left( \dfrac{n \pi}{b} \right)^{2} }
$$
Apparently, for a given mode index pair $(m, n)$, there exists a **cutoff frequency** $\omega_{\mathrm{c}}$ such that
$$
\omega_{\mathrm{c}} = c \sqrt{ \left( \dfrac{m \pi}{a} \right)^{2} + \left( \dfrac{n \pi}{b} \right)^{2} }
$$
Below this frequency, $\beta$ is **imaginary**, meaning the wave is **evanescent, 衰减**, and cannot propagate through the waveguide. 

With $\omega_{\mathrm{c}}$, the propagation constant $\beta$ can be expressed as
$$
\beta = \dfrac{\sqrt{ \omega^{2} - \omega_{\mathrm{c}}^{2} }}{c}
$$

##### Phase \& Group Velocities, 相速度与群速度

The **phase velocity, 相速度**, of a waveguide mode is given by
$$
v_{\mathrm{p}} = \dfrac{\omega}{\beta} = \dfrac{\omega}{\sqrt{ \omega^{2} - \omega_{\mathrm{c}}^{2} }} c > c
$$

The **group velocity, 群速度**, which is the speed at which the energy of the wave propagates, is given by
$$
v_{\mathrm{g}} = \dfrac{\dif\omega}{\dif\beta} = \left( \dfrac{\dif\beta}{\dif\omega} \right)^{-1} = \dfrac{\sqrt{ \omega^{2} - \omega_{\mathrm{c}}^{2} }}{\omega} c
$$

**Dispersion, 色散**, in rectangular metallic waveguides arises because different frequency components of a signal **propagate at different phase and group velocities.** 

