# Model Background: GPT-4.1 mini

This project uses `gpt-4.1-mini` by default.

## What kind of model is it?

`gpt-4.1-mini` is a large language model (LLM) in OpenAI's GPT-4.1 family.

At a high level, an LLM is a neural network trained to predict the next token in text. By learning from very large amounts of text and code, it becomes good at tasks such as:
- answering questions
- following instructions
- summarizing
- writing and editing code
- using tools through structured function calling

## Why this project uses it

This project uses `gpt-4.1-mini` because it is a practical model for beginners:
- lower cost than larger models in the same family
- faster than larger models
- strong enough for tool-calling and simple agent tasks
- good instruction-following for small projects and demos

## What OpenAI has publicly said

According to OpenAI's public GPT-4.1 release information:
- GPT-4.1, GPT-4.1 mini, and GPT-4.1 nano support up to 1 million tokens of context.
- GPT-4.1 mini is positioned as a smaller, faster, lower-cost model.
- OpenAI states that GPT-4.1 mini matches or exceeds GPT-4o on many intelligence evaluations while reducing latency by nearly half and reducing cost by 83%.
- The GPT-4.1 family was optimized for coding, instruction following, long-context use, and agent-like workflows.

## How it was created

Only high-level information is public.

Based on OpenAI's public descriptions, the GPT-4.1 family was developed through:
- large-scale pretraining on broad text and code data
- post-training to improve instruction following
- additional work to improve tool use, long-context retrieval, and reliability on real developer tasks

OpenAI has not publicly released the full training dataset, parameter count, layer count, or all implementation details.

## Model architecture

OpenAI has not publicly published the full architecture details for `gpt-4.1-mini`.

What can be said safely:
- it is part of the GPT family of transformer-based language models
- it is designed for token prediction plus post-training for instruction following and tool use
- exact internal architecture details are not publicly disclosed

So for teaching, the right framing is:

"We know it is a modern transformer-style LLM, but we do not know every internal engineering detail because that information has not been fully published."

## What it is especially good at

Based on OpenAI's public materials, the GPT-4.1 family is especially good at:
- coding tasks
- instruction following
- multi-turn conversations
- long-context retrieval and reasoning
- function calling / tool use

For this project, the most relevant strengths are:
- understanding a user's request
- deciding when to call a tool
- formatting tool arguments correctly
- turning tool output into a natural-language answer

## Public performance information

OpenAI's public GPT-4.1 release notes report the following family-level and model-specific signals:
- GPT-4.1 scored 54.6% on SWE-bench Verified in OpenAI's reported evaluation.
- GPT-4.1 scored 87.4% on IFEval in OpenAI's reported evaluation.
- GPT-4.1 mini is described as matching or exceeding GPT-4o on many intelligence evaluations while being faster and cheaper.
- GPT-4.1 mini is listed at $0.40 input, $0.10 cached input, and $1.60 output per 1M tokens in OpenAI's release pricing table at launch.

These numbers are useful background, but they should not be treated as guarantees for every classroom project. Real performance depends on prompting, task design, tool definitions, and evaluation setup.

## Limitations students should know

Even strong models can:
- hallucinate facts
- misunderstand vague prompts
- call the wrong tool when instructions are unclear
- sound confident when they are wrong
- produce different wording on different runs

That is why this project gives the model real tools for time, notes, and arithmetic instead of asking it to guess everything from memory.

## Why tool use matters here

When a student asks, "What time is it?", the model should not rely on its internal knowledge. Instead, it should call the `get_current_time` tool and use the real result.

That is one of the most important lessons in this project:

An agent becomes more reliable when it can use tools instead of only generating text.

## Summary for beginners

`gpt-4.1-mini` is a fast, lower-cost LLM that is well suited to beginner agent projects. Publicly, OpenAI describes it as strong at coding, instruction following, long context, and tool use. Some details, such as exact architecture size and full training data, have not been publicly disclosed, so those parts should be described carefully.