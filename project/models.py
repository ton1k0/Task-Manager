from django.db import models
from authentication.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='participant_projects')
    admins = models.ManyToManyField(User, related_name='admin_projects')
    status = models.CharField(max_length=20, default='Not Started') #only 3 options ("Not Started", "In Progress", "Completed")
    #company_id = models.ForeignKey(Company)


    def __str__(self):
        return self.name