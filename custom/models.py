from django.db import models

# Create your models here.
from django.db import models
import pytz
# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=32)

    def __str__(self):
        return self.real_name

    @property
    def activities(self):
        return self.activity_set.all()

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

