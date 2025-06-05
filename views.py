# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, ChatMessage
from .serializers import ProductSerializer, ChatMessageSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('chat')
        else:
            return render(request, 'chatbot/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chatbot/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def chat_view(request):
    return render(request, 'chatbot/chat.html')

@method_decorator(login_required, name='dispatch')
class ChatbotResponseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get('message', '').lower()
        user = request.user

        if 'laptop' in message:
            products = Product.objects.filter(category__icontains='laptop')
            if products.exists():
                serializer = ProductSerializer(products, many=True)
                response_text = "Here are some laptops you might like:\n"
                for product in serializer.data:
                    response_text += f"- {product['name']}: ${product['price']}\n"
            else:
                response_text = "Sorry, we don't have laptops at the moment."
        else:
            response_text = "I'm here to help you find electronics. What are you looking for?"

        # Save the chat message
        ChatMessage.objects.create(user=user, message=message, response=response_text)

        return Response({'response': response_text}, status=status.HTTP_200_OK)
