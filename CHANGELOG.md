# Changelog

本项目的所有重要变更都记录在此文件中。

## [未发布]

### 新增（`.pi/APPEND_SYSTEM.md`：Worker 会话的项目硬规则）

- **为什么改**：用户 2026-11-07 定下全局 Leader / Worker 分工——子项目的具体活由以子项目根 / worktree 为工作目录的 Worker 会话承担，Leader 只做 local main 同步、建 worktree、派活与收尾。Worker 会话读不到 Agent 项目那一层的上下文，本仓特有的硬规则必须落在本仓，由 pi 在会话启动时自动追加进系统提示；否则 Worker 只能靠 Leader 口头交代，规则随任务结束即丢失。
- **改了什么**（2026-11-07）：新增 `.pi/APPEND_SYSTEM.md`（40 行）。只写本项目特有的约束：Worker 角色边界（不碰 local main、不建 / 删 worktree）、编号即契约（1–22 连续、新增只能追加到末尾）、七类目顺序固定、每条规则的写法固定、第 4 条 JSON 与第 9 条路径两组正误对照示例不许删、中英同轮同步、README 徽章与类目区间表跟着改、只放工具调用规则的定位边界、PolyForm 非商业许可的搬运限制；末尾附可直接跑的核对命令（条数 / 编号序列 / 类目数）。通用身份与全局规则仍由 `AGENTS.md` 软链接提供，此处不重述。
- **顺带修正**：CHANGELOG 此前把 validate 条目挂在没有 `## [未发布]` 标题的位置上，本次补上该标题并把我这条与它一起归入未发布区，结构符合 Keep a Changelog。
- **边界**：不改任何规则正文与 README，纯新增一份会话层配置 + 归档结构调整。

### 新增（CI 门禁：validate 检查 + main 分支 strict 保护）

- **为什么改**：用户 2026-11-03 立规「新建仓库一律必须 strict 模式的 PR CI」，并要求 28 个不合规的存量仓库统一执行最新标准。本项目此前在 PR 上没有门禁——改动合进 main 全靠人工把关，PR 可以拿旧 main 上通过的检查直接合并，回归防护存在缺口。本次补齐团队要求的「三件套」：PR 上真实跑的 CI 检查 + 挂成 required status check + `required_status_checks.strict = true`。
- **改了什么**（2026-11-03）：新增 `.github/workflows/validate.yml`（PR 与 main push 触发，检查名 `validate`）与 `.github/scripts/validate.py`（仓库卫生检查：必备文件存在、敏感文件未被跟踪、被跟踪文件不超过 10 MB、README 相对链接有效、Python / Shell 语法检查）；main 分支保护补挂 required check `validate` 并设 `strict=true`。
- **边界**：检查只做确定性、低误报的项目（required check 一旦误报就会卡住正常 PR，所以宁可少查）；不改动仓库任何原有内容。

## [1.0.0] - 2026-10-31

首个记录版本。规则集本身在此之前已作为独立项目存在（22 条规则、7 大类），本次纳入 NeuralCoreAgent（Ada）名下维护，并补齐项目标配。

### 新增

- `VERSION` 与 `CHANGELOG.md`：版本号与变更记录从此有唯一权威来源。
- README 中英两版新增 Version、Type 两枚徽章，新增中英文互链，新增底部「版权与署名」段（版权声明 + 署名方式 + 项目地址）。
- GitHub 仓库 About 补齐中英双语描述与 topics。

### 变更

- 2026-10-31 起由 NeuralCoreAgent（Ada）负责维护：新增身份层 `AGENTS.md` 软链接（指向 `../NeuralCoreAgent/AGENTS.md`）与能力层 `.pi/settings.json`（引用 NeuralCoreAgent 的 extensions / skills / prompts / themes 目录）。
- `.gitignore` 新增两条忽略规则，把与本规则集无关的业务与平台运营笔记排除在版本控制之外（文件保留在原位置，不入库）。
