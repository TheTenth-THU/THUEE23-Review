评估一个计算机架构时，需要考虑多个方面的因素，如：
+ **Cost：成本**
	+ 片上成本 (die cost) 与系统成本 (system cost)
+ **Performance：性能**
	+ 平均性能与最差性能
	+ 延迟 (latency) 与吞吐量 (throughput)
+ **Power & Thermal：能耗**
	+ 静态功耗 (static power) 与动态功耗 (dynamic power)
	+ 平均功耗 (average power) 与峰值功耗 (peak power)
	+ 热设计功耗 (thermal design power, TDP)
+ **Reliability：可靠性**
	+ 对电气噪声 (electrical noise)、部件故障 (part failure) 的耐受能力
	+ 对恶劣软件 (bad software)、操作失误 (operator error) 的鲁棒性
+ **Maintainability：维护性**
	+ 系统管理开销
+ **Security：安全性**
	+ 访问控制 (access control)
	+ 内存泄漏 (memory leakage)
	+ 侧信道 (side channels)

## Power & Thermal <br>功耗与发热设计

### Dynamic power <br>动态功耗

![[功耗的动态变化.png|功耗的动态变化]]

同时最优化性能和能效往往是冲突的目标。**峰值功耗 (peak power dissipation)** 是系统能够消耗的最大功率水平。系统需要能够在**不发生过热或故障**的情况下**处理峰值功率**。

对一个简单的 **$RC$ 电路**，一次**电平抬升中的功耗**为
$$
\begin{align}
E_{0 \to 1} &= \dint_{0}^{T} V_{\mathrm{dd}} i_{\text{supply}} (t) \dif t 
= \dint_{0}^{T} V_{\mathrm{dd}} C \dfrac{\dif V_{\mathrm{out}}(t)}{\dif t} \dif t \\
&= \dint_{0}^{V_{\mathrm{dd}}} V_{\mathrm{dd}} C \dif V_{\mathrm{out}} 
= C V_{\mathrm{dd}}^{2}
\end{align}
$$
其中进入电容的能量为
$$
\begin{align}
E_{\mathrm{cap}} &= \dint_{0}^{T} V_{\mathrm{out}} i_{\mathrm{cap}} (t) \dif t
= \dint_{0}^{T} V_{\mathrm{out}} C \dfrac{\dif V_{\mathrm{out}}(t)}{\dif t} \dif t \\
&= \dint_{0}^{V_{\mathrm{dd}}} V_{\mathrm{out}} C \dif V_{\mathrm{out}}
= \dfrac{1}{2} C V_{\mathrm{dd}}^{2}
\end{align}
$$
余下的 $\dfrac{1}{2} C V_{\mathrm{dd}}^{2}$ 能量被耗散在电阻上。类似地，对负载端为电容 $C_{\mathrm{L}}$ 的 **CMOS 逻辑门**，输出电平一次抬升的功耗也是 $C_{\mathrm{L}} V_{\mathrm{dd}}^{2}$，其中一半耗散在 PMOS 晶体管的阻性通道上，另一半存储在电容中，随后在下一次电平下降时耗散在 NMOS 晶体管的阻性通道上。

因此，每个晶体管[^1]的动态功耗为
$$
P_{\mathrm{dynamic}} = \dfrac{E_{0 \to 1}}{T} = \dfrac{1}{2} C_{\mathrm{L}} V_{\mathrm{dd}}^{2} f_{0 \to 1}
$$
整个**微处理器的动态功耗**即为
$$
P_{\mathrm{dynamic, total}} = \dfrac{1}{2} C_{\mathrm{L, total}} V_{\mathrm{dd}}^{2} f_{\mathrm{switching}} = \dfrac{1}{2} \alpha C_{\mathrm{L, total}} V_{\mathrm{dd}}^{2} f_{\mathrm{clock}}
$$
其中，$f_{\mathrm{switching}} = \alpha f_{\mathrm{clock}}$，$\alpha$ 为**切换因子 (switching factor)**，表示在时钟周期内晶体管发生电平转换的概率；$C_{\mathrm{L, total}}$ 可视为处理器中晶体管数目及其工艺技术的函数。

[^1]: 这里将一个 CMOS 逻辑门的 PMOS 和 NMOS 两部分分别视为 1 个晶体管，即共 2 个晶体管。

### Static power <br>静态功耗

考虑一个 CMOS 反相器，其中**静态功耗**来源于三种**关断态电流**：
+ **亚阈值漏电流 (subthreshold leakage current)**：
	当输入电压 $V_{\mathrm{GS}}$ 低于阈值电压 $V_{\mathrm{th}}$ 时，NMOS 晶体管仍有微小的漏电流 $I_{\mathrm{sub}}$ 流过，导致静态功耗 $P_{\mathrm{sub}} = V_{\mathrm{dd}} I_{\mathrm{sub}}$。
