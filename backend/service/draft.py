
from __future__ import annotations
# 서로 다른 프로그램끼리 데이터를 주고받을 때 필요하다. 자바와 파이썬 혹은 백엔드와 프론트엔드에서 필요하다
import json
from typing import Any, Sequence

from ...infra.openai_client import extract_first_json_object, generate_text, generate_text_with_files


def build_examiner_pattern_report_text(
    client: Any,
    model: str,
    *,
    examiner_canonical: str,
    topk_pattern_pack: dict[str, Any],
) -> str:
    """Top-K 패턴을 바탕으로 심사관 패턴 분석 리포트 텍스트 생성."""
    system = (
        "You are a senior patent attorney.\n"
        "Write an examiner pattern analysis based ONLY on TOPK_PATTERN_PACK.\n"
        "Cite application numbers as evidence.\n"
        "Output attorney-grade, actionable guidance."
    )
    user = (
        f"EXAMINER: {examiner_canonical}\n\n"
        f"TOPK_PATTERN_PACK:\n{json.dumps(topk_pattern_pack, ensure_ascii=False, indent=2)[:260_000]}\n\n"
        "Write:\n"
        "1) Patterns in rejections\n"
        "2) Winning argument moves (with App #)\n"
        "3) Winning amendment moves (with App #)\n"
        "4) Checklist/rubric for drafting responses\n"
    )
    return generate_text(client, model, system, user, reasoning_effort="medium")