# geminiIntegration.py

# Import necessary libraries
#from langchain.models import GPT3Model
#from langchain.pipeline import GeminiPipeline
import GPT3Model

class GeminiIntegration:
    def __init__(self, api_key):
        # Initialize Langchain with GPT-3 model
        self.langchain = Langchain(model=GPT3Model(api_key))#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
        # Initialize Gemini pipeline
        self.gemini = GeminiPipeline(self.langchain)

    def answer_query(self, query, documents):
        # Process the query using Gemini
        response = self.gemini.process_query(query, documents)
        return response

# Example usage
if __name__ == "__main__":
    # Initialize GeminiIntegration with your API key
    gemini_integration = GeminiIntegration("your_api_key")

    # Sample documents
    documents = [
        "This is the content of document 1.",
        "Here is document 2.",
        "Document 3 contains relevant information."
    ]

    # Example query
    user_query = "What is document 2 about?"

    # Get response
    response = gemini_integration.answer_query(user_query, documents)
    print(response)
