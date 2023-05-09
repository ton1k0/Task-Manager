from rest_framework import serializers
from .models import Project
from company.models import Company


class ProjectSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    class Meta:
        model = Project
        fields = '__all__'