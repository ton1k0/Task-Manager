from django.urls import path
from .views import ChatCreateView


urlpatterns = [
    path('create/', ChatCreateView.as_view(), name='create')
]