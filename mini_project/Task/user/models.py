from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=10,null=False,blank=False)


# Create your models here.
