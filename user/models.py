from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from netflixapp.models import Profile
import uuid

# Profile

class CustomUser(AbstractBaseUser, PermissionsMixin):
    TRUE_FALSE_CHOICES = (
        (True, "SIM"),
        (False, "NAO"),
    )
    profiles = models.ManyToManyField(Profile, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(
        max_length=254, null=True, blank=True, unique=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False, choices=TRUE_FALSE_CHOICES)
    is_superuser = models.BooleanField(default=False, choices=TRUE_FALSE_CHOICES)
    

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    objects = UserManager()
