from rest_framework import generics, status
from rest_framework.generics import get_object_or_404, DestroyAPIView
from rest_framework.response import Response
from authentication.models import User
from profiles.models import Profile
from .models import Company
from .permission import IsCompanyOwner
from .serializers import CompanySerializer, JoinCompanySerializer, UpdateCompanyCodeSerializer, CompanyOwnerSerializer
from rest_framework.permissions import IsAuthenticated


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        owners = [self.request.user]
        serializer.save(owners=owners)


class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Данные о компании успешно изменены.'}, status=status.HTTP_200_OK)


class CompanyDeleteView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Компания успешно удалена.'}, status=status.HTTP_204_NO_CONTENT)


class UpdateCompanyCodeView(generics.UpdateAPIView):
    serializer_class = UpdateCompanyCodeSerializer
    permission_classes = [IsCompanyOwner]

    def get_object(self):
        user = self.request.user
        serializer = CompanyOwnerSerializer(instance=user, context={'request': self.request})
        company_id = serializer.data['id']
        return Company.objects.get(pk=company_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data) # передаем request.data в качестве аргумента data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Код приглашения обновлен успешно'}, status=status.HTTP_200_OK)



class JoinCompanyAPIView(generics.CreateAPIView):
    serializer_class = JoinCompanySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        code = request.data.get('code')
        company = get_object_or_404(Company, code=code)
        user = request.user
        company.staff.add(user)
        message = "Вы успешно вступили в компанию."
        return Response({'message': message}, status=status.HTTP_200_OK)


class RemoveUserFromCompanyView(DestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsCompanyOwner]

    def delete(self, request, *args, **kwargs):
        company_id = request.data.get('company_id')
        staff_id = request.data.get('staff_id')
        if not company_id or not staff_id:
            return Response({'error': 'company_id and staff_id are required fields'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            staff = User.objects.get(id=staff_id)
        except User.DoesNotExist:
            return Response({'error': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)

        company.staff.remove(staff)
        profile = Profile.objects.get(user=staff.id)
        profile.is_frozen = True
        profile.save()

        return Response(status=status.HTTP_204_NO_CONTENT)