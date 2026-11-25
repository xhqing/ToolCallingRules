# ToolCallingRules

> NeuralCoreAgent（Ada）名下的子项目 · 本项目规则本体

注入 system prompt 的 LLM 工具调用规则集：22 条规则 / 7 大类。中文正文 `toolCallingRules.md`、英文 `toolCallingRules_en.md`，两版逐条对应；仓库里没有代码，正文就是产品。

## 归谁负责

本项目由 **Ada**（NeuralCoreAgent）负责维护。改动范围跨出本项目时，先向 Ada 说明，不自行扩张改动面。

## 你的角色

角色按全局三级分工（2026-11-25 起，见全局 `~/.pi/agent/AGENTS.md`「Leader / Worker 的定义」）：

- **本项目主工作区的 main 分支会话 = subLeader**：只管本项目——local main 的 ff 同步、从自身 main 建删任务 worktree、把任务派给 Worker、按全局工作流合并本项目 PR、发本项目版本、回收 Worker；对本项目以外（NeuralCoreAgent 与兄弟子项目）只读。
- **本项目 worktree 里的会话 = Worker**：只做当前 worktree 里的这一件事，干完向派它的 Leader 汇报——改了什么、验证结果、PR 号、遗留问题；**不碰 local main、不建删 worktree**。
- 建删 worktree 与 ff 同步 local main 是 subLeader（本项目主工作区 main 会话）的活，agentLeader（Ada）可代管。
- 上下文不够时向 Leader 问，不要凭猜测改代码。
- 本项目的硬约束与验证要求写在 `.pi/APPEND_SYSTEM.md`（会话启动时自动加载），动代码前先看一遍。

## 项目规则在哪

| 内容 | 位置 |
|---|---|
| 本项目硬约束、验证要求、易踩的坑 | `.pi/APPEND_SYSTEM.md`（自动加载） |
| 开发 / 构建 / 发版全流程 | `DEVELOPMENT.md`、`README.md` / `README_cn.md` |
| 待办 | `TODO.md`（已处理进 `TODO-archive.md`） |
| 改动记录 | `CHANGELOG.md` |
| 团队通用规则（git 流程、敏感信息、agentLeader / subLeader / Worker 三级分工等） | 全局 `~/.pi/agent/AGENTS.md` |
