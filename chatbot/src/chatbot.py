from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def chatbot(input_text):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate response
    response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)

    # Decode response and return
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text

# Example conversation loop
print("Chatbot: Hello! I'm a simple chatbot. You can start the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
