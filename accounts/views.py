from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from contacts.models import Contact

def register(request):
  if 'POST' == request.method:
    p = request.POST
    fname = p.get('first_name')
    lname = p.get('last_name')
    uname = p.get('username')
    email = p.get('email')
    passwd = p.get('password')
    passwd2 = p.get('password2')
    if passwd == passwd2:
      if User.objects.filter(username=uname).exists():
        messages.error(request, 'Username is taken.')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Email is taken.')
        else:
          User.objects.create_user(username=uname, password=passwd, email=email, first_name=fname, last_name=lname).save()
          messages.success(request, 'You are now registered.')
          return redirect('accounts.login')
    else:
      messages.error(request, 'Passwords do not match.')
    return redirect('accounts.register')
  return render(request, 'accounts/register.html')
  
def login(request):
  if 'POST' == request.method:
    p = request.POST
    uname = p.get('username')
    passwd = p.get('password')
    user = authenticate(username=uname, password=passwd)
    if user:
      auth_login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('accounts.dashboard')
    else:
      messages.error(request, 'Invalid credentials. Please try again.')
      return redirect('accounts.login')
  if request.user.is_authenticated:
    return redirect('accounts.dashboard')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if 'POST' == request.method:
    auth_logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('accounts.login')

def dashboard(request):
  if request.user.is_authenticated:
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    params = {}
    params['accounts_dashboard'] = 'active'
    params['contacts'] = contacts
    return render(request, 'accounts/dashboard.html', params)
  else:
    return redirect('accounts.login')