+ **栅致漏极泄漏电流 (gate-induced drain leakage current, GIDL current)**：
	当晶体管关闭时，栅极与漏极之间的强电场可引起电子隧穿效应，产生微小的泄漏电流 $I_{\mathrm{GD}}$（或 $I_{\mathrm{GS}}$），导致静态功耗 $P_{\mathrm{GD}} = V_{\mathrm{dd}} I_{\mathrm{GD}}$。
+ **漏极结漏电流 (drain junction leakage current)**：
	当晶体管关闭时，漏极—衬底 PN 结反向偏置下的微小漏电流 $I_{\mathrm{leak}}$ 流过，导致静态功耗 $P_{\mathrm{leak}} = V_{\mathrm{dd}} I_{\mathrm{leak}}$。

![[NMOS 空闲电流示意.png|NMOS 空闲电流示意|651x377]]

总之，关断态的泄漏电流在处理器中持续存在，即使在空闲状态下也会消耗功率，即静态功耗。随着工艺技术的缩小，静态功耗在总功耗中的比例逐渐增加，成为设计中不可忽视的因素。在 SRAM 中，静态功耗甚至可能超过动态功耗。

### Power reduction strategies <br>功耗降低策略

处理器的总功耗可表示为
$$
P_{\mathrm{total}} = \dfrac{1}{2} \alpha C_{\mathrm{L, total}} V_{\mathrm{dd}}^{2} f_{\mathrm{clock}} + I_{\mathrm{static}} V_{\mathrm{dd}}
$$
除了**直接降低供电电压 $V_{\mathrm{dd}}$**（20 年间已降低 80\%）外，还可以通过以下方法降低功耗。

#### Clock gating & Power gating <br>时钟门控与电源门控

**时钟门控**是指在不活动模块中，通过一个触发器控制关闭时钟信号，防止其进行不必要的状态切换，从而**降低动态功耗**。

**电源门控**是指通过一个高性能开关晶体管，将不活动模块与电源断开，**减少静态功耗**。

#### Dynamic voltage & frequency scaling (DVFS) <br>动态电压与频率调节

典型任务的执行能耗遵循 $E \propto V_{\mathrm{dd}}^{2}$，因此通过降低供电电压 $V_{\mathrm{dd}}$ 可以显著降低能耗。然而，CMOS 延迟时间依赖于 $V_{\mathrm{dd}}$ 和饱和区电流 $I_{\mathrm{on}}$，具体为
$$
t_{\mathrm{pd}} \propto C_{\mathrm{L}} \dfrac{V_{\mathrm{dd}}}{I_{\mathrm{on}}}, \qquad 
I_{\mathrm{on}} \propto \left( V_{\mathrm{dd}} - V_{\mathrm{th}} \right)^{\alpha}
$$
致使时钟频率与 $V_{\mathrm{dd}}$ 之间有关系
$$
f_{\mathrm{clock}} \propto \dfrac{\left( V_{\mathrm{dd}} - V_{\mathrm{th}} \right)^{\alpha}}{V_{\mathrm{dd}}}
$$
降低 $V_{\mathrm{dd}}$ 会增加晶体管的延迟 $t_{\mathrm{pd}}$，从而降低处理器的时钟频率 $f_{\mathrm{clock}}$。

**动态电压与频率调节 (DVFS)** 技术允许处理器根据工作负载动态调整 $V_{\mathrm{dd}}$ 和 $f_{\mathrm{clock}}$，在性能允许的范围内最大限度地降低功耗。

#### Thermal/load balancing control <br>发热/负载均衡控制

在微处理器中，通过**热传感器 (thermal sensors)** 监测处理器各部分的温度，结合 DVFS 技术，可以动态调整不同核心或模块的工作频率和电压，以避免过热并均衡负载，从而提高系统的整体可靠性和性能。

SRAM 设计中采用**多电压线路**设计，可以根据不同区域的访问频率和性能需求，动态调整供电电压，在空闲时转入**睡眠模式 (drowsy modes)**，以降低静态功耗；DRAM 则会设计一系列**低功耗工作模式 (low-power modes)**，如自刷新模式 (self-refresh mode)，以减少空闲时的功耗。

## Performance <br>性能

### Benchmarks & performance metrics <br>基准测试与性能参数

> [!definition] Performance, 性能参数
> 为量化计算机系统的性能，将**性能 (performance)** 定义为**单位时间内完成「工作」的数量**，即
> $$
> \text{Performance}(x) = \dfrac{1}{\text{ExTime}(x)}
> $$
> 这样，性能越高，执行时间越短，「$X$ 比 $Y$ 快 $n$ 倍」即
> $$
> n = \dfrac{\text{Performance}(X)}{\text{Performance}(Y)} = \dfrac{\text{ExTime}(Y)}{\text{ExTime}(X)}
> $$

