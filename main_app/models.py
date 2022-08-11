from telnetlib import STATUS
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# from django.contrib.auth.models import User

DEVICES = (
  ('M', 'Montage'),
  ('N', 'Neuro Combo 1.5mm'),
  ('Q', 'Rib Fix Advantage'),
  ('R', 'Rib Fix Blu'),
  ('S', 'Sternalock Blu'),
  ('T', 'Thin Flap Neuro 1.5mm'),
  ('U', 'Trauma One'),
)

STATUS = (
  ('C', 'Consignment'),
  ('L', 'Loaner'),
)

class Hospital(models.Model):
  name = models.CharField('Hospital Name', max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('hospitals')

class Device(models.Model):
  name = models.CharField(
    max_length=1,
    choices=DEVICES,
    default=DEVICES[0][0]
    )
  status = models.CharField(
    max_length=1,
    choices=STATUS,
    default=STATUS[0][0],
  )
  hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.name)
