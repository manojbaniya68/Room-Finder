from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
   return render(request, 'Room1/index.html')


def about(request):
    return render(request, 'Room1/body.html')

def nav(request):
      return render(request, 'Room1/nav.html')  
  
def signin(request):
      return render(request, 'Room1/signin.html')    
def signup(request):
      return render(request, 'Room1/signup.html') 