通常，将定义计算机性能所用的「工作」任务选定为一系列的**基准测试 (benchmark)**，如 SPEC CPU、Transaction Processing Council (TPC) 基准等。

同一基准测试任务上多次测试的执行时间可以简单平均，但不同的基准测试任务执行时间则需要先**转化为相对性能指标**后再进行几何平均，以避免某些任务执行时间过长而主导整体结果，即**归一化 (normalization)**。归一化得到的加速比之间**只能进行几何平均**。

> [!theorem] Amdahl's Law, 阿姆达尔定律
> 在计算机系统中，整体性能提升受到最慢部分的限制。即使某个组件的性能大幅提升，如果其他组件没有相应提升，整体性能提升也会受到限制。具体地，提升前、后的**执行时间**关系为
> $$
> \text{ExTime}_{\text{new}} = \text{ExTime}_{\text{old}} \times \left( \left( 1 - \text{Fraction}_{\text{enhanced}} \right) + \dfrac{\text{Fraction}_{\text{enhanced}}}{\text{Speedup}_{\text{enhanced}}} \right) 
> $$
> 而**整体加速比**为
> $$
> \text{Speedup}_{\text{overall}} = \cfrac{1}{\left( 1 - \text{Fraction}_{\text{enhanced}} \right) + \dfrac{\text{Fraction}_{\text{enhanced}}}{\text{Speedup}_{\text{enhanced}}}}
> $$
> 其中，$\text{Fraction}_{\text{enhanced}}$表示被提升部分在整体中的比例，$\text{Speedup}_{\text{enhanced}}$表示被提升部分的加速比。

### Cycles per instruction (CPI) <br>指令平均周期数

一段程序的执行时间可表示为
$$
\text{ExTime} = \text{Instructions} \times \underbrace{ \dfrac{\text{Cycles}}{\text{Instruction}} }_{ \text{CPI} } \times \underbrace{ \frac{\text{Time}}{\text{Cycle}} }_{ \tfrac{1}{f_{\mathrm{clock}}} }
$$

| 因素                | Instructions | CPI    | Clock cycle time |
| :---------------- | :----------- | :----- | :--------------- |
| 程序 Program        | **相关**       |        |                  |
| 编译器 Compiler      | **相关**       | 间接相关   |                  |
| 指令集 Inst. set     | **相关**       | 间接相关   |                  |
| 组织架构 Organization |              | **相关** | **相关**           |
| 晶体管工艺 Technology  |              |        | **相关**           |

**指令平均周期数 (CPI, cycles per instruction)** 不取决于顶层程序长度和底层晶体管工艺技术，而是取决于处理器的微架构设计和指令集架构 (ISA)，因而是衡量处理器架构性能的重要指标。为遵循「越大越好」的原则，通常也使用其倒数值，即**每周期指令数 (IPC, instructions per cycle)**。

从处理器数据通路设计角度来看，CPI 可进一步细分为各种类型指令的比例及其对应的周期数之和，即
$$
\text{ExTime} = \dfrac{1}{f_{\text{clock}}} \times \sum_{i=1}^{n} \left( \text{Instructions}_{i} \times \text{CPI}_{i} \right)
$$

## Cost & Reliability <br>成本与可靠性

### Cost factors <br>成本因素

影响计算机系统成本的主要因素有：
+ **时间**：产量随时间增长，单位成本下降，遵循学习曲线 (learning curve)；
+ **规模**：大规模生产摊薄固定成本，提高采购、制造效率；
+ **竞争**：市场竞争不仅缩小了成本和价格之间的差距，而且还降低了成本。

就一块芯片而言，其成本表示为：
$$
\begin{align} 
\text{Cost of integrated circuit} = \dfrac{1}{\text{Final test yield}} \times (& \text{Cost of die} + \text{Cost of testing die} \\
&+ \text{Cost of packaging and final test} )  
\end{align}
$$
其中，**片上成本 (cost of die)** 可表示为
$$
\text{Cost of die} = \dfrac{\text{Cost of wafer}}{\text{Dies per wafer} \times \text{Die yield}}
$$
而每片晶圆的成本 (cost of wafer) 取决于晶圆的尺寸和制造工艺技术，晶圆上的芯片数 (dies per wafer) 和**良率 (die yield)** 则为
$$
\begin{align}
& \text{Dies per wafer} = \cfrac{\pi \times \left( \dfrac{\text{Wafer diameter}}{2} \right)^{2}}{\text{Die area}}- \dfrac{\pi \times \text{Wafer diameter}}{\sqrt{ 2\times \text{Die area} }}  \\
& \text{Die yield} = \text{Wafer yield} \times \dfrac{1}{\left( 1 + \text{Defects per unit area} \times \text{Die area} \right)^{N}}
\end{align}
$$


可行的