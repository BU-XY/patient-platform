# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, UserManager


class Patient(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Patient ID
    name = models.CharField(db_column='name', max_length=35) # Patient name
    temp = models.FloatField(db_column='tempreture')         # Tempreture (Celsius)
    pressure = models.IntegerField(db_column='pressure')     # Blood pressure (mmHg)
    pulse = models.FloatField(db_column='pulse')             # Pulse (bpm)
    oximeter = models.FloatField(db_column='oximeter')       # Oximeter (%)
    height = models.FloatField(db_column='height')           # Height (cm)
    weight = models.FloatField(db_column='weight')           # Weight (kg)

    class Meta:
        managed = False
        db_table = 'patient'

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class MyCustomUserManager(BaseUserManager):
    def create_user(self, email_id, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email_id:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyCustomUserManager.normalize_email(email_id),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name=None):
        u = self.create_user(email_id=email, password=password, first_name=first_name, last_name=last_name)
        u.is_superuser = True
        u.is_staff = True
        u.save(using=self._db)
        return u

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, default="female")
    email = models.CharField(max_length=100, primary_key=True)
    phone_number = PhoneNumberField(blank=True)

    objects = MyCustomUserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

