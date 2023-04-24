from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    company = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_company(self, obj):
        return obj.user.company_id