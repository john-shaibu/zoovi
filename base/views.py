from cmath import pi
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import uploadForm

from .models import Video, User

# Create your views here.
def index(request):

      if request.user.is_authenticated:
              return redirect('dashboard')

      return render(request, 'base/home.html')

def loginPage(request):
      # if request.user.is_authenticated:
      #   return redirect('dashboard')

      if request.method == 'POST':
            email = request.POST.get('email').lower()
            password = request.POST.get('password')

            try:
                  user = User.objects.get(email=email)
            except:
                  # messages.error(request, 'User does not exist')
                  print('user not found')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                  login(request, user)
                  return redirect('home')
            else:
                  messages.error(request, 'Username OR password does not exit')

      return render(request, 'base/login.html')

def registerPage(request):

      if request.method == 'POST':
            # error = None
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            firstname = name.split(' ')[0]
            lastname = name.split(' ')[1]

            print(firstname, lastname)

            try:
                  user_to_check = User.objects.get(email=email)
                  if user_to_check is not None:
                        messages.error(request, 'User already exist!!!')

                  else :
                        u = User.objects.create(
                        first_name = firstname,
                        last_name = lastname,
                        email = email,
                        password = password
                  )
                  print(u)
                  login(request, u)

                  return redirect('home')
            except:
                  User.DoesNotExist

            # if user_to_check is None:      
            #       u = User.objects.create(
            #             first_name = firstname,
            #             last_name = lastname,
            #             email = email,
            #             password = password
            #       )

            #       login(request, u)

            #       return redirect('home')
            # else:
            #       print('error')
            #       messages.error(request, 'unable to create account')

      return render(request, 'base/register.html')

def dashboard(request, pk):

      form = uploadForm(request.POST or None, request.FILES or None)

      user_videos = Video.objects.get(id=pk)

      if request.method =='POST':
            if form.is_valid():
                  form.save()

                  return JsonResponse({'message' : 'Hell yeah!'})

      context = {
            'form' : form,
            'videos': user_videos
      }
                 
      return render(request, 'base/dashboard.html', context)