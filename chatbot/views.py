from django.http import JsonResponse
import random
from django.shortcuts import render


def home(request):
    return render(request, 'chatbot/index.html')


def chatbot_response(request):
    user_input = str(request.GET.get('message'))

    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm just code, but I'm doing great!", "All good here!"],
        "bye": ["Goodbye!", "See you later!"]
    }

    for key in responses:
        if key in user_input.lower():
            return JsonResponse({"response": random.choice(responses[key])})

    return JsonResponse({"response": "Sorry, I don't understand that yet."})
