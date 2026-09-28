# Cross-method comparisons

[Home](../README.md) · [中文](evidence.zh-CN.md) · [Methods and experiments](paper-notes.md)

## Representations and search spaces

| Systems | Representation | Design consequence |
|---|---|---|
| [ViperGPT](https://arxiv.org/html/2303.08128v1) / [PyVision](https://arxiv.org/html/2507.07998v1) | Python over fixed perception APIs / dynamically written image tools | Flexibility extends from control flow to tool implementation; visual backbones and libraries also differ. |
| [SlideCoder](https://arxiv.org/html/2506.07964v1) / [Paper2Poster](https://arxiv.org/html/2505.21497v1) | Reference-conditioned code / content planning plus deterministic code generation | Reconstruction starts from supplied designs and assets; poster generation also selects information and allocates space. |
| [CAD-Recode](https://arxiv.org/html/2412.14042v2) / [Real2Code](https://arxiv.org/html/2406.08474v2) | Sketch-and-extrude operations / articulation relative to part bounding boxes | Recovered structure describes how a shape is constructed or how its parts move. |
| [Code as Policies](https://arxiv.org/abs/2209.07753) / [Eureka](https://arxiv.org/html/2310.12931v1) | Control policy / reward for policy learning | API composition acts directly; reward search incurs policy-training cost for each candidate. |
| [WorldCoder](https://arxiv.org/html/2402.12275v3) / [Code2World](https://arxiv.org/abs/2602.09856) | Transition and reward functions / next interface observation | Planning queries dynamics; interface prediction constructs an observation. |

Programs expose different optimization variables: a tool sequence, numerical parameters, an expression structure or a learned objective. This affects both the search space and the cost of candidate evaluation. Rendering a scene, fitting coefficients and training a control policy place substantially different work inside one evaluation.

## Feedback and component evidence

Runtime errors constrain program validity. Renders expose visual defects; task fitness selects useful behavior; proof checkers verify derivations of supplied statements. The following ablations separate several of these effects.

| Study | Controlled change | Finding and scope |
|---|---|---|
| [CodeAct, Table 3](https://arxiv.org/html/2402.01030v4) | Action representation under GPT-4-1106-preview | M3ToolEval: code 74.4%, JSON 52.4%, text 53.7%; tasks emphasize compositional tool use. |
| [MatPlotAgent, Table 2](https://arxiv.org/html/2402.11453v1) | Remove visual feedback | GPT-4 score falls from 61.16 to 53.44; direct generation scores 48.86. Reference-based GPT-4V evaluation on 100 tasks. |
| [CAD-Recode, Table 1](https://arxiv.org/html/2412.14042v2) | 160k DeepCAD examples → one million synthetic examples | DeepCAD/Fusion360 IoU rises from 80.7/67.6 to 92.0/87.8. Training source and scale change together. |
| [WorldCoder, Figures 3–5](https://arxiv.org/html/2402.12275v3) | Remove optimistic reachability constraints | Little effect in dense-reward Sokoban; substantial effect in sparse-reward and new-goal settings. |
| [LLM-SR, §5.1](https://arxiv.org/html/2404.18400v2) | Remove semantic descriptions or coefficient optimization | Oscillation 2 OOD NMSE rises from 3.81×10⁻⁵ to 7.10×10⁻³ or 0.378 respectively. |
| [ScienceAgentBench, Table 3](https://arxiv.org/html/2410.05080v1) | Add domain knowledge to Claude-3.5-Sonnet self-debugging | Best-of-three success rises from 32.4% to 34.3%, while valid execution falls from 92.2% to 86.3%. |

The GIF-MCTS comparison uses a [WorldCoder-v1-based baseline](https://arxiv.org/html/2405.15383v2). WorldCoder v3 supplies the experience-consistency and optimism formulation above; these comparisons concern different versions.

## Reuse and transfer

| Study | Shared or transferred object | Setting |
|---|---|---|
| [OpenHands-Versa](https://arxiv.org/abs/2506.03011) | Framework and tool environment | Software, assistant and enterprise task coverage |
| [Voyager](https://arxiv.org/html/2305.16291v2) | Executable skills indexed by description | New tasks under shared Minecraft rules and Mineflayer APIs |
| [RoboPro](https://arxiv.org/abs/2501.04268) | Trained program generator | Original / renamed / refactored APIs: 42.7 / 42.7 / 40.4% on nine RLBench tasks, 25 episodes each |
| [GenSim2](https://arxiv.org/abs/2410.03645) | Policies trained with generated demonstrations | Real / simulated / mixed training: 36.3 / 42.5 / 57.5%; ten real or 100 simulated demonstrations per task |
| [JanusCoder](https://arxiv.org/abs/2510.23538) | Jointly trained visual-program model | Data-removal ablations show gains and interference; replacement of removed samples and resulting update counts are unspecified |

Framework coverage tests whether a system supports different task families. Skill reuse transfers executable artifacts. Joint training transfers parameter updates. The experimental interventions differ accordingly.

## Evaluation targets

**Planning.** With Llama-3-70B and 50 calls, [GIF-MCTS](https://arxiv.org/html/2405.15383v2) improves model accuracy on simplified RTFM while normalized planning return remains −0.11. This setting fixes the manual and immobilizes monsters. Accurate transitions and useful planning are separately measured outcomes.

**Formal proving.** [DeepSeek-Prover-V2](https://arxiv.org/html/2504.21801v1) reaches 82.4% pass@32 and 88.9% pass@8192 with its 671B CoT model on MiniF2F-test. Lean checks the supplied formal statement; statement formalization is a separate step. [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y)'s IMO setting includes human formalization and extended test-time computation.

**Scientific discovery.** [LLM-SR](https://arxiv.org/html/2404.18400v2) measures fitting and extrapolation; [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) evaluates constructions and heuristics through supplied fitness functions; [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) adds physical measurements. Each provides evidence for a different scientific output.
