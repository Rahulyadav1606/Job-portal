# chatbot/chatbot.py
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('JobPortalBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with the English corpus
trainer.train("chatterbot.corpus.english")

def get_response(user_input):
    return chatbot.get_response(user_input)
