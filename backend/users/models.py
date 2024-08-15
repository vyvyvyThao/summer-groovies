from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserQuerySet(models.QuerySet):
    def search(self, query, user=None):
        # return self.filter(username__icontains=query)
        lookup = Q(title__icontains=query)
        qs = self.filter(lookup)
        
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class AccountManager(BaseUserManager):
    def create_user(self, username, full_name, birth_year, facebook_url, phone_number, email, password):
        if not username:
            raise ValueError("You must have username")
        if not password:
            raise ValueError("You must have password")
        
        user = self.model(
            username = username,
            full_name = full_name,
            password = password,
            birth_year = birth_year,
            facebook_url = facebook_url,
            phone_number = phone_number,
            email = email,
        )

        user.set_password(password)
        user.save(using=self.__db)
        return user
    
    def get_queryset(self, *args, **kwargs):
        return UserQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        # return User.objects.filter(username__icontains=query)
        return self.get_queryset().search(query, user=user)
    

class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    facebook_url = models.URLField(unique=True)
    phone_number = PhoneNumberField(region="VN")  
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username", "full_name", "password", "phone_number"]

    objects = AccountManager()