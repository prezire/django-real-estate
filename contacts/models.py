from django.db import models
from datetime import datetime

class Contact(models.Model):
  property_name = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  #If logged in.
  user_id = models.IntegerField(blank=True)
  
  class Meta:
    db_table = 'contacts'
  
  def __str__(self):
    return self.name