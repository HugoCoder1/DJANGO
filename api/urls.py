from django.urls import path, include
from django.contrib import admin
from .views import HelloWorldAPIView

urlpatterns = [
    path("hello/", HelloWorldAPIView.as_view(), name="hello_world"),  # Example endpoint
]
