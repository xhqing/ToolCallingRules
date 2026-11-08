<p align="center">
  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=A professional minimalist logo for LLM tool calling rules project featuring geometric shield icon with checkmark symbol representing safety and precision dark blue and teal gradient clean tech style white background&image_size=square" alt="Tool Calling Rules Logo" width="200" />
</p>

<h1 align="center">Tool Calling Rules</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Rules-22-blue?style=for-the-badge&logo=markdown" alt="Rules Count" />
  <img src="https://img.shields.io/badge/Categories-7-orange?style=for-the-badge&logo=list" alt="Categories" />
  <img src="https://img.shields.io/badge/License-PolyForm--Noncommercial-red?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Type-Project-lightgrey?style=for-the-badge" alt="Type" />
  <img src="https://img.shields.io/badge/LLM-Compatible-brightgreen?style=for-the-badge&logo=openai" alt="LLM Compatible" />
</p>

<p align="center">
  <a href="README_cn.md">简体中文</a>
</p>

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

## License & Attribution

Copyright (c) 2026 xhqing <https://github.com/xhqing>. Licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE.md) — commercial use is not permitted.

Attribution is welcome and appreciated: you may reference, quote, or adopt these rules (with credit and a link back to this repository) as long as the copyright notice and this license are retained.

- Project: https://github.com/xhqing/ToolCallingRules
