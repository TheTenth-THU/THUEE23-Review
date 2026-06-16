## Complex Refractive Index, 复折射率

> [!danger] Misconception about the polarization
> It is important to note that we cannot directly apply
> $$
> \v{P} = \varepsilon_{0} \chi_{\mathrm{e}} \v{E}
> $$
> as this relation assumes that the polarization $\v{P}$ **responds instantaneously, 瞬时响应**, to the applied electric field $\v{E}$, which is **physically unrealistic**.
> 
> To accurately describe the polarization of dielectric materials, we must consider the **time-dependent response**, which may lead to a **convolution, 卷积**, form of the polarization as
> $$\v{P}(t) = \varepsilon_{0} \dint_{-\infty}^{t} \chi_{\mathrm{e}} (t - \tau) \v{E} (\tau) \dif \tau$$
> 
> To avoid complex integration, we can use the **Fourier transform, 傅里叶变换**, to convert the time-dependent response into a **frequency-dependent form**. Therefore, we can convert convolution $\varepsilon_{0} \cpq{\chi} * \cpq{\v{E}}$ into multiplication $\varepsilon_{0} \cpq{\chi}(\omega) \cpq{\v{E}}(\omega)$.
> 
> To simplify the analysis, we can assume that the electric field $\v{E}$ is a **single-frequency plane wave**, which allows us to express the polarization as another plane wave with the same frequency $\omega$.

We proceed by substituting a set of **trial plane-wave solutions, 试探平面波解**
$$
\cpq{\v{E}} = \cpq{E}_{0} (\omega) \e^{\I(\cpq{k} z - \omega t)} \vu{x}, \qquad
\cpq{\v{P}} = \cpq{P}_{0} (\omega) \e^{\I(\cpq{k} z - \omega t)} \vu{x}
$$
into the wave equation $\nabla ^2 \v{E} - \dfrac{1}{c^{2}} \partial_{tt}\v{E} = \mu_{0}\partial_{tt} \v{P}$ and get
$$
\begin{align}
-\cpq{k}^2 \cpq{E}_{0} (\omega) \e^{\I(\cpq{k} z - \omega t)} \vu{x} + \dfrac{\omega^2}{c^2} \cpq{E}_{0} (\omega) \e^{\I(\cpq{k} z - \omega t)} \vu{x} &= - \mu_{0} \omega^2 \cpq{P}_{0} (\omega) \e^{\I(\cpq{k} z - \omega t)} \vu{x} \\
-\cpq{k}^2 \cpq{E}_{0} (\omega) + \dfrac{\omega^2}{c^2} \cpq{E}_{0} (\omega) &= - \mu_{0} \omega^2 \cpq{P}_{0} (\omega)
\end{align}
$$
We assume **$\cpq{P}_{0}(\omega) = \varepsilon_{0} \cpq{\chi}_{\mathrm{e}}(\omega) \cpq{E}_{0}(\omega)$**, therefore
$$
\cpq{k}^2 = \dfrac{\omega^2}{c^2} + \mu_{0} \omega^2 \cdot \varepsilon_{0} \cpq{\chi}_{\mathrm{e}} (\omega) = \dfrac{\omega^2}{c^2} + \dfrac{\omega^2}{c^2} \cpq{\chi}_{\mathrm{e}} (\omega) = \dfrac{\omega^2}{c^2} \left(1 + \cpq{\chi}_{\mathrm{e}} (\omega)\right) := k_{0}^2 \cpq{n}^2
$$
where:
+ $\mu_{0}\varepsilon_{0} = \dfrac{1}{c^2}$,
+ $k_{0} = \dfrac{\omega}{c}$ is the **wave number in vacuum**, and
+ **$\cpq{n} = \sqrt{1 + \cpq{\chi}_{\mathrm{e}} (\omega)} = \sqrt{ \cpq{\varepsilon}_{\mathrm{r}}(\omega) }$** is the frequency-dependent complex **refractive index, 折射率**, of the medium.

The complex refractive index $\cpq{n}(\omega)$ can be also expressed as
$$
\cpq{n}(\omega) = n(\omega) + \I \kappa(\omega)
$$
where:
+ $n(\omega)$ is the **real part** of the refractive index, which describes the **phase velocity** of the wave in the medium,
+ $\kappa(\omega)$ is the **extinction coefficient**, which describes the **attenuation** of the wave in the medium.

