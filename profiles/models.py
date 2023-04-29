from django.db import models
from authentication.models import User
from company.models import Company


class Profile(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    is_frozen = models.BooleanField(default=False) #if user remove from company "staff", it's make 'True'

    def __str__(self):
        return self.nickname