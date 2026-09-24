"""Google Gemini service with lazy, non-fatal configuration."""

import logging

from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL

logger = logging.getLogger("enterprise_rag.llm")


class LLMService:
    def __init__(self, api_key: str | None = GEMINI_API_KEY, model: str = GEMINI_MODEL):
        self.api_key = api_key
        self.model = model
        self.client = genai.Client(api_key=api_key) if api_key else None
        if self.client:
            logger.info("Gemini initialized (%s)", self.model)
        else:
            logger.warning("Gemini is not configured; API is running without LLM connectivity.")

    @property
    def configured(self) -> bool:
        return self.client is not None

    def generate_answer(self, prompt: str) -> str:
        if not self.client:
            raise RuntimeError("Gemini is not configured. Set GEMINI_API_KEY in .env.")
        try:
            response = self.client.models.generate_content(model=self.model, contents=prompt)
            text = getattr(response, "text", None)
            if not text:
                return "No response generated."
            return text.strip()
        except Exception as error:
            logger.exception("Gemini generation failed.")
            raise RuntimeError(f"LLM Error: {error}") from error

    def health_check(self) -> bool:
        if not self.client:
            return False
        try:
            response = self.client.models.generate_content(model=self.model, contents="Reply with OK")
            return bool(response is not None and getattr(response, "text", None))
        except Exception:
            logger.exception("Gemini health check failed.")
            return False