If we substitute $\cpq{k} = k_{0} \cpq{n} = k_{0} (n + \I \kappa)$ into the wave, we have
$$
\cpq{E} = \cpq{E}_{0} \e^{\I(k_{0} n z - \omega t)} = \cpq{E}_{0} \e^{-\kappa k_{0} z} \e^{\I (k_{0} n z - \omega t)}
$$
Thus, the **phase velocity, 相速度**, of the wave in the medium is given by
$$
v_{\mathrm{p}} = \dfrac{\omega}{k} = \dfrac{c}{n(\omega)}
$$
while the **intensity** of the wave is given by
$$
I \propto \cpq{E} \cpq{E}^{*} \propto \e^{-2\kappa k_{0} z} 
$$
$\alpha = 2\kappa k_{0}$ is the **attenuation coefficient, 衰减系数**, which describes how quickly the intensity of the wave decreases as it propagates through the medium.

## Modeling Interaction between Electromagnetic Waves and Media, 介质与电磁波的作用模型

### Lorentz model of dielectric materials, 电介质的洛伦兹模型

Within the dielectric material, the attraction force between the **positive ion, 正电原子核**, and the **electron cloud, 电子云**, can be **modeled as a spring mass system, 建模为弹簧系统**, whose oscillation is **driven by the external electric field**. The motion of the **electron cloud** follows
$$
m \ddot{\cpq{x}} = -qE - m \omega_{0}^2 \cpq{x} - m \gamma \dot{\cpq{x}}
$$
where we build the $x$-axis along the direction of the external electric field, and:
+ $m$ is the **effective mass** of the electron cloud,
+ $\omega_{0}$ is the **natural frequency, 固有频率**, of the free oscillation of the electron cloud, which is determined by the **energy levels** of the electron cloud, with $m\omega_{0}^2$ corresponds to the classical spring constant,
+ $\gamma$ is the **damping constant, 阻尼系数**, of the electron cloud which represents the **friction** loss.

To simplify the analysis, we can also substitute a **trial plane-wave solution** $\cpq{E}(t) = \cpq{E}(\omega) \e^{-\I \omega t}$ and $\cpq{x}(t) = \cpq{x}(\omega) \e^{-\I \omega t}$ to take the advantage of the **Fourier transform, 傅里叶变换**. We have
$$
m \left( -\I \omega \right)^2 \cpq{x}(\omega) = -q \cpq{E}(\omega) - m \omega_{0}^2 \cpq{x}(\omega) - m \gamma \left( -\I \omega \right) \cpq{x}(\omega)
$$
and solving for $\cpq{x}(\omega)$ yields
$$
\cpq{x}(\omega) = - \dfrac{q}{m} \dfrac{\cpq{E}(\omega)}{\left( \omega_{0}^2 - \omega^2 - \I \gamma \omega \right)}
$$
For a single electron cloud, the **dipole moment** is $\cpq{p}_{\mathrm{dip}}(\omega) = -q\cpq{x}(\omega)$; and for a **macroscopic material**, the **polarization** is $\cpq{P}(\omega) = N\cpq{p}_{\mathrm{dip}}(\omega)$. Therefore,
$$
\cpq{\chi}_{\mathrm{e}} (\omega) = \dfrac{\cpq{P}(\omega)}{\varepsilon_{0} \cpq{E}(\omega)} = \underbrace{ \dfrac{Nq^2}{\varepsilon_{0} m} }_{ \omega_{\mathrm{P}}^{2} } \dfrac{1}{\omega_{0}^2 - \omega^2 - \I \gamma \omega } = \dfrac{\omega_{\mathrm{P}}^{2}}{\omega_{0}^2 - \omega^2 - \I \gamma \omega }
$$
where:
+ $N$ is the **number density** of the electron clouds,
+ $\omega_{\mathrm{P}} = \sqrt{\dfrac{Nq^2}{\varepsilon_{0} m}}$ is the **plasma frequency, 等离子体频率**, which is a characteristic frequency of the material.

The material model above is known as the **Lorentz model of dielectric materials, 洛伦兹模型**. Under this model, the **complex refractive index** is given by
$$
\cpq{n}(\omega) = \sqrt{1 + \dfrac{\omega_{\mathrm{P}}^{2}}{\omega_{0}^2 - \omega^2 - \I \gamma \omega }} 
$$

### Drude model of metals, 金属的德鲁德模型

