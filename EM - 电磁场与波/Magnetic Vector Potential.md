## Introduction of Magnetic Vector Potential, 磁矢势的引入

Noticing for volume current distribution, 
$$
\v{B}(\v{r}) = \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\v{J}(\v{r}') \times \hat{\sr }}{\sr ^2} \dif \tau' = \dfrac{\mu_{0}}{4\pi} \int_{V} \v{J}(\v{r}') \times \dfrac{\hat{\sr }}{\sr ^2} \dif \tau' = -\dfrac{\mu_{0}}{4\pi} \int_{V} \v{J}(\v{r}') \times \nabla\dfrac{1}{\sr } \dif \tau' 
$$
and we have the [[Math Basement#Product Rules of Special Derivatives|product rule]] $\nabla \times (f\v{F}) = f \nabla \times \v{F} - \v{F} \times \nabla f$, so
$$
-\v{J}(\v{r}') \times \nabla\dfrac{1}{\sr } = \nabla \times \dfrac{\v{J}(\v{r}')}{\sr } - \dfrac{1}{\sr } \underbrace{\nabla \times \v{J}(\v{r}')}_{\nabla \text{ is for } \v{r}} = \nabla \times \dfrac{\v{J}(\v{r}')}{\sr }
$$
thus
$$
\v{B}(\v{r}) = \dfrac{\mu_{0}}{4\pi} \int_{V} \nabla \times \dfrac{\v{J}(\v{r}')}{\sr } \dif \tau' = \nabla \times \left( \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\v{J}(\v{r}')}{\sr } \dif \tau' \right) 
$$
Comparing with the [[Electric Potential#^98645c|introduce of electric potential]], we can define the **[[Magnetic Vector Potential|magnetic vector potential]] $\v{A}$** as

> [!definition] Magnetic Vector Potential
> The **magnetic vector potential $\v{A}$** is defined as
> $$\v{A}(\v{r}) = \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\v{J}(\v{r}')}{\sr } \dif \tau'$$
> where $\v{J}$ is the **current density**, and $\mu_{0}$ is the **vacuum permeability**.

so that 
$$
\v{B}(\v{r}) = \nabla \times \v{A}(\v{r})
$$

> [!note] Magnetic vector potential is not unique
> The magnetic vector potential $\v{A}$ is not unique, as we can add a gradient of any scalar field $\nabla \Lambda$ to $\v{A}$ without changing the magnetic field $\v{B}$, i.e.
> $$\nabla \times (\v{A} + \nabla \Lambda) = \nabla \times \v{A} + \nabla \times \nabla \Lambda = \nabla \times \v{A} = \v{B}$$

> [!example] Magnetic vector potential of a spinning spherical shell
> Consider a **uniformly charged spherical shell** with radius $R$ and surface charge density $\sigma$, spinning with angular velocity $\v{\omega}$ around the $z$ axis. The **current density** on the shell is given by
> $$\v{K}(\v{r}) = \sigma \v{\omega} \times \v{r}$$ 
> Therefore,
> $$\v{A}(\v{r}) = \dfrac{\mu_{0}}{4\pi} \int_{V} \dfrac{\v{K}(\v{r}')}{\sr } \dif a' = \dfrac{\mu_{0}}{4\pi} \int_{S} \dfrac{\sigma \v{\omega} \times \v{r}'}{\sr } \dif a' = \dfrac{\mu_{0} \sigma \v{\omega} }{4\pi} \times \int_{S} \dfrac{\v{r}'}{\sr } \dif a'$$

## Typical Distributions of Magnetic Vector Potential, 磁矢势的典型分布

The relationship between $\v{A}$ and $\v{B}$ **mirrors that between $\v{B}$ and $\v{J}$**.

![[Pasted image 20250422160127.png]]

> [!example] Magnetic Vector Potential of a Solenoid
> Consider a **long solenoid** along $z$ axis, with radius of $R$ and turns of $N$ per unit length, carrying a **steady current $I$**. We [[Magnetic Fields#^287a4f|have known that]] the magnetic field inside the solenoid is uniform as $\v{B} = \mu_{0}NI \vu{z}$.
> 
> We can find the magnetic vector potential $\v{A}$ by **integrating it along a circular path** of radius $r$ around the solenoid. In this way, we have
> $$\displaystyle\oint_{C} \v{A} \cdot \dif \v{l} = \dint_{S} \nabla \times \v{A} \cdot \dif \v{a} = \dint_{S} \dint_{S} \v{B} \cdot \dif \v{a} = \varPhi_{B}$$
> where $\varPhi_{B}$ is the **magnetic flux** through the surface $S$ enclosed by the path $C$. So we have
> $$\v{A} = \begin{cases}
> \dfrac{\mu_{0}}{2} NI r \vu{\phi}, & r < R \\
> \dfrac{\mu_{0}}{2} NI \dfrac{R^2}{r} \vu{\phi}, & r > R
> \end{cases}$$
> 
> ```tikz
> \begin{document}
> \large
> \begin{tikzpicture}
> 
> \draw[thick,-latex] (0,0) -- (6,0) node[right] {$r$};
> \draw[thick,-latex] (0,0) -- (0,3) node[above] {$B$};
> 
> \draw[thick, blue!50!white] plot[domain=0:1.5,samples=100] (\x,2);
> \draw[thick, blue!50!white] (0.75,2) node[above] {$r < R$};
> \draw[thick, blue!50!white] (0,2) node[left] {$\mu_{0}NI$};
> 
> \draw[thick, red!50!white] plot[domain=0:1.5,samples=100] (\x,{2*\x}) node[left] {};
> \draw[thick, red!50!white] plot[domain=1.5:6,samples=100] (\x,{4.5/\x}) node[above] {$r > R$};
> 
> \draw[thick, dashed] (1.5,0) node[below] {$R$} -- (1.5,3);
> \end{tikzpicture}
> \end{document}
> ```

## The Aharonov-Bohm Effect, A-B 效应

In the original _Young's double-slit experiment_, the **first dark fringe, 第 1 暗纹**, occurs at
$$
x = \dfrac{\lambda L}{2d}
$$
where $L$ is the distance from the slits to the screen, $d$ is the distance between the slits, and $\lambda$ is the wavelength of the light. 

Due to the **wave-like nature, 波动性, of electrons**, it is possible to reproduce Young’s double-slit experiment using electrons, with the above formula still holding.

```tikz
\usepackage{amsmath}
\begin{document}
\large
\begin{tikzpicture}

\draw[dashed] (0, 0) -- (8, 0);
\draw[thick] (0, 2) -- (0, 0.6) (0, 0.4) -- (0, -0.4) (0, -0.6) -- (0, -2)
			 (8, 2) -- (8, -2);

\draw (0, 0) -- (8, 0.9) coordinate (P) node[right] {$x$};
\draw[thick, -latex] (0: 3) -- (6: 3) node[right] {$\theta$};
\draw[thick, red!50!white, -latex] (0, 0.5) -- (P) node[above, midway] {$L_1$}; 
\draw[thick, red!50!white, -latex] (0, -0.5) -- (P) node[below, midway] {$L_2$}; 

\end{tikzpicture}
\end{document}
```

If we have a **thin magnetic field** $B$ with width of $w$ in the left part of the middle space, the electron beam will get a **verticle momentum** $p_{\perp}$, and the pattern will have a **phase shift** of $\Delta \phi$ due to the **Lorentz force**. The **momentum** is given approximately by
$$
p_{\perp} = F_{\mathrm{B}} t = qvB \cdot \dfrac{w}{v} = qBw
$$
where $t$ is the time of flight within the magnetic field. The horizontal momentum of the electron beam is given by $p = \dfrac{h}{\lambda}$, so the **position shift** on the screen is given by
$$
\Delta x = \dfrac{p_{\perp}}{p} L = \dfrac{qBw}{h/\lambda} L = \dfrac{qB\lambda w L}{h}
$$
and the **phase shift** is given by
$$
\Delta \phi = \dfrac{\pi}{x} \Delta x = \dfrac{qB\lambda w L}{h} \dfrac{\pi}{\dfrac{\lambda L}{2d}} = \dfrac{q}{\hbar} Bwd = \dfrac{q}{\hbar} \varPhi_{B}
$$
where $\varPhi_{B}$ is the **magnetic flux** through the **area enclosed by the path of the electron beam**. 

Further experiments show that the phase shift **holds** even when the magnetic field 完全收缩到两 loop 之内, **$B$ 与电子束无空间交集**, so the phenomenon is wholly due to the **magnetic vector potential** $\v{A}$, i.e.
$$
\Delta \phi = \dfrac{q}{\hbar} \varPhi_{B} = \dfrac{q}{\hbar} \oint_{\mathrm{Loop}} \v{A} \cdot \dif \v{l}
$$

> [!note] The more FUNDAMENTAL quantity in magnetism
> A-B effect shows that the **magnetic vector potential $\v{A}$** is more **fundamental** than the magnetic field $\v{B}$, as it can affect the phase of a charged particle even in a region where the magnetic field is zero.



