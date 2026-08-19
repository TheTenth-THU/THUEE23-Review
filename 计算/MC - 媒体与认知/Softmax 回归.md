## 多分类概率模型

对 $K$ 个互斥类别，线性层产生 logits

$$
z_k=\v w_k^{\mathsf T}\v x+b_k.
$$

**Softmax 回归**将 logits 归一化为条件概率：

$$
p(y=k\mid\v x)=\frac{\e^{z_k}}{\sum_{j=1}^K\e^{z_j}}.
$$

为避免指数溢出，计算时应先令 $z_k\leftarrow z_k-\max_j z_j$。平移所有 logits 不改变概率，因此参数存在等价表示。

## 交叉熵损失

若标签的 one-hot 向量为 $\v y$，单样本负对数似然为

$$
\ell=-\sum_{k=1}^K y_k\log p_k.
$$

Softmax 与交叉熵合并后，对 logit 的梯度具有简洁形式

$$
\frac{\partial\ell}{\partial z_k}=p_k-y_k.
$$

这表示预测概率高于目标的类别受到向下修正，真实类别受到向上修正。$K=2$ 时，选择一个参考类即可化为 sigmoid logistic 回归。

> [!note] 决策边界仍然是线性的
> Softmax 的非线性只把 logits 映射为概率。若 logits 直接来自原始特征的线性变换，任意两类的等概率边界仍是超平面；深度网络依靠前面的非线性表示得到复杂边界。

## 温度与校准

温度缩放使用 $p_k\propto\exp(z_k/T)$。$T>1$ 使分布更平滑，$T<1$ 使分布更尖锐；在知识蒸馏中，高温能够暴露类别间的相似关系。

高准确率不等于概率可靠。可用可靠性图、Expected Calibration Error 或负对数似然评价校准，并仅在验证集上拟合温度。

> [!danger] Softmax 不能识别所有未知样本
> 概率和恒为 $1$，即使输入远离训练分布，模型也可能给出高置信度。开放集任务需要额外的拒识、能量分数或分布外检测机制。

## 类别不平衡

类别频率差异显著时，可使用类别加权交叉熵、重采样或 focal loss。评价时应同时观察每类 Recall、macro-F1 与混淆矩阵，不能只看总体准确率。

