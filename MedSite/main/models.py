import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(models.Model):
    pass
    # name = models.CharField(max_length=255, null=False, blank=False, help_text="Enter your name")
    # surname = models.CharField(max_length=255, null=False, blank=False, help_text="Enter your surname")
    # dateOfBirth = models.DateField(help_text="Pick your birth date")
    # password = models.CharField(max_length=100, null=False, blank=False)
    # phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    # email = models.EmailField(unique=True)
    # # language_choice = models.Choices[
    # #     ('UA', 'Українська'),
    # #     ('EN', 'English'),
    # # ]
    # # language = models.CharField(max_length=1, choices= language_choice, default='UA')
    # inv_code = models.CharField(max_length=255, null=False, blank=False, help_text="Your invitation code")
    # uid = uuid.uuid4()
    #
    # class Meta:
    #     db_table = 'users'
# Create your models here.
