# 内容方法与视觉教学原则

本课程采用 Olah-style-posts 的教学工程方法，但不是复刻任何单一网站。

## 叙事顺序

1. 从读者可以感受到的计算问题开始。
2. 先展示最小对象和最小反例，再引入术语。
3. 用一张只回答一个问题的图解释机制。
4. 再给出带维度、范数和假设的数学表达式。
5. 用可执行的 Python / MATLAB 小例子交叉验证。
6. 说明失败模式、适用边界和未验证事项。
7. 在主张附近提供可追溯的一手来源。

## 方法参考

- [Christopher Olah — Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)：借鉴渐进式视觉解释，不复制其图形、文字或网页实现。
- [Harvard NLP — The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)：借鉴代码与计算机制并排解释，不复制其代码、图形或样式。
- [Olah-style-posts Skill](https://github.com/1998x-stack/Olah-style-posts/blob/main/skills/olah-style-paper-posts/SKILL.md)：作为叙事、证据、MathML、SVG、浏览器 QA 和发布门禁的工程规范。

## 本课程的专属要求

数值线性代数的每张图都要表达矩阵形状、运算方向、误差来源或数据移动。不能把图形当作装饰；不能把理论 FLOPs、估计误差和实测性能混为一谈。
