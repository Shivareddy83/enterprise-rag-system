"""
Prompt Builder

Enterprise RAG System
Version 7 - RAG Chatbot

Builds prompts for the Large Language Model
using retrieved document context.
"""


class PromptBuilder:
    """
    Builds prompts for the LLM.
    """

    def __init__(self):
        """
        Initialize the Prompt Builder.
        """
        pass

    def build(
        self,
        question: str,
        search_results: dict,
    ) -> str:
        """
        Build the final prompt.

        Args:
            question (str):
                User question.

            search_results (dict):
                Semantic search results.

        Returns:
            str:
                Prompt ready for the LLM.
        """

        documents = search_results.get(
            "documents",
            [[]],
        )[0]

        context = "\n\n".join(documents)

        prompt = f"""
You are an intelligent AI assistant.

Answer the user's question ONLY using the
information provided in the context.

If the answer is not available in the context,
reply exactly:

"I could not find the answer in the provided documents."

------------------------------------------------------------
CONTEXT
------------------------------------------------------------

{context}

------------------------------------------------------------
QUESTION
------------------------------------------------------------

{question}

------------------------------------------------------------
ANSWER
------------------------------------------------------------
"""

        return prompt