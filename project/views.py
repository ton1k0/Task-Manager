from .serializers import ProjectSerializer
from rest_framework import generics
from .models import Project


class ProjectCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
