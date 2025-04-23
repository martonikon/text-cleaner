from langchain_community.llms import GPT4All
import logging

class LocalLLMService:
    def __init__(self, model_path: str):
        self.llm = GPT4All(model=model_path)

    def clean_text(self, text: str) -> str:
        prompt = f"""
You are a highly efficient text-cleaning assistant. 
Remove headers, footers, page numbers, and formatting artifacts (###, ----, \n, etc.). Keep full, coherent sentences.

Now, clean this:
{text}

Cleaned version:
"""
        logging.info("Sending prompt to GPT4All.")
        response = self.llm.invoke(prompt)
        logging.info("Received response from GPT4All.")
        return response.strip()
