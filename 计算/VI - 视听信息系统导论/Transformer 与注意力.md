## 注意力机制

attention 根据 query 与 keys 的相关性，对 values 加权汇聚。缩放点积形式为

$$
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^{\mathsf T}}{\sqrt{d_k}}+M\right)V.
$$

cross-attention 的 query 与 key／value 来自不同序列，可用于机器翻译源—目标对齐；self-attention 三者来自同一序列，直接建立任意位置关系。

## Transformer block

输入先加入位置表示，再经过 multi-head self-attention、残差连接、Layer Normalization 和逐位置 feed-forward network。多头机制让模型在不同投影子空间并行组合关系。

encoder 可使用双向上下文，decoder 的 causal mask 把未来位置设为不可见，保证自回归分解。padding mask 则避免把补齐 token 当作内容。

> [!note] 位置信息不可省略
> 不带位置表示的 self-attention 对 token 排列等变，无法区分相同元素的不同顺序。可使用绝对 embedding、相对位置偏置或旋转位置编码。

## 与 RNN 的比较

Transformer 在训练时可并行处理各位置，任意两 token 的依赖路径短；RNN 按时间递推，具有强序列归纳偏置和较低的单步状态存储。标准 attention 的 $n\times n$ 矩阵使显存与计算随长度近似平方增长。

局部、稀疏或线性 attention 可降低长序列成本，自回归推理还可用 KV cache 复用历史 key 与 value。

## 表示与生成

encoder 表示适合分类和抽取，decoder 适合条件或无条件生成，encoder–decoder 适合源到目标转换。相同算子因 mask、训练目标和数据而形成不同能力。

> [!danger] attention 不等于解释
> 权重只描述某一层的信息汇聚，后续残差与非线性仍会改变输出。解释结论需要扰动、梯度或因果实验等多种证据交叉验证。

