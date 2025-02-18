import random

from django.db import models
from django.conf import settings
from django.db.models import Q

from datetime import date
from datetime import timedelta

# from users.models import User as Student

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ['beginner', 'basic', 'intermediate']

class ClassQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        # lookup = Q(title__icontains=query) | Q(start_date__icontains=query)
        lookup = Q(title__icontains=query)
        qs = self.is_public().filter(lookup)
        
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
    

class ClassManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ClassQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Class(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    start_date = models.DateField()
    schedule = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=500, default='')
    slots_remaining = models.DecimalField(max_digits=2, decimal_places=0, default=15)
    student_list = models.ManyToManyField('users.User', related_name='register_classes')
    public = models.BooleanField(default=True)

    objects = ClassManager()

    @property
    def path(self):
        return f'/classes/{self.pk}/'
    
    def get_absolute_url(self):
        return f'/api/classes/{self.pk}/'
    
    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def body(self):
        return self.description

    def is_public(self) -> bool:
        return self.public 
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    @property
    def end_date(self):
        try:
            return str(self.start_date + timedelta(days=30))
        except:
            return None

        