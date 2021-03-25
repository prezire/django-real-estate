from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Contact

def create(request):
  if 'POST' == request.method:
    p = request.POST
    property_name = p.get('property_name')
    listing_id = p.get('listing_id')
    name = p.get('name')
    email = p.get('email')
    phone = p.get('phone')
    message = p.get('message')
    user_id = p.get('user_id')
    
    #Check existing inquiry.
    if request.user.is_authenticated:
      if Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists():
        messages.error(request, 'You have already made an inquiry on this property.')
        return redirect('listings.read', id=listing_id)
    # else:
    #   if Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists():
    #     messages.error(request, 'You have already made an inquiry on this property.')
    #     return redirect('listings.read', id=listing_id)
    
    Contact(property_name=property_name, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id).save()
    
    f = User.objects.filter
    admins = f(is_staff=True) | f(is_superuser=True)
    recipients = [a.email for a in admins]
    send_mail(
      'Property Listing Inquiry',
      'Inquiry for ' + property_name + '. Sign into the admin panel for more info.',
      settings.EMAIL_HOST_USER,
      recipients,
      fail_silently=False,
    )
    
    messages.success(request, 'Your request has been submitted. A realtor will contact you soon.')
    return redirect('listings.read', id=listing_id)