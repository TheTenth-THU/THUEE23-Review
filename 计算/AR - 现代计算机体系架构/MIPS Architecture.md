## Basic MIPS Architecture <br>基础 MIPS 架构

**MIPS (microprocessor without interlocked pipeline stages)** 是一种经典的 RISC 处理器架构，最早由斯坦福大学的 John L. Hennessy 教授领导的团队在 1981 年设计。MIPS 架构以其简洁、高效和易于实现流水线而闻名，广泛应用于嵌入式系统、网络设备和高性能计算等领域。

以下，考虑简化的 MIPS 指令集，包括以下三类指令：
+ 访存指令：`lw` (load word)、`sw` (store word)；
+ 算术指令：`add`、`sub`、`and`、`or`、`slt` (set on less than)；
+ 控制指令：`beq` (branch if equal)、`j` (jump)。

一般地，实现一个 MIPS 处理器需要：
+ 一个**程序计数器 (program counter, PC)**，用于提供下一条将要执行的指令的地址；
+ 一个**寄存器堆 (register file)**，包含 32 个通用 32 位寄存器；
+ 一套**取指令**机制；
+ 一套**译码**机制，将指令译码为相应的控制信号；
+ 一套**执行**逻辑和各种**算术逻辑单元 (ALU)**，用于执行指令。

### Single Cycle MIPS Processor <br>单周期 MIPS 处理器

![[单周期处理器.png]]

### Multiple Cycle MIPS Processor <br>多周期 MIPS 处理器

![[多周期处理器.png]]

### Pipelined MIPS Processor <br>流水线 MIPS 处理器

![[流水线处理器的控制信号传递.png|流水线处理器的控制信号传递]]

![[流水线处理器的数据冒险.png|流水线处理器的数据冒险]]

![[流水线处理器的数据冒险解决.png|流水线处理器的数据冒险解决]]

![[流水线处理器的 Load-Use 冒险解决.png|流水线处理器的 Load-Use 冒险解决]]

## SuperPipelined MIPS Architecture <br>超流水线 MIPS 架构

### Overview <br>概述

增加流水线深度可实现更短的时钟周期，从而提升时钟频率和处理器性能。然而，过深的流水线也会带来一些挑战，例如：
+ 所需的数据转发、冒险处理硬件更复杂；
+ 流水线锁存器的延迟开销增加，建立时间和保持时间会占据时钟周期中更大比例；
+ 时钟频率加快导致时钟偏移问题更加严重。

超流水线处理器的指令延迟高于超标量处理器，在存在数据依赖时会降低性能；而超标量处理器更易受资源冲突影响，但也可通过硬件方案解决。