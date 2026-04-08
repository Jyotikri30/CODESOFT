from difflib import get_close_matches
import random
import time

# Memory
user_name = ""

# Knowledge base
qa_pairs = {
    "what is ai": "AI means Artificial Intelligence.",
    "what is machine learning": "Machine learning is a subset of AI that learns from data.",
    "what is deep learning": "Deep learning uses neural networks with many layers.",
    "what is a neural network": "A neural network mimics how the human brain processes data.",
    "types of chatbot": "There are rule-based chatbots and AI-based chatbots.",
    "what is rule based chatbot": "It works on predefined rules and patterns.",
    "what is ai chatbot": "It uses machine learning and NLP to understand users.",
    "how chatbot works": "A chatbot processes input, finds intent, and returns a response.",
    "how you built this chatbot": "I used Python, rule-based logic, and similarity matching.",
    
}

# Typing effect
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

# Chatbot logic
def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower().strip()
    words = user_input.split()

    # 🔹 Greetings
    if any(word in ["hello", "hi", "hii", "hey"] for word in words):
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help you?"])

    # 🔹 How are you
    if "how are you" in user_input:
        return "I am fine, thank you!  How can I help you?"

    # 🔹 Memory
    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}!"

    if "what is my name" in user_input:
        return f"Your name is {user_name}" if user_name else "I don't know your name yet."

    # 🔹 Thank you
    if "thank" in user_input:
        return "You're welcome! "

    # 🔹 Knowledge
    if "machine learning" in user_input:
        return qa_pairs["what is machine learning"]

    if "deep learning" in user_input:
        return qa_pairs["what is deep learning"]

    if "neural network" in user_input:
        return qa_pairs["what is a neural network"]

    if "ai" in words:
        return qa_pairs["what is ai"]

    # 🔹 Similarity fallback
    matches = get_close_matches(user_input, qa_pairs.keys(), n=1, cutoff=0.8)

    if matches:
        return qa_pairs[matches[0]]

    return "Sorry, I don't understand. Can you rephrase?"

# Main program
print("🤖 AI Chatbot (type 'exit' to stop)\n")

while True:
    user = input("You: ")

    if user.lower() in ["exit", "bye", "quit"]:
        slow_print("Bot: Goodbye! Have a great day ")
        break

    response = chatbot_response(user)
    slow_print("Bot: " + response)