from django.shortcuts import render
from django.http import request
from listings.models import Listing
from realtors.models import Realtor

def index(request):
  params = {}
  params['pages_index'] = 'active'
  params['listings'] = Listing.objects.latest_published()[:3]
  return render(request, 'pages/index.html', params)
  
def about(request):
  params = {}
  params['pages_about'] = 'active'
  params['realtors'] = Realtor.objects.order_by('-hire_date')
  params['mvp_realtors'] = Realtor.objects.order_by('-hire_date').filter(is_mvp=True)
  return render(request, 'pages/about.html', params)