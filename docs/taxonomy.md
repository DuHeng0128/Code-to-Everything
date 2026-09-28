# How this collection is organized

[Home](../README.md) · [中文目录](../README.zh-CN.md) · [Evidence](evidence.md)

The central question is concrete: **what becomes possible when a model can write, edit and execute programs beyond ordinary software development?** Domains are the main navigation because a reader looking for robot policies should not first need to learn a new conceptual vocabulary. Within each domain, the subsections separate different tasks and different responsibilities of code.

## One primary home, several connections

Every record has exactly one `domain` and one `subcategory`. This keeps counts and bibliography exports consistent. `related_domains` records useful connections without duplicating the paper. FunSearch is primarily under scientific and algorithmic discovery, with mathematics as a related domain; Code2World is under world models, with digital tasks as a related domain.

| Primary area | What the grouping separates | A useful comparison |
|---|---|---|
| Vision | Reasoning programs, editable graphics, multimodal code models | [ViperGPT](https://arxiv.org/abs/2303.08128) orchestrates perception; [JanusCoder](https://arxiv.org/abs/2510.23538) trains visual-program generation |
| Media | Audio workflows, video/animation, documents | [WavJourney](https://arxiv.org/abs/2307.14335) compiles a constrained script; [WavCraft](https://arxiv.org/abs/2403.09527) generates tool-using programs |
| Spatial | Recovering structure, CAD operations, scene editing | [Real2Code](https://arxiv.org/abs/2406.08474) recovers articulation; [CAD-Recode](https://arxiv.org/abs/2412.14042) recovers construction programs |
| Digital | Executable actions, browser/desktop interaction, task evaluation | [CodeAct](https://arxiv.org/abs/2402.01030) studies action representations; [OSWorld](https://arxiv.org/abs/2404.07972) tests desktop tasks |
| Robotics | Policies, reusable skills, reward/simulation/data generation | [Code as Policies](https://arxiv.org/abs/2209.07753) writes policies; [Eureka](https://arxiv.org/abs/2310.12931) writes rewards used to train policies |
| Worlds | Transition programs, observable interfaces, persistent state/rendering | [WorldCoder](https://arxiv.org/abs/2402.12275) predicts transitions; [Code2World](https://arxiv.org/abs/2602.09856) generates a renderable next observation |
| Mathematics | Program-aided computation, formal proof, research systems | [PAL](https://arxiv.org/abs/2211.10435) executes computations; [LeanDojo](https://arxiv.org/abs/2306.15626) interacts with a proof assistant |
| Science | Program search, equations, research workflows, evaluation | [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) searches constructions; [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) connects to physical experiments |
| Foundations | Synthesis, feedback, tools and libraries | [DreamCoder](https://arxiv.org/abs/2006.08381) accumulates abstractions; [Voyager](https://arxiv.org/abs/2305.16291) accumulates executable skills |
| Surveys | Prior maps and competing explanations | [Beyond NL2Code](https://arxiv.org/abs/2606.15932) and [Code as Agent Harness](https://arxiv.org/abs/2605.18747) overlap substantially with this project's questions |

## What qualifies for the main collection?

A method belongs when a model generates, edits, selects or executes a program that materially advances the target task. The program may be Python, JavaScript, a CAD sequence, a graphics DSL, a reward function, a transition function, or a formal proof. One-shot generation and iterative agents are both relevant, but they should not be described as the same architecture.

Code merely being present in the implementation is insufficient. A VLA that directly predicts actions is a useful **Comparison**, not a code-generating policy. A benchmark belongs because it measures a relevant capability, not because it is itself an agent. Structured function calls and fixed compilation pipelines can illuminate the boundary; their notes must identify who actually produces the executable program.

## Two distinct labels: contribution and reading depth

| Field | Values | Interpretation |
|---|---|---|
| `kind` | method, benchmark, background, comparison, survey | Why the entry is included |
| `reading_depth` | abstract, sections | How deeply its original source has been examined for this collection |
| `program_role` | Plain-language descriptor | The task that code performs; not a claim that the whole system is autonomous |
| `milestone` | true/false, with a written reason | An editorial anchor that explains a turning point |
| `checked_on` | Date | When the recorded source/claim was checked, not a claim that every link was re-tested |

**K** means selected full-text methods, experiments or limitations were examined. It does not mean every appendix was read or the system was reproduced. **A** entries are useful pointers whose detailed experimental claims still require reading. A historical milestone can be A: its conceptual role is clear, while this collection has not audited all of its experiments.

Milestone selection should reflect a concrete shift: a new role for programs, a revealing controlled comparison, a reusable interface, or a result that changes the scope of credible application. A recent release, high score or catchy title alone is insufficient. This is why recent world-model and robot-system preprints are included without automatically being labeled milestones.

## Preserve differences that matter

- **A generated program versus a compiler output.** PosterAgent plans content and layout, while a deterministic component generates code. That is different from SlideCoder directly generating `python-pptx` programs.
- **An acting policy versus training code.** Eureka's code supplies rewards; the downstream trained policy executes robot motion.
- **A transition model versus an image renderer.** A useful rendered frame does not establish a correct state transition model.
- **Coverage versus transfer.** Evaluating the same framework on several tasks differs from carrying learned parameters or useful programs from one task to another.
- **Execution versus correctness.** Rendering, passing tests, proving a formal statement, and reproducing a physical experiment answer different questions.

These distinctions are developed with sources in [evidence comparisons](evidence.md). They are also the reason this index is organized by tasks first, rather than forcing every paper into one identical agent loop.

## Dates and publication claims

Sort by first public release, normally arXiv v1. For inherited records whose exact day is unavailable, retain month precision. Publisher first-online dates can differ from the volume year; FunSearch and AlphaProof retain both through their date/year fields. Preprint and publication versions remain one record.

Conference names in inherited metadata may come from authors' arXiv comments and are labeled accordingly. The README does not turn these into acceptance badges. Use a proceedings entry, publisher page or explicit acceptance statement before claiming a formal venue. Unknown metadata stays empty.
