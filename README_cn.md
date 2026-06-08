<p align="center">
  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=A professional minimalist logo for LLM tool calling rules project featuring geometric shield icon with checkmark symbol representing safety and precision dark blue and teal gradient clean tech style white background&image_size=square" alt="工具调用规则 Logo" width="200" />
</p>

<h1 align="center">工具调用规则</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Rules-22-blue?style=for-the-badge&logo=markdown" alt="规则数量" />
  <img src="https://img.shields.io/badge/Categories-7-orange?style=for-the-badge&logo=list" alt="类别" />
  <img src="https://img.shields.io/badge/License-PolyForm--Noncommercial-red?style=for-the-badge" alt="许可证" />
  <img src="https://img.shields.io/badge/LLM-Compatible-brightgreen?style=for-the-badge&logo=openai" alt="LLM兼容" />
</p>

一套用于LLM工具调用的结构化规则，旨在减少参数格式错误、提升调用准确性并增强安全性。

## 概述

当LLM调用外部工具（函数调用）时，经常会出现反复出现的错误——为可选字段发送`null`占位符、用Markdown格式包裹路径、容器类型不匹配，或盲目重试错误。本项目提供了一套简洁、可执行的规则集，可注入系统提示词以纠正这些行为。

## 规则

22条规则，分为7个类别：

| 类别 | 规则 | 要点 |
|------|------|------|
| 调用前准备 | 1–3 | 先读后调、禁止捏造值、确认必填与可选 |
| 参数格式 | 4–8 | 枚举值须精确匹配 |
| 路径与标识符 | 9–11 | 一律使用绝对路径 |
| 关联参数 | 12–13 | 参数间的依赖关系 |
| 工具选择与策略 | 14–16 | 独立调用可并行，有依赖时串行 |
| 错误恢复 | 17–19 | 权限或不存在错误时停止重试 |
| 安全与副作用 | 20–22 | 破坏性操作谨慎、避免冗余写入、尊重幂等性 |

## 使用方法

将规则文件的内容复制到您的系统提示词或智能体指令中。例如：

```
你是一个有用的助手。调用工具时，请遵循以下规则：

<在此处粘贴toolCallingRules.md的内容>
```

## 语言

规则文件（`toolCallingRules.md`）使用中文编写。

## 许可证

PolyForm 非商业许可证 1.0.0