from rest_framework import generics, status
from rest_framework.response import Response
from company.permissions.staff import IsStaff
from company.permissions.owners import IsOwner
from .models import Profile
from .serializers import ProfileSerializer


class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsStaff, IsOwner]
    serializer_class = ProfileSerializer


class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsStaff, IsOwner]
    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        logged_in_user = self.request.user
        profile = Profile.objects.get(user_id=logged_in_user.id)
        instance = profile
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Профиль успешно изменен.', 'profile': serializer.data}, status=status.HTTP_200_OK)