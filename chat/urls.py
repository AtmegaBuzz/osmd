from django.urls import path
from .views import chat

urlpatterns = [
    path("group/<int:pk>/",chat,name="room")
] 