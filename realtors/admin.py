from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id', 'full_name', 'email', 'hire_date', 'is_mvp')
  list_display_links = ('id', 'full_name', 'email')
  search_fields = ('full_name', 'description', 'email', 'phone', 'is_mvp', 'hire_date')
  list_editable = ('is_mvp',)
  list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)