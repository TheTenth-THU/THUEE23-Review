## MOSFET 的控制机理

**金属—氧化物—半导体场效应晶体管 (metal-oxide-semiconductor field-effect transistor, MOSFET)** 由栅极电压控制源漏之间的反型沟道。栅氧层使直流栅电流近似为零，因此 MOSFET 输入电阻很高。

对增强型 NMOS，定义过驱动电压

$$
V_{OV}=V_{GS}-V_{TH}
$$

当 $V_{GS}<V_{TH}$ 时未形成强反型沟道，器件近似截止。

## 大信号工作区

令 $k_n=\mu_nC_{\mathrm{ox}}W/L$，忽略沟道长度调制时，长沟道 NMOS 的平方律模型为

$$
i_D=
\begin{cases}
0, & V_{GS}<V_{TH},\\
k_n\left(V_{OV}V_{DS}-\dfrac{V_{DS}^2}{2}\right), & 0\leq V_{DS}<V_{OV},\\
\dfrac{1}{2}k_nV_{OV}^2, & V_{DS}\geq V_{OV}.
\end{cases}
$$

第二种状态称为三极管区或线性区，第三种状态称为饱和区。MOSFET 用作开关时在截止区与低 $V_{DS}$ 的三极管区之间切换，用作放大器时通常偏置在饱和区。

> [!danger] MOSFET 饱和区不是低阻导通区
> MOSFET 的饱和区适合受控电流源式放大；作为数字开关导通时，器件通常工作在三极管区。它与 BJT「饱和导通」的命名含义不同。

### 非理想效应

沟道长度调制使饱和区电流随 $V_{DS}$ 略有增加，可写成

$$
i_D\approx\frac{1}{2}k_nV_{OV}^2(1+\lambda V_{DS})
$$

体端与源端电位不同会产生体效应并改变阈值。亚阈值电流、迁移率退化和速度饱和则使短沟道器件偏离简单平方律。

## 偏置与小信号模型

偏置网络确定 $I_D$、$V_{GS}$ 和 $V_{DS}$，并保证信号摆动期间器件保持在目标工作区。工作点附近的主要小信号参数为

$$
g_m=\frac{\partial I_D}{\partial V_{GS}}=k_nV_{OV}=\frac{2I_D}{V_{OV}}
$$

以及

$$
r_o\approx\frac{1}{\lambda I_D}
$$

若体端不与源端交流等势，还需加入体跨导 $g_{mb}$。栅源、栅漏和结电容决定高频极点。

## 基本放大级

### 共源级

共源级提供反相电压增益。源极交流接地时

$$
A_v\approx-g_m(R_D\parallel r_o\parallel R_L)
$$

加入未旁路源极电阻产生源极退化，使增益约变为

$$
A_v\approx-\frac{g_m(R_D\parallel r_o\parallel R_L)}{1+g_mR_S}
$$

增益降低，但线性度和偏置稳定性提高。

### 源极跟随器

共漏级也称**源极跟随器 (source follower)**，电压增益接近 1，输入电阻高、输出电阻较低，可作为缓冲器。体效应和有限 $r_o$ 会进一步降低增益。

### 共栅级

共栅级输入电阻约为 $1/g_m$，不反相且 Miller 效应小，适合宽带输入和级联结构。共源与共栅串接形成 cascode，可提高输出电阻并减小栅漏电容反馈。

## MOS 电流镜

把一只饱和区 MOSFET 的栅漏相连，可用参考电流建立 $V_{GS}$，再驱动匹配输出管。理想情况下，电流比由尺寸比决定：

$$
\frac{I_{O}}{I_{\mathrm{REF}}}\approx\frac{(W/L)_O}{(W/L)_{\mathrm{REF}}}
$$

实际误差来自沟道长度调制、阈值失配和有限输出摆幅。cascode 电流镜能提高输出电阻，但需要更多电压裕量。

## MOSFET 与 BJT 的比较

MOSFET 由电压控制且输入电流小，易于高密度 CMOS 集成；BJT 在相同偏置电流下常具有更大的跨导 $g_m=I_C/V_T$。实际选择还取决于噪声、速度、输入阻抗、功耗和工艺条件。

> [!tip]
> MOSFET 电路同样按「工作区—偏置—小信号—摆幅」求解。写出电流方程后必须回代检查 $V_{GS}$ 与 $V_{DS}$ 是否满足所假设的工作区不等式。
