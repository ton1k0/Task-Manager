from django.db import models
from django.utils import timezone
from authentication.models import User
from company.models import Company
from project.models import Project


class GeneralChat(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name='general_chats')


class GeneralMessage(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(GeneralChat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)


class PersonalChat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chats')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    created_at = models.DateTimeField(default=timezone.now)


class PersonalMessage(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(PersonalChat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)



