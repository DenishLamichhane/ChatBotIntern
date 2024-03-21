# main.py


from ConversationalForm import manage_conversation
from GeminiIntegration import GeminiIntegration
from ScheduleCalls import initiate_scheduling
from DataStorage import DataStorage

def main():
    print("Welcome to the Chatbot Application!")

    # Initialize GeminiIntegration with your API key
    gemini_integration = GeminiIntegration("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")

    # Sample documents
    documents = [
        "This is the content of document 1.",
        "Here is document 2.",
        "Document 3 contains relevant information."
    ]

    # Example query
    user_query = "What is document 2 about?"

    # Get response using GeminiIntegration
    response = gemini_integration.answer_query(user_query, documents)
    print("GeminiIntegration Response:", response)

    # Collect user information through conversational form
    manage_conversation()

    # Schedule calls
    initiate_scheduling()

    # Save and read user information from data storage
    storage = DataStorage("user_info.txt")
    user_info = {"name": "Denish", "phone": "9866998742", "email": "denishlamichhane1@example.com"}
    storage.save_user_info(user_info)
    saved_user_info = storage.read_user_info()
    print("Saved User Information:", saved_user_info)

if __name__ == "__main__":
    main()
