from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer
from rest_framework.permissions import IsAuthenticated


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        owners = [self.request.user]
        serializer.save(owners=owners)