
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.TextField(max_length=255, blank=False)
    last_name = models.TextField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    phone_number = models.IntegerField( blank=False)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    alternate_phonenumber = models.IntegerField( blank=True)
    addressline_one = models.CharField(max_length=100, blank=False)
    addressline_two = models.CharField(max_length=100, blank=True)
    country_or_city = models.TextField(max_length=100,default=True, blank=False)
    postalcode = models.CharField(max_length=100, blank=False)
    company_name = models.TextField(max_length=100, blank=True)
    company_type = models.TextField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=False)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_table"
