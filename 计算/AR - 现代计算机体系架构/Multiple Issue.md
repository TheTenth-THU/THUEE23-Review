## Introduction <br>引入

### Instruction-level _v.s._ Machine-level parallelism <br>指令级并行与机器级并行

#### Instruction-level parallelism (ILP) <br>指令级并行

**指令级并行 (ILP)** 针对**程序**而言，是衡量处理器**可能同时执行**程序中指令平均数量的一项指标。ILP 反映了程序中**指令之间的独立性**和并行执行的潜力。ILP 的高低取决于程序的结构和编译器的优化能力，通常受限于**数据依赖**与**控制依赖**。

> [!example] 程序的指令级并行性
> 考虑如下指令序列：
> ```
> I1 - r1 <- r2 + 1
> I2 - r3 <- r1 / 17
> I3 - r4 <- r0 - r3
> ```
> 在该序列中，`I2` 依赖于 `I1` 的结果，而 `I3` 依赖于 `I2` 的结果，因此这些指令**必须顺序执行**，$\mathrm{ILP} = 1$；而若指令间无依赖关系，如考虑如下指令序列：
> ```
> I1 - r1 <- r2 + 1
> I2 - r3 <- r9 / 17
> I3 - r4 <- r0 - r10
> ```
> 则这些指令**可以并行执行**，$\mathrm{ILP} = 3$。

#### Machine-level parallelism (MLP) <br>机器级并行

**机器级并行 (MLP)** 针对**处理器**而言，是衡量处理器**实际同时执行**指令平均数量的一项指标。MLP 反映了处理器**对程序 ILP 的利用能力**。MLP 的高低取决于处理器的架构设计、流水线深度、缓存层次结构以及多核处理能力。

在提高并行性能的意义上，ILP 与 MLP 均重要。高 ILP 的程序为处理器提供了更多并行执行的机会，而高 MLP 的处理器则能够更有效地利用这些机会，从而提升整体性能。

