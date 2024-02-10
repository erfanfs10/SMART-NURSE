from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    MALE = "M"
    FEMALE = "F"
    OTHER= "O"

    GENDER_CHOICES = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHER, "OTHER"),
    )

    CENTER_OWNER = "C"
    NURSE = "N"
    PATIENT = "P"

    ACCESS_CHOICES = (
        (CENTER_OWNER, "CENTER_OWNER"),
        (NURSE, "NURSE"),
        (PATIENT, "PATIENT")
    )

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True, unique=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=5, null=True, blank=True, choices=GENDER_CHOICES)
    access = models.CharField(max_length=5, null=True, blank=True, choices=ACCESS_CHOICES)
    language = models.CharField(max_length=10, null=True, blank=True)
    theme = models.CharField(max_length=10, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, default="default_avatar.png")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        indexes = [models.Index(fields=["username", "email", "phone_number"])]

    def __str__(self) -> str:
        return self.username    
