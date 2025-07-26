from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloWorldAPIView(APIView):
    def get(self, request):
        """
        Une fonction qui retourne un message de bienvenue en JSON.
        """
        return Response({"message": "Hello, World!"})
