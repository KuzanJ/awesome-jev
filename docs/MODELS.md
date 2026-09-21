# Models and inference implementations

[Back to Awesome Jev](../README.md)

Snapshot: September 21, 2026. This is an architectural reading guide based on public project documentation, not a benchmark leaderboard. Project names do not establish affiliation. A repository license does not automatically cover the base model, weights, or datasets.

## Compare by artifact, not by name

| Project | Main approach | Artifacts to inspect | Important boundary |
|---|---|---|---|
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | Existing model, candidate-logit scoring, shared state | Inference runners and measurements | Previously called OpenJev; not TypeSafe's model |
| [LitJev](https://github.com/zhengxuyu/litjev) | Qwen output-head scoring | Compatible server and examples | Default distributions are not calibrated |
| [Simple Jev](https://github.com/featherless-ai/simple-jev) | Existing language-model logits | Local server, prompt/scoring rules, RFDT tools | Project-specific API semantics; inspect the contract |
| [Reflex](https://github.com/kshetrajna12/reflex) | Cached state and isolated question branches | Runtime, calibration tools, browser demo | Browser and Python paths have different limits |
| [OpenJev](https://github.com/razorback16/openjev) | DiffusionGemma answer-slot readout | vLLM/MLX server and compatibility notes | Different project from SemIf; option limits differ from Jev |
| [Jeff](https://github.com/logan-markewich/jeff) | GLiFormer-backed decisions | Server, deployment code, benchmark report | Implements the interface using another model family |
| [jevmlx](https://github.com/bnsd55/jevmlx) | MLX candidate scoring | Local runtime and schema handling | Finite fields do not replace arbitrary generation |
| [JEVfire](https://github.com/kikoncuo/jevfire) | Parallel vLLM candidate scoring | Engine integration and recorded benchmarks | Shared-prefix benefits depend on workload and caching |
| [cu-Jev](https://github.com/dtunai/cu-Jev) | C/CUDA Qwen inference | Native engine and reference comparisons | A runtime implementation, not an official training reproduction |
| [Laya-MLX](https://github.com/mizorewww/laya-mlx) | MLX port of Laya | Converted checkpoints and parity measurements | Related through Laya; port fidelity is not task accuracy |
| [Decider](https://github.com/Mapika/decider) | Trained Qwen decision readouts | Weights, training, calibration, serving, evaluation | Compare the exact checkpoint and training stage |
| [Kev](https://github.com/jaredpalmer/kev) | Trained Qwen-based model family | Weights, recipe, frozen evaluation suites | Independent interpretation of public architectural ideas |
| [Laya](https://github.com/NandhaKishorM/laya) | Encoder-based typed decision models | English/multilingual checkpoints and fine-tuning notebook | Check language coverage and native context limits |
| [Luce](https://github.com/scienthoon/luce) | Teacher data, LoRA, decision heads | Data synthesis, training, evaluation, serving | Task-trained comparisons are not zero-shot comparisons |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | Small backbone and dynamic candidate heads | Game datasets, checkpoint, training, replay | Specialized game performance is not general-purpose parity |
| [Jevlike](https://github.com/vinnylarouge/jevlike) | Option attention over encoded context | Small-model training and visual examples | Educational independent design |
| [PlayJev](https://github.com/OmniJev/PlayJev) | Vision model with bounded action readout | Weights, imitation learning, DAgger, games | Closed-loop outcomes matter more than one-step accuracy |
| [PoorJev](https://github.com/rupeshpoojary9/poorjev) | NLI-based judgments and calibration | Local scoring and abstention experiments | Calibration is conditional on data and assumptions |
| [Eve RLCD](https://github.com/anthony-maio/eve-rlcd) | Independent calibration-training research | Training and evaluation artifacts | The RLCD name does not establish the official method |

## What to verify before comparing

1. **Decision contract:** question isolation, option limits, Score semantics, Noul semantics, and the definition of confidence.
2. **Training exposure:** frozen backbone, supervised tuning, RL stage, task-specific data, and held-out tasks.
3. **Probability quality:** Brier score, log loss, reliability plots, ECE with sample sizes, and risk versus coverage after abstention.
4. **Robustness:** option order, paraphrases, irrelevant context, missing correct answers, multilingual inputs, and adversarial content.
5. **Performance:** whole-request latency, p50/p95, cold start, caching, context length, question count, precision, hardware, and concurrency.
6. **Reproducibility:** pinned revisions, dataset permissions, executable scoring code, raw outputs, and an explicit boundary between demonstrations and tests.

The initial TypeSafe launch presented workflow-specific speed and cost comparisons. Those should not be transplanted onto arbitrary workloads or used to certify independent replicas. For open projects, author-reported results remain author-reported until independently reproduced.

## Name collisions

- `TheoLeeCJ/openjev` now resolves to **TheoLeeCJ/SemIf**.
- **razorback16/openjev** is a separate DiffusionGemma server.
- Other `openjev` / `open-jev` repositories are separate implementations, experiments, or task-specific projects. Always cite the owner.
- The GitHub organization **typesafe-ai** is the official source linked by TypeSafe documentation. Similar names alone do not establish official status.
