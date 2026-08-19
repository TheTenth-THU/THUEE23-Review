---
longform:
  format: scenes
  title: 现代计算机体系架构
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Overview
    - Evaluation of Computer
    - MIPS Architecture
    - Multiple Issue
    - Memory
    - - Cache
      - Virtual Memory
      - 存算一体
      - Disk
    - Interconnection
    - 多处理器与缓存一致性
    - GPU
    - Cloud Computation
  ignoredFiles: []
---
## 课程知识地图

现代计算机体系结构围绕「**如何利用有限硬件资源缩短程序执行时间**」展开。核心主线由性能量化、指令级并行、存储层次、系统级并行和规模化计算逐层递进。

```text
性能度量与功耗约束
        ↓
单发射流水线 → 多发射与乱序执行
        ↓
缓存 → 虚拟内存 → 外存与 I/O
        ↓
多处理器一致性 → GPU 吞吐计算
        ↓
仓库级计算机与云计算
```

## 处理器组织

+ [[Overview|体系结构概览]]：从状态机、指令执行和并行层次建立全局视角。
+ [[Evaluation of Computer|性能评估]]：用执行时间、CPI、加速比、功耗和可靠性评价设计。
+ [[MIPS Architecture|MIPS 处理器]]：比较单周期、多周期与流水线数据通路及其控制。
+ [[Multiple Issue|多发射处理器]]：讨论 VLIW、超标量、动态调度和控制预测。

## 存储与互连

+ [[Memory|存储器与存储层次]]：说明存储介质、局部性和层次化设计的共同规律。
    + [[Cache|缓存]]：地址映射、替换、写策略和平均访存时间。
    + [[Virtual Memory|虚拟内存]]：分页、页表、TLB 与缺页处理。
    + [[存算一体]]：在数据所在位置附近完成计算，缓解数据搬移瓶颈。
    + [[Disk|磁盘与 RAID]]：外存访问时间、阵列组织与可靠性。
+ [[Interconnection|互连与 I/O]]：总线仲裁、同步方式、中断和 DMA。

## 并行与规模化系统

+ [[多处理器与缓存一致性]]：共享存储多处理器、侦听／目录协议、MESI 和内存一致性。
+ [[GPU|GPU 架构]]：SIMT 执行、线程层次、访存合并和占用率。
+ [[Cloud Computation|仓库级计算机与云计算]]：规模扩展、PUE、服务目标、冗余和尾延迟。

> [!tip]
> 复习时先以 [[Evaluation of Computer|性能评估]] 中的执行时间与 AMAT 为统一量尺，再判断流水线、缓存、并行处理器或规模化系统分别优化了哪一项，以及引入了哪些额外代价。
