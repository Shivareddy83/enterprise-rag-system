"""
LLM Service

Enterprise RAG System
Version 7 - RAG Chatbot

Handles communication with the Gemini API.
"""

from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


class LLMService:
    """
    Handles all interactions with the Gemini API.
    """

    def __init__(self):
        """
        Initialize the Gemini client.
        """

        if not GEMINI_API_KEY:
            raise ValueError(
                "Gemini API Key not found. "
                "Please configure GEMINI_API_KEY in the .env file."
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY,
        )

    def generate_answer(
        self,
        prompt: str,
    ) -> str:
        """
        Generate an answer using Gemini.

        Args:
            prompt (str):
                Prompt sent to the LLM.

        Returns:
            str:
                Generated response.
        """

        try:

            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            return response.text

        except Exception as error:

            raise RuntimeError(
                f"Failed to generate response: {error}"
            )

    def health_check(self) -> bool:
        """
        Verify that the Gemini service is available.

        Returns:
            bool:
                True if the service is reachable,
                otherwise False.
        """

        try:

            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents="Hello",
            )

            return response.text is not None

        except Exception:

            return False