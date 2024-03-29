from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_patient(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctor(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    sex = models.BooleanField(default=False)
    dateOfBithday = models.DateTimeField(default=timezone.now)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    role = models.BooleanField(default=False)
    last_result = models.BooleanField(default=False)
    last_result_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False
