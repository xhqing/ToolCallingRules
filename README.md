# Tool Calling Rules

A set of structured rules for LLM tool calling, designed to reduce parameter formatting errors, improve call accuracy, and enhance safety.

## Overview

When LLMs call external tools (function calling), they often make recurring mistakes — sending `null` placeholders for optional fields, wrapping paths in Markdown formatting, mismatching container types, or blindly retrying on errors. This project provides a concise, enforceable rule set that can be injected into system prompts to correct these behaviors.

## Rules

22 rules across 7 categories:

| Category | Rules | Key Points |
|----------|-------|-------------|
| Pre-Call Preparation | 1–3 | Read before calling, never fabricate values, confirm required vs. optional |
| Parameter Format | 4–8 | Enum values must match exactly |
| Paths and Identifiers | 9–11 | Always use absolute paths |
| Related Parameters | 12–13 | Inter-parameter dependencies |
| Tool Selection & Strategy | 14–16 | Parallelize independent calls, serialize dependent ones |
| Error Recovery | 17–19 | Stop retrying on permission/not-found errors |
| Safety and Side Effects | 20–22 | Destructive operations caution, avoid redundant writes, respect idempotency |

## Usage

Copy the content of the rule file into your system prompt or agent instructions. For example:

```
You are a helpful assistant. When calling tools, follow these rules:

<paste content of toolCallingRules.md here>
```

## Language

The rule file (`toolCallingRules.md`) is written in Chinese.

## License

PolyForm Noncommercial License 1.0.0
