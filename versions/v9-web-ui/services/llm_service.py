"""
LLM Service

Enterprise RAG System
Version 9

Handles communication with Google Gemini.
"""

import logging

from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)

logger = logging.getLogger("enterprise_rag.llm")


class LLMService:
    """
    Google Gemini Service.
    """

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing from .env"
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = GEMINI_MODEL

        logger.info(
            "Gemini initialized (%s)",
            self.model,
        )

    # ======================================================
    # GENERATE ANSWER
    # ======================================================

    def generate_answer(
        self,
        prompt: str,
    ) -> str:
        """
        Generate an answer using Gemini.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            if (
                response is None
                or response.text is None
            ):
                return "No response generated."

            return response.text.strip()

        except Exception as error:

            logger.exception(
                "Gemini generation failed."
            )

            raise RuntimeError(
                f"LLM Error: {error}"
            )

    # ======================================================
    # HEALTH CHECK
    # ======================================================

    def health_check(self) -> bool:
        """
        Verify Gemini connectivity.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents="Reply with OK",
            )

            return (
                response is not None
                and response.text is not None
            )

        except Exception:

            return False