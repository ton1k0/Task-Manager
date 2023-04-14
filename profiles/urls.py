from django.urls import path
from .views import ProfileCreateView, ProfileUpdateView


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile-create'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
]