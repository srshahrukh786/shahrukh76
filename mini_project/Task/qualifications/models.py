from django.db import models
from user.models import User

class Qualification(models.Model):
    degree = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qualifications')


# Create your models here.