In metals, the **free electrons** can be modeled as a **gas of free electrons**, which are not bound to any specific atom, so they would not have a **natural frequency, 固有频率**. Therefore, we can set $\omega_{0} = 0$ in the Lorentz model, which leads to the **Drude model of metals, 德鲁德模型**, as
$$
\cpq{n}(\omega) = \sqrt{1 + \dfrac{\omega_{\mathrm{P}}^{2}}{-\omega^{2}- \I \gamma \omega }} = \sqrt{1 - \dfrac{\omega_{\mathrm{P}}^{2}}{\omega^{2} + \I \gamma \omega }}
$$
where:
+ $\omega_{\mathrm{P}} = \sqrt{\dfrac{Nq^2}{\varepsilon_{0} m}}$ is the **plasma frequency, 等离子体频率**, which is a characteristic frequency of the material, and
+ $\gamma$ is the **damping constant, 阻尼系数**, which represents the **friction** loss of the free electrons.

The **plasma frequency, 等离子体频率**, is an important parameter for metals, representing the **natural oscillation frequency, 自然震荡频率**, of the free electron gas in response to an external electric field.

#### High-Frequency Limit, 高频极限

If **$\omega \gg \gamma$**, we can neglect the damping term $\I \gamma \omega$ in the denominator, which leads to
$$
\cpq{n}(\omega) = \sqrt{1 - \dfrac{\omega_{\mathrm{P}}^{2}}{\omega^{2}}}
$$
+ For $\omega > \omega_{\mathrm{P}}$, the refractive index $\cpq{n}(\omega)$ is **real and positive**, while the wave is **propagating** with phase velocity $v_{\mathrm{p}} = \dfrac{c}{n(\omega)} > c$,
+ For $\omega < \omega_{\mathrm{P}}$, the refractive index $\cpq{n}(\omega)$ is **imaginary**, which leads to a **decaying wave** with no propagation.

> [!definition] Fresnel Reflection Coefficient
> The **Fresnel reflection coefficient** at normal incidence is given by
> $$ R = \dfrac{(n - 1)^{2} + \kappa^{2}}{(n + 1)^{2} + \kappa^{2}} $$
> where $\cpq{n} = n + \I\kappa$ is the complex refractive index of the medium.

In the frequency range of **$\gamma \ll \omega < \omega_{\mathrm{P}}$**, the **Fresnel reflection coefficient** at normal incidence is given by
$$
R \approx \dfrac{1 + \kappa^{2}}{1 + \kappa^{2}} = 1
$$

#### Low-Frequency Limit, 低频极限

If **$\omega \ll \gamma = \dfrac{1}{\tau}$** and **$\omega \ll \omega_{\mathrm{P}}$**, 
$$
\cpq{n}(\omega) = \sqrt{1 - \dfrac{\omega_{\mathrm{P}}^{2}}{\I \gamma \omega }} = \sqrt{ 1 + \I \dfrac{\omega_{\mathrm{P}}^{2}}{\gamma \omega} } \approx \sqrt{ \I \dfrac{\omega_{\mathrm{P}}^{2}}{\gamma \omega} } = \dfrac{\omega_{\mathrm{P}}}{\sqrt{2 \gamma \omega} } (1+\I)
$$
so $n(\omega) = \kappa(\omega) = \dfrac{\omega_{\mathrm{P}}}{\sqrt{2 \gamma \omega} }$, and the **attenuation coefficient** is given by
$$
\alpha = 2 \kappa k_{0} = \dfrac{2\omega_{\mathrm{P}}}{\sqrt{2 \gamma \omega} } \cdot \dfrac{\omega}{c} = \dfrac{\omega_{\mathrm{P}}}{c}  \sqrt{2\omega \tau}
$$

## Phase \& Group Velocities, 相速度和群速度

> [!definition] Phase Velocity
> The **phase velocity** of a wave is the speed at which the phase of the wave propagates in space, given by
> $$ v_{\mathrm{p}} = \dfrac{\omega}{k} $$
> where $\omega$ is the angular frequency and $k$ is the wave number.

> [!definition] Group Velocity
> The **group velocity** of a wave is the speed at which the envelope of the wave packet propagates in space, given by
> $$ v_{\mathrm{g}} = \dfrac{\partial \omega}{\partial k} $$
> where $\omega$ is the angular frequency and $k$ is the wave number.

Real signals cannot be purely monochromatic; instead, they are **modulated** and have a **finite bandwidth**. Such signals must be represented as a superposition of frequencies. Therefore, only a **wave packet**, which is a superposition of many monochromatic waves, can be physically realized and carry information.