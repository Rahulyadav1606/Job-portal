# chatbot/urls.py
from django.urls import path
from .views import chat_view, chat_interface

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('interface/', chat_interface, name='chat_interface'),
]
