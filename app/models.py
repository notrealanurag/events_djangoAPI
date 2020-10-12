from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import uuid
import os

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Creates & saves a new user"""
        if not email:
            raise ValueError(_('Please enter a valid email address'))
        if not password:
            raise ValueError(_('Please Enter a valid password'))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser):
    """Custom User Model"""
    email = models.EmailField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

def image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/event_img/', filename)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)    
    conducted_by = models.CharField(max_length=100)    
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, upload_to=image_file_path)

    def __str__(self):
        return self.title
