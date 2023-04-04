from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    owners = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Company
        fields = ('name', 'web_site', 'owners')