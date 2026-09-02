## C++ 的抽象版图

### 从 C 到 C++

C++ 保留 C 的过程式计算能力，并通过类、对象生命周期、模板、标准库与异常机制增加更强的抽象边界。复习时不应把这些机制都归入面向对象，而应区分对象模型、泛型编程、库接口与失败传播。

### 三条并列主线

+ [[C++ 面向对象程序设计]]研究封装、类不变量、对象生命周期、继承与运行时多态。
+ [[C++ 泛型与标准库]]研究类型参数化、容器与迭代器，以及基于流的通用输入输出接口。
+ [[异常处理]]研究失败如何跨越函数边界传播，以及栈展开期间如何依靠 RAII 恢复资源不变量。

## 依赖与学习顺序

### 学习顺序

先学习类与对象生命周期，再学习继承和虚函数；模板与标准库与面向对象是并列的抽象方法。异常处理依赖对象析构与资源管理，因此应在掌握 RAII 后复习。

## 贯穿示例

```cpp
class ScoreSet {
public:
    void add(double score) { scores_.push_back(score); }

    double average() const {
        if (scores_.empty()) {
            throw std::logic_error("empty score set");
        }
        return std::accumulate(scores_.begin(), scores_.end(), 0.0)
             / scores_.size();
    }

private:
    std::vector<double> scores_;
};
```

`ScoreSet` 用类维护「所有成绩由对象自身管理」的不变量；`std::vector` 与迭代器来自泛型标准库；空集合无法求平均值时用异常传播失败。三种机制在一个程序中协作，但分别解决封装、通用存储和错误传播问题，因此在知识结构中应保持并列。
