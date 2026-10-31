# Changelog

本项目的所有重要变更都记录在此文件中。

## [1.0.0] - 2026-10-31

首个记录版本。规则集本身在此之前已作为独立项目存在（22 条规则、7 大类），本次纳入 NeuralCoreAgent（Ada）名下维护，并补齐项目标配。

### 新增

- `VERSION` 与 `CHANGELOG.md`：版本号与变更记录从此有唯一权威来源。
- README 中英两版新增 Version、Type 两枚徽章，新增中英文互链，新增底部「版权与署名」段（版权声明 + 署名方式 + 项目地址）。
- GitHub 仓库 About 补齐中英双语描述与 topics。

### 变更

- 2026-10-31 起由 NeuralCoreAgent（Ada）负责维护：新增身份层 `AGENTS.md` 软链接（指向 `../NeuralCoreAgent/AGENTS.md`）与能力层 `.pi/settings.json`（引用 NeuralCoreAgent 的 extensions / skills / prompts / themes 目录）。
- `.gitignore` 新增两条忽略规则，把与本规则集无关的业务与平台运营笔记排除在版本控制之外（文件保留在原位置，不入库）。
