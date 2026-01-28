# duilian-writer (Codex Skill for Chinese Couplets)

[简体中文](README.md) | English

An opinionated Codex skill for composing, revising, and validating Chinese couplets (对联/楹联/春联/挽联/行业联/题赠联), with optional stricter rules:

- Same length (字数对等)
- Parallel structure (词性/结构/节律对仗)
- Tone opposition (平仄对立)
- Connected meaning (形对意联)
- Optional: allusions, rhyming, horizontal scroll (横批) and posting guidance

## Repository layout

- `SKILL.md`: the skill instructions (with frontmatter).
- `references/`: checklists, rules, and writing materials.
- `scripts/pingze_check.py`: a quick Modern-Mandarin ping/ze helper.

## Install

Clone (or copy) this repo into your Codex skills directory:

- Default: `~/.codex/skills/duilian-writer`
- Or: `$CODEX_HOME/skills/duilian-writer`

Example (SSH):

```bash
git clone git@github.com:JaysonGeng/duilian-writer-skill.git ~/.codex/skills/duilian-writer
```

Example (HTTPS):

```bash
git clone https://github.com/JaysonGeng/duilian-writer-skill.git ~/.codex/skills/duilian-writer
```

## Use

In Codex, ask for writing/revising/checking couplets. Helpful details:

- Occasion: Spring Festival / wedding / birthday / memorial / business / dedication
- Register: classical vs. modern; formal vs. casual
- Length: 5/7/9/11/13… (or segmented rhythm like 2-2-3)
- Strictness: basic / strict parallelism / strict ping-ze / rhyming / include 横批
- Required keywords and taboo words

Prompt examples:

- `Write a 7-character Spring Festival couplet for a housewarming, in classical style, strict parallelism, include a horizontal scroll and posting guidance.`
- `Polish this couplet and check parallelism + ping/ze in Modern Mandarin: 上联：… 下联：…`

## Ping/Ze helper script (optional)

`scripts/pingze_check.py` maps Modern Mandarin tones to ping/ze using the common heuristic:

- 1/2 = 平 (ping)
- 3/4 = 仄 (ze)
- neutral tone is shown as `?`

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

