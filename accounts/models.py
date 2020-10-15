from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

