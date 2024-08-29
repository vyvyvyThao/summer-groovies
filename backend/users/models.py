from typing import Iterable
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from classes.models import Class
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
            # password = password,
            birth_year = birth_year,
            facebook_url = facebook_url,
            phone_number = phone_number,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, full_name, birth_year=None, facebook_url=None, phone_number=None, email=None, password=None, **extra_fields):
        user: "User" = self.create_user(
            username=username,
            full_name=full_name,
            birth_year=birth_year,
            facebook_url = facebook_url,
            phone_number = phone_number,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True

        user.save()    
        return user

    def get_queryset(self, *args, **kwargs):
        return UserQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        # return User.objects.filter(username__icontains=query)
        return self.get_queryset().search(query, user=user)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=50)
    birth_year = models.IntegerField(null=True)
    facebook_url = models.URLField(unique=True, null=True)
    phone_number = PhoneNumberField(region="VN", null=True)  
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["full_name", "password", "phone_number"]
    REQUIRED_FIELDS = ["full_name", "password"]

    objects = AccountManager()

    registered_classes = models.ManyToManyField('classes.Class', related_name='students')

    def save(self, **kwargs) -> None:
        # self.set_password(self.password)
        return super().save(**kwargs)

    def register(self, class_title):
        try:
            wish = Class.objects.get(title=class_title)
            print(wish.title)
        except Class.DoesNotExist:
            return "Class not found."
        
        if self in wish.student_list.all():
            return "You already registered."

        if wish.slots_remaining > 0:
            self.registered_classes.add(wish)
            self.save()

            wish.slots_remaining -= 1
            wish.student_list.add(self)
            wish.save()
            return "Registration successful!"
        else:
            return "This class is full."            