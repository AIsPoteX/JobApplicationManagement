"""Utilities for fetching company interview briefs via Gemini."""

from __future__ import annotations

from django.conf import settings

try:  # Lazy-import so the rest of the app still runs without the SDK
    import google.generativeai as genai
except ImportError:  # pragma: no cover - optional dependency
    genai = None


class GeminiAPIError(Exception):
    """Raised when Gemini calls fail or are misconfigured."""


def _build_prompt(company_name: str) -> str:
    """Craft a focused prompt for interview prep research."""
    return (
        "You are an interview research assistant. "
        "Generate a concise Chinese brief to help prepare for an interview with the company below. "
        "Use bullet points and keep it under 250 words. "
        "Avoid fabricating data; when unsure, say you could not find public info.\n\n"
        f"Company: {company_name}\n"
        "Required sections: \n"
        "1) 公司的经营理念，社会责任，员工成长培养相关的内容。\n"
        "2) 搜索有关这家公司的“新卒”招聘的“技術職”岗位的实际工作内容 \n"
    )


def fetch_company_brief(company_name: str, *, model_name: str = "gemini-2.5-flash") -> str:
    """Call Gemini with the preset prompt and return the brief text."""
    normalized_name = (company_name or "").strip()
    if not normalized_name:
        raise GeminiAPIError("Company name is required.")

    if genai is None:
        raise GeminiAPIError("google-generativeai is not installed. Run `pip install google-generativeai`.")

    api_key = getattr(settings, "GEMINI_API_KEY", "")
    if not api_key:
        raise GeminiAPIError("GEMINI_API_KEY is not configured.")

    try:
        genai.configure(api_key=api_key)
    except Exception as exc:  # pragma: no cover - defensive guard
        raise GeminiAPIError(f"Failed to configure Gemini: {exc}") from exc

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            _build_prompt(normalized_name),
            generation_config={
                "temperature": 0.6,
                "top_p": 0.9,
                "top_k": 40,
                "max_output_tokens": 5120,
            },
        )
        text = (response.text or "").strip()
    except Exception as exc:  # pragma: no cover - network/SDK errors
        raise GeminiAPIError(f"Gemini request failed: {exc}") from exc

    if not text:
        raise GeminiAPIError("Gemini returned an empty response.")

    return text
