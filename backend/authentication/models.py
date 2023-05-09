from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from company.models import Company


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, surname, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, surname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, surname, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname']

    objects = UserManager()