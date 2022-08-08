from django.db import models
from django.urls import reverse

# Create your models here.
# from django.contrib.auth.models import User

class Hospital(models.Model):
  name = models.CharField('Hospital Name', max_length=100)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('hospitals')
