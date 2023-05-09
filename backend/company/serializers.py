import uuid

from django.utils import timezone
from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    owners = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Company
        fields = ('name', 'web_site', 'owners')


class JoinCompanySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=64)

    def create(self, validated_data):
        company = validated_data['company']
        user = self.context['request'].user
        company.staff.add(user)
        return company


class CompanyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id']

    def to_representation(self, instance):
        user = self.context['request'].user
        company = Company.objects.filter(owners=user, id=self.instance.id).first()
        if not company:
            raise serializers.ValidationError("Вы не являетесь владельцем этой компании.")
        return {'id': instance.id}


class UpdateCompanyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = []

    def update(self, instance, validated_data):
        instance.code = uuid.uuid4().hex[:8]
        instance.code_expiration = timezone.now() + timezone.timedelta(days=7)
        instance.save()
        return instance


