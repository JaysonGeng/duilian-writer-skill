# duilian-writer (Codex Skill)

A reusable writing workflow for Chinese couplets (对联/楹联/春联/挽联/行业联/题赠联), with optional stricter 格律 checks:

- 字数对等、词性/结构/节律对仗、平仄对立、形对意联
- 可选：用典与押韵、横批与贴法说明

This repository contains:

- `SKILL.md`: the skill instructions (with frontmatter).
- `references/`: practical checklists, rules, and writing materials.
- `scripts/pingze_check.py`: a quick helper to map Modern Mandarin tones (今声) to 平/仄.

## Install

Clone (or copy) this repo into your Codex skills directory:

- Default: `~/.codex/skills/duilian-writer`
- Or: `$CODEX_HOME/skills/duilian-writer`

Example:

```bash
git clone git@github.com:JaysonGeng/duilian-writer-skill.git ~/.codex/skills/duilian-writer
```

## Use

In Codex, invoke it by asking for couplets. Helpful details to include:

- 场景：春联/喜联/寿联/挽联/行业联/题赠联
- 语域：典雅/通俗；文言/白话
- 字数：常见 5/7/9/11/13…（或指定分节如 2-2-3）
- 要求：只求工整 / 严格对仗 / 严格平仄 / 押韵 / 需要横批
- 关键字：人名/地名/品牌/行业术语/禁忌字

Prompt examples:

- `写一副七字春联，主题“乔迁新居”，典雅文言，要求严格对仗，给横批并说明贴法。`
- `请把这副对联改得更工整，并检查对仗与平仄（按今声，不用平水韵）：上联：…… 下联：……`

## Ping/Ze helper script (optional)

`scripts/pingze_check.py` uses Modern Mandarin tones (1/2=平, 3/4=仄) to give a quick map.

Install dependency:

```bash
python -m pip install -r requirements.txt
```

Run:

```bash
python scripts/pingze_check.py "上联" "下联"
```

## License

MIT. See `LICENSE`.

