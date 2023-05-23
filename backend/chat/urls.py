from django.urls import path, re_path
from .views import GeneralChatCreateView, PersonalChatCreateView, GeneralChatHistoryAPIView, PersonalChatHistoryAPIView


urlpatterns = [
    path('general/create/', GeneralChatCreateView.as_view(), name='general-chat-create'),
    path('personal/create/', PersonalChatCreateView.as_view(), name='personal-chat-create'),
    re_path(r'general-chat/(?P<chat_id>\d+)/history/$', GeneralChatHistoryAPIView.as_view(), name='general-chat-history'),
    re_path(r'personal-chat/(?P<chat_id>\d+)/history/$', PersonalChatHistoryAPIView.as_view(), name='personal-chat-history'),
]