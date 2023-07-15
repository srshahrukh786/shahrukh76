from django.db import models

# Create your models here.

from users.models import User

class Qualification(models.Model):
    degree = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qualifications')
    
    def __str__(self):
        return self.degree
