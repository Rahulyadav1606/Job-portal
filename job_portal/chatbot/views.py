# chatbot/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot import get_response
import json
from django.shortcuts import render

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message')
        bot_response = str(get_response(user_input))
        return JsonResponse({'response': bot_response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# chatbot/views.py


def chat_interface(request):
    return render(request, 'chatbot/chat.html')

