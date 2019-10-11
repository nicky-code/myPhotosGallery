from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    
    return render(request, 'welcome.html',{'image':images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-galleries/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-galleries/search.html',{"message":message})