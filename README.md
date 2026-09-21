# Awesome Jev

Open models, libraries, tools, and applications for [Jev](https://typesafe.ai/) and System One decisions.

**76 featured projects · 1,219 repositories indexed · Updated September 21, 2026**

Start with the projects below, or browse **806 licensed repositories** in the full catalog. Projects with unclear licensing and those awaiting review are listed separately.

**[Browse all projects](catalog/README.md)** · [Compare implementations](docs/MODELS.md) · [References](docs/SOURCES.md) · [Contribute](CONTRIBUTING.md)

## What is Jev?

[TypeSafe introduced Jev on September 15, 2026](https://typesafe.ai/blog/introducing-system-one-models-and-jev) as its first public **System One model**: software supplies state and bounded questions, and receives typed decisions with probabilities. The name System One draws on fast, intuitive judgments; Jev refers to Jevons and the idea that cheaper intelligence enables more uses.

```text
state + question + allowed answers
                |
         decision model
                |
    typed answer + probabilities
                |
     application-owned control flow
```

The [official interface](https://docs.typesafe.ai/introduction) exposes:

| Primitive | Question | Returned information |
|---|---|---|
| Choice | Which allowed option fits? | Selected option, option probabilities, confidence |
| Score | Where does this fall on a defined rubric? | Score, level probabilities, confidence |
| Noul | Is this statement true? | A value from 0 to 1 |

Questions should be atomic. Code combines judgments, applies thresholds, and performs exact arithmetic. Jev does not generate arbitrary prose. The public product description names a new architecture, parallel sampling, and **Reinforcement Learning for Calibrated Decisions (RLCD)**; it does not provide enough detail to establish that any independent implementation reproduces the original model.

Read the [official confidence definition](https://docs.typesafe.ai/confidence) and [known failure modes](https://docs.typesafe.ai/model-jaggedness/jev-1.13). Schema validity does not imply a correct decision. Confidence is a statistic derived from a distribution, not automatically the probability that an answer is correct. Independent implementations may define these fields differently.

## Project types

| Artifact | What is open | How it relates to Jev |
|---|---|---|
| Official SDK or adapter | Client / integration code | Usually calls hosted Jev, or substitutes another provider |
| Local inference engine | Runtime and interface implementation | Scores bounded choices using existing model weights |
| Trained decision model | Some combination of code, weights, data, and recipe | Independently trains for a similar decision interface |
| Application or agent integration | Application code | Uses Jev as one component; often still requires a hosted API |
| Evaluation project | Harness, cases, or recorded results | Measures a specific task or property, not universal superiority |

API compatibility does not guarantee matching behavior. Check whether a project provides inference code, weights, training data, and calibration results.

## Where to start

- **Understand the product:** [launch announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [API introduction](https://docs.typesafe.ai/introduction), then [limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13).
- **Study inference:** [SemIf](https://github.com/TheoLeeCJ/SemIf), [mini-Jev](https://github.com/r-ms/mini-jev), and [Simple Jev](https://github.com/featherless-ai/simple-jev).
- **Study training:** [Decider](https://github.com/Mapika/decider), [Kev](https://github.com/jaredpalmer/kev), [Laya](https://github.com/NandhaKishorM/laya), and [Luce](https://github.com/scienthoon/luce).
- **Build a workflow:** [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast), [DocJev](https://github.com/jerryjliu/docjev), and [Jevwire](https://github.com/Brainwires/jevwire).
- **Compare results:** [JevBench](https://github.com/fstandhartinger/jevbench) and [Jev Calibration Audit](https://github.com/jujumilk3/jev-calibration-audit); examine labels, option ordering, abstention, splits, and measurement conditions.

## Featured projects

Grouped by what they build. Source links point to project documentation; licenses cover code unless noted otherwise.

- [Official tools](#official-tools)
- [Trained models and training recipes](#trained-models-and-training-recipes)
- [Local inference and compatible servers](#local-inference-and-compatible-servers)
- [Evaluation and calibration](#evaluation-and-calibration)
- [SDKs and integrations](#sdks-and-integrations)
- [Agent tools and workflow control](#agent-tools-and-workflow-control)
- [Browser and device control](#browser-and-device-control)
- [Data search and document workflows](#data-search-and-document-workflows)
- [Games robotics and simulations](#games-robotics-and-simulations)

### Official tools

| Project | Description | License | Source |
|---|---|---|---|
| [Official Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) | Synchronous and asynchronous clients for the hosted System One API. | MIT | [Source](https://github.com/typesafe-ai/typesafe-sdk-python/blob/2ce5c65f13646cab6e6f782328194c9d85f3300a/README.md#L3) |
| [Official JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) | Typed JavaScript and TypeScript access to Jev questions and answers. | MIT | [Source](https://github.com/typesafe-ai/typesafe-sdk-js/blob/66880ccded6cb642dc1809620c2b108c33730214/README.md#L3) |
| [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) | Runs the same decision interface against language-model APIs for comparison and fallback experiments. | MIT | [Source](https://github.com/typesafe-ai/system-one-adapter-python/blob/adffc2eab300a4fa3c0e92252d4ffd6ceaa53700/README.md#L3) |
| [TypeSafe Skills](https://github.com/typesafe-ai/skills) | Official agent instructions and examples for designing bounded decision workflows. | MIT | [Source](https://github.com/typesafe-ai/skills/blob/65a39f393687675ce170e6094757de20370365b9/README.md#L3) |

### Trained models and training recipes

| Project | Description | License | Source |
|---|---|---|---|
| [Decider](https://github.com/Mapika/decider) | Qwen-based decision models with released checkpoints, training code, calibration experiments, and a compatible server. | Apache-2.0 | [Source](https://github.com/Mapika/decider/blob/c4daaac28af9fea95d627015cffa2dd5a5926ee6/README.md#L14) |
| [Laya](https://github.com/NandhaKishorM/laya) | Compact encoder-based decision models with multilingual variants, public checkpoints, and a domain fine-tuning notebook. | Apache-2.0 | [Source](https://github.com/NandhaKishorM/laya/blob/42626c348753fbb17572a813127df2278a1ec527/README.md#L24) |
| [Kev](https://github.com/jaredpalmer/kev) | Qwen-based model family with weights, training code, evaluation suites, and CUDA or Apple Silicon serving. | Apache-2.0 | [Source](https://github.com/jaredpalmer/kev/blob/4f8110a3f8620cc3a182ae9a708e4398492c4b1a/README.md#L3) |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | Small decision model with dynamic candidates, released game-task data, training scripts, and replayable evaluations. | MIT | [Source](https://github.com/TianyuCodings/NanoJev/blob/76fdfc9ecdca45a9bcef17991a07d3041a87685a/README.md#L1) |
| [Luce](https://github.com/scienthoon/luce) | Task-specific pipeline for synthetic data, LoRA and decision-head training, calibration evaluation, and serving. | Apache-2.0 | [Source](https://github.com/scienthoon/luce/blob/fd137a0bb9024d1505ef343b7f8c96833721377b/README.md#L9) |
| [Von](https://github.com/wfzyx/von) | Encoder-style local decision model with released weights and a System One endpoint; inspect task-specific benchmark conditions. | Apache-2.0 | [Source](https://github.com/wfzyx/von/blob/14d09878e89b103bfbbe641f9bed02e4d72c8830/README.md#L32) |
| [Jevlike](https://github.com/vinnylarouge/jevlike) | Small option-attention scorer for learning decisions over changing candidate sets, with text and visual examples. | MIT | [Source](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/README.md#L5) |
| [PlayJev](https://github.com/OmniJev/PlayJev) | Vision-based game decision model with public weights, imitation-learning scripts, and closed-loop evaluation. | Apache-2.0 | [Source](https://github.com/OmniJev/PlayJev/blob/2d7a0280841e3244a299c9c640efc8cefc46d476/README.md#L5) |
| [Eve RLCD](https://github.com/anthony-maio/eve-rlcd) | Independent calibration-training experiments inspired by Jev; its method is not TypeSafe's unpublished training recipe. | MIT | [Source](https://github.com/anthony-maio/eve-rlcd/blob/57a179b7b1bedc80f65bf42ccda129dd1888272f/README.md#L189) |

### Local inference and compatible servers

| Project | Description | License | Source |
|---|---|---|---|
| [SemIf (formerly OpenJev)](https://github.com/TheoLeeCJ/SemIf) | Reads candidate scores from existing open models, with shared-state inference and local backend experiments. | MIT | [Source](https://github.com/TheoLeeCJ/SemIf/blob/ca3ba65f142967030ecb453346e94d6f476a69df/README.md#L7) |
| [LitJev](https://github.com/zhengxuyu/litjev) | Serves typed decisions from Qwen output-head scores without retraining; probabilities are not calibrated by default. | Apache-2.0 | [Source](https://github.com/zhengxuyu/litjev/blob/f21216c9fe5afe7fa52ff7064a402ee57fdbddd3/README.md#L3) |
| [Simple Jev](https://github.com/featherless-ai/simple-jev) | Local decision API over compatible open models, plus examples and optional task-specific training tools. | Apache-2.0 | [Source](https://github.com/featherless-ai/simple-jev/blob/b02aa81c915a8193759b3cd33fef74721d6e005b/README.md#L9) |
| [OpenJev (razorback16)](https://github.com/razorback16/openjev) | DiffusionGemma decision server with vLLM and MLX backends; distinct from the project renamed SemIf. | Apache-2.0 | [Source](https://github.com/razorback16/openjev/blob/2050fdb8280d3094180870ac4df962f1bb44edca/README.md#L10) |
| [Reflex](https://github.com/kshetrajna12/reflex) | Shared-state question branches, bounded label scoring, local serving, and a browser demonstration. | MIT | [Source](https://github.com/kshetrajna12/reflex/blob/e21b3b23afdfeee7021a6604fa38f57e7ff5187f/README.md#L10) |
| [Jeff](https://github.com/logan-markewich/jeff) | GLiFormer-backed implementation of the System One API, including deployment and compatibility documentation. | MIT | [Source](https://github.com/logan-markewich/jeff/blob/34b32f99a727c47b679adde33f4702a001e02979/README.md#L3) |
| [jevmlx](https://github.com/bnsd55/jevmlx) | MLX runtime that scores allowed field values and assembles structured decisions on Apple Silicon. | MIT | [Source](https://github.com/bnsd55/jevmlx/blob/4a746fe0cf3fa027387ef99b83ef977053899f7f/README.md#L5) |
| [JEVfire](https://github.com/kikoncuo/jevfire) | Parallel candidate scoring through vLLM, with reproducible inference comparisons and game demonstrations. | MIT | [Source](https://github.com/kikoncuo/jevfire/blob/5df83b558bf635e006d31f8f2fc2798d0e3ff051/README.md#L5) |
| [cu-Jev](https://github.com/dtunai/cu-Jev) | C and CUDA inference engine for Qwen checkpoints, shared state, isolated questions, and typed decision serving. | Apache-2.0 | [Source](https://github.com/dtunai/cu-Jev/blob/2da91c65ee267f493e189b9ec56dc0e836fde5ea/README.md#L4) |
| [Laya-MLX](https://github.com/mizorewww/laya-mlx) | Native MLX inference for Laya checkpoints, with port-fidelity checks and local gameplay examples. | Apache-2.0 | [Source](https://github.com/mizorewww/laya-mlx/blob/fc1df62828a3fedf4d8229fdac1cbd85f1cdf337/README.md#L1) |
| [LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | Adapts local language models into structured decision engines using prefill-only binary inference. | Apache-2.0 | [Source](https://github.com/Yinsongxu/LLM2Jev/blob/924618721277976a4730518cb11381d4aa79c3a9/README.md#L5) |
| [PoorJev](https://github.com/rupeshpoojary9/poorjev) | Local decision interface built around NLI models, with temperature scaling and abstention experiments. | MIT | [Source](https://github.com/rupeshpoojary9/poorjev/blob/7e684e95db13b90238c63e6ab39e1a016263a168/README.md#L3) |
| [Jev Visual](https://github.com/hr98w/jev-visual) | Educational Apple Silicon visual-decision experiments using shared context and direct candidate scoring. | MIT | [Source](https://github.com/hr98w/jev-visual/blob/4382bba455647400951429134ceb012ca155e3fe/README.md#L7) |

### Evaluation and calibration

| Project | Description | License | Source |
|---|---|---|---|
| [JevBench](https://github.com/fstandhartinger/jevbench) | Cross-backend benchmark covering decision quality, calibration, latency, and cost; inspect version-specific scoring assumptions. | MIT | [Source](https://github.com/fstandhartinger/jevbench/blob/fd51755eb0c0b546ca206d764faf3302feca913e/README.md#L6) |
| [mini-Jev](https://github.com/r-ms/mini-jev) | Preregistered comparison of candidate-logit readout and grammar-constrained JSON, including abstention and dependent-field limitations. | MIT | [Source](https://github.com/r-ms/mini-jev/blob/ca612198bfb69f538f029a4615f6d0a18b4f814c/README.md#L3) |
| [Jev Calibration Audit](https://github.com/jujumilk3/jev-calibration-audit) | API-only study of abstention, option effects, language transfer, and probability calibration. | MIT | [Source](https://github.com/jujumilk3/jev-calibration-audit/blob/daab9e2c2d5d5683bf07f3482deb653c26856219/README.md#L3) |
| [Jev Rerank Bench](https://github.com/anessbelbati/jev-rerank-bench) | Reranking comparisons with recorded provider responses, evaluation scripts, and uncertainty estimates. | MIT | [Source](https://github.com/anessbelbati/jev-rerank-bench/blob/cd9a35b22aeb4187334f7018a0ee1960a7470586/README.md#L5) |
| [Jev Search Rerank Eval](https://github.com/zhuyansen/jev-search-rerank-eval) | Compares Jev reranking and embedding retrieval on a graded catalog-search workload. | MIT | [Source](https://github.com/zhuyansen/jev-search-rerank-eval/blob/c896f14e944182e17a002dd7546f06ba3788d586/README.md#L3) |
| [Jev ORDER BY Bench](https://github.com/yodablocks/jev-orderby-bench) | Tests whether decision probabilities support useful SQL ordering, including calibration and wording sensitivity. | MIT | [Source](https://github.com/yodablocks/jev-orderby-bench/blob/523979540d0fad2786208ba07cc8d0fe2711f9ed/README.md#L4) |
| [jevcal](https://github.com/abhixhek/jevcal) | Fits and checks task-specific decision thresholds, coverage, and drift on labeled examples. | MIT | [Source](https://github.com/abhixhek/jevcal/blob/ae8f3144d69c9cb0e5e0a2c17f70b9d14714cb9f/README.md#L7) |
| [Agent Failure Benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) | Evaluates Jev on identifying agent failures in a published failure-attribution task. | Apache-2.0 | [Source](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/4d46af795a4a4409940a65857da73e45abaea2db/README.md#L4) |
| [Jev Behavior Study](https://github.com/RINNECODER/jev-behavior-study) | Controlled API experiments with a written report, recorded outputs, and offline verification. | MIT | [Source](https://github.com/RINNECODER/jev-behavior-study/blob/e4a1d7ec691a91f33d3b5879a780e6f27328f173/README.md#L357) |

### SDKs and integrations

| Project | Description | License | Source |
|---|---|---|---|
| [jev-go](https://github.com/Gaurav-Gosain/jev-go) | Go client for typed questions and probabilistic answers from the hosted API. | MIT | [Source](https://github.com/Gaurav-Gosain/jev-go/blob/c9867e4afad0ddfaf4b9deb31038218495712fd0/README.md#L3) |
| [jev-go (Stumble)](https://github.com/Stumble/jev-go) | Go client and CLI supporting TypeSafe direct access and Vercel AI Gateway. | MIT | [Source](https://github.com/Stumble/jev-go/blob/a475dc925ba68602be93f4478e1381cf5ec27ee4/README.md#L16) |
| [TypeSafe AI for Rust](https://github.com/Twister915/typesafe-ai) | Rust client with asynchronous and blocking transports and retry observability. | Apache-2.0 | [Source](https://github.com/Twister915/typesafe-ai/blob/d4455efb1d061ae6aac47b40c42ef390182201b1/README.md#L3) |
| [s1-rs](https://github.com/AbdelStark/s1-rs) | Rust types and question builders for composing System One decisions. | MIT | [Source](https://github.com/AbdelStark/s1-rs/blob/b9168979a9beaeb74878483ff2876958acb98b86/README.md#L3) |
| [ZIO TypeSafe AI](https://github.com/jamesward/zio-typesafe-ai) | Scala and ZIO integration for typed, composable decision requests. | Apache-2.0 | [Source](https://github.com/jamesward/zio-typesafe-ai/blob/38082e8712b49ce239ae628557619347909165dc/README.md#L1) |
| [Swift SDK](https://github.com/alterhq/typesafe-sdk-swift) | Swift client for Choice, Score, and Noul, with concurrency and transport support. | MIT | [Source](https://github.com/alterhq/typesafe-sdk-swift/blob/4d416746fd74933d03b95fdb31d4cd0f1a9f10af/README.md#L3) |
| [Jev for Elixir OTP](https://github.com/dannote/jev) | Integrates decision requests and responses with OTP process messaging. | MIT | [Source](https://github.com/dannote/jev/blob/09fbb6cbaf32257924c08ba993ca8631adc16056/README.md#L5) |
| [Ruby SDK](https://github.com/joshmn/typesafe-sdk) | Ruby client for the TypeSafe API. | MIT | [Source](https://github.com/joshmn/typesafe-sdk/blob/21d65a1e089896850fe31054cec565ef4e3d020b/README.md#L3) |
| [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) | Adapters for using Jev as a retrieval reranker and query-engine selector. | MIT | [Source](https://github.com/WiktorB2004/llama-index-jev/blob/72c73dc50bca4b7ea6928ef65ea09f1a7ee4a01e/README.md#L1) |
| [Advocaat](https://github.com/pithings/advocaat) | Small TypeScript client for expressing typed questions over application data. | MIT | [Source](https://github.com/pithings/advocaat/blob/bc46287fc1102b95852a81d679c6e34a2c44f4a2/README.md#L3) |
| [jev4k](https://github.com/pambrose/jev4k) | Kotlin client and DSL for Jev decision requests. | Apache-2.0 | [Source](https://github.com/pambrose/jev4k/blob/e55206acd7894d590a8985dfbdeac04dcf92aaff/README.md#L12) |

### Agent tools and workflow control

| Project | Description | License | Source |
|---|---|---|---|
| [Jev MCP](https://github.com/jkudish/jev-mcp) | MCP tools for bounded judgments such as verification, screening, and ranking. | MIT | [Source](https://github.com/jkudish/jev-mcp/blob/69ffb4b49c88802ec6e49b883f4a36b91d23197e/README.md#L6) |
| [Jevwire](https://github.com/Brainwires/jevwire) | MCP server, embeddable decision library, and agent hooks for bounded workflow judgments. | MIT | [Source](https://github.com/Brainwires/jevwire/blob/fabe7e79252b415278cd4b42355e63106fb5af80/README.md#L3) |
| [jev-use](https://github.com/shitianfang/jev-use) | Agent integration that delegates typed judgments to Jev and flags uncertain results for escalation. | MIT | [Source](https://github.com/shitianfang/jev-use/blob/358819d34fd82840595660153408867fb155e1f8/README.md#L6) |
| [Fast Jev Compaction](https://github.com/tamaratran/fast-jev-compaction) | Scores tool-call history to retain useful content and remove or truncate stale results. | MIT | [Source](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/README.md#L3) |
| [Jev Pruner](https://github.com/tamaratran/jev-pruner) | Scores and trims long shell outputs before they enter an agent's context. | MIT | [Source](https://github.com/tamaratran/jev-pruner/blob/47d017c34eab7690b95f075ce6f4839247c5dc0a/README.md#L3) |
| [Jev Router](https://github.com/gargpratyush/jev-router) | Uses Jev decisions to route coding work between model tiers. | MIT | [Source](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/README.md#L12) |
| [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) | Selects a model, reasoning depth, and speed setting for each coding turn. | MIT | [Source](https://github.com/0xNatoshi/jev-codex-router/blob/faf46df90f3c6a3962bb5876d393c7d6552b7c8f/README.md#L5) |
| [Foreman](https://github.com/thruwire/foreman) | Uses Jev judgments to supervise a software-factory workflow. | MIT | [Source](https://github.com/thruwire/foreman/blob/a7d21d18d306a0cb9f3e15acefbdb5663521405c/README.md#L3) |
| [Jev Review](https://github.com/devagrawal09/jev-review) | Staged code-review workflow with a local dashboard and bounded judgments. | MIT | [Source](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/README.md#L3) |
| [Supercov](https://github.com/supercorp-ai/supercov) | Code-quality and coverage tooling that uses Jev to prioritize review work. | MIT | [Source](https://github.com/supercorp-ai/supercov/blob/b66518f8032a0356329ef0b1b3812d4ad2639503/README.md#L5) |
| [Pi Warden](https://github.com/DevMortimer/pi-warden) | Agent guardrails and loop checks built on the Pi TypeSafe integration. | MIT | [Source](https://github.com/DevMortimer/pi-warden/blob/d44ea782d3b6f3e7c281aedb9dae85b003d429ef/README.md#L17) |
| [Jev Belay](https://github.com/valentynkit/jev-belay) | Checks recorded evidence before accepting a coding agent's completion claim. | MIT | [Source](https://github.com/valentynkit/jev-belay/blob/ef719db7eaadc56aa4def86c4da4ffff5bcbca35/README.md#L23) |
| [Jev Commit](https://github.com/valentynkit/jev-commit) | Compares commit messages and staged changes through bounded pre-commit judgments. | MIT | [Source](https://github.com/valentynkit/jev-commit/blob/311e163b8abb9c333132155bc2e0bbfac4f36283/README.md#L39) |

### Browser and device control

| Project | Description | License | Source |
|---|---|---|---|
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | Browser agent where Jev chooses operations and elements, while a text model supplies typed content. | MIT | [Source](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/README.md#L1) |
| [TypeSafe Computer Use](https://github.com/awlevin/typesafe-computer-use) | macOS control loop combining screen OCR, bounded action selection, and execution. | MIT | [Source](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/README.md#L10) |
| [Mobile Jev](https://github.com/droidrun/mobile-jev) | Android interaction experiments with Jev selecting actions in a device-control loop. | MIT | [Source](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/README.md#L7) |
| [Jev Browser](https://github.com/jkudish/jev-browser) | Browser automation library, CLI, and MCP integration using Jev for step selection. | MIT | [Source](https://github.com/jkudish/jev-browser/blob/800e80b42f1a8dd5461add01d2c95d223be90ee6/README.md#L6) |
| [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) | Voice-driven browser control using typed intent and target decisions. | MIT | [Source](https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/README.md#L5) |
| [Unclutter](https://github.com/kitze/unclutter) | Browser extension using Jev judgments and reusable rules to remove page clutter. | MIT | [Source](https://github.com/kitze/unclutter/blob/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/README.md#L103) |

### Data search and document workflows

| Project | Description | License | Source |
|---|---|---|---|
| [DocJev](https://github.com/jerryjliu/docjev) | Classifies documents and finds packet boundaries using local text extraction and hosted Jev judgments. | Apache-2.0 | [Source](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/README.md#L15) |
| [jevql](https://github.com/kylemclaren/jevql) | SQL-oriented tools that apply Jev judgments to PostgreSQL query results. | MIT | [Source](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/README.md#L23) |
| [DuckDB Jev](https://github.com/recodelabs/duckdb-jev) | DuckDB integration for filtering rows using natural-language criteria. | MIT | [Source](https://github.com/recodelabs/duckdb-jev/blob/378d36ffba2b7dd8cc3e1a20a673768748892bbe/README.md#L4) |
| [SQLite3 Jev](https://github.com/mattn/sqlite3-jev) | SQLite extension exposing decision calls as SQL functions. | MIT | [Source](https://github.com/mattn/sqlite3-jev/blob/2172600da148182703f8f221089d9304d0fb97f9/README.md#L3) |
| [jgrep](https://github.com/kyu1204/jgrep) | Searches code chunks by semantic criteria and returns file-and-line matches. | MIT | [Source](https://github.com/kyu1204/jgrep/blob/e91569b6c871717ac47ac1e94e4387110ac900f1/README.md#L14) |
| [Jev Search](https://github.com/superagents-lab/jev-search) | Uses Jev for query interpretation, source selection, and search-result relevance. | MIT | [Source](https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/README.md#L5) |
| [Jev Align](https://github.com/sutro-sh/jev-align) | Human-feedback workflow for improving decision definitions and evaluating calibrated AI functions. | Apache-2.0 | [Source](https://github.com/sutro-sh/jev-align/blob/3d997fc76593036655c28d4964de43b55f81fe2c/README.md#L4) |

### Games robotics and simulations

| Project | Description | License | Source |
|---|---|---|---|
| [Jev Drone](https://github.com/RomanSlack/jev-drone) | MuJoCo drone experiment placing Jev judgments inside a slower decision loop. | MIT | [Source](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/README.md#L4) |
| [EmbodiedJev](https://github.com/FBddcz/embodied-jev) | Robot-decision workbench comparing local models, Jev, and compatible endpoints. | MIT | [Source](https://github.com/FBddcz/embodied-jev/blob/764f2ffac40ef65c7fda0d5ba897f9992ba8d464/README.md#L31) |
| [Jev Plays Pokemon Red](https://github.com/valentynkit/jev-plays-pokemon-red) | Game harness combining deterministic mechanics with bounded Jev decisions and prediction scoring. | MIT | [Source](https://github.com/valentynkit/jev-plays-pokemon-red/blob/cbe5387aeb6c7b3ef6b1f67d4a95e284aee3b0af/README.md#L84) |
| [Jev T-Rex Runner](https://github.com/joshlarsen/jev-t-rex-runner) | Chrome dinosaur-game experiment driven by Jev decisions. | BSD-3-Clause | [Source](https://github.com/joshlarsen/jev-t-rex-runner/blob/49682008948c8715fd5a2824d33284193d6eab89/README.md#L5) |

## More projects

The [complete index](catalog/README.md) adds community SDKs, agent plugins, security and moderation tools, document workflows, browser agents, games, robotics, productivity applications, and finance experiments. Full repository names disambiguate unrelated projects that share names such as `openjev`, `jev-mcp`, and `jev-go`.

## About this list

This is a community list, unaffiliated with TypeSafe AI. It includes both applications using the hosted Jev API and independent models that run locally.

Found a useful project or a broken link? [Open an issue](https://github.com/KuzanJ/awesome-jev/issues) or send a pull request. See [how the list is maintained](docs/METHODOLOGY.md) and the [contribution guide](CONTRIBUTING.md).

Thanks to the project authors and the [community lists](docs/SOURCES.md) that helped make this directory possible.

[MIT](LICENSE). Linked projects retain their own licenses.
