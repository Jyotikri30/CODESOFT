import tkinter as tk
from difflib import get_close_matches
import random


user_name = ""


qa_pairs = {
    "what is ai": "AI means Artificial Intelligence.",
    "what is machine learning": "Machine learning is a subset of AI that learns from data.",
    "what is deep learning": "Deep learning uses neural networks with many layers.",
    "what is a neural network": "A neural network mimics how the human brain processes data."
}

# logic
def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower().strip()
    words = user_input.split()

    if any(word in ["hello", "hi", "hii", "hey"] for word in words):
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help you?"])

    if "how are you" in user_input:
        return "I am fine. How can I help you?"

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}!"

    if "what is my name" in user_input:
        return f"Your name is {user_name}" if user_name else "I don't know your name yet."

    if "thank" in user_input:
        return "You're welcome! "

    if "machine learning" in user_input:
        return qa_pairs["what is machine learning"]

    if "deep learning" in user_input:
        return qa_pairs["what is deep learning"]

    if "neural network" in user_input:
        return qa_pairs["what is a neural network"]

    if "ai" in words:
        return qa_pairs["what is ai"]

    matches = get_close_matches(user_input, qa_pairs.keys(), n=1, cutoff=0.8)

    if matches:
        return qa_pairs[matches[0]]

    return "Sorry, I don't understand."

# function
def send_message(event=None):
    user_input = entry.get().strip()

    if user_input == "":
        return

    chatbox.insert(tk.END, "You: " + user_input + "\n")

    response = chatbot_response(user_input)
    chatbox.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)
    chatbox.see(tk.END)

    if user_input.lower() in ["bye", "exit", "quit"]:
        window.after(1000, window.destroy)

# GUI 
window = tk.Tk()
window.title("AI Chatbot ")

# Chat 
chatbox = tk.Text(window, height=20, width=60)
chatbox.pack(padx=10, pady=10)


entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=5)


entry.bind("<Return>", send_message)


button = tk.Button(window, text="Send", command=send_message)
button.pack(pady=5)


window.mainloop()
