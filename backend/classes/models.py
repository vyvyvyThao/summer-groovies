from django.db import models
from datetime import date
from datetime import timedelta

# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=120)
    start_date = models.DateField()
    schedule = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=500, default='')
    slots_remaining = models.DecimalField(max_digits=2, decimal_places=0, default=15)

    @property
    def end_date(self):
        try:
            return str(self.start_date + timedelta(days=30))
        except:
            return None
    
    # def recover_slots(self, num_slots):
    #     self.slots_remaining += num_slots
    #     return self.slots_remaining