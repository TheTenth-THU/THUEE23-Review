## 训练闭环

PyTorch 实验由数据、模型、损失、优化器、训练循环和评估组成。设备、随机种子、数据版本和超参数应与结果一起记录。

`Dataset` 定义单个样本的读取与变换，`DataLoader` 负责 batching、shuffle 和并行加载。训练集可使用随机增强，验证与测试变换必须确定且保持一致。

## 模型与张量

模型通常继承 `torch.nn.Module`，参数由子模块自动注册。输入张量应明确 batch、channel 和空间或时间维度，维数错误比公式错误更常见。

自动微分会记录需要梯度的运算。推理阶段使用 `torch.no_grad()`，避免构建计算图并降低显存占用。

## 标准训练骨架

```python
model.train()
for inputs, targets in train_loader:
    inputs, targets = inputs.to(device), targets.to(device)
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

model.eval()
with torch.no_grad():
    for inputs, targets in valid_loader:
        outputs = model(inputs.to(device))
```

`zero_grad()` 清除上一步累积梯度，`backward()` 计算梯度，`step()` 更新参数。若要进行 gradient accumulation，应有意控制清零频率，并按累积步数处理损失尺度。

> [!danger] `train()` 与 `eval()` 不只是性能开关
> 二者会改变 dropout 和 Batch Normalization 的行为。验证时忘记 `eval()`、训练时忘记恢复 `train()`，都会造成隐蔽的结果偏差。

## 初始化、损失与优化器

初始化应匹配激活函数，损失应匹配输出语义。`CrossEntropyLoss` 接受未归一化 logits，并在内部计算 LogSoftmax；若先手动 Softmax，可能造成数值和梯度问题。

优化器只应接收需要训练的参数。迁移学习冻结或解冻层后，要确认 `requires_grad` 和 optimizer 参数组同步更新。

## 评估与保存

每轮记录训练损失、验证损失、任务指标和学习率。保存 checkpoint 时至少包含模型参数、优化器状态、epoch 与配置；最终模型应按预先确定的验证准则选择，而不是依据测试集。

> [!tip] 可复现检查
> 固定随机种子只能降低随机性，GPU 算子、并行加载和库版本仍可能产生差异。重要结果应报告多次运行的均值与离散程度。

