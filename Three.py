import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')


pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am  Easybot!!.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How can I assist you today?",]
    ],
    [
        r"(.*) your creator ?",
        ["I was developed to assist you.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am just a program, I exist in the cloud!',]
    ],
    [
        r"what (.*) do ?",
        ["I can chat with you and answer simple queries. Try asking me something!",]
    ],
    [
        r"(.*) (help|support) ?",
        ["Sure, I'm here to help! What do you need assistance with?",]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later!", "Exiting..."]
    ],
]


chatbot = Chat(pairs, reflections)


def start_chat():
    print("Hi! I'm your Easybot. Type 'bye' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
