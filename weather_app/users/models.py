from django.db import models
from django.contrib.auth.models import User

class LastWeatherSearch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    humidity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s last search: {self.city_name}"
