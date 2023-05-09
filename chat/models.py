from django.db import models
from django.utils import timezone
from authentication.models import User
from company.models import Company
from project.models import Project


class Chat(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name='chats')


class Message(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
