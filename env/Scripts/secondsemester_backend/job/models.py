from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from django.contrib.auth.models import  AbstractBaseUser

from django.contrib.auth.models import UserManager
from django.utils import timezone

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# from db_connection import db
from djongo import models

# modify
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, Permission
# from job.models import CustomUserManager as User
# Create your models here.

# commented
class Notification(models.Model):
    notification = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-notification',)
    
    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)


class History(models.Model):
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    intent = models.CharField(max_length=255)
    announcement = models.TextField()
    start = models.TimeField(auto_now_add=True)
    end = models.TimeField()
    duration = models.TimeField(max_length=255)
    date_at = models.DateTimeField(auto_now_add=True)
    Total_parking_Slots = models.IntegerField(default=50)
    Vehicles_Parked = models.IntegerField(default=0)
    Available_slots = models.IntegerField(default=50)

    class Meta:
        ordering=('-date_at',)

    def date_formatted(self):
        return defaultfilters.date(self.date_at, 'M d, Y')
    
# end of commented

# commented
class totalSlots(models.Model):
    total_slots = models.IntegerField()
    class Meta:
        ordering=('-total_slots',)

class availableSlots(models.Model):
    available_slots = models.IntegerField()
    class Meta:
        ordering=('-available_slots',)

class parkingSlots(models.Model):
    parking_slots = models.IntegerField()
    class Meta:
        ordering=('-parking_slots',)


# for jairo's db
class real_time(models.Model):
    confidence = models.FloatField()
    plate = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering=('-plate',)
    
    def date_formatted(self):
        return defaultfilters.date(self.date, 'M d, Y')
# end of commented

# added
# for test run
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
# end of testrun
# end of added
    
# for historytab
class historytab(models.Model):
    intent = models.CharField(max_length=255)
    start = models.TimeField(auto_now_add=True)
    end = models.TimeField(auto_now_add=True)
    duration = models.TimeField(auto_now_add=True)
    date_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-date_at',)

    def date_formatted(self):
        return defaultfilters.date(self.date_at, 'M d, Y')


class CustomUserManager(UserManager):
    def _create_user(self, email, password, first_name, last_name, plate, **extra_fields):
        if email:  # Check if email was provided
                    try:
                        validate_email(email)
                    except ValidationError:
                        raise ValueError("Please provide a valid email address")


        # email = email.normalize_email(email)  # Normalize
        user = self.model(email=email, first_name=first_name, last_name=last_name, plate=plate, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_user(self, email='', password=None, first_name='', last_name='', plate='', **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, plate, **extra_fields)

    def create_superuser(self, email='', password=None, first_name='', last_name='', plate='', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, plate, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # email = models.CharField(max_length=255, unique=True)
    email = models.EmailField( unique=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255)
    plate = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'plate']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name