## Electric Potential of Point Charges  点电荷的电势

Noticing that
$$
\v{E}(\v{r}) = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}^2} \vu{\mathscr{r}_{i}} = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}} \nabla \left( - \dfrac{1}{\mathscr{r}_{i}} \right) = - \nabla \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}}
$$
is the gradient of some scalar field, we define this scalar field as the **electric potential $V$**.

> [!definition] Electric Potential
> The **electric potential $V$** at a point $\v{r}$ due to a collection of point charges $q_{i}$ at positions $\v{r}_{i}$ is given by
> $$
> V(\v{r}) = \sum\limits_{i} \dfrac{q_{i}}{4\pi\varepsilon_{0}\mathscr{r}_{i}}
> $$
> where $\v{\mathscr{r}_{i}} = \v{r} - \v{r}_{i}$, and $\varepsilon_0$ is the vacuum permittivity.

Then, the electric field can be calculated by taking the negative gradient of the electric potential,  i.e.
$$
\v{E}(\v{r}) = - \nabla V(\v{r})
$$

^98645c

## Conservative Property of Static Electric Fields  静电场的保守性

The integration of the electric field $\v{E}$ along a path $\varGamma$ from $\v{r}_{1}$ to $\v{r}_{2}$ is given by
$$
\int_{\v{r}_{1}}^{\v{r}_{2}} \v{E}(\v{r}) \cdot \dif \v{l} = - \int_{\v{r}_{1}}^{\v{r}_{2}} \nabla V(\v{r}) \cdot \dif \v{l} = V(\v{r}_{1}) - V(\v{r}_{2})
$$
which is **independent of the path taken**. So we say the electric field $\v{E}$ is **conservative**, and the electric potential $V$ is well-defined as **a function of charge distribution**, like
$$
\begin{align}
V(\v{r}) &= - \int_{\infty}^{\v{r}} \v{E}(\v{r}') \cdot \dif \v{l}' 
= -\int_{\infty}^{\v{r}} \int_{\mathbb{R}^3} \dfrac{1}{4\pi\varepsilon_{0}} \dfrac{\rho(\v{r}'') \dif \tau''}{\mathscr{r}'^2} \vu{\mathscr{r}}' \cdot \dif \v{l}' \\
&= \dfrac{1}{4\pi\varepsilon_{0}} \int_{\mathbb{R}^3} \rho(\v{r}'') \int_{\v{r}}^{\infty} \dfrac{1}{(\v{r}''-\v{r}')^2} \dif l' \dif \tau''  \\
&= \dfrac{1}{4\pi\varepsilon_{0}} \int_{\mathbb{R}^3} \dfrac{\rho(\v{r}'')}{\mathscr{r}''} \dif \tau'' = \dfrac{1}{4\pi\varepsilon_{0}} \int_{\mathbb{R}^3} \dfrac{\dif q}{\mathscr{r}} 
\end{align}
$$

## Poisson's Equation  泊松方程

For a **charge distribution** $\rho(\v{r})$, the electric field $\v{E}$ and the electric potential $V$ are related by
$$
\nabla \cdot \v{E} = \dfrac{\rho}{\varepsilon_{0}}, \quad \v{E} = - \nabla V
$$
so we have

> [!theorem] Poisson's Equation
> The electric potential $V$ at a point $\v{r}$ due to a charge distribution $\rho(\v{r})$ is given by
> $$\nabla^2 V(\v{r}) = - \dfrac{\rho(\v{r})}{\varepsilon_{0}}$$

^db59a9

Especially, at the point with zero charge density, the electric potential satisfies

> [!theorem] Laplace's Equation
> The electric potential $V$ at a point $\v{r}$ in a region with zero charge density is given by
> $$\nabla^2 V(\v{r}) = 0$$

^127adf



