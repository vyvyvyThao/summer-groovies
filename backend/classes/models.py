from django.db import models
from django.conf import settings
from django.db.models import Q

from datetime import date
from datetime import timedelta


User = settings.AUTH_USER_MODEL

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
    public = models.BooleanField(default=True)

    objects = ClassManager()

    @property
    def end_date(self):
        try:
            return str(self.start_date + timedelta(days=30))
        except:
            return None
    
    # def recover_slots(self, num_slots):
    #     self.slots_remaining += num_slots
    #     return self.slots_remaining