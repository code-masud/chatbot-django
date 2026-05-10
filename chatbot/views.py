import os
import json
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def home(request):
    return render(request, 'chatbot/index.html')


@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        user_message = str(data.get('message'))

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response.choices[0].message.content

        return JsonResponse({
            'response': bot_reply
        })

    return JsonResponse({'error': 'Invalid request'})
