from time import timezone

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import uuid

from phonenumber_field.modelfields import PhoneNumberField



class CustomUserManager(BaseUserManager):

    def create_user(self, password, email,
                    name, surname,
                    # phone_number,
                    uid
                    ):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.set_name(name)
        user.set_surname(surname)
        # user.set_phone(phone_number)
        user.set_id(uid)
        user.save(using=self._db)
        return user

    def create_superuser(self,  password, email):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # inv_code = models.CharField(max_length=255, null=False, blank=False, help_text="Your invitation code")
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            help_text="Enter your name",
                            default=" ", )

    surname = models.CharField(max_length=255,
                               null=False,
                               blank=False,
                               help_text="Enter your surname",
                               default=" ", )

    # phone_number = PhoneNumberField(blank=True,
    #                                 null=True,
    #                                 unique=True,
    #                                 # default=""
    #                                 )

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255,
                                null=False,
                                blank=False,
                                )

    uid = models.UUIDField(default=uuid.uuid4,
                           editable=False)

    is_staff = models.BooleanField(default=False,
                                   help_text='Designates whether this user can access this admin site.',
                                   verbose_name='is staff')

    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
        verbose_name='is active'
    )
    is_superuser = models.BooleanField(default=False,
                                       help_text=('Designates that this user has all permissions without '
                                                   'explicitly assigning them.'),
                                       verbose_name='is superuser')

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')

    last_login = models.DateTimeField('last login', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'
