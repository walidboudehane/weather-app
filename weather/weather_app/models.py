from django.db import models

class Weather(models.Model):
    city=models.CharField(max_length=30)
    
    def __str__(self):
        return self.city
