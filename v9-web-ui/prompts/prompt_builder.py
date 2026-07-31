"""
Prompt Builder

Enterprise RAG System
Version 9

Builds prompts for the LLM.
"""


class PromptBuilder:
    """
    Builds prompts for Retrieval-Augmented Generation.
    """

    def __init__(self):
        pass

    def build_prompt(
        self,
        context: str,
        question: str,
    ) -> str:
        """
        Build the final prompt sent to Gemini.

        Args:
            context (str): Retrieved document context.
            question (str): User question.

        Returns:
            str: Complete prompt.
        """

        if not context.strip():
            context = "No relevant context was retrieved."

        prompt = f"""
You are an intelligent AI assistant.

Answer the user's question ONLY using the provided context.

If the answer cannot be found in the context, clearly say:

"I couldn't find the answer in the provided documents."

Do not make up facts.

-------------------------
CONTEXT
-------------------------

{context}

-------------------------
QUESTION
-------------------------

{question}

-------------------------
ANSWER
-------------------------
"""

        return prompt.strip()