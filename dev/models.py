from django.db import models
from datetime import datetime

class Image(models.Model):

    pic = models.ImageField()
    time = models.DateTimeField(default =datetime.now())