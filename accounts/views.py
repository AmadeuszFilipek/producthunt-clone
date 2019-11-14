from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):

   if request.method == "POST":
      new_username = request.POST['username']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      email = ''

      if password1 == password2:
         try:
            user = User.objects.get(username=new_username)
            return render(request, 'accounts/signup.html', {'error': 'Username taken.'})
         except User.DoesNotExist:
            user = User.objects.create_user(new_username, email, password1)
            auth.login(request, user)
            return redirect('home')
      else:
         return render(request, 'accounts/signup.html', {'error': 'Nonmatching passwords.'})

   else:
      return render(request, 'accounts/signup.html')

def login(request):

   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      
      if user is not None:
         auth.login(request, user)
         return redirect('home')
      else:
         return render(request, 'accounts/login.html', {'error': 'Invalid credentials.'})

   return render(request, 'accounts/login.html')

def logout(request):
   if request.method == "POST":
      auth.logout(request)
      return redirect('home')
