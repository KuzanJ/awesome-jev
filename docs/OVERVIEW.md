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

## Understand the ecosystem

| Artifact | What is open | How it relates to Jev |
|---|---|---|
| Official SDK or adapter | Client / integration code | Usually calls hosted Jev, or substitutes another provider |
| Local inference engine | Runtime and interface implementation | Scores bounded choices using existing model weights |
| Trained decision model | Some combination of code, weights, data, and recipe | Independently trains for a similar decision interface |
| Application or agent integration | Application code | Uses Jev as one component; often still requires a hosted API |
| Evaluation project | Harness, cases, or recorded results | Measures a specific task or property, not universal superiority |

A compatible request schema, open inference code, released weights, a complete training recipe, and demonstrated calibration are **five separate properties**. Check each independently.

## Suggested reading paths

- **Understand the product:** [launch announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [API introduction](https://docs.typesafe.ai/introduction), then [limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13).
- **Study inference:** [SemIf](https://github.com/TheoLeeCJ/SemIf), [mini-Jev](https://github.com/r-ms/mini-jev), and [Simple Jev](https://github.com/featherless-ai/simple-jev).
- **Study training:** [Decider](https://github.com/Mapika/decider), [Kev](https://github.com/jaredpalmer/kev), [Laya](https://github.com/NandhaKishorM/laya), and [Luce](https://github.com/scienthoon/luce).
- **Build a workflow:** [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast), [DocJev](https://github.com/jerryjliu/docjev), and [Jevwire](https://github.com/Brainwires/jevwire).
- **Evaluate a claim:** [JevBench](https://github.com/fstandhartinger/jevbench) and [Jev Calibration Audit](https://github.com/jujumilk3/jev-calibration-audit); examine labels, option ordering, abstention, splits, and measurement conditions.
