## 图像 token 化

ViT 把图像划分为固定大小 patch，将每个 patch 展平并线性映射为 token。若图像尺寸为 $H\times W$、patch 边长为 $P$，token 数为 $N=HW/P^2$。

token 加上位置编码后进入 Transformer encoder。分类可使用专门的 class token 或对所有 token 汇聚。

## 自注意力

对输入 $X$，有

$$
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V,
$$

$$
\operatorname{Attention}(Q,K,V)
=\operatorname{softmax}\left(\frac{QK^{\mathsf T}}{\sqrt{d_k}}\right)V.
$$

多头注意力在不同子空间建立关系，前馈网络对每个 token 独立变换，残差连接与 Layer Normalization 稳定深层训练。

## 层级与局部注意力

全局注意力的计算和存储随 token 数近似平方增长。PVT 逐级降低分辨率并建立金字塔，Swin Transformer 在局部窗口计算注意力，并通过 shifted windows 连接相邻窗口。

这类层级表示更适合检测和分割，因为下游任务需要多尺度空间特征。Deformable attention 则只访问少量参考点，降低高分辨率特征的成本。

> [!note] CNN 与 ViT 的归纳偏置
> CNN 强调局部连接和平移等变，ViT 更直接建立全局内容关系。数据规模、增强和架构设计会影响二者的样本效率，不能仅按模块名称判断优劣。

## 混合视觉骨干

ConvNeXt 等模型吸收了 Transformer 的宏观设计和训练方法，同时保留 convolution。现代骨干的差异不只在算子，还涉及 stage 划分、归一化、激活、kernel size 与优化策略。

> [!danger] 注意力图不是完整解释
> 单层权重只描述一次信息混合，最终输出还经过多层残差和非线性。可视化可辅助诊断，但不能单独证明因果贡献。

