# duilian-writer（对联写作 Codex Skill）

用于写作/改写/校验中文对联（对联/楹联/春联/挽联/行业联/题赠联）的 Codex Skill，支持按需启用更严格的格律要求：

- 字数对等、词性/结构/节律对仗、平仄对立、形对意联
- 可选：用典与押韵、横批与贴法说明

（English: An opinionated couplet-writing workflow for Codex, with references and an optional ping/ze helper script.）

## 项目结构

- `SKILL.md`: the skill instructions (with frontmatter).
- `references/`: practical checklists, rules, and writing materials.
- `scripts/pingze_check.py`: a quick helper to map Modern Mandarin tones (今声) to 平/仄.

## 安装

将本仓库 clone（或拷贝）到你的 Codex skills 目录：

- Default: `~/.codex/skills/duilian-writer`
- Or: `$CODEX_HOME/skills/duilian-writer`

示例：

```bash
git clone git@github.com:JaysonGeng/duilian-writer-skill.git ~/.codex/skills/duilian-writer
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

`scripts/pingze_check.py` uses Modern Mandarin tones (1/2=平, 3/4=仄) to give a quick map.

安装依赖：

```bash
python -m pip install -r requirements.txt
```

运行：

```bash
python scripts/pingze_check.py "上联" "下联"
```

## License

MIT. See `LICENSE`.
