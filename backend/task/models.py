from django.db import models
from authentication.models import User
from project.models import Project


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='New') #only 4 options ("new", "in progress", "completed", "postponed")
    priority = models.CharField(max_length=20, default='Low') #only 3 options ("high", "medium", "low")
    due_date = models.DateField()
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')


    def __str__(self):
        return self.title