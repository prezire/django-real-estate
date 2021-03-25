from django.db import models
from django.utils import timezone

class Realtor(models.Model):
  full_name = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='photos/%Y%m%dH%M%S')
  description = models.TextField(blank=True)
  email = models.CharField(max_length=50, unique=True)
  phone = models.CharField(max_length=20)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=timezone.now, blank=True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = 'realtors'
  
  def __str__(self):
    return self.full_name