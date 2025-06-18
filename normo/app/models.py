from django.db import models

# Create your models here.
class report(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(unique=True)
    
