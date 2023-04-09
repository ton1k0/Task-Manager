import uuid
from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=50)
    web_site = models.TextField(max_length=200)
    code = models.CharField(max_length=8, unique=True, default=uuid.uuid4().hex)
    code_expiration = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))
    owners = models.ManyToManyField('authentication.User', related_name='owners_company')
    staff = models.ManyToManyField('authentication.User', related_name='staff_company')


    def __str__(self):
        return self.name
