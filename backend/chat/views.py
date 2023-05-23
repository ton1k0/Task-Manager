from rest_framework import generics
from .models import GeneralChat, PersonalChat, GeneralMessage, PersonalMessage
from .serializers import GeneralChatSerializer, GeneralMessageSerializer, PersonalChatSerializer, PersonalMessageSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions.IsTokenAuthenticated import IsTokenAuthenticated

class GeneralChatCreateView(generics.CreateAPIView):
    queryset = GeneralChat.objects.all()
    serializer_class = GeneralChatSerializer


class PersonalChatCreateView(generics.CreateAPIView):
    queryset = PersonalChat.objects.all()
    serializer_class = PersonalChatSerializer


class ChatHistoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class GeneralChatHistoryAPIView(generics.ListAPIView):
    queryset = GeneralMessage.objects.all()
    serializer_class = GeneralMessageSerializer
    pagination_class = ChatHistoryPagination
    permission_classes = [IsTokenAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return self.queryset.filter(chat_id=chat_id).order_by('-created_at')


class PersonalChatHistoryAPIView(generics.ListAPIView):
    queryset = PersonalMessage.objects.all()
    serializer_class = PersonalMessageSerializer
    pagination_class = ChatHistoryPagination

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return self.queryset.filter(chat_id=chat_id).order_by('-created_at')