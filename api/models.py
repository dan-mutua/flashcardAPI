from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flashcard(models.Model):
  name=models.ForeignKey(to=User,on_delete=models.CASCADE)
  subject=models.CharField(max_length=200)
  body=models.CharField(max_length=200)
  is_complete=models.BooleanField(default=False)