MLP 的提升，即**多发射 (multiple issue)** 的实现，通常包括以下两种策略：
+ 静态多发射，即**[[#^VLIWArchitecture|超长指令字 (very long instruction word, VLIW)]]** 设计，通过**编译器**在**编译时**识别和打包可并行执行的指令；
+ 动态多发射，即**[[#^SuperscalarArchitecture|超标量 (superscalar, SS)]]** 设计，通过**处理器硬件**在**运行时**动态调度和发射指令。

### Instruction issue & completion policies <br>指令发射与指令完成

指令开始执行的时刻称为**指令发射 (instruction issue)**，指令完成执行的时刻称为**指令完成 (instruction completion)**。指令发射与完成的策略影响处理器的并行度和性能，具体地：
+ 指令的发射影响**指令预取 (instruction lookahead) 能力**，即处理器能够获取、解码并发射超越当前执行点的指令，以尝试寻找更多可发射指令的能力；
+ 指令的完成影响**处理器前瞻 (processor lookahead) 能力**，即处理器能够检查超越当前执行点的已发射指令，以尝试寻找更多可完成指令的能力。

#### In-order issue with in-order completion <br>顺序发射顺序完成

最简单的策略是按照程序的确切顺序发出指令，并按照取指顺序（即程序顺序）完成指令，这称为**顺序发射、顺序完成 (in-order issue with in-order completion, IOI-IOC)**。

考虑如下指令序列：
```
I1 – needs two execute cycles (a multiply)  
I2  
I3
I4 – needs the same function unit as I3
I5 – needs data value produced by I4
I6 – needs the same function unit as I5
```
^557724

假定处理器为 IFID—EX—WB 三级结构，每周期可以取指、译码和发射 2 条指令，同时可以写回 2 条指令。按照 IOI-IOC 策略，指令的执行过程如下：

![[IOI-IOC.png|IOI-IOC]]

#### In-order issue with out-of-order completion <br>顺序发射乱序完成

为了提升处理器的前瞻能力，可以允许指令按照程序顺序发射，但允许指令乱序完成，这称为**顺序发射、乱序完成 (in-order issue with out-of-order completion, IOI-OOC)**。

采用乱序完成机制时，后续指令可以先于前序指令执行完毕，由此**提升长延迟操作（如除法运算）的性能表现**。使用乱序完成时，若出现资源冲突（例如功能单元占用）或待发射指令所需数据尚未计算完成，指令发射仍将暂停。

考虑[[#^557724|上述指令序列]]，采用 IOI-OOC 策略，指令的执行过程如下：

![[IOI-OOC.png|IOI-OOC]]

当引入乱序完成机制后，处理器需要额外处理一类数据冒险，即**输出依赖 (output dependency)**，典型例子是**写前写 (write-before-write)**。假定
```
I1 - writes to R3
I2 - writes to R3
I5 - reads R3
```
如果 `I2` 在 `I1` 之前完成，则 `I5` 可能读到错误的 `R3` 值。为避免这种情况，处理器需要确保**后续指令的写回不会覆盖前序指令的结果**。

#### Out-of-order issue with out-of-order completion <br>乱序发射乱序完成

采用顺序发射时，处理器一旦遇到已解码指令存在资源冲突或与已发射但未完成的指令存在数据依赖，便会**停止解码**指令。即使后续更多指令可能不存在冲突因而可被发射，处理器也无法查看超越冲突指令之后的内容。

为了进一步提升处理器的指令预取能力，可以在解码阶段与执行阶段之间插入**缓冲区 (buffer)** 存储暂时冲突指令之后的指令，并标记缓冲区中不存在资源冲突或数据依赖的指令，被标记的指令随后可不考虑其程序顺序而从缓冲区中发射，这称为**乱序发射、乱序完成 (out-of-order issue with out-of-order completion, OOI-OOC)**。

采用 OOI-OOC 策略时，处理器可以**更灵活地调度指令执行**，以最大化资源利用率和并行度；但同时，处理器需要复杂的硬件机制来跟踪指令的状态、管理数据依赖，并确保程序语义的正确性。

考虑[[#^557724|上述指令序列]]，采用 OOI-OOC 策略，指令的执行过程如下：

![[OOI-OOC.png|OOI-OOC]]

采用乱序发射机制时，处理器需要额外处理一类数据冒险，即**反向依赖 (antidependency)**，典型例子是**读前写 (write-before-read)**。假定
```
I1 - Uses R3 to compute a value and writes to R3
I2 - Reads R3
I3 - Writes to R3
```
如果 `I3` 在 `I1` 之前完成，则 `I2` 可能读到错误的 `R3` 值。为避免这种情况，处理器需要确保**后续指令的写回不会覆盖前序指令的值**。

### Multiple-issue datapath responsibilities <br>多发射数据通路的冒险处理

类似单发射处理器，多发射处理器的数据通路也需要处理**数据冒险 (data hazard)**、**控制冒险 (control hazard)** 和**结构冒险 (structural hazard)**。然而，多发射处理器由于同时发射多条指令，指令之间的依赖与冲突更为复杂。

#### Data dependencies <br>数据依赖

数据依赖描述了指令之间因数据使用而产生的关系，主要包括以下三类：
+ **真实依赖 (true dependency)**，也称为**流依赖 (flow dependency)**，表示后一条指令**需要使用**前一条指令产生的数据，因此必须在**写入后**才能读取该数据，称为**读前写 (read-after-write, RAW) 依赖**，或**读后写 (read-before-write) 冒险**；
+ **反向依赖 (antidependency)**，表示后一条指令**将要覆盖**前一条指令要使用的数据，因此必须在**读取后**才能写入该数据，称为**写前读 (write-after-read, WAR) 依赖**，或**写后读 (write-before-read) 冒险**；
+ **输出依赖 (output dependency)**，表示两条指令将要写入同一数据位置，因此必须确保前一条指令的写入**先于**后一条指令的写入，称为**写前写 (write-after-write, WAW) 依赖**，或**写后写 (write-before-write) 冒险**。

> [!note] 反向依赖与真实依赖
> **反向依赖**约束与**真实依赖**相似，但方向相反。
> + 违背真实依赖产生的冒险是因为后一条指令使用了前一条指令（尚未）产生的值，即**读后写 (read-before-write)**；
> + 违背反向依赖产生的冒险是因为后一条指令覆盖了前一条指令（尚未）使用的值，即**写后读 (write-before-read)**。
> 
> 两者的根本区别在于，真实依赖关系源自**数据流动**，是指令语义的一部分；而反向依赖关系源自**资源重用**，是指令调度时需要考虑的约束。

反向依赖和输出依赖不是指令语义的一部分，而是由于多发射处理器**乱序发射**和**乱序完成**机制引入的额外约束。通过**寄存器重命名 (register renaming)** 技术，引入不可见的寄存器来拆分前后读写关系，可以消除这些依赖，从而提升指令并行度。

> [!example] 寄存器重命名示例
> 考虑如下指令序列：
> ```
> I1 >>> r3 <- r3 * r5
> I2 >>> r4 <- r3 + 1
> I3 >>> r3 <- r5 + 1
> ```
> 在该序列中，`I2` 依赖于 `I1` 的结果，而 `I3` 又写入了 `r3`，导致 `I2` 和 `I3` 之间存在**反向依赖**。通过寄存器重命名，可以将 `I3` 的目标寄存器重命名为一个新的寄存器，即
> ```
> I1 >>> r3b <- r3a * r5a
> I2 >>> r4a <- r3b + 1
> I3 >>> r3c <- r5a + 1
> ```
> 这样，`I2` 和 `I3` 之间的反向依赖被消除，允许它们并行执行。

#### Procedural dependencies <br>控制依赖

**控制依赖 (control dependency)** 描述了指令之间因控制流变化而产生的关系，主要涉及分支指令和跳转指令的执行。

#### Resource conflicts <br>资源冲突

多发射处理器存在更多潜在的**资源冲突 (structural hazard)** 或者说**结构冒险**，因为多条指令可能同时需要使用相同的硬件资源，特别是寄存器堆写入端口、缓存端口等。

通过**增加硬件资源**可以缓解资源冲突，但这也会增加处理器的复杂性，提高功耗和成本。因此，多发射处理器通常需要**智能调度机制**，以在发射指令时避免资源冲突。 

## Very Long Instruction Word (VLIW) Architecture <br>超长指令字体系架构 ^VLIWArchitecture

**超长指令字 (Very Long Instruction Word, VLIW)** 是一种处理器设计方法，通过将多条操作编码在单个超长指令字中，实现**高指令级并行性 (ILP)**。VLIW 处理器**依赖编译器**在编译时识别和调度可并行执行的指令，从而简化硬件设计，提升执行效率。

VLIW 打包在一个时钟周期内发射的指令组合称为**发射包 (issue packet)**，包内捆绑的指令类型的组合通常是有限的。

> [!example] VLIW MIPS 发射包示例
> 考虑一个 2 发射 VLIW MIPS 处理器，其发射包设定为
> ```tx
> | 64 bits ||
> | Slot 1        | Slot 2        |
> |:--------------|:--------------|
> | ALU 指令 (R)  | Load/Store 指令 (I) |
> | Branch 指令 (I) | Load/Store 指令 (I) |
> ```
> 
> 这一简单的设定要求：
> + 寄存器堆有 4 个读端口和 2 个写端口，以支持包内指令的并行读写；
> + 内存地址计算拥有独立的 ALU 单元，以支持 Load/Store 指令的并行执行。

^9c668a

### VLIW data hazards <br>VLIW 的数据冒险

VLIW 是静态多发射体系结构，指令的调度和打包在编译时完成，因此**数据冒险 (data hazard)** 的处理主要依赖于**编译器**的静态分析和调度能力，以确保**发射包内的指令之间**不存在数据依赖冲突。

具体地，考虑[[#^9c668a|上述 2 发射 VLIW MIPS 处理器]]，编译器在生成发射包时需要注意的至少有：
+ **`lw`** 获取的数据在**下 1 个发射包及之前**都不能被使用，即含有 `lw` 指令的发射包的下 1 个发射包（下 2 条指令）中不能包含使用该数据的指令；
+ **ALU 指令**的结果不能被**同一发射包内**的 Load/Store 指令使用，即含有 ALU 指令的发射包中不能包含使用该结果的 Load/Store 指令。

![[VLIW 数据冒险.png|2 发射 VLIW MIPS 处理器的流水线示意]]

#### Loop unrolling <br>循环展开

考虑下面的汇编指令序列：
```asm
I.1 >>> lp:     lw      $t0,    0       ($s1)
I.2 >>>         addu    $t0,    $t0,    $s2
I.3 >>>         sw      $t0,    0       ($s1)
I.4 >>>         addi    $s1,    $s1,    -4
I.5 >>>         bne     $s1,    $zero,  lp
```
显然这是一个用于将数组每个元素都加上一个偏移量的**循环**。编译器需要将这些指令打包成发射包，同时避免数据冒险。

由于程序第 1、2 行 `$t0`，第 2、3 行 `t0`，第 4、5 行 `$s1` 之间均存在**真实依赖 (RAW)**，因此编译器无法将这些指令打包在一个发射包内，最佳的调度结果为

```tx
| 周期  | Slot 1        | Slot 2        | 注 |
|:------|:--------------|:--------------|:---|
| 1     |               | I.1: `lw $t0, 0 ($s1)` |  |
| 2     | I.4: `addi $s1, $s1, -4` |  | I.2 所需 `$t0` |\
| | | | 尚未准备好 |
| 3     | I.2: `addu $t0, $t0, $s2` |  |  |
| 4     | I.5: `bne $s1, $zero, lp` | I.3: `sw $t0, 4 ($s1)` | 由于 I.4 提前，|\
| | | | I.3 增量有改动 |
```

这一打包方案效率较低，**IPC 仅为 1.25**，大量空指令被引入发射包中。为解决这一问题，编译器可以采用**循环展开 (loop unrolling)** 技术，将循环体展开多次，从而增加指令间的独立性。如将循环展开 4 次，得到
```asm
I.1 >>> lp:     lw      $t0,    0       ($s1)
I.2 >>>         lw      $t1,    -4      ($s1)
I.3 >>>         lw      $t2,    -8      ($s1)
I.4 >>>         lw      $t3,    -12     ($s1)
I.5 >>>         addu    $t0,    $t0,    $s2
I.6 >>>         addu    $t1,    $t1,    $s2
I.7 >>>         addu    $t2,    $t2,    $s2
I.8 >>>         addu    $t3,    $t3,    $s2
I.9 >>>         sw      $t0,    0       ($s1)
I10 >>> 		sw      $t1,    -4      ($s1)
I11 >>> 		sw      $t2,    -8      ($s1)
I12 >>> 		sw      $t3,    -12     ($s1)
I13 >>>         addi    $s1,    $s1,    -16
I14 >>>         bne     $s1,    $zero,  lp
```
即可得到更高效的打包方案

```tx
| 周期  | Slot 1        | Slot 2        | 注 |
|:------|:--------------|:--------------|:---|
| 1	    | I.13: `addi $s1, $s1, -16` | I.1: `lw $t0, 0 ($s1)` |  |
| 2     |               | I.2: `lw $t1, 12 ($s1)` | I.5 所需的 `$t0` |\
| | | | 尚未准备好 |
| 3     | I.5: `addu $t0, $t0, $s2` | I.3: `lw $t2, 8 ($s1)` |  |
| 4     | I.6: `addu $t1, $t1, $s2` | I.4: `lw $t3, 4 ($s1)` |  |
| 5     | I.7: `addu $t2, $t2, $s2` | I.9: `sw $t0, 16 ($s1)` |  |
| 6     | I.8: `addu $t3, $t3, $s2` | I.10: `sw $t1, 12 ($s1)` |  |
| 7     |               | I.11: `sw $t2, 8 ($s1)` |  |
| 8     | I.14: `bne $s1, $zero, lp` | I.12: `sw $t3, 4 ($s1)` |  |
```

这一方案的 **IPC 提升至 1.8**，显著提高了处理器的利用率。

### Branch prediction <br>分支预测技术

在 VLIW 体系结构中，**分支预测 (branch prediction)** 技术尤为重要，因为错误的分支预测会导致整个发射包的指令被浪费。

分支预测包括两种主要方法：
+ **静态分支预测 (static branch prediction)**：基于固定规则进行预测，例如总是预测向前跳转不发生，向后跳转发生。
+ **动态分支预测 (dynamic branch prediction)**：利用历史信息和模式识别进行预测，例如使用分支历史表 (Branch History Table, BHT) 来记录分支的过去行为。

## Superscalar Architecture <br>超标量体系架构 ^SuperscalarArchitecture

**超标量 (Superscalar, SS)** 是一种处理器设计方法，通过在硬件层面实现**动态多发射 (dynamic multiple issue)**，允许处理器在每个时钟周期内发射多条指令，从而更好利用程序的 ILP，提升整体性能。

### Register Update Unit (RUU) <br>寄存器更新单元




### Load/Store Queue (LSQ) <br>存储器访问队列



### Superscalar speedup measurement <br>超标量加速测量
