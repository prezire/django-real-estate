from django.db import models
from django.utils import timezone
from realtors.models import Realtor

class Manager(models.Manager):
  def latest_published(self):
    return self.order_by('-listing_date').filter(is_published=True)

class Listing(models.Model):
  objects = Manager()
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y%m%H%M%S')
  photo_1 = models.ImageField(upload_to='photos/%Y%m%H%M%S', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y%m%H%M%S', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y%m%H%M%S', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y%m%H%M%S', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y%m%H%M%S', blank=True)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip_code = models.IntegerField()
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  garage = models.IntegerField(default=0)
  listing_date = models.DateField(default=timezone.now, blank=True)
  is_published = models.BooleanField(default=False)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = 'listings'
  
  def __str__(self):
    return self.title
  
#https://stackoverflow.com/questions/51141769/upload-multiple-images-in-django-admin
# class ListingPhoto(models.Model):
#   listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#   photo = models.ImageField(upload_to='photos/%Y%m%H%M%S')
  #original_filename:str
  #system_filename:str
  #friendly_name:str
  # is_main = models.BooleanField(default=False)
  # created_on = models.DateTimeField(auto_now_add=True)
  # updated_on = models.DateTimeField(auto_now_add=True)
  
  # class Meta:
  #   db_table = 'listing_photos'