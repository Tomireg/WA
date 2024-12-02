from django.db import models
from django.contrib.auth.models import User

class WeatherSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    humidity = models.IntegerField()
    date_searched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.location} searched by {self.user.username} on {self.date_searched}"
