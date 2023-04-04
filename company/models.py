from django.db import models
from authentication.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)
    web_site = models.TextField(max_length=200)
    owners = models.ManyToManyField(User, related_name='owners_company')
    staff = models.ManyToManyField(User, related_name='staff_company')


    def __str__(self):
        return self.name