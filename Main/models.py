from django.db import models

# Create your models here.

class crush(models.Model):
    first=models.EmailField()
    second=models.EmailField()

class pendingcrush(models.Model):
    first=models.EmailField()
    second=models.EmailField()
    verification=models.CharField(max_length=32)

