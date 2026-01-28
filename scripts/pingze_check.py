#!/usr/bin/env python3
"""
Quick ping/ze helper for Chinese couplets using Modern Mandarin tones (今声).

Usage:
  python scripts/pingze_check.py "上联" "下联"
  python scripts/pingze_check.py "任意一句"

Notes:
  - Requires `pypinyin` (install: python -m pip install pypinyin)
  - This script uses the common heuristic: 1/2=平, 3/4=仄; neutral tone is marked as '?'
  - This does NOT implement classical (旧声/平水韵/入声) classification.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass


_CJK_RE = re.compile(r"[\u4e00-\u9fff]")
_BOUNDARY_CHARS = set("，,；;。.!！？?：:、")


def _extract_chars_and_segment_ends(text: str) -> tuple[list[str], list[int]]:
    """
    Return (cjk_chars, segment_end_indices).

    Segment ends are inferred from common punctuation boundaries in the original text.
    Indices are 0-based positions in cjk_chars.
    """
    chars: list[str] = []
    segment_ends: list[int] = []

    for ch in text:
        if _CJK_RE.match(ch):
            chars.append(ch)
            continue

        if ch in _BOUNDARY_CHARS:
            if chars:
                end_idx = len(chars) - 1
                if not segment_ends or segment_ends[-1] != end_idx:
                    segment_ends.append(end_idx)

    if chars:
        end_idx = len(chars) - 1
        if not segment_ends or segment_ends[-1] != end_idx:
            segment_ends.append(end_idx)

    return chars, segment_ends


def _tone_number(pinyin_with_tone: str) -> int | None:
    if not pinyin_with_tone:
        return None
    last = pinyin_with_tone[-1]
    if last.isdigit():
        num = int(last)
        if 1 <= num <= 5:
            return num
    return None


def _pingze(tone: int | None) -> str:
    if tone in (1, 2):
        return "平"
    if tone in (3, 4):
        return "仄"
    return "?"


@dataclass(frozen=True)
class LineAnalysis:
    raw: str
    chars: list[str]
    pinyin: list[str]
    tones: list[int | None]
    pingze: list[str]
    segment_ends: list[int]

    @property
    def length(self) -> int:
        return len(self.chars)

    @property
    def last_char(self) -> str | None:
        return self.chars[-1] if self.chars else None

    @property
    def last_pingze(self) -> str | None:
        return self.pingze[-1] if self.pingze else None


def analyze_line(text: str) -> LineAnalysis:
    try:
        from pypinyin import Style, lazy_pinyin  # type: ignore
    except ModuleNotFoundError:
        print("Missing dependency: pypinyin", file=sys.stderr)
        print("Install with: python -m pip install pypinyin", file=sys.stderr)
        raise

    chars, segment_ends = _extract_chars_and_segment_ends(text)
    pinyin = lazy_pinyin(chars, style=Style.TONE3, neutral_tone_with_five=True)
    tones = [_tone_number(py) for py in pinyin]
    pingze = [_pingze(t) for t in tones]
    return LineAnalysis(
        raw=text,
        chars=chars,
        pinyin=pinyin,
        tones=tones,
        pingze=pingze,
        segment_ends=segment_ends,
    )


def _fmt_list(items: list[str]) -> str:
    return " ".join(items)


def print_line(label: str, analysis: LineAnalysis) -> None:
    print(f"{label}：{analysis.raw}")
    print(f"字数：{analysis.length}")
    if analysis.chars:
        print(f"逐字：{_fmt_list(analysis.chars)}")
        print(f"拼音：{_fmt_list(analysis.pinyin)}")
        print(f"平仄：{_fmt_list(analysis.pingze)}")
        if len(analysis.segment_ends) > 1:
            ends = [f"{analysis.chars[i]}({analysis.pingze[i]})" for i in analysis.segment_ends]
            print(f"句脚：{_fmt_list(ends)}")
        last = analysis.last_char
        last_pz = analysis.last_pingze
        if last and last_pz:
            print(f"末字：{last}（{last_pz}）")
    print()


def compare(upper: LineAnalysis, lower: LineAnalysis) -> None:
    if upper.length != lower.length:
        print(f"WARNING: 字数不等：上联 {upper.length}，下联 {lower.length}")
        return

    total = upper.length
    ok = 0
    mismatches: list[str] = []
    for idx, (up, down) in enumerate(zip(upper.pingze, lower.pingze), start=1):
        if up == "?" or down == "?":
            mismatches.append(f"{idx}:?/{up}{down}")
            continue
        if (up, down) in (("平", "仄"), ("仄", "平")):
            ok += 1
        else:
            mismatches.append(f"{idx}:{up}{down}")

    print(f"对位平仄相反：{ok}/{total}")

    # Common default preference: 上仄下平 at the last character.
    if upper.last_pingze and lower.last_pingze:
        print(f"末字格：上联末字 {upper.last_pingze}，下联末字 {lower.last_pingze}（常见偏好：上仄下平）")

    if mismatches:
        preview = ", ".join(mismatches[:20])
        suffix = "..." if len(mismatches) > 20 else ""
        print(f"疑似不对位/无法判定（位置:上/下）：{preview}{suffix}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="pingze_check.py",
        description="Modern-Mandarin ping/ze helper for Chinese couplets (requires pypinyin).",
    )
    parser.add_argument("lines", nargs="+", help="1 line or 2 lines (upper then lower)")
    args = parser.parse_args(argv)

    try:
        analyses = [analyze_line(line) for line in args.lines]
    except ModuleNotFoundError:
        return 2

    if len(analyses) == 1:
        print_line("句", analyses[0])
        return 0

    upper = analyses[0]
    lower = analyses[1]
    print_line("上联", upper)
    print_line("下联", lower)
    compare(upper, lower)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
