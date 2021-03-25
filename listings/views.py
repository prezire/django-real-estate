from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import request
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
  listings = Listing.objects.latest_published()
  p = Paginator(listings, 2)
  page = request.GET.get('page')
  paged_listings = p.get_page(page)
  params = {}
  params['listings_index'] = 'active'
  params['listings'] = paged_listings
  return render(request, 'listings/index.html', params)

def read(request, id:int):
  params = {}
  params['listings_read'] = 'active'
  params['listing'] = get_object_or_404(Listing, pk=id)
  print(params['listing'])
  return render(request, 'listings/read.html', params)

def search(request):
  listings = Listing.objects.order_by('-listing_date')
  g = request.GET
  
  if 'keywords' in g:
    keywords = g.get('keywords')
    if keywords:
      listings = listings.filter(description__icontains=keywords)
      
  if 'city' in g:
    city = g.get('city')
    if city:
      listings = listings.filter(city__iexact=city)
      
  if 'state' in g:
    state = g.get('state')
    if state:
      listings = listings.filter(state__iexact=state)
      
  if 'bedrooms' in g:
    bedrooms = g.get('bedrooms')
    if bedrooms:
      listings = listings.filter(bedrooms__lte=int(bedrooms))
      
  if 'price' in g:
    price = g.get('price')
    if price:
      listings = listings.filter(price__lte=int(price))
  
  params = {}
  params['listings_search'] = 'active'
  params['listings'] = listings
  #TODO: Repopulate form.
  #params['form_values'] = g
  return render(request, 'listings/search.html', params)