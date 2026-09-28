# 跨方法比较

[中文首页](../README.zh-CN.md) · [English](evidence.md) · [方法与实验](paper-notes.zh-CN.md)

## 程序表示与搜索空间

| 方法 | 表示方式 | 设计差异 |
|---|---|---|
| [ViperGPT](https://arxiv.org/html/2303.08128v1) / [PyVision](https://arxiv.org/html/2507.07998v1) | Python 组合固定感知 API / 即时编写图像工具 | 灵活性从控制流扩展到工具实现；视觉骨干和基础库也有差别。 |
| [SlideCoder](https://arxiv.org/html/2506.07964v1) / [Paper2Poster](https://arxiv.org/html/2505.21497v1) | 参考设计驱动代码生成 / 内容规划加固定代码生成器 | 设计还原已有布局与资产；海报生成还需取舍信息、分配版面。 |
| [CAD-Recode](https://arxiv.org/html/2412.14042v2) / [Real2Code](https://arxiv.org/html/2406.08474v2) | 草图—拉伸操作 / 相对部件包围盒的关节参数 | 重建结构分别描述形状的构造方式与部件的运动方式。 |
| [Code as Policies](https://arxiv.org/abs/2209.07753) / [Eureka](https://arxiv.org/html/2310.12931v1) | 控制策略 / 用于策略学习的奖励 | API 组合直接执行动作；奖励搜索的每个候选包含策略训练成本。 |
| [WorldCoder](https://arxiv.org/html/2402.12275v3) / [Code2World](https://arxiv.org/abs/2602.09856) | 状态转移与奖励函数 / 下一界面观察 | 规划查询动力学，界面预测构造观察。 |

程序暴露的优化变量可以是工具序列、数值参数、表达式结构或学习目标。这同时影响搜索空间和候选评价成本：场景渲染、系数拟合与控制策略训练，在一次评价中承担的工作量差别很大。

## 反馈与组件作用

运行错误约束程序有效性，渲染图暴露视觉缺陷，任务指标选择有效行为，形式检查器验证给定命题的推导。以下消融分别检验其中部分作用。

| 工作 | 对照变量 | 发现与条件 |
|---|---|---|
| [CodeAct，表3](https://arxiv.org/html/2402.01030v4) | GPT-4-1106-preview 下的动作表示 | M3ToolEval：代码74.4%、JSON 52.4%、文本53.7%；任务强调工具组合。 |
| [MatPlotAgent，表2](https://arxiv.org/html/2402.11453v1) | 移除视觉反馈 | GPT-4 评分从61.16降至53.44，直接生成为48.86；100个任务，GPT-4V 对照参考图评分。 |
| [CAD-Recode，表1](https://arxiv.org/html/2412.14042v2) | 16万 DeepCAD 样本 → 100万合成样本 | DeepCAD/Fusion360 IoU 从80.7/67.6升至92.0/87.8；训练数据来源与规模同时变化。 |
| [WorldCoder，图3—5](https://arxiv.org/html/2402.12275v3) | 移除乐观可达性约束 | 对稠密奖励 Sokoban 影响较小，对稀疏奖励和新目标设置影响明显。 |
| [LLM-SR，第5.1节](https://arxiv.org/html/2404.18400v2) | 移除问题语义或系数优化 | Oscillation 2 的 OOD NMSE 从3.81×10⁻⁵分别增至7.10×10⁻³或0.378。 |
| [ScienceAgentBench，表3](https://arxiv.org/html/2410.05080v1) | 为 Claude-3.5-Sonnet 自调试增加领域知识 | 三次尝试选优，任务成功率32.4%→34.3%，可执行率92.2%→86.3%。 |

GIF-MCTS 的对照采用 [WorldCoder v1 实现](https://arxiv.org/html/2405.15383v2)；上述经验一致性与乐观约束来自 WorldCoder v3，两组比较对应不同版本。

## 复用与迁移

| 工作 | 共享或迁移的对象 | 实验设置 |
|---|---|---|
| [OpenHands-Versa](https://arxiv.org/abs/2506.03011) | 框架与工具环境 | 软件、通用助理和企业任务覆盖 |
| [Voyager](https://arxiv.org/html/2305.16291v2) | 按描述索引的可执行技能 | 共享世界规则与 Mineflayer API 下的新任务 |
| [RoboPro](https://arxiv.org/abs/2501.04268) | 训练后的程序生成器 | 原始／改名／重构 API：42.7／42.7／40.4%；9个 RLBench 任务，每项25次 |
| [GenSim2](https://arxiv.org/abs/2410.03645) | 用生成示范训练的策略 | 真实／仿真／混合训练：36.3／42.5／57.5%；每任务10条真实或100条仿真示范 |
| [JanusCoder](https://arxiv.org/abs/2510.23538) | 联合训练的视觉程序模型 | 数据移除消融同时出现收益与干扰；移除后的样本补齐与更新次数未明确 |

框架覆盖考察系统支持的任务范围，技能复用传递可执行产物，联合训练通过参数更新影响其他任务。三者对应的干预变量和对照条件各不相同。

## 评价目标

**规划。** 使用 Llama-3-70B、50次调用时，[GIF-MCTS](https://arxiv.org/html/2405.15383v2) 在简化 RTFM 上提高了模型准确率，归一化规划回报仍为−0.11；该设置固定规则手册并禁止怪物移动。转移预测与有效规划是分别测量的结果。

**形式证明。** [DeepSeek-Prover-V2](https://arxiv.org/html/2504.21801v1) 的671B CoT 模型在 MiniF2F-test 上达到82.4% pass@32 和88.9% pass@8192。Lean 检查输入的形式化命题，命题形式化是独立步骤。[AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) 的 IMO 评价包含人工形式化与较长的测试时计算。

**科学发现。** [LLM-SR](https://arxiv.org/html/2404.18400v2) 评价方程拟合与外推；[FunSearch](https://www.nature.com/articles/s41586-023-06924-6) 通过给定适应度函数评价数学构造与启发式算法；[Coscientist](https://www.nature.com/articles/s41586-023-06792-0) 引入真实化学实验测量。各自的证据对应不同的科学产物。
