# duilian-writer（对联写作 Codex Skill）

简体中文 | [English](README.en.md)

用于写作/改写/校验中文对联（对联/楹联/春联/挽联/行业联/题赠联）的 Codex Skill，支持按需启用更严格的格律要求：

- 字数对等、词性/结构/节律对仗、平仄对立、形对意联
- 可选：用典与押韵、横批与贴法说明

## 项目结构

- `SKILL.md`：技能主说明（含 frontmatter）
- `references/`：规则清单、写作素材与场景用语
- `scripts/pingze_check.py`：今声（普通话四声）平仄快速辅助脚本

## 安装

将本仓库 clone（或拷贝）到你的 Codex skills 目录：

- 默认：`~/.codex/skills/duilian-writer`
- 或：`$CODEX_HOME/skills/duilian-writer`

### 推荐：让你的 CLI 工具代劳

如果你在使用支持“让 AI 执行安装步骤”的 CLI（例如 Claude Code、Codex CLI 等），可以直接把下面这段提示词发给它，让它自动完成 clone 与放置路径：

```text
请帮我安装一个 Codex Skill（对联写作 duilian-writer）。

仓库地址：https://github.com/JaysonGeng/duilian-writer-skill.git

请将其克隆到 ~/.codex/skills/duilian-writer（如果我本机使用的是其它 skills 目录，也请按我的环境自动识别/询问我确认）。
完成后请确认 SKILL.md 存在且能被识别加载，并给我一个验证方法（例如如何触发该 skill 写一副对联）。
```

示例（SSH）：

```bash
git clone git@github.com:JaysonGeng/duilian-writer-skill.git ~/.codex/skills/duilian-writer
```

示例（HTTPS）：

```bash
git clone https://github.com/JaysonGeng/duilian-writer-skill.git ~/.codex/skills/duilian-writer
```

## 使用

在 Codex 中，直接提出“写对联/改对联/检查对仗平仄”等需求即可。为了更贴合你的场景，建议补充：

- 场景：春联/喜联/寿联/挽联/行业联/题赠联
- 语域：典雅/通俗；文言/白话
- 字数：常见 5/7/9/11/13…（或指定分节如 2-2-3）
- 要求：只求工整 / 严格对仗 / 严格平仄 / 押韵 / 需要横批
- 关键字：人名/地名/品牌/行业术语/禁忌字

示例：

- `写一副七字春联，主题“乔迁新居”，典雅文言，要求严格对仗，给横批并说明贴法。`
- `请把这副对联改得更工整，并检查对仗与平仄（按今声，不用平水韵）：上联：…… 下联：……`

## 平仄脚本（可选）

`scripts/pingze_check.py` 使用今声（普通话四声）做快速映射：`1/2=平`，`3/4=仄`（轻声以 `?` 标记）。

安装依赖：

```bash
python -m pip install -r requirements.txt
```

运行：

```bash
python scripts/pingze_check.py "上联" "下联"
```

## 许可证

MIT，见 `LICENSE`。
