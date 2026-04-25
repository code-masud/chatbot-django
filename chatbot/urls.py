from django.urls import path
from .views import home, chatbot_response

urlpatterns = [
    path('', home),
    path('get-response/', chatbot_response),
]
