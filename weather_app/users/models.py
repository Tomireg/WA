from django.db import models
from django.contrib.auth.models import User

class WeatherSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Many-to-one relationship
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    humidity = models.IntegerField()
    search_date = models.DateTimeField(auto_now_add=True)  # Automatically records the time of the search

    def __str__(self):
        return f"{self.user.username}'s search: {self.city_name} on {self.search_date}"
