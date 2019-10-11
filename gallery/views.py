from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    
    return render(request, 'welcome.html',{'image':images})


