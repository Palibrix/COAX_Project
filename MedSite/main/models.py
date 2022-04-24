import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class user(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, help_text="Enter your name")
    surname = models.CharField(max_length=255, null=False, blank=False, help_text="Enter your surname")
    dateOfBirth = models.DateField(help_text="Pick your birth date")
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(unique=True)
    # language = models.Choices[
    #     ('UA', 'Українська'),
    #     ('EN', 'English'),
    # ]
    inv_code = models.CharField(max_length=255, null=False, blank=False, help_text="Your invitation code")
    uid = uuid.uuid4()

    class Meta:
        db_table = 'users'
# Create your models here.
