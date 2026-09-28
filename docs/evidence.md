# What the evidence supports

[Home](../README.md) · [Taxonomy](taxonomy.md) · [Reading paths](reading-guide.md)

The strongest version of this collection's thesis is not that every task is secretly software engineering. It is that generating and revising programs gives models access to a large collection of precise, composable and testable operations. The supporting systems differ in what they generate, what is supplied externally, and what counts as success.

## What code changes, in concrete systems

| System | Generated or manipulated object | Executor / external capabilities | Feedback and interpretation |
|---|---|---|---|
| [ViperGPT](https://arxiv.org/abs/2303.08128) | Python that calls visual APIs | Python plus pretrained perception models | Program execution composes existing expertise; it does not replace perception |
| [MatPlotAgent](https://arxiv.org/abs/2402.11453) | Scientific plotting code | Plotting libraries and a visual critic | Runtime and visual feedback can improve charts; visual scores do not certify scientific meaning |
| [SlideCoder](https://arxiv.org/abs/2506.07964) | `python-pptx` code and assembled fragments | Reference design, separate picture assets and API documentation | Execution repairs and layout evaluation concern a single-slide reconstruction setting |
| [Paper2Poster](https://arxiv.org/abs/2505.21497) | Content and layout decisions | A deterministic code generator plus visual critique | Useful programmatic output, but not unrestricted model-written Python; model readers are not human learning studies |
| [CAD-Recode](https://arxiv.org/abs/2412.14042) | CadQuery construction programs | Geometry encoder and CAD kernel | Geometric similarity and editability do not uniquely recover the original design history |
| [Code as Policies](https://arxiv.org/abs/2209.07753) | Hierarchical policies and helper functions | Provided perception and low-level control APIs | Compositional planning is distinct from acquiring all motor capabilities |
| [Eureka](https://arxiv.org/abs/2310.12931) | Reward functions | Simulator and reinforcement-learning training | Training outcomes improve the next reward; the trained policy supplies the final motor behavior |
| [WorldCoder](https://arxiv.org/abs/2402.12275) | Transition and reward programs | Interaction data and a planner | A model must be useful for planning, not merely fit observed transitions |
| [LeanDojo](https://arxiv.org/abs/2306.15626) | Formal tactics | Lean, retrieved premises and a formal library | Proof states give precise local feedback; the target statement must still represent the intended problem |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | Functions generating constructions or heuristics | Human-defined skeleton and automatic evaluator | Search can find new valid constructions without proving global optimality |
| [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) | Code and experiment operations | Documentation, analysis tools and laboratory automation | Physical measurements add evidence beyond executable simulation |

These comparisons explain a recurring advantage: an intermediate program can be edited, rerun, combined and checked. They also identify where progress actually comes from: a stronger model, a better interface, a domain-specific executor, a better evaluator, additional search, or human problem design.

## Coverage, reuse and transfer

| Claim | Relevant evidence | Limit |
|---|---|---|
| The same framework handles different task families | [OpenHands-Versa](https://arxiv.org/abs/2506.03011) evaluates software, assistant and enterprise tasks | Multi-task coverage does not establish that training or skills from one domain improved another |
| Programs from earlier tasks help later tasks | [Voyager](https://arxiv.org/abs/2305.16291) stores executable skills and evaluates reuse | Shared Minecraft semantics and APIs constrain the transfer setting |
| A policy generator adapts to changed interfaces | [RoboPro](https://arxiv.org/abs/2501.04268) tests renamed/refactored APIs | Provided APIs and a single real robot platform are not cross-hardware zero-adaptation |
| Generated data help physical robot policies | [GenSim2](https://arxiv.org/abs/2410.03645) compares real, synthetic and combined demonstrations | Different demonstration counts mean it is not an equal-data comparison |
| Joint training transfers across program tasks | [JanusCoder](https://arxiv.org/abs/2510.23538) removes data groups and measures other tasks | Some metrics improve after removing algorithm data; replenishment of removed samples is not specified |
| Improved robot software helps new robot tasks | [Learning and Transferring Closed-Loop Robot Software](https://arxiv.org/abs/2609.19906) explicitly compares no references, initial source code and optimized source code | Newly included, **abstract-screened**. The abstract reports target-task comparisons and some negative cases; protocol and compute controls need a full-text audit |
| A single learned mechanism transfers broadly across vision, robotics, proofs and science | No sufficiently matched cross-domain experiment established by the sources examined here | An open research question; shared use of code is not that experiment |

The September robot-software paper is a useful update to the research question: direct program-experience transfer is not absent. The remaining issue is how far it carries under controlled changes in tasks, interfaces and compute. We retain the paper's reading-depth limitation rather than turning an abstract into an audited result.

## Numerical results need their experimental conditions

This is a set of protocol reminders, not a cross-paper leaderboard. Most entries below inherit a methods/results check from **2026-09-12/13**; they are not newly reproduced experiments.

| Source | Result / contrast | Conditions to preserve |
|---|---|---|
| [CodeAct](https://arxiv.org/abs/2402.01030) | 74.4% code vs 52.4% JSON / 53.7% text on M3ToolEval | Same GPT-4-1106 comparison; not universal superiority for every model/task |
| [OpenHands-Versa](https://arxiv.org/abs/2506.03011) | GAIA 37.21 → 51.16 | Claude 3.7; test split, pass@1; 60-step limit; final-answer extraction; not OSWorld desktop evaluation |
| [MatPlotAgent](https://arxiv.org/abs/2402.11453) | 48.86 → 61.16 | A 0–100 GPT-4V visual score, not success percentage; 100 tasks and up to three code-debug attempts |
| [JanusCoder](https://arxiv.org/abs/2510.23538) | Data-removal ablations | Three epochs, batch 128; replacement of deleted data and resulting update-count controls are not specified |
| [RoboPro](https://arxiv.org/abs/2501.04268) | 42.7 / 42.7 / 40.4% for original / renamed / refactored APIs | Nine RLBench tasks, 25 episodes per task; real robot evaluation is a separate setting |
| [GenSim2](https://arxiv.org/abs/2410.03645) | 36.3 / 42.5 / 57.5% for real / sim / combined training | Ten real or 100 simulated demonstrations per task; eight real tasks, ten evaluation episodes each |
| [DeepSeek-Prover-V2](https://arxiv.org/abs/2504.21801) | 82.4 / 88.9% | 671B CoT, MiniF2F-test; pass@32 vs pass@8192, not matched inference cost |
| [ScienceAgentBench](https://arxiv.org/abs/2410.05080) | 86.3% executable vs 34.3% task success | Claude 3.5 with domain knowledge and self-debugging; best of three attempts |

The source data retain additional notes on evaluation, budgets and human roles. A missing cost field means the collection has not verified it; it does not mean the cost was zero.

## Formal and scientific confirmation

Numerical agreement, a valid construction, a counterexample, a conjecture, an informal proof, a checked formal proof and an independently repeated physical experiment are different products. They are not one universal ladder: a physical experiment does not replace a mathematical proof, and a proof checker cannot establish that a chemical measurement was made correctly.

[AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) illustrates how formal feedback can support training and test-time adaptation. Its IMO evaluation includes human formalization and extended inference time. [AlphaEvolve](https://arxiv.org/abs/2506.13131) illustrates broad program search with automatic evaluators, whose task definitions and objectives remain crucial. Neither result licenses attributing every component's capability to the code model alone.

## Recent world-model release checks

The following availability notes are **snapshots checked on 2026-09-13**, not claims about release state today. They should be rechecked before reproduction.

- [Programmable World Model](https://arxiv.org/abs/2609.10540): the [pinned repository](https://github.com/AlayaLab/PWM/tree/f1f1ece42e4df8ba7400da0af37d4f0f538fe442) listed inference code and pretrained weights as pending. Its reported visible-count/state checks do not cover all physics or identity consistency.
- [Code World Model](https://arxiv.org/abs/2608.25927): the [pinned environment document](https://github.com/buaacyw/code-world-model/blob/17fa82ba2fb8168aa0d30fc51a1d1d0ebbc9180b/ENVIRONMENT.md) explains that upstream proxy generation depends on a non-redistributable game-code foundation. Released video inference, LoRA and condition examples do not expose the complete upstream coding-agent workflow.

## The contribution this survey can make

[Beyond NL2Code](https://arxiv.org/abs/2606.15932) already covers many multimodal program tasks and asks for matched-size transfer controls. [Code as Agent Harness](https://arxiv.org/abs/2605.18747) already includes formal proving, scientific applications and evaluator limitations. A useful survey should acknowledge this overlap and then explain domain histories, compare actual experimental conditions, and make clearer judgments about the responsibility of code. A broader list is a starting point; those comparisons are the substance.

中文提示：本页最值得保留的判断是“共同方法已有证据，普遍跨域迁移仍需具体检验”。不要因为同一套系统处理多类任务，就把它写成训练迁移；也不要因为生成代码可以运行，就把它写成任务、科学或物理结果已正确。
