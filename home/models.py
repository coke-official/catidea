from django.db import models
from django.conf import settings

class Neko(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nekodo = models.FloatField(default=1000)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=False)
