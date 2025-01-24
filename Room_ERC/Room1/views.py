from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
   return render(request, 'Room1/index.html')


def about(request):
    return render(request, 'Room1/foot.html')