from prompts.prompt_builder import PromptBuilder

builder = PromptBuilder()

search_results = {
    "documents": [[
        "Python is a programming language.",
        "AI is a branch of computer science."
    ]]
}

prompt = builder.build(
    question="What is AI?",
    search_results=search_results,
)

print(prompt)