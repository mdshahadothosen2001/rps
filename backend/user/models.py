from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from utils.models import TimeStamp
from utils.utils import PHONE_REGEX


class UserAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        if username is None or password is None:
            raise ValueError("Username & Password is required")

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin, TimeStamp):
    username = models.CharField(max_length=150, unique=True)
    roll = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_number = models.CharField(
        validators=[PHONE_REGEX], max_length=11, unique=True, null=True, blank=True
    )
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=55, null=True, blank=True)
    last_name = models.CharField(max_length=55, null=True, blank=True)

    class Gender(models.TextChoices):
        male = "male"
        female = "female"
        others = "others"

    gender = models.CharField(
        max_length=10, choices=Gender.choices, null=True, blank=True
    )
    date_of_birth = models.DateField(null=True, blank=True)

    class MaritalStatus(models.TextChoices):
        single = "single"
        married = "married"
        divorced = "divorced"
        widowed = "widowed"
        separated = "separated"
        others = "others"

    marital_status = models.CharField(
        max_length=10, choices=MaritalStatus.choices, null=True, blank=True
    )
    nationality = models.CharField(max_length=25, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    session = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=15, null=True, blank=True)

    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserAccountManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"
        db_table = "user_account"
