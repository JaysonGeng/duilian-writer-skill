---
name: duilian-writer
description: Compose, revise, and validate Chinese couplets (对联/楹联/春联/挽联/行业联/题赠联), including core rules (字数对等、词性/结构/节律对仗、平仄对立、形对意联), optional 用典与押韵, and presentation (横批与贴法). Use when asked to 写对联/拟横批/改对联/检查平仄或对仗/为节日婚寿乔迁开业题赠等场景拟联, or when you must use web search to research classical literature (诗词/典故出处) and modern hotspots to craft context-appropriate couplets.
---

# Duilian Writer

## Goal

Write (or revise) a high-quality Chinese couplet that is context-appropriate and, when requested, follows stricter 格律：对仗、节律、平仄与（可选）押韵。

## Quick Intake (ask if missing)

- Confirm the scene and register: 春联/喜联/寿联/挽联/行业联/题赠联；典雅/通俗；文言/白话。
- Confirm the constraints: 字数（常见 5/7/9/11/13…）；是否要分节（如 2-2-3）；是否需要横批。
- Confirm the 格律强度：只求工整/要求严格对仗/要求严格平仄/要求押韵。
- Choose a tone system and keep it consistent: 旧声（平水韵/入声）或今声（普通话四声）。不要混用。
- Collect any required keywords, taboo words, names, places, brand terms.

## Workflow A: Write a New Couplet

1. Choose a “skeleton” first: decide the phrase segmentation and the main word slots（名/动/形/数/量/方位…）。
2. Draft one line with clear imagery and intent:
   - Prefer concrete nouns + dynamic verbs + restrained adjectives.
   - Keep the ending character meaningful and stable (avoid weak particles).
3. Draft the matching line by mirroring the skeleton:
   - Align word class (词性对品) and syntactic structure (结构对应).
   - Keep meaning linked but not redundant; avoid 合掌（两联同义复述）.
4. Align rhythm (节律对拍):
   - Keep punctuation and caesura positions consistent across both lines.
5. Check tones (平仄对立) if required:
   - Prefer “上联末字仄、下联末字平” as default.
   - Make corresponding positions opposite tone as much as possible; allow rare exceptions (虚字/专名/不可拆词).
   - For multi-clause couplets, keep clause-end tones alternating (马蹄格) when possible.
6. Polish diction for classical flavor when desired:
   - Replace plain words with idioms,典故意象, and parallel imagery.
   - Avoid repeating the same character in the same position; avoid awkward homophones.
7. Output in a clean format:
   - Provide 上联、下联；if needed provide 横批（2–4 字为常见）.
   - Provide贴法（按读向判定）：横批/竖排从右往左读 → 上联贴右、下联贴左；横批从左往右读 → 上联贴左、下联贴右；无横批时可用“上仄下平”判上/下联，再据读向贴。

## Workflow B: Review / Repair an Existing Couplet

1. Diagnose quickly: 字数/对仗（词性+结构+节律）/平仄/语义/场景用词/禁忌。
2. Produce fixes in tiers:
   - Minimal-change fix (preserve most wording).
   - More elegant rewrite (improve imagery and register).
3. Explain briefly what changed and why (1–3 bullets max).

## Workflow C: Web Research (Classics & Hot Topics)

Use web search when you need to (1) confirm facts and proper nouns, (2) find classical imagery/典故出处, or (3) incorporate modern hot topics responsibly.

1. Decide the target: facts / classical corpus / modern hotspots (ask the user if unclear).
2. Search with constraints:
   - Classics: prefer sources that show original text + author/work; cross-check once before using.
   - Hot topics: apply recency filters; confirm date/context; avoid outdated or controversial wording.
3. Build a small “素材表” (5–10 candidates): phrase → meaning → source → how to transform into 联语.
4. Convert material into parallel slots (词对/意象) instead of copying long quotes.
5. Return to Workflow A/B and re-check 对仗/节律/平仄.

## Built-in Resources

- Read `references/duilian-rules.md` for the “联律通则” style checklist and common pitfalls.
- Read `references/pingze-yun.md` for 平仄/马蹄格/押韵 guidance and old-vs-modern tone choice.
- Read `references/occasions.md` for scenario-specific vocabulary, imagery, and taboos.
- Read `references/classical-culture.md` for classical imagery,典故 usage, and elegant parallel phrasing patterns.
- Read `references/web-research.md` for a web-search workflow to gather classical sources and modern hotspots safely.
- Use `scripts/pingze_check.py` for a quick modern-Mandarin 平/仄 map (requires `pypinyin`).
