from rest_framework import serializers
from .models import GeneralChat, PersonalChat, GeneralMessage, PersonalMessage

class GeneralChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralChat
        fields = '__all__'


class GeneralMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralMessage
        fields = '__all__'


class PersonalChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalChat
        fields = '__all__'


class PersonalMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalMessage
        fields = "__all